"""Cuaderno del estudiante, 2.º básico Orientación: OA 01 (características, habilidades e intereses) y OA 02 (emociones)."""
from __future__ import annotations

from student_lessons import ex, register

OA1, OA2 = "OR02 OA 01", "OR02 OA 02"


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
    "Una hoja y lápiz. Los retratos de los niños están escritos en cada ejercicio. No tienes que contar nada privado.",
    "Aprenderé a mirar a una persona y a describirla con datos: cómo se ve, cómo es y qué le gusta. Sirve para conocerme y conocer a otros con respeto.",
    ["Sé que cada persona es distinta.", "Sé decir una característica mía sin compararme."],
    [
        "Una característica es un dato que dice cómo es una persona. Hay tres tipos. Unas se ven, como el pelo rizado o los lentes. Otras son de la forma de ser, como ser paciente o curioso. Otras son gustos, como querer saber de planetas.",
        "Para describir bien, usa al menos dos datos y que sean verdaderos. Por ejemplo: «Inés tiene el pelo corto y siempre espera su turno». Describir no es poner una etiqueta fija como «Inés es aburrida». Una etiqueta dice demasiado poco y casi nunca es justa.",
        "Tú eliges qué contar de ti. Hay cosas que son privadas y no tienes que decirlas. Cuando describes a otra persona, usa solo lo que ves o lo que ella cuenta. No adivines lo que no sabes.",
    ],
    [("característica", "dato que dice cómo es una persona"), ("rasgo", "una característica de la forma de ser"), ("dato", "algo verdadero que se puede observar"), ("etiqueta", "palabra fija que encierra a una persona"), ("privado", "algo que cada uno decide si cuenta")],
    [
        W("Describir con dos datos", "Mateo usa lentes y siempre ayuda a repartir las hojas. Describe a Mateo con dos datos.", ["Primer dato que se ve: usa lentes.", "Segundo dato de su forma de ser: ayuda a repartir.", "Junto los dos con «y»."], "Mateo usa lentes y es ayudador"),
        W("Distinguir tipos", "Rita dice: «Me encanta mirar las nubes». ¿Qué tipo de característica es?", ["No se ve por fuera.", "No dice cómo actúa con otros.", "Dice lo que le llama la atención: es un gusto."], "Es un gusto"),
    ],
    [
        M("Describir a alguien con una etiqueta como «es el tímido».", "Una sola palabra parece resumir a toda la persona.", "Usa dos datos y deja espacio para que cambie: «A veces habla bajito»."),
        M("Contar cosas privadas porque otro niño las pidió.", "Pensamos que hay que responder todo.", "Puedes decir «prefiero no contarlo» y elegir otra característica."),
    ],
    R=[
        ex("Lola tiene el pelo trenzado. ¿Es una característica que se ve o de la forma de ser?", "Que se ve", "El pelo trenzado se observa con los ojos."),
        ex("Beto siempre espera su turno. ¿Eso es un rasgo de forma de ser o un gusto?", "Un rasgo de forma de ser", "Esperar el turno muestra cómo actúa Beto."),
        ex("Sara dice: «Me gusta dibujar peces». ¿Qué tipo de característica es?", "Un gusto", "Dice lo que le gusta hacer."),
    ],
    U=[
        ex("¿Cuántos datos conviene usar para describir bien a una persona?", "Al menos dos", "Con dos datos la descripción no queda corta ni injusta."),
        ex("¿«Pablo es flojo» es un dato o una etiqueta?", "Una etiqueta", "Encierra a Pablo en una palabra sin mostrar qué hace."),
        ex("Si un compañero te pregunta algo muy privado, ¿puedes decir «prefiero no contarlo»?", "Sí", "Cada persona decide qué comparte."),
    ],
    A=[
        ex("Nico tiene gorro rojo y presta sus lápices. Escribe una frase con esos dos datos.", "Nico tiene gorro rojo y presta sus lápices", "Usa un dato que se ve y uno de su forma de ser."),
        ex("En la lista «ojos verdes, tranquila, le gusta el fútbol», ¿cuál es el gusto?", "Le gusta el fútbol", "Es lo que a la persona le agrada hacer."),
        ex("Dani levantó la voz en el recreo. Escribe una frase que cuente ese hecho en vez de la etiqueta «Dani es peleador».", "Dani levantó la voz en el recreo", "Se cuenta lo que ocurrió y no se encierra a Dani en una palabra."),
    ],
    Z=[
        ex("Ema dice: «Julia es mala porque no habló hoy». ¿Qué falta para describir bien a Julia?", "Más datos, porque no hablar un día no basta", "Una sola conducta no muestra cómo es Julia."),
        ex("Leo cuenta una característica suya y otro niño dice «eso es raro». ¿Dejó de ser una característica válida?", "No", "Cada persona tiene rasgos propios que se respetan."),
    ],
    D=[
        ex("Tres niños dicen: «Soy curiosa», «Tengo pecas» y «Soy tranquilo». ¿Cuántas características de forma de ser dijeron?", "2", "Curiosa y tranquilo son de la forma de ser; pecas se ve."),
        ex("Una niña dice: «Uso lentes y me gusta cantar». ¿Cuántos tipos de característica distintos usó?", "2", "Lentes se ve y cantar es un gusto."),
    ],
    context=[ex("En la ronda de presentación, la profesora pide: «Cuenta dos datos tuyos». Camila dice: «Tengo el pelo rizado y me gusta armar rompecabezas». ¿Cumplió lo pedido?", "Sí", "Dijo dos datos verdaderos sobre ella: uno que se ve y un gusto.")],
    selfcheck=[ex("¿Una característica puede ser un gusto?", "Sí", "Lo que te gusta también te describe."), ex("¿Decir «eres aburrido» describe bien?", "No", "Es una etiqueta que no muestra datos."), ex("¿Debes contar todo sobre ti?", "No", "Tú eliges qué compartir.")],
    task=T("Completa dos frases con datos verdaderos sobre ti y di o dibuja cuál se ve y cuál es de tu forma de ser: «Yo tengo…» y «Yo soy una persona…». Si prefieres, usa a un personaje: Mateo (usa lentes, ayuda a repartir hojas).", "«Tengo el pelo corto» (se ve) y «soy cuidadosa con mis cosas» (forma de ser).", ["usa dos datos", "distingue lo que se ve de la forma de ser", "no usa etiquetas ni compara"], ["frases dichas o escritas", "dibujo con explicación breve"], ["usar una etiqueta fija", "contar algo privado"], "Reconoce los datos que sí describen y pregunta qué otro dato agregaría."),
    reinforce="Escribe tres datos sobre ti: uno que se ve, uno de tu forma de ser y un gusto.",
    extend="Describe con dos datos a un personaje de un cuento que conozcas, sin usar etiquetas.",
)

