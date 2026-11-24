"""Artes Visuales EPJA Media N1 y N2, módulo 1, OAD-04: presentar los trabajos explicitando y argumentando ideas, proceso, resultados y decisiones (2 clases). Trabajos descritos, de ejemplo; todo en papel."""
from __future__ import annotations

from epja_avis_a_common import K

O = "EPJA-AVIS-NM1y2-OAD-04"

# ====================================================== OAD-04 clase 1
F = ("Ficha 11 (bitácora de ejemplo de un afiche de ejemplo llamado «Revisa tu llave»). Idea y propósito: invitar a las familias del barrio a revisar las llaves que gotean. "
     "Proceso: se hicieron tres bocetos y se eligió el segundo porque obtuvo el mayor puntaje en claridad. "
     "Decisión 1: fondo amarillo y letras negras, para lograr contraste. Decisión 2: témpera sobre cartulina, porque el afiche se colgará bajo techo. "
     "Decisión 3: un título de cuatro palabras, para que se lea desde 3 metros. "
     "Resultado: el título se lee desde 3 metros, pero la fecha de la jornada quedó pequeña. Dificultad: la témpera se corrió en un borde; se corrigió usando menos agua.")
K(O, 1, F,
  "Hoy aprenderé qué partes tiene la presentación de un trabajo visual y a argumentar las decisiones tomadas con razones claras.",
  ["Presentar un trabajo es contar a otras personas qué hiciste y por qué. Una buena presentación tiene cinco partes: la idea y el propósito, el proceso creativo, el resultado, las decisiones principales y lo que mejorarías. No se trata de justificar que el trabajo es bonito, sino de explicar cómo y para qué se hizo.",
   "Argumentar una decisión es dar una razón. Se usa una fórmula simple: «decidí X porque Y». Por ejemplo, «elegí letras negras sobre amarillo porque contrastan y se leen de lejos». Una razón sólida se apoya en el propósito o en una evidencia que se pueda ver. «Porque me gustó» es una opinión, no un argumento suficiente.",
   "También se habla con honestidad de las dificultades y de cómo se resolvieron, porque eso muestra el proceso. Quien escucha puede hacer preguntas, y responderlas con calma es parte de presentar. La bitácora, que son tus notas de pruebas y bocetos, es la fuente principal. Aquí el trabajo y la bitácora son inventados para el cuaderno."],
  [("presentación", "momento en que se explica a otras personas un trabajo, su proceso y sus decisiones"), ("argumentar", "dar razones que apoyan una decisión"), ("proceso creativo", "camino desde la idea hasta el resultado, con bocetos, pruebas y ajustes"), ("bitácora", "notas de pruebas, bocetos y decisiones de un trabajo")],
  [("Decidir y argumentar", "Una persona eligió cartulina como soporte para un afiche que irá bajo techo. ¿Cómo lo argumenta con la fórmula «decidí X porque Y»?", ["X es la decisión: cartulina.", "Y es la razón: irá bajo techo y no recibirá lluvia."], "Decidí usar cartulina porque el afiche irá bajo techo"),
   ("Argumento o gusto", "«Elegí amarillo porque me gusta» y «elegí amarillo porque contrasta con el negro». ¿Cuál argumenta mejor?", ["Una razón se apoya en el propósito.", "El contraste ayuda a leer."], "La segunda, porque se apoya en el contraste")],
  [("Contar solo el resultado y omitir el proceso.", "Se piensa que importa únicamente lo terminado.", "Incluye bocetos, pruebas, dificultades y ajustes."),
   ("Defender cada decisión con «porque me gusta».", "Se confunde opinión con argumento.", "Apoya cada decisión en el propósito o en una evidencia.")],
  [("abc", "En Artes Visuales: ¿qué es argumentar una decisión?", "Dar razones que la apoyan", "Repetirla varias veces con más fuerza", "Decir que es la mejor sin explicar", "Un argumento entrega razones que quien escucha puede revisar."),
   ("abc", "¿Cuál es una de las cinco partes de una presentación?", "Las decisiones principales y sus razones", "El precio del material", "El nombre del negocio que vende la pintura", "Presentar incluye idea, proceso, resultado, decisiones y mejoras."),
   ("abc", "{F} ¿Cuál era el propósito del afiche?", "Invitar a las familias a revisar las llaves que gotean", "Vender cartulinas en el barrio", "Mostrar un paisaje", "El propósito está al comienzo de la bitácora."),
   ("abc", "{F} ¿Por qué se eligió el segundo boceto?", "Porque obtuvo el mayor puntaje en claridad", "Porque era el más grande", "Porque era el último en hacerse", "La ficha lo explica en el proceso."),
   ("ab", "{F} ¿Qué razón se da para el fondo amarillo y las letras negras?", "Lograr contraste para que se lea", "Que eran los únicos colores disponibles", "La ficha dice que la decisión busca contraste."),
   ("abc", "{F} ¿Qué decisión se apoya en que el afiche se colgará bajo techo?", "Usar témpera sobre cartulina", "Usar un título de cuatro palabras", "Usar fondo amarillo", "Un lugar techado permite un soporte de papel."),
   ("=", "{F} El boceto elegido tuvo claridad 3, pertinencia 3 y factibilidad 2. ¿Cuántos puntos totales obtuvo ese boceto?", "3+3+2", "Se suman los puntajes de los tres criterios.", " puntos"),
   ("abc", "{F} ¿Qué dificultad apareció en el proceso y cómo se resolvió?", "La témpera se corrió en un borde y se usó menos agua", "El papel se rompió y se cambió el propósito", "No hubo dificultades", "Contar el problema y su solución muestra el proceso."),
   ("abc", "{F} ¿Qué mejoraría quien presenta este trabajo?", "Hacer más grande la fecha de la jornada", "Cambiar el título por uno de veinte palabras", "Quitar el amarillo", "El resultado señala que la fecha quedó pequeña."),
   ("ab", "Una persona dice solo: «el afiche quedó bonito». ¿Qué le falta a su presentación?", "Explicar el proceso, las decisiones y sus razones", "Nada, es suficiente", "Una presentación debe mostrar cómo y por qué se hizo, no solo cómo quedó."),
   ("abc", "Quien presenta recibe una pregunta que no esperaba. ¿Qué es lo más adecuado?", "Responder con calma lo que sabe y decir que lo revisará si no sabe", "Inventar una respuesta para no quedar mal", "Ignorar la pregunta", "Responder con honestidad da confianza a quien escucha."),
   ("abc", "{F} Un asistente dice: «el título se lee bien, pero no entiendo la fecha». ¿Qué respuesta argumenta mejor?", "Reconocer que la fecha quedó pequeña y explicar cómo la haría más grande", "Decir que la fecha no importa", "Culpar a la cartulina", "Reconoce el problema y lo conecta con una mejora concreta."),
   ("abc", "{F} Se debe explicar la decisión 3 usando la fórmula «decidí X porque Y». ¿Cuál es la formulación correcta?", "Decidí un título de cuatro palabras porque se lee desde 3 metros", "Decidí un título corto porque sí", "Decidí un título largo porque se ve elegante", "Une la decisión con una razón comprobable de la ficha.")],
  ("abc", "En la junta de vecinos le piden a una persona adulta que cuente cómo hizo el letrero de la sede. ¿Qué orden de presentación es más claro?", "Propósito, proceso con bocetos y pruebas, decisiones con razones, resultado y qué mejoraría", "Solo mostrar el letrero terminado", "Empezar por lo que costó y no hablar del propósito", "Ese orden permite entender el trabajo completo."),
  [("En Artes Visuales: ¿cuáles son las cinco partes de una presentación?", "Idea y propósito, proceso, resultado, decisiones y mejoras", "Juntas cuentan qué se hizo y por qué."),
   ("¿Cómo se argumenta una decisión?", "Con la fórmula «decidí X porque Y»", "La razón se apoya en el propósito o en una evidencia."),
   ("¿Qué se hace con una dificultad en el proceso?", "Se cuenta con honestidad y se explica cómo se resolvió", "Contar la dificultad muestra el aprendizaje del proceso.")],
  ("{F} Prepara la presentación de un trabajo tuyo, o de la ficha si no tienes uno: escribe la idea y el propósito, el proceso en tres pasos, tres decisiones con la fórmula «decidí X porque Y», el resultado, una dificultad y una mejora. Si usas la ficha, rotula tu texto como «presentación de ejemplo».",
   "Idea: afiche para revisar llaves. Proceso: tres bocetos, elegí el segundo; probé colores; pinté. Decidí letras negras porque contrastan; decidí cartulina porque va bajo techo; decidí un título corto porque se lee a 3 metros. Resultado: se lee de lejos. Dificultad: la témpera se corrió. Mejora: fecha más grande.",
   ["incluye las cinco partes de la presentación", "escribe tres decisiones con «decidí X porque Y»", "nombra una dificultad y una mejora"],
   ["texto de presentación de cinco partes con tres decisiones argumentadas"],
   ["usar «porque me gustó» como razón", "omitir el proceso"],
   "Revisa que cada razón se apoye en el propósito o en una evidencia. Si falta una parte, pregunta qué contaría ahí. Valora la honestidad sobre las dificultades."),
  "Escribe tres decisiones de un trabajo visual cualquiera con la fórmula «decidí X porque Y».",
  "Cuenta por escrito el proceso de algo que hayas hecho con las manos, con una dificultad y su solución.")

