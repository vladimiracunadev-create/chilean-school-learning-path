"""Artes Visuales EPJA Media N1 y N2, módulo 3, OAD-12: presentar y evaluar creaciones audiovisuales y performances con criterios (2 clases). Pautas y casos inventados; todo en papel."""
from __future__ import annotations

from epja_avis_c_common import K

O = "EPJA-AVIS-NM1y2-OAD-12"

# ====================================================== clase 1
F = ("Ficha 1 (pauta de ejemplo con tres criterios). A) Propósito expresivo: queda claro qué se quiere decir. "
     "B) Elementos del lenguaje audiovisual y corporal: planos, ángulos, luz, sonido, gesto y espacio se usan con intención. "
     "C) Relación entre ellos: los elementos se apoyan entre sí y apoyan el propósito. "
     "Niveles por criterio: 1 aún no se observa; 2 en desarrollo; 3 logrado; 4 destacado. Máximo total: 12 puntos. "
     "Orden de una presentación: 1) título y propósito; 2) mostrar o leer la obra; 3) contar dos decisiones; 4) recibir comentarios.")
K(O, 1, F,
  "Hoy aprenderé a presentar una creación audiovisual o una performance y a evaluarla con criterios de propósito, de elementos del lenguaje y de relación entre ellos.",
  ["Presentar es mostrar tu obra y explicar tus decisiones. Una presentación breve tiene cuatro momentos: decir el título y el propósito, mostrar o leer la obra, contar dos decisiones importantes (por ejemplo, por qué elegiste ese plano o esa luz) y recibir comentarios. Así quien escucha entiende qué buscabas y puede responder con más precisión.",
   "Evaluar es juzgar con criterios, no con simpatía. La pauta de la ficha tiene tres: el propósito expresivo, el uso de elementos del lenguaje audiovisual y corporal, y la relación entre ellos. Cada criterio se califica de 1 a 4 y se anota una razón con evidencia: «el plano general muestra que el personaje está solo». El puntaje sin razón no sirve para mejorar.",
   "La retroalimentación respetuosa dice qué funciona, qué se podría mejorar y cómo. Habla de la obra y no de la persona. Cuando evalúas la tuya, se llama autoevaluación. Recibir un comentario distinto del tuyo no es un ataque: es una pista para revisar. Evaluar también es una forma de aprender a mirar."],
  [("criterio", "aspecto que se mira al evaluar una obra"), ("evidencia", "dato concreto de la obra que respalda un juicio"), ("retroalimentación", "comentario que dice qué funciona y qué se puede mejorar"), ("autoevaluación", "evaluación que haces de tu propia obra")],
  [("Sumar una pauta", "Una obra de ejemplo recibe A = 3, B = 4 y C = 2 con la pauta de la ficha 1. ¿Cuántos puntos tiene de 12?", ["Se suman 3 + 4 + 2.", "El total es 9."], "9 de 12"),
   ("Escribir un comentario respetuoso", "La obra de ejemplo logra el propósito (A = 3) pero sus elementos no se relacionan bien (C = 2). Escribe un comentario con lo que funciona y una mejora.", ["Primero lo que funciona: el propósito se entiende.", "Luego una mejora: ajustar el sonido para apoyar la imagen."], "Funciona el propósito; mejora: sonido que apoye la imagen")],
  [("Evaluar es decir si me cae bien la persona.", "Se confunde evaluar con simpatía.", "Se evalúa la obra con criterios y evidencia, no a la persona."),
   ("Un puntaje alto basta, sin explicación.", "Se cree que el número sustituye la razón.", "Cada puntaje lleva una razón con evidencia para poder mejorar.")],
  [("abc", "En Artes Visuales: ¿qué es un criterio de evaluación?", "Un aspecto que se mira al evaluar una obra", "Una opinión sin razones", "El título de la obra", "Orienta qué se observa y cómo se juzga."),
   ("abc", "{F} ¿Qué mide el criterio A de la pauta?", "Que queda claro qué se quiere decir", "Que la obra dure exactamente 3 minutos", "Que haya muchos efectos", "Evalúa si el propósito expresivo queda claro."),
   ("abc", "{F} ¿Qué mide el criterio C?", "La relación entre los elementos y con el propósito", "El precio del equipo", "La edad de quien creó la obra", "Mide si los elementos se apoyan entre sí."),
   ("abc", "{F} ¿Cuál es el máximo total de la pauta?", "12 puntos", "9 puntos", "16 puntos", "Hay tres criterios con máximo 4: 3 × 4 = 12."),
   ("=", "{F} Una obra recibe A = 2, B = 3 y C = 1. ¿Cuántos puntos suma?", "2+3+1", "Se suman los tres criterios: 2 + 3 + 1 = 6 puntos.", " puntos"),
   ("abc", "{F} ¿Qué nivel tiene un criterio «logrado»?", "Nivel 3", "Nivel 1", "Nivel 4", "En la pauta, 3 corresponde a logrado."),
   ("abc", "{F} Según el orden de la presentación, ¿qué se hace primero?", "Decir el título y el propósito", "Recibir comentarios", "Contar las decisiones", "El primer momento presenta la obra y su propósito."),
   ("abc", "¿Cuál comentario usa evidencia?", "«El plano general muestra que el personaje está solo»", "«Me cae bien quien la hizo»", "«No me gusta, y punto»", "Cita un recurso concreto y su efecto."),
   ("ab", "Un comentario respetuoso sobre una obra dice", "«Funciona el propósito; podrías mejorar el sonido»", "«Esto es un desastre y no sabes nada»", "Reconoce lo logrado y propone una mejora sin atacar a la persona."),
   ("abc", "{F} Una obra tiene A = 4, B = 2 y C = 2. ¿Cuántos puntos le faltan para el máximo de 12?", "4 puntos", "8 puntos", "12 puntos", "Suma 8 y 12 − 8 = 4."),
   ("=", "{F} Una obra suma 7 puntos de 12. ¿Cuántos puntos le faltan para el máximo?", "12-7", "Se resta lo obtenido del máximo: 12 − 7 = 5 puntos.", " puntos"),
   ("abc", "Alguien califica con 4 porque «es mi amigo». ¿Qué corresponde?", "Volver a mirar con la pauta y citar evidencia", "Mantener el puntaje porque es amigo", "Dejar el espacio en blanco", "Evaluar con criterios exige razones, no afecto."),
   ("abc", "La autoevaluación sirve para", "mirar tu propia obra con la misma pauta y decidir mejoras", "reemplazar la opinión de todas las demás personas", "evitar mostrar la obra", "Aplica los mismos criterios a tu trabajo.")],
  ("abc", "En un taller comunitario, una persona presenta su nanometraje de 20 segundos sobre una feria. ¿Cuál es el orden de presentación más adecuado según la pauta?",
   "Título y propósito, mostrar la obra, contar dos decisiones y recibir comentarios", "Recibir comentarios, mostrar la obra y decir el título al final", "Solo mostrar la obra y no decir nada", "El orden de la ficha ayuda a que se entienda el propósito antes de evaluar."),
  [("En Artes Visuales: ¿qué es la retroalimentación?", "Un comentario sobre lo que funciona y lo que se puede mejorar", "Habla de la obra, no de la persona."),
   ("¿Qué es una autoevaluación?", "La evaluación de tu propia obra", "Se usan los mismos criterios con tu propia obra."),
   ("En la pauta de evaluación audiovisual: ¿cuántos criterios hay?", "Tres: propósito, elementos y relación", "Cada uno se califica de 1 a 4.")],
  ("{F} Imagina que presentas un nanometraje inventado de 15 segundos sobre un oficio. Escribe tu presentación en cuatro frases (título y propósito, qué se verá, dos decisiones y una pregunta para el público), y evalúa tu obra con A, B y C y una razón para cada puntaje.",
   "«Zapatero»: propósito: mostrar el cuidado en un oficio. Verán un detalle de manos y un plano general del taller. Decisiones: plano detalle para el martillo; luz cálida de tarde. Pregunta: ¿se entendió el cuidado? A = 3 (se entiende), B = 3 (planos y luz), C = 2 (el sonido no ayuda).",
   ["escribe las cuatro partes de la presentación", "califica A, B y C con una razón", "usa evidencia de la obra", "el texto es respetuoso con la propia obra"],
   ["texto de cuatro frases y una tabla con tres puntajes y razones"],
   ["poner puntajes sin razón", "olvidar las dos decisiones"],
   "Revisa que cada puntaje tenga evidencia y que el total esté bien sumado. Reconoce la honestidad al evaluarse."),
  "Escribe una pauta propia de tres criterios para una obra inventada y úsala para calificarla.",
  "Escribe un comentario respetuoso de cinco líneas para una obra que obtuvo 6 de 12.")

