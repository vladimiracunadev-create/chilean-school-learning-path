"""Specific third-grade Mathematics and Language sequences.

The compact profiles below are editorial source data: every OA has its own
progression, disciplinary anchor, expected evidence and misconception.  The
builders expand those decisions into the stable lesson contract used by the
public Markdown and HTML outputs.
"""
from __future__ import annotations


MATH_SKILLS = (
    ("de Habilidad MA03 OAH a", "resolver un problema dado o creado"),
    ("de Habilidad MA03 OAH b", "entender, planificar, resolver y comprobar"),
    ("de Habilidad MA03 OAH c", "transferir un procedimiento a un problema semejante"),
    ("de Habilidad MA03 OAH d", "formular preguntas matemáticas que profundizan la comprensión"),
    ("de Habilidad MA03 OAH e", "descubrir y comunicar una regularidad"),
    ("de Habilidad MA03 OAH f", "hacer una deducción apoyada en material o dibujo"),
    ("de Habilidad MA03 OAH g", "describir una situación con una expresión, ecuación o dibujo"),
    ("de Habilidad MA03 OAH h", "escuchar otro razonamiento y usarlo para revisar un error"),
    ("de Habilidad MA03 OAH i", "seleccionar y evaluar un modelo matemático"),
    ("de Habilidad MA03 OAH j", "traducir acciones cotidianas a lenguaje matemático"),
    ("de Habilidad MA03 OAH k", "identificar una regularidad numérica o geométrica"),
    ("de Habilidad MA03 OAH l", "usar tablas, esquemas y símbolos con precisión"),
    ("de Habilidad MA03 OAH m", "crear un problema coherente con una expresión"),
    ("de Habilidad MA03 OAH n", "pasar entre representaciones concretas, pictóricas y simbólicas"),
)
MATH_ATTITUDES = (
    ("de Actitud MA03 OAA A", "trabajo ordenado y metódico"),
    ("de Actitud MA03 OAA B", "búsqueda flexible y creativa de soluciones"),
    ("de Actitud MA03 OAA C", "curiosidad por las regularidades matemáticas"),
    ("de Actitud MA03 OAA D", "confianza progresiva en las propias capacidades"),
    ("de Actitud MA03 OAA E", "esfuerzo y perseverancia ante un desafío"),
    ("de Actitud MA03 OAA F", "expresión y escucha respetuosa de ideas"),
)
LANGUAGE_ATTITUDES = (
    ("de Actitud LE03 OAA A", "interés activo por leer y aprender de los textos"),
    ("de Actitud LE03 OAA B", "disposición a compartir ideas, experiencias y opiniones"),
    ("de Actitud LE03 OAA C", "expresión creativa mediante oralidad y escritura"),
    ("de Actitud LE03 OAA D", "trabajo riguroso y perseverante según el propósito"),
    ("de Actitud LE03 OAA E", "reflexión respetuosa sobre ideas e intereses propios"),
    ("de Actitud LE03 OAA F", "empatía con personas y personajes en su contexto"),
    ("de Actitud LE03 OAA G", "respeto por opiniones y puntos de vista diversos"),
)


def _p(topic, prior, vocabulary, anchor, misconception, focuses):
    return {"topic": topic, "prior": prior, "vocabulary": vocabulary, "anchor": anchor,
            "misconception": misconception, "focuses": focuses}


