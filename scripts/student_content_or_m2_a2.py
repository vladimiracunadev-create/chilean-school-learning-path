"""Cuaderno del estudiante, 2.º medio Orientación: OA 03 (evaluación de riesgos y redes de apoyo)."""
from __future__ import annotations

from or_m2_common import M, T, W, lesson
from student_lessons import arith, ex

OA3 = "OR2M OA 03"

lesson(
    OA3, 1,
    "Una hoja y un lápiz. El caso de Rodrigo, un estudiante inventado, está escrito en la clase y en los ejercicios. Nadie debe contar experiencias propias.",
    "Aprenderé a examinar un caso ficticio con una posible situación de riesgo y a separar factores de riesgo, factores protectores y personas de apoyo. Sirve para evaluar un riesgo con datos antes de actuar.",
    ["Sé que mis decisiones tienen consecuencias (1.º medio).", "Sé que puedo pedir ayuda a una persona adulta de confianza."],
    [
        "Un riesgo es la posibilidad de que algo cause daño a la salud, a la integridad o a los vínculos de una persona. Algunos riesgos se relacionan con el consumo de sustancias, con conductas sexuales sin cuidado o con la violencia. Evaluar un riesgo es mirar qué podría pasar, qué tan probable es y qué tan grave sería, sin exagerar ni minimizar.",
        "En todo caso hay factores de riesgo, que aumentan la posibilidad de daño, y factores protectores, que la disminuyen. Por ejemplo, estar en un lugar sin personas adultas es un factor de riesgo. Tener un plan para volver a casa y una persona a quien llamar es un factor protector. También importan las redes de apoyo, que son las personas e instituciones a las que se puede pedir ayuda.",
        "Un caso ficticio se analiza en tercera persona, con los datos escritos, sin preguntar por la vida privada de nadie. Primero se anotan los hechos, luego se buscan los factores y al final se piensa quién puede ayudar. Si el riesgo es serio, el paso siguiente siempre es avisar a una persona adulta de confianza.",
    ],
    [("riesgo", "posibilidad de que algo cause daño"), ("factor de riesgo", "circunstancia que aumenta la posibilidad de daño"), ("factor protector", "circunstancia que disminuye la posibilidad de daño"), ("red de apoyo", "personas e instituciones a las que se puede pedir ayuda"), ("minimizar", "decir que algo es menos grave de lo que es")],
    [
        W("Clasificar un factor", "Rodrigo, personaje inventado, va a una fiesta de curso en una casa donde no habrá ninguna persona adulta. ¿Es un factor de riesgo o protector?", ["Sin adultos presentes, nadie puede intervenir si algo sale mal.", "Eso aumenta la posibilidad de daño."], "Factor de riesgo"),
        W("Separar hecho e interpretación", "Del caso: «Dos compañeros llevan bebidas alcohólicas» y «Seguro nadie se va a emborrachar». ¿Cuál es el hecho?", ["Llevar bebidas se puede observar y describir.", "«Seguro nadie…» es una predicción que minimiza el riesgo."], "El hecho es que dos compañeros llevan bebidas alcohólicas"),
    ],
    [
        M("Decir «no pasa nada» porque la mayoría lo hace.", "Se minimiza el riesgo y se usa la costumbre como prueba.", "Evalúa qué podría pasar y qué tan grave sería, sin importar cuántos lo hagan."),
        M("Creer que pedir ayuda es delatar.", "Se confunde cuidar a alguien con acusarlo.", "Avisar a una persona adulta de confianza protege a las personas en riesgo."),
    ],
    R=[
        ex("Tener el teléfono de una persona adulta de confianza para pedirle que te vaya a buscar, ¿es un factor de riesgo o protector?", "Protector", "Disminuye la posibilidad de daño porque hay a quién recurrir."),
        ex("¿Qué es un riesgo? A) La posibilidad de que algo cause daño B) Algo que ya causó un daño grave", "A", "El riesgo se refiere a lo que podría ocurrir."),
        ex("En Orientación: ¿una red de apoyo son las personas e instituciones a las que se puede pedir ayuda?", "Sí", "Esa es la definición de red de apoyo."),
    ],
    U=[
        ex("Un amigo dice: «Es solo una vez, no es riesgoso». ¿Qué error comete? A) Minimiza el riesgo B) Exagera el riesgo", "A", "Dice que no hay peligro sin evaluarlo."),
        ex("Para evaluar un riesgo hay que mirar qué tan probable y qué tan grave sería. ¿Cuál frase mira la gravedad? A) «Podría terminar en una pelea con heridas.» B) «Puede que llueva ese día.»", "A", "Habla de un daño y de cuán serio sería."),
        ex("¿Por qué el caso de Rodrigo se analiza en tercera persona? A) Para aprender sin exponer la vida privada de nadie B) Para evitar hablar del tema", "A", "Se puede estudiar el riesgo sin contar experiencias personales."),
    ],
    A=[
        ex("Clasifica con R (riesgo) o P (protector): 1) No hay personas adultas en la casa. 2) Rodrigo avisó a su casa dónde estará. 3) Hay más de 30 personas y poca luz. Escribe las letras en orden.", "R, P, R", "La 1 y la 3 aumentan la posibilidad de daño; la 2 deja una persona informada."),
        ex("Rodrigo ve que un compañero se siente mal después de tomar mucho alcohol. ¿Qué paso corresponde primero? A) Avisar de inmediato a una persona adulta B) Esperar a que se le pase solo", "A", "Una persona con mal estado necesita ayuda adulta sin demora."),
        ex("En la fiesta de ejemplo hay 24 invitados y 3 llevaron bebidas alcohólicas. ¿Cuántos invitados no las llevaron?", "21", "A los 24 invitados se les restan los 3 que las llevaron."),
    ],
    Z=[
        ex("¿Por qué conviene anotar primero los hechos antes de opinar sobre el caso?", "Porque así no se mezclan los datos con suposiciones y se evalúa el riesgo con lo que realmente ocurre", "Los hechos permiten una evaluación justa."),
        ex("Un compañero dice: «Si hay un factor protector, ya no hay riesgo». ¿Qué respondes? A) Lo protector lo disminuye, pero no lo elimina B) Tiene razón, desaparece por completo", "A", "Disminuir no es lo mismo que eliminar."),
    ],
    D=[
        arith("En un listado de ejemplo sobre una salida, hay 14 factores de riesgo y 9 protectores. ¿Cuántos factores tiene el listado?", "14+9", "Se suman los factores de riesgo y los protectores."),
        ex("Un amigo de Rodrigo dice que avisar a un adulto es «ser sapo». Escribe cuál de estas respuestas es mejor. A) «Avisar cuida a quien está en riesgo, no es acusar.» B) «Tienes razón, mejor no decir nada.»", "A", "Pedir ayuda protege la integridad de las personas."),
    ],
    context=[ex("En el recreo escuchas a unos estudiantes comentar un caso inventado: unos jóvenes se juntan de noche en una plaza oscura con alcohol. ¿Qué factor de riesgo nombra mejor el caso? A) Un lugar oscuro y sin adultos B) Que sean jóvenes", "A", "Es una circunstancia del lugar; ser joven no es un factor de riesgo en sí.")],
    selfcheck=[ex("En Orientación: ¿un factor protector disminuye la posibilidad de daño?", "Sí", "Ayuda a reducir el riesgo."), ex("¿Minimizar un riesgo es decir que es menos grave de lo que es?", "Sí", "Es un error de evaluación."), ex("¿Ante un riesgo serio hay que avisar a una persona adulta de confianza?", "Sí", "Así se busca ayuda competente.")],
    task=T("Lee el caso inventado: Pablo, de 16 años, recibe una invitación a una reunión en un patio sin personas adultas, donde algunos llevarán alcohol y otros vapeadores. Pablo no sabe quiénes irán. Escribe: (1) dos hechos del caso, (2) un factor de riesgo, (3) un factor protector que Pablo podría agregar y (4) a qué persona adulta de confianza podría contarle la invitación.", "Hechos: la reunión es sin adultos; algunos llevarán alcohol y vapeadores. Factor de riesgo: no hay personas adultas. Factor protector: avisar en su casa dónde estará y tener a quién llamar. Persona de confianza: alguien de su casa o la persona orientadora.", ["escribe dos hechos del caso", "nombra un factor de riesgo", "propone un factor protector", "indica una persona adulta de confianza"], ["texto escrito", "tabla"], ["mezclar hechos y suposiciones", "no nombrar a quién pedir ayuda"], "Reconoce los hechos bien separados y pregunta qué otra persona de apoyo podría sumar."),
    reinforce="Anota un factor de riesgo y uno protector de cualquier salida inventada al cine.",
    extend="Explica con un ejemplo inventado por qué un factor protector no elimina del todo el riesgo.",
)

