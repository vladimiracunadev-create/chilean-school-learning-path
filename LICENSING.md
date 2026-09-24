# Política maestra de licenciamiento

## Modelo por capas

| Capa | Regla |
|---|---|
| Software original | MIT |
| Contenido educativo original | CC BY-NC-SA 4.0 |
| Datos/metadatos | licencia específica por dataset |
| Terceros | licencia original |
| Licencia desconocida | cuarentena / no redistribuir |
| Marca y logos | fuera del alcance automático de MIT/CC |
| Datos personales/secretos | no publicar |

## Software

`LICENSE` aplica al **software original del proyecto**, salvo declaración específica distinta.
Esto incluye normalmente `src/`, `app/`, `api/`, `scripts/`, `tests/`, `tools/`,
`school_knowledge/`, `cli/`, `frontend/` y `backend/`.

SPDX recomendado: `SPDX-License-Identifier: MIT`.

No conviene limitar MIT únicamente a `scripts/` y `tests/` si existen otros directorios de
software.

## Contenido educativo

`LICENSE-CONTENT.md` aplica al contenido original de `curriculum/`, `classes/`, `lessons/`,
`actividades/`, `activities/`, `rubrics/`, `cases/`, `guides/`, `training/` y equivalentes,
salvo aviso específico.

## Datos

Los datasets no heredan automáticamente MIT o CC por vivir en el repositorio. Deben declarar
procedencia, licencia, restricciones, fecha y permisos de redistribución/derivación.

## Terceros

Libros, papers, textos escolares, imágenes, videos, recursos MINEDUC/BCN, datasets, modelos,
pesos de IA y software externo conservan sus derechos y licencias originales.

## IA

Antes de publicar contenido asistido por IA:
1. conservar fuentes;
2. evitar reproducción sustancial de material protegido;
3. separar citas de redacción original;
4. revisar código, imágenes y datasets por separado.

## Precedencia

1. licencia específica del archivo/directorio;
2. software original → MIT;
3. contenido educativo original → CC BY-NC-SA 4.0;
4. datos → `DATA-LICENSE.md`;
5. terceros → licencia original;
6. origen/licencia desconocidos → no redistribuir.

## Licenciamiento dual

La versión comunitaria puede permanecer bajo CC BY-NC-SA 4.0 y el titular conceder una licencia
comercial independiente a empresas o instituciones.

> Política operativa; no sustituye asesoría jurídica individual.