lesson(
    OA1, 2,
    "Una hoja y lápiz. Las situaciones y la tabla de práctica están escritas en los ejercicios.",
    "Aprenderé que una habilidad se desarrolla con práctica y que puedo planear pasos pequeños. Sirve para animarme a aprender sin rendirme.",
    ["Sé que tengo características.", "Sé que algunas cosas me salen y otras todavía no."],
    [
        "Una habilidad es algo que sabes hacer y que puedes mejorar. Puede ser del cuerpo, como saltar la cuerda. Puede ser de la mente, como resolver un rompecabezas. Puede ser con otros, como escuchar o ayudar.",
        "Las habilidades crecen con práctica. Un buen plan tiene pasos pequeños y claros. Por ejemplo: día 1, mirar cómo se hace; día 2, intentar con ayuda; día 3, intentar solo. Equivocarse es parte del camino, y cada intento enseña algo.",
        "La palabra «todavía» ayuda mucho. «No sé andar en bicicleta» se convierte en «todavía no sé andar en bicicleta». Así recuerdas que puedes aprender. Para saber si avanzas, compara contigo mismo: cómo te salía antes y cómo te sale hoy, no con otro niño.",
    ],
    [("habilidad", "algo que sé hacer y puedo mejorar"), ("práctica", "repetir algo con calma para mejorar"), ("plan", "pasos ordenados para lograr algo"), ("avance", "mejora que ya se nota"), ("todavía", "palabra que recuerda que puedo aprender")],
    [
        W("Armar un plan", "Valentina quiere aprender a saltar la cuerda 10 veces seguidas. Hoy salta 3. Propón un plan de dos pasos.", ["Meta: llegar a 10 saltos.", "Paso 1: practicar 5 minutos al día hasta llegar a 5 saltos.", "Paso 2: seguir otra semana hasta llegar a 10."], "Practicar 5 minutos al día: primero 5 saltos y luego 10"),
        W("Medir el avance", "El lunes Tomás leyó 2 renglones sin trabarse. El viernes leyó 6. ¿Avanzó?", ["Compara contigo mismo: lunes 2, viernes 6.", "6 es más que 2.", "Sí hay un avance."], "Sí, avanzó de 2 a 6 renglones"),
    ],
    [
        M("Decir «no sirvo para esto» cuando algo no sale a la primera.", "Una dificultad parece una condición para siempre.", "Cambia la frase por «todavía no me sale» y elige un paso pequeño."),
        M("Medir el avance comparándome con quien lo hace mejor.", "El otro lleva más práctica y eso desanima.", "Compara cómo te salía antes con cómo te sale hoy."),
    ],
    R=[
        ex("Ana sabe atarse los cordones. ¿Eso es una habilidad?", "Sí", "Es algo que Ana sabe hacer."),
        ex("¿Qué ayuda más a mejorar una habilidad: practicar o esperar?", "Practicar", "Repetir con calma permite avanzar."),
        ex("Completa: «Todavía no sé nadar» quiere decir que puedo…", "Aprender más adelante", "La palabra «todavía» deja abierta la posibilidad."),
    ],
    U=[
        ex("¿Un plan de práctica debe tener pasos pequeños o un solo paso enorme?", "Pasos pequeños", "Los pasos pequeños se pueden cumplir."),
        ex("¿Equivocarse al practicar significa que no se puede aprender?", "No", "Los errores muestran qué ajustar."),
        ex("Para saber si avanzas, ¿comparas contigo mismo o con el mejor del curso?", "Contigo mismo", "Así ves tu propia mejora."),
    ],
    A=[
        ex("Pedro cuenta 2 pelotazos al arco el lunes y 5 el viernes. ¿Cuántos más hizo el viernes?", "3", "5 menos 2 es 3, y eso muestra su avance."),
        ex("Ema quiere dibujar caras. Escribe un primer paso pequeño de práctica.", "Por ejemplo: dibujar solo los ojos cada día", "Es concreto y se puede cumplir."),
        ex("Convierte «no sé armar este rompecabezas» en una frase con «todavía».", "Todavía no sé armar este rompecabezas", "Se agrega «todavía» sin cambiar lo demás."),
    ],
    Z=[
        ex("Rosa practicó 5 minutos cada día. Luis practicó 30 minutos solo el domingo. ¿Quién tiene un hábito más fácil de mantener?", "Rosa", "Pocos minutos seguidos son más simples de repetir."),
        ex("Un niño dice: «Mi amiga lo hace mejor, así que yo no avanzo». ¿Qué dato le faltó mirar?", "Cómo le salía a él antes", "El avance se mide con el propio punto de partida."),
    ],
    D=[
        ex("Un plan dice: lunes mirar, martes intentar con ayuda, miércoles intentar solo. ¿Cuántos pasos tiene?", "3", "Hay un paso por cada día nombrado."),
        ex("Si alguien practica 4 minutos al día durante 5 días, ¿cuántos minutos practicó en total?", "20", "4 por 5 es 20 minutos."),
    ],
    context=[ex("Camila no logra cantar una canción sin olvidar la letra. Su abuelo le dice: «Cántala una estrofa por día». ¿Qué tipo de plan le propone?", "Uno con pasos pequeños", "Dividir la canción en partes la hace posible de aprender.")],
    selfcheck=[ex("¿Una habilidad puede mejorar?", "Sí", "La práctica ayuda a mejorar."), ex("En Orientación: ¿Los errores sirven para aprender?", "Sí", "Muestran qué cambiar."), ex("¿Con quién comparas tu avance?", "Contigo mismo", "Miras tu antes y tu ahora.")],
    task=T("Elige una habilidad de esta lista: atarme los cordones, escribir mi nombre con letra clara, saltar la cuerda o contar un cuento. Escribe o dibuja un plan de tres pasos pequeños y di cómo sabrás que avanzas.", "Habilidad: escribir mi nombre claro. Paso 1: copiar mi nombre 1 vez. Paso 2: escribirlo 2 veces. Paso 3: escribirlo sin mirar. Avanzo si cada vez me queda más parejo.", ["elige una habilidad concreta", "plan de tres pasos pequeños", "dice cómo medir su avance contra sí mismo"], ["plan escrito o dibujado"], ["pasos demasiado grandes", "medir el avance comparándose con otros"], "Reconoce el plan y sugiere hacer el primer paso más pequeño si cuesta."),
    reinforce="Escribe una cosa que antes no sabías hacer y ahora sí. Cuenta cómo practicaste.",
    extend="Elige otra habilidad de la lista y escribe solo su primer paso.",
)

