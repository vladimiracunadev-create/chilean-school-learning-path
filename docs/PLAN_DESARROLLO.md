# Plan maestro de desarrollo y control profesional

> [⬅️ Volver al centro documental](README.md) · [Estado editorial](../EDITORIAL_STATUS.md) · [Metodología](../METHODOLOGY.md)

**Nivel activo:** 8° básico — nivel en desarrollo · **Asignatura activa:** Educación Física y Salud · **Unidad de entrega:** nivel completo

Este documento es la fuente de seguimiento del desarrollo pedagógico. Publicar archivos no cierra el desarrollo interno de una asignatura: deben cumplirse sus gates automatizados y mantenerse separadas la producción interna y la revisión profesional humana.

## Flujo sostenido

~~~mermaid
flowchart LR
    A[Investigar OA e indicadores] --> B[Diseñar progresión]
    B --> C[Escribir clases]
    C --> D[Control interno]
    D --> E[Markdown + HTML]
    E --> F[CI verde]
    F --> G[Cerrar desarrollo interno]
    G --> H[Revisión profesional]
    H --> I[Declarar revisada]
~~~

## Definición y orden editorial de 1° a 8° básico

| Nivel | Orden | Asignatura | OA disciplinares | Clases disciplinares | Habilidades/actitudes a integrar | Estado |
|---|---:|---|---:|---:|---:|---|
| 1° básico | 1 | Matemática | 20 | 83 | 16 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 2 | Lenguaje y Comunicación | 26 | 131 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 3 | Ciencias Naturales | 12 | 49 | 10 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 4 | Historia, Geografía y Ciencias Sociales | 15 | 68 | 16 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 5 | Artes Visuales | 5 | 24 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 6 | Música | 7 | 29 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 7 | Educación Física y Salud | 11 | 48 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 8 | Orientación | 8 | 35 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 9 | Tecnología | 6 | 26 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 10 | Inglés (Propuesta) | 14 | 69 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 1° básico | 11 | Lengua y Cultura de los Pueblos Originarios Ancestrales | 29 | 129 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 1 | Matemática | 22 | 93 | 15 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 2 | Lenguaje y Comunicación | 30 | 149 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 3 | Ciencias Naturales | 14 | 57 | 11 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 4 | Historia, Geografía y Ciencias Sociales | 16 | 72 | 18 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 5 | Artes Visuales | 5 | 24 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 6 | Música | 7 | 29 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 7 | Educación Física y Salud | 11 | 47 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 8 | Orientación | 8 | 35 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 9 | Tecnología | 7 | 31 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 10 | Inglés (Propuesta) | 14 | 68 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 2° básico | 11 | Lengua y Cultura de los Pueblos Originarios Ancestrales | 27 | 116 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 1 | Matemática | 26 | 112 | 20 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 2 | Lenguaje y Comunicación | 31 | 157 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 3 | Ciencias Naturales | 13 | 55 | 12 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 4 | Historia, Geografía y Ciencias Sociales | 16 | 72 | 18 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 5 | Artes Visuales | 5 | 25 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 6 | Música | 8 | 35 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 7 | Educación Física y Salud | 11 | 48 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 8 | Orientación | 8 | 35 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 9 | Tecnología | 7 | 33 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 10 | Inglés (Propuesta) | 14 | 69 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 3° básico | 11 | Lengua y Cultura de los Pueblos Originarios Ancestrales | 26 | 116 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 1 | Matemática | 27 | 118 | 20 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 2 | Lenguaje y Comunicación | 30 | 161 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 3 | Ciencias Naturales | 17 | 71 | 12 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 4 | Historia, Geografía y Ciencias Sociales | 18 | 82 | 19 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 5 | Artes Visuales | 5 | 25 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 6 | Música | 8 | 35 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 7 | Educación Física y Salud | 11 | 49 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 8 | Orientación | 9 | 40 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 9 | Tecnología | 7 | 35 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 10 | Inglés (Propuesta) | 14 | 69 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 4° básico | 11 | Lengua y Cultura de los Pueblos Originarios Ancestrales | 29 | 126 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 1 | Matemática | 27 | 115 | 20 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 2 | Lenguaje y Comunicación | 30 | 166 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 3 | Ciencias Naturales | 14 | 64 | 14 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 4 | Historia, Geografía y Ciencias Sociales | 22 | 106 | 22 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 5 | Artes Visuales | 5 | 27 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 6 | Música | 8 | 35 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 7 | Educación Física y Salud | 11 | 49 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 8 | Orientación | 9 | 41 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 9 | Tecnología | 7 | 35 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 10 | Inglés | 16 | 76 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 11 | Inglés (Propuesta) | 15 | 71 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 5° básico | 12 | Lengua y Cultura de los Pueblos Originarios Ancestrales | 29 | 135 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 1 | Matemática | 24 | 98 | 20 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 2 | Lenguaje y Comunicación | 31 | 176 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 3 | Ciencias Naturales | 18 | 78 | 13 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 4 | Historia, Geografía y Ciencias Sociales | 26 | 116 | 23 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 5 | Artes Visuales | 5 | 27 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 6 | Música | 8 | 35 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 7 | Educación Física y Salud | 11 | 50 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 8 | Orientación | 9 | 41 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 9 | Tecnología | 7 | 37 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 10 | Inglés | 16 | 76 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 11 | Inglés (Propuesta) | 15 | 74 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 6° básico | 12 | Lengua y Cultura de los Pueblos Originarios Ancestrales | 29 | 144 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 1 | Matemática | 19 | 83 | 19 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 2 | Lengua y Literatura | 25 | 147 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 3 | Ciencias Naturales | 15 | 72 | 21 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 4 | Historia, Geografía y Ciencias Sociales | 23 | 113 | 20 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 5 | Artes Visuales | 6 | 29 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 6 | Música | 7 | 30 | 9 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 7 | Educación Física y Salud | 5 | 25 | 7 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 8 | Orientación | 10 | 49 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 9 | Tecnología | 6 | 26 | 4 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 10 | Inglés | 16 | 80 | 5 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 11 | Inglés (Propuesta) | 13 | 65 | 21 | Desarrollo interno completo · revisión humana pendiente |
| 7° básico | 12 | Lengua Indígena | 8 | 41 | 0 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 1 | Matemática | 17 | 77 | 19 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 2 | Lengua y Literatura | 26 | 155 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 3 | Ciencias Naturales | 15 | 74 | 21 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 4 | Historia, Geografía y Ciencias Sociales | 22 | 117 | 20 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 5 | Artes Visuales | 6 | 29 | 8 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 6 | Música | 7 | 30 | 9 | Desarrollo interno completo · revisión humana pendiente |
| 8° básico | 7 | Educación Física y Salud | 5 | 26 | 7 | Activa |
| 8° básico | 8 | Orientación | 10 | 49 | 0 | 0/10 OA desarrollados |
| 8° básico | 9 | Tecnología | 6 | 26 | 4 | 0/6 OA desarrollados |
| 8° básico | 10 | Inglés | 16 | 80 | 5 | 0/16 OA desarrollados |
| 8° básico | 11 | Inglés (Propuesta) | 13 | 65 | 0 | 0/13 OA desarrollados |
| 8° básico | 12 | Lengua Indígena | 9 | 43 | 0 | 0/9 OA desarrollados |

## Plan por asignatura e ítem

Cada fila corresponde a un ítem curricular real. Las clases indicadas son la dosificación actual; pueden ajustarse con evidencia, pero no desaparecer para inflar el avance.

### Matemática · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA01 OA 01` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-01) |
| `MA01 OA 02` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-02) |
| `MA01 OA 03` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-03) |
| `MA01 OA 04` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-04) |
| `MA01 OA 05` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-05) |
| `MA01 OA 06` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-06) |
| `MA01 OA 07` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-07) |
| `MA01 OA 08` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-08) |
| `MA01 OA 09` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-09) |
| `MA01 OA 10` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-10) |
| `MA01 OA 11` | Patrones y álgebra | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-11) |
| `MA01 OA 12` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-12) |
| `MA01 OA 13` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-13) |
| `MA01 OA 14` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-14) |
| `MA01 OA 15` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-15) |
| `MA01 OA 16` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-16) |
| `MA01 OA 17` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-17) |
| `MA01 OA 18` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-18) |
| `MA01 OA 19` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-19) |
| `MA01 OA 20` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/1-basico/ma01-oa-20) |

**Integración transversal documentada:** 16 ítems de habilidades o actitudes se incorporan en 68 experiencias dentro de las 83 clases de contenido; no se contabilizan como clases autónomas.

