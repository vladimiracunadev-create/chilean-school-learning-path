# Estado editorial

Fecha de corte: **2026-09-24**. Los conteos provienen de `curriculum/catalog.json` y se verifican en CI.

| Estado | Clases | Significado |
|---|---:|---|
| Inventariada | 12.997 | OA, nivel, asignatura, eje y fuente oficial identificados |
| Secuenciada | 12.997 | posición, fase y duración propuestas dentro del OA |
| Borrador | 873 | arquitectura automática de 1° básico pendiente de investigación y reescritura específica |
| Desarrollada | 115 | contenido disciplinar específico validado contra el contrato estructural |
| Integrada | 68 | habilidades y actitudes matemáticas incorporadas dentro de las clases de contenido |
| Revisada | 0 | control pedagógico, disciplinar, documental y técnico humano |
| Publicada | 12.997 | Markdown y HTML accesibles, enlazados y verificados automáticamente |

“Publicada” describe disponibilidad técnica; no sustituye “desarrollada” ni “revisada”. **1° básico está en reconstrucción pedagógica**: 93 clases desarrolladas, 68 experiencias integradas y 873 borradores. Matemática está completa en sus 83 clases de contenido, aunque su revisión humana sigue pendiente. Se conservan además 22 clases piloto de otros niveles.

## Reconstrucción de 1° básico

| Secuencia | Clases desarrolladas | Fundamento |
|---|---:|---|
| `AR01 OA 01` | 6 | observación, expresión visual y producción artística |
| Matemática · `MA01 OA 01` a `MA01 OA 20` | 83 | 20 secuencias de contenido alineadas con unidades e indicadores oficiales |
| `LE01 OA 03` | 4 | progresión de conciencia fonológica alineada con indicadores oficiales |
| **Total desarrollado en 1° básico** | **93** | revisión humana pendiente |

Las 93 clases desarrolladas contienen propósito docente, meta estudiantil, inicio, modelado, práctica guiada, desempeño individual, materiales, apoyo, profundización, ticket, evidencia, criterios, decisión posterior y adaptación a 45 minutos. Los desarrollos específicos se conservan en [content/developed-lessons.json](content/developed-lessons.json) y [scripts/grade_one_math_lessons.py](scripts/grade_one_math_lessons.py). La arquitectura de [scripts/grade_one_lessons.py](scripts/grade_one_lessons.py) produce borradores y no se contabiliza como desarrollo terminado.

[Ver documentación de 1° básico](docs/PRIMERO_BASICO.md) · [Abrir programa por asignaturas](docs/1-basico/README.md)

## Pilotos conservados en otros niveles

- Matemática 3° básico · MA03 OA 11 · 5 clases.
- Historia 3° básico · HI03 OA 05 · 6 clases.
- Ciencias Naturales 4° básico · CN04 OA 01 · 4 clases.
- Lengua y Literatura 8° básico · LE08 OA 09 · 7 clases.

## Cobertura publicada

- 12 niveles, desde 1° básico hasta 4° medio.
- 35 asignaturas o denominaciones curriculares.
- 2.823 Objetivos de Aprendizaje.
- 595 vínculos de lectura asociados por MINEDUC.
- 2.823 páginas HTML de OA con anclas estables para las 12.997 clases.

## Próximo gate editorial

Un lote solo pasa a “desarrollado” cuando cada clase incluye contenido disciplinar específico, ejemplo o demostración, práctica y evaluación propias del OA. El validador rechaza campos ausentes, criterios insuficientes, conteos divergentes y páginas que no materialicen el contrato. Solo pasa a “revisado” con evidencia humana registrada. La automatización no certifica por sí sola calidad pedagógica.
