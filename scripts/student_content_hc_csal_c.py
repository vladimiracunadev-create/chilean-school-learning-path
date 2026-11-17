"""Ciencias de la salud (electivo 3.º y 4.º medio HC): OAC-05 (desarrollo científico y tecnológico, biotecnología, nanomedicina, medicina nuclear, imagenología y farmacología, y calidad de vida, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio, internet ni equipos. "
             "Este cuaderno no propone experimentos con sustancias, seres vivos ni cuerpos, no diagnostica ni da consejos médicos personales, y no incluye procedimientos clínicos ni dosis de medicamentos. "
             "Las tecnologías de salud se explican solo a nivel conceptual: su uso corresponde a profesionales formados y autorizados. "
             "Las cifras son ilustrativas y no sirven para decidir sobre tu salud. Si un tema te preocupa a ti o a alguien cercano, cuéntaselo a una persona adulta de confianza o a un profesional de salud; si necesitas orientación inmediata, el Fono Niños 147 puede ayudarte.")
build = make_build(MATERIALS)

O5 = "CN-CSAL-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 21 (cinco innovaciones, descritas en términos generales). "
     "Biotecnología: uso de organismos vivos o de sus moléculas para fabricar productos; por ejemplo, la insulina que se produce con bacterias modificadas. "
     "Nanomedicina: uso de partículas de tamaño nanométrico (un nanómetro, nm, es la milmillonésima parte de un metro) para llevar medicamentos o detectar enfermedades; gran parte está aún en investigación. "
     "Medicina nuclear: uso de cantidades muy pequeñas de sustancias radiactivas, llamadas trazadores, para obtener imágenes o para tratar, siempre bajo control profesional. "
     "Imagenología: técnicas que producen imágenes del interior del cuerpo, como la radiografía, la ecografía y la resonancia magnética. "
     "Farmacología: estudio de cómo actúan los medicamentos en el cuerpo y de sus efectos. "
     "Dimensiones de la calidad de vida: física, psicológica, social y de acceso (cuánta gente puede usar la innovación).")
build(
    O5, 1, F,
    use="Aprenderé a delimitar qué innovación científica y tecnológica de la salud se analiza y qué parte de la calidad de vida se evalúa. Sirve para formular preguntas sobre beneficios, riesgos y acceso sin generalizar.",
    prior=["Sé que la ciencia y la tecnología cambian la medicina.", "Sé qué es una hipótesis.", "Sé qué es una unidad de medida."],
    explain=[
        "El desarrollo científico y tecnológico ha cambiado la salud de muchas personas. La biotecnología fabrica productos con organismos o moléculas vivas. La nanomedicina trabaja con partículas de tamaño nanométrico; un nanómetro es la milmillonésima parte de un metro, y un cabello humano es unas decenas de miles de veces más ancho. La medicina nuclear usa trazadores radiactivos para obtener imágenes o tratar. La imagenología produce imágenes del interior del cuerpo. La farmacología estudia cómo actúan los medicamentos.",
        "Evaluar una innovación es preguntar cómo influye en la calidad de vida, que es la percepción que una persona tiene de su bienestar físico, psicológico y social, y de su acceso a lo que necesita. Una misma innovación puede mejorar una dimensión y no otra: puede aliviar un síntoma físico y a la vez ser inaccesible para muchas personas. Por eso se delimita: qué innovación, para qué grupo, qué dimensión y con qué comparación.",
        "Una pregunta bien delimitada puede ser: «¿cómo cambió la calidad de vida de personas con diabetes tipo 1 desde que se produce insulina por biotecnología?». Observa que nombra una innovación, un grupo y una dimensión. Este cuaderno explica las tecnologías de manera conceptual, no enseña a usarlas ni a decidir tratamientos, y cualquier duda personal se conversa con un profesional de salud.",
    ],
    vocab=[("biotecnología", "uso de organismos vivos o de sus moléculas para fabricar productos o resolver problemas"), ("nanomedicina", "uso de partículas de tamaño nanométrico en el diagnóstico y el tratamiento"), ("medicina nuclear", "uso de pequeñas cantidades de sustancias radiactivas para imágenes o tratamientos"), ("imagenología", "conjunto de técnicas que producen imágenes del interior del cuerpo"), ("calidad de vida", "percepción de bienestar físico, psicológico y social de una persona y de su acceso a lo que necesita")],
    worked=[
        ("Clasificar una innovación", "Un laboratorio fabrica una proteína usando bacterias modificadas. ¿A qué área pertenece?",
         ["Usa organismos vivos para fabricar un producto.", "Eso corresponde a la biotecnología."],
         "Biotecnología"),
        ("Delimitar una pregunta", "¿Qué pregunta está mejor delimitada: «¿es buena la tecnología médica?» o «¿cómo cambió la movilidad de personas mayores con prótesis nuevas?»",
         ["La primera no fija una innovación, un grupo ni una dimensión.", "La segunda nombra una innovación, un grupo y una dimensión, la movilidad."],
         "La segunda pregunta"),
    ],
    mistakes=[("Pensar que toda innovación mejora la calidad de vida de todos.", "Una innovación puede ayudar a unos y no llegar a otros, o tener riesgos.", "Pregunta para quién, en qué dimensión y con qué acceso."),
              ("Confundir una tecnología con otra, por ejemplo imagenología con medicina nuclear.", "La imagenología produce imágenes con distintas técnicas, y la medicina nuclear usa trazadores radiactivos.", "Usa la definición de cada una antes de clasificar.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la biotecnología?", "El uso de organismos vivos o de sus moléculas para fabricar productos", "El estudio del desarrollo de los huesos", "El diseño de edificios de salud", "La biotecnología aprovecha los seres vivos o sus moléculas."),
        ("{F} ¿Qué mide un nanómetro?", "La milmillonésima parte de un metro", "La ficha define el nanómetro con esa fracción del metro."),
        ("ab", "{F} Una ecografía y una resonancia magnética son ejemplos de:", "Imagenología", "Farmacología", "Ambas técnicas producen imágenes del interior del cuerpo."),
        ("abc", "{F} Una técnica usa pequeñas cantidades de una sustancia radiactiva, bajo control profesional, para obtener una imagen. ¿Cuál es?", "Medicina nuclear", "Nanomedicina", "Farmacología", "La medicina nuclear emplea trazadores radiactivos."),
        ("=", "{F} Una nanopartícula de ejemplo mide 100 nm y un cabello de ejemplo mide 80.000 nm de ancho. ¿Cuántas veces más ancho es el cabello?", "80000/100", "Se divide 80.000 entre 100.", " veces"),
        ("abc", "{F} ¿Cuál es la mejor pregunta para evaluar una innovación?", "¿Cómo cambió la calidad de vida de personas con diabetes tipo 1 con la insulina biotecnológica?", "¿Qué es la salud?", "¿Por qué existen los medicamentos?", "La primera nombra una innovación, un grupo y una dimensión."),
        ("abc", "{F} Una prótesis nueva mejora la movilidad física, pero cuesta tanto que casi nadie puede acceder a ella. ¿Qué dimensiones mejoran y cuál no?", "Mejora la física, pero no el acceso", "Mejora el acceso, pero no la física", "No mejora ninguna", "La movilidad es física, y el costo limita el acceso."),
        ("abc", "{F} ¿Por qué se dice que la nanomedicina está en gran parte en investigación?", "Porque muchas aplicaciones aún se están probando y no se usan de manera general", "Porque ya se usa en todos los hospitales", "Porque no tiene ningún resultado", "La ficha señala que gran parte está aún en investigación."),
        ("abc", "{F} Un joven quiere estudiar el efecto de las vacunas producidas por biotecnología. ¿Qué dimensión de calidad de vida mide si cuenta cuántas personas dejaron de enfermar?", "La dimensión física", "La dimensión de acceso", "La dimensión social", "Enfermar menos se relaciona con la salud física."),
        ("abc", "{F} ¿Qué pregunta de delimitación se olvida si solo se dice «la medicina nuclear mejora la vida»?", "Para quién, en qué dimensión y con qué comparación", "Cuál es el color del equipo", "Cuántas personas trabajan en el hospital", "Delimitar exige precisar grupo, dimensión y comparación."),
        ("abc", "{F} Una innovación aumenta la calidad de vida de personas con una enfermedad poco frecuente, pero llega a muy pocas por su costo. ¿Qué conclusión es más completa?", "Mejora la vida de quienes la reciben, y el acceso es una limitación importante", "Mejora la vida de todos", "No sirve para nada", "La conclusión completa reconoce el beneficio y la limitación de acceso."),
        ("abc", "{F} Un estudiante dice: «la imagenología es lo mismo que la medicina nuclear». ¿Qué le aclaras?", "Que la imagenología incluye varias técnicas de imágenes y la medicina nuclear usa trazadores radiactivos", "Que son idénticas", "Que ninguna produce imágenes", "La medicina nuclear es una de las formas de obtener imágenes, con trazadores."),
        ("abc", "Una persona de ejemplo se pregunta si le conviene un tratamiento innovador. ¿Qué corresponde según este cuaderno?", "Conversarlo con un profesional de salud, que conoce su caso", "Decidir leyendo este cuaderno", "Probarlo para ver si funciona", "Este cuaderno no da consejos médicos y orienta a consultar."),
    ],
    ctx=("abc", "Contexto: tu curso debe presentar una exposición sobre una innovación en salud. ¿Cuál es el mejor tema bien delimitado?", "¿Cómo ha cambiado la calidad de vida de personas con diabetes tipo 1 desde que existe la insulina biotecnológica?", "La salud del mundo", "Todas las tecnologías médicas", "El tema nombra una innovación, un grupo y una dimensión de calidad de vida."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la farmacología?", "El estudio de cómo actúan los medicamentos en el cuerpo y de sus efectos", "La farmacología analiza la acción y los efectos de los medicamentos."),
        ("ab", "La calidad de vida incluye:", "Dimensiones físicas, psicológicas, sociales y de acceso", "Solo el estado físico", "Es una idea amplia que considera varias dimensiones."),
        ("ab", "Una buena pregunta de evaluación nombra:", "Una innovación, un grupo y una dimensión", "Solo la palabra salud", "Delimitar la pregunta permite buscar datos concretos y comparables."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) elige una de las cinco innovaciones y explica con tus palabras qué es; (2) escribe una pregunta bien delimitada sobre su efecto en la calidad de vida; (3) nombra una dimensión que podría mejorar y otra en la que podría no ayudar.",
        "(1) La imagenología produce imágenes del interior del cuerpo con técnicas como la ecografía. (2) «¿Cómo cambió la detección a tiempo de problemas en personas de zonas rurales con equipos de ecografía en un consultorio?» (3) Podría mejorar la dimensión física, y quizás no la de acceso si la persona vive lejos del equipo.",
        ["explicación correcta de la innovación", "pregunta con innovación, grupo y dimensión", "dos dimensiones distintas", "no da consejos médicos personales"],
        ["tres partes numeradas"],
        ["hacer una pregunta demasiado general", "confundir una tecnología con otra", "pensar que toda innovación sirve a todos"],
        "Pregunta: «¿qué dato necesitarías para saber si la innovación llega a quienes más la necesitan?»."),
    reinforce="Elige una innovación y escribe una ventaja y una limitación para la calidad de vida, indicando la dimensión de cada una.",
    extend="Explica por qué la misma innovación puede tener efectos distintos en la calidad de vida de dos grupos de personas.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 22 (tres textos de ejemplo sobre un tratamiento nuevo, el nanotratamiento NT). "
     "Texto 1: una noticia dice que «el NT hizo desaparecer tumores en ratones» en un estudio de laboratorio con 20 ratones y sin personas. "
     "Texto 2: un artículo científico, revisado por especialistas independientes antes de publicarse, informa un ensayo con 2.000 personas asignadas al azar: 1.000 recibieron el NT y 1.000 el tratamiento habitual. El ensayo fue financiado por la empresa que fabrica el NT, lo declaró y publicó todos sus resultados, incluidos los efectos adversos. "
     "Texto 3: un aviso de una tienda en línea que vende un «nanotratamiento milagroso» sin datos, solo con testimonios de clientes. "
     "Fases de una investigación de un tratamiento: preclínica (laboratorio y animales), fase 1 (seguridad en pocas personas), fase 2 (primera señal de eficacia), fase 3 (comparación en muchas personas) y fase 4 (vigilancia después de aprobarse).")
build(
    O5, 2, F,
    use="Aprenderé a evaluar fuentes y variables sobre una innovación de salud: en qué fase está la evidencia, quién la financia y si hay un grupo de comparación. Sirve para distinguir una noticia llamativa de evidencia sólida.",
    prior=["Sé qué es un grupo de comparación.", "Sé qué es una muestra.", "Sé calcular porcentajes."],
    explain=[
        "Para evaluar una innovación se pregunta en qué etapa está su evidencia. Un resultado en ratones, en la fase preclínica, es apenas un primer paso: muchos tratamientos que funcionan en animales no funcionan en personas. Las fases siguientes buscan primero seguridad en pocas personas (fase 1), luego una primera señal de eficacia (fase 2), después una comparación con el tratamiento habitual en muchas personas (fase 3) y, tras aprobarse, vigilancia (fase 4).",
        "Los mejores estudios son ensayos clínicos con asignación al azar y grupo de comparación, a veces con ciego, es decir, sin que las personas sepan qué grupo les tocó, para que sus expectativas no cambien los resultados. También se revisa quién financia el estudio, porque un interés económico no invalida el resultado pero exige transparencia, y si se publican todos los resultados, incluidos los efectos adversos. La revisión por pares es un filtro de calidad donde especialistas independientes revisan el trabajo antes de publicarlo.",
        "Un aviso con solo testimonios no es evidencia: nadie sabe cuántos casos hay, cómo se midió ni qué ocurrió con los demás. Ante una noticia sobre un «tratamiento milagroso», se pregunta por la fase, la muestra, la comparación y la fuente. Cualquier decisión sobre un tratamiento la toma una persona con su profesional de salud, no una noticia ni este cuaderno.",
    ],
    vocab=[("ensayo clínico", "estudio con personas que prueba un tratamiento siguiendo reglas éticas y científicas"), ("fase preclínica", "etapa de laboratorio y animales antes de probar en personas"), ("ciego", "diseño en que las personas no saben a qué grupo fueron asignadas, para que sus expectativas no cambien los resultados"), ("revisión por pares", "revisión de un trabajo por especialistas independientes antes de publicarlo"), ("efecto adverso", "efecto no deseado de un tratamiento")],
    worked=[
        ("Ubicar la fase", "Un estudio de ejemplo prueba un tratamiento en 15 personas para ver si es seguro. ¿En qué fase está?",
         ["Probar un tratamiento en pocas personas para ver si es seguro es la fase 1.", "La fase 2 buscaría una primera señal de eficacia y la fase 3 compararía en muchas personas."],
         "Fase 1"),
        ("Tamaño de grupos", "Un ensayo de ejemplo asigna al azar a 600 personas a dos grupos iguales. ¿Cuántas hay en cada grupo?",
         ["Se divide el total entre 2 grupos.", "600 entre 2 son 300."],
         "300 personas"),
    ],
    mistakes=[("Creer que un resultado en ratones ya vale para personas.", "Muchos tratamientos que funcionan en animales no funcionan en personas.", "Mira en qué fase está la evidencia."),
              ("Descartar un estudio solo porque lo financió una empresa.", "El financiamiento exige transparencia, pero no invalida el resultado por sí solo.", "Revisa si declaró el interés, publicó todos los resultados y pasó revisión por pares.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es un ensayo clínico?", "Un estudio con personas que prueba un tratamiento con reglas éticas y científicas", "Un aviso de venta", "Un experimento casero", "El ensayo clínico sigue protocolos éticos y científicos con personas."),
        ("{F} ¿En qué fase está la evidencia del Texto 1?", "Preclínica", "El Texto 1 habla de ratones, es decir, de laboratorio y animales."),
        ("ab", "{F} El Texto 2 compara el NT con el tratamiento habitual en 2.000 personas. Esto corresponde a:", "La fase 3", "La fase 1", "Comparar en muchas personas es la fase 3."),
        ("=", "{F} En el ensayo del Texto 2, ¿cuántas personas recibieron el tratamiento habitual?", "2000-1000", "De 2.000 personas, 1.000 recibieron el NT y las otras 1.000 el habitual.", " personas"),
        ("abc", "{F} ¿Por qué el Texto 1 no basta para decir que el NT sirve en personas?", "Porque se hizo en ratones y no en personas", "Porque no tiene números", "Porque es muy largo", "Los resultados en animales no siempre se repiten en personas."),
        ("abc", "{F} ¿Qué medida del Texto 2 hace más parecidos los dos grupos antes de comparar?", "La asignación al azar con grupo de comparación", "El título del artículo", "El tamaño de la letra", "El azar equilibra los grupos y el grupo de comparación permite comparar."),
        ("abc", "{F} El Texto 2 fue financiado por la empresa. ¿Qué es importante revisar?", "Que declaró el interés y publicó todos los resultados, incluidos los efectos adversos", "Que no hay ningún interés", "Que el financiamiento prueba que es falso", "La transparencia permite evaluar el interés económico."),
        ("abc", "{F} ¿Por qué un aviso con solo testimonios no es evidencia?", "Porque no se sabe cuántos casos hay, cómo se midieron ni qué pasó con los demás", "Porque los testimonios son largos", "Porque los clientes siempre mienten", "Un testimonio es una historia individual sin comparación ni medición."),
        ("abc", "{F} Si en el ensayo de 2.000 personas mejoraron 600 en el grupo NT y 400 en el habitual, ¿qué porcentaje mejoró en el grupo NT?", "60 %", "30 %", "40 %", "Son 600 de 1.000, es decir, 60 por cada 100."),
        ("abc", "{F} ¿Qué pregunta haces frente a un titular como «científicos curan el cáncer en ratones»?", "¿En qué fase está y qué pasó en personas?", "¿Cuántos ratones leyeron la noticia?", "¿Qué color tenían los ratones?", "Hay que ver si el resultado llega a ensayos en personas."),
        ("abc", "{F} ¿Qué función cumple la revisión por pares?", "Que especialistas independientes revisen el trabajo antes de publicarlo", "Que dos amigos lo aprueben", "Que la empresa lo corrija", "Es un filtro de calidad aunque no garantiza que no haya errores."),
        ("abc", "{F} Una persona ficticia quiere comprar el «nanotratamiento milagroso» del Texto 3. ¿Qué es lo más adecuado?", "Consultar primero con un profesional de salud y no confiar en un aviso sin datos", "Comprarlo de inmediato", "Recomendarlo a sus amigos", "Un aviso sin evidencia no es una base para decidir sobre la salud."),
        ("abc", "{F} Si un estudio es ciego, esto significa que:", "Las personas no saben a qué grupo fueron asignadas", "Los investigadores no miran los datos", "Todas las personas reciben lo mismo", "Ocultar el grupo evita que las expectativas cambien los resultados."),
    ],
    ctx=("abc", "Contexto: un compañero te cuenta que leyó «la nanomedicina curará todas las enfermedades». ¿Qué respuesta es la más útil?", "Pregunto en qué fase está la evidencia, con qué muestra y quién la financió", "Le digo que es verdad porque está en internet", "Le digo que la ciencia siempre miente", "Las preguntas sobre fase, muestra y fuente permiten evaluar el titular."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un efecto adverso?", "Un efecto no deseado de un tratamiento", "Los efectos adversos deben informarse junto a los beneficios."),
        ("ab", "Un resultado solo en ratones es:", "Un primer paso que debe confirmarse en personas", "Una prueba definitiva", "Muchos tratamientos no funcionan igual en personas."),
        ("ab", "La fase 3 de un ensayo:", "Compara con el tratamiento habitual en muchas personas", "Prueba la seguridad en pocas personas", "La fase 3 busca comparar a gran escala."),
    ],
    op=("Con los textos de la ficha {F} haz lo siguiente: (1) ubica la evidencia de cada texto en una fase o di que no tiene fase; (2) ordena los textos de más a menos confiables con una razón para cada uno; (3) escribe tres preguntas que harías antes de creer un titular sobre un tratamiento nuevo.",
        "(1) Texto 1: preclínica. Texto 2: fase 3. Texto 3: no tiene fase, solo testimonios. (2) Primero el Texto 2, porque tiene grupo de comparación, azar y revisión por pares. Luego el Texto 1, porque es un primer paso en animales. Último el Texto 3, porque no tiene datos. (3) ¿En qué fase está?, ¿cuántas personas tiene el estudio?, ¿quién lo financió y publicó todos los resultados?",
        ["fases bien ubicadas", "orden justificado con criterios de evidencia", "tres preguntas útiles", "no recomienda un tratamiento"],
        ["tres partes numeradas"],
        ["confiar en testimonios", "pensar que ratones equivalen a personas", "descartar el estudio solo por el financiamiento"],
        "Pregunta: «¿qué dato te haría confiar menos en el Texto 2?»."),
    reinforce="Escribe en una frase cada una de las cinco fases de una investigación de un tratamiento.",
    extend="Explica por qué es importante que se publiquen todos los resultados de un ensayo, incluidos los efectos adversos.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 23 (modelos de ejemplo de imagenología, medicina nuclear y farmacología). "
     "Radiografía: los rayos X son absorbidos más por el hueso que por los tejidos blandos, y se forma una imagen con sombras; es una radiación ionizante. "
     "Ecografía: ondas de sonido de alta frecuencia rebotan en los tejidos y su eco forma la imagen; no es radiación ionizante. "
     "Resonancia magnética: un campo magnético y ondas de radio hacen que los átomos de hidrógeno del agua del cuerpo emitan señales; no es radiación ionizante. "
     "Medicina nuclear: un trazador radiactivo se acumula en un órgano y emite radiación que detecta una cámara externa; la radiactividad del trazador disminuye con el tiempo según su semivida. Para un trazador de ejemplo, la semivida es de 6 horas, es decir, cada 6 horas la cantidad de sustancia radiactiva se reduce a la mitad. "
     "Farmacología (modelo llave y cerradura): un medicamento actúa uniéndose a una molécula del cuerpo, llamada receptor, que le corresponde como una llave a su cerradura. Además de su efecto buscado, puede tener efectos adversos.")
build(
    O5, 3, F,
    use="Aprenderé a interpretar modelos físicos y biológicos que explican cómo funcionan la imagenología, la medicina nuclear y los medicamentos. Sirve para entender por qué cada técnica muestra algo distinto y qué riesgos y límites tiene.",
    prior=["Sé que el sonido es una onda.", "Sé que existen los átomos.", "Sé multiplicar y dividir por 2."],
    explain=[
        "Cada técnica de imagen usa un principio físico distinto. La radiografía aprovecha que los rayos X se absorben más en el hueso que en los tejidos blandos. La ecografía usa el eco de ondas de sonido. La resonancia magnética usa un campo magnético y ondas de radio, y muestra bien los tejidos blandos. La radiación ionizante tiene energía suficiente para alterar átomos; por eso se usa solo cuando el beneficio supera el riesgo, y la ecografía y la resonancia no la usan.",
        "La medicina nuclear funciona al revés: el trazador emite radiación desde dentro del órgano y una cámara externa la detecta. Como la radiactividad del trazador disminuye con el tiempo, se habla de semivida: el tiempo en que la cantidad se reduce a la mitad. Con una semivida de 6 horas, queda la mitad a las 6 horas, la cuarta parte a las 12 y la octava parte a las 18. Esto permite que la sustancia desaparezca pronto.",
        "En farmacología, el modelo llave y cerradura explica por qué un medicamento actúa sobre ciertas células: se une a un receptor específico. Los efectos buscados y los adversos dependen de dónde está ese receptor. Todo modelo tiene límites: no dice cuánto, cuándo ni a quién conviene usar un tratamiento. Eso lo decide un profesional de salud con el caso concreto. Este cuaderno no da instrucciones de uso de equipos ni medicamentos.",
    ],
    vocab=[("radiación ionizante", "radiación con energía suficiente para alterar átomos"), ("trazador", "sustancia radiactiva en cantidad muy pequeña que sirve para obtener imágenes"), ("semivida", "tiempo en que una cantidad radiactiva se reduce a la mitad"), ("receptor", "molécula del cuerpo a la que se une un medicamento o una señal"), ("ecografía", "técnica de imagen que usa el eco de ondas de sonido")],
    worked=[
        ("Calcular con la semivida", "Un trazador de ejemplo con semivida de 6 horas parte de 80 unidades. ¿Cuántas quedan a las 12 horas?",
         ["12 horas son dos semividas de 6 horas.", "A las 6 horas quedan 40 y a las 12 horas quedan 20."],
         "20 unidades"),
        ("Elegir la técnica", "Para ver el hueso se usa una técnica que aprovecha que el hueso absorbe más de cierta radiación. ¿Cuál es?",
         ["El hueso absorbe más rayos X que los tejidos blandos.", "La técnica es la radiografía."],
         "Radiografía"),
    ],
    mistakes=[("Creer que toda técnica de imagen usa radiación ionizante.", "La ecografía y la resonancia no la usan.", "Revisa el principio físico de cada una."),
              ("Creer que un medicamento actúa en todas las células por igual.", "Actúa donde está el receptor al que se une.", "Piensa en llave y cerradura: solo actúa donde encaja.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es la semivida de un trazador?", "El tiempo en que la cantidad radiactiva se reduce a la mitad", "El tiempo que dura un examen", "El doble de su cantidad inicial", "La semivida mide la rapidez con que desaparece la radiactividad."),
        ("{F} ¿Qué técnica usa el eco de ondas de sonido para formar la imagen?", "La ecografía", "La ficha dice que la ecografía usa el eco de ondas de sonido."),
        ("ab", "{F} ¿Cuál de estas técnicas no usa radiación ionizante?", "La resonancia magnética", "La radiografía", "La resonancia usa campo magnético y ondas de radio."),
        ("=", "{F} Un trazador de ejemplo parte de 160 unidades. ¿Cuántas quedan después de 6 horas?", "160/2", "Después de una semivida queda la mitad.", " unidades"),
        ("=", "{F} Con el mismo trazador de 160 unidades, ¿cuántas quedan después de 18 horas?", "160/2/2/2", "18 horas son tres semividas, y la cantidad se reduce a la mitad tres veces.", " unidades"),
        ("abc", "{F} ¿Por qué la radiografía muestra bien los huesos?", "Porque los huesos absorben más rayos X que los tejidos blandos", "Porque los huesos emiten sonido", "Porque los huesos son más grandes", "La diferencia de absorción forma la sombra del hueso."),
        ("abc", "{F} En el modelo llave y cerradura, la «cerradura» es:", "El receptor", "El medicamento", "El efecto adverso", "La cerradura es la molécula del cuerpo a la que se une el medicamento."),
        ("abc", "{F} Un medicamento de ejemplo se une a un receptor que está solo en las células del corazón. ¿Qué órganos puede afectar principalmente?", "El corazón", "Los pulmones", "La piel", "El medicamento actúa solo donde está el receptor."),
        ("=", "{F} ¿Cuántas horas pasan hasta que un trazador de ejemplo, con semivida de 6 horas, se reduce a la cuarta parte?", "6*2", "Reducirse a la cuarta parte toma dos semividas, es decir, 12 horas.", " horas"),
        ("abc", "{F} ¿Qué diferencia tiene la ecografía con la radiografía respecto de la radiación?", "La ecografía no usa radiación ionizante y la radiografía sí", "Las dos usan radiación ionizante", "La ecografía usa rayos X y la radiografía ondas de sonido", "La ecografía usa ondas de sonido y la radiografía rayos X, que son ionizantes."),
        ("abc", "{F} Se dice que la medicina nuclear usa un trazador «de semivida corta». ¿Qué ventaja tiene?", "La radiactividad disminuye rápido y la sustancia desaparece pronto", "Que dura para siempre", "Que no emite nada", "Con una semivida corta, la radiactividad baja rápidamente."),
        ("abc", "{F} ¿Qué límite tiene el modelo llave y cerradura?", "No dice cuánto, cuándo ni a quién conviene usar un tratamiento", "No usa palabras", "Solo sirve para la imagenología", "Esas decisiones requieren un profesional de salud."),
        ("abc", "Una persona de ejemplo con dudas sobre un examen de imágenes se pregunta si es riesgoso. ¿Qué corresponde?", "Preguntar al equipo de salud que lo indica sobre el beneficio y el riesgo", "Suponer que siempre es peligroso", "Suponer que no tiene ningún riesgo", "El equipo de salud evalúa beneficio y riesgo según el caso."),
    ],
    ctx=("abc", "Contexto: en una exposición te piden decir por qué hay distintas técnicas de imagen. ¿Qué explicación eliges?", "Cada una usa un principio físico distinto y muestra mejor ciertos tejidos, con riesgos y límites distintos", "Todas hacen lo mismo y solo cambia el precio", "Todas usan rayos X", "Elegir la técnica depende del principio físico, de lo que se quiere ver y del riesgo."),
    sc=[
        ("En Ciencias de la salud: ¿qué es un receptor?", "Una molécula del cuerpo a la que se une un medicamento o una señal", "El receptor es la cerradura del modelo llave y cerradura."),
        ("ab", "La radiación ionizante:", "Tiene energía suficiente para alterar átomos", "No tiene ninguna energía", "Por eso se usa solo si el beneficio supera el riesgo."),
        ("ab", "En la medicina nuclear la cámara:", "Detecta la radiación que emite el trazador", "Emite radiación hacia el cuerpo", "El trazador emite y la cámara externa detecta."),
    ],
    op=("Con los modelos de la ficha {F} haz lo siguiente: (1) arma una tabla con las cuatro técnicas, su principio físico y si usan radiación ionizante; (2) calcula cuánto queda de un trazador de 120 unidades a las 12 horas (semivida de 6 horas); (3) escribe un límite del modelo llave y cerradura.",
        "(1) Radiografía: rayos X, sí. Ecografía: ondas de sonido, no. Resonancia: campo magnético y ondas de radio, no. Medicina nuclear: trazador radiactivo, sí. (2) A las 6 horas quedan 60 y a las 12 horas quedan 30 unidades. (3) No dice cuánto ni a quién conviene el tratamiento.",
        ["tabla con los cuatro principios", "cálculo con dos semividas correcto", "límite razonable del modelo", "no instruye sobre usos clínicos"],
        ["tres partes numeradas"],
        ["decir que todas usan radiación ionizante", "olvidar que la cantidad se reduce a la mitad cada semivida", "usar el modelo como indicación médica"],
        "Pregunta: «¿qué técnica elegirías para ver tejidos blandos sin radiación ionizante y por qué?»."),
    reinforce="Escribe en una frase el principio físico de cada una de las tres técnicas de imagen de la ficha.",
    extend="Explica por qué la elección de una técnica de imagen depende de lo que se quiere ver y del riesgo, y no solo de su costo.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 24 (resultados de ejemplo de un ensayo clínico de un medicamento nuevo, M, frente al tratamiento habitual, H). "
     "Grupo M: 1.000 personas, 600 mejoran según un criterio definido antes de comenzar; 150 tienen un efecto adverso leve; 10 tienen un efecto adverso grave. "
     "Grupo H: 1.000 personas, 400 mejoran con el mismo criterio; 50 tienen un efecto adverso leve; 8 tienen un efecto adverso grave. "
     "Las personas fueron asignadas al azar y no sabían qué grupo les tocó. Los números son de ejemplo y no representan ningún medicamento real.")
build(
    O5, 4, F,
    use="Aprenderé a analizar los resultados de un ensayo clínico calculando diferencias de beneficio y de riesgo, y a ponerlas en conjunto. Sirve para entender cómo se decide si una innovación mejora la calidad de vida.",
    prior=["Sé calcular porcentajes.", "Sé qué es un grupo de comparación.", "Sé restar porcentajes."],
    explain=[
        "En un ensayo clínico se compara un grupo que recibe el tratamiento nuevo con otro que recibe el habitual. Si la asignación fue al azar y las personas no saben qué grupo les tocó, la diferencia se puede atribuir con más seguridad al tratamiento. El beneficio se mide con un criterio definido antes de comenzar, para evitar elegir después el resultado que mejor se vea.",
        "Para comparar, se calcula el porcentaje de cada grupo y su diferencia. En la ficha mejoran el 60 % con M y el 40 % con H: la diferencia absoluta es de 20 puntos porcentuales, que equivale a 20 personas más por cada 100 tratadas. El aumento relativo es la diferencia dividida por el valor de H: 20 sobre 40, es decir, 50 %. Hay que mirar ambos, porque un aumento relativo grande puede significar una diferencia absoluta pequeña.",
        "También se calculan los riesgos: efectos adversos leves del 15 % con M y del 5 % con H, y graves del 1 % y del 0,8 %. Decidir es poner juntos beneficios y riesgos y mirar la incertidumbre, ya que una muestra no es toda la población. Además, el resultado es un promedio y no dice qué pasará en una persona concreta. Las decisiones sobre un tratamiento las toman las personas con su equipo de salud.",
    ],
    vocab=[("diferencia absoluta", "resta entre dos porcentajes o cantidades"), ("aumento relativo", "diferencia dividida por el valor de comparación"), ("criterio de mejoría", "definición, hecha antes del ensayo, de lo que se considera mejorar"), ("riesgo", "probabilidad de que ocurra un efecto no deseado"), ("balance beneficio-riesgo", "comparación entre los beneficios y los riesgos de un tratamiento")],
    worked=[
        ("Diferencia absoluta y relativa", "En un ensayo de ejemplo mejoran 30 % con el tratamiento nuevo y 20 % con el habitual. ¿Cuál es la diferencia absoluta y el aumento relativo?",
         ["La diferencia absoluta es 30 menos 20, es decir, 10 puntos.", "El aumento relativo es 10 dividido por 20, que es 0,5, es decir, 50 %."],
         "10 puntos y 50 %"),
        ("Leer los riesgos", "En otro ensayo de ejemplo, los efectos leves son 8 % con un tratamiento y 2 % con otro. ¿Cuántas personas más por cada 100 tienen efectos leves con el primero?",
         ["La diferencia es 8 menos 2.", "Son 6 puntos porcentuales, es decir, 6 personas más por cada 100."],
         "6 personas más por cada 100"),
    ],
    mistakes=[("Mirar solo el aumento relativo.", "Un aumento relativo grande puede significar una diferencia absoluta pequeña.", "Calcula siempre la diferencia absoluta y el aumento relativo."),
              ("Mirar solo los beneficios.", "Un tratamiento también tiene riesgos que deben compararse con los beneficios.", "Pon juntos beneficios y riesgos antes de decidir.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es el aumento relativo?", "La diferencia dividida por el valor de comparación", "La suma de los dos porcentajes", "El número total de personas", "El aumento relativo mide la diferencia respecto de un valor base."),
        ("=", "{F} ¿Qué porcentaje mejora en el grupo M?", "600/1000*100", "Son 600 de 1.000, es decir, 60 %.", " %"),
        ("=", "{F} ¿Qué porcentaje mejora en el grupo H?", "400/1000*100", "Son 400 de 1.000, es decir, 40 %.", " %"),
        ("=", "{F} ¿Cuál es la diferencia absoluta de mejoría entre M y H, en puntos porcentuales?", "60-40", "La diferencia entre 60 % y 40 % es de 20 puntos.", " puntos porcentuales"),
        ("=", "{F} ¿Cuál es el aumento relativo de mejoría de M respecto a H, en porcentaje?", "(60-40)/40*100", "La diferencia de 20 puntos sobre 40 es 50 %.", " %"),
        ("abc", "{F} Por cada 100 personas tratadas con M en vez de H, ¿cuántas más mejoran?", "20", "50", "10", "La diferencia absoluta es de 20 puntos, que son 20 personas por cada 100."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de efectos adversos leves hay en M que en H?", "150/1000*100-50/1000*100", "Los porcentajes son 15 % y 5 %, y su diferencia es 10 puntos.", " puntos porcentuales"),
        ("abc", "{F} ¿Qué se observa en los efectos graves?", "Hay 10 casos en M y 8 en H, una diferencia pequeña que puede deberse al azar", "No hubo ningún caso", "M tiene muchos más casos graves que H", "La diferencia de 2 casos en 1.000 es pequeña y es incierta."),
        ("abc", "{F} Un titular dice: «M mejora un 50 % más». ¿Qué dato debes agregar para que sea más claro?", "Que son 20 personas más por cada 100, es decir, la diferencia absoluta", "Que el medicamento es nuevo", "Que hay dos grupos", "El aumento relativo debe acompañarse de la diferencia absoluta."),
        ("abc", "{F} ¿Por qué es importante que el criterio de mejoría se defina antes del ensayo?", "Para no elegir después el resultado que mejor se vea", "Para que el ensayo sea más corto", "Para que haya más mejorías", "Fijar el criterio antes evita acomodar la interpretación a lo que se quiere ver."),
        ("abc", "{F} ¿Cuál es una conclusión prudente?", "M se asoció con más mejoría que H, a costa de más efectos leves, y la decisión debe considerar ambos", "M es mejor que H para todas las personas", "M no sirve", "La conclusión pone juntos beneficios y riesgos."),
        ("abc", "{F} Una persona ficticia del grupo H no mejoró. ¿Qué dice el ensayo sobre ella?", "Nada concreto: describe grupos y no predice lo que le pasa a una persona", "Que seguro habría mejorado con M", "Que no se cuidó", "El resultado de un grupo no determina el de una persona concreta."),
        ("abc", "Una persona de ejemplo quiere cambiar su tratamiento por M porque «mejoró 50 % más». ¿Qué corresponde?", "Conversarlo con su equipo de salud, que conoce su caso y los riesgos", "Cambiarlo por su cuenta", "Dejar el tratamiento", "Los cambios de tratamiento los decide el equipo de salud con la persona."),
    ],
    ctx=("abc", "Contexto: una noticia dice «el nuevo medicamento M duplica el éxito». Tienes la ficha. ¿Cómo la comentas con respeto y rigor?", "Digo que mejoran 60 % contra 40 %, que hay más efectos leves, y que la decisión la toma cada persona con su equipo de salud", "Digo que el titular exagera siempre", "Digo que M es mejor para todos", "El comentario incluye cifras absolutas, riesgos y la orientación profesional."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la diferencia absoluta?", "La resta entre dos porcentajes o cantidades", "La diferencia absoluta indica cuántos puntos o personas más hay."),
        ("ab", "El balance beneficio-riesgo:", "Pone juntos los beneficios y los riesgos", "Mira solo los beneficios", "Una decisión informada considera ambos aspectos a la vez."),
        ("ab", "El resultado de un ensayo describe:", "Grupos de personas", "Lo que pasará con cada persona", "No predice lo que le ocurrirá a una persona concreta."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) calcula la diferencia absoluta y el aumento relativo de mejoría y la diferencia de efectos leves; (2) escribe una conclusión de dos oraciones que ponga juntos beneficio y riesgo; (3) nombra una incertidumbre y un dato adicional que pedirías.",
        "(1) Mejoría: 20 puntos y 50 %. Efectos leves: 10 puntos más con M. (2) M se asoció con 20 personas más por cada 100 que mejoran, y con 10 más por cada 100 que tienen efectos leves. La decisión debe considerar ambos. (3) La diferencia en efectos graves es pequeña e incierta. Pediría un seguimiento más largo.",
        ["cálculos correctos", "conclusión que incluye beneficio y riesgo", "incertidumbre razonable", "no da consejos médicos personales"],
        ["tres partes numeradas"],
        ["usar solo el aumento relativo", "olvidar los efectos adversos", "aplicar el resultado a una persona"],
        "Pregunta: «¿qué cambiaría en la conclusión si los efectos graves fueran 30 en M y 8 en H?»."),
    reinforce="Con tus propios números de ejemplo en dos grupos, calcula la diferencia absoluta y el aumento relativo de una mejoría.",
    extend="Explica por qué un aumento relativo grande puede ser engañoso si no se informa la diferencia absoluta.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 25 (opciones de ejemplo para un servicio de salud ficticio con presupuesto limitado). "
     "Opción A, un equipo de ecografía para un consultorio rural. Opción B, un tratamiento biotecnológico de alto costo para unas pocas personas con una enfermedad poco frecuente. "
     "Opción C, un programa de atención a distancia con apoyo de imágenes. Opción D, ampliar el acceso a medicamentos esenciales. "
     "Puntajes de 1 a 3 (3 es mejor) en tres criterios: mejora de la calidad de vida, personas que alcanza y costo accesible. "
     "A: mejora 2, alcance 2, costo 2. B: mejora 3, alcance 1, costo 1. C: mejora 2, alcance 3, costo 2. D: mejora 3, alcance 3, costo 2. "
     "Consideraciones éticas: equidad en el acceso, consentimiento informado, privacidad de los datos y transparencia de intereses.")
build(
    O5, 5, F,
    use="Aprenderé a comparar innovaciones en salud con criterios de calidad de vida, alcance, costo y ética, y a comunicar una decisión con sus límites. Sirve para participar con argumentos en debates sobre tecnología y salud.",
    prior=["Sé sumar puntajes de una tabla.", "Sé qué es una matriz de decisión.", "Sé qué es la equidad."],
    explain=[
        "Evaluar cómo una innovación influye en la calidad de vida exige mirar más que su beneficio para quien la recibe. También importa a cuántas personas llega, cuánto cuesta y qué otras necesidades se dejan de atender con ese dinero. Con presupuesto limitado, elegir una opción es no elegir otra, y por eso se habla de costo de oportunidad: lo que se renuncia al elegir.",
        "La ética orienta la decisión. La equidad pide que el acceso no dependa solo de los recursos de cada persona. El consentimiento informado pide que cada persona decida con información clara. La privacidad protege los datos de salud, y la transparencia pide declarar los intereses económicos. Una opción puede tener gran beneficio para pocas personas, como en la opción B, y aun así ser valiosa. La matriz de decisión ordena la discusión, pero no la reemplaza.",
        "Al comunicar la decisión se dice qué se eligió, con qué criterios, qué beneficios y límites tiene, qué se renunció y cómo se evaluará después. En la ficha, la opción D suma 3 más 3 más 2, es decir, 8 puntos; C suma 7; A suma 6; y B suma 5. Un buen mensaje es respetuoso con las personas que quedaron fuera y abre una forma de revisar la decisión cuando haya nueva evidencia.",
    ],
    vocab=[("costo de oportunidad", "lo que se renuncia al elegir una opción en vez de otra"), ("equidad en el acceso", "que el acceso a una tecnología no dependa solo de los recursos de cada persona"), ("privacidad de los datos", "protección de la información de salud de cada persona"), ("transparencia", "declarar abiertamente los intereses y los datos"), ("enfermedad poco frecuente", "enfermedad que afecta a muy pocas personas")],
    worked=[
        ("Sumar puntajes", "Una opción de ejemplo tiene puntajes 3, 2 y 3. ¿Cuántos puntos suma?",
         ["Se suman los tres puntajes.", "3 más 2 más 3."],
         "8 puntos"),
        ("Costo de oportunidad", "Un servicio de ejemplo gasta todo su presupuesto en un equipo caro. ¿Qué es el costo de oportunidad?",
         ["Es lo que se renuncia al elegir.", "Aquí, otras necesidades que ya no se atenderán con ese dinero."],
         "Lo que se renuncia al elegir esa opción"),
    ],
    mistakes=[("Elegir siempre la opción que llega a más gente.", "Una opción que llega a pocos puede ser muy valiosa para quienes no tienen otra alternativa.", "Considera beneficio, alcance, costo y ética a la vez."),
              ("Creer que la matriz decide sola.", "La matriz ordena la discusión, pero los valores y el contexto también cuentan.", "Presenta la matriz como apoyo y explica los valores en juego.")],
    T=[
        ("abc", "En Ciencias de la salud: ¿qué es el costo de oportunidad?", "Lo que se renuncia al elegir una opción en vez de otra", "El precio de una opción", "El dinero que sobra", "Elegir una opción implica no elegir las demás."),
        ("=", "{F} ¿Cuántos puntos suma la opción A?", "2+2+2", "Se suman 2, 2 y 2.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción B?", "3+1+1", "Se suman 3, 1 y 1.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción C?", "2+3+2", "Se suman 2, 3 y 2.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la opción D?", "3+3+2", "Se suman 3, 3 y 2.", " puntos"),
        ("abc", "{F} Con la suma simple de puntajes, ¿qué opción queda primera?", "Opción D", "Opción B", "Opción A", "D suma 8, C suma 7, A suma 6 y B suma 5."),
        ("abc", "{F} Si el criterio de mejora de la calidad de vida valiera el doble, ¿qué opción quedaría primera entre A, B y C?", "La opción C, que suma 9", "La opción B, que suma 10", "La opción A, que suma 8", "Con mejora doble: A suma 4+2+2=8, B suma 6+1+1=8 y C suma 4+3+2=9."),
        ("abc", "{F} La opción B suma pocos puntos. ¿Qué argumento ético puede sostener que aun así es valiosa?", "Que la equidad implica no dejar sin alternativa a personas con enfermedades poco frecuentes", "Que la matriz es siempre incorrecta", "Que las enfermedades poco frecuentes no importan", "Hay valores como la equidad que no se capturan solo con el alcance."),
        ("abc", "{F} ¿Qué cuidado ético corresponde al usar el programa a distancia (opción C)?", "Proteger la privacidad de los datos de salud y pedir consentimiento informado", "Compartir los datos con quien los pida", "Evitar informar a las personas", "La atención a distancia maneja datos sensibles y requiere consentimiento y reserva."),
        ("abc", "{F} Una empresa que fabrica el tratamiento de la opción B financia un informe que lo recomienda. ¿Qué conviene exigir?", "Que declare su interés y que los datos sean revisables", "Que no se mencione el financiamiento", "Que se descarte sin leerlo", "La transparencia permite evaluar el posible conflicto de interés."),
        ("abc", "{F} Tras elegir D, el servicio comunica la decisión. ¿Qué mensaje es más completo?", "Se eligió D por su beneficio y alcance; se renuncia a otras opciones; se evaluará en un año", "Se eligió D y no se explica nada", "Se eligió D porque es la más cara", "Un buen mensaje incluye razones, renuncias y evaluación posterior."),
        ("abc", "{F} ¿Por qué una decisión como esta debería poder revisarse?", "Porque aparecen nuevos datos y tecnologías, y las necesidades cambian", "Porque la primera decisión siempre es mala", "Porque la ética no importa", "Revisar permite ajustar la decisión cuando cambia la evidencia."),
        ("abc", "Una persona de ejemplo con una enfermedad poco frecuente siente que fue excluida de la decisión. ¿Qué respuesta es más respetuosa?", "Reconocer su situación, explicar los criterios y abrir un canal para revisar cuando haya nueva evidencia", "Decirle que no importa", "Culparla por su enfermedad", "El respeto exige explicar y mantener vías de revisión."),
    ],
    ctx=("abc", "Contexto: tu curso debate cómo debería un servicio de salud ficticio elegir entre dos innovaciones. ¿Qué aporte es más útil?", "Proponer criterios claros, mostrar cómo cambia el resultado según los pesos y considerar equidad y privacidad", "Votar por la que más gusta", "Decidir por la más moderna", "El aporte ordena la discusión con criterios y valores explícitos."),
    sc=[
        ("En Ciencias de la salud: ¿qué es la equidad en el acceso?", "Que el acceso a una tecnología no dependa solo de los recursos de cada persona", "La equidad busca acceso justo, no solo igual."),
        ("ab", "La transparencia en un estudio financiado por una empresa significa:", "Declarar los intereses y los datos", "Ocultar el financiamiento", "Declarar los intereses permite evaluar si el resultado pudo ser influido por ellos."),
        ("ab", "Una matriz de decisión es:", "Un apoyo que no reemplaza el juicio", "Una regla que decide sola", "La decisión también depende de los valores y del contexto."),
    ],
    op=("Con la ficha {F} haz lo siguiente: (1) suma los puntajes de las cuatro opciones; (2) elige una opción y justifica con dos criterios y un valor ético; (3) escribe un mensaje de tres oraciones para comunicar la decisión, con un límite y una forma de revisarla.",
        "(1) A: 6. B: 5. C: 7. D: 8. (2) Elijo D porque suma 8, con alto beneficio y alcance, y por equidad: llega a mucha gente. (3) Se eligió ampliar el acceso a medicamentos esenciales por su beneficio y alcance. Nos limitamos a un año de datos y no atendemos aún a las pocas personas con enfermedades poco frecuentes. Revisaremos la decisión con nueva evidencia.",
        ["puntajes correctos", "elección con dos criterios y un valor ético", "mensaje con límite y revisión", "respeta a las personas que quedan fuera"],
        ["tres partes numeradas"],
        ["decidir sin criterios", "ignorar la ética", "comunicar sin límites ni revisión"],
        "Pregunta: «¿qué harías para apoyar a las personas que quedan fuera de la opción elegida?»."),
    reinforce="Elige dos innovaciones de la ficha y escribe una ventaja y una limitación ética de cada una.",
    extend="Explica con un ejemplo por qué el desarrollo científico puede mejorar la calidad de vida de muchas personas y a la vez ampliar desigualdades si no hay equidad en el acceso.",
)