lesson(
    OA1, 3,
    "Una hoja y lápices. La lista de actividades y los casos están escritos en los ejercicios.",
    "Aprenderé qué son los intereses y cómo me ayudan a elegir qué conocer. Sirve para descubrir cosas nuevas sin miedo a probar.",
    ["Sé que tengo gustos.", "Sé que puedo aprender con práctica."],
    [
        "Un interés es algo que te llama la atención y te dan ganas de conocer más. No es lo mismo que una habilidad. Una habilidad es lo que sabes hacer. Un interés es lo que quieres explorar, aunque aún no sepas mucho.",
        "Los intereses sirven para elegir. Si te interesan los planetas, puedes pedir un libro de astronomía, mirar el cielo con un adulto o dibujar el sistema solar. Los intereses también cambian con el tiempo, y eso es normal.",
        "A veces no sabes si algo te interesa. Entonces puedes probarlo una vez, con calma, y preguntarte: ¿me dieron ganas de seguir? Si dices que sí, es un posible interés. Si dices que no, no pasa nada, ya aprendiste algo sobre ti.",
    ],
    [("interés", "algo que quiero conocer más"), ("explorar", "mirar y probar algo con curiosidad"), ("elegir", "decidir entre varias opciones"), ("cambiar", "volverse distinto con el tiempo"), ("probar", "intentar algo para saber si me gusta")],
    [
        W("Interés o habilidad", "Gaspar dice: «Quiero saber cómo viven las hormigas». ¿Es un interés o una habilidad?", ["Gaspar no dice que sepa hacer algo.", "Dice que quiere conocer algo.", "Eso es querer explorar."], "Es un interés"),
        W("Usar un interés para elegir", "A Ema le interesan las aves. Puede elegir entre: armar una caja con recortes de aves, ordenar sus zapatos o jugar a las escondidas. ¿Cuál se relaciona con su interés?", ["Busca la opción que habla de aves.", "La caja de recortes de aves conecta con su interés.", "Las otras dos no."], "Armar la caja con recortes de aves"),
    ],
    [
        M("Pensar que si algo me interesa, ya debo hacerlo perfecto.", "Se mezclan interés y habilidad.", "Un interés es ganas de conocer; la habilidad llega practicando."),
        M("Creer que si cambio de interés hice algo malo.", "Pensamos que un gusto debe durar para siempre.", "Los intereses cambian y eso es normal."),
    ],
    R=[
        ex("A Lía le interesan los trenes. ¿Eso es algo que quiere conocer o algo que sabe hacer?", "Algo que quiere conocer", "Un interés son las ganas de explorar."),
        ex("¿Los intereses pueden cambiar con el tiempo?", "Sí", "Con nuevas experiencias aparecen otros gustos."),
        ex("Si pruebas algo una vez y no te gustó, ¿hiciste algo mal?", "No", "Probar también ayuda a conocerse."),
    ],
    U=[
        ex("¿Cuál frase es un interés: «Sé tocar un tambor» o «Quiero saber cómo suena un tambor»?", "«Quiero saber cómo suena un tambor»", "Habla de ganas de conocer."),
        ex("Para saber si algo te interesa, ¿qué pregunta te haces después de probarlo?", "¿Me dieron ganas de seguir?", "Esa pregunta muestra si hay interés."),
        ex("¿Se puede tener más de un interés a la vez?", "Sí", "Una persona puede explorar varias cosas."),
    ],
    A=[
        ex("A Tomás le interesa la música. Elige la actividad que se conecta: escuchar sonidos de distintos instrumentos, lavar platos o contar monedas.", "Escuchar sonidos de distintos instrumentos", "Se relaciona con la música."),
        ex("Rosa tiene tres actividades: hacer un volcán de papel, pintar con témpera, armar un barco con cajas. Le interesan los barcos. ¿Cuál elige?", "Armar un barco con cajas", "Conecta con su interés en los barcos."),
        ex("Escribe una frase con «me interesa…» sobre las nubes.", "Me interesa saber cómo se forman las nubes", "Muestra ganas de conocer y no una habilidad."),
    ],
    Z=[
        ex("Un niño probó el ajedrez y dijo «no quiero seguir». Otro dijo «quiero aprender más». ¿Quién descubrió un posible interés?", "El que quiere aprender más", "Las ganas de seguir son la señal de un interés."),
        ex("Beto dijo en 1.º que le interesaban los dinosaurios y ahora le interesan los insectos. ¿Su interés anterior valió menos?", "No", "Los intereses cambian y todos valen."),
    ],
    D=[
        ex("Ana tiene 3 intereses y se le sumó 1 nuevo. ¿Cuántos intereses tiene ahora?", "4", "3 más 1 es 4."),
        ex("Un amigo dice: «Eso que te interesa es de niñas» sobre el baile. ¿Un interés tiene dueño según género?", "No", "Cualquier persona puede explorar lo que le interesa."),
    ],
    context=[ex("En una feria de talleres hay cuatro mesas: huerto, dibujo, música y ciencias. A Pablo le llamó la atención el huerto y se quedó preguntando cómo crecen las semillas. ¿Qué interés mostró?", "El huerto y cómo crecen las semillas", "Se quedó preguntando, y eso muestra ganas de conocer.")],
    selfcheck=[ex("¿Un interés es lo que quiero conocer más?", "Sí", "Es curiosidad por algo."), ex("¿Los intereses pueden cambiar?", "Sí", "Con el tiempo aparecen otros."), ex("¿Se necesita ser experto para tener un interés?", "No", "Basta con las ganas de conocer.")],
    task=T("Mira esta lista: planetas, cocinar con un adulto, insectos, bailar, construir con cajas, cantar. Marca dos que te interesen y para una escribe o dibuja una cosa pequeña que podrías hacer esta semana para explorarla, con ayuda de un adulto si hace falta.", "Marco insectos y bailar. Para insectos: mirar con una lupa una hormiga del patio sin tocarla.", ["marca dos intereses de la lista", "propone una acción de exploración posible y segura", "no compara con otros"], ["lista marcada", "dibujo o frase de la acción"], ["proponer algo peligroso o imposible", "creer que debe ser experto"], "Reconoce el interés y revisa que la acción sea segura y pequeña."),
    reinforce="Cuenta qué te gustaría conocer más y a quién le preguntarías.",
    extend="Elige un interés y piensa dos cosas pequeñas que podrías hacer para explorarlo.",
)

