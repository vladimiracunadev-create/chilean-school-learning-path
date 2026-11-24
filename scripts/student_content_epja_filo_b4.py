"""Filosofía EPJA Media N1 y N2, módulo 2, OAD-08: elaborar una posición respecto del problema filosófico de la libertad. Textos de ejemplo originales (paráfrasis breves); todo en papel."""
from __future__ import annotations

from epja_filo_b_common import make_K

K = make_K()
O = "EPJA-FILO-NM1y2-OAD-08"

# ====================================================== clase 1
F = ("Ficha 10 (textos de ejemplo, escritos para esta ficha; no son citas de ningún autor). "
     "Texto 1, inspirado en el determinismo: «Todo lo que ocurre, incluidas nuestras acciones, tiene causas anteriores que lo hacen necesario; si conociéramos todas las causas, podríamos prever lo que alguien hará.» "
     "Texto 2, inspirado en la idea de libre albedrío: «Aunque haya condiciones que influyen, la persona puede elegir entre varias opciones y su elección no queda fijada de antemano.» "
     "Texto 3: «Una persona es libre cuando nadie la obliga ni la amenaza para que actúe de cierta manera.»")
K(O, 1, F,
  "Hoy aprenderé el vocabulario del problema de la libertad: coacción, libre albedrío, determinismo y responsabilidad, y reconocer tres ideas sobre ella.",
  ["El problema de la libertad pregunta si las personas pueden elegir lo que hacen. Hay dos sentidos de la palabra. La libertad externa es no ser obligada ni amenazada, es decir, no sufrir coacción. La libertad interna, o libre albedrío, es la capacidad de elegir entre varias opciones. Distinguirlas evita discusiones en que cada persona habla de una cosa distinta.",
   "El determinismo es la idea de que todo lo que ocurre, incluidas las acciones humanas, tiene causas anteriores que lo hacen necesario. Condicionar no es lo mismo que determinar. Un horario de transporte limita a qué hora puedes salir, pero no decide por ti. Condicionar es influir; determinar sería dejar una sola posibilidad. Esa diferencia es clave para pensar el tema.",
   "La responsabilidad es la capacidad de responder por lo que se hace. Muchas personas piensan que solo se puede atribuir responsabilidad a quien pudo actuar de otro modo. Si eso es cierto, el problema de la libertad afecta lo que pensamos sobre premios, culpas y decisiones del trabajo y la comunidad. No hay una única respuesta; hay posiciones con razones."],
  [("coacción", "obligar o amenazar a alguien para que actúe de cierta manera"), ("libre albedrío", "capacidad de elegir entre varias opciones"), ("determinismo", "idea de que todo, incluidas las acciones, tiene causas que lo hacen necesario"), ("condicionar", "influir en una decisión sin fijar una sola posibilidad"), ("responsabilidad", "capacidad de responder por lo que se hace")],
  [("Coacción o no", "Una persona ficticia firma un papel porque le advirtieron que perdería su empleo si no lo hacía. ¿Hay coacción?", ["La amenaza es un modo de obligar.", "Firma por una amenaza: hay coacción."], "Sí, hay coacción"),
   ("Condicionar o determinar", "Un bus pasa cada 30 minutos. ¿El horario condiciona o determina a qué hora sales?", ["Limita tus opciones, pero puedes tomar otro medio o salir antes.", "No deja una sola posibilidad."], "Condiciona")],
  [("Creer que «libre» solo significa que nadie te obliga.", "Se mira un único sentido de la palabra.", "También se discute si podemos elegir entre varias opciones: el libre albedrío."),
   ("Pensar que cualquier influencia anula la libertad.", "Se confunde condicionar con determinar.", "Una influencia puede dejar varias opciones abiertas.")],
  [("abc", "En Filosofía: la coacción es", "obligar o amenazar a alguien para que actúe de cierta manera", "elegir entre varias opciones", "una explicación de causas anteriores", "La coacción limita la libertad externa."),
   ("abc", "{F} ¿Qué texto sostiene que las acciones tienen causas que las hacen necesarias?", "El texto 1", "El texto 2", "El texto 3", "Habla de causas anteriores que hacen necesario lo que ocurre."),
   ("ab", "{F} ¿Qué texto describe la libertad externa?", "El texto 3, porque habla de no ser obligado ni amenazado", "El texto 1, porque habla de causas anteriores", "Libertad externa es ausencia de coacción."),
   ("abc", "{F} ¿Qué texto afirma que la persona puede elegir entre varias opciones?", "El texto 2", "El texto 1", "El texto 3", "Eso es lo que sostiene la idea de libre albedrío."),
   ("abc", "El libre albedrío es", "la capacidad de elegir entre varias opciones", "no sufrir obligación ni amenaza", "tener causas anteriores que lo hacen necesario", "Es el sentido interno de la libertad."),
   ("abc", "Una persona ficticia decide no viajar porque el pasaje le parece muy caro. ¿Hay coacción?", "No: el precio condiciona su decisión, pero nadie la obliga ni la amenaza", "Sí: el precio la obliga a no viajar", "Sí: toda influencia es una coacción", "Coacción es obligar o amenazar; un precio influye, pero no obliga."),
   ("ab", "Una persona ficticia elige entre dos trabajos: uno paga más y el otro queda más cerca de su casa. Esas diferencias", "condicionan su elección sin fijar una sola opción", "determinan que elija el que paga más", "Influyen, pero ambas opciones siguen abiertas."),
   ("abc", "Según el determinismo de la ficha, si se conocieran todas las causas, se podría", "prever lo que una persona hará", "garantizar que nadie haga nada", "eliminar toda coacción", "Esa es la consecuencia que el texto menciona."),
   ("abc", "¿Qué significa responsabilidad en la ficha?", "Poder responder por lo que se hace", "No haber elegido nada", "Tener causas anteriores", "Es la capacidad de responder por los propios actos."),
   ("abc", "Un principio dice: «Solo se puede hacer responsable a quien pudo actuar de otro modo». Una persona ficticia llega tarde porque un paro total cerró todos los caminos y no había ninguna forma de llegar a tiempo. Según el principio, ¿es responsable de llegar tarde?", "No, porque no pudo actuar de otro modo", "Sí, porque llegó después de la hora", "Sí, porque el principio no se aplica a las llegadas tardías", "El caso dice que no había ninguna forma de llegar a tiempo, así que el principio excluye la responsabilidad."),
   ("abc", "Alguien dice: «Que me influya mi barrio demuestra que no soy libre». ¿Qué distinción falta?", "Entre condicionar y determinar", "Entre innato y adquirido", "Entre premisa y conclusión", "Una influencia no siempre fija una sola opción."),
   ("ab", "La pregunta «¿puede una persona elegir distinto de lo que eligió?» es", "una pregunta filosófica sobre el libre albedrío", "una pregunta factual con un dato", "No se responde con un dato, sino con razones sobre la libertad."),
   ("abc", "{F} ¿Con qué texto coincide quien dice «aunque mi horario me limita, yo decido cómo organizar mi día»?", "Con el texto 2", "Con el texto 1", "Con ninguno", "Reconoce condiciones y afirma capacidad de elegir.")],
  ("abc", "En una conversación, alguien dice: «No tuve libertad: me obligaron». ¿A qué sentido de libertad se refiere?", "A la libertad externa, por la coacción", "A que no tiene causas anteriores", "A que no puede elegir ningún día", "Dice que alguien lo obligó, es decir, coacción."),
  [("En Filosofía: ¿qué es la coacción?", "Obligar o amenazar a alguien para que actúe de cierta manera", "Es lo que limita la libertad externa."),
   ("¿Qué diferencia hay entre condicionar y determinar?", "Condicionar influye; determinar deja una sola posibilidad", "Una influencia no siempre elimina las opciones."),
   ("¿Qué es el libre albedrío?", "La capacidad de elegir entre varias opciones", "Es el sentido interno de la libertad.")],
  ("{F} Elige uno de los tres textos y escribe: (1) qué afirma, con tus palabras, (2) una situación de trabajo o de la vida diaria (puede ser ficticia) que lo ilustre y (3) una pregunta que te surja sobre la libertad. Todavía no hace falta que tomes posición.",
   "Texto 3. Afirma que alguien es libre cuando no lo obligan ni lo amenazan. Ejemplo: un trabajador que puede cambiar de turno sin que lo sancionen. Pregunta: ¿se puede ser libre si faltan opciones, aunque nadie obligue?",
   ["reformula el texto con claridad", "da un ejemplo adecuado", "formula una pregunta abierta sobre la libertad"],
   ["texto breve con las tres partes numeradas"],
   ["copiar el texto sin reformularlo", "dar un ejemplo que no ilustra la idea"],
   "Revisa que el ejemplo corresponda al texto elegido. Si la pregunta se responde con un dato, pide que empiece con «¿qué...?» o «¿en qué caso...?»."),
  "Escribe un ejemplo de coacción y uno de condicionamiento que no sea coacción.",
  "Explica con tus palabras por qué condicionar no es lo mismo que determinar.")