### Lenguaje y Comunicación · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE01 OA 01` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-01) |
| `LE01 OA 02` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-02) |
| `LE01 OA 03` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-03) |
| `LE01 OA 04` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-04) |
| `LE01 OA 05` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-05) |
| `LE01 OA 06` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-06) |
| `LE01 OA 07` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-07) |
| `LE01 OA 08` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-08) |
| `LE01 OA 09` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-09) |
| `LE01 OA 10` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-10) |
| `LE01 OA 11` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-11) |
| `LE01 OA 12` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-12) |
| `LE01 OA 13` | Escritura - Producción | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-13) |
| `LE01 OA 14` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-14) |
| `LE01 OA 15` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-15) |
| `LE01 OA 16` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-16) |
| `LE01 OA 17` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-17) |
| `LE01 OA 18` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-18) |
| `LE01 OA 19` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-19) |
| `LE01 OA 20` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-20) |
| `LE01 OA 21` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-21) |
| `LE01 OA 22` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-22) |
| `LE01 OA 23` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-23) |
| `LE01 OA 24` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-24) |
| `LE01 OA 25` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-25) |
| `LE01 OA 26` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/1-basico/le01-oa-26) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 29 experiencias dentro de las 131 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN01 OA 01` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-01) |
| `CN01 OA 02` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-02) |
| `CN01 OA 03` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-03) |
| `CN01 OA 04` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-04) |
| `CN01 OA 05` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-05) |
| `CN01 OA 06` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-06) |
| `CN01 OA 07` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-07) |
| `CN01 OA 08` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-08) |
| `CN01 OA 09` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-09) |
| `CN01 OA 10` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-10) |
| `CN01 OA 11` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-11) |
| `CN01 OA 12` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/1-basico/cn01-oa-12) |

**Integración transversal documentada:** 10 ítems de habilidades o actitudes se incorporan en 40 experiencias dentro de las 49 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI01 OA 01` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-01) |
| `HI01 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-02) |
| `HI01 OA 03` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-03) |
| `HI01 OA 04` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-04) |
| `HI01 OA 05` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-05) |
| `HI01 OA 06` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-06) |
| `HI01 OA 07` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-07) |
| `HI01 OA 08` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-08) |
| `HI01 OA 09` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-09) |
| `HI01 OA 10` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-10) |
| `HI01 OA 11` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-11) |
| `HI01 OA 12` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-12) |
| `HI01 OA 13` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-13) |
| `HI01 OA 14` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-14) |
| `HI01 OA 15` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/1-basico/hi01-oa-15) |

**Integración transversal documentada:** 16 ítems de habilidades o actitudes se incorporan en 64 experiencias dentro de las 68 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR01 OA 01` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/1-basico/ar01-oa-01) |
| `AR01 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/1-basico/ar01-oa-02) |
| `AR01 OA 03` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/1-basico/ar01-oa-03) |
| `AR01 OA 04` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/1-basico/ar01-oa-04) |
| `AR01 OA 05` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/1-basico/ar01-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 24 clases de contenido; no se contabilizan como clases autónomas.

### Música · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU01 OA 01` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-01) |
| `MU01 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-02) |
| `MU01 OA 03` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-03) |
| `MU01 OA 04` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-04) |
| `MU01 OA 05` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-05) |
| `MU01 OA 06` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-06) |
| `MU01 OA 07` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/1-basico/mu01-oa-07) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 29 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF01 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-01) |
| `EF01 OA 02` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-02) |
| `EF01 OA 03` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-03) |
| `EF01 OA 04` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-04) |
| `EF01 OA 05` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-05) |
| `EF01 OA 06` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-06) |
| `EF01 OA 07` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-07) |
| `EF01 OA 08` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-08) |
| `EF01 OA 09` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-09) |
| `EF01 OA 10` | Seguridad, juego limpio y liderazgo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-10) |
| `EF01 OA 11` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/1-basico/ef01-oa-11) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 48 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR01 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-01) |
| `OR01 OA 02` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-02) |
| `OR01 OA 03` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-03) |
| `OR01 OA 04` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-04) |
| `OR01 OA 05` | Relaciones interpersonales | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-05) |
| `OR01 OA 06` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-06) |
| `OR01 OA 07` | Participación y pertenencia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-07) |
| `OR01 OA 08` | Trabajo escolar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/1-basico/or01-oa-08) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE01 OA 01` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/1-basico/te01-oa-01) |
| `TE01 OA 02` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/1-basico/te01-oa-02) |
| `TE01 OA 03` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/1-basico/te01-oa-03) |
| `TE01 OA 04` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/1-basico/te01-oa-04) |
| `TE01 OA 05` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/1-basico/te01-oa-05) |
| `TE01 OA 06` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/1-basico/te01-oa-06) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 20 experiencias dentro de las 26 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN01 OA 01` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-01) |
| `EN01 OA 02` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-02) |
| `EN01 OA 03` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-03) |
| `EN01 OA 04` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-04) |
| `EN01 OA 05` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-05) |
| `EN01 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-06) |
| `EN01 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-07) |
| `EN01 OA 08` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-08) |
| `EN01 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-09) |
| `EN01 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-10) |
| `EN01 OA 11` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-11) |
| `EN01 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-12) |
| `EN01 OA 13` | Expresión escrita | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-13) |
| `EN01 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/1-basico/en01-oa-14) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 69 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Cultura de los Pueblos Originarios Ancestrales · 1° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LC01 OA LF01` | Contexto de fortalecimiento y desarrollo de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lf01) |
| `LC01 OA LF02` | Contexto de fortalecimiento y desarrollo de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lf02) |
| `LC01 OA LF03` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lf03) |
| `LC01 OA LF04` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lf04) |
| `LC01 OA LF05` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lf05) |
| `LC01 OA LF06` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lf06) |
| `LC01 OA LR01` | Contexto de rescate y revitalización de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lr01) |
| `LC01 OA LR02` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lr02) |
| `LC01 OA LR03` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lr03) |
| `LC01 OA LR04` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lr04) |
| `LC01 OA LR05` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lr05) |
| `LC01 OA LR06` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-lr06) |
| `LC01 OA LS01` | Contexto de Sensibilización sobre la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-ls01) |
| `LC01 OA LS02` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-ls02) |
| `LC01 OA LS03` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-ls03) |
| `LC01 OA LS04` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-ls04) |
| `LC01 OA LS05` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-ls05) |
| `LC01 OA LS06` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-ls06) |
| `LC01 OA 10` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-10) |
| `LC01 OA 11` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-11) |
| `LC01 OA 12` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-12) |
| `LC01 OA 13` | Cosmovisión de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-13) |
| `LC01 OA 14` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-14) |
| `LC01 OA 15` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-15) |
| `LC01 OA 16` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-16) |
| `LC01 OA 17` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-17) |
| `LC01 OA 07` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-07) |
| `LC01 OA 08` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-08) |
| `LC01 OA 09` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/1-basico/lc01-oa-09) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 18 experiencias dentro de las 129 clases de contenido; no se contabilizan como clases autónomas.

### Matemática · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA02 OA 01` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-01) |
| `MA02 OA 02` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-02) |
| `MA02 OA 03` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-03) |
| `MA02 OA 04` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-04) |
| `MA02 OA 05` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-05) |
| `MA02 OA 06` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-06) |
| `MA02 OA 07` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-07) |
| `MA02 OA 08` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-08) |
| `MA02 OA 09` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-09) |
| `MA02 OA 10` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-10) |
| `MA02 OA 11` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-11) |
| `MA02 OA 12` | Patrones y álgebra | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-12) |
| `MA02 OA 13` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-13) |
| `MA02 OA 14` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-14) |
| `MA02 OA 15` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-15) |
| `MA02 OA 16` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-16) |
| `MA02 OA 17` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-17) |
| `MA02 OA 18` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-18) |
| `MA02 OA 19` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-19) |
| `MA02 OA 20` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-20) |
| `MA02 OA 21` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-21) |
| `MA02 OA 22` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-22) |

**Integración transversal documentada:** 15 ítems de habilidades o actitudes se incorporan en 64 experiencias dentro de las 93 clases de contenido; no se contabilizan como clases autónomas.

### Lenguaje y Comunicación · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE02 OA 01` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-01) |
| `LE02 OA 02` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-02) |
| `LE02 OA 03` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-03) |
| `LE02 OA 04` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-04) |
| `LE02 OA 05` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-05) |
| `LE02 OA 06` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-06) |
| `LE02 OA 07` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-07) |
| `LE02 OA 08` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-08) |
| `LE02 OA 09` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-09) |
| `LE02 OA 10` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-10) |
| `LE02 OA 11` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-11) |
| `LE02 OA 12` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-12) |
| `LE02 OA 13` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-13) |
| `LE02 OA 14` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-14) |
| `LE02 OA 15` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-15) |
| `LE02 OA 16` | Escritura - Producción | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-16) |
| `LE02 OA 17` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-17) |
| `LE02 OA 18` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-18) |
| `LE02 OA 19` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-19) |
| `LE02 OA 20` | Escritura - Producción | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-20) |
| `LE02 OA 21` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-21) |
| `LE02 OA 22` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-22) |
| `LE02 OA 23` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-23) |
| `LE02 OA 24` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-24) |
| `LE02 OA 25` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-25) |
| `LE02 OA 26` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-26) |
| `LE02 OA 27` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-27) |
| `LE02 OA 28` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-28) |
| `LE02 OA 29` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-29) |
| `LE02 OA 30` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/2-basico/le02-oa-30) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 29 experiencias dentro de las 149 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN02 OA 01` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-01) |
| `CN02 OA 02` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-02) |
| `CN02 OA 03` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-03) |
| `CN02 OA 04` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-04) |
| `CN02 OA 05` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-05) |
| `CN02 OA 06` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-06) |
| `CN02 OA 07` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-07) |
| `CN02 OA 08` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-08) |
| `CN02 OA 09` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-09) |
| `CN02 OA 10` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-10) |
| `CN02 OA 11` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-11) |
| `CN02 OA 12` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-12) |
| `CN02 OA 13` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-13) |
| `CN02 OA 14` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/2-basico/cn02-oa-14) |

**Integración transversal documentada:** 11 ítems de habilidades o actitudes se incorporan en 44 experiencias dentro de las 57 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI02 OA 01` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-01) |
| `HI02 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-02) |
| `HI02 OA 03` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-03) |
| `HI02 OA 04` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-04) |
| `HI02 OA 05` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-05) |
| `HI02 OA 06` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-06) |
| `HI02 OA 07` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-07) |
| `HI02 OA 08` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-08) |
| `HI02 OA 09` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-09) |
| `HI02 OA 10` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-10) |
| `HI02 OA 11` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-11) |
| `HI02 OA 12` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-12) |
| `HI02 OA 13` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-13) |
| `HI02 OA 14` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-14) |
| `HI02 OA 15` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-15) |
| `HI02 OA 16` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/2-basico/hi02-oa-16) |

**Integración transversal documentada:** 18 ítems de habilidades o actitudes se incorporan en 72 experiencias dentro de las 72 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR02 OA 01` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/2-basico/ar02-oa-01) |
| `AR02 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/2-basico/ar02-oa-02) |
| `AR02 OA 03` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/2-basico/ar02-oa-03) |
| `AR02 OA 04` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/2-basico/ar02-oa-04) |
| `AR02 OA 05` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/2-basico/ar02-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 24 clases de contenido; no se contabilizan como clases autónomas.

### Música · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU02 OA 01` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-01) |
| `MU02 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-02) |
| `MU02 OA 03` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-03) |
| `MU02 OA 04` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-04) |
| `MU02 OA 05` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-05) |
| `MU02 OA 06` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-06) |
| `MU02 OA 07` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/2-basico/mu02-oa-07) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 29 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF02 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-01) |
| `EF02 OA 02` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-02) |
| `EF02 OA 03` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-03) |
| `EF02 OA 04` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-04) |
| `EF02 OA 05` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-05) |
| `EF02 OA 06` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-06) |
| `EF02 OA 07` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-07) |
| `EF02 OA 08` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-08) |
| `EF02 OA 09` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-09) |
| `EF02 OA 10` | Seguridad, juego limpio y liderazgo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-10) |
| `EF02 OA 11` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/2-basico/ef02-oa-11) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 47 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR02 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-01) |
| `OR02 OA 02` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-02) |
| `OR02 OA 03` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-03) |
| `OR02 OA 04` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-04) |
| `OR02 OA 05` | Relaciones interpersonales | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-05) |
| `OR02 OA 06` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-06) |
| `OR02 OA 07` | Participación y pertenencia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-07) |
| `OR02 OA 08` | Trabajo escolar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/2-basico/or02-oa-08) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE02 OA 01` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-01) |
| `TE02 OA 02` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-02) |
| `TE02 OA 03` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-03) |
| `TE02 OA 04` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-04) |
| `TE02 OA 05` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-05) |
| `TE02 OA 06` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-06) |
| `TE02 OA 07` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/2-basico/te02-oa-07) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 20 experiencias dentro de las 31 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN02 OA 01` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-01) |
| `EN02 OA 02` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-02) |
| `EN02 OA 03` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-03) |
| `EN02 OA 04` | Comprensión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-04) |
| `EN02 OA 05` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-05) |
| `EN02 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-06) |
| `EN02 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-07) |
| `EN02 OA 08` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-08) |
| `EN02 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-09) |
| `EN02 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-10) |
| `EN02 OA 11` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-11) |
| `EN02 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-12) |
| `EN02 OA 13` | Expresión escrita | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-13) |
| `EN02 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/2-basico/en02-oa-14) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 68 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Cultura de los Pueblos Originarios Ancestrales · 2° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LC02 OA LF01` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lf01) |
| `LC02 OA LF02` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lf02) |
| `LC02 OA LF03` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lf03) |
| `LC02 OA LF04` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lf04) |
| `LC02 OA LF05` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lf05) |
| `LC02 OA LR01` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lr01) |
| `LC02 OA LR02` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lr02) |
| `LC02 OA LR03` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lr03) |
| `LC02 OA LR04` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lr04) |
| `LC02 OA LR05` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-lr05) |
| `LC02 OA LS01` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-ls01) |
| `LC02 OA LS02` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-ls02) |
| `LC02 OA LS03` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-ls03) |
| `LC02 OA LS04` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-ls04) |
| `LC02 OA LS05` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-ls05) |
| `LC02 OA 10` | Cosmovisión de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-10) |
| `LC02 OA 11` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-11) |
| `LC02 OA 12` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-12) |
| `LC02 OA 13` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-13) |
| `LC02 OA 14` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-14) |
| `LC02 OA 15` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-15) |
| `LC02 OA 16` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-16) |
| `LC02 OA 17` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-17) |
| `LC02 OA 06` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-06) |
| `LC02 OA 07` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-07) |
| `LC02 OA 08` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-08) |
| `LC02 OA 09` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/2-basico/lc02-oa-09) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 18 experiencias dentro de las 116 clases de contenido; no se contabilizan como clases autónomas.

