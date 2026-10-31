"""Cuaderno del estudiante, 5.º básico Orientación: OA 03 (desarrollo afectivo y sexual en la pubertad) y OA 04 (autocuidado, intimidad y uso seguro de redes)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or5_a import M, T, W, lesson

OA3, OA4 = "OR05 OA 03", "OR05 OA 04"

# ================================================================ OA 03
lesson(
    OA3, 1,
    "Una hoja y un lápiz. Los casos de Noa y las listas de cambios están escritos en los ejercicios. Nadie debe mostrar su cuerpo ni contar cosas privadas: trabajas con personajes inventados.",
    "Aprenderé qué es la pubertad y qué cambios físicos trae. Sirve para entender mi cuerpo y el de otras personas, y para cuidarlo con respeto.",
    ["Sé que mi cuerpo es mío y merece respeto.", "Sé que cada persona crece a su ritmo."],
    [
        "La pubertad es la etapa en que el cuerpo cambia para pasar de la niñez a la adolescencia. Empieza a distintas edades. En general ocurre entre los 8 y los 14 años, pero puede empezar antes o después, y eso es normal. Los cambios los provocan las hormonas, que son sustancias que produce el cuerpo y que le avisan cómo crecer.",
        "Algunos cambios físicos son comunes a todas las personas: el cuerpo crece rápido (el «estirón»), sale más vello en el cuerpo, se suda más, aparece olor corporal y pueden salir granos en la cara. Otros cambios son distintos: en las niñas crecen los pechos, se ensanchan las caderas y llega la menstruación, que es un sangrado normal que ocurre cada cierto tiempo. En los niños cambia la voz, sale vello en la cara y los músculos se desarrollan. En todas las personas también crecen y maduran los órganos sexuales.",
        "Cada cuerpo cambia a su propio ritmo. Que un compañero crezca antes o después que tú no significa que algo esté mal. Para cuidarte, aprende hábitos de higiene: ducharte con agua y jabón, lavar las axilas, cambiar la ropa interior y la ropa que usas todos los días. Si algo te preocupa de tu cuerpo, puedes preguntarle a una persona adulta de confianza.",
    ],
    [("pubertad", "etapa en que el cuerpo cambia al pasar de la niñez a la adolescencia"), ("hormonas", "sustancias del cuerpo que le indican cómo crecer y cambiar"), ("menstruación", "sangrado normal que ocurre cada cierto tiempo en las niñas durante la pubertad"), ("higiene", "hábitos de limpieza para cuidar el cuerpo"), ("ritmo", "velocidad con la que cada persona cambia")],
    [
        W("Reconocer un cambio común", "Teo nota que ahora suda más y que su cuerpo huele más fuerte que antes. ¿Es un cambio de la pubertad?", ["La pubertad trae más sudor y olor corporal.", "Es común a niñas y niños.", "Se cuida con higiene."], "Sí, es un cambio de la pubertad"),
        W("Cada cuerpo tiene su ritmo", "Sam empezó a crecer antes que su amigo Luis. Luis se preocupa. ¿Qué puede decirle un amigo para ser justo?", ["La pubertad empieza a edades distintas.", "Que alguien cambie antes o después es normal.", "Hay que respetar el ritmo de cada uno."], "«Cada persona cambia a su ritmo; es normal»"),
    ],
    [
        M("Pensar que si mi cuerpo cambia más tarde, algo está mal.", "Se compara con otros sin saber que el ritmo es distinto.", "Recuerda que la pubertad empieza a edades diferentes."),
        M("Hablar de los cambios del cuerpo de otros para reírse.", "Se confunde curiosidad con burla.", "Respeta el cuerpo de los demás y no hagas comentarios que hieran."),
    ],
    R=[
        ex("¿Qué produce los cambios de la pubertad: las hormonas o la comida?", "Las hormonas", "Son sustancias del cuerpo que indican cómo crecer."),
        ex("«Sudar más y tener olor corporal». ¿Es un cambio físico de la pubertad?", "Sí", "Aparece en niñas y niños durante la pubertad."),
        ex("«Dar un estirón». ¿Qué significa?", "Crecer rápido", "Es un aumento rápido de la estatura."),
    ],
    U=[
        ex("¿Por qué es normal que una amiga cambie antes que otra?", "Porque la pubertad empieza a edades distintas", "No hay una edad exacta igual para todos."),
        ex("La menstruación, ¿es una enfermedad o un cambio normal de la pubertad en las niñas?", "Un cambio normal", "Es parte del desarrollo y no es una enfermedad."),
        ex("¿Para qué sirve la higiene en la pubertad?", "Para cuidar el cuerpo y evitar el mal olor", "El sudor aumenta y hay que limpiar el cuerpo."),
    ],
    A=[
        ex("Lista: 1) estirón, 2) cambio de voz, 3) mochila nueva, 4) más vello en el cuerpo. ¿Cuántos son cambios de la pubertad?", "3", "Los cambios 1, 2 y 4 son físicos de la pubertad; la mochila no."),
        ex("Noa se ducha y cambia su ropa interior todos los días. ¿Qué hábito practica: higiene o descanso?", "Higiene", "Limpiar el cuerpo y cambiar la ropa es higiene."),
        ex("Un niño inventado cuenta que su voz cambió. ¿Cuál es una respuesta respetuosa: «Es parte de crecer» o «Qué ridículo suena»?", "«Es parte de crecer»", "Reconoce el cambio sin burlarse."),
    ],
    Z=[
        ex("Un grupo dice: «Si no ha cambiado todavía, no es normal». ¿Tienen razón?", "No", "La pubertad puede empezar más temprano o más tarde."),
        ex("¿Por qué es mejor preguntar a una persona adulta de confianza que a un compañero cuando algo del cuerpo preocupa?", "Porque el adulto puede dar información segura", "Un compañero puede equivocarse o inventar."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 8 ya notaron el estirón. ¿Cuántos todavía no lo notan?", "30-8", "Se restan los que ya lo notaron al total."),
        arith("Noa mide 140 centímetros y creció 6 centímetros en un año. ¿Cuánto mide ahora?", "140+6", "Se suma lo que creció."),
    ],
    context=[ex("En clase, el profesor dice: «A veces los cambios del cuerpo se notan primero en unos y después en otros». Una niña inventada responde: «Entonces mi ritmo no es mejor ni peor». ¿Entendió bien?", "Sí", "Reconoció que cada uno cambia a su ritmo.")],
    selfcheck=[ex("En Orientación: ¿la pubertad empieza igual para todos?", "No", "Empieza a distintas edades."), ex("¿Se debe hacer burlas sobre los cambios del cuerpo de otros?", "No", "Hay que respetar a las personas."), ex("¿La higiene ayuda a cuidar el cuerpo?", "Sí", "Limpiarse bien es un hábito de autocuidado.")],
    task=T("Lee las frases y clasifícalas en «cambio de la pubertad» o «no es de la pubertad»: crecer rápido, mojarse por la lluvia, sudar más, tener sueño por la noche, que cambie la voz. Después escribe una frase respetuosa que le dirías a un amigo inventado que se preocupa porque su cuerpo todavía no ha cambiado.", "Pubertad: crecer rápido, sudar más, que cambie la voz. No: mojarse por la lluvia, tener sueño. Frase: «Cada uno cambia a su ritmo; es normal».", ["clasifica las cinco frases", "escribe una frase respetuosa", "no habla de su propio cuerpo"], ["lista escrita o dicha"], ["decir una edad exacta para todos", "burlarse de un cambio"], "Reconoce la clasificación y pregunta qué hábito de higiene ayuda al cambio de sudor."),
    reinforce="Escribe tres cambios físicos de la pubertad y un hábito de higiene para cuidarse.",
    extend="Explica con tus palabras por qué el ritmo de cambio es distinto en cada persona.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. Los casos de Noa y Alex están escritos en los ejercicios.",
    "Aprenderé que la pubertad también cambia lo que siento y cómo me relaciono, y que mi cuerpo y mi intimidad tienen límites. Sirve para entenderme y respetar a otros.",
    ["Sé nombrar cambios físicos de la pubertad.", "Sé que las emociones se pueden describir con intensidad."],
    [
        "La pubertad no cambia solo el cuerpo. También cambian los afectos y las relaciones. Es común que el ánimo cambie rápido: un rato estás alegre y poco después irritable o triste, sin una razón clara. También aparece más vergüenza, más interés en la opinión de los amigos y más necesidad de privacidad. A veces una persona empieza a sentir atracción o curiosidad hacia otra, y a veces todavía no. Ambas cosas son normales.",
        "Distingue tres cosas. Los hechos son lo que pasa: «mi amigo cambió de voz». Las emociones son lo que sientes: vergüenza, curiosidad, nervios. Y los límites son lo que está bien y lo que no. Tu cuerpo es tuyo. Nadie puede tocarlo ni pedirte que lo muestres si tú no quieres, y tú tampoco puedes hacerlo con el cuerpo de otros. Solo en un control de salud, con una persona adulta de tu confianza presente, un profesional puede revisarte, y antes te explica lo que hará. Un secreto que da miedo o malestar no se guarda: se cuenta a una persona adulta de confianza.",
        "Otro límite es la privacidad. Cambiarte de ropa o ir al baño son momentos privados. Tienes derecho a cerrar la puerta y a pedir que respeten tu espacio. También debes respetar el espacio de los demás: tocar la puerta antes de entrar y no hacer preguntas incómodas sobre su cuerpo.",
    ],
    [("afecto", "sentimiento de cariño hacia alguien"), ("privacidad", "derecho a tener momentos y cosas solo para mí"), ("límite", "lo que acepto y lo que no acepto"), ("ánimo", "forma en que me siento durante el día"), ("atracción", "sentir interés especial por otra persona")],
    [
        W("Separar hecho, emoción y límite", "Noa se siente avergonzada porque un compañero la miró mucho mientras se cambiaba de ropa en el camarín. ¿Cuál es el hecho, cuál la emoción y cuál el límite?", ["Hecho: la miró mucho mientras se cambiaba.", "Emoción: vergüenza.", "Límite: su cuerpo es privado y puede pedir que la dejen tranquila."], "Hecho: la miró; emoción: vergüenza; límite: su cuerpo es privado"),
        W("Un secreto que da miedo", "Alex recibió un mensaje que dice: «Es un secreto entre los dos». Le da miedo. ¿Qué conviene hacer?", ["Un secreto que da miedo no se guarda.", "Se cuenta a una persona adulta de confianza.", "No es culpa de Alex."], "Contárselo a una persona adulta de confianza"),
    ],
    [
        M("Pensar que si cambio de ánimo muy rápido, algo está mal conmigo.", "Se cree que los afectos deben ser siempre iguales.", "En la pubertad es común; nómbralo y pide ayuda si pesa mucho."),
        M("Pensar que, si un amigo me pide un secreto, debo guardarlo aunque me dé miedo.", "Se confunde lealtad con obedecer.", "Los secretos que dan miedo o malestar se cuentan a un adulto de confianza."),
    ],
    R=[
        ex("«Estoy contento y diez minutos después irritable». ¿Puede ser un cambio de ánimo de la pubertad?", "Sí", "El ánimo cambia con más rapidez en esta etapa."),
        ex("Tu cuerpo, ¿es tuyo o de quien quiera tocarlo?", "Es tuyo", "Nadie puede tocarlo sin que tú quieras."),
        ex("«Cambiarse de ropa». ¿Es un momento privado?", "Sí", "Tienes derecho a hacerlo sin que te miren."),
    ],
    U=[
        ex("¿Por qué conviene distinguir hecho, emoción y límite?", "Para entender qué pasó, qué siento y qué no acepto", "Cada parte ayuda a decidir qué hacer."),
        ex("Un secreto que da miedo, ¿se guarda o se cuenta a un adulto de confianza?", "Se cuenta a un adulto de confianza", "Un secreto que da miedo puede ser peligroso."),
        ex("Querer privacidad en la pubertad, ¿es raro o es un derecho?", "Es un derecho", "Todas las personas pueden tener momentos privados."),
    ],
    A=[
        ex("Frases: 1) «me miró mientras me cambiaba», 2) «me da vergüenza», 3) «no quiero que me miren». ¿Cuál es el límite?", "La frase 3", "Dice lo que la persona no acepta."),
        ex("Un niño inventado golpea la puerta antes de entrar al baño de su casa. ¿Qué respeta: la privacidad de los demás o la hora de la comida?", "La privacidad de los demás", "Golpear la puerta es una forma de respetar el espacio."),
        ex("Frase de Alex: «Siento nervios cuando mi amiga me habla». ¿Es un hecho, una emoción o un límite?", "Una emoción", "Dice lo que siente Alex."),
    ],
    Z=[
        ex("Dos amigos: uno ya siente atracción por alguien y el otro todavía no. ¿Alguno está mal?", "Ninguno", "Cada persona vive esta etapa a su ritmo."),
        ex("Un compañero pregunta cosas muy íntimas sobre el cuerpo de otra persona. ¿Cuál es el límite que debe respetar?", "La privacidad de esa persona", "Tiene derecho a no responder."),
    ],
    D=[
        arith("En una semana Noa anotó que su ánimo cambió 3 veces el lunes, 2 el martes y 1 el miércoles. ¿Cuántos cambios anotó?", "3+2+1", "Se suman los cambios de los tres días."),
        arith("De 25 estudiantes, 10 dijeron que quieren más privacidad en el baño. ¿Cuántos no lo dijeron?", "25-10", "Se restan los que lo dijeron al total."),
    ],
    context=[ex("En el camarín, un niño inventado le dice a otro: «Déjame cambiarme tranquilo». El otro responde: «Perdón, me doy vuelta». ¿Respetó el límite?", "Sí", "Aceptó el pedido y respetó la privacidad.")],
    selfcheck=[ex("En Orientación: ¿un secreto que da miedo se cuenta a un adulto de confianza?", "Sí", "Es una forma de cuidarse."), ex("¿Tienes derecho a privacidad?", "Sí", "Es un derecho de todas las personas."), ex("¿Los cambios de ánimo son comunes en la pubertad?", "Sí", "Aparecen por los cambios del cuerpo.")],
    task=T("Lee el caso de Noa: «Noa nota que su ánimo cambia rápido: un rato ríe con sus amigas y después se siente irritable. Un compañero hizo un comentario sobre su cuerpo y ella quedó callada». Escribe el hecho, la emoción y el límite de Noa, y una frase respetuosa que ella podría decir al compañero.", "Hecho: el compañero comentó sobre su cuerpo. Emoción: vergüenza. Límite: mi cuerpo no es tema de comentarios. Frase: «No me gusta que comentes mi cuerpo; por favor, no lo hagas».", ["escribe el hecho", "nombra la emoción", "dice el límite", "propone una frase respetuosa"], ["texto escrito o dicho"], ["mezclar emoción con hecho", "frase que insulta"], "Reconoce la separación y pregunta con quién podría hablar Noa si el comentario se repite."),
    reinforce="Escribe un hecho, una emoción y un límite para una situación inventada de burla por el cuerpo.",
    extend="Escribe dos frases para pedir privacidad con respeto.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. El caso de Alex y las opciones están escritos en los ejercicios.",
    "Aprenderé a comparar opciones ante comentarios o burlas por los cambios del cuerpo, y a prever consecuencias. Sirve para elegir respuestas respetuosas.",
    ["Sé que los cambios de la pubertad ocurren a ritmos distintos.", "Sé distinguir hecho, emoción y límite."],
    [
        "Durante la pubertad aparecen comentarios sobre el cuerpo: «¡qué alto!», «¡tu voz suena rara!», «¡tienes granos!». A veces son bromas y a veces son burlas que hieren. Ante un comentario así hay varias opciones. Puedes reírte para encajar, burlarte también, ignorar, decir con calma que no te gusta, apoyar a quien recibe la burla o avisar a un adulto.",
        "Cada opción tiene consecuencias. Burlarte hace que otros se sientan mal y puede pasar a ser acoso, que es una agresión repetida. Reírte «por si acaso» también puede animar a quien se burla. Decir con calma «no me gusta ese comentario» pone un límite. Acompañar a quien recibe la burla le muestra apoyo. Avisar a un adulto es una opción segura cuando la burla se repite o te sientes inseguro.",
        "Una buena regla es esta: antes de comentar el cuerpo de alguien, pregúntate si lo diría con respeto y si la otra persona se sentiría bien. Si la respuesta es no, mejor no lo digas. El cuerpo de cada persona merece respeto, sea cual sea su ritmo de cambio.",
    ],
    [("burla", "comentario que hiere a alguien"), ("acoso", "agresión que se repite contra alguien"), ("respeto", "tratar a alguien con consideración"), ("apoyar", "acompañar a alguien que lo necesita"), ("opción", "una de las formas posibles de actuar")],
    [
        W("Comparar dos opciones", "Un compañero se burla de la voz de Luis. Opción A: reírse. Opción B: decir «no me parece gracioso». ¿Cuál tiene mejor consecuencia para Luis?", ["Reírse anima la burla y Luis se siente peor.", "Decir «no me parece gracioso» pone un límite.", "Apoya a Luis sin atacar."], "La opción B"),
        W("Saber cuándo avisar", "La burla contra Luis se repite todos los días. ¿Qué conviene hacer además de decir que no te parece bien?", ["Que sea una burla repetida la vuelve acoso.", "Un adulto puede detenerla.", "Avisar es una opción segura."], "Avisar a un adulto del colegio"),
    ],
    [
        M("Reírme para que no se rían de mí.", "Se piensa que reírse es la forma de encajar.", "Puedes decir que no te parece gracioso o simplemente no unirte."),
        M("Creer que avisar a un adulto es acusar.", "Se confunde cuidar con delatar.", "Avisar cuando alguien es herido de forma repetida es cuidar."),
    ],
    R=[
        ex("Reírse de una burla, ¿ayuda a quien la recibe o lo hiere más?", "Lo hiere más", "Anima a quien se burla."),
        ex("«No me gusta ese comentario». ¿Es una opción respetuosa?", "Sí", "Pone un límite sin atacar."),
        ex("Una burla que se repite todos los días, ¿es una broma o puede ser acoso?", "Puede ser acoso", "Una agresión repetida se llama acoso."),
    ],
    U=[
        ex("¿Por qué acompañar a quien recibe la burla es una buena opción?", "Porque le muestra apoyo", "Se siente menos solo."),
        ex("¿Cuándo es útil avisar a un adulto del colegio?", "Cuando la burla se repite o hay inseguridad", "Un adulto puede detenerla."),
        ex("Antes de comentar el cuerpo de alguien, ¿qué conviene preguntarse?", "Si lo diría con respeto y la otra persona se sentiría bien", "Ayuda a evitar comentarios que hieren."),
    ],
    A=[
        ex("Opciones ante una burla: 1) reírse, 2) decir «no me gusta», 3) acompañar a la víctima, 4) avisar a un adulto. ¿Cuántas ayudan a detener o reducir la burla?", "3", "Las opciones 2, 3 y 4 ayudan; reírse la anima."),
        ex("Alex ve que se burlan de los granos de Mía. ¿Qué es más respetuoso: «Eso no se dice» o «Qué asco»?", "«Eso no se dice»", "Pone un límite sin sumarse a la burla."),
        ex("Mía quedó triste. ¿Qué puede hacer Alex para apoyarla: acompañarla o ignorarla?", "Acompañarla", "Le muestra que no está sola."),
    ],
    Z=[
        ex("Una niña piensa: «Si me quedo callada, la burla se detiene sola». ¿Es seguro?", "No", "Puede continuar; avisar o poner un límite ayuda."),
        ex("¿Por qué una broma sobre el cuerpo puede herir aunque la persona se ría?", "Porque puede reír por vergüenza", "Reír no siempre significa que le guste."),
    ],
    D=[
        arith("En una semana, a Luis le hicieron burlas 2 veces el lunes, 1 el martes y 3 el miércoles. ¿Cuántas burlas en total?", "2+1+3", "Se suman las burlas de los tres días."),
        arith("De 28 estudiantes, 7 dijeron que avisarían a un adulto. ¿Cuántos no lo dijeron?", "28-7", "Se restan los que lo dijeron al total."),
    ],
    context=[ex("Alex y dos amigos ven que un grupo se burla de la estatura de un niño. Alex dice: «Eso no está bien», y los tres lo acompañan al patio. ¿Qué opción usaron?", "Poner un límite y acompañar", "Dijeron que no estaba bien y le mostraron apoyo.")],
    selfcheck=[ex("En Orientación: ¿una burla repetida puede ser acoso?", "Sí", "Una agresión repetida se llama acoso."), ex("¿Acompañar a quien recibe una burla es apoyar?", "Sí", "Le muestra que no está solo."), ex("¿Avisar cuando alguien se siente herido es cuidar?", "Sí", "Busca ayuda para detener el daño.")],
    task=T("Lee el caso: «Un grupo se burla de los granos de Mía y de la voz de Luis cada día». Escribe dos opciones para Alex (que lo ve). Para cada una escribe una consecuencia para Mía y Luis y otra para el grupo. Elige una y explica por qué.", "Opción 1: decir «no está bien». Consecuencia para Mía y Luis: se sienten acompañados; para el grupo: saben que alguien los frena. Opción 2: avisar a la orientadora. Elijo avisar porque se repite todos los días.", ["escribe dos opciones", "escribe dos consecuencias por opción", "elige una y la justifica", "no incluye burlas ni insultos"], ["texto escrito o dicho", "cuadro de dos columnas"], ["elegir reírse", "no pensar en la consecuencia"], "Reconoce las consecuencias y pregunta si la opción elegida es segura."),
    reinforce="Escribe tres frases respetuosas para detener una burla sobre el cuerpo.",
    extend="Escribe qué harías si un amigo tuyo es quien se burla.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. Los casos de Sam y Noa están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura para expresar afecto con respeto y consentimiento. Sirve para relacionarme bien con amigos y compañeros.",
    ["Sé que mi cuerpo es mío y que tengo límites.", "Sé comparar opciones y consecuencias."],
    [
        "Expresar afecto es mostrar cariño a alguien. Se puede hacer de muchas formas: con palabras amables, con un gesto, con ayuda, con un regalo o con un abrazo. En la pubertad, a veces aparece interés especial por una persona, y eso se llama gustar de alguien. También es normal no sentirlo todavía. Cada persona se relaciona a su ritmo.",
        "Una forma respetuosa de expresar afecto requiere consentimiento. Consentimiento es decir «sí» de forma libre, sin presión ni engaño, y se puede retirar en cualquier momento. Si no estás seguro, preguntas: «¿Quieres un abrazo?». Si la respuesta es «no», o si la persona se queda callada o se aleja, no insistes. Nadie debe tocar a otra persona si ella no quiere, ni presionarla para hacer algo con su cuerpo.",
        "Algunas formas apropiadas a esta edad son hablar con amabilidad, ayudar, invitar a jugar o escribir una nota respetuosa. Algunas formas que no son apropiadas son perseguir, presionar, tocar sin permiso o enviar mensajes insistentes. Si alguien, de cualquier edad, te presiona o te hace sentir incómodo, di que no y avisa a un adulto de confianza. No es tu culpa.",
    ],
    [("afecto", "sentimiento de cariño hacia alguien"), ("consentimiento", "decir «sí» de forma libre, sin presión; se puede retirar"), ("presión", "insistir para que alguien haga algo que no quiere"), ("respeto", "tratar a alguien con consideración"), ("insistir", "pedir una y otra vez algo que ya se negó")],
    [
        W("Pedir consentimiento", "Sam quiere dar un abrazo a su amiga Mía, que está triste. ¿Qué hace primero?", ["El abrazo es tocar el cuerpo de otra persona.", "Debe preguntar: «¿Quieres un abrazo?».", "Si dice que no, Sam acepta."], "Preguntarle si quiere un abrazo"),
        W("Una respuesta que no es un sí", "Sam pregunta si quiere un abrazo y Mía se queda callada y se aleja. ¿Es un sí?", ["Un sí es libre y claro.", "Quedarse callada y alejarse no es un sí.", "Sam respeta y no insiste."], "No, no es un sí"),
    ],
    [
        M("Creer que si alguien no dice «no», entonces dijo «sí».", "Se confunde silencio con permiso.", "Un sí es claro y libre; si no lo es, no sigas."),
        M("Insistir cuando alguien dijo que no, porque «seguro cambia de idea».", "Se piensa que insistir demuestra cariño.", "Insistir es presionar; respeta el «no»."),
    ],
    R=[
        ex("Consentimiento: ¿es decir «sí» libremente o aceptar por miedo?", "Decir «sí» libremente", "Es un sí sin presión."),
        ex("Una persona dice «no quiero un abrazo». ¿Qué haces?", "Respetarlo", "El cuerpo es suyo y decide ella."),
        ex("«Invitar a jugar» ¿es una forma apropiada de mostrar afecto?", "Sí", "Es amable y no obliga a nadie."),
    ],
    U=[
        ex("¿Por qué quedarse callada no es un «sí»?", "Porque el sí debe ser claro y libre", "El silencio puede ser miedo o duda."),
        ex("¿Se puede retirar un consentimiento después de darlo?", "Sí", "La persona puede cambiar de idea cuando quiera."),
        ex("¿Gustar de alguien obliga a esa persona a corresponder?", "No", "Cada persona decide cómo se siente y cómo se relaciona."),
    ],
    A=[
        ex("Formas de expresar afecto: 1) ayudar con la tarea, 2) perseguir en el recreo, 3) escribir una nota amable, 4) abrazar sin preguntar. ¿Cuántas son apropiadas?", "2", "Las formas 1 y 3 respetan a la otra persona; 2 y 4 no."),
        ex("Noa dice: «Prefiero que solo nos saludemos». ¿Qué respuesta respeta su decisión: «Está bien» o «Dale, solo un poquito»?", "«Está bien»", "Acepta su decisión sin presionar."),
        ex("¿Qué frase pide permiso: «¿Quieres que te dé un abrazo?» o «Te voy a dar un abrazo»?", "«¿Quieres que te dé un abrazo?»", "Pregunta y deja decidir."),
    ],
    Z=[
        ex("Un niño dice: «Si le doy muchos regalos, me tiene que querer». ¿Es correcto?", "No", "Nadie está obligado a corresponder por regalos."),
        ex("Si te presionan para hacer algo con tu cuerpo y sientes incomodidad, ¿qué debes hacer?", "Decir que no y avisar a un adulto de confianza", "Tu cuerpo es tuyo y puedes pedir ayuda."),
    ],
    D=[
        arith("De 24 estudiantes, 18 dijeron que pedirían permiso antes de abrazar. ¿Cuántos no lo dijeron?", "24-18", "Se restan los que lo dijeron al total."),
        arith("Noa escribió 3 notas amables por semana durante 4 semanas. ¿Cuántas escribió?", "3*4", "Son 3 notas repetidas en 4 semanas."),
    ],
    context=[ex("Un niño inventado quiere saludar a un compañero que no conoce bien. Pregunta: «¿Te saludo con la mano?». El compañero dice «mejor con la mano en alto». ¿El niño respetó el consentimiento?", "Sí", "Preguntó y aceptó la forma que la otra persona prefirió.")],
    selfcheck=[ex("En Orientación: ¿el consentimiento es un sí libre?", "Sí", "No hay presión."), ex("¿Se puede insistir cuando alguien dice no?", "No", "Hay que respetar el no."), ex("¿Es normal que algunas personas todavía no sientan interés especial por otras?", "Sí", "Cada persona tiene su ritmo.")],
    task=T("Lee: «Sam quiere mostrar cariño a su amiga Noa, que lo ayudó con la tarea». Escribe tres formas apropiadas de mostrarle afecto y una frase para pedir permiso antes de un gesto físico. Escribe también qué haría Sam si Noa responde «no».", "Formas: darle las gracias, invitarla a jugar, escribir una nota. Frase: «¿Quieres un abrazo?». Si responde no: «Está bien» y sigue conversando.", ["tres formas apropiadas", "una frase para pedir permiso", "qué hace si hay un no"], ["texto escrito o dicho"], ["acciones que presionan", "no aceptar el no"], "Reconoce el respeto y pregunta cómo se sentiría Noa en cada caso."),
    reinforce="Escribe tres formas de decir «gracias» o «me importas» sin tocar a nadie.",
    extend="Escribe qué harías si alguien te presiona para un gesto físico que no quieres.",
)

lesson(
    OA3, 5,
    "Una hoja y un lápiz. Las situaciones y las frases están escritas en los ejercicios.",
    "Aprenderé a pedir ayuda y a buscar información confiable sobre los cambios de la pubertad. Sirve para resolver dudas sin pasar vergüenza ni informarme mal.",
    ["Sé que mi cuerpo y mi intimidad tienen límites.", "Sé que puedo contar con una persona adulta de confianza."],
    [
        "Es normal tener dudas sobre la pubertad: ¿por qué cambia mi voz?, ¿qué es la menstruación?, ¿por qué siento tanta vergüenza? Preguntar es una forma de cuidarte. Para preguntar bien, puedes elegir a una persona adulta de confianza: alguien de tu casa, tu profesor o profesora, el orientador, una profesional de la salud. Puedes decir: «Tengo una duda y me da vergüenza preguntar. ¿Podemos hablar?».",
        "No toda la información sirve. Una fuente confiable tiene un autor o una institución que se pueda identificar, como un ministerio de salud, un hospital o un libro de la biblioteca del colegio. Usa un lenguaje claro y respetuoso y no pide datos personales. Una fuente poco confiable promete «secretos» o «trucos», no dice quién escribe o pide datos como tu nombre completo o tu dirección.",
        "Si un compañero te cuenta algo sobre los cambios del cuerpo, puede estar equivocado. Antes de creerlo, compáralo con lo que dice una fuente confiable o pregúntale a un adulto. Si alguien te da información que te hace sentir incómodo, o te pide guardar un secreto, avisa a un adulto de confianza.",
    ],
    [("duda", "pregunta que aún no tiene respuesta"), ("fuente confiable", "lugar de información con autor o institución identificable y datos correctos"), ("adulto de confianza", "persona adulta con la que me siento seguro de hablar"), ("profesional de la salud", "persona formada para cuidar la salud"), ("comparar fuentes", "revisar si dos fuentes dicen lo mismo")],
    [
        W("Elegir a quién preguntar", "Una niña inventada tiene una duda sobre la menstruación. Puede preguntar a (a) un compañero que dice saber todo o (b) una profesional de la salud del consultorio. ¿Quién le dará información más confiable?", ["Un compañero puede equivocarse.", "Una profesional de la salud estudió el tema.", "La información debe ser clara y segura."], "(b), la profesional de la salud"),
        W("Una fuente confiable", "Una página dice: «Secretos que tus padres no te cuentan. Entra tu nombre completo y tu dirección». ¿Es confiable?", ["Promete «secretos».", "Pide datos personales.", "No dice quién escribe."], "No es confiable"),
    ],
    [
        M("Creer todo lo que dice el compañero que sabe más.", "Se confunde seguridad al hablar con información correcta.", "Comparar con una fuente confiable o preguntar a un adulto."),
        M("Quedarme con la duda porque me da vergüenza.", "Se piensa que preguntar es mostrar debilidad.", "Prepara una frase para pedir hablar con calma."),
    ],
    R=[
        ex("Si tienes una duda sobre la pubertad, ¿es bueno preguntarla a una persona adulta de confianza?", "Sí", "Preguntar es una forma de cuidarte."),
        ex("Una fuente confiable, ¿tiene un autor o institución identificable o no se sabe quién escribe?", "Tiene un autor o institución identificable", "Eso permite confiar en los datos."),
        ex("Una página que pide tu nombre completo y dirección para dar información, ¿es confiable?", "No", "Una fuente confiable no pide datos personales."),
    ],
    U=[
        ex("¿Por qué conviene comparar lo que dice un compañero con una fuente confiable?", "Porque el compañero puede estar equivocado", "Revisar evita creer información falsa."),
        ex("¿Qué frase sirve para empezar a preguntar con vergüenza: «Tengo una duda y me da vergüenza; ¿podemos hablar?» o «No quiero preguntar nada»?", "«Tengo una duda y me da vergüenza; ¿podemos hablar?»", "Dice lo que necesitas y pide un momento."),
        ex("Un adulto te pide guardar un secreto sobre tu cuerpo. ¿Qué haces?", "Aviso a otro adulto de confianza", "Un secreto sobre tu cuerpo no debe guardarse."),
    ],
    A=[
        ex("Fuentes: 1) libro de la biblioteca del colegio, 2) página sin autor que promete «trucos», 3) ministerio de salud, 4) mensaje que pide tu dirección. ¿Cuántas son confiables?", "2", "El libro y el ministerio de salud tienen institución identificable; las otras no."),
        ex("Para ordenar tus ideas antes de hablar, ¿qué ayuda más: escribir tu duda en una hoja o esperar a que se te ocurra en el momento?", "Escribir tu duda en una hoja", "Escribir prepara lo que se quiere decir y baja la vergüenza."),
        ex("Un amigo dice: «Dicen que no tienes que bañarte en la pubertad». ¿Qué haces: compararlo con una fuente confiable o creerle?", "Compararlo con una fuente confiable", "La higiene es importante en la pubertad y hay que revisar."),
    ],
    Z=[
        ex("¿Por qué una persona adulta de confianza puede ser mejor para responder que una búsqueda sin criterio?", "Porque conoce a la persona y puede explicar con cuidado", "Evita información equivocada o demasiado fuerte."),
        ex("¿Qué signo muestra que una fuente de información no es segura?", "Pide datos personales o promete secretos", "Una fuente segura informa sin pedir datos privados."),
    ],
    D=[
        arith("En una lista de 15 fuentes, 9 son confiables. ¿Cuántas no lo son?", "15-9", "Se restan las confiables al total."),
        arith("Noa preparó 3 preguntas y le respondieron 2. ¿Cuántas quedan por preguntar?", "3-2", "Se resta lo respondido a lo preparado."),
    ],
    context=[ex("Un niño inventado ve en una página: «Hospital Regional: Qué es la pubertad». Tiene autor, fecha y no pide datos. ¿Es una fuente confiable?", "Sí", "Tiene institución, fecha y no pide datos personales.")],
    selfcheck=[ex("En Orientación: ¿preguntar sobre la pubertad es una forma de cuidarse?", "Sí", "Ayuda a resolver dudas con información correcta."), ex("¿Una fuente que pide tus datos personales es confiable?", "No", "No debe pedirlos."), ex("¿Puedes pedir hablar con un adulto de confianza?", "Sí", "Es una forma de pedir ayuda.")],
    task=T("Escribe tres preguntas que podrías hacer sobre la pubertad (por ejemplo, sobre higiene, ánimo o cambios del cuerpo). Para cada una, escribe a quién la harías y por qué. Después escribe una frase para empezar a conversar con vergüenza.", "Pregunta: ¿cómo cuido mi cuerpo cuando sudo más? A: la orientadora, porque sabe de hábitos. Frase: «Tengo una duda y me da vergüenza preguntar; ¿podemos hablar?»", ["tres preguntas con destinatario", "razón de por qué", "una frase para comenzar", "no incluye datos personales"], ["lista escrita o dicha"], ["elegir a quien no tiene información", "frase que ofende"], "Reconoce la preparación y pregunta cómo comprobaría la respuesta."),
    reinforce="Haz una lista de dos adultos de confianza a quienes podrías preguntar y una frase para cada uno.",
    extend="Explica por qué una fuente confiable no pide tu nombre completo ni tu dirección.",
)

# ================================================================ OA 04
lesson(
    OA4, 1,
    "Una hoja y un lápiz. El caso de Alex está escrito en los ejercicios. Trabajas con personajes inventados.",
    "Aprenderé qué información debo proteger y qué hacer cuando un mensaje me incomoda. Sirve para cuidar mi intimidad dentro y fuera de las redes.",
    ["Sé que mi cuerpo es mío y que tengo derecho a decir que no.", "Sé que puedo contar con una persona adulta de confianza."],
    [
        "Tu intimidad es todo lo que es privado de ti: tu cuerpo, tus fotos íntimas, tus emociones más personales y tu información personal. Información personal es tu nombre completo, tu dirección, tu colegio, tu teléfono, tus contraseñas y las rutinas de tu familia. Esta información no se comparte con desconocidos ni se publica en redes sociales.",
        "Una foto íntima es una imagen donde se ve tu cuerpo de forma privada. Nadie tiene derecho a pedirte una, y tú no debes enviar ninguna. Si alguien te pide una foto íntima, aunque sea un amigo o digan que es un juego, la respuesta es no. Lo que se envía por una pantalla puede copiarse y reenviarse, y ya no puedes controlarlo. Si ya enviaste una, cuéntalo igual a un adulto de confianza: no es tu culpa y te pueden ayudar.",
        "Si recibes un mensaje que te incomoda, sigue tres pasos. Primero, no respondas. Segundo, guarda el mensaje o haz una captura como evidencia, y no lo reenvíes a nadie. Tercero, cuéntaselo a una persona adulta de confianza. Si el mensaje te pide algo sexual, no es tu culpa. La responsabilidad es de quien lo envió.",
    ],
    [("intimidad", "todo lo privado de mí, como mi cuerpo y mis fotos íntimas"), ("información personal", "datos como nombre completo, dirección o contraseñas"), ("foto íntima", "imagen donde se ve el cuerpo de forma privada"), ("evidencia", "mensaje o captura que muestra lo que pasó"), ("incómodo", "que hace sentir mal o inseguro")],
    [
        W("Reconocer información personal", "¿Cuál es información personal: «mi dirección» o «mi color favorito»?", ["Información personal permite ubicar o identificar a alguien.", "La dirección dice dónde vive.", "El color favorito no pone en riesgo."], "«Mi dirección»"),
        W("Qué hacer ante un mensaje incómodo", "Alex recibe un mensaje que le pide una foto íntima de su cuerpo. ¿Cuáles son los tres pasos?", ["No responde.", "Guarda una captura.", "Se lo cuenta a un adulto de confianza."], "No responder, guardar la evidencia y avisar a un adulto"),
    ],
    [
        M("Pensar que si alguien me pide una foto íntima y digo que no, es mi culpa que insista.", "Se cree que uno provocó la situación.", "No es tu culpa; la responsabilidad es de quien pide."),
        M("Borrar el mensaje sin contarle a nadie.", "Se quiere olvidar lo que incomoda.", "Guarda una captura y avisa a un adulto de confianza."),
    ],
    R=[
        ex("Tu nombre completo, ¿es información personal?", "Sí", "Con ese dato otra persona puede identificarte."),
        ex("Si alguien pide una foto íntima, ¿la respuesta es sí o no?", "No", "Nadie tiene derecho a pedirla."),
        ex("Cuando un mensaje te incomoda, ¿primero respondes o no respondes?", "No respondes", "Responder puede empeorar la situación."),
    ],
    U=[
        ex("¿Por qué no se debe enviar una foto íntima aunque sea a un amigo?", "Porque se puede copiar y reenviar", "Después ya no se puede controlar."),
        ex("¿Qué se debe hacer con el mensaje que incomoda: guardarlo como evidencia o borrarlo sin contarlo?", "Guardarlo como evidencia", "La evidencia ayuda a un adulto a actuar."),
        ex("Si alguien te envía un mensaje sexual, ¿de quién es la responsabilidad?", "De quien lo envió", "No es culpa de quien lo recibe."),
    ],
    A=[
        ex("Lista: 1) mi dirección, 2) mi contraseña, 3) mi comida favorita, 4) el horario en que mi casa está vacía. ¿Cuántas son información personal que debo proteger?", "3", "Las opciones 1, 2 y 4 ponen en riesgo; la comida favorita no."),
        ex("Un desconocido dice: «Si me mandas una foto, te regalo un juego». ¿Qué haces: no respondes, guardas el mensaje y avisas a un adulto, o la envías rápido?", "No respondes, guardas el mensaje y avisas a un adulto", "Es la forma segura de actuar."),
        ex("Alex siente que algo no está bien con un mensaje. ¿Qué señal usa: su sensación de incomodidad o la presión del que escribe?", "Su sensación de incomodidad", "La incomodidad es una señal para parar y pedir ayuda."),
    ],
    Z=[
        ex("Un amigo dice: «Es solo un juego, nadie se enterará». ¿Qué error tiene?", "Una imagen enviada puede copiarse y compartirse", "Nada en una pantalla queda totalmente privado."),
        ex("¿Por qué no es buena idea responder furioso a quien envió un mensaje incómodo?", "Puede empeorar la situación y seguir la conversación", "Lo mejor es no responder, guardar el mensaje y pedir ayuda."),
    ],
    D=[
        arith("Alex tiene 12 mensajes en su celular inventado. 3 incomodan y el resto son normales. ¿Cuántos son normales?", "12-3", "Se restan los incómodos al total."),
        arith("En un curso de 30 estudiantes, 6 ya saben a qué adulto acudir. ¿Cuántos faltan por saberlo?", "30-6", "Se restan los que ya saben al total."),
    ],
    context=[ex("Mía recibe mensajes de un número desconocido que dicen: «Dime dónde vives y en qué colegio estás». Ella se lo muestra a una persona de su casa. ¿Actuó bien?", "Sí", "No respondió y avisó a un adulto de confianza.")],
    selfcheck=[ex("En Orientación: ¿tu dirección es información personal?", "Sí", "No se comparte con desconocidos."), ex("¿Una foto íntima se envía a un amigo?", "No", "La imagen puede copiarse y reenviarse."), ex("¿Es bueno contarle a un adulto de confianza un mensaje incómodo?", "Sí", "Un adulto puede ayudar.")],
    task=T("Lee los datos: «nombre completo, dirección, color favorito, contraseña del juego, colegio, comida favorita, horario en que no hay nadie en casa». Clasifícalos en «se pueden compartir» y «no se comparten con desconocidos». Después escribe los tres pasos para actuar si recibes un mensaje que te pide una foto íntima.", "Se pueden compartir: color favorito, comida favorita. No: nombre completo, dirección, contraseña, colegio, horario. Pasos: no respondo, guardo la captura, aviso a un adulto.", ["clasifica los siete datos", "escribe los tres pasos", "no cuenta nada privado propio"], ["lista escrita o dicha"], ["compartir la dirección", "borrar sin avisar"], "Reconoce la clasificación y pregunta a qué adulto acudiría."),
    reinforce="Escribe tres datos personales que no compartirías con un desconocido.",
    extend="Explica por qué una foto enviada no se puede controlar después.",
)

lesson(
    OA4, 2,
    "Una hoja y un lápiz. Los casos de Noa están escritos en los ejercicios.",
    "Aprenderé a separar lo que pasó, lo que siento y el límite que quiero poner ante manifestaciones de índole sexual inapropiadas. Sirve para protegerme y saber qué decir.",
    ["Sé qué es información personal.", "Sé que nadie debe pedir fotos íntimas."],
    [
        "Una manifestación de índole sexual inapropiada es una palabra, mensaje, imagen o gesto de contenido sexual que no corresponde a tu edad y no pediste. Puede ocurrir en persona o en una pantalla. Por ejemplo: un mensaje con imágenes de cuerpos desnudos, un comentario sexual sobre ti o alguien que te pide que le muestres tu cuerpo. No es tu culpa y no tienes que soportarlo.",
        "Cuando algo así ocurre, distingue tres cosas. El hecho: qué pasó exactamente. La emoción: lo que sientes, por ejemplo susto, vergüenza, asco o confusión. Y el límite: lo que no aceptas. Si es alguien que conoces en persona y te sientes seguro, puedes decir con pocas palabras: «No me gusta esto. Para». Si es un desconocido o una cuenta en línea, no respondas: bloquea, guarda la evidencia y avisa. Si la persona no para, te alejas y avisas a un adulto.",
        "A veces quien envía el mensaje dice «es un secreto» o «si cuentas, tendrás problemas». Eso es una señal de alerta. Los secretos que dan miedo o malestar siempre se cuentan a un adulto de confianza. Hablar protege.",
    ],
    [("inapropiado", "que no corresponde a la edad o a la situación"), ("señal de alerta", "algo que avisa que puede haber peligro"), ("secreto que da miedo", "algo que me piden ocultar y me hace sentir mal"), ("límite", "lo que no acepto"), ("avisar", "contar a una persona que puede ayudar")],
    [
        W("Identificar lo inapropiado", "Noa recibe una imagen de un cuerpo desnudo que no pidió. ¿Es una manifestación sexual inapropiada?", ["No la pidió.", "No corresponde a su edad.", "Le provoca incomodidad."], "Sí, es inapropiada"),
        W("Hecho, emoción y límite", "Noa dice: «Me enviaron una imagen, me dio vergüenza y bloqueo a esa persona». ¿Qué parte es el límite?", ["El hecho es la imagen.", "La emoción es la vergüenza.", "El límite es bloquear a esa persona."], "«Bloqueo a esa persona»"),
    ],
    [
        M("Pensar que una imagen sexual inesperada es culpa mía por haber abierto el mensaje.", "Se confunde abrir con provocar.", "Nadie debe enviarla; la responsabilidad es de quien la envió."),
        M("Guardar el secreto porque dijeron que si cuento tendré problemas.", "Se cree la amenaza.", "Un secreto que da miedo se cuenta a un adulto de confianza."),
    ],
    R=[
        ex("Una imagen sexual que no pediste, ¿es adecuada para tu edad?", "No", "No corresponde ni fue pedida."),
        ex("«No me gusta esto. Para». ¿Es un límite?", "Sí", "Dice lo que no se acepta."),
        ex("Si te dicen «si cuentas, tendrás problemas», ¿es una señal de alerta?", "Sí", "Se usa para que no pidas ayuda."),
    ],
    U=[
        ex("¿De quién es la responsabilidad si recibes un mensaje sexual que no pediste?", "De quien lo envió", "Tú no lo provocaste."),
        ex("¿Por qué un secreto que da miedo debe contarse?", "Porque puede haber peligro y un adulto puede ayudar", "Hablar con un adulto de confianza protege."),
        ex("Si una persona que ves en persona no para cuando le dices «para», ¿qué haces?", "Me alejo o cierro la conversación y aviso a un adulto", "Es una forma segura de protegerte."),
    ],
    A=[
        ex("Noa recibe una imagen que no pidió, le da susto y no sabe qué hacer. Ordena: A) avisar a un adulto, B) no responder, C) guardar el mensaje. ¿Cuál es el primer paso para no empeorar?", "B", "No responder evita seguir la conversación."),
        ex("Frases de Noa: 1) «Me enviaron una imagen», 2) «Me dio susto», 3) «Voy a bloquear esta cuenta». ¿Cuál es la emoción?", "La frase 2", "Dice lo que siente Noa."),
        ex("Un compañero repite comentarios sexuales sobre el cuerpo de una niña inventada. ¿Qué es lo correcto: reírse o decir «no está bien» y avisar a un adulto?", "Decir «no está bien» y avisar a un adulto", "Pone un límite y busca ayuda."),
    ],
    Z=[
        ex("¿Por qué la vergüenza no debe impedir que cuentes lo ocurrido?", "Porque no es tu culpa y un adulto puede ayudar", "La vergüenza es una emoción, no una prueba de culpa."),
        ex("Una amiga te cuenta que le pidieron una foto íntima. ¿Qué le aconsejas?", "Que no responda, guarde la evidencia y avise a un adulto", "Es la forma segura de actuar."),
    ],
    D=[
        arith("Un curso inventado tiene 32 estudiantes. 4 dicen que recibieron un mensaje incómodo. ¿Cuántos no lo recibieron?", "32-4", "Se restan los que lo recibieron al total."),
        arith("Noa puede contar a 3 adultos de confianza en casa y 2 en el colegio. ¿A cuántos adultos puede contar?", "3+2", "Se suman los dos grupos."),
    ],
    context=[ex("Alex recibe un chiste sexual de un contacto que no conoce. Siente incomodidad y lo muestra a su profesor. ¿Qué parte del plan seguro cumplió?", "Avisar a un adulto", "Compartió lo ocurrido con una persona que puede ayudar.")],
    selfcheck=[ex("En Orientación: ¿un mensaje sexual que no pedí es mi culpa?", "No", "La responsabilidad es de quien lo envió."), ex("¿Un secreto que da miedo se cuenta?", "Sí", "A un adulto de confianza."), ex("¿Decir «para» es poner un límite?", "Sí", "Dice lo que no aceptas.")],
    task=T("Lee: «Un contacto de una red social envía a Noa una imagen de un cuerpo desnudo y le dice que no cuente a nadie». Escribe: el hecho, la emoción posible, el límite que Noa pone y a quién le contaría.", "Hecho: me enviaron una imagen desnuda y pidieron secreto. Emoción: susto. Límite: no respondo y bloqueo la cuenta. Le cuento a mi profesor y a una persona de mi casa.", ["escribe el hecho", "nombra una emoción posible", "escribe un límite", "nombra a una persona adulta"], ["texto escrito o dicho"], ["culparse", "guardar el secreto"], "Reconoce el plan y pregunta si guardó la evidencia."),
    reinforce="Escribe tres señales de alerta en un mensaje de un desconocido.",
    extend="Explica por qué quien envió el mensaje es el responsable.",
)

lesson(
    OA4, 3,
    "Una hoja y un lápiz. El caso de Sam y las opciones están escritos en los ejercicios.",
    "Aprenderé a comparar opciones ante un mensaje o pedido que me incomoda en redes, y a prever consecuencias. Sirve para elegir la opción más segura.",
    ["Sé separar hecho, emoción y límite.", "Sé que un mensaje incómodo se guarda y se cuenta."],
    [
        "Sam recibe una solicitud de amistad de una cuenta que no conoce. La cuenta le escribe: «Hola, ¿cuántos años tienes y dónde vives?». Sam tiene varias opciones. Puede responder todo, hacerse el simpático, mostrárselo a un amigo, ignorar, bloquear, o contárselo a un adulto de confianza. Cada opción tiene consecuencias distintas.",
        "Responder con datos personales da información a un desconocido. Mostrárselo a un amigo no resuelve nada si el amigo tampoco sabe qué hacer. Ignorar puede dejar que la cuenta escriba otra vez. Bloquear impide que escriba, y reportar la cuenta avisa a la red social. Contárselo a un adulto de confianza permite saber qué hacer. La opción más segura combina varias: no responder, bloquear, guardar la evidencia y avisar.",
        "Para comparar opciones usa tres preguntas: ¿es segura para mí?, ¿protege mi intimidad?, ¿pide ayuda a quien puede dármela? Una opción que cumple las tres es la mejor.",
    ],
    [("bloquear", "impedir que una cuenta me escriba o me vea"), ("reportar", "avisar a la red social que una cuenta se comporta mal"), ("desconocido", "persona que no conozco en la vida real"), ("consecuencia", "lo que pasa después de una acción"), ("ignorar", "no responder ni hacer nada")],
    [
        W("Comparar opciones", "Sam recibe un mensaje de un desconocido que pregunta dónde vive. Opción A: responder la dirección. Opción B: bloquear, guardar captura y avisar. ¿Cuál es más segura?", ["A da información personal a un desconocido.", "B impide más mensajes y guarda evidencia.", "B busca ayuda adulta."], "La opción B"),
        W("Las tres preguntas", "Sam compara «ignorar» con «bloquear y avisar». ¿Cuál protege su intimidad y pide ayuda?", ["Ignorar no impide que escriban de nuevo.", "Bloquear y avisar corta y busca ayuda.", "Cumple las tres preguntas."], "Bloquear y avisar"),
    ],
    [
        M("Aceptar la solicitud para ver qué quiere.", "Se siente curiosidad por saber quién es.", "No aceptes a desconocidos."),
        M("Solo borrar el mensaje y no avisar.", "Se cree que así termina el problema.", "Guarda evidencia y cuéntalo a un adulto."),
    ],
    R=[
        ex("Responder con tu dirección a un desconocido, ¿es seguro?", "No", "Le das información que puede ponerte en riesgo."),
        ex("Bloquear una cuenta, ¿impide que te siga escribiendo?", "Sí", "La cuenta ya no puede contactarte."),
        ex("Reportar una cuenta, ¿avisa a la red social?", "Sí", "Permite que revisen el comportamiento."),
    ],
    U=[
        ex("¿Por qué mostrárselo solo a un amigo no basta?", "Porque el amigo tampoco puede resolverlo", "Se necesita un adulto de confianza."),
        ex("¿Qué plan es más seguro: «solo ignorar» o «bloquear, guardar captura y avisar»?", "Bloquear, guardar captura y avisar", "Corta el contacto y pide ayuda."),
        ex("¿Qué preguntas ayudan a comparar opciones?", "Si es segura, si protege mi intimidad y si pide ayuda", "Las tres miran la seguridad completa."),
    ],
    A=[
        ex("Opciones: 1) responder todo, 2) ignorar, 3) bloquear sin contarle a nadie, 4) bloquear y avisar a un adulto con la captura. ¿Cuántas cumplen las tres preguntas (seguras, protegen intimidad, piden ayuda)?", "1", "Solo la opción 4 cumple las tres; la 3 corta el contacto pero no pide ayuda."),
        ex("Sam rechazó la solicitud y guardó el mensaje. ¿Qué parte del plan le falta?", "Contárselo a un adulto de confianza", "Aún no pidió ayuda."),
        ex("Una cuenta insiste: «Dime tu colegio». ¿Qué conviene: responder «no te lo diré» o bloquear?", "Bloquear", "Responder mantiene la conversación abierta."),
    ],
    Z=[
        ex("Un niño piensa: «Si ignoro, el problema desaparece». ¿Por qué puede no ser cierto?", "La cuenta puede volver a escribir", "Ignorar no corta el contacto."),
        ex("¿Por qué no es buena idea aceptar a alguien que no conoces para «saber quién es»?", "Porque da acceso a tu información", "Una cuenta aceptada puede ver tus datos."),
    ],
    D=[
        arith("Sam tiene 40 contactos. 3 son desconocidos y los bloquea. ¿Cuántos contactos le quedan?", "40-3", "Se restan los bloqueados al total."),
        arith("Una niña inventada bloquea 2 cuentas en la mañana y 4 en la tarde. ¿Cuántas cuentas bloqueó?", "2+4", "Se suman las de la mañana y las de la tarde."),
    ],
    context=[ex("Luz recibe: «Hola, vi tu foto. ¿Nos vemos en el parque solos?». ¿Qué opción es la más segura: aceptar ir, o no responder, bloquear y avisar?", "No responder, bloquear y avisar", "Evita un encuentro peligroso y pide ayuda.")],
    selfcheck=[ex("En Orientación: ¿bloquear a un desconocido es una opción segura?", "Sí", "Corta el contacto."), ex("¿Hay que aceptar solicitudes de desconocidos?", "No", "Pueden poner en riesgo tu intimidad."), ex("¿Avisar a un adulto es parte del plan seguro?", "Sí", "Un adulto puede ayudar.")],
    task=T("Sam recibe el mensaje: «Hola, ¿cuántos años tienes? Mándame una foto y te cuento un secreto». Compara dos opciones: A) responder con curiosidad y B) bloquear, guardar captura y avisar a un adulto. Para cada una escribe una consecuencia para Sam. Aplica las tres preguntas a la opción elegida.", "A: Sam da información y puede recibir más mensajes. B: Sam corta el contacto y recibe apoyo. Elijo B: es segura, protege mi intimidad y pide ayuda.", ["compara dos opciones", "escribe una consecuencia por opción", "aplica las tres preguntas a la opción elegida"], ["texto escrito o dicho", "cuadro de dos columnas"], ["elegir responder con datos", "no pedir ayuda"], "Reconoce la comparación y pregunta qué adulto elegiría."),
    reinforce="Escribe tres consecuencias de aceptar a un desconocido en una red social.",
    extend="Agrega una tercera opción al caso de Sam y aplícale las tres preguntas.",
)

lesson(
    OA4, 4,
    "Una hoja y un lápiz. Las listas de ajustes y contraseñas están escritas en los ejercicios.",
    "Aprenderé a elegir acciones seguras para usar redes sociales: cuidar contraseñas, perfil, publicaciones y encuentros. Sirve para protegerme de forma autónoma.",
    ["Sé qué es información personal.", "Sé comparar opciones ante un mensaje incómodo."],
    [
        "Usar redes sociales de forma segura requiere decisiones tuyas. Muchas redes piden tener al menos 13 años para abrir una cuenta, así que si eres menor de esa edad, el uso lo acuerdas con una persona adulta de tu casa. Cuando uses una red o un juego en línea, tu perfil debe ser privado, tu nombre de usuario no debe mostrar tu nombre completo y tu foto no debe mostrar el colegio ni la dirección.",
        "Las contraseñas se protegen. Una contraseña segura es larga, mezcla letras, números y símbolos y no incluye tu nombre ni tu fecha de nacimiento. No se comparte con amigos, ni siquiera con los más cercanos. Cada cuenta debe tener una distinta.",
        "Antes de publicar algo, pregúntate: ¿me gustaría que lo viera cualquier persona?, ¿muestra datos personales?, ¿podría herir a alguien? Lo que se publica puede copiarse y quedar mucho tiempo. Nunca te encuentres en persona con alguien que conociste solo en línea. Si alguien lo propone, avisa a un adulto de confianza.",
    ],
    [("perfil privado", "cuenta que solo ven las personas que acepto"), ("contraseña segura", "clave larga y distinta que no se comparte"), ("nombre de usuario", "nombre que se muestra en una cuenta"), ("publicar", "poner algo en línea para que otros lo vean"), ("encuentro", "reunirse en persona con alguien")],
    [
        W("Cuidar el perfil", "¿Cuál nombre de usuario es más seguro: «Valentina_Rojas_5B» o «estrella_azul»?", ["El primero dice el nombre y el curso.", "El segundo no dice datos reales.", "Un nombre seguro no revela quién eres."], "«estrella_azul»"),
        W("Contraseña segura", "¿Cuál contraseña es más segura: «sam2015» o «Lluvia_Tren_47»?", ["La primera usa un nombre y un año fácil de adivinar.", "La segunda es larga y mezcla letras, números y símbolo.", "No incluye datos personales."], "«Lluvia_Tren_47»"),
    ],
    [
        M("Compartir mi contraseña con mi mejor amigo.", "Se confunde confianza con compartir claves.", "La contraseña no se comparte con nadie, solo con un adulto de tu casa si lo acuerdan."),
        M("Pensar que el perfil público es más divertido.", "Se busca recibir más reacciones.", "Un perfil privado protege tu información."),
    ],
    R=[
        ex("Un perfil privado, ¿lo ven todas las personas o solo quienes acepto?", "Solo quienes acepto", "Protege tu información."),
        ex("Tu contraseña, ¿se comparte con los amigos?", "No", "Debe mantenerse en secreto."),
        ex("Una foto de perfil que muestra el uniforme con el nombre del colegio, ¿es segura?", "No", "Revela dónde estudias."),
    ],
    U=[
        ex("¿Por qué una contraseña con tu nombre y fecha de nacimiento es débil?", "Porque es fácil de adivinar", "Otros pueden probar esos datos."),
        ex("¿Qué se hace antes de publicar algo?", "Pensar si lo vería cualquier persona y si muestra datos", "Así se evita lo que no se puede borrar del todo."),
        ex("Si conoces a alguien solo en línea y quiere verte, ¿qué haces?", "Aviso a un adulto de confianza y no voy", "Un encuentro así puede ser peligroso."),
    ],
    A=[
        ex("Contraseñas: 1) «Pelota123», 2) «Mi_Cielo_Nube_58», 3) «nombrecompleto», 4) «01012014». ¿Cuántas son seguras?", "1", "Solo la 2 es larga, mezcla y no usa datos personales."),
        ex("Una niña inventada va a publicar una foto en su casa donde se ve el número de su casa. ¿Qué hace: recortar o tapar el número, o publicarla igual?", "Recortar o tapar el número", "Evita mostrar su dirección."),
        ex("Ajustes: A) perfil público, B) perfil privado con contactos conocidos. ¿Cuál es más seguro?", "B", "Controla quién ve su información."),
    ],
    Z=[
        ex("Un niño dice: «Mi amigo es de confianza, le doy mi clave». ¿Qué problema tiene?", "Su amigo podría compartirla o usarla sin querer", "La clave no debe compartirse."),
        ex("¿Por qué lo que publicas puede durar mucho tiempo aunque lo borres?", "Porque otros pueden copiarlo o guardarlo", "Una captura basta para conservarlo."),
    ],
    D=[
        arith("Una contraseña tiene 8 letras, 3 números y 1 símbolo. ¿Cuántos caracteres tiene?", "8+3+1", "Se suman las letras, los números y el símbolo."),
        arith("Una niña revisa 5 cuentas y cambia la contraseña de 3. ¿Cuántas quedan sin cambiar?", "5-3", "Se restan las cambiadas al total."),
    ],
    context=[ex("Sam crea una cuenta en un juego en línea con ayuda de una persona de su casa. Eligen perfil privado, nombre «roble_veloz» y una contraseña larga. ¿Aplicaron prácticas seguras?", "Sí", "Perfil privado, nombre sin datos y contraseña segura.")],
    selfcheck=[ex("En Orientación: ¿conviene un perfil privado?", "Sí", "Controla quién te ve."), ex("¿Se comparte la contraseña con amigos?", "No", "Debe mantenerse en secreto."), ex("¿Se debe pensar antes de publicar?", "Sí", "Lo publicado puede quedar mucho tiempo.")],
    task=T("Escribe una lista de 5 reglas para usar redes de forma segura. Debe incluir una sobre contraseñas, una sobre el perfil, una sobre lo que publicas, una sobre desconocidos y una sobre adultos de confianza. Después crea un ejemplo de contraseña segura inventada que no uses en la vida real.", "1) No comparto mi contraseña. 2) Mi perfil es privado. 3) No publico mi dirección. 4) No acepto a desconocidos. 5) Si algo me incomoda, aviso a un adulto. Ejemplo: Rio_Verde_92_Luna.", ["cinco reglas", "cubre los cinco temas", "ejemplo de contraseña que no uses"], ["lista escrita"], ["incluir su contraseña real", "reglas vagas"], "Reconoce las reglas y pregunta cuál sería la más difícil de cumplir."),
    reinforce="Escribe dos nombres de usuario seguros que no revelen quién eres.",
    extend="Explica por qué cada cuenta debe tener una contraseña distinta.",
)

lesson(
    OA4, 5,
    "Una hoja y un lápiz. Los ejemplos de fuentes y frases están escritos en los ejercicios.",
    "Aprenderé a comunicarme bien con mi familia o un adulto de confianza y a elegir fuentes confiables sobre sexualidad (personas, libros, páginas especializadas). Sirve para pedir ayuda a tiempo.",
    ["Sé qué hacer ante un mensaje incómodo.", "Sé reconocer fuentes confiables."],
    [
        "Comunicar bien es decir lo que pasa de forma clara y calmada. Para hablar con tu familia o con un adulto de confianza, puedes elegir un momento tranquilo, decir «necesito contarte algo importante» y explicar los hechos: qué pasó, cuándo y qué sientes. No necesitas tener todas las respuestas, solo empezar. Si el adulto no te escucha o no puede ayudarte, busca a otro adulto de confianza hasta que te escuchen.",
        "Para informarte sobre sexualidad hay tres tipos de fuentes confiables. Las personas significativas, como alguien de tu casa o de tu familia, tu profesor, el orientador o una profesional de la salud. Los libros, como los de la biblioteca del colegio, escritos para tu edad. Y las páginas de internet especializadas, como las de un ministerio de salud o de un hospital, que tienen autores o instituciones identificables.",
        "Antes de creer algo, revisa quién lo escribe, para qué y si pide datos personales. Si una fuente te hace sentir incómodo, te pide secreto o te presiona, sal de ahí y cuéntalo a un adulto de confianza. Esto es parte de cuidar tu cuerpo, tu intimidad y tu seguridad.",
    ],
    [("comunicación efectiva", "decir lo que pasa de forma clara y calmada"), ("persona significativa", "persona importante en mi vida, como un familiar o profesor"), ("página especializada", "sitio de una institución que sabe del tema"), ("hecho", "lo que ocurrió"), ("fuente confiable", "lugar de información correcta y con autor identificable")],
    [
        W("Armar una frase", "Alex quiere contar que recibió un mensaje incómodo. ¿Qué frase ayuda a empezar: «Necesito contarte algo importante» o «No quiero decir nada»?", ["La primera avisa que es un tema importante.", "Abre el espacio para hablar.", "La segunda cierra la conversación."], "«Necesito contarte algo importante»"),
        W("Elegir una fuente", "Para entender la pubertad, ¿qué fuente conviene: la web de un ministerio de salud o un comentario anónimo en una red?", ["El ministerio es una institución identificable.", "Un comentario anónimo no dice quién escribe.", "Una fuente confiable es verificable."], "La web de un ministerio de salud"),
    ],
    [
        M("No hablar con nadie porque me da vergüenza.", "Se cree que el problema es solo mío.", "Pide un momento tranquilo y empieza por los hechos."),
        M("Confiar en cualquier página que aparezca primero en una búsqueda.", "Se piensa que lo que aparece primero es lo mejor.", "Revisa quién escribe y si pide datos personales."),
    ],
    R=[
        ex("Para contar algo importante, ¿conviene un momento tranquilo o gritar en el pasillo?", "Un momento tranquilo", "Permite hablar con calma."),
        ex("Un libro de la biblioteca del colegio, ¿es una fuente confiable?", "Sí", "Está pensado para tu edad y tiene autor."),
        ex("Si un adulto no te escucha, ¿buscas a otro adulto de confianza o te quedas callado?", "Busco a otro adulto de confianza", "Hay que seguir pidiendo ayuda hasta que te escuchen."),
    ],
    U=[
        ex("¿Qué partes tiene una buena forma de contar un problema?", "Qué pasó, cuándo y qué siento", "Con esos datos el adulto entiende."),
        ex("¿Por qué una fuente sin autor no es confiable?", "No se sabe quién escribe ni si es correcto", "No se puede verificar."),
        ex("¿Una página que pide tus datos para informarte es segura?", "No", "Una fuente confiable no los pide."),
    ],
    A=[
        ex("Fuentes: 1) tu profesora, 2) un chat anónimo, 3) libro de la biblioteca, 4) hospital con página oficial. ¿Cuántas son confiables?", "3", "La profesora, el libro y el hospital son identificables; el chat anónimo no."),
        ex("Alex dice: «Ayer recibí un mensaje. Me dio miedo». ¿Qué parte es el hecho?", "Ayer recibí un mensaje", "Cuenta lo ocurrido; «me dio miedo» es la emoción."),
        ex("Para empezar a conversar, Alex escribe «Necesito contarte algo importante; ¿tienes un momento?». ¿A qué tipo de persona se lo dice: persona significativa o desconocido?", "Persona significativa", "Es alguien de confianza, como un familiar o profesor."),
    ],
    Z=[
        ex("¿Por qué conviene tener más de un adulto de confianza?", "Porque si uno no puede ayudar, hay otro", "Así siempre hay a quién acudir."),
        ex("Un sitio dice: «Todos mienten, solo nosotros te decimos la verdad». ¿Qué alerta muestra?", "Pide que no confíes en otros", "Una fuente confiable no te aísla."),
    ],
    D=[
        arith("Una lista tiene 12 fuentes. 5 son confiables. ¿Cuántas no lo son?", "12-5", "Se restan las confiables al total."),
        arith("Noa tiene 2 adultos de confianza en casa, 2 en el colegio y 1 en su comunidad. ¿Cuántos tiene?", "2+2+1", "Se suman los tres grupos."),
    ],
    context=[ex("Luz tiene una duda sobre su cuerpo. Primero revisa un libro del colegio y luego se lo cuenta a la orientadora. ¿Usó fuentes confiables?", "Sí", "Libro del colegio y una persona significativa.")],
    selfcheck=[ex("En Orientación: ¿puedes pedir ayuda a más de un adulto?", "Sí", "Hasta que alguien te escuche."), ex("¿Un libro del colegio puede ser fuente confiable?", "Sí", "Tiene autor y es para tu edad."), ex("¿Una página que pide datos personales es confiable?", "No", "No debe pedirlos.")],
    task=T("Escribe una carta corta de ayuda para un adulto de confianza (sin nombres reales): cuenta un hecho inventado de un mensaje incómodo, qué siente el personaje y qué ayuda necesita. Luego haz una lista de tres fuentes confiables para informarte sobre la pubertad.", "Hola, necesito contarte algo importante. Recibí un mensaje que me incomodó. Me siento con miedo. ¿Me ayudas? Fuentes: mi profesora, un libro de la biblioteca, la web de un hospital.", ["carta con hecho, emoción y ayuda", "tres fuentes confiables", "no incluye datos reales"], ["carta escrita", "lista escrita"], ["no pedir ayuda concreta", "incluir fuentes no confiables"], "Reconoce el pedido de ayuda y pregunta cuándo hablaría."),
    reinforce="Escribe una frase para iniciar una conversación difícil con un adulto de confianza.",
    extend="Explica cómo comprobarías si una página sobre sexualidad es confiable.",
)
