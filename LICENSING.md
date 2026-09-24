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

## Respuesta rápida

- Si es **código original**, aplica MIT y se conserva el aviso de licencia.
- Si es una **clase, tarea, actividad, guía o rúbrica original**, aplica CC BY-NC-SA 4.0.
- Si es un **dato o metadato**, se revisa `DATA-LICENSE.md` y su procedencia.
- Si es una **obra o recurso externo**, conserva la licencia de su titular; un enlace no concede permiso para copiar.
- Si no puede determinarse la licencia, no se redistribuye.

## Software

`LICENSE` aplica al **software original del proyecto**, salvo declaración específica distinta.
En este repositorio incluye `scripts/`, `tests/`, `site/app.js` y el código funcional original,
salvo aviso específico distinto.

SPDX recomendado: `SPDX-License-Identifier: MIT`.

No conviene limitar MIT únicamente a `scripts/` y `tests/` si existen otros directorios de
software.

## Contenido educativo

`LICENSE-CONTENT.md` aplica al contenido educativo original de `curriculum/`, `content/`,
`docs/`, guías raíz y páginas educativas generadas bajo `site/classes/`, salvo aviso específico.

Ejemplo de atribución:

> “Trayectoria Escolar Chile”, por Vladimir Acuña (`vladimiracunadev-create`),
> CC BY-NC-SA 4.0, https://github.com/vladimiracunadev-create/chilean-school-learning-path.
> Adaptado por [nombre], [fecha].

## Datos

Los datasets no heredan automáticamente MIT o CC por vivir en el repositorio. Deben declarar
procedencia, licencia, restricciones, fecha y permisos de redistribución/derivación.

## Terceros

Libros, papers, textos escolares, imágenes, videos, recursos MINEDUC/BCN, datasets, modelos,
pesos de IA y software externo conservan sus derechos y licencias originales.

El proyecto enlaza 595 recursos de lectura asociados por MINEDUC, pero no los republica ni los
declara obligatorios. Las descripciones curriculares mantienen enlace y fecha de consulta.

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

## Activos visuales y marca

`ASSET_LICENSES.md` identifica los activos incluidos. `TRADEMARKS.md` regula nombre, identidad y
marcas: una licencia de código o contenido no concede automáticamente derechos de marca.

## Licenciamiento dual

La versión comunitaria puede permanecer bajo CC BY-NC-SA 4.0 y el titular conceder una licencia
comercial independiente a empresas o instituciones.

> Política operativa; no sustituye asesoría jurídica individual.
