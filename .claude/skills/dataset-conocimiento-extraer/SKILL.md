---
name: dataset-conocimiento-extraer
description: >-
  Extrae conocimiento puro (definiciones, hechos, relaciones, procedimientos y concepciones erróneas)
  desde cualquier fuente —un programa de aprendizaje, documentación, apuntes, un manual— y lo escribe
  como registros atómicos, autocontenidos y fundamentados en la fuente, con procedencia y licencia,
  listos para un dataset JSONL. Úsalo cuando el usuario pida "extrae el conocimiento de…", "crea un
  dataset de <tema>", "convierte este programa/curso/documento en datos para entrenar", "atomiza este
  contenido", "saca definiciones y hechos de…". Es general: no depende del dominio. NO verifica su propio
  trabajo: la verificación la hace otro contexto con la skill dataset-verificar.
---

# Extraer conocimiento puro

Sigue el [estándar de conocimiento puro](https://github.com/vladimiracunadev-create/learning-path-datasets/blob/main/docs/KNOWLEDGE_STANDARD.md) y el [esquema](https://github.com/vladimiracunadev-create/learning-path-datasets/blob/main/docs/DATASET_SCHEMA.md) del repositorio `learning-path-datasets`. Si trabajas fuera de ese repositorio, aplica los mismos principios y los mismos campos.

## Qué hace

Convierte texto de una fuente en registros del esquema común, sin inventar nada y dejando en cada uno de dónde salió.

## Antes de empezar

1. **Define la unidad de trabajo**: un capítulo, una clase, un archivo. Es también la unidad de **partición** (todos sus registros irán a `train` o todos a `eval`).
2. **Anota la procedencia**: repositorio o URL, commit o fecha de consulta, ruta o sección, **licencia** de la fuente. Si no conoces la licencia, **no extraigas**: pregunta.
3. **Lee la fuente completa de la unidad** antes de escribir el primer registro.

## Procedimiento

1. **Segmenta** la unidad en ideas. Una idea = algo que se puede afirmar o negar por separado.
2. **Clasifica** cada idea: `definicion`, `hecho`, `relacion`, `procedimiento` o `concepcion_erronea`. Usa `concepto` solo si de verdad no se puede atomizar.
3. **Redacta** cada registro:
   - `entrada`: el término, la pregunta o el sujeto, escrito para entenderse solo.
   - `salida`: una oración o una lista corta de pasos, en lenguaje claro, sin referencias al formato original.
   - `razon`: la **cita breve** de la fuente que lo respalda (≤ 25 palabras) o el motivo.
   - `extra`: `sujeto`/`predicado`/`objeto` cuando aporte, `vigencia` si cambia con el tiempo y `confianza` (`alta` si la fuente lo dice textual, `media` si lo infieres de forma directa, `baja` si dudas).
4. **Autocomprueba** cada registro con la lista de abajo.
5. **Escribe** los registros en un archivo de trabajo (staging) JSONL, uno por línea, con `particion` calculada por la unidad y `revision: ia_asistida_sin_revision_humana`.
6. **Informa**: cuántos registros por tipo, qué quedó fuera y por qué, y qué dudas tienes.

## Lista de autocomprobación

- [ ] ¿Se entiende sin ver los registros vecinos?
- [ ] ¿Es una sola idea?
- [ ] ¿La fuente lo dice o lo implica directamente? Si no, bórralo.
- [ ] ¿Depende de una fecha o versión? Declárala en `extra.vigencia`.
- [ ] ¿Hay copia larga de la fuente? Redáctalo con tus palabras; deja solo la cita breve en `razon`.
- [ ] ¿Contiene datos personales, opiniones o publicidad? Quítalo.
- [ ] ¿Repite otro registro tuyo? Fusiona o descarta.

## Reglas que no se rompen

- **No inventes**. Si la fuente es ambigua o está incompleta, registra la duda en tu informe en vez de rellenar con lo que «sabes».
- **No mezcles fuentes** en un mismo registro.
- **No marques revisión humana**. Tú no la hiciste ni la hizo nadie.
- **No te verifiques a ti mismo**: tu autocomprobación no sustituye al verificador independiente.
- Respeta las exclusiones de la fuente (contenido que exige un experto, material de terceros, datos personales).

## Salida esperada

Un JSONL de staging, un resumen con conteos por tipo y una lista de exclusiones y dudas, listos para pasar a `dataset-verificar`.
