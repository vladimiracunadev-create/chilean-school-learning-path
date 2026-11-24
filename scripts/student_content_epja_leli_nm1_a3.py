"""Lengua y Literatura EPJA Media N1, módulo 1, OAD-03: construir una interpretación de una obra a partir de su análisis. Todos los cuentos y datos son inventados y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los cuentos, fichas y opiniones de este cuaderno son inventados («de ejemplo») y están escritos en cada ejercicio: "
    "no necesitas libros, audio, video ni internet. Si algo te cuesta leer, pide que te lo lean en voz alta; pedir apoyo es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)
build = make_build(MATERIALS)

O = "EPJA-LELI-NM1-OAD-03"
PRIOR = ["Sé contar de qué trata un cuento.", "Reconozco personajes, lugar y hechos de una historia.", "He dicho alguna vez «eso significa que...» después de ver un gesto o una escena."]

SILLA = ("Cuento (inventado), «La silla vacía»: En la cocina de doña Amanda había tres sillas. Cada domingo ponía tres platos, aunque solo almorzaban ella y su nieto. "
         "Esa tarde, el niño preguntó por qué ponía un plato de más. Ella acomodó la cuchara junto al plato vacío y respondió: «Por si alguien llega».")
HIGUERA = ("Cuento (inventado), «La higuera»: Cuando la familia vendió la casa del pasaje, solo Olga volvió una vez al patio. La higuera seguía allí, con sus hojas anchas. "
           "Tocó el tronco con la palma de la mano, recogió dos higos del suelo y los guardó en el bolsillo del delantal. Al salir, cerró el portón sin hacer ruido.")
PUENTE = ("Cuento (inventado), «El puente de tablas»: Para cruzar el estero, los vecinos del cerro usaban un puente de tablas. Cada invierno el agua se llevaba alguna. "
          "Cada primavera, Julián y su hija salían con martillo y clavos a reponerlas, y nadie les pedía que lo hicieran. Un año llegó una cuadrilla de la municipalidad a construir un puente de cemento. "
          "Julián miró cómo trabajaban, guardó su martillo en la caja y, al caer la tarde, cruzó por última vez el puente viejo, despacio, tocando cada tabla. "
          "Ficha de contexto (inventada): el autor ficticio escribió el cuento en una época en que muchos barrios pasaron de caminos de tierra a obras públicas.")
CUADERNO = ("Cuento (inventado), «El cuaderno de Rosa»: Rosa volvió a la escuela nocturna siendo adulta. El primer día se sentó atrás y escondió su cuaderno bajo el brazo. "
            "Cuando la profesora pidió que alguien leyera su párrafo, Rosa bajó la mirada. Al terminar la clase, un compañero le dijo que su letra era clara. "
            "Al día siguiente se sentó adelante y dejó el cuaderno abierto sobre la mesa. "
            "Ficha de contexto (inventada): el autor ficticio fue profesor en escuelas nocturnas y escribió el cuento para quienes vuelven a estudiar.")
LETRERO = ("Cuento (inventado), «El letrero»: Don Mario pintó con esmero el letrero de su almacén: «Almacén El Encuentro». Pasaron los años y la lluvia borró las letras, pero los vecinos seguían diciendo «voy donde don Mario». "
           "Un día su sobrina propuso repintarlo. Don Mario miró la pared descascarada, pensó un momento y respondió: «Déjalo así; el que me busca, me encuentra». "
           "Ficha de contexto (inventada): en el barrio del cuento, los almacenes eran también lugares donde los vecinos se reunían a conversar.")
GLADYS = ("Cuento (inventado), «El último turno de Gladys»: Gladys trabajó treinta años en la fábrica de conservas. En su último turno limpió su máquina con más cuidado que nunca y dejó sobre ella una cinta roja. "
          "Al salir, sus compañeros la esperaban en la puerta con un pastel. Ella agradeció, pero antes de irse se dio vuelta una vez más para mirar la ventana iluminada. "
          "Interpretación A: «El cuento trata de una fábrica de conservas». "
          "Interpretación B: «Gladys se va contenta porque la fábrica era mala». "
          "Interpretación C: «El cuento muestra que dejar un trabajo de muchos años mezcla gratitud y pena: limpia su máquina con cuidado, deja una cinta roja y mira la ventana una vez más». "
          "Pauta: 1) propone un sentido global; 2) lo apoya con al menos dos citas o datos; 3) no contradice nada del texto.")


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(O, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ============================================================ clase 1
K(1, SILLA,
  "Hoy parto de lo que ya hago a diario: interpretar gestos y situaciones. Veo que interpretar un cuento es dar sentido con razones.",
  ["Todos los días interpretamos: cuando alguien deja una luz encendida, cuando una vecina no saluda, cuando una persona llega tarde. Miramos lo que pasa, pensamos qué podría significar y, si nos equivocamos, corregimos. Esa es la base de interpretar un texto.",
   "Interpretar un cuento es proponer qué significa en conjunto lo que ocurre, y mostrar en qué datos se apoya esa idea. Una interpretación no es lo mismo que un gusto: «me gustó» es una opinión; «el cuento muestra la soledad porque pone un plato de más» es una interpretación con razón.",
   "Una buena interpretación cumple dos cosas. Primero, está apoyada en el texto: usa datos o frases del cuento. Segundo, no lo contradice: no inventa hechos que el cuento no cuenta. En cambio, puede haber más de una interpretación posible si cada una se apoya en el texto."],
  [("interpretar", "dar sentido a lo que ocurre apoyándose en pistas"), ("pista", "dato del texto que ayuda a entender algo"), ("opinión", "juicio personal que no siempre se prueba"), ("razón", "motivo que sostiene una idea")],
  [("Del gesto a la idea", "Gesto del cuento: doña Amanda pone un plato de más. Se interpreta.",
    ["Observo: pone tres platos y solo almuerzan dos.", "Pregunto: ¿qué significa ese plato?", "Idea: espera a alguien o recuerda a quien no está; el plato es una pista."], "El plato de más muestra espera o recuerdo"),
   ("Opinión o interpretación", "Frase A: «Me gustó el cuento». Frase B: «El cuento muestra esperanza porque ella dice ‘por si alguien llega’».",
    ["A es un gusto, no explica el texto.", "B propone un sentido y cita una frase del cuento.", "B es una interpretación."], "A es opinión; B interpreta")],
  [("Decir «es sobre una señora que cocina» y creer que ya interpretó.", "Eso describe lo que pasa, no qué significa.", "Agrega qué podría significar el plato de más."),
   ("Inventar que el esposo de doña Amanda murió.", "El cuento no lo dice: es un hecho inventado.", "Usa solo lo que el cuento muestra y marca lo que supones como posibilidad.")],
  [("abc", "{F} ¿Cuántos platos pone doña Amanda cada domingo?", "Tres", "Dos", "Cuatro", "El cuento dice que ponía tres platos."),
   ("ab", "{F} ¿Quiénes almuerzan en realidad?", "Doña Amanda y su nieto", "Doña Amanda y tres invitados", "El texto dice que solo almorzaban ella y su nieto."),
   ("{F} ¿Qué responde doña Amanda cuando el niño pregunta por el plato de más? Escribe las cuatro palabras de su respuesta.", "Por si alguien llega", "La respuesta aparece entre comillas al final del cuento."),
   ("abc", "En Lengua y Literatura: ¿qué es interpretar un texto?", "Proponer qué significa en conjunto y apoyarlo en datos del texto", "Copiar el texto con otras palabras", "Decir si me gustó o no", "La interpretación une sentido y evidencia."),
   ("abc", "{F} ¿Cuál es una interpretación apoyada en el cuento?", "Doña Amanda mantiene la esperanza de que alguien llegue", "Doña Amanda no sabe cocinar", "Doña Amanda odia a su nieto", "Su respuesta «por si alguien llega» apoya la idea de esperanza."),
   ("ab", "{F} ¿Qué dato apoya la idea de que doña Amanda espera a alguien?", "Pone un plato de más cada domingo", "Su nieto le hace una pregunta", "Poner un plato extra de forma repetida muestra espera; la pregunta del nieto no prueba que espere a alguien."),
   ("abc", "Una vecina siempre deja la luz del pasillo encendida hasta tarde. Tú piensas que espera a alguien. ¿Qué haces para interpretar bien?", "Me fijo en otras pistas, como si mira por la ventana", "Afirmo que ella es insomne sin otros datos", "No pienso nada", "Una interpretación necesita más de una pista, no una suposición suelta."),
   ("abc", "{F} Una persona dice: «Doña Amanda es rica porque tiene tres sillas». ¿Qué problema tiene?", "El cuento no da ningún dato sobre su riqueza", "Tiene demasiadas palabras", "Es una frase demasiado breve", "No hay evidencia en el texto que sostenga la riqueza."),
   ("abc", "{F} Marca la frase que es una opinión y no una interpretación.", "«Este cuento me dio ternura»", "«El plato de más muestra espera»", "«La respuesta final muestra esperanza»", "La primera expresa un sentimiento, no explica el texto."),
   ("ab", "{F} Otra lectora dice: «Doña Amanda recuerda a alguien que ya no está». ¿Es una interpretación posible?", "Sí, el plato de más puede mostrar recuerdo, aunque el cuento no lo diga", "No, solo existe una interpretación del cuento", "Se apoya en la pista del plato; el cuento admite más de una lectura."),
   ("abc", "{F} ¿Qué significa que una interpretación «no contradiga» el texto?", "Que no afirme cosas opuestas a lo que el cuento muestra", "Que repita el texto igual", "Que sea muy larga", "Contradecir sería, por ejemplo, decir que ella almuerza sola."),
   ("abc", "{F} ¿Qué frase mejora «El cuento trata de una señora»?", "«El cuento muestra la espera con el plato de más»", "«El cuento trata de platos»", "«El cuento tiene cuatro líneas»", "Propone un sentido y se apoya en un detalle."),
   ("ab", "{F} Si el cuento dijera que doña Amanda espera a su hijo, ¿cambiaría la interpretación?", "Sí, se volvería más precisa: espera a un hijo", "No, el dato no importa", "Un dato nuevo permite afinar la idea de espera.")],
  ("abc", "En un grupo de trabajo, un compañero dice: «Ese cliente me miró raro, seguro me va a reclamar». ¿Qué mejoraría su manera de interpretar?", "Buscar más pistas antes de sacar una conclusión", "Dar por seguro que reclamará", "Ignorar al cliente", "Interpretar bien exige varias pistas, no solo una."),
  [("En Lengua y Literatura: ¿qué es una interpretación?", "Un sentido propuesto para el texto, apoyado en datos", "No basta con opinar: se necesita evidencia."),
   ("¿Qué dos condiciones tiene una buena interpretación?", "Se apoya en el texto y no lo contradice", "Una lectura así respeta lo que el texto muestra."),
   ("¿Puede haber más de una interpretación?", "Sí, si cada una se apoya en el texto", "El texto puede admitir lecturas distintas.")],
  ("Lee el cuento: {F} Escribe en tu cuaderno (1) una frase que diga qué significa el plato de más, (2) la cita o dato en que te apoyas y (3) una razón por la que tu idea no contradice el cuento.",
   "Significa que doña Amanda mantiene la esperanza de que alguien llegue. Me apoyo en «Por si alguien llega» y en que pone tres platos aunque son dos. No contradice el cuento porque ella misma dice que espera.",
   ["propone un sentido", "cita una frase o dato del cuento", "explica por qué no contradice"],
   ["tres frases"],
   ["opinar sin citar", "inventar hechos que el cuento no dice"],
   "Pregunta: «¿Qué dato del cuento prueba tu idea?»."),
  "Piensa en un gesto cotidiano de una persona que conoces y escribe qué crees que significa y por qué.",
  "Escribe una segunda interpretación del plato de más y compara con la tuya.")

# ============================================================ clase 2
K(2, HIGUERA,
  "Hoy conozco el vocabulario para interpretar: tema, símbolo, evidencia, inferencia e hipótesis de interpretación.",
  ["Para interpretar con orden usamos palabras precisas. El tema es la idea general de la que trata el cuento, dicha en una palabra o frase corta, como «la memoria» o «la despedida». No es lo mismo que el argumento, que cuenta los hechos.",
   "Un símbolo es un objeto, lugar o gesto que representa una idea más amplia. En «La higuera», el árbol del patio puede representar la raíz de la familia o el recuerdo del hogar. Una inferencia es una idea que el texto no escribe, pero que se deduce de pistas. La evidencia es el dato o la cita que prueba lo que decimos.",
   "Una hipótesis de interpretación es una propuesta de sentido que luego comprobamos con evidencia. Por ejemplo: «La higuera representa el recuerdo de la casa; la evidencia es que Olga toca el tronco y guarda dos higos». Si la evidencia no alcanza, afinamos o cambiamos la hipótesis."],
  [("tema", "idea general de la que trata un texto"), ("símbolo", "objeto o gesto que representa una idea más amplia"), ("inferencia", "idea que se deduce de pistas, sin estar escrita"), ("hipótesis", "propuesta de sentido que se comprueba con evidencia")],
  [("Argumento y tema", "Cuento «La higuera». ¿Cuál es el argumento y cuál el tema?",
    ["Argumento: Olga vuelve al patio de la casa vendida y se lleva dos higos.", "Tema: la despedida del hogar o la memoria.", "El argumento cuenta hechos; el tema es la idea general."], "Argumento: hechos; tema: la despedida"),
   ("Hipótesis y evidencia", "Hipótesis: «La higuera simboliza el recuerdo de la casa». ¿Qué evidencia hay?",
    ["Olga toca el tronco con la palma de la mano.", "Guarda dos higos en su delantal.", "Cierra el portón sin hacer ruido: respeto al lugar."], "Tres evidencias de apego al lugar")],
  [("Confundir el tema con el argumento.", "El tema es una idea; el argumento cuenta los hechos.", "Pregunta «¿de qué idea trata?» para el tema y «¿qué pasa?» para el argumento."),
   ("Decir «la higuera es un árbol y nada más».", "Se ignora el posible significado simbólico.", "Pregunta qué idea podría representar el árbol en el cuento.")],
  [("abc", "{F} ¿Qué hace Olga con los higos?", "Los guarda en el bolsillo del delantal", "Los vende en la feria", "Los deja en el suelo", "El cuento dice que los guarda en el bolsillo."),
   ("ab", "{F} ¿Quién vuelve al patio después de vender la casa?", "Solo Olga", "Toda la familia", "El texto dice «solo Olga volvió una vez al patio»."),
   ("{F} ¿Cuántos higos recoge Olga? Escribe el número.", "2", "El cuento dice que recogió dos higos del suelo."),
   ("abc", "En Lengua y Literatura: ¿qué es un símbolo?", "Un objeto o gesto que representa una idea más amplia", "Un tipo de rima", "El título de un libro", "El símbolo representa una idea más allá del objeto."),
   ("abc", "{F} ¿Cuál es el tema más apoyado del cuento?", "La despedida de un lugar querido", "Las ventajas de vender una casa", "La fruta del invierno", "Olga se despide de la casa y del patio."),
   ("ab", "{F} ¿Qué puede simbolizar la higuera?", "El recuerdo del hogar", "Un negocio de frutas", "El árbol sigue allí cuando la familia ya se fue, como el recuerdo."),
   ("abc", "En Lengua y Literatura: ¿qué es una inferencia?", "Una idea que se deduce de pistas aunque no esté escrita", "Una cita copiada", "Una palabra con rima", "Se infiere a partir de lo que el texto sí dice."),
   ("abc", "{F} ¿Qué se puede inferir de que Olga cierre «sin hacer ruido» el portón?", "Que trata el lugar con respeto o cuidado", "Que está enojada con la familia", "Que quiere que todos la oigan", "Cerrar sin ruido es un gesto cuidadoso."),
   ("abc", "{F} Marca la evidencia que apoya la hipótesis «Olga siente apego por la higuera».", "Toca el tronco con la palma de la mano", "La higuera tiene hojas anchas", "La familia vendió la casa", "Tocar el tronco es un gesto de cariño."),
   ("ab", "{F} Una lectora dice: «La higuera simboliza una guerra». ¿Qué falta?", "Evidencia del cuento que apoye esa idea", "Más hojas en la higuera", "El cuento no tiene ningún dato sobre guerras, por eso carece de apoyo."),
   ("abc", "{F} ¿Cuál de estas es una hipótesis de interpretación bien formulada?", "«La higuera representa lo que queda de un hogar: Olga la toca y guarda higos»", "«La higuera es un árbol»", "«A mí me gustan los higos»", "Propone un sentido y señala evidencias."),
   ("abc", "{F} ¿Qué diferencia hay entre argumento y tema?", "El argumento cuenta los hechos; el tema es la idea general", "Son lo mismo", "El tema cuenta los hechos; el argumento es una idea", "El argumento narra y el tema abstrae."),
   ("ab", "{F} Si el cuento dijera que Olga arranca la higuera, ¿qué hipótesis cambiaría?", "La del apego: ya no estaría tan apoyada", "Ninguna, porque el símbolo no depende de los hechos", "Arrancar el árbol contradice la idea de cuidado y apego.")],
  ("abc", "Un compañero de tu taller dice que el cuento «La higuera» trata de una señora que recoge fruta. ¿Qué parte del análisis le falta?", "Decir qué podría significar ese gesto y apoyarlo", "Contar los árboles", "Cambiar la palabra «higuera»", "Describir los hechos no es lo mismo que interpretarlos."),
  [("En Lengua y Literatura: ¿qué es el tema de un cuento?", "La idea general de la que trata", "No cuenta hechos, expresa una idea."),
   ("En Lengua y Literatura: ¿qué es una evidencia?", "Un dato o cita del texto que sostiene una idea", "Prueba que la interpretación sale del texto."),
   ("¿Qué es una hipótesis de interpretación?", "Una propuesta de sentido que se comprueba con evidencia", "Si no se comprueba, se ajusta.")],
  ("Lee el cuento: {F} Escribe en tu cuaderno (1) el argumento en una oración, (2) el tema en una frase corta, (3) un posible símbolo y qué representa y (4) una evidencia exacta del cuento.",
   "Argumento: Olga vuelve al patio de la casa vendida y se lleva dos higos. Tema: la despedida del hogar. Símbolo: la higuera, que representa el recuerdo de la casa. Evidencia: «Tocó el tronco con la palma de la mano».",
   ["distingue argumento y tema", "propone un símbolo con su significado", "cita una evidencia exacta"],
   ["cuatro frases"],
   ["confundir tema y argumento", "decir un símbolo sin explicar qué representa"],
   "Pregunta: «¿Esa idea sale de algo que dice el cuento?»."),
  "Piensa en un objeto de tu casa que guarde un recuerdo y di qué representa.",
  "Escribe una hipótesis de interpretación sobre el portón del cuento.")

# ============================================================ clase 3
K(3, PUENTE,
  "Hoy aprendo, paso a paso, a pasar del análisis a una interpretación: observar, preguntar, proponer una hipótesis y comprobarla con evidencia y contexto.",
  ["Interpretar con método evita los saltos al azar. Hay seis pasos. Uno: lee y resume qué ocurre. Dos: anota los detalles que llaman la atención. Tres: pregunta qué podrían significar. Cuatro: formula una hipótesis. Cinco: compruébala con citas y con el contexto. Seis: escribe tu interpretación.",
   "En «El puente de tablas», los detalles llamativos son varios. Nadie les pide a Julián y a su hija que repongan las tablas, y lo hacen cada primavera. Después llega un puente de cemento. Al final, Julián cruza despacio, tocando cada tabla. Podemos preguntar: ¿qué significa dejar el martillo y tocar las tablas?",
   "Una hipótesis posible es: «El cuento muestra el valor del trabajo voluntario de los vecinos y la pena de verlo reemplazado por una obra pública». Se comprueba con las citas y con la ficha de contexto sobre los barrios que pasaban a obras públicas. Si una cita contradice la hipótesis, hay que revisarla."],
  [("detalle llamativo", "dato que sobresale y merece una pregunta"), ("comprobar", "verificar con pruebas si una idea es correcta"), ("obra pública", "construcción hecha por una institución para la comunidad"), ("voluntario", "que se hace por decisión propia y sin que lo pidan")],
  [("Paso 2 y 3", "Detalle: «cruzó por última vez el puente viejo, despacio, tocando cada tabla». Pregunta: ¿qué significa?",
    ["Observo: va despacio y toca las tablas.", "Pregunto: ¿por qué las toca?", "Idea provisional: se despide de algo que cuidó."], "Se despide de lo que cuidó"),
   ("Paso 5: comprobar", "Hipótesis: «El cuento muestra la pena de ver reemplazado un trabajo voluntario por una obra pública». Se comprueba.",
    ["Cita: «nadie les pedía que lo hicieran».", "Cita: «guardó su martillo en la caja».", "Contexto: muchos barrios pasaban a obras públicas."], "Hipótesis apoyada por dos citas y el contexto")],
  [("Saltar del resumen a una conclusión sin anotar detalles.", "Se pierden pistas importantes.", "Anota primero los detalles llamativos."),
   ("Ignorar la ficha de contexto.", "El contexto puede aclarar el sentido de lo que ocurre.", "Úsala para comprobar si tu hipótesis es coherente con la época.")],
  [("abc", "{F} ¿Con qué se cruzaba el estero antes de la obra nueva?", "Con un puente de tablas", "Con una lancha", "Con un puente de cemento", "El cuento dice que usaban un puente de tablas."),
   ("ab", "{F} ¿Quiénes reponían las tablas cada primavera?", "Julián y su hija", "La cuadrilla de la municipalidad", "El cuento dice que Julián y su hija salían con martillo y clavos."),
   ("{F} ¿Cuántos pasos tiene el método de interpretación de hoy? Escribe el número.", "6", "El método tiene seis pasos numerados."),
   ("abc", "En Lengua y Literatura: ¿qué se hace en el paso 5 del método?", "Comprobar la hipótesis con citas y contexto", "Escribir el resumen", "Anotar los detalles", "El paso cinco es la comprobación."),
   ("abc", "{F} ¿Qué detalle del cuento es llamativo?", "Que nadie les pedía a Julián y su hija que repusieran las tablas", "Que el estero tenía agua", "Que había un cerro", "Ese hecho sugiere un trabajo hecho por voluntad propia."),
   ("ab", "{F} ¿Qué muestra que Julián se despide del puente viejo?", "Lo cruza despacio, tocando cada tabla", "Saca fotos de las tablas", "El gesto de tocar cada tabla expresa despedida y cariño."),
   ("abc", "{F} ¿Qué cita apoya la idea de que el trabajo de Julián era voluntario?", "«nadie les pedía que lo hicieran»", "«llegó una cuadrilla de la municipalidad»", "«un puente de cemento»", "La cita dice que nadie se lo pedía."),
   ("abc", "{F} ¿Cuál es una hipótesis bien formulada?", "El cuento muestra la pena de que un trabajo comunitario sea reemplazado por una obra pública", "El cuento trata de un puente", "Julián vive en un cerro", "Propone un sentido global y se puede comprobar."),
   ("abc", "{F} ¿Qué aporta la ficha de contexto a esa hipótesis?", "Muestra que en esa época muchos barrios pasaban a obras públicas", "Dice cuántos clavos usó Julián", "Aclara cómo se llamaba el estero", "Conecta el cambio del cuento con la época del autor."),
   ("ab", "{F} Una lectora propone: «El cuento critica a la municipalidad porque es mala». ¿Está apoyada?", "No, el cuento no dice que la obra sea mala, solo que reemplaza el puente", "Sí, porque la cuadrilla llega sin avisar", "El texto muestra el cambio, pero no dice que la obra fuera dañina."),
   ("abc", "{F} ¿Qué paso del método falta en esta conclusión: «El cuento significa la pena del cambio»?", "Comprobarla con citas", "Leer el título", "Contar las palabras", "No hay evidencia citada que apoye la conclusión."),
   ("abc", "{F} ¿Qué cita relaciona al protagonista con su trabajo?", "«guardó su martillo en la caja»", "«un estero»", "«el cerro»", "El martillo guardado muestra que su trabajo termina."),
   ("ab", "{F} Si Julián fuera pagado por la municipalidad para cuidar el puente, ¿cambiaría la hipótesis?", "Sí, ya no sería un trabajo voluntario", "No, nada cambia", "El carácter voluntario es parte de la hipótesis y se perdería.")],
  ("abc", "En una reunión de vecinos se debate una obra nueva en la plaza. Alguien dice: «Hay que escuchar qué significa para quienes cuidaban el lugar». ¿Cómo se parece esto a interpretar un cuento?", "Se buscan pistas y razones antes de sacar conclusiones", "No hay ninguna relación", "Se prefiere callar a todos", "Interpretar es mirar pistas y razones, tanto en un cuento como en una decisión comunitaria."),
  [("En Lengua y Literatura: ¿cuál es el primer paso para interpretar?", "Leer y resumir qué ocurre", "Primero hay que comprender lo que pasa."),
   ("¿Qué se hace con un detalle llamativo?", "Preguntar qué podría significar", "El detalle abre la pregunta que lleva a la hipótesis."),
   ("¿Para qué sirve la ficha de contexto?", "Para comprobar si la hipótesis coincide con la época del cuento", "El contexto ayuda a aclarar el sentido.")],
  ("Lee el cuento: {F} Aplica el método. Escribe (1) un resumen de dos líneas, (2) dos detalles llamativos, (3) una hipótesis de interpretación, (4) dos citas exactas que la apoyen y (5) un dato de contexto que ayude.",
   "Resumen: Julián y su hija cuidan un puente de tablas hasta que llega uno de cemento. Detalles: nadie se lo pedía; cruza tocando cada tabla. Hipótesis: el cuento muestra la pena de ver reemplazado un trabajo voluntario por una obra pública. Citas: «nadie les pedía que lo hicieran»; «tocando cada tabla». Contexto: los barrios pasaban a obras públicas.",
   ["cinco partes completas", "citas exactas", "hipótesis coherente con la ficha de contexto"],
   ["cinco puntos escritos"],
   ["saltar pasos", "no usar el contexto"],
   "Pregunta: «¿Qué cita de tu lista prueba tu hipótesis?»."),
  "Cuenta con tus palabras los seis pasos del método a otra persona.",
  "Escribe una segunda hipótesis posible para el mismo cuento y búscale una cita.")

# ============================================================ clase 4
K(4, CUADERNO,
  "Hoy practico con apoyo: elijo entre varias interpretaciones la que mejor se apoya en el texto y la completo con evidencia y contexto.",
  ["Ya conoces los pasos para interpretar. Hoy practicas juntos: comparas tres interpretaciones de un mismo cuento y decides cuál está mejor sostenida. Una interpretación sólida tiene tres rasgos: propone un sentido global, cita evidencias del texto y es coherente con el contexto.",
   "Una forma de comparar es usar una tabla de tres columnas: hipótesis, evidencia del texto y dato de contexto. Si la columna de evidencia está vacía, la hipótesis es débil. Si hay evidencias pero contradicen otra parte del cuento, tampoco convence.",
   "Cuando trabajes con otra persona, escucha su idea con respeto y pregunta «¿en qué parte del cuento ves eso?». Así se aprende de las lecturas de otras personas sin necesidad de imponer la propia. Si dos lecturas se apoyan bien, puedes mantener las dos."],
  [("coherente", "que no se contradice y tiene sentido en conjunto"), ("sólida", "bien apoyada en pruebas"), ("débil", "con poco apoyo o sin pruebas"), ("tabla de comprobación", "cuadro que une hipótesis, evidencia y contexto")],
  [("Elegir la mejor interpretación", "Interpretaciones: A) «Rosa abandona la escuela». B) «Rosa gana confianza». C) «El cuento trata de una escuela nocturna».",
    ["A: contradice que al día siguiente se sienta adelante.", "C: describe el lugar y no propone un sentido.", "B: apoyada por sentarse adelante y dejar el cuaderno abierto."], "La B es la mejor sostenida"),
   ("Completar la tabla", "Hipótesis B: «Rosa gana confianza». ¿Qué evidencias y contexto?",
    ["Evidencia: «se sentó atrás» y después «se sentó adelante».", "Evidencia: escondió su cuaderno y luego «dejó el cuaderno abierto sobre la mesa».", "Contexto: el autor escribió para quienes vuelven a estudiar."], "Dos evidencias y un contexto")],
  [("Elegir la interpretación que más me gusta, aunque no tenga apoyo.", "Gustar no es probar.", "Elige la que tenga más evidencia y menos contradicciones."),
   ("Tomar una parte del cuento y olvidar el resto.", "La interpretación debe explicar todo el texto.", "Revisa que la idea sirva para el inicio, el medio y el final.")],
  [("abc", "{F} ¿Dónde se sentó Rosa el primer día?", "Atrás", "Adelante", "Junto a la profesora", "El cuento dice que se sentó atrás."),
   ("ab", "{F} ¿Qué dijo un compañero sobre su letra?", "Que era clara", "Que era pequeña", "El cuento indica que un compañero le dijo que su letra era clara."),
   ("{F} ¿Cuántos días distintos se mencionan en el cuento? Escribe el número.", "2", "Se cuentan el primer día y el día siguiente."),
   ("abc", "{F} ¿Cuál interpretación se apoya mejor en el cuento?", "Rosa gana confianza poco a poco", "Rosa abandona la escuela", "Rosa nunca habla con nadie", "El cambio de lugar y de actitud muestra confianza."),
   ("abc", "{F} ¿Qué evidencia apoya la idea de que Rosa gana confianza?", "Al día siguiente deja el cuaderno abierto sobre la mesa", "El cuento se llama «El cuaderno de Rosa»", "La profesora pidió que alguien leyera", "Antes escondía el cuaderno y después lo deja a la vista."),
   ("ab", "{F} ¿Qué interpretación solo describe y no interpreta?", "«El cuento trata de una escuela nocturna»", "«Rosa gana confianza»", "Nombra el lugar, pero no propone qué significa lo que ocurre."),
   ("abc", "{F} ¿Qué dato de la ficha de contexto ayuda?", "El autor escribió para quienes vuelven a estudiar", "El cuento tiene tres párrafos", "Rosa tiene un compañero", "Muestra que el cuento da ánimo a quienes retoman estudios."),
   ("abc", "{F} Una lectora dice: «Rosa se avergüenza de saber poco». ¿Qué problema tiene?", "El cuento no dice que sepa poco: hay una suposición", "Es demasiado corta", "No tiene verbos", "El texto muestra timidez, no falta de saber."),
   ("abc", "{F} ¿Qué evidencia sirve para la idea «Rosa era tímida al comienzo»?", "Bajó la mirada cuando la profesora pidió leer", "Se sentó adelante al día siguiente", "Un compañero elogió su letra", "Bajar la mirada es un gesto de timidez."),
   ("ab", "{F} Un compañero propone: «Rosa se siente valorada cuando alguien nota su letra». ¿Es una lectura compatible?", "Sí, se apoya en el elogio del compañero", "No, contradice el cuento", "El elogio ocurre antes de que ella cambie de lugar."),
   ("abc", "{F} ¿Qué pasa si una interpretación no explica el final?", "Es incompleta y conviene ajustarla", "Está perfecta", "Debe ser la única válida", "Una buena interpretación explica todo el cuento."),
   ("abc", "{F} ¿Qué columna de la tabla de comprobación está vacía en «Rosa abandona la escuela»?", "La de evidencia del texto", "La de hipótesis", "La del título", "No hay ninguna cita del cuento que muestre abandono."),
   ("ab", "{F} Si el cuento terminara con Rosa saliendo sin mirar a nadie, ¿qué cambiaría?", "La hipótesis de la confianza perdería apoyo", "Nada, porque la idea no depende del final", "El final es evidencia fundamental para la idea de crecimiento.")],
  ("abc", "En un grupo de estudio, dos personas leen distinto un cuento y ambas citan el texto. ¿Qué actitud es la mejor?", "Escuchar las dos lecturas y comprobar sus evidencias", "Decidir cuál es la única correcta", "No hablar más del cuento", "Si ambas se apoyan en el texto, se respeta la diversidad de lecturas."),
  [("En Lengua y Literatura: ¿qué tres rasgos tiene una interpretación sólida?", "Propone sentido, cita evidencias y es coherente con el contexto", "Esos tres rasgos permiten comprobarla con claridad."),
   ("¿Qué columnas tiene la tabla de comprobación?", "Hipótesis, evidencia y contexto", "Une cada idea con su apoyo."),
   ("¿Qué pregunta se hace a otra persona sobre su interpretación?", "¿En qué parte del cuento ves eso?", "Pide la evidencia de su lectura.")],
  ("Lee el cuento: {F} Haz una tabla con tres columnas (hipótesis, evidencia del texto, contexto) para la hipótesis «Rosa gana confianza». Agrega dos evidencias exactas y un dato de contexto. Después escribe en una oración por qué esta hipótesis es mejor que «Rosa abandona la escuela».",
   "Hipótesis: Rosa gana confianza. Evidencias: «se sentó atrás» frente a «se sentó adelante»; «escondió su cuaderno» frente a «dejó el cuaderno abierto». Contexto: el autor escribió para quienes vuelven a estudiar. Es mejor porque «abandona» no tiene ninguna cita y contradice que vuelva al día siguiente.",
   ["tabla con tres columnas", "dos evidencias exactas", "justifica por qué la otra hipótesis es más débil"],
   ["una tabla y una oración"],
   ["no citar", "no justificar la comparación"],
   "Pregunta: «¿Qué parte del cuento contradice la otra hipótesis?»."),
  "Cuenta a otra persona cómo cambia Rosa de un día al otro, usando dos citas.",
  "Inventa un final distinto para el cuento y di qué interpretación respaldaría.")

# ============================================================ clase 5
K(5, LETRERO,
  "Hoy aplico lo aprendido a una situación de comunidad: escribo una interpretación breve de un cuento para compartirla en el boletín de un taller de lectura.",
  ["Interpretar un cuento sirve también para conversar en la comunidad. En un taller de lectura, un boletín del barrio o una reunión, una interpretación bien dicha ayuda a otras personas a ver algo que no habían notado. No hace falta usar palabras difíciles: hace falta claridad y pruebas.",
   "Una interpretación para compartir tiene cuatro partes. Primero, la idea principal en una oración. Segundo, una o dos evidencias con cita exacta. Tercero, un dato de contexto que aclare el sentido. Cuarto, un cierre que invite a pensar o a conversar.",
   "En «El letrero», un letrero borrado puede parecer solo un descuido. Con el dato de que el almacén era un lugar de encuentro, la respuesta de don Mario toma otro sentido: el almacén importa por las personas que lo buscan, no por la pintura. Así, el contexto cambia lo que vemos."],
  [("boletín", "hoja o publicación breve para informar a un grupo"), ("idea principal", "la idea más importante que sostiene un texto"), ("cierre", "parte final que remata o invita a pensar"), ("encuentro", "reunión o lugar donde las personas se juntan")],
  [("Idea principal y evidencia", "Interpretación: «El almacén vale por la gente que lo busca, no por su letrero». Evidencia: «los vecinos seguían diciendo ‘voy donde don Mario’».",
    ["Idea principal en una oración.", "Evidencia con cita exacta.", "Los vecinos siguen llegando aunque no se lea el letrero."], "Idea con evidencia"),
   ("Sumar el contexto", "Dato de contexto: los almacenes eran lugares de encuentro. ¿Cómo ayuda?",
    ["Explica por qué los vecinos van aunque el letrero esté borrado.", "Refuerza la idea de comunidad.", "Cambia lo que parece un descuido."], "El contexto explica el valor del lugar")],
  [("Escribir una interpretación sin una cita.", "Los lectores no pueden comprobarla.", "Agrega una frase exacta del cuento."),
   ("Usar palabras difíciles para parecer más serio.", "Se pierde claridad para la audiencia.", "Escribe con frases cortas y simples.")],
  [("abc", "{F} ¿Qué dice el letrero original?", "«Almacén El Encuentro»", "«Almacén Don Mario»", "«Almacén del Barrio»", "El cuento dice que el letrero decía «Almacén El Encuentro»."),
   ("ab", "{F} ¿Qué había pasado con las letras del letrero?", "La lluvia las borró", "Alguien las repintó", "El cuento dice que la lluvia borró las letras."),
   ("{F} ¿Quién propone repintar el letrero? Escribe una sola palabra.", "sobrina", "El cuento dice que su sobrina propuso repintarlo."),
   ("abc", "{F} ¿Qué respondió don Mario cuando su sobrina propuso repintar el letrero?", "«Déjalo así; el que me busca, me encuentra»", "«Repíntalo hoy mismo»", "«No me importa lo que digan»", "Es la frase entre comillas al final del cuento."),
   ("abc", "{F} ¿Cuál es la idea principal mejor apoyada?", "El almacén vale por las personas que lo buscan, no por el letrero", "Los letreros siempre se deben repintar", "Don Mario es descuidado", "Los vecinos siguen llegando aunque el letrero no se lea."),
   ("ab", "{F} ¿Qué cita apoya la idea de comunidad?", "«los vecinos seguían diciendo ‘voy donde don Mario’»", "«la lluvia borró las letras»", "Muestra que la gente reconoce el almacén por su dueño y no por el letrero."),
   ("abc", "{F} ¿Cómo ayuda el dato de contexto a entender la respuesta de don Mario?", "Explica que el almacén era un lugar de encuentro de vecinos", "Dice cuánto cuesta la pintura", "Cuenta cuántos años tiene el almacén", "Si el almacén es un lugar de encuentro, el letrero no es tan importante."),
   ("abc", "{F} ¿Qué parte tendría un cierre adecuado para el boletín?", "«¿Qué lugares de tu barrio importan por quienes los visitan?»", "«Fin»", "«El cuento tiene una pared»", "Un buen cierre invita a pensar en la propia experiencia."),
   ("abc", "{F} ¿Qué simboliza el nombre «El Encuentro» del almacén?", "La unión de los vecinos", "Una marca comercial", "Una fecha importante", "El nombre se conecta con el rol del lugar."),
   ("ab", "{F} Un lector dice: «Don Mario no repinta porque no tiene dinero». ¿Qué le falta?", "Una cita o dato del cuento que apoye esa idea", "Más palabras difíciles", "El cuento no dice nada sobre el dinero; falta evidencia."),
   ("abc", "{F} Si el cuento dijera que nadie visita el almacén desde que se borró el letrero, ¿qué ocurriría con la interpretación?", "La idea de que vale por la gente perdería apoyo", "Se confirmaría totalmente", "No cambiaría nada", "Cambiaría la evidencia principal de la interpretación."),
   ("abc", "{F} ¿Qué frase de apertura es clara para un boletín?", "«En ‘El letrero’, un almacén importa más por su gente que por su pintura»", "«Se evidencia una polisemia estructural del signo»", "«Este cuento es lindo»", "La primera dice la idea de forma simple."),
   ("ab", "{F} ¿Qué parte del boletín muestra de dónde viene la idea?", "La cita exacta del cuento", "El título del boletín", "La cita demuestra que la idea sale del texto.")],
  ("abc", "Te piden escribir tres líneas en el boletín de tu centro sobre un cuento leído en el taller. ¿Qué incluyes?", "La idea principal, una cita y un cierre", "Solo tu opinión sin pruebas", "Una copia del cuento completo", "Una interpretación breve necesita idea, evidencia y cierre."),
  [("En Lengua y Literatura: ¿qué partes tiene una interpretación para compartir?", "Idea principal, evidencia, contexto y cierre", "Son cuatro partes simples y fáciles de recordar."),
   ("¿Por qué conviene usar frases simples?", "Para que cualquier lector entienda la idea", "La claridad ayuda a compartir la interpretación."),
   ("¿Qué aporta el dato de contexto?", "Ayuda a entender mejor el sentido de lo que ocurre", "Explica por qué el cuento puede significar eso.")],
  ("Lee el cuento: {F} Escribe una interpretación de cinco o seis líneas para el boletín del taller: idea principal, una cita exacta, el dato de contexto y un cierre con una pregunta para el grupo. No uses datos personales.",
   "En «El letrero», un almacén importa más por su gente que por su pintura. Los vecinos «seguían diciendo ‘voy donde don Mario’» aunque no se leía el letrero. Como los almacenes eran lugares de encuentro, don Mario sabe que lo importante es el vínculo. ¿Qué lugares de tu barrio valen por las personas que los visitan?",
   ["idea principal clara", "cita exacta", "dato de contexto y cierre con pregunta"],
   ["un texto de cinco o seis líneas"],
   ["no citar", "no incluir el contexto"],
   "Pregunta: «¿Qué dato muestra que tu idea sale del cuento?»."),
  "Lee tu texto en voz alta a alguien y pregúntale si se entiende la idea principal.",
  "Escribe otra frase de cierre con una pregunta distinta para el boletín.")

# ============================================================ clase 6
K(6, GLADYS,
  "Hoy reviso lo logrado: evalúo interpretaciones con una pauta, ajusto una según cambie una condición y decido qué practicar.",
  ["Llegamos al cierre del recorrido: aprendimos a observar detalles, a formular hipótesis, a comprobarlas con evidencia y contexto y a escribirlas con claridad. Hoy aplicamos una pauta para evaluar interpretaciones y para mejorar las propias.",
   "La pauta tiene tres criterios: propone un sentido global, lo apoya con al menos dos citas o datos y no contradice nada del texto. Una interpretación que cumple los tres es sólida. Una que solo describe no interpreta. Una que contradice el cuento debe corregirse.",
   "También conviene preguntar qué pasaría si una condición cambia. Si el cuento dijera otra cosa, ¿mi conclusión seguiría igual? Una interpretación bien pensada se ajusta cuando cambia la evidencia. Eso no es debilidad: es honestidad con el texto."],
  [("pauta", "lista de criterios para evaluar"), ("condición", "dato o situación que puede cambiar una conclusión"), ("ajustar", "cambiar un poco una idea para que calce mejor con las pruebas"), ("honestidad", "decir lo que realmente se sostiene con las pruebas")],
  [("Aplicar la pauta a A", "Interpretación A: «El cuento trata de una fábrica de conservas». Se evalúa.",
    ["1) Propone un sentido global: no, solo nombra el lugar.", "2) Dos citas: no hay ninguna.", "3) No contradice: no hay nada que contradecir."], "Cumple solo el criterio 3"),
   ("Aplicar la pauta a C", "Interpretación C: gratitud y pena al dejar un trabajo, con tres detalles citados. Se evalúa.",
    ["1) Propone sentido global: sí.", "2) Cita limpieza, cinta roja y mirada: sí.", "3) No contradice: la fábrica era un lugar querido."], "Cumple los tres criterios")],
  [("Elegir la interpretación más larga como la mejor.", "El largo no prueba apoyo en el texto.", "Evalúa con la pauta."),
   ("Mantener una conclusión aunque cambien las pruebas.", "Se pierde honestidad con el texto.", "Ajusta la idea cuando la evidencia cambia.")],
  [("abc", "{F} ¿Cuántos años trabajó Gladys en la fábrica?", "Treinta", "Veinte", "Diez", "El cuento dice que trabajó treinta años."),
   ("ab", "{F} ¿Qué deja Gladys sobre su máquina?", "Una cinta roja", "Una carta", "El texto dice que dejó una cinta roja."),
   ("{F} ¿Cuántos criterios tiene la pauta? Escribe el número.", "3", "La pauta del enunciado numera tres criterios."),
   ("abc", "{F} ¿Qué interpretación cumple los tres criterios?", "La C", "La A", "La B", "La C propone un sentido, cita tres detalles y no contradice el texto."),
   ("abc", "{F} ¿Por qué la interpretación B contradice el cuento?", "Gladys limpia su máquina con cuidado y mira la ventana; no parece que odie el lugar", "Porque tiene un pastel", "Porque usa una cinta", "Los gestos de cuidado y de mirar atrás van en contra de que el lugar fuera malo."),
   ("ab", "{F} ¿Qué criterio no cumple la interpretación A?", "Proponer un sentido global", "No contradecir el texto", "Solo nombra el lugar sin decir qué significa lo ocurrido."),
   ("abc", "{F} ¿Qué dos detalles apoyan la idea de gratitud?", "Limpia su máquina con cuidado y agradece a sus compañeros", "Come pastel y se va", "Trabaja treinta años y llega tarde", "Esos gestos muestran cariño y reconocimiento."),
   ("abc", "{F} ¿Qué detalle apoya la idea de pena?", "Se da vuelta una vez más para mirar la ventana iluminada", "Los compañeros la esperan con pastel", "Trabajó treinta años en la fábrica", "Mirar atrás una vez más muestra despedida."),
   ("abc", "{F} ¿Qué pasaría con C si el cuento dijera que Gladys sale corriendo sin mirar atrás?", "Perdería apoyo la idea de pena", "No cambiaría nada", "Se confirmaría la gratitud", "La evidencia de la pena desaparecería del cuento."),
   ("ab", "{F} ¿Es correcto afirmar: «Gladys sintió pena» si el cuento no usa esa palabra?", "Sí, se infiere de sus gestos", "No, solo vale lo que el texto dice con esas palabras exactas", "La inferencia se apoya en detalles, aunque la palabra no aparezca."),
   ("abc", "{F} ¿Cómo se debería mejorar la interpretación A?", "Agregando qué significa el cierre de la carrera de Gladys y dos citas", "Repitiendo «fábrica»", "Quitándole el título", "Debe proponer un sentido y apoyarlo."),
   ("abc", "{F} Un estudiante dice que la C es mejor porque nombra tres detalles. ¿Qué tiene de cierto?", "Que tres detalles ofrecen más evidencia", "Que el largo siempre decide", "Que la B siempre es mejor", "Las pruebas dan fuerza a la interpretación."),
   ("ab", "{F} Si el cuento incluyera que Gladys no quiso ir a la despedida, ¿qué haría falta?", "Revisar la idea de gratitud", "No tocar nada", "Un dato nuevo puede cambiar la conclusión y obliga a ajustarla.")],
  ("abc", "En tu trabajo, el equipo debe decidir cómo despedir a una compañera que se jubila. ¿Qué actitud se parece a interpretar con pruebas?", "Escuchar distintas ideas y decidir según lo que hizo y valoró ella", "Imponer la idea de quien habla más fuerte", "Ignorar lo que ella dijo", "Decidir con evidencia y respeto es parecido a interpretar un cuento."),
  [("En Lengua y Literatura: ¿qué tres criterios tiene la pauta de hoy?", "Sentido global, dos citas y no contradecir el texto", "Esa pauta permite revisar cada interpretación."),
   ("¿Qué hago cuando cambia la evidencia?", "Reviso y ajusto mi conclusión", "Una buena lectura se adapta a las pruebas."),
   ("¿Para qué sirve evaluar mis interpretaciones?", "Para saber qué practicar", "Marca con claridad qué parte conviene mejorar.")],
  ("Aplica la pauta: {F} Evalúa la interpretación B con los tres criterios y reescríbela para que cumpla la pauta con dos citas exactas. Después escribe qué cambió si el cuento dijera que Gladys no quería dejar la fábrica.",
   "B no propone un sentido apoyado y contradice los gestos de cuidado. Reescritura: «Gladys deja su trabajo con gratitud y pena: ‘limpió su máquina con más cuidado que nunca’ y ‘se dio vuelta una vez más para mirar la ventana iluminada’». Si no quisiera dejar la fábrica, la pena sería más fuerte y la gratitud se debilitaría.",
   ["evalúa con los tres criterios", "dos citas exactas", "explica cómo cambia la conclusión"],
   ["una evaluación, una reescritura y una explicación"],
   ["no citar", "no explicar el efecto del cambio de condición"],
   "Pregunta: «¿Qué parte de tu idea cambia si cambia el dato?»."),
  "Revisa con la pauta una interpretación que hayas escrito en esta unidad.",
  "Elige un cuento corto que conozcas y escribe una hipótesis con una cita.")