lesson(
    OA3, 2,
    "Una hoja y un lápiz. Las afirmaciones y los datos están escritos en los ejercicios; los casos son inventados.",
    "Aprenderé a distinguir mitos, hechos y derechos sobre consumo de sustancias, conductas sexuales sin cuidado y violencia. Sirve para evaluar un riesgo con información confiable.",
    ["Sé evaluar un caso con factores de riesgo y protectores.", "Sé qué es una fuente confiable."],
    [
        "Un mito es una creencia que se repite pero no es verdadera, como «si todos lo hacen, no es peligroso». Un hecho se comprueba en una fuente confiable, como un centro de salud, un establecimiento educacional o un organismo público. Frente al consumo, es un hecho que en Chile la venta de alcohol y de tabaco a menores de 18 años está prohibida, y que las sustancias afectan más a un cuerpo que aún se está desarrollando.",
        "También es un hecho que mantener relaciones sexuales sin protección puede traer infecciones de transmisión sexual y embarazos no planificados, y que las dudas se consultan con profesionales de la salud, sin vergüenza. En cuanto a la violencia, los gritos, las amenazas, los golpes y la humillación no son una forma válida de resolver diferencias.",
        "Hay derechos que siempre valen: vivir sin violencia, decidir sobre tu cuerpo con consentimiento y recibir atención de salud. Un límite es una frontera personal que otros deben respetar, como decir «no quiero» sin explicar más. Nadie puede presionarte con burlas, chantaje o amenazas, y si ocurre, corresponde avisar a una persona adulta de confianza.",
    ],
    [("mito", "creencia repetida que no es verdadera"), ("hecho", "dato que se puede comprobar en una fuente confiable"), ("límite", "frontera personal que los demás deben respetar"), ("presión de grupo", "empuje del entorno para que alguien haga algo que no quiere"), ("infección de transmisión sexual", "enfermedad que se contagia por contacto sexual")],
    [
        W("Mito o hecho", "Una cadena de mensajes dice: «Los vapeadores no hacen daño a nadie». ¿Es un hecho confiable? Justifica.", ["No trae autor ni fuente.", "Una afirmación tan general necesita respaldo de una institución de salud."], "No es confiable: es un mito sin fuente"),
        W("Reconocer un derecho", "Una estudiante inventada dice: «No quiero que me graben». Otros se burlan. ¿Qué derecho ejerce?", ["Dice que no a algo que afecta su imagen.", "Los demás deben respetar ese límite."], "Su derecho a decidir sobre su imagen y su cuerpo"),
    ],
    [
        M("Creer que una afirmación es verdadera porque se repite mucho.", "Se confunde popularidad con prueba.", "Busca una fuente confiable antes de aceptar un dato."),
        M("Pensar que poner un límite arruina la amistad.", "Se cree que decir «no» es faltar el respeto.", "Un límite se puede decir con calma y quien te respeta lo acepta."),
    ],
    R=[
        ex("¿La venta de alcohol a menores de 18 años está prohibida en Chile? Responde sí o no.", "Sí", "Es una regla legal que protege a los menores de edad."),
        ex("«Si todos lo hacen, no es peligroso». ¿Es un mito o un hecho?", "Un mito", "La cantidad de personas no demuestra que algo sea seguro."),
        ex("Decir «no quiero» a algo que incomoda, ¿es poner un límite? Responde sí o no.", "Sí", "Un límite es una frontera personal que otros deben respetar."),
    ],
    U=[
        ex("¿Dónde conviene consultar dudas sobre salud sexual? A) En un centro de salud con profesionales B) En una cadena de mensajes sin autor", "A", "Los profesionales entregan información comprobada."),
        ex("Un compañero grita y amenaza para que otro le pase la tarea. ¿Qué es esa conducta? A) Violencia B) Una forma válida de pedir algo", "A", "Las amenazas dañan emocionalmente y no son un trato válido."),
        ex("¿Qué es la presión de grupo? A) El empuje del entorno para que alguien haga lo que no quiere B) Un trabajo en equipo", "A", "La persona siente que debe aceptar para no quedar fuera."),
    ],
    A=[
        ex("Clasifica con H (hecho) o M (mito): 1) «Las relaciones sin protección pueden traer infecciones.» 2) «Probar una vez no puede hacer daño.» 3) «Las amenazas son violencia.» Escribe las letras en orden.", "H, M, H", "La 1 y la 3 se respaldan en información de salud y convivencia; la 2 minimiza el riesgo sin prueba."),
        ex("Un grupo le dice a Isidora, personaje inventado: «Si no pruebas, no eres de los nuestros». ¿Qué respuesta pone un límite? A) «Gracias, yo no quiero.» B) «Bueno, pero solo esta vez.»", "A", "Dice que no sin dar espacio a la presión."),
        ex("En una encuesta anónima de ejemplo, 40 estudiantes marcaron si han sentido presión de grupo: 15 dijeron que sí. ¿Cuántos dijeron que no?", "25", "A los 40 se les restan los 15 que dijeron que sí."),
    ],
    Z=[
        ex("¿Por qué «es mi decisión» no sirve para ignorar un riesgo que puede dañar a otra persona?", "Porque los derechos de una persona terminan donde empiezan los de otra y hay que cuidar también a los demás", "Cuidar de sí mismo y de otros va de la mano."),
        ex("Un mensaje reenviado dice: «Fumar es sano». ¿Qué debes hacer antes de creerlo? A) Buscar la información en una fuente de salud confiable B) Compartirlo con tus amigos", "A", "Se verifica antes de creer o difundir."),
    ],
    D=[
        arith("En un taller de ejemplo hay 6 afirmaciones sobre riesgos. 4 son mitos. ¿Cuántas son hechos?", "6-4", "Al total se le restan los mitos."),
        ex("Una compañera insiste en que pruebes algo mientras tú dijiste que no. ¿Qué pasa con su insistencia? A) Es presión y no cambia tu límite B) Es cuidado y debes aceptar", "A", "Insistir después de un «no» no respeta tu decisión."),
    ],
    context=[ex("En el Consejo de Curso un estudiante dice: «Las peleas se arreglan a golpes». ¿Qué respuesta corresponde? A) «Los golpes son violencia y no resuelven el conflicto.» B) «Depende de quién gane.»", "A", "Afirma el derecho a vivir sin violencia.")],
    selfcheck=[ex("En Orientación: ¿un hecho se puede comprobar en una fuente confiable?", "Sí", "Por eso se distingue de un mito, que se repite sin respaldo."), ex("¿Las amenazas son una forma de violencia?", "Sí", "Dañan emocionalmente a la persona."), ex("¿Es válido consultar dudas de salud a profesionales?", "Sí", "Es una forma de cuidarse.")],
    task=T("Lee estas cuatro frases inventadas: (a) «En Chile no se puede vender alcohol a menores de 18 años»; (b) «Si lo prueba todo el curso, no es riesgoso»; (c) «Una amenaza por mensaje es violencia»; (d) «Preguntar en un centro de salud es una falta». Clasifica cada frase como hecho, mito o derecho y escribe una razón breve.", "(a) Hecho: es una regla legal. (b) Mito: la cantidad de personas no mide el riesgo. (c) Hecho: la amenaza daña a la persona. (d) Mito: preguntar a profesionales es una forma de cuidado.", ["clasifica las cuatro frases", "da una razón para cada una", "distingue mito de hecho", "no cuenta experiencias personales"], ["tabla escrita", "texto oral"], ["llamar hecho a un mito", "no dar razón"], "Reconoce las clasificaciones bien razonadas y pregunta cómo comprobaría la frase más dudosa."),
    reinforce="Escribe un mito que hayas escuchado en general sobre la presión de grupo y cómo lo comprobarías.",
    extend="Explica por qué poner un límite es un acto de cuidado y no de maleducación.",
)

