"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 08 (formación de la República de Chile y Constitución de 1833)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 08"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (hechos y fechas de la formación de la República de Chile). "
     "1810: Primera Junta Nacional de Gobierno, el 18 de septiembre. "
     "1814: Desastre de Rancagua y comienzo de la Reconquista española. "
     "1817: batalla de Chacabuco; Bernardo O'Higgins queda como Director Supremo. "
     "1818: Declaración de Independencia y batalla de Maipú. "
     "1823: O'Higgins deja el poder. "
     "1822, 1823 y 1828: textos constitucionales que no lograron estabilidad. "
     "1830: batalla de Lircay. "
     "1833: Constitución que rigió hasta 1925. "
     "Visiones: liberales (llamados pipiolos), que querían más libertades y menos poder concentrado; conservadores (llamados pelucones), que querían orden y autoridad fuerte; federalistas, que querían provincias con más autonomía.")
build(
    OA, 1, F,
    use="Aprenderé a situar la formación de la República de Chile en el tiempo, y a plantear la pregunta que guía este tema: ¿cómo se organizó el país y por qué la Constitución de 1833 dio estabilidad?",
    prior=["Sé qué es el republicanismo y el liberalismo.", "Sé qué es una constitución.", "Sé calcular diferencias entre años."],
    explain=[
        "Después de la Primera Junta de 1810 y de la Independencia de 1818, Chile debía decidir cómo organizarse. No había un solo proyecto: había visiones distintas. Los liberales, llamados pipiolos, querían más libertades y limitar el poder del gobierno. Los conservadores, llamados pelucones, querían orden y un Ejecutivo fuerte. Los federalistas querían que las provincias tuvieran más autonomía.",
        "Entre 1822 y 1828 se escribieron varias constituciones que no lograron estabilidad. Hubo conflictos entre grupos y una guerra civil en 1829–1830, que terminó con la batalla de Lircay. Los conservadores ganaron, y desde ahí se redactó la Constitución de 1833, que rigió hasta 1925, es decir, durante muchas décadas. Esa duración la hace un caso de relativa estabilidad en América Latina.",
        "Situar el proceso exige separar etapas: independencia (1810–1818), ensayos de organización (1818–1830) y orden conservador (desde 1830). Hay que evitar el error de pensar que la república nació completa en 1818 o que todos los chilenos pensaban lo mismo sobre cómo gobernar el país.",
    ],
    vocab=[("Director Supremo", "cargo con poder ejecutivo máximo en los primeros años de la república"), ("pipiolos", "grupo liberal que quería más libertades y poder menos concentrado"), ("pelucones", "grupo conservador que quería orden y un Ejecutivo fuerte"), ("federalismo", "sistema donde las provincias tienen autonomía dentro del país"), ("estabilidad política", "situación en que las instituciones funcionan sin cambios violentos")],
    worked=[
        ("Calcular un intervalo", "¿Cuántos años pasaron entre la Primera Junta (1810) y la Declaración de Independencia (1818)?", ["Tomo los dos años de la ficha.", "Resto: 1818 − 1810 = 8."], "8 años"),
        ("Calcular otro intervalo", "¿Cuántos años pasaron entre la batalla de Maipú (1818) y la batalla de Lircay (1830)?", ["Tomo los dos años de la ficha.", "Resto: 1830 − 1818 = 12."], "12 años"),
    ],
    mistakes=[("Decir que la república quedó organizada en 1818.", "Después de la Independencia hubo ensayos constitucionales y conflictos.", "Separa independencia y organización."),
              ("Creer que todos pensaban igual.", "Había pipiolos, pelucones y federalistas.", "Nombra al menos dos visiones.")],
    T=[
        ("{F} ¿En qué año se declaró la Independencia?", "1818", "La ficha lo indica."),
        ("{F} ¿Qué querían los pipiolos?", "Más libertades y un poder menos concentrado", "La ficha los describe así."),
        ("{F} ¿Qué querían los pelucones?", "Orden y una autoridad fuerte", "La ficha los describe así."),
        ("=", "{F} ¿Cuántos años rigió la Constitución de 1833 hasta 1925?", "1925-1833", "Se resta el año de la Constitución al de su término.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la batalla de Lircay y la Constitución de 1833?", "1833-1830", "Se resta el año de Lircay al de la Constitución.", " años"),
        ("{F} ¿Qué hito es posterior? A) Constitución de 1833 B) Batalla de Maipú", "A) Constitución de 1833", "1833 es posterior a 1818."),
        ("{F} Un grupo propone que cada provincia decida sus asuntos internos. ¿Qué visión representa? A) Federalista B) Pelucona", "A) Federalista", "Querían autonomía provincial."),
        ("{F} Un grupo quiere un presidente con mucho poder para mantener el orden. ¿Qué visión representa? A) Pelucona B) Pipiola", "A) Pelucona", "Querían un Ejecutivo fuerte."),
        ("{F} ¿Qué etapa corresponde a 1822–1828? A) Ensayos constitucionales que no lograron estabilidad B) El orden conservador", "A) Ensayos constitucionales que no lograron estabilidad", "La ficha lo dice."),
        ("{F} ¿Por qué se dice que la Constitución de 1833 dio relativa estabilidad?", "Porque rigió 92 años, hasta 1925", "Duró mucho más que los textos anteriores."),
        ("{F} Un compañero dice: «Después de 1818 el país quedó organizado». Corrígelo.", "Hubo ensayos constitucionales entre 1822 y 1828 y una guerra civil antes de 1833", "La organización fue un proceso."),
        ("{F} ¿Cuál es la mejor pregunta histórica? A) ¿Cómo se organizó la república y por qué la Constitución de 1833 dio estabilidad? B) ¿Qué batalla fue la más bonita?", "A) ¿Cómo se organizó la república y por qué la Constitución de 1833 dio estabilidad?", "La A se responde con hechos."),
        ("{F} Una línea de tiempo usa 1 cm = 5 años y va de 1810 a 1835. ¿Cuántos centímetros mide?", "5 cm", "Se divide el tramo de 25 años por 5."),
    ],
    ctx=("Un afiche escolar dice: «En 1818 Chile ya tenía una república estable». ¿Cómo lo corriges? A) La república se organizó después de ensayos y de una guerra civil, y la estabilidad llegó con 1833 B) Es correcto", "A) La república se organizó después de ensayos y de una guerra civil, y la estabilidad llegó con 1833", "La ficha muestra conflictos posteriores a 1818."),
    sc=[("¿Qué fue Lircay?", "Una batalla de 1830 que dio la victoria a los conservadores", "Cierra la guerra civil de 1829–1830."),
        ("¿Qué es el federalismo?", "Un sistema donde las provincias tienen autonomía", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1810 y 1830?", "1830-1810", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1810 a 1835 con escala 1 cm = 5 años y marca: Primera Junta (1810), Independencia (1818), textos constitucionales de 1822–1828, Lircay (1830) y Constitución de 1833. Debajo escribe dos frases: una que explique qué querían pipiolos y pelucones, y otra que diga por qué 1833 fue importante. {F}",
        "Posiciones desde 1810: 0; 1,6; 2,4 a 3,6; 4; 4,6 cm. Frases: «Los pipiolos querían más libertades y los pelucones orden y autoridad fuerte»; «La Constitución de 1833 rigió hasta 1925».",
        ["respeta la escala", "los hitos están bien ubicados", "las frases son correctas"], ["línea de tiempo", "dos frases"], ["no medir con la escala", "confundir pipiolos con pelucones"],
        "Pide que explique por qué el orden fue valorado por unos y criticado por otros."),
    reinforce="Explica en voz alta las tres visiones de la república y la fecha de la Constitución.",
    extend="Busca en tu casa o ciudad una calle o plaza con nombre de un personaje del siglo XIX y anota quién fue.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, editorial de un periódico liberal, 1828: «Pedimos libertad de prensa, elecciones frecuentes y un gobierno limitado por la ley. Las provincias deben tener voz.» "
     "Fuente B, carta de un hacendado conservador a un amigo, 1830: «Sin orden no hay progreso. Solo un gobierno fuerte puede evitar el desorden de estos años y proteger la propiedad.» "
     "Fuente C, resumen de ejemplo de la Constitución de 1833: el presidente dura cinco años y puede ser reelegido una vez; existe un Congreso con Senado y Cámara de Diputados; la religión católica es la oficial; votan los hombres que cumplan requisitos de renta o propiedad y sepan leer.")
build(
    OA, 2, F,
    use="Aprenderé a contextualizar y comparar fuentes de la formación de la república: un editorial liberal, una carta conservadora y un resumen de la Constitución de 1833.",
    prior=["Sé qué visiones había sobre la república.", "Sé contextualizar una fuente.", "Sé separar descripción de interpretación."],
    explain=[
        "Un editorial es un texto de opinión de un periódico: expresa la postura de un grupo. La carta del hacendado es privada y muestra el miedo al desorden. El resumen de la Constitución es una fuente normativa: dice cómo debe organizarse el poder. Cada una informa algo distinto: ideas, temores y reglas.",
        "Para comparar, se contextualiza cada fuente: quién la hizo, cuándo y para qué. El editorial de 1828 busca convencer a favor de libertades. La carta de 1830, escrita tras la guerra civil, busca justificar un gobierno fuerte. La Constitución de 1833 fija reglas con un presidente de cinco años, reelegible una vez, y un voto limitado por renta o propiedad.",
        "Las tres fuentes tienen límites. Los dos primeros textos expresan solo la voz de un grupo, y el tercero describe lo que dice la ley, no cómo se aplicaba en la práctica. Por eso, antes de concluir, se comparan y se reconoce qué voces faltan, por ejemplo las de quienes no podían votar.",
    ],
    vocab=[("editorial", "texto de opinión que expresa la postura de un periódico"), ("fuente normativa", "documento que fija reglas, como una constitución"), ("reelección", "volver a ser elegido para el mismo cargo"), ("Senado", "cámara del Congreso, de menor número de miembros"), ("Cámara de Diputados", "cámara del Congreso con representantes elegidos")],
    worked=[
        ("Contextualizar", "¿Quién escribe la Fuente B, cuándo y para qué?", ["Autor: un hacendado conservador.", "Fecha: 1830. Propósito: defender un gobierno fuerte."], "Un hacendado conservador, en 1830, para defender un gobierno fuerte"),
        ("Calcular un intervalo", "¿Cuántos años pasaron entre la carta del hacendado (1830) y la Constitución de 1833?", ["Tomo los dos años.", "Resto: 1833 − 1830 = 3."], "3 años"),
    ],
    mistakes=[("Tomar la Constitución como descripción de cómo se vivía en la práctica.", "Una constitución dice lo que debe ocurrir.", "Compara con otras fuentes."),
              ("Concluir con un editorial que todos pedían libertad de prensa.", "Expresa la voz de un grupo.", "Escribe «este periódico pedía».")],
    T=[
        ("{F} ¿Qué pide el editorial de la Fuente A?", "Libertad de prensa, elecciones frecuentes y un gobierno limitado por la ley", "El texto lo dice."),
        ("{F} ¿Qué cree el hacendado de la Fuente B que se necesita para el progreso?", "Orden, con un gobierno fuerte", "La carta lo dice."),
        ("{F} ¿Cuántos años dura el presidente según la Fuente C?", "Cinco años", "El resumen lo dice."),
        ("=", "{F} ¿Cuántos años puede gobernar como máximo un presidente según la Fuente C?", "5*2", "Se multiplica la duración por los dos periodos permitidos.", " años"),
        ("=", "{F} ¿Cuántos años separan la Fuente A de la Fuente B?", "1830-1828", "Se resta el año del editorial al de la carta.", " años"),
        ("{F} ¿Qué fuente es normativa? A) La Fuente C B) La Fuente B", "A) La Fuente C", "Fija las reglas del poder."),
        ("{F} ¿Qué fuente defiende un gobierno fuerte? A) La Fuente B B) La Fuente A", "A) La Fuente B", "La carta del hacendado."),
        ("{F} ¿Qué frase describe la Fuente C? A) Votan los hombres que cumplan requisitos de renta o propiedad y sepan leer B) Todos los habitantes votan", "A) Votan los hombres que cumplan requisitos de renta o propiedad y sepan leer", "El resumen lo indica."),
        ("{F} ¿Qué rasgo de la Fuente C se relaciona con las ideas conservadoras? A) El presidente con cinco años reelegible y religión oficial B) Voto abierto a todos los adultos", "A) El presidente con cinco años reelegible y religión oficial", "Dan estabilidad al Ejecutivo y a la tradición."),
        ("{F} ¿Por qué el editorial no prueba lo que pensaban todos los chilenos?", "Porque expresa la postura de un periódico liberal", "Es la voz de un grupo."),
        ("{F} Un compañero concluye: «Con la Constitución de 1833 todos votaban». ¿Qué corrección haces?", "El resumen dice que votaban solo los hombres con renta o propiedad que sabían leer", "El voto era limitado."),
        ("{F} ¿Qué voz falta en las tres fuentes? A) La de personas que no podían votar B) La de otro hacendado", "A) La de personas que no podían votar", "Ninguna fuente las incluye."),
        ("{F} ¿Qué conclusión es más proporcional? A) Las fuentes muestran visiones opuestas sobre el poder y una constitución que fijó un Ejecutivo fuerte y voto limitado B) Las fuentes prueban lo que pensaba todo el país", "A) Las fuentes muestran visiones opuestas sobre el poder y una constitución que fijó un Ejecutivo fuerte y voto limitado", "No dice más de lo que muestran."),
    ],
    ctx=("Para una exposición sobre 1833, un grupo solo cita la Constitución. ¿Qué fuente suman para mostrar las visiones en disputa? A) Un editorial liberal y una carta conservadora B) Otro artículo de la misma Constitución", "A) Un editorial liberal y una carta conservadora", "Muestran lo que pensaban los grupos."),
    sc=[("¿Qué es una fuente normativa?", "Un documento que fija reglas", "Así se define."),
        ("¿Qué es la reelección?", "Volver a ser elegido para el mismo cargo", "Así se define."),
        ("=", "En un país de ejemplo el presidente dura 6 años y puede ser reelegido una vez. ¿Cuántos años puede gobernar como máximo?", "6*2", "Se multiplica la duración por los dos periodos permitidos.", " años")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (una frase); qué interpretas (con «Esto sugiere que…»). Cierra con qué no puedes concluir y qué voz falta. {F}",
        "Fuente B. Autor y fecha: un hacendado conservador, 1830. Dice: sin orden no hay progreso y se necesita un gobierno fuerte. Interpretación: esto sugiere que los conservadores temían el desorden tras la guerra civil. No puedo concluir que todos pensaban igual; falta la voz de quienes no votaban.",
        ["contextualiza", "separa descripción e interpretación", "señala límite y voz ausente"], ["tabla de tres filas", "frase de cierre"], ["usar un juicio como descripción", "generalizar"],
        "Pide que cuente qué diría un pipiolo sobre la carta."),
    reinforce="Explica por qué un editorial, una carta y una constitución informan cosas distintas.",
    extend="Lee un artículo de la Constitución actual con una persona de tu casa y anota qué regula.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de cambio, continuidad y territorio). "
     "Cambios: de colonia gobernada por la Corona española a república con autoridades propias; Congreso con Senado y Cámara de Diputados; esclavitud abolida en 1823; textos constitucionales de 1822, 1823, 1828 y 1833. "
     "Continuidades: sociedad jerárquica, con grandes propietarios de tierras (haciendas) con mucho poder; Iglesia católica con gran influencia; mayoría de la población en el campo; voto restringido. "
     "Territorio: el poder se concentraba en Santiago y el Valle Central; provincias como Concepción y Coquimbo reclamaban más autonomía. "
     "Economía: minería de la plata y del cobre en el norte y comercio por el puerto de Valparaíso.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio en la formación de la república: qué cambió, qué siguió igual y cómo se repartía el poder en el espacio.",
    prior=["Sé las visiones políticas de la república.", "Sé calcular diferencias de años.", "Sé leer un cuadro de datos."],
    explain=[
        "Con la república cambiaron las autoridades: ya no gobernaba la Corona española, sino autoridades chilenas con un Congreso y constituciones. También se abolió la esclavitud en 1823. Es decir, hubo cambios políticos importantes. Pero muchos rasgos de la sociedad continuaron: grandes propietarios de tierras con poder, una Iglesia católica influyente, una mayoría de la población en el campo y un voto restringido.",
        "El territorio muestra tensiones. El poder se concentraba en Santiago y el Valle Central, y las provincias como Concepción y Coquimbo reclamaban más autonomía. Esa discusión sobre cuánto poder debe tener la capital frente a las regiones se llama centralismo. La Constitución de 1833 mantuvo un Estado unitario, es decir, con un solo gobierno central.",
        "La economía también influyó. La minería del norte y el comercio por Valparaíso daban recursos y fortalecían a grupos de comerciantes y mineros que apoyaban un orden estable. Analizar cambio y continuidad evita decir que todo se transformó con la independencia. En la práctica cambió el sistema político, pero mucho de la estructura social se mantuvo.",
    ],
    vocab=[("centralismo", "concentración del poder y las decisiones en la capital"), ("Estado unitario", "Estado con un solo gobierno central para todo el territorio"), ("hacienda", "gran propiedad agrícola"), ("abolición", "término legal de una práctica, como la esclavitud"), ("provincia", "división territorial del país")],
    worked=[
        ("Medir un intervalo", "¿Cuántos años pasaron entre la abolición de la esclavitud (1823) y la Constitución de 1833?", ["Tomo los dos años de la ficha.", "Resto: 1833 − 1823 = 10."], "10 años"),
        ("Clasificar", "«Siguieron existiendo grandes haciendas con mucho poder.» ¿Es cambio o continuidad?", ["Esto ya existía en la colonia.", "Se mantuvo en la república."], "Continuidad"),
    ],
    mistakes=[("Decir que la república cambió toda la sociedad.", "La estructura social y la propiedad de la tierra continuaron.", "Busca qué siguió igual."),
              ("Confundir centralismo con federalismo.", "Son ideas opuestas sobre el reparto del poder.", "Define cada una.")],
    T=[
        ("{F} ¿En qué año se abolió la esclavitud en Chile según la ficha?", "1823", "La ficha lo indica."),
        ("{F} ¿Dónde se concentraba el poder político?", "En Santiago y el Valle Central", "La ficha lo dice."),
        ("{F} ¿Qué provincias reclamaban más autonomía?", "Concepción y Coquimbo", "La ficha las nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la abolición de la esclavitud y la Constitución de 1828?", "1828-1823", "Se resta el año de la abolición al de la Constitución.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1822 y la de 1833?", "1833-1822", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué es un cambio? A) Pasó de colonia a república con autoridades propias B) Siguió el poder de las haciendas", "A) Pasó de colonia a república con autoridades propias", "La B es una continuidad."),
        ("{F} ¿Qué es una continuidad? A) La Iglesia católica mantuvo gran influencia B) Se abolió la esclavitud", "A) La Iglesia católica mantuvo gran influencia", "Es algo que se mantuvo."),
        ("{F} ¿Qué actividad económica estaba en el norte? A) Minería B) Pesca de altura", "A) Minería", "La ficha la señala."),
        ("{F} ¿Qué es el centralismo? A) El poder concentrado en la capital B) El poder repartido por igual", "A) El poder concentrado en la capital", "Así se define."),
        ("{F} ¿Por qué las provincias reclamaban autonomía?", "Porque las decisiones se concentraban en Santiago", "Querían más voz."),
        ("{F} Un compañero dice: «Con la independencia desapareció la influencia de las haciendas». Refútalo.", "La ficha dice que los grandes propietarios mantuvieron mucho poder", "Hubo continuidad en el poder de las haciendas."),
        ("{F} ¿Qué relación hay entre minería, comercio y estabilidad? A) Daban recursos y fortalecían a grupos que apoyaban el orden B) No tenían relación", "A) Daban recursos y fortalecían a grupos que apoyaban el orden", "Fortalecieron a comerciantes y mineros."),
        ("{F} ¿Qué conclusión es más ajustada? A) Cambió el sistema político, pero la estructura social y el poder concentrado continuaron B) Todo cambió con la independencia", "A) Cambió el sistema político, pero la estructura social y el poder concentrado continuaron", "Reúne cambio y continuidad."),
    ],
    ctx=("Un compañero afirma que «con la república, las provincias tuvieron igual poder que Santiago». ¿Qué dato de la ficha lo contradice? A) El poder se concentraba en Santiago y las provincias reclamaban autonomía B) Valparaíso era un puerto", "A) El poder se concentraba en Santiago y las provincias reclamaban autonomía", "Muestra el centralismo de la época."),
    sc=[("¿Qué es un Estado unitario?", "Un Estado con un solo gobierno central", "Así se define."),
        ("¿Qué es una hacienda?", "Una gran propiedad agrícola", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1828 y 1833?", "1833-1828", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», y escribe tres datos en cada una con la ficha. Luego dibuja un esquema simple de Chile: un círculo grande para «Santiago» y dos círculos pequeños para «Concepción» y «Coquimbo» con flechas hacia el grande. {F}",
        "Cambió: de colonia a república; Congreso; esclavitud abolida en 1823. Continuó: haciendas con poder; Iglesia influyente; voto restringido. Esquema: dos flechas desde Concepción y Coquimbo hacia Santiago.",
        ["usa datos de la ficha", "separa cambio y continuidad", "esquema de centralismo"], ["tabla completa", "esquema"], ["mezclar cambio y continuidad", "olvidar una provincia"],
        "Pide que diga quién gana y quién pierde con el centralismo."),
    reinforce="Explica en voz alta un cambio, una continuidad y el centralismo.",
    extend="Averigua cuál es la capital de tu región y qué servicios ofrece que otras comunas no tienen.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Político liberal (pipiolo), 1828: «Queremos libertad de prensa y que el poder se limite con leyes claras y elecciones.» "
     "Político conservador (pelucón), 1830: «Hemos visto el desorden y la guerra civil. Necesitamos un presidente fuerte y la religión como base moral.» "
     "Federalista, 1827: «Cada provincia conoce sus problemas. Debe decidir sobre sus impuestos y sus escuelas.» "
     "Mujer artesana, 1830 (ejemplo): «Trabajo todo el día y pago impuestos con mi venta de tejidos, pero no puedo votar.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores y perspectivas en la formación de la república: liberales, conservadores, federalistas y quienes no votaban.",
    prior=["Sé qué visiones políticas había.", "Sé contextualizar fuentes.", "Sé que cada actor tiene intereses."],
    explain=[
        "El enfrentamiento de visiones se ve en las voces de los actores. El pipiolo valoraba la libertad de prensa y las leyes claras. El pelucón priorizaba el orden y creía que la religión debía ser la base moral. El federalista quería que las provincias decidieran sobre sus propios impuestos y escuelas. La mujer artesana, en cambio, ni siquiera podía votar aunque pagaba impuestos.",
        "Estas posturas explican los conflictos de los años 1820. Los liberales querían limitar el poder; los conservadores querían fortalecerlo; los federalistas querían repartirlo entre provincias. Cuando los conservadores ganaron en Lircay en 1830, impusieron su proyecto. La Constitución de 1833 mostró esa victoria: Ejecutivo fuerte, Estado unitario y religión oficial.",
        "Para contrastar, se compara qué quiere cada actor, qué le conviene y qué teme. El pipiolo teme los abusos de un gobierno fuerte; el pelucón, el desorden; el federalista, quedar bajo el centralismo; la artesana, quedar sin voz. Una buena explicación considera todas las voces y no solo la del grupo que ganó.",
    ],
    vocab=[("libertad de prensa", "derecho a publicar opiniones sin censura previa"), ("orden público", "situación de tranquilidad y respeto de las leyes"), ("base moral", "idea o valor que orienta lo que se considera correcto"), ("autonomía provincial", "capacidad de una provincia de decidir sus asuntos"), ("excluido", "persona que no puede participar en algo")],
    worked=[
        ("Quién teme al desorden", "¿Qué actor teme el desorden y la guerra civil?", ["Busco una voz que hable de orden.", "El pelucón dice haber visto desorden y guerra civil."], "El pelucón"),
        ("Quién queda excluido", "¿Qué actor paga impuestos pero no puede votar?", ["Busco una voz que lo diga.", "La mujer artesana."], "La mujer artesana"),
    ],
    mistakes=[("Explicar el periodo solo con la voz del grupo que ganó.", "Se ignoran los pipiolos, federalistas y excluidos.", "Incluye al menos tres voces."),
              ("Pensar que los federalistas y los pipiolos querían lo mismo.", "Unos pedían libertades y otros autonomía provincial.", "Distingue lo que pide cada uno.")],
    T=[
        ("{F} ¿Qué valora el político liberal?", "La libertad de prensa y las leyes claras", "Su voz lo dice."),
        ("{F} ¿Qué necesita el político conservador según su voz?", "Un presidente fuerte y la religión como base moral", "Su voz lo dice."),
        ("{F} ¿Qué quiere el federalista para las provincias?", "Decidir sobre sus impuestos y sus escuelas", "Su voz lo dice."),
        ("{F} ¿Qué no puede hacer la mujer artesana?", "Votar", "Su voz lo dice."),
        ("{F} ¿Quién teme el desorden? A) El conservador B) El federalista", "A) El conservador", "Habla de guerra civil."),
        ("{F} ¿Quién teme el centralismo? A) El federalista B) El conservador", "A) El federalista", "Quiere decidir en su provincia."),
        ("{F} ¿Qué actor se beneficia con un Ejecutivo fuerte? A) El conservador B) El liberal", "A) El conservador", "Lo pide para mantener el orden."),
        ("{F} ¿Qué actor critica el poder concentrado? A) El liberal B) El conservador", "A) El liberal", "Quiere limitarlo con leyes."),
        ("{F} ¿Por qué el pelucón y el pipiolo tienen perspectivas opuestas?", "Porque uno prioriza el orden con autoridad fuerte y el otro las libertades con poder limitado", "Sus intereses chocan."),
        ("{F} Un compañero dice: «Todos aceptaban la Constitución de 1833». Refútalo con la ficha.", "Los liberales y federalistas tenían visiones distintas y las mujeres no podían votar", "Hubo grupos con otras ideas."),
        ("{F} ¿Qué voz falta para entender la república? A) La de un campesino sin tierras B) La de otro político", "A) La de un campesino sin tierras", "Completa la perspectiva de los excluidos."),
        ("{F} ¿Qué conclusión es más equilibrada? A) La república se formó entre visiones distintas y la victoria conservadora impuso su proyecto, dejando fuera a algunos grupos B) Todos pensaban igual", "A) La república se formó entre visiones distintas y la victoria conservadora impuso su proyecto, dejando fuera a algunos grupos", "Reúne las cuatro voces."),
        ("{F} ¿Qué pregunta ayuda a contrastar actores? A) ¿Qué quiere, qué le conviene y qué teme cada uno? B) ¿Qué actor tiene la razón y cuál se equivoca?", "A) ¿Qué quiere, qué le conviene y qué teme cada uno?", "Es el método de contraste."),
    ],
    ctx=("En un debate escolar, un grupo defiende el Ejecutivo fuerte y otro la autonomía de las provincias. ¿Qué voz usa el segundo grupo? A) La del federalista B) La del conservador", "A) La del federalista", "Pide decidir en cada provincia."),
    sc=[("¿Qué es la libertad de prensa?", "El derecho a publicar opiniones sin censura previa", "Así se define."),
        ("¿Qué actor pide autonomía provincial?", "El federalista", "Su voz lo dice."),
        ("¿Qué es una persona excluida?", "Alguien que no puede participar en algo", "Así se define.")],
    op=("Elige dos actores de la ficha y haz una tabla con: qué quiere, qué le conviene y qué teme. Después escribe tres líneas sobre por qué sus perspectivas chocan. {F}",
        "Liberal: quiere libertad de prensa; le conviene poder limitado por leyes; teme abusos del gobierno. Conservador: quiere orden; le conviene presidente fuerte; teme el desorden. Texto: «Uno teme los abusos y otro el desorden, por eso discrepan sobre el poder del presidente».",
        ["elige dos actores", "tres columnas completas", "explica el choque"], ["tabla completa", "tres líneas"], ["mezclar voces", "opinar sin base"],
        "Pide que diga qué voz habría que sumar para una república más inclusiva."),
    reinforce="Elige un actor y explica en voz alta qué quería y qué temía.",
    extend="Piensa en una discusión de tu curso donde hubo visiones distintas y anota qué quería cada grupo.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento). "
     "Pregunta: ¿qué explica la relativa estabilidad política alcanzada a partir de la Constitución de 1833? "
     "Dato 1: la Constitución de 1833 estableció un presidente con amplias atribuciones, elegido por cinco años y reelegible una vez. "
     "Dato 2: un grupo dirigente cohesionado, formado por hacendados, comerciantes y mineros, apoyaba el orden. "
     "Dato 3: la economía creció con la minería y el comercio por Valparaíso. "
     "Dato 4: el ejército quedó, en general, subordinado al poder civil (hubo levantamientos, como los de 1851 y 1859) y existió una Guardia Nacional. "
     "Dato 5: la Constitución regía por 92 años (hasta 1925) y el voto estaba restringido a hombres con renta o propiedad que sabían leer.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre los factores que explican la estabilidad después de 1833: afirmación, evidencia, razonamiento y conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé contrastar actores.", "Sé qué disponía la Constitución de 1833."],
    explain=[
        "Un argumento sobre la estabilidad puede afirmar: «la estabilidad se explica por un Ejecutivo fuerte, un grupo dirigente cohesionado, crecimiento económico y control civil del ejército». La evidencia son los datos de la ficha: las atribuciones del presidente, la unidad de hacendados, comerciantes y mineros, la minería y el comercio, y la subordinación del ejército.",
        "El razonamiento explica cómo cada dato apoya la afirmación. Un presidente con amplias atribuciones puede imponer orden. Un grupo dirigente cohesionado evita conflictos internos. El crecimiento económico da recursos al Estado. Un ejército subordinado evita golpes militares. Todas son causas que actúan a la vez, por eso la explicación es multicausal.",
        "Para que sea proporcional, hay que decir que la estabilidad fue relativa: se apoyó en un voto restringido, y los grupos excluidos no tenían voz. Un contraargumento posible es que la estabilidad se logró por la fuerza y por excluir a la oposición; se responde reconociendo ese costo.",
    ],
    vocab=[("atribuciones", "poderes o facultades que da la ley a una autoridad"), ("grupo dirigente", "grupo que toma las decisiones importantes en una sociedad"), ("cohesionado", "unido por intereses o ideas comunes"), ("subordinado", "que depende de una autoridad superior"), ("multicausal", "con más de una causa que actúa a la vez")],
    worked=[
        ("Elegir evidencia política", "¿Qué dato muestra el papel del Ejecutivo?", ["Busco un dato sobre el presidente.", "El dato 1."], "Dato 1"),
        ("Elegir evidencia sobre control civil", "¿Qué dato evita golpes militares?", ["Busco un dato sobre el ejército.", "El dato 4."], "Dato 4"),
    ],
    mistakes=[("Explicar la estabilidad con una sola causa.", "Hubo causas políticas, económicas y sociales.", "Nombra al menos tres."),
              ("Olvidar el costo de la estabilidad.", "Se apoyó en un voto restringido.", "Menciona el dato 5.")],
    T=[
        ("{F} ¿Qué dato muestra una causa económica de la estabilidad?", "El dato 3, la minería y el comercio por Valparaíso", "Dio recursos al Estado y a la élite."),
        ("{F} ¿Qué dato muestra la unidad de la élite?", "El dato 2, el grupo dirigente cohesionado", "Hacendados, comerciantes y mineros apoyaban el orden."),
        ("{F} ¿Qué tres grupos forman el grupo dirigente cohesionado del dato 2?", "Hacendados, comerciantes y mineros", "El dato 2 los nombra."),
        ("=", "{F} ¿Cuántos años puede gobernar como máximo un presidente según el dato 1?", "5*2", "Se multiplica la duración por los dos periodos.", " años"),
        ("{F} ¿Qué afirmación responde la pregunta? A) La estabilidad se explica por un Ejecutivo fuerte, una élite unida, crecimiento económico y control civil del ejército B) La estabilidad fue casual", "A) La estabilidad se explica por un Ejecutivo fuerte, una élite unida, crecimiento económico y control civil del ejército", "Se apoya en los datos 1 a 4."),
        ("{F} ¿Qué dato sirve de contraargumento? A) El dato 5, el voto restringido B) El dato 3", "A) El dato 5, el voto restringido", "Muestra el costo de la estabilidad."),
        ("{F} Completa el razonamiento: «El dato 4 apoya la estabilidad porque…» A) un ejército subordinado evita golpes militares B) el ejército gobernaba", "A) un ejército subordinado evita golpes militares", "Conecta el dato con la causa."),
        ("{F} Un compañero escribe: «La estabilidad se debió solo a que el presidente tenía mucho poder». ¿Qué datos usas para corregirlo?", "Los datos 2, 3 y 4, que muestran causas económicas, sociales y militares", "Hubo varias causas."),
        ("{F} ¿Por qué el dato 5 limita la idea de una estabilidad para todos?", "Porque solo votaban hombres con renta o propiedad que sabían leer", "Muchos quedaban sin voz."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «relativa» B) «absoluta»", "A) «relativa»", "Refleja la exclusión."),
        ("{F} Ordena las partes de un argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y se explica."),
        ("{F} ¿Qué dato falta para incluir la voz de los excluidos? A) Un dato sobre cómo vivían quienes no podían votar B) Otro dato sobre Valparaíso", "A) Un dato sobre cómo vivían quienes no podían votar", "Aporta la perspectiva ausente."),
        ("{F} ¿Qué conclusión se ajusta mejor a los datos? A) La estabilidad fue relativa y se apoyó en un Ejecutivo fuerte, una élite unida y una economía en crecimiento, con voto restringido B) La estabilidad fue total", "A) La estabilidad fue relativa y se apoyó en un Ejecutivo fuerte, una élite unida y una economía en crecimiento, con voto restringido", "Reúne los datos."),
    ],
    ctx=("Un afiche escolar dice: «La estabilidad se debió a que todos estaban conformes». ¿Qué evidencia de la ficha usas para responder? A) El dato 5, el voto restringido B) El dato 3 solo", "A) El dato 5, el voto restringido", "Muestra que muchos no tenían voz."),
    sc=[("¿Qué quiere decir que la estabilidad de 1833 fue multicausal?", "Que tuvo varias causas a la vez", "Así se aplica el término a la estabilidad."),
        ("¿Qué son las atribuciones?", "Los poderes que da la ley a una autoridad", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1833 y 1925?", "1925-1833", "Se resta el año menor al mayor.", " años")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Qué explica la relativa estabilidad después de 1833?». Usa al menos tres datos de la ficha, incluye el dato 5 como límite y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«La estabilidad después de 1833 fue relativa y se explica por varias causas. El presidente tenía amplias atribuciones, la élite estaba cohesionada y la economía crecía con la minería y el comercio. El ejército quedó subordinado. Sin embargo, el voto estaba restringido a hombres con renta o propiedad, así que muchos no tenían voz».",
        ["responde la pregunta", "usa tres datos y un límite", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["usar una sola causa", "no explicar el vínculo"],
        "Pide que diga qué grupo habría opinado distinto."),
    reinforce="Explica en voz alta tres factores de la estabilidad y un límite.",
    extend="Escribe un contraargumento y respóndelo con un dato de la ficha.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (proyecciones y límites del orden de 1833). "
     "Proyecciones: la Constitución de 1833 rigió hasta 1925, con reformas parciales. "
     "Límites: voto restringido; las mujeres no votaban; el presidente tenía muchas atribuciones y la oposición tenía poca influencia en el gobierno; las provincias seguían reclamando autonomía. "
     "Tensiones posteriores: revoluciones armadas en 1851 y en 1859 contra el gobierno. "
     "Reformas posteriores: en la segunda mitad del siglo XIX se redujeron las atribuciones del presidente y se amplió el voto.")
build(
    OA, 6, F,
    use="Aprenderé a evaluar proyecciones y límites del orden de 1833: qué logró, a quiénes dejó fuera y qué tensiones aparecieron después.",
    prior=["Sé qué explica la estabilidad.", "Sé construir un argumento.", "Sé qué es una proyección histórica."],
    explain=[
        "El orden de 1833 logró estabilidad, pero tuvo límites. El voto estaba restringido y las mujeres no votaban. El presidente concentraba mucho poder, y la oposición tenía poca influencia. Las provincias seguían pidiendo autonomía. Estos límites generaron tensiones que reaparecieron en revoluciones armadas en 1851 y 1859.",
        "También hubo proyecciones: la Constitución rigió hasta 1925 con reformas parciales. En la segunda mitad del siglo XIX se redujeron las atribuciones del presidente y se amplió el voto. Esto muestra que el orden conservador no fue inmóvil: cambió con el tiempo por presiones de grupos que querían más participación.",
        "Evaluar significa pesar logros y costos. El logro fue la estabilidad institucional en una época de conflictos en la región. El costo fue la exclusión y las tensiones. Una buena conclusión no dice que la estabilidad fue «buena» o «mala» sin más; muestra para quién fue buena y para quién no, con evidencia.",
    ],
    vocab=[("reforma", "cambio en una ley o institución para mejorarla"), ("oposición", "grupo que se opone al gobierno"), ("revolución armada", "levantamiento con armas contra el gobierno"), ("participación", "capacidad de tomar parte en decisiones"), ("proyección", "efecto que un proceso tiene hacia el futuro")],
    worked=[
        ("Calcular un intervalo", "¿Cuántos años pasaron entre la Constitución de 1833 y la revolución de 1851?", ["Tomo los dos años de la ficha.", "Resto: 1851 − 1833 = 18."], "18 años"),
        ("Pesar un logro y un costo", "El logro fue la estabilidad. ¿Qué costo señala la ficha?", ["La ficha menciona el voto restringido.", "También que las mujeres no votaban."], "Voto restringido y exclusión de las mujeres"),
    ],
    mistakes=[("Decir que el orden de 1833 no cambió nunca.", "Hubo reformas en la segunda mitad del siglo XIX.", "Menciona las reformas."),
              ("Decir que las revoluciones fueron sin causa.", "Respondían a tensiones con el gobierno y el poder concentrado.", "Relaciona con los límites.")],
    T=[
        ("{F} ¿Hasta qué año rigió la Constitución de 1833?", "Hasta 1925", "La ficha lo indica."),
        ("{F} ¿En qué años hubo revoluciones armadas?", "En 1851 y en 1859", "La ficha lo indica."),
        ("{F} ¿Qué se amplió en la segunda mitad del siglo XIX?", "El voto", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre las revoluciones de 1851 y 1859?", "1859-1851", "Se resta el año menor al mayor.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la revolución de 1859 y el fin de la Constitución (1925)?", "1925-1859", "Se resta el año de la revolución al del fin.", " años"),
        ("{F} ¿Qué es un logro del orden de 1833? A) La estabilidad institucional B) El voto universal", "A) La estabilidad institucional", "Rigió 92 años."),
        ("{F} ¿Qué es un costo del orden de 1833? A) La exclusión del voto de muchos B) La estabilidad", "A) La exclusión del voto de muchos", "El voto estaba restringido."),
        ("{F} ¿Qué reforma ocurrió después? A) Se redujeron las atribuciones del presidente B) Se eliminó el Congreso", "A) Se redujeron las atribuciones del presidente", "La ficha lo indica."),
        ("{F} ¿Qué efecto tenía un presidente con mucho poder en la oposición? A) Tenía poca influencia B) Gobernaba junto al presidente", "A) Tenía poca influencia", "La ficha lo señala."),
        ("{F} ¿Por qué las revoluciones se relacionan con los límites del orden?", "Porque respondían a tensiones por el poder concentrado y la falta de participación", "Mostraban el descontento de algunos grupos."),
        ("{F} Un compañero dice: «El orden de 1833 fue perfecto». Refútalo con la ficha.", "Tuvo voto restringido y revoluciones en 1851 y 1859", "Hubo límites y tensiones."),
        ("{F} ¿Qué muestra la ampliación del voto? A) Que el orden cambió por presiones de grupos que querían participar B) Que no hubo cambios", "A) Que el orden cambió por presiones de grupos que querían participar", "Hubo reformas posteriores al orden de 1833."),
        ("{F} ¿Qué conclusión pesa logros y límites? A) El orden de 1833 dio estabilidad, pero con exclusión y tensiones que llevaron a reformas B) El orden de 1833 no tuvo problemas", "A) El orden de 1833 dio estabilidad, pero con exclusión y tensiones que llevaron a reformas", "Considera ambas caras."),
    ],
    ctx=("Un compañero propone: «Una constitución es buena si dura mucho». ¿Cómo respondes con la ficha? A) La duración no basta: también importa quién participaba y qué tensiones había B) Tiene toda la razón", "A) La duración no basta: también importa quién participaba y qué tensiones había", "La ficha muestra límites a la participación."),
    sc=[("¿Qué es una reforma?", "Un cambio en una ley o institución para mejorarla", "Así se define."),
        ("¿Qué es la oposición?", "El grupo que se opone al gobierno", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1851 y 1925?", "1925-1851", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Logros» y «Límites», con tres datos en cada una usando la ficha. Después escribe una frase que pese ambos y diga si, en tu opinión, el orden de 1833 fue más beneficioso para unos que para otros, con una razón apoyada en la ficha. {F}",
        "Logros: estabilidad; Constitución duradera; reformas posteriores. Límites: voto restringido; oposición con poca influencia; provincias sin autonomía. Frase: «Fue más beneficioso para quienes votaban, porque el voto estaba limitado».",
        ["tres logros y tres límites", "usa evidencia", "frase que pesa ambos"], ["tabla completa", "una frase"], ["solo logros o solo límites", "opinar sin evidencia"],
        "Pide que diga qué reforma te parece más importante y por qué."),
    reinforce="Explica en voz alta un logro y un límite del orden de 1833.",
    extend="Averigua en qué año las mujeres chilenas pudieron votar en elecciones presidenciales y anota la fecha.",
)
