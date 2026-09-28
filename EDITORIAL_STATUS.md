# Estado editorial

Fecha de corte: **2026-09-28**. Los conteos provienen de `curriculum/catalog.json` y se verifican en CI.

| Estado | Clases | Significado |
|---|---:|---|
| Inventariada | 12.997 | OA, nivel, asignatura, eje y fuente oficial identificados |
| Secuenciada | 12.997 | posición, fase y duración propuestas dentro del OA |
| Borrador | 0 | no quedan borradores en 1° básico |
| Desarrollada | 713 | contenido disciplinar específico validado contra el contrato estructural |
| Integrada | 343 | habilidades o actitudes incorporadas dentro de las clases de contenido |
| Revisada | 0 | control pedagógico, disciplinar, documental y técnico humano |
| Publicada | 12.997 | Markdown y HTML accesibles, enlazados y verificados automáticamente |

“Publicada” describe disponibilidad técnica; no sustituye “desarrollada” ni “revisada”. **1° básico tiene desarrollo interno completo**: 691 clases desarrolladas, 343 experiencias integradas y 0 borradores. Las once asignaturas están completas en contenido, aunque su revisión humana sigue pendiente. Se conservan además 22 clases piloto de otros niveles.

## Reconstrucción de 1° básico

| Secuencia | Clases desarrolladas | Fundamento |
|---|---:|---|
| Artes Visuales · `AR01 OA 01` a `AR01 OA 05` | 24 | creación, experimentación y apreciación con decisiones visuales explicadas |
| Ciencias Naturales · `CN01 OA 01` a `CN01 OA 12` | 49 | observación, indagación, diseño, evidencia y seguridad |
| Historia · `HI01 OA 01` a `HI01 OA 15` | 68 | temporalidad, fuentes, territorio, comunidad y ciudadanía |
| Música · `MU01 OA 01` a `MU01 OA 07` | 29 | escucha, interpretación, creación y reflexión musical |
| Educación Física · `EF01 OA 01` a `EF01 OA 11` | 48 | desempeño motriz, vida activa, seguridad y colaboración |
| Orientación · `OR01 OA 01` a `OR01 OA 08` | 35 | crecimiento personal, autocuidado, convivencia y hábitos de aprendizaje |
| Tecnología · `TE01 OA 01` a `TE01 OA 06` | 26 | diseño, elaboración, prueba y uso responsable de TIC |
| Inglés · `EN01 OA 01` a `EN01 OA 14` | 69 | comprensión y producción inicial oral, lectora y escrita |
| Lengua y Cultura de Pueblos Originarios · 29 OA | 129 | lengua, territorio, memoria, cosmovisión y patrimonio con resguardos culturales |
| Matemática · `MA01 OA 01` a `MA01 OA 20` | 83 | 20 secuencias de contenido alineadas con unidades e indicadores oficiales |
| Lenguaje · `LE01 OA 01` a `LE01 OA 26` | 131 | 26 secuencias de lectura, escritura y comunicación oral; criterios internos distinguidos de indicadores oficiales |
| **Total desarrollado en 1° básico** | **691** | revisión humana pendiente |

Las 691 clases desarrolladas contienen propósito docente, meta estudiantil, inicio, modelado, práctica guiada, desempeño individual, materiales, apoyo, profundización, ticket, evidencia, criterios, decisión posterior y adaptación a 45 minutos. Los desarrollos específicos se conservan en [content/developed-lessons.json](content/developed-lessons.json) y en los módulos disciplinares de `scripts/grade_one_*_lessons.py`. La arquitectura de [scripts/grade_one_lessons.py](scripts/grade_one_lessons.py) queda disponible para niveles aún no desarrollados y no se contabiliza como desarrollo terminado.

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
