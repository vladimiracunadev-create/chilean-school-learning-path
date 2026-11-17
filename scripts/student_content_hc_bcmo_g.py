"""Biología celular y molecular (electivo 3.º y 4.º medio HC): OAC-07 (aplicaciones biotecnológicas e implicancias éticas, sociales y legales, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los casos, ensayos, tablas y cifras de los ejercicios son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas laboratorio ni internet. "
             "Este cuaderno trata las aplicaciones biotecnológicas solo a nivel de conceptos y análisis de evidencia: no incluye procedimientos de laboratorio ni de manipulación genética. "
             "Los casos de salud son generales y ficticios y no sirven para diagnosticar ni decidir tratamientos: esas decisiones son de profesionales de la salud. En los debates se presentan posturas con sus argumentos y se respeta a quienes piensan distinto.")
build = make_build(MATERIALS)

O7 = "CN-BCMO-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (cinco aplicaciones de ejemplo). Aplicación 1: producción de una hormona proteica usando células cultivadas. Aplicación 2: cultivo vegetal con resistencia a una plaga. Aplicación 3: tratamiento de aguas usando microorganismos que degradan contaminantes. "
     "Aplicación 4: terapia dirigida contra un tipo de célula tumoral. Aplicación 5: banco de células madre. "
     "Tres dimensiones para analizar implicancias: ética (qué es correcto o justo), social (cómo afecta a las personas y grupos) y legal (qué normas la regulan).")
build(
    O7, 1, F,
    use="Aprenderé qué es la biotecnología, en qué áreas se aplica y cómo delimitar una pregunta sobre sus implicancias éticas, sociales y legales. Sirve para empezar a analizar aplicaciones como tratamientos, células madre y transgénicos con criterio.",
    prior=["Conozco el dogma central y la regulación génica.", "Sé qué es una proteína.", "Sé que una decisión se justifica con argumentos."],
    explain=[
        "La biotecnología es el uso de organismos vivos, células o sus componentes para producir bienes o servicios. Existe desde hace siglos en formas tradicionales, como la fermentación para hacer pan o yogur, y hoy incluye aplicaciones modernas basadas en el conocimiento molecular: producir hormonas en células cultivadas, desarrollar tratamientos dirigidos, conservar células madre o crear organismos transgénicos.",
        "Se aplica en varias áreas: salud (medicamentos, vacunas, diagnósticos), agricultura (cultivos más resistentes), ambiente (tratamiento de aguas y residuos) e industria (enzimas para fabricar productos). Cada aplicación tiene beneficios y también preguntas: ¿quién tiene acceso?, ¿qué riesgos hay?, ¿qué normas la regulan?",
        "Para analizar una aplicación se delimitan tres dimensiones. La ética pregunta qué es correcto o justo, por ejemplo si hay consentimiento de las personas. La social pregunta cómo afecta a las personas, a las comunidades y al ambiente, y quiénes ganan o pierden. La legal pregunta qué leyes y normas existen o hacen falta. Una buena pregunta de investigación nombra la aplicación y al menos una dimensión.",
    ],
    vocab=[("biotecnología", "uso de organismos, células o sus componentes para producir bienes o servicios"), ("implicancia", "consecuencia o efecto de algo"), ("terapia dirigida", "tratamiento que actúa sobre una molécula o célula específica"), ("consentimiento informado", "aceptación libre de una persona después de entender qué se hará y sus riesgos"), ("regulación", "conjunto de normas que ordenan una actividad")],
    worked=[
        ("Clasificar por área", "La aplicación 3 trata aguas con microorganismos. ¿En qué área se ubica?",
         ["Se aplica al tratamiento de agua y contaminantes.", "Eso corresponde al área ambiental."],
         "Ambiente"),
        ("Elegir la dimensión", "¿Qué dimensión analiza si una persona dio su consentimiento para guardar sus células en un banco?",
         ["El consentimiento trata de lo que es correcto respecto de la decisión de la persona.", "Eso es una pregunta ética."],
         "Dimensión ética"),
    ],
    mistakes=[("Pensar que la biotecnología es solo ingeniería genética moderna.", "Incluye usos tradicionales, como la fermentación, y también aplicaciones modernas.", "Describe un rango de aplicaciones."),
              ("Confundir la dimensión legal con la ética.", "Lo legal depende de normas; lo ético, de principios y valores, y no siempre coinciden.", "Pregunta por separado: ¿qué dice la norma? y ¿qué es justo?")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es la biotecnología?", "El uso de organismos, células o sus componentes para producir bienes o servicios", "El estudio de las rocas", "La copia de un libro", "La biotecnología aprovecha lo vivo para producir bienes o servicios."),
        ("{F} ¿Qué aplicación (1 a 5) usa células cultivadas para producir una hormona?", "Aplicación 1", "La aplicación 1 produce una hormona proteica en células cultivadas."),
        ("{F} ¿Qué aplicación corresponde al área de agricultura?", "Aplicación 2", "El cultivo con resistencia a una plaga es una aplicación agrícola."),
        ("abc", "{F} ¿Cuál de estas aplicaciones es del área de salud?", "La aplicación 4, la terapia dirigida", "La aplicación 3, el tratamiento de aguas", "La aplicación 2, el cultivo vegetal", "La terapia contra células tumorales es una aplicación de salud."),
        ("ab", "{F} La fermentación para hacer pan, ¿es biotecnología?", "Sí: usa microorganismos para producir un alimento", "No: solo lo moderno es biotecnología", "Usar microorganismos para un producto es biotecnología tradicional."),
        ("{F} ¿Cuáles son las tres dimensiones que se proponen para analizar las implicancias?", "Ética, social y legal", "La ficha nombra las dimensiones ética, social y legal."),
        ("=", "En un listado de ejemplo hay 30 aplicaciones biotecnológicas: 12 de salud, 8 de agricultura y el resto de ambiente e industria. ¿Cuántas son de ambiente e industria?", "30-12-8", "Se restan del total las aplicaciones de salud y de agricultura.", " aplicaciones"),
        ("=", "En otro listado de ejemplo con 20 aplicaciones, 5 son de salud. ¿Qué porcentaje es de salud?", "5*100/20", "Para obtener el porcentaje se divide 5 entre 20 y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué dimensión pregunta cómo afecta a distintos grupos de personas el acceso desigual a una terapia dirigida?", "La social", "La legal", "Ninguna de las tres", "Preguntar cómo afecta a grupos y comunidades es una pregunta social."),
        ("abc", "{F} ¿Qué dimensión pregunta si existen normas que regulen un banco de células madre?", "La legal", "La ética", "La social", "Preguntar por normas es una pregunta legal."),
        ("ab", "Un compañero dice: «si algo es legal, entonces es ético». ¿Qué corriges?", "No siempre: lo legal y lo ético se analizan por separado y pueden no coincidir", "Tiene razón: son lo mismo", "Una norma puede permitir algo sobre lo que aún se discute éticamente."),
        ("abc", "{F} ¿Cuál es la pregunta de investigación mejor delimitada?", "¿Qué beneficios y qué dilemas éticos plantea un banco de células madre?", "¿Qué es la biotecnología?", "¿Qué ocurre hoy en la ciencia?", "La mejor pregunta nombra la aplicación y la dimensión analizada."),
        ("abc", "{F} Un compañero dice: «los tratamientos solo traen beneficios». ¿Cuál es la mejor respuesta?", "Tienen beneficios y también riesgos y dilemas que hay que analizar", "Tiene razón: no tienen riesgos", "No tienen beneficios", "Un análisis honesto considera beneficios y riesgos."),
    ],
    ctx=("abc", "Contexto: tu liceo organizará un foro sobre biotecnología y debes proponer una pregunta que oriente el debate. ¿Cuál eliges?", "¿Qué beneficios, riesgos y reglas debería tener una aplicación biotecnológica?", "¿Quién gana siempre?", "¿Es la ciencia buena o mala?", "La pregunta orienta el debate hacia beneficios, riesgos y reglas, sin conclusión anticipada."),
    sc=[
        ("En Biología celular y molecular: ¿qué es el consentimiento informado?", "La aceptación libre de una persona después de entender qué se hará y sus riesgos", "Es un principio ético básico de la investigación y la atención de salud."),
        ("ab", "La terapia dirigida actúa sobre:", "Una molécula o célula específica", "Todo el organismo sin distinción", "La terapia dirigida apunta a un blanco concreto."),
        ("ab", "La dimensión legal pregunta por:", "Las normas", "Los gustos", "Lo legal se refiere a leyes y normas."),
    ],
    op=("Con las aplicaciones de la ficha {F}: (1) clasifica cada una por área (salud, agricultura, ambiente); (2) elige una y escribe una pregunta para cada dimensión: ética, social y legal; (3) escribe un beneficio y un riesgo posibles de esa aplicación.",
        "(1) 1 salud, 2 agricultura, 3 ambiente, 4 salud, 5 salud. (2) Aplicación 5: ética, ¿hubo consentimiento?; social, ¿quién puede acceder al banco?; legal, ¿qué normas regulan el uso de las muestras? (3) Beneficio: material para tratamientos futuros; riesgo: uso indebido de la información.",
        ["clasificación por área", "una pregunta por dimensión", "beneficio y riesgo"],
        ["tres respuestas numeradas"],
        ["mezclar las dimensiones", "preguntas demasiado amplias", "mencionar solo beneficios"],
        "Pregunta: «¿qué datos necesitarías para responder tu pregunta social?»."),
    reinforce="Elige otra aplicación de la ficha y escribe una pregunta ética, una social y una legal.",
    extend="Explica por qué la biotecnología tradicional y la moderna comparten el principio de aprovechar procesos de los seres vivos.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (conceptos y ensayo de ejemplo sobre tratamientos del cáncer; todo es general, ficticio y no sirve para decidir tratamientos). Algunas estrategias: cirugía, que retira un tumor; radioterapia, que daña el ADN de células tumorales; quimioterapia, que actúa sobre células que se dividen rápido; "
     "terapia dirigida, que actúa sobre una molécula alterada característica de un tipo de tumor; inmunoterapia, que ayuda al sistema inmune a reconocer células tumorales. Los tratamientos pueden tener efectos secundarios. "
     "Ensayo de ejemplo: 200 personas voluntarias de un estudio ficticio se reparten al azar en dos grupos de 100. Grupo 1: tratamiento nuevo; 60 mejoran. Grupo 2: tratamiento habitual; 45 mejoran. "
     "Un ensayo clínico compara tratamientos con personas voluntarias, con un grupo de comparación, autorización previa y consentimiento informado.")
build(
    O7, 2, F,
    use="Aprenderé la base molecular de algunos tratamientos para el cáncer y cómo se evalúa con evidencia si un tratamiento nuevo funciona. Sirve para analizar noticias sobre tratamientos sin sacar conclusiones apresuradas.",
    prior=["Conozco cómo se regula la proliferación celular.", "Sé calcular porcentajes.", "Sé qué es un grupo de comparación."],
    explain=[
        "El cáncer nace de cambios en genes que regulan la división celular. Por eso muchos tratamientos se diseñan con base molecular. La radioterapia y la quimioterapia dañan a células que se dividen rápido, pero también pueden afectar a células sanas, lo que explica efectos secundarios. La terapia dirigida actúa sobre una molécula alterada propia de cierto tumor. La inmunoterapia ayuda al sistema inmune a reconocer las células tumorales.",
        "Para saber si un tratamiento nuevo funciona se usa un ensayo clínico: se comparan grupos de personas voluntarias, con autorización previa y consentimiento informado. Los grupos se arman al azar para que sean parecidos, y uno recibe el tratamiento nuevo y otro el habitual. Se comparan los resultados con proporciones. Una diferencia a favor puede deberse a azar, por lo que importa tener muchas personas y repetir los estudios.",
        "Interpretar un ensayo exige cuidado. Un porcentaje mayor no significa que el tratamiento sea adecuado para cualquier persona: dependen de la edad, el tipo de tumor, los efectos secundarios y los valores de cada paciente. Las decisiones médicas son de profesionales y de cada paciente con su equipo de salud, no de un cuaderno de estudio.",
    ],
    vocab=[("terapia dirigida", "tratamiento que actúa sobre una molécula alterada característica de un tipo de tumor"), ("inmunoterapia", "tratamiento que ayuda al sistema inmune a reconocer células tumorales"), ("ensayo clínico", "estudio que compara tratamientos en personas voluntarias con autorización y consentimiento"), ("efecto secundario", "efecto no buscado de un tratamiento"), ("grupo de comparación", "grupo que recibe el tratamiento habitual para comparar")],
    worked=[
        ("Calcular porcentajes", "En el grupo 1, 60 de 100 mejoran. ¿Qué porcentaje es y cuál es el del grupo 2?",
         ["Grupo 1: 60 de 100 es 60 %.", "Grupo 2: 45 de 100 es 45 %."],
         "60 % y 45 %"),
        ("Interpretar la diferencia", "La diferencia entre grupos es 15 puntos porcentuales. ¿Prueba que el tratamiento nuevo es mejor para toda persona?",
         ["El ensayo solo incluye a las personas del estudio.", "Puede haber efectos secundarios y diferencias entre personas."],
         "No: aporta evidencia, pero no decide el tratamiento de cada persona"),
    ],
    mistakes=[("Creer que un tratamiento nuevo es mejor solo porque un grupo mejoró más.", "La diferencia puede deberse al azar y hay que considerar efectos secundarios y repetir el estudio.", "Habla de evidencia a favor, no de prueba definitiva."),
              ("Usar un ensayo para recomendar un tratamiento a una persona concreta.", "Las decisiones de salud son de profesionales y de cada paciente.", "Aclara que el análisis es general.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un ensayo clínico?", "Un estudio que compara tratamientos en personas voluntarias con autorización y consentimiento", "Un experimento en una cocina", "Una opinión de un periodista", "Un ensayo clínico compara tratamientos con reglas éticas y legales."),
        ("{F} ¿Cuántas personas voluntarias hay en total en el ensayo de ejemplo?", "200", "La ficha indica 200 personas, repartidas en dos grupos de 100."),
        ("{F} ¿Cuántas personas del grupo 2 mejoran?", "45", "La ficha señala 45 de 100 en el grupo con tratamiento habitual."),
        ("abc", "{F} ¿Qué estrategia actúa sobre una molécula alterada propia de un tipo de tumor?", "La terapia dirigida", "La cirugía", "La radioterapia", "La terapia dirigida apunta a una molécula específica."),
        ("ab", "{F} ¿Por qué los grupos se arman al azar?", "Para que los grupos sean parecidos y la diferencia no se deba a quién se eligió", "Para que el tratamiento nuevo tenga más éxito", "El azar evita que quien arma los grupos sesgue la comparación."),
        ("{F} ¿Qué estrategia ayuda al sistema inmune a reconocer las células tumorales?", "La inmunoterapia", "La ficha atribuye esa función a la inmunoterapia."),
        ("=", "Otro ensayo ficticio tiene 80 personas en el grupo 1 y mejoran 40. ¿Qué porcentaje del grupo mejora?", "40*100/80", "Se divide 40 entre 80 y se multiplica por 100 para obtener el porcentaje.", " %"),
        ("=", "En otro ensayo ficticio con 90 personas por grupo, mejoran 54 en el grupo 1 y 36 en el grupo 2. ¿Cuántos puntos porcentuales más mejoran en el grupo 1?", "54*100/90-36*100/90", "Se calcula el porcentaje de cada grupo (60 % y 40 %) y se restan.", " puntos"),
        ("abc", "{F} Un estudio ficticio posterior con solo 10 personas por grupo encuentra 7 y 6 que mejoran. ¿Qué conviene concluir?", "Que la diferencia es muy pequeña y con tan pocas personas puede deberse al azar", "Que el tratamiento nuevo es mucho mejor", "Que el tratamiento habitual es mucho mejor", "Con pocas personas, las diferencias pequeñas son poco confiables."),
        ("abc", "{F} Una noticia dice: «el tratamiento nuevo cura al 60 %». ¿Qué falta aclarar?", "Qué significa mejorar, qué tipo de tumor, qué efectos secundarios y la comparación con el grupo habitual", "Nada, está completo", "Solo el nombre del tratamiento", "El 60 % necesita contexto: definición de mejoría, comparación y efectos."),
        ("ab", "{F} La quimioterapia actúa sobre células que se dividen rápido. ¿Qué explica los efectos secundarios?", "También puede afectar a células sanas que se dividen rápido", "Solo afecta al tumor", "El tratamiento no distingue siempre entre células tumorales y sanas de rápida división."),
        ("abc", "{F} Alguien escribe: «con ese ensayo recomiendo que una persona conocida use el tratamiento nuevo». ¿Qué respuesta es correcta?", "La decisión corresponde a su equipo de salud, que considera su caso", "Tiene razón: el ensayo basta", "El ensayo no sirve para nada", "El ensayo aporta evidencia general; la decisión individual es de profesionales."),
        ("abc", "{F} ¿Qué principio ético exige que las personas del ensayo sepan en qué consiste el estudio?", "El consentimiento informado", "El azar", "La rapidez", "Las personas deben aceptar libremente tras entender riesgos y objetivos."),
    ],
    ctx=("abc", "Contexto: en redes sociales circula un mensaje que dice «terapia milagrosa cura todo tipo de cáncer». ¿Cómo lo analizas con lo visto?", "Pido evidencia: ensayos con grupo de comparación, tipo de tumor y efectos secundarios", "Lo comparto porque da esperanza", "Lo creo porque lo dice mucha gente", "Una afirmación absoluta requiere evidencia revisable."),
    sc=[
        ("En Biología celular y molecular: ¿qué es un efecto secundario?", "Un efecto no buscado de un tratamiento", "Los efectos secundarios deben evaluarse junto con los beneficios."),
        ("ab", "El azar al armar los grupos sirve para:", "Que los grupos sean parecidos", "Que gane el nuevo tratamiento", "El azar evita que quien arma los grupos introduzca sesgos en la comparación."),
        ("ab", "Un ensayo de pocas personas es:", "Menos confiable", "Más confiable", "Con pocas personas el azar pesa más."),
    ],
    op=("Con la ficha {F}: (1) calcula el porcentaje de mejora de cada grupo y la diferencia; (2) escribe dos razones por las que esa diferencia no basta para recomendar el tratamiento a cualquier persona; (3) escribe una pregunta que le harías al equipo investigador.",
        "(1) 60 %, 45 % y 15 puntos de diferencia. (2) Puede haber efectos secundarios y las personas son distintas; el ensayo solo incluye a un grupo. (3) ¿Qué efectos secundarios se observaron en cada grupo?",
        ["porcentajes y diferencia correctos", "dos razones distintas", "pregunta pertinente al estudio"],
        ["tres respuestas numeradas"],
        ["no calcular la diferencia", "dar solo una razón", "dar consejos de salud personales"],
        "Pregunta: «¿qué dato adicional te haría más confiable el resultado?»."),
    reinforce="Escribe tres preguntas que harías ante cualquier noticia que dice que un tratamiento nuevo funciona.",
    extend="Explica por qué un ensayo con personas exige consentimiento informado y autorización antes de empezar.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (modelo de ejemplo de células madre). Potencial de diferenciación: totipotentes, pueden dar origen a un organismo completo y a sus anexos; pluripotentes, pueden originar casi todos los tipos de células del cuerpo; multipotentes, pueden originar varios tipos de células de un mismo tejido. "
     "Fuentes de ejemplo: células de embriones muy tempranos (pluripotentes); células de tejidos adultos, como la médula ósea (multipotentes); células de la sangre del cordón umbilical, que se pueden guardar en bancos; células adultas reprogramadas en laboratorio para volverse pluripotentes. "
     "Usos conocidos: el trasplante de células formadoras de sangre se usa en algunas enfermedades de la sangre. Se investigan otros usos. Banco de ejemplo: guardar una muestra cuesta 4 unidades por año.")
build(
    O7, 3, F,
    use="Aprenderé qué son las células madre, qué tipos hay según su potencial, cómo se preservan y usan, y qué preguntas éticas y sociales plantean. Sirve para construir un modelo del potencial de las células y para interpretar casos de preservación.",
    prior=["Conozco la diferenciación celular.", "Sé que las células de un organismo tienen los mismos genes.", "Sé calcular costos acumulados."],
    explain=[
        "Las células madre son células capaces de dividirse y de dar origen a otros tipos de células. Se clasifican por su potencial de diferenciación: las totipotentes pueden originar un organismo completo; las pluripotentes, casi todos los tipos de células del cuerpo; las multipotentes, varios tipos de un tejido. Mientras mayor el potencial, mayor la diversidad de células que pueden originar.",
        "Pueden obtenerse de varias fuentes: de embriones muy tempranos, de tejidos adultos (por ejemplo, médula ósea), de la sangre del cordón umbilical y por reprogramación de células adultas. El uso mejor establecido es el trasplante de células formadoras de sangre en algunas enfermedades de la sangre. Otras aplicaciones se encuentran en investigación y requieren más evidencia antes de ofrecerse como tratamiento.",
        "Su preservación en bancos plantea preguntas: ¿quién decide?, ¿hay un banco público o privado?, ¿qué ocurre con los costos y el acceso? Si se usan embriones, se discute cuándo comienza a tener valor ético una vida, y distintas personas responden de forma diferente. En Chile existen normas que regulan la investigación con seres humanos; para detalles, tu docente o fuentes oficiales. Un análisis serio presenta las posturas con sus argumentos.",
    ],
    vocab=[("célula madre", "célula capaz de dividirse y de originar otros tipos de células"), ("pluripotente", "capaz de originar casi todos los tipos de células del cuerpo"), ("multipotente", "capaz de originar varios tipos de células de un mismo tejido"), ("reprogramación", "proceso por el que una célula adulta adquiere características de célula pluripotente"), ("banco de células", "lugar donde se conservan muestras de células")],
    worked=[
        ("Clasificar por potencial", "Una célula de la médula ósea puede originar varios tipos de células de la sangre. ¿Qué potencial tiene?",
         ["Origina varios tipos, pero de un mismo tejido.", "Eso es multipotente."],
         "Multipotente"),
        ("Costo acumulado", "Guardar una muestra cuesta 4 unidades por año. ¿Cuánto cuesta guardarla 10 años?",
         ["4 unidades por año durante 10 años.", "4 × 10 = 40."],
         "40 unidades"),
    ],
    mistakes=[("Creer que todas las células madre pueden originar cualquier tipo de célula.", "Solo las pluripotentes y totipotentes tienen ese potencial amplio; las multipotentes son limitadas.", "Indica siempre el potencial al hablar de una célula madre."),
              ("Dar por probado un tratamiento que todavía se investiga.", "Muchos usos están en investigación y requieren más evidencia.", "Distingue usos establecidos y usos en investigación.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es una célula madre?", "Una célula capaz de dividirse y de originar otros tipos de células", "Una célula que no se divide", "Una célula muerta", "Su rasgo central es dividirse y dar origen a otras células."),
        ("{F} ¿Qué tipo de células madre pueden originar casi todos los tipos de células del cuerpo?", "Las pluripotentes", "La ficha asigna a las pluripotentes ese potencial."),
        ("{F} ¿De qué fuente son las células de la médula ósea?", "De tejidos adultos", "La médula ósea es un ejemplo de tejido adulto."),
        ("abc", "{F} ¿Qué potencial tienen las células que pueden originar varios tipos de un mismo tejido?", "Multipotente", "Totipotente", "Pluripotente", "El potencial limitado a un tejido es multipotente."),
        ("ab", "{F} ¿Cuál tiene mayor potencial de diferenciación?", "Una célula pluripotente", "Una célula multipotente", "Las pluripotentes originan más tipos de células que las multipotentes."),
        ("{F} ¿Qué uso de las células madre está mejor establecido según la ficha?", "El trasplante de células formadoras de sangre", "La ficha lo menciona como uso conocido en algunas enfermedades de la sangre."),
        ("=", "{F} ¿Cuánto cuesta guardar una muestra durante 8 años?", "4*8", "Se multiplica el costo anual por el número de años.", " unidades"),
        ("=", "{F} Una familia quiere guardar 3 muestras durante 5 años cada una. ¿Cuál es el costo total?", "3*4*5", "Se multiplica el número de muestras por el costo anual y por los años.", " unidades"),
        ("abc", "{F} Un laboratorio de ejemplo reprograma una célula de la piel para que sea pluripotente. ¿Qué cambia?", "Se parece más a una célula con gran potencial de diferenciación", "Su ADN desaparece", "Se vuelve totipotente siempre", "La reprogramación aumenta su potencial de diferenciación."),
        ("abc", "{F} Una publicidad de ejemplo ofrece «un tratamiento con células madre para cualquier enfermedad». ¿Qué conviene hacer?", "Pedir evidencia de ensayos y consultar a profesionales de la salud", "Aceptarlo de inmediato", "Pagar sin preguntar", "Una promesa universal sin evidencia merece desconfianza."),
        ("ab", "{F} ¿Por qué se discute éticamente el uso de embriones como fuente?", "Porque personas distintas piensan diferente sobre el valor de la vida desde sus primeras etapas", "Porque los embriones no tienen células", "Hay posturas diversas, y un buen análisis las presenta con respeto."),
        ("abc", "{F} Un banco público de sangre de cordón y uno privado se comparan. ¿Qué dimensión social se discute?", "El acceso y los costos para distintos grupos", "El color de los tubos", "La temperatura del ambiente", "La forma de organizar un banco afecta quién accede a él."),
        ("abc", "{F} Se dice: «las células madre siempre curan». ¿Qué se corrige?", "Muchos usos están en investigación y no están probados", "Nunca se usan", "Funcionan igual para todas las enfermedades", "Hay usos establecidos y otros que requieren más evidencia."),
    ],
    ctx=("abc", "Contexto: una familia de ejemplo duda si guardar una muestra de sangre de cordón. Como estudiante, ¿qué aportas sin dar una recomendación médica?", "Explico conceptos, costos y preguntas por hacer, y sugiero consultar a profesionales de la salud", "Les digo qué deben hacer", "Les digo que no sirve para nada", "Se puede informar sin reemplazar la decisión de profesionales y de la familia."),
    sc=[
        ("En Biología celular y molecular: ¿qué es una célula multipotente?", "Una célula que puede originar varios tipos de células de un mismo tejido", "Su potencial se limita a un tejido."),
        ("ab", "La reprogramación de una célula adulta la vuelve:", "Pluripotente", "Totipotente de inmediato", "La reprogramación busca un estado pluripotente."),
        ("ab", "Un banco de células:", "Conserva muestras de células", "Fabrica ADN", "Un banco de células conserva muestras para posibles usos futuros."),
    ],
    op=("Con el modelo de la ficha {F}: (1) dibuja un esquema con los tres potenciales y una flecha del tipo de células que puede originar cada uno; (2) calcula el costo de guardar una muestra 12 años; (3) escribe una pregunta ética y otra social sobre los bancos de células madre.",
        "(1) Totipotente: organismo completo; pluripotente: casi todos los tipos; multipotente: varios tipos de un tejido. (2) 4 × 12 = 48 unidades. (3) Ética: ¿se obtuvo consentimiento? Social: ¿quién puede acceder a ese banco?",
        ["esquema con tres potenciales", "cálculo correcto", "una pregunta ética y otra social"],
        ["un esquema, un cálculo y dos preguntas"],
        ["confundir pluripotente con multipotente", "calcular mal el costo", "poner dos preguntas de la misma dimensión"],
        "Pregunta: «¿qué postura distinta a la tuya conoces y cuál es su argumento?»."),
    reinforce="Haz una tabla con los tres potenciales, un ejemplo de fuente y lo que pueden originar.",
    extend="Explica por qué un tratamiento que todavía está en investigación no debería ofrecerse como si estuviera comprobado.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (conceptos y ensayo de campo de ejemplo sobre organismos transgénicos; no se describen procedimientos). Un organismo transgénico es aquel que lleva incorporado un gen de otra especie, que le da una característica nueva, por ejemplo resistencia a una plaga. "
     "Evaluación de una aplicación: se analizan beneficios, riesgos para la salud y el ambiente, seguridad alimentaria, etiquetado, coexistencia con otros cultivos y propiedad de las semillas. "
     "Datos de ejemplo de dos parcelas de igual tamaño: cultivo convencional: daño por la plaga en 40 de cada 100 plantas, 3 aplicaciones de insecticida durante la temporada; cultivo con resistencia: daño en 10 de cada 100 plantas, 1 aplicación de insecticida.")
build(
    O7, 4, F,
    use="Aprenderé qué es un organismo transgénico, para qué se produce y cómo se evalúan con datos sus beneficios y riesgos, sin entrar en procedimientos de laboratorio. Sirve para analizar evidencia sobre transgénicos y distinguir hechos de opiniones.",
    prior=["Conozco el dogma central.", "Sé que el código genético es casi universal.", "Sé calcular porcentajes."],
    explain=[
        "Un organismo transgénico lleva en su genoma un gen de otra especie, que le da una característica nueva. Esto es posible porque el código genético es casi universal: una célula puede leer y traducir un gen de otra especie. Con ese principio se producen, por ejemplo, cultivos con resistencia a ciertas plagas o microorganismos que fabrican una proteína útil, como una hormona.",
        "Evaluar una aplicación transgénica exige mirar beneficios y riesgos con datos. Los beneficios posibles son mayor rendimiento, menos daño por plagas o menos uso de ciertos insecticidas. Los riesgos que se estudian incluyen efectos sobre la salud, sobre otras especies y sobre la diversidad, además de temas sociales como el etiquetado, la coexistencia con cultivos tradicionales y quién controla las semillas. Cada país tiene normas distintas.",
        "Al analizar evidencia hay que separar lo que muestran los datos de lo que no. Los datos de una parcela en una temporada no permiten concluir sobre todos los lugares ni sobre efectos a largo plazo. Por eso se hacen estudios repetidos y se vigilan los efectos. Y aunque los datos ayuden, las decisiones también dependen de valores, como la prioridad que una comunidad da a la producción, a la diversidad o a la precaución.",
    ],
    vocab=[("transgénico", "organismo que lleva incorporado un gen de otra especie"), ("seguridad alimentaria", "acceso a alimentos suficientes, inocuos y nutritivos"), ("etiquetado", "información en el envase sobre el contenido de un producto"), ("coexistencia", "convivencia de cultivos distintos en una misma zona"), ("principio de precaución", "criterio de actuar con cuidado cuando hay incertidumbre sobre riesgos")],
    worked=[
        ("Comparar daño", "En la parcela convencional el daño es 40 de cada 100 plantas, y en la de resistencia, 10 de cada 100. ¿Cuántas plantas menos dañadas por cada 100?",
         ["Se restan los dos valores.", "40 − 10 = 30."],
         "30 plantas menos por cada 100"),
        ("Declarar el límite", "¿Los datos de una parcela en una temporada permiten concluir sobre efectos a largo plazo?",
         ["Solo miden una parcela y una temporada.", "Los efectos a largo plazo requieren más años y más lugares."],
         "No: son insuficientes para eso"),
    ],
    mistakes=[("Decir que un transgénico es peligroso o seguro «en general».", "Cada aplicación se evalúa por separado con sus datos.", "Habla de una aplicación concreta y de la evidencia disponible."),
              ("Concluir a partir de una sola parcela y una sola temporada.", "Falta repetir en otros lugares y años.", "Declara el límite y propone repetir el estudio.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un organismo transgénico?", "Un organismo con un gen de otra especie incorporado", "Un organismo sin genes", "Un organismo muy grande", "Lleva un gen de otra especie que le da una característica nueva."),
        ("{F} ¿Cuántas aplicaciones de insecticida tuvo el cultivo convencional?", "3", "La ficha indica 3 aplicaciones en la parcela convencional."),
        ("{F} ¿En cuántas de cada 100 plantas hay daño en el cultivo con resistencia?", "10", "La ficha señala daño en 10 de cada 100 plantas."),
        ("abc", "{F} ¿Por qué una célula puede leer un gen de otra especie?", "Porque el código genético es casi universal", "Porque los genes son siempre iguales", "Porque se usa otro código", "Un código casi universal permite traducir genes de distintas especies."),
        ("ab", "{F} ¿Qué es el etiquetado en este contexto?", "La información en el envase sobre el contenido del producto", "Un tipo de cultivo", "El etiquetado informa para que las personas puedan elegir."),
        ("{F} ¿Qué criterio propone actuar con cuidado cuando hay incertidumbre sobre riesgos?", "El principio de precaución", "Ese es el sentido del principio de precaución."),
        ("=", "{F} ¿Cuántas aplicaciones de insecticida menos tuvo el cultivo con resistencia?", "3-1", "Se resta el número de aplicaciones del cultivo con resistencia al del convencional.", " aplicaciones"),
        ("=", "{F} Si cada parcela tiene 500 plantas, ¿cuántas plantas dañadas hay en el cultivo convencional?", "500*40/100", "Se calcula el 40 % de 500 plantas.", " plantas"),
        ("abc", "{F} Con 500 plantas por parcela, ¿cuántas plantas dañadas hay en el cultivo con resistencia?", "50", "10", "100", "El 10 % de 500 es 50 plantas dañadas."),
        ("abc", "{F} Un comunicado dice: «el cultivo transgénico es seguro en todos los casos porque redujo el daño». ¿Qué falla?", "Reducir el daño por plagas no prueba la ausencia de otros riesgos", "Nada: el comunicado es correcto", "El daño no se puede medir", "Un beneficio no demuestra que no haya riesgos que evaluar."),
        ("ab", "{F} Un agricultor vecino cultiva de forma tradicional. ¿Qué tema social aparece?", "La coexistencia entre cultivos distintos", "La temperatura de las semillas", "Los cultivos vecinos pueden influir entre sí, por lo que se regula su convivencia."),
        ("abc", "{F} ¿Qué dato adicional haría más confiable la comparación de las dos parcelas?", "Repetir el estudio en otros lugares y temporadas", "Eliminar la parcela convencional", "Mirar solo la parcela con resistencia", "Repetir el estudio muestra si el resultado se mantiene."),
        ("abc", "Dos personas debaten sobre un cultivo de ejemplo con el mismo dato de daño y llegan a posturas distintas. ¿Qué puede explicarlo?", "Les dan prioridad distinta a valores como producción, diversidad o precaución", "Una de ellas leyó mal los datos", "Los datos de la parcela cambian al discutirlos", "Las decisiones combinan datos y valores."),
    ],
    ctx=("abc", "Contexto: para el foro del liceo debes presentar en un minuto los datos de las dos parcelas sin tomar partido. ¿Qué incluyes?", "Los datos de daño e insecticida, sus límites y las preguntas abiertas", "Solo los datos que favorecen una postura", "Una opinión sin datos", "Una presentación equilibrada muestra datos, límites y preguntas."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la coexistencia de cultivos?", "La convivencia de cultivos distintos en una misma zona", "Es un tema práctico y social al evaluar cultivos."),
        ("ab", "El principio de precaución sugiere:", "Actuar con cuidado ante incertidumbre", "Ignorar los riesgos", "Se aplica cuando no se conocen bien los efectos."),
        ("ab", "Para concluir sobre efectos a largo plazo hacen falta:", "Estudios repetidos en el tiempo", "Un solo dato", "Se requieren varios años y lugares."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula cuántas plantas dañadas hay en cada parcela si cada una tiene 200; (2) escribe un beneficio y un riesgo o pregunta abierta; (3) escribe dos preguntas, una social y otra legal, que haría una comunidad antes de cultivar.",
        "(1) Convencional: 80 plantas; con resistencia: 20 plantas. (2) Beneficio: menos daño; pregunta abierta: efectos a largo plazo sobre otras especies. (3) Social: ¿cómo conviven con cultivos tradicionales? Legal: ¿qué normas regulan su cultivo y etiquetado?",
        ["cálculos correctos", "beneficio y riesgo o pregunta abierta", "una pregunta social y una legal"],
        ["tres respuestas numeradas"],
        ["calcular mal el porcentaje", "mencionar solo beneficios", "mezclar las dimensiones"],
        "Pregunta: «¿qué postura distinta a la tuya podría tener otra persona y por qué?»."),
    reinforce="Escribe una lista de tres beneficios posibles y tres preguntas abiertas sobre un cultivo con resistencia a una plaga.",
    extend="Explica por qué la universalidad del código genético permite producir proteínas de una especie en otra, y qué responsabilidades implica.",
)

# ============================================================ OAC-07, clase 5
F = ("Ficha 5 (caso de ejemplo para decidir). Un servicio de salud ficticio puede elegir entre dos políticas para una terapia dirigida nueva y costosa. Política 1: ofrecerla a un grupo pequeño, el de mayor riesgo, elegido por criterios médicos. "
     "Política 2: ofrecer una terapia menos eficaz pero más barata a un grupo mayor. Datos de ejemplo: la terapia nueva cuesta 10 unidades por persona y beneficia a 8 de cada 10 personas tratadas; la terapia más barata cuesta 2 unidades por persona y beneficia a 5 de cada 10. Presupuesto: 100 unidades. "
     "Principios de análisis: autonomía (decidir con información y libertad), beneficencia y no daño (buscar el bien y evitar daño), justicia (distribución justa de beneficios y cargas). Dimensión legal: derecho a la información, protección de datos y normas de acceso.")
build(
    O7, 5, F,
    use="Aprenderé a comparar soluciones frente a un dilema biotecnológico usando principios éticos, datos y normas, y a defender una decisión sin imponerla. Sirve para evaluar las implicancias éticas, sociales y legales de las aplicaciones de la biología molecular.",
    prior=["Conozco las dimensiones ética, social y legal.", "Sé calcular costos y porcentajes.", "Sé argumentar con evidencia."],
    explain=[
        "Un dilema ocurre cuando hay valores o principios que chocan y no existe una solución perfecta. Los principios más usados en bioética son: autonomía (las personas deciden con información suficiente y sin presiones), beneficencia y no daño (buscar el bien y evitar el daño) y justicia (repartir los beneficios y las cargas de forma justa). En un dilema, estos principios pueden dar respuestas distintas.",
        "Para comparar soluciones se siguen pasos: describir el caso y sus datos, identificar a las personas afectadas, aplicar los principios a cada opción, considerar las normas legales y declarar los supuestos y las incertidumbres. Los datos de costo y beneficio ayudan, pero no deciden solos: se necesitan juicios sobre qué es justo. Una buena decisión explica por qué prioriza ciertos principios.",
        "La dimensión legal incluye el derecho a recibir información clara, la protección de datos personales y las normas de acceso a los tratamientos. Las leyes cambian con el tiempo, por eso se deben consultar fuentes oficiales actualizadas. Argumentar bien es presentar la postura propia con razones y reconocer las posturas distintas con respeto.",
    ],
    vocab=[("dilema", "situación en que valores o principios chocan y no hay una solución perfecta"), ("autonomía", "derecho a decidir con información y sin presiones"), ("beneficencia", "buscar el bien de las personas"), ("justicia", "distribución justa de beneficios y cargas"), ("protección de datos", "resguardo de la información personal")],
    worked=[
        ("Calcular personas tratadas", "Con 100 unidades de presupuesto, ¿a cuántas personas se puede tratar con la terapia nueva?",
         ["Cada persona cuesta 10 unidades.", "100 ÷ 10 = 10."],
         "10 personas"),
        ("Calcular personas beneficiadas", "Con la terapia más barata (2 unidades por persona, benefician 5 de cada 10), ¿cuántas se tratan y cuántas se benefician con 100 unidades?",
         ["Se tratan 100 ÷ 2 = 50 personas.", "Se benefician 5 de cada 10: 50 × 5 ÷ 10 = 25."],
         "50 tratadas y 25 beneficiadas"),
    ],
    mistakes=[("Elegir la opción con mayor número de beneficiados sin considerar la justicia ni la autonomía.", "Los números no agotan lo que importa; hay principios que ponderar.", "Aplica los tres principios a cada opción."),
              ("Presentar una sola postura como la única posible.", "En un dilema hay posturas razonables distintas.", "Reconoce los argumentos de otras posturas.")],
    T=[
        ("abc", "En Biología celular y molecular: ¿qué es un dilema?", "Una situación en que valores o principios chocan y no hay solución perfecta", "Una pregunta con una sola respuesta", "Un tipo de gen", "Un dilema enfrenta valores que no se pueden satisfacer del todo."),
        ("{F} ¿Cuánto cuesta por persona la terapia nueva?", "10 unidades", "La ficha indica 10 unidades por persona."),
        ("{F} ¿Cuál es el presupuesto del servicio de salud de ejemplo?", "100 unidades", "La ficha fija un presupuesto de 100 unidades."),
        ("abc", "{F} ¿Qué principio se centra en repartir los beneficios y las cargas de forma justa?", "La justicia", "La autonomía", "La beneficencia", "La justicia trata de la distribución justa."),
        ("ab", "{F} ¿Qué principio protege que una persona decida con información suficiente?", "La autonomía", "La justicia", "La autonomía es el derecho a decidir informada y libremente."),
        ("{F} ¿Qué principio busca el bien de las personas y evitar el daño?", "La beneficencia y no daño", "Ese principio se orienta al bien y a evitar daño."),
        ("=", "{F} Si el presupuesto subiera a 150 unidades, ¿a cuántas personas se podría tratar con la terapia nueva?", "150/10", "Se divide el presupuesto por el costo por persona.", " personas"),
        ("=", "{F} Con la terapia nueva se tratan 10 personas y benefician 8 de cada 10. ¿Cuántas se benefician?", "10*8/10", "Se calcula la parte que se beneficia de las 10 personas tratadas.", " personas"),
        ("=", "{F} Con 150 unidades se tratan 15 personas con la terapia nueva, que beneficia a 8 de cada 10. ¿Cuántas se benefician?", "15*8/10", "Se calcula la parte que se beneficia de las 15 personas tratadas.", " personas"),
        ("abc", "{F} Al comparar los beneficiados, ¿cuántas personas más se benefician con la política 2 que con la política 1?", "17", "8", "25", "La política 2 beneficia a 25 y la 1 a 8, y la diferencia es 17."),
        ("abc", "{F} Una persona dice: «la política 2 es mejor porque beneficia a más gente». ¿Qué falta considerar?", "Que la terapia es menos eficaz por persona y que el principio de justicia y los criterios médicos también cuentan", "Nada: los números deciden", "Que el presupuesto no importa", "Los números no agotan el análisis ético."),
        ("ab", "{F} Un paciente quiere saber los riesgos de la terapia antes de aceptarla. ¿Qué principio respalda su petición?", "La autonomía, que exige información suficiente", "La justicia, que reparte el presupuesto", "Para decidir libremente, la persona necesita información clara."),
        ("abc", "{F} ¿Qué aspecto legal está en juego si el servicio guarda datos genéticos de las personas tratadas?", "La protección de datos personales", "El color de las etiquetas", "La temperatura del archivo", "Los datos genéticos son sensibles y requieren protección."),
    ],
    ctx=("abc", "Contexto: tu curso debe preparar una breve recomendación sobre el caso de la ficha para una conversación comunitaria. ¿Qué estructura es más sólida?", "Datos, personas afectadas, principios aplicados a cada opción, normas, supuestos y una decisión justificada", "Una opinión sin datos", "Copiar la postura de un medio de comunicación", "Una recomendación sólida integra datos, principios y límites."),
    sc=[
        ("En Biología celular y molecular: ¿qué es la autonomía?", "El derecho a decidir con información y sin presiones", "Es un principio ético central en salud."),
        ("ab", "En un dilema, los principios éticos:", "Pueden dar respuestas distintas", "Siempre coinciden", "Por eso hay que ponderarlos y justificar la decisión que se toma."),
        ("ab", "Una buena decisión debe:", "Explicar por qué prioriza ciertos principios", "Ocultar los argumentos contrarios", "Explicar las razones permite discutir con respeto."),
    ],
    op=("Con el caso de la ficha {F}: (1) calcula cuántas personas se tratan y cuántas se benefician con cada política; (2) aplica los tres principios a cada política en una tabla; (3) escribe tu decisión justificada y la mejor objeción a ella.",
        "(1) Política 1: 10 tratadas y 8 beneficiadas; política 2: 50 tratadas y 25 beneficiadas. (2) Tabla con autonomía, beneficencia y justicia para cada política. (3) Elijo una combinación que priorice la terapia nueva para el grupo de mayor riesgo y la barata para los demás; objeción: puede resultar compleja de administrar.",
        ["cálculos correctos", "tabla con los tres principios", "decisión justificada y objeción reconocida"],
        ["un cálculo, una tabla y una decisión"],
        ["calcular mal los beneficiados", "aplicar solo un principio", "no reconocer ninguna objeción"],
        "Pregunta: «¿qué dato nuevo te haría cambiar de decisión?»."),
    reinforce="Escribe un dilema inventado sobre biotecnología y aplica a él los tres principios.",
    extend="Explica por qué las leyes sobre biotecnología deben revisarse a medida que aparecen nuevos conocimientos.",
)
