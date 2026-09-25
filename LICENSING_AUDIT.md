# Auditoría del sistema de licencias

**Fecha de corte:** 2026-09-25

**Repositorio:** `vladimiracunadev-create/chilean-school-learning-path`

**Alcance Git inspeccionado:** historial completo disponible hasta `f0e09d2b`
**Naturaleza:** auditoría técnica y documental; no es asesoría jurídica.

## 1. Estado encontrado

El repositorio ya aplicaba correctamente un modelo por capas: MIT para software original; CC BY-NC-SA 4.0 para contenido educativo original; políticas específicas para datos y activos; conservación de derechos de terceros; y exclusión de marcas. El árbol estaba limpio, `main` coincidía con `origin/main` y no existían ramas locales auxiliares ni otros worktrees.

El riesgo material estaba en las salidas mixtas. Las 2.823 fichas curriculares reproducían código y redacción oficial de OA junto con elaboración pedagógica original, mientras el pie HTML resumía toda la página como “contenido original CC BY-NC-SA 4.0”. La política general excluía documentos oficiales, pero el aviso de la salida podía inducir a una interpretación más amplia.

## 2. Archivos y superficies auditadas

Se revisaron `LICENSE`, `LICENSE-CONTENT.md`, `LICENSING.md`, `DATA-LICENSE.md`, `ASSET_LICENSES.md`, `THIRD_PARTY_NOTICES.md`, `TRADEMARKS.md`, `CONTRIBUTING.md`, `README.md`, `OFFICIAL_REFERENCES.md`, `METHODOLOGY.md`, `CURRICULUM.md`, `curriculum/`, `content/`, `docs/`, `sources/`, `scripts/`, `tests/`, `site/`, `.github/`, el historial Git y la lista de autores de commits.

## 3. Mapa de derechos por familia

| Familia | Titular/origen | Naturaleza | Regla | Redistribución / modificación / comercial | Atribución |
|---|---|---|---|---|---|
| `scripts/`, `tests/`, `site/app.js`, `site/styles.css` | Vladimir Acuña; código original del proyecto | software | MIT | sí / sí / sí, conservando MIT | aviso MIT |
| secuencias, clases, actividades, ejercicios, tareas, rúbricas y guías originales | Vladimir Acuña, salvo atribución distinta | contenido educativo | CC BY-NC-SA 4.0 | sí / sí / no comercial bajo la licencia pública; SA en adaptaciones | autor, licencia, enlace y cambios |
| códigos de OA, nivel, asignatura, eje, URL, fecha e identificadores | Currículum Nacional/MINEDUC como procedencia | hechos y metadatos | regla por procedencia; no se afirma exclusividad | evaluar por campo y contexto | fuente y fecha |
| redacción exacta de OA y descripciones oficiales | MINEDUC o titular correspondiente | contenido oficial | fuera de la CC del proyecto | no se presume permiso abierto, modificación ni uso comercial | titular, URL y fecha |
| `sources/mineduc-curriculum-snapshot.json` | páginas públicas de Currículum Nacional | dataset mixto | `DATA-LICENSE.md` | redistribución cautelar con trazabilidad; sin licencia autónoma sobre redacción oficial | fuente y fecha |
| `curriculum/catalog.json`, `site/catalog.json` | transformación del snapshot + estructura y redacción propia | salida de datos mixta | derechos por componente | no existe permiso único para todos los campos | conservar procedencia y avisos |
| `content/developed-lessons.json` | Vladimir Acuña | contenido pedagógico estructurado | CC BY-NC-SA 4.0 | no comercial bajo licencia pública | sí |
| `site/icon.svg` | diseño original del proyecto | activo visual | CC BY-NC-SA 4.0; sin concesión de marca | no comercial bajo licencia pública | sí |
| lecturas enlazadas | titulares y editoriales correspondientes | material de terceros | licencia original | el repositorio enlaza, no republica | título/enlace; licencia si se redistribuye |
| Markdown, HTML, Pages, sitemap, copias offline y PDF | generados desde las familias anteriores | salida derivada | hereda por componente | ninguna conversión amplía permisos | conservar avisos de cada fuente |
| nombre, logo e identidad | titulares correspondientes | marca | `TRADEMARKS.md` | no concedidos por MIT o CC | no implicar respaldo |

## 4. Inconsistencias detectadas

