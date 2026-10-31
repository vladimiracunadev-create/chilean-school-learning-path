# Análisis de alineación con el OA oficial

Este análisis contrasta cada cuaderno con el **texto oficial del OA** y con el **título de la clase planificada**: mide qué parte de sus términos de contenido aparece realmente en el cuaderno, la longitud media de las oraciones de la explicación y algunas señales pedagógicas débiles. **No** juzga exactitud disciplinar: ordena las clases para que una persona lea primero las más débiles. Se regenera con `python scripts/audit_alignment.py --write`.

**Límite de la medida.** Es una heurística de triage por coincidencia de términos: sobre-marca, sobre todo en Inglés, donde el título planificado es metalenguaje docente («Connect prior knowledge») que no aparece en un cuaderno para estudiantes, y en las clases de Lengua y Cultura, cuyo título lleva rótulos de método. Una marca no prueba un defecto; una ausencia de marca no prueba exactitud.

## 1.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 16 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 24 | 39 % | 6 |
| ciencias-naturales | 49 | 46 % | 3 |
| educacion-fisica-salud | 48 | 37 % | 14 |
| historia-geografia-ciencias-sociales | 68 | 46 % | 11 |
| ingles-propuesta | 69 | 28 % | 28 |
| lengua-cultura-pueblos-originarios-ancestrales | 129 | 44 % | 13 |
| lenguaje-comunicacion | 131 | 41 % | 6 |
| matematica | 83 | 51 % | 7 |
| musica | 29 | 51 % | 1 |
| orientacion | 35 | 41 % | 0 |
| tecnologia | 26 | 41 % | 0 |

**Clases marcadas para lectura prioritaria (1.º básico):** 89 de 691.

### Segunda lectura crítica de las 691 clases

Después de la validación automática, cada una de las 691 clases de 1.º básico fue releída de principio a fin por un segundo lector (asistido por IA, independiente de quien la escribió), que la contrastó con el texto del OA y el título de la clase en el currículo del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional: se usó el texto oficial reproducido en cada ficha.

| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 83 | Dato falso sobre la derecha y la izquierda; centímetros y operaciones de 2.º básico en OA 18 y otros; contradicciones internas entre explicación y ejemplos; respuestas falsas en patrones y familias de operaciones. |
| Lenguaje y Comunicación | 131 | Conteos de palabras erróneos; datos falsos en textos (gatos que no nadan, osos pescando en invierno); definiciones y terminología silábica; léxico difícil sin definir; ejercicios de oralidad ambiguos. |
| Ciencias Naturales | 49 | Conclusiones no justificadas por los datos; cifras de seres vivos eliminadas o hechas cualitativas; datos de ejemplo rotulados; operaciones de otro nivel; avisos de seguridad. |
| Historia, Geografía y Ciencias Sociales | 68 | Edades calculadas sin considerar el mes; voto femenino (1934 y 1949 son leyes, no el día en que votaron); restas de años fuera de nivel; fechas de casos inventados; ambigüedades de mapas. |
| Inglés | 69 | Inglés incorrecto o antinatural; estructuras de otro nivel; vocabulario usado sin enseñarse; explicaciones en español falsas; expresiones del OA agregadas (/s/-/z/, I want, Here). |
| Lengua y Cultura de los Pueblos Originarios | 129 | Conteos de sílabas y palabras; afirmaciones culturales no seguras eliminadas o generalizadas; frase inventada retirada; preguntas que jerarquizaban identidad; aritmética de otro nivel. |
| Educación Física y Salud | 48 | Riesgos motores (retroceder de espaldas); equivalencias falsas («dos brazos» = 2 m); cifras de salud generalizadas; ejercicios imposibles de practicar. |
| Orientación | 35 | Lenguaje de las clases de cuerpo y protección ajustado («no es tu culpa», nada es un secreto); ambigüedades; operaciones de otro nivel; seguridad con tijeras. |
| Música | 29 | Conteos de pulsos y sílabas erróneos; contradicciones entre consigna y ejemplo; objetos de vidrio y martillo reemplazados por opciones seguras. |
| Artes Visuales | 24 | Multiplicaciones y restas de años de otro nivel; datos de obras dudosos; ambigüedades. |
| Tecnología | 26 | Instrucciones de seguridad incorrectas; respuesta contraria a lo enseñado; multiplicaciones; software ficticio rotulado. |

#### Vacíos de cobertura frente al OA

- **Cerrados en una pasada posterior:** Inglés OA 03 (contraste /w/-/th/) y OA 07 (ocupaciones y comida); Tecnología OA 03 (fibras y plásticos) y OA 06 (tipos de software); Historia (restas de años de cuatro cifras reemplazadas por comparación, orden y saltos cortos).
- **Lenguaje:** OA 17 y OA 09 piden obras completas y poemas de autor; el cuaderno usa textos originales breves por derechos de autor. Queda abierto.
- **Lengua y Cultura de los Pueblos Originarios:** las clases de lengua se practican sólo con castellano y el saludo «mari mari»; el aprendizaje de la lengua real queda en manos del educador o educadora tradicional.

Todos los contenidos que requieren especialista, incluida la verificación contra el Programa de Estudio oficial, siguen listados en [Revisión profesional pendiente](REVISION_PENDIENTE_CUADERNOS.md).

### Clases marcadas de 1.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| EN01 OA 07 | 5 | Read actions happening now | 7 % | 0 % | 14.9 | — |
| EN01 OA 02 | 3 | Objects, possession and quantity | 8 % | 0 % | 12.8 | — |
| EN01 OA 02 | 2 | People and abilities | 8 % | 0 % | 12.6 | — |
| EN01 OA 02 | 1 | School instructions | 11 % | 50 % | 16.1 | — |
| LE01 OA 23 | 3 | Describir para hacer visible | 12 % | 33 % | 14.1 | — |
| EN01 OA 03 | 3 | Notice frequent expressions | 12 % | 33 % | 10.5 | — |
| EN01 OA 02 | 4 | Places and location | 13 % | 0 % | 10.4 | — |
| EN01 OA 02 | 5 | Actions happening now | 13 % | 0 % | 9.7 | — |
| EN01 OA 07 | 2 | Ability, feeling and possession | 14 % | 0 % | 8.5 | — |
| EN01 OA 04 | 4 | Focus on key words | 14 % | 0 % | 10.0 | — |
| EN01 OA 07 | 4 | Location and information questions | 14 % | 33 % | 7.8 | — |
| EF01 OA 07 | 2 | Juego tradicional contextualizado | 15 % | 67 % | 19.6 | — |
| EN01 OA 10 | 2 | Explore /th/ safely | 15 % | 0 % | 10.9 | — |
| EN01 OA 11 | 3 | Use objects and gestures | 17 % | 0 % | 9.8 | — |
| EN01 OA 11 | 5 | Interact after presenting | 17 % | 33 % | 7.3 | — |
| EN01 OA 12 | 5 | Location and current action | 18 % | 0 % | 19.9 | — |
| EN01 OA 12 | 2 | Ability and quantity | 19 % | 0 % | 19.3 | — |
| EN01 OA 03 | 4 | Distinguish key English sounds | 21 % | 33 % | 13.2 | — |
| EN01 OA 11 | 1 | Enter classroom interaction | 21 % | 0 % | 11.7 | — |
| EF01 OA 04 | 2 | Adaptar locomoción | 21 % | 0 % | 12.2 | — |
| EN01 OA 05 | 2 | Show meaning through drawing | 22 % | 0 % | 12.2 | — |
| LC01 OA LF02 | 4 | Lengua en uso · Contrastar con cuidado | 23 % | 33 % | 14.0 | — |
| EF01 OA 01 | 3 | Lanzar y recibir | 23 % | 100 % | 16.2 | — |
| EN01 OA 05 | 5 | Express a preference or feeling | 24 % | 33 % | 11.8 | — |
| EF01 OA 04 | 1 | Leer el entorno | 25 % | 0 % | 14.8 | — |
| EN01 OA 03 | 2 | Follow simple instructions | 25 % | 33 % | 12.1 | — |
| AR01 OA 01 | 5 | Ampliar la mirada latinoamericana y universal | 27 % | 25 % | 15.2 | — |
| EN01 OA 03 | 1 | Identify characters and objects | 27 % | 33 % | 16.0 | — |
| HI01 OA 04 | 3 | Una fuente oral | 27 % | 100 % | 16.3 | — |
| LC01 OA LS06 | 2 | Primer acercamiento · Escucha focalizada | 27 % | 25 % | 9.7 | — |
| LC01 OA LS06 | 3 | Primer acercamiento · Símbolo y soporte digital | 27 % | 40 % | 13.2 | — |
| EF01 OA 01 | 1 | Locomoción con control | 28 % | 100 % | 17.0 | — |
| EF01 OA 09 | 3 | Agua y colación | 28 % | 100 % | 17.7 | — |
| LE01 OA 05 | 2 | Releer para ganar continuidad | 28 % | 33 % | 9.9 | — |
| LE01 OA 07 | 1 | Explorar un repertorio | 28 % | 0 % | 8.1 | — |
| LE01 OA 10 | 1 | Carta y nota: quién comunica | 28 % | 100 % | 17.1 | — |
| EN01 OA 04 | 3 | Use images without guessing only | 29 % | 33 % | 12.0 | — |
| EN01 OA 09 | 4 | Write a supported reaction | 29 % | 33 % | 10.4 | — |
| LC01 OA LS04 | 3 | Primer acercamiento · Conectar con cuidado | 29 % | 25 % | 10.0 | — |
| EF01 OA 08 | 4 | Señales para regular o detener | 30 % | 33 % | 11.5 | — |
| LC01 OA LS04 | 2 | Primer acercamiento · Recuperar información cultural | 30 % | 40 % | 11.2 | — |
| EN01 OA 06 | 5 | Demonstrate understanding | 30 % | 0 % | 11.5 | — |
| MA01 OA 07 | 4 | Dobles y elección de estrategia | 31 % | 67 % | 18.0 | — |
| EN01 OA 05 | 1 | Connect safely to experience | 32 % | 33 % | 15.9 | — |
| EN01 OA 06 | 3 | Track characters and actions | 33 % | 33 % | 11.4 | — |
| EN01 OA 10 | 3 | Contrast /s/ and /z/ | 33 % | 0 % | 13.8 | — |
| LC01 OA LF06 | 5 | Lengua en uso · Guardar la procedencia | 33 % | 100 % | 18.7 | — |
| LC01 OA LR04 | 3 | Recuperar la lengua · Conectar con cuidado | 33 % | 25 % | 13.1 | — |
| LE01 OA 24 | 1 | Escuchar una palabra nueva | 33 % | 100 % | 16.2 | — |
| LE01 OA 11 | 1 | Un libro ofrece pistas | 38 % | 67 % | 16.4 | — |
| EF01 OA 04 | 4 | Ruta segura | 38 % | 100 % | 16.6 | — |
| EF01 OA 05 | 3 | Una idea en movimiento | 38 % | 100 % | 16.6 | — |
| EF01 OA 01 | 5 | Circuito combinado | 39 % | 50 % | 17.5 | — |
| HI01 OA 14 | 2 | Buena convivencia | 40 % | 100 % | 18.1 | — |
| MA01 OA 13 | 1 | Derecha e izquierda en mi cuerpo | 40 % | 100 % | 13.9 | respuesta «depende» en ejercicio cerrado |
| AR01 OA 01 | 6 | Obra con punto de vista propio | 41 % | 100 % | 20.0 | — |
| AR01 OA 04 | 1 | Detenerse a observar | 41 % | 50 % | 17.0 | — |
| EF01 OA 09 | 1 | Higiene después de moverse | 42 % | 67 % | 16.7 | — |
| LC01 OA LS01 | 1 | Primer acercamiento · Entrar por la escucha completa | 43 % | 60 % | 16.7 | — |
| MA01 OA 17 | 4 | Leer fechas significativas | 44 % | 100 % | 17.6 | — |
| HI01 OA 13 | 4 | Igualdad y no discriminación | 45 % | 100 % | 17.3 | — |
| EN01 OA 01 | 1 | Listen for the text type | 46 % | 100 % | 17.0 | — |
| HI01 OA 11 | 3 | Interdependencia local | 46 % | 100 % | 11.6 | respuesta «depende» en ejercicio cerrado |
| CN01 OA 07 | 1 | Rutinas que cuidan | 47 % | 100 % | 17.0 | — |
| MU01 OA 05 | 2 | Pregunta y respuesta | 47 % | 100 % | 11.6 | respuesta «depende» en ejercicio cerrado |
| HI01 OA 06 | 5 | Muestra cultural respetuosa | 48 % | 100 % | 19.1 | — |
| AR01 OA 03 | 1 | Laboratorio de materiales | 50 % | 100 % | 20.0 | — |
| AR01 OA 04 | 4 | Galería comparada | 50 % | 100 % | 19.1 | — |
| CN01 OA 11 | 1 | Observar el cielo diario | 50 % | 67 % | 20.4 | — |
| EF01 OA 06 | 2 | Circuito continuo | 50 % | 100 % | 16.1 | — |
| EF01 OA 07 | 1 | Moverse en la rutina | 50 % | 100 % | 17.4 | — |
| HI01 OA 05 | 3 | Conmemoraciones y memoria | 50 % | 50 % | 19.3 | — |
| HI01 OA 14 | 4 | Vía pública y autocuidado | 50 % | 100 % | 19.0 | — |
| MA01 OA 19 | 4 | Responder con evidencia | 50 % | 100 % | 17.0 | — |
| HI01 OA 06 | 2 | Fiestas y tradiciones | 52 % | 100 % | 24.5 | — |
| AR01 OA 03 | 2 | Herramientas y seguridad | 53 % | 100 % | 26.6 | — |
| MA01 OA 02 | 2 | Del sexto al décimo | 56 % | 100 % | 16.6 | — |
| LC01 OA 10 | 1 | Observar relaciones | 60 % | 100 % | 18.1 | — |
| LC01 OA 12 | 4 | Aprendizaje sin escenificación | 60 % | 100 % | 16.3 | — |
| CN01 OA 12 | 4 | Informe estacional local | 64 % | 67 % | 16.7 | — |
| MA01 OA 13 | 4 | Posiciones en un plano simple | 64 % | 100 % | 17.0 | — |
| LC01 OA LF03 | 2 | Lengua en uso · Toponimia con territorio | 64 % | 100 % | 16.9 | — |
| HI01 OA 11 | 1 | Trabajo visible e invisible | 71 % | 100 % | 16.8 | — |
| HI01 OA 09 | 4 | Ruta de localización | 73 % | 100 % | 20.0 | — |
| HI01 OA 15 | 2 | Personas que la hacen funcionar | 76 % | 100 % | 21.6 | — |
| LC01 OA 11 | 2 | Fuente cultural | 78 % | 100 % | 17.9 | — |
| EF01 OA 08 | 2 | Cambios durante el esfuerzo | 79 % | 100 % | 16.3 | — |
| LC01 OA LF05 | 1 | Lengua en uso · Mirar con procedencia | 80 % | 100 % | 17.9 | — |
| MA01 OA 18 | 1 | Largo y corto en un objeto | 86 % | 100 % | 13.8 | respuesta «depende» en ejercicio cerrado |

