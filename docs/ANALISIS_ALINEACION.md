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
| tecnologia | 35 | 46 % | 2 |

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

## 6.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 27 | 46 % | 4 |
| ciencias-naturales | 78 | 60 % | 9 |
| educacion-fisica-salud | 50 | 44 % | 18 |
| historia-geografia-ciencias-sociales | 116 | 56 % | 14 |
| ingles-propuesta | 74 | 31 % | 49 |
| lengua-cultura-pueblos-originarios-ancestrales | 144 | 61 % | 10 |
| lenguaje-comunicacion | 176 | 46 % | 48 |
| matematica | 98 | 40 % | 33 |
| musica | 35 | 45 % | 19 |
| orientacion | 41 | 42 % | 15 |
| tecnologia | 37 | 39 % | 12 |

**Clases marcadas para lectura prioritaria (6.º básico):** 231 de 876.

### Segunda lectura crítica de las 876 clases

Cada una de las 876 clases de 6.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios.

| Asignatura | Clases | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 98 | Seis ejercicios idénticos al ejemplo resuelto o a la caja de errores frecuentes; «cuántos ángulos iguales» falso con rectas perpendiculares; «complemento» usado para 180° contra complementario de 90° en otro OA; «puerta contra la pared = 180°» no seguro; triángulo 2-2-3 con ángulo de 100° (97°); datos de ejemplo que daban dos modas o no decían cuántos sectores eran rojos; división de decimales por un decimal, que el OA nombra, agregada en OA 07; desigualdad triangular mal enunciada. |
| Lenguaje y Comunicación | 176 | Orden alfabético con ñ mal explicado (la ñ decide en la 5.ª letra); «5 comas» en un texto de 3; «irrompible» como «i- + rompible» (es ir-); «afable es lo contrario de tímido»; «previsible» con «-ble»; «pinta» por escondida; actividades abiertas que citaban un cuento que solo estaba en otros ejercicios (OA 16); figuras literarias dudosas (hipérbole, onomatopeya); aritmética escrita como texto pasada a cálculo verificado; fogata «con ayuda de su papá» cambiada por amasar pan. |
| Ciencias Naturales | 78 | «Un ovario libera un óvulo por ciclo» precisado; recorrido masculino contado con 5 estructuras (enseña 4); energía del carnívoro invertida; «gas invisible porque sus partículas son transparentes»; hielo derretido 8 veces por debajo de lo plausible; orden de estados por separación de partículas falso para el agua; «ilegales» para marihuana y cocaína; «las mareas no dependen del Sol»; sublimación inversa y desertificación usadas sin enseñarlas. |
| Historia, Geografía y Ciencias Sociales | 116 | Pisagua ubicada al sur de Iquique; «dos de los tres patrimonios tienen reconocimiento UNESCO» (uno); «en el altiplano casi no llueve»; una misma persona diputada y concejala a la vez; tribunal que revisa «una ley muy injusta»; fuentes «resumen» usadas como primarias; perspectiva mapuche inventada rotulada de modo que parecía testimonio real; «zonas poco ocupadas» sin mencionar a los pueblos que vivían allí; ser tricontinental como «rasgo único»; soberanía y recurso usados sin definir; relieve agregado en OA 11. |
| Inglés | 74 | Cinco palabras con /r/ y no cuatro; adivinanza con 3 pistas y no 2; «fifty hundred»; «eat bread and tea»; «Penguins live in cold places» (hay pingüinos en Chile); estructuras usadas antes de enseñarse (went, ate, saw, easier, fewer, so); módulo de OA 11 y 12 sobrescrito por error y reescrito; piscina con el lunes sin decir; ejercicios aritméticos sin valor reemplazados. |
| Lengua y Cultura de los Pueblos Originarios | 144 | «Dos de los tres patrimonios» con UNESCO; «colonos en 1900» cuando la memoria decía «antes de 1900»; 328 ejercicios A/B con la A siempre correcta, 168 reordenados; «chocolate (náhuatl)» (etimología discutida) cambiado por «chicle»; «marimari» presentado como error de «mari mari»; ciclo lunar de 29 días como dato; ficha con permiso contradicha por un ejercicio; supuestos sobre la familia («tu abuela», «tu pulsera»); aritmética trivial. |
| Educación Física y Salud | 50 | Pausa activa «cada 45 min en 180» que daba 4 y son 3; dos toallas de 6 cm contra la regla de 10 cm; pausas de bebida cada 15–20 min contra ejercicios de 30; material insuficiente (3 vasos para 6 piezas, «no se usa ningún material» con pelota); supuestos sobre la familia; peso corporal: balanza y «pesa tu peso» retirados. |
| Orientación | 41 | Orden de los pasos ante grooming contradictorio entre ejercicios (decir no, guardar pruebas, bloquear, contar); testigo que confrontaba al agresor; recibir una foto íntima sin indicar no reenviarla; encuentros con desconocidos en línea; «lo íntimo se cuenta solo si uno quiere» que podía leerse como fomento del secreto; «una ofensa repetida es discriminación» (es hostigamiento); «hibernan los osos» (Chile no tiene osos). |
| Música | 35 | Melodía que rompía dos reglas con pregunta de una; 2/4 con dos respuestas válidas; «la lenta» para 80 pulsos contradiciendo los rangos de la clase; accelerando calculado a tempo fijo; ficha de orquesta sin compositor clasificada como tradición escrita; «tu abuela canta»; aritmética trivial recalculada por el verificador. |
| Artes Visuales | 27 | Oscurecer con «azul oscuro»; mural de Siqueiros clasificado como espacio público (está en un interior escolar); interpretación de «Las dos Fridas» con causalidad sin lógica; aguja de bordado sin punta roma; ejercicios cerrados sin opciones; sumas de puntos antes de enseñarse. |
| Tecnología | 37 | «Cuánto sobra» sin dar el largo del material; rango en mm sin tolerancia; regla «mejorar el criterio con menos puntos» contra «la seguridad va primero»; «tela de papel»; «algunas familias no pueden pagar»; frase con coma extra que daba tres errores y no dos; plagio y derechos de autor sin matiz. |

#### Desajuste entre el texto del OA y los títulos de las clases

Como en 5.º, los títulos de clase del plan son etapas genéricas («Reconocer propósito y desafío», «Situar pueblo, territorio y fuente», «Ubicar en tiempo y espacio»…), repetidas en todos los OA de la asignatura. Los autores repartieron el contenido del OA entre las clases y los lectores comprobaron que lo enseñado calza con el OA. En Matemática, además, el insumo y la consigna de cada clase son una plantilla que no corresponde al OA (por ejemplo «Tarjetas numéricas 29, 145, 147» en teselados), por lo que se ignoraron. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Matemática (división de decimales por un decimal, OA 07); Historia (relieve de las cuatro regiones representativas, OA 11); Inglés (sonido /r/ en OA 02).
- **Abiertos:** software geométrico, educativo y de presentación (Matemática OA 03, 04, 05, 12, 15, 20 y 23; Tecnología OA 05, 06 y 07); audio, video y formato audiovisual (Inglés, Lenguaje OA 26, Música); lectura en voz alta y fluidez real (Lenguaje OA 01); obras completas, plan lector y relatos históricos reales (Lenguaje OA 03, 04, 06 y 23); las 50 obras al año (Artes OA 04, el cuaderno describe unas 10 con texto) e imágenes; práctica de herramientas de taller (Tecnología OA 03); producción en lengua indígena, lenguajes artísticos propios del pueblo y lengua y relatos reales (Lengua y Cultura, con educador o educadora tradicional); pruebas de 50 y 100 m y danzas del norte, sur e Isla de Pascua (Educación Física); investigación experimental real (Ciencias OA 01, 09 y 13); elección de curso y voluntariado reales (Historia OA 22 y 23); biblioteca, buscador e internet reales (Lenguaje OA 09 a 12).
- **Decisiones que dependen del programa oficial:** definición de isósceles como «exactamente dos lados iguales», ángulos suplementarios, umbrales de «pocas» y «muchas» repeticiones, 100 °C como punto de ebullición sin ajuste por altura, y las convenciones propias del cuaderno (rangos de tempo, escala de esfuerzo 0 a 10, regla de palabras desconocidas por cada 100).

