"""Lengua y Literatura EPJA Media Nivel 1, módulo 4 (parte 3): OAD-15, escribir una interpretación de una obra literaria a partir del análisis intertextual (tesis, evidencia textual, dilemas). Los resúmenes de obras clásicas son propios y los relatos son inventados."""
from __future__ import annotations

from epja_leli_nm1_d_common import build

O = "EPJA-LELI-NM1-OAD-15"

F1 = ("Relato (inventado), «La llave del taller»: don Mario atendió su taller mecánico durante treinta años. El día que se jubiló, puso la llave en la mano de su ayudante, Camilo, y le dijo: «Ahora la puerta la abres tú». "
      "Camilo se quedó un rato mirando la llave. Al día siguiente llegó una hora antes y abrió despacio. "
      "Texto A (inventado): «Don Mario le da la llave del taller a Camilo, quien llega temprano al día siguiente y abre la puerta». "
      "Texto B (inventado): «La llave representa la responsabilidad que pasa de don Mario a Camilo. Camilo se queda mirándola y abre despacio, porque siente el peso de esa responsabilidad».")

F2 = ("Relato (inventado), «La silla vacía»: doña Julia pone cada noche la mesa para tres, aunque su hijo Tomás trabaja en el norte desde hace dos años y en la casa solo viven ella y su hermana Elsa. "
      "Un día, Elsa le dice que ya no es necesario poner el plato de Tomás. Doña Julia responde: «La mesa se pone completa; así la casa sabe que alguien viene». Esa noche, Elsa también deja el pan para tres. "
      "Interpretación de ejemplo (inventada): «La silla vacía representa la esperanza de que Tomás vuelva. Esto se ve cuando doña Julia dice que la casa «sabe que alguien viene». "
      "Además, Elsa termina dejando el pan para tres, lo que muestra que la esperanza se comparte».")

F3 = ("Relato (inventado), «La silla vacía»: doña Julia pone cada noche la mesa para tres, aunque su hijo Tomás trabaja en el norte desde hace dos años y en la casa solo viven ella y su hermana Elsa. "
      "Cuando Elsa le dice que ya no es necesario poner el plato de Tomás, doña Julia responde: «La mesa se pone completa; así la casa sabe que alguien viene». Esa noche Elsa también deja el pan para tres. El relato no cuenta si Tomás vuelve. "
      "Resumen propio, la Odisea, de Homero: Penélope espera a Ulises, que tarda años en volver, y cuida la casa. Cada noche deshace la tela que teje de día para ganar tiempo. "
      "Ficha de análisis (inventada): Personajes: doña Julia cumple el papel de Penélope (quien espera); Tomás, el de Ulises (el ausente). Tema: la espera de un regreso. "
      "Símbolo: la mesa puesta, como la tela, es un gesto que mantiene viva la espera. Lo que cambia: doña Julia no es presionada por pretendientes y el relato no dice si Tomás regresa.")

F4 = ("Resumen propio, Cenicienta (cuento tradicional): una joven maltratada por su familia va a una fiesta con ayuda mágica, deja un zapato al huir y, al final, ese zapato permite que la reconozcan. "
      "Relato (inventado), «El zapato de Mónica»: Mónica limpia las oficinas de una empresa. En la fiesta de aniversario ayuda a colgar los adornos y se queda mirando desde la puerta. "
      "Se va corriendo cuando termina su turno y deja un zapato bajo una mesa. Al día siguiente, el gerente, don Esteban, entra a la sala de aseo con el zapato en la mano y pregunta de quién es. "
      "Mónica levanta la mano, avergonzada. Don Esteban le agradece los adornos, que dejaron bonita la fiesta, y le pide que desde ahora participe en el comité de eventos.")

F5 = ("Resumen propio, Antígona, de Sófocles: Creonte, rey de Tebas, prohíbe enterrar a Polinices, hermano de Antígona. Antígona decide enterrarlo de todos modos, sabiendo que será castigada. "
      "Relato (inventado), «La orden de la bodega»: Nora es encargada de turno en una bodega. Su jefe le ordenó no abrir el local fuera de horario. "
      "A las diez de la noche su compañero Iván la llama: dejó en su casillero la carpeta con los papeles que necesita mañana temprano para un trámite. "
      "Nora piensa en la orden, en el trámite de Iván y en las consecuencias. Decide abrir, sacar la carpeta y escribir un informe para su jefe a primera hora, explicando lo que hizo.")

