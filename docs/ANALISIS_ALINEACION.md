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
| tecnologia | 26 | 40 % | 0 |

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
| LC01 OA LF05 | 1 | Lengua en uso · Mirar con procedencia | 67 % | 67 % | 17.9 | — |
| HI01 OA 11 | 1 | Trabajo visible e invisible | 71 % | 100 % | 16.8 | — |
| HI01 OA 09 | 4 | Ruta de localización | 73 % | 100 % | 20.0 | — |
| EF01 OA 08 | 2 | Cambios durante el esfuerzo | 74 % | 100 % | 16.3 | — |
| HI01 OA 15 | 2 | Personas que la hacen funcionar | 76 % | 100 % | 21.6 | — |
| LC01 OA 11 | 2 | Fuente cultural | 78 % | 100 % | 17.9 | — |
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
