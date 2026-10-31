"""Cuaderno del estudiante, 5.º básico Lenguaje y Comunicación: OA 29 (vocabulario nuevo en intervenciones orales)."""
from __future__ import annotations

from student_content_le5_d import E, reg
from student_lessons import arith

OA29 = "LE05 OA 29"

# ================================================================ OA 29 · clase 1
reg(
    OA29, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer en voz alta el texto «El pasillo de noche».",
    "Aprenderé a reconocer una palabra nueva en un texto leído o escuchado, a descubrir su significado con pistas y a prepararla para usarla al hablar. Sirve para expresarme con más precisión.",
    ["Sé buscar información en un texto.", "Sé usar un diccionario o preguntar el significado de una palabra."],
    [
        "El vocabulario es el conjunto de palabras que conocemos. Cuando leemos o escuchamos un texto, a veces aparece una palabra nueva. En vez de saltarla, podemos descubrir su significado. Primero, leemos la oración completa y las oraciones de alrededor, porque suelen dar pistas. Este conjunto de pistas se llama contexto.",
        "Veamos un ejemplo. Texto «El pasillo de noche»: «Teo salió de su pieza de puntillas. Caminó sigiloso por el pasillo para no despertar a su hermana. Al pasar frente a la puerta, contuvo la respiración. Los peldaños de la escalera no crujieron, pues pisó con mucho cuidado». La palabra nueva es «sigiloso». Las pistas son «de puntillas», «para no despertar» y «no crujieron». Juntas muestran que Teo se movía sin hacer ruido.",
        "Después de inferir el significado, lo comprobamos en un diccionario o con una persona. Sigiloso significa que actúa sin hacer ruido para que nadie lo note. Por último, usamos la palabra en una oración propia, para que pase de «palabra que leí» a «palabra que uso». Una palabra aprendida se anota con su significado y una oración de ejemplo.",
    ],
    [("vocabulario", "conjunto de palabras que conocemos"), ("contexto", "oraciones y pistas que rodean una palabra"), ("inferir", "deducir algo a partir de pistas"), ("sigiloso", "que actúa sin hacer ruido para que nadie lo note"), ("sigilo", "silencio con que se hace algo para que nadie lo note")],
    [
        ("Descubrir con pistas", "Texto «El pasillo de noche». Palabra nueva: «sigiloso». Pistas: «de puntillas», «para no despertar a su hermana», «no crujieron». ¿Qué significa?", ["Junto las pistas.", "Todas hablan de no hacer ruido.", "Entonces sigiloso es actuar en silencio."], "Que actúa sin hacer ruido para que nadie lo note."),
        ("Usar la palabra", "¿Cuál oración usa bien «sigiloso»: a) «El gato se acercó sigiloso al pájaro.» b) «El tambor sonó sigiloso en la plaza.»", ["Recuerdo que sigiloso es sin ruido.", "El tambor hace ruido.", "El gato que se acerca sin ruido es la a."], "La a."),
    ],
    [("Saltar la palabra nueva sin intentar entenderla.", "Se piensa que no importa para entender el texto.", "Lee las oraciones cercanas y busca pistas."), ("Aprender el significado y no usarlo nunca.", "Se cree que basta con haberlo leído.", "Escribe una oración propia y úsala al hablar.")],
    [
        E("Según el texto «El pasillo de noche», ¿cómo salió Teo de su pieza?", "De puntillas", "Lo dice la primera oración."),
        E("¿Para qué caminó sigiloso Teo por el pasillo?", "Para no despertar a su hermana", "Está escrito en la segunda oración."),
        E("«Sigiloso» significa: a) sin hacer ruido para no ser notado b) con mucho ruido.", "a", "Es lo que muestran las pistas del texto."),
    ],
    [
        E("¿Qué pistas del texto ayudan a entender «sigiloso»: a) «de puntillas» y «para no despertar a su hermana» b) «pieza» y «escalera»?", "a", "Hablan de no hacer ruido."),
        E("Cuando aparece una palabra nueva, ¿qué es lo primero que conviene hacer: leer la oración completa y buscar pistas o saltarla?", "Leer la oración completa y buscar pistas", "El contexto ayuda a inferir su significado."),
        E("«Sigilo» es silencio con que se hace algo para que nadie lo note. ¿Cuál oración está correcta: a) «Actuó con sigilo para no asustar al bebé.» b) «Actuó con sigilo gritando.»", "a", "Gritar no es coherente con el sigilo."),
    ],
    [
        E("Ordena los pasos para aprender una palabra. a) comprobar en el diccionario b) leer la oración y buscar pistas c) inferir un significado d) usarla en una oración propia. Escribe las letras.", "b, c, a, d", "Primero se buscan pistas, luego se infiere, se comprueba y se usa."),
        E("«Meticuloso» es quien hace las cosas con mucho cuidado, atendiendo a cada detalle. Ema ordenó su caja de lápices por color y tamaño y revisó que ninguno faltara. ¿Qué palabra la describe: meticulosa o sigilosa?", "Meticulosa", "Cuidó cada detalle."),
        E("Elige la oración que usa bien «sigiloso»: a) «La profesora entró sigilosa a la sala donde dormían los bebés.» b) «La profesora entró sigilosa dando portazos.»", "a", "Dar portazos hace ruido."),
    ],
    [
        E("Hugo dice que «sigiloso» significa «veloz». En el texto, Teo va de puntillas y con cuidado. ¿Hugo tiene razón? Responde sí o no.", "No", "Las pistas hablan de no hacer ruido, no de velocidad."),
        E("Dos niños explican «sigiloso». Pía dice: «Es hacer algo en silencio para que no se note». León dice: «Es estar enojado». ¿Quién usa las pistas del texto?", "Pía", "Las pistas del texto hablan de silencio."),
    ],
    [
        E("En «La profesora entró sigilosa a la sala, donde los niños dormían la siesta», ¿qué pista del contexto apoya el significado de «sigilosa»: a) «donde los niños dormían la siesta» b) «La profesora»?", "a", "Explica por qué entró sin ruido."),
        E("Debes explicar «sigiloso» a un niño más pequeño usando el texto de Teo. ¿Qué explicación sirve: a) «Es caminar de puntillas, sin ruido, para que nadie te note.» b) «Es una palabra de un cuento.»", "a", "Se apoya en las pistas y es clara."),
    ],
    [E("Escuchas en una exposición: «El zorro avanzó sigiloso entre los arbustos». ¿Qué imagen te ayuda a recordar el significado: a) un zorro que avanza sin ruido para que nadie lo note b) un zorro que ladra fuerte?", "a", "Coincide con el significado de la palabra.")],
    [
        E("En Lenguaje: ¿Qué es el contexto de una palabra?", "Las oraciones y pistas que la rodean", "Ayuda a deducir su significado."),
        E("¿Conviene comprobar el significado en un diccionario después de inferirlo? Responde sí o no.", "Sí", "Así confirmamos que la idea era correcta."),
        E("¿Una palabra aprendida se anota con su significado y una oración de ejemplo? Responde sí o no.", "Sí", "Ayuda a recordarla y usarla."),
    ],
    ("Lee otra vez «El pasillo de noche» y escribe: 1) las pistas que te ayudan a entender «sigiloso», 2) el significado con tus palabras y 3) una oración propia con «sigiloso» sobre una situación de tu casa o escuela. Léela en voz alta a una persona de tu casa y pregúntale si entendió qué significa la palabra.",
     "1) «de puntillas», «para no despertar a su hermana», «no crujieron». 2) Sigiloso es hacer algo sin ruido para que nadie lo note. 3) «Mi gato camina sigiloso cuando quiere acercarse al pájaro del patio».",
     ["nombra al menos dos pistas del texto", "explica el significado con palabras propias", "la oración propia usa bien la palabra"], ["pistas copiadas", "significado escrito", "oración propia"], ["definir sin mostrar pistas", "usar la palabra en una situación que no corresponde"],
     "Si tu oración suena rara, pregúntate: ¿esa persona o animal actúa sin hacer ruido para que no lo noten?"),
    "Escribe dos pistas de contexto que expliquen la palabra «meticuloso» en una oración tuya.",
    "Busca en un libro de tu casa una palabra que no conozcas, escribe la oración y qué pistas te ayudaron.",
)

