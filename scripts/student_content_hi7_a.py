"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 01 (hominización y poblamiento humano)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 01"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (datos redondeados y de ejemplo, hechos para este cuaderno; las fechas reales son aproximadas y se revisan con nuevos hallazgos). "
     "Australopithecus afarensis: África oriental, hace unos 3.500.000 años; caminaba en dos pies. "
     "Homo habilis: África, hace unos 2.400.000 años. "
     "Homo erectus: aparece en África hace unos 1.800.000 años y luego llega a Asia y Europa. "
     "Homo neanderthalensis: Europa y Asia occidental, desde hace unos 400.000 años hasta hace unos 40.000 años. "
     "Homo sapiens: África, hace unos 300.000 años, y hoy vive en todos los continentes.")
build(
    OA, 1, F,
    use="Aprenderé a ubicar las etapas de la evolución humana en el tiempo y a manejar escalas de miles y millones de años. Sirve para no confundir cuándo ocurrió cada cambio.",
    prior=["Sé leer una línea de tiempo y restar años.", "Sé que una fuente histórica puede ser una pista incompleta.", "Sé ubicar los continentes en un mapa."],
    explain=[
        "La hominización es el proceso largo por el cual, a lo largo de millones de años, surgieron especies cada vez más parecidas a los seres humanos actuales. Sus cambios principales fueron caminar en dos pies (bipedismo), tener un cerebro más grande y fabricar herramientas.",
        "Las fechas de este proceso se dan en miles y millones de años y son aproximadas, porque dependen de los hallazgos de fósiles y de los métodos para fecharlos. Para ubicarlas se usa una escala: por ejemplo, 1 cm en el papel puede representar 100.000 años. Así se ve que la escritura, de unos 5.000 años, ocupa un espacio mínimo.",
        "No hay que imaginar una escalera donde cada especie se transforma en la siguiente. Hubo muchas ramas, como en un árbol, y varias especies vivieron al mismo tiempo. Por ejemplo, neandertales y Homo sapiens convivieron durante miles de años. Ninguna especie era «mejor» que otra: cada una se adaptó a su ambiente.",
    ],
    vocab=[("hominización", "proceso de miles de años por el que surgió la especie humana"), ("bipedismo", "capacidad de caminar sobre dos pies"), ("fósil", "resto de un ser vivo antiguo conservado en la roca"), ("especie", "grupo de seres vivos con rasgos comunes que se reproducen entre sí"), ("escala", "relación entre una medida dibujada y el tiempo o la distancia real")],
    worked=[
        ("Calcular una diferencia de tiempo", "{F} ¿Cuántos años antes apareció Homo habilis que Homo erectus?", ["Busco las fechas: 2.400.000 y 1.800.000 años.", "Resto: 2.400.000 − 1.800.000 = 600.000."], "600.000 años"),
        ("Ubicar en una escala", "Una línea de tiempo usa 1 cm = 100.000 años. ¿A cuántos centímetros del presente queda un hallazgo de hace 700.000 años?", ["Cada 100.000 años equivalen a 1 cm.", "Divido: 700.000 ÷ 100.000 = 7."], "A 7 cm del presente"),
    ],
    mistakes=[("Dibujar la evolución como una fila recta de figuras que van de simio a persona actual.", "Se piensa que cada especie se convirtió en la siguiente y que no convivieron.", "Dibuja ramas: varias especies existieron a la vez y muchas se extinguieron sin dejar descendientes."),
              ("Creer que «hace 300.000 años» es una fecha exacta.", "No se recuerda que se estima a partir de fósiles y métodos con margen de error.", "Escribe «hace unos 300.000 años» y recuerda que puede cambiar con nuevos hallazgos.")],
    T=[
        ("{F} ¿En qué continente aparecieron Homo habilis y Homo sapiens?", "En África", "La ficha ubica a ambas especies en África."),
        ("{F} ¿Cuál es la especie más antigua de la ficha?", "Australopithecus afarensis", "Su fecha, 3.500.000 años, es la mayor."),
        ("=", "{F} ¿Cuántos años antes apareció Homo erectus que Homo sapiens?", "1800000-300000", "Se restan las dos fechas de la ficha.", " años"),
        ("=", "{F} ¿Cuántos años antes del Homo sapiens apareció el Homo neanderthalensis?", "400000-300000", "Se restan las fechas de aparición de ambos.", " años"),
        ("{F} Ordena de la más antigua a la más reciente: Homo sapiens, Homo habilis, Homo neanderthalensis, Australopithecus afarensis.", "Australopithecus afarensis, Homo habilis, Homo neanderthalensis, Homo sapiens", "Las fechas son 3.500.000, 2.400.000, 400.000 y 300.000 años."),
        ("{F} La ficha dice «hace unos 300.000 años». ¿Es una fecha exacta o aproximada? Explica con una palabra de la ficha.", "Aproximada, porque la ficha dice «unos»", "La palabra «unos» indica una estimación."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 100.000 años. ¿A cuántos centímetros del presente se ubica la aparición de Homo erectus?", "1800000//100000", "Se divide la fecha por lo que vale cada centímetro.", " cm"),
        ("=", "{F} La escritura tiene unos 5.000 años. ¿Cuántas veces cabe esa cifra en los 300.000 años de existencia de Homo sapiens?", "300000//5000", "Se divide 300.000 por 5.000 para comparar escalas.", " veces"),
        ("=", "{F} ¿Durante cuántos años, aproximadamente, existieron los neandertales según la ficha?", "400000-40000", "Se resta la fecha de desaparición a la de aparición.", " años"),
        ("{F} Ana dice: «Los neandertales son los antepasados directos de Homo sapiens porque aparecieron antes». Corrígela con un dato de la ficha.", "No: ambos vivieron a la vez muchos miles de años, así que fueron ramas distintas", "La ficha muestra que los neandertales existieron hasta hace 40.000 años, cuando ya vivía Homo sapiens."),
        ("Un afiche muestra seis figuras en fila, de la más encorvada a la más erguida, como si cada una se convirtiera en la siguiente. ¿Por qué esa imagen puede inducir a error?", "Porque sugiere una sola línea de progreso, y en realidad varias especies convivieron y fueron ramas distintas", "La evolución humana se parece a un árbol con ramas, no a una escalera."),
        ("Una línea de tiempo usa 1 cm = 100.000 años. ¿Qué espacio ocupan en ella los 5.000 años de escritura y por qué se ve casi pegada al presente?", "0,5 mm, porque 5.000 años es una veinteava parte de 100.000", "10 mm equivalen a 100.000 años; 5.000 años son la vigésima parte de ese tramo."),
        ("Un compañero dice: «Los humanos aparecieron hace 5.000 años, cuando empezó la escritura». ¿Qué confunde?", "Confunde el inicio de la escritura con el inicio de la especie, que es mucho más antigua", "Homo sapiens existe hace unos 300.000 años; la escritura es mucho más reciente."),
    ],
    ctx=("Un museo escolar quiere poner un panel de «¿quién vivía cuándo?» con las cuatro especies de la ficha. ¿Qué debe hacer con los neandertales y Homo sapiens para no sugerir una escalera? {F}", "Mostrarlos como ramas paralelas, que coincidieron en el tiempo, y no uno detrás de otro", "Sus fechas se solapan: entre hace 300.000 y 40.000 años existieron ambos."),
    sc=[("En una línea de tiempo, ¿qué especie va más cerca del presente: Homo habilis o Homo sapiens?", "Homo sapiens", "Aparece hace menos tiempo."),
        ("¿A qué se parece más la evolución humana: (A) una escalera de un solo camino o (B) un árbol con muchas ramas?", "B) un árbol con muchas ramas", "Varias especies convivieron y no todas fueron antepasadas de las siguientes."),
        ("=", "{F} ¿Cuántos años separan la aparición de Australopithecus afarensis y la de Homo sapiens?", "3500000-300000", "Se restan las dos fechas de la ficha.", " años")],
    op=("Dibuja una línea de tiempo con la escala 1 cm = 500.000 años que parta en el presente (0) y llegue a 3.500.000 años. Marca las cinco especies de la ficha con una raya y su nombre, y escribe una frase que explique por qué no es una escalera. {F}",
        "Raya de afarensis a 7 cm, habilis a unos 4,8 cm, erectus a 3,6 cm, neandertal a 0,8 cm y sapiens a 0,6 cm, con la frase «varias especies convivieron».",
        ["usa la escala indicada", "las cinco especies están en su lugar", "la frase explica la idea de ramas y no de escalera"], ["línea de tiempo dibujada", "frase escrita"], ["poner las especies en orden pero sin respetar la escala", "dibujarlas como si una se transformara en la siguiente"],
        "Pide que explique por qué sapiens y neandertal quedan casi juntos y qué significa eso."),
    reinforce="Di en voz alta las cinco especies de la ficha de la más antigua a la más reciente, con su continente.",
    extend="Escribe una pregunta que un especialista haría para saber si una fecha de la ficha podría cambiar.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (hallazgos de ejemplo, hechos para este cuaderno). "
     "Hallazgo A: un esqueleto con pelvis ancha y huesos de las piernas que muestran que caminaba en dos pies; su cerebro era pequeño, de unos 450 cm³. Se halló en África oriental. "
     "Hallazgo B: herramientas de piedra talladas junto a huesos de animales con marcas de corte; en el sitio no se hallaron huesos humanos. "
     "Hallazgo C: un cráneo con cerebro de unos 1.350 cm³ y rostro más plano. "
     "Hallazgo D: un dibujo hecho por un artista que muestra una familia con piel y pelo de un color determinado, a partir de un cráneo; el color de la piel y del pelo no se conserva en los huesos.")
build(
    OA, 2, F,
    use="Aprenderé a distinguir qué dice una evidencia, qué se interpreta a partir de ella y qué no se puede saber. Sirve para leer hallazgos sin exagerar.",
    prior=["Sé que la evolución humana tiene muchas ramas.", "Sé manejar cifras en miles y millones de años.", "Sé distinguir una fuente primaria de una secundaria."],
    explain=[
        "Las ciencias que estudian el origen humano trabajan con evidencia. La evidencia biológica son los restos del cuerpo: huesos, dientes y cráneos. De ellos se obtienen datos como la forma de la pelvis, que indica si caminaba en dos pies, o el volumen del cerebro, que se mide en cm³.",
        "La evidencia arqueológica son los objetos que dejaron las personas: herramientas de piedra, restos de fogatas, huesos de animales con marcas de corte. Dicen qué hacían, pero no siempre quiénes lo hicieron. Para saberlo hay que encontrar también restos humanos en la misma capa de tierra y fecharlos.",
        "Hay que separar la descripción de la interpretación. Describir es decir lo que se ve: «el cráneo mide 1.350 cm³». Interpretar es proponer una explicación: «esta especie cazaba en grupo». Una reconstrucción dibujada es una interpretación, y una conclusión debe ser proporcional: no puede afirmar más de lo que la evidencia permite.",
    ],
    vocab=[("evidencia biológica", "restos del cuerpo de seres vivos del pasado, como huesos y dientes"), ("evidencia arqueológica", "objetos y huellas que dejaron las personas, como herramientas"), ("descripción", "lo que se observa directamente en la evidencia"), ("interpretación", "explicación que se propone a partir de la evidencia"), ("volumen cerebral", "tamaño del cerebro, que se mide en cm³")],
    worked=[
        ("Clasificar evidencia", "Se halla un cuenco de barro con restos de comida en una cueva. ¿Es evidencia biológica o arqueológica?", ["El cuenco lo fabricaron personas.", "No es un resto del cuerpo."], "Arqueológica"),
        ("Separar descripción e interpretación", "De un cráneo se escribe: «Mide 1.100 cm³» y «Su dueño era un gran cazador». ¿Cuál es la descripción?", ["La medida se obtiene directamente del cráneo.", "Lo de «gran cazador» es una explicación que el cráneo no demuestra."], "La primera frase es la descripción; la segunda es una interpretación"),
    ],
    mistakes=[("Decir que unas herramientas de piedra demuestran qué especie las fabricó.", "Se supone que el objeto «firma» a su autor.", "Se necesitan además restos humanos en la misma capa y su fecha."),
              ("Tomar una reconstrucción dibujada como si fuera una foto del pasado.", "No se distingue entre evidencia e interpretación.", "Pregunta qué datos del hueso sustentan el dibujo y qué partes inventó el artista.")],
    T=[
        ("{F} ¿Qué tipo de evidencia es el hallazgo B: biológica o arqueológica?", "Arqueológica", "Son herramientas y huesos con marcas, hechos por personas."),
        ("{F} ¿Qué rasgo del hallazgo A indica que caminaba en dos pies?", "La pelvis ancha y los huesos de las piernas", "La ficha dice que esos huesos muestran el caminar en dos pies."),
        ("=", "{F} ¿Cuántas veces mayor es el cerebro del hallazgo C que el del hallazgo A?", "1350//450", "Se divide el volumen de C por el de A.", " veces"),
        ("{F} ¿Qué dato no se conserva en los huesos según la ficha?", "El color de la piel y del pelo", "La ficha lo dice al describir el hallazgo D."),
        ("{F} El hallazgo D, ¿es evidencia directa o interpretación? Explica.", "Interpretación, porque es un dibujo de un artista", "Un dibujo se hace a partir del cráneo, pero incluye partes imaginadas."),
        ("=", "{F} Un cráneo de otra especie tiene 1.100 cm³. ¿Cuántos cm³ menos que el hallazgo C?", "1350-1100", "Se resta el volumen menor al mayor.", " cm³"),
        ("{F} Clasifica cada frase como descripción (D) o interpretación (I): 1) «El hallazgo B incluye huesos de animales con marcas de corte». 2) «Quienes hicieron esas marcas vivían en grupos». 3) «El hallazgo A tiene pelvis ancha». 4) «Esa especie cuidaba a sus crías».", "1 D, 2 I, 3 D, 4 I", "Las frases 1 y 3 se observan en los restos; 2 y 4 son explicaciones que se proponen."),
        ("{F} ¿Se puede afirmar con el hallazgo B qué especie fabricó las herramientas? Responde con un dato de la ficha.", "No, porque en el sitio no se hallaron huesos humanos", "Sin restos humanos en la misma capa no se sabe quién las hizo."),
        ("=", "{F} Un hallazgo E tiene un cerebro de unos 900 cm³. ¿Cuántos cm³ más que el hallazgo A?", "900-450", "Se resta el volumen de A al de E.", " cm³"),
        ("{F} Luis dice: «El hallazgo A prueba que toda su especie tenía un cerebro de 450 cm³». Corrígelo.", "Un esqueleto es un solo individuo; otros individuos pueden tener un volumen distinto", "Un caso no permite generalizar a toda la especie."),
        ("{F} ¿Cuál es la conclusión más segura sobre el hallazgo A? A) Caminaba en dos pies, pero no se sabe cómo se comunicaba; B) Caminaba en dos pies y hablaba un idioma complejo.", "A) Caminaba en dos pies, pero no se sabe cómo se comunicaba", "La evidencia (pelvis y piernas) solo sustenta el caminar en dos pies."),
        ("{F} ¿Qué evidencia nueva ayudaría a saber qué especie hizo las herramientas del hallazgo B? Da una respuesta posible.", "Un fósil humano hallado en la misma capa de tierra, o una fecha que coincida con la de una especie conocida", "Se vincula el objeto con restos de personas de la misma época."),
        ("{F} Un museo quiere exhibir el dibujo D. ¿Qué debe decir el rótulo para ser honesto?", "Que es una interpretación del artista basada en un cráneo, y que el color de la piel y del pelo no se conserva en los huesos", "El rótulo debe señalar los límites de la reconstrucción."),
    ],
    ctx=("Una profesora muestra al curso solo el dibujo D y dice: «Así eran exactamente». Usa la ficha para decir qué parte de esa frase es un error. {F}", "Es un error decir «exactamente»: el color de la piel y del pelo no se conserva y el dibujo es una interpretación", "La ficha aclara que el dibujo incluye datos que los huesos no entregan."),
    sc=[("¿Qué es una interpretación en ciencias del pasado?", "Una explicación que se propone a partir de la evidencia, no lo que se ve directamente", "Se distingue de la descripción, que sí es observable."),
        ("Un cráneo mide 1.350 cm³. ¿Es una descripción o una interpretación?", "Una descripción", "Es una medida que se obtiene directamente del hueso."),
        ("Unas herramientas de piedra, ¿son evidencia biológica o arqueológica?", "Arqueológica", "Son objetos que fabricaron personas.")],
    op=("Elige uno de los hallazgos A, B, C o D de la ficha. Escribe tres líneas: qué se ve (descripción), qué se puede interpretar y qué no se puede saber con ese hallazgo. {F}",
        "Hallazgo B: se ven herramientas y huesos con marcas; se puede interpretar que se procesaba carne; no se sabe qué especie fue ni cuántas personas.",
        ["la descripción solo nombra lo observado", "la interpretación es razonable", "el límite está bien indicado"], ["tres líneas escritas"], ["mezclar interpretación en la descripción", "no señalar ningún límite"],
        "Pide que diga qué evidencia adicional haría más segura su interpretación."),
    reinforce="Escribe dos frases sobre un objeto de tu casa: una que lo describa y otra que interprete para qué se usó.",
    extend="Escribe una pregunta que la ficha 2 no permite contestar y qué evidencia haría falta.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (casos de ejemplo, hechos para este cuaderno). "
     "Caso 1: un grupo de Homo sapiens vive en una zona fría de Europa durante una glaciación; construye refugios de pieles y huesos, mantiene fogatas y cose ropa de piel con agujas de hueso. "
     "Caso 2: un grupo vive en la sabana de África; recolecta frutos y semillas, caza en grupo y se desplaza cuando cambian las lluvias. "
     "Caso 3: un grupo vive en una costa; recolecta mariscos, pesca con arpones de hueso y deja grandes montones de conchas. "
     "Dato general: una generación dura unos 25 años, y un cambio biológico en una población puede tardar miles de generaciones; un cambio cultural puede ocurrir en una sola generación.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar el ambiente, los cambios del cuerpo y la cultura de los grupos humanos. Sirve para explicar cómo la humanidad pudo vivir en lugares muy distintos.",
    prior=["Sé que hubo varias especies humanas en el pasado.", "Sé leer una descripción de un ambiente.", "Sé que Homo sapiens vive en todos los continentes."],
    explain=[
        "Los grupos humanos se adaptaron a ambientes muy distintos: zonas frías, sabanas, costas y montañas. Los factores geográficos, como el clima, el agua, el relieve y los recursos disponibles, influyeron en qué comían, dónde vivían y qué herramientas fabricaban.",
        "Hay dos formas de adaptación. La adaptación biológica es un cambio en el cuerpo de una población que se hereda y tarda miles de generaciones, como una piel con más melanina que protege mejor del sol intenso. La adaptación cultural son soluciones creadas y aprendidas, como el fuego, la ropa, los refugios y las herramientas, y puede ocurrir en una sola generación.",
        "La cultura permitió que Homo sapiens ocupara casi todos los ambientes sin esperar cambios del cuerpo. Algunas diferencias de aspecto entre poblaciones, como el color de la piel, se relacionan con esa historia de adaptación y no hacen superior a ninguna: todas las personas pertenecen a la misma especie. Los casos se explican con varios factores, no con uno solo.",
    ],
    vocab=[("factor geográfico", "rasgo del lugar, como el clima, el agua o el relieve, que influye en la vida"), ("adaptación biológica", "cambio del cuerpo de una población que se hereda, a lo largo de muchas generaciones"), ("adaptación cultural", "solución creada y aprendida por un grupo, como la ropa o el fuego"), ("generación", "periodo entre el nacimiento de padres e hijos, de unos 25 años"), ("recurso", "algo del ambiente que las personas usan, como agua, plantas o piedra")],
    worked=[
        ("Clasificar una adaptación", "Un grupo cose mantas de piel para pasar el invierno. ¿Es adaptación biológica o cultural?", ["La manta se fabrica y se aprende.", "No es un cambio del cuerpo."], "Cultural"),
        ("Calcular generaciones", "Si una generación dura 25 años, ¿cuántas generaciones hay en 500 años?", ["Cada generación equivale a 25 años.", "Divido: 500 ÷ 25 = 20."], "20 generaciones"),
    ],
    mistakes=[("Pensar que las diferencias de aspecto entre poblaciones muestran personas más o menos desarrolladas.", "Se confunden adaptaciones al ambiente con jerarquías.", "Son adaptaciones de una misma especie; no hacen superior a nadie."),
              ("Atribuir la vida de un grupo a un solo factor, por ejemplo el frío.", "Se ignora que influyen varios factores a la vez.", "Considera clima, recursos, agua y cultura juntos.")],
    T=[
        ("{F} ¿Qué recurso usa el caso 3 para obtener alimento del mar? Nombra un recurso.", "Mariscos o peces", "La ficha dice que recolecta mariscos y pesca."),
        ("{F} En el caso 1, ¿qué usa el grupo para coser la ropa de piel?", "Agujas de hueso", "Lo dice la ficha."),
        ("{F} En el caso 2, ¿qué hace el grupo cuando cambian las lluvias?", "Se desplaza", "La ficha lo indica."),
        ("{F} Clasifica como adaptación biológica (B) o cultural (C): 1) coser ropa de piel; 2) tener una piel con más melanina que protege del sol intenso; 3) mantener una fogata; 4) fabricar un arpón de hueso.", "1 C, 2 B, 3 C, 4 C", "Solo la piel es un rasgo del cuerpo que se hereda; lo demás se crea y se aprende."),
        ("{F} ¿Cuál de los tres casos vive de manera más claramente ligada al mar?", "El caso 3", "Recolecta mariscos y pesca con arpones."),
        ("{F} ¿Por qué el caso 1 necesita refugios y ropa más abrigados que el caso 2?", "Porque vive en una zona fría durante una glaciación", "El clima es un factor geográfico que influye en la vida."),
        ("=", "{F} ¿Cuántas generaciones hay en 750 años?", "750//25", "Se divide por los 25 años de una generación.", " generaciones"),
        ("=", "{F} Un cambio biológico tarda 4.000 generaciones. ¿Cuántos años son?", "4000*25", "Se multiplica por los 25 años de cada generación.", " años"),
        ("{F} Un grupo del caso 2 llega a una zona fría. ¿Qué adaptación le permitirá sobrevivir más rápido: una biológica o una cultural? Explica con el dato general de la ficha.", "Una cultural, porque puede aparecer en una sola generación", "Los cambios del cuerpo tardan miles de generaciones."),
        ("{F} Mateo dice: «El caso 1 es más avanzado que el caso 2 porque usa ropa». Corrígelo.", "Cada grupo resolvió su ambiente; en la sabana la ropa abrigada no era necesaria", "Las soluciones culturales dependen del lugar y no miden quién es superior."),
        ("{F} Un compañero afirma: «Los grupos humanos viven en lugares distintos solo por el clima». Nombra otro factor de la ficha que influya.", "Los recursos disponibles, como los mariscos de la costa o los frutos de la sabana", "Hay varios factores: clima y recursos, entre otros."),
        ("{F} ¿Qué prueba la acumulación de conchas del caso 3 y qué no prueba?", "Prueba que ese grupo comía mariscos en ese lugar; no prueba cuánto tiempo vivió allí ni cuántas personas eran", "Un montón de conchas es evidencia de alimentación, no de población."),
        ("{F} Explica en una frase por qué la cultura permitió a Homo sapiens vivir en casi todos los ambientes.", "Porque podía crear y aprender soluciones, como ropa, fuego y refugios, sin esperar cambios del cuerpo", "La adaptación cultural es más rápida que la biológica."),
    ],
    ctx=("Dos amigos discuten si el abrigo de las personas que viven en zonas muy frías es una adaptación biológica o cultural. Resuelve con la ficha. {F}", "Es cultural, porque la ropa se fabrica y se aprende", "La ropa de piel cosida con agujas es una solución creada, no un rasgo hereditario."),
    sc=[("¿Qué factor geográfico influye en que un grupo viva en refugios de pieles: el clima frío o la abundancia de frutos de la sabana?", "El clima frío", "El clima es un rasgo del lugar."),
        ("¿Cuál es más rápida: la adaptación biológica o la cultural?", "La cultural", "Puede ocurrir en una generación."),
        ("=", "{F} ¿Cuántos años hay en 40 generaciones?", "40*25", "Se multiplica por 25 años.", " años")],
    op=("Elige uno de los tres casos de la ficha y escribe cuatro líneas: el ambiente, dos adaptaciones culturales, un factor geográfico que influyó y una pregunta que quedaría abierta. {F}",
        "Caso 3: costa; arpón de hueso y recolección de mariscos; el mar como recurso; pregunta: ¿viajaban a otras costas?",
        ["describe el ambiente", "nombra dos adaptaciones culturales", "relaciona un factor geográfico con la vida del grupo"], ["cuatro líneas escritas"], ["decir que un grupo es más avanzado que otro", "usar un solo factor para explicarlo todo"],
        "Pide que explique por qué otro caso necesitaría soluciones distintas."),
    reinforce="Haz una lista de tres adaptaciones culturales de tu casa para el calor o el frío.",
    extend="Escribe cómo cambiaría la vida del caso 3 si el mar se alejara 10 km de la costa.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (fechas redondeadas y aproximadas, de ejemplo para este cuaderno). "
     "Homo sapiens sale de África hacia Asia hace unos 70.000 años; llega a Australia hace unos 50.000 años y a Europa hace unos 45.000 años. "
     "Poblamiento de América, tres explicaciones: "
     "1) Beringia: grupos cruzan a pie un puente de tierra entre Asia y América cuando el nivel del mar estaba más bajo, hace más de 15.000 años. "
     "2) Ruta costera: grupos avanzan por la costa del Pacífico usando embarcaciones simples. "
     "3) Cruce del Atlántico: grupos de Europa llegan por el hielo o el mar; es una teoría muy discutida y con poca evidencia. "
     "Evidencia: en Monte Verde, cerca de Puerto Montt (Chile), hay restos de cabañas, huesos y plantas de hace unos 14.500 años. En Norteamérica, las puntas de lanza llamadas Clovis tienen unos 13.000 años. "
     "Estudios de ADN antiguo muestran que sapiens y neandertales tuvieron hijos juntos.")
build(
    OA, 4, F,
    use="Aprenderé a explicar cómo Homo sapiens se dispersó por el planeta y a comparar las teorías del poblamiento de América. Sirve para entender por qué las explicaciones cambian con nuevas evidencias.",
    prior=["Sé que Homo sapiens apareció en África.", "Sé distinguir evidencia e interpretación.", "Sé leer una línea de tiempo."],
    explain=[
        "Homo sapiens apareció en África y, con el tiempo, se dispersó por casi todo el planeta. Los grupos se desplazaron por tierra y por mar, siguiendo recursos como animales y plantas, y llegaron a Asia, Australia y Europa. No fue una carrera hacia un destino, sino movimientos de grupos pequeños que se mezclaron o se separaron.",
        "Para América hay varias teorías. La más conocida dice que los grupos cruzaron Beringia, un puente de tierra entre Asia y América que quedó libre cuando el mar estaba más bajo. Otra propone una ruta costera por el Pacífico en embarcaciones simples. Una tercera, el cruce del Atlántico, tiene poca evidencia. Cada teoría debe comprobarse con restos reales y sus fechas.",
        "Monte Verde, en Chile, tiene restos de unos 14.500 años, más antiguos que las puntas Clovis de unos 13.000 años. Eso lleva a pensar que los primeros grupos llegaron antes y se movieron rápido hacia el sur. Las explicaciones pueden cambiar si aparecen hallazgos nuevos: la ciencia revisa sus conclusiones.",
    ],
    vocab=[("dispersión", "movimiento de grupos humanos que ocupan nuevos territorios"), ("poblamiento", "proceso por el que un lugar comienza a ser habitado"), ("Beringia", "puente de tierra que unió Asia y América cuando el mar estaba más bajo"), ("ruta costera", "camino por la orilla del mar, usando embarcaciones simples"), ("ADN antiguo", "material genético obtenido de restos muy antiguos")],
    worked=[
        ("Comparar fechas de dos hallazgos", "Un sitio A tiene restos de 12.000 años y un sitio B de 16.000 años. ¿Cuántos años más antiguo es B?", ["Busco las fechas.", "Resto: 16.000 − 12.000 = 4.000."], "4.000 años"),
        ("Evaluar una teoría", "Si aparecen restos fechados en 20.000 años en Sudamérica, ¿qué idea sobre la fecha de llegada de los primeros grupos se ve afectada?", ["Las teorías dicen que la llegada fue hace unos 15.000 años o más.", "Una fecha mayor obliga a retroceder el momento de llegada."], "La fecha propuesta para la llegada tendría que retroceder"),
    ],
    mistakes=[("Decir que el poblamiento de América ya está totalmente explicado y no puede cambiar.", "Se olvida que nuevos hallazgos pueden modificar las fechas.", "Presenta las teorías con su evidencia y su límite."),
              ("Dibujar una flecha que va solo en una dirección, como un camino de progreso.", "Se piensa que los grupos humanos avanzaron hacia un fin.", "Los grupos se desplazaron, se separaron, se mezclaron y a veces volvieron.")],
    T=[
        ("{F} ¿En qué continente está Monte Verde?", "En América (Chile, en Sudamérica)", "La ficha lo ubica cerca de Puerto Montt, Chile."),
        ("{F} ¿Qué teoría propone un puente de tierra entre Asia y América?", "La de Beringia", "La ficha la describe como puente de tierra con el mar más bajo."),
        ("=", "{F} ¿Cuántos años pasaron entre la salida de África hacia Asia y la llegada a Australia?", "70000-50000", "Se restan las fechas de la ficha.", " años"),
        ("{F} ¿Qué especie humana tuvo hijos con Homo sapiens según los estudios de ADN antiguo?", "Los neandertales", "La ficha lo dice al final."),
        ("=", "{F} ¿Cuántos años más antiguo es Monte Verde que las puntas Clovis?", "14500-13000", "Se restan las dos fechas de la ficha.", " años"),
        ("{F} Ordena de la llegada más antigua a la más reciente: Europa, Australia, Monte Verde (América del Sur).", "Australia, Europa, Monte Verde", "Las fechas son 50.000, 45.000 y 14.500 años."),
        ("{F} ¿Cuál de las tres teorías de América tiene menos evidencia según la ficha?", "El cruce del Atlántico", "La ficha la llama muy discutida y con poca evidencia."),
        ("{F} Clasifica cada hallazgo como evidencia biológica (B) o arqueológica (A): 1) cabañas de Monte Verde; 2) puntas de lanza Clovis; 3) ADN antiguo de un hueso.", "1 A, 2 A, 3 B", "Los dos primeros son obras humanas y el ADN viene de restos del cuerpo."),
        ("=", "{F} Si un sitio de Alaska tuviera 16.000 años y Monte Verde tiene 14.500 años, ¿cuántos años más antiguo sería el sitio de Alaska?", "16000-14500", "Se restan las dos edades.", " años"),
        ("{F} Un compañero dice: «Monte Verde demuestra que la teoría de Beringia es falsa». Corrígelo.", "No: Monte Verde muestra que la llegada fue más antigua que Clovis, pero Beringia o la ruta costera siguen siendo posibles", "Un hallazgo cambia las fechas, no elimina por sí solo las rutas."),
        ("{F} ¿Qué relación hay entre la ubicación de Monte Verde, tan al sur de América, y la fecha de llegada de los primeros grupos?", "Que llegaron antes de hace 14.500 años, porque recorrer ese camino toma tiempo", "Para llegar tan al sur, los grupos tuvieron que moverse antes."),
        ("{F} Ana dibuja una flecha recta de África a Chile con el título «El camino del progreso humano». Explica el error.", "Los movimientos no fueron una carrera recta hacia un destino; hubo grupos que se separaron, se mezclaron y volvieron", "La dispersión fue un conjunto de desplazamientos, no un progreso."),
        ("{F} Si se hallara un sitio en Chile con restos de 18.000 años, ¿qué idea de la ficha deberías revisar?", "La fecha de la llegada de los primeros grupos a América del Sur", "Un hallazgo más antiguo que Monte Verde obligaría a retroceder esa fecha."),
    ],
    ctx=("Una guía de museo dice: «Los primeros americanos caminaron desde Asia». Usa la ficha para completar la frase con otra posibilidad. {F}", "También pudieron avanzar por la costa del Pacífico en embarcaciones simples", "La ficha propone la ruta costera como otra teoría."),
    sc=[("¿Qué es Beringia?", "Un puente de tierra entre Asia y América", "Quedó libre cuando el nivel del mar estaba más bajo."),
        ("¿Cuál es más antiguo: Monte Verde o las puntas Clovis?", "Monte Verde", "Tiene unos 14.500 años contra unos 13.000."),
        ("=", "{F} ¿Cuántos años pasaron entre la llegada de Homo sapiens a Australia y a Europa?", "50000-45000", "Se restan las dos fechas de la ficha.", " años")],
    op=("Haz un mapa mudo sencillo de los continentes y dibuja flechas con las rutas de la ficha (África–Asia–Australia–Europa y las rutas a América). Escribe junto a cada flecha una fecha aproximada y el tipo de evidencia que la apoya. {F}",
        "Flecha de África a Asia con «70.000 años», otra a Australia con «50.000 años», y una flecha a América por Beringia con «15.000 años o más».",
        ["usa las fechas de la ficha", "indica al menos dos rutas a América", "nombra evidencia o reconoce que es una teoría"], ["mapa con flechas", "fechas anotadas"], ["dibujar una sola ruta como si fuera segura", "olvidar que las fechas son aproximadas"],
        "Pide que explique qué hallazgo podría cambiar una de sus flechas."),
    reinforce="Repite en voz alta las tres teorías del poblamiento de América y la evidencia de cada una.",
    extend="Escribe una pregunta para el equipo que excava Monte Verde.",
)
