"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 12 (biblioteca) y OA 13 (escritura emergente)."""
from __future__ import annotations

from student_lessons import ex, register

OA12, OA13 = "LE01 OA 12", "LE01 OA 13"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ======================================================================== OA 12
lesson(
    OA12, 1,
    "Cuaderno y lápiz. Los acuerdos y las situaciones están escritos en los ejercicios; si quieres practicar, usa un estante de libros de tu casa.",
    "Aprenderé los acuerdos para usar bien una biblioteca. Sirve para que todos podamos leer, escuchar y cuidar los libros.",
    ["Sé qué es un libro.", "Sé esperar mi turno."],
    [
        "La biblioteca es un lugar con muchos libros para leer, escuchar y mirar. Para que todos lo pasemos bien hay acuerdos: hablamos en voz baja, caminamos sin correr, tenemos las manos limpias y tratamos los libros con cuidado.",
        "Cuando sacas un libro, lo pones de nuevo en su lugar para que otros lo encuentren. Si quieres otro, esperas tu turno con la persona que atiende. Si un libro se rompe, avisas a un adulto y no lo escondes.",
        "Los acuerdos no son castigos. Son formas de cuidarnos y de cuidar los libros. Cuando todos los cumplen, la biblioteca es un lugar tranquilo donde se puede disfrutar de la lectura.",
    ],
    [("biblioteca", "lugar con muchos libros para leer y pedir prestados"), ("acuerdo", "regla que todos cumplimos"), ("voz baja", "hablar despacio para no molestar"), ("cuidar", "tratar bien algo para que no se dañe"), ("su lugar", "el estante donde vive cada libro")],
    [
        ("Elegir un acuerdo", "Pablo entra corriendo a la biblioteca. ¿Qué acuerdo no cumple?", ["En la biblioteca se camina.", "Correr puede chocar con otros."], "No cumple el acuerdo de caminar sin correr"),
        ("Dejar el libro", "Ana terminó de mirar un libro. ¿Qué debe hacer?", ["Los libros tienen su lugar.", "Otros lo buscarán ahí."], "Ponerlo de nuevo en su lugar"),
    ],
    [
        ("Hablar fuerte porque a mí me gusta contar.", "Se olvida que otros leen.", "Habla en voz baja."),
        ("Dejar el libro en cualquier parte.", "Se cree que no importa.", "Ponlo en su lugar."),
    ],
    [
        E("¿Cómo se habla en la biblioteca? A) en voz baja B) a gritos", "A) en voz baja", "Así no se molesta a los que leen."),
        E("¿Cómo se camina en la biblioteca?", "Caminando, sin correr", "Se evita chocar y hacer ruido."),
        E("Antes de tomar un libro, ¿cómo deben estar las manos?", "Limpias", "Así no se ensucian las páginas."),
    ],
    [
        E("Lee: «Nico dobló una página para marcar dónde iba». ¿Cuidó bien el libro?", "No", "Doblar la hoja la daña."),
        E("Lee: «Eva usó un papel para marcar y cerró el libro con cuidado». ¿Cuidó bien el libro?", "Sí", "Usó un marcador y no dañó el libro."),
        E("Un libro se rompió sin querer. ¿Qué debes hacer?", "Avisar a un adulto", "Así se puede arreglar."),
    ],
    [
        E("Lee: «Hay una fila para pedir libros. Luis se pone adelante sin esperar». ¿Qué acuerdo no cumple?", "Esperar su turno", "Todos deben esperar en la fila."),
        E("Ana ve a un niño que come un helado cerca de los libros. ¿Qué acuerdo puede recordarle?", "Mantener los libros limpios", "Un helado puede ensuciar las páginas."),
        E("Escribe un acuerdo de la biblioteca con la palabra «cuidar».", "Por ejemplo: Hay que cuidar los libros", "Debe ser un acuerdo y usar la palabra."),
    ],
    [
        E("Camila dice: «Los acuerdos son para castigar». Su profesora responde que no. ¿Para qué sirven?", "Para cuidar a todos y a los libros", "Permiten que todos lean tranquilos."),
        E("Si todos hablaran fuerte en la biblioteca, ¿qué pasaría?", "No se podría leer tranquilo", "El ruido molesta a los lectores."),
    ],
    [
        E("Ordena: a) Poner el libro en su lugar. b) Leer el libro. c) Tomar el libro del estante. Escribe las letras.", "c, b, a", "Primero se toma, luego se lee y al final se devuelve al estante."),
        E("Hay 3 acuerdos en el cartel: voz baja, caminar, manos limpias. Pablo cumple 2. ¿Cuántos le faltan?", "1", "3 menos 2 es 1."),
    ],
    [E("Una niña llega a la biblioteca con la mochila abierta y deja caer sus lápices al piso con ruido. ¿Qué debe hacer?", "Recoger los lápices con cuidado y ser más silenciosa", "Así cuida el ambiente de la biblioteca.")],
    [
        E("En Lenguaje, ¿qué es un acuerdo?", "Una regla que todos cumplimos", "Ayuda a convivir bien."),
        E("¿Dónde se pone un libro después de usarlo?", "En su lugar", "Así otros lo encuentran."),
        E("¿Cómo se habla en la biblioteca?", "En voz baja", "Para no molestar."),
    ],
    task(
        "Elige tres acuerdos de esta lista y haz un cartel dibujado con una frase para cada uno: voz baja, caminar sin correr, manos limpias, devolver el libro a su lugar, esperar el turno. Usa «Debo...» en cada frase.",
        "Debo hablar en voz baja. Debo caminar sin correr. Debo tener las manos limpias.",
        ["tres acuerdos de la lista", "cada frase empieza con «Debo»", "las frases se entienden"],
        ["cartel con tres frases", "lectura en voz alta"],
        ["escribir acuerdos que no están en la lista sin sentido", "dos acuerdos en vez de tres"],
        "Lee tu cartel a otra persona y pregúntale si entiende cada acuerdo.",
    ),
    "Di en voz alta tres acuerdos de la biblioteca.",
    "Dibuja un cartel para un rincón de lectura de tu casa.",
)

ESTANTES = "Estantes: ANIMALES (perros, pájaros, peces), CUENTOS (hadas, dragones), POEMAS (rimas), DEPORTES (fútbol, natación), COCINA (recetas), ESPACIO (planetas, estrellas)."

