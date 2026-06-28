## spot-render-cli

> **PT-BR:** CLI em Python que facilita uploads locais para a API do Spot Render. Armazena o nome do funcionário em `~/.spotrender/config`, envia arquivos com metadados e mostra o status do job.

> **EN:** Python CLI that simplifies local uploads to the Spot Render API. Stores the artist name in `~/.spotrender/config`, uploads files with metadata and prints job info.

### Uso

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
spotrender --file model.blend --project sky-tower --variation v1
```

### Tecnologias
- Python 3.12 + Click  
- Requests (HTTP)  
- Config local (`~/.spotrender/config`)  
- GitHub Actions (lint/test)  
- Publicação opcional em PyPI interno.

### Render lists
- Use `--renderlist render-list.xlsx` para anexar uma render list específica ao upload.  
- Para atualizar a lista padrão, use `--set-default --username admin --password admin` (ambiente de teste). Em produção, configure credenciais via Secrets Manager/CLI.

### Métricas e alertas
- O CLI envia eventos para a API, que incrementa `render_requests_total{source="cli"}`.  
- Para adicionar novos eventos, adapte `spotrender/client.py` para enviar cabeçalhos extras ou chamar um endpoint dedicado.  
- Alertas seguem a camada API (veja `spot-render-observability`).

### Testes locais
- `pytest` roda testes unitários da CLI.  
- Para e2e, use o repositório [`spot-render-teste-local`](https://github.com/raafa001/spot-render-teste-local) e aponte `--api http://spot-render-api.spot-render.svc.cluster.local:8000`.

### TechDocs
- Consulte `docs/index.md` + `mkdocs.yml` para a documentação utilizada no Backstage.

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
