"""Música 3.º y 4.º medio FG: OAC-02 (creación musical, emociones e ideas). Fragmentos y patrones de ejemplo, inventados; sin audio real."""
from __future__ import annotations

from fg_musi_common import build

O2 = "FG-MUSI-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (tres fragmentos de ejemplo, inventados). Fragmento 1: 60 pulsos por minuto, notas largas y graves, volumen suave, timbre de cuerdas, sonido en tonalidad menor. "
     "Fragmento 2: 150 pulsos por minuto, notas cortas y agudas, volumen fuerte, percusión marcada, sonido en tonalidad mayor. "
     "Fragmento 3: 90 pulsos por minuto, una melodía que sube de a poco y termina en una nota larga; el volumen va creciendo; hay un silencio justo antes de la última nota.")
build(
    O2, 1, F,
    use="Aprenderé a reconocer cómo los elementos del lenguaje musical (tempo, registro, dinámica, tonalidad, silencio) pueden expresar emociones e ideas, y a no suponer que un rasgo produce siempre la misma emoción.",
    prior=["Reconozco pulso, tempo, timbre y textura.", "Sé qué es una melodía que sube o baja.", "Separo lo que se oye de lo que siento."],
    explain=[
        "Los elementos del lenguaje musical son las herramientas con que se expresa algo. El tempo es la rapidez del pulso; el registro es qué tan grave o agudo suena; la dinámica es el volumen y sus cambios (crescendo es subir de a poco); la tonalidad mayor suele sonar más luminosa y la menor más sombría; la duración es cuánto dura cada sonido; y el silencio también expresa, porque crea espera o tensión. La armonía es el conjunto de sonidos que suenan a la vez (acordes) y acompañan a la melodía; acordes largos y suaves dan un fondo sereno y acordes cortos y fuertes dan un fondo agitado.",
        "Estas relaciones son tendencias, no reglas. Un tempo lento puede expresar calma, pero también tristeza o misterio, y una pieza en tonalidad mayor puede sonar inquieta si lo demás la contradice. La emoción depende de la combinación de rasgos, del contexto y de cada oyente, por eso conviene describir primero lo que se oye y después decir qué sensación produce.",
        "Para crear con una emoción o una idea, conviene elegir primero los rasgos que la apoyen y comprobar con la escucha si el resultado se parece a lo que buscabas. Una misma emoción puede expresarse con recursos muy distintos.",
    ],
    vocab=[("registro", "qué tan grave o agudo suena un sonido"), ("armonía", "sonidos que suenan a la vez (acordes) y acompañan a la melodía"), ("dinámica", "volumen de la música y sus cambios"), ("crescendo", "aumento gradual del volumen"), ("tonalidad mayor y menor", "dos modos que tienden a sonar luminoso y sombrío"), ("duración", "tiempo que dura un sonido"), ("silencio", "ausencia de sonido que también expresa")],
    worked=[
        ("Relacionar rasgos y sensación", "Fragmento de ejemplo: notas largas y graves, volumen suave, 60 pulsos por minuto. Describe lo que se oye y propone una sensación posible.", ["Rasgos: registro grave, notas largas, volumen suave y tempo lento.", "Combinados, suelen dar sensación de calma o de pesadez.", "Es una tendencia: el oyente podría sentir otra cosa."], "Registro grave, notas largas, volumen suave y tempo lento; sensación posible: calma o pesadez"),
        ("Distinguir tendencia y regla", "Un compañero dice: «Todo lo que está en tonalidad menor es triste». ¿Qué le responderías?", ["La menor suele sonar sombría, pero no es una regla.", "Depende del tempo, el timbre y el contexto.", "Una pieza en menor puede sonar enérgica o solemne."], "Es una tendencia, no una regla"),
    ],
    mistakes=[("Afirmar que un rasgo produce siempre la misma emoción.", "La emoción surge de la combinación de rasgos y del contexto del oyente.", "Escribe «suele sonar» o «puede sugerir» y cita los otros rasgos."),
              ("Describir solo la emoción («es triste») sin decir qué se oye.", "No se puede comprobar ni reconstruir la idea de la pieza.", "Primero anota rasgos audibles y luego la sensación.")],
    T=[
        ('=', '{F} En un minuto, ¿cuántos pulsos más suenan en el fragmento 2 que en el fragmento 1?', '150-60', 'Se restan los pulsos por minuto: 150 del fragmento 2 menos 60 del fragmento 1.', ' pulsos'),
        ('abc', '¿Qué es un crescendo?', 'Un aumento gradual del volumen, de más suave a más fuerte', 'Un cambio brusco de tempo', 'Una nota que se repite varias veces', 'Crescendo significa que el volumen sube de a poco.'),
        ('ab', '{F} El fragmento 3 incluye un silencio antes de la última nota. ¿Qué efecto suele producir?', 'Espera o tensión antes del final', 'Que la melodía se acelere', 'Un silencio breve antes de una nota larga suele crear expectativa.'),
        ('abc', '{F} ¿Qué rasgos del fragmento 1 pueden sugerir calma o pesadez?', 'Tempo lento, notas largas, registro grave y volumen suave', 'Tempo rápido, notas cortas y percusión marcada', 'Un crescendo y un silencio antes del final', 'Esos rasgos combinados suelen dar sensación de calma o de pesadez.'),
        ('abc', '{F} ¿Qué fragmento es más probable para una escena de persecución?', 'El fragmento 2, de notas cortas, percusión marcada y 150 pulsos por minuto', 'El fragmento 1, de notas largas y graves', 'El fragmento 3, que sube de a poco', 'Tempo rápido, notas cortas y percusión marcada sugieren movimiento y tensión.'),
        ('abc', 'Una estudiante dice: «La tonalidad mayor siempre expresa alegría». ¿Qué falla?', 'Presenta una tendencia como si fuera una regla que se cumple siempre', 'Confunde la tonalidad con el tempo', 'Cree que la mayor es solo para música rápida', 'La emoción depende de varios rasgos y no solo de la tonalidad.'),
        ('abc', '{F} El fragmento 3 sube de a poco y crece en volumen. ¿Qué idea puede apoyar?', 'Algo que se acerca o que crece en intensidad de a poco', 'Algo que se aleja y desaparece', 'Un momento de total quietud', 'Subida melódica y crescendo sugieren acercamiento o intensificación.'),
        ('abc', 'Dos personas oyen el mismo fragmento: una siente calma y la otra tristeza. ¿Qué se puede concluir?', 'La sensación depende también de cada oyente, no solo del fragmento', 'Una de las dos personas oyó mal el fragmento', 'La sensación depende solo del tempo del fragmento', 'Las emociones que provoca la música varían entre personas.'),
        ('abc', '{F} Quieren expresar «sorpresa» con una variante del fragmento 3. ¿Qué cambio es coherente?', 'Un silencio más largo y una última nota fuerte y corta', 'Bajar el volumen hasta que casi no se oiga', 'Repetir la misma nota larga hasta el final', 'Un silencio prolongado seguido de un contraste fuerte puede sorprender.'),
        ('abc', 'Una pieza lenta, grave y en tonalidad mayor. ¿Qué es lo más razonable decir?', 'Que los rasgos se contradicen y la emoción dependerá de la combinación', 'Que es triste, porque lo lento siempre es triste', 'Que es alegre porque es mayor, sin importar el tempo', 'Cuando los rasgos apuntan a emociones distintas, hay que describir la combinación.'),
        ('abc', '{F} ¿Qué frase describe sin opinar el fragmento 2?', 'Percusión marcada, notas cortas y agudas, a 150 pulsos por minuto', 'Es muy buena porque da ganas de moverse', 'Se nota que quien lo hizo estaba enojado', 'Describir es citar rasgos audibles; las otras frases opinan o suponen intenciones.'),
        ('abc', 'Para componer con la idea de «calma», ¿qué decisión es coherente?', 'Tempo lento, volumen suave y notas largas con pocos cambios', 'Tempo rápido, volumen fuerte y notas cortas', 'Silencios inesperados y golpes fuertes', 'Esos rasgos suelen asociarse a calma, aunque no son reglas.'),
        ('abc', 'Una melodía se canta sola y luego se repite con acordes de teclado debajo. ¿Qué elemento del lenguaje musical se agregó?', 'La armonía, porque ahora suenan varios sonidos a la vez junto con la melodía', 'El tempo, porque la melodía se volvió más rápida', 'El silencio, porque la melodía se detiene entre frases', 'Los acordes que acompañan a la melodía forman la armonía; el tempo y el silencio no cambiaron.'),
    ],
    ctx=('abc', 'Un grupo de estudiantes quiere crear un fragmento que exprese «espera». Prueban notas largas, un tempo lento y un silencio antes de la última nota. ¿Qué deben hacer después?', 'Escuchar y comprobar si la espera se siente, y ajustar', 'Declarar que expresa espera y no probarlo', 'Cambiar todo el fragmento sin escucharlo', 'La emoción se comprueba escuchando, no suponiéndola.'),
    sc=[
        ('¿Qué es la dinámica en música?', 'El volumen y sus cambios', 'Incluye subir de a poco o bajar el volumen.'),
        ('¿Una tonalidad menor siempre expresa tristeza?', 'No, es una tendencia', 'Depende de la combinación de rasgos y del contexto.'),
        ('abc', 'Para expresar una idea con música, ¿qué se hace primero?', 'Elegir rasgos que la apoyen y comprobarlos escuchando', 'Escribir el título de la pieza antes que nada', 'Copiar la música de una película conocida', 'Los rasgos elegidos deben verificarse con la escucha.'),
    ],
    op=("Con la {F} elige la sensación que quieres expresar (calma, alegría, espera o sorpresa) y escribe qué rasgos usarías: tempo, registro, volumen, tonalidad y silencio. Cierra con una frase que diga cómo comprobarás que se parece a lo que querías.",
        "Sensación: espera. Tempo lento (60), registro medio, volumen suave que crece, tonalidad menor y un silencio de 2 pulsos antes del final. Lo comprobaré escuchando y preguntando a un compañero qué sintió.",
        ["elige una sensación", "usa varios rasgos", "plan para comprobar"], ["lista de rasgos y frase de comprobación"], ["usar solo un rasgo", "afirmar que siempre produce lo mismo"],
        "Reconoce los rasgos elegidos y pide cómo comprobará el efecto con otra persona."),
    reinforce="Escucha una canción y anota tres rasgos audibles; después escribe qué sensación pueden sugerir, usando «suele» o «puede».",
    extend="Elige una emoción y propone dos combinaciones de rasgos muy distintas que podrían expresarla.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (tres propuestas de ejemplo para una pieza que exprese «incertidumbre»). Propuesta A (segura): una melodía conocida de cuatro frases iguales, tempo constante, sin sorpresas. "
     "Propuesta B (riesgo con criterio): una voz susurrada sobre golpes suaves de objetos; un silencio de 2 pulsos justo donde se espera un golpe; el tempo baja un poco al final. "
     "Propuesta C (azar sin criterio): elegir cada sonido tirando un dado, sin escuchar el resultado ni decidir nada.")