lesson(
    OA12, 2,
    "Cuaderno y lápiz. El plano de los estantes de la biblioteca está escrito en los ejercicios.",
    "Aprenderé a buscar un libro según lo que me interesa mirando los carteles de los estantes. Sirve para encontrar libros que me gusten.",
    ["Sé leer palabras como animales y cuentos.", "Sé qué me gusta."],
    [
        "En la biblioteca los libros están ordenados por temas. Cada estante tiene un cartel que dice de qué tratan los libros que contiene. Así no tienes que mirar todos: vas directo al estante que te interesa.",
        "Para encontrar tu libro, primero piensa qué quieres: ¿animales?, ¿cuentos de aventuras?, ¿poemas? Luego busca el cartel que lo nombra. Si no lo ves, puedes preguntar a la persona que atiende.",
        "Cuando llegues al estante, mira los títulos y las portadas. Saca un libro, hójealo y decide si es el que buscabas. Si no te gusta, lo dejas de nuevo en su lugar y pruebas otro.",
    ],
    [("estante", "tabla donde se guardan los libros"), ("tema", "de qué trata un libro"), ("cartel", "papel con letras que indica algo"), ("interés", "lo que quiero saber o leer"), ("buscar", "ir a ver dónde está algo")],
    [
        ("Buscar un tema", f"{ESTANTES} Quieres un libro de pájaros. ¿A qué estante vas?", ["Los pájaros son animales.", "El cartel ANIMALES nombra pájaros."], "Al estante ANIMALES"),
        ("Otro interés", f"{ESTANTES} Quieres aprender a hacer una ensalada. ¿A qué estante vas?", ["Una ensalada se prepara con una receta.", "Las recetas están en COCINA."], "Al estante COCINA"),
    ],
    [
        ("Buscar sin pensar qué quiero.", "Se mira todo al azar.", "Primero piensa tu interés."),
        ("Dejar el libro en otro estante.", "Se cree que da lo mismo.", "Devuélvelo al estante donde estaba."),
    ],
    [
        E(f"{ESTANTES} Quieres un libro de dragones. ¿A qué estante vas?", "CUENTOS", "Los dragones aparecen en cuentos."),
        E(f"{ESTANTES} Quieres leer sobre planetas. ¿A qué estante vas?", "ESPACIO", "Los planetas están en el espacio."),
        E(f"{ESTANTES} Quieres un libro con rimas. ¿A qué estante vas?", "POEMAS", "Los poemas tienen rimas."),
    ],
    [
        E(f"{ESTANTES} ¿Cuántos estantes hay?", "6", "Se cuentan seis carteles."),
        E(f"{ESTANTES} ¿En qué estante hay libros de fútbol?", "DEPORTES", "El cartel nombra fútbol."),
        E("¿Para qué sirven los carteles de los estantes?", "Para encontrar libros por tema", "Dicen de qué tratan los libros."),
    ],
    [
        E(f"{ESTANTES} A Mía le encantan los peces. ¿A qué estante va?", "ANIMALES", "Los peces son animales."),
        E(f"{ESTANTES} A Tomás le gusta la natación. ¿A qué estante va?", "DEPORTES", "La natación es un deporte."),
        E(f"{ESTANTES} A Rosa le gustan las estrellas. ¿A qué estante va?", "ESPACIO", "Las estrellas están en el espacio."),
    ],
    [
        E(f"{ESTANTES} Un niño busca un libro de hadas en COCINA. ¿Lo encontrará ahí? Responde sí o no.", "No", "Las hadas están en CUENTOS."),
        E("Luis no encuentra el estante que quiere. ¿Qué puede hacer? A) preguntar a la persona que atiende B) irse sin hacer nada", "A) preguntar a la persona que atiende", "Puede ayudarlo a buscar."),
    ],
    [
        E(f"{ESTANTES} Quieres un libro que te enseñe a tirar un penal y que tenga imágenes de jugadores. ¿Qué estante eliges?", "DEPORTES", "El fútbol es un deporte."),
        E("Escribe un cartel nuevo con una palabra para un estante de libros sobre plantas y flores.", "Por ejemplo: PLANTAS", "Debe nombrar el tema."),
    ],
    [E("Eva visita la biblioteca. Quiere un libro de recetas para cocinar con su abuela y otro de un cuento de dragones. Estantes: " + ESTANTES + " ¿A cuáles va?", "A COCINA y a CUENTOS", "Cada interés tiene su estante.")],
    [
        E("¿Cómo están ordenados los libros en la biblioteca?", "Por temas", "Cada estante tiene un tema."),
        E("Si quieres un libro de perros, ¿a qué estante vas? ANIMALES o COCINA", "ANIMALES", "Los perros son animales."),
        E("¿Qué haces si no ves el cartel que buscas?", "Pregunto a la persona que atiende", "Puede indicar dónde está."),
    ],
    task(
        "Escribe tres intereses tuyos y el estante donde los buscarías, usando esta lista: ANIMALES, CUENTOS, POEMAS, DEPORTES, COCINA, ESPACIO. Usa «Me interesa... Lo busco en...».",
        "Me interesa el fútbol. Lo busco en DEPORTES. Me interesan las recetas. Las busco en COCINA. Me interesan los planetas. Los busco en ESPACIO.",
        ["tres intereses", "cada uno con un estante de la lista", "usa las frases pedidas"],
        ["tres pares de oraciones", "explicación oral"],
        ["usar un estante que no existe", "no relacionar interés y estante"],
        "Relee la lista de estantes y comprueba que cada tema esté en el estante que dijiste.",
    ),
    "Mira los libros de tu casa y di a qué estante irían.",
    "Haz un cartel para un estante de tu casa con una palabra y un dibujo.",
)

