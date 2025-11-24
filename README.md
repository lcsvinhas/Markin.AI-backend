# Markin.AI — Assistente RAG Local com FastAPI + Ollama + Qwen 2.5

Este projeto implementa um assistente de IA utilizando FastAPI, Ollama e a arquitetura RAG (Retrieval Augmented Generation).
O sistema lê arquivos PDF, gera embeddings, cria um banco vetorial e permite fazer perguntas via interface `/docs` da API.

---

## Pré-requisitos

### 1. Instale o Ollama

Baixe o Ollama conforme seu sistema operacional:
[https://ollama.com/download](https://ollama.com/download)

### 2. Baixe o modelo Qwen 2.5 0.5B

O projeto usa o modelo Qwen 2.5 0.5B:

```bash
ollama pull qwen2.5:0.5b
```

---

## Instalação do Projeto

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

### 4. Ative o ambiente virtual e instale as dependências

```bash
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

---

## Base de Conhecimento

### 5. Crie a pasta `base/`

Crie uma pasta chamada `base` no diretório raiz e coloque dentro dela todos os PDFs que deseja utilizar como fonte de conhecimento:

```
base/
```

---

## Banco Vetorial

### 6. Gere o banco vetorial

Execute:

```bash
python criar_db.py
```

Esse script irá:

* Ler os PDFs da pasta `base`
* Gerar embeddings usando Ollama
* Criar um banco vetorial local com ChromaDB

---

## Servidor FastAPI

### 7. Inicie o servidor

```bash
uvicorn main:app
```

---

## Uso

### 8. Acesse o Swagger UI

Abra no navegador:

```
http://localhost:8000/docs
```

No endpoint disponível, faça sua pergunta para o Markin.AI.