## 2.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 18 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 24 | 39 % | 0 |
| ciencias-naturales | 57 | 50 % | 0 |
| educacion-fisica-salud | 47 | 40 % | 3 |
| historia-geografia-ciencias-sociales | 72 | 44 % | 1 |
| ingles-propuesta | 68 | 31 % | 40 |
| lengua-cultura-pueblos-originarios-ancestrales | 116 | 46 % | 13 |
| lenguaje-comunicacion | 149 | 42 % | 5 |
| matematica | 93 | 45 % | 3 |
| musica | 29 | 47 % | 1 |
| orientacion | 35 | 40 % | 4 |
| tecnologia | 31 | 42 % | 5 |

**Clases marcadas para lectura prioritaria (2.º básico):** 75 de 721.

### Segunda lectura crítica de las 721 clases

Cada una de las 721 clases de 2.º básico (las 20 de Matemática OA 01 a 05 escritas antes y las 701 restantes) fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y con el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional.

| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 93 | Materiales que no existían en el cuaderno (tablas y tarjetas «de este cuaderno»); billetes de $10 y $100 inexistentes; multiplicaciones, divisiones y años de cuatro cifras fuera de nivel; error ilustrado sin sentido; saltos que cruzaban la decena que la clase prohibía; restas de reloj de 24 horas sin enseñar la regla. |
| Lenguaje y Comunicación | 149 | Regla de diptongo falsa («ciudad»); «g fuerte» contraria a la enseñanza tradicional; palabras y conteos erróneos; dato falso sobre aves en Chile; estructuras no enseñadas; enunciados que daban la respuesta; textos que podían herir (tartamudez, edad, familia). |
| Ciencias Naturales | 57 | Datos biológicos falsos (piel de anfibios, escorpión diurno, «las branquias sacan el aire»); caracol sin concha; estaciones con fechas aproximadas; hielo en vaso de vidrio; veleta con alfiler. |
| Historia, Geografía y Ciencias Sociales | 72 | Respuestas con más de una válida (países de referencia); anacronismo de los videos; piñones atribuidos a todos los mapuche; seguridad ante temblor y tsunami; términos usados sin definir. |
| Inglés | 68 | Inglés incorrecto («has a bread»); conteos de palabras falsos; estructuras no enseñadas (do you like, here you are); prueba de «vibra la garganta» engañosa; regla a/an con excepciones. |
| Lengua y Cultura de los Pueblos Originarios | 116 | Eliminadas o generalizadas fechas y ceremonias (We Tripantu, Tapati, Año Nuevo, Pachamama, machi, yatiri); asociaciones de arte con pueblos; variante «cuyén» de ortografía no segura; afirmación histórica generalizada; aritmética de otro nivel. |
| Educación Física y Salud | 47 | Volteo sin supervisión; alfombra y libro como superficies resbalosas; pulso y respiración poco realistas; riesgo de caminar hacia atrás; protocolo inconsistente ante un compañero herido; contradicciones de datos en las metas. |
| Orientación | 35 | Divisiones y multiplicaciones fuera de nivel; ejercicio alarmante sobre secretos reemplazado; doble negativo; supuestos sobre la composición de la familia; datos de higiene y sueño como recomendaciones generales. |
| Música | 29 | Respuesta de ejemplo que no cambiaba el pulso; confusión entre vocal y altura del sonido; pieza que no calzaba con la respuesta; enunciado subjetivo de más suave a más fuerte. |
| Artes Visuales | 24 | Actividad que contradecía sus criterios; ejercicios sobre lo no enseñado (óvalos); ambigüedades de enunciado; obras reales sustituidas por tipos de obra seguros. |
| Tecnología | 31 | Falso «las imágenes propias no tienen derechos de autor»; relleno que no tapa un dibujo; instrucciones de seguridad; software ficticio rotulado. |

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Lenguaje (grupo «dr», anécdota, experiencia personal y relato de hechos, carta, cuento folclórico frente a cuento de autor, lectura independiente); Historia (chango, rapa nui y huilliche, inmigración oriental, patrimonio de más regiones, río, océano, isla y ciudad); Artes (textiles, herramientas digitales, tipos de obra local, latinoamericana y universal); Ciencias (hábitat del mamífero); Matemática (preguntas estadísticas, números cercanos a 1.000); Educación Física (niveles, juegos individuales y colectivos).
- **Abiertos:** Artes OA 04 pide observar al año 10 obras locales o chilenas, 10 latinoamericanas y 10 universales, y el cuaderno solo puede describirlas (imágenes reales y derechos los aporta el docente); Música OA 03 nombra obras con derechos que no se reproducen; Lenguaje OA 06 y 22 piden poemas y cuentos reales de autor o tradicionales; Lengua y Cultura de los Pueblos Originarios: relatos, textos y oraciones reales en lengua indígena y eventos o técnicas propias de cada pueblo los aporta el educador o educadora tradicional; software educativo (Matemática OA 03, 09 y 12) es opcional en el OA y no se puede entregar en el cuaderno; Ciencias OA 02 (moluscos y miriápodos) y vocabulario «endémico» de OA 05 requerirían clases nuevas.
- **Decisiones que dependen del programa oficial:** reloj de 24 horas o a. m./p. m. (Matemática OA 18), equivalencia 1 m = 100 cm (OA 19) y aristas y vértices del cubo (OA 16); no se pudo contrastar con el texto vigente.
- **Criterio distinto entre asignaturas, a revisar por especialista:** Historia mantiene las celebraciones y ceremonias de los pueblos (ngillatun, We Tripantu, Año Nuevo Andino, Tapati, Hain, Pachamama) como fichas generales, porque el OA 01 pide creencias y fiestas; Lengua y Cultura las eliminó por no poder afirmarlas con seguridad.

