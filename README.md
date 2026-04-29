# Markin.AI — Back-end (RAG com FastAPI + Groq + Llama 3.3)

> Componente back-end oficial do Markin.AI, responsável por processamento de conhecimento, pipelines de ingestão, RAG, governança e exposição de APIs para o widget e integrações corporativas.

Este repositório complementa o front-end do Markin.AI e fornece toda a base inteligente que transforma documentos em respostas estruturadas, contextualizadas e auditáveis.

---

## 📚 Sumário

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Produto](#arquitetura-do-produto)
3. [Tecnologias](#tecnologias)
4. [Configuração inicial](#configuração-inicial)
5. [Rodando o projeto](#rodando-o-projeto)
6. [Uso](#uso)
7. [Documentação e Materiais](#documentação-e-materiais)
8. [Front-end](#front-end)
9. [Equipe](#equipe)

---

## Visão Geral

O **Markin.AI** implementa pipelines de ingestão e normalização de conhecimento a partir de PDFs, com:

- Redação de PII (dados sensíveis)
- Extração de metadados
- Geração de embeddings
- Construção do banco vetorial
- RAG (Retrieval Augmented Generation)
- API REST com FastAPI
- Integração com Groq API
- Respostas otimizadas para o widget e integrações externas

Este back-end funciona tanto para:

- Ambientes corporativos on-premise
- Versão SaaS / cloud
- Integrações white-label
- Ambientes locais de desenvolvimento

---

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
                | Llama 3.3 70B • Groq API      |
                |       • LangChain             |
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

---

## Tecnologias

- **FastAPI**
- **Python 3.12**
- **Groq API**
- **Llama 3.3 70B**
- **LangChain**
- **ChromaDB**
- **Pydantic**
- **Uvicorn**

Arquitetura baseada em *features* e componentes reutilizáveis.

---

## Configuração inicial

Antes de subir o projeto (com Docker ou localmente), faça os dois passos abaixo:

**1.** Coloque seus PDFs na pasta `base/`:

```
base/
├── documento1.pdf
├── documento2.pdf
└── ...
```

**2.** Renomeie o arquivo `.env.exemplo` para `.env` e preencha com sua chave Groq (obtenha gratuitamente em https://console.groq.com/keys):


```env
GROQ_API_KEY=sua_chave_aqui
```

---

## Rodando o projeto

Você pode rodar o Markin.AI de duas formas: com **Docker** (recomendado) ou **localmente** com Python.

### 🐳 Com Docker

Não é necessário instalar Python, criar ambientes virtuais ou rodar scripts manualmente. Apenas suba a aplicação:

```bash
docker compose up
```

> ⏳ A primeira execução é demorada: a imagem é construída, as dependências são instaladas, o modelo de embeddings é baixado e o banco vetorial é criado a partir dos PDFs. As execuções seguintes são bem mais rápidas.

### 💻 Localmente (sem Docker)

<summary>Expandir instruções para rodar localmente</summary>

#### 1. Python 3.12 (obrigatório)

O projeto deve ser executado com Python 3.12 para garantir compatibilidade com todas as bibliotecas utilizadas.

Verifique sua versão:

```bash
python --version
```

Caso não tenha, baixe em: https://www.python.org/downloads/release/python-3120/

#### 2. Crie e ative o ambiente virtual

```bash
python -m venv .venv
```

Linux / macOS:
```bash
source .venv/bin/activate
```

Windows:
```powershell
.venv\Scripts\Activate.ps1
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Crie o banco vetorial

```bash
python criar_db.py
```

#### 5. Suba o servidor

```bash
uvicorn main:app
```

---

## Uso

Com o servidor rodando, acesse o **Swagger UI** no navegador:

```
http://localhost:8000/docs
```

A interface permitirá:

- Enviar perguntas
- Testar endpoints
- Visualizar respostas do RAG
- Inspecionar o fluxo de consulta

---

## Documentação e Materiais

Documentos estratégicos e técnicos do projeto:

- 📌 **Estrutura do Case** — [/docs/estrutura-do-case.md](https://github.com/lcsvinhas/Markin.AI-frontend/blob/main/docs/estrutura-do-case.md)
- 📌 **Levantamento Inicial** — [/docs/CopilotoAI_Levantamento_Inicial.md](https://github.com/lcsvinhas/Markin.AI-frontend/blob/main/docs/CopilotoAI_Levantamento_Inicial.md)
- 📌 **Soluções, Mitigações e Viabilidade** — *(em breve)*

---

## Front-end

O front-end (TypeScript / React) está disponível em:
👉 [Markin.AI-frontend](https://github.com/lcsvinhas/Markin.AI-frontend)

---

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
