"""Student material for 7.º básico Música, OA 05 (improvisar y crear música con ambientaciones sonoras libres y acompañamientos rítmicos, melódicos y/o armónicos simples).

Todas las melodías, escenas y patrones de los ejercicios son inventados para esta clase. Los sonidos se producen con el cuerpo, la voz y objetos cotidianos seguros (sin vidrio, sin fuego, sin electricidad de red) a volumen bajo.
"""
from __future__ import annotations

from student_content_mu7_a import L
from student_lessons import arith, ex

OA5 = "MU07 OA 05"
NOTAS = "1 = do, 2 = re, 3 = mi, 4 = fa, 5 = sol, 6 = la, 7 = si, 8 = do agudo"
PENTA = "1, 2, 3, 5 y 6 (do, re, mi, sol y la)"
LEY = "semicorchea = 1 unidad; corchea = 2; negra = 4 (un pulso); blanca = 8; redonda = 16"

# ---------------------------------------------------------------- OA 05 · clase 1 (improvisar con reglas)
L(
    OA5, 1,
    f"Lápiz y papel. Escala de números: {NOTAS}. Notas permitidas para improvisar: {PENTA}. Si tienes un instrumento melódico o puedes cantar con «la», improvisa a volumen bajo; si no, escribe las melodías con números.",
    "Aprenderé a improvisar una melodía con un conjunto de notas permitidas y reglas simples. Sirve para crear música en el momento sin miedo a equivocarme y con un resultado que suena bien.",
    ["Sé escribir una melodía con números del 1 al 8.", "Sé que una melodía tiene principio y final.", "Sé contar notas de una lista."],
    [
        "Improvisar es crear música en el momento, mientras se canta o se toca. No significa tocar cualquier cosa: se improvisa dentro de reglas que dan seguridad. Una regla muy útil es elegir un conjunto de notas permitidas. En esta clase usaremos las notas "
        + PENTA + ". Con ellas, casi cualquier combinación suena bien, porque no incluyen las notas 4 y 7, que son las que más tensión producen.",
        "Además se fijan reglas de forma. Por ejemplo: improvisar 8 notas, a un pulso estable, empezar donde quieras y terminar en la nota 1 para que se sienta un final. También conviene repetir una idea corta y variarla, porque una idea que vuelve cambiada hace que la improvisación tenga sentido. Si una nota sale fuera del conjunto, no pasa nada: se sigue con el pulso y se vuelve al conjunto en la siguiente nota.",
        "Improvisar se puede hacer solo o con un grupo. En grupo, una persona mantiene el pulso o un ostinato y las demás improvisan por turnos, escuchándose. Nadie está obligado a improvisar frente al curso: se puede hacer en parejas, en grupos pequeños o en privado. Lo importante es probar, escuchar el resultado y repetir cambiando algo, como se hace con cualquier otra habilidad.",
    ],
    [("improvisar", "crear música en el momento, siguiendo reglas simples"), ("notas permitidas", "conjunto de notas que se eligen para improvisar"), ("pulso estable", "latido parejo sobre el que se improvisa"), ("idea corta", "grupo pequeño de notas que se repite y se varía"), ("final", "nota donde la improvisación termina; aquí, la nota 1")],
    [
        ("Revisar las reglas", "Regla: usar solo 1, 2, 3, 5 y 6, y terminar en 1. ¿Cumple la improvisación 3-5-6-5-3-2-3-1?", ["Notas usadas: 3, 5, 6, 2 y 1.", "Todas están permitidas.", "Termina en 1."], "Sí cumple"),
        ("Descubrir la nota fuera", "¿Cumple la regla la improvisación 2-3-4-5-3-1? Si no, ¿qué nota está fuera?", ["Reviso cada nota con la lista 1, 2, 3, 5, 6.", "El 4 no está permitido."], "No cumple: el 4 está fuera"),
    ],
    [
        ("Pensar que improvisar es tocar cualquier cosa sin reglas.", "Se improvisa dentro de un conjunto de notas y de una forma, y eso da seguridad.", "Elige las notas permitidas antes de empezar."),
        ("Parar cuando se toca una nota que no estaba permitida.", "Parar rompe el pulso; lo mejor es seguir y volver al conjunto en la siguiente nota.", "Mantén el pulso y corrige después."),
    ],
    [
        ex("¿La nota 4 está entre las permitidas de la clase (1, 2, 3, 5 y 6)? Responde sí o no.", "No", "La lista permitida no incluye el 4."),
        ex("Improvisar, ¿es crear la música en el momento o leerla de una partitura?", "Crearla en el momento", "Esa es la definición."),
        ex("¿Cuántas notas permitidas hay en el conjunto de la clase?", "5", "Son 1, 2, 3, 5 y 6."),
    ],
    [
        ex("¿Cumple la regla «usar solo 1, 2, 3, 5 y 6» la melodía 1-3-5-6-5-3-2-1? Responde sí o no.", "Sí", "Todos los números están en el conjunto."),
        ex("¿Cuántas notas distintas usa la melodía 3-5-3-5-6-5-3-1?", "4", "Las distintas son 3, 5, 6 y 1."),
        ex("¿Cuántas veces aparece la nota 5 en la melodía 5-6-5-3-2-3-1?", "2", "El 5 está en la primera y en la tercera posición."),
    ],
    [
        ex("La regla pide 8 notas, empezar en 3 y terminar en 1. ¿Qué melodía la cumple: A) 3-6-5-3-2-3-5-1 o B) 3-6-5-4-2-3-5-1?", "A", "La B usa el 4, que no está permitido."),
        arith("Improvisas 4 compases de 4 pulsos a 80 pulsos por minuto. ¿Cuántos segundos dura tu improvisación?", "4*4*60//80", "Hay 16 pulsos que, a 80 por minuto, duran 12 segundos.", " segundos"),
        ex("Tu idea corta es 3-5-3-2. ¿Qué variación respeta las notas permitidas y cambia solo la última nota: A) 3-5-3-1 o B) 3-5-3-4?", "A", "La opción B usa el 4, que no está permitido."),
    ],
    [
        ex("Pedro dice que improvisar significa tocar sin ninguna regla. ¿Tiene razón? Responde sí o no.", "No", "Se improvisa dentro de notas permitidas y reglas de forma."),
        ex("De las notas 1 a 7, ¿qué dos no pertenecen al conjunto permitido?", "El 4 y el 7", "El conjunto es 1, 2, 3, 5 y 6."),
    ],
    [
        arith("Con las 5 notas permitidas, ¿cuántas parejas de dos notas se pueden formar si cada nota puede repetirse y se cuenta el orden?", "5*5", "Hay 5 opciones para la primera nota y 5 para la segunda.", " parejas"),
        ex("Una improvisación tiene 8 notas y sus dos últimas son 2 y 1. ¿Cumple la regla de terminar en 1? Responde sí o no.", "Sí", "La última nota es 1."),
    ],
    [ex("Un compañero improvisa 2-3-5-6-5-3-2-1. ¿Cumple las tres reglas de la clase: notas permitidas, 8 notas y final en 1? Responde sí o no.", "Sí", "Usa 2, 3, 5, 6 y 1, tiene 8 notas y termina en 1.")],
    [ex("¿En qué nota termina la improvisación de la clase?", "En la nota 1", "Es la regla del final."), ex("¿Qué se hace si una nota sale fuera del conjunto?", "Se sigue con el pulso y se vuelve al conjunto", "No se interrumpe la música."), ex("¿Está obligada una persona a improvisar frente al curso?", "No", "Puede hacerlo en parejas, en grupo pequeño o en privado.")],
    (
        "Improvisa tres veces una melodía de 8 notas con las notas permitidas (1, 2, 3, 5 y 6), cantando con «la» o tocando, a volumen bajo y con un pulso marcado con el pie. Escribe cada versión con números. En cada una revisa: ¿usa solo notas permitidas?, ¿tiene 8 notas?, ¿termina en 1? Marca con una tabla de sí o no y elige tu versión favorita.",
        "Versión 1: 3-5-6-5-3-2-3-1 (sí, sí, sí). Versión 2: 5-5-6-3-2-3-2-1 (sí, sí, sí). Versión 3: 3-3-5-6-5-3-2-1 (sí, sí, sí). Me gustó la 3 porque repite el 3-3 y termina bajando.",
        ["usa solo notas permitidas", "tiene 8 notas y termina en 1", "registra las tres versiones"],
        ["tres melodías escritas", "tabla de revisión"],
        ["usar el 4 o el 7", "no terminar en 1"],
        "Reconoce las versiones y pide cantar la favorita explicando qué idea se repite.",
    ),
    "Improvisa una melodía de 4 notas con las notas permitidas y escríbela con números.",
    "Improvisa una melodía de 8 notas que repita una idea corta dos veces con una variación.",
)

