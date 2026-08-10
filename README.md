# DMP

Aplicação offline-first para gestão de uma papelaria. O projeto é um monólito
modular: Streamlit apresenta a aplicação localmente, as regras permanecem em
Python e o estado persistido pertence ao SQLite no computador da loja.

## Estrutura

```text
src/dmp/
  domain/       Entidades, valores e regras de negócio puras
  application/  Casos de uso e portas para dependências externas
  data/         Implementações de persistência SQLite e migrações
  ui/           Entrypoint e componentes de apresentação Streamlit
docs/
  ARCHITECTURE.md  Limites, dependências e entradas do projeto
```

Os limites entre os módulos estão descritos em
[`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md). Regras de domínio e casos de uso
não podem importar componentes Streamlit.

## Entrypoints

O entrypoint local é `src/dmp/ui/app.py`.

A suíte de testes será executada a partir da raiz com:

```bash
uv run pytest
```

## Desenvolvimento local

Crie o ambiente reproduzível e instale as dependências de desenvolvimento com:

```bash
uv sync --locked --dev
```

Inicie a aplicação apenas no computador local com:

```bash
uv run streamlit run src/dmp/ui/app.py --server.address localhost
```

Execute a quality gate a partir da raiz do repositório:

```bash
uv run ruff format --check .
uv run ruff check .
uv run mypy .
uv run pytest
```
