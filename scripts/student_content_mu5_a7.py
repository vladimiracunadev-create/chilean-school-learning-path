"""Student material for 5.º básico Música, OA 08 (reflexión sobre fortalezas y áreas de mejora en la audición, la interpretación y la creación, propia y de otros, con respeto y autocrítica).

Todos los casos y comentarios son inventados. Compartir la reflexión personal con otras personas es siempre opcional; ninguna actividad compara personas entre sí.
"""
from __future__ import annotations

from student_content_mu5_a import L
from student_lessons import arith, ex

OA8 = "MU05 OA 08"

# ---------------------------------------------------------------- OA 08 · clase 1 (fortalezas y áreas de mejora con evidencia)
FRA = [
    (1, "Mantengo el pulso parejo en 3 de mis 4 ensayos.", "fortaleza con evidencia"),
    (2, "Entro tarde en el compás 5 en la mitad de mis intentos.", "área de mejora con evidencia"),
    (3, "Soy bueno para la música.", "frase vaga"),
    (4, "Describí una música usando dos rasgos sonoros: tempo e intensidad.", "fortaleza con evidencia"),
    (5, "No me sale nada.", "frase vaga"),
]
FRA_TXT = " ".join(f"Frase {n}: «{t}»" for n, t, _c in FRA)

