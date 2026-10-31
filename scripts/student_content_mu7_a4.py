"""Student material for 7.º básico Música, OA 04 (interpretar a una y más voces repertorio diverso, con medios de registro y transmisión como apoyo).

Todas las piezas, tablas y registros de los ejercicios son inventados para esta clase; el repertorio y las grabaciones reales los elige y autoriza el docente.
Toda grabación o difusión requiere permiso de quienes participan y de una persona adulta; nadie está obligado a que se registre o se comparta su voz.
"""
from __future__ import annotations

from student_content_mu7_a import L
from student_lessons import arith, ex

OA4 = "MU07 OA 04"
NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"

# ---------------------------------------------------------------- OA 04 · clase 1 (una voz y más voces)
L(
    OA4, 1,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las melodías están escritas en los ejercicios; puedes cantarlas con «la» o tocarlas, solo o con alguien más, a volumen cómodo.",
    "Aprenderé a diferenciar cantar a una voz (unísono) de cantar a más voces (tercera paralela, canon y ostinato). Sirve para elegir cómo interpretar una pieza solo o en grupo.",
    ["Sé cantar una melodía escrita con números.", "Sé que una melodía se puede repetir con retraso.", "Sé sumar y restar números pequeños."],
    [
        "Interpretar a una voz es cantar o tocar una sola melodía. Si varias personas cantan las mismas notas al mismo tiempo, hay una sola voz repetida por muchas personas, y se llama unísono. Interpretar a más voces es cantar dos o más líneas distintas a la vez. Cada línea es una voz. Las voces se distinguen por sus notas o por el momento en que entran, no por cuántas personas las cantan.",
        f"Hay varias maneras sencillas de cantar a dos voces. En la tercera paralela, la segunda voz canta la misma melodía dos números más abajo en la escala ({NOTAS}): si la voz 1 canta 5-5-4-3, la voz 2 canta 3-3-2-1. En el canon, la segunda voz canta la misma melodía, pero empieza después de unos compases. En el ostinato, una voz repite sin parar un patrón corto mientras la otra canta la melodía.",
        "Para cantar a más voces conviene ensayar primero cada voz por separado, después juntar dos voces y por último todas. Hay que escuchar a las demás voces y mantener un pulso común. Si una voz entra tarde en un canon, no es un error: así funciona. Un grupo puede dividirse en partes iguales; por ejemplo, 12 personas en un canon a 3 voces forman 3 grupos de 4.",
    ],
    [("voz", "cada línea melódica de una pieza"), ("unísono", "varias personas cantando las mismas notas a la vez"), ("tercera paralela", "segunda voz que va dos números más abajo que la melodía"), ("canon", "la misma melodía que entra en cada voz con retraso"), ("ostinato", "patrón corto que se repite sin parar")],
    [
        ("Escribir la segunda voz", "La voz 1 canta 6-5-4-3. ¿Qué canta la voz 2 en tercera paralela?", ["La tercera paralela baja dos números en cada nota.", "6−2 = 4, 5−2 = 3, 4−2 = 2, 3−2 = 1."], "4-3-2-1"),
        ("Calcular el final de un canon", "Una melodía dura 8 compases y se canta en canon a 2 voces con la segunda voz entrando 2 compases después. ¿En qué compás termina la segunda voz?", ["La voz 2 empieza en el compás 3.", "Dura 8 compases: 3 + 8 − 1 = 10."], "En el compás 10"),
    ],
    [
        ("Pensar que dos personas cantando lo mismo ya son dos voces.", "Si cantan las mismas notas a la vez, es una voz en unísono.", "Cuenta cuántas líneas distintas suenan, no cuántas personas."),
        ("Creer que la voz que entra tarde en un canon se equivocó.", "En el canon cada voz entra con retraso a propósito.", "Mira en la partitura en qué compás debe entrar cada voz."),
    ],
    [
        ex("Dos personas cantan las mismas notas al mismo tiempo. ¿Hay una voz (unísono) o dos voces?", "Una voz (unísono)", "Las líneas son iguales."),
        ex("En un canon, ¿la segunda voz canta otra melodía o la misma melodía con retraso?", "La misma melodía con retraso", "Es la definición del canon."),
        ex("¿Cuántas voces suenan a la vez en un canon a tres voces cuando ya entraron todas?", "3", "Cada voz es una línea."),
    ],
    [
        ex("La voz 1 canta 8-7-7-6. ¿Qué canta la voz 2 en tercera paralela?", "6-5-5-4", "Cada nota baja dos números."),
        ex("Un canon a 2 voces tiene 8 compases y la voz 2 entra 2 compases después. ¿En qué compás entra la voz 2?", "En el compás 3", "Después de 2 compases empieza el tercero."),
        arith("Un grupo de 12 personas se divide por igual en 3 voces para un canon. ¿Cuántas personas hay en cada voz?", "12//3", "Se reparten 12 personas en 3 grupos iguales.", " personas"),
    ],
    [
        ex("Escribe la tercera paralela de la melodía 7-6-5-4.", "5-4-3-2", "Cada nota baja dos números."),
        arith("Una melodía dura 6 compases y se canta como canon: la voz 1 empieza en el compás 1 y la voz 2 entra 2 compases después. ¿Cuántos compases dura la pieza completa hasta que termina la voz 2?", "2+6", "La voz 2 termina 2 compases después de que termina la voz 1.", " compases"),
        ex("Un ostinato 1-5-1-5 acompaña una melodía de 8 notas. ¿Cuántas veces se repite completo el ostinato mientras suena la melodía, si cada nota de la melodía coincide con una nota del ostinato?", "2", "El ostinato tiene 4 notas y 8 notas se reparten en 2 vueltas."),
    ],
    [
        ex("Marta dice que dos personas cantando lo mismo ya son dos voces. ¿Tiene razón? Responde sí o no.", "No", "Si cantan lo mismo a la vez, es una sola voz en unísono."),
        ex("Compás 1 de la voz 1: 1-2-3-1. Compás 2: 3-4-5-3. La voz 2 entra en el compás 2 con la misma melodía desde el principio. ¿Qué canta la voz 2 en el compás 2?", "1-2-3-1", "La voz 2 empieza la melodía: su primer compás es 1-2-3-1."),
    ],
    [
        arith("En un canon a 2 voces de 12 compases, la voz 2 entra 3 compases después. ¿Durante cuántos compases suenan las dos voces a la vez?", "12-3", "Las dos suenan desde que entra la segunda hasta que termina la primera.", " compases"),
        ex("En un canon a 3 voces, la voz 2 entra tras 2 compases y la voz 3 entra 2 compases después de la voz 2. ¿En qué compás entra la voz 3?", "En el compás 5", "La voz 2 entra en el compás 3 y la voz 3 en el 5."),
    ],
    [arith("Un coro de 18 estudiantes canta un canon a 3 voces. Entra una voz nueva cada 2 compases y la melodía dura 6 compases. ¿En qué compás termina la voz 3?", "5+6-1", "La voz 3 entra en el compás 5 y dura 6 compases.", "")],
    [ex("¿Cómo se llama cantar las mismas notas a la vez?", "Unísono", "Es una sola voz repetida por varias personas."), ex("¿Cuántos números baja la segunda voz en una tercera paralela?", "2", "La voz 2 va dos números más abajo."), ex("¿Qué se ensaya primero cuando se canta a más voces?", "Cada voz por separado", "Es la estrategia de la clase.")],
    (
        "Con la melodía 5-5-6-5-3 escribe: 1) su tercera paralela (dos números más abajo); 2) la melodía como canon a dos voces, indicando en qué pulso entra la segunda voz si entra 2 pulsos después y cada nota dura un pulso. Canta cada voz por separado con «la» y, si puedes, con otra persona de tu casa canten juntas a dos voces.",
        "Tercera paralela: 3-3-4-3-1. Canon: la voz 1 canta en los pulsos 1 a 5 y la voz 2 entra en el pulso 3 y termina en el pulso 7.",
        ["escribe bien la tercera paralela", "indica cuándo entra la segunda voz", "ensaya cada voz por separado"],
        ["voz 2 escrita", "plan del canon"],
        ["contar mal los pulsos de entrada", "bajar otro número de dos"],
        "Reconoce la voz 2 y pide cantar solo la voz 2 con la mano marcando el pulso.",
    ),
    "Canta con «la» la melodía 5-5-4-3 y su tercera paralela 3-3-2-1, una después de la otra.",
    "Escribe un canon de 4 notas para tres voces e indica en qué pulso entra cada una.",
)

