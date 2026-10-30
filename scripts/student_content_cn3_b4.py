"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 13 (modelos de eclipses, diseño de un modelo seguro y evaluación de sus alcances)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA13 = "CN03 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA13, 3,
    materials="Una linterna fija, una pelota grande o naranja como Tierra, una bolita de plasticina de 2 cm como Luna en un palito de helado, una pieza oscura y una mesa. Nunca mires al Sol; los eclipses se estudian con el modelo.",
    use="Aprenderé a distinguir el eclipse de Sol y el eclipse de Luna con un modelo. Sirve para saber qué cuerpo hace sombra sobre cuál.",
    prior=["Sé las posiciones del Sol, la Tierra y la Luna en las fases.", "Sé que un objeto opaco forma sombra."],
    explain=[
        "Un eclipse ocurre cuando tres cuerpos del Sistema Solar quedan alineados y la sombra de uno cae sobre otro. En un eclipse de Sol, la Luna queda entre el Sol y la Tierra y su sombra cae sobre una pequeña zona de la Tierra. Desde esa zona, la Luna tapa el Sol por unos minutos. Ocurre en Luna nueva. Si la Luna tapa todo el Sol, el eclipse es total; si tapa solo una parte, es parcial.",
        "En un eclipse de Luna, la Tierra queda entre el Sol y la Luna y su sombra cae sobre la Luna. La Luna se oscurece y a veces se ve rojiza. Ocurre en Luna llena. Se puede mirar sin peligro desde cualquier lugar donde sea de noche y la Luna esté en el cielo.",
        "Los eclipses no ocurren todos los meses, porque la órbita de la Luna está un poco inclinada y casi siempre la sombra pasa por arriba o por abajo. El eclipse de Sol nunca se debe mirar directamente: daña los ojos aunque el Sol esté casi tapado. Solo se mira con lentes especiales para eclipses, que tienen certificación (los lentes de sol comunes no sirven), o con una proyección indirecta, siempre con una persona adulta.",
    ],
    vocab=[("eclipse", "cuando la sombra de un cuerpo cae sobre otro"), ("alineación", "tres cuerpos casi en una misma línea"), ("sombra", "zona sin luz que deja un objeto opaco"), ("total", "cuando el cuerpo queda completamente tapado"), ("parcial", "cuando solo una parte queda tapada")],
    worked=[
        {"title": "Eclipse de Sol", "problem": "La linterna, la bolita y la pelota quedan en línea, con la bolita en medio. ¿Qué eclipse representa?", "steps": ["La bolita (Luna) está entre la linterna (Sol) y la pelota (Tierra).", "La sombra de la bolita cae sobre la pelota.", "Es un eclipse de Sol."], "answer": "Eclipse de Sol"},
        {"title": "Eclipse de Luna", "problem": "Ahora la pelota (Tierra) queda en medio, entre la linterna y la bolita. ¿Qué eclipse representa?", "steps": ["La Tierra está entre el Sol y la Luna.", "La sombra de la Tierra cae sobre la Luna.", "Es un eclipse de Luna."], "answer": "Eclipse de Luna"},
    ],
    mistakes=[
        {"wrong": "Mirar un eclipse de Sol sin protección porque el Sol está tapado casi del todo.", "why": "Se piensa que un Sol tapado no daña.", "fix": "Nunca mires el Sol directamente; usa lentes certificados o una proyección indirecta con una persona adulta."},
        {"wrong": "Decir que en el eclipse de Luna la Luna se apaga.", "why": "Se ve oscura.", "fix": "La sombra de la Tierra cae sobre ella, pero la Luna sigue ahí."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué cuerpo queda en medio en un eclipse de Sol?", "La Luna", "La Luna tapa al Sol."),
            ex("¿Qué cuerpo queda en medio en un eclipse de Luna?", "La Tierra", "Su sombra cae sobre la Luna."),
            ex("Completa: un eclipse de Sol ocurre en Luna ___.", "nueva", "La Luna queda entre el Sol y la Tierra."),
        ],
        "understand": [
            ex("¿Qué es un eclipse?", "Cuando la sombra de un cuerpo cae sobre otro", "Se produce por una alineación."),
            ex("¿En qué fase de la Luna ocurre un eclipse de Luna?", "En Luna llena", "La Tierra queda entre el Sol y la Luna."),
            ex("¿Por qué no hay eclipses todos los meses?", "Porque la órbita de la Luna está inclinada y la sombra suele pasar por arriba o abajo", "No siempre hay alineación."),
        ],
        "apply": [
            ex("Clasifica: la Tierra proyecta su sombra sobre la Luna. ¿Eclipse de Sol o de Luna?", "Eclipse de Luna", "La Luna recibe la sombra."),
            ex("La Luna proyecta su sombra sobre una zona de la Tierra. ¿Eclipse de Sol o de Luna?", "Eclipse de Sol", "Desde esa zona el Sol queda tapado."),
            ex("Un eclipse de Luna ocurre de noche en Chile. ¿Puedes mirarlo sin peligro a simple vista?", "Sí", "La Luna refleja luz débil y no daña los ojos."),
        ],
        "reason": [
            ex("Felipe dice: «Puedo mirar un eclipse de Sol si casi está tapado». ¿Es seguro?", "No", "Sigue siendo el Sol, que daña los ojos."),
            ex("Ana dice que en un eclipse de Sol se oscurece toda la Tierra. ¿Qué dato del modelo la corrige?", "Solo una zona pequeña queda en la sombra de la Luna", "La sombra de la bolita cubre solo una parte de la pelota."),
        ],
        "challenge": [
            ex("El 2 de julio de 2019, en la Región de Coquimbo, la Luna tapó todo el Sol por unos minutos. ¿Fue un eclipse total o parcial?", "Total", "La Luna quedó en medio y tapó el Sol completo."),
            ex("Quieres mostrar un eclipse de Luna con tu modelo. ¿Dónde pones la pelota: entre la linterna y la bolita, o al lado de la linterna?", "Entre la linterna y la bolita", "Así la sombra de la Tierra cae sobre la Luna."),
        ],
    },
    context=[ex("Un telediario avisa que esta noche habrá un eclipse de Luna visible en Chile. Una persona de la casa dice que mejor no mirarlo porque daña. ¿Tiene razón?", "No, un eclipse de Luna se puede mirar sin peligro", "A diferencia del Sol, la Luna no daña los ojos.")],
    selfcheck=[
        ex("¿Qué se alinea en un eclipse?", "El Sol, la Tierra y la Luna", "Tres cuerpos casi en línea."),
        ex("¿Se puede mirar directamente un eclipse de Sol?", "No", "Daña los ojos."),
        ex("¿Qué fase tiene la Luna en un eclipse de Luna?", "Luna llena", "La Tierra está entre el Sol y la Luna."),
    ],
    open_task=task(
        "Si puedes, usa la linterna, la pelota y la bolita en una pieza oscura. Alinéalas de dos maneras: bolita en medio, y pelota en medio. Anota dónde cae la sombra en cada caso. Si no puedes, dibuja las dos alineaciones con tres círculos en fila: en la primera, Sol, Luna, Tierra; en la segunda, Sol, Tierra, Luna. Pinta la sombra y rotula cada eclipse.",
        "Con la bolita en medio, su sombra cae sobre la pelota: eclipse de Sol. Con la pelota en medio, su sombra cae sobre la bolita: eclipse de Luna.",
        ["dibuja las dos alineaciones", "pinta la sombra en el cuerpo correcto", "rotula eclipse de Sol y de Luna"],
        ["dos dibujos", "frases de rotulación"],
        ["intercambiar los dos eclipses", "olvidar la sombra"],
        "Valora los dibujos y pregunta qué fase de la Luna ocurre en cada eclipse.",
    ),
    reinforce="Explica a alguien de tu casa la diferencia entre un eclipse de Sol y uno de Luna usando tres objetos.",
    extend="Pregunta a una persona de tu casa si vio el eclipse de Sol de 2019 y cómo lo miró de forma segura.",
)

