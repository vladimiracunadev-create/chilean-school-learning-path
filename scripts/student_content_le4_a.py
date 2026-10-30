"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación, OA 01 (lectura oral fluida y expresiva).

Todos los textos son originales y breves; cada ejercicio trae el texto que necesita.
Aquí se definen también los ayudantes `L`, `E`, `task` que reutilizan los otros módulos le4_*.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "LE04 OA 01"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


def n_words(text):
    """Cuenta las palabras de un texto separado por espacios (los signos no cuentan como palabras)."""
    return str(len(text.split()))


# ------------------------------------------------------------------ OA 01
L(OA1, 1,
  "Este cuaderno, lápiz y los textos escritos en cada ejercicio. Si quieres, un reloj con segundero.",
  "Aprenderé a leer en voz alta diciendo cada palabra completa y correcta, también las largas y difíciles, y a subir la velocidad solo cuando ya leo sin errores.",
  ["Leo oraciones en voz alta.", "Sé que cambiar una letra puede cambiar la palabra."],
  ["Leer con precisión es decir cada palabra tal como está escrita, sin cambiar, quitar ni agregar letras o sílabas. En cuarto básico aparecen más palabras largas, como «transparente» o «extraordinario». Para no tropezar, léelas por partes: trans-pa-ren-te, y luego dilas completas.",
   "La velocidad adecuada es la que te deja decir bien todas las palabras y que quien te escucha entienda. Leer muy rápido hace que te comas sílabas; leer muy lento hace que se pierda la idea de la oración. Primero se busca la precisión y después se acelera de a poco.",
   "Puedes medir tu precisión: cuentas las palabras del texto, cuentas las que leíste mal y restas. Si notas un error, vuelve a la palabra y léela otra vez. Eso se llama autocorrección y los buenos lectores la usan siempre."],
  [("precisión", "leer cada palabra completa y sin cambiarla"), ("velocidad", "qué tan rápido se lee"), ("autocorrección", "volver a una palabra para decirla bien"), ("sílaba", "cada golpe de voz con que se pronuncia una palabra")],
  [("Dividir una palabra larga", "Para leer «extraordinario» sin errores, ¿cómo la separas en sílabas?", ["Digo la palabra despacio y marco cada golpe de voz.", "Suena ex-tra-or-di-na-rio.", "Leo cada parte y luego las uno."], "ex-tra-or-di-na-rio (6 sílabas)"),
   ("Calcular palabras bien leídas", "Un texto tiene 80 palabras y te equivocas en 5. ¿Cuántas leíste bien?", ["Cuento las palabras del texto: 80.", "Cuento los errores: 5.", "Resto: 80 − 5 = 75."], "75 palabras bien leídas")],
  [("Leer muy rápido para terminar primero, aunque se cambien sílabas.", "Se cree que leer bien es leer rápido.", "Baja la velocidad hasta decir cada palabra completa."), ("Seguir leyendo aunque notaste el error.", "Da vergüenza volver atrás.", "Vuelve a la palabra y léela de nuevo: es autocorrección.")],
  ([E("¿Cuántas sílabas tiene la palabra «transparente» (trans-pa-ren-te)?", "4", "Se cuentan los golpes de voz: trans, pa, ren, te."),
    E("Alguien lee «cabra» como «cobra». ¿Se leyó con precisión?", "No", "Cambió una vocal y ahora nombra otro animal."),
    E("¿Qué debe ir primero al aprender a leer bien en voz alta: la precisión o la velocidad?", "La precisión", "Si se cambian palabras, leer rápido no sirve.")],
   [E("Una niña lee «extraordinario» como «extraordinaro». ¿Qué letra de la palabra original no leyó?", "i", "La palabra original termina en -rio y ella dijo -ro, sin la i."),
    E("¿Cómo se llama volver a una palabra mal leída para decirla bien?", "Autocorrección", "Es la acción de corregirse uno mismo al leer."),
    E("Un lector va muy rápido, pero cambia varias palabras. ¿Su lectura es precisa?", "No", "Precisa es la que dice cada palabra como está escrita.")],
   [arith("Lees un texto de 90 palabras y te equivocas en 6. ¿Cuántas palabras leíste bien?", "90-6", "Se restan los errores del total de palabras."),
    E("El texto dice «La pastora conducía las ovejas». Alguien lee «La pastora conducía las orejas». ¿Qué palabra se leyó mal?", "ovejas", "Se leyó «orejas» en lugar de «ovejas»."),
    arith("Una lectora lee 240 palabras en 2 minutos. ¿Cuántas palabras lee por minuto, si lee igual de rápido todo el tiempo?", "240//2", "Se divide el total de palabras por los minutos.")],
   [E("Sofía lee un texto de 60 palabras en un minuto con 9 errores. Tomás lo lee en dos minutos con 1 error. ¿Quién leyó con más precisión?", "Tomás", "Tuvo un solo error, mientras que Sofía tuvo nueve."),
    E("Tomás se equivocó en una palabra, se detuvo y la leyó bien. Sofía siguió con el error. ¿Quién usó la autocorrección?", "Tomás", "Volver a la palabra para decirla bien es autocorregirse.")],
   [E("Lee y cuenta las palabras de esta oración: «El carpintero lijó la tabla con mucho cuidado.»", n_words("El carpintero lijó la tabla con mucho cuidado."), "Se cuenta cada palabra separada por espacios."),
    arith("Lees «El carpintero lijó la tabla con mucho cuidado.» y te equivocas en 2 palabras. ¿Cuántas palabras leíste bien?", "8-2", "La oración tiene 8 palabras; se restan los errores del total.")]),
  [E("El aviso del curso dice «El viernes habrá reunión de apoderados». Un niño lo lee como «El lunes habrá reunión de apoderados». ¿Se entiende lo mismo?", "No", "Cambió el día y la gente podría llegar cuando no corresponde.")],
  [E("¿Cómo se llama leer cada palabra completa y sin cambiarla?", "Precisión", "Ese es el nombre de leer sin cambiar las palabras."),
   E("Si dices mal una palabra, ¿qué conviene hacer?", "Volver y leerla de nuevo", "Eso se llama autocorrección."),
   E("¿Cuántas palabras tiene «Hoy comimos pan fresco»?", "4", "Las palabras son Hoy, comimos, pan y fresco.")],
  ("Lee en voz alta, despacio, estas tres oraciones: 1) «La pastora conducía las ovejas por el sendero.» 2) «El científico observó una hormiga transparente.» 3) «Mi abuelo cuenta historias extraordinarias.» Pide a otra persona que marque en un papel cada palabra que cambies. Cuenta tus errores y calcula cuántas palabras leíste bien (entre las tres hay 19 palabras).", "Si tuve 1 error, leí bien 19 − 1 = 18 palabras. Me equivoqué en «extraordinarias», que leí «extraordinaria», y la corregí.", ["lee las tres oraciones completas", "cuenta los errores", "calcula las palabras bien leídas", "corrige una palabra que dijo mal"], ["nota con el número de errores", "lectura ante otra persona"], ["leer rápido y cambiar sílabas", "no volver atrás ante un error"], "Anota qué sílabas se te escapan con más frecuencia y practica esas palabras antes de subir la velocidad."),
  "Lee dos veces en voz alta una página de un libro que te guste y cuenta los errores de cada vez.",
  "Escribe tres palabras que cambien de sentido si se cambia una sola letra (como cabra y cobra) y léelas con cuidado.")

