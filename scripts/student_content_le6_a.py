"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación, OA 01 (lectura fluida).

Todos los textos son originales y breves; cada ejercicio trae el texto que necesita.
Aquí se definen también los ayudantes `L`, `E`, `task`, `n_words`, `syl`, `cnt` que reutilizan los otros módulos le6_a*.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1 = "LE06 OA 01"
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


def syl(word):
    """Cuenta las sílabas de una palabra ya separada con guiones."""
    return str(len(word.split("-")))


def cnt(text, sign):
    """Cuenta cuántas veces aparece un signo en un texto."""
    return str(text.count(sign))


MAT = "Este cuaderno, lápiz y los textos escritos en cada ejercicio. Si quieres, un reloj con segundero."

# ------------------------------------------------------------------ OA 01
L(OA1, 1,
  MAT,
  "Aprenderé a preguntarme para qué voy a leer un texto y qué palabras o signos me pueden hacer tropezar, para preparar una lectura en voz alta clara y precisa.",
  ["Leo en voz alta con precisión.", "Separo palabras largas en sílabas."],
  ["Leer de manera fluida significa tres cosas a la vez: decir cada palabra con precisión, respetar la música de la voz que marcan los signos de puntuación (la prosodia) y reconocer casi todas las palabras de un vistazo, sin deletrearlas. En sexto básico los textos traen palabras largas y más variedad de signos.",
   "Antes de leer en voz alta conviene hacerse dos preguntas. La primera es el propósito: ¿para qué leo? Puede ser para informar a otras personas, para entretener o para enterarme de un dato. La segunda es el desafío: ¿qué palabras largas, nombres o signos me pueden hacer tropezar?",
   "Para descubrir el desafío, recorre el texto con la vista. Marca con lápiz las palabras largas o poco conocidas y los signos que no sueles usar, como el punto y coma o los paréntesis. Luego practica solo esas partes. Prepararte así te permite leer sin detenerte y con seguridad."],
  [("fluidez", "leer con precisión, buen ritmo y buena entonación"), ("prosodia", "la música de la voz: pausas, fuerza y tono"), ("propósito", "para qué se hace algo, por ejemplo para qué se lee"), ("desafío", "la parte difícil que hay que preparar")],
  [("Descubrir el desafío", "Vas a leer en voz alta: «El electricista revisó el funcionamiento de la antena.» ¿Qué palabras debes practicar?",
    ["Recorro el texto y busco palabras largas.", "Encuentro «electricista», «funcionamiento» y «antena».", "Elijo las dos más largas para practicar por sílabas: «electricista» y «funcionamiento»."],
    "Practico «electricista» y «funcionamiento»"),
   ("Reconocer el propósito", "Una compañera leerá a su curso: «El ensayo del acto será el martes a las 10:15.» ¿Cuál es su propósito?",
    ["Es un aviso con datos concretos.", "Quienes escuchan necesitan el día y la hora.", "Entonces el propósito es informar, y debe leer despacio y claro."],
    "Informar al curso")],
  [("Leer un texto en voz alta sin mirarlo antes.", "Se cree que se puede descubrir el desafío mientras se lee.", "Recorre el texto antes y marca palabras y signos difíciles."),
   ("Practicar solo las palabras fáciles.", "Se escogen las que ya se saben.", "Practica las palabras largas o desconocidas, que son las que hacen tropezar.")],
  ([E("¿Cuántas sílabas tiene «responsabilidad» (res-pon-sa-bi-li-dad)?", syl("res-pon-sa-bi-li-dad"), "Se cuentan las partes separadas por guiones."),
    E("Si lees una receta para saber cuánto azúcar necesitas, ¿tu propósito es informarte o pasar el rato?", "Informarte", "Lees para obtener un dato concreto."),
    E("Una lectora dijo «aeroporto» donde el texto dice «aeropuerto». ¿Qué cambió: «ue» por «o» o «p» por «b»?", "«ue» por «o»", "La precisión exige decir las letras tal como están escritas.")],
   [E("En «Mañana el curso presentará una obra sobre la historia del barrio.», ¿cuál es la palabra más larga?", "presentará", "Tiene 10 letras; «historia» tiene 8."),
    E("Vas a leer un aviso en voz alta ante todo el colegio. ¿Qué debe cuidar más tu lectura: que se entienda cada palabra o que termines primero?", "Que se entienda cada palabra", "El propósito del aviso es informar."),
    E("Antes de leer en voz alta, ¿qué conviene hacer con una palabra larga que no conoces: saltarla o practicarla por sílabas?", "Practicarla por sílabas", "Así la dices completa y sin cambiarla.")],
   [arith("Un artículo tiene 180 palabras y marcaste 9 como difíciles. ¿Cuántas palabras no marcaste?", "180-9", "Se restan las difíciles del total."),
    E("¿Cuántas palabras tiene «Los buzos exploraron el casco hundido del barco durante toda la tarde.»?", n_words("Los buzos exploraron el casco hundido del barco durante toda la tarde."), "Se cuenta cada palabra separada por espacios."),
    E("¿Cuántas sílabas tiene «funcionamiento» (fun-cio-na-mien-to)?", syl("fun-cio-na-mien-to"), "Se cuentan los golpes de voz: fun, cio, na, mien, to.")],
   [E("Dos estudiantes preparan la misma noticia. Ana marca y practica sus palabras largas; Bruno la lee de corrido, sin verla antes. ¿Quién se preparó mejor para el desafío?", "Ana", "Ella identificó las partes difíciles antes de leer."),
    E("«Leo para saber a qué hora parte el bus» y «leo para pasar el rato con un cuento». ¿En cuál debes revisar con más cuidado los números?", "En el del bus", "Un número mal leído cambia el dato que buscas.")],
   [arith("Un artículo tiene 240 palabras. En la primera lectura tuviste 12 errores y en la segunda, 5. ¿Cuántas palabras más leíste bien en la segunda lectura?", "(240-5)-(240-12)", "Se comparan las palabras bien leídas de cada intento."),
    E("¿Cuál tiene más sílabas, «electrodoméstico» (e-lec-tro-do-més-ti-co) o «extraordinario» (ex-tra-or-di-na-rio)? Responde la palabra y cuántas sílabas más tiene.", "Electrodoméstico, con 1 sílaba más", "Tiene 7 sílabas y la otra, 6.")]),
  [E("Se informa a las familias que la reunión del jueves comenzará a las 18:30 horas en el gimnasio. Vas a leer este aviso por el parlante. ¿Cuántos datos distintos sobre cuándo ocurre la reunión no puedes equivocar?", "2", "El día, jueves, y la hora, 18:30.")],
  [E("¿Qué pregunta nos ayuda a elegir cómo leer: ¿para qué leo?, o ¿cuánto pesa el libro?", "¿Para qué leo?", "Esa pregunta define el propósito de la lectura."),
   E("¿Cómo se llama la parte del texto que puede hacerte tropezar y que conviene practicar antes?", "El desafío", "Son las palabras o signos difíciles."),
   E("¿Qué es la prosodia: la música de la voz o el significado de una palabra?", "La música de la voz", "Incluye pausas, fuerza y tono.")],
  ("Este es el texto que leerás: «En la ladera del volcán, los guías explican a los visitantes que no deben salirse del sendero señalizado.» 1) Marca las tres palabras que te parezcan más difíciles y sepáralas en sílabas. 2) Escribe en una frase el propósito de leer este texto a un grupo de visitantes. 3) Léelo dos veces en voz alta y anota si la segunda lectura te resultó más segura.",
   "Marco «volcán» (vol-cán), «señalizado» (se-ña-li-za-do) y «visitantes» (vi-si-tan-tes). Propósito: informar a los visitantes una regla de seguridad. En la segunda lectura no me detuve en «señalizado».",
   ["marca tres palabras difíciles y las separa bien en sílabas", "formula un propósito coherente con un aviso a visitantes", "compara dos lecturas y lo anota"], ["texto con palabras marcadas", "frase del propósito", "lectura en voz alta ante otra persona"], ["marcar solo palabras cortas", "decir como propósito «leer rápido»"], "Pide a quien te escuche que anote qué palabra te costó más y practícala tres veces."),
  "Lee en voz alta un párrafo de un libro que tengas en casa, marcando antes dos palabras difíciles, y repítelo.",
  "Escribe cinco palabras largas que hayas encontrado esta semana, sepáralas en sílabas y léelas en voz alta.")

