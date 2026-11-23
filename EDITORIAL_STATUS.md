# Estado editorial

Fecha de corte: **2026-10-02**. Los conteos provienen de `curriculum/catalog.json` y se verifican en CI.

| Estado | Clases | Significado |
|---|---:|---|
| Inventariada | 17.420 | OA, nivel, asignatura, eje y fuente oficial identificados |
| Secuenciada | 17.420 | posición, fase y duración propuestas dentro del OA |
| Borrador | 0 | no quedan borradores |
| Desarrollada | 13.264 | contenido disciplinar específico validado contra el contrato estructural |
| Integrada | 4.156 | habilidades o actitudes incorporadas dentro de las clases de contenido |
| Revisada | 0 | control pedagógico, disciplinar, documental y técnico humano |
| Publicada | 17.420 | Markdown y HTML accesibles, enlazados y verificados automáticamente |

“Publicada” describe disponibilidad técnica; no sustituye “desarrollada” ni “revisada”. **Desde 1° básico hasta 4° medio, los doce niveles tienen desarrollo interno completo**. La revisión humana permanece separada y pendiente.

La capa longitudinal de competencias publicada el 2 de octubre enlaza estos OA y clases sin cambiar sus conteos ni estados. Su taxonomía, progresiones, ítems y correspondencias con marcos externos son elaboración del proyecto y permanecen pendientes de revisión experta y pilotaje.

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

## Desarrollo completo de 8° básico

| Asignatura | OA de contenido | Clases desarrolladas | OA transversales | Experiencias integradas | Pendientes en la asignatura |
|---|---:|---:|---:|---:|---:|
| Matemática | 17 | 77 | 19 | 82 | 0 |
| Lengua y Literatura | 26 | 155 | 8 | 33 | 0 |
| Ciencias Naturales | 15 | 74 | 21 | 89 | 0 |
| Historia, Geografía y Ciencias Sociales | 22 | 117 | 20 | 91 | 0 |
| Artes Visuales | 6 | 29 | 8 | 33 | 0 |
| Música | 7 | 30 | 9 | 37 | 0 |
| Educación Física y Salud | 5 | 26 | 7 | 28 | 0 |
| Orientación | 10 | 49 | 0 | 0 | 0 |
| Tecnología | 6 | 26 | 4 | 16 | 0 |
| Inglés | 16 | 80 | 5 | 21 | 0 |
| Inglés (Propuesta) | 13 | 65 | 0 | 0 | 0 |
| Lengua Indígena | 9 | 43 | 0 | 0 | 0 |
| **Total de 8° básico** | **152** | **771** | **101** | **430** | **0** |

Las doce denominaciones mantienen continuidad explícita con 7°, secuencias OA por OA y el contrato de aula completo. El nivel se declara con desarrollo interno completo, pero no revisado: siguen pendientes la revisión profesional y el pilotaje documentado.

## 1° medio completo

| Asignatura | OA de contenido | Clases desarrolladas | OA transversales | Experiencias integradas | Pendientes en la asignatura |
|---|---:|---:|---:|---:|---:|
| Matemática | 15 | 66 | 21 | 89 | 0 |
| Lengua y Literatura | 24 | 143 | 8 | 33 | 0 |
| Ciencias Naturales | 20 | 100 | 21 | 93 | 0 |
| Historia, Geografía y Ciencias Sociales | 25 | 132 | 23 | 103 | 0 |
| Inglés | 16 | 80 | 5 | 21 | 0 |
| Inglés (Propuesta) | 13 | 65 | 0 | 0 | 0 |
| Artes Visuales | 6 | 29 | 8 | 33 | 0 |
| Música | 7 | 32 | 9 | 37 | 0 |
| Educación Física y Salud | 5 | 28 | 7 | 28 | 0 |
| Orientación | 10 | 52 | 0 | 0 | 0 |
| Tecnología | 6 | 26 | 4 | 19 | 0 |
| **Estado del nivel** | **147** | **753** | **106** | **456** | **0** |

Las once denominaciones cuentan con secuencias específicas, integraciones transversales cuando corresponden, [índice del nivel](docs/1-medio/README.md) y guías propias. El nivel no conserva propuestas secuenciadas ni borradores; la revisión humana sigue pendiente.

