# Política de datos y datasets

## Principio

No existe una licencia única para todos los datos.

| Estado | Redistribuir | Derivar | Uso en corpus |
|---|---:|---:|---:|
| PUBLIC_DOMAIN | sí | sí | sí |
| CC_BY | sí | sí | sí, con atribución |
| CC_BY_SA | sí | sí | sí, con SA |
| CC_BY_NC | no comercial | no comercial | corpus NC |
| CC_BY_NC_SA | no comercial | no comercial | corpus NC-SA |
| CC_BY_ND | limitado | no | metadatos |
| CC_BY_NC_ND | limitado | no | metadatos |
| COPYRIGHT | no por defecto | no por defecto | no por defecto |
| TEXTBOOK_COPYRIGHT | no por defecto | no por defecto | protección reforzada |
| UNKNOWN | no | no | cuarentena |

## Datos publicados por este repositorio

| Artefacto | Procedencia | Redistribución en este repo | Regla práctica |
|---|---|---|---|
| `sources/mineduc-curriculum-snapshot.json` | páginas públicas de Currículum Nacional | metadatos, redacciones oficiales y enlaces con trazabilidad; no se ofrece una licencia autónoma sobre la redacción oficial | conservar fuente y fecha; no presentar como dataset oficial emitido por MINEDUC ni como contenido CC del proyecto |
| `curriculum/catalog.json` | transformación estructurada del snapshot y contenido propio | sí, como salida mixta del proyecto | hechos/metadatos, redacción oficial y elaboración original conservan reglas separadas; no existe una licencia única para todos los campos |
| `site/catalog.json` | copia compacta generada del catálogo | sí, como artefacto técnico mixto | mismas condiciones por componente que `curriculum/catalog.json`; la minificación no cambia derechos |
| `content/developed-lessons.json` | redacción educativa original | sí, bajo CC BY-NC-SA 4.0 | atribuir, uso no comercial y compartir adaptaciones igual |
| `content/development-plan.json` | planificación editorial original generada por el proyecto | sí, bajo CC BY-NC-SA 4.0 | atribuir, uso no comercial y compartir adaptaciones igual |
| `competencies/taxonomy.v1.json` | taxonomía educativa original del proyecto | sí, bajo CC BY-NC-SA 4.0 | no presentarla como taxonomía oficial ni como medición validada |
| `competencies/progressions.v1.json` | relaciones pedagógicas inferidas desde OA y contenido existente | sí, como salida mixta bajo las reglas de cada componente | conservar códigos y fuentes oficiales; atribuir la organización y las inferencias al proyecto |
| `competencies/frameworks.v1.json` | metadatos y síntesis de marcos oficiales con correspondencias pedagógicas propias | sí, como salida mixta | conservar fuente, versión, alcance, limitaciones y tipo de alineamiento; no declarar oficial una inferencia |
| `assessments/item-bank.v1.json` | tareas y rúbricas originales del proyecto | sí, bajo CC BY-NC-SA 4.0 | no presentar ítems internos como oficiales, pilotados o psicométricamente validados |
| `evidence/examples/*.json` | casos enteramente sintéticos | sí, bajo CC BY-NC-SA 4.0 | no reemplazar los códigos sintéticos por datos personales en el repositorio público |
| `site/competencias/data/*.json` | copias generadas de los artefactos anteriores | sí, bajo la licencia y procedencia del archivo fuente | la publicación web no cambia derechos ni estado de revisión |
| `site/updates.json` | resumen generado desde `CHANGELOG.md` | sí, bajo CC BY-NC-SA 4.0 | publicar fecha, título y alcance sin sustituir el historial versionado |
| `competencies/taxonomy.v1.json` | taxonomía educativa original del proyecto | sí, bajo CC BY-NC-SA 4.0 | no presentarla como taxonomía oficial ni como medición validada |
| `competencies/progressions.v1.json` | relaciones pedagógicas inferidas desde OA y contenido existente | sí, como salida mixta bajo las reglas de cada componente | conservar códigos y fuentes oficiales; atribuir la organización y las inferencias al proyecto |
| `competencies/frameworks.v1.json` | metadatos y síntesis de marcos oficiales con correspondencias pedagógicas propias | sí, como salida mixta | conservar fuente, versión, alcance, limitaciones y tipo de alineamiento; no declarar oficial una inferencia |
| `assessments/item-bank.v1.json` | tareas y rúbricas originales del proyecto | sí, bajo CC BY-NC-SA 4.0 | no presentar ítems internos como oficiales, pilotados o psicométricamente validados |
| `evidence/examples/*.json` | casos enteramente sintéticos | sí, bajo CC BY-NC-SA 4.0 | no reemplazar los códigos sintéticos por datos personales en el repositorio público |
| `site/competencias/data/*.json` | copias generadas de los artefactos anteriores | sí, bajo la licencia y procedencia del archivo fuente | la publicación web no cambia derechos ni estado de revisión |

Los hechos y códigos curriculares pueden no estar protegidos del mismo modo que una redacción creativa. Esta política no afirma dominio sobre materiales oficiales: documenta procedencia y evita mezclar licencias.

Los catálogos JSON, Markdown, HTML, sitemap, GitHub Pages, copias offline y PDF heredan las reglas de sus fuentes. La transformación técnica o el cambio de formato no relicencian una redacción oficial ni una obra de tercero.

## Dataset propio

Un dataset íntegramente propio puede usar una licencia específica. Opciones a evaluar:
- **CC0 1.0** para metadatos abiertos que se quieran liberar ampliamente;
- **CC BY-NC-SA 4.0** para una selección/estructura creativa no comercial, siempre que sus
  componentes sean compatibles.

Un nuevo dataset externo debe añadir su licencia o una ficha equivalente antes de incorporarse.

## Datos personales

No publicar RUT, direcciones, teléfonos, correos privados, datos de menores, evaluaciones
identificables, credenciales o telemetría personal no autorizada.
