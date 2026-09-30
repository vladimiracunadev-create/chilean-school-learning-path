# Estado editorial

Fecha de corte: **2026-09-30**. Los conteos provienen de `curriculum/catalog.json` y se verifican en CI.

| Estado | Clases | Significado |
|---|---:|---|
| Inventariada | 12.997 | OA, nivel, asignatura, eje y fuente oficial identificados |
| Secuenciada | 12.997 | posición, fase y duración propuestas dentro del OA |
| Borrador | 0 | no quedan borradores; las propuestas pendientes permanecen secuenciadas |
| Desarrollada | 5.619 | contenido disciplinar específico validado contra el contrato estructural |
| Integrada | 2.814 | habilidades o actitudes incorporadas dentro de las clases de contenido |
| Revisada | 0 | control pedagógico, disciplinar, documental y técnico humano |
| Publicada | 12.997 | Markdown y HTML accesibles, enlazados y verificados automáticamente |

“Publicada” describe disponibilidad técnica; no sustituye “desarrollada” ni “revisada”. **1° a 7° básico tienen desarrollo interno completo**. En 7° las doce denominaciones reúnen 760 clases disciplinares y 515 experiencias integradas. Se mantienen además 7 clases piloto en Lengua y Literatura de 8°.

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

## Reconstrucción de 4° básico

| Asignatura | Clases desarrolladas | Experiencias integradas |
|---|---:|---:|
| Artes Visuales | 25 | 28 |
| Ciencias Naturales | 71 | 49 |
| Educación Física y Salud | 49 | 32 |
| Historia, Geografía y Ciencias Sociales | 82 | 77 |
| Inglés (Propuesta) | 69 | 16 |
| Lengua y Cultura de los Pueblos Originarios Ancestrales | 126 | 18 |
| Lenguaje y Comunicación | 161 | 29 |
| Matemática | 118 | 87 |
| Música | 35 | 28 |
| Orientación | 40 | 0 |
| Tecnología | 35 | 20 |
| **Total desarrollado en 4° básico** | **811** | **384** |

Las 1.195 entradas del nivel están resueltas. Las guías explicitan continuidad con 3°, método disciplinar, evidencia observable y resguardos de seguridad, privacidad, cultura y autoría.

[Ver mapa de 4° básico](docs/4-basico/README.md) · [Abrir sus once guías](docs/4-basico/README.md#las-11-asignaturas)

## Reconstrucción de 5° básico

| Asignatura | Clases desarrolladas | Experiencias integradas | Pendientes en la asignatura |
|---|---:|---:|---:|
| Matemática | 115 | 86 | 0 |
| Lenguaje y Comunicación | 166 | 29 | 0 |
| Ciencias Naturales | 64 | 58 | 0 |
| Historia, Geografía y Ciencias Sociales | 106 | 91 | 0 |
| Artes Visuales | 27 | 28 | 0 |
| Música | 35 | 28 | 0 |
| Educación Física y Salud | 49 | 32 | 0 |
| Orientación | 41 | 0 | 0 |
| Tecnología | 35 | 20 | 0 |
| Inglés | 76 | 16 | 0 |
| Inglés (Propuesta) | 71 | 32 | 0 |
| Lengua y Cultura de los Pueblos Originarios Ancestrales | 135 | 0 | 0 |
| **Total de 5° básico** | **920** | **420** | **0** |

Las 1.340 entradas del nivel están resueltas. [Ver programa completo de 5° básico](docs/5-basico/README.md).

## Desarrollo completo de 7° básico

| Asignatura | OA de contenido | Clases desarrolladas | OA transversales | Experiencias integradas | Pendientes en la asignatura |
|---|---:|---:|---:|---:|---:|
| Matemática | 19 | 83 | 19 | 82 | 0 |
| Lengua y Literatura | 25 | 147 | 8 | 33 | 0 |
| Ciencias Naturales | 15 | 72 | 21 | 89 | 0 |
| Historia, Geografía y Ciencias Sociales | 23 | 113 | 20 | 91 | 0 |
| Inglés | 16 | 80 | 5 | 21 | 0 |
| Educación Física y Salud | 5 | 25 | 7 | 28 | 0 |
| Artes Visuales | 6 | 29 | 8 | 33 | 0 |
| Inglés (Propuesta) | 13 | 65 | 21 | 85 | 0 |
| Lengua indígena | 8 | 41 | 0 | 0 | 0 |
| Música | 7 | 30 | 9 | 37 | 0 |
| Orientación | 10 | 49 | 0 | 0 | 0 |
| Tecnología | 6 | 26 | 4 | 16 | 0 |
| **Total del nivel** | **153** | **760** | **122** | **515** | **0** |

Las doce denominaciones cumplen el contrato automatizado y cuentan con [índice y guías propias](docs/7-basico/README.md). No quedan fichas secuenciadas ni borradores en 7° básico.

## Piloto conservado en otro nivel

- Lengua y Literatura 8° básico · LE08 OA 09 · 7 clases.

## Cobertura publicada

- 12 niveles, desde 1° básico hasta 4° medio.
- 35 asignaturas o denominaciones curriculares.
- 2.823 Objetivos de Aprendizaje.
- 595 vínculos de lectura asociados por MINEDUC.
- 2.823 páginas HTML de OA con anclas estables para las 12.997 clases.

## Próximo gate editorial

Un lote solo pasa a “desarrollado” cuando cada clase incluye contenido disciplinar específico, ejemplo o demostración, práctica y evaluación propias del OA. El validador rechaza campos ausentes, criterios insuficientes, conteos divergentes y páginas que no materialicen el contrato. Solo pasa a “revisado” con evidencia humana registrada. La automatización no certifica por sí sola calidad pedagógica.