F6 = ("Relato (inventado), «La silla vacía»: doña Julia pone cada noche la mesa para tres, aunque su hijo Tomás trabaja en el norte desde hace dos años. Cuando su hermana Elsa le dice que no hace falta, ella responde: «La mesa se pone completa; así la casa sabe que alguien viene». Esa noche Elsa también deja pan para tres. "
      "Texto de Gloria (inventado): «El relato cuenta que doña Julia pone la mesa para tres y que su hermana Elsa le dice que no hace falta. Julia responde que la casa sabe que alguien viene. Elsa deja pan para tres. Es un cuento bonito». "
      "Pauta de revisión (inventada), seis criterios: 1) tiene una tesis clara; 2) apoya la tesis con al menos dos evidencias del texto; 3) explica cada evidencia; 4) usa conectores; 5) relaciona con la otra obra; 6) cierra con una conclusión. "
      "Resumen propio, la Odisea, de Homero: Penélope espera a Ulises y cuida la casa durante años.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya hago a diario, explicar qué quiso decir alguien, y aprendo a distinguir un resumen de una interpretación.",
    prior=["Explico qué quiso decir alguien cuando habla con frases indirectas.", "Sé contar con mis palabras una historia.", "Sé que un objeto puede significar algo."],
    explain=[
        "Tú ya interpretas todos los días. Si alguien dice «hay que apretarse el cinturón», no piensas en un cinturón: entiendes que habrá que gastar menos. Interpretar es explicar qué significa algo y por qué lo piensas.",
        "Un resumen cuenta lo que pasa en el texto, de forma breve. Una interpretación va más allá: dice qué significa lo que pasa y lo apoya con datos del texto. Resumir responde «¿qué ocurre?»; interpretar responde «¿qué significa y cómo lo sé?».",
        "Una interpretación válida no es cualquier opinión. Debe apoyarse en lo que el texto dice o muestra. Si dices que la llave representa la responsabilidad, debes señalar qué dato lo sugiere, como la mirada larga de Camilo o la frase de don Mario.",
    ],
    vocab=[("resumen", "texto breve que cuenta lo principal sin explicar su sentido"), ("interpretación", "explicación de lo que significa un texto, apoyada en datos"), ("significar", "querer decir o representar algo"), ("dato del texto", "información que está escrita en el texto")],
    worked=[
        ("Distinguir resumen e interpretación", "Texto A: don Mario da la llave a Camilo, que abre al día siguiente. Texto B: la llave representa la responsabilidad.", ["A cuenta lo que ocurre: es un resumen.", "B explica qué significa la llave: es una interpretación."], "A resume y B interpreta"),
        ("Apoyar una interpretación", "Idea: la llave representa la responsabilidad. Dato: Camilo se quedó un rato mirando la llave.", ["El dato muestra que Camilo da importancia a la llave.", "Eso apoya que lo que recibe es más que un objeto."], "El dato respalda la interpretación"),
    ],
    mistakes=[("Entregar un resumen cuando piden interpretar.", "El resumen cuenta qué pasa, pero no dice qué significa.", "Agrega una frase: «esto representa…» o «esto muestra…» y un dato."),
              ("Decir una interpretación que el texto contradice.", "La interpretación debe estar de acuerdo con lo que dice el texto.", "Compara tu idea con los datos del relato.")],
    T=[
        ("abc", "{F} ¿Cuál texto es un resumen?", "El Texto A", "El Texto B", "Ninguno", "El Texto A solo cuenta lo que ocurre."),
        ("abc", "{F} ¿Cuál texto es una interpretación?", "El Texto B", "El Texto A", "Ninguno", "El Texto B dice qué representa la llave."),
        ("abc", "{F} ¿Qué objeto se interpreta como símbolo en el relato?", "La llave", "El taller", "La puerta", "El Texto B interpreta la llave como responsabilidad."),
        ("{F} ¿Cuántos años atendió don Mario su taller? Escribe el número.", "30", "El relato dice que atendió el taller durante treinta años."),
        ("ab", "En Lengua y Literatura: ¿qué hace un resumen?", "Cuenta lo principal sin explicar su sentido", "Explica el significado con datos", "Un resumen informa de lo que pasa; no interpreta."),
        ("abc", "En Lengua y Literatura: ¿qué hace una interpretación?", "Explica qué significa el relato y lo apoya con datos del texto", "Copia el texto completo", "Cuenta el final", "Una interpretación va más allá del resumen y se apoya en el texto."),
        ("abc", "{F} ¿Qué dato del relato apoya que la llave es importante para Camilo?", "Camilo se quedó un rato mirando la llave", "Don Mario tiene un taller", "El taller es mecánico", "La mirada larga muestra que la llave le importa."),
        ("abc", "{F} ¿Cuál es otra interpretación posible y apoyada en el texto?", "La llave muestra la confianza de don Mario en Camilo", "La llave muestra que don Mario odia a Camilo", "La llave es de oro", "Don Mario le entrega la llave y le dice «ahora la abres tú»."),
        ("ab", "{F} Pedro dice: «La llave significa que Camilo robó el taller». ¿Se apoya en el texto?", "No: el relato muestra que don Mario se la entrega", "Sí: Camilo tiene la llave", "Una interpretación no puede contradecir lo que el relato cuenta."),
        ("abc", "{F} Camilo llegó una hora antes y abrió despacio. ¿Qué sugiere este dato?", "Que se toma en serio su nueva responsabilidad", "Que no quiere trabajar", "Que olvidó la llave", "Llegar antes y abrir despacio muestra cuidado."),
        ("abc", "¿En qué debe apoyarse siempre una interpretación?", "En datos del texto", "En el título más largo", "En lo que opina otra persona sin explicar", "Los datos del texto dan firmeza a la interpretación."),
        ("ab", "{F} Rita escribe: «Don Mario le da la llave a Camilo». ¿Eso es resumir o interpretar?", "Resumir, porque solo cuenta lo que ocurre", "Interpretar, porque da una opinión", "No dice qué significa la acción, solo la cuenta."),
        ("abc", "{F} ¿Qué frase convertiría un resumen en una interpretación?", "«Esto representa la responsabilidad que pasa de uno a otro»", "«Esto ocurre en un taller»", "«Esto pasa durante treinta años»", "Dice qué representa la acción y no solo qué ocurre."),
    ],
    ctx=("abc", "En una oficina alguien de la jefatura dice: «Las puertas de esta empresa siempre están abiertas». Después, una persona explica: «Quiere decir que podemos hablar con ella cuando queramos». ¿Qué hizo esa persona?", "Interpretó la frase y dijo qué significa", "Resumió el relato", "Copió la frase", "Explicó el significado de una expresión, que es interpretar."),
    sc=[("En Lengua y Literatura: ¿qué es interpretar?", "Explicar qué significa algo y por qué lo pienso", "Una interpretación se apoya en datos."),
        ("¿Qué diferencia hay entre resumir e interpretar?", "Resumir cuenta qué pasa; interpretar dice qué significa", "La interpretación agrega el sentido que el resumen no explica."),
        ("¿Qué necesito para sostener una interpretación?", "Un dato del texto", "El dato muestra que la idea sale del texto.")],
    op=("Lee el relato de la ficha y escribe en tu cuaderno dos oraciones: una que resuma lo que pasa y una que interprete qué representa la llave, con un dato del texto. {F}",
        "Resumen: don Mario le entrega la llave a Camilo y este abre al día siguiente. Interpretación: la llave representa la confianza que don Mario deposita en Camilo, porque le dice «ahora la puerta la abres tú».",
        ["una oración resume", "una oración interpreta", "la interpretación usa un dato del texto"],
        ["dos oraciones escritas"],
        ["escribir dos resúmenes", "interpretar sin dato"],
        "Pregunta: «¿Qué frase del relato te hizo pensar eso?»."),
    reinforce="Elige una frase de tu vida diaria que no se entienda al pie de la letra y explica qué significa.",
    extend="Escribe una segunda interpretación de la llave y compárala con la primera con un dato del relato.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo las palabras para escribir una interpretación: tesis, evidencia textual, cita, paráfrasis y conectores.",
    prior=["Distingo resumen e interpretación.", "Apoyo una idea con un dato del texto.", "Sé usar palabras como «porque»."],
    explain=[
        "Una interpretación escrita tiene tres partes. La tesis es la idea principal que defiendes, por ejemplo qué representa un símbolo. La evidencia textual son los datos del relato que la apoyan. La explicación dice por qué esa evidencia apoya tu idea.",
        "Hay dos maneras de usar el texto. La cita copia palabras del texto entre comillas. La paráfrasis cuenta lo mismo con otras palabras. Puedes usar las dos, pero siempre debes decir qué parte del texto usas.",
        "Los conectores unen las ideas y ayudan a leer. «Porque» da una razón, «además» agrega otra, «sin embargo» marca una diferencia y «por eso» cierra una conclusión. Una buena interpretación los usa para que se note el hilo de tus ideas.",
    ],
    vocab=[("tesis", "idea principal que defiendes en un texto"), ("evidencia textual", "dato o frase del texto que apoya tu idea"), ("paráfrasis", "decir con otras palabras lo que dice el texto"), ("conector", "palabra que une ideas, como «porque» o «además»")],
    worked=[
        ("Reconocer las partes", "«La silla vacía representa la esperanza de que Tomás vuelva. Esto se ve cuando doña Julia dice que la casa «sabe que alguien viene».»", ["Tesis: la silla vacía representa la esperanza.", "Evidencia: la frase de doña Julia.", "Conector: «esto se ve cuando»."], "Tesis, evidencia y conector identificados"),
        ("Parafrasear", "Frase del relato: «La mesa se pone completa; así la casa sabe que alguien viene».", ["Cambio las palabras, pero no el sentido.", "Escribo: «Doña Julia deja la mesa completa para que el hogar espere a alguien»."], "Paráfrasis fiel a la frase"),
    ],
    mistakes=[("Poner una cita sin comillas.", "Sin comillas parece que las palabras son tuyas.", "Escribe las palabras exactas entre comillas."),
              ("Cambiar el sentido al parafrasear.", "La paráfrasis debe decir lo mismo con otras palabras.", "Compara tu frase con la original.")],
    T=[
        ("abc", "{F} ¿Cuál es la tesis de la interpretación de ejemplo?", "La silla vacía representa la esperanza de que Tomás vuelva", "Doña Julia pone la mesa", "Elsa deja pan para tres", "Es la idea principal que el ejemplo defiende."),
        ("abc", "{F} ¿Qué frase entre comillas se usa como cita de evidencia?", "«sabe que alguien viene»", "«dos años»", "«ya no es necesario poner el plato de Tomás»", "La cita copia palabras de doña Julia."),
        ("{F} ¿Cuántos platos pone doña Julia cada noche? Escribe el número.", "3", "El relato dice que pone la mesa para tres."),
        ("ab", "En Lengua y Literatura: ¿qué es una paráfrasis?", "Decir con otras palabras lo que dice el texto", "Copiar el texto entre comillas", "La paráfrasis cambia las palabras, no el sentido."),
        ("abc", "{F} ¿Qué conector agrega una segunda evidencia en la interpretación de ejemplo?", "Además", "Porque", "Sin embargo", "«Además» suma otro dato a lo ya dicho."),
        ("abc", "{F} ¿Qué función cumple la frase «Esto se ve cuando…»?", "Presentar la evidencia que apoya la tesis", "Cerrar el texto", "Copiar un título", "Introduce el dato que sostiene la idea."),
        ("abc", "En Lengua y Literatura: ¿qué es la evidencia textual?", "Un dato o frase del texto que apoya tu idea", "Una opinión sin base", "El título del libro", "La evidencia textual sale del texto."),
        ("ab", "{F} «Doña Julia pone la mesa para tres». ¿Es tesis o evidencia?", "Evidencia: es un dato del relato", "Tesis: es la idea principal", "Es un dato que sirve para apoyar una idea."),
        ("abc", "{F} ¿Qué evidencia apoya que la esperanza se comparte?", "Elsa deja pan para tres", "Tomás trabaja en el norte", "Doña Julia pone la mesa", "Elsa copia el gesto, lo que muestra que la esperanza se comparte."),
        ("abc", "¿Qué conector sirve mejor para cerrar una interpretación?", "Por eso", "Además", "Sin embargo", "El conector «por eso» introduce la conclusión de lo dicho antes."),
        ("abc", "{F} ¿Cuál es una paráfrasis fiel de la frase de doña Julia?", "Deja la mesa completa para que la casa espere a alguien", "Dice que la casa está vacía y sin esperanza", "Pide que Tomás regrese hoy", "Mantiene el sentido de la frase original."),
        ("ab", "{F} Un compañero dice: «La silla vacía representa que Tomás murió». ¿Se apoya en el texto?", "No: el relato dice que Tomás trabaja en el norte y que «alguien viene»", "Sí: la silla está vacía", "El texto habla de esperar, no de muerte."),
        ("abc", "{F} ¿Qué parte de la interpretación de ejemplo explica el símbolo?", "La primera oración, que dice qué representa la silla", "La segunda, que presenta una cita", "La tercera, que habla de pan", "La primera oración dice qué representa el símbolo."),
    ],
    ctx=("abc", "En una carta formal escribes: «Pido más plazo porque me falta una fuente; además, quiero revisar el trabajo con calma». ¿Qué conectores usaste?", "«Porque» y «además»", "«Sin embargo» y «por eso»", "Ninguno", "«Porque» da una razón y «además» agrega otra."),
    sc=[("En Lengua y Literatura: ¿qué es una tesis?", "La idea principal que defiendes", "La tesis guía todo lo que escribes."),
        ("¿Cuál es la diferencia entre cita y paráfrasis?", "La cita copia con comillas; la paráfrasis lo dice con otras palabras", "Las dos usan el texto, pero de distinto modo."),
        ("En Lengua y Literatura: ¿para qué sirven los conectores al escribir una interpretación?", "Para unir ideas y mostrar su relación", "Marcan razones, sumas, diferencias y cierres.")],
    op=("Con el relato de la ficha, escribe una tesis sobre qué representa la mesa puesta y una evidencia, usando una cita entre comillas. Después escribe la misma evidencia como paráfrasis. {F}",
        "Tesis: la mesa puesta representa la esperanza del regreso. Cita: doña Julia dice «así la casa sabe que alguien viene». Paráfrasis: ella deja la mesa completa para que la casa espere a alguien.",
        ["una tesis clara", "una cita con comillas", "una paráfrasis fiel"],
        ["tres oraciones escritas"],
        ["cita sin comillas", "paráfrasis que cambia el sentido"],
        "Pregunta: «¿Qué palabras son del texto y cuáles son tuyas?»."),
    reinforce="Elige una frase de una conversación y escríbela como cita y como paráfrasis.",
    extend="Escribe cuatro conectores nuevos y una oración con cada uno.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo paso a paso cómo pasar de una ficha de análisis intertextual a un párrafo interpretativo.",
    prior=["Reconozco tesis, evidencia y conector.", "Sé hacer una ficha de personajes, tema y símbolo.", "Sé que una interpretación se apoya en el texto."],
    explain=[
        "Para escribir una interpretación a partir de un análisis intertextual sigue cinco pasos. Paso 1: lee tu ficha de análisis. Paso 2: decide una idea central, tu tesis. Paso 3: elige dos evidencias de los textos. Paso 4: escribe el párrafo. Paso 5: revísalo.",
        "El párrafo tiene cuatro partes: la tesis, la primera evidencia con su explicación, la segunda evidencia con su explicación y un cierre. En el cierre dices qué relación hay con la otra obra y qué cambia en el texto nuevo.",
        "La relación con la otra obra debe estar explicada con datos de ambos textos. No basta con decir que «se parece a la Odisea»: señala qué personaje, tema o símbolo se repite y qué dato lo muestra.",
    ],
    vocab=[("ficha de análisis", "tabla con personajes, tema y símbolo de dos obras"), ("idea central", "lo más importante que quieres decir"), ("cierre", "última parte del párrafo que resume la idea"), ("revisión", "relectura para corregir un texto")],
    worked=[
        ("Elegir la tesis desde la ficha", "Ficha: tema, la espera de un regreso; símbolo, la mesa puesta.", ["Elijo el símbolo, porque es lo que el relato muestra.", "Escribo la tesis: la mesa puesta mantiene viva la espera, como la tela de Penélope."], "Tesis apoyada en la ficha"),
        ("Armar el párrafo", "Tesis: la mesa puesta mantiene viva la espera. Evidencia 1: la frase de doña Julia. Evidencia 2: Elsa deja pan para tres.", ["Escribo la tesis.", "Agrego cada evidencia con «porque» y «además».", "Cierro con la relación con la Odisea."], "Párrafo con tesis, dos evidencias y cierre"),
    ],
    mistakes=[("Escribir solo la tesis sin evidencias.", "Una tesis sin datos es una opinión.", "Agrega al menos dos evidencias del texto."),
              ("Decir «se parece a la Odisea» sin explicar en qué.", "La relación debe mostrar qué se repite y con qué dato.", "Nombra el personaje o símbolo y el dato de cada obra.")],
    T=[
        ("abc", "{F} ¿Qué personaje de la Odisea cumple el papel de doña Julia según la ficha?", "Penélope, quien espera", "Ulises, el ausente", "Un pretendiente", "La ficha dice que doña Julia cumple el papel de quien espera."),
        ("abc", "{F} ¿Qué tema une los dos textos según la ficha?", "La espera de un regreso", "La ambición de poder", "El miedo al mar", "La ficha anota la espera de un regreso."),
        ("{F} ¿Cuántos años lleva Tomás en el norte? Escribe el número.", "2", "El relato dice que trabaja en el norte desde hace dos años."),
        ("abc", "{F} ¿Qué elemento del relato cumple la función de la tela de Penélope?", "La mesa puesta", "El pan", "La carta", "La ficha dice que la mesa, como la tela, mantiene viva la espera."),
        ("ab", "{F} ¿Cuál es una buena tesis para el párrafo?", "La mesa puesta mantiene viva la espera, como la tela que Penélope teje y deshace", "Doña Julia vive en una casa", "Una buena tesis dice qué representa el símbolo y lo relaciona con la otra obra."),
        ("abc", "En Lengua y Literatura: ¿qué paso va después de elegir la tesis?", "Elegir dos evidencias de los textos", "Escribir el título", "Borrar la ficha", "Los pasos son lectura de la ficha, tesis, evidencias, párrafo y revisión."),
        ("abc", "{F} ¿Cuál es la mejor primera evidencia de un párrafo sobre la mesa puesta?", "La frase «así la casa sabe que alguien viene»", "El dato de que Tomás trabaja en el norte", "La palabra «tres»", "La frase muestra que el gesto mantiene viva la espera."),
        ("abc", "{F} ¿Qué evidencia apoya que el gesto se contagia?", "Elsa también deja pan para tres", "Doña Julia está sola", "Tomás vive lejos", "El gesto de Elsa muestra que se comparte."),
        ("abc", "{F} ¿Qué diferencia entre la obra y el relato puede ir en el cierre?", "Doña Julia no es presionada por pretendientes y no se sabe si Tomás vuelve", "Ambos ocurren en una isla", "En ambos el hijo regresa", "La ficha de análisis anota esas dos diferencias entre las obras."),
        ("ab", "¿Qué parte del párrafo explica por qué una evidencia apoya la tesis?", "La explicación que sigue a cada evidencia", "El título", "Un párrafo no puede quedar solo con datos: necesita explicar su relación con la tesis."),
        ("abc", "¿Qué conector es adecuado para agregar la segunda evidencia?", "Además", "Por lo tanto", "A pesar de eso", "«Además» suma otro dato a la idea."),
        ("abc", "{F} ¿Qué cierre sería adecuado?", "Por eso, el relato recuerda a la Odisea, aunque cambia que no se sabe si Tomás vuelve", "Es un cuento bonito", "Doña Julia vive en el norte", "Relaciona con la otra obra y marca lo que cambia."),
        ("ab", "{F} Marcos escribe solo: «El relato se parece a la Odisea». ¿Está completo su párrafo?", "No: falta explicar en qué se parece con datos de ambos textos", "Sí: ya nombró la obra", "Falta señalar personajes, tema o símbolo y los datos que lo muestran."),
    ],
    ctx=("abc", "En el club de lectura te piden escribir una interpretación para el boletín del centro. Ya tienes la ficha. ¿Qué haces primero?", "Decido mi idea central a partir de la ficha", "Escribo el cierre", "Elijo el título del boletín", "La tesis se define antes que las evidencias y el párrafo."),
    sc=[("¿Cuántos pasos tiene la escritura de hoy?", "Cinco", "Lectura de la ficha, tesis, evidencias, párrafo y revisión."),
        ("En Lengua y Literatura: ¿qué partes tiene el párrafo interpretativo?", "Tesis, dos evidencias explicadas y cierre", "El párrafo reúne idea, datos y conclusión."),
        ("¿Qué debe decir el cierre?", "La relación con la otra obra y qué cambia", "El cierre muestra la mirada propia del texto nuevo.")],
    op=("Con la ficha de la clase, escribe un párrafo de seis oraciones: una tesis, dos evidencias explicadas con conectores y un cierre que diga la relación con la Odisea y qué cambia. {F}",
        "La mesa puesta mantiene viva la espera, como la tela de Penélope. Doña Julia dice que así «la casa sabe que alguien viene», lo que muestra que no abandona la esperanza. Además, Elsa deja pan para tres, porque el gesto se comparte. Por eso, el relato recuerda a la Odisea. Cambia que no hay pretendientes. Tampoco se sabe si Tomás vuelve.",
        ["tesis clara", "dos evidencias explicadas", "usa conectores", "cierre con relación y diferencia"],
        ["un párrafo de seis oraciones"],
        ["no explicar las evidencias", "no decir qué cambia"],
        "Pregunta: «¿Qué dato de cada obra apoya tu idea?»."),
    reinforce="Haz una ficha de personaje, tema y símbolo para un relato que conozcas.",
    extend="Escribe un segundo párrafo con otra tesis sobre el mismo relato.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: distingo resumen e interpretación, elijo evidencias y corrijo un párrafo débil sobre un relato que dialoga con Cenicienta.",
    prior=["Sé armar un párrafo interpretativo.", "Sé usar una cita y una paráfrasis.", "Sé usar conectores."],
    explain=[
        "Practicamos con un relato nuevo que recuerda a Cenicienta. En Cenicienta, un zapato permite reconocer a una joven que nadie veía. En «El zapato de Mónica», el zapato hace que el gerente reconozca a una trabajadora de aseo y su aporte.",
        "Para interpretar, mira qué representa el objeto. El zapato es una huella de la persona: lo que se deja, lo que permite reconocerla. Y mira qué cambia: en el relato nuevo no hay magia y el reconocimiento llega por el trabajo, no por la belleza.",
        "Al elegir evidencias, escoge datos que prueben tu idea, no cualquier dato. «Mónica limpia oficinas» es un dato, pero solo sirve si se relaciona con la tesis. Revisa siempre que la evidencia responda: «¿cómo prueba esto mi idea?».",
    ],
    vocab=[("huella", "señal que deja alguien al pasar"), ("reconocimiento", "hecho de valorar o identificar a alguien"), ("trabajo invisible", "labor que casi nadie nota"), ("evidencia relevante", "dato que sí prueba la idea")],
    worked=[
        ("Elegir la evidencia relevante", "Tesis: el zapato representa el reconocimiento del trabajo de Mónica. Datos: (a) Mónica limpia oficinas; (b) don Esteban le agradece los adornos.", ["El dato (b) muestra el reconocimiento.", "El dato (a) no prueba la idea por sí solo."], "Dato (b) como evidencia"),
        ("Corregir un resumen", "Texto débil: «Mónica deja un zapato y el gerente lo encuentra».", ["Es un resumen: no dice qué significa.", "Agrego: «El zapato representa la huella de una trabajadora que nadie veía»."], "Interpretación con tesis"),
    ],
    mistakes=[("Elegir como evidencia un dato que no prueba la idea.", "La evidencia debe responder cómo apoya la tesis.", "Pregunta: «¿cómo prueba esto mi idea?»."),
              ("Decir que el zapato «es» el amor.", "Ese significado no está en el relato.", "Interpreta solo con lo que el texto muestra.")],
    T=[
        ("abc", "{F} ¿Con qué cuento tradicional dialoga «El zapato de Mónica»?", "Cenicienta", "Caperucita Roja", "Pinocho", "El resumen propio de Cenicienta menciona el zapato que permite reconocerla."),
        ("abc", "{F} ¿Qué objeto se repite en los dos textos?", "Un zapato", "Una llave", "Una tela", "Ambos textos giran en torno a un zapato."),
        ("{F} ¿Cómo se llama el gerente? Escribe una palabra.", "Esteban", "El relato dice que se llama don Esteban."),
        ("abc", "{F} ¿Qué diferencia hay entre los dos textos?", "En el relato nuevo no hay magia y el reconocimiento llega por el trabajo", "En ambos hay magia", "En ambos el gerente pregunta", "El resumen de Cenicienta incluye ayuda mágica; el relato nuevo, no."),
        ("ab", "{F} ¿Qué representa el zapato de Mónica?", "La huella de una trabajadora que nadie veía", "Un regalo caro", "El texto muestra que el zapato permite que la reconozcan y valoren su trabajo."),
        ("abc", "{F} ¿Qué dato prueba mejor que Mónica es reconocida?", "Don Esteban le agradece los adornos", "Mónica limpia las oficinas", "La fiesta es de aniversario", "El agradecimiento y la invitación al comité muestran reconocimiento."),
        ("abc", "{F} Texto débil: «Mónica deja un zapato y el gerente lo encuentra». ¿Qué le falta?", "Una frase que diga qué significa el zapato", "Más palabras copiadas", "El nombre del autor", "Es un resumen: falta la interpretación."),
        ("abc", "{F} ¿Cuál es una tesis adecuada?", "El zapato representa el reconocimiento de un trabajo que nadie veía", "El zapato es muy bonito", "La fiesta fue de aniversario", "Dice qué representa el objeto y se apoya en el texto."),
        ("ab", "{F} Vivi dice: «El zapato significa que Mónica se enamora del gerente». ¿Se apoya en el texto?", "No: el relato muestra agradecimiento, no amor", "Sí: se encuentran", "No hay ningún dato de amor, solo de reconocimiento de su trabajo."),
        ("abc", "{F} ¿Qué conector completa la oración «El zapato representa el reconocimiento ___ don Esteban le agradece los adornos»?", "Porque", "Sin embargo", "En conclusión", "«Porque» introduce la razón de lo que se afirma."),
        ("abc", "{F} ¿Qué hace el gerente que cambia la situación de Mónica?", "La invita a participar en el comité de eventos", "La despide", "No hace nada", "La invitación muestra que su aporte fue valorado."),
        ("abc", "En Lengua y Literatura: ¿qué es una evidencia relevante?", "Un dato que sí prueba la idea que defiendo", "Cualquier dato del texto", "Una opinión de otra persona", "La evidencia relevante responde cómo apoya la tesis."),
        ("ab", "{F} ¿Qué diferencia hay en cómo se reconoce a los personajes?", "En el relato nuevo, por el trabajo que hizo", "En ambos, por su belleza", "El relato dice que don Esteban le agradece los adornos, es decir, su trabajo."),
    ],
    ctx=("abc", "Una compañera dice que su jefe nunca nota su trabajo hasta que un día le agradece frente a todos. Si lo relacionas con el relato, ¿qué puedes decir?", "Que se parece al reconocimiento de Mónica, aunque no hay un zapato", "Que es idéntico a Cenicienta", "Que no tiene relación con nada", "Se parece en el tema del reconocimiento, pero cambia el objeto."),
    sc=[("En Lengua y Literatura: ¿qué es una evidencia relevante?", "Un dato que prueba mi idea", "No cualquier dato sirve: debe apoyar la tesis."),
        ("¿Qué representa el zapato en el relato de Mónica?", "La huella de una trabajadora que nadie veía", "El zapato permite que el gerente la reconozca y valore."),
        ("¿Qué cambia respecto de Cenicienta?", "No hay magia", "El reconocimiento llega por el trabajo, no por la ayuda mágica.")],
    op=("Escribe un párrafo de cinco oraciones sobre «El zapato de Mónica»: tesis, dos evidencias, relación con Cenicienta y una diferencia. {F}",
        "El zapato representa el reconocimiento de una trabajadora que nadie veía. Esto se ve cuando don Esteban le agradece los adornos. Además, la invita al comité de eventos. Como en Cenicienta, un zapato permite reconocer a alguien. Pero en el relato no hay magia: el reconocimiento viene del trabajo.",
        ["tesis clara", "dos evidencias relevantes", "relación con Cenicienta", "una diferencia"],
        ["un párrafo de cinco oraciones"],
        ["evidencias que no prueban la idea", "no mencionar qué cambia"],
        "Pregunta: «¿Cómo prueba tu dato la idea?»."),
    reinforce="Escribe una oración que interprete el objeto más importante de un relato que conozcas.",
    extend="Reescribe el cierre del relato de Mónica con otra decisión de don Esteban y di qué cambiaría.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico la interpretación a un dilema: dos personajes que deben elegir entre una orden y la solidaridad.",
    prior=["Sé escribir una interpretación con tesis y evidencias.", "Sé relacionar un relato con una obra clásica.", "Conozco situaciones en que hay que elegir entre dos cosas importantes."],
    explain=[
        "Un dilema es una situación en que una persona debe elegir entre dos deberes o valores que chocan, y cualquier decisión tiene un costo. En Antígona, ella debe elegir entre obedecer la orden del rey y cumplir con enterrar a su hermano.",
        "En «La orden de la bodega», Nora debe elegir entre cumplir la orden de su jefe y ayudar a su compañero. Los dos casos tienen un conflicto entre una autoridad y la solidaridad, aunque ocurren en mundos muy distintos.",
        "Al interpretar un dilema no se trata de decir quién tiene razón, sino de explicar qué valores chocan, qué decide cada personaje y qué consecuencias asume. Tu interpretación debe apoyarse en datos de ambos textos, sin juzgar a las personas.",
    ],
    vocab=[("dilema", "situación en que hay que elegir entre dos deberes o valores que chocan"), ("valor", "idea que una persona considera importante, como la solidaridad"), ("autoridad", "persona que puede dar órdenes"), ("consecuencia", "lo que ocurre como resultado de una decisión")],
    worked=[
        ("Reconocer qué valores chocan", "Nora: la orden del jefe frente a la necesidad de Iván.", ["Un valor es obedecer la orden.", "Otro valor es ayudar a un compañero.", "No se pueden cumplir los dos al mismo tiempo."], "Dilema entre obediencia y solidaridad"),
        ("Comparar decisiones", "Antígona entierra al hermano aun sabiendo que será castigada; Nora abre y escribe un informe.", ["Ambas desobedecen una orden.", "Ambas asumen una consecuencia.", "Nora lo informa a su jefe a primera hora."], "Se parecen en desobedecer y asumir consecuencias; cambia la gravedad y cómo la enfrentan"),
    ],
    mistakes=[("Decir quién es «bueno» y quién «malo» en vez de interpretar.", "El dilema muestra valores que chocan; no se trata de juzgar.", "Explica qué valores chocan y qué consecuencias asumen."),
              ("Olvidar la consecuencia que asume el personaje.", "Un dilema tiene siempre un costo.", "Señala qué pierde o qué arriesga cada personaje.")],
    T=[
        ("abc", "{F} ¿Qué orden recibe Nora?", "No abrir el local fuera de horario", "Entregar una carpeta", "Escribir un informe", "El relato dice que su jefe le ordenó no abrir el local fuera de horario."),
        ("abc", "{F} ¿Qué necesita Iván?", "La carpeta con sus papeles para un trámite", "Un permiso de vacaciones", "Una llave del jefe", "Dejó los papeles en su casillero."),
        ("{F} ¿A qué hora lo llama Iván? Escribe el número de la hora.", "10", "El relato dice que lo llama a las diez de la noche."),
        ("ab", "{F} ¿Qué valores chocan en el dilema de Nora?", "Obedecer la orden y ayudar a un compañero", "Ganar dinero y descansar", "Una orden frente a una necesidad de un compañero: ambas importan a Nora."),
        ("abc", "En Lengua y Literatura: ¿qué es un dilema?", "Una situación en que hay que elegir entre dos deberes o valores que chocan", "Una orden escrita por una jefatura", "Un resumen de una obra", "Un dilema exige elegir y cada opción tiene un costo."),
        ("abc", "{F} ¿Qué orden desobedece Antígona?", "La de Creonte, que prohíbe enterrar a Polinices", "La de su hermano", "La de Nora", "El resumen dice que Creonte prohíbe enterrarlo."),
        ("abc", "{F} ¿En qué se parecen Antígona y Nora?", "Ambas desobedecen una orden por un valor que consideran importante", "Ambas son reinas", "Ambas trabajan en una bodega", "Las dos eligen contra una orden y asumen consecuencias."),
        ("abc", "{F} ¿Qué cambia entre las dos decisiones?", "Antígona sabe que será castigada; Nora informa a su jefe", "Ambas deciden no hacer nada", "Ambas son aprobadas por la autoridad", "Los textos muestran distintas formas de enfrentar las consecuencias."),
        ("abc", "{F} ¿Qué dato muestra que Nora asume una consecuencia?", "Escribe un informe para su jefe explicando lo que hizo", "Abre la bodega a escondidas sin decir nada", "Deja la carpeta donde está y no hace nada", "El informe muestra que responde por su decisión."),
        ("ab", "{F} Pedro dice: «Nora es mala porque desobedece». ¿Es una buena interpretación?", "No: juzga a la persona y no explica los valores en conflicto", "Sí: desobedece a su jefe", "Interpretar es explicar qué valores chocan, no juzgar."),
        ("abc", "{F} ¿Cuál es una tesis adecuada para interpretar el dilema de Nora?", "Nora elige la solidaridad con su compañero sin ocultar su decisión", "Nora es la mejor trabajadora del mundo", "El jefe tiene la razón siempre", "Dice qué valor elige y se apoya en el relato."),
        ("abc", "{F} ¿Qué evidencia apoya que Nora no oculta su decisión?", "Escribirá un informe a primera hora", "Piensa en las consecuencias", "Iván la llama a las diez", "El informe muestra que decide sin esconder lo hecho."),
        ("ab", "{F} ¿Cuál es la diferencia de lugar y época entre ambas obras?", "Una obra antigua en Tebas y un relato actual en una bodega", "Ambas ocurren en una bodega moderna", "Antígona ocurre en una ciudad antigua; el relato nuevo, en un trabajo actual."),
    ],
    ctx=("abc", "En una bodega o en un trámite te piden cumplir una norma, pero una persona necesita ayuda urgente que la norma impide. ¿Qué haces al interpretar la situación como un dilema?", "Identifico qué valores chocan y qué consecuencias tiene cada opción", "Juzgo quién es culpable", "Ignoro a mi compañero", "Un dilema se analiza mirando los valores y las consecuencias."),
    sc=[("En Lengua y Literatura: ¿qué es un dilema?", "Una elección entre dos deberes que chocan", "En un dilema cada opción tiene un costo para quien elige."),
        ("¿Se trata de decir quién tiene la razón?", "No: se explica qué valores chocan", "Se interpretan valores y consecuencias, no se juzga."),
        ("¿Qué consecuencia asume Nora?", "Responde ante su jefe con un informe", "Escribirlo muestra que asume su decisión.")],
    op=("Escribe un párrafo de seis oraciones que interprete el dilema de Nora en relación con Antígona: tesis, dos evidencias, una semejanza y una diferencia. {F}",
        "Nora y Antígona deben elegir entre una orden y la solidaridad. Nora decide abrir porque Iván necesita sus papeles. Además, escribirá un informe, lo que muestra que asume su decisión. Como Antígona, desobedece una orden por un valor importante. Pero Antígona sabe que será castigada, mientras Nora informa. Por eso, el relato actualiza el dilema.",
        ["tesis sobre los valores en conflicto", "dos evidencias", "una semejanza y una diferencia con Antígona", "no juzga"],
        ["un párrafo de seis oraciones"],
        ["juzgar a los personajes", "no incluir diferencia"],
        "Pregunta: «¿Qué valores chocan y cómo lo muestra el texto?»."),
    reinforce="Anota un dilema que hayas visto en tu entorno, sin nombres, y los dos valores que chocan.",
    extend="Escribe un final distinto para Nora, en que obedece la orden, y di qué consecuencias tendría.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso una interpretación con una pauta, la corrijo y decido qué mejorar en mis textos.",
    prior=["Sé escribir una interpretación con tesis y evidencias.", "Sé usar conectores y citas.", "Sé relacionar un relato con otra obra."],
    explain=[
        "Revisar es leer tu texto como si fuera de otra persona. Usa una pauta con criterios claros: tesis, evidencias, explicación, conectores, relación con la otra obra y cierre. Marca cuáles cumple y cuáles faltan.",
        "Un texto que solo cuenta lo que pasa es un resumen. Para convertirlo en interpretación, agrega una tesis, elige dos evidencias y explica cada una. Después revisa la ortografía básica: punto al final, mayúscula al comienzo y tildes en palabras clave.",
        "Terminada la revisión, decide el siguiente paso. Si falta la tesis, escríbela. Si faltan evidencias, vuelve al texto. Si falta la relación con la otra obra, revisa tu ficha. Revisar no es castigo: es la parte de la escritura que más la mejora.",
    ],
    vocab=[("pauta", "lista de criterios para revisar un texto"), ("revisar", "leer de nuevo para corregir"), ("ortografía", "forma correcta de escribir las palabras"), ("voz propia", "manera personal de expresar una idea")],
    worked=[
        ("Aplicar la pauta", "Texto de Gloria: solo cuenta lo que pasa y termina con «Es un cuento bonito».", ["No tiene tesis.", "No tiene evidencias explicadas.", "No relaciona con la Odisea.", "El cierre es solo una opinión."], "Cumple 0 de 6 criterios: es un resumen"),
        ("Mejorar el texto", "Texto mejorado: «La mesa puesta representa la esperanza del regreso, como la tela de Penélope. Doña Julia dice que así «la casa sabe que alguien viene»».", ["Agrego tesis.", "Agrego evidencia con comillas.", "Relaciono con Penélope."], "Texto con tesis, evidencia y relación"),
    ],
    mistakes=[("Corregir solo la ortografía y dejar un resumen.", "La ortografía no cambia el tipo de texto.", "Revisa primero la tesis y las evidencias."),
              ("Cerrar con una opinión suelta como «es bonito».", "Una opinión sin datos no cierra una interpretación.", "Cierra con la relación con la otra obra y una diferencia.")],
    T=[
        ("abc", "{F} ¿Qué tipo de texto es el de Gloria?", "Un resumen", "Una interpretación completa", "Una cita", "Solo cuenta lo que pasa, sin tesis."),
        ("abc", "{F} ¿Cuántos criterios tiene la pauta de revisión?", "Seis", "Tres", "Diez", "La pauta de revisión anota seis criterios, numerados del 1 al 6."),
        ("{F} ¿Cuántos criterios de la pauta cumple el texto de Gloria? Escribe el número.", "0", "No tiene tesis, evidencias explicadas, conectores, relación ni cierre."),
        ("abc", "{F} ¿Qué criterio falta primero en el texto de Gloria?", "Una tesis clara", "La letra grande", "El título", "Sin tesis no hay idea que defender."),
        ("abc", "{F} ¿Qué frase convertiría el texto de Gloria en una tesis?", "La mesa puesta representa la esperanza del regreso, como la tela de Penélope", "Es un cuento bonito", "Elsa deja pan", "Dice qué representa el símbolo y lo relaciona con la Odisea."),
        ("ab", "{F} ¿Qué evidencia podría agregar Gloria?", "La frase de doña Julia: «así la casa sabe que alguien viene»", "El nombre del autor", "Es una frase del relato que muestra la esperanza."),
        ("abc", "{F} ¿Qué criterio incumple la frase final «Es un cuento bonito»?", "El cierre con una conclusión apoyada en datos", "El uso de comillas", "La ortografía", "Una opinión suelta no cierra una interpretación."),
        ("abc", "En Lengua y Literatura: ¿qué es una pauta?", "Una lista de criterios para revisar un texto", "Un resumen largo", "Un título para el texto", "La pauta ordena lo que hay que revisar."),
        ("abc", "{F} ¿Qué relación con la Odisea puede agregar Gloria?", "Doña Julia cumple el papel de Penélope, que espera y cuida la casa", "Doña Julia es un pretendiente", "Elsa es Ulises", "Ambas esperan a alguien lejano y cuidan la casa."),
        ("ab", "Marcela corrige solo las tildes de su texto sin tesis. ¿Mejoró su interpretación?", "No: sigue sin tesis ni evidencias", "Sí: ya está completa", "La ortografía ayuda, pero no reemplaza las ideas ni las evidencias."),
        ("abc", "¿Qué haces si falta la relación con la otra obra?", "Vuelvo a mi ficha de análisis", "Borro el texto", "Agrego un dibujo", "La ficha indica personajes, tema y símbolo que se relacionan."),
        ("abc", "¿Qué orden conviene al revisar?", "Primero tesis y evidencias, después ortografía", "Primero tildes, después ideas", "Solo el título", "Las ideas se ordenan antes de pulir la forma."),
        ("ab", "{F} Beatriz dice: «No quiero revisar porque ya escribí mucho». ¿Qué le respondes?", "Que revisar mejora lo escrito y muestra qué ajustar", "Que tiene razón", "La revisión es la parte que más mejora un texto."),
    ],
    ctx=("abc", "Vas a mandar una carta formal a tu centro para pedir apoyo. Antes de enviarla la relees con una lista: motivo claro, razones, cierre y ortografía. ¿Qué haces?", "Reviso con una pauta y corrijo", "La envío sin leerla", "La borro", "La pauta ordena la revisión de cualquier texto."),
    sc=[("En Lengua y Literatura: ¿para qué sirve una pauta al revisar una interpretación?", "Para revisar un texto con criterios claros", "Una pauta evita olvidar partes importantes del texto escrito."),
        ("¿Qué falta en un resumen para ser interpretación?", "Una tesis y evidencias explicadas", "La interpretación agrega sentido y datos que el resumen no tiene."),
        ("En Lengua y Literatura: ¿qué hago al terminar la revisión?", "Decido qué mejorar y lo corrijo", "Revisar sirve para mejorar el texto.")],
    op=("Reescribe el texto de Gloria en un párrafo de cinco oraciones que cumpla los seis criterios de la pauta, y anota qué criterio fue lo más difícil de lograr. {F}",
        "La mesa puesta representa la esperanza del regreso, como la tela de Penélope. Esto se ve cuando doña Julia dice que así «la casa sabe que alguien viene». Además, Elsa deja pan para tres, porque el gesto se comparte. Por eso, el relato recuerda a la Odisea, aunque no dice si Tomás vuelve. Lo más difícil fue explicar las evidencias.",
        ["tesis clara", "dos evidencias explicadas con conectores", "relación con la Odisea y diferencia", "nombra qué criterio le costó"],
        ["un párrafo de cinco oraciones"],
        ["dejar un resumen", "no decir qué le costó"],
        "Pregunta: «¿Qué cambiarías si el texto fuera para el boletín del centro?»."),
    reinforce="Revisa un mensaje que hayas escrito esta semana con tres criterios: claro, ordenado y sin errores.",
    extend="Intercambia tu párrafo con otra persona del grupo, si puedes, y anótale una cosa que está bien y una que mejorar.",
)
