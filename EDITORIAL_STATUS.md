# Estado editorial

Fecha de corte: **2026-09-24**. Los conteos provienen de `curriculum/catalog.json` y se verifican en CI.

| Estado | Clases | Significado |
|---|---:|---|
| Inventariada | 12.997 | OA, nivel, asignatura, eje y fuente oficial identificados |
| Secuenciada | 12.997 | posición, fase y duración propuestas dentro del OA |
| Desarrollada | 1.056 | contenido disciplinar específico validado contra el contrato completo |
| Revisada | 0 | control pedagógico, disciplinar, documental y técnico humano |
| Publicada | 12.997 | Markdown y HTML accesibles, enlazados y verificados automáticamente |

“Publicada” describe disponibilidad técnica; no sustituye “desarrollada” ni “revisada”. **1° básico está completamente desarrollado**: 1.034 clases, 237 OA y 11 asignaturas. Se conservan además 22 clases piloto de otros niveles. El trabajo continúa nivel por nivel.

## Nivel completo: 1° básico

| Asignatura | OA | Clases |
|---|---:|---:|
| Artes Visuales | 12 | 52 |
| Ciencias Naturales | 22 | 89 |
| Educación Física y Salud | 19 | 80 |
| Historia, Geografía y Ciencias Sociales | 31 | 132 |
| Inglés (Propuesta) | 18 | 85 |
| Lengua y Cultura de los Pueblos Originarios Ancestrales | 33 | 147 |
| Lenguaje y Comunicación | 33 | 160 |
| Matemática | 36 | 151 |
| Música | 14 | 57 |
| Orientación | 8 | 35 |
| Tecnología | 11 | 46 |
| **Total 1° básico** | **237** | **1.034** |

Cada clase contiene propósito docente, meta estudiantil, inicio, modelado, práctica guiada, desempeño individual, materiales, apoyo sin rebajar el OA, profundización, ticket de salida, evidencia, al menos tres criterios observables, decisión posterior y adaptación a 45 minutos. La arquitectura especializada de 1° básico vive en [scripts/grade_one_lessons.py](scripts/grade_one_lessons.py); los desarrollos manuales se conservan en [content/developed-lessons.json](content/developed-lessons.json).

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