### Clases marcadas de 2.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| LC02 OA 16 | 3 | Continuidad y presente · Relación entre ser humano, naturale | 8 % | 17 % | 14.3 | — |
| EN02 OA 10 | 2 | Shape and airflow · English sounds through chants, rhymes an | 11 % | 0 % | 9.6 | — |
| EN02 OA 02 | 5 | Actions now · Listening for familiar topics and communicativ | 13 % | 0 % | 9.6 | — |
| EN02 OA 12 | 4 | Ask and locate · Supported oral expression for familiar func | 14 % | 0 % | 16.1 | — |
| EN02 OA 03 | 5 | Sounds /w/ and /th/ · Evidence of oral comprehension and Eng | 14 % | 20 % | 15.0 | — |
| EN02 OA 07 | 5 | Actions happening now · Reading familiar topics and function | 15 % | 14 % | 13.8 | — |
| EN02 OA 12 | 2 | Abilities and quantities · Supported oral expression for fam | 17 % | 0 % | 13.2 | — |
| EN02 OA 07 | 4 | Food, jobs and city places · Reading familiar topics and fun | 17 % | 0 % | 9.0 | — |
| EN02 OA 01 | 4 | Mini-dialogues · Listening to short rhymes, songs, stories a | 18 % | 17 % | 14.6 | — |
| EN02 OA 10 | 3 | Voice for /s/ and /z/ · English sounds through chants, rhyme | 18 % | 14 % | 10.8 | — |
| EN02 OA 12 | 1 | Safe personal information · Supported oral expression for fa | 18 % | 33 % | 15.9 | — |
| LC02 OA LS02 | 2 | Reconocer contexto y fuente · Descripción respetuosa del med | 19 % | 38 % | 9.9 | — |
| OR02 OA 04 | 2 | Alimentación sin culpa · Autocuidado, intimidad e informació | 19 % | 33 % | 10.7 | — |
| EN02 OA 07 | 1 | Instructions and introductions · Reading familiar topics and | 20 % | 29 % | 8.7 | — |
| EN02 OA 03 | 4 | Sounds /s/ and /z/ · Evidence of oral comprehension and Engl | 20 % | 20 % | 12.8 | — |
| LE02 OA 24 | 4 | Explorar expresivamente | 20 % | 100 % | 10.4 | respuesta «depende» en ejercicio cerrado |
| OR02 OA 04 | 5 | Plan de protección · Autocuidado, intimidad e información pe | 20 % | 40 % | 10.3 | — |
| TE02 OA 01 | 3 | Comunicar con un boceto · Diseño de objetos tecnológicos par | 20 % | 43 % | 9.7 | — |
| EN02 OA 12 | 5 | Actions now · Supported oral expression for familiar functio | 21 % | 0 % | 10.1 | — |
| EN02 OA 02 | 2 | Abilities and feelings · Listening for familiar topics and c | 21 % | 29 % | 14.2 | — |
| EN02 OA 02 | 4 | Places and locations · Listening for familiar topics and com | 21 % | 0 % | 13.5 | — |
| LE02 OA 21 | 1 | Familias ce-ci y que-qui | 21 % | 0 % | 13.2 | — |
| EN02 OA 07 | 3 | Animals and objects in place · Reading familiar topics and f | 21 % | 12 % | 13.9 | — |
| LC02 OA 11 | 2 | Relaciones y significados · Naturaleza y actividades product | 21 % | 43 % | 11.8 | — |
| EF02 OA 03 | 2 | Cooperar por una meta | 22 % | 0 % | 12.3 | — |
| LC02 OA 10 | 3 | Continuidad y presente · Elementos espirituales, naturales y | 22 % | 12 % | 12.3 | — |
| EN02 OA 07 | 2 | Ability, feeling and possession · Reading familiar topics an | 23 % | 0 % | 13.5 | — |
| LC02 OA LS05 | 2 | Reconocer contexto y fuente · Recursos tecnológicos para con | 23 % | 25 % | 13.8 | — |
| LE02 OA 21 | 3 | R fuerte en distintas posiciones | 24 % | 33 % | 10.0 | — |
| EN02 OA 06 | 2 | General idea · Reading short English text types | 24 % | 20 % | 8.8 | — |
| EN02 OA 14 | 3 | Locations · Image-supported English writing for familiar mea | 24 % | 14 % | 13.8 | — |
| EN02 OA 02 | 3 | Possession and quantities · Listening for familiar topics an | 25 % | 14 % | 10.5 | — |
| EN02 OA 08 | 2 | Connect known words · Reading strategies with prediction, im | 25 % | 12 % | 14.9 | — |
| EN02 OA 11 | 3 | Ask for a word · Participation in brief English interactions | 25 % | 25 % | 10.3 | — |
| LC02 OA LS05 | 4 | Responder sin apropiarse · Recursos tecnológicos para conoce | 25 % | 43 % | 13.6 | — |
| OR02 OA 01 | 2 | Habilidades que se desarrollan · Características, habilidade | 25 % | 40 % | 10.0 | — |
| TE02 OA 01 | 5 | Elegir con criterios · Diseño de objetos tecnológicos para n | 25 % | 43 % | 10.4 | — |
| EN02 OA 04 | 3 | Images plus words · Listening strategies for meaning | 26 % | 20 % | 11.4 | — |
| EN02 OA 01 | 3 | Story characters · Listening to short rhymes, songs, stories | 26 % | 25 % | 16.1 | — |
| OR02 OA 03 | 4 | Una red de cuidado · Expresiones de afecto y cuidado con con | 26 % | 25 % | 14.6 | — |
| LC02 OA 11 | 4 | Cuidado y reciprocidad · Naturaleza y actividades productiva | 27 % | 43 % | 13.1 | — |
| LC02 OA LR04 | 1 | Activar memoria lingüística · Escritura de palabras y frases | 27 % | 29 % | 11.7 | — |
| MU02 OA 02 | 3 | Imagen nacida del sonido | 27 % | 33 % | 13.4 | — |
| EN02 OA 03 | 2 | Follow the sequence · Evidence of oral comprehension and Eng | 27 % | 0 % | 16.9 | — |
| EN02 OA 01 | 2 | Song actions · Listening to short rhymes, songs, stories and | 28 % | 14 % | 14.7 | — |
| LC02 OA LR05 | 3 | Relacionar lengua y experiencia · TIC y transcripción en con | 28 % | 33 % | 11.1 | — |
| EN02 OA 14 | 4 | Actions now · Image-supported English writing for familiar m | 28 % | 43 % | 9.6 | — |
| EN02 OA 09 | 2 | Drama from text · Responding to English reading | 29 % | 25 % | 14.7 | — |
| EN02 OA 12 | 3 | Describe and prohibit · Supported oral expression for famili | 29 % | 33 % | 11.8 | — |
| EN02 OA 10 | 4 | Chant with rhythm · English sounds through chants, rhymes an | 29 % | 29 % | 10.7 | — |
| LC02 OA 14 | 4 | Cuidado y reciprocidad · Técnicas y producción vinculadas a  | 29 % | 29 % | 13.0 | — |
| EN02 OA 06 | 4 | Known chunks · Reading short English text types | 30 % | 17 % | 8.4 | — |
| EN02 OA 08 | 3 | Picture and text together · Reading strategies with predicti | 30 % | 29 % | 10.2 | — |
| EN02 OA 08 | 5 | Retell with support · Reading strategies with prediction, im | 30 % | 14 % | 11.0 | — |
| EN02 OA 11 | 1 | Classroom exchanges · Participation in brief English interac | 31 % | 33 % | 9.7 | — |
| HI02 OA 16 | 2 | Usos diversos | 31 % | 0 % | 11.0 | — |
| LE02 OA 07 | 2 | Datos que están y datos que infiero | 31 % | 33 % | 9.0 | — |
| EN02 OA 13 | 2 | Complete from a word bank · Model-supported English writing | 31 % | 20 % | 11.7 | — |
| LC02 OA 07 | 2 | Relaciones y significados · Historia local: pasado y present | 31 % | 43 % | 11.4 | — |
| LC02 OA 17 | 3 | Continuidad y presente · Expresiones de arte indígena con pe | 31 % | 33 % | 12.6 | — |
| LC02 OA 17 | 4 | Cuidado y reciprocidad · Expresiones de arte indígena con pe | 31 % | 33 % | 11.1 | — |
| EN02 OA 08 | 4 | Reread with a question · Reading strategies with prediction, | 32 % | 17 % | 9.1 | — |
| EN02 OA 05 | 3 | Connect safely · Responding personally and creatively to lis | 32 % | 33 % | 17.5 | — |
| EN02 OA 14 | 1 | Identify and label · Image-supported English writing for fam | 32 % | 25 % | 11.9 | — |
| EN02 OA 03 | 3 | Frequent expressions · Evidence of oral comprehension and En | 33 % | 14 % | 8.9 | — |
| EN02 OA 05 | 2 | Act an action · Responding personally and creatively to list | 33 % | 40 % | 13.8 | — |
| LE02 OA 03 | 2 | Construir una película mental | 33 % | 33 % | 11.9 | — |
| TE02 OA 01 | 2 | Más de una idea · Diseño de objetos tecnológicos para necesi | 33 % | 40 % | 13.0 | — |
| TE02 OA 02 | 3 | Orden y dependencias · Organización de tareas, materiales y  | 33 % | 67 % | 11.4 | respuesta «depende» en ejercicio cerrado |
| TE02 OA 05 | 2 | Capas visuales simples · Dibujo digital para representar ide | 33 % | 43 % | 9.8 | — |
| EF02 OA 11 | 3 | Implementos supervisados | 35 % | 100 % | 19.5 | — |
| MA02 OA 03 | 1 | Más decenas decide | 38 % | 100 % | 20.7 | — |
| MA02 OA 14 | 4 | Dar y seguir un recorrido | 50 % | 100 % | 12.3 | respuesta «depende» en ejercicio cerrado |
| EF02 OA 07 | 1 | Muchas maneras de estar activo | 71 % | 75 % | 19.2 | — |
| MA02 OA 02 | 2 | Del material al dibujo | 100 % | 100 % | 18.2 | — |

## 3.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 25 | 45 % | 0 |
| ciencias-naturales | 55 | 50 % | 0 |
| educacion-fisica-salud | 48 | 46 % | 0 |
| historia-geografia-ciencias-sociales | 72 | 51 % | 2 |
| ingles-propuesta | 69 | 30 % | 27 |
| lengua-cultura-pueblos-originarios-ancestrales | 116 | 49 % | 2 |
| lenguaje-comunicacion | 157 | 43 % | 1 |
| matematica | 112 | 45 % | 5 |
| musica | 35 | 49 % | 1 |
| orientacion | 35 | 37 % | 0 |
| tecnologia | 33 | 45 % | 1 |

**Clases marcadas para lectura prioritaria (3.º básico):** 39 de 757.

### Segunda lectura crítica de las 757 clases

Cada una de las 757 clases de 3.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional; solo un lector confirmó el teléfono 147 en ChileAtiende.

| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 112 | Ejes que no parten de 0 mal descritos; error de ejemplo no plausible (5:100); dinero imposible (precios terminados en 5); aritmética fuera de nivel (2.500 − 2.000, divisiones por decenas); definición de vértice que contradecía el cono; prisma triangular fuera del OA; ejercicios copiados del ejemplo resuelto; material irrealizable (328 tapas). |
| Lenguaje y Comunicación | 157 | 17 actividades abiertas sin su texto; orden alfabético erróneo; inferencia que el texto decía literalmente; unos 30 ejercicios abiertos pasados a cerrados; expresiones que podían leerse como burla; supuestos sobre la familia; nombre de una persona real en un libro ficticio. |
| Ciencias Naturales | 55 | Estambres «en el centro» de la flor; prueba no justa (dos variables a la vez); mito del cartón de huevos; mano como material opaco; eco sin superficie lejana; aritmética fuera de nivel; seguridad al mirar eclipses. |
| Historia, Geografía y Ciencias Sociales | 72 | Ciudadanía ateniense mal definida; carreras de carros atribuidas al anfiteatro; acueducto definido solo como puente; Atenas y Esparta «en el mismo país»; teléfono 147 verificado y afirmación no comprobable retirada; fuentes sin fecha tratadas como «la más nueva». |
| Inglés | 69 | Calcos del español (I change my idea); «in the hospital» sobre un médico; glosas erróneas (sleep tight, desk); estructuras no enseñadas; respuesta que contradecía la consigna (an frente a a); enunciados que daban la respuesta. |
| Lengua y Cultura de los Pueblos Originarios | 116 | 33 ejercicios aritméticos triviales puestos para el verificador reemplazados; «ruka» pasó a «casa mapuche»; afirmaciones culturales generalizadas; conteos erróneos; atribución falsa de una ficha a la educadora; estereotipos del ejemplo retirados. |
| Educación Física y Salud | 48 | Cifras de pulso y respiración sin número que lograr; visión periférica mal enseñada; «salto mortal» retirado; escaleras, empujones y bebidas energizantes; contradicciones de metas; aritmética fuera de nivel. |
| Orientación | 35 | Intimidad y consentimiento con excepción de salud explícita; origen de la vida en lenguaje sobrio; consumo de drogas con salida segura; supuestos sobre la familia; «copiar es copiar sin entender» falso. |
| Música | 35 | Explicación de duración que daba 5 y no 4 pulsos; siglos con años de cuatro cifras retirados; datos de obras y autores generalizados; digitaciones de flauta agregadas; supuestos sobre abuelos. |
| Artes Visuales | 25 | Ejercicios sobre lo no enseñado (semicírculo, cono, profundidad); regla de seguridad que contradecía su material (tierra); ocho supuestos sobre la familia; «mirete» sin definición. |
| Tecnología | 33 | Tarea de reordenar frases ya ordenadas; ejemplo que cumplía «todos los criterios» con una punta que corta; «regar una vez por semana» retirado; reglas de seguridad de lijado, arcilla y cola; insumo ficticio rotulado. |

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Lenguaje (mitos, novelas, biografías, relatos históricos, cartas, catálogo digital, diccionario ilustrado, revistas y diarios, apoyos para exponer); Historia (legados griegos, arte romano, Greenwich, líneas de referencia); Ciencias (coníferas, hábitat del mamífero, efectos de la alimentación); Inglés (Easter, rimas, figuras y lugares); Música (reiteraciones, digitaciones de flauta, audición y creación); Matemática (minutos sueltos, números cercanos a 1.000, redes del cubo); Educación Física (giro de 180°, desmarque); Orientación (derecho a ser diferente, intereses propios, gestora de su vida).
- **Abiertos:** Música OA 03 pide escuchar al menos 20 músicas y las fichas son escritas; Artes OA 04 pide 15 + 15 + 15 obras al año y las del cuaderno son inventadas; Lenguaje: mitos, leyendas, cuentos folclóricos y novelas reales con derechos de autor; Lengua y Cultura de los Pueblos Originarios: textos, oraciones y relatos reales en lengua indígena, que aporta el educador o educadora tradicional; software educativo, audio y video en varias asignaturas; Educación Física OA 04 (bicicleta y playa solo como contexto) y los pasos de danzas concretas.
- **Decisiones que dependen del programa oficial:** si el prisma y la pirámide de base triangular son de 3.º (se retiró el prisma triangular y se dejó la pirámide), si los ejes que no parten de 0 y la hora de 24 horas son contenido del nivel, y si «moda» corresponde a 3.º (se usó «valor más frecuente»).

