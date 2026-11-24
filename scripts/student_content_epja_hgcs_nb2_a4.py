"""Historia, Geografía y Ciencias Sociales EPJA Básica N2, módulo 1 (parte 4): OAD-04, relacionar hitos de una vida de ejemplo con la historia de Chile y el mundo, cómo se construye el conocimiento histórico y conversatorio. Personajes, testimonios y datos locales inventados («de ejemplo»); hitos de Chile y del mundo solo muy conocidos."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Las personas, los testimonios y los barrios de los ejemplos son inventados: no necesitas contar datos de tu vida. "
             "Los hitos de Chile y del mundo son hechos muy conocidos; si quieres profundizar, un docente o un libro de historia puede ayudarte. "
             "El conversatorio de la clase se practica por escrito con guiones de ejemplo; si lo haces en grupo, cada persona participa solo hasta donde se sienta cómoda, con respeto por todas las opiniones y sin comentar a personas concretas. "
             "Si algo cuesta leer, pide apoyo.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NB2-OAD-04"

# ======================================================= clase 1
F1 = ("Ficha 1 (personajes inventados de un taller de memoria). Marta nació en 1958, Luis en 1985 y Ana en 2000. "
      "Hitos conocidos: 1990, comienzan los gobiernos democráticos en Chile; 2010, ocurre un gran terremoto en Chile; 2020, comienza la pandemia mundial de COVID-19. "
      "Hito personal de ejemplo de cada persona: Marta empezó a trabajar en 1978, Luis terminó su enseñanza media en 2003 y Ana se matriculó en un curso en 2019.")
build(
    O, 1, F1,
    use="Hoy parto de lo que ya sé: veo que los hechos de una vida y los hechos de un país ocurren al mismo tiempo, con personajes de ejemplo.",
    prior=["Calculo edades restando años.", "Sé qué es un hito.", "Conozco algunos hitos de Chile y del mundo."],
    explain=[
        "Cada persona vive hechos propios: empezar a trabajar, terminar un estudio, mudarse. Se llaman hitos personales. Al mismo tiempo ocurren hitos de Chile y del mundo que afectan a todos. Relacionarlos permite ver nuestra vida dentro de una historia más grande.",
        "Un hito histórico no lo vive igual cada persona: depende de la edad que tenía, del lugar donde estaba y de lo que hacía. Un mismo hecho, como un terremoto, lo recuerda distinto una persona de 52 años y una de 10. Por eso los testimonios de varias personas son valiosos.",
        "Para relacionar, anota el año del hito personal, busca qué ocurrió ese año o esa década en Chile y el mundo, y calcula la edad restando el año de nacimiento. En esta clase trabajamos con personajes inventados; tú no tienes que contar nada de tu vida.",
    ],
    vocab=[("hito personal", "hecho importante en la vida de una persona"), ("hito histórico", "hecho importante para un país o el mundo"), ("testimonio", "relato de alguien sobre lo que vivió"), ("memoria", "recuerdo de lo vivido"), ("generación", "grupo de personas que nacieron en años parecidos")],
    worked=[
        ("Calcular la edad", "{F} ¿Qué edad tenía Marta en 1990?", ["Resto el año de nacimiento: 1990 menos 1958.", "Resultado: 32."], "32 años"),
        ("Un hito, varias miradas", "{F} Ana y Marta vivieron la pandemia de 2020. ¿Por qué la recuerdan distinto?", ["Sus edades eran distintas: 20 y 62.", "Además, cada persona vive un hecho según su trabajo, su familia y el lugar donde está."], "Porque la edad y la situación de cada persona cambian cómo vive un mismo hecho"),
    ],
    mistakes=[("Creer que todas las personas viven un hito histórico de la misma manera.", "Cada persona lo vive según su edad y su situación.", "Pide testimonios de varias personas y compara."),
              ("Calcular la edad sumando los años.", "La edad es la diferencia entre el año del hecho y el de nacimiento.", "Resta siempre el año de nacimiento.")],
    T=[
        ("abc", "{F} ¿En qué año nació Luis?", "1985", "2003", "1958", "La ficha da 1985 como su año de nacimiento."),
        ("ab", "En HGCS: ¿qué es un hito personal?", "Un hecho importante en la vida de una persona", "Un hecho importante para todo el mundo", "El hito personal marca un cambio en la vida de alguien."),
        ("{F} ¿Qué hito de Chile ocurrió en 2010?", "un gran terremoto", "La ficha lo ubica en ese año."),
        ("=", "{F} ¿Qué edad tenía Marta cuando empezó a trabajar en 1978?", "1978-1958", "Se resta el año de nacimiento del año del hito personal.", " años"),
        ("=", "{F} ¿Qué edad tenía Luis en 2010, cuando ocurrió el terremoto?", "2010-1985", "La edad se obtiene restando el año de nacimiento.", " años"),
        ("abc", "{F} ¿Cuál hito personal de la ficha ocurrió en 2019?", "Ana se matriculó en un curso", "Luis terminó su enseñanza media", "Marta empezó a trabajar", "La ficha ubica la matrícula de Ana en 2019."),
        ("ab", "{F} Entre Marta y Luis, ¿quién era más joven en 1990, cuando comenzaron los gobiernos democráticos?", "Luis", "Marta", "Luis tenía 5 años y Marta 32; Ana todavía no había nacido."),
        ("=", "{F} ¿Cuántos años tenía Ana cuando comenzó la pandemia de 2020?", "2020-2000", "Se resta el año de nacimiento de 2020.", " años"),
        ("abc", "{F} ¿En qué año ocurrió el hito personal de Luis, terminar su enseñanza media?", "2003", "1985", "2010", "La ficha da 2003 para ese hito."),
        ("abc", "{F} ¿Por qué el terremoto de 2010 pudo ser recordado distinto por Marta y por Luis?", "Porque tenían edades y situaciones distintas", "Porque el terremoto fue distinto para cada uno", "Porque Marta no vivía en Chile", "Una persona de 52 años y una de 25 viven un hecho con responsabilidades y recuerdos distintos."),
        ("ab", "Alguien dice: «Si Marta vivió 1990, entonces todos vivimos 1990 igual». ¿Qué falla?", "Cada persona lo vive según su edad y situación", "Nada", "No hay una única forma de vivir un hito histórico."),
        ("abc", "{F} ¿Qué generación tiene personas que no habían nacido en 1990?", "Ana, nacida en 2000", "Marta", "Luis", "Solo Ana nació después de 1990."),
        ("abc", "{F} Para entender un hito, ¿qué conviene reunir?", "Testimonios de varias personas y otras fuentes", "Solo un testimonio", "Solo una opinión", "Varias miradas dan una imagen más completa."),
    ],
    ctx=("abc", "En una sede vecinal se arma un mural con una línea de tiempo llamada «Nuestro barrio y Chile». Pegan un hito del barrio de ejemplo: «1995, se abre la plaza». ¿Qué hito histórico del mismo mural conviene poner al lado para dar contexto?", "Los gobiernos democráticos desde 1990", "La fundación de Santiago en 1541", "La Primera Junta de 1810", "Está en la misma década, cinco años antes."),
    sc=[("En el trabajo histórico: ¿qué es un testimonio?", "El relato de alguien sobre lo que vivió", "Es una fuente oral valiosa porque cuenta lo que vivió una persona."),
        ("¿Cómo calculo la edad en un año del pasado?", "Resto el año de nacimiento del año del hecho", "La resta da los años cumplidos o por cumplir."),
        ("¿Por qué conviene escuchar a varias personas?", "Porque cada una vivió el hecho desde su situación", "Así se obtiene una mirada más completa.")],
    op=("Personaje de ejemplo: Rosa, nacida en 1970. Hitos personales inventados: 1988 termina un curso técnico, 1995 abre un pequeño negocio, 2015 se cambia de comuna. "
        "Hitos de Chile y del mundo: 1990 comienzan los gobiernos democráticos, 2010 terremoto, 2020 pandemia. Arma una tabla con año, hito personal, hito de Chile o del mundo de la misma década y edad de Rosa.",
        "1988: 18 años, hito de Chile cercano: 1990. 1995: 25 años, década de 1990 (gobiernos democráticos). 2015: 45 años, cinco años después del terremoto de 2010.",
        ["calcula bien las edades", "relaciona con un hito cercano", "no afirma causas sin fuente"],
        ["una tabla de tres filas"], ["restar mal", "afirmar que un hito causó un hecho personal"],
        "Pregunta: «¿Qué edad tenía en ese año y qué pasaba en Chile?»."),
    reinforce="Elige un personaje de ejemplo y escribe dos hechos de su vida con la edad que tenía.",
    extend="Explica por qué dos personas de edades distintas recuerdan un mismo hecho de forma distinta.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Pregunta de investigación: «¿Cómo cambió la vida en la población Los Alerces cuando llegó el agua potable?». "
      "Fuentes: A) Un acta de la junta de vecinos de 1985 (de ejemplo) que anota la instalación de llaves en las casas. "
      "B) El testimonio de una vecina: «Antes íbamos con baldes a una llave común; después se acabaron las filas». "
      "C) Un artículo de 2018 de un historiador local que resume el cambio. Con las tres fuentes se escribe una explicación: «El agua potable facilitó las tareas del hogar».")
build(
    O, 2, F2,
    use="Hoy aprendo las palabras clave para entender cómo se construye el conocimiento histórico: pregunta, fuente, testimonio, evidencia e interpretación.",
    prior=["Sé qué es una fuente.", "Distingo primaria de secundaria.", "Separo hecho de opinión."],
    explain=[
        "El conocimiento histórico no aparece solo: se construye. Se parte de una pregunta, como «¿cómo cambió la vida cuando llegó el agua potable?». Luego se buscan fuentes, se leen con cuidado, se comparan y, con la evidencia que dan, se escribe una explicación.",
        "La evidencia es el dato de una fuente que apoya una afirmación. La interpretación es la explicación que se arma con esas evidencias; por eso puede cambiar cuando aparecen fuentes nuevas. Un testimonio, es decir el relato de una persona, es una fuente valiosa, pero depende de su memoria y de su punto de vista.",
        "Una buena explicación dice qué fuentes usó y qué no se sabe. Eso la hace confiable. Y permite que otras personas la revisen, la discutan y la mejoren, que es parte del trabajo de la historia.",
    ],
    vocab=[("pregunta de investigación", "lo que quiero saber, escrita con claridad"), ("evidencia", "dato de una fuente que apoya una afirmación"), ("interpretación", "explicación armada con evidencias"), ("testimonio", "relato de una persona sobre lo vivido"), ("punto de vista", "lugar desde el cual una persona mira lo que ocurrió")],
    worked=[
        ("Evidencia para una afirmación", "{F} ¿Qué evidencia apoya «el agua potable facilitó las tareas»?", ["La fuente B dice que se acabaron las filas y los baldes.", "La fuente A confirma la instalación de llaves en 1985."], "Fuentes A y B"),
        ("Límite de un testimonio", "{F} ¿Qué no sabemos si solo usamos el testimonio de la vecina?", ["Es una sola persona.", "No dice cuántas familias tenían agua."], "No sabemos cuántas familias se beneficiaron ni qué opinaban otras personas"),
    ],
    mistakes=[("Creer que un testimonio es «solo un recuerdo» y no sirve.", "Es una fuente valiosa que hay que contrastar.", "Compárala con documentos y otros testimonios."),
              ("Pensar que una interpretación es una opinión sin apoyo.", "Una interpretación se apoya en evidencia.", "Cita las fuentes que respaldan cada afirmación.")],
    T=[
        ("abc", "{F} ¿Cuál es la pregunta de investigación de la ficha?", "Cómo cambió la vida cuando llegó el agua potable", "Quién fundó la junta", "Cuándo cierran las llaves", "La ficha la anuncia al comienzo."),
        ("ab", "En HGCS: ¿qué es una evidencia?", "Un dato de una fuente que apoya una afirmación", "Una opinión sin apoyo", "La evidencia respalda lo que se afirma."),
        ("{F} ¿En qué año es el acta de la junta de vecinos?", "1985", "El acta lleva la fecha 1985 en su texto, según la ficha."),
        ("abc", "{F} ¿Qué tipo de fuente es la B?", "Un testimonio oral", "Un objeto antiguo", "Un plano", "Es el relato de una vecina."),
        ("ab", "{F} ¿Qué fuente es secundaria?", "El artículo de 2018", "El acta de 1985", "El artículo resume el cambio muchos años después."),
        ("=", "{F} ¿Cuántos años pasaron entre el acta (1985) y el artículo (2018)?", "2018-1985", "Se resta el año más antiguo del más reciente.", " años"),
        ("abc", "{F} ¿Qué evidencia de la fuente B muestra un cambio?", "Antes iban con baldes a una llave común y después se acabaron las filas", "Que el artículo es de 2018", "Que el acta existe", "La vecina describe el antes y el después."),
        ("ab", "{F} La afirmación «El agua potable facilitó las tareas del hogar» es:", "Una interpretación apoyada en evidencia", "Un dato inventado", "Se arma con evidencias de las fuentes."),
        ("abc", "{F} ¿Qué conviene hacer para confirmar el testimonio de la vecina?", "Compararlo con el acta y otros testimonios", "Dejarlo igual", "Borrar el acta", "Contrastar fuentes distintas aumenta la confianza en el dato."),
        ("abc", "Un estudiante dice: «Con un solo testimonio basta para explicar todo el barrio». ¿Qué falla?", "Una persona no representa a todo el barrio", "Los testimonios no existen", "El testimonio es una fuente escrita", "Cada persona vive el hecho desde su situación."),
        ("ab", "¿Por qué una buena explicación debe decir qué fuentes usó?", "Para que otras personas puedan revisarla", "Para hacerla más larga", "Citar fuentes permite comprobar y discutir la explicación."),
        ("abc", "{F} Aparece una nueva acta que dice que en 1985 solo la mitad de las casas tenía llaves. ¿Qué pasaría con la interpretación?", "Podría ajustarse, porque hay evidencia nueva", "Seguiría igual sin pensar", "Se borraría la historia", "Las interpretaciones cambian con nuevas fuentes."),
        ("abc", "{F} ¿Cuál es la mejor forma de cerrar la explicación?", "El agua potable facilitó las tareas, según el acta y el testimonio; falta saber cuántas familias la tuvieron", "El agua potable arregló todo", "No sabemos nada", "Incluye evidencia y reconoce un límite."),
    ],
    ctx=("abc", "En una radio comunitaria se prepara un programa sobre cuándo llegó el alumbrado al barrio. Tienen un recorte de 1972 (de ejemplo) y el relato de un vecino. ¿Cuál es la mejor manera de armar la explicación?", "Usar ambos y decir qué dice cada uno y qué falta", "Usar solo el recorte", "Usar solo lo que recuerda alguien del equipo", "Usar varias fuentes y mostrar sus límites mejora la explicación."),
    sc=[("¿Qué es una interpretación histórica?", "Una explicación armada con evidencias", "Puede cambiar cuando aparecen nuevas fuentes con otra evidencia."),
        ("En HGCS: ¿qué es un testimonio?", "El relato de una persona sobre lo que vivió", "Es una fuente oral, es decir, un relato hablado de lo vivido."),
        ("¿Por qué hay que contrastar un testimonio?", "Porque depende de la memoria y del punto de vista de quien cuenta", "Compararlo con otras fuentes ayuda a comprobar sus datos.")],
    op=("Pregunta de ejemplo: «¿Cómo cambió la vida en un barrio cuando se abrió un consultorio?». Fuentes de ejemplo: a) acta de 1998: se abre el consultorio; b) relato de una vecina: «Antes viajábamos una hora para un control»; c) artículo de 2015 que resume los cambios. "
        "Escribe una explicación de dos frases con evidencias y una frase de lo que no sabes.",
        "Con el consultorio, la gente dejó de viajar una hora para sus controles (a y b). El artículo de 2015 resume ese cambio (c). No sabemos cuántas personas se atienden hoy.",
        ["usa evidencias de al menos dos fuentes", "distingue evidencia de interpretación", "señala un límite"],
        ["tres frases escritas con las fuentes citadas"], ["no citar fuentes", "afirmar más de lo que dicen"],
        "Pregunta: «¿Qué fuente apoya cada frase?»."),
    reinforce="Escribe una pregunta sobre tu barrio y di dos fuentes que ayudarían a responderla.",
    extend="Explica la diferencia entre una evidencia y una interpretación con un ejemplo propio.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Personaje inventado: Carmen, nacida en 1966. Hecho personal de ejemplo: en 1990 termina su educación básica en una escuela nocturna. "
      "Hitos históricos de ese año y de esa década (conocidos): en 1990 comienzan los gobiernos democráticos en Chile. "
      "Dato del barrio (de ejemplo): en 1990 la junta de vecinos abre una escuela nocturna en la sede. Pregunta: «¿Qué relación puede haber entre la vida de Carmen y lo que ocurría en Chile en 1990?».")
build(
    O, 3, F3,
    use="Hoy sigo pasos para relacionar un hecho de una vida de ejemplo con la historia de Chile y del mundo, sin afirmar más de lo que dicen las fuentes.",
    prior=["Calculo edades.", "Sé qué es un hito histórico.", "Distingo coincidencia de causa."],
    explain=[
        "Relacionar un hecho personal con la historia es un trabajo de cinco pasos. Paso 1: escribe el hecho personal con su fecha. Paso 2: busca qué ocurrió en Chile y en el mundo en ese año o en esa década. Paso 3: calcula la edad de la persona. Paso 4: revisa si una fuente conecta ambos hechos. Paso 5: escribe una frase que diga qué sabes y qué no.",
        "Es importante distinguir entre coincidir y causar. Si Carmen terminó su escuela en 1990 y en 1990 comenzaron los gobiernos democráticos, solo sabemos que ocurrieron en el mismo año. Para decir que uno influyó en el otro necesitamos una fuente, como el relato de ella o un documento.",
        "También conviene ubicar el hecho en un periodo: 1990 pertenece a la República en Chile y a la Edad Contemporánea en el mundo. Así se ve que cada vida ocurre dentro de periodos más amplios.",
    ],
    vocab=[("coincidir", "ocurrir al mismo tiempo"), ("causa", "razón por la que ocurre algo"), ("conectar", "mostrar que dos hechos se relacionan"), ("década", "diez años seguidos"), ("contexto", "lo que ocurría alrededor de un hecho")],
    worked=[
        ("Los cinco pasos", "{F} Relaciona la vida de Carmen con 1990.", ["Paso 1: en 1990 termina la básica. Paso 2: en 1990 comienzan gobiernos democráticos.", "Paso 3: tenía 24 años. Paso 4: la ficha no dice que una cosa influyera en la otra. Paso 5: coinciden en el año."], "Coinciden en 1990; la ficha no prueba que una cosa influyera en la otra"),
        ("Edad en el hito", "{F} ¿Qué edad tenía Carmen en 1990?", ["Resto 1990 menos 1966.", "Resultado: 24."], "24 años"),
    ],
    mistakes=[("Afirmar que los gobiernos democráticos hicieron que Carmen terminara la escuela.", "La ficha no lo dice; solo coinciden en el año.", "Escribe «coinciden» y busca una fuente que muestre la relación."),
              ("Olvidar calcular la edad.", "La edad ayuda a imaginar la situación de la persona en ese momento.", "Resta siempre el año de nacimiento.")],
    T=[
        ("abc", "{F} ¿Qué hecho personal de Carmen se menciona?", "Terminó su educación básica en una escuela nocturna", "Se mudó a otra región", "Cambió de trabajo", "La ficha lo menciona de forma directa en su texto."),
        ("ab", "{F} ¿En qué año terminó Carmen su educación básica?", "1990", "1966", "El año del hito personal es 1990."),
        ("=", "{F} ¿Qué edad tendría Carmen en 2000?", "2000-1966", "Se resta el año de nacimiento del año que se pregunta.", " años"),
        ("abc", "{F} ¿Qué hito histórico ocurrió en 1990?", "Comenzaron los gobiernos democráticos en Chile", "Se fundó Santiago", "Se proclamó la independencia", "La ficha lo anota como hito de 1990."),
        ("ab", "{F} ¿Qué abrió la junta de vecinos en 1990 según la ficha?", "Una escuela nocturna", "Un consultorio", "El dato de barrio habla de una escuela nocturna en la sede."),
        ("En HGCS: ¿cómo se llama el hecho de ocurrir al mismo tiempo?", "coincidir", "Coincidir significa ocurrir en el mismo tiempo, sin implicar causa."),
        ("abc", "{F} Una persona dice: «Los gobiernos democráticos hicieron que Carmen terminara la escuela». ¿Qué falla?", "Coinciden en el año, pero la ficha no prueba que uno causó el otro", "Nada, está probado", "Carmen no existe", "Para hablar de causa se necesita evidencia."),
        ("abc", "{F} ¿Qué fuente podría mostrar si hubo una conexión?", "El relato de Carmen o un documento de la escuela nocturna", "Un horóscopo", "Una opinión sin autor", "Un testimonio o documento puede explicar la relación."),
        ("ab", "{F} ¿En qué periodo de Chile está 1990?", "República", "Colonia", "El siglo XX pertenece a la República."),
        ("abc", "{F} ¿En qué periodo de la humanidad está 1990?", "Edad Contemporánea", "Edad Media", "Prehistoria", "Desde fines del siglo XVIII hasta hoy corresponde a la Edad Contemporánea."),
        ("abc", "{F} ¿Cuál es la mejor frase final de los cinco pasos?", "En 1990, Carmen terminó la básica a los 24 años, el mismo año en que comenzaron los gobiernos democráticos; no sabemos si hubo conexión", "Carmen terminó la básica gracias a los gobiernos", "No pasó nada", "Dice qué sabe y qué no."),
        ("ab", "¿Por qué conviene decir «no sabemos si hubo conexión»?", "Porque declara el límite de las fuentes", "Porque es obligatorio", "Reconocer lo que no se sabe evita afirmar de más."),
        ("abc", "{F} Aparece el relato de Carmen: «Me animé porque abrieron la escuela en la sede». ¿Qué conexión muestra?", "Una relación con un hecho del barrio, no necesariamente con el hito nacional", "Una relación probada con el hito de 1990", "Ninguna", "Cita la escuela del barrio, no el hito nacional."),
    ],
    ctx=("abc", "En un taller, una persona dice: «Mi tío empezó a trabajar en una fábrica en 1985 y ese año yo nací». Si se arma una tabla con ese dato de ejemplo, ¿qué conviene hacer primero?", "Anotar el año de cada hecho y buscar hitos de ese año", "Decidir que se relacionan", "Ignorar las fechas", "El primer paso es ubicar cada hecho con su fecha."),
    sc=[("¿Qué diferencia hay entre coincidir y causar?", "Coincidir es ocurrir al mismo tiempo; causar es producir otro hecho", "Para afirmar causa se necesita evidencia."),
        ("¿Qué tengo que hacer en el paso 4?", "Revisar si una fuente conecta los dos hechos", "Evita afirmar relaciones que ninguna fuente respalda."),
        ("¿Cómo calculo la edad en un hito?", "Resto el año de nacimiento del año del hito", "Esa resta da la edad que se tenía en ese año.")],
    op=("Personaje de ejemplo: Julio, nacido en 1972. Hechos: 1994 empieza a trabajar en un taller; 2010 se muda a otra ciudad; 2020 hace un curso en línea. "
        "Aplica los cinco pasos al hecho de 2010: edad, hito de Chile del mismo año, periodo y una frase final que diga qué sabes y qué no.",
        "Edad: 38 años. Hito de 2010: terremoto en Chile. Periodo: República y Edad Contemporánea. Frase: en 2010, Julio se mudó a los 38 años, el mismo año del terremoto; no sabemos si hubo conexión.",
        ["calcula la edad", "ubica el hito del mismo año", "no afirma causa sin fuente"],
        ["cinco líneas escritas, una por paso"], ["afirmar que el terremoto causó la mudanza", "olvidar el límite"],
        "Pregunta: «¿Qué fuente me permitiría afirmar una relación?»."),
    reinforce="Con un personaje de ejemplo, calcula su edad en tres años distintos.",
    extend="Explica por qué una coincidencia de fechas puede ser un buen punto de partida para investigar.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Tema: la llegada del agua potable al sector Las Lomas. "
      "Testimonio 1 (vecina Elsa): «Las llaves llegaron en 1985; yo fui de las primeras». "
      "Testimonio 2 (vecino Raúl): «Fue en 1987; me acuerdo porque ese año nació mi sobrino». "
      "Acta de la junta de vecinos de 1986: «Se inaugura la instalación de llaves en 40 casas». "
      "Pregunta: «¿En qué año llegó el agua potable?».")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo contrastar testimonios y documentos para construir una explicación, y qué nos permite conocer cada fuente.",
    prior=["Sé qué es una evidencia y una interpretación.", "Distingo testimonio de documento.", "Calculo diferencias de años."],
    explain=[
        "A veces las fuentes no coinciden. En la ficha, la vecina dice 1985, el vecino dice 1987 y un acta dice que en 1986 se inauguró la instalación de llaves. ¿Quién tiene razón? No se trata de elegir al que más nos gusta, sino de contrastar: compararlas y ver qué se puede afirmar con seguridad.",
        "Un testimonio puede equivocarse en una fecha por el paso del tiempo, pero sigue siendo valioso para saber cómo se vivió. Un acta es un documento de la época y suele ser más firme para fechas. Si dos fuentes difieren, se busca una tercera y se explica la diferencia con claridad.",
        "Una buena práctica es escribir: «Según el acta de 1986, la instalación se inauguró en 1986; los testimonios dicen 1985 y 1987, así que el proceso pudo extenderse entre esos años». Así se reconoce lo que no se sabe y se evita dar por cierta una sola versión.",
    ],
    vocab=[("contrastar", "comparar fuentes para ver en qué coinciden y en qué difieren"), ("versión", "forma en que alguien cuenta un hecho"), ("firme", "que tiene buen respaldo"), ("proceso", "cambios que ocurren en un tiempo"), ("explicar la diferencia", "decir por qué dos fuentes no coinciden")],
    worked=[
        ("Contrastar tres fuentes", "{F} ¿Qué se puede afirmar con seguridad?", ["El acta de 1986 dice que se inauguró la instalación en 40 casas.", "Los testimonios dicen 1985 y 1987."], "Que hubo instalación de llaves hacia 1986, en 40 casas; el año exacto de llegada varía"),
        ("Explicar la diferencia", "{F} ¿Por qué podrían diferir Elsa y Raúl?", ["Pueden recordar momentos distintos del proceso.", "El tiempo puede confundir un año."], "Porque el proceso pudo extenderse y la memoria puede variar"),
    ],
    mistakes=[("Elegir la fuente que coincide con lo que ya pensaba.", "Se escoge por gusto y no por evidencia.", "Aplica el mismo criterio a todas las fuentes."),
              ("Descartar un testimonio porque el año no coincide.", "Aún puede entregar datos valiosos sobre cómo se vivió.", "Úsalo para esa información y contrasta las fechas con documentos.")],
    T=[
        ("abc", "{F} ¿Qué año dice Elsa?", "1985", "1986", "1987", "Elsa dice que las llaves llegaron en 1985."),
        ("ab", "{F} ¿Qué año dice Raúl?", "1987", "1985", "Raúl menciona 1987 y el nacimiento de su sobrino."),
        ("{F} ¿Cuántas casas se mencionan en el acta?", "40", "El acta anota la instalación de llaves en 40 casas."),
        ("abc", "{F} ¿Qué tipo de fuente es el acta?", "Un documento de la época", "Un testimonio oral", "Un objeto", "Es un documento escrito de 1986."),
        ("ab", "{F} Si solo se usara el testimonio de Elsa, ¿qué año se afirmaría?", "1985", "1986", "Elsa dice 1985 y esa es su versión de los hechos."),
        ("=", "{F} ¿Cuántos años separan el testimonio más temprano (1985) del más tardío (1987)?", "1987-1985", "Se resta el año menor del mayor.", " años"),
        ("abc", "{F} ¿Qué conviene hacer cuando las fuentes no coinciden?", "Contrastarlas y buscar otra fuente", "Elegir la que gusta", "Borrar la que difiere", "Contrastar y buscar más evidencia es el método."),
        ("abc", "{F} ¿Cuál afirmación es la más segura?", "Hubo instalación de llaves en 40 casas, según un acta de 1986", "Todas las casas tuvieron llaves en 1985", "Raúl se equivocó", "Está respaldada por un documento de la época, no por memoria."),
        ("ab", "{F} ¿Por qué el acta suele ser más firme para fechas?", "Porque se escribió en la época", "Porque es más larga", "Un documento de la época reduce los errores de memoria."),
        ("abc", "Un estudiante dice: «Raúl no sirve porque dice 1987». ¿Qué respuesta es mejor?", "Su testimonio puede servir para saber cómo se vivió, aunque la fecha se contraste", "Tiene razón", "El acta no sirve", "Los testimonios aportan experiencia aun si hay que revisar fechas."),
        ("ab", "{F} ¿Qué frase reconoce lo que no se sabe?", "El año exacto de llegada del agua varía según las fuentes", "El agua llegó en 1985 sin dudas", "Reconocer la diferencia evita dar una sola versión por cierta."),
        ("abc", "{F} ¿Qué fuente nueva podría ayudar a decidir?", "Un registro de la empresa de agua de la época", "El recuerdo de alguien que no vivió en el sector", "Una opinión sin fecha", "Un registro de la época es una buena tercera fuente."),
        ("abc", "{F} ¿Cuál es la mejor conclusión provisional?", "El proceso de instalación ocurrió entre 1985 y 1987, con una inauguración en 1986 según el acta", "Nada se puede decir", "Fue en 1990", "Resume lo que respaldan las fuentes."),
    ],
    ctx=("abc", "Dos vecinas de ejemplo discrepan sobre cuándo se inauguró una plaza: una dice 2004 y otra 2006. Hay un afiche de inauguración de 2005 en la sede. ¿Qué hacen?", "Usan el afiche como tercera fuente y explican por qué difieren", "Eligen a la que conocen más", "Descartan el afiche", "Un documento de la época ayuda a contrastar."),
    sc=[("En HGCS: ¿qué significa contrastar fuentes?", "Compararlas para ver en qué coinciden y en qué difieren", "Así se decide qué se puede afirmar."),
        ("¿Por qué puede fallar un testimonio en una fecha?", "Porque la memoria cambia con el tiempo", "Eso no le quita valor a lo que cuenta."),
        ("¿Qué escribo cuando no se puede precisar un dato?", "Que el dato varía según las fuentes", "Declarar el límite es parte del método.")],
    op=("Fuentes de ejemplo sobre la apertura de una biblioteca barrial: testimonio A: «Abrió en 2001»; testimonio B: «Abrió en 2003»; acta de 2002: «Se inaugura la biblioteca con 300 libros». "
        "Contrasta las fuentes, escribe qué afirmas con seguridad y qué te falta saber.",
        "Con seguridad: según el acta, se inauguró en 2002 con 300 libros. Los testimonios dicen 2001 y 2003, por lo que el proceso pudo extenderse. Falta saber cuándo abrió al público.",
        ["compara las tres fuentes", "afirma lo que el acta respalda", "señala un límite"],
        ["una tabla con tres fuentes y dos frases"], ["elegir sin criterio", "descartar un testimonio"],
        "Pregunta: «¿Qué fuente es de la época y qué fuente depende de la memoria?»."),
    reinforce="Con dos fuentes de ejemplo que no coinciden, escribe una frase que explique la diferencia.",
    extend="Explica por qué contrastar fuentes hace más confiable una explicación histórica.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (guion de ejemplo de un conversatorio en un centro comunitario, personajes inventados). Tema: «¿Qué nos permite conocer la historia del barrio?». Reglas acordadas: hablar por turnos, usar ejemplos o fuentes, escuchar sin interrumpir y no hablar de personas concretas. "
      "Intervención 1 (Lucía): «Nos permite saber cuándo llegó la luz, porque tenemos un acta de 1975». "
      "Intervención 2 (Pedro): «Eso no sirve para nada». "
      "Intervención 3 (Marta): «Me parece que también nos permite entender por qué la sede está donde está, según el relato de don Hugo». "
      "Intervención 4 (Iván): «Mi vecino siempre se equivoca con las fechas».")
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido en un conversatorio de ejemplo: reconozco buenas intervenciones, uso evidencia y respeto turnos y personas.",
    prior=["Sé contrastar fuentes.", "Relaciono hechos de una vida con hitos históricos.", "Reconozco una opinión y un hecho."],
    explain=[
        "Un conversatorio es una conversación ordenada sobre un tema, donde cada persona escucha y aporta. No es una discusión para ganar, sino una forma de comprender mejor entre varias personas. Sirve para compartir lo que sabemos y aprender de otros.",
        "Una buena intervención tiene tres rasgos. Responde al tema, usa un ejemplo o una fuente y respeta a las demás personas. Algunas reglas útiles: pedir la palabra, hablar por turnos, no interrumpir, no hablar mal de personas concretas y aceptar que otros piensen distinto.",
        "En un conversatorio de historia no tienes que contar tu vida personal. Puedes hablar de casos, de fuentes o de lo que otros han relatado. Al cerrar, alguien resume lo conversado: qué ideas aparecieron, qué se acordó y qué falta investigar.",
    ],
    vocab=[("conversatorio", "conversación ordenada sobre un tema, con turnos y respeto"), ("intervención", "lo que dice una persona cuando le toca hablar"), ("argumento", "razón con que se apoya una idea"), ("moderar", "ordenar los turnos de una conversación"), ("síntesis", "resumen de lo más importante")],
    worked=[
        ("Reconocer una buena intervención", "{F} ¿Cuál es una buena intervención?", ["La de Lucía responde al tema y usa un acta como evidencia.", "La de Marta usa un relato y relaciona con el tema."], "Las de Lucía y Marta"),
        ("Qué corregir", "{F} ¿Qué falla en la intervención de Pedro?", ["Dice «no sirve para nada» sin dar razones.", "No respeta lo dicho por otra persona."], "No da razones y descalifica sin argumentos"),
    ],
    mistakes=[("Creer que un conversatorio es una competencia para ganar.", "Se trata de comprender entre varias personas.", "Escucha, aporta y ofrece razones."),
              ("Hablar de personas concretas con críticas personales.", "Se daña la confianza del grupo.", "Habla de las ideas y las fuentes, no de las personas.")],
    T=[
        ("abc", "{F} ¿Cuál es el tema del conversatorio?", "Qué nos permite conocer la historia del barrio", "Cuánto cuesta una micro", "Quién ganó un partido", "La ficha lo anuncia al comienzo."),
        ("ab", "En HGCS: ¿qué es un conversatorio?", "Una conversación ordenada sobre un tema", "Una pelea para ganar", "Es un espacio de turnos, respeto y aprendizaje."),
        ("{F} ¿Qué fuente usa Lucía?", "un acta de 1975", "Lucía menciona un acta de 1975."),
        ("abc", "{F} ¿Qué regla se menciona en la ficha?", "Hablar por turnos", "Hablar todos a la vez", "No usar ejemplos", "Es una de las reglas acordadas."),
        ("ab", "{F} ¿Qué usa Marta para apoyar su idea?", "El relato de don Hugo", "Un cuadro de fútbol", "Marta cita un relato como fuente."),
        ("{F} ¿Qué intervención descalifica lo dicho sin dar ninguna razón? Escribe el nombre.", "Pedro", "Pedro dice «eso no sirve para nada» sin explicar."),
        ("abc", "{F} ¿Qué falla en la intervención de Iván?", "Habla mal de una persona concreta y no aporta evidencia", "Usa un acta", "Responde al tema con una fuente", "Va contra la regla de no hablar de personas concretas."),
        ("abc", "{F} ¿Cómo podría Pedro mejorar su intervención?", "Explicando por qué cree que no sirve y qué propone", "Gritando más fuerte", "Quedándose callado siempre", "Dar razones mejora la conversación y permite que otros respondan."),
        ("ab", "{F} Un buen resumen del conversatorio incluye:", "Las ideas que aparecieron y lo que falta investigar", "Solo los errores de alguien", "La síntesis recoge lo central de lo conversado."),
        ("abc", "Una persona prefiere no contar episodios de su vida. ¿Qué respuesta es correcta?", "No está obligada: puede aportar con casos o fuentes", "Debe contarlos", "Debe irse", "La participación es voluntaria y nadie debe contar lo que no desea."),
        ("abc", "{F} ¿Qué pregunta nueva ayuda a seguir el conversatorio?", "¿Qué otras fuentes podrían confirmar lo que dice el acta?", "¿Quién habló peor?", "¿Quién es más importante?", "Orienta a buscar evidencia que confirme o corrija lo dicho."),
        ("ab", "¿Qué hace una persona moderadora?", "Ordena los turnos y cuida el respeto", "Decide quién tiene razón", "Moderar es cuidar que todos puedan participar."),
        ("abc", "{F} ¿Cuál de estas cierra mejor el conversatorio?", "Conocimos fuentes (acta, relatos) sobre la llegada de la luz y la sede; falta buscar más testimonios", "Ganó Lucía", "Perdió Pedro", "Es una síntesis que no califica a las personas."),
    ],
    ctx=("abc", "En un centro de adultos se conversa sobre «Cómo cambió el comercio del barrio». Un participante se burla de la opinión de otra persona. ¿Qué conviene que haga quien modera?", "Recordar la regla de respeto y volver a las ideas y las fuentes", "Dejar que siga la burla", "Cerrar el conversatorio sin explicar", "Las reglas acordadas protegen a todas las personas y permiten seguir conversando."),
    sc=[("¿Qué tres rasgos tiene una buena intervención?", "Responde al tema, usa ejemplo o fuente y respeta a los demás", "Son criterios que permiten evaluar cualquier intervención."),
        ("¿Es obligatorio contar mi vida personal?", "No, puedo participar con casos o fuentes", "La participación es voluntaria y puede hacerse con casos o fuentes."),
        ("En un conversatorio: ¿qué es una síntesis?", "Un resumen de lo central de lo conversado", "Se hace al cierre para recoger las ideas centrales conversadas.")],
    op=("Conversatorio de ejemplo (por escrito). Tema: «¿Qué nos permite conocer la historia de un barrio?». Preparar una intervención de tres frases con: una idea, un ejemplo o fuente de ejemplo (por ejemplo, un acta de 1990 que anota la apertura de una plaza) y una pregunta para otra persona. "
        "Después evalúa tu intervención con las tres reglas.",
        "Idea: nos permite saber cómo cambió la vida. Ejemplo: un acta de 1990 anota la apertura de una plaza. Pregunta: ¿qué otras fuentes podrían mostrar cómo se usaba la plaza?",
        ["responde al tema", "usa un ejemplo o fuente", "incluye una pregunta respetuosa"],
        ["tres frases escritas y una autoevaluación"], ["hablar de personas concretas", "no usar ejemplo"],
        "Pregunta: «¿Lo que digo responde al tema y respeta a las personas?»."),
    reinforce="Escribe una idea y un ejemplo para un conversatorio sobre tu comunidad.",
    extend="Explica por qué escuchar es tan importante como hablar en un conversatorio.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Resumen de un taller: Se trabajó con tres personajes inventados: Marta (1958), Luis (1985) y Ana (2000). "
      "Se relacionaron sus hitos personales con hitos de Chile y del mundo: 1990, comienzo de los gobiernos democráticos en Chile; 2010, un gran terremoto en Chile; 2020, comienzo de una pandemia mundial. "
      "Se contrastaron testimonios y actas sobre la llegada del agua potable a un barrio. Se acordó que la historia nos permite conocer el pasado, comprender el presente y valorar los cambios y las continuidades.")
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: hago una síntesis de cómo se construye el conocimiento histórico y qué nos permite comprender, y decido qué quiero seguir practicando.",
    prior=["Relaciono hechos de una vida con hitos de Chile y del mundo.", "Contrasto fuentes.", "Participo en un conversatorio con respeto."],
    explain=[
        "Revisar lo logrado es mirar lo que ya sabes hacer. Ahora puedes ubicar hechos en el tiempo, calcular edades, relacionar una vida con hitos de Chile y del mundo, y contrastar testimonios y documentos para construir explicaciones.",
        "El conocimiento histórico se construye con preguntas, fuentes, contraste y explicación. Nos permite conocer el pasado, comprender cómo se llegó al presente y valorar lo que cambió y lo que sigue igual. Sirve para entender nuestro barrio, nuestro país y el mundo, y para conversar con mejores argumentos.",
        "Para cerrar, hazte tres preguntas: ¿qué aprendí? ¿qué puedo explicar con mis palabras? ¿qué me gustaría seguir practicando? Responderlas orienta tu siguiente paso.",
    ],
    vocab=[("conocimiento histórico", "explicación del pasado construida con preguntas y fuentes"), ("cambio y continuidad", "lo que cambió y lo que siguió igual"), ("síntesis", "resumen de lo más importante"), ("autoevaluación", "revisión del propio trabajo con criterios"), ("próximo paso", "lo que decido practicar después")],
    worked=[
        ("Armar la síntesis", "{F} Resume cómo se construye el conocimiento histórico.", ["Se parte de una pregunta y se buscan fuentes.", "Se contrastan las fuentes y se escribe una explicación con evidencias."], "Pregunta, fuentes, contraste y explicación con evidencia"),
        ("Calcular una edad para el cierre", "{F} ¿Qué edad tenía Luis en 2020?", ["Resto 2020 menos 1985.", "Resultado: 35."], "35 años"),
    ],
    mistakes=[("Creer que aprender historia es solo memorizar fechas.", "Importa también preguntar, usar fuentes y explicar.", "Practica con preguntas y evidencia."),
              ("Dejar la autoevaluación sin decisión.", "No sirve si no se decide qué hacer después.", "Termina siempre con un próximo paso.")],
    T=[
        ("abc", "{F} ¿Qué se contrastó en el taller?", "Testimonios y actas sobre el agua potable", "Precios de pan", "Resultados de fútbol", "La ficha lo menciona de forma directa en su resumen."),
        ("ab", "{F} ¿Qué hito ocurrió en 2020?", "El comienzo de una pandemia mundial", "El comienzo de los gobiernos democráticos", "La ficha ubica la pandemia en 2020."),
        ("=", "{F} ¿Qué edad tenía Ana en 2020?", "2020-2000", "Se resta el año de nacimiento del año del hito.", " años"),
        ("abc", "{F} ¿Qué edad tenía Marta en 1990?", "32", "40", "20", "La resta 1990 menos 1958 da 32 años."),
        ("ab", "{F} Entre Marta y Luis, ¿quién nació antes?", "Marta", "Luis", "Marta nació en 1958 y Luis en 1985."),
        ("En HGCS: ¿qué nombre recibe el resumen de lo central?", "síntesis", "Una síntesis recoge las ideas principales."),
        ("abc", "{F} ¿Qué nos permite la historia según el resumen del taller?", "Conocer el pasado, comprender el presente y valorar cambios y continuidades", "Predecir el futuro con exactitud", "Elegir quién tiene razón", "El resumen del taller lo señala de forma explícita."),
        ("abc", "{F} ¿Qué pasos sigue la construcción del conocimiento histórico?", "Pregunta, fuentes, contraste y explicación", "Memorizar, repetir y olvidar", "Opinar sin fuentes", "Es el método de la clase 2."),
        ("ab", "¿Qué hago al autoevaluarme?", "Reviso mi trabajo con criterios y decido qué practicar", "Me comparo con otras personas", "La autoevaluación ayuda a mejorar sin compararse."),
        ("abc", "{F} Un hito personal de Luis fue en 2003. ¿Cuántos años pasaron hasta la pandemia de 2020?", "17", "27", "7", "La resta 2020 menos 2003 da 17 años."),
        ("abc", "Una persona dice: «Aprender historia es solo recordar fechas». ¿Qué respuesta es mejor?", "También es preguntar, usar fuentes y explicar con evidencia", "Tiene razón", "No hay fechas en historia", "El método incluye pregunta, fuentes y explicación."),
        ("ab", "{F} ¿Qué conviene incluir en una síntesis final?", "Lo aprendido, lo que se puede explicar y lo que falta practicar", "Solo los errores", "La síntesis considera logros y próximos pasos."),
        ("abc", "{F} ¿Cuál es una buena decisión de próximo paso?", "Practicar el cálculo de edades con nuevos ejemplos si me cuesta", "No volver a estudiar", "Cambiar de tema sin revisar", "Se relaciona con una dificultad concreta."),
    ],
    ctx=("abc", "Una dirigente prepara una síntesis para el cierre de un taller sobre la historia del barrio. Tiene tres ideas: un resumen de las fuentes usadas, un cálculo de cuántos años pasaron entre la apertura de la sede (1980, de ejemplo) y hoy, y la lista de lo que falta investigar. ¿Cuál es el mejor orden?", "Fuentes usadas, cálculo del tiempo y lo que falta investigar", "Lo que falta, fuentes y cálculo", "Solo el cálculo", "Va de lo que se hizo a lo que falta."),
    sc=[("¿Qué permite el conocimiento histórico?", "Conocer el pasado y comprender el presente", "Ayuda a ver cambios y continuidades."),
        ("¿Qué incluye una autoevaluación?", "Qué aprendí, qué puedo explicar y qué quiero practicar", "Una autoevaluación cierra con un próximo paso concreto."),
        ("¿Cuáles son los pasos para construir conocimiento histórico?", "Pregunta, fuentes, contraste y explicación", "Es el método estudiado en este módulo para construir conocimiento.")],
    op=("Haz tu síntesis final con personajes de ejemplo. Escribe: (1) una pregunta histórica sobre un barrio ficticio; (2) dos fuentes de ejemplo que usarías; (3) un hito de Chile o del mundo al que podrías relacionarla; (4) una frase sobre lo que la historia nos permite comprender; (5) un próximo paso de estudio. "
        "Puedes compartirla en un conversatorio si lo deseas; no tienes que contar datos personales.",
        "(1) ¿Cómo cambió el comercio del barrio entre 1990 y 2020? (2) Una lista de patentes y un relato de una comerciante. (3) La pandemia de 2020. (4) Nos permite comprender cómo llegamos al presente. (5) Practicar ubicar hitos en una línea de tiempo.",
        ["escribe los cinco elementos", "relaciona con un hito conocido", "no incluye datos personales"],
        ["cinco frases escritas"], ["dejar elementos vacíos", "copiar el ejemplo"],
        "Pregunta: «¿Qué elemento me costó más y qué haré para mejorarlo?»."),
    reinforce="Cuéntale a otra persona qué aprendiste en este módulo sin leer el cuaderno.",
    extend="Explica cómo usarías lo aprendido para investigar la historia de tu barrio o de tu comunidad.",
)