# ---------------------------------------------------------------- OA 05 · clase 2 (ambientación sonora libre)
TXT = "Primero hay calma. De pronto sopla el viento entre los árboles. Luego cae una lluvia fina y al final sale el sol."

L(
    OA5, 2,
    f"Lápiz y papel. Texto de la clase (inventado): «{TXT}». Sonidos con el cuerpo, la voz y objetos cotidianos seguros (hoja de papel, caja de cartón, cuchara de madera), siempre a volumen bajo. Nada de vidrio, fuego ni objetos pequeños.",
    "Aprenderé a crear una ambientación sonora libre: elegir sonidos, ubicarlos en el tiempo y ordenarlos por planos. Sirve para dar clima de lugar y de emoción a una escena, un cuento o un poema.",
    ["Sé producir sonidos con mi cuerpo y mi voz.", "Sé que hay sonidos fuertes y suaves.", "Sé medir tiempo en segundos."],
    [
        "Una ambientación sonora es una creación hecha con sonidos que dan clima a una escena, sin necesidad de melodías. Es libre porque no usa notas fijas: se pueden usar sonidos del cuerpo (palmas, respiración, pasos suaves), de la voz (susurros, silbidos) y de objetos cotidianos seguros, como frotar papel para imitar el viento. El primer paso es leer la escena y decidir qué sonido da clima a cada momento.",
        "Después se ordenan los sonidos en el tiempo con un esquema escrito, que se llama partitura gráfica o guion sonoro. Se anota cuándo empieza y termina cada sonido, en segundos. También se piensa en los planos: el fondo es un sonido suave y continuo, como la lluvia fina, y el primer plano es un sonido que se destaca, como un trueno. Si todo suena a la vez y fuerte, no se distingue nada; la ambientación necesita contraste y silencios.",
        "Por último se ensaya, se escucha y se ajusta. Se cuida que los sonidos no tapen la voz de quien lee el texto y que el volumen sea seguro. La ambientación puede hacerse solo o en grupo, repartiendo sonidos entre las personas. Cada persona decide qué sonido aporta, y quien prefiere no actuar frente al curso puede cuidar el tiempo, dirigir las entradas o preparar el guion.",
    ],
    [("ambientación sonora", "creación con sonidos que da clima a una escena"), ("guion sonoro", "esquema que anota qué sonido suena y en qué segundos"), ("plano de fondo", "sonido suave y continuo que acompaña"), ("primer plano", "sonido que se destaca sobre los demás"), ("clima", "ambiente o emoción que transmite una escena")],
    [
        ("Leer un guion sonoro", "Guion: 0–10 s lluvia suave con los dedos; 10–20 s lluvia más viento con papel; 20–30 s solo lluvia. ¿Cuántos sonidos suenan a la vez entre los 10 y los 20 segundos?", ["En ese tramo está la lluvia.", "También está el viento de papel.", "Son 2 sonidos."], "2 sonidos"),
        ("Dividir una escena", "Una escena de 60 segundos se reparte en 4 momentos de igual duración. ¿Cuántos segundos dura cada momento?", ["Se reparte el tiempo en partes iguales.", "60 ÷ 4 = 15."], "15 segundos"),
    ],
    [
        ("Hacer sonar todo a la vez y muy fuerte.", "Cuando todo suena junto no se distingue nada, y la ambientación pierde sentido.", "Alterna sonidos, usa silencios y define un fondo y un primer plano."),
        ("Tapar la voz de quien lee con la ambientación.", "La ambientación acompaña el texto; si lo tapa, no cumple su función.", "Baja el volumen y ajusta en el ensayo."),
    ],
    [
        ex("La lluvia fina, que dura mucho rato y suena suave debajo de todo, ¿es plano de fondo o primer plano?", "Plano de fondo", "Es continua y suave."),
        ex("Un trueno que suena una vez y se destaca, ¿es plano de fondo o primer plano?", "Primer plano", "Se destaca sobre el resto."),
        ex("Frotar suavemente una hoja de papel para imitar el viento, ¿suena fuerte o suave?", "Suave", "Frotar suave produce un sonido suave."),
    ],
    [
        ex("Guion: 0–10 s lluvia suave; 10–20 s lluvia más viento; 20–30 s solo lluvia. ¿Qué sonido dura todo el tiempo?", "La lluvia", "Aparece en los tres tramos."),
        ex("En ese mismo guion, ¿cuántos segundos dura el viento?", "10", "Solo suena entre los segundos 10 y 20."),
        ex(f"El texto «{TXT}» tiene cuatro momentos: calma, viento, lluvia y sol. ¿Cuántos sonidos distintos necesitas como mínimo si cada momento tiene el suyo y la calma es silencio?", "3", "Viento, lluvia y sol; la calma es silencio."),
    ],
    [
        ex("Guion: 0–15 s mar suave; 15–30 s mar y gaviotas con la voz aguda; 30–45 s mar fuerte; 45–60 s mar suave. ¿En qué segundo empieza el momento más fuerte?", "En el segundo 30", "El mar fuerte empieza en el 30."),
        ex("En ese guion del mar, ¿cuántos segundos suenan las gaviotas?", "15", "Van del segundo 15 al 30."),
        ex("Quieres que se oiga la voz de quien lee el texto. ¿Qué conviene hacer: bajar el volumen de los sonidos o pedir a quien lee que hable gritando?", "Bajar el volumen de los sonidos", "La ambientación acompaña al texto, y gritar cansa la voz."),
    ],
    [
        ex("Beto dice que, mientras más sonidos suenan a la vez, mejor es una ambientación. ¿Tiene razón? Responde sí o no.", "No", "Demasiados sonidos juntos tapan unos a otros y no se distingue nada."),
        ex("El trueno de tu ambientación tapa la voz que lee el cuento. ¿Qué haces: bajar el volumen del trueno o dejarlo igual y pedir a quien lee que hable más fuerte?", "Bajar el volumen del trueno", "La voz de la lectura debe oírse y la ambientación es la que se ajusta."),
    ],
    [
        ex("Escena de 40 s. Sonido A suena de 0 a 40 s, sonido B de 10 a 25 s y sonido C de 20 a 35 s. ¿Entre qué segundos suenan los tres a la vez?", "Entre los 20 y los 25 segundos", "Es el tramo que comparten A, B y C."),
        arith("En esa escena de 40 s (A de 0 a 40, B de 10 a 25, C de 20 a 35), ¿cuántos segundos suena solamente A?", "10+5", "A suena solo de 0 a 10 s y de 35 a 40 s.", " segundos"),
    ],
    [ex(f"Vas a ambientar el texto «{TXT}». ¿Cuántos momentos distintos tiene que tu ambientación diferencie?", "4", "Calma, viento, lluvia y sol.")],
    [ex("¿Cómo se llama el esquema que anota qué sonido suena y cuándo?", "Guion sonoro", "Organiza los sonidos en el tiempo."), ex("¿Qué plano es suave y continuo?", "El fondo", "Acompaña sin destacarse."), ex("¿Con qué se hacen los sonidos de una ambientación libre?", "Con el cuerpo, la voz y objetos seguros", "No usa notas fijas.")],
    (
        f"Ambienta el texto «{TXT}» con un guion sonoro de 40 segundos: elige un sonido (del cuerpo, de la voz o de un objeto seguro) para cada momento, escribe en segundos cuándo suena cada uno, di cuál es plano de fondo y cuál primer plano y qué dinámica usas (suave o fuerte). Ensaya a volumen bajo y escribe qué ajustarías.",
        "0–10 s: calma, silencio y respiración suave. 10–20 s: viento, papel frotado suave (fondo). 20–32 s: lluvia fina, dedos sobre una caja de cartón (fondo) y una gota con la voz (primer plano). 32–40 s: sol, silbido suave que sube (primer plano). Ajuste: bajar el papel para que se oiga el texto.",
        ["asigna un sonido a cada momento", "indica los segundos de cada sonido", "distingue fondo y primer plano"],
        ["guion sonoro escrito", "ensayo"],
        ["sonidos fuertes que tapan el texto", "no usar silencios"],
        "Reconoce el guion y pide mostrar con el dedo qué sonido es fondo y cuál primer plano en cada tramo.",
    ),
    "Haz tres sonidos suaves con el cuerpo y nómbralos.",
    "Crea un guion sonoro de 30 segundos para una escena de feria y marca fondo y primer plano.",
)