lesson(
    OA12, 3,
    "Cuaderno y lápiz. Los fragmentos y la regla de los dedos están escritos en los ejercicios.",
    "Aprenderé a elegir un libro que pueda leer yo o con ayuda. Sirve para escoger libros que disfrute y entienda.",
    ["Sé leer frases cortas.", "Sé contar hasta 5."],
    [
        "No todos los libros son iguales de fáciles. Para saber si un libro es posible para ti, lee una página y cuenta cuántas palabras no sabes leer o no entiendes. Marca con un dedo cada palabra difícil.",
        "Si encuentras 0 o 1 palabras difíciles, el libro es muy fácil: puedes leerlo solo. Si hay 2 o 3, es adecuado: te desafía un poco. Si hay 4 o 5 o más, es difícil: pídele a alguien que te lo lea o déjalo para más adelante.",
        "Elegir un libro también depende de lo que te gusta. Un libro puede ser fácil, pero si no te interesa, no lo disfrutarás. Lo mejor es un libro que puedas entender y que te llame la atención.",
    ],
    [("palabra difícil", "palabra que no sé leer o no entiendo"), ("adecuado", "que es apropiado para mí"), ("desafío", "algo un poco difícil que me hace aprender"), ("muy fácil", "libro que leo sin dificultad"), ("ayuda", "apoyo de un adulto")],
    [
        ("Contar dedos", "Lees una página y levantas 3 dedos por palabras difíciles. ¿Es muy fácil, adecuado o difícil?", ["3 está entre 2 y 3.", "Es un desafío posible."], "Es adecuado"),
        ("Pedir ayuda", "En una página levantas 5 dedos. ¿Qué haces?", ["5 es mucho.", "Pido que me lo lean o lo dejo para más adelante."], "Pido ayuda o lo dejo para más adelante"),
    ],
    [
        ("Elegir un libro porque es más gordo.", "Se cree que más páginas es mejor.", "Cuenta las palabras difíciles de una página."),
        ("Elegir siempre libros muy fáciles.", "Se quiere evitar el esfuerzo.", "Prueba también libros adecuados."),
    ],
    [
        E("Levantaste 1 dedo en una página. ¿Es muy fácil, adecuado o difícil?", "Muy fácil", "Una palabra difícil es poca."),
        E("Levantaste 2 dedos en una página. ¿Es muy fácil, adecuado o difícil?", "Adecuado", "Dos palabras difíciles es un desafío posible."),
        E("Levantaste 5 dedos en una página. ¿Es muy fácil, adecuado o difícil?", "Difícil", "Cinco palabras difíciles son demasiadas."),
    ],
    [
        E("Una página tiene 4 palabras difíciles para Ana. ¿Cuántos dedos levanta?", "4", "Un dedo por cada palabra."),
        E("¿Qué se hace con un libro difícil? A) Se pide ayuda a un adulto B) Se rompe", "A) Se pide ayuda a un adulto", "Así se puede disfrutar igual."),
        E("¿Qué es un libro adecuado?", "El que puedo leer con un poco de esfuerzo", "Tiene pocas palabras difíciles."),
    ],
    [
        E("Lee: «El perro corre en el patio». Si sabes todas las palabras, ¿cuántos dedos levantas?", "0", "No hay palabras difíciles."),
        E("Lee la frase: «Mi gato duerme sobre la manta». Si no sabes «manta», ¿cuántos dedos levantas?", "1", "Sólo una palabra es difícil."),
        E("Camila levantó 2 dedos en un libro de animales que le gusta mucho. ¿Lo elige? Responde sí o no.", "Sí", "Es adecuado y además le interesa."),
    ],
    [
        E("Nico elige un libro sólo porque es el más grande de la estantería. ¿Es una buena razón? Responde sí o no.", "No", "El tamaño no dice si puedo leerlo."),
        E("Un niño levantó 3 dedos y dijo «No puedo, es muy difícil». ¿Tiene razón?", "No; es adecuado", "Con 2 o 3 palabras difíciles se puede leer."),
    ],
    [
        E("Dos libros: A) 1 dedo, tema aburrido para Luisa. B) 3 dedos, tema que le encanta. Si Luisa quiere disfrutarlo y aprender, ¿cuál elige?", "B", "Es adecuado y le interesa."),
        E("Una página tiene 20 palabras. Pedro levantó 5 dedos por palabras difíciles. ¿Cuántas palabras entendió?", "15", "20 menos 5 es 15."),
    ],
    [E("En la biblioteca Beto toma «Los planetas». Lee la primera página y levanta 4 dedos. Le pide a un adulto que se lo lea. ¿Hizo bien?", "Sí", "Pidió ayuda porque era difícil.")],
    [
        E("Si levantas 0 o 1 dedo, ¿cómo es el libro?", "Muy fácil", "Casi no tiene palabras difíciles."),
        E("¿Qué haces si un libro tiene 5 palabras difíciles en una página?", "Pido que me lo lean", "Es difícil para leer solo."),
        E("¿Qué debe tener un buen libro para elegir además de ser posible?", "Un tema que me guste", "Así lo disfrutaré."),
    ],
    task(
        "Prueba esta página: «Mi perro se llama Bruno. Es grande y negro. Le gusta correr por el parque.» Cuenta las palabras que no sabes leer o entender (cuenta 0 si las sabes todas) y escribe si el libro sería muy fácil, adecuado o difícil para ti, con una razón.",
        "Conté 0 palabras difíciles, así que es muy fácil para mí porque entendí todo.",
        ["dice cuántas palabras difíciles contó", "dice si es fácil, adecuado o difícil", "da una razón"],
        ["oración escrita", "respuesta oral"],
        ["no contar", "no dar razón", "decir algo que no coincide con el número"],
        "Vuelve a leer la página y marca cada palabra difícil con el dedo antes de contarlas.",
    ),
    "Lee una página de un libro de tu casa y cuenta tus dedos.",
    "Elige un libro de un nivel difícil y pide a un adulto que te lo lea.",
)