L(OA1, 2,
  "Este cuaderno, lápiz y los textos escritos en cada ejercicio.",
  "Aprenderé a respetar las pausas que marcan la coma, el punto, los dos puntos y la raya de diálogo, para que lo que leo en voz alta se entienda.",
  ["Sé leer oraciones con precisión.", "Reconozco la coma y el punto."],
  ["La coma (,) pide una pausa corta. Separa los elementos de una lista, como en «Compré pan, leche y queso», y también el nombre de la persona a quien se le habla: «Ana, ven acá». El punto seguido (.) pide una pausa más larga y separa oraciones dentro del mismo párrafo. El punto aparte cierra un párrafo.",
   "Los dos puntos (:) avisan que viene algo importante, como una lista o lo que alguien dijo: «Traje tres cosas: lápiz, goma y regla». La raya (—) en un diálogo indica que habla un personaje: «—Buenos días —dijo el profesor». Al leer, la voz cambia cuando habla el personaje.",
   "Si no haces las pausas, el texto suena atropellado y se confunde. La coma puede cambiar el sentido: «Come, Ana» le habla a Ana, y «Come Ana» dice que Ana come. Antes de leer, mira los signos y decide dónde irán tus pausas."],
  [("coma", "signo (,) que pide una pausa corta"), ("punto seguido", "punto que separa oraciones en un mismo párrafo"), ("dos puntos", "signo (:) que anuncia una lista o lo que alguien dice"), ("raya", "signo (—) que marca lo que dice un personaje en un diálogo")],
  [("Contar elementos de una lista", "En «Compré pan, leche, queso y té», ¿cuántos alimentos hay y cuántas comas?", ["Los alimentos son pan, leche, queso y té: 4.", "Las comas están después de pan y de leche: 2.", "Antes de té va «y», no coma."], "4 alimentos y 2 comas"),
   ("Cambiar el sentido con la coma", "Compara «Come, Ana» y «Come Ana». ¿En cuál se le habla a Ana?", ["En «Come, Ana» la coma separa el nombre.", "Eso muestra que a Ana se le habla.", "En «Come Ana» Ana es quien come."], "En «Come, Ana»")],
  [("Leer sin detenerse en ninguna coma ni punto.", "No se mira la puntuación.", "Antes de leer, marca con lápiz suave las comas y los puntos."), ("Hacer una pausa larga en cada coma.", "Se confunde la coma con el punto.", "En la coma, pausa corta; en el punto, pausa más larga.")],
  ([E("En «Pedro, ven aquí.» ¿qué signo marca la pausa corta?", "La coma", "La coma está después de Pedro y pide una pausa corta."),
    E("¿Qué signo cierra la oración «Hoy llueve.»?", "El punto", "El punto cierra la oración."),
    E("¿Cuántas comas tiene «Compré pan, leche, queso y té.»?", "2", "Hay una coma después de pan y otra después de leche.")],
   [E("¿Qué pausa es más larga: la de la coma o la del punto?", "La del punto", "El punto cierra la oración y pide una pausa más larga."),
    E("En «Traje tres cosas: lápiz, goma y regla.» ¿qué signo anuncia la lista?", "Los dos puntos", "Los dos puntos avisan que viene una lista."),
    E("En «—Buenos días —dijo el profesor.» ¿qué signo muestra que alguien está hablando?", "La raya", "La raya marca lo que dice un personaje.")],
   [E("Pon la coma que falta: «Tomás vamos al parque.»", "Tomás, vamos al parque.", "La coma separa el nombre de la persona a quien se habla."),
    E("Divide en dos oraciones: «Llegó la lluvia las calles se mojaron». ¿Después de qué palabra va el punto?", "lluvia", "La primera idea termina en «lluvia»."),
    E("Lee «Rosa corre, salta y ríe.» ¿Cuántas acciones hace Rosa?", "3", "Las acciones son corre, salta y ríe.")],
   [E("«Llama, Ana.» y «Llama Ana.» ¿En cuál de las dos Ana es quien llama?", "En «Llama Ana.»", "Sin coma, Ana es quien hace la acción de llamar."),
    E("Al leer «—Vamos —dijo Pía—, ya es tarde.» ¿quién habla: Pía o el narrador?", "Pía", "La raya marca lo que dice Pía; «dijo Pía» es el aviso del narrador.")],
   [E("Lee «Ayer compré tres frutas: manzanas, peras y uvas.» ¿Cuántas frutas se nombran?", "3", "Las frutas son manzanas, peras y uvas."),
    E("Une con punto y mayúscula estas dos ideas: «el perro ladra» y «el gato duerme».", "El perro ladra. El gato duerme.", "Cada idea es una oración: termina con punto y la siguiente empieza con mayúscula.")]),
  [E("Una receta dice «Mezcla estos ingredientes: harina, azúcar y leche.» ¿Cuántos ingredientes se mezclan?", "3", "Los ingredientes son harina, azúcar y leche.")],
  [E("¿Qué signo hace una pausa corta?", "La coma", "La coma pide una pausa corta."),
   E("¿Qué signo anuncia una lista?", "Los dos puntos", "Los dos puntos avisan que viene una enumeración."),
   E("¿Cuántos puntos tiene «Llueve. Hace frío. Me abrigo.»?", "3", "Cada oración termina con un punto.")],
  ("Lee en voz alta este texto respetando las pausas. Cuenta mentalmente uno en cada coma y uno, dos en cada punto. «Ayer fui a la feria. Compré estas cosas: tomates, lechugas y zanahorias. Después, volví a casa.» Luego escribe cuántas comas, cuántos puntos y cuántos signos de dos puntos tiene.", "El texto tiene 3 puntos, 2 comas (después de tomates y de «Después») y 1 signo de dos puntos (después de «cosas»).", ["hace pausa corta en las comas", "hace pausa más larga en los puntos", "cuenta bien los signos"], ["lectura en voz alta", "conteo escrito"], ["leer sin pausas", "pausa larga en cada coma"], "Pide a quien te escuche que levante un dedo en cada pausa y comparen con los signos del texto."),
  "Lee en voz alta un párrafo de un libro y marca con lápiz suave cada coma y cada punto antes de leer.",
  "Escribe un diálogo de dos líneas con raya y léelo cambiando la voz para cada personaje.")