L(
    OA8, 1,
    f"Lápiz y papel. Frases de ejemplo (inventadas): {FRA_TXT} Ámbitos de la clase: audición (lo que escucho y describo), interpretación (lo que canto o toco) y creación (lo que invento).",
    "Aprenderé a reflexionar sobre lo que hago bien y lo que puedo mejorar en la audición, la interpretación y la creación, apoyándome en evidencia. Sirve para saber qué conservar y qué trabajar.",
    ["Sé escuchar, interpretar y crear música.", "Sé usar criterios para revisar un trabajo.", "Sé que equivocarse es parte de aprender."],
    [
        "Reflexionar es pensar con calma sobre lo que hice. En música hay tres ámbitos: la audición (lo que escucho y describo), la interpretación (lo que canto o toco) y la creación (lo que invento). En cada uno puedes tener fortalezas, que son cosas que haces bien, y áreas de mejora, que son cosas que puedes trabajar más. Tener áreas de mejora no es algo malo: todas las personas las tienen.",
        f"Una buena reflexión tiene tres partes: el ámbito, lo que haces bien o lo que quieres mejorar, y la evidencia, es decir, un dato que lo muestra. Compara las frases de ejemplo: {FRA_TXT} Las frases 1 y 4 son fortalezas con evidencia. La frase 2 es un área de mejora con evidencia. Las frases 3 y 5 son vagas: no dicen qué ni muestran un dato.",
        "Reflexionar con respeto significa tratarte con amabilidad. Reconocer una fortaleza no es presumir, y nombrar una mejora no es castigarte. Compartir tu reflexión con otras personas es voluntario. Y cuando reflexionas sobre el trabajo de otros, hablas de la música, no de la persona.",
    ],
    [("fortaleza", "algo que hago bien"), ("área de mejora", "algo que puedo trabajar más"), ("evidencia", "dato que muestra lo que digo"), ("ámbito", "audición, interpretación o creación"), ("reflexionar", "pensar con calma sobre lo que hice")],
    [
        ("Clasificar una frase", f"{FRA_TXT} ¿La frase 2 es una fortaleza o un área de mejora?", ["Habla de entrar tarde en el compás 5.", "Es algo que puede trabajarse."], "Un área de mejora"),
        ("Reconocer la evidencia", f"{FRA_TXT} ¿Qué dato da la frase 1 como evidencia?", ["Dice cuántos ensayos salieron con el pulso parejo.", "Son 3 de 4 ensayos."], "3 de 4 ensayos con el pulso parejo"),
    ],
    [
        ("Decir «soy malo» o «soy bueno» sin dar ejemplos.", "No muestra qué ni cuándo.", "Escribe qué hiciste y un dato que lo muestre."),
        ("Pensar que nombrar una mejora es una crítica a uno mismo.", "Todas las personas tienen áreas de mejora y se trabajan.", "Nómbrala con amabilidad y plantea cómo mejorar."),
    ],
    [
        ex("¿Cuáles son los tres ámbitos de la clase?", "Audición, interpretación y creación", "Son los que nombra la clase."),
        ex(f"{FRA_TXT} ¿La frase 3 da una evidencia?", "No", "Dice «soy bueno» sin ningún dato."),
        ex("¿Una fortaleza es algo que haces bien o algo que debes mejorar?", "Algo que haces bien", "Las áreas de mejora son lo que se trabaja."),
    ],
    [
        ex(f"{FRA_TXT} ¿Cuántas frases son fortalezas con evidencia?", "2", "Son la frase 1 y la frase 4."),
        ex(f"{FRA_TXT} ¿Cuántas frases son vagas?", "2", "Son la frase 3 y la frase 5."),
        ex(f"{FRA_TXT} ¿En qué ámbito está la frase 4: audición, interpretación o creación?", "Audición", "Describir una música que se escucha es audición."),
    ],
    [
        ex(f"{FRA_TXT} ¿En qué ámbito está la frase 2?", "Interpretación", "Entrar en un compás al tocar o cantar es interpretación."),
        arith(f"{FRA_TXT} La frase 2 dice que entra tarde la mitad de sus intentos. Si hizo 8 intentos, ¿en cuántos entró tarde?", "8//2", "La mitad de 8 es 4.", " intentos"),
        ex("Reescribe «Soy bueno para la música» como una fortaleza con evidencia. ¿Qué dato falta?", "Un dato que lo muestre, como cuántas veces o en qué actividad", "La evidencia convierte la frase en una fortaleza con base."),
    ],
    [
        ex("Ana dice: «Soy malo en música porque me equivoqué una vez». ¿Qué error comete al reflexionar?", "Generaliza desde un solo dato", "Una equivocación no define todo lo que haces."),
        ex("Luis dice que reconocer sus fortalezas es presumir. ¿Es cierto?", "No", "Reconocer lo que haces bien ayuda a conservarlo."),
    ],
    [
        arith("En un curso de 30 estudiantes, 12 escribieron una fortaleza con evidencia y 9 un área de mejora con evidencia. Los demás escribieron frases vagas. ¿Cuántos escribieron frases vagas?", "30-12-9", "Se restan los dos grupos del total.", " estudiantes"),
        arith("Un estudiante revisa 4 ensayos y en 3 mantuvo el pulso. ¿En cuántos no lo mantuvo?", "4-3", "Se resta lo logrado del total.", " ensayo"),
    ],
    [ex("Después de crear un ritmo, una niña escribe: «Mi ritmo cumplió las 3 reglas de la consigna, pero me faltó ensayar el cambio de la sección B». ¿Esa frase incluye una fortaleza y un área de mejora?", "Sí", "La primera parte es una fortaleza y la segunda es un área de mejora.")],
    [ex("En Música: ¿Qué es la evidencia?", "Un dato que muestra lo que digo", "Sostiene la reflexión."), ex("¿Todas las personas tienen áreas de mejora?", "Sí", "Forman parte de aprender."), ex("¿Con quién debo compartir mi reflexión?", "Con quien yo quiera, es voluntario", "La reflexión personal es opcional compartirla.")],
    (
        "Escribe una reflexión de tres frases sobre tu trabajo musical de este año: una fortaleza con evidencia en un ámbito, un área de mejora con evidencia en otro ámbito y un plan de una línea para mejorar. Puedes usar las frases de la clase como modelo. Compartirla es voluntario.",
        "Fortaleza (audición): describo la música con dos rasgos sonoros en 4 de 5 escuchas. Mejora (interpretación): entro tarde en el compás 5 en 4 de 8 intentos. Plan: practicaré ese compás más lento.",
        ["una fortaleza con evidencia", "un área de mejora con evidencia", "un plan de una línea", "tono respetuoso"],
        ["texto escrito"],
        ["frases vagas", "tono duro con uno mismo"],
        "Reconoce la reflexión y pide la evidencia de cada frase; no obliga a compartirla.",
    ),
    "Escribe una frase que empiece con «Mi fortaleza es…».",
    "Escribe una reflexión sobre una actividad musical que hiciste en la semana.",
)