lesson(
    OA3, 3,
    "Una hoja y un lápiz. El caso de Joaquín, un estudiante inventado, y sus tres opciones están escritos en los ejercicios.",
    "Aprenderé a comparar opciones frente a una situación de riesgo con una tabla de seguridad, cuidado de otras personas y ayuda disponible. Sirve para elegir con anticipación qué hacer.",
    ["Sé distinguir mitos, hechos y límites.", "Sé qué son corto y largo plazo."],
    [
        "Ante una situación de riesgo hay varias opciones, y cada una tiene consecuencias. Para compararlas conviene usar tres preguntas: ¿protege mi seguridad?, ¿protege a las demás personas? y ¿conecta con ayuda? Cada respuesta afirmativa vale 1 punto, de modo que una opción puede sumar entre 0 y 3.",
        "Las consecuencias pueden ser inmediatas, como un susto o una discusión, o de largo plazo, como un daño a la salud o la pérdida de confianza. Una opción que parece fácil hoy puede tener una consecuencia grave mañana. Por eso no basta preguntar cuál incomoda menos: hay que preguntar cuál cuida más.",
        "Elegir con puntos ayuda, pero no reemplaza el criterio. Si una opción pone en peligro inmediato a alguien, se descarta aunque sume puntos en otras preguntas. Y si dos opciones empatan, gana la que incluye avisar a una persona adulta de confianza, porque suma ayuda competente.",
    ],
    [("opción", "alternativa posible frente a una situación"), ("consecuencia inmediata", "lo que ocurre enseguida después de una decisión"), ("consecuencia de largo plazo", "lo que ocurre mucho tiempo después"), ("anticipar", "pensar antes de actuar lo que puede pasar"), ("empate", "igualdad de puntos entre dos opciones")],
    [
        W("Puntuar una opción", "Joaquín, personaje inventado, evalúa irse de una reunión de riesgo y llamar a su casa. Protege su seguridad: sí. Protege a otros: no. Conecta con ayuda: sí. ¿Cuántos puntos suma?", ["Cada sí vale 1 punto.", "Hay dos síes."], "2 puntos"),
        W("Elegir con empate", "Dos opciones empatan con 2 puntos. La opción X incluye avisar a una persona adulta de confianza y la Y no. ¿Cuál conviene?", ["El empate se resuelve con el criterio de ayuda.", "X suma ayuda competente."], "La opción X"),
    ],
    [
        M("Elegir la opción que incomoda menos hoy.", "Se mira solo la consecuencia inmediata.", "Compara también la consecuencia de largo plazo."),
        M("Sumar puntos aunque la opción ponga en peligro a alguien.", "Se olvida que el peligro inmediato descarta una opción.", "Descarta primero lo que expone a alguien a un daño."),
    ],
    R=[
        ex("Una opción sí protege tu seguridad, sí protege a otros y sí conecta con ayuda. ¿Cuántos puntos suma?", "3", "Hay tres respuestas afirmativas."),
        ex("¿Qué es una consecuencia de largo plazo? A) Lo que ocurre mucho tiempo después B) Lo que ocurre en el mismo minuto", "A", "Se aprecia con el paso del tiempo."),
        ex("Si dos opciones empatan, ¿gana la que incluye avisar a una persona adulta de confianza? Responde sí o no.", "Sí", "Suma ayuda competente."),
    ],
    U=[
        ex("¿Qué pregunta mira el cuidado de los demás? A) ¿Protege a las demás personas? B) ¿Es la más rápida?", "A", "Evalúa si nadie más queda expuesto."),
        ex("Una opción sumó 3 puntos pero deja a un compañero en peligro inmediato. ¿Qué corresponde? A) Descartarla B) Elegirla por los puntos", "A", "El peligro inmediato descarta una opción."),
        ex("¿Por qué no basta preguntar cuál opción incomoda menos? A) Porque la que cuida más puede incomodar B) Porque la incomodidad no existe", "A", "Cuidar puede requerir un momento difícil."),
    ],
    A=[
        ex("Joaquín evalúa: (1) quedarse y no decir nada: seguridad no, otros no, ayuda no. (2) Irse y avisar a su casa: seguridad sí, otros no, ayuda sí. (3) Llamar a un adulto para que ayude a todos: seguridad sí, otros sí, ayuda sí. ¿Cuál suma más puntos?", "La opción 3", "Suma 3, mientras la 2 suma 2 y la 1 suma 0."),
        ex("Una compañera se siente mal en una fiesta de ejemplo. Joaquín puede A) llamar de inmediato a una persona adulta o B) esperar una hora a ver si mejora. ¿Cuál conviene?", "A", "Ante malestar, la ayuda adulta no se posterga."),
        ex("Clasifica con I (inmediata) o L (largo plazo): 1) Una discusión con un amigo. 2) Daño a la salud por consumo repetido. 3) Un castigo ese mismo día. Escribe las letras en orden.", "I, L, I", "La 2 aparece con el paso del tiempo; la 1 y la 3 ocurren enseguida."),
    ],
    Z=[
        ex("¿Por qué anticipar las consecuencias antes de una salida ayuda más que improvisar?", "Porque permite preparar un plan seguro y pedir ayuda antes de que el riesgo sea mayor", "Anticipar da tiempo para cuidar."),
        ex("Un compañero dice: «Mejor no avisar a nadie, así no hay problemas». ¿Qué respondes? A) Callar puede dejar a alguien sin ayuda B) Callar siempre es lo más seguro", "A", "El silencio puede dejar a una persona en peligro."),
    ],
    D=[
        arith("Joaquín compara 3 opciones con 3 preguntas cada una. ¿Cuántas respuestas debe dar en total?", "3*3", "Se multiplica el número de opciones por las preguntas."),
        arith("Joaquín puntúa cuatro opciones y obtienen 3, 1, 2 y 3 puntos. ¿Cuántos puntos suman entre todas?", "3+1+2+3", "Se suman los puntos de cada opción."),
    ],
    context=[ex("En una charla del liceo, una estudiante dice: «Antes de salir con mis amigos pienso a quién llamaría si algo sale mal». ¿Qué está haciendo? A) Anticipando una consecuencia B) Evitando salir siempre", "A", "Prepara un plan de ayuda antes de que se necesite.")],
    selfcheck=[ex("En Orientación: ¿anticipar es pensar antes de actuar lo que puede pasar?", "Sí", "Ayuda a elegir con más cuidado."), ex("¿Una opción que pone en peligro inmediato a alguien se descarta?", "Sí", "La seguridad va primero."), ex("¿Avisar a una persona adulta de confianza suma ayuda?", "Sí", "Conecta con ayuda competente.")],
    task=T("Lee el caso inventado: Valentina está en una reunión donde un grupo empieza a presionar a un compañero para que consuma una sustancia. Tiene tres opciones: (1) quedarse mirando; (2) decirle al compañero «vámonos» y salir juntos para llamar a un adulto; (3) grabar el momento para mostrarlo en redes. Compara las tres con las preguntas de seguridad, otros y ayuda, suma los puntos y justifica cuál elige.", "Opción 1: 0 puntos. Opción 2: seguridad sí, otros sí, ayuda sí = 3. Opción 3: seguridad no, otros no (expone al compañero), ayuda no = 0. Elige la 2 porque protege y conecta con una persona adulta de confianza.", ["responde las tres preguntas por opción", "suma bien los puntos", "justifica la elección", "incluye avisar a una persona adulta"], ["tabla escrita", "explicación oral"], ["sumar mal", "elegir exponer al compañero"], "Reconoce la tabla clara y pregunta qué dato cambiaría su elección."),
    reinforce="Compara dos formas de volver a casa de una salida inventada usando las tres preguntas.",
    extend="Explica cómo cambiaría tu tabla si el compañero estuviera en peligro inmediato.",
)