lesson(
    OA1, 4,
    "Una hoja y lápiz. La tabla de tres niños y las frases están escritas en los ejercicios.",
    "Aprenderé a valorar mis características y las de otros sin competir. Sirve para convivir respetando que todos somos distintos.",
    ["Sé describir características con datos.", "Sé que tengo habilidades e intereses."],
    [
        "Valorar es reconocer que algo tiene importancia. Puedes valorar una característica tuya o de otra persona. Valorar no es decir quién gana. Es notar que cada uno aporta algo distinto a un grupo.",
        "Piensa en un equipo que arma un mural. Una niña dibuja bien, otro niño ordena los colores y otra escucha las ideas de todos. Nadie es «el mejor». Sin una de esas tres cosas, el mural sería más difícil de hacer.",
        "Comparar para ver quién es mejor suele dejar a alguien triste. Una frase que valora dice algo como: «Me gusta cómo explicas» o «Gracias por esperar». Habla de lo que la persona hace y no la pone arriba ni abajo de otra.",
    ],
    [("valorar", "reconocer que algo tiene importancia"), ("aportar", "dar algo que ayuda al grupo"), ("diversidad", "que las personas somos distintas"), ("competir", "tratar de ganarle a otro"), ("reconocer", "decir con respeto lo bueno que alguien hace")],
    [
        W("Frase que valora", "¿Qué frase valora a Mía: «Dibujas mejor que todos» o «Me gusta cómo pintas el cielo»?", ["La primera pone a Mía sobre los demás.", "La segunda habla de lo que ella hace.", "Valorar es mirar lo que la persona aporta."], "«Me gusta cómo pintas el cielo»"),
        W("Aportes distintos", "Un grupo arma un mural. Ana dibuja, Beto ordena colores y Cata escucha las ideas. ¿Quién aporta algo importante?", ["Ana aporta dibujo.", "Beto aporta orden.", "Cata aporta escucha. Los tres son necesarios."], "Los tres aportan algo importante"),
    ],
    [
        M("Pensar que valorar a otro me hace menos a mí.", "Se cree que el reconocimiento es una competencia.", "Reconocer a otro no quita nada de lo que tú vales."),
        M("Decir «tú eres el mejor» a un niño y «tú no sirves» a otro.", "Sentimos que alguien siempre debe ganar.", "Reconoce lo que cada uno hace sin ordenarlos."),
    ],
    R=[
        ex("¿Valorar es decir quién gana o reconocer lo que alguien aporta?", "Reconocer lo que alguien aporta", "Valorar no es competir."),
        ex("En el mural, Beto ordena los colores. ¿Su aporte sirve al grupo?", "Sí", "El orden ayuda a que el trabajo salga."),
        ex("¿«Gracias por esperar» es una frase que valora?", "Sí", "Reconoce algo que la persona hizo."),
    ],
    U=[
        ex("Una frase dice: «Eres más inteligente que Luis». ¿Valora o compara?", "Compara", "Pone a una persona sobre otra."),
        ex("¿Cada persona de un grupo puede aportar cosas distintas?", "Sí", "La diversidad suma al grupo."),
        ex("¿Una frase que valora habla de lo que la persona hace o de quién es mejor?", "De lo que la persona hace", "Se fija en un aporte concreto."),
    ],
    A=[
        ex("Escribe una frase que valore a Rosa, que ayudó a recoger los materiales.", "Gracias, Rosa, por ayudar a recoger los materiales", "Dice qué hizo y no compara."),
        ex("Un niño mide con la huincha su salto: Ema 80 cm, Leo 95 cm, Sofi 70 cm. ¿Hay que decir que Leo vale más?", "No", "El salto es un dato; el valor de la persona no se mide."),
        ex("Tabla: Ana explica bien, Beto cuenta chistes sanos, Cata es muy ordenada. ¿Quién aporta humor al grupo?", "Beto", "Contar chistes sanos aporta alegría."),
    ],
    Z=[
        ex("En el recreo, Luis dice: «Yo corro más que todos, entonces soy mejor». ¿Qué parte no valora a los demás?", "«Soy mejor»", "Pasar de un dato de velocidad a decir que valdría más es comparar."),
        ex("Dos niñas dicen cada una lo que la otra hace bien. ¿Perdió alguna de las dos?", "No", "Reconocerse mutuamente no es competir."),
    ],
    D=[
        ex("Si un grupo de 4 niños tiene 4 aportes distintos, ¿cuántos aportes se pierden si uno se va?", "1", "Cada uno aporta uno, así que se pierde 1."),
        ex("Un niño dice: «Mi característica no sirve porque nadie más la tiene». ¿Qué le dirías?", "Que ser distinto también aporta", "La diversidad suma al grupo."),
    ],
    context=[ex("Después de un juego, el profesor pide: «Cada uno diga algo que valora de un compañero». Beto dice: «Valoro que Inés siempre me presta la goma». ¿Valoró bien?", "Sí", "Habló de una acción concreta sin comparar.")],
    selfcheck=[ex("¿Valorar es lo mismo que competir?", "No", "Valorar reconoce y no ordena."), ex("¿Todos aportan algo a un grupo?", "Sí", "Cada persona suma algo distinto."), ex("¿Una frase que valora dice qué hizo la persona?", "Sí", "Se fija en un aporte concreto.")],
    task=T("Escribe o di dos frases de valoración sin comparar: una para ti y una para alguien de tu curso o familia. Puedes usar estos comienzos: «Me gusta cómo…» o «Gracias por…». Si no quieres nombrar a nadie, escribe para un personaje: Beto, que ordena los colores.", "Para mí: «Me gusta cómo cuido mis cosas». Para mi hermano: «Gracias por esperarme en la puerta».", ["dos frases", "hablan de lo que la persona hace", "no comparan ni ordenan personas"], ["frases escritas o dichas"], ["usar «mejor que» o «peor que»", "elogiar solo el resultado"], "Reconoce las frases que valoran y pregunta cómo se sentiría la otra persona al oírlas."),
    reinforce="Di una frase de valoración para alguien de tu casa, usando «Gracias por…».",
    extend="Anota tres aportes distintos que ves en tu curso o tu familia.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y lápiz. Las escenas, las palabras y los gestos están escritos en los ejercicios.",
    "Aprenderé a reconocer emociones con pistas: la situación, las palabras y los gestos. Sirve para entender lo que siento y lo que podría sentir otra persona.",
    ["Conozco las palabras pena, rabia, miedo y alegría.", "Sé que sentir emociones es normal."],
    [
        "Una emoción es lo que sientes ante algo que pasa. Pena, rabia, miedo y alegría son algunas emociones. Todas son normales y todas pueden sentirse. Lo importante es reconocer qué sientes y qué hacer con eso.",
        "Para reconocer una emoción puedes usar tres pistas: la situación, las palabras y los gestos. Por ejemplo, si a un niño se le cae su helado, dice «¡no!» y baja la cabeza, puede sentir pena. Con dos o tres pistas juntas es más fácil acertar.",
        "Con otras personas ten cuidado. Solo puedes decir «puede estar sintiendo…». No puedes asegurarlo. Lo mejor es preguntar: «¿Cómo te sientes?». Cada persona siente a su manera, y dos niños pueden sentir cosas distintas ante lo mismo.",
    ],
    [("emoción", "lo que siento ante algo que pasa"), ("pista", "dato que ayuda a descubrir algo"), ("gesto", "movimiento de la cara o del cuerpo"), ("situación", "lo que está pasando"), ("puede ser", "forma de no asegurar lo que siente otro")],
    [
        W("Usar tres pistas", "A Lía se le cayó su torre de bloques, dijo «¡otra vez!» y apretó los puños. ¿Qué podría sentir?", ["Situación: se cayó su torre.", "Palabras: «¡otra vez!».", "Gesto: aprieta los puños. Las pistas apuntan a rabia."], "Puede sentir rabia"),
        W("No asegurar", "Tomás está callado en la mesa. ¿Qué es mejor decir: «Estás triste» o «¿Cómo te sientes?»?", ["Una sola pista (callado) no basta para asegurar.", "Preguntar respeta lo que Tomás sienta.", "La pregunta es la mejor opción."], "«¿Cómo te sientes?»"),
    ],
    [
        M("Decir «tú estás enojado» sin preguntar.", "Una pista parece suficiente para saber todo.", "Di «puede ser que sientas…» y pregunta."),
        M("Pensar que la rabia o el miedo son emociones malas.", "Se confunde la emoción con lo que se hace con ella.", "Todas las emociones son normales; lo que importa es cómo las expreso."),
    ],
    R=[
        ex("Una niña sonríe y salta porque llegó su abuela. ¿Qué emoción puede sentir?", "Alegría", "La situación, la sonrisa y el salto señalan alegría."),
        ex("¿La rabia es una emoción normal?", "Sí", "Todas las emociones son normales."),
        ex("Un niño tiembla al ver un perro muy grande ladrar. ¿Qué podría sentir?", "Miedo", "El temblor y la situación apuntan a miedo."),
    ],
    U=[
        ex("¿Cuáles son las tres pistas para reconocer una emoción?", "La situación, las palabras y los gestos", "Juntas dan más seguridad."),
        ex("¿Se puede asegurar lo que siente otra persona con una sola pista?", "No", "Una pista no basta; hay que preguntar."),
        ex("Si dos niños pierden el mismo juego, ¿sienten siempre lo mismo?", "No", "Cada persona siente a su manera."),
    ],
    A=[
        ex("Ema llora bajito, mira el piso y dice «mi gato se perdió». ¿Qué emoción puede estar sintiendo?", "Pena", "Las lágrimas, la mirada baja y la situación apuntan a pena."),
        ex("Escribe una frase que no asegure: Beto tiene el ceño fruncido.", "Puede ser que Beto esté enojado, voy a preguntarle", "Usa «puede ser» y pregunta."),
        ex("Pistas: salta, ríe, dice «¡ganamos!». Elige: pena, alegría o miedo.", "Alegría", "Las tres pistas coinciden con alegría."),
    ],
    Z=[
        ex("Dani se tapa la cara tras perder un partido. Una persona dice «seguro tiene pena» y otra dice «puede tener rabia o pena». ¿Quién habla con más cuidado?", "La segunda", "Reconoce que no puede asegurarlo."),
        ex("Luisa cierra los ojos y respira hondo antes de un baile. Con solo esas pistas, ¿se puede asegurar qué siente?", "No", "Respirar hondo puede mostrar miedo, nervios o ganas de hacerlo bien; hay que preguntarle."),
    ],
    D=[
        ex("En una escena hay 3 pistas: situación, palabras y gestos. Si coinciden 2, ¿cuántas faltan por coincidir?", "1", "3 menos 2 es 1."),
        ex("¿Por qué conviene preguntar «¿cómo te sientes?» en vez de asegurar?", "Porque solo la persona sabe lo que siente", "Preguntar respeta lo que ella siente."),
    ],
    context=[ex("En el patio, Pía se sienta sola con los brazos cruzados. Su compañero Leo piensa en qué decir. ¿Cuál es una mejor frase: «Estás enojada» o «¿Quieres contarme cómo estás?»?", "«¿Quieres contarme cómo estás?»", "Pregunta sin asegurar y le deja elegir si quiere hablar.")],
    selfcheck=[ex("¿Las emociones son normales?", "Sí", "Todas se pueden sentir."), ex("¿Una sola pista alcanza para asegurar lo que siente otro?", "No", "Hay que juntar pistas y preguntar."), ex("¿Es bueno preguntar «cómo te sientes»?", "Sí", "Respeta lo que siente la otra persona.")],
    task=T("Lee esta escena: «Sofía vio que su dibujo se mojó con agua. Miró el papel, suspiró y dijo: no puede ser». Escribe o di qué emoción puede estar sintiendo, con dos pistas, y qué le preguntarías. Si quieres, elige otra escena con un personaje.", "Puede sentir pena o rabia. Pistas: se mojó su dibujo y suspiró. Le preguntaría: «¿Cómo te sientes?».", ["nombra una emoción posible", "usa dos pistas", "no asegura y propone preguntar"], ["frases escritas o dichas"], ["asegurar lo que siente", "usar solo una pista"], "Reconoce las pistas usadas y pregunta si hay otra emoción posible."),
    reinforce="Mira la cara de un adulto de tu familia y di una pista que viste; luego pregúntale cómo se siente.",
    extend="Escribe una escena corta con tres pistas para que otro adivine la emoción.",
)