MATH = {
    "MA03 OA 01": _p("Conteo flexible hasta 1.000", "conteo por 2, 5, 10 y 100 en rangos menores", "intervalo, múltiplo, secuencia, ascendente, descendente", "recorridos numéricos que parten en 137, 248 y 615", "reiniciar en un múltiplo conocido y perder el punto de partida", ["Saltos de 5 desde cualquier número", "Decenas que cruzan centenas", "Centenas hacia adelante y atrás", "Patrones de 3 y 4 desde sus múltiplos"]),
    "MA03 OA 02": _p("Números hasta 1.000 en múltiples representaciones", "decenas, unidades y lectura de números hasta 100", "centena, numeral, forma concreta, pictórica y simbólica", "el número 406 construido con material base diez y un dibujo abreviado", "leer 406 como cuarenta y seis o ignorar el cero posicional", ["Leer centenas completas e incompletas", "Construir un numeral con centenas, decenas y unidades", "Traducir material a dibujo y símbolo", "Representaciones equivalentes y no canónicas"]),
    "MA03 OA 03": _p("Comparación y orden hasta 1.000", "comparación de números de dos cifras", "mayor, menor, igual, valor posicional, recta, intervalo", "tarjetas 398, 403, 430 y 304", "comparar cifras aisladas sin atender su posición", ["Comparar primero las centenas", "Resolver empates con decenas y unidades", "Ordenar sobre una recta numérica", "Encontrar números entre dos límites"]),
    "MA03 OA 04": _p("Cálculo mental aditivo hasta 100", "completar diez, dobles y descomposición", "descomponer, compensar, doble, asociar, operación inversa", "cálculos 38+27, 64-29 y 25+19+5", "aplicar una estrategia aunque los números no la favorezcan", ["Descomponer para sumar", "Completar la decena más cercana", "Usar dobles y casi dobles", "Sumar para resolver una resta", "Asociar sumandos estratégicamente"]),
    "MA03 OA 05": _p("Valor posicional hasta 1.000", "canje entre unidades y decenas", "unidad, decena, centena, posición, cifra, canje", "572 representado como 5C 7D 2U y como 4C 17D 2U", "confundir la cifra con el valor que ocupa", ["Diez decenas forman una centena", "Leer una tabla CDU", "Explicar el valor de cada cifra", "Realizar canjes no canónicos"]),
    "MA03 OA 06": _p("Adición y sustracción hasta 1.000", "valor posicional y problemas aditivos hasta 100", "sumando, minuendo, sustraendo, reserva, canje, estimación", "inventario escolar con 368 cuadernos, 247 entregados y nuevas cajas", "alinear cifras incorrectamente o aceptar el algoritmo sin estimar", ["Estrategias personales con material", "Adición de varios sumandos con reserva", "Sustracción con canje", "Problemas con operaciones sucesivas", "Estimar y comprobar algoritmos"]),
    "MA03 OA 07": _p("Familias de adición y sustracción", "hechos aditivos y sentido de parte-todo", "operación inversa, familia, término desconocido, comprobar", "la familia 286+157=443, 157+286=443, 443-286=157", "creer que cambiar el orden conserva también una resta", ["Construir una familia desde partes y total", "Comprobar una suma mediante resta", "Encontrar un término desconocido", "Resolver problemas inversos"]),
    "MA03 OA 08": _p("Multiplicación y tablas hasta 10", "conteo por grupos iguales y adición repetida", "factor, producto, grupo igual, arreglo, distributividad", "un arreglo de 7 filas por 6 columnas", "contar objetos uno a uno o invertir filas y columnas sin explicarlo", ["Grupos iguales y adición repetida", "Arreglos y conmutatividad", "Construir tablas 2, 5 y 10", "Usar distributividad para tablas difíciles", "Resolver y crear problemas multiplicativos"]),
    "MA03 OA 09": _p("División como reparto y agrupación", "tablas de multiplicar y sustracción repetida", "dividendo, divisor, cociente, reparto, agrupación, inversa", "24 fichas repartidas en 6 bandejas y agrupadas de 4 en 4", "confundir cuántos grupos hay con cuántos elementos recibe cada grupo", ["Repartir en partes iguales", "Formar grupos de tamaño dado", "Dividir mediante sustracción repetida", "Relacionar división y multiplicación", "Problemas de reparto y agrupación"]),
    "MA03 OA 10": _p("Problemas con dinero y cuatro operaciones", "suma, resta, multiplicación y división en contextos simples", "precio, total, vuelto, cantidad, reparto, unidad monetaria", "una feria escolar con precios de $120, $250 y $480 usando dinero didáctico", "elegir una operación por una palabra clave y no por la relación", ["Compras que requieren sumar", "Vuelto como diferencia", "Varias unidades del mismo precio", "Repartir un monto o una colección"]),
    "MA03 OA 12": _p("Patrones numéricos en tablas", "secuencias aditivas y conteo salteado", "regla, patrón, término, incremento, tabla, regularidad", "una tabla del 100 ampliada hasta 1.000 con saltos horizontales y verticales", "describir los números observados sin formular la regla", ["Reconocer reglas horizontales", "Explorar cambios verticales", "Registrar una regla con símbolos", "Crear y verificar un patrón"]),
    "MA03 OA 13": _p("Ecuaciones aditivas de un paso", "familias de operaciones y parte desconocida", "ecuación, igualdad, incógnita, término, verificar", "□+37=82 y 96-△=41", "tratar el signo igual como señal de calcular solo hacia la derecha", ["Mantener una igualdad con material", "Resolver una suma con término desconocido", "Resolver una resta con término desconocido", "Crear y comprobar una ecuación"]),
    "MA03 OA 14": _p("Localización en mapas y cuadrículas", "posición relativa y lectura de filas y columnas", "fila, columna, coordenada, recorrido, referencia, orientación", "un mapa simple de plaza con biblioteca, juego y acceso", "dar indicaciones dependientes de dónde mira quien escucha", ["Nombrar filas y columnas", "Ubicar mediante coordenadas", "Describir recorridos sin ambigüedad", "Comparar rutas y puntos de referencia"]),
    "MA03 OA 15": _p("Relación entre redes 2D y cuerpos 3D", "reconocimiento de figuras planas y cuerpos", "red, cara, arista, vértice, plegar, desplegar", "redes correctas e incorrectas de un cubo y una pirámide", "suponer que cualquier conjunto de caras puede plegarse", ["Desplegar un envase", "Reconocer redes posibles", "Construir un cuerpo desde una red", "Diseñar y justificar una plantilla"]),
    "MA03 OA 16": _p("Descripción de cuerpos geométricos", "clasificación por rasgos visibles", "cara plana, superficie curva, arista, vértice, base", "cubo, paralelepípedo, esfera, cono, cilindro y pirámide", "clasificar solo por parecido con objetos cotidianos", ["Distinguir superficies planas y curvas", "Contar caras, aristas y vértices", "Comparar prismas y pirámides", "Clasificar cuerpos con propiedades"]),
    "MA03 OA 17": _p("Traslación, reflexión y rotación", "orientación y figuras 2D", "trasladar, reflejar, rotar, eje, giro, congruencia", "huellas geométricas en mosaicos, señalética y tejidos", "confundir mover una figura con cambiar su tamaño o forma", ["Trasladar sin girar", "Reflejar respecto de un eje", "Rotar alrededor de un punto", "Reconocer transformaciones en el entorno"]),
    "MA03 OA 18": _p("Ángulos con referentes de 45° y 90°", "giros, esquinas y comparación de aberturas", "ángulo, vértice, lado, abertura, recto, estimar", "esquinas de papel, medias vueltas de aguja y aperturas de tijera", "comparar el largo de los lados en vez de la abertura", ["Descubrir ángulos en giros", "Construir un referente de 90°", "Estimar con 45° y 90°", "Clasificar ángulos del entorno"]),
    "MA03 OA 19": _p("Calendarios y líneas de tiempo", "secuencia de días, meses y acontecimientos", "fecha, duración, intervalo, simultáneo, antes, después", "calendario mensual y cronología de una investigación de plantas", "contar marcas en vez de intervalos o incluir dos veces el día inicial", ["Leer información de un calendario", "Calcular intervalos entre fechas", "Ordenar hechos en una línea de tiempo", "Interpretar escalas y acontecimientos", "Resolver una planificación temporal"]),
    "MA03 OA 20": _p("Hora, medias horas, cuartos y minutos", "hora y media hora en relojes analógicos", "hora, minuto, cuarto, media, manecilla, formato digital", "relojes que muestran 08:45, 12:30 y 17:05", "intercambiar las manecillas o leer 8:45 como ocho y cuarenta y cinco horas", ["Relacionar manecillas y escala", "Leer cuartos y medias horas", "Traducir entre reloj análogo y digital", "Calcular horarios cotidianos"]),
    "MA03 OA 21": _p("Perímetro de figuras regulares e irregulares", "medición de longitudes y suma", "perímetro, lado, unidad, contorno, regular, irregular", "bordes de cuadernos, mesas y polígonos en cuadrícula", "sumar medidas interiores o confundir perímetro con superficie", ["Recorrer y medir el contorno", "Perímetro en cuadrícula", "Cuadrados y rectángulos sin medir cada lado", "Resolver diseños con igual perímetro"]),
    "MA03 OA 22": _p("Peso en gramos y kilogramos", "comparación informal de peso", "gramo, kilogramo, balanza, estimar, referente, equivalencia", "paquetes rotulados de 250 g, 500 g y 1 kg", "inferir el peso por el tamaño o mezclar unidades", ["Comparar con una balanza", "Construir referentes de gramo y kilogramo", "Relacionar 1.000 g y 1 kg", "Estimar y luego medir", "Resolver problemas con medios y cuartos de kilogramo"]),
    "MA03 OA 23": _p("Encuestas, tablas y gráficos de barra", "conteo, categorías y pictogramas simples", "pregunta, categoría, frecuencia, tabla, barra, escala", "encuesta sobre formas de traslado usando categorías inclusivas", "cambiar categorías después de recoger datos o dibujar barras sin escala", ["Diseñar una pregunta clara", "Clasificar respuestas sin perder datos", "Construir una tabla de frecuencias", "Transformar la tabla en gráfico y concluir"]),
    "MA03 OA 24": _p("Datos de juegos aleatorios", "registro con marcas de conteo", "azar, resultado, frecuencia, mínimo, máximo, punto medio", "series de lanzamientos de dos dados y una moneda", "afirmar que un resultado futuro está asegurado por los anteriores", ["Registrar resultados sin omisiones", "Ordenar frecuencias", "Encontrar menor, mayor y punto medio", "Comparar dos experimentos aleatorios"]),
    "MA03 OA 25": _p("Pictogramas y gráficos de barra con escala", "tablas y gráficos sin escala", "pictograma, símbolo, escala, eje, frecuencia, intervalo", "un símbolo que representa 2 libros y barras graduadas de 5 en 5", "contar símbolos o cuadrículas sin aplicar la escala", ["Leer una escala antes de responder", "Construir un pictograma con equivalencias", "Completar barras a partir de datos", "Comparar dos representaciones", "Detectar gráficos engañosos"]),
    "MA03 OA 26": _p("Diagramas de puntos", "ordenar datos numéricos y usar rectas", "dato, eje, punto, frecuencia, moda, distribución", "mediciones repetidas de longitudes de hojas en centímetros", "ubicar un dato una sola vez aunque se repita", ["Preparar una escala numérica", "Registrar cada dato con un punto", "Leer frecuencias y valores extremos", "Comparar distribuciones sencillas"]),
}