register(
    OA13, 4,
    materials="Una linterna, una pelota de 7 cm o naranja para la Tierra, una bolita de plasticina de 2 cm para la Luna, tres palitos de helado, plasticina para sostener y una caja de cartón como base. Tijeras de punta redonda solo con una persona adulta. Sin fuego, sin vidrio y sin mirar el Sol.",
    use="Aprenderé a diseñar y construir un modelo seguro que explique las fases y los eclipses. Sirve para mostrar un evento del cielo sin mirar el Sol.",
    prior=["Sé las posiciones del Sol, la Tierra y la Luna en las fases y eclipses.", "Sé que un objeto opaco forma sombra."],
    explain=[
        "Un modelo tecnológico se diseña y se construye para explicar algo. Primero defino el problema: mostrar cómo se produce un eclipse y las fases. Luego dibujo el diseño, listo los materiales, lo construyo, lo pruebo y lo mejoro.",
        "En mi modelo, cada pieza representa un cuerpo. La linterna es el Sol porque emite luz. La pelota es la Tierra y la bolita en un palito es la Luna. La bolita se mueve con facilidad para cambiar las posiciones. Debo poder alinear los tres cuerpos y ver las sombras.",
        "Mi modelo debe ser seguro: se usa en una pieza oscura con linterna, nunca con el Sol real; la luz no se apunta a los ojos; las tijeras solo las usa una persona adulta; no uso vidrio ni fuego. Un buen modelo cumple criterios: muestra las posiciones, permite ver la sombra, se puede mover y es seguro.",
    ],
    vocab=[("diseño", "plan o dibujo de lo que voy a construir"), ("prototipo", "primera versión de un modelo para probarlo"), ("criterio", "condición que debe cumplir el modelo"), ("probar", "usar el modelo para ver si funciona"), ("mejorar", "cambiar algo para que funcione mejor")],
    worked=[
        {"title": "Qué representa cada pieza", "problem": "¿Qué pieza usas para el Sol y por qué?", "steps": ["El Sol emite luz.", "La linterna también emite luz.", "Entonces la linterna representa al Sol."], "answer": "La linterna"},
        {"title": "Un criterio de seguridad", "problem": "Un compañero quiere probar el modelo apuntando un espejo al Sol. ¿Está bien?", "steps": ["No se debe mirar el Sol ni reflejar su luz.", "El modelo se prueba en una pieza oscura con linterna."], "answer": "No, es inseguro; se usa la linterna en una pieza oscura"},
    ],
    mistakes=[
        {"wrong": "Usar el Sol real para probar el modelo.", "why": "Se piensa que sería más real.", "fix": "Usa una linterna en una pieza oscura; el Sol real daña los ojos."},
        {"wrong": "Construir sin diseñar ni probar.", "why": "Se quiere terminar rápido.", "fix": "Dibuja el diseño, construye, prueba y mejora."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué representa la linterna en el modelo?", "El Sol", "Es la fuente de luz."),
            ex("¿Qué representa la pelota grande?", "La Tierra", "Es el cuerpo grande donde vivimos."),
            ex("Completa: la bolita en un palito representa la ___.", "Luna", "Es el cuerpo pequeño que gira alrededor de la Tierra."),
        ],
        "understand": [
            ex("¿Por qué conviene que la Luna del modelo esté en un palito?", "Para poder moverla y alinearla", "Así cambio las posiciones."),
            ex("¿Por qué el modelo se prueba en una pieza oscura?", "Para que solo la linterna ilumine y se vean las sombras", "Otra luz dificultaría ver la sombra."),
            ex("¿Por qué no se debe probar el modelo con el Sol real?", "Porque mirar el Sol daña los ojos", "Es una regla de seguridad."),
        ],
        "apply": [
            ex("Ordena los pasos de la tecnología: construir, diseñar, probar, mejorar.", "Diseñar, construir, probar, mejorar", "Se planifica antes de construir y se prueba antes de mejorar."),
            ex("Tu modelo muestra la sombra de la Luna sobre la Tierra. ¿Qué evento representa?", "Un eclipse de Sol", "La Luna tapa al Sol."),
            ex("Quieres mostrar una alineación de Luna llena. ¿Pones la pelota entre la linterna y la bolita o la bolita entre la linterna y la pelota?", "La pelota entre la linterna y la bolita", "En Luna llena la Tierra queda entre el Sol y la Luna."),
        ],
        "reason": [
            ex("Un modelo hecho con tijeras sin ayuda de un adulto y con una vela como Sol, ¿cumple los criterios de seguridad?", "No", "Hay fuego y tijeras sin supervisión."),
            ex("Tu modelo se mueve tanto que la sombra no cae donde quieres. ¿Qué criterio no cumple: que se pueda mover con control o que sea de cartón?", "Que se pueda mover con control", "Debe poder alinearse con facilidad."),
        ],
        "challenge": [
            ex("Para que el modelo muestre mejor las fases, ¿qué mejora sirve: marcar con papelitos cuatro posiciones de la Luna alrededor de la Tierra o pintar la linterna de rojo?", "Marcar con papelitos cuatro posiciones de la Luna", "Facilita repetir las posiciones de cada fase."),
            ex("De estas tres condiciones, ¿cuáles son criterios de tu modelo: mostrar las posiciones Sol-Tierra-Luna, ser seguro o ser muy caro?", "Mostrar las posiciones y ser seguro", "Un buen modelo muestra lo que quiero explicar y es seguro; el precio no es un criterio."),
        ],
    },
    context=[ex("Mateo quiere construir un modelo de eclipse con una linterna, una naranja y una bolita. No tiene palitos. ¿Qué podría usar para sostener la bolita?", "Un trozo de plasticina o un lápiz con plasticina", "Sirve para mover la bolita.")],
    selfcheck=[
        ex("¿Qué pieza representa al Sol?", "La linterna", "La linterna emite luz como el Sol."),
        ex("¿Qué se hace antes de construir?", "Diseñar", "Se hace un plan."),
        ex("¿Dónde se prueba el modelo?", "En una pieza oscura", "No se usa el Sol real."),
    ],
    open_task=task(
        "Diseña un modelo con la lista de materiales de la clase. Haz un dibujo con las piezas rotuladas, escribe tres criterios (por ejemplo, que se vea la sombra, que se pueda mover y que sea seguro) y construye el modelo si puedes. Pruébalo con las dos alineaciones de eclipse y anota si cumple los criterios.",
        "Mi modelo tiene linterna, pelota y bolita en un palito. Criterios: se ve la sombra, se mueve, es seguro. Lo probé en una pieza oscura y mostró el eclipse de Sol y el de Luna.",
        ["dibuja y rotula el diseño", "escribe tres criterios", "anota el resultado de la prueba"],
        ["dibujo del diseño", "lista de criterios", "registro de la prueba"],
        ["usar el Sol real", "no escribir criterios"],
        "Valora el diseño y pide una mejora concreta.",
    ),
    reinforce="Rotula con papelitos las piezas de tu modelo y explica qué representa cada una a alguien de tu casa.",
    extend="Averigua qué otro modelo se usa para explicar el cielo, como una maqueta del Sistema Solar.",
)