# ---------------------------------------------------------------- OA 04 · clase 2 (medios de registro)
L(
    OA4, 2,
    "Lápiz y papel. Los cifrados, partituras y registros están escritos en los ejercicios. Cifrado de la clase: C = acorde I (do mayor); F = acorde IV (fa mayor); G = acorde V (sol mayor).",
    "Aprenderé qué medios sirven para registrar música (partitura, cifrado, notación gráfica, grabación de audio y video) y cuándo conviene cada uno. Sirve para guardar una pieza, ensayarla y compartirla con otros grupos.",
    ["Sé que la música se puede escribir con números.", "Sé qué son los acordes I, IV y V.", "Sé que una grabación guarda el sonido."],
    [
        "Un medio de registro es una forma de guardar la música para poder volver a ella. La partitura convencional escribe con figuras y pentagrama las alturas y duraciones exactas; permite que alguien que no escuchó la pieza la lea y la toque. El cifrado escribe solo los acordes con letras: C, F y G corresponden a los acordes I, IV y V de do mayor. Sirve para acompañar con guitarra o teclado.",
        "La notación gráfica usa dibujos, líneas y puntos; es muy útil cuando la música no usa notas fijas, como una ambientación libre. La grabación de audio guarda el sonido real, con volumen, matices y errores. El video agrega lo que se ve, como la postura o quién entra y cuándo. Cada medio guarda cosas distintas: el audio no dice los nombres de las notas y la partitura no guarda cómo sonó cada ensayo.",
        "Por eso se combinan. Con la partitura se ensaya, con el audio se compara cómo sonó y con el cifrado se acompaña rápido. Para elegir se piensa qué necesita el grupo: reproducir notas exactas, acompañar con acordes, registrar una idea libre o revisar un ensayo. Toda grabación debe hacerse con permiso de quienes participan y de una persona adulta, y nadie está obligado a que su voz sea grabada.",
    ],
    [("medio de registro", "forma de guardar la música para volver a ella"), ("partitura convencional", "escritura musical con figuras y pentagrama"), ("cifrado", "escritura de acordes con letras: C, F, G"), ("notación gráfica", "registro con dibujos, líneas y puntos"), ("grabación de audio", "registro del sonido real de una interpretación")],
    [
        ("Traducir un cifrado", "El cifrado dice C – F – G – C. ¿Qué acordes numéricos son?", ["C = I.", "F = IV.", "G = V."], "I – IV – V – I"),
        ("Elegir el medio", "Un grupo quiere revisar si su volumen estuvo parejo en el ensayo de ayer. ¿Qué medio le sirve: partitura o grabación de audio?", ["Necesita oír cómo sonó el volumen real.", "La grabación guarda el sonido real."], "La grabación de audio"),
    ],
    [
        ("Creer que la grabación reemplaza a la partitura.", "El audio guarda el sonido, pero no muestra cuáles son las notas ni sus duraciones escritas.", "Usa la partitura para estudiar y el audio para comparar."),
        ("Grabar a un compañero sin avisar.", "La voz de cada persona es suya y requiere su permiso.", "Pide permiso y, si alguien no quiere, ofrécele otro rol."),
    ],
    [
        ex("¿Qué medio guarda el sonido real de una interpretación: la partitura o la grabación de audio?", "La grabación de audio", "El audio conserva el sonido tal como sonó."),
        ex("¿Qué medio indica con exactitud las alturas y las duraciones de las notas?", "La partitura convencional", "Escribe figuras y pentagrama."),
        ex("¿Cómo se llama la escritura de acordes con letras como C, F y G?", "Cifrado", "Es su nombre."),
    ],
    [
        ex("¿Qué acorde numérico corresponde a la letra F en el cifrado de la clase?", "IV", "F = IV en do mayor."),
        ex("Un grupo anota una ambientación libre con líneas y puntos. ¿Qué medio usa?", "Notación gráfica", "Usa dibujos en vez de notas."),
        ex("¿Qué medio agrega lo que se ve, como la postura y las entradas: el audio o el video?", "El video", "Muestra imagen además de sonido."),
    ],
    [
        ex("Una canción tiene 8 compases con un acorde por compás: C F G C C F G C. ¿Cuántas veces aparece el acorde C?", "4", "C aparece en los compases 1, 4, 5 y 8."),
        ex("Escribe en cifrado la progresión I – V – I.", "C – G – C", "I = C y V = G."),
        arith("Un audio de ensayo dura 2 minutos 45 segundos. ¿Cuántos segundos son?", "2*60+45", "Se pasan los minutos a segundos y se suman 45.", " segundos"),
    ],
    [
        ex("Bea dice que, si tiene la grabación, no necesita la partitura para saber qué notas son. ¿Tiene razón? Responde sí o no.", "No", "El audio no muestra los nombres de las notas ni sus duraciones escritas."),
        ex("Un grupo quiere que una persona que no escuchó la pieza pueda tocarla. ¿Qué medio le entrega: partitura o grabación de audio?", "Partitura", "La partitura se lee y se toca sin haber oído la pieza."),
    ],
    [
        ex("Una progresión es C – F – C – G – C. ¿Cuántos acordes distintos tiene?", "3", "Los distintos son C, F y G."),
        ex("¿Cuál medio no necesita que sepas leer notas ni acordes para usarlo: A) la partitura convencional o B) la grabación de audio?", "B", "Escuchar el audio no exige leer símbolos."),
    ],
    [ex("Dos estudiantes preparan una canción: uno graba un audio con el permiso de todos y otra escribe el cifrado. ¿Qué medio guardó cómo sonó la interpretación: el audio o el cifrado?", "El audio", "El cifrado solo guarda los acordes.")],
    [ex("¿Qué letra del cifrado corresponde al acorde I?", "C", "C = I en do mayor."), ex("¿Qué se necesita antes de grabar la voz de alguien?", "Su permiso", "La voz es de cada persona."), ex("¿Qué medio sirve para anotar una idea libre sin notas?", "La notación gráfica", "Usa dibujos y líneas.")],
    (
        "Registra esta melodía inventada de tres maneras: 5-5-6-5-8-7 con acordes C (compases 1-2) y G (compás 3). 1) Escríbela con números. 2) Escribe el cifrado de los 3 compases (un acorde por compás, usa los acordes dados). 3) Dibújala con la convención «línea que sube = sube; línea que baja = baja; punto = nota corta». Explica qué guarda cada registro y cuál usarías para ensayar.",
        "Números: 5-5-6-5-8-7. Cifrado: C – C – G. Dibujo: dos puntos iguales, un punto un poco más alto, uno más bajo, una línea que sube mucho y una que baja un poco. La partitura o los números sirven para ensayar las notas; el cifrado, para acompañar; el dibujo, para recordar la forma.",
        ["escribe los tres registros", "explica qué guarda cada uno", "elige un medio y lo justifica"],
        ["tres registros escritos", "explicación"],
        ["pensar que un registro reemplaza a los demás", "olvidar el permiso al grabar"],
        "Reconoce los tres registros y pide explicar qué información falta en cada uno.",
    ),
    "Escribe el cifrado C – F – G – C y tradúcelo a números romanos.",
    "Elige una pieza que conozcas y explica qué medios usarías para guardarla y compartirla con permiso.",
)