### Matemática · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA03 OA 01` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-01) |
| `MA03 OA 02` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-02) |
| `MA03 OA 03` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-03) |
| `MA03 OA 04` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-04) |
| `MA03 OA 05` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-05) |
| `MA03 OA 06` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-06) |
| `MA03 OA 07` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-07) |
| `MA03 OA 08` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-08) |
| `MA03 OA 09` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-09) |
| `MA03 OA 10` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-10) |
| `MA03 OA 11` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-11) |
| `MA03 OA 12` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-12) |
| `MA03 OA 13` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-13) |
| `MA03 OA 14` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-14) |
| `MA03 OA 15` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-15) |
| `MA03 OA 16` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-16) |
| `MA03 OA 17` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-17) |
| `MA03 OA 18` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-18) |
| `MA03 OA 19` | Medición | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-19) |
| `MA03 OA 20` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-20) |
| `MA03 OA 21` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-21) |
| `MA03 OA 22` | Medición | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-22) |
| `MA03 OA 23` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-23) |
| `MA03 OA 24` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-24) |
| `MA03 OA 25` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-25) |
| `MA03 OA 26` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-26) |

**Integración transversal documentada:** 20 ítems de habilidades o actitudes se incorporan en 87 experiencias dentro de las 112 clases de contenido; no se contabilizan como clases autónomas.

### Lenguaje y Comunicación · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE03 OA 01` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-01) |
| `LE03 OA 02` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-02) |
| `LE03 OA 03` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-03) |
| `LE03 OA 04` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-04) |
| `LE03 OA 05` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-05) |
| `LE03 OA 06` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-06) |
| `LE03 OA 07` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-07) |
| `LE03 OA 08` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-08) |
| `LE03 OA 09` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-09) |
| `LE03 OA 10` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-10) |
| `LE03 OA 11` | Lectura - Comprensión | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-11) |
| `LE03 OA 12` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-12) |
| `LE03 OA 13` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-13) |
| `LE03 OA 14` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-14) |
| `LE03 OA 15` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-15) |
| `LE03 OA 16` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-16) |
| `LE03 OA 17` | Escritura - Producción | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-17) |
| `LE03 OA 18` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-18) |
| `LE03 OA 19` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-19) |
| `LE03 OA 20` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-20) |
| `LE03 OA 21` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-21) |
| `LE03 OA 22` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-22) |
| `LE03 OA 23` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-23) |
| `LE03 OA 24` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-24) |
| `LE03 OA 25` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-25) |
| `LE03 OA 26` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-26) |
| `LE03 OA 27` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-27) |
| `LE03 OA 28` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-28) |
| `LE03 OA 29` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-29) |
| `LE03 OA 30` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-30) |
| `LE03 OA 31` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/3-basico/le03-oa-31) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 29 experiencias dentro de las 157 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN03 OA 01` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-01) |
| `CN03 OA 02` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-02) |
| `CN03 OA 03` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-03) |
| `CN03 OA 04` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-04) |
| `CN03 OA 05` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-05) |
| `CN03 OA 06` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-06) |
| `CN03 OA 07` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-07) |
| `CN03 OA 08` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-08) |
| `CN03 OA 09` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-09) |
| `CN03 OA 10` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-10) |
| `CN03 OA 11` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-11) |
| `CN03 OA 12` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-12) |
| `CN03 OA 13` | Ciencias de la Tierra y el Universo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/3-basico/cn03-oa-13) |

**Integración transversal documentada:** 12 ítems de habilidades o actitudes se incorporan en 49 experiencias dentro de las 55 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI03 OA 01` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-01) |
| `HI03 OA 02` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-02) |
| `HI03 OA 03` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-03) |
| `HI03 OA 04` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-04) |
| `HI03 OA 05` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-05) |
| `HI03 OA 06` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-06) |
| `HI03 OA 07` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-07) |
| `HI03 OA 08` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-08) |
| `HI03 OA 09` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-09) |
| `HI03 OA 10` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-10) |
| `HI03 OA 11` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-11) |
| `HI03 OA 12` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-12) |
| `HI03 OA 13` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-13) |
| `HI03 OA 14` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-14) |
| `HI03 OA 15` | Formación ciudadana | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-15) |
| `HI03 OA 16` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/3-basico/hi03-oa-16) |

**Integración transversal documentada:** 18 ítems de habilidades o actitudes se incorporan en 72 experiencias dentro de las 72 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR03 OA 01` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/3-basico/ar03-oa-01) |
| `AR03 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/3-basico/ar03-oa-02) |
| `AR03 OA 03` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/3-basico/ar03-oa-03) |
| `AR03 OA 04` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/3-basico/ar03-oa-04) |
| `AR03 OA 05` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/3-basico/ar03-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 25 clases de contenido; no se contabilizan como clases autónomas.

### Música · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU03 OA 01` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-01) |
| `MU03 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-02) |
| `MU03 OA 03` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-03) |
| `MU03 OA 04` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-04) |
| `MU03 OA 05` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-05) |
| `MU03 OA 06` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-06) |
| `MU03 OA 07` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-07) |
| `MU03 OA 08` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/3-basico/mu03-oa-08) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 35 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF03 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-01) |
| `EF03 OA 02` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-02) |
| `EF03 OA 03` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-03) |
| `EF03 OA 04` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-04) |
| `EF03 OA 05` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-05) |
| `EF03 OA 06` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-06) |
| `EF03 OA 07` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-07) |
| `EF03 OA 08` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-08) |
| `EF03 OA 09` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-09) |
| `EF03 OA 10` | Seguridad, juego limpio y liderazgo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-10) |
| `EF03 OA 11` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/3-basico/ef03-oa-11) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 48 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR03 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-01) |
| `OR03 OA 02` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-02) |
| `OR03 OA 03` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-03) |
| `OR03 OA 04` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-04) |
| `OR03 OA 05` | Relaciones interpersonales | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-05) |
| `OR03 OA 06` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-06) |
| `OR03 OA 07` | Participación y pertenencia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-07) |
| `OR03 OA 08` | Trabajo escolar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/3-basico/or03-oa-08) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE03 OA 01` | Diseñar, hacer y probar | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-01) |
| `TE03 OA 02` | Diseñar, hacer y probar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-02) |
| `TE03 OA 03` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-03) |
| `TE03 OA 04` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-04) |
| `TE03 OA 05` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-05) |
| `TE03 OA 06` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-06) |
| `TE03 OA 07` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/3-basico/te03-oa-07) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 20 experiencias dentro de las 33 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN03 OA 01` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-01) |
| `EN03 OA 02` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-02) |
| `EN03 OA 03` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-03) |
| `EN03 OA 04` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-04) |
| `EN03 OA 05` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-05) |
| `EN03 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-06) |
| `EN03 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-07) |
| `EN03 OA 08` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-08) |
| `EN03 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-09) |
| `EN03 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-10) |
| `EN03 OA 11` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-11) |
| `EN03 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-12) |
| `EN03 OA 13` | Expresión escrita | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-13) |
| `EN03 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/3-basico/en03-oa-14) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 69 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Cultura de los Pueblos Originarios Ancestrales · 3° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LC03 OA LF01` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lf01) |
| `LC03 OA LF02` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lf02) |
| `LC03 OA LF03` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lf03) |
| `LC03 OA LF04` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lf04) |
| `LC03 OA LF05` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lf05) |
| `LC03 OA LR01` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lr01) |
| `LC03 OA LR02` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lr02) |
| `LC03 OA LR03` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lr03) |
| `LC03 OA LR04` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lr04) |
| `LC03 OA LR05` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-lr05) |
| `LC03 OA LS01` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-ls01) |
| `LC03 OA LS02` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-ls02) |
| `LC03 OA LS03` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-ls03) |
| `LC03 OA LS04` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-ls04) |
| `LC03 OA LS05` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-ls05) |
| `LC03 OA 09` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-09) |
| `LC03 OA 10` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-10) |
| `LC03 OA 11` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-11) |
| `LC03 OA 12` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-12) |
| `LC03 OA 13` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-13) |
| `LC03 OA 14` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-14) |
| `LC03 OA 15` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-15) |
| `LC03 OA 16` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-16) |
| `LC03 OA 06` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-06) |
| `LC03 OA 07` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-07) |
| `LC03 OA 08` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/3-basico/lc03-oa-08) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 18 experiencias dentro de las 116 clases de contenido; no se contabilizan como clases autónomas.

