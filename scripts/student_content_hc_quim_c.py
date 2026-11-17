"""Química (electivo 3.º y 4.º medio HC): OAC-05 (contaminantes químicos y servicios ecosistémicos, clases 1 a 6) y OAC-06 (aportes de la química a la mitigación y la restauración, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado o en la ficha de la clase. Los valores de referencia son inventados para practicar y no reemplazan normas oficiales. "
             "Este cuaderno no propone experimentos, mezclas ni procedimientos con sustancias: los resultados que se analizan vienen ya escritos y los cálculos se hacen en papel. "
             "Las masas atómicas y las constantes que se usan se entregan en cada ficha. Si sospechas que el agua, el aire o el suelo de tu casa o de tu barrio están contaminados, avisa a una persona adulta de confianza y a la autoridad de salud; no manipules ni pruebes sustancias por tu cuenta.")
build = make_build(MATERIALS)

O5 = "CN-QUIM-3y4-OAC-05"
O6 = "CN-QUIM-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (datos de ejemplo). Fuente puntual: lugar identificable de descarga, como una tubería o una chimenea. Fuente difusa: llegada repartida en un área, como el agua que escurre desde campos o desde el pavimento de una ciudad. "
     "Casos: C1: relave (residuo sólido molido) de una faena minera con cobre, que puede filtrarse al agua; C2: fertilizantes con nitrato y fosfato que la lluvia arrastra desde campos de cultivo hacia un río; C3: aceites y metales de los vehículos que la lluvia lava desde el pavimento de una ciudad; C4: aguas servidas domésticas con detergentes y materia orgánica descargadas por una tubería. "
     "Servicios ecosistémicos: de provisión (agua, alimento), de regulación (por ejemplo, un humedal depura el agua) y culturales (recreación). Carga contaminante = concentración (mg/L) × caudal (L/s), en mg/s. Tubería de ejemplo: 5 mg/L de un contaminante X y caudal de 100 L/s.")
build(
    O5, 1, F,
    use="Aprenderé a delimitar el sistema y la pregunta para analizar el origen de contaminantes químicos de actividades domésticas e industriales (minería, agricultura, desarrollo urbano) y qué servicios ecosistémicos pueden verse afectados. Sirve para ordenar el análisis antes de medir.",
    prior=["Sé qué es una concentración.", "Sé multiplicar y convertir unidades de tiempo.", "Sé que los ecosistemas dan beneficios a las personas."],
    explain=[
        "Un contaminante químico es una sustancia que, por su cantidad o su lugar, daña a los seres vivos o al ambiente. Puede venir de actividades domésticas, como los detergentes y las aguas servidas, o industriales, como la minería, la agricultura y el desarrollo urbano. Según cómo llega al ambiente, la fuente puede ser puntual, si sale de un lugar identificable, o difusa, si llega repartida por un área.",
        "Los sistemas naturales prestan servicios ecosistémicos, que son los beneficios que las personas obtienen de ellos. Los de provisión incluyen agua y alimento; los de regulación, por ejemplo la depuración del agua por un humedal; y los culturales, como la recreación. Un contaminante importa, entre otras razones, porque puede deteriorar uno o varios de estos servicios.",
        "Para investigar se delimita el sistema, es decir, qué contaminante, qué fuente, qué ambiente y qué servicio se estudian. Una medida básica es la carga contaminante, que se calcula como concentración por caudal y da la cantidad que sale por unidad de tiempo. Una pregunta como «¿contamina la minería?» es demasiado amplia; una pregunta delimitada nombra un contaminante, una fuente, un lugar y una variable medible.",
    ],
    vocab=[("contaminante", "sustancia que por su cantidad o lugar daña a los seres vivos o al ambiente"), ("fuente puntual", "lugar identificable de descarga de un contaminante"), ("fuente difusa", "llegada de un contaminante repartida en un área"), ("servicio ecosistémico", "beneficio que las personas obtienen de un ecosistema"), ("carga contaminante", "cantidad de contaminante que sale por unidad de tiempo: concentración por caudal")],
    worked=[
        ("Clasificar la fuente", "Una tubería descarga aguas servidas de un pueblo en un río. ¿La fuente es puntual o difusa?",
         ["Se puede señalar un lugar exacto de descarga: la tubería.", "Eso corresponde a una fuente puntual.", "Una fuente difusa llegaría repartida en un área."],
         "Puntual"),
        ("Carga contaminante", "Una descarga de ejemplo tiene 8 mg/L de un contaminante y un caudal de 50 L/s. ¿Cuál es la carga en mg/s?",
         ["Carga = concentración × caudal.", "8 × 50.", "El resultado es 400 mg/s."],
         "400 mg/s"),
    ],
    mistakes=[("Decir que una actividad entera, como la minería, «es» un contaminante.", "Una actividad puede generar contaminantes específicos; lo que se evalúa es qué sustancia, cuánta y por qué vía llega.", "Nombra el contaminante, la fuente y el ambiente."),
              ("Confundir concentración con carga.", "La concentración es cuánto hay por litro; la carga incluye el caudal y dice cuánto sale por segundo.", "Multiplica concentración por caudal para obtener la carga.")],
    T=[
        ("abc", "En Química: ¿qué es una fuente puntual de contaminación?", "Un lugar identificable de descarga, como una tubería", "Una llegada repartida en un área grande", "Un contaminante de origen natural", "La fuente puntual se puede señalar en un punto exacto."),
        ("{F} ¿Qué caso (C1, C2, C3 o C4) es una fuente difusa de origen agrícola?", "C2", "La lluvia arrastra los fertilizantes desde campos completos, repartidos en un área."),
        ("{F} ¿Qué caso es una fuente puntual de origen doméstico?", "C4", "Las aguas servidas salen por una tubería, que es un punto identificable."),
        ("abc", "{F} En el caso C3, ¿qué tipo de fuente es el pavimento de una ciudad lavado por la lluvia?", "Difusa", "Puntual", "Natural", "La lluvia lava un área extensa, de modo que la llegada está repartida."),
        ("=", "{F} ¿Cuál es la carga contaminante de la tubería de ejemplo, en mg/s?", "5*100", "Se multiplica la concentración por el caudal.", " mg/s"),
        ("=", "{F} ¿Cuántos mg del contaminante X salen de la tubería de ejemplo en un minuto (60 s)?", "5*100*60", "Se multiplica la carga por los 60 segundos de un minuto.", " mg"),
        ("abc", "{F} Un humedal depura el agua de un río. ¿Qué tipo de servicio ecosistémico es?", "De regulación", "De provisión", "Cultural", "Depurar el agua es una función de regulación del ecosistema."),
        ("abc", "¿Qué pregunta está mejor delimitada?", "¿Cuánto nitrato llega por semana a un río desde los campos de un valle de ejemplo después de lluvias?", "¿Es mala la agricultura?", "¿Qué pasa con la naturaleza?", "La mejor pregunta nombra contaminante, fuente, lugar, tiempo y variable medible."),
        ("ab", "Un estudiante dice: «la minería contamina». ¿Qué mejora su afirmación?", "Nombrar el contaminante, la vía por la que llega al ambiente y el sistema afectado", "Cambiar «minería» por «industria»", "Una afirmación evaluable precisa qué sustancia, por qué vía y dónde."),
        ("=", "{F} Si la concentración de la tubería de ejemplo bajara a 2 mg/L con el mismo caudal, ¿cuál sería la carga?", "2*100", "Se multiplica la nueva concentración por el caudal que no cambia.", " mg/s"),
        ("abc", "Un pueblo pesca en un río y la pesca le da alimento. ¿Qué tipo de servicio ecosistémico es?", "De provisión", "De regulación", "Cultural", "La pesca entrega alimento, un servicio de provisión."),
        ("abc", "Un río recibe agua de un pueblo y de un campo. ¿Cómo se puede averiguar de dónde viene un contaminante?", "Midiendo antes y después de cada posible fuente", "Preguntando solo la opinión de vecinos", "Midiendo una sola vez lejos de ambas", "Comparar puntos antes y después de cada fuente permite atribuir el origen."),
        ("=", "{F} Una descarga de ejemplo tiene 4 mg/L y un caudal de 250 L/s. ¿Cuántos kilogramos salen en una hora (3.600 s)? 1 kg equivale a 1.000.000 mg.", "4*250*3600/1000000", "Se calcula la carga en mg/s, se multiplica por los segundos de una hora y se convierte a kg.", " kg"),
    ],
    ctx=("abc", "Contexto: una escuela de ejemplo vive junto a un estero donde alumnos observan espuma. Deben proponer una pregunta de investigación para su informe. ¿Cuál elige?", "¿Qué concentración de detergentes hay en el estero antes y después de la tubería del barrio?", "¿Por qué hay contaminación?", "¿Es sucio el estero?", "La pregunta elegida nombra la sustancia, los puntos de medición y la variable."),
    sc=[
        ("En Química: ¿qué es un servicio ecosistémico?", "Un beneficio que las personas obtienen de un ecosistema", "El agua, el alimento y la depuración son servicios ecosistémicos."),
        ("ab", "Una fuente difusa llega:", "Repartida en un área", "Desde un lugar exacto", "Difusa significa sin un punto único de descarga."),
        ("ab", "La carga contaminante se calcula como:", "Concentración por caudal", "Concentración más caudal", "Se multiplican ambas para obtener cantidad por tiempo."),
    ],
    op=("Con los casos de la ficha {F}: (1) elige uno (C1 a C4) y clasifícalo como fuente puntual o difusa; (2) nombra el contaminante, el ambiente afectado y un servicio ecosistémico que podría deteriorarse; (3) escribe una pregunta delimitada con su variable medible.",
        "(1) C2, difusa. (2) Contaminantes: nitrato y fosfato; ambiente: un río; servicio: agua para beber y pesca. (3) ¿Cómo cambia la concentración de nitrato del río en los días siguientes a una lluvia en el valle?",
        ["caso clasificado", "contaminante, ambiente y servicio", "pregunta con variable medible"],
        ["tres respuestas numeradas"],
        ["clasificar mal la fuente", "pregunta demasiado amplia", "no nombrar un servicio afectado"],
        "Pregunta: «¿en qué puntos medirías para confirmar la fuente?»."),
    reinforce="Clasifica cada caso de la ficha (C1 a C4) como puntual o difusa y nombra un servicio ecosistémico posiblemente afectado.",
    extend="Explica por qué es más difícil controlar una fuente difusa que una puntual.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (datos de ejemplo; los valores de referencia son inventados para practicar). Vías de exposición: ingestión (agua y alimentos), inhalación (aire) y contacto con la piel. "
     "Dosis diaria = concentración × consumo diario ÷ masa corporal, en mg/kg al día. Contaminante X en el agua de un pozo de ejemplo: 2 mg/L. Un adulto de 50 kg bebe 2 L al día; un niño de 20 kg bebe 1,5 L al día. Valor de referencia de ejemplo del contaminante X en agua potable: 0,5 mg/L. "
     "Fuente A: informe de monitoreo con método, laboratorio e instrumento descritos, y 12 muestras en 12 meses. Fuente B: rumor sin datos: «el agua del pozo enferma a todos». Variables de exposición: concentración, tiempo, vía y características de la persona.")
build(
    O5, 2, F,
    use="Aprenderé a evaluar fuentes y variables sobre cómo un contaminante llega a las personas: vías de exposición, dosis y tiempo. Sirve para distinguir una alarma sin datos de un informe de monitoreo y para reconocer quiénes están más expuestos.",
    prior=["Sé qué es una concentración y una masa corporal.", "Sé multiplicar y dividir con decimales simples.", "Sé evaluar una fuente por su método y sus datos."],
    explain=[
        "Un contaminante solo puede afectar a una persona si entra en contacto con ella. Los caminos de entrada se llaman vías de exposición: ingestión, si se bebe o se come; inhalación, si se respira; y contacto con la piel. La exposición depende de la concentración del contaminante, del tiempo que dura, de la vía y de las características de la persona, como su edad o su masa corporal.",
        "Para comparar exposiciones se calcula la dosis, que relaciona lo que entra con el tamaño de quien lo recibe: dosis = concentración × consumo ÷ masa corporal. Un niño que bebe 1,5 L al día con 20 kg recibe una dosis mayor por kilo que un adulto que bebe 2 L con 50 kg, aunque el agua sea la misma. Un valor de referencia es un nivel con el que se compara una medición para priorizar acciones; no es una prueba de daño por sí solo.",
        "Al evaluar fuentes, un informe de monitoreo con método, laboratorio y muestras repetidas es más confiable que un rumor. Para atribuir un efecto a un contaminante hay que controlar otras variables. Si sospechas que el agua que usas está contaminada, avisa a una persona adulta de confianza y a la autoridad de salud, y no la bebas ni la pruebes.",
    ],
    vocab=[("vía de exposición", "camino por el que un contaminante llega a una persona"), ("dosis", "cantidad de contaminante que recibe una persona por unidad de masa corporal"), ("valor de referencia", "nivel con el que se compara una medición para priorizar acciones"), ("ingestión", "entrada de una sustancia por la boca"), ("inhalación", "entrada de una sustancia por la respiración")],
    worked=[
        ("Calcular una dosis", "Un adulto de 60 kg bebe 3 L al día de agua con 1 mg/L de un contaminante de ejemplo. ¿Cuál es su dosis diaria?",
         ["Dosis = concentración × consumo ÷ masa corporal.", "1 × 3 ÷ 60.", "El resultado es 0,05 mg/kg al día."],
         "0,05 mg/kg al día"),
        ("Identificar la vía", "Una persona respira polvo con partículas del aire de una calle. ¿Cuál es la vía de exposición?",
         ["El polvo entra al cuerpo con la respiración.", "Respirar se llama inhalación.", "Esa es la vía."],
         "Inhalación"),
    ],
    mistakes=[("Pensar que si el agua supera un valor de referencia, entonces ya enfermó a todos.", "El valor de referencia sirve para priorizar acciones; el daño depende de la dosis, el tiempo y la persona.", "Escribe «supera el valor de referencia» y pide más datos sobre la exposición."),
              ("Comparar solo la concentración y olvidar la masa corporal.", "Una misma agua da dosis distintas a personas de distinto tamaño y consumo.", "Calcula la dosis por kilo.")],
    T=[
        ("abc", "En Química: ¿qué es una vía de exposición?", "El camino por el que un contaminante llega a una persona", "La velocidad de una reacción química", "El valor de referencia de una norma", "La vía de exposición indica cómo entra el contaminante: ingestión, inhalación o piel."),
        ("{F} ¿Qué vía de exposición corresponde a beber agua del pozo de ejemplo?", "Ingestión", "Beber agua es introducirla por la boca, es decir, ingestión."),
        ("{F} ¿Qué fuente (A o B) es más confiable?", "La fuente A", "La A describe método, laboratorio e instrumento y tiene 12 muestras; la B no tiene datos."),
        ("=", "{F} ¿Cuál es la dosis diaria del adulto de ejemplo, en mg/kg al día?", "2*2/50", "Se multiplica la concentración por el consumo y se divide por la masa corporal.", " mg/kg al día"),
        ("=", "{F} ¿Cuál es la dosis diaria del niño de ejemplo, en mg/kg al día?", "2*1.5/20", "Se multiplica la concentración por el consumo del niño y se divide por su masa.", " mg/kg al día"),
        ("abc", "{F} ¿Por qué el niño recibe una dosis mayor que el adulto con la misma agua?", "Porque bebe más agua en relación con su masa corporal", "Porque el agua cambia de concentración al llegar a él", "Porque los niños no tienen vías de exposición", "La dosis depende del consumo en relación con la masa corporal."),
        ("=", "{F} ¿Cuántas veces mayor es la concentración del pozo que el valor de referencia?", "2/0.5", "Se divide la concentración medida por el valor de referencia.", " veces"),
        ("abc", "{F} Se quiere saber si el efecto depende del tiempo de exposición. ¿Qué variable se cambia en el estudio?", "La duración de la exposición", "La masa corporal del niño", "El nombre del pozo", "Para estudiar el efecto del tiempo se compara con distintas duraciones."),
        ("abc", "{F} El pozo supera el valor de referencia de ejemplo. ¿Qué conclusión es correcta?", "Hay que priorizar acciones y obtener datos de exposición, pues la superación no prueba por sí sola un daño", "El pozo enferma con certeza a todas las personas", "El valor de referencia no importa", "El valor de referencia sirve para priorizar, no para afirmar daño sin más datos."),
        ("ab", "{F} Sobre la fuente B, ¿qué conviene hacer?", "Pedir datos de monitoreo y no difundirla como un hecho", "Compartirla de inmediato para alertar", "Un rumor sin datos no es evidencia; hay que verificarlo antes de difundirlo."),
        ("=", "{F} Si el adulto de ejemplo redujera su consumo del agua del pozo a 1 L al día, ¿cuál sería su dosis, en mg/kg al día?", "2*1/50", "Se recalcula la dosis con 1 L de consumo.", " mg/kg al día"),
        ("abc", "{F} Una familia sospecha que su agua tiene un contaminante. ¿Qué es lo más adecuado?", "Avisar a una persona adulta y a la autoridad de salud, y usar otra fuente segura mientras tanto", "Beber más agua para diluirlo", "Probar el agua para ver si cambia su sabor", "Ante la sospecha se avisa a las personas y autoridades responsables y no se prueba el agua."),
        ("abc", "Una persona vive junto a una avenida con mucho tránsito. ¿Cuál es la vía principal de exposición al material particulado del aire?", "Inhalación", "Ingestión", "Contacto con la piel", "Las partículas del aire se respiran."),
    ],
    ctx=("abc", "Contexto: una junta de vecinos de ejemplo recibe una carta con un informe de monitoreo del pozo: 2 mg/L con valor de referencia de ejemplo de 0,5 mg/L. ¿Qué mensaje comunica con precisión?", "El pozo supera 4 veces el valor de referencia de ejemplo; se necesitan más datos de exposición y se debe informar a la autoridad de salud", "El pozo enferma a todos", "El pozo está bien, porque nadie se ha quejado", "El mensaje correcto compara con la referencia y declara lo que falta."),
    sc=[
        ("En Química: ¿qué es la dosis?", "La cantidad de contaminante que recibe una persona por unidad de masa corporal", "Relaciona lo que entra con el tamaño de quien lo recibe."),
        ("ab", "Un informe de monitoreo es más confiable que un rumor porque:", "Muestra método, datos y muestras repetidas", "Es más largo", "Los datos y el método se pueden revisar."),
        ("ab", "La inhalación es la vía de:", "Respirar", "Beber", "El material particulado entra por las vías respiratorias al respirar."),
    ],
    op=("Con la ficha {F}: (1) calcula la dosis de dos personas distintas (por ejemplo, el adulto y el niño); (2) nombra la vía de exposición y dos variables que influyen en la exposición; (3) escribe una conclusión prudente y una acción para proteger a la persona más expuesta.",
        "(1) Adulto: 0,08 mg/kg al día; niño: 0,15 mg/kg al día. (2) Vía: ingestión; variables: concentración y tiempo. (3) El niño recibe una dosis mayor; se recomienda avisar a la autoridad de salud y usar otra fuente de agua segura.",
        ["dos dosis correctas", "vía y dos variables", "conclusión prudente", "acción de protección"],
        ["tres respuestas numeradas"],
        ["olvidar la masa corporal", "afirmar daño seguro", "no recomendar avisar a la autoridad o a un adulto"],
        "Pregunta: «¿qué dato sobre el tiempo de exposición pedirías?»."),
    reinforce="Calcula la dosis diaria de un adulto de 50 kg que bebe 2 L al día de agua con 0,5 mg/L del contaminante X.",
    extend="Explica por qué el valor de referencia sirve para priorizar acciones pero no para afirmar un daño sin más datos.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (datos de ejemplo). Propiedades que determinan el comportamiento de un contaminante: solubilidad en agua (si se disuelve, viaja con el agua), afinidad por las grasas (si la tiene, se acumula en tejidos grasos), persistencia (cuánto tarda en degradarse; se resume con la vida media: el tiempo en que su cantidad baja a la mitad) y volatilidad (si pasa al aire). "
     "Bioacumulación: aumento de la concentración de una sustancia en un organismo a lo largo de su vida. Biomagnificación: aumento de la concentración al subir por la cadena alimentaria. "
     "Contaminante P de ejemplo: vida media 2 años; cantidad inicial en un suelo: 80 unidades. Cadena de ejemplo (µg/kg): fitoplancton 2; zooplancton 20; pez pequeño 200; pez grande 2.000. "
     "Modelo de eutrofización: más nutrientes (nitrato, fosfato) → más algas → al morir, su descomposición consume oxígeno → menos oxígeno disuelto → muerte de peces.")
build(
    O5, 3, F,
    use="Aprenderé a interpretar modelos sobre las propiedades de los contaminantes (solubilidad, persistencia, bioacumulación) y sobre la eutrofización. Sirve para explicar cómo un contaminante se mueve, permanece y afecta a los sistemas naturales.",
    prior=["Sé qué es una cadena alimentaria.", "Sé qué es la concentración y el oxígeno disuelto.", "Sé dividir por 2 varias veces."],
    explain=[
        "Las propiedades químicas de un contaminante explican su comportamiento. Un contaminante soluble en agua se mueve con ella por ríos y aguas subterráneas. Uno con afinidad por las grasas tiende a acumularse en los tejidos grasos de los seres vivos. Uno persistente tarda mucho en degradarse. La persistencia se resume con la vida media: tras cada vida media, la cantidad que queda es la mitad de la anterior.",
        "La bioacumulación ocurre cuando un organismo incorpora más sustancia de la que elimina. La biomagnificación ocurre cuando la concentración aumenta al subir por la cadena alimentaria, porque cada depredador come muchas presas contaminadas. En la cadena de ejemplo, la concentración aumenta en cada paso, de presa a depredador. Son más probables con sustancias persistentes y con afinidad por las grasas.",
        "La eutrofización es un modelo de cadena de efectos: el exceso de nutrientes, por ejemplo de fertilizantes o aguas servidas, favorece el crecimiento de algas; al morir, su descomposición consume oxígeno, y los peces mueren por falta de él. El modelo supone que los nutrientes son el factor limitante, y no cubre todos los casos. Siempre hay que decir qué explica un modelo y qué deja fuera.",
    ],
    vocab=[("vida media", "tiempo en que la cantidad de una sustancia baja a la mitad"), ("persistencia", "capacidad de una sustancia de permanecer sin degradarse"), ("bioacumulación", "aumento de la concentración en un organismo a lo largo de su vida"), ("biomagnificación", "aumento de la concentración al subir por la cadena alimentaria"), ("eutrofización", "exceso de nutrientes que lleva a falta de oxígeno en el agua")],
    worked=[
        ("Vida media", "Un contaminante de ejemplo con vida media de 3 años parte con 64 unidades. ¿Cuántas quedan a los 6 años?",
         ["6 años son 2 vidas medias (6 ÷ 3).", "Tras la primera: 64 ÷ 2 = 32.", "Tras la segunda: 32 ÷ 2 = 16."],
         "16 unidades"),
        ("Cadena de efectos", "En la eutrofización, ¿qué ocurre inmediatamente después de que muere un gran número de algas?",
         ["Las algas muertas quedan en el agua.", "Su descomposición necesita oxígeno.", "El oxígeno disuelto disminuye."],
         "Baja el oxígeno disuelto"),
    ],
    mistakes=[("Pensar que una sustancia desaparece del todo después de una vida media.", "Después de una vida media queda la mitad, no cero.", "Divide por 2 por cada vida media transcurrida."),
              ("Creer que la biomagnificación ocurre con cualquier sustancia.", "Es más probable con sustancias persistentes y con afinidad por las grasas.", "Revisa persistencia y afinidad antes de predecirla.")],
    T=[
        ("abc", "En Química: ¿qué es la vida media de un contaminante?", "El tiempo en que su cantidad baja a la mitad", "El tiempo total hasta que desaparece por completo", "La cantidad máxima que puede disolverse", "La vida media mide la mitad de la cantidad, no su desaparición total."),
        ("=", "{F} ¿Cuántas unidades del contaminante P quedan en el suelo después de 2 años?", "80/2", "Pasa una vida media y la cantidad queda en la mitad.", " unidades"),
        ("=", "{F} ¿Cuántas vidas medias transcurren en 6 años para el contaminante P?", "6/2", "Se divide el tiempo transcurrido por la vida media.", " vidas medias"),
        ("=", "{F} ¿Cuántas unidades del contaminante P quedan después de 6 años?", "80/2/2/2", "Pasan tres vidas medias y la cantidad se divide por 2 en cada una.", " unidades"),
        ("abc", "{F} Un contaminante persistente y con afinidad por las grasas, ¿qué se espera en los depredadores finales de una cadena?", "Una concentración mayor por biomagnificación", "Una concentración menor", "Ninguna concentración", "La sustancia persistente y afín a la grasa se acumula y sube por la cadena."),
        ("=", "{F} ¿Cuántas veces mayor es la concentración del pez grande que la del fitoplancton?", "2000/2", "Se divide la concentración del pez grande por la del fitoplancton.", " veces"),
        ("=", "{F} ¿Cuántas veces mayor es la concentración del pez pequeño que la del zooplancton?", "200/20", "Se divide la concentración del pez pequeño por la del zooplancton.", " veces"),
        ("abc", "{F} En la eutrofización, ¿qué ocurre después de que muere un gran número de algas?", "La descomposición consume oxígeno y baja el oxígeno disuelto", "El oxígeno disuelto aumenta", "Los nutrientes desaparecen sin efecto", "La descomposición de la materia orgánica necesita oxígeno."),
        ("abc", "{F} ¿Qué propiedad hace que un contaminante viaje lejos disuelto en un río?", "Su alta solubilidad en agua", "Su afinidad por las grasas", "Su baja persistencia siempre", "Lo soluble se mueve con el agua."),
        ("ab", "{F} ¿Qué supone el cálculo con vida media?", "Que la cantidad baja a la mitad en cada período igual", "Que la cantidad baja la misma cantidad cada año", "La vida media implica una disminución proporcional en períodos iguales."),
        ("abc", "Contaminante 1: muy soluble en agua y poco persistente. Contaminante 2: poco soluble, persistente y afín a las grasas. ¿Cuál es más probable que se biomagnifique?", "El contaminante 2", "El contaminante 1", "Ambos por igual", "La persistencia y la afinidad por la grasa favorecen la biomagnificación."),
        ("abc", "{F} Un agricultor usa menos fertilizante. ¿Qué eslabón del modelo de eutrofización se ve afectado primero?", "La cantidad de nutrientes que llega al agua", "La temperatura del suelo", "La cantidad de peces", "Menos fertilizante reduce los nutrientes, el primer eslabón de la cadena."),
        ("=", "{F} ¿Cuántas unidades del contaminante P quedan a los 8 años?", "80/2/2/2/2", "En 8 años pasan cuatro vidas medias y la cantidad se divide por 2 cuatro veces.", " unidades"),
    ],
    ctx=("abc", "Contexto: un lago de ejemplo recibe nutrientes de los campos de la cuenca y en verano aparecen mortandades de peces. ¿Qué explicación de la cadena de efectos es la más completa?", "Más nutrientes provocan más algas; al morir, su descomposición baja el oxígeno y los peces mueren", "Los peces mueren porque se cansan", "Los peces mueren porque falta luz", "La explicación correcta enlaza nutrientes, algas, consumo de oxígeno y muerte de peces."),
    sc=[
        ("En Química: ¿qué es la biomagnificación?", "El aumento de la concentración al subir por la cadena alimentaria", "Cada depredador come presas con sustancia acumulada."),
        ("ab", "Una sustancia con vida media corta se degrada:", "Más rápido", "Más lento", "Una vida media corta significa que baja pronto a la mitad."),
        ("ab", "La eutrofización comienza con:", "Exceso de nutrientes", "Falta de nutrientes", "El exceso de nutrientes favorece el crecimiento de algas."),
    ],
    op=("Con los modelos de la ficha {F}: (1) elige uno (vida media, cadena alimentaria o eutrofización); (2) usa los datos de la ficha para calcular un valor; (3) explica en dos oraciones qué predice el modelo y escribe un supuesto que podría fallar.",
        "(1) Vida media. (2) Después de 4 años quedan 20 unidades del contaminante P. (3) Predice que cada 2 años la cantidad baja a la mitad; supone que la degradación es constante, lo que puede fallar si cambian la temperatura o el suelo.",
        ["modelo elegido", "cálculo correcto", "predicción", "supuesto declarado"],
        ["tres respuestas numeradas"],
        ["confundir vida media con tiempo total", "no declarar supuestos", "no usar los datos de la ficha"],
        "Pregunta: «¿qué medición real confirmaría tu predicción?»."),
    reinforce="Calcula cuántas unidades quedan del contaminante P tras 2, 4 y 6 años y dibuja una tabla.",
    extend="Explica por qué una sustancia persistente y afín a las grasas puede ser más preocupante que una soluble que se degrada pronto.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (datos de ejemplo; el valor de referencia es inventado para practicar). Cobre disuelto en un río de ejemplo, en µg/L: punto 1 (antes de una faena minera): 20; punto 2 (junto a la descarga): 600; punto 3 (5 km aguas abajo): 150. Valor de referencia de ejemplo: 50 µg/L. "
     "pH en los mismos puntos: punto 1: 7; punto 2: 4; punto 3: 6. 1 mg/L equivale a 1.000 µg/L. La población de ejemplo vive cerca del punto 3 y riega huertos con esa agua. "
     "Material particulado en el aire de una ciudad de ejemplo (µg/m³): invierno 60; verano 20.")
build(
    O5, 4, F,
    use="Aprenderé a analizar datos de contaminantes de minería, agricultura y ciudad comparándolos con un valor de referencia y entre puntos de medición. Sirve para describir efectos sobre sistemas naturales con números y sin exagerar.",
    prior=["Sé calcular cambios porcentuales.", "Sé convertir µg/L a mg/L.", "Sé que el pH mide la acidez."],
    explain=[
        "Analizar datos de contaminantes comienza con comparar. Se compara un punto con otro, por ejemplo antes y después de una descarga, y con un valor de referencia. Un cociente simple indica cuántas veces supera una medición al valor de referencia. Si hay 600 µg/L y la referencia es 50 µg/L, el cociente es 12. Para convertir unidades, 1.000 µg equivalen a 1 mg.",
        "Los efectos de un contaminante dependen también de las condiciones del ambiente. En aguas con pH bajo, los metales tienden a mantenerse disueltos y pueden afectar más a los organismos; por eso se mide el pH junto con el metal. Que la concentración baje aguas abajo, por dilución o por depositarse en el sedimento, no significa que el problema desaparezca: el metal puede seguir sobre la referencia o acumularse en el sedimento.",
        "Un estudio con un solo muestreo muestra un momento. Para atribuir el cobre a la faena minera ayuda tener un punto antes de la fuente, como el punto 1, que es bajo, y mediciones repetidas en el tiempo. En aire, el material particulado cambia con las estaciones, y conviene comparar períodos equivalentes. Siempre se debe declarar cuántas mediciones hay y qué falta medir.",
    ],
    vocab=[("valor de referencia", "nivel con el que se comparan las mediciones"), ("µg/L", "microgramos por litro; 1.000 µg/L equivalen a 1 mg/L"), ("material particulado", "partículas sólidas o líquidas muy pequeñas suspendidas en el aire"), ("dilución", "disminución de la concentración al mezclarse con más agua"), ("sedimento", "material que se deposita en el fondo de un cuerpo de agua")],
    worked=[
        ("Cociente con la referencia", "En la ficha, ¿cuántas veces supera el punto 2 al valor de referencia?",
         ["Concentración en el punto 2: 600 µg/L.", "Valor de referencia: 50 µg/L.", "600 ÷ 50 = 12 veces."],
         "12 veces"),
        ("Cambio entre puntos", "¿Cuál es el cambio de cobre del punto 1 al punto 3, en µg/L?",
         ["Punto 3: 150 µg/L; punto 1: 20 µg/L.", "Cambio: 150 − 20.", "El cobre aumentó 130 µg/L."],
         "Aumentó 130 µg/L"),
    ],
    mistakes=[("Concluir que el problema terminó porque la concentración bajó aguas abajo.", "Puede seguir sobre la referencia o acumularse en el sedimento.", "Compara cada punto con la referencia."),
              ("Atribuir la contaminación a una fuente con un solo punto de medición.", "Falta un punto antes de la fuente y mediciones repetidas.", "Busca puntos antes y después y varias fechas.")],
    T=[
        ("abc", "En Química: ¿para qué sirve un valor de referencia?", "Para comparar mediciones y priorizar acciones", "Para demostrar el daño con certeza", "Para medir el pH", "El valor de referencia es un nivel de comparación, no una prueba de daño."),
        ("{F} ¿En qué punto del río hay más cobre?", "En el punto 2", "600 µg/L es el valor más alto de los tres."),
        ("=", "{F} ¿Cuántas veces supera el punto 3 al valor de referencia?", "150/50", "Se divide la concentración del punto 3 por el valor de referencia.", " veces"),
        ("=", "{F} ¿Cuál es el cambio porcentual del cobre entre el punto 2 y el punto 3?", "(150-600)*100/600", "Se divide la diferencia por el valor del punto 2 y se multiplica por 100.", " %"),
        ("=", "{F} Expresa 600 µg/L en mg/L.", "600/1000", "Cada 1.000 µg son 1 mg, así que se divide por 1.000.", " mg/L"),
        ("abc", "{F} ¿Qué ocurre con el cobre entre el punto 2 y el punto 3?", "Disminuye, pero sigue sobre el valor de referencia", "Aumenta", "Queda bajo el valor de referencia", "150 µg/L es menor que 600, pero mayor que 50."),
        ("abc", "{F} El punto 2 tiene pH 4. ¿Qué relación tiene con el cobre?", "El pH bajo favorece que los metales se mantengan disueltos y afecten más a los organismos", "El pH bajo hace desaparecer el cobre", "El pH no tiene relación con los metales", "En aguas ácidas los metales tienden a permanecer disueltos."),
        ("abc", "{F} La población riega huertos con el agua del punto 3. ¿Qué conclusión es prudente?", "El cobre supera la referencia de ejemplo; conviene medir suelo y cultivos y avisar a la autoridad de salud", "No pasa nada, porque bajó de 600", "El suelo está contaminado con certeza", "La conclusión se limita a lo medido y recomienda más datos."),
        ("=", "{F} ¿Cuántos µg/L aumentó el cobre entre el punto 1 y el punto 2?", "600-20", "Se resta el valor del punto 1 al del punto 2.", " µg/L"),
        ("=", "{F} ¿Cuántas veces mayor es el material particulado en invierno que en verano?", "60/20", "Se divide el valor de invierno por el de verano.", " veces"),
        ("ab", "{F} ¿Qué dato ayuda a atribuir el cobre a la faena minera?", "El punto 1, antes de la faena, con un valor bajo, y mediciones repetidas", "Una fotografía del río", "Un punto antes de la fuente y datos repetidos permiten comparar causas."),
        ("abc", "{F} Un estudiante dice: «el punto 3 ya está limpio porque bajó de 600 a 150». ¿Qué respondes?", "Sigue sobre el valor de referencia de ejemplo", "Tiene razón: 150 es poco", "El punto 3 está bajo la referencia", "Bajar no es cumplir: 150 es mayor que 50."),
        ("abc", "{F} ¿Por qué el material particulado se compara entre invierno y verano de un mismo lugar?", "Para ver cómo cambia con la estación en el mismo lugar", "Para saber qué ciudad es más grande", "Porque en verano no se mide", "Comparar períodos equivalentes en el mismo sitio muestra la variación estacional."),
    ],
    ctx=("abc", "Contexto: la comunidad de ejemplo pide a una autoridad ambiental explicar los resultados de la ficha. ¿Qué frase respeta los datos y sus límites?", "El cobre fue 12 veces la referencia de ejemplo junto a la descarga y 3 veces 5 km aguas abajo, con una sola medición por punto; se recomienda repetir y medir suelo", "El río está completamente muerto", "El río está limpio, porque bajó el cobre", "La frase correcta da cifras, la referencia y la limitación del muestreo."),
    sc=[
        ("En Química: ¿qué es el material particulado?", "Partículas muy pequeñas suspendidas en el aire", "Se respira y puede afectar la salud según la cantidad."),
        ("ab", "Un solo muestreo muestra:", "Un momento y un lugar", "Todo el año y todo el río", "Una medición única no representa el tiempo completo."),
        ("ab", "Si la concentración baja aguas abajo pero sigue sobre la referencia:", "El problema continúa", "El problema terminó", "Sigue superando el nivel de comparación."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula cuántas veces supera cada punto del río el valor de referencia; (2) escribe una conclusión sobre la relación del cobre con la faena minera usando el punto 1; (3) indica una limitación y qué medirías después.",
        "(1) Punto 1: 0,4 veces; punto 2: 12 veces; punto 3: 3 veces. (2) El punto 1 está bajo la referencia y el 2, junto a la descarga, muy sobre ella, lo que sugiere un aporte de la faena. (3) Hay una sola medición por punto; mediría en varias fechas y en el sedimento.",
        ["tres cocientes correctos", "conclusión apoyada en el punto 1", "limitación y medición propuesta"],
        ["tres respuestas numeradas"],
        ["no comparar con la referencia", "concluir sin el punto de comparación", "no declarar limitación"],
        "Pregunta: «¿qué otra fuente podría aportar cobre?»."),
    reinforce="Calcula el cociente del punto 1 con respecto a la referencia e interpreta si está bajo o sobre ella.",
    extend="Explica por qué el pH y la concentración de un metal se miden juntos al evaluar un río cercano a una mina.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (datos de ejemplo). Agua de descarga con cobre disuelto a 600 µg/L; valor de referencia de ejemplo 50 µg/L. Fórmula: concentración final = concentración inicial × (100 − % retirado) ÷ 100. "
     "Opciones: tratamiento A: retira 90 % del cobre, costo relativo 5; tratamiento B: retira 60 %, costo relativo 2; humedal artificial con plantas (fitorremediación, es decir, uso de plantas para retirar o estabilizar contaminantes) como paso adicional: retira 50 % de lo que le llega, costo relativo 1, es lento y necesita terreno; "
     "reducir en la fuente: recircular el agua dentro de la faena para que la descarga baje a 300 µg/L antes de tratarla, costo relativo 3. Los pasos pueden combinarse en serie, uno después de otro.")
build(
    O5, 5, F,
    use="Aprenderé a comparar soluciones frente a un contaminante: reducir en la fuente, tratar y restaurar, con cálculos de concentración final y costo. Sirve para decidir con criterios y reconocer residuos y límites de cada opción.",
    prior=["Sé calcular porcentajes.", "Sé qué es un valor de referencia.", "Sé comparar opciones con criterios."],
    explain=[
        "Frente a un contaminante hay tres tipos de solución. Prevenir o reducir en la fuente evita que el contaminante se genere o salga. Tratar el agua o el suelo lo retira antes de que llegue al ambiente. Restaurar recupera un sistema ya dañado. Prevenir suele producir menos residuos y evitar costos mayores, pero puede exigir cambios en los procesos de la industria.",
        "Para comparar opciones se calcula la concentración final tras cada una: concentración final = inicial × (100 − % retirado) ÷ 100. Si se combinan pasos en serie, el resultado del primero es el inicio del segundo. Luego se compara con el valor de referencia y se suma el costo. Un tratamiento puede cumplir la referencia y, aun así, dejar un residuo, como lodos con metales, que hay que manejar con seguridad.",
        "La fitorremediación usa plantas para retirar o estabilizar contaminantes; suele costar poco, pero es lenta y necesita terreno. Ninguna opción es perfecta, y la mejor depende de los criterios y su peso. Una comparación honesta nombra las limitaciones, por ejemplo qué se hace con los residuos y si hay datos reales de eficacia en el lugar.",
    ],
    vocab=[("fitorremediación", "uso de plantas para retirar o estabilizar contaminantes"), ("tratamiento en serie", "pasos que se aplican uno después de otro"), ("prevención en la fuente", "medida que evita que el contaminante se genere o salga"), ("residuo del tratamiento", "material que queda tras retirar el contaminante"), ("eficacia", "porcentaje de contaminante que retira una medida")],
    worked=[
        ("Concentración final", "Un tratamiento de ejemplo retira 75 % de un contaminante que está a 400 µg/L. ¿Cuál es la concentración final?",
         ["Se aplica concentración final = inicial × (100 − % retirado) ÷ 100.", "400 × (100 − 75) ÷ 100 = 400 × 25 ÷ 100.", "El resultado es 100 µg/L."],
         "100 µg/L"),
        ("Pasos en serie", "Tras ese tratamiento (100 µg/L), se agrega un humedal que retira 50 %. ¿Cuál es la concentración final?",
         ["El resultado del primer paso es el inicio del segundo: 100 µg/L.", "100 × (100 − 50) ÷ 100.", "El resultado es 50 µg/L."],
         "50 µg/L"),
    ],
    mistakes=[("Aplicar el segundo tratamiento sobre la concentración original en vez de sobre el resultado del primero.", "En una serie, el segundo paso recibe lo que sale del primero.", "Calcula paso a paso y usa el resultado anterior."),
              ("Suponer que un tratamiento que cumple la referencia no genera ningún problema.", "Puede dejar residuos que hay que manejar.", "Agrega el residuo como criterio de comparación.")],
    T=[
        ("abc", "En Química: ¿qué es la fitorremediación?", "El uso de plantas para retirar o estabilizar contaminantes", "La quema de residuos para eliminarlos", "La medición de pH en un río", "La fitorremediación aprovecha plantas para tratar sitios contaminados."),
        ("=", "{F} ¿Cuál es la concentración final con el tratamiento A?", "600*(100-90)/100", "Se aplica la fórmula con 90 % retirado.", " µg/L"),
        ("abc", "{F} Con el tratamiento A solo, ¿se cumple el valor de referencia de ejemplo?", "No, porque 60 µg/L es mayor que 50 µg/L", "Sí, porque retira 90 %", "Sí, porque 60 es menor que 50", "60 µg/L sigue sobre la referencia de 50."),
        ("=", "{F} ¿Cuál es la concentración final con el tratamiento B?", "600*(100-60)/100", "Se aplica la fórmula con 60 % retirado.", " µg/L"),
        ("=", "{F} Si se aplica el tratamiento A y luego el humedal, ¿cuál es la concentración final?", "600*(100-90)/100*(100-50)/100", "Se aplica la fórmula en dos pasos: primero 90 % y luego 50 % sobre el resultado.", " µg/L"),
        ("abc", "{F} Con el tratamiento A seguido del humedal, ¿se cumple el valor de referencia?", "Sí, porque 30 µg/L es menor que 50 µg/L", "No, porque 30 es mayor que 50", "No se puede calcular", "30 µg/L queda bajo la referencia de 50."),
        ("=", "{F} ¿Cuál es el costo relativo total del tratamiento A seguido del humedal?", "5+1", "Se suman los costos relativos de ambos pasos.", ""),
        ("=", "{F} Si se reduce en la fuente (300 µg/L) y luego se aplica el tratamiento B, ¿cuál es la concentración final?", "300*(100-60)/100", "Se parte de 300 µg/L y se aplica 60 % de retiro.", " µg/L"),
        ("abc", "{F} Entre las combinaciones A + humedal (costo 6, 30 µg/L), B + humedal (costo 3, 120 µg/L) y reducir en la fuente + A (costo 8, 30 µg/L), ¿cuál cumple la referencia con el menor costo?", "A + humedal, con costo 6", "B + humedal, con costo 3", "Reducir en la fuente + A, con costo 8", "Solo A + humedal y fuente + A cumplen, y la primera cuesta menos."),
        ("ab", "{F} Además de costo y eficacia, ¿qué criterio conviene considerar?", "Los residuos que quedan, como lodos con metales, y cómo se manejan", "El color del equipo de tratamiento", "Un tratamiento puede cumplir la referencia y dejar residuos que también hay que manejar."),
        ("abc", "{F} El humedal es «lento y necesita terreno». ¿Qué limitación implica?", "No sirve si se necesita un tratamiento inmediato o no hay espacio", "No retira ningún contaminante", "Siempre es la opción más cara", "Su lentitud y su necesidad de terreno limitan dónde y cuándo se puede usar."),
        ("abc", "¿Por qué reducir el contaminante en la fuente suele ser preferible a solo tratarlo al final?", "Porque disminuye la cantidad que hay que tratar y los residuos", "Porque elimina la necesidad de medir", "Porque siempre es más barato", "Menos contaminante en el origen significa menos que tratar y menos residuo."),
        ("=", "{F} ¿Qué porcentaje total de cobre se retira con el tratamiento A seguido del humedal (de 600 a 30 µg/L)?", "(600-30)*100/600", "Se divide la cantidad retirada por la inicial y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Contexto: un municipio de ejemplo con poco presupuesto debe tratar el agua de una descarga que parte en 600 µg/L, con referencia de 50 µg/L. ¿Qué recomendación sigue los cálculos de la ficha?", "Combinar el tratamiento A con el humedal, que cumple la referencia con costo 6, y planificar el manejo de los residuos", "Usar solo el tratamiento B por ser barato, aunque no cumple la referencia", "No tratar, porque el costo es alto", "La recomendación cumple la referencia con el menor costo e incluye el manejo de residuos."),
    sc=[
        ("En Química: ¿qué es un tratamiento en serie?", "Pasos que se aplican uno después de otro", "El segundo paso recibe lo que sale del primero."),
        ("ab", "Prevenir en la fuente:", "Disminuye lo que hay que tratar", "Aumenta los residuos", "Menos contaminante en el origen reduce el tratamiento."),
        ("ab", "Un tratamiento que cumple la referencia:", "Puede dejar residuos que manejar", "No deja residuos", "Los lodos con metales son un ejemplo de residuo."),
    ],
    op=("Con las opciones de la ficha {F}: (1) calcula la concentración final de dos combinaciones distintas; (2) compara costo, cumplimiento de la referencia y un residuo; (3) recomienda una combinación y escribe una limitación de la recomendación.",
        "(1) A: 60 µg/L; A + humedal: 30 µg/L. (2) A solo no cumple y cuesta 5; A + humedal cumple y cuesta 6; deja lodos con metales. (3) Recomiendo A + humedal; falta saber cómo manejar los lodos y no hay datos reales de la zona.",
        ["dos concentraciones finales", "comparación con tres criterios", "recomendación", "limitación"],
        ["tres respuestas numeradas"],
        ["aplicar el segundo paso a la concentración original", "olvidar los residuos", "no comparar con la referencia"],
        "Pregunta: «¿qué criterio nuevo agregarías a la comparación?»."),
    reinforce="Calcula la concentración final si se combina B con el humedal y decide si cumple la referencia.",
    extend="Explica por qué conviene combinar prevención en la fuente con tratamiento y no depender solo de uno.",
)

# ============================================================ OAC-05, clase 6
F = ("Ficha 6 (datos de ejemplo; el valor de referencia es inventado para practicar). Caso: la comunidad de un valle debe decidir si instala un tratamiento A + humedal para el agua de riego. Cobre en el río aguas abajo: 150 µg/L; valor de referencia de ejemplo: 50 µg/L. Hay solo 3 mediciones, de un solo mes. "
     "El costo de la medida es de 6.000 unidades monetarias de ejemplo y beneficiaría a 300 familias. Si no se actúa, una parte de los cultivos podría verse afectada, pero no hay datos de suelo. "
     "Principio precautorio: cuando existe posibilidad de daño serio y falta certeza científica, se toman medidas razonables sin esperar certeza absoluta. Modelo de comunicación: qué muestran los datos, qué no muestran, qué se recomienda y quién decide.")
build(
    O5, 6, F,
    use="Aprenderé a comunicar los límites de un análisis sobre contaminantes y a fundamentar una decisión: qué muestran los datos, qué no, qué se recomienda y quién decide. Sirve para hablar con honestidad ante una comunidad.",
    prior=["Sé comparar una medición con un valor de referencia.", "Sé que correlación no es causalidad.", "Sé calcular costos por persona o familia."],
    explain=[
        "Comunicar bien un análisis ambiental implica ser claro con cuatro cosas: qué muestran los datos, qué no muestran, qué se recomienda y quién decide. Qué muestran: por ejemplo, que el cobre superó 3 veces el valor de referencia de ejemplo en tres mediciones de un mes. Qué no muestran: el efecto en el suelo y los cultivos, o lo que ocurre en otras estaciones. Las decisiones sobre una comunidad las toman las personas y las autoridades responsables, con la información de especialistas.",
        "Cuando hay posibilidad de daño serio y falta certeza, el principio precautorio indica tomar medidas razonables y proporcionales sin esperar certeza absoluta, mientras se sigue midiendo. No significa tomar cualquier medida: se consideran costos, beneficios y riesgos de cada opción. Una comunicación responsable evita tanto el alarmismo («el agua está envenenada») como la minimización («no pasa nada»).",
        "Al decidir también se cuida la equidad: quiénes se benefician y quiénes asumen los costos o los riesgos. Es útil calcular, por ejemplo, el costo por familia. Y quien tiene un interés económico en el resultado puede sesgar la información, por lo que se pide que los datos sean verificables. Aquí no se toma partido por una decisión: se muestra cómo ordenar los argumentos.",
    ],
    vocab=[("principio precautorio", "tomar medidas razonables ante un posible daño serio aunque falte certeza científica"), ("alarmismo", "exagerar un riesgo más allá de lo que muestran los datos"), ("minimización", "restar importancia a un riesgo más allá de lo que muestran los datos"), ("equidad", "reparto justo de beneficios, costos y riesgos"), ("sesgo", "desviación que favorece un resultado por interés o por error")],
    worked=[
        ("Qué no muestran los datos", "Con tres mediciones de cobre en un mes, ¿qué NO se puede afirmar?",
         ["Solo se midió un mes y en un lugar.", "No hay datos de otras estaciones ni de suelo.", "No se puede afirmar qué pasa durante todo el año ni en los cultivos."],
         "Lo que ocurre todo el año y en el suelo"),
        ("Costo por familia", "Una medida cuesta 4.500 unidades de ejemplo y beneficia a 150 familias. ¿Cuánto es por familia?",
         ["Costo total: 4.500.", "Familias: 150.", "4.500 ÷ 150 = 30."],
         "30 unidades por familia"),
    ],
    mistakes=[("Comunicar «el agua está envenenada» con tres mediciones.", "Los datos no permiten esa afirmación y generan alarma innecesaria.", "Di lo que muestran las cifras y lo que falta."),
              ("Decir «no pasa nada» porque no hay datos del suelo.", "La ausencia de datos no es ausencia de riesgo.", "Declara la incertidumbre y propón medir.")],
    T=[
        ("abc", "En Química: ¿qué es el principio precautorio?", "Tomar medidas razonables ante un posible daño serio aunque falte certeza científica", "Esperar certeza absoluta antes de actuar", "Ignorar los datos", "El principio precautorio busca actuar con prudencia sin certeza absoluta."),
        ("=", "{F} ¿Cuántos µg/L por sobre el valor de referencia de ejemplo está el cobre aguas abajo?", "150-50", "Se resta el valor de referencia a la concentración medida.", " µg/L"),
        ("=", "{F} Se recomienda tener 12 mediciones en el año. ¿Cuántas faltan?", "12-3", "Se resta el número de mediciones que ya existen al número recomendado.", " mediciones"),
        ("=", "{F} ¿Cuántas unidades monetarias de ejemplo cuesta la medida por familia?", "6000/300", "Se divide el costo total por el número de familias beneficiadas.", " unidades por familia"),
        ("abc", "{F} ¿Qué NO muestran los datos de la ficha?", "El efecto en el suelo y en los cultivos", "Que se midió cobre", "Que hay una referencia de ejemplo", "La ficha dice que no hay datos de suelo."),
        ("abc", "{F} ¿Qué comunicación sigue el modelo (muestran, no muestran, recomienda, decide)?", "El cobre superó 3 veces la referencia en 3 mediciones de un mes; no se sabe el efecto en suelos; se recomienda seguir midiendo y evaluar la medida; decide la comunidad con las autoridades", "El agua está envenenada y hay que cerrar todo", "No hay nada que informar", "La frase correcta entrega los cuatro elementos del modelo."),
        ("abc", "¿Cuál de estas frases es alarmista?", "«El agua del valle está envenenada»", "«El cobre superó la referencia de ejemplo en tres mediciones»", "«Faltan datos de suelo»", "Afirma un daño extremo que los datos no demuestran."),
        ("ab", "{F} ¿Qué decisión es coherente con el principio precautorio?", "Evaluar una medida de costo razonable y seguir midiendo", "Esperar a tener certeza absoluta sin hacer nada", "El principio busca actuar con prudencia mientras se obtienen más datos."),
        ("=", "{F} Si con el tratamiento el cobre bajara de 150 a 30 µg/L, ¿cuál sería el porcentaje de disminución?", "(150-30)*100/150", "Se divide la baja por la concentración inicial y se multiplica por 100.", " %"),
        ("abc", "¿Quién debe tomar la decisión sobre la medida para la comunidad?", "La comunidad y las autoridades responsables, con la información de especialistas", "Una sola persona sin consultar", "El que tiene un interés económico en la medida", "Las decisiones sobre una comunidad las toman las personas afectadas y las autoridades."),
        ("abc", "Una empresa proveedora del tratamiento entrega un informe que muestra solo resultados favorables. ¿Qué debe hacer la comunidad?", "Pedir datos completos y verificables, porque puede haber sesgo por interés", "Aceptarlo porque es técnico", "Descartarlo por venir de una empresa sin revisarlo", "Un interés económico puede sesgar; se piden datos verificables."),
        ("abc", "Se dice: «como no hay datos de suelo, no hay riesgo». ¿Qué falla?", "La falta de datos no demuestra la ausencia de riesgo", "Que hay demasiados datos", "Nada: la frase es correcta", "Sin datos no se puede afirmar ni descartar un riesgo."),
        ("=", "{F} La medida se instala con la inversión de la ficha y cuesta 500 unidades de ejemplo por año de mantenimiento durante 10 años. ¿Cuál es el costo total?", "6000+500*10", "Se suma la inversión inicial a los 10 años de mantenimiento.", " unidades"),
    ],
    ctx=("abc", "Contexto: te piden presentar el caso del valle en la asamblea de vecinos. ¿Cómo empiezas tu intervención?", "Con lo que muestran los datos y sus cifras, y luego con lo que aún no se sabe", "Con la decisión que debería tomar la comunidad, sin datos", "Con una frase alarmante para llamar la atención", "Una buena presentación parte de los datos y declara sus límites."),
    sc=[
        ("En Química: ¿qué es la equidad al decidir sobre una medida ambiental?", "Un reparto justo de beneficios, costos y riesgos", "Considera quiénes se benefician y quiénes asumen costos o riesgos."),
        ("ab", "Una comunicación responsable evita:", "El alarmismo y la minimización", "Mostrar los datos", "Debe ser fiel a lo que muestran los datos."),
        ("ab", "Las decisiones sobre una comunidad las toman:", "Las personas y autoridades responsables", "Quien redactó el informe técnico solo", "Los especialistas informan, pero la decisión es colectiva."),
    ],
    op=("Con el caso de la ficha {F}: (1) escribe la comunicación al curso con el modelo (qué muestran los datos, qué no, qué se recomienda y quién decide); (2) calcula el costo por familia; (3) menciona una consideración de equidad.",
        "(1) El cobre superó 3 veces la referencia de ejemplo en tres mediciones de un mes. No se conoce el efecto en suelos ni en otras estaciones. Se recomienda evaluar la medida y seguir midiendo; decide la comunidad con las autoridades. (2) 20 unidades por familia. (3) Hay que ver quién asume el costo y quién recibe el beneficio.",
        ["cuatro partes del modelo", "costo por familia", "consideración de equidad"],
        ["tres respuestas numeradas"],
        ["alarmismo o minimización", "afirmar sin datos", "decidir por la comunidad"],
        "Pregunta: «¿qué dato nuevo cambiaría tu recomendación?»."),
    reinforce="Reescribe la frase «el agua está envenenada» para que respete lo que muestran los datos de la ficha.",
    extend="Explica la diferencia entre el principio precautorio y actuar por miedo, usando el caso del valle.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (datos de ejemplo). Tres tipos de acciones frente al cambio climático: mitigación (reducir emisiones o aumentar los sumideros de carbono), adaptación (ajustarse a sus efectos) y restauración (recuperar un ecosistema dañado). "
     "Masas atómicas que se entregan: H = 1, C = 12, O = 16. Combustión del metano: CH4 + 2 O2 → CO2 + 2 H2O (16 g de CH4 producen 44 g de CO2). Combustión del octano, componente de la bencina: 2 C8H18 + 25 O2 → 16 CO2 + 18 H2O; cada mol de octano (114 g) produce 8 mol de CO2. "
     "Preguntas de ejemplo: P1 «¿Cómo ayuda la química al clima?». P2 «¿Cuánto CO2 se evita al dejar de quemar 32 g de metano?». P3 «¿Qué es mejor, mitigar o adaptar?».")
build(
    O6, 1, F,
    use="Aprenderé a delimitar preguntas sobre cómo la química y sus aplicaciones tecnológicas ayudan a entender, prevenir y mitigar el cambio climático y a restaurar sistemas naturales. Sirve para distinguir mitigación, adaptación y restauración y para calcular emisiones con masas.",
    prior=["Sé qué es una reacción de combustión.", "Sé calcular una masa molar.", "Sé qué es el CO2 y su relación con el clima."],
    explain=[
        "La química contribuye de tres maneras. Para entender, mide gases y estudia los equilibrios y los ciclos del carbono. Para prevenir y mitigar, desarrolla materiales, energías y procesos que emiten menos CO2 o lo retiran del aire. Para restaurar, ayuda a tratar aguas y suelos. Mitigar es reducir emisiones o aumentar sumideros, que son los lugares que absorben carbono, como los bosques. Adaptar es ajustarse a los efectos, y restaurar es recuperar un ecosistema dañado.",
        "Los cálculos de masa permiten estimar emisiones. En la combustión del metano, 16 g de CH4 producen 44 g de CO2, de modo que 32 g producen 88 g. En la del octano, cada mol (114 g) produce 8 mol de CO2, y cada mol de CO2 pesa 44 g. La masa se conserva: la masa de los productos es la de los reactivos que se combinaron.",
        "Para investigar, se delimita una pregunta que nombre una tecnología, una variable y un resultado medible. «¿Cómo ayuda la química al clima?» es demasiado amplia; en cambio, «¿cuánto CO2 se evita al dejar de quemar 32 g de metano?» se responde con un cálculo. Y preguntas como «¿qué es mejor, mitigar o adaptar?» necesitan un sitio, un criterio y datos para comparar.",
    ],
    vocab=[("mitigación", "reducir las emisiones o aumentar los sumideros de carbono"), ("adaptación", "ajustarse a los efectos del cambio climático"), ("restauración", "recuperar un ecosistema dañado"), ("sumidero de carbono", "sistema que absorbe más carbono del que emite"), ("combustión", "reacción de una sustancia con oxígeno que libera energía")],
    worked=[
        ("Clasificar una acción", "Una comunidad costera construye un muro para proteger casas de las marejadas. ¿Es mitigación, adaptación o restauración?",
         ["El muro no reduce las emisiones ni recupera un ecosistema.", "Ayuda a ajustarse a un efecto.", "Eso es adaptación."],
         "Adaptación"),
        ("CO2 de la combustión", "Se queman 48 g de metano. ¿Cuántos gramos de CO2 se producen? Recuerda que 16 g de CH4 producen 44 g de CO2.",
         ["48 g de metano son 48 ÷ 16 = 3 veces la cantidad base.", "El CO2 es 3 × 44.", "El resultado es 132 g."],
         "132 g de CO2"),
    ],
    mistakes=[("Confundir adaptación con mitigación.", "La mitigación reduce la causa (emisiones); la adaptación disminuye el daño de los efectos.", "Pregunta: ¿la acción reduce emisiones o ayuda a convivir con los efectos?"),
              ("Creer que la masa de CO2 es igual a la masa de metano quemado.", "El CO2 incluye el oxígeno del aire, por lo que su masa es mayor.", "Usa la proporción de masas de la reacción.")],
    T=[
        ("abc", "En Química: ¿qué es la mitigación del cambio climático?", "Reducir las emisiones o aumentar los sumideros de carbono", "Ajustarse a los efectos del cambio climático", "Recuperar un ecosistema dañado", "Mitigar actúa sobre la causa: menos emisiones o más absorción."),
        ("{F} ¿Cuál de las tres preguntas (P1, P2 o P3) se puede responder con un cálculo de masas?", "P2", "P2 nombra una masa y una reacción de la ficha, de modo que se calcula."),
        ("=", "{F} ¿Cuál es la masa molar del metano (CH4)?", "12+4*1", "Se suma la masa del carbono y la de cuatro hidrógenos.", " g/mol"),
        ("=", "{F} ¿Cuál es la masa molar del CO2?", "12+2*16", "Se suma la masa del carbono y la de dos oxígenos.", " g/mol"),
        ("=", "{F} Se queman 64 g de metano. ¿Cuántos gramos de CO2 se producen?", "64/16*44", "Se calcula cuántas veces cabe 16 g en 64 g y se multiplica por los 44 g de CO2.", " g"),
        ("abc", "Se reforesta un terreno para que los árboles absorban CO2. ¿Qué tipo de acción es?", "Mitigación, porque aumenta un sumidero de carbono", "Adaptación, porque cambia el clima", "Ninguna de las tres", "Los bosques absorben carbono, así que aumentan los sumideros."),
        ("abc", "Un pueblo instala un sistema de alerta de inundaciones. ¿Qué tipo de acción es?", "Adaptación", "Mitigación", "Restauración", "Ayuda a la población a convivir con un efecto, sin reducir emisiones."),
        ("abc", "Se recupera un humedal degradado con plantas nativas. ¿Qué tipo de acción es?", "Restauración", "Mitigación únicamente", "Adaptación únicamente", "Se recupera un ecosistema dañado, que es restaurar."),
        ("=", "{F} ¿Cuántos gramos de CO2 produce la combustión completa de 1 mol de octano (114 g)?", "8*(12+2*16)", "Cada mol de octano produce 8 mol de CO2 de 44 g cada uno.", " g"),
        ("ab", "{F} ¿Qué mejora la pregunta P3 «¿qué es mejor, mitigar o adaptar?»?", "Comparar, para un mismo lugar, el costo y la reducción de riesgo de una medida de cada tipo", "Responderla igual para todo el mundo", "Una comparación necesita sitio, criterios y datos concretos."),
        ("abc", "{F} ¿Por qué P1 «¿Cómo ayuda la química al clima?» está mal delimitada?", "Es tan amplia que no nombra tecnología, variable ni resultado medible", "Porque nombra la química", "Porque es demasiado específica", "Sin tecnología ni variable no se puede responder con datos."),
        ("=", "{F} Se queman 64 g de metano y una tecnología de captura retiene 75 % del CO2. ¿Cuántos gramos de CO2 llegan a la atmósfera?", "64/16*44*(100-75)/100", "Se calcula el CO2 producido y se multiplica por la fracción que no se captura.", " g"),
        ("=", "{F} Una cocina de ejemplo quemaba 64 g de metano y ahora quema solo 32 g por un cambio de hábitos. ¿Cuántos gramos de CO2 se evitan?", "64/16*44-32/16*44", "Se resta el CO2 producido con 32 g del producido con 64 g de metano.", " g"),
    ],
    ctx=("abc", "Contexto: una escuela de ejemplo quiere proponer un proyecto sobre clima. ¿Qué pregunta delimitada elige?", "¿Cuántos gramos de CO2 se evitan al año si el casino reemplaza una cocina a gas por otra eléctrica con electricidad renovable?", "¿Qué se puede hacer por el clima?", "¿La química arregla el clima?", "La pregunta elegida nombra una tecnología, una variable y un resultado calculable."),
    sc=[
        ("En Química: ¿qué es un sumidero de carbono?", "Un sistema que absorbe más carbono del que emite", "Los bosques y los océanos son sumideros de carbono."),
        ("ab", "Adaptar significa:", "Ajustarse a los efectos del cambio climático", "Reducir la causa de las emisiones", "La adaptación disminuye el daño de los efectos."),
        ("ab", "Al quemar metano, la masa de CO2 producida es:", "Mayor que la masa de metano", "Igual que la masa de metano", "El CO2 incluye el oxígeno del aire."),
    ],
    op=("Con la ficha {F}: (1) escribe una pregunta delimitada sobre una tecnología (energía, transporte, materiales o tratamiento de agua) y el clima; (2) clasifícala como mitigación, adaptación o restauración; (3) escribe cómo la responderías con un cálculo o con datos de ejemplo.",
        "(1) ¿Cuántos gramos de CO2 se evitan al dejar de quemar 64 g de metano en una cocina? (2) Mitigación. (3) Con la proporción de masas: 64 ÷ 16 × 44 = 176 g de CO2 que se dejan de emitir.",
        ["pregunta delimitada", "clasificación correcta", "método de respuesta"],
        ["tres respuestas numeradas"],
        ["pregunta demasiado amplia", "confundir adaptación con mitigación", "no indicar cómo responder"],
        "Pregunta: «¿qué dato real usarías en vez del dato de ejemplo?»."),
    reinforce="Clasifica cinco acciones frente al clima en mitigación, adaptación o restauración y justifica cada una en una frase.",
    extend="Explica por qué la masa de CO2 producida al quemar un combustible es mayor que la masa del combustible.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (datos de ejemplo). Factores de emisión de ejemplo de transporte de pasajeros, en g de CO2 por kilómetro y por persona: auto de combustión con un ocupante: 150; auto eléctrico con la mezcla eléctrica de ejemplo: 60; bus urbano lleno: 30. Si la electricidad proviene de más energías renovables, el factor del auto eléctrico baja a 30. "
     "Distancia anual de ejemplo: 10.000 km. 1 tonelada equivale a 1.000.000 g. Fuente A: análisis de ciclo de vida (estudio que suma las emisiones de fabricar, usar y desechar) con método, supuestos y datos publicados. Fuente B: aviso que dice «100 % limpio» sin datos. "
     "Variables: tipo de vehículo, mezcla eléctrica, ocupación y distancia.")
build(
    O6, 2, F,
    use="Aprenderé a evaluar fuentes y variables cuando se comparan tecnologías para reducir emisiones: factores de emisión, ciclo de vida y condiciones como la mezcla eléctrica. Sirve para no creer afirmaciones como «100 % limpio» sin datos.",
    prior=["Sé calcular porcentajes y toneladas.", "Sé qué son las variables independiente y dependiente.", "Sé que la electricidad se genera de distintas fuentes."],
    explain=[
        "El factor de emisión es la masa de CO2 que se emite por unidad de actividad, por ejemplo gramos de CO2 por kilómetro y por persona. Con él se calcula la emisión anual: factor × distancia. Un vehículo de 100 g/km que recorre 5.000 km emite 500.000 g, es decir, 0,5 toneladas de CO2 al año. Comparar factores permite estimar cuánto se reduce al cambiar de tecnología.",
        "Para comparar de forma justa hay que controlar variables y mirar todo el ciclo de vida. Un auto eléctrico no emite CO2 al circular, pero la electricidad que usa puede emitirlo al generarse, y fabricarlo y su batería también emiten. Por eso su factor depende de la mezcla eléctrica, la variable que cambia entre 60 y 30 g/km en la ficha. La ocupación también importa: un auto con tres personas reparte su emisión entre tres.",
        "Al evaluar fuentes, un análisis de ciclo de vida con método y supuestos publicados es más confiable que un aviso que dice «100 % limpio» sin datos. Una conclusión debe decir bajo qué condiciones se cumple, por ejemplo «con la mezcla eléctrica de ejemplo». Generalizar sin condiciones es un error frecuente.",
    ],
    vocab=[("factor de emisión", "masa de CO2 emitida por unidad de actividad"), ("ciclo de vida", "conjunto de etapas de fabricar, usar y desechar un producto"), ("mezcla eléctrica", "proporción de fuentes con que se genera la electricidad"), ("ocupación", "número de personas que comparten un vehículo"), ("condición", "valor de una variable bajo el cual se cumple una conclusión")],
    worked=[
        ("Emisión anual", "Un vehículo de ejemplo tiene 80 g/km por persona y recorre 20.000 km al año. ¿Cuántas toneladas de CO2 emite?",
         ["Emisión: 80 × 20.000 = 1.600.000 g.", "1 tonelada son 1.000.000 g.", "1.600.000 ÷ 1.000.000 = 1,6 toneladas."],
         "1,6 toneladas"),
        ("Variable que cambia", "En la comparación del auto eléctrico con 60 y 30 g/km, ¿qué variable cambió?",
         ["El tipo de vehículo y la distancia no cambiaron.", "Lo que cambió fue el origen de la electricidad.", "Esa es la mezcla eléctrica."],
         "La mezcla eléctrica"),
    ],
    mistakes=[("Decir que el auto eléctrico «no emite nada».", "No emite al circular, pero fabricarlo y generar su electricidad pueden emitir.", "Mira el ciclo de vida y la mezcla eléctrica."),
              ("Generalizar una comparación a cualquier país o año.", "Los factores dependen de la mezcla eléctrica y las condiciones.", "Escribe la condición bajo la que se cumple.")],
    T=[
        ("abc", "En Química: ¿qué es un factor de emisión?", "La masa de CO2 emitida por unidad de actividad", "La temperatura de un motor", "El costo de un vehículo", "Se expresa, por ejemplo, en g de CO2 por kilómetro."),
        ("{F} ¿Qué transporte tiene el menor factor de emisión con la mezcla eléctrica de ejemplo?", "El bus urbano lleno, con 30 g/km", "Entre 150, 60 y 30 g/km, el menor es el del bus."),
        ("=", "{F} ¿Cuántas toneladas de CO2 al año emite el auto de combustión en la distancia anual de ejemplo?", "10000*150/1000000", "Se multiplica el factor por los kilómetros y se convierte de gramos a toneladas.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas de CO2 al año emite el auto eléctrico con la mezcla de ejemplo?", "10000*60/1000000", "Se multiplica el factor por los kilómetros y se convierte a toneladas.", " toneladas"),
        ("=", "{F} ¿Cuál es el cambio porcentual del factor de emisión al pasar del auto de combustión al eléctrico con la mezcla de ejemplo?", "(60-150)*100/150", "Se divide la diferencia por el valor de comparación (150) y se multiplica por 100.", " %"),
        ("=", "{F} Con la mezcla más renovable, ¿cuántas toneladas al año emite el auto eléctrico?", "10000*30/1000000", "Se usa el factor de 30 g/km y se convierte a toneladas.", " toneladas"),
        ("abc", "{F} Al comparar el auto eléctrico con 60 y 30 g/km, ¿cuál es la variable independiente?", "La mezcla eléctrica", "La distancia anual", "El tipo de vehículo", "Es la que cambia entre ambos casos."),
        ("abc", "{F} ¿Qué problema tiene la fuente B («100 % limpio»)?", "No entrega datos ni método ni considera el ciclo de vida", "Usa números", "Es demasiado larga", "Una afirmación absoluta sin datos no se puede evaluar."),
        ("=", "{F} Un auto de combustión (150 g/km por un ocupante) lleva 3 ocupantes. ¿Cuántos g de CO2 por km y por persona emite?", "150/3", "La emisión del auto se reparte entre los ocupantes.", " g/km por persona"),
        ("ab", "{F} ¿Por qué no basta comparar solo las emisiones al circular?", "Porque no incluyen la fabricación ni la generación de la electricidad", "Porque circular no emite nada", "El ciclo de vida suma todas las etapas, no solo el uso."),
        ("abc", "{F} ¿Qué conclusión respeta los datos?", "Con la mezcla eléctrica de ejemplo, el auto eléctrico emite 60 % menos CO2 por km que el de combustión de un ocupante", "El auto eléctrico siempre emite 60 % menos en cualquier país", "El auto eléctrico no emite CO2", "La conclusión correcta incluye la condición de la mezcla de ejemplo."),
        ("=", "{F} Al año, ¿cuántas toneladas menos emite el auto eléctrico con mezcla renovable que el de combustión?", "(150-30)*10000/1000000", "Se multiplica la diferencia de factores por los kilómetros y se convierte a toneladas.", " toneladas"),
        ("abc", "{F} Si solo se quiere comparar el efecto de la mezcla eléctrica sobre el auto eléctrico, ¿qué debe mantenerse igual?", "El tipo de vehículo, la distancia y la ocupación", "La mezcla eléctrica", "El factor de emisión que se quiere medir", "Solo cambia la mezcla; lo demás se mantiene igual para atribuir el efecto."),
    ],
    ctx=("abc", "Contexto: una empresa de buses de ejemplo anuncia «100 % limpio». Te piden verificar. ¿Qué haces primero?", "Pedir el análisis de ciclo de vida con método, supuestos y datos", "Aceptar el anuncio por ser de una empresa", "Rechazarlo sin mirar", "Una afirmación absoluta se verifica con datos y método publicados."),
    sc=[
        ("En Química: ¿qué es un análisis de ciclo de vida?", "Un estudio que suma las emisiones de fabricar, usar y desechar un producto", "Incluye todas las etapas, no solo el uso."),
        ("ab", "La ocupación de un auto afecta:", "La emisión por persona", "La masa molar del CO2", "Dividir la emisión entre más personas la reduce por persona."),
        ("ab", "Una conclusión sobre vehículos debe indicar:", "La condición bajo la que se cumple", "Que vale para cualquier caso", "Los factores dependen de las condiciones."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula la emisión anual de dos tecnologías; (2) clasifica las variables de la comparación (la que cambia, la que se mide, dos controladas); (3) escribe una conclusión con su condición y una limitación.",
        "(1) Combustión: 1,5 t; bus lleno para 10.000 km: 0,3 t. (2) Cambia el tipo de transporte; se mide la emisión anual; se mantienen la distancia y la ocupación del bus. (3) Con la ocupación de ejemplo, el bus emite 80 % menos que el auto de un ocupante; falta incluir el ciclo de vida completo.",
        ["dos emisiones anuales", "variables clasificadas", "conclusión con condición", "limitación"],
        ["tres respuestas numeradas"],
        ["no convertir gramos a toneladas", "generalizar sin condición", "olvidar el ciclo de vida"],
        "Pregunta: «¿qué variable cambiarías para ver otro escenario?»."),
    reinforce="Calcula la emisión anual del bus lleno para 10.000 km y compárala con la del auto de combustión.",
    extend="Explica por qué la misma tecnología puede ser más o menos limpia según la mezcla eléctrica del país.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (datos de ejemplo; los modelos son conceptuales y no describen procedimientos). Masas atómicas que se entregan: H = 1, C = 12, O = 16, Ca = 40. "
     "Modelo A (hidrógeno con electricidad renovable): 2 H2O → 2 H2 + O2; 36 g de agua producen 4 g de H2 y 32 g de O2. Modelo B (mineralización del CO2): CO2 + CaO → CaCO3; la masa molar del CO2 es 44, la del CaO es 56 y la del CaCO3 es 100. "
     "Modelo C (sumidero): un bosque restaurado almacena una cantidad de carbono (C) por año; para convertir masa de carbono a masa de CO2 se multiplica por 44 ÷ 12.")
build(
    O6, 3, F,
    use="Aprenderé a interpretar tres modelos químicos usados frente al cambio climático: hidrógeno a partir de agua, mineralización del CO2 y sumideros de carbono. Sirve para calcular masas, seguir la conservación de la masa y reconocer los supuestos y límites de cada modelo.",
    prior=["Sé calcular masas molares.", "Sé que la masa se conserva en una reacción.", "Sé hacer proporciones."],
    explain=[
        "El hidrógeno puede producirse separando el agua: 2 H2O → 2 H2 + O2. Si la electricidad usada viene de fuentes renovables, el proceso no emite CO2 directamente, y el hidrógeno puede usarse como combustible que al reaccionar solo da agua. Pero si esa electricidad viene de combustibles fósiles, las emisiones se trasladan a otro lugar. La masa se conserva: 36 g de agua dan 4 g de hidrógeno más 32 g de oxígeno.",
        "La mineralización del CO2 es un modelo en el que el CO2 se combina con un óxido como el CaO para formar un carbonato estable: CO2 + CaO → CaCO3. Con las masas molares se calcula cuánto CO2 puede fijarse: 44 g de CO2 con 56 g de CaO forman 100 g de CaCO3. El modelo no incluye el origen del CaO ni la energía para obtenerlo, lo que puede significar emisiones adicionales.",
        "Los sumideros son sistemas que absorben carbono, como un bosque restaurado. La masa de carbono se convierte en masa de CO2 multiplicando por 44 ÷ 12, porque cada átomo de carbono (12) corresponde a una molécula de CO2 (44). Todos los modelos de la clase suponen condiciones ideales: no consideran pérdidas, costos ni la duración del almacenamiento.",
    ],
    vocab=[("hidrógeno (H2)", "gas que puede usarse como combustible y al reaccionar da agua"), ("mineralización del CO2", "fijación del CO2 en un carbonato sólido estable"), ("sumidero de carbono", "sistema que absorbe más carbono del que emite"), ("conservación de la masa", "la masa de los productos es igual a la de los reactivos"), ("supuesto", "condición que el modelo da por cierta")],
    worked=[
        ("Conservación de la masa", "Con el modelo A, ¿cuántos gramos de H2 y O2 en total se forman a partir de 36 g de agua?",
         ["Se forman 4 g de H2 y 32 g de O2.", "Suma: 4 + 32.", "El total es 36 g, igual que el agua que reaccionó."],
         "36 g"),
        ("De carbono a CO2", "Un bosque de ejemplo almacena 9 toneladas de carbono. ¿A cuántas toneladas de CO2 equivale?",
         ["Se multiplica por 44 ÷ 12.", "9 × 44 ÷ 12 = 396 ÷ 12.", "El resultado es 33 toneladas."],
         "33 toneladas de CO2"),
    ],
    mistakes=[("Creer que producir hidrógeno nunca emite CO2.", "Depende de cuánto emitió la generación de la electricidad usada.", "Pregunta siempre de dónde viene la electricidad."),
              ("Olvidar que el modelo B necesita CaO y que obtenerlo requiere energía.", "El modelo no incluye ese costo, que puede emitir CO2.", "Declara el supuesto y la parte que el modelo deja fuera.")],
    T=[
        ("abc", "En Química: ¿qué es un sumidero de carbono?", "Un sistema que absorbe más carbono del que emite", "Un lugar donde se produce CO2", "Un tipo de combustible", "Un sumidero retira carbono de la atmósfera."),
        ("=", "{F} ¿Cuál es la masa molar del agua (H2O)?", "2*1+16", "Se suman las masas de dos hidrógenos y un oxígeno.", " g/mol"),
        ("=", "{F} Se separan 72 g de agua. ¿Cuántos gramos de O2 se forman?", "72/36*32", "72 g son el doble de 36 g, así que se forma el doble de O2: dos veces 32 g.", " g"),
        ("=", "{F} ¿Cuántos gramos de H2 se forman a partir de 180 g de agua?", "180*4/36", "Se calcula cuántas veces cabe 36 g en 180 g y se multiplica por los 4 g de H2.", " g"),
        ("abc", "{F} ¿Por qué importa de dónde viene la electricidad para producir hidrógeno del agua?", "Porque si viene de combustibles fósiles, las emisiones se trasladan a otro lugar", "Porque el agua no conduce nada", "Porque el hidrógeno no es un combustible", "El proceso es limpio solo en la medida en que lo es su electricidad."),
        ("=", "{F} ¿Cuántos gramos de CaCO3 se forman a partir de 88 g de CO2 según el modelo B?", "88/44*100", "Se calcula cuántas veces cabe 44 g en 88 g y se multiplica por 100 g de CaCO3.", " g"),
        ("=", "{F} ¿Cuántos gramos de CaO se necesitan para fijar 88 g de CO2 según el modelo B?", "88/44*56", "Se calcula cuántas veces cabe 44 g en 88 g y se multiplica por 56 g de CaO.", " g"),
        ("abc", "{F} En el modelo B, ¿qué se conserva?", "La masa: 44 g de CO2 más 56 g de CaO dan 100 g de CaCO3", "El número de gramos de CO2 sin cambio", "La energía como si fuera masa", "La suma de masas de reactivos es igual a la del producto."),
        ("=", "{F} Un bosque de ejemplo almacena 3 toneladas de carbono. ¿A cuántas toneladas de CO2 equivale?", "3*44/12", "Se multiplica por 44 ÷ 12 para convertir masa de carbono a masa de CO2.", " toneladas"),
        ("ab", "{F} ¿Qué supuesto hace el modelo C del bosque?", "Que el carbono almacenado se mantiene y el bosque no se quema ni se tala", "Que el bosque crece sin ninguna condición", "Si el bosque se quema, el carbono vuelve a la atmósfera, por lo que el modelo supone que se mantiene."),
        ("abc", "{F} ¿Qué limitación tiene el modelo B?", "No incluye el origen del CaO ni la energía para obtenerlo, que pueden emitir CO2", "No usa masas", "Solo funciona con agua", "El modelo omite los costos de obtener el óxido."),
        ("abc", "Para comparar dos tecnologías con un mismo modelo, ¿qué se debe mantener igual?", "Las condiciones y supuestos con que se calcula cada una", "El resultado que se espera", "El nombre de la tecnología", "Controlar condiciones permite comparar con justicia."),
        ("=", "{F} Un proyecto almacena 6 toneladas de carbono por año. Una empresa emite 50 toneladas de CO2 por año. ¿Qué porcentaje de sus emisiones compensa el proyecto?", "6*44/12*100/50", "Se convierte el carbono a CO2, se divide por las emisiones de la empresa y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Contexto: una empresa de ejemplo anuncia que fija CO2 con el modelo B y que por eso «no emite». ¿Qué pregunta de evaluación es la más importante?", "¿Cuánta energía y cuántas emisiones requiere obtener el CaO y la operación del proceso?", "¿De qué color es el producto final?", "¿Cuántas personas trabajan en la empresa?", "Un modelo se evalúa por lo que deja fuera, aquí el costo en energía y emisiones."),
    sc=[
        ("En Química: ¿qué es la conservación de la masa?", "La masa de los productos es igual a la de los reactivos", "Los átomos no se crean ni se destruyen en una reacción."),
        ("ab", "Para convertir masa de C a masa de CO2 se multiplica por:", "44 ÷ 12", "12 ÷ 44", "Cada 12 g de carbono corresponden a 44 g de CO2."),
        ("ab", "Un modelo conceptual:", "Declara supuestos y límites", "Asegura el resultado en la práctica", "Un modelo simplifica y debe informar lo que deja fuera."),
    ],
    op=("Con los modelos de la ficha {F}: (1) elige uno (A, B o C) y haz un cálculo con datos de la ficha; (2) explica qué muestra la conservación de la masa; (3) escribe un supuesto y una limitación.",
        "(1) Modelo B: 44 g de CO2 forman 100 g de CaCO3. Con 132 g de CO2, se forman 300 g de CaCO3. (2) La masa de CO2 más CaO es igual a la de CaCO3. (3) Supone que todo el CO2 reacciona y no incluye la energía para obtener el CaO.",
        ["cálculo correcto", "conservación explicada", "supuesto y limitación"],
        ["tres respuestas numeradas"],
        ["no usar las proporciones de masa", "olvidar el origen de la energía", "no declarar supuestos"],
        "Pregunta: «¿qué dato real pedirías para evaluar la tecnología?»."),
    reinforce="Calcula cuántos gramos de H2 se forman a partir de 72 g de agua y comprueba la conservación de la masa.",
    extend="Explica por qué un modelo que solo calcula masas no basta para decidir si una tecnología reduce el cambio climático.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (datos de ejemplo). Ciclo de vida de dos autos: auto convencional: fabricación 6 t de CO2; uso 150 g de CO2 por km. Auto eléctrico: fabricación 15 t de CO2; uso 60 g de CO2 por km (mezcla eléctrica de ejemplo). Punto de equilibrio: distancia desde la cual el total acumulado del auto eléctrico es menor que el del convencional. 1 t = 1.000.000 g. "
     "Humedal restaurado de ejemplo: almacena 2 t de carbono por hectárea y año; área restaurada: 60 hectáreas; carbono a CO2: multiplicar por 44 ÷ 12. "
     "Planta de ejemplo con captura de CO2: sin captura emite 1.000 t de CO2 al año; con captura retiene el 80 % de ellas, y el sistema de captura consume energía que agrega 100 t de CO2 al año. Lago acidificado de ejemplo: pH 5 antes de una medida y 6 después.")
build(
    O6, 4, F,
    use="Aprenderé a analizar evidencia sobre tecnologías y restauración frente al cambio climático: punto de equilibrio en el ciclo de vida, captura neta y sumideros. Sirve para evaluar cuánto contribuyen realmente y con qué límites.",
    prior=["Sé resolver ecuaciones simples de proporción.", "Sé calcular porcentajes.", "Sé que el pH es logarítmico."],
    explain=[
        "Al analizar el ciclo de vida de dos tecnologías, una puede emitir más al fabricarse y menos al usarse. El punto de equilibrio es la distancia desde la cual el total acumulado de una es menor que el de la otra. Se calcula dividiendo la diferencia de emisiones de fabricación por la diferencia de emisiones de uso por kilómetro. Por ejemplo, si un auto cuesta 4 t más de fabricar y ahorra 80 g/km, el punto de equilibrio está en 4.000.000 ÷ 80 = 50.000 km.",
        "En captura de CO2, el resultado neto debe incluir la energía que consume la propia captura. Si una planta captura el 80 % de sus emisiones pero agrega emisiones por el uso de energía, la reducción neta es menor al 80 %. Para sumideros como un humedal restaurado, el cálculo es área por carbono almacenado por hectárea, convertido a CO2, siempre que ese carbono se mantenga almacenado.",
        "En restauración, un cambio de pH de 4 a 6 en un lago reduce la concentración de H+ 100 veces, pero la recuperación de los organismos puede tardar más y depende de otras variables. Una conclusión sólida dice qué cambia, cuánto y en qué condiciones, y reconoce qué no está medido.",
    ],
    vocab=[("punto de equilibrio", "distancia desde la cual una tecnología acumula menos emisiones que otra"), ("emisión neta", "emisión total menos lo que se retira, incluyendo la energía de la captura"), ("captura de CO2", "retención del CO2 antes de que llegue a la atmósfera"), ("hectárea", "unidad de superficie de 10.000 metros cuadrados"), ("restauración", "recuperación de un ecosistema dañado")],
    worked=[
        ("Emisión acumulada", "Un auto de ejemplo tiene 5 t de fabricación y 100 g de uso por km. ¿Cuántas toneladas acumula tras 50.000 km?",
         ["Uso: 100 × 50.000 = 5.000.000 g = 5 t.", "Fabricación: 5 t.", "Total: 5 + 5 = 10 t."],
         "10 toneladas"),
        ("Emisión neta de la planta", "Una planta de ejemplo emite 500 t sin captura, captura 60 % y su sistema agrega 50 t. ¿Cuál es la emisión neta?",
         ["Emisión con captura: 500 × (100 − 60) ÷ 100 = 200 t.", "Se agregan 50 t por la energía.", "Total: 200 + 50 = 250 t."],
         "250 toneladas"),
    ],
    mistakes=[("Decir que la planta con captura reduce exactamente el 80 % de sus emisiones.", "El sistema de captura consume energía que agrega emisiones.", "Calcula la emisión neta."),
              ("Afirmar que el auto eléctrico siempre emite menos desde el primer kilómetro.", "Parte con más emisiones de fabricación, y el ahorro aparece con el uso.", "Calcula el punto de equilibrio.")],
    T=[
        ("abc", "En Química: ¿qué es el punto de equilibrio en la comparación de dos autos?", "La distancia desde la cual uno acumula menos emisiones que el otro", "La velocidad en que ambos se encuentran", "El precio de ambos autos", "Es la distancia donde los totales acumulados se igualan y después cambia cuál es menor."),
        ("=", "{F} ¿Cuántas toneladas de CO2 acumula el auto convencional a los 200.000 km (fabricación más uso)?", "6+150*200000/1000000", "Se suman la fabricación y el uso, convertido de gramos a toneladas.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas acumula el auto eléctrico a los 200.000 km?", "15+60*200000/1000000", "Se suman la fabricación y el uso en toneladas.", " toneladas"),
        ("=", "{F} ¿A cuántos km se alcanza el punto de equilibrio entre ambos autos?", "(15-6)*1000000/(150-60)", "Se divide la diferencia de fabricación, en gramos, por el ahorro en gramos por kilómetro.", " km"),
        ("abc", "{F} ¿Qué conclusión respeta los datos?", "Antes del punto de equilibrio el eléctrico acumula más; después, menos", "El eléctrico acumula menos desde el primer kilómetro", "El convencional siempre acumula menos", "La fabricación del eléctrico es mayor y el ahorro aparece con el uso."),
        ("=", "{F} ¿Cuántas toneladas de CO2 equivale el carbono que almacena al año el humedal restaurado de ejemplo (60 hectáreas)?", "60*2*44/12", "Se calcula el carbono total y se convierte a CO2 multiplicando por 44 ÷ 12.", " toneladas"),
        ("=", "{F} ¿Cuál es la emisión neta de la planta de ejemplo con captura, incluyendo la energía del sistema?", "1000*(100-80)/100+100", "Se calcula lo que no se captura y se suman las emisiones de la propia captura.", " toneladas"),
        ("=", "{F} ¿Qué porcentaje de reducción neta logra la planta de ejemplo respecto de su emisión sin captura?", "(1000-300)*100/1000", "Se divide la reducción neta por la emisión sin captura y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Por qué la reducción neta de la planta es 70 % y no 80 %?", "Porque el sistema de captura consume energía que agrega emisiones", "Porque la captura no funciona", "Porque 80 % no puede lograrse nunca", "Hay emisiones adicionales por la energía usada."),
        ("abc", "{F} El pH del lago pasó de 5 a 6. ¿Qué ocurrió con la concentración de H+?", "Disminuyó 10 veces", "Aumentó 10 veces", "No cambió", "Una unidad más de pH significa diez veces menos H+."),
        ("ab", "{F} ¿Qué limitación tiene el dato del humedal de ejemplo?", "Que el valor por hectárea y año depende del clima y de las especies, y debe medirse en el lugar", "Que se mide en hectáreas", "El valor es de ejemplo; en un sitio real depende de condiciones locales."),
        ("abc", "{F} Un estudiante dice: «el auto eléctrico emite cero». ¿Qué responde la ficha?", "Fabricarlo emite 15 t y usarlo emite 60 g por km con la mezcla de ejemplo", "Tiene razón: no emite nada", "Emite más que el convencional siempre", "La ficha muestra emisiones de fabricación y de uso."),
        ("=", "{F} Con una mezcla eléctrica más renovable, el uso del auto eléctrico baja a 30 g/km. ¿A cuántos km sería el punto de equilibrio?", "(15-6)*1000000/(150-30)", "Se divide la diferencia de fabricación, en gramos, por el nuevo ahorro por kilómetro.", " km"),
    ],
    ctx=("abc", "Contexto: una ciudad de ejemplo decide cambiar su flota de taxis y debe estimar cuándo ahorrará emisiones. ¿Qué dato necesita primero?", "La distancia que recorrerá cada vehículo, para compararla con el punto de equilibrio", "El color de los vehículos", "El número de ventanas", "El ahorro depende de que los vehículos superen el punto de equilibrio."),
    sc=[
        ("En Química: ¿qué es la emisión neta?", "La emisión total menos lo que se retira, incluyendo la energía de la captura", "Considera tanto lo retirado como lo agregado."),
        ("ab", "Una hectárea equivale a:", "10.000 metros cuadrados", "100 metros cuadrados", "Es la unidad habitual de superficie en restauración."),
        ("ab", "El pH sube una unidad. La concentración de H+:", "Baja 10 veces", "Sube 10 veces", "La escala de pH es logarítmica, de factor diez por unidad."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula el punto de equilibrio o la emisión neta de la planta; (2) escribe una conclusión con su condición; (3) indica una limitación de los datos y qué medición real pedirías.",
        "(1) Emisión neta de la planta: 300 t. (2) Con captura del 80 % y energía adicional, la reducción neta es del 70 %. (3) Los datos son de ejemplo; pediría la medición real de energía del sistema.",
        ["cálculo correcto", "conclusión con condición", "limitación y medición propuesta"],
        ["tres respuestas numeradas"],
        ["ignorar la energía de la captura", "no convertir unidades", "generalizar sin condición"],
        "Pregunta: «¿qué haría cambiar el punto de equilibrio?»."),
    reinforce="Calcula la emisión acumulada de ambos autos a los 100.000 km y comprueba el punto de equilibrio.",
    extend="Explica por qué una tecnología con mayor emisión de fabricación puede ser mejor a largo plazo si se usa mucho.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (datos de ejemplo). Tres propuestas para una cuenca afectada por un incendio y una laguna con menos agua: Propuesta 1, reforestar con especies nativas (aumenta un sumidero, restaura el ecosistema y retiene agua del suelo); Propuesta 2, instalar una planta de captura de CO2 en una industria cercana (mitigación); Propuesta 3, construir un embalse pequeño para guardar agua (adaptación). "
     "Puntajes de ejemplo de 1 a 3 (3 es lo mejor) y pesos: reducción de emisiones o de riesgo (peso 3): P1 = 2; P2 = 3; P3 = 1. Costo (peso 2): P1 = 3; P2 = 1; P3 = 2. Beneficios para el ecosistema y la comunidad (peso 3): P1 = 3; P2 = 1; P3 = 2. Plazo en que da resultados (peso 1): P1 = 1; P2 = 3; P3 = 2. "
     "Puntaje total = suma de peso × puntaje en los cuatro criterios.")
build(
    O6, 5, F,
    use="Aprenderé a comparar soluciones químicas y de restauración frente al cambio climático con una matriz de criterios y pesos, y a ver cómo cambia el orden si cambian los pesos. Sirve para evaluar contribuciones con honestidad y reconocer lo que cada opción no resuelve.",
    prior=["Sé calcular una matriz de criterios y pesos.", "Sé la diferencia entre mitigación, adaptación y restauración.", "Sé comparar con criterios."],
    explain=[
        "Comparar soluciones frente al cambio climático exige criterios explícitos, por ejemplo cuánto reducen las emisiones o el riesgo, cuánto cuestan, qué beneficios dan al ecosistema y a la comunidad, y en qué plazo dan resultados. Cada criterio recibe un peso según su importancia, y cada propuesta un puntaje. El total es la suma de peso por puntaje en todos los criterios.",
        "Algunas propuestas combinan objetivos: reforestar con especies nativas es restauración, porque recupera un ecosistema; mitigación, porque el bosque es un sumidero; y adaptación, porque el suelo retiene agua. Otras se concentran en uno solo: la captura de CO2 reduce emisiones, y el embalse ayuda a convivir con la falta de agua. Ningún tipo de acción reemplaza a los otros.",
        "La matriz depende de los pesos elegidos. Si se cambia el peso de un criterio, el orden puede cambiar, como ocurre si el plazo gana importancia. Por eso la decisión debe mostrar sus pesos, probar qué pasa al variarlos y reconocer criterios que faltan, como el mantenimiento a largo plazo. Quién fija los pesos es una decisión de la comunidad.",
    ],
    vocab=[("criterio", "aspecto con el que se juzga una propuesta"), ("peso", "importancia que se da a un criterio"), ("puntaje total", "suma de peso por puntaje en todos los criterios"), ("restauración ecológica", "ayudar a recuperar un ecosistema dañado"), ("sensibilidad", "cuánto cambia el resultado al variar un peso")],
    worked=[
        ("Puntaje total", "Con otra propuesta de ejemplo: reducción (peso 3) = 2; costo (peso 2) = 2; beneficios (peso 3) = 1; plazo (peso 1) = 3. ¿Cuál es su total?",
         ["Reducción: 3 × 2 = 6; costo: 2 × 2 = 4.", "Beneficios: 3 × 1 = 3; plazo: 1 × 3 = 3.", "Total: 6 + 4 + 3 + 3 = 16."],
         "16 puntos"),
        ("Efecto de un peso", "Si el peso del plazo pasara de 1 a 3 en esa propuesta, ¿cuánto sube su total?",
         ["Puntaje en plazo: 3.", "El producto pasa de 1 × 3 = 3 a 3 × 3 = 9.", "Sube 9 − 3 = 6 puntos."],
         "6 puntos"),
    ],
    mistakes=[("Elegir la propuesta de mayor puntaje sin revisar cómo dependen los pesos.", "Un cambio de pesos puede alterar el orden.", "Prueba al menos un cambio de pesos."),
              ("Creer que una propuesta resuelve todos los problemas.", "Cada propuesta resuelve ciertos criterios y deja otros pendientes.", "Anota qué no resuelve cada una.")],
    T=[
        ("abc", "En Química: ¿qué es la restauración ecológica?", "Ayudar a recuperar un ecosistema dañado", "Construir una obra de ingeniería", "Eliminar toda actividad humana", "La restauración apunta a recuperar el ecosistema."),
        ("=", "{F} ¿Cuál es el puntaje total de la Propuesta 1?", "3*2+2*3+3*3+1*1", "Se multiplica cada peso por el puntaje de P1 y se suman los cuatro productos.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la Propuesta 2?", "3*3+2*1+3*1+1*3", "Se multiplica cada peso por el puntaje de P2 y se suman.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la Propuesta 3?", "3*1+2*2+3*2+1*2", "Se multiplica cada peso por el puntaje de P3 y se suman.", " puntos"),
        ("abc", "{F} Con los pesos de la ficha, ¿qué propuesta tiene el mayor puntaje?", "La Propuesta 1", "La Propuesta 2", "La Propuesta 3", "P1 suma 22, más que P2 y P3."),
        ("=", "{F} Si el peso del plazo subiera a 4 (los demás igual), ¿cuál sería el total de la Propuesta 2?", "3*3+2*1+3*1+4*3", "Se recalcula con peso 4 en el plazo.", " puntos"),
        ("=", "{F} Con el peso del plazo en 4, ¿cuál sería el total de la Propuesta 1?", "3*2+2*3+3*3+4*1", "Se recalcula con peso 4 en el plazo.", " puntos"),
        ("abc", "{F} Con el peso del plazo en 4, ¿qué pasa con el orden entre P1 y P2?", "P2 supera a P1", "P1 sigue superando a P2", "Quedan empatadas", "P2 suma 26 y P1 suma 25."),
        ("abc", "{F} ¿Qué enseña el cambio de orden al variar el peso del plazo?", "Que el resultado de la matriz depende de los pesos que se elijan", "Que la matriz no sirve para nada", "Que el plazo es el único criterio válido", "La sensibilidad a los pesos debe declararse."),
        ("ab", "{F} ¿Cuál afirmación describe mejor la Propuesta 1?", "Combina restauración, mitigación como sumidero y adaptación por la retención de agua", "Es solo una obra de adaptación", "Reforestar con nativas restaura el ecosistema, aumenta un sumidero y retiene agua."),
        ("abc", "{F} ¿Qué criterio adicional convendría agregar a la matriz?", "El mantenimiento a largo plazo y el riesgo de nuevos incendios", "El color de las obras", "El nombre de la empresa", "Un criterio que afecte la permanencia de los beneficios mejora la decisión."),
        ("abc", "¿Quién debería decidir los pesos de los criterios para una cuenca?", "La comunidad y las autoridades, con información de especialistas", "Una sola persona sin consultar", "El resultado de una calculadora", "Los pesos reflejan valores de la comunidad afectada."),
        ("=", "{F} ¿Cuántos puntos más obtiene la Propuesta 1 que la 3 en el criterio de beneficios, considerando el peso?", "3*3-3*2", "Se calcula peso por puntaje de P1 y de P3 en beneficios y se restan.", " puntos"),
    ],
    ctx=("abc", "Contexto: una asamblea de ejemplo debe elegir una propuesta con la matriz y alguien dice que, como P2 tiene el mayor puntaje en reducción, hay que elegirla. ¿Qué respuesta es la más razonable?", "Mirar el total con todos los criterios, probar cambios de pesos y declarar qué deja pendiente cada propuesta", "Elegir P2 sin mirar nada más", "Descartar la matriz y votar sin criterios", "Una decisión sólida considera todos los criterios y su sensibilidad."),
    sc=[
        ("En Química: ¿qué es la sensibilidad de una matriz a los pesos?", "Cuánto cambia el resultado al variar un peso", "Si el orden cambia con pocos cambios de peso, el resultado es menos firme."),
        ("ab", "El peso de un criterio expresa:", "Su importancia", "Su costo", "Cada criterio recibe un peso según su importancia."),
        ("ab", "Una propuesta de reforestación nativa puede ser a la vez:", "Restauración y mitigación", "Solo adaptación", "Recupera el ecosistema y aumenta un sumidero."),
    ],
    op=("Con la matriz de la ficha {F}: (1) calcula el total de las tres propuestas; (2) cambia el peso de un criterio a tu elección y recalcula el orden; (3) escribe una recomendación en tres oraciones con una limitación.",
        "(1) P1 = 22; P2 = 17; P3 = 15. (2) Con peso 4 en plazo: P1 = 25; P2 = 26; P3 = 21; el orden entre P1 y P2 cambia. (3) Recomiendo P1 por su total y sus beneficios para el ecosistema. Sin embargo, si el plazo fuera prioritario, P2 la supera. Falta incluir el mantenimiento a largo plazo.",
        ["tres totales correctos", "recalculo con un peso distinto", "recomendación con razones", "limitación"],
        ["tres respuestas numeradas"],
        ["sumar sin multiplicar por el peso", "no recalcular al cambiar el peso", "no declarar limitaciones"],
        "Pregunta: «¿qué criterio agregarías para decidir mejor?»."),
    reinforce="Rehace la matriz con un quinto criterio de tu elección y recalcula los totales.",
    extend="Explica por qué ninguna de las tres propuestas reemplaza completamente a las otras en una cuenca afectada.",
)