lesson(
    OA3, 4,
    "Una hoja y un lápiz. Los casos de Amanda y de Matilde, estudiantes inventadas, están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura ante una situación de violencia, de consumo o de riesgo sexual, siguiendo el orden: seguridad, alejarse y avisar a una persona adulta. Sirve para actuar sin exponerme.",
    ["Sé comparar opciones con tres preguntas.", "Sé que existen redes de apoyo."],
    [
        "Una acción segura es la que protege a las personas y conecta con ayuda, sin poner a nadie en más riesgo. Se puede recordar con tres pasos: primero la seguridad, luego alejarse del lugar o de la situación si es posible y por último avisar a una persona adulta de confianza. Si hay peligro inmediato, se pide ayuda de inmediato.",
        "Frente a la violencia, no hace falta intervenir en medio de una pelea, porque eso puede aumentar el riesgo. Alejarse y avisar a una persona adulta, como un profesor o la persona inspectora, protege a todos. Frente a una persona que se siente mal por consumo, se avisa a un adulto sin demora. Frente a una presión sexual, se dice que no, se sale del lugar y se cuenta.",
        "No se resuelve un riesgo con secretos, castigos propios ni exposición pública. Por ejemplo, no se difunde un video de una pelea ni se promete callar algo que daña a alguien. Y no se enfrenta a la persona que agrede por cuenta propia: se informa a quien corresponde para que los adultos actúen.",
    ],
    [("acción segura", "acción que protege a las personas y conecta con ayuda"), ("peligro inmediato", "riesgo que puede dañar a alguien ahora mismo"), ("intervenir", "meterse en una situación para cambiarla"), ("exposición pública", "mostrar algo privado o doloroso a muchas personas"), ("persona inspectora", "adulto del establecimiento que cuida la convivencia")],
    [
        W("Ordenar los pasos", "Amanda, personaje inventado, ve a dos estudiantes empezar a golpearse en el patio. ¿Qué hace primero?", ["Primero va su seguridad y la de los demás.", "No se mete entre ellos.", "Se aleja y busca a una persona adulta."], "Alejarse y avisar a una persona adulta"),
        W("Detectar la exposición", "Alguien propone grabar la pelea y subirla a redes «para que los castiguen». ¿Es una acción segura?", ["Difundir el video expone a quienes aparecen.", "No conecta con ayuda adulta."], "No, expone a las personas y no protege"),
    ],
    [
        M("Meterse en medio de una pelea para separarla.", "Se piensa que ayudar es intervenir con el propio cuerpo.", "Aléjate y busca de inmediato a una persona adulta."),
        M("Prometer guardar un secreto que daña a alguien.", "Se confunde lealtad con proteger.", "Cuenta a una persona adulta de confianza: cuidar a alguien no es traicionarlo."),
    ],
    R=[
        ex("Ante una pelea, ¿qué haces primero según los tres pasos? A) Alejarte y avisar a una persona adulta B) Meterte entre las personas", "A", "Evitas sumar riesgo y buscas ayuda competente."),
        ex("¿Subir un video de una pelea a redes es una acción segura? Responde sí o no.", "No", "Expone a las personas y no las protege."),
        ex("Si hay peligro inmediato para alguien, ¿se pide ayuda de inmediato? Responde sí o no.", "Sí", "Esperar puede aumentar el daño."),
    ],
    U=[
        ex("Matilde, personaje inventado, ve que una compañera se siente mal por haber consumido una sustancia. ¿Cuál es la acción segura? A) Avisar sin demora a una persona adulta B) Prometerle que no dirá nada", "A", "La persona puede necesitar atención de salud."),
        ex("¿Por qué no es buena idea enfrentar solo a quien agrede? A) Puede aumentar el riesgo para ti B) Porque los agresores siempre cambian", "A", "Intervenir sin adultos puede ponerte en peligro."),
        ex("¿Qué orden siguen los pasos? A) Seguridad, alejarse y avisar B) Avisar, grabar y callar", "A", "Primero se protege, luego se aleja y se pide ayuda."),
    ],
    A=[
        ex("Una amiga de ejemplo dice: «Mi pareja me presiona para algo que no quiero». ¿Qué acción corresponde? A) Apoyarla, sugerirle contarlo a una persona adulta de confianza y acompañarla B) Decirle que lo resuelva sola", "A", "El apoyo adulto protege su integridad y no la deja sola."),
        ex("Ordena con números los pasos para un caso de violencia en el patio: (a) avisar a una persona adulta, (b) alejarte del lugar. ¿Cuál va primero?", "b", "Primero te alejas y luego avisas; en ese orden proteges tu seguridad."),
        ex("Clasifica con S (segura) o N (no segura): 1) Avisar a un profesor. 2) Difundir un video. 3) Acompañar a un compañero que está mal hasta que llegue un adulto. Escribe las letras en orden.", "S, N, S", "La 1 y la 3 conectan con ayuda; la 2 expone a las personas."),
    ],
    Z=[
        ex("¿Por qué guardar un secreto que daña a alguien no es lealtad?", "Porque la lealtad verdadera cuida a la persona y el secreto la deja sin ayuda", "Cuidar a alguien incluye pedir apoyo adulto."),
        ex("Un compañero dice: «Si aviso, me van a tratar de soplón». ¿Qué respuesta ayuda más? A) «Avisar protege a alguien y no es acusar.» B) «Tienes razón, mejor callar.»", "A", "Reencuadra avisar como cuidado."),
    ],
    D=[
        arith("En un simulacro de ejemplo, 28 estudiantes practicaron los tres pasos y 4 olvidaron avisar a una persona adulta. ¿Cuántos sí avisaron?", "28-4", "Al total se le restan quienes lo olvidaron."),
        ex("Si una compañera te cuenta algo grave y te pide guardar secreto, ¿qué haces? A) Le explicas que lo cuentas a una persona adulta porque te importa B) Se lo cuentas a todo el curso", "A", "Cuidas su seguridad y respetas su privacidad ante los demás."),
    ],
    context=[ex("Durante un recreo ves a un grupo molestando físicamente a un estudiante más pequeño. ¿Cuál es la acción segura? A) Alejarte y avisar de inmediato a una persona adulta B) Grabarlos para mostrarlo en el curso", "A", "Protege al estudiante y conecta con ayuda adulta.")],
    selfcheck=[ex("En Orientación: ¿una acción segura conecta con ayuda adulta?", "Sí", "Es parte de la definición."), ex("¿Se debe grabar y difundir una pelea?", "No", "Expone a las personas."), ex("¿Alejarse puede ser una forma de cuidado?", "Sí", "Evita sumar riesgo.")],
    task=T("Lee el caso inventado: Antonia ve que un compañero de otro curso aprieta del brazo a una estudiante en la salida del liceo mientras le grita que no le hable a nadie. La estudiante parece asustada. Antonia no conoce a ninguno de los dos. Escribe: (1) qué hecho observa, (2) la acción segura que elegiría en orden, (3) por qué no conviene grabar ni enfrentarlo sola y (4) a qué persona adulta avisaría.", "Hecho: un estudiante aprieta del brazo y grita. Acción: alejarse del lugar y avisar a la persona inspectora o a un profesor. No grabar: expondría a la estudiante; no enfrentarlo sola: podría aumentar el riesgo. Persona adulta: inspectora, profesor u orientadora.", ["describe el hecho sin suposiciones", "ordena la acción segura", "explica por qué no grabar ni enfrentar", "nombra una persona adulta"], ["texto escrito", "explicación oral"], ["proponer enfrentar al agresor", "proponer difundir el video"], "Reconoce el orden de los pasos y pregunta qué haría si no encuentra a ese adulto."),
    reinforce="Escribe los tres pasos de una acción segura con tus palabras y un ejemplo inventado.",
    extend="Explica con un ejemplo inventado la diferencia entre guardar un secreto y proteger a alguien.",
)

