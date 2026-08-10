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

O entrypoint local será executado com:

```bash
uv run streamlit run src/dmp/ui/app.py --server.address localhost
```

A suíte de testes será executada a partir da raiz com:

```bash
uv run pytest
```

O ambiente `uv` e os comandos de qualidade serão configurados no card MPJ-50.
