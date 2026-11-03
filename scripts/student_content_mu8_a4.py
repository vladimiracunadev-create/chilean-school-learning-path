"""Student material for 8.º básico Música, OA 04 (interpretar repertorio a una y más voces, con precisión rítmica y melódica, usando medios de registro y transmisión como guía).

Todas las melodías, tomas y casos de los ejercicios son esquemas inventados para esta clase; el repertorio real lo selecciona el docente.
"""
from __future__ import annotations

from student_content_mu8_a import L
from student_lessons import arith, ex

OA4 = "MU08 OA 04"

NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"

# ---------------------------------------------------------------- OA 04 · clase 1 (una voz y más voces)
L(
    OA4, 1,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las melodías están escritas en los ejercicios; puedes cantarlas con «la» o tocarlas, solo o con alguien más, a volumen cómodo.",
    "Aprenderé a organizar una interpretación a una o más voces: unísono, a la octava, tercera paralela, bordón y canon. Sirve para planificar quién canta qué, cuándo entra cada voz y cuánto dura la pieza.",
    ["Sé cantar una melodía escrita con números.", "Sé que una melodía puede repetirse con retraso.", "Sé calcular compases y pulsos."],
    [
        f"Interpretar a una voz es cantar o tocar una sola línea melódica. Si todas las personas cantan las mismas notas, es unísono. Si una parte canta la misma melodía ocho grados más aguda o más grave ({NOTAS}), se canta a la octava y sigue siendo una sola línea, porque la nota 1 y la nota 8 tienen el mismo nombre. Interpretar a más voces es cantar dos o más líneas distintas a la vez.",
        "Hay varias formas sencillas de hacerlo. En la tercera paralela, la segunda voz canta dos números más abajo que la primera: si la voz 1 canta 7-6-5, la voz 2 canta 5-4-3. El bordón es una nota larga que suena debajo de la melodía sin cambiar, por ejemplo la nota 1. En el canon, cada voz canta la misma melodía, pero entra después de unos compases. Con 3 voces, cada entrada llega un cierto número de compases tras la anterior.",
        "Para interpretar a más voces conviene ensayar cada voz por separado, escuchar a las demás y mantener un pulso común. El reparto se calcula dividiendo el grupo en partes iguales, y el final de un canon se calcula sumando el retraso de la última voz al largo de la melodía. Si una voz entra tarde en un canon, no es un error: así funciona esa forma.",
    ],
    [("voz", "cada línea melódica de una pieza"), ("unísono", "todas las personas cantan las mismas notas a la vez"), ("octava", "misma melodía en un registro más agudo o más grave; la nota 8 repite el nombre de la 1"), ("bordón", "nota larga que suena debajo de la melodía sin cambiar"), ("canon", "la misma melodía que entra en cada voz con retraso")],
    [
        ("Escribir la voz 2", "La voz 1 canta 7-6-5. ¿Qué canta la voz 2 en tercera paralela?", ["La tercera paralela baja dos números en cada nota.", "7−2 = 5, 6−2 = 4, 5−2 = 3."], "5-4-3"),
        ("Calcular el final de un canon", "Una melodía de 6 compases se canta en canon a 2 voces con la segunda voz entrando 2 compases después. ¿En qué compás termina la segunda voz?", ["La voz 2 empieza en el compás 3.", "3 + 6 − 1 = 8."], "En el compás 8"),
    ],
    [
        ("Pensar que dos personas cantando una octava distinta son dos voces diferentes.", "Cantan la misma melodía en otro registro: sigue siendo una sola línea.", "Compara las notas, no los registros."),
        ("Creer que la voz que entra tarde en un canon se equivocó.", "En el canon cada voz entra con retraso a propósito.", "Mira en la partitura en qué compás debe entrar cada voz."),
    ],
    [
        ex("Una nota larga suena debajo de la melodía sin cambiar. ¿Cómo se llama?", "Bordón", "Es la definición de bordón."),
        ex("En tercera paralela, la voz 1 canta la nota 6. ¿Qué nota canta la voz 2?", "4", "La voz 2 va dos números más abajo."),
        ex("Cincuenta personas cantan las mismas notas al mismo tiempo. ¿Cuántas voces hay?", "1", "Es un unísono: una sola línea."),
    ],
    [
        ex("Un canon a 3 voces tiene una melodía de 4 compases y cada voz entra 2 compases después de la anterior. ¿En qué compás entra la voz 3?", "En el compás 5", "La voz 2 entra en el compás 3 y la voz 3 en el 5."),
        ex("Una voz aguda y una voz grave cantan la misma melodía, la grave ocho grados más abajo. ¿Cuántas melodías distintas hay?", "1", "Es la misma línea a la octava."),
        ex("Una voz canta 5-6-5-3 y un bordón canta la nota 1 todo el tiempo. ¿Cuántas notas distintas canta el bordón?", "1", "El bordón no cambia de nota."),
    ],
    [
        ex("La voz 1 canta 8-7-6-5. ¿Qué canta la voz 2 en tercera paralela?", "6-5-4-3", "Cada nota baja dos números."),
        arith("Un canon a 3 voces con melodía de 4 compases tiene entradas cada 2 compases. La voz 3 entra en el compás 5. ¿En qué compás termina?", "5+4-1", "Entra en el compás 5 y dura 4 compases.", ""),
        arith("Un grupo de 20 personas se divide por igual en 4 voces. ¿Cuántas personas hay en cada voz?", "20//4", "Se reparten 20 personas en 4 grupos iguales.", " personas"),
    ],
    [
        ex("Marta dice: «Si canto la misma melodía que mi compañera una octava más grave, somos dos voces distintas». ¿Tiene razón? Responde sí o no.", "No", "Es la misma línea melódica en otro registro."),
        ex("La voz 2 canta 2-3-4 en tercera paralela. ¿Qué canta la voz 1?", "4-5-6", "La voz 1 va dos números más arriba que la voz 2."),
    ],
    [
        arith("Un canon a 3 voces con melodía de 4 compases se toca en 4/4 a 80 pulsos por minuto. La voz 3 termina en el compás 8. ¿Cuántos segundos dura toda la pieza?", "8*4*60//80", "Son 32 pulsos que se convierten a segundos con el tempo.", " segundos"),
        ex("En ese mismo canon (melodía de 4 compases, entradas cada 2 compases), la voz 1 canta los compases 1 a 4, la voz 2 los compases 3 a 6 y la voz 3 los compases 5 a 8. ¿En cuántos compases suenan las tres voces a la vez?", "En ninguno", "La voz 1 termina en el compás 4 y la voz 3 entra en el 5."),
    ],
    [arith("Un grupo de 15 estudiantes se reparte por igual en 3 voces para cantar un canon en el acto del colegio. ¿Cuántos estudiantes hay en cada voz?", "15//3", "Se reparten 15 estudiantes en 3 grupos iguales.", " estudiantes")],
    [ex("¿Cómo se llama cantar las mismas notas a la vez?", "Unísono", "Es una sola línea cantada por varias personas."), ex("¿Cuántos números baja la voz 2 en una tercera paralela?", "2", "Va dos números más abajo."), ex("¿Qué se ensaya primero cuando se canta a más voces?", "Cada voz por separado", "Es la estrategia de la clase.")],
    (
        f"Con la melodía de ejemplo 5-5-6-5-3 ({NOTAS}) escribe: 1) su tercera paralela (dos números más abajo); 2) un bordón con la nota 1 que dure los 5 pulsos; 3) la melodía como canon a dos voces si cada nota dura un pulso y la voz 2 entra 2 pulsos después: ¿en qué pulso empieza y en cuál termina? Canta cada voz por separado con «la» y, si puedes, con otra persona de tu casa canten juntas dos de las voces.",
        "Tercera paralela: 3-3-4-3-1. Bordón: 1-1-1-1-1. Canon: la voz 1 canta en los pulsos 1 a 5 y la voz 2 empieza en el pulso 3 y termina en el pulso 7.",
        ["escribe bien la tercera paralela", "indica cuándo entra y termina la segunda voz", "ensaya cada voz por separado"],
        ["voz 2 escrita", "bordón escrito", "plan del canon"],
        ["contar mal los pulsos de entrada", "bajar otro número que dos"],
        "Reconoce la voz 2 y pide cantar solo la voz 2 con la mano marcando el pulso.",
    ),
    "Canta con «la» la melodía 5-5-4-3 y su tercera paralela 3-3-2-1, una después de la otra.",
    "Escribe un canon de 4 notas para tres voces e indica en qué pulso entra cada una.",
)