build(
    O2, 2, F,
    use="Aprenderé a tomar riesgos creativos al elegir recursos de producción (voz, objetos, instrumentos, tecnologías) y a distinguirlos del azar sin criterio, comprobando con la escucha si el riesgo expresa la idea.",
    prior=["Sé qué recursos de producción existen.", "Relaciono rasgos del lenguaje musical con sensaciones.", "Sé cambiar una variable por prueba."],
    explain=[
        "Tomar un riesgo creativo es probar algo que no sabes si funcionará, porque podría expresar mejor tu idea que lo habitual. Por ejemplo, usar la voz susurrada en vez de cantada, ubicar un silencio donde se espera un sonido, o combinar un instrumento con un objeto sonoro. El riesgo tiene criterio cuando se relaciona con la idea que quieres expresar y se comprueba escuchando.",
        "No todo cambio inesperado es un riesgo creativo. Elegir sonidos a ciegas, sin escucharlos ni decidir, es azar sin criterio. La opción segura, como repetir una fórmula conocida, tampoco está mal, pero puede expresar menos. Una buena práctica es probar una opción segura y otra arriesgada, compararlas y quedarse con la que sirve a la idea.",
        "Los riesgos también tienen límites de seguridad: volumen moderado, objetos sin filo ni piezas pequeñas, y nunca poner en peligro a otras personas ni sus oídos. Registra qué arriesgaste, qué esperabas y qué ocurrió.",
    ],
    vocab=[("riesgo creativo", "probar una opción poco habitual cuyo resultado no está asegurado"), ("criterio", "razón que guía una decisión"), ("azar", "elegir sin decidir, dejando todo a la suerte"), ("opción segura", "fórmula conocida que probablemente funcione"), ("contraste", "diferencia marcada entre dos partes o sonidos")],
    worked=[
        ("Clasificar una propuesta", "¿La propuesta B de la ficha es riesgo con criterio o azar? Justifica.", ["Tiene una idea: incertidumbre.", "El silencio donde se espera un golpe crea duda, y se puede comprobar escuchando.", "Cada decisión se relaciona con la idea."], "Riesgo con criterio, porque las decisiones se relacionan con la idea"),
        ("Planificar pruebas", "Probar cada propuesta cuesta 3 minutos de ensayo. ¿Cuánto tiempo tarda el grupo en probar A, B y dos variantes de B?", ["Total de pruebas: 1 + 1 + 2 = 4.", "Tiempo: 4 × 3 = 12 minutos."], "12 minutos"),
    ],
    mistakes=[("Creer que «arriesgar» es hacer cualquier cosa rara.", "Sin relación con la idea no hay riesgo creativo, solo azar.", "Pregunta qué idea expresa cada decisión inesperada."),
              ("Pensar que la opción segura siempre está mal.", "Puede funcionar; el problema es no compararla con otra.", "Prueba una segura y una arriesgada y elige con evidencia.")],
    T=[
        ('abc', '{F} ¿Qué propuesta es azar sin criterio?', 'La C, porque elige los sonidos con un dado sin escuchar', 'La A, porque no tiene sorpresas', 'La B, porque tiene un silencio inesperado', 'En C no hay escucha ni decisión; en B las decisiones apoyan la idea.'),
        ('abc', '{F} ¿Qué decisión de la propuesta B crea duda?', 'Un silencio de 2 pulsos donde se espera un golpe', 'Una melodía conocida de cuatro frases iguales', 'Un tempo exactamente constante', 'El silencio inesperado rompe la expectativa y sugiere incertidumbre.'),
        ('ab', 'Un riesgo creativo con criterio es', 'una decisión poco habitual que se relaciona con la idea y se comprueba', 'un cambio al azar que no se escucha', 'Se relaciona con la idea y se comprueba escuchando, a diferencia del azar.'),
        ('abc', '{F} ¿Qué caracteriza a la propuesta A?', 'Repite una fórmula conocida con poca sorpresa', 'Usa objetos sonoros y silencios inesperados', 'Elige sonidos con un dado', 'Es la opción segura: cuatro frases iguales y tempo constante.'),
        ('=', '{F} Cada prueba dura 3 minutos. Si prueban la propuesta A, la B y tres variantes de B, ¿cuántos minutos necesitan?', '(1+1+3)*3', 'Hay 5 pruebas de 3 minutos cada una.', ' minutos'),
        ('abc', '{F} El grupo prefiere la propuesta A pero quiere compararla. ¿Qué decisión conviene?', 'Probar A y B con el mismo tempo base y escuchar las dos', 'Descartar B sin probarla porque parece rara', 'Elegir B solo porque nadie la hizo antes', 'La comparación con evidencia evita decidir por prejuicio o por novedad.'),
        ('abc', 'Una estudiante dice que arriesgarse es usar el sonido más fuerte posible. ¿Qué advertencia corresponde?', 'El volumen alto daña los oídos y además no expresa ninguna idea, así que no es un riesgo creativo', 'Sí, porque sonar fuerte siempre llama la atención', 'Solo se permite con un instrumento eléctrico', 'El volumen seguro es una condición, no un recurso expresivo.'),
        ('abc', '{F} La voz susurrada de la propuesta B se tapa con los golpes. ¿Qué ajuste es mejor?', 'Bajar el volumen de los golpes para que la voz se oiga', 'Subir el volumen de toda la mezcla', 'Eliminar la voz', 'Se equilibran las capas sin subir el volumen general.'),
        ('abc', 'Un grupo agrega un objeto sonoro de plástico al azar «porque suena raro». ¿Qué pregunta lo ayudaría a decidir?', '¿Qué parte de la idea expresa este sonido y cómo lo comprobaremos?', '¿Qué otro grupo usó uno parecido?', '¿Cuál objeto es más difícil de conseguir?', 'Relacionar el recurso con la idea convierte el azar en una decisión.'),
        ('abc', '{F} En la propuesta B, ¿qué recurso pertenece a la familia de los objetos sonoros?', 'Los golpes suaves hechos con objetos', 'La voz susurrada', 'El tempo que baja al final', 'Los golpes de objetos son objetos sonoros; la voz es otra familia y el tempo es un rasgo, no un recurso.'),
        ('abc', 'Probaron una opción arriesgada y no funcionó. ¿Qué conclusión es válida?', 'Aprendieron qué no sirve para esa idea y pueden ajustar', 'Que no deben volver a arriesgarse nunca más', 'Que la idea era mala desde el principio', 'Un riesgo que falla entrega información útil para decidir.'),
        ('abc', '{F} La propuesta B baja el tempo un poco al final. ¿Qué efecto busca probablemente?', 'Una sensación de duda o de que algo se detiene', 'Un final enérgico y festivo', 'Que el público aplauda antes de terminar', 'Bajar el tempo suele frenar y dejar la idea en suspenso.'),
        ('abc', 'Para registrar un riesgo, ¿qué conviene anotar?', 'Qué arriesgaron, qué esperaban y qué ocurrió', 'Solo si les gustó o no', 'El nombre del grupo que lo hizo antes', 'El registro permite comparar lo esperado con lo logrado.'),
    ],
    ctx=('abc', 'Un grupo escolar quiere expresar «incertidumbre» y duda entre repetir una fórmula conocida o probar un silencio inesperado. Tienen tiempo para dos pruebas. ¿Qué es lo más razonable?', 'Probar ambas opciones y elegir según lo que se oye en cada una', 'Probar solo la conocida porque siempre funciona', 'Probar el silencio sin escucharlo', 'Comparar con la escucha permite decidir con evidencia.'),
    sc=[
        ('¿Qué es un riesgo creativo?', 'Probar una opción poco habitual relacionada con la idea', 'Se relaciona con la idea y se comprueba escuchando.'),
        ('¿Cuántos minutos son 5 pruebas de 4 minutos cada una?', '20', 'Se multiplica 5 pruebas por 4 minutos cada una.'),
        ('abc', 'Elegir sonidos con un dado sin escucharlos es', 'azar sin criterio, porque no hay escucha ni decisión', 'riesgo creativo con criterio', 'una opción segura', 'No hay escucha ni decisión que lo relacione con la idea.'),
    ],
    op=("Con la {F} imagina que debes expresar «incertidumbre» con un recurso distinto a los de la ficha. Elige un recurso (voz, objeto, instrumento o tecnología), describe el riesgo que tomarás, qué esperas que ocurra y cómo lo comprobarás.",
        "Recurso: reverberación. Riesgo: aplicarla solo al último golpe para que se alargue y quede en duda. Espero que el final no suene cerrado. Lo comprobaré escuchando con y sin el efecto.",
        ["recurso elegido", "riesgo relacionado con la idea", "forma de comprobar"], ["descripción del riesgo y su comprobación"], ["riesgo sin relación con la idea", "no comprobar escuchando"],
        "Reconoce el riesgo y pide explicar qué opción segura compararía."),
    reinforce="Escribe dos propuestas para expresar «alegría»: una segura y una arriesgada, y justifica cada una en una frase.",
    extend="Elige una pieza que conozcas y señala un riesgo creativo que tome, relacionándolo con su idea.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (figuras y compás de ejemplo). En un compás de 4/4 caben 4 pulsos. Valores: redonda = 4 pulsos; blanca = 2 pulsos; negra = 1 pulso; dos corcheas juntas = 1 pulso; silencio de negra = 1 pulso sin sonido. "
     "Compás P: blanca, negra, negra. Compás Q: negra, dos corcheas, negra, negra. Compás R: blanca, dos corcheas, silencio de negra. Compás S: negra, negra, blanca, negra.")
