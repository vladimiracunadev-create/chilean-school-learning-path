"""Student material for 3.º básico Música, OA 07 (experiencias musicales y sonoras en la vida y la sociedad) y OA 08 (reflexión sobre escucha, interpretación y creación)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA7, OA8 = "MU03 OA 07", "MU03 OA 08"


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 07 · clase 1
MAPA = [
    ("al despertar", "suena una alarma de reloj", "sonido cotidiano"),
    ("al despertar", "una radio toca música suave", "música"),
    ("camino al colegio", "una bocina de auto", "sonido cotidiano"),
    ("camino al colegio", "pájaros que cantan", "sonido cotidiano"),
    ("recreo", "niños cantan un juego con palmas", "música"),
    ("recreo", "suena la campana", "sonido cotidiano"),
    ("tarde", "una persona de la casa canta mientras ordena", "música"),
    ("noche", "se escucha música suave antes de dormir", "música"),
]
MAPA_TXT = " ".join(f"{i}) {m}: {d} ({t})." for i, (m, d, t) in enumerate(MAPA, 1))
N_MUS = sum(1 for *_x, t in MAPA if t == "música")
N_SON = len(MAPA) - N_MUS

L(
    OA7, 1,
    f"Lápiz y papel. Mapa sonoro de ejemplo de un niño imaginado en un día: {MAPA_TXT} Puedes hacer luego tu propio mapa con lo que oyes en tu día.",
    "Aprenderé a mapear los sonidos y músicas de situaciones cotidianas. Sirve para darme cuenta de cuánta música y sonido hay en mi vida.",
    ["Sé nombrar cualidades del sonido.", "Sé escuchar con atención.", "Sé que hay músicas en distintas situaciones."],
    [
        "Un mapa sonoro es una lista de los sonidos y músicas que aparecen en las situaciones de un día. Para hacerlo, anotas el momento, lo que suena y si es música o un sonido cotidiano. La música tiene sonidos organizados con intención, con pulso o melodía. Un sonido cotidiano, como una bocina, no está organizado así.",
        f"Mira el mapa de ejemplo: {MAPA_TXT} Hay {len(MAPA)} registros: {N_MUS} son música y {N_SON} son sonidos cotidianos. Cada uno tiene una función: la alarma avisa, la campana ordena el recreo, la música suave acompaña o calma.",
        "Al hacer tu mapa, anota solo lo que realmente escuchaste. No hace falta que sea parecido al de otras personas: cada día y cada casa suenan distinto. Puedes añadir una cualidad del sonido, como fuerte o suave, o largo o corto. Y si no escuchas música en algún momento, déjalo vacío; no pasa nada.",
    ],
    [("mapa sonoro", "lista de sonidos y músicas de un día"), ("cotidiano", "que ocurre en la vida diaria"), ("música", "sonidos organizados con intención musical"), ("sonido cotidiano", "sonido del ambiente que no es música"), ("situación", "momento del día en que ocurre algo")],
    [
        ("Contar músicas", f"{MAPA_TXT} ¿Cuántos registros son música?", ["Busco los que dicen «(música)».", "Son los registros 2, 5, 7 y 8."], f"{N_MUS} registros"),
        ("Clasificar un sonido", "Una bocina de auto suena en la calle. ¿Es música o sonido cotidiano?", ["No tiene pulso ni melodía organizados.", "Es un sonido del ambiente."], "Sonido cotidiano"),
    ],
    [
        ("Anotar sonidos que no escuchaste para que el mapa se vea completo.", "El mapa debe ser de lo que realmente oíste.", "Deja vacío lo que no escuchaste."),
        ("Pensar que mi mapa debe ser igual al de los demás.", "Cada persona vive sonidos distintos.", "Anota tu propia experiencia."),
    ],
    [
        ex(f"{MAPA_TXT} ¿Qué suena camino al colegio en el registro 4?", "Pájaros que cantan", "El registro 4 dice «pájaros que cantan»."),
        ex(f"{MAPA_TXT} ¿El registro 6 es música o sonido cotidiano?", "Sonido cotidiano", "La campana no es música organizada."),
        ex("¿Qué es un mapa sonoro?", "Una lista de sonidos y músicas de un día", "Anota qué suena en cada situación."),
    ],
    [
        ex(f"{MAPA_TXT} ¿Cuántos registros hay en total?", str(len(MAPA)), "Se numeran del 1 al 8."),
        ex(f"{MAPA_TXT} ¿Cuántos son sonidos cotidianos?", str(N_SON), "Son el 1, el 3, el 4 y el 6."),
        ex(f"{MAPA_TXT} ¿En qué momento suena música suave antes de dormir?", "Por la noche", "El registro 8 dice «noche»."),
    ],
    [
        arith(f"En el mapa hay {N_MUS} músicas y {N_SON} sonidos cotidianos. Si agregas 3 músicas más, ¿cuántas músicas habrá?", f"{N_MUS}+3", "Se suman las nuevas a las que ya había.", " músicas"),
        ex(f"{MAPA_TXT} ¿En qué situación del día (momento) hay más registros: recreo o camino al colegio?", "Hay los mismos", "Cada momento tiene 2 registros."),
        ex("Una niña dice que su mapa tiene solo 2 músicas y el de otro tiene 6. ¿Alguno está mal?", "Ninguno", "Cada persona vive días distintos."),
    ],
    [
        ex("Un niño dice «no hay música en mi día». Escucha con atención y descubre que su casa tiene una radio con música suave a la hora de comer. ¿Cambia su mapa?", "Sí, agrega la música de la radio", "El mapa debe reflejar lo que escuchó."),
        ex("La alarma, la bocina y la campana tienen una función: avisar. ¿Cuál es la función de la música suave antes de dormir?", "Calmar o acompañar", "No avisa, sino que ayuda a descansar."),
    ],
    [
        arith("En una semana anotas 3 músicas cada día, de lunes a viernes. ¿Cuántas músicas anotas?", "3*5", "Son 3 músicas por día durante 5 días.", " músicas"),
        ex("Quieres comparar dos mapas de la misma semana: uno tiene 8 registros y otro 5. ¿Cuántos registros más tiene el primero?", "3", "8 menos 5."),
    ],
    [ex("Una familia imaginaria escucha música en el auto de camino a la escuela y su hijo anota lo que oye cada mañana. ¿Cómo se llama esa lista?", "Mapa sonoro", "Es una lista de sonidos y músicas de un día.")],
    [ex("¿Qué es música?", "Sonidos organizados con intención musical", "Tienen pulso o melodía."), ex("¿Una alarma es música?", "No", "Es un sonido cotidiano."), ex("¿Debes anotar lo que no oíste?", "No", "El mapa es de lo que escuchaste.")],
    (
        "Haz tu mapa sonoro de un día con al menos cinco registros. Para cada uno escribe el momento, lo que suena y si es música o sonido cotidiano. Añade una cualidad del sonido en dos de ellos (por ejemplo, fuerte o suave). Si en alguna situación no escuchas música, déjalo vacío. No escribas nombres de personas ni datos privados.",
        "1) al despertar: alarma, sonido cotidiano, fuerte. 2) recreo: juego con palmas, música. 3) tarde: radio suave, música, suave. 4) noche: grillos, sonido cotidiano. 5) camino: pájaros, sonido cotidiano.",
        ["anota cinco registros", "clasifica música y sonido cotidiano", "añade cualidades sin datos privados"],
        ["tabla escrita"],
        ["anotar sonidos que no escuchó", "mezclar música con sonido cotidiano"],
        "Reconoce el mapa propio y pregunta cómo supo que algo era música o sonido; no compara mapas.",
    ),
    "Escucha en silencio un minuto y anota tres sonidos que oigas.",
    "Haz un mapa sonoro de tu casa en un momento del día con cuatro registros.",
)

# ---------------------------------------------------------------- OA 07 · clase 2
CEL = [
    ("un cumpleaños", "se canta una canción para quien cumple años", "celebrar y compartir"),
    ("las Fiestas Patrias", "se baila cueca, el baile nacional de Chile", "bailar y celebrar juntos"),
    ("una fiesta de fin de año del curso", "se canta y se toca música en grupo", "despedirse y compartir"),
    ("un acto escolar", "el curso canta una canción", "mostrar el trabajo"),
    ("una reunión de amigos", "se escucha música de fondo mientras conversan", "acompañar la conversación"),
]
CEL_TXT = " ".join(f"{i}) {c}: {d}; función: {f}." for i, (c, d, f) in enumerate(CEL, 1))

L(
    OA7, 2,
    f"Lápiz y papel. Celebraciones de ejemplo: {CEL_TXT} No todas las familias celebran lo mismo: lo importante es describir lo que tú vives o lo que otros cuentan.",
    "Aprenderé a relacionar la música con celebraciones, reuniones y festividades. Sirve para entender para qué se usa la música cuando nos reunimos.",
    ["Sé qué es un mapa sonoro.", "Sé que la música tiene funciones.", "Sé describir una situación."],
    [
        f"Una celebración es un momento especial para reunirse. Puede ser un cumpleaños, una fiesta de curso o una festividad del país. En muchas celebraciones hay música: se canta, se baila o se toca. También hay reuniones, como juntarse con amigos o con el curso, donde la música puede acompañar. Ejemplos: {CEL_TXT}",
        "La música cumple una función en la celebración. Puede servir para bailar, para cantar juntos, para marcar el inicio o para recordar. Por ejemplo, la cueca es el baile nacional de Chile y se baila en las Fiestas Patrias de septiembre. Pero no todas las personas la bailan, ni todas las familias celebran de la misma manera.",
        "Para describir una celebración, responde: ¿qué se celebra?, ¿qué música suena?, ¿qué hacen las personas con esa música? y ¿cuál es su función? No des por hecho que todos celebran igual: di «en esta celebración» o «en mi experiencia». Si la celebración pertenece a una comunidad, respeta cómo ella la vive.",
    ],
    [("celebración", "momento especial para reunirse"), ("festividad", "celebración que se repite cada año"), ("función", "para qué sirve la música en esa situación"), ("cueca", "baile nacional de Chile"), ("reunión", "encuentro de personas")],
    [
        ("Hallar la función", f"{CEL_TXT} ¿Cuál es la función de la música en el acto escolar (registro 4)?", ["Busco el registro 4.", "Dice «mostrar el trabajo»."], "Mostrar el trabajo"),
        ("Contar celebraciones", f"{CEL_TXT} ¿En cuántas celebraciones se canta?", ["Busco la palabra «canta» en las descripciones.", "Aparece en los registros 1, 3 y 4."], "3 celebraciones"),
    ],
    [
        ("Decir que todas las personas celebran igual.", "Cada familia y cada comunidad celebra a su manera.", "Usa «en mi experiencia» o «en esta celebración»."),
        ("Pensar que la música solo sirve para bailar.", "Cumple muchas funciones.", "Pregunta qué hace la gente con esa música."),
    ],
    [
        ex(f"{CEL_TXT} ¿Qué baile se menciona en las Fiestas Patrias?", "La cueca", "El registro 2 la nombra."),
        ex("¿La cueca es el baile nacional de Chile?", "Sí", "Así se reconoce en el país."),
        ex(f"{CEL_TXT} ¿Cuántas situaciones hay en la lista?", str(len(CEL)), "Hay cinco registros."),
    ],
    [
        ex(f"{CEL_TXT} ¿En qué celebración la función es despedirse y compartir?", "La fiesta de fin de año del curso", "Es el registro 3."),
        ex(f"{CEL_TXT} ¿En qué celebración se baila?", "Las Fiestas Patrias", "El registro 2 dice que se baila cueca."),
        ex("Una música sirve para que todo un curso cante junto. ¿Cuál es su función: (a) avisar, (b) compartir y celebrar juntos?", "(b)", "Cantar juntos une al grupo."),
    ],
    [
        ex(f"{CEL_TXT} ¿En cuántas celebraciones la función incluye compartir?", "2", "Los registros 1 y 3 dicen «compartir»."),
        arith("Una fiesta de curso tiene 6 canciones de 3 minutos cada una. ¿Cuántos minutos de música hay?", "6*3", "Son 6 canciones de 3 minutos.", " minutos"),
        ex("Una niña dice «en mi casa no celebramos las Fiestas Patrias con baile». ¿Está equivocada?", "No", "Cada familia celebra a su manera."),
    ],
    [
        ex("Ana dice «en todas las fiestas se baila cueca». ¿Qué problema tiene esa frase?", "Generaliza: no todas las fiestas ni todas las personas", "Dice «todas» sin evidencia."),
        ex("Reescribe «todos bailan cueca» sin generalizar: (a) «En las Fiestas Patrias que yo viví se bailó cueca.» (b) «Nadie baila cueca.»", "(a)", "La (a) habla de una experiencia concreta."),
    ],
    [
        arith("En un acto hay 5 presentaciones de 4 minutos cada una y 1 minuto de transición entre cada par. Hay 4 transiciones. ¿Cuántos minutos dura?", "5*4+4*1", "Son 20 minutos de música y 4 de transición.", " minutos"),
        ex("Una escuela quiere una música para que sus estudiantes bailen en una fiesta. ¿Qué función busca: bailar o avisar?", "Bailar", "Una música para bailar tiene la función de hacer bailar."),
    ],
    [ex("En un acto del colegio, un curso canta para recordar el comienzo del año. ¿Cuál es la función de la música?", "Recordar y compartir", "Marca un momento y une al grupo.")],
    [ex("¿Qué función puede tener la música en una fiesta?", "Bailar, cantar juntos o celebrar", "Son funciones distintas."), ex("¿Dónde se baila la cueca según la clase?", "En las Fiestas Patrias", "Es una de sus ocasiones."), ex("¿Debes pensar que todos celebran igual?", "No", "Cada persona y comunidad celebra a su manera.")],
    (
        "Elige una celebración que tú conozcas o una de la lista (cumpleaños, Fiestas Patrias, fiesta del curso o acto escolar). Escribe: qué se celebra, qué música suena, qué hacen las personas con ella y cuál es su función. Usa «en mi experiencia» o «en esta celebración» y no escribas nombres de personas ni datos privados.",
        "Fiesta del curso. Música: canciones cantadas en grupo. Las personas cantan y aplauden. Función: compartir y despedir el año. En esta celebración, todos cantaron juntos.",
        ["responde las cuatro preguntas", "nombra la función", "usa un lenguaje que no generaliza"],
        ["escrito breve"],
        ["escribir «todos» sin evidencia", "olvidar la función"],
        "Reconoce la descripción concreta y pide cambiar «todos» por «en esta celebración» si aparece.",
    ),
    "Pregunta a una persona de tu casa qué música le gusta para celebrar y por qué.",
    "Compara dos celebraciones y escribe en qué se parece la música y en qué se diferencia.",
)

# ---------------------------------------------------------------- OA 07 · clase 3
FUN = [
    ("una canción para dormir a un bebé", "calmar"),
    ("un baile en una fiesta", "bailar"),
    ("una marcha en un desfile del colegio", "marchar al mismo paso"),
    ("una canción cantada mientras se ordena la casa", "acompañar el trabajo"),
    ("la campana del recreo", "avisar"),
]
FUN_TXT = " ".join(f"{i}) {s}: función {f}." for i, (s, f) in enumerate(FUN, 1))

L(
    OA7, 3,
    f"Lápiz y papel. Situaciones con su función: {FUN_TXT}",
    "Aprenderé a comparar funciones sociales de la música: para qué sirve en distintas situaciones. Sirve para entender por qué la música cambia según el momento.",
    ["Sé qué es una celebración.", "Sé qué es una función.", "Sé nombrar cualidades del sonido."],
    [
        "La música cumple funciones en la sociedad. Algunas son calmar, bailar, marchar, acompañar el trabajo, avisar, celebrar o recordar. La función explica por qué la música suena de cierta manera. Una canción para dormir suele ser lenta y suave. Una música para bailar suele tener un pulso claro y marcado.",
        f"Veamos ejemplos: {FUN_TXT} Son {len(FUN)} situaciones con {len(set(f for _s, f in FUN))} funciones distintas. Comparamos funciones mirando dos cosas: para qué sirve y qué cualidades del sonido tiene. Así vemos que función y sonido se relacionan.",
        "Al comparar, usamos criterios y no decimos que una función vale más que otra. Una canción para dormir no es «mejor» que una música para bailar: sirven para cosas distintas. Si una persona usa la música de otra manera, es su experiencia, y la respetamos.",
    ],
    [("función social", "para qué se usa la música en una situación"), ("calmar", "ayudar a quedar tranquilo"), ("marchar", "caminar al mismo paso"), ("acompañar", "estar junto a una actividad"), ("avisar", "dar una señal")],
    [
        ("Hallar la función", f"{FUN_TXT} ¿Cuál es la función de la marcha del desfile?", ["Busco el registro 3.", "Dice «marchar al mismo paso»."], "Marchar al mismo paso"),
        ("Relacionar función y sonido", "Una canción tiene función de calmar. ¿Será más probable que sea lenta y suave o rápida y fuerte?", ["Calmar pide tranquilidad.", "Lo lento y suave tranquiliza."], "Lenta y suave"),
    ],
    [
        ("Decir que la música para bailar es mejor que la de dormir.", "Sirven para cosas distintas.", "Compara para qué sirve cada una."),
        ("Creer que una música tiene una sola función para siempre.", "La misma música puede servir para cosas distintas según la persona.", "Pregunta para qué se usa en esa situación."),
    ],
    [
        ex(f"{FUN_TXT} ¿Qué función tiene la campana del recreo?", "Avisar", "El registro 5 dice avisar."),
        ex(f"{FUN_TXT} ¿Qué función tiene la canción para dormir?", "Calmar", "El registro 1 dice calmar."),
        ex("¿Una marcha ayuda a caminar al mismo paso?", "Sí", "Su pulso parejo ayuda a marchar."),
    ],
    [
        ex(f"{FUN_TXT} ¿Cuántas funciones distintas hay en la lista?", str(len(set(f for _s, f in FUN))), "Cada situación tiene una función diferente."),
        ex(f"{FUN_TXT} ¿En qué situación se usa la música para acompañar el trabajo?", "Cantar mientras se ordena la casa", "El registro 4 lo dice."),
        ex("Una música para bailar, ¿suele tener un pulso claro o ninguno?", "Un pulso claro", "El pulso marcado ayuda a bailar."),
    ],
    [
        ex("Compara la canción para dormir (función calmar) con la música de baile (función bailar). ¿Qué cualidad del tempo es más probable en cada una?", "Lento para dormir y más rápido para bailar", "Calmar pide lentitud y bailar pide energía."),
        arith("Una canción para dormir dura 3 minutos y se canta 4 veces. ¿Cuántos minutos se canta?", "3*4", "Son 4 veces de 3 minutos.", " minutos"),
        ex("Un desfile marcha al ritmo de 1 paso por pulso. Si la música tiene 16 pulsos, ¿cuántos pasos dan?", "16", "Es un paso por cada pulso."),
    ],
    [
        ex("Luis dice «la música de los desfiles es mejor que la de dormir». ¿Qué respuesta compara sin jerarquizar?", "Sirven para cosas distintas: una marcha y otra calma", "Compara funciones, no valor."),
        ex("Una persona pone música suave mientras estudia. ¿Cuál función de la lista se parece más: marchar o acompañar el trabajo?", "Acompañar el trabajo", "Acompaña lo que hace, como cantar mientras se ordena la casa."),
    ],
    [
        arith("En un día hay 3 canciones para acompañar el trabajo, 2 para bailar y 1 para calmar. ¿Cuántas canciones hay?", "3+2+1", "Se suman las canciones de cada función.", " canciones"),
        ex("En un día hay 3 canciones para acompañar el trabajo, 2 para bailar y 1 para calmar. ¿Cuál función tiene más canciones?", "Acompañar el trabajo", "Tiene 3, más que las otras."),
    ],
    [ex("Un curso arma un desfile para un acto. Necesita música para marchar. ¿Qué cualidad del sonido le conviene?", "Un pulso parejo", "El pulso parejo ayuda a marchar al mismo paso.")],
    [ex("¿Qué es una función social de la música?", "Para qué se usa en una situación", "Cambia según el momento."), ex("¿Qué función tiene una alarma?", "Avisar", "Da una señal."), ex("¿Una función vale más que otra?", "No", "Sirven para cosas distintas.")],
    (
        "Elige dos situaciones donde hay música o sonido (por ejemplo, una canción para calmar y una música para bailar, o dos de la lista). Compara: ¿cuál es la función de cada una?, ¿qué cualidades del sonido crees que tiene cada una (lenta o rápida, suave o fuerte)? y ¿en qué se parecen y en qué se diferencian? No digas cuál es mejor.",
        "Canción para dormir: calmar, lenta y suave. Música de baile: bailar, rápida y con pulso marcado. Se parecen en que tienen pulso, y se diferencian en el tempo y la intensidad.",
        ["nombra la función de cada una", "relaciona función y sonido", "compara sin jerarquizar"],
        ["escrito breve"],
        ["decir cuál es mejor", "no relacionar función y sonido"],
        "Reconoce la relación entre función y sonido y quita cualquier frase con «mejor» o «peor».",
    ),
    "Piensa en una música que escuchas en tu casa y di para qué sirve.",
    "Escribe una tabla de tres situaciones con su función y una cualidad del sonido.",
)

# ---------------------------------------------------------------- OA 07 · clase 4
EXP = [
    "Esta semana, en mi casa, escuchamos música suave a la hora de comer.",
    "Todos los chilenos bailan cueca en septiembre.",
    "En el recreo de ayer, mi curso cantó un juego con palmas.",
    "Nadie escucha música clásica.",
    "En mi experiencia, la música alegre me hace querer moverme.",
]
EXP_TXT = " ".join(f"{i}) {e}" for i, e in enumerate(EXP, 1))
GEN = [2, 4]

L(
    OA7, 4,
    f"Lápiz y papel. Frases de ejemplo: {EXP_TXT} Regla: una buena documentación cuenta lo que pasó o lo que uno vive, y no dice que todas las personas hacen lo mismo. No escribas nombres de personas ni datos privados.",
    "Aprenderé a documentar una experiencia musical sin generalizar. Sirve para contar lo que viví con precisión y respetar lo que viven otros.",
    ["Sé hacer un mapa sonoro.", "Sé qué es una función de la música.", "Sé cuidar los datos privados."],
    [
        "Documentar una experiencia es escribirla para que otros la entiendan. Una ficha incluye: qué pasó, cuándo y dónde (sin direcciones exactas), qué música o sonido hubo, con qué cualidades y cuál fue su función. No se escriben nombres ni datos privados: se dice «una persona de mi casa» o «mi curso».",
        f"Generalizar es decir que todas las personas hacen o sienten lo mismo. Por ejemplo, {EXP[1]} es una generalización, porque no todas las personas bailan cueca. En cambio {EXP[2]} es una experiencia concreta. Frases como «todos», «nadie» o «siempre» suelen ser generalizaciones.",
        "Para evitar generalizar usa: «en mi experiencia», «esta vez», «en mi casa» o «algunas personas». Así cuentas lo que sabes sin hablar por los demás. También puedes decir lo que no sabes: «no sé qué música escuchan otros». Documentar bien es una forma de respeto.",
    ],
    [("documentar", "registrar una experiencia con datos"), ("generalizar", "decir que todos hacen lo mismo"), ("experiencia concreta", "algo que pasó o vives tú"), ("datos privados", "información que identifica a una persona"), ("ficha", "hoja con los datos de una experiencia")],
    [
        ("Detectar una generalización", f"{EXP_TXT} ¿Cuáles frases generalizan?", ["Busco palabras como «todos» y «nadie».", "La 2 dice «Todos los chilenos…».", "La 4 dice «Nadie…»."], "La 2 y la 4"),
        ("Reescribir sin generalizar", "Reescribe «Todos bailan en las fiestas» para que cuente una experiencia concreta.", ["Cambio «todos» por «en la fiesta que viví».", "Digo qué ocurrió."], "«En la fiesta que viví, la gente bailó»"),
    ],
    [
        ("Escribir nombres de personas en la ficha.", "Son datos privados.", "Escribe «una persona de mi casa»."),
        ("Usar «todos» para afirmar algo que solo viste una vez.", "Generaliza.", "Usa «esta vez» o «en mi experiencia»."),
    ],
    [
        ex(f"{EXP_TXT} ¿La frase 3 es una experiencia concreta o una generalización?", "Experiencia concreta", "Cuenta lo que pasó en un recreo."),
        ex("¿«Nadie escucha música clásica» generaliza?", "Sí", "Dice «nadie» sin evidencia."),
        ex("¿Qué escribes en vez de un nombre de persona?", "Una persona de mi casa", "Así no se dan datos privados."),
    ],
    [
        ex(f"{EXP_TXT} ¿Cuántas frases son generalizaciones?", str(len(GEN)), "Son la 2 y la 4."),
        ex(f"{EXP_TXT} ¿Cuántas frases son experiencias concretas o personales?", str(len(EXP) - len(GEN)), "Son la 1, la 3 y la 5."),
        ex("Escoge una frase que no generaliza: (a) «Todos aman el jazz.» (b) «En mi experiencia, el jazz suena a veces con mucha improvisación.»", "(b)", "La (b) habla de la propia experiencia."),
    ],
    [
        ex("¿Cuáles palabras suelen señalar una generalización: «todos», «nadie» o «en mi casa»?", "Todos y nadie", "«En mi casa» es una experiencia concreta."),
        arith("Una ficha tiene 6 frases. Hay 2 con «todos» y 1 con «nadie». ¿Cuántas frases no tienen esas palabras?", "6-2-1", "A las 6 frases se les quitan las 3 que tienen «todos» o «nadie».", " frases"),
        ex("Una niña escribe «mi tío Carlos canta en las fiestas». ¿Qué dato privado debe quitar?", "El nombre", "Los nombres son datos privados."),
    ],
    [
        ex("Pedro escribió «Siempre escucho música en el auto», pero solo lo hizo dos veces. ¿Cómo lo corrige: (a) «Dos veces escuché música en el auto.» (b) «Todos escuchan música en el auto.»?", "(a)", "Describe lo que realmente pasó."),
        ex("Una persona dice «las personas de otra región no escuchan lo mismo que yo». ¿Qué le falta?", "Evidencia o decir que no sabe", "No puede afirmarlo sin saber."),
    ],
    [
        arith("Una ficha tiene 9 frases y 4 generalizan. ¿Cuántas frases no generalizan?", "9-4", "A las 9 frases se les quitan las 4 que generalizan.", " frases"),
        ex("Escribe una forma de empezar una frase para no generalizar: (a) «En mi experiencia…» (b) «Todo el mundo…»", "(a)", "La (a) habla desde lo propio."),
    ],
    [ex("Un estudiante cuenta a su curso una experiencia musical de su casa, sin dar nombres. ¿Cuál frase generaliza: (a) «Esta vez cantamos en la cocina.» (b) «Todas las familias cantan en la cocina.»?", "(b)", "Dice «todas» sin saberlo; la (a) cuenta lo propio.")],
    [ex("En Música: ¿Qué es generalizar?", "Decir que todos hacen lo mismo", "No se puede saber."), ex("¿Qué palabras ayudan a no generalizar?", "En mi experiencia, esta vez", "Hablan de lo propio."), ex("¿Se escriben nombres en la ficha?", "No", "Son datos privados.")],
    (
        "Escribe una ficha de una experiencia musical o sonora que hayas vivido (puede ser un recreo, un viaje o una escucha en casa). Incluye: qué pasó, cuándo (sin fecha exacta si no quieres), qué música o sonido hubo, dos cualidades del sonido y su función. Usa «en mi experiencia» o «esta vez». No escribas nombres ni direcciones. Revisa que no haya «todos», «nadie» ni «siempre».",
        "Esta vez, en el recreo, mi curso cantó un juego con palmas. Hubo una canción rápida y fuerte. Su función fue jugar y compartir. En mi experiencia, lo cantamos juntos.",
        ["incluye los datos de la ficha", "no usa nombres ni generaliza", "nombra cualidades y función"],
        ["ficha escrita"],
        ["escribir «todos» sin evidencia", "poner nombres de personas"],
        "Reconoce la ficha concreta y pide reemplazar cualquier «todos» o «nadie»; no pide compartir si no quiere.",
    ),
    "Escribe una frase de tu experiencia usando «en mi experiencia».",
    "Corrige tres frases con «todos» para que cuenten una experiencia concreta.",
)

# ---------------------------------------------------------------- OA 08 · clase 1
RES = {"audición": 4, "interpretación": 3, "creación": 5}
RES_TXT = ", ".join(f"{k}: {v} de 5 criterios" for k, v in RES.items())
MAXK = max(RES, key=RES.get)

L(
    OA8, 1,
    f"Lápiz y papel. Registro de una estudiante imaginaria, Camila, después de tres actividades: {RES_TXT}. Cada criterio cumplido se anota con evidencia.",
    "Aprenderé a identificar una fortaleza con evidencia en mi audición, mi interpretación y mi creación. Sirve para saber en qué soy bueno y seguir desde ahí.",
    ["Sé revisar con una lista.", "Sé que los errores son pistas.", "Sé nombrar cualidades del sonido."],
    [
        "Una fortaleza es algo que haces bien, y se reconoce con evidencia. La evidencia es lo que se puede ver o escuchar: por ejemplo, una lista con criterios cumplidos. Decir «soy bueno» no basta; hay que decir en qué y mostrar cómo lo sabes.",
        f"Mira el registro de Camila: {RES_TXT}. En audición cumplió 4 de 5 criterios, en interpretación 3 y en creación 5. Su fortaleza más clara es la {MAXK}, porque cumplió todos los criterios. Una fortaleza se apoya en datos: «en creación cumplí 5 de 5: usé pulso, motivo, contraste, variación y cierre».",
        "También puedes tener fortalezas pequeñas dentro de cada área. Por ejemplo, en interpretación: «mantuve el pulso en los silencios». Reconocer tus fortalezas te da confianza para trabajar lo que cuesta más. No se compara con otras personas: se compara contigo en el tiempo.",
    ],
    [("fortaleza", "algo que haces bien y puedes mostrar"), ("evidencia", "dato que se puede ver o escuchar"), ("criterio", "regla para revisar un trabajo"), ("audición", "escuchar con atención"), ("interpretación", "tocar o cantar")],
    [
        ("Hallar la fortaleza", f"Registro de Camila: {RES_TXT}. ¿En qué área tiene su mayor fortaleza?", ["Comparo 4, 3 y 5.", "El mayor es 5."], "En creación"),
        ("Escribir una fortaleza con evidencia", "Camila cumplió 5 de 5 criterios en creación. Escribe su fortaleza con evidencia.", ["Digo en qué área: creación.", "Doy el dato: 5 de 5 criterios."], "«Mi fortaleza es la creación: cumplí 5 de 5 criterios»"),
    ],
    [
        ("Decir «soy bueno» sin dar evidencia.", "No muestra cómo lo sabes.", "Agrega un dato, como los criterios cumplidos."),
        ("Compararse con otra persona para decidir la fortaleza.", "La fortaleza se mide con tus propios criterios.", "Compara con tu trabajo anterior."),
    ],
    [
        ex(f"Registro de Camila: {RES_TXT}. ¿Cuántos criterios cumplió en audición?", "4", "El registro lo dice."),
        ex(f"Registro de Camila: {RES_TXT}. ¿En qué área cumplió menos criterios?", "En interpretación", "Tiene 3 de 5."),
        ex("¿Una fortaleza se apoya en evidencia o en una opinión sin datos?", "En evidencia", "Se necesita un dato para reconocerla."),
    ],
    [
        ex(f"Registro de Camila: {RES_TXT}. ¿Cuántos criterios cumplió en total en las tres áreas?", str(sum(RES.values())), "4 + 3 + 5 = 12."),
        ex(f"Registro de Camila: {RES_TXT}. ¿Cuántos criterios más cumplió en creación que en interpretación?", str(RES["creación"] - RES["interpretación"]), "5 menos 3."),
        ex(f"Registro de Camila: {RES_TXT}. ¿Cuál es la frase que reconoce una fortaleza con evidencia: (a) «Soy buena en todo.» (b) «En creación cumplí 5 de 5 criterios.»?", "(b)", "La (b) da el área y el dato."),
    ],
    [
        arith(f"¿Cuántos criterios le faltaron a Camila en total para tener 15 de 15 en las tres áreas?", f"15-{sum(RES.values())}", "Se resta lo cumplido al total posible de 15 criterios.", " criterios"),
        ex(f"Registro de Camila: {RES_TXT}. ¿Qué área quedó en segundo lugar en cantidad de criterios cumplidos?", "Audición", "Creación tiene 5, audición 4 e interpretación 3."),
        ex("Dos estudiantes cumplen 4 de 5 criterios en audición. ¿Tienen que tener la misma fortaleza?", "No, depende de sus otras áreas", "Una fortaleza se define por el propio registro."),
    ],
    [
        ex("Pedro dice «mi fortaleza es cantar porque canto más fuerte que los demás». ¿Qué problema tiene?", "Compara con otros y habla de volumen, no de evidencia", "La fortaleza se apoya en criterios."),
        ex("Una niña cumple 5 de 5 criterios en audición pero no lo anota. ¿Puede decir que es su fortaleza?", "Sí, si puede mostrar el registro", "La evidencia es el registro."),
    ],
    [
        arith("En una semana cumples 2 criterios más cada día, de lunes a viernes. ¿Cuántos criterios más cumples en la semana?", "2*5", "Son 2 criterios por 5 días.", " criterios"),
        ex("Escribe una fortaleza con evidencia usando estos datos: interpretación, 4 de 5 criterios, mantuvo el pulso.", "En interpretación cumplí 4 de 5 criterios porque mantuve el pulso", "Área, dato y evidencia."),
    ],
    [ex("Después de una muestra, un curso revisa una lista de 5 criterios. Un estudiante cumplió 5. ¿Cómo debería expresar su fortaleza?", "Con el área, el dato y la evidencia", "Así queda comprobable.")],
    [ex("¿Qué es una fortaleza?", "Algo que haces bien y puedes mostrar", "Se apoya en evidencia."), ex("En Música: ¿Qué es la evidencia?", "Un dato que se puede ver o escuchar", "Hace comprobable la fortaleza."), ex("¿Con quién se compara tu avance?", "Contigo mismo en el tiempo", "No con otras personas.")],
    (
        "Toca con las palmas esta pieza: TA – TA – ti-ti – TAA – SIL (6 pulsos), tres veces, y revisa con esta lista de criterios: (1) mantuve el pulso, (2) toqué el silencio, (3) el TAA duró 2 pulsos, (4) toqué suave, (5) terminé a tiempo. Marca los que cumpliste. Escribe tu fortaleza con el área, el dato y la evidencia. No te compares con otras personas.",
        "Cumplí 4 de 5 criterios: mantuve el pulso, toqué el silencio, el TAA duró 2 pulsos y terminé a tiempo. Mi fortaleza en interpretación es mantener el pulso en los silencios.",
        ["revisa con los cinco criterios", "escribe una fortaleza con evidencia", "no se compara con otros"],
        ["interpretación", "escrito breve"],
        ["decir «soy bueno» sin dato", "compararse con otras personas"],
        "Reconoce la fortaleza con el dato y pide la evidencia; evita compararlo con otros.",
    ),
    "Di en voz alta una cosa que hiciste bien hoy en música y el dato que lo muestra.",
    "Escribe tres fortalezas con evidencia: una de audición, una de interpretación y una de creación.",
)

# ---------------------------------------------------------------- OA 08 · clase 2
ENSAYOS = [("ensayo 1", 2, 4, 3), ("ensayo 2", 3, 4, 3), ("ensayo 3", 3, 5, 3)]
ENS_TXT = " ".join(f"{n}: pulso {p} de 5, silencios {s} de 5, volumen {v} de 5." for n, p, s, v in ENSAYOS)
AREA_MENOS = {"pulso": sum(p for _n, p, _s, _v in ENSAYOS), "silencios": sum(s for _n, _p, s, _v in ENSAYOS), "volumen": sum(v for _n, _p, _s, v in ENSAYOS)}
PEOR = min(AREA_MENOS, key=AREA_MENOS.get)

L(
    OA8, 2,
    f"Lápiz y papel. Registro de ensayos de un estudiante imaginario, Tomás, con tres aspectos: {ENS_TXT}",
    "Aprenderé a localizar un área de mejora con precisión: qué aspecto exacto necesito practicar. Sirve para trabajar en lo que más ayuda.",
    ["Sé identificar una fortaleza.", "Sé revisar con criterios.", "Sé que un error es una pista."],
    [
        "Un área de mejora es un aspecto que todavía puedes hacer mejor. No es una falla personal: es una pista de qué practicar. Para localizarla hay que ser preciso. «Me va mal en música» no sirve. «Se me acelera el pulso en los silencios» sí sirve, porque dice qué y dónde.",
        f"Mira el registro de Tomás: {ENS_TXT} Sumando los tres ensayos: pulso {AREA_MENOS['pulso']} de 15, silencios {AREA_MENOS['silencios']} de 15 y volumen {AREA_MENOS['volumen']} de 15. El aspecto con menos puntaje es el {PEOR}, así que ese es su área de mejora principal.",
        "Después de encontrarla, escríbela en una frase: «Mi área de mejora es …, porque en los ensayos obtuve …». Así queda con evidencia. Mejorar un aspecto a la vez es más fácil que querer mejorarlo todo. Y recuerda: tener un área de mejora es normal; todas las personas tenemos varias. Pueden estar en la audición («confundo agudo con fuerte»), en la interpretación («se me acelera el pulso») o en la creación («mi motivo cambia cada vez y no se reconoce»).",
    ],
    [("área de mejora", "aspecto que se puede hacer mejor"), ("preciso", "que dice exactamente qué y dónde"), ("puntaje", "número de criterios cumplidos"), ("aspecto", "parte de un trabajo, como el pulso"), ("normal", "que le pasa a todas las personas")],
    [
        ("Sumar un aspecto", f"{ENS_TXT} ¿Cuántos puntos sumó el pulso en los tres ensayos?", ["Pulso: 2, 3 y 3.", "2 + 3 + 3 = 8."], f"{AREA_MENOS['pulso']} puntos"),
        ("Localizar el área de mejora", f"{ENS_TXT} ¿Qué aspecto sumó menos puntos en total?", [f"Pulso {AREA_MENOS['pulso']}, silencios {AREA_MENOS['silencios']}, volumen {AREA_MENOS['volumen']}.", f"El menor es {AREA_MENOS['pulso']}."], "El pulso"),
    ],
    [
        ("Decir «me va mal en música» sin precisar.", "No dice qué mejorar.", "Di qué aspecto y en qué parte."),
        ("Pensar que tener un área de mejora es ser malo.", "Es una pista para practicar.", "Todas las personas tienen áreas de mejora."),
    ],
    [
        ex("«Confundo los sonidos agudos con los fuertes.» ¿Es un área de mejora de audición, de interpretación o de creación?", "Audición", "Se trata de cómo escucha los sonidos."),
        ex("¿Un área de mejora es una falla personal o una pista de qué practicar?", "Una pista de qué practicar", "Dice qué trabajar."),
        ex("¿Cuál frase es más precisa: (a) «Me va mal.» (b) «Se me acelera el pulso en los silencios.»?", "(b)", "Dice qué y dónde."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos puntos sumó el volumen en los tres ensayos?", str(AREA_MENOS["volumen"]), "3 + 3 + 3 = 9."),
        ex(f"{ENS_TXT} ¿Cuántos puntos sumaron los silencios en los tres ensayos?", str(AREA_MENOS["silencios"]), "4 + 4 + 5 = 13."),
        ex("«Mi motivo cambia cada vez que lo repito y no se reconoce.» ¿Es un área de mejora de audición, de interpretación o de creación?", "Creación", "Se trata de cómo inventa y trabaja una idea musical."),
    ],
    [
        ex(f"{ENS_TXT} ¿Cuántos puntos más sumó el volumen que el pulso en los tres ensayos?", str(AREA_MENOS["volumen"] - AREA_MENOS["pulso"]), "El volumen suma 9 y el pulso 8."),
        arith(f"Tomás quiere llegar a 5 de 5 en el pulso. En el ensayo 3 tuvo 3. ¿Cuántos puntos le faltan?", "5-3", "Se resta lo logrado a lo que busca.", " puntos"),
        ex("¿Qué frase localiza mejor el área de mejora: (a) «Practiqué poco.» (b) «Mi pulso suma 8 de 15 y se acelera en los silencios.»?", "(b)", "La (b) dice el aspecto, el dato y dónde ocurre."),
    ],
    [
        ex("Una niña ve que dos de sus aspectos suman lo mismo y empatan como los más bajos. ¿Qué área elige primero?", "La que le parezca más importante para su propósito", "Cuando empatan, decide según el propósito."),
        ex("Pedro dice: «tengo cinco áreas de mejora; las practicaré todas hoy». ¿Qué le conviene?", "Elegir una y practicarla", "Mejorar un aspecto a la vez es más fácil."),
    ],
    [
        arith(f"En el ensayo 1 el pulso fue 2 y en el ensayo 3 fue 3. ¿Cuántos puntos subió?", "3-2", "Se restan los dos puntajes.", " punto"),
        ex(f"{ENS_TXT} Tomás elige mejorar el pulso. Escribe su área de mejora con evidencia en una frase que use el total.", "Mi área de mejora es el pulso: sumé 8 de 15 en los tres ensayos", "Dice el aspecto y el dato."),
    ],
    [ex("Una niña ve que en el último ensayo su pulso se aceleró en los silencios. ¿Cómo lo anota como área de mejora precisa?", "Mantener el pulso en los silencios", "Dice qué aspecto y en qué parte.")],
    [ex("¿Qué es un área de mejora?", "Un aspecto que puedes hacer mejor", "Se trabaja con práctica."), ex("¿Es normal tener áreas de mejora?", "Sí", "Todas las personas las tienen."), ex("¿Cuántos aspectos conviene mejorar a la vez?", "Uno", "Es más fácil enfocarse.")],
    (
        "Toca con las palmas tres veces la pieza TA – TA – ti-ti – TAA – SIL y anota en cada intento con ✓ o ✗ cada uno de estos aspectos: pulso parejo, silencio respetado, TAA de 2 pulsos, volumen suave, terminar a tiempo. Cuenta en cuántos de los tres intentos cumpliste cada aspecto (de 0 a 3) y escribe tu área de mejora principal con una frase que diga qué aspecto es y qué dato lo muestra.",
        "Pulso parejo 3 de 3, silencio respetado 1 de 3, TAA de 2 pulsos 3 de 3, volumen suave 2 de 3, terminar a tiempo 3 de 3. Mi área de mejora es respetar el silencio: lo cumplí solo 1 de 3 veces.",
        ["anota los tres intentos", "cuenta cuántas veces cumplió cada aspecto", "escribe un área de mejora precisa"],
        ["registro escrito", "interpretación con palmas"],
        ["decir «me va mal» sin precisar", "culparse"],
        "Reconoce la frase precisa y pregunta en qué parte exacta ocurre; si se culpa, reencuadra como pista.",
    ),
    "Escribe una frase precisa de algo que podrías mejorar en tu escucha.",
    "Revisa tu trabajo anterior de música y localiza un aspecto con menos puntaje.",
)

# ---------------------------------------------------------------- OA 08 · clase 3
ESTR = {
    "practicar lento": "ayuda cuando el pulso se acelera",
    "marcar el pulso con el pie": "ayuda a mantener el pulso y los silencios",
    "dividir en secciones": "ayuda cuando una parte de la pieza falla",
    "tocar más suave": "ayuda cuando el volumen es demasiado fuerte",
    "volver a escuchar y marcar lo que cambia": "ayuda cuando confundo agudo con fuerte (audición)",
    "cambiar una sola cualidad del motivo cada vez": "ayuda cuando mi motivo pierde su identidad (creación)",
}
ESTR_TXT = " ".join(f"({i}) {k}: {v}." for i, (k, v) in enumerate(ESTR.items(), 1))
MIN_DIA, DIAS = 5, 4

L(
    OA8, 3,
    f"Lápiz y papel. Estrategias de práctica: {ESTR_TXT} Plan de ejemplo: {MIN_DIA} minutos al día durante {DIAS} días.",
    "Aprenderé a elegir una estrategia de práctica que ayude a mejorar mi área, y a planificar cuándo practicar. Sirve para mejorar con un plan en vez de repetir sin pensar.",
    ["Sé localizar un área de mejora.", "Sé que los ensayos se registran.", "Sé calcular minutos."],
    [
        f"Una estrategia es un modo de practicar para mejorar un aspecto concreto. Estrategias posibles: {ESTR_TXT} No todas sirven para todo: hay que elegir la que se relaciona con tu área de mejora. Si te falla el volumen, practicar lento no ayuda tanto como tocar más suave.",
        f"Un buen plan de práctica dice: qué área mejoras, qué estrategia usas, cuántos minutos y cuántos días. Por ejemplo: «Área: el pulso en los silencios. Estrategia: marcar el pulso con el pie. {MIN_DIA} minutos al día durante {DIAS} días». Son {MIN_DIA} × {DIAS} = {MIN_DIA * DIAS} minutos en total.",
        "Practicar poco y seguido sirve más que practicar mucho una sola vez. Después de unos días, vuelve a revisar con la lista y anota si hubo cambios. Si la estrategia no ayudó, prueba otra: cambiar de estrategia también es aprender. Practica a volumen bajo y descansa si te cansas.",
    ],
    [("estrategia", "modo de practicar para mejorar algo"), ("plan de práctica", "área, estrategia, minutos y días"), ("constante", "que se hace seguido"), ("comprobar", "revisar si hubo cambio"), ("descansar", "parar un rato para no cansarse")],
    [
        ("Elegir la estrategia", f"Área de mejora: se acelera el pulso. {ESTR_TXT} ¿Qué estrategia conviene primero?", ["Busco la que ayuda cuando el pulso se acelera.", "Es practicar lento."], "Practicar lento"),
        ("Calcular el tiempo", f"Plan: {MIN_DIA} minutos al día durante {DIAS} días. ¿Cuántos minutos son?", [f"Cada día practicas {MIN_DIA} minutos durante {DIAS} días.", f"{MIN_DIA} × {DIAS} = {MIN_DIA * DIAS}."], f"{MIN_DIA * DIAS} minutos"),
    ],
    [
        ("Elegir una estrategia que no se relaciona con el área.", "No ayuda al aspecto que falla.", "Elige la estrategia que corresponde al área."),
        ("Practicar mucho un solo día y nada el resto.", "Se aprende mejor con práctica seguida.", "Practica poco cada día."),
    ],
    [
        ex(f"{ESTR_TXT} Si una parte de la pieza falla, ¿qué estrategia sirve?", "Dividir en secciones", "Permite practicar solo la parte que falla."),
        ex(f"{ESTR_TXT} Si el volumen es demasiado fuerte, ¿qué estrategia sirve?", "Tocar más suave", "Va directo al aspecto que falla."),
        ex("¿Qué cuatro datos tiene un plan de práctica?", "Área, estrategia, minutos y días", "Con eso queda claro qué hacer."),
    ],
    [
        arith(f"Practicas {MIN_DIA} minutos al día durante 6 días. ¿Cuántos minutos son?", f"{MIN_DIA}*6", "Se multiplican los minutos por los días.", " minutos"),
        ex(f"{ESTR_TXT} Si te cuesta mantener los silencios, ¿qué estrategia ayuda?", "Marcar el pulso con el pie", "Mantiene el pulso también en los silencios."),
        ex(f"{ESTR_TXT} Tu motivo pierde su identidad cuando cambias varias cosas a la vez. ¿Qué estrategia ayuda?", "Cambiar una sola cualidad del motivo cada vez", "Así el motivo sigue reconociéndose."),
    ],
    [
        arith("Un plan es 10 minutos al día en 3 días. Otro plan es 5 minutos al día en 5 días. ¿Cuál suma más minutos y cuántos?", "10*3-5*5", "El primero suma 30 y el segundo 25: la diferencia es 5.", " minutos más el primero"),
        ex(f"{ESTR_TXT} Confundes los sonidos agudos con los fuertes al escuchar. ¿Qué estrategia ayuda?", "Volver a escuchar y marcar lo que cambia", "Va directo al aspecto de la audición que falla."),
        ex("Una estrategia no ayudó después de cuatro días. ¿Qué haces?", "Pruebas otra estrategia", "Cambiar de estrategia también es aprender."),
    ],
    [
        ex("Ana practica 20 minutos seguidos un solo día. Pedro practica 5 minutos durante 4 días. ¿Quién practica con más constancia?", "Pedro", "Practica seguido, aunque poco."),
        ex("Una niña tiene dos áreas de mejora: pulso y volumen. ¿Qué plan conviene: trabajar las dos a la vez o elegir una primero?", "Elegir una primero", "Enfocarse mejora los resultados."),
    ],
    [
        arith("Quieres practicar 40 minutos en total, 5 minutos por día. ¿Cuántos días necesitas?", "40//5", "Se reparten 40 minutos en bloques de 5.", " días"),
        ex("Escribe un plan de práctica con área, estrategia, minutos y días para mantener el pulso en los silencios, con 5 minutos durante 4 días.", "Área: pulso en los silencios; estrategia: marcar el pulso con el pie; 5 minutos al día durante 4 días", "Incluye los cuatro datos."),
    ],
    [ex("Una estudiante tiene una presentación en dos semanas y le falla la sección B. ¿Qué estrategia y plan le sirven?", "Dividir en secciones y practicar la B unos minutos cada día", "Se enfoca en la parte que falla con práctica seguida.")],
    [ex("¿Qué es una estrategia de práctica?", "Un modo de practicar para mejorar algo", "Debe corresponder al área."), ex("¿Es mejor practicar poco y seguido o mucho una vez?", "Poco y seguido", "Se aprende mejor."), ex("¿Qué haces si la estrategia no ayuda?", "Pruebas otra", "Cambiar es parte de aprender.")],
    (
        f"Elige un área de mejora de las clases anteriores (por ejemplo, el pulso en los silencios o el volumen). Escribe un plan de práctica con: área, estrategia (elige una de la lista: {ESTR_TXT}), minutos por día y días. Calcula los minutos totales. Practica el primer día con las palmas y anota cómo te fue, sin compararte con otras personas.",
        f"Área: el pulso en los silencios. Estrategia: marcar el pulso con el pie. {MIN_DIA} minutos al día durante {DIAS} días: {MIN_DIA * DIAS} minutos. Primer día: mantuve el pulso en 3 de 4 silencios.",
        ["relaciona el área con la estrategia", "calcula bien los minutos", "anota el resultado del primer día"],
        ["plan escrito", "práctica"],
        ["elegir una estrategia que no corresponde", "planificar un solo día"],
        "Reconoce el plan con área y estrategia relacionadas y pide el cálculo; revisa que sean varios días.",
    ),
    "Practica una estrategia durante 5 minutos y anota si te ayudó.",
    "Escribe dos estrategias distintas para el mismo aspecto y di cuál probarías primero.",
)

# ---------------------------------------------------------------- OA 08 · clase 4
ANTES = {"pulso": 2, "silencios": 3, "volumen": 3}
DESPUES = {"pulso": 4, "silencios": 3, "volumen": 5}
ANT_TXT = ", ".join(f"{k}: {v} de 5" for k, v in ANTES.items())
DES_TXT = ", ".join(f"{k}: {v} de 5" for k, v in DESPUES.items())
CAMB = {k: DESPUES[k] - ANTES[k] for k in ANTES}

L(
    OA8, 4,
    f"Lápiz y papel. Antes de practicar, una estudiante imaginaria sumó: {ANT_TXT}. Después de cuatro días de práctica: {DES_TXT}.",
    "Aprenderé a comprobar mi progreso comparando mi trabajo antes y después, y a elegir un siguiente paso. Sirve para saber si mi práctica funcionó y qué hacer luego.",
    ["Sé localizar un área de mejora.", "Sé elegir una estrategia.", "Sé restar números."],
    [
        f"El progreso es el cambio entre cómo estabas antes y cómo estás después de practicar. Se comprueba comparando datos del mismo criterio. Antes: {ANT_TXT}. Después: {DES_TXT}. Si restamos, el pulso subió {CAMB['pulso']}, los silencios cambiaron {CAMB['silencios']} y el volumen subió {CAMB['volumen']}.",
        "Interpretar el cambio ayuda a decidir. Si subió, la estrategia funcionó. Si no cambió, hay que probar otra o practicar más tiempo. Si bajó, revisa si la estrategia fue adecuada o si estabas cansada. No te compares con otras personas: compárate con tu propio punto de partida.",
        "El siguiente paso es la decisión que tomas con esos datos. Por ejemplo: «El pulso mejoró, así que seguiré con la misma estrategia. Los silencios no cambiaron, así que probaré marcar el pulso con el pie». Un buen siguiente paso es concreto, corto y posible. Celebrar lo que mejoró también forma parte de aprender.",
    ],
    [("progreso", "cambio entre el antes y el después"), ("punto de partida", "cómo estabas al comienzo"), ("comparar", "mirar qué cambió entre dos datos"), ("siguiente paso", "decisión que tomas con los datos"), ("concreto", "claro y posible de hacer")],
    [
        ("Calcular un cambio", f"Antes: {ANT_TXT}. Después: {DES_TXT}. ¿Cuánto subió el volumen?", ["Antes: 3; después: 5.", "5 − 3 = 2."], f"{CAMB['volumen']} puntos"),
        ("Decidir el siguiente paso", f"Antes: {ANT_TXT}. Después: {DES_TXT}. Los silencios no cambiaron. ¿Qué haces con ese aspecto?", ["No hubo cambio.", "Pruebo otra estrategia o practico más tiempo."], "Probar otra estrategia o practicar más tiempo"),
    ],
    [
        ("Compararse con otra persona para saber si progresó.", "El progreso se mide contra uno mismo.", "Compara con tu punto de partida."),
        ("Pensar que si no hubo cambio fracasaste.", "Es una pista para probar otra cosa.", "Cambia la estrategia o el tiempo."),
    ],
    [
        ex(f"Antes: {ANT_TXT}. Después: {DES_TXT}. ¿Cuántos puntos subió el pulso?", str(CAMB["pulso"]), "4 menos 2."),
        ex(f"Antes: {ANT_TXT}. Después: {DES_TXT}. ¿Cuántos puntos cambiaron los silencios?", str(CAMB["silencios"]), "Tenían 3 y siguen en 3."),
        ex("¿El progreso se mide comparando con otra persona o con tu propio antes y después?", "Con tu propio antes y después", "Eso se llama punto de partida."),
    ],
    [
        ex(f"Antes: {ANT_TXT}. Después: {DES_TXT}. ¿En qué aspecto hubo mayor mejora?", "En el volumen y el pulso por igual", "Ambos subieron 2 puntos."),
        arith(f"Antes la suma de los tres aspectos era {sum(ANTES.values())}. Después, {sum(DESPUES.values())}. ¿Cuántos puntos subió el total?", f"{sum(DESPUES.values())}-{sum(ANTES.values())}", "Se resta el total de antes al de después.", " puntos"),
        ex("Si un aspecto no cambió, ¿qué siguiente paso conviene?", "Probar otra estrategia", "La que usaste no ayudó todavía."),
    ],
    [
        ex(f"Antes: {ANT_TXT}. Después: {DES_TXT}. ¿Qué aspecto tiene el puntaje más alto ahora?", "El volumen", "Tiene 5 de 5."),
        ex("Pedro dice que su pulso mejoró porque ahora toca mejor que Ana. ¿Qué problema tiene su frase?", "Se compara con otra persona y no con su antes", "El progreso se compara con el punto de partida."),
        ex("Una niña subió en el volumen, pero bajó en el pulso. ¿Qué siguiente paso conviene: (a) abandonar el volumen, (b) practicar el pulso con una estrategia sin perder el volumen?", "(b)", "Se trabaja lo que bajó sin perder lo ganado."),
    ],
    [
        ex("Un estudiante escribe: «Siguiente paso: mejorar». ¿Qué le falta para ser concreto?", "Decir qué aspecto, con qué estrategia y por cuánto tiempo", "Un siguiente paso concreto es posible de hacer."),
        arith("Un estudiante sube 2 puntos por semana en el pulso, partiendo de 1. ¿En cuántas semanas llega a 5?", "(5-1)//2", "Hay 4 puntos por subir, de a 2 por semana.", " semanas"),
    ],
    [
        ex("Completa con evidencia: «Mi pulso subió de 2 a 4. Mi siguiente paso es…». Elige: (a) «dejar de practicar el pulso» (b) «mantener la estrategia y aplicarla a los silencios»", "(b)", "Se aprovecha lo que funcionó."),
        arith(f"Si cada aspecto máximo es 5 y hay 3 aspectos, ¿cuántos puntos faltan para llegar al máximo después de practicar (suma {sum(DESPUES.values())})?", f"15-{sum(DESPUES.values())}", "El máximo es 3 × 5 = 15.", " puntos"),
    ],
    [ex("Una niña mejoró su volumen de 3 a 5 pero sus silencios siguen en 3. Escribe su siguiente paso.", "Probar una estrategia nueva para los silencios", "El silencio no ha cambiado.")],
    [ex("¿Qué es el progreso?", "El cambio entre el antes y el después", "Se mide con tus datos."), ex("¿Qué es un siguiente paso?", "Una decisión concreta con los datos", "Dice qué haces luego."), ex("¿Con quién te comparas?", "Contigo mismo", "Es tu punto de partida.")],
    (
        "Repite la pieza TA – TA – ti-ti – TAA – SIL tres veces y compara con tu primer intento (o con el ejemplo antes de practicar: pulso 2, silencios 3, volumen 3). Anota de 0 a 5 cada aspecto, calcula cuánto cambió cada uno y escribe tu siguiente paso concreto (aspecto, estrategia y tiempo). Escribe también una cosa que mejoró y que te alegra.",
        "Pulso: 2 a 4 (+2). Silencios: 3 a 3 (0). Volumen: 3 a 5 (+2). Mejoró el pulso y me alegra. Siguiente paso: practicar los silencios marcando el pulso con el pie, 5 minutos durante 4 días.",
        ["compara antes y después con restas", "interpreta el cambio", "escribe un siguiente paso concreto"],
        ["registro escrito", "interpretación"],
        ["compararse con otras personas", "escribir un siguiente paso vago"],
        "Reconoce la comparación con datos y el paso concreto; si es vago, pide aspecto, estrategia y tiempo.",
    ),
    "Cuenta a una persona de tu casa una cosa que mejoraste en música y cómo lo sabes.",
    "Haz una tabla antes-después para tres aspectos de otra actividad y escribe tu siguiente paso.",
)
