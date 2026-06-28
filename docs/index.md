# Spot Render CLI – TechDocs

## Objetivo
CLI oficial para técnicos/artistas enviarem arquivos e render lists diretamente à API, persistindo o nome do funcionário localmente.

## Uso rápido
```
spotrender --file scene.blend --project mall --variation night
spotrender --file scenes.zip --renderlist render-list.xlsx --project sky --set-default --username admin --password admin
```

## Estrutura
```
spotrender/
  config.py
  client.py
pyproject.toml
```

## Configuração
- Config é salva em `~/.spotrender/config.json`.  
- Para redefinir o artista: `rm ~/.spotrender/config.json` ou `spotrender --reset` (implementar conforme issue #2).

## Métricas/Alertas
- CLI apenas encaminha eventos para a API (`render_requests_total`).  
- Para instrumentar a própria CLI (ex.: contagem local), utilize OpenTelemetry + exporter ou envie eventos para um endpoint `/cli-metrics`.

## Teste local
- `pip install -e .`  
- `pytest` executa os testes.
- Para e2e, use `spot-render-teste-local` e aponte `--api http://spot-render-api.spot-render.svc.cluster.local:8000`.

## TechDocs / Backstage
- `mkdocs.yml` aponta para este documento.