### Clases marcadas de 3.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| EN03 OA 02 | 2 | Identify abilities and feelings | 8 % | 0 % | 13.2 | — |
| EN03 OA 11 | 2 | Introduce a fictional person | 8 % | 33 % | 13.7 | — |
| EN03 OA 07 | 1 | Read about school and home | 10 % | 0 % | 9.8 | — |
| EN03 OA 02 | 3 | Locate possession, quantity and position | 10 % | 0 % | 19.1 | — |
| EN03 OA 02 | 4 | Recognize actions in progress | 10 % | 0 % | 12.4 | — |
| EN03 OA 12 | 1 | Share safe fictional information | 11 % | 33 % | 16.8 | — |
| EN03 OA 10 | 3 | Contrast /s/ and /z/ | 15 % | 0 % | 13.7 | — |
| EN03 OA 07 | 3 | Read about occupations and places | 16 % | 0 % | 12.7 | — |
| MA03 OA 22 | 3 | Relacionar 1.000 g y 1 kg | 17 % | 0 % | 9.9 | — |
| EN03 OA 02 | 1 | Follow instructions and introductions | 18 % | 33 % | 12.6 | — |
| LE03 OA 03 | 3 | Fábula sin reducirla a una moraleja | 18 % | 67 % | 15.3 | respuesta «depende» en ejercicio cerrado |
| EN03 OA 01 | 3 | Sequence a short song or story | 20 % | 0 % | 13.3 | — |
| EN03 OA 11 | 1 | Exchange classroom requests | 20 % | 0 % | 13.3 | — |
| EN03 OA 03 | 4 | Order three events | 21 % | 33 % | 12.1 | — |
| EN03 OA 07 | 2 | Read about animals and shapes | 21 % | 33 % | 10.2 | — |
| EN03 OA 10 | 1 | Notice and produce /w/ | 21 % | 0 % | 12.7 | — |
| EN03 OA 10 | 2 | Explore /th/ safely | 21 % | 0 % | 14.5 | — |
| MA03 OA 12 | 2 | Explorar cambios verticales | 21 % | 33 % | 11.0 | — |
| EN03 OA 12 | 4 | Request and locate an item | 22 % | 0 % | 13.3 | — |
| EN03 OA 12 | 5 | Describe actions happening now | 22 % | 33 % | 11.6 | — |
| EN03 OA 14 | 4 | Describe visible actions | 24 % | 33 % | 17.8 | — |
| MA03 OA 22 | 1 | Comparar con una balanza | 24 % | 100 % | 10.5 | respuesta «depende» en ejercicio cerrado |
| TE03 OA 02 | 3 | Ordenar dependencias y puntos de control | 25 % | 100 % | 12.2 | respuesta «depende» en ejercicio cerrado |
| EN03 OA 12 | 2 | Express ability and quantity | 26 % | 0 % | 11.7 | — |
| EN03 OA 06 | 4 | Follow written instructions | 26 % | 33 % | 11.4 | — |
| EN03 OA 09 | 5 | Express and support an opinion | 26 % | 33 % | 14.4 | — |
| EN03 OA 11 | 4 | Give a brief supported presentation | 28 % | 33 % | 8.1 | — |
| EN03 OA 04 | 4 | Focus on key words | 29 % | 0 % | 13.3 | — |
| EN03 OA 08 | 4 | Reread for a specific question | 29 % | 33 % | 11.1 | — |
| EN03 OA 13 | 4 | Write and check a supported sentence | 29 % | 25 % | 16.8 | — |
| EN03 OA 11 | 3 | Ask for a missing word | 30 % | 0 % | 11.3 | — |
| MA03 OA 24 | 2 | Ordenar frecuencias | 38 % | 100 % | 12.6 | respuesta «depende» en ejercicio cerrado |
| EN03 OA 14 | 2 | Write feelings and quantities | 41 % | 33 % | 20.3 | — |
| LC03 OA LR01 | 5 | Crear una devolución que aporta a revitalizar | 43 % | 100 % | 20.4 | — |
| HI03 OA 07 | 1 | Distinguir globo y mapa | 50 % | 100 % | 13.5 | respuesta «depende» en ejercicio cerrado |
| MA03 OA 14 | 3 | Describir recorridos sin ambigüedad | 57 % | 100 % | 12.8 | respuesta «depende» en ejercicio cerrado |
| LC03 OA 12 | 1 | Reconocer relaciones concretas | 67 % | 100 % | 9.9 | respuesta «depende» en ejercicio cerrado |
| HI03 OA 15 | 1 | Formular una pregunta de investigación | 73 % | 100 % | 10.8 | respuesta «depende» en ejercicio cerrado |
| MU03 OA 08 | 1 | Identificar una fortaleza con evidencia | 78 % | 100 % | 13.8 | respuesta «depende» en ejercicio cerrado |

## 4.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 25 | 43 % | 2 |
| ciencias-naturales | 71 | 58 % | 5 |
| educacion-fisica-salud | 49 | 48 % | 4 |
| historia-geografia-ciencias-sociales | 82 | 47 % | 5 |
| ingles-propuesta | 69 | 30 % | 43 |
| lengua-cultura-pueblos-originarios-ancestrales | 126 | 47 % | 9 |
| lenguaje-comunicacion | 161 | 41 % | 16 |
| matematica | 118 | 45 % | 2 |
| musica | 35 | 49 % | 1 |
| orientacion | 40 | 42 % | 4 |
| tecnologia | 35 | 45 % | 2 |

**Clases marcadas para lectura prioritaria (4.º básico):** 93 de 811.

### Segunda lectura crítica de las 811 clases

Cada una de las 811 clases de 4.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Varios lectores declararon que no pudieron resolver uno por uno todos los ejercicios.

| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 118 | 99 − 45 explicado como 56 (es 54); estimaciones que no calzaban (640 − 285 + 152); errores de división con resto que no cumplían la prueba; ejercicio sin solución (dos números de suma 700 con estimación 600); cuadrado de 6 cm² imposible; unos 30 ejercicios copiados del ejemplo resuelto; divisores de dos cifras y dividendos de tres cifras fuera del OA; comparación con 1/2 que no discriminaba; gráfico de ejes truncados descrito como «el doble». |
| Lenguaje y Comunicación | 161 | Unas 30 preguntas cerradas sobre textos que nunca se entregaban; 4 mayúsculas contadas de más (cordillera); pingüinos «de lugares fríos» (falso para el de Humboldt); divisor de dos cifras fuera de nivel; salto lógico del queque; «coma tras de pronto» como obligatoria; «cuenta» como «cuento»; ordenaciones con dos soluciones; escenas de riesgo (río, pozo) y supuestos sobre la familia. |
| Ciencias Naturales | 71 | Ruta del mensaje nervioso con el ojo y el oído pasando por la médula (falso); «núcleo de 3.440 km» ajustado para que sumara; globo que pesa más inflado; imán que levanta clips a distancia; hibernación de «días»; cuchara de plástico que se hunde; llave que sube el agua 20 mL; bolsa de plástico cerca de la cara. |
| Historia, Geografía y Ciencias Sociales | 82 | Mesoamérica presentada solo como territorio maya; incas sin calendario por comparación; «allillanchu» como saludo; semáforo y vereda atribuidos a la municipalidad; presupuesto de escuelas decidido por el Congreso; río Tíber y «Educación Cívica» de otro nivel; siete ejercicios abiertos pasados a elección; «y sangre» en las ofrendas retirado. |
| Inglés | 69 | Respuestas con dos opciones válidas (small o blue); estructuras no enseñadas (How old is he/she, Do they…); regla de I don't know incoherente; glosas faltantes (Mr., Dr., near, river); Easter definido solo como huevos; leche para un gato; «mariquita» por «chinita»; textos de escucha sin su guion. |
| Lengua y Cultura de los Pueblos Originarios | 126 | Fichas, testimonios y textos que el ejercicio citaba y la clase no entregaba; «según el educador tradicional, su pueblo…» retirado; idea central equivocada en un relato de práctica; «antu» y «ruca» presentados como error de grafía; «espíritu enojado» en distractores; foto de un compañero en un afiche; conteos que no calzaban; unos 14 «Ordena…» con dos órdenes posibles. |
| Educación Física y Salud | 49 | Correr de espaldas; dolor de rodilla resuelto con «cambiar a caminar»; giros de cuello y rodilla; pañuelo-cola con «sin contacto»; cemento mojado que «no resbala»; 55 usos de «persona de tu casa»; 60 min «de actividad» sin intensidad; contradicciones de metros y de tiempos de calentamiento. |
| Orientación | 40 | Frutas y verduras contadas como dos grupos contra su explicación; comparación de Ema con Pablo en una clase que enseña a no etiquetar; campaña de «4 útiles» que presiona a familias; revisión de garganta como excepción de salud; 29 ejercicios de redacción libre pasados a elección; ejemplos de control o aislamiento reescritos. |
| Música | 35 | Motivo de 5 pulsos dentro de secciones de 4; regla de variación ambigua; ejercicios cerrados con respuesta libre; supuesto de canción de cuna en el hogar; ejemplo de «misma idea» con dos lecturas. |
| Artes Visuales | 25 | Resumen del relato de Trentren Vilu y Kaikai Vilu reducido a lo general; Caleuche y cerámica diaguita sin afirmaciones que el cuaderno no puede sostener; obras del OA 04 rotuladas como inventadas; «la lana es pesada» y «la plasticina se ensucia» retirados; unos 73 ajustes entre ambigüedades y distractores absurdos. |
| Tecnología | 35 | Insumos no entregados (plan del atril, letra de la diapositiva); sumas puestas para el verificador cambiadas por cálculos con sentido; carpeta con símbolos contra la regla de nombres; direcciones inventadas terminadas en .cl pasadas a .example; «girasoles siguen al Sol» matizado; hojas de cálculo y diagramas integrados en clases existentes. |

#### Desajuste entre el texto del OA y los títulos de las clases

Los lectores confirmaron que en el repositorio el texto oficial citado bajo varios OA de 4.º no coincide con el título y las etapas de sus clases: Lenguaje OA 11 a 18 (por ejemplo, el OA 11 cita «escribir frecuentemente» y sus clases enseñan diccionario y orden alfabético; el OA 16 cita «planificar la escritura» y sus clases tratan la letra legible), y Lengua y Cultura de los Pueblos Originarios OA 10 a 16 (el OA 10 cita relatos fundacionales y sus clases tratan tiempo y espacio). Los cuadernos siguieron el título de la clase y repartieron el contenido del OA dentro de las clases existentes. Conviene corregir esa asignación en el currículo; no se hizo aquí porque exige el Programa de Estudio.

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Lenguaje (ortografía b-v, h, ay/hay/ahí y acentuación del OA 21; diario de vida); Matemática (decena de mil; fracciones con denominador 12 y 100); Historia (escritura y construcciones mayas, extensión azteca, sociedad en la tabla comparativa, ubicación frente a los océanos); Inglés (partes de la casa, lugares de la ciudad, presentar a otros, acciones en curso); Tecnología (hoja de cálculo y diagramas); Educación Física (base a pequeña altura, elementos de la cueca); Orientación (aceptar las emociones ajenas, vínculo entre sexualidad y origen de la vida).
- **Abiertos:** Lenguaje OA 11 (no hay clase que enseñe a escribir con frecuencia como hábito) y OA 15 (letra clara solo como criterio); Música OA 03 (escuchar al menos 20 músicas, sin audio) y OA 05 (creación con alturas); Artes OA 04 (15 + 15 + 15 obras reales al año, las del cuaderno son inventadas) y OA 03 (fotografía, imágenes digitales y software); Tecnología OA 05 (no se enseña a usar un programa real de hojas de cálculo); software geométrico y educativo en Matemática (OA 17, 23, 24 y 26); Lengua y Cultura de los Pueblos Originarios: relatos fundacionales, cosmovisión, textos y oraciones en lengua indígena (educador o educadora tradicional); Inglés: audio, video y discriminación auditiva de /s/-/z/ y /w/-/th/.
- **Decisiones que dependen del programa oficial:** divisores de dos cifras y factores de dos cifras en Matemática (se usaron factores de dos cifras y divisor de un dígito); convención de coordenadas y de 12:00 p.m. / 00:00 (convenciones didácticas del cuaderno); si las inecuaciones usan números naturales; clases de OA 11 a 18 de Lenguaje y OA 10 a 16 de Lengua y Cultura cuyos títulos no corresponden a su texto de OA.