### Matemática · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA04 OA 01` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-01) |
| `MA04 OA 02` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-02) |
| `MA04 OA 03` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-03) |
| `MA04 OA 04` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-04) |
| `MA04 OA 05` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-05) |
| `MA04 OA 06` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-06) |
| `MA04 OA 07` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-07) |
| `MA04 OA 08` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-08) |
| `MA04 OA 09` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-09) |
| `MA04 OA 10` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-10) |
| `MA04 OA 11` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-11) |
| `MA04 OA 12` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-12) |
| `MA04 OA 13` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-13) |
| `MA04 OA 14` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-14) |
| `MA04 OA 15` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-15) |
| `MA04 OA 16` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-16) |
| `MA04 OA 17` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-17) |
| `MA04 OA 18` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-18) |
| `MA04 OA 19` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-19) |
| `MA04 OA 20` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-20) |
| `MA04 OA 21` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-21) |
| `MA04 OA 22` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-22) |
| `MA04 OA 23` | Medición | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-23) |
| `MA04 OA 24` | Medición | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-24) |
| `MA04 OA 25` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-25) |
| `MA04 OA 26` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-26) |
| `MA04 OA 27` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/4-basico/ma04-oa-27) |

**Integración transversal documentada:** 20 ítems de habilidades o actitudes se incorporan en 87 experiencias dentro de las 118 clases de contenido; no se contabilizan como clases autónomas.

### Lenguaje y Comunicación · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE04 OA 01` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-01) |
| `LE04 OA 02` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-02) |
| `LE04 OA 03` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-03) |
| `LE04 OA 04` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-04) |
| `LE04 OA 05` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-05) |
| `LE04 OA 06` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-06) |
| `LE04 OA 07` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-07) |
| `LE04 OA 08` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-08) |
| `LE04 OA 09` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-09) |
| `LE04 OA 10` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-10) |
| `LE04 OA 11` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-11) |
| `LE04 OA 12` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-12) |
| `LE04 OA 13` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-13) |
| `LE04 OA 14` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-14) |
| `LE04 OA 15` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-15) |
| `LE04 OA 16` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-16) |
| `LE04 OA 17` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-17) |
| `LE04 OA 18` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-18) |
| `LE04 OA 19` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-19) |
| `LE04 OA 20` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-20) |
| `LE04 OA 21` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-21) |
| `LE04 OA 22` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-22) |
| `LE04 OA 23` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-23) |
| `LE04 OA 24` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-24) |
| `LE04 OA 25` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-25) |
| `LE04 OA 26` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-26) |
| `LE04 OA 27` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-27) |
| `LE04 OA 28` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-28) |
| `LE04 OA 29` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-29) |
| `LE04 OA 30` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/4-basico/le04-oa-30) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 29 experiencias dentro de las 161 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN04 OA 01` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-01) |
| `CN04 OA 02` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-02) |
| `CN04 OA 03` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-03) |
| `CN04 OA 04` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-04) |
| `CN04 OA 05` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-05) |
| `CN04 OA 06` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-06) |
| `CN04 OA 07` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-07) |
| `CN04 OA 08` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-08) |
| `CN04 OA 09` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-09) |
| `CN04 OA 10` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-10) |
| `CN04 OA 11` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-11) |
| `CN04 OA 12` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-12) |
| `CN04 OA 13` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-13) |
| `CN04 OA 14` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-14) |
| `CN04 OA 15` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-15) |
| `CN04 OA 16` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-16) |
| `CN04 OA 17` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/4-basico/cn04-oa-17) |

**Integración transversal documentada:** 12 ítems de habilidades o actitudes se incorporan en 49 experiencias dentro de las 71 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI04 OA 01` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-01) |
| `HI04 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-02) |
| `HI04 OA 03` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-03) |
| `HI04 OA 04` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-04) |
| `HI04 OA 05` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-05) |
| `HI04 OA 06` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-06) |
| `HI04 OA 07` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-07) |
| `HI04 OA 08` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-08) |
| `HI04 OA 09` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-09) |
| `HI04 OA 10` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-10) |
| `HI04 OA 11` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-11) |
| `HI04 OA 12` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-12) |
| `HI04 OA 13` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-13) |
| `HI04 OA 14` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-14) |
| `HI04 OA 15` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-15) |
| `HI04 OA 16` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-16) |
| `HI04 OA 17` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-17) |
| `HI04 OA 18` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/4-basico/hi04-oa-18) |

**Integración transversal documentada:** 19 ítems de habilidades o actitudes se incorporan en 77 experiencias dentro de las 82 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR04 OA 01` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/4-basico/ar04-oa-01) |
| `AR04 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/4-basico/ar04-oa-02) |
| `AR04 OA 03` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/4-basico/ar04-oa-03) |
| `AR04 OA 04` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/4-basico/ar04-oa-04) |
| `AR04 OA 05` | Apreciar y responder frente al arte | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/4-basico/ar04-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 25 clases de contenido; no se contabilizan como clases autónomas.

### Música · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU04 OA 01` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-01) |
| `MU04 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-02) |
| `MU04 OA 03` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-03) |
| `MU04 OA 04` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-04) |
| `MU04 OA 05` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-05) |
| `MU04 OA 06` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-06) |
| `MU04 OA 07` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-07) |
| `MU04 OA 08` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/4-basico/mu04-oa-08) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 35 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF04 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-01) |
| `EF04 OA 02` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-02) |
| `EF04 OA 03` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-03) |
| `EF04 OA 04` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-04) |
| `EF04 OA 05` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-05) |
| `EF04 OA 06` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-06) |
| `EF04 OA 07` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-07) |
| `EF04 OA 08` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-08) |
| `EF04 OA 09` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-09) |
| `EF04 OA 10` | Seguridad, juego limpio y liderazgo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-10) |
| `EF04 OA 11` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/4-basico/ef04-oa-11) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 49 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR04 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-01) |
| `OR04 OA 02` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-02) |
| `OR04 OA 03` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-03) |
| `OR04 OA 04` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-04) |
| `OR04 OA 05` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-05) |
| `OR04 OA 06` | Relaciones interpersonales | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-06) |
| `OR04 OA 07` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-07) |
| `OR04 OA 08` | Participación y pertenencia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-08) |
| `OR04 OA 09` | Trabajo escolar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/4-basico/or04-oa-09) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE04 OA 01` | Diseñar, hacer y probar | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-01) |
| `TE04 OA 02` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-02) |
| `TE04 OA 03` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-03) |
| `TE04 OA 04` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-04) |
| `TE04 OA 05` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-05) |
| `TE04 OA 06` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-06) |
| `TE04 OA 07` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/4-basico/te04-oa-07) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 20 experiencias dentro de las 35 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN04 OA 01` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-01) |
| `EN04 OA 02` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-02) |
| `EN04 OA 03` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-03) |
| `EN04 OA 04` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-04) |
| `EN04 OA 05` | Comprensión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-05) |
| `EN04 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-06) |
| `EN04 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-07) |
| `EN04 OA 08` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-08) |
| `EN04 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-09) |
| `EN04 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-10) |
| `EN04 OA 11` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-11) |
| `EN04 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-12) |
| `EN04 OA 13` | Expresión escrita | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-13) |
| `EN04 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/4-basico/en04-oa-14) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 69 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Cultura de los Pueblos Originarios Ancestrales · 4° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LC04 OA LF01` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lf01) |
| `LC04 OA LF02` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lf02) |
| `LC04 OA LF03` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lf03) |
| `LC04 OA LF04` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lf04) |
| `LC04 OA LF05` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lf05) |
| `LC04 OA LF06` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lf06) |
| `LC04 OA LR01` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lr01) |
| `LC04 OA LR02` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lr02) |
| `LC04 OA LR03` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lr03) |
| `LC04 OA LR04` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lr04) |
| `LC04 OA LR05` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lr05) |
| `LC04 OA LR06` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-lr06) |
| `LC04 OA LS01` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-ls01) |
| `LC04 OA LS02` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-ls02) |
| `LC04 OA LS03` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-ls03) |
| `LC04 OA LS04` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-ls04) |
| `LC04 OA LS05` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-ls05) |
| `LC04 OA LS06` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-ls06) |
| `LC04 OA 10` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-10) |
| `LC04 OA 11` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-11) |
| `LC04 OA 12` | Cosmovisión de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-12) |
| `LC04 OA 13` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-13) |
| `LC04 OA 14` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-14) |
| `LC04 OA 15` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-15) |
| `LC04 OA 16` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-16) |
| `LC04 OA 17` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-17) |
| `LC04 OA 07` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-07) |
| `LC04 OA 08` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-08) |
| `LC04 OA 09` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/4-basico/lc04-oa-09) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 18 experiencias dentro de las 126 clases de contenido; no se contabilizan como clases autónomas.

### Matemática · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA05 OA 01` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-01) |
| `MA05 OA 02` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-02) |
| `MA05 OA 03` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-03) |
| `MA05 OA 04` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-04) |
| `MA05 OA 05` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-05) |
| `MA05 OA 06` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-06) |
| `MA05 OA 07` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-07) |
| `MA05 OA 08` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-08) |
| `MA05 OA 09` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-09) |
| `MA05 OA 10` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-10) |
| `MA05 OA 11` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-11) |
| `MA05 OA 12` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-12) |
| `MA05 OA 13` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-13) |
| `MA05 OA 14` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-14) |
| `MA05 OA 15` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-15) |
| `MA05 OA 16` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-16) |
| `MA05 OA 17` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-17) |
| `MA05 OA 18` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-18) |
| `MA05 OA 19` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-19) |
| `MA05 OA 20` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-20) |
| `MA05 OA 21` | Medición | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-21) |
| `MA05 OA 22` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-22) |
| `MA05 OA 23` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-23) |
| `MA05 OA 24` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-24) |
| `MA05 OA 25` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-25) |
| `MA05 OA 26` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-26) |
| `MA05 OA 27` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/5-basico/ma05-oa-27) |

**Integración transversal documentada:** 20 ítems de habilidades o actitudes se incorporan en 86 experiencias dentro de las 115 clases de contenido; no se contabilizan como clases autónomas.