lesson(
    OA12, 4,
    "Cuaderno y lápiz. El guion que lee el adulto y las preguntas están escritos en los ejercicios.",
    "Aprenderé a escuchar un cuento en la biblioteca y a conversar sobre él. Sirve para disfrutar de lo que otros leen y entender mejor.",
    ["Sé escuchar sin interrumpir.", "Sé hacer preguntas."],
    [
        "En la biblioteca a veces un adulto lee en voz alta. Para escuchar bien, te sientas cómodo, miras a quien lee y guardas silencio. Si tienes una duda, la anotas o la dices al final.",
        "Después de escuchar, conversamos. Cada uno cuenta qué le gustó, qué entendió o qué pregunta tiene. Se habla por turnos y se escucha con respeto lo que dicen los demás.",
        "Una buena conversación tiene tres partes: escuchar, pensar y hablar. Primero escuchas la historia, luego piensas qué te pareció y después lo cuentas con tus palabras.",
    ],
    [("escuchar", "poner atención a lo que se dice"), ("turno", "momento en que me toca hablar"), ("conversar", "hablar y escuchar entre varios"), ("duda", "algo que no entendí"), ("respeto", "tratar bien lo que dicen los demás")],
    [
        ("Escuchar", "Un adulto lee: «Una vez, una hormiga encontró una migaja de pan. La llevó a su casa con sus amigas.» ¿Qué encontró la hormiga?", ["Escucho con atención.", "La migaja de pan."], "Una migaja de pan"),
        ("Conversar", "Después de la historia, Ana dice qué le gustó. ¿Qué hacen los demás?", ["Esperan su turno.", "La escuchan sin interrumpir."], "La escuchan y esperan su turno"),
    ],
    [
        ("Hablar mientras el adulto lee.", "Se tiene ganas de comentar.", "Guarda tu comentario para el final."),
        ("Contar algo que no tiene que ver con la historia.", "Se pierde el hilo.", "Habla de lo que escuchaste."),
    ],
    [
        E("Un adulto lee: «Una hormiga encontró una migaja de pan y la llevó a su casa.» ¿Qué hizo la hormiga?", "Llevó la migaja a su casa", "El texto lo cuenta."),
        E("¿Cómo escuchas bien a quien lee? A) Miro a quien lee B) Hablo con mi vecino", "A) Miro a quien lee", "Se escucha con atención."),
        E("¿Qué haces si tienes una duda mientras alguien lee?", "La anoto o la digo al final", "Así no se interrumpe."),
    ],
    [
        E("Escuchaste el cuento de la hormiga. ¿Quién es el personaje?", "La hormiga", "Es quien hace la acción."),
        E("¿Cuándo se comenta lo que escuchamos?", "Al final de la lectura", "Primero se escucha todo."),
        E("¿Cuál es el turno de hablar? Cuando A) yo quiero B) me toca", "B) me toca", "Se espera el turno."),
    ],
    [
        E("Un adulto lee: «El viento sopló y el sombrero de Beto voló por el aire.» ¿Qué se llevó el viento?", "El sombrero de Beto", "El texto lo dice."),
        E("Escribe una pregunta que puedes hacer después de escuchar el cuento de la hormiga.", "Por ejemplo: ¿Dónde vive la hormiga?", "Debe ser una pregunta sobre el cuento."),
        E("Completa: «Me gustó la parte en que...», para el cuento de la hormiga.", "Por ejemplo: la hormiga llevó la migaja a su casa", "Debe nombrar una parte del cuento."),
    ],
    [
        E("Dos niños: Eva escucha en silencio y Pablo interrumpe con otros temas. ¿Quién escucha mejor?", "Eva", "Respeta la lectura."),
        E("Un niño dice «No me gustó» y no explica nada. ¿Cómo podría mejorar su comentario?", "Diciendo por qué no le gustó", "Una razón ayuda a entender su opinión."),
    ],
    [
        E("Un adulto lee «La hormiga y la migaja» en dos partes. En la primera, la hormiga encuentra la migaja. En la segunda, la lleva a su casa. ¿En cuántas partes se divide?", "2", "Hay dos partes."),
        E("Nico tiene que compartir qué le gustó. Hay 3 niños antes que él. ¿En qué lugar habla?", "En cuarto lugar", "Después de tres viene el cuarto."),
    ],
    [E("En la hora del cuento la bibliotecaria lee y Mía quiere contar su historia en ese momento. ¿Qué le conviene hacer?", "Esperar al final para comentar", "Así se respeta la lectura de todos.")],
    [
        E("¿Qué se hace primero en una conversación de lectura?", "Escuchar", "Primero hay que entender la historia."),
        E("En la hora del cuento de la biblioteca, ¿qué es un turno?", "El momento en que me toca hablar", "Se habla de uno en uno."),
        E("¿Cómo se comenta con respeto?", "Escuchando y hablando por turnos", "No se interrumpe a los demás."),
    ],
    task(
        "Pide a un adulto que lea este cuento de dos oraciones: «Un caracol salió de su casa después de la lluvia. Subió despacito por una hoja verde.» Luego, cuéntale en una oración qué te gustó y en otra una pregunta que tengas. Pauta de oralidad: espero mi turno, miro a quien habla y hablo con voz clara.",
        "Me gustó que el caracol subió por la hoja verde. ¿Por qué salió después de la lluvia?",
        ["cuenta qué le gustó", "hace una pregunta sobre el cuento", "espera su turno y habla claro"],
        ["conversación con un adulto", "registro escrito de la pregunta"],
        ["no relacionar lo dicho con el cuento", "interrumpir mientras se lee"],
        "Pide al adulto que diga qué parte de tu comentario entendió mejor.",
    ),
    "Escucha un cuento corto y cuéntalo con tus palabras.",
    "Anota dos preguntas sobre un cuento que escuches en esta semana.",
)

