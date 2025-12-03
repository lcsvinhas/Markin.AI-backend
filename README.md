# Markin.AI (RAG Local com FastAPI + Ollama + Qwen 2.5)

> Componente back-end oficial do Markin.AI, responsável por processamento de conhecimento, pipelines de ingestão, RAG, governança e exposição de APIs para o widget e integrações corporativas.

Este repositório complementa o front-end do Markin.AI e fornece toda a base inteligente que transforma documentos em respostas estruturadas, contextualizadas e auditáveis.

📚 **Sumário**

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Produto](#arquitetura-do-produto)
3. [Documentação e Materiais](#documentação-e-materiais)
4. [Front-end (Typescript / React)](https://github.com/lcsvinhas/Markin.AI-frontend)
5. [Equipe](#equipe)
   <br><br>

## Visão Geral

O **Markin.AI** implementa:

Pipelines de ingestão e normalização de conhecimento (PDFs)

- Redação de PII (dados sensíveis)
- Extração de metadados
- Geração de embeddings
- Construção do banco vetorial
- RAG (Retrieval Augmented Generation)
- API REST com FastAPI
- Integração direta com Ollama
- Respostas otimizadas para o widget e integrações externas

Este back-end funciona tanto para:

- Ambientes corporativos on-premise
- Versão SaaS / cloud
- Integrações white-label
- Ambientes locais de desenvolvimento
  <br><br>

## Arquitetura do Produto

```plaintext

                     +---------------------+
                     |      Front-end      |
                     |     (React + TS)    |
                     +----------+----------+
                                |
                                v
           +-------------------------------------------+
           |                  API Layer                |
           |  FastAPI • Auth • Logs • Auditoria • PII  |
           +--------------------+----------------------+
                                |
                                v
                +-------------------------------+
                |   Motor de RAG + Embeddings   |
                |   Qwen 2.5 • LangChain        |
                +--------------+----------------+
                               |
                               v
                +-------------------------------+
                |  Pipelines de Ingestão        |
                |  PDFs • Normalização • PII    |
                +--------------+----------------+
                               |
                               v
                +-------------------------------+
                |  Base de Conhecimento         |
                |  (Embeddings + Metadados)     |
                +-------------------------------+

```

<br><br>

## Documentação e Materiais

Aqui você encontra todos os documentos estratégicos e técnicos do projeto.

📌 Estrutura do Case<br>
👉 [/docs/estrutura-do-case.md](https://github.com/lcsvinhas/Markin.AI-frontend/blob/main/docs/estrutura-do-case.md)

📌 Levantamento Inicial<br>
👉 [/docs/levantamento-inicial.md](https://github.com/lcsvinhas/Markin.AI-frontend/blob/main/docs/CopilotoAI_Levantamento_Inicial.md)

📌 Soluções, Mitigações e outros dados para a viabilidade<br>
👉 [/docs/levantamento-inicial.md](#)
<br><br>

## Markin.AI Back-end

Tecnologias utilizadas:

- **FastAPI**
- **Python 3.12**
- **Ollama**
- **Qwen 2.5 (0.5B)**
- **LangChain / LlamaIndex**
- **ChromaDB**
- **Pydantic**
- **Uvicorn**
  <br>

Arquitetura baseada em _features_ e componentes reutilizáveis
<br>

### Instalação

#### 1. Python 3.12 (recomendado)

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

#### 2. Instale o Ollama

Baixe o Ollama conforme seu sistema operacional:
[https://ollama.com/download](https://ollama.com/download)

#### 3. Baixe o modelo Qwen 2.5 0.5B

O projeto usa o modelo Qwen 2.5 0.5B:

```powershell

ollama pull qwen2.5:0.5b

```

Se der timeout:

```powershell

ollama pull qwen2.5:0.5b --timeout 0

```

### Instalação do Projeto

#### 1. Crie um ambiente virtual

```powershell

python -m venv .venv

```

#### 2. Ative o ambiente virtual e instale as dependências

```powershell

.venv\Scripts\Activate.ps1
    pip install -r requirements.txt

```

### Pipelines de Ingestão e Banco Vetorial

#### 1. Crie a pasta de base

```powershell

base/

```

Coloque dentro dela todos os PDFs que serão indexados no Markin.AI.

#### 2. Gere o banco vetorial

Execute:

```powershell

python criar_db.py

```

Esse script irá:

- Ler os PDFs da pasta `base`
- Gerar embeddings usando Ollama
- Criar um banco vetorial local com ChromaDB

---

### Servidor FastAPI

#### 1. Inicie o servidor

```powershell

uvicorn main:app

```

### Uso

#### 1. Acesse o Swagger UI

Abra no navegador:

```powershell

http://localhost:8000/docs

```

A interface Swagger UI permitirá:

- Enviar perguntas
- Testar endpoints
- Visualizar respostas do RAG
- Inspecionar o fluxo de consulta

## Equipe

<table align="center">
  <tr>
    <td align="center">
      <a href="https://github.com/lcsvinhas">
        <img src="https://avatars.githubusercontent.com/u/179336216?v=4" width="100px;" alt="Avatar Lucas Vinhas"/><br>
        <sub><b>Lucas Vinhas</b></sub>
      </a>
      <br><br>
      <a href="https://www.linkedin.com/in/lucas-vinhas-/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/pckzin01">
        <img src="https://avatars.githubusercontent.com/u/177571525?v=4" width="100px;" alt="Avatar Patrick Paiva"/><br>
        <sub><b>Patrick Paiva</b></sub>
      </a>
      <br><br>
      <a href="https://www.linkedin.com/in/patrick-gon%C3%A7alves-66621b1b9/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
      </a>
    </td>
    <td align="center">
      <a href="https://github.com/thaiscardosodemello">
        <img src="https://avatars.githubusercontent.com/u/14929797?v=4" width="100px;" alt="Avatar Thais Cardoso"/><br>
        <sub><b>Thais Cardoso</b></sub>
      </a>
      <br><br>
      <a href="https://www.linkedin.com/in/thais-cardoso-de-mello/" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
      </a>
    </td>
  </tr>
</table>