# ---------------------------------------------------------------- OA 08 · clase 2 (comentar el trabajo de otros con respeto)
COM = [
    (1, "Tu melodía terminó en una nota que se sentía como llegada; podrías probar un crescendo antes del final.", {"respetuoso", "específico", "útil"}),
    (2, "Lo hiciste horrible.", set()),
    (3, "Estuvo bien.", {"respetuoso"}),
    (4, "Eres lento para aprender.", set()),
    (5, "El pulso se aceleró en el compás 6; ¿pueden ensayarlo más lento?", {"respetuoso", "específico", "útil"}),
]
COM_TXT = " ".join(f"Comentario {n}: «{t}»" for n, t, _s in COM)
COM_OK = [n for n, _t, s in COM if len(s) == 3]

L(
    OA8, 2,
    f"Lápiz y papel. Criterios de un buen comentario: respetuoso (no ataca a la persona), específico (nombra algo de la música) y útil (dice qué conservar o qué mejorar). Comentarios de ejemplo (inventados): {COM_TXT}",
    "Aprenderé a comentar el trabajo musical de otras personas con respeto: hablar de la música, nombrar algo concreto y decir cómo mejorar con amabilidad. Sirve para ayudar a otros a crecer y recibir ayuda de los demás.",
    ["Sé que hay fortalezas y áreas de mejora.", "Sé escuchar con respeto.", "Sé describir la música con rasgos sonoros."],
    [
        "Comentar el trabajo de otras personas es una forma de ayudar. Un buen comentario cumple tres criterios. Es respetuoso: habla de la música y no ataca a la persona. Es específico: nombra algo concreto de lo que se oyó, como el pulso, la dinámica o una entrada. Y es útil: dice qué conviene conservar o cómo se podría mejorar.",
        f"Revisa los comentarios de ejemplo: {COM_TXT} Los comentarios 1 y 5 cumplen los tres criterios: hablan de la música, nombran algo concreto y sugieren qué probar. El comentario 3 es respetuoso, pero no es específico ni útil. Los comentarios 2 y 4 no son respetuosos: el 2 descalifica y el 4 habla de la persona, no de la música.",
        "También es importante recibir comentarios. Escucha sin interrumpir, pregunta si no entendiste y agradece. No tienes que estar de acuerdo con todo, pero sí escuchar. Y si un comentario te hiere, puedes decirlo con calma y pedir que hable de la música. Una forma útil de comentar es empezar por algo que funcionó, nombrar una cosa a mejorar y proponer una idea.",
    ],
    [("comentario", "opinión sobre un trabajo musical"), ("respetuoso", "habla de la música y no ataca a la persona"), ("específico", "nombra algo concreto de lo que se oyó"), ("útil", "dice qué conservar o cómo mejorar"), ("sugerencia", "idea amable para mejorar")],
    [
        ("Evaluar un comentario", f"Comentario 3: «{COM[2][1]}». ¿Cumple los tres criterios de la clase?", ["Es respetuoso.", "No nombra nada concreto.", "No dice cómo mejorar."], "No: es respetuoso pero no es específico ni útil"),
        ("Transformar un comentario", "«Lo hiciste horrible.» ¿Qué comentario lo reemplaza mejor: (a) «Me costó escuchar la melodía; ¿pueden tocar la percusión más suave?» o (b) «Ni lo intentes»?", ["Hay que hablar de la música.", "Hay que dar una idea para mejorar."], "(a)"),
    ],
    [
        ("Decir «lo hiciste mal» sin explicar.", "No dice qué ni cómo mejorar y puede herir.", "Nombra algo concreto y propone una idea."),
        ("Hablar de cómo es la persona en vez de la música.", "El comentario debe ser sobre el trabajo.", "Cambia «eres…» por «en la música se oyó…»."),
    ],
    [
        ex("¿Cuáles son los tres criterios de un buen comentario?", "Respetuoso, específico y útil", "Son los de la clase."),
        ex(f"{COM_TXT} ¿El comentario 2 es respetuoso?", "No", "Descalifica en vez de hablar de la música."),
        ex("Un comentario dice «el pulso se aceleró en el compás 6». ¿Es específico?", "Sí", "Nombra un rasgo y un lugar concretos."),
    ],
    [
        ex(f"{COM_TXT} ¿Cuántos comentarios cumplen los tres criterios?", str(len(COM_OK)), "Son el 1 y el 5."),
        ex(f"{COM_TXT} ¿Cuál es el único criterio que cumple el comentario 3?", "Respetuoso", "No es específico ni útil."),
        ex(f"{COM_TXT} ¿Por qué el comentario 4 no es respetuoso?", "Habla de la persona y no de la música", "El comentario debe ser sobre el trabajo."),
    ],
    [
        ex("Un compañero tocó una melodía y se atrasó en el compás 3. ¿Qué comentario cumple los tres criterios: (a) «Se atrasó en el compás 3; ¿probamos ese compás más lento?» o (b) «Estuvo mal»?", "(a)", "Es respetuoso, específico y útil."),
        ex("Quieres comentar una creación que tuvo un motivo claro que volvía. ¿Qué dices primero según la clase: algo que funcionó o algo a mejorar?", "Algo que funcionó", "Empezar por lo que funcionó ayuda a recibir mejor la sugerencia."),
        arith("En un curso, cada estudiante comenta el trabajo de 2 compañeros. Si hay 24 estudiantes, ¿cuántos comentarios se hacen?", "24*2", "Se multiplican los estudiantes por los comentarios de cada uno.", " comentarios"),
    ],
    [
        ex("Pedro dice que ser sincero significa decir «lo hiciste mal». ¿Es necesario ser cruel para ser sincero?", "No", "Se puede ser sincero y respetuoso a la vez."),
        ex("Ana recibe un comentario que no le gusta. ¿Qué es mejor: (a) escuchar, preguntar si no entendió y agradecer o (b) interrumpir y enojarse?", "(a)", "Escuchar permite aprender del comentario."),
    ],
    [
        arith("En un grupo de 6 personas, cada una da 1 comentario a cada otra persona. ¿Cuántos comentarios se dan en total?", "6*5", "Cada una comenta a 5 personas.", " comentarios"),
        arith("Un curso recibe 40 comentarios. 28 cumplieron los tres criterios y el resto, no. ¿Cuántos no los cumplieron?", "40-28", "Se resta del total.", " comentarios"),
    ],
    [ex("Una niña se queda en silencio cuando tocó un compañero porque «no sabe qué decirle». ¿Qué puede decir según la clase?", "Algo que funcionó y una sugerencia concreta", "Un comentario específico y útil ayuda.")],
    [ex("¿Un comentario debe hablar de la música o de la persona?", "De la música", "Es la clave del respeto."), ex("¿Qué haces al recibir un comentario?", "Escucho y agradezco", "Es parte de aprender."), ex("¿Qué pasa si un comentario te hiere?", "Puedo decirlo con calma y pedir que hable de la música", "Se cuida el respeto.")],
    (
        "Elige un trabajo musical (una creación del curso, un ritmo de un compañero o uno inventado como: «una melodía de 6 notas que termina en 1 y tiene un crescendo al final»). Escribe un comentario con los tres criterios: algo que funcionó, algo concreto a mejorar y una sugerencia. Revisa que no hable de la persona. Compartirlo con alguien es voluntario.",
        "«El final de tu melodía, con crescendo, se sintió muy claro. Al comienzo el pulso se aceleró un poco; ¿pueden ensayar el inicio más lento?»",
        ["algo que funcionó", "algo concreto a mejorar", "una sugerencia", "habla de la música"],
        ["comentario escrito"],
        ["decir «bien» o «mal» sin dar detalles", "hablar de cómo es la persona"],
        "Reconoce los tres criterios y pide revisar que cada frase hable de la música y no de la persona.",
    ),
    "Escribe un comentario respetuoso sobre una canción que escuchaste.",
    "Reescribe «Qué fome» como un comentario respetuoso y útil.",
)