lesson(
    OA2, 2,
    "Una hoja y lápiz. Las escenas con las formas de expresar están escritas en los ejercicios.",
    "Aprenderé que una misma emoción se puede expresar de formas distintas y que algunas son seguras. Sirve para sentir sin dañar a nadie ni dañarme.",
    ["Sé reconocer emociones con pistas.", "Sé que todas las emociones son normales."],
    [
        "Una emoción se puede expresar de muchas formas. Con palabras: «estoy enojado». Con el cuerpo: respirar, caminar, abrazar un cojín. Con arte: dibujar o escribir. Con otras personas: pedir ayuda. Hay una forma distinta para cada momento.",
        "Una expresión es segura cuando no hace daño a ti ni a otros, ni rompe lo que es de alguien. Golpear, gritar insultos o romper cosas no son expresiones seguras, aunque la emoción sea real. La rabia es normal; lo que se cuida es lo que haces con ella.",
        "Para elegir cómo expresar, puedes preguntarte tres cosas. ¿Me hago daño? ¿Hago daño a alguien? ¿Dañé algo? Si todas las respuestas son no, es una expresión segura. Si no te sale, pide ayuda a un adulto de confianza.",
    ],
    [("expresar", "mostrar lo que siento"), ("seguro", "que no hace daño a nadie"), ("respirar", "tomar y soltar aire con calma"), ("insulto", "palabra que ofende a otra persona"), ("adulto de confianza", "persona grande que me cuida y a quien puedo pedir ayuda")],
    [
        W("Elegir una forma segura", "Camila siente rabia porque le quitaron un juego. Opciones: golpear la mesa, decir «me enojó que me lo quitaran» o romper un papel. ¿Cuál es segura?", ["Golpear la mesa puede dañar la mesa y la mano.", "Romper cosas daña lo que es de alguien.", "Decir con palabras no daña a nadie."], "Decir «me enojó que me lo quitaran»"),
        W("Las tres preguntas", "Un niño con pena dibuja una nube gris. ¿Hace daño a alguien, a él o a algo?", ["¿Se daña a sí mismo? No.", "¿Daña a otro? No.", "¿Daña algo? No. Es segura."], "Es una expresión segura"),
    ],
    [
        M("Pensar que si siento rabia debo pegar o romper algo.", "Se mezcla sentir con hacer.", "La rabia se siente; para expresarla elijo una forma segura."),
        M("Esconder siempre lo que siento para que nadie se moleste.", "Creemos que mostrar una emoción molesta a otros.", "Se puede expresar con palabras tranquilas o pedir ayuda."),
    ],
    R=[
        ex("Dibujar lo que siento, ¿es una forma segura de expresar?", "Sí", "No hace daño a nadie."),
        ex("Gritar insultos a un compañero, ¿es una forma segura?", "No", "Ofende y daña a otra persona."),
        ex("¿Pedir ayuda a un adulto de confianza es una forma de expresar?", "Sí", "Compartir lo que siento ayuda a calmarlo."),
    ],
    U=[
        ex("¿Cuáles son las tres preguntas para saber si una expresión es segura?", "¿Me hago daño? ¿Hago daño a alguien? ¿Dañé algo?", "Si todo es no, la expresión es segura."),
        ex("¿Sentir rabia es lo mismo que romper algo?", "No", "Sentir es una cosa y actuar es otra."),
        ex("¿Existe una sola forma correcta de expresar una emoción?", "No", "Hay varias formas seguras para elegir."),
    ],
    A=[
        ex("Pedro está nervioso antes de leer en voz alta. Elige una forma segura: respirar 4 veces, morderse las uñas hasta lastimarse o empujar a un compañero.", "Respirar 4 veces", "Calma sin dañar a nadie."),
        ex("A Rosa le dan ganas de llorar porque extraña a su abuelo. Elige: esconder todo o contarle a su mamá cómo se siente.", "Contarle a su mamá cómo se siente", "Compartir con un adulto de confianza ayuda."),
        ex("Escribe una frase para decir que estás enojado sin ofender a nadie.", "Me enojé porque no me dejaron jugar", "Cuenta la emoción y el motivo sin insultar."),
    ],
    Z=[
        ex("Si dos niños sienten rabia y uno pega y otro cuenta lo que le molestó, ¿sintieron cosas distintas?", "No, sintieron lo mismo y expresaron distinto", "La emoción es igual; la forma de expresarla es distinta."),
        ex("¿Respirar hondo hace desaparecer la rabia de inmediato?", "No, ayuda a calmarla pero la emoción puede seguir un rato", "Respirar baja la intensidad, no borra la emoción de inmediato."),
    ],
    D=[
        ex("Lista de formas: dibujar, respirar, insultar, hablar, golpear. ¿Cuántas son seguras?", "3", "Dibujar, respirar y hablar son seguras."),
        ex("Si un amigo te cuenta que está enojado, ¿qué es mejor decir: «No te enojes» o «Entiendo que te enojaste»?", "«Entiendo que te enojaste»", "Reconoce su emoción sin negarla."),
    ],
    context=[ex("En el recreo, Sofía pierde en un juego y siente mucha rabia. Hay tres opciones: tirar la pelota lejos, decirle a su profesora «necesito calmarme» o gritarle a Luis. ¿Cuál es una forma segura?", "Decirle a su profesora «necesito calmarme»", "No daña a nadie y pide ayuda.")],
    selfcheck=[ex("¿Una expresión segura puede hacer daño?", "No", "Segura significa que no daña."), ex("¿Sentir rabia es malo?", "No", "Es una emoción normal."), ex("¿Puedes pedir ayuda cuando sientes algo fuerte?", "Sí", "Contárselo a un adulto de confianza ayuda.")],
    task=T("Elige una emoción (pena, rabia, miedo o alegría). Escribe o dibuja dos formas seguras de expresarla y una forma que no sería segura, con la razón. Puedes usar esta escena: Camila siente rabia porque le quitaron un juego.", "Rabia. Seguras: decir «me enojó», respirar contando hasta 4. No segura: golpear la mesa, porque puede dañar.", ["dos formas seguras", "una no segura con razón", "usa las tres preguntas"], ["lista escrita o dibujo"], ["listar formas que dañan como seguras", "no explicar el motivo"], "Reconoce las formas seguras y pregunta cuál usaría esta semana."),
    reinforce="Elige una forma segura de expresar rabia y practícala con un adulto.",
    extend="Dibuja cómo expresarías alegría de tres formas distintas y seguras.",
)