LANGUAGE = {
    "LE03 OA 01": _p("Lectura oral fluida y expresiva", "decodificación de palabras frecuentes y lectura de frases", "precisión, pausa, entonación, ritmo, fraseo", "un cuento breve, una noticia infantil y un poema", "confundir fluidez con leer lo más rápido posible", ["Precisión antes que velocidad", "Pausas que construyen sentido", "Interrogación y exclamación", "Fraseo de grupos de palabras", "Lectura ensayada para una audiencia"]),
    "LE03 OA 02": _p("Estrategias de comprensión lectora", "localización de información y conversación sobre textos", "conectar, releer, visualizar, recapitular, preguntar, subrayar", "un artículo breve sobre picaflores y un relato de excursión", "usar todas las estrategias como lista sin decidir cuál resuelve la dificultad", ["Conectar sin abandonar el texto", "Releer el punto de quiebre", "Visualizar detalles comprobables", "Recapitular por segmentos", "Formular y responder preguntas", "Subrayar solo información relevante"]),
    "LE03 OA 03": _p("Repertorio literario amplio", "escucha y lectura de cuentos, poemas e historietas", "género, narrador, tradición, verso, viñeta, repertorio", "poemas, cuentos folclóricos y de autor, fábulas, leyendas, mitos, novelas e historietas", "leer géneros distintos como si todos funcionaran igual", ["Cuento folclórico y memoria cultural", "Cuento de autor y decisiones narrativas", "Fábula sin reducirla a una moraleja", "Leyenda y vínculo territorial", "Poema e imagen verbal", "Historieta y secuencia multimodal"]),
    "LE03 OA 04": _p("Comprensión profunda de narraciones", "reconstrucción de hechos explícitos", "secuencia, inferencia, personaje, ambiente, motivación, opinión", "un relato donde una niña devuelve un cuaderno encontrado antes de una tormenta", "opinar sobre un personaje sin citar acciones o palabras", ["Información explícita e implícita", "Secuencia y relaciones causales", "Personajes a partir de evidencia", "Ambiente y efecto en la acción", "Opiniones fundamentadas sobre hechos", "Juicio sobre personajes con matices"]),
    "LE03 OA 05": _p("Comprensión de poemas y lenguaje figurado", "reconocimiento de versos, rimas e imágenes", "verso, estrofa, hablante, comparación, personificación, imagen", "poemas breves sobre lluvia, mar y árboles sin exigir una interpretación única", "traducir cada imagen figurada literalmente o buscar una respuesta única", ["Escuchar ritmo e imágenes", "Construir sentido por estrofas", "Interpretar comparaciones", "Reconocer personificaciones", "Fundamentar una interpretación completa"]),
    "LE03 OA 06": _p("Comprensión de textos no literarios", "lectura de títulos, imágenes e información explícita", "propósito, título, subtítulo, índice, glosario, símbolo", "carta, biografía, instrucciones, artículo informativo y noticia", "leer solo el cuerpo e ignorar organizadores e imágenes", ["Reconocer propósito y formato", "Encontrar información con organizadores", "Inferir desde texto e ilustración", "Interpretar símbolos y pictogramas", "Relacionar información explícita e implícita", "Formar una opinión con respaldo"]),
    "LE03 OA 07": _p("Hábitos y gusto lector", "elección acompañada de textos", "preferencia, recomendación, registro, abandono justificado, variedad", "canasto con géneros, extensiones y formatos diversos", "medir el gusto lector solo por cantidad de páginas", ["Explorar antes de elegir", "Sostener una lectura breve", "Registrar una respuesta auténtica", "Recomendar con razones", "Ampliar el repertorio sin imponer gustos"]),
    "LE03 OA 08": _p("Uso responsable de la biblioteca", "cuidado de libros y búsqueda guiada", "catálogo, estante, signatura, préstamo, devolución, propósito", "biblioteca escolar o biblioteca de aula organizada por criterios visibles", "buscar al azar y dejar el material fuera de su sistema", ["Definir para qué se visita", "Orientarse en colecciones", "Elegir y registrar un recurso", "Cuidar, devolver y favorecer el uso común"]),
    "LE03 OA 09": _p("Búsqueda de información para investigar", "formulación de preguntas y uso de libros informativos", "pregunta, fuente, autor, fecha, palabra clave, confiabilidad", "investigación acotada sobre humedales locales con libro, atlas y sitio institucional", "copiar el primer resultado sin comprobar pertinencia ni procedencia", ["Convertir un tema en pregunta", "Elegir palabras clave y fuentes", "Localizar y registrar información", "Contrastar y comunicar sin copiar"]),
    "LE03 OA 10": _p("Significado por contexto y morfología", "uso de pistas cercanas en una oración", "contexto, raíz, prefijo, sufijo, hipótesis, comprobar", "palabras como submarino, desordenado, florista y luminoso en textos breves", "elegir cualquier significado conocido sin comprobarlo en la oración", ["Pistas antes y después de la palabra", "Raíces que conservan significado", "Prefijos que modifican", "Sufijos y familias de palabras", "Comprobar una hipótesis en el texto"]),
    "LE03 OA 11": _p("Diccionario y orden alfabético", "secuencia de letras y búsqueda por inicial", "entrada, palabra guía, definición, acepción, abreviatura", "diccionario infantil impreso o equivalente accesible", "buscar solo por la primera letra y elegir la primera acepción", ["Ordenar por primera y segunda letra", "Usar palabras guía", "Leer una entrada completa", "Elegir la acepción que corresponde al contexto"]),
    "LE03 OA 12": _p("Escritura frecuente y creativa", "producción de frases y textos breves", "voz, detalle, imagen, destinatario, borrador", "cuaderno de autor con poema, diario ficticio, carta y comentario lector", "convertir toda escritura creativa en un formato rígido corregido durante la idea", ["Capturar una observación", "Escribir desde una voz ficticia", "Transformar un recuerdo en escena", "Probar un formato nuevo", "Compartir y elegir qué revisar"]),
    "LE03 OA 13": _p("Narraciones con secuencia lógica", "relato de hechos con inicio y final", "inicio, conflicto, acción, desenlace, conector, coherencia", "cuento sobre una llave encontrada que obliga a tomar una decisión", "enumerar hechos sin relación causal o resolver el conflicto de golpe", ["Planificar situación y conflicto", "Ordenar acciones con causa", "Desarrollar personajes y ambiente", "Construir un desenlace coherente", "Revisar conectores y secuencia"]),
    "LE03 OA 14": _p("Artículos informativos en párrafos", "reunir datos sobre un tema", "tema, subtema, párrafo, explicación, definición, ejemplo", "artículo sobre cómo las plantas dispersan sus semillas", "acumular datos en una lista sin explicar cómo se relacionan", ["Delimitar tema y lector", "Agrupar datos por subtema", "Construir párrafos con idea central", "Explicar mediante ejemplos", "Revisar orden y precisión"]),
    "LE03 OA 15": _p("Textos funcionales con propósito", "reconocimiento de cartas, instrucciones y afiches", "propósito, destinatario, formato, mensaje, paso, llamado", "carta a la biblioteca, instrucciones de un juego, afiche y reporte de experiencia", "usar el mismo formato aunque cambien propósito y audiencia", ["Elegir formato según propósito", "Carta con mensaje claro", "Instrucciones comprobables", "Afiche con jerarquía visual", "Reporte de una experiencia"]),
    "LE03 OA 16": _p("Escritura manuscrita legible", "formación convencional de letras y separación de palabras", "legibilidad, tamaño, inclinación, espacio, margen, velocidad", "nota destinada a una pareja que debe poder leerla sin ayuda", "copiar muy lento y decorar letras sin mejorar la lectura", ["Diagnosticar qué dificulta leer", "Regular tamaño y apoyo en línea", "Separar palabras y renglones", "Mantener forma al aumentar velocidad", "Editar la presentación para un lector"]),
    "LE03 OA 17": _p("Planificación de la escritura", "generación oral de ideas", "propósito, destinatario, idea, selección, esquema, fuente", "encargo de escribir una recomendación para estudiantes de otro curso", "escribir de inmediato sin decidir qué debe comprender el lector", ["Definir propósito y destinatario", "Generar ideas por conversación e investigación", "Seleccionar información pertinente", "Ordenar un plan flexible"]),
    "LE03 OA 18": _p("Revisión y edición con propósito", "relectura de textos propios", "párrafo, conector, vocabulario, sugerencia, edición, versión", "borrador informativo con ideas repetidas, conectores imprecisos y puntuación insuficiente", "copiar en limpio sin tomar decisiones de revisión", ["Revisar primero el sentido global", "Separar y ordenar párrafos", "Mejorar conectores", "Variar vocabulario y redacción", "Usar retroalimentación de pares", "Editar ortografía y presentación"]),
    "LE03 OA 19": _p("Vocabulario nuevo en la escritura", "registro de palabras interesantes durante la lectura", "significado, contexto, matiz, sinónimo, precisión", "palabras recolectadas de un relato y un texto científico", "insertar palabras nuevas donde no corresponden para parecer más elaborado", ["Recolectar palabra y contexto", "Explicar significado y matiz", "Comparar con sinónimos cercanos", "Usar en una oración propia", "Integrar y revisar en un texto"]),
    "LE03 OA 20": _p("Artículos, sustantivos y adjetivos", "reconocimiento intuitivo de nombres y descripciones", "artículo, sustantivo, adjetivo, concordancia, precisión", "descripciones de un animal imaginario y un objeto extraviado", "agregar muchos adjetivos sin mejorar la precisión", ["Núcleo nominal en textos reales", "Artículos y concordancia", "Adjetivos que distinguen", "Combinar para cambiar significado", "Revisar una descripción ambigua"]),
    "LE03 OA 21": _p("Pronombres y referentes", "referencia a personas y objetos en oraciones", "pronombre, referente, repetición, ambigüedad, cohesión", "un relato donde Ana, Elisa y ella pueden confundirse", "reemplazar todos los sustantivos y volver ambiguo el referente", ["Reconocer qué sustantivo reemplaza", "Evitar repeticiones innecesarias", "Detectar referentes ambiguos", "Alternar nombre y pronombre", "Revisar cohesión en un párrafo"]),
    "LE03 OA 22": _p("Ortografía para facilitar comprensión", "mayúscula inicial y punto final", "mayúscula, nombre propio, párrafo, plural, enumeración, terminación", "mensaje escolar con errores que cambian pausas y palabras", "corregir signos aislados sin releer el sentido", ["Mayúsculas y puntos con propósito", "Punto aparte y organización", "Plurales de palabras en z", "Ge-gi y je-ji en familias", "Terminaciones cito-cita", "Coma en enumeraciones"]),
    "LE03 OA 23": _p("Escucha literaria de obras completas", "atención sostenida a relatos y poemas", "anticipar, episodio, imagen, reacción, conversación literaria", "lectura docente de cuento folclórico, fábula, mito, leyenda y poema", "interrumpir la experiencia para convertir cada fragmento en cuestionario", ["Prepararse para escuchar una obra", "Anticipar sin cerrar sentidos", "Sostener memoria entre episodios", "Conversar desde pasajes", "Responder creativamente a la obra"]),
    "LE03 OA 24": _p("Comprensión de textos orales", "seguir instrucciones y recuperar información escuchada", "propósito, información explícita, inferencia, conexión, pregunta, opinión", "explicación científica, noticia radial, instrucciones y documental breve", "recordar detalles sueltos sin reconocer propósito o relación", ["Identificar propósito y situación", "Registrar información explícita", "Conectar con experiencias pertinentes", "Preguntar para aclarar y profundizar", "Relacionar dos textos orales", "Inferir y opinar con evidencia"]),
    "LE03 OA 25": _p("Experiencia y lenguaje teatral", "juego dramático y escucha de relatos", "escena, personaje, diálogo, conflicto, gesto, público", "obra infantil presencial, grabada con autorización o representación del curso", "evaluar teatro solo por decorado o memorizar sin comprender la escena", ["Prepararse como público", "Observar cuerpo, voz y espacio", "Reconstruir conflicto y acciones", "Explorar una escena desde otro rol", "Crear una respuesta teatral breve"]),
    "LE03 OA 26": _p("Conversación grupal enfocada y respetuosa", "turnos básicos y expresión de opiniones", "foco, turno, pregunta, acuerdo, desacuerdo, empatía", "conversación sobre una decisión de un personaje con evidencia del texto", "esperar turno para repetir la propia idea sin escuchar", ["Preparar una idea con respaldo", "Mantener el foco", "Preguntar para aclarar", "Construir sobre lo dicho", "Discrepar sin descalificar", "Cerrar con acuerdos y preguntas abiertas"]),
    "LE03 OA 27": _p("Convenciones sociales según situación", "saludos y fórmulas de cortesía cotidianas", "registro, contexto, cortesía, presentación, permiso, reparación", "situaciones ficticias de aula, biblioteca, visita y desacuerdo", "repetir una fórmula sin ajustar tono, relación o propósito", ["Presentarse y presentar a otros", "Saludar según contexto", "Preguntar y pedir permiso", "Expresar opinión o sentimiento con respeto", "Agradecer, disculparse y reparar"]),
    "LE03 OA 28": _p("Exposición oral coherente y articulada", "relato oral breve sobre un tema conocido", "introducción, desarrollo, ejemplo, descripción, referente, apoyo", "presentación de dos minutos sobre un tema investigado", "leer diapositivas o enumerar datos sin una idea organizadora", ["Definir idea central y audiencia", "Ordenar introducción y desarrollo", "Incorporar ejemplos y descripciones", "Precisar referentes y vocabulario", "Ensayar voz, postura y apoyo visual"]),
    "LE03 OA 29": _p("Vocabulario nuevo en intervenciones orales", "uso contextual de palabras recién aprendidas", "contexto, precisión, paráfrasis, registro, autocorrección", "conversación sobre un texto que aporta términos como hábitat, migrar y refugio", "usar la palabra de memoria sin comprenderla o fuera del registro", ["Recuperar significado desde el texto", "Ensayar una paráfrasis", "Usar la palabra en conversación", "Ajustar registro y referente", "Autocorregir cuando no encaja"]),
    "LE03 OA 30": _p("Caracterización colaborativa de personajes", "lectura de diálogos y juego de roles", "personaje, intención, rasgo, voz, gesto, cooperación", "escena ficticia con personajes que desean soluciones diferentes", "reducir el personaje a una voz graciosa o estereotipo", ["Inferir intención desde el texto", "Construir voz y gesto sin caricatura", "Responder manteniendo el personaje", "Ensayar y retroalimentar en equipo"]),
    "LE03 OA 31": _p("Recitación expresiva de poemas", "lectura oral y memoria de textos breves", "verso, pausa, ritmo, entonación, volumen, expresión", "poema breve elegido entre opciones culturalmente diversas", "declamar fuerte y rápido sin comunicar las imágenes", ["Comprender antes de memorizar", "Marcar pausas y palabras clave", "Ensayar ritmo, voz y gesto", "Recitar, escuchar y revisar"]),
}