# ================================================================ OA 29 · clase 2
reg(
    OA29, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tus oraciones.",
    "Aprenderé a usar una palabra nueva con sentido, concordancia y registro adecuados en una intervención oral. Sirve para que las palabras que aprendo se noten en mi forma de hablar.",
    ["Sé inferir el significado de una palabra con pistas.", "Sé que hay un registro formal y uno informal."],
    [
        "Usar bien una palabra nueva significa que sea pertinente: que encaje con lo que quiero decir. Para eso comprobamos tres cosas. Primero, el sentido: ¿el significado calza con la situación? Segundo, la concordancia: si la palabra es un adjetivo, tiene que coincidir en género y número con el sustantivo (meticulosa, meticulosos). Tercero, el registro: ¿es adecuada para quien me escucha?",
        "Veamos con «meticuloso», que significa que hace las cosas con mucho cuidado, atendiendo a cada detalle. «Mi compañera fue meticulosa: revisó cada dato dos veces» está bien, porque el sentido calza y la concordancia es correcta. «El día fue meticuloso» no tiene sentido, porque un día no hace las cosas con cuidado. «Mis amigas son meticuloso» no concuerda: debería ser «meticulosas».",
        "Al usarla en una intervención oral, conviene dar un contexto que ayude a entenderla. Decimos la palabra y, si la audiencia puede no conocerla, la explicamos con otras palabras: «fue meticulosa, es decir, cuidó cada detalle». Ensayar en voz alta nos ayuda a pronunciarla bien y a usarla con naturalidad.",
    ],
    [("pertinente", "que encaja bien con lo que se quiere decir"), ("concordancia", "coincidencia de género y número entre palabras"), ("meticuloso", "que hace las cosas con mucho cuidado, atendiendo a cada detalle"), ("adjetivo", "palabra que dice cómo es algo o alguien"), ("sentido", "significado que calza con la situación")],
    [
        ("Comprobar sentido", "¿Cuál oración usa bien «meticuloso»: a) «Mi compañera fue meticulosa: revisó cada dato dos veces.» b) «El día fue meticuloso.»", ["Meticuloso es hacer algo con mucho cuidado.", "Un día no hace cosas con cuidado.", "La a calza con el significado."], "La a."),
        ("Comprobar concordancia", "Corrige: «Mis amigas son meticuloso».", ["El sustantivo es «amigas», femenino plural.", "El adjetivo debe coincidir.", "«Meticulosas»."], "«Mis amigas son meticulosas.»"),
    ],
    [("Usar la palabra nueva en una oración donde no calza.", "Se quiere mostrar que se aprendió.", "Comprueba el sentido antes de usarla."), ("No cambiar la terminación del adjetivo.", "Se olvida concordar con el sustantivo.", "Revisa género y número.")],
    [
        E("¿Qué significa «meticuloso»: a) hacer las cosas con mucho cuidado y atención a los detalles b) hacerlas de prisa?", "a", "Es la definición de la palabra."),
        E("¿Cuál es el femenino de «meticuloso»?", "Meticulosa", "Cambia la terminación a -a."),
        E("¿Cuál es el plural de «meticulosa»?", "Meticulosas", "Se agrega -s."),
    ],
    [
        E("¿Cuál oración concuerda bien: a) «Los niños fueron meticulosos.» b) «Los niños fueron meticulosa.»", "a", "«Niños» es masculino plural."),
        E("En «Julia es meticulosa con sus tareas», ¿qué palabra cambia su terminación para concordar con «Julia»: a) meticulosa b) es?", "a", "La terminación -a concuerda con un sustantivo femenino."),
        E("Para explicar «meticuloso» a la audiencia, ¿qué conviene decir: a) «es decir, que cuida cada detalle» b) «no sé qué significa»?", "a", "Una explicación breve ayuda a entender."),
    ],
    [
        E("Completa con la forma correcta: «Las investigadoras fueron muy ______ (meticuloso)».", "Meticulosas", "El sujeto es femenino plural."),
        E("Ordena para formar una oración: a) meticuloso b) Mi amigo c) con su colección de piedras d) es. Escribe las letras.", "b, d, a, c", "La oración es: Mi amigo es meticuloso con su colección de piedras."),
        E("¿Cuál opción conviene si hablas con la directora: a) «Fui meticulosa al revisar los datos.» b) «Fui re meticulosa po.»", "a", "Es una forma más cuidada."),
    ],
    [
        E("Una niña dice: «El silencio fue meticuloso». ¿Por qué no es pertinente: a) porque el silencio no actúa con cuidado b) porque no hay verbo?", "a", "La palabra describe a quien hace algo."),
        E("Dos oraciones: A) «Elena fue meticulosa y revisó tres veces su informe.» B) «Elena fue meticulosa y rompió el informe.» ¿En cuál calza mejor el sentido?", "A", "Revisar tres veces muestra cuidado."),
    ],
    [
        E("Quieres decir que un compañero revisó su trabajo con mucho cuidado. ¿Qué frase es más pertinente: a) «Mi compañero fue meticuloso al revisar su trabajo.» b) «Mi compañero fue sigiloso al revisar su trabajo.»", "a", "Meticuloso se refiere al cuidado; sigiloso, a no hacer ruido."),
        E("¿Qué oración tiene un error de concordancia: a) «Los dibujantes son meticulosos.» b) «Las dibujantes son meticulosos.»", "b", "«Las dibujantes» es femenino plural y el adjetivo debería ser «meticulosas»."),
    ],
    [E("En una exposición, dices: «Mis compañeros fueron meticulosos con sus cuadernos». Un niño no conoce «meticulosos». ¿Qué explicación agregas: a) «es decir, cuidaron cada detalle» b) «es una palabra difícil»?", "a", "Da un significado claro para la audiencia.")],
    [
        E("¿Una palabra pertinente encaja con lo que quiero decir? Responde sí o no.", "Sí", "Debe calzar con el sentido."),
        E("El adjetivo, ¿debe coincidir en género y número con el sustantivo? Responde sí o no.", "Sí", "Eso se llama concordancia."),
        E("¿Conviene ensayar en voz alta una palabra nueva antes de usarla? Responde sí o no.", "Sí", "Ayuda a pronunciarla y usarla con naturalidad."),
    ],
    ("Escribe tres oraciones con «meticuloso» (o su forma femenina o plural): 1) sobre un compañero o compañera en la escuela, 2) sobre una tarea de tu casa, 3) para una exposición formal ante el curso. Cada una debe tener sentido y buena concordancia. Léelas en voz alta y marca con una cruz la que usarías ante la directora.",
     "1) «Mi compañera Ana es meticulosa al pintar sus mapas». 2) «Ordené mis juguetes de manera meticulosa». 3) «Para este trabajo fuimos meticulosos y revisamos cada dato».",
     ["las tres oraciones tienen sentido", "la concordancia es correcta", "una está en registro formal"], ["tres oraciones escritas y dichas"], ["usar la palabra donde no calza", "no concordar el adjetivo"],
     "Si dudas, reemplaza «meticuloso» por «con mucho cuidado»: si la oración sigue con sentido, está bien."),
    "Escribe dos oraciones con «sigiloso» que concuerden bien.",
    "Anota una palabra nueva de esta semana y úsala en tres oraciones distintas.",
)