L(OA1, 2,
  MAT,
  "Aprenderé a modelar una buena lectura en voz alta: marcar las pausas antes de leer y dar a cada signo de puntuación su pausa y su tono.",
  ["Conozco la coma, el punto, los paréntesis y las comillas.", "Sé que la prosodia es la música de la voz."],
  ["Un lector experto «piensa en voz alta» antes de leer: mira los signos y decide cómo sonará cada parte. La coma pide una pausa corta; el punto, una pausa larga; el punto y coma, una intermedia; los dos puntos anuncian algo que viene; los puntos suspensivos dejan la voz en suspenso.",
   "La raya (—) marca lo que dice un personaje en un diálogo, y el narrador comenta entre rayas. Los paréntesis encierran un comentario aparte que se lee con voz más suave. Las comillas « » muestran palabras exactas de alguien. Los signos ¿? y ¡! cambian el tono: la pregunta sube al final y la exclamación se dice con fuerza.",
   "Una forma de modelar es dibujar marcas sobre el texto: una barra (/) para cada pausa corta y dos barras (//) para cada pausa larga. Después se lee siguiendo las marcas. Si ignoras un signo, puedes cambiar lo que el texto quiere decir."],
  [("pausa", "momento breve en que la voz se detiene"), ("puntos suspensivos", "tres puntos (...) que dejan la idea sin terminar"), ("raya", "signo (—) que marca la voz de un personaje en un diálogo"), ("entonación", "subida y bajada del tono de la voz")],
  [("Marcar las pausas", "Marca las pausas de: «Cuando llegó la tarde, el pueblo entero salió a la plaza. Hubo música, baile y empanadas.»",
    ["La coma después de «tarde» pide una pausa corta: /.", "El primer punto pide una pausa larga: //.", "Las comas de «música, baile» piden pausas cortas; el punto final, una larga."],
    "Cuando llegó la tarde / el pueblo entero salió a la plaza // Hubo música / baile y empanadas //"),
   ("Leer con entonación", "¿Cómo lees «—¿Vienes mañana? —preguntó Clara—. ¡Ojalá!»?",
    ["La pregunta entre ¿? la leo con tono que sube al final.", "El comentario entre rayas («preguntó Clara») lo leo como narración, con voz normal.", "La exclamación ¡Ojalá! la leo con fuerza y emoción."],
    "Pregunta con tono ascendente, narración normal y exclamación fuerte")],
  [("Hacer una pausa larga en cada coma.", "Se cree que toda coma es un punto pequeño.", "La coma pide pausa corta; solo el punto pide la larga."),
   ("Leer la voz del narrador entre rayas con el tono del personaje.", "No se distingue quién habla.", "Lo que va entre rayas y no es diálogo se lee como narración.")],
  ([E("Al leer, ¿qué pausa es más larga: la de la coma o la del punto?", "La del punto", "El punto cierra la oración."),
    E("¿Cuántas comas tiene «Compré pan, queso, jamón y tomates.»?", cnt("Compré pan, queso, jamón y tomates.", ","), "Se cuentan los signos «,» del texto."),
    E("¿Qué signo marca lo que dice un personaje en un diálogo: la raya o el paréntesis?", "La raya", "La raya abre cada intervención.")],
   [E("En «Mi abuelo (el que vive en Osorno) llega hoy.», ¿cómo se lee la parte entre paréntesis: con voz más suave o con un grito?", "Con voz más suave", "Es un comentario aparte."),
    E("En «¡Qué susto!», ¿el tono se lee plano o con fuerza?", "Con fuerza", "Los signos ¡! piden énfasis."),
    E("En «Esperó, esperó, esperó...», ¿qué indican los puntos suspensivos: que la voz queda en suspenso o que termina la lectura?", "Que la voz queda en suspenso", "Dejan la idea abierta, como una espera.")],
   [E("Marca con / cada pausa corta y con // cada pausa larga en: «Llegó el verano, volvieron los pájaros. Todos salimos.» Escribe el texto con las marcas.", "Llegó el verano / volvieron los pájaros // Todos salimos //", "La coma lleva una barra y cada punto, dos."),
    E("¿Cuántas pausas largas (puntos) hay en «Fuimos al cerro. Subimos despacio. Al final, descansamos.»?", cnt("Fuimos al cerro. Subimos despacio. Al final, descansamos.", "."), "Se cuentan los puntos: tres oraciones, tres puntos."),
    E("En «—Hola —dijo Sofía—, ¿cómo estás?», ¿qué palabras no las dice el personaje sino el narrador?", "dijo Sofía", "Están entre rayas y son comentario del narrador.")],
   [E("«Ven, Jorge, rápido.» y «Ven Jorge rápido.». ¿Cuál lleva las pausas que marcan que se le habla a Jorge?", "«Ven, Jorge, rápido.»", "Las comas separan el nombre de la persona a quien se habla."),
    E("Un lector lee «¿Dónde está mi cuaderno?» con el tono plano de una afirmación. ¿Qué signos ignoró?", "Los de interrogación", "¿? piden tono que sube al final.")],
   [E("¿Cuántas barras en total (/ y //) llevará «Al salir, Rosa corrió; el bus ya partía.» si cada coma y el punto y coma llevan una barra y el punto final dos?", "4", "Coma 1, punto y coma 1, punto final 2: 1 + 1 + 2 = 4."),
    E("Dos lectoras leen «Llegó tarde; no pudo entrar.» Una hace la pausa del punto y coma tan larga como la de un punto; la otra la hace intermedia. ¿Cuál lo hace mejor?", "La de la pausa intermedia", "El punto y coma pide una pausa menor que el punto.")]),
  [E("En un cuento, la narradora dice: «Matías gritó desde la cima: ¡Lo logré!». ¿Cuántos signos de dos puntos debes marcar como anuncio de lo que sigue?", cnt("Matías gritó desde la cima: ¡Lo logré!", ":"), "El signo de dos puntos anuncia lo que gritó.")],
  [E("¿Qué marca usas para una pausa corta al preparar el texto?", "Una barra", "Se anota / sobre cada coma."),
   E("¿Qué signo hace subir el tono al final de una pregunta?", "El signo de interrogación", "Ese signo indica la entonación."),
   E("¿Cuál es el signo que deja una idea en suspenso?", "Los puntos suspensivos", "Indican que la voz queda abierta.")],
  ("Copia este texto marcando con / las pausas cortas y con // las largas, y léelo en voz alta: «Anoche llovió mucho; hoy, sin embargo, salió el sol. —¿Vamos al parque? —preguntó Camila—. ¡Sí! —respondió su hermano—. Llevaré la pelota, la cuerda y el jugo.»",
   "Anoche llovió mucho ; hoy / sin embargo / salió el sol // —¿Vamos al parque? —preguntó Camila— // ¡Sí! —respondió su hermano— // Llevaré la pelota / la cuerda y el jugo //. Leo las preguntas con tono ascendente.",
   ["marca pausas cortas y largas en los lugares correctos", "distingue narración y diálogo", "usa tono ascendente en la pregunta y fuerza en la exclamación"], ["texto copiado con marcas", "lectura en voz alta"], ["pausa larga en cada coma", "leer las rayas como diálogo"], "Lee mirando tus marcas y pide a otra persona que levante la mano en cada pausa para comprobar que coinciden."),
  "Elige un párrafo de un cuento que tengas en casa, marca sus pausas y léelo siguiendo tus marcas.",
  "Escribe un diálogo de cuatro líneas con raya, una pregunta y una exclamación y léelo con otra persona.")

