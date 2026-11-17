"""Estética (electivo HC, 3.º y 4.º medio): OAC-05 (interpretar obras artísticas con conceptos filosóficos, corrientes de la teoría del arte y temas de la sociedad actual), clases 1 a 5. Obras ficticias descritas con palabras."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, caso o ficha está escrito en el enunciado. "
             "Los textos filosóficos son resúmenes originales de posturas y las obras de arte son casos ficticios descritos con palabras: no se reproducen obras con derechos ni se usan imágenes o audio. "
             "Las posturas se presentan con sus razones y sin tomar partido: tu tarea es analizar y evaluar. Si tu docente propone mirar o escuchar una obra real, hazlo en sala y con las pautas que él o ella indique. "
             "En los temas de moral, política o bienestar emocional se usan casos ficticios; si algo te afecta, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O5 = "FI-ESTE-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 21 (obra ficticia descrita con palabras). «Ventana 7» es una pintura imaginaria: muestra una ventana grande vista desde dentro de un cuarto casi vacío y gris; por la ventana se ve una ciudad de colores muy vivos; en el alféizar hay una taza y no hay nadie en el cuarto. "
     "Tres lecturas. Ana: «La obra habla de aislamiento: el cuarto gris está separado de la ciudad viva.» "
     "Bruno: «Habla de descanso: la taza y la calma sugieren que alguien mira el mundo sin apuro.» "
     "Camila: «Me gustó cómo el gris hace resaltar los colores de afuera.»")
build(
    O5, 1, F,
    use="Aprenderé a distinguir describir, interpretar y opinar sobre una obra y a plantear una interpretación como una hipótesis apoyada en lo que la obra muestra.",
    prior=["Distingo percepción de interpretación.", "Reconozco juicio estético.", "Sé reconstruir una posición."],
    explain=[
        "Interpretar una obra es proponer qué significa o qué experiencia ofrece, apoyándose en lo que muestra. Es distinto de describirla, que dice qué se ve o se oye sin añadir significado, y de opinar, que expresa si nos gusta o no. Una buena lectura suele combinar las tres cosas pero las mantiene separadas.",
        "Una interpretación es una hipótesis: puede ser más o menos convincente según cuánto se apoye en la obra. Se sostiene señalando rasgos concretos: colores, ritmos, palabras, gestos o silencios. Una misma obra puede admitir varias interpretaciones razonables, y eso no significa que cualquiera valga: algunas están mejor apoyadas que otras.",
        "Las obras pueden ser visuales, musicales, literarias, teatrales, audiovisuales o dancísticas. En este cuaderno las conocemos a través de descripciones escritas de obras ficticias. Si tu docente propone ver o escuchar una obra real, aplica el mismo método: describe, interpreta con evidencia y distingue de tu opinión.",
    ],
    vocab=[("describir", "decir qué se ve, se oye o sucede sin añadir significado"), ("interpretar", "proponer qué significa una obra apoyándose en lo que muestra"), ("opinar", "expresar si algo nos gusta o no"), ("evidencia de la obra", "rasgo concreto de la obra que apoya una interpretación"), ("hipótesis interpretativa", "lectura propuesta que se puede apoyar o debilitar con evidencia")],
    worked=[
        ("Clasificar una frase", "De la obra «Ventana 7»: «Hay una taza en el alféizar». ¿Es descripción, interpretación u opinión?",
         ["Mira si añade significado o valoración: no, dice lo que hay.", "Entonces es una descripción."],
         "Descripción"),
        ("Apoyar una interpretación", "Apoya con evidencia de «Ventana 7» la lectura de Ana (aislamiento).",
         ["Busca rasgos de la ficha que sugieran separación: el cuarto está gris y casi vacío.", "Añade el contraste con la ciudad de colores vivos y que no hay nadie en el cuarto."],
         "El cuarto gris y vacío contrasta con la ciudad viva, lo que sugiere separación"),
    ],
    mistakes=[("Presentar una interpretación como si fuera lo que la obra «dice» sin más.", "Se olvida que es una hipótesis.", "Usa fórmulas como «una lectura posible es…» y señala evidencia."),
              ("Aceptar cualquier interpretación porque «todo vale».", "Se confunde pluralidad con ausencia de criterio.", "Cuenta cuánta evidencia de la obra apoya cada lectura.")],
    T=[
        ("abc", "{F} ¿Qué frase de la ficha es una descripción?", "«Por la ventana se ve una ciudad de colores muy vivos»", "«La obra habla de aislamiento»", "«Me gustó cómo el gris hace resaltar los colores»", "La primera dice lo que se ve sin añadir significado ni valoración."),
        ("abc", "{F} ¿Qué lectura propone Bruno?", "Que la obra habla de descanso, de mirar el mundo sin apuro", "Que habla de aislamiento", "Que la obra trata del color gris", "Bruno interpreta la taza y la calma como descanso."),
        ("abc", "{F} ¿Qué tipo de frase es la de Camila?", "Una opinión, porque expresa lo que le gustó", "Una descripción neutra", "Una interpretación de aislamiento", "Dice que le gustó, es decir, expresa una preferencia."),
        ("En Estética: ¿cómo se llama decir qué se ve o se oye en una obra sin añadir significado?", "Describir", "Es la acción que se distingue de interpretar y opinar."),
        ("abc", "{F} Una estudiante dice: «No hay nadie en el cuarto». ¿Qué papel cumple esta frase en la lectura de Ana?", "Es una descripción que sirve de evidencia para la idea de aislamiento", "Es una opinión sobre lo que le gustó de la pintura", "Es la lectura de descanso de Bruno", "Describe un rasgo de la obra que Ana puede usar como apoyo de su lectura."),
        ("ab", "{F} ¿Qué rasgo de la obra apoya la lectura de Bruno?", "La taza en el alféizar, que sugiere calma", "La ciudad ruidosa", "La taza sugiere un momento de pausa, mientras la ciudad no se describe como ruidosa."),
        ("abc", "{F} Una espectadora dice: «La obra trata de dinero». ¿Qué falta para que sea una buena interpretación?", "Rasgos concretos de la obra que la apoyen", "Que cite a una crítica de arte", "Que sea una opinión", "Una interpretación se sostiene con evidencia."),
        ("abc", "{F} Una espectadora dice: «Esta pintura es horrible». ¿Qué es?", "Una opinión", "Una descripción", "Una interpretación apoyada", "Expresa una valoración personal sin evidencia."),
        ("abc", "{F} ¿Por qué se puede decir que las lecturas de Ana y de Bruno son hipótesis?", "Porque proponen un significado que se puede apoyar o debilitar con evidencia", "Porque los dos autores se contradicen", "Porque una pintura no se puede interpretar", "Una hipótesis interpretativa es una lectura sujeta a la evidencia."),
        ("abc", "{F} Un amigo dice: «Como hay dos lecturas, todas las lecturas valen lo mismo». ¿Qué falla?", "Una lectura puede estar mejor apoyada que otra", "Que haya tres lecturas distintas", "Que Ana y Bruno hayan visto la obra", "La pluralidad no elimina diferencias de evidencia."),
        ("abc", "{F} Una profesora propone agregar a la obra una persona sentada en el cuarto. ¿Qué lectura se debilitaría más?", "La de aislamiento, porque ya no habría ausencia de gente", "La de que hay una ventana", "Las dos por igual", "La ausencia de personas apoyaba la lectura de aislamiento."),
        ("abc", "{F} Si el título de la obra fuera «Mi casa tranquila», ¿qué lectura se fortalecería?", "La de descanso", "La de aislamiento", "Las dos por igual", "El título sugeriría calma, coherente con la lectura de Bruno."),
        ("abc", "{F} ¿Cuál es el orden más útil para escribir sobre una obra?", "Describir, interpretar con evidencia y luego opinar", "Opinar primero y después buscar rasgos que confirmen lo que opinaste", "Interpretar primero y describir solo si alguien lo pide", "Separar los tres pasos hace más claro el análisis."),
    ],
    ctx=("abc", "En un club escolar ficticio se muestra una descripción de una obra de danza: una persona baila sola frente a un grupo que se queda inmóvil. Un integrante dice: «Esto es sobre soledad»; otra: «Hay un solo cuerpo en movimiento y un grupo que no se mueve». ¿Qué frase es la descripción?", "La de la otra integrante", "La del integrante que dice soledad", "Las dos por igual", "La segunda dice lo que sucede; la primera ya añade un significado."),
    sc=[
        ("En Estética: ¿qué es interpretar una obra?", "Proponer qué significa o qué experiencia ofrece, apoyándose en lo que muestra", "No es lo mismo que describir ni que opinar."),
        ("¿Por qué una interpretación es una hipótesis?", "Porque puede apoyarse o debilitarse con evidencia de la obra", "Su valor depende de la evidencia."),
        ("¿Por qué no «todas las lecturas valen lo mismo»?", "Porque algunas están mejor apoyadas por la obra", "La pluralidad no elimina el criterio de evidencia."),
    ],
    op=("Elige una de estas obras ficticias: (1) una canción instrumental con un ritmo que se acelera y luego se detiene de golpe, (2) un cuento muy breve en que una persona riega todos los días una planta seca, (3) una escena de teatro en que dos personas hablan sin mirarse. "
        "Escribe una descripción de tres líneas, una interpretación con dos rasgos que la apoyen, una segunda interpretación posible y una opinión personal marcada como tal.",
        "Obra 2. Descripción: una persona riega cada mañana una planta seca. Interpretación: habla de la esperanza terca; rasgos: lo hace todos los días y sigue aunque no cambia. Segunda lectura: habla de la rutina. Opinión: me parece triste y bonito.",
        ["la descripción no incluye interpretación", "la interpretación se apoya en rasgos de la obra", "propone una segunda lectura razonable", "la opinión se marca como personal"],
        ["descripción, interpretación con evidencia, segunda lectura y opinión"],
        ["incluir significados en la descripción", "interpretar sin evidencia", "presentar la opinión como interpretación"],
        "Pregunta: «¿qué rasgo de la obra respalda esa lectura?». Pídele que lo señale."),
    reinforce="Elige un afiche, canción o escena de serie y escribe una descripción de tres líneas sin interpretar.",
    extend="Explica por qué una interpretación puede ser razonable y, aun así, no ser la única posible.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 22 (obras ficticias descritas y glosario). Obra musical «Marea»: pieza imaginaria para piano; empieza con notas graves repetidas y lentas; luego aparecen notas agudas que suben poco a poco; al final vuelven las graves y hay un silencio largo. "
     "Poema original «Pozo»: «Tiro una palabra al pozo / y espero el eco / que no vuelve; / sin embargo, / sigo asomándome.» "
     "Glosario: forma = cómo está organizada la obra; contenido o tema = de qué trata; símbolo = elemento que representa una idea más allá de sí mismo; contexto = circunstancias de su creación y recepción; formalismo = lectura centrada en la forma; expresivismo = lectura centrada en el sentimiento que expresa; lectura contextual = lectura que relaciona la obra con su sociedad; lo sublime = experiencia de algo muy grande o poderoso que impresiona y a la vez abruma.")
build(
    O5, 2, F,
    use="Aprenderé a definir forma, contenido, símbolo, contexto y algunas corrientes (formalismo, expresivismo, lectura contextual) y conceptos como lo sublime, y a usarlos para interpretar obras de distintos lenguajes artísticos.",
    prior=["Distingo describir, interpretar y opinar.", "Conozco formalismo y expresivismo.", "Sé apoyar una lectura con evidencia."],
    explain=[
        "Para interpretar con precisión conviene distinguir algunos elementos. La forma es cómo está organizada la obra: ritmos, colores, estrofas, escenas. El contenido o tema es de qué trata. Un símbolo es un elemento que representa una idea más allá de sí mismo. El contexto reúne las circunstancias de su creación y de su recepción.",
        "Las corrientes de la teoría del arte son maneras de dar prioridad a ciertos elementos. El formalismo mira sobre todo la forma. El expresivismo, el sentimiento que la obra expresa. La lectura contextual relaciona la obra con la sociedad en que nace o se recibe. No son excluyentes: una interpretación rica puede combinarlas y decir de cuál parte.",
        "Los conceptos filosóficos ayudan a nombrar una experiencia. Por ejemplo, lo sublime se refiere a la experiencia de algo muy grande o poderoso que impresiona y a la vez abruma. Puede aparecer en una pieza musical, un paisaje pintado o un poema. Usar un concepto no sustituye mirar la obra: sirve para describir con más precisión lo que se encuentra en ella.",
    ],
    vocab=[("forma", "cómo está organizada una obra"), ("tema", "de qué trata una obra"), ("símbolo", "elemento que representa una idea más allá de sí mismo"), ("contexto", "circunstancias en que se crea y se recibe una obra"), ("lectura contextual", "lectura que relaciona la obra con su sociedad"), ("lo sublime", "experiencia de algo muy grande o poderoso que impresiona y a la vez abruma")],
    worked=[
        ("Distinguir forma y tema", "De «Marea»: «Hay notas graves, luego agudas, y vuelven las graves». ¿Es forma o tema?",
         ["Mira si dice cómo está organizada la pieza: sí, describe su estructura.", "No dice de qué trata; entonces es forma."],
         "Forma"),
        ("Proponer un símbolo", "En «Pozo», ¿qué podría simbolizar el pozo?",
         ["Observa que el pozo recibe palabras y no devuelve el eco.", "Puede simbolizar un silencio o una espera sin respuesta."],
         "Un silencio o una espera sin respuesta"),
    ],
    mistakes=[("Confundir tema con forma.", "Se mezcla de qué trata la obra con cómo está organizada.", "Pregunta: ¿esto dice cómo está hecha la obra o de qué habla?"),
              ("Usar «lo sublime» como sinónimo de «muy bello».", "Se pierde el matiz de lo abrumador.", "Lo sublime incluye grandeza que impresiona y abruma, no solo belleza.")],
    T=[
        ("abc", "{F} ¿Qué dato de «Pozo» es de forma y no de tema?", "Tiene versos cortos y «sin embargo» ocupa una línea propia", "Trata de una espera sin respuesta", "Habla de la insistencia de seguir intentando", "La forma dice cómo está organizado el poema; las otras opciones dicen de qué trata."),
        ("abc", "{F} En «Pozo», ¿qué gesto del hablante puede leerse como símbolo de la insistencia?", "Seguir asomándose al pozo", "Lanzar la palabra una sola vez", "Contar los versos del poema", "Asomarse otra vez, aunque el eco no vuelva, representa seguir intentándolo."),
        ("abc", "{F} ¿Cuál es un posible tema de «Pozo»?", "La espera de una respuesta que no llega", "La construcción de un pozo", "Una celebración colectiva", "Los versos hablan de lanzar una palabra y esperar un eco."),
        ("En Estética: ¿cómo se llama la lectura centrada en el sentimiento que una obra expresa?", "Expresivismo", "Es la corriente que prioriza el sentimiento expresado."),
        ("abc", "{F} ¿Qué lectura se centra en cómo cambian las notas de «Marea»?", "Una lectura formalista", "Una lectura contextual", "Una lectura expresivista", "Se concentra en la forma de la pieza."),
        ("ab", "{F} Una lectura relaciona «Marea» con las ciudades costeras que la rodean. ¿Qué tipo de lectura es?", "Contextual", "Formalista", "Relaciona la obra con su sociedad y su entorno, por eso es contextual."),
        ("abc", "{F} El silencio largo del final de «Marea» puede provocar la sensación de algo muy grande que abruma. ¿Qué concepto se usa para nombrarlo?", "Lo sublime", "El símbolo", "El contexto", "Esa experiencia de grandeza que abruma es lo sublime."),
        ("abc", "{F} ¿Qué lectura de «Pozo» es expresivista?", "El poema transmite la ansiedad de esperar sin respuesta", "El poema tiene cinco líneas", "El poema fue escrito en una ciudad", "Se centra en el sentimiento que expresa."),
        ("abc", "{F} ¿Qué lectura de «Pozo» es formalista?", "Los versos son cortos y «sin embargo» queda solo en una línea, como una pausa antes del último verso", "El poema habla de soledad", "El poema se leyó en una plaza", "Atiende a la organización del texto."),
        ("abc", "{F} Una estudiante dice: «Marea es sublime porque es bonita». ¿Qué corrección es mejor?", "Lo sublime implica grandeza que impresiona y abruma; la belleza es otro concepto", "Es correcto", "Sublime es lo contrario de bello", "El concepto añade el matiz de lo abrumador."),
        ("abc", "{F} Un estudiante dice: «Un símbolo es lo que se ve en la obra». ¿Qué falla?", "Un símbolo representa una idea más allá de sí mismo", "Nada falla", "Un símbolo es el objeto más grande de la obra", "No basta con ser visible: un símbolo remite a algo más."),
        ("abc", "{F} ¿Qué combinación de corrientes daría una lectura más completa de «Pozo»?", "Mirar su forma y el sentimiento que expresa, y relacionarlo con su contexto", "Elegir solo una y no mirar el poema", "Usarlas todas sin mirar el poema", "Las corrientes pueden combinarse con evidencia."),
        ("abc", "{F} Si se quitara el silencio largo del final de «Marea», ¿qué se vería más afectado?", "La forma de la pieza, que ya no cerraría con un silencio después de las graves", "El número de notas graves del inicio", "El instrumento con que se toca la pieza", "El silencio forma parte de cómo se organiza el final de la pieza."),
    ],
    ctx=("abc", "En una exposición ficticia sobre ciudades, una obra de teatro describe a un grupo que construye un puente de cajas que siempre se cae. Un visitante la interpreta como símbolo de esfuerzo colectivo. ¿Qué elemento usa?", "El símbolo del puente", "La forma de la escena", "El contexto de creación", "Interpreta el puente como algo que representa más allá de sí mismo."),
    sc=[
        ("En Estética: ¿qué es un símbolo?", "Un elemento que representa una idea más allá de sí mismo", "Su sentido va más allá de lo literal."),
        ("¿Qué es lo sublime?", "La experiencia de algo muy grande o poderoso que impresiona y a la vez abruma", "Lo sublime añade el matiz de grandeza que abruma, no solo belleza."),
        ("¿En qué se diferencian formalismo y expresivismo?", "El formalismo mira la forma y el expresivismo el sentimiento que se expresa", "El formalismo prioriza la forma y el expresivismo prioriza el sentimiento expresado."),
    ],
    op=("Elige una de las dos obras de la ficha («Marea» o «Pozo») y escribe una interpretación en tres partes: (a) una lectura formalista con un rasgo de forma, (b) una lectura expresivista con un sentimiento, (c) una lectura contextual con una circunstancia posible. "
        "Cierra con una frase que diga cuál te parece más convincente y por qué, apoyada en la obra.",
        "«Pozo». (a) Formalista: «sin embargo» queda solo en una línea, como una pausa antes del último verso. (b) Expresivista: transmite espera y ansiedad. (c) Contextual: podría leerse en una época en que cuesta recibir respuestas. Más convincente: la (b), porque el último verso muestra que sigue asomándose.",
        ["distingue las tres lecturas", "cada lectura usa un rasgo de la obra", "la elección final se justifica con la obra", "no confunde forma con tema"],
        ["tres lecturas y una elección justificada"],
        ["escribir tres veces la misma lectura", "elegir sin justificar", "confundir forma con tema"],
        "Pregunta: «¿qué verso o qué parte de la pieza usas como evidencia?». Pídele que lo cite."),
    reinforce="Elige una canción o escena que conozcas y escribe su forma, su tema y un posible símbolo.",
    extend="Explica por qué una interpretación que combina corrientes puede ser más rica, pero necesita decir de dónde viene cada parte.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 23 (obra teatral ficticia). «El último banco»: dos personas, la Señora y el Joven, comparten un banco en una plaza. Cada una mira su teléfono. Durante la obra se escucha un reloj. A mitad de la obra, el teléfono de la Señora se descarga; ella mira alrededor, ve al Joven y le ofrece un pañuelo. Él levanta la mirada. Final: ambos se quedan sentados en silencio, sin teléfono, mirando el atardecer pintado en el fondo. "
     "Conceptos: mimesis = representación de la realidad; catarsis = depuración de emociones; experiencia estética = atención a cómo algo se presenta. "
     "Tema de la sociedad actual: la comunicación a través de pantallas y los vínculos presenciales.")
build(
    O5, 3, F,
    use="Aprenderé a interpretar una obra con conceptos filosóficos y con un tema de la sociedad actual, y a reconstruir tres lecturas (formal, expresiva y contextual) de una misma obra.",
    prior=["Conozco forma, tema, símbolo y contexto.", "Distingo formalismo, expresivismo y lectura contextual.", "Sé apoyar una interpretación con evidencia."],
    explain=[
        "Un concepto filosófico es una herramienta para pensar una obra. La mimesis, o representación de la realidad, sirve para preguntar qué aspecto de la vida actual muestra una obra. La catarsis, la depuración de emociones, sirve para preguntar qué emociones mueve en el público y cómo se resuelven. La experiencia estética sirve para preguntar cómo nos hace atender a lo que se presenta.",
        "Los temas de la sociedad actual, como el uso de pantallas, los vínculos y la convivencia, pueden dar contexto para una lectura. Una obra ficticia puede mostrar estas realidades sin dar una moraleja. La lectura contextual explica cómo la obra dialoga con su época sin reducirla a un mensaje.",
        "Reconstruir tres lecturas de una misma obra significa decir, para cada corriente, qué elemento destaca y qué interpretación propone. Por ejemplo, ante una obra imaginaria sobre un mercado, la lectura formal puede notar el ritmo repetido de los pregones; la expresiva, una alegría que se vuelve cansancio; la contextual, el diálogo con las formas de comprar hoy. Ninguna lectura agota la obra.",
    ],
    vocab=[("mimesis", "representación de la realidad en una obra"), ("catarsis", "depuración de emociones al presenciar una obra"), ("lectura formal", "lectura que destaca la organización de la obra"), ("lectura expresiva", "lectura que destaca el sentimiento expresado"), ("lectura contextual", "lectura que relaciona la obra con su época")],
    worked=[
        ("Identificar un elemento formal", "En «El último banco», ¿qué elemento formal se repite durante toda la obra?",
         ["Busca algo que se mantenga: el sonido del reloj.", "Es un elemento formal que organiza el ritmo de la obra."],
         "El sonido del reloj"),
        ("Aplicar mimesis", "¿Qué aspecto de la vida actual representa «El último banco»?",
         ["Observa qué hacen los personajes: miran sus teléfonos en un espacio compartido.", "Representa la convivencia entre pantallas y presencia."],
         "La convivencia entre pantallas y presencia en un espacio compartido"),
    ],
    mistakes=[("Reducir la obra a una moraleja como «los teléfonos son malos».", "Se pierde la complejidad de la obra.", "Describe qué pasa y qué experiencia ofrece sin imponer un mensaje único."),
              ("Usar un concepto filosófico sin mostrar dónde aparece en la obra.", "Se queda en la etiqueta.", "Cita una escena o rasgo donde se vea el concepto.")],
    T=[
        ("abc", "{F} ¿Qué ocurre justo antes de que la Señora le ofrezca un pañuelo al Joven?", "Se descarga el teléfono de la Señora y ella mira alrededor", "El Joven la saluda", "Suena el reloj fuerte", "La ficha dice que el teléfono se descarga y ella mira alrededor antes de ofrecer el pañuelo."),
        ("abc", "{F} ¿Qué gesto de la Señora abre un cambio en la obra?", "Ofrecer un pañuelo al Joven", "Pedir al Joven que guarde silencio", "Cambiar de banco", "El pañuelo rompe la rutina de las pantallas."),
        ("abc", "{F} ¿Qué hacen los personajes en el final?", "Se quedan sentados sin teléfono, mirando el atardecer", "Vuelven a mirar sus teléfonos", "Se despiden con un abrazo", "La ficha describe un final en silencio."),
        ("abc", "{F} ¿Qué concepto filosófico se aplica a la pregunta «¿qué aspecto de la vida actual representa la obra?»?", "Mimesis", "Catarsis", "Símbolo", "La mimesis es la representación de la realidad."),
        ("abc", "{F} ¿Qué concepto filosófico se aplica a «¿qué emociones mueve en el público y cómo se resuelven?»?", "Catarsis", "Mimesis", "Contexto", "La catarsis trata de la depuración de emociones."),
        ("ab", "{F} Que la obra termine en silencio, ¿es un rasgo de forma o de tema?", "De forma, porque dice cómo se organiza el final", "De tema, porque dice de qué trata la obra", "El silencio es una decisión de organización del final, no el asunto principal de la obra."),
        ("abc", "{F} Una lectura expresiva de la obra diría…", "Que muestra la transformación de un aislamiento en cercanía", "Que el reloj marca el ritmo de la obra", "Que la obra dialoga con el uso de pantallas de hoy", "Se centra en el sentimiento que la obra expresa."),
        ("abc", "{F} Una lectura contextual de la obra diría…", "Que dialoga con la vida actual con pantallas y vínculos presenciales", "Que el reloj repite siempre el mismo sonido", "Que la obra expresa tristeza y alivio", "Relaciona la obra con su época."),
        ("abc", "{F} Una lectura formal de la obra diría…", "Que el silencio final contrasta con el sonido repetido del reloj", "Que la obra critica a los jóvenes", "Que la obra transmite una emoción de cercanía", "Se centra en la organización de la obra."),
        ("abc", "{F} Un estudiante concluye: «La obra dice que los teléfonos son malos». ¿Qué falla?", "Reduce una obra compleja a una moraleja que la ficha no sostiene", "Resume la obra con precisión", "Confunde formalismo con expresivismo", "La obra muestra una situación sin juzgarla de forma explícita."),
        ("abc", "{F} ¿Qué evidencia apoya mejor que el Joven y la Señora pasan del aislamiento a la cercanía?", "Ella le ofrece un pañuelo y él levanta la mirada", "El sonido del reloj", "El atardecer pintado", "Los gestos del pañuelo y de la mirada muestran un acercamiento."),
        ("abc", "{F} Si el final fuera que ambos vuelven a mirar sus teléfonos, ¿qué lectura cambiaría más?", "La de la transformación en cercanía", "La lectura formal sobre el silencio final", "La lectura contextual sobre pantallas", "El final ya no mostraría un cambio sostenido."),
        ("abc", "{F} ¿Qué lectura es más completa para esta obra?", "Combinar lo formal, lo expresivo y lo contextual con evidencia", "Elegir una sin evidencia", "Resumirla en una moraleja que todos acepten", "Una combinación, justificada con rasgos, ofrece una visión más amplia."),
    ],
    ctx=("abc", "Una profesora ficticia lleva a su curso a ver un ensayo de «El último banco» y pide que escriban una frase sobre la obra. Un estudiante anota: «Es una obra sobre vínculos humanos que mira con cariño un mundo lleno de pantallas». ¿Qué tipo de frase es?", "Una interpretación contextual con un tono expresivo", "Una lectura formalista", "Una opinión sin evidencia", "Relaciona la obra con la sociedad actual e incluye una valoración."),
    sc=[
        ("En Estética: ¿qué es la mimesis?", "La representación de la realidad en una obra", "Sirve para preguntar qué aspecto de la vida muestra la obra."),
        ("¿Qué es una lectura contextual?", "Una lectura que relaciona la obra con su época o su sociedad", "Se apoya en el entorno de la obra."),
        ("¿Por qué conviene evitar reducir una obra a una moraleja?", "Porque se pierde la complejidad y se afirma más de lo que la obra muestra", "La obra puede ofrecer experiencias más ricas."),
    ],
    op=("Reconstruye tres lecturas de «El último banco»: una formal (con un elemento de forma), una expresiva (con una emoción) y una contextual (con un tema actual). "
        "Después escribe qué concepto filosófico (mimesis, catarsis o experiencia estética) usarías para hablar de la obra y en qué escena lo ves.",
        "Formal: el reloj repetido marca un ritmo que se rompe con el pañuelo. Expresiva: de aislamiento a cercanía. Contextual: vínculos presenciales y pantallas. Concepto: catarsis, en el final silencioso, donde se resuelve la tensión acumulada.",
        ["las tres lecturas son distintas", "cada lectura se apoya en una escena", "el concepto filosófico se aplica con evidencia", "no reduce la obra a una moraleja"],
        ["tres lecturas, un concepto y una escena"],
        ["repetir la misma lectura con otro nombre", "usar el concepto sin escena", "concluir con una moraleja única"],
        "Pregunta: «¿en qué escena se ve ese concepto?». Pídele que la nombre."),
    reinforce="Describe una escena cotidiana (en la micro, un recreo) como si fuera una obra de teatro y propón dos lecturas.",
    extend="Explica por qué una lectura contextual puede iluminar una obra sin agotarla.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 24 (obra audiovisual ficticia). Cortometraje imaginario «Conexión»: una abuela hace una videollamada con su nieto; ella sostiene el teléfono lejos y se ve solo su frente; él habla rápido y mira otra pantalla. "
     "A los dos minutos, la imagen se congela; la abuela deja el teléfono sobre la mesa, toma un álbum de fotos y lo abre mostrando a la cámara; el nieto mira por primera vez a la cámara. El corto termina con la imagen congelada y se oye una risa. "
     "Dos interpretaciones. Lectura 1: «Es sobre la brecha entre generaciones, que se resuelve cuando se comparte algo tangible.» Lectura 2: «Es sobre el tiempo: la congelación de la imagen es una pausa que permite mirar.» "
     "Criterios para evaluar una interpretación: evidencia en la obra, coherencia con otros elementos, plausibilidad y riqueza (ilumina más de la obra).")
build(
    O5, 4, F,
    use="Aprenderé a formular y evaluar interpretaciones de una obra con criterios de evidencia, coherencia, plausibilidad y riqueza, y a distinguir una buena interpretación de una sobreinterpretación.",
    prior=["Distingo describir, interpretar y opinar.", "Conozco corrientes y conceptos.", "Evalúo argumentos con criterios."],
    explain=[
        "Una interpretación argumentada tiene tres partes: una tesis (qué significa o qué experiencia ofrece la obra), evidencia (rasgos concretos que la apoyan) y una conexión que explique por qué esos rasgos apoyan la tesis. Sin evidencia es una opinión; sin conexión es una lista de rasgos.",
        "Para evaluar una interpretación se usan cuatro criterios. La evidencia: ¿se apoya en lo que muestra la obra? La coherencia: ¿cuadra con otros elementos o los contradice? La plausibilidad: ¿es razonable dado el contexto? La riqueza: ¿ilumina varios aspectos de la obra? La sobreinterpretación ocurre cuando se atribuye a la obra más de lo que su evidencia permite.",
        "Un error frecuente es creer que lo que dijo el autor cierra la interpretación. La intención del autor es una fuente útil, pero no la única: una obra puede significar cosas que su autor no previó. Otro error es creer que cualquier interpretación vale. Evaluar interpretaciones es una conversación con la obra y con otras lecturas, no un concurso de opiniones.",
    ],
    vocab=[("tesis interpretativa", "afirmación sobre el significado o la experiencia que ofrece una obra"), ("coherencia interpretativa", "ajuste de la lectura con otros elementos de la obra"), ("plausibilidad", "razonabilidad de una lectura dado el contexto"), ("riqueza interpretativa", "capacidad de una lectura de iluminar varios aspectos de la obra"), ("sobreinterpretación", "atribuir a la obra más de lo que su evidencia permite")],
    worked=[
        ("Evaluar con el criterio de evidencia", "Evalúa la Lectura 2 de la ficha con el criterio de evidencia.",
         ["Busca el rasgo en que se apoya: la imagen congelada.", "Ese rasgo existe en la obra; la lectura tiene apoyo."],
         "Tiene evidencia: la imagen congelada que permite mirar"),
        ("Detectar una sobreinterpretación", "Un espectador dice: «La mesa del corto es una crítica a los muebles de las ciudades». ¿Qué pasa?",
         ["Mira la evidencia: solo se dice que hay una mesa.", "Se atribuye a la obra un significado que no tiene apoyo: es una sobreinterpretación."],
         "Es una sobreinterpretación"),
    ],
    mistakes=[("Creer que la intención declarada del autor cierra la interpretación.", "Se confunde fuente útil con única fuente.", "Considera la intención, pero evalúa la lectura con la obra."),
              ("Dar una lista de rasgos sin explicar por qué apoyan la tesis.", "Falta la conexión.", "Añade una frase que una cada rasgo con la tesis.")],
    T=[
        ("abc", "{F} ¿Qué rasgo del corto apoya la Lectura 1 (brecha entre generaciones que se resuelve compartiendo algo tangible)?", "La abuela muestra un álbum de fotos y el nieto mira a la cámara", "El nieto habla rápido", "La risa final", "El álbum es algo tangible que cambia el vínculo."),
        ("abc", "{F} ¿Qué rasgo apoya la Lectura 2 (el tiempo y la pausa)?", "La imagen congelada", "El teléfono sostenido lejos", "La risa", "La congelación es una pausa visible."),
        ("abc", "{F} Si el nieto nunca mirara a la cámara, ni siquiera cuando aparece el álbum, ¿qué lectura se debilitaría más?", "La Lectura 1, porque el cambio en su actitud no sería visible", "Las dos por igual", "La que dice que hay un teléfono", "La Lectura 1 depende de que el nieto cambie su actitud cuando aparece el álbum."),
        ("En Estética: ¿cómo se llama atribuir a una obra más de lo que su evidencia permite?", "Sobreinterpretación", "Es el nombre de ese error de interpretación."),
        ("abc", "¿Qué criterio evalúa si una interpretación cuadra con otros elementos de la obra?", "Coherencia", "Evidencia", "Plausibilidad", "La coherencia revisa que no se contradiga con otros elementos."),
        ("ab", "{F} ¿Puede la Lectura 1 explicar la risa final del corto?", "Sí: la risa puede entenderse como resultado de un vínculo recuperado", "No: la risa no tiene relación con el vínculo entre abuela y nieto", "La risa tras el momento del álbum se puede leer como señal de reencuentro, lo que apoya la Lectura 1."),
        ("abc", "{F} Un espectador dice: «La abuela abre el álbum porque quiere vender sus recuerdos». ¿Qué problema tiene?", "Atribuye una intención que ningún rasgo del corto apoya: es una sobreinterpretación", "Describe con exactitud lo que se ve", "Se apoya en la risa final", "Nada en la ficha sugiere esa intención; la lectura excede la evidencia."),
        ("abc", "{F} El director ficticio dice que el corto trata solo del cuidado de los mayores. ¿Qué se puede afirmar?", "Que su intención es una fuente útil, pero no impide otras lecturas bien apoyadas", "Que ninguna otra lectura es posible", "Que su palabra no vale nada", "La intención no cierra la interpretación."),
        ("abc", "{F} ¿Qué lectura ilumina más aspectos de la obra (mirada, álbum, congelación, risa)?", "Una que combine la brecha entre generaciones y la pausa que permite mirar", "Una que solo diga que hay un teléfono", "Una que solo hable de la mesa", "Combinar lecturas puede aumentar la riqueza."),
        ("abc", "{F} Escribe la conexión que falta: «Evidencia: el álbum de fotos. Tesis: el vínculo se recupera al compartir algo tangible. Conexión: …»", "Mostrar un objeto concreto cambia la actitud del nieto, que por primera vez mira", "El álbum aparece en el segundo minuto", "El nieto habla rápido al principio", "Una conexión explica por qué el rasgo apoya la tesis."),
        ("abc", "{F} Una estudiante afirma: «La obra tiene seguramente un mensaje secreto en cada plano». ¿Qué problema tiene?", "Sobreinterpreta sin evidencia para cada plano", "Es una descripción", "Es un criterio", "Un mensaje en cada plano excede lo que se ve."),
        ("abc", "{F} Dos estudiantes proponen lecturas opuestas del final congelado. ¿Cómo decidir cuál está mejor apoyada?", "Comparar cuánta evidencia, coherencia y riqueza aporta cada una", "Votar", "Elegir la del más popular", "Se decide con criterios y no con popularidad."),
        ("abc", "{F} Una buena interpretación…", "Propone una tesis, la apoya con rasgos y explica la conexión", "Opina sin rasgos", "Lista rasgos sin tesis", "Una interpretación argumentada necesita una tesis, evidencia de la obra y la conexión entre ambas."),
    ],
    ctx=("abc", "En un taller ficticio de cine escolar, un estudiante dice que su corto trata «de todo». Una compañera le pide que elija una tesis y la apoye con tres planos. ¿Qué mejora con esa petición?", "La claridad de la interpretación y la evidencia que la sostiene", "La duración del corto", "Su volumen", "Una tesis con evidencia es más evaluable que algo que «trata de todo»."),
    sc=[
        ("En Estética: ¿cuáles son los cuatro criterios para evaluar una interpretación?", "Evidencia, coherencia, plausibilidad y riqueza", "Son los criterios de la clase."),
        ("¿Por qué la intención del autor no cierra la interpretación?", "Porque una obra puede significar cosas que el autor no previó", "Es una fuente útil pero no la única."),
        ("¿Qué partes tiene una interpretación argumentada?", "Tesis, evidencia y conexión", "Sin alguna de ellas queda incompleta."),
    ],
    op=("Elige una lectura del corto «Conexión» (la Lectura 1, la Lectura 2 o una tercera tuya) y escribe una interpretación argumentada: tesis, dos rasgos como evidencia, la conexión de cada rasgo con la tesis y una evaluación con los cuatro criterios (una frase por criterio).",
        "Tesis: el corto habla de cómo el tiempo compartido repara el vínculo. Evidencia 1: la imagen congelada; conexión: la pausa permite mirar. Evidencia 2: el álbum; conexión: el objeto concreto atrae la atención. Evaluación: tiene evidencia, es coherente con la risa final, es plausible y ilumina varios planos.",
        ["tesis clara", "dos rasgos de la obra como evidencia", "cada rasgo se conecta con la tesis", "evalúa con los cuatro criterios"],
        ["interpretación argumentada con evaluación"],
        ["presentar rasgos sin conexión", "tesis demasiado general", "no evaluar con criterios"],
        "Pregunta: «¿por qué ese rasgo apoya tu tesis?». Pídele que lo explique en una frase."),
    reinforce="Elige una canción que conozcas (sin copiar su letra) y propón una tesis interpretativa con dos rasgos de apoyo.",
    extend="Explica la diferencia entre una interpretación audaz, pero bien apoyada, y una sobreinterpretación.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 25 (obra dancística ficticia y objeciones). «Círculo»: danza imaginaria de seis personas. Comienzan tomadas de las manos formando un círculo y girando; una persona suelta las manos y sale del círculo; las otras cierran el espacio y siguen girando; después de un tiempo la persona vuelve y el círculo se abre para dejarla entrar. Final: el círculo cambia de dirección. "
     "Lectura L: «La obra trata de pertenecer a un grupo y de salir y volver sin romperlo.» "
     "Objeción 1: «Tu lectura es solo tuya: nada en la obra dice que se trate de grupos humanos; podría ser sobre planetas.» "
     "Objeción 2: «Si la obra admite muchas lecturas, entonces no hay una mejor, y no vale la pena discutir.» "
     "Tema de la sociedad actual: migrar, ausentarse y regresar a una comunidad.")
build(
    O5, 5, F,
    use="Aprenderé a responder objeciones a una interpretación, incluida la de que «es solo tuya» y la de que «todas valen», y a defender una lectura con matices frente a lecturas rivales.",
    prior=["Evalúo interpretaciones con cuatro criterios.", "Reconozco sobreinterpretación.", "Sé formular una réplica."],
    explain=[
        "Una interpretación puede recibir objeciones de dos tipos. Las objeciones al apoyo señalan que la evidencia no alcanza o que otra lectura la explica mejor. Las objeciones al sentido cuestionan que valga la pena interpretar, por ejemplo, diciendo que todas las lecturas valen lo mismo. Ambas se responden con razones y con casos de la obra.",
        "Una réplica sólida puede reconocer el límite de la lectura, precisar qué parte de la obra apoya y qué parte queda abierta, y comparar con la lectura rival. Frente a «es solo tuya», se muestra que los rasgos de la obra (el círculo, el salir, el volver) conectan con la lectura. Frente a «todas valen», se muestra que las lecturas se comparan por evidencia, coherencia, plausibilidad y riqueza.",
        "La pluralidad de lecturas no es lo mismo que el relativismo total. Una obra puede admitir varias lecturas razonables y excluir otras mal apoyadas. Defender una lectura con matices significa decir qué abarca, qué no explica y qué evidencia podría hacer cambiar de opinión. Es una conversación abierta, no una pelea para ganar.",
    ],
    vocab=[("objeción al apoyo", "señala que la evidencia no alcanza o que otra lectura explica mejor"), ("objeción al sentido", "cuestiona que valga la pena interpretar o compara lecturas como equivalentes"), ("pluralidad de lecturas", "existencia de varias lecturas razonables de una obra"), ("relativismo total", "idea de que todas las lecturas valen lo mismo"), ("lectura rival", "interpretación que compite con otra por explicar la obra")],
    worked=[
        ("Clasificar la Objeción 1", "La Objeción 1 dice que nada en la obra indica que se trate de grupos humanos. ¿Qué tipo de objeción es?",
         ["Mira qué cuestiona: si la evidencia alcanza para la lectura.", "Es una objeción al apoyo."],
         "Objeción al apoyo"),
        ("Dar una réplica", "Responde a la Objeción 1 con un rasgo de la obra.",
         ["Rasgo: los bailarines se toman de las manos, como suele hacerse en grupos de personas.", "Réplica: el contacto de manos, el salir y el volver sugieren vínculos humanos más que planetas."],
         "El contacto de manos y el salir y volver sugieren vínculos humanos"),
    ],
    mistakes=[("Defender una lectura diciendo «es mi opinión» sin dar evidencia.", "Se evita el debate en vez de responder.", "Responde con rasgos de la obra."),
              ("Concluir que, como hay varias lecturas, cualquiera vale.", "Se confunde pluralidad con relativismo total.", "Compara lecturas con criterios.")],
    T=[
        ("abc", "{F} ¿Qué dice la Lectura L?", "Que la obra trata de pertenecer a un grupo y de salir y volver sin romperlo", "Que la obra trata de planetas", "Que el círculo cambia de dirección sin razón", "Es la lectura de pertenencia al grupo."),
        ("abc", "{F} ¿Qué tipo de objeción es la Objeción 1?", "Objeción al apoyo", "Objeción al sentido", "Es una lectura rival", "Dice que la evidencia no alcanza para la lectura propuesta."),
        ("abc", "{F} ¿Qué tipo de objeción es la Objeción 2?", "Objeción al sentido", "Objeción al apoyo", "Es una lectura rival", "Cuestiona que valga la pena discutir lecturas."),
        ("En Estética: ¿cómo se llama la idea de que todas las lecturas valen lo mismo?", "Relativismo total", "Es el nombre que damos aquí a esa idea."),
        ("abc", "{F} ¿Qué rasgo de la obra apoya la Lectura L?", "Que alguien sale del círculo, vuelve y el círculo se abre para dejarlo entrar", "Que hay seis bailarines", "Que el círculo cambia de dirección", "Ese rasgo muestra salida y regreso sin ruptura."),
        ("ab", "{F} ¿Cuál es una réplica a la Objeción 2?", "Las lecturas se comparan por evidencia, coherencia, plausibilidad y riqueza", "Tienes razón, no se puede discutir", "Hay lecturas mejor apoyadas que otras, por lo que sí vale la pena compararlas."),
        ("abc", "{F} ¿Qué cambio en la obra debilitaría más la Lectura L?", "Que la persona que sale nunca vuelva y el círculo se cierre sin ella", "Que los seis bailarines sean ocho", "Que el círculo cambie de dirección al principio", "Sin regreso, la lectura de salir y volver pierde apoyo."),
        ("abc", "{F} Una estudiante responde a la Objeción 1: «No importa, es mi opinión». ¿Qué falla?", "No da evidencia ni discute la objeción", "Es una réplica sólida", "Usa un criterio", "Evita el debate en lugar de responder con rasgos de la obra."),
        ("abc", "{F} Un estudiante dice: «La obra es sobre la migración de una persona que se va y vuelve». ¿Qué relación tiene con el tema de la sociedad actual?", "Conecta la obra con el migrar y regresar a una comunidad", "No tiene relación", "Es una descripción neutra", "Aplica el tema de la ficha como lectura contextual."),
        ("abc", "{F} Otro dice: «Cualquier lectura de Círculo, incluso la que dice que es una receta, vale lo mismo que L». ¿Qué responder?", "Que una receta no tiene apoyo en la obra, mientras L usa varios rasgos", "Que tiene razón", "Que no se puede comparar", "Las lecturas se comparan por cuánta evidencia de la obra las apoya."),
        ("abc", "{F} ¿Cómo se puede defender L con matices?", "Reconociendo que no explica por qué cambia la dirección al final y que podría ampliarse", "Diciendo que explica todo", "Evitando hablar del final", "Un matiz es decir qué no explica."),
        ("abc", "{F} ¿Qué lectura rival de «Círculo» tendría apoyo en el cambio de dirección final?", "Una sobre el cambio y la renovación del grupo después del regreso", "Una que afirma que el final no tiene ningún sentido", "Una que dice que la danza es solo ejercicio físico", "Se apoya en un rasgo de la obra."),
        ("abc", "{F} ¿Cuál es el mejor modo de cerrar una discusión entre L y la lectura rival?", "Comparar evidencia, coherencia y riqueza, y reconocer lo que cada una ilumina", "Declarar un ganador sin razones", "Dejar de hablar", "Una conclusión con matices reconoce lo que cada lectura ilumina y lo que deja sin explicar."),
    ],
    ctx=("abc", "Dos estudiantes ficticias debaten sobre el final de «Círculo». Una dice que el cambio de dirección es renovación del grupo; la otra, que simplemente es un efecto visual. ¿Qué pregunta ayuda a avanzar?", "¿Qué otros rasgos de la obra apoyan o debilitan cada lectura?", "¿Quién tiene más años de experiencia?", "¿Qué lectura es más popular?", "Buscar más evidencia permite comparar lecturas."),
    sc=[
        ("En Estética: ¿qué es una objeción al apoyo?", "Una que señala que la evidencia no alcanza o que otra lectura explica mejor", "Se responde con rasgos de la obra."),
        ("¿Por qué pluralidad de lecturas no es relativismo total?", "Porque algunas lecturas son razonables y otras están mal apoyadas", "Las lecturas razonables se comparan con criterios y no todas están igual de apoyadas."),
        ("¿Qué puede hacer una réplica sólida?", "Reconocer límites, precisar la evidencia y comparar con la lectura rival", "Conversa con la obra y con otras lecturas."),
    ],
    op=("Toma la Lectura L de «Círculo» y escribe: la objeción más fuerte que se le puede hacer, tu réplica con un rasgo de la obra, una lectura rival con su evidencia y una evaluación final que diga cuál te parece mejor apoyada y qué evidencia te haría cambiar de opinión.",
        "Objeción: el cambio de dirección al final no se explica. Réplica: puede leerse como el grupo transformado por el regreso. Lectura rival: es sobre el movimiento circular de la naturaleza; evidencia: el giro. Mejor apoyada: L, por salir y volver. Cambiaría de opinión si se supiera que la coreografía nunca incluyó la salida.",
        ["la objeción es pertinente", "la réplica usa un rasgo de la obra", "la lectura rival tiene evidencia", "indica qué evidencia le haría cambiar de opinión"],
        ["objeción, réplica, lectura rival y evaluación final"],
        ["no usar evidencia", "presentar una lectura rival sin apoyo", "no decir qué evidencia le haría cambiar de opinión"],
        "Pregunta: «¿qué rasgo de la obra respalda tu réplica?». Pídele que lo marque."),
    reinforce="Elige una canción, afiche o escena y escribe una lectura, una objeción posible y una réplica.",
    extend="Explica por qué dejar abierta una pregunta sobre la obra puede ser parte de una buena interpretación.",
)