### Lenguaje y Comunicación · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE05 OA 01` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-01) |
| `LE05 OA 02` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-02) |
| `LE05 OA 03` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-03) |
| `LE05 OA 04` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-04) |
| `LE05 OA 05` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-05) |
| `LE05 OA 06` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-06) |
| `LE05 OA 07` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-07) |
| `LE05 OA 08` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-08) |
| `LE05 OA 09` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-09) |
| `LE05 OA 10` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-10) |
| `LE05 OA 11` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-11) |
| `LE05 OA 12` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-12) |
| `LE05 OA 13` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-13) |
| `LE05 OA 14` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-14) |
| `LE05 OA 15` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-15) |
| `LE05 OA 16` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-16) |
| `LE05 OA 17` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-17) |
| `LE05 OA 18` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-18) |
| `LE05 OA 19` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-19) |
| `LE05 OA 20` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-20) |
| `LE05 OA 21` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-21) |
| `LE05 OA 22` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-22) |
| `LE05 OA 23` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-23) |
| `LE05 OA 24` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-24) |
| `LE05 OA 25` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-25) |
| `LE05 OA 26` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-26) |
| `LE05 OA 27` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-27) |
| `LE05 OA 28` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-28) |
| `LE05 OA 29` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-29) |
| `LE05 OA 30` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/5-basico/le05-oa-30) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 29 experiencias dentro de las 166 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN05 OA 01` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-01) |
| `CN05 OA 02` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-02) |
| `CN05 OA 03` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-03) |
| `CN05 OA 04` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-04) |
| `CN05 OA 05` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-05) |
| `CN05 OA 06` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-06) |
| `CN05 OA 07` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-07) |
| `CN05 OA 08` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-08) |
| `CN05 OA 09` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-09) |
| `CN05 OA 10` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-10) |
| `CN05 OA 11` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-11) |
| `CN05 OA 12` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-12) |
| `CN05 OA 13` | Ciencias de la Tierra y el Universo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-13) |
| `CN05 OA 14` | Ciencias de la Tierra y el Universo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/5-basico/cn05-oa-14) |

**Integración transversal documentada:** 14 ítems de habilidades o actitudes se incorporan en 58 experiencias dentro de las 64 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI05 OA 01` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-01) |
| `HI05 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-02) |
| `HI05 OA 03` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-03) |
| `HI05 OA 04` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-04) |
| `HI05 OA 05` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-05) |
| `HI05 OA 06` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-06) |
| `HI05 OA 07` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-07) |
| `HI05 OA 08` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-08) |
| `HI05 OA 09` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-09) |
| `HI05 OA 10` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-10) |
| `HI05 OA 11` | Geografía | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-11) |
| `HI05 OA 12` | Geografía | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-12) |
| `HI05 OA 13` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-13) |
| `HI05 OA 14` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-14) |
| `HI05 OA 15` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-15) |
| `HI05 OA 16` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-16) |
| `HI05 OA 17` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-17) |
| `HI05 OA 18` | Formación ciudadana | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-18) |
| `HI05 OA 19` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-19) |
| `HI05 OA 20` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-20) |
| `HI05 OA 21` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-21) |
| `HI05 OA 22` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/5-basico/hi05-oa-22) |

**Integración transversal documentada:** 22 ítems de habilidades o actitudes se incorporan en 91 experiencias dentro de las 106 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR05 OA 01` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/5-basico/ar05-oa-01) |
| `AR05 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/5-basico/ar05-oa-02) |
| `AR05 OA 03` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/5-basico/ar05-oa-03) |
| `AR05 OA 04` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/5-basico/ar05-oa-04) |
| `AR05 OA 05` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/5-basico/ar05-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 27 clases de contenido; no se contabilizan como clases autónomas.

### Música · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU05 OA 01` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-01) |
| `MU05 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-02) |
| `MU05 OA 03` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-03) |
| `MU05 OA 04` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-04) |
| `MU05 OA 05` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-05) |
| `MU05 OA 06` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-06) |
| `MU05 OA 07` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-07) |
| `MU05 OA 08` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/5-basico/mu05-oa-08) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 35 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF05 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-01) |
| `EF05 OA 02` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-02) |
| `EF05 OA 03` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-03) |
| `EF05 OA 04` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-04) |
| `EF05 OA 05` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-05) |
| `EF05 OA 06` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-06) |
| `EF05 OA 07` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-07) |
| `EF05 OA 08` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-08) |
| `EF05 OA 09` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-09) |
| `EF05 OA 10` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-10) |
| `EF05 OA 11` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/5-basico/ef05-oa-11) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 49 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR05 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-01) |
| `OR05 OA 02` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-02) |
| `OR05 OA 03` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-03) |
| `OR05 OA 04` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-04) |
| `OR05 OA 05` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-05) |
| `OR05 OA 06` | Relaciones interpersonales | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-06) |
| `OR05 OA 07` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-07) |
| `OR05 OA 08` | Participación y pertenencia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-08) |
| `OR05 OA 09` | Trabajo escolar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/5-basico/or05-oa-09) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE05 OA 01` | Diseñar, hacer y probar | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-01) |
| `TE05 OA 02` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-02) |
| `TE05 OA 03` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-03) |
| `TE05 OA 04` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-04) |
| `TE05 OA 05` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-05) |
| `TE05 OA 06` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-06) |
| `TE05 OA 07` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/5-basico/te05-oa-07) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 20 experiencias dentro de las 35 clases de contenido; no se contabilizan como clases autónomas.

### Inglés · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `IN05 OA 01` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-01) |
| `IN05 OA 02` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-02) |
| `IN05 OA 03` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-03) |
| `IN05 OA 04` | Comprensión auditiva | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-04) |
| `IN05 OA 05` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-05) |
| `IN05 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-06) |
| `IN05 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-07) |
| `IN05 OA 08` | Comprensión de lectura | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-08) |
| `IN05 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-09) |
| `IN05 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-10) |
| `IN05 OA 11` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-11) |
| `IN05 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-12) |
| `IN05 OA 13` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-13) |
| `IN05 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-14) |
| `IN05 OA 15` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-15) |
| `IN05 OA 16` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/5-basico/in05-oa-16) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 76 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN05 OA 01` | Comprensión auditiva | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-01) |
| `EN05 OA 02` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-02) |
| `EN05 OA 03` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-03) |
| `EN05 OA 04` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-04) |
| `EN05 OA 05` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-05) |
| `EN05 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-06) |
| `EN05 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-07) |
| `EN05 OA 08` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-08) |
| `EN05 OA 09` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-09) |
| `EN05 OA 10` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-10) |
| `EN05 OA 11` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-11) |
| `EN05 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-12) |
| `EN05 OA 13` | Expresión escrita | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-13) |
| `EN05 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-14) |
| `EN05 OA 15` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/5-basico/en05-oa-15) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 71 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Cultura de los Pueblos Originarios Ancestrales · 5° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LC05 OA LF01` | Contexto de fortalecimiento y desarrollo de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lf01) |
| `LC05 OA LF02` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lf02) |
| `LC05 OA LF03` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lf03) |
| `LC05 OA LF04` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lf04) |
| `LC05 OA LF05` | Contexto de fortalecimiento y desarrollo de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lf05) |
| `LC05 OA LF06` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lf06) |
| `LC05 OA LR01` | Contexto de rescate y revitalización de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lr01) |
| `LC05 OA LR02` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lr02) |
| `LC05 OA LR03` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lr03) |
| `LC05 OA LR04` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lr04) |
| `LC05 OA LR05` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lr05) |
| `LC05 OA LR06` | Contexto de rescate y revitalización de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-lr06) |
| `LC05 OA LS01` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-ls01) |
| `LC05 OA LS02` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-ls02) |
| `LC05 OA LS03` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-ls03) |
| `LC05 OA LS04` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-ls04) |
| `LC05 OA LS05` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-ls05) |
| `LC05 OA LS06` | Contexto de Sensibilización sobre la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-ls06) |
| `LC05 OA 10` | Cosmovisión de los pueblos originarios | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-10) |
| `LC05 OA 11` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-11) |
| `LC05 OA 12` | Cosmovisión de los pueblos originarios | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-12) |
| `LC05 OA 13` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-13) |
| `LC05 OA 14` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-14) |
| `LC05 OA 15` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-15) |
| `LC05 OA 16` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-16) |
| `LC05 OA 17` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-17) |
| `LC05 OA 07` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-07) |
| `LC05 OA 08` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-08) |
| `LC05 OA 09` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/5-basico/lc05-oa-09) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Matemática · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA06 OA 01` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-01) |
| `MA06 OA 02` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-02) |
| `MA06 OA 03` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-03) |
| `MA06 OA 04` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-04) |
| `MA06 OA 05` | Números y operaciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-05) |
| `MA06 OA 06` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-06) |
| `MA06 OA 07` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-07) |
| `MA06 OA 08` | Números y operaciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-08) |
| `MA06 OA 09` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-09) |
| `MA06 OA 10` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-10) |
| `MA06 OA 11` | Patrones y álgebra | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-11) |
| `MA06 OA 12` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-12) |
| `MA06 OA 13` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-13) |
| `MA06 OA 14` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-14) |
| `MA06 OA 15` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-15) |
| `MA06 OA 16` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-16) |
| `MA06 OA 17` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-17) |
| `MA06 OA 18` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-18) |
| `MA06 OA 19` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-19) |
| `MA06 OA 20` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-20) |
| `MA06 OA 21` | Medición | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-21) |
| `MA06 OA 22` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-22) |
| `MA06 OA 23` | Datos y probabilidades | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-23) |
| `MA06 OA 24` | Datos y probabilidades | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/6-basico/ma06-oa-24) |

**Integración transversal documentada:** 20 ítems de habilidades o actitudes se incorporan en 88 experiencias dentro de las 98 clases de contenido; no se contabilizan como clases autónomas.

### Lenguaje y Comunicación · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE06 OA 01` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-01) |
| `LE06 OA 02` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-02) |
| `LE06 OA 03` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-03) |
| `LE06 OA 04` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-04) |
| `LE06 OA 05` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-05) |
| `LE06 OA 06` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-06) |
| `LE06 OA 07` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-07) |
| `LE06 OA 08` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-08) |
| `LE06 OA 09` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-09) |
| `LE06 OA 10` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-10) |
| `LE06 OA 11` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-11) |
| `LE06 OA 12` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-12) |
| `LE06 OA 13` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-13) |
| `LE06 OA 14` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-14) |
| `LE06 OA 15` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-15) |
| `LE06 OA 16` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-16) |
| `LE06 OA 17` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-17) |
| `LE06 OA 18` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-18) |
| `LE06 OA 19` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-19) |
| `LE06 OA 20` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-20) |
| `LE06 OA 21` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-21) |
| `LE06 OA 22` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-22) |
| `LE06 OA 23` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-23) |
| `LE06 OA 24` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-24) |
| `LE06 OA 25` | Comunicación oral | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-25) |
| `LE06 OA 26` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-26) |
| `LE06 OA 27` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-27) |
| `LE06 OA 28` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-28) |
| `LE06 OA 29` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-29) |
| `LE06 OA 30` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-30) |
| `LE06 OA 31` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lenguaje-comunicacion/6-basico/le06-oa-31) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 29 experiencias dentro de las 176 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN06 OA 01` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-01) |
| `CN06 OA 02` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-02) |
| `CN06 OA 03` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-03) |
| `CN06 OA 04` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-04) |
| `CN06 OA 05` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-05) |
| `CN06 OA 06` | Ciencias de la Vida | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-06) |
| `CN06 OA 07` | Ciencias de la Vida | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-07) |
| `CN06 OA 08` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-08) |
| `CN06 OA 09` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-09) |
| `CN06 OA 10` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-10) |
| `CN06 OA 11` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-11) |
| `CN06 OA 12` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-12) |
| `CN06 OA 13` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-13) |
| `CN06 OA 14` | Ciencias Físicas y Químicas | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-14) |
| `CN06 OA 15` | Ciencias Físicas y Químicas | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-15) |
| `CN06 OA 16` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-16) |
| `CN06 OA 17` | Ciencias de la Tierra y el Universo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-17) |
| `CN06 OA 18` | Ciencias de la Tierra y el Universo | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ciencias-naturales/6-basico/cn06-oa-18) |

**Integración transversal documentada:** 13 ítems de habilidades o actitudes se incorporan en 53 experiencias dentro de las 78 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI06 OA 01` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-01) |
| `HI06 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-02) |
| `HI06 OA 03` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-03) |
| `HI06 OA 04` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-04) |
| `HI06 OA 05` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-05) |
| `HI06 OA 06` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-06) |
| `HI06 OA 07` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-07) |
| `HI06 OA 08` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-08) |
| `HI06 OA 09` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-09) |
| `HI06 OA 10` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-10) |
| `HI06 OA 11` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-11) |
| `HI06 OA 12` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-12) |
| `HI06 OA 13` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-13) |
| `HI06 OA 14` | Geografía | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-14) |
| `HI06 OA 15` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-15) |
| `HI06 OA 16` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-16) |
| `HI06 OA 17` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-17) |
| `HI06 OA 18` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-18) |
| `HI06 OA 19` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-19) |
| `HI06 OA 20` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-20) |
| `HI06 OA 21` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-21) |
| `HI06 OA 22` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-22) |
| `HI06 OA 23` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-23) |
| `HI06 OA 24` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-24) |
| `HI06 OA 25` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-25) |
| `HI06 OA 26` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/historia-geografia-ciencias-sociales/6-basico/hi06-oa-26) |

**Integración transversal documentada:** 23 ítems de habilidades o actitudes se incorporan en 96 experiencias dentro de las 116 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR06 OA 01` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/6-basico/ar06-oa-01) |
| `AR06 OA 02` | Expresar y crear visualmente | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/6-basico/ar06-oa-02) |
| `AR06 OA 03` | Expresar y crear visualmente | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/6-basico/ar06-oa-03) |
| `AR06 OA 04` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/6-basico/ar06-oa-04) |
| `AR06 OA 05` | Apreciar y responder frente al arte | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/artes-visuales/6-basico/ar06-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 27 clases de contenido; no se contabilizan como clases autónomas.

