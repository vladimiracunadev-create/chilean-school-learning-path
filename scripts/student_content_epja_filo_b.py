"""Filosofía EPJA Media N1 y N2, módulo 2, OAD-05: reflexionar en torno al sentido de las acciones humanas a partir de textos filosóficos de ejemplo. Casos ficticios; todo en papel."""
from __future__ import annotations

from epja_filo_b_common import make_K

K = make_K()
O = "EPJA-FILO-NM1y2-OAD-05"

# ====================================================== clase 1
F = ("Ficha 1 (situaciones de ejemplo). Situación A: a Hernán, personaje ficticio, se le cierra el ojo cuando un insecto se acerca de golpe. "
     "Situación B: Hernán se levanta a las 5 de la mañana para abrir su taller, porque quiere que el trabajo quede listo para sus clientes. "
     "Situación C: Lucía, personaje ficticio, acompaña cada semana a una vecina mayor a su control de salud, aunque nadie se lo exige. "
     "Texto de ejemplo, escrito para esta ficha: «Una acción humana es lo que una persona hace sabiendo lo que hace y por alguna razón. Preguntar por su sentido es preguntar para qué la hace y por qué le parece valiosa.»")
K(O, 1, F,
  "Hoy aprenderé a distinguir una acción humana de un reflejo y a preguntar por su sentido: para qué se hace y por qué vale la pena.",
  ["Muchas cosas que hace nuestro cuerpo no las decidimos: parpadear, estornudar, sobresaltarnos. Son reflejos. En cambio, una acción humana es algo que una persona hace sabiendo lo que hace y con alguna intención. Levantarse temprano a abrir un taller, cuidar a alguien o cocinar para la familia son acciones, porque hay una persona que decide.",
   "Toda acción tiene una finalidad, que es aquello para lo que se hace. También se hace porque la persona le da un valor, es decir, le parece que vale la pena. El sentido de una acción reúne las dos cosas: para qué se hace y por qué se considera valiosa. Cuando alguien dice «esto no tiene sentido», suele decir que no ve ni el para qué ni el valor. Una acción puede ser un medio, es decir, algo que se hace para lograr otra cosa.",
   "La filosofía no parte de una respuesta cerrada, sino de preguntas bien planteadas y de razones que se pueden examinar. Preguntar por el sentido de nuestras acciones es una forma de pensar la propia vida sin que nadie nos diga qué responder. Quizá ya lo has hecho al preguntarte para qué te esfuerzas en lo que haces cada día."],
  [("acción humana", "algo que una persona hace sabiendo lo que hace y por alguna razón"), ("reflejo", "reacción del cuerpo que ocurre sin decidirla"), ("finalidad", "aquello para lo que se hace una acción"), ("valor", "lo que hace que algo parezca importante o digno de hacerse"), ("sentido", "el para qué de una acción junto con el valor que se le da")],
  [("Acción o reflejo", "Una persona ficticia cierra el ojo cuando una chispa salta cerca. ¿Es una acción humana o un reflejo?", ["El cierre del ojo ocurre sin decidirlo.", "No hay intención ni razón: es un reflejo."], "Un reflejo"),
   ("Finalidad", "Una vecina ficticia lleva cada mañana pan a una persona enferma. ¿Cuál es la finalidad de su acción?", ["La finalidad es aquello para lo que se hace.", "Lo hace para que la persona enferma tenga pan."], "Que la persona enferma tenga pan")],
  [("Creer que filosofar es tener una respuesta única y definitiva.", "Se confunde la filosofía con una lista de verdades ya resueltas.", "Filosofar es preguntar y dar razones; distintas personas pueden responder de forma razonada y distinta."),
   ("Pensar que toda cosa que hace el cuerpo es una acción humana.", "No se distingue lo que se decide de lo que ocurre solo.", "Una acción se hace sabiendo lo que se hace; el reflejo ocurre sin decidirlo.")],
  [("abc", "En Filosofía: una acción humana se distingue de un reflejo porque la acción", "se hace sabiendo lo que se hace y por alguna razón", "ocurre sin que la persona lo decida", "siempre produce un resultado exitoso", "Lo propio de la acción es la intención con que se realiza."),
   ("ab", "{F} ¿Cuál de las dos situaciones corresponde a un reflejo?", "La situación A, el ojo que se cierra", "La situación B, abrir el taller a las 5", "En A el cierre del ojo ocurre solo, sin decidirlo."),
   ("abc", "La finalidad de una acción es", "aquello para lo que se hace", "el cansancio que produce hacerla", "el nombre que recibe en el trabajo", "La finalidad responde a la pregunta «¿para qué lo hago?»."),
   ("abc", "{F} ¿Cuál es la finalidad de Hernán al levantarse a las 5?", "Que el trabajo esté listo para sus clientes", "Que el insecto se aleje de su cara", "Que la vecina llegue a su control", "La ficha dice que lo hace para tener el trabajo listo."),
   ("ab", "{F} ¿Qué dato muestra que la acción de Lucía no es una obligación impuesta?", "Que nadie se lo exige", "Que ocurre una vez por semana", "La ficha dice que lo hace aunque nadie se lo exige."),
   ("abc", "Preguntar por el sentido de una acción es preguntar", "para qué se hace y por qué vale la pena", "cuánto tiempo toma terminarla", "quién más la hace en el barrio", "El sentido reúne la finalidad y el valor que se le da."),
   ("abc", "Una persona ficticia amasa para tener pan, vende el pan para ganar un sueldo y busca el sueldo para sostener su casa. En esa cadena, ¿para qué se busca el sueldo?", "Para sostener su casa", "Para tener pan", "Para amasar mejor", "Según la cadena, el sueldo se busca para sostener la casa."),
   ("ab", "En una cadena de acciones, un medio es", "lo que se hace para lograr otra cosa", "lo que se logra al final de todo", "El medio sirve para alcanzar algo distinto de sí mismo."),
   ("abc", "Alguien dice: «Barro la vereda para que mi cuadra esté limpia». ¿Qué parte del sentido de la acción nombra?", "Su finalidad", "Su reflejo", "Su horario", "Dice para qué barre, y eso es la finalidad."),
   ("abc", "En Filosofía: ¿qué significa que una pregunta por el sentido no tenga una única respuesta?", "Que distintas personas pueden dar respuestas razonadas distintas", "Que cualquier respuesta sirve aunque no tenga razones", "Que no vale la pena pensar en ella", "Hay varias respuestas posibles, pero todas deben tener razones."),
   ("abc", "Ana dice que cuidar tiene sentido porque ayuda a otras personas. Beto dice que lo tiene porque le gusta hacer bien su trabajo. ¿Qué tienen en común sus respuestas?", "Cada una da una razón para valorar la acción", "Cada una niega que la acción tenga sentido", "Cada una describe un reflejo", "Ambas ofrecen un motivo por el cual la acción vale la pena."),
   ("ab", "Una acción que se hace por costumbre, sin pensar para qué, ¿puede examinarse con una pregunta filosófica?", "Sí, porque se puede preguntar para qué se hace y si vale la pena", "No, porque lo que se hace por costumbre ya no se puede pensar", "Preguntar por su sentido es posible aunque se haya vuelto rutina."),
   ("abc", "Un vecino dice que abrir el taller a las 5 es «solo un reflejo». ¿Qué respuesta es correcta?", "No lo es: Hernán decide levantarse y sabe para qué lo hace", "Sí lo es: se levanta sin pensar", "Sí lo es: ocurre todos los días", "Hay decisión e intención, así que es una acción y no un reflejo.")],
  ("abc", "Una persona se pregunta, al terminar el día: «¿Para qué hago todo esto?». ¿Qué tipo de pregunta se hace?", "Una pregunta por el sentido de sus acciones", "Una pregunta sobre un reflejo del cuerpo", "Una pregunta que se responde con una boleta", "Pregunta por el para qué y el valor de lo que hace."),
  [("En Filosofía: ¿qué es una acción humana?", "Algo que se hace sabiendo lo que se hace y por alguna razón", "Lo que la distingue es la intención de quien actúa."),
   ("¿Qué dos cosas reúne el sentido de una acción?", "Para qué se hace y por qué vale la pena", "Son la finalidad y el valor que se le da."),
   ("¿Es un reflejo una acción humana?", "No: ocurre sin decidirlo", "En el reflejo no hay intención ni razón.")],
  ("{F} Elige la situación B o C de la ficha, o inventa una acción de un personaje ficticio. Escribe: (1) la acción, (2) su finalidad, (3) un valor que podría darle sentido y (4) una pregunta filosófica sobre ella. No necesitas contar nada personal.",
   "Situación C. Acción: acompañar a una vecina al control. Finalidad: que llegue segura. Valor: el cuidado de otras personas. Pregunta: ¿cuidar a otro es una obligación o una elección que vale por sí misma?",
   ["describe una acción y no un reflejo", "nombra su finalidad con claridad", "explica un valor que le da sentido", "formula una pregunta abierta, no una de respuesta única"],
   ["texto breve con las cuatro partes numeradas"],
   ["confundir la acción con su resultado", "formular una pregunta que se responde con un dato"],
   "Revisa que la finalidad responda «¿para qué?» y el valor «¿por qué vale la pena?». Si la pregunta se responde con sí o no sin razones, pide que la reescriba con «¿por qué?» o «¿en qué caso?»."),
  "Escribe tres acciones de tu semana (puedes inventarlas) y marca cuáles son acciones y cuáles reflejos.",
  "Elige una acción de rutina y escribe dos finalidades posibles distintas para ella.")

