"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación, OA 04 (comprensión profunda de narraciones).

Todos los cuentos son originales y breves; cada ejercicio trae el texto que necesita.
"""
from __future__ import annotations

from student_content_le4_a import E, L
from student_lessons import arith

OA4 = "LE04 OA 04"

T1 = ("Cuando sonó la campana, Joaquín guardó su bufanda en la mochila y salió al patio sin mirar a nadie. En la sala quedó su banco vacío, con el cuaderno abierto en la última página: "
      "«Hoy no hice la tarea», decía con letra apretada. Su amiga Valentina lo vio sentarse solo bajo el aromo, mirando el piso.")

# ------------------------------------------------------------------ OA 04
L(OA4, 1,
  "Este cuaderno, lápiz y el cuento escrito en esta clase (original de este cuaderno).",
  "Aprenderé a distinguir lo que un cuento dice con claridad (información explícita) de lo que debo deducir con pistas (información implícita).",
  ["Releo para entender.", "Respondo preguntas sobre quién, qué, dónde y cuándo."],
  ["La información explícita es la que el texto dice directamente. Puedes señalarla con el dedo: «Joaquín guardó su bufanda». La información implícita es la que el texto no dice, pero puedes deducir con pistas. A ese razonamiento se le llama inferencia.",
   "Para inferir, junta tres cosas: lo que dice el texto, lo que ya sabes y lo que hacen los personajes. Si Joaquín sale sin mirar a nadie y se sienta solo mirando el piso, esas pistas sugieren que se siente mal. El texto no dice «estaba triste», pero lo muestra.",
   "Una inferencia buena siempre tiene pruebas en el texto. Si no puedes señalar una pista, probablemente estás inventando. Cuando respondas, escribe tu inferencia y la pista que la apoya, por ejemplo: «Joaquín se siente preocupado, porque dejó escrito que no hizo la tarea»."],
  [("explícito", "dicho directamente en el texto"), ("implícito", "que no está dicho, pero se deduce"), ("inferencia", "idea que deduzco con pistas del texto"), ("pista", "dato del texto que sirve para deducir algo")],
  [("Información explícita", "Lee el cuento: «" + T1 + "» ¿Qué guardó Joaquín?", ["Busco el verbo «guardó».", "Leo lo que sigue.", "Respondo con lo que el texto dice."], "Su bufanda"),
   ("Información implícita", "En el mismo texto, ¿cómo se siente Joaquín y qué pista lo muestra?", ["El texto no dice cómo se siente.", "Pistas: sale sin mirar a nadie, se sienta solo, mira el piso.", "Eso sugiere que está preocupado o avergonzado."], "Preocupado o avergonzado; sale sin mirar a nadie y se sienta solo")],
  [("Responder una inferencia sin una pista del texto.", "Se inventa una respuesta.", "Escribe qué dice el texto que apoya tu idea."), ("Creer que lo implícito es adivinar.", "No se distingue pista de suposición.", "Una inferencia se apoya en datos del texto.")],
  ([E("Lo que el texto dice directamente, ¿es información explícita o implícita?", "Explícita", "Está escrita en el texto."),
    E("Lo que se deduce con pistas, ¿es explícito o implícito?", "Implícito", "No está dicho, se infiere."),
    E("Según el texto, ¿adónde salió Joaquín cuando sonó la campana?", "Al patio", "El texto dice «salió al patio».")],
   [E("¿Qué decía el cuaderno de Joaquín?", "«Hoy no hice la tarea»", "El texto lo copia entre comillas."),
    E("¿Quién vio a Joaquín sentarse solo?", "Valentina", "El texto dice que su amiga Valentina lo vio."),
    E("¿Dónde se sentó Joaquín: bajo el aromo o en su banco?", "Bajo el aromo", "El texto dice «bajo el aromo».")],
   [E("¿Qué pista muestra que Joaquín no quiere hablar con nadie?", "Salió sin mirar a nadie", "Evitar las miradas es una pista de que no quiere conversar."),
    E("¿Es explícito o implícito que Joaquín está avergonzado por la tarea?", "Implícito", "El texto no lo dice, se deduce de sus acciones."),
    E("El texto dice que el cuaderno quedó abierto en la última página. ¿Dice por qué quedó abierto?", "No", "Ninguna oración explica el motivo.")],
   [E("Dos lectores infieren cómo se siente Joaquín. Uno dice «contento» y otro «preocupado». ¿Qué pista contradice al primero?", "Se sienta solo y mira el piso", "Esos gestos no muestran alegría."),
    E("«Joaquín tiene frío porque guardó su bufanda.» ¿Esa inferencia tiene apoyo en el texto?", "No", "Guardar la bufanda no indica frío.")],
   [E("Un lector dice: «Valentina es una buena amiga porque se preocupa por Joaquín». ¿Qué parte del texto apoya esa inferencia?", "Que lo vio y lo miró sentarse solo", "Se fija en su amigo y se interesa por él."),
    E("¿Cuál es una inferencia sobre Valentina con pista: «Es atenta, porque se fijó en que Joaquín estaba solo» o «Es alta, porque se sentó bajo el aromo»?", "«Es atenta, porque se fijó en que Joaquín estaba solo»", "La otra opción no tiene pista en el texto.")]),
  [E("En tu cuaderno de comunicaciones lees: «Mañana salimos temprano, traigan sombrero y bloqueador». Sin que lo diga, ¿qué infieres del clima: que habrá sol fuerte o nieve?", "Que habrá sol fuerte", "El sombrero y el bloqueador son pistas de sol.")],
  [E("¿Cómo se llama la idea que deduzco con pistas?", "Inferencia", "Se apoya en datos del texto."),
   E("Si algo está escrito en el texto, ¿es explícito o implícito?", "Explícito", "Está dicho directamente."),
   E("¿Qué debe tener toda inferencia para ser buena?", "Una pista del texto", "Sin pista sería inventar.")],
  ("Lee y responde: «" + T1 + "» 1) Escribe dos datos explícitos. 2) Escribe una inferencia sobre cómo se siente Joaquín y la pista que la apoya. 3) Escribe una inferencia sobre cómo es Valentina y su pista.", "1) Guardó su bufanda; Valentina lo vio solo. 2) Joaquín está preocupado; sale sin mirar a nadie. 3) Valentina es atenta; se fija en que Joaquín está solo.", ["distingue datos explícitos", "formula inferencias razonables", "apoya cada inferencia en el texto"], ["tres respuestas escritas"], ["inventar sin pista", "confundir explícito con implícito"], "Lee tus pistas a otra persona y comprueba si llega a tu misma inferencia."),
  "Lee un cuento breve y anota un dato explícito y una inferencia con su pista.",
  "Escribe una escena de tres oraciones donde un personaje muestre una emoción sin nombrarla.")

T2 = ("El sábado, Marta quiso hornear un queque para el cumpleaños de su abuelo. Con ayuda de su tía mezcló los ingredientes, pero olvidó encender el horno antes de meter el molde y lo notó recién diez minutos después, cuando lo encendió. "
      "Pasados los 40 minutos que decía la receta, el queque estaba crudo por dentro. Marta y su tía lo dejaron 30 minutos más. Entonces quedó dorado y firme. "
      "Cuando el abuelo llegó, la cocina olía a vainilla.")

L(OA4, 2,
  "Este cuaderno, lápiz y el cuento escrito en esta clase (original de este cuaderno).",
  "Aprenderé a ordenar los hechos de un cuento, a ver cómo una acción provoca otra (causa y consecuencia) y a reconocer el problema y su solución.",
  ["Distingo información explícita e implícita.", "Sé qué significa «primero, luego, finalmente»."],
  ["La secuencia es el orden en que ocurren los hechos de un cuento. Se reconoce con palabras como primero, luego, después, entonces y finalmente. Ordenar una secuencia ayuda a contar el cuento sin perder partes.",
   "Una causa es lo que provoca un hecho, y la consecuencia es el hecho que ocurre. Se unen con palabras como porque, por eso y entonces. Por ejemplo: Marta olvidó encender el horno (causa), por eso el queque quedó crudo (consecuencia).",
   "Casi todo cuento tiene un problema y una solución. El problema es la dificultad que enfrentan los personajes; la solución es lo que hacen para resolverla. En este cuento, el problema es el queque crudo y la solución es dejarlo hornear 30 minutos más."],
  [("secuencia", "orden en que ocurren los hechos"), ("causa", "lo que provoca un hecho"), ("consecuencia", "lo que ocurre a partir de una causa"), ("problema y solución", "dificultad de los personajes y lo que hacen para resolverla")],
  [("Causa y consecuencia", "Lee el cuento: «" + T2 + "» ¿Por qué el queque quedó crudo por dentro?", ["Busco qué hizo Marta mal.", "Olvidó encender el horno antes de meter el molde.", "Por eso el queque quedó crudo."], "Porque olvidó encender el horno antes"),
   ("Calcular el tiempo", "La receta pedía 40 minutos y el queque se dejó 30 minutos más. ¿Cuánto tiempo estuvo en el horno?", ["Tiempo de la receta: 40 minutos.", "Tiempo extra: 30 minutos.", "Sumo: 40 + 30 = 70."], "70 minutos")],
  [("Confundir el orden de los hechos.", "Se cuenta como se recuerda, no como pasó.", "Marca primero, luego y finalmente."), ("Decir que la causa es el final del cuento.", "Se confunde causa con consecuencia.", "La causa viene antes; la consecuencia, después.")],
  ([E("La secuencia de un cuento, ¿es el orden de los hechos o el color de los personajes?", "El orden de los hechos", "Secuencia es el orden en que ocurre todo."),
    E("¿Qué quiso hacer Marta el sábado?", "Hornear un queque", "El texto lo dice al inicio."),
    E("¿Cuál es el problema del cuento: el queque crudo o el abuelo atrasado?", "El queque crudo", "Después de 40 minutos seguía crudo por dentro.")],
   [E("¿Quién ayudó a Marta a mezclar los ingredientes?", "Su tía", "El texto dice «con ayuda de su tía»."),
    E("¿Cuánto tiempo decía la receta?", "40 minutos", "Lo dice el texto."),
    E("¿Cuál es la solución al problema: dejarlo 30 minutos más o tirarlo?", "Dejarlo 30 minutos más", "Así el queque quedó dorado y firme.")],
   [arith("Marta tardó 25 minutos en mezclar los ingredientes y el queque estuvo 70 minutos en el horno. ¿Cuántos minutos pasaron en total desde que empezó a mezclar hasta que lo sacó, sin contar otras esperas?", "25+70", "Se suman el tiempo de mezclar y el tiempo en el horno."),
    E("Ordena: (a) El queque quedó dorado. (b) Marta mezcló los ingredientes. (c) El queque estaba crudo. ¿Cuál es el orden?", "b, c, a", "Primero mezcla, luego se ve crudo y después queda dorado."),
    E("¿Qué palabra une causa y consecuencia en «Marta olvidó encender el horno, por eso el queque quedó crudo»?", "Por eso", "«Por eso» conecta la causa con su consecuencia.")],
   [E("Un lector dice: «El queque quedó crudo porque la receta estaba mala». ¿Qué dice el texto que lo contradice?", "Marta olvidó encender el horno", "La causa es el horno apagado, no la receta."),
    E("Si Marta hubiera encendido el horno antes, ¿qué habría ocurrido con el queque después de los 40 minutos?", "Habría quedado cocido", "El queque habría podido hornearse el tiempo de la receta.")],
   [E("¿Qué palabra muestra la secuencia en «Entonces quedó dorado y firme»?", "Entonces", "«Entonces» indica que algo ocurre después."),
    E("Si el queque entró al horno a las 4:00 de la tarde y estuvo 70 minutos, ¿a qué hora salió? Responde con hora y minutos.", "5:10", "4:00 más 70 minutos es 5:10.")]),
  [E("Preparas una receta que dura 35 minutos y sabes que debes sumar 25 minutos más si queda cruda. ¿Cuántos minutos serían en total?", "60", "Se suman 35 y 25.", "35+25")],
  [E("¿Cómo se llama el orden en que ocurren los hechos?", "Secuencia", "Es el orden de los hechos."),
   E("En una causa y consecuencia, ¿qué ocurre primero: la causa o la consecuencia?", "La causa", "La causa provoca la consecuencia."),
   E("¿Cómo se llama la dificultad que enfrentan los personajes?", "Problema", "Es lo que deben resolver.")],
  ("Lee el cuento: «" + T2 + "» 1) Ordena los hechos con primero, luego y finalmente. 2) Escribe una causa y su consecuencia con «por eso». 3) Escribe el problema y la solución. 4) Calcula cuánto estuvo el queque en el horno.", "1) Primero mezcló los ingredientes, luego olvidó encender el horno y finalmente lo dejó 30 minutos más. 2) Olvidó encender el horno, por eso quedó crudo. 3) Problema: el queque crudo. Solución: dejarlo 30 minutos más. 4) 70 minutos.", ["ordena la secuencia", "separa causa y consecuencia", "identifica problema y solución", "calcula el tiempo"], ["respuestas escritas"], ["mezclar el orden", "confundir causa y consecuencia"], "Cuenta el cuento oralmente en orden, usando las palabras primero, luego y finalmente."),
  "Cuenta a alguien lo que hiciste hoy usando primero, luego y finalmente.",
  "Escribe un cuento breve con un problema y una solución, y subraya la causa y la consecuencia.")

T3 = ("Ante la acequia que cruzaba el camino, Ema miró cada piedra antes de pisar y probó una con el pie. Solo entonces avanzó. Tito, en cambio, saltó de piedra en piedra gritando «¡Yo primero!». "
      "En la tercera piedra se resbaló y mojó su zapato. Ema le pasó un palo para que se apoyara y no se rió de él.")

L(OA4, 3,
  "Este cuaderno, lápiz y los cuentos escritos en esta clase (originales de este cuaderno).",
  "Aprenderé a describir y comparar personajes usando lo que hacen y dicen, y a comparar textos de un mismo autor.",
  ["Distingo información explícita e implícita.", "Reconozco causa y consecuencia."],
  ["Para conocer a un personaje, mira lo que hace, lo que dice y lo que piensa. Con eso descubres cómo es: cuidadoso, apurado, generoso. A estos rasgos se les llama características del personaje. Un buen retrato de un personaje siempre apoya cada rasgo en un hecho del texto.",
   "Comparar personajes es ver en qué se parecen y en qué se diferencian. Ema y Tito enfrentan la misma situación, pero actúan distinto: Ema observa antes de moverse; Tito se lanza sin pensar. También puedes comparar cómo reacciona cada uno ante un problema.",
   "A veces un mismo autor escribe varios textos y repite ciertas ideas, tipos de personajes o formas de contar. Comparar dos textos del mismo autor es buscar qué tienen en común y qué cambia. En esta clase compararás dos cuentos breves de una misma autora imaginaria."],
  [("personaje", "ser que participa en un cuento"), ("rasgo", "característica de cómo es o actúa un personaje"), ("comparar", "ver en qué se parecen y en qué se diferencian dos cosas"), ("autor", "persona que escribe un texto")],
  [("Rasgo con evidencia", "Lee el cuento: «" + T3 + "» ¿Cómo es Ema y qué lo prueba?", ["Busco lo que hace Ema.", "Mira cada piedra y prueba una con el pie.", "Eso muestra que es cuidadosa."], "Cuidadosa; mira cada piedra y la prueba"),
   ("Comparar", "¿En qué se diferencian Ema y Tito ante la acequia?", ["Ema revisa cada piedra antes de pisar.", "Tito salta gritando sin revisar.", "Ema es cuidadosa y Tito es impulsivo."], "Ema actúa con cuidado; Tito, sin pensar")],
  [("Decir cómo es un personaje sin dar ninguna prueba del texto.", "Se opina sin apoyo.", "Agrega una frase: «porque…»."), ("Comparar solo apariencia física.", "Se mira lo que se ve, no cómo actúan.", "Compara acciones y actitudes.")],
  ([E("Un rasgo de un personaje, ¿es una característica de cómo es o un lugar?", "Una característica de cómo es", "Describe al personaje."),
    E("¿Quién miró cada piedra antes de pisar?", "Ema", "El texto lo dice de Ema."),
    E("¿Quién gritó «¡Yo primero!»?", "Tito", "Lo dice el texto.")],
   [E("¿Qué le pasó a Tito en la tercera piedra?", "Se resbaló y mojó su zapato", "El texto lo describe."),
    E("¿Qué le pasó a Ema?", "No se cayó; ayudó a Tito", "Pasó un palo a Tito."),
    E("¿Quién le pasó el palo a Tito para que se apoyara?", "Ema", "Lo dice el texto.")],
   [E("¿Qué rasgo tiene Tito: impulsivo o cuidadoso?", "Impulsivo", "Salta sin revisar y grita que será primero."),
    E("¿Qué rasgo muestra Ema al no reírse de Tito: respeto o burla?", "Respeto", "No se rió y lo ayudó."),
    E("¿Qué hizo Ema con una de las piedras antes de avanzar?", "La probó con el pie", "El texto dice que probó una piedra con el pie.")],
   [E("Un lector dice que Ema es cobarde porque revisó las piedras. ¿Qué puede responder otro para defender que no es cobarde, sino cuidadosa?", "Que revisó y luego avanzó", "Revisó y después cruzó; no se quedó paralizada."),
    E("¿En qué se parecen Ema y Tito? Ambos…", "Intentaron cruzar la acequia", "Los dos enfrentan el mismo obstáculo.")],
   [E("Texto A de una autora: «Ina ayudó a su abuela a cuidar el huerto todas las tardes.» Texto B de la misma autora: «Ina ayudó al vecino a reparar la cerca después de la lluvia.» ¿Qué acción repite Ina en ambos textos?", "Ayudar a otros", "En ambos textos ayuda a alguien."),
    E("Comparando A y B, ¿cambia el lugar o el personaje principal?", "Cambia el lugar", "El personaje es Ina en los dos; el lugar es el huerto y la cerca.")]),
  [E("En tu curso, un compañero espera su turno y otro se adelanta empujando. ¿Qué rasgo muestra el que espera: paciencia o apuro?", "Paciencia", "Esperar el turno muestra paciencia.")],
  [E("¿Qué se mira para descubrir cómo es un personaje?", "Lo que hace, dice y piensa", "Eso muestra sus rasgos."),
   E("¿Comparar es ver semejanzas y diferencias?", "Sí", "Eso es comparar."),
   E("¿Cómo se llama quien escribe un texto?", "Autor", "El autor es quien lo escribe.")],
  ("Lee: «" + T3 + "» 1) Escribe dos rasgos de Ema y una prueba de cada uno. 2) Escribe un rasgo de Tito y su prueba. 3) Escribe una semejanza y una diferencia entre ambos. 4) Escribe cómo reaccionarías tú en lugar de Ema ante la caída de Tito.", "1) Cuidadosa: prueba la piedra. Solidaria: le pasa un palo a Tito. 2) Impulsivo: salta gritando «¡Yo primero!». 3) Semejanza: ambos cruzan la acequia. Diferencia: Ema revisa y Tito no. 4) Yo le diría que se apoye, como Ema.", ["dos rasgos de Ema con pruebas", "un rasgo de Tito con prueba", "semejanza y diferencia", "reacción propia coherente"], ["cuatro respuestas escritas"], ["rasgos sin prueba", "comparar solo apariencia"], "Revisa que cada rasgo que escribiste tenga una frase del texto como prueba."),
  "Elige dos personajes de libros que conozcas y compáralos en una frase: en qué se parecen y en qué se diferencian.",
  "Escribe un cuento corto con dos personajes que enfrenten el mismo problema de forma distinta.")

T4 = ("La casa del abuelo estaba al fondo del valle. Cada mañana, el techo amanecía cubierto de escarcha. Adentro, la estufa crepitaba y el olor a pan tostado llenaba la cocina. "
      "Afuera, la niebla se pegaba a las ventanas y no dejaba ver el cerro. Por eso, Lía prefirió quedarse leyendo junto a la estufa en vez de salir a explorar.")

L(OA4, 4,
  "Este cuaderno, lápiz y el cuento escrito en esta clase (original de este cuaderno).",
  "Aprenderé a describir el ambiente de un cuento (lugar, momento y clima) y a explicar cómo influye en lo que hacen los personajes.",
  ["Describo personajes con pruebas.", "Distingo causa y consecuencia."],
  ["El ambiente de un cuento es el lugar y el momento en que ocurre. Incluye dónde están los personajes, la hora o la época y el clima. En el cuento de Lía, el ambiente es una casa al fondo del valle, de mañana, con escarcha y niebla. Los detalles que lo muestran son palabras como «estufa», «niebla» o «escarcha».",
   "Un mismo cuento puede tener más de un ambiente. Adentro de la casa hay calor y olor a pan; afuera hay frío y niebla. Para describirlos, busca palabras que hablen de lo que se ve, se oye, se huele o se siente.",
   "El ambiente influye en la acción. Por la niebla no se ve el cerro, por eso Lía decide quedarse leyendo. Si el día hubiera estado despejado, tal vez habría salido a explorar. Cuando leas, pregúntate: ¿cómo cambia el ambiente lo que hacen los personajes?"],
  [("ambiente", "lugar, momento y clima en que ocurre un cuento"), ("escarcha", "capa fina de hielo que se forma con el frío"), ("crepitar", "hacer ruidos pequeños y secos, como la leña al quemarse"), ("influir", "hacer que algo cambie")],
  [("Ambiente de afuera y de adentro", "Lee el cuento: «" + T4 + "» ¿Cómo es el ambiente de adentro y el de afuera?", ["Adentro: estufa, olor a pan tostado.", "Afuera: niebla, escarcha, techo helado.", "Adentro es cálido y afuera es frío."], "Adentro cálido; afuera frío y con niebla"),
   ("Efecto en la acción", "¿Por qué Lía no salió a explorar?", ["Busco la causa en el ambiente.", "La niebla no dejaba ver el cerro.", "Por eso se quedó leyendo."], "Porque la niebla no dejaba ver el cerro")],
  [("Decir «el ambiente es el cuento».", "Se confunde ambiente con historia.", "Ambiente es lugar, momento y clima."), ("Nombrar solo el lugar.", "Se olvida el momento y el clima.", "Agrega hora, época o clima si aparecen.")],
  ([E("El ambiente de un cuento, ¿es el lugar y momento donde ocurre o el nombre del autor?", "El lugar y momento donde ocurre", "Eso es el ambiente."),
    E("¿Dónde estaba la casa del abuelo?", "Al fondo del valle", "Lo dice el texto."),
    E("¿Qué cubría el techo cada mañana?", "Escarcha", "El texto lo dice.")],
   [E("¿Qué olor había en la cocina?", "Pan tostado", "El texto lo menciona."),
    E("¿Qué hacía la niebla?", "Se pegaba a las ventanas y tapaba el cerro", "Lo dice el texto."),
    E("¿Qué hacía la estufa?", "Crepitaba", "El texto dice «crepitaba».")],
   [E("¿Qué clima hay afuera de la casa: cálido o frío?", "Frío", "La escarcha y la niebla son pistas de frío."),
    E("¿Qué palabra del texto muestra el momento del día?", "Mañana", "Dice que cada mañana el techo amanecía con escarcha."),
    E("¿Qué hace Lía en el ambiente de adentro?", "Lee junto a la estufa", "El texto lo cuenta al final.")],
   [E("Si el día hubiera estado despejado, ¿qué crees que habría podido hacer Lía?", "Salir a explorar", "La niebla era la causa de que no saliera."),
    E("¿Qué ambiente hace sentir más abrigo: «la cocina con estufa» o «el patio con niebla»?", "La cocina con estufa", "El calor y el olor a pan dan abrigo.")],
   [E("Un lector dice que el ambiente del cuento es una playa soleada. ¿Qué dos datos del texto contradicen esa idea?", "La escarcha y la niebla", "Ambas indican frío, no sol."),
    E("Las frases «la estufa crepitaba» y «olor a pan tostado», ¿qué dos sentidos hacen imaginar?", "Oído y olfato", "Crepitar es un sonido y el olor se percibe con el olfato.")]),
  [E("Sales de la sala y llueve fuerte. Tu profesor suspende el partido de fútbol. ¿Qué parte del ambiente influyó en la decisión?", "La lluvia", "El clima cambió lo que se hizo.")],
  [E("¿Qué tres cosas incluye el ambiente de un cuento?", "Lugar, momento y clima", "Esos tres elementos forman el ambiente."),
   E("¿Cómo se llama la capa de hielo que se forma con el frío?", "Escarcha", "Así lo define esta clase."),
   E("¿Puede el ambiente cambiar lo que hace un personaje?", "Sí", "El ambiente influye en la acción.")],
  ("Lee: «" + T4 + "» 1) Escribe dos detalles de adentro y dos de afuera. 2) Escribe cómo es el momento del día. 3) Explica cómo el ambiente influye en lo que hace Lía. 4) Escribe una oración que describa el ambiente de tu sala con un lugar, un momento y un clima.", "1) Adentro: estufa y olor a pan. Afuera: niebla y escarcha. 2) La mañana. 3) Por la niebla no puede ver el cerro, así que se queda leyendo. 4) En mi sala, por la mañana, hace frío y se ve la lluvia en las ventanas.", ["detalles de adentro y de afuera", "momento del día", "influencia del ambiente en la acción", "describe un ambiente propio"], ["cuatro respuestas escritas"], ["solo nombrar el lugar", "no explicar la influencia"], "Lee tu descripción y pide a otra persona que diga cómo se imagina el lugar."),
  "Describe en tres oraciones el ambiente del lugar donde lees tus cuentos.",
  "Escribe una escena corta en que el clima cambie lo que decide un personaje.")

T5 = ("Cuando la profesora dijo que quien encontrara el libro perdido ganaría un punto extra, Daniel recordó dónde estaba: bajo su propio banco, donde él lo había dejado. "
      "Pensó en devolverlo de inmediato, pero lo guardó hasta el recreo. Luego lo entregó diciendo que lo había encontrado en el pasillo.")

L(OA4, 5,
  "Este cuaderno, lápiz y el cuento escrito en esta clase (original de este cuaderno).",
  "Aprenderé a expresar una opinión sobre lo que hace un personaje y a fundamentarla con hechos del texto.",
  ["Distingo hechos de inferencias.", "Reconozco rasgos de personajes."],
  ["Un hecho es algo que ocurre en el texto y se puede comprobar: «Daniel lo entregó diciendo que lo encontró en el pasillo». Una opinión es lo que tú piensas sobre eso: «Daniel actuó mal». La opinión no es un hecho: depende de ti, pero debe tener razones.",
   "Una opinión fundamentada tiene tres partes: dices lo que piensas, das una razón y la apoyas con un hecho del texto. Por ejemplo: «Pienso que Daniel no fue honesto, porque dijo que había encontrado el libro en el pasillo y en realidad estaba bajo su banco». La palabra «porque» une tu opinión con la prueba.",
   "No todas las opiniones son iguales: las mejores se apoyan en datos del texto. Una opinión sin prueba («porque sí») no convence. Además, escucha las opiniones de otros: pueden pensar distinto, pero deben apoyarlas con hechos."],
  [("hecho", "algo que ocurre y se puede comprobar en el texto"), ("opinión", "lo que yo pienso sobre algo"), ("fundamentar", "dar razones y pruebas para apoyar lo que pienso"), ("honesto", "que dice la verdad y actúa con sinceridad")],
  [("Hecho u opinión", "Lee el cuento: «" + T5 + "» Frase: «Daniel entregó el libro en el recreo.» ¿Hecho u opinión?", ["Puedo comprobarlo en el texto.", "No depende de lo que yo piense.", "Es un hecho."], "Hecho"),
   ("Fundamentar", "Opinión: «Daniel no fue honesto». ¿Qué hecho la apoya?", ["Busco una acción en el texto que lo muestre.", "Dijo que lo encontró en el pasillo, pero estaba bajo su banco.", "Eso es una mentira."], "Dijo que lo encontró en el pasillo, pero estaba bajo su banco")],
  [("Dar una opinión sin ninguna prueba.", "Se usa «porque sí».", "Agrega un hecho del texto después de «porque»."), ("Decir que mi opinión es un hecho.", "Se confunde lo que pienso con lo que ocurrió.", "Los hechos están en el texto; las opiniones, en mi cabeza.")],
  ([E("Lo que ocurre en el texto y se puede comprobar, ¿es un hecho o una opinión?", "Un hecho", "Se puede comprobar."),
    E("Lo que yo pienso sobre un personaje, ¿es un hecho o una opinión?", "Una opinión", "Depende de mi pensamiento."),
    E("¿Dónde estaba el libro en realidad?", "Bajo el banco de Daniel", "El texto lo dice.")],
   [E("«Daniel guardó el libro hasta el recreo.» ¿Hecho u opinión?", "Hecho", "El texto lo cuenta."),
    E("«Daniel fue muy malo.» ¿Hecho u opinión?", "Opinión", "Es un juicio personal."),
    E("¿Qué palabra une una opinión con su razón?", "Porque", "«Porque» introduce la razón.")],
   [E("¿Qué mentira le dijo Daniel a la profesora?", "Que había encontrado el libro en el pasillo", "En realidad estaba bajo su banco."),
    E("Completa: «Pienso que Daniel actuó mal, porque ______». ¿Cuál razón apoya la opinión: «dijo que lo había encontrado en el pasillo» o «guardó el libro»?", "«dijo que lo había encontrado en el pasillo»", "Mentir sobre dónde estaba el libro es una acción clara para fundamentar."),
    E("¿Qué buscaba Daniel al devolver el libro con esa historia?", "El punto extra", "La profesora había ofrecido un punto extra.")],
   [E("Un lector dice: «Daniel es un niño malo porque sí». ¿Qué le falta a esa opinión?", "Una razón con un hecho del texto", "No tiene prueba."),
    E("Otro lector dice: «Daniel quería un punto y no pensó en lo honesto». ¿Qué hecho apoya?", "Que esperó al recreo y mintió", "Se apoya en sus acciones.")],
   [E("¿Cuál es una opinión fundamentada: «Daniel actuó mal porque dijo que había encontrado el libro en el pasillo» o «Daniel actuó mal porque sí»?", "«Daniel actuó mal porque dijo que había encontrado el libro en el pasillo»", "La razón se apoya en un hecho del texto."),
    E("Si dos compañeros dan distintas opiniones sobre Daniel, ¿ambos deben apoyarlas con hechos del texto?", "Sí", "Una opinión valiosa tiene pruebas.")]),
  [E("En tu curso, un compañero dice que un cuento es aburrido. ¿Qué debe agregar para fundamentar su opinión?", "Una razón con un hecho del cuento", "Debe explicar por qué con algo del cuento.")],
  [E("¿Cómo se llama lo que pienso sobre algo?", "Opinión", "Es lo que yo pienso."),
   E("¿Qué debe llevar una buena opinión?", "Una razón y un hecho del texto", "Eso la fundamenta."),
   E("¿Qué palabra suele introducir la razón?", "Porque", "Une la opinión con la prueba.")],
  ("Lee: «" + T5 + "» 1) Escribe dos hechos del cuento. 2) Escribe tu opinión sobre lo que hizo Daniel. 3) Fundamenta tu opinión con «porque» y un hecho. 4) Escribe qué le dirías a Daniel.", "1) El libro estaba bajo su banco. Lo entregó en el recreo. 2) Daniel no actuó bien. 3) Porque dijo que lo había encontrado en el pasillo y mintió. 4) Le diría que devolver el libro de inmediato y decir la verdad es mejor que un punto.", ["escribe dos hechos reales del texto", "expresa una opinión", "la fundamenta con un hecho", "da un consejo coherente"], ["cuatro respuestas escritas"], ["opinión sin prueba", "confundir hecho con opinión"], "Compara tu opinión con la de otra persona y busquen qué hecho del texto la apoya en cada caso."),
  "Cuéntale a alguien un cuento y pregúntale su opinión sobre un personaje, pidiéndole una razón.",
  "Escribe tu opinión sobre un personaje de un libro que hayas leído, con dos razones y dos hechos.")

T6a = ("Rosa vio que su perro Chispa se había escapado por el portón mal cerrado. Su hermano Iván estaba rindiendo una prueba importante, así que ella no quiso interrumpirlo. "
       "Salió a buscarlo sola y lo encontró en la plaza, pero volvió tarde. Su madre estaba muy preocupada.")
T6b = ("En otro cuento de la misma autora, Rosa ve que la vecina no puede cargar sus bolsas. No le dice nada a nadie y, sin pensar en la hora, la ayuda a llevarlas. "
       "Su mamá se enoja porque nadie sabía dónde estaba, pero la vecina agradece mucho.")

L(OA4, 6,
  "Este cuaderno, lápiz y los cuentos escritos en esta clase (originales de este cuaderno).",
  "Aprenderé a juzgar las acciones de los personajes con matices: ver la intención, las consecuencias y qué podría haber hecho distinto, y a comparar dos cuentos de una misma autora.",
  ["Fundamento opiniones con hechos.", "Describo personajes y sus rasgos."],
  ["Algunos personajes no son del todo buenos ni del todo malos. Para juzgar sus acciones con matices, mira tres cosas: la intención (qué quería lograr), la acción (qué hizo) y las consecuencias (qué ocurrió después). Una persona puede tener una buena intención y, aun así, cometer un error.",
   "Rosa quiso ayudar a su hermano al no interrumpirlo (buena intención). Salió sola a buscar a Chispa (acción) y su madre se preocupó (consecuencia). Una opinión con matices diría: «Su intención fue buena, pero habría sido mejor avisar a alguien». Así reconoces lo bueno y lo que podría mejorarse.",
   "También puedes comparar dos cuentos de una misma autora para ver qué se repite. En ambos cuentos, Rosa ayuda sin avisar, y en ambos hay una preocupación en casa. Esa repetición ayuda a comprender cómo es el personaje y qué quiere mostrar la autora."],
  [("intención", "lo que un personaje quiere lograr con lo que hace"), ("consecuencia", "lo que ocurre a partir de una acción"), ("matiz", "detalle que muestra que algo no es todo bueno ni todo malo"), ("juicio", "opinión que valora una acción")],
  [("Intención, acción y consecuencia", "Lee el cuento: «" + T6a + "» ¿Cuál fue la intención de Rosa al no avisar a Iván?", ["Busco por qué no lo interrumpió.", "Iván rendía una prueba importante.", "Su intención fue no molestarlo."], "No molestar a su hermano durante la prueba"),
   ("Opinión con matices", "Completa: «Rosa tuvo una buena intención, pero ______».", ["La intención fue buena.", "Faltó avisar a alguien.", "La consecuencia fue que su madre se preocupó."], "Pero su madre se preocupó porque no avisó a nadie")],
  [("Juzgar solo por la consecuencia.", "Se olvida la intención.", "Considera qué quería lograr el personaje."), ("Decir que un personaje es totalmente bueno o malo.", "No se ven los matices.", "Reconoce lo que hizo bien y lo que podría mejorar.")],
  ([E("La intención de un personaje, ¿es lo que quiere lograr o lo que ocurrió después?", "Lo que quiere lograr", "Intención es el propósito."),
    E("Lo que ocurre a partir de una acción, ¿es la intención o la consecuencia?", "La consecuencia", "Es el resultado."),
    E("¿Por qué Rosa no avisó a su hermano?", "Porque estaba rindiendo una prueba", "El texto lo dice.")],
   [E("¿Dónde encontró Rosa a Chispa?", "En la plaza", "Lo dice el texto."),
    E("¿Cómo estaba la madre de Rosa al volver?", "Muy preocupada", "El texto lo dice."),
    E("¿Por qué se había escapado Chispa?", "Porque el portón estaba mal cerrado", "Así lo cuenta el texto.")],
   [E("¿Qué quería lograr Rosa al salir sola a buscar a Chispa: encontrarlo o molestar a Iván?", "Encontrarlo", "Quiso recuperar a su perro."),
    E("¿Cuál fue una consecuencia del actuar de Rosa: que su madre se preocupó o que ganó un premio?", "Que su madre se preocupó", "Volvió tarde sin avisar."),
    E("¿Qué pudo hacer Rosa para evitar la preocupación: avisarle a su madre o no buscar a Chispa?", "Avisarle a su madre", "Así habría ayudado y evitado la preocupación.")],
   [E("¿Cuál opinión tiene matices: «Rosa fue mala» o «Rosa tuvo buena intención, pero debió avisar»?", "«Rosa tuvo buena intención, pero debió avisar»", "Reconoce lo bueno y lo que se puede mejorar."),
    E("Si Rosa hubiera interrumpido a Iván, ¿habría sido mejor o peor para él en ese momento?", "Peor", "Estaba en medio de una prueba importante.")],
   [E("En los dos cuentos de la misma autora, ¿qué repite Rosa en su forma de actuar?", "Ayuda sin avisar", "En ambos ayuda sin decirle a nadie."),
    E("En el segundo cuento, ¿cuál es la consecuencia buena y cuál la mala? Elige la buena: «la vecina agradece» o «la mamá se enoja».", "«la vecina agradece»", "La mala consecuencia es el enojo de su mamá.")]),
  [E("Ayudas a un compañero con su mochila, pero llegas tarde a clase sin avisar. Tu intención fue buena. ¿Qué podrías haber hecho para evitar el problema?", "Avisar a la profesora", "Con aviso, ayudar no genera preocupación.")],
  [E("¿Qué es el matiz en un juicio?", "Un detalle que muestra que no es todo bueno ni todo malo", "Permite reconocer varios aspectos."),
   E("¿Qué tres cosas se miran para juzgar una acción con matices?", "La intención, la acción y las consecuencias", "Son los tres elementos de la clase."),
   E("¿Para qué sirve comparar dos cuentos de una misma autora?", "Para ver qué se repite", "Ayuda a conocer al personaje.")],
  ("Lee los dos cuentos de la misma autora: «" + T6a + "» y «" + T6b + "» 1) Escribe la intención de Rosa en cada cuento. 2) Escribe una consecuencia en cada uno. 3) Escribe un juicio con matices sobre lo que hizo Rosa. 4) Escribe una semejanza entre los dos cuentos.", "1) Cuento 1: no molestar a su hermano. Cuento 2: ayudar a la vecina. 2) Cuento 1: la madre se preocupó. Cuento 2: la vecina agradeció y su mamá se enojó. 3) Rosa quiso ayudar, pero debió avisar. 4) En ambos cuentos ayuda sin avisar a su familia.", ["identifica la intención en ambos", "señala consecuencias", "da un juicio con matices", "compara los dos cuentos"], ["cuatro respuestas escritas"], ["juzgar solo la consecuencia", "no comparar"], "Explica tu juicio a otra persona y pregúntale si está de acuerdo con la parte buena y con la parte que se puede mejorar."),
  "Piensa en una vez en que quisiste ayudar y causaste un problema. Escribe qué harías distinto.",
  "Escribe un cuento breve donde una buena intención tenga una consecuencia no esperada.")