lesson(
    OA3, 5,
    "Una hoja y un lápiz. Las frases de ejemplo para pedir ayuda están escritas en los ejercicios. No necesitas contar nada tuyo.",
    "Aprenderé a pedir ayuda con un mensaje claro de tres partes: lo que ocurre, cómo me siento y lo que necesito. Sirve para contarle a una persona adulta de confianza sin quedarme sin palabras.",
    ["Sé elegir una acción segura.", "Sé qué personas forman una red de apoyo."],
    [
        "Pedir ayuda es una habilidad que se puede ensayar. Un mensaje claro tiene tres partes: lo que ocurre, que es el hecho; cómo me siento, que es la emoción; y lo que necesito, que es la petición. Por ejemplo: «Un compañero me amenaza por mensaje, tengo miedo y quiero que me ayudes a avisar al colegio».",
        "Conviene elegir bien a quién se lo cuentas y cuándo. Puede ser una persona de tu casa, un profesor, la persona orientadora o alguien del centro de salud. Si la primera persona no te escucha o no actúa, se busca otra: no se deja el tema. Para decirlo, ayuda partir con «necesito hablar contigo de algo importante» y pedir un lugar tranquilo.",
        "Hay también ayuda por teléfono y por internet. El Fono Niños 147 atiende a niños, niñas y adolescentes, y debe usarse junto con el aviso a una persona adulta, no en lugar de él. Quien pide ayuda no queda en falta: busca protección. Y quien recibe el aviso debe escuchar sin juzgar.",
    ],
    [("petición", "lo que se necesita de la otra persona"), ("emoción", "lo que se siente frente a una situación"), ("ensayar", "practicar antes cómo decir algo"), ("escuchar sin juzgar", "atender sin culpar ni burlarse"), ("Fono Niños 147", "línea de ayuda para niños, niñas y adolescentes")],
    [
        W("Armar el mensaje", "Cintia, personaje inventado, recibe mensajes de burla de un grupo. Escribe: «Me escriben burlas en el chat, me siento mal y necesito que me ayudes a avisar». ¿Qué parte es la petición?", ["La petición dice lo que necesita.", "Es la última parte de la frase."], "«Necesito que me ayudes a avisar»"),
        W("Buscar otra persona", "Cintia le cuenta a un adulto y este le dice «no exageres». ¿Qué conviene hacer?", ["Que alguien no escuche no quita el problema.", "Se busca otra persona adulta de confianza."], "Contarlo a otra persona adulta de confianza"),
    ],
    [
        M("Dejar de buscar ayuda si la primera persona no responde.", "Se piensa que el problema no tiene solución.", "Busca otra persona adulta de confianza hasta que alguien actúe."),
        M("Llamar al 147 y no contar a nadie más.", "Se cree que una línea reemplaza a la red cercana.", "Úsalo junto con el aviso a una persona adulta de confianza."),
    ],
    R=[
        ex("Un mensaje de ayuda tiene tres partes. ¿Cuál no es una de ellas? A) El hecho B) Una amenaza", "B", "Las partes son hecho, emoción y petición."),
        ex("En «necesito que me acompañes a hablar con la orientadora», ¿qué parte aparece? A) La petición B) El hecho", "A", "Dice lo que se necesita de la otra persona."),
        ex("¿El Fono Niños 147 sirve para reemplazar el aviso a una persona adulta de confianza? Responde sí o no.", "No", "Se usa junto con ese aviso, no en su lugar."),
    ],
    U=[
        ex("Si una persona no te escucha, ¿qué haces? A) Buscas a otra persona adulta de confianza B) Dejas de pedir ayuda", "A", "Pedir ayuda no termina con un solo intento."),
        ex("¿Por qué ayuda ensayar el mensaje antes? A) Porque con palabras listas es más fácil decirlo B) Porque así se evita contar el hecho", "A", "Reduce los nervios y ordena las ideas."),
        ex("Escuchar sin juzgar significa A) atender sin culpar ni burlarse B) dar la razón en todo", "A", "La persona se siente segura para seguir contando."),
    ],
    A=[
        ex("Ordena con letras las partes de este mensaje inventado: (a) «Quiero que me acompañes a hablar con la inspectora.» (b) «Me siento asustado.» (c) «Un compañero me sigue después de clases.» ¿Cuál es el orden hecho, emoción, petición?", "c, b, a", "La c es el hecho, la b la emoción y la a la petición."),
        ex("Clasifica con H (hecho), E (emoción) o P (petición): 1) «Tengo miedo.» 2) «Necesito que me ayudes a avisar.» 3) «Me dejaron fuera del chat.» Escribe las letras en orden.", "E, P, H", "La 1 es lo que siente, la 2 lo que necesita y la 3 lo que ocurrió."),
        ex("¿Cuál frase abre bien una conversación para pedir ayuda? A) «Necesito hablar contigo de algo importante.» B) «Si te cuento, prométeme que no harás nada.»", "A", "Pide atención sin condicionar la ayuda."),
    ],
    Z=[
        ex("¿Por qué conviene decir qué necesitas y no solo qué pasó?", "Porque la petición guía a la persona adulta sobre cómo ayudar", "Con una petición clara la ayuda es más concreta."),
        ex("Un compañero dice: «Si pido ayuda, me van a ver como débil». ¿Qué respondes? A) Pedir ayuda es una forma de cuidarse B) Tienes razón, es una debilidad", "A", "Buscar protección es una decisión responsable."),
    ],
    D=[
        arith("Un grupo de ejemplo ensayó el mensaje en parejas: 12 parejas, 3 intentos cada una. ¿Cuántos ensayos hubo en total?", "12*3", "Se multiplican las parejas por los intentos."),
        ex("Elige cuál de estos mensajes está completo (hecho, emoción y petición). A) «Me excluyen del grupo, me siento triste y quiero que me ayudes a hablar con la orientadora.» B) «Me excluyen del grupo.»", "A", "Solo el A incluye las tres partes."),
    ],
    context=[ex("Una estudiante de ejemplo recibe mensajes amenazantes. Quiere avisar a su profesor jefe. ¿Cuál mensaje es más claro? A) «Un compañero me amenaza por chat, tengo miedo y quiero que me ayude a avisar al colegio.» B) «Ayuda, todo mal.»", "A", "Incluye hecho, emoción y petición.")],
    selfcheck=[ex("En Orientación: ¿un mensaje de ayuda incluye hecho, emoción y petición?", "Sí", "Así queda claro y completo."), ex("¿Se debe seguir buscando ayuda si una persona no actúa?", "Sí", "Hay otras personas de la red."), ex("¿El Fono Niños 147 se usa junto con avisar a una persona adulta?", "Sí", "No la reemplaza.")],
    task=T("Escribe un mensaje de tres partes (hecho, emoción y petición) para este caso inventado: Simón recibe cada día mensajes de burla sobre su apariencia en un chat de curso. Elige a quién se lo diría (persona de su casa, profesor jefe u orientadora) y escribe una frase con la que abriría la conversación. Anota también qué haría si esa persona no puede ayudarlo.", "«Necesito hablar contigo de algo importante. En el chat del curso me escriben burlas cada día. Me siento triste y avergonzado. Quiero que me ayudes a avisar al colegio.» Si no puede, buscaría a la orientadora u otra persona adulta de confianza.", ["incluye hecho, emoción y petición", "elige a una persona adulta", "escribe una frase de apertura", "plantea qué hacer si no hay respuesta"], ["texto escrito", "ensayo oral"], ["omitir la petición", "no prever una segunda persona"], "Reconoce las tres partes y pregunta cómo cambiaría el mensaje para otra persona."),
    reinforce="Escribe un mensaje de tres partes para pedir ayuda por una dificultad inventada en un trabajo grupal.",
    extend="Explica por qué ensayar un mensaje ayuda a quien lo recibe.",
)