L(OA1, 3,
  MAT,
  "Aprenderé a elegir recursos para leer palabras largas o desconocidas: separar en sílabas, buscar el prefijo y la raíz, y releer por grupos de palabras.",
  ["Separo palabras en sílabas.", "Sé que hay palabras que se forman con otras."],
  ["Cuando una palabra larga te frena, puedes elegir entre varios recursos. El primero es separarla en sílabas y leerla por partes: im-pre-sio-nan-te. El segundo es buscar el prefijo, una parte que va al comienzo y cambia el sentido: des- (desorden), re- (reconstruir), in- (increíble), sub- (subterráneo).",
   "El tercer recurso es buscar la raíz, la parte que se repite en una familia de palabras: de «mar» salen «marino», «marinero» y «submarino». Si ya reconoces la raíz, la palabra deja de ser desconocida. El cuarto recurso es releer: vuelve al inicio de la oración y léela por grupos de palabras con sentido.",
   "Elegir bien el recurso ahorra tiempo. Si la palabra es larga pero la reconoces por su raíz, basta con leerla de una vez. Si es totalmente nueva, sepárala por sílabas. La lectura fluida se logra practicando estos recursos hasta que se vuelven automáticos."],
  [("prefijo", "parte que se agrega al comienzo de una palabra y cambia su sentido"), ("raíz", "parte de la palabra que se repite en las de su familia"), ("familia de palabras", "palabras que comparten la misma raíz"), ("recurso", "herramienta o estrategia que ayuda a hacer algo")],
  [("Buscar prefijo y raíz", "¿Cómo te ayuda a leer «desordenado» ver el prefijo y la raíz?",
    ["Busco el comienzo: des-.", "Busco la raíz: «orden».", "Leo «des» + «orden» + «ado» y la palabra deja de ser desconocida."],
    "Se lee por partes: des + orden + ado"),
   ("Separar en sílabas", "¿Cómo lees por sílabas «instrumento»?",
    ["Marco los golpes de voz.", "Separo: ins-tru-men-to.", "Leo cada parte despacio y las uno."],
    "ins-tru-men-to (4 sílabas)")],
  [("Cambiar una palabra desconocida por otra parecida.", "Se cree que da lo mismo cuál se diga.", "Usa un recurso para leer la palabra tal como está escrita."),
   ("Creer que toda palabra que empieza con «re» tiene el prefijo re-.", "Se mira solo el comienzo.", "Comprueba que, al quitarlo, quede una palabra con sentido.")],
  ([E("¿Qué prefijo tiene «reconstruir»?", "re-", "Quitando re- queda «construir»."),
    E("¿Cuál es la raíz que se repite en «marino», «marinero» y «submarino»?", "mar", "Todas las palabras comienzan o contienen esa base."),
    E("¿Cuántas sílabas tiene «impresionante» (im-pre-sio-nan-te)?", syl("im-pre-sio-nan-te"), "Se cuentan las partes separadas por guiones.")],
   [E("Al separar «increíble» queda «in» + «creíble». ¿Qué parte es el prefijo?", "in-", "Está al comienzo y cambia el sentido a «no creíble»."),
    E("¿Qué recurso usarías para una palabra totalmente nueva y larga: separarla en sílabas o adivinarla?", "Separarla en sílabas", "Así la lees completa y sin cambiarla."),
    E("«Panadero», «panadería» y «panera» comparten una raíz. ¿Cuál es?", "pan", "Es la parte que se repite en la familia.")],
   [E("¿Pertenece «librería» a la familia de «libro»: sí o no?", "Sí", "Comparte la raíz «libr-»."),
    E("¿Cuántas sílabas tiene «desordenado» (des-or-de-na-do)?", syl("des-or-de-na-do"), "Se cuentan cinco partes."),
    E("En «subterráneo» el prefijo sub- significa «debajo». ¿Qué significa entonces «submarino»: debajo del mar o sobre el mar?", "Debajo del mar", "Sub- indica que está debajo.")],
   [E("¿Cuál de estas palabras NO es de la familia de «tierra»: «terreno», «enterrar» o «teléfono»?", "teléfono", "No comparte la raíz «terr-» ni el sentido de suelo."),
    E("Un lector lee «destapar» como «desta-par» y se detiene. Otra ve «des» + «tapar» y lee de corrido. ¿Qué recurso usó la segunda?", "Buscar el prefijo y la raíz", "Reconocer des- y «tapar» facilita la lectura.")],
   [E("De las palabras «rehacer», «deshacer» y «hacer», ¿cuántas tienen un prefijo que cambia el sentido?", "2", "Rehacer (re-) y deshacer (des-)."),
    E("Si «des-» indica lo contrario, ¿cómo se dice lo contrario de «armar»?", "Desarmar", "Se agrega el prefijo des- al comienzo.")]),
  [E("Lees en un cartel: «Prohibido desordenar los instrumentos». ¿Qué prefijo tiene «desordenar»?", "des-", "Quitando des- queda «ordenar».")],
  [E("¿Un prefijo se coloca al comienzo o al final de la palabra?", "Al comienzo", "Eso lo distingue de otras partes."),
   E("¿Qué es la raíz de una palabra: la parte que se repite en la familia o la última sílaba?", "La parte que se repite en la familia", "Es la base común."),
   E("¿Cuántas sílabas tiene «instrumento» (ins-tru-men-to)?", "4", "Se cuentan cuatro partes.")],
  ("Te damos cinco palabras: «reconstruir», «submarino», «desorden», «increíble», «montaña». Escribe de cada una el prefijo (o «sin prefijo» si no lo tiene) y sepáralas en sílabas. Luego léelas en voz alta con tus recursos.",
   "reconstruir: re- (re-cons-truir); submarino: sub- (sub-ma-ri-no); desorden: des- (des-or-den); increíble: in- (in-cre-í-ble); montaña: sin prefijo (mon-ta-ña).",
   ["identifica correctamente los prefijos", "separa las palabras en sílabas", "lee cada palabra completa y sin cambiarla"], ["lista escrita", "lectura en voz alta"], ["tratar como prefijo cualquier comienzo parecido", "cambiar sílabas al leer"], "Si dudas en un prefijo, quítalo y comprueba que quede una palabra con sentido."),
  "Busca en un texto cuatro palabras con prefijo, subraya el prefijo y léelas en voz alta.",
  "Escribe una familia de cinco palabras con la raíz «papel» y úsalas en dos oraciones.")