L(OA1, 3,
  "Este cuaderno, lápiz y las oraciones escritas en cada ejercicio.",
  "Aprenderé a leer con entonación las preguntas, las exclamaciones y los puntos suspensivos, cambiando la voz como lo piden los signos.",
  ["Respeto la coma y el punto al leer.", "Reconozco los signos de interrogación y de exclamación."],
  ["Los signos de interrogación (¿?) encierran una pregunta. En español se escriben dos: uno que abre y otro que cierra. Los signos de exclamación (¡!) encierran emociones: alegría, susto, enojo o sorpresa. Se leen con más fuerza, como en «¡Qué susto me diste!».",
   "Los puntos suspensivos (...) son tres puntos seguidos. Indican que la voz se queda en suspenso, porque falta algo, hay duda o se espera algo: «Abrí la caja y vi...». Se leen alargando un poco el final y haciendo una pausa.",
   "La entonación es la música de la voz al leer. Si lees «¿Dónde estás?» y «¡Dónde estás!» con la misma voz, no se nota la diferencia. Antes de leer, mira los signos y decide cómo sonará cada oración."],
  [("interrogación", "signos ¿? que encierran una pregunta"), ("exclamación", "signos ¡! que encierran una emoción o un aviso fuerte"), ("puntos suspensivos", "tres puntos (...) que dejan la idea en suspenso"), ("entonación", "la música de la voz al leer")],
  [("Reconocer la pregunta", "¿La oración «¿Dónde está mi gorro?» es pregunta o exclamación?", ["Veo los signos ¿ y ?.", "Esos signos encierran preguntas.", "Se lee con tono de pregunta."], "Es una pregunta"),
   ("Poner los signos", "Escribe con signos: «Cuánto cuesta el pan».", ["La oración pide un dato: es pregunta.", "Abro con ¿ antes de Cuánto.", "Cierro con ? al final."], "¿Cuánto cuesta el pan?")],
  [("Leer «¡Qué lindo día!» con voz plana, como si no pasara nada.", "No se mira la exclamación.", "Lee con alegría, subiendo la fuerza de la voz."), ("Escribir solo el signo del final: «Cómo estás?».", "Se olvida el signo de apertura.", "Escribe ¿Cómo estás? con signo de apertura y de cierre.")],
  ([E("¿Qué signos encierran una pregunta: ¿? o ¡!?", "¿?", "Los signos ¿? se usan para preguntas."),
    E("¿Qué signos muestran sorpresa o emoción fuerte: ¿? o ¡!?", "¡!", "Los signos ¡! encierran exclamaciones."),
    E("«¿Dónde está mi gorro?» ¿Es pregunta o exclamación?", "Pregunta", "Pide un dato y lleva signos de interrogación.")],
   [E("¿Cuál se lee con voz de alegría: «Hoy es mi cumpleaños.» o «¡Hoy es mi cumpleaños!»?", "«¡Hoy es mi cumpleaños!»", "Los signos de exclamación piden emoción."),
    E("¿Qué signo se escribe al comienzo de una pregunta en español?", "¿", "La pregunta se abre con ¿ y se cierra con ?."),
    E("En «Abrí la caja y vi...» ¿qué hace la voz al llegar a los puntos suspensivos: se queda en suspenso o termina firme?", "Se queda en suspenso", "Los puntos suspensivos dejan la idea sin cerrar.")],
   [E("Escribe los signos: «Cuántos años tienes».", "¿Cuántos años tienes?", "Es una pregunta: lleva ¿ al comienzo y ? al final."),
    E("Escribe los signos de una exclamación de susto: «Qué susto me diste».", "¡Qué susto me diste!", "Expresa susto, así que lleva ¡ y !."),
    E("Dos niños leen «¿Vienes a jugar?». Uno sube la voz al final y el otro la baja. ¿Cuál suena como pregunta?", "El que sube la voz", "En una pregunta de sí o no la voz suele subir al terminar.")],
   [E("¿Cuál se lee con urgencia: «¡Ayuda!» o «¿Ayuda?»?", "«¡Ayuda!»", "La exclamación muestra la urgencia."),
    E("Un niño lee «¡Cómo te llamas!» enojado, pero quiere saludar con amabilidad. ¿Cómo debería escribirse?", "¿Cómo te llamas?", "Es una pregunta amable, así que lleva signos de interrogación.")],
   [E("¿Cuántas de estas oraciones son preguntas? «¿Quién llegó?» «¡Llegó Laura!» «¿Viene sola?» «Viene con su hermano.»", "2", "Solo «¿Quién llegó?» y «¿Viene sola?» llevan signos de interrogación."),
    E("¿Qué pregunta tiene como respuesta «Tengo nueve años»: «¿Cuántos años tienes?» o «¿Dónde vives?»?", "«¿Cuántos años tienes?»", "La respuesta dice la edad.")]),
  [E("En la puerta hay un cartel: «¡Cuidado con el escalón!» ¿Lo lees para preguntar o para avisar con fuerza?", "Para avisar con fuerza", "Los signos de exclamación piden una voz fuerte de aviso.")],
  [E("¿Qué signos van al principio y al final de una pregunta?", "¿ y ?", "Se abre con ¿ y se cierra con ?."),
   E("¿Cómo se llama la música de la voz al leer?", "Entonación", "La entonación cambia según los signos."),
   E("Escribe con signos: «Dónde está la biblioteca».", "¿Dónde está la biblioteca?", "Es una pregunta, así que lleva ¿ y ?.")],
  ("Lee en voz alta este diálogo cambiando la voz según los signos. Luego dibuja una cara de alegría, de duda o de suspenso junto a cada línea. 1) «¿Ya llegó el bus?» 2) «¡Sí, aquí está!» 3) «¿Subimos juntos?» 4) «¡Claro que sí!» 5) «Y al subir, vi...»", "Líneas 1 y 3: cara de duda y voz que sube al final. Líneas 2 y 4: cara de alegría y voz más fuerte. Línea 5: cara de suspenso y voz alargada al final.", ["lee las preguntas con tono de pregunta", "lee las exclamaciones con emoción", "alarga el final ante los puntos suspensivos"], ["lectura en voz alta", "caras dibujadas"], ["leer todo con la misma voz", "olvidar el signo de apertura"], "Pide a otra persona que diga si notó la diferencia entre preguntas, exclamaciones y suspenso."),
  "Lee un cuento ilustrado y busca tres oraciones con signos. Léelas con la entonación correcta.",
  "Escribe un diálogo de cuatro líneas con dos preguntas y dos exclamaciones y léelo con una persona.")