# ---------------------------------------------------------------- OA 05 · clase 3 (acompañamiento rítmico)
L(
    OA5, 3,
    f"Lápiz y papel. Duraciones de la clase: {LEY}. Un compás de 4/4 tiene 16 unidades. Todos los patrones están escritos en los ejercicios; se palmean a volumen bajo.",
    "Aprenderé a crear un acompañamiento rítmico: un patrón que se repite y apoya la melodía sin taparla. Sirve para dar base y movimiento a una canción o a una improvisación.",
    ["Sé medir figuras en unidades.", "Sé que el ostinato es un patrón que se repite.", "Sé sumar y multiplicar números pequeños."],
    [
        "Un acompañamiento rítmico es un patrón de sonidos y silencios que se repite debajo de una melodía y da base y movimiento. Suele ser un ostinato, de uno o dos compases. El acompañamiento más simple marca el pulso con negras. Otro más movido usa corcheas para llenar el espacio entre pulsos. Hay también patrones que mezclan figuras, por ejemplo negra, corchea, corchea, negra, negra.",
        "Para que el acompañamiento funcione debe llenar justo el compás. En 4/4 el patrón suma 16 unidades. Por ejemplo, negra, corchea, corchea, negra, negra suma 4 + 2 + 2 + 4 + 4 = 16 y llena el compás; si sumara 20, se pasaría. También debe ser distinto de la melodía para dar contraste: si la melodía va en notas largas, el acompañamiento puede moverse en notas cortas, y al revés. Y debe sonar más suave para no tapar la melodía.",
        "Se crea un acompañamiento eligiendo primero el compás, luego un patrón que sume lo que corresponde, y probándolo con la melodía. Se escucha si ambas se oyen y si el pulso se mantiene claro. Se puede tocar con las palmas, con un objeto seguro o con la voz diciendo sílabas. Si funciona, se repite a lo largo de la pieza y se puede variar solo en el final.",
    ],
    [("acompañamiento rítmico", "patrón rítmico repetido que apoya la melodía"), ("ostinato", "patrón corto que se repite sin parar"), ("contraste rítmico", "que la melodía y el acompañamiento no se muevan igual"), ("unidad", "duración de una semicorchea, que sirve para medir"), ("pulso", "latido parejo, que marca la negra")],
    [
        ("Comprobar que llena el compás", "¿El patrón corchea, corchea, negra, blanca llena justo un compás de 4/4?", ["Corchea 2, corchea 2, negra 4, blanca 8.", "Suman 2 + 2 + 4 + 8 = 16."], "Sí, suma 16 unidades"),
        ("Elegir el contraste", "La melodía va en blancas (notas largas). ¿Qué acompañamiento da más contraste: corcheas o blancas?", ["Si ambos fueran blancas, se moverían igual.", "Las corcheas se mueven más rápido, y dan contraste."], "Corcheas"),
    ],
    [
        ("Crear un acompañamiento que no suma lo que debe.", "Si el patrón se pasa o le falta, el pulso se desordena en cada repetición.", "Suma las unidades de todas las figuras y silencios."),
        ("Tocar el acompañamiento tan fuerte como la melodía.", "Entonces la melodía no se distingue.", "Toca el acompañamiento más suave."),
    ],
    [
        ex("En la medida de la clase, ¿cuántas unidades suma un compás de 4/4 al crear un acompañamiento?", "16", "Son 4 pulsos de 4 unidades cada uno."),
        ex("¿Qué patrón marca solo el pulso en un compás de 4/4: negra, negra, negra, negra o blanca, blanca?", "Negra, negra, negra, negra", "Una negra por pulso."),
        ex("Un acompañamiento que se repite sin parar debajo de la melodía, ¿se llama ostinato o improvisación?", "Ostinato", "Es la definición de la clase."),
    ],
    [
        ex("¿Llena un compás de 4/4 el patrón blanca, negra, negra? Responde sí o no.", "Sí", "8 + 4 + 4 = 16."),
        ex("La melodía va en notas largas. ¿El acompañamiento da más contraste con notas cortas o con notas largas?", "Con notas cortas", "El contraste exige que se muevan distinto."),
        ex("¿Cuántas corcheas caben en una blanca?", "4", "Una blanca dura 8 unidades y cada corchea 2."),
    ],
    [
        arith("Un ostinato de 2 compases se repite 6 veces. ¿Cuántos compases dura el acompañamiento?", "2*6", "Se multiplican los compases de cada vuelta por las repeticiones.", " compases"),
        arith("Un patrón de 4/4 tiene cuatro corcheas y una blanca. ¿Cuántas unidades suma?", "4*2+8", "Las corcheas suman 8 y la blanca 8.", " unidades"),
        ex("En un compás de 3/4 (12 unidades) hay una blanca. ¿Qué figura falta para llenarlo: una negra o una corchea?", "Una negra", "Faltan 12 − 8 = 4 unidades, o sea una negra."),
    ],
    [
        ex("Ana crea un acompañamiento de 20 unidades para un compás de 4/4. ¿Qué pasa con el patrón?", "Se pasa por 4 unidades", "El compás tiene 16 unidades."),
        ex("Una melodía va en blancas y un acompañamiento va en semicorcheas. ¿Cuántas semicorcheas del acompañamiento suenan durante cada blanca de la melodía?", "8", "Una blanca dura 8 unidades y una semicorchea 1."),
    ],
    [
        ex("Patrón A: negra, negra, negra, negra. Patrón B: negra, corchea, corchea, negra, negra. ¿Cuántos sonidos tiene el patrón B?", "5", "Son una negra, dos corcheas y dos negras."),
        ex("Patrón A: cuatro negras. Patrón B: negra, corchea, corchea, negra, negra. Las unidades del compás se numeran del 0 al 15 y el primer sonido cae en la 0. Los dos patrones tienen sonidos en las unidades 0, 4, 8 y 12, pero B tiene uno más. ¿En qué unidad cae el sonido extra de B?", "En la unidad 6", "Los ataques de B caen en 0, 4, 6, 8 y 12; el extra es el de la 6."),
    ],
    [arith("Un grupo tiene tres capas en un compás de 4/4: pulso en negras (4 sonidos), un ostinato en corcheas (8 sonidos) y una melodía en blancas (2 sonidos). ¿Cuántos sonidos suenan en total en el compás?", "4+8+2", "Se suman los sonidos de las tres capas.", " sonidos")],
    [ex("¿Cuántos pulsos marca un patrón de cuatro negras?", "4", "Una negra por pulso."), ex("¿Qué debe hacer el acompañamiento respecto del volumen de la melodía?", "Sonar más suave", "Así no la tapa."), ex("¿Qué debe sumar el patrón en un compás de 4/4?", "16 unidades", "Debe llenar el compás.")],
    (
        "Crea un acompañamiento rítmico de 1 compás de 4/4 para esta melodía inventada: blanca (nota 3), blanca (nota 5). Elige un patrón de al menos tres figuras distintas con una suma de 16 unidades (usa las duraciones de la clase), escribe la suma y palméalo 4 veces a volumen bajo mientras alguien canta o tú tarareas la melodía en voz baja. Explica qué contraste logra con la melodía.",
        "Patrón: corchea, corchea, negra, blanca = 2 + 2 + 4 + 8 = 16, con tres figuras distintas. Lo palmeé 4 veces. La melodía va en blancas y el acompañamiento tiene corcheas y negras, que se mueven más, por eso hay contraste.",
        ["el patrón suma 16", "usa tres o más figuras distintas", "explica el contraste"],
        ["patrón escrito", "suma de unidades"],
        ["pasarse o no llegar a 16", "tocar el acompañamiento más fuerte que la melodía"],
        "Reconoce el patrón y pide palmearlo lento mostrando dónde cae cada pulso.",
    ),
    "Palmea cuatro veces el patrón negra, negra, negra, negra a volumen bajo.",
    "Crea un acompañamiento de 2 compases de 3/4 que use un silencio y compruébalo con una suma de unidades.",
)