# ================================================================ OA 29 · clase 3
reg(
    OA29, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer los cuatro textos breves.",
    "Aprenderé a encontrar y seleccionar las pistas de contexto que explican una palabra nueva: definición, contraste, ejemplo y sinónimo. Sirve para entender lo que leo y escucho y usar esas palabras al hablar.",
    ["Sé que el contexto ayuda a inferir un significado.", "Sé usar palabras nuevas con sentido."],
    [
        "En los textos, una palabra nueva suele venir acompañada de pistas. Hay cuatro tipos muy comunes. La definición explica la palabra directamente, a menudo con «es decir». El contraste muestra lo opuesto con «pero», «en cambio» o «mientras». El ejemplo muestra un caso que ilustra la palabra. El sinónimo usa otra palabra de significado parecido, a menudo entre comas o con «o sea».",
        "Veamos cuatro textos. Definición: «La noticia fue efímera, es decir, duró muy poco tiempo». Contraste: «En el pueblo de Lina el agua era escasa; en cambio, en la casa de su tía había agua abundante». Ejemplo: «Clara fue tenaz: intentó seis veces armar la maqueta hasta lograrlo». Sinónimo: «Mateo vaciló un momento, dudando entre el rojo y el azul».",
        "Para seleccionar la evidencia, subrayamos la frase exacta que da la pista y decimos de qué tipo es. Así no adivinamos: respaldamos el significado con el texto. Luego comprobamos que ese significado calce en la oración y lo usamos al hablar.",
    ],
    [("efímero", "que dura muy poco tiempo"), ("escaso", "que hay poco o no alcanza"), ("tenaz", "que no se rinde y sigue intentando"), ("vacilar", "dudar, no decidirse"), ("abundante", "que hay en gran cantidad")],
    [
        ("Encontrar la pista de definición", "Texto: «La noticia fue efímera, es decir, duró muy poco tiempo en los diarios». ¿Qué pista explica «efímera»?", ["Busco una frase que explique directamente.", "«Es decir» introduce una definición.", "Dice «duró muy poco tiempo»."], "«Duró muy poco tiempo» (definición con «es decir»)."),
        ("Encontrar la pista de contraste", "Texto: «En el pueblo de Lina el agua era escasa; en cambio, en la casa de su tía había agua abundante». ¿Qué pista ayuda a entender «escasa»?", ["Busco qué se contrapone.", "«En cambio» señala el opuesto.", "Lo opuesto es «abundante», o sea mucha."], "El contraste con «abundante»: escasa es poca."),
    ],
    [("Elegir un significado sin mostrar la frase que lo respalda.", "Se responde por intuición.", "Subraya la pista exacta del texto."), ("Confundir la palabra nueva con la palabra opuesta.", "No se advierte el conector de contraste.", "Mira «pero», «en cambio» o «mientras».")],
    [
        E("Texto: «Clara fue tenaz: intentó seis veces armar la maqueta hasta lograrlo». ¿Cuántas veces intentó Clara armar la maqueta?", "Seis", "Lo dice el texto."),
        E("«Tenaz» significa: a) que no se rinde b) que se rinde rápido.", "a", "Intentó muchas veces hasta lograrlo."),
        E("Texto: «Mateo vaciló un momento, dudando entre el rojo y el azul». ¿Qué significa «vaciló»?", "Dudó", "El texto da el sinónimo: dudando."),
    ],
    [
        E("¿Qué tipo de pista usa «es decir, duró muy poco tiempo»: definición o ejemplo?", "Definición", "Explica directamente la palabra."),
        E("En «El agua era escasa; en cambio, había agua abundante», ¿qué conector muestra el contraste: a) en cambio b) agua?", "a", "«En cambio» introduce lo contrario."),
        E("En el texto de Clara, ¿qué parte funciona como ejemplo de ser tenaz: a) «intentó seis veces armar la maqueta» b) «Clara»?", "a", "Muestra un caso concreto de no rendirse."),
    ],
    [
        arith("Clara intentó seis veces armar la maqueta y lo logró en el último intento. ¿Cuántas veces falló?", "6-1", "Se resta el intento logrado al total de intentos.", " veces"),
        E("Lee: «Fue una alegría efímera: apareció y se acabó en un minuto». ¿Cuánto duró la alegría?", "Un minuto", "Eso muestra que efímera es de poca duración."),
        E("Ordena para encontrar el significado de «escasa». a) Reviso el conector «en cambio». b) Leo el contraste con «abundante». c) Concluyo que escasa es poca cantidad. Escribe las letras.", "a, b, c", "Se identifica el conector, el opuesto y luego se concluye."),
    ],
    [
        E("Lucas dice que «efímera» significa «larga». ¿Qué pista del texto muestra que se equivoca: a) «duró muy poco tiempo» b) «la noticia»?", "a", "La definición dice lo contrario."),
        E("Si el contraste es «El agua era escasa; en cambio había abundante», ¿qué quiere decir si en la casa de la tía había abundante agua: a) que tenían mucha b) que tenían poca?", "a", "Abundante es lo opuesto a escasa."),
    ],
    [
        E("Lee: «Julián fue tenaz: aunque se cayó dos veces de la bicicleta, volvió a subir». ¿Qué pista muestra que ser tenaz es no rendirse: a) volvió a subir b) se cayó?", "a", "Volver a intentar muestra que no se rindió."),
        E("En «Mientras Tomás vaciló, su prima eligió enseguida», ¿qué significa que Tomás vaciló: a) tardó en decidir b) eligió enseguida?", "a", "Se contrasta con su prima, que eligió enseguida."),
    ],
    [E("Escuchas esta frase de una exposición: «La emoción de los fuegos artificiales es efímera, es decir, dura apenas unos segundos». Para explicarla a un compañero, ¿qué pista usas: a) «dura apenas unos segundos» b) «emoción»?", "a", "Es la definición que explica la palabra.")],
    [
        E("¿Qué palabras suelen introducir una definición: «es decir» o «mientras»?", "Es decir", "Explican lo que significa la palabra."),
        E("¿Un contraste muestra lo opuesto? Responde sí o no.", "Sí", "Ayuda a deducir el significado por oposición."),
        E("¿Hay que subrayar la frase exacta que da la pista? Responde sí o no.", "Sí", "Así se respalda con evidencia."),
    ],
    ("Lee estos dos textos. A) «La fruta de la huerta era abundante: había tantas ciruelas que llenamos tres canastos». B) «Los cupos del taller eran escasos: solo había dos para treinta alumnos». Para cada texto escribe: la frase que da la pista, el tipo de pista (definición, contraste, ejemplo o sinónimo) y el significado de la palabra subrayada. Luego usa «abundante» o «escaso» en una oración oral propia.",
     "A) Pista: «había tantas ciruelas que llenamos tres canastos» (ejemplo): abundante es mucha cantidad. B) Pista: «solo había dos para treinta alumnos» (ejemplo): escaso es poco. Oración: «En la feria había abundante fruta».",
     ["cita la frase que da la pista", "nombra el tipo de pista", "explica el significado con palabras propias"], ["pistas copiadas", "tipos de pista", "oración oral"], ["decir el significado sin citar la pista", "confundir abundante con escaso"],
     "Si dudas del tipo de pista, pregúntate si define, contrasta, ejemplifica o repite con otra palabra."),
    "Escribe un texto breve de dos oraciones que explique «vacilar» con un ejemplo.",
    "Busca un texto breve y subraya una pista de contexto de una palabra nueva.",
)