# ====================================================== clase 2
F = ("Ficha 2 (creación ficticia). «Pan para todos», nanometraje de 20 segundos de Teresa, personaje inventado, para invitar a una olla común. "
     "Plano 1 (8 s): plano general de ollas humeantes en un patio; luz natural. Plano 2 (6 s): plano detalle de manos que sirven con un cucharón; sonido del cucharón y risas muy bajas. "
     "Plano 3 (6 s): cartel final «Jueves, 13 h», que se alcanza a leer solo 1 segundo. "
     "Propósito de Teresa: «que las personas se sientan invitadas». Evaluación de compañeros (pauta con tres criterios, máximo 12): A = 4, B = 3, C = 3. "
     "Autoevaluación de Teresa: A = 4, B = 4, C = 2.")
K(O, 2, F,
  "Hoy aprenderé a evaluar una creación con una pauta, a escribir retroalimentación respetuosa y a decidir mejoras para mi obra.",
  ["Evaluar una obra completa tiene cuatro pasos. Primero, recordar el propósito de la persona que la creó. Segundo, revisar cada criterio con evidencia. Tercero, sumar el puntaje. Cuarto, escribir un comentario con lo que funciona, lo que se podría mejorar y una sugerencia concreta. Así la evaluación sirve para mejorar la obra.",
   "A veces la autoevaluación y la de otras personas no coinciden. Eso no significa que alguien se equivoque: puede indicar que quien creó la obra sabe lo que quiso hacer y el público solo ve el resultado. Mirar la diferencia ayuda a decidir qué ajustar. En la obra de ejemplo, el sonido muy bajo y el cartel que dura 1 segundo debilitan la relación entre los elementos.",
   "También se evalúa la presentación: ¿se entendió el propósito?, ¿se explicaron las decisiones?, ¿se recibieron los comentarios con respeto? Una persona que escucha y revisa su idea demuestra flexibilidad. Cuando tengas la oportunidad, presenta tu obra en tu comunidad o ante personas de confianza, sin obligación de mostrar nada personal."],
  [("evidencia", "dato concreto de la obra que respalda un juicio"), ("relación entre elementos", "cuánto se apoyan entre sí imagen, sonido, luz y gesto"), ("mejora", "cambio concreto que se propone tras evaluar"), ("flexibilidad", "disposición a revisar la propia idea con buenas razones")],
  [("Detectar un problema de relación", "Con la ficha 2, ¿qué problema debilita la relación entre elementos y propósito en el plano 3?", ["El propósito es que se sientan invitadas.", "El cartel se lee solo 1 segundo, así que no invita a asistir."], "El cartel dura 1 s y no se alcanza a leer"),
   ("Comparar puntajes", "¿Cuántos puntos suman los compañeros y cuántos Teresa?", ["Compañeros: 4 + 3 + 3 = 10.", "Teresa: 4 + 4 + 2 = 10."], "Ambos suman 10 de 12")],
  [("Si dos evaluaciones coinciden en el total, dicen lo mismo.", "Se mira solo la suma.", "Hay que comparar cada criterio: el mismo total puede ocultar distintas razones."),
   ("Una crítica debe ser dura para ser honesta.", "Se confunde franqueza con dureza.", "La honestidad se dice con respeto y con una sugerencia concreta.")],
  [("=", "{F} A la evaluación de compañeros, ¿cuántos puntos le faltan para el máximo de 12?", "12-4-3-3", "Los compañeros suman 4 + 3 + 3 = 10; faltan 12 − 10 = 2 puntos.", " puntos"),
   ("=", "{F} Si Teresa subiera su criterio C a 3 y mantuviera A y B, ¿cuántos puntos sumaría?", "4+4+3", "Se suman A = 4, B = 4 y C = 3: 11 puntos.", " puntos"),
   ("abc", "{F} ¿En qué criterio coinciden compañeros y Teresa con el mismo puntaje?", "En A, con 4 puntos", "En B, con 3 puntos", "En C, con 3 puntos", "Ambos pusieron A = 4; en B y C difieren."),
   ("abc", "{F} ¿En qué criterio Teresa se evaluó más baja que el grupo?", "En C", "En A", "En B", "Teresa puso C = 2 y los compañeros C = 3."),
   ("abc", "{F} ¿Qué elemento sonoro debilita la relación con el propósito?", "Las risas muy bajas, que apenas se oyen", "El cucharón, que suena muy fuerte", "El silencio total en el plano 1", "Un sonido que casi no se oye no refuerza la invitación."),
   ("=", "{F} Los planos duran 8, 6 y 6 segundos. ¿Cuántos segundos dura la obra?", "8+6+6", "Se suman las tres duraciones: 8 + 6 + 6 = 20 segundos.", " segundos"),
   ("abc", "{F} ¿Cuál comentario es respetuoso y útil?", "«La luz y el plano general invitan; el cartel necesita más segundos para leerse»", "«El cartel es un desastre»", "«Nada sirve»", "Reconoce un acierto y propone una mejora concreta."),
   ("=", "{F} El plano 1 se acorta a 6 segundos y el plano 3 pasa a durar 8 para alargar el cartel. ¿Cuántos segundos debe durar el plano 2 para que la obra siga en 20?", "20-6-8", "Se restan los otros dos planos del total: 20 − 6 − 8 = 6 segundos.", " segundos"),
   ("abc", "{F} Teresa dice que el cartel está bien porque lo escribió con cuidado. ¿Qué pregunta la ayuda a revisar?", "¿Se alcanza a leer en el tiempo que aparece?", "¿Quién lo dibujó primero?", "¿De qué color es el papel?", "Mira el efecto en el público, no solo el esfuerzo."),
   ("abc", "{F} El propósito de Teresa es «que se sientan invitadas». ¿Qué mejora lo apoya más?", "Subir el sonido de las risas y alargar el cartel", "Agregar un ruido fuerte de alarma", "Quitar el plano de las ollas", "Voces cálidas y un cartel legible invitan mejor."),
   ("abc", "Alguien recibe un comentario distinto del suyo. ¿Qué actitud demuestra flexibilidad?", "Revisar la obra con la evidencia y ajustar si hay razones", "Rechazar el comentario sin leerlo", "Retirar la obra", "Escuchar y evaluar razones permite mejorar."),
   ("ab", "{F} ¿Qué mejora es más pequeña y posible de hacer en un día?", "Alargar el cartel y subir el volumen de las risas", "Filmar de nuevo toda la obra con otro equipo", "Son ajustes concretos que no exigen rehacer todo."),
   ("abc", "Después de evaluar, ¿qué paso siguiente es coherente?", "Anotar tres mejoras, ensayar el cambio y presentar de nuevo", "Archivar la obra para siempre", "Cambiar de propósito sin avisar", "Mejorar y volver a mostrar cierra el ciclo de evaluar.")],
  ("abc", "Una persona de una agrupación vecinal evalúa una performance inventada: logra comunicar su idea (A = 4), los gestos son claros (B = 3) pero la voz tapa la música (C = 2). ¿Qué retroalimentación es más útil?",
   "«Tu idea se entiende y los gestos son claros; baja la voz o sube la música para que se apoyen»", "«Estuvo mal»", "«Eres muy buena persona»", "Reconoce los logros y señala un ajuste concreto en la relación."),
  [("En Artes Visuales: ¿qué se evalúa en la relación entre elementos?", "Si imagen, sonido, luz y gesto se apoyan entre sí", "Se mira cómo trabajan juntos en la obra."),
   ("¿Qué debe llevar un comentario útil?", "Un acierto, una mejora y una sugerencia concreta", "Así la persona sabe qué hacer."),
   ("¿Qué muestra revisar una idea al recibir un comentario?", "Flexibilidad", "Es una actitud importante al analizar y crear.")],
  ("{F} Evalúa la creación de la ficha con A, B y C (de 1 a 4) y una razón con evidencia para cada puntaje; suma los puntos; escribe un comentario respetuoso de tres líneas y una lista de dos mejoras posibles de hacer en un día.",
   "A = 4: se entiende que invita. B = 3: planos y luz se usan con intención. C = 2: el sonido y el cartel no ayudan. Total 9 de 12. Comentario: la invitación se siente en las ollas y la luz; falta que se oiga el sonido y se lea el cartel. Mejoras: subir las risas; alargar el cartel a 4 s.",
   ["califica A, B y C con evidencia", "suma bien los puntos", "escribe un comentario respetuoso con sugerencia", "propone dos mejoras posibles"],
   ["tabla con tres puntajes y razones, suma, comentario de tres líneas y dos mejoras"],
   ["poner puntaje sin razón", "proponer mejoras que obligan a rehacer toda la obra"],
   "Revisa que cada razón cite la ficha y que la suma sea correcta. Reconoce los comentarios que dicen qué hacer."),
  "Escribe tres diferencias posibles entre una autoevaluación y la evaluación del público y qué harías con ellas.",
  "Evalúa con la pauta de la ficha 1 una obra inventada de tu elección y compara con la autoevaluación de otra persona.")
