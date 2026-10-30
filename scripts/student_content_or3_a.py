"""Cuaderno del estudiante, 3.º básico Orientación: OA 01 (características, habilidades y fortalezas) y OA 02 (emociones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR03 OA 01", "OR03 OA 02"


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
    "Una hoja y un lápiz. Los perfiles de los niños están escritos en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a describir a una persona con hechos y evidencia, sin ponerle etiquetas. Sirve para conocer a los demás y a mí con respeto.",
    ["Sé que cada persona tiene características distintas.", "Sé decir un dato verdadero sobre alguien."],
    [
        "Una característica es un rasgo que dice cómo es una persona: lo que se nota por fuera, cómo actúa con otros o qué le gusta. Para decirla bien necesitas evidencia. La evidencia es algo que viste o escuchaste y que apoya lo que dices.",
        "Un hecho se puede observar: «Ema ayudó a juntar los lápices». Una etiqueta es una palabra fija que encierra a la persona: «Luis es un flojo». La etiqueta casi nunca tiene evidencia y no deja espacio para cambiar. Para describir sin etiquetar, parte del hecho y usa palabras como «hoy», «a veces» o «en esta tarea».",
        "Hay cosas íntimas, como lo que sientes o lo que pasa en tu familia. Las cuentas solo si quieres y a quien confíes. Nadie puede presionarte. En esta clase puedes hablar de un personaje o de gustos que no te incomodan, como que te gusta dibujar.",
    ],
    [("característica", "rasgo que dice cómo es una persona"), ("evidencia", "algo visto o escuchado que apoya lo que digo"), ("hecho", "algo que se puede observar"), ("etiqueta", "palabra fija que encierra a una persona"), ("íntimo", "algo muy personal que cada uno decide si cuenta")],
    [
        W("Hecho o etiqueta", "¿Cuál es un hecho: «Tomás es un miedoso» o «Tomás no quiso subir al columpio alto»?", ["Pregunta: ¿se puede observar?", "«No quiso subir al columpio alto» se vio.", "«Es un miedoso» es una palabra fija sobre Tomás."], "«Tomás no quiso subir al columpio alto»"),
        W("Reescribir sin etiqueta", "Un niño dijo «Pía es desordenada». Pía dejó la mochila abierta y se cayeron los lápices. Escribe la frase con el hecho.", ["Busca qué pasó: la mochila quedó abierta.", "Agrega la palabra «hoy» para no encerrar a Pía.", "Escribe el hecho."], "Hoy a Pía se le cayeron los lápices porque la mochila quedó abierta"),
    ],
    [
        M("Decir «Luis es un flojo» porque hoy no terminó.", "Un solo momento parece mostrar cómo es toda la persona.", "Cuenta el hecho: «Hoy Luis no alcanzó a terminar», y pregunta si necesita ayuda."),
        M("Contar algo íntimo porque un compañero insiste.", "Pensamos que hay que responder todas las preguntas.", "Puedes decir «prefiero no contarlo» y elegir otra característica."),
    ],
    R=[
        ex("«Rafa presta su goma a quien la necesita». ¿Es un hecho o una etiqueta?", "Un hecho", "Cuenta algo que Rafa hace y que se puede ver."),
        ex("«Fabiola es una niña mala». ¿Es un hecho o una etiqueta?", "Una etiqueta", "Es una palabra fija sin decir qué hizo Fabiola."),
        ex("«Lo vi esperar su turno tres veces». ¿Es evidencia de que alguien sabe esperar?", "Sí", "Es algo visto que apoya la característica."),
    ],
    U=[
        ex("¿Por qué «Luis es un flojo» no sirve para describir a Luis?", "Es una etiqueta sin evidencia", "No dice qué hizo y lo encierra en una palabra."),
        ex("¿Qué palabra deja espacio para cambiar: «hoy» o «siempre»?", "Hoy", "«Hoy» habla de un momento y no de toda la vida."),
        ex("Si te piden contar algo muy íntimo en clases, ¿estás obligado a contarlo?", "No", "Cada persona decide qué comparte."),
    ],
    A=[
        ex("Ema dibuja las nubes con muchos detalles y las colorea con cuidado. Escribe una característica de Ema con su evidencia.", "Es detallista, porque dibuja las nubes con muchos detalles", "Une la característica con algo que se vio."),
        ex("¿Cuál frase no etiqueta: «Joaquín es un llorón» o «Hoy Joaquín lloró cuando se rompió su dibujo»?", "«Hoy Joaquín lloró cuando se rompió su dibujo»", "Cuenta un hecho con su momento."),
        ex("Un compañero dijo «Sofía es rara porque le gusta hablar con las plantas». Reescribe la frase como un hecho.", "A Sofía le gusta hablar con las plantas", "Se quita el juicio «rara» y queda lo observado."),
    ],
    Z=[
        ex("Uno dice «Iván lee mal». Otra dice «Hoy Iván leyó un renglón con 3 errores». ¿Quién describe con evidencia?", "La que dice que leyó un renglón con 3 errores", "Da un dato concreto y no juzga a Iván."),
        ex("Una niña dice: «Prefiero no hablar de mi familia». ¿Se debe respetar su decisión?", "Sí", "Lo íntimo se cuenta solo si la persona quiere."),
    ],
    D=[
        arith("Esta semana Nora ayudó 4 veces, Beto 3 veces y Ana 5 veces a sus compañeros. ¿Cuántas veces ayudaron entre los tres?", "4+3+5", "Se suman las evidencias de cada niño."),
        ex("Evidencias sobre Lila: «prestó su regla», «esperó su turno», «gritó a Pía». ¿Cuántas apoyan que Lila trata con respeto?", "2", "Prestar y esperar muestran respeto; gritar no."),
    ],
    context=[ex("La profesora pide describir a una niña del cuento sin etiquetas. Sara dice: «Matilde es valiente: se acercó sola a pedir ayuda al conserje». ¿Sara usó evidencia?", "Sí", "Apoyó la característica con algo que Matilde hizo.")],
    selfcheck=[ex("En Orientación: ¿una etiqueta deja espacio para cambiar?", "No", "Encierra a la persona en una palabra."), ex("¿Un hecho se puede observar?", "Sí", "Se ve o se escucha."), ex("¿Debes contar algo íntimo si te lo piden?", "No", "Tú decides qué compartir.")],
    task=T("Lee los perfiles. Luz ayudó 3 veces a repartir hojas y dibuja flores. Teo esperó su turno y, cuando se equivocó, lo intentó otra vez. Mía invitó a jugar a una niña nueva. Elige a uno. Escribe dos hechos y una característica con evidencia, usando «hoy» o «a veces». No uses etiquetas.", "Teo: esperó su turno; se equivocó y lo intentó otra vez. Teo se esfuerza porque lo intentó otra vez.", ["escribe dos hechos observables", "une la característica con una evidencia", "no usa etiquetas ni cuenta algo íntimo"], ["texto escrito o dicho", "dibujo con una frase"], ["usar una etiqueta fija", "dar una característica sin evidencia"], "Reconoce los hechos y pregunta qué evidencia apoya la característica."),
    reinforce="Escribe tres hechos sobre un personaje de un cuento y una característica que ellos apoyan.",
    extend="Toma una etiqueta que hayas escuchado y reescríbela como un hecho con «hoy» o «a veces».",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. Las situaciones y las tablas de avance están escritas en los ejercicios.",
    "Aprenderé a reconocer mis habilidades con evidencia y a ver mi avance. Sirve para confiar en mí y saber qué puedo seguir mejorando.",
    ["Sé que una característica necesita evidencia.", "Sé que lo que practico mejora."],
    [
        "Una habilidad es algo que sabes hacer y puedes mejorar. Hay habilidades para aprender, como leer o resolver problemas. Hay habilidades con otros, como escuchar o invitar a jugar. Hay habilidades con los afectos, como consolar a alguien. Y hay habilidades para colaborar en tu casa, como ayudar a ordenar.",
        "Para reconocer una habilidad necesitas evidencia: algo que hiciste y que se puede mostrar. «Sé escuchar» se apoya con «el lunes esperé a que mi compañera terminara de hablar». También puedes mirar tu avance. Compara cómo te salía antes con cómo te sale ahora, no con otra persona.",
        "No todo lo que te gusta es una habilidad, y no todo lo que te cuesta es un defecto. Si algo te cuesta, todavía puedes aprenderlo. Reconocer tus habilidades no es presumir. Es saber con qué cuentas.",
    ],
    [("habilidad", "algo que sé hacer y puedo mejorar"), ("evidencia", "algo que hice y se puede mostrar"), ("avance", "mejora que se nota con el tiempo"), ("colaborar", "trabajar con otros para lograr algo"), ("presumir", "hablar de lo que sé para sentirse más que otros")],
    [
        W("Habilidad con evidencia", "Bruno dice «sé escuchar». Su evidencia es: «ayer esperé a que Camila terminara de hablar y luego respondí». ¿La evidencia apoya su habilidad?", ["Escuchar es esperar y entender lo que dice el otro.", "Bruno esperó y después respondió.", "Eso se hizo y se puede contar."], "Sí, la evidencia apoya su habilidad"),
        W("Medir el avance", "El lunes Tomás leyó 2 renglones sin trabarse. El viernes leyó 6. ¿Cuántos renglones más leyó sin trabarse?", ["Se compara a Tomás con él mismo.", "Viernes menos lunes: 6 menos 2.", "El resultado es el avance."], "4 renglones más"),
    ],
    [
        M("Pensar que reconocer mis habilidades es presumir.", "Se confunde hablar de lo que sé con sentirse más que otros.", "Di lo que sabes con evidencia y sin comparar."),
        M("Medir mi avance mirando a quien lo hace mejor.", "El otro lleva más práctica y eso desanima.", "Compara cómo te salía antes con cómo te sale hoy."),
    ],
    R=[
        ex("Ana se ata los cordones sola. ¿Es una habilidad?", "Sí", "Es algo que Ana sabe hacer."),
        ex("«Consolar a alguien que está triste» ¿es una habilidad con los afectos o para aprender?", "Con los afectos", "Se trata de acompañar lo que otro siente."),
        ex("¿Qué ayuda más a mejorar una habilidad: practicar con calma o esperar a que salga sola?", "Practicar con calma", "Repetir con atención permite avanzar."),
    ],
    U=[
        ex("¿Qué es la evidencia de una habilidad?", "Algo que hice y se puede mostrar", "Apoya lo que digo de mí con un hecho."),
        ex("Para ver si avanzas, ¿comparas tu antes y tu ahora o te comparas con el mejor del curso?", "Mi antes y mi ahora", "Así ves tu propia mejora."),
        ex("Si algo te cuesta hoy, ¿significa que nunca lo podrás hacer?", "No", "Con práctica y ayuda se puede aprender."),
    ],
    A=[
        arith("El lunes Pedro metió 3 pelotazos en el arco y el viernes 8. ¿Cuántos más metió el viernes?", "8-3", "El avance es la diferencia entre los dos días."),
        ex("Marta dice «sé ayudar». ¿Cuál es evidencia: «hoy ayudé a ordenar los libros de la sala» o «me gusta ayudar»?", "«Hoy ayudé a ordenar los libros de la sala»", "Cuenta algo hecho y no solo un gusto."),
        ex("Convierte «no sé armar rompecabezas» en una frase que deje espacio para aprender.", "Todavía no sé armar rompecabezas", "La palabra «todavía» recuerda que se puede aprender."),
    ],
    Z=[
        ex("Un niño dice: «Mi amiga canta mejor, así que yo no avanzo». ¿Qué dato le falta mirar?", "Cómo le salía a él antes", "El avance se mide con el propio punto de partida."),
        ex("Dos niñas dicen «soy buena para ayudar». Una cuenta que ayer ayudó a una compañera con su mochila y la otra no da ejemplos. ¿Cuál tiene evidencia?", "La que contó lo de la mochila", "Dio un hecho que se puede mostrar."),
    ],
    D=[
        arith("Una tabla dice: semana 1, 4 palabras bien escritas; semana 2, 7; semana 3, 10. ¿Cuántas palabras más escribió bien en la semana 3 que en la semana 1?", "10-4", "Se compara la semana 3 con la semana 1."),
        ex("Luis solo dice «soy bueno en todo». ¿Qué le falta para reconocer sus habilidades con evidencia?", "Ejemplos de cosas que hizo", "Sin hechos, la frase no se puede mostrar."),
    ],
    context=[ex("La profesora pide a cada niño decir una habilidad con evidencia. Rodrigo dice: «Sé trabajar en equipo: esta semana repartí las tareas y todos terminamos a tiempo». ¿Cumplió lo pedido?", "Sí", "Dijo una habilidad y la apoyó con algo que hizo.")],
    selfcheck=[ex("En Orientación: ¿puedes comparar tu avance contigo mismo?", "Sí", "Mirar tu antes y tu ahora es justo."), ex("¿Decir lo que sabes hacer, con evidencia, es presumir?", "No", "Es conocer con qué cuentas."), ex("¿Una habilidad puede mejorar con práctica?", "Sí", "Repetir con calma ayuda a avanzar.")],
    task=T("Elige tres habilidades de esta lista: leer en voz alta, escuchar a un compañero, ayudar a ordenar, consolar a alguien, trabajar en equipo, resolver un problema. Para cada una escribe o dibuja una evidencia. Si no tienes evidencia de una, escribe «todavía» y un primer paso.", "Escuchar a un compañero: ayer esperé a que mi compañera terminara de hablar. Resolver un problema: todavía; primer paso: pedir una pista.", ["elige tres habilidades de la lista", "cada una tiene evidencia o un «todavía» con paso", "no se compara con otras personas"], ["lista escrita o dibujada"], ["decir la habilidad sin evidencia", "compararse con otros"], "Reconoce las evidencias y propone un paso pequeño si falta alguna."),
    reinforce="Escribe una habilidad que hayas mejorado en este año y qué hiciste para mejorarla.",
    extend="Elige una habilidad de la lista que todavía no tengas y escribe dos cosas que podrías practicar.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. El caso del equipo está escrito en los ejercicios.",
    "Aprenderé a valorar mis fortalezas y las de otros, que son distintas. Sirve para trabajar en grupo sin competir.",
    ["Sé reconocer una habilidad con evidencia.", "Sé que cada persona es distinta."],
    [
        "Una fortaleza es una habilidad o una forma de ser que te ayuda y que también ayuda a otros. Hay fortalezas en lo académico, como ser curioso. Hay fortalezas sociales, como invitar a alguien a jugar. Hay fortalezas afectivas, como ser cariñoso. Y hay fortalezas para colaborar en tu casa, como cuidar tus cosas.",
        "Valorar es reconocer que algo tiene importancia. Piensa en un equipo que arma un mural. Una niña dibuja, un niño ordena los colores y otra escucha las ideas de todos. Nadie es «el mejor». Sin cualquiera de las tres cosas, el mural sería más difícil.",
        "Comparar para saber quién gana suele dejar a alguien triste. Una frase que valora dice qué hizo la persona: «Me gusta cómo explicas» o «Gracias por esperar». No pone a nadie arriba ni abajo. Tú también puedes valorar tus fortalezas sin que otro tenga menos.",
    ],
    [("fortaleza", "habilidad o forma de ser que ayuda a mí y a otros"), ("valorar", "reconocer que algo tiene importancia"), ("aportar", "dar algo que ayuda al grupo"), ("diversidad", "que las personas somos distintas"), ("afectivo", "que tiene que ver con lo que sentimos por otros")],
    [
        W("Frase que valora", "¿Qué frase valora a Mía: «Dibujas mejor que todos» o «Me gusta cómo pintas el cielo»?", ["La primera pone a Mía sobre los demás.", "La segunda dice lo que Mía hace.", "Valorar es mirar lo que la persona aporta."], "«Me gusta cómo pintas el cielo»"),
        W("Aportes distintos", "En un mural, Ana dibuja, Beto ordena los colores y Cata escucha las ideas. ¿Cuántos aportes distintos hay?", ["Ana aporta dibujo.", "Beto aporta orden.", "Cata aporta escucha. Se cuentan: 1, 2, 3."], "3 aportes distintos"),
    ],
    [
        M("Pensar que valorar a otro me hace menos a mí.", "Se cree que el reconocimiento es una competencia.", "Reconocer a otro no quita nada de lo que tú vales."),
        M("Creer que solo cuentan las fortalezas de las notas.", "Se olvida que ayudar, escuchar y cuidar también son fortalezas.", "Mira fortalezas académicas, sociales, afectivas y de colaboración."),
    ],
    R=[
        ex("¿Valorar es decir quién gana o reconocer lo que alguien aporta?", "Reconocer lo que alguien aporta", "Valorar no es competir."),
        ex("Beto ordena los colores del mural. ¿Su aporte sirve al grupo?", "Sí", "El orden ayuda a que el trabajo salga."),
        ex("«Gracias por esperar» ¿es una frase que valora?", "Sí", "Reconoce algo que la persona hizo."),
    ],
    U=[
        ex("«Consolar a un compañero triste» ¿es una fortaleza afectiva o académica?", "Afectiva", "Tiene que ver con lo que sentimos por otros."),
        ex("¿Por qué «tú eres el mejor del curso» no valora bien?", "Pone a una persona sobre las otras", "Valorar mira lo que cada uno aporta."),
        ex("¿Cuidar tus cosas en tu casa puede ser una fortaleza?", "Sí", "Colaborar en casa también ayuda a otros."),
    ],
    A=[
        ex("Escribe una frase que valore a Pablo, que siempre explica con calma cómo se hace un ejercicio.", "Me gusta cómo explicas con calma", "Dice qué hace Pablo y no lo compara."),
        ex("Un equipo tiene a Rita que escucha ideas, a Sol que busca información y a Lalo que anima al grupo. ¿Quién muestra una fortaleza académica, como ser curiosa?", "Sol", "Buscar información tiene que ver con aprender."),
        ex("Un amigo dice: «Yo no tengo fortalezas». Nombra una fortaleza de cualquier tipo que él podría tener.", "Por ejemplo, ser leal, curioso o ayudador", "Todas las personas tienen fortalezas distintas."),
    ],
    Z=[
        ex("En un grupo, alguien dice: «Solo vale quien saca buenas notas». ¿Esa idea valora la diversidad?", "No", "Deja afuera fortalezas sociales y afectivas."),
        ex("Dos niños dibujan igual de bien, y uno dice que el otro no vale. ¿Qué podría decirse para valorar a los dos?", "Que cada uno dibuja a su manera y aporta algo", "Valorar no es elegir a un ganador."),
    ],
    D=[
        arith("En un taller de 24 niños, 9 prefieren dibujar y 8 prefieren cantar. El resto prefiere construir. ¿Cuántos prefieren construir?", "24-9-8", "Se restan los que dibujan y los que cantan al total."),
        ex("En el mismo taller, ¿es importante que haya niños que dibujen, que canten y que construyan?", "Sí, porque cada grupo aporta algo distinto", "La diversidad de fortalezas enriquece al grupo."),
    ],
    context=[ex("Para la fiesta del curso, Julia propone ideas, Tomás hace carteles y Elena avisa a los demás. Alguien dice: «Julia es la más importante». ¿Es correcto?", "No", "Cada una hace un aporte que el grupo necesita.")],
    selfcheck=[ex("En Orientación: ¿valorar a otro me quita valor a mí?", "No", "El reconocimiento no es una competencia."), ex("¿Todas las personas tienen fortalezas?", "Sí", "Cada uno tiene las suyas."), ex("¿Una fortaleza puede ser afectiva?", "Sí", "Cuidar y consolar ayudan a otros.")],
    task=T("Mira esta lista de fortalezas: curioso, cariñoso, ordenado, animar al grupo, escuchar, explicar con calma. Elige dos que veas en alguien (puede ser un personaje o un compañero que acepte) y una que reconozcas en ti. Escribe una frase que valore a esa persona, usando «me gusta cómo…» o «gracias por…».", "Escuchar: «Gracias por escuchar mis ideas». Explicar con calma: «Me gusta cómo explicas».", ["elige fortalezas de la lista", "la frase dice qué hizo la persona", "no compara ni pone a nadie sobre otro"], ["frases escritas o dichas"], ["comparar para ver quién es mejor", "valorar solo las notas"], "Reconoce las frases y revisa que digan qué hizo la persona."),
    reinforce="Escribe una fortaleza de alguien de tu curso o de un personaje y cómo ayuda al grupo.",
    extend="Escribe una fortaleza tuya de cada tipo: académica, social, afectiva y de colaboración. Si no encuentras alguna, escribe «todavía».",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. Las metas de ejemplo están escritas en los ejercicios.",
    "Aprenderé a proponerme una meta de mejora concreta y pequeña. Sirve para mejorar paso a paso sin sentirme mal por lo que me cuesta.",
    ["Sé reconocer mis habilidades y fortalezas.", "Sé que lo que me cuesta puedo mejorarlo."],
    [
        "Una meta es algo que quieres lograr. «Mejorar» es una meta muy grande y poco clara. Una meta concreta dice qué vas a hacer, cuánto y por cuánto tiempo. Por ejemplo: «leer 10 minutos al día durante una semana». Así sabes si la cumpliste.",
        "Una acción es lo que haces para llegar a la meta. Elige una acción pequeña que sí puedas hacer. También puedes pedir ayuda a una persona de confianza, y revisar tu avance al final de la semana. Si no salió, no pasa nada: cambias la acción o la haces más pequeña.",
        "Las metas son sobre lo que tú haces, como practicar, preguntar o ordenar tus cosas. No son para cambiar tu cuerpo ni para parecerte a otra persona. Mejorar es aprender algo nuevo, no ser perfecto.",
    ],
    [("meta", "lo que quiero lograr"), ("acción", "lo que hago para lograr la meta"), ("concreto", "claro y que se puede medir"), ("plazo", "tiempo en que quiero lograr algo"), ("progreso", "avance hacia la meta")],
    [
        W("Meta concreta", "¿Cuál meta es concreta: «mejorar en lectura» o «leer 10 minutos al día durante una semana»?", ["Una meta concreta dice qué, cuánto y cuándo.", "La segunda dice qué (leer), cuánto (10 minutos) y cuándo (una semana).", "La primera es muy general."], "«Leer 10 minutos al día durante una semana»"),
        W("Revisar el avance", "Lía se propuso practicar 15 minutos de cuerda por día durante 4 días. Practicó 3 días. ¿Cuántos días le faltaron?", ["Meta: 4 días.", "Cumplió 3.", "Faltó 4 menos 3."], "1 día"),
    ],
    [
        M("Ponerme una meta muy grande, como «ser el mejor».", "Parece motivante, pero no se sabe qué hacer ni cuándo se cumple.", "Escribe qué, cuánto y por cuánto tiempo."),
        M("Pensar que si no cumplí la meta soy un fracaso.", "Se confunde la meta con el valor de la persona.", "Revisa qué pasó y cambia la acción o hazla más pequeña."),
    ],
    R=[
        ex("¿Una meta concreta dice qué, cuánto y cuándo, o solo «mejorar»?", "Dice qué, cuánto y cuándo", "Así se puede saber si se cumplió."),
        ex("¿La «acción» es lo que hago o lo que quiero lograr?", "Lo que hago", "La acción es el paso que llevo a cabo."),
        ex("Si no cumpliste una meta, ¿qué puedes hacer: abandonar o cambiar la acción?", "Cambiar la acción", "Ajustar permite seguir avanzando."),
    ],
    U=[
        ex("¿Por qué «ser el mejor» no es una buena meta de mejora?", "Porque no dice qué hacer ni cuándo se cumple", "No es concreta y compara con otros."),
        ex("¿Una meta de mejora puede ser cambiar mi cuerpo?", "No", "Las metas son sobre lo que yo hago, como practicar."),
        ex("¿Pedir ayuda a una persona de confianza puede ser parte del plan?", "Sí", "Con apoyo es más fácil avanzar."),
    ],
    A=[
        ex("Quieres mejorar tu letra. Escribe una meta concreta usando «cada día» y un plazo.", "Copiar una línea con letra clara cada día durante una semana", "Dice qué, cuánto y por cuánto tiempo."),
        arith("Mateo quiere ordenar su mochila 5 días seguidos y ya lo hizo 2 días. ¿Cuántos días le faltan?", "5-2", "Se restan los días cumplidos a los de la meta."),
        ex("¿Cuál acción es más pequeña y posible: «estudiar todo el día» o «repasar mis tablas 5 minutos»?", "Repasar mis tablas 5 minutos", "Una acción pequeña es más fácil de cumplir."),
    ],
    Z=[
        ex("Ema se propuso «leer mejor» y al final no sabe si lo logró. ¿Qué le faltó a su meta?", "Ser concreta: qué, cuánto y cuándo", "Sin datos no se puede medir el avance."),
        ex("Rafa no cumplió su meta de leer 20 minutos. Cambió a 10 minutos y lo logró. ¿Hizo trampa?", "No, ajustó la acción", "Cambiar a una acción posible es parte de mejorar."),
    ],
    D=[
        arith("Una meta dice: leer 10 minutos por día durante 6 días. ¿Cuántos minutos serían en total?", "10*6", "Se repite 10 minutos seis veces."),
        ex("Una niña quiere mejorar en escuchar. ¿Cuál plan tiene meta, acción y plazo: «ser mejor persona» o «esta semana, esperar a que mi compañero termine antes de hablar»?", "«Esta semana, esperar a que mi compañero termine antes de hablar»", "Tiene una acción clara y un plazo."),
    ],
    context=[ex("En una reunión de curso, Camilo dice: «Mi meta es llegar con mis útiles listos los lunes, durante tres semanas». ¿Su meta es concreta?", "Sí", "Dice qué, cuándo y por cuánto tiempo.")],
    selfcheck=[ex("En Orientación: ¿una meta puede ser pequeña?", "Sí", "Lo pequeño se puede cumplir."), ex("¿Las metas son para cambiar mi cuerpo?", "No", "Son sobre lo que yo hago y aprendo."), ex("¿Revisar mi avance sirve?", "Sí", "Permite ajustar la acción.")],
    task=T("Elige un aspecto de esta lista: terminar mis tareas, escuchar sin interrumpir, ordenar mi mochila, leer más. Escribe una meta con qué, cuánto y cuándo; una acción pequeña; y a quién pedirías ayuda. Al final de la semana, escribe si la cumpliste y qué cambiarías.", "Escuchar sin interrumpir: esta semana, levantar la mano antes de hablar en cada conversación. Pido ayuda a mi profesora.", ["meta con qué, cuánto y cuándo", "acción pequeña y posible", "no habla de cambiar el cuerpo ni de compararse"], ["meta escrita en la hoja"], ["metas demasiado grandes", "metas sobre el cuerpo o sobre ganarle a otros"], "Reconoce la meta y propone hacerla más pequeña si es muy grande."),
    reinforce="Convierte «quiero mejorar» en una meta concreta sobre algo de tu aprendizaje.",
    extend="Escribe un plan de tres pasos pequeños para lograr tu meta y cómo sabrás que avanzas.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. Las situaciones y las tarjetas de emociones están escritas en los ejercicios.",
    "Aprenderé a distinguir la emoción, la sensación del cuerpo y lo que hago. Sirve para entender lo que siento y no adivinar lo que sienten otros.",
    ["Sé nombrar emociones como alegría, miedo o pena.", "Sé que mis sensaciones cambian."],
    [
        "Una emoción es lo que sientes ante algo que pasa: alegría, rabia, miedo, pena, sorpresa, vergüenza. Una sensación es lo que notas en el cuerpo, como el corazón rápido, las manos frías o un nudo en la guata. Una conducta es lo que haces: gritar, quedarte quieto, llorar, abrazar.",
        "Estas tres cosas se mezclan, pero no son lo mismo. Puedes sentir rabia (emoción), notar calor en la cara (sensación) y decidir respirar profundo (conducta). La emoción aparece sola. La conducta sí se puede elegir.",
        "Las señales de otros te dan pistas, pero no certezas. Si alguien baja la mirada, puede tener pena, vergüenza o solo sueño. Para saber, puedes preguntar con respeto: «¿Cómo te sientes?». Y si no quiere contestar, se respeta.",
    ],
    [("emoción", "lo que siento ante algo que pasa"), ("sensación", "lo que noto en el cuerpo"), ("conducta", "lo que hago"), ("señal", "pista que muestra algo, pero no es una certeza"), ("intensidad", "qué tan fuerte es lo que siento")],
    [
        W("Tres cosas distintas", "Cuando Pía perdió su lápiz, sintió rabia, le dio calor en la cara y tiró la goma. ¿Cuál es la emoción?", ["Rabia es lo que siente.", "Calor en la cara es del cuerpo: sensación.", "Tirar la goma es lo que hace: conducta."], "La rabia"),
        W("Señal sin certeza", "Un niño mira al suelo en el recreo. ¿Puedes saber con seguridad que está triste?", ["Mirar al suelo es una señal.", "Puede ser pena, vergüenza o cansancio.", "Para saber, hay que preguntar con respeto."], "No, solo puedo preguntarle"),
    ],
    [
        M("Pensar que sé lo que siente otro por su cara.", "Las señales parecen claras, pero pueden significar varias cosas.", "Pregunta con respeto y acepta si no quiere contar."),
        M("Creer que emoción y conducta son lo mismo.", "Se piensa que sentir rabia obliga a gritar.", "La emoción aparece sola, la conducta se puede elegir."),
    ],
    R=[
        ex("«Corazón rápido» ¿es una emoción o una sensación del cuerpo?", "Una sensación del cuerpo", "Se nota en el cuerpo."),
        ex("«Gritar» ¿es una emoción o una conducta?", "Una conducta", "Es algo que se hace."),
        ex("«Miedo» ¿es emoción, sensación o conducta?", "Emoción", "Es lo que se siente ante algo."),
    ],
    U=[
        ex("¿Qué se puede elegir: la emoción o la conducta?", "La conducta", "La emoción aparece sola y la conducta se decide."),
        ex("Si un compañero tiene la cabeza gacha, ¿es seguro que siente pena?", "No", "Es una señal que puede tener varios significados."),
        ex("¿Cómo puedes saber cómo se siente alguien: adivinando o preguntando con respeto?", "Preguntando con respeto", "Solo la persona sabe lo que siente."),
    ],
    A=[
        ex("Tomás tiene las manos frías, el estómago apretado y siente miedo antes de pasar adelante. ¿Cuál es la emoción?", "Miedo", "Manos frías y estómago apretado son sensaciones."),
        ex("Clasifica «llorar»: ¿emoción, sensación o conducta?", "Conducta", "Es algo que la persona hace."),
        ex("Escribe una pregunta respetuosa para saber cómo se siente Nico, que está callado.", "¿Cómo te sientes?", "Una pregunta abierta deja que Nico elija si contesta."),
    ],
    Z=[
        ex("Dos niños sienten rabia. Uno respira y el otro empuja. ¿Qué cambió entre ellos: la emoción o la conducta?", "La conducta", "Los dos sienten lo mismo, pero actúan distinto."),
        ex("Una niña dice: «Mi compañera frunció el ceño, así que está enojada conmigo». ¿Eso es seguro?", "No", "Fruncir el ceño tiene muchos posibles motivos."),
    ],
    D=[
        arith("Una niña anotó 3 emociones en la mañana y 4 en la tarde. ¿Cuántas anotó en total?", "3+4", "Se suman las emociones de las dos partes del día."),
        ex("Una tarjeta dice: «Me sudan las manos, siento vergüenza y me escondo detrás de la puerta». ¿Cuántas cosas distintas hay: sensación, emoción y conducta?", "3", "Sudar es sensación, vergüenza es emoción y esconderse es conducta."),
    ],
    context=[ex("En el recreo, una niña nueva está sola y mira al suelo. Una compañera le pregunta: «¿Quieres jugar o prefieres estar tranquila?». ¿Respetó lo que siente?", "Sí", "Preguntó y le dio opciones sin adivinar.")],
    selfcheck=[ex("En Orientación: ¿una sensación se nota en el cuerpo?", "Sí", "Por ejemplo, el corazón rápido."), ex("¿Una señal siempre dice con certeza lo que siente alguien?", "No", "Solo da una pista."), ex("¿Puedes elegir qué haces cuando sientes rabia?", "Sí", "La conducta se puede elegir.")],
    task=T("Lee la tarjeta de Sol: «Perdí en el juego, sentí rabia, me ardió la cara y me quedé sin hablar». Escribe o dibuja la emoción, la sensación y la conducta. Después escribe una pregunta respetuosa que podrías hacerle a un compañero que se ve callado.", "Emoción: rabia. Sensación: cara caliente. Conducta: quedarse sin hablar. Pregunta: «¿Cómo te sientes?».", ["separa emoción, sensación y conducta", "la pregunta no adivina ni obliga a contar", "no clasifica la emoción como mala"], ["tres respuestas escritas o dibujadas"], ["confundir emoción con conducta", "afirmar lo que siente otro"], "Reconoce la separación y revisa que la pregunta no suponga nada."),
    reinforce="Escribe una emoción de hoy, qué notaste en tu cuerpo y qué hiciste. Cuenta solo lo que quieras.",
    extend="Elige una película o cuento y separa emoción, sensación y conducta de un personaje.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. Las tarjetas de situaciones están escritas en los ejercicios.",
    "Aprenderé que todas las emociones se pueden sentir y que algunas conductas hay que limitar porque dañan. Sirve para sentir sin lastimar.",
    ["Sé separar emoción, sensación y conducta.", "Sé que puedo elegir qué hago."],
    [
        "Todas las emociones son válidas. La rabia, el miedo y la pena no son buenas ni malas. Son parte de ser persona y tienen información: la rabia puede decir «algo me parece injusto»; el miedo, «necesito cuidarme».",
        "Lo que sí tiene límites es la conducta. Puedo sentir rabia, pero no puedo golpear, insultar ni romper las cosas de otros, porque eso daña. Aceptar una emoción es decir «lo que siento está bien». Limitar la conducta es decir «no lo voy a expresar de una forma que lastime».",
        "Hay maneras de expresar una emoción sin dañar: decirla con palabras («me enojé porque…»), pedir una pausa, dibujar, mover el cuerpo con calma o buscar a un adulto de confianza. Si una emoción es muy fuerte o te dura mucho, avisar a una persona adulta de confianza también es cuidarte.",
    ],
    [("aceptar", "reconocer que lo que siento es válido"), ("límite", "lo que no puedo hacer porque daña"), ("válido", "que tiene derecho a existir"), ("expresar", "mostrar lo que siento"), ("dañar", "hacer mal a alguien o a algo")],
    [
        W("Emoción y conducta", "Lola siente rabia porque rompieron su torre de bloques. ¿Qué parte está bien y qué parte necesita límite si ella pega?", ["Sentir rabia está bien.", "Pegar daña a alguien.", "La emoción se acepta y la conducta se limita."], "La rabia se acepta; pegar no está bien"),
        W("Expresar sin dañar", "Beto está enojado. Puede gritar un insulto o decir «me enojé porque me quitaron el lápiz». ¿Cuál no daña?", ["El insulto lastima a otro.", "La frase con «me enojé porque…» dice lo que siente.", "No daña a nadie."], "Decir «me enojé porque me quitaron el lápiz»"),
    ],
    [
        M("Pensar que sentir rabia es malo.", "A veces escuchamos que hay emociones prohibidas.", "Toda emoción es válida, lo que se limita es la conducta que daña."),
        M("Aguantar una emoción fuerte sin avisar a nadie.", "Pensamos que debemos arreglarlo solos.", "Si es muy fuerte o dura mucho, avisa a un adulto de confianza."),
    ],
    R=[
        ex("¿La rabia es una emoción buena o mala?", "Ninguna de las dos; es válida", "Toda emoción es parte de ser persona."),
        ex("«Pegar» ¿es una conducta que se debe limitar?", "Sí", "Daña a otra persona."),
        ex("¿Decir «me enojé porque…» daña a alguien?", "No", "Expresa la emoción con palabras."),
    ],
    U=[
        ex("¿Qué se acepta y qué se limita: la emoción o la conducta que daña?", "La emoción se acepta y la conducta que daña se limita", "Sentir es válido; dañar no."),
        ex("Si una emoción es muy fuerte y dura mucho, ¿qué es una buena idea?", "Avisar a un adulto de confianza", "Pedir ayuda también es cuidarse."),
        ex("¿Una emoción puede dar información sobre lo que necesitamos?", "Sí", "Por ejemplo, el miedo dice que debo cuidarme."),
    ],
    A=[
        ex("Rita se enoja y rompe el cuaderno de su compañero. ¿Qué conducta se debe limitar?", "Romper el cuaderno", "Daña las cosas de otra persona."),
        ex("Elige una forma de expresar la pena sin dañar: dar un portazo, dibujar lo que siento o decir un insulto.", "Dibujar lo que siento", "Expresa la emoción sin lastimar."),
        ex("Escribe una frase con «me dio… porque…» para contar que te dio vergüenza equivocarte frente al curso.", "Me dio vergüenza porque me equivoqué frente al curso", "Nombra la emoción y el motivo."),
    ],
    Z=[
        ex("Un niño dice: «Si siento rabia, tengo derecho a pegar». ¿Qué parte es cierta y cuál no?", "Tiene derecho a sentir rabia, pero no a pegar", "La emoción es válida; la conducta que daña no."),
        ex("Una niña llora mucho y le dicen «deja de llorar, no es para tanto». ¿Aceptaron su emoción?", "No", "Le dijeron que su emoción no valía."),
    ],
    D=[
        arith("En la semana, 5 niños pidieron una pausa, 3 dibujaron y 2 hablaron con la profesora. ¿Cuántos usaron una forma de expresar sin dañar?", "5+3+2", "Todas son formas que no dañan; se suman."),
        ex("Una tarjeta dice: «Siento envidia porque otra niña ganó. No le hago nada». ¿Aceptó la emoción y limitó la conducta?", "Sí", "Reconoció lo que sentía y no dañó a nadie."),
    ],
    context=[ex("En el patio, Mario siente mucha rabia porque lo sacaron del juego. Respira, dice «me enojé» y se sienta un rato. ¿Aceptó su emoción sin dañar?", "Sí", "Sintió la rabia y eligió una conducta que no lastima.")],
    selfcheck=[ex("En Orientación: ¿todas las emociones son válidas?", "Sí", "Ninguna está prohibida."), ex("¿Se puede pegar porque se siente rabia?", "No", "Pegar daña a otro."), ex("¿Pedir ayuda a un adulto de confianza ayuda con una emoción muy fuerte?", "Sí", "Acompañar ayuda a calmarse.")],
    task=T("Lee las situaciones: (1) le quitaron su turno en el columpio, (2) el dibujo se mojó, (3) no la invitaron a jugar. Elige una. Escribe la emoción que podría sentir, una conducta que dañaría y una forma de expresarla sin dañar.", "(2) El dibujo se mojó: pena. Dañaría tirar el dibujo de otro. Sin dañar: decir «me da pena que se mojó» y pedir una hoja nueva.", ["acepta la emoción como válida", "nombra una conducta que daña y otra que no", "no culpa a la persona"], ["frases escritas o dibujadas"], ["decir que la emoción es mala", "sugerir una conducta que lastima"], "Reconoce la aceptación de la emoción y pregunta qué conducta cuidaría a todos."),
    reinforce="Cuenta qué hiciste la última vez que sentiste una emoción fuerte y si dañó a alguien.",
    extend="Escribe dos maneras de expresar la rabia sin dañar y una forma de pedir ayuda.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. Las estrategias y los casos están escritos en los ejercicios. Puedes practicar la respiración sentado.",
    "Aprenderé a esperar un momento y a calmarme con estrategias simples. Sirve para decidir qué hago cuando siento algo fuerte.",
    ["Sé que puedo elegir mi conducta.", "Sé que todas las emociones son válidas."],
    [
        "Esperar un tiempo antes de actuar ayuda a pensar. Cuando sientes una emoción muy fuerte, el cuerpo se acelera. Si esperas un poco, te calmas y decides mejor. Eso se llama regulación: manejar lo que siento para no dañar ni dañarme.",
        "Hay estrategias que puedes usar. Respirar: sacas el aire despacio, como si soplaras una vela. Contar hasta diez antes de hablar. Pedir una pausa y alejarte un rato. Mover el cuerpo con calma, como estirarte. O decir en voz baja lo que sientes.",
        "No todas las estrategias sirven igual para todos. Tú puedes probar y elegir las tuyas. Si una no te resulta, pruebas otra. Si pasas la pausa y sigues muy mal, pides ayuda a un adulto de confianza.",
    ],
    [("regulación", "manejar lo que siento para decidir qué hago"), ("estrategia", "forma de hacer algo para lograr un objetivo"), ("pausa", "detenerse un momento antes de seguir"), ("respirar", "tomar y sacar el aire despacio"), ("calmarse", "volver a estar más tranquilo")],
    [
        W("Orden de pasos", "Dani siente mucha rabia. Los pasos son: (a) hablar de lo que pasó, (b) respirar despacio, (c) notar que siente rabia. ¿Cuál es un buen orden?", ["Primero noto lo que siento.", "Luego respiro para calmarme.", "Al final hablo con calma."], "c, b, a"),
        W("Contar la respiración", "Una niña respira así: 4 segundos para tomar aire y 6 para sacarlo. ¿Cuántos segundos dura una respiración completa?", ["Toma aire: 4 segundos.", "Saca aire: 6 segundos.", "Se suman 4 más 6."], "10 segundos"),
    ],
    [
        M("Decidir lo que voy a hacer justo cuando siento la emoción más fuerte.", "Con la emoción al máximo cuesta pensar.", "Haz una pausa y espera antes de decidir."),
        M("Creer que una estrategia debe servirle a todos igual.", "Pensamos que hay una sola receta.", "Prueba varias y elige las que te sirven."),
    ],
    R=[
        ex("¿Respirar despacio ayuda a calmarse?", "Sí", "Le da tiempo al cuerpo para bajar la intensidad."),
        ex("Cuando sientes una emoción muy fuerte, ¿conviene decidir enseguida o esperar un poco?", "Esperar un poco", "Con calma se decide mejor."),
        ex("¿Pedir una pausa es una estrategia?", "Sí", "Permite alejarse un momento para calmarse."),
    ],
    U=[
        ex("¿Qué es la regulación de las emociones?", "Manejar lo que siento para decidir qué hago", "No es no sentir, es elegir cómo actuar."),
        ex("Si una estrategia no te resulta, ¿qué haces?", "Pruebo otra", "No hay una sola receta."),
        ex("Si después de la pausa sigues muy mal, ¿qué conviene?", "Pedir ayuda a un adulto de confianza", "Acompañarte ayuda a calmarte."),
    ],
    A=[
        arith("Rosa respira 3 veces. Cada respiración dura 10 segundos. ¿Cuántos segundos respira en total?", "3*10", "Se repite 10 segundos tres veces."),
        ex("Tomás cuenta hasta diez antes de contestar. ¿Qué estrategia usa?", "Esperar un tiempo contando", "Cuenta para hacer una pausa antes de actuar."),
        ex("Escribe una frase para pedir una pausa en el juego.", "Necesito una pausa un momento", "Dice lo que necesitas sin culpar a nadie."),
    ],
    Z=[
        ex("Dos niñas se enojan. Una respira y espera; la otra grita enseguida. ¿Cuál tuvo más tiempo para decidir?", "La que respira y espera", "La pausa le dio tiempo para pensar."),
        ex("Un niño dice: «Respirar a mí no me sirve». ¿Qué le puedes decir?", "Que pruebe otra estrategia, como contar o moverse con calma", "Cada persona encuentra las que le sirven."),
    ],
    D=[
        ex("Ordena con letras, de primera a última acción: a) avisar a un adulto si sigo muy mal, b) notar que mi cuerpo está acelerado, c) respirar despacio.", "b, c, a", "Primero noto, luego me calmo y si sigo mal pido ayuda."),
        arith("Una pausa dura 2 minutos. Beto hizo 4 pausas en la semana. ¿Cuántos minutos de pausa fueron?", "2*4", "Se repiten 2 minutos cuatro veces."),
    ],
    context=[ex("En clase, a Laura le salió mal un ejercicio y siente que le sube la rabia. Pide permiso, toma agua, respira y vuelve. ¿Usó una estrategia de regulación?", "Sí", "Hizo una pausa para calmarse antes de seguir.")],
    selfcheck=[ex("En Orientación: ¿esperar un tiempo ayuda a decidir mejor?", "Sí", "El cuerpo se calma y se piensa mejor."), ex("¿Hay una sola estrategia para todos?", "No", "Cada uno prueba y elige."), ex("¿Se puede pedir una pausa?", "Sí", "Es una forma de cuidarse.")],
    task=T("Lee las estrategias: respirar despacio, contar hasta diez, pedir una pausa, estirar el cuerpo, decir en voz baja lo que siento. Prueba dos en este momento y escribe cuál te dejó más tranquilo y cuándo la usarías. Si ninguna te sirve, escribe una idea tuya.", "Probé respirar despacio y estirar el cuerpo. Respirar me calmó más; la usaría cuando me enojo en el recreo.", ["prueba al menos dos estrategias", "dice cuál le sirve y cuándo usarla", "acepta que a otros les sirva otra"], ["registro escrito o dibujado"], ["decir que su estrategia es la única", "no probar ninguna"], "Reconoce la elección y pregunta cómo avisaría si la emoción sigue fuerte."),
    reinforce="Practica tres respiraciones lentas y escribe cómo te sientes antes y después.",
    extend="Inventa una estrategia propia para calmarte y explica cuándo la usarías.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. Las conversaciones están escritas en los ejercicios. Puedes hacer los diálogos con un compañero o por escrito.",
    "Aprenderé a escuchar a otros y a pensar cómo mis acciones los afectan. Sirve para cuidar a los demás y arreglar cuando algo salió mal.",
    ["Sé nombrar lo que siento.", "Sé hacer una pausa."],
    [
        "Escuchar es más que estar callado. Escuchar bien es mirar a la persona, esperar a que termine, y luego decir con tus palabras lo que entendiste: «Entiendo que te dio pena que no te invitáramos». No es dar consejos ni decir que su emoción es exagerada.",
        "El impacto es el efecto que tienen mis acciones en otros. Puedo tener una buena intención y aun así lastimar. Por eso, después de actuar, me pregunto: ¿cómo se sintió la otra persona? Si la lastimé, puedo reparar: reconocer lo que pasó, decir «lo siento» y preguntar cómo ayudar.",
        "Pedir disculpas no es solo decir una palabra. Es hacerse cargo y cambiar lo que sigue. Y si te hicieron daño, no tienes que aceptar enseguida. Puedes esperar, y siempre puedes pedir ayuda a un adulto de confianza.",
    ],
    [("escucha", "poner atención a lo que otro dice"), ("impacto", "efecto de lo que hago en otros"), ("reformular", "decir con mis palabras lo que entendí"), ("reparar", "hacer algo para arreglar el daño"), ("disculpa", "decir que lo siento y hacerme cargo")],
    [
        W("Escuchar bien", "Camila cuenta que se sintió triste porque no la dejaron jugar. ¿Qué respuesta muestra buena escucha: «No es para tanto» o «Entiendo que te dio pena que no te dejaran jugar»?", ["La primera dice que su emoción no importa.", "La segunda repite con otras palabras lo que dijo Camila.", "Eso es reformular."], "«Entiendo que te dio pena que no te dejaran jugar»"),
        W("Reparar el impacto", "Sebastián empujó sin querer a un compañero y se le cayó el cuaderno. ¿Qué puede hacer para reparar?", ["Reconocer lo que pasó.", "Decir «lo siento».", "Ayudar a recoger y preguntar si está bien."], "Decir «lo siento», ayudar a recoger y preguntar si está bien"),
    ],
    [
        M("Escuchar pensando solo en lo que voy a contestar.", "Queremos defendernos rápido.", "Espera, mira a la persona y repite lo que entendiste."),
        M("Decir «lo siento» y seguir igual.", "Se piensa que la palabra arregla todo.", "Haz algo para reparar y cuida que no vuelva a pasar."),
    ],
    R=[
        ex("Para escuchar bien, ¿miras a la persona o miras para otro lado?", "Miro a la persona", "La atención se nota en la mirada."),
        ex("«Reformular» ¿es repetir con mis palabras lo que entendí o dar un consejo?", "Repetir con mis palabras lo que entendí", "Así la otra persona sabe que la escuchaste."),
        ex("Si lastimas a alguien sin querer, ¿qué puedes hacer?", "Reconocerlo, decir lo siento y ayudar", "Así reparas el daño."),
    ],
    U=[
        ex("¿Qué es el impacto de lo que hago?", "El efecto en otros", "Mide cómo se sienten o qué pasa por mi acción."),
        ex("¿Una buena intención garantiza que no lastimé a nadie?", "No", "Puedo lastimar sin querer."),
        ex("Si alguien te lastimó y te pide disculpas, ¿debes aceptar enseguida?", "No, puedes esperar", "Cada persona necesita su tiempo."),
    ],
    A=[
        ex("Lola dice: «Me dio vergüenza que se rieran de mi dibujo». Escribe cómo reformularías lo que dijo.", "Entiendo que te dio vergüenza que se rieran de tu dibujo", "Repite lo que entendió sin juzgar."),
        ex("Pedro rompió sin querer el trabajo de Eli. Escribe una disculpa que se haga cargo.", "Lo siento, rompí tu trabajo sin querer; te ayudo a rehacerlo", "Reconoce lo que hizo y ofrece reparar."),
        ex("Tras un empujón en la fila, ¿qué pregunta ayuda a pensar en el impacto: «¿cómo se sintió?» o «¿quién ganó?»?", "¿Cómo se sintió?", "Mira el efecto en la otra persona."),
    ],
    Z=[
        ex("Una niña dice «lo siento» y vuelve a burlarse al día siguiente. ¿Reparó?", "No", "No cambió su conducta."),
        ex("Un compañero cuenta algo con pena y tú le dices «eso no es nada». ¿Escuchaste y respetaste su emoción?", "No", "Le restaste importancia a lo que siente."),
    ],
    D=[
        arith("Un grupo practica la escucha: 6 niños hablan 2 minutos cada uno. ¿Cuántos minutos de escucha hay en total?", "6*2", "Se repite 2 minutos seis veces."),
        ex("Beto dice: «Me enojé porque se burlaron de mi apellido». Elige la mejor respuesta: «No hagas caso» o «Entiendo que te enojaste porque se burlaron de tu apellido y eso no está bien».", "«Entiendo que te enojaste porque se burlaron de tu apellido y eso no está bien»", "Escucha, nombra la emoción y no resta importancia."),
    ],
    context=[ex("En una conversación de curso, Inés interrumpió a Joaquín y él se quedó callado. Inés dice: «Perdona, te interrumpí. ¿Quieres seguir con lo que decías?». ¿Reparó el impacto?", "Sí", "Reconoció lo que hizo y le devolvió la palabra.")],
    selfcheck=[ex("En Orientación: ¿escuchar es solo estar callado?", "No", "También es mirar y entender."), ex("¿Una disculpa debe incluir algo para reparar?", "Sí", "Así se hace cargo del daño."), ex("¿Puedes pedir ayuda a un adulto de confianza si te lastimaron?", "Sí", "No tienes que resolverlo solo.")],
    task=T("Lee: Mía dice «Me dio pena que no me escogieran para el equipo». Escribe cómo reformularías lo que dijo y qué pregunta le harías. Después escribe una disculpa para esta situación: sin querer pisaste el dibujo de un compañero.", "Reformulo: «Entiendo que te dio pena no ser elegida». Pregunta: «¿Quieres que juguemos algo juntas?». Disculpa: «Perdón, pisé tu dibujo; te ayudo a pintarlo de nuevo».", ["reformula sin juzgar", "la disculpa reconoce y repara", "no obliga a nadie a aceptar la disculpa"], ["frases escritas o actuadas"], ["decir «no es para tanto»", "decir «lo siento» sin reparar"], "Reconoce la escucha y revisa que la disculpa incluya una forma de reparar."),
    reinforce="Escribe cómo escucharías a un compañero que está triste sin darle consejos.",
    extend="Piensa en una vez que lastimaste a alguien sin querer y escribe, sin dar nombres, qué harías hoy para reparar.",
)