# ---------------------------------------------------------------- OA 04 · clase 3 (medios de transmisión y respeto)
L(
    OA4, 3,
    "Lápiz y papel. Todas las situaciones están escritas en los ejercicios. Cualquier grabación o envío de música se hace con permiso de quienes participan y de una persona adulta, sin datos personales.",
    "Aprenderé las formas en que se transmite la música (oral, escrita, grabada y digital) y cómo compartirla con respeto por sus autores y por las personas que participan. Sirve para aprender repertorio y compartirlo de manera segura.",
    ["Sé que la música se puede registrar con partitura, cifrado o audio.", "Sé que cada persona decide si se graba su voz.", "Sé contar elementos de una lista."],
    [
        "Un medio de transmisión es la forma en que la música llega de una persona a otra. En la transmisión oral se aprende escuchando y repitiendo en persona. En la transmisión escrita se lee una partitura o un cifrado. En la transmisión grabada se escucha un audio o un video. En la transmisión digital el archivo viaja por internet o por mensajes. Una misma canción puede viajar por varias vías: se aprende de oído, luego se anota y después se graba.",
        "Compartir música tiene reglas de respeto. La música tiene autoras y autores, y eso implica derechos: no se sube ni se copia una obra sin permiso de quien corresponde. La voz y la imagen de cada persona también son suyas: antes de grabar o compartir hay que pedir permiso a quienes aparecen y a una persona adulta, y respetar a quien dice que no, ofreciéndole otro rol. En los nombres de archivo y mensajes no se escriben datos personales.",
        "Cuando una canción llega por un medio distinto, cambia lo que se pierde y lo que se gana. De oído se pierden algunos detalles, pero se gana la manera viva de cantar. Con una partitura se gana exactitud. Con un audio se gana el sonido real. Elegir bien el medio y compartir con permiso permite que el repertorio de un grupo llegue a otras personas sin dañar a nadie.",
    ],
    [("transmisión oral", "aprender música escuchando y repitiendo en persona"), ("transmisión escrita", "aprender música leyendo partitura o cifrado"), ("transmisión grabada", "escuchar un audio o un video guardado"), ("transmisión digital", "enviar música por internet o por mensajes"), ("derechos de autor", "derechos de quien creó una obra para decidir cómo se copia y se comparte")],
    [
        ("Identificar la vía", "Una niña aprende una canción de su abuelo escuchándolo cantar varias tardes. ¿Qué transmisión es?", ["Se aprende en persona.", "Se escucha y se repite."], "Transmisión oral"),
        ("Contar permisos", "Se quiere grabar un coro de 12 personas. 9 dieron permiso y 3 no. ¿Cuántas voces no deben quedar en la grabación?", ["Solo se graba a quienes dieron permiso.", "12 − 9 = 3."], "3 voces"),
    ],
    [
        ("Pensar que, como está en internet, se puede copiar a otra página sin pedir permiso.", "Las obras tienen autoras y autores y se necesita su permiso o una licencia que lo permita.", "Pide permiso o usa solo obras que declaren que se pueden compartir."),
        ("Grabar al grupo y compartirlo sin preguntar a todos.", "Cada persona decide si se graba y comparte su voz o su imagen.", "Pregunta a todas y todos, y a una persona adulta."),
    ],
    [
        ex("Aprender una canción escuchando a otra persona y repitiéndola, ¿es transmisión oral o escrita?", "Oral", "Se aprende en persona, sin leer."),
        ex("Una partitura impresa, ¿es transmisión escrita o digital?", "Escrita", "Se aprende leyendo."),
        ex("Antes de grabar a un compañero, ¿qué haces: pedirle permiso o grabarlo sin avisar?", "Pedirle permiso", "Su voz es suya."),
    ],
    [
        ex("Un audio enviado por mensaje a otro curso, ¿es transmisión digital o oral?", "Digital", "Viaja por internet o por mensajes."),
        ex("Una compañera no quiere que graben su voz. ¿Qué haces: respetarlo y proponerle otro rol o grabar igual?", "Respetarlo y proponerle otro rol", "Nadie está obligado a que se registre su voz."),
        ex("En el nombre de un archivo de audio para compartir, ¿qué conviene poner: el título de la pieza o tu nombre completo y tu dirección?", "El título de la pieza", "No se publican datos personales."),
    ],
    [
        ex("Una canción se aprendió de oído, luego se anotó en partitura y después se grabó en un audio. ¿Cuántos medios de transmisión distintos usó?", "3", "Oral, escrita y grabada."),
        arith("Un audio de ejemplo ocupa 3 MB por minuto y dura 4 minutos. ¿Cuántos MB ocupa?", "3*4", "Se multiplica el tamaño por minuto por los minutos.", " MB"),
        ex("Un curso tiene 5 canciones: 2 se aprenden de oído, 2 con partitura y 1 con un audio. ¿Cuántas se transmiten de forma oral?", "2", "Solo las que se aprenden de oído."),
    ],
    [
        ex("Pedro dice que, si una canción está en internet, puede subirla a otra página sin preguntar. ¿Tiene razón? Responde sí o no.", "No", "Las obras tienen autoras y autores y se necesita permiso."),
        ex("Una versión de una canción, aprendida solo de oído, tiene un cambio en el último verso respecto de la partitura. ¿Qué medio conserva con más exactitud las notas: la transmisión oral o la escrita?", "La escrita", "La partitura fija las notas; de oído pueden cambiar."),
    ],
    [
        ex("Un grupo de 15 personas quiere grabar su coro. 4 no dieron permiso y 2 no están seguras todavía. ¿Cuántas personas pueden aparecer hoy en la grabación?", "9", "15 − 4 − 2 = 9: solo quienes dieron permiso."),
        arith("El grupo envía 4 audios de 2 minutos cada uno. ¿Cuántos minutos de audio son en total?", "4*2", "Se multiplican los audios por su duración.", " minutos"),
    ],
    [ex("Tu curso quiere compartir la grabación del coro en internet. ¿Qué es lo primero: pedir permiso a quienes aparecen y a una persona adulta o subirla y avisar después?", "Pedir permiso a quienes aparecen y a una persona adulta", "Primero se pide permiso; avisar después ya no cuida a nadie.")],
    [ex("¿Qué transmisión usa partituras?", "La escrita", "Se aprende leyendo."), ex("¿Qué se debe pedir antes de grabar la voz de alguien?", "Permiso", "Es su voz."), ex("¿Qué datos no se ponen en un archivo compartido?", "Datos personales", "Se protege la privacidad.")],
    (
        "Una canción inventada se transmite así: Rosa la aprende de su tía cantándola en persona; luego la anota con cifrado C – F – G – C; después la graba con el permiso de las 6 personas que la cantan; y finalmente la comparte con otro curso. Escribe qué medios usó en cada paso, qué permisos hacen falta antes de grabar y compartir, y un nombre de archivo para el audio sin datos personales.",
        "Pasos: 1 oral, 2 escrita (cifrado), 3 grabada y 4 digital. Permisos: de las 6 personas que cantan y de una persona adulta. Nombre: cancion_ejemplo_curso7.",
        ["identifica los cuatro medios", "nombra los permisos necesarios", "propone un nombre de archivo sin datos personales"],
        ["lista de pasos y medios", "nombre de archivo"],
        ["omitir los permisos", "poner nombres completos en el archivo"],
        "Reconoce la lista y pide explicar qué se gana y qué se pierde en cada cambio de medio.",
    ),
    "Cuenta qué canciones aprendiste de oído, cuáles leyendo y cuáles escuchando un audio.",
    "Explica en cinco líneas cómo compartirías una canción del curso con otro curso respetando a todos.",
)

