"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 09 (consolidación republicana, debate y conflictos políticos)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 09"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (hechos y fechas de la consolidación de la república en Chile). "
     "1836–1839: guerra contra la Confederación Perú-Boliviana; el ministro Diego Portales fue asesinado en 1837; la batalla de Yungay, en 1839, dio la victoria a Chile. "
     "1843: toma de posesión del Estrecho de Magallanes. "
     "Presidentes de periodos de diez años: José Joaquín Prieto (1831–1841), Manuel Bulnes (1841–1851) y Manuel Montt (1851–1861). "
     "1850: Sociedad de la Igualdad. 1851 y 1859: revoluciones armadas. "
     "1863: formación del Partido Radical. "
     "Voto censitario: votaban solo los hombres que cumplían requisitos de renta o propiedad y sabían leer.")
build(
    OA, 1, F,
    use="Aprenderé a situar la consolidación de la república chilena en el tiempo y a plantear la pregunta que guía este tema: ¿cómo se consolidó el orden y qué debates y conflictos aparecieron?",
    prior=["Sé qué disponía la Constitución de 1833.", "Sé calcular diferencias entre años.", "Sé qué es el voto censitario."],
    explain=[
        "La consolidación de la república es el proceso por el cual el orden institucional se afianzó. Tuvo varios aspectos. Uno fue la defensa del territorio nacional: Chile enfrentó a la Confederación Perú-Boliviana entre 1836 y 1839 y tomó posesión del Estrecho de Magallanes en 1843. Otro fue la continuidad de gobiernos: los presidentes Prieto, Bulnes y Montt gobernaron cada uno diez años seguidos.",
        "Otro aspecto fue la institucionalización del debate político. Aparecieron partidos, la discusión en el Congreso y la prensa política. Sin embargo, el voto seguía siendo censitario, así que solo una minoría decidía. También persistieron conflictos: la crítica al centralismo y el debate sobre las atribuciones del Ejecutivo y del Legislativo llevaron a las revoluciones de 1851 y 1859.",
        "Situar este periodo exige separar etapas: el orden conservador de 1831–1861 y la apertura posterior. Hay que evitar el error de pensar que la consolidación significó ausencia de conflictos. Los conflictos estaban, pero se expresaban cada vez más por vías institucionales.",
    ],
    vocab=[("consolidación", "proceso en que algo se afirma y se hace estable"), ("Confederación Perú-Boliviana", "unión de Perú y Bolivia (1836–1839) que Chile combatió"), ("decenio", "periodo de diez años"), ("institucionalización", "proceso por el que algo se organiza dentro de reglas e instituciones"), ("partido político", "organización que busca ejercer el poder con un proyecto común")],
    worked=[
        ("Calcular la duración", "¿Cuántos años gobernó Prieto, de 1831 a 1841?", ["Tomo los años de la ficha.", "Resto: 1841 − 1831 = 10."], "10 años"),
        ("Calcular un intervalo", "¿Cuántos años pasaron entre la Sociedad de la Igualdad (1850) y la formación del Partido Radical (1863)?", ["Tomo los dos años de la ficha.", "Resto: 1863 − 1850 = 13."], "13 años"),
    ],
    mistakes=[("Decir que la consolidación fue una etapa sin conflictos.", "Hubo revoluciones en 1851 y 1859.", "Menciona los conflictos."),
              ("Confundir la guerra contra la Confederación con la Guerra del Pacífico.", "Son conflictos distintos y de épocas diferentes.", "Usa las fechas: 1836–1839.")],
    T=[
        ("{F} ¿Quién fue asesinado en 1837?", "Diego Portales", "La ficha lo indica."),
        ("{F} ¿Qué batalla dio la victoria a Chile en 1839?", "Yungay", "La ficha la nombra."),
        ("{F} ¿En qué año se tomó posesión del Estrecho de Magallanes?", "1843", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años gobernó Bulnes?", "1851-1841", "Se resta el año de inicio al del término.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el inicio de la guerra con la Confederación (1836) y las revoluciones de 1851?", "1851-1836", "Se resta el año del inicio al de la revolución.", " años"),
        ("{F} ¿Qué presidente gobernó primero? A) Prieto B) Montt", "A) Prieto", "Prieto gobernó 1831–1841 y Montt 1851–1861."),
        ("{F} ¿Qué hecho corresponde a la defensa del territorio? A) La guerra contra la Confederación Perú-Boliviana B) La formación del Partido Radical", "A) La guerra contra la Confederación Perú-Boliviana", "Defendía la seguridad del país."),
        ("{F} ¿Qué hecho corresponde al debate político institucionalizado? A) La formación del Partido Radical B) La batalla de Yungay", "A) La formación del Partido Radical", "Es una organización política."),
        ("{F} ¿Qué hecho muestra un conflicto armado interno? A) Las revoluciones de 1851 y 1859 B) El Estrecho de Magallanes", "A) Las revoluciones de 1851 y 1859", "Fueron levantamientos contra el gobierno."),
        ("{F} ¿Por qué se dice que el voto censitario limitaba la república?", "Porque solo una minoría de hombres con renta o propiedad votaba", "El resto no participaba."),
        ("{F} Un compañero dice: «Entre 1831 y 1861 no hubo conflictos». Corrígelo.", "Hubo revoluciones en 1851 y 1859", "La consolidación tuvo conflictos."),
        ("{F} ¿Cuál es la mejor pregunta histórica? A) ¿Cómo se consolidó la república y qué debates y conflictos aparecieron? B) ¿Qué presidente fue el mejor de todos?", "A) ¿Cómo se consolidó la república y qué debates y conflictos aparecieron?", "La A se responde con hechos."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y va de 1830 a 1870. ¿Cuántos centímetros mide?", "4 cm", "Se divide el tramo de 40 años por 10."),
    ],
    ctx=("Un afiche escolar titula «La consolidación republicana: 30 años sin ningún problema». ¿Cómo lo corriges? A) Hubo orden institucional, pero también revoluciones y críticas al centralismo B) Es correcto", "A) Hubo orden institucional, pero también revoluciones y críticas al centralismo", "La ficha muestra conflictos en 1851 y 1859."),
    sc=[("¿Qué es un decenio?", "Un periodo de diez años", "Así se define."),
        ("¿Qué fue Yungay?", "La batalla de 1839 que dio la victoria a Chile", "Cierra la guerra con la Confederación."),
        ("=", "¿Cuántos años pasaron entre 1837 y 1843?", "1843-1837", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1830 a 1870 con escala 1 cm = 10 años y marca: Prieto (1831), guerra con la Confederación (1836), Yungay (1839), Estrecho (1843), Sociedad de la Igualdad (1850), revolución (1851), revolución (1859) y Partido Radical (1863). Debajo escribe una frase que explique qué significa consolidar la república. {F}",
        "Posiciones desde 1830: 0,1; 0,6; 0,9; 1,3; 2; 2,1; 2,9; 3,3 cm. Frase: «Consolidar es afirmar un orden institucional estable, con debates y conflictos».",
        ["respeta la escala", "los ocho hitos bien ubicados", "la definición es correcta"], ["línea de tiempo", "una frase"], ["no medir con la escala", "olvidar los conflictos"],
        "Pide que explique por qué hubo conflictos aunque el orden era estable."),
    reinforce="Explica en voz alta tres hechos de la consolidación republicana.",
    extend="Busca en tu ciudad una calle, plaza o monumento que recuerde la batalla de Yungay y anota qué dice.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, editorial de un periódico opositor, 1850: «El gobierno decide todo y el Congreso solo obedece. Pedimos que las elecciones sean libres y que las provincias puedan opinar.» "
     "Fuente B, discurso de un senador oficialista, 1858: «El orden que tenemos nos ha dado paz y progreso. Un Ejecutivo fuerte evita la anarquía que conocimos en los años 1820.» "
     "Fuente C, resumen de ejemplo de una ley electoral de 1874: votan los hombres adultos que sepan leer y escribir.")
build(
    OA, 2, F,
    use="Aprenderé a contextualizar y comparar fuentes de la consolidación republicana: un editorial opositor, un discurso oficialista y una ley electoral.",
    prior=["Sé qué visiones había sobre el poder.", "Sé contextualizar una fuente.", "Sé separar descripción de interpretación."],
    explain=[
        "Un editorial opositor expresa la crítica de un periódico al gobierno. Un discurso parlamentario muestra el debate político dentro de las instituciones. Una ley electoral es una fuente normativa: fija reglas sobre quién puede votar. Cada una informa algo distinto, y juntas muestran que el debate político se había institucionalizado.",
        "Para comparar, se contextualiza cada fuente. El editorial de 1850 critica que el gobierno decide todo y pide elecciones libres. El discurso de 1858 defiende un Ejecutivo fuerte por su experiencia de paz. La ley de 1874 amplía el voto: en la práctica reemplaza el requisito de renta o propiedad por saber leer y escribir. Esto muestra que el sistema cambió con las presiones.",
        "Cada fuente tiene límites: las dos primeras expresan la postura de grupos, y la tercera describe una regla, no cuántos votaron en la práctica. Una conclusión debe ser proporcional: mostrar los argumentos del debate y reconocer que faltan voces, por ejemplo las de quienes no podían votar.",
    ],
    vocab=[("oficialista", "que apoya al gobierno"), ("opositor", "que se opone al gobierno"), ("anarquía", "ausencia de autoridad que genera desorden"), ("ley electoral", "ley que regula quién vota y cómo se elige"), ("alfabetismo", "capacidad de leer y escribir")],
    worked=[
        ("Contextualizar", "¿Quién escribe la Fuente B, cuándo y para qué?", ["Autor: un senador oficialista.", "Fecha: 1858. Propósito: defender el Ejecutivo fuerte."], "Un senador oficialista, en 1858, para defender el Ejecutivo fuerte"),
        ("Calcular una diferencia", "¿Cuántos años pasaron entre el editorial de 1850 y la ley de 1874?", ["Tomo los dos años de la ficha.", "Resto: 1874 − 1850 = 24."], "24 años"),
    ],
    mistakes=[("Tomar el discurso del senador como la opinión de todo el país.", "Expresa la postura de los oficialistas.", "Escribe «este senador defendía»."),
              ("Creer que la ley de 1874 hizo votar a toda la población.", "Seguían sin votar las mujeres y quienes no sabían leer.", "Lee quién podía votar.")],
    T=[
        ("{F} ¿Qué critica el editorial de 1850?", "Que el gobierno decide todo y el Congreso solo obedece", "El texto lo dice."),
        ("{F} ¿Qué defiende el senador de 1858?", "Un Ejecutivo fuerte para evitar la anarquía", "El discurso lo dice."),
        ("{F} ¿Qué pide la ley electoral de 1874?", "Ser hombre adulto y saber leer y escribir", "La Fuente C lo indica."),
        ("=", "{F} ¿Cuántos años separan la Fuente A de la Fuente B?", "1858-1850", "Se resta el año del editorial al del discurso.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Fuente B y la Fuente C?", "1874-1858", "Se resta el año del discurso al de la ley.", " años"),
        ("{F} ¿Qué fuente es oficialista? A) La Fuente B B) La Fuente A", "A) La Fuente B", "Defiende el orden vigente."),
        ("{F} ¿Qué fuente es normativa? A) La Fuente C B) La Fuente A", "A) La Fuente C", "Fija reglas electorales."),
        ("{F} ¿Qué frase describe la Fuente C? A) Votan hombres adultos que sepan leer y escribir B) Votan todas las personas adultas", "A) Votan hombres adultos que sepan leer y escribir", "El resumen lo indica."),
        ("{F} ¿Qué cambió en la ley de 1874 respecto al voto censitario? A) Ya no pide renta o propiedad, sino saber leer y escribir B) Exige tener propiedades y saber leer", "A) Ya no pide renta o propiedad, sino saber leer y escribir", "El requisito económico se reemplaza por el alfabetismo."),
        ("{F} ¿Por qué el discurso del senador no prueba que todos estaban conformes?", "Porque expresa la postura de los oficialistas y hay críticas como la del editorial", "Es la voz de un grupo."),
        ("{F} Un compañero concluye: «Con la ley de 1874 todos podían votar». ¿Qué corrección haces?", "La ley exigía ser hombre adulto y saber leer y escribir", "Seguían excluidas las mujeres y quienes no sabían leer."),
        ("{F} ¿Qué voz falta en las tres fuentes? A) La de quienes no podían votar B) La de otro senador", "A) La de quienes no podían votar", "Ninguna fuente las incluye."),
        ("{F} ¿Qué conclusión es más proporcional? A) Las fuentes muestran críticas al poder del Ejecutivo, su defensa y una ampliación del voto limitada B) Las fuentes prueban lo que pensaba todo el país", "A) Las fuentes muestran críticas al poder del Ejecutivo, su defensa y una ampliación del voto limitada", "No dice más de lo que muestran."),
    ],
    ctx=("Para una exposición sobre el debate político, un grupo solo cita el discurso del senador oficialista. ¿Qué suman para mostrar el debate? A) El editorial opositor B) Otro discurso oficialista", "A) El editorial opositor", "Presenta la crítica al gobierno."),
    sc=[("¿Qué es un oficialista?", "Quien apoya al gobierno", "Así se define."),
        ("¿Qué es una ley electoral?", "Una ley que regula quién vota y cómo se elige", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1874 y 1900?", "1900-1874", "Se resta el año menor al mayor.", " años")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (una frase); qué interpretas (con «Esto sugiere que…»). Cierra con qué no puedes concluir y qué voz falta. {F}",
        "Fuente A. Autor y fecha: un periódico opositor, 1850. Dice: el gobierno decide todo y pide elecciones libres. Interpretación: esto sugiere que había críticas al poder del Ejecutivo. No puedo concluir que todos pensaran así; falta la voz de quienes no votaban.",
        ["contextualiza", "separa descripción e interpretación", "señala límite y voz ausente"], ["tabla de tres filas", "frase de cierre"], ["usar un juicio como descripción", "generalizar"],
        "Pide que diga qué respondería el senador al editorial."),
    reinforce="Explica por qué un editorial, un discurso y una ley electoral informan cosas distintas.",
    extend="Busca un titular de diario actual sobre una elección y anota si es descripción u opinión.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de cambio, continuidad y territorio; cifras de ejemplo redondeadas). "
     "Voto: en 1833 votaban hombres con renta o propiedad que sabían leer; en 1874 bastaba, en la práctica, ser hombre adulto y saber leer y escribir. "
     "Cifras de ejemplo: en una elección de 1860, 20.000 personas inscritas para votar en un país de 1.500.000 habitantes. "
     "Territorio: Chile defendió su soberanía en el sur al tomar posesión del Estrecho de Magallanes en 1843 y enfrentó a la Confederación Perú-Boliviana en el norte, 1836–1839. "
     "Centralismo: las decisiones importantes se tomaban en Santiago; en 1851 hubo levantamientos, entre ellos uno que surgió en Concepción, y en 1859 otro en el norte, en Atacama y Coquimbo.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio en la consolidación republicana: voto, defensa del territorio y centralismo.",
    prior=["Sé qué es el voto censitario.", "Sé calcular porcentajes simples.", "Sé leer un cuadro de datos."],
    explain=[
        "En la consolidación, el voto cambió poco a poco. En 1833 se exigía renta o propiedad. En 1874 bastaba saber leer y escribir. Aun así, el número de votantes era pequeño en relación con la población. Con las cifras de ejemplo, 20.000 inscritos sobre 1.500.000 habitantes son cerca de un 1,3 %. Este cálculo muestra que la participación política era limitada.",
        "El territorio es clave. En el sur, Chile tomó posesión del Estrecho de Magallanes en 1843, lo que fortaleció su soberanía. En el norte enfrentó a la Confederación Perú-Boliviana. Estos hechos son parte de la defensa del territorio nacional. Pero dentro del país hubo tensiones: el centralismo hacía que las decisiones se tomaran en Santiago, y las revoluciones de 1851 y 1859 surgieron en provincias.",
        "Hay cambios y continuidades. Cambió el requisito del voto y se institucionalizó el debate. Continuó el centralismo y la limitación de la participación. Analizar ambos permite ver que la consolidación fue un equilibrio entre orden y reclamos de apertura, y no un proceso lineal.",
    ],
    vocab=[("participación electoral", "porcentaje de la población que vota o puede votar"), ("soberanía", "poder supremo de un Estado sobre su territorio"), ("inscrito", "persona registrada para poder votar"), ("provincia", "división territorial del país"), ("equilibrio", "situación en que fuerzas opuestas se compensan")],
    worked=[
        ("Calcular el porcentaje", "Con las cifras de ejemplo, ¿qué porcentaje de 1.500.000 habitantes son 20.000 inscritos?", ["Divido 20.000 entre 1.500.000: da 0,0133.", "Multiplico por 100: aproximadamente 1,3 %."], "Aproximadamente 1,3 %"),
        ("Clasificar", "«Las decisiones importantes siguieron tomándose en Santiago.» ¿Cambio o continuidad?", ["Esto venía de antes.", "Se mantuvo."], "Continuidad"),
    ],
    mistakes=[("Pensar que el cambio del requisito del voto significó participación masiva.", "Los inscritos siguieron siendo una pequeña parte.", "Calcula el porcentaje."),
              ("Olvidar que las revoluciones surgieron en provincias.", "Muestran la crítica al centralismo.", "Relaciona revoluciones y territorio.")],
    T=[
        ("{F} ¿Qué requisito pedía el voto en 1874?", "Ser hombre adulto y saber leer y escribir", "La ficha lo indica."),
        ("{F} ¿En qué ciudad surgió uno de los levantamientos de 1851, según la ficha?", "Concepción", "La ficha lo indica."),
        ("{F} ¿Dónde se tomó posesión del Estrecho de Magallanes?", "En el sur de Chile", "La ficha lo señala."),
        ("=", "{F} Con las cifras de ejemplo, si 20.000 personas están inscritas y la población es de 1.500.000, ¿cuántas personas no están inscritas?", "1500000-20000", "Se resta el número de inscritos al total.", " personas"),
        ("=", "{F} ¿Cuántos años pasaron entre la toma del Estrecho y la revolución de 1859?", "1859-1843", "Se resta el año del Estrecho al de la revolución.", " años"),
        ("{F} ¿Qué es un cambio? A) El requisito del voto cambió de renta o propiedad a saber leer y escribir B) Las decisiones siguieron en Santiago", "A) El requisito del voto cambió de renta o propiedad a saber leer y escribir", "La B es una continuidad."),
        ("{F} ¿Qué es una continuidad? A) El centralismo se mantuvo B) Se amplió el voto", "A) El centralismo se mantuvo", "Es algo que continuó."),
        ("{F} ¿Qué hecho fortaleció la soberanía en el sur? A) La toma de posesión del Estrecho de Magallanes B) La batalla de Yungay", "A) La toma de posesión del Estrecho de Magallanes", "La ficha lo señala."),
        ("{F} ¿Dónde surgió la revolución de 1859? A) En el norte B) En Santiago", "A) En el norte", "La ficha menciona Atacama y Coquimbo."),
        ("{F} ¿Por qué las revoluciones se relacionan con el centralismo?", "Porque surgieron en provincias que reclamaban más voz frente a las decisiones de Santiago", "La ficha las ubica fuera de la capital."),
        ("{F} Un compañero dice: «Con la ley de 1874 votó la mayoría de la población». Refútalo.", "El requisito seguía excluyendo a las mujeres y a quienes no sabían leer, y los inscritos eran pocos", "La participación política era limitada."),
        ("{F} ¿Qué mide la participación electoral? A) Qué parte de la población vota o puede votar B) Cuántos políticos hay", "A) Qué parte de la población vota o puede votar", "Así se define."),
        ("{F} ¿Qué conclusión es más ajustada? A) Cambió el requisito del voto y se defendió el territorio, pero el centralismo y la baja participación continuaron B) Todo cambió", "A) Cambió el requisito del voto y se defendió el territorio, pero el centralismo y la baja participación continuaron", "Reúne cambio y continuidad."),
    ],
    ctx=("Un compañero concluye que «el 1,3 % de inscritos significa que casi todos votaban». ¿Qué le respondes? A) 1,3 % es una proporción muy pequeña: casi nadie votaba B) Es una proporción muy grande", "A) 1,3 % es una proporción muy pequeña: casi nadie votaba", "Un 1,3 % es mucho menor que la mitad."),
    sc=[("¿Qué es la participación electoral?", "La parte de la población que vota o puede votar", "Así se define."),
        ("¿Qué es el centralismo?", "La concentración de las decisiones en la capital", "Así se define."),
        ("=", "Si una comuna de ejemplo tiene 1.000.000 de habitantes y 20.000 inscritos, ¿cuántos no están inscritos?", "1000000-20000", "Se resta el número de inscritos al total.", " personas")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», y escribe tres datos en cada una con la ficha. Luego dibuja un esquema simple de Chile con tres puntos: «Santiago», «Concepción» (revolución 1851) y «Norte» (revolución 1859), con flechas de reclamo hacia Santiago. {F}",
        "Cambió: requisito del voto; defensa del territorio; debate político. Continuó: centralismo; baja participación; Ejecutivo fuerte. Esquema: flechas desde Concepción y Norte hacia Santiago.",
        ["usa datos de la ficha", "separa cambio y continuidad", "esquema de centralismo"], ["tabla completa", "esquema"], ["mezclar cambio y continuidad", "olvidar un punto"],
        "Pide que diga qué región crees que se sentía más lejos de las decisiones."),
    reinforce="Explica en voz alta un cambio, una continuidad y cómo el territorio muestra el centralismo.",
    extend="Averigua cuántos habitantes tiene tu comuna y calcula qué porcentaje es 20.000 personas.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Gobernante conservador, 1855: «El Ejecutivo debe tener autoridad para defender el orden, el territorio y la paz.» "
     "Liberal opositor, 1857: «El presidente interviene en las elecciones y el Congreso pierde independencia. Hay que limitar al Ejecutivo.» "
     "Provinciano, 1858: «Los impuestos salen de nuestra provincia, pero las decisiones se toman en la capital.» "
     "Artesano de la Sociedad de la Igualdad, 1850: «Queremos que los trabajadores tengan voz y puedan votar aunque no tengan propiedades.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores y perspectivas en los conflictos de la consolidación: gobierno, oposición liberal, provincias y sectores populares.",
    prior=["Sé qué debates había sobre el poder.", "Sé contextualizar fuentes.", "Sé que cada actor tiene intereses."],
    explain=[
        "Los conflictos de la consolidación enfrentaron a actores con intereses distintos. El gobernante conservador defendía un Ejecutivo fuerte para el orden. El liberal opositor criticaba que el presidente interviniera en las elecciones y quería limitar al Ejecutivo. El provinciano reclamaba que los impuestos salieran de su provincia, pero las decisiones se tomaran en la capital. El artesano de la Sociedad de la Igualdad pedía voz y voto para los trabajadores.",
        "Dos debates sobresalen. Uno es el debate sobre las atribuciones del Ejecutivo y el Legislativo: cuánto poder debe tener el presidente y cuánto el Congreso. Otro es la crítica al centralismo. Los dos explican por qué hubo revoluciones en 1851 y 1859, y por qué después se hicieron reformas que redujeron las atribuciones del presidente.",
        "Contrastar significa comparar qué quiere cada actor, qué le conviene y qué teme. El gobernante teme el desorden; el liberal, el abuso de poder; el provinciano, quedarse sin voz; el artesano, seguir excluido. Una buena explicación no elige un bando sin evidencia: muestra cómo la disputa fue moldeando las instituciones.",
    ],
    vocab=[("atribuciones", "poderes que la ley da a una autoridad"), ("independencia del Congreso", "capacidad del Congreso de decidir sin presión del presidente"), ("intervención electoral", "uso del poder del gobierno para influir en una elección"), ("Sociedad de la Igualdad", "organización de 1850 que pedía derechos políticos y sociales para sectores populares"), ("reclamo", "petición de cambio por considerar injusta una situación")],
    worked=[
        ("Quién critica la intervención", "¿Qué actor critica la intervención del presidente en las elecciones?", ["Busco una voz que hable de elecciones.", "El liberal opositor."], "El liberal opositor"),
        ("Quién reclama voz", "¿Qué actor pide que los trabajadores voten aunque no tengan propiedades?", ["Busco una voz que hable del voto sin propiedades.", "El artesano de la Sociedad de la Igualdad."], "El artesano de la Sociedad de la Igualdad"),
    ],
    mistakes=[("Explicar los conflictos solo con la voz del gobierno.", "Se ignoran la oposición, las provincias y los sectores populares.", "Incluye al menos tres voces."),
              ("Pensar que todos pedían lo mismo.", "Unos pedían menos Ejecutivo, otros autonomía y otros voto.", "Distingue cada petición.")],
    T=[
        ("{F} ¿Qué defiende el gobernante conservador?", "Un Ejecutivo con autoridad para defender el orden, el territorio y la paz", "Su voz lo dice."),
        ("{F} ¿Qué critica el liberal opositor?", "Que el presidente interviene en las elecciones y el Congreso pierde independencia", "Su voz lo dice."),
        ("{F} ¿Qué reclama el provinciano?", "Que los impuestos salen de su provincia pero las decisiones se toman en la capital", "Su voz lo dice."),
        ("{F} ¿Qué pide el artesano?", "Voz y voto para los trabajadores aunque no tengan propiedades", "Su voz lo dice."),
        ("{F} ¿Qué actor teme el desorden? A) El gobernante conservador B) El artesano", "A) El gobernante conservador", "Defiende el orden."),
        ("{F} ¿Qué actor critica el centralismo? A) El provinciano B) El gobernante", "A) El provinciano", "Quiere decisiones fuera de la capital."),
        ("{F} ¿Qué actor quiere limitar al Ejecutivo? A) El liberal opositor B) El gobernante", "A) El liberal opositor", "Su voz lo pide."),
        ("{F} ¿Qué actor busca ampliar el voto? A) El artesano B) El gobernante", "A) El artesano", "Pide voto sin propiedades."),
        ("{F} ¿Por qué el gobernante y el liberal ven distinto el poder del presidente?", "Porque uno teme el desorden y el otro el abuso de poder", "Sus temores son opuestos."),
        ("{F} Un compañero dice: «Todos aceptaban el poder del Ejecutivo». Refútalo.", "El liberal quería limitarlo y el provinciano criticaba el centralismo", "Hubo críticas al poder del Ejecutivo."),
        ("{F} ¿Qué voz falta para completar la perspectiva de los excluidos del voto? A) La de una mujer que no podía votar B) La de otro gobernante", "A) La de una mujer que no podía votar", "Ningún actor de la ficha es mujer."),
        ("{F} ¿Qué conclusión es más equilibrada? A) Los conflictos mostraron visiones distintas sobre el poder, el territorio y el voto B) Todos tenían el mismo interés", "A) Los conflictos mostraron visiones distintas sobre el poder, el territorio y el voto", "Reúne las cuatro voces."),
        ("{F} ¿Qué pregunta ayuda a contrastar actores? A) ¿Qué quiere, qué le conviene y qué teme cada uno? B) ¿Qué actor tiene la razón y cuál se equivoca?", "A) ¿Qué quiere, qué le conviene y qué teme cada uno?", "Es el método de contraste."),
    ],
    ctx=("En un debate escolar, un grupo defiende un presidente con más poder y otro defiende un Congreso más fuerte. ¿Qué voz usa el segundo grupo? A) La del liberal opositor B) La del gobernante conservador", "A) La del liberal opositor", "Pide limitar al Ejecutivo."),
    sc=[("En el debate sobre el Ejecutivo y el Legislativo, ¿a qué se llama atribuciones de un presidente?", "A los poderes que la ley le da", "Así se aplica el término en la clase."),
        ("¿Qué actor critica la intervención electoral?", "El liberal opositor", "Su voz lo dice."),
        ("¿Qué es un reclamo?", "Una petición de cambio por considerar injusta una situación", "Así se define.")],
    op=("Elige dos actores de la ficha y haz una tabla con: qué quiere, qué le conviene y qué teme. Después escribe tres líneas sobre por qué sus perspectivas chocan. {F}",
        "Gobernante: quiere orden; le conviene un Ejecutivo fuerte; teme el desorden. Provinciano: quiere voz; le conviene descentralizar; teme quedar sin decisión. Texto: «Uno quiere concentrar el poder para el orden y el otro repartirlo; por eso chocan».",
        ["elige dos actores", "tres columnas completas", "explica el choque"], ["tabla completa", "tres líneas"], ["mezclar voces", "opinar sin base"],
        "Pide que diga qué reforma satisfaría a ambos actores."),
    reinforce="Elige un actor y explica en voz alta qué pedía y qué temía.",
    extend="Piensa en una decisión de tu colegio donde unos quieren más control y otros más participación, y nombra a dos actores.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento). "
     "Pregunta: ¿cómo se consolidó la república en Chile y qué conflictos persistieron? "
     "Dato 1: Chile defendió su territorio frente a la Confederación Perú-Boliviana (1836–1839) y tomó posesión del Estrecho de Magallanes (1843). "
     "Dato 2: tres presidentes gobernaron diez años cada uno entre 1831 y 1861. "
     "Dato 3: se institucionalizó el debate político, con partidos, discusión parlamentaria y prensa política. "
     "Dato 4: el voto siguió siendo restringido a una minoría; en 1874 bastaba saber leer y escribir. "
     "Dato 5: hubo revoluciones en 1851 y 1859, por la crítica al centralismo y al poder del Ejecutivo.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre la consolidación republicana: afirmación, evidencia, razonamiento y conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé contrastar actores.", "Sé qué conflictos hubo."],
    explain=[
        "Un argumento sobre la consolidación puede afirmar: «la república se consolidó por la defensa del territorio, la continuidad de gobiernos y la institucionalización del debate, aunque persistieron conflictos». La evidencia son los datos: las guerras y la toma del Estrecho, los tres gobiernos de diez años, los partidos y la prensa, el voto restringido y las revoluciones.",
        "El razonamiento explica cómo cada dato apoya la afirmación. El dato 1 muestra que el Estado afirmó su soberanía. El dato 2, que hubo continuidad de gobierno. El dato 3, que el conflicto se expresaba en instituciones. El dato 4 es un límite: participaba una minoría. El dato 5 muestra que persistieron los conflictos.",
        "Para que sea proporcional, hay que decir que la consolidación fue relativa: el orden se afirmó pero con conflictos. Un contraargumento posible es que las revoluciones de 1851 y 1859 muestran que no hubo consolidación; se responde mostrando que el sistema resistió y después se reformó.",
    ],
    vocab=[("consolidación", "proceso en que algo se afirma y se hace estable"), ("institucionalizar", "organizar dentro de reglas e instituciones"), ("persistir", "continuar a lo largo del tiempo"), ("afirmación", "respuesta que defiendes a una pregunta"), ("contraargumento", "dato o idea que podría contradecir la afirmación")],
    worked=[
        ("Elegir evidencia de soberanía", "¿Qué dato muestra la defensa del territorio?", ["Busco un dato sobre territorio.", "El dato 1."], "Dato 1"),
        ("Elegir evidencia de conflicto", "¿Qué dato muestra que persistieron los conflictos?", ["Busco un dato sobre revoluciones.", "El dato 5."], "Dato 5"),
    ],
    mistakes=[("Decir que la consolidación terminó con los conflictos.", "Hubo revoluciones en 1851 y 1859.", "Menciona el dato 5."),
              ("Citar un dato sin explicar el vínculo.", "Falta el razonamiento.", "Agrega «Esto muestra que…».")],
    T=[
        ("{F} ¿Qué dato muestra continuidad de gobierno?", "El dato 2, tres presidentes de diez años cada uno", "Es una sucesión ordenada."),
        ("{F} ¿Qué dato muestra el debate institucionalizado?", "El dato 3, partidos, Congreso y prensa política", "Son formas de debate organizado."),
        ("{F} ¿Qué dato muestra un límite de la participación?", "El dato 4, voto restringido a una minoría", "Pocos decidían en las elecciones."),
        ("=", "{F} Si cada uno de los tres presidentes gobierna diez años, ¿cuántos años suman?", "10*3", "Se multiplica la duración por tres presidentes.", " años"),
        ("{F} ¿Qué afirmación responde la pregunta? A) La república se consolidó con defensa del territorio, continuidad de gobiernos y debate institucional, aunque persistieron conflictos B) La república no se consolidó", "A) La república se consolidó con defensa del territorio, continuidad de gobiernos y debate institucional, aunque persistieron conflictos", "Se apoya en los cinco datos."),
        ("{F} ¿Qué dato sirve de contraargumento a la idea de una consolidación sin conflictos? A) El dato 5 B) El dato 2", "A) El dato 5", "Muestra que hubo revoluciones armadas."),
        ("{F} Completa el razonamiento: «El dato 3 muestra que…» A) el conflicto se expresaba en instituciones y no solo en armas B) no había debate", "A) el conflicto se expresaba en instituciones y no solo en armas", "Conecta el dato con la afirmación."),
        ("{F} Un compañero escribe: «Con la consolidación todos pudieron votar». ¿Qué dato lo contradice?", "El dato 4, voto restringido a una minoría", "Muestra que muchos quedaban excluidos."),
        ("{F} ¿Por qué el dato 5 no anula la idea de consolidación?", "Porque el sistema resistió los conflictos y luego se reformó", "Las instituciones sobrevivieron."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «relativa» B) «total»", "A) «relativa»", "Refleja conflictos y límites."),
        ("{F} Ordena las partes de un argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y se explica."),
        ("{F} ¿Qué dato falta para incluir la voz de las provincias? A) Un dato sobre los reclamos de provincias frente al centralismo B) Otro dato del Estrecho", "A) Un dato sobre los reclamos de provincias frente al centralismo", "Aporta una perspectiva ausente."),
        ("{F} ¿Qué conclusión se ajusta mejor a los datos? A) La consolidación fue relativa: hubo orden y debate institucional, pero con participación limitada y conflictos persistentes B) La consolidación fue total", "A) La consolidación fue relativa: hubo orden y debate institucional, pero con participación limitada y conflictos persistentes", "Reúne los datos."),
    ],
    ctx=("Un diario escolar publica: «La consolidación republicana fue un periodo de paz total». ¿Qué evidencia de la ficha usas para responder? A) El dato 5, las revoluciones de 1851 y 1859 B) El dato 2 solo", "A) El dato 5, las revoluciones de 1851 y 1859", "Muestra que hubo conflictos políticos."),
    sc=[("Menciona las tres partes de un argumento sobre la consolidación republicana.", "Afirmación, evidencia y razonamiento", "Son las partes enseñadas en la clase."),
        ("En Historia: ¿Qué significa persistir?", "Continuar a lo largo del tiempo", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1859 y 1874?", "1874-1859", "Se resta el año menor al mayor.", " años")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Cómo se consolidó la república en Chile y qué conflictos persistieron?». Usa al menos tres datos de la ficha, incluye el dato 4 o 5 como límite y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«La república se consolidó de forma relativa. Chile defendió su territorio, hubo tres presidentes de diez años y el debate se institucionalizó con partidos y prensa. Sin embargo, el voto estaba restringido y hubo revoluciones en 1851 y 1859, por la crítica al centralismo y al poder del Ejecutivo».",
        ["responde la pregunta", "usa tres datos y un límite", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["no incluir conflictos", "no explicar el vínculo"],
        "Pide que diga qué dato nuevo le gustaría conocer."),
    reinforce="Explica en voz alta tres factores de la consolidación y un conflicto que persistió.",
    extend="Escribe un contraargumento y respóndelo con un dato de la ficha.",
)