L(OA1, 4,
  MAT,
  "Aprenderé a comparar dos lecturas en voz alta de un mismo texto y a decidir cuál es mejor según la precisión y el respeto a los signos.",
  ["Marco pausas con / y //.", "Sé qué es la precisión al leer."],
  ["Una misma oración puede cambiar de significado según las pausas y la entonación. Comparar lecturas ayuda a ver cómo la voz modifica lo que se entiende. «Vamos a comer, niños» invita a los niños a comer. «Vamos a comer niños» dice otra cosa muy distinta.",
   "Para comparar dos lecturas, se usan criterios: ¿dijo las palabras tal como están escritas?, ¿respetó la pausa de cada signo?, ¿cambió el tono en preguntas y exclamaciones? Se puede dar un punto por cada criterio cumplido y restar un punto por cada error de palabra. Así dos personas pueden ponerse de acuerdo con evidencia.",
   "Comparar no es decir quién lee «más bonito». Es justificar con ejemplos: «En la segunda lectura no hizo pausa en la coma de la línea 2, por eso se entendió distinto». Esa justificación te sirve para mejorar tu propia lectura."],
  [("criterio", "regla o aspecto que se usa para juzgar algo"), ("interpretación", "la forma de entender y expresar un texto"), ("evidencia", "dato observable que respalda una conclusión"), ("énfasis", "mayor fuerza que se da a una palabra al decirla")],
  [("Cambio de sentido por la coma", "¿En qué cambia el sentido entre «Vamos a comer, niños» y «Vamos a comer niños»?",
    ["En la primera, la coma separa a quienes se les habla.", "Se invita a los niños a comer.", "En la segunda, «niños» es lo que se come, lo que no tiene sentido razonable."],
    "La coma cambia quién come y qué se come"),
   ("Comparar dos lecturas con puntaje", "Lectura A: 8 palabras bien leídas de 10 y 4 signos respetados. Lectura B: 10 palabras bien leídas de 10 y 3 signos respetados. Se suma 1 punto por palabra bien leída y 1 por signo respetado. ¿Cuál tiene más puntos?",
    ["A: 8 + 4 = 12.", "B: 10 + 3 = 13.", "Comparo: 13 es mayor que 12."],
    "La lectura B, con 13 puntos")],
  [("Decir que una lectura es mejor porque es más rápida.", "Se olvida la precisión.", "Compara con criterios: palabras, pausas y entonación."),
   ("Juzgar a la persona y no la lectura.", "Se opina sin evidencia.", "Describe lo que escuchaste: «hizo una pausa en…».")],
  ([E("«Perdón, señor» y «Perdón señor». ¿Cuál lleva la coma que separa a la persona a quien se habla?", "«Perdón, señor»", "La coma va antes del nombre de quien escucha."),
    E("Para comparar dos lecturas, ¿sirve un criterio como «respetó los signos» o «me gustó la voz»?", "Respetó los signos", "Es un aspecto observable."),
    E("¿Qué significa «evidencia»: un dato que respalda una conclusión o una opinión sin pruebas?", "Un dato que respalda una conclusión", "Es lo que se puede observar.")],
   [E("Dos personas responden a la pregunta «¿Prefieres quedarte?»: una dice «No, quiero ir» y la otra «No quiero ir». ¿Cuál de las dos quiere ir?", "La que dice «No, quiero ir»", "Con la coma, el «no» responde la pregunta y luego se afirma «quiero ir»."),
    E("Una lectora dice «los pájaros cantaban» como «los pájaros cantaron». ¿Se trata de un error de palabra o de pausa?", "De palabra", "Cambió el verbo, no una pausa."),
    E("Dos lectores tienen 0 errores de palabras. Uno hace todas las pausas de las comas y el otro ninguna. ¿Quién respeta mejor los signos?", "El que hace todas las pausas", "Respetar los signos significa hacer la pausa que cada uno pide.")],
   [arith("Una lectura tuvo 9 palabras bien leídas y 5 signos respetados. Si cada uno vale 1 punto, ¿cuántos puntos suma?", "9+5", "Se suman los dos criterios."),
    arith("Lectura C tiene 14 puntos. Lectura D, 11 palabras bien leídas más 2 signos respetados. ¿Cuántos puntos más tiene C que D?", "14-(11+2)", "Primero se calcula el puntaje de D."),
    E("En «Ayúdame, Julia, por favor.» ¿cuántas pausas cortas (comas) debe hacer el lector?", cnt("Ayúdame, Julia, por favor.", ","), "Se cuentan las comas del texto.")],
   [E("Un compañero dice: «Mi lectura fue mejor porque la terminé primero». ¿Usa un criterio de precisión o de rapidez?", "De rapidez", "Terminar primero no mide palabras bien dichas ni signos respetados."),
    E("Una persona dice: «La segunda lectura fue mejor porque no cambió ninguna palabra y marcó cada pausa». ¿Usa evidencia?", "Sí", "Menciona hechos observables de la lectura.")],
   [E("Lectura E: 12 palabras bien leídas y 6 signos respetados. Lectura F: 13 palabras bien leídas y 4 signos respetados. ¿Cuál suma más y por cuántos puntos?", "E, por 1 punto", "E suma 18 y F suma 17."),
    E("Si una lectura pierde 1 punto por cada error y gana 1 por cada signo respetado, y tiene 3 errores y 7 signos respetados, ¿cuántos puntos tiene?", "4", "7 − 3 = 4.")]),
  [E("En un cartel del colegio dicen: «Silencio, estudiantes trabajando». Un lector lo lee sin hacer la pausa de la coma. ¿Qué dos partes del mensaje se mezclan: la orden y el aviso, o el título y la firma?", "La orden y el aviso", "La coma separa la orden «Silencio» del aviso «estudiantes trabajando».")],
  [E("¿Con qué se comparan dos lecturas: con criterios o con gustos personales?", "Con criterios", "Los criterios son observables."),
   E("¿Cuánto vale 7 palabras bien leídas más 3 signos respetados si cada uno vale 1 punto?", "10", "7 + 3 = 10."),
   E("«Ven, Ana» y «Ven Ana». ¿En cuál se le habla a Ana?", "En «Ven, Ana»", "La coma marca a quien se habla.")],
  ("Lee en voz alta dos veces este texto: «Ayer, en el patio, Daniela encontró un gatito; lo llevó a su casa, le dio leche y lo cuidó. —¿Cómo lo llamarás? —preguntó su madre—. —Nube —respondió ella.» En la primera lectura ignora a propósito las comas; en la segunda, respétalas. Luego escribe qué diferencia notaste y asígnate 1 punto por cada pausa bien hecha.",
   "El texto tiene 3 comas y 1 punto y coma; en la segunda lectura hice todas las pausas, en la primera ninguna. En la primera, «Ayer en el patio Daniela encontró» sonó apurado y se entendía menos.",
   ["lee dos veces con la diferencia pedida", "describe la diferencia con ejemplos", "cuenta las pausas"], ["lectura en voz alta", "texto con las pausas marcadas", "comentario escrito"], ["decir solo que una lectura fue más rápida", "no justificar con ejemplos"], "Escribe la oración exacta donde se notó el cambio y léela otra vez."),
  "Lee a otra persona una oración sin coma y con coma y pídele que cuente en qué cambia lo que entiende.",
  "Inventa dos oraciones cuyo sentido cambie según dónde pongas una coma y léelas de las dos maneras.")