### Música · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU06 OA 01` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-01) |
| `MU06 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-02) |
| `MU06 OA 03` | Escuchar y apreciar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-03) |
| `MU06 OA 04` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-04) |
| `MU06 OA 05` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-05) |
| `MU06 OA 06` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-06) |
| `MU06 OA 07` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-07) |
| `MU06 OA 08` | Reflexionar y contextualizar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/musica/6-basico/mu06-oa-08) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 35 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF06 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-01) |
| `EF06 OA 02` | Habilidades motrices | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-02) |
| `EF06 OA 03` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-03) |
| `EF06 OA 04` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-04) |
| `EF06 OA 05` | Habilidades motrices | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-05) |
| `EF06 OA 06` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-06) |
| `EF06 OA 07` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-07) |
| `EF06 OA 08` | Vida activa y saludable | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-08) |
| `EF06 OA 09` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-09) |
| `EF06 OA 10` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-10) |
| `EF06 OA 11` | Seguridad, juego limpio y liderazgo | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/educacion-fisica-salud/6-basico/ef06-oa-11) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 50 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR06 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-01) |
| `OR06 OA 02` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-02) |
| `OR06 OA 03` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-03) |
| `OR06 OA 04` | Crecimiento personal | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-04) |
| `OR06 OA 05` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-05) |
| `OR06 OA 06` | Relaciones interpersonales | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-06) |
| `OR06 OA 07` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-07) |
| `OR06 OA 08` | Participación y pertenencia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-08) |
| `OR06 OA 09` | Trabajo escolar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/orientacion/6-basico/or06-oa-09) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE06 OA 01` | Diseñar, hacer y probar | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-01) |
| `TE06 OA 02` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-02) |
| `TE06 OA 03` | Diseñar, hacer y probar | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-03) |
| `TE06 OA 04` | Diseñar, hacer y probar | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-04) |
| `TE06 OA 05` | Tecnologías de la información y la comunicación | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-05) |
| `TE06 OA 06` | Tecnologías de la información y la comunicación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-06) |
| `TE06 OA 07` | Tecnologías de la información y la comunicación | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/tecnologia/6-basico/te06-oa-07) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 20 experiencias dentro de las 37 clases de contenido; no se contabilizan como clases autónomas.

### Inglés · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `IN06 OA 01` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-01) |
| `IN06 OA 02` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-02) |
| `IN06 OA 03` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-03) |
| `IN06 OA 04` | Comprensión auditiva | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-04) |
| `IN06 OA 05` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-05) |
| `IN06 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-06) |
| `IN06 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-07) |
| `IN06 OA 08` | Comprensión de lectura | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-08) |
| `IN06 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-09) |
| `IN06 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-10) |
| `IN06 OA 11` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-11) |
| `IN06 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-12) |
| `IN06 OA 13` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-13) |
| `IN06 OA 14` | Expresión escrita | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-14) |
| `IN06 OA 15` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-15) |
| `IN06 OA 16` | Expresión escrita | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles/6-basico/in06-oa-16) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 76 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN06 OA 01` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-01) |
| `EN06 OA 02` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-02) |
| `EN06 OA 03` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-03) |
| `EN06 OA 04` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-04) |
| `EN06 OA 05` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-05) |
| `EN06 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-06) |
| `EN06 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-07) |
| `EN06 OA 08` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-08) |
| `EN06 OA 09` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-09) |
| `EN06 OA 10` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-10) |
| `EN06 OA 11` | Expresión oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-11) |
| `EN06 OA 12` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-12) |
| `EN06 OA 13` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-13) |
| `EN06 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-14) |
| `EN06 OA 15` | Expresión escrita | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/ingles-propuesta/6-basico/en06-oa-15) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 32 experiencias dentro de las 74 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Cultura de los Pueblos Originarios Ancestrales · 6° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LC06 OA LF01` | Contexto de fortalecimiento y desarrollo de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lf01) |
| `LC06 OA LF02` | Contexto de fortalecimiento y desarrollo de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lf02) |
| `LC06 OA LF03` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lf03) |
| `LC06 OA LF04` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lf04) |
| `LC06 OA LF05` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lf05) |
| `LC06 OA LF06` | Contexto de fortalecimiento y desarrollo de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lf06) |
| `LC06 OA LR01` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lr01) |
| `LC06 OA LR02` | Contexto de rescate y revitalización de la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lr02) |
| `LC06 OA LR03` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lr03) |
| `LC06 OA LR04` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lr04) |
| `LC06 OA LR05` | Contexto de rescate y revitalización de la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lr05) |
| `LC06 OA LR06` | Contexto de rescate y revitalización de la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-lr06) |
| `LC06 OA LS01` | Contexto de Sensibilización sobre la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-ls01) |
| `LC06 OA LS02` | Contexto de Sensibilización sobre la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-ls02) |
| `LC06 OA LS03` | Contexto de Sensibilización sobre la lengua | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-ls03) |
| `LC06 OA LS04` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-ls04) |
| `LC06 OA LS05` | Contexto de Sensibilización sobre la lengua | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-ls05) |
| `LC06 OA LS06` | Contexto de Sensibilización sobre la lengua | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-ls06) |
| `LC06 OA 10` | Cosmovisión de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-10) |
| `LC06 OA 11` | Cosmovisión de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-11) |
| `LC06 OA 12` | Cosmovisión de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-12) |
| `LC06 OA 13` | Cosmovisión de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-13) |
| `LC06 OA 14` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-14) |
| `LC06 OA 15` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-15) |
| `LC06 OA 16` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-16) |
| `LC06 OA 17` | Patrimonio, tecnologías, técnicas, ciencias y artes ancestrales de los pueblos originarios | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-17) |
| `LC06 OA 07` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-07) |
| `LC06 OA 08` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-08) |
| `LC06 OA 09` | Territorio, territorialidad, identidad y memoria histórica de los pueblos originarios | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/1o-6o-basico/lengua-cultura-pueblos-originarios-ancestrales/6-basico/lc06-oa-09) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Matemática · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA07 OA 01` | Números | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-01) |
| `MA07 OA 02` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-02) |
| `MA07 OA 03` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-03) |
| `MA07 OA 04` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-04) |
| `MA07 OA 05` | Números | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-05) |
| `MA07 OA 06` | Álgebra y funciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-06) |
| `MA07 OA 07` | Álgebra y funciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-07) |
| `MA07 OA 08` | Álgebra y funciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-08) |
| `MA07 OA 09` | Álgebra y funciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-09) |
| `MA07 OA 10` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-10) |
| `MA07 OA 11` | Geometría | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-11) |
| `MA07 OA 12` | Geometría | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-12) |
| `MA07 OA 13` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-13) |
| `MA07 OA 14` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-14) |
| `MA07 OA 15` | Probabilidad y estadística | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-15) |
| `MA07 OA 16` | Probabilidad y estadística | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-16) |
| `MA07 OA 17` | Probabilidad y estadística | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-17) |
| `MA07 OA 18` | Probabilidad y estadística | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-18) |
| `MA07 OA 19` | Probabilidad y estadística | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/7-basico/ma07-oa-19) |

**Integración transversal documentada:** 19 ítems de habilidades o actitudes se incorporan en 82 experiencias dentro de las 83 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Literatura · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE07 OA 01` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-01) |
| `LE07 OA 02` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-02) |
| `LE07 OA 03` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-03) |
| `LE07 OA 04` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-04) |
| `LE07 OA 05` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-05) |
| `LE07 OA 06` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-06) |
| `LE07 OA 07` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-07) |
| `LE07 OA 08` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-08) |
| `LE07 OA 09` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-09) |
| `LE07 OA 10` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-10) |
| `LE07 OA 11` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-11) |
| `LE07 OA 12` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-12) |
| `LE07 OA 13` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-13) |
| `LE07 OA 14` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-14) |
| `LE07 OA 15` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-15) |
| `LE07 OA 16` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-16) |
| `LE07 OA 17` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-17) |
| `LE07 OA 18` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-18) |
| `LE07 OA 19` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-19) |
| `LE07 OA 20` | Comunicación oral | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-20) |
| `LE07 OA 21` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-21) |
| `LE07 OA 22` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-22) |
| `LE07 OA 23` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-23) |
| `LE07 OA 24` | Investigación | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-24) |
| `LE07 OA 25` | Investigación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/7-basico/le07-oa-25) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 33 experiencias dentro de las 147 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN07 OA 01` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-01) |
| `CN07 OA 02` | Biología | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-02) |
| `CN07 OA 03` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-03) |
| `CN07 OA 04` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-04) |
| `CN07 OA 05` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-05) |
| `CN07 OA 06` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-06) |
| `CN07 OA 07` | Física | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-07) |
| `CN07 OA 08` | Física | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-08) |
| `CN07 OA 09` | Física | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-09) |
| `CN07 OA 10` | Física | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-10) |
| `CN07 OA 11` | Física | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-11) |
| `CN07 OA 12` | Física | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-12) |
| `CN07 OA 13` | Química | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-13) |
| `CN07 OA 14` | Química | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-14) |
| `CN07 OA 15` | Química | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/7-basico/cn07-oa-15) |

**Integración transversal documentada:** 21 ítems de habilidades o actitudes se incorporan en 89 experiencias dentro de las 72 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI07 OA 01` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-01) |
| `HI07 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-02) |
| `HI07 OA 03` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-03) |
| `HI07 OA 04` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-04) |
| `HI07 OA 05` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-05) |
| `HI07 OA 06` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-06) |
| `HI07 OA 07` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-07) |
| `HI07 OA 08` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-08) |
| `HI07 OA 09` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-09) |
| `HI07 OA 10` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-10) |
| `HI07 OA 11` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-11) |
| `HI07 OA 12` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-12) |
| `HI07 OA 13` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-13) |
| `HI07 OA 14` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-14) |
| `HI07 OA 15` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-15) |
| `HI07 OA 16` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-16) |
| `HI07 OA 21` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-21) |
| `HI07 OA 22` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-22) |
| `HI07 OA 23` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-23) |
| `HI07 OA 17` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-17) |
| `HI07 OA 18` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-18) |
| `HI07 OA 19` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-19) |
| `HI07 OA 20` | Formación ciudadana | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/7-basico/hi07-oa-20) |

**Integración transversal documentada:** 20 ítems de habilidades o actitudes se incorporan en 91 experiencias dentro de las 113 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR07 OA 01` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/7-basico/ar07-oa-01) |
| `AR07 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/7-basico/ar07-oa-02) |
| `AR07 OA 03` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/7-basico/ar07-oa-03) |
| `AR07 OA 04` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/7-basico/ar07-oa-04) |
| `AR07 OA 05` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/7-basico/ar07-oa-05) |
| `AR07 OA 06` | Difundir y comunicar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/7-basico/ar07-oa-06) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 33 experiencias dentro de las 29 clases de contenido; no se contabilizan como clases autónomas.

### Música · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU07 OA 01` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-01) |
| `MU07 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-02) |
| `MU07 OA 03` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-03) |
| `MU07 OA 04` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-04) |
| `MU07 OA 05` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-05) |
| `MU07 OA 06` | Reflexionar y relacionar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-06) |
| `MU07 OA 07` | Reflexionar y relacionar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/7-basico/mu07-oa-07) |

**Integración transversal documentada:** 9 ítems de habilidades o actitudes se incorporan en 37 experiencias dentro de las 30 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF07 OA 01` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/7-basico/ef07-oa-01) |
| `EF07 OA 02` | Habilidades motrices | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/7-basico/ef07-oa-02) |
| `EF07 OA 03` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/7-basico/ef07-oa-03) |
| `EF07 OA 04` | Vida activa y saludable | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/7-basico/ef07-oa-04) |
| `EF07 OA 05` | Responsabilidad personal y social en el deporte y la actividad física | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/7-basico/ef07-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 28 experiencias dentro de las 25 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR07 OA 01` | Crecimiento personal | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-01) |
| `OR07 OA 02` | Crecimiento personal | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-02) |
| `OR07 OA 03` | Bienestar y autocuidado | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-03) |
| `OR07 OA 04` | Bienestar y autocuidado | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-04) |
| `OR07 OA 05` | Relaciones interpersonales | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-05) |
| `OR07 OA 06` | Relaciones interpersonales | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-06) |
| `OR07 OA 07` | Pertenencia y participación democrática | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-07) |
| `OR07 OA 08` | Pertenencia y participación democrática | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-08) |
| `OR07 OA 09` | Gestión y proyección del aprendizaje | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-09) |
| `OR07 OA 10` | Gestión y proyección del aprendizaje | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/7-basico/or07-oa-10) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE07 OA 01` | Resolución de problemas tecnológicos | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/7-basico/te07-oa-01) |
| `TE07 OA 02` | Resolución de problemas tecnológicos | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/7-basico/te07-oa-02) |
| `TE07 OA 03` | Resolución de problemas tecnológicos | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/7-basico/te07-oa-03) |
| `TE07 OA 04` | Resolución de problemas tecnológicos | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/7-basico/te07-oa-04) |
| `TE07 OA 05` | Tecnología, ambiente y sociedad | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/7-basico/te07-oa-05) |
| `TE07 OA 06` | Tecnología, ambiente y sociedad | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/7-basico/te07-oa-06) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 16 experiencias dentro de las 26 clases de contenido; no se contabilizan como clases autónomas.