- La variante histórica indicada en el encargo, `DATA_LICENSES.md`, ya no existía ni era referenciada al inicio de esta auditoría; `DATA-LICENSE.md` era canónico. Faltaba, sin embargo, una prueba automática contra su reaparición.
- Los avisos HTML de las fichas no separaban con suficiente precisión redacción oficial y elaboración propia.
- El validador solo comprobaba presencia de unos archivos y campos mínimos; no verificaba enlaces legales, aliases obsoletos, inventarios, procedencia del snapshot ni avisos de salidas generadas.
- No existían `docs/COMMERCIAL_USE.md`, `docs/LICENSING_HISTORY.md` ni este entregable.
- `CONTRIBUTING.md` distinguía licencias, pero no documentaba una decisión sobre DCO.

## 5. Cambios efectuados

- Se mantuvo `DATA-LICENSE.md` como nombre canónico, sin duplicarlo.
- Se añadió un aviso visible a Markdown y HTML generado que excluye expresamente código y redacción oficial del OA de la CC del proyecto.
- Se aclaró la separación entre hechos/metadatos, redacción oficial y elaboración original.
- Se documentó la herencia de licencias en todas las salidas generadas.
- Se incorporaron guía de uso comercial, historial y DCO 1.1 para contribuciones futuras, sin CLA.
- Se amplió `scripts/validate_licensing.py` y su cobertura automatizada.

## 6. Material MINEDUC detectado

El snapshot contiene 2.823 objetivos con código, descripción oficial, eje y URL, organizados en 149 registros de nivel/asignatura, con verificación declarada el 24 de septiembre de 2026. También registra 595 enlaces de lectura asociados. La auditoría clasifica los identificadores y campos factuales separadamente de la redacción oficial. El proyecto no afirma autoría, patrocinio ministerial ni una licencia abierta sobre esa redacción.

## 7. Otros terceros

Se detectaron enlaces a Currículum Nacional, Biblioteca del Congreso Nacional, Biblioteca Digital Escolar, Creative Commons, GitHub y recursos de lectura. No se encontraron fotografías, fuentes, audio, video ni binarios de terceros versionados. El único activo visual versionado es `site/icon.svg`, inventariado en `ASSET_LICENSES.md`. Los recursos de lectura se enlazan y no se alojan.

## 8. Contributors externos

`git shortlog -sne --all` mostró un solo autor de commits: Vladimir Acuña (`vladimir.acuna.dev@gmail.com`). No se sustituyeron nombres ni se atribuyó al mantenedor material externo. Futuras contribuciones deberán conservar su autoría y firmar DCO 1.1.

## 9. Riesgos pendientes

- No se verificó una licencia abierta específica de MINEDUC que autorice de forma general la redistribución o explotación comercial de todas las redacciones oficiales incluidas. La mitigación es excluirlas expresamente de la CC y mantener fuente, enlace y fecha.
- La licitud concreta de reproducir cada texto oficial depende de la normativa y del uso aplicable; requiere revisión jurídica chilena si se prepara explotación comercial o redistribución independiente del dataset.
- Los enlaces y términos externos pueden cambiar; deben revisarse periódicamente.
- Los validadores demuestran coherencia técnica, no titularidad ni permiso legal sustantivo.

## 10. Recomendaciones

1. Antes de un producto comercial, separar físicamente el contenido original de los campos oficiales y obtener revisión jurídica.
2. Preferir metadatos + referencia + enlace + fecha cuando la reproducción literal no sea necesaria.
3. Exigir ficha de procedencia antes de añadir datasets, activos o material externo.
4. Mantener DCO y revisión de derechos en cada contribución.
5. Repetir esta auditoría cuando cambie el modelo de datos, se añadan medios o se publique una nueva versión.

## 11. Resultado de validadores

Resultados locales del 25 de septiembre de 2026:

- `generate_development_plan.py`: 153 OA disciplinares de 1° básico generados;
- `generate_school_program.py`: 12.997 clases, 2.823 OA, 12 niveles, 35 asignaturas y 595 enlaces de lectura;
- segunda generación: 5.702 artefactos comparados por SHA-256, sin diferencias;
- `validate_school_program.py`: aprobado;
- `validate_licensing.py`: aprobado;
- `python -m unittest discover -s tests -p "test_*.py" -v`: 16 pruebas aprobadas;
- `python -m compileall -q scripts tests`: aprobado.

## 12. Estado final del CI

La workflow `Quality and Pages` integra generación, ambos validadores, tests, compilación y comprobación de diff reproducible. El estado remoto de la ejecución asociada al commit final se comprueba después de publicar `main`; este documento registra la evidencia local y no sustituye la evidencia de GitHub Actions.