## 2° medio completo

| Asignatura | OA de contenido | Clases desarrolladas | OA transversales | Experiencias integradas | Pendientes en la asignatura |
|---|---:|---:|---:|---:|---:|
| Matemática | 12 | 55 | 21 | 89 | 0 |
| Lengua y Literatura | 24 | 146 | 8 | 33 | 0 |
| Ciencias Naturales | 18 | 85 | 21 | 93 | 0 |
| Historia, Geografía y Ciencias Sociales | 25 | 142 | 23 | 103 | 0 |
| Inglés | 16 | 81 | 5 | 21 | 0 |
| Inglés (Propuesta) | 13 | 66 | 0 | 0 | 0 |
| Artes Visuales | 6 | 30 | 8 | 33 | 0 |
| Música | 7 | 31 | 9 | 37 | 0 |
| Educación Física y Salud | 5 | 28 | 7 | 28 | 0 |
| Orientación | 10 | 52 | 0 | 0 | 0 |
| Tecnología | 6 | 28 | 4 | 19 | 0 |
| **Estado del nivel** | **142** | **744** | **106** | **456** | **0** |

Las once denominaciones cuentan con secuencias específicas, integraciones transversales cuando corresponden, [índice de 2° medio](docs/2-medio/README.md) y guías propias. El nivel no conserva propuestas secuenciadas ni borradores; la revisión humana sigue pendiente.

## 3° medio · Formación General completo

| Asignatura | OA de contenido | Clases desarrolladas | Pendientes en la asignatura |
|---|---:|---:|---:|
| Matemática 3° medio | 4 | 17 | 0 |
| Lengua y Literatura 3° medio | 9 | 59 | 0 |
| Otras asignaturas y opciones del nivel | 85 | 419 | 0 |
| **Estado del nivel** | **98** | **495** | **0** |

Las dieciocho denominaciones cuentan con [índice de nivel](docs/3-medio/README.md), guías propias, fichas oficiales por OA y criterios pedagógicos internos rotulados. El desarrollo interno está completo y la revisión humana sigue pendiente.

## 4° medio · Formación General completo

| Asignatura | OA de contenido | Clases desarrolladas | Pendientes en la asignatura |
|---|---:|---:|---:|
| Ambiente y sostenibilidad | 3 | 16 | 0 |
| Artes visuales | 7 | 35 | 0 |
| Bienestar y salud | 3 | 17 | 0 |
| Chile y la región latinoamericana | 7 | 36 | 0 |
| Danza | 6 | 28 | 0 |
| Educación ciudadana 4° medio | 8 | 39 | 0 |
| Educación física y salud 1 | 5 | 24 | 0 |
| Educación física y salud 2 | 5 | 25 | 0 |
| Filosofía 4° medio | 5 | 24 | 0 |
| Inglés 4° medio | 4 | 18 | 0 |
| Lengua y Literatura 4° medio | 8 | 53 | 0 |
| Matemática 4° medio | 4 | 17 | 0 |
| Mundo global | 7 | 36 | 0 |
| Música | 7 | 34 | 0 |
| Seguridad, prevención y autocuidado | 3 | 18 | 0 |
| Teatro | 6 | 31 | 0 |
| Tecnología y sociedad | 3 | 15 | 0 |
| **Estado del nivel** | **91** | **466** | **0** |

Las diecisiete denominaciones cuentan con [índice de nivel](docs/4-medio/README.md), guías propias, fichas oficiales por OA y criterios pedagógicos internos rotulados. El desarrollo interno de toda la trayectoria está completo y la revisión humana sigue pendiente.

## 3° y 4° medio · Electivos HC (Formación Diferenciada Humanístico-Científica)

