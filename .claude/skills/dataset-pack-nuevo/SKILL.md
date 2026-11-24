---
name: dataset-pack-nuevo
description: >-
  Incorpora un programa de aprendizaje o una base de conocimiento nueva (cualquier dominio) al repositorio
  learning-path-datasets creando su pack: analiza la estructura de la fuente, define la unidad y la
  partición, mapea sus partes al esquema común, escribe el adaptador, las pruebas y la tarjeta del dataset.
  Úsalo cuando el usuario pida "suma este programa/curso/repositorio a los datasets", "crea un pack para
  <programa>", "adapta <repo> al esquema", "agrega un dominio nuevo". General: sirve para ciberseguridad,
  finanzas, IA, escolar, etc.
---

# Crear un pack nuevo

Guía de apoyo: [Cómo sumar un programa](https://github.com/vladimiracunadev-create/learning-path-datasets/blob/main/docs/ADDING_A_PACK.md).

## Procedimiento

1. **Reconocer la fuente.** Lee su README, su estructura de carpetas y sus generadores. Responde: ¿en qué formato vive el contenido (Markdown, código, JSON)?, ¿qué unidad natural tiene (clase, módulo, capítulo)?, ¿qué partes hay (explicación, ejercicios con respuesta, glosario, rúbricas)?, ¿cuál es su licencia?
2. **Elegir la ruta.**
   - Si es Markdown plano, prueba primero el pack `markdown-course` y mide qué saca.
   - Si tiene partes estructuradas (ejercicios con respuesta, glosarios), escribe un adaptador propio.
3. **Definir el mapa a registros.** Para cada parte de la fuente, decide el `tipo`, qué va en `entrada`, `salida` y `razon`, y qué va en `extra`. Prefiere los tipos de conocimiento puro cuando la fuente sea explicativa.
4. **Fijar la partición.** La clave es la **unidad** (clase, capítulo), nunca el ejemplo. Todos los registros de una unidad caen en el mismo lado.
5. **Fijar exclusiones.** Qué partes no se publican (material de terceros, contenido que exige un experto, datos personales, texto oficial con derechos) y por qué. Quedan escritas en el adaptador y en la tarjeta.
6. **Escribir el adaptador** en `src/lpdatasets/packs/<pack>.py`, decorado con `@register("<pack>")`, y registrarlo en `load_builtin`. Debe producir `id` estables, `fuente` completa y `licencia`.
7. **Probar** con una fuente sintética pequeña en `tests/`: genera, valida, reproduce igual y rechaza un dato manipulado.
8. **Exportar** una unidad real, validar, y pasar por `dataset-verificar` una muestra antes de exportar todo.
9. **Documentar**: fila en la tabla de packs del README, tarjeta `docs/DATASET_CARD_<pack>.md` con composición, exclusiones y límites, licencia en `DATA-LICENSE.md`, y `CHANGELOG.md`.

## Criterios de hecho

- El pack pasa lint, pruebas y `lpdatasets validate`.
- La exportación se reproduce byte a byte.
- Las exclusiones y límites están escritos.
- Ninguna parte de la fuente con derechos de terceros quedó en los datos.
- La tarjeta dice con claridad que no hay revisión humana, si es el caso.

## Lo que no hace

No cambia el contenido de la fuente ni la corrige. Si encuentra errores en ella, los reporta al repositorio de origen.
