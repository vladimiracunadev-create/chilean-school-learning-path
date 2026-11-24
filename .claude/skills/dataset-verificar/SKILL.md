---
name: dataset-verificar
description: >-
  Verifica de forma independiente registros de un dataset de conocimiento: fidelidad a la fuente,
  corrección factual y de cálculo, atomicidad y autonomía, ambigüedad, duplicados, fuga entre train y
  eval, sesgos de forma, derechos y datos personales, y vigencia. Produce un veredicto por registro
  (ok, corregir, descartar) y un informe con conteos. Úsalo cuando el usuario pida "verifica el dataset",
  "revisa la calidad de estos registros", "haz la segunda lectura", "audita el dataset antes de
  publicar", o después de dataset-conocimiento-extraer. Es general y no depende del dominio. Debe
  ejecutarla un contexto distinto al que escribió los registros.
---

# Verificar un dataset de conocimiento

## Regla de oro

**Quien verifica no es quien escribió.** Si esta skill se invoca en el mismo contexto que extrajo los registros, detente y pide un contexto nuevo. Verificar es resolver y contrastar por tu cuenta, no releer buscando que «suene bien».

## Entradas

- Los registros (JSONL de staging o publicados).
- La **fuente** de cada uno (para contrastar).
- El [estándar](https://github.com/vladimiracunadev-create/learning-path-datasets/blob/main/docs/KNOWLEDGE_STANDARD.md) y el [esquema](https://github.com/vladimiracunadev-create/learning-path-datasets/blob/main/docs/DATASET_SCHEMA.md).

## Pruebas, en este orden

| # | Prueba | Cómo |
|---|---|---|
| 1 | **Esquema** | `lpdatasets validate` o un validador equivalente; corrige lo estructural primero |
| 2 | **Fidelidad a la fuente** | abre el pasaje citado y comprueba que **respalda** la `salida`; si dice otra cosa, matiza más o menos, es `corregir` |
| 3 | **Corrección** | responde tú la pregunta **sin mirar la `salida`** y compara; lo numérico, calcúlalo con herramienta |
| 4 | **Atomicidad y autonomía** | una sola idea, sin pronombres sin referente, sin «lo anterior» |
| 5 | **Ambigüedad** | ¿hay más de una respuesta válida? ¿la pregunta depende de contexto que no está? |
| 6 | **Duplicados** | exactos y casi iguales dentro del dataset y con otros niveles o packs |
| 7 | **Fuga** | ningún contenido casi idéntico entre `train` y `eval`; las particiones por unidad |
| 8 | **Sesgos de forma** | longitud de la respuesta correcta, posición de la opción correcta, plantillas repetidas |
| 9 | **Derechos y personas** | texto de terceros, citas largas, correos, teléfonos, nombres de personas reales |
| 10 | **Vigencia** | cifras, versiones o normas sin fecha de corte |

## Veredicto por registro

- **ok**: pasa todo.
- **corregir**: el registro es salvable; indica el cambio exacto y por qué.
- **descartar**: no se puede salvar o no debe publicarse; indica el motivo.

No edites en silencio. Entrega una **bitácora de correcciones** (id, campo, antes, después, motivo) y aplica los cambios solo si se te pide.

## Informe

1. Conteos: revisados, ok, corregir, descartar, por prueba y por tipo.
2. Tasa de error observada y qué tipo de error domina.
3. Ejemplos concretos (no más de 10) de cada categoría de problema.
4. **Cobertura real**: qué pruebas no pudiste ejecutar (sin acceso a la fuente, sin herramienta de cálculo) y qué porcentaje del dataset revisaste. Lo no ejecutado se reporta como **NO EJECUTADO**, nunca como aprobado.
5. Recomendación: publicar, corregir y volver a verificar, o no publicar.

## Reglas que no se rompen

- **No subas el estado de revisión**: aunque verifiques, `revision` sigue siendo `ia_asistida_sin_revision_humana`. Solo una persona real puede cambiarlo, y debe quedar registrada.
- Si revisas una **muestra**, dilo, di cómo la elegiste y extrapola con cautela.
- Si la tasa de error supera el 5 % en una prueba de corrección, no recomiendes publicar sin una segunda ronda.
- No inventes una fuente para «arreglar» un registro; si no se puede respaldar, se descarta.