| Área | Electivos | OA | Clases por nivel | Clases en ambos niveles | Pendientes |
|---|---:|---:|---:|---:|---:|
| Matemática | 4 | 20 | 92 | 184 | 0 |
| Lengua y literatura | 3 | 18 | 84 | 168 | 0 |
| Ciencias | 5 | 30 | 143 | 286 | 0 |
| Historia, geografía y ciencias sociales | 3 | 19 | 93 | 186 | 0 |
| Filosofía | 3 | 18 | 82 | 164 | 0 |
| Artes | 6 | 44 | 214 | 428 | 0 |
| Educación física y salud | 3 | 16 | 72 | 144 | 0 |
| **Estado de los electivos** | **27** | **165** | **780** | **1.560** | **0** |

Los 165 OA son los mismos en 3° y 4° medio y cuentan en los dos niveles. Cada electivo tiene su ficha oficial por OA, cuaderno del estudiante y [índice](docs/electivos-hc/README.md). El desarrollo interno está completo y la revisión humana sigue pendiente.

<!-- TP:estado -->
## 3° y 4° medio · Formación técnico-profesional (publicada por lotes de sectores)

| Sector | Especialidad | Riesgo físico | OA | Clases |
|---|---|---|---:|---:|
| Administración | Administración | bajo | 15 | 62 |
| Administración | Contabilidad | bajo | 7 | 58 |
| Agropecuario | Agropecuaria | alto | 26 | 109 |
| Alimentación | Elaboración Industrial de Alimentos | medio | 8 | 68 |
| Alimentación | Gastronomía | medio | 14 | 57 |
| Confección | Vestuario y Confección Textil | medio | 8 | 66 |
| Construcción | Construcción | alto | 27 | 116 |
| Construcción | Instalaciones Sanitarias | alto | 8 | 74 |
| Construcción | Montaje Industrial | alto | 10 | 86 |
| Construcción | Refrigeración y Climatización | alto | 9 | 82 |
| Electricidad | Electricidad | alto | 8 | 70 |
| Electricidad | Electrónica | medio | 7 | 58 |
| Gráfico | Dibujo Técnico | bajo | 9 | 82 |
| Gráfico | Gráfica | bajo | 7 | 60 |
| Hotelería y Turismo | Servicios de Hotelería | bajo | 9 | 82 |
| Hotelería y Turismo | Servicios de Turismo | bajo | 7 | 66 |
| Maderero | Forestal | alto | 10 | 92 |
| Maderero | Muebles y Terminaciones en Madera | alto | 10 | 84 |
| Marítimo | Acuicultura | alto | 8 | 72 |
| Marítimo | Operaciones Portuarias | alto | 7 | 68 |
| Marítimo | Pesquería | alto | 7 | 68 |
| Marítimo | Tripulación de Naves Mercantes y Especiales | alto | 9 | 88 |
| Metalmecánica | Construcciones Metálicas | alto | 9 | 76 |
| Metalmecánica | Mecánica Automotriz | alto | 8 | 70 |
| Metalmecánica | Mecánica de Mantenimiento de Aeronaves | alto | 7 | 64 |
| Metalmecánica | Mecánica Industrial | alto | 23 | 98 |
| Minero | Asistencia en Geología | alto | 8 | 66 |
| Minero | Explotación Minera | alto | 8 | 70 |
| Minero | Metalurgia Extractiva | alto | 8 | 72 |
| Química e Industria | Química Industrial | alto | 13 | 61 |
| Salud y Educación | Atención de Enfermería | alto | 15 | 68 |
| Salud y Educación | Atención de Párvulos | medio | 10 | 86 |
| Tecnología y Comunicaciones | Conectividad y Redes | bajo | 11 | 88 |
| Tecnología y Comunicaciones | Programación | bajo | 10 | 80 |
| Tecnología y Comunicaciones | Telecomunicaciones | bajo | 10 | 82 |
| Transversal | Objetivos genéricos A-L | bajo | 12 | 96 |
| **Total** | **35 especialidades** | | **382** | **2745** |

