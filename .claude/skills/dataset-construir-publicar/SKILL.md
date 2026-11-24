---
name: dataset-construir-publicar
description: >-
  Construye, valida y publica datasets JSONL de conocimiento con el CLI `lpdatasets`: exporta desde un
  pack, valida esquema, huellas y particiones, comprueba que la exportación sea reproducible, actualiza
  las cifras de los documentos, construye el índice vectorial, escribe la tarjeta del dataset y deja el
  repositorio en verde. Úsalo cuando el usuario pida "construye el dataset", "exporta <nivel/programa>",
  "publica el dataset", "actualiza las cifras y el índice", "deja el repo de datasets en verde".
  Trabaja en el repositorio learning-path-datasets; para otro repositorio adapta las rutas y los comandos.
  Publicar es una acción pública: confirma con el usuario antes del push si no lo pidió expresamente.
---

# Construir y publicar un dataset

## Prerrequisitos

- Estás en la raíz de `learning-path-datasets`, con el entorno instalado: `pip install -e ".[dev,qdrant]"`.
- Los registros ya pasaron `dataset-verificar` o el usuario aceptó publicar sin esa verificación (deja constancia).
- Conoces la licencia de la fuente y está registrada en `DATA-LICENSE.md`.

## Procedimiento

1. **Exportar** desde un commit fijo de la fuente:
   ```bash
   lpdatasets export --pack <pack> --source <ruta-a-la-fuente> --nivel <nivel> --out datasets
   ```
   Anota el commit de la fuente que quedó en el manifiesto.
2. **Validar**: `lpdatasets validate`. Debe decir `OK`. Si falla, corrige la causa (no edites los JSONL a mano).
3. **Comprobar reproducibilidad**: exporta de nuevo en una carpeta temporal y compara el SHA-256 de `train.jsonl`, `eval.jsonl` y `manifest.json`. Si difieren, hay no determinismo: encuéntralo antes de publicar.
4. **Cifras de los documentos**: `python scripts/docs_stats.py --write` y luego `--check`.
5. **Documentar**: actualiza `CHANGELOG.md`, `STATUS.md` y la tarjeta del dataset (`docs/DATASET_CARD_<pack>.md`) con límites reales: revisión humana, exclusiones, cobertura.
6. **Índice vectorial** (opcional, no se versiona): `lpdatasets index --out .vector` y una búsqueda de prueba con filtros.
7. **Controles locales**: `ruff check src tests scripts`, `ruff format --check src tests scripts`, `pytest`, `python scripts/smoke.py`.
8. **Publicar**: commit con mensaje claro, `git push`, y espera a que CI y Security terminen. Si Security falla por límite de la API de un servicio externo, reintenta con `gh run rerun <id> --failed`; si falla por contenido, corrígelo.
9. **Informar**: tabla con registros por dataset, partición, tipos, estado de CI y límites abiertos.

## Reglas

- **Nunca** versiones índices, entornos virtuales ni archivos de trabajo.
- **Nunca** declares una revisión que no ocurrió; el manifiesto debe reflejar `ia_asistida_sin_revision_humana` mientras sea el caso.
- Un dataset con licencia no comercial lo dice en el README, en la tarjeta y en `DATA-LICENSE.md`.
- No cambies el esquema sin subir la versión del esquema y migrar los datos; añadir valores nuevos de `tipo` es compatible, quitarlos no.
- Si cambias código que afecta la salida, vuelve a exportar **todos** los datasets publicados y confirma que no cambian de forma inesperada.
