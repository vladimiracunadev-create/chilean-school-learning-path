# Estado editorial

Fecha de corte: **2026-09-29**. Los conteos provienen de `curriculum/catalog.json` y se verifican en CI.

| Estado | Clases | Significado |
|---|---:|---|
| Inventariada | 12.997 | OA, nivel, asignatura, eje y fuente oficial identificados |
| Secuenciada | 12.997 | posición, fase y duración propuestas dentro del OA |
| Borrador | 0 | no quedan borradores en 1°, 2° ni 3° básico |
| Desarrollada | 2.298 | contenido disciplinar específico validado contra el contrato estructural |
| Integrada | 1.160 | habilidades o actitudes incorporadas dentro de las clases de contenido |
| Revisada | 0 | control pedagógico, disciplinar, documental y técnico humano |
| Publicada | 12.997 | Markdown y HTML accesibles, enlazados y verificados automáticamente |

“Publicada” describe disponibilidad técnica; no sustituye “desarrollada” ni “revisada”. **1°, 2° y 3° básico tienen desarrollo interno completo**: 691, 721 y 757 clases desarrolladas, junto con 343, 351 y 379 experiencias integradas. Cada nivel cubre sus once asignaturas sin propuestas pendientes. **Matemática de 4° básico también está completa** con 118 clases y 87 experiencias integradas. Se mantienen además 11 clases piloto en Ciencias de 4° y Lengua y Literatura de 8°.

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

## Reconstrucción de 2° básico

| Asignatura | Clases desarrolladas | Experiencias integradas |
|---|---:|---:|
| Artes Visuales | 24 | 28 |
| Ciencias Naturales | 57 | 44 |
| Educación Física y Salud | 47 | 32 |
| Historia, Geografía y Ciencias Sociales | 72 | 72 |
| Inglés (Propuesta) | 68 | 16 |
| Lengua y Cultura de los Pueblos Originarios Ancestrales | 116 | 18 |
| Lenguaje y Comunicación | 149 | 29 |
| Matemática | 93 | 64 |
| Música | 29 | 28 |
| Orientación | 35 | 0 |
| Tecnología | 31 | 20 |
| **Total desarrollado en 2° básico** | **721** | **351** |

Las secuencias canónicas viven en los módulos `scripts/grade_two_*_lessons.py`. Los criterios de progresión derivados se rotulan como internos, cada ficha conserva el enlace al OA oficial y las integraciones transversales no se cuentan como clases independientes.

[Ver mapa de 2° básico](docs/2-basico/README.md) · [Abrir sus once guías](docs/2-basico/README.md#las-11-asignaturas)

[Ver documentación de 1° básico](docs/PRIMERO_BASICO.md) · [Abrir programa por asignaturas](docs/1-basico/README.md)

## Reconstrucción de 3° básico

| Asignatura | Clases desarrolladas | Experiencias integradas |
|---|---:|---:|
| Artes Visuales | 25 | 28 |
| Ciencias Naturales | 55 | 49 |
| Educación Física y Salud | 48 | 32 |
| Historia, Geografía y Ciencias Sociales | 72 | 72 |
| Inglés (Propuesta) | 69 | 16 |
| Lengua y Cultura de los Pueblos Originarios Ancestrales | 116 | 18 |
| Lenguaje y Comunicación | 157 | 29 |
| Matemática | 112 | 87 |
| Música | 35 | 28 |
| Orientación | 35 | 0 |
| Tecnología | 33 | 20 |
| **Total desarrollado en 3° básico** | **757** | **379** |

Las 1.136 entradas del nivel están resueltas. Las guías explicitan continuidad con 2°, método disciplinar, evidencia observable y resguardos particulares de seguridad, privacidad y pertinencia cultural.

[Ver mapa de 3° básico](docs/3-basico/README.md) · [Abrir sus once guías](docs/3-basico/README.md#las-11-asignaturas)

## Matemática de 4° básico

| Cobertura | Cantidad | Estado |
|---|---:|---|
| OA de contenido | 27 | 118 clases desarrolladas |
| OA de habilidades y actitudes | 20 | 87 experiencias integradas |
| Propuestas pendientes de Matemática | 0 | asignatura completa |
| Revisión humana | 0 | pendiente |

El recorrido diferencia número y operaciones, patrones y álgebra, geometría, medición, datos y probabilidades. Cada clase incluye representación, razonamiento, comprobación, error previsible, apoyo y profundización específicos.

[Abrir guía de Matemática de 4° básico](docs/4-basico/matematica.md)

## Pilotos conservados en otros niveles

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