Los objetivos son los perfiles de egreso de las Bases Curriculares de Formación Diferenciada Técnico-Profesional (Decreto Supremo de Educación N.º 452/2013 según el propio documento, edición 2016; las bases no traen módulos). Las especialidades sin mención comparten cuaderno entre 3° y 4° medio; en las con menciones, el tronco va en 3° y las menciones en 4°. Cada especialidad tiene [guía propia](docs/formacion-tp/README.md). Solo conceptos y casos en papel: nada de taller, laboratorio ni práctica; en las especialidades de riesgo medio o alto no hay procedimientos operativos y el cuaderno no habilita para trabajar. Revisión humana pendiente. Avance completo de la fase en [AVANCE_ASIGNATURAS_NUEVAS.md](docs/AVANCE_ASIGNATURAS_NUEVAS.md).

<!-- /TP:estado -->
<!-- EPJA:estado -->
## Educación de Personas Jóvenes y Adultas (EPJA, publicada por asignaturas)

| Nivel | Asignatura | Objetivos | Clases | Cuaderno escrito |
|---|---|---:|---:|---:|
| EPJA | Lenguaje y Comunicación · EPJA Básica N1 | 16 | 118 | 0 |
| **Total** | **1 asignatura** | **16** | **118** | **0** |

Los objetivos son las actividades de desempeño de los programas de estudio EPJA oficiales (4 módulos obligatorios con 4 actividades cada uno); las clases de cada objetivo son las horas pedagógicas que el programa le asigna. Las clases con cuaderno del estudiante son 0 de 118; el resto figura como pendiente en [docs/COBERTURA_ESTUDIANTE.md](docs/COBERTURA_ESTUDIANTE.md). Los módulos electivos de proyecto o de problemas reutilizan los mismos conocimientos y no suman clases. Tono de persona adulta o joven, sin infantilizar. Escrito por IA, revisión humana pendiente. Índice en [docs/formacion-epja/README.md](docs/formacion-epja/README.md) e [inventario](docs/EPJA_INVENTARIO.md).

<!-- /EPJA:estado -->
## Cobertura publicada

- 12 niveles, desde 1° básico hasta 4° medio, más 27 electivos HC, especialidades técnico-profesionales de 3° y 4° medio y asignaturas de EPJA.
- 116 asignaturas o denominaciones curriculares (35 de formación general, 27 electivos HC, 53 de formación técnico-profesional contando las menciones como denominaciones propias, y 1 de EPJA).
- 3.800 Objetivos de Aprendizaje.
- 595 vínculos de lectura asociados por MINEDUC.
- 3.800 páginas HTML de OA con anclas estables para 17.420 registros pedagógicos: 13.264 clases y 4.156 experiencias integradas.

## Próximo gate editorial

Un lote solo pasa a “desarrollado” cuando cada clase incluye contenido disciplinar específico, ejemplo o demostración, práctica y evaluación propias del OA. El validador rechaza campos ausentes, criterios insuficientes, conteos divergentes y páginas que no materialicen el contrato. Solo pasa a “revisado” con evidencia humana registrada. La automatización no certifica por sí sola calidad pedagógica.

## Material para el estudiante (estado separado)

“Desarrollada” describe la **planificación docente** de una clase: propósito, secuencia, evidencia y criterios. No significa que el estudiante disponga de explicación, ejercicios y respuestas para aprender por sí mismo. Ese material se publica como **cuaderno del estudiante** y se cuenta aparte en [Cobertura real del material del estudiante](docs/COBERTURA_ESTUDIANTE.md). Los contenidos que requieren revisión especializada se listan en [Revisión profesional pendiente](docs/REVISION_PENDIENTE_CUADERNOS.md). La [auditoría de contenido](docs/AUDITORIA_CONTENIDO.md) documenta la línea base reproducible y los defectos comprobados.

| Estado | Clases | Evidencia |
|---|---:|---|
| Con cuaderno del estudiante | 8.605 | 1° básico (691 clases), 2° básico (721), 3° básico (757), 4° básico (811), 5° básico (844), 6° básico (876), 7° básico (719), 8° básico (728), 1° medio (753), 2° medio (744), 3° medio Formación General (495) y 4° medio Formación General (466; 339 de las clases de ambos niveles comparten cuaderno) completos en sus 11 asignaturas, con segunda lectura crítica asistida por IA; validación automática aprobada; sin revisión profesional humana |
| Con revisión profesional del cuaderno | 0 | pendiente: ningún cuaderno tiene revisión disciplinar humana documentada |