lesson(
    OA3, 6,
    "Una hoja y un lápiz. La lista de redes de apoyo y los casos inventados están escritos en los ejercicios.",
    "Aprenderé a elegir la red de apoyo adecuada según el tipo de problema, sin contar nada personal. Sirve para saber a dónde acudir antes de que haga falta.",
    ["Sé pedir ayuda con un mensaje de tres partes.", "Sé qué es una acción segura."],
    [
        "Las redes de apoyo son personas e instituciones que ayudan frente a un riesgo. La familia, o una persona de tu casa, acompaña en lo cotidiano. Los profesores y la persona orientadora ayudan con la convivencia y con el apoyo en el liceo. Las instituciones de salud, como un centro de salud familiar, atienden dudas y problemas de salud, de consumo o de salud sexual. Los centros comunitarios ofrecen talleres y espacios de apoyo cerca del barrio.",
        "También existen fonos y páginas web especializadas. Antes de usarlos, hay que comprobar que sean de instituciones conocidas y que no pidan datos privados innecesarios. Para niños, niñas y adolescentes, el Fono Niños 147 es una opción. Siempre conviene avisar también a una persona adulta de confianza, porque el acompañamiento cercano completa la ayuda.",
        "Cada problema se conecta mejor con una red. Un problema de convivencia entre compañeros va a la orientadora o a la inspectoría. Un malestar de salud o un riesgo de consumo va al centro de salud. Un riesgo grave e inmediato exige avisar al adulto más cercano sin demora. Conocer el mapa antes ayuda a no improvisar.",
    ],
    [("red de apoyo", "personas e instituciones que ayudan frente a un riesgo"), ("centro de salud", "lugar donde profesionales atienden problemas de salud"), ("centro comunitario", "espacio del barrio con talleres y apoyo a la comunidad"), ("línea de ayuda", "teléfono o sitio especializado que orienta"), ("inspectoría", "área del establecimiento que cuida la convivencia")],
    [
        W("Elegir la red", "Un estudiante inventado tiene dudas sobre protección en las relaciones sexuales. ¿Qué red es la más adecuada?", ["Es un tema de salud sexual.", "Los profesionales de la salud tienen información comprobada."], "Un centro de salud con profesionales"),
        W("Verificar una página", "Aparece una página que pide el nombre completo y la dirección para dar «consejos». ¿Conviene usarla?", ["Pide datos privados sin necesidad.", "No se sabe qué institución la respalda."], "No, es una fuente dudosa"),
    ],
    [
        M("Usar la primera página o cadena que aparece en internet.", "Se cree que cualquier sitio es una ayuda.", "Verifica que sea de una institución conocida y que no pida datos privados."),
        M("Esperar a tener un problema para saber a quién recurrir.", "Se deja el mapa de ayuda para después.", "Reconoce tus redes antes, en tiempo de calma."),
    ],
    R=[
        ex("Una duda de salud sexual, ¿a qué red se lleva? A) Un centro de salud B) Un grupo de chat sin adultos", "A", "Los profesionales de salud tienen información confiable."),
        ex("Un conflicto entre compañeros del curso, ¿a qué persona del liceo se puede avisar? A) A la orientadora o a la inspectoría B) A nadie", "A", "Ellas cuidan la convivencia."),
        ex("¿Un centro comunitario puede ofrecer talleres y apoyo cerca del barrio? Responde sí o no.", "Sí", "Esa es una de sus funciones."),
    ],
    U=[
        ex("¿Qué se debe comprobar antes de usar una página de ayuda? A) Que sea de una institución conocida y no pida datos privados B) Que tenga muchos colores", "A", "La verificación evita fuentes engañosas."),
        ex("¿Por qué avisar también a una persona adulta de confianza si se llama a una línea de ayuda? A) Porque el acompañamiento cercano completa la ayuda B) Porque la línea no sirve", "A", "La persona cercana puede acompañar en lo cotidiano."),
        ex("Un riesgo grave e inmediato para alguien exige A) avisar sin demora al adulto más cercano B) esperar a la hora de clases", "A", "La rapidez protege."),
    ],
    A=[
        ex("Une cada problema con su red, escribe las letras en orden: 1) burlas en el curso, 2) tos persistente y malestar físico, 3) taller de ocio en el barrio. Redes: (a) centro de salud, (b) orientadora o inspectoría, (c) centro comunitario.", "b, a, c", "La convivencia va al liceo, el malestar a salud y el taller al centro comunitario."),
        ex("Un sitio dice: «Escríbenos tu clave del celular para ayudarte». ¿Qué corresponde? A) No usarlo y avisar a una persona adulta B) Enviar la clave rápido", "A", "Ninguna ayuda real pide claves privadas."),
        ex("Un grupo de ejemplo tiene 5 redes escritas en su mapa: familia, profesores, salud, centro comunitario y fono. Agrega 1 más: la orientadora. ¿Cuántas redes tiene ahora?", "6", "A las 5 se les suma 1."),
    ],
    Z=[
        ex("¿Por qué es mejor conocer el mapa de redes antes de un problema?", "Porque en una crisis no se improvisa y se puede acudir sin demora", "Prepararse ahorra tiempo y reduce el riesgo."),
        ex("Un compañero dice: «Las redes de apoyo son solo para casos extremos». ¿Qué respondes? A) También sirven para dudas y prevención B) Tienes razón, solo para extremos", "A", "Consultar a tiempo previene problemas."),
    ],
    D=[
        arith("En un afiche de ejemplo se anotan 4 redes del liceo y 3 del barrio. ¿Cuántas redes aparecen en total?", "4+3", "Se suman las redes del liceo y las del barrio."),
        ex("Un adolescente inventado dice que no confía en nadie de su casa. ¿Qué opción es adecuada? A) Buscar a otra persona adulta de confianza, como la orientadora B) No contarle a nadie", "A", "La red incluye otras personas adultas."),
    ],
    context=[ex("En una reunión de curso proponen hacer un panel con redes de apoyo del barrio. ¿Qué debe llevar para ser útil? A) Nombres de instituciones conocidas y para qué sirve cada una B) Solo fotos de personas", "A", "Dice a quién acudir según cada necesidad.")],
    selfcheck=[ex("En Orientación: ¿un centro de salud es una red de apoyo?", "Sí", "Atiende problemas de salud."), ex("¿Una página que pide tu clave es confiable?", "No", "Pide datos privados innecesarios."), ex("¿Conviene conocer las redes antes de necesitarlas?", "Sí", "Así no se improvisa.")],
    task=T("Arma un mapa de redes de apoyo con estos tres problemas inventados: (a) un estudiante recibe amenazas por mensaje; (b) una estudiante tiene dudas sobre salud sexual; (c) un grupo quiere un espacio de actividades saludables en su barrio. Para cada problema escribe la red más adecuada y una razón, sin usar nombres reales.", "(a) Orientadora o inspectoría, porque cuidan la convivencia, y una persona adulta de su casa. (b) Centro de salud, porque hay profesionales con información comprobada. (c) Centro comunitario, porque ofrece espacios y talleres en el barrio.", ["asocia cada problema con una red", "da una razón", "no usa nombres reales", "incluye una persona adulta de confianza"], ["tabla escrita", "mapa dibujado"], ["elegir fuentes dudosas", "usar datos reales de personas"], "Reconoce las asociaciones razonadas y pregunta qué otra red sumaría."),
    reinforce="Anota tres personas o lugares de ayuda de tu comunidad que no incluyan datos privados.",
    extend="Explica por qué una página que pide datos innecesarios no es una red de apoyo.",
)
