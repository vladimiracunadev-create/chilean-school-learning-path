"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 13 (textos explicativos con fuentes).

Todas las fuentes, tablas, entrevistas y borradores son originales e inventados («de ejemplo»);
cada ejercicio trae escritos los textos y datos que necesita.
Nota: los títulos de las clases del repositorio son específicos del eje; este cuaderno los sigue.
El «formato acordado» de referencias es el definido en la clase 2 de este cuaderno (no un estándar oficial).
"""
from __future__ import annotations

import re

from student_lessons import arith, ex, register

def E(q, a, why, calc=None):
    """Ejercicio cerrado; en las preguntas de tres opciones (a), (b), (c) reparte la correcta entre las tres posiciones."""
    import zlib
    m = list(re.finditer(r"\(([abc])\) ", q))
    if len(m) == 3 and [x.group(1) for x in m] == ["a", "b", "c"] and a.strip() in ("(a)", "(b)", "(c)"):
        stem = q[:m[0].start()]
        raw = [q[m[0].end():m[1].start()], q[m[1].end():m[2].start()], q[m[2].end():]]
        tail = ""
        last = raw[2].rstrip()
        if last.endswith(("?", ".")) and not (last.startswith(("¿", "¡")) and last.endswith("?") and last.count("?") == last.count("¿")):
            tail = last[-1]
            last = last[:-1]
        raw = [raw[0].strip(), raw[1].strip(), last.strip()]
        opts = []
        for o in raw:
            if o.endswith(".") or (o.endswith("?") and not o.startswith("¿")):
                o = o[:-1]
            opts.append(o.strip())
        if all(opts):
            correct = "abc".index(a.strip()[1])
            want = zlib.crc32((stem + "|".join(sorted(opts))).encode("utf-8")) % 3
            order = list(range(3))
            order.remove(correct)
            order.insert(want, correct)
            new = [opts[i] for i in order]
            mapping = {"abc"[old]: "abc"[pos] for pos, old in enumerate(order)}
            q = stem + " ".join(f"({'abc'[i]}) {t}" for i, t in enumerate(new)) + tail
            a = f"({'abc'[want]})"
            why = re.sub(r"\(([abc])\)", lambda x: f"({mapping[x.group(1)]})", why)
    return ex(q, a, why, calc)


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


OA = "LE07 OA 13"

FG = "Fuente G (entrevista de ejemplo, 8 de abril de 2024, a Marcos Lillo, coordinador): «La biblioteca nació en 2019 en una sede vecinal. Hoy tiene 1.800 libros y 6 voluntarios que atienden por turnos.»"
FH = "Fuente H (tabla de ejemplo, total de socios al cierre de cada año): 2020, 90; 2021, 140; 2022, 210; 2023, 260."
FI = "Fuente I (entrada sin autor ni fecha): «Estas bibliotecas son maravillosas y todos deberían ir.»"

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. Los temas, preguntas y audiencias están escritos en los ejercicios.",
  "Aprenderé a delimitar un tema, definir el propósito explicativo y pensar en la audiencia antes de escribir un texto que explica.",
  ["Sé que un texto informativo presenta datos y explicaciones.", "Sé distinguir un hecho de una opinión."],
  ["Un texto explicativo (como un artículo, un informe o un reportaje) tiene el propósito de que el lector comprenda un tema. No busca convencer, sino aclarar cómo funciona algo, por qué ocurre o qué es. Para lograrlo, el primer paso es delimitar el tema: pasar de un asunto muy amplio («las bibliotecas») a uno acotado que se pueda explicar bien («cómo funciona el préstamo de libros en la biblioteca vecinal de mi barrio»).",
   "Un tema bien delimitado se puede convertir en una pregunta guía: ¿cómo?, ¿por qué?, ¿qué es?, ¿cuántos? La pregunta guía orienta qué información buscar y qué dejar fuera. Si cada dato responde a la pregunta, el texto tiene unidad. Un tema demasiado amplio produce textos superficiales; uno demasiado estrecho se agota en dos líneas.",
   "También hay que pensar en la audiencia: ¿quién va a leer? Un texto para estudiantes de 3.º básico usa palabras más simples y más ejemplos que uno para jóvenes de 7.º. La audiencia decide el vocabulario, la cantidad de detalles y el tipo de ayuda gráfica. Antes de escribir, anota tres decisiones: tema delimitado, propósito (explicar) y audiencia."],
  [("texto explicativo", "texto que busca que el lector comprenda un tema"), ("delimitar", "acotar un tema para poder tratarlo bien"), ("pregunta guía", "pregunta que orienta la búsqueda y la escritura"), ("audiencia", "personas que leerán el texto"), ("propósito", "para qué se escribe el texto")],
  [("Delimitar un tema", "Tema amplio: «las bibliotecas». Delimítalo para explicarlo en una página y formula una pregunta guía.",
    ["Elijo un caso concreto: la biblioteca vecinal de un barrio.", "Elijo un aspecto: el préstamo de libros.", "Pregunta guía: ¿cómo funciona el préstamo de libros en esa biblioteca?"], "Tema: el préstamo de libros en la biblioteca vecinal; pregunta: ¿cómo funciona?"),
   ("Adaptar a la audiencia", "Debes explicar qué es un préstamo a estudiantes de 3.º básico y a estudiantes de 7.º. ¿Qué cambia?",
    ["Para 3.º: palabras simples y ejemplos cotidianos, como «llevar un libro a casa y devolverlo».", "Para 7.º: más datos y vocabulario como «plazo» y «socio».", "El tema es el mismo; cambian vocabulario y detalle."], "Cambian el vocabulario y la cantidad de detalle; el tema es el mismo")],
  [("Elegir un tema tan amplio que no se puede explicar.", "El texto queda superficial y desordenado.", "Delimita con un caso, un lugar o un aspecto."),
   ("Escribir sin pensar en quién leerá.", "El vocabulario puede ser muy difícil o muy simple.", "Anota la audiencia antes de escribir.")],
  ([E("Dos temas posibles: «Los animales» y «Cómo se alimenta el pingüino de Humboldt en su colonia». ¿Cuál es el tema más delimitado?", "«Cómo se alimenta el pingüino de Humboldt en su colonia»", "Precisa especie y aspecto."),
    E("Un texto que busca que el lector comprenda cómo funciona un reciclaje de papel, ¿tiene propósito explicativo o persuasivo?", "Explicativo", "Quiere aclarar un proceso."),
    E("¿Qué orienta la búsqueda de información: la pregunta guía o la cantidad de fuentes?", "La pregunta guía", "Define qué datos sirven y cuáles no.")],
   [E("Pregunta guía: «¿Cómo funciona el préstamo en la biblioteca vecinal?». ¿Qué dato sirve: el plazo de devolución o el precio de un libro nuevo en una librería?", "El plazo de devolución", "Responde la pregunta guía."),
    E("¿Qué palabra interrogativa orienta a explicar un proceso: «cómo» o «quién fue»?", "Cómo", "Pide pasos o funcionamiento."),
    E("Un texto para niños de 8 años, ¿usa más ejemplos cotidianos o más términos técnicos?", "Más ejemplos cotidianos", "La audiencia necesita ejemplos cercanos.")],
   [E("Delimitación elegida: «Quién atiende la biblioteca y cuándo». Subtemas posibles: (a) turnos de los voluntarios (b) historia de la imprenta (c) horario de atención. ¿Cuáles pertenecen?", "(a) y (c)", "Responden quién atiende y cuándo; (b) queda fuera."),
    E("Un compañero quiere explicar «todo sobre los océanos» en una página. ¿Qué le recomiendas?", "Delimitar el tema a un aspecto o un lugar", "Un tema tan amplio no cabe en una página."),
    arith("Un informe tiene 4 secciones y cada una usa 2 datos de la pregunta guía. ¿Cuántos datos usa en total?", "4*2", "Se multiplica el número de secciones por los datos de cada una.", " datos")],
   [E("Alguien escribe «Las bibliotecas son lo mejor del mundo» y dice que es un texto explicativo. ¿Tiene razón?", "No; expresa una opinión y no explica", "Un texto explicativo informa y aclara."),
    E("Si la audiencia son vecinos que nunca fueron a la biblioteca, ¿qué conviene explicar primero: cómo asociarse o la historia de las imprentas?", "Cómo asociarse", "Responde lo que necesita saber la audiencia.")],
   [E("Pregunta guía mal formulada: «¿Bibliotecas?». ¿Cómo la mejoras? (a) ¿Cómo se organizan los libros en la biblioteca vecinal? (b) ¿Qué son? (c) ¿Cuántos?", "(a)", "Es clara y acotada."),
    E("Tema delimitado: préstamo de libros. Audiencia: estudiantes de 5.º. Propósito: explicar. ¿Cuántas decisiones tomó el autor antes de escribir?", "3", "Tema, propósito y audiencia son tres decisiones.")]),
  [E("Tu curso hará una página para el diario mural sobre la biblioteca del colegio, dirigida a estudiantes nuevos de 5.º. ¿Cuál delimitación es mejor? (a) Todo sobre libros (b) Cómo pedir un libro prestado en la biblioteca del colegio (c) La historia de la escritura", "(b)", "Es acotada y útil para esa audiencia.")],
  [E("¿Qué hace un texto explicativo?", "Busca que el lector comprenda un tema", "No busca convencer."),
   E("¿Qué es delimitar un tema?", "Acotarlo para poder tratarlo bien", "Evita temas demasiado amplios."),
   E("¿Qué anotas antes de escribir?", "Tema delimitado, propósito y audiencia", "Son las tres decisiones previas.")],
  ("Elige uno de estos temas amplios: A) los volcanes, B) la música, C) el transporte público. Delimítalo en un caso o aspecto concreto, formula una pregunta guía, escribe el propósito y la audiencia, y anota tres datos que buscarías.",
   "Tema C. Delimitado: cómo funciona el pago con tarjeta en las micros de mi ciudad. Pregunta: ¿cómo se paga con tarjeta? Propósito: explicar. Audiencia: estudiantes de 5.º. Datos: cómo se carga la tarjeta, cuánto cuesta el pasaje, qué pasa si no hay saldo.",
   ["tema delimitado", "pregunta guía clara", "audiencia y datos coherentes con la pregunta"], ["ficha de cuatro líneas"],
   ["dejar el tema amplio", "buscar datos que no responden la pregunta"], "Muestra tu ficha a alguien y pregúntale si entiende qué vas a explicar."),
  "Escribe un tema amplio y delimítalo en una pregunta guía.",
  "Delimita el mismo tema para dos audiencias distintas y compara.")

# ================================================================== clase 2
L(OA, 2,
  "Este cuaderno y un lápiz. Las fuentes de ejemplo están escritas en los ejercicios.",
  "Aprenderé a seleccionar fuentes confiables, a registrar lo que encuentro en una ficha y a escribir su referencia en un formato acordado.",
  ["Sé delimitar un tema y formular una pregunta guía.", "Sé qué es una fuente."],
  ["Un texto explicativo se apoya en información de distintas fuentes: entrevistas, tablas, artículos, libros, mapas. Usar más de una fuente permite contrastar datos y mostrar el tema desde varios ángulos. Para elegir bien, revisa tres cosas: quién escribe (autor o institución), cuándo se publicó (fecha) y si responde tu pregunta guía (pertinencia). Una fuente sin autor ni fecha pide más cuidado.",
   "Para registrar lo encontrado usamos una ficha: pregunta guía, hallazgo (dato o idea en tus palabras o entre comillas), tipo de fuente y referencia. Anotar la referencia desde el comienzo evita perder el origen de un dato. Si copias palabras exactas, usa comillas; si lo cuentas con tus palabras (parafraseas), igual debes citar la fuente.",
   "En esta clase acordamos este formato de referencia: Apellido, Inicial. (año). Título. Tipo de fuente. Por ejemplo: Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista. Si no hay autor, se escribe el nombre de la institución o «Sin autor», y se advierte que la fuente es débil. Cuando el texto tenga varias referencias, se ordenan alfabéticamente por apellido."],
  [("fuente", "texto o persona de donde sale la información"), ("pertinencia", "relación directa de un dato con la pregunta guía"), ("parafrasear", "decir con palabras propias lo que dice una fuente"), ("referencia", "indicación de autor, año, título y tipo de una fuente"), ("ficha", "registro ordenado de lo encontrado")],
  [("Registrar una fuente", f"Pregunta guía: ¿desde cuándo existe la biblioteca vecinal? {FG} Completa la ficha.",
    ["Hallazgo: nació en 2019 en una sede vecinal.", "Tipo de fuente: entrevista.", "Referencia: Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista."], "Hallazgo: nació en 2019; referencia: Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista."),
   ("Evaluar una fuente", f"{FI} ¿Sirve para tu pregunta guía sobre cuántos socios tiene la biblioteca?",
    ["No tiene autor ni fecha.", "No entrega ninguna cifra, solo opiniones.", "No es pertinente ni confiable para esa pregunta."], "No sirve: sin autor, sin fecha y sin datos")],
  [("Anotar un dato sin referencia.", "Después no se sabe de dónde viene.", "Escribe la referencia al mismo tiempo."),
   ("Parafrasear sin citar la fuente.", "Aunque uses tus palabras, la idea es de otra persona.", "Cita siempre la fuente de la información.")],
  ([E(f"{FG} ¿Cuántos libros tiene la biblioteca según la entrevista?", "1.800 libros", "Es la cifra de la entrevista."),
    E("¿Qué tres cosas revisas al elegir una fuente?", "Autor, fecha y pertinencia", "Son los criterios de la clase."),
    E("Si copias palabras exactas, ¿qué usas?", "Comillas", "Marcan que son palabras de la fuente.")],
   [E(f"{FH} ¿Cuántos socios tenía la biblioteca al cierre de 2021?", "140", "Es el dato de 2021."),
    E(f"{FI} ¿Por qué es una fuente débil?", "Porque no tiene autor ni fecha", "No se puede saber quién la escribió."),
    E("¿Qué formato de referencia usamos? (a) Apellido, Inicial. (año). Título. Tipo de fuente. (b) Título, color, tamaño. (c) Solo el año.", "(a)", "Es el formato acordado en la clase.")],
   [E(f"{FG} Escribe la referencia de esta entrevista en el formato acordado.", "Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista.", "Sigue Apellido, Inicial. (año). Título. Tipo."),
    arith(f"{FH} ¿Cuántos socios más tenía la biblioteca al cierre de 2023 que al cierre de 2020?", "260-90", "Se resta el valor inicial al final.", " socios"),
    E(f"{FG} Pregunta guía: ¿cuántos voluntarios atienden? ¿Cuál es el hallazgo?", "6 voluntarios que atienden por turnos", "Es el dato pertinente.")],
   [E(f"{FG} Un estudiante anota «Hay muchos voluntarios» como hallazgo. ¿Es buen hallazgo?", "No; la entrevista dice 6, que es el dato preciso", "«Muchos» es vago; la fuente da una cifra."),
    E("Dos estudiantes anotan el mismo dato. Uno con referencia y otro sin ella. ¿Cuál ficha es mejor y por qué?", "La que tiene referencia, porque permite comprobar el origen", "La referencia da trazabilidad.")],
   [E(f"{FG} {FH} {FI} Para la pregunta ¿cuántos socios hubo al cierre de 2022?, ¿qué fuente usas?", "La fuente H", "Es la única que entrega ese dato."),
    E(f"{FH} La tabla no tiene autor personal. Escribe su referencia con la institución «Biblioteca Vecinal (de ejemplo)», año 2024, título «Socios por año» y tipo «Tabla».", "Biblioteca Vecinal (de ejemplo). (2024). Socios por año. Tabla.", "Usa la institución como autor, como se acordó en la clase.")]),
  [E(f"Vas a escribir sobre la biblioteca vecinal. Encuentras {FI} ¿La usas como fuente principal?", "No; sin autor ni fecha y sin datos", "No aporta información comprobable.")],
  [E("En Lenguaje: ¿Qué es parafrasear?", "Decir con palabras propias lo que dice una fuente", "Se debe citar igual."),
   E("¿Cómo se ordenan varias referencias?", "Alfabéticamente por apellido", "Es la regla acordada."),
   E("¿Qué indica la referencia?", "De dónde viene una información", "Permite que otra persona la verifique.")],
  ("Llena una ficha con estas tres fuentes de ejemplo para la pregunta «¿Cuántos libros y voluntarios tiene la biblioteca y cómo creció el número de socios?». " + FG + " " + FH + " " + FI + " Anota hallazgos, tipo de fuente y referencia, y marca cuál fuente descartas. Para las referencias: la tabla (fuente H) es de la institución Biblioteca Vecinal (de ejemplo), año 2024, título «Socios por año».",
   "Fuente G: 1.800 libros y 6 voluntarios; referencia: Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista. Fuente H: socios 90, 140, 210 y 260 entre 2020 y 2023; referencia: Biblioteca Vecinal (de ejemplo). (2024). Socios por año. Tabla. Descarto la fuente I porque no tiene autor ni fecha ni datos.",
   ["usa los datos exactos", "escribe referencias en el formato", "descarta la fuente débil con razón"], ["ficha escrita"],
   ["copiar sin comillas", "omitir la referencia"], "Pide a alguien que encuentre un dato en tu ficha usando solo la referencia."),
  "Escribe la referencia de un libro o artículo de tu casa en el formato acordado.",
  "Inventa tres fuentes de ejemplo para un tema que te guste y evalúa cuál es la más confiable.")

# ================================================================== clase 3
PARR = "Cómo funciona la biblioteca vecinal. La biblioteca nació en 2019 en una sede vecinal. Hoy atiende con voluntarios por turnos. Gracias a ellos, el número de socios creció cada año. Por eso hoy puede ofrecer más horarios."
L(OA, 3,
  "Este cuaderno y un lápiz. Los párrafos y planes están escritos en los ejercicios.",
  "Aprenderé a organizar un texto explicativo con una progresión temática clara: presentación, desarrollo ordenado y cierre.",
  ["Sé delimitar un tema y registrar fuentes.", "Sé qué son los conectores."],
  ["Un texto explicativo se organiza en tres partes: presentación del tema (qué se va a explicar y por qué importa), desarrollo (los aspectos explicados en orden) y cierre. En el desarrollo, cada párrafo trata un aspecto, y los párrafos se ordenan con un criterio claro: cronológico (primero, luego), de causa a consecuencia, de lo general a lo particular o por comparación.",
   "La progresión temática es la manera en que avanza la información. Cada oración tiene un tema (de qué se habla) y un rema (lo que se dice de él). En la progresión lineal, el rema de una oración pasa a ser el tema de la siguiente: «La biblioteca nació en 2019. Esa fecha coincide con…». En la progresión constante, se mantiene el mismo tema: «La biblioteca nació en 2019. Hoy atiende… Además ofrece…». Una buena mezcla evita repetir y evita saltos.",
   "Para ordenar, haz un plan de párrafos con una idea principal para cada uno y revisa que cada oración aporte al tema. Usa conectores de orden (primero, luego, finalmente), de causa (porque, por eso) y de ejemplo (por ejemplo). Si un dato no encaja en ninguna parte, quizás pertenece a otro texto."],
  [("progresión temática", "manera en que la información avanza de una oración a otra"), ("tema", "de qué se habla en una oración"), ("rema", "lo que se dice del tema"), ("plan de párrafos", "lista de las ideas principales en el orden en que aparecerán"), ("conector de orden", "palabra que ordena ideas, como primero o luego")],
  [("Identificar tema y rema", "«La biblioteca nació en 2019. Esa fecha coincide con la apertura de la sede vecinal.» ¿Qué tipo de progresión hay?",
    ["Oración 1: tema «la biblioteca», rema «nació en 2019».", "Oración 2: tema «esa fecha» (retoma el rema anterior).", "El rema pasa a ser tema: progresión lineal."], "Progresión lineal"),
   ("Ordenar un plan", "Aspectos: (a) cierre con una síntesis, (b) presentación del tema, (c) cómo se financia, (d) cuántos voluntarios atienden. Ordena un plan lógico.",
    ["La presentación va primero.", "El desarrollo explica aspectos de la biblioteca: voluntarios y financiamiento.", "El cierre va al final."], "b, d, c, a")],
  [("Mezclar aspectos distintos en un solo párrafo.", "El lector pierde el hilo.", "Cada párrafo trata un aspecto."),
   ("Cambiar de tema entre oraciones sin conectar.", "Parecen saltos.", "Retoma una idea anterior o usa un conector.")],
  ([E("¿Cuáles son las tres partes de un texto explicativo?", "Presentación, desarrollo y cierre", "Esa es la organización básica."),
    E("¿Qué es el rema de una oración?", "Lo que se dice del tema", "Es la información nueva."),
    E("En «Primero se inscribe el socio. Luego recibe su carnet», ¿qué conectores ordenan?", "Primero y luego", "Marcan el orden de los pasos.")],
   [E(f"{PARR} ¿Qué conector expresa consecuencia?", "Por eso", "Une «más socios» con «más horarios»."),
    E("«La biblioteca tiene libros. Los libros llegan por donaciones.» ¿Qué tipo de progresión hay: lineal o constante?", "Lineal", "El rema de la primera pasa a ser el tema de la segunda."),
    E("«La biblioteca abre. La biblioteca presta. La biblioteca organiza talleres.» ¿Qué tipo de progresión hay: lineal o constante?", "Constante", "Se mantiene el mismo tema.")],
   [E("Ordena un plan para explicar el préstamo: a) devolver el libro, b) inscribirse como socio, c) elegir y llevar el libro. Escribe las letras en orden.", "b, c, a", "Sigue el orden cronológico del proceso."),
    E(f"{PARR} ¿Qué conector falta para unir «Hoy atiende con voluntarios por turnos» con «el número de socios creció»? Elige: (a) Gracias a ellos (b) Sin embargo (c) Por ejemplo", "(a)", "Muestra la causa del crecimiento."),
    arith("Un texto tiene 5 párrafos de desarrollo y cada uno desarrolla un aspecto con 3 oraciones. ¿Cuántas oraciones tiene el desarrollo?", "5*3", "Se multiplican los párrafos por las oraciones de cada uno.", " oraciones")],
   [E("Un párrafo mezcla horarios, historia de la biblioteca y precio de un libro. ¿Qué problema tiene?", "Mezcla tres aspectos distintos", "Cada párrafo debe tratar un aspecto."),
    E("Un cierre dice: «Además, la semana próxima habrá un concurso». ¿Es un buen cierre?", "No; agrega información nueva en vez de sintetizar", "El cierre resume o proyecta, no introduce datos nuevos.")],
   [E("Plan de párrafos: 1 presentación, 2 voluntarios, 3 socios, 4 libros, 5 cierre. El estudiante pone «libros» al final, después del cierre. ¿Qué cambia?", "Debe moverse antes del cierre", "El cierre va al final."),
    E("«Los voluntarios son 6. Ellos atienden por turnos. Estos turnos cubren dos tardes.» ¿Qué palabra retoma el tema anterior en la última oración?", "Estos turnos", "Retoma «por turnos» de la oración anterior.")]),
  [E("Quieres explicar a estudiantes de 5.º cómo funciona la biblioteca del colegio. ¿Cuál es un buen orden? (a) Presentación, cómo pedir un libro, cómo devolverlo y cierre. (b) Cierre, cómo devolver, presentación. (c) Solo el cierre.", "(a)", "Sigue una progresión lógica.")],
  [E("¿En qué parte del texto se presenta el tema?", "En la presentación", "Es la primera parte."),
   E("¿Qué es la progresión constante?", "Mantener el mismo tema en varias oraciones", "Repite el tema como punto de partida."),
   E("¿Para qué sirve un plan de párrafos?", "Para ordenar las ideas principales antes de escribir", "Evita saltos y repeticiones.")],
  ("Ordena un plan de párrafos para explicar «cómo funciona el préstamo de libros» usando estos aspectos desordenados: horario, cómo inscribirse, cierre, cómo devolver, presentación, cómo llevar un libro. Escribe una idea principal de una línea para cada párrafo.",
   "1) Presentación: la biblioteca presta libros a los socios. 2) Cómo inscribirse. 3) Horario. 4) Cómo llevar un libro. 5) Cómo devolver. 6) Cierre: síntesis de los pasos.",
   ["presentación primero y cierre al final", "orden lógico", "una idea por párrafo"], ["plan de seis líneas"],
   ["poner el cierre en medio", "mezclar dos aspectos en un párrafo"], "Pide a otra persona que siga tu plan y vea si el orden se entiende."),
  "Ordena los pasos para preparar un té y escribe un conector entre cada uno.",
  "Escribe tres oraciones con progresión lineal y tres con progresión constante.")

# ================================================================== clase 4
L(OA, 4,
  "Este cuaderno y un lápiz. Las fuentes de ejemplo están escritas en los ejercicios.",
  "Aprenderé a desarrollar las ideas de un texto explicativo con hechos, descripciones, ejemplos y explicaciones, integrando información de distintas fuentes.",
  ["Sé organizar un plan de párrafos.", "Sé registrar fuentes."],
  ["Una idea principal necesita desarrollo. Hay cuatro recursos básicos. El hecho o dato es información comprobable («1.800 libros»). La descripción muestra cómo es algo («la sede tiene estantes de madera y una mesa grande»). El ejemplo ilustra con un caso («por ejemplo, un vecino puede llevar dos libros por 15 días»). La explicación da razones o causas («el préstamo es gratuito porque los libros son donados»).",
   "Cuando integras varias fuentes, no pegues sus frases una tras otra. Úsalas para construir tu propia explicación: parafrasea, une los datos con conectores y cita entre paréntesis (Lillo, 2024). Por ejemplo: «La biblioteca nació en 2019 (Lillo, 2024) y, desde entonces, sus socios aumentaron de 90 a 260 entre 2020 y 2023 (Biblioteca Vecinal, 2024)». Las dos fuentes se complementan.",
   "Revisa tu párrafo con tres preguntas: ¿cada dato responde la pregunta guía?, ¿distingo hechos de opiniones?, ¿puse la fuente de cada dato? Si una fuente es débil (sin autor ni fecha), no la uses para sostener un hecho importante. Un buen desarrollo es preciso, ordenado y no repite lo mismo con otras palabras."],
  [("hecho o dato", "información comprobable"), ("descripción", "texto que muestra cómo es algo"), ("ejemplo", "caso que ilustra una idea"), ("explicación", "razón o causa que aclara algo"), ("cita entre paréntesis", "indicación breve de la fuente, como (Lillo, 2024)")],
  [("Reconocer recursos", "«El préstamo es gratuito porque los libros llegan por donaciones. Por ejemplo, un vecino puede llevarse dos libros por 15 días.» ¿Qué recursos hay?",
    ["«El préstamo es gratuito porque los libros llegan por donaciones»: explicación (causa).", "«Un vecino puede llevarse dos libros por 15 días»: ejemplo con un dato.", "Los datos «dos libros» y «15 días» son hechos."], "Una explicación (causa) y un ejemplo con datos"),
   ("Integrar dos fuentes", f"{FG} {FH} Escribe una oración que una ambas fuentes con citas.",
    ["De G tomo el año de inicio: 2019.", "De H tomo el crecimiento: de 90 a 260 socios entre 2020 y 2023.", "Uno con un conector y cito: «Nacida en 2019 (Lillo, 2024), la biblioteca pasó de 90 a 260 socios entre 2020 y 2023 (Biblioteca Vecinal, 2024)»."], "«Nacida en 2019 (Lillo, 2024), la biblioteca pasó de 90 a 260 socios entre 2020 y 2023 (Biblioteca Vecinal, 2024)»")],
  [("Pegar frases de las fuentes una tras otra.", "No hay explicación propia ni relación entre los datos.", "Parafrasea y une con conectores."),
   ("Usar una fuente débil para un dato importante.", "El dato puede no ser confiable.", "Apóyate en fuentes con autor y fecha.")],
  ([E("«La sede tiene estantes de madera y una mesa grande.» ¿Es hecho, descripción o ejemplo?", "Descripción", "Muestra cómo es el lugar."),
    E("«La biblioteca tiene 1.800 libros.» ¿Es dato, ejemplo o explicación?", "Dato", "Es una cifra comprobable."),
    E("¿Qué recurso da razones o causas?", "La explicación", "Aclara por qué ocurre algo.")],
   [E("«Por ejemplo, un vecino puede llevarse dos libros por 15 días.» ¿Qué recurso usa?", "Ejemplo", "Ilustra con un caso concreto."),
    E(f"{FG} ¿Qué cita entre paréntesis corresponde a esta fuente en el formato de la clase?", "(Lillo, 2024)", "Lleva apellido y año."),
    E("¿Qué conectores unen un dato con su causa: porque o también?", "Porque", "Introduce una causa.")],
   [E(f"{FH} Escribe un dato de esta fuente que sirva para explicar el crecimiento. ¿Cuántos socios hubo al cierre de 2022?", "210", "Es el dato de esa fila."),
    arith(f"{FH} ¿Cuántos socios aumentó la biblioteca entre el cierre de 2022 y el de 2023?", "260-210", "Se resta el valor anterior al posterior.", " socios"),
    E(f"{FG} {FH} ¿Qué oración integra bien las dos fuentes? (a) Con 6 voluntarios (Lillo, 2024), la biblioteca llegó a 260 socios en 2023 (Biblioteca Vecinal, 2024). (b) La biblioteca es bonita. (c) Hay libros y socios.", "(a)", "Une dos datos de fuentes distintas y los cita.")],
   [E(f"{FI} Un estudiante escribe «La biblioteca es maravillosa (Sin autor)». ¿Qué problema tiene?", "Usa una opinión de una fuente débil como si fuera hecho", "No es un dato comprobable ni confiable."),
    E("Un párrafo repite tres veces que «hay muchos socios» con distintas palabras. ¿Qué le falta?", "Datos precisos que desarrollen la idea", "Desarrollar es agregar información, no repetirla.")],
   [E(f"{FG} {FH} Un estudiante afirma: «Los 6 voluntarios causaron el aumento de 90 a 260 socios». ¿Lo demuestran las fuentes?", "No; muestran los dos datos, pero no que uno cause el otro", "Dos datos juntos no prueban una relación de causa."),
    arith(f"{FH} Entre el cierre de 2020 (90) y el de 2021 (140), ¿cuántos socios más hubo? Y entre 2021 y 2022 (210), ¿cuántos? Responde la suma de ambos aumentos.", "(140-90)+(210-140)", "Se calculan los dos aumentos y se suman.", " socios")]),
  [E(f"Debes explicar a tu curso en un párrafo cómo creció la biblioteca. Tienes {FH} ¿Qué dos años elegirías para mostrar el aumento más claro?", "2020 y 2023", "Muestran el punto inicial y el final de la tabla.")],
  [E("¿Qué cuatro recursos desarrollan una idea?", "Hecho, descripción, ejemplo y explicación", "Son los recursos de la clase."),
   E("¿Cómo se cita en el texto a Lillo, 2024?", "(Lillo, 2024)", "Apellido y año entre paréntesis."),
   E("¿Se deben pegar frases de las fuentes sin elaborarlas?", "No", "Hay que parafrasear y unir.")],
  ("Escribe un párrafo de cuatro a cinco líneas que explique cómo funciona y crece la biblioteca vecinal usando solo estos datos: " + FG + " " + FH + " Incluye un dato, una explicación de cómo funciona (sin afirmar causas que las fuentes no prueban), un ejemplo con cifras de la tabla y dos citas entre paréntesis.",
   "La biblioteca nació en 2019 y hoy tiene 1.800 libros (Lillo, 2024). Atiende con 6 voluntarios por turnos, es decir, se reparten las tardes para que siempre haya alguien que preste los libros. Sus socios aumentaron de 90 a 260 entre 2020 y 2023 (Biblioteca Vecinal, 2024). Por ejemplo, entre 2022 y 2023 se sumaron 50 socios, de 210 a 260.",
   ["incluye un dato verificable", "explica sin afirmar causas que las fuentes no prueban", "cita las dos fuentes"], ["párrafo de cuatro a cinco líneas"],
   ["inventar datos o causas", "omitir las citas"], "Subraya en tu párrafo dónde está cada recurso y cada cita."),
  "Escribe un dato y un ejemplo sobre un lugar de tu barrio.",
  "Reescribe tu párrafo para una audiencia de 3.º básico.")

# ================================================================== clase 5
L(OA, 5,
  "Este cuaderno y un lápiz. Los textos y las tablas están escritos en los ejercicios.",
  "Aprenderé a usar correferencias (anáforas) para evitar repeticiones y a incorporar recursos gráficos pertinentes en un texto explicativo.",
  ["Sé organizar un texto y recuperar referentes.", "Sé leer tablas y gráficos."],
  ["Una anáfora es una palabra o expresión que retoma algo ya mencionado en el texto. Sirve para no repetir y para unir las oraciones. Hay varias formas: el pronombre («la biblioteca… ella»), el sinónimo («el local»), una expresión más general («el lugar») o una descripción («la sede vecinal»). Y también la elipsis, cuando se omite lo que se sobreentiende.",
   "Para usar bien las anáforas, comprueba que el lector sepa a quién se refieren. Si hay dos posibles referentes, es ambiguo y conviene repetir el nombre. Evita también repetir la misma palabra más de dos veces seguidas. Alterna con pronombres y expresiones equivalentes sin cambiar el sentido.",
   "Los recursos gráficos (tablas, gráficos, ilustraciones, mapas) deben ser pertinentes: ayudar a entender, no decorar. Cada recurso lleva un título o pie, la fuente de los datos y una mención dentro del texto («como muestra la Tabla 1»). Elige el tipo según el dato: una tabla para varios valores exactos, un gráfico para ver cambios o comparaciones, una ilustración para mostrar un proceso."],
  [("anáfora", "palabra o expresión que retoma algo ya mencionado"), ("correferencia", "relación entre dos expresiones que se refieren a lo mismo"), ("sinónimo", "palabra de significado parecido"), ("recurso gráfico", "tabla, gráfico, mapa o ilustración que acompaña el texto"), ("pie de figura", "texto breve bajo una imagen o tabla que la explica")],
  [("Evitar repeticiones", "Texto: «La biblioteca vecinal abre dos tardes. La biblioteca vecinal presta libros. La biblioteca vecinal tiene 6 voluntarios.» Reescríbelo con anáforas.",
    ["Reemplazo la segunda mención por un pronombre o elipsis: «Presta libros».", "Reemplazo la tercera por una expresión equivalente: «El local».", "Reviso que el lector entienda de quién se habla."], "«La biblioteca vecinal abre dos tardes. Presta libros. El local tiene 6 voluntarios.»"),
   ("Elegir un recurso gráfico", f"{FH} Quieres mostrar cómo creció el número de socios de 2020 a 2023. ¿Qué recurso eliges y qué le agregas?",
    ["Quiero ver un cambio en el tiempo: un gráfico de líneas o barras sirve.", "Le agrego título, la fuente de los datos y una mención en el texto.", "Si necesito los valores exactos, también puedo añadir la tabla."], "Un gráfico con título, fuente y mención en el texto")],
  [("Repetir la misma palabra en cada oración.", "El texto suena torpe.", "Alterna pronombres, sinónimos y elipsis."),
   ("Poner un gráfico sin mencionarlo ni dar su fuente.", "El lector no sabe para qué sirve ni de dónde viene.", "Menciona el recurso en el texto y escribe un pie.")],
  ([E("«Marta trajo un libro. Ella lo dejó en la mesa.» ¿Qué palabra retoma a Marta?", "Ella", "Es un pronombre que reemplaza el nombre."),
    E("¿Qué es una anáfora?", "Una expresión que retoma algo ya mencionado", "Evita repetir y une las oraciones."),
    E("«El perro corrió. El animal saltó la reja.» ¿Qué expresión retoma al perro?", "El animal", "Es una expresión más general.")],
   [E("«La directora abrió la biblioteca. La directora saludó. La directora entregó llaves.» ¿Cómo evitas repetir más de dos veces seguidas?", "Usando pronombres o elipsis: Saludó y entregó llaves", "Se alternan formas para no repetir."),
    E("Para ver cambios en el tiempo, ¿conviene una tabla o un gráfico de líneas?", "Un gráfico de líneas", "Muestra la evolución visualmente."),
    E("¿Qué lleva un recurso gráfico además de los datos: título y fuente?", "Título, fuente y mención en el texto", "Son los elementos de la clase.")],
   [E("Reescribe con una anáfora: «Los vecinos pintaron el mural. Los vecinos celebraron el resultado». ¿Cuál queda mejor? (a) Los vecinos pintaron el mural. Ellos celebraron el resultado. (b) Los vecinos pintaron el mural. Mural celebraron. (c) Pintaron los vecinos y los vecinos.", "(a)", "Usa un pronombre claro."),
    E("«Rita habló con Camila. Ella la saludó.» ¿Qué problema hay?", "Es ambiguo: no se sabe quién saludó", "Hay dos posibles referentes."),
    E(f"{FH} ¿Qué título pondrías a un gráfico de estos datos? (a) Total de socios al cierre de cada año, 2020 a 2023 (b) Gráfico (c) Libros", "(a)", "Describe qué mide y el periodo.")],
   [E("Un estudiante pone una ilustración de un estadio de fútbol en un texto sobre la biblioteca vecinal. ¿Es pertinente?", "No; no ayuda a entender el tema", "Un recurso gráfico debe aportar a la comprensión."),
    E("En el texto escribes: «El número de socios creció (ver Tabla 1)». ¿Por qué es útil esa mención?", "Porque conecta el texto con el recurso", "Guía al lector para ver los datos.")],
   [E("Reescribe sin repetir «la biblioteca»: «La biblioteca atiende en la tarde. La biblioteca ofrece talleres. La biblioteca recibe donaciones». ¿Qué versión es mejor? (a) La biblioteca atiende en la tarde, ofrece talleres y recibe donaciones. (b) La biblioteca atiende, la biblioteca ofrece, la biblioteca recibe. (c) Biblioteca atiende talleres donaciones.", "(a)", "Mantiene el sujeto con elipsis y no repite."),
    arith(f"{FH} Si se hace un gráfico de barras con 4 años y cada barra mide, en centímetros, el número de socios dividido por 10, ¿cuántos centímetros mide la barra de 2023?", "260//10", "Se divide 260 entre 10.", " cm")]),
  [E("En tu informe sobre el reciclaje del colegio escribes: «El reciclaje del colegio recolectó 40 kilos. El reciclaje del colegio recolectó 55 kilos al mes siguiente». ¿Qué cambio haces? (a) Reemplazar el segundo «El reciclaje del colegio» por «Este programa» (b) No cambiar nada (c) Borrar la cifra", "(a)", "Evita repetir y mantiene la referencia clara.")],
  [E("¿Qué es una correferencia?", "Relación entre dos expresiones que se refieren a lo mismo", "Evita repetir y une oraciones."),
   E("¿Qué se hace antes de mostrar una tabla?", "Se menciona en el texto y se agrega título y fuente", "Así el lector sabe para qué sirve."),
   E("¿Un recurso gráfico puede ser solo decorativo?", "No", "Debe ser pertinente.")],
  ("Revisa este texto de ejemplo y reescríbelo con anáforas y mencionando un recurso gráfico: «La biblioteca vecinal tiene 1.800 libros. La biblioteca vecinal tiene 6 voluntarios. Los socios aumentaron de 90 a 260 entre 2020 y 2023». Agrega el título de un gráfico adecuado.",
   "La biblioteca vecinal tiene 1.800 libros. Cuenta además con 6 voluntarios. Sus socios aumentaron de 90 a 260 entre 2020 y 2023, como muestra el Gráfico 1. Título del gráfico: Total de socios al cierre de cada año, 2020 a 2023.",
   ["usa anáforas claras", "evita repeticiones", "menciona el gráfico y da un título"], ["texto reescrito y título"],
   ["crear ambigüedad", "no mencionar el gráfico en el texto"], "Subraya tus anáforas y comprueba que cada una tenga un referente claro."),
  "Reescribe una oración repetitiva usando un pronombre.",
  "Diseña la tabla y el gráfico para otros cuatro datos de tu elección.")

# ================================================================== clase 6
L(OA, 6,
  "Este cuaderno y un lápiz. Los textos y las referencias están escritos en los ejercicios.",
  "Aprenderé a cerrar un texto explicativo de manera coherente y a escribir las referencias con el formato acordado.",
  ["Sé organizar, desarrollar y conectar un texto explicativo.", "Sé escribir citas y referencias."],
  ["El cierre de un texto explicativo recuerda lo esencial y deja una idea final. No agrega información nueva ni opiniones que el texto no preparó. Puede sintetizar (resumir la idea central), proyectar (decir qué pasaría o qué falta saber) o valorar con prudencia lo explicado. Debe coincidir con el género: un informe cierra con conclusiones; un artículo, con una síntesis y una mirada hacia adelante.",
   "Las referencias van al final, en una lista titulada «Referencias». Cada fuente que se citó en el texto debe aparecer en la lista, y cada fuente de la lista debe haberse citado. Se ordenan alfabéticamente por apellido o nombre de la institución y siguen el formato acordado: Apellido, Inicial. (año). Título. Tipo de fuente.",
   "Antes de entregar, haz una lista de revisión: ¿el tema está presentado?, ¿hay información de distintas fuentes?, ¿hay hechos, ejemplos y explicaciones?, ¿la progresión es clara?, ¿usé anáforas y un recurso gráfico pertinente?, ¿el cierre es coherente?, ¿las referencias están completas y ordenadas? Esta lista resume los criterios del texto explicativo."],
  [("cierre", "parte final que sintetiza o proyecta lo explicado"), ("síntesis", "resumen de la idea central"), ("proyección", "mirada hacia lo que viene o falta saber"), ("lista de referencias", "lista final de las fuentes citadas"), ("coherente", "que mantiene relación lógica con el resto del texto")],
  [("Escribir un cierre", f"{FG} {FH} Escribe un cierre de dos oraciones para un texto sobre el crecimiento de la biblioteca.",
    ["Sintetizo: la biblioteca creció de 90 a 260 socios entre 2020 y 2023.", "Proyecto sin inventar: queda por saber cómo seguirá creciendo.", "No agrego datos nuevos."], "«La biblioteca pasó de 90 a 260 socios entre 2020 y 2023. Queda por observar si seguirá creciendo con sus 6 voluntarios.»"),
   ("Ordenar referencias", "Referencias desordenadas: Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista. / Biblioteca Vecinal (de ejemplo). (2024). Socios por año. Tabla. Ordénalas.",
    ["Se ordenan alfabéticamente por el primer elemento.", "«Biblioteca» empieza con B y «Lillo» con L.", "Primero la tabla de la biblioteca; luego la entrevista."], "Primero Biblioteca Vecinal (de ejemplo)…, luego Lillo, M. …")],
  [("Agregar información nueva en el cierre.", "El lector no tiene cómo conectarla con el desarrollo.", "Sintetiza lo que ya explicaste."),
   ("Citar una fuente y no ponerla en la lista de referencias.", "El lector no puede encontrarla.", "Revisa que cada cita tenga su referencia.")],
  ([E("¿Qué hace el cierre de un texto explicativo: sintetiza o inicia un tema nuevo?", "Sintetiza", "Recuerda lo esencial."),
    E("¿Dónde van las referencias: al comienzo o al final?", "Al final", "Se agrupan en una lista final."),
    E("¿Se puede agregar un dato totalmente nuevo en el cierre?", "No", "El cierre no introduce información nueva.")],
   [E("Cierre A: «En resumen, la biblioteca creció porque más vecinos se sumaron». Cierre B: «Además, el próximo año se venderán entradas a un concierto». ¿Cuál es coherente con un texto sobre el crecimiento?", "El cierre A", "El B introduce un tema nuevo."),
    E("Referencias: Pérez, A. (2022). Lectura barrial. Artículo. / Álvarez, B. (2021). Bibliotecas hoy. Libro. ¿Cuál va primero en orden alfabético?", "Álvarez", "A precede a P en el alfabeto."),
    E("¿Qué debe coincidir entre el texto y la lista de referencias?", "Cada fuente citada debe aparecer en la lista", "Así el lector puede comprobarla.")],
   [E(f"{FH} Escribe la cita en el texto de la tabla del formato: institución «Biblioteca Vecinal» y año 2024.", "(Biblioteca Vecinal, 2024)", "Incluye el nombre y el año entre paréntesis."),
    E("Ordena alfabéticamente: Soto, P. / Araya, L. / Muñoz, R. Escribe los apellidos en orden.", "Araya, Muñoz, Soto", "Es el orden alfabético."),
    arith("Una lista de verificación tiene 7 preguntas y tu texto cumple 5. ¿Cuántas faltan por cumplir?", "7-5", "Se resta lo cumplido al total.", " preguntas")],
   [E("Un estudiante cita (Torres, 2023) en el texto pero su lista no tiene a Torres. ¿Qué error hay?", "Citó una fuente que no está en las referencias", "Falta la referencia."),
    E("Un informe termina con «Estoy seguro de que todos deben ir». ¿Qué problema tiene el cierre?", "Introduce una opinión que el texto no preparó", "Un texto explicativo no persuade sin argumentos.")],
   [E("Cierre mejor para un texto que explicó cómo funciona el préstamo: (a) En síntesis, para pedir un libro solo hay que inscribirse, elegir y devolverlo en el plazo. (b) Hay muchas bibliotecas en el mundo. (c) La biblioteca es lo mejor.", "(a)", "Sintetiza los pasos explicados."),
    E("Lista de referencias: Soto, P. (2020) / Soto, M. (2022) / Araya, L. (2021). ¿Cuál es el orden alfabético correcto?", "Araya, L.; Soto, M.; Soto, P.", "Se ordena por apellido y, si coincide, por la inicial.")]),
  [E("Terminaste un texto sobre el reciclaje del colegio. Usaste una entrevista a Ana Rojas (2024) y una tabla de la dirección (2024). ¿Qué debes agregar al final?", "Una lista de referencias con las dos fuentes", "Cada fuente citada debe aparecer allí.")],
  [E("¿Qué lleva la lista de referencias?", "Las fuentes citadas, en orden alfabético y con el formato acordado", "Permite ubicar cada fuente."),
   E("¿Un cierre puede sintetizar y proyectar?", "Sí", "Son dos modos de cerrar."),
   E("¿Qué se revisa antes de entregar?", "La lista de verificación del texto explicativo", "Resume los criterios.")],
  ("Termina este texto de ejemplo con un cierre de dos o tres líneas y una lista de referencias en el formato acordado. Texto: «La biblioteca vecinal nació en 2019 y hoy tiene 1.800 libros (Lillo, 2024). Sus socios pasaron de 90 a 260 entre 2020 y 2023 (Biblioteca Vecinal, 2024).» Datos de las fuentes: Lillo, M., entrevista de 2024; Biblioteca Vecinal (de ejemplo), tabla «Socios por año», 2024.",
   "Cierre: En síntesis, la biblioteca creció en libros y en socios desde 2019. Falta observar si mantendrá ese ritmo. Referencias: Biblioteca Vecinal (de ejemplo). (2024). Socios por año. Tabla. / Lillo, M. (2024). Entrevista sobre la biblioteca vecinal. Entrevista.",
   ["cierre sin información nueva", "referencias en el formato", "orden alfabético"], ["cierre y lista"],
   ["agregar datos nuevos en el cierre", "desordenar las referencias"], "Revisa con alguien que cada cita del texto tenga su referencia."),
  "Escribe un cierre de una línea para un texto sobre tu barrio.",
  "Ordena una lista de seis referencias inventadas.")