build(
    O2, 3, F,
    use="Aprenderé a ensayar decisiones de ritmo y duración con figuras (redonda, blanca, negra, corcheas y silencios) dentro de un compás de 4/4, para dar un carácter expresivo a una idea.",
    prior=["Cuento pulsos en un patrón.", "Sé que el silencio ocupa tiempo.", "Relaciono rasgos con sensaciones."],
    explain=[
        "El ritmo organiza los sonidos y silencios en el tiempo, y la duración es cuánto dura cada sonido. Las figuras son los signos que indican esa duración. Tomando la negra como un pulso: la blanca dura 2 pulsos, la redonda 4 pulsos, y dos corcheas juntas completan 1 pulso. Los silencios tienen figuras equivalentes; el silencio de negra dura 1 pulso, pero sin sonido.",
        "En el compás de 4/4 caben 4 pulsos. Un compás está completo cuando la suma de sus figuras da 4. Por ejemplo, blanca (2) + negra (1) + negra (1) = 4. Los patrones con notas largas suelen sonar tranquilos, mientras que muchas corcheas seguidas dan sensación de movimiento. Un silencio bien ubicado crea tensión antes de un golpe.",
        "Para ensayar una decisión rítmica se escribe el compás en texto, se cuenta en voz baja pulso por pulso («1, 2, 3, 4») y se comprueba que suma 4. Después se cambia una figura por otra de igual duración y se compara el efecto.",
    ],
    vocab=[("figura", "signo que indica cuánto dura un sonido"), ("negra", "figura que dura 1 pulso"), ("blanca", "figura que dura 2 pulsos"), ("corcheas", "figuras que se cuentan de a dos por cada pulso"), ("compás de 4/4", "agrupación de 4 pulsos"), ("duración", "tiempo que dura un sonido")],
    worked=[
        ("Completar el compás", "Un compás de 4/4 tiene: negra, blanca y un espacio vacío. ¿Qué figura lo completa?", ["Negra (1) + blanca (2) = 3 pulsos.", "Faltan 4 − 3 = 1 pulso.", "Una negra o un silencio de negra completan."], "Una negra o un silencio de negra"),
        ("Sumar duraciones", "¿Cuánto suman: negra, dos corcheas, negra, negra?", ["Negra: 1.", "Dos corcheas juntas: 1.", "Negra: 1 y negra: 1."], "4 pulsos, el compás está completo"),
    ],
    mistakes=[("Contar cada corchea como un pulso completo.", "Dos corcheas juntas suman un solo pulso.", "Cuenta las corcheas de a dos por cada pulso."),
              ("Olvidar sumar los silencios.", "Un silencio también ocupa tiempo del compás.", "Incluye los silencios en la suma.")],
    T=[
        ('=', '{F} ¿Cuántos pulsos suma el compás P (blanca, negra, negra)?', '2+1+1', 'Blanca 2, negra 1 y negra 1.', ' pulsos'),
        ('=', '{F} ¿Cuántos pulsos suma el compás Q (negra, dos corcheas, negra, negra)?', '1+1+1+1', 'Negra 1, dos corcheas juntas 1, negra 1 y negra 1.', ' pulsos'),
        ('abc', '{F} ¿Cuántos pulsos dura una blanca?', '2', '1', '4', 'La blanca dura el doble de una negra.'),
        ('=', '{F} ¿Cuántos pulsos suma el compás R (blanca, dos corcheas, silencio de negra)?', '2+1+1', 'Blanca 2, dos corcheas 1 y silencio de negra 1.', ' pulsos'),
        ('abc', '{F} El compás S: negra, negra, blanca, negra. ¿Cuánto suma?', '5 pulsos, así que sobra un pulso y el compás no está completo', '4 pulsos, así que está completo', '3 pulsos, así que falta uno', '1 + 1 + 2 + 1 = 5, más que los 4 pulsos del compás.'),
        ('abc', '{F} Quieren corregir el compás S para que sume 4. ¿Qué cambio basta?', 'Cambiar la blanca por una negra, que reduce 1 pulso', 'Cambiar la última negra por una blanca', 'Agregar una redonda al final', 'Cambiar la blanca (2) por una negra (1) reduce la suma de 5 a 4.'),
        ('abc', 'En 4/4, ¿cuál de estas combinaciones está completa?', 'Una sola redonda, que dura 4 pulsos', 'Blanca y negra', 'Blanca, negra, negra y negra', 'Una redonda dura 4 pulsos; la segunda suma 3 y la tercera suma 5.'),
        ('abc', '{F} Entre los compases P y Q, ¿cuál suena más tranquilo por tener un sonido más largo?', 'El compás P, porque tiene una blanca de sonido largo', 'El compás Q, que tiene corcheas', 'Los dos suenan igual', 'Una nota larga como la blanca tiende a dar más calma que varias corcheas.'),
        ('abc', '{F} El silencio de negra del compás R aparece al final. ¿Qué efecto puede producir?', 'Una pequeña espera antes del compás siguiente', 'Que el compás tenga 5 pulsos', 'Que las corcheas pasen a durar 2 pulsos', 'Un silencio al final marca pausa y no cambia las duraciones.'),
        ('abc', 'Alguien cuenta «1, 2, 3, 4, 5» al leer un compás de 4/4. ¿Qué debe revisar?', 'Si alguna figura está mal sumada o falta recortar un valor', 'Si los silencios no se escuchan', 'Si el tempo es demasiado lento', 'Contar un pulso de más indica que la suma excede lo que cabe.'),
        ('abc', '{F} ¿Cuántos pulsos hay en 3 compases iguales al compás P?', '12', '8', '9', '3 compases de 4 pulsos cada uno suman 12 pulsos.'),
        ('abc', 'Al cambiar dos corcheas por una negra, ¿qué pasa con la duración del compás?', 'No cambia, porque ocupan lo mismo', 'Aumenta en un pulso', 'Disminuye en un pulso', 'Dos corcheas juntas y una negra duran 1 pulso las dos.'),
        ('abc', '{F} Quieren una versión más inquieta del compás P. ¿Qué cambio es coherente?', 'Reemplazar cada negra por dos corcheas', 'Reemplazar la blanca por una redonda', 'Quitar todos los sonidos', 'Dos corcheas ocupan lo mismo que una negra, pero dan más movimiento.'),
    ],
    ctx=('abc', 'Un grupo escribe un compás en 4/4: negra, silencio de negra, blanca. Quiere que dure exactamente 4 pulsos. ¿Qué concluyen?', 'Está completo, porque el silencio también cuenta: 1 + 1 + 2 = 4', 'Le sobra un pulso por el silencio', 'Le falta un pulso porque la blanca dura 1', 'Los silencios cuentan: la suma es 4.'),
    sc=[
        ('¿Cuántos pulsos suman dos corcheas juntas?', '1', 'Dos corcheas juntas equivalen a una negra.'),
        ('¿Cuántos pulsos caben en un compás de 4/4?', '4', 'El nombre 4/4 indica cuatro pulsos por compás.'),
        ('abc', 'El silencio de negra', 'dura 1 pulso, que se cuenta aunque no suene nada', 'dura 2 pulsos y suena suave', 'no cuenta en el compás', 'Los silencios también ocupan tiempo dentro del compás.'),
    ],
    op=("Con la {F} escribe un compás de 4/4 propio con al menos una blanca o una negra, un silencio y dos corcheas. Suma las figuras (debe dar 4) y di qué sensación quieres lograr con ese ritmo.",
        "Compás: negra, silencio de negra, dos corcheas, negra. 1 + 1 + 1 + 1 = 4. Quiero una sensación de duda: el silencio crea espera y las corcheas llevan a la nota final.",
        ["compás completo", "suma comprobada", "sensación justificada"], ["compás en texto y suma"], ["suma distinta de 4", "olvidar el silencio"],
        "Reconoce el compás y pide mostrar la suma figura por figura."),
    reinforce="Escribe tres compases distintos de 4/4 con figuras de la clase y comprueba que cada uno suma 4.",
    extend="Elige una canción que conozcas y marca con palmadas un compás de cuatro pulsos; cuenta en voz baja y anota dónde hay notas largas.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (idea y boceto de ejemplo). Idea: «la espera de un bus que no llega». Parte 1 (4 compases de 4/4): 70 pulsos por minuto, un golpe suave en cada compás (pulso 1). "
     "Parte 2 (4 compases): los golpes aparecen en cada pulso con corcheas al final del compás y el tempo sube a 90 pulsos por minuto. "
     "Parte 3 (1 compás): un silencio de 2 pulsos y una nota larga de 2 pulsos, sin acompañamiento. Recursos: cajonera, voz hablada y teclado con sonido de cuerdas.")