lesson(
    OA12, 5,
    "Cuaderno y lápiz. La ficha de préstamo y el calendario de ejemplo están en los ejercicios.",
    "Aprenderé cómo se pide un libro prestado, cómo se cuida y cuándo se devuelve. Sirve para usar la biblioteca con responsabilidad.",
    ["Sé contar hasta 20.", "Sé que debo cuidar los libros."],
    [
        "En la biblioteca puedes pedir libros prestados para leer en casa. La persona que atiende anota tu nombre, el libro y la fecha en que debes devolverlo. Esa fecha es una promesa: tienes que cumplirla.",
        "Mientras el libro está en casa debes cuidarlo: guárdalo en la mochila, lejos de líquidos, sin rayarlo ni doblar sus hojas. Si lo dejas en el suelo o lo mojas, puede dañarse.",
        "Al devolverlo, lo entregas a la persona que atiende. Así queda disponible para otros lectores. Si no puedes devolverlo a tiempo, avisa a un adulto para pedir más tiempo.",
    ],
    [("préstamo", "llevar un libro a casa por unos días"), ("devolver", "traer de vuelta el libro"), ("fecha", "el día en que debo devolverlo"), ("responsabilidad", "cumplir lo que prometí"), ("disponible", "que otro puede usar")],
    [
        ("Calcular la fecha", "Retiras un libro el día 4 y debes devolverlo en 7 días. ¿Qué día lo devuelves?", ["Sumo 7 días a 4.", "4 + 7 = 11."], "El día 11"),
        ("Cuidar el libro", "Tienes un libro prestado y quieres comer. ¿Qué haces?", ["Los líquidos y migas pueden dañarlo.", "Lo guardo antes de comer."], "Lo guardo lejos de la comida"),
    ],
    [
        ("Quedarse con el libro más tiempo.", "Se olvida la fecha.", "Anota la fecha y devuélvelo ese día."),
        ("Dejar el libro en el suelo.", "Se cree que no pasa nada.", "Guárdalo en la mochila o en un estante."),
    ],
    [
        E("¿Qué se anota cuando prestan un libro? A) nombre, libro y fecha B) sólo el color", "A) nombre, libro y fecha", "Así se sabe quién lo tiene y cuándo vuelve."),
        E("¿Dónde guardas el libro prestado para llevarlo a casa?", "En la mochila", "Así se protege."),
        E("¿Qué debes hacer con el libro en la fecha de devolución?", "Devolverlo", "Es la promesa del préstamo."),
    ],
    [
        E("Lee: «Pedro derramó jugo sobre el libro prestado». ¿Cuidó bien el libro?", "No", "El jugo puede dañar las hojas."),
        E("Lee: «Eva guardó el libro en un estante alto lejos de su hermano pequeño». ¿Lo cuidó bien?", "Sí", "Lo protegió de daños."),
        E("¿Qué haces si no puedes devolver el libro a tiempo?", "Aviso a un adulto para pedir más tiempo", "Hay que avisar y no esconderlo."),
    ],
    [
        E("Retiras un libro el día 3 y debes devolverlo 7 días después. ¿Qué día lo devuelves?", "El día 10", "3 más 7 es 10."),
        E("Retiras un libro el día 12 y debes devolverlo 7 días después. ¿Qué día lo devuelves?", "El día 19", "12 más 7 es 19."),
        E("Retiras dos libros el día 5. Debes devolver uno el día 12 y el otro el día 19. ¿Cuántos días de diferencia hay entre las dos fechas?", "7", "19 menos 12 es 7."),
    ],
    [
        E("Rosa dice: «Me quedo el libro porque me gusta mucho». ¿Es una buena razón? Responde sí o no.", "No", "Otros lectores también lo necesitan."),
        E("¿Por qué es importante devolver el libro en la fecha?", "Para que otros lectores puedan leerlo", "Así queda disponible."),
    ],
    [
        E("Ficha de préstamo: Nombre: Tomás. Libro: «El oso y la luna». Retiro: día 8. Devolución: día 15. ¿Cuántos días tiene para leer el libro?", "7", "15 menos 8 es 7."),
        E("Ordena: a) Entrego el libro. b) Leo el libro en casa. c) Pido el libro prestado. Escribe las letras en orden.", "c, b, a", "Primero se pide, luego se lee y al final se devuelve."),
    ],
    [E("Una niña pidió el libro «Los planetas» el día 2 con devolución a los 7 días. En casa lo dejó afuera y lo mojó la lluvia. ¿Qué debió hacer? Elige: A) guardarlo B) mojarlo", "A) guardarlo", "Debía protegerlo de la lluvia.")],
    [
        E("¿Qué es la fecha de devolución?", "El día en que debo traer el libro", "Es el plazo del préstamo."),
        E("¿Qué hago con el libro cuando lo termino de leer en casa?", "Lo guardo bien hasta devolverlo", "Se cuida hasta entregarlo."),
        E("¿Para qué sirve devolver a tiempo?", "Para que otros lo lean", "Lo comparte la comunidad."),
    ],
    task(
        "Completa esta ficha de préstamo con un libro real o con «El oso y la luna»: Libro; Retiro: día 6; Devolución: 7 días después (escribe qué día es); Un cuidado que prometes tener (por ejemplo, guardarlo en la mochila).",
        "Libro: El oso y la luna. Retiro: día 6. Devolución: día 13. Prometo guardarlo en la mochila.",
        ["escribe el libro", "la fecha de devolución es 13", "promete un cuidado"],
        ["ficha escrita", "lectura en voz alta"],
        ["calcular mal la fecha", "no prometer cuidado"],
        "Cuenta 7 días desde el 6 con el dedo para comprobar la fecha.",
    ),
    "Cuenta tres formas de cuidar un libro prestado.",
    "Haz tu propia tarjeta de préstamo con nombre, libro, retiro y devolución.",
)

# ======================================================================== OA 13
lesson(
    OA13, 1,
    "Cuaderno, lápiz y una hoja. Las palabras y las frases están escritas en los ejercicios; se aceptan escrituras como «mama» para «mamá», porque estás aprendiendo.",
    "Aprenderé que lo que escribo queda guardado y otros lo pueden leer después. Sirve para comunicar lo que pienso, aunque todavía esté aprendiendo a escribir.",
    ["Sé algunas letras.", "Sé decir lo que quiero comunicar."],
    [
        "Cuando hablas, las palabras se van. Cuando escribes, tus palabras quedan guardadas y otra persona puede leerlas más tarde. Por eso escribir sirve para recordar y para comunicar a quien no está contigo.",
        "Puedes escribir una palabra, como «sol», o una frase, como «Me gusta el sol». No importa si algunas letras todavía te cuestan: primero se escribe lo que se quiere decir y se usan las letras que conoces. Con la práctica se escriben cada vez mejor.",
        "Cuando termines, lee en voz alta lo que escribiste. Si lo que lees dice lo que querías decir, tu escritura funciona. Después puedes mejorar las letras o agregar más palabras.",
    ],
    [("escribir", "dejar mis ideas con letras"), ("comunicar", "hacer que otro entienda lo que quiero decir"), ("palabra", "letras juntas que significan algo"), ("frase", "palabras que dicen una idea"), ("leer", "decir en voz alta lo que está escrito")],
    [
        ("Escribir una palabra", "Quieres escribir el nombre de tu sol favorito: «sol». ¿Con qué letras empieza?", ["Digo la palabra despacio: s-o-l.", "Empieza con la s."], "Con la letra s"),
        ("Escribir una frase", "Quieres decir que te gusta el sol. ¿Qué escribes?", ["Digo qué quiero decir.", "Escribo: Me gusta el sol."], "Me gusta el sol"),
    ],
    [
        ("Pensar que sólo vale la escritura perfecta.", "Se tiene miedo a equivocarse.", "Escribe lo que quieres decir y mejora después."),
        ("Escribir sin releer.", "Se termina rápido.", "Lee en voz alta para comprobar."),
    ],
    [
        E("¿Qué sucede con lo que escribes? A) Queda guardado B) Se va como el aire", "A) Queda guardado", "La escritura permanece."),
        E("Escribe la palabra «sol». ¿Con qué letra termina?", "l", "La palabra sol termina con l."),
        E("¿Para qué sirve escribir?", "Para comunicar y recordar", "Otros pueden leerlo después."),
    ],
    [
        E("Quieres decirle a tu mamá «te quiero». ¿Cuántas palabras son?", "2", "Son «te» y «quiero»."),
        E("Escribe con tus letras lo que dice el dibujo de un gato: ¿qué animal es? (Escribe «gato»).", "gato", "La palabra es gato."),
        E("Una niña escribió «mama» en vez de «mamá». ¿Se entiende lo que quiso decir?", "Sí", "Se entiende y puede mejorar después."),
    ],
    [
        E("Mira estas palabras: sol, luna, flor. Escribe la que empieza con f.", "flor", "Es la única que empieza con la letra f."),
        E("Escribe una frase de dos palabras que diga a quién quieres, por ejemplo «Quiero a...».", "Por ejemplo: Quiero a mamá", "Debe decir a quién quiere."),
        E("Escribe un saludo para una persona: «Hola, ...» agregando su nombre inventado.", "Por ejemplo: Hola, Ana", "Debe empezar con «Hola»."),
    ],
    [
        E("Tomás dice: «No sé escribir bien, mejor no escribo». ¿Qué le dirías?", "Que escriba lo que quiere decir y mejore después", "Se aprende escribiendo."),
        E("Dos mensajes: «mi gato duerme» y «mi gto duerme». ¿Se entienden los dos? Responde sí o no.", "Sí", "Aunque falte una letra, se puede leer."),
    ],
    [
        E("Quieres escribir tres cosas que te gustan. ¿Cuántas palabras escribes como mínimo?", "3", "Una por cada cosa."),
        E("Escribe una frase que diga qué hay en tu mesa (por ejemplo, «Hay un vaso»).", "Por ejemplo: Hay un vaso", "Debe nombrar algo que hay."),
    ],
    [E("Mamá no llegó aún y te pide que le dejes un mensaje para saber que hiciste la tarea. Escribe un mensaje breve: «Mamá, hice la tarea».", "Mamá, hice la tarea", "Es un mensaje breve y claro.")],
    [
        E("¿Qué es escribir?", "Dejar mis ideas con letras", "Así otros las pueden leer."),
        E("¿Qué se hace al terminar de escribir?", "Se lee en voz alta", "Así se comprueba que dice lo que quiero."),
        E("¿Tiene que ser perfecta la primera escritura? Responde sí o no.", "No", "Se mejora con la práctica."),
    ],
    task(
        "Escribe tres frases con las palabras de este cuadro: «mamá, sol, gato, casa, flor». Cada frase debe usar una palabra distinta. Ejemplo: «Mi gato duerme».",
        "Mi mamá canta. El sol brilla. La flor es roja.",
        ["tres frases", "cada una usa una palabra del cuadro", "se entienden aunque tengan errores de letras"],
        ["tres frases en el cuaderno", "lectura en voz alta"],
        ["escribir sólo palabras sueltas", "repetir la misma palabra"],
        "Lee tus frases a un adulto y ayúdale a decir qué letra falta si no se entienden.",
    ),
    "Escribe tu nombre y el de dos personas que quieres.",
    "Escribe cinco palabras que veas en tu casa.",
)

