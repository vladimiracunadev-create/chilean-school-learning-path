"""Cuaderno del estudiante, 1.º básico Orientación: OA 01 (características e intereses), OA 02 (emociones) y OA 03 (afecto y cuidado)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA1, OA2, OA3 = "OR01 OA 01", "OR01 OA 02", "OR01 OA 03"

# ================================================================ OA 01
register(
    OA1, 1,
    materials="Una hoja, lápiz y las descripciones escritas en cada ejercicio; sin materiales especiales. Nadie tiene que contar nada privado.",
    use="Aprenderé a decir cómo soy sin compararme con nadie. Sirve para conocerme y para presentarme con confianza.",
    prior=["Sé quién soy y cómo me llamo.", "Sé que cada persona es distinta."],
    explain=[
        "Una característica es algo que describe cómo eres. Puede ser algo que se ve, como tener el pelo rizado o usar lentes. También puede ser algo de tu forma de ser, como ser tranquilo, simpático o curioso.",
        "Cuando describes una característica, dices un hecho sobre ti: «Soy ordenada». No dices «soy mejor que Beto» ni «soy peor que Ana». Comparar no ayuda a conocerse, porque cada persona tiene sus propias características y todas valen.",
        "Puedes elegir qué contar. Hay cosas que son tuyas y no tienes que decirlas si no quieres. Para esta clase basta una característica sencilla, como «me gusta reír» o «soy cuidadoso con mis cosas».",
    ],
    vocab=[("característica", "algo que describe cómo eres"), ("describir", "decir cómo es algo o alguien"), ("comparar", "decir quién es mejor o peor"), ("hecho", "algo que es verdad y se puede observar"), ("valorar", "reconocer que algo tiene importancia")],
    worked=[
        {"title": "Describir sin comparar", "problem": "Ana quiere hablar de sí misma. ¿Qué frase describe una característica sin comparar: «Soy más rápida que Eva» o «Soy rápida para correr»?", "steps": ["La primera frase nombra a otra persona y dice quién gana.", "La segunda solo cuenta algo que Ana hace.", "Describir es decir cómo soy, sin mirar al otro."], "answer": "«Soy rápida para correr»"},
        {"title": "Característica de forma de ser", "problem": "Tomás siempre espera su turno y ayuda a guardar los lápices. ¿Qué característica de su forma de ser puedes decir?", "steps": ["Mira lo que Tomás hace: espera y ayuda.", "Esas acciones muestran cómo es.", "Una palabra que lo describe es «colaborador»."], "answer": "Tomás es colaborador"},
    ],
    mistakes=[
        {"wrong": "Decir «soy el mejor del curso» para describirme.", "why": "Parece una característica, pero compara con los demás.", "fix": "Cuenta algo tuyo: «Me gusta aprender cosas nuevas»."},
        {"wrong": "Pensar que una característica tiene que ser perfecta.", "why": "Creemos que solo se cuentan cosas muy buenas.", "fix": "Una característica solo dice cómo eres; puede ser sencilla."},
    ],
    tiers={
        "recovery": [
            ex("Mía tiene el pelo largo y negro. ¿Qué dice la frase: cómo es Mía o quién gana?", "Cómo es Mía", "Describe a Mía sin comparar con otra persona."),
            ex("¿«Soy alegre» es una característica de cómo se ve o de la forma de ser?", "De la forma de ser", "Alegre habla de cómo eres por dentro."),
            ex("Beto dice: «Tengo una mochila azul». ¿Eso es una característica de Beto?", "No", "La mochila es algo que tiene, no cómo es él."),
        ],
        "understand": [
            ex("¿Para qué sirve decir una característica tuya?", "Para contar cómo soy y conocerme", "Describirse ayuda a que otros y yo nos conozcamos."),
            ex("¿Cuál frase compara: «Soy tranquilo» o «Soy más tranquilo que Dani»?", "«Soy más tranquilo que Dani»", "Nombra a Dani y dice quién es más."),
            ex("¿Tienes que contar todo sobre ti cuando describes una característica?", "No", "Cada persona elige qué contar."),
        ],
        "apply": [
            ex("Luis tiene los ojos cafés y le gusta ayudar. Escribe una frase que empiece con «Luis es…» sin comparar.", "Por ejemplo: «Luis es ayudador»", "La frase describe a Luis y no nombra a otros."),
            ex("Convierte «Soy más callada que Rosa» en una frase que no compare.", "Por ejemplo: «Soy callada» o «Hablo bajito»", "Se quita el nombre de Rosa y se deja la característica."),
            ex("Elige la característica que se ve: curiosa, de pelo rizado o paciente.", "De pelo rizado", "El pelo se puede observar con los ojos."),
        ],
        "reason": [
            ex("Sofía dice: «Soy fuerte, así que valgo más que Pedro». ¿Qué parte está mal?", "«Valgo más que Pedro»", "Comparar valor entre personas no es describir una característica."),
            ex("Dani dice: «Me cuesta esperar mi turno». ¿Es una característica que puede contar?", "Sí", "Es un hecho sobre él y no lo compara con nadie."),
        ],
        "challenge": [
            ex("Eva dice: «Soy simpática y tengo el pelo corto». ¿Cuántas características dijo?", "2", "Simpática es una y pelo corto es otra."),
            ex("Dos amigos dicen la misma característica: «Soy curioso». ¿Son iguales en todo?", "No", "Comparten una característica, pero cada uno tiene muchas otras."),
        ],
    },
    context=[ex("En la ronda de presentación, la profesora dice: «Cuenta una característica tuya». Carla dice: «Soy cariñosa». ¿Hizo lo pedido?", "Sí", "Carla dijo una característica suya sin comparar.")],
    selfcheck=[ex("¿Una característica puede ser de la forma de ser?", "Sí", "Ser amable o tranquilo describe cómo eres."), ex("¿Decir «soy mejor que todos» es describir?", "No", "Es comparar, no describir."), ex("¿Puedes elegir qué característica contar?", "Sí", "Contar es una elección de cada persona.")],
    open_task=task("Elige una de estas frases para empezar y complétala con algo verdadero sobre ti: «Soy una persona…», «Me gusta mucho…» o «Se me nota que soy…». Dila a un adulto o dibújala. No tienes que contar nada privado.", "«Soy una persona curiosa». Dibujo una lupa y una flor.", ["dice o dibuja una característica propia", "no se compara con otras personas", "es verdadera para quien la dice"], ["frase dicha o escrita", "dibujo con una breve explicación"], ["usar «mejor que» o «peor que»", "describir un objeto en vez de una característica"], "Reconoce lo que sí dijo y pregunta: «¿Cómo se nota eso en lo que haces?»."),
    reinforce="Mira tu dibujo o tu frase y di en voz alta: «Esta característica es mía».",
    extend="Escribe dos características tuyas: una que se ve y otra de tu forma de ser.",
)

register(
    OA1, 2,
    materials="Una hoja y lápiz. Las acciones y los personajes están escritos en cada ejercicio.",
    use="Aprenderé que una habilidad es algo que puedo hacer y mejorar practicando. Sirve para animarme a seguir aprendiendo.",
    prior=["Sé que tengo características.", "Sé hacer algunas cosas, como dibujar o saltar."],
    explain=[
        "Una habilidad es algo que sabes hacer. Puedes saber atarte los cordones, cantar, armar un rompecabezas o consolar a un amigo. Hay habilidades del cuerpo, de la mente y de convivir con otros.",
        "Las habilidades se desarrollan con práctica. Nadie nace sabiendo andar en bicicleta. Primero cuesta, después sale un poco mejor y al final sale bien. Practicar un poco cada día ayuda más que practicar una vez muy largo.",
        "Aún no poder hacer algo no es un problema. Puedes decir «todavía no lo logro» y elegir una acción pequeña para practicar. Esa acción es una meta posible: concreta y de tu tamaño.",
    ],
    vocab=[("habilidad", "algo que sé hacer"), ("practicar", "repetir algo para hacerlo mejor"), ("todavía", "palabra que dice que puedo aprender más"), ("meta", "lo que quiero lograr"), ("avanzar", "ir mejorando poco a poco")],
    worked=[
        {"title": "Reconocer una habilidad", "problem": "Luis sabe contar cuentos a su hermano para que se duerma. ¿Qué habilidad tiene Luis?", "steps": ["Mira lo que Luis hace: cuenta cuentos.", "Lo hace con otra persona, con voz tranquila.", "Eso es una habilidad de comunicar."], "answer": "Sabe contar cuentos y calmar a otros"},
        {"title": "Elegir una acción para practicar", "problem": "Eva todavía no se abrocha bien los botones del delantal. ¿Qué puede practicar cada día?", "steps": ["La meta es abrochar botones.", "Una acción pequeña es abrochar un botón grande lento.", "Practicar cada día ayuda a mejorar."], "answer": "Abrochar un botón cada día"},
    ],
    mistakes=[
        {"wrong": "Decir «no sé hacer nada».", "why": "Nos fijamos solo en lo que cuesta.", "fix": "Piensa en lo que sí haces, aunque parezca pequeño."},
        {"wrong": "Pensar que quien practica poco es «tonto».", "why": "Creemos que las habilidades se tienen o no se tienen.", "fix": "Di «todavía» y elige una acción pequeña de práctica."},
    ],
    tiers={
        "recovery": [
            ex("Mía sabe saltar la cuerda. ¿Saltar la cuerda es una habilidad?", "Sí", "Es algo que Mía sabe hacer."),
            ex("¿Qué se hace para mejorar una habilidad: practicar o esperar sin hacer nada?", "Practicar", "Repetir ayuda a hacerlo mejor."),
            ex("Beto dice «todavía no sé nadar». ¿Puede aprender?", "Sí", "Con práctica y ayuda se puede aprender."),
        ],
        "understand": [
            ex("¿Qué quiere decir la palabra «todavía» en «todavía no lo logro»?", "Que puedo aprender más adelante", "Marca que el aprendizaje sigue."),
            ex("¿Cuál es mejor: practicar 5 minutos cada día o una vez muy largo y nunca más?", "5 minutos cada día", "Practicar seguido ayuda a recordar."),
            ex("¿Consolar a un amigo triste es una habilidad?", "Sí", "Es algo que se hace y se puede mejorar."),
        ],
        "apply": [
            ex("Ana quiere atarse los cordones. Escribe una acción pequeña que pueda practicar.", "Por ejemplo: hacer el primer nudo cada mañana", "Es concreta y se puede hacer cada día."),
            ex("Elige la habilidad que se practica con el cuerpo: dibujar, reír o contar cuentos.", "Dibujar", "Dibujar usa las manos y se mejora con práctica."),
            ex("Dani corre rápido pero se enoja si pierde. ¿Qué habilidad puede practicar: correr o perder sin enojarse?", "Perder sin enojarse", "Es la que a él le cuesta."),
        ],
        "reason": [
            ex("Carla se cae en bicicleta y dice «nunca aprenderé». ¿Qué frase la ayudaría más?", "«Todavía no lo logro; mañana practico otra vez»", "Mantiene la posibilidad de mejorar."),
            ex("Rosa practicó leer cinco días. Pedro no practicó. ¿Quién tiene más probabilidad de mejorar?", "Rosa", "Practicar seguido hace avanzar."),
        ],
        "challenge": [
            ex("Pedro dice: «Mi habilidad es ayudar a guardar los juguetes». ¿Con qué otra habilidad se parece: ordenar o cantar?", "Ordenar", "Guardar y ordenar son acciones parecidas."),
            ex("Una meta es «ser buena en todo». Otra es «hacer un dibujo al día». ¿Cuál es más posible?", "«Hacer un dibujo al día»", "Es pequeña y se puede cumplir."),
        ],
    },
    context=[ex("Mía quiere aprender a lanzar y atrapar una pelota. Hoy la pelota se le cayó dos veces. ¿Qué puede decir para seguir?", "«Todavía no la atrapo bien; lo intento otra vez»", "Reconoce el esfuerzo y propone seguir practicando.")],
    selfcheck=[ex("¿Una habilidad es algo que sé hacer?", "Sí", "Habilidad significa saber hacer algo."), ex("¿Se puede mejorar una habilidad?", "Sí", "La práctica ayuda a mejorar."), ex("¿Qué palabra ayuda cuando algo me cuesta?", "Todavía", "Recuerda que puedo seguir aprendiendo.")],
    open_task=task("Mira esta lista y marca con un círculo una habilidad que ya tienes y con un cuadrado una que quieres practicar: cantar, dibujar, saltar la cuerda, contar un cuento, ordenar mis útiles, compartir. Después escribe o dibuja una acción pequeña para practicar la del cuadrado.", "Círculo en dibujar. Cuadrado en ordenar mis útiles. Acción: guardar el lápiz en el estuche cada tarde.", ["marca una habilidad que ya tiene", "marca una que quiere practicar", "propone una acción pequeña y posible"], ["lista marcada", "dibujo de la acción"], ["elegir una meta enorme", "decir que no tiene ninguna habilidad"], "Valida la habilidad que ya tiene y ayuda a hacer la acción más pequeña y concreta."),
    reinforce="Escribe una habilidad tuya y una acción que harías mañana para practicarla.",
    extend="Cuenta cómo aprendiste algo que antes no sabías: qué hiciste primero y qué hiciste después.",
)

register(
    OA1, 3,
    materials="Una hoja, lápices de colores y los personajes y listas escritos en cada ejercicio.",
    use="Aprenderé qué son los intereses y cómo me ayudan a elegir qué quiero conocer. Sirve para descubrir cosas nuevas que me gustan.",
    prior=["Sé que tengo características y habilidades.", "Sé decir lo que me gusta."],
    explain=[
        "Un interés es algo que te llama la atención y te dan ganas de conocer más. Puede ser un animal, un deporte, un instrumento, las estrellas o cocinar con ayuda de un adulto. Los intereses pueden ser muchos y pueden cambiar.",
        "Los intereses te ayudan a elegir. Si te interesan los insectos, quizás pidas un libro de insectos o observes una hormiga en el patio, siempre con cuidado y sin dañarla. Elegir con calma permite probar sin miedo a equivocarse.",
        "También puedes tener ganas de conocer algo que nunca has probado. Puedes decir «quiero conocer cómo vuelan los pájaros». Una pregunta así es un buen comienzo para aprender, y puedes hacerla a un adulto de confianza.",
    ],
    vocab=[("interés", "algo que me llama la atención y quiero conocer"), ("elegir", "tomar una opción entre varias"), ("probar", "intentar algo nuevo"), ("curioso", "que quiere saber más"), ("cambiar", "hacerse distinto con el tiempo")],
    worked=[
        {"title": "Reconocer un interés", "problem": "A Dani le encanta mirar los barcos y siempre pregunta cómo flotan. ¿Cuál es su interés?", "steps": ["Dani mira barcos.", "Pregunta cómo flotan.", "Quiere conocer más de eso."], "answer": "Los barcos y cómo flotan"},
        {"title": "Un interés ayuda a elegir", "problem": "A Mía le interesan las plantas. En el recreo puede ir a regar la maceta del curso o jugar a las escondidas. ¿Qué puede elegir para conocer más de plantas?", "steps": ["Mía quiere conocer más de plantas.", "Regar la maceta se relaciona con plantas.", "Escondidas es otra actividad."], "answer": "Regar la maceta del curso"},
    ],
    mistakes=[
        {"wrong": "Decir «no me interesa nada».", "why": "Aún no se ha puesto atención en lo que llama la curiosidad.", "fix": "Piensa en lo que miras más rato o preguntas seguido."},
        {"wrong": "Pensar que un interés debe ser igual al de tus amigos.", "why": "Es agradable compartir, pero cada persona tiene los suyos.", "fix": "Tu interés puede ser distinto y también vale."},
    ],
    tiers={
        "recovery": [
            ex("A Tomás le gustan los dinosaurios y pregunta por ellos todos los días. ¿Cuál es su interés?", "Los dinosaurios", "Es lo que más le llama la atención."),
            ex("¿Un interés puede cambiar con el tiempo?", "Sí", "Con los años aparecen intereses nuevos."),
            ex("Eva mira un libro de aves y pregunta cómo cantan. ¿Tiene curiosidad por las aves?", "Sí", "Quiere saber más de ellas."),
        ],
        "understand": [
            ex("¿Qué quiere decir tener un interés?", "Que algo me llama la atención y quiero conocerlo", "Un interés nace de la curiosidad."),
            ex("¿Los intereses de dos amigos deben ser iguales?", "No", "Cada persona tiene los suyos."),
            ex("¿Cuál es una pregunta de interés: «¿Por qué las abejas hacen miel?» o «¿Qué hora es?»?", "«¿Por qué las abejas hacen miel?»", "Muestra ganas de conocer un tema."),
        ],
        "apply": [
            ex("Ana quiere conocer los instrumentos musicales. Escribe una pregunta que pueda hacer a un adulto.", "Por ejemplo: «¿Cómo suena un tambor?»", "Es una pregunta sobre su interés."),
            ex("Luis quiere saber de cocina. ¿Qué actividad segura puede hacer con un adulto: revolver la masa o encender el horno solo?", "Revolver la masa con un adulto", "Con un adulto es seguro, solo no."),
            ex("Pedro dice «me interesan los planetas». Elige qué puede pedir: un libro de planetas o un juguete cualquiera.", "Un libro de planetas", "Sirve para conocer más de su interés."),
        ],
        "reason": [
            ex("Rosa tiene ganas de conocer cómo crecen las flores. ¿Qué puede hacer: sembrar una semilla con ayuda o dejar de pensar en el tema?", "Sembrar una semilla con ayuda", "Probar acerca su interés."),
            ex("Carla antes prefería los dibujos y hoy prefiere el fútbol. ¿Hizo algo malo?", "No", "Los intereses cambian y es normal."),
        ],
        "challenge": [
            ex("Beto elige entre ir al taller de pintura (le interesa) o ir donde van sus amigos (le interesa menos). ¿Qué decisión se parece más a su interés?", "Ir al taller de pintura", "La elección sigue lo que le interesa."),
            ex("Dos niñas dicen: «Me interesan los peces». ¿Puedes saber qué quiere conocer cada una?", "No", "Debes preguntarles; el interés tiene detalles distintos."),
        ],
    },
    context=[ex("En la biblioteca del curso hay libros de animales, de cuentos y de planetas. Sofía siempre se queda mirando fotos de ballenas. ¿Qué libro conviene ofrecerle?", "El de animales", "Las ballenas son animales y es su interés.")],
    selfcheck=[ex("¿Un interés puede ser un tema como los insectos?", "Sí", "Un tema que quiero conocer es un interés."), ex("¿Puedo tener más de un interés?", "Sí", "Una persona puede tener varios."), ex("¿Con quién puedo conversar para conocer más de mi interés?", "Con un adulto de confianza", "Un adulto puede dar libros o ideas seguras.")],
    open_task=task("Elige una de estas cosas que podrías querer conocer: el mar, los insectos, los instrumentos musicales o las estrellas. Escribe o dibuja una pregunta que te gustaría hacer sobre esa cosa y quién podría ayudarte a responderla.", "Quiero conocer el mar. Pregunta: «¿Por qué hay olas?». Me puede ayudar mi profesora o un libro.", ["elige un tema", "formula una pregunta sobre ese tema", "nombra una persona o recurso que ayuda"], ["pregunta escrita", "dibujo del tema elegido"], ["preguntar algo que no se relaciona con el tema", "no nombrar a quién pedir ayuda"], "Felicita la curiosidad y propone una forma segura de encontrar la respuesta."),
    reinforce="Cuéntale a alguien de confianza algo que te gustaría conocer.",
    extend="Escribe tres preguntas que te gustaría hacer sobre un mismo tema que te interesa.",
)

register(
    OA1, 4,
    materials="Una hoja, lápices y las descripciones de personajes escritas en cada ejercicio.",
    use="Aprenderé a hacer un retrato personal que muestre cómo soy, qué sé hacer y qué me interesa, y que puede cambiar. Sirve para valorarme.",
    prior=["Sé qué son características, habilidades e intereses."],
    explain=[
        "Un retrato personal junta tres cosas: cómo soy (características), qué sé hacer (habilidades) y qué quiero conocer (intereses). Puedes hacerlo con un dibujo, con palabras o con ambas cosas.",
        "Un retrato es flexible. Eso significa que puede cambiar cuando creces o cuando aprendes algo nuevo. Hoy puedes escribir «todavía no sé nadar» y dentro de un año podrás decir «ya nado un poco».",
        "Valorar tus rasgos es reconocer que importan, sin creerte mejor ni peor que otros. También puedes valorar algo que te cuesta, porque te da una oportunidad de aprender. Cuando muestras tu retrato, tú decides qué compartir.",
    ],
    vocab=[("retrato", "una imagen o descripción de una persona"), ("rasgo", "algo propio de una persona"), ("flexible", "que puede cambiar"), ("valorar", "reconocer que algo importa"), ("compartir", "mostrar o contar a otros")],
    worked=[
        {"title": "Armar un retrato", "problem": "Mía es alegre, sabe dibujar y le interesan las ballenas. Arma su retrato con tres frases.", "steps": ["Característica: «Soy alegre».", "Habilidad: «Sé dibujar».", "Interés: «Quiero conocer las ballenas»."], "answer": "Soy alegre. Sé dibujar. Quiero conocer las ballenas."},
        {"title": "Un retrato que cambia", "problem": "En marzo Tomás escribió: «Todavía no sé atarme los cordones». En octubre ya los ata. ¿Qué cambió en su retrato?", "steps": ["En marzo no lo sabía hacer.", "Practicó.", "En octubre ya sabe, es una nueva habilidad."], "answer": "Ahora tiene la habilidad de atarse los cordones"},
    ],
    mistakes=[
        {"wrong": "Pensar que el retrato queda fijo para siempre.", "why": "Creemos que lo que escribimos hoy no cambia.", "fix": "Puedes agregar o cambiar frases cuando aprendas más."},
        {"wrong": "Mostrar a otros todo el retrato aunque no quiera.", "why": "Se cree que hay que contar todo.", "fix": "Tú decides qué compartir y qué guardar."},
    ],
    tiers={
        "recovery": [
            ex("«Soy cariñosa» en un retrato, ¿es característica, habilidad o interés?", "Característica", "Cuenta cómo es la persona."),
            ex("«Sé armar rompecabezas», ¿es característica, habilidad o interés?", "Habilidad", "Es algo que sabe hacer."),
            ex("«Quiero conocer los volcanes», ¿es característica, habilidad o interés?", "Interés", "Dice qué quiere conocer."),
        ],
        "understand": [
            ex("¿Qué tres cosas junta un retrato personal?", "Características, habilidades e intereses", "Dice cómo soy, qué sé hacer y qué quiero conocer."),
            ex("¿Por qué se dice que el retrato es flexible?", "Porque puede cambiar", "Las personas crecen y aprenden."),
            ex("¿Quién decide qué parte del retrato se muestra a otros?", "Yo", "Cada persona elige qué compartir."),
        ],
        "apply": [
            ex("Ordena en el retrato de Ana: «Sé cantar», «Soy paciente», «Quiero conocer los delfines». ¿Cuál es la característica?", "«Soy paciente»", "Paciente dice cómo es Ana."),
            ex("Beto escribió: «Soy tranquilo. Sé hacer torres con bloques. Quiero conocer los puentes». Escribe su interés.", "Conocer los puentes", "Es lo que Beto quiere conocer."),
            ex("Completa: «Todavía no sé silbar, pero quiero ___». Elige: practicar o rendirme.", "Practicar", "Mantiene abierta la posibilidad de cambio."),
        ],
        "reason": [
            ex("Dani guardó su retrato de marzo y en diciembre agregó dos habilidades nuevas. ¿Qué muestra eso?", "Que aprendió y cambió", "El retrato se actualiza con el tiempo."),
            ex("Eva dice: «Mi retrato es feo porque soy distinta de mis amigas». ¿Qué le dirías?", "Que ser distinta no es feo; cada retrato es propio", "Las diferencias no son defectos."),
        ],
        "challenge": [
            ex("Luis dibuja su retrato con un martillo, un libro y un balón. Si dice que el balón es lo que sabe hacer, ¿qué sección del retrato es el balón?", "Habilidad", "Jugar con el balón es algo que sabe hacer."),
            ex("Pedro y Rosa hacen retratos y los dos escriben «Soy alegre». ¿Sus retratos son iguales?", "No", "Los demás rasgos pueden ser distintos."),
        ],
    },
    context=[ex("Sofía muestra su retrato al curso y dice solo dos de sus tres frases porque la tercera es algo que prefiere guardar. ¿Hizo bien?", "Sí", "Ella decide qué compartir.")],
    selfcheck=[ex("¿Un retrato puede tener un dibujo?", "Sí", "Se puede hacer con dibujo y palabras."), ex("¿Puede cambiar mi retrato en un año?", "Sí", "Las personas aprenden y cambian."), ex("¿Mi retrato dice que soy mejor que otros?", "No", "Solo muestra cómo soy, sin comparar.")],
    open_task=task("Haz tu retrato en una hoja dividida en tres partes: «Soy…», «Sé…» y «Quiero conocer…». En cada parte escribe o dibuja una cosa. Abajo agrega una frase que empiece con «Dentro de un año quizás…». Puedes guardarlo o mostrarlo, como prefieras.", "Soy curioso. Sé dibujar. Quiero conocer los volcanes. Dentro de un año quizás sepa nadar.", ["completa las tres partes", "incluye una posibilidad de cambio", "no compara con otros"], ["hoja con tres partes", "dibujo y frases"], ["dejar partes vacías sin intentarlo", "escribir cosas de otras personas"], "Reconoce cada parte completada y sugiere agregar un dibujo si le cuesta escribir."),
    reinforce="Cuéntale a alguien de confianza qué parte de tu retrato te gusta más.",
    extend="Dibuja cómo imaginas tu retrato dentro de un año y escribe una frase sobre lo que habrá cambiado.",
)

# ================================================================ OA 02
register(
    OA2, 1,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio; no necesitas contar nada personal.",
    use="Aprenderé a ponerle nombre a lo que siento y a distinguir lo que siento de lo que hago. Sirve para entenderme y pedir ayuda.",
    prior=["Sé que a veces me siento contento o triste.", "Sé decir lo que me pasa con palabras sencillas."],
    explain=[
        "Una emoción es lo que sientes por dentro: alegría, tristeza, rabia, miedo, sorpresa o calma. Tiene señales en el cuerpo. Con miedo puede latirte el corazón más rápido, con rabia puede apretarse la mandíbula y con tristeza puedes sentir ganas de llorar.",
        "Lo que haces con esa emoción es la conducta. Sentir rabia es una emoción. Gritar o empujar es una conducta. Todas las emociones son normales, pero no todas las conductas son seguras ni respetuosas.",
        "Ponerle nombre a la emoción ayuda a calmarte y a contar qué te pasa. Puedes decir «siento rabia» o «tengo miedo». Así otra persona te entiende y puede ayudarte.",
    ],
    vocab=[("emoción", "lo que siento por dentro"), ("conducta", "lo que hago"), ("señal del cuerpo", "algo que noto en el cuerpo cuando siento una emoción"), ("rabia", "emoción que aparece cuando algo me molesta mucho"), ("miedo", "emoción que aparece cuando creo que algo me puede dañar")],
    worked=[
        {"title": "Emoción o conducta", "problem": "Beto se enoja y tira el lápiz al suelo. ¿Qué es la emoción y qué es la conducta?", "steps": ["Beto siente algo por dentro: rabia.", "Tira el lápiz: eso es lo que hace.", "Lo que siente es la emoción; lo que hace es la conducta."], "answer": "Emoción: rabia. Conducta: tirar el lápiz"},
        {"title": "Leer una señal del cuerpo", "problem": "A Mía le late fuerte el corazón antes de pasar adelante a hablar. ¿Qué emoción puede sentir?", "steps": ["El corazón rápido es una señal del cuerpo.", "Puede pasar con nervios o miedo.", "Mía puede decir «siento nervios»."], "answer": "Nervios o miedo"},
    ],
    mistakes=[
        {"wrong": "Decir «estoy gritando» cuando quieres decir «estoy enojado».", "why": "Confundimos lo que hacemos con lo que sentimos.", "fix": "Primero nombra lo que sientes; después piensa qué hacer."},
        {"wrong": "Creer que sentir rabia o miedo es malo.", "why": "Nos han dicho que algunas emociones no se sienten.", "fix": "Todas las emociones se pueden sentir; elegimos qué hacer con ellas."},
    ],
    tiers={
        "recovery": [
            ex("Si sonríes porque tu amigo te regaló un dibujo, ¿qué emoción sientes?", "Alegría", "Sonreír por un regalo muestra alegría."),
            ex("«Siento tristeza» ¿dice lo que siento o lo que hago?", "Lo que siento", "Tristeza es una emoción."),
            ex("«Tiré la silla» ¿es emoción o conducta?", "Conducta", "Tirar es una acción."),
        ],
        "understand": [
            ex("¿Qué diferencia hay entre emoción y conducta?", "La emoción se siente y la conducta se hace", "Una está por dentro y la otra se ve."),
            ex("¿Cuál es una señal del cuerpo del miedo: corazón rápido o bostezar?", "Corazón rápido", "El miedo acelera el corazón."),
            ex("¿Es malo sentir rabia?", "No", "Todas las emociones son normales; lo importante es qué hago."),
        ],
        "apply": [
            ex("Dani escucha un trueno fuerte y se esconde bajo la mesa. Nombra la emoción.", "Miedo", "Se esconde para protegerse."),
            ex("Ana perdió su peluche y llora. ¿Qué emoción puede sentir?", "Tristeza", "Llorar por una pérdida muestra tristeza."),
            ex("Luis vio un regalo sorpresa y abrió bien los ojos. Nombra la emoción.", "Sorpresa", "Abrir los ojos grandes muestra sorpresa."),
        ],
        "reason": [
            ex("Eva dice: «Siento rabia y por eso voy a golpear». ¿Qué parte es la emoción y qué parte la conducta?", "Rabia es la emoción y golpear la conducta", "Una se siente y la otra se hace."),
            ex("Carla sintió rabia y fue a respirar al rincón de calma. ¿Cambió la emoción o la conducta?", "La conducta", "Eligió una acción tranquila."),
        ],
        "challenge": [
            ex("Pedro tiene las manos sudadas, mira al piso y no habla. ¿Qué emoción puede sentir: vergüenza o alegría?", "Vergüenza", "Las señales muestran que se esconde."),
            ex("Dos niños sienten rabia. Uno respira y el otro empuja. ¿Sienten lo mismo?", "Sí, pero hacen cosas distintas", "La emoción es igual y la conducta es distinta."),
        ],
    },
    context=[ex("Rosa estaba armando una torre de bloques y se cayó. Aprieta los puños y dice: «¡Me da rabia!». ¿Qué hizo bien al hablar?", "Nombró su emoción", "Dijo lo que sentía sin dañar.")],
    selfcheck=[ex("¿Las emociones se sienten por dentro?", "Sí", "Una emoción es algo que sentimos."), ex("¿Empujar es una emoción?", "No", "Es una conducta."), ex("¿Poner nombre a una emoción ayuda?", "Sí", "Ayuda a calmarse y a pedir ayuda.")],
    open_task=task("Mira estas cuatro caras: alegre, triste, enojada, asustada. Dibújalas en tu hoja. Debajo de cada cara escribe o dibuja una señal del cuerpo que podría tener esa emoción (por ejemplo: sonrisa, lágrimas, ceño, manos frías).", "Cara alegre: sonrisa. Cara triste: lágrimas. Cara enojada: ceño fruncido. Cara asustada: manos frías.", ["dibuja las cuatro caras", "asocia una señal del cuerpo a cada una", "separa lo que siente de lo que hace"], ["hoja con cuatro caras", "señales anotadas"], ["usar solo una emoción para todas", "mezclar emociones con acciones"], "Reconoce las caras bien hechas y pregunta: «¿Qué haces tú cuando sientes esa emoción?»."),
    reinforce="Mira una cara de tu libro favorito y di qué emoción parece sentir y por qué.",
    extend="Escribe dos emociones y, para cada una, una conducta segura que podrías elegir.",
)

register(
    OA2, 2,
    materials="Una hoja, lápiz y las viñetas escritas en cada ejercicio.",
    use="Aprenderé que una misma situación puede producir emociones distintas y que no debo adivinar lo que otro siente. Sirve para entender mejor a los demás.",
    prior=["Sé nombrar emociones.", "Sé que cada persona siente a su manera."],
    explain=[
        "Una misma situación puede hacer sentir cosas distintas a personas distintas. Si se acaba el recreo, a uno le da pena y a otro le da alegría porque quiere volver a la sala. Las dos emociones pueden ser verdaderas.",
        "No siempre se nota lo que otro siente. Un niño puede estar callado porque está tranquilo, cansado o triste. Por eso no conviene adivinar. Es mejor decir «te veo callado» y preguntar «¿cómo te sientes?» con voz amable.",
        "Cuando alguien te cuenta cómo se siente, puedes creerle. Puedes decir: «Gracias por contarme». Si no quiere hablar, puedes respetarlo y decirle que estarás cerca si te necesita.",
    ],
    vocab=[("situación", "lo que pasa en un momento"), ("adivinar", "decir sin saber lo que otro siente"), ("preguntar", "pedir que alguien cuente lo que le pasa"), ("posible", "que puede ser"), ("respetar", "aceptar lo que el otro decide")],
    worked=[
        {"title": "Emociones posibles", "problem": "A Ana y a Beto les avisan que habrá paseo a la plaza. Ana salta de alegría y Beto se queda mirando el suelo. ¿Sienten lo mismo?", "steps": ["Ana muestra alegría.", "Beto puede sentir miedo, pena u otra cosa.", "No sabemos qué siente Beto; hay que preguntar."], "answer": "No necesariamente; hay que preguntar a Beto"},
        {"title": "Preguntar en vez de adivinar", "problem": "Luis está sentado solo y no habla. Eva piensa: «Debe estar enojado». ¿Qué puede hacer mejor?", "steps": ["Eva no sabe lo que siente Luis.", "Puede acercarse con calma.", "Puede preguntar: «¿Cómo te sientes?»."], "answer": "Preguntarle cómo se siente"},
    ],
    mistakes=[
        {"wrong": "Decir «sé que estás triste» sin preguntar.", "why": "A veces creemos conocer a la otra persona.", "fix": "Pregunta: «¿Cómo te sientes?»."},
        {"wrong": "Pensar que si yo me río, el otro también se ríe de lo mismo.", "why": "Creemos que todos sienten igual.", "fix": "Recuerda que cada persona puede sentir distinto en la misma situación."},
    ],
    tiers={
        "recovery": [
            ex("Si dos niños ven llover, uno se pone contento y otro triste. ¿Es posible?", "Sí", "Cada persona puede sentir distinto."),
            ex("¿Qué haces si no sabes lo que siente un amigo: adivinar o preguntar?", "Preguntar", "Preguntar evita errores."),
            ex("Mía está callada. ¿Eso prueba que está enojada?", "No", "Callada puede ser muchas cosas."),
        ],
        "understand": [
            ex("¿Por qué no conviene adivinar lo que siente otro?", "Porque puedo equivocarme", "Solo él sabe lo que siente."),
            ex("¿Qué puedes decir a alguien que te cuenta cómo se siente: «Gracias por contarme» o «Eso no es verdad»?", "«Gracias por contarme»", "Muestra respeto hacia quien habla."),
            ex("Si un amigo no quiere hablar, ¿qué puedes hacer?", "Respetar y decirle que estaré cerca", "No obligar y ofrecer apoyo."),
        ],
        "apply": [
            ex("Tomás perdió en un juego. Escribe dos emociones posibles que puede sentir.", "Por ejemplo: tristeza y rabia", "Perder puede causar varias emociones."),
            ex("Carla ve que Dani está solo en el patio. Escribe una pregunta amable para él.", "Por ejemplo: «¿Cómo te sientes hoy?»", "Es una pregunta sin adivinar."),
            ex("Pedro recibió una nota de su profesora. Una emoción posible es alegría. Escribe otra distinta.", "Por ejemplo: nervios", "Una misma situación puede tener varias emociones."),
        ],
        "reason": [
            ex("Sofía dice: «Rosa está feliz porque se ríe». Rosa dice: «Me río porque estoy nerviosa». ¿Quién sabe mejor lo que siente Rosa?", "Rosa", "Solo ella sabe lo que siente."),
            ex("Dos niños ven a un perro grande. Uno lo acaricia y el otro se aleja. ¿Alguno siente mal?", "No, sienten distinto", "Cada uno siente lo que siente."),
        ],
        "challenge": [
            ex("Si dices «Seguro estás enojado» y el otro dice «No, estoy cansado», ¿qué aprendiste?", "Que adiviné mal", "Conviene preguntar primero."),
            ex("Nombra una situación del patio donde dos niños sientan emociones distintas.", "Por ejemplo: ganar un juego; uno se alegra y otro se frustra", "Una situación puede dar varias emociones."),
        ],
    },
    context=[ex("Al entrar a la sala, Eva ve a Pedro con la cabeza baja. Ella le dice: «¿Quieres contarme cómo estás? Si no, está bien». ¿Eva adivinó o preguntó?", "Preguntó", "Le dio opción de contar sin adivinar.")],
    selfcheck=[ex("¿Una situación puede dar emociones distintas a dos personas?", "Sí", "Cada persona siente a su manera."), ex("¿Es mejor preguntar o adivinar?", "Preguntar", "Así se evita equivocarse."), ex("¿Puedo respetar que alguien no quiera hablar?", "Sí", "Respetar es aceptar su decisión.")],
    open_task=task("Lee la situación: «En el cumpleaños de Ana hay una piñata que hace mucho ruido al romperse». Escribe o dibuja dos niños que sientan emociones distintas por lo mismo y una pregunta amable que alguien podría hacerles.", "Beto siente alegría. Mía siente susto. Pregunta: «¿Cómo te sentiste con el ruido?».", ["dos emociones distintas para la misma situación", "una pregunta amable", "no adivina lo que siente cada uno"], ["dibujo con dos personajes", "pregunta escrita"], ["poner la misma emoción en ambos", "afirmar que sabe lo que siente alguien"], "Destaca las preguntas amables y recuerda que otras emociones también serían posibles."),
    reinforce="Pregunta a un adulto cómo se siente hoy y escucha su respuesta sin decir si está bien o mal.",
    extend="Escribe una situación del recreo y tres emociones distintas que podrían sentir tres niños.",
)

register(
    OA2, 3,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio; ningún objeto peligroso.",
    use="Aprenderé a elegir palabras y acciones que expresan lo que siento sin dañar. Sirve para llevarme bien con los demás y cuidarme.",
    prior=["Sé nombrar emociones.", "Sé que las conductas pueden dañar."],
    explain=[
        "Puedes expresar lo que sientes de muchas formas. Puedes decirlo con palabras: «Me enojé porque no me dejaron jugar». Puedes dibujarlo, respirar hondo, alejarte un momento o pedir ayuda a un adulto.",
        "Hay formas que no dañan y formas que sí dañan. Gritar insultos, pegar, romper cosas o burlarte hace daño a otros o a ti. Una forma segura cuida a todos, incluso cuando estás muy enojado.",
        "Una frase útil tiene tres partes: lo que siento, por qué y qué necesito. Por ejemplo: «Me siento triste porque se rompió mi dibujo; necesito un momento para calmarme». Con esa frase, el otro entiende sin sentirse atacado.",
    ],
    vocab=[("expresar", "mostrar o decir lo que siento"), ("dañar", "hacer daño a alguien o a algo"), ("respirar hondo", "tomar aire despacio y soltarlo"), ("necesito", "lo que me ayudaría"), ("insultar", "decir palabras que ofenden")],
    worked=[
        {"title": "Elegir una forma segura", "problem": "Dani siente rabia porque su amigo no lo esperó. ¿Qué forma segura de expresarlo puede elegir: gritar o decir «Me enojé porque no me esperaste»?", "steps": ["Gritar puede hacer sentir mal al otro.", "Decir lo que siente y por qué no daña.", "Es la forma segura."], "answer": "Decir «Me enojé porque no me esperaste»"},
        {"title": "Armar la frase de tres partes", "problem": "Mía está triste porque no la invitaron a un juego. Arma una frase con: siento, porque, necesito.", "steps": ["Siento: tristeza.", "Porque: no me invitaron.", "Necesito: que me inviten otra vez."], "answer": "«Me siento triste porque no me invitaron; necesito que me inviten otra vez»"},
    ],
    mistakes=[
        {"wrong": "Pensar que para mostrar enojo hay que pegar o gritar.", "why": "Es lo que se ve a veces en otros.", "fix": "Elige respirar, decir lo que sientes o pedir ayuda."},
        {"wrong": "Callar siempre lo que siento.", "why": "Creemos que molestar a otros es peor.", "fix": "Se puede contar lo que sientes con palabras respetuosas."},
    ],
    tiers={
        "recovery": [
            ex("¿Respirar hondo daña a alguien?", "No", "Es una forma segura de calmarse."),
            ex("¿Pegar daña a alguien?", "Sí", "Pegar hace daño."),
            ex("¿Decir «me enojé» es una forma segura?", "Sí", "Dice lo que siente sin dañar."),
        ],
        "understand": [
            ex("¿Cuáles son las tres partes de una frase para expresar lo que siento?", "Lo que siento, por qué y qué necesito", "Ayudan a que el otro entienda."),
            ex("¿Para qué sirve alejarse un momento cuando hay mucha rabia?", "Para calmarse antes de actuar", "Da tiempo para elegir mejor."),
            ex("¿Insultar es una forma segura de expresar rabia?", "No", "Los insultos ofenden."),
        ],
        "apply": [
            ex("Ana se enojó porque Luis rompió su dibujo sin querer. Elige la mejor frase: «Eres malo» o «Me enojé porque se rompió mi dibujo».", "«Me enojé porque se rompió mi dibujo»", "Habla de lo que siente y no ataca."),
            ex("Beto está muy asustado por una tormenta. Escribe una acción segura que pueda hacer.", "Por ejemplo: pedir un abrazo a un adulto o respirar hondo", "Cuida a Beto y no daña a nadie."),
            ex("Completa: «Me siento ___ porque ___; necesito ___». Usa: Carla está triste porque no encuentra su estuche.", "Por ejemplo: «Me siento triste porque no encuentro mi estuche; necesito ayuda para buscarlo»", "Incluye las tres partes."),
        ],
        "reason": [
            ex("Tomás tiró los lápices de Eva porque estaba enojado. ¿Qué acción más segura podía elegir?", "Respirar o decir que estaba enojado", "No habría dañado a Eva."),
            ex("Rosa se burló de una amiga para mostrar su rabia. ¿Por qué no es buena idea?", "Porque dañó los sentimientos de su amiga", "Burlarse hace daño."),
        ],
        "challenge": [
            ex("Pedro está tan enojado que no logra hablar. Elige primero: gritar, o alejarse y respirar.", "Alejarse y respirar", "Se calma antes de hablar."),
            ex("Dos niños tienen rabia. Uno dibuja y otro rompe el dibujo del compañero. ¿Quién expresó sin dañar?", "El que dibujó", "No dañó a nadie."),
        ],
    },
    context=[ex("Sofía se enoja porque un compañero no le prestó la goma. ¿Cuál de estas es una forma segura: «¿Me la prestas cuando termines?» o empujarlo?", "«¿Me la prestas cuando termines?»", "Pide con palabras y no daña.")],
    selfcheck=[ex("¿Puedo expresar enojo sin dañar?", "Sí", "Con palabras o respirando."), ex("¿Qué debo evitar cuando estoy enojado?", "Pegar o insultar", "Dañan a otros."), ex("¿Qué parte de la frase dice por qué siento algo?", "La que empieza con «porque»", "Explica la causa.")],
    open_task=task("Lee: «Tomás hizo un castillo de bloques y Beto lo tiró sin querer». Escribe o di la frase de tres partes que diría Tomás, y dibuja una acción segura que puede hacer después (por ejemplo: respirar o pedir ayuda a un adulto).", "«Me siento enojado porque se cayó mi castillo; necesito que me ayudes a armarlo de nuevo». Dibujo: Tomás respirando.", ["usa las tres partes de la frase", "elige una acción que no daña", "no insulta ni culpa"], ["frase escrita o dicha", "dibujo de la acción"], ["frase que ataca a Beto", "acción que daña"], "Reconoce lo que sí funcionó y ayuda a cambiar palabras que ataquen."),
    reinforce="Practica en voz alta la frase de tres partes con un peluche.",
    extend="Escribe dos formas de expresar el miedo sin dañar a nadie.",
)

register(
    OA2, 4,
    materials="Una hoja, lápiz y los casos de personajes escritos en cada ejercicio.",
    use="Aprenderé a pedir apoyo y a usar una estrategia para calmarme. Sirve para sentirme mejor y no quedarme solo con una emoción fuerte.",
    prior=["Sé nombrar emociones.", "Sé expresar lo que siento sin dañar."],
    explain=[
        "A veces una emoción es muy fuerte y cuesta calmarse. Para eso hay estrategias: respirar como si soplaras una vela, contar hasta diez, abrazar un peluche, tomar agua o mirar un dibujo tranquilo. Cada persona puede tener sus favoritas.",
        "Pedir apoyo también es una estrategia. Puedes decir a un adulto de confianza: «Me siento mal, ¿puedes ayudarme?». Pedir ayuda es de valientes. No significa que no puedas solo, sino que quieres cuidarte.",
        "Si la primera estrategia no funciona, pruebas otra. Puedes practicar la estrategia antes, cuando estás tranquilo, así te sale más fácil cuando la necesites. En esta clase usas casos ficticios; no tienes que contar nada tuyo.",
    ],
    vocab=[("estrategia", "una forma de hacer algo para lograrlo"), ("calmarse", "volver a estar tranquilo"), ("adulto de confianza", "persona grande que me cuida y a quien puedo contar lo que siento"), ("valiente", "que hace algo importante aunque cueste"), ("practicar", "repetir para que salga fácil")],
    worked=[
        {"title": "Elegir una estrategia", "problem": "Eva está muy nerviosa antes de una presentación. ¿Qué estrategia puede usar: respirar como soplando una vela o gritar?", "steps": ["Soplar una vela suave baja el ritmo del cuerpo.", "Gritar puede ponerla más nerviosa.", "Respirar le ayuda a calmarse."], "answer": "Respirar como soplando una vela"},
        {"title": "Pedir apoyo", "problem": "Luis perdió su cuaderno y siente que va a llorar. ¿Qué puede hacer?", "steps": ["Puede respirar.", "Si sigue mal, busca a un adulto de confianza.", "Le dice: «Me siento mal, ¿me ayudas?»."], "answer": "Pedir ayuda a un adulto de confianza"},
    ],
    mistakes=[
        {"wrong": "Quedarse callado cuando algo duele mucho.", "why": "Creemos que molestamos o que no nos creerán.", "fix": "Dilo a un adulto de confianza."},
        {"wrong": "Usar una sola estrategia y rendirse si no funciona.", "why": "Pensamos que solo hay una forma.", "fix": "Prueba otra y, si hace falta, pide ayuda."},
    ],
    tiers={
        "recovery": [
            ex("Contar hasta diez despacio, ¿ayuda a calmarse?", "Sí", "Da tiempo para bajar la emoción."),
            ex("¿Pedir ayuda es de valientes?", "Sí", "Cuidar tu bienestar es importante."),
            ex("¿Gritar fuerte es una estrategia para calmarse?", "No", "Puede aumentar la emoción."),
        ],
        "understand": [
            ex("¿Qué es una estrategia para calmarse?", "Una forma de bajar una emoción fuerte", "Ayuda a sentirse tranquilo."),
            ex("¿Para qué conviene practicar la estrategia cuando estoy tranquilo?", "Para usarla fácil cuando la necesite", "Lo practicado sale más rápido."),
            ex("¿Qué haces si una estrategia no funciona?", "Pruebo otra o pido ayuda", "Hay más de una forma."),
        ],
        "apply": [
            ex("Tomás está enojado porque perdió. Elige una estrategia: contar hasta diez, o tirar los bloques.", "Contar hasta diez", "No daña y ayuda a calmarse."),
            ex("Mía tiene miedo a la oscuridad. Escribe una frase para pedir apoyo a su mamá o papá.", "Por ejemplo: «Tengo miedo, ¿te quedas conmigo un rato?»", "Dice la emoción y pide ayuda."),
            ex("Dani está triste. Nombra una estrategia con un objeto seguro.", "Por ejemplo: abrazar un peluche", "Un objeto suave consuela."),
        ],
        "reason": [
            ex("Beto respiró y siguió muy enojado. ¿Debe rendirse o probar otra estrategia?", "Probar otra estrategia", "Una estrategia no siempre basta."),
            ex("Carla no quiere pedir ayuda porque cree que molesta. ¿Qué le dirías?", "Que pedir ayuda es válido y no molesta", "Los adultos de confianza quieren ayudar."),
        ],
        "challenge": [
            ex("Sofía prueba tres estrategias en orden: respirar, tomar agua y hablar con la profesora. ¿Cuál es pedir apoyo?", "Hablar con la profesora", "Es contar a un adulto."),
            ex("Dos niños están nerviosos. Uno respira y el otro se esconde sin decir nada. ¿Quién usó una estrategia para calmarse?", "El que respiró", "Respirar baja los nervios."),
        ],
    },
    context=[ex("Pedro se asusta con los fuegos artificiales de la plaza. Su abuela lo abraza y respiran juntos. ¿Qué estrategia usaron?", "Abrazo y respirar con apoyo", "Un adulto de confianza ayuda a calmarse.")],
    selfcheck=[ex("¿Respirar despacio ayuda a calmar?", "Sí", "Baja el ritmo del cuerpo."), ex("¿Todos usamos la misma estrategia?", "No", "Cada persona tiene sus favoritas."), ex("¿A quién puedo pedir ayuda?", "A un adulto de confianza", "Es quien me cuida.")],
    open_task=task("Imagina a Rosa: está muy enojada porque se rompió su torre. Elige dos estrategias de esta lista y dibújalas en orden: respirar soplando una vela, contar hasta diez, abrazar un peluche, tomar agua, pedir ayuda a un adulto. Escribe cuál usaría primero y cuál después.", "Primero respira soplando una vela. Después, si sigue enojada, pide ayuda a un adulto.", ["elige dos estrategias seguras", "las ordena", "incluye pedir ayuda como opción"], ["dibujo de dos pasos", "frase con primero y después"], ["elegir una estrategia que daña", "no decir qué hacer si no funciona"], "Valida la elección y sugiere ensayar la estrategia con una persona de confianza."),
    reinforce="Practica hoy, estando tranquilo, una respiración de cinco soplidos suaves.",
    extend="Haz una tarjeta con tu estrategia favorita para calmarte y cuéntale a alguien cuándo la usarías.",
)

# ================================================================ OA 03
register(
    OA3, 1,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio.",
    use="Aprenderé distintas formas de mostrar cariño y cuidado. Sirve para sentirme querido y para querer a otros de modo respetuoso.",
    prior=["Sé que hay personas que me quieren.", "Sé decir gracias."],
    explain=[
        "El afecto es el cariño que sentimos por alguien. Se puede mostrar con palabras, como «te quiero» o «gracias por ayudarme». También se muestra con acciones, como compartir tu colación, esperar a alguien o acompañar a un amigo triste.",
        "No todas las personas muestran cariño de la misma manera. Hay quien da abrazos, quien escribe notitas y quien ayuda con las tareas. Todas estas formas pueden ser cariño, y cada persona prefiere unas más que otras.",
        "Cuidar es hacer algo para que otro esté bien, por ejemplo avisar si se le cayó algo o llevarle agua si tiene sed. Cuidar a otros y a ti mismo es una forma de querer. Siempre se hace con respeto.",
    ],
    vocab=[("afecto", "cariño que siento por alguien"), ("cuidar", "hacer algo para que alguien esté bien"), ("acción", "algo que hago"), ("palabra amable", "algo que digo con buen trato"), ("respeto", "tratar bien al otro y aceptar lo que prefiere")],
    worked=[
        {"title": "Palabra o acción", "problem": "Ana le dice a su abuelo «gracias por el cuento». Luego le trae sus lentes. ¿Qué es palabra y qué es acción?", "steps": ["«Gracias por el cuento» se dice: es palabra.", "Traer los lentes se hace: es acción."], "answer": "Palabra: «gracias por el cuento». Acción: traer los lentes"},
        {"title": "Formas distintas de cuidar", "problem": "Beto cuida a su hermano pequeño tomándole la mano para cruzar. Mía cuida a su amiga prestándole un lápiz. ¿Las dos cuidan?", "steps": ["Beto protege a su hermano.", "Mía ayuda a su amiga.", "Las dos buscan que el otro esté bien."], "answer": "Sí, cuidan de formas distintas"},
    ],
    mistakes=[
        {"wrong": "Pensar que cariño es solo dar abrazos.", "why": "Es la forma que más vemos en las películas.", "fix": "El cariño también se muestra con palabras y ayuda."},
        {"wrong": "Creer que quien no abraza no quiere.", "why": "Cada persona muestra afecto distinto.", "fix": "Mira también sus acciones y palabras."},
    ],
    tiers={
        "recovery": [
            ex("«Te quiero mucho» ¿es palabra o acción?", "Palabra", "Se dice con la voz."),
            ex("Compartir la colación, ¿es palabra o acción?", "Acción", "Se hace con las manos."),
            ex("Acompañar a un amigo triste, ¿es una forma de cuidar?", "Sí", "Está con él para que se sienta mejor."),
        ],
        "understand": [
            ex("¿Qué es el afecto?", "El cariño que siento por alguien", "Es una emoción de querer."),
            ex("¿Hay una sola forma de mostrar cariño?", "No", "Hay palabras, acciones y más."),
            ex("¿Cuidar puede hacerse sin respeto?", "No", "Cuidar incluye tratar bien al otro."),
        ],
        "apply": [
            ex("Tomás quiere mostrar cariño a su amiga que está triste. Escribe una palabra amable que pueda decir.", "Por ejemplo: «Estoy aquí contigo»", "Es una palabra que acompaña."),
            ex("Luis quiere cuidar a su perro. Elige una acción: darle agua fresca o dejarlo sin comer.", "Darle agua fresca", "Cuida su necesidad básica."),
            ex("Eva ve que a Pedro se le cayeron las hojas. Escribe una acción de cuidado que pueda hacer.", "Por ejemplo: ayudarle a recogerlas", "Ayuda sin que se lo pida."),
        ],
        "reason": [
            ex("Sofía no abraza a su mamá, pero siempre le deja un dibujo sobre la cama. ¿Le muestra cariño?", "Sí", "Un dibujo regalado es una forma de afecto."),
            ex("Dani dice «te quiero» pero se burla de su amigo. ¿Sus acciones coinciden con sus palabras?", "No", "Burlarse no es cuidar."),
        ],
        "challenge": [
            ex("Rosa escribe una notita «gracias» y la deja en la mochila de su amigo. ¿Es palabra, acción o las dos?", "Las dos", "Escribe una palabra y hace algo con ella."),
            ex("Dos niños muestran cariño: uno con palabras y otro ayudando. ¿Quién lo hace bien?", "Los dos", "Las dos formas son válidas."),
        ],
    },
    context=[ex("La abuela de Carla vive lejos. Carla le dibuja una flor y se la manda con una nota que dice «Te echo de menos». ¿Qué formas de cariño usó?", "Un dibujo y una palabra escrita", "Usó acción y palabra.")],
    selfcheck=[ex("¿Una palabra amable puede mostrar afecto?", "Sí", "Las palabras también cuidan."), ex("¿Ayudar es una forma de cuidar?", "Sí", "Ayudar busca el bienestar del otro."), ex("¿Todos muestran cariño igual?", "No", "Hay muchas formas.")],
    open_task=task("Elige a una persona ficticia de esta lista: Ana (le cuesta hablar), Beto (tiene un resfrío) o Mía (perdió su juguete). Escribe o dibuja una palabra amable y una acción de cuidado que podrías ofrecerle.", "Para Beto con resfrío: palabra «Que te mejores pronto»; acción: llevarle su tarea para que no se atrase.", ["elige a un personaje", "incluye una palabra amable", "incluye una acción de cuidado respetuosa"], ["dibujo o texto con palabra y acción"], ["ofrecer algo que no se puede cumplir", "burlarse o presionar"], "Destaca la palabra y la acción y propone una forma más sencilla si fue muy complicada."),
    reinforce="Di hoy una palabra amable a alguien de tu familia.",
    extend="Escribe tres formas distintas de cuidar a un amigo que está resfriado.",
)

register(
    OA3, 2,
    materials="Una hoja, lápiz y las situaciones escritas en cada ejercicio.",
    use="Aprenderé a preguntar si a alguien le gusta una muestra de cariño y a respetar si dice que no. Sirve para que todos se sientan seguros.",
    prior=["Sé que hay formas de mostrar afecto.", "Sé decir sí y no."],
    explain=[
        "A cada persona le gustan cosas distintas. A uno le gustan los abrazos, a otro prefiere un choque de manos y a otro solo saludar con la palabra. Esas son preferencias, y todas se pueden respetar.",
        "Antes de abrazar, tomar la mano o dar un beso a alguien, pregunta: «¿Quieres un abrazo?». Eso se llama pedir consentimiento. Si la persona dice «no», esa respuesta se respeta siempre, aunque no explique por qué.",
        "Tú también puedes decir «no, gracias» cuando algo no te gusta, incluso a un familiar. Tu cuerpo es tuyo. Y si alguien te presiona y no te escucha, avisa a un adulto de confianza.",
    ],
    vocab=[("preferencia", "lo que me gusta más"), ("consentimiento", "decir que sí o que no antes de tocar o abrazar"), ("respetar un no", "aceptar la respuesta sin enojarse"), ("presionar", "insistir para que alguien diga que sí"), ("«no, gracias»", "forma amable de decir que no")],
    worked=[
        {"title": "Preguntar primero", "problem": "Luis quiere abrazar a Ana porque ella está triste. ¿Qué hace primero?", "steps": ["Luis le pregunta: «¿Quieres un abrazo?».", "Espera su respuesta.", "Si Ana dice sí, la abraza; si dice no, hace otra cosa."], "answer": "Preguntar y esperar la respuesta"},
        {"title": "Respetar un no", "problem": "Mía le dice a Beto «hoy no quiero abrazos». ¿Qué responde Beto?", "steps": ["Mía dijo no.", "Beto no insiste.", "Puede ofrecer otra cosa: saludar con la mano."], "answer": "«Está bien, lo respeto»"},
    ],
    mistakes=[
        {"wrong": "Abrazar sin preguntar porque «es amigo».", "why": "Creemos que el cariño no necesita permiso.", "fix": "Pregunta siempre antes."},
        {"wrong": "Insistir cuando alguien dice no.", "why": "Pensamos que el otro cambiará de idea.", "fix": "Un no se respeta; ofrece otra forma de saludar."},
    ],
    tiers={
        "recovery": [
            ex("Antes de abrazar a alguien, ¿qué haces?", "Preguntar", "Eso es pedir consentimiento."),
            ex("Si dicen «no», ¿qué haces: insistir o respetar?", "Respetar", "Un no se acepta."),
            ex("¿Puedes decir «no, gracias» a un abrazo?", "Sí", "Es tu cuerpo y tienes derecho."),
        ],
        "understand": [
            ex("En Orientación, ¿qué es el consentimiento?", "Preguntar y recibir un sí o un no antes de tocar", "Se pide permiso."),
            ex("¿Por qué las personas prefieren cosas distintas?", "Porque cada una es distinta", "Cada persona siente a su manera."),
            ex("¿Debe explicar por qué dijo no?", "No", "Basta con decir no."),
        ],
        "apply": [
            ex("Dani quiere chocar la mano a Sofía. Escribe qué le pregunta.", "Por ejemplo: «¿Quieres chocar la mano?»", "Pide permiso antes."),
            ex("Carla dice «hoy prefiero saludar de lejos». Elige la respuesta correcta: «Está bien» o «Dame un abrazo igual».", "«Está bien»", "Se respeta su preferencia."),
            ex("Pedro no quiere que le den un beso en la mejilla. ¿Qué frase amable puede decir?", "«No, gracias»", "Dice su no con respeto."),
        ],
        "reason": [
            ex("Rosa insiste: «Solo un abrazo, porfa» aunque Tomás dijo no. ¿Hizo bien?", "No", "Presionó en vez de respetar."),
            ex("Eva dijo no a un abrazo, pero sí a un choque de manos. ¿Cambió de idea o tiene preferencias?", "Tiene preferencias", "Cada forma de saludar es distinta."),
        ],
        "challenge": [
            ex("Beto quiere demostrar cariño a un amigo que no quiere contacto. Nombra una forma sin tocar.", "Por ejemplo: una palabra amable o un dibujo", "El cariño no necesita contacto."),
            ex("Si alguien no respeta tu no y sigue insistiendo, ¿qué haces?", "Aviso a un adulto de confianza", "Un adulto puede ayudar."),
        ],
    },
    context=[ex("En el cumpleaños, una tía quiere dar un beso a Ana, pero a Ana no le gusta. ¿Qué puede decir Ana?", "«No, gracias, mejor te saludo con la mano»", "Dice no con respeto y ofrece otra forma.")],
    selfcheck=[ex("¿Debo preguntar antes de abrazar?", "Sí", "Así se respeta al otro."), ex("¿Un no se puede discutir?", "No", "Un no se respeta."), ex("¿Puedo decir no a una muestra de cariño que no quiero?", "Sí", "Mi cuerpo es mío.")],
    open_task=task("Lee la tarjeta: «Mía quiere abrazar a Tomás, que parece triste». Escribe o di tres cosas: lo que Mía pregunta, una respuesta posible de Tomás que diga no, y lo que Mía responde después.", "Mía: «¿Quieres un abrazo?». Tomás: «No, gracias». Mía: «Está bien, estoy aquí si me necesitas».", ["pregunta antes de abrazar", "respeta el no", "ofrece otra forma de apoyo"], ["tres frases escritas o dichas", "dibujo con globos de diálogo"], ["abrazar sin preguntar", "insistir tras un no"], "Reconoce el respeto y pregunta cómo podría ofrecer apoyo de otra forma."),
    reinforce="Practica con un peluche la frase «¿Quieres un abrazo?».",
    extend="Escribe tres formas distintas de saludar sin abrazar.",
)

register(
    OA3, 3,
    materials="Una hoja, lápiz y los casos escritos en cada ejercicio.",
    use="Aprenderé a diferenciar un apoyo de una imposición. Sirve para ayudar sin molestar y recibir ayuda sin sentirme obligado.",
    prior=["Sé que ayudar es una forma de cuidar.", "Sé que puedo decir sí o no."],
    explain=[
        "Dar apoyo es ofrecer ayuda de una forma que la otra persona pueda aceptar o no. Por ejemplo: «¿Te ayudo a guardar los lápices?». El otro puede decir «sí, gracias» o «no, puedo solo».",
        "Imponer es obligar a que se haga lo que yo decido, sin preguntar. Por ejemplo, quitarle el estuche a alguien y guardarlo por él. Aunque quieras ayudar, imponer puede hacer sentir mal, porque la otra persona no tuvo opción.",
        "Recibir ayuda también tiene su manera. Puedes decir: «Sí, gracias» o «Prefiero intentarlo yo». Y si necesitas ayuda, puedes pedirla con claridad: «¿Me ayudas con esto, por favor?».",
    ],
    vocab=[("apoyo", "ayuda que se ofrece"), ("imponer", "obligar a hacer lo que yo quiero"), ("ofrecer", "proponer sin obligar"), ("aceptar", "decir sí a una ayuda"), ("rechazar", "decir no a una ayuda")],
    worked=[
        {"title": "Ofrecer y no imponer", "problem": "Eva ve que Dani está armando un rompecabezas. ¿Qué es apoyo: «¿Quieres que te ayude?» o quitarle las piezas y armarlo ella?", "steps": ["La primera frase pregunta.", "La segunda quita las piezas sin preguntar.", "Apoyar es ofrecer."], "answer": "«¿Quieres que te ayude?»"},
        {"title": "Recibir con claridad", "problem": "Luis quiere hacer su dibujo solo, pero Ana le ofrece ayuda. ¿Qué puede decir Luis?", "steps": ["Luis puede rechazar con respeto.", "Dice: «No, gracias, prefiero hacerlo solo».", "Ana respeta."], "answer": "«No, gracias, prefiero hacerlo solo»"},
    ],
    mistakes=[
        {"wrong": "Quitarle algo a alguien «para ayudarlo».", "why": "Creemos que ayudar es hacerlo por el otro.", "fix": "Primero pregunta si quiere ayuda."},
        {"wrong": "Aceptar una ayuda que no quieres por no molestar.", "why": "Nos da pena decir no.", "fix": "Puedes decir «No, gracias» con amabilidad."},
    ],
    tiers={
        "recovery": [
            ex("«¿Te ayudo?» ¿ofrece o impone?", "Ofrece", "Deja que el otro decida."),
            ex("Quitarle la mochila a un compañero sin preguntar, ¿es apoyo o imposición?", "Imposición", "No dio opción."),
            ex("¿Puedes decir «no, gracias» a una ayuda?", "Sí", "Aceptar es opcional."),
        ],
        "understand": [
            ex("¿Cuál es la diferencia entre apoyo e imposición?", "El apoyo se ofrece y la imposición se obliga", "Una deja elegir y la otra no."),
            ex("¿Por qué conviene preguntar antes de ayudar?", "Para saber si el otro quiere ayuda", "Cada persona decide."),
            ex("Si pides ayuda, ¿cómo lo dices con claridad?", "«¿Me ayudas con esto, por favor?»", "Dice qué necesitas."),
        ],
        "apply": [
            ex("Mía ve que Tomás no puede abrir su botella. Escribe una frase para ofrecer ayuda.", "Por ejemplo: «¿Quieres que te ayude a abrirla?»", "Pregunta antes de ayudar."),
            ex("Pedro prefiere vestirse solo. Escribe cómo puede responder si su papá le ofrece ayuda.", "Por ejemplo: «No, gracias, quiero intentarlo yo»", "Rechaza con respeto."),
            ex("Sofía necesita ayuda con un cordón. Escribe cómo la pide.", "Por ejemplo: «¿Me ayudas con el cordón, por favor?»", "Pide con claridad y amabilidad."),
        ],
        "reason": [
            ex("Rosa terminó la tarea de Beto «para ayudarlo» sin preguntarle. ¿Fue apoyo o imposición? ¿Por qué?", "Imposición, porque no le preguntó", "Beto no pudo elegir."),
            ex("Carla ofreció ayuda y Dani dijo no. Carla se fue molesta. ¿Respetó el no?", "No", "Respetar es aceptar sin enojarse."),
        ],
        "challenge": [
            ex("Un amigo está intentando algo difícil. ¿Cuál ayuda lo respeta más: darle una pista cuando la pida o hacerlo todo por él?", "Darle una pista cuando la pida", "Respeta su decisión de intentarlo."),
            ex("Dos niños necesitan ayuda: uno la pide, el otro dice que está bien. ¿A quién ayudas ahora?", "Al que la pide", "Se ayuda a quien lo solicita."),
        ],
    },
    context=[ex("Un niño pequeño del patio intenta subir al columpio. Eva se acerca y le dice: «¿Quieres que te dé un empujoncito?». Él dice: «No, lo hago yo». ¿Qué debe hacer Eva?", "Respetar y quedarse cerca", "Respeta su decisión y lo acompaña.")],
    selfcheck=[ex("¿Dar apoyo es obligar?", "No", "Apoyar es ofrecer."), ex("¿Puedo decir no a una ayuda?", "Sí", "Aceptar es una decisión."), ex("¿Cómo se ofrece ayuda con respeto?", "Preguntando", "Así el otro elige.")],
    open_task=task("Lee el caso: «Ana intenta pegar una figura en su cuaderno y se le arruga. Luis la ve». Escribe o di tres frases: lo que Luis dice para ofrecer ayuda, lo que Ana responde si acepta y lo que responde si prefiere intentarlo sola.", "Luis: «¿Quieres que te ayude?». Ana acepta: «Sí, gracias». Ana rechaza: «No, gracias, lo intento yo».", ["ofrece con una pregunta", "incluye una respuesta de aceptación", "incluye una respuesta de rechazo respetuoso"], ["tres frases", "dibujo con globos"], ["frase que da órdenes", "enojarse ante un no"], "Reconoce las frases que dejan elegir y ayuda a cambiar las que obligan."),
    reinforce="Pregunta a alguien en casa si quiere ayuda con una tarea pequeña y respeta su respuesta.",
    extend="Escribe una situación en que ayudar sin preguntar pudo hacer sentir mal a alguien.",
)

register(
    OA3, 4,
    materials="Una hoja, lápiz y la ficha de red de cuidado escrita en el ejercicio; no se escribe ningún dato personal.",
    use="Aprenderé a reconocer qué adultos y espacios me cuidan, sin decir datos privados. Sirve para saber a quién acudir si necesito ayuda.",
    prior=["Sé que hay personas que me cuidan.", "Sé qué es pedir ayuda."],
    explain=[
        "Una red de cuidado son las personas que te cuidan y te ayudan. Pueden ser familiares, tu profesora, la persona que te cuida en el recreo o un vecino de confianza. Cada niño tiene una red distinta, y todas son válidas.",
        "Un adulto seguro es alguien que te trata bien, te escucha, respeta tus límites y no te pide guardar secretos que te hagan sentir mal. Si no te sientes tranquilo con una persona, avisa a otro adulto de confianza.",
        "Puedes pensar en tu red con una mano: un dedo por cada adulto o lugar de confianza. Esta red se puede dibujar sin nombres ni direcciones. Así protegemos nuestros datos y todos podemos participar.",
    ],
    vocab=[("red de cuidado", "personas y lugares que me cuidan"), ("adulto seguro", "adulto que me trata bien y respeta mis límites"), ("confianza", "sentir que alguien me cuida"), ("secreto que no me hace sentir bien", "algo que alguien me pide guardar y me da miedo o pena"), ("dato privado", "información personal que no se comparte con cualquiera")],
    worked=[
        {"title": "Reconocer un adulto seguro", "problem": "Tomás tiene una profesora que lo escucha y le pregunta cómo está. ¿Es un adulto seguro?", "steps": ["La profesora lo trata bien.", "Lo escucha.", "Respeta cómo se siente."], "answer": "Sí, es un adulto seguro"},
        {"title": "Dibujar la red sin datos", "problem": "Mía dibuja una mano con cinco dedos y escribe «mamá, mi tía, mi profe, el guardia del colegio, la bibliotecaria». ¿Escribió datos privados?", "steps": ["Solo puso quiénes son, no sus nombres ni direcciones.", "No dice dónde vive nadie.", "Está bien."], "answer": "No, no incluyó datos privados"},
    ],
    mistakes=[
        {"wrong": "Pensar que un adulto es seguro solo por ser amable con regalos.", "why": "Los regalos pueden confundir.", "fix": "Un adulto seguro respeta tus límites y te escucha."},
        {"wrong": "Escribir direcciones o teléfonos en la red.", "why": "Creemos que hay que contar todo para que sea completa.", "fix": "Dibuja solo quiénes son, sin datos privados."},
    ],
    tiers={
        "recovery": [
            ex("¿Tu mamá, papá o cuidador pueden ser parte de tu red?", "Sí", "Son personas que te cuidan."),
            ex("¿Un adulto que te escucha con respeto puede ser seguro?", "Sí", "Escuchar es una señal de cuidado."),
            ex("¿Debes escribir tu dirección en la red de cuidado?", "No", "La red no necesita datos privados."),
        ],
        "understand": [
            ex("¿Qué es una red de cuidado?", "Las personas y lugares que me cuidan", "Son quienes me ayudan."),
            ex("¿Cuál es una señal de adulto seguro: respeta tus límites o te pide guardar secretos que te asustan?", "Respeta tus límites", "Un adulto seguro cuida."),
            ex("¿Todas las redes de cuidado son iguales?", "No", "Cada niño tiene su propia red."),
        ],
        "apply": [
            ex("Ana tiene a su abuela, a su profesora y al guardia del colegio. ¿Cuántas personas hay en su red?", "3", "Son tres adultos."),
            ex("Beto dibuja su red con una mano. ¿Cuántos dedos usa si nombra a 4 personas?", "4", "Un dedo por persona."),
            ex("Carla se siente mal en el patio. Elige a quién acude: a la profesora de turno o a alguien que no conoce.", "A la profesora de turno", "Es un adulto de su red."),
        ],
        "reason": [
            ex("Un adulto le dice a Pedro: «Guarda este secreto, no se lo cuentes a nadie», y Pedro se siente mal. ¿Qué debe hacer?", "Contar a otro adulto de confianza", "Un secreto que incomoda se cuenta."),
            ex("Dani dibuja su red con nombres, calles y teléfonos. ¿Qué debe cambiar?", "Quitar los datos privados", "La red solo necesita decir quiénes."),
        ],
        "challenge": [
            ex("Sofía dice: «Mi red es más grande que la tuya». ¿Es mejor tener una red grande?", "No", "Lo importante es que haya al menos un adulto seguro."),
            ex("Eva tiene un adulto seguro en casa y otro en el colegio. ¿Dónde puede pedir ayuda si está en el colegio?", "Con el adulto del colegio", "Está cerca y puede ayudar."),
        ],
    },
    context=[ex("Luis dibuja una mano con cuatro dedos: «Mi tío», «Mi profe», «Mi abuela» y «El cuidador del recreo». Dice dónde vive cada uno. ¿Qué debe hacer?", "No decir dónde viven", "Eso son datos privados.")],
    selfcheck=[ex("¿Mi red puede incluir a mi profesora?", "Sí", "Una profesora cuida y apoya."), ex("¿Debo contar a un adulto de confianza si algo me asusta?", "Sí", "Para recibir ayuda."), ex("¿En el dibujo de mi red pongo mi dirección?", "No", "Es un dato privado.")],
    open_task=task("Dibuja una mano de cinco dedos. En cada dedo dibuja o escribe un tipo de persona o lugar de confianza, sin nombres ni direcciones. Puedes elegir de esta lista: mi familia, mi profesora, un compañero amable, la biblioteca del colegio, el cuidador del recreo. Cuéntale a un adulto de confianza cómo te sientes con tu red.", "Dedo 1: mi familia. Dedo 2: mi profesora. Dedo 3: la biblioteca. Dedo 4: el cuidador del recreo.", ["dibuja una mano con al menos tres dedos usados", "no escribe datos privados", "incluye al menos un adulto"], ["mano dibujada", "frase breve sobre cómo se siente con su red"], ["escribir direcciones o teléfonos", "incluir a alguien que lo hace sentir mal"], "Reconoce lo que incluyó y recuerda que siempre puede sumar o cambiar personas."),
    reinforce="Muestra tu mano de la red a alguien de confianza y cuéntale quién es cada dedo.",
    extend="Piensa en un lugar del colegio donde puedes pedir ayuda y dibuja cómo llegar sin escribir datos privados.",
)