# ---------------------------------------------------------------- OA 05 · clase 4 (acompañamiento melódico y armónico simple)
L(
    OA5, 4,
    f"Lápiz y papel. Escala de números: {NOTAS}. Acordes de la clase: I = 1-3-5 (cifrado C); IV = 4-6-8 (F); V = 5-7-2 (G). Todo está escrito en los ejercicios; si tienes un teclado o una guitarra, puedes comprobarlo, pero no es necesario.",
    "Aprenderé a acompañar una melodía con un bordón (una nota sostenida) y con acordes simples, eligiendo en cada compás el acorde que contiene la mayoría de las notas. Sirve para crear una base armónica sencilla.",
    ["Sé que los acordes I, IV y V tienen tres notas cada uno.", "Sé leer números de nota en una melodía.", "Sé contar elementos de una lista."],
    [
        "Un acompañamiento puede ser rítmico, melódico o armónico. El acompañamiento melódico agrega otra línea, por ejemplo un bordón: una nota larga y repetida que suena debajo. El acompañamiento armónico usa acordes. Con los tres acordes de la clase, I = 1-3-5, IV = 4-6-8 y V = 5-7-2, se puede acompañar una gran cantidad de melodías. Los acordes pueden tocarse todos a la vez o nota por nota.",
        "Para elegir el acorde de cada compás se miran las notas de la melodía. Se cuenta cuántas de ellas pertenecen a cada acorde y se elige el que contiene más. Por ejemplo, si el compás tiene las notas 6, 6, 4 y 8, el acorde IV las contiene a las cuatro. Si hay un empate, se prefiere el acorde que da la sensación que busca: I para reposo, V para tensión.",
        "El bordón se elige entre las notas que comparten varios acordes. La nota 5, por ejemplo, está en el acorde I y en el acorde V, de modo que sirve de base en ambos. Una buena práctica es probar la melodía con el acompañamiento más suave, comprobar que la melodía se distingue y que el acorde elegido encaja. Si algo suena raro, se prueba el otro acorde que contenga más notas.",
    ],
    [("acompañamiento armónico", "acompañar con acordes"), ("bordón", "nota larga que se repite debajo de la melodía"), ("acorde que encaja", "acorde que contiene la mayoría de las notas del compás"), ("cifrado", "escritura de acordes con letras, como C, F y G"), ("progresión", "orden de los acordes de una pieza")],
    [
        ("Elegir el acorde", "Un compás de la melodía tiene las notas 6, 8, 8, 4. ¿Qué acorde de la clase lo acompaña?", ["I = 1-3-5 no tiene ni 6 ni 4.", "IV = 4-6-8 tiene las cuatro notas.", "V = 5-7-2 no tiene ninguna."], "El acorde IV (cifrado F)"),
        ("Contar coincidencias", "El compás tiene las notas 1, 1, 3, 2. ¿Cuántas de ellas pertenecen al acorde I (1-3-5)?", ["El 1 está en I, dos veces.", "El 3 está en I.", "El 2 no está en I."], "3 notas"),
    ],
    [
        ("Elegir el acorde por el nombre de la primera nota solamente.", "Una sola nota no basta: hay que mirar todas las notas del compás.", "Cuenta cuántas notas de cada compás están en cada acorde."),
        ("Tocar el acompañamiento más fuerte que la melodía.", "Entonces la melodía no se distingue.", "Baja el volumen del acompañamiento."),
    ],
    [
        ex("Un bordón, ¿es una nota larga que se repite debajo o una melodía rápida arriba?", "Una nota larga que se repite debajo", "Esa es su definición."),
        ex("¿Qué acorde contiene las notas 4 y 6?", "El acorde IV", "IV = 4-6-8."),
        ex("¿Qué acorde contiene las notas 7 y 2?", "El acorde V", "V = 5-7-2."),
    ],
    [
        ex("Un compás tiene las notas 4, 4, 6, 6. ¿Qué acorde lo acompaña mejor?", "El acorde IV", "Contiene las cuatro notas."),
        ex("Un compás tiene las notas 7, 7, 2, 2. ¿Qué acorde lo acompaña mejor?", "El acorde V", "Contiene las cuatro notas."),
        ex("Un compás tiene las notas 1, 3, 5, 3. ¿Cuál es el cifrado del acorde que lo acompaña?", "C", "El acorde I se escribe C."),
    ],
    [
        ex("Un compás tiene las notas 3, 3, 2, 1. ¿Qué acorde de la clase contiene la mayoría de sus notas?", "El acorde I", "Contiene tres de las cuatro notas (3, 3 y 1)."),
        ex("Escribe en cifrado la progresión I – IV – V – I.", "C – F – G – C", "I = C, IV = F y V = G."),
        arith("Cada acorde dura un compás de 4 pulsos y la progresión de 4 acordes se repite 3 veces. ¿Cuántos pulsos dura el acompañamiento?", "4*4*3", "Cada vuelta tiene 16 pulsos.", " pulsos"),
    ],
    [
        ex("¿Con cuáles de los tres acordes de la clase comparte la nota 5 un bordón: con I y V, con IV y V o con I y IV?", "Con I y V", "El 5 está en 1-3-5 y en 5-7-2."),
        ex("Carla acompaña un compás con las notas 7, 7, 2, 2 usando el acorde I (1-3-5). ¿Cuántas notas de la melodía están en ese acorde?", "0", "Ni el 7 ni el 2 están en 1-3-5."),
    ],
    [
        ex("El compás 3-3-2-1 se acompaña con el acorde V (5-7-2) en vez del I. ¿Cuántas notas de la melodía coinciden con el acorde V?", "1", "Solo la nota 2 pertenece al acorde V."),
        arith("Una melodía de 8 compases de 4 pulsos va a 120 pulsos por minuto. ¿Cuántos segundos dura?", "8*4*60//120", "Hay 32 pulsos y cada uno dura medio segundo.", " segundos"),
    ],
    [ex("El primer compás de tu melodía es 5-5-3-1. ¿Qué acorde de la clase lo acompaña: I, IV o V?", "I", "Las cuatro notas están en 1-3-5.")],
    [ex("¿Qué es un bordón?", "Una nota larga que se repite debajo de la melodía", "Es un acompañamiento melódico simple."), ex("¿Cómo se elige el acorde de un compás?", "Con el que contiene más notas de ese compás", "Es el criterio de la clase."), ex("¿Qué letra escribe el acorde V en el cifrado de la clase?", "G", "V = G.")],
    (
        "Acompaña esta melodía inventada de cuatro compases: compás 1: 3-3-2-1; compás 2: 4-4-6-6; compás 3: 7-7-2-2; compás 4: 1-3-5-3. Para cada compás elige uno de los acordes I, IV o V (cuenta cuántas notas del compás contiene cada uno), escribe los números del acorde y su cifrado y marca un bordón posible con la nota 5. Si tienes un teclado o una guitarra, tócalos suave bajo la melodía.",
        "Compás 1: I (C) con 3 coincidencias. Compás 2: IV (F) con 4. Compás 3: V (G) con 4. Compás 4: I (C) con 4. Progresión: C – F – G – C. Bordón en 5: comparte I y V, pero no está en IV; por eso se usa solo en compases 1, 3 y 4.",
        ["elige un acorde por compás con criterio", "escribe los números y el cifrado", "propone un bordón y dice dónde sirve"],
        ["progresión escrita", "explicación del bordón"],
        ["elegir solo por la primera nota", "usar el bordón con un acorde que no contiene esa nota sin avisarlo"],
        "Reconoce la progresión y pide contar, compás por compás, cuántas notas coinciden con el acorde elegido.",
    ),
    "Escribe los números de los tres acordes de la clase sin mirar.",
    "Elige una melodía de 4 compases tuya y acompáñala con acordes y un bordón.",
)

