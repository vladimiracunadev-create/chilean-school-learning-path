"""Lengua y Literatura EPJA Media Nivel 1, módulo 3: OAD-10, organizar la información recopilada sobre una persona de la cultura chilena o latinoamericana (esquemas, coherencia y cohesión, normas de citación). Personas y fuentes inventadas; todo se resuelve en papel."""
from __future__ import annotations

from epja_leli_nm1_c_common import build

O = "EPJA-LELI-NM1-OAD-10"

F1 = ("Apuntes sueltos (inventados) sobre don Armando Fuentes, pescador artesanal y dirigente de una caleta ficticia, anotados tal como aparecieron en las fuentes: "
      "(1) embarcó por primera vez a los 16 años; (2) en 1985 fundó el sindicato de pescadores de la caleta (acta del sindicato); "
      "(3) enseñaba nudos a los jóvenes (entrevista a un vecino, 2016); (4) en 1999 consiguió una bodega común para guardar redes (acta del sindicato); "
      "(5) la bodega servía a 25 familias (acta del sindicato); (6) arreglaba redes en su casa los domingos (entrevista a un vecino, 2016).")

F2 = ("Datos (inventados) sobre doña Lidia Carrasco, profesora rural que formó una biblioteca para su comunidad en una localidad ficticia. "
      "(a) En 1990 reunió 40 libros donados por vecinos. (b) La biblioteca funcionaba los sábados en la sala de la escuela. (c) En 1995 ya tenía 200 libros. "
      "(d) Prestaba libros anotándolos en un cuaderno de registro. (e) Organizaba lecturas en voz alta para personas adultas. (f) Dicen que era muy querida. "
      "Fuentes: (a) y (c) salen del acta de la junta de vecinos; (b), (d) y (e) salen de una entrevista a una socia de la biblioteca; (f) no tiene fuente.")

F3 = ("Notas en bruto (inventadas) sobre doña Rosa Oyarzún, tejedora que fundó un taller de telar. Fuente A: acta del taller (1992). Fuente B: entrevista a una tejedora (2018). Fuente C: sitio sin autor ni fecha. "
      "N1 (A): en 1992 se fundó el taller con 6 tejedoras. N2 (B): doña Rosa enseñaba a teñir lana con plantas del lugar. N3 (A): en 1996 el taller tenía 15 tejedoras. "
      "N4 (B): el taller se fundó en 1992. N5 (C): doña Rosa es «la tejedora más famosa de América». N6 (B): cada tejedora aportaba una cuota mensual para comprar lana.")

F4 = ("Oraciones sueltas (inventadas) sobre don Armando Fuentes: 1) Don Armando fundó el sindicato en 1985. 2) Los pescadores tenían problemas para guardar sus redes. "
      "3) Don Armando consiguió una bodega común en 1999. 4) La bodega servía a 25 familias. 5) Los jóvenes aprendían nudos con él.")

F5 = ("Notas de dos fuentes (inventadas) sobre doña Teresa Ibáñez, fundadora de una radio comunitaria ficticia. "
      "Fuente A: libro «Voces del cerro» de Paula Soto, 2015. Nota 1: la radio comenzó a emitir en 2002 desde una sala prestada. Nota 2: al principio transmitía dos horas al día. Nota 3: en 2010 transmitía doce horas al día. "
      "Fuente B: entrevista a un locutor, hecha por Radio del Cerro (ficticia) en 2019. Nota 4: doña Teresa enseñaba a los vecinos a usar los equipos. Nota 5: para comprar cintas y cables hacían una once solidaria cada mes. Nota 6: los vecinos participaban con programas de noticias del barrio.")