lesson(
    OA13, 2,
    "Cuaderno y lápiz. Los hechos y las ideas están escritos en los ejercicios.",
    "Aprenderé a escribir un hecho, es decir, algo que pasó, en el orden en que ocurrió. Sirve para contar lo que hice o lo que vi.",
    ["Sé escribir frases cortas.", "Sé decir qué hice hoy."],
    [
        "Un hecho es algo que realmente pasó. «Hoy fui a la plaza» es un hecho. Para contar un hecho, escribe qué pasó, quién lo hizo y dónde. Puedes usar palabras como «primero», «luego» y «al final» para ordenar.",
        "No es lo mismo un hecho que una idea. Un hecho se puede comprobar: sucedió o no sucedió. «Los perros son los mejores» es una idea, porque cada persona puede pensar distinto.",
        "Cuando cuentes un hecho, usa el orden en que ocurrió. Si primero te levantaste y luego desayunaste, escribe primero eso. Si lo cuentas desordenado, el lector se confunde.",
    ],
    [("hecho", "algo que realmente pasó"), ("idea", "lo que pienso"), ("orden", "primero, luego y al final"), ("primero", "lo que ocurrió antes"), ("al final", "lo último que pasó")],
    [
        ("Hecho o idea", "«Ayer fui a la plaza con mi hermano». ¿Hecho o idea?", ["Se puede comprobar si ocurrió.", "Pasó ayer."], "Es un hecho"),
        ("Ordenar", "Primero me levanté. Luego desayuné. Al final fui al colegio. ¿Qué hice primero?", ["Busco la palabra primero.", "Dice: me levanté."], "Me levanté"),
    ],
    [
        ("Contar los hechos desordenados.", "Se escribe lo que se recuerda primero.", "Usa primero, luego y al final."),
        ("Mezclar hechos con ideas.", "Se piensa que son lo mismo.", "Pregunta: ¿se puede comprobar?"),
    ],
    [
        E("«Hoy llovió en mi barrio». ¿Es un hecho o una idea?", "Un hecho", "Se puede comprobar."),
        E("«Los helados son lo más rico». ¿Es un hecho o una idea?", "Una idea", "Cada persona piensa distinto."),
        E("Primero lavé mis manos. Luego comí. ¿Qué hice antes de comer?", "Lavé mis manos", "Está dicho en el primer paso."),
    ],
    [
        E("Ordena: a) Luego comí. b) Primero me lavé las manos. c) Al final dormí. Escribe las letras en orden.", "b, a, c", "El orden es primero, luego, al final."),
        E("¿Qué palabras ayudan a ordenar un hecho?", "Primero, luego y al final", "Marcan el orden en que ocurrió."),
        E("«Ana fue a la biblioteca el lunes». ¿Es un hecho o una idea?", "Un hecho", "Cuenta algo que sucedió."),
    ],
    [
        E("Escribe un hecho sobre algo que hiciste hoy, empezando con «Hoy».", "Por ejemplo: Hoy desayuné pan", "Debe empezar con «Hoy» y contar un hecho."),
        E("Escribe dos hechos en orden con «Primero» y «Luego».", "Por ejemplo: Primero me vestí. Luego tomé el desayuno", "Debe usar ambas palabras."),
        E("Completa: «Al final del día yo...»", "Por ejemplo: me fui a dormir", "Debe contar el último hecho del día."),
    ],
    [
        E("Mía escribió: «Los gatos son malos. Ayer vi un gato en el techo». ¿Cuál es el hecho?", "Ayer vio un gato en el techo", "La primera oración es una idea."),
        E("Tomás escribió: «Luego fui al parque. Primero hice la tarea». ¿Está en orden? Responde sí o no.", "No", "Debió contar primero la tarea y luego el parque."),
    ],
    [
        E("Ordena para contar bien: a) Salí a jugar. b) Me puse los zapatos. c) Terminé de almorzar. Escribe las letras.", "c, b, a", "Primero se almuerza, luego se calza y por último se sale."),
        E("Escribe una oración con un hecho y otra con una idea sobre el parque.", "Por ejemplo: Ayer fui al parque. El parque es muy lindo", "Debe haber un hecho y una idea."),
    ],
    [E("Tu hermano llegó tarde de la escuela y quiere saber qué pasó hoy en tu casa. Cuéntale con «Primero» y «Luego»: llegó tu tía; después comieron sopa.", "Primero llegó la tía. Luego comieron sopa", "Respeta el orden en que ocurrió.")],
    [
        E("¿Qué es un hecho?", "Algo que realmente pasó", "Se puede comprobar."),
        E("¿Qué palabra usamos para el último hecho?", "Al final", "Marca el cierre."),
        E("«El fútbol es mejor que la natación» ¿es hecho o idea?", "Una idea", "Depende de lo que piense cada uno."),
    ],
    task(
        "Escribe tres hechos de lo que hiciste hoy, ordenados con las palabras «Primero», «Luego» y «Al final». Si necesitas ayuda, usa estas ideas: me levanté, desayuné, jugué, estudié, dormí.",
        "Primero me levanté. Luego desayuné. Al final jugué.",
        ["tres hechos", "usa las tres palabras de orden", "están en orden lógico"],
        ["tres oraciones", "lectura en voz alta"],
        ["escribir ideas en vez de hechos", "desordenar los hechos"],
        "Lee tus hechos en voz alta y pregunta: ¿estaría en ese orden lo que hice?",
    ),
    "Cuenta a alguien de tu casa lo que hiciste hoy usando primero, luego y al final.",
    "Escribe cuatro hechos del día de ayer, en orden.",
)