### Inglés · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `IN07 OA 01` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-01) |
| `IN07 OA 02` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-02) |
| `IN07 OA 03` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-03) |
| `IN07 OA 04` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-04) |
| `IN07 OA 05` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-05) |
| `IN07 OA 06` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-06) |
| `IN07 OA 07` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-07) |
| `IN07 OA 08` | Comunicación oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-08) |
| `IN07 OA 09` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-09) |
| `IN07 OA 10` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-10) |
| `IN07 OA 11` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-11) |
| `IN07 OA 12` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-12) |
| `IN07 OA 13` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-13) |
| `IN07 OA 14` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-14) |
| `IN07 OA 15` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-15) |
| `IN07 OA 16` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/7-basico/in07-oa-16) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 21 experiencias dentro de las 80 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN07 OA 01` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-01) |
| `EN07 OA 02` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-02) |
| `EN07 OA 03` | Comprensión auditiva | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-03) |
| `EN07 OA 04` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-04) |
| `EN07 OA 05` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-05) |
| `EN07 OA 06` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-06) |
| `EN07 OA 07` | Comprensión de lectura | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-07) |
| `EN07 OA 08` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-08) |
| `EN07 OA 09` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-09) |
| `EN07 OA 10` | Expresión oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-10) |
| `EN07 OA 11` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-11) |
| `EN07 OA 12` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-12) |
| `EN07 OA 13` | Expresión escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/7-basico/en07-oa-13) |

**Integración transversal documentada:** 21 ítems de habilidades o actitudes se incorporan en 85 experiencias dentro de las 65 clases de contenido; no se contabilizan como clases autónomas.

### Lengua Indígena · 7° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LI07 OF A` | Tradición oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07) |
| `LI07 OF B` | Tradición oral | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07-b) |
| `LI07 OF C` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07-c) |
| `LI07 OF D` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07-d) |
| `LI07 OF E` | Comunicación oral | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07) |
| `LI07 OF F` | Comunicación escrita | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07-f) |
| `LI07 OF G` | Comunicación escrita | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07-g) |
| `LI07 OF H` | Comunicación escrita | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/7-basico/li07-h) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Matemática · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MA08 OA 01` | Números | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-01) |
| `MA08 OA 02` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-02) |
| `MA08 OA 03` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-03) |
| `MA08 OA 04` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-04) |
| `MA08 OA 05` | Números | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-05) |
| `MA08 OA 06` | Álgebra y funciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-06) |
| `MA08 OA 07` | Álgebra y funciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-07) |
| `MA08 OA 08` | Álgebra y funciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-08) |
| `MA08 OA 09` | Álgebra y funciones | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-09) |
| `MA08 OA 10` | Álgebra y funciones | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-10) |
| `MA08 OA 11` | Geometría | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-11) |
| `MA08 OA 12` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-12) |
| `MA08 OA 13` | Geometría | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-13) |
| `MA08 OA 14` | Geometría | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-14) |
| `MA08 OA 15` | Probabilidad y estadística | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-15) |
| `MA08 OA 16` | Probabilidad y estadística | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-16) |
| `MA08 OA 17` | Probabilidad y estadística | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/matematica/8-basico/ma08-oa-17) |

**Integración transversal documentada:** 19 ítems de habilidades o actitudes se incorporan en 82 experiencias dentro de las 77 clases de contenido; no se contabilizan como clases autónomas.

### Lengua y Literatura · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LE08 OA 01` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-01) |
| `LE08 OA 02` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-02) |
| `LE08 OA 03` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-03) |
| `LE08 OA 04` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-04) |
| `LE08 OA 05` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-05) |
| `LE08 OA 06` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-06) |
| `LE08 OA 07` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-07) |
| `LE08 OA 08` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-08) |
| `LE08 OA 09` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-09) |
| `LE08 OA 10` | Lectura - Comprensión | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-10) |
| `LE08 OA 11` | Lectura - Comprensión | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-11) |
| `LE08 OA 12` | Lectura - Comprensión | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-12) |
| `LE08 OA 13` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-13) |
| `LE08 OA 14` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-14) |
| `LE08 OA 15` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-15) |
| `LE08 OA 16` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-16) |
| `LE08 OA 17` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-17) |
| `LE08 OA 18` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-18) |
| `LE08 OA 19` | Escritura - Producción | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-19) |
| `LE08 OA 20` | Escritura - Producción | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-20) |
| `LE08 OA 21` | Comunicación oral | 7 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-21) |
| `LE08 OA 22` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-22) |
| `LE08 OA 23` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-23) |
| `LE08 OA 24` | Comunicación oral | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-24) |
| `LE08 OA 25` | Investigación | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-25) |
| `LE08 OA 26` | Investigación | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-literatura/8-basico/le08-oa-26) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 33 experiencias dentro de las 155 clases de contenido; no se contabilizan como clases autónomas.

### Ciencias Naturales · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `CN08 OA 01` | Biología | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-01) |
| `CN08 OA 02` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-02) |
| `CN08 OA 03` | Biología | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-03) |
| `CN08 OA 04` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-04) |
| `CN08 OA 05` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-05) |
| `CN08 OA 06` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-06) |
| `CN08 OA 07` | Biología | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-07) |
| `CN08 OA 08` | Física | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-08) |
| `CN08 OA 09` | Física | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-09) |
| `CN08 OA 10` | Física | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-10) |
| `CN08 OA 11` | Física | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-11) |
| `CN08 OA 12` | Química | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-12) |
| `CN08 OA 13` | Química | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-13) |
| `CN08 OA 14` | Química | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-14) |
| `CN08 OA 15` | Química | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ciencias-naturales/8-basico/cn08-oa-15) |