PILOT_MATH = _p(
    "Fracciones de uso común", "partición equitativa, comparación de cantidades y ubicación entre 0 y 1",
    "entero, parte igual, numerador, denominador, medio, tercio, cuarto",
    "tiras fraccionarias, conjuntos, rectas numéricas y repartos cotidianos",
    "aceptar partes desiguales o comparar fracciones construidas sobre enteros distintos",
    ["Una fracción nace al repartir en partes iguales", "La misma fracción en objetos, dibujos y símbolos", "Fracciones ubicadas entre 0 y 1", "Elegir fracciones para resolver situaciones", "Representar, explicar y comprobar fracciones"],
)

def _links(code: str, index: int, goal: str, discipline: str) -> list[dict[str, str]]:
    number = int(code.split(" OA ")[1])
    if discipline == "math":
        skill_code, skill = MATH_SKILLS[(number * 3 + index) % len(MATH_SKILLS)]
        attitude_code, attitude = MATH_ATTITUDES[(number + index * 2) % len(MATH_ATTITUDES)]
        return [
            {"code": skill_code, "type": "Habilidad", "application": f"Se observa al {skill} mientras se alcanza la meta «{goal}»."},
            {"code": attitude_code, "type": "Actitud", "application": f"Se promueve {attitude}; se valora explicar, comprobar y revisar, no la rapidez."},
        ]
    attitude_code, attitude = LANGUAGE_ATTITUDES[(number + index * 2) % len(LANGUAGE_ATTITUDES)]
    return [{"code": attitude_code, "type": "Actitud", "application": f"Se promueve {attitude} mediante una respuesta auténtica y observable ligada a la meta «{goal}»."}]