lesson(
    OA13, 3,
    "Cuaderno y lápiz. Las ideas de ejemplo están escritas en los ejercicios.",
    "Aprenderé a expresar una idea mía con «Creo que...» y una razón con «porque». Sirve para decir lo que pienso por escrito.",
    ["Sé escribir frases cortas.", "Sé que una idea es lo que pienso."],
    [
        "Una idea es lo que tú piensas o sientes sobre algo. Se puede escribir con la frase «Creo que...» o «Pienso que...». Otras personas pueden tener otras ideas, y eso está bien.",
        "Una idea tiene más valor si das una razón. Para eso se usa la palabra «porque». Por ejemplo: «Creo que el verano es lindo porque puedo ir a la playa». La razón explica por qué piensas así.",
        "Primero escribe tu idea, luego la palabra «porque» y al final la razón. Lee en voz alta para comprobar que se entiende. Una idea clara ayuda a que otros te comprendan.",
    ],
    [("idea", "lo que pienso"), ("creo que", "frase para decir mi idea"), ("porque", "palabra para dar la razón"), ("razón", "explicación de mi idea"), ("opinar", "decir lo que pienso")],
    [
        ("Escribir una idea", "Quieres decir que te gusta el verano. ¿Cómo empiezas?", ["Uso «Creo que...».", "Creo que el verano es lindo."], "Creo que el verano es lindo"),
        ("Agregar razón", "Completa: «Creo que el verano es lindo porque ...»", ["Pienso por qué me gusta.", "Puedo ir a la playa."], "Porque puedo ir a la playa"),
    ],
    [
        ("Escribir una idea sin razón.", "Se cree que basta con decirla.", "Agrega «porque» y la razón."),
        ("Poner una razón que no explica.", "Se escribe lo primero que se ocurre.", "Piensa: ¿esto explica mi idea?"),
    ],
    [
        E("¿Qué palabra usamos para dar la razón?", "Porque", "Une la idea con su explicación."),
        E("«Creo que el perro es leal». ¿Es un hecho o una idea?", "Una idea", "Es lo que piensa quien lo dice."),
        E("«Creo que...» sirve para...", "Decir mi idea", "Introduce lo que pienso."),
    ],
    [
        E("Lee: «Creo que el invierno es frío porque llueve mucho». ¿Cuál es la razón?", "Porque llueve mucho", "Viene después de «porque»."),
        E("Elige la idea con razón: A) «Me gusta el pan.» B) «Me gusta el pan porque es calentito.»", "B", "Sólo la B explica."),
        E("Lee: «Creo que el recreo es importante porque jugamos». ¿Cuál es la idea?", "El recreo es importante", "Está antes de «porque»."),
    ],
    [
        E("Escribe una idea con razón sobre los perros: «Creo que los perros son buenos amigos porque ...»", "Por ejemplo: acompañan a las personas", "Debe terminar con una razón."),
        E("Escribe una idea con razón sobre el helado: «Creo que ... porque ...»", "Por ejemplo: Creo que el helado es rico porque es dulce", "Debe tener idea y razón."),
        E("Completa: «Pienso que leer es bueno porque ...»", "Por ejemplo: aprendo cosas nuevas", "Debe dar una razón."),
    ],
    [
        E("Ana dice: «Creo que el cuaderno es lindo porque sí». ¿Dio una razón? Responde sí o no.", "No", "«Porque sí» no explica."),
        E("Dos amigos opinan sobre el fútbol y no están de acuerdo. ¿Está mal? Responde sí o no.", "No", "Cada persona puede pensar distinto."),
    ],
    [
        E("Ordena las palabras y escribe la oración: «divertido / es / jugar / que / creo / al sol».", "Creo que jugar al sol es divertido", "El orden correcto forma una idea con sentido."),
        E("Escribe una idea con dos razones usando «porque» y «y».", "Por ejemplo: Creo que el parque es lindo porque hay árboles y juegos", "Debe incluir dos razones."),
    ],
    [E("En tu curso votan el juego favorito del recreo: pelota, cuerda o escondida. Escribe tu voto con una razón: «Elijo ... porque ...»", "Por ejemplo: Elijo la cuerda porque salto muy alto", "Debe tener elección y razón.")],
    [
        E("¿Qué es una idea?", "Lo que yo pienso", "Puede variar entre personas."),
        E("En «Creo que el verano es lindo porque hay sol», ¿qué viene después de «porque»?", "La razón", "La explicación de la idea."),
        E("¿Está bien que otro piense distinto?", "Sí", "Cada uno tiene su idea."),
    ],
    task(
        "Elige una de estas preguntas y escribe tu idea con «Creo que... porque...»: A) ¿Cuál es la mejor estación del año? B) ¿Cuál es el mejor juego del recreo? C) ¿Es bueno dormir temprano?",
        "Creo que la mejor estación es el verano porque puedo ir a la playa.",
        ["responde una de las preguntas", "usa «Creo que»", "usa «porque» y da una razón"],
        ["oración escrita", "lectura en voz alta"],
        ["no usar porque", "no responder la pregunta"],
        "Pregúntate si la razón explica por qué piensas así; si no, cámbiala.",
    ),
    "Di en voz alta una idea tuya con «porque».",
    "Escribe dos ideas distintas con sus razones sobre tu comida favorita.",
)