# ---------------------------------------------------------------- OA 05 · clase 5 (ensayar y ajustar una creación)
L(
    OA5, 5,
    "Lápiz y papel. Los criterios y las versiones están escritos en los ejercicios. Criterios de la clase (0 a 2 puntos cada uno): claridad de la idea, variedad, equilibrio entre melodía y acompañamiento, y cierre.",
    "Aprenderé a mejorar una creación musical con criterios: escuchar, puntuar cada criterio, decidir un cambio y volver a escuchar. Sirve para que mis improvisaciones y creaciones sean cada vez más claras y variadas.",
    ["Sé improvisar con notas permitidas.", "Sé crear un acompañamiento sencillo.", "Sé sumar y restar números pequeños."],
    [
        "Una creación mejora cuando se escucha con criterios claros. Los de esta clase son cuatro y cada uno vale de 0 a 2 puntos. La claridad pregunta si se reconoce la idea principal. La variedad pregunta si hay contraste o cambios que mantengan el interés. El equilibrio pregunta si el acompañamiento deja oír la melodía. El cierre pregunta si la pieza termina de manera que se siente final, por ejemplo en la nota 1. El máximo posible es 8 puntos.",
        "El ciclo es: crear una versión, escucharla, puntuar los cuatro criterios, elegir el criterio más bajo y cambiar solo una cosa para mejorarlo. Después se crea la nueva versión y se vuelve a puntuar. Cambiar muchas cosas juntas hace perder el rastro de qué ayudó. Una versión puede empeorar un criterio al mejorar otro; por eso se miran los cuatro y se decide con calma.",
        "Las devoluciones de otras personas ayudan si hablan de lo que se oye y proponen algo. Decir «en el compás 3 no se oye el final porque el acompañamiento sigue fuerte» sirve; decir «está malo» no sirve. Para registrar el progreso se anotan los puntajes de cada versión y se mira la tendencia. Todas y todos pueden mejorar su creación; el objetivo es avanzar, no compararse con quienes ya tienen más práctica.",
    ],
    [("criterio", "aspecto que se usa para juzgar una creación"), ("claridad", "que se reconozca la idea principal"), ("variedad", "que haya contraste y cambios"), ("cierre", "que la pieza termine con sensación de final"), ("devolución", "comentario que ayuda a mejorar, basado en lo que se oye")],
    [
        ("Sumar el puntaje", "Una versión obtiene claridad 2, variedad 1, equilibrio 2 y cierre 0. ¿Cuántos puntos suma de 8?", ["2 + 1 = 3.", "3 + 2 = 5.", "5 + 0 = 5."], "5 puntos"),
        ("Elegir qué mejorar", "Con esos puntajes, ¿qué criterio conviene mejorar primero?", ["Comparo los cuatro puntajes.", "El más bajo es el cierre, con 0."], "El cierre"),
    ],
    [
        ("Cambiar todo en la siguiente versión.", "Si se cambia todo, no se sabe qué mejoró y qué empeoró.", "Cambia una sola cosa y vuelve a puntuar."),
        ("Dar un comentario como «está malo».", "No dice qué se oye ni cómo mejorar.", "Describe lo que se oye y propón un cambio."),
    ],
    [
        ex("Después de crear una versión, ¿qué se hace: escucharla y puntuar los criterios o decir que está perfecta?", "Escucharla y puntuar los criterios", "Sin escuchar no se sabe qué mejorar."),
        ex("¿Qué criterio revisa que el acompañamiento no tape la melodía?", "El equilibrio", "Por eso se llama equilibrio entre melodía y acompañamiento."),
        ex("¿Cuántos criterios tiene la lista de la clase?", "4", "Claridad, variedad, equilibrio y cierre."),
    ],
    [
        ex("Versión 1: 3-3-3-3-3-3-3-1. ¿Qué criterio falla más: la variedad o el cierre?", "La variedad", "Casi todas las notas son la misma, sin cambios; en cambio, termina en 1."),
        ex("Versión 2: 3-3-5-3-2-3-1-1. ¿Cumple el cierre, si el cierre pide terminar en la nota 1? Responde sí o no.", "Sí", "Termina en 1."),
        ex("¿Cuántas notas distintas usa la versión 2 (3-3-5-3-2-3-1-1)?", "4", "Las distintas son 3, 5, 2 y 1."),
    ],
    [
        ex("Una meta es llegar a 6 puntos de 8. Una versión tiene 5. ¿Cuántos puntos le faltan?", "1", "6 − 5 = 1."),
        ex("Claridad 1, variedad 2, equilibrio 0 y cierre 2. ¿Qué criterio tiene el puntaje más bajo?", "El equilibrio", "Tiene 0 puntos."),
        ex("Versión 1 sumó 4 puntos, versión 2 sumó 6 y versión 3 sumó 5. ¿Cuál es la mejor versión según el puntaje?", "La versión 2", "Es la de mayor puntaje."),
    ],
    [
        ex("Laura cambia todo en la segunda versión. ¿Es mejor cambiar solo una cosa por vez? Responde sí o no.", "Sí", "Así se sabe qué cambio ayudó."),
        ex("Una versión mejora la variedad pero baja el equilibrio. ¿Es correcto mirar solo la variedad? Responde sí o no.", "No", "Hay que mirar los cuatro criterios antes de decidir."),
    ],
    [
        arith("Los puntajes de cuatro versiones fueron 3, 4, 6 y 7. ¿Cuántos puntos subió el puntaje entre la primera y la última?", "7-3", "Se resta el primero al último.", " puntos"),
        arith("Tienes 20 minutos: 3 versiones de 4 minutos cada una y el resto para decidir cambios. ¿Cuántos minutos quedan para decidir?", "20-3*4", "Las versiones suman 12 minutos.", " minutos"),
    ],
    [ex("Un compañero dice sobre tu creación: A) «Me perdí en el compás 3: no se oye el final» o B) «Esto está horrible». ¿Cuál es una devolución respetuosa y útil?", "A", "Describe lo que se oye y dónde, sin juzgar a la persona.")],
    [ex("¿Cuántos puntos vale como máximo cada criterio?", "2", "Cada criterio va de 0 a 2."), ex("¿Cuántos puntos es el máximo total?", "8", "Cuatro criterios de 2 puntos."), ex("¿Qué se cambia a la vez para mejorar una versión?", "Una sola cosa", "Así se sabe qué ayudó.")],
    (
        "Mejora esta creación inventada. Versión 1: melodía 3-3-3-3-3-3-3-3 con acompañamiento de negras muy fuerte. Puntúala con los cuatro criterios (de 0 a 2) y escribe por qué. Después elige el criterio más bajo, cambia solo una cosa y escribe la versión 2 (puede ser una melodía nueva de 8 notas con las notas permitidas 1, 2, 3, 5 y 6, o un acompañamiento más suave). Puntúa también la versión 2 y compara.",
        "Versión 1: claridad 2 (se reconoce la nota 3), variedad 0 (una sola nota), equilibrio 0 (el acompañamiento tapa), cierre 0 (no termina en 1); suma 2 de 8. Cambio: bajar el acompañamiento y cambiar la melodía a 3-3-5-3-2-3-1-1. Versión 2: claridad 2, variedad 1, equilibrio 2, cierre 2; suma 7 de 8 (en este ejemplo).",
        ["puntúa los cuatro criterios con razones", "cambia una cosa para mejorar el criterio más bajo", "compara los puntajes de las dos versiones"],
        ["puntajes escritos", "versión 2"],
        ["cambiar muchas cosas a la vez", "juzgar sin decir qué se oye"],
        "Reconoce los puntajes y pide explicar qué se oye en cada criterio que bajó o subió.",
    ),
    "Puntúa en voz alta una melodía tuya de 4 notas con los cuatro criterios.",
    "Escribe un plan de tres versiones de una creación, cada una con un cambio distinto, y predice cómo subirá el puntaje.",
)
