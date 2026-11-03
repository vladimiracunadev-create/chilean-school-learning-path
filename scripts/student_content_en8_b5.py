"""Cuaderno del estudiante, 8.º básico Inglés (propuesta): EN08 OA 13, proceso de escritura (clases 1 a 3).

Clase 1: organizar ideas. Clase 2: redactar. Clase 3: revisar. Los títulos de clase del plan son genéricos; aquí cada
clase aplica un paso del proceso (organizar, redactar, revisar, editar, publicar). Textos originales y breves, con
pista en español, sin audio ni material externo.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA13 = "EN08 OA 13"


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


# ================================================================ clase 1: organizar ideas
lesson(
    OA13, 1,
    "Las listas de ideas y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé el primer paso del proceso de escritura: organizar las ideas antes de escribir. Sirve para saber para qué escribo, qué ideas uso y en qué orden.",
    ["Sé escribir oraciones simples y párrafos cortos en inglés.", "Conozco conectores como first, then y because."],
    [
        "El proceso de escritura tiene cinco pasos: organizar ideas (organize), redactar (draft), revisar (revise), editar (edit) y publicar (publish). Hoy practicamos el primero. Antes de escribir, decide tu propósito (purpose): informar (to inform), que es dar datos; dar una opinión (to express an opinion), que es decir lo que piensas con razones; o narrar (to narrate), que es contar hechos en orden.",
        "Luego haz una lluvia de ideas (brainstorm): anota muchas ideas rápido, sin juzgarlas. Después elimina las que no tienen que ver con el tema (off-topic), agrupa las demás y ordénalas en un esquema (outline) con tres partes: introduction (presenta el tema), main points (los puntos principales, con razones o datos) y conclusion (cierra la idea). Un esquema puede ser una lista o un mapa de ideas.",
        "Ejemplo para informar sobre el reciclaje en un colegio ficticio. Ideas: Each class has a blue box. Bottles are washed on Fridays. My favourite food is pizza. The bottles go to a recycling company. La tercera idea no sirve, porque no tiene relación con el tema. Esquema: Introduction: Our school recycles bottles. Main points: blue boxes; washing on Fridays. Conclusion: recycling helps our school.",
    ],
    [("organize ideas", "organizar ideas: primer paso del proceso"), ("purpose", "propósito: para qué escribes"), ("to inform", "informar: dar datos"), ("to express an opinion", "dar una opinión con razones"), ("to narrate", "narrar: contar hechos en orden"), ("brainstorm", "lluvia de ideas"), ("off-topic", "fuera del tema"), ("outline", "esquema: plan con introducción, puntos y conclusión")],
    [
        ("Descartar una idea fuera del tema", "Ideas para informar sobre el reciclaje: 1) Each class has a blue box. 2) My favourite food is pizza. 3) Bottles are washed on Fridays. ¿Qué idea se descarta? Responde con su número.", ["El tema es el reciclaje en el colegio.", "Las ideas 1 y 3 hablan de eso.", "La idea 2 es sobre comida."], "2"),
        ("Ordenar un esquema", "Ordena las partes de un esquema: a) Conclusion b) Introduction c) Main points. Escribe las letras en orden.", ["Primero se presenta el tema.", "Luego van los puntos principales.", "Al final se cierra con la conclusión."], "b, c, a"),
    ],
    [
        ("Empezar a escribir sin plan.", "Sin esquema se pierde el orden y aparecen ideas fuera del tema.", "Haz la lluvia de ideas y el esquema primero."),
        ("Dejar en el plan una idea que no tiene relación con el tema.", "Distrae al lector y alarga el texto sin aportar.", "Elimina las ideas fuera del tema."),
    ],
    [
        ("Ordena los cinco pasos del proceso de escritura y escribe las letras en orden. a) edit b) organize ideas c) publish d) draft e) revise", "b, d, e, a, c", "El orden es organizar, redactar, revisar, editar y publicar."),
        ("«Say what you think and give reasons» corresponde a qué propósito? A) To narrate B) To express an opinion", "B", "Dar una opinión con razones es el propósito de un texto de opinión."),
        ("Una lluvia de ideas (brainstorm) consiste en A) anotar muchas ideas rápido B) corregir la ortografía", "A", "Se anotan muchas ideas antes de elegir."),
    ],
    [
        ("«Last summer, I went to the beach. First, we took a bus. Then we built a sandcastle.» ¿Qué propósito tiene? A) To inform B) To narrate C) To express an opinion", "B", "Cuenta hechos pasados en orden."),
        ("Ideas para un plan sobre el reciclaje en el colegio: 1) Each class has a blue box. 2) Bottles are washed on Fridays. 3) My favourite food is pizza. 4) The bottles go to a recycling company. ¿Cuál de estas ideas no pertenece al plan? Responde con su número.", "3", "Es la única que no habla del reciclaje."),
        ("En un esquema, ¿dónde va la idea final «Recycling helps our school»? A) Introduction B) Conclusion", "B", "Cierra el texto, por lo que va en la conclusión."),
    ],
    [
        ("Ideas para el plan de opinión «I think we need more bins»: 1) There is only one bin in the yard. 2) Many students throw paper on the floor. 3) My cousin has a red bike. 4) Bins keep the yard clean. ¿Qué idea no sirve para este plan? Responde con su número.", "3", "La bicicleta no se relaciona con los basureros del patio."),
        ("Para un texto que narra un fin de semana, ¿qué primera oración calza con el propósito? A) First, I played football with my cousins. B) Football is the best sport in the world.", "A", "Narrar es contar hechos en orden, y A comienza una secuencia."),
        ("Ordena el esquema y escribe las letras en orden. a) Conclusion: Recycling helps our school. b) Introduction: Our school recycles bottles. c) Main point: Each class has a blue box.", "b, c, a", "El esquema va de la introducción a los puntos y luego a la conclusión."),
    ],
    [
        ("¿Por qué se elimina «My favourite food is pizza» de un plan sobre el reciclaje? A) Está fuera del tema B) Es demasiado larga", "A", "No aporta nada al tema elegido."),
        ("Un plan para un texto de opinión solo tiene la idea «I like it». ¿Qué le falta? A) Razones B) Un título", "A", "Una opinión necesita razones que la apoyen."),
    ],
    [
        ("Tarjetas de ideas: 1) Bins keep the yard clean. 2) There is only one bin. 3) Students throw paper. 4) We need more bins. 5) My cat is black. La opinión es la tarjeta 4 y la 5 está fuera del tema. ¿Qué tarjetas son las razones? Escribe los números en orden.", "1, 2, 3", "Las razones son las que apoyan la opinión: 1, 2 y 3."),
        ("Ana escribió el texto final y después hizo el plan. ¿Qué error cometió? A) No organizó las ideas antes de redactar B) Publicó antes de terminar", "A", "El plan debe hacerse antes de redactar."),
    ],
    [("La revista escolar pide un texto breve para informar sobre una actividad del colegio. ¿Qué esquema calza? A) Introduction: nombre de la actividad; main points: cuándo y dónde, qué pasó; conclusion B) Introduction: mis mascotas; main points: sus nombres; conclusion", "A", "Responde al propósito de informar sobre la actividad.")],
    [
        ("¿Cuál es el primer paso del proceso de escritura?", "Organizar las ideas", "Se planifica antes de redactar."),
        ("¿Cuáles son las tres partes de un esquema?", "Introduction, main points y conclusion", "Introducción, puntos principales y conclusión."),
        ("¿Qué se hace con las ideas que están fuera del tema?", "Se eliminan", "No aportan al propósito."),
    ],
    task("Lee este encargo: tu curso debe publicar un texto de opinión con el título «Our school needs a garden». Escribe en una hoja el propósito, una lluvia de ideas con al menos seis ideas, marca con una cruz las que están fuera del tema y arma un esquema con introduction, tres main points y conclusion. Todavía no escribas el texto completo.", "Purpose: express an opinion. Ideas: plants make the yard beautiful; students learn about nature; the garden is a quiet place; I like cats (x); we can grow tomatoes; the yard is empty. Outline: Introduction: I think our school needs a garden. Points: it is beautiful; students learn; it is quiet. Conclusion: a garden helps everyone.", ["indica el propósito correcto", "elimina las ideas fuera del tema", "el esquema tiene introducción, tres puntos y conclusión"], ["hoja con propósito, ideas y esquema"], ["empezar a redactar sin esquema", "dejar ideas fuera del tema"], "Cuéntale tu esquema a una persona de tu casa y pregunta qué punto le convence más."),
    "Haz una lluvia de ideas de ocho ideas sobre tu deporte favorito y marca dos que podrías eliminar.",
    "Arma dos esquemas distintos para el mismo tema, uno para informar y otro para narrar.",
)

# ================================================================ clase 2: redactar
lesson(
    OA13, 2,
    "Los esquemas y los textos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a redactar un primer borrador a partir de un esquema, con conectores y estructuras que ya conozco. Sirve para convertir las ideas en un texto continuo, sin preocuparme aún de la perfección.",
    ["Sé hacer un esquema con introducción, puntos y conclusión.", "Conozco conectores como because, also y finally."],
    [
        "El borrador (draft) es la primera versión completa del texto. Se escribe siguiendo el esquema: un párrafo corto por cada punto principal. Cada párrafo empieza con una oración principal (topic sentence) que dice de qué trata. En esta etapa lo importante es poner las ideas por escrito; los errores pequeños se arreglan después.",
        "Los conectores ayudan a que el texto fluya. Para ordenar: First, Then, Finally. Para sumar razones: Also. Para dar una razón: because. Para dar un ejemplo: For example. Para dar el resultado: so. En un texto de opinión usa I think o In my opinion, y da una razón con because. En un texto que narra usa el pasado simple y la secuencia. Usa solo palabras y estructuras que ya conoces; si dudas de una palabra, busca otra más simple.",
        "Ejemplo de borrador de opinión: «In my opinion, we need more bins. First, there is only one bin in the yard. Also, many students throw paper on the floor. Finally, bins keep the yard clean». Observa: una opinión en la primera oración, tres razones con conectores y una idea final.",
    ],
    [("draft", "borrador: primera versión completa"), ("topic sentence", "oración principal: dice de qué trata el párrafo"), ("In my opinion / I think", "en mi opinión / creo que"), ("because", "porque (da una razón)"), ("for example", "por ejemplo"), ("first, then, finally", "primero, luego, finalmente"), ("also", "además"), ("so", "así que (resultado)")],
    [
        ("Unir una opinión y una razón", "Une con because: «We need more bins.» «The yard is dirty.»", ["La segunda oración es la razón.", "Se une con because, sin punto.", "Queda We need more bins because the yard is dirty."], "We need more bins because the yard is dirty."),
        ("Elegir la oración principal", "Párrafo sobre los viernes de reciclaje. ¿Qué oración sirve de oración principal? A) On Fridays, our school collects bottles. B) Blue is a nice colour.", ["La oración principal dice de qué trata el párrafo.", "A habla de los viernes y el reciclaje.", "B no se relaciona con el tema."], "A"),
    ],
    [
        ("Repetir la misma idea con otras palabras en tres oraciones seguidas.", "No agrega información nueva y el texto se hace pesado.", "Cada oración debe aportar una razón o un dato distinto."),
        ("Escribir una opinión sin ninguna razón.", "El lector no sabe por qué piensas eso.", "Agrega because y una razón."),
    ],
    [
        ("Un borrador (draft) es A) la primera versión completa B) la versión final", "A", "Se escribe primero y se mejora en los pasos siguientes."),
        ("Completa: «I think uniforms are useful ___ they save time.» A) because B) but", "A", "Because introduce la razón de la opinión."),
        ("Completa: «Our school has recycling boxes in many places. ___, there are three boxes in the gym.» A) For example B) Because", "A", "For example introduce un ejemplo del dato anterior."),
    ],
    [
        ("Borrador: «In my opinion, we need more bins. First, there is only one bin in the yard. Also, many students throw paper on the floor. Finally, bins keep the yard clean.» Copia la oración que da la opinión.", "In my opinion, we need more bins.", "Es la única oración que dice lo que piensa el autor."),
        ("Borrador: «In my opinion, we need more bins. First, there is only one bin. Also, many students throw paper on the floor. Finally, bins keep the yard clean.» ¿Qué conector suma otra razón? A) Also B) Finally", "A", "Also significa además y suma una razón más."),
        ("¿Qué oración sirve de oración principal de un párrafo sobre cómo lavar botellas? A) Bottles are washed on Fridays. B) The school has a yard.", "A", "Dice el tema exacto del párrafo."),
    ],
    [
        ("Completa con el pasado: «Last Saturday, we ___ (go) to the park.»", "went", "Go es irregular y su pasado es went."),
        ("Ordena las palabras: think / I / library / is / the / useful", "I think the library is useful.", "I think va primero y luego se escribe la opinión."),
        ("Une con so: «The bin is full.» «Students leave the paper on the floor.»", "The bin is full, so students leave the paper on the floor.", "So muestra el resultado de la primera idea."),
    ],
    [
        ("¿Qué oración da una razón? A) I think recess should be longer because we need time to rest. B) I think recess should be longer.", "A", "Because introduce la razón; la otra solo da la opinión."),
        ("¿Qué borrador narra mejor? A) First, we took the bus. Then we arrived at the museum. Finally, we ate lunch. B) We ate lunch. Then we took the bus. First, we arrived at the museum.", "A", "Tiene los hechos ordenados con conectores de secuencia."),
    ],
    [
        ("Completa con First, Also o Finally en orden: «I think we should have a school garden. ___, plants make the yard beautiful. ___, students learn about nature. ___, a garden is a good place to rest.»", "First, Also, Finally", "First abre, Also suma y Finally cierra."),
        ("Corrige el verbo: «In my opinion, we needs more time at recess.»", "In my opinion, we need more time at recess.", "Con we se usa need, sin s."),
    ],
    [("Un compañero escribió: «I think field trips are good. They are good. Good.» ¿Qué comentario lo ayuda más? A) Agrega una razón con because B) Agrega fotos", "A", "Le faltan razones que expliquen por qué son buenas.")],
    [
        ("¿Qué conector sirve para dar una razón?", "because", "Because introduce una razón."),
        ("¿Qué dice la oración principal de un párrafo?", "De qué trata", "Presenta el tema del párrafo."),
        ("¿Qué se escribe en un borrador?", "Todas las ideas del esquema", "Se redactan siguiendo el esquema."),
    ],
    task("Lee este encargo: con el esquema del texto «Our school needs a garden» (introducción: I think our school needs a garden; puntos: es bonita, los estudiantes aprenden, es un lugar tranquilo; conclusión: a garden helps everyone), redacta en una hoja un borrador de cinco a siete oraciones. Usa I think o In my opinion, tres razones con First, Also y Finally, y because al menos una vez.", "In my opinion, our school needs a garden. First, a garden makes the yard beautiful. Also, students learn about plants. Finally, it is a quiet place because there are many trees. A garden helps everyone.", ["tiene una opinión clara al comienzo", "usa conectores First, Also y Finally", "da razones con because o con ejemplos"], ["hoja con el borrador"], ["escribir una opinión sin razones", "repetir la misma idea"], "Lee tu borrador a una persona de tu casa y pregunta si se entiende tu opinión."),
    "Escribe un borrador de cuatro oraciones que narre lo que hiciste ayer, usando First, Then y Finally.",
    "Escribe dos oraciones principales distintas para un mismo párrafo y elige la mejor.",
)

# ================================================================ clase 3: revisar
lesson(
    OA13, 3,
    "Los borradores y las listas de revisión escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a revisar un borrador: mejorar las ideas, el orden y la claridad. Sirve para que el texto cumpla su propósito antes de arreglar la ortografía.",
    ["Sé escribir un borrador con opinión, razones y conectores.", "Conozco la diferencia entre una idea principal y un detalle."],
    [
        "Revisar (revise) es mejorar el contenido del borrador: que tenga un propósito claro, ideas suficientes, buen orden y conectores. Editar (edit) es otra cosa y viene después: corregir ortografía, mayúsculas y puntuación. Si mezclas ambos pasos, corriges comas en oraciones que luego vas a eliminar.",
        "Usa una lista de revisión (checklist) con preguntas: 1) ¿El propósito es claro? 2) ¿Hay razones o datos que apoyen la idea principal? 3) ¿Las ideas están en orden lógico? 4) ¿Hay conectores? 5) ¿Hay alguna oración fuera del tema? Cambia lo que haga falta: agrega una razón, elimina una oración que no va, reordena y reemplaza palabras repetidas.",
        "También sirve la opinión de un compañero (peer feedback). Un buen comentario es concreto: «Add a reason after your first sentence». Un comentario como «Nice» no ayuda a mejorar. Al recibirlo, decide qué cambios hacer; no tienes que aceptarlos todos, pero sí pensar en cada uno.",
    ],
    [("revise", "revisar: mejorar ideas, orden y claridad"), ("edit", "editar: corregir ortografía, mayúsculas y puntuación"), ("checklist", "lista de revisión"), ("add", "agregar"), ("delete", "eliminar"), ("reorder", "reordenar"), ("peer feedback", "comentarios de un compañero"), ("detail", "detalle: dato concreto que apoya una idea")],
    [
        ("Detectar una oración fuera del tema", "Borrador: «Our school has a garden. Tomatoes grow there. My uncle has a truck.» ¿Qué oración se elimina al revisar?", ["El tema es el jardín del colegio.", "Las dos primeras hablan del jardín.", "La tercera habla del camión del tío."], "My uncle has a truck."),
        ("Ordenar un párrafo", "Ordena los hechos: a) Finally, we ate lunch. b) First, we arrived at the zoo. c) Then we saw the penguins. Escribe las letras en orden.", ["First va primero.", "Then va en medio.", "Finally cierra."], "b, c, a"),
    ],
    [
        ("Revisar corrigiendo solo comas y ortografía.", "Eso es editar, y las ideas siguen sin mejorar.", "Primero mejora ideas y orden; después edita."),
        ("Aceptar un comentario como «Nice» y no cambiar nada.", "No dice qué mejorar.", "Pide un comentario concreto, como «add a reason»."),
    ],
    [
        ("Revisar es A) mejorar ideas, orden y claridad B) publicar el texto", "A", "Revisar trata del contenido; publicar es el último paso."),
        ("Borrador: «The garden has six boxes of tomatoes.» «Gardens exist.» ¿Qué oración agrega un detalle concreto? Copia la oración.", "The garden has six boxes of tomatoes.", "Dice un número y un objeto que se pueden comprobar."),
        ("¿Qué comentario ayuda más? A) Add a reason after your first sentence. B) Nice.", "A", "Dice exactamente qué cambiar."),
    ],
    [
        ("Lista: 1) propósito claro, 2) razones que apoyen la idea, 3) orden lógico. Borrador: «I think we need more bins. Bins are good.» ¿Qué punto de la lista falla más claramente? Responde con su número.", "2", "No da razones que apoyen la idea."),
        ("¿Qué cambio mejora la oración «It is good»? A) The garden is good because students learn about plants. B) It is very very good.", "A", "Agrega una razón y deja claro de qué se habla."),
        ("Texto: «The park is nice. The park has nice trees. The park has nice benches.» ¿Qué versión evita repetir? A) The park is nice. It has tall trees and wooden benches. B) The park is nice. The park is nice.", "A", "Reemplaza la repetición por it y suma detalles."),
    ],
    [
        ("Une con so: «The bin is full.» «Students throw paper on the floor.»", "The bin is full, so students throw paper on the floor.", "So muestra el resultado."),
        ("Agrega el conector para sumar una razón: «Plants make the yard beautiful. ___, students learn about nature.» Opciones: Also / Because.", "Also", "Also significa además y suma una razón."),
        ("En el borrador «Our school needs a garden. Our cat is brown. Plants make the yard beautiful. Students learn about nature.», ¿qué oración sobra? Copia la oración.", "Our cat is brown.", "Es la única que no se relaciona con el jardín."),
    ],
    [
        ("Ana cambió «We need bins» por «We need more bins because the yard is dirty». ¿Qué hizo? A) Revisar B) Editar", "A", "Agregó una razón, es decir, mejoró el contenido."),
        ("Tomás cambió «becouse» por «because». ¿Qué hizo? A) Revisar B) Editar", "B", "Corrigió la ortografía de una palabra."),
    ],
    [
        ("Un compañero te dice: «Your text has a good idea, but it does not say when and where the trip happened». ¿Qué cambio haces? Responde en español.", "Agregar cuándo y dónde fue el viaje", "El comentario pide dos datos concretos."),
        ("Reordena el borrador de un paseo y escribe las letras en orden. a) First, we arrived at the museum. b) Finally, we saw the dinosaurs. c) Then we bought tickets.", "a, c, b", "Se llega, se compran los boletos y al final se ven los dinosaurios."),
    ],
    [("En un taller de escritura recibes tres comentarios sobre tu texto de un paseo: 1) Good. 2) Add when and where the trip happened. 3) Great job. ¿Cuál te ayuda a mejorar el texto? A) El comentario 2 B) El comentario 1 C) El comentario 3", "A", "Es el único concreto, que dice qué agregar.")],
    [
        ("¿Qué se mejora al revisar?", "Ideas, orden y claridad", "No se corrige solo la ortografía."),
        ("¿Qué paso viene después de revisar?", "Editar", "Se corrigen ortografía y puntuación."),
        ("¿Cómo es un buen comentario de un compañero?", "Concreto", "Dice qué cambiar, como add a reason."),
    ],
    task("Lee este encargo: revisa en una hoja este borrador. «I think we need a school library. Libraries are good. My dog is brown. We can read books. Also we can study.» Aplica la lista de revisión: elimina una oración fuera del tema, agrega una razón con because y reordena si hace falta. Reescribe el texto mejorado y anota qué cambios hiciste.", "I think we need a school library. We can read books there. Also, we can study in a quiet place because there is no noise. A library helps everyone. Changes: deleted the dog sentence; added a reason with because.", ["elimina la oración fuera del tema", "agrega una razón con because", "anota los cambios que hizo"], ["hoja con el texto mejorado y la lista de cambios"], ["corregir solo la ortografía", "borrar ideas útiles"], "Pide a una persona de tu casa que lea las dos versiones y diga cuál se entiende mejor."),
    "Escribe tres comentarios concretos que le harías a un borrador sobre las vacaciones.",
    "Revisa un texto antiguo tuyo con la lista de cinco preguntas y anota qué cambiarías.",
)
