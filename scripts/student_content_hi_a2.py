"""Material del estudiante de 1.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (identidad personal) y OA 04 (historia de la familia)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA3, OA4 = "HI01 OA 03", "HI01 OA 04"

# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Lápiz y papel. Las fichas de niños imaginarios están escritas en cada ejercicio. No uses datos privados en ninguna ficha.",
    use="Aprenderé a escribir información segura sobre mí, como mi nombre y mis gustos, y a no compartir datos privados. Sirve para presentarme sin riesgos.",
    prior=["Sé decir mi nombre.", "Sé que algunas cosas no se cuentan a desconocidos."],
    explain=[
        "Tu nombre es parte de quién eres. En Chile las personas suelen llevar uno o más nombres y dos apellidos. Por ejemplo: Sofía Rojas Pinto. Sofía es el nombre; Rojas y Pinto son los apellidos, que vienen de tu familia.",
        "Otros datos que hablan de ti son tu fecha de nacimiento (el día, mes y año en que naciste) y lo que te gusta: tu comida, tu color, tu juego favorito. Todos son parte de tu identidad, es decir, de lo que te hace ser tú.",
        "No todo se comparte con todos. Tu dirección, tu teléfono y tus contraseñas son datos privados: solo las personas de confianza de tu familia deben saberlos. En una ficha del curso escribe solo cosas seguras, como tu primer nombre, tu color y tu comida favorita.",
    ],
    vocab=[("identidad", "lo que me hace ser yo"), ("apellido", "parte del nombre que viene de la familia"), ("fecha de nacimiento", "día, mes y año en que naciste"), ("dato privado", "información que solo sabe mi familia, como la dirección"), ("gusto", "algo que me agrada")],
    worked=[
        {"title": "Partes de un nombre", "problem": "En la ficha dice: Mateo Soto Vega. ¿Cuál es el nombre y cuáles son los apellidos?", "steps": ["El primer nombre es la primera palabra: Mateo.", "Las otras dos palabras son los apellidos: Soto y Vega."], "answer": "Nombre Mateo; apellidos Soto y Vega"},
        {"title": "Dato seguro o privado", "problem": "¿Es seguro escribir en una ficha del curso «mi comida favorita es el pastel de choclo»?", "steps": ["Una comida favorita es un gusto.", "No sirve para encontrar a la persona ni para entrar a su casa."], "answer": "Sí, es seguro compartirlo"},
    ],
    mistakes=[
        {"wrong": "Escribir la dirección de la casa en una ficha del curso.", "why": "Se piensa que ese dato también muestra quién soy.", "fix": "Guarda la dirección: solo la saben tu familia y personas de confianza."},
        {"wrong": "Creer que mi nombre y el de otra persona son lo mismo si empiezan igual.", "why": "No se mira el apellido.", "fix": "Lee el nombre completo: los apellidos distinguen a las personas."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuál es el primer nombre en «Sofía Rojas Pinto»?", "Sofía", "El nombre es la primera palabra."),
            ex("¿Cuántos apellidos tiene «Mateo Soto Vega»?", "2", "Soto y Vega son los apellidos."),
            ex("Un compañero dice que su color favorito es el verde. ¿Es un gusto?", "Sí", "Un color que agrada es un gusto."),
        ],
        "understand": [
            ex("¿Qué dice la fecha de nacimiento de una persona?", "El día, mes y año en que nació", "Cuenta cuándo empezó su vida."),
            ex("¿Por qué la dirección de tu casa es un dato privado?", "Porque solo la deben saber tu familia y personas de confianza", "Compartirla con desconocidos puede ser peligroso."),
            ex("¿Qué es la identidad de una persona?", "Lo que la hace ser quien es", "Incluye su nombre, sus gustos y su historia."),
        ],
        "apply": [
            ex("Escribe S si es seguro compartir con el curso o P si es privado: «mi animal favorito es el gato».", "S", "Un animal favorito es un gusto que no pone en riesgo a nadie."),
            ex("Escribe S si es seguro compartir con el curso o P si es privado: «mi número de teléfono es el de la casa».", "P", "El teléfono es un dato privado."),
            ex("Escribe S si es seguro compartir con el curso o P si es privado: «la contraseña de la tablet de mi casa».", "P", "Las contraseñas no se comparten con nadie fuera de la familia."),
        ],
        "reason": [
            ex("Un niño escribe en su ficha: «Me llamo Tomás, me gusta el fútbol y vivo en esta dirección completa de calle y número». ¿Qué parte no debería compartir?", "la dirección", "La dirección es un dato privado y puede ser peligrosa."),
            ex("Dos niñas se llaman Sofía; una es Sofía Rojas Pinto y la otra Sofía Rojas Vera. ¿Qué parte del nombre las distingue?", "el segundo apellido", "Tienen el mismo nombre y primer apellido, pero Pinto y Vera son distintos."),
        ],
        "challenge": [
            ex("Marta Reyes Mora nació el 29 de febrero de 2020, un año bisiesto. ¿Cuántos días tuvo febrero de ese año?", "29", "En un año bisiesto febrero tiene 29 días."),
            ex("Valentina Díaz Soto nació el 3 de octubre de 2018. ¿Cuál es su segundo apellido y en qué mes nació?", "Soto; octubre", "El segundo apellido es el último y el mes está escrito en la fecha."),
        ],
    },
    context=[ex("La profesora arma un diario mural y pide a cada niño: nombre, comida favorita y animal favorito. Un niño quiere agregar el teléfono de su casa. ¿Debe hacerlo?", "No; el teléfono es un dato privado", "La profesora no pidió el teléfono y es información de riesgo.")],
    selfcheck=[
        ex("¿Qué es un apellido?", "La parte del nombre que viene de la familia", "Se hereda de familiares."),
        ex("Escribe S si es seguro compartir con el curso o P si es privado: «mi juego favorito es la rayuela».", "S", "Un juego favorito es un gusto seguro."),
        ex("¿Quién puede saber tu dirección: cualquier persona o solo personas de confianza?", "solo personas de confianza", "La dirección es un dato privado."),
    ],
    open_task=task("Haz una ficha de identidad con cuatro datos seguros: tu primer nombre, tu mes de cumpleaños, tu color favorito y tu juego o comida favorita. Elige entre estas opciones: color (rojo, azul, verde, amarillo), juego (pelota, rayuela, bicicleta, dibujar), comida (empanada, arroz con pollo, pan con palta, fruta). No escribas dirección ni teléfono.", "Me llamo Sofía. Mi cumpleaños es en junio. Mi color favorito es el azul. Mi juego favorito es la rayuela.", ["cuatro datos", "solo datos seguros", "datos escritos con claridad"], ["ficha con cuatro datos"], ["incluir la dirección", "incluir el teléfono"], "Pide que explique por qué no escribió su dirección en la ficha."),
    reinforce="Cuenta a tu familia qué dato de tu ficha es un gusto y cuál es tu mes de cumpleaños.",
    extend="Escribe una lista de tres datos que no compartirías con desconocidos y por qué.",
)

register(
    OA3, 2,
    materials="Lápiz y papel. Los relatos de niños imaginarios y los lugares de Chile están escritos en cada ejercicio.",
    use="Aprenderé a hablar de dónde viene una persona y de las historias de su familia sin suponer. Sirve para respetar que cada familia tiene una historia distinta.",
    prior=["Sé que hay lugares distintos en Chile.", "Sé qué es una familia."],
    explain=[
        "El lugar de procedencia es donde nació una persona o donde vivió antes. Los lugares pueden ser una ciudad, un pueblo, una región o incluso otro país. Una persona puede venir de un lugar y su familia de otro.",
        "Las ascendencias son las familias de las que venimos: abuelos, bisabuelos y antepasados. En Chile conviven personas con ascendencias muy distintas: de pueblos originarios como el mapuche, el aymara y el rapa nui, y de familias que llegaron desde otras partes de América, Europa, Asia y África.",
        "No debemos suponer de dónde viene una persona por su cara, su apellido o cómo habla. Para saberlo se pregunta con respeto: «¿Quieres contarnos de dónde viene tu familia?». Cada persona decide qué quiere contar.",
    ],
    vocab=[("procedencia", "lugar de donde viene una persona"), ("ascendencia", "las familias de las que vengo"), ("región", "una de las partes en que se divide Chile; hay 16"), ("suponer", "creer algo sin preguntar ni saberlo"), ("pueblo originario", "pueblo que ya vivía aquí antes de la llegada de los europeos")],
    worked=[
        {"title": "Lugares de Chile de norte a sur", "problem": "Arica está en el extremo norte de Chile y Punta Arenas en el sur. Valparaíso está en el centro. Ordena de norte a sur: Punta Arenas, Valparaíso, Arica.", "steps": ["El norte está primero: Arica.", "Luego el centro: Valparaíso.", "Al final el sur: Punta Arenas."], "answer": "Arica, Valparaíso, Punta Arenas"},
        {"title": "No suponer", "problem": "Luis dice: «Tu apellido es extranjero, así que no eres de Chile». ¿Es correcta su frase?", "steps": ["El apellido no dice dónde nació una persona.", "Hay que preguntar con respeto."], "answer": "No, está suponiendo"},
    ],
    mistakes=[
        {"wrong": "Decir de dónde viene un compañero por su apariencia.", "why": "Se piensa que las personas de un lugar se ven todas iguales.", "fix": "Pregunta con respeto y acepta lo que cuente."},
        {"wrong": "Creer que todos nacieron en la misma ciudad que su familia.", "why": "Se olvida que las personas se mudan.", "fix": "Distingue dónde nació cada persona y de dónde viene su familia."},
    ],
    tiers={
        "recovery": [
            ex("Mateo nació en Arica. ¿Cuál es su lugar de nacimiento?", "Arica", "Es donde nació."),
            ex("¿Qué palabra significa «lugar de donde viene una persona»: procedencia o gusto?", "procedencia", "La procedencia habla del lugar de origen."),
            ex("Si Camila cuenta que sus abuelos vinieron de Perú, ¿esa información es sobre procedencia o sobre ascendencia?", "ascendencia", "Habla de las familias de las que viene."),
        ],
        "understand": [
            ex("¿Cuántas regiones tiene Chile?", "16", "Chile se divide en 16 regiones."),
            ex("¿Por qué no debemos suponer de dónde viene alguien por su apariencia?", "Porque la apariencia no dice dónde nació ni de dónde viene su familia", "Se puede equivocar y ofender a la persona."),
            ex("Nombra dos pueblos originarios de Chile.", "mapuche y aymara", "Son dos de los pueblos originarios de Chile (también está el rapa nui)."),
        ],
        "apply": [
            ex("Arica está al norte, Valparaíso al centro y Punta Arenas al sur. Ordena de norte a sur: Valparaíso, Arica, Punta Arenas.", "Arica, Valparaíso, Punta Arenas", "El norte va primero y el sur último."),
            ex("Ana nació en Puerto Montt, en el sur. Su abuela nació en Santiago, en el centro. ¿Quién nació más al sur?", "Ana", "Puerto Montt está más al sur que Santiago."),
            ex("Ordena las personas por lugar de nacimiento de norte a sur: Luz (Antofagasta, norte), Ema (Punta Arenas, extremo sur), Iván (Concepción, sur-centro).", "Luz, Iván, Ema", "Antofagasta está más al norte; Punta Arenas, más al sur."),
        ],
        "reason": [
            ex("Un niño llega a la escuela y su compañero dice: «Seguro eres de otro país». El niño nació en Temuco. ¿Qué hizo mal el compañero?", "Supuso sin preguntar", "No debemos creer algo sin saberlo."),
            ex("Lucía nació en Santiago, pero su mamá nació en La Paz y su papá en Valdivia. ¿Cuál es el lugar de nacimiento de Lucía?", "Santiago", "El lugar de nacimiento es donde nació ella, no donde nacieron sus padres."),
        ],
        "challenge": [
            ex("Tres compañeros hablan: Nico dice que su familia llegó de Italia, Ema que su abuela es mapuche y Caro que sus abuelos son de Chiloé. ¿Tienen todos las mismas ascendencias?", "No; cada familia tiene una historia distinta", "Los tres relatos hablan de lugares y pueblos distintos."),
            ex("Un niño dice «No sé de dónde viene mi abuelo». ¿Debe inventarlo para completar su ficha?", "No; puede preguntar a su familia o escribir que no lo sabe", "Inventar daría datos falsos."),
        ],
    },
    context=[ex("Ema cuenta: «Yo nací en Punta Arenas, mi papá nació en Iquique y mi mamá en Osorno». ¿Qué lugar es la procedencia de Ema?", "Punta Arenas", "Es el lugar donde nació ella.")],
    selfcheck=[
        ex("¿Qué es una ascendencia?", "Las familias de las que vengo", "Habla de los antepasados."),
        ex("¿Se puede saber de dónde viene alguien mirando su cara?", "No", "Hay que preguntarle con respeto."),
        ex("En Chile, ¿Arica está en el norte o en el sur?", "en el norte", "Arica es una ciudad del extremo norte."),
    ],
    open_task=task("Dibuja un mapa muy simple de Chile como una línea larga vertical, con el norte arriba y el sur abajo. Marca con puntos tres ciudades: Arica (arriba), Valparaíso (en el medio) y Punta Arenas (abajo). Escribe al lado de cada punto un lugar de procedencia que podrías contar: «Mi familia viene de…». Puedes elegir de esta lista: Arica, Valparaíso, Punta Arenas, Chiloé, Temuco, otro país.", "Línea vertical con Arica arriba, Valparaíso en el medio y Punta Arenas abajo. Al lado de Valparaíso: «Mi familia viene de Valparaíso».", ["línea con norte arriba", "tres ciudades en orden de norte a sur", "una procedencia escrita"], ["mapa dibujado con tres puntos"], ["poner el sur arriba", "suponer la procedencia de otra persona"], "Pide que cuente por qué eligió ese lugar sin suponer nada de otros."),
    reinforce="Pregunta a un adulto de tu casa dónde nació y escribe el nombre del lugar.",
    extend="Averigua de qué ciudad o pueblo vienen tus abuelos y márcalo en tu línea de Chile.",
)

register(
    OA3, 3,
    materials="Lápiz y papel. Las tablas de gustos de dos niños imaginarios están escritas en cada ejercicio.",
    use="Aprenderé a comparar mis gustos, intereses y amistades con los de otra persona y a ver semejanzas y diferencias. Sirve para respetar que somos distintos.",
    prior=["Sé qué es un gusto.", "Sé contar hasta 10."],
    explain=[
        "Los gustos son cosas que nos agradan, como una comida o un color. Los intereses son temas que queremos conocer más, como los animales o los autos. Los vínculos son las relaciones con otras personas, como los amigos y la familia.",
        "Dos personas pueden tener gustos parecidos y también distintos. Al comparar usamos dos palabras: semejanza (en lo que coinciden) y diferencia (en lo que no coinciden). Ana y Beto pueden tener el mismo juego favorito, pero distinta comida favorita.",
        "Comparar no sirve para decir quién está mejor, sino para conocernos. Que algo sea distinto no es malo. Las amistades suelen nacer entre quienes tienen gustos parecidos, pero también entre quienes aprenden algo nuevo del otro.",
    ],
    vocab=[("interés", "tema que quiero conocer más"), ("vínculo", "relación con otra persona"), ("semejanza", "algo en lo que dos personas coinciden"), ("diferencia", "algo en lo que no coinciden"), ("comparar", "mirar dos cosas para ver cómo son")],
    worked=[
        {"title": "Semejanza", "problem": "Ana: juego pelota, comida empanada, animal perro. Beto: juego pelota, comida arroz, animal gato. ¿En qué se parecen?", "steps": ["Miro cada gusto de los dos.", "El juego es el mismo: pelota."], "answer": "Les gusta el mismo juego: la pelota"},
        {"title": "Diferencia", "problem": "Con las mismas fichas de Ana y Beto, ¿en qué son diferentes?", "steps": ["Comparo la comida: empanada y arroz son distintas.", "Comparo el animal: perro y gato son distintos."], "answer": "Se diferencian en la comida y en el animal"},
    ],
    mistakes=[
        {"wrong": "Decir que un gusto está mal porque no es igual al mío.", "why": "Se compara para elegir al mejor.", "fix": "Los gustos distintos no son buenos ni malos: son distintos."},
        {"wrong": "Mezclar semejanzas con diferencias en la lista.", "why": "No se revisa uno por uno.", "fix": "Mira cada gusto por separado: ¿es igual o es distinto?"},
    ],
    tiers={
        "recovery": [
            ex("Ana: color azul. Beto: color azul. ¿Es una semejanza o una diferencia?", "semejanza", "Los dos tienen el mismo color favorito."),
            ex("Ana: animal perro. Beto: animal gato. ¿Es una semejanza o una diferencia?", "diferencia", "Los animales son distintos."),
            ex("¿Qué es un vínculo: una relación con otra persona o un color?", "una relación con otra persona", "Los vínculos son relaciones, como una amistad."),
        ],
        "understand": [
            ex("¿Cuál palabra significa «en lo que coinciden»: semejanza o diferencia?", "semejanza", "Semejanza es lo parecido o igual."),
            ex("¿Para qué comparamos nuestros gustos con los de otros?", "Para conocernos y respetarnos", "No es para decir quién es mejor."),
            ex("Explica con tus palabras qué es un interés.", "Un tema que quiero conocer más", "Es algo que nos llama la atención."),
        ],
        "apply": [
            ex("Tabla. Ana: juego pelota, comida empanada, animal perro. Beto: juego pelota, comida arroz, animal gato. ¿Cuántas semejanzas hay?", "1", "Solo el juego es igual."),
            ex("Tabla. Ana: juego pelota, comida empanada, animal perro. Beto: juego pelota, comida arroz, animal gato. ¿Cuántas diferencias hay?", "2", "La comida y el animal son distintos."),
            ex("Tabla. Lía: color rojo, comida pizza, animal caballo. Ema: color rojo, comida pizza, animal caballo. ¿En cuántos gustos coinciden?", "3", "Los tres gustos son iguales."),
        ],
        "reason": [
            ex("Pedro dice: «A mi amigo le gusta el pescado y a mí no, así que su gusto es malo». ¿Tiene razón?", "No; solo es un gusto distinto", "Los gustos distintos no son malos."),
            ex("Dos niñas tienen el mismo juego favorito y distinta comida. ¿Pueden ser amigas?", "Sí", "Un gusto en común y una diferencia no impiden la amistad."),
        ],
        "challenge": [
            ex("Tres niños. Mía: color verde, juego cuerda. Noa: color verde, juego pelota. Tito: color amarillo, juego pelota. ¿Quién comparte el color con Mía y quién comparte el juego con Noa?", "Noa comparte el color con Mía; Tito comparte el juego con Noa", "Mía y Noa tienen verde; Noa y Tito tienen pelota."),
            ex("Dos niños tienen 4 gustos: color, comida, juego y animal. Coinciden en 3. ¿En cuántos son diferentes?", "1", "Si coinciden en 3 de 4, solo uno es distinto."),
        ],
    },
    context=[ex("Un grupo de cuatro amigos: Sol y Leo aman los dinosaurios, Ema y Teo los aviones. ¿Qué interés comparten Sol y Leo?", "los dinosaurios", "Es el interés que aparece en ambos.")],
    selfcheck=[
        ex("¿Qué palabra usamos para lo que no coincide: semejanza o diferencia?", "diferencia", "Diferencia es lo que no es igual."),
        ex("Ana: color azul. Beto: color rojo. ¿Qué hay entre los dos colores?", "una diferencia", "Los colores son distintos."),
        ex("¿Un gusto distinto es un gusto malo?", "No", "Solo es distinto."),
    ],
    open_task=task("Compara tus gustos con los de este niño imaginario, Beto: juego pelota, comida arroz, animal gato, color azul. Escribe una tabla de dos columnas (tú y Beto) y marca una semejanza y una diferencia. Para ti puedes elegir entre juegos (pelota, rayuela, bicicleta), comidas (arroz, empanada, fruta), animales (gato, perro, pez) y colores (azul, rojo, verde).", "Yo: juego rayuela, comida empanada, animal perro, color azul. Beto: pelota, arroz, gato, azul. Semejanza: color azul. Diferencia: mi juego es rayuela y el suyo pelota.", ["tabla de dos columnas", "una semejanza", "una diferencia"], ["tabla escrita con las dos columnas"], ["decir que un gusto es mejor", "no marcar semejanzas ni diferencias"], "Pide que lea una semejanza y una diferencia en voz alta."),
    reinforce="Pregunta a un familiar su comida favorita y dime si es igual o distinta a la tuya.",
    extend="Haz una tabla comparando tus gustos con los de dos personas de tu casa.",
)

register(
    OA3, 4,
    materials="Lápiz y papel. El retrato de ejemplo y las opciones de elementos están escritos en cada ejercicio.",
    use="Aprenderé a hacer un retrato de mi identidad con cinco elementos elegidos y a cuidar mi privacidad. Sirve para presentarme a otros de forma segura.",
    prior=["Sé qué es mi nombre y mi fecha de cumpleaños.", "Sé distinguir gustos y datos privados."],
    explain=[
        "Un retrato de identidad es un dibujo o texto con rasgos que dicen quién eres. Puede llevar tu nombre, tu mes de cumpleaños, algo que te gusta, algo que haces bien, una persona que quieres y un lugar importante para ti.",
        "Tú eliges qué mostrar. Puedes dejar fuera cosas que prefieres guardar. Elige solo datos seguros: un gusto, un juego, una cualidad como «soy ordenado» o «soy buena para dibujar». Los datos privados no van en el retrato.",
        "Un buen retrato es claro, tiene al menos cinco elementos y muestra que somos distintos. Cuando veas el retrato de otra persona, escucha con respeto y no te burles. Cada persona es única.",
    ],
    vocab=[("retrato", "dibujo o texto que muestra cómo es una persona"), ("rasgo", "característica de una persona"), ("cualidad", "algo bueno de cómo soy"), ("único", "que no hay otro igual"), ("privacidad", "derecho a guardar mis datos privados")],
    worked=[
        {"title": "Revisar un retrato", "problem": "Retrato de Sol: nombre Sol; cumpleaños en mayo; me gusta dibujar; mi mejor amiga es Ema; vivo en esta dirección completa. ¿Qué elemento debería quitar?", "steps": ["Reviso cada elemento.", "Nombre, mes, gusto y amiga son seguros.", "La dirección es un dato privado."], "answer": "Debe quitar la dirección"},
        {"title": "Contar elementos", "problem": "En el retrato de Sol quedan cuatro elementos seguros. ¿Cuántos más necesita para tener cinco?", "steps": ["Necesita 5 elementos.", "Tiene 4.", "5 − 4 = 1."], "answer": "Necesita uno más"},
    ],
    mistakes=[
        {"wrong": "Poner solo mi nombre y creer que el retrato está terminado.", "why": "No se piensa en otros rasgos.", "fix": "Agrega gustos, algo que haces bien, una persona que quieres y un lugar."},
        {"wrong": "Incluir información privada porque la pide un compañero.", "why": "Se siente presión.", "fix": "Tú decides: puedes decir «prefiero no contarlo»."},
    ],
    tiers={
        "recovery": [
            ex("¿Es un retrato de identidad un dibujo o texto que muestra quién eres?", "Sí", "Reúne rasgos de la persona."),
            ex("Mi color favorito es el rojo. ¿Es un rasgo seguro de poner en el retrato?", "Sí", "Un color favorito es un gusto sin riesgo."),
            ex("¿Cuántos elementos tiene un buen retrato según la clase: 1 o 5?", "5", "Se pide al menos cinco elementos."),
        ],
        "understand": [
            ex("¿Qué significa que cada persona es única?", "Que no hay otra persona igual", "Cada uno tiene gustos e historia distintos."),
            ex("¿Quién decide qué mostrar en tu retrato?", "Yo", "Cada persona elige."),
            ex("Explica qué es una cualidad.", "Algo bueno de cómo soy", "Por ejemplo: soy ordenada o soy generoso."),
        ],
        "apply": [
            ex("Retrato de Ema: nombre Ema; cumpleaños en julio; me gusta nadar; mi abuela me enseña a tejer; mi número de teléfono es el de mi casa. ¿Qué elemento debería quitar?", "el número de teléfono", "Es un dato privado."),
            ex("Retrato de Sol: nombre Sol; cumpleaños en mayo; me gusta dibujar; mi mejor amiga es Ema. ¿Cuántos elementos tiene?", "4", "Son nombre, cumpleaños, gusto y amiga."),
            ex("¿Cuál de estas palabras NO es una cualidad de una persona: generosa, valiente, martes, curioso?", "martes", "Martes es un día; las otras tres dicen cómo es una persona."),
        ],
        "reason": [
            ex("Luis dijo: «Tu retrato es feo porque dibujaste una cuerda y yo dibujé una pelota». ¿Qué debería recordar?", "Que cada persona es única y no hay gustos malos", "Los retratos son distintos porque somos distintos."),
            ex("Ana no quiere contar quiénes son sus abuelos en su retrato. ¿Debe obligarse?", "No; ella decide", "Cada persona elige qué mostrar."),
        ],
        "challenge": [
            ex("Un retrato trae: nombre, mes de nacimiento, comida favorita, mejor amigo y dirección de la casa. Quita el elemento que no es seguro. ¿Cuántos elementos quedan?", "4", "Se quita la dirección y quedan cuatro."),
            ex("Dos retratos tienen cinco elementos cada uno. Coinciden en 2. ¿Cuántos elementos son diferentes en cada retrato?", "3", "De los 5 elementos, 2 son iguales y 3 son distintos."),
        ],
    },
    context=[ex("Para la muestra del curso, cada niño pone su retrato en la pared. Tomás quiere agregar el nombre de su calle. La profesora le dice que no. ¿Qué dato podría agregar en su lugar?", "un gusto como su juego favorito", "Los gustos son datos seguros.")],
    selfcheck=[
        ex("¿Debe un retrato tener datos privados?", "No", "Los datos privados se guardan."),
        ex("¿Qué es un rasgo?", "Una característica de una persona", "Dice cómo es alguien."),
        ex("¿Cuántos elementos debe tener como mínimo un retrato completo?", "5", "Lo vimos en la clase."),
    ],
    open_task=task("Haz tu retrato de identidad con cinco elementos. Usa un cuadrado para cada uno: (1) tu primer nombre; (2) el mes de tu cumpleaños; (3) algo que te gusta (jugar, dibujar, bailar, leer); (4) una cosa que haces bien (ayudar, saltar, cantar, ordenar); (5) una persona que quieres. No pongas dirección ni teléfono.", "1) Sofía. 2) Junio. 3) Me gusta dibujar. 4) Soy buena para ayudar. 5) Quiero mucho a mi abuela.", ["cinco elementos", "todos seguros", "uno por cuadrado"], ["retrato con cinco cuadrados"], ["incluir dirección o teléfono", "tener menos de cinco elementos"], "Pide que cuente cuál de los cinco elementos es su favorito y por qué."),
    reinforce="Dibuja un sexto cuadrado con un lugar que te gusta mucho.",
    extend="Compara tu retrato con el de alguien de tu familia y marca una semejanza.",
)

# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Lápiz y papel. Las descripciones de familias imaginarias están escritas en cada ejercicio.",
    use="Aprenderé que hay muchos tipos de familia y que los integrantes pueden hacer distintas tareas sin estereotipos. Sirve para respetar a todas las familias.",
    prior=["Sé qué es una familia.", "Sé nombrar a personas de mi casa."],
    explain=[
        "Una familia es un grupo de personas que se cuidan y se quieren. Hay familias con mamá y papá, familias con una sola mamá o un solo papá, con abuelos, con tíos, con hermanos o con otras personas que cuidan a los niños. Todas son familias.",
        "Cada integrante tiene un rol, es decir, tareas que hace en la familia: cocinar, trabajar, cuidar, ordenar, jugar. Esas tareas no dependen de ser hombre o mujer. Un papá puede cocinar y una mamá puede manejar un camión.",
        "Cuando miramos una familia, miramos quiénes la forman y qué hace cada uno. No decimos que una familia es mejor porque tiene más personas. Lo importante es que se cuidan. Nunca suponemos cómo es una familia por su apellido o su casa.",
    ],
    vocab=[("familia", "personas que se cuidan y se quieren"), ("integrante", "persona que forma parte de la familia"), ("rol", "tarea que hace cada uno en la familia"), ("estereotipo", "idea fija sobre cómo debe ser alguien"), ("diverso", "distinto, con muchas formas")],
    worked=[
        {"title": "Contar integrantes", "problem": "La familia de Ana: su mamá, su abuela, su hermano Nico y Ana. ¿Cuántas personas son?", "steps": ["Cuento a cada una: mamá, abuela, Nico, Ana.", "Son cuatro."], "answer": "4 personas"},
        {"title": "Rol sin estereotipo", "problem": "Julián dice: «Mi papá cocina el almuerzo». ¿Está mal que un papá cocine?", "steps": ["Cocinar es una tarea de la familia.", "La puede hacer cualquier integrante."], "answer": "No, cualquier integrante puede cocinar"},
    ],
    mistakes=[
        {"wrong": "Decir que solo las mujeres cuidan a los niños.", "why": "Se repite una idea fija.", "fix": "Cualquier integrante puede cuidar: mamá, papá, abuelos o tíos."},
        {"wrong": "Pensar que una familia con una sola mamá no es una familia completa.", "why": "Se compara con un solo tipo de familia.", "fix": "Hay muchos tipos y todas se cuidan y se quieren."},
    ],
    tiers={
        "recovery": [
            arith("En la familia de Ana viven su mamá, su abuela, Nico y Ana. ¿Cuántas personas son?", "1+1+1+1", "Se cuenta a cada integrante."),
            ex("¿Una familia con una sola mamá y un hijo es una familia?", "Sí", "Se cuidan y se quieren."),
            ex("Julián dice que su abuelo cocina los domingos. ¿Cuál es el rol del abuelo?", "cocinar", "La tarea que hace es cocinar."),
        ],
        "understand": [
            ex("¿Qué es un rol en la familia?", "La tarea que hace cada integrante", "Cada persona ayuda de una manera."),
            ex("¿Por qué decimos que las familias son diversas?", "Porque hay familias distintas", "Cada una está formada de manera diferente."),
            ex("¿Qué es un estereotipo?", "Una idea fija sobre cómo debe ser alguien", "Por ejemplo: pensar que solo las mujeres cocinan."),
        ],
        "apply": [
            ex("Familia de Lía: papá, tío Raúl, Lía y su hermano. ¿Cuántos integrantes tiene?", "4", "Se cuenta papá, tío, Lía y el hermano."),
            ex("En la familia de Beto, su abuela maneja el auto y su papá cose los botones. ¿Alguna de esas tareas es solo de mujeres o solo de hombres?", "No", "Cualquier persona puede hacer cualquier tarea."),
            ex("Dos mamás y un niño viven juntos. ¿Cuántas personas forman esa familia?", "3", "Son dos mamás y un niño."),
        ],
        "reason": [
            ex("Pablo dijo: «Mi familia es mejor porque somos siete». ¿Tiene razón?", "No; ninguna familia es mejor por el número", "Lo importante es que se cuiden."),
            ex("Carla dice que su papá limpia la casa y su mamá arregla el auto. Un compañero se ríe. ¿Qué podría decirle la profesora?", "Que cada persona puede hacer cualquier tarea", "Los roles no dependen de ser hombre o mujer."),
        ],
        "challenge": [
            ex("En una casa viven la abuela, el abuelo, una tía, dos primos y Mía. ¿Cuántas personas son en total?", "6", "Abuela, abuelo, tía, dos primos y Mía suman 6."),
            ex("Una familia tiene 3 integrantes y otra 5. ¿Cuántos integrantes más tiene la segunda?", "2", "5 − 3 = 2."),
        ],
    },
    context=[ex("En el curso de Juana hay tres niños: Tomás vive con su mamá y su abuelo, Sol vive con sus dos papás y su hermano, y Mario vive con su tía. ¿Cuál es una familia?", "Las tres", "Todas se cuidan y se quieren.")],
    selfcheck=[
        ex("¿Qué es una familia?", "Personas que se cuidan y se quieren", "Eso las hace familia."),
        ex("¿Cualquier integrante puede cocinar?", "Sí", "No depende de ser hombre o mujer."),
        ex("¿Qué es un integrante?", "Una persona que forma parte de la familia", "Cada uno cuenta como integrante."),
    ],
    open_task=task("Dibuja a tu familia o a una familia imaginaria y escribe cuántas personas son. Al lado de cada persona anota una tarea que hace, eligiendo entre estas: cocinar, ordenar, trabajar, cuidar, jugar con los niños, arreglar cosas, leer cuentos.", "Mi familia son 4: mamá (trabajar), papá (cocinar), mi hermana (jugar) y yo (ordenar mis juguetes).", ["dibujo de las personas", "número correcto", "una tarea por persona"], ["dibujo con tareas escritas"], ["decir que una tarea es solo de hombres o de mujeres", "no escribir cuántos son"], "Pide que cuente en voz alta cuántas personas dibujó y qué hace cada una."),
    reinforce="Cuenta cuántas personas viven en tu casa y escribe una tarea de cada una.",
    extend="Escribe una tarea que le gustaría hacer a cada integrante y que antes no hacía.",
)

register(
    OA4, 2,
    materials="Lápiz y papel. Las preguntas y las situaciones están escritas en cada ejercicio.",
    use="Aprenderé a hacer preguntas respetuosas a un adulto para conocer la historia de mi familia. Sirve para investigar y aprender de las personas mayores.",
    prior=["Sé hacer preguntas simples.", "Sé escuchar a un adulto."],
    explain=[
        "Para saber sobre la historia de mi familia puedo preguntar a un adulto de confianza, como una abuela o un tío. Una buena pregunta empieza con una palabra como qué, quién, cuándo, dónde, cómo o por qué.",
        "Las preguntas que se responden solo con sí o no dan poca información. Es mejor preguntar «¿Cómo celebraban tu cumpleaños cuando eras niña?» que «¿Celebraban tu cumpleaños?». Así la persona cuenta una historia y yo aprendo más.",
        "Pregunta con respeto: pide permiso, saluda, escucha sin interrumpir y agradece. No hagas preguntas que puedan entristecer o que sean demasiado privadas. Si la persona no quiere contestar, se acepta.",
    ],
    vocab=[("pregunta", "lo que digo para saber algo"), ("entrevista", "conversación en que hago preguntas a alguien"), ("respeto", "tratar bien a los demás y escucharlos"), ("permiso", "decir primero «¿puedo preguntarte algo?»"), ("recuerdo", "algo del pasado que una persona tiene en la memoria")],
    worked=[
        {"title": "Elegir la mejor pregunta", "problem": "¿Cuál pregunta da más información: «¿Había juguetes?» o «¿Con qué jugabas cuando eras niño?»?", "steps": ["La primera se responde con sí o no.", "La segunda pide contar con qué jugaba."], "answer": "«¿Con qué jugabas cuando eras niño?»"},
        {"title": "Pregunta respetuosa", "problem": "¿Es respetuoso preguntar «¿Por qué eres tan viejo?»?", "steps": ["La pregunta puede ofender.", "Una pregunta respetuosa sería: «¿Qué recuerdas de tu infancia?»."], "answer": "No es respetuoso"},
    ],
    mistakes=[
        {"wrong": "Hacer solo preguntas de sí o no.", "why": "Se piensa que son más fáciles.", "fix": "Usa qué, quién, cuándo, dónde, cómo o por qué."},
        {"wrong": "Interrumpir cuando la persona está contando.", "why": "Se quiere hacer la siguiente pregunta.", "fix": "Escucha hasta el final y luego pregunta."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué palabra empieza «¿Cuándo naciste?»?", "cuándo", "Es la primera palabra de la pregunta."),
            ex("Escribe una palabra que sirva para empezar una pregunta, de estas: cuándo, hoy, rojo.", "cuándo", "Cuándo es una palabra de pregunta."),
            ex("¿A quién puedes entrevistar para conocer la historia de tu familia: a un adulto de confianza o a un desconocido?", "a un adulto de confianza", "Es seguro y respetuoso."),
        ],
        "understand": [
            ex("¿Por qué una pregunta de sí o no da poca información?", "Porque se responde con una sola palabra", "No invita a contar una historia."),
            ex("¿Para qué se pide permiso antes de hacer preguntas?", "Para ser respetuoso", "La persona decide si quiere contestar."),
            ex("¿Qué significa escuchar con respeto?", "Atender sin interrumpir", "Se deja terminar a quien cuenta."),
        ],
        "apply": [
            ex("Convierte «¿Tenías mascotas?» en una pregunta que empiece con cuál.", "¿Cuál era tu mascota?", "Pregunta cuál, en vez de sí o no."),
            ex("Convierte «¿Había fiestas en tu pueblo?» en una pregunta que empiece con cómo.", "¿Cómo eran las fiestas de tu pueblo?", "Pide una descripción."),
            ex("¿Cuál pregunta es mejor para saber qué comía la abuela de niña: «¿Comías?» o «¿Qué comías en tu casa cuando eras niña?».", "¿Qué comías en tu casa cuando eras niña?", "La segunda pide contar."),
        ],
        "reason": [
            ex("Luis preguntó a su tío: «¿Por qué no tienes plata?». Su tío se puso triste. ¿Por qué fue mala la pregunta?", "Porque era privada y podía ofender", "Hay preguntas que no se deben hacer."),
            ex("Rosa quiere saber cómo era el barrio de su abuela. ¿Cuál pregunta debe hacer: «¿Había casas?» o «¿Cómo era el barrio donde vivías?»?", "¿Cómo era el barrio donde vivías?", "Invita a describir."),
        ],
        "challenge": [
            ex("Hay tres preguntas: A) «¿Naciste en la ciudad?» B) «¿Dónde naciste?» C) «¿Te gusta la ciudad?». ¿Cuáles empiezan con una palabra de pregunta?", "B", "Solo B empieza con dónde."),
            ex("Ordena los pasos de una entrevista: A) hacer las preguntas, B) saludar, C) agradecer.", "B, A, C", "Primero se saluda, luego se pregunta y al final se agradece."),
        ],
    },
    context=[ex("Camila quiere entrevistar a su abuelo sobre su infancia. Tiene tres preguntas: «¿A qué jugabas de niño?», «¿Tenías juguetes?» y «¿Cómo era tu escuela?». ¿Cuál no se responde con sí o no?", "«¿A qué jugabas de niño?» y «¿Cómo era tu escuela?»", "Las dos piden contar.")],
    selfcheck=[
        ex("¿Una entrevista es una conversación con preguntas?", "Sí", "Se hace para saber algo."),
        ex("¿Se debe interrumpir a quien cuenta?", "No", "Se le escucha con respeto."),
        ex("Escribe una pregunta con la palabra quién.", "¿Quién te enseñó a cocinar?", "Es una pregunta abierta."),
    ],
    open_task=task("Prepara tres preguntas respetuosas para un adulto de tu familia, tomando una de cada lista: (a) cuándo o dónde: «¿Dónde viviste de niño?» o «¿Cuándo naciste?»; (b) cómo: «¿Cómo celebraban un cumpleaños?» o «¿Cómo era tu escuela?»; (c) qué: «¿Qué juegos tenías?» o «¿Qué comida preparaban en las fiestas?».", "1) ¿Dónde viviste de niño? 2) ¿Cómo era tu escuela? 3) ¿Qué juegos tenías?", ["tres preguntas", "empiezan con palabra de pregunta", "respetuosas"], ["lista de tres preguntas"], ["preguntas de sí o no", "preguntas privadas"], "Pide que lea cada pregunta y diga si se puede contestar con una sola palabra."),
    reinforce="Haz una pregunta con qué a alguien de tu casa y escribe lo que contesta.",
    extend="Agrega una cuarta pregunta que empiece con por qué.",
)

register(
    OA4, 3,
    materials="Lápiz y papel. La entrevista imaginaria a una abuela está escrita en los ejercicios. Si puedes, hazla con un adulto de tu casa.",
    use="Aprenderé a registrar lo que cuenta un adulto como una fuente oral, con fechas. Sirve para conservar los recuerdos de mi familia.",
    prior=["Sé hacer preguntas.", "Sé leer fechas con día, mes y año."],
    explain=[
        "Una fuente oral es lo que una persona cuenta en voz alta sobre lo que vivió. Una entrevista es una fuente oral. Para que sirva, hay que anotar el nombre de quien cuenta, su parentesco (por ejemplo, abuela), la fecha de la entrevista y lo que dijo.",
        "Aquí tienes una entrevista imaginaria a Rosa, una abuela: «Nací el 3 de mayo de 1950. Entré a la escuela en 1957. Me casé el 12 de diciembre de 1970. Mi hija Marta nació el 10 de julio de 1975. En mi infancia jugábamos a la rayuela y no había televisión en mi casa».",
        "Con esa fuente podemos ordenar una línea de tiempo: 1950, nació Rosa; 1957, entró a la escuela; 1970, se casó; 1975, nació su hija. Una fuente oral cuenta recuerdos, y los recuerdos a veces cambian, así que podemos preguntar a otras personas para confirmarlos.",
    ],
    vocab=[("fuente oral", "lo que una persona cuenta en voz alta"), ("parentesco", "relación familiar, como abuela o tío"), ("línea de tiempo", "fila de hechos ordenados por fecha"), ("registrar", "anotar lo que se averigua"), ("recuerdo", "algo del pasado que se guarda en la memoria")],
    worked=[
        {"title": "Leer la fuente", "problem": "Entrevista a Rosa: «Nací el 3 de mayo de 1950. Entré a la escuela en 1957». ¿En qué año entró Rosa a la escuela?", "steps": ["Busco la frase que habla de la escuela.", "Dice 1957."], "answer": "1957"},
        {"title": "Calcular un intervalo", "problem": "Con la misma entrevista, ¿cuántos años tenía Rosa cuando entró a la escuela?", "steps": ["Nació en 1950 y entró en 1957.", "1957 − 1950 = 7."], "answer": "7 años"},
    ],
    mistakes=[
        {"wrong": "Anotar solo lo que me llamó la atención y no la fecha.", "why": "Se piensa que la fecha no importa.", "fix": "Escribe la fecha de la entrevista y el nombre de quien cuenta."},
        {"wrong": "Creer que la fuente oral es siempre exacta.", "why": "Los recuerdos pueden cambiar con el tiempo.", "fix": "Pregunta a otras personas o mira una foto para confirmar."},
    ],
    tiers={
        "recovery": [
            ex("Entrevista a Rosa: «Nací el 3 de mayo de 1950». ¿En qué año nació Rosa?", "1950", "Es el año que dice la entrevista."),
            ex("Entrevista a Rosa: «Me casé el 12 de diciembre de 1970». ¿En qué mes se casó Rosa?", "diciembre", "Es el mes que aparece en la fecha."),
            ex("Entrevista a Rosa: «Mi hija Marta nació el 10 de julio de 1975». ¿Cómo se llama la hija de Rosa?", "Marta", "La entrevista la nombra."),
        ],
        "understand": [
            ex("¿Qué es una fuente oral?", "Lo que una persona cuenta en voz alta", "Es una entrevista o un relato hablado."),
            ex("¿Qué cuatro datos conviene anotar de una entrevista?", "Nombre, parentesco, fecha y lo que dijo", "Así se sabe quién contó y cuándo."),
            ex("¿Por qué conviene confirmar un recuerdo con otra persona o una foto?", "Porque los recuerdos pueden cambiar", "Otra fuente ayuda a comprobarlo."),
        ],
        "apply": [
            arith("Rosa nació en 1950 y se casó en 1970. ¿Cuántos años tenía cuando se casó?", "1970-1950", "Se resta el año de nacimiento al año del matrimonio."),
            arith("Rosa nació en 1950 y su hija Marta nació en 1975. ¿Cuántos años tenía Rosa cuando nació Marta?", "1975-1950", "Se resta el año de nacimiento de Rosa al de Marta."),
            ex("Ordena de más antiguo a más nuevo: Marta nació (10 de julio de 1975), Rosa nació (3 de mayo de 1950), Rosa se casó (12 de diciembre de 1970).", "Rosa nació; Rosa se casó; Marta nació", "Se ordenan por año: 1950, 1970 y 1975."),
        ],
        "reason": [
            ex("Rosa dice que de niña no había televisión en su casa. ¿Esto es un hecho comprobado o un recuerdo de ella?", "un recuerdo de ella", "Es lo que ella cuenta de su infancia."),
            ex("Un niño anota solo «la abuela nació en 1950». ¿Qué otros datos le faltan para que sea una buena fuente?", "Nombre, fecha de la entrevista y qué más contó", "Falta saber quién habló y cuándo."),
        ],
        "challenge": [
            ex("Dos hermanos recuerdan distinto: uno dice que su abuela entró a la escuela a los 7 años y otro que a los 8. La abuela nació en 1950 y entró en 1957. ¿Quién tiene razón?", "el que dice 7", "1957 − 1950 = 7."),
            ex("Rosa cuenta que se casó 5 años antes de que naciera su hija Marta. Rosa se casó en 1970. ¿En qué año nació Marta?", "1975", "1970 + 5 = 1975."),
        ],
    },
    context=[ex("Camila entrevista a su abuelo el 5 de abril de 2025. Él le cuenta que nació el 20 de octubre de 1948. ¿Qué año de nacimiento anota Camila?", "1948", "Es el año dicho por el abuelo.")],
    selfcheck=[
        ex("¿Una fuente oral se escribe o se cuenta en voz alta?", "se cuenta en voz alta", "Oral viene de hablar."),
        ex("Rosa entró a la escuela en 1957 y nació en 1950. ¿Cuántos años tenía?", "7", "1957 − 1950 = 7."),
        ex("¿Qué dato de la entrevista es el parentesco: «abuela Rosa» o «1950»?", "abuela", "Parentesco es la relación familiar."),
    ],
    open_task=task("Hazle una entrevista corta a un adulto de tu casa, o usa esta entrevista imaginaria: «Soy tu tío Mario. Nací en Valdivia el 2 de abril de 1980. Mi juego favorito era el trompo». Anota: nombre, parentesco, fecha de la entrevista, dos datos que cuenta y un año importante. Escribe cuántos años pasaron entre ese año y 2025.", "Nombre: Mario. Parentesco: tío. Fecha de la entrevista: 5 de abril de 2025. Datos: nació en Valdivia; jugaba al trompo. Año importante: 1980. Pasaron 45 años.", ["seis datos anotados", "fecha escrita completa", "diferencia de años correcta"], ["hoja de entrevista con los datos"], ["no anotar la fecha", "calcular mal los años"], "Pide que lea su hoja en voz alta y diga de quién es la fuente."),
    reinforce="Haz una línea de tiempo con tres años que te contó un adulto.",
    extend="Compara dos recuerdos de dos personas sobre el mismo juego.",
)

register(
    OA4, 4,
    materials="Lápiz y papel. Las tablas de antes y ahora están escritas en cada ejercicio.",
    use="Aprenderé a ver qué costumbres de mi familia siguen igual y cuáles cambiaron con el tiempo. Sirve para comprender cómo vivimos hoy.",
    prior=["Sé qué es una costumbre.", "Sé usar antes y ahora."],
    explain=[
        "Una costumbre es algo que una familia hace siempre. Una tradición es una costumbre que pasa de abuelos a padres y a hijos. Una fiesta, como un cumpleaños, es una ocasión en que se celebra algo con la familia.",
        "Con el tiempo, algunas costumbres cambian y otras se mantienen. Lo que se mantiene es una continuidad. Lo que cambia es un cambio. Por ejemplo, hace mucho tiempo las personas escribían cartas a mano; hoy también se mandan mensajes, pero tomar once en familia sigue igual.",
        "Para comparar, hacemos una tabla con «antes» y «ahora» y marcamos si algo cambió o sigue igual. Así vemos que no todo es nuevo y que nuestras familias conservan cosas valiosas.",
    ],
    vocab=[("costumbre", "algo que la familia hace siempre"), ("tradición", "costumbre que pasa de generación en generación"), ("cambio", "algo que antes era de una manera y hoy es de otra"), ("continuidad", "algo que sigue igual con el tiempo"), ("celebrar", "hacer una fiesta por algo que alegra")],
    worked=[
        {"title": "Cambio o continuidad", "problem": "Antes: la abuela lavaba la ropa a mano. Ahora: la familia usa lavadora. ¿Es un cambio o una continuidad?", "steps": ["Antes y ahora son distintos.", "Es un cambio."], "answer": "Es un cambio"},
        {"title": "Continuidad", "problem": "Antes: la familia tomaba once todos los días. Ahora: la familia toma once todos los días. ¿Cambió?", "steps": ["Antes y ahora son iguales.", "Eso es una continuidad."], "answer": "No cambió: es una continuidad"},
    ],
    mistakes=[
        {"wrong": "Pensar que todo cambió con el tiempo.", "why": "Solo se mira lo nuevo.", "fix": "Busca también lo que sigue igual: las tradiciones."},
        {"wrong": "Creer que lo antiguo es siempre mejor o peor.", "why": "Se compara para elegir un ganador.", "fix": "Describe qué cambió y qué siguió igual, sin decir cuál es mejor."},
    ],
    tiers={
        "recovery": [
            ex("Antes: cartas escritas a mano. Ahora: mensajes en el teléfono. ¿Cambió o siguió igual?", "cambió", "El modo de enviar mensajes es distinto."),
            ex("Antes: cumpleaños con torta. Ahora: cumpleaños con torta. ¿Cambió o siguió igual?", "siguió igual", "En los dos casos hay torta."),
            ex("¿Cuál palabra significa que algo sigue igual con el tiempo: cambio o continuidad?", "continuidad", "Continuidad es seguir igual."),
        ],
        "understand": [
            ex("¿Qué es una tradición familiar?", "Una costumbre que pasa de generación en generación", "Se transmite de abuelos a nietos."),
            ex("¿Por qué comparamos antes y ahora?", "Para ver qué cambió y qué sigue igual", "Así entendemos cómo cambió la vida."),
            ex("Un cambio, ¿es siempre algo malo?", "No", "Un cambio solo es algo distinto."),
        ],
        "apply": [
            ex("Tabla. Antes: la familia comía en una mesa grande. Ahora: la familia come en una mesa grande. Clasifica: cambio o continuidad.", "continuidad", "Antes y ahora son iguales."),
            ex("Tabla. Antes: las personas viajaban en carreta. Ahora: las personas viajan en bus. Clasifica: cambio o continuidad.", "cambio", "El medio de transporte es distinto."),
            ex("Tabla. Antes: mi abuela jugaba a la rayuela. Ahora: yo juego a la rayuela. Clasifica: cambio o continuidad.", "continuidad", "El juego sigue igual."),
        ],
        "reason": [
            ex("Lola dice: «Hoy no queda nada igual a cuando mi abuela era niña». Su abuela dice que todavía celebran Navidad en familia. ¿Tiene razón Lola?", "No; algunas cosas siguen igual", "La celebración de Navidad es una continuidad."),
            ex("Beto dice que lo de antes era mejor. ¿Qué debería hacer una comparación justa?", "Describir qué cambió y qué siguió igual", "No se trata de elegir al mejor."),
        ],
        "challenge": [
            ex("Dos filas. Antes: lavar a mano, escribir cartas, tomar once, jugar rayuela. Ahora: lavadora, mensajes, tomar once, jugar rayuela. ¿Cuántas continuidades hay?", "2", "Solo tomar once y jugar rayuela siguen igual."),
            ex("En las mismas dos filas, ¿cuántos cambios hay?", "2", "Lavar y escribir cartas cambiaron."),
        ],
    },
    context=[ex("La abuela de Ema cuenta que de niña su familia hacía pan amasado los domingos. Ema cuenta que su familia hace pan amasado los domingos, pero ahora lo cuecen en horno eléctrico. ¿Qué se mantuvo y qué cambió?", "Se mantuvo hacer pan amasado los domingos; cambió el horno", "El pan sigue igual y el horno es distinto.")],
    selfcheck=[
        ex("¿Una costumbre que sigue igual es una continuidad o un cambio?", "continuidad", "No cambió con el tiempo."),
        ex("Antes: lámpara a gas. Ahora: lámpara eléctrica. ¿Es continuidad o cambio?", "cambio", "El tipo de lámpara es distinto."),
        ex("¿Qué es una tradición?", "Una costumbre que pasa de generación en generación", "Es lo que la familia conserva."),
    ],
    open_task=task("Haz una tabla de dos columnas, antes y ahora, con tres filas sobre tu familia. Usa estas ideas: cómo comen, cómo celebran los cumpleaños, cómo se comunican con los parientes lejanos. En cada fila marca con una C si cambió o con una I si sigue igual.", "Comer: antes en la mesa familiar, ahora en la mesa familiar (I). Cumpleaños: antes torta con velas, ahora torta con velas (I). Comunicarse: antes cartas, ahora llamadas por teléfono (C).", ["tres filas", "antes y ahora distintos o iguales", "marca C o I correcta"], ["tabla de tres filas"], ["marcar C cuando es igual", "no completar antes y ahora"], "Pide que explique en una fila por qué marcó C o I."),
    reinforce="Pregunta a un adulto qué juego tenía de niño y si todavía se juega.",
    extend="Escribe una costumbre de tu familia que quisieras conservar y por qué.",
)

register(
    OA4, 5,
    materials="Lápiz y papel. Las frases de familias imaginarias están escritas en cada ejercicio. No uses datos privados en ninguna tarea.",
    use="Aprenderé a comunicar lo que descubrí de mi familia cuidando lo privado y respetando a las personas. Sirve para compartir historias sin hacer daño.",
    prior=["Sé hacer una entrevista.", "Sé distinguir datos privados de datos seguros."],
    explain=[
        "Cuando cuentas la historia de tu familia a otros, elige qué compartir. Sirven los recuerdos alegres, las fiestas, las comidas y los juegos. No compartas direcciones, teléfonos, contraseñas ni cosas tristes o delicadas, como enfermedades o peleas.",
        "Antes de contar algo sobre una persona, pregúntale si te da permiso. Si dice que no, se respeta. También puedes contar sin decir nombres: «Mi tía hace unas sopaipillas muy ricas» sin dar su nombre completo.",
        "Un buen relato familiar dice qué pasó, quién lo cuenta y cuándo. Por ejemplo: «Mi abuela me contó, el 5 de abril de 2025, que de niña jugaba a la rayuela en el patio». Así quien escucha sabe que es una fuente oral y de dónde viene la información.",
    ],
    vocab=[("permiso", "decir primero si puedo contar algo de otra persona"), ("dato delicado", "información que puede entristecer o poner en riesgo"), ("relato", "historia que se cuenta"), ("compartir", "mostrar o contar a otros"), ("respetar", "aceptar lo que otra persona decide")],
    worked=[
        {"title": "Elegir qué compartir", "problem": "Mi abuela me contó que de niña jugaba a la rayuela y que su casa quedaba en una calle con nombre y número. ¿Qué parte cuento a mi curso?", "steps": ["Los juegos son seguros.", "La dirección es privada."], "answer": "Cuento que jugaba a la rayuela; no digo la dirección"},
        {"title": "Pedir permiso", "problem": "Mi tío me contó una anécdota divertida. ¿Qué hago antes de contarla en el curso?", "steps": ["La historia es de mi tío.", "Le pregunto si me deja contarla."], "answer": "Le pido permiso a mi tío"},
    ],
    mistakes=[
        {"wrong": "Contar un secreto familiar porque es interesante.", "why": "Se piensa que contar algo importante lo hace valioso.", "fix": "Los secretos y las cosas tristes no se cuentan sin permiso."},
        {"wrong": "Decir «mi abuela dijo» sin avisar de quién es la fuente.", "why": "Se olvida citar de dónde viene la información.", "fix": "Di quién te lo contó y cuándo."},
    ],
    tiers={
        "recovery": [
            ex("¿Se puede compartir con el curso la comida preferida de tu familia?", "Sí", "Es un gusto seguro."),
            ex("¿Se puede compartir el número de teléfono de tu casa?", "No", "Es un dato privado."),
            ex("¿Qué se debe pedir antes de contar la historia de otra persona?", "Permiso", "La historia es de ella."),
        ],
        "understand": [
            ex("¿Por qué no se cuentan las cosas tristes o delicadas de la familia sin permiso?", "Porque pueden herir o poner en riesgo a alguien", "Son datos delicados."),
            ex("¿Qué tres cosas dice un buen relato: quién cuenta, cuándo y qué pasó, o solo qué pasó?", "Quién cuenta, cuándo y qué pasó", "Así se sabe de dónde viene la información."),
            ex("¿Qué es un dato delicado?", "Información que puede entristecer o poner en riesgo", "Se debe cuidar."),
        ],
        "apply": [
            ex("Escribe S si puedes compartir con el curso o P si es privado: «Mi mamá hace sopaipillas los domingos».", "S", "Es una costumbre alegre y segura."),
            ex("Escribe S si puedes compartir con el curso o P si es privado: «El número de cuenta del banco de mi papá».", "P", "Es un dato muy privado."),
            ex("Escribe S si puedes compartir con el curso o P si es privado: «Mi abuela jugaba al trompo cuando era niña».", "S", "Es un recuerdo de juego y no pone en riesgo a nadie."),
        ],
        "reason": [
            ex("Mateo quiere contar que su tío está enfermo. Su tío no sabe. ¿Qué debería hacer?", "Preguntarle antes o no contarlo", "Es un dato delicado de otra persona."),
            ex("Una compañera dice «mi abuela contó que se casó muy joven». ¿Qué falta para que sea una buena fuente?", "Decir quién lo contó y cuándo", "Solo dice una frase sin la fecha."),
        ],
        "challenge": [
            ex("Tres frases: A) «Mi tía hace pan amasado los domingos» B) «Mi vecino tiene problemas de plata» C) «Mi abuelo nació en 1948». ¿Cuáles puedes compartir sin problemas?", "A y C", "B es un dato delicado sobre otra persona."),
            ex("Escribe un relato de una frase con quién lo cuenta, cuándo y qué pasó, usando estos datos: abuela, 5 de abril de 2025, jugaba a la rayuela en el patio.", "Mi abuela me contó el 5 de abril de 2025 que jugaba a la rayuela en el patio", "Incluye la fuente, la fecha y lo contado."),
        ],
    },
    context=[ex("Para el diario mural, la profesora pide una historia familiar de tres frases. Lola escribió: «Mi abuela se llama Rosa. Vive en la calle con número de su casa. Hace sopaipillas». ¿Qué frase debe sacar?", "La que dice dónde vive", "Es la dirección, un dato privado.")],
    selfcheck=[
        ex("¿Qué se pide antes de contar la historia de un familiar?", "permiso", "Es su historia."),
        ex("¿Se puede contar la clave del computador de tu casa?", "No", "Es un dato privado."),
        ex("¿Se puede contar un juego que jugaba tu abuela?", "Sí", "Es un recuerdo seguro."),
    ],
    open_task=task("Escribe un pequeño relato familiar de tres frases usando uno de estos datos imaginarios: (a) «Mi abuela jugaba a la rayuela»; (b) «Mi abuelo hacía volantines en septiembre»; (c) «Mi tía preparaba pan amasado los domingos». Indica quién cuenta y la fecha. No incluyas direcciones ni teléfonos.", "Mi abuela me contó el 5 de abril de 2025 que jugaba a la rayuela. Dibujaba el juego con tiza en el patio. Todavía me enseña a jugar.", ["tres frases", "dice quién cuenta y cuándo", "sin datos privados"], ["relato escrito"], ["incluir dirección", "no decir quién lo cuenta"], "Pide que lea el relato y diga qué parte es la fuente oral."),
    reinforce="Cuenta a un adulto una historia de tu familia que sí puedas compartir.",
    extend="Haz una lista de tres tipos de datos que nunca se cuentan a desconocidos.",
)