# ---------------------------------------------------------------- OA 04 · clase 4 (leer y cantar dos voces alineadas)
L(
    OA4, 4,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las dos voces están escritas en tablas por pulso; cada columna es un pulso. Puedes cantar cada voz con «la» por separado o con otra persona.",
    "Aprenderé a leer dos voces alineadas por pulso, calcular la distancia entre ellas y cantar la pieza con equilibrio. Sirve para interpretar música a dos voces con partitura y escuchar la armonía que forman.",
    ["Sé qué es una voz y qué es una tercera paralela.", "Sé restar números del 1 al 8.", "Sé que un compás agrupa pulsos."],
    [
        "Cuando hay dos voces, la partitura las escribe una encima de la otra, alineadas por pulso. Para leerlas, se mira hacia abajo cada pulso y se ve qué cantan las dos voces al mismo tiempo. Con los números de la escala, la distancia entre las dos voces es la resta del número mayor menos el menor. Si la distancia es 0, cantan la misma nota (unísono); si es 2, es una tercera; si es 4, es una quinta.",
        "Las distancias dan colores a la armonía: las voces en tercera y en quinta suenan estables, y las que están a un número de distancia suenan más tensas. Cuando las notas de las dos voces pertenecen a un mismo acorde, como el 1 y el 3 del acorde 1-3-5, suenan especialmente firmes. Por eso en la tercera paralela las dos voces mantienen siempre la distancia de 2.",
        "Para interpretar a dos voces se ensaya cada voz sola, luego juntas lentamente, escuchando cómo suena la combinación. Se cuida el equilibrio: si una voz tapa a la otra, se baja su volumen. Cada persona sigue su línea sin imitar a la otra, y todas respetan el mismo pulso. Un grupo puede alternar voces para que todas y todos conozcan ambas líneas.",
    ],
    [("alineadas por pulso", "escritas una bajo la otra, de modo que cada columna es un pulso"), ("distancia entre voces", "resta entre los números de las dos voces en un mismo pulso"), ("tercera y quinta", "distancias de 2 y de 4 números entre las voces"), ("equilibrio", "que ninguna voz tape a la otra"), ("unísono", "las dos voces cantan la misma nota")],
    [
        ("Leer una columna", "En el pulso 2 la voz 1 canta 8 y la voz 2 canta 4. ¿Cuál es la distancia y cómo se llama?", ["La distancia es 8 − 4 = 4.", "La distancia de 4 se llama quinta."], "4: una quinta"),
        ("Contar unísonos", "Pulso 1 al 5. Voz 1: 1 2 3 4 5. Voz 2: 1 1 5 5 5. ¿En cuántos pulsos cantan la misma nota?", ["Pulso 1: 1 y 1 coinciden.", "Pulsos 2, 3 y 4 no coinciden.", "Pulso 5: 5 y 5 coinciden."], "En 2 pulsos"),
    ],
    [
        ("Creer que la voz más aguda siempre debe sonar más fuerte.", "El volumen depende de qué voz lleva la melodía, no de qué tan aguda sea.", "Decide en el ensayo qué voz se oye más."),
        ("Cantar siguiendo a la otra voz en vez de a la propia.", "Se pierde la línea propia y se desordena el pulso.", "Ensaya tu voz sola hasta que te sientas seguro."),
    ],
    [
        ex("Si la voz 1 canta 4 y la voz 2 canta 4 en el mismo pulso, ¿cuál es la distancia?", "0", "4 − 4 = 0, es un unísono."),
        ex("¿Cuál es la distancia entre las notas 6 y 4 sonando a la vez?", "2", "6 − 4 = 2."),
        ex("Para ensayar a dos voces, ¿se parte con cada voz sola o con las dos juntas de inmediato?", "Con cada voz sola", "Así se asegura la propia línea."),
    ],
    [
        ex("Tabla por pulso. Voz 1: 5 5 6 5 3 1. Voz 2: 3 3 4 3 1 1. En el pulso 3, ¿qué canta cada voz y cuál es la distancia?", "6 y 4, distancia 2", "En la tercera columna están 6 y 4, y 6 − 4 = 2."),
        ex("En esa misma tabla (voz 1: 5 5 6 5 3 1; voz 2: 3 3 4 3 1 1), ¿en qué pulso cantan las dos voces la misma nota?", "En el pulso 6", "Solo en la última columna ambas cantan 1."),
        ex("Dos voces cantan las notas 3 y 3 a la vez. ¿Cómo se llama esa relación entre ellas?", "Unísono", "La distancia es 0."),
    ],
    [
        ex("Voz 1: 5 5 6 5 3 1. Voz 2: 3 3 4 3 1 1. ¿En cuántos pulsos hay una distancia de 2 (tercera)?", "5", "Los pulsos 1 a 5 tienen distancia 2; el pulso 6 tiene 0."),
        ex("Voz 1: 8 7 6 5. Voz 2: 6 5 4 3. ¿Cuál es la distancia en cada pulso y qué tipo de armonía hace?", "2 en los cuatro pulsos: tercera paralela", "Siempre baja dos números."),
        arith("Una pieza a dos voces tiene 8 compases de 4 pulsos. ¿Cuántas columnas de pulso hay que leer?", "8*4", "Hay una columna por pulso.", " columnas"),
    ],
    [
        ex("Ana dice que la voz más aguda debe sonar siempre más fuerte. ¿Tiene razón? Responde sí o no.", "No", "El volumen se decide según qué voz lleva la melodía."),
        ex("Una pieza tiene la melodía en la voz 2 y la voz 1 solo acompaña. Para mantener el equilibrio, ¿qué voz baja el volumen?", "La voz 1", "La que acompaña queda por debajo de la melodía."),
    ],
    [
        ex("Voz 1: 1 3 5 3. Voz 2: 1 1 3 1. ¿Cuántas veces la distancia entre voces es 0, 2 o 4 (unísono, tercera o quinta)?", "4", "Las distancias son 0, 2, 2 y 2: en los cuatro pulsos."),
        ex("Voz 1: 2 4 6 8. Voz 2: 1 2 3 4. ¿En qué pulso la distancia es mayor y cuánto vale?", "En el pulso 4, vale 4", "Las distancias son 1, 2, 3 y 4."),
    ],
    [ex("Dos grupos ensayan la pieza a dos voces de 8 compases a 60 pulsos por minuto, con 4 pulsos por compás. ¿Cuántos segundos dura una vuelta completa?", "32 segundos", "8 compases × 4 pulsos = 32 pulsos, y cada pulso dura un segundo.", "8*4*60//60")],
    [ex("¿Cómo se calcula la distancia entre dos voces?", "Restando los números", "El mayor menos el menor."), ex("¿Qué distancia tiene una tercera?", "2", "Una tercera son dos números de diferencia."), ex("¿Qué se cuida para que ninguna voz tape a la otra?", "El equilibrio", "Se ajusta el volumen de cada voz.")],
    (
        "Lee esta pieza inventada a dos voces por pulso. Voz 1: 3 4 5 6 5 3. Voz 2: 1 2 3 4 3 1. Calcula la distancia en cada pulso y escribe cuántas veces es 2. Canta o toca cada voz sola con «la» y luego, si puedes, junto con otra persona de tu casa, cuidando que ninguna tape a la otra. Escribe cómo sonó el equilibrio.",
        "Distancias: 2, 2, 2, 2, 2, 2: las seis son terceras. Cada voz sola salió bien; juntas, la voz 1 se oía más y la voz 2 bajó un poco el volumen para equilibrar.",
        ["calcula bien la distancia en los seis pulsos", "ensaya cada voz sola antes de juntarlas", "describe el equilibrio"],
        ["distancias escritas", "descripción del equilibrio"],
        ["restar mal", "no ensayar cada voz por separado"],
        "Reconoce las distancias y pide explicar qué voz lleva la melodía y cuál acompaña.",
    ),
    "Calcula la distancia entre las notas 7 y 5, 8 y 4, y 3 y 3.",
    "Escribe una segunda voz en quinta paralela (cuatro números abajo) para la melodía 6-7-8-7.",
)

