# MVP1 - Back-end da API

API REST desenvolvida com Flask, Flask-OpenAPI3 e SQLAlchemy para gerenciamento de clientes e assinaturas.

O projeto disponibiliza endpoints documentados no Swagger e utiliza SQLite como banco de dados local.

---

## Tecnologias utilizadas

- Python 3.10+
- Flask
- Flask-OpenAPI3
- SQLAlchemy
- SQLite

---

## Pré-requisitos

Antes de iniciar, você precisa ter instalado:

- Python 3.10 ou superior
- Pip

---

## Instalação e configuração do ambiente

1. Clone o repositório em https://github.com/cesaracvazs-lab/puc-rio-mvp1-backend.git
2. Acesse a pasta do projeto
3. Crie e ative um ambiente virtual
4. Instale as dependências

### 1) Criar ambiente virtual

No Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

No Linux/Mac:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2) Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Como executar a aplicação

Com o ambiente virtual ativo, execute:

```bash
flask run --host 0.0.0.0 --port 5000
```

---

## Documentação da API

Após iniciar o servidor, acesse no navegador:

- http://localhost:5000/
- http://localhost:5000/openapi

---

## Estrutura resumida do projeto

- `app.py`: ponto de entrada da aplicação
- `src/model`: modelos e configuração do banco
- `src/route`: endpoints da API
- `src/schemas`: schemas de entrada e saída

---

## Observações

- O banco SQLite é criado localmente em `src/database/db.sqlite3`.
- Para reinstalar dependências do zero, recrie o ambiente virtual e rode novamente `pip install -r requirements.txt`.
