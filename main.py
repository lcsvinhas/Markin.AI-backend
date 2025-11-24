from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from langchain_ollama import OllamaLLM
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

MODEL_NAME = "qwen2.5:0.5b"
DB_DIR = "db"
MAX_CONTEXT_CHARS = 3500

embeddings = HuggingFaceEmbeddings(
    model_name="nomic-ai/nomic-embed-text-v1.5",
    model_kwargs={"trust_remote_code": True}
)

db = Chroma(
    persist_directory=DB_DIR,
    embedding_function=embeddings
)

llm = OllamaLLM(
    model=MODEL_NAME,
    streaming=True
)

app = FastAPI(
    title="Markin.AI",
    description="Faça sua pergunta para o Markin.AI e receba respostas baseadas na base de conhecimento interna.",
)


class PerguntaInput(BaseModel):
    pergunta: str


@app.post(
    "/perguntar",
    summary="Pergunte algo ao Markin.AI",
    description="Envie qualquer pergunta e o Markin.AI responderá com base nos documentos carregados no sistema."
)
async def perguntar(req: PerguntaInput):

    resultados = db.similarity_search(req.pergunta, k=3)

    if not resultados:
        return {"resposta": "Não encontrei essa informação."}

    contexto = "\n".join([r.page_content[:1200] for r in resultados])
    contexto = contexto[:MAX_CONTEXT_CHARS]

    prompt = f"""
    Responda somente com base no CONTEXTO.  
    Se não houver resposta, diga: "Não encontrei essa informação."

    CONTEXTOS:
    {contexto}

    PERGUNTA:
    {req.pergunta}

    RESPOSTA:
    """.strip()

    def gerar_resposta():
        for token in llm.stream(prompt):
            yield token

    return StreamingResponse(gerar_resposta(), media_type="text/plain")