# ====================================================== clase 2
F = ("Ficha 11 (textos de ejemplo, escritos para esta ficha; paráfrasis breves). "
     "Argumento determinista: «P1: toda acción tiene una causa anterior. P2: lo que tiene una causa anterior no podría haber sido distinto. Conclusión: ninguna acción podría haber sido distinta.» "
     "Perspectiva libertarista (libre albedrío): «Las personas pueden iniciar acciones que no quedan fijadas por causas anteriores.» "
     "Perspectiva compatibilista, defendida entre otros por David Hume: «Actuar libremente es actuar según los propios deseos sin coacción, aunque esas acciones tengan causas.» "
     "Perspectiva existencialista, inspirada en Jean-Paul Sartre: «No podemos escapar de elegir: incluso no elegir es una elección, y por eso somos responsables.»")
K(O, 2, F,
  "Hoy practicaré, con apoyo, cómo se comparan cuatro perspectivas sobre la libertad y cómo se analiza un argumento sobre ella.",
  ["La ficha trae cuatro perspectivas. El determinismo sostiene que las acciones no podrían ser distintas porque tienen causas necesarias. El libertarismo, o defensa del libre albedrío, sostiene que algunas acciones no quedan fijadas por causas anteriores. El compatibilismo sostiene que ser libre es actuar según los propios deseos sin coacción, aunque haya causas. El existencialismo sostiene que no podemos evitar elegir.",
   "Un argumento es válido cuando, si sus premisas fueran verdaderas, la conclusión necesariamente se seguiría. Que sea válido no obliga a aceptarlo: se pueden discutir sus premisas. Un libertarista puede negar la premisa 2, diciendo que no toda causa vuelve necesaria una acción. Un compatibilista puede aceptar las premisas y negar que de ellas se siga que no somos libres en el sentido que importa.",
   "Para tomar posición con razones se puede elegir una perspectiva, combinarla o criticarla, siempre mostrando por qué. Dialogar sobre libertad exige empatía: muchas personas viven condiciones muy distintas, y una idea que parece sencilla para una persona puede ser difícil para otra. Se examinan las ideas, se agradecen las objeciones y se mantiene la posibilidad de reelaborar la propia visión."],
  [("determinismo", "idea de que las acciones tienen causas que las hacen necesarias"), ("libertarismo", "idea de que existe libre albedrío no fijado por causas anteriores"), ("compatibilismo", "idea de que ser libre es compatible con tener causas, si no hay coacción"), ("existencialismo", "corriente que destaca que debemos elegir y responsabilizarnos"), ("argumento válido", "aquel cuya conclusión se sigue necesariamente de sus premisas")],
  [("Premisas y conclusión", "Argumento: «P1: toda herramienta de la obra puede perderse. P2: lo que puede perderse conviene guardarlo. Conclusión: toda herramienta de la obra conviene guardarla». ¿Cuál es la conclusión?", ["La conclusión se indica con esa palabra.", "Es: toda herramienta de la obra conviene guardarla."], "Toda herramienta de la obra conviene guardarla"),
   ("Qué niega cada perspectiva", "En el argumento determinista, P1 dice que toda acción tiene una causa anterior y P2 que lo que tiene una causa anterior no podría ser distinto. Una persona libertarista dice: «Una causa puede influir en una acción sin volverla necesaria». ¿Qué premisa niega?", ["Habla de si la causa hace necesario lo que ocurre.", "Eso es lo que afirma la premisa 2."], "La premisa 2")],
  [("Creer que un argumento válido es siempre verdadero.", "Se confunde validez con verdad de las premisas.", "Un argumento válido puede tener premisas falsas; hay que examinarlas."),
   ("Tratar de «ingenua» a una perspectiva en lugar de examinar sus razones.", "Se descalifica en vez de analizar.", "Examina qué razón da y qué objeción enfrenta.")],
  [("abc", "{F} ¿Qué afirma la premisa 1 del argumento determinista?", "Que toda acción tiene una causa anterior", "Que toda acción es libre", "Que ninguna acción tiene causa", "Es lo que dice la primera premisa."),
   ("abc", "{F} ¿Cuál es la conclusión del argumento determinista?", "Ninguna acción podría haber sido distinta", "Toda acción tiene una causa anterior", "Hay coacción en todas las acciones", "Es lo que se obtiene de las premisas."),
   ("ab", "{F} ¿Cuántas premisas tiene el argumento determinista?", "Dos", "Una", "Las premisas son P1 y P2."),
   ("abc", "{F} ¿Qué perspectiva dice que ser libre es actuar según los propios deseos sin coacción, aunque haya causas?", "El compatibilismo", "El libertarismo", "El determinismo estricto", "Acepta causas y libertad al mismo tiempo."),
   ("abc", "{F} ¿Qué perspectiva sostiene que incluso no elegir es una elección?", "El existencialismo", "El determinismo", "El compatibilismo", "Es la idea existencialista de la ficha."),
   ("abc", "{F} ¿Qué perspectiva defiende que algunas acciones no quedan fijadas por causas anteriores?", "El libertarismo", "El compatibilismo", "El determinismo", "Afirma un libre albedrío no fijado por causas."),
   ("abc", "Un argumento es válido cuando", "la conclusión se sigue necesariamente de sus premisas", "sus premisas son siempre verdaderas", "lo escribe una persona conocida", "La validez habla de la relación entre premisas y conclusión."),
   ("ab", "Un argumento válido con una premisa falsa", "puede tener una conclusión que no hay que aceptar", "siempre tiene conclusión verdadera", "Para aceptar la conclusión, las premisas también deben ser verdaderas."),
   ("abc", "Un compatibilista puede aceptar la premisa 1 del argumento determinista porque", "para él las causas no impiden actuar libremente sin coacción", "cree que no hay ninguna causa", "niega toda libertad", "Distingue entre tener causas y ser obligado."),
   ("abc", "Una persona objeta al libertarismo: «Si mis acciones no tuvieran causa, serían azarosas, no mías». ¿Qué hace?", "Plantea una razón en contra de esa perspectiva", "Confirma el determinismo con un dato", "Ataca a quien defiende el libertarismo", "Es una objeción con razón, no un ataque."),
   ("abc", "Alguien responde a la objeción anterior: «Una elección es mía aunque no esté fijada, porque la hago yo con mis razones». ¿Qué hace?", "Responde la objeción con una razón", "Cambia de tema", "Ataca a quien objetó", "Mantiene la perspectiva con una razón."),
   ("abc", "Una persona dice: «Tu perspectiva es ingenua». ¿Qué le falta a esa frase?", "Examinar la razón de la perspectiva", "Decirlo con más seguridad", "Citar a una persona conocida", "Descalifica a la perspectiva sin considerar su contenido."),
   ("abc", "{F} ¿Qué perspectiva destaca más la responsabilidad que viene de elegir?", "El existencialismo", "El determinismo estricto", "El compatibilismo sin coacción", "Dice que somos responsables porque no podemos evitar elegir.")],
  ("abc", "Una vecina ficticia dice: «Mis ingresos limitan mis opciones, pero igual elijo entre las que tengo, y por eso me hago cargo de lo que elijo». ¿Qué perspectiva se parece más a la suya?", "El existencialismo, que destaca elegir y responsabilizarse", "El determinismo estricto", "Ninguna, porque no da razón", "Reconoce condiciones y se responsabiliza de elegir."),
  [("En Filosofía: ¿qué es el determinismo?", "La idea de que las acciones tienen causas que las hacen necesarias", "Niega que pudiera haber sido de otra manera."),
   ("¿Qué es un argumento válido?", "Aquel cuya conclusión se sigue de sus premisas", "No dice nada sobre si las premisas son verdaderas."),
   ("¿Qué sostiene el compatibilismo?", "Que ser libre es compatible con tener causas, si no hay coacción", "Acepta causas y libertad a la vez.")],
  ("{F} Elige una de las cuatro perspectivas y escribe: (1) qué sostiene, (2) una razón a su favor, (3) una objeción que le harías y (4) cómo la perspectiva podría responder. Puedes usar un ejemplo de trabajo, ficticio o no.",
   "Compatibilismo. Sostiene que ser libre es actuar según los propios deseos sin coacción. A favor: distingue las amenazas, que sí quitan libertad, de las causas en general. Objeción: ¿y si mis deseos fueron instalados por otros? Respuesta: aun así, si los reconozco como míos y no hay coacción, actúo libremente en el sentido importante.",
   ["resume con fidelidad la perspectiva elegida", "da una razón a favor", "formula una objeción con razón", "propone una respuesta posible"],
   ["texto de cuatro partes numeradas"],
   ["resumir mal la perspectiva", "dar una objeción sin razón"],
   "Revisa que el resumen sea fiel a la ficha. Si la objeción no da una razón, pide que agregue «porque». Reconoce una respuesta bien conectada con la objeción."),
  "Resume cada perspectiva en una frase breve con tus palabras.",
  "Escribe una objeción al compatibilismo y una posible respuesta.")

