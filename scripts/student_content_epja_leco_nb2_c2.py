"""Lenguaje y Comunicación EPJA Nivel 2 (5.º y 6.º), módulo 3: OAD-10, evaluar textos audiovisuales a partir de su contenido y su forma.
Los guiones son inventados y se leen en papel: no hay audio ni video reales."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los guiones, fichas y datos están escritos en cada ejercicio y son inventados para este cuaderno: "
    "no necesitas video, audio ni internet. Cuando la clase habla de un video, usa el guion escrito: lo que se ve, la voz y los gestos "
    "se describen entre paréntesis. Si quieres, pide a otra persona que lo lea en voz alta con el tono indicado. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)

build = make_build(MATERIALS)

O = "EPJA-LECO-NB2-OAD-10"

G1 = ("Video de ejemplo «Cómo preparar lentejas» (datos inventados). IMAGEN: una persona lava lentejas en un colador. "
      "VOZ (tono claro, ritmo calmado): «Lave las lentejas y cocínelas con agua hasta que estén blandas.» "
      "TEXTO EN PANTALLA: «Ingredientes: lentejas, agua, sal». No se indica quién publicó el video.")
G2 = ("Tres textos de ejemplo. Texto 1 (voz de noticiero): «La junta de vecinos recibió ayer 40 firmas para pedir más luminarias; las firmas se entregaron a la municipalidad.» "
      "Texto 2 (voz de tutorial): «El hielo flota porque, al congelarse, el agua ocupa más espacio y por eso queda más liviana que el agua líquida.» "
      "Texto 3 (voz de columna): «Creo que la feria debería abrir también los domingos, porque así más familias podrían comprar y los feriantes venderían más.»")
G3 = ("Aviso de ejemplo, sin marcas reales. VOZ (tono muy seguro, volumen alto, ritmo rápido): «Todos los expertos dicen que este jabón limpia diez veces más. ¡Compre ya!» "
      "IMAGEN: una persona con bata blanca sostiene el jabón. TEXTO EN PANTALLA, en letra muy pequeña: «Resultado de ejemplo; depende del uso».")
G4 = ("Pauta de ejemplo para evaluar un video: cada criterio vale de 0 a 2 puntos (0 = no cumple, 1 = cumple en parte, 2 = cumple bien). "
      "Criterios: 1) tema claro, 2) fuente indicada, 3) datos respaldados, 4) voz e imagen coherentes. "
      "Video A de ejemplo: tema claro 2, fuente indicada 2, datos respaldados 1, voz e imagen coherentes 2. "
      "Video B de ejemplo: tema claro 1, fuente indicada 0, datos respaldados 0, voz e imagen coherentes 2.")
G5 = ("Video de ejemplo «El control de salud» emitido por un consultorio ficticio (datos inventados). VOZ (tono cálido, ritmo calmado): "
      "«El control de salud es una cita para conversar con un profesional y revisar cómo estamos. Si tiene dudas, pregunte; el equipo del consultorio las responderá.» "
      "IMAGEN: una profesional escucha a una persona y toma notas. TEXTO EN PANTALLA: «Consultorio de ejemplo. Pida hora en el mesón».")
G6 = ("Video de ejemplo «Ahorro en casa» (datos inventados). VOZ (tono animado, ritmo rápido): «Desenchufar los aparatos ahorra mucho; los expertos lo saben.» "
      "IMAGEN: una persona desenchufa un cargador. TEXTO EN PANTALLA: «Fuente: informe de una organización de consumidores de ejemplo, 2024 (año de ejemplo)».")

# ============================================================ clase 1
build(
    O, 1, G1,
    use="Hoy distingo el contenido y la forma de un video y empiezo a evaluarlo con razones.",
    prior=["Sé separar lo verbal de lo no verbal.", "Puedo decir de qué trata un video.", "He visto recetas, avisos o indicaciones en pantalla."],
    explain=[
        "Evaluar un texto audiovisual es juzgarlo con razones: ¿es claro?, ¿está completo?, ¿se puede confiar? No es decir solo «me gustó» o «no me gustó». Lo haces cuando decides si sigues una receta o una indicación que viste en pantalla.",
        "Hay dos grandes cosas para mirar. El contenido es lo que el video dice: los datos, los pasos, las ideas. La forma es cómo lo dice: la voz, el ritmo, la imagen, el orden y el tipo de lenguaje.",
        "Además conviene preguntarse por la fuente, que es quién publicó el video, y por el propósito, que es para qué se hizo: informar, explicar, convencer o vender. Sin fuente conocida, el contenido merece más cuidado.",
    ],
    vocab=[("evaluar", "juzgar algo con razones"), ("contenido", "lo que dice un texto"), ("forma", "cómo está dicho: voz, imagen, orden"), ("fuente", "quién publicó la información"), ("propósito", "para qué se hizo el texto")],
    worked=[
        ("Contenido y forma de un video", "Video de ejemplo «Cómo regar una huerta». IMAGEN: una persona riega plantas con una regadera. VOZ (tono calmado, ritmo lento): «Riegue temprano en la mañana o al atardecer.» TEXTO EN PANTALLA: «Menos sol, menos evaporación». No se indica quién publicó el video.", ["Contenido: regar temprano o al atardecer, con la razón del sol y la evaporación.", "Forma: voz calmada, ritmo lento e imagen que muestra el riego.", "Falta: cuánta agua usar; tampoco se indica la fuente."], "Contenido útil pero incompleto; forma clara; fuente desconocida"),
        ("Hecho y opinión", "Dos frases de ejemplo: «La persona riega con una regadera» y «Es la forma más linda de regar».", ["La primera se puede observar: es un hecho.", "La segunda es un juicio sin razones: es una opinión."], "La primera es un hecho; la segunda, una opinión"),
    ],
    mistakes=[("Evaluar diciendo solo «me gustó».", "Una evaluación necesita razones sobre el contenido y la forma.", "Agrega por qué: qué dice, qué falta, cómo se entiende."),
              ("Confiar sin saber quién lo publicó.", "Sin fuente no se puede comprobar el contenido.", "Pregunta siempre: ¿quién lo publicó y para qué?")],
    T=[
        ("abc", "{F} ¿Qué enseña este video?", "Cómo preparar lentejas", "Cómo comprar verduras", "Cómo lavar la ropa", "El título y la voz hablan de lavar y cocinar lentejas."),
        ("ab", "{F} ¿Qué aspecto corresponde a la forma?", "El tono claro y el ritmo calmado de la voz", "La lista de ingredientes", "La forma es cómo se dice: voz, ritmo e imagen; los ingredientes son contenido."),
        ("{F} La lista «lentejas, agua, sal», ¿es contenido o forma? Responde con una palabra.", "contenido", "Son datos del texto, es decir, lo que dice."),
        ("abc", "{F} ¿Qué dato importante falta en el contenido?", "Cuánto tiempo cocinar y cuánta agua usar", "El color de la olla", "Cuántas personas ven el video", "Sin tiempo ni cantidad de agua no se puede repetir la receta."),
        ("ab", "{F} ¿Qué se desconoce sobre la fuente?", "Quién publicó el video", "Cuántas lentejas se usan", "El guion dice expresamente que no se indica quién lo publicó."),
        ("abc", "{F} ¿Cuál es el propósito del video?", "Enseñar a preparar un plato", "Vender un producto", "Convencer de votar por alguien", "Explica pasos y no ofrece compra ni pide apoyo."),
        ("ab", "Un video dice «Esta es la mejor receta del mundo» y no da razones. ¿Es hecho u opinión?", "Una opinión", "Un hecho", "«La mejor» es un juicio personal que no se puede comprobar."),
        ("abc", "«La persona lava las lentejas en un colador», ¿es un hecho o una opinión?", "Un hecho, porque se puede observar en la imagen", "Una opinión, porque la dice una persona", "Una opinión, porque está en un video", "Lo que se ve en la imagen puede comprobarse."),
        ("ab", "¿Qué significa evaluar un video?", "Juzgar si es claro, completo y confiable, con razones", "Decir si me gusta o no", "Evaluar exige fundamentos; el gusto solo no es evaluación."),
        ("abc", "{F} Ana dice: «Me gustó». Luis dice: «Explica los pasos con claridad, pero no dice el tiempo de cocción». ¿Quién evalúa mejor?", "Luis, porque da razones sobre el contenido", "Ana, porque es breve", "Las dos por igual", "Luis menciona qué dice y qué falta; Ana solo da su gusto."),
        ("abc", "{F} Si el video no tuviera sonido, ¿qué parte del contenido se perdería?", "La indicación de cocinar hasta que estén blandas", "La lista de ingredientes", "Nada", "Solo la voz dice cuándo está lista la comida; el texto solo enumera ingredientes."),
        ("¿Cuál es la letra que falta en «e_aluar»: b o v?", "v", "Evaluar se escribe con v, como evaluación y valor."),
        ("abc", "{F} ¿Cuál es la evaluación más completa?", "Contenido útil pero incompleto; forma clara; fuente desconocida", "Es un video lindo", "No sirve para nada", "El primero considera contenido, forma y fuente con razones."),
    ],
    ctx=("abc", "Una persona ve un video con una indicación sobre cómo tomar un medicamento que no tiene autor ni fuente. ¿Qué es lo más razonable?", "Consultar la indicación con un profesional de la salud", "Seguir el video sin dudar", "Compartirlo con todos", "Sin fuente conocida y en un tema de salud, se confirma con un profesional."),
    sc=[("En Lenguaje: ¿qué es el contenido de un video?", "Lo que dice: datos, pasos e ideas", "El contenido es el mensaje, no la manera de decirlo."),
        ("¿Qué es la forma de un video?", "Cómo está dicho: voz, ritmo, imagen y orden", "La forma incluye todo lo que no es el dato mismo."),
        ("¿Por qué importa la fuente?", "Porque permite comprobar si se puede confiar", "Quien publica se hace responsable de lo que dice.")],
    op=("Evalúa este video de ejemplo: «Voz (tono animado): «Para quitar una mancha, use este truco: frote con sal y deje un rato.» Imagen: una persona frota una tela con sal. No se indica quién lo publicó.» Escribe: qué dice (contenido), cómo lo dice (forma), qué falta y si lo recomendarías sin comprobar.",
        "Contenido: truco de sal para una mancha; falta cuánto tiempo y qué tipo de tela. Forma: voz animada, imagen clara. Fuente desconocida: conviene comprobar antes.",
        ["distingue contenido y forma", "señala qué falta", "da una razón para confiar o dudar"],
        ["un párrafo de tres a cuatro líneas"],
        ["decir solo «me gustó»", "no mencionar la fuente"],
        "Pregunta: «¿Qué razón le diste a tu opinión?»."),
    reinforce="Evalúa un video corto que veas hoy diciendo una razón sobre su contenido y otra sobre su forma.",
    extend="Explica por qué un video puede estar bien hecho en su forma y aun así tener un contenido dudoso.",
)

# ============================================================ clase 2
build(
    O, 2, G2,
    use="Hoy reconozco textos informativos, explicativos y argumentativos y aprendo las palabras para evaluarlos.",
    prior=["Distingo contenido, forma y fuente.", "Sé la diferencia entre hecho y opinión.", "Conozco sinónimos y antónimos."],
    explain=[
        "Los textos no literarios sirven para informar, explicar o convencer. Un texto informativo cuenta qué pasó o qué es algo, con datos. Un texto explicativo dice cómo o por qué ocurre algo. Un texto argumentativo defiende una opinión con razones.",
        "En el texto argumentativo hay una tesis, que es la opinión que se defiende, y argumentos, que son las razones que la apoyan. Una opinión sin razones no es un argumento: es solo una afirmación.",
        "Para evaluar usamos criterios, que son las preguntas que nos hacemos: ¿es claro?, ¿es confiable?, ¿es adecuado para quien lo escucha? Conocer sinónimos y antónimos ayuda a precisar: confiable es lo contrario de dudoso; claro, lo contrario de confuso.",
    ],
    vocab=[("texto informativo", "cuenta qué pasó o qué es algo, con datos"), ("texto explicativo", "dice cómo o por qué ocurre algo"), ("texto argumentativo", "defiende una opinión con razones"), ("tesis", "opinión que se defiende"), ("argumento", "razón que apoya una opinión"), ("criterio", "pregunta con la que juzgamos algo")],
    worked=[
        ("Clasificar textos", "Texto A: «El consultorio atenderá mañana hasta las 17:00 horas». Texto B: «El pan sube porque la levadura produce gas». Texto C: «Opino que la sede debería tener más sillas, porque el taller se llena».", ["Texto A da un dato sobre un horario: informativo.", "Texto B dice por qué sube el pan: explicativo.", "Texto C defiende que haya más sillas y da una razón: argumentativo."], "A: informativo; B: explicativo; C: argumentativo"),
        ("Tesis y argumento", "Del texto C: «Opino que la sede debería tener más sillas, porque el taller se llena».", ["La tesis es «la sede debería tener más sillas».", "El argumento es «el taller se llena»."], "Tesis: más sillas. Argumento: el taller se llena"),
    ],
    mistakes=[("Llamar argumentativo a todo texto que tiene una opinión.", "Es argumentativo cuando defiende la opinión con razones.", "Busca la tesis y las razones que la apoyan."),
              ("Confundir texto informativo con explicativo.", "El informativo cuenta qué es o qué pasó; el explicativo dice cómo o por qué.", "Pregunta: ¿cuenta, explica una causa o convence?")],
    T=[
        ("abc", "{F} ¿Qué tipo de texto es el Texto 1?", "Informativo", "Argumentativo", "Explicativo", "Cuenta un hecho con un dato (40 firmas) sin explicar causas ni dar opiniones."),
        ("abc", "{F} ¿Qué tipo de texto es el Texto 2?", "Explicativo", "Informativo", "Argumentativo", "Dice por qué flota el hielo: explica una causa."),
        ("ab", "{F} ¿Qué tipo de texto es el Texto 3?", "Argumentativo", "Informativo", "Defiende una opinión («debería abrir») con una razón («porque…»)."),
        ("{F} En el Texto 3, ¿qué palabra introduce la razón? Responde con una palabra.", "porque", "«Porque» une la opinión con su razón."),
        ("ab", "{F} ¿Cuál es la tesis del Texto 3?", "La feria debería abrir también los domingos", "Los feriantes venderían más", "La tesis es la opinión que se defiende; lo demás son razones."),
        ("abc", "¿Qué es un argumento?", "Una razón que apoya una opinión", "Una discusión a gritos", "Un dato sin relación", "Un argumento es una razón que justifica o apoya la tesis del texto."),
        ("ab", "Un sinónimo de «confiable» es:", "fidedigno", "dudoso", "Fidedigno significa digno de fe; dudoso es lo contrario."),
        ("abc", "El antónimo de «confuso» es:", "claro", "oscuro", "complicado", "Confuso es lo que no se entiende; claro es lo contrario."),
        ("abc", "«Los feriantes venderían más» en el Texto 3 es:", "Un argumento", "Una fuente", "Una tesis", "Es una razón para apoyar la opinión de abrir los domingos."),
        ("ab", "Un video dice «Esta marcha es una vergüenza» sin dar razones. ¿Es un argumento?", "No, es solo una afirmación sin razones", "Sí, porque expresa una opinión", "Un argumento necesita razones que lo apoyen."),
        ("abc", "¿Qué criterio sirve para evaluar un texto explicativo?", "Si la causa que da es correcta y está bien explicada", "Si tiene muchos adjetivos", "Si dura mucho", "Un texto explicativo se juzga por la exactitud y claridad de su explicación."),
        ("abc", "Un texto: «El 5 de mayo se inauguró la nueva plaza de ejemplo». ¿Qué tipo de texto es?", "Informativo", "Argumentativo", "Explicativo", "Cuenta un hecho con una fecha de ejemplo."),
        ("ab", "Un texto empieza «Opino que todos deberían usar bicicleta, porque contamina menos». ¿Cuál es el tipo de texto?", "Argumentativo", "Informativo", "Hay una tesis («deberían usar bicicleta») y una razón («contamina menos»)."),
    ],
    ctx=("abc", "En una reunión de vecinos alguien muestra un video donde una voz dice «La tarifa subirá el próximo mes, según el aviso de la empresa de ejemplo». ¿Qué tipo de texto es?", "Informativo, porque comunica un hecho y cita su fuente", "Argumentativo, porque defiende una postura", "Explicativo, porque dice por qué ocurre", "Comunica un dato y nombra una fuente; no defiende una opinión."),
    sc=[("En Lenguaje: ¿qué hace un texto argumentativo?", "Defiende una opinión con razones", "Un texto argumentativo tiene una tesis y argumentos que la apoyan."),
        ("¿Qué dice un texto explicativo?", "Cómo o por qué ocurre algo", "Un texto explicativo trata de las causas y los procesos de algo."),
        ("En Lenguaje: ¿qué es un criterio para evaluar un video?", "Una pregunta con la que se juzga el texto", "Por ejemplo: ¿es claro?, ¿es confiable?, ¿es adecuado para quien lo ve?")],
    op=("Lee este texto de ejemplo (voz de columna): «Pienso que los paraderos deberían tener techo, porque con lluvia las personas se mojan y esperan más incómodas.» Escribe: tipo de texto, tesis y un argumento. Luego inventa un segundo argumento.",
        "Tipo: argumentativo. Tesis: los paraderos deberían tener techo. Argumento: con lluvia las personas se mojan. Otro: protege del sol.",
        ["identifica el tipo de texto", "separa tesis y argumento", "agrega un argumento propio relacionado"],
        ["tres líneas y un argumento adicional escritos"],
        ["confundir tesis con argumento", "dar una opinión sin razón"],
        "Pregunta: «¿Qué razón apoya la opinión?»."),
    reinforce="Elige un aviso y di si informa, explica o convence, y por qué.",
    extend="Escribe un texto explicativo de dos frases sobre algo que sepas hacer, y otro argumentativo con una opinión y una razón.",
)

# ============================================================ clase 3
build(
    O, 3, G3,
    use="Hoy sigo cuatro pasos para evaluar un aviso: contenido, forma, fuente y conclusión con razones.",
    prior=["Distingo hecho y opinión.", "Sé qué es una fuente.", "Reconozco tono, volumen y ritmo."],
    explain=[
        "Un método sencillo para evaluar un texto audiovisual tiene cuatro pasos. Paso 1: ¿qué dice? Anota el contenido y separa hechos de opiniones. Paso 2: ¿cómo lo dice? Observa voz, ritmo, imagen y letras. Paso 3: ¿quién lo dice y para qué? Busca la fuente y el propósito. Paso 4: concluye con razones.",
        "En los avisos que quieren vender o convencer, la forma puede presionar: voz fuerte, ritmo rápido, frases como «compre ya» o «todos dicen». Esos recursos no prueban nada por sí mismos. También conviene revisar la letra pequeña, donde a veces está lo importante.",
        "Al escribir tu evaluación usa los verbos con cuidado: «el aviso afirma», «mostró», «mostrará». El presente cuenta lo que hace el texto; el pasado, lo que ya ocurrió; el futuro, lo que se anuncia.",
    ],
    vocab=[("afirmar", "decir que algo es verdad"), ("respaldo", "prueba o fuente que apoya un dato"), ("presionar", "empujar a decidir rápido"), ("letra pequeña", "condiciones escritas con letra diminuta")],
    worked=[
        ("Evaluar el aviso", "Aviso de ejemplo. VOZ (tono muy seguro, ritmo rápido): «Esta pintura cubre todo en una mano. ¡Compre ya!» IMAGEN: una persona con delantal sostiene un tarro. TEXTO EN PANTALLA, en letra muy pequeña: «Depende de la superficie; ver condiciones».", ["Paso 1: afirma que cubre «todo en una mano»; es una afirmación sin respaldo.", "Paso 2: voz muy segura y ritmo rápido; el delantal da apariencia de experto; la letra pequeña dice «depende de la superficie».", "Paso 3: no hay fuente; el propósito es vender.", "Paso 4: no convence: la promesa no tiene respaldo y la letra pequeña la matiza."], "Poco confiable: promesa sin respaldo, fuente ausente y propósito de venta"),
        ("Verbos en la evaluación", "Frases de ejemplo: «El aviso promete», «el aviso prometió ayer», «el aviso prometerá mañana».", ["Promete está en presente.", "Prometió está en pasado.", "Prometerá está en futuro."], "Promete: presente. Prometió: pasado. Prometerá: futuro"),
    ],
    mistakes=[("Creer una cifra solo porque se dice con seguridad.", "La seguridad de la voz no es una prueba.", "Pregunta cuál es la fuente de la cifra."),
              ("No leer la letra pequeña.", "Ahí pueden estar las condiciones que cambian el mensaje.", "Léela antes de concluir.")],
    T=[
        ("abc", "{F} ¿Qué afirma el aviso?", "Que el jabón limpia diez veces más", "Que el jabón es gratis", "Que el jabón es nuevo", "La voz lo dice con seguridad, aunque sin pruebas."),
        ("ab", "{F} ¿Cuál es un elemento de forma que presiona?", "El volumen alto y el ritmo rápido", "El tipo de jabón", "La forma son los recursos de la voz y la imagen; el jabón es parte del contenido."),
        ("ab", "{F} ¿A qué invita la frase «Compre ya»?", "A comprar rápido", "A informarse con calma", "La frase empuja a decidir rápido, no a informarse con calma."),
        ("abc", "{F} ¿Qué dato falta para respaldar «todos los expertos dicen»?", "Quiénes son los expertos y dónde lo dijeron", "El color del envase", "Cuánto cuesta", "Sin nombres ni fuente, la frase no se puede comprobar."),
        ("ab", "{F} ¿Qué dice la letra pequeña?", "«Resultado de ejemplo; depende del uso»", "«Garantizado para todos»", "La letra pequeña matiza lo que la voz afirma sin condiciones."),
        ("abc", "{F} ¿Cuál es el propósito del aviso?", "Vender un producto", "Enseñar a limpiar sin comprar", "Informar de un corte de agua", "Termina con «Compre ya» y muestra el producto."),
        ("ab", "{F} ¿Qué efecto tiene la bata blanca en la imagen?", "Da apariencia de experto sin demostrar nada", "Prueba que el jabón funciona", "La imagen sugiere autoridad, pero no es un respaldo real."),
        ("abc", "¿Cuál es el orden correcto de los pasos?", "Contenido, forma, fuente y propósito, conclusión", "Conclusión, forma, contenido, fuente", "Fuente, conclusión, forma, contenido", "Primero se reúnen los datos y al final se concluye."),
        ("abc", "El aviso afirma hoy, afirmó ayer y _____ mañana. ¿Qué forma falta?", "afirmará", "afirma", "afirmó", "El futuro del verbo afirmar para él o ella es afirmará."),
        ("ab", "{F} Si la voz tuviera tono calmado y el texto en pantalla dijera «Cifra obtenida en una prueba de ejemplo realizada por la empresa», ¿qué cambiaría?", "Habría un respaldo parcial, aunque seguiría siendo un aviso de venta", "El aviso dejaría de querer vender", "Aparece una fuente, pero la propia empresa vende el producto; aún se debe dudar."),
        ("abc", "{F} ¿Qué conclusión con razones es la mejor?", "Es poco confiable: la cifra no tiene respaldo y la letra pequeña la matiza", "Es bueno porque la voz es fuerte", "Es malo porque no me gusta la bata", "La conclusión se apoya en el contenido y en la letra pequeña."),
        ("¿Cómo se escribe: «presionar» con z o con s? Responde con una letra: s o z.", "s", "Presionar viene de presión, que se escribe con s."),
        ("abc", "Una persona dice «Conviene dudar porque no hay fuente». ¿Qué paso del método usa?", "El paso 3: buscar la fuente y el propósito", "El paso 1: copiar el aviso", "El paso 2: medir el volumen", "La falta de fuente es el centro del paso 3."),
    ],
    ctx=("abc", "En la tele pasan un aviso de ejemplo: una voz rápida dice «¡Último día! Baje de peso en una semana». En pantalla, letra diminuta: «Resultados de ejemplo». ¿Qué conviene hacer?", "Notar la presión y la letra pequeña, y consultar a un profesional de salud antes de decidir", "Comprar de inmediato", "Creer que todos bajaron de peso", "La urgencia y la promesa sin respaldo piden cautela, y en salud corresponde consultar a un profesional."),
    sc=[("¿Qué se hace en el paso 3 del método?", "Buscar la fuente y el propósito", "Saber quién habla y para qué ayuda a juzgar."),
        ("En Lenguaje: ¿qué es la letra pequeña?", "Condiciones escritas con letra diminuta", "Puede cambiar el sentido del mensaje."),
        ("¿Qué tiempo verbal es «afirmó»?", "Pasado", "El pasado cuenta algo que ya ocurrió, por eso «afirmó» está en pasado.")],
    op=("Evalúa con los cuatro pasos este aviso de ejemplo: «Voz (tono muy rápido): «Nuestro curso lo garantiza todo. ¡Inscríbase ya!» Texto en pantalla, letra muy pequeña: «Cupos limitados; condiciones en la oficina».» Escribe una frase por paso. Revisa que los verbos estén bien conjugados.",
        "Paso 1: afirma que lo garantiza todo. Paso 2: voz rápida y letra pequeña. Paso 3: no se indica quién lo ofrece; propósito: vender. Paso 4: poco confiable.",
        ["escribe una frase por cada paso", "separa lo que afirma de lo que prueba", "concluye con una razón"],
        ["cuatro frases escritas"],
        ["concluir sin leer la letra pequeña", "mezclar los tiempos verbales"],
        "Pregunta: «¿Qué razón sostiene tu conclusión?»."),
    reinforce="Mira un aviso comercial y cuenta cuántas veces intenta apurarte.",
    extend="Reescribe el aviso del jabón para que sea honesto, con una afirmación que pueda respaldarse.",
)

# ============================================================ clase 4
build(
    O, 4, G4,
    use="Hoy practico con apoyo: uso una pauta con puntajes para evaluar dos videos y redactar mi conclusión.",
    prior=["Sé los cuatro pasos para evaluar.", "Distingo hecho y opinión.", "Sé sumar números pequeños."],
    explain=[
        "Una pauta es una lista de criterios con puntajes. Sirve para evaluar con orden: cada criterio se juzga por separado y al final se suman los puntos. Los puntajes ayudan a comparar, pero no reemplazan las razones: siempre se explica por qué se puso cada nota.",
        "Al escribir la evaluación cuida la ortografía. Las palabras agudas (la fuerza cae en la última sílaba) llevan tilde si terminan en n, s o vocal: canción, además, está. Las graves llevan tilde si no terminan en n, s ni vocal: fácil, árbol. Las esdrújulas siempre llevan tilde: música, teléfono.",
        "Cuida también la puntuación: la coma separa partes de una lista o una aclaración, y el punto cierra una idea. «Es claro, tiene fuente y datos respaldados.» se lee distinto que sin comas.",
    ],
    vocab=[("pauta", "lista de criterios con puntajes"), ("puntaje", "número que muestra cuánto se cumple un criterio"), ("coherente", "que no se contradice"), ("tilde", "rayita que marca la sílaba más fuerte")],
    worked=[
        ("Sumar la pauta", "Con la misma pauta, video C de ejemplo: tema claro 2, fuente indicada 1, datos respaldados 1, voz e imagen coherentes 2. Video D de ejemplo: tema claro 0, fuente indicada 2, datos respaldados 2, voz e imagen coherentes 1.", ["Video C: 2 + 1 + 1 + 2 = 6 de 8.", "Video D: 0 + 2 + 2 + 1 = 5 de 8.", "C suma más, pero D tiene mejor fuente y datos; el puntaje no reemplaza las razones."], "C obtiene 6 puntos y D, 5 puntos"),
        ("Acentuar", "Palabras de ejemplo: «corazon», «lapiz», «pajaro».", ["Corazón es aguda y termina en n: lleva tilde.", "Lápiz es grave y no termina en n, s ni vocal: lleva tilde.", "Pájaro es esdrújula: siempre lleva tilde."], "Corazón, lápiz, pájaro"),
    ],
    mistakes=[("Poner puntaje sin explicar por qué.", "El puntaje sin razón no se puede discutir ni mejorar.", "Escribe una razón corta junto a cada nota."),
              ("Olvidar la tilde en palabras agudas terminadas en n.", "Una palabra como «información» lleva tilde porque termina en n.", "Marca la sílaba fuerte y revisa su terminación.")],
    T=[
        ("=", "{F} ¿Cuántos puntos suma el video A?", "2+2+1+2", "Se suman los cuatro criterios del video A.", "puntos"),
        ("=", "{F} ¿Cuántos puntos suma el video B?", "1+0+0+2", "Se suman los cuatro criterios del video B.", "puntos"),
        ("{F} ¿Cuál es el puntaje máximo posible de la pauta? Responde con un número.", "8", "Son cuatro criterios de hasta 2 puntos cada uno, es decir, 4 por 2."),
        ("abc", "{F} ¿Qué video indica su fuente?", "El video A", "El video B", "Ambos", "A obtuvo 2 en fuente y B obtuvo 0."),
        ("ab", "{F} ¿Qué significa que B tenga 0 en «datos respaldados»?", "Que no cumple: no respalda sus datos", "Que cumple del todo", "0 es «no cumple», según la pauta."),
        ("=", "{F} ¿Cuántos puntos más que B tiene A?", "7-3", "A suma 7 y B suma 3; la diferencia se calcula restando.", "puntos"),
        ("abc", "¿Cuál palabra está bien escrita?", "canción", "cancion", "cáncion", "Es aguda, termina en n y la fuerza cae en -ción: lleva tilde en la o."),
        ("ab", "¿Cuál palabra lleva tilde?", "fácil", "facil", "Es grave y no termina en n, s ni vocal, por eso se acentúa."),
        ("abc", "{F} ¿Cuál frase explica bien un puntaje?", "«Fuente: 0, porque no dice quién lo publicó»", "«Fuente: 0»", "«Me cae mal»", "La razón hace verificable la nota."),
        ("ab", "¿Cuál oración está bien puntuada?", "El video es claro, tiene fuente y respalda sus datos.", "El video es claro tiene fuente y respalda, sus datos.", "Las comas separan los elementos de la lista; la segunda corta mal la frase."),
        ("abc", "{F} Un compañero dice que A «es perfecto». ¿Qué respuesta es más justa?", "A es bueno, pero respalda sus datos solo en parte", "Tiene toda la razón, porque tiene 7", "A es peor que B", "Con 1 en datos respaldados no es perfecto: la pauta muestra que algo mejora."),
        ("abc", "Escribe el verbo en pasado: «El video B no _____ su fuente». Elige la forma correcta.", "indicó", "indica", "indicará", "El pasado de indicar en tercera persona es indicó, con tilde por ser aguda terminada en vocal."),
        ("ab", "¿Cuál palabra es esdrújula y lleva tilde?", "teléfono", "telefono", "La fuerza cae en la antepenúltima sílaba (te-LÉ-fo-no), y las esdrújulas siempre llevan tilde."),
    ],
    ctx=("abc", "Una persona compara dos videos de ejemplo sobre cómo ahorrar luz. El primero obtiene 7 de 8 y el segundo 3 de 8 con esta pauta. ¿Qué es lo más razonable?", "Elegir el primero y revisar por qué el segundo perdió puntos", "Elegir el segundo porque es más corto", "Ignorar la pauta", "Los puntajes ayudan a comparar y sus razones muestran qué mejorar."),
    sc=[("En Lenguaje: ¿qué es una pauta de evaluación?", "Una lista de criterios con puntajes", "Ordena la evaluación y permite comparar."),
        ("¿Qué palabras agudas llevan tilde?", "Las que terminan en n, s o vocal", "Por ejemplo, canción, además y está."),
        ("¿Para qué sirven las comas en una lista?", "Para separar sus elementos", "Evitan que se lea como una sola idea.")],
    op=("Evalúa este video de ejemplo con la pauta de la clase (0 a 2 por criterio): «La voz explica con claridad cómo reducir el gasto de agua, cita un informe de una organización de ejemplo y la imagen coincide con lo que dice, pero una de sus cifras no tiene respaldo.» Escribe los cuatro puntajes con una razón, la suma y una conclusión.",
        "Tema claro: 2. Fuente indicada: 2. Datos respaldados: 1 (una cifra sin respaldo). Voz e imagen coherentes: 2. Total: 7 de 8.",
        ["asigna un puntaje a cada criterio", "explica cada puntaje con una razón", "suma bien y concluye"],
        ["una tabla con cuatro filas y el total"],
        ["poner puntajes sin razón", "sumar mal"],
        "Pregunta: «¿Por qué no pusiste el máximo en este criterio?»."),
    reinforce="Evalúa con la pauta un aviso corto y suma sus puntos.",
    extend="Agrega un quinto criterio a la pauta y explica por qué lo agregas.",
)

# ============================================================ clase 5
build(
    O, 5, G5,
    use="Hoy evalúo un video de información de salud y escribo mi evaluación con buena ortografía.",
    prior=["Conozco los pasos y la pauta.", "Sé acentuar palabras agudas, graves y esdrújulas.", "Distingo hecho y opinión."],
    explain=[
        "Los videos sobre salud, trámites o servicios del barrio son textos informativos que influyen en decisiones. Evaluarlos significa revisar si son claros, si indican su fuente y si se limitan a informar sin prometer más de lo que pueden. Estos ejemplos son de lectura: no reemplazan la atención de un profesional.",
        "Fíjate también en el registro: un video del consultorio usa un registro formal pero cercano, con «usted». El tono cálido y el ritmo calmado ayudan a que las personas se sientan acogidas.",
        "Cuando escribes tu evaluación, cuida que cada oración tenga sentido y uses las tildes y los signos correctamente: «¿Por qué?» se escribe en dos palabras con tilde cuando pregunta, y «porque» en una palabra cuando responde.",
    ],
    vocab=[("registro formal", "modo de hablar cuidado y respetuoso"), ("acogedor", "que hace sentir bienvenida a la persona"), ("profesional de salud", "persona preparada para atender la salud"), ("por qué / porque", "«por qué» pregunta; «porque» responde")],
    worked=[
        ("Evaluar un video de un trámite", "Video de ejemplo «Cómo pedir una constancia». VOZ (tono claro): «Para pedir una constancia, lleve su cédula y pida un número en el mesón.» IMAGEN: un mesón con un funcionario que atiende. TEXTO EN PANTALLA: «Municipalidad de ejemplo. Atención de lunes a viernes».", ["Contenido: explica qué llevar y dónde pedir un número.", "Forma: tono claro, imagen de un mesón de atención.", "Fuente: indica una municipalidad de ejemplo.", "Conclusión: es claro e indica su fuente; faltaría el horario de atención."], "Claro y con fuente; falta el horario"),
        ("Por qué y porque", "Frases: «¿Por qué cerraron el mesón?» y «Cerraron el mesón porque era feriado».", ["La primera pregunta: se escribe «por qué» en dos palabras con tilde.", "La segunda responde: se escribe «porque» junto y sin tilde."], "Pregunta: por qué. Respuesta: porque"),
    ],
    mistakes=[("Evaluar un video de salud como si diera una indicación personal.", "Un video general no sabe cómo está cada persona.", "Úsalo como información y consulta con un profesional."),
              ("Escribir «porque» cuando se pregunta.", "En una pregunta va «por qué», separado y con tilde.", "Si pregunta, usa «por qué»; si responde, «porque».")],
    T=[
        ("abc", "{F} ¿De qué trata el video?", "De qué es un control de salud", "De cómo cocinar", "De cómo pagar una cuenta", "La voz explica qué es y para qué sirve el control de salud."),
        ("ab", "{F} ¿Qué se invita a hacer si hay dudas?", "Preguntar al equipo del consultorio", "Esperar a que pasen solas", "La voz dice «Si tiene dudas, pregunte»."),
        ("{F} ¿Qué tono tiene la voz? Responde con una palabra.", "cálido", "El guion lo indica: tono cálido."),
        ("abc", "{F} ¿Qué texto aparece en pantalla?", "«Consultorio de ejemplo. Pida hora en el mesón»", "«Compre ya»", "«Resultados garantizados»", "Es el texto en pantalla descrito en el guion."),
        ("ab", "{F} ¿Qué registro usa la voz?", "Formal y cercano, con «usted»", "Muy informal, con groserías", "Habla de «usted» y «tiene», un modo respetuoso y amable."),
        ("abc", "{F} ¿Cuál es el propósito del video?", "Informar sobre un servicio", "Vender un producto", "Convencer de una postura política", "Explica qué es un control y cómo pedir hora."),
        ("ab", "¿Cuál oración está bien escrita?", "¿Por qué conviene preguntar?", "¿Porque conviene preguntar?", "Cuando la oración pregunta, se escribe «por qué» separado y con tilde."),
        ("abc", "Completa: «Conviene preguntar _____ así se aclaran las dudas».", "porque", "por qué", "porqué", "Responde a una pregunta: se escribe junto y sin tilde."),
        ("abc", "{F} Una persona dice: «El video me dice cómo estoy». ¿Es correcto?", "No: el video informa en general y no evalúa a nadie", "Sí, porque es sobre salud", "Sí, porque tiene imágenes", "Solo un profesional que atiende a la persona puede valorar su situación."),
        ("ab", "{F} ¿Qué mejora le agregarías al video?", "Indicar cómo contactar al consultorio", "Subir más el volumen", "Sumar un dato de contacto da más utilidad; el volumen ya es adecuado."),
        ("abc", "{F} ¿Cuál evaluación escrita es la mejor?", "El video es claro y cálido; informa sin prometer cosas, aunque falta un contacto", "Está bien", "No me gustó", "Menciona contenido, forma y una mejora."),
        ("ab", "¿Cuál palabra está bien escrita?", "información", "informacion", "Es aguda, termina en n y lleva tilde en la o."),
        ("abc", "Elige la oración bien puntuada.", "El video explica, informa y orienta.", "El video explica informa, y orienta.", "El, video explica informa y orienta.", "Las comas separan los elementos de la lista de verbos."),
    ],
    ctx=("abc", "Alguien reenvía un video: «Este té cura todo; deje sus controles de salud». ¿Qué es lo más razonable?", "Dudar, porque promete demasiado y desaconseja ir al control; conversar con un profesional de salud", "Aceptarlo porque el tono es amable", "Compartirlo con todos", "Un mensaje que reemplaza la atención profesional con una promesa es poco confiable."),
    sc=[("¿Cuándo se escribe «por qué» separado?", "Cuando se pregunta", "Cuando se pregunta, «por qué» se escribe separado y «qué» lleva tilde."),
        ("En Lenguaje: ¿qué es un registro formal?", "Un modo de hablar cuidado y respetuoso", "Se usa, por ejemplo, con «usted»."),
        ("¿Un video de salud reemplaza a un profesional?", "No", "Informa en general; no conoce cada caso.")],
    op=("Evalúa este video de ejemplo: «VOZ (tono tranquilo): «La vacunación protege a la comunidad. Consulte en su consultorio los datos y las fechas vigentes.» TEXTO EN PANTALLA: «Consultorio de ejemplo». IMAGEN: un calendario en blanco.» Escribe un párrafo de evaluación con contenido, forma y fuente. Revisa tildes, comas y verbos.",
        "Contenido: informa de la vacunación y manda a consultar datos vigentes. Forma: tono tranquilo; el calendario en blanco no entrega fechas. Fuente: consultorio de ejemplo. Conclusión: prudente; faltaría un contacto.",
        ["distingue contenido, forma y fuente", "da una conclusión con razones", "usa bien tildes y comas"],
        ["un párrafo de cuatro a cinco líneas"],
        ["inventar fechas o datos de salud", "no revisar la ortografía"],
        "Pregunta: «¿Dónde está la razón de tu conclusión?»."),
    reinforce="Evalúa un aviso informativo de tu barrio y escribe dos razones.",
    extend="Escribe una pregunta con «por qué» y su respuesta con «porque» sobre un aviso que hayas visto.",
)

# ============================================================ clase 6
build(
    O, 6, G6,
    use="Hoy reviso lo logrado, evalúo un texto con respaldo parcial y decido qué quiero repasar.",
    prior=["Sé evaluar contenido, forma y fuente.", "Uso la pauta de puntajes.", "Cuido tildes y puntuación."],
    explain=[
        "Para cerrar, junta lo aprendido. Un texto audiovisual se evalúa por su contenido (qué dice y si lo respalda), su forma (cómo lo dice) y su fuente (quién lo publica y para qué). Con eso puedes concluir con razones.",
        "Algunos textos mezclan elementos confiables y dudosos. Por ejemplo, una cifra puede tener fuente indicada, pero la frase «los expertos lo saben» no dice quiénes son. Evaluar bien es separar lo que está respaldado de lo que solo se afirma.",
        "Para decidir qué repasar, mira tus puntos débiles: distinguir hecho y opinión, leer la letra pequeña, usar bien las tildes o conjugar los verbos. Anota uno o dos y practica solo esos esta semana.",
    ],
    vocab=[("respaldado", "apoyado por una fuente o una prueba"), ("matizar", "hacer una afirmación menos absoluta"), ("verificar", "comprobar si algo es verdad"), ("repasar", "volver a estudiar algo")],
    worked=[
        ("Separar lo respaldado", "Aviso de ejemplo: VOZ (tono animado): «Cerrar las ventanas en invierno conserva el calor; los especialistas lo recomiendan.» TEXTO EN PANTALLA: «Fuente: guía de una institución de ejemplo, 2023 (año de ejemplo)».", ["«Conserva el calor» es una afirmación general: no dice cuánto.", "«Los especialistas lo recomiendan» no nombra a nadie.", "El texto en pantalla sí indica una fuente de ejemplo con año: eso aporta respaldo, aunque no precisa a los especialistas."], "Respaldo parcial: hay fuente, pero «los especialistas» siguen sin precisar"),
        ("Conjugar", "Frases de ejemplo: «El video explica», «el video explicó», «el video explicará».", ["Explica: presente.", "Explicó: pasado, con tilde.", "Explicará: futuro, con tilde."], "Explica, explicó, explicará"),
    ],
    mistakes=[("Aceptar todo el texto porque una parte tiene fuente.", "Una fuente no respalda cada afirmación del mensaje.", "Revisa cada afirmación por separado."),
              ("Creer que evaluar es criticar.", "Evaluar incluye reconocer lo bueno con razones.", "Anota fortalezas y debilidades.")],
    T=[
        ("ab", "{F} ¿Qué parte del texto en pantalla aporta respaldo?", "Indica una fuente de ejemplo con año", "El volumen de la voz", "El texto en pantalla nombra una organización y un año, que permiten buscar la fuente."),
        ("abc", "{F} ¿Qué es lo que se dice que ahorra?", "Desenchufar los aparatos", "Apagar la tele", "Cambiar la ampolleta", "La voz dice «Desenchufar los aparatos ahorra mucho»."),
        ("{F} ¿La frase «los expertos lo saben» nombra a algún experto? Responde sí o no.", "no", "La frase no da nombres ni fuente, por eso no se puede comprobar."),
        ("abc", "{F} ¿Qué tono tiene la voz?", "Animado", "Cansado", "Serio", "La descripción de la voz en el guion indica un tono animado."),
        ("ab", "{F} ¿Qué tan preciso es «ahorra mucho»?", "Poco preciso, porque no dice cuánto", "Muy preciso", "«Mucho» no es una cantidad medible; falta un dato."),
        ("abc", "{F} ¿Qué relación hay entre la imagen y la voz?", "Se refuerzan: la persona desenchufa un cargador", "Se contradicen", "No tienen relación", "La imagen muestra la acción que la voz nombra."),
        ("ab", "{F} Un amigo dice «Con fuente, todo lo que dice el video es verdad». ¿Es correcto?", "No, porque una fuente no respalda todas las frases", "Sí, porque tiene fuente", "Conviene revisar cada afirmación, no solo la presencia de una fuente."),
        ("abc", "Completa: «El video _____ cómo desenchufar un aparato». Elige el pasado.", "mostró", "muestra", "mostrará", "El pasado de mostrar es mostró, con tilde por ser aguda terminada en vocal."),
        ("abc", "¿Qué es verificar?", "Comprobar si algo es verdad", "Copiar un dato", "Repetir una frase", "Se verifica con otra fuente o un dato confiable."),
        ("ab", "¿Cuál es el antónimo de «respaldado»?", "sin pruebas", "apoyado", "Respaldado es apoyado; sin pruebas es lo contrario."),
        ("abc", "{F} ¿Cuál conclusión es más justa?", "Parcialmente confiable: tiene una fuente, pero deja afirmaciones sin precisar", "Totalmente falso", "Totalmente cierto", "Incluye lo bueno y lo débil con razones."),
        ("ab", "¿Cuál palabra lleva tilde?", "mostró", "muestra", "Mostró es aguda y termina en vocal; muestra es grave y termina en vocal, así que no lleva."),
        ("abc", "Una persona anota: «Debo repasar la letra pequeña y las tildes». ¿Qué hace?", "Elegir qué practicar según sus puntos débiles", "Rendirse", "Repasar todo sin orden", "Elegir dos puntos concretos hace que el repaso sea eficaz."),
    ],
    ctx=("abc", "En un grupo de mensajería alguien publica este aviso de ejemplo: «Los expertos lo saben: comer a oscuras ayuda a bajar de peso». No indica fuente. ¿Qué conviene hacer?", "Pedir la fuente y, si se trata de salud, consultar a un profesional", "Compartirlo de inmediato", "Creerlo porque lo dice un grupo", "La frase «los expertos» sin nombres no se puede comprobar."),
    sc=[("En Lenguaje: ¿qué es verificar?", "Comprobar si algo es verdad", "Se verifica, por ejemplo, buscando la fuente o un dato confiable."),
        ("¿Una fuente respalda todo el texto?", "No, solo lo que se relaciona con ella", "Cada afirmación se revisa por separado."),
        ("¿Cómo decido qué repasar?", "Elijo mis puntos más débiles", "Un repaso concreto es más eficaz.")],
    op=("Haz una autoevaluación con estas preguntas: ¿distingo hecho y opinión?, ¿reconozco la fuente?, ¿uso bien tildes y comas?, ¿conjugo bien los verbos? Luego evalúa este aviso de ejemplo: «VOZ (tono seguro): «Esta aplicación de ejemplo mejora tu memoria en una semana.» TEXTO EN PANTALLA: «Basado en un estudio». IMAGEN: una persona sonríe frente a un teléfono.» Indica qué falta y qué repasarás.",
        "Falta saber quién hizo el estudio y qué mide «mejorar». La sonrisa no prueba nada. Voy a repasar: leer la fuente y distinguir hechos.",
        ["responde las cuatro preguntas", "señala lo respaldado y lo no respaldado", "elige uno o dos puntos para repasar"],
        ["una lista y un párrafo en el cuaderno"],
        ["responder todo con «sí»", "no decir qué repasar"],
        "Pregunta: «¿Qué dato te falta para creerle?»."),
    reinforce="Evalúa un aviso con la pauta de la clase 4 y justifica un puntaje.",
    extend="Escribe un aviso breve y honesto sobre algo que sepas, con una afirmación que pueda respaldarse.",
)