build(
    O2, 4, F,
    use="Aprenderé a pasar de una idea a un boceto musical: dividirla en partes, elegir recursos y rasgos del lenguaje musical para cada parte, y comprobar que la secuencia expresa lo que quería.",
    prior=["Relaciono rasgos con sensaciones.", "Tomo riesgos con criterio.", "Sumo figuras en un compás de 4/4."],
    explain=[
        "Crear música a partir de una idea requiere un boceto: un plan breve con partes ordenadas. Primero se escribe la idea en una frase y se imagina cómo cambia a lo largo del tiempo, por ejemplo de la calma a la tensión y a la resolución. Después se asigna a cada parte un conjunto de decisiones: tempo, ritmo, timbre, dinámica y silencios, siempre relacionados con la idea.",
        "En el boceto de la espera de un bus, la parte 1 muestra tranquilidad con pocos golpes, la parte 2 crece con más golpes y más rapidez, y la parte 3 resuelve con un silencio y una nota larga. El total de compases se calcula sumando: 4 + 4 + 1 = 9 compases, y como cada compás tiene 4 pulsos, la pieza dura 36 pulsos.",
        "Un buen boceto se comprueba ensayándolo en voz baja o con golpes suaves. Si una parte no expresa la idea, se cambia una sola variable y se vuelve a probar. Conviene anotar qué cambio hiciste y por qué.",
    ],
    vocab=[("boceto", "plan breve de una pieza, con partes y decisiones"), ("idea", "lo que se quiere expresar con la música"), ("resolución", "parte donde la tensión se calma o termina"), ("progresión", "cambio gradual de una parte a otra"), ("compases", "grupos de pulsos en que se divide la pieza")],
    worked=[
        ("Calcular la extensión", "Un boceto de ejemplo tiene partes de 5, 3 y 2 compases en 4/4. ¿Cuántos pulsos dura?", ["Compases: 5 + 3 + 2 = 10.", "Pulsos: 10 × 4 = 40."], "40 pulsos"),
        ("Justificar una decisión", "¿Por qué sube el tempo de 70 a 90 pulsos por minuto en la parte 2?", ["La idea es una espera que se vuelve impaciente.", "Un pulso más rápido da sensación de impaciencia.", "Se contrasta con la parte 1, tranquila."], "Para expresar impaciencia y contrastar con la parte 1"),
    ],
    mistakes=[("Poner todas las decisiones en una sola parte.", "La idea no cambia en el tiempo y el boceto no tiene contraste.", "Divide la idea en partes y asigna decisiones a cada una."),
              ("Olvidar anotar el tempo o los compases del boceto.", "Otras personas, o tú más tarde, no podrán reproducirlo.", "Anota tempo, compases y recursos por cada parte.")],
    T=[
        ('=', '{F} ¿Cuántos compases tiene el boceto en total?', '4+4+1', 'Se suman los compases de las tres partes.', ' compases'),
        ('=', '{F} ¿Cuántos pulsos tiene la parte 2?', '4*4', 'Son 4 compases de 4 pulsos cada uno.', ' pulsos'),
        ('abc', '{F} ¿Qué parte del boceto resuelve la tensión?', 'La parte 3, con un silencio y una nota larga sin acompañamiento', 'La parte 1, con un golpe suave', 'La parte 2, con golpes en cada pulso', 'Un silencio y una nota larga sin acompañamiento generan una resolución.'),
        ('abc', '¿Qué es un boceto musical?', 'Un plan breve de una pieza, con partes y decisiones', 'La grabación final lista para publicar', 'La opinión del público sobre la pieza', 'El boceto ordena las decisiones antes de la versión final.'),
        ('abc', '{F} ¿Qué rasgo hace que la parte 2 transmita más impaciencia que la 1?', 'Más golpes por compás y un tempo mayor', 'Un silencio de dos pulsos', 'Una sola nota larga en la voz', 'Los golpes en cada pulso y el tempo de 90 aceleran la sensación.'),
        ('=', '{F} En la parte 3 hay un silencio de 2 pulsos y una nota larga de 2 pulsos. ¿Cuántos pulsos suma el compás?', '2+2', 'El silencio y la nota larga suman los 4 pulsos del compás.', ' pulsos'),
        ('abc', '{F} Si la parte 1 durara 6 compases en vez de 4, ¿cuántos compases tendría el boceto?', '11', '9', '13', '6 + 4 + 1 = 11 compases.'),
        ('abc', 'Una compañera propone que la parte 3 incluya percusión muy fuerte. ¿Qué pregunta ayuda a decidir?', '¿Eso ayuda a resolver la espera de la idea o la contradice?', '¿Cuántas personas conocen esa percusión?', '¿Qué estilo es más popular entre sus amistades?', 'Toda decisión debe relacionarse con la idea del boceto.'),
        ('abc', '{F} Quieren mostrar que el bus por fin llega. ¿Qué agregarían a la parte 3?', 'Un crescendo corto y un golpe final claro que marque la llegada', 'Más silencios hasta que no suene nada', 'Un tempo de 40 pulsos por minuto', 'Un sonido final claro después de la espera sugiere la llegada.'),
        ('abc', '{F} ¿Qué dato de la parte 1 indica poca actividad?', 'Un golpe suave en el pulso 1 de cada compás', 'Golpes en cada pulso', 'Un tempo de 90', 'Un golpe por compás es poca actividad rítmica.'),
        ('abc', 'Al ensayar el boceto, la parte 2 no logra parecer impaciente. ¿Cuál es el mejor ajuste?', 'Cambiar una sola variable, como más golpes o más tempo, y comparar', 'Reescribir todo el boceto desde cero', 'Dejar la parte 2 igual y subir el volumen de toda la pieza', 'Un cambio a la vez permite saber qué mejoró.'),
        ('abc', '{F} ¿Cuántos pulsos hay entre el inicio de la parte 1 y el final de la parte 2?', '32', '36', '16', '8 compases de 4 pulsos: 32 pulsos.'),
        ('abc', 'La idea de un boceto es «una tormenta que se calma». ¿Qué orden de partes es coherente?', 'Tensión creciente, un punto máximo y después calma', 'Calma, calma y calma', 'Calma y luego silencio', 'La idea implica un cambio en el tiempo que debe notarse en las partes.'),
    ],
    ctx=('abc', 'Un grupo escolar quiere presentar un boceto de 9 compases en 4/4 y solo dispone de 30 pulsos en el acto. ¿Qué concluyen?', 'No cabe: 9 compases de 4 pulsos son 36 pulsos y superan los 30', 'Cabe de sobra porque 9 es menor que 30', 'Cabe exactamente porque 9 × 3 = 27', 'Cada compás tiene 4 pulsos y 9 × 4 = 36, más que 30.'),
    sc=[
        ('¿Cuántos pulsos hay en 5 compases de 4/4?', '20', 'Se multiplica 5 por 4 pulsos.'),
        ('¿Para qué sirve un boceto antes de la versión final?', 'Para ordenar partes y decisiones', 'Permite ensayar y corregir con un plan.'),
        ('abc', 'Una idea se expresa mejor si', 'cambia a lo largo de la pieza con contrastes', 'se repite igual todo el tiempo', 'se esconde detrás de efectos', 'El contraste hace notar la progresión de la idea.'),
    ],
    op=("Con la {F} como modelo, escribe tu propio boceto de 3 partes para la idea «una sorpresa en la sala de clases»: número de compases por parte (suma total), tempo, un recurso y un rasgo por parte, y una frase que explique cómo cambia la idea.",
        "Parte 1: 4 compases, 80 ppm, voz hablada suave. Parte 2: 2 compases, 120 ppm, golpes en cada pulso. Parte 3: 1 compás, silencio de 2 pulsos y nota larga. Total: 7 compases. La idea pasa de la normalidad a la sorpresa y a la calma.",
        ["tres partes", "total de compases", "recursos y rasgos justificados"], ["boceto escrito"], ["partes sin contraste", "total mal sumado"],
        "Reconoce el boceto y pide comprobar la suma de compases."),
    reinforce="Escribe un boceto de dos partes para la idea «amanecer» con tempo y recurso para cada una.",
    extend="Agrega una cuarta parte a tu boceto y explica cómo cambia la idea con ella.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 5 (bitácora de ejemplo de un grupo). Registro en tres columnas: versión, cambio, efecto. V1: boceto de 9 compases a 90 pulsos por minuto; efecto: la parte 2 se confunde porque la cajonera y el teclado suenan fuertes a la vez. "
     "V2: se baja el volumen del teclado en la parte 2; efecto: se oyen mejor los golpes. V3: se agrega un silencio de 1 pulso antes de la nota final; efecto: la nota final se espera más. "
     "Registro gráfico de la parte 3: una línea horizontal larga (nota larga) precedida de un espacio vacío (silencio).")