# ====================================================== clase 3
F = ("Ficha 12 (caso de ejemplo, personajes ficticios). Héctor es conductor de reparto y llegó tarde tres veces este mes. Su jefa, Irene, quiere sancionarlo. "
     "Hechos del caso: Héctor trabaja turnos largos, vive lejos y el transporte que usa tiene pocas salidas por la mañana; también pudo haber salido antes, pero no lo hizo. Nadie lo obligó a llegar tarde. "
     "Principio P: «Solo se puede hacer responsable a quien pudo actuar de otro modo.» "
     "Irene: «Se sanciona, porque pudo salir antes.» Mateo, compañero: «Con esos turnos y ese transporte, no se le puede hacer responsable de todo.»")
K(O, 3, F,
  "Hoy aplicaré las perspectivas sobre la libertad a un caso de trabajo y elaboraré una posición propia, con una razón, un ejemplo y una objeción respondida.",
  ["El caso de Héctor muestra por qué el problema de la libertad importa en la vida diaria. Para decidir si es responsable hay que preguntar si pudo actuar de otro modo. Irene dice que sí, porque pudo salir antes. Mateo recuerda que sus condiciones limitan sus opciones. Ambos usan el principio P, pero evalúan de manera distinta cuánto pesan las condiciones.",
   "Para analizar el caso se separan tres cosas. Los hechos que el caso entrega: turnos largos, transporte con pocas salidas, ausencia de coacción, posibilidad de salir antes. El principio que se aplica: solo hay responsabilidad si se pudo actuar de otro modo. Y la conclusión que cada persona saca. Un buen análisis comprueba que la conclusión se siga de los hechos y del principio.",
   "Condicionar no es determinar, y la responsabilidad puede ser mayor o menor según cuántas opciones había. Esta idea permite tomar posiciones matizadas. Elaborar una posición sobre la libertad exige una tesis, una razón, un ejemplo que la fortalezca y una respuesta a una objeción. Quien se arriesga a tomar posición también acepta que puede cambiar si aparece una razón mejor."],
  [("hecho", "dato del caso que se puede comprobar en el texto"), ("principio", "idea general que se usa para evaluar los casos"), ("matiz", "diferencia de grado que evita una respuesta de todo o nada"), ("tesis", "posición que se sostiene con razones"), ("responsabilidad", "capacidad de responder por lo que se hace")],
  [("Hecho o principio", "En el caso de Héctor, el texto dice: «Nadie lo obligó a llegar tarde». ¿Es un hecho del caso o un principio?", ["Es un dato que el caso entrega.", "No es una idea general."], "Un hecho"),
   ("Aplicar un principio", "Principio Q: «Quien no recibió un aviso no puede ser culpado por no actuar según él». María, personaje ficticio, no recibió el aviso de cambio de turno y llegó a la hora antigua. Según Q, ¿se le puede culpar?", ["Q habla de quien no recibió el aviso.", "María no lo recibió."], "No, no se le puede culpar")],
  [("Sacar una conclusión que no se sigue de los hechos.", "No se revisa si el principio y los hechos la apoyan.", "Comprueba que la conclusión se siga de los hechos y del principio."),
   ("Responder «todo o nada» sobre la responsabilidad.", "No se considera que las opciones pueden ser más o menos limitadas.", "Considera que la responsabilidad puede ser mayor o menor según las opciones que había.")],
  [("abc", "{F} ¿Cuál de estas frases es un hecho del caso?", "Héctor llegó tarde tres veces este mes", "Hay que sancionar a todos los que llegan tarde", "Las personas siempre pueden salir antes", "Las otras son principios o juicios, no hechos del caso."),
   ("abc", "{F} ¿Cuál es el principio P?", "Solo se puede hacer responsable a quien pudo actuar de otro modo", "Todos los conductores deben llegar temprano", "Nadie es responsable de nada", "Es la idea general que se usa para juzgar el caso."),
   ("ab", "{F} ¿Hubo coacción en que Héctor llegara tarde?", "No, porque el caso dice que nadie lo obligó", "Sí, porque trabaja turnos largos", "La coacción es obligar o amenazar, y el caso lo descarta."),
   ("abc", "{F} ¿Qué razón da Irene para sancionar?", "Que Héctor pudo salir antes", "Que Héctor es un mal trabajador", "Que el transporte falla siempre", "Su razón es que tenía la posibilidad de actuar distinto."),
   ("abc", "{F} ¿Qué razón da Mateo contra la sanción completa?", "Que los turnos y el transporte limitan las opciones de Héctor", "Que nadie debe llegar nunca tarde", "Que Irene es injusta por ser jefa", "Su razón apunta a las condiciones que limitan sus opciones."),
   ("abc", "{F} Si se acepta P y se acepta que Héctor pudo salir antes, ¿qué se sigue sobre su responsabilidad?", "Que P no excluye atribuirle responsabilidad", "Que P excluye toda responsabilidad de Héctor", "Que Irene es responsable de todo", "P solo dice que sin poder actuar distinto no hay responsabilidad; como pudo salir antes, esa exclusión no se aplica."),
   ("ab", "{F} Mateo dice que no se le puede hacer responsable «de todo». ¿Qué tipo de afirmación es?", "Una afirmación que matiza el grado de responsabilidad", "Una negación total de la responsabilidad", "Dice «de todo», no «de nada», por lo que reconoce una parte."),
   ("abc", "¿Qué diferencia hay entre condicionar y determinar en el caso?", "Los turnos y el transporte condicionan, pero no fijan una única opción", "Los turnos fijan una única opción", "No hay ninguna diferencia", "El caso dice que también pudo salir antes."),
   ("abc", "Alguien dice: «Como Mateo es compañero de Héctor, su idea no vale». ¿Qué error comete?", "Descalifica a la persona sin examinar su razón", "Usa un hecho del caso", "Aplica el principio P", "No examina las razones que da Héctor."),
   ("abc", "Un compatibilista, ante el caso, diría que Héctor actuó libremente si", "actuó según sus propios deseos y sin coacción", "no tuvo causas anteriores", "nunca influyeron las condiciones", "Para esa perspectiva basta la ausencia de coacción."),
   ("abc", "Un defensor del determinismo estricto diría que Héctor", "no podía haber actuado de otro modo, dadas las causas", "siempre pudo elegir sin ninguna influencia", "tiene toda la responsabilidad por elegir", "Según el determinismo, las causas hacían necesaria su acción."),
   ("abc", "Un existencialista destacaría en el caso que", "Héctor debe responsabilizarse de lo que elige, pese a las condiciones", "las condiciones eliminan toda elección", "nadie elige nunca", "Pone el acento en elegir y asumir las consecuencias."),
   ("abc", "Una posición bien elaborada sobre el caso incluye", "tesis, razón, ejemplo y respuesta a una objeción", "solo una frase con «yo creo»", "una cita larga sin explicar", "Ese es el conjunto mínimo de partes de una posición argumentada.")],
  ("abc", "Una operaria ficticia dice: «Elijo cada día aprender más en mi trabajo, aunque la empresa me asigne tareas; las tareas no las elijo, pero sí cómo las hago». ¿Qué idea expresa?", "Que hay libertad dentro de condiciones que no se eligen", "Que no existe ninguna libertad", "Que no hay condiciones", "Distingue lo que se impone de lo que aún se puede elegir."),
  [("En Filosofía: ¿qué es un principio?", "Una idea general que se usa para evaluar casos", "Un principio se aplica a hechos concretos del caso."),
   ("En Filosofía: ¿qué es un matiz?", "Una diferencia de grado que evita responder todo o nada", "Permite hablar de más o menos responsabilidad."),
   ("¿Qué partes tiene una posición argumentada?", "Tesis, razón, ejemplo y respuesta a una objeción", "Con ellas se puede examinar y discutir.")],
  ("{F} Toma posición sobre esta pregunta: «¿Qué grado de responsabilidad tiene Héctor, y qué dice eso sobre la libertad?». Escribe una tesis, una razón, un ejemplo (puede ser de otro personaje ficticio o de tu experiencia, si quieres), una objeción y tu respuesta. Si lo deseas, apóyate en alguna perspectiva de la clase anterior.",
   "Tesis: Héctor tiene responsabilidad parcial. Razón: pudo salir antes, pero sus condiciones limitaban sus opciones. Ejemplo: alguien que llega tarde por un único bus tiene menos opciones que quien dispone de varios. Objeción: «si no fue obligado, es totalmente responsable». Respuesta: no ser obligado quita la coacción, pero no elimina el peso de las condiciones.",
   ["formula una tesis clara", "da una razón conectada con los hechos del caso", "ofrece un ejemplo que fortalece la tesis", "plantea una objeción y la responde con razón"],
   ["texto de siete a diez líneas con las cuatro partes marcadas"],
   ["tesis sin razón", "ignorar los hechos del caso", "responder la objeción con un ataque"],
   "Evalúa la calidad argumentativa y la coherencia con los hechos, no la posición elegida. Si no usa los hechos del caso, pide que cite al menos dos. Reconoce el matiz cuando aparece."),
  "Escribe tres hechos del caso y dos juicios que no sean hechos.",
  "Escribe una objeción a la posición de Mateo y una respuesta con razón.")