# ====================================================== clase 2
F = ("Ficha 2 (texto de ejemplo: paráfrasis breve de una idea de Aristóteles, filósofo griego de la Antigüedad; la redacción es de esta ficha). "
     "«Todo lo que hacemos lo hacemos buscando algún bien. Algunos bienes se buscan para conseguir otros: se estudia para trabajar y se trabaja para vivir. "
     "Pero esa cadena no puede seguir sin fin: debe haber un bien que se busque por sí mismo y no para otra cosa. Ese bien es la felicidad, que no es un momento de gusto, sino una vida bien vivida en la que la persona ejercita sus capacidades de manera excelente.»")
K(O, 2, F,
  "Hoy practicaré, con apoyo, cómo leer un texto filosófico breve: encontrar su problema, su tesis, sus razones y su ejemplo.",
  ["Para leer un texto filosófico conviene hacerle cuatro preguntas. ¿Qué problema plantea? ¿Qué sostiene, es decir, cuál es su tesis? ¿Qué razones da? ¿Qué ejemplo usa? Esas preguntas ayudan a entender el texto antes de estar de acuerdo o en desacuerdo con él. Comprender bien es el primer paso para pensar con flexibilidad.",
   "Un argumento es un conjunto de razones que apoyan una conclusión. Las razones se llaman premisas y lo que se quiere mostrar es la conclusión. Palabras como «porque» suelen anunciar una premisa, y «por lo tanto» anuncia una conclusión. Una opinión sin razones no es un argumento: solo dice lo que alguien piensa, pero no muestra por qué.",
   "El texto de la ficha pregunta para qué hacemos lo que hacemos. Dice que muchas acciones son medios para otras y que la cadena debe terminar en un bien buscado por sí mismo: la felicidad. Una objeción es una razón en contra de una tesis. Si alguien objeta, no ataca a la persona: examina si las razones sostienen la conclusión."],
  [("tesis", "idea central que un texto sostiene"), ("premisa", "razón o dato en que se apoya una conclusión"), ("conclusión", "lo que se quiere mostrar con las premisas"), ("argumento", "conjunto de premisas que apoyan una conclusión"), ("objeción", "razón en contra de una idea")],
  [("Premisa o conclusión", "«Se trabaja para vivir, por lo tanto el trabajo es un medio». ¿Cuál parte es la conclusión?", ["«Por lo tanto» anuncia la conclusión.", "Lo que sigue a esas palabras es «el trabajo es un medio»."], "El trabajo es un medio"),
   ("Buscar el ejemplo", "«Todo oficio busca un bien; por ejemplo, el panadero busca que su pan quede bien hecho». ¿Cuál es el ejemplo?", ["Un ejemplo es un caso concreto.", "Viene después de «por ejemplo»."], "El panadero que busca que su pan quede bien hecho")],
  [("Tomar una opinión sin razones por un argumento.", "Se cree que decir algo con seguridad basta para probarlo.", "Un argumento muestra premisas que apoyan la conclusión."),
   ("Responder a una objeción atacando a quien la dice.", "Se confunde examinar una idea con desacreditar a la persona.", "Revisa si la razón de la objeción es buena y responde con otra razón.")],
  [("abc", "{F} ¿Qué problema plantea el texto?", "Para qué hacemos lo que hacemos y si hay un fin último", "Cómo ahorrar dinero para los estudios", "Quién debe gobernar la ciudad", "El texto se pregunta por el fin de nuestras acciones."),
   ("abc", "{F} ¿Cuál es el ejemplo que el texto usa?", "Se estudia para trabajar y se trabaja para vivir", "La felicidad es una vida bien vivida", "Todo lo que hacemos busca algún bien", "Las otras dos frases son afirmaciones generales, no un caso concreto."),
   ("ab", "En Filosofía: una premisa es", "una razón en que se apoya la conclusión", "la idea que se quiere mostrar al final", "La premisa sostiene la conclusión; no es la conclusión misma."),
   ("abc", "{F} ¿Cuál de estas frases del texto es una premisa?", "Esa cadena no puede seguir sin fin", "Ese bien es la felicidad", "La felicidad es un momento de gusto", "Es una razón en que se apoya la idea de un bien último."),
   ("abc", "{F} ¿Cuál es la conclusión del argumento del texto?", "Existe un bien buscado por sí mismo: la felicidad", "Estudiar es un gasto inútil de tiempo", "Todas las personas trabajan lo mismo", "Lo que el texto quiere mostrar es que hay un bien último."),
   ("ab", "{F} Que un bien se busque «por sí mismo» significa que", "se valora por sí mismo y no como medio para otra cosa", "se busca solo cuando falta dinero", "El texto lo opone a los bienes que se buscan para conseguir otros."),
   ("abc", "{F} Según el texto, la felicidad es", "una vida bien vivida en que se ejercitan las capacidades de modo excelente", "un momento pasajero de gusto", "un sueldo alto y estable", "El texto niega que sea un momento de gusto y la define como vida bien vivida."),
   ("ab", "Una expresión como «por lo tanto» suele anunciar", "una conclusión", "una premisa", "Esas palabras indican que lo que sigue se deduce de lo anterior."),
   ("abc", "Argumento de ejemplo: «Todo oficio busca algún bien. La costura es un oficio. Por lo tanto, la costura busca algún bien». ¿Cuál es la conclusión?", "La costura busca algún bien", "Todo oficio busca algún bien", "La costura es un oficio", "Es la frase que sigue a «por lo tanto»."),
   ("abc", "Una persona objeta: «Hay quien busca el dinero por sí mismo». ¿Qué hace esa frase respecto del texto?", "Cuestiona que la felicidad sea el único bien buscado por sí mismo", "Confirma que el texto no necesita razones", "Repite la conclusión del texto", "Es una razón en contra de la tesis del texto."),
   ("abc", "{F} ¿Cuál resumen es fiel al texto?", "Toda acción busca un bien y debe haber un bien final, la felicidad, entendida como vida bien vivida", "El texto dice que hay que trabajar mucho para ser feliz", "El texto dice que la felicidad es no hacer nada", "Conserva la tesis y las razones del texto; los otros agregan ideas ajenas."),
   ("abc", "Argumento de ejemplo: «Todo lo que busco, lo busco por otra cosa; esa otra cosa también, y así sin fin; por lo tanto, nada vale por sí mismo». ¿Qué parte del texto de la ficha contradice?", "Que debe haber un bien buscado por sí mismo", "Que se estudia para trabajar", "Que la felicidad no es un momento de gusto", "La conclusión del ejemplo niega justo lo que el texto afirma."),
   ("ab", "¿Qué hace que el texto de la ficha sea un argumento y no solo una opinión?", "Ofrece razones que apoyan una conclusión", "Está escrito por una persona del pasado", "El texto da razones; la antigüedad de su autor no lo hace argumento.")],
  ("abc", "Una temporera ficticia dice: «Cosecho para ganar, gano para mantener mi hogar, y mantener mi hogar lo busco por sí mismo». ¿Qué muestra su frase?", "Una cadena de medios que termina en un bien buscado por sí mismo", "Una acción que ocurre como reflejo", "Una opinión sin ninguna razón", "Cada paso es medio de otro hasta el último."),
  [("En Filosofía: ¿qué es la tesis de un texto?", "La idea central que sostiene", "La tesis es lo que el texto defiende."),
   ("¿Qué diferencia hay entre premisa y conclusión?", "La premisa apoya y la conclusión es lo que se muestra", "Las premisas son las razones y la conclusión es el resultado."),
   ("¿Cómo se responde a una objeción?", "Examinando su razón, sin atacar a la persona", "Se evalúa la razón y se contesta con otra razón.")],
  ("{F} Con el texto de la ficha, escribe: (1) el problema, (2) la tesis, (3) dos razones que la apoyan, (4) el ejemplo y (5) una objeción posible, con una frase que la responda.",
   "Problema: para qué hacemos lo que hacemos. Tesis: hay un bien último buscado por sí mismo. Razones: unos bienes se buscan por otros; la cadena no puede ser infinita. Ejemplo: estudiar para trabajar. Objeción: algunos buscan dinero por sí mismo; respuesta: el dinero sirve para comprar cosas, o sea es medio.",
   ["identifica el problema y la tesis sin confundirlos", "separa dos razones de la tesis", "cita el ejemplo del texto", "formula una objeción y la responde con una razón"],
   ["lista numerada de cinco puntos con la respuesta a la objeción"],
   ["mezclar la tesis con una razón", "responder a la objeción solo diciendo que está equivocada"],
   "Comprueba que la tesis sea una sola idea central. Si la respuesta a la objeción no da una razón, pide que agregue «porque»."),
  "Copia tres frases del texto y marca cuáles son premisas, cuál es la conclusión y cuál es el ejemplo.",
  "Escribe una objeción distinta a la de la ficha y una respuesta con razón.")