build(
    O2, 5, F,
    use="Aprenderé a registrar una creación musical (con texto, esquemas gráficos o grabación) y a ajustar una versión con evidencia, anotando qué cambió y qué efecto tuvo.",
    prior=["Hago un boceto con partes.", "Cambio una variable por prueba.", "Describo el efecto con rasgos comprobables."],
    explain=[
        "Registrar una obra significa dejarla anotada de modo que otra persona, o tú mismo más adelante, pueda reproducirla. Se puede registrar con texto (partes, compases, tempo, recursos), con un esquema gráfico (líneas largas para notas largas, espacios para silencios, puntos para golpes) o con una grabación hecha a volumen moderado. Lo importante es que el registro permita rehacer la pieza y entender las decisiones.",
        "Ajustar es mejorar una versión con evidencia. La bitácora de versiones anota qué cambió y cuál fue el efecto oído. Se cambia una variable por vez, y si el cambio no ayuda, se puede volver a la versión anterior. Un ajuste útil se relaciona con la idea: no se corrige solo por gusto, sino porque la idea se expresa mejor.",
        "Al terminar, conviene dejar anotado qué quedó logrado y qué no se alcanzó a resolver. Reconocer un límite honestamente es parte del proceso creativo.",
    ],
    vocab=[("registro", "anotación que permite reproducir y entender una obra"), ("esquema gráfico", "dibujo con líneas y puntos que representa duraciones y golpes"), ("bitácora", "cuaderno donde se anotan versiones, cambios y efectos"), ("versión", "estado de la obra en un momento del proceso"), ("ajuste", "cambio que busca mejorar una versión")],
    worked=[
        ("Leer una bitácora", "En la ficha, ¿qué cambio mejoró la claridad de los golpes de la parte 2?", ["Revisamos las filas de la bitácora.", "V2 baja el volumen del teclado en la parte 2.", "El efecto anotado es que se oyen mejor los golpes."], "V2: bajar el volumen del teclado en la parte 2"),
        ("Calcular una duración", "A 90 pulsos por minuto, ¿cuántos segundos duran 9 compases de 4/4 (36 pulsos)?", ["36 × 60 = 2.160.", "2.160 ÷ 90 = 24 segundos."], "24 segundos"),
    ],
    mistakes=[("Registrar solo «mejoré la pieza».", "No se sabe qué cambió ni qué efecto produjo.", "Anota la versión, el cambio y el efecto oído."),
              ("Borrar las versiones anteriores.", "Impide volver atrás si el cambio no ayudó.", "Conserva cada versión con su fecha o número.")],
    T=[
        ('abc', '{F} ¿Qué cambio se hizo entre V1 y V2?', 'Se bajó el volumen del teclado para oír los golpes de la parte 2', 'Se subió el tempo a 120 pulsos por minuto', 'Se agregó un silencio antes de la nota final', 'La bitácora indica ese ajuste en V2.'),
        ('abc', '{F} ¿Qué efecto tuvo agregar el silencio de 1 pulso en V3?', 'La nota final se espera más, con sensación de expectativa', 'Los golpes se oyen más fuertes', 'La pieza se vuelve más rápida', 'El silencio antes de la nota crea expectativa.'),
        ('=', '{F} A 90 pulsos por minuto, ¿cuántos segundos duran 45 pulsos?', '45*60//90', 'Se multiplican los pulsos por 60 y se divide por los pulsos por minuto.', ' segundos'),
        ('abc', '¿Qué debe permitir un buen registro de una obra?', 'Reproducir la pieza y entender las decisiones', 'Reemplazar la escucha por completo', 'Ocultar las versiones anteriores', 'Registrar sirve para rehacer y comprender la obra.'),
        ('abc', '{F} En el registro gráfico, ¿qué representa el espacio vacío antes de la línea larga?', 'Un silencio, es decir, un momento sin sonido', 'Un golpe fuerte que marca el pulso', 'Una nota corta que suena aguda', 'Los espacios vacíos representan silencio y la línea larga una nota larga.'),
        ('abc', '{F} V3 agrega un silencio, pero la parte 2 sigue confusa. ¿Qué anotación es útil para V4?', 'Cambio: bajar el volumen de la cajonera en la parte 2; efecto esperado: se distinguen los golpes del teclado', 'Cambio: rehacer todo el boceto; efecto: tal vez mejore', 'Cambio: ninguno; efecto: sigue igual de confuso', 'Se anota un solo cambio y el efecto que se espera comprobar.'),
        ('abc', 'Un grupo graba su pieza con volumen muy alto «para que se note». ¿Qué corresponde?', 'Bajar el volumen y mantenerlo moderado para cuidar los oídos', 'Subirlo más para evitar ruidos', 'Dejarlo igual porque es una grabación', 'El volumen alto daña los oídos aun en una grabación.'),
        ('abc', '{F} ¿Qué versión conviene conservar si V3 resulta peor que V2?', 'V2, porque conservarla permite volver a ella si un cambio empeora', 'Ninguna: se borran V2 y V3', 'Solo V1, porque fue la primera', 'Conservar las versiones permite volver atrás si un cambio no ayuda.'),
        ('abc', 'Un ajuste se justifica mejor con la frase', '«Cambié el volumen porque la voz no se oía y ahora comprobé que se oye»', '«Cambié el volumen porque sí»', '«Cambié el volumen porque a mi amigo no le gusta»', 'Un ajuste útil responde a un efecto comprobable.'),
        ('abc', '{F} ¿Qué versión ajusta el final de la pieza y no la mezcla de la parte 2?', 'V3, que agrega un silencio antes de la nota final', 'V2, que baja el volumen del teclado', 'V1, que es el boceto inicial', 'V3 cambia el final; V2 corrige la mezcla de la parte 2 y V1 no ajusta nada.'),
        ('abc', 'En el registro gráfico, un punto representa un golpe. ¿Cuántos golpes hay en «● ● _ ● _ _ ● _» (● es un golpe, _ es un silencio y cada símbolo es un pulso)?', '4', '3', '5', 'Los puntos están en los pulsos 1, 2, 4 y 7.'),
        ('abc', 'Al terminar la obra, ¿qué es un límite honesto?', 'Una parte que no alcanzaron a resolver, dicha con claridad', 'Una lista de culpas por lo que salió mal', 'Una opinión sobre otro grupo', 'Reconocer lo no resuelto ayuda a mejorar sin culpar.'),
        ('abc', '{F} ¿Qué orden sigue un ajuste con evidencia?', 'Escuchar, cambiar una variable, volver a escuchar y anotar', 'Cambiar varias variables, anotar y no escuchar', 'Escuchar una vez y decidir sin más', 'El orden asegura que el efecto se comprueba.'),
    ],
    ctx=('abc', 'El grupo tiene dos versiones: V1 y V2. En V2 cambiaron tempo y timbre a la vez y quedó mejor, pero no saben por qué. ¿Qué deberían hacer en la próxima prueba?', 'Cambiar solo una de las dos variables en cada prueba y comparar los resultados', 'Cambiar una tercera variable para ver qué pasa', 'Mantener V2 sin más pruebas porque quedó mejor', 'Separar las variables permite saber qué produjo la mejora.'),
    sc=[
        ('¿Qué anota una bitácora de versiones?', 'La versión, el cambio y el efecto oído', 'Permite reconstruir el proceso de ajuste.'),
        ('¿Cuántos segundos duran 60 pulsos a 120 pulsos por minuto?', '30', '60 × 60 ÷ 120 da 30 segundos.'),
        ('abc', 'Un registro gráfico es', 'un esquema con líneas, espacios y puntos que representa duraciones', 'una partitura profesional completa, que solo sirve para expertos', 'una grabación de video de todo el ensayo', 'Es una forma simple de anotar duraciones y silencios.'),
    ],
    op=("Con la {F} como modelo, escribe una bitácora de 3 versiones para tu propia creación: versión, cambio y efecto en cada fila, y un registro gráfico de una de las partes con líneas largas, espacios y puntos.",
        "V1: boceto de 7 compases; efecto: la parte 1 es muy larga. V2: acorto la parte 1 a 3 compases; efecto: la idea avanza más rápido. V3: agrego un silencio de 1 pulso al final; efecto: el cierre se espera. Gráfico parte 3: ● _ ● ● _ _ ● _.",
        ["tres versiones", "cambio y efecto", "registro gráfico"], ["bitácora y esquema"], ["no anotar el efecto", "cambiar varias variables"],
        "Reconoce la bitácora y pide separar mejor el cambio del efecto."),
    reinforce="Elige una pieza tuya o una de ejemplo y escribe un registro en texto con tempo, partes, compases y recursos.",
    extend="Compara tu registro gráfico con el de una compañera y anota si cualquiera de los dos podría reproducir la pieza.",
)