lesson(
    OA2, 3,
    "Una hoja y lápiz. La escala de intensidad y las historias están escritas en los ejercicios.",
    "Aprenderé que las emociones tienen más o menos fuerza y que cambian. Sirve para saber cuándo necesito calmarme o pedir ayuda.",
    ["Sé reconocer emociones y expresarlas de forma segura.", "Sé que respirar ayuda a calmarme."],
    [
        "Una emoción puede ser débil o muy fuerte. A eso se le llama intensidad. Podemos usar una escala de 1 a 3. El 1 es poco, el 2 es medio y el 3 es mucho. Sentir poca rabia no es lo mismo que sentir mucha rabia.",
        "Las emociones también cambian. Lo que se siente muy fuerte ahora puede bajar después de unos minutos. La rabia en nivel 3 puede bajar a nivel 1 si respiras y descansas. La pena puede sentirse más suave si alguien te acompaña.",
        "Para bajar la intensidad puedes respirar contando hasta 4, tomar agua, alejarte un rato o pedir un abrazo si lo quieres. Si la emoción sigue muy fuerte o te asusta, avisa a un adulto de confianza. Pedir ayuda es una forma de cuidarte.",
    ],
    [("intensidad", "cuánta fuerza tiene una emoción"), ("escala", "serie de niveles ordenados, como 1, 2 y 3"), ("cambiar", "volverse distinto"), ("calmarse", "bajar la fuerza de una emoción"), ("avisar", "decirle a alguien que necesito ayuda")],
    [
        W("Usar la escala", "Tras un empujón en la fila, Beto siente mucha rabia. ¿Qué número de la escala le pones: 1, 2 o 3?", ["Mucha rabia es la parte más fuerte.", "La escala va de poco (1) a mucho (3).", "Mucha corresponde al 3."], "3"),
        W("Ver el cambio", "Ema tenía miedo nivel 3 en el dentista. Respiró y la doctora le explicó. Quedó en nivel 1. ¿Cuántos niveles bajó?", ["Empezó en 3.", "Terminó en 1.", "3 menos 1 es 2."], "Bajó 2 niveles"),
    ],
    [
        M("Pensar que una emoción fuerte durará para siempre.", "En el momento parece que no va a pasar.", "Las emociones cambian; respirar y pedir ayuda las baja."),
        M("Esconder una emoción muy fuerte para que nadie se entere.", "Se cree que pedir ayuda es debilidad.", "Avisar a un adulto de confianza es cuidarse."),
    ],
    R=[
        ex("En la escala de 1 a 3, ¿qué número es «mucha»?", "3", "El 3 es el nivel más fuerte."),
        ex("Si una emoción es pequeña, ¿qué número le pones?", "1", "El 1 es poca fuerza."),
        ex("¿Las emociones pueden cambiar con el tiempo?", "Sí", "Se vuelven más débiles o distintas."),
    ],
    U=[
        ex("¿La intensidad mide cuánta fuerza tiene una emoción?", "Sí", "Intensidad es la fuerza de lo que siento."),
        ex("Nombra una forma de bajar la intensidad de una emoción.", "Respirar contando hasta 4", "Respirar con calma ayuda al cuerpo a relajarse."),
        ex("Si una emoción sigue muy fuerte y te asusta, ¿qué conviene hacer?", "Avisar a un adulto de confianza", "Pedir ayuda cuida a quien la siente."),
    ],
    A=[
        ex("Rosa tenía pena nivel 3. Después de abrazar a su mamá quedó en nivel 2. ¿Cuántos niveles bajó?", "1", "3 menos 2 es 1."),
        ex("Pedro dice: «Me enojé un poquito». ¿Qué número de la escala le pones?", "1", "Un poquito es poca intensidad."),
        ex("Ordena de menos a más fuerte: nivel 3, nivel 1, nivel 2.", "Nivel 1, nivel 2, nivel 3", "La escala crece del 1 al 3."),
    ],
    Z=[
        ex("Un niño con rabia nivel 3 se pone rojo y habla muy fuerte, y otro con rabia nivel 1 solo frunce el ceño. ¿Sienten emociones distintas?", "No, es la misma emoción con distinta intensidad", "La emoción es rabia en ambos; cambia la fuerza."),
        ex("Una niña dice: «Mi miedo bajó de 3 a 1 porque respiré». ¿Qué ayudó a que bajara?", "Respirar", "La respiración calmó su cuerpo."),
    ],
    D=[
        ex("Tomás tenía miedo nivel 3. Bajó 1 nivel al respirar y otro nivel al hablar con su papá. ¿En qué nivel quedó?", "1", "3 menos 1 es 2, y 2 menos 1 es 1."),
        ex("Dos niños sienten pena. Uno está en nivel 3 y otro en nivel 1. ¿Quién necesita más apoyo ahora?", "El de nivel 3", "Una emoción más fuerte suele necesitar más compañía."),
    ],
    context=[ex("Pía tiene que hablar frente al curso. Siente miedo nivel 3 y le tiembla la voz. La profesora le dice que respire contando hasta 4. ¿Qué busca esa ayuda?", "Bajar la intensidad del miedo", "Respirar calma el cuerpo y reduce el nivel.")],
    selfcheck=[ex("¿La escala va de 1 a 3?", "Sí", "Así medimos la intensidad."), ex("¿Las emociones fuertes pueden bajar?", "Sí", "Cambian con calma y apoyo."), ex("¿Avisar a un adulto cuando algo es muy fuerte es cuidarse?", "Sí", "Pedir ayuda protege.")],
    task=T("Piensa en una situación de esta lista: perder un juego, escuchar un ruido fuerte, recibir un regalo, que un amigo no te invite. Elige una, di qué emoción sientes y con qué número de la escala; luego escribe una cosa que harías para bajar la intensidad si fuera 3.", "Situación: perder un juego. Rabia nivel 2. Si fuera 3, respiraría contando hasta 4 y le avisaría a un adulto.", ["elige una situación", "nombra emoción e intensidad", "propone una acción para bajar la intensidad"], ["frases escritas o dichas", "dibujo de una escala"], ["decir que la emoción no cambia", "acciones que dañan"], "Reconoce la acción y pregunta qué otra podría probar."),
    reinforce="La próxima vez que sientas una emoción, ponle un número de 1 a 3.",
    extend="Dibuja una escala con tres caras: poca, media y mucha rabia.",
)