F6 = ("Texto (inventado) de una estudiante sobre doña Lidia Carrasco: «Doña Lidia fue muy querida. La biblioteca tenía 200 libros en 1995. La biblioteca se formó en 1990 con 40 libros. "
      "Los sábados funcionaba en la sala de la escuela. La biblioteca prestaba libros con un cuaderno. La biblioteca organizaba lecturas para adultos.» "
      "Lista de verificación (inventada): 1) orden lógico o cronológico; 2) sin repeticiones innecesarias; 3) conectores que unen las ideas; 4) cada dato con su cita; 5) título que anuncia la idea principal.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que ya sé ordenar en la vida diaria y lo aplico a los apuntes de una investigación: agrupo y ordeno la información.",
    prior=["Sé que cada dato tiene una fuente.", "Ordeno boletas, papeles o compras por tipo o fecha.", "Distingo un dato de una opinión."],
    explain=[
        "Tú ya organizas información todos los días: separas las boletas por mes, ordenas las cuentas del hogar o agrupas la lista de compras por sección. Con los apuntes de una investigación se hace lo mismo antes de escribir.",
        "Los apuntes sueltos se agrupan por tema: por ejemplo, inicios, trabajo y comunidad. Dentro de cada grupo, los hechos se pueden ordenar por fecha, de lo más antiguo a lo más reciente. Cada apunte conserva el nombre de su fuente.",
        "Un apunte que es una opinión, como «fue el mejor de todos», no se mezcla con los hechos: se anota aparte o se descarta. Si dos apuntes dicen casi lo mismo, se unen en una sola idea con sus datos.",
    ],
    vocab=[("agrupar", "reunir datos que tratan del mismo tema"), ("orden cronológico", "orden de los hechos de lo más antiguo a lo más reciente"), ("tema", "asunto del que trata un grupo de datos"), ("apunte", "nota breve con un dato y su fuente")],
    worked=[
        ("Agrupar por tema", "Tienes tres apuntes: «fundó una feria», «enseñaba a leer a sus vecinos» y «consiguió una sede» (ejemplo).", ["Veo qué apuntes hablan de la organización de la comunidad: feria y sede.", "El que habla de enseñar queda en otro grupo."], "Grupo 1: organización (feria, sede); grupo 2: enseñanza (leer)"),
        ("Ordenar por fecha", "Hechos: 45 puestos en 2005; feria fundada en 1995 (ejemplo).", ["Busco el año más antiguo: 1995.", "Pongo después el siguiente: 2005."], "1995 fundación; 2005 con 45 puestos"),
    ],
    mistakes=[("Juntar todos los apuntes en un párrafo, en el orden en que los anotaste.", "El orden en que los hallaste no es el orden que ayuda a leer.", "Agrupa por tema y ordena los hechos por fecha."),
              ("Mezclar opiniones con hechos en el mismo grupo.", "Una opinión no se puede comprobar como un hecho.", "Anota las opiniones aparte o descártalas.")],
    T=[
        ("abc", "{F} ¿Qué grupo reúne bien los apuntes 2, 4 y 5?", "La organización de la caleta: sindicato y bodega", "Su juventud en el mar", "Sus pasatiempos de domingo", "Los tres hablan del sindicato y de la bodega común."),
        ("ab", "{F} ¿Qué apunte ayuda a responder «¿cómo empezó a trabajar?»", "El 1: embarcó por primera vez a los 16 años", "El 5: la bodega servía a 25 familias", "El apunte 1 cuenta su primera vez en el mar."),
        ("{F} ¿Cuántas familias servía la bodega común? Escribe solo el número.", "25", "El apunte 5 indica 25 familias."),
        ("abc", "Para mostrar cómo cambió la vida de una persona, ¿qué criterio de orden sirve?", "El orden cronológico, de lo más antiguo a lo más reciente", "El orden alfabético de las palabras", "El largo de cada apunte", "El orden por fechas muestra cómo cambian las cosas con el tiempo."),
        ("ab", "{F} ¿Qué ocurrió primero: la fundación del sindicato (1985) o la bodega común (1999)?", "La fundación del sindicato", "La bodega común", "El año 1985 es anterior al año 1999, por eso va primero."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación del sindicato y la obtención de la bodega común?", "1999 - 1985", "Se restan los años de los dos hechos para saber el tiempo entre ellos.", "años"),
        ("abc", "{F} ¿Qué apuntes pertenecen al grupo «enseñanza y vida cotidiana»?", "El 3 y el 6", "El 2 y el 4", "El 1 y el 5", "Enseñar nudos y arreglar redes son actividades de la vida cotidiana."),
        ("abc", "Un apunte dice «fue el mejor pescador de todos». ¿Dónde lo ubicas?", "Aparte, como opinión, o lo descarto porque no se puede comprobar", "Entre los hechos, porque es importante", "Lo copio dos veces para destacarlo", "Una opinión no se mezcla con los datos que se pueden comprobar."),
        ("{F} ¿De qué fuente salen los apuntes 2, 4 y 5? Responde: acta o entrevista.", "acta", "Los tres indican que provienen del acta del sindicato."),
        ("ab", "Una persona junta todos los apuntes en un párrafo sin ordenarlos. Otra los agrupa por tema y los ordena por fechas. ¿Qué texto será más claro?", "El de la segunda persona, porque quien lee puede seguir un orden", "El de la primera persona, porque incluye todo de una vez", "Agrupar y ordenar ayuda a quien lee a seguir el hilo."),
        ("abc", "{F} Los apuntes 4 y 5 hablan de la bodega. ¿Qué haces con ellos?", "Los junto en un solo grupo y los uno en una idea con dos datos", "Elimino el 4 y dejo solo la cifra", "Los separo en grupos distintos para que parezca más largo", "Dos datos de un mismo asunto se reúnen en una idea."),
        ("abc", "{F} Quieres un esquema con tres grupos. ¿Qué reparto es correcto?", "Inicios (1); sindicato y bodega (2, 4, 5); enseñanza y vida diaria (3, 6)", "Inicios (2, 4); sindicato (1); enseñanza (3, 5, 6)", "Inicios (3); sindicato (6); bodega (1, 2, 4, 5)", "El primer reparto agrupa cada apunte con otros del mismo tema."),
        ("{F} ¿Cuántos apuntes provienen de la entrevista de 2016? Escribe solo el número.", "2", "Los apuntes 3 y 6 salen de la entrevista a un vecino."),
    ],
    ctx=("abc", "Tienes anotaciones de una reunión de vecinos mezcladas: fechas, acuerdos y dudas. Debes entregar un resumen a la directiva. ¿Qué haces primero?", "Agruparlas por tema y ordenarlas antes de escribir", "Copiarlas en el orden en que están, sin revisar", "Escribir solo la última anotación", "Agrupar y ordenar permite escribir un resumen claro."),
    sc=[("En Lengua y Literatura: ¿qué significa agrupar apuntes?", "Reunir los que tratan del mismo tema", "Agrupar es juntar lo que se parece."),
        ("En Lengua y Literatura: ¿qué es el orden cronológico?", "Ordenar los hechos de lo más antiguo a lo más reciente", "Los hechos siguen el paso del tiempo, del pasado al presente."),
        ("En Lengua y Literatura: ¿qué haces con una opinión entre tus apuntes?", "La anoto aparte o la descarto, porque no se puede comprobar", "No se mezcla con los hechos.")],
    op=("{F} En tu cuaderno haz una tabla de tres columnas: grupo, apuntes (por su número) y fuente. Forma tres grupos con los seis apuntes y ponles un título. Dentro del grupo que tenga fechas, ordena los hechos del más antiguo al más reciente.",
        "Grupo 1: Inicios (apunte 1). Grupo 2: Sindicato y bodega (apuntes 2, 4 y 5), fuente: acta; orden: 1985, 1999. Grupo 3: Enseñanza y vida diaria (apuntes 3 y 6), fuente: entrevista.",
        ["los seis apuntes están en algún grupo", "cada grupo tiene un título que explica su tema", "los hechos con fecha están en orden cronológico"],
        ["tabla de tres columnas con tres grupos titulados"],
        ["dejar un apunte sin grupo", "poner títulos como «varios»"],
        "Pregunta de revisión: «¿Se entiende por qué cada apunte está en ese grupo?»."),
    reinforce="Ordena por tema una lista de tus gastos del mes (ejemplos inventados) en tres grupos y ponles título.",
    extend="Anota seis hechos de la historia de tu barrio (sin datos personales) y organízalos en grupos y por orden cronológico.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy conozco las herramientas para organizar información: esquema, categorías, línea de tiempo, idea principal y detalles.",
    prior=["Agrupo apuntes por tema.", "Ordeno hechos por fecha.", "Distingo hechos de opiniones."],
    explain=[
        "Un esquema es un dibujo en papel que muestra cómo se organiza un texto. Tiene un título, grupos que llamamos categorías y, dentro de cada una, una idea principal con sus detalles. Sirve para escribir con orden.",
        "La idea principal es lo más importante de un grupo de datos; los detalles la explican o la apoyan. Si el título de un grupo es «varios» o «otros», no ayuda: debe decir qué une a esos datos.",
        "Una línea de tiempo es una recta con años, de lo más antiguo a lo más reciente, y debajo de cada año un hecho. Se usa cuando importa el orden en que ocurrieron las cosas. Los datos sin fuente o sin comprobación se dejan fuera del esquema.",
    ],
    vocab=[("esquema", "organización en papel de las ideas de un texto"), ("categoría", "grupo de datos con un título que los une"), ("idea principal", "lo más importante de un grupo, que los detalles explican"), ("línea de tiempo", "recta con hechos ordenados por fecha")],
    worked=[
        ("Titular un grupo", "Datos: «la feria tenía 20 puestos» y «la feria tenía 45 puestos» (ejemplo).", ["Busco qué los une: ambos hablan de cuántos puestos había.", "El título dice eso: «Crecimiento de la feria»."], "Título: Crecimiento de la feria"),
        ("Armar una línea de tiempo", "Hechos: 2000, 20 puestos; 2010, 45 puestos (ejemplo).", ["Dibujo una recta y marco 2000 a la izquierda.", "Marco 2010 a la derecha y anoto el hecho de cada año."], "2000: 20 puestos; 2010: 45 puestos"),
    ],
    mistakes=[("Poner títulos vagos como «otros» a un grupo.", "Un título vago no dice qué une a los datos.", "Escribe un título que nombre la idea del grupo."),
              ("Incluir en el esquema un dato sin fuente, como si fuera un hecho.", "No se puede comprobar y debilita el trabajo.", "Déjalo fuera o búscale una fuente.")],
    T=[
        ("abc", "En Lengua y Literatura: ¿qué es la idea principal de un grupo de datos?", "La idea central que los demás datos explican", "El dato más largo del grupo", "La primera frase que aparece", "La idea principal resume lo más importante y los detalles la apoyan."),
        ("abc", "{F} ¿Qué título resume mejor los datos (a) y (c)?", "Crecimiento de la colección de libros", "Horario de la biblioteca", "Actividades para adultos", "(a) y (c) dan la cantidad de libros en dos años."),
        ("{F} ¿Cuántos libros tenía la biblioteca en 1995? Escribe solo el número.", "200", "El dato (c) indica 200 libros."),
        ("ab", "{F} ¿En qué categoría pones el dato (b), que la biblioteca funcionaba en la sala de la escuela los sábados?", "Funcionamiento", "Colección", "El dato (b) cuenta cómo y dónde funcionaba."),
        ("abc", "¿Para qué sirve una línea de tiempo?", "Para ordenar hechos por fecha de lo más antiguo a lo más reciente", "Para comparar opiniones de distintas personas", "Para contar las palabras de un texto", "Una línea de tiempo muestra el orden de los hechos."),
        ("abc", "En Lengua y Literatura: ¿qué es un detalle en un esquema?", "Un dato que apoya o explica la idea principal", "Una idea que reemplaza al título", "Una opinión sin respaldo", "Los detalles aportan datos que explican la idea principal."),
        ("=", "{F} ¿Cuántos libros más tenía la biblioteca en 1995 que en 1990?", "200 - 40", "Se restan los libros de 1990 a los de 1995 para ver el aumento.", "libros"),
        ("abc", "{F} Haz una línea de tiempo con los datos que tienen año. ¿Cuál es correcta?", "1990: 40 libros donados; 1995: 200 libros", "1995: 40 libros donados; 1990: 200 libros", "1990: 200 libros; 1995: sala de la escuela", "Los años van de menor a mayor y cada cifra queda con su año."),
        ("abc", "{F} ¿Dónde ubicas el dato (e), las lecturas en voz alta para adultos?", "En una categoría de actividades", "En la categoría de colección", "Lo descartas, porque no tiene año", "Las lecturas son una actividad de la biblioteca."),
        ("ab", "{F} ¿Por qué el dato (f), «dicen que era muy querida», no entra en el esquema como hecho?", "Porque es una opinión sin fuente que se pueda comprobar", "Porque es demasiado corto para un esquema", "Sin fuente y sin hechos, no es un dato comprobable."),
        ("abc", "Alguien propone el título «Datos varios» para un grupo de apuntes. ¿Qué problema tiene?", "No dice la idea que une al grupo, por lo que no orienta a quien lee", "Es demasiado preciso", "No tiene verbos", "Un título útil dice qué une a los datos del grupo."),
        ("abc", "{F} Para un esquema con dos categorías, ¿cuál es la mejor organización de (a), (b), (c) y (d)?", "Colección: (a) y (c); funcionamiento: (b) y (d)", "Colección: (a) y (d); funcionamiento: (b) y (c)", "Colección: (b) y (d); funcionamiento: (a) y (c)", "Las cifras de libros van juntas; el lugar y el registro describen el funcionamiento."),
        ("{F} ¿Cuántos de los datos (a) a (f) son hechos con fuente y no opiniones? Escribe solo el número.", "5", "Todos tienen fuente indicada menos (f), que es una opinión."),
    ],
    ctx=("abc", "Debes presentar en el centro de estudios una cronología de cinco hechos de la fundación de una junta de vecinos. ¿Qué herramienta te sirve más?", "Una línea de tiempo con los hechos ordenados por fecha", "Una lista de opiniones sobre el barrio", "Un listado alfabético de nombres", "La línea de tiempo muestra el orden de los hechos."),
    sc=[("En Lengua y Literatura: ¿qué es un esquema?", "La organización en papel de las ideas de un texto", "Muestra título, categorías e ideas con sus detalles."),
        ("En Lengua y Literatura: ¿qué es una categoría?", "Un grupo de datos con un título que los une", "Reúne datos del mismo tema con un título."),
        ("En Lengua y Literatura: ¿cuándo conviene una línea de tiempo?", "Cuando importa el orden en que ocurrieron los hechos", "Se usa para hechos con fecha.")],
    op=("{F} Dibuja en tu cuaderno un esquema con un título, dos categorías con título propio y los datos (a) a (e) repartidos con la fuente de cada uno. Aparte, haz una línea de tiempo con los dos datos que tienen año. Deja fuera el dato (f) y explica en una línea por qué.",
        "Título: La biblioteca de doña Lidia. Colección: (a) 1990, 40 libros (acta); (c) 1995, 200 libros (acta). Funcionamiento: (b), (d), (e) (entrevista). (f) queda fuera porque es una opinión sin fuente.",
        ["tiene título y dos categorías con título propio", "reparte los datos (a) a (e) con su fuente", "la línea de tiempo está en orden y deja fuera (f) con explicación"],
        ["un esquema con título y dos categorías, una línea de tiempo y una explicación de una línea"],
        ["poner títulos como «varios»", "incluir el dato (f)"],
        "Pregunta de revisión: «¿El título de cada categoría dice qué une a sus datos?»."),
    reinforce="Inventa cuatro fechas de la historia de una feria o de un taller y arma con ellas una línea de tiempo.",
    extend="Elige un tema que conozcas (un oficio, una fiesta del barrio) y arma un esquema con título y tres categorías.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo paso a paso cómo pasar de notas en bruto a un esquema: marcar la fuente, descartar, agrupar, ordenar y titular.",
    prior=["Agrupo apuntes por tema.", "Conozco el esquema y la línea de tiempo.", "Evalúo la confiabilidad de una fuente."],
    explain=[
        "Pasar de notas en bruto a un esquema sigue cinco pasos. Primero, lee todas las notas y marca la fuente de cada una. Segundo, descarta las repetidas y las que no tienen respaldo. Tercero, agrupa por tema.",
        "Cuarto, ordena los hechos dentro de cada grupo, por fecha si importa la secuencia. Quinto, ponle un título a cada grupo y al esquema completo. Al lado de cada dato mantén la letra de su fuente para poder citarla después.",
        "Si dos fuentes confiables dicen lo mismo, dejas un solo dato y anotas las dos fuentes: así queda más respaldado. Si una nota no cabe en ningún grupo, puedes crear un grupo nuevo; no la dejes suelta sin título.",
    ],
    vocab=[("notas en bruto", "apuntes tal como se anotaron, sin ordenar"), ("descartar", "dejar fuera un dato repetido o sin respaldo"), ("respaldo", "fuente confiable que apoya un dato"), ("esquema final", "organización lista para escribir el texto")],
    worked=[
        ("Descartar y unir", "Dos notas dicen que la feria se fundó en 2001: una del acta y otra de una entrevista (ejemplo).", ["Son el mismo dato.", "Dejo un solo dato y anoto las dos fuentes."], "Feria fundada en 2001 (acta y entrevista)"),
        ("Descartar por falta de respaldo", "Una nota de un sitio sin autor dice «el mejor maestro del continente» (ejemplo).", ["No sé quién lo afirma ni en qué se apoya.", "Es una exageración, no un dato comprobable."], "Se descarta del esquema"),
    ],
    mistakes=[("Saltarse el paso de marcar la fuente de cada nota.", "Después no sabrás qué dato citar ni de dónde salió.", "Marca la fuente al lado de cada nota desde el comienzo."),
              ("Dejar una nota suelta, sin grupo ni título.", "Una nota sin grupo queda fuera del hilo del texto.", "Ubícala en el grupo que la explique o crea uno nuevo.")],
    T=[
        ("abc", "¿Cuál es el primer paso para organizar notas en bruto?", "Leer todas las notas y marcar de qué fuente es cada una", "Escribir el informe final de inmediato", "Borrar las notas que parezcan largas", "Primero hay que conocer el material y su procedencia."),
        ("ab", "{F} ¿Qué notas se repiten?", "La N1 y la N4, que dicen que el taller se fundó en 1992", "La N2 y la N6, que hablan de lana", "N1 y N4 dan el mismo dato, el año de fundación."),
        ("{F} ¿Cuántas tejedoras tenía el taller en 1996? Escribe solo el número.", "15", "La nota N3 indica 15 tejedoras en 1996."),
        ("abc", "{F} ¿Qué nota se descarta por no tener respaldo?", "La N5, de un sitio sin autor, que exagera", "La N3, que sale del acta", "La N6, que sale de la entrevista", "La N5 no tiene autor, fecha ni pruebas."),
        ("=", "{F} ¿Cuántas tejedoras más tenía el taller en 1996 que cuando se fundó?", "15 - 6", "Se restan las tejedoras de la fundación a las de 1996.", "tejedoras"),
        ("abc", "{F} Dos fuentes dicen que el taller se fundó en 1992. ¿Qué haces?", "Dejo un solo dato y anoto las dos fuentes que lo confirman", "Dejo los dos datos para que haya más información", "Dejo solo el de la entrevista, porque es más reciente", "Un dato confirmado por dos fuentes se anota una vez con ambas."),
        ("abc", "{F} ¿Qué título resume el grupo de N1, N3 y N4?", "Fundación y crecimiento del taller", "Cuotas para comprar lana", "Técnicas de teñido", "Las tres notas hablan del comienzo y del tamaño del taller."),
        ("abc", "{F} Ordena N1 y N3 de la más antigua a la más reciente. ¿Cómo queda?", "Primero 1992 con 6 tejedoras, después 1996 con 15 tejedoras", "Primero 1996 con 15 tejedoras, después 1992 con 6 tejedoras", "Solo 1996, porque es el último dato", "Los hechos se ordenan del año menor al mayor."),
        ("ab", "{F} ¿En qué grupo pones N2 y N6?", "Funcionamiento del taller: enseñanza y cuotas", "Fundación y crecimiento del taller", "Enseñar a teñir y juntar cuotas son parte del día a día del taller."),
        ("ab", "Al pasar las notas al esquema, ¿por qué conviene dejar al lado la fuente (A, B)?", "Para citar después cada dato y poder comprobarlo", "Para que el esquema se vea más largo", "La fuente al lado permite citar y comprobar."),
        ("abc", "{F} Si la nota N2 queda sin grupo en tu esquema, ¿qué haces?", "Creo un grupo nuevo que la incluya o la ubico donde mejor la explique", "La descarto sin pensarlo, porque no tiene año", "La pego al final sin título", "Una nota válida debe tener un grupo con título."),
        ("abc", "{F} ¿Cuál es el esquema final correcto?", "Título: Doña Rosa y su taller. 1) Fundación y crecimiento: N1 y N4 (A, B), N3 (A). 2) Funcionamiento: N2 (B), N6 (B)", "Título: Doña Rosa. 1) Fundación: N5 (C), N1 (A). 2) Funcionamiento: N2 (B)", "Sin título. Todas las notas en una lista, según llegaron", "El primero descarta lo dudoso, une lo repetido y mantiene las fuentes."),
        ("=", "{F} Después de unir la nota repetida y de descartar la nota sin respaldo, ¿cuántas de las seis notas quedan? Cuenta como una las notas N1 y N4.", "6 - 2", "Se restan una nota unida y una descartada de las seis notas.", "notas"),
    ],
    ctx=("abc", "Tienes ocho notas de entrevistas a vecinos para la historia de tu junta de vecinos. Dos repiten lo mismo y una exagera sin pruebas. ¿Qué haces antes de escribir?", "Unir las repetidas, descartar la que exagera y agrupar el resto con título", "Copiar las ocho tal como están", "Escoger solo las más entusiastas", "Se une lo repetido, se descarta lo dudoso y se agrupa lo demás."),
    sc=[("En Lengua y Literatura: ¿cuál es el primer paso para organizar notas en bruto?", "Leerlas y marcar la fuente de cada una", "Hay que conocer cada nota y de dónde sale."),
        ("En Lengua y Literatura: ¿qué haces con dos notas que dicen lo mismo?", "Dejo una y anoto las fuentes que la confirman", "Se unen en un solo dato con todas sus fuentes."),
        ("En Lengua y Literatura: ¿qué nota se descarta?", "La que no tiene respaldo o exagera sin pruebas", "Un dato sin respaldo no es confiable.")],
    op=("{F} Con las seis notas, arma en tu cuaderno el esquema final: título, dos categorías con título propio y los datos que se mantienen con su fuente (A o B). Escribe aparte qué notas descartaste o uniste y por qué.",
        "Título: Doña Rosa y su taller. Fundación y crecimiento: taller fundado en 1992 con 6 tejedoras (A, B); 15 tejedoras en 1996 (A). Funcionamiento: enseñaba a teñir con plantas (B); cuota mensual para lana (B). Descarté N5 por no tener respaldo y uní N1 y N4.",
        ["el esquema tiene título y dos categorías con título", "cada dato mantiene su fuente", "explica qué notas descartó o unió"],
        ["esquema con título y dos categorías, y nota de lo descartado o unido"],
        ["incluir la nota N5 como hecho", "olvidar la fuente de los datos"],
        "Pregunta de revisión: «¿Cada dato del esquema se puede rastrear hasta su fuente?»."),
    reinforce="Toma cinco anotaciones de tu semana y sigue los cinco pasos: marca, descarta, agrupa, ordena y titula.",
    extend="Escribe una lista breve con los cinco pasos para pasar de notas a un esquema, como una receta que le entregarías a otra persona.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo los recursos de coherencia y cohesión: conectores, reemplazos para no repetir y citas dentro del texto.",
    prior=["Tengo un esquema ordenado.", "Sé citar con apellido y año.", "Sé qué es un párrafo."],
    explain=[
        "Un texto es coherente cuando sus ideas siguen un orden lógico y tratan de un mismo asunto. Es cohesionado cuando las oraciones están bien unidas entre sí con conectores y con palabras que evitan repetir.",
        "Los conectores unen ideas. Para sumar: además. Para causa: porque. Para consecuencia: por eso. Para oponer: sin embargo. Para ordenar en el tiempo: primero, luego, finalmente. Elige el que corresponda a la relación entre las ideas.",
        "Para no repetir una palabra, puedes usar un pronombre (él, ella, que) o una expresión equivalente («el dirigente»). Cuando incluyas un dato de una fuente, agrega la cita al final de la oración.",
    ],
    vocab=[("coherencia", "orden lógico de las ideas en torno a un mismo asunto"), ("cohesión", "unión entre oraciones con conectores y reemplazos"), ("conector", "palabra que une ideas y muestra su relación"), ("pronombre", "palabra que reemplaza a un nombre para no repetirlo")],
    worked=[
        ("Elegir un conector", "Oraciones: «llovió toda la tarde» y «se suspendió la feria» (ejemplo).", ["La segunda es consecuencia de la primera.", "Uso «por eso»."], "Llovió toda la tarde; por eso se suspendió la feria"),
        ("Evitar la repetición", "«Doña Clara organizó la feria. Doña Clara llevó las cuentas» (ejemplo).", ["Repetir el nombre cansa a quien lee.", "Reemplazo el segundo por «ella»."], "Doña Clara organizó la feria. Ella llevó las cuentas"),
    ],
    mistakes=[("Usar «sin embargo» para sumar ideas que no se oponen.", "El conector equivocado cambia el sentido del texto.", "Antes de elegir, pregunta si las ideas suman, se oponen o una explica a la otra."),
              ("Llenar el texto de conectores sin que las ideas tengan relación.", "Un conector no arregla un orden confuso.", "Primero ordena las ideas y después únelas.")],
    T=[
        ("abc", "En Lengua y Literatura: ¿qué conector indica causa?", "porque", "luego", "sin embargo", "«Porque» introduce la razón de algo."),
        ("abc", "En Lengua y Literatura: ¿qué conector indica consecuencia?", "por eso", "además", "porque", "«Por eso» muestra el resultado de lo anterior."),
        ("abc", "En Lengua y Literatura: ¿qué conector indica oposición?", "sin embargo", "porque", "primero", "«Sin embargo» presenta una idea contraria a la anterior."),
        ("abc", "¿Qué conector sirve para ordenar acciones en el tiempo?", "luego", "porque", "sin embargo", "«Luego» indica lo que viene después."),
        ("ab", "{F} Une las oraciones 2 y 3 con una relación de consecuencia. ¿Cuál es correcta?", "Los pescadores tenían problemas para guardar sus redes; por eso don Armando consiguió una bodega común en 1999.", "Los pescadores tenían problemas para guardar sus redes; sin embargo, don Armando consiguió una bodega común en 1999.", "La bodega fue la respuesta al problema, no una oposición."),
        ("abc", "Repetir «don Armando» al comienzo de cada oración suena pesado. ¿Qué recurso evita la repetición?", "Reemplazarlo por un pronombre o una expresión como «el dirigente»", "Repetir el nombre más veces para dejar claro quién es", "Quitar todos los verbos del texto", "Los pronombres y las expresiones equivalentes dan cohesión."),
        ("abc", "{F} Une las oraciones 3 y 4 sin repetir «la bodega». ¿Cuál es mejor?", "Don Armando consiguió una bodega común en 1999, que servía a 25 familias.", "Don Armando consiguió una bodega común en 1999 y luego una bodega servía a 25 familias.", "Una bodega común consiguió don Armando, 1999, 25 familias servía.", "El «que» une las ideas sin repetir el sustantivo."),
        ("{F} ¿Cuántas familias servía la bodega? Escribe solo el número.", "25", "La oración 4 dice que servía a 25 familias."),
        ("abc", "{F} ¿Qué orden de oraciones cuenta mejor la secuencia problema, acción y resultado?", "2, 3, 4", "4, 2, 3", "3, 4, 2", "Primero el problema, luego la acción y después el resultado."),
        ("ab", "El párrafo «Consiguió la bodega. Los pescadores tenían problemas.» no se entiende bien. ¿Qué le falta?", "Un orden lógico y un conector que muestre la causa", "Más adjetivos para describir la bodega", "El problema debe ir antes y unirse con un conector causal."),
        ("abc", "{F} La oración 4 sale del acta del sindicato de 1999. ¿Qué cita lleva al final?", "(Acta del sindicato, 1999)", "(Don Armando)", "(25 familias)", "La cita nombra la fuente y su año."),
        ("abc", "{F} ¿Qué párrafo muestra mejor coherencia y cohesión?", "En 1985 don Armando fundó el sindicato. Luego, los pescadores tuvieron problemas para guardar sus redes; por eso él consiguió una bodega común en 1999, que servía a 25 familias.", "Don Armando fundó el sindicato en 1985. Los pescadores tenían problemas para guardar sus redes. Don Armando consiguió una bodega común en 1999. La bodega servía a 25 familias.", "Los jóvenes aprendían nudos con él. Además, en 1985 fundó el sindicato. Luego, los pescadores tenían problemas. Por eso la bodega servía a 25 familias en 1999.", "El primero ordena los hechos y los une con conectores adecuados."),
        ("En «los pescadores tuvieron problemas para guardar sus redes; por eso él consiguió una bodega común», ¿qué conector indica consecuencia? Escribe solo las dos palabras.", "por eso", "El conector que une el problema con la acción que lo resuelve es «por eso»."),
    ],
    ctx=("abc", "Escribes un correo a la municipalidad para explicar por qué tu junta de vecinos necesita una sala. Tienes tres razones. ¿Cómo las unes?", "Con conectores como «además» y «por eso», ordenando las razones", "Una debajo de otra, sin unirlas", "Repitiendo cada razón dos veces para insistir", "Los conectores ayudan a que la lectura sea clara."),
    sc=[("En Lengua y Literatura: ¿qué es la coherencia de un texto?", "El orden lógico de sus ideas en torno a un mismo asunto", "Las ideas siguen un hilo comprensible."),
        ("En Lengua y Literatura: ¿qué es la cohesión de un texto?", "La unión entre sus oraciones con conectores y reemplazos", "Las oraciones se enlazan entre sí."),
        ("En Lengua y Literatura: ¿para qué sirve un pronombre?", "Para reemplazar un nombre y no repetirlo", "Evita repetir palabras y da cohesión al texto.")],
    op=("{F} Con las cinco oraciones escribe en tu cuaderno un párrafo de cinco a seis líneas. Ordénalas con sentido, une al menos tres con conectores distintos, evita repetir «don Armando» más de dos veces y agrega una cita (Acta del sindicato, 1985 o 1999) donde corresponda.",
        "En 1985 don Armando fundó el sindicato (Acta del sindicato, 1985). Los pescadores tenían problemas para guardar sus redes; por eso él consiguió una bodega común en 1999, que servía a 25 familias (Acta del sindicato, 1999). Además, los jóvenes aprendían nudos con él.",
        ["ordena las ideas de forma lógica", "usa al menos tres conectores distintos y bien elegidos", "evita repeticiones y agrega citas"],
        ["párrafo de cinco a seis líneas con conectores y citas"],
        ["usar el mismo conector tres veces", "olvidar las citas"],
        "Pregunta de revisión: «Si quito los conectores, ¿se pierde la relación entre las ideas?»."),
    reinforce="Une con un conector adecuado dos oraciones de tu vida diaria: «Salí tarde» y «perdí el bus».",
    extend="Escribe cuatro oraciones sobre un oficio que conoces y únelas en un párrafo con un conector de causa, uno de consecuencia y uno de orden.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una investigación: organizo notas de dos fuentes en un esquema y las uno en párrafos con citas.",
    prior=["Paso notas a un esquema.", "Uso conectores y reemplazos.", "Cito con apellido o institución y año."],
    explain=[
        "En un trabajo real tienes notas de varias fuentes y debes organizarlas con criterio. Primero separas lo que sale de cada fuente. Después agrupas por tema y ordenas los hechos con fecha.",
        "Al escribir cada párrafo, parte con una oración que anuncie la idea principal, sigue con los datos y cierra con una oración que relacione lo dicho. Cada dato de una fuente lleva su cita al final de la oración.",
        "Si usas dos fuentes en un párrafo, cada cita se coloca donde corresponde. Así quien lee sabe de dónde sale cada afirmación y puede contrastarla con facilidad.",
    ],
    vocab=[("párrafo", "bloque de oraciones sobre una misma idea"), ("oración temática", "oración que anuncia la idea principal del párrafo"), ("cita en el texto", "apellido o institución y año entre paréntesis"), ("hilo del texto", "relación lógica que une párrafos y oraciones")],
    worked=[
        ("Titular un grupo", "Notas: «la feria tenía 20 puestos» y «la feria tenía 45 puestos» (ejemplo).", ["Ambas hablan de la cantidad de puestos.", "Muestran cambio en el tiempo."], "Título: Crecimiento de la feria"),
        ("Escribir con citas", "Dato del libro de Pedro Vega, 2012, sobre el comienzo de una feria (ejemplo).", ["Redacto la oración con el dato.", "Agrego (Vega, 2012) al final."], "La feria comenzó en 1995 (Vega, 2012)."),
    ],
    mistakes=[("Poner todas las citas juntas al final del párrafo.", "No se sabe qué dato viene de qué fuente.", "Pon la cita al final de cada oración con un dato."),
              ("Mezclar en una oración datos de dos fuentes sin citarlas.", "No se puede comprobar cuál dato sale de dónde.", "Separa los datos o cita cada fuente donde corresponda.")],
    T=[
        ("abc", "{F} ¿Qué categoría agrupa las notas 1, 2 y 3?", "Inicio y crecimiento de la radio", "Participación de los vecinos", "Financiamiento", "Las tres notas cuentan cómo comenzó y cómo creció la radio."),
        ("{F} ¿Cuántas horas al día transmitía la radio en 2010? Escribe solo el número.", "12", "La nota 3 indica doce horas al día en 2010."),
        ("=", "{F} ¿Cuántas horas más al día transmitía la radio en 2010 que al principio?", "12 - 2", "Se restan las horas iniciales a las de 2010 para ver el aumento.", "horas"),
        ("ab", "{F} ¿Qué cita corresponde a la nota 1?", "(Soto, 2015)", "(Radio del Cerro, 2019)", "La nota 1 sale del libro de Paula Soto de 2015."),
        ("abc", "{F} ¿Qué cita corresponde a la nota 5?", "(Radio del Cerro, 2019)", "(Soto, 2015)", "(Ibáñez, 2019)", "La nota 5 sale de la entrevista hecha por Radio del Cerro."),
        ("abc", "{F} ¿Cuál es el mejor párrafo inicial, con coherencia y citas?", "La radio comenzó a emitir en 2002 desde una sala prestada y al principio transmitía dos horas al día (Soto, 2015). Con el tiempo, en 2010, ya transmitía doce horas diarias (Soto, 2015).", "La radio comenzó a emitir en 2002. Transmitía dos horas al día. Transmitía doce horas al día en 2010. Tenía una sala prestada.", "Doña Teresa fue la gran fundadora que todos admiran y la radio fue la mejor.", "La primera versión ordena los datos en el tiempo y los cita."),
        ("ab", "{F} Para unir las notas 4 y 6 en una idea sobre participación, ¿qué conector conviene?", "Además", "Sin embargo", "Ambas notas muestran formas de participar, así que se suman."),
        ("abc", "{F} ¿Qué título corresponde a las notas 4, 5 y 6?", "Participación y financiamiento comunitario", "Inicio de la radio en 2002", "Horas de transmisión", "Las tres notas tratan de cómo colaboraban los vecinos."),
        ("{F} ¿Qué años de hechos aparecen en las notas de la Fuente A? Escribe los dos números separados por coma, de menor a mayor.", "2002, 2010", "Las notas 1 y 3 mencionan 2002 y 2010."),
        ("ab", "{F} Alguien ordena así: nota 3, nota 1, nota 2. ¿Qué problema tiene?", "Rompe el orden cronológico y confunde el crecimiento de la radio", "Ninguno, porque todas las notas son de la misma fuente", "Mostrar 2010 antes de 2002 desordena el relato."),
        ("abc", "{F} ¿Por qué conviene separar lo que sale del libro de lo que sale de la entrevista?", "Porque cada dato se cita con su propia fuente y se pueden contrastar", "Porque el libro siempre es más confiable", "Porque la entrevista debe ir primero siempre", "Separar las fuentes permite citar cada dato bien."),
        ("abc", "{F} ¿Cuál es el esquema más completo para organizar las seis notas?", "1) Inicio y crecimiento (notas 1 a 3, Soto, 2015); 2) Participación y financiamiento (notas 4 a 6, Radio del Cerro, 2019)", "1) Notas 1 a 6 sin títulos; 2) Opinión final", "1) Financiamiento (nota 1); 2) Participación (nota 3)", "El primero agrupa las notas por tema y mantiene sus fuentes."),
        ("{F} Si agregas el dato «en 2020, 30 vecinos hacían programas» sin fuente, ¿qué debes hacer antes de usarlo? Responde: buscar fuente o usarlo igual.", "buscar fuente", "Un dato sin fuente no se usa hasta encontrar su respaldo."),
    ],
    ctx=("abc", "Eres parte del equipo que escribe la historia de tu junta de vecinos con datos de un acta y de una entrevista. ¿Cómo escribes un párrafo con ambas fuentes?", "Agrupo los datos por tema y cito cada fuente donde corresponde", "Junto todos los datos y pongo una sola cita al final", "Uso solo la entrevista, para no citar el acta", "Cada dato debe quedar unido a su fuente."),
    sc=[("En Lengua y Literatura: ¿qué es una oración temática?", "La que anuncia la idea principal del párrafo", "Presenta el tema que desarrolla el párrafo."),
        ("En Lengua y Literatura: ¿dónde va la cita de un dato?", "Al final de la oración que lo contiene", "Cada dato lleva su cita para saber su origen."),
        ("En Lengua y Literatura: ¿por qué se organizan las notas antes de escribir?", "Para escribir con orden y no perder el hilo", "El esquema da orden al texto.")],
    op=("{F} Con las seis notas, escribe en tu cuaderno dos párrafos, uno por categoría (inicio y crecimiento; participación y financiamiento). Cada párrafo debe tener una oración que anuncie la idea, al menos dos conectores distintos y una cita por cada dato. Al final, escribe la lista de las dos referencias con los datos que tienes.",
        "Inicio y crecimiento: La radio de doña Teresa tuvo un inicio modesto. Comenzó en 2002 desde una sala prestada (Soto, 2015); al principio transmitía dos horas al día. Luego, en 2010, ya emitía doce horas diarias (Soto, 2015).",
        ["dos párrafos con una oración que anuncia la idea", "usa al menos dos conectores distintos", "cita cada dato y escribe las dos referencias"],
        ["dos párrafos con citas y lista de dos referencias"],
        ["olvidar una cita", "no ordenar los hechos por fecha"],
        "Pregunta de revisión: «¿Cada dato del párrafo tiene una cita que lleva a su fuente?»."),
    reinforce="Escribe una oración con un dato y su cita usando la nota 3 de la ficha.",
    extend="Imagina que una tercera fuente dice que la radio comenzó en 2003. Escribe cómo presentarías la diferencia en un párrafo.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso la organización y la redacción de una investigación con una lista de verificación y decido qué mejorar.",
    prior=["Organizo información en esquemas.", "Uso conectores y reemplazos.", "Cito datos de fuentes."],
    explain=[
        "Para revisar la organización de un texto, lee primero el conjunto y pregúntate: ¿hay un título?, ¿las ideas van en un orden lógico?, ¿cada párrafo trata de una sola idea? Después revisa oración por oración.",
        "Busca repeticiones que cansan, conectores que faltan o que están mal elegidos, y datos sin cita. Una lista de verificación ordena la revisión: cada criterio se marca como cumplido o no cumplido, con una frase del texto que lo muestre.",
        "Después de revisar, decide los pasos siguientes: qué reordenar, qué unir, qué citar. Si otra persona revisa tu texto, pídele comentarios sobre cada criterio y recibe sus ideas con respeto: la revisión es sobre el texto, no sobre quien lo escribió.",
    ],
    vocab=[("revisión", "lectura crítica para mejorar un texto"), ("criterio", "aspecto concreto con el que se evalúa un trabajo"), ("repetición innecesaria", "palabra o idea repetida que no aporta"), ("título", "frase que anuncia la idea principal del texto")],
    worked=[
        ("Detectar repeticiones", "Texto: «El taller abrió en 2005. El taller tenía diez socias» (ejemplo).", ["Las palabras «El taller» abren dos oraciones seguidas.", "Puedo unir o reemplazar."], "Se une: El taller abrió en 2005 y tenía diez socias"),
        ("Aplicar un criterio", "Frase sin cita: «En 2010 la feria tenía 45 puestos» (ejemplo).", ["El criterio 4 pide cita para cada dato.", "No dice de dónde sale."], "Incumple el criterio 4; hay que agregar la cita"),
    ],
    mistakes=[("Revisar solo la ortografía y no el orden ni las citas.", "El texto puede estar bien escrito pero mal organizado.", "Revisa primero orden, citas y conectores; la ortografía al final."),
              ("Reescribir todo el texto cuando solo falla un criterio.", "Se pierde tiempo y se pueden introducir nuevos errores.", "Mejora cada criterio que falla, uno a uno.")],
    T=[
        ("abc", "{F} ¿Qué problema de orden tiene el texto?", "Cuenta la situación de 1995 antes de la formación de 1990", "Comienza con un nombre propio", "Usa números en lugar de palabras", "Los hechos van del año más reciente al más antiguo."),
        ("{F} ¿Cuántas oraciones del texto comienzan con «La biblioteca»? Escribe solo el número.", "4", "La 2.ª, la 3.ª, la 5.ª y la 6.ª oración abren con esas palabras."),
        ("ab", "{F} ¿Qué criterio incumplen las repeticiones de «La biblioteca» al comienzo de cuatro oraciones?", "El 2: sin repeticiones innecesarias", "El 5: título que anuncia la idea principal", "Repetir la misma apertura cansa y es lo que mide el criterio 2."),
        ("abc", "{F} ¿Qué criterio incumple la primera oración, «Doña Lidia fue muy querida»?", "El 4: es una afirmación sin cita ni hecho comprobable", "El 1: está en orden cronológico", "El 3: tiene demasiados conectores", "Es una opinión que no tiene fuente comprobable."),
        ("=", "{F} ¿Cuántos libros más había en 1995 que cuando se formó la biblioteca?", "200 - 40", "Se restan los libros de 1990 a los de 1995 para ver el aumento.", "libros"),
        ("abc", "{F} ¿Cuál es la mejor reescritura de las oraciones sobre 1995 y 1990?", "La biblioteca se formó en 1990 con 40 libros y, cinco años después, ya tenía 200.", "La biblioteca tenía 200 libros y 40 libros; se formó en 1995 y 1990.", "Cinco años, 200 libros, 40 libros, 1990 y 1995.", "Ordena los hechos y los une con una expresión de tiempo."),
        ("ab", "{F} ¿Qué conector une bien «prestaba libros con un cuaderno» y «organizaba lecturas para adultos»?", "Además", "Porque", "La segunda oración suma otra actividad, no explica la primera."),
        ("abc", "{F} ¿Qué título anuncia mejor la idea principal del texto?", "La biblioteca de doña Lidia: formación y funcionamiento", "Un texto", "Lo que pasó", "Un título útil dice de qué trata el texto."),
        ("abc", "{F} Para cumplir el criterio 4, ¿qué debe llevar la oración sobre los 200 libros?", "Una cita con la fuente y el año, que la estudiante debe indicar", "Un adjetivo que destaque la cifra", "Nada, porque las cifras no se citan", "Las cifras también se citan, porque vienen de una fuente."),
        ("ab", "{F} Alguien dice: «Con corregir las tildes ya está revisado». ¿Es cierto?", "No: además hay que revisar orden, repeticiones, conectores y citas", "Sí: las tildes son lo único importante en una revisión", "La lista tiene cinco criterios y las tildes no son uno de ellos."),
        ("abc", "Quieres que otra persona revise tu texto. ¿Qué es mejor para recibir una crítica útil?", "Entregarle la lista de criterios y pedir comentarios sobre cada uno", "Pedir que diga solo si le gustó", "Pedir que lo reescriba entero", "Los criterios guían una crítica concreta."),
        ("{F} ¿Cuántos de los cinco criterios incumple el texto en su versión actual? Escribe solo el número.", "5", "Falla el orden, hay repeticiones, faltan conectores y citas, y no tiene título."),
        ("abc", "{F} ¿Qué paso siguiente es más útil después de esta revisión?", "Reescribir el texto en orden cronológico, con pronombres, conectores, citas y título", "Agregar más elogios sobre doña Lidia", "Dejarlo igual y entregarlo", "Se corrige cada criterio que falló, uno por uno."),
    ],
    ctx=("abc", "Escribes un informe breve para tu trabajo y se lo muestras a otra persona. ¿Cómo lo revisan de forma útil?", "Con una lista de criterios, marcando frases concretas y proponiendo cambios", "Diciendo «está bien» sin leerlo con atención", "Cambiando el texto completo sin avisar", "Una revisión con criterios y ejemplos ayuda a mejorar."),
    sc=[("En Lengua y Literatura: ¿qué es una lista de verificación?", "Un conjunto de criterios para revisar un trabajo", "Ordena la revisión en criterios claros."),
        ("En Lengua y Literatura: ¿qué haces con una oración repetitiva?", "La uno con otra o reemplazo la palabra repetida", "Unir o reemplazar la palabra evita repetirla sin necesidad."),
        ("En Lengua y Literatura: ¿qué criterio revisas primero en un texto?", "El orden lógico de las ideas", "Si las ideas no tienen orden, el texto no se entiende bien.")],
    op=("{F} Aplica la lista de verificación al texto: marca en tu cuaderno qué criterios no se cumplen y escribe una frase del texto que lo muestre. Después reescribe el texto en un párrafo de cinco a seis líneas con título, orden cronológico, conectores y dos citas inventadas del tipo (Acta de la junta de vecinos, 1990). Escribe dos pasos siguientes para mejorar el trabajo.",
        "Título: La biblioteca de doña Lidia. En 1990 reunió 40 libros donados por vecinos (Acta de la junta de vecinos, 1990). Cinco años después, ya tenía 200 (Acta de la junta de vecinos, 1995). Además, funcionaba los sábados en la sala de la escuela.",
        ["identifica criterios que no se cumplen con frases concretas", "reescribe con título, orden, conectores y citas", "propone dos pasos siguientes"],
        ["lista marcada, párrafo reescrito de cinco a seis líneas y dos pasos siguientes"],
        ["corregir solo la ortografía", "olvidar el título"],
        "Pregunta de revisión: «¿Una persona que lea mi párrafo entiende el orden de los hechos y de dónde salen?»."),
    reinforce="Revisa un mensaje que hayas escrito esta semana con los criterios 1 y 3 de la lista de verificación.",
    extend="Escribe tu propia lista de verificación de cinco criterios para revisar textos y úsala con un trabajo tuyo.",
)