# ---------------------------------------------------------------- OA 04 · clase 2 (precisión rítmica y melódica)
L(
    OA4, 2,
    f"Lápiz y papel. Escala de números: {NOTAS}. Las melodías escritas y las ejecutadas están en los ejercicios, como listas de notas o de figuras. Puedes cantarlas con «la» para comprobarlas, a volumen cómodo.",
    "Aprenderé a medir la precisión rítmica y melódica de una interpretación comparando lo escrito con lo ejecutado: contar errores, calcular el porcentaje de aciertos y tomar decisiones. Sirve para mejorar sin adivinar, sobre todo cuando se canta a varias voces.",
    ["Sé leer una melodía escrita con números.", "Sé que cada figura tiene una duración.", "Sé que el pulso debe mantenerse parejo."],
    [
        "La precisión significa interpretar justo lo que está escrito. Un error melódico es cantar una nota distinta de la que corresponde. Un error rítmico es dar a una figura una duración distinta, o entrar antes o después de lo debido. Para medir la precisión, se comparan las dos listas nota por nota: la escrita y la ejecutada. Cada diferencia es un error, y el resto son aciertos.",
        "El porcentaje de aciertos se calcula dividiendo las notas correctas por las notas totales y multiplicando por 100. Si de 30 notas 27 son correctas, el resultado es 27 ÷ 30 × 100 = 90 %. Un porcentaje solo sirve si se comparan tomas con la misma cantidad de notas o se calcula el porcentaje de cada una. En un grupo, además de la precisión de cada persona, importa la sincronía: que todas entren juntas y mantengan el pulso.",
        "Para mejorar la precisión se practica despacio, con el pulso marcado, y se aísla el trozo que falla. En los pasajes a dos voces, cada persona ensaya su línea y luego escucha a la otra para ajustarse. Medir los errores toma por toma permite comprobar si el trabajo sirvió. Mejorar significa que los errores bajan, no que el volumen sube.",
    ],
    [("error melódico", "cantar una nota distinta de la escrita"), ("error rítmico", "dar a una figura una duración distinta o entrar a destiempo"), ("porcentaje de aciertos", "notas correctas ÷ notas totales × 100"), ("sincronía", "que todas las voces entren juntas y mantengan el mismo pulso"), ("toma", "cada vez que se interpreta y se registra una pieza completa")],
    [
        ("Contar errores", "Escrito: 1-2-3-5-3-2-1. Cantado: 1-2-4-5-3-1-1. ¿Cuántos errores melódicos hay?", ["Se comparan posición por posición.", "En la 3.ª nota se cantó 4 en vez de 3 y en la 6.ª se cantó 1 en vez de 2."], "2 errores"),
        ("Calcular el porcentaje", "En una toma de 10 notas, 8 son correctas. ¿Qué porcentaje de aciertos hay?", ["8 ÷ 10 = 0,8.", "0,8 × 100 = 80."], "80 %"),
    ],
    [
        ("Pensar que, si las notas están bien, la interpretación es precisa.", "También cuentan las duraciones y el pulso.", "Revisa notas, duraciones y entradas."),
        ("Comparar dos tomas sin decir cuántas notas tiene cada una.", "Un número de errores solo se entiende respecto del total de notas.", "Calcula el porcentaje de aciertos de cada toma."),
    ],
    [
        ex("Escrito: 1-2-3-5. Cantado: 1-2-4-5. ¿En qué posición está el error?", "En la 3.ª nota", "La tercera nota debía ser 3 y se cantó 4."),
        ex("Una voz entra un pulso más tarde de lo escrito. ¿Es un error rítmico o melódico?", "Rítmico", "La nota puede ser la correcta, pero llegó a destiempo."),
        ex("Cantas la nota correcta, pero la dejas sonar más corta de lo escrito. ¿Es un error rítmico o melódico?", "Rítmico", "Se alteró la duración, no la altura."),
    ],
    [
        ex("Escrito: 5-4-3-2-1. Cantado: 5-4-3-2-2. ¿Cuántos errores hay?", "1", "Solo la última nota es distinta."),
        ex("Escrito: negra, negra, blanca. Tocado: negra, negra, negra. ¿Qué error rítmico hubo? A) La blanca se acortó a negra. B) Se tocó una nota de más.", "A", "La tercera figura debía durar más que una negra."),
        ex("¿Qué ayuda más a la precisión? A) Practicar despacio con el pulso marcado. B) Tocar más rápido para que los errores no se noten.", "A", "El tempo lento permite corregir cada nota y cada duración."),
    ],
    [
        arith("En una toma de 20 notas, 17 son correctas. ¿Qué porcentaje de aciertos hay?", "17*100//20", "Se divide lo correcto por el total y se multiplica por 100.", " %"),
        ex("Escrito: 1-2-3-5-3-2-1. Cantado: 1-2-4-5-3-2-2. ¿Cuántos errores hay?", "2", "Fallan la 3.ª nota (4 en vez de 3) y la 7.ª (2 en vez de 1)."),
        arith("Un grupo tuvo 6, 4 y 2 errores en tres ensayos seguidos. ¿Cuántos errores menos hubo en el tercer ensayo que en el primero?", "6-2", "Se resta lo del tercer ensayo de lo del primero.", " errores menos"),
    ],
    [
        ex("Toma A: 1-2-3-5-3-2-1, con el pulso irregular. Toma B: 1-2-4-5-3-2-1, con el pulso parejo. ¿Cuál tiene un error melódico?", "La toma B", "Cantó 4 en vez de 3; la A tiene un error de pulso."),
        ex("Ana dice: «Toqué todas las notas bien, así que mi interpretación es precisa». ¿Basta con las notas correctas? Responde sí o no.", "No", "También importan las duraciones y el pulso."),
    ],
    [
        arith("Una toma tuvo 15 notas correctas de 20 y la siguiente tuvo 18 de 20. ¿Cuántos puntos subió el porcentaje de aciertos?", "18*100//20-15*100//20", "Se calcula el porcentaje de cada toma y se resta.", " puntos"),
        ex("A 60 pulsos por minuto, una voz entra 2 pulsos más tarde de lo escrito. ¿Cuántos segundos se atrasa?", "2 segundos", "A 60 por minuto cada pulso dura un segundo."),
    ],
    [arith("El coro del colegio ensaya una canción de 50 notas y comete 5 errores. ¿Qué porcentaje de aciertos tiene?", "45*100//50", "Hay 45 notas correctas sobre 50.", " %")],
    [ex("¿Qué se compara para medir la precisión?", "Lo escrito con lo ejecutado", "Nota por nota y figura por figura."), ex("¿Qué es la sincronía?", "Que todas las voces entren juntas y con el mismo pulso", "Es la precisión del grupo."), ex("¿Mejorar es subir el volumen? Responde sí o no.", "No", "Mejorar es que bajen los errores.")],
    (
        f"Compara estas dos listas de ejemplo: escrito 1-2-3-4-5-4-3-2-1-1; cantado 1-2-3-4-4-4-3-1-1-1 ({NOTAS}). 1) Marca las posiciones con error melódico. 2) Cuenta aciertos y calcula el porcentaje. 3) Escribe una decisión de práctica para la próxima toma, indicando qué trozo ensayarás despacio y con el pulso marcado.",
        "Errores en las posiciones 5 (4 en vez de 5) y 8 (1 en vez de 2): 2 errores. Aciertos 8 de 10 = 80 %. Decisión: ensayar despacio las notas 5 y 8 con el pulso marcado, con una nota de referencia.",
        ["encuentra todos los errores", "calcula bien el porcentaje", "propone una práctica concreta"],
        ["posiciones con error", "porcentaje de aciertos", "decisión escrita"],
        ["no revisar todas las posiciones", "confundir el porcentaje con el número de errores"],
        "Reconoce el cálculo y pide cantar el trozo que ensayará, despacio, con el pulso marcado.",
    ),
    "Canta 5-4-3-2-1 sin errores y cuenta si lo hiciste a un pulso parejo.",
    "Escribe una lista de 8 notas con 2 errores a propósito y pide a otra persona que los encuentre.",
)