# ====================================================== clase 3
F = ("Ficha 3 (caso y textos de ejemplo, escritos para esta ficha; no pertenecen a ningún autor). Caso: Valentín, personaje ficticio, trabaja en el turno de noche de una panadería y a veces se pregunta si lo que hace tiene sentido. "
     "Texto A: «El sentido de una acción está en la obra: una acción vale cuando deja algo bien hecho que otras personas pueden usar.» "
     "Texto B: «El sentido de una acción está en el vínculo: una acción vale cuando cuida o fortalece la relación con otras personas.»")
K(O, 3, F,
  "Hoy aplicaré dos perspectivas sobre el sentido de las acciones a una situación de trabajo y escribiré una visión propia con razones.",
  ["Una misma situación se puede mirar desde distintas perspectivas. La perspectiva A de la ficha pone el sentido en la obra bien hecha. La perspectiva B lo pone en el vínculo con otras personas. Ninguna se descarta por cuestión de gusto: se examinan sus razones y lo que implican para la vida diaria, por ejemplo qué diría cada una de un turno de noche.",
   "Para aplicar una perspectiva a un caso se siguen pasos. Primero se describe la acción con precisión. Segundo, se nombra su finalidad. Tercero, se pregunta qué diría cada perspectiva sobre su sentido. Cuarto, se evalúa qué razones son más fuertes en este caso. Quinto, se formula una visión propia, con una razón y un ejemplo, y se reconoce una objeción posible.",
   "Elaborar una visión personal no es repetir un texto ni elegir al azar. Es asumir una posición y hacerse responsable de ella con razones. Puedes quedar con una de las perspectivas, combinarlas o plantear otra, siempre que expliques por qué. Asumir el riesgo de equivocarte es parte de pensar: una visión se puede revisar si aparece una razón mejor."],
  [("perspectiva", "modo de mirar un asunto, con sus razones propias"), ("obra", "algo hecho que queda y que otras personas pueden usar"), ("vínculo", "relación que une a una persona con otras"), ("visión personal", "posición propia sostenida con razones"), ("implicancia", "consecuencia que se sigue de una idea")],
  [("Qué dice cada texto", "Si el sentido está en la obra bien hecha, ¿qué podría decir esa perspectiva del trabajo de una costurera ficticia que deja un abrigo bien arreglado?", ["La perspectiva A valora la obra que queda.", "El abrigo arreglado queda para que otra persona lo use."], "Que su trabajo tiene sentido porque deja un abrigo bien arreglado que otra persona usa"),
   ("Una implicancia", "Si el sentido está en el vínculo, ¿qué importaría más en el turno de noche?", ["La perspectiva B valora la relación con otras personas.", "Importaría cómo el trabajo cuida o fortalece esa relación."], "Cómo su trabajo cuida a las personas que lo reciben")],
  [("Elegir una perspectiva sin dar razones.", "Se escoge por simpatía y no por argumentos.", "Una visión personal necesita al menos una razón y un ejemplo."),
   ("Creer que adoptar una perspectiva obliga a aceptar todas sus implicancias sin pensarlas.", "No se revisan las consecuencias de la idea.", "Examina qué se sigue de la perspectiva y decide si lo aceptas.")],
  [("abc", "{F} ¿Qué texto sostiene que el sentido está en la obra bien hecha?", "El texto A", "El texto B", "Ninguno de los dos", "Lo dice la primera línea del texto A."),
   ("ab", "{F} ¿Dónde pone el texto B el sentido de una acción?", "En el vínculo con otras personas", "En la obra que queda hecha", "El texto B habla de cuidar y fortalecer la relación con otras personas."),
   ("abc", "Aplicar una perspectiva a un caso exige primero", "describir la acción con precisión", "decidir quién tiene razón", "copiar el texto completo", "Sin describir la acción no se puede examinar su sentido."),
   ("abc", "{F} Valentín deja listo el pan para que lo compren al amanecer. ¿Qué perspectiva destaca más ese hecho?", "La perspectiva A, de la obra bien hecha", "La perspectiva B, del vínculo", "Ninguna puede hablar de él", "Un pan que queda hecho y que otros usan es una obra."),
   ("abc", "{F} Valentín deja una nota amable a su compañera del turno siguiente. ¿Qué perspectiva destaca más ese hecho?", "La perspectiva B, del vínculo", "La perspectiva A, de la obra", "Ninguna, porque una nota no es una acción", "Una nota amable cuida la relación con otra persona."),
   ("ab", "Una visión personal bien elaborada incluye", "una posición con razones y un ejemplo", "una frase solo con la palabra «creo»", "Sin razones y ejemplo no se puede examinar la posición."),
   ("abc", "Argumento de ejemplo: «Mi trabajo deja pan para el barrio. Una acción vale si deja algo útil. Por lo tanto, mi trabajo vale». ¿Cuál es la premisa general?", "Una acción vale si deja algo útil", "Mi trabajo vale", "Mi trabajo deja pan para el barrio", "Es la regla general de la que se deduce la conclusión."),
   ("abc", "En ese mismo argumento, ¿cuál es la conclusión?", "Mi trabajo vale", "Una acción vale si deja algo útil", "Mi trabajo deja pan para el barrio", "Es la frase que aparece después de «por lo tanto»."),
   ("abc", "Alguien objeta a la perspectiva A: «Hay trabajos que dejan obra y aun así nadie los valora». ¿Qué hace esa frase?", "Plantea un caso que pone en duda la perspectiva", "Confirma sin dudas la perspectiva A", "Cambia de tema a un reflejo", "Es una objeción con un caso concreto."),
   ("abc", "Una persona dice: «La perspectiva B es mejor porque sí». ¿Qué le falta?", "Una razón que apoye su posición", "Decirlo con más seguridad", "Una cita de un libro", "Le falta el «porque» con una razón real."),
   ("abc", "Alguien combina ambas perspectivas: «Una acción vale cuando deja algo bien hecho y además cuida a otros». ¿Es una visión posible?", "Sí, si explica por qué junta ambas ideas", "No, porque hay que elegir solo una", "No, porque una visión no puede tener razones", "Combinar es posible cuando se justifica."),
   ("ab", "Si aparece una razón mejor, una visión personal bien pensada", "puede revisarse y cambiarse", "debe mantenerse sin cambios", "Asumir una posición incluye estar dispuesto a revisarla."),
   ("abc", "{F} ¿Qué paso va justo después de nombrar la finalidad de la acción de Valentín?", "Preguntar qué diría cada perspectiva", "Formular la visión personal", "Elegir una perspectiva sin razones", "Es el tercer paso, antes de evaluar y de formular la visión.")],
  ("abc", "En una feria, un vendedor ficticio dice: «Mi trabajo tiene sentido porque mis clientes confían en mí». ¿Qué perspectiva usa?", "La del vínculo", "La de la obra", "Ninguna, es un reflejo", "Pone el sentido en la relación con otras personas."),
  [("En Filosofía: ¿qué es una perspectiva?", "Un modo de mirar un asunto con razones propias", "Cada perspectiva tiene razones que se pueden examinar."),
   ("¿Qué lleva una visión personal?", "Una posición con razones y un ejemplo", "Sin razones es solo una opinión."),
   ("¿Qué hace quien asume el riesgo de pensar?", "Sostiene una posición y está abierto a revisarla", "Pensar implica responsabilizarse de lo que se sostiene.")],
  ("{F} Escribe tu visión sobre qué da sentido al trabajo de Valentín. Elige la perspectiva A, la B, una combinación o una idea propia. Incluye una razón, un ejemplo y una objeción con tu respuesta. Puedes basarte solo en el caso ficticio.",
   "Creo que el sentido está en ambas cosas: el pan bien hecho es una obra (A), pero además alimenta a una comunidad (B). Ejemplo: un pan quemado no sirve aunque lo haga con cariño. Objeción: ¿y si nadie lo agradece? Respuesta: el sentido no depende del agradecimiento, depende de lo que el trabajo produce y cuida.",
   ["expresa una posición clara", "da al menos una razón", "usa un ejemplo concreto", "reconoce una objeción y la responde con una razón"],
   ["párrafo de seis a ocho líneas con posición, razón, ejemplo y objeción"],
   ["dar solo una opinión sin razón", "ignorar la objeción"],
   "Valora la calidad argumentativa y no cuál perspectiva elige. Si falta la razón, pide que agregue «porque». Si no hay objeción, pregunta qué diría alguien que piense distinto."),
  "Escribe qué diría la perspectiva A y qué diría la B sobre el trabajo de una costurera ficticia.",
  "Inventa una tercera perspectiva sobre el sentido de las acciones y escribe una razón a su favor.")
