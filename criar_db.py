import os
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

PASTA_BASE = "base"
DB_DIR = "db"
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 500
BATCH_SIZE = 100


def _carregar_pdf(caminho: Path):
    return PyPDFLoader(str(caminho), extract_images=False).load()


def carregar_documentos():
    arquivos = sorted(Path(PASTA_BASE).glob("*.pdf"))
    if not arquivos:
        print(f"Nenhum PDF encontrado em '{PASTA_BASE}'")
        return []

    print(f"Carregando {len(arquivos)} arquivo(s) em paralelo...")
    documentos = []
    with ThreadPoolExecutor() as executor:
        futuros = {executor.submit(_carregar_pdf, f): f for f in arquivos}
        for futuro in as_completed(futuros):
            nome = futuros[futuro].name
            try:
                documentos.extend(futuro.result())
                print(f"  OK  {nome}")
            except Exception as e:
                print(f"  ERRO {nome}: {e}")

    print(f"{len(documentos)} pagina(s) carregada(s)")
    return documentos


def dividir_chunks(documentos):
    separador = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,
    )
    chunks = separador.split_documents(documentos)
    print(f"{len(chunks)} chunks gerados")
    return chunks


def vetorizar_chunks(chunks):
    try:
        import torch
        device = "cuda" if torch.cuda.is_available() else "cpu"
    except ImportError:
        device = "cpu"

    print(f"Carregando modelo de embeddings (device: {device})...")
    embeddings = HuggingFaceEmbeddings(
        model_name="nomic-ai/nomic-embed-text-v1.5",
        model_kwargs={"trust_remote_code": True, "device": device},
        encode_kwargs={"batch_size": 64, "normalize_embeddings": True},
    )

    if os.path.exists(DB_DIR):
        shutil.rmtree(DB_DIR)

    total_lotes = (len(chunks) + BATCH_SIZE - 1) // BATCH_SIZE
    print(f"Inserindo {len(chunks)} chunks em {total_lotes} lote(s)...")

    db = None
    for i in range(0, len(chunks), BATCH_SIZE):
        lote = chunks[i:i + BATCH_SIZE]
        lote_num = i // BATCH_SIZE + 1
        print(f"  Lote {lote_num}/{total_lotes} ({len(lote)} chunks)...")
        if db is None:
            db = Chroma.from_documents(lote, embedding=embeddings, persist_directory=DB_DIR)
        else:
            db.add_documents(lote)

    print("Banco criado com sucesso!")


def criar_db():
    documentos = carregar_documentos()
    if not documentos:
        return
    chunks = dividir_chunks(documentos)
    vetorizar_chunks(chunks)


criar_db()