### Clases marcadas de 4.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| LE04 OA 24 | 4 | Explorar una escena desde otro rol · Experiencia y lenguaje  | 6 % | 20 % | 13.6 | — |
| HI04 OA 03 | 1 | Ubicar el problema en tiempo y espacio · Civilización inca | 7 % | 20 % | 12.0 | — |
| EN04 OA 11 | 2 | Introduce a fictional person · Brief classroom interaction a | 11 % | 29 % | 14.1 | — |
| EN04 OA 10 | 2 | Explore /th/ safely · English sounds through chants, rhymes  | 11 % | 0 % | 14.7 | — |
| EN04 OA 12 | 5 | Describe actions happening now · Supported oral expression f | 13 % | 14 % | 16.0 | — |
| LE04 OA 19 | 3 | Comparar matices entre alternativas · Adverbios para precisa | 13 % | 29 % | 9.5 | — |
| EN04 OA 02 | 4 | Recognize actions in progress · Listening for familiar topic | 14 % | 0 % | 12.5 | — |
| CN04 OA 13 | 1 | Observar y separar evidencia de interpretación · Roce, peso  | 16 % | 17 % | 10.5 | — |
| EN04 OA 02 | 2 | Identify abilities and feelings · Listening for familiar top | 16 % | 0 % | 13.8 | — |
| EN04 OA 07 | 5 | Compare information without stereotyping · Reading about fam | 16 % | 30 % | 18.5 | — |
| EN04 OA 01 | 2 | Follow actions in a chant · Listening to rhymes, chants, son | 17 % | 12 % | 15.1 | — |
| EN04 OA 12 | 1 | Share safe fictional information · Supported oral expression | 17 % | 14 % | 22.9 | — |
| EN04 OA 10 | 3 | Contrast /s/ and /z/ · English sounds through chants, rhymes | 18 % | 14 % | 11.2 | — |
| LC04 OA LS05 | 3 | Seleccionar palabras contextualizadas · Creaciones digitales | 18 % | 38 % | 14.2 | — |
| EN04 OA 02 | 1 | Follow instructions and introductions · Listening for famili | 19 % | 14 % | 16.8 | — |
| EN04 OA 03 | 4 | Order three events · Demonstrating detailed listening compre | 19 % | 29 % | 14.9 | — |
| LE04 OA 03 | 3 | Fábula sin reducirla a una moraleja · Repertorio literario a | 19 % | 33 % | 12.5 | — |
| EN04 OA 07 | 2 | Read about animals and shapes · Reading about familiar cross | 19 % | 12 % | 13.9 | — |
| EN04 OA 11 | 3 | Ask for a missing word · Brief classroom interaction and pre | 19 % | 0 % | 14.2 | — |
| EN04 OA 12 | 4 | Request and locate an item · Supported oral expression for f | 20 % | 0 % | 18.7 | — |
| HI04 OA 16 | 2 | Interrogar fuentes y reconocer su procedencia · Resolución d | 21 % | 43 % | 15.5 | — |
| EN04 OA 07 | 3 | Read about occupations and places · Reading about familiar c | 21 % | 0 % | 13.9 | — |
| CN04 OA 13 | 2 | Formular una pregunta o predicción comprobable · Roce, peso  | 21 % | 17 % | 16.0 | — |
| EN04 OA 06 | 4 | Follow written instructions · Reading short literary and fun | 21 % | 12 % | 14.3 | — |
| EN04 OA 04 | 4 | Focus on key words · Strategies for listening comprehension | 22 % | 20 % | 12.7 | — |
| EN04 OA 07 | 4 | Read about food and celebrations · Reading about familiar cr | 22 % | 14 % | 14.6 | — |
| EN04 OA 01 | 4 | Identify speakers in a dialogue · Listening to rhymes, chant | 22 % | 25 % | 9.1 | — |
| EN04 OA 02 | 3 | Locate possession, quantity and position · Listening for fam | 22 % | 0 % | 16.8 | — |
| EN04 OA 03 | 5 | Show evidence for an answer · Demonstrating detailed listeni | 22 % | 33 % | 14.6 | — |
| LC04 OA LR05 | 2 | Seleccionar expresiones autorizadas · Creaciones digitales p | 23 % | 43 % | 12.1 | — |
| LE04 OA 28 | 4 | Ajustar registro y referente · Vocabulario nuevo en interven | 23 % | 43 % | 13.2 | — |
| EN04 OA 12 | 2 | Express ability and quantity · Supported oral expression for | 23 % | 0 % | 14.4 | — |
| EN04 OA 07 | 1 | Read about school and home · Reading about familiar cross-cu | 23 % | 0 % | 17.0 | — |
| EN04 OA 03 | 2 | Select the general idea · Demonstrating detailed listening c | 25 % | 33 % | 11.9 | — |
| EN04 OA 03 | 3 | Locate one explicit detail · Demonstrating detailed listenin | 25 % | 33 % | 12.8 | — |
| EN04 OA 14 | 3 | Describe locations · Image-supported writing for familiar to | 25 % | 29 % | 15.8 | — |
| LE04 OA 08 | 2 | Orientarse en colecciones · Uso responsable de la biblioteca | 25 % | 25 % | 12.1 | — |
| LE04 OA 10 | 2 | Raíces que conservan significado · Significado por contexto  | 25 % | 40 % | 10.6 | — |
| LE04 OA 28 | 1 | Recuperar significado desde el texto · Vocabulario nuevo en  | 25 % | 29 % | 14.5 | — |
| LE04 OA 28 | 2 | Ensayar una paráfrasis · Vocabulario nuevo en intervenciones | 25 % | 33 % | 15.9 | — |
| LE04 OA 21 | 1 | Mayúsculas y puntos con propósito · Ortografía para facilita | 26 % | 33 % | 11.9 | — |
| EN04 OA 01 | 1 | Track repeated sounds in a rhyme · Listening to rhymes, chan | 26 % | 22 % | 11.7 | — |
| EN04 OA 01 | 3 | Sequence a short song or story · Listening to rhymes, chants | 26 % | 11 % | 17.1 | — |
| EN04 OA 10 | 5 | Perform a brief intelligible dialogue · English sounds throu | 26 % | 22 % | 11.8 | — |
| EF04 OA 06 | 3 | Explorar flexibilidad sin rebotes forzados · Condición físic | 27 % | 44 % | 15.3 | — |
| EN04 OA 12 | 3 | Describe and state a prohibition · Supported oral expression | 28 % | 29 % | 17.7 | — |
| LC04 OA 17 | 2 | Explorar cualidades sin copiar símbolos · Creación con sonor | 28 % | 38 % | 13.6 | — |
| EN04 OA 09 | 1 | Illustrate one supported idea · Responding to reading throug | 28 % | 29 % | 13.9 | — |
| EN04 OA 09 | 2 | Build a figure or scene · Responding to reading through mult | 28 % | 38 % | 14.1 | — |
| TE04 OA 01 | 6 | Seleccionar y comunicar una propuesta · Diseño de objetos y  | 28 % | 38 % | 12.1 | — |
| AR04 OA 01 | 2 | Transformar una observación en intención visual · Creación v | 29 % | 38 % | 13.8 | — |
| EF04 OA 04 | 5 | Evaluar el cuidado del espacio utilizado · Actividad física  | 29 % | 44 % | 13.8 | — |
| LE04 OA 10 | 3 | Prefijos que modifican · Significado por contexto y morfolog | 29 % | 40 % | 15.9 | — |
| LE04 OA 18 | 3 | Mejorar conectores · Revisión y edición con propósito | 29 % | 40 % | 8.8 | — |
| LE04 OA 22 | 3 | Sostener memoria entre episodios · Escucha literaria de obra | 29 % | 29 % | 10.8 | — |
| OR04 OA 07 | 4 | Acordar, reparar y pedir ayuda cuando corresponde · Resoluci | 29 % | 44 % | 14.2 | — |
| EN04 OA 04 | 3 | Use images without guessing alone · Strategies for listening | 29 % | 29 % | 12.0 | — |
| EN04 OA 05 | 4 | Express a preference with a reason · Responding personally a | 29 % | 43 % | 10.6 | — |
| EN04 OA 09 | 5 | Express and support an opinion · Responding to reading throu | 29 % | 25 % | 11.9 | — |
| CN04 OA 12 | 2 | Formular una pregunta o predicción comprobable · Efectos de  | 29 % | 43 % | 11.6 | — |
| EF04 OA 04 | 2 | Preparar una actividad al aire libre · Actividad física resp | 30 % | 43 % | 12.0 | — |
| EN04 OA 11 | 1 | Exchange classroom requests · Brief classroom interaction an | 30 % | 17 % | 14.3 | — |
| EN04 OA 03 | 1 | Identify people, animals and objects · Demonstrating detaile | 31 % | 38 % | 12.9 | — |
| CN04 OA 14 | 3 | Comparar casos con un criterio común · Diseño tecnológico qu | 31 % | 38 % | 11.0 | — |
| EN04 OA 14 | 2 | Write feelings and quantities · Image-supported writing for  | 31 % | 25 % | 16.9 | — |
| OR04 OA 03 | 3 | Comprender intimidad, consentimiento y límites · Sexualidad  | 31 % | 43 % | 12.4 | — |
| TE04 OA 06 | 2 | Editar mediante selección y movimiento · Creación y edición  | 31 % | 43 % | 14.2 | — |
| EN04 OA 10 | 4 | Use sounds in a chant · English sounds through chants, rhyme | 31 % | 33 % | 15.8 | — |
| EN04 OA 13 | 2 | Complete from a word bank · Model-supported English writing | 31 % | 20 % | 13.3 | — |
| MA04 OA 24 | 2 | Construir y comparar cuerpos | 31 % | 100 % | 15.5 | respuesta «depende» en ejercicio cerrado |
| OR04 OA 09 | 3 | Respetar el trabajo y concentración ajenos · Hábitos, esfuer | 31 % | 44 % | 13.8 | — |
| LE04 OA 01 | 2 | Pausas que construyen sentido · Lectura oral fluida y expres | 32 % | 33 % | 14.9 | — |
| OR04 OA 06 | 3 | Actuar solidariamente sin sustituir · Solidaridad, empatía,  | 32 % | 43 % | 13.6 | — |
| EN04 OA 05 | 2 | Respond through mime and action · Responding personally and  | 32 % | 33 % | 14.2 | — |
| EN04 OA 09 | 3 | Dramatize with textual evidence · Responding to reading thro | 32 % | 38 % | 14.1 | — |
| EF04 OA 08 | 2 | Localizar y contar pulso con apoyo · Registro de respuestas  | 33 % | 38 % | 11.6 | — |
| EN04 OA 10 | 1 | Notice and produce /w/ · English sounds through chants, rhym | 33 % | 38 % | 13.1 | — |
| HI04 OA 05 | 3 | Caracterizar dimensiones con evidencia · Pueblos indígenas a | 33 % | 43 % | 11.9 | — |
| HI04 OA 10 | 1 | Ubicar el problema en tiempo y espacio · Paisajes regionales | 33 % | 43 % | 16.2 | — |
| LC04 OA 10 | 3 | Explorar una noción de espacio · Nociones indígenas de tiemp | 33 % | 40 % | 17.1 | — |
| LE04 OA 21 | 4 | Ge-gi y je-ji en familias · Ortografía para facilitar compre | 33 % | 25 % | 10.6 | — |
| LE04 OA 21 | 5 | Terminaciones cito-cita · Ortografía para facilitar comprens | 33 % | 25 % | 13.9 | — |
| LC04 OA 15 | 3 | Distinguir acceso público y restringido · Patrimonio cultura | 44 % | 67 % | 22.3 | — |
| LC04 OA 13 | 4 | Proponer una acción situada · Vida en armonía e interdepende | 47 % | 60 % | 21.0 | — |
| CN04 OA 10 | 4 | Construir una explicación o modelo con límites · Estados de  | 56 % | 83 % | 11.9 | respuesta «depende» en ejercicio cerrado |
| LC04 OA 09 | 4 | Valorar sin apropiarse ni homogeneizar · Aportes vivos de cu | 56 % | 75 % | 20.6 | — |
| LE04 OA 05 | 6 | Sintetizar hallazgos y próximos pasos · Comprensión de poema | 58 % | 75 % | 24.2 | — |
| LC04 OA 11 | 2 | Relacionar material, técnica y naturaleza · Arte y técnicas  | 64 % | 100 % | 20.6 | — |
| AR04 OA 01 | 6 | Crear una obra personal que articule referentes · Creación v | 75 % | 78 % | 20.8 | — |
| HI04 OA 06 | 4 | Comparar perspectivas, cambios o continuidades · Paralelos,  | 75 % | 86 % | 13.1 | respuesta «depende» en ejercicio cerrado |
| MU04 OA 08 | 2 | Localizar un área de mejora · Reflexión sobre escucha, inter | 78 % | 67 % | 11.4 | respuesta «depende» en ejercicio cerrado |
| MA04 OA 19 | 4 | Comparar y corregir construcciones | 80 % | 100 % | 10.5 | respuesta «depende» en ejercicio cerrado |
| LC04 OA 15 | 4 | Recrear sólo lo autorizado · Patrimonio cultural de comunida | 81 % | 71 % | 23.4 | — |

## 5.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 27 | 43 % | 5 |
| ciencias-naturales | 64 | 60 % | 5 |
| educacion-fisica-salud | 49 | 40 % | 21 |
| historia-geografia-ciencias-sociales | 106 | 55 % | 6 |
| ingles-propuesta | 71 | 25 % | 63 |
| lengua-cultura-pueblos-originarios-ancestrales | 135 | 59 % | 7 |
| lenguaje-comunicacion | 166 | 43 % | 51 |
| matematica | 115 | 46 % | 17 |
| musica | 35 | 39 % | 16 |
| orientacion | 41 | 39 % | 9 |
| tecnologia | 35 | 33 % | 20 |

**Clases marcadas para lectura prioritaria (5.º básico):** 220 de 844.

### Segunda lectura crítica de las 844 clases

Cada una de las 844 clases de 5.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios; los lectores sí lo intentaron, y varios advirtieron que no pudieron recalcular cada cifra con herramienta.