# ---------------------------------------------------------------- OA 08 · clase 3 (autocrítica con datos)
INT = [(1, 6), (2, 4), (3, 4), (4, 1)]
INT_TXT = " ".join(f"Intento {n}: {e} errores." for n, e in INT)
MEJOR = max(range(1, len(INT)), key=lambda i: INT[i - 1][1] - INT[i][1]) + 1

L(
    OA8, 3,
    f"Lápiz y papel. Registro de un estudiante que ensaya una pieza de 8 compases (inventado): {INT_TXT} Un «error» es un compás que no salió como en la partitura.",
    "Aprenderé a evaluar mi propio trabajo con honestidad y amabilidad, usando datos de mis intentos y comparándome con mi intento anterior, no con otras personas. Sirve para ver cuánto avancé y qué falta.",
    ["Sé registrar intentos.", "Sé restar números.", "Sé nombrar fortalezas y áreas de mejora."],
    [
        "La autocrítica es revisar tu propio trabajo con honestidad. No es criticarse con dureza ni decir que todo está perfecto. Es mirar qué salió bien, qué no salió bien y por qué. Una buena autocrítica se apoya en datos: cuántos errores hubo, en qué compás, en qué intento. Con datos, puedes ver tu avance con claridad.",
        f"Mira el registro de ejemplo: {INT_TXT} El estudiante pasó de 6 errores a 1 en 4 intentos, o sea, redujo 5 errores. Entre el intento 1 y el 2 redujo 2 errores; entre el 2 y el 3 no hubo cambio; entre el 3 y el 4 redujo 3 errores. El mayor avance ocurrió en el intento {MEJOR}. Esto permite decir con evidencia: «Avancé, aunque en el intento 3 me estanqué».",
        "Cuando analices tu progreso, compárate contigo mismo: tu intento de hoy con el de ayer. Compararte con otras personas no sirve, porque cada persona parte de un lugar distinto. Y si un intento sale peor, no es un fracaso: es información para mejorar. Reconoce lo que avanzaste y nombra una cosa concreta para el siguiente intento.",
    ],
    [("autocrítica", "revisar mi trabajo con honestidad"), ("dato", "número o hecho que muestra lo que pasó"), ("avance", "mejora respecto del intento anterior"), ("estancarse", "no avanzar entre un intento y otro"), ("progreso", "cambio a lo largo de varios intentos")],
    [
        ("Calcular el avance", f"{INT_TXT} ¿Cuántos errores se redujeron entre el intento 1 y el intento 4?", ["En el intento 1 hubo 6 errores.", "En el intento 4 hubo 1.", "6 − 1 = 5."], "5 errores"),
        ("Encontrar el estancamiento", f"{INT_TXT} ¿Entre qué intentos no hubo cambio?", ["Intento 2: 4 errores.", "Intento 3: 4 errores.", "No cambió."], "Entre el 2 y el 3"),
    ],
    [
        ("Compararse con quien toca mejor.", "Cada persona parte de un lugar distinto.", "Compara tu intento de hoy con el de ayer."),
        ("Decir que todo salió perfecto o que todo salió mal.", "No es honesto ni se apoya en datos.", "Nombra lo que salió bien y lo que no, con números."),
    ],
    [
        ex(f"{INT_TXT} ¿Cuántos errores hubo en el intento 2?", "4", "Lo dice el registro."),
        ex("¿Con quién conviene compararse para ver tu avance: con tu intento anterior o con otra persona?", "Con mi intento anterior", "Cada persona parte de un lugar distinto."),
        ex("Un intento sale peor que el anterior. ¿Es un fracaso o información para mejorar?", "Información para mejorar", "Muestra qué ajustar."),
    ],
    [
        ex(f"{INT_TXT} ¿Entre qué dos intentos seguidos fue mayor la reducción de errores?", f"Entre el {MEJOR - 1} y el {MEJOR}", "Pasó de 4 a 1, una reducción de 3."),
        ex(f"{INT_TXT} ¿Cuántos errores se redujeron entre el intento 1 y el intento 2?", "2", "Pasó de 6 a 4."),
        ex("Una autocrítica honesta, ¿nombra solo lo bueno, solo lo malo o ambas cosas con datos?", "Ambas cosas con datos", "Ayuda a ver el avance y lo que falta."),
    ],
    [
        arith(f"{INT_TXT} ¿Cuántos errores hubo en total sumando los cuatro intentos?", "6+4+4+1", "Se suman los errores de los cuatro intentos.", " errores"),
        arith(f"{INT_TXT} La pieza tiene 8 compases. En el intento 4, ¿cuántos compases salieron sin error?", "8-1", "Se resta el error de los 8 compases.", " compases"),
        ex(f"{INT_TXT} ¿Entre qué dos intentos seguidos hubo la menor reducción de errores?", "Entre el 2 y el 3", "No cambió el número de errores."),
    ],
    [
        ex("Luis dice: «Mi compañera tuvo solo 1 error al primer intento, yo tuve 6; soy malo». ¿Qué error comete?", "Se compara con otra persona en vez de con su propio avance", "Cada persona parte de un lugar distinto."),
        ex(f"{INT_TXT} Ana dice que no avanzó nada. ¿Qué dato lo contradice?", "Pasó de 6 a 1 error", "El registro muestra una reducción de 5 errores."),
    ],
    [
        arith("Un estudiante tuvo 10 errores el lunes y 3 el viernes. ¿Cuántos errores redujo?", "10-3", "Se resta de lo que tenía antes.", " errores"),
        arith("Otro estudiante tuvo 9 errores el primer intento y redujo 2 errores por intento durante 4 intentos. ¿Cuántos errores tuvo en el último intento?", "9-2*4", "Se resta lo que redujo en total.", " error"),
    ],
    [ex("Un niño anota: «En el intento 3 no avancé, pero en el 4 corregí el compás 6». ¿Esa frase se apoya en datos y es amable consigo mismo?", "Sí", "Nombra un dato concreto y un avance, sin castigarse.")],
    [ex("En una autocrítica, ¿qué es un dato?", "Un número o hecho que muestra lo que pasó", "Sirve de evidencia."), ex("¿Con quién te comparas para ver tu avance?", "Contigo mismo", "Compara intento con intento."), ex("¿Un intento peor es un fracaso?", "No", "Es información para mejorar.")],
    (
        "Elige una pieza breve o un ritmo y haz 4 intentos. En cada intento anota cuántos errores tuviste. Calcula cuánto avanzaste entre el primero y el último y entre qué intentos fue el mayor avance. Escribe una autocrítica de 3 frases: una cosa que salió bien (con dato), una cosa que falta (con dato) y una acción amable para el siguiente intento. Compartirla es voluntario.",
        "Intentos: 5, 3, 3, 2 errores. Avancé 3 errores. Mayor avance: del intento 1 al 2. Salió bien: bajé de 5 a 2 errores. Falta: el compás 6 sigue fallando. Próxima acción: practicarlo más lento.",
        ["registra cuatro intentos con números", "calcula el avance total", "escribe una autocrítica con datos y amable"],
        ["registro escrito", "cálculo", "texto breve"],
        ["compararse con otros", "no usar datos"],
        "Reconoce el registro y pide justificar cada frase con un número; valora el tono amable.",
    ),
    "Anota cuántos errores tuviste hoy en un ensayo.",
    "Haz dos intentos más y calcula si seguiste avanzando.",
)