# ---------------------------------------------------------------- OA 04 · clase 3 (medios de registro)
L(
    OA4, 3,
    "Lápiz y papel. Los cifrados, partituras y casos están escritos en los ejercicios. Cifrado de la clase: C = do mayor; F = fa mayor; G = sol mayor; Am = la menor. Si quieres, practica con un dispositivo de grabación de audio que ya tengas en casa, a volumen bajo.",
    "Aprenderé qué medios sirven para registrar música (partitura, cifrado, notación gráfica, grabación de audio y de video) y cuándo conviene cada uno. Sirve para guardar una pieza, ensayarla y revisar cómo suena.",
    ["Sé que una partitura escribe las notas y su duración.", "Sé que una grabación guarda cómo suena una interpretación.", "Sé sumar y multiplicar números pequeños."],
    [
        "Registrar música es guardarla para recordarla, ensayarla o compartirla. La partitura convencional escribe las notas y sus duraciones. El cifrado anota los acordes con letras: C es do mayor, F es fa mayor, G es sol mayor y Am es la menor. La notación gráfica usa dibujos, como una línea que sube cuando la melodía sube y se engrosa cuando crece el volumen. La grabación de audio guarda el sonido. La grabación de video guarda el sonido y la imagen.",
        "Cada medio guarda algo distinto y deja otras cosas fuera. La partitura no guarda el timbre de quien interpreta. El audio guarda el timbre, el pulso y las dinámicas, pero no muestra la postura. El video muestra la postura y la respiración, pero necesita permiso de las personas que aparecen. El cifrado es rápido para acompañar, pero no escribe la melodía. Elegir bien el medio depende de lo que se quiere guardar.",
        "Para grabar bien conviene un lugar silencioso, una distancia constante entre las personas y el dispositivo, y un volumen que no se sature. Cada archivo debe guardarse con un nombre claro que incluya la pieza, la fecha y el número de toma. Después se escucha la grabación con criterios, como el pulso parejo y las entradas a tiempo, y se decide qué ajustar.",
    ],
    [("partitura", "registro escrito de notas y duraciones"), ("cifrado", "anotación de los acordes con letras"), ("notación gráfica", "dibujos que representan rasgos de la música"), ("toma", "cada vez que se graba una pieza completa"), ("saturación", "volumen tan alto que el sonido se distorsiona al grabar")],
    [
        ("Elegir el medio", "Quieres que una compañera ausente aprenda una melodía, pero ella no sabe leer partitura. ¿Qué medio le sirve más: grabación de audio o cifrado?", ["El cifrado no escribe la melodía.", "El audio le deja escuchar cómo suena."], "La grabación de audio"),
        ("Calcular tomas", "Un grupo graba 3 tomas de 150 segundos cada una. ¿Cuántos segundos graba en total?", ["Son 3 tomas iguales.", "3 × 150 = 450."], "450 segundos"),
    ],
    [
        ("Pensar que la partitura guarda cómo suena cada intérprete.", "La partitura no guarda el timbre ni la manera de interpretar de cada persona.", "Si importa el sonido, graba un audio."),
        ("Guardar los archivos sin nombre claro.", "Después no se sabe cuál toma es cuál.", "Escribe pieza, fecha y número de toma."),
    ],
    [
        ex("¿Qué medio anota los acordes con letras?", "El cifrado", "Cada letra representa un acorde."),
        ex("Una grabación de audio, ¿permite oír el timbre de la voz? Responde sí o no.", "Sí", "El audio guarda el sonido, incluido el timbre."),
        ex("¿Qué medio permite ver cómo respira y se coloca una persona al cantar?", "El video", "Muestra la imagen además del sonido."),
    ],
    [
        ex("En el cifrado «C – F – G», ¿cuántos acordes distintos hay?", "3", "Son tres letras distintas."),
        ex("En el cifrado de la clase, ¿qué acorde representa la letra F?", "Fa mayor", "Así lo dice el cifrado de la clase."),
        ex("Para una buena grabación, ¿qué conviene? A) Un lugar silencioso. B) El patio durante el recreo, para que se oiga el ambiente.", "A", "El ruido ambiente tapa la música y no se puede quitar después."),
    ],
    [
        arith("Un grupo guarda tomas de 90 segundos. Graba 4 y descarta 1. ¿Cuántos segundos de grabación quedan guardados?", "(4-1)*90", "Quedan 3 tomas de 90 segundos.", " segundos"),
        ex("El cifrado C F G C se repite 4 veces, un acorde por compás. ¿Cuántos compases usan el acorde G?", "4", "El acorde G aparece una vez en cada repetición."),
        ex("¿Cómo conviene nombrar un archivo de grabación? A) Con la pieza, la fecha y el número de toma. B) Solo con la palabra «audio».", "A", "Así se reconoce cada toma después."),
    ],
    [
        ex("Un coro quiere guardar la manera de colocar la boca y de respirar. ¿Le sirve un audio o un video con permiso de quienes aparecen?", "Un video con permiso", "El audio no muestra la imagen."),
        ex("¿La partitura guarda el timbre de cada instrumento? Responde sí o no.", "No", "Solo escribe notas y duraciones."),
    ],
    [
        arith("Un grupo ensaya una pieza de 5 minutos y graba 2 tomas completas. ¿Cuántos minutos de grabación hay?", "5*2", "Se multiplica la duración por el número de tomas.", " minutos"),
        ex("Una línea dibujada empieza fina y baja, y luego se engrosa y sube. ¿Qué dos rasgos de la música anota en notación gráfica?", "La altura y el volumen", "La posición de la línea muestra la altura y el grosor muestra el volumen."),
    ],
    [ex("Un grupo grabó una toma de 2 minutos y a los 40 segundos se oye una conversación al fondo. ¿Qué conviene? A) Volver a grabar en un lugar silencioso. B) Dejar la toma así, sin decir nada.", "A", "El ruido tapa la música y se resuelve con una nueva toma.")],
    [ex("¿Qué medio guarda notas y duraciones por escrito?", "La partitura", "Es el registro escrito convencional."), ex("¿Qué datos lleva el nombre de un archivo?", "Pieza, fecha y número de toma", "Así se reconoce cada toma."), ex("¿Qué medio necesita permiso de las personas que aparecen?", "El video", "Muestra su imagen.")],
    (
        "Elige una de estas dos situaciones de ejemplo. A) Un grupo quiere enseñar a otro curso el acompañamiento «C – F – G – C», un acorde por compás, repetido 4 veces. B) Una estudiante quiere guardar su canción de 3 minutos para revisarla. Para tu situación escribe 1) qué medio o medios de registro usarías y por qué, 2) un nombre de archivo o de papel con pieza, fecha y número de toma, 3) una condición para grabar bien (lugar, distancia o volumen), 4) cuántos segundos se graban si hay 2 tomas (en la situación A cada toma dura 1 minuto y en la B dura 3 minutos).",
        "Situación A: cifrado, porque escribe los acordes con letras, y audio para oír el ritmo. Nombre: «acompañamiento-C-F-G-fecha-toma1». Condición: lugar silencioso. Segundos: 2 tomas de 60 segundos = 120 segundos. (Situación B: audio, nombre «cancion-fecha-toma1», 2 tomas de 180 segundos = 360 segundos.)",
        ["relaciona el medio con lo que quiere guardar", "escribe un nombre con pieza, fecha y toma", "da una condición de grabación"],
        ["medio elegido con motivo", "nombre del archivo", "condición y cálculo"],
        ["elegir un medio que no guarda lo que se necesita", "olvidar el número de toma"],
        "Reconoce el medio elegido y pide explicar qué se pierde al no usar el otro.",
    ),
    "Anota con un cifrado de tres letras el acompañamiento de una canción que conozcas.",
    "Dibuja la notación gráfica de un sonido que sube y se hace más fuerte, y de otro que baja y se hace más suave.",
)