### Clases marcadas de 6.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| TE06 OA 02 | 3 | Planificar recursos y seguridad · Planificar la elaboración  | 9 % | 15 % | 15.9 | — |
| LE06 OA 20 | 4 | Comparar interpretaciones o decisiones · Ampliar su capacida | 12 % | 18 % | 13.8 | — |
| TE06 OA 01 | 5 | Probar con evidencia · Diseños de objetos y sistemas tecnoló | 12 % | 30 % | 12.9 | — |
| TE06 OA 02 | 2 | Representar una solución · Planificar la elaboración de obje | 12 % | 21 % | 15.4 | — |
| MA06 OA 04 | 2 | Conectar representaciones y lenguaje matemático · Porcentaje | 13 % | 33 % | 16.4 | — |
| EN06 OA 14 | 1 | Notice purpose and context · Escribir para realizar las sigu | 14 % | 29 % | 20.3 | — |
| LE06 OA 30 | 2 | Modelar una lectura o producción · Incorporar de manera pert | 15 % | 15 % | 15.0 | — |
| MA06 OA 03 | 1 | Representar y precisar el concepto · Razones entre cantidade | 15 % | 40 % | 13.0 | — |
| EN06 OA 09 | 2 | Locate key words and clues · Reproducir y producir textos or | 16 % | 7 % | 15.2 | — |
| EN06 OA 12 | 1 | Notice purpose and context · Participar en diálogos con pare | 16 % | 20 % | 12.4 | — |
| EN06 OA 06 | 2 | Locate key words and clues · Leer y demostrar comprensión de | 16 % | 17 % | 14.0 | — |
| EF06 OA 08 | 2 | Modelar control y decisión motriz · Determinar la intensidad | 17 % | 17 % | 14.5 | — |
| EN06 OA 01 | 2 | Locate key words and clues · Demostrar comprensión de textos | 17 % | 15 % | 13.4 | — |
| EN06 OA 01 | 3 | Model a communicative strategy · Demostrar comprensión de te | 17 % | 15 % | 9.8 | — |
| MU06 OA 06 | 2 | Reconocer un rasgo audible · Presentar su trabajo musical al | 17 % | 17 % | 19.0 | — |
| EN06 OA 08 | 4 | Interact or compose with support · Reaccionar y demostrar in | 17 % | 7 % | 10.4 | — |
| EF06 OA 06 | 3 | Ensayar con variantes accesibles · Ejecutar actividades físi | 17 % | 0 % | 14.5 | — |
| LE06 OA 29 | 4 | Comparar interpretaciones o decisiones · Expresarse de maner | 18 % | 10 % | 17.4 | — |
| MA06 OA 02 | 3 | Elegir, ejecutar y justificar una estrategia · Operaciones c | 18 % | 25 % | 13.5 | — |
| MA06 OA 23 | 2 | Conectar representaciones y lenguaje matemático · Tendencia  | 18 % | 14 % | 14.9 | — |
| LE06 OA 31 | 3 | Seleccionar evidencia o recursos · Textos orales espontáneos | 18 % | 9 % | 14.8 | — |
| MA06 OA 24 | 3 | Elegir, ejecutar y justificar una estrategia · Gráficos de b | 18 % | 25 % | 12.9 | — |
| OR06 OA 03 | 5 | Practicar comunicación o ayuda · Reconocer y valorar el proc | 18 % | 10 % | 14.8 | — |
| CN06 OA 17 | 3 | Modelar el sistema o fenómeno · Investigar experimentalmente | 19 % | 18 % | 17.2 | — |
| MA06 OA 07 | 3 | Elegir, ejecutar y justificar una estrategia · Multiplicació | 19 % | 29 % | 14.0 | — |
| EN06 OA 12 | 5 | Communicate independently · Participar en diálogos con pares | 19 % | 11 % | 21.8 | — |
| EN06 OA 06 | 5 | Communicate independently · Leer y demostrar comprensión de  | 19 % | 9 % | 15.8 | — |
| HI06 OA 04 | 6 | Evaluar una decisión ciudadana · Investigar sobre algunos as | 19 % | 36 % | 18.9 | — |
| TE06 OA 03 | 4 | Elaborar o configurar · Elaborar un producto tecnológico par | 19 % | 9 % | 13.8 | — |
| EF06 OA 07 | 2 | Modelar control y decisión motriz · Practicar y planificar d | 20 % | 23 % | 15.7 | — |
| EN06 OA 04 | 3 | Model a communicative strategy · Reaccionar y demostrar inte | 20 % | 27 % | 10.7 | — |
| MA06 OA 03 | 3 | Elegir, ejecutar y justificar una estrategia · Razones entre | 20 % | 33 % | 19.0 | — |
| MA06 OA 04 | 3 | Elegir, ejecutar y justificar una estrategia · Porcentajes c | 20 % | 33 % | 14.8 | — |
| MA06 OA 14 | 1 | Representar y precisar el concepto · Teselaciones mediante t | 20 % | 20 % | 16.7 | — |
| EN06 OA 08 | 5 | Communicate independently · Reaccionar y demostrar interés p | 21 % | 21 % | 8.0 | — |
| EN06 OA 01 | 4 | Interact or compose with support · Demostrar comprensión de  | 21 % | 23 % | 11.3 | — |
| EN06 OA 06 | 3 | Model a communicative strategy · Leer y demostrar comprensió | 21 % | 17 % | 19.5 | — |
| EN06 OA 10 | 2 | Locate key words and clues · Expresarse oralmente, ya sea en | 21 % | 23 % | 12.6 | — |
| MA06 OA 04 | 4 | Resolver un caso con una condición nueva · Porcentajes como  | 21 % | 40 % | 17.6 | — |
| MA06 OA 13 | 3 | Elegir, ejecutar y justificar una estrategia · Área en cubos | 21 % | 17 % | 21.0 | — |
| EF06 OA 02 | 2 | Modelar control y decisión motriz · Ejecutar juegos colectiv | 22 % | 21 % | 16.4 | — |
| MA06 OA 19 | 1 | Representar y precisar el concepto · Volumen de cubos y para | 22 % | 17 % | 14.8 | — |
| MU06 OA 01 | 2 | Reconocer un rasgo audible · Describir la música escuchada e | 22 % | 20 % | 17.9 | — |
| LE06 OA 22 | 5 | Producir una respuesta propia · Escribir correctamente para  | 23 % | 14 % | 16.2 | — |
| EN06 OA 05 | 3 | Model a communicative strategy · Leer y comprender textos li | 23 % | 33 % | 11.5 | — |
| LE06 OA 14 | 2 | Modelar una lectura o producción · Escribir creativamente na | 23 % | 27 % | 11.5 | — |
| MU06 OA 01 | 1 | Escuchar antes de nombrar · Describir la música escuchada e  | 23 % | 36 % | 21.4 | — |
| OR06 OA 02 | 1 | Examinar un caso ficticio protegido · Distinguir y describir | 23 % | 23 % | 12.7 | — |
| TE06 OA 06 | 3 | Planificar recursos y seguridad · Usar procesador de textos  | 23 % | 23 % | 14.8 | — |
| HI06 OA 04 | 3 | Relacionar actores, causas y consecuencias · Investigar sobr | 23 % | 42 % | 12.2 | — |
| LE06 OA 24 | 5 | Producir una respuesta propia · Textos orales (explicaciones | 23 % | 6 % | 12.8 | — |
| EN06 OA 08 | 2 | Locate key words and clues · Reaccionar y demostrar interés  | 23 % | 33 % | 12.1 | — |
| EN06 OA 08 | 3 | Model a communicative strategy · Reaccionar y demostrar inte | 23 % | 33 % | 12.8 | — |
| LE06 OA 22 | 4 | Comparar interpretaciones o decisiones · Escribir correctame | 23 % | 21 % | 14.9 | — |
| LE06 OA 20 | 3 | Seleccionar evidencia o recursos · Ampliar su capacidad expr | 24 % | 20 % | 18.0 | — |
| EN06 OA 06 | 1 | Notice purpose and context · Leer y demostrar comprensión de | 24 % | 27 % | 9.7 | — |
| LE06 OA 10 | 2 | Modelar una lectura o producción · Asistir habitualmente a l | 24 % | 29 % | 12.7 | — |
| EF06 OA 01 | 2 | Modelar control y decisión motriz · Demostrar la aplicación  | 24 % | 33 % | 16.1 | — |
| EN06 OA 12 | 3 | Model a communicative strategy · Participar en diálogos con  | 24 % | 20 % | 34.5 | — |
| TE06 OA 01 | 3 | Planificar recursos y seguridad · Diseños de objetos y siste | 24 % | 36 % | 15.7 | — |
| OR06 OA 09 | 1 | Examinar un caso ficticio protegido · Practicar en forma aut | 24 % | 25 % | 14.8 | — |
| EN06 OA 02 | 3 | Model a communicative strategy · Textos orales acerca de tem | 24 % | 20 % | 14.5 | — |
| EN06 OA 02 | 1 | Notice purpose and context · Textos orales acerca de temas v | 25 % | 14 % | 14.2 | — |
| LC06 OA LR02 | 4 | Construir una respuesta atribuida · Expresar oralmente el an | 25 % | 21 % | 16.8 | — |
| LE06 OA 19 | 2 | Modelar una lectura o producción · Incorporar de manera pert | 25 % | 25 % | 14.4 | — |
| LE06 OA 23 | 5 | Producir una respuesta propia · Y disfrutar versiones comple | 25 % | 36 % | 15.1 | — |
| MA06 OA 13 | 1 | Representar y precisar el concepto · Área en cubos y paralel | 25 % | 20 % | 16.6 | — |
| TE06 OA 03 | 2 | Representar una solución · Elaborar un producto tecnológico  | 25 % | 17 % | 14.2 | — |
| EN06 OA 05 | 5 | Communicate independently · Leer y comprender textos literar | 26 % | 21 % | 11.4 | — |
| EN06 OA 15 | 4 | Interact or compose with support · Utilizar los pasos del pr | 26 % | 19 % | 11.4 | — |
| LE06 OA 22 | 1 | Reconocer propósito y desafío · Escribir correctamente para  | 26 % | 29 % | 15.1 | — |
| LE06 OA 22 | 2 | Modelar una lectura o producción · Escribir correctamente pa | 26 % | 21 % | 11.2 | — |
| LE06 OA 22 | 3 | Seleccionar evidencia o recursos · Escribir correctamente pa | 26 % | 21 % | 15.6 | — |
| EF06 OA 06 | 4 | Resolver una situación nueva · Ejecutar actividades físicas  | 26 % | 15 % | 12.5 | — |
| LE06 OA 27 | 5 | Producir una respuesta propia · Dialogar para compartir y de | 26 % | 33 % | 17.6 | — |
| AR06 OA 01 | 6 | Revisar sin perder autoría · Trabajos de arte y diseños a pa | 26 % | 38 % | 14.5 | — |
| LE06 OA 01 | 3 | Seleccionar evidencia o recursos · Leer de manera fluida tex | 26 % | 29 % | 14.3 | — |
| EN06 OA 12 | 2 | Locate key words and clues · Participar en diálogos con pare | 27 % | 0 % | 51.0 | — |
| EN06 OA 12 | 4 | Interact or compose with support · Participar en diálogos co | 27 % | 10 % | 60.7 | — |
| MA06 OA 11 | 1 | Representar y precisar el concepto · Ecuaciones de primer gr | 27 % | 17 % | 13.3 | — |
| EF06 OA 09 | 2 | Modelar control y decisión motriz · Practicar actividades fí | 27 % | 14 % | 11.6 | — |
| MU06 OA 03 | 3 | Interpretar o crear con criterio · Escuchar música en forma  | 27 % | 27 % | 19.9 | — |
| MA06 OA 14 | 2 | Conectar representaciones y lenguaje matemático · Teselacion | 27 % | 17 % | 16.0 | — |
| MA06 OA 24 | 2 | Conectar representaciones y lenguaje matemático · Gráficos d | 27 % | 38 % | 18.0 | — |
| MU06 OA 05 | 2 | Reconocer un rasgo audible · Improvisar y crear ideas musica | 27 % | 27 % | 18.6 | — |
| MU06 OA 05 | 4 | Ensayar y ajustar desde la escucha · Improvisar y crear idea | 27 % | 27 % | 15.8 | — |
| EN06 OA 07 | 4 | Interact or compose with support · Usar estrategias para apo | 28 % | 38 % | 9.9 | — |
| LE06 OA 26 | 2 | Modelar una lectura o producción · Apreciar obras de teatro, | 28 % | 25 % | 11.9 | — |
| LE06 OA 26 | 5 | Producir una respuesta propia · Apreciar obras de teatro, pe | 28 % | 12 % | 15.5 | — |
| LE06 OA 29 | 2 | Modelar una lectura o producción · Expresarse de manera clar | 28 % | 9 % | 14.0 | — |
| TE06 OA 05 | 5 | Probar con evidencia · Usar software para organizar y comuni | 28 % | 9 % | 13.2 | — |
| HI06 OA 23 | 2 | Interrogar fuentes y procedencia · Participar, mediante acci | 28 % | 31 % | 10.8 | — |
| MA06 OA 09 | 1 | Representar y precisar el concepto · Relaciones en tablas | 28 % | 40 % | 17.7 | — |
| LE06 OA 06 | 2 | Modelar una lectura o producción · Leer independientemente y | 28 % | 47 % | 15.6 | — |
| EF06 OA 01 | 4 | Resolver una situación nueva · Demostrar la aplicación de la | 28 % | 8 % | 18.7 | — |
| AR06 OA 05 | 4 | Crear una respuesta propia · Evaluar críticamente trabajos d | 29 % | 20 % | 18.0 | — |
| EN06 OA 14 | 5 | Communicate independently · Escribir para realizar las sigui | 29 % | 33 % | 15.6 | — |
| HI06 OA 10 | 2 | Interrogar fuentes y procedencia · Identificar elementos con | 29 % | 29 % | 12.0 | — |
| LE06 OA 06 | 4 | Comparar interpretaciones o decisiones · Leer independientem | 29 % | 47 % | 16.5 | — |
| LE06 OA 24 | 6 | Revisar para una audiencia · Textos orales (explicaciones, i | 29 % | 13 % | 13.8 | — |
| LE06 OA 26 | 3 | Seleccionar evidencia o recursos · Apreciar obras de teatro, | 29 % | 25 % | 14.1 | — |
| MA06 OA 13 | 2 | Conectar representaciones y lenguaje matemático · Área en cu | 29 % | 0 % | 17.2 | — |
| MA06 OA 22 | 2 | Conectar representaciones y lenguaje matemático · Comparació | 29 % | 14 % | 19.0 | — |
| OR06 OA 04 | 1 | Examinar un caso ficticio protegido · Practicar en forma aut | 29 % | 14 % | 14.4 | — |
| OR06 OA 06 | 5 | Practicar comunicación o ayuda · Manifestar actitudes de sol | 29 % | 44 % | 19.1 | — |
| EF06 OA 11 | 3 | Ensayar con variantes accesibles · Practicar actividades fís | 29 % | 36 % | 17.3 | — |
| EN06 OA 05 | 4 | Interact or compose with support · Leer y comprender textos  | 29 % | 40 % | 12.2 | — |
| EN06 OA 13 | 2 | Locate key words and clues · Escribir de acuerdo a un modelo | 29 % | 36 % | 9.9 | — |
| EN06 OA 13 | 4 | Interact or compose with support · Escribir de acuerdo a un  | 29 % | 36 % | 12.0 | — |
| MU06 OA 03 | 2 | Reconocer un rasgo audible · Escuchar música en forma abunda | 29 % | 27 % | 20.1 | — |
| LE06 OA 18 | 4 | Comparar interpretaciones o decisiones · Escribir, revisar y | 29 % | 31 % | 9.8 | — |
| LE06 OA 29 | 1 | Reconocer propósito y desafío · Expresarse de manera clara y | 29 % | 27 % | 14.6 | — |
| LE06 OA 12 | 2 | Modelar una lectura o producción · Aplicar estrategias para  | 29 % | 33 % | 15.4 | — |
| MA06 OA 01 | 1 | Representar y precisar el concepto · Factores, múltiplos y n | 29 % | 43 % | 15.9 | — |
| MA06 OA 09 | 4 | Resolver un caso con una condición nueva · Relaciones en tab | 29 % | 40 % | 15.8 | — |
| EN06 OA 15 | 3 | Model a communicative strategy · Utilizar los pasos del proc | 30 % | 19 % | 10.4 | — |
| LC06 OA LS01 | 4 | Construir una respuesta atribuida · Disfrutar y comprender d | 30 % | 21 % | 13.4 | — |
| MU06 OA 03 | 1 | Escuchar antes de nombrar · Escuchar música en forma abundan | 30 % | 20 % | 21.8 | — |
| EN06 OA 14 | 4 | Interact or compose with support · Escribir para realizar la | 30 % | 14 % | 19.4 | — |
| CN06 OA 08 | 2 | Formular una pregunta o predicción · Que la energía es neces | 30 % | 42 % | 13.5 | — |
| EF06 OA 08 | 1 | Reconocer meta y seguridad · Determinar la intensidad del es | 30 % | 30 % | 13.7 | — |
| EN06 OA 04 | 1 | Notice purpose and context · Reaccionar y demostrar interés  | 30 % | 40 % | 18.6 | — |
| LE06 OA 23 | 2 | Modelar una lectura o producción · Y disfrutar versiones com | 30 % | 18 % | 12.1 | — |
| LE06 OA 23 | 3 | Seleccionar evidencia o recursos · Y disfrutar versiones com | 30 % | 18 % | 17.4 | — |
| MA06 OA 18 | 3 | Elegir, ejecutar y justificar una estrategia · Superficie de | 30 % | 14 % | 12.5 | — |
| MA06 OA 19 | 2 | Conectar representaciones y lenguaje matemático · Volumen de | 30 % | 29 % | 14.2 | — |
| MA06 OA 24 | 1 | Representar y precisar el concepto · Gráficos de barra doble | 30 % | 43 % | 16.8 | — |
| OR06 OA 04 | 2 | Distinguir hechos, emociones y límites · Practicar en forma  | 30 % | 11 % | 18.8 | — |
| TE06 OA 04 | 3 | Planificar recursos y seguridad · Probar y evaluar la calida | 30 % | 30 % | 19.6 | — |
| LE06 OA 24 | 3 | Seleccionar evidencia o recursos · Textos orales (explicacio | 30 % | 12 % | 12.6 | — |
| EN06 OA 03 | 4 | Interact or compose with support · Escuchar textos orales y  | 30 % | 18 % | 12.5 | — |
| LE06 OA 27 | 2 | Modelar una lectura o producción · Dialogar para compartir y | 30 % | 33 % | 15.6 | — |
| LE06 OA 04 | 5 | Producir una respuesta propia · Aspectos relevantes de las n | 31 % | 22 % | 14.9 | — |
| MA06 OA 22 | 4 | Resolver un caso con una condición nueva · Comparación de di | 31 % | 33 % | 18.4 | — |
| MU06 OA 01 | 4 | Ensayar y ajustar desde la escucha · Describir la música esc | 31 % | 29 % | 18.7 | — |
| MU06 OA 08 | 3 | Interpretar o crear con criterio · Reflexionar sobre sus for | 31 % | 11 % | 18.7 | — |
| OR06 OA 04 | 3 | Comparar opciones y consecuencias · Practicar en forma autón | 31 % | 38 % | 15.1 | respuesta «depende» en ejercicio cerrado |
| EN06 OA 06 | 4 | Interact or compose with support · Leer y demostrar comprens | 31 % | 17 % | 10.4 | — |
| EN06 OA 04 | 5 | Communicate independently · Reaccionar y demostrar interés p | 31 % | 36 % | 13.6 | — |
| EN06 OA 07 | 2 | Locate key words and clues · Usar estrategias para apoyar la | 31 % | 25 % | 12.8 | — |
| EN06 OA 05 | 2 | Locate key words and clues · Leer y comprender textos litera | 31 % | 47 % | 11.1 | — |
| EN06 OA 11 | 2 | Locate key words and clues · Demostrar conocimiento y uso de | 31 % | 38 % | 18.5 | — |
| EN06 OA 11 | 3 | Model a communicative strategy · Demostrar conocimiento y us | 31 % | 38 % | 12.3 | — |
| LE06 OA 13 | 2 | Modelar una lectura o producción · Escribir frecuentemente,  | 31 % | 36 % | 12.6 | — |
| MA06 OA 02 | 1 | Representar y precisar el concepto · Operaciones combinadas  | 31 % | 43 % | 15.2 | — |
| MA06 OA 08 | 1 | Representar y precisar el concepto · Problemas con fraccione | 31 % | 33 % | 10.9 | — |
| AR06 OA 04 | 2 | Explorar una variable visual · E interpretar obras de arte y | 32 % | 42 % | 14.4 | — |
| EF06 OA 04 | 4 | Resolver una situación nueva · Planificar y ejecutar activid | 32 % | 33 % | 18.4 | — |
| EN06 OA 09 | 4 | Interact or compose with support · Reproducir y producir tex | 32 % | 27 % | 11.9 | — |
| MU06 OA 02 | 4 | Ensayar y ajustar desde la escucha · Expresar, mostrando gra | 32 % | 43 % | 17.4 | — |
| OR06 OA 04 | 4 | Elegir una acción segura · Practicar en forma autónoma condu | 32 % | 25 % | 11.5 | — |
| LE06 OA 18 | 3 | Seleccionar evidencia o recursos · Escribir, revisar y edita | 32 % | 38 % | 11.9 | — |
| LE06 OA 18 | 5 | Producir una respuesta propia · Escribir, revisar y editar s | 32 % | 38 % | 15.0 | — |
| EF06 OA 11 | 1 | Reconocer meta y seguridad · Practicar actividades físicas y | 32 % | 42 % | 16.2 | — |
| EN06 OA 02 | 4 | Interact or compose with support · Textos orales acerca de t | 32 % | 21 % | 13.5 | — |
| EN06 OA 15 | 2 | Locate key words and clues · Utilizar los pasos del proceso  | 32 % | 31 % | 15.7 | — |
| HI06 OA 11 | 1 | Ubicar en tiempo y espacio · Caracterizar geográficamente la | 32 % | 40 % | 13.5 | — |
| LC06 OA LS03 | 5 | Contrastar sin jerarquizar · Textos orales y escritos propio | 32 % | 38 % | 16.8 | — |
| LE06 OA 06 | 5 | Producir una respuesta propia · Leer independientemente y co | 32 % | 47 % | 15.3 | — |
| LE06 OA 31 | 1 | Reconocer propósito y desafío · Textos orales espontáneos o  | 32 % | 45 % | 15.4 | — |
| OR06 OA 03 | 1 | Examinar un caso ficticio protegido · Reconocer y valorar el | 32 % | 30 % | 19.3 | — |
| OR06 OA 03 | 4 | Elegir una acción segura · Reconocer y valorar el proceso de | 32 % | 20 % | 16.2 | — |
| EF06 OA 09 | 3 | Ensayar con variantes accesibles · Practicar actividades fís | 32 % | 23 % | 21.4 | — |
| LE06 OA 04 | 4 | Comparar interpretaciones o decisiones · Aspectos relevantes | 32 % | 44 % | 17.1 | — |
| EN06 OA 07 | 5 | Communicate independently · Usar estrategias para apoyar la  | 32 % | 43 % | 10.5 | — |
| EN06 OA 03 | 3 | Model a communicative strategy · Escuchar textos orales y ap | 32 % | 27 % | 15.6 | — |
| HI06 OA 02 | 2 | Interrogar fuentes y procedencia · El desarrollo del proceso | 32 % | 25 % | 14.0 | — |
| OR06 OA 09 | 2 | Distinguir hechos, emociones y límites · Practicar en forma  | 32 % | 31 % | 13.1 | — |
| LE06 OA 24 | 2 | Modelar una lectura o producción · Textos orales (explicacio | 33 % | 25 % | 12.5 | — |
| MU06 OA 03 | 5 | Comunicar una decisión musical · Escuchar música en forma ab | 33 % | 30 % | 18.5 | — |
| LE06 OA 04 | 1 | Reconocer propósito y desafío · Aspectos relevantes de las n | 33 % | 33 % | 13.4 | — |
| LE06 OA 29 | 5 | Producir una respuesta propia · Expresarse de manera clara y | 33 % | 18 % | 15.1 | — |
| AR06 OA 04 | 5 | Interpretar y fundamentar · E interpretar obras de arte y ob | 33 % | 45 % | 12.8 | — |
| CN06 OA 03 | 3 | Modelar el sistema o fenómeno · Los efectos de la actividad  | 33 % | 38 % | 14.5 | — |
| CN06 OA 17 | 4 | Comparar resultados con un criterio · Investigar experimenta | 33 % | 45 % | 13.7 | — |
| EN06 OA 01 | 1 | Notice purpose and context · Demostrar comprensión de textos | 33 % | 38 % | 12.1 | — |
| EN06 OA 08 | 1 | Notice purpose and context · Reaccionar y demostrar interés  | 33 % | 33 % | 15.3 | — |
| EN06 OA 14 | 2 | Locate key words and clues · Escribir para realizar las sigu | 33 % | 14 % | 38.0 | — |
| EN06 OA 14 | 3 | Model a communicative strategy · Escribir para realizar las  | 33 % | 29 % | 28.6 | — |
| HI06 OA 03 | 4 | Comparar perspectivas o territorios · Describir algunos hito | 33 % | 36 % | 17.6 | — |
| HI06 OA 04 | 2 | Interrogar fuentes y procedencia · Investigar sobre algunos  | 33 % | 45 % | 16.6 | — |
| HI06 OA 06 | 2 | Interrogar fuentes y procedencia · Caracterizar los principa | 33 % | 38 % | 15.8 | — |
| HI06 OA 07 | 4 | Comparar perspectivas o territorios · Y dar ejemplos de la p | 33 % | 17 % | 16.2 | — |
| LC06 OA LR01 | 3 | Reconocer relaciones culturales · Disfrutar y comprender dif | 33 % | 23 % | 16.2 | — |
| LC06 OA LS02 | 2 | Escuchar o leer con límites declarados · Describir oralmente | 33 % | 43 % | 13.9 | — |
| LE06 OA 04 | 6 | Revisar para una audiencia · Aspectos relevantes de las narr | 33 % | 38 % | 18.5 | — |
| LE06 OA 19 | 4 | Comparar interpretaciones o decisiones · Incorporar de maner | 33 % | 33 % | 15.4 | — |
| LE06 OA 24 | 4 | Comparar interpretaciones o decisiones · Textos orales (expl | 33 % | 44 % | 11.9 | — |
| MA06 OA 15 | 3 | Elegir, ejecutar y justificar una estrategia · Construcción  | 33 % | 43 % | 13.9 | — |
| MA06 OA 16 | 2 | Conectar representaciones y lenguaje matemático · Ángulos en | 33 % | 29 % | 13.2 | — |
| MA06 OA 17 | 2 | Conectar representaciones y lenguaje matemático · Suma de án | 33 % | 33 % | 15.4 | — |
| MA06 OA 18 | 4 | Resolver un caso con una condición nueva · Superficie de cub | 33 % | 33 % | 15.9 | — |
| OR06 OA 07 | 1 | Examinar un caso ficticio protegido · Conflictos de conviven | 33 % | 33 % | 12.1 | — |
| OR06 OA 08 | 2 | Distinguir hechos, emociones y límites · Participar activa y | 33 % | 36 % | 14.0 | — |
| OR06 OA 09 | 3 | Comparar opciones y consecuencias · Practicar en forma autón | 33 % | 25 % | 19.6 | — |
| TE06 OA 06 | 5 | Probar con evidencia · Usar procesador de textos para crear, | 33 % | 33 % | 14.5 | — |
| TE06 OA 07 | 1 | Definir necesidad, usuario y criterio · Usar internet y comu | 33 % | 29 % | 16.0 | — |
| MU06 OA 02 | 3 | Interpretar o crear con criterio · Expresar, mostrando grado | 35 % | 43 % | 23.5 | — |
| CN06 OA 18 | 4 | Comparar resultados con un criterio · Las consecuencias de l | 36 % | 50 % | 22.4 | — |
| MU06 OA 08 | 2 | Reconocer un rasgo audible · Reflexionar sobre sus fortaleza | 36 % | 20 % | 22.1 | — |
| EF06 OA 09 | 4 | Resolver una situación nueva · Practicar actividades físicas | 36 % | 38 % | 20.2 | — |
| LE06 OA 06 | 3 | Seleccionar evidencia o recursos · Leer independientemente y | 41 % | 47 % | 20.5 | — |
| CN06 OA 15 | 1 | Observar y separar evidencia de interpretación · Medir e int | 42 % | 42 % | 26.0 | — |
| CN06 OA 15 | 3 | Modelar el sistema o fenómeno · Medir e interpretar la infor | 42 % | 42 % | 20.8 | — |
| OR06 OA 05 | 3 | Comparar opciones y consecuencias · Reconocer y describir ca | 46 % | 50 % | 20.4 | — |
| MA06 OA 15 | 2 | Conectar representaciones y lenguaje matemático · Construcci | 47 % | 29 % | 25.8 | — |
| LC06 OA LS02 | 4 | Construir una respuesta atribuida · Describir oralmente dife | 50 % | 50 % | 20.5 | — |
| LE06 OA 28 | 6 | Revisar para una audiencia · Interactuar de acuerdo con las  | 50 % | 38 % | 20.4 | — |
| MA06 OA 20 | 1 | Representar y precisar el concepto · Estimación y medición d | 50 % | 33 % | 20.1 | — |
| MU06 OA 02 | 2 | Reconocer un rasgo audible · Expresar, mostrando grados crec | 50 % | 36 % | 29.1 | — |
| MU06 OA 04 | 2 | Reconocer un rasgo audible · Cantar al unísono y a más voces | 50 % | 62 % | 21.7 | — |
| MU06 OA 02 | 1 | Escuchar antes de nombrar · Expresar, mostrando grados creci | 53 % | 71 % | 20.4 | — |
| EF06 OA 05 | 3 | Ensayar con variantes accesibles · Demostrar la correcta eje | 56 % | 62 % | 23.9 | — |
| HI06 OA 21 | 3 | Relacionar actores, causas y consecuencias · Trabajar en equ | 56 % | 58 % | 14.0 | respuesta «depende» en ejercicio cerrado |
| EF06 OA 03 | 1 | Reconocer meta y seguridad · Practicar deportes individuales | 57 % | 45 % | 21.6 | — |
| HI06 OA 14 | 1 | Ubicar en tiempo y espacio · Cómo han influido los desastres | 57 % | 69 % | 23.7 | — |
| HI06 OA 12 | 1 | Ubicar en tiempo y espacio · Comparar diversos ambientes nat | 58 % | 76 % | 24.4 | — |
| LC06 OA LF05 | 3 | Reconocer relaciones culturales · El sentido de la revitaliz | 58 % | 67 % | 21.4 | — |
| TE06 OA 05 | 1 | Definir necesidad, usuario y criterio · Usar software para o | 58 % | 62 % | 21.9 | — |
| LE06 OA 09 | 1 | Reconocer propósito y desafío · Desarrollar el gusto por la  | 60 % | 60 % | 20.1 | — |
| LE06 OA 03 | 2 | Modelar una lectura o producción · Leer y familiarizarse con | 62 % | 58 % | 11.0 | respuesta «depende» en ejercicio cerrado |
| CN06 OA 12 | 2 | Formular una pregunta o predicción · Explicar, a partir de m | 67 % | 70 % | 14.6 | respuesta «depende» en ejercicio cerrado |
| CN06 OA 15 | 5 | Explicar con evidencia y límites · Medir e interpretar la in | 67 % | 67 % | 14.2 | respuesta «depende» en ejercicio cerrado |
| EF06 OA 01 | 1 | Reconocer meta y seguridad · Demostrar la aplicación de las  | 67 % | 55 % | 25.3 | — |
| EF06 OA 04 | 1 | Reconocer meta y seguridad · Planificar y ejecutar actividad | 67 % | 64 % | 23.1 | — |
| LC06 OA 16 | 1 | Situar pueblo, territorio y fuente · Valorar y expresar a tr | 74 % | 67 % | 26.3 | — |
| LC06 OA LR03 | 2 | Escuchar o leer con límites declarados · Textos orales y esc | 74 % | 62 % | 21.0 | — |
| MU06 OA 06 | 4 | Ensayar y ajustar desde la escucha · Presentar su trabajo mu | 75 % | 75 % | 21.7 | — |
| MU06 OA 08 | 1 | Escuchar antes de nombrar · Reflexionar sobre sus fortalezas | 79 % | 70 % | 26.9 | — |
| LC06 OA 09 | 1 | Situar pueblo, territorio y fuente · Problematizar la relaci | 93 % | 100 % | 23.0 | — |
| HI06 OA 17 | 1 | Ubicar en tiempo y espacio · Que todas las personas tienen d | 95 % | 100 % | 21.4 | — |

## 7.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 29 | 57 % | 5 |
| ciencias-naturales | 72 | 51 % | 10 |
| educacion-fisica-salud | 25 | 45 % | 4 |
| historia-geografia-ciencias-sociales | 113 | 51 % | 12 |
| ingles | 80 | 34 % | 20 |
| ingles-propuesta | 65 | 31 % | 35 |
| lengua-literatura | 147 | 46 % | 15 |
| matematica | 83 | 47 % | 4 |
| musica | 30 | 41 % | 8 |
| orientacion | 49 | 47 % | 4 |
| tecnologia | 26 | 47 % | 4 |

**Clases marcadas para lectura prioritaria (7.º básico):** 121 de 719.

### Segunda lectura crítica de las 719 clases

Cada una de las 719 clases de 7.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios. Las fichas de actitud y la asignatura de Lengua Indígena de 7.º son integración transversal y no llevan cuaderno propio.

| Asignatura | Clases | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 83 | Enunciados imposibles («tres enteros de valor absoluto menor que 4 y menores que −1», solo hay dos; una reducción lineal incorrecta que coincide en dos puntos); dato irreal de 69 cuadritos completos y 20 partidos en un círculo de radio 5 (son 60 y 28); mediana de 7,5 cm en un triángulo de 9, 8 y 6 cm que no existe; pares ordenados «(7,5)» que en Chile se leen como decimal, ahora «(7, 5)»; piso −3 fuera de un edificio que llegaba al −2; descomposición del paralelogramo «en trapecio y triángulo» no general; división de fracciones planteada como reparto; términos usados sin definir (mediana, hipotenusa, fracción irreducible, puntos porcentuales). |
| Lengua y Literatura | 147 | Rima y asonancia con diptongos revisadas vocal por vocal; contradicciones entre regla y explicación («al menos 3 evidencias» contra «dos o tres»); eje de un gráfico que hacía parecer «el triple» lo que era 2,5 veces; «decido» en una lista de participios mal formados; texto con coma «que sobra» que era válida; «reímos» y verbos en -ar con la misma forma en presente y pasado; respuestas Sí/No sesgadas (50 No contra 16 Sí) reformuladas; homófonos y tildes verificados; alternativas absurdas reescritas. |
| Ciencias Naturales | 72 | Abstinencia y preservativo en una misma lista con «el único que reduce ITS»; ventana fértil calculada del 9 al 15 cuando con ovulación el día 16 es del 11 al 17; términos de biología usados antes de enseñarlos (estrógenos, anticuerpos, páncreas, insulina); ciclo del aire y estaciones precisados (el verano austral es de fines de diciembre a fines de marzo); leche agria «por el sabor»; seis casos de riesgo cerrados en «avisar a un adulto»; datos de tectónica y volcanes sin imprecisión. |
| Historia, Geografía y Ciencias Sociales | 113 | La Moneda «terminado en 1805 por Toesca» (Toesca murió en 1799); «los aztecas cultivaban cacao» (lo recibían como tributo); «chocolate» como palabra náhuatl de etimología discutida; cirílico atribuido directamente a Cirilo y Metodio; fortalezas incas «al sur del Maule»; un dux vitalicio contado entre cargos temporales; fuentes «independientes» que repetían la misma noticia; ostracismo ejemplificado con un acusado; ciclos de refuerzo y equilibrio confundidos; andenes (OA 14), minoica, fenicia, olmeca y chavín (OA 04) agregados para cubrir el OA. |
| Inglés (propuesta EN07) | 65 | «While Ana was cooking, her brother ___ music» con dos respuestas gramaticales; «has» sin considerar «have»; «going to» y «leather» usados sin enseñar; pasado irregular y comparativos sin regla; cinco palabras con /r/ y no cuatro; adivinanza con 3 pistas y no 2; «Penguins live in cold places» (hay pingüinos en Chile); módulo de OA 11 y 12 de 6.º reescrito tras una sobrescritura. |
| Inglés (oficial IN07) | 80 | «table» presentado como cognado de «tabla» (falso amigo); torta de chocolate para un perro; «must» usado antes de enseñarlo; «Pia plays the violin every Thursday. Today is Friday» sin probar nada; «Dear Mr. Pedro Gonzalez»; «es obligatorio» el casco sin certeza legal; OA 11 reescrito tras una sobrescritura; colocaciones y «too much/too many» agregados para cubrir el OA 08. |
| Educación Física y Salud | 25 | Ejemplo de respuesta que mandaba recoger vidrio; subir y bajar peldaños dentro de la casa; máquinas de ejercicio al aire libre; metas de 150 minutos semanales contra 30 diarios del OA; salto de 200 cm irreal; la plancha, «finta», «interceptar» y «golpe de calor» usados sin enseñar; supuestos sobre la familia («tu mamá», «tu hermano pequeño»). |
| Orientación | 49 | Pasos ante grooming contradictorios («guardar el chat» contra no guardar imágenes íntimas); víctima o testigo enfrentando al agresor como primer paso; recibir una petición culpada; número de ayuda inventado (solo se usa 147); «cambios hormonales» sin enseñar; frase agresiva que podía leerse como asertiva; ejercicios de sueño con la respuesta en el paréntesis. |
| Música | 30 | «Compás 1» de 16 unidades que sumaba 20; distancia 3 donde era 4; «2 minutos» para 36 tiempos de respiración; escala de niveles sin definir; «palmas» como medio sonoro y corporal a la vez; viola y violonchelo sin enseñar; «marchar» y «acto cívico» ambiguos. |
| Artes Visuales | 29 | «El doble de grande, 2 y 4 tazas» (el volumen se multiplica por 8); engrudo secado en 20 minutos por capa; escultura de cartón de 3 m en una plaza contra una clase de cuidado; foto de una compañera «sin permiso de su familia»; «base al menos la mitad de la altura» como regla; plano medio contradicho por el cielo; «pieza de adolescente». |
| Tecnología | 26 | Repartos que dejaban «sobra 0 cm²» cuando la consigna pedía usar los retazos; 20 ÷ 8 = 2,5 MB fuera de cifras enteras; criterio «peso» que chocaba con el «peso» de ponderación; rampa de cartón y madera para una silla de ruedas; «pincharse» con tijeras; «tu hermano de 6 años». |

#### Desajuste entre el texto del OA y los títulos de las clases

Los títulos de clase del plan son etapas genéricas, repetidas en todos los OA de cada asignatura (por ejemplo «Definir necesidad…», «Recognize purpose and context», «Situar pueblo, territorio y fuente»), y los autores repartieron el contenido del OA entre ellas. Los lectores comprobaron que lo enseñado calza con el OA. En Historia, Ciencias, Música, Educación Física, Orientación y parte de Lengua y Literatura los títulos sí coinciden con el contenido. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Matemática (valor de π y estimación del círculo en OA 11); Ciencias (anticoncepción general y métodos, cuidado de materiales); Historia (andenes y sistemas de cultivo en OA 14; minoica, fenicia, olmeca y chavín en OA 04; ecúmene, romanización, Euclides y Juegos Olímpicos); Inglés propuesta («I want / don't want» y «a few»); Inglés oficial (preguntar para clarificar, colocaciones y palabras compuestas del OA 08, «too much / too many», instructions).
- **Abiertos:** software educativo, geométrico y de presentación (Matemática OA 03, 12, 15, 16, 18 y 19; Tecnología OA 04); audio, video y escucha (Inglés, Lengua y Literatura OA 20, Música); obras completas, plan lector, romances y lira popular reales, mitos de pueblos originarios (Lengua y Literatura OA 02, 05 y 06); reglas de ortografía literal completas (OA 19: faltan h, g/j, ll/y); sacrificios humanos y relaciones de género (Historia OA 08 y OA 15); anticoncepción de emergencia (Ciencias OA 02); esclavitud en Roma sin clase propia (OA 07); ortocentro y bisectrices en cuadriláteros (Matemática OA 12); pasos concretos de danza y gimnasia (Educación física OA 01); obras reales, imágenes y visitas a museos (Artes); mediciones y experimentos reales (Ciencias OA 07 a 15, Tecnología OA 02).
- **Decisiones que dependen del programa oficial:** el listado de temas y obras del curso (Lengua y Literatura OA 02), la definición escolar de embrión y feto (semana 8), K = °C + 273 en Ciencias, la convención 1 GB = 1.000 MB, el estatus de los vectores libres y de «pocas» y «muchas» repeticiones, y las reglas propias del cuaderno rotuladas como tales (escala de esfuerzo, regla «6 por 6», rangos de palabras por minuto).

### Clases marcadas de 7.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| MU07 OA 02 | 1 | Escuchar antes de nombrar · Lenguaje musical y procedimiento | 7 % | 0 % | 17.2 | — |
| EN07 OA 05 | 5 | Communicate independently · Lectura de temas cercanos, actua | 10 % | 0 % | 13.5 | — |
| IN07 OA 01 | 3 | Locate explicit details | 13 % | 33 % | 13.7 | — |
| EN07 OA 05 | 1 | Recognize purpose and context · Lectura de temas cercanos, a | 14 % | 0 % | 15.9 | — |
| EN07 OA 08 | 3 | Model a comprehension or communication strategy · Presentaci | 16 % | 17 % | 15.8 | — |
| IN07 OA 08 | 1 | Exchange information and quantities | 16 % | 0 % | 14.5 | — |
| EN07 OA 01 | 4 | Practice through a genuine information gap · Comprensión glo | 17 % | 33 % | 15.0 | — |
| IN07 OA 05 | 4 | Speak from key words rather than read | 17 % | 33 % | 14.2 | — |
| EN07 OA 12 | 5 | Communicate independently · Funciones comunicativas en texto | 17 % | 17 % | 17.9 | — |
| EN07 OA 05 | 2 | Locate useful clues · Lectura de temas cercanos, actuales e  | 17 % | 0 % | 15.1 | — |
| EN07 OA 01 | 2 | Locate useful clues · Comprensión global de textos orales si | 17 % | 12 % | 16.4 | — |
| IN07 OA 09 | 5 | Answer with a cited clue | 18 % | 0 % | 11.7 | — |
| MU07 OA 04 | 4 | Interpretar o crear con criterio · Interpretación a una y má | 18 % | 33 % | 18.8 | — |
| EN07 OA 10 | 1 | Recognize purpose and context · Funciones comunicativas en c | 19 % | 29 % | 12.7 | — |
| EN07 OA 04 | 3 | Model a comprehension or communication strategy · Comprensió | 20 % | 33 % | 14.0 | — |
| EN07 OA 10 | 4 | Practice through a genuine information gap · Funciones comun | 21 % | 12 % | 11.9 | — |
| IN07 OA 16 | 1 | Express quantity and comparison | 21 % | 67 % | 25.9 | — |
| HI07 OA 02 | 3 | Examinar excedentes, intercambio y especialización | 21 % | 75 % | 23.1 | — |
| EN07 OA 01 | 3 | Model a comprehension or communication strategy · Comprensió | 22 % | 25 % | 13.6 | — |
| IN07 OA 01 | 2 | Identify the main idea | 22 % | 0 % | 14.2 | — |
| EN07 OA 01 | 5 | Communicate independently · Comprensión global de textos ora | 23 % | 29 % | 21.2 | — |
| EN07 OA 03 | 5 | Communicate independently · Estrategias antes, durante y des | 23 % | 29 % | 16.3 | — |
| IN07 OA 02 | 1 | Notice frequent chunks | 23 % | 33 % | 11.9 | — |
| IN07 OA 02 | 4 | Use stress and sound clues | 23 % | 0 % | 15.1 | — |
| EN07 OA 11 | 2 | Locate useful clues · Escritura breve según género, modelo y | 24 % | 44 % | 12.1 | — |
| MU07 OA 03 | 2 | Reconocer un rasgo audible · Interpretación vocal e instrume | 24 % | 29 % | 16.4 | — |
| MU07 OA 03 | 3 | Relacionar lenguaje musical y efecto · Interpretación vocal  | 24 % | 12 % | 17.6 | — |
| EF07 OA 03 | 2 | Regular intensidad y recuperación | 25 % | 67 % | 20.2 | — |
| EN07 OA 05 | 3 | Model a comprehension or communication strategy · Lectura de | 25 % | 0 % | 14.6 | — |
| MU07 OA 04 | 1 | Escuchar antes de nombrar · Interpretación a una y más voces | 25 % | 43 % | 18.2 | — |
| MU07 OA 04 | 2 | Reconocer un rasgo audible · Interpretación a una y más voce | 25 % | 43 % | 17.8 | — |
| OR07 OA 05 | 5 | Practicar comunicación o búsqueda de ayuda · Relaciones pres | 25 % | 22 % | 14.5 | — |
| TE07 OA 03 | 2 | Investigar soluciones y restricciones · Evaluación técnica d | 25 % | 33 % | 14.4 | — |
| EN07 OA 12 | 3 | Model a comprehension or communication strategy · Funciones  | 25 % | 12 % | 18.3 | — |
| EN07 OA 02 | 2 | Locate useful clues · Información explícita y relaciones en  | 25 % | 12 % | 17.7 | — |
| EN07 OA 10 | 3 | Model a comprehension or communication strategy · Funciones  | 26 % | 12 % | 15.0 | — |
| EN07 OA 02 | 5 | Communicate independently · Información explícita y relacion | 26 % | 29 % | 14.1 | — |
| IN07 OA 08 | 4 | Narrate past events and future plans | 26 % | 25 % | 12.0 | — |
| EN07 OA 09 | 5 | Communicate independently · Interacción y reparación del sig | 26 % | 0 % | 16.4 | — |
| CN07 OA 13 | 2 | Relacionar presión y volumen | 26 % | 100 % | 22.5 | — |
| EN07 OA 06 | 4 | Practice through a genuine information gap · Estrategias de  | 27 % | 29 % | 10.9 | — |
| OR07 OA 08 | 4 | Elegir una acción segura · Acuerdos y participación democrát | 27 % | 43 % | 16.2 | — |
| EN07 OA 12 | 1 | Recognize purpose and context · Funciones comunicativas en t | 27 % | 43 % | 12.4 | — |
| EN07 OA 05 | 4 | Practice through a genuine information gap · Lectura de tema | 27 % | 22 % | 13.2 | — |
| LE07 OA 11 | 5 | Recuperar referentes perdidos | 27 % | 100 % | 20.4 | — |
| EN07 OA 03 | 4 | Practice through a genuine information gap · Estrategias ant | 28 % | 33 % | 12.6 | — |
| EF07 OA 03 | 4 | Registrar progreso respecto de sí mismo | 28 % | 100 % | 20.2 | — |
| EN07 OA 12 | 2 | Locate useful clues · Funciones comunicativas en textos escr | 28 % | 29 % | 24.3 | — |
| IN07 OA 16 | 3 | Narrate past events | 28 % | 50 % | 40.2 | — |
| EN07 OA 02 | 4 | Practice through a genuine information gap · Información exp | 29 % | 38 % | 14.8 | — |
| MU07 OA 02 | 3 | Relacionar lenguaje musical y efecto · Lenguaje musical y pr | 29 % | 29 % | 14.1 | — |
| EN07 OA 02 | 1 | Recognize purpose and context · Información explícita y rela | 29 % | 25 % | 19.9 | — |
| TE07 OA 01 | 3 | Representar y planificar · Necesidades de reparación, adapta | 29 % | 33 % | 15.9 | — |
| EN07 OA 09 | 3 | Model a comprehension or communication strategy · Interacció | 30 % | 29 % | 11.1 | — |
| EN07 OA 04 | 2 | Locate useful clues · Comprensión de textos literarios y no  | 30 % | 33 % | 14.0 | — |
| IN07 OA 03 | 5 | Support an answer with two oral clues | 30 % | 33 % | 11.1 | — |
| EN07 OA 12 | 4 | Practice through a genuine information gap · Funciones comun | 30 % | 12 % | 11.3 | — |
| LE07 OA 11 | 2 | Resumir conservando relaciones | 30 % | 100 % | 22.9 | — |
| IN07 OA 08 | 2 | Describe people, places and actions | 30 % | 25 % | 14.1 | — |
| EN07 OA 03 | 2 | Locate useful clues · Estrategias antes, durante y después d | 31 % | 38 % | 13.9 | — |
| IN07 OA 06 | 2 | Open and sustain a turn | 31 % | 0 % | 10.6 | — |
| IN07 OA 03 | 2 | Locate specific people, places and actions | 31 % | 20 % | 14.4 | — |
| HI07 OA 08 | 1 | Reconocer qué se entiende por canon | 31 % | 33 % | 23.0 | — |
| IN07 OA 06 | 5 | Respond and repair meaning | 32 % | 33 % | 12.6 | — |
| EN07 OA 02 | 3 | Model a comprehension or communication strategy · Informació | 32 % | 22 % | 13.6 | — |
| EN07 OA 08 | 2 | Locate useful clues · Presentación oral multimodal | 32 % | 20 % | 12.3 | — |
| MU07 OA 03 | 1 | Escuchar antes de nombrar · Interpretación vocal e instrumen | 32 % | 43 % | 14.2 | — |
| IN07 OA 14 | 3 | Develop a coherent short text | 32 % | 33 % | 12.0 | — |
| OR07 OA 05 | 4 | Elegir una acción segura · Relaciones presenciales y virtual | 32 % | 38 % | 12.6 | — |
| EN07 OA 09 | 2 | Locate useful clues · Interacción y reparación del significa | 33 % | 17 % | 18.3 | — |
| LE07 OA 02 | 6 | Elaborar una reflexión con evidencia | 33 % | 67 % | 22.6 | — |
| MA07 OA 12 | 1 | Construir paralelas, perpendiculares y puntos medios | 33 % | 100 % | 21.6 | — |
| TE07 OA 02 | 3 | Representar y planificar · Diseño e implementación eficiente | 33 % | 33 % | 17.1 | — |
| IN07 OA 12 | 3 | Reread for a precise question | 34 % | 67 % | 20.2 | — |
| EF07 OA 04 | 1 | Leer riesgos y oportunidades del entorno | 35 % | 100 % | 20.3 | — |
| IN07 OA 15 | 1 | State a clear purpose | 36 % | 33 % | 21.1 | — |
| HI07 OA 09 | 3 | Relacionar herencia grecorromana y cristianismo | 40 % | 100 % | 20.8 | — |
| LE07 OA 05 | 4 | Interpretar desde el contexto | 40 % | 100 % | 21.1 | — |
| IN07 OA 08 | 5 | Combine functions in a real interaction | 41 % | 100 % | 23.0 | — |
| LE07 OA 12 | 5 | Editar una versión para circular | 42 % | 100 % | 20.2 | — |
| LE07 OA 15 | 1 | Analizar contexto, género y destinatario | 43 % | 100 % | 21.0 | — |
| CN07 OA 11 | 4 | Explicar transformaciones y escalas temporales | 44 % | 75 % | 13.8 | respuesta «depende» en ejercicio cerrado |
| HI07 OA 07 | 5 | Evaluar continuidad, cambio y apropiación del legado | 44 % | 100 % | 22.1 | — |
| LE07 OA 07 | 2 | Relacionar experiencia y evidencia sin autobiografía obligat | 45 % | 100 % | 20.4 | — |
| HI07 OA 08 | 3 | Examinar ciudadanía y centralidad humana | 46 % | 100 % | 22.1 | — |
| HI07 OA 02 | 1 | Comparar caza-recolección y producción de alimentos | 46 % | 100 % | 18.9 | respuesta «depende» en ejercicio cerrado |
| CN07 OA 12 | 1 | Relacionar energía solar, latitud y estaciones | 46 % | 100 % | 20.2 | — |
| EN07 OA 13 | 3 | Model a comprehension or communication strategy · Proceso de | 47 % | 11 % | 20.9 | — |
| IN07 OA 16 | 5 | Combine functions in a purposeful text | 49 % | 33 % | 22.6 | — |
| AR07 OA 06 | 3 | Examinar mediación, acceso y cuidado | 50 % | 75 % | 21.6 | — |
| CN07 OA 10 | 4 | Tomar decisiones de prevención desde mapas oficiales | 50 % | 100 % | 23.4 | — |
| CN07 OA 15 | 4 | Diseñar una prueba con control | 50 % | 100 % | 24.6 | — |
| MA07 OA 12 | 2 | Trazar bisectrices y alturas | 50 % | 100 % | 21.1 | — |
| OR07 OA 05 | 2 | Distinguir hechos, emociones, derechos y límites · Relacione | 53 % | 67 % | 20.8 | — |
| MA07 OA 16 | 3 | Elegir y construir un gráfico apropiado | 53 % | 75 % | 21.4 | — |
| CN07 OA 13 | 5 | Argumentar desde datos y condiciones seguras | 55 % | 75 % | 21.9 | — |
| HI07 OA 01 | 3 | Relacionar adaptación, cultura y ambiente | 55 % | 100 % | 20.1 | — |
| LE07 OA 06 | 2 | Analizar conflicto, personajes y símbolos | 55 % | 100 % | 22.9 | — |
| LE07 OA 08 | 6 | Construir una postura propia | 55 % | 100 % | 21.0 | — |
| CN07 OA 03 | 2 | Comparar ITS sin asociarlas a identidades | 55 % | 100 % | 17.5 | respuesta «depende» en ejercicio cerrado |
| LE07 OA 11 | 1 | Definir propósito y anticipar dificultades | 56 % | 100 % | 23.1 | — |
| CN07 OA 09 | 5 | Usar evidencia para evaluar el modelo | 57 % | 100 % | 27.3 | — |
| LE07 OA 03 | 6 | Comparar elementos con otra narración | 58 % | 100 % | 22.1 | — |
| LE07 OA 09 | 7 | Elaborar una evaluación fundamentada | 59 % | 100 % | 20.4 | — |
| LE07 OA 06 | 5 | Interpretar la función cultural del relato | 60 % | 100 % | 21.7 | — |
| HI07 OA 18 | 1 | Contextualizar ciudadanía y democracia | 62 % | 100 % | 14.3 | respuesta «depende» en ejercicio cerrado |
| TE07 OA 05 | 1 | Definir necesidad, usuario y criterio · Contraste de solucio | 62 % | 50 % | 21.2 | — |
| HI07 OA 18 | 3 | Examinar municipio y gremio | 64 % | 100 % | 25.4 | — |
| EF07 OA 04 | 5 | Evaluar seguridad y cuidado ambiental | 69 % | 100 % | 20.7 | — |
| AR07 OA 01 | 1 | Observar manifestaciones y registrar preguntas | 70 % | 100 % | 22.1 | — |
| CN07 OA 02 | 4 | Explicar responsabilidad reproductiva con fuentes sanitarias | 70 % | 80 % | 17.7 | respuesta «depende» en ejercicio cerrado |
| LE07 OA 10 | 3 | Relacionar información y pasaje literario | 70 % | 100 % | 23.3 | — |
| MA07 OA 15 | 2 | Comparar métodos de selección | 70 % | 100 % | 20.5 | — |
| HI07 OA 11 | 1 | Ubicar espacios y cronologías conectadas | 73 % | 100 % | 20.8 | — |
| CN07 OA 12 | 5 | Integrar factores en una explicación multicausal | 77 % | 100 % | 20.5 | — |
| HI07 OA 20 | 4 | Debatir principios para la convivencia actual | 78 % | 75 % | 21.9 | — |
| AR07 OA 06 | 4 | Diseñar una difusión pertinente para un trabajo | 80 % | 100 % | 20.6 | — |
| HI07 OA 23 | 1 | Delimitar una pregunta investigable | 81 % | 100 % | 23.0 | — |
| AR07 OA 06 | 1 | Caracterizar museo, galería, espacio público y plataforma di | 88 % | 100 % | 20.8 | — |
| LE07 OA 10 | 1 | Formular una necesidad de contexto | 89 % | 100 % | 21.0 | — |
| AR07 OA 02 | 1 | Definir intención y criterios de sustentabilidad | 93 % | 100 % | 20.3 | — |

## 8.º básico

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 29 | 62 % | 6 |
| ciencias-naturales | 74 | 51 % | 13 |
| educacion-fisica-salud | 26 | 48 % | 3 |
| historia-geografia-ciencias-sociales | 117 | 58 % | 20 |
| ingles | 80 | 30 % | 55 |
| ingles-propuesta | 65 | 30 % | 48 |
| lengua-literatura | 155 | 48 % | 26 |
| matematica | 77 | 41 % | 7 |
| musica | 30 | 39 % | 9 |
| orientacion | 49 | 51 % | 5 |
| tecnologia | 26 | 42 % | 8 |

**Clases marcadas para lectura prioritaria (8.º básico):** 200 de 728.

### Segunda lectura crítica de las 728 clases

Cada una de las 728 clases de 8.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios. Las fichas de actitud y la asignatura de Lengua Indígena de 8.º son integración transversal y no llevan cuaderno propio.

| Asignatura | Clases | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 77 | Ejemplo cuyo «error» no se veía (cilindro con r = 2 y h = 5 da 62,8 con la fórmula buena y con la mala); respuestas parecidas que confundían (13.000 y 5); definición de percentil que se contradecía con la regla del cuaderno y percentil 100 sin dato i+1; raíz cuadrada, cuadrantes en número romano y fórmula del ángulo interior usados sin enseñar; contar cuadritos del cuadrado inclinado sin pista; «completa la tabla» sin tabla; edades de «personas que conozcas» cambiadas por datos inventados; «interés compuesto» usado cuando la clase solo trata el simple. |
| Lengua y Literatura | 155 | Clave errada (OA 15: la correcta era la b); aleteos del colibrí, miel por abeja obrera y «las abejas viven en colonias» (hay solitarias); murciélagos que polinizan (los de Chile son insectívoros); conservar alimentos «sin refrigerador»; fragmentos T1 a T5, el «Canto de Ilén» y «El reloj de Elisa» citados en preguntas sin estar en la clase; rima consonante y tópicos verificados; «hubo/hubieron», «entre tú y yo» y subjuntivo revisados; «tal vez» con ambos modos; «Hoy necesito: cuaderno» incorrecto tras verbo; «lápiz» como grave (es esdrújula); voseo «decís». |
| Ciencias Naturales | 74 | Pared celular «solo vegetal» contra la clase de bacterias; inducción sin quitar la conexión a tierra; mito del celular encendido en la bencinera; lista de los 20 elementos solo en la clase 1 y usada en las clases 3 y 4; promedio ponderado y modelo de Thomson usados sin enseñar; datos de calentamiento del hielo incoherentes con una fuente constante; «los átomos no se ven» demasiado categórico; ejemplo de luz y burbujas que no sigue el inverso del cuadrado, rotulado como patrón de ejemplo. |
| Historia, Geografía y Ciencias Sociales | 117 | Alta Navarra en 1512 y 1515; «leones» del grabado colonial que podían ser pumas; capitán neerlandés fechado en 1600 (1605); «6 artículos» frente a 8; IDH regional que no calzaba con el promedio ponderado; «más fuentes de soldados» falso (5 y 5); consumo definido contra intercambio; años en miles («1.818»); salmones presentados solo como ventaja; Leonardo y Miguel Ángel (OA 01), Zipoli, autos sacramentales y Sor Juana (OA 09) agregados para cubrir el OA. |
| Inglés (propuesta EN08) | 65 | «The gym is behind the garden» y otros ordenamientos con más de una respuesta; «Reescribe con I would like to…» pasado a opción múltiple; el sonido inicial de «brother» pedido como /θ/; «I seen» al revés; «fifteen after four» y «ninetieth» de octubre; «by 5 p.m.» contra la voz pasiva; edad calculada que dependía del cumpleaños; «Bees make honey» generalizado; «quite» británico frente a estadounidense. |
| Inglés (oficial IN08) | 80 | Texto con «three rooms» y cuatro salas; «sea bass» como corvina; «Owls hunt at night» y «Penguins live in cold places» generalizados; «tea bags» en el compost; biblioteca «open every day» y «closed on weekends»; «Paper Boat» que era un gorro; cadenas en las ruedas de una bicicleta; /t/ después de ch; regla «i antes de e» sin excepciones; título repetido con 7.º; colocaciones del OA 08 sin ejercicio, agregadas. |
| Educación Física y Salud | 26 | Cuerda a la altura de la cabeza y entre sillas; 3 contra 3 con 2 o 3 personas; vóleibol de duplas sin cuatro personas; zonas de 3 m en una cancha de 6 m; meta de 150 minutos contra 30 diarios; «subió de 4 a 6 y bajó a 3»; materiales (globo, pared, caja) no entregados; ejemplos que no cumplían la consigna (2 materiales cuando se piden 3). |
| Orientación | 49 | «Bórrala» ante una imagen íntima recibida, cambiado por no reenviar ni guardar la imagen y no borrar el chat; orden de pasos ante grooming (decir no, guardar captura, bloquear, contar a un adulto); distractores «911» y «112» que parecían líneas de ayuda (solo se usa el 147); amigo que bebió mucho dejado «solo»; «una vez no genera adicción» imprecisa; «Cesfam» sin definir; supuestos sobre la familia («tu mamá»). |
| Música | 30 | Pedía qué acorde se siente más cerca del reposo cuando la clase solo enseña I y V; sección B igual a A en una forma ABA; «grados» contados de dos maneras (ahora «escalón»); motivo, puente, cifrados, soprano y bajo usados sin definir; síncopa pedida antes de enseñarse; homenaje a una persona fallecida cambiado; alternativas absurdas reescritas. |
| Artes Visuales | 29 | Opción «segura» con hilos colgados a la altura de la cabeza; pegamento fuera de la lista de materiales; 2 obras de 70 cm en 360 cm con espacio decimal; ejemplo que cambiaba dos decisiones cuando la consigna dice una; «una instalación es temporal» y «los colores vivos transmiten energía» demasiado categóricos; supuesto de que los adultos mayores no tienen internet; altura de montaje de 150 cm como referencia, no como norma. |
| Tecnología | 26 | Repartos de piezas por plancha con el cálculo regalado y el área mal contada (6000 ÷ 875 da 6,86); error relativo de 2,67 % fuera de cifras enteras; ejemplo de «impacto medio» cuando la consigna pide alto o bajo; pregunta de encuesta neutra, promedio y citar la fuente usados sin enseñar; 18 alternativas absurdas; tarea con un aparato conectado sin aviso de no abrirlo. |

#### Desajuste entre el texto del OA y los títulos de las clases

Los títulos de clase del plan son etapas genéricas, repetidas en todos los OA de cada asignatura (por ejemplo «Recognize purpose and context», «Definir necesidad, usuario y criterio», «Examinar un caso ficticio…»), y los autores repartieron el contenido del OA entre ellas. Los lectores comprobaron que lo enseñado calza con el OA. En Lengua y Literatura, Historia y Ciencias los títulos coinciden en general con el contenido. La clase 3 de OA 20 de Lengua y Literatura se titula «punto y coma», que no figura en el texto del OA, y se siguió el título del plan. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Lengua y Literatura (tópicos literarios en OA 05); Historia (capacidad de transformar el mundo y expresiones culturales en OA 01, música y teatro barrocos en OA 09); Inglés oficial (preguntar para clarificar, colocaciones y palabras compuestas del OA 08); Inglés propuesta («I want / don't want» y «a few» en 7.º, y en 8.º la voz pasiva y who/which).
- **Abiertos:** software educativo, geométrico y de simulación (Matemática OA 07, 09, 10, 12 a 15); audio, video, escucha, canciones y pronunciación real (Inglés, Lengua y Literatura OA 12 y 21, Música); obras completas, epopeyas y comedias reales y el plan lector (Lengua y Literatura OA 02, 06 a 08); ortografía literal completa (OA 20: faltan c/s/z, y/ll, x, mayúsculas, siglas); deícticos por nombre (OA 18); procesador de textos y diccionario en línea (Lengua y Literatura OA 16, Inglés); investigación experimental real y reactivos (Ciencias OA 06); entornos reales de práctica (Educación Física OA 01 y 04); rotaciones en el espacio y poliedros distintos del cubo y los prismas (Matemática OA 14); cuartiles con n impar y valores atípicos (OA 15); evangelización y roles de género con clase propia (Historia OA 11); formación del Estado nacional como clase propia (OA 19); pirámides de población y migración internacional (OA 21); patrimonio de pueblos originarios concreto (Artes OA 04).
- **Decisiones que dependen del programa oficial:** regla de percentiles y cuartiles (i = p·n/100) y bigotes al mínimo y al máximo; π = 3 y 3,14; tarifa de $200 por kWh; sentido antihorario positivo; 6/8 como dos pulsos; «escalón» frente a grado; escala de esfuerzo 1 a 10 y reglas propias de cada clase en Educación Física; forma de contar «grados» de un intervalo.

### Clases marcadas de 8.º básico

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| CN08 OA 12 | 4 | Investigar relaciones entre variables: evolución de los mode | 11 % | 33 % | 13.5 | — |
| IN08 OA 01 | 4 | Communicate through an information gap: Global and explicit  | 11 % | 12 % | 10.2 | — |
| EN08 OA 01 | 3 | Model a useful strategy: Understanding varied literary and f | 12 % | 0 % | 9.6 | — |
| IN08 OA 09 | 3 | Use a strategy or language function: Global and explicit mea | 12 % | 0 % | 18.6 | — |
| IN08 OA 08 | 2 | Locate precise evidence: Communicative functions for interac | 13 % | 0 % | 14.0 | — |
| IN08 OA 09 | 4 | Communicate through an information gap: Global and explicit  | 13 % | 11 % | 15.3 | — |
| IN08 OA 01 | 3 | Use a strategy or language function: Global and explicit mea | 13 % | 12 % | 13.4 | — |
| IN08 OA 08 | 1 | Recognize purpose and context: Communicative functions for i | 14 % | 0 % | 15.0 | — |
| IN08 OA 05 | 4 | Communicate through an information gap: Coherent multimodal  | 14 % | 17 % | 15.9 | — |
| IN08 OA 01 | 2 | Locate precise evidence: Global and explicit meaning in vari | 16 % | 25 % | 19.7 | — |
| IN08 OA 02 | 4 | Communicate through an information gap: Key language and int | 16 % | 0 % | 15.0 | — |
| EN08 OA 01 | 2 | Locate precise evidence: Understanding varied literary and f | 16 % | 25 % | 11.4 | — |
| EN08 OA 01 | 4 | Communicate through an information gap: Understanding varied | 16 % | 12 % | 14.1 | — |
| EN08 OA 02 | 4 | Communicate through an information gap: Purpose, detail and  | 16 % | 12 % | 12.0 | — |
| IN08 OA 07 | 3 | Use a strategy or language function: Personal and critical r | 18 % | 0 % | 14.4 | — |
| EN08 OA 07 | 3 | Model a useful strategy: Supported response and connection a | 18 % | 12 % | 13.4 | — |
| EN08 OA 05 | 2 | Locate precise evidence: Reading language functions in meani | 18 % | 0 % | 11.2 | — |
| EN08 OA 12 | 4 | Communicate through an information gap: Language functions i | 18 % | 14 % | 14.8 | — |
| IN08 OA 02 | 3 | Use a strategy or language function: Key language and intell | 19 % | 0 % | 17.2 | — |
| EF08 OA 01 | 3 | Combinar habilidades o decisiones: Habilidades motrices espe | 19 % | 43 % | 18.2 | — |
| IN08 OA 11 | 4 | Communicate through an information gap: Literary reading: th | 20 % | 12 % | 14.9 | — |
| IN08 OA 06 | 4 | Communicate through an information gap: Planning, repairing  | 20 % | 12 % | 12.4 | — |
| IN08 OA 05 | 2 | Locate precise evidence: Coherent multimodal oral presentati | 20 % | 33 % | 13.1 | — |
| IN08 OA 10 | 2 | Locate precise evidence: Critical reading of functional non- | 20 % | 0 % | 20.7 | — |
| IN08 OA 16 | 2 | Locate precise evidence: Communicative functions in written  | 20 % | 14 % | 16.8 | — |
| EN08 OA 05 | 4 | Communicate through an information gap: Reading language fun | 20 % | 12 % | 16.2 | — |
| IN08 OA 10 | 3 | Use a strategy or language function: Critical reading of fun | 20 % | 14 % | 17.1 | — |
| CN08 OA 11 | 4 | Investigar relaciones entre variables: calor, temperatura y  | 20 % | 29 % | 18.2 | — |
| IN08 OA 02 | 1 | Recognize purpose and context: Key language and intelligible | 21 % | 0 % | 18.3 | — |
| IN08 OA 02 | 2 | Locate precise evidence: Key language and intelligible sound | 21 % | 0 % | 14.4 | — |
| TE08 OA 06 | 2 | Investigar soluciones y restricciones: Impactos éticos, ambi | 21 % | 38 % | 19.0 | — |
| IN08 OA 02 | 5 | Respond independently: Key language and intelligible sounds  | 22 % | 0 % | 16.0 | — |
| IN08 OA 03 | 3 | Use a strategy or language function: Purpose, detail, sequen | 22 % | 12 % | 15.6 | — |
| IN08 OA 06 | 2 | Locate precise evidence: Planning, repairing and reviewing s | 22 % | 0 % | 7.8 | — |
| IN08 OA 08 | 3 | Use a strategy or language function: Communicative functions | 22 % | 0 % | 13.8 | — |
| EN08 OA 12 | 2 | Locate precise evidence: Language functions in written texts | 22 % | 0 % | 11.5 | — |
| EN08 OA 05 | 1 | Recognize purpose and context: Reading language functions in | 22 % | 0 % | 14.1 | — |
| IN08 OA 03 | 4 | Communicate through an information gap: Purpose, detail, seq | 22 % | 0 % | 19.9 | — |
| IN08 OA 10 | 4 | Communicate through an information gap: Critical reading of  | 22 % | 12 % | 14.1 | — |
| MU08 OA 05 | 3 | Relacionar lenguaje musical y propósito: improvisación, acom | 22 % | 14 % | 18.9 | — |
| EN08 OA 10 | 2 | Locate precise evidence: Language functions in conversation  | 22 % | 14 % | 14.4 | — |
| EN08 OA 11 | 3 | Model a useful strategy: Short multimodal texts for real aud | 22 % | 29 % | 9.1 | — |
| EN08 OA 08 | 3 | Model a useful strategy: Audience-aware multimodal oral pres | 23 % | 43 % | 9.6 | — |
| CN08 OA 05 | 3 | Construir o contrastar un modelo: interacción de sistemas pa | 24 % | 43 % | 16.6 | — |
| EN08 OA 06 | 3 | Model a useful strategy: Strategic reading before, during an | 24 % | 14 % | 11.1 | — |
| MU08 OA 02 | 1 | Escuchar y registrar antes de nombrar: lenguaje musical, com | 24 % | 22 % | 19.5 | — |
| EN08 OA 10 | 1 | Recognize purpose and context: Language functions in convers | 24 % | 14 % | 13.1 | — |
| EN08 OA 05 | 3 | Model a useful strategy: Reading language functions in meani | 24 % | 0 % | 10.6 | — |
| EN08 OA 08 | 4 | Communicate through an information gap: Audience-aware multi | 24 % | 29 % | 10.6 | — |
| EN08 OA 08 | 5 | Respond independently: Audience-aware multimodal oral presen | 24 % | 33 % | 14.6 | — |
| IN08 OA 14 | 4 | Communicate through an information gap: Writing process acro | 24 % | 25 % | 18.2 | — |
| TE08 OA 04 | 2 | Investigar soluciones y restricciones: Comunicación ética de | 24 % | 29 % | 17.1 | — |
| IN08 OA 06 | 3 | Use a strategy or language function: Planning, repairing and | 24 % | 12 % | 10.5 | — |
| IN08 OA 05 | 3 | Use a strategy or language function: Coherent multimodal ora | 24 % | 33 % | 15.3 | — |
| MA08 OA 10 | 3 | Interpretar pendiente e intercepto | 24 % | 100 % | 20.7 | — |
| EN08 OA 09 | 5 | Respond independently: Strategies for clear and fluent inter | 24 % | 0 % | 19.9 | — |
| IN08 OA 16 | 3 | Use a strategy or language function: Communicative functions | 24 % | 0 % | 15.7 | — |
| HI08 OA 21 | 2 | Contextualizar y seleccionar fuentes: conectividad, migració | 25 % | 29 % | 15.7 | — |
| IN08 OA 09 | 2 | Locate precise evidence: Global and explicit meaning in prin | 25 % | 44 % | 15.8 | — |
| TE08 OA 03 | 4 | Implementar con seguridad: Evaluación técnica y mejora de pr | 25 % | 33 % | 16.9 | — |
| EF08 OA 01 | 2 | Seleccionar una respuesta motriz: Habilidades motrices espec | 26 % | 71 % | 25.6 | — |
| IN08 OA 09 | 1 | Recognize purpose and context: Global and explicit meaning i | 26 % | 33 % | 14.9 | — |
| EN08 OA 05 | 5 | Respond independently: Reading language functions in meaning | 26 % | 29 % | 12.1 | — |
| IN08 OA 13 | 2 | Locate precise evidence: Creative multimodal stories and inf | 26 % | 29 % | 19.8 | — |
| EN08 OA 12 | 3 | Model a useful strategy: Language functions in written texts | 26 % | 14 % | 15.8 | — |
| EN08 OA 10 | 4 | Communicate through an information gap: Language functions i | 26 % | 43 % | 13.0 | — |
| IN08 OA 16 | 1 | Recognize purpose and context: Communicative functions in wr | 26 % | 0 % | 15.1 | — |
| TE08 OA 02 | 3 | Representar y planificar: Diseño sustentable y creación con  | 26 % | 33 % | 14.3 | — |
| EN08 OA 06 | 5 | Respond independently: Strategic reading before, during and  | 26 % | 0 % | 14.0 | — |
| IN08 OA 12 | 3 | Use a strategy or language function: Purposeful reading stra | 26 % | 0 % | 11.8 | — |
| IN08 OA 07 | 5 | Respond independently: Personal and critical response to tex | 27 % | 40 % | 11.3 | — |
| EN08 OA 09 | 3 | Model a useful strategy: Strategies for clear and fluent int | 27 % | 0 % | 14.5 | — |
| EN08 OA 07 | 2 | Locate precise evidence: Supported response and connection a | 27 % | 0 % | 12.7 | — |
| EN08 OA 11 | 4 | Communicate through an information gap: Short multimodal tex | 27 % | 14 % | 16.2 | — |
| IN08 OA 11 | 2 | Locate precise evidence: Literary reading: theme, character, | 27 % | 25 % | 14.8 | — |
| IN08 OA 13 | 4 | Communicate through an information gap: Creative multimodal  | 27 % | 17 % | 14.3 | — |
| EN08 OA 02 | 2 | Locate precise evidence: Purpose, detail and language eviden | 27 % | 14 % | 12.0 | — |
| EN08 OA 07 | 4 | Communicate through an information gap: Supported response a | 27 % | 12 % | 16.0 | — |
| IN08 OA 08 | 5 | Respond independently: Communicative functions for interacti | 27 % | 20 % | 14.8 | — |
| IN08 OA 08 | 4 | Communicate through an information gap: Communicative functi | 28 % | 0 % | 11.9 | — |
| EN08 OA 04 | 2 | Locate precise evidence: Integrated literary and non-literar | 28 % | 33 % | 11.9 | — |
| OR08 OA 04 | 4 | Elegir una acción segura: Bienestar cotidiano, vida saludabl | 28 % | 43 % | 21.1 | — |
| IN08 OA 04 | 3 | Use a strategy or language function: Before, during and afte | 28 % | 0 % | 10.7 | — |
| IN08 OA 04 | 5 | Respond independently: Before, during and after listening st | 28 % | 0 % | 16.7 | — |
| TE08 OA 01 | 2 | Investigar soluciones y restricciones: Oportunidades locales | 28 % | 25 % | 13.4 | — |
| EN08 OA 04 | 4 | Communicate through an information gap: Integrated literary  | 28 % | 17 % | 11.9 | — |
| LE08 OA 23 | 6 | Revisar desde evidencia de audiencia | 28 % | 100 % | 22.9 | — |
| EN08 OA 09 | 2 | Locate precise evidence: Strategies for clear and fluent int | 28 % | 14 % | 12.6 | — |
| EN08 OA 08 | 2 | Locate precise evidence: Audience-aware multimodal oral pres | 29 % | 43 % | 12.3 | — |
| EN08 OA 02 | 1 | Recognize purpose and context: Purpose, detail and language  | 29 % | 29 % | 19.0 | — |
| LE08 OA 08 | 4 | Construir una postura | 29 % | 100 % | 21.1 | — |
| MU08 OA 03 | 1 | Escuchar y registrar antes de nombrar: interpretación expres | 29 % | 38 % | 14.1 | — |
| EN08 OA 11 | 2 | Locate precise evidence: Short multimodal texts for real aud | 29 % | 29 % | 18.3 | — |
| EN08 OA 03 | 3 | Model a useful strategy: Strategic listening and clarificati | 29 % | 0 % | 15.3 | — |
| EN08 OA 03 | 4 | Communicate through an information gap: Strategic listening  | 29 % | 33 % | 16.6 | — |
| IN08 OA 07 | 2 | Locate precise evidence: Personal and critical response to t | 29 % | 29 % | 15.7 | — |
| MU08 OA 02 | 2 | Localizar rasgos audibles: lenguaje musical, composición y p | 29 % | 12 % | 17.7 | — |
| MU08 OA 04 | 3 | Relacionar lenguaje musical y propósito: interpretación a un | 29 % | 43 % | 14.3 | — |
| MU08 OA 05 | 4 | Interpretar o crear con criterio: improvisación, acompañamie | 29 % | 43 % | 16.1 | — |
| EN08 OA 02 | 5 | Respond independently: Purpose, detail and language evidence | 30 % | 0 % | 13.4 | — |
| EN08 OA 12 | 1 | Recognize purpose and context: Language functions in written | 30 % | 0 % | 13.6 | — |
| IN08 OA 15 | 4 | Communicate through an information gap: Writing to inform, n | 30 % | 0 % | 13.1 | — |
| LE08 OA 05 | 5 | Distinguir texto y puesta en escena | 30 % | 100 % | 20.8 | — |
| OR08 OA 05 | 3 | Comparar opciones y consecuencias: Derechos y bienestar en r | 30 % | 38 % | 16.7 | — |
| IN08 OA 16 | 4 | Communicate through an information gap: Communicative functi | 30 % | 17 % | 12.0 | — |
| EN08 OA 10 | 3 | Model a useful strategy: Language functions in conversation  | 30 % | 14 % | 13.1 | — |
| CN08 OA 11 | 2 | Examinar evidencia y representaciones: calor, temperatura y  | 30 % | 43 % | 15.9 | — |
| IN08 OA 04 | 4 | Communicate through an information gap: Before, during and a | 31 % | 25 % | 15.6 | — |
| IN08 OA 05 | 5 | Respond independently: Coherent multimodal oral presentation | 31 % | 20 % | 14.2 | — |
| AR08 OA 03 | 3 | Explorar procedimientos y decisiones visuales: instalación c | 31 % | 38 % | 16.4 | — |
| AR08 OA 04 | 3 | Explorar procedimientos y decisiones visuales: análisis de m | 31 % | 25 % | 13.1 | — |
| MU08 OA 07 | 3 | Relacionar lenguaje musical y propósito: música, sociedad y  | 31 % | 43 % | 18.6 | — |
| EN08 OA 09 | 4 | Communicate through an information gap: Strategies for clear | 31 % | 14 % | 12.8 | — |
| IN08 OA 06 | 5 | Respond independently: Planning, repairing and reviewing spo | 31 % | 14 % | 17.1 | — |
| MU08 OA 04 | 4 | Interpretar o crear con criterio: interpretación a una y más | 31 % | 20 % | 14.7 | — |
| EN08 OA 03 | 2 | Locate precise evidence: Strategic listening and clarificati | 31 % | 0 % | 12.0 | — |
| CN08 OA 15 | 3 | Construir o contrastar un modelo: elementos químicos frecuen | 32 % | 29 % | 15.4 | — |
| EN08 OA 12 | 5 | Respond independently: Language functions in written texts | 32 % | 17 % | 11.7 | — |
| IN08 OA 14 | 3 | Use a strategy or language function: Writing process across  | 32 % | 0 % | 16.3 | — |
| TE08 OA 04 | 3 | Representar y planificar: Comunicación ética del proceso tec | 32 % | 50 % | 27.3 | — |
| EN08 OA 10 | 5 | Respond independently: Language functions in conversation an | 32 % | 33 % | 12.1 | — |
| IN08 OA 01 | 5 | Respond independently: Global and explicit meaning in varied | 32 % | 14 % | 14.1 | — |
| EN08 OA 02 | 3 | Model a useful strategy: Purpose, detail and language eviden | 32 % | 0 % | 12.9 | — |
| IN08 OA 09 | 5 | Respond independently: Global and explicit meaning in print  | 32 % | 38 % | 15.1 | — |
| IN08 OA 03 | 2 | Locate precise evidence: Purpose, detail, sequence, fact and | 32 % | 12 % | 14.4 | — |
| EN08 OA 11 | 5 | Respond independently: Short multimodal texts for real audie | 32 % | 33 % | 16.7 | — |
| EN08 OA 09 | 1 | Recognize purpose and context: Strategies for clear and flue | 33 % | 0 % | 14.2 | — |
| CN08 OA 05 | 1 | Formular una pregunta investigable: interacción de sistemas  | 33 % | 29 % | 14.7 | — |
| AR08 OA 03 | 4 | Crear una respuesta visual propia: instalación como medio de | 33 % | 38 % | 13.9 | — |
| CN08 OA 12 | 2 | Examinar evidencia y representaciones: evolución de los mode | 33 % | 33 % | 15.8 | — |
| EN08 OA 04 | 3 | Model a useful strategy: Integrated literary and non-literar | 33 % | 0 % | 17.7 | — |
| IN08 OA 15 | 1 | Recognize purpose and context: Writing to inform, narrate an | 33 % | 25 % | 13.2 | — |
| EN08 OA 07 | 1 | Recognize purpose and context: Supported response and connec | 34 % | 12 % | 15.6 | — |
| IN08 OA 07 | 1 | Recognize purpose and context: Personal and critical respons | 35 % | 43 % | 21.1 | — |
| MU08 OA 04 | 1 | Escuchar y registrar antes de nombrar: interpretación a una  | 35 % | 83 % | 20.3 | — |
| LE08 OA 16 | 5 | Editar ortografía y presentación | 36 % | 100 % | 26.0 | — |
| OR08 OA 01 | 2 | Distinguir hechos, emociones, derechos y límites: Autoconcep | 36 % | 78 % | 13.9 | respuesta «depende» en ejercicio cerrado |
| LE08 OA 02 | 6 | Construir una reflexión fundamentada | 38 % | 100 % | 20.7 | — |
| HI08 OA 14 | 2 | Contextualizar y seleccionar fuentes: ilustración, razón y c | 40 % | 71 % | 20.5 | — |
| LE08 OA 22 | 5 | Negociar acuerdos parciales | 40 % | 100 % | 21.3 | — |
| LE08 OA 26 | 3 | Parafrasear con precisión | 41 % | 100 % | 20.7 | — |
| LE08 OA 08 | 2 | Relacionar experiencia y evidencia sin autobiografía obligat | 42 % | 100 % | 21.5 | — |
| LE08 OA 04 | 2 | Analizar apelación a los sentidos | 43 % | 100 % | 20.2 | — |
| AR08 OA 02 | 3 | Explorar procedimientos y decisiones visuales: impresión, pa | 44 % | 78 % | 20.8 | — |
| MA08 OA 12 | 4 | Aplicar y verificar en problemas | 44 % | 100 % | 28.0 | — |
| CN08 OA 05 | 2 | Examinar evidencia y representaciones: interacción de sistem | 45 % | 57 % | 20.7 | — |
| LE08 OA 22 | 1 | Preparar una postura provisional | 45 % | 100 % | 20.5 | — |
| LE08 OA 04 | 1 | Escuchar y registrar primeras imágenes | 45 % | 100 % | 21.0 | — |
| MA08 OA 16 | 3 | Detectar escalas manipuladoras | 45 % | 100 % | 23.1 | — |
| IN08 OA 14 | 5 | Respond independently: Writing process across short genres | 46 % | 43 % | 20.1 | — |
| MA08 OA 13 | 4 | Relacionar reglas y coordenadas | 47 % | 67 % | 20.6 | — |
| IN08 OA 03 | 1 | Recognize purpose and context: Purpose, detail, sequence, fa | 47 % | 29 % | 23.3 | — |
| AR08 OA 01 | 3 | Explorar procedimientos y decisiones visuales: personas, nat | 47 % | 75 % | 20.4 | — |
| CN08 OA 10 | 2 | Examinar evidencia y representaciones: circuitos eléctricos  | 47 % | 71 % | 22.8 | — |
| LE08 OA 10 | 3 | Examinar estereotipos y prejuicios | 47 % | 67 % | 21.2 | — |
| TE08 OA 02 | 4 | Implementar con seguridad: Diseño sustentable y creación con | 47 % | 67 % | 21.1 | — |
| HI08 OA 22 | 1 | Situar tiempo, espacio y problema: desarrollo regional y sus | 48 % | 43 % | 18.5 | respuesta «depende» en ejercicio cerrado |
| MA08 OA 03 | 2 | Explicar productos y cocientes de potencias | 50 % | 100 % | 20.4 | — |
| MA08 OA 11 | 2 | Desplegar redes y derivar el área | 50 % | 33 % | 22.5 | — |
| TE08 OA 03 | 5 | Probar con evidencia: Evaluación técnica y mejora de product | 50 % | 67 % | 24.5 | — |
| LE08 OA 04 | 6 | Comparar poemas | 52 % | 100 % | 22.8 | — |
| OR08 OA 05 | 6 | Transferir sin exposición personal: Derechos y bienestar en  | 52 % | 50 % | 20.1 | — |
| LE08 OA 18 | 6 | Justificar decisiones de cohesión | 52 % | 100 % | 24.0 | — |
| CN08 OA 14 | 1 | Formular una pregunta investigable: tabla periódica, patrone | 52 % | 86 % | 20.8 | — |
| HI08 OA 22 | 3 | Relacionar cambio, continuidad y territorio: desarrollo regi | 52 % | 43 % | 15.4 | respuesta «depende» en ejercicio cerrado |
| HI08 OA 18 | 2 | Contextualizar y seleccionar fuentes: derechos del hombre, c | 53 % | 75 % | 23.4 | — |
| LE08 OA 15 | 6 | Publicar y justificar decisiones | 54 % | 100 % | 21.4 | — |
| LE08 OA 08 | 5 | Vincular obra y visión de mundo | 54 % | 100 % | 23.2 | — |
| CN08 OA 14 | 3 | Construir o contrastar un modelo: tabla periódica, patrones  | 55 % | 57 % | 25.9 | — |
| HI08 OA 16 | 1 | Situar tiempo, espacio y problema: independencias hispanoame | 55 % | 100 % | 20.9 | — |
| CN08 OA 10 | 6 | Evaluar límites, seguridad e implicancias: circuitos eléctri | 55 % | 62 % | 22.2 | — |
| HI08 OA 01 | 1 | Situar tiempo, espacio y problema: humanismo y renacimiento | 56 % | 83 % | 20.2 | — |
| LE08 OA 04 | 7 | Construir una interpretación | 56 % | 100 % | 21.8 | — |
| HI08 OA 13 | 5 | Construir un argumento con evidencia: hacienda y sociedad ru | 58 % | 100 % | 20.7 | — |
| LE08 OA 10 | 1 | Reconocer propósitos explícitos e implícitos | 58 % | 100 % | 22.8 | — |
| CN08 OA 14 | 4 | Investigar relaciones entre variables: tabla periódica, patr | 61 % | 86 % | 23.5 | respuesta «depende» en ejercicio cerrado |
| OR08 OA 02 | 4 | Elegir una acción segura: Sexualidad integral, intimidad, re | 62 % | 67 % | 26.1 | — |
| LE08 OA 07 | 5 | Interpretar desde su contexto | 62 % | 100 % | 20.2 | — |
| LE08 OA 10 | 7 | Publicar una evaluación fundamentada | 63 % | 100 % | 22.2 | — |
| LE08 OA 01 | 6 | Recomendar desde una experiencia situada | 64 % | 100 % | 20.1 | — |
| HI08 OA 14 | 1 | Situar tiempo, espacio y problema: ilustración, razón y crít | 65 % | 100 % | 23.5 | — |
| HI08 OA 13 | 1 | Situar tiempo, espacio y problema: hacienda y sociedad rural | 67 % | 100 % | 20.1 | — |
| HI08 OA 17 | 4 | Contrastar actores, causas y perspectivas: legitimidad de la | 67 % | 75 % | 23.0 | — |
| LE08 OA 11 | 5 | Comunicar una comprensión enriquecida | 67 % | 100 % | 22.4 | — |
| LE08 OA 12 | 6 | Evaluar la estrategia utilizada | 71 % | 67 % | 21.1 | respuesta «depende» en ejercicio cerrado |
| HI08 OA 21 | 5 | Construir un argumento con evidencia: conectividad, migració | 72 % | 86 % | 13.6 | respuesta «depende» en ejercicio cerrado |
| HI08 OA 14 | 5 | Construir un argumento con evidencia: ilustración, razón y c | 72 % | 86 % | 21.6 | — |
| HI08 OA 02 | 5 | Construir un argumento con evidencia: de la sociedad medieva | 73 % | 100 % | 16.7 | respuesta «depende» en ejercicio cerrado |
| LE08 OA 17 | 5 | Revisar oraciones en un texto | 75 % | 100 % | 21.2 | — |
| HI08 OA 20 | 4 | Contrastar actores, causas y perspectivas: regiones: criteri | 77 % | 62 % | 14.0 | respuesta «depende» en ejercicio cerrado |
| AR08 OA 05 | 1 | Observar referentes sin copiar: evaluación y revisión de tra | 80 % | 86 % | 20.1 | — |
| HI08 OA 20 | 1 | Situar tiempo, espacio y problema: regiones: criterios físic | 80 % | 62 % | 15.5 | respuesta «depende» en ejercicio cerrado |
| HI08 OA 08 | 5 | Construir un argumento con evidencia: ciudad y administració | 81 % | 100 % | 21.6 | — |
| HI08 OA 16 | 5 | Construir un argumento con evidencia: independencias hispano | 81 % | 100 % | 22.5 | — |
| EF08 OA 01 | 1 | Explorar con seguridad: Habilidades motrices específicas en  | 81 % | 86 % | 14.1 | respuesta «depende» en ejercicio cerrado |
| LE08 OA 13 | 1 | Elegir tema, género y destinatario | 82 % | 100 % | 25.3 | — |
| MA08 OA 08 | 1 | Traducir situaciones a ecuaciones | 86 % | 100 % | 21.0 | — |
| LE08 OA 11 | 1 | Formular una necesidad de contexto | 89 % | 100 % | 22.7 | — |
| HI08 OA 06 | 1 | Situar tiempo, espacio y problema: conquista y caída de impe | 91 % | 100 % | 21.2 | — |
| HI08 OA 09 | 1 | Situar tiempo, espacio y problema: barroco y cultura colonia | 100 % | 100 % | 20.6 | — |

## 1.º medio

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 20 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

### Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 29 | 52 % | 5 |
| ciencias-naturales | 100 | 42 % | 41 |
| educacion-fisica-salud | 28 | 45 % | 4 |
| historia-geografia-ciencias-sociales | 132 | 58 % | 25 |
| ingles | 80 | 34 % | 43 |
| ingles-propuesta | 65 | 30 % | 47 |
| lengua-literatura | 143 | 49 % | 36 |
| matematica | 66 | 40 % | 16 |
| musica | 32 | 43 % | 12 |
| orientacion | 52 | 49 % | 14 |
| tecnologia | 26 | 47 % | 4 |

**Clases marcadas para lectura prioritaria (1.º medio):** 247 de 753.

### Segunda lectura crítica de las 753 clases

Cada una de las 753 clases de 1.º medio fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta los ejercicios cerrados y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios, y dos lectores (Inglés propuesta OA 01 a 10 e Inglés oficial OA 01 a 10) leyeron y comprobaron datos sin resolver cada ejercicio a ciegas. Las fichas de actitud y la asignatura de Lengua Indígena son integración transversal y no llevan cuaderno propio.

| Asignatura | Clases | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 66 | Unos 60 ejercicios que repetían un ejemplo de la explicación o un ejemplo resuelto; error de estudiante mal descrito («2^-3 < 2^-5 porque −3 < −5» es falso); «semejantes» y «eje x» usados antes de enseñarse; pregunta de homotecia que no consideraba las rectas por el centro; «1.º A» con 30 estudiantes contra un ejemplo de 20; «menos de 0 errores»; juego con dinero cambiado por puntos; fila 4 del triángulo de Pascal ambigua. |
| Lengua y Literatura | 143 | Diptongo «cui-da-do» en la fila equivocada; «ardilla» como diminutivo en -illa; «Completa con b o v» con respuesta g; saludo «Querida Ana,» aceptable pero usado como distractor; «sábado 10 + dos días» llegaba al lunes; mayúscula tras el saludo de una carta formal; unas 35 sumas triviales reemplazadas por ejercicios de contenido; unas 25 consignas abiertas pasadas a opción múltiple; citas de un poema no entregado; «el río se repite» que era falso; «cardal» y otros datos inseguros; termómetro doméstico con mercurio. |
| Ciencias Naturales | 100 | Ejemplo de coincidencias de rasgos mal contado (0 y 0 donde eran 1 y 1); ala de ave y de murciélago presentadas como homólogas; géneros reales con conteos de especies inventados; tabla de temperatura y volumen que contradecía a otra; explicación de las estaciones con el invierno austral invertido; tabla de hipocentros que no calzaba con el ejercicio; Pitágoras y «infiltración», «kWh» usados sin enseñar; vela encendida en un frasco cerrado, espejo de vidrio y elástico estirado reemplazados por opciones seguras; pregunta sensible de evolución frente a creación reformulada. |
| Historia, Geografía y Ciencias Sociales | 132 | Unas 150 consignas y contextos que citaban fuentes, cuadros o dossiers «de este cuaderno» sin traerlos; las mujeres «votaron» en 1934 y 1949 (obtuvieron el derecho); tabla con 800 inscritos de los que 500 sabían leer contra una regla que exige saber leer; ferrocarril a Temuco, primer censo de 1854 y «libre tránsito» imprecisos; África con 10 % de control europeo fechada en 1880 (1870); edad del voto de 1874 sin sustento; Brasil omitido en la abolición; «cambio climático» definido como variación natural; «militante comunista» anacrónico en 1905; ejercicio que pedía a un estudiante representar a un pueblo. |
| Inglés (propuesta EN1M) | 65 | Ejercicios que repetían un ejemplo resuelto; «And ___» que aceptaba last y finally; «Although it is cheap, the bag is not strong» sin contraste real; ejemplos de respuesta que no calzaban con los datos; esquema «de la clase anterior» sin traerlo; shall presentado como futuro seguro; supuestos sobre la familia; texto de «School uniforms» con el mismo tema que el Inglés oficial; una opción A/B con doble coma. |
| Inglés (oficial IN1M) | 80 | Opción «5–14 January» contra clave «5–16»; /tr/ y /dr/ explicados como si el español no los tuviera; -tion enseñado como /ʧ/ (es /ʃən/); orden de adjetivos usado sin enseñarse; razón errónea sobre «honest» y la h; inglés británico y americano mezclados en un pasaje (unificado en americano); contextos de museo, mercado y bicicletas idénticos a los de Inglés propuesta, cambiados. |
| Educación Física y Salud | 28 | Pasar de «defensa a atacar» desde 2-2-1 llevaba a 1-2-2, no a 2-1-2; plan de baile que subía a 35 minutos con un máximo de 30; caminar de espaldas y círculos de cuello eliminados; pulso en la muñeca sin presionar el cuello; «me molestó la espalda» como razón para seguir con la plancha; alternativas de alimentación que sugerían restringirse; unas 20 alternativas absurdas. |
| Orientación | 52 | Unas 130 preguntas de recuperación de tipo «¿X es Y, sí o no?» que regalaban la definición; afirmación de que todo contacto íntimo de un adulto con un menor es delito (no lo es a los 14 a 17 años); protocolo en línea con el orden «bloquear y luego guardar captura» (ahora guardar captura, bloquear, avisar); kiosco del colegio con sellos «ALTO EN»; ejemplo que suponía que Ema ya había pedido orientación; soldadura reemplazada por circuitos con pila y LED; Fono Niños 147 descrito como «atendido por profesionales» sin sustento. |
| Música | 32 | Ejemplo y ejercicio que cambiaban tempo y volumen a la vez cuando la clase enseña a cambiar un solo rasgo; «la 1» como única respuesta cuando cumplían la 1 y la 4; patrón de golpes repetido del ejemplo resuelto; «compás fuerte» sin definir; «desafinar» usado para la pentatónica; empate de minutos entre dos estudiantes; «funeral» y «persona de la familia» cambiados. |
| Artes Visuales | 29 | Doce puntos máximos donde dos criterios dan 6 (ahora 9 en tres criterios); cifras de rampa, muro y litros de pintura repetidas del ejemplo; «tallar» la matriz y libro cosido con aguja cambiados por cartón pegado y cordel; ficha de grabado sin tamaño; «saturado» sin definir. |
| Tecnología | 26 | Ejemplos de respuesta que no calzaban con la consigna (6 criterios pedidos y 3 dados); promedio de 3,875 fuera de cifras enteras; ejercicio trivial «1 o 5»; afirmación categórica sobre derechos de autor suavizada; protocolo de seguridad digital completado con «no se borra el chat ni se reenvía una imagen íntima». |

#### Desajuste entre el texto del OA y los títulos de las clases

Los títulos de clase del plan son etapas genéricas, repetidas en todos los OA de cada asignatura (por ejemplo «Recognize purpose and context», «Definir necesidad, usuario y criterio»), y los autores repartieron el contenido del OA entre ellas. Los lectores comprobaron que lo enseñado calza con el OA. Casos señalados: Tecnología OA 01 avanza hacia priorizar e idear aunque el OA pide identificar oportunidades; los tres entornos de Tecnología OA 05 (natural, construido y digital) y las cuatro «dimensiones de la experiencia humana» de Lengua y Literatura OA 02 son interpretación de los autores, no texto del OA; la clase 6 de Educación Física OA 03 se dedicó a ingesta y gasto calórico.

#### Vacíos de cobertura frente al OA

- **Cerrados dentro de las clases existentes:** Inglés oficial (excepción «question» /tʃ/ en OA 02); Inglés propuesta (caracterización del personaje en OA 04); Inglés oficial OA 14 (cuento y resumen).
- **Abiertos:** software educativo y geometría dinámica (Matemática OA 04, 05, 08, 09, 11, 14 y 15); audio, video, canciones, noticieros y pronunciación real (Inglés, Lengua y Literatura OA 19 y 21, Música); obras completas del programa y plan lector (Lengua y Literatura OA 01, 02, 06 y 07; el Lazarillo de Tormes en OA 03); cuentos, artículos y diario personal (Inglés propuesta OA 11); narraciones y exposiciones orales como formatos (Inglés propuesta OA 01); mitos, leyendas y novelas adaptadas (Inglés propuesta OA 04); técnica real por deporte, RCP y maniobras de atragantamiento (Educación Física OA 01 y 04); segmento circular de 120° (Matemática OA 06, exige trigonometría de 2.º medio); lupa e instrumentos ópticos (Matemática OA 08); aportes de científicos en Ciencias OA 02; salitre y guano como exportaciones (Historia OA 10); flujos del Estado con subsidios y gasto público (Historia OA 19); casos de quechua, colla, diaguita, atacameño, kawéskar y yagán (Historia OA 24); procesador de textos y diccionario en línea (Lengua y Literatura OA 15, Inglés); institutos locales de protección y sexualidad integral más allá de lo general (Orientación OA 02 y 03).
- **Decisiones que dependen del programa oficial:** notación en unidades de duración (corchea = 1) y términos «compás fuerte» y «densidad» de Música; formato de cita acordado `(Apellido, año, v. N)` de Lengua y Literatura; ortografía de «kawéskar» y «yagán»; fórmulas de pendiente de rampa 1 en 12 y alturas de montaje de 150 cm de Artes Visuales como referencia; rango 60 a 80 % de la frecuencia cardíaca máxima estimada de Educación Física.

### Clases marcadas de 1.º medio

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| IN1M OA 01 | 4 | Communicate through an information gap: Global and explicit  | 9 % | 25 % | 8.7 | — |
| CN1M OA 16 | 4 | Investigar relaciones entre variables: Astronomía en Chile,  | 11 % | 38 % | 16.8 | — |
| IN1M OA 09 | 4 | Communicate through an information gap: Global and explicit  | 12 % | 11 % | 14.6 | — |
| MU1M OA 05 | 4 | Interpretar, improvisar o crear: Improvisación, creación y a | 12 % | 29 % | 16.4 | — |
| IN1M OA 01 | 2 | Locate precise evidence: Global and explicit meaning in vari | 13 % | 25 % | 16.5 | — |
| EN1M OA 01 | 3 | Model a useful strategy: Understanding varied literary and f | 14 % | 0 % | 14.3 | — |
| EN1M OA 01 | 4 | Communicate through an information gap: Understanding varied | 14 % | 25 % | 17.2 | — |
| EN1M OA 05 | 3 | Model a useful strategy: Language functions interpreted in m | 14 % | 12 % | 14.3 | — |
| MA1M OA 12 | 3 | Construir una regla o comparación: Distribuciones bivariadas | 14 % | 14 % | 18.8 | — |
| CN1M OA 11 | 2 | Examinar evidencia y representaciones: Luz, modelos, imágene | 16 % | 17 % | 19.0 | — |
| EN1M OA 10 | 3 | Model a useful strategy: Language functions in discussion an | 16 % | 0 % | 19.6 | — |
| EN1M OA 05 | 1 | Recognize purpose and context: Language functions interprete | 16 % | 12 % | 19.4 | — |
| TE1M OA 02 | 2 | Investigar soluciones y restricciones: Desarrollo ético y se | 17 % | 29 % | 18.1 | — |
| MA1M OA 07 | 1 | Explorar una construcción: Área y volumen del cono | 18 % | 0 % | 15.1 | — |
| EN1M OA 01 | 2 | Locate precise evidence: Understanding varied literary and f | 18 % | 25 % | 15.1 | — |
| IN1M OA 13 | 4 | Communicate through an information gap: Creative multimodal  | 18 % | 14 % | 16.7 | — |
| MA1M OA 15 | 2 | Representar patrones: Azar, tabla de Galton y paseos aleator | 18 % | 50 % | 21.0 | — |
| IN1M OA 08 | 3 | Use a strategy or language function: First-year secondary co | 18 % | 14 % | 13.5 | — |
| IN1M OA 08 | 4 | Communicate through an information gap: First-year secondary | 18 % | 14 % | 11.6 | — |
| CN1M OA 12 | 3 | Construir o contrastar un modelo: Oído, ojo, espectros y tec | 18 % | 33 % | 18.0 | — |
| IN1M OA 09 | 2 | Locate precise evidence: Global and explicit meaning in prin | 18 % | 33 % | 16.7 | — |
| MA1M OA 10 | 4 | Resolver un caso nuevo: Semejanza, proporcionalidad y modelo | 18 % | 33 % | 17.3 | — |
| EN1M OA 02 | 4 | Communicate through an information gap: Purpose, detail, lan | 19 % | 11 % | 14.6 | — |
| EN1M OA 04 | 4 | Communicate through an information gap: Integrated literary  | 19 % | 33 % | 17.1 | — |
| EN1M OA 07 | 4 | Communicate through an information gap: Critical and persona | 19 % | 22 % | 19.1 | — |
| IN1M OA 02 | 3 | Use a strategy or language function: Key expressions, colloc | 19 % | 14 % | 19.1 | — |
| IN1M OA 14 | 3 | Use a strategy or language function: Writing process across  | 20 % | 0 % | 22.6 | — |
| CN1M OA 07 | 4 | Investigar relaciones entre variables: Fotosíntesis, respira | 20 % | 43 % | 16.1 | — |
| CN1M OA 19 | 2 | Examinar evidencia y representaciones: Compuestos binarios y | 20 % | 38 % | 17.5 | — |
| CN1M OA 19 | 3 | Construir o contrastar un modelo: Compuestos binarios y tern | 20 % | 25 % | 23.1 | — |
| IN1M OA 01 | 3 | Use a strategy or language function: Global and explicit mea | 20 % | 25 % | 14.6 | — |
| EN1M OA 05 | 2 | Locate precise evidence: Language functions interpreted in m | 21 % | 12 % | 16.2 | — |
| IN1M OA 16 | 4 | Communicate through an information gap: First-year secondary | 21 % | 0 % | 13.1 | — |
| AR1M OA 06 | 2 | Explorar materiales y referentes: Diseño de difusión artísti | 21 % | 0 % | 17.1 | — |
| OR1M OA 05 | 4 | Elegir una acción segura: Relaciones constructivas presencia | 21 % | 14 % | 19.4 | — |
| EN1M OA 05 | 4 | Communicate through an information gap: Language functions i | 21 % | 12 % | 13.2 | — |
| EN1M OA 12 | 4 | Communicate through an information gap: Language functions i | 21 % | 0 % | 16.7 | — |
| TE1M OA 04 | 4 | Implementar con seguridad: Comunicación del diseño y desarro | 21 % | 14 % | 15.6 | — |
| EN1M OA 07 | 5 | Respond independently: Critical and personal response across | 21 % | 29 % | 15.0 | — |
| IN1M OA 06 | 2 | Locate precise evidence: Planning, repairing and reviewing s | 21 % | 0 % | 13.2 | — |
| AR1M OA 06 | 3 | Probar decisiones visuales: Diseño de difusión artística par | 22 % | 29 % | 18.4 | — |
| EN1M OA 09 | 4 | Communicate through an information gap: Strategies for clear | 22 % | 25 % | 13.9 | — |
| IN1M OA 05 | 2 | Locate precise evidence: Coherent multimodal oral presentati | 22 % | 29 % | 14.5 | — |
| EN1M OA 10 | 1 | Recognize purpose and context: Language functions in discuss | 22 % | 0 % | 20.1 | — |
| IN1M OA 05 | 4 | Communicate through an information gap: Coherent multimodal  | 22 % | 43 % | 12.8 | — |
| MA1M OA 14 | 3 | Construir una regla o comparación: Reglas aditiva y multipli | 22 % | 67 % | 22.1 | — |
| EN1M OA 12 | 1 | Recognize purpose and context: Language functions in connect | 22 % | 12 % | 13.5 | — |
| IN1M OA 08 | 2 | Locate precise evidence: First-year secondary communicative  | 22 % | 0 % | 13.4 | — |
| EN1M OA 05 | 5 | Respond independently: Language functions interpreted in mea | 23 % | 14 % | 15.4 | — |
| HI1M OA 21 | 2 | Contextualizar y seleccionar fuentes: Ahorro, crédito, inver | 23 % | 50 % | 22.5 | — |
| LE1M OA 18 | 2 | Investigar y seleccionar insumos: Ortografía y puntuación pa | 23 % | 0 % | 22.4 | — |
| EN1M OA 08 | 2 | Locate precise evidence: Audience-aware multimodal oral pres | 23 % | 29 % | 17.0 | — |
| IN1M OA 16 | 3 | Use a strategy or language function: First-year secondary co | 23 % | 0 % | 17.9 | — |
| LE1M OA 10 | 2 | Localizar evidencias decisivas: Lectura crítica de medios | 24 % | 17 % | 14.2 | — |
| EN1M OA 03 | 3 | Model a useful strategy: Purposeful listening, inference and | 24 % | 0 % | 13.2 | — |
| MU1M OA 03 | 3 | Ensayar una decisión musical: Interpretación vocal e instrum | 24 % | 12 % | 17.8 | — |
| EN1M OA 07 | 2 | Locate precise evidence: Critical and personal response acro | 24 % | 0 % | 17.8 | — |
| CN1M OA 09 | 4 | Investigar relaciones entre variables: Ondas: energía, propi | 24 % | 29 % | 15.8 | — |
| IN1M OA 09 | 3 | Use a strategy or language function: Global and explicit mea | 24 % | 11 % | 14.2 | — |
| CN1M OA 11 | 3 | Construir o contrastar un modelo: Luz, modelos, imágenes y c | 24 % | 20 % | 20.3 | — |
| EF1M OA 04 | 3 | Combinar habilidades o decisiones: Actividad física regular, | 25 % | 33 % | 16.2 | — |
| EN1M OA 04 | 3 | Model a useful strategy: Integrated literary and non-literar | 25 % | 0 % | 20.3 | — |
| EN1M OA 11 | 2 | Locate precise evidence: Modeled multimodal writing for real | 25 % | 29 % | 15.0 | — |
| IN1M OA 02 | 4 | Communicate through an information gap: Key expressions, col | 25 % | 0 % | 17.8 | — |
| IN1M OA 10 | 3 | Use a strategy or language function: Purpose, structure and  | 25 % | 14 % | 12.8 | — |
| MA1M OA 04 | 3 | Construir el procedimiento: Sistemas de ecuaciones lineales  | 25 % | 40 % | 20.1 | — |
| MA1M OA 10 | 2 | Medir y formular una conjetura: Semejanza, proporcionalidad  | 25 % | 43 % | 19.0 | — |
| MU1M OA 04 | 3 | Ensayar una decisión musical: Interpretación a una y más voc | 25 % | 43 % | 14.8 | — |
| EN1M OA 10 | 2 | Locate precise evidence: Language functions in discussion an | 25 % | 14 % | 16.1 | — |
| IN1M OA 11 | 4 | Communicate through an information gap: Theme, character, se | 26 % | 25 % | 9.9 | — |
| CN1M OA 17 | 3 | Construir o contrastar un modelo: Evidencias, variables y re | 26 % | 50 % | 21.8 | — |
| CN1M OA 10 | 2 | Examinar evidencia y representaciones: Sonido, modelo ondula | 26 % | 14 % | 15.8 | — |
| IN1M OA 16 | 2 | Locate precise evidence: First-year secondary communicative  | 26 % | 12 % | 16.1 | — |
| OR1M OA 10 | 5 | Practicar comunicación o búsqueda de ayuda: Diseño flexible  | 26 % | 50 % | 21.0 | — |
| EF1M OA 04 | 4 | Aplicar estrategia o plan: Actividad física regular, autocui | 26 % | 38 % | 16.8 | — |
| LE1M OA 22 | 4 | Ensayar con retroalimentación: Exposición investigada para u | 26 % | 40 % | 15.4 | — |
| EN1M OA 10 | 5 | Respond independently: Language functions in discussion and  | 27 % | 17 % | 16.6 | — |
| IN1M OA 10 | 5 | Respond independently: Purpose, structure and language in no | 27 % | 14 % | 13.5 | — |
| IN1M OA 16 | 1 | Recognize purpose and context: First-year secondary communic | 27 % | 25 % | 17.4 | — |
| IN1M OA 08 | 1 | Recognize purpose and context: First-year secondary communic | 27 % | 25 % | 15.1 | — |
| CN1M OA 06 | 4 | Investigar relaciones entre variables: Ciclos biogeoquímicos | 27 % | 25 % | 16.1 | — |
| CN1M OA 12 | 1 | Formular una pregunta investigable: Oído, ojo, espectros y t | 27 % | 50 % | 20.6 | — |
| CN1M OA 12 | 2 | Examinar evidencia y representaciones: Oído, ojo, espectros  | 27 % | 33 % | 17.2 | — |
| CN1M OA 12 | 4 | Investigar relaciones entre variables: Oído, ojo, espectros  | 27 % | 33 % | 19.5 | — |
| IN1M OA 01 | 5 | Respond independently: Global and explicit meaning in varied | 27 % | 29 % | 14.5 | — |
| EN1M OA 08 | 4 | Communicate through an information gap: Audience-aware multi | 27 % | 29 % | 15.8 | — |
| EN1M OA 08 | 5 | Respond independently: Audience-aware multimodal oral presen | 27 % | 17 % | 15.7 | — |
| IN1M OA 13 | 2 | Locate precise evidence: Creative multimodal stories and rel | 28 % | 38 % | 17.9 | — |
| IN1M OA 13 | 3 | Use a strategy or language function: Creative multimodal sto | 28 % | 25 % | 15.8 | — |
| MA1M OA 15 | 1 | Organizar datos o resultados: Azar, tabla de Galton y paseos | 28 % | 43 % | 17.4 | — |
| EN1M OA 09 | 2 | Locate precise evidence: Strategies for clear, fluent and re | 28 % | 0 % | 17.3 | — |
| CN1M OA 20 | 3 | Construir o contrastar un modelo: Estequiometría y relacione | 28 % | 43 % | 13.4 | — |
| EN1M OA 07 | 1 | Recognize purpose and context: Critical and personal respons | 28 % | 22 % | 22.3 | — |
| IN1M OA 02 | 1 | Recognize purpose and context: Key expressions, collocations | 28 % | 43 % | 12.5 | — |
| IN1M OA 02 | 2 | Locate precise evidence: Key expressions, collocations and s | 28 % | 29 % | 12.0 | — |
| EN1M OA 03 | 4 | Communicate through an information gap: Purposeful listening | 28 % | 25 % | 13.4 | — |
| IN1M OA 04 | 4 | Communicate through an information gap: Strategic listening, | 28 % | 25 % | 10.3 | — |
| EN1M OA 11 | 5 | Respond independently: Modeled multimodal writing for real a | 28 % | 33 % | 16.6 | — |
| CN1M OA 08 | 4 | Investigar relaciones entre variables: Impactos humanos, fen | 29 % | 38 % | 14.9 | — |
| IN1M OA 11 | 5 | Respond independently: Theme, character, setting and plot in | 29 % | 14 % | 20.8 | — |
| IN1M OA 07 | 2 | Locate precise evidence: Evidence-based personal response an | 29 % | 0 % | 15.1 | — |
| EN1M OA 02 | 1 | Recognize purpose and context: Purpose, detail, language and | 29 % | 25 % | 18.0 | — |
| LE1M OA 04 | 2 | Localizar evidencias decisivas: Análisis de poemas | 29 % | 40 % | 19.7 | — |
| LE1M OA 15 | 2 | Investigar y seleccionar insumos: Proceso de escritura, revi | 29 % | 14 % | 13.9 | — |
| AR1M OA 02 | 3 | Probar decisiones visuales: Grabado, pintura mural e investi | 29 % | 44 % | 19.7 | — |
| LE1M OA 22 | 3 | Modelar una decisión comunicativa: Exposición investigada pa | 29 % | 33 % | 9.8 | — |
| MU1M OA 04 | 1 | Escuchar y reconocer rasgos: Interpretación a una y más voce | 29 % | 14 % | 15.0 | — |
| MU1M OA 05 | 3 | Ensayar una decisión musical: Improvisación, creación y arre | 29 % | 43 % | 23.8 | — |
| EN1M OA 01 | 5 | Respond independently: Understanding varied literary and fun | 30 % | 29 % | 14.7 | — |
| EN1M OA 12 | 3 | Model a useful strategy: Language functions in connected wri | 30 % | 25 % | 17.6 | — |
| EN1M OA 06 | 3 | Model a useful strategy: Strategic reading before, during an | 30 % | 0 % | 14.2 | — |
| CN1M OA 03 | 3 | Construir o contrastar un modelo: Clasificación biológica y  | 30 % | 43 % | 14.1 | — |
| EN1M OA 09 | 5 | Respond independently: Strategies for clear, fluent and repa | 30 % | 0 % | 22.6 | — |
| IN1M OA 06 | 4 | Communicate through an information gap: Planning, repairing  | 30 % | 25 % | 14.2 | — |
| CN1M OA 15 | 3 | Construir o contrastar un modelo: Escalas y propiedades de e | 31 % | 29 % | 21.0 | — |
| CN1M OA 15 | 4 | Investigar relaciones entre variables: Escalas y propiedades | 31 % | 29 % | 17.5 | — |
| EN1M OA 11 | 3 | Model a useful strategy: Modeled multimodal writing for real | 31 % | 33 % | 15.5 | — |
| EN1M OA 02 | 3 | Model a useful strategy: Purpose, detail, language and sound | 31 % | 0 % | 14.2 | — |
| CN1M OA 09 | 2 | Examinar evidencia y representaciones: Ondas: energía, propi | 31 % | 29 % | 15.6 | — |
| EN1M OA 12 | 5 | Respond independently: Language functions in connected writt | 31 % | 14 % | 16.1 | — |
| IN1M OA 09 | 1 | Recognize purpose and context: Global and explicit meaning i | 31 % | 44 % | 14.3 | — |
| MA1M OA 07 | 3 | Justificar la relación: Área y volumen del cono | 31 % | 33 % | 14.9 | — |
| MU1M OA 02 | 4 | Interpretar, improvisar o crear: Comparación musical, lengua | 31 % | 44 % | 18.1 | — |
| AR1M OA 05 | 3 | Probar decisiones visuales: Crítica fundamentada de proyecto | 32 % | 25 % | 14.3 | — |
| EN1M OA 13 | 4 | Communicate through an information gap: Independent writing  | 32 % | 25 % | 16.1 | — |
| IN1M OA 10 | 2 | Locate precise evidence: Purpose, structure and language in  | 32 % | 38 % | 13.5 | — |
| CN1M OA 06 | 2 | Examinar evidencia y representaciones: Ciclos biogeoquímicos | 32 % | 25 % | 16.4 | — |
| LE1M OA 12 | 5 | Revisar con evidencia de lectura: Escritura flexible en nuev | 32 % | 43 % | 14.5 | — |
| EN1M OA 10 | 4 | Communicate through an information gap: Language functions i | 32 % | 14 % | 12.1 | — |
| IN1M OA 06 | 3 | Use a strategy or language function: Planning, repairing and | 32 % | 0 % | 9.6 | — |
| IN1M OA 15 | 2 | Locate precise evidence: Writing to explain, narrate and exp | 32 % | 12 % | 11.6 | — |
| IN1M OA 15 | 4 | Communicate through an information gap: Writing to explain,  | 32 % | 0 % | 15.2 | — |
| OR1M OA 02 | 4 | Elegir una acción segura: Sexualidad, vínculos afectivos, re | 32 % | 50 % | 21.3 | — |
| CN1M OA 02 | 2 | Examinar evidencia y representaciones: Evidencias de evoluci | 32 % | 33 % | 17.3 | — |
| IN1M OA 13 | 5 | Respond independently: Creative multimodal stories and relev | 32 % | 43 % | 9.2 | — |
| MA1M OA 08 | 4 | Resolver un caso nuevo: Homotecia y razón de escala | 32 % | 60 % | 21.8 | — |
| IN1M OA 03 | 3 | Use a strategy or language function: Purpose, relevant ideas | 32 % | 10 % | 14.1 | — |
| CN1M OA 11 | 5 | Explicar patrones y mecanismos: Luz, modelos, imágenes y col | 32 % | 33 % | 18.1 | — |
| IN1M OA 12 | 3 | Use a strategy or language function: Strategic reading befor | 32 % | 14 % | 17.6 | — |
| LE1M OA 15 | 3 | Planificar decisiones: Proceso de escritura, revisión y edic | 32 % | 33 % | 18.6 | — |
| CN1M OA 13 | 4 | Investigar relaciones entre variables: Ondas sísmicas, medic | 32 % | 57 % | 23.7 | — |
| CN1M OA 13 | 5 | Explicar patrones y mecanismos: Ondas sísmicas, medición y c | 32 % | 43 % | 16.5 | — |
| EF1M OA 04 | 2 | Seleccionar una respuesta motriz: Actividad física regular,  | 32 % | 44 % | 18.2 | — |
| EN1M OA 03 | 2 | Locate precise evidence: Purposeful listening, inference and | 33 % | 0 % | 14.5 | — |
| EN1M OA 09 | 3 | Model a useful strategy: Strategies for clear, fluent and re | 33 % | 14 % | 14.5 | — |
| IN1M OA 05 | 3 | Use a strategy or language function: Coherent multimodal ora | 33 % | 43 % | 14.3 | — |
| EN1M OA 04 | 2 | Locate precise evidence: Integrated literary and non-literar | 33 % | 33 % | 13.0 | — |
| CN1M OA 09 | 5 | Explicar patrones y mecanismos: Ondas: energía, propiedades  | 33 % | 43 % | 17.1 | — |
| CN1M OA 20 | 1 | Formular una pregunta investigable: Estequiometría y relacio | 33 % | 14 % | 19.1 | — |
| EF1M OA 04 | 1 | Explorar con seguridad y diagnóstico: Actividad física regul | 33 % | 44 % | 16.6 | — |
| EN1M OA 07 | 3 | Model a useful strategy: Critical and personal response acro | 33 % | 33 % | 18.3 | — |
| LE1M OA 16 | 2 | Investigar y seleccionar insumos: Estilo directo e indirecto | 33 % | 67 % | 21.6 | — |
| LE1M OA 19 | 6 | Responder y ajustar: Comprensión y evaluación de textos oral | 33 % | 43 % | 17.1 | — |
| MA1M OA 03 | 1 | Reconocer variables y restricciones: Productos notables y co | 33 % | 29 % | 17.2 | — |
| MA1M OA 05 | 3 | Construir el procedimiento: Relaciones lineales en dos varia | 33 % | 40 % | 16.9 | — |
| MA1M OA 06 | 1 | Explorar una construcción: Sectores y segmentos circulares | 33 % | 40 % | 15.0 | — |
| OR1M OA 07 | 5 | Practicar comunicación o búsqueda de ayuda: Participación so | 33 % | 12 % | 11.8 | — |
| LE1M OA 05 | 3 | Analizar recursos y relaciones: Análisis de textos dramático | 34 % | 86 % | 20.7 | — |
| EN1M OA 04 | 1 | Recognize purpose and context: Integrated literary and non-l | 34 % | 33 % | 24.3 | — |
| CN1M OA 10 | 4 | Investigar relaciones entre variables: Sonido, modelo ondula | 34 % | 43 % | 21.6 | — |
| HI1M OA 24 | 4 | Contrastar actores, causas y perspectivas: Conflicto, conviv | 34 % | 89 % | 24.4 | — |
| CN1M OA 01 | 2 | Examinar evidencia y representaciones: Formación, estratos y | 35 % | 43 % | 21.0 | — |
| MU1M OA 02 | 2 | Relacionar lenguaje, contexto y propósito: Comparación music | 36 % | 50 % | 20.5 | — |
| CN1M OA 13 | 3 | Construir o contrastar un modelo: Ondas sísmicas, medición y | 36 % | 29 % | 21.0 | — |
| EN1M OA 11 | 1 | Recognize purpose and context: Modeled multimodal writing fo | 36 % | 71 % | 21.4 | — |
| HI1M OA 21 | 5 | Construir un argumento con evidencia: Ahorro, crédito, inver | 36 % | 62 % | 20.8 | — |
| LE1M OA 05 | 1 | Entrar al texto con propósito: Análisis de textos dramáticos | 37 % | 71 % | 20.2 | — |
| EN1M OA 02 | 2 | Locate precise evidence: Purpose, detail, language and sound | 37 % | 12 % | 20.8 | — |
| LE1M OA 13 | 4 | Escribir un primer desarrollo: Escritura explicativa | 38 % | 100 % | 21.4 | — |
| CN1M OA 14 | 4 | Investigar relaciones entre variables: Sistema Tierra-Luna-S | 38 % | 43 % | 21.9 | — |
| LE1M OA 18 | 3 | Planificar decisiones: Ortografía y puntuación para facilita | 38 % | 33 % | 24.3 | — |
| CN1M OA 15 | 2 | Examinar evidencia y representaciones: Escalas y propiedades | 38 % | 0 % | 21.6 | — |
| LE1M OA 08 | 5 | Situar texto y contexto: Interpretación literaria situada | 38 % | 60 % | 24.0 | respuesta «depende» en ejercicio cerrado |
| OR1M OA 03 | 4 | Elegir una acción segura: Evaluación de riesgos, protección  | 39 % | 75 % | 22.4 | — |
| MU1M OA 01 | 3 | Ensayar una decisión musical: Apreciación de músicas de trad | 39 % | 71 % | 20.3 | — |
| MU1M OA 04 | 2 | Relacionar lenguaje, contexto y propósito: Interpretación a  | 39 % | 50 % | 22.6 | — |
| LE1M OA 05 | 4 | Contrastar interpretaciones: Análisis de textos dramáticos y | 39 % | 100 % | 22.4 | — |
| CN1M OA 11 | 1 | Formular una pregunta investigable: Luz, modelos, imágenes y | 39 % | 83 % | 20.5 | — |
| MU1M OA 03 | 1 | Escuchar y reconocer rasgos: Interpretación vocal e instrume | 40 % | 62 % | 20.3 | — |
| CN1M OA 16 | 1 | Formular una pregunta investigable: Astronomía en Chile, ins | 41 % | 62 % | 20.9 | — |
| AR1M OA 02 | 2 | Explorar materiales y referentes: Grabado, pintura mural e i | 41 % | 75 % | 20.9 | — |
| OR1M OA 06 | 4 | Elegir una acción segura: Resolución de conflictos en un mar | 41 % | 57 % | 20.5 | — |
| CN1M OA 14 | 3 | Construir o contrastar un modelo: Sistema Tierra-Luna-Sol, e | 41 % | 29 % | 23.2 | — |
| IN1M OA 14 | 4 | Communicate through an information gap: Writing process acro | 41 % | 25 % | 20.4 | — |
| LE1M OA 05 | 7 | Revisar y transferir: Análisis de textos dramáticos y puesta | 42 % | 100 % | 25.9 | — |
| LE1M OA 03 | 6 | Formular una lectura propia: Análisis de narraciones | 42 % | 60 % | 20.8 | respuesta «depende» en ejercicio cerrado |
| CN1M OA 18 | 3 | Construir o contrastar un modelo: Conservación de átomos y m | 43 % | 33 % | 20.6 | — |
| OR1M OA 02 | 6 | Transferir sin exposición personal: Sexualidad, vínculos afe | 44 % | 50 % | 22.4 | — |
| MA1M OA 09 | 4 | Resolver un caso nuevo: Teorema de Tales desde la homotecia | 44 % | 60 % | 21.4 | — |
| LE1M OA 17 | 3 | Planificar decisiones: Correferencia con metáfora y metonimi | 45 % | 60 % | 25.0 | — |
| LE1M OA 18 | 5 | Revisar con evidencia de lectura: Ortografía y puntuación pa | 45 % | 43 % | 28.0 | — |
| LE1M OA 07 | 1 | Entrar al texto con propósito: Romanticismo y visión de mund | 46 % | 67 % | 22.1 | — |
| MA1M OA 12 | 2 | Representar patrones: Distribuciones bivariadas y nubes de p | 46 % | 33 % | 20.1 | — |
| OR1M OA 10 | 4 | Elegir una acción segura: Diseño flexible y responsable de p | 46 % | 86 % | 23.9 | — |
| HI1M OA 24 | 3 | Relacionar cambio, continuidad y territorio: Conflicto, conv | 46 % | 89 % | 21.3 | — |
| LE1M OA 04 | 5 | Situar texto y contexto: Análisis de poemas | 47 % | 80 % | 23.3 | — |
| TE1M OA 06 | 2 | Investigar soluciones y restricciones: Efectos sociales de l | 47 % | 43 % | 22.1 | — |
| OR1M OA 03 | 2 | Distinguir hechos, derechos y límites: Evaluación de riesgos | 47 % | 78 % | 21.0 | — |
| LE1M OA 10 | 3 | Analizar recursos y relaciones: Lectura crítica de medios | 47 % | 50 % | 13.7 | respuesta «depende» en ejercicio cerrado |
| LE1M OA 03 | 7 | Revisar y transferir: Análisis de narraciones | 47 % | 100 % | 21.6 | — |
| HI1M OA 25 | 3 | Relacionar cambio, continuidad y territorio: Industrializaci | 47 % | 75 % | 23.6 | — |
| OR1M OA 09 | 2 | Distinguir hechos, derechos y límites: Opciones académicas y | 47 % | 62 % | 19.1 | respuesta «depende» en ejercicio cerrado |
| LE1M OA 08 | 3 | Analizar recursos y relaciones: Interpretación literaria sit | 48 % | 67 % | 33.6 | — |
| LE1M OA 05 | 5 | Situar texto y contexto: Análisis de textos dramáticos y pue | 49 % | 71 % | 21.0 | — |
| CN1M OA 14 | 1 | Formular una pregunta investigable: Sistema Tierra-Luna-Sol, | 50 % | 57 % | 22.3 | — |
| HI1M OA 10 | 2 | Contextualizar y seleccionar fuentes: Chile, mercados atlánt | 50 % | 62 % | 22.6 | — |
| HI1M OA 13 | 6 | Evaluar proyecciones y límites: Ocupación austral, inmigraci | 50 % | 88 % | 20.4 | — |
| LE1M OA 06 | 3 | Analizar recursos y relaciones: Tragedia, conflicto humano y | 50 % | 57 % | 24.5 | — |
| LE1M OA 24 | 3 | Evaluar fuentes: Investigación sobre lenguaje y literatura | 50 % | 100 % | 13.8 | respuesta «depende» en ejercicio cerrado |
| HI1M OA 19 | 1 | Situar tiempo, espacio y problema: Escasez, necesidades y ci | 52 % | 62 % | 20.9 | — |
| OR1M OA 04 | 1 | Examinar un caso ficticio protegido: Acciones autónomas para | 52 % | 67 % | 22.4 | — |
| OR1M OA 08 | 4 | Elegir una acción segura: Iniciativas de justicia, buen trat | 52 % | 71 % | 24.1 | — |
| MU1M OA 06 | 2 | Relacionar lenguaje, contexto y propósito: Fortalezas, creci | 52 % | 67 % | 20.3 | — |
| OR1M OA 09 | 4 | Elegir una acción segura: Opciones académicas y laborales pa | 53 % | 71 % | 21.4 | — |
| CN1M OA 18 | 1 | Formular una pregunta investigable: Conservación de átomos y | 53 % | 83 % | 20.3 | — |
| CN1M OA 15 | 5 | Explicar patrones y mecanismos: Escalas y propiedades de est | 54 % | 71 % | 21.2 | — |
| LE1M OA 14 | 1 | Reconocer género, propósito y audiencia: Escritura persuasiv | 55 % | 100 % | 21.6 | — |
| MA1M OA 09 | 2 | Medir y formular una conjetura: Teorema de Tales desde la ho | 55 % | 100 % | 20.4 | — |
| HI1M OA 18 | 1 | Situar tiempo, espacio y problema: Cuestión social, actores  | 55 % | 62 % | 22.4 | — |
| TE1M OA 04 | 2 | Investigar soluciones y restricciones: Comunicación del dise | 55 % | 50 % | 26.4 | — |
| CN1M OA 20 | 4 | Investigar relaciones entre variables: Estequiometría y rela | 59 % | 50 % | 20.5 | — |
| HI1M OA 10 | 4 | Contrastar actores, causas y perspectivas: Chile, mercados a | 59 % | 78 % | 20.3 | respuesta «depende» en ejercicio cerrado |
| HI1M OA 22 | 1 | Situar tiempo, espacio y problema: Consumo informado, derech | 60 % | 50 % | 22.4 | — |
| LE1M OA 04 | 7 | Revisar y transferir: Análisis de poemas | 60 % | 100 % | 23.7 | — |
| HI1M OA 21 | 1 | Situar tiempo, espacio y problema: Ahorro, crédito, inversió | 61 % | 56 % | 22.7 | — |
| OR1M OA 03 | 6 | Transferir sin exposición personal: Evaluación de riesgos, p | 61 % | 75 % | 21.1 | — |
| LE1M OA 23 | 3 | Modelar una decisión comunicativa: Efectos de recursos lingü | 62 % | 57 % | 17.3 | respuesta «depende» en ejercicio cerrado |
| LE1M OA 06 | 1 | Entrar al texto con propósito: Tragedia, conflicto humano y  | 62 % | 71 % | 34.1 | — |
| LE1M OA 08 | 6 | Formular una lectura propia: Interpretación literaria situad | 63 % | 67 % | 27.7 | — |
| HI1M OA 25 | 1 | Situar tiempo, espacio y problema: Industrialización, ambien | 65 % | 88 % | 23.1 | — |
| HI1M OA 11 | 5 | Construir un argumento con evidencia: Opinión pública, educa | 65 % | 100 % | 21.1 | — |
| CN1M OA 19 | 4 | Investigar relaciones entre variables: Compuestos binarios y | 67 % | 75 % | 20.2 | — |
| LE1M OA 17 | 4 | Escribir un primer desarrollo: Correferencia con metáfora y  | 67 % | 67 % | 22.4 | — |
| HI1M OA 16 | 6 | Evaluar proyecciones y límites: Orden liberal y parlamentari | 69 % | 86 % | 20.7 | — |
| HI1M OA 11 | 1 | Situar tiempo, espacio y problema: Opinión pública, educació | 71 % | 67 % | 21.8 | — |
| HI1M OA 23 | 1 | Situar tiempo, espacio y problema: Respuestas políticas ante | 71 % | 100 % | 29.0 | — |
| HI1M OA 24 | 1 | Situar tiempo, espacio y problema: Conflicto, convivencia y  | 72 % | 78 % | 24.1 | — |
| MU1M OA 07 | 5 | Registrar y contrastar versiones: Música, identidad, cultura | 73 % | 100 % | 22.0 | — |
| LE1M OA 23 | 4 | Ensayar con retroalimentación: Efectos de recursos lingüísti | 75 % | 83 % | 18.7 | respuesta «depende» en ejercicio cerrado |
| HI1M OA 12 | 1 | Situar tiempo, espacio y problema: Exploración estatal, cien | 76 % | 56 % | 21.9 | — |
| HI1M OA 19 | 2 | Contextualizar y seleccionar fuentes: Escasez, necesidades y | 76 % | 71 % | 22.2 | — |
| HI1M OA 10 | 5 | Construir un argumento con evidencia: Chile, mercados atlánt | 77 % | 100 % | 20.6 | — |
| HI1M OA 23 | 2 | Contextualizar y seleccionar fuentes: Respuestas políticas a | 77 % | 71 % | 21.4 | — |
| HI1M OA 10 | 1 | Situar tiempo, espacio y problema: Chile, mercados atlántico | 78 % | 56 % | 20.9 | — |
| HI1M OA 23 | 5 | Construir un argumento con evidencia: Respuestas políticas a | 82 % | 100 % | 22.9 | — |
| HI1M OA 23 | 4 | Contrastar actores, causas y perspectivas: Respuestas políti | 83 % | 100 % | 25.0 | respuesta «depende» en ejercicio cerrado |
| LE1M OA 23 | 1 | Escuchar o preparar con propósito: Efectos de recursos lingü | 85 % | 86 % | 23.0 | — |