L(OA1, 4,
  "Este cuaderno, lápiz y los textos escritos en cada ejercicio.",
  "Aprenderé a leer las palabras en grupos con sentido, para que mi lectura suene natural y no a saltitos.",
  ["Respeto la coma y el punto al leer.", "Reconozco quién hace la acción en una oración."],
  ["Una oración no se lee palabra por palabra, como saltando. Se lee en grupos de palabras que van juntas porque forman una idea. A esto se le llama fraseo. Por ejemplo: «El perro grande | ladra | a la puerta». Los grupos no tienen un largo fijo: dependen del sentido.",
   "Muchas veces un grupo dice quién hace la acción («Los niños pequeños») y otro dice lo que hace («juegan en la plaza»). Las palabras como «un», «el» o «de» se leen unidas a la palabra siguiente: «un perro», «el gato», «de mi casa». También se mantienen juntos el nombre y la palabra que lo describe: «gato negro».",
   "Antes de leer, imagina barritas entre los grupos. Si lees «El gato | negro duerme», suena raro, porque «negro» describe al gato y debe ir con él: «El gato negro | duerme». El fraseo también cuida el ritmo: una lectura en grupos suena fluida y se entiende mejor."],
  [("fraseo", "leer las palabras en grupos con sentido"), ("grupo de palabras", "palabras que van juntas porque forman una idea"), ("ritmo", "cómo se suceden las palabras y las pausas al leer"), ("describir", "decir cómo es algo")],
  [("Separar quién y qué hace", "Marca los grupos de «Mi tía Rosa canta en el coro».", ["Busco quién hace la acción: «Mi tía Rosa».", "Busco lo que hace: «canta en el coro».", "Pongo una barra entre ambos."], "Mi tía Rosa | canta en el coro"),
   ("Mantener unido lo que describe", "¿Cuál suena mejor: «El pájaro | azul canta» o «El pájaro azul | canta»?", ["«azul» cuenta cómo es el pájaro.", "Debe ir junto a «pájaro».", "El grupo «El pájaro azul» va primero."], "«El pájaro azul | canta»")],
  [("Leer una palabra por vez: «El... perro... grande... ladra...»", "No se piensa en el sentido de la oración.", "Une las palabras que forman una idea."), ("Separar «un» de «perro» con una pausa.", "Se cree que cada palabra es un grupo.", "Lee «un perro» como una sola unidad.")],
  ([E("¿Cuántas palabras tiene «El perro grande ladra.»?", "4", "Las palabras son El, perro, grande y ladra."),
    E("Al leer, ¿se dicen las palabras una por una con saltos o en grupos con sentido?", "En grupos con sentido", "Así se entiende mejor lo que se lee."),
    E("¿Cuál tiene orden y sentido: «Mi hermano menor | come una manzana» o «Mi hermano menor | una come manzana»?", "«Mi hermano menor | come una manzana»", "La otra opción tiene las palabras desordenadas.")],
   [E("¿Cuántos grupos tiene «El pájaro azul | canta en el árbol.»?", "2", "La barra separa dos grupos."),
    E("¿Qué grupo dice quién hace la acción: «Los niños pequeños» o «juegan en la plaza»?", "Los niños pequeños", "Dice quiénes son; el otro dice lo que hacen."),
    E("¿Cuál separa bien: «La abuela | cuenta un cuento.» o «La | abuela cuenta | un | cuento.»?", "«La abuela | cuenta un cuento.»", "Mantiene junto lo que va junto: «La abuela» y «un cuento».")],
   [E("Marca con una barra / entre quién y lo que hace: «Mi vecino Pedro arregla su bicicleta.»", "Mi vecino Pedro / arregla su bicicleta.", "La primera parte dice quién; la segunda, lo que hace."),
    E("¿Cuántos grupos tiene «Hoy / en la escuela / hicimos un mural.»?", "3", "Las dos barras separan tres grupos."),
    E("¿Cuántas palabras tiene el grupo «hicimos un mural»?", "3", "Las palabras son hicimos, un y mural.")],
   [E("Una lectora separa «El gato / negro duerme» y otra «El gato negro / duerme». ¿Cuál mantiene junto a quien describe?", "La segunda", "«Negro» describe al gato y va con «El gato»."),
    E("¿Por qué no conviene separar «un | perro»? (a) Porque «un perro» forma una sola idea. (b) Porque es muy largo.", "(a)", "El artículo y el nombre forman una idea juntos.")],
   [E("En «Cada tarde, / mi vecino riega / las flores del patio.» ¿cuántas palabras tiene el grupo más largo?", "4", "El último grupo tiene las, flores, del y patio."),
    E("En «Los pollitos duermen bajo el ala de su madre», si separas quién de lo que hace, ¿después de qué palabra va la primera barra?", "pollitos", "«Los pollitos» dice quiénes son y «duermen...» lo que hacen.")]),
  [E("Un aviso dice «Los alumnos de cuarto / traerán su cuaderno / el lunes.» ¿Cuántos grupos de palabras tiene?", "3", "Las dos barras separan tres grupos.")],
  [E("¿Cómo se llama leer las palabras en grupos con sentido?", "Fraseo", "Ese es el nombre de la lectura en grupos."),
   E("En «Mi gato | duerme.», ¿qué grupo dice quién hace la acción?", "Mi gato", "El primer grupo dice quién."),
   E("¿«un perro» se lee como un solo grupo o como dos?", "Un solo grupo", "El artículo se une a la palabra siguiente.")],
  ("Lee en voz alta este texto en grupos de palabras. Primero copia cada oración y marca los grupos con barras. «La luna sale temprano. Los grillos cantan en el jardín. Mi perro escucha atento.»", "La luna / sale temprano. Los grillos / cantan en el jardín. Mi perro / escucha atento.", ["pone barras entre quién y qué hace", "no separa artículo y nombre", "la lectura suena natural"], ["oraciones con barras", "lectura en voz alta"], ["leer palabra por palabra", "separar el artículo del nombre"], "Lee dos veces: primero palabra por palabra y luego en grupos. Compara cuál suena mejor."),
  "Elige una oración de un libro y marca sus grupos con barras antes de leerla.",
  "Escribe una oración larga de más de ocho palabras y márcala en tres grupos.")