lesson(
    OA2, 4,
    "Una hoja y lápiz. Las situaciones están escritas en los ejercicios.",
    "Aprenderé a pedir apoyo cuando lo necesito y a ofrecerlo con respeto cuando otro lo necesita. Sirve para que nadie se sienta solo con una emoción.",
    ["Sé reconocer emociones con pistas.", "Sé que hay formas seguras de expresarlas."],
    [
        "Cuando una emoción es muy fuerte, pedir apoyo es una buena idea. Puedes decir: «Me siento mal, ¿puedes ayudarme?». Pídelo a un adulto de confianza, como tu familia o tu profesora. Pedir ayuda no es de débiles; es cuidarte.",
        "También puedes ofrecer apoyo a otra persona. Primero pregunta: «¿Quieres que te acompañe?». Si dice que sí, escucha con calma. Si dice que no, respeta y quédate cerca por si cambia de idea. No obligues a nadie a contar lo que no quiere contar.",
        "Hay cosas que no ayudan. Decir «no es para tanto» no ayuda. Tampoco ayuda burlarse ni contar lo que alguien te dijo a todo el mundo. Apoyar es escuchar y acompañar. Si un amigo cuenta algo que te asusta o parece peligroso, avisa de inmediato a un adulto de confianza.",
    ],
    [("apoyo", "ayuda que alguien da o recibe"), ("acompañar", "estar cerca de otro con respeto"), ("escuchar", "prestar atención a lo que otro dice"), ("respetar", "aceptar lo que otro decide"), ("avisar", "decir a un adulto algo que preocupa")],
    [
        W("Pedir apoyo", "Tomás está muy triste porque se mudó su mejor amigo. ¿Qué puede decir a su mamá: «No me pasa nada» o «Me siento triste, ¿puedes quedarte conmigo?»?", ["La primera frase esconde lo que siente.", "La segunda dice la emoción y pide algo claro.", "Pedir con claridad ayuda a recibir apoyo."], "«Me siento triste, ¿puedes quedarte conmigo?»"),
        W("Ofrecer apoyo", "Lía ve a Rosa llorar sola. ¿Qué es mejor: «Cuéntame ahora mismo» o «¿Quieres que me quede contigo?»?", ["La primera obliga a contar.", "La segunda pregunta y deja decidir a Rosa.", "Se ofrece sin presionar."], "«¿Quieres que me quede contigo?»"),
    ],
    [
        M("Decir «no es para tanto» a alguien que está mal.", "Queremos que la emoción pase rápido.", "Escucha y di «entiendo que te sientas así»."),
        M("Obligar a un amigo a contar lo que le pasa.", "Pensamos que contar siempre ayuda.", "Pregunta si quiere hablar y respeta su respuesta."),
    ],
    R=[
        ex("Si una emoción es muy fuerte, ¿conviene pedir apoyo a un adulto de confianza?", "Sí", "Alguien puede ayudarte a calmarte."),
        ex("¿Pedir ayuda significa que eres débil?", "No", "Pedir ayuda es una forma de cuidarte."),
        ex("Un amigo no quiere contar lo que le pasa. ¿Se le debe obligar?", "No", "Cada persona decide si quiere hablar."),
    ],
    U=[
        ex("¿Qué se dice primero para ofrecer apoyo: preguntar o mandar?", "Preguntar", "Preguntar respeta lo que la otra persona quiere."),
        ex("¿Decir «no es para tanto» ayuda a quien está mal?", "No", "Niega lo que siente la persona."),
        ex("Si un amigo cuenta algo peligroso, ¿a quién se avisa?", "A un adulto de confianza", "Los adultos pueden protegerlo."),
    ],
    A=[
        ex("Ema tiene miedo de la tormenta. Escribe una frase para pedir apoyo a su papá.", "Papá, tengo miedo de la tormenta, ¿puedes quedarte conmigo?", "Nombra la emoción y pide algo claro."),
        ex("Beto ve a Dani solo y callado en el recreo. Elige la frase que ofrece apoyo: «¿Quieres jugar conmigo o prefieres estar tranquilo?» o «Deja de estar así».", "«¿Quieres jugar conmigo o prefieres estar tranquilo?»", "Da opciones y respeta."),
        ex("Pía contó un secreto triste y su amiga lo dijo al curso. ¿Eso apoya o daña?", "Daña", "Contar lo que otro confió quita la confianza."),
    ],
    Z=[
        ex("Un adulto le pide a Sofía que guarde en secreto algo que la asusta o la hace sentir mal. ¿Debe guardarlo?", "No, debe contárselo a otro adulto de confianza", "Un secreto que asusta o incomoda se cuenta; ningún adulto debe pedir que se oculte."),
        ex("Rosa dijo «no quiero hablar ahora». Su amiga se quedó cerca sin decir nada. ¿Respetó a Rosa?", "Sí", "Se quedó cerca sin presionar."),
    ],
    D=[
        ex("Hay tres adultos de confianza: mamá, la profesora y un tío. Si Ema no encuentra a su mamá, ¿cuántas personas más puede buscar?", "2", "Quedan la profesora y el tío."),
        ex("Un amigo te cuenta que alguien lo lastima y que le pidió guardar el secreto. ¿Qué haces?", "Avisar de inmediato a un adulto de confianza", "Un adulto debe saberlo para cuidarlo; avisar no es acusar, es proteger."),
    ],
    context=[ex("Después de un partido, Luis está llorando porque su equipo perdió. Su compañero Pedro se acerca y le pregunta: «¿Quieres que me siente contigo?». Luis dice que sí. ¿Qué hizo bien Pedro?", "Preguntó y respetó la respuesta", "Ofreció apoyo sin obligar a Luis.")],
    selfcheck=[ex("¿Pedir ayuda es cuidarse?", "Sí", "Compartir una emoción fuerte ayuda."), ex("¿Se debe obligar a alguien a contar?", "No", "Cada persona decide."), ex("¿Un secreto que asusta debe guardarse?", "No", "Hay que contárselo a un adulto de confianza.")],
    task=T("Escribe o di dos frases: una para pedir apoyo (por ejemplo: «Me siento… ¿puedes…?») y una para ofrecerlo a alguien que parece triste. Puedes usar a Pía, que está sola en el recreo. Escribe también a quién le pedirías apoyo si lo necesitaras: tu adulto de confianza.", "Pedir: «Me siento nervioso, ¿puedes acompañarme?». Ofrecer: «Pía, ¿quieres que me quede contigo?». Mi adulto de confianza: mi profesora.", ["frase para pedir apoyo con la emoción", "frase para ofrecer apoyo con pregunta", "nombra un adulto de confianza"], ["frases escritas o dichas"], ["obligar a contar", "no nombrar la emoción"], "Reconoce la pregunta de respeto y sugiere tener más de un adulto de confianza."),
    reinforce="Nombra dos adultos de confianza a quienes podrías pedir apoyo.",
    extend="Escribe qué harías si un amigo te dijera «no quiero hablar ahora».",
)