# ---------------------------------------------------------------- OA 04 · clase 5 (ensayar y ajustar desde la escucha)
L(
    OA4, 5,
    "Lápiz y papel. Los registros de ensayo están escritos en los ejercicios. Si grabas tu práctica, hazlo solo con tu voz o con el permiso de quienes participan y de una persona adulta, y borra lo que no necesites.",
    "Aprenderé a ensayar y ajustar una interpretación a una o más voces escuchando una grabación o a mis compañeros, anotando problemas y decidiendo qué corregir primero. Sirve para mejorar de forma ordenada, sin repetir a ciegas.",
    ["Sé que la grabación guarda el sonido real.", "Sé aislar un compás con error.", "Sé restar números para comparar ensayos."],
    [
        "Ensayar bien es un ciclo con cuatro pasos. Primero se interpreta la pieza y, si hay permiso, se registra. Segundo, se escucha el registro con la partitura y se anotan los problemas: de ritmo, de afinación, de volumen o de equilibrio entre voces, con el compás donde ocurren. Tercero, se decide qué corregir primero. Cuarto, se vuelve a interpretar y se compara el nuevo registro con el anterior.",
        "Para decidir qué corregir primero se usa un criterio. Uno muy útil es empezar por el problema que afecta a más compases, porque corregirlo mejora más la pieza. Se corrige un problema a la vez: si se cambian cinco cosas juntas, no se sabe cuál ayudó. Los ajustes se practican aislando el compás, lento y sin apuro, antes de volver a la pieza completa.",
        "Para saber si mejoramos, se cuentan los problemas de cada ensayo y se comparan. Un ensayo puede salir peor que el anterior y la tendencia general seguir mejorando; por eso se miran varios ensayos. En un grupo, todas y todos escuchan y aportan observaciones respetuosas, hablando de lo que se oye. Así el ensayo es un trabajo compartido y no una evaluación a una sola persona.",
    ],
    [("ciclo de ensayo", "interpretar, escuchar, decidir y volver a interpretar"), ("registro de ensayo", "lista de problemas con el compás donde ocurren"), ("criterio", "regla para decidir qué corregir primero"), ("equilibrio", "que ninguna voz tape a otra"), ("tendencia", "cómo cambian los resultados a lo largo de varios ensayos")],
    [
        ("Elegir qué corregir", "Registro: afinación en 2 compases; ritmo en 6 compases; volumen en 1 compás. Con el criterio «primero el que afecta a más compases», ¿qué problema se corrige primero?", ["Comparo los compases afectados: 2, 6 y 1.", "El mayor es 6, del ritmo."], "El problema de ritmo"),
        ("Comparar ensayos", "Ensayo 1: 9 problemas. Ensayo 3: 4 problemas. ¿Cuántos problemas menos hay en el ensayo 3?", ["Resto 9 − 4.", "El resultado es 5."], "5 problemas menos"),
    ],
    [
        ("Corregir cinco cosas a la vez.", "Si se cambian muchas cosas juntas, no se sabe cuál mejoró el resultado.", "Corrige un problema a la vez y vuelve a escuchar."),
        ("Concluir que ensayar no sirve porque un ensayo salió peor.", "Una vuelta puede salir peor y la tendencia ser positiva.", "Compara varios ensayos antes de concluir."),
    ],
    [
        ex("Después de interpretar y registrar, ¿qué haces primero: escuchar y anotar problemas o borrar el registro?", "Escuchar y anotar problemas", "Sin escuchar no sabes qué ajustar."),
        ex("Si en el registro la voz 2 tapa a la voz 1, ¿qué voz conviene que baje su volumen?", "La voz 2", "La que tapa debe bajar para lograr equilibrio."),
        ex("Un error de ritmo en el compás 5, ¿qué compás practicas lento?", "El compás 5", "Se aísla el compás con error."),
    ],
    [
        ex("Registro: compás 3, entrada tarde; compás 5, nota desafinada; compás 7, volumen muy alto. ¿Cuántos problemas hay en total?", "3", "Hay uno en cada compás nombrado."),
        ex("En ese mismo registro, ¿cuántos problemas son de afinación?", "1", "Solo la nota desafinada del compás 5."),
        ex("Quieres saber si mejoraste. ¿Con qué registro comparas el nuevo: con el anterior o con el de otra persona?", "Con el anterior", "Se compara el progreso propio."),
    ],
    [
        ex("Registro: ritmo en 6 compases, afinación en 2 compases y volumen en 1 compás. ¿Cuántos compases en total tienen algún problema, si ningún compás repite problema?", "9", "6 + 2 + 1 = 9 compases."),
        arith("Un ensayo dura 30 minutos: 5 de calentamiento, 3 vueltas de 4 minutos cada una y el resto para ajustar. ¿Cuántos minutos quedan para ajustar?", "30-5-3*4", "Se restan el calentamiento y las vueltas al total.", " minutos"),
        ex("Quieres bajar de 9 problemas a menos de 3, quitando 2 por ensayo. ¿Cuántos ensayos hacen falta?", "4", "9 → 7 → 5 → 3 → 1: se necesitan 4 ensayos para llegar a menos de 3."),
    ],
    [
        ex("Laura corrige cinco problemas a la vez. ¿Es mejor corregir un problema por vez? Responde sí o no.", "Sí", "Así se ve cuál ajuste mejoró el resultado."),
        ex("Ana dice que ensayar no sirvió. Problemas: ensayo 1, 9; ensayo 2, 10; ensayo 3, 5. ¿Se puede decir que no sirvió? Responde sí o no.", "No", "En el ensayo 3 bajó a 5, la tendencia general mejoró."),
    ],
    [
        arith("Los problemas por ensayo fueron 12, 9, 7 y 4. ¿Cuántos problemas bajaron en total entre el primer y el último ensayo?", "12-4", "Se resta el último al primero.", " problemas"),
        ex("Quedan 15 minutos de ensayo: escuchar la grabación (4 minutos), ajustar 2 compases (3 minutos cada uno) y registrar de nuevo (4 minutos). ¿Alcanza el tiempo? Responde sí o no.", "Sí", "4 + 6 + 4 = 14 minutos, que es menos de 15."),
    ],
    [ex("Con permiso de tu familia, grabas solo tu voz cantando una frase de 8 compases a dos intentos. En el segundo intento hay 2 problemas menos que en el primero, que tuvo 5. ¿Cuántos problemas hubo en el segundo?", "3", "5 − 2 = 3.", "5-2")],
    [ex("¿Qué se hace después de escuchar la grabación y anotar problemas?", "Decidir qué corregir primero", "Es el tercer paso del ciclo."), ex("¿Cuántos problemas se corrigen a la vez?", "Uno", "Así se sabe qué ajuste ayudó."), ex("¿Qué se cuida al hablar con un compañero sobre su interpretación?", "Hablar de lo que se oye, con respeto", "El comentario se apoya en la evidencia audible.")],
    (
        "Usa este registro de ensayo inventado de una pieza a dos voces. Ensayo 1: compás 2, voz 2 entra tarde; compás 4, voz 1 desafinada; compás 6, voz 2 tapa a la voz 1; compás 7, ritmo apurado. Ensayo 2: compás 4 y compás 6. Escribe: 1) cuántos problemas bajaron entre los dos ensayos; 2) cuál problema quedó sin resolver; 3) un plan de ensayo de 15 minutos con tiempos para calentar, ajustar un problema y volver a interpretar.",
        "1) El ensayo 1 tuvo 4 problemas y el ensayo 2 tuvo 2, bajaron 2. 2) Quedaron sin resolver los problemas de los compases 4 y 6. 3) Plan: 4 min calentamiento, 7 min ajustar el compás 4 lento, 4 min volver a interpretar la pieza completa.",
        ["cuenta bien los problemas de cada ensayo", "identifica los que no se resolvieron", "planea un ajuste a la vez con tiempos"],
        ["comparación escrita", "plan de 15 minutos"],
        ["corregir todo a la vez", "no comparar con el ensayo anterior"],
        "Reconoce la comparación y pide explicar por qué eligió ese problema primero.",
    ),
    "Escucha o canta una frase tuya y anota un problema y un acierto.",
    "Diseña un plan de tres ensayos para una pieza a dos voces, con un ajuste distinto en cada uno.",
)