POEMA = "Cuando amanece en el cerro, / el viento despierta al río. / ¡Qué frío! —dice el pastor— / y se abriga con su poncho."

L(OA1, 5,
  "Este cuaderno, lápiz, el poema escrito en esta clase y, si quieres, una persona de tu casa como público.",
  "Aprenderé a ensayar un texto para leerlo a una audiencia, cuidando precisión, pausas, entonación, fraseo, velocidad y voz clara.",
  ["Leo con precisión.", "Respeto pausas, signos y grupos de palabras."],
  ["Un texto se lee mejor cuando se ensaya. El ensayo tiene pasos: leerlo primero en silencio para entenderlo, marcar los signos y los grupos, practicar en voz alta y, al final, leerlo a una persona. Cada ensayo mejora un poco la lectura.",
   "Para que la audiencia entienda necesitas voz clara y un volumen adecuado: ni tan bajo que no se oiga, ni tan fuerte que moleste. También conviene una velocidad adecuada: la que permite decir bien las palabras y hacer las pausas. Puedes medirla contando cuántas palabras lees en un minuto; tu docente te dirá la meta para tu curso.",
   "Después de ensayar, revisa tu lectura con una lista: ¿dije todas las palabras bien?, ¿hice las pausas?, ¿cambié la voz en preguntas y exclamaciones?, ¿leí en grupos de palabras?, ¿se oyó mi voz? Mirar de vez en cuando a la audiencia, sin perder el lugar en el texto, ayuda a comunicar."],
  [("ensayar", "practicar varias veces antes de presentar"), ("audiencia", "las personas que escuchan"), ("volumen", "qué tan fuerte o suave se oye la voz"), ("lista de revisión", "preguntas que sirven para revisar un trabajo")],
  [("Ordenar los pasos", "Ordena: (a) leer a la audiencia, (b) leer en silencio, (c) practicar en voz alta, (d) marcar pausas y grupos.", ["Primero entiendo el texto: leo en silencio.", "Luego marco pausas y grupos.", "Después practico en voz alta y al final leo a la audiencia."], "b, d, c, a"),
   ("Calcular ensayos", "Ensayas un poema 3 veces el lunes y 3 veces el martes. ¿Cuántas veces lo ensayaste?", ["El lunes son 3 ensayos.", "El martes son otros 3.", "Se suman: 3 + 3 = 6."], "6 ensayos")],
  [("Leer por primera vez frente al público, sin haber ensayado.", "Se cree que no hace falta practicar.", "Ensaya al menos tres veces antes."), ("Leer con la cabeza metida en el papel y voz muy baja.", "Se tiene vergüenza.", "Sube un poco el volumen y mira a la audiencia entre una línea y otra.")],
  ([E("¿Cuál es el primer paso para preparar una lectura: leer en silencio o leer a la audiencia?", "Leer en silencio", "Primero hay que entender el texto."),
    E("¿Cómo se llaman las personas que escuchan una lectura?", "Audiencia", "Audiencia es el público que escucha."),
    E("Si nadie oye tu lectura, ¿el volumen es muy alto o muy bajo?", "Muy bajo", "Si no se oye, la voz está demasiado suave.")],
   [E("¿Para qué sirve ensayar?", "Para leer mejor y con más seguridad", "Cada práctica mejora precisión, pausas y entonación."),
    E("En una lista de revisión, ¿qué pregunta revisa la precisión: «¿Dije bien todas las palabras?» o «¿Miré a la audiencia?»", "«¿Dije bien todas las palabras?»", "La precisión es decir cada palabra tal como está escrita."),
    E("¿Qué pregunta revisa la entonación: «¿Cambié la voz en preguntas y exclamaciones?» o «¿Cuántas páginas leí?»", "«¿Cambié la voz en preguntas y exclamaciones?»", "La entonación es la música de la voz según los signos.")],
   [arith("Ensayas un poema 4 veces el lunes y 3 veces el martes. ¿Cuántas veces lo ensayaste?", "4+3", "Se suman los ensayos de los dos días."),
    E("Lee este verso: «¿Quién llama a mi ventana?». ¿Con qué tono lo leerás: de pregunta o de alegría fuerte?", "De pregunta", "El verso lleva signos de interrogación."),
    arith("Una niña lee un poema de 180 palabras en 2 minutos. ¿Cuántas palabras lee por minuto, si va siempre igual de rápido?", "180//2", "Se divide el total de palabras por los minutos.")],
   [E("Una niña ensayó dos veces y lee con mucha velocidad y errores. Otra ensayó seis veces y lee sin errores. ¿Cuál tuvo más práctica?", "La segunda", "Seis ensayos son más que dos."),
    E("Un niño mira solo el papel y nunca levanta la vista. ¿Qué podría hacer para conectar con la audiencia?", "Levantar la vista entre una línea y otra", "Mirar al público ayuda a comunicar.")],
   [E("Cuenta las palabras del primer verso: «Cuando amanece en el cerro». ¿Cuántas son?", "5", "Las palabras son Cuando, amanece, en, el y cerro."),
    arith("Si un poema tiene 4 versos y cada uno tiene 5 palabras, ¿cuántas palabras tiene el poema?", "5+5+5+5", "Se suman las palabras de los cuatro versos.")]),
  [E("Mañana leerás un aviso en la sala. Ensayas hoy 3 veces en la mañana y 2 en la tarde. ¿Cuántos ensayos hiciste hoy?", "5", "Se suman 3 y 2.")],
  [E("¿Cuál es el último paso: leer a la audiencia o marcar pausas?", "Leer a la audiencia", "Se lee al público después de ensayar."),
   E("¿Qué debes cuidar con el volumen: que se oiga o que sea gritado?", "Que se oiga bien", "El volumen adecuado permite que todos escuchen sin molestar."),
   E("¿Para qué sirve una lista de revisión?", "Para revisar cómo leí", "Sirve para comprobar precisión, pausas y entonación.")],
  ("Ensaya este poema original tres veces y léelo a una persona de tu casa. Las barras / separan los versos. Antes de leer, subraya con lápiz los signos de puntuación. «" + POEMA + "» Luego completa la lista: precisión, pausas, entonación, volumen. Marca sí o no en cada una.", "Leí con 1 error corregido, hice las pausas, subí la voz en la exclamación y mi volumen se oyó bien: sí en las cuatro.", ["ensaya tres veces", "cuida precisión, pausas, entonación y volumen", "completa la lista de revisión"], ["lectura ante una persona", "lista completada"], ["no ensayar", "leer sin cambiar la voz en la exclamación"], "Pide a quien te escuchó una cosa que hiciste bien y una para mejorar en el próximo ensayo."),
  "Lee de nuevo el poema a otra persona y compara con tu primera lectura.",
  "Elige otro texto breve, marca pausas y grupos y prepáralo para leerlo a tu curso.")