# ---------------------------------------------------------------- OA 08 · clase 4 (plan de mejora)
METAS = [
    (1, "Mejorar mucho.", set()),
    (2, "Entrar a tiempo en el compás 5 en 4 de 5 intentos antes del viernes.", {"concreta", "medible", "con plazo"}),
    (3, "Practicar más.", {"concreta"}),
    (4, "Bajar de 4 a 1 error en la sección B en una semana.", {"concreta", "medible", "con plazo"}),
]
METAS_TXT = " ".join(f"Meta {n}: «{t}»" for n, t, _s in METAS)
META_OK = [n for n, _t, s in METAS if len(s) == 3]

L(
    OA8, 4,
    f"Lápiz y papel; un calendario o una hoja con los días de la semana. Una buena meta es concreta (dice qué), medible (dice cuánto) y con plazo (dice cuándo). Metas de ejemplo (inventadas): {METAS_TXT}",
    "Aprenderé a fijar una meta de mejora y a planificar la práctica para cumplirla, y a revisar el progreso. Sirve para convertir una reflexión en acciones concretas.",
    ["Sé reconocer fortalezas y áreas de mejora.", "Sé registrar intentos con datos.", "Sé sumar y multiplicar."],
    [
        "Después de reflexionar, el siguiente paso es planificar. Una meta de mejora tiene tres características: es concreta, porque dice qué voy a mejorar; es medible, porque dice cuánto o cuántas veces; y tiene plazo, porque dice para cuándo. «Mejorar mucho» no sirve, porque no es concreta ni medible ni tiene plazo.",
        f"Revisa las metas de ejemplo: {METAS_TXT} La meta 2 cumple los tres criterios: dice qué (entrar a tiempo en el compás 5), cuánto (4 de 5 intentos) y cuándo (antes del viernes). La meta 4 también los cumple. La meta 1 no cumple ninguno. La meta 3 («practicar más») apenas dice qué hacer y no dice cuánto ni cuándo.",
        "Con una buena meta, se arma un plan de práctica. Por ejemplo: 3 días a la semana, 10 minutos cada día. Se registra cada práctica y se revisa al final del plazo. Si no se cumplió la meta, no pasa nada: se analiza qué ajustar y se fija una nueva. Si se cumplió, se celebra el avance y se fija un nuevo desafío.",
    ],
    [("meta", "lo que quiero lograr"), ("concreta", "dice qué voy a mejorar"), ("medible", "dice cuánto o cuántas veces"), ("plazo", "dice para cuándo"), ("plan de práctica", "días y minutos para lograr la meta")],
    [
        ("Evaluar una meta", f"Meta 2: «{METAS[1][1]}». ¿Es concreta, medible y con plazo?", ["Qué: entrar a tiempo en el compás 5.", "Cuánto: en 4 de 5 intentos.", "Cuándo: antes del viernes."], "Sí, cumple los tres criterios"),
        ("Calcular una práctica", "Un plan tiene 3 días de práctica a la semana, 10 minutos cada día. ¿Cuántos minutos practica en 2 semanas?", ["En una semana: 3 × 10 = 30 minutos.", "En 2 semanas: 30 × 2 = 60."], "60 minutos"),
    ],
    [
        ("Fijar una meta sin plazo.", "Nunca se sabe si se cumplió.", "Agrega para cuándo quieres lograrla."),
        ("Abandonar el plan porque un día no se pudo practicar.", "Un día perdido no arruina el plan.", "Retómalo al día siguiente."),
    ],
    [
        ex("¿Cuáles son las tres características de una buena meta?", "Concreta, medible y con plazo", "Son las de la clase."),
        ex(f"{METAS_TXT} ¿La meta 1 es medible?", "No", "«Mejorar mucho» no dice cuánto."),
        ex("Si no se cumplió la meta, ¿qué se hace: analizar qué ajustar o abandonar?", "Analizar qué ajustar", "El plan se mejora con lo aprendido."),
    ],
    [
        ex(f"{METAS_TXT} ¿Cuántas metas cumplen los tres criterios?", str(len(META_OK)), "Son la 2 y la 4."),
        ex(f"{METAS_TXT} ¿Qué le falta a la meta 3 («practicar más»)?", "Que diga cuánto y para cuándo", "Falta lo medible y el plazo."),
        ex(f"{METAS_TXT} ¿Cuál es el plazo de la meta 4?", "Una semana", "Lo dice la meta."),
    ],
    [
        arith("Un plan: 4 días a la semana, 15 minutos por día. ¿Cuántos minutos practica en una semana?", "4*15", "Se multiplican los días por los minutos.", " minutos"),
        arith("Un estudiante quiere practicar en total 90 minutos en 3 semanas. ¿Cuántos minutos debe practicar por semana, si reparte por igual?", "90//3", "Se reparte el total en 3 semanas.", " minutos"),
        ex("Un estudiante tiene 4 errores y quiere bajar a 1. ¿Cuántos errores debe reducir?", "3", "4 menos 1 son 3 errores."),
    ],
    [
        ex("Reescribe «Practicar más» como una meta concreta, medible y con plazo. ¿Cuál opción lo hace: (a) «Practicar 10 minutos, 3 días a la semana, durante dos semanas» o (b) «Practicar cuando pueda»?", "(a)", "Dice cuánto, cuántas veces y por cuánto tiempo."),
        ex("Un niño cumplió su meta antes del plazo. ¿Qué conviene hacer: celebrar el avance y fijar un nuevo desafío o dejar de practicar?", "Celebrar el avance y fijar un nuevo desafío", "El plan de mejora es un ciclo."),
    ],
    [
        arith("Un grupo de 24 estudiantes fija una meta cada uno. 18 metas cumplen los tres criterios. ¿Cuántas faltan por mejorar?", "24-18", "Se restan las bien formuladas del total.", " metas"),
        arith("Un estudiante practica 3 días por semana, 10 minutos cada vez, durante 4 semanas. ¿Cuántos minutos practicó?", "3*10*4", "Se multiplican días, minutos y semanas.", " minutos"),
    ],
    [ex("Después de reflexionar, un niño decide: «Voy a practicar 10 minutos, 3 días a la semana, hasta el viernes de la próxima semana para entrar a tiempo en el compás 5». ¿Esa decisión incluye un plan y una meta?", "Sí", "Dice qué practicar, cuánto y hasta cuándo.")],
    [ex("¿Qué es una meta medible?", "La que dice cuánto o cuántas veces", "Se puede comprobar."), ex("¿Qué haces si no cumples una meta?", "Analizo y ajusto el plan", "El plan se mejora."), ex("¿Qué haces si la cumples?", "La celebro y fijo un nuevo desafío", "El ciclo sigue.")],
    (
        "Fija una meta de mejora para tu audición, tu interpretación o tu creación. Escribe la meta con los tres criterios (qué, cuánto y cuándo), un plan de práctica con días y minutos (calcula cuántos minutos serán en total) y cómo revisarás si la cumpliste. Compartir tu meta es voluntario.",
        "Meta: entrar a tiempo en el compás 5 en 4 de 5 intentos antes del viernes. Plan: 3 días, 10 minutos cada día (30 minutos en la semana). Revisión: anotaré cada intento y contaré cuántos salieron bien.",
        ["la meta es concreta, medible y con plazo", "el plan tiene días y minutos con total correcto", "dice cómo revisará el cumplimiento"],
        ["meta escrita", "plan con cálculo"],
        ["meta sin plazo", "plan sin forma de revisar"],
        "Reconoce la meta y pide mostrar el cálculo de minutos; recuerda que compartirla es voluntario.",
    ),
    "Escribe una meta que cumpla con qué, cuánto y cuándo.",
    "Revisa tu meta de la semana pasada y anota si se cumplió.",
)