def _lesson(code: str, index: int, profile: dict, discipline: str) -> dict:
    focus = profile["focuses"][index]
    topic, anchor, misconception = profile["topic"], profile["anchor"], profile["misconception"]
    goal = ("resolveré y explicaré " if discipline == "math" else "comprenderé o produciré ") + focus.lower()
    modes = ("diagnosticar", "representar", "comparar", "analizar un error", "aplicar", "transferir")
    mode = modes[index % len(modes)]
    if discipline == "math":
        opening = f"Presenta {anchor} y plantea una decisión breve sobre «{focus.lower()}». Cada estudiante anticipa una respuesta y registra qué dato o representación usaría para comprobarla."
        model = f"Modela cómo {mode} el foco «{focus.lower()}»: nombra los datos, elige una representación, ejecuta una estrategia y vuelve al contexto para comprobar. Contrasta con este error frecuente: {misconception}."
        guided = f"En parejas resuelven dos variaciones de {anchor}; una conserva la estructura y otra cambia un dato decisivo. Comparan estrategias y acuerdan qué comprobación descarta una respuesta aparente."
        independent = f"Resuelve un caso nuevo de «{focus.lower()}» sin copiar el ejemplo. Incluye representación, procedimiento, respuesta con unidad y una comprobación independiente."
        ticket = f"Explica en dos pasos cómo resolverías un caso de «{focus.lower()}» y señala qué evidencia te permitiría detectar un error."
        evidence = f"Solución individual sobre {focus.lower()} con representación pertinente, razonamiento visible, unidad y comprobación."
        support = "Reduce el rango numérico o la cantidad de elementos, conserva la relación matemática y permite material concreto, tabla o dibujo antes del símbolo; luego retorna al desafío original."
        extension = f"Cambia una condición de {anchor}, predice el efecto y crea un contraejemplo que obligue a revisar la estrategia inicial."
        coordination = "El docente mantiene la demanda matemática; educación diferencial ajusta acceso, manipulación, lectura o forma de respuesta sin entregar la estrategia ni reducir el OA."
    else:
        opening = f"Presenta {anchor} sin explicar todavía el foco «{focus.lower()}». Cada estudiante observa, lee o escucha, registra una primera interpretación y marca la evidencia que la provoca."
        model = f"Piensa en voz alta para {mode} «{focus.lower()}»: explicita propósito, selecciona una pista textual u oral y revisa la interpretación frente a {misconception}."
        guided = f"Parejas trabajan con un segundo fragmento relacionado con {anchor}. Primero responden por separado, después comparan evidencias y mejoran una interpretación o producción sin uniformar sus voces."
        independent = f"Lee, escucha o produce una versión nueva vinculada con «{focus.lower()}». Responde al propósito, incorpora evidencia pertinente y explica una decisión de comprensión o comunicación."
        ticket = f"Completa una respuesta breve sobre «{focus.lower()}» y subraya la palabra, pasaje, rasgo o decisión que la sostiene."
        evidence = f"Respuesta individual de comprensión o producción sobre {focus.lower()}, con propósito reconocible, evidencia y revisión."
        support = "Acorta el fragmento, anticipa vocabulario imprescindible y permite lectura compartida, audio, dictado o respuesta gráfica; conserva la interpretación, producción o justificación central."
        extension = f"Introduce otro texto, audiencia o punto de vista relacionado con {anchor} y pide revisar la primera respuesta explicando qué cambió y por qué."
        coordination = "El docente enseña lectura, escritura u oralidad; educación diferencial y otros apoyos ajustan acceso y expresión sin reemplazar la interpretación ni homogeneizar la voz del estudiante."
    return {
        "title": focus,
        "purpose": f"Desarrollar {topic.lower()} mediante {focus.lower()}, con modelado disciplinar, práctica y revisión basada en evidencia.",
        "goal": f"Hoy {goal}.", "opening": opening, "model": model, "guided": guided,
        "independent": independent, "ticket": ticket,
        "materials": f"Recursos reutilizables para {anchor}; pizarra, cuaderno y alternativa sin conectividad. El docente verifica legibilidad, seguridad y disponibilidad antes de la clase.",
        "support": support, "extension": extension, "evidence": evidence,
        "criteria": ["responde al foco específico de la clase", "usa evidencia o representación disciplinar pertinente", "explica una decisión y comprueba o revisa su respuesta"],
        "next_step": "Avanza si la evidencia y la explicación coinciden; si no, identifica si la barrera está en el acceso, el concepto o la justificación y reenseña con un ejemplo diferente.",
        "short_version": "Conserva el desafío específico, un modelado breve, práctica conjunta, evidencia individual y ticket; reduce repeticiones, no la demanda del OA.",
        "home_task": "Busca o crea un ejemplo cotidiano seguro del foco y explícalo mediante dibujo, nota u oralidad. No requiere internet, impresión, compras ni revelar información familiar.",
        "complementary": [
            "Recuperación: vuelve a un caso con menos elementos y retorna después al desafío original.",
            f"Análisis de error: corrige un caso ficticio que muestra esta confusión: {misconception}.",
            "Transferencia: cambia una condición, audiencia o representación y revisa la respuesta inicial.",
        ],
        "difficulty_actions": [
            {"signal": "Responde antes de examinar datos, texto o representación", "action": "Pide señalar primero la evidencia que usará y anticipar cómo la comprobará.", "check": "La respuesta nueva cita o muestra evidencia pertinente."},
            {"signal": misconception.capitalize(), "action": support, "check": "Resuelve un caso nuevo sin repetir la confusión y explica la diferencia."},
            {"signal": "Completa la tarea, pero no puede explicar su decisión", "action": "Solicita comparar con una alternativa y nombrar el criterio decisivo.", "check": "La explicación permite reconstruir el razonamiento o intención."},
        ],
        "specialist_coordination": coordination,
        "transversal": _links(code, index, goal, discipline),
    }


