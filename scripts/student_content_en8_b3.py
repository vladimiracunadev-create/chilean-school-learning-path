"""Cuaderno del estudiante, 8.º básico Inglés (propuesta): EN08 OA 12, funciones del lenguaje en textos escritos (clases 1 a 3).

Clase 1: tiempo y frecuencia. Clase 2: conectar ideas y expresar cantidades. Clase 3: acciones pasadas que continúan
en el presente y duración. Textos originales y breves, con pista en español. Los títulos de clase del plan son
genéricos; aquí cada clase aplica una función del OA. Los años usados en cálculos se declaran en el enunciado.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA12 = "EN08 OA 12"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ clase 1: tiempo, frecuencia y grado
lesson(
    OA12, 1,
    "Los textos y datos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a pedir y dar información sobre el tiempo, y a señalar frecuencia y grado en mensajes escritos. Sirve para escribir invitaciones, horarios y avisos que se entiendan sin dudas.",
    ["Conozco los días, los meses y la hora en inglés.", "Sé escribir oraciones simples con be y con verbos en presente."],
    [
        "Para preguntar por el tiempo se usa When…? Se responde con tres preposiciones. On va con días: On Saturday. At va con la hora: at 10:00. In va con meses, años y estaciones: in December, in 2027. Con tomorrow, today, next week y last week no se usa preposición: The party is tomorrow. Ejemplo: «When is the party? — On Saturday, at 10:00».",
        "Para hablar de un tiempo anterior a hoy se usa ago, que va después del período: I studied French five years ago. Para decir cada cuánto ocurre algo se usa la frecuencia: always, usually, often, sometimes, never, o expresiones como once a month (una vez al mes), twice a week (dos veces por semana) y three times a year. Los adverbios de frecuencia van antes del verbo principal y después de be: Tomás is always on time.",
        "El grado dice cuánto: quite significa bastante y very significa muy; very es más fuerte que quite: It is quite cold (bastante frío) y It is very cold (muy frío). Ejemplo: She is quite shy. En un texto escrito, estas palabras hacen que un aviso sea claro: «Open day: next Tuesday, at 10:00. Clubs meet twice a week». Al revisar, comprueba que cada dato de tiempo tenga la preposición correcta y que la frecuencia esté en su lugar.",
    ],
    [("When…?", "¿Cuándo…?"), ("on / at / in", "con días / con la hora / con meses y años"), ("ago", "hace (tiempo atrás)"), ("once / twice a week", "una vez / dos veces por semana"), ("always, usually, often, sometimes, never", "siempre, por lo general, a menudo, a veces, nunca"), ("quite", "bastante"), ("very", "muy"), ("next week", "la próxima semana"), ("tomorrow", "mañana (el día siguiente)")],
    [
        ("Elegir la preposición", "Completa: «The concert is ___ Friday ___ 7:30.» Usa on, at o in.", ["Friday es un día: va con on.", "7:30 es una hora: va con at.", "Queda on Friday at 7:30."], "on, at"),
        ("Colocar la frecuencia", "Ordena: always / is / Tomás / on time", ["Tomás es el sujeto y is es be.", "Con be, el adverbio va después.", "Queda Tomás is always on time."], "Tomás is always on time."),
    ],
    [
        ("Escribir «The meeting is in Monday».", "In no se usa con días de la semana.", "Con días se usa on: on Monday."),
        ("Escribir «We visited the museum two weeks after».", "After no expresa hace dos semanas.", "Usa ago: two weeks ago."),
    ],
    [
        ("Completa: «The concert is ___ Friday.» A) on B) in", "A", "Los días de la semana van con on."),
        ("Completa: «The class starts ___ 9:15.» A) at B) on", "A", "Las horas van con at."),
        ("Completa: «My birthday is ___ March.» A) in B) on", "A", "Los meses van con in."),
    ],
    [
        ("Aviso: «The science fair is on Thursday at 4:30. Next week is the prize ceremony.» ¿A qué hora es la feria? Responde con la hora.", "4:30", "El aviso da la hora con at 4:30 después del día."),
        ("«She studied Japanese four years ago.» ¿Qué significa ago? A) hace (tiempo atrás) B) dentro de", "A", "Ago señala un tiempo anterior a hoy."),
        ("«I swim twice a week.» ¿Cuántas veces nado en una semana?", "2", "Twice significa dos veces."),
    ],
    [
        ("Completa la pregunta: «___ is the match? — On Sunday at 11:00.»", "When", "La respuesta da día y hora, así que la pregunta es When."),
        ("Una clase de natación es el lunes y el jueves de cada semana. Completa: «We swim ___ a week.» Opciones: once / twice.", "twice", "Hay dos clases por semana, por lo que se usa twice."),
        ("Completa para decir «bastante estricta, pero también amable»: «Our teacher is ___ strict, but also kind.» Opciones: quite / very.", "quite", "Quite significa bastante; very significa muy, que es más fuerte."),
    ],
    [
        ("¿Qué mensaje está bien escrito? A) The meeting is in Monday at 8:00. B) The meeting is on Monday at 8:00.", "B", "El día de la semana lleva on y la hora lleva at."),
        ("¿Dónde va el adverbio en «Lena ___ walks to school»? Opciones: usually walks / walks usually.", "usually walks", "Con un verbo común, el adverbio de frecuencia va antes del verbo."),
    ],
    [
        ("Afiche: «Open day: next Tuesday, at 10:00. The clubs meet twice a week. The library is closed on Sundays.» ¿Cuántas veces por semana se reúnen los clubes y qué día es la jornada abierta?", "Dos veces; el próximo martes", "El afiche dice twice a week y next Tuesday."),
        ("Corrige: «We visited the museum two weeks after.» Escribe la oración corregida con el significado hace dos semanas.", "We visited the museum two weeks ago.", "Ago se usa después del período para decir hace."),
    ],
    [("Hay que elegir el afiche mejor escrito para un taller. ¿Cuál? A) The workshop is on Saturday at 10:00 and it is open once a month. B) The workshop is in Saturday at 10:00 and it is open one time monthly.", "A", "Usa on con el día, at con la hora y la expresión once a month.")],
    [
        ("¿Qué preposición va con meses y años?", "in", "In December, in 2027."),
        ("¿Cómo se dice «dos veces por semana»?", "twice a week", "Twice significa dos veces."),
        ("¿Qué palabra se escribe después de un período para decir «hace»?", "ago", "Five years ago."),
    ],
    task("Lee este encargo: escribe en una hoja una invitación de cuatro oraciones para una actividad de tu curso, como una feria de libros o un campeonato. Debe responder When is it?, usar on, at e in al menos una vez cada una, incluir una frase con ago o con once a month, y una oración con quite. Revísala con esa lista.", "Book fair: it is on Friday at 3:00. Last year we sold books in June, two years ago in May. The fair is quite big and it takes place once a year. Please come!", ["usa on, at e in correctamente", "tiene una expresión de frecuencia o con ago", "usa quite con un adjetivo"], ["hoja con la invitación y cada recurso subrayado"], ["usar in con un día de la semana", "poner el adverbio de frecuencia lejos del verbo"], "Lee tu invitación a una persona de tu casa y pregunta cuándo es, para ver si el dato quedó claro."),
    "Escribe cinco oraciones sobre tu semana con always, usually, often, sometimes y never.",
    "Escribe un horario semanal de cuatro actividades con día y hora, usando on y at.",
)

# ================================================================ clase 2: conectar ideas y cantidades
lesson(
    OA12, 2,
    "Los textos y datos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a conectar ideas con and then, so, until y also, y a expresar cantidades con thousand, million, enough y no. Sirve para que un texto escrito fluya y para dar cifras con claridad.",
    ["Conozco and, but y because.", "Sé contar hasta cien en inglés."],
    [
        "Los conectores unen ideas. And then indica una secuencia: He came and then we watched the film. So muestra un resultado: It was far, so we took the bus. Until significa hasta: I'll wait until Monday (esperaré hasta el lunes). Also significa además y va antes del verbo principal: The library is the best in town. It also has a quiet room. Una coma suele ir antes de so.",
        "Para las cantidades, los números grandes se dicen two thousand (2,000), four thousand (4,000) y one million (1,000,000). Con un número delante, thousand y million no llevan s: four thousand people. En inglés se escribe una coma entre miles. Enough significa suficiente: We have enough chairs. No significa ninguno o nada: We have no time. We don't have enough money es otra forma de decir que falta dinero.",
        "Al escribir, elige el conector que dice lo que quieres: secuencia, resultado, límite en el tiempo o información adicional. Y revisa las cifras: si el texto dice «50.000 pesos» en español, en inglés queda fifty thousand pesos. Un buen texto conecta las ideas sin repetir siempre and.",
    ],
    [("and then", "y luego (secuencia)"), ("so", "así que (resultado)"), ("until", "hasta"), ("also", "además"), ("thousand", "mil"), ("million", "millón"), ("enough", "suficiente"), ("no money / no time", "nada de dinero / nada de tiempo")],
    [
        ("Elegir el conector de resultado", "Completa: «It was far, ___ we took the bus.» Opciones: so / until.", ["La segunda parte es el resultado de la primera.", "El conector de resultado es so.", "Queda It was far, so we took the bus."], "so"),
        ("Escribir una cifra en palabras", "Una ciudad ficticia tiene 4,000 habitantes. Escribe 4,000 en palabras.", ["4 es four.", "Mil es thousand, sin s.", "Queda four thousand."], "four thousand"),
    ],
    [
        ("Escribir «two thousands people».", "Thousand no lleva s después de un número.", "Escribe two thousand people."),
        ("Usar until para dar un resultado: «It rained until we stayed home».", "Until significa hasta, no así que.", "Usa so: It rained, so we stayed home."),
    ],
    [
        ("Completa: «I'll wait ___ Monday.» A) until B) also", "A", "Until significa hasta."),
        ("¿Cómo se escribe 3,000 en palabras? A) three thousand B) three thousands", "A", "Thousand no lleva s después de un número."),
        ("«We have enough chairs.» ¿Qué significa enough? A) suficientes B) ninguna", "A", "Enough indica que la cantidad alcanza."),
    ],
    [
        ("«He came and then we watched the film.» ¿Qué ocurrió primero?", "He came", "And then marca que lo segundo ocurrió después."),
        ("«The library is the best in town. It also has a free computer room.» ¿Qué hace also? A) Agrega otra información B) Da un resultado", "A", "Also significa además y suma un dato."),
        ("¿Cómo se escribe 1,000,000 en palabras?", "one million", "Un millón se escribe one million."),
    ],
    [
        ("Une las oraciones con so: «It was raining. We stayed at home.»", "It was raining, so we stayed at home.", "Lo segundo es el resultado de lo primero."),
        ("El banco cerró a las 5:00 y ahora son las 6:30. Completa: «We have ___ time to go today.» Opciones: no / enough.", "no", "El banco ya cerró, así que no queda tiempo para ir."),
        ("Una ciudad ficticia tiene 2,000,000 de habitantes. Escribe la cifra en palabras.", "two million", "Million no lleva s después de un número."),
    ],
    [
        ("¿Qué oración es correcta? A) The town has two thousands people. B) The town has two thousand people.", "B", "Thousand no lleva s detrás de un número."),
        ("¿Qué oración es lógica? A) We didn't have enough money, so we didn't buy the ticket. B) We didn't have enough money, until we bought the ticket.", "A", "La falta de dinero explica el resultado; until no encaja."),
    ],
    [
        ("Completa con so, until o then: «The bus was late, ___ we walked. We waited ___ 8:00 and ___ we left.»", "so, until, then", "So da el resultado, until marca el límite y then marca la secuencia."),
        ("Reescribe con no, sin cambiar el sentido: «We don't have money.»", "We have no money.", "No más el sustantivo reemplaza don't have."),
    ],
    [("El curso reunió $50.000 y el viaje cuesta $60.000. ¿Qué oración es correcta? A) We don't have enough money for the trip. B) We have enough money for the trip.", "A", "Con $50.000 no alcanza para un viaje de $60.000.")],
    [
        ("¿Qué conector significa «hasta»?", "until", "I'll wait until Monday."),
        ("¿Qué palabra significa «suficiente»?", "enough", "Enough chairs significa sillas suficientes."),
        ("¿Cómo se escribe 5,000 en palabras?", "five thousand", "Thousand no lleva s."),
    ],
    task("Lee este encargo: escribe en una hoja un aviso de cuatro a cinco oraciones sobre una colecta de tu curso. Usa y subraya and then, so, until, also, además una cantidad con thousand y una oración con enough o no. Datos: el curso necesita 60.000 pesos y ya juntó 40.000.", "We need sixty thousand pesos for our trip. First we sold cakes, and then we sold drinks. We have forty thousand pesos, so we don't have enough money yet. We will sell cakes until Friday. We also need more helpers.", ["usa tres conectores distintos con su sentido correcto", "escribe la cantidad con thousand sin s", "usa enough o no con sentido"], ["hoja con el aviso y los conectores subrayados"], ["agregar s a thousand", "usar until como si fuera así que"], "Lee tu aviso a una persona de tu casa y pregunta cuánto dinero falta, para comprobar que las cifras se entienden."),
    "Escribe tres oraciones con so a partir de tres pares de ideas sobre tu día.",
    "Escribe un párrafo de cinco oraciones sobre un fin de semana sin repetir and más de una vez.",
)

# ================================================================ clase 3: acciones que continúan y duración
lesson(
    OA12, 3,
    "Los textos y datos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir sobre acciones pasadas que continúan hoy, con have/has + participio, y a decir cuánto dura algo con for y since. Sirve para contar cuánto tiempo llevas haciendo algo.",
    ["Conozco el pasado simple, como studied y saved.", "Sé usar have y has con I, you, he y she."],
    [
        "El presente perfecto se forma con have o has + participio pasado: I have saved money to buy a bike. He has worked here since 2015. Se usa para una acción que empezó en el pasado y continúa o importa hoy. Has va con he, she e it; have con I, you, we y they. Los participios regulares terminan en -ed (saved, worked) y otros son irregulares: been, had, made, done, seen, known, written.",
        "Para decir cuánto dura algo se usa How long…? Se responde con for + período (for two years) o con since + punto de inicio (since 2016, since Monday). Compara: I studied French five years ago es un hecho terminado en el pasado y usa pasado simple con ago; I have studied French for five years muestra que continúo estudiando.",
        "Al escribir, pregúntate: ¿la acción terminó o continúa? Si terminó y hay una fecha o ago, usa pasado simple. Si continúa y hay for o since, usa presente perfecto. Para calcular un período con since, resta el año de inicio al año actual: si el año actual es 2030 y empezó en 2018, son 12 años.",
    ],
    [("have / has + participio", "presente perfecto"), ("participle", "participio: been, made, saved, worked"), ("How long…?", "¿Cuánto tiempo…?"), ("for", "durante (un período: for two years)"), ("since", "desde (un punto de inicio: since 2016)"), ("save money", "ahorrar dinero"), ("worked", "trabajó / ha trabajado"), ("been", "participio de be: sido o estado")],
    [
        ("Elegir for o since", "Completa con for o since: «I have known him ___ 2019» y «I have known him ___ five years».", ["2019 es un punto de inicio: since.", "Five years es un período: for.", "Queda since 2019 y for five years."], "since, for"),
        ("Formar el presente perfecto", "Completa: «She ___ lived here for two years.» Opciones: has / have.", ["She es tercera persona.", "Con she se usa has.", "Queda She has lived here."], "has"),
    ],
    [
        ("Escribir «I have studied French five years ago».", "Ago no se combina con el presente perfecto.", "Usa pasado simple: I studied French five years ago."),
        ("Usar for con un año de inicio: «for 2016».", "Un año de inicio pide since.", "Escribe since 2016."),
    ],
    [
        ("Completa: «She ___ lived here for two years.» A) has B) have", "A", "Con she se usa has."),
        ("Completa: «I have known him ___ 2019.» A) since B) for", "A", "2019 es un punto de inicio."),
        ("¿Cuál es el participio de make? A) made B) maked", "A", "Make es irregular: make, made, made."),
    ],
    [
        ("«I lived in Temuco for three years» (ya no vivo allí) y «I have lived in Temuco for three years» (sigo viviendo allí). ¿Cuál de las dos oraciones dice que la acción continúa hoy? Escribe la que continúa.", "I have lived in Temuco for three years.", "El presente perfecto muestra una acción que sigue vigente."),
        ("Completa: «How long have you been friends? — We have been friends ___ two years.» Opciones: for / since.", "for", "Two years es un período de duración."),
        ("«He has worked here since 2015.» ¿Desde cuándo trabaja allí?", "2015", "Since indica el punto de inicio."),
    ],
    [
        arith("Suponte que el año actual es 2030. Ana ha vivido en su casa desde 2018. ¿Cuántos años lleva viviendo ahí?", "2030 - 2018", "Se resta el año de inicio al año actual."),
        ("Completa: «I ___ saved money to buy a bike.» Opciones: have / has.", "have", "Con I se usa have."),
        ("Ordena: has / since / worked / Leo / 2020 / here", "Leo has worked here since 2020.", "La estructura es sujeto, has, participio, lugar y since más el año."),
    ],
    [
        ("¿Qué oración es correcta? A) I have studied French five years ago. B) I studied French five years ago.", "B", "Con ago se usa pasado simple."),
        ("Completa: «How long ___ you been in this school?» Opciones: have / did.", "have", "How long con una situación que continúa lleva el presente perfecto."),
    ],
    [
        ("Completa con for o since: «She has had the bike ___ six months. She has had it ___ last June.»", "for, since", "Six months es un período y last June es un punto de inicio."),
        ("Completa la pregunta: «___ have you been in the choir? — For two years.»", "How long", "La respuesta da una duración."),
    ],
    [("Nico ahorra para una bicicleta desde hace diez semanas y todavía sigue ahorrando. ¿Qué pregunta calza con «for ten weeks»? A) How long has Nico saved money? B) When did Nico save money?", "A", "For ten weeks responde a una pregunta de duración con How long.")],
    [
        ("¿Qué palabra se usa con un período, como five years?", "for", "For two years, for five years."),
        ("¿Qué palabra se usa con un inicio, como 2016?", "since", "Since 2016, since Monday."),
        ("¿Qué auxiliar va con she en el presente perfecto?", "has", "She has saved."),
    ],
    task("Lee este encargo: escribe en una hoja cinco oraciones sobre ti con el presente perfecto. Usa for en dos, since en dos, y una pregunta con How long y su respuesta. Puedes hablar de tu curso, un hobby o un deporte. Revisa que cada oración tenga have o has y un participio.", "I have played the guitar for two years. My brother has played football since 2022. We have been in this class since March. I have studied English for five years. How long have you lived here? — I have lived here for ten years.", ["usa have o has con participio", "usa for con períodos y since con inicios", "incluye una pregunta con How long y su respuesta"], ["hoja con las cinco oraciones y for o since subrayados"], ["usar since con un período", "usar ago con el presente perfecto"], "Lee tus oraciones a una persona de tu casa y pregunta si los períodos son verdaderos."),
    "Escribe tres preguntas con How long y sus respuestas con for.",
    "Escribe tres oraciones con since y calcula cuántos años son suponiendo que el año actual es 2030.",
)
