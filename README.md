## spot-render-cli

> **PT-BR:** CLI em Python que facilita uploads locais para a API do Spot Render. Armazena o nome do funcionário em `~/.spotrender/config`, envia arquivos com metadados e mostra o status do job.

> **EN:** Python CLI that simplifies local uploads to the Spot Render API. Stores the artist name in `~/.spotrender/config`, uploads files with metadata and prints job info.

### Uso

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
spotrender --file model.blend --project sky-tower --variation v1
```

### Estrutura

```
spotrender/
  __init__.py
  config.py
  client.py
pyproject.toml
```

### CI

`.github/workflows/ci.yml` executa lint (ruff), pytest e gera artefato para publicação futura no PyPI interno.