| Asignatura | Clases | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 115 | Unos 20 ejercicios idénticos al ejemplo resuelto de su clase en OA 01 a 11 y otros tantos en OA 12 a 23; «5.060.000 > 5.600.000 porque el 6 está más a la izquierda» (falso); denominador común mayor que 12 «no hace falta» (falso: 1/3 + 1/5); giro de 180° con fórmula algebraica y números negativos de 7.º; «el doble de 7 más 3» con dos lecturas; rectángulo de vértices (1,2), (4,2), (4,5), (1,5) que era un cuadrado; regla de «poco posible» con casos no clasificados; contextos poco creíbles (agua de un colegio, carrera de 12 a 38 s). |
| Lenguaje y Comunicación | 166 | Unos 190 ejercicios de OA 02 a 08 que citaban un texto («el faro», «el poema de la lluvia») que el enunciado no entregaba; cuentos de Nico y Lía ausentes en OA 16; conteos erróneos (22 palabras y no 19, resumen de 30 palabras contra la regla de un tercio); «pájaro / rápido» como asonante y «papel / miel» como asonante (es consonante); nombre «Marta Lagos» igual al de una persona real; estereotipo de género en la caleta; unos 25 ejercicios de OA 18 a 26 idénticos al ejemplo resuelto; «salto» como palabra que el corrector corregiría; escena de un cable eléctrico arreglado sin adulto; «grábate» en una actividad oral. |
| Ciencias Naturales | 64 | Glóbulos rojos comparados con células nerviosas «en una gota de sangre»; virus «no es célula porque es más pequeño»; absorción solo en el intestino delgado contra la clase; cargador sin uso con consumo sobreestimado; tocar ampolletas encendidas «si hay adulto»; tabla de mareas con una hora de caminata a las 21:00; pregunta que sugería beber agua de río; «bajo 200 m todo es oscuro»; «promedio» no enseñado; siete ejercicios que repetían cifras del ejemplo. |
| Historia, Geografía y Ciencias Sociales | 106 | Voto femenino sin precisar (1935 municipal y 1949 todas las elecciones) y convención de los derechos del niño sin fecha; «maratón» para 5 km y Quellón «pueblo pesquero»; cifras de consumo de agua y luz irreales; mensaje de sismo que invertía el consejo («corre al cerro» contra «no hay maremoto»); «adobe y teja bastan para reconocer un edificio colonial» (falso); «Magallanes llegó a la India»; «universidad solo en Perú»; citas atribuidas a Las Casas y Guamán Poma que eran resúmenes; fundación con nombre real; obras de arte coloniales y relieve sin cobertura, agregados. |
| Inglés | 71 | «There is some milk» como poca cantidad; rima ten/again; glosa «stand in a line» como «ponte de pie»; estructuras no enseñadas (has, wakes, does, played); «Can a bird fly?» contra el pingüino de la misma clase; jirafa «vive en la jungla»; familias y abuelas en diálogos; diálogos, ilustraciones y canciones del OA sin ejercicio, agregados; 8 respuestas aritméticas planas pasadas a cálculo verificado. |
| Lengua y Cultura de los Pueblos Originarios | 135 | Ritos y costumbres inventados (silencio para recordar el relato, dar gracias al primer pasto, agradecer a la tierra y a las manos) cambiados por prácticas neutras; «según el educador tradicional dijo que chaltumay se usa para…» retirado; «mari mari significa que todos somos hermanos» y el distractor «mapusur» retirados; huerto donde «se dice ko / chaltumay al traer agua»; 14 ejercicios abiertos con varias respuestas pasados a cerrados; conteos que no calzaban con el texto (6 oraciones y no 7); «los pueblos indígenas aportan…» generalizado. |
| Educación Física y Salud | 49 | Carreras de 20 m en espacios de 4×3 y 3×3 m; calcetines por vuelta que contradecían el circuito; zapateado y escobillado con 8 tiempos (tienen 4); básquetbol en «tres pasos y pase» (regla de balonmano); polera lavada «cada 2 usos»; botella «compartida» contra «no compartas»; sumas de pulsos sin sentido; pedazos de globo reventado sin advertencia. |
| Orientación | 41 | «Para» como límite ante un contacto en línea contradiciendo «no respondas»; encuentro con alguien conocido solo en línea «con un adulto»; foto íntima descrita de forma explícita; «nadie puede mirar tu cuerpo» sin la excepción del control de salud; estereotipo asociado al país de origen; «habla con la familia» como único factor protector; «mayoría simple» definida como mayoría relativa; datos de drogas con matices de legalidad suavizados. |
| Música | 35 | Ejemplo que pedía 6 músicas y listaba 3 («faltan 12»); criterios 3 de 5 que pasaban a 5 con un solo cambio; tambor grave que «sube»; obra citada sin lugar de baile; melodía de práctica sin ritmo; «¿qué dos preguntas ayudan a conocer el contexto?» con cuatro respuestas válidas; más de 20 menciones a «adulto de tu casa». |
| Artes Visuales | 27 | Forma abierta definida como «contorno cerrado con una abertura»; trabajos C y D con «materiales similares» siendo témpera y papel con pegamento; «gris» como color frío; «menos agua para evitar grumos»; «las sombras no eran negras» sin matiz; tijeras «con el filo hacia adentro»; «ángulo normal» no definido; «cambian tres elementos, ¿cuántos?». |
| Tecnología | 35 | Sumas sin sentido (fichas de tres pruebas, puntajes de cuatro evaluadores) cambiadas por diferencias; puerta de 200 cm a escala 1:2 en una hoja y ranura de 25 cm con pieza de 24 cm que «no encaja»; asas probadas con 5 y 9 kg; perforador sobre paredes de caja; empate de 8 puntos sin criterio; fotos de compañeros sin permiso de todos; «solo 2 de 30 pueden pagarlo» supone la situación económica de las familias. |

#### Desajuste entre el texto del OA y los títulos de las clases

A diferencia de 4.º básico, los lectores de 5.º no hallaron un desajuste que obligara a cambiar el contenido: los títulos de clase del plan son etapas genéricas (por ejemplo «Reconocer propósito y desafío», «Situar pueblo, territorio y fuente», «Definir necesidad, usuario y criterio»), repetidas en todos los OA de la asignatura, y los autores repartieron el contenido del OA dentro de ellas. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Historia (obras de arte coloniales, relieve de Chile, seguridad en hogar, escuela y espacios públicos); Inglés (diálogos del OA 05, ilustraciones del OA 08, canciones del OA 09); Lengua y Cultura (la lengua que corresponde a cada pueblo, en OA 09); Lenguaje (relato en OA 24; comparación de interpretaciones de una descripción de actividad en OA 30); Orientación (pubertad: maduración de los órganos sexuales; ejemplo de burla por pertenecer a un pueblo originario en el OA 06).
- **Abiertos:** Lenguaje OA 30 (testimonio y descripción de actividad solo se reconocen y se comparan, no se planifican paso a paso), OA 01 (prosodia y lectura en voz alta requieren oír al estudiante) y OA 03, 23 y 25 (obras reales, teatro y películas, que elige el docente); Música OA 03 (escuchar al menos 15 músicas y las obras de Chávez, Guastavino y Satie, sin audio) y OA 04 (digitación de flauta y guitarra, práctica real de instrumentos); Artes OA 04 (50 obras al año, las del cuaderno son descripciones), OA 03 (fotografía, video y diseño digital con programa real); Tecnología OA 05 y 06 (programas reales de presentación, hoja de cálculo y procesador de textos; solo se usa la suma); Matemática OA 06, 07, 18 y 20 (calculadora con computador, software geométrico y educativo) y representaciones pictóricas descritas con texto; Inglés (escucha real, pronunciación y producción oral, formato audiovisual); Lengua y Cultura de los Pueblos Originarios: lengua, pronunciación, textos y relatos reales de cada pueblo (LF01 a LF06, LR y LS) con educador o educadora tradicional, y el solapamiento entre LR05 y LS05; Educación Física (danzas de las demás zonas, solo se enseña la cueca); Ciencias (cuadernos sin experimento ni microscopio real, científicos como Galvani, Ampère, Ohm, Joule y Tesla fuera del OA 08).
- **Decisiones que dependen del programa oficial:** acento diacrítico (dé/de, sé/se, más/mas, aún/aun fuera de las clases), vatios, Wh y kWh en Ciencias OA 11, definición de trapecio como un solo par de lados paralelos, «obra universal» como obra fuera de Chile y Latinoamérica, y la regla numérica de «poco posible» (1 o 2 resultados entre muchos), que es una convención del cuaderno.