register(
    OA13, 5,
    materials="Papel y lápiz. Si construiste el modelo, tenlo a mano; si no, usa la descripción escrita en el cuaderno.",
    use="Aprenderé a evaluar qué muestra bien y qué no muestra un modelo del Sol, la Tierra y la Luna. Sirve para usar los modelos con cuidado.",
    prior=["Sé que un modelo representa algo real.", "Sé construir un modelo de fases y eclipses."],
    explain=[
        "Todos los modelos tienen alcances, es decir, lo que muestran bien, y limitaciones, es decir, lo que no muestran bien. Mi modelo muestra bien el orden de los cuerpos, la alineación y dónde cae la sombra.",
        "Pero mi modelo no respeta tamaños ni distancias reales. Si la Tierra midiera 4 cm, la Luna mediría 1 cm y estaría a unos 120 cm de ella. El Sol mediría unos 436 cm de ancho, más de 4 metros, y estaría a unos 470 metros. Por eso en el modelo todo está mucho más cerca y casi del mismo tamaño. Tampoco muestra la inclinación de la órbita de la Luna.",
        "Para evaluar un modelo reviso criterios: ¿muestra lo que quiero explicar?, ¿es seguro?, ¿qué no muestra?, ¿qué puedo mejorar? Una buena evaluación es honesta: dice lo que el modelo logra y también sus limitaciones. Así otras personas saben cómo usarlo.",
    ],
    vocab=[("alcance", "lo que un modelo logra mostrar bien"), ("limitación", "lo que un modelo no muestra bien"), ("evaluar", "revisar qué tan bien cumple un modelo sus criterios"), ("escala", "relación entre el tamaño del modelo y el real"), ("honesto", "que dice la verdad, incluso sobre lo que no resultó")],
    worked=[
        {"title": "Un alcance y una limitación", "problem": "Tu modelo usa una linterna cerca de la pelota. ¿Qué muestra bien y qué no?", "steps": ["Muestra bien la alineación y la sombra.", "No muestra las distancias reales."], "answer": "Muestra la alineación y la sombra; no muestra tamaños ni distancias reales"},
        {"title": "Tamaños a escala", "problem": "Si la Tierra mide 4 cm y la Luna mide cerca de una cuarta parte de la Tierra, ¿cuánto mide la Luna?", "steps": ["Una cuarta parte de 4 es 4 ÷ 4.", "4 ÷ 4 = 1."], "answer": "1 cm"},
    ],
    mistakes=[
        {"wrong": "Pensar que el modelo muestra los tamaños reales.", "why": "Las piezas se ven bien proporcionadas entre sí.", "fix": "Los tamaños y distancias del modelo son mucho más pequeños y cercanos que los reales."},
        {"wrong": "Evaluar el modelo diciendo solo que «está bonito».", "why": "No se usan criterios.", "fix": "Evalúa con criterios: qué muestra, qué no, qué mejorar."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es una limitación de un modelo?", "Lo que no muestra bien", "Es una parte donde el modelo no es fiel."),
            ex("¿Qué es un alcance de un modelo?", "Lo que muestra bien", "Es lo que logra explicar."),
            ex("Completa: el modelo de la linterna y las pelotas no respeta los tamaños ni las ___ reales.", "distancias", "En el modelo todo está muy cerca."),
        ],
        "understand": [
            ex("¿Por qué es importante decir las limitaciones de un modelo?", "Para saber hasta dónde se puede confiar en él", "Evita sacar conclusiones equivocadas."),
            ex("¿Qué muestra bien el modelo de eclipses: la alineación y dónde cae la sombra, o los tamaños reales?", "La alineación y dónde cae la sombra", "Eso permite explicar los eclipses; los tamaños no son reales."),
            ex("¿Qué debe incluir una evaluación honesta de un modelo, además de lo que muestra bien?", "Lo que no muestra bien", "La honestidad incluye las limitaciones."),
        ],
        "apply": [
            arith("En un modelo a escala, la Tierra mide 4 cm y la Luna 1 cm. ¿Cuántos cm más ancha es la Tierra que la Luna?", "4-1", "Se resta el ancho menor del mayor.", " cm"),
            arith("En un modelo a escala, el Sol mediría unos 436 cm. Tu mesa mide 150 cm de largo. ¿Cuántos cm le faltan a la mesa para igualar el ancho del Sol?", "436-150", "Se resta el largo de la mesa a los 436 cm.", " cm"),
            ex("En tu modelo, la linterna está a 30 cm de la pelota. En la realidad, el Sol está mucho más lejos. ¿Es una limitación o un alcance?", "Una limitación", "La distancia no es real."),
        ],
        "reason": [
            ex("Un compañero dice: «Mi modelo prueba cuántos minutos dura un eclipse». ¿Puede probarlo?", "No", "El modelo no muestra el tiempo real."),
            ex("Dos modelos: uno cuesta mucho y es bonito pero no se pueden alinear los cuerpos; el otro es de cartón y muestra bien la alineación. ¿Cuál cumple mejor el criterio de explicar el eclipse?", "El de cartón", "Lo importante es que muestre la alineación."),
        ],
        "challenge": [
            ex("Con la Tierra de 4 cm, la Luna a escala estaría a unos 120 cm. En tu modelo está a 30 cm. ¿La Luna real está más cerca o más lejos de la Tierra que en tu modelo?", "Más lejos", "La Luna real está mucho más lejos que en el modelo."),
            ex("Una evaluación dice: «Muestra la alineación; no muestra tamaños reales; mejoraría la base». ¿Incluye alcance, limitación y mejora?", "Sí, incluye los tres", "El alcance es la alineación, la limitación son los tamaños y la mejora es la base."),
        ],
    },
    context=[ex("En una feria de ciencias, Ignacio dice que su modelo muestra los tamaños reales del Sol y la Luna. ¿Qué dato de esta clase usas para ayudarlo a corregir?", "Que el Sol sería enorme comparado con la Tierra, mucho más grande que el modelo", "El modelo no respeta la escala de tamaños.")],
    selfcheck=[
        ex("¿Un modelo puede tener limitaciones y aun así ser útil?", "Sí", "Sirve para lo que sí muestra bien."),
        ex("¿Qué muestra bien el modelo de eclipses?", "La alineación y la sombra", "Es su alcance."),
        ex("¿Qué no muestra bien el modelo?", "Los tamaños y las distancias reales", "Es una limitación."),
    ],
    open_task=task(
        "Evalúa tu modelo con esta tabla: alcance 1 (qué muestra bien), alcance 2, limitación 1 (qué no muestra), limitación 2 y una mejora. Si no tienes modelo, evalúa este: una linterna, una naranja y una bolita en un palito, a 30 cm unas de otras. Escribe tu evaluación en cinco frases.",
        "Alcance 1: muestra la alineación. Alcance 2: muestra la sombra. Limitación 1: los tamaños no son reales. Limitación 2: no muestra la inclinación de la órbita de la Luna. Mejora: agregar una nota con las distancias reales.",
        ["escribe dos alcances y dos limitaciones", "propone una mejora concreta", "usa un lenguaje honesto"],
        ["tabla de evaluación", "cinco frases"],
        ["decir que el modelo es perfecto", "no escribir ninguna limitación"],
        "Valora la honestidad y pide que explique la mejora propuesta con un ejemplo.",
    ),
    reinforce="Explica a alguien de tu casa por qué un mapa y un globo terráqueo son modelos con alcances y limitaciones.",
    extend="Averigua qué instrumentos usan los científicos para estudiar los eclipses de verdad.",
)
