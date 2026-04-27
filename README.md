# Markin.AI (RAG com FastAPI + Groq + Llama 3.3)

> Componente back-end oficial do Markin.AI, responsável por processamento de conhecimento, pipelines de ingestão, RAG, governança e exposição de APIs para o widget e integrações corporativas.

Este repositório complementa o front-end do Markin.AI e fornece toda a base inteligente que transforma documentos em respostas estruturadas, contextualizadas e auditáveis.

---

## Rodando com Docker

Não é necessário instalar Python, criar ambientes virtuais ou rodar scripts manualmente. Apenas:

**1.** Coloque seus PDFs na pasta `base/`

**2.** Renomeie o arquivo `.env.exemplo` para `.env` e preencha com sua chave Groq (obtenha gratuitamente em https://console.groq.com/keys):

```
GROQ_API_KEY=sua_chave_aqui
```

**3.** Suba a aplicação:

```bash
docker compose up
```

> A primeira execução é demorada: a imagem é construída, as dependências são instaladas, o modelo de embeddings é baixado e o banco vetorial é criado a partir dos PDFs. As execuções seguintes são bem mais rápidas.

---

📚 **Sumário**

1. [Visão Geral](#visão-geral)
2. [Arquitetura do Produto](#arquitetura-do-produto)
3. [Documentação e Materiais](#documentação-e-materiais)
4. [Como rodar o projeto](#como-rodar-o-projeto)
5. [Front-end (Typescript / React)](https://github.com/lcsvinhas/Markin.AI-frontend)
6. [Equipe](#equipe)
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
- Integração com Groq API
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
- **Groq API**
- **Llama 3.3 70B**
- **LangChain**
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

```bash
python --version
```

Se aparecer Python 3.12.x, está ok.

Caso não tenha, baixe aqui:
https://www.python.org/downloads/release/python-3120/

---

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

---

### Como rodar o projeto

#### 1. Adicione seus PDFs

Coloque dentro da pasta `base/` todos os PDFs que serão indexados pelo Markin.AI:

```
base/
├── documento1.pdf
├── documento2.pdf
└── ...
```

#### 2. Configure a chave de API

O repositório inclui um arquivo `.env.example` com o formato esperado. Renomeie-o para `.env` e substitua pelo valor real da sua chave Groq (obtenha gratuitamente em https://console.groq.com/keys):

```bash
cp .env.example .env
```

```
GROQ_API_KEY=sua_chave_aqui
```

#### 3. Suba com Docker

```bash
docker compose up
```

> Na primeira execução o processo demora mais: a imagem é construída, as dependências são instaladas, o modelo de embeddings é baixado e o banco vetorial é criado a partir dos PDFs. As execuções seguintes são bem mais rápidas.

---

#### Alternativa: rodar sem Docker

<details>
<summary>Expandir instruções para rodar localmente</summary>

Crie e ative o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\Activate.ps1  # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Crie o banco vetorial:

```bash
python criar_db.py
```

Suba o servidor:

```bash
uvicorn main:app
```

</details>

---

### Uso

#### Acesse o Swagger UI

Abra no navegador:

```
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
