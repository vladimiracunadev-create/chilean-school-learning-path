"""Atención de Enfermería, mención Adulto Mayor (4.º medio TP): OAM-01 (actividades sociales y recreativas), OAM-02 (informar a las familias) y OAM-03 (alimentación y nutrición del adulto mayor). Todo en papel: residencias, personas y familias inventadas y rotuladas «de ejemplo»; sin técnicas clínicas ni procedimientos."""
from __future__ import annotations

from tp_adma_common import LIM, build

O1 = "TP-ADMA-4-OAM-01"
O2 = "TP-ADMA-4-OAM-02"
O3 = "TP-ADMA-4-OAM-03"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (residencia de ejemplo, inventada). En la «Residencia Los Aromos de Ejemplo» viven 30 personas mayores. El equipo incluye una terapeuta ocupacional, una enfermera y 4 técnicos en enfermería. "
     "El taller social se hace los lunes y jueves, de 16:00 a 17:00, en un salón con 24 sillas estables. Para el taller del lunes, la enfermera indicó reposo a 3 residentes y 6 residentes dijeron que prefieren no participar. "
     "Reglas: la participación es voluntaria; se respeta el nombre y el trato de cada persona; el salón se deja despejado y se organizan pausas.")
build(
    O1, 1, F,
    use="Aprenderé quién planifica y quién apoya las actividades sociales de una residencia, qué principios las orientan y qué riesgos se previenen.",
    prior=["Conozco los derechos de los pacientes.", "Sé restar y comparar números.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería, mención Adulto Mayor, las actividades sociales y recreativas son momentos de encuentro, juego, conversación, música o manualidades que ayudan a la persona mayor a sentirse acompañada y a mantener sus capacidades. Las planifica el equipo con la terapeuta ocupacional o la enfermera, según los intereses de cada persona, y el técnico apoya con la organización, el acompañamiento y el registro.",
        "Los principios son tres: la participación voluntaria, es decir, nadie es obligado; el respeto a la autonomía y a la dignidad, lo que incluye no tratar a la persona como a un niño; y la seguridad individual y grupal, con un espacio despejado, sillas estables y pausas. Los riesgos más frecuentes son las caídas, la fatiga y la frustración si la actividad no se adapta a la persona.",
        "Si alguien se siente mal, se cae o tiene un malestar repentino durante la actividad, el técnico no actúa por cuenta propia: avisa de inmediato a la enfermera y a emergencias." + LIM,
    ],
    vocab=[("actividad social", "momento de encuentro, juego, conversación o música para acompañar a la persona mayor"), ("terapeuta ocupacional", "profesional que ayuda a mantener las capacidades en las actividades diarias"), ("participación voluntaria", "nadie es obligado a participar"), ("autonomía", "capacidad de decidir y hacer por sí misma lo que puede"), ("seguridad grupal", "cuidado del espacio y del grupo para evitar accidentes"), ("infantilizar", "tratar a una persona mayor como a un niño")],
    worked=[
        ("Elegir un tratamiento respetuoso", "Un técnico de ejemplo se dirige a una residente con «ya, mijita, a ponerse el gorro». ¿Qué principio se descuida?", ["El trato debe ser respetuoso y por su nombre.", "Se descuida la dignidad: es un trato infantilizado."], "La dignidad: el trato debe ser respetuoso y por su nombre"),
        ("Calcular participantes", "En otra residencia de ejemplo viven 20 personas, 2 están en reposo por indicación y 5 prefieren no participar. ¿Cuántas podrían participar?", ["20 − 2 − 5 = 13.", "Participan quienes pueden y quieren."], "13 personas")],
    mistakes=[("Insistir con una residente que prefiere no participar «para que se integre».", "Se vulnera su derecho a decidir; la participación es voluntaria.", "Ofrece otras opciones y respeta su decisión, e infórmalo a la enfermera."),
              ("Mover las sillas entre actividades sin dejar espacio libre «porque caben más».", "Reduce el espacio para caminar y aumenta el riesgo de caídas.", "Mantén pasillos despejados y sillas estables.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué significa que la participación sea voluntaria?", "Que nadie es obligado a participar", "Que todos deben participar siempre", "Que la familia decide por la persona", "La participación es una decisión de la persona mayor; no se obliga."),
        ("abc", "{F} ¿Quién indicó el reposo de 3 residentes?", "La enfermera", "La terapeuta ocupacional", "Los técnicos", "La ficha dice que la enfermera indicó el reposo."),
        ("abc", "{F} ¿Qué debe hacer el técnico con la lista de quienes prefieren no participar?", "Respetar su decisión y registrarla", "Convencerlos de ir con insistencia", "Excluirlos de otras actividades", "La decisión de no participar se respeta y se registra."),
        ("=", "{F} ¿Cuántos residentes podrían participar en el taller del lunes?", "30-3-6", "Se restan los residentes en reposo y los que prefieren no participar.", " residentes"),
        ("=", "{F} ¿Cuántas sillas quedarían libres en el salón del lunes si participan todos los posibles?", "24-(30-3-6)", "Se restan los participantes posibles de las sillas del salón.", " sillas"),
        ("=", "{F} ¿Cuántas horas de taller hay en una semana, con los dos días?", "2*(17-16)", "Se multiplican los días por la duración de cada taller.", " horas"),
        ("abc", "{F} Una residente dice que hoy no quiere ir al taller. ¿Qué hace el técnico?", "Respeta su decisión, le ofrece otras opciones y lo registra", "Le dice que debe ir porque es parte del programa", "La deja sola sin avisar a nadie", "Se respeta su autonomía y se ofrecen alternativas."),
        ("abc", "{F} Un técnico responde por un residente sin preguntarle y dice «él no entiende, yo decido por él». ¿Qué principio descuida?", "El respeto a la autonomía y a la dignidad", "La seguridad grupal", "El orden de las sillas del salón", "La persona mayor decide por sí misma lo que puede; hablar y decidir por ella le quita autonomía y dignidad."),
        ("abc", "{F} Durante el taller, una residente dice que se siente mareada y se agarra del respaldo de la silla. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias, y acompaña sin darle nada", "Le da agua y pide que continúe", "Le pide que camine hasta su cama", "Ante un malestar repentino se avisa de inmediato; no se actúa por cuenta propia."),
        ("abc", "{F} Un compañero quiere sacar las 24 sillas del salón y poner 30 para que quepan todos. ¿Qué corresponde?", "No hacerlo: el salón se deja despejado para que todos puedan moverse con seguridad", "Hacerlo, porque todos tienen derecho", "Hacerlo solo si las sillas están cerca de la pared", "Poner más sillas de las que caben reduce el espacio libre y aumenta el riesgo de caídas."),
        ("abc", "{F} Un compañero dice: «Si se cae alguien en el taller, lo ayudo a levantarse rápido». ¿Qué corresponde responder?", "Que ante una caída se avisa de inmediato a la enfermera y a emergencias, sin mover a la persona", "Que sí, para que no se asuste", "Que sí, si la persona lo pide", "Mover a una persona caída puede agravar una lesión; se avisa de inmediato."),
        ("=", "{F} Si el taller se hiciera un día más a la semana, ¿cuántas horas de taller habría en 4 semanas?", "3*(17-16)*4", "Se multiplican los días por la duración y por las semanas.", " horas"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué hace el técnico en una actividad social?", "Apoya la organización, acompaña y registra", "Decide por sí solo la actividad de cada persona", "Hace un diagnóstico de cada participante", "El técnico apoya; la planificación la hace el equipo con la terapeuta o la enfermera."),
    ],
    ctx=("abc", "{F} Una residente que llegó hace una semana se queda sola mirando por la ventana durante el taller. El técnico nota que no ha hablado con nadie. ¿Qué hace?", "La invita con respeto, sin presionarla, y cuenta lo observado a la terapeuta ocupacional o a la enfermera", "La obliga a sentarse con el grupo", "Anota que es una persona antisocial", "Se invita sin presionar y se informa lo observado; las etiquetas no ayudan."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿es obligatorio participar en una actividad social?", "No, es voluntaria", "Es la propia persona mayor quien decide si participa."),
        ("¿Qué haces si alguien se cae durante la actividad?", "Aviso de inmediato a la enfermera y a emergencias", "No muevo a la persona ni actúo por cuenta propia."),
        ("¿Qué es infantilizar?", "Tratar a una persona mayor como a un niño", "Esa forma de tratar a la persona vulnera su dignidad."),
    ],
    op=("Caso de ejemplo: la enfermera te pide apoyar un taller de música del jueves en la residencia de la ficha, de 16:00 a 17:00. Hay 30 residentes: 4 están en reposo y 8 prefieren no participar. "
        "Escribe: cuántas personas podrían participar y cuántas sillas libres quedan en el salón de 24; qué harías con quien no quiere participar; qué harías si una residente se cae; y una frase de registro con un hecho observable.",
        "Participantes posibles: 30 − 4 − 8 = 18; sillas libres: 24 − 18 = 6. Quien no quiere participar: respetar su decisión y ofrecer otras opciones. Si una residente se cae: avisar de inmediato a la enfermera y a emergencias, sin moverla. Registro: «Jueves 16:00, taller de música, participaron 18 personas; Luisa prefirió ver la televisión».",
        ["calcula 18 participantes y 6 sillas libres", "respeta la decisión de no participar", "avisa de inmediato ante una caída", "el registro es un hecho"],
        ["hoja con dos cálculos, una conducta, una conducta ante la caída y un registro"],
        ["obligar a participar", "mover a la persona caída", "escribir una etiqueta en el registro"],
        "Pregunta: «¿qué hace el técnico ante la caída: ayudar a levantar o avisar?». Debe responder avisar de inmediato."),
    reinforce="Escribe tres principios de una actividad social para personas mayores y un ejemplo de cada uno.",
    extend="Explica con un ejemplo inventado por qué llamar «abuelito» o «mijita» a una persona mayor puede afectar su dignidad.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (preferencias de residentes de ejemplo, inventada). Actividades propuestas: canto, dominó, tejido y conversatorio. Marcas de interés de cada residente: Ana, canto y conversatorio; Beto, dominó, conversatorio y canto; Carmen, tejido, canto y conversatorio; Dante, conversatorio y dominó. "
     "Notas del equipo (de ejemplo): Ana ve poco y necesita letra grande; Beto oye poco y debe sentarse cerca de quien habla; Carmen tiene temblor en las manos y necesita agujas gruesas; Dante se pone nervioso con el ruido fuerte. "
     "Dimensiones de la persona: biológica (cuerpo y salud), psicológica (emociones y pensamientos) y social (relaciones y entorno).")
build(
    O1, 2, F,
    use="Aprenderé qué significa «biopsicosocial», cómo se leen los intereses y las necesidades de una persona mayor y qué técnicas de motivación y recursos son apropiados.",
    prior=["Conozco los principios de una actividad social.", "Sé contar marcas en una tabla.", "Sé leer una ficha."],
    explain=[
        "Biopsicosocial significa que una persona se entiende en tres dimensiones a la vez: la biológica (el cuerpo y su salud), la psicológica (las emociones y los pensamientos) y la social (sus relaciones y su entorno). Al planificar una actividad se consideran las tres: si la persona ve poco, necesita letra grande (biológica); si le da vergüenza equivocarse, necesita un ambiente de confianza (psicológica); si disfruta compartir, se favorece el trabajo en grupo (social).",
        "Las técnicas de motivación son maneras respetuosas de invitar: ofrecer opciones, reconocer lo que la persona sabe hacer, recordar sus logros y no presionar. Los recursos y materiales deben ser seguros, adecuados a la edad, con letra grande, sin piezas que puedan tragarse ni estridencias. La ficha de intereses se usa solo para organizar mejor las actividades, y su información es confidencial.",
        "El técnico anota lo que observa; no decide diagnósticos ni limita a una persona por una nota." + LIM,
    ],
    vocab=[("biopsicosocial", "que considera a la vez el cuerpo, las emociones y las relaciones de la persona"), ("interés", "actividad que a la persona le gusta y quiere hacer"), ("necesidad", "ayuda o ajuste que permite participar a la persona"), ("técnica de motivación", "forma respetuosa de invitar a participar, sin presionar"), ("material apropiado", "material seguro y adaptado a las capacidades de las personas"), ("ficha de intereses", "documento confidencial con las preferencias de cada persona")],
    worked=[
        ("Ubicar una necesidad", "Un residente de ejemplo se siente solo y quiere hacer amigos. ¿En qué dimensión está esa necesidad?", ["Hacer amigos tiene que ver con las relaciones.", "Es una necesidad de la dimensión social."], "La dimensión social"),
        ("Contar intereses", "En otra ficha de ejemplo, 3 de 5 residentes marcaron «pintura» y 2 marcaron «bingo». ¿Cuántas marcas hay en total?", ["Se suman las marcas de ambas actividades.", "3 + 2 = 5."], "5 marcas")],
    mistakes=[("Elegir la misma actividad para todos «porque es más fácil».", "Cada persona tiene intereses y necesidades distintos; una sola actividad deja fuera a algunos.", "Ofrece opciones y adapta los materiales."),
              ("Usar materiales con piezas muy pequeñas porque «los adultos no se las llevan a la boca».", "Pueden caerse, perderse o provocar accidentes si hay dificultad para ver o coordinar.", "Elige materiales grandes, seguros y fáciles de tomar.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué significa «biopsicosocial»?", "Que considera a la vez el cuerpo, las emociones y las relaciones de la persona", "Que se ocupa solo de la salud del cuerpo", "Que se ocupa solo de las actividades en grupo", "Biopsicosocial es una mirada que reúne las tres dimensiones."),
        ("abc", "{F} ¿Qué necesita Ana según las notas del equipo?", "Letra grande", "Agujas gruesas", "Un lugar sin ruido", "La ficha dice que Ana ve poco y necesita letra grande."),
        ("abc", "{F} ¿En qué dimensión está la necesidad de Dante de evitar el ruido fuerte?", "Psicológica", "Biológica", "Social", "Ponerse nervioso tiene que ver con sus emociones y su bienestar."),
        ("abc", "{F} ¿Cuántos residentes marcaron interés en el canto?", "Tres", "Dos", "Cuatro", "Marcaron canto Ana, Beto y Carmen; Dante no lo marcó."),
        ("=", "{F} ¿Cuántas marcas de interés hay en total entre los cuatro residentes?", "2+3+3+2", "Se suman las marcas de Ana, Beto, Carmen y Dante.", " marcas"),
        ("=", "{F} ¿Cuántas marcas más tiene el conversatorio que el tejido?", "4-1", "Se restan las marcas del tejido de las del conversatorio.", " marcas"),
        ("abc", "{F} ¿Cuál es la actividad con más marcas de interés?", "El conversatorio", "El canto", "El dominó", "El conversatorio fue marcado por los cuatro residentes; es el que tiene más."),
        ("abc", "{F} ¿Qué adaptación necesita el tejido para Carmen?", "Agujas gruesas", "Letra grande", "Un lugar sin ruido", "La nota dice que Carmen necesita agujas gruesas por el temblor en las manos."),
        ("abc", "{F} Para el canto, ¿dónde conviene sentar a Beto?", "Cerca de quien dirige, para que oiga mejor", "Al fondo, para que no moleste", "Fuera del salón", "La nota dice que oye poco y debe sentarse cerca de quien habla."),
        ("abc", "{F} Un compañero propone que Dante participe del canto porque «es la actividad más popular». ¿Qué corresponde?", "Respetar sus intereses: Dante marcó conversatorio y dominó, y se pone nervioso con el ruido fuerte", "Obligarlo, porque a la mayoría le gusta", "Ignorar sus preferencias", "La participación se basa en los intereses de cada persona, no en lo que elige la mayoría."),
        ("abc", "{F} Una técnica quiere decir en voz alta, frente al grupo, que Carmen tiembla al tejer. ¿Qué corresponde?", "No hacerlo: la información es confidencial y puede avergonzarla", "Hacerlo, para que todos la ayuden", "Hacerlo solo si Carmen no se da cuenta", "Las notas de la ficha son confidenciales y no se comentan frente a otros."),
        ("=", "{F} Si el conversatorio se hace en grupos de 2 personas, ¿cuántos grupos se forman con los residentes que lo marcaron?", "4//2", "Se divide la cantidad de residentes interesados entre el tamaño de cada grupo.", " grupos"),
        ("abc", "{F} ¿Qué técnica de motivación es respetuosa con Beto, que dudó de participar en el dominó?", "Ofrecerle opciones y recordarle que juega bien", "Decirle que si no participa pierde su lugar", "Anunciar su nombre para que todos lo miren", "Reconocer lo que sabe hacer y ofrecer opciones motiva sin presionar."),
    ],
    ctx=("abc", "{F} Una residente dice al técnico que ya no quiere tejer porque «con estas manos no sirvo para nada». ¿Qué hace?", "La escucha con respeto, le ofrece materiales más fáciles y cuenta lo observado a la terapeuta ocupacional", "Le dice que no sea negativa", "Le quita el tejido para que no se frustre", "Se acoge su emoción y se adapta el recurso; la terapeuta decide cómo seguir."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cuáles son las tres dimensiones del enfoque biopsicosocial?", "Biológica, psicológica y social", "Reúnen el cuerpo, las emociones y las relaciones."),
        ("¿Qué materiales son apropiados para personas mayores?", "Seguros, con letra grande y fáciles de tomar", "Se adaptan a las capacidades de cada persona."),
        ("¿Qué haces con la información de la ficha de intereses?", "La uso para organizar mejor las actividades y la mantengo confidencial", "La ficha es privada y no se comenta con otros."),
    ],
    op=("Ficha de ejemplo: «Residentes y marcas: Elena, bingo y jardinería; Felipe, bingo, ajedrez y jardinería; Gloria, jardinería; Hernán, bingo y ajedrez. Notas: Elena usa andador; Felipe se cansa rápido; Gloria tiene dolor en las manos; Hernán ve poco». "
        "Escribe: cuántas marcas tiene cada actividad; cuál elegirías para el grupo y por qué; una adaptación por cada nota; y una frase de motivación respetuosa.",
        "Bingo 3 (Elena, Felipe, Hernán), jardinería 3 (Elena, Felipe, Gloria), ajedrez 2 (Felipe, Hernán). Elegiría bingo o jardinería, que empatan con 3 marcas; para decidir se consulta al grupo. Adaptaciones: Elena, espacio libre para el andador; Felipe, pausas; Gloria, herramientas livianas de agarre fácil; Hernán, cartones con letra grande. Frase: «Tú sabes mucho de plantas, ¿te gustaría mostrarnos cómo lo haces?».",
        ["cuenta 3, 3 y 2 marcas", "reconoce el empate entre bingo y jardinería", "propone una adaptación por nota", "la frase de motivación es respetuosa"],
        ["hoja con tres conteos, una elección razonada, cuatro adaptaciones y una frase"],
        ["decir que hay una única actividad más popular", "obligar a participar", "comentar las notas frente al grupo"],
        "Pregunta: «¿hay una sola actividad con más marcas?». Debe notar el empate y proponer consultar al grupo."),
    reinforce="Escribe una necesidad biológica, una psicológica y una social de una persona mayor de ejemplo y una adaptación para cada una.",
    extend="Explica con un ejemplo inventado por qué una actividad pensada para un niño puede resultar poco respetuosa para una persona mayor.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (planificación de un taller de ejemplo). Taller de música, 45 minutos, 12 residentes: 10 minutos de bienvenida, 25 de desarrollo y 10 de cierre. Material: 12 sillas con respaldo, 6 instrumentos de percusión livianos y letras impresas en letra grande. "
     "Notas del equipo: Irene usa andador; Jorge se cansa con rapidez; Karen oye poco. Regla del taller: el espacio se deja despejado, se hacen pausas y nadie es obligado a participar. "
     "Observación del técnico durante el taller: Jorge se retiró a los 20 minutos y dijo que estaba cansado; Karen no cantó, pero siguió el ritmo con las manos; Irene participó todo el taller.")
build(
    O1, 3, F,
    use="Aprenderé a analizar un caso de planificación y de observación de un taller, a evaluar si se cuidó la seguridad y la participación de cada persona y a informar lo observado.",
    prior=["Conozco los principios de una actividad social.", "Conozco la ficha de intereses.", "Sé calcular tiempos."],
    explain=[
        "Para analizar una actividad se compara lo planificado con lo que ocurrió. Se revisa si los tiempos se cumplieron, si el material alcanzó para todos, si el espacio fue seguro y si cada persona pudo participar a su manera. Participar «a su manera» incluye distintas formas de hacerlo: cantar, seguir el ritmo, mirar o retirarse cuando se está cansado.",
        "Cuando una persona se retira o participa menos, no es un fracaso: es información. El técnico anota el hecho, sin etiquetas, por ejemplo «se retiró a los 20 minutos y dijo que estaba cansado», y lo informa a la terapeuta o a la enfermera para ajustar la próxima actividad, por ejemplo con más pausas. Si el cansancio fuera acompañado de un malestar repentino, se avisa de inmediato a la enfermera.",
        "La evaluación se hace sobre la actividad y no sobre la persona." + LIM,
    ],
    vocab=[("planificación", "plan escrito de lo que se hará, con tiempos, materiales y adaptaciones"), ("participar a su manera", "tomar parte de acuerdo con las capacidades y los deseos de cada persona"), ("observación", "mirar lo que ocurre y anotar hechos"), ("ajuste", "cambio en la próxima actividad para que sea más adecuada"), ("pausa", "momento de descanso dentro de una actividad")],
    worked=[
        ("Revisar los tiempos", "En un taller de ejemplo de 60 minutos, la bienvenida duró 10 y el desarrollo 35. ¿Cuánto debe durar el cierre para cumplir el tiempo?", ["Se suman bienvenida y desarrollo: 10 + 35 = 45.", "60 − 45 = 15."], "15 minutos"),
        ("Distinguir un hecho de una opinión", "Un técnico de ejemplo anota «Marta es una residente complicada». ¿Es un hecho?", ["Es un juicio sobre la persona, no una observación.", "Un hecho sería «Marta se levantó a los 15 minutos y pidió ir a su pieza»."], "No, es una opinión")],
    mistakes=[("Anotar «Jorge no tiene ganas de participar» cuando se retiró por cansancio.", "Atribuye una intención que el técnico no sabe y puede etiquetarlo.", "Anota lo que hizo y dijo: «se retiró a los 20 minutos y dijo que estaba cansado»."),
              ("Dar por fracasado el taller porque una persona se retiró.", "Se mide la actividad completa y cada persona participó a su manera.", "Analiza qué ajustar, como más pausas, sin culpar a nadie.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué significa «participar a su manera»?", "Tomar parte según las capacidades y los deseos de cada persona", "Hacer exactamente lo que hace el grupo", "Participar solo en la bienvenida", "Cada persona participa de una forma distinta y válida."),
        ("abc", "{F} ¿Cuántos minutos dura el taller completo?", "45", "35", "60", "La ficha dice que dura 45 minutos: 10 de bienvenida, 25 de desarrollo y 10 de cierre."),
        ("=", "{F} Jorge se retiró a los 20 minutos de comenzar el taller. ¿Cuántos minutos del taller quedaron sin su participación?", "45-20", "Se resta el tiempo que participó de la duración total.", " minutos"),
        ("=", "{F} ¿Cuántos residentes más que instrumentos hay en el taller?", "12-6", "Se restan los instrumentos de los residentes.", " residentes"),
        ("abc", "{F} ¿Cómo participó Karen según la observación?", "Siguió el ritmo con las manos, sin cantar", "No participó", "Cantó todo el taller", "La observación dice que no cantó, pero siguió el ritmo con las manos."),
        ("abc", "{F} ¿Qué anota el técnico sobre Jorge?", "«Se retiró a los 20 minutos y dijo que estaba cansado»", "«Jorge no tiene ganas de participar»", "«Jorge es una persona perezosa»", "El registro describe lo que hizo y dijo, sin atribuir intenciones."),
        ("abc", "{F} ¿Qué ajuste razonable propone el técnico a la enfermera para el próximo taller?", "Agregar pausas para quienes se cansan", "Prohibir que Jorge participe", "Cobrar a los participantes", "Las pausas permiten que más personas participen sin forzarse."),
        ("=", "{F} Si cada instrumento se comparte entre 2 residentes, ¿cuántos residentes pueden usar instrumento a la vez?", "6*2", "Se multiplican los instrumentos por los residentes que comparten cada uno.", " residentes"),
        ("abc", "{F} Irene usa andador. ¿Qué cuidado del espacio es importante para ella?", "Mantener los pasillos despejados y las sillas estables", "Poner sillas en todos los pasillos", "Retirar el andador durante el taller", "El espacio libre permite que se mueva con seguridad."),
        ("abc", "{F} Un compañero dice: «Que Jorge se retire demuestra que el taller fue un fracaso». ¿Qué corresponde responder?", "Que fue información para ajustar: se evalúa la actividad completa, no a una persona", "Que sí, porque no todos participaron hasta el final", "Que sí, y que hay que obligar a Jorge a quedarse", "Una persona que se retira por cansancio no hace fracasar el taller; se ajusta."),
        ("abc", "{F} A los 20 minutos, Jorge, además de cansado, dice que le duele el pecho. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias, y lo acompaña sin darle nada", "Le ofrece agua y que descanse un rato", "Anota que es cansancio y sigue con el taller", "Un dolor en el pecho no se evalúa en la sala: se avisa de inmediato."),
        ("=", "{F} ¿Cuántos minutos tiene el desarrollo más el cierre del taller?", "25+10", "Se suman los minutos del desarrollo y del cierre.", " minutos"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿para qué se anota una observación sin etiquetas?", "Para que el equipo pueda ajustar la actividad con datos concretos", "Para decidir quién no participa más", "Para entregar un informe a la familia sin avisar a la persona", "Los hechos permiten mejorar la actividad sin dañar a la persona."),
    ],
    ctx=("abc", "{F} Karen no cantó durante el taller y la técnica piensa en escribir que «Karen no sabe cantar». ¿Qué corresponde?", "Anotar que siguió el ritmo con las manos y que no cantó, sin interpretar", "Anotar que no sabe cantar", "No anotar nada, porque no hay nada importante", "Se describe lo observado; interpretar puede etiquetar a la persona."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué se anota en la observación?", "Hechos: qué hizo o dijo la persona", "Los hechos permiten ajustar sin etiquetar."),
        ("¿Qué haces si una persona dice que le duele el pecho?", "Aviso de inmediato a la enfermera y a emergencias", "No se evalúa en la sala ni se da nada."),
        ("¿Qué se puede ajustar si alguien se cansa?", "Agregar pausas", "Así más personas participan sin forzarse."),
    ],
    op=("Planificación de ejemplo: taller de jardinería, 50 minutos, 10 residentes: 10 de bienvenida, 30 de desarrollo y 10 de cierre; 5 macetas grandes y 10 palas pequeñas livianas. Observación: «Lola participó los 50 minutos; Mario dejó el taller a los 25 minutos y dijo que le dolían las rodillas; Nora miró desde su silla y sonrió». "
        "Escribe: cuántas palas más que macetas hay; qué hizo cada persona como hecho observable; qué ajuste propondrías; y qué harías si Mario hubiera dicho que le dolía el pecho.",
        "Palas más que macetas: 10 − 5 = 5. Lola participó los 50 minutos; Mario se retiró a los 25 minutos y dijo que le dolían las rodillas; Nora miró y sonrió. Ajuste: más pausas y asientos más cercanos. Si hubiera dicho dolor en el pecho: avisar de inmediato a la enfermera y a emergencias.",
        ["calcula 5 palas más", "describe tres hechos sin etiquetas", "propone un ajuste", "avisa de inmediato ante el dolor en el pecho"],
        ["hoja con un cálculo, tres hechos, un ajuste y una conducta ante el dolor"],
        ["escribir una etiqueta sobre Mario", "decidir por su cuenta qué hacer con el dolor", "olvidar el ajuste"],
        "Pregunta: «¿tu frase sobre Nora describe lo que hizo o lo que piensas de ella?». Si piensa, pídele reescribirla."),
    reinforce="Reescribe tres frases con etiquetas, como «es floja» o «no quiere», convirtiéndolas en hechos observables.",
    extend="Explica con un ejemplo inventado por qué una persona que se retira de una actividad aporta información útil al equipo.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (programa mensual de talleres, de ejemplo). Ocho talleres de 1 hora en el mes. Asistencia por taller: 18, 20, 16, 22, 20, 18, 24 y 22 residentes. Aforo del salón: 24 sillas. "
     "Meta del equipo (de ejemplo): un promedio de al menos 18 residentes por taller. Material: 2 hojas de trabajo por residente asistente y 6 hojas de repuesto por taller. "
     "Regla de acompañamiento (de ejemplo): un técnico por cada 8 residentes presentes; en el taller de 24 residentes se necesitan 3 técnicos.")
build(
    O1, 4, F,
    use="Aprenderé a calcular asistencia, promedio, uso del aforo, material y personal de apoyo de un programa de talleres y a compararlos con una meta.",
    prior=["Sé sumar y dividir números enteros.", "Conozco el taller social y su planificación.", "Sé leer una tabla."],
    explain=[
        "Un programa de actividades se evalúa con números simples. La asistencia total es la suma de los asistentes de cada taller. El promedio es la asistencia total dividida por la cantidad de talleres, y se compara con la meta del equipo. El aforo es la cantidad máxima de personas que caben con seguridad; superarlo es un riesgo. El material se calcula con las hojas por asistente más las de repuesto.",
        "También se calcula cuántos técnicos hacen falta para acompañar con seguridad al grupo: se divide el número de residentes presentes entre los que cada técnico puede acompañar. Los números sirven para organizar mejor y para ver qué ajustar, no para juzgar a las personas que asisten menos o más.",
        "Los datos son inventados y los valores de acompañamiento son solo de ejemplo; los reales los fija la norma vigente y el establecimiento." + LIM,
    ],
    vocab=[("asistencia total", "suma de los asistentes de todos los talleres"), ("promedio", "asistencia total dividida por la cantidad de talleres"), ("aforo", "cantidad máxima de personas que caben con seguridad"), ("meta", "valor que el equipo se propone alcanzar"), ("acompañamiento", "presencia de técnicos que apoyan y cuidan al grupo")],
    worked=[
        ("Calcular un promedio", "En otro programa de ejemplo, tres talleres tuvieron 12, 15 y 18 asistentes. ¿Cuál fue el promedio?", ["12 + 15 + 18 = 45.", "45 ÷ 3 = 15."], "15 asistentes"),
        ("Técnicos necesarios", "Con la regla de un técnico por cada 8 residentes, ¿cuántos técnicos hacen falta para 16 residentes?", ["Se divide la cantidad de residentes entre los que acompaña cada técnico.", "Se dividen 16 residentes entre 8 por técnico: 16 ÷ 8 = 2."], "2 técnicos")],
    mistakes=[("Poner más sillas que el aforo «porque llegaron más personas».", "Se reduce el espacio libre y se aumenta el riesgo de caídas.", "Respeta el aforo y ofrece otra sesión o un grupo adicional."),
              ("Calcular el promedio dividiendo entre los residentes de la residencia.", "El promedio de un programa se calcula sobre los talleres realizados.", "Divide la asistencia total entre el número de talleres.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es el aforo?", "La cantidad máxima de personas que caben con seguridad en un lugar", "El número de talleres de un mes", "El total de residentes de la residencia", "El aforo se fija para cuidar la seguridad del espacio."),
        ("=", "{F} ¿Cuántos residentes asistieron en total a los ocho talleres?", "18+20+16+22+20+18+24+22", "Se suman las asistencias de cada taller.", " residentes"),
        ("=", "{F} ¿Cuál fue el promedio de asistencia por taller?", "(18+20+16+22+20+18+24+22)//8", "Se divide la asistencia total entre los ocho talleres.", " residentes"),
        ("abc", "{F} ¿Se alcanzó la meta del equipo?", "Sí: el promedio de 20 supera los 18 residentes de la meta", "No: el promedio es menor que 18", "No se puede saber con los datos", "La meta era un promedio de al menos 18 residentes por taller."),
        ("=", "{F} ¿Cuántos residentes más que la meta asistieron en promedio?", "(18+20+16+22+20+18+24+22)//8-18", "Se resta la meta del promedio de asistencia.", " residentes"),
        ("=", "{F} ¿Cuántas hojas de trabajo se preparan para el taller de 24 residentes?", "24*2+6", "Se multiplican las hojas por asistente y se suman las de repuesto.", " hojas"),
        ("=", "{F} Según la regla de acompañamiento, ¿cuántos residentes puede acompañar un equipo de 2 técnicos?", "2*8", "Se multiplican los técnicos por los residentes que acompaña cada uno.", " residentes"),
        ("=", "{F} ¿Cuántas hojas de trabajo se preparan para el taller de 16 residentes?", "16*2+6", "Se multiplican las hojas por asistente y se suman las de repuesto.", " hojas"),
        ("abc", "{F} En el taller del día 7, que tuvo 24 residentes, llegan 2 residentes más. ¿Qué corresponde?", "No superar el aforo de 24: ofrecer otro horario o grupo a quienes no caben", "Poner dos sillas más en el pasillo", "Hacerlos sentarse en el suelo", "El aforo cuida la seguridad; se ofrece otra opción."),
        ("=", "{F} ¿Cuántas sillas libres hubo en el taller de menor asistencia?", "24-16", "Se restan los asistentes del taller de menor asistencia del aforo.", " sillas"),
        ("abc", "{F} El taller 3 tuvo la menor asistencia. ¿Cuál es la actitud adecuada?", "Revisar horario y forma de invitar, sin culpar a los residentes", "Reclamar a los residentes por no asistir", "Anotar los nombres de quienes faltaron para reprenderlos", "La baja asistencia se analiza para ajustar la actividad, no para culpar."),
        ("abc", "{F} Un compañero dice: «El promedio es solo un número, no importa». ¿Qué corresponde responder?", "Que el promedio ayuda a organizar materiales y personal y a ver si se alcanza la meta", "Que tiene razón, porque no cuenta a cada persona", "Que solo importa en el último taller", "Los números permiten organizar mejor y ajustar el programa."),
        ("=", "{F} Si el próximo mes se hicieran 10 talleres con el mismo promedio, ¿cuántas asistencias habría en total?", "(18+20+16+22+20+18+24+22)//8*10", "Se multiplica el promedio por la cantidad de talleres.", " asistencias"),
    ],
    ctx=("abc", "{F} Al preparar el taller de 24 residentes, el técnico ve que solo hay 2 técnicos disponibles y la regla pide 3. ¿Qué hace?", "Avisa a la enfermera para que consiga otro apoyo o reduzca el grupo, y no comienza sin el acompañamiento", "Comienza igual con 2 técnicos", "Pide a un residente que ayude a cuidar al grupo", "Un grupo sin el acompañamiento mínimo es un riesgo; se avisa antes de comenzar."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cómo se calcula el promedio de asistencia?", "Asistencia total ÷ cantidad de talleres", "Resume la asistencia de varios talleres."),
        ("¿Qué haces si llegan más personas que el aforo?", "No supero el aforo y ofrezco otra opción", "El aforo cuida la seguridad de todas las personas presentes."),
        ("¿Cuántos técnicos se necesitan para 16 residentes con la regla de 1 por cada 8?", "2", "Se dividen 16 residentes entre 8 por técnico: 16 ÷ 8 = 2."),
    ],
    op=("Programa de ejemplo: «Seis talleres con 12, 15, 9, 18, 15 y 21 asistentes; aforo 24; meta: promedio de al menos 14; 2 hojas por asistente y 4 de repuesto por taller; un técnico por cada 6 residentes». "
        "Calcula: la asistencia total, el promedio y si se alcanzó la meta; las hojas del taller de 21 asistentes; los técnicos del taller de 18. Escribe qué harías si el taller más lleno tuviera más personas que el aforo.",
        "Total: 12+15+9+18+15+21 = 90; promedio: 90 ÷ 6 = 15, que supera la meta de 14. Hojas del taller de 21: 21×2+4 = 46. Técnicos del taller de 18: 18 ÷ 6 = 3. Si hubiera más personas que el aforo: no superarlo y ofrecer otro horario o grupo.",
        ["calcula 90 y 15", "compara con la meta", "calcula 46 hojas y 3 técnicos", "respeta el aforo"],
        ["hoja con cuatro cálculos, una comparación y una conducta"],
        ["calcular mal el promedio", "olvidar las hojas de repuesto", "superar el aforo"],
        "Pregunta: «¿tu promedio divide entre los talleres o entre los residentes?». Debe dividir entre los talleres."),
    reinforce="Con asistencias de 10, 14 y 12 en tres talleres, calcula el promedio y cuántos técnicos hacen falta en el de 14 si cada uno acompaña a 7 residentes.",
    extend="Explica con un ejemplo inventado por qué una baja asistencia debe analizarse sin culpar a las personas.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (comparar propuestas, de ejemplo). Propuesta A: bingo con cartones y fichas grandes, 45 minutos, sentados, en grupo de 16 residentes. Propuesta B: juego de mesa con piezas pequeñas y reglas complejas, 45 minutos, en grupos de 4. "
     "Propuesta C: caminata larga por el jardín, 60 minutos, sin pausas programadas. Puntaje de 0 a 2 por criterio (2 cumple bien, 1 cumple en parte, 0 no cumple): A, intereses 2, accesibilidad 2, seguridad 2, socialización 2; B, intereses 1, accesibilidad 0, seguridad 1, socialización 2; C, intereses 1, accesibilidad 1, seguridad 0, socialización 1. "
     "Lista de verificación antes de realizar la actividad (6 puntos): espacio despejado; sillas estables; material seguro; técnicos suficientes; pausas previstas; aviso a la enfermera de residentes con reposo.")
build(
    O1, 5, F,
    use="Aprenderé a comparar propuestas de actividad con criterios, a elegir una con justificación y a verificar la seguridad con una lista antes de realizarla.",
    prior=["Conozco los principios de una actividad social.", "Sé sumar puntajes.", "Sé leer una lista de verificación."],
    explain=[
        "Comparar alternativas es ponerlas frente a los mismos criterios. En una actividad para personas mayores, los criterios son los intereses del grupo, la accesibilidad (que puedan participar con sus capacidades), la seguridad y la socialización. Se da un puntaje a cada criterio y se suma, y la propuesta con más puntaje es la más conveniente, siempre que ninguna cumpla en cero un criterio de seguridad.",
        "Elegir una propuesta no termina el trabajo: antes de realizarla se verifica con una lista que el espacio esté despejado, las sillas sean estables, el material sea seguro, haya suficientes técnicos, estén previstas las pausas y la enfermera haya informado de los residentes con reposo. Si algún punto falla, se avisa a la enfermera antes de comenzar y no se improvisa.",
        "Los puntajes de esta clase son de ejemplo para practicar la comparación." + LIM,
    ],
    vocab=[("criterio", "aspecto con el que se compara una propuesta"), ("accesibilidad", "posibilidad de que todas las personas participen con sus capacidades"), ("socialización", "oportunidad de relacionarse con otros"), ("puntaje", "número que indica cuánto cumple una propuesta cada criterio"), ("lista de verificación", "puntos que se revisan antes de comenzar una actividad")],
    worked=[
        ("Sumar un puntaje", "Una propuesta de ejemplo tiene intereses 1, accesibilidad 2, seguridad 2 y socialización 1. ¿Cuántos puntos suma?", ["Se suman los cuatro puntajes.", "1 + 2 + 2 + 1 = 6."], "6 puntos"),
        ("Aplicar el criterio de seguridad", "Una propuesta de ejemplo suma 7 de 8 puntos, pero tiene 0 en seguridad. ¿Se elige?", ["Un 0 en seguridad es un riesgo que no se acepta.", "No se elige, aunque suma muchos puntos."], "No se elige: un 0 en seguridad lo impide")],
    mistakes=[("Elegir la propuesta con más puntaje aunque tenga 0 en seguridad.", "La seguridad es una condición: sin ella la actividad no se hace.", "Antes de sumar, descarta lo que tenga 0 en seguridad."),
              ("Dar por revisada la lista sin mirar el espacio.", "Una verificación sin observar no previene accidentes.", "Revisa cada punto de la lista con los ojos y marca solo lo que viste.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la accesibilidad de una actividad?", "La posibilidad de que todas las personas participen con sus capacidades", "La cercanía del salón a la cocina", "El costo de los materiales", "La accesibilidad se refiere a que cada persona pueda participar."),
        ("=", "{F} ¿Cuántos puntos suma la propuesta A?", "2+2+2+2", "Se suman los cuatro puntajes de la propuesta A.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la propuesta B?", "1+0+1+2", "Se suman los cuatro puntajes de la propuesta B.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma la propuesta C?", "1+1+0+1", "Se suman los cuatro puntajes de la propuesta C.", " puntos"),
        ("abc", "{F} ¿Cuál propuesta es la más conveniente?", "La propuesta A", "La propuesta B", "La propuesta C", "La propuesta A suma 8 puntos y no tiene 0 en seguridad."),
        ("abc", "{F} ¿Por qué la propuesta C no se elige aunque tiene 3 puntos?", "Porque tiene 0 en seguridad", "Porque tiene muy pocos intereses", "Porque se hace en el jardín", "Un 0 en seguridad es una condición que impide elegir la propuesta."),
        ("abc", "{F} ¿Qué falla de accesibilidad tiene la propuesta B?", "Las piezas pequeñas y las reglas complejas dificultan que algunos participen", "Que se hace en grupos de 4", "Que dura 45 minutos", "El puntaje 0 en accesibilidad se debe a que piezas y reglas dejan fuera a algunos residentes."),
        ("=", "{F} ¿Cuántos grupos de 4 se forman con 16 residentes en la propuesta B?", "16//4", "Se divide la cantidad de residentes entre los integrantes de cada grupo.", " grupos"),
        ("abc", "{F} Antes de realizar la propuesta A, la técnica ve que dos sillas del salón están flojas. ¿Qué corresponde?", "Retirarlas del uso y avisar a la enfermera antes de comenzar", "Usarlas igual, con cuidado", "Pedir a los residentes que no se apoyen mucho", "Una silla inestable es un riesgo; se retira y se avisa."),
        ("abc", "{F} La lista de verificación dice «aviso a la enfermera de residentes con reposo» y la técnica no lo ha recibido. ¿Qué hace?", "Consulta a la enfermera antes de comenzar y espera su respuesta", "Supone que no hay residentes con reposo", "Pregunta a los residentes quién tiene reposo", "Los reposos los indica la enfermera; se consulta antes de comenzar."),
        ("=", "{F} Si la lista de verificación tiene 6 puntos y se cumplieron 5, ¿cuántos faltan?", "6-5", "Se restan los puntos cumplidos del total de la lista.", " punto"),
        ("abc", "{F} Un compañero dice: «Si falta una verificación, lo importante es empezar y arreglar después». ¿Qué corresponde responder?", "Que se avisa a la enfermera y no se comienza hasta resolver los puntos de seguridad", "Que sí, porque el tiempo se acaba", "Que sí, mientras no pase nada", "Los puntos de la lista previenen accidentes y se resuelven antes."),
        ("abc", "{F} Se propone mezclar A y B: bingo con piezas pequeñas. ¿Qué corresponde?", "Evaluar la nueva propuesta con los mismos criterios antes de decidir", "Aceptarla de inmediato", "Rechazarla sin evaluar", "Toda propuesta nueva se compara con los criterios."),
    ],
    ctx=("abc", "{F} Al verificar la propuesta A, el técnico nota que 3 de los 6 puntos no se cumplen: faltan técnicos, el material tiene cartones rotos y no hay pausas previstas. Los residentes ya llegaron. ¿Qué hace?", "Avisa a la enfermera, explica con respeto a los residentes que habrá una espera y no comienza hasta resolver los puntos", "Comienza igual, porque ya llegaron", "Cancela la actividad sin avisar", "La seguridad se resuelve antes de comenzar, y se informa con respeto a quienes esperan."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cómo se elige entre varias propuestas?", "Se comparan con los mismos criterios y se suman los puntajes", "Se evita elegir por gusto personal."),
        ("¿Qué condición impide elegir una propuesta?", "Tener 0 en seguridad", "La seguridad es una condición, no un punto más."),
        ("¿Qué haces si falla un punto de la lista de verificación?", "Aviso a la enfermera antes de comenzar", "Se resuelve antes de realizar la actividad."),
    ],
    op=("Propuestas de ejemplo: «P1, canto en círculo, 30 minutos: intereses 2, accesibilidad 2, seguridad 2, socialización 2. P2, taller de cocina con horno, 60 minutos: intereses 2, accesibilidad 1, seguridad 0, socialización 2. P3, pintura con témpera, 45 minutos: intereses 1, accesibilidad 2, seguridad 2, socialización 1». "
        "Calcula los puntos de cada una; di cuál elegirías y por qué; y escribe tres puntos de verificación que revisarías antes de comenzar.",
        "P1: 8 puntos; P2: 5, pero con 0 en seguridad; P3: 6. Elegiría P1: tiene el mayor puntaje y no tiene 0 en seguridad. Verificación: espacio despejado, sillas estables y técnicos suficientes, además de las pausas y el aviso de residentes con reposo.",
        ["suma 8, 5 y 6", "descarta P2 por la seguridad", "elige P1 con razón", "nombra tres puntos de verificación"],
        ["hoja con tres sumas, una elección con razón y tres puntos de verificación"],
        ["elegir P2 por tener buenos intereses", "sumar mal", "olvidar la verificación"],
        "Pregunta: «¿tu elección explica el criterio de seguridad?». Si no, pídele agregar esa razón."),
    reinforce="Elige una actividad que conozcas, califícala de 0 a 2 en los cuatro criterios y suma el puntaje.",
    extend="Explica con un ejemplo inventado por qué una actividad muy divertida puede no ser apropiada para una persona mayor.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (residencia de ejemplo, inventada). En la «Residencia Los Aromos de Ejemplo» hay 30 residentes y las familias visitan los sábados y domingos de 15:00 a 18:00. La enfermera informa a las familias sobre el estado de salud y los cuidados; "
     "el técnico en enfermería puede contar cómo fue la rutina del día, las actividades y el ánimo que observó, sin entregar datos clínicos. Cada residente, si puede decidirlo, autoriza por escrito a quién y qué se informa; si no puede decidir, se informa a su representante. "
     "Todo contacto con una familia se anota en el cuaderno de comunicaciones: fecha, hora, quién habló, tema y quién informó.")
build(
    O2, 1, F,
    use="Aprenderé qué es el estado integral de una persona mayor, quién puede informar a las familias y qué reglas de confidencialidad y autorización se respetan.",
    prior=["Conozco los derechos de las personas mayores.", "Sé calcular horas y minutos.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería (mención Adulto Mayor), el estado integral de una persona es cómo está en conjunto: su cuerpo y salud, su ánimo y sus relaciones. Informar a la familia significa contarle cómo está su familiar de forma clara y respetuosa. La información clínica, como diagnósticos, exámenes o tratamientos, la entrega el profesional. El técnico informa sobre lo que observa en la rutina diaria, siguiendo los protocolos de la institución.",
        "Los datos de salud son confidenciales. La persona mayor decide a quién se informa y qué, si puede decidirlo; esa decisión se respeta aunque la familia insista. Si no puede decidir, se informa a su representante, según el protocolo. Cada contacto con una familia se registra en el cuaderno de comunicaciones, con hechos y sin opiniones.",
        "Si una familia pregunta por algo que corresponde al profesional, el técnico no responde por su cuenta: la deriva a la enfermera con amabilidad." + LIM,
    ],
    vocab=[("estado integral", "cómo está la persona en su cuerpo, su ánimo y sus relaciones"), ("información clínica", "diagnósticos, exámenes y tratamientos, que entrega el profesional"), ("autorización", "decisión escrita de la persona sobre a quién y qué se informa"), ("representante", "persona que decide por quien no puede hacerlo, según el protocolo"), ("cuaderno de comunicaciones", "registro de cada contacto con una familia"), ("derivar", "enviar una consulta al profesional que corresponde")],
    worked=[
        ("Qué informa el técnico", "Un hijo de ejemplo pregunta al técnico qué hizo su madre hoy. ¿Puede responder?", ["Contar la rutina y las actividades es parte de su rol.", "Sí, sin entregar datos clínicos."], "Sí: puede contar la rutina y las actividades, sin datos clínicos"),
        ("Calcular horas de visita", "En otra residencia de ejemplo, las visitas son de 14:00 a 17:30. ¿Cuántos minutos duran?", ["De 14:00 a 17:00 son 3 horas, es decir, 180 minutos.", "180 + 30 = 210."], "210 minutos")],
    mistakes=[("Contarle a una hija el resultado de un examen de su madre «porque es de confianza».", "Los resultados los entrega el profesional y la madre decide a quién se informa.", "Deriva la consulta a la enfermera."),
              ("Informar a otro familiar que la residente no autorizó, porque «insiste mucho».", "Se vulnera la decisión de la persona mayor sobre sus datos.", "Respeta su autorización y avisa a la enfermera si la familia insiste.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es el estado integral de una persona?", "Cómo está en su cuerpo, su ánimo y sus relaciones", "Solo la lista de sus medicamentos", "Su peso y su talla", "El estado integral es una mirada completa, no solo un dato."),
        ("abc", "{F} ¿Quién informa a las familias sobre el estado de salud y los cuidados?", "La enfermera", "El técnico en enfermería", "Un residente de confianza", "La ficha dice que la enfermera informa sobre salud y cuidados."),
        ("abc", "{F} ¿Qué puede contar el técnico a una familia?", "Cómo fue la rutina del día, las actividades y el ánimo observado", "Los resultados de los exámenes", "El diagnóstico de la persona", "La ficha limita al técnico a la rutina, las actividades y el ánimo, sin datos clínicos."),
        ("=", "{F} ¿Cuántos minutos duran las visitas de un día?", "(18-15)*60", "Se multiplican las horas de visita por 60 minutos.", " minutos"),
        ("=", "{F} ¿Cuántas horas de visita hay en un fin de semana completo?", "2*(18-15)", "Se multiplican los días de visita por las horas de cada día.", " horas"),
        ("abc", "{F} Un residente autoriza por escrito que solo se informe a su hija. Un hijo le pide detalles al técnico. ¿Qué hace?", "No entrega información y avisa a la enfermera, respetando la decisión del residente", "Le cuenta, porque también es hijo", "Le cuenta solo cosas poco importantes", "La persona decide a quién se informa; se respeta aunque la familia insista."),
        ("abc", "{F} Una residente no puede decidir por sí misma. ¿A quién se informa?", "A su representante, según el protocolo", "A cualquier persona que visite", "A nadie, nunca", "Si no puede decidir, se informa a su representante conforme al protocolo."),
        ("abc", "{F} Una nuera pregunta si su suegro tiene una enfermedad grave. ¿Qué corresponde?", "Derivar su consulta a la enfermera con amabilidad", "Decirle lo que se comenta en el equipo", "Decirle que no se preocupe", "La información clínica la entrega el profesional, y solo a quien corresponde."),
        ("abc", "{F} ¿Qué se anota en el cuaderno de comunicaciones?", "Fecha, hora, quién habló, tema y quién informó", "El diagnóstico de la persona", "La opinión del técnico sobre la familia", "La ficha indica los datos del contacto; no incluye datos clínicos ni opiniones."),
        ("=", "{F} Si cada contacto toma 10 minutos y se atiende de forma continua durante las 3 horas de visita de un día, ¿cuántos contactos caben?", "(18-15)*60//10", "Se calculan los minutos de la visita y se dividen entre la duración de cada contacto.", " contactos"),
        ("abc", "{F} Un familiar le pide al técnico que le avise por un mensaje de su celular personal cómo amaneció su madre cada día. ¿Qué corresponde?", "No dar información por canales personales y derivar la solicitud a la enfermera", "Aceptar, porque es más rápido para la familia", "Aceptar, pero solo si escribe sin el nombre de la residente", "Los datos se informan por los canales del establecimiento y según la autorización de la persona."),
        ("=", "{F} Si 30 residentes tienen una visita cada fin de semana y cada visita dura 10 minutos con la enfermera, ¿cuántos minutos necesita en total para atender todas las visitas?", "30*10", "Se multiplican los residentes por los minutos de cada visita.", " minutos"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿por qué se anota cada contacto con la familia?", "Para que el equipo sepa qué se informó, cuándo y quién lo hizo", "Para controlar cuántas visitas recibe cada residente", "Para elegir qué familias son más cooperadoras", "El registro da trazabilidad a la comunicación."),
    ],
    ctx=("abc", "{F} Una hija llega muy angustiada y le dice al técnico que no ha podido hablar con la enfermera en toda la semana. Su madre residente está bien según lo que observa el técnico. ¿Qué hace?", "La escucha con calma, le cuenta lo que observó de la rutina y le ofrece pedir una hora con la enfermera", "Le dice que todo está bien y que no se preocupe", "Le cuenta lo que cree que tiene su madre", "Se acoge su angustia, se informa lo que corresponde al técnico y se facilita el contacto con la enfermera."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿quién informa sobre diagnósticos y tratamientos?", "El profesional", "La información clínica corresponde al profesional."),
        ("¿Qué haces si la residente no autorizó que se informe a alguien?", "Respeto su decisión y aviso a la enfermera", "La persona decide sobre sus propios datos."),
        ("¿Qué registras después de hablar con una familia?", "Fecha, hora, quién habló, tema y quién informó", "El cuaderno deja trazabilidad de cada contacto."),
    ],
    op=("Caso de ejemplo: en el taller del sábado a las 16:30, el hijo de una residente le pregunta al técnico si su madre «está mejor de la presión». La residente tiene una autorización escrita para informar a ese hijo. El técnico sabe que la enfermera mide la presión. "
        "Escribe: qué puede contar el técnico y qué no; a quién derivarías la pregunta de la presión; qué frase respetuosa usarías; y qué anotarías en el cuaderno de comunicaciones.",
        "Puede contar cómo fue la rutina y el ánimo; no puede informar sobre la presión, que es información clínica. Deriva a la enfermera. Frase: «Su mamá participó hoy del taller y se veía contenta; lo que usted pregunta lo puede explicar la enfermera, ¿le pido una hora?». Registro: «Sábado 16:30, hijo de la residente consultó por la presión; se derivó a la enfermera».",
        ["distingue lo que puede y no puede contar", "deriva a la enfermera", "la frase es respetuosa y clara", "el registro no incluye datos clínicos"],
        ["hoja con lo que informa, lo que deriva, una frase y un registro"],
        ["informar la presión", "no respetar la autorización", "registrar datos clínicos"],
        "Pregunta: «¿tu frase explica por qué no cuentas sobre la presión sin parecer descortés?». Si no, pídele reescribirla."),
    reinforce="Escribe tres cosas que puede contar el técnico a una familia y tres que debe derivar a la enfermera.",
    extend="Explica con un ejemplo inventado por qué una persona mayor puede decidir que no se informe a algún familiar.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (frases de ejemplo para informar a una familia). Frase 1: «Hoy participó del taller de música y almorzó acompañada». Frase 2: «Tiene una infección grave». Frase 3: «No se preocupe, seguro se mejora pronto». "
     "Frase 4: «La enfermera le explicará cómo está; ¿quiere que le pida una hora?». Frase 5: «Está depre». Frase 6: «Hoy durmió la siesta y pidió escuchar música». "
     "Elementos de la comunicación efectiva: escucha activa, mensaje claro y breve, empatía, lenguaje no verbal respetuoso y verificar que la otra persona comprendió. Documentos: hoja de autorización de información y cuaderno de comunicaciones.")
build(
    O2, 2, F,
    use="Aprenderé qué es la comunicación efectiva, qué frases son apropiadas para el técnico y cuáles no, y para qué sirven la hoja de autorización y el cuaderno de comunicaciones.",
    prior=["Conozco quién informa a las familias y qué.", "Sé leer una lista de frases.", "Sé contar elementos."],
    explain=[
        "La comunicación efectiva es la que logra que la otra persona entienda el mensaje y se sienta escuchada. Sus elementos son la escucha activa (mirar, no interrumpir y repetir lo que se entendió), el mensaje claro y breve, la empatía (reconocer lo que la otra persona siente), un lenguaje no verbal respetuoso (tono, gestos, postura) y verificar que se comprendió, por ejemplo preguntando «¿le quedó claro?».",
        "Una frase apropiada para el técnico describe un hecho observado, como «hoy participó del taller». Una frase no apropiada da un diagnóstico («tiene una infección»), promete algo que no se puede asegurar («seguro se mejora») o pone una etiqueta («está depre»). Cuando la pregunta corresponde al profesional, la frase deriva con amabilidad. La hoja de autorización dice a quién se informa y el cuaderno registra cada contacto.",
        "El tono y los gestos también comunican: mirar con atención y hablar sin apuro muestran respeto." + LIM,
    ],
    vocab=[("comunicación efectiva", "comunicación en que la otra persona entiende y se siente escuchada"), ("escucha activa", "mirar, no interrumpir y repetir lo que se entendió"), ("empatía", "reconocer lo que la otra persona siente"), ("lenguaje no verbal", "tono, gestos y postura al comunicar"), ("hoja de autorización", "documento que dice a quién y qué se informa"), ("etiqueta", "palabra que resume a una persona sin describir hechos")],
    worked=[
        ("Clasificar una frase", "Un técnico de ejemplo dice: «Ayer almorzó toda su comida y salió a caminar al jardín». ¿Es un hecho observado?", ["Describe lo que se vio sin interpretar.", "Es un hecho observado y apropiado para informar."], "Sí, es un hecho observado"),
        ("Contar elementos", "La ficha menciona cinco elementos de la comunicación efectiva. Si un técnico cumple tres, ¿cuántos le faltan?", ["La ficha menciona cinco elementos en total.", "Si cumple tres, le faltan 5 − 3 = 2."], "2 elementos")],
    mistakes=[("Decir «no se preocupe, seguro se mejora» para tranquilizar a una familia.", "Promete algo que el técnico no puede asegurar y puede generar falsas expectativas.", "Reconoce su preocupación y deriva a la enfermera, que puede explicar."),
              ("Hablar de «la señora de la 5» en voz alta en el pasillo.", "Otras personas pueden oír datos de la residente.", "Habla en un lugar reservado y por su nombre, con respeto.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es la escucha activa?", "Mirar, no interrumpir y repetir lo que se entendió", "Hablar sin parar para dar toda la información", "Escuchar mientras se hace otra tarea", "La escucha activa muestra atención y permite comprobar lo entendido."),
        ("abc", "{F} ¿Cuál de estas frases es un hecho observado que el técnico puede informar?", "La frase 1: «Hoy participó del taller de música y almorzó acompañada»", "La frase 2: «Tiene una infección grave»", "La frase 5: «Está depre»", "La frase 1 describe hechos; la 2 es un diagnóstico y la 5 una etiqueta."),
        ("abc", "{F} ¿Por qué la frase 2 no es apropiada para el técnico?", "Porque da un diagnóstico, que corresponde al profesional", "Porque es muy corta", "Porque es muy positiva", "El diagnóstico lo comunica el profesional."),
        ("abc", "{F} ¿Por qué la frase 3 no es apropiada?", "Porque promete algo que no se puede asegurar", "Porque describe un hecho", "Porque es una derivación", "«Seguro se mejora» es una promesa que el técnico no puede garantizar."),
        ("abc", "{F} ¿Qué hace la frase 4?", "Deriva a la enfermera con amabilidad", "Da un diagnóstico", "Pone una etiqueta", "La frase ofrece pedir una hora con la enfermera, que es quien puede explicar."),
        ("abc", "{F} ¿Qué frase pone una etiqueta a la persona en vez de describir hechos?", "La frase 5: «Está depre»", "La frase 6: «Hoy durmió la siesta y pidió escuchar música»", "La frase 4: «La enfermera le explicará cómo está»", "«Está depre» resume a la persona con una palabra; la 6 y la 4 describen un hecho o derivan."),
        ("=", "{F} Las frases 2, 3 y 5 no son apropiadas para el técnico. ¿Cuántas de las seis sí lo son?", "6-3", "Se restan de las seis frases las tres que no son apropiadas.", " frases"),
        ("abc", "{F} ¿Cuántos elementos de la comunicación efectiva menciona la ficha?", "Cinco", "Tres", "Siete", "La ficha enumera escucha activa, mensaje claro, empatía, lenguaje no verbal y verificar la comprensión."),
        ("abc", "{F} Un familiar pregunta algo y el técnico responde sin mirarlo, mientras escribe. ¿Qué elemento descuida?", "El lenguaje no verbal y la escucha activa", "El mensaje breve", "La hoja de autorización", "No mirar ni dar atención es no demostrar escucha."),
        ("abc", "{F} Después de explicar la rutina, el técnico pregunta «¿le quedó claro?». ¿Qué elemento aplica?", "Verificar que la otra persona comprendió", "Poner una etiqueta", "Dar un diagnóstico", "Preguntar si quedó claro es una forma de verificar la comprensión."),
        ("abc", "{F} Un técnico dice: «Entiendo que usted esté preocupada; es normal». ¿Qué elemento aplica?", "La empatía", "El diagnóstico", "La promesa", "Reconocer lo que la otra persona siente es empatía."),
        ("abc", "{F} Antes de informar a una nieta, el técnico revisa la hoja de autorización. ¿Para qué?", "Para saber a quién y qué puede informar", "Para decidir si la nieta merece información", "Para anotar su nombre en el cuaderno", "La hoja dice a quién se informa y qué; el técnico debe respetarla."),
        ("abc", "{F} Una familia pregunta cómo está su madre y el técnico responde durante 10 minutos con muchas palabras técnicas que nadie entiende. ¿Qué elemento descuida?", "El mensaje claro y breve", "La hoja de autorización", "El cuaderno de comunicaciones", "Un mensaje largo y con palabras difíciles no logra que la otra persona entienda."),
    ],
    ctx=("abc", "{F} Una nieta de ejemplo se acerca al técnico y le pregunta, en el pasillo, cómo ha estado su abuela. El técnico sabe que la residente autorizó a informar a su nieta sobre la rutina. ¿Qué hace?", "La invita a un lugar reservado, cuenta cómo fue la rutina y el ánimo observado, y verifica que comprendió", "Responde en el pasillo, porque ahí está", "Le cuenta también el diagnóstico, porque la autorizaron", "Se informa en un lugar reservado y solo lo que corresponde al técnico."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué es la empatía?", "Reconocer lo que la otra persona siente", "Ayuda a que la otra persona se sienta escuchada."),
        ("¿Qué frase es apropiada para informar a una familia?", "Una que describe un hecho observado", "Los hechos observados no interpretan ni prometen."),
        ("¿Qué haces con una pregunta clínica de la familia?", "La derivo a la enfermera con amabilidad", "La información clínica la entrega el profesional."),
    ],
    op=("Frases de ejemplo: «(a) Hoy almorzó y salió a tomar el sol; (b) Tiene el azúcar alta; (c) Está de mal humor siempre; (d) Su hijo puede pedir una hora con la enfermera para saber más; (e) Se pondrá bien, se lo aseguro». "
        "Clasifica cada frase como apropiada o no para el técnico y explica por qué; reescribe las que no lo sean; y escribe los cinco elementos de la comunicación efectiva.",
        "(a) apropiada: hecho observado. (b) no: es información clínica; reescribir: «La enfermera le puede explicar cómo está; ¿le pido una hora?». (c) no: etiqueta; reescribir: «Hoy estuvo más callado y prefirió estar en su pieza». (d) apropiada: deriva. (e) no: promesa; reescribir: «Entiendo su preocupación; la enfermera le explicará». Elementos: escucha activa, mensaje claro, empatía, lenguaje no verbal y verificar la comprensión.",
        ["clasifica las cinco frases", "reescribe las tres no apropiadas", "nombra los cinco elementos", "no incluye datos clínicos"],
        ["hoja con una clasificación, tres reescrituras y cinco elementos"],
        ["mantener «tiene el azúcar alta»", "aceptar una promesa", "olvidar un elemento"],
        "Pregunta: «¿tu reescritura de (b) describe un hecho o deriva?». Debe derivar."),
    reinforce="Escribe una frase apropiada y una no apropiada que el técnico podría decir a una familia sobre cómo comió su familiar.",
    extend="Explica con un ejemplo inventado por qué una promesa dicha para tranquilizar a una familia puede generar un problema después.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (casos y pauta de comunicación, de ejemplo). Pauta de cinco criterios: (1) saluda y escucha con respeto; (2) informa solo lo que corresponde a su rol; (3) respeta la autorización de la persona mayor; (4) usa un lenguaje claro y sin etiquetas; (5) registra el contacto y avisa a la enfermera cuando corresponde. "
     "Caso A: una hija pregunta si su madre tuvo una caída hoy; el técnico la escucha, le dice «hubo un incidente y la enfermera le dará el detalle», y lo registra y avisa a la enfermera; cumple los 5. "
     "Caso B: un nieto pide ver la ficha clínica; el técnico saluda con respeto pero se la muestra; cumple solo el criterio 1. "
     "Caso C: un hijo molesto reclama porque su padre no quiso comer; el técnico lo escucha y le explica con palabras claras lo que observó, pero no registra el contacto ni avisa a la enfermera; cumple los criterios 1, 2, 3 y 4. "
     "Caso D: una familia pide que no se le diga a la residente su diagnóstico; el técnico escucha, deriva a la enfermera y registra el contacto, pero comenta que «su mamá es una persona difícil»; cumple los criterios 1, 2, 3 y 5.")
build(
    O2, 3, F,
    use="Aprenderé a analizar un caso de comunicación con una familia usando una pauta, a reconocer lo que se hizo bien y mal y a decidir qué se registra y a quién se avisa.",
    prior=["Conozco la comunicación efectiva.", "Conozco la autorización y la confidencialidad.", "Sé calcular porcentajes de números enteros."],
    explain=[
        "Para analizar un caso de comunicación con una familia se lee primero lo que ocurrió y luego se revisa con una pauta de criterios. Los criterios son saludar y escuchar con respeto, informar solo lo que corresponde al rol, respetar la autorización de la persona mayor, usar un lenguaje claro y sin etiquetas, y registrar el contacto avisando a la enfermera cuando corresponde. Se marca cuáles se cumplieron y cuáles no.",
        "Cuando una familia está molesta o angustiada, el técnico la escucha sin discutir ni defenderse, reconoce lo que siente y le explica con claridad qué puede informar y a quién derivar. No se miente ni se esconden hechos: si ocurrió un incidente, quien informa los detalles es la enfermera. Si una familia pide algo que vulnera los derechos de la persona mayor, como ocultarle su diagnóstico, no se resuelve en el pasillo: se deriva a la enfermera.",
        "El análisis sirve para mejorar la comunicación del equipo, no para culpar." + LIM,
    ],
    vocab=[("pauta de criterios", "lista de conductas esperadas que se revisan una por una"), ("incidente", "hecho inesperado que afectó o pudo afectar a una persona"), ("rol", "función que le corresponde a cada persona del equipo"), ("derivar", "enviar la consulta al profesional que corresponde"), ("familia angustiada", "familia que siente preocupación o temor por su familiar")],
    worked=[
        ("Aplicar un criterio", "Un técnico de ejemplo le dice a una familia que su madre «es una mañosa». ¿Qué criterio incumple?", ["La frase es una etiqueta.", "Incumple el criterio 4: lenguaje claro y sin etiquetas."], "El criterio 4"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 4 de los 5 criterios. ¿Qué porcentaje es?", ["4 × 100 = 400.", "400 ÷ 5 = 80."], "80 %")],
    mistakes=[("Defenderse ante una familia molesta diciendo «nosotros hacemos lo posible».", "La familia no se siente escuchada y aumenta el conflicto.", "Escucha, reconoce lo que siente y ofrece derivar a la enfermera."),
              ("No registrar un contacto «porque fue solo una conversación corta».", "Sin registro, el equipo no sabe qué se informó ni qué quedó pendiente.", "Anota fecha, hora, tema y quién informó, aunque sea breve.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué debe hacer el técnico con una familia molesta?", "Escucharla sin discutir, reconocer lo que siente y derivar lo que no le corresponde", "Defenderse y explicarle que el equipo hace lo posible", "Evitarla hasta que se calme", "Escuchar con respeto reduce el conflicto y la derivación corresponde a quien tiene la información."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso B?", "El criterio 2: informar solo lo que corresponde a su rol", "El criterio 1: saludar con respeto", "Ninguno, porque saludó", "Mostrar la ficha clínica excede el rol del técnico."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso C?", "El criterio 5: registrar el contacto y avisar a la enfermera", "El criterio 1: escuchar con respeto", "El criterio 4: lenguaje claro", "El caso C no registró el contacto ni avisó a la enfermera."),
        ("abc", "{F} ¿Qué caso cumple todos los criterios?", "El caso A", "El caso B", "El caso C", "El caso A cumple los cinco: escuchó, informó lo que correspondía, respetó la autorización, habló claro y registró."),
        ("=", "{F} ¿Cuántos criterios cumplen en total los casos A, B, C y D?", "5+1+4+4", "Se suman los criterios cumplidos por cada caso.", " criterios"),
        ("=", "{F} ¿Qué porcentaje de los criterios cumplen en total los cuatro casos?", "(5+1+4+4)*100//(4*5)", "Se divide el total de criterios cumplidos entre los evaluados (4 casos × 5) y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos criterios incumplen en total los cuatro casos?", "(5-5)+(5-1)+(5-4)+(5-4)", "Se resta de los 5 criterios de cada caso la cantidad que cumple y se suman las fallas.", " criterios"),
        ("abc", "{F} En el caso C, ¿qué debió hacer el técnico además de escuchar y explicar?", "Registrar el contacto y avisar a la enfermera", "Pedir que el hijo se calme y se retire", "Mostrar la ficha de su padre", "El criterio 5 pide registrar y avisar cuando corresponde."),
        ("abc", "{F} En el caso D, la familia pide que no se le diga el diagnóstico a la residente. ¿Qué hace bien el técnico?", "Deriva a la enfermera y registra el contacto", "Promete cumplir el pedido", "Le cuenta el diagnóstico a la residente", "No puede decidir sobre la información de la residente: la deriva a quien corresponde y deja registro."),
        ("abc", "{F} El técnico del caso B dice: «Como es el nieto, tenía derecho a ver la ficha». ¿Qué corresponde responder?", "Que la ficha es confidencial y el acceso lo autoriza la residente y lo gestiona la enfermera", "Que sí, porque es familia", "Que sí, si lo pide con buena educación", "El derecho a la información lo define la persona mayor y los protocolos, no el parentesco."),
        ("abc", "{F} Un compañero quiere corregir al técnico del caso B diciéndole «eres un irresponsable». ¿Qué corresponde?", "Describir lo ocurrido con hechos y proponer la mejora, sin juzgar", "Decirle lo mismo, para que aprenda", "No decir nada nunca", "Una crítica con hechos permite aprender sin dañar."),
        ("=", "{F} Si el técnico del caso C hubiera registrado el contacto y avisado a la enfermera, ¿cuántos criterios habría cumplido?", "4+1", "Se suma el criterio 5 a los cuatro que ya cumplía.", " criterios"),
        ("abc", "{F} La enfermera pide una frase para empezar a conversar con una familia molesta. ¿Cuál es adecuada?", "«Entiendo que esté preocupado; cuénteme qué le inquieta»", "«Cálmese, nosotros hacemos lo posible»", "«Eso no es asunto mío»", "Reconocer lo que la persona siente y escucharla baja el conflicto; defenderse o evadir lo aumenta."),
    ],
    ctx=("abc", "{F} Un hijo exige al técnico que le muestre el cuaderno de comunicaciones de los últimos días de su madre. La residente no ha autorizado que se comparta. ¿Qué hace?", "Le explica con respeto que no puede mostrarlo y lo deriva a la enfermera", "Se lo muestra, porque es su hijo", "Le muestra solo las anotaciones que parecen inofensivas", "El cuaderno contiene información que la residente decide compartir; se deriva a la enfermera."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces si una familia exige ver la ficha?", "Le explico con respeto y la derivo a la enfermera", "El acceso a la ficha lo gestiona la enfermera."),
        ("¿Qué criterio pide registrar el contacto?", "El criterio 5", "El contacto debe quedar registrado y avisado cuando corresponda."),
        ("¿Se oculta un incidente a la familia?", "No, se deriva el detalle a la enfermera", "No se miente ni se esconden hechos."),
    ],
    op=("Casos de ejemplo: «A: una hija pregunta por el estado de ánimo de su padre; el técnico la saluda, le cuenta que hoy participó del taller, y registra el contacto. B: un sobrino pregunta cuánto tiempo le queda a su tío; el técnico le responde que «seguro unos meses». C: una nieta pide que se le diga a su abuela que se mudará de residencia; el técnico dice que «se le avisará cuando llegue el día» sin consultar a nadie». "
        "Usa la pauta de la ficha. Escribe: qué criterios incumple cada caso; cuántos criterios cumplen en total si cada caso se evalúa con 5; y cómo corregirías B y C.",
        "A cumple los 5 criterios. B incumple 2 (entrega información clínica, un pronóstico) y 5 (no registra ni avisa); cumple 3. C incumple 2 y 3 (no consulta a la enfermera ni a la residente) y 5; cumple 1 y 4. Cumplen: A 5, B 3 (1, 3 y 4), C 2 = 10 de 15. Corrección: B, no dar pronósticos; derivar a la enfermera. C, derivar la petición a la enfermera y respetar la decisión de la residente.",
        ["identifica los criterios incumplidos de B y C", "calcula 10 de 15", "propone correcciones", "deriva a la enfermera"],
        ["hoja con criterios incumplidos, un total y correcciones"],
        ["dar un pronóstico", "no derivar la petición de la nieta", "sumar mal"],
        "Pregunta: «¿quién decide si se avisa a la abuela de un cambio de residencia?». Debe responder que la residente con el equipo, no la nieta ni el técnico."),
    reinforce="Escribe una frase respetuosa para derivar a la enfermera una consulta clínica de la familia.",
    extend="Explica con un ejemplo inventado por qué una familia puede sentirse mejor al ser escuchada, aunque el técnico derive su pregunta.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (comunicación con familias, planilla de ejemplo). Fin de semana: el sábado hay 18 horas de atención (cada «hora» es una cita de 10 minutos con la enfermera) y el domingo, otras 18; 40 familias pidieron una hora. "
     "Llamadas telefónicas de familias registradas en la semana: lunes 12, martes 9, miércoles 15, jueves 6 y viernes 8; cada llamada dura 5 minutos. "
     "Residentes: 30, de los cuales 24 tienen la hoja de autorización firmada al día. Regla: los 6 residentes sin autorización al día se informan a la enfermera para que se regularice; mientras tanto no se entrega información a terceros.")
build(
    O2, 4, F,
    use="Aprenderé a organizar con cuentas simples la atención a las familias: horas disponibles, llamadas, porcentaje de autorizaciones al día y qué se informa a la enfermera.",
    prior=["Sé sumar, dividir y calcular porcentajes de números enteros.", "Conozco la hoja de autorización.", "Sé leer una planilla."],
    explain=[
        "Con una planilla de comunicación con familias se hacen cuentas que ayudan a organizar el trabajo. Las horas disponibles se calculan sumando las de cada día. Las que faltan son la diferencia entre las pedidas y las disponibles. El promedio de llamadas se calcula sumando las llamadas de los días y dividiéndolas por la cantidad de días. El tiempo total se calcula multiplicando las llamadas por los minutos de cada una.",
        "También se revisa el cumplimiento de las autorizaciones: el porcentaje de residentes con la hoja al día es los que la tienen multiplicados por 100 y divididos por el total de residentes. Cuando falta una autorización, se informa a la enfermera para que se regularice y, mientras tanto, no se entrega información a terceros. Con los datos se propone a la enfermera una organización razonable, por ejemplo más horas o un horario especial.",
        "Los datos son inventados y el técnico solo propone; la organización la decide la enfermera." + LIM,
    ],
    vocab=[("horas disponibles", "cantidad de «horas» o citas de 10 minutos con la enfermera que se pueden ofrecer"), ("llamada registrada", "contacto telefónico anotado en el cuaderno de comunicaciones"), ("autorización al día", "hoja firmada y vigente sobre a quién se informa"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("regularizar", "completar o renovar un documento que falta")],
    worked=[
        ("Horas que faltan", "En otra residencia de ejemplo hay 24 horas de atención disponibles y 30 familias pidieron una. ¿Cuántas familias quedan sin hora?", ["Se restan las horas disponibles de las pedidas.", "30 − 24 = 6."], "6 familias"),
        ("Porcentaje de autorizaciones", "En otro servicio de ejemplo, 18 de 20 residentes tienen la hoja al día. ¿Qué porcentaje es?", ["18 × 100 = 1.800.", "1.800 ÷ 20 = 90."], "90 %")],
    mistakes=[("Entregar información a un familiar de un residente sin autorización al día porque «seguro estaría de acuerdo».", "No se puede suponer su decisión; se vulnera su derecho a decidir.", "No entregues información y avisa a la enfermera para regularizar."),
              ("Calcular el promedio de llamadas dividiendo entre las familias.", "El promedio diario se calcula entre los días de registro.", "Divide el total de llamadas entre los días registrados.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es una autorización al día?", "Una hoja firmada y vigente que dice a quién y qué se informa", "Un permiso para entrar a la residencia", "Una lista de familias que visitan", "La autorización al día permite saber a quién se puede informar."),
        ("=", "{F} ¿Cuántas horas de atención hay disponibles en el fin de semana?", "18+18", "Se suman las horas del sábado y del domingo.", " horas"),
        ("=", "{F} ¿Cuántas familias quedan sin hora?", "40-(18+18)", "Se restan las horas disponibles de las familias que la pidieron.", " familias"),
        ("=", "{F} ¿Cuántas llamadas se registraron en la semana?", "12+9+15+6+8", "Se suman las llamadas de cada día.", " llamadas"),
        ("=", "{F} ¿Cuál fue el promedio diario de llamadas?", "(12+9+15+6+8)//5", "Se divide el total de llamadas entre los 5 días.", " llamadas"),
        ("=", "{F} ¿Cuántos minutos se dedicaron a llamadas en la semana?", "(12+9+15+6+8)*5", "Se multiplican las llamadas totales por los minutos de cada una.", " minutos"),
        ("=", "{F} ¿Qué porcentaje de los residentes tiene la hoja de autorización al día?", "24*100//30", "Se multiplican los residentes con hoja al día por 100 y se dividen entre el total.", " %"),
        ("abc", "{F} ¿Qué día se registraron más llamadas?", "El miércoles", "El lunes", "El viernes", "El miércoles tuvo 15 llamadas, más que los otros días."),
        ("abc", "{F} Una familia de un residente sin autorización al día pide información por teléfono. ¿Qué corresponde?", "No entregar información y avisar a la enfermera para regularizar la autorización", "Entregar información básica, porque es familia", "Pedirle que firme una hoja por teléfono", "Sin autorización vigente no se entrega información a terceros."),
        ("abc", "{F} La técnica propone a la enfermera agregar horas especiales para atender a las familias que quedaron sin hora. ¿Qué corresponde?", "Dejar la decisión a la enfermera, que organiza el horario", "Citar por su cuenta a las familias fuera del horario", "Avisar a las familias que no habrá hora", "El técnico propone; la enfermera organiza."),
        ("=", "{F} Si se agregaran 4 horas especiales de atención, ¿cuántas familias quedarían sin hora?", "40-(18+18+4)", "Se restan las horas totales, con las especiales, de las familias que pidieron.", " familias"),
        ("abc", "{F} Un compañero dice: «Con 80 % de autorizaciones al día ya está bien». ¿Qué corresponde responder?", "Que los 6 residentes sin autorización necesitan regularización para proteger su derecho a decidir", "Que tiene razón, porque es un buen porcentaje", "Que solo importa el 100 % del mes siguiente", "Cada persona tiene derecho a decidir sobre su información; no basta con un buen promedio."),
        ("abc", "{F} Una llamada dura más de lo previsto y la técnica no alcanza a registrarla. ¿Qué hace?", "Registra con la hora real y deja constancia de que se alargó", "No la registra, porque ya pasó", "Registra una llamada más corta", "El registro debe ser fiel a lo ocurrido."),
    ],
    ctx=("abc", "{F} La técnica nota que, según la planilla, hay 6 residentes sin autorización al día, y una de las visitas de hoy es de un hijo de uno de ellos. ¿Qué hace?", "Avisa a la enfermera antes de entregar información y deriva al hijo a ella", "Informa al hijo y regulariza después", "Pide al residente que firme apurado frente al hijo", "Se informa a la enfermera primero; no se entrega información sin autorización al día."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿cómo calculas el promedio diario de llamadas?", "Total de llamadas ÷ cantidad de días", "Resume varios días en un valor."),
        ("¿Qué haces si falta la autorización de un residente?", "No entrego información y aviso a la enfermera", "Se regulariza antes de informar a terceros."),
        ("¿Quién decide la organización de las horas de atención?", "La enfermera", "El técnico propone y ella decide."),
    ],
    op=("Planilla de ejemplo: «Sábado y domingo: 12 horas de atención cada día; 30 familias pidieron hora. Llamadas de una semana: 8, 10, 6, 12 y 9, de 5 minutos cada una. 20 residentes en total y 16 con autorización al día». "
        "Calcula: cuántas horas hay y cuántas familias quedan sin hora; el total de llamadas, el promedio diario y los minutos usados; el porcentaje de autorizaciones al día. Escribe qué informarías a la enfermera.",
        "Horas: 12 + 12 = 24; sin hora: 30 − 24 = 6. Llamadas: 8+10+6+12+9 = 45; promedio: 45 ÷ 5 = 9; minutos: 45 × 5 = 225. Autorizaciones: 16 × 100 ÷ 20 = 80 %. Informaría a la enfermera que 6 familias quedan sin hora y que 4 residentes necesitan regularizar su autorización.",
        ["calcula 24 horas y 6 familias", "calcula 45, 9 y 225", "calcula 80 %", "informa a la enfermera"],
        ["hoja con cuatro grupos de cálculos y una frase de informe"],
        ["dividir mal el promedio", "olvidar los minutos de cada llamada", "entregar información sin autorización"],
        "Pregunta: «¿cuántos residentes necesitan regularizar la autorización?». Debe responder 4, que es 20 − 16."),
    reinforce="Con 10, 12 y 8 llamadas en tres días, calcula el promedio diario y los minutos totales si cada una dura 4 minutos.",
    extend="Explica con un ejemplo inventado por qué una autorización firmada protege los derechos de una persona mayor.",
)

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (residencia de ejemplo, inventada). En la «Residencia Los Aromos de Ejemplo» viven 30 personas y se sirven cuatro comidas al día: desayuno, almuerzo, once y cena. Cuatro técnicos apoyan el servicio. "
     "El régimen de cada residente está escrito en su ficha por la nutricionista o el médico; el personal de cocina prepara las bandejas con una etiqueta con el nombre y el régimen; el técnico presenta y sirve según la indicación, apoya la autonomía de cada persona y registra cuánto comió. "
     "Reglas: higiene de manos antes de servir; revisar que la etiqueta coincida con la persona; respetar preferencias y ritmo; si alguien tose con fuerza o no puede respirar con normalidad al comer, avisar de inmediato a la enfermera y a emergencias.")
build(
    O3, 1, F,
    use="Aprenderé quién define el régimen de una persona mayor, qué hace el técnico al servir los alimentos, qué principios se respetan y qué hacer ante un riesgo mientras come.",
    prior=["Conozco los derechos de las personas mayores.", "Sé multiplicar y dividir números enteros.", "Sé leer una ficha."],
    explain=[
        "En Atención de Enfermería (mención Adulto Mayor), alimentar bien a una persona mayor significa cuidar su nutrición, su autonomía y su dignidad. El régimen, que es la forma de alimentación indicada para cada persona, lo define un profesional, como la nutricionista o el médico, y está escrito en su ficha. El técnico no cambia el régimen por su cuenta: presenta y sirve lo que corresponde, apoya a la persona para que coma lo más autónomamente posible y registra cuánto comió.",
        "Los principios son: respetar las preferencias y los tiempos de cada persona, cuidar la higiene de manos y de los alimentos, comprobar que la bandeja corresponde a la persona y mantener una postura cómoda y segura, también para el propio técnico, lo que se llama ergonomía. Los riesgos son servir un régimen equivocado, apurar a la persona o no notar una dificultad para tragar.",
        "Si una persona se atraganta, tose con fuerza o no puede respirar con normalidad, el técnico no actúa por cuenta propia: avisa de inmediato a la enfermera y a emergencias." + LIM,
    ],
    vocab=[("régimen", "forma de alimentación indicada por un profesional para cada persona"), ("nutricionista", "profesional que define la alimentación según las necesidades de la persona"), ("etiqueta de bandeja", "rótulo con el nombre de la persona y su régimen"), ("autonomía en la alimentación", "capacidad de comer por sí misma lo que puede"), ("ergonomía", "postura y organización que cuidan el cuerpo de quien trabaja"), ("registro de ingesta", "anotación de cuánto comió y bebió la persona")],
    worked=[
        ("Quién cambia un régimen", "Un técnico de ejemplo cree que un residente «ya puede comer de todo» y quiere servirle la bandeja de otro. ¿Qué corresponde?", ["El régimen lo define un profesional.", "El técnico propone el cambio a la enfermera y sirve lo que dice la ficha."], "Servir lo que indica la ficha y proponer el cambio a la enfermera"),
        ("Bandejas del día", "En otra residencia de ejemplo viven 20 personas y se sirven 4 comidas al día. ¿Cuántas bandejas se sirven en el día?", ["Se multiplican las personas por las comidas.", "20 × 4 = 80."], "80 bandejas")],
    mistakes=[("Cambiar la bandeja de un residente por otra «porque tiene más variedad».", "El régimen está indicado según su salud; un cambio puede perjudicarlo.", "Sirve la bandeja con su etiqueta y avisa si la persona prefiere otra cosa."),
              ("Darle de comer más rápido a quien come lento para terminar el turno.", "Apurar aumenta el riesgo de atragantamiento y quita autonomía.", "Respeta su ritmo y avisa a la enfermera si falta tiempo.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es el régimen de una persona?", "La forma de alimentación indicada por un profesional para ella", "La hora en que prefiere comer", "El menú de toda la residencia", "El régimen se define para cada persona según su salud y sus necesidades."),
        ("abc", "{F} ¿Quién define el régimen de cada residente?", "La nutricionista o el médico", "El técnico que sirve", "Los familiares", "La ficha dice que el régimen lo escribe la nutricionista o el médico."),
        ("abc", "{F} ¿Qué hace el técnico antes de servir una bandeja?", "Revisa que la etiqueta coincida con la persona y se higieniza las manos", "Cambia el contenido si la persona lo pide", "Prueba la comida de cada bandeja", "Las reglas piden higiene de manos y revisar la etiqueta."),
        ("=", "{F} ¿Cuántas bandejas se sirven en la residencia en un día?", "30*4", "Se multiplican los residentes por las comidas diarias.", " bandejas"),
        ("=", "{F} Si las bandejas del día se reparten por igual entre los 4 técnicos, ¿cuántas sirve cada uno?", "30*4//4", "Se dividen las bandejas del día entre los técnicos.", " bandejas"),
        ("=", "{F} Si el servicio de una comida demora 45 minutos y se hacen 4 comidas, ¿cuántas horas al día dedica el equipo al servicio de comidas?", "45*4//60", "Se multiplican los minutos de cada comida por las comidas y se pasan a horas.", " horas"),
        ("abc", "{F} Un residente dice que hoy no quiere el pescado de su bandeja y prefiere otra cosa. ¿Qué hace el técnico?", "Respeta su decisión, registra lo que comió y avisa a la enfermera si es necesario ajustar", "Le obliga a comerlo, porque es su régimen", "Le cambia la bandeja por la de otro residente", "Se respeta la preferencia dentro de lo posible y se informa para que el profesional ajuste."),
        ("abc", "{F} Un residente tose con fuerza mientras come y le cuesta respirar. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias, y no le da nada más", "Le da agua para que pase el bocado", "Le golpea la espalda por cuenta propia", "Ante un atragantamiento no se actúa por cuenta propia: se avisa de inmediato."),
        ("abc", "{F} Una compañera nota que la etiqueta de la bandeja dice «Pedro» y debía servirse a «Pablo». ¿Qué hace?", "Detiene el servicio de esa bandeja y consulta a la enfermera", "La sirve igual, porque los nombres se parecen", "Cambia la etiqueta con un lápiz", "Un error de identificación puede ser grave; se verifica antes de servir."),
        ("abc", "{F} Un técnico se agacha con la espalda curva toda la comida para ayudar a un residente. ¿Qué observación corresponde?", "Aplicar la ergonomía: cuidar su postura y avisar si necesita otro apoyo", "No importa, porque el residente es lo primero", "Que lo haga más rápido", "La postura del técnico también se cuida; la técnica la enseña un instructor."),
        ("=", "{F} Si cada técnico puede atender como máximo a 7 residentes por comida, ¿cuántos residentes quedarían sin atención con los 4 técnicos?", "30-4*7", "Se restan los residentes que pueden atender los técnicos de los 30 residentes.", " residentes"),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿por qué el técnico registra cuánto comió cada persona?", "Para que la enfermera y la nutricionista puedan evaluar si es necesario ajustar", "Para decidir si la persona merece el postre", "Para avisar a la familia cuánto gasta la residencia", "El registro permite detectar a tiempo si una persona come menos de lo habitual."),
        ("abc", "{F} Un compañero dice: «Si el residente se demora, le damos de comer nosotros para terminar antes». ¿Qué corresponde responder?", "Que se respeta su ritmo y autonomía, y si falta tiempo se avisa a la enfermera", "Que sí, porque el turno es limitado", "Que sí, mientras lo haga con cariño", "Apurar quita autonomía y aumenta el riesgo; se avisa la falta de tiempo."),
    ],
    ctx=("abc", "{F} Durante la cena, un residente deja casi toda la comida y dice que no tiene hambre. Es la tercera cena seguida. ¿Qué hace el técnico?", "Registra lo que comió y lo comenta a la enfermera, sin insistir ni opinar sobre el motivo", "Le dice que debe comer para no enfermarse", "No anota nada, porque ya sabe que no tiene hambre", "El registro y el aviso permiten que el profesional evalúe; el técnico no interpreta ni presiona."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿quién cambia el régimen de una persona?", "El profesional", "El técnico sirve lo que indica la ficha."),
        ("¿Qué haces si una persona tose con fuerza mientras come?", "Aviso de inmediato a la enfermera y a emergencias", "No actúo por cuenta propia ante un atragantamiento."),
        ("¿Qué verificas antes de servir una bandeja?", "Que la etiqueta coincida con la persona", "Así se evita servir un régimen equivocado."),
    ],
    op=("Caso de ejemplo: en una residencia de 24 personas se sirven 4 comidas al día y trabajan 3 técnicos. Un residente, Víctor, come muy despacio y dice que hoy prefiere no comer el postre. Otro, Wilson, empieza a toser con fuerza a mitad del almuerzo. "
        "Escribe: cuántas bandejas se sirven al día y cuántas sirve cada técnico; qué hace el técnico con Víctor; qué hace con Wilson; y una frase de registro sobre Víctor, sin etiquetas.",
        "Bandejas: 24 × 4 = 96; por técnico: 96 ÷ 3 = 32. Con Víctor: respeta su ritmo y su decisión, registra y avisa a la enfermera si es necesario. Con Wilson: avisa de inmediato a la enfermera y a emergencias, sin actuar por su cuenta. Registro: «Almuerzo: Víctor comió despacio y no quiso el postre».",
        ["calcula 96 y 32", "respeta el ritmo y la decisión de Víctor", "avisa de inmediato ante la tos de Wilson", "el registro es un hecho"],
        ["hoja con dos cálculos, dos conductas y una frase de registro"],
        ["apurar a Víctor", "darle agua a Wilson", "escribir una etiqueta en el registro"],
        "Pregunta: «¿qué hace el técnico si Wilson sigue tosiendo?». Debe responder que avisa de inmediato y no actúa por cuenta propia."),
    reinforce="Escribe tres cosas que hace el técnico al servir una comida y una que nunca hace por su cuenta.",
    extend="Explica con un ejemplo inventado por qué apurar a una persona mayor al comer puede ser peligroso.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (etiquetas de bandeja y regímenes de ejemplo). Residente 1, Olga: régimen común. Residente 2, Pedro: régimen blando, con alimentos de textura suave, indicado por la nutricionista. Residente 3, Rita: régimen sin sal agregada. "
     "Residente 4, Saúl: régimen común, con una alergia anotada a un alimento de ejemplo (el maní). Residente 5, Tina: régimen común; prefiere comer sin compañía. Residente 6, Ulises: régimen blando, con apoyo parcial de un técnico por temblor en las manos. "
     "Distribución de los 30 residentes por régimen: común 14, blando 7, sin sal agregada 5, otros 4. Grados de autonomía para comer: sin ayuda 12, con apoyo parcial 10, con apoyo mayor 8. Registro de ingesta por comida: 0, 25, 50, 75 o 100 por ciento de lo servido.")
build(
    O3, 2, F,
    use="Aprenderé el vocabulario de regímenes, alergias, autonomía e hidratación, a leer una etiqueta de bandeja y a anotar el registro de ingesta.",
    prior=["Conozco el régimen y el servicio de comidas.", "Sé leer una ficha y calcular promedios.", "Sé sumar y restar."],
    explain=[
        "Un régimen común es la alimentación sin restricciones especiales. Un régimen blando usa alimentos de textura suave y lo indica un profesional para personas con dificultad para masticar o tragar. Un régimen sin sal agregada se prepara sin añadir sal. Una alergia es una reacción dañina del cuerpo a un alimento; si la ficha la anota, ese alimento no se sirve. Una preferencia es lo que a la persona le gusta o no, incluidas las razones culturales o religiosas, y se respeta dentro de lo posible.",
        "La autonomía puede ser total, parcial o mayor apoyo, y la evalúa el equipo. La hidratación es el consumo de líquidos; se estimula y se registra. El registro de ingesta se anota por comida en porcentajes: 0, 25, 50, 75 o 100 de lo servido. Una etiqueta de bandeja debe coincidir con el nombre y el régimen de la persona; si no coincide, se detiene el servicio y se consulta.",
        "El técnico no cambia el régimen ni la textura por su cuenta; solo la nutricionista o el médico pueden hacerlo." + LIM,
    ],
    vocab=[("régimen común", "alimentación sin restricciones especiales"), ("régimen blando", "alimentación de textura suave, indicada por un profesional"), ("alergia", "reacción dañina del cuerpo a un alimento"), ("preferencia", "lo que a la persona le gusta o no, o razones culturales y religiosas"), ("hidratación", "consumo de líquidos de la persona"), ("porcentaje de ingesta", "parte de lo servido que la persona comió")],
    worked=[
        ("Elegir qué bandeja corresponde", "Una residente de ejemplo tiene anotado «régimen blando». ¿Qué bandeja corresponde?", ["La etiqueta debe coincidir con el régimen.", "La bandeja con etiqueta «régimen blando»."], "La bandeja con la etiqueta «régimen blando»"),
        ("Promedio de ingesta", "Una persona de ejemplo comió el 50 % en el desayuno y el 100 % en el almuerzo. ¿Cuál fue el promedio de esas dos comidas?", ["50 + 100 = 150.", "150 ÷ 2 = 75."], "75 %")],
    mistakes=[("Servir un alimento con maní a Saúl «solo un poquito» porque «no se nota».", "Una alergia puede causar una reacción dañina aunque la cantidad sea pequeña.", "No sirvas el alimento anotado como alergia y avisa a la enfermera."),
              ("Anotar «comió bien» sin porcentaje.", "No permite saber cuánto comió ni comparar entre comidas.", "Anota el porcentaje de lo servido: 0, 25, 50, 75 o 100.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es un régimen blando?", "Alimentación de textura suave, indicada por un profesional", "Alimentación sin ningún tipo de líquidos", "Alimentación solo con postres", "El régimen blando usa alimentos de textura suave y lo indica un profesional."),
        ("abc", "{F} ¿Qué régimen tiene Rita?", "Sin sal agregada", "Blando", "Común", "La ficha dice que Rita tiene régimen sin sal agregada."),
        ("abc", "{F} ¿Qué debe cuidar el técnico al servir la bandeja de Saúl?", "Que no contenga maní", "Que el alimento sea blando", "Que no lleve sal agregada", "La ficha anota una alergia al maní."),
        ("abc", "{F} ¿Qué preferencia tiene Tina?", "Comer sin compañía", "Comer con apoyo de un técnico", "No comer postre", "La ficha dice que Tina prefiere comer sin compañía."),
        ("=", "{F} ¿Cuántos residentes tienen un régimen distinto al común?", "30-14", "Se restan los residentes con régimen común del total.", " residentes"),
        ("=", "{F} ¿Cuántos residentes necesitan algún apoyo para comer, parcial o mayor?", "10+8", "Se suman los residentes con apoyo parcial y con apoyo mayor.", " residentes"),
        ("=", "{F} ¿Qué porcentaje de los residentes come sin ayuda?", "12*100//30", "Se multiplican los residentes sin ayuda por 100 y se dividen entre el total.", " %"),
        ("=", "{F} Si las ingestas de Olga en cuatro comidas fueron 100, 50, 75 y 75 por ciento, ¿cuál fue su promedio?", "(100+50+75+75)//4", "Se suman las cuatro ingestas y se dividen entre 4.", " %"),
        ("abc", "{F} La bandeja con etiqueta «Pedro, régimen común» llega a la mesa de Pedro, que tiene régimen blando. ¿Qué corresponde?", "Detener el servicio y consultar a la enfermera", "Servirla, porque Pedro puede masticar", "Cambiar la etiqueta con un lápiz", "La etiqueta no coincide con el régimen indicado; se verifica antes de servir."),
        ("abc", "{F} Un familiar de Ulises quiere llevarle comida desde su casa. ¿Qué hace el técnico?", "Avisa a la enfermera para que verifique que sea compatible con su régimen", "La sirve, porque es de la familia", "La rechaza sin explicar", "Los alimentos externos se revisan según el régimen indicado."),
        ("abc", "{F} Una residente de ejemplo no come carne por razones religiosas. ¿Qué corresponde?", "Respetar su preferencia y avisar a la nutricionista para ajustar", "Servirle carne igual, porque está en el menú", "Pedirle que la deje, sin avisar a nadie", "Las razones religiosas se respetan y el profesional adapta el régimen."),
        ("abc", "{F} Saúl dice que se siente raro después de comer una galleta que le dio otra persona. No se sabe si contenía maní. ¿Qué hace el técnico?", "Avisa de inmediato a la enfermera y a emergencias, y no le da nada más", "Le da agua y espera a ver qué pasa", "Le dice que es una impresión suya", "Una posible reacción a un alimento exige avisar de inmediato; el técnico no trata por su cuenta."),
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿para qué se registra la hidratación?", "Para que el equipo vea si la persona consume líquidos suficientes", "Para controlar cuánta agua gasta la residencia", "Para decidir cuánto debe pagar la familia", "El registro de hidratación ayuda a detectar a tiempo si una persona bebe poco."),
    ],
    ctx=("abc", "{F} Al servir el desayuno, la técnica nota que la bandeja de Rita (sin sal agregada) tiene la sal de un sobre al lado. Rita pide usarla porque «sin sal no tiene sabor». ¿Qué hace?", "Retira la sal, explica con respeto que su régimen la indica así y avisa a la nutricionista de su petición", "Se la deja, porque es su preferencia", "Le dice que se aguante, sin dar explicaciones", "La indicación del profesional se respeta; la petición se informa para que se evalúe."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces si la ficha anota una alergia?", "No sirvo ese alimento y aviso a la enfermera", "Una alergia puede causar una reacción dañina."),
        ("¿Cómo se anota la ingesta de una comida?", "En porcentajes: 0, 25, 50, 75 o 100", "Así se compara entre comidas y días."),
        ("¿Qué haces si la etiqueta no coincide con la persona?", "Detengo el servicio y consulto", "Un error de identificación puede ser grave."),
    ],
    op=("Etiquetas de ejemplo: «Bandeja 1, Abel, común. Bandeja 2, Berta, blando. Bandeja 3, Cecilia, sin sal agregada, alergia a un alimento de ejemplo (nueces). Bandeja 4, Darío, común, prefiere no comer cerdo». En la mesa están sentados Abel, Berta, Cecilia y Darío. La bandeja 3 trae un postre con nueces. "
        "Escribe: qué problema tiene la bandeja 3 y qué hace el técnico; cómo respeta la preferencia de Darío; y calcula el promedio de ingesta de Abel si comió el 75, 100, 50 y 75 por ciento en las cuatro comidas.",
        "La bandeja 3 trae un alimento al que Cecilia es alérgica: se retira, no se sirve y se avisa a la enfermera. Con Darío: no se le sirve cerdo y se avisa a la nutricionista para ajustar su menú. Promedio de Abel: (75+100+50+75) ÷ 4 = 75 %.",
        ["detecta la alergia y no sirve el postre", "respeta la preferencia", "calcula 75 %", "avisa a la enfermera o nutricionista"],
        ["hoja con el problema de la bandeja 3, la preferencia de Darío y el promedio"],
        ["servir el postre con nueces", "ignorar la preferencia de Darío", "calcular mal el promedio"],
        "Pregunta: «¿quién decide cómo cambiar el menú de Darío?». Debe responder la nutricionista."),
    reinforce="Escribe un régimen común, uno blando y uno sin sal agregada con tus palabras, y una alergia de ejemplo.",
    extend="Explica con un ejemplo inventado por qué se respetan las preferencias culturales o religiosas al servir una comida.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (casos y pauta de servir con dignidad, de ejemplo). Pauta de cinco criterios: (1) verificar que la etiqueta coincida con la persona; (2) higiene de manos antes de servir; (3) respetar preferencias y ritmo; (4) cuidar la postura segura de la persona y del técnico; (5) registrar lo consumido y avisar de tos, rechazo o cambios. "
     "Caso A: un técnico sirve la bandeja de régimen común a Pedro, que tiene régimen blando, sin revisar la etiqueta; cumple los criterios 2, 3, 4 y 5. "
     "Caso B: una técnica apura a Olga, que come despacio, y se inclina sobre ella con la espalda curva durante toda la comida; cumple los criterios 1, 2 y 5. "
     "Caso C: Rita tose con fuerza al comer; el técnico avisa de inmediato a la enfermera y a emergencias, no le da nada más y registra después; cumple los cinco criterios. "
     "Caso D: Saúl rechaza el almuerzo; el técnico respeta su decisión, registra 25 % de ingesta y avisa a la enfermera; cumple los cinco criterios.")
build(
    O3, 3, F,
    use="Aprenderé a analizar casos de alimentación con una pauta, a reconocer qué criterios se cumplieron y a decidir qué se informa y a quién.",
    prior=["Conozco el régimen, las alergias y el registro de ingesta.", "Sé calcular porcentajes de números enteros.", "Conozco el atragantamiento como riesgo."],
    explain=[
        "Analizar un caso de alimentación es leer lo que ocurrió y compararlo con la pauta. Cada criterio protege algo: verificar la etiqueta evita un régimen equivocado, la higiene de manos evita infecciones, respetar preferencias y ritmo cuida la autonomía y la dignidad, la postura segura previene lesiones de la persona y del técnico, y el registro permite que el equipo vea cambios a tiempo.",
        "Cuando un criterio falla, no se busca culpar: se describe el hecho y se informa a la enfermera para corregir. Cuando hay una señal de riesgo, como tos fuerte o rechazo repetido de comida, el técnico avisa de inmediato y no decide por cuenta propia. La enfermera evalúa si es necesario que intervenga el médico o la nutricionista.",
        "El rechazo de una comida es una decisión de la persona y también una información para el equipo." + LIM,
    ],
    vocab=[("pauta", "lista de criterios que se revisan en un caso"), ("rechazo de una comida", "decisión de la persona de no comer lo servido"), ("señal de alerta", "hecho que debe avisarse de inmediato al equipo"), ("postura segura", "posición que evita lesiones de la persona y de quien la ayuda"), ("registro de ingesta", "anotación de cuánto comió y bebió la persona")],
    worked=[
        ("Aplicar un criterio", "Una técnica de ejemplo sirve sin lavarse las manos después de tocar un pañuelo. ¿Qué criterio incumple?", ["Antes de servir se hace higiene de manos.", "Incumple el criterio 2."], "El criterio 2"),
        ("Calcular el cumplimiento", "Un caso de ejemplo cumple 4 de los 5 criterios. ¿Qué porcentaje es?", ["4 × 100 = 400.", "400 ÷ 5 = 80."], "80 %")],
    mistakes=[("Dejar de registrar el rechazo de una comida «porque la persona estaba de mal humor».", "El registro permite ver cambios en el tiempo; un rechazo puede ser un dato importante.", "Anota el porcentaje consumido y lo que la persona dijo, sin interpretar."),
              ("Seguir sirviendo al grupo mientras una persona tose con fuerza.", "La persona puede estar en peligro y necesita ayuda inmediata.", "Avisa de inmediato a la enfermera y a emergencias.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué debe hacer el técnico si una persona rechaza una comida?", "Respetar su decisión, registrar la ingesta y avisar a la enfermera", "Obligarla a comer", "Servirle otra comida sin avisar", "Se respeta la decisión y se informa para que el equipo evalúe."),
        ("abc", "{F} ¿Qué criterio incumple el técnico del caso A?", "El criterio 1: verificar la etiqueta", "El criterio 2: higiene de manos", "El criterio 5: registrar", "En el caso A no revisó la etiqueta y sirvió un régimen equivocado."),
        ("abc", "{F} ¿Qué criterios incumple la técnica del caso B?", "Los criterios 3 y 4", "Los criterios 1 y 2", "Solo el criterio 5", "La técnica cumple los criterios 1, 2 y 5; incumple el 3 porque apuró a Olga y el 4 porque cuidó mal la postura."),
        ("abc", "{F} ¿Qué casos cumplen todos los criterios de la pauta?", "Los casos C y D", "Los casos A y B", "Solo el caso A", "La ficha indica que C y D cumplen los cinco criterios."),
        ("=", "{F} ¿Cuántos criterios cumplen en total los cuatro casos?", "4+3+5+5", "Se suman los criterios cumplidos de cada caso.", " criterios"),
        ("=", "{F} ¿Qué porcentaje del total de criterios (4 casos de 5 criterios) se cumplió?", "(4+3+5+5)*100//(4*5)", "Se multiplica el total cumplido por 100 y se divide entre los criterios evaluados.", " %"),
        ("=", "{F} ¿Cuántos criterios incumplen en total los casos A y B?", "(5-4)+(5-3)", "Se restan los criterios cumplidos de los 5 de cada caso y se suman las fallas.", " criterios"),
        ("abc", "{F} En el caso C, ¿qué hace bien el técnico cuando Rita tose con fuerza?", "Avisa de inmediato a la enfermera y a emergencias y no actúa por cuenta propia", "Le da agua para que pase el bocado", "Le golpea la espalda para ayudar", "Ante un atragantamiento solo se avisa de inmediato."),
        ("abc", "{F} En el caso A, ¿qué debe hacer el técnico cuando se da cuenta del error de bandeja?", "Detener el servicio, avisar a la enfermera y dejar constancia", "Cambiar la bandeja en silencio", "No decir nada, porque no hubo daño", "Un error se informa para corregirlo y prevenirlo."),
        ("abc", "{F} Un compañero opina que en el caso D, Saúl «es caprichoso». ¿Qué corresponde?", "Anotar el hecho: rechazó el almuerzo y comió el 25 %, sin etiquetas", "Anotar que es caprichoso", "No anotar nada", "El registro describe hechos; las etiquetas no ayudan."),
        ("abc", "{F} En el caso B, la técnica dice que no tenía tiempo. ¿Qué corresponde?", "Avisar a la enfermera de la falta de tiempo para reorganizar el servicio", "Seguir apurando a los residentes", "Dejar a algunos sin comer", "La falta de tiempo es un problema de organización que se informa."),
        ("=", "{F} Si Saúl comió el 25 % en el almuerzo y el 75 % en la cena, ¿cuál es su promedio de esas dos comidas?", "(25+75)//2", "Se suman las dos ingestas y se dividen entre 2.", " %"),
        ("abc", "{F} Una persona de ejemplo, en una comida, solo toma una cucharada de su plato y se queda en silencio. ¿Qué anota el técnico?", "Que comió una cucharada y estuvo en silencio, e informa a la enfermera", "Que está deprimida", "Que no sabe comer", "Se describe lo observado y se avisa, sin diagnosticar."),
    ],
    ctx=("abc", "{F} Una técnica se da cuenta de que sirvió a un residente un vaso de jugo con azúcar, pero su ficha indica jugo sin azúcar. El residente ya empezó a tomar. ¿Qué hace?", "Avisa de inmediato a la enfermera, deja constancia del error y no le sirve más hasta que ella indique", "Le quita el vaso sin decir nada", "Espera a ver si el residente nota algo", "Un error de servicio se informa de inmediato; no se esconde ni se corrige a solas."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué haces si cometiste un error al servir?", "Aviso de inmediato a la enfermera y lo registro", "Ocultarlo impide corregir a tiempo y cuidar a la persona."),
        ("¿Qué haces si alguien tose con fuerza al comer?", "Aviso de inmediato a la enfermera y a emergencias", "No actúo por mi cuenta en un atragantamiento."),
        ("¿Cuántos criterios tiene la pauta de la ficha?", "5", "Etiqueta, higiene, preferencias, postura y registro."),
    ],
    op=("Casos de ejemplo: «A: un técnico sirve la bandeja correcta, con etiqueta verificada y manos limpias, pero habla de Lorenzo con otra persona frente a él, diciendo que es lento para comer. B: una técnica sirve una bandeja y el residente, que come con apoyo parcial, tose con fuerza; ella le da agua y sigue con otras bandejas sin avisar a nadie. C: un técnico registra 50 % de ingesta de Marta y la deja tranquila». "
        "Usa la pauta de la ficha. Escribe: qué criterios incumple cada caso; cuántos criterios se cumplen en total si A cumple 4, B cumple 4 y C cumple 5; y qué haría el técnico del caso B correctamente.",
        "A incumple el criterio 3 (no respeta la dignidad y el ritmo al comentar su lentitud frente a él). B incumple el criterio 5: no avisó de inmediato ante la tos ni lo registró, y dio agua por cuenta propia, lo que no corresponde. C cumple todos. Total: 4+4+5 = 13 de 15. En B correcto: avisar de inmediato a la enfermera y a emergencias, sin dar agua.",
        ["identifica criterios incumplidos", "calcula 13 de 15", "indica avisar de inmediato en B", "no recomienda dar agua"],
        ["hoja con criterios incumplidos, un total y la conducta correcta en el caso B"],
        ["recomendar dar agua", "no ver el problema del comentario sobre Lorenzo", "sumar mal"],
        "Pregunta: «¿tu respuesta para el caso B dice qué hace el técnico o qué debería hacer el residente?». Debe decir qué hace el técnico: avisar."),
    reinforce="Escribe los cinco criterios de la pauta y un ejemplo de una conducta que los incumpla.",
    extend="Explica con un ejemplo inventado por qué comentar frente a una persona mayor que come lento puede afectar su dignidad.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (registro de ingesta de dos residentes, de ejemplo; valores inventados que no sirven como referencia clínica). Residente X: porcentaje de lo servido que comió: desayuno 100, almuerzo 50, once 75, cena 75; líquidos bebidos por comida: 180, 220, 140 y 140 mililitros. "
     "Residente Y: desayuno 25, almuerzo 50, once 50, cena 75; líquidos: 200, 250, 250 y 200 mililitros. "
     "Regla de la hoja (de ejemplo): avisar a la enfermera si el promedio de ingesta del día es menor que 60 %, o si los líquidos del día suman menos de 700 mililitros.")
build(
    O3, 4, F,
    use="Aprenderé a calcular el promedio de ingesta y el total de líquidos de un día con enteros, a aplicar la regla de la hoja y a decidir qué se informa.",
    prior=["Sé sumar y dividir números enteros.", "Conozco el registro de ingesta.", "Sé aplicar una regla de aviso."],
    explain=[
        "El registro de ingesta se resume con dos números: el promedio de lo comido y el total de líquidos. El promedio de ingesta del día se calcula sumando los porcentajes de las comidas y dividiéndolos por la cantidad de comidas. El total de líquidos se calcula sumando los mililitros de cada comida. Ambos se comparan con la regla que escribió el profesional en la hoja.",
        "Si el resultado llega a la condición de la regla, el técnico avisa a la enfermera con los datos concretos: cuánto comió, cuánto bebió y cuándo. No interpreta ni da consejos: no dice si es grave ni qué debe hacer la persona. Un mismo resultado puede tener causas muy distintas, y solo el profesional las evalúa. También se registra el hecho de que la persona rechazó la comida, si ocurrió.",
        "Los valores son inventados y sirven solo para practicar la lectura de una hoja de registro." + LIM,
    ],
    vocab=[("promedio de ingesta", "suma de los porcentajes de las comidas dividida por la cantidad de comidas"), ("total de líquidos", "suma de los mililitros bebidos en el día"), ("mililitro", "unidad pequeña de volumen, abreviada ml"), ("regla de la hoja", "criterio escrito por el profesional que dice cuándo avisar"), ("dato concreto", "número o hecho exacto que se informa")],
    worked=[
        ("Promedio de ingesta", "Una persona de ejemplo comió el 100 %, el 50 % y el 50 % de tres comidas. ¿Cuál fue su promedio?", ["100 + 50 + 50 = 200.", "200 ÷ 3 no es exacto: se informan los tres porcentajes."], "No es exacto; se informan 100 %, 50 % y 50 %"),
        ("Total de líquidos", "En otra hoja de ejemplo, una persona bebió 150, 200 y 250 mililitros en tres comidas. ¿Cuántos mililitros bebió en total?", ["Se suman los tres volúmenes.", "150 + 200 + 250 = 600."], "600 mililitros")],
    mistakes=[("Redondear un promedio no exacto a un número «bonito» sin decirlo.", "Se altera el dato y puede ocultar información.", "Informa los datos de cada comida o el promedio exacto si es entero."),
              ("Decir «no es grave» al avisar a la enfermera.", "Es una interpretación que no le corresponde al técnico.", "Informa solo datos: cuánto comió, cuánto bebió y cuándo.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿cómo se calcula el promedio de ingesta del día?", "Se suman los porcentajes y se dividen por la cantidad de comidas", "Se multiplican los porcentajes entre sí", "Se toma solo el almuerzo", "El promedio resume las comidas del día en un solo valor."),
        ("=", "{F} ¿Cuál fue el promedio de ingesta del residente X?", "(100+50+75+75)//4", "Se suman los cuatro porcentajes y se dividen entre 4.", " %"),
        ("=", "{F} ¿Cuál fue el promedio de ingesta del residente Y?", "(25+50+50+75)//4", "Se suman los cuatro porcentajes y se dividen entre 4.", " %"),
        ("=", "{F} ¿Cuántos mililitros bebió en total el residente X?", "180+220+140+140", "Se suman los volúmenes de las cuatro comidas.", " mililitros"),
        ("=", "{F} ¿Cuántos mililitros bebió en total el residente Y?", "200+250+250+200", "Se suman los volúmenes de las cuatro comidas.", " mililitros"),
        ("abc", "{F} Según la regla de la hoja, ¿corresponde avisar por el promedio de ingesta del residente X?", "No: su promedio es 75 %, mayor que 60 %", "Sí: comió solo el 50 % en el almuerzo", "Sí: su promedio es menor que 60 %", "El promedio de X es 75 %, que no es menor que 60 %."),
        ("abc", "{F} Según la regla de la hoja, ¿corresponde avisar por los líquidos del residente X?", "Sí: sus líquidos suman 680 ml, menos de 700 ml", "No: bebió más de 700 ml", "No: la regla solo se refiere a la ingesta", "La regla pide avisar si los líquidos suman menos de 700 ml."),
        ("abc", "{F} Según la regla de la hoja, ¿corresponde avisar por el residente Y?", "Sí: su promedio de ingesta es 50 %, menor que 60 %", "No: sus líquidos suman más de 700 ml, así que está bien", "No: comió el 75 % en la cena", "Aunque sus líquidos están sobre 700 ml, el promedio de ingesta es menor que 60 %."),
        ("=", "{F} ¿Cuántos mililitros más que el residente X bebió el residente Y?", "(200+250+250+200)-(180+220+140+140)", "Se restan los líquidos totales de X de los de Y.", " mililitros"),
        ("abc", "{F} Al avisar por el residente X, ¿qué informa el técnico?", "Que bebió 680 ml en el día, con el detalle por comida", "Que el residente tiene un problema por beber poco", "Que debe tomar más agua", "Se informa un dato concreto; diagnosticar o aconsejar no corresponde al técnico."),
        ("abc", "{F} El residente Y dice que no tiene apetito. ¿Qué hace el técnico?", "Registra sus palabras, lo informa a la enfermera y no lo obliga a comer", "Le dice que debe comer más para no enfermarse", "Anota que está enfermo", "Se registra lo dicho y se informa; no se presiona ni se diagnostica."),
        ("=", "{F} Si el residente X hubiera comido 100, 100, 75 y 25 por ciento en las cuatro comidas, ¿cuál habría sido su promedio?", "(100+100+75+25)//4", "Se suman los cuatro porcentajes y se dividen entre 4.", " %"),
        ("abc", "{F} Una compañera anota 30 % en la once de Y, pero la persona había comido el 75 %. ¿Qué corresponde?", "Corregir con una línea, el valor correcto, hora y firma, y avisar a la enfermera", "Dejar el 30 %, porque ya está anotado", "Borrar el 30 % con corrector", "Los errores se corrigen con trazabilidad; un dato falso puede afectar decisiones."),
    ],
    ctx=("abc", "{F} Al revisar la hoja de Y, la técnica nota que otra persona anotó 250 ml en cada comida del día sin que Y beba tanto, según lo que ella observó. ¿Qué hace?", "Consulta a quien anotó y a la enfermera antes de aceptar el dato", "Corrige las cifras por su cuenta con lo que cree", "Acepta los datos, porque ya están firmados", "Un dato dudoso se verifica con quien lo anotó y se informa a la enfermera."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿qué informas cuando avisas por una regla de la hoja?", "Datos concretos: cuánto comió, cuánto bebió y cuándo", "Los datos permiten que el profesional evalúe."),
        ("¿Qué haces si un dato parece dudoso?", "Lo consulto con quien lo anotó y con la enfermera", "No se corrigen datos ajenos por suposición."),
        ("¿Qué le informas a la enfermera, los datos o un diagnóstico?", "Los datos", "El técnico no hace diagnósticos: eso lo evalúa el profesional."),
    ],
    op=("Hoja de ejemplo (valores inventados): «Residente Z. Ingesta por comida: 75, 75, 50, 100 por ciento; líquidos: 200, 150, 200, 150 mililitros. Regla: avisar si el promedio de ingesta es menor que 70 % o si los líquidos suman menos de 600 mililitros». "
        "Calcula: el promedio de ingesta y el total de líquidos; di si corresponde avisar y por qué; y escribe la frase que usarías para avisar a la enfermera, solo con datos.",
        "Promedio: (75+75+50+100) ÷ 4 = 75 %; líquidos: 200+150+200+150 = 700 mililitros. No corresponde avisar por la regla: 75 % no es menor que 70 % y 700 no es menor que 600. Frase: «Residente Z: ingesta de 75 % en promedio y 700 ml de líquidos en el día; se registró en la hoja».",
        ["calcula 75 % y 700 ml", "aplica la regla correctamente", "la frase usa solo datos", "no interpreta"],
        ["hoja con dos cálculos, una decisión y una frase de aviso"],
        ["decir que debe avisar sin cumplir la regla", "agregar un diagnóstico", "sumar mal los líquidos"],
        "Pregunta: «¿tu frase interpreta o solo cuenta datos?». Si interpreta, pídele quitar la interpretación."),
    reinforce="Con ingestas de 100, 50, 50 y 100 por ciento, calcula el promedio y di si se alcanza la regla de la ficha.",
    extend="Explica con un ejemplo inventado por qué un técnico informa datos y no un diagnóstico.",
)

# ============================================================ OAM-03, clase 5
F = ("Ficha 5 (comparar alternativas, de ejemplo). Dos modos de servir las comidas a 30 residentes con 4 técnicos. Alternativa A, comedor común con mesas de 4: 8 minutos por residente. Alternativa B, servicio en la habitación: 12 minutos por residente. "
     "Puntaje de 0 a 2 por criterio: comedor, autonomía 2, socialización 2, seguridad 1, ergonomía del técnico 1, higiene 1; habitación, autonomía 1, socialización 0, seguridad 2, ergonomía 1, higiene 2. "
     "Lista de verificación antes de servir (6 puntos): etiqueta con el nombre y régimen; manos limpias; superficie despejada; postura segura; alimentos a la temperatura de servicio indicada por la cocina; aviso a la enfermera de residentes con indicación especial. "
     "Regla: el modo de servir de cada residente lo decide la enfermera según su indicación y preferencia.")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos modos de servir comidas con criterios y tiempos, a verificar la calidad con una lista y a respetar la decisión individual de cada residente.",
    prior=["Conozco el servicio de comidas, la pauta y el registro.", "Sé sumar puntajes y calcular tiempos.", "Sé leer una lista de verificación."],
    explain=[
        "Comparar dos modos de servir comidas es evaluarlos con los mismos criterios: la autonomía de la persona, la socialización, la seguridad, la ergonomía del técnico y la higiene. Cada criterio se califica de 0 a 2 y se suman los puntos. También se compara el tiempo: se multiplican los minutos por residente por la cantidad de residentes y se dividen entre los técnicos que sirven al mismo tiempo.",
        "Un modo con más puntos no es el mejor para todos. Hay residentes que, por indicación del profesional o por su preferencia, comen mejor en la habitación, y otros prefieren el comedor. Por eso la enfermera decide el modo de cada persona. Antes de servir, el técnico verifica la lista: etiqueta, manos limpias, superficie despejada, postura segura, temperatura de servicio de los alimentos y avisos de indicaciones especiales.",
        "La temperatura de servicio la define la cocina según la norma vigente; el técnico solo comprueba que se cumpla lo que se le informa." + LIM,
    ],
    vocab=[("alternativa", "una de varias formas posibles de hacer algo"), ("criterio", "aspecto con el que se compara una alternativa"), ("socialización", "oportunidad de compartir con otros"), ("lista de verificación", "puntos que se revisan antes de servir"), ("decisión individual", "elección del modo de servir para cada persona según indicación y preferencia")],
    worked=[
        ("Calcular un tiempo", "Con 12 residentes, 6 minutos por residente y 3 técnicos sirviendo a la vez, ¿cuántos minutos demora el servicio?", ["12 × 6 = 72 minutos de trabajo.", "72 ÷ 3 = 24."], "24 minutos"),
        ("Sumar un puntaje", "Una alternativa de ejemplo tiene autonomía 2, socialización 1, seguridad 2, ergonomía 1 e higiene 2. ¿Cuántos puntos suma?", ["Se suman los cinco puntajes.", "2 + 1 + 2 + 1 + 2 = 8."], "8 puntos")],
    mistakes=[("Elegir un solo modo para todos porque suma más puntos.", "Cada persona tiene indicaciones y preferencias propias.", "Deja que la enfermera decida el modo de cada residente."),
              ("Marcar un punto de la lista sin mirar la bandeja.", "Una verificación sin observar no previene errores.", "Mira la etiqueta, las manos y el entorno antes de marcar.")],
    T=[
        ("abc", "En Atención de Enfermería (mención Adulto Mayor): ¿qué es una alternativa?", "Una de varias formas posibles de hacer algo", "El resultado final de una tarea", "Una opinión del técnico", "Se compara una alternativa con otra con los mismos criterios."),
        ("=", "{F} ¿Cuántos puntos suma el comedor?", "2+2+1+1+1", "Se suman los cinco puntajes del comedor.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma el servicio en la habitación?", "1+0+2+1+2", "Se suman los cinco puntajes de la habitación.", " puntos"),
        ("=", "{F} ¿Cuántos minutos demora el servicio en el comedor con 4 técnicos?", "30*8//4", "Se multiplican los residentes por los minutos de cada uno y se dividen entre los técnicos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos demora el servicio en la habitación con 4 técnicos?", "30*12//4", "Se multiplican los residentes por los minutos de cada uno y se dividen entre los técnicos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos más demora el servicio en la habitación que en el comedor?", "30*12//4-30*8//4", "Se restan los minutos del comedor de los de la habitación.", " minutos"),
        ("abc", "{F} ¿Qué modo es mejor en seguridad e higiene según la ficha?", "El servicio en la habitación", "El comedor", "Ambos por igual", "La habitación tiene 2 en seguridad y 2 en higiene; el comedor tiene 1 en ambos."),
        ("abc", "{F} Una residente de ejemplo ama conversar durante las comidas. ¿Qué modo respeta mejor su preferencia?", "El comedor, que tiene mayor socialización", "El servicio en la habitación", "Ninguno, porque no importa", "El comedor ofrece más oportunidades de compartir con otros."),
        ("abc", "{F} Otro residente tiene una indicación de comer en la habitación por una infección contagiosa. ¿Qué corresponde?", "Respetar la indicación del profesional y servir en la habitación", "Llevarlo al comedor para que socialice", "Preguntarle a los otros residentes qué prefieren", "Una indicación del profesional prevalece sobre las preferencias."),
        ("abc", "{F} La lista de verificación pide aviso a la enfermera de residentes con indicación especial. ¿Qué hace el técnico si no ha recibido ese aviso?", "Consulta a la enfermera antes de servir", "Supone que no hay indicaciones", "Pregunta al resto del equipo qué recuerdan", "Las indicaciones especiales las informa la enfermera; se consulta antes de servir."),
        ("abc", "{F} Al verificar, el técnico nota que dos bandejas no tienen etiqueta. ¿Qué hace?", "No las sirve y avisa a la cocina y a la enfermera", "Las sirve, porque cree saber a quién corresponden", "Les pone una etiqueta con lápiz", "Sin etiqueta no se puede verificar el régimen; se consulta."),
        ("abc", "{F} Un compañero dice: «El comedor suma 7 puntos y la habitación 6; entonces servimos a todos en el comedor». ¿Qué corresponde responder?", "Que el modo de cada residente lo decide la enfermera según su indicación y preferencia", "Que tiene razón, porque suma más puntos", "Que no se debe usar el comedor nunca", "El puntaje compara las alternativas, pero la decisión es individual."),
        ("=", "{F} Si se agregara un quinto técnico, ¿cuántos minutos demoraría el servicio en el comedor (con 30 residentes y 8 minutos cada uno)?", "30*8//5", "Se dividen los minutos de trabajo entre los 5 técnicos.", " minutos"),
    ],
    ctx=("abc", "{F} Antes del almuerzo, la técnica nota que la cocina entregó los alimentos con una temperatura que le parece distinta a la habitual, pero no tiene instrumentos para medirla. ¿Qué hace?", "Avisa a la enfermera y a la cocina antes de servir", "Sirve igual, porque no puede comprobarlo", "Prueba la comida para decidir", "La temperatura de servicio la define la cocina; ante una duda se avisa antes de servir."),
    sc=[
        ("En Atención de Enfermería (mención Adulto Mayor): ¿quién decide cómo come cada residente?", "La enfermera, según su indicación y preferencia", "El puntaje no reemplaza la decisión individual."),
        ("¿Qué haces si falta un punto de la lista de verificación?", "Consulto antes de servir", "Se resuelve antes de que la persona coma."),
        ("¿Cómo se calcula el tiempo de un servicio?", "Residentes × minutos ÷ técnicos", "Se reparte el trabajo entre los técnicos."),
    ],
    op=("Alternativas de ejemplo: «A, servicio en el comedor: 6 minutos por residente; puntaje: autonomía 2, socialización 2, seguridad 1, ergonomía 1, higiene 1. B, servicio en la habitación: 10 minutos por residente; puntaje: autonomía 1, socialización 0, seguridad 2, ergonomía 2, higiene 2». "
        "Hay 20 residentes y 5 técnicos. Calcula: los puntos de cada alternativa; el tiempo de cada una; y escribe qué decidiría la enfermera para un residente con una indicación de comer en la habitación y qué dos puntos de verificación revisarías.",
        "A: 2+2+1+1+1 = 7 puntos; B: 1+0+2+2+2 = 7 puntos: empatan. Tiempo A: 20×6÷5 = 24 minutos; B: 20×10÷5 = 40 minutos. Con la indicación de comer en la habitación, la decide el profesional: se sirve en la habitación. Puntos: etiqueta con nombre y régimen, y manos limpias.",
        ["calcula 7 y 7 y reconoce el empate", "calcula 24 y 40 minutos", "respeta la indicación del profesional", "nombra dos puntos de verificación"],
        ["hoja con dos puntajes, dos tiempos, una decisión y dos puntos"],
        ["decir que B es mejor por tener menos puntos de autonomía", "sumar mal", "ignorar la indicación"],
        "Pregunta: «¿hay una alternativa claramente mejor por puntaje?». Debe notar el empate y que decide la persona y la enfermera."),
    reinforce="Elige un residente de ejemplo y escribe qué modo de servir le convendría y por qué, según sus preferencias.",
    extend="Explica con un ejemplo inventado por qué una comida compartida puede ser buena para el ánimo de una persona mayor.",
)