lesson(
    OA13, 4,
    "Cuaderno y lápiz. Las situaciones están escritas en los ejercicios; no hace falta contar nada personal.",
    "Aprenderé a nombrar un sentimiento por escrito. Sirve para decir cómo me siento sin tener que contar detalles que no quiero compartir.",
    ["Sé que las personas sienten cosas.", "Sé escribir frases cortas."],
    [
        "Todas las personas sentimos cosas: alegría, pena, miedo, rabia o sorpresa. Poner nombre a lo que sentimos nos ayuda a entendernos y a que otros nos entiendan. Se puede escribir «Me siento contento» o «Estoy triste».",
        "Puedes explicar el sentimiento con una situación: «Me siento contento cuando juego con mis amigos». Es una forma de decir cuándo aparece ese sentimiento sin contar historias privadas.",
        "Tú decides qué compartes. Puedes escribir sobre un personaje de un cuento, sobre un animal o sobre una situación inventada. Lo importante es practicar las palabras de los sentimientos.",
    ],
    [("sentimiento", "lo que sentimos por dentro"), ("alegría", "sentimiento de estar contento"), ("pena", "sentimiento de estar triste"), ("miedo", "sentimiento cuando algo me asusta"), ("rabia", "sentimiento cuando algo me molesta mucho")],
    [
        ("Nombrar", "Luisa sonríe y salta porque ganó un premio. ¿Qué siente?", ["Sonríe y salta.", "Eso muestra alegría."], "Alegría"),
        ("Escribir", "Completa: «Me siento ... cuando ...» para el sentimiento alegría.", ["Elijo alegría.", "Pienso cuándo la siento."], "Me siento contento cuando juego con mis amigos"),
    ],
    [
        ("Decir «mal» sin más.", "Cuesta poner nombre al sentimiento.", "Usa palabras como alegría, pena, miedo o rabia."),
        ("Pensar que hay sentimientos prohibidos.", "Se cree que algunos están mal.", "Todos los sentimientos son normales; lo importante es cómo los manejamos."),
    ],
    [
        E("Un niño llora porque su globo se voló. ¿Qué siente?", "Pena", "Llorar por una pérdida muestra tristeza."),
        E("Una niña salta y ríe porque llegó su cumpleaños. ¿Qué siente?", "Alegría", "Reír y saltar muestran alegría."),
        E("Un gato se esconde bajo la cama por un trueno. ¿Qué siente?", "Miedo", "Esconderse muestra susto."),
    ],
    [
        E("Completa: «Cuando me quitan mi juguete siento rabia». ¿Cuál es el sentimiento?", "Rabia", "Es la palabra que nombra lo que siente."),
        E("¿Qué palabra nombra el sentimiento de estar contento?", "Alegría", "Es el nombre de ese sentimiento."),
        E("¿Para qué sirve nombrar lo que siento?", "Para entenderme y que me entiendan", "Poner nombre ayuda."),
    ],
    [
        E("Escribe un sentimiento que sientes cuando comes algo rico: «Me siento ...»", "Por ejemplo: contento", "Debe nombrar un sentimiento."),
        E("Completa con una situación: «Me siento tranquilo cuando ...»", "Por ejemplo: escucho un cuento", "Debe decir una situación."),
        E("Escribe una frase con la palabra «pena» sobre un personaje de cuento.", "Por ejemplo: El oso tuvo pena porque perdió su gorra", "Debe usar la palabra y hablar de un personaje."),
    ],
    [
        E("Tomás dice: «No quiero decir qué me pasa, pero me siento triste». ¿Está bien escribir sólo el sentimiento? Responde sí o no.", "Sí", "Puede nombrar el sentimiento sin dar detalles."),
        E("Ana dice «La rabia es mala». Su profesora dice que es normal. ¿Quién tiene razón?", "La profesora", "Todos los sentimientos son normales."),
    ],
    [
        E("Lee: «El zorro esperó toda la tarde, pero su amigo no llegó. Se sentó en una piedra y bajó las orejas.» ¿Qué siente el zorro?", "Pena", "Esperar y bajar las orejas muestra tristeza."),
        E("Escribe un sentimiento distinto de los de la clase (alegría, pena, miedo, rabia), por ejemplo «sorpresa», y una situación.", "Por ejemplo: Siento sorpresa cuando abro un regalo", "Debe nombrar un sentimiento nuevo y una situación."),
    ],
    [E("Una niña quiere escribir que se siente nerviosa antes de una presentación, sin contar más. ¿Qué frase le sirve? A) Estoy nerviosa B) Hoy pasó algo muy secreto", "A) Estoy nerviosa", "Nombra el sentimiento sin dar más datos.")],
    [
        E("¿Cómo se llama lo que sentimos por dentro?", "Sentimiento", "Es una emoción."),
        E("¿Cuál es un sentimiento? A) mesa B) alegría", "B) alegría", "La mesa es un objeto."),
        E("¿Hay que contar todo lo que nos pasa? Responde sí o no.", "No", "Cada uno decide qué comparte."),
    ],
    task(
        "Escribe dos frases de sentimientos usando este modelo: «Me siento ... cuando ...». Puedes escribir sobre ti, un personaje de cuento o un animal. Elige entre estos sentimientos: alegría, pena, miedo, rabia, sorpresa.",
        "Me siento alegre cuando juego con mis amigos. Me siento sorprendido cuando abro un regalo.",
        ["dos frases con el modelo", "nombra un sentimiento de la lista", "dice una situación"],
        ["dos frases en el cuaderno", "lectura en voz alta"],
        ["no nombrar un sentimiento", "dar detalles privados que no quiere compartir"],
        "Lee tus frases y comprueba que cada una diga el sentimiento y la situación.",
    ),
    "Di en voz alta tres sentimientos y cuándo los siente un personaje de cuento.",
    "Dibuja una cara para cada uno de los cuatro sentimientos básicos y escribe su nombre.",
)