def _build(code: str, table: dict, discipline: str) -> dict | None:
    profile = table.get(code)
    if not profile:
        return None
    subject_slug = "matematica" if discipline == "math" else "lenguaje-comunicacion"
    axis = "Números, álgebra, geometría, medición y datos" if discipline == "math" else "Lectura, escritura y comunicación oral"
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": f"{profile['topic']} se desarrolla como una progresión de decisiones observables. Parte de {profile['prior'][0].lower() + profile['prior'][1:]} y enfrenta explícitamente la confusión «{profile['misconception']}».",
        "prerequisites": profile["prior"], "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje {axis} · progresión interna en {len(profile['focuses'])} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/{subject_slug}/3-basico/{code.lower().replace(' ', '-')}",
        },
        "lessons": [_lesson(code, index, profile, discipline) for index in range(len(profile["focuses"]))],
    }


def build_sequence(code: str) -> dict | None:
    # MA03 OA 11 remains the manually curated pilot stored in developed-lessons.json.
    return _build(code, MATH, "math") or _build(code, LANGUAGE, "language")


def attach_pilot_transversals(code: str, lessons: list[dict]) -> None:
    if code != "MA03 OA 11":
        return
    for index, lesson in enumerate(lessons):
        lesson["transversal"] = _links(code, index, lesson["goal"].removeprefix("Hoy ").rstrip("."), "math")