# ---------------------------------------------------------------- OA 04 · clase 4 (medios de transmisión y respeto)
L(
    OA4, 4,
    "Lápiz y papel. Los casos están escritos en los ejercicios (son de ejemplo). No se necesita grabar ni publicar nada: se trata de decidir bien antes de compartir música.",
    "Aprenderé qué medios hay para transmitir música (en vivo, radio escolar, plataformas en línea y mensajes) y cómo compartirla con respeto: pedir permiso, citar la autoría, proteger los datos personales y avisar a una persona adulta de confianza si algo sale mal. Sirve para presentar mi trabajo musical de forma segura.",
    ["Sé que una grabación guarda una interpretación.", "Sé que algunas personas no quieren aparecer en videos.", "Sé que debo pedir ayuda a una persona adulta de confianza si algo me inquieta."],
    [
        "Transmitir música es hacerla llegar a otras personas. Puede ser en vivo, como en un acto escolar, donde el público escucha una sola vez. Puede ser por radio escolar o por una plataforma en línea, donde la grabación se escucha varias veces y llega lejos. También puede enviarse por mensaje a personas conocidas. Cada medio llega a un público distinto, y mientras más abierto es, más cuidado exige.",
        "Compartir con respeto significa pedir permiso a todas las personas que aparecen en una grabación. Si son menores de edad, una persona adulta responsable también debe autorizar. Hay que decir quién creó la música y quién la interpreta, y no presentar como propia una obra ajena. Muchas obras tienen derechos de autor, así que antes de publicar una obra ajena se consulta a la docente. No se escriben datos personales, como nombre completo, dirección o el lugar donde está la persona. Conviene compartir primero por canales del colegio y con personas conocidas.",
        "Si alguien escribe un comentario ofensivo, no se responde ni se discute: se avisa a una persona adulta de confianza. Si un material se publicó sin permiso, se retira y se avisa a quien aparecía en él. Antes de publicar, se revisan tres condiciones: tener los permisos, citar la autoría y no mostrar datos personales. Si falta una, no se publica.",
    ],
    [("transmisión", "hacer llegar la música a otras personas"), ("permiso", "autorización de quien aparece en una grabación; en menores, también de una persona adulta responsable"), ("autoría", "quién creó la obra y quién la interpreta"), ("datos personales", "información que identifica a alguien, como el nombre completo o la dirección"), ("canal del colegio", "medio de difusión que usa el establecimiento, con adultos responsables")],
    [
        ("Contar permisos", "Un video muestra a 12 estudiantes y 9 ya tienen autorización. ¿Cuántas autorizaciones faltan?", ["Hay 12 personas y 9 autorizaciones.", "12 − 9 = 3."], "Faltan 3"),
        ("Aplicar las tres condiciones", "Una grabación tiene permisos y cita la autoría, pero se ve la dirección de una casa. ¿Se puede publicar?", ["Las condiciones son permisos, autoría y sin datos personales.", "La dirección es un dato personal."], "No, hasta quitar el dato personal"),
    ],
    [
        ("Subir una obra ajena sin decir quién la creó.", "Se estaría presentando como propia una obra ajena.", "Anota quién la creó y quién la interpreta."),
        ("Responder los comentarios ofensivos para defenderse.", "Responder puede empeorar la situación.", "No respondas y avisa a una persona adulta de confianza."),
    ],
    [
        ex("Para publicar un video donde aparece una compañera, ¿qué se necesita primero?", "Su permiso", "Nadie debe aparecer en una grabación sin autorizarlo."),
        ex("Cuando se interpreta una canción de otra persona, ¿hay que decir quién la creó? Responde sí o no.", "Sí", "Se cita la autoría para reconocer a quien creó la obra."),
        ex("¿Se puede escribir tu dirección en la descripción de una grabación? Responde sí o no.", "No", "Es un dato personal."),
    ],
    [
        ex("¿Qué es más correcto? A) Indicar quién creó la canción y que yo la interpreté. B) Decir que yo creé una canción que no es mía.", "A", "La autoría debe ser verdadera."),
        ex("Recibes un mensaje ofensivo sobre tu grabación. ¿Qué haces primero: avisas a una persona adulta de confianza o respondes con otro insulto?", "Aviso a una persona adulta de confianza", "Responder puede empeorar la situación."),
        ex("¿Qué medio permite escuchar varias veces lo mismo: un acto en vivo o una grabación publicada?", "Una grabación publicada", "El acto en vivo se escucha una sola vez."),
    ],
    [
        arith("En un acto escolar se hacen 3 funciones con 120 personas en cada una. ¿Cuántas personas escuchan en total?", "3*120", "Se multiplican las funciones por el público de cada una.", " personas"),
        arith("La radio escolar emite 4 canciones por programa y hace 5 programas. ¿Cuántas canciones emite?", "4*5", "Se multiplican las canciones por los programas.", " canciones"),
        ex("Un grupo quiere compartir una grabación con rostros y nombres completos en una plataforma abierta. ¿Qué es más adecuado? A) Compartirla primero por un canal del colegio, con permisos. B) Subirla de inmediato a una plataforma abierta y pedir los permisos después.", "A", "Un canal conocido y los permisos protegen a quienes aparecen."),
    ],
    [
        ex("Ana dice: «No hace falta citar la autoría si la canción es famosa». ¿Tiene razón? Responde sí o no.", "No", "La autoría siempre se reconoce, sea famosa o no."),
        ex("Una grabación se publicó sin que una estudiante lo supiera. ¿Qué conviene hacer primero: retirarla y avisarle, o dejarla hasta que se queje?", "Retirarla y avisarle", "Se repara cuanto antes la falta de permiso."),
    ],
    [
        arith("Un grupo prepara un programa para la radio escolar con 3 canciones de 2 minutos y 4 canciones de 3 minutos. ¿Cuántos minutos de música tiene?", "3*2+4*3", "Se suman los minutos de cada tipo de canción.", " minutos"),
        ex("Condiciones para publicar: permisos, autoría citada y sin datos personales. Una grabación tiene permisos y no tiene datos personales, pero no cita la autoría. ¿Se publica? Responde sí o no.", "No", "Debe cumplir las tres condiciones."),
    ],
    [ex("El curso quiere enviar una grabación de su canción a las familias. ¿Qué es más adecuado? A) Enviarla por el canal del colegio, con permisos. B) Subirla a una plataforma abierta con el nombre completo de cada estudiante.", "A", "El canal del colegio es conocido y protege los datos personales.")],
    [ex("¿Qué tres condiciones se revisan antes de publicar?", "Permisos, autoría y sin datos personales", "Si falta una, no se publica."), ex("¿Qué haces si alguien comenta algo ofensivo sobre tu música?", "Aviso a una persona adulta de confianza", "No respondes ni lo discutes."), ex("¿Qué medio llega a más personas: un mensaje entre dos amigas o una plataforma abierta?", "Una plataforma abierta", "Llega a un público más amplio.")],
    (
        "Revisa este caso de ejemplo. Un curso quiere publicar un video de 3 minutos de su canción. En el video aparecen 10 estudiantes: 8 tienen autorización de su persona adulta responsable. La canción fue creada por otra persona y el curso solo la interpreta. En la descripción del video está escrito el nombre completo de cada estudiante y el nombre del colegio. Escribe 1) cuántas autorizaciones faltan, 2) qué cambios harías en la descripción, 3) a quién preguntarías para decidir en qué canal publicarlo, 4) si hay un comentario ofensivo después de publicar, qué haces.",
        "Faltan 2 autorizaciones. En la descripción: quitar nombres completos y el colegio, e indicar quién creó la canción y que el curso la interpreta. Preguntaría a la docente o a una persona adulta responsable del colegio. Ante un comentario ofensivo: no respondería y avisaría a una persona adulta de confianza.",
        ["cuenta bien los permisos que faltan", "protege los datos personales y cita la autoría", "avisa a una persona adulta de confianza"],
        ["cuatro respuestas escritas"],
        ["publicar sin tener todos los permisos", "responder el comentario ofensivo"],
        "Reconoce las respuestas y pide explicar por qué no se puede publicar mientras falten permisos.",
    ),
    "Escribe una frase para citar la autoría de una canción: quién la creó y quién la interpreta.",
    "Escribe una lista de tres condiciones que revisarías antes de compartir una grabación de tu curso.",
)