### Clases marcadas de 5.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| EN05 OA 09 | 3 | Model a communicative strategy · English sounds through oral | 5 % | 0 % | 13.5 | — |
| AR05 OA 02 | 4 | Crear una respuesta propia · Color complementario, formas, l | 10 % | 33 % | 13.8 | — |
| CN05 OA 14 | 3 | Construir o examinar un modelo · Actividad humana y protecci | 10 % | 12 % | 15.4 | — |
| EN05 OA 01 | 2 | Locate words, chunks and clues · Listening comprehension acr | 11 % | 10 % | 12.0 | — |
| TE05 OA 01 | 5 | Probar con evidencia · Design of technological objects and s | 11 % | 33 % | 13.4 | — |
| EN05 OA 12 | 1 | Notice purpose and context · Dialogues about ability, quanti | 11 % | 12 % | 14.4 | — |
| EN05 OA 08 | 4 | Interact or compose with support · Multimodal response to re | 13 % | 0 % | 17.0 | — |
| EN05 OA 01 | 3 | Model a communicative strategy · Listening comprehension acr | 15 % | 11 % | 7.8 | — |
| EN05 OA 14 | 1 | Notice purpose and context · Writing for the functions of th | 15 % | 0 % | 12.5 | — |
| EN05 OA 04 | 2 | Locate words, chunks and clues · Response and connection aft | 15 % | 0 % | 10.1 | — |
| TE05 OA 03 | 2 | Representar una solución · Safe elaboration with tools and m | 15 % | 20 % | 12.8 | — |
| EN05 OA 13 | 3 | Model a communicative strategy · Model-supported literary an | 15 % | 14 % | 11.9 | — |
| LE05 OA 03 | 3 | Localizar y seleccionar evidencia · Repertorio literario y v | 15 % | 0 % | 14.3 | — |
| MU05 OA 05 | 4 | Ensayar y ajustar desde la escucha · Improvisation and creat | 15 % | 14 % | 11.4 | — |
| AR05 OA 03 | 2 | Explorar una variable visual · Dominio de materiales, herram | 16 % | 25 % | 11.6 | — |
| EN05 OA 04 | 1 | Notice purpose and context · Response and connection after l | 16 % | 14 % | 18.2 | — |
| EF05 OA 07 | 2 | Modelar control y decisión motriz · Planificación regular de | 16 % | 12 % | 14.4 | — |
| EN05 OA 12 | 2 | Locate words, chunks and clues · Dialogues about ability, qu | 16 % | 11 % | 17.9 | — |
| EN05 OA 02 | 5 | Communicate independently · Listening for purpose, ideas and | 16 % | 0 % | 13.4 | — |
| MU05 OA 01 | 2 | Reconocer y representar un rasgo audible · Musical language  | 17 % | 12 % | 14.1 | — |
| EN05 OA 13 | 2 | Locate words, chunks and clues · Model-supported literary an | 18 % | 11 % | 9.4 | — |
| TE05 OA 01 | 4 | Elaborar o configurar · Design of technological objects and  | 18 % | 0 % | 10.7 | — |
| EN05 OA 12 | 5 | Communicate independently · Dialogues about ability, quantit | 18 % | 14 % | 17.1 | — |
| EF05 OA 01 | 1 | Reconocer meta y condiciones de seguridad · Habilidades motr | 18 % | 12 % | 14.6 | — |
| EF05 OA 01 | 3 | Ensayar con variantes accesibles · Habilidades motrices apli | 18 % | 0 % | 16.7 | — |
| EF05 OA 08 | 1 | Reconocer meta y condiciones de seguridad · Pulso y percepci | 18 % | 33 % | 13.7 | — |
| LE05 OA 06 | 2 | Modelar una lectura o producción · Comprensión crítica de te | 18 % | 29 % | 16.4 | — |
| EN05 OA 08 | 2 | Locate words, chunks and clues · Multimodal response to read | 19 % | 0 % | 14.7 | — |
| EN05 OA 06 | 1 | Notice purpose and context · Reading communicative functions | 19 % | 0 % | 13.2 | — |
| LE05 OA 23 | 5 | Producir una respuesta propia · Escucha literaria de obras c | 19 % | 43 % | 15.0 | — |
| EN05 OA 05 | 4 | Interact or compose with support · Reading literary and non- | 19 % | 0 % | 13.0 | — |
| LE05 OA 03 | 5 | Producir una respuesta propia · Repertorio literario y valor | 19 % | 0 % | 14.4 | — |
| OR05 OA 03 | 5 | Practicar comunicación o solicitud de ayuda · Affective and  | 19 % | 22 % | 15.2 | — |
| EN05 OA 04 | 4 | Interact or compose with support · Response and connection a | 19 % | 14 % | 11.8 | — |
| EN05 OA 08 | 1 | Notice purpose and context · Multimodal response to reading | 19 % | 17 % | 13.1 | — |
| EN05 OA 06 | 5 | Communicate independently · Reading communicative functions  | 19 % | 0 % | 14.3 | — |
| LE05 OA 18 | 3 | Localizar y seleccionar evidencia · Revisión y edición para  | 20 % | 17 % | 13.8 | — |
| LE05 OA 05 | 5 | Producir una respuesta propia · Imágenes, figuras y forma po | 20 % | 17 % | 12.7 | — |
| EN05 OA 02 | 3 | Model a communicative strategy · Listening for purpose, idea | 20 % | 0 % | 12.6 | — |
| LE05 OA 05 | 6 | Revisar con retroalimentación · Imágenes, figuras y forma po | 21 % | 0 % | 14.0 | — |
| TE05 OA 01 | 3 | Planificar recursos y seguridad · Design of technological ob | 21 % | 14 % | 9.5 | — |
| EF05 OA 09 | 2 | Modelar control y decisión motriz · Higiene, postura, hidrat | 21 % | 12 % | 18.7 | — |
| LE05 OA 10 | 5 | Producir una respuesta propia · Uso autónomo y responsable d | 21 % | 33 % | 13.8 | — |
| EN05 OA 14 | 4 | Interact or compose with support · Writing for the functions | 21 % | 0 % | 19.2 | — |
| MA05 OA 18 | 1 | Representar y precisar el sentido · Congruencia mediante tra | 21 % | 20 % | 14.4 | — |
| MU05 OA 01 | 1 | Escuchar antes de nombrar · Musical language and expressive  | 21 % | 14 % | 14.8 | — |
| MU05 OA 05 | 2 | Reconocer y representar un rasgo audible · Improvisation and | 21 % | 12 % | 16.6 | — |
| EF05 OA 11 | 1 | Reconocer meta y condiciones de seguridad · Calentamiento, m | 22 % | 17 % | 13.7 | — |
| EN05 OA 14 | 5 | Communicate independently · Writing for the functions of the | 22 % | 0 % | 14.6 | — |
| LE05 OA 10 | 2 | Modelar una lectura o producción · Uso autónomo y responsabl | 22 % | 33 % | 16.2 | — |
| EN05 OA 03 | 4 | Interact or compose with support · Strategies for audiovisua | 22 % | 0 % | 15.2 | — |
| LE05 OA 04 | 1 | Reconocer propósito y desafío · Análisis profundo de narraci | 22 % | 17 % | 15.0 | — |
| LE05 OA 18 | 2 | Modelar una lectura o producción · Revisión y edición para c | 22 % | 17 % | 11.7 | — |
| LE05 OA 18 | 4 | Comparar interpretaciones o decisiones · Revisión y edición  | 22 % | 0 % | 9.6 | — |
| EN05 OA 07 | 2 | Locate words, chunks and clues · Purposeful reading strategi | 22 % | 14 % | 11.1 | — |
| EN05 OA 11 | 2 | Locate words, chunks and clues · Vocabulary for the function | 22 % | 14 % | 15.6 | — |
| LE05 OA 18 | 1 | Reconocer propósito y desafío · Revisión y edición para comu | 22 % | 33 % | 13.8 | — |
| AR05 OA 03 | 5 | Interpretar y fundamentar · Dominio de materiales, herramien | 23 % | 43 % | 14.4 | — |
| MU05 OA 03 | 3 | Interpretar o crear con un criterio · Abundant listening acr | 23 % | 22 % | 18.3 | — |
| EN05 OA 05 | 2 | Locate words, chunks and clues · Reading literary and non-li | 23 % | 0 % | 12.1 | — |
| EN05 OA 06 | 2 | Locate words, chunks and clues · Reading communicative funct | 23 % | 0 % | 31.0 | — |
| EN05 OA 13 | 4 | Interact or compose with support · Model-supported literary  | 23 % | 14 % | 11.7 | — |
| LE05 OA 03 | 2 | Modelar una lectura o producción · Repertorio literario y va | 23 % | 14 % | 12.5 | — |
| LE05 OA 29 | 2 | Modelar una lectura o producción · Vocabulario nuevo en inte | 23 % | 14 % | 14.2 | — |
| MA05 OA 20 | 4 | Resolver un caso con una condición nueva · Conversión de uni | 23 % | 33 % | 16.8 | — |
| MU05 OA 06 | 2 | Reconocer y representar un rasgo audible · Responsible and m | 23 % | 29 % | 14.3 | — |
| EN05 OA 08 | 5 | Communicate independently · Multimodal response to reading | 23 % | 20 % | 9.8 | — |
| EN05 OA 03 | 2 | Locate words, chunks and clues · Strategies for audiovisual  | 24 % | 14 % | 13.0 | — |
| EN05 OA 11 | 3 | Model a communicative strategy · Vocabulary for the function | 24 % | 0 % | 17.7 | — |
| LE05 OA 13 | 3 | Localizar y seleccionar evidencia · Escritura frecuente con  | 24 % | 17 % | 16.1 | — |
| EN05 OA 07 | 3 | Model a communicative strategy · Purposeful reading strategi | 24 % | 0 % | 13.2 | — |
| TE05 OA 02 | 2 | Representar una solución · Planning with resources, safety a | 24 % | 0 % | 13.9 | — |
| OR05 OA 09 | 1 | Examinar un caso ficticio protegido · Perseverance, honest s | 24 % | 12 % | 11.1 | — |
| EN05 OA 15 | 5 | Communicate independently · Writing process with digital and | 24 % | 0 % | 13.5 | — |
| LE05 OA 04 | 2 | Modelar una lectura o producción · Análisis profundo de narr | 24 % | 0 % | 14.2 | — |
| LE05 OA 04 | 3 | Localizar y seleccionar evidencia · Análisis profundo de nar | 24 % | 17 % | 14.6 | — |
| EN05 OA 02 | 2 | Locate words, chunks and clues · Listening for purpose, idea | 24 % | 11 % | 9.7 | — |
| MU05 OA 03 | 2 | Reconocer y representar un rasgo audible · Abundant listenin | 24 % | 30 % | 16.4 | — |
| EF05 OA 08 | 2 | Modelar control y decisión motriz · Pulso y percepción de in | 25 % | 29 % | 12.2 | — |
| EN05 OA 04 | 3 | Model a communicative strategy · Response and connection aft | 25 % | 14 % | 12.2 | — |
| EN05 OA 10 | 1 | Notice purpose and context · Supported oral communication | 25 % | 0 % | 15.7 | — |
| EN05 OA 14 | 2 | Locate words, chunks and clues · Writing for the functions o | 25 % | 0 % | 13.2 | — |
| LC05 OA 17 | 2 | Escuchar o leer con límites declarados · Manifestaciones art | 25 % | 29 % | 17.4 | — |
| LE05 OA 02 | 3 | Localizar y seleccionar evidencia · Estrategias conscientes  | 25 % | 17 % | 15.9 | — |
| LE05 OA 08 | 3 | Localizar y seleccionar evidencia · Síntesis y registro de i | 25 % | 29 % | 15.6 | — |
| LE05 OA 27 | 2 | Modelar una lectura o producción · Convenciones sociales y r | 25 % | 17 % | 15.9 | — |
| MU05 OA 01 | 3 | Interpretar o crear con un criterio · Musical language and e | 25 % | 14 % | 13.7 | — |
| MU05 OA 05 | 3 | Interpretar o crear con un criterio · Improvisation and crea | 25 % | 29 % | 13.1 | — |
| OR05 OA 08 | 4 | Elegir una acción segura · Democratic participation and cour | 25 % | 0 % | 15.3 | — |
| TE05 OA 01 | 6 | Mejorar y comunicar · Design of technological objects and sy | 25 % | 33 % | 12.1 | — |
| TE05 OA 05 | 4 | Elaborar o configurar · Presentations and spreadsheets for c | 25 % | 0 % | 13.1 | — |
| EN05 OA 05 | 3 | Model a communicative strategy · Reading literary and non-li | 26 % | 17 % | 14.9 | — |
| LE05 OA 04 | 4 | Comparar interpretaciones o decisiones · Análisis profundo d | 26 % | 33 % | 15.6 | — |
| LE05 OA 24 | 3 | Localizar y seleccionar evidencia · Comprensión y contraste  | 26 % | 43 % | 11.0 | — |
| EN05 OA 04 | 5 | Communicate independently · Response and connection after li | 26 % | 17 % | 13.2 | — |
| EN05 OA 08 | 3 | Model a communicative strategy · Multimodal response to read | 26 % | 33 % | 18.1 | — |
| EF05 OA 04 | 3 | Ensayar con variantes accesibles · Actividad física y cuidad | 26 % | 25 % | 14.2 | — |
| EN05 OA 01 | 1 | Notice purpose and context · Listening comprehension across  | 26 % | 22 % | 11.2 | — |
| EN05 OA 01 | 4 | Interact or compose with support · Listening comprehension a | 26 % | 0 % | 11.8 | — |
| EN05 OA 13 | 1 | Notice purpose and context · Model-supported literary and fu | 26 % | 12 % | 11.2 | — |
| TE05 OA 01 | 2 | Representar una solución · Design of technological objects a | 26 % | 17 % | 13.2 | — |
| EF05 OA 03 | 2 | Modelar control y decisión motriz · Estrategias ofensivas y  | 26 % | 29 % | 18.8 | — |
| EN05 OA 09 | 2 | Locate words, chunks and clues · English sounds through oral | 26 % | 0 % | 10.1 | — |
| EN05 OA 02 | 1 | Notice purpose and context · Listening for purpose, ideas an | 26 % | 29 % | 14.8 | — |
| EN05 OA 06 | 4 | Interact or compose with support · Reading communicative fun | 26 % | 14 % | 14.4 | — |
| LE05 OA 01 | 3 | Localizar y seleccionar evidencia · Fluidez, precisión y pro | 26 % | 17 % | 12.8 | — |
| LE05 OA 01 | 4 | Comparar interpretaciones o decisiones · Fluidez, precisión  | 26 % | 33 % | 14.9 | — |
| MA05 OA 22 | 2 | Conectar dos representaciones · Áreas de triángulos, paralel | 26 % | 33 % | 13.3 | — |
| EN05 OA 10 | 3 | Model a communicative strategy · Supported oral communicatio | 27 % | 0 % | 15.3 | — |
| EN05 OA 10 | 4 | Interact or compose with support · Supported oral communicat | 27 % | 25 % | 13.3 | — |
| LE05 OA 06 | 3 | Localizar y seleccionar evidencia · Comprensión crítica de t | 27 % | 29 % | 17.6 | — |
| TE05 OA 02 | 1 | Definir necesidad, usuario y criterio · Planning with resour | 27 % | 12 % | 12.8 | — |
| LE05 OA 18 | 5 | Producir una respuesta propia · Revisión y edición para comu | 27 % | 33 % | 10.1 | — |
| EN05 OA 07 | 4 | Interact or compose with support · Purposeful reading strate | 27 % | 0 % | 12.6 | — |
| MA05 OA 01 | 3 | Elegir y justificar una estrategia · Números naturales hasta | 27 % | 33 % | 12.0 | — |
| MA05 OA 01 | 4 | Resolver un caso con una condición nueva · Números naturales | 27 % | 33 % | 11.2 | — |
| AR05 OA 03 | 4 | Crear una respuesta propia · Dominio de materiales, herramie | 27 % | 25 % | 15.0 | — |
| EF05 OA 01 | 2 | Modelar control y decisión motriz · Habilidades motrices apl | 27 % | 12 % | 14.0 | — |
| EF05 OA 01 | 4 | Resolver una situación nueva · Habilidades motrices aplicada | 27 % | 12 % | 16.4 | — |
| LE05 OA 09 | 2 | Modelar una lectura o producción · Lectura habitual y elecci | 27 % | 33 % | 13.2 | — |
| LE05 OA 22 | 3 | Localizar y seleccionar evidencia · Ortografía al servicio d | 27 % | 17 % | 12.6 | — |
| LE05 OA 22 | 4 | Comparar interpretaciones o decisiones · Ortografía al servi | 27 % | 0 % | 17.2 | — |
| EN05 OA 12 | 3 | Model a communicative strategy · Dialogues about ability, qu | 27 % | 25 % | 15.2 | — |
| EN05 OA 02 | 4 | Interact or compose with support · Listening for purpose, id | 28 % | 0 % | 11.6 | — |
| EF05 OA 11 | 2 | Modelar control y decisión motriz · Calentamiento, materiale | 28 % | 12 % | 14.3 | — |
| MA05 OA 01 | 1 | Representar y precisar el sentido · Números naturales hasta  | 28 % | 33 % | 14.1 | — |
| OR05 OA 03 | 1 | Examinar un caso ficticio protegido · Affective and sexual d | 28 % | 25 % | 17.8 | — |
| TE05 OA 04 | 3 | Planificar recursos y seguridad · Testing quality through te | 28 % | 22 % | 13.7 | — |
| EN05 OA 03 | 5 | Communicate independently · Strategies for audiovisual liste | 28 % | 0 % | 13.6 | — |
| LE05 OA 02 | 5 | Producir una respuesta propia · Estrategias conscientes de c | 29 % | 0 % | 13.9 | — |
| LE05 OA 23 | 3 | Localizar y seleccionar evidencia · Escucha literaria de obr | 29 % | 14 % | 20.0 | — |
| LE05 OA 26 | 3 | Localizar y seleccionar evidencia · Diálogo para desarrollar | 29 % | 29 % | 13.5 | — |
| MA05 OA 04 | 1 | Representar y precisar el sentido · División de tres dígitos | 29 % | 20 % | 14.2 | — |
| MU05 OA 01 | 5 | Comunicar una decisión musical · Musical language and expres | 29 % | 33 % | 12.6 | — |
| MU05 OA 08 | 3 | Interpretar o crear con un criterio · Reflection and improve | 29 % | 0 % | 11.6 | — |
| EN05 OA 12 | 4 | Interact or compose with support · Dialogues about ability,  | 29 % | 12 % | 17.6 | — |
| HI05 OA 16 | 5 | Argumentar con evidencia · Actitudes cívicas en la vida coti | 29 % | 40 % | 14.9 | — |
| LE05 OA 14 | 2 | Modelar una lectura o producción · Narraciones con trama, de | 29 % | 29 % | 18.3 | — |
| LE05 OA 14 | 3 | Localizar y seleccionar evidencia · Narraciones con trama, d | 29 % | 29 % | 14.3 | — |
| EN05 OA 15 | 3 | Model a communicative strategy · Writing process with digita | 29 % | 12 % | 12.0 | — |
| EN05 OA 10 | 2 | Locate words, chunks and clues · Supported oral communicatio | 29 % | 17 % | 10.7 | — |
| EN05 OA 11 | 1 | Notice purpose and context · Vocabulary for the functions of | 29 % | 33 % | 17.2 | — |
| MA05 OA 02 | 1 | Representar y precisar el sentido · Estrategias de cálculo m | 29 % | 43 % | 14.5 | — |
| MA05 OA 02 | 4 | Resolver un caso con una condición nueva · Estrategias de cá | 29 % | 43 % | 14.7 | — |
| EF05 OA 04 | 1 | Reconocer meta y condiciones de seguridad · Actividad física | 30 % | 38 % | 15.2 | — |
| LE05 OA 02 | 1 | Reconocer propósito y desafío · Estrategias conscientes de c | 30 % | 17 % | 12.9 | — |
| EN05 OA 06 | 3 | Model a communicative strategy · Reading communicative funct | 30 % | 17 % | 15.6 | — |
| EF05 OA 05 | 4 | Resolver una situación nueva · Danzas nacionales con context | 30 % | 29 % | 14.4 | — |
| MA05 OA 19 | 2 | Conectar dos representaciones · Medición de longitudes en m, | 30 % | 25 % | 12.4 | — |
| TE05 OA 05 | 3 | Planificar recursos y seguridad · Presentations and spreadsh | 30 % | 0 % | 11.7 | — |
| EF05 OA 09 | 3 | Ensayar con variantes accesibles · Higiene, postura, hidrata | 30 % | 0 % | 14.3 | — |
| EN05 OA 05 | 1 | Notice purpose and context · Reading literary and non-litera | 30 % | 17 % | 11.6 | — |
| EN05 OA 05 | 5 | Communicate independently · Reading literary and non-literar | 30 % | 20 % | 12.6 | — |
| LE05 OA 10 | 3 | Localizar y seleccionar evidencia · Uso autónomo y responsab | 30 % | 33 % | 12.8 | — |
| LE05 OA 29 | 3 | Localizar y seleccionar evidencia · Vocabulario nuevo en int | 31 % | 29 % | 11.6 | — |
| MA05 OA 04 | 2 | Conectar dos representaciones · División de tres dígitos por | 31 % | 25 % | 13.2 | — |
| TE05 OA 06 | 3 | Planificar recursos y seguridad · Word processing for purpos | 31 % | 17 % | 13.9 | — |
| HI05 OA 12 | 2 | Interrogar fuentes y reconocer procedencia · Riesgos natural | 31 % | 38 % | 12.4 | — |
| TE05 OA 02 | 5 | Probar con evidencia · Planning with resources, safety and i | 31 % | 17 % | 11.5 | — |
| TE05 OA 05 | 5 | Probar con evidencia · Presentations and spreadsheets for co | 31 % | 17 % | 14.2 | — |
| LE05 OA 06 | 5 | Producir una respuesta propia · Comprensión crítica de texto | 31 % | 29 % | 12.5 | — |
| EN05 OA 03 | 3 | Model a communicative strategy · Strategies for audiovisual  | 31 % | 0 % | 12.7 | — |
| LE05 OA 16 | 3 | Localizar y seleccionar evidencia · Comentarios lectores fun | 31 % | 33 % | 15.1 | — |
| MA05 OA 02 | 3 | Elegir y justificar una estrategia · Estrategias de cálculo  | 31 % | 33 % | 17.6 | — |
| TE05 OA 03 | 4 | Elaborar o configurar · Safe elaboration with tools and mate | 31 % | 25 % | 11.7 | — |
| LE05 OA 28 | 2 | Modelar una lectura o producción · Exposición oral clara y f | 31 % | 33 % | 12.7 | — |
| LE05 OA 05 | 2 | Modelar una lectura o producción · Imágenes, figuras y forma | 31 % | 33 % | 11.4 | — |
| AR05 OA 04 | 2 | Explorar una variable visual · Interpretación de obras y dis | 32 % | 43 % | 13.3 | — |
| LE05 OA 24 | 6 | Revisar con retroalimentación · Comprensión y contraste de t | 32 % | 33 % | 12.5 | — |
| LE05 OA 25 | 2 | Modelar una lectura o producción · Apreciación de teatro y l | 32 % | 14 % | 19.4 | — |
| LE05 OA 25 | 3 | Localizar y seleccionar evidencia · Apreciación de teatro y  | 32 % | 29 % | 13.6 | — |
| MA05 OA 03 | 1 | Representar y precisar el sentido · Multiplicación de dos dí | 32 % | 40 % | 12.6 | — |
| MU05 OA 04 | 1 | Escuchar antes de nombrar · Singing and instrumental ensembl | 32 % | 29 % | 16.4 | — |
| OR05 OA 09 | 2 | Distinguir hechos, emociones y límites · Perseverance, hones | 32 % | 44 % | 13.5 | — |
| TE05 OA 07 | 2 | Representar una solución · Online communication, source safe | 32 % | 14 % | 10.9 | — |
| OR05 OA 04 | 1 | Examinar un caso ficticio protegido · Autonomous self-care,  | 32 % | 29 % | 13.8 | — |
| EN05 OA 09 | 1 | Notice purpose and context · English sounds through oral tex | 32 % | 0 % | 14.2 | — |
| HI05 OA 18 | 2 | Interrogar fuentes y reconocer procedencia · Proyecto escola | 32 % | 43 % | 11.5 | — |
| LE05 OA 22 | 2 | Modelar una lectura o producción · Ortografía al servicio de | 32 % | 17 % | 11.5 | — |
| MU05 OA 02 | 1 | Escuchar antes de nombrar · Elaborated response to musical e | 32 % | 43 % | 14.7 | — |
| EF05 OA 06 | 2 | Modelar control y decisión motriz · Condición física y metas | 32 % | 33 % | 11.9 | — |
| TE05 OA 04 | 2 | Representar una solución · Testing quality through technical | 32 % | 12 % | 16.2 | — |
| TE05 OA 04 | 4 | Elaborar o configurar · Testing quality through technical an | 32 % | 12 % | 14.9 | — |
| EF05 OA 10 | 3 | Ensayar con variantes accesibles · Responsabilidad, liderazg | 32 % | 29 % | 15.4 | — |
| MU05 OA 03 | 4 | Ensayar y ajustar desde la escucha · Abundant listening acro | 33 % | 33 % | 18.8 | — |
| EF05 OA 02 | 2 | Modelar control y decisión motriz · Tácticas para resolver p | 33 % | 38 % | 16.6 | — |
| EF05 OA 05 | 2 | Modelar control y decisión motriz · Danzas nacionales con co | 33 % | 38 % | 14.3 | — |
| EF05 OA 07 | 3 | Ensayar con variantes accesibles · Planificación regular de  | 33 % | 43 % | 13.8 | — |
| EF05 OA 11 | 3 | Ensayar con variantes accesibles · Calentamiento, materiales | 33 % | 29 % | 13.4 | — |
| EN05 OA 09 | 5 | Communicate independently · English sounds through oral text | 33 % | 0 % | 14.5 | — |
| EN05 OA 15 | 4 | Interact or compose with support · Writing process with digi | 33 % | 25 % | 13.6 | — |
| LE05 OA 11 | 4 | Comparar interpretaciones o decisiones · Búsqueda y selecció | 33 % | 33 % | 11.7 | — |
| LE05 OA 19 | 3 | Localizar y seleccionar evidencia · Vocabulario nuevo en la  | 33 % | 33 % | 10.8 | — |
| LE05 OA 23 | 4 | Comparar interpretaciones o decisiones · Escucha literaria d | 33 % | 43 % | 11.8 | — |
| LE05 OA 24 | 2 | Modelar una lectura o producción · Comprensión y contraste d | 33 % | 29 % | 11.1 | — |
| MA05 OA 10 | 3 | Elegir y justificar una estrategia · Equivalencia entre frac | 33 % | 33 % | 13.0 | — |
| MA05 OA 15 | 1 | Representar y precisar el sentido · Ecuaciones e inecuacione | 33 % | 40 % | 13.3 | — |
| MU05 OA 05 | 5 | Comunicar una decisión musical · Improvisation and creation  | 33 % | 33 % | 17.7 | — |
| OR05 OA 01 | 4 | Elegir una acción segura · Positive self-appraisal, strength | 33 % | 43 % | 11.8 | — |
| OR05 OA 02 | 1 | Examinar un caso ficticio protegido · Emotions, expression a | 33 % | 14 % | 13.2 | — |
| OR05 OA 08 | 5 | Practicar comunicación o solicitud de ayuda · Democratic par | 33 % | 38 % | 14.5 | — |
| TE05 OA 02 | 3 | Planificar recursos y seguridad · Planning with resources, s | 33 % | 14 % | 10.5 | — |
| TE05 OA 06 | 2 | Representar una solución · Word processing for purposeful do | 33 % | 20 % | 12.8 | — |
| LE05 OA 05 | 3 | Localizar y seleccionar evidencia · Imágenes, figuras y form | 37 % | 50 % | 22.1 | — |
| LC05 OA LS06 | 1 | Situar pueblo, territorio y fuente · Registro tecnológico co | 46 % | 62 % | 21.2 | — |
| HI05 OA 22 | 2 | Interrogar fuentes y reconocer procedencia · Información y o | 47 % | 75 % | 12.1 | respuesta «depende» en ejercicio cerrado |
| MA05 OA 16 | 4 | Resolver un caso con una condición nueva · Coordenadas en el | 50 % | 50 % | 21.2 | — |
| MU05 OA 07 | 4 | Ensayar y ajustar desde la escucha · Music and the context i | 54 % | 29 % | 24.9 | — |
| LC05 OA LS04 | 4 | Construir una respuesta atribuida · Mensajes con expresiones | 55 % | 57 % | 20.6 | — |
| CN05 OA 10 | 2 | Formular una pregunta o predicción comprobable · Conductores | 57 % | 88 % | 19.0 | respuesta «depende» en ejercicio cerrado |
| LC05 OA 14 | 4 | Construir una respuesta atribuida · Técnicas productivas y e | 58 % | 57 % | 21.1 | — |
| CN05 OA 10 | 5 | Explicar con evidencia y límites · Conductores, aisladores y | 59 % | 100 % | 14.1 | respuesta «depende» en ejercicio cerrado |
| LC05 OA 11 | 4 | Construir una respuesta atribuida · Personas portadoras de s | 62 % | 86 % | 21.3 | — |
| CN05 OA 11 | 4 | Comparar resultados con un criterio común · Uso responsable  | 71 % | 86 % | 15.7 | respuesta «depende» en ejercicio cerrado |
| HI05 OA 13 | 1 | Ubicar en tiempo y espacio · Personas como sujetos de derech | 84 % | 50 % | 14.6 | respuesta «depende» en ejercicio cerrado |
| HI05 OA 15 | 1 | Ubicar en tiempo y espacio · Esfuerzo, mérito y reconocimien | 85 % | 62 % | 17.3 | respuesta «depende» en ejercicio cerrado |
| CN05 OA 14 | 1 | Observar y separar evidencia de interpretación · Actividad h | 86 % | 100 % | 21.9 | — |
| MA05 OA 25 | 3 | Elegir y justificar una estrategia · Comparación cualitativa | 89 % | 83 % | 21.5 | — |
| LC05 OA LS03 | 1 | Situar pueblo, territorio y fuente · Textos del territorio y | 90 % | 86 % | 20.2 | — |
| LC05 OA LS05 | 3 | Reconocer relaciones culturales · Lengua, comunidad e identi | 92 % | 83 % | 20.1 | — |
