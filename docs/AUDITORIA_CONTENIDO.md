# Auditoría de contenido: línea base reproducible

Esta auditoría mide lo que un programa puede comprobar. **No** juzga la exactitud disciplinar ni la pertinencia etaria de cada clase: eso requiere revisión profesional y permanece pendiente. Se regenera con `python scripts/audit_content.py --write`.

## Defectos comprobados

1. **La clase está escrita para quien enseña.** Antes del cuaderno del estudiante, las clases publicaban acciones docentes, criterios y pautas, pero ninguna publicaba ejemplos resueltos, un conjunto de ejercicios con todos sus datos ni un solucionario para el alumno.
2. **Insumo genérico por palabras clave.** `scripts/lesson_quality_enrichment.py` elige el recurso, la consigna y la referencia con coincidencias de palabras en el título (`_math`, `_science`, `_generic`...). Una clase sobre descomponer 63 en decenas y unidades recibía «tarjetas numéricas 18, 20 y 21», que no corresponden a su OA. Para las clases con cuaderno, el insumo, la consigna y la referencia se derivan ahora del propio cuaderno y el generador por palabras clave ya no se aplica.
3. **Consignas que sólo cambian números o el título.** Las consignas sin cuaderno se repiten con una plantilla por asignatura y curso; la tabla siguiente la cuantifica.

## Cobertura y repetición por nivel

Las columnas de plantillas consideran sólo las clases **sin** cuaderno; una plantilla aplica a números o títulos distintos pero a la misma redacción.

| Nivel | Clases con consigna | Con cuaderno | Plantillas de consigna distintas | Mayor repetición de una plantilla |
|---|---:|---:|---:|---:|
| 1.º básico | 691 | 691 | 0 | 0 |
| 2.º básico | 721 | 721 | 0 | 0 |
| 3.º básico | 757 | 0 | 85 | 157 |
| 4.º básico | 811 | 0 | 85 | 161 |
| 5.º básico | 920 | 0 | 162 | 166 |
| 6.º básico | 952 | 0 | 152 | 176 |
| 7.º básico | 760 | 0 | 189 | 113 |
| 8.º básico | 771 | 0 | 180 | 117 |
| 1.º medio | 753 | 0 | 154 | 143 |
| 2.º medio | 744 | 0 | 156 | 146 |
| 3.º medio | 495 | 0 | 28 | 109 |
| 4.º medio | 466 | 0 | 28 | 111 |

**Total:** 8841 clases con consigna exacta; 1412 con cuaderno del estudiante.

## Qué se corrige y en qué orden

- Se trabaja por lotes verificables: cada lote reemplaza el insumo genérico por un cuaderno específico del OA y lo valida (`scripts/validate_student_lessons.py`).
- Las clases que aún no tienen cuaderno conservan su planificación docente y siguen figurando como pendientes en `docs/COBERTURA_ESTUDIANTE.md`.
- Prioridad: primero OA donde el insumo genérico contradice el contenido; después los niveles con mayor repetición de una misma consigna.
- Estado de revisión profesional: **pendiente** para todos los lotes. La validación automática no la sustituye.