# ---------------------------------------------------------------- OA 04 · clase 5 (ensayar, registrar y ajustar)
L(
    OA4, 5,
    "Lápiz y papel. Las tomas y los planes de ensayo están descritos en los ejercicios (son de ejemplo). Puedes aplicar lo aprendido con tu propia práctica, ensayando, registrando por audio y revisando con los mismos criterios.",
    "Aprenderé el ciclo ensayar, registrar, escuchar con criterios y ajustar, y a planificar un ensayo con tiempos. Sirve para mejorar una interpretación a una o más voces con decisiones basadas en lo que se oye.",
    ["Sé medir la precisión comparando lo escrito con lo ejecutado.", "Sé que una toma es una vez que se interpreta la pieza.", "Sé cuidar los permisos al grabar."],
    [
        "Mejorar una interpretación sigue un ciclo de cuatro pasos. Se ensaya, se registra una toma, se escucha con criterios y se ajusta lo que falló. Después se vuelve a ensayar y se registra otra toma para comprobar si mejoró. Los criterios son las preguntas fijas con que se revisa cada toma: ¿el pulso es parejo?, ¿las notas son correctas?, ¿las voces entran a tiempo?, ¿se cumple la dinámica?",
        "Conviene planificar el ensayo con minutos. Por ejemplo, en 30 minutos: 5 de calentamiento, 10 para la célula difícil, 10 para unir los trozos y 5 para una toma. Cada ensayo trabaja un foco principal, no todo a la vez. Si se cambia el tempo, las notas y la dinámica juntos, no se sabe qué ajuste produjo la mejora. Con un foco por ensayo, la causa es clara.",
        "Para comprobar el progreso se comparan las tomas con los mismos criterios. Si la toma 1 cumple 1 de los 4 criterios y la toma 2 cumple 3, mejoró en dos. Se registra cada resultado, para mostrar evidencia. Una interpretación a varias voces mejora cuando cada persona cumple su parte y escucha a las demás. Al final del ciclo se decide un nuevo foco para el próximo ensayo.",
    ],
    [("ciclo de ensayo", "ensayar, registrar, escuchar con criterios y ajustar"), ("criterio", "pregunta fija con que se revisa una toma, como si el pulso es parejo"), ("foco", "el aspecto que se trabaja en un ensayo"), ("ajuste", "cambio que se hace para corregir lo que falló"), ("evidencia", "dato de la toma que muestra que algo mejoró o no")],
    [
        ("Contar criterios", "En la toma 1 el pulso no es parejo, las notas son correctas, las entradas no son a tiempo y la dinámica se cumple. ¿Cuántos de los 4 criterios cumple?", ["Cumple las notas y la dinámica.", "Son 2 de 4."], "2 de 4"),
        ("Planificar el tiempo", "Un ensayo dura 45 minutos: 5 de calentamiento, 15 para la célula difícil y 10 para la toma. ¿Cuántos minutos quedan para escuchar y ajustar?", ["Se suman los minutos usados: 5 + 15 + 10 = 30.", "45 − 30 = 15."], "15 minutos"),
    ],
    [
        ("Cambiar muchas cosas a la vez después de una mala toma.", "Si se cambia todo, no se sabe cuál ajuste ayudó.", "Elige un foco por ensayo."),
        ("Comparar tomas por recuerdo.", "La memoria falla; se necesitan los mismos criterios para comparar.", "Usa la misma lista de criterios en cada toma."),
    ],
    [
        ex("¿Qué se hace después de registrar una toma?", "Escucharla con criterios", "Así se detecta lo que hay que ajustar."),
        ex("¿Cuántos focos conviene trabajar en un mismo ensayo: uno o muchos?", "Uno", "Con uno solo se sabe qué ajuste produjo la mejora."),
        ex("¿Para qué se vuelve a grabar después de ajustar?", "Para comprobar si mejoró", "La nueva toma muestra el efecto del ajuste."),
    ],
    [
        ex("Una toma cumple el pulso parejo y la dinámica, pero falla las notas y las entradas. ¿Cuántos de los 4 criterios cumple?", "2", "Cumple dos y falla dos."),
        ex("Si fallan dos criterios, ¿conviene trabajar los dos a la vez o primero uno? Responde con una de las dos opciones.", "Primero uno", "Así se sabe qué ajuste ayudó."),
        ex("¿Cómo se compara la toma 2 con la toma 1? A) Con los mismos criterios. B) Por lo que se recuerda.", "A", "Los mismos criterios permiten una comparación justa."),
    ],
    [
        arith("Un plan de ensayo tiene 5 minutos de calentamiento, 10 para la célula difícil, 10 para unir los trozos y 5 para una toma. ¿Cuántos minutos dura el ensayo?", "5+10+10+5", "Se suman los minutos de cada parte.", " minutos"),
        arith("La toma 1 tuvo 6 errores y la toma 2 tuvo 3. ¿Cuántos errores menos hubo en la toma 2?", "6-3", "Se resta lo de la toma 2 de lo de la toma 1.", " errores menos"),
        ex("Un grupo tiene 20 minutos y cada ciclo completo (ensayar, registrar, escuchar y ajustar) dura 5 minutos. ¿Cuántos ciclos completos alcanza a hacer?", "4", "20 ÷ 5 da 4."),
    ],
    [
        ex("La toma 1 cumple 1 de los 4 criterios y la toma 2 cumple 3 de 4. ¿Mejoró? ¿Cuántos criterios más cumple?", "Sí; 2 criterios más", "3 − 1 = 2."),
        ex("Un grupo cambia el tempo, las notas y la dinámica a la vez después de una toma mala. ¿Qué no podrá saber: cuál ajuste produjo la mejora o cuántas notas tiene la pieza?", "Cuál ajuste produjo la mejora", "Al cambiar todo junto, no se aísla la causa."),
    ],
    [
        arith("Un grupo parte con 8 errores y corrige 2 errores en cada ensayo. ¿Cuántos errores le quedan tras 3 ensayos?", "8-2*3", "Se restan los errores corregidos en los tres ensayos.", " errores"),
        arith("Una pieza de 24 pulsos debía durar 24 segundos a 60 pulsos por minuto, pero la toma duró 30 segundos. ¿Cuántos segundos más lenta fue?", "30-24", "Se resta la duración esperada de la duración real.", " segundos"),
    ],
    [ex("Una banda escolar graba una toma y escucha que el pulso se acelera en el final. ¿Qué foco puede trabajar en el próximo ensayo: el pulso parejo en el final o el volumen del comienzo?", "El pulso parejo en el final", "Es el criterio que falló en la toma.")],
    [ex("¿Cuáles son los cuatro pasos del ciclo?", "Ensayar, registrar, escuchar con criterios y ajustar", "Es el orden de la clase."), ex("¿Cuántos focos principales conviene por ensayo?", "Uno", "Trabajar más hace perder claridad."), ex("¿Qué se hace con los mismos criterios en cada toma?", "Compararlas", "Así se mide el progreso.")],
    (
        "Usa estas dos tomas de ejemplo de una canción a dos voces. Toma 1: pulso parejo, no; notas correctas, no; entradas a tiempo, sí; dinámica, no. Toma 2: pulso parejo, sí; notas correctas, no; entradas a tiempo, sí; dinámica, sí. Escribe 1) cuántos criterios cumple cada toma, 2) cuál es el próximo foco que elegirías y por qué, 3) un plan de 30 minutos con tiempos que sumen 30 y que incluya una nueva toma.",
        "Toma 1 cumple 1 de 4; toma 2 cumple 3 de 4. Próximo foco: las notas correctas, porque es el criterio que falla. Plan: calentamiento 5, practicar despacio los trozos con notas incorrectas 15, unir 5, nueva toma 5 = 30.",
        ["cuenta bien los criterios de cada toma", "elige un foco justificado con un dato", "arma un plan que suma 30"],
        ["conteo por toma", "foco elegido", "plan con tiempos"],
        ["elegir más de un foco sin razón", "un plan cuyos minutos no suman 30"],
        "Reconoce el plan y pide mostrar en cuál minuto se registrará la nueva toma y qué se hará con ella.",
    ),
    "Escribe los cuatro criterios que usarías para revisar una toma de tu curso.",
    "Describe un ciclo de ensayo con dos tomas y qué foco cambiarías entre una y otra.",
)
