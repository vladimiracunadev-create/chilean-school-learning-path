"""Cuaderno del estudiante, 4.º básico Orientación: OA 01 (características, habilidades, fortalezas y metas) y OA 02 (emociones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR04 OA 01", "OR04 OA 02"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Una hoja y un lápiz. Los perfiles de los personajes están escritos en los ejercicios. No necesitas contar nada privado tuyo: puedes trabajar solo con personajes.",
    "Aprenderé a describir a una persona con hechos y evidencia, sin ponerle etiquetas. Sirve para conocer a los demás y a mí con respeto.",
    ["Sé que una característica es un rasgo de una persona.", "Sé que lo íntimo se cuenta solo si uno quiere."],
    [
        "Una característica dice cómo es una persona o qué le gusta. Hay características en lo académico, como ser curioso. Hay características sociales, como invitar a jugar. Hay características afectivas, como consolar a un amigo. Y hay características familiares, como ayudar con tareas de la casa. Para decirlas bien necesitas evidencia: algo que viste o escuchaste.",
        "Un hecho se puede observar: «Camila anotó los tres recados». Una suposición es algo que creo sin comprobarlo: «Seguro no quiere ayudar». Una etiqueta es una palabra fija que encierra a la persona: «Nico es un desordenado». La etiqueta y la suposición no tienen evidencia y no dejan espacio para cambiar.",
        "Para describir sin etiquetar, escribe el hecho y agrega «hoy», «a veces» o «todavía». Hay cosas íntimas que nadie está obligado a contar, como problemas de la casa o lo que sientes por dentro. Si te preguntan, puedes decir «prefiero no contarlo». Pero si algo te hace daño o te da miedo, sí conviene contárselo a una persona adulta de confianza. En esta clase trabajamos con personajes inventados.",
    ],
    [("característica", "rasgo que dice cómo es una persona"), ("evidencia", "algo visto o escuchado que apoya lo que digo"), ("hecho", "algo que se puede observar"), ("suposición", "algo que creo sin haberlo comprobado"), ("etiqueta", "palabra fija que encierra a una persona")],
    [
        W("Hecho, suposición o etiqueta", "Un niño dice: «Seguro Sam no quiere jugar». ¿Es hecho, suposición o etiqueta?", ["Pregunta: ¿alguien lo comprobó? No, Sam no dijo nada.", "No es una palabra fija sobre cómo es Sam.", "Es algo que se cree sin comprobar."], "Es una suposición"),
        W("Reescribir con el hecho", "Un niño escribió «Pía es desordenada». Lo que ocurrió: hoy la mochila de Pía quedó abierta y se cayeron los lápices. Escribe la frase con el hecho.", ["Busca qué pasó: la mochila quedó abierta.", "Agrega «hoy» para no encerrar a Pía.", "Cuenta el hecho sin juzgar."], "Hoy a Pía se le cayeron los lápices porque la mochila quedó abierta"),
    ],
    [
        M("Decir «Luis es un flojo» porque hoy no terminó.", "Un solo momento parece mostrar cómo es toda la persona.", "Cuenta el hecho: «Hoy Luis no alcanzó a terminar», y pregunta si necesita ayuda."),
        M("Contar algo íntimo porque un compañero insiste.", "Pensamos que hay que responder todas las preguntas.", "Puedes decir «prefiero no contarlo» y elegir otra característica."),
    ],
    R=[
        ex("«Camila anotó los tres recados en su cuaderno». ¿Es un hecho o una etiqueta?", "Un hecho", "Cuenta algo que Camila hizo y que se puede ver."),
        ex("«Nico es un desordenado». ¿Es un hecho o una etiqueta?", "Una etiqueta", "Es una palabra fija sin decir qué hizo Nico."),
        ex("«Seguro Nico no quiere ayudar». ¿Es un hecho, una etiqueta o una suposición?", "Una suposición", "Se cree algo sin comprobarlo con lo que Nico hizo."),
    ],
    U=[
        ex("¿Por qué «Luis es un flojo» no sirve para describir a Luis?", "Es una etiqueta sin evidencia", "No dice qué hizo y lo encierra en una palabra."),
        ex("¿Qué palabra deja espacio para cambiar: «todavía» o «siempre»?", "Todavía", "«Todavía» recuerda que la persona puede aprender y cambiar."),
        ex("Un compañero te pregunta si en tu casa hay problemas. ¿Estás obligado a contestar?", "No", "Es algo íntimo y tú decides si lo cuentas."),
    ],
    A=[
        ex("Tres frases sobre Rita: 1) «Rita trajo su mapa». 2) «Rita es presumida». 3) «Rita explicó el mapa a su grupo». ¿Cuántas son hechos?", "2", "Las frases 1 y 3 cuentan lo que Rita hizo; la 2 es una etiqueta."),
        ex("Reescribe como hecho con «hoy»: «Tomás es torpe». Lo ocurrido: Tomás tropezó con la mochila de Ana.", "Hoy Tomás tropezó con la mochila de Ana", "Se cuenta lo que pasó, con «hoy», y no se juzga a Tomás."),
        ex("La característica «curioso», ¿con qué evidencia se apoya mejor: «hoy preguntó por qué la luna cambia de forma» o «es bueno en todo»?", "«Hoy preguntó por qué la luna cambia de forma»", "Es un hecho que muestra curiosidad; la otra frase no dice qué hizo."),
    ],
    Z=[
        ex("Un compañero dice «Dani es antipático» porque hoy no habló en el recreo. ¿Alcanza ese hecho para decir que siempre es antipático?", "No", "Un solo día no muestra cómo es siempre; Dani pudo estar cansado."),
        ex("¿Cuál pregunta pide algo íntimo: «¿Qué te gusta dibujar?» o «¿Por qué lloraste anoche en tu casa?»", "«¿Por qué lloraste anoche en tu casa?»", "Habla de emociones y de la casa, que cada uno decide si cuenta."),
    ],
    D=[
        arith("Esta semana Mía ayudó 3 veces y escuchó con atención 2 veces a un compañero. Se rió de otro compañero 1 vez. ¿Cuántos hechos de ayuda y escucha hay?", "3+2", "Solo se suman los hechos de ayuda y de escucha."),
        arith("Ayer Ema tardó 12 minutos en resolver un problema y hoy tardó 9. Alguien dijo «Ema es lenta». ¿Cuántos minutos menos tardó Ema hoy que ayer?", "12-9", "La diferencia entre ayer y hoy es el dato concreto, y muestra que Ema cambió."),
    ],
    context=[ex("La profesora pide describir a un personaje sin etiquetas. Sara dice: «Matilde es valiente: se acercó sola a pedir ayuda al conserje». ¿Sara usó evidencia?", "Sí", "Apoyó la característica con algo que Matilde hizo.")],
    selfcheck=[ex("En Orientación: ¿una etiqueta deja espacio para cambiar?", "No", "Encierra a la persona en una palabra."), ex("¿Un hecho se puede observar?", "Sí", "Se ve o se escucha."), ex("¿Debes contar algo íntimo si te lo piden?", "No", "Tú decides qué compartir.")],
    task=T("Lee los perfiles. Luz ayudó 3 veces a repartir hojas y dibuja flores. Teo esperó su turno y, cuando se equivocó, lo intentó otra vez. Mía invitó a jugar a una niña nueva. Elige a uno. Escribe dos hechos y una característica con su evidencia, usando «hoy», «a veces» o «todavía». No uses etiquetas ni suposiciones.", "Teo: esperó su turno; se equivocó y lo intentó otra vez. Teo es perseverante porque hoy lo intentó otra vez.", ["escribe dos hechos observables", "une la característica con una evidencia", "no usa etiquetas ni cuenta algo íntimo"], ["texto escrito o dicho", "dibujo con una frase"], ["usar una etiqueta fija", "dar una característica sin evidencia"], "Reconoce los hechos y pregunta qué evidencia apoya la característica."),
    reinforce="Escribe tres hechos sobre un personaje de un cuento y una característica que ellos apoyan.",
    extend="Toma una etiqueta que hayas escuchado y reescríbela como un hecho con «hoy» o «a veces».",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. Las tablas de avance y las situaciones están escritas en los ejercicios.",
    "Aprenderé a reconocer mis habilidades con evidencia y a ver mi progreso. Sirve para confiar en mí y saber qué puedo seguir mejorando.",
    ["Sé describir con hechos y sin etiquetas.", "Sé que lo que practico puede mejorar."],
    [
        "Una habilidad es algo que sabes hacer y que puedes mejorar. Hay habilidades académicas, como resolver problemas. Hay habilidades sociales, como trabajar en equipo. Hay habilidades afectivas, como consolar a alguien. Y hay habilidades para colaborar en la casa, como ordenar tus cosas. Una misma persona tiene habilidades en varias áreas.",
        "Para reconocer una habilidad necesitas evidencia que se pueda mostrar: un trabajo hecho, algo que hiciste o algo que otra persona vio. «Mi amigo dice que soy bueno» es una opinión y no alcanza. «Terminé el cartel con mi grupo y repartí las partes» es una evidencia. Una evidencia que se repite es más sólida que una sola vez.",
        "El progreso es lo que mejoró entre un antes y un ahora. Se mide comparando contigo mismo, no con otro niño. Si algo todavía te cuesta, no es un defecto. Es una habilidad que puedes practicar.",
    ],
    [("habilidad", "algo que sé hacer y puedo mejorar"), ("evidencia", "algo que hice y se puede mostrar"), ("progreso", "mejora que se nota entre un antes y un ahora"), ("académico", "que tiene que ver con aprender en la escuela"), ("afectivo", "que tiene que ver con lo que sentimos por otros")],
    [
        W("Evidencia que se puede mostrar", "Bruno dice «sé escuchar». Su evidencia: «ayer esperé a que Camila terminara de hablar y luego respondí lo que ella dijo». ¿La evidencia apoya su habilidad?", ["Escuchar es esperar y entender al otro.", "Bruno esperó y después respondió lo que Camila dijo.", "Eso lo hizo y se puede contar."], "Sí, la evidencia apoya su habilidad"),
        W("Medir el progreso", "Tomás leyó 35 palabras por minuto el lunes y 52 palabras por minuto el viernes. ¿Cuánto avanzó?", ["Se compara a Tomás con él mismo.", "Se resta lo del viernes menos lo del lunes: 52 menos 35.", "El resultado es su progreso."], "17 palabras por minuto más"),
    ],
    [
        M("Pensar que reconocer mis habilidades es presumir.", "Se confunde hablar de lo que sé con sentirse más que otros.", "Di lo que sabes con evidencia y sin comparar."),
        M("Medir mi progreso mirando a quien lo hace mejor.", "El otro lleva más práctica y eso desanima.", "Compara cómo te salía antes con cómo te sale hoy."),
    ],
    R=[
        ex("«Resolver problemas de suma». ¿Es una habilidad académica o afectiva?", "Académica", "Tiene que ver con aprender y pensar en la escuela."),
        ex("«Consolar a una amiga que está triste». ¿Es una habilidad afectiva o académica?", "Afectiva", "Se trata de acompañar lo que siente otra persona."),
        ex("«Tengo un cuaderno con cinco problemas resueltos». ¿Es una evidencia que se puede mostrar?", "Sí", "El cuaderno se puede mirar y comprobar."),
    ],
    U=[
        ex("¿Por qué «soy genial» no es una evidencia?", "Es una opinión sin hechos", "No dice nada que hiciste y se pueda mostrar."),
        ex("Para ver tu progreso, ¿qué comparas?", "Tu trabajo de antes con el de ahora", "Así ves tu propia mejora."),
        ex("¿Qué evidencia es más sólida: «una vez ayudé» o «esta semana ayudé 4 veces»?", "«Esta semana ayudé 4 veces»", "Una evidencia que se repite muestra mejor la habilidad."),
    ],
    A=[
        arith("En la semana 1 Rosa leyó 28 palabras por minuto y en la semana 4 leyó 46. ¿Cuántas palabras por minuto más leyó en la semana 4?", "46-28", "El progreso es la diferencia entre los dos momentos."),
        ex("¿Qué habilidad apoya la evidencia «terminé el cartel con mi grupo y repartí las partes»: cocinar o trabajar en equipo?", "Trabajar en equipo", "Repartir las partes y terminar juntos es colaborar."),
        ex("Cambia «no sé dividir» por una frase que deje espacio para aprender.", "Todavía no sé dividir", "La palabra «todavía» recuerda que se puede aprender."),
    ],
    Z=[
        ex("Un niño dice: «Ana lee mejor, así que yo no avanzo». Antes leía 30 palabras por minuto y ahora 45. ¿Avanzó?", "Sí, avanzó 15", "Su progreso se mide con su antes y su ahora, no con Ana."),
        ex("Una niña presenta como evidencia «mi amigo dice que soy buena para dibujar». ¿Alcanza?", "No, falta algo que ella hizo", "Es una opinión; falta mostrar un dibujo o algo hecho."),
    ],
    D=[
        arith("Julia practicó 15 minutos cada día, de lunes a viernes. ¿Cuántos minutos practicó en total?", "15*5", "Son 15 minutos repetidos en 5 días."),
        ex("Evidencias de Ben: (a) «dibujó el afiche del curso», (b) «dice que es el mejor dibujante», (c) «su dibujo está pegado en la sala». ¿Cuántas son hechos que se pueden mostrar?", "2", "Las evidencias (a) y (c) se pueden comprobar; (b) es una opinión."),
    ],
    context=[ex("En una reunión, Lucía dice: «Soy buena para organizar: ordené los útiles del grupo en cajas por color y nadie perdió nada». ¿Lucía dio una evidencia de su habilidad?", "Sí", "Contó algo que hizo y que se puede comprobar.")],
    selfcheck=[ex("En Orientación: ¿puedes medir tu progreso comparándote contigo mismo?", "Sí", "Mirar tu antes y tu ahora es justo."), ex("¿Decir lo que sabes hacer, con evidencia, es presumir?", "No", "Es conocer con qué cuentas."), ex("¿Una habilidad puede mejorar con práctica?", "Sí", "Repetir con calma ayuda a avanzar.")],
    task=T("Elige tres habilidades de esta lista: leer en voz alta, escuchar a un compañero, ordenar tus útiles, consolar a alguien, trabajar en equipo, resolver un problema. Para cada una escribe o dibuja una evidencia. Si no tienes evidencia de una, escribe «todavía» y un primer paso pequeño.", "Escuchar a un compañero: ayer esperé a que mi compañera terminara de hablar. Resolver un problema: todavía; primer paso: pedir una pista.", ["elige tres habilidades de la lista", "cada una tiene evidencia o un «todavía» con un paso", "no se compara con otras personas"], ["lista escrita o dibujada"], ["decir la habilidad sin evidencia", "compararse con otros"], "Reconoce las evidencias y propone un paso pequeño si falta alguna."),
    reinforce="Escribe una habilidad que hayas mejorado en este año y qué hiciste para mejorarla.",
    extend="Elige una habilidad de la lista que todavía no tengas y escribe dos cosas que podrías practicar.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. El caso del equipo está escrito en los ejercicios.",
    "Aprenderé a valorar mis fortalezas y las de otros, que son distintas. Sirve para trabajar en grupo sin competir.",
    ["Sé reconocer una habilidad con evidencia.", "Sé que cada persona es distinta."],
    [
        "Una fortaleza es una habilidad o una forma de ser que te ayuda y que también ayuda a otros. Hay fortalezas académicas, como investigar. Hay fortalezas sociales, como invitar a alguien a jugar. Hay fortalezas afectivas, como ser cariñoso. Y hay fortalezas para colaborar, como cuidar los materiales del curso. Todas importan.",
        "Valorar es reconocer que algo tiene importancia. Imagina un equipo que arma un mural: una niña dibuja, un niño ordena los colores y otra escucha las ideas de todos. Nadie es «el mejor». Sin cualquiera de los tres aportes, el mural sería más difícil de terminar.",
        "Comparar para saber quién gana suele dejar a alguien triste. Una buena frase de valoración dice qué hizo la persona y qué efecto tuvo: «Me gustó que ordenaras los colores, porque encontramos todo rápido». No pone a nadie arriba ni abajo. Tú también puedes valorar tus fortalezas sin que otro valga menos.",
    ],
    [("fortaleza", "habilidad o forma de ser que ayuda a mí y a otros"), ("valorar", "reconocer que algo tiene importancia"), ("aporte", "lo que una persona da para ayudar al grupo"), ("diversidad", "que las personas somos distintas"), ("comparar", "mirar dos cosas para ver cuál es mejor")],
    [
        W("Frase que valora", "¿Qué frase valora a Mía: «Dibujas mejor que todos» o «Me gustó cómo pintaste el cielo, porque se ve muy real»?", ["La primera pone a Mía sobre los demás.", "La segunda dice qué hizo Mía y qué efecto tuvo.", "Valorar es mirar lo que la persona aporta."], "«Me gustó cómo pintaste el cielo, porque se ve muy real»"),
        W("Aportes distintos", "En un mural, Ana dibuja, Beto ordena los colores, Cata escucha las ideas y Dino pega las partes. ¿Cuántos aportes distintos hay?", ["Ana aporta dibujo.", "Beto aporta orden y Cata aporta escucha.", "Dino aporta el pegado: son 1, 2, 3, 4."], "4 aportes distintos"),
    ],
    [
        M("Pensar que valorar a otro me hace menos a mí.", "Se cree que el reconocimiento es una competencia.", "Reconocer a otro no quita nada de lo que tú vales."),
        M("Creer que solo cuentan las fortalezas de las notas.", "Se olvida que ayudar, escuchar y cuidar también son fortalezas.", "Mira fortalezas académicas, sociales, afectivas y de colaboración."),
    ],
    R=[
        ex("¿Valorar es decir quién gana o reconocer lo que alguien aporta?", "Reconocer lo que alguien aporta", "Valorar no es competir."),
        ex("Beto ordena los colores del mural. ¿Su aporte sirve al grupo?", "Sí", "El orden ayuda a que el trabajo salga."),
        ex("«Gracias por esperar mi turno» ¿es una frase que valora?", "Sí", "Reconoce algo que la persona hizo."),
    ],
    U=[
        ex("¿Por qué «Eres el mejor del curso» no ayuda a valorar a alguien?", "Lo pone sobre los demás y no dice qué hizo", "Compara y no describe el aporte."),
        ex("«Cuidar los materiales del curso» ¿es una fortaleza social o de colaboración?", "De colaboración", "Ayuda a que todos puedan usar los materiales."),
        ex("Si otro compañero tiene una fortaleza distinta a la tuya, ¿tu fortaleza vale menos?", "No", "Cada fortaleza ayuda de una forma distinta."),
    ],
    A=[
        ex("Completa con un hecho y un efecto: «Me gustó que ___, porque ___». Dino pegó las partes del mural y quedó firme.", "Me gustó que pegaras las partes del mural, porque quedó firme", "Dice qué hizo Dino y qué efecto tuvo."),
        ex("En un equipo, Ema investiga, Leo anima a todos y Rita cuida los lápices. ¿Cuántas fortalezas distintas se nombran?", "3", "Investigar, animar y cuidar son tres fortalezas diferentes."),
        ex("¿Cuál frase valora sin comparar: «Cantas mejor que Pedro» o «Tu voz le dio alegría a la canción del curso»?", "«Tu voz le dio alegría a la canción del curso»", "Dice el aporte y no pone a nadie por debajo."),
    ],
    Z=[
        ex("Un niño dice: «Si reconozco que Ana explica bien, quedo como el que no sabe». ¿Tiene razón?", "No", "Reconocer a otro no te quita valor; tú también tienes fortalezas."),
        ex("Un grupo dice que solo sirve quien saca buenas notas. ¿Qué fortalezas se les olvidaron?", "Las sociales, afectivas y de colaboración", "Escuchar, ayudar y cuidar también hacen que el grupo funcione."),
    ],
    D=[
        arith("El curso de 4.º tiene 28 estudiantes y el mural lo arman en grupos de 4. ¿Cuántos grupos hay?", "28//4", "Se reparten 28 estudiantes en grupos de 4."),
        ex("Un grupo escribió estas frases: 1) «Eres lo máximo». 2) «Gracias por explicar el paso 3, así lo entendí». 3) «Tú sí sabes más que todos». ¿Cuántas valoran con un hecho y un efecto?", "1", "Solo la frase 2 dice qué hizo la persona y qué efecto tuvo."),
    ],
    context=[ex("Para el mural, el curso se divide en tareas. Nico dice: «Yo no sé dibujar, no sirvo». Su compañera responde: «Tú escuchaste las ideas de todos y las anotaste; eso nos ayudó». ¿La compañera valoró un aporte de Nico?", "Sí", "Nombró algo que Nico hizo y cómo ayudó al grupo.")],
    selfcheck=[ex("En Orientación: ¿valorar a otro es competir con él?", "No", "Es reconocer lo que aporta."), ex("¿Ayudar y escuchar pueden ser fortalezas?", "Sí", "No solo las notas son fortalezas."), ex("¿Una buena frase de valoración dice qué hizo la persona?", "Sí", "Así se apoya en un hecho.")],
    task=T("Lee el caso. En el grupo de Teo, Ana dibuja bien, Lola organiza los turnos y Marcos anima cuando alguien se equivoca. Escribe una frase de valoración para cada uno con la forma «Me gustó que… porque…». Después escribe una fortaleza tuya, con una evidencia, que podrías aportar a un grupo.", "Para Lola: Me gustó que organizaras los turnos, porque todos pudimos hablar. Mi fortaleza: ordenar; ayer ordené los materiales del grupo.", ["escribe tres frases con hecho y efecto", "no compara a unas personas con otras", "nombra una fortaleza propia con evidencia"], ["texto escrito o dicho"], ["decir «eres el mejor»", "valorar solo las notas"], "Reconoce el hecho y el efecto y pregunta cómo se sentiría la otra persona al oírlo."),
    reinforce="Escribe una frase de valoración para alguien que te ayudó esta semana, con un hecho y un efecto.",
    extend="Piensa en un equipo de tu escuela y escribe tres aportes distintos que lo hacen funcionar.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. Las metas y las tablas de práctica están escritas en los ejercicios.",
    "Aprenderé a proponerme una acción concreta para mejorar algo que todavía me cuesta. Sirve para avanzar paso a paso, sin sentirme mal.",
    ["Sé reconocer una habilidad con evidencia.", "Sé que lo que todavía no sé puedo aprenderlo."],
    [
        "Una meta es algo que quieres lograr. «Ser mejor» es muy vago, porque no se sabe qué hacer. Una acción concreta dice qué haré, cuánto y por cuánto tiempo. Por ejemplo: «Leeré 10 minutos cada día durante 2 semanas». Así puedes saber si la cumpliste.",
        "Una buena acción de mejora cumple cuatro cosas. Es pequeña y se puede hacer en tu vida real. Tiene una medida, como minutos o veces. Tiene un plazo, como dos semanas. Y puede tener apoyo de alguien, por ejemplo de una persona de tu casa o de tu profesora. Si no cumples un día, no pasa nada: sigues al día siguiente.",
        "Para revisar tu progreso, anota lo que hiciste y compara con tu meta. Si no resultó, cambia la acción, no a ti. Un aspecto que debes superar no es una etiqueta tuya. Es solo un lugar donde todavía puedes crecer.",
    ],
    [("meta", "algo que quiero lograr"), ("acción concreta", "algo que haré, con medida y plazo"), ("plazo", "el tiempo que me doy para hacerlo"), ("progreso", "mejora que se nota entre un antes y un ahora"), ("apoyo", "ayuda de alguien de confianza")],
    [
        W("Meta vaga y acción concreta", "Rita escribió «voy a ser más ordenada». ¿Cómo la convertirías en una acción concreta? Ya sabes que se le pierden los lápices.", ["Elige qué hará: guardar los lápices en el estuche.", "Pon una medida y un plazo: cada día al terminar la clase, durante 2 semanas.", "Une las partes en una frase."], "Guardaré mis lápices en el estuche al terminar cada clase, durante 2 semanas"),
        W("Revisar la meta", "Teo se propuso practicar 10 minutos al día durante 5 días. Practicó 10, 10, 0, 10 y 10 minutos. ¿Cuántos minutos practicó en total?", ["Se suman los minutos de los cinco días.", "10 + 10 + 0 + 10 + 10.", "Un día sin práctica no echa a perder la meta."], "40 minutos"),
    ],
    [
        M("Escribir una meta vaga como «ser mejor».", "No dice qué hacer, así que no se sabe si se logró.", "Escribe qué harás, cuánto y por cuánto tiempo."),
        M("Dejar la meta si un día no la cumplí.", "Se piensa que fallar una vez es fallar para siempre.", "Anota lo que pasó y sigue al día siguiente."),
    ],
    R=[
        ex("¿Cuál es más concreta: «ser más ordenada» o «guardar los lápices cada día al terminar la clase»?", "«Guardar los lápices cada día al terminar la clase»", "Dice qué hacer y cuándo."),
        ex("En «leeré 10 minutos cada día durante 2 semanas», ¿cuál es el plazo?", "2 semanas", "El plazo es el tiempo que me doy para hacerlo."),
        ex("Si un día no cumples tu acción, ¿tienes que abandonar la meta?", "No", "Puedes seguir al día siguiente."),
    ],
    U=[
        ex("¿Por qué «voy a ser mejor» no es una acción concreta?", "No dice qué hacer ni cuánto", "Sin medida ni plazo no se puede comprobar."),
        ex("¿Qué dos datos hacen que una acción se pueda medir: medida y plazo o color y tamaño?", "Medida y plazo", "Dicen cuánto y por cuánto tiempo."),
        ex("Si tu acción no resultó, ¿qué cambias: la acción o a ti mismo?", "La acción", "El aspecto por mejorar no es una etiqueta tuya."),
    ],
    A=[
        arith("Lola quiere repasar las tablas 10 minutos al día durante 6 días. ¿Cuántos minutos repasará en total si cumple?", "10*6", "Son 10 minutos repetidos en 6 días."),
        ex("Para «hablar más fuerte al exponer», ¿cuál es una acción concreta: «Practicaré mi exposición 5 minutos al día frente a una persona de confianza durante 1 semana» o «Voy a hablar mejor»?", "«Practicaré mi exposición 5 minutos al día frente a una persona de confianza durante 1 semana»", "Tiene qué hacer, medida, plazo y apoyo; la otra no dice cuánto ni hasta cuándo."),
        ex("Pedro anotó los minutos que practicó: 5, 10, 10, 5. ¿Cuántos minutos practicó en total?", "30", "5 + 10 + 10 + 5 = 30."),
    ],
    Z=[
        ex("Un niño dice: «No logré mi meta, soy un fracaso». ¿Qué conviene decir en cambio?", "Mi acción no resultó; voy a cambiarla", "Se cambia la acción y no se etiqueta a la persona."),
        ex("Una niña se propuso 20 minutos de práctica cada día, pero solo tiene 10 minutos libres después de la tarea. ¿Qué debería ajustar?", "La medida: bajar a 10 minutos", "Una buena acción es pequeña y se puede hacer en la vida real."),
    ],
    D=[
        arith("Ana se propuso practicar 15 minutos al día durante 4 días. El tercer día practicó solo 5. ¿Cuántos minutos le faltaron para cumplir la meta ese día?", "15-5", "La meta diaria era 15 minutos y practicó 5."),
        ex("Meta A: «ser más amable». Meta B: «saludar a mi profesora cada mañana durante 10 días». Meta C: «ser responsable». ¿Cuál se puede comprobar?", "Meta B", "Tiene una acción, una frecuencia y un plazo."),
    ],
    context=[ex("Un niño dice que le cuesta terminar los trabajos a tiempo. Su profesora le propone dividir el trabajo en tres partes pequeñas y terminar una por día. ¿Es una acción concreta?", "Sí", "Tiene pasos pequeños, una medida y un plazo.")],
    selfcheck=[ex("En Orientación: ¿una meta como «ser mejor» es concreta?", "No", "No dice qué hacer ni cuánto."), ex("¿Una acción de mejora debe tener medida y plazo?", "Sí", "Así se puede revisar."), ex("¿Puedes pedir apoyo a alguien de confianza para cumplir tu meta?", "Sí", "El apoyo ayuda a seguir.")],
    task=T("Elige una de estas situaciones: (a) a Nora le cuesta guardar sus útiles, (b) a Iván le cuesta empezar las tareas, (c) a Sofía le cuesta hablar en grupo. Escribe una acción concreta con qué, cuánto y plazo. Agrega un apoyo posible y cómo anotarías tu progreso en una tabla de 5 días.", "(a) Nora guardará sus útiles al terminar cada clase durante 2 semanas. Apoyo: su profesora le recordará. Tabla: lun ✓, mar ✓, mié ✗…", ["la acción tiene qué, cuánto y plazo", "incluye un apoyo y una forma de anotar el progreso", "no etiqueta a la persona"], ["texto o tabla escrita"], ["escribir una meta vaga", "ponerse un plazo imposible"], "Revisa que la acción se pueda comprobar y pregunta cómo la ajustaría si un día falla."),
    reinforce="Escribe una acción concreta, con plazo, para mejorar algo de tu vida escolar. Puede ser sobre un personaje.",
    extend="Anota durante 3 días cuánto cumpliste de una acción pequeña y escribe qué cambiarías.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. Las escenas con personajes están escritas en los ejercicios.",
    "Aprenderé a identificar mis emociones y las señales del cuerpo, y a ser prudente cuando pienso en lo que siente otra persona. Sirve para entender mejor lo que me pasa y preguntar a los demás.",
    ["Sé distinguir una emoción de una conducta.", "Sé que el cuerpo da señales cuando siento algo."],
    [
        "Una emoción es lo que sientes ante algo que pasa, como alegría, rabia, miedo, pena o vergüenza. Tiene una intensidad: puede ser débil, media o muy fuerte. Una escala de 1 a 5 ayuda a decirla: 1 es muy poca y 5 es muchísima. La emoción te da información sobre lo que te importa.",
        "El cuerpo y la voz dan señales: el corazón late más rápido, el estómago se aprieta, la cara se pone roja o las manos se mueven. Son pistas, pero una misma señal puede ser de distintas emociones. Con el corazón rápido puedes tener miedo o puedes tener emoción por un juego.",
        "Para las emociones de otra persona, usa cautela. Puedes ver una señal, pero no puedes saber con certeza qué siente. Es mejor decir «Parece que estás enojado, ¿es así?» que afirmar «Estás enojado». Así dejas que la persona diga lo que siente. Nadie está obligado a contar sus emociones si no quiere.",
    ],
    [("emoción", "lo que siento ante algo que pasa"), ("intensidad", "cuánta fuerza tiene lo que siento"), ("señal", "pista del cuerpo o de la voz"), ("cautela", "cuidado para no afirmar lo que no sé"), ("certeza", "estar seguro de que algo es verdad")],
    [
        W("Intensidad", "Ema está muy asustada: tiembla y no puede hablar. En una escala de 1 a 5, ¿dónde la pondrías: 1 o 5?", ["Hay señales fuertes: tiembla y no habla.", "Eso indica mucha intensidad.", "Pon el valor más alto."], "5"),
        W("Señal con cautela", "Dani frunce el ceño y no habla. ¿Qué dices: «Estás enojado» o «Parece que algo te molestó, ¿es así?»", ["Fruncir el ceño es solo una señal.", "No sabes con certeza qué siente Dani.", "La segunda frase pregunta y no afirma."], "«Parece que algo te molestó, ¿es así?»"),
    ],
    [
        M("Decir «tú estás triste» solo porque veo su cara.", "Una señal puede significar distintas emociones.", "Pregunta: «Parece que estás triste, ¿es así?»"),
        M("Pensar que si no sé nombrar lo que siento, no siento nada.", "A veces hay emociones mezcladas.", "Prueba con una escala de 1 a 5 y con señales del cuerpo."),
    ],
    R=[
        ex("«Sentir rabia porque se rompió mi trabajo» ¿es una emoción o una conducta?", "Una emoción", "Es lo que siento; la conducta sería lo que hago."),
        ex("En una escala de 1 a 5, ¿5 es poca intensidad o mucha?", "Mucha", "El 5 es el valor más alto."),
        ex("«Corazón rápido» ¿es una señal del cuerpo o una conducta?", "Una señal del cuerpo", "Es algo que el cuerpo hace sin que uno lo decida."),
    ],
    U=[
        ex("Una misma señal, como el corazón rápido, ¿puede ser de distintas emociones?", "Sí", "Puede ser miedo o puede ser emoción por un juego."),
        ex("¿Qué es más cuidadoso: «Estás enojado» o «Parece que estás enojado, ¿es así?»", "«Parece que estás enojado, ¿es así?»", "Pregunta y no afirma lo que no sabe con certeza."),
        ex("¿Estás obligado a contar tus emociones si no quieres?", "No", "Tú decides si lo cuentas y a quién."),
    ],
    A=[
        ex("Rita cruza los brazos, mira al suelo y no responde. ¿Qué frase es más cuidadosa: «Parece que algo te preocupa, ¿quieres contarme?» o «Estás enojada, admítelo»?", "«Parece que algo te preocupa, ¿quieres contarme?»", "Describe una señal y pregunta sin afirmar."),
        ex("Pedro se pone rojo cuando lo felicitan frente al curso y dice «quiero esconderme». ¿Qué emoción describe mejor lo que cuenta: vergüenza o rabia?", "Vergüenza", "Querer esconderse ante muchas personas es lo que cuenta alguien con vergüenza."),
        ex("Si tu emoción es una pena de intensidad 2, ¿es débil, media o muy fuerte?", "Débil", "En una escala de 1 a 5, el 2 es bajo."),
    ],
    Z=[
        ex("Un niño dice: «Mi amiga está contenta porque sonrió». Luego ella dice que se sentía nerviosa. ¿Por qué se equivocó?", "Una sonrisa es solo una señal y no prueba la emoción", "No tenía certeza; debió preguntarle."),
        ex("Dos niños tienen la misma señal: manos temblorosas. Uno siente miedo y otro emoción por salir a un acto. ¿Qué muestra esto?", "Que una señal puede ser de distintas emociones", "Por eso hay que preguntar y no suponer."),
    ],
    D=[
        arith("Una escala de rabia va de 1 a 5. Teo marcó 4 al empezar y 2 después de una pausa. ¿Cuántos puntos bajó su rabia?", "4-2", "Se resta la intensidad final a la inicial."),
        ex("Marca la señal que más claramente indica miedo fuerte en una escena: «sonreía mucho» o «temblaba y se escondía»", "«Temblaba y se escondía»", "Son señales de miedo, aunque habría que preguntar para estar seguro."),
    ],
    context=[ex("En el recreo, Lola ve a Tomás solo, con la mirada baja. Le dice: «Te veo callado, ¿quieres jugar o prefieres estar solo?». ¿Lola usó cautela?", "Sí", "Describió lo que vio y preguntó sin afirmar lo que siente.")],
    selfcheck=[ex("En Orientación: ¿una señal del cuerpo prueba qué emoción siente otro?", "No", "Solo da una pista."), ex("¿Una escala de 1 a 5 ayuda a decir la intensidad de una emoción?", "Sí", "Permite decir cuánta fuerza tiene."), ex("¿Puedes decidir no contar lo que sientes?", "Sí", "Tus emociones son tuyas.")],
    task=T("Lee las escenas. A) Una niña aprieta los puños y respira rápido porque no la escogieron para un juego. B) Un niño sonríe y mueve las piernas antes de salir a un acto. C) Una niña mira por la ventana, sin hablar. Elige dos. Para cada una escribe una señal que ves, una emoción posible, la intensidad de 1 a 5 y una pregunta cuidadosa que le harías.", "A) Señal: aprieta los puños. Emoción posible: rabia, intensidad 4. Pregunta: Parece que te molestó, ¿es así?", ["nombra una señal y una emoción posible", "pone una intensidad de 1 a 5", "usa una pregunta cuidadosa y no afirma"], ["texto escrito o dicho"], ["afirmar lo que el otro siente", "no decir la intensidad"], "Reconoce la señal y pregunta qué otra emoción podría haber."),
    reinforce="Elige un personaje de un cuento y escribe una emoción, su intensidad y una señal de su cuerpo.",
    extend="Escribe dos señales que puede tener la vergüenza y dos que puede tener la alegría, y di cuál se parece.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. Las situaciones de personajes están escritas en los ejercicios.",
    "Aprenderé a aceptar mis emociones y a distinguirlas de lo que hago con ellas. Sirve para sentir con libertad y no lastimar a nadie.",
    ["Sé reconocer una emoción y su intensidad.", "Sé que el cuerpo da señales."],
    [
        "Todas las emociones se pueden sentir. La rabia, la pena, el miedo y la alegría no son buenas ni malas. Son información sobre lo que pasa. Aceptar una emoción es decir: «Esto siento ahora», sin enojarme conmigo por sentirlo. También puedes aceptar las emociones de otras personas: cada una siente a su manera y lo que siente es válido, aunque tú sentirías distinto.",
        "Lo que puede ser dañino no es la emoción, sino lo que hago con ella. Sentir rabia está bien. Pegar, romper cosas o insultar lastima y no está bien. La conducta tiene límites: no puedo dañar a otros, a mí ni a las cosas. Puedo decidir qué hago aunque la emoción sea muy fuerte.",
        "Hay conductas que sí ayudan a expresar una emoción: decir con palabras lo que siento, pedir un momento a solas, dibujar, moverme con calma o pedir ayuda a un adulto. Si lastimé a alguien por una emoción fuerte, puedo reparar el daño: decir lo siento y ayudar a arreglarlo.",
    ],
    [("aceptar", "reconocer que algo lo siento, sin juzgarme"), ("conducta", "lo que hago con lo que siento"), ("límite", "algo que no puedo hacer porque dañaría a alguien"), ("expresar", "mostrar con palabras o acciones lo que siento"), ("reparar", "arreglar un daño que causé")],
    [
        W("Emoción y conducta", "Beto siente rabia y rompe el lápiz de un compañero. ¿Qué es emoción y qué es conducta?", ["La rabia es lo que siente Beto: emoción.", "Romper el lápiz es lo que hace: conducta.", "La conducta lastimó a otro."], "Rabia es la emoción; romper el lápiz es la conducta"),
        W("Otra conducta posible", "Beto siente mucha rabia. Elige una conducta sin daño: «romper el lápiz» o «decir que está muy enojado y pedir un momento a solas».", ["Romper cosas daña a otro.", "Decir con palabras lo que siente no daña.", "Pedir un momento a solas ayuda a calmarse."], "Decir que está muy enojado y pedir un momento a solas"),
    ],
    [
        M("Pensar que sentir rabia es malo.", "Se confunde la emoción con la conducta.", "La emoción se acepta; la conducta dañina tiene límites."),
        M("Creer que si estoy muy enojado, no puedo elegir qué hago.", "La emoción fuerte hace sentir que no hay opciones.", "Siempre puedo pausar y elegir una conducta sin daño."),
    ],
    R=[
        ex("¿La rabia es una emoción buena, mala o ninguna de las dos?", "Ninguna de las dos", "Las emociones no son buenas ni malas."),
        ex("«Gritar un insulto» ¿es una emoción o una conducta?", "Una conducta", "Es algo que se hace."),
        ex("¿Se puede sentir rabia y no pegar?", "Sí", "La emoción y la conducta son cosas distintas."),
    ],
    U=[
        ex("¿Por qué no está bien romper las cosas de otro cuando siento rabia?", "Porque lastima o daña a otra persona", "La conducta tiene límites aunque la emoción sea fuerte."),
        ex("¿Aceptar una emoción significa hacer lo que ella pide?", "No", "Aceptarla es reconocerla; igual elijo qué hago."),
        ex("Si lastimé a alguien por mi enojo, ¿qué puedo hacer después?", "Decir lo siento y ayudar a reparar el daño", "Reparar ayuda a arreglar lo que pasó."),
    ],
    A=[
        ex("Marta siente vergüenza porque se equivocó frente al curso. ¿Qué conducta sin daño puede elegir: reírse de otro o respirar y decir «me equivoqué, lo intento otra vez»?", "Respirar y decir «me equivoqué, lo intento otra vez»", "Expresa su emoción sin dañar."),
        ex("Pedro siente mucha pena porque se perdió su dibujo. ¿Qué conducta lo ayuda a expresarla sin dañar: contarle a una persona de confianza o romper el dibujo de otro niño?", "Contarle a una persona de confianza", "Es una forma de expresar la pena sin lastimar."),
        ex("Un niño dice «estoy enojado» y se aparta un momento. ¿Qué hizo con su emoción: la expresó con palabras o dañó a alguien?", "La expresó con palabras", "Dijo lo que sentía y no lastimó a nadie."),
    ],
    Z=[
        ex("Ana dice: «Me puse furiosa y lo empujé, pero ya qué, estaba enojada». ¿La emoción justifica empujar?", "No", "La emoción es válida, pero empujar es una conducta que lastima."),
        ex("Un niño dice: «Mi amigo no debería llorar por algo tan pequeño». ¿Qué conviene recordar al aceptar las emociones de los demás?", "Que cada persona siente a su manera y su emoción es válida", "Aceptar también significa no juzgar lo que siente otra persona."),
    ],
    D=[
        arith("Teo se enojó 3 veces en la mañana y 2 en la tarde. Pausó antes de actuar en 4 de esas veces. ¿En cuántas veces no hizo pausa?", "3+2-4", "Primero se suman las veces enojado y luego se resta las que pausó."),
        ex("Tres conductas ante la rabia: 1) pegar, 2) decir con palabras que se enojó, 3) pedir un momento a solas. ¿Cuántas no dañan a nadie?", "2", "Las conductas 2 y 3 no lastiman."),
    ],
    context=[ex("Luis perdió en un juego y sintió mucha rabia. Dijo «estoy muy enojado, necesito un momento» y se sentó. Después felicitó al ganador. ¿Luis aceptó su emoción y cuidó a los demás?", "Sí", "Sintió la rabia, la expresó y no dañó a nadie.")],
    selfcheck=[ex("En Orientación: ¿las emociones son buenas o malas?", "Ninguna", "Todas dan información sobre lo que pasa."), ex("¿La conducta puede tener límites aunque la emoción sea fuerte?", "Sí", "No se puede dañar a nadie."), ex("¿Reparar es decir lo siento y ayudar a arreglar?", "Sí", "Así se hace cargo del daño.")],
    task=T("Lee: Eli está muy molesta porque otro niño usó sin permiso su estuche. Escribe tres cosas: la emoción que podría sentir, una conducta que dañaría y una conducta sin daño con la que podría expresarla. Agrega una frase que ella podría decir.", "Emoción: rabia. Conducta que dañaría: romper el estuche del otro. Conducta sin daño: decir qué le molestó. Frase: Me enojé porque usaste mi estuche sin pedir permiso.", ["distingue emoción de conducta", "propone una conducta sin daño", "escribe una frase que expresa la emoción"], ["texto escrito o dicho"], ["decir que la emoción es mala", "justificar el daño"], "Reconoce la emoción como válida y revisa que la conducta propuesta no lastime."),
    reinforce="Escribe una emoción de un personaje de cuento y dos cosas que podría hacer con ella sin dañar a nadie.",
    extend="Piensa en una conducta dañina que se justifique con una emoción y escribe qué conducta distinta podría elegirse.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. Un reloj o un contador de segundos solo si quieres practicar; los tiempos están escritos en los ejercicios.",
    "Aprenderé a esperar un tiempo y a probar estrategias que me ayudan a calmarme. Sirve para decidir qué hacer cuando una emoción es muy fuerte.",
    ["Sé que emoción y conducta son distintas.", "Sé que puedo hacer una pausa antes de actuar."],
    [
        "Cuando una emoción es muy fuerte, puede ser difícil pensar. Una estrategia es una forma de ayudarte a calmarte antes de actuar. Una muy útil es esperar un tiempo: hacer una pausa de uno o dos minutos antes de responder. Otra es respirar contando: inhalar por la nariz contando hasta 4 y soltar el aire contando hasta 4.",
        "Otras estrategias son alejarte un poco del conflicto, tomar un vaso de agua, mover los brazos con calma, dibujar lo que sientes o pedir ayuda a un adulto. No todas sirven a todas las personas. Por eso conviene probar y elegir las que a ti te ayudan. Todas deben ser seguras: no lastimar a nadie y no ponerte en peligro.",
        "Después de la pausa, vuelves a pensar: ¿qué pasó?, ¿qué siento?, ¿qué puedo hacer sin dañar? Esperar no es huir ni callarse para siempre. Es darle tiempo al cuerpo para calmarse y luego hablar. La intensidad de la emoción suele bajar con la pausa.",
    ],
    [("estrategia", "forma de ayudarme a calmarme y actuar mejor"), ("pausa", "detenerse un momento antes de actuar"), ("regulación", "calmar una emoción fuerte para decidir con calma"), ("respirar contando", "inhalar y soltar el aire contando hasta 4"), ("alejarse", "apartarse un poco de lo que me altera")],
    [
        W("Elegir una estrategia", "Ema siente rabia 5 porque un compañero rompió su dibujo. ¿Qué estrategia segura puede usar primero: gritarle o respirar contando hasta 4 y pedir un momento?", ["Gritar puede lastimar.", "Respirar y pedir un momento calma el cuerpo.", "Después podrá hablar."], "Respirar contando hasta 4 y pedir un momento"),
        W("Medir si ayudó", "Tomás tenía rabia 5. Después de una pausa de 2 minutos y de respirar contando, marcó rabia 2. ¿Cuántos puntos bajó?", ["Se compara la rabia de antes con la de después.", "5 menos 2.", "El número muestra si la estrategia ayudó."], "3 puntos"),
    ],
    [
        M("Pensar que esperar es lo mismo que huir.", "Se confunde la pausa con evitar el problema para siempre.", "Después de la pausa vuelves y hablas con calma."),
        M("Creer que una estrategia sirve igual a todas las personas.", "A cada cuerpo le ayuda algo distinto.", "Prueba varias y elige las que a ti te calman."),
    ],
    R=[
        ex("«Respirar contando hasta 4» ¿es una estrategia para calmarse?", "Sí", "Ayuda al cuerpo a bajar la intensidad."),
        ex("¿Esperar uno o dos minutos antes de responder es una pausa?", "Sí", "Es detenerse un momento antes de actuar."),
        ex("¿Gritarle a alguien es una estrategia segura para calmarse?", "No", "Puede lastimar a otro."),
    ],
    U=[
        ex("¿Por qué conviene probar varias estrategias?", "Porque no todas sirven a todas las personas", "Cada persona encuentra las que le ayudan."),
        ex("Después de la pausa, ¿qué haces: olvidar el problema o volver a pensar qué hacer?", "Volver a pensar qué hacer", "La pausa sirve para decidir mejor."),
        ex("¿Una estrategia puede ser caminar hacia un lugar peligroso para calmarse?", "No", "Toda estrategia debe ser segura."),
    ],
    A=[
        arith("Una niña respira contando 4 al inhalar y 4 al soltar. Repite esto 3 veces. ¿Cuántos números cuenta en total?", "(4+4)*3", "En cada vuelta cuenta 4 + 4 y se repite 3 veces."),
        ex("Pedro siente mucha pena y quiere llorar frente al curso. Elige una estrategia segura: «pedir permiso para tomar agua y respirar» o «salir corriendo del colegio».", "Pedir permiso para tomar agua y respirar", "Es segura y ayuda a calmarse."),
        ex("Lola tuvo rabia 4 y después de la pausa tuvo rabia 1. ¿La estrategia ayudó?", "Sí", "La intensidad bajó de 4 a 1."),
    ],
    Z=[
        ex("Un niño dice: «Respirar no me sirve, así que ninguna estrategia me sirve». ¿Qué le sugieres?", "Probar otras, como alejarse un momento o dibujar", "Hay varias estrategias y cada persona descubre las suyas."),
        ex("Una niña espera 1 minuto y vuelve a hablar con su compañero. Otro niño se aleja y no vuelve nunca. ¿Quién usó la pausa para resolver?", "La niña que volvió a hablar", "La pausa sirve para volver al problema con calma."),
    ],
    D=[
        arith("Una pausa dura 90 segundos. Si Ema hizo 2 pausas durante el día, ¿cuántos segundos esperó en total?", "90*2", "Son 90 segundos repetidos dos veces."),
        arith("Una escala de rabia va de 1 a 5. Teo marcó 5 y quiere llegar a 2 con pausas. Cada pausa le baja 1 punto. ¿Cuántas pausas necesita?", "5-2", "Debe bajar 3 puntos, uno por pausa."),
    ],
    context=[ex("Dos niños discuten por un asiento. Uno dice: «Necesito un minuto, ahora vuelvo y lo hablamos». Respira contando y regresa. ¿Usó una pausa segura?", "Sí", "Se calmó y volvió a resolver el problema.")],
    selfcheck=[ex("En Orientación: ¿esperar un tiempo es una estrategia de regulación?", "Sí", "La pausa ayuda a calmarse."), ex("¿Una estrategia puede lastimar a otra persona?", "No", "Debe ser siempre segura."), ex("¿Después de calmarte puedes volver a hablar del problema?", "Sí", "La pausa no evita hablar.")],
    task=T("Lee la situación: Nora está muy molesta porque en el juego le dijeron que perdió y no está de acuerdo. Elige dos estrategias de esta lista y escribe cómo las usaría: respirar contando hasta 4, pausa de 1 minuto, alejarse un poco, tomar agua, dibujar lo que siente, pedir ayuda a un adulto. Después escribe qué haría al volver.", "Estrategias: respirar contando hasta 4 y pausa de 1 minuto. Al volver diría: Quiero explicar por qué no estoy de acuerdo.", ["elige dos estrategias seguras", "dice cómo las usaría", "dice qué haría al volver"], ["texto escrito o dicho"], ["usar una estrategia que dañe", "no volver al problema"], "Reconoce las estrategias y pregunta cómo sabría si funcionó."),
    reinforce="Haz una lista de tres estrategias seguras que podrías probar. Marca cuál te parece más útil.",
    extend="Practica respirar contando hasta 4 durante 3 vueltas y anota si bajó tu intensidad de 1 a 5.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. Los diálogos y los casos están escritos en los ejercicios.",
    "Aprenderé a escuchar a otra persona de forma activa y a pensar en el impacto de lo que digo y hago. Sirve para entendernos mejor y para reparar cuando algo duele.",
    ["Sé que puedo hacer una pausa antes de actuar.", "Sé que mis acciones pueden afectar a otros."],
    [
        "Escuchar de verdad tiene tres pasos. Primero, esperas a que la otra persona termine, sin interrumpir. Segundo, reformulas: dices con tus palabras lo que entendiste. Tercero, preguntas con cuidado, por ejemplo «¿quieres contarme más?». Dar consejos al tiro o decir «no es para tanto» no es escuchar, porque le quita importancia a lo que el otro siente.",
        "El impacto es el efecto que tiene tu acción en otra persona. La intención es lo que tú querías. Pueden no coincidir: alguien puede bromear para reír juntos y que el otro se sienta mal. Para considerar el impacto, antes de hablar o actuar pregúntate cómo se podría sentir la otra persona. Después de actuar, escucha cómo se sintió.",
        "Si tu acción dolió, puedes reparar en tres pasos: reconoces lo que hiciste, dices lo siento y propones algo concreto para arreglarlo. Si te lastimaron a ti, no tienes que perdonar enseguida. Puedes decir cómo te sentiste, tomarte tu tiempo o pedir ayuda a una persona adulta de confianza.",
    ],
    [("escucha activa", "escuchar con atención y mostrar que entendí"), ("reformular", "decir con mis palabras lo que entendí"), ("impacto", "efecto de lo que hago en otra persona"), ("intención", "lo que quería lograr con lo que hice"), ("reparar", "arreglar un daño que causé")],
    [
        W("Ordenar los pasos de escuchar", "Ordena los pasos de la escucha: A) reformular, B) esperar a que termine, C) preguntar con cuidado.", ["Primero no se interrumpe: B.", "Luego se dice lo entendido: A.", "Al final se pregunta: C."], "B, A, C"),
        W("Intención e impacto", "Pedro quiso ayudar y cerró el cuaderno de Eli sin avisar; ella perdió la página en que escribía. ¿Cuál fue el impacto?", ["La intención de Pedro fue ayudar.", "Lo que le pasó a Eli es el impacto.", "Eli perdió su página."], "Eli perdió la página en que escribía"),
    ],
    [
        M("Pensar que si tuve buena intención, no pude lastimar a nadie.", "Se mira solo lo que yo quería.", "Pregunta cómo se sintió la otra persona."),
        M("Responder «no es para tanto» a quien cuenta una pena.", "Se cree que así lo consuelo.", "Reformula lo que dijo y pregunta si quiere contar más."),
    ],
    R=[
        ex("Cuando alguien habla, ¿qué haces primero: esperar a que termine o dar un consejo?", "Esperar a que termine", "Primero se escucha sin interrumpir."),
        ex("Reformular, ¿es repetir con mis palabras lo que entendí o decir mi opinión?", "Repetir con mis palabras lo que entendí", "Así el otro comprueba que lo entendieron."),
        ex("La intención de una acción, ¿es lo que yo quería o lo que sintió el otro?", "Lo que yo quería", "Lo que sintió el otro es el impacto."),
    ],
    U=[
        ex("¿Por qué «no es para tanto» no es una buena respuesta?", "Porque le quita importancia a lo que siente el otro", "No es escuchar sino juzgar."),
        ex("Una broma que causa pena, ¿tuvo un impacto bueno o doloroso para esa persona?", "Doloroso", "El impacto se mide por lo que vive el otro."),
        ex("Si te piden perdón, ¿tienes que perdonar en ese mismo momento?", "No", "Puedes tomarte el tiempo que necesites."),
    ],
    A=[
        ex("Dino dice: «Me da rabia que siempre me dejen para el final». ¿Qué frase reformula lo que dijo: «Entiendo que te da rabia que te dejen siempre para el final» o «Ya te va a tocar, no te enojes»?", "«Entiendo que te da rabia que te dejen siempre para el final»", "Repite lo entendido con otras palabras; la otra frase da un consejo y le quita importancia."),
        ex("Una disculpa tiene tres partes: lo que hice, lo siento y cómo reparo. Marta pisó sin querer el dibujo de Joaquín. ¿Qué disculpa tiene las tres partes: «Pisé tu dibujo sin querer, lo siento; te ayudo a hacerlo de nuevo» o «Fue sin querer, no te enojes»?", "«Pisé tu dibujo sin querer, lo siento; te ayudo a hacerlo de nuevo»", "Dice qué hizo, pide perdón y propone reparar."),
        ex("Antes de hacer una broma, ¿qué pregunta ayuda a pensar en el impacto: «¿cómo podría sentirse él?» o «¿cuántos se van a reír?»", "¿Cómo podría sentirse él?", "Piensa en el efecto sobre la persona."),
    ],
    Z=[
        ex("Un niño dice «lo siento» y a la hora repite la burla. ¿Reparó el daño?", "No", "Pidió perdón pero no cambió lo que hacía."),
        ex("Ana contó que estaba triste y su compañero cambió de tema. ¿Escuchó con atención?", "No", "No esperó, no reformuló y no preguntó."),
    ],
    D=[
        arith("En un taller de escucha hay 5 parejas. En cada pareja los dos hablan 3 minutos. ¿Cuántos minutos hablan en total entre todos?", "5*2*3", "Cada pareja tiene dos personas que hablan 3 minutos."),
        ex("Una broma divirtió a Tomás, a Ema y a Rita, pero a Leo le dio vergüenza. ¿Para cuántas personas el impacto fue doloroso?", "1", "Solo Leo se sintió mal."),
    ],
    context=[ex("En el recreo, Inés interrumpió a Joaquín y él se quedó callado. Inés dice: «Perdona, te interrumpí. ¿Quieres seguir con lo que decías?». ¿Reparó el impacto?", "Sí", "Reconoció lo que hizo y le devolvió la palabra.")],
    selfcheck=[ex("En Orientación: ¿escuchar es solo estar callado?", "No", "También es reformular y preguntar."), ex("¿Una disculpa con reparación es mejor que solo decir lo siento?", "Sí", "Se hace cargo del daño."), ex("¿Puedes pedir ayuda a un adulto de confianza si te lastimaron?", "Sí", "No tienes que resolverlo solo.")],
    task=T("Lee: Mía dice «Me dio pena que no me escogieran para el equipo». Escribe cómo reformularías lo que dijo y qué pregunta le harías. Después escribe una disculpa de tres partes para esta situación: sin querer pisaste el dibujo de un compañero y se arrugó.", "Reformulo: Entiendo que te dio pena no ser elegida. Pregunta: ¿Quieres contarme más? Disculpa: Pisé tu dibujo sin querer, lo siento; te ayudo a hacerlo de nuevo.", ["reformula sin juzgar", "hace una pregunta cuidadosa", "la disculpa tiene tres partes"], ["texto escrito o dicho"], ["dar consejos en vez de reformular", "disculpa sin reparar"], "Revisa que reformule sin juzgar y que la disculpa diga qué hizo y cómo repara."),
    reinforce="Escribe cómo escucharías a un compañero que está triste sin darle consejos.",
    extend="Piensa en una vez que lastimaste a alguien sin querer y escribe, sin dar nombres, qué harías hoy para reparar.",
)