**Integración transversal documentada:** 21 ítems de habilidades o actitudes se incorporan en 89 experiencias dentro de las 74 clases de contenido; no se contabilizan como clases autónomas.

### Historia, Geografía y Ciencias Sociales · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `HI08 OA 01` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-01) |
| `HI08 OA 02` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-02) |
| `HI08 OA 03` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-03) |
| `HI08 OA 04` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-04) |
| `HI08 OA 05` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-05) |
| `HI08 OA 06` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-06) |
| `HI08 OA 07` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-07) |
| `HI08 OA 08` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-08) |
| `HI08 OA 09` | Historia | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-09) |
| `HI08 OA 10` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-10) |
| `HI08 OA 11` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-11) |
| `HI08 OA 12` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-12) |
| `HI08 OA 13` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-13) |
| `HI08 OA 14` | Historia | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-14) |
| `HI08 OA 15` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-15) |
| `HI08 OA 16` | Historia | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-16) |
| `HI08 OA 20` | Geografía | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-20) |
| `HI08 OA 21` | Geografía | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-21) |
| `HI08 OA 22` | Geografía | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-22) |
| `HI08 OA 17` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-17) |
| `HI08 OA 18` | Formación ciudadana | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-18) |
| `HI08 OA 19` | Formación ciudadana | 6 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/historia-geografia-ciencias-sociales/8-basico/hi08-oa-19) |

**Integración transversal documentada:** 20 ítems de habilidades o actitudes se incorporan en 91 experiencias dentro de las 117 clases de contenido; no se contabilizan como clases autónomas.

### Artes Visuales · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `AR08 OA 01` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/8-basico/ar08-oa-01) |
| `AR08 OA 02` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/8-basico/ar08-oa-02) |
| `AR08 OA 03` | Expresar y crear visualmente | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/8-basico/ar08-oa-03) |
| `AR08 OA 04` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/8-basico/ar08-oa-04) |
| `AR08 OA 05` | Apreciar y responder frente al arte | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/8-basico/ar08-oa-05) |
| `AR08 OA 06` | Difundir y comunicar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/artes-visuales/8-basico/ar08-oa-06) |

**Integración transversal documentada:** 8 ítems de habilidades o actitudes se incorporan en 33 experiencias dentro de las 29 clases de contenido; no se contabilizan como clases autónomas.

### Música · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `MU08 OA 01` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-01) |
| `MU08 OA 02` | Escuchar y apreciar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-02) |
| `MU08 OA 03` | Interpretar y crear | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-03) |
| `MU08 OA 04` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-04) |
| `MU08 OA 05` | Interpretar y crear | 5 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-05) |
| `MU08 OA 06` | Reflexionar y relacionar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-06) |
| `MU08 OA 07` | Reflexionar y relacionar | 4 | Desarrollado | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/musica/8-basico/mu08-oa-07) |

**Integración transversal documentada:** 9 ítems de habilidades o actitudes se incorporan en 37 experiencias dentro de las 30 clases de contenido; no se contabilizan como clases autónomas.

### Educación Física y Salud · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EF08 OA 01` | Habilidades motrices | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/8-basico/ef08-oa-01) |
| `EF08 OA 02` | Habilidades motrices | 6 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/8-basico/ef08-oa-02) |
| `EF08 OA 03` | Vida activa y saludable | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/8-basico/ef08-oa-03) |
| `EF08 OA 04` | Vida activa y saludable | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/8-basico/ef08-oa-04) |
| `EF08 OA 05` | Responsabilidad personal y social en el deporte y la actividad física | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/educacion-fisica-salud/8-basico/ef08-oa-05) |

**Integración transversal documentada:** 7 ítems de habilidades o actitudes se incorporan en 0 experiencias dentro de las 26 clases de contenido; no se contabilizan como clases autónomas.

### Orientación · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `OR08 OA 01` | Crecimiento personal | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-01) |
| `OR08 OA 02` | Crecimiento personal | 6 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-02) |
| `OR08 OA 03` | Bienestar y autocuidado | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-03) |
| `OR08 OA 04` | Bienestar y autocuidado | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-04) |
| `OR08 OA 05` | Relaciones interpersonales | 6 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-05) |
| `OR08 OA 06` | Relaciones interpersonales | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-06) |
| `OR08 OA 07` | Pertenencia y participación democrática | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-07) |
| `OR08 OA 08` | Pertenencia y participación democrática | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-08) |
| `OR08 OA 09` | Gestión y proyección del aprendizaje | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-09) |
| `OR08 OA 10` | Gestión y proyección del aprendizaje | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/orientacion/8-basico/or08-oa-10) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Tecnología · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `TE08 OA 01` | Resolución de problemas tecnológicos | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/8-basico/te08-oa-01) |
| `TE08 OA 02` | Resolución de problemas tecnológicos | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/8-basico/te08-oa-02) |
| `TE08 OA 03` | Resolución de problemas tecnológicos | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/8-basico/te08-oa-03) |
| `TE08 OA 04` | Resolución de problemas tecnológicos | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/8-basico/te08-oa-04) |
| `TE08 OA 05` | Tecnología, ambiente y sociedad | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/8-basico/te08-oa-05) |
| `TE08 OA 06` | Tecnología, ambiente y sociedad | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/tecnologia/8-basico/te08-oa-06) |

**Integración transversal documentada:** 4 ítems de habilidades o actitudes se incorporan en 0 experiencias dentro de las 26 clases de contenido; no se contabilizan como clases autónomas.

### Inglés · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `IN08 OA 01` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-01) |
| `IN08 OA 02` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-02) |
| `IN08 OA 03` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-03) |
| `IN08 OA 04` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-04) |
| `IN08 OA 05` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-05) |
| `IN08 OA 06` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-06) |
| `IN08 OA 07` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-07) |
| `IN08 OA 08` | Comunicación oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-08) |
| `IN08 OA 09` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-09) |
| `IN08 OA 10` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-10) |
| `IN08 OA 11` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-11) |
| `IN08 OA 12` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-12) |
| `IN08 OA 13` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-13) |
| `IN08 OA 14` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-14) |
| `IN08 OA 15` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-15) |
| `IN08 OA 16` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles/8-basico/in08-oa-16) |

**Integración transversal documentada:** 5 ítems de habilidades o actitudes se incorporan en 0 experiencias dentro de las 80 clases de contenido; no se contabilizan como clases autónomas.

### Inglés (Propuesta) · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `EN08 OA 01` | Comprensión auditiva | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-01) |
| `EN08 OA 02` | Comprensión auditiva | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-02) |
| `EN08 OA 03` | Comprensión auditiva | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-03) |
| `EN08 OA 04` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-04) |
| `EN08 OA 05` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-05) |
| `EN08 OA 06` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-06) |
| `EN08 OA 07` | Comprensión de lectura | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-07) |
| `EN08 OA 08` | Expresión oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-08) |
| `EN08 OA 09` | Expresión oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-09) |
| `EN08 OA 10` | Expresión oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-10) |
| `EN08 OA 11` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-11) |
| `EN08 OA 12` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-12) |
| `EN08 OA 13` | Expresión escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/ingles-propuesta/8-basico/en08-oa-13) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

### Lengua Indígena · 8° básico

| Ítem | Eje | Clases | Estado | Fuente |
|---|---|---:|---|---|
| `LI08 OF A` | Tradición oral | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08) |
| `LI08 OF B` | Tradición oral | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-b) |
| `LI08 OF C` | Comunicación oral | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-c) |
| `LI08 OF D` | Comunicación oral | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-d) |
| `LI08 OF E` | Comunicación oral | 4 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08) |
| `LI08 OF F` | Comunicación escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-f) |
| `LI08 OF G` | Comunicación escrita | 5 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-g) |
| `LI08 OF H` | Comunicación escrita | 6 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-h) |
| `LI08 OF I` | Comunicación escrita | 6 | Pendiente | [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/7o-basico-2o-medio/lengua-indigena/8-basico/li08-i) |

**Integración transversal:** la asignatura no registra OA separados de habilidades o actitudes en el snapshot; las habilidades propias se observan dentro de las clases de contenido.

## Controles profesionales

| Control | Estado | Evidencia exigida |
|---|---|---|
| Disciplinar | pendiente | Nombre o rol, fecha, alcance, hallazgos y cierre documentado |
| Pedagógico | pendiente | Nombre o rol, fecha, alcance, hallazgos y cierre documentado |
| Accesibilidad e inclusión | pendiente | Nombre o rol, fecha, alcance, hallazgos y cierre documentado |
| Cultural y contextual | pendiente | Nombre o rol, fecha, alcance, hallazgos y cierre documentado |
| Documental y fuentes | control interno completo niveles 1 a 7 y seis asignaturas 8 | Las asignaturas de 1° a 7° y Matemática, Lengua y Literatura, Ciencias Naturales, Historia, Artes Visuales y Música de 8° registran ficha oficial por OA, origen explícito de criterios y clases verificadas en catálogo, Markdown y HTML; 5°, 6° y 7° conservan separadas las dos denominaciones oficiales de Inglés presentes en el inventario |
| Derechos y privacidad | interno en curso | validación automática de licencias y prohibición de datos personales |

## Gates del desarrollo interno de 1° a 7° básico

Estos controles están cerrados para el alcance desarrollado. La revisión profesional continúa como un estado posterior e independiente.

- [x] Todos los OA disciplinares tienen secuencias específicas y completas.
- [x] Habilidades y actitudes están mapeadas dentro de las clases y no se contabilizan como clases independientes.
- [x] Cada clase contiene ejemplo disciplinar, práctica, evidencia, criterios, tarea y acciones ante dificultades.
- [x] Markdown y HTML se generan desde la misma fuente y conservan enlaces de su propio formato.
- [x] Generación, validadores, pruebas, compilación y reproducibilidad quedan en verde.
- [x] La revisión profesional solo se declara cuando existe nombre o rol, fecha, alcance y evidencia registrada.

## Regla de comunicación

El avance se informa con OA y clases efectivamente desarrollados. No se usan cantidad de archivos, publicación HTML ni plantillas como sustitutos de contenido terminado. Una asignatura solo aparece como **desarrollo interno completo** cuando todos sus OA disciplinares y sus gates internos están cerrados; solo aparece como **revisada** cuando existe evidencia profesional humana registrada.