def complete_pilot_sequence(sequence: dict) -> dict:
    """Preserve the hand-written MA03 OA 11 lessons and add the current contract."""
    generated = {
        "topic": PILOT_MATH["topic"],
        "pedagogical_explanation": "Las fracciones se construyen desde particiones equitativas y un entero explícito antes de coordinar dibujos, palabras, símbolos, recta numérica y problemas.",
        "prerequisites": PILOT_MATH["prior"],
        "vocabulary": PILOT_MATH["vocabulary"],
        "official_alignment": {
            "units": ["Eje Números y operaciones · progresión interna en 5 clases"],
            "unit_origin": "Organización pedagógica interna derivada del OA; no se presenta como unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in PILOT_MATH["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial",
            "source": "https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/3-basico/ma03-oa-11",
        },
    }
    base_lessons = [_lesson("MA03 OA 11", index, PILOT_MATH, "math") for index in range(5)]
    sequence.update({key: value for key, value in generated.items() if key not in sequence})
    sequence["lessons"] = [base | current for base, current in zip(base_lessons, sequence["lessons"])]
    attach_pilot_transversals("MA03 OA 11", sequence["lessons"])
    return sequence


def build_transversal_integration(item: dict) -> dict:
    is_math = item["subject_slug"] == "matematica"
    code = item["oa_code"]
    clean = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    lessons = []
    for index, (phase, phase_purpose) in enumerate(item["phases"]):
        context = ("un problema del OA disciplinar que se esté enseñando" if is_math else "un texto, conversación o producción del OA disciplinar que se esté enseñando")
        lessons.append({
            "title": f"{phase}: {clean}",
            "purpose": f"Integrar de forma observable la disposición o habilidad «{clean.lower()}» dentro de {context}, sin convertirla en una clase aislada.",
            "goal": f"Hoy demostraré {clean.lower()} mientras resuelvo una tarea con propósito.",
            "opening": f"Presenta dos respuestas ficticias ante {context}: una evidencia la habilidad o actitud y otra solo la nombra. El curso identifica conductas observables.",
            "model": f"Modela {phase_purpose} y verbaliza cuándo aparece «{clean.lower()}», qué decisión exige y qué evidencia permitiría observarla sin juzgar rasgos personales.",
            "guided": f"Durante {context}, parejas usan una pauta de una conducta observable y ofrecen retroalimentación descriptiva antes de un segundo intento.",
            "independent": f"Cada estudiante completa el desempeño disciplinar y anota o explica qué hizo para demostrar «{clean.lower()}».",
            "ticket": "Describe una acción observable que realizaste, la evidencia que produjo y qué ajustarías en el siguiente intento.",
            "materials": "Tarea disciplinar en curso, pauta breve y medio de respuesta accesible; no requiere materiales adicionales ni datos personales.",
            "support": "Anticipa la conducta observable, ofrece una pauta visual y permite ensayo; no reduzcas el OA disciplinar ni atribuyas la dificultad a la personalidad.",
            "extension": "Transfiere la misma habilidad o disposición a otra representación, texto, problema o rol y compara qué cambia.",
            "evidence": "Desempeño disciplinar y registro individual de una acción observable vinculada con la habilidad o actitud.",
            "criteria": ["mantiene el OA disciplinar", "hace observable la habilidad o actitud", "revisa su actuación con evidencia"],
            "next_step": "Si solo repite la formulación, vuelve a una conducta concreta; si la demuestra con autonomía, transfiérela a otro contexto.",
            "short_version": "Conserva modelado, desempeño disciplinar, observación individual y ticket.",
            "home_task": "Explica con un ejemplo ficticio cómo se vería esta habilidad o actitud. No requiere revelar experiencias familiares.",
            "complementary": ["Recuperación: elegir entre dos acciones cuál evidencia el foco y justificar.", "Práctica: aplicar la pauta en un segundo intento.", "Profundización: adaptar la conducta a otro contexto disciplinar."],
            "difficulty_actions": [
                {"signal": "Repite la actitud o habilidad sin mostrarla", "action": "Pide nombrar una acción, un momento y una evidencia.", "check": "Describe y ejecuta una conducta observable."},
                {"signal": "La integración desplaza el contenido", "action": "Vuelve a la meta del OA y observa el foco durante ese desempeño.", "check": "La evidencia demuestra contenido y transversalidad."},
                {"signal": "La pauta se usa para etiquetar", "action": "Reformula en conductas situadas y modificables.", "check": "La retroalimentación describe acciones, no identidades."},
            ],
            "specialist_coordination": "El docente conserva la responsabilidad disciplinar; los apoyos acuerdan accesos y observación sin sustituir respuestas ni convertir la pauta en diagnóstico.",
            "transversal": [],
        })
    return {"lessons": lessons}
