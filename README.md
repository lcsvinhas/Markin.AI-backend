# Markin.AI — Assistente RAG Local com FastAPI + Ollama + Qwen 2.5

Este projeto implementa um assistente de IA utilizando FastAPI, Ollama e a arquitetura RAG (Retrieval Augmented Generation).
O sistema lê arquivos PDF, gera embeddings, cria um banco vetorial e permite fazer perguntas via interface `/docs` da API.

---

## Pré-requisitos

### 1. Python 3.12 (recomendado)

O projeto deve ser executado com Python 3.12 para garantir compatibilidade com todas as bibliotecas utilizadas.

Verifique sua versão:

```powershell
python --version
```

Se aparecer Python 3.12.x, está ok.
O Python 3.14 ainda não possui compatibilidade com todas as libs utilizadas.

Caso não tenha, baixe aqui:
https://www.python.org/downloads/release/python-3120/

---

### 2. Instale o Ollama

Baixe o Ollama conforme seu sistema operacional:
[https://ollama.com/download](https://ollama.com/download)

### 3. Baixe o modelo Qwen 2.5 0.5B

O projeto usa o modelo Qwen 2.5 0.5B:

```powershell
ollama pull qwen2.5:0.5b
```

⚠️ Problema comum: Timeout ao baixar o modelo

Dependendo da sua conexão ou do servidor, o comando acima pode falhar com erro de timeout.
Se isso acontecer, basta executar o comando abaixo, que desabilita o tempo limite:

```powershell
ollama pull qwen2.5:0.5b --timeout 0
```

Isso garante que o download continue até finalizar, mesmo que seja demorado.

---

## Instalação do Projeto

### 1. Crie um ambiente virtual

```powershell
python -m venv .venv
```

### 2. Ative o ambiente virtual e instale as dependências

```powershell
.venv\Scripts\Activate.ps1
    pip install -r requirements.txt
```

---

## Base de Conhecimento

### python --version

Crie a pasta `base/`

Crie uma pasta chamada `base` no diretório raiz e coloque dentro dela todos os PDFs que deseja utilizar como fonte de conhecimento:

```
base/
```

---

## Banco Vetorial

### Gere o banco vetorial

Execute:

```powershell
python criar_db.py
```

Esse script irá:

- Ler os PDFs da pasta `base`
- Gerar embeddings usando Ollama
- Criar um banco vetorial local com ChromaDB

---

## Servidor FastAPI

### Inicie o servidor

```powershell
uvicorn main:app
```

---

## Uso

### Acesse o Swagger UI

Abra no navegador:

```
http://localhost:8000/docs
```

No endpoint disponível, faça sua pergunta para o Markin.AI.