L(OA1, 5,
  MAT,
  "Aprenderé a producir mi propia lectura en voz alta con precisión y signos respetados, y a medir mi avance en palabras bien leídas por minuto.",
  ["Resto errores del total de palabras.", "Divido un número por 2, 3 o 4."],
  ["Producir tu propia lectura significa prepararla, leerla en voz alta y revisar cómo te fue. Para medir tu avance se usa una cifra: las palabras bien leídas por minuto. Se calcula restando los errores a las palabras leídas y dividiendo por los minutos que tardaste.",
   "Por ejemplo, si lees 300 palabras en 3 minutos, lees 100 palabras por minuto. Esa cifra no es una carrera: leer más rápido pero con errores no mejora tu lectura. Lo importante es que la lectura sea precisa, respete los signos y se entienda.",
   "Después de leer, revisa tres cosas: ¿cuántas palabras cambié?, ¿respeté los signos?, ¿qué palabra debo practicar? Anota una meta pequeña para la próxima vez, por ejemplo leer sin errores una oración que antes te costaba. Repetir varias veces hace que las palabras se vuelvan automáticas."],
  [("palabras por minuto", "cantidad de palabras que se leen en un minuto"), ("meta", "lo que quieres lograr en el próximo intento"), ("autocorrección", "volver a una palabra para decirla bien"), ("registro", "anotación de cómo te fue en cada lectura")],
  [("Palabras bien leídas por minuto", "Lees 160 palabras en 2 minutos con 10 errores. ¿Cuántas palabras bien leídas por minuto?",
    ["Resto los errores: 160 − 10 = 150.", "Divido por los minutos: 150 ÷ 2 = 75.", "Respuesta: 75 palabras bien leídas por minuto."],
    "75 palabras bien leídas por minuto"),
   ("Poner una meta", "Tu registro dice: «Lectura 1: 5 errores. Lectura 2: 3 errores.» ¿Qué meta razonable pones para la lectura 3?",
    ["Veo que bajé de 5 a 3 errores.", "Pienso en un paso pequeño: bajar 1 o 2 errores más.", "Escribo: «Lectura 3: máximo 2 errores y repasar las palabras largas»."],
    "Máximo 2 errores en la lectura 3")],
  [("Contar como bien leídas las palabras que cambié.", "Se cuenta cada palabra sin revisar errores.", "Resta los errores antes de dividir por los minutos."),
   ("Ponerse una meta imposible, como cero errores en el primer intento.", "Se quiere lograr todo de una vez.", "Elige una meta pequeña y alcanzable.")],
  ([arith("Lees 120 palabras y tienes 4 errores. ¿Cuántas palabras bien leídas hay?", "120-4", "Se restan los errores."),
    E("En el registro «Lectura 1: 8 errores. Lectura 2: 6 errores.», ¿mejoró la lectura o empeoró?", "Mejoró", "Hubo menos errores en la lectura 2."),
    E("¿Una meta pequeña y alcanzable es «leer perfecto siempre» o «bajar un error la próxima vez»?", "Bajar un error la próxima vez", "Es un paso concreto y posible.")],
   [arith("Lees 90 palabras en 3 minutos, todas bien leídas. ¿Cuántas palabras por minuto lees?", "90//3", "Se divide el total por los minutos."),
    arith("Un lector tuvo 100 palabras y 5 errores en la primera lectura; en la segunda, 100 palabras y 2 errores. ¿Cuántos errores menos tuvo?", "5-2", "Se comparan los errores de ambos intentos."),
    E("Después de leer, revisas tu lectura. ¿Qué aspecto es de precisión: «cambié la palabra desfiladero» o «mi voz sonó fuerte»?", "Cambié la palabra desfiladero", "La precisión es decir las palabras tal como están escritas.")],
   [arith("Lees 280 palabras en 4 minutos con 20 errores. ¿Cuántas palabras bien leídas por minuto?", "(280-20)//4", "Primero se restan los errores y luego se divide."),
    arith("Una lectora hace 2 minutos y 30 segundos. ¿Cuántos segundos tardó en total?", "2*60+30", "Cada minuto tiene 60 segundos."),
    E("En el texto «Los pájaros llegan temprano, cantan fuerte y despiertan al barrio.» ¿cuántas palabras hay?", n_words("Los pájaros llegan temprano, cantan fuerte y despiertan al barrio."), "Se cuenta cada palabra separada por espacios.")],
   [arith("Beto lee 150 palabras en 3 minutos con 6 errores. Carla lee 120 palabras en 2 minutos con 0 errores. ¿Cuántas palabras bien leídas por minuto más tiene Carla?", "120//2-(150-6)//3", "Beto: 144 ÷ 3 = 48. Carla: 120 ÷ 2 = 60. Diferencia: 12."),
    E("Si dos lectores leen igual de rápido pero uno tiene más errores, ¿cuál tiene más palabras bien leídas por minuto?", "El que tiene menos errores", "Los errores se restan del total.")],
   [arith("Una lectora quiere llegar a 70 palabras bien leídas por minuto. Hoy lee 240 palabras en 4 minutos con 20 errores. ¿Cuántas palabras por minuto le faltan?", "70-(240-20)//4", "Hoy lee 220 ÷ 4 = 55; le faltan 15."),
    E("En una meta «no cambiar ninguna palabra de la segunda oración», ¿qué debes revisar: la precisión o el volumen?", "La precisión", "La meta trata de decir las palabras tal como están escritas.")]),
  [arith("En la biblioteca, un voluntario lee un cuento a niños pequeños: 200 palabras en 2 minutos. ¿Cuántas palabras por minuto lee?", "200//2", "Se divide el total por los minutos.")],
  [E("¿Qué se resta del total de palabras para saber cuántas están bien leídas?", "Los errores", "Cada error es una palabra mal dicha."),
   E("Si lees 60 palabras en 1 minuto, ¿cuántas palabras por minuto lees?", "60", "Con un minuto, el total es la velocidad."),
   E("¿Una meta debe ser pequeña y posible o grande e imposible?", "Pequeña y posible", "Así se puede lograr y seguir avanzando.")],
  ("Lee en voz alta este texto de 37 palabras tres veces y completa un registro (veces, errores, autocorrecciones): «Cuando llegó el invierno, las golondrinas del alero se prepararon para el viaje. Volaron en círculos sobre la plaza, se despidieron del campanario y, al amanecer, cruzaron las montañas rumbo al norte, donde el sol las esperaba.» Escribe tu meta para una cuarta lectura.",
   "Lectura 1: 4 errores, 1 autocorrección. Lectura 2: 2 errores, 1 autocorrección. Lectura 3: 1 error, 0 autocorrecciones. Meta: leer «golondrinas» y «campanario» sin errores y respetar las comas de la segunda oración.",
   ["lee tres veces el texto completo", "anota errores y autocorrecciones", "escribe una meta pequeña y precisa"], ["tabla de registro", "lectura en voz alta"], ["meta imposible", "no restar los errores al contar"], "Compara la primera y la última lectura y anota qué palabra mejoró."),
  "Repite el texto de la actividad cada día de la semana y anota cuántos errores tuviste.",
  "Escribe un texto propio de 40 palabras, cuéntalas y léelo en voz alta con un compañero que anote tus errores.")