# ====================================================== OAD-04 clase 2
F = ("Ficha 12 (guion de ejemplo para presentar un afiche ante la junta de vecinos en 3 minutos, con las partes desordenadas). "
     "G4: decisiones con sus razones (50 segundos). G1: saludo y nombre del trabajo (20 segundos). G6: invitación a hacer preguntas (10 segundos). "
     "G3: proceso, con los bocetos y la elección (40 segundos). G2: propósito del afiche (30 segundos). G5: resultado y qué mejoraría (30 segundos). "
     "Preguntas de ejemplo del público: «¿por qué elegiste ese color?» y «¿se puede hacer más grande?».")
K(O, 2, F,
  "Hoy aprenderé a preparar y realizar la presentación de un trabajo ante un público real, ajustando el guion al tiempo y a quienes escuchan, y a usar los comentarios recibidos.",
  ["Para presentar ante la junta de vecinos o ante un grupo, conviene escribir un guion corto con las partes en orden y un tiempo para cada una. Si la presentación dura 3 minutos, o 180 segundos, se reparten los segundos: saludo, propósito, proceso, decisiones, resultado y preguntas. Se practica en voz alta una vez, con reloj.",
   "Se adapta el lenguaje a quienes escuchan: palabras simples, ejemplos del barrio y frases breves. Se muestra el trabajo o su foto, o un dibujo, y se apunta a lo que se explica. Se mira a las personas y se habla con un volumen que se escuche. No hace falta memorizar: bastan notas con palabras clave.",
   "Al terminar, se escuchan las preguntas y los comentarios sin tomarlos como ataque. Se anota lo que se puede mejorar y se agradece. Una presentación también es un aprendizaje: lo que dicen otras personas sirve para ajustar el siguiente trabajo. Si no se puede presentar ante un grupo, se puede practicar frente a una persona de confianza o escribirla como carta."],
  [("guion", "texto breve con las partes de una presentación en orden y con su tiempo"), ("público", "personas que escuchan o ven la presentación"), ("palabras clave", "palabras que recuerdan lo que se quiere decir"), ("retroalimentación", "comentarios de otras personas para mejorar un trabajo")],
  [("Repartir el tiempo", "Una presentación de 2 minutos tiene 4 partes iguales. ¿Cuántos segundos dura cada parte?", ["2 minutos son 120 segundos.", "120 dividido en 4 da 30."], "30 segundos"),
   ("Adaptar el lenguaje", "Quien escucha es una vecina que no conoce términos de arte. ¿Qué es mejor decir: «alto contraste cromático» o «las letras se distinguen bien del fondo»?", ["Hay que usar palabras simples.", "La segunda frase se entiende sin vocabulario técnico."], "Las letras se distinguen bien del fondo")],
  [("Leer el guion entero sin mirar a nadie.", "Se teme olvidar lo que se quiere decir.", "Usa notas con palabras clave y mira a las personas."),
   ("Tomar una pregunta como un ataque.", "Se confunde la crítica del trabajo con la crítica de la persona.", "Escucha, agradece y anota lo que sirve para mejorar.")],
  [("abc", "En Artes Visuales: ¿qué es un guion de presentación?", "Un texto breve con las partes en orden y su tiempo", "Una pintura para la sede vecinal", "Una lista de personas invitadas", "El guion ordena lo que se dirá y cuánto tiempo se usará."),
   ("abc", "{F} ¿Cuál es el orden correcto de las partes del guion?", "G1, G2, G3, G4, G5, G6", "G2, G1, G4, G3, G6, G5", "G6, G5, G4, G3, G2, G1", "Se saluda, se dice el propósito, el proceso, las decisiones, el resultado y se invita a preguntas."),
   ("=", "{F} ¿Cuántos segundos suman todas las partes del guion?", "20+30+40+50+30+10", "Se suman los segundos de las seis partes.", " segundos"),
   ("=", "{F} ¿Cuántos minutos son 180 segundos?", "180//60", "Se divide la cantidad de segundos entre 60.", " minutos"),
   ("abc", "{F} ¿Cuál es la parte más larga del guion?", "G4, las decisiones con sus razones, con 50 segundos", "G1, el saludo, con 20 segundos", "G6, las preguntas, con 10 segundos", "Es la parte con más segundos asignados."),
   ("ab", "Para presentar a personas que no conocen términos de arte, conviene usar", "palabras simples y ejemplos del barrio", "términos técnicos sin explicarlos", "El lenguaje debe ser comprensible para quienes escuchan."),
   ("abc", "{F} Una persona pregunta «¿por qué elegiste ese color?». ¿Qué respuesta es más adecuada?", "Explicar la razón del color con el propósito, por ejemplo el contraste", "Decir «porque sí»", "Cambiar de tema", "Responde con un argumento que conecta decisión y propósito."),
   ("abc", "{F} Otra persona dice «¿se puede hacer más grande?». ¿Cómo se toma esa pregunta?", "Como una sugerencia útil que se anota para el próximo trabajo", "Como un ataque personal", "Como algo sin importancia", "Los comentarios ayudan a ajustar el siguiente trabajo."),
   ("ab", "¿Qué conviene usar mientras se presenta?", "Notas con palabras clave", "Un texto completo para leer sin mirar a nadie", "Las palabras clave recuerdan lo central y dejan mirar al público."),
   ("abc", "Quien presenta se pone nervioso y olvida una parte. ¿Qué es lo más razonable?", "Respirar, mirar sus notas y continuar con la siguiente parte", "Abandonar la presentación", "Pedir disculpas todo el tiempo", "Retomar con las notas mantiene el hilo sin dramatizar."),
   ("abc", "{F} Se dispone de solo 2 minutos (120 segundos). ¿Qué ajuste del guion es más acertado?", "Acortar el proceso y las decisiones, conservando propósito, resultado y preguntas", "Eliminar el propósito", "Hablar más rápido sin cambiar nada", "Se acorta lo secundario y se conserva lo esencial."),
   ("abc", "Alguien no puede presentar ante un grupo. ¿Qué alternativa conserva el aprendizaje?", "Practicarla frente a una persona de confianza o escribirla como carta", "No hacer ninguna presentación", "Copiar la presentación de otra persona", "Hay formas distintas de comunicar un trabajo sin exponerse ante un grupo."),
   ("abc", "{F} Después de la presentación, el grupo propone hacer la fecha más grande. ¿Qué registro de retroalimentación es más útil?", "Fecha pequeña: agrandarla y usar un color oscuro en el próximo afiche", "Todo estuvo mal", "No anotar nada", "Anota el problema, la mejora y cuándo se aplicará.")],
  ("abc", "Una persona adulta debe presentar el mural de la junta de vecinos en una reunión de 5 minutos. ¿Cuál es el mejor plan?", "Escribir un guion con tiempos, practicarlo una vez en voz alta y llevar notas con palabras clave", "Improvisar sin preparar nada", "Leer un texto muy largo sin mirar al público", "El guion con tiempos y práctica permite explicar con claridad dentro del tiempo."),
  [("En Artes Visuales: ¿qué es un guion de presentación?", "Un texto breve con las partes en orden y su tiempo", "Ayuda a no olvidar nada ni pasarse del tiempo."),
   ("¿Cómo se adapta una presentación al público?", "Con palabras simples, ejemplos del barrio y frases breves", "Así se entiende sin vocabulario técnico."),
   ("¿Qué se hace con los comentarios recibidos?", "Se anotan y se usan para mejorar el próximo trabajo", "La retroalimentación forma parte del aprendizaje.")],
  ("{F} Escribe tu guion de tres minutos para presentar un trabajo tuyo (o el afiche de la ficha), con seis partes y los segundos de cada una, y las palabras clave de cada parte. Si puedes, practícalo en voz alta frente a una persona o un espejo y anota un comentario que recibas. Si no puedes presentar, deja el guion escrito y rotúlalo «guion de ejemplo» si usas la ficha.",
   "G1 saludo (20 s): «Buenas tardes, soy... presento mi afiche». G2 propósito (30 s): invitar a revisar las llaves. G3 proceso (40 s): tres bocetos y una elección. G4 decisiones (50 s): contraste, soporte y título corto. G5 resultado (30 s): se lee a 3 metros; mejora: fecha más grande. G6 preguntas (10 s). Comentario: «podría hablar más fuerte».",
   ["divide la presentación en seis partes con tiempos", "usa palabras clave y lenguaje simple", "anota un comentario o una mejora para la próxima vez"],
   ["guion con seis partes, tiempos y un comentario o una mejora"],
   ["no sumar bien los tiempos", "escribir un guion sin las decisiones y sus razones"],
   "Revisa que los tiempos sumen lo previsto. Si faltan las razones de las decisiones, pide que las agregue. Valora que practique en voz alta."),
  "Escribe el guion de 1 minuto de un trabajo visual que conozcas, con tres partes y sus segundos.",
  "Prepara tres respuestas a posibles preguntas del público sobre un trabajo tuyo.")
