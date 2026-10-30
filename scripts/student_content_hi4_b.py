"""Cuaderno del estudiante, 4.º básico Historia, Geografía y Ciencias Sociales: OA 10 (paisajes regionales y americanos) y OA 11 (organización política de Chile)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA10, OA11 = "HI04 OA 10", "HI04 OA 11"


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


# ================================================================ OA 10
register(
    OA10, 1,
    materials="Este cuaderno y un lápiz. Si puedes, un mapa de América o de Chile (no es obligatorio: los datos están escritos en los ejercicios).",
    use="Aprenderé a ubicar un paisaje en América y en Chile con puntos cardinales y elementos cercanos. Sirve para comparar paisajes sin confundir dónde están.",
    prior=["Conozco los puntos cardinales.", "Sé que Chile es un país de América del Sur."],
    explain=[
        "Un paisaje es lo que se ve en un lugar. Tiene elementos naturales, como montañas, ríos, desiertos y bosques, y elementos hechos por las personas, como casas, caminos y cultivos. América es un continente muy largo de norte a sur: América del Norte, América Central y América del Sur. Chile está en América del Sur, en el suroeste, entre la cordillera de los Andes y el océano Pacífico.",
        "Para ubicar un paisaje decimos el punto cardinal (norte, sur, este u oeste), el país y un elemento cercano, como una cordillera o un océano. El desierto de Atacama está en el norte de Chile y es muy seco. La Patagonia está en el sur de Chile y de Argentina, con viento fuerte y frío. La selva del Amazonas está en el norte de América del Sur, en gran parte en Brasil, y allí llueve mucho.",
        "Primero ubicamos y después comparamos. Dos paisajes lejanos pueden parecerse, y dos paisajes cercanos pueden ser muy distintos. Por eso, antes de explicar un paisaje, decimos dónde está y qué se ve en él.",
    ],
    vocab=[("paisaje", "lo que se ve en un lugar, hecho de elementos naturales y de elementos hechos por las personas"), ("punto cardinal", "norte, sur, este u oeste"), ("cordillera", "cadena larga de montañas"), ("desierto", "lugar donde llueve muy poco"), ("selva", "bosque muy grande y lluvioso de clima caluroso")],
    worked=[
        W("Ubicar con tres datos", "Ubica el desierto de Atacama usando punto cardinal, país y un elemento cercano.",
          ["Punto cardinal: está en el norte.", "País: Chile.", "Elemento cercano: la cordillera de los Andes, al este, y el océano Pacífico, al oeste."], "En el norte de Chile, entre la cordillera de los Andes y el océano Pacífico"),
        W("Separar lo natural de lo hecho por personas", "En una descripción aparecen: un río, una casa, un cerro, un camino. ¿Cuáles son elementos naturales?",
          ["Pregunto de cada uno si existía sin las personas.", "El río y el cerro existían solos.", "La casa y el camino los construyeron personas."], "El río y el cerro"),
    ],
    mistakes=[
        M("Ubicar un paisaje diciendo solo «está lejos» o «allá».", "No sirve para encontrarlo en un mapa.", "Usa un punto cardinal, el país y un elemento cercano."),
        M("Pensar que todos los paisajes de Chile se parecen entre sí.", "Chile es muy largo de norte a sur.", "El norte, el centro y el sur de Chile tienen paisajes distintos."),
    ],
    tiers=tiers(
        [ex("Una montaña y un río, ¿son elementos naturales o hechos por las personas?", "Elementos naturales", "Existen sin que las personas los construyan."),
         ex("Un camino y una casa, ¿son elementos naturales o hechos por las personas?", "Hechos por las personas", "Las personas los construyen."),
         ex("Chile, ¿está en América del Sur o en América del Norte?", "En América del Sur", "Así lo ubica la explicación de la clase.")],
        [ex("Con tus palabras, ¿qué es un paisaje?", "Lo que se ve en un lugar, con elementos naturales y hechos por las personas", "Combina lo natural y lo construido."),
         ex("¿Para qué sirve nombrar un elemento cercano, como la cordillera, al ubicar un paisaje?", "Para poder encontrarlo en el mapa", "Da una referencia concreta."),
         ex("Escribe los cuatro puntos cardinales.", "Norte, sur, este y oeste", "Son los que se usan para ubicar.")],
        [ex("En un mapa de Chile con el norte hacia arriba, ¿dónde dibujas el desierto de Atacama: en la parte de arriba o de abajo?", "En la parte de arriba", "Atacama está en el norte de Chile."),
         ex("Ordena de norte a sur estos paisajes de Chile: Patagonia, desierto de Atacama, valle central.", "Desierto de Atacama, valle central, Patagonia", "Atacama está en el norte, el valle en el centro y la Patagonia en el sur."),
         ex("La cordillera de los Andes separa a Chile de Argentina. Si estás en Chile y miras hacia la cordillera, ¿Argentina queda al este o al oeste?", "Al este", "El océano Pacífico está al oeste de Chile, así que Argentina queda al otro lado, al este.")],
        [ex("Lía dice: «La selva del Amazonas está en el sur de Chile». ¿Qué error tiene?", "La selva del Amazonas está en el norte de América del Sur, en gran parte en Brasil, no en Chile", "Ubicó mal el paisaje."),
         ex("Tomás afirma: «Dos paisajes lejanos nunca se parecen». ¿Es verdadero o falso? Explica.", "Falso; paisajes lejanos pueden parecerse", "La clase dice que lo lejano puede parecerse y lo cercano puede ser distinto.")],
        [ex("Tarjeta: «Está en el sur de Chile y de Argentina. Hay viento fuerte y frío». ¿Qué paisaje de la clase describe?", "La Patagonia", "Es el paisaje del sur con viento fuerte y frío."),
         ex("Ordena los pasos para estudiar un paisaje: A) comparar con otro, B) ubicarlo, C) describir lo que se ve.", "B, C, A", "Primero se ubica, luego se describe y después se compara.")],
    ),
    context=[ex("Una tarjeta de viaje dice: «Árboles muy altos, mucha lluvia y un río muy ancho, en el norte de América del Sur». ¿Es la selva del Amazonas o el desierto de Atacama? Explica con un dato.", "La selva del Amazonas, porque allí llueve mucho", "El desierto de Atacama es muy seco.")],
    selfcheck=[ex("Menciona dos elementos naturales de un paisaje.", "Por ejemplo: montañas y ríos", "Son elementos naturales."), ex("¿Qué tres datos sirven para ubicar un paisaje?", "Punto cardinal, país y un elemento cercano", "Son los de la clase."), ex("¿En qué parte de Chile está el desierto de Atacama?", "En el norte", "Así se ubicó en la clase.")],
    open_task=task("Escribe una ficha del paisaje que ves cerca de tu casa o de tu escuela (si no puedes salir, usa el que ves desde una ventana o el que recuerdas). Incluye: nombre del lugar, dónde está (punto cardinal y un elemento cercano), dos elementos naturales y dos hechos por las personas.", "Lugar: plaza de mi barrio. Está al oeste de la escuela, cerca de un cerro. Naturales: árboles y cerro. Hechos por personas: bancas y un camino.", ["incluye punto cardinal y un elemento cercano", "separa elementos naturales de los hechos por las personas", "usa al menos cuatro elementos"], ["ficha escrita", "lista de elementos clasificados"], ["poner una casa como elemento natural", "ubicar el lugar solo con «cerca» o «allá»"], "Muestra tu ficha a una persona y pídele que diga cuáles elementos son naturales; compara con tu lista."),
    reinforce="Nombra tres elementos naturales y tres hechos por personas que veas desde donde estás.",
    extend="Escribe por qué el norte, el centro y el sur de Chile tienen paisajes distintos aunque estén en el mismo país.",
)

register(
    OA10, 2,
    materials="Este cuaderno y un lápiz. Las fuentes que se estudian están escritas en los ejercicios.",
    use="Aprenderé a leer una imagen, un mapa o un relato como fuente: qué muestra, quién lo hizo y qué no permite saber. Sirve para no sacar conclusiones apresuradas de un paisaje.",
    prior=["Sé ubicar un paisaje con punto cardinal, país y elemento cercano.", "Distingo elementos naturales de los hechos por las personas."],
    explain=[
        "Una fuente es algo que da información sobre un tema: una fotografía, un mapa, un dibujo, un texto o el relato de una persona. Para estudiar un paisaje podemos usar varias fuentes. El mapa dice dónde está y cómo es el relieve. La fotografía muestra cómo se ve en un momento. El relato cuenta lo que vivió alguien.",
        "Toda fuente tiene una procedencia: quién la hizo, cuándo y para qué. Un folleto de turismo se hace para atraer visitantes, así que muestra lo más atractivo. Un informe de una escuela se hace para enseñar. Preguntar por la procedencia ayuda a saber cuánto confiar en una fuente y qué le falta.",
        "Al leer una fuente separamos lo que se observa de lo que se interpreta. Observar es decir lo que realmente se ve: «hay casas de barro y un cerro». Interpretar es agregar una idea: «la gente vive así desde siempre». Una fotografía no permite afirmar eso, porque muestra solo un momento y un lugar pequeño.",
    ],
    vocab=[("fuente", "algo que entrega información, como una foto, un mapa o un relato"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("observar", "decir lo que realmente se ve"), ("interpretar", "agregar una idea sobre lo que se ve"), ("relato", "texto en que una persona cuenta lo que vivió")],
    worked=[
        W("Observar o interpretar", "Fuente: foto de un valle con viñas y un canal. Frase A: «Hay viñas y un canal de agua». Frase B: «Los viñedos siempre han estado ahí». ¿Cuál es observación?",
          ["Reviso qué se puede ver en la foto.", "Las viñas y el canal se ven.", "«Siempre» habla del pasado, que una foto no muestra."], "La frase A es observación; la B es interpretación"),
        W("Preguntar por la procedencia", "Un folleto de turismo muestra solo playas soleadas de una isla. ¿Qué pregunta conviene hacer?",
          ["Pregunto quién lo hizo y para qué.", "Se hizo para atraer visitantes.", "Quizá no muestra los días de lluvia ni los problemas del lugar."], "Para qué se hizo y qué no muestra"),
    ],
    mistakes=[
        M("Creer que una fotografía muestra todo el paisaje de un lugar.", "Una foto muestra un momento y una parte pequeña.", "Pregunta qué no se alcanza a ver y busca otra fuente."),
        M("Confiar en una fuente sin preguntar quién la hizo.", "Cada fuente se hace con un propósito.", "Revisa la procedencia: quién, cuándo y para qué."),
    ],
    tiers=tiers(
        [ex("Un mapa, una foto y un relato de viaje, ¿son fuentes?", "Sí, son fuentes", "Todas entregan información sobre un lugar."),
         ex("La procedencia de una fuente, ¿dice quién la hizo o dice cuántas páginas tiene?", "Dice quién la hizo", "La procedencia es quién, cuándo y para qué."),
         ex("«Hay un cerro y tres casas», ¿es una observación o una interpretación?", "Una observación", "Describe lo que se ve.")],
        [ex("Con tus palabras, ¿qué diferencia hay entre observar e interpretar?", "Observar es decir lo que se ve; interpretar es agregar una idea", "La interpretación va más allá de lo que se ve."),
         ex("¿Por qué un folleto de turismo puede mostrar solo lo más bonito?", "Porque se hizo para atraer visitantes", "Su propósito es atraer."),
         ex("¿Qué dos datos de procedencia, además de quién la hizo, hay que preguntar?", "Cuándo y para qué", "Son las otras dos partes de la procedencia.")],
        [ex("Fuente: una foto tomada en enero en el desierto muestra arena, cerros y una carretera. Frase: «Nunca llueve en ese desierto». ¿Se puede afirmar con esa foto? Responde sí o no.", "No", "Una foto de un día no muestra todo el año."),
         ex("¿Qué fuente sirve mejor para saber dónde queda la selva del Amazonas: un mapa o un relato de una persona que no dice la ubicación?", "El mapa", "El mapa muestra ubicaciones."),
         ex("Un folleto con fotos de playas dice «¡Ven a la isla más linda!». Escribe qué pregunta de procedencia harías y qué crees que el folleto no muestra.", "Quién lo hizo y para qué; por ejemplo, no muestra los días de lluvia ni los problemas del lugar", "Un folleto se hace para atraer visitantes, así que muestra lo más atractivo.")],
        [ex("Ema mira una foto de nieve en la Patagonia y dice: «En la Patagonia siempre hay nieve en todas partes». ¿Qué error tiene?", "Generalizó con una sola foto, que muestra un lugar y un momento", "Una foto no muestra toda la Patagonia ni todo el año."),
         ex("Una persona escribe un relato: «Qué hermosa selva, nadie sufre allí por la lluvia». ¿Qué pregunta de procedencia conviene hacerle?", "Quién lo escribió, cuándo y qué vivió", "Un relato es una experiencia personal y puede no mostrar todo.")],
        [ex("Tienes una foto del desierto de Atacama sin título ni fecha. Escribe una pregunta de procedencia y una de contenido.", "Por ejemplo: ¿Quién la tomó y cuándo? ¿Qué se ve en el primer plano?", "Una pregunta es sobre su origen y la otra sobre lo que muestra."),
         ex("Ordena los pasos al usar una fuente: A) decir qué se interpreta, B) leer quién la hizo, C) decir qué se observa.", "B, C, A", "Primero la procedencia, luego lo observado y al final lo interpretado.")],
    ),
    context=[ex("Un folleto muestra una playa del Caribe con sol y palmeras. Una niña concluye: «Allí nunca hay tormentas». ¿Qué le dices usando la idea de procedencia?", "Que el folleto se hizo para atraer visitantes y no muestra todo", "Su propósito era mostrar lo atractivo.")],
    selfcheck=[ex("¿Qué es una fuente?", "Algo que entrega información, como una foto o un mapa", "Es la definición de la clase."), ex("¿Qué tres datos forman la procedencia?", "Quién la hizo, cuándo y para qué", "Así se definió."), ex("¿Una foto muestra todo un paisaje?", "No", "Muestra un lugar y un momento.")],
    open_task=task("Lee esta fuente: «Relato de un viajero: En el Altiplano vi llamas, casas de adobe y un cielo muy limpio; en la noche hacía mucho frío». Escribe dos observaciones que el relato permite afirmar, una interpretación que el relato no permite afirmar y una pregunta de procedencia.", "Observaciones: hay llamas; las noches son frías. No permite: que todos viven así. Pregunta: ¿cuándo viajó?", ["dos observaciones tomadas del relato", "una interpretación que no se puede afirmar", "una pregunta de procedencia"], ["cuatro frases escritas"], ["poner como observación algo que el relato no dice", "no escribir la pregunta de procedencia"], "Pide a una persona que subraye en el relato cada observación que escribiste."),
    reinforce="Mira una foto de tu casa o barrio y escribe una observación y una interpretación.",
    extend="Escribe qué otra fuente usarías para saber cómo es el clima de un lugar durante todo el año.",
)

register(
    OA10, 3,
    materials="Este cuaderno y un lápiz. Las fichas de los paisajes están escritas en los ejercicios.",
    use="Aprenderé a describir un paisaje con evidencia y a distinguir adaptación y transformación. Sirve para explicar cómo las personas viven en su ambiente natural.",
    prior=["Sé ubicar paisajes de Chile y de América.", "Sé separar lo que se observa de lo que se interpreta."],
    explain=[
        "Para caracterizar un paisaje describimos varias dimensiones: el clima, el relieve, el agua, la vegetación y lo que hacen las personas. En el desierto de Atacama llueve casi nada. En la selva del Amazonas llueve mucho y hace calor. En el valle central de Chile los veranos son secos y las lluvias llegan en invierno. Cada dato debe apoyarse en una fuente.",
        "Las personas se relacionan con el ambiente de dos maneras. La adaptación es cambiar la forma de vivir para ajustarse al lugar: usar ropa abrigadora en la Patagonia, construir casas de adobe de muros gruesos en el norte desértico, o levantar casas sobre pilotes cerca de los ríos de la Amazonía. La transformación es cambiar el ambiente: hacer canales de riego, construir caminos o cortar un bosque para sembrar.",
        "Una adaptación no se explica solo por el clima. También influyen el relieve, el agua, los materiales que hay y las costumbres. Y una transformación puede traer beneficios y problemas: un canal de riego permite cultivar, pero usa agua que ya no llega a otros lugares.",
    ],
    vocab=[("adaptación", "cambiar la forma de vivir para ajustarse al ambiente natural"), ("transformación", "cambiar el ambiente natural para algún fin"), ("clima", "calor, frío y lluvia de un lugar durante el año"), ("riego", "llevar agua a los cultivos"), ("pilotes", "postes que sostienen una casa sobre el suelo")],
    worked=[
        W("Adaptación o transformación", "En el valle central se construyen canales para llevar agua a los cultivos. ¿Es adaptación o transformación?",
          ["Pregunto si cambian el ambiente o su forma de vivir.", "Los canales cambian el paisaje: llevan agua donde antes no había.", "Cambiar el ambiente es transformación."], "Transformación"),
        W("Describir con evidencia", "Ficha del Amazonas: «mucha lluvia, calor todo el año, ríos anchos, casas sobre pilotes». ¿Qué dato explica la adaptación de las casas?",
          ["Busco un dato del ambiente relacionado con las casas.", "Los ríos anchos pueden crecer con la lluvia.", "Las casas sobre pilotes quedan sobre el agua."], "Los ríos anchos y la mucha lluvia"),
    ],
    mistakes=[
        M("Decir que toda adaptación se explica solo por el clima.", "También influyen el relieve, el agua y los materiales.", "Busca más de un dato del ambiente."),
        M("Creer que una transformación es siempre mala o siempre buena.", "Casi siempre tiene beneficios y problemas.", "Nombra qué ganan y qué pierden las personas y el ambiente."),
    ],
    tiers=tiers(
        [ex("Usar ropa abrigadora en un lugar frío, ¿es adaptación o transformación?", "Adaptación", "Cambia la forma de vivir, no el ambiente."),
         ex("Construir un canal de riego, ¿es adaptación o transformación?", "Transformación", "Cambia el ambiente al llevar agua."),
         ex("Una casa de adobe con muros gruesos en el desierto, ¿es adaptación o transformación?", "Adaptación", "Se ajusta al clima del lugar sin cambiarlo.")],
        [ex("Nombra tres dimensiones para describir un paisaje.", "Por ejemplo: clima, relieve y agua", "La clase menciona clima, relieve, agua, vegetación y lo que hacen las personas."),
         ex("¿Por qué una casa sobre pilotes sirve cerca de un río que crece con la lluvia?", "Porque queda sobre el agua", "Los pilotes la elevan del suelo."),
         ex("Con tus palabras, ¿qué es una transformación del ambiente?", "Cambiar el ambiente natural para algún fin", "Las personas modifican el lugar.")],
        [ex("Ficha: «llueve casi nada, hay arena y cerros». De estas dimensiones, ¿cuál aparece en la ficha: clima, vegetación o animales?", "Clima", "«Llueve casi nada» habla del clima; la ficha no dice nada de plantas ni de animales."),
         ex("Un pueblo corta un bosque para sembrar. ¿Es adaptación o transformación?", "Transformación", "Cambia el ambiente natural."),
         ex("Ficha de la Patagonia: viento fuerte y frío. ¿Qué adaptación coincide: casas con paredes resistentes o ropa muy ligera?", "Casas con paredes resistentes", "Responde al viento y al frío; la ropa ligera no.")],
        [ex("Bruno dice: «Las casas de adobe se hacen solo por el clima». ¿Qué otro dato del ambiente puede influir?", "Los materiales que hay en el lugar, como la tierra", "El adobe se hace con tierra del lugar."),
         ex("Sara dice: «Un canal de riego solo trae cosas buenas». ¿Qué problema puede tener?", "Puede usar agua que ya no llega a otros lugares", "Toda transformación tiene ventajas y problemas.")],
        [ex("Ficha del valle central: «veranos secos, lluvias en invierno, terreno plano entre cordilleras». Escribe una transformación que ayude a cultivar en verano y por qué.", "Canales de riego, porque llevan agua cuando no llueve", "El riego resuelve la falta de lluvia en verano."),
         ex("Une cada dato con la dimensión: 1) llueve mucho, 2) hay cerros y valles, 3) hay ríos anchos. Dimensiones: relieve, agua, clima.", "1 clima, 2 relieve, 3 agua", "La lluvia es clima, cerros y valles son relieve y los ríos son agua.")],
    ),
    context=[ex("En la Amazonía una familia construye su casa sobre pilotes y usa canoa. En el valle central se hace un canal para el riego. ¿Cuál de las dos acciones es adaptación y cuál transformación?", "La casa sobre pilotes es adaptación; el canal de riego es transformación", "La casa se ajusta al río; el canal cambia el ambiente.")],
    selfcheck=[ex("En Historia: ¿Qué es una adaptación?", "Cambiar la forma de vivir para ajustarse al ambiente", "Es la definición de la clase."), ex("Menciona una transformación del ambiente.", "Por ejemplo: hacer un canal o un camino", "Las personas cambian el lugar."), ex("¿Una adaptación depende solo del clima?", "No", "También influyen relieve, agua y materiales.")],
    open_task=task("Elige un paisaje: A) desierto de Atacama, B) selva del Amazonas o C) valle central. Escribe una ficha con dos dimensiones (por ejemplo clima y agua), una adaptación y una transformación de las personas, y un problema que puede traer la transformación.", "Elegí A. Clima: llueve casi nada. Agua: muy poca. Adaptación: casas de adobe. Transformación: caminos. Problema: el polvo y el ruido.", ["incluye dos dimensiones del paisaje", "distingue adaptación de transformación", "nombra un problema de la transformación"], ["ficha escrita"], ["llamar adaptación a un cambio del ambiente", "explicar todo solo por el clima"], "Pide a una persona que lea tu ficha y te diga cuál es la adaptación y cuál la transformación."),
    reinforce="Escribe una adaptación y una transformación que veas en tu comuna.",
    extend="Explica con una frase por qué una misma transformación puede ser buena para unas personas y problemática para otras.",
)

register(
    OA10, 4,
    materials="Este cuaderno y un lápiz. Los cuadros para comparar están escritos en los ejercicios.",
    use="Aprenderé a comparar un paisaje de mi región con uno de América, mirando semejanzas, diferencias y distintas formas de adaptación y transformación. Sirve para sacar una conclusión justa.",
    prior=["Sé describir un paisaje con clima, relieve y agua.", "Distingo adaptación de transformación."],
    explain=[
        "Comparar es mirar dos cosas con las mismas preguntas. Si digo que en el paisaje A hay lluvia, debo decir también cuánta llueve en el B. Usamos un cuadro con las mismas filas: clima, relieve, agua, adaptación y transformación. Luego marcamos qué se parece y qué es distinto.",
        "Dos paisajes pueden parecerse en un rasgo por razones distintas. El Altiplano y la Patagonia son fríos, pero el Altiplano está muy alto sobre el nivel del mar y la Patagonia está muy al sur. El valle central de Chile y la Pampa de Argentina son terrenos planos con cultivos, pero el valle está entre dos cordilleras y la Pampa es una llanura muy extensa.",
        "También comparamos cómo cambian las cosas. Una casa de adobe de hace años y una casa nueva de cemento muestran un cambio. Que se siga usando ropa abrigadora en el sur muestra una continuidad. Al final escribimos una conclusión que use los datos del cuadro, sin exagerar: «en estos dos casos» es más justo que «en todos los paisajes».",
    ],
    vocab=[("comparar", "mirar dos cosas con las mismas preguntas para ver semejanzas y diferencias"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas son distintas"), ("continuidad", "algo que sigue igual a lo largo del tiempo"), ("conclusión", "idea final que se apoya en los datos")],
    worked=[
        W("Semejanza con causa distinta", "El Altiplano y la Patagonia son fríos. ¿Se parecen por la misma razón?",
          ["Reviso la causa del frío en cada uno.", "El Altiplano es frío por estar muy alto.", "La Patagonia es fría por estar muy al sur."], "No; se parecen en el frío pero por razones distintas"),
        W("Conclusión justa", "Cuadro: dos paisajes tienen canales de riego. ¿Es justo concluir «todos los paisajes de América tienen canales»?",
          ["Cuento los casos: solo dos.", "Dos casos no representan todos.", "Conviene decir «en estos dos paisajes»."], "No; hay que limitarse a los casos comparados"),
    ],
    mistakes=[
        M("Comparar un paisaje por su clima y el otro por sus animales.", "No se usan las mismas preguntas.", "Compara las mismas dimensiones en ambos."),
        M("Concluir algo sobre «toda América» con dos ejemplos.", "Dos ejemplos no representan todo.", "Limita la conclusión a los casos comparados."),
    ],
    tiers=tiers(
        [ex("Para comparar dos paisajes, ¿usas las mismas preguntas en ambos o preguntas distintas?", "Las mismas preguntas", "Así se pueden ver semejanzas y diferencias."),
         ex("Que dos paisajes sean fríos, ¿es una semejanza o una diferencia?", "Una semejanza", "Ambos tienen el mismo rasgo."),
         ex("Que en un paisaje llueva mucho y en otro casi nada, ¿es semejanza o diferencia?", "Una diferencia", "Los dos casos no coinciden.")],
        [ex("Con tus palabras, ¿qué es una conclusión justa?", "Una idea final que se apoya en los datos y no exagera", "Se limita a los casos comparados."),
         ex("¿Qué es una continuidad? Da un ejemplo.", "Algo que sigue igual, como usar ropa abrigadora en el sur", "Permanece a lo largo del tiempo."),
         ex("¿Por qué el Altiplano es frío, según la clase?", "Porque está muy alto sobre el nivel del mar", "La altura enfría el aire.")],
        [ex("Cuadro: Valle central: plano, entre cordilleras, riego. Pampa: plano, muy extensa, cultivos. Escribe una semejanza entre los dos.", "Los dos son terrenos planos", "Es el rasgo que coincide."),
         ex("Cuadro: Altiplano: frío por la altura. Patagonia: frío por estar muy al sur. ¿Los dos son fríos por la misma causa? Responde sí o no.", "No", "Cada uno tiene una causa distinta."),
         ex("Una casa de adobe de hace años y una casa nueva de cemento en el mismo pueblo, ¿muestran un cambio o una continuidad?", "Un cambio", "Cambió el material de construcción.")],
        [ex("Ana dice: «Como el Altiplano y la Patagonia son fríos, son iguales». ¿Qué error hay?", "Se parecen en el frío pero tienen causas y rasgos distintos", "Una semejanza no hace iguales a dos paisajes."),
         ex("Beto compara el clima de un paisaje con las casas del otro. ¿Qué debe cambiar?", "Comparar las mismas dimensiones en los dos", "Para comparar se usan las mismas preguntas.")],
        [ex("Se compararon dos paisajes con canales de riego. Escribe una conclusión justa que empiece con «En estos dos paisajes...».", "Por ejemplo: En estos dos paisajes las personas usan canales de riego para cultivar", "Se limita a los casos comparados."),
         ex("Un canal de riego en el valle central da agua a los cultivos, pero deja menos agua en el río. Escribe quién gana y quién puede perder.", "Ganan los cultivos y las personas que los trabajan; puede perder el río o quien lo usa más abajo", "Una transformación tiene ventajas y problemas.")],
    ),
    context=[ex("Un cuaderno de clase tiene este cuadro. Paisaje X: muchas lluvias, casas sobre pilotes. Paisaje Y: casi sin lluvias, casas de adobe. ¿Qué diferencia de clima explica los dos tipos de casas?", "En X llueve mucho y en Y casi nada", "El clima es la diferencia entre los dos.")],
    selfcheck=[ex("¿Qué se hace al comparar dos paisajes?", "Mirar las mismas preguntas en ambos para ver semejanzas y diferencias", "Es la idea central de la clase."), ex("¿Por qué conviene escribir «en estos dos casos»?", "Para no exagerar la conclusión", "Dos casos no son todos."), ex("¿Qué es una continuidad?", "Algo que sigue igual a lo largo del tiempo", "Es lo contrario de un cambio.")],
    open_task=task("Compara dos paisajes con un cuadro de cuatro filas (clima, relieve, adaptación y transformación). Usa el paisaje que ves cerca de ti y uno de estos: A) desierto de Atacama, B) Amazonía, C) Pampa argentina. Escribe una semejanza, una diferencia y una conclusión que empiece con «En estos dos paisajes...».", "Mi barrio y la Pampa son planos. Diferencia: en mi barrio hay cerros cerca. En estos dos paisajes las personas construyen caminos.", ["usa las mismas filas para ambos paisajes", "escribe una semejanza y una diferencia", "la conclusión se limita a los dos paisajes"], ["cuadro de cuatro filas", "tres frases"], ["comparar dimensiones distintas", "concluir sobre toda América"], "Pide a una persona que revise que tu cuadro tiene los mismos datos en ambos paisajes."),
    reinforce="Compara dos plazas o parques que conozcas con las mismas tres preguntas.",
    extend="Explica por qué un rasgo parecido (como el frío) puede tener causas distintas en dos paisajes.",
)

# ================================================================ OA 11
register(
    OA11, 1,
    materials="Este cuaderno y un lápiz. Las tarjetas de cargos están escritas en los ejercicios.",
    use="Aprenderé quiénes son el Presidente, los ministros, los senadores, los diputados y los alcaldes, y qué hace cada uno. Sirve para entender cómo se organiza la política de Chile.",
    prior=["Sé que en una democracia las personas participan en las decisiones.", "Sé qué es una comuna."],
    explain=[
        "Chile es una república democrática. Eso significa que las autoridades no heredan el cargo: las personas con derecho a voto eligen a algunas de ellas. Las autoridades trabajan en instituciones, que son organizaciones con funciones definidas, como el Congreso o la municipalidad.",
        "El Presidente de la República gobierna el país: dirige la administración del Estado. Los ministros lo ayudan: cada uno dirige un ministerio, por ejemplo el de Educación o el de Salud. El Presidente los nombra. Los senadores y los diputados trabajan en el Congreso Nacional, que está en Valparaíso, y discuten y aprueban las leyes. El alcalde dirige la municipalidad de su comuna.",
        "No todos llegan al cargo igual. El Presidente, los senadores, los diputados y los alcaldes son elegidos por votación de las personas con derecho a voto. Los ministros no se eligen en votación: los nombra el Presidente. Esta diferencia ayuda a saber quién responde por qué decisión.",
    ],
    vocab=[("democracia", "forma de gobierno en que las personas participan en las decisiones"), ("institución", "organización con funciones definidas, como el Congreso"), ("ministro", "persona nombrada por el Presidente para dirigir un ministerio"), ("ley", "norma que deben cumplir todas las personas"), ("alcalde", "autoridad elegida que dirige la municipalidad de una comuna")],
    worked=[
        W("Quién hace las leyes", "Una persona dice: «Soy diputado y voto una ley». ¿En qué institución trabaja?",
          ["Recuerdo que los diputados y los senadores aprueban leyes.", "Lo hacen en el Congreso Nacional.", "El Congreso está en Valparaíso."], "En el Congreso Nacional"),
        W("Elegido o nombrado", "¿Cómo llega a su cargo un ministro de Educación?",
          ["Pregunto si lo eligen votando o si alguien lo designa.", "Lo designa el Presidente.", "No se elige en votación."], "Lo nombra el Presidente"),
    ],
    mistakes=[
        M("Creer que los ministros se eligen por votación.", "Se mezcla a los ministros con las autoridades elegidas.", "Los ministros los nombra el Presidente."),
        M("Pensar que el alcalde gobierna todo el país.", "Se confunde la comuna con el país.", "El alcalde dirige la municipalidad de su comuna; el Presidente gobierna el país."),
    ],
    tiers=tiers(
        [ex("¿Quién dirige la municipalidad de una comuna: el alcalde o el Presidente?", "El alcalde", "La municipalidad es del alcalde."),
         ex("¿Los diputados y senadores trabajan en el Congreso Nacional o en un ministerio?", "En el Congreso Nacional", "Allí discuten y aprueban leyes."),
         ex("¿Quién nombra a los ministros: el Presidente o los alcaldes?", "El Presidente", "Los ministros no se eligen por votación.")],
        [ex("Con tus palabras, ¿qué hace el Presidente de la República?", "Gobierna el país y dirige la administración del Estado", "Es la autoridad que gobierna."),
         ex("¿Qué es una institución? Da un ejemplo.", "Una organización con funciones definidas, como el Congreso o la municipalidad", "Las autoridades trabajan en instituciones."),
         ex("¿Qué es una ley?", "Una norma que deben cumplir todas las personas", "Es lo que aprueban diputados y senadores.")],
        [ex("Tarjeta: «Dirijo el Ministerio de Salud. Me nombró el Presidente». ¿Esa persona es ministro o alcalde?", "Ministro", "Los ministros dirigen ministerios y los nombra el Presidente."),
         ex("Tarjeta: «Fui elegido por los vecinos de mi comuna y dirijo la municipalidad». ¿Quién es?", "El alcalde", "Es elegido en la comuna y dirige la municipalidad."),
         ex("Una ley se discute en el Congreso Nacional. ¿En qué ciudad está el Congreso?", "En Valparaíso", "Así lo dice la explicación de la clase.")],
        [ex("Tomás dice: «El ministro de Educación lo elegimos votando». ¿Qué le respondes?", "Que no se elige, sino que lo nombra el Presidente", "Los ministros son nombrados."),
         ex("Ana cree que el alcalde puede dirigir el país entero. ¿Qué autoridad gobierna el país?", "El Presidente de la República", "El alcalde dirige solo su comuna.")],
        [ex("¿Qué cargo actúa en un nivel más amplio: el alcalde, que dirige una comuna, o el Presidente, que gobierna el país?", "El Presidente", "Su alcance es todo el país; el del alcalde es una comuna."),
         ex("Escribe cuáles de estas autoridades se eligen en votación: Presidente, ministro, diputado, alcalde.", "Presidente, diputado y alcalde", "El ministro es nombrado por el Presidente.")],
    ),
    context=[ex("Los vecinos de una comuna quieren arreglar una plaza del barrio. ¿A qué autoridad cercana conviene pedirle ayuda: al alcalde o a un senador? Explica.", "Al alcalde, porque dirige la municipalidad de la comuna", "La plaza es un asunto de la comuna.")],
    selfcheck=[ex("Nombra cinco cargos de la organización política de Chile.", "Presidente, ministros, senadores, diputados y alcaldes", "Son los de la clase."), ex("¿Quién nombra a los ministros?", "El Presidente", "No se eligen por votación."), ex("¿Dónde trabajan los senadores y diputados?", "En el Congreso Nacional", "Allí se aprueban las leyes.")],
    open_task=task("Haz una tarjeta para cada cargo: Presidente, ministro, senador, diputado y alcalde. En cada una escribe qué hace, en qué institución trabaja y cómo llega al cargo (elegido o nombrado).", "Alcalde: dirige la municipalidad. Institución: municipalidad. Llega por elección de los vecinos.", ["cinco tarjetas con cargo", "indica qué hace cada uno", "dice si es elegido o nombrado"], ["cinco tarjetas escritas"], ["decir que los ministros son elegidos", "confundir alcalde con Presidente"], "Pide a una persona que te pregunte por un cargo al azar y responde sin mirar las tarjetas."),
    reinforce="Pregunta en casa quién es hoy el alcalde de tu comuna y escribe su cargo.",
    extend="Explica con una frase por qué es importante que algunas autoridades sean elegidas por votación.",
)

register(
    OA11, 2,
    materials="Este cuaderno y un lápiz. Los textos breves están escritos en los ejercicios.",
    use="Aprenderé a revisar de dónde viene una información sobre un cargo político y si es confiable. Sirve para no confundirme con noticias, afiches o comentarios.",
    prior=["Conozco los cargos de Presidente, ministros, senadores, diputados y alcaldes.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Para saber quién hace qué en la política de Chile podemos usar fuentes: la Constitución, páginas oficiales del Congreso o de la municipalidad, noticias y afiches de campaña. Cada fuente se hizo para algo. Una página oficial informa sobre la institución. Un afiche de campaña quiere conseguir votos. Una noticia cuenta un hecho, pero puede incluir opiniones.",
        "Antes de creer una información hacemos tres preguntas: ¿quién la escribió?, ¿para qué la escribió? y ¿se puede comprobar en otra fuente? Si un afiche dice «el mejor alcalde de todos», es una opinión. Si una página de la municipalidad dice «el alcalde dirige la municipalidad», es un dato que cualquiera puede comprobar.",
        "También hay que distinguir un hecho de una opinión. Un hecho se puede comprobar: «El Congreso Nacional está en Valparaíso». Una opinión expresa lo que alguien piensa: «Los diputados trabajan poco». Una opinión puede tener razones, pero no se comprueba como un hecho.",
    ],
    vocab=[("Constitución", "ley más importante del país, que organiza las instituciones"), ("fuente oficial", "información que entrega una institución sobre sí misma"), ("afiche de campaña", "cartel de un candidato para pedir votos"), ("hecho", "algo que se puede comprobar"), ("opinión", "lo que una persona piensa o siente sobre algo")],
    worked=[
        W("Hecho u opinión", "Frase: «El mejor Presidente es el que más sonríe». ¿Es hecho u opinión?",
          ["Pregunto si se puede comprobar.", "«Mejor» y «sonríe más» dependen de lo que cada uno piensa.", "No se puede comprobar con un dato."], "Es una opinión"),
        W("Procedencia de un afiche", "Un afiche dice: «Vota por mí, soy la mejor candidata». ¿Para qué se hizo?",
          ["Reviso quién lo hizo: una candidata.", "Pide votos.", "Su propósito es conseguir apoyo."], "Para conseguir votos"),
    ],
    mistakes=[
        M("Creer que todo lo que aparece en un afiche de campaña es un dato comprobado.", "Un afiche busca votos y puede exagerar.", "Compruébalo en una fuente oficial."),
        M("Llamar «hecho» a una opinión que suena segura.", "Decirla con fuerza no la vuelve comprobable.", "Pregúntate si se puede comprobar con un dato."),
    ],
    tiers=tiers(
        [ex("«El Congreso Nacional está en Valparaíso», ¿es un hecho o una opinión?", "Un hecho", "Se puede comprobar."),
         ex("Un afiche de campaña, ¿se hizo para pedir votos o para dar una lección de matemática?", "Para pedir votos", "Es propaganda de un candidato."),
         ex("«Los diputados son muy flojos», ¿es un hecho o una opinión?", "Una opinión", "Expresa lo que alguien piensa y no se comprueba con un dato.")],
        [ex("Nombra las tres preguntas para revisar una información.", "Quién la escribió, para qué y si se puede comprobar en otra fuente", "Son las preguntas de la clase."),
         ex("¿Qué es una fuente oficial?", "Información que entrega una institución sobre sí misma", "Por ejemplo, la página del Congreso."),
         ex("¿Por qué un afiche de campaña puede exagerar?", "Porque busca conseguir votos", "Su propósito es convencer.")],
        [ex("Frase de una página de la municipalidad: «El alcalde dirige la municipalidad de la comuna». ¿Se puede comprobar en otra fuente? Responde sí o no.", "Sí", "Es un dato sobre la institución."),
         ex("Dos afiches: A) «Vota por mí: mejor, imposible», B) «Mi propuesta: construir una plaza». ¿Cuál contiene una propuesta que se puede comprobar si se cumple?", "B", "Construir una plaza se puede verificar; A solo es una opinión."),
         ex("Una noticia cuenta que el Senado aprobó una ley y agrega «Fue una decisión muy tonta». ¿Qué parte es opinión?", "«Fue una decisión muy tonta»", "Es lo que piensa quien escribe.")],
        [ex("Lola dice: «Si está en un afiche, es verdad». ¿Qué le respondes?", "Que un afiche busca votos y hay que comprobar el dato en una fuente oficial", "El propósito del afiche es convencer."),
         ex("Tomás cree que una opinión no puede tener razones. ¿Qué le dices?", "Que una opinión puede tener razones, pero no se comprueba como un hecho", "La clase distingue ambas cosas.")],
        [ex("Frases: 1) «El Presidente nombra a los ministros». 2) «Los ministros son los más trabajadores». 3) «El Congreso Nacional está en Valparaíso». Escribe los números de las que son hechos.", "1 y 3", "La 2 es una opinión."),
         ex("Un cartel no dice quién lo hizo ni cuándo. Escribe una pregunta de procedencia que harías.", "¿Quién lo hizo y para qué?", "Sin esos datos no se sabe si es confiable.")],
    ),
    context=[ex("Un vecino repite: «El alcalde es el que hace las leyes del país». Dos fuentes dicen que las leyes las aprueban diputados y senadores en el Congreso. ¿Qué concluyes sobre lo que dijo el vecino?", "Que está equivocado, porque las leyes las aprueban diputados y senadores", "Dos fuentes coinciden y lo contradicen.")],
    selfcheck=[ex("¿Qué es un hecho?", "Algo que se puede comprobar", "Se diferencia de una opinión."), ex("¿Para qué se hace un afiche de campaña?", "Para conseguir votos", "Su propósito es convencer."), ex("Menciona una pregunta para revisar una información.", "Por ejemplo: ¿quién la escribió?", "Es una de las tres de la clase.")],
    open_task=task("Lee estas tres frases: A) «El alcalde dirige la municipalidad.» B) «Nuestro alcalde es el más guapo.» C) «Vota por mí y todo será perfecto.» Escribe cuál es un hecho, cuáles son opiniones o promesas, y para cada una cómo la comprobarías o por qué no se puede comprobar.", "A es un hecho: se comprueba en la página de la municipalidad. B es una opinión: depende de gustos. C es una promesa.", ["clasifica las tres frases", "explica cómo comprobar el hecho", "explica por qué las otras no se comprueban"], ["tres clasificaciones con razón"], ["llamar hecho a una opinión", "no explicar cómo comprobar"], "Pide a una persona que diga si está de acuerdo con tu clasificación y por qué."),
    reinforce="Escribe un hecho y una opinión sobre tu comuna.",
    extend="Explica por qué dos fuentes que coinciden dan más seguridad que una sola.",
)

register(
    OA11, 3,
    materials="Este cuaderno y un lápiz. La tabla de cargos y los datos están escritos en los ejercicios.",
    use="Aprenderé a caracterizar cada cargo con tres evidencias: qué hace, dónde trabaja y cómo llega al cargo. Sirve para armar un cuadro claro de la organización política de Chile.",
    prior=["Sé quiénes son el Presidente, los ministros, los senadores, los diputados y los alcaldes.", "Distingo un hecho de una opinión."],
    explain=[
        "Podemos describir cada cargo con tres datos. El primero es la función: qué hace. El segundo es la institución: dónde trabaja. El tercero es la forma de llegar al cargo: elegido por votación o nombrado. El Presidente: gobierna el país, trabaja desde el Palacio de La Moneda, en Santiago, y es elegido por votación. Los ministros: dirigen ministerios y los nombra el Presidente.",
        "Los senadores y los diputados: discuten y aprueban leyes en el Congreso Nacional, en Valparaíso, y son elegidos por votación. El alcalde: dirige la municipalidad de la comuna y es elegido por los vecinos con derecho a voto. A su lado trabaja el concejo municipal, formado por concejales, que también se eligen.",
        "Ordenar los datos en un cuadro permite comparar. En un cuadro de tres columnas, cada fila es un cargo. Podemos ver que cuatro cargos se eligen por votación y uno, el de ministro, se nombra. También vemos que unos actúan en todo el país y otro, el alcalde, actúa en una comuna.",
    ],
    vocab=[("función", "lo que hace un cargo"), ("Palacio de La Moneda", "edificio de Santiago donde trabaja el Presidente"), ("municipalidad", "institución que gobierna una comuna"), ("concejal", "persona elegida que trabaja junto al alcalde en el concejo municipal"), ("cuadro", "tabla que ordena datos en filas y columnas")],
    worked=[
        W("Completar una fila del cuadro", "Cargo: diputado. ¿Qué datos van en función, institución y forma de llegar?",
          ["Función: discutir y aprobar leyes.", "Institución: Congreso Nacional.", "Llega por votación."], "Aprueba leyes; Congreso Nacional; elegido por votación"),
        W("Contar con un cuadro", "En el cuadro hay cinco cargos y solo uno se nombra. ¿Cuántos se eligen?",
          ["Total de cargos: 5.", "Los nombrados: 1.", "Los elegidos son 5 − 1 = 4."], "4 cargos se eligen por votación"),
    ],
    mistakes=[
        M("Poner al Presidente en la columna del Congreso Nacional.", "Se mezclan las instituciones.", "El Presidente trabaja desde La Moneda; el Congreso es de diputados y senadores."),
        M("Creer que el concejal es lo mismo que el alcalde.", "Se confunden los cargos de la municipalidad.", "El alcalde dirige; el concejo, formado por concejales, trabaja junto a él."),
    ],
    tiers=tiers(
        [ex("¿Dónde trabaja el Presidente: en el Palacio de La Moneda o en el Congreso Nacional?", "En el Palacio de La Moneda", "Está en Santiago."),
         ex("¿Los diputados trabajan en la municipalidad o en el Congreso Nacional?", "En el Congreso Nacional", "Allí se aprueban las leyes."),
         ex("El alcalde, ¿es elegido por votación o nombrado por el Presidente?", "Elegido por votación", "Lo eligen los vecinos con derecho a voto.")],
        [ex("¿Qué tres datos se usan para describir un cargo?", "Función, institución y forma de llegar al cargo", "Son los tres de la clase."),
         ex("¿Qué es un concejal?", "Una persona elegida que trabaja junto al alcalde en el concejo municipal", "Forma parte de la municipalidad."),
         ex("¿Para qué sirve ordenar los datos en un cuadro?", "Para compararlos con facilidad", "Cada cargo queda en una fila.")],
        [ex("Cuadro con 5 cargos: 4 se eligen por votación y 1 se nombra. ¿Cuál es el que se nombra?", "El ministro", "Los ministros los nombra el Presidente."),
         ex("En el cuadro, ¿qué columna llenarías con «Congreso Nacional»: función, institución o forma de llegar?", "Institución", "El Congreso es una institución."),
         ex("Fila: «Gobierna el país; trabaja en La Moneda; elegido por votación». ¿Qué cargo es?", "Presidente", "Son los datos del Presidente.")],
        [ex("Rosa dice: «El alcalde actúa en todo el país». Usa el cuadro para corregirla.", "El alcalde actúa en su comuna", "Dirige la municipalidad de una comuna."),
         ex("Beto puso al diputado con la función «dirige un ministerio». ¿Qué cargo hace eso?", "El ministro", "El diputado aprueba leyes.")],
        [ex("Un cuadro tiene 5 cargos. Si dos de ellos se nombraran en vez de elegirse, el resto sería elegido. ¿Cuántos serían elegidos?", "3", "5 − 2 = 3.", "5-2"),
         ex("Arma esta fila: cargo senador. Escribe su función, institución y cómo llega.", "Aprueba leyes; Congreso Nacional; elegido por votación", "Cada dato corresponde a una columna del cuadro.")],
    ),
    context=[ex("Una niña investiga y anota: «Cargo: ministra. Función: dirige el Ministerio de Educación. Llega: elegida por votación». ¿Qué dato está mal y cuál debería ser?", "Llega: debería decir nombrada por el Presidente", "Los ministros no se eligen.")],
    selfcheck=[ex("¿Dónde trabaja el Presidente?", "En el Palacio de La Moneda, en Santiago", "Es su sede."), ex("¿Cuántos cargos de la lista (Presidente, ministro, senador, diputado, alcalde) se nombran?", "Uno, el ministro", "Los demás se eligen."), ex("¿Con quién trabaja un concejal en la municipalidad?", "Con el alcalde", "El concejo municipal trabaja junto a él.")],
    open_task=task("Completa un cuadro de tres columnas (función, institución y forma de llegar) para los cinco cargos: Presidente, ministro, senador, diputado y alcalde. Debajo escribe cuántos se eligen y cuántos se nombran.", "Alcalde: dirige la municipalidad; municipalidad; elegido. Al final: 4 elegidos y 1 nombrado.", ["cinco filas completas", "tres datos por cargo", "cuenta correcta de elegidos y nombrados"], ["cuadro completo"], ["poner al ministro como elegido", "mezclar instituciones"], "Pide a una persona que verifique una fila usando la explicación de la clase."),
    reinforce="Dibuja un cuadro en blanco con las tres columnas y llénalo de memoria.",
    extend="Escribe una pregunta que le harías a un concejal para entender su trabajo.",
)

register(
    OA11, 4,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a comparar cómo se elige a cada autoridad y qué cambia según el nivel: país o comuna. Sirve para decidir a quién acudir y para explicar por qué votar importa.",
    prior=["Conozco las funciones, instituciones y forma de llegar de cada cargo.", "Sé usar un cuadro para comparar."],
    explain=[
        "Las autoridades actúan en distintos niveles. El Presidente, los senadores y los diputados toman decisiones que se aplican a todo el país, como las leyes. El alcalde toma decisiones para su comuna, como cuidar las plazas y el aseo de la comuna. Por eso, al tener un problema, hay que pensar en qué nivel se resuelve.",
        "Comparemos dos casos. Si el problema es que los juegos de la plaza del barrio están rotos, conviene hablar con la municipalidad. Si se quiere cambiar una ley para todo el país, eso lo discute el Congreso Nacional. Los ministros ayudan al Presidente a ejecutar políticas, como las de educación o salud. Cada autoridad responde por sus funciones.",
        "Votar es la forma en que las personas con derecho a voto participan. Si las autoridades se eligen, los votantes pueden decidir quién los representa. Lo que decide cada autoridad puede cambiar la vida de muchas personas, y por eso es importante informarse antes de votar. También se puede participar de otras maneras: opinando, asistiendo a reuniones de vecinos o pidiendo información a la municipalidad.",
    ],
    vocab=[("nivel", "alcance de un cargo: la comuna o todo el país"), ("representar", "hablar y decidir en nombre de otras personas"), ("política pública", "plan del Estado para resolver un tema, como educación o salud"), ("votante", "persona con derecho a votar"), ("participar", "tomar parte en las decisiones de la comunidad")],
    worked=[
        W("Elegir a quién acudir", "Los basureros de la plaza de tu barrio están rotos. ¿A qué autoridad conviene avisar?",
          ["El problema es de una plaza de la comuna.", "La municipalidad se ocupa de la comuna.", "Entonces conviene avisar al alcalde o a la municipalidad."], "A la municipalidad, dirigida por el alcalde"),
        W("Nivel de una decisión", "Se discute una ley para todo el país. ¿Dónde se discute?",
          ["Una ley vale para todo el país.", "Las leyes las discuten diputados y senadores.", "Lo hacen en el Congreso Nacional."], "En el Congreso Nacional"),
    ],
    mistakes=[
        M("Avisar al Presidente de todos los problemas del barrio.", "Hay autoridades más cercanas para cada asunto.", "Primero piensa en el nivel: comuna o país."),
        M("Creer que votar no cambia nada.", "Quienes ganan la elección toman decisiones que afectan a muchas personas.", "Votar es una forma de elegir a quienes decidirán."),
    ],
    tiers=tiers(
        [ex("Una ley para todo el país, ¿la discute el Congreso Nacional o el concejo de la comuna?", "El Congreso Nacional", "Las leyes valen para todo el país."),
         ex("Los juegos rotos de la plaza de tu barrio, ¿son un asunto de la comuna o de todo el país?", "De la comuna", "Se resuelve en la municipalidad."),
         ex("¿Quién decide el plan de educación del país: el Ministerio de Educación junto al Presidente o un vecino?", "El Ministerio de Educación junto al Presidente", "Los ministros ejecutan políticas del Presidente.")],
        [ex("¿Qué significa que una autoridad te represente?", "Que habla y decide en nombre de otras personas", "Esa es la idea de representar."),
         ex("¿Por qué conviene informarse antes de votar?", "Porque las autoridades toman decisiones que afectan a muchas personas", "Se vota por quien se cree que decidirá bien."),
         ex("Menciona dos formas de participar, además de votar.", "Por ejemplo: asistir a reuniones de vecinos y pedir información a la municipalidad", "Son formas de participar de la clase.")],
        [ex("Caso: faltan luces en una plaza. ¿Qué autoridad actúa primero: el alcalde o el senador?", "El alcalde", "Las plazas son de la comuna."),
         ex("Caso: se propone una ley sobre el uso de cascos para todo el país. ¿Quiénes la discuten: los diputados y senadores o los vecinos de una calle?", "Los diputados y senadores", "Las leyes las discute el Congreso."),
         ex("Caso: se quiere organizar una campaña de vacunación para todo el país. ¿Qué ministro, nombrado por el Presidente, dirige ese tema?", "El ministro de Salud", "Dirige el Ministerio de Salud.")],
        [ex("Ana dice: «Votar es inútil porque son muchas personas». ¿Qué le respondes?", "Que quienes ganan toman decisiones y votar es una forma de elegirlos", "Cada voto cuenta para elegir."),
         ex("Pedro avisó al Presidente de un pastizal sucio en su cuadra. ¿A quién conviene avisar primero?", "A la municipalidad", "Es un asunto de la comuna.")],
        [ex("Un grupo de vecinos quiere más contenedores de reciclaje en su comuna. Escribe a quién acudirían y qué le pedirían.", "A la municipalidad, para pedir más contenedores", "Es una decisión comunal."),
         ex("Escribe una semejanza y una diferencia entre un diputado y un alcalde.", "Semejanza: los dos son elegidos por votación; diferencia: el diputado trabaja en el Congreso y el alcalde en la municipalidad", "Se comparan forma de llegar e institución.")],
    ),
    context=[ex("Una escuela quiere arreglar los juegos de la plaza que está al frente. El director dice: «Esto lo resuelve la municipalidad». ¿Por qué tiene razón?", "Porque las plazas de la comuna son asunto de la municipalidad", "El alcalde dirige la municipalidad.")],
    selfcheck=[ex("¿Qué autoridad actúa en toda la comuna?", "El alcalde", "Dirige la municipalidad."), ex("¿Dónde se discuten las leyes?", "En el Congreso Nacional", "Allí trabajan senadores y diputados."), ex("Menciona una razón para votar con información.", "Las autoridades toman decisiones que afectan a muchas personas", "Es la idea de la clase.")],
    open_task=task("Lee estos tres problemas: A) una luz quemada en la plaza de la comuna, B) una nueva ley para todo el país, C) cambiar la forma de enseñar en todas las escuelas del país. Escribe a qué autoridad o institución acudirías en cada caso y una razón.", "A: la municipalidad, porque la plaza es de la comuna. B: el Congreso, porque las leyes valen para todo el país. C: el Ministerio de Educación.", ["cada problema tiene una autoridad", "explica el nivel comuna o país", "usa los cargos de la clase"], ["tres respuestas con razón"], ["avisar al Presidente por todo", "confundir alcalde con diputado"], "Pide a una persona que lea tus respuestas y te diga si está de acuerdo con el nivel que elegiste."),
    reinforce="Anota un problema de tu barrio y escribe a qué autoridad corresponde.",
    extend="Escribe una pregunta que le harías a tu alcalde para entender cómo cuida tu comuna.",
)
