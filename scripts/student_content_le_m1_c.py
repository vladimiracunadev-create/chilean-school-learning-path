"""Cuaderno del estudiante, 1.º medio Lengua y Literatura, OA 17 (correferencia léxica con metáfora y metonimia).

Textos originales y breves; cada ejercicio trae el texto que necesita.
Aquí se definen los ayudantes `L`, `E`, `M`, `task`, `MAT` que reutilizan los otros módulos le_m1_c*.
"""
from __future__ import annotations

from student_lessons import ex, register

OA17 = "LE1M OA 17"
E = ex
MAT = "Este cuaderno, lápiz y los textos escritos en cada ejercicio. Si quieres, lápices de dos colores para subrayar."


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def M(stem, options, right, why):
    """Pregunta de alternativas A) B) C)...; `right` es el índice (0, 1, 2) de la correcta."""
    letters = "ABCD"
    # Sin punto final en las opciones: el registro reordena las alternativas y mueve el último signo.
    options = [o[:-1] if o.endswith(".") and not o.endswith(("..", "…", "etc.")) else o for o in options]
    options = [f"«{o}»" if o.endswith(("?", "!")) else o for o in options]
    q = stem + " " + " ".join(f"{letters[i]}) {o}" for i, o in enumerate(options))
    return ex(q, f"{letters[right]}) {options[right]}", why)


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 17, clase 1
L(OA17, 1,
  MAT,
  "Aprenderé a reconocer cómo un texto nombra varias veces lo mismo con palabras distintas (cadena de referencia) y a elegir esas palabras según el propósito y la audiencia, sin volver confuso el texto.",
  ["Reconozco sinónimos y palabras más generales (como «ave» y «gorrión»).", "Sé distinguir entre un texto informativo y uno literario."],
  ["En un texto hablas varias veces de la misma persona, cosa o idea. Eso de lo que se habla se llama referente. Las distintas expresiones que lo nombran forman una cadena de referencia, y que dos expresiones nombren lo mismo se llama correferencia. En «Un perro vagaba por la plaza. El animal olfateaba los bancos», «Un perro» y «El animal» tienen el mismo referente.",
   "La correferencia léxica usa palabras con significado propio para retomar el referente. Los recursos principales son: la repetición de la misma palabra; el sinónimo (casa, hogar); el hiperónimo, que es una palabra más general (gorrión, ave); el hipónimo, más específico (ave, gorrión); y la descripción, que nombra al referente por una característica («la capital de Chile» por Santiago). Cada recurso agrega una pista distinta.",
   "Cambiar de palabra solo para no repetir puede volver ambiguo un texto. En «El zorro vio al cuervo. El animal tenía un queso» no se sabe quién tiene el queso. Elige la expresión según el propósito y la audiencia: una noticia pide expresiones neutras; un cuento admite expresiones con más carga expresiva. Antes de reemplazar, pregúntate: ¿mi lector sabrá de quién hablo?"],
  [("referente", "persona, cosa o idea de la que se habla en un texto"), ("cadena de referencia", "conjunto de expresiones que nombran el mismo referente"), ("hiperónimo", "palabra más general que incluye a otra (ave incluye a gorrión)"), ("descripción", "expresión que nombra algo por una característica suya"), ("ambigüedad", "falta de claridad: una expresión puede entenderse de dos maneras")],
  [("Marcar la cadena", "Lee: «Un perro vagaba por la plaza. El animal olfateaba los bancos y el cachorro se detuvo ante la panadería. Después, el perro durmió.» ¿Cuántas expresiones nombran al perro?",
    ["El referente es el perro.", "Subrayo «Un perro», «El animal», «el cachorro» y «el perro».", "Compruebo que cada una puede leerse como el mismo perro."],
    "Cuatro expresiones: Un perro, El animal, el cachorro, el perro"),
   ("Detectar ambigüedad", "Lee: «La tía visitó a la abuela. La señora llevó empanadas.» ¿Quién llevó las empanadas?",
    ["«La señora» podría ser la tía o la abuela.", "El texto no permite decidir: es ambiguo.", "Se corrige repitiendo el nombre: «La tía llevó empanadas»."],
    "No se sabe: el texto es ambiguo hasta que se repite «La tía»")],
  [("Cambiar la palabra en cada mención aunque se pierda claridad.", "Se cree que repetir siempre es malo.", "Reemplaza solo si el lector identifica el referente sin dudar."),
   ("Pensar que repetir una palabra siempre es un error.", "Se confunde repetir con escribir mal.", "Repetir es válido cuando evita la ambigüedad.")],
  ([M("Lee: «El presidente del club habló. El dirigente pidió calma.» ¿Qué expresión retoma a «El presidente del club»?", ["El dirigente", "pidió calma", "habló"], 0, "«El dirigente» nombra a la misma persona con otra palabra."),
    M("¿Cuál es un hiperónimo de «gorrión»?", ["ave", "golondrina", "vuelo"], 0, "«Ave» incluye al gorrión; «golondrina» es otra ave y «vuelo» es una acción."),
    ex("Lee: «Lucía llegó tarde. La estudiante se disculpó y la joven se sentó atrás.» ¿Cuántas expresiones nombran a Lucía?", "3", "Son Lucía, la estudiante y la joven.")],
   [M("En «La luna salió. El satélite natural iluminó el mar.», ¿a qué se refiere «el satélite natural»?", ["a la luna", "al mar", "a la noche"], 0, "Es una descripción de la luna, que ya fue nombrada."),
    M("En «El gato persiguió al ratón por la cocina. El animal se escondió bajo la mesa.», ¿por qué «El animal» es problemático?", ["Puede referirse al gato o al ratón", "Es una palabra inventada", "Es un hipónimo del gato y del ratón"], 0, "Ambos son animales y el texto no indica cuál se escondió."),
    M("«La capital de Chile» usada en lugar de «Santiago» es un caso de…", ["descripción", "repetición", "hipónimo"], 0, "Nombra a Santiago por una característica suya.")],
   [M("Completa para no repetir y mantener la claridad: «Valparaíso tiene cerros y escaleras. ___ atrae turistas cada verano.»", ["El puerto", "El cerro", "La región"], 0, "«El puerto» describe a Valparaíso; «el cerro» es solo una parte y «la región» es un territorio mayor."),
    ex("Lee: «El volcán despertó al amanecer. La montaña humeaba, y por eso los vecinos dejaron el pueblo. Más tarde, el volcán dejó de lanzar ceniza.» ¿Cuántas menciones tiene el volcán?", "3", "Son «El volcán», «La montaña» y «el volcán»."),
    M("Completa con un hiperónimo que incluya todo lo comprado: «Ana compró manzanas, peras y uvas. Guardó las ___ en el refrigerador.»", ["frutas", "manzanas", "verduras"], 0, "«Frutas» incluye las tres; «manzanas» dejaría fuera las otras y «verduras» es otra clase.")],
   [ex("Lee: «Pedro y Tomás discutieron. El joven pidió disculpas.» ¿Qué defecto tiene la cadena de referencia?", "Es ambigua: «El joven» puede ser Pedro o Tomás", "Ambos son jóvenes y el texto no dice cuál."),
    M("Una noticia sobre una persona que aún no tiene condena debe usar expresiones neutras. Para nombrarla, conviene…", ["el sospechoso", "el delincuente", "el culpable"], 0, "«El sospechoso» no afirma una culpa que aún no se prueba.")],
   [M("Lee: «Tomás y su hermano menor armaron un robot. Tomás lo probó y su hermano menor se rio.» ¿Qué versión varía la expresión sin generar dudas?", ["El mayor lo probó y el menor se rio.", "El niño lo probó y el pequeño se rio.", "El joven lo probó y el chico se rio."], 0, "«El mayor» y «el menor» distinguen a cada hermano; las otras opciones no."),
    M("Elige la palabra que incluye a las otras tres:", ["animal", "mamífero", "perro", "labrador"], 0, "«Animal» es la más general; las demás son casos cada vez más específicos.")]),
  [M("Un boletín escolar repite tres veces «la biblioteca». Para la segunda mención se propone: «La biblioteca estrenó horario. ___ abre a las 8:00.»", ["El recinto", "El estante", "La sala de computación"], 0, "«El recinto» nombra a la biblioteca como lugar; las otras opciones son otro referente.")],
  [E("¿Una cadena de referencia reúne expresiones que nombran el mismo referente?", "Sí", "Esa es su definición."),
   E("Si una palabra nueva puede entenderse de dos maneras, ¿conviene usarla?", "No", "Genera ambigüedad en el texto."),
   E("¿«Ave» es un hiperónimo de «gorrión»?", "Sí", "Es más general e incluye al gorrión.")],
  ("Lee este texto de ejemplo: «Camila presentó su informe sobre las ballenas. Camila explicó que las ballenas viven en todos los océanos. Camila mostró una foto de una ballena azul. Las ballenas necesitan mucho alimento.» Reescríbelo usando dos recursos distintos (por ejemplo un hiperónimo y una descripción) sin crear ambigüedad. Luego anota la cadena de referencia de Camila y la de las ballenas.",
   "«Camila presentó su informe sobre las ballenas. La expositora explicó que estos mamíferos marinos viven en todos los océanos. Mostró una foto de la ballena azul. Los animales necesitan mucho alimento.» Cadena de Camila: Camila, La expositora. Cadena de las ballenas: las ballenas, estos mamíferos marinos, los animales.",
   ["usa al menos dos recursos distintos", "mantiene identificables los referentes", "anota ambas cadenas"], ["texto reescrito", "dos cadenas escritas"], ["cambiar palabras que ocultan el referente", "mezclar a Camila con las ballenas"], "Léeselo a otra persona y pregúntale de quién habla en cada oración."),
  "Subraya en un texto breve de tu cuaderno de cualquier asignatura las expresiones que nombran el mismo referente.",
  "Escribe un párrafo de cuatro oraciones sobre un animal sin repetir su nombre más de dos veces.")

# ------------------------------------------------------------------ OA 17, clase 2
L(OA17, 2,
  MAT,
  "Aprenderé a usar la metáfora para retomar un referente: cómo funciona, cuándo el lector la entiende y qué tono o perspectiva aporta.",
  ["Sé qué es una cadena de referencia.", "Distingo una comparación de otras figuras."],
  ["La metáfora identifica una cosa con otra por una semejanza, sin usar «como»: «el rey de la selva» por el león. En la correferencia, una metáfora puede retomar un referente ya nombrado con una expresión figurada. En «El río bajó crecido. La serpiente de agua rompió el puente», «La serpiente de agua» es el río, visto como un animal que se curva y ataca.",
   "Para que la metáfora funcione como correferencia, el lector debe poder reconstruir el referente. Por eso primero se nombra el referente en forma literal y después aparece la metáfora, apoyada por el contexto. También debe haber una semejanza reconocible (el río serpentea, igual que una serpiente). No la confundas con la comparación, que sí usa «como»: «bravo como un león».",
   "La metáfora no solo evita repetir: agrega una mirada. Llamar «monstruo de hierro» a una locomotora da un tono amenazante; llamarla «caballo de acero» da un tono más admirativo. Por eso la eliges según tu propósito. Evita mezclar imágenes incompatibles (una serpiente que aletea) y no la uses en textos que deben ser exactos, como un instructivo."],
  [("metáfora", "figura que identifica una cosa con otra por semejanza, sin «como»"), ("comparación", "figura que une dos cosas por semejanza usando «como» u otro nexo"), ("referente literal", "forma directa y no figurada de nombrar algo"), ("tono", "actitud que transmite un texto: amenazante, admirativa, irónica…")],
  [("Leer la metáfora", "Lee: «La locomotora entró a la estación. El monstruo de hierro soltó vapor y se detuvo.» ¿Qué retoma «El monstruo de hierro» y qué tono da?",
    ["Antes se nombró «La locomotora»: ese es el referente literal.", "«Monstruo» sugiere tamaño y fuerza; «de hierro», el material.", "El tono es amenazante o imponente."],
    "Retoma a la locomotora y da un tono imponente"),
   ("Metáfora o comparación", "Lee: «El mar, como un espejo, reflejaba las nubes» y «El espejo azul reflejaba las nubes». ¿Cuál puede retomar a «el mar» dentro de una cadena?",
    ["La primera usa «como»: es una comparación y mantiene «el mar» como sujeto.", "La segunda reemplaza «el mar» por «el espejo azul»: es una metáfora.", "Solo la segunda sustituye al referente."],
    "«El espejo azul reflejaba las nubes»")],
  [("Usar una metáfora sin haber nombrado antes el referente.", "Se piensa que el lector adivinará.", "Nombra primero el referente literal y luego la metáfora."),
   ("Mezclar imágenes que no combinan.", "Se acumulan imágenes sin plan.", "Mantén un solo campo de imágenes en cada cadena breve.")],
  ([M("¿Cuál es una metáfora que retoma al sol?", ["el astro rey", "la estrella más cercana", "el sol de la mañana"], 0, "«El astro rey» lo presenta como un rey; las otras son descripciones literales."),
    M("¿Cuál de estas frases es una metáfora y no una comparación?", ["Su voz era una campana.", "Su voz sonaba como una campana.", "Su voz sonaba parecida a una campana."], 0, "No lleva «como» ni «parecida a»: identifica la voz con la campana."),
    M("Lee: «El aceite de oliva nuevo llenó las botellas. Los vecinos probaron el oro líquido con pan.» ¿A qué se refiere «el oro líquido»?", ["al aceite de oliva", "al pan", "a las botellas"], 0, "El contexto previo nombra el aceite y es lo que se prueba con pan.")],
   [M("¿Por qué una metáfora sirve de correferencia solo si el referente ya está claro?", ["Porque sin una pista previa el lector no sabe de qué se habla", "Porque la metáfora debe ser corta", "Porque la metáfora reemplaza a los verbos"], 0, "La metáfora depende del contexto para ser reconocida."),
    M("En «El camión frenó. La bestia de ocho ruedas soltó un bufido», ¿qué aporta «la bestia»?", ["una imagen de fuerza y amenaza", "la cantidad exacta de ruedas", "la hora del suceso"], 0, "Presenta al camión como un animal poderoso."),
    M("Lee: «El río avanzó entre los cerros. La serpiente de agua se curvaba en cada valle.» ¿Qué semejanza justifica la metáfora?", ["la forma sinuosa", "el color verde", "el tamaño de la boca"], 0, "El río se curva como el cuerpo de una serpiente.")],
   [M("Completa con la metáfora que retoma a la tormenta: «La tormenta cayó sobre el pueblo. ___ derribó los techos.»", ["La furia del cielo", "La nube de algodón", "El cielo azul"], 0, "Presenta la tormenta como una fuerza violenta; las otras imágenes no calzan."),
    M("Lee: «El bus llegó repleto. La lata de sardinas se detuvo en la esquina.» ¿Qué característica del bus destaca la metáfora?", ["que iba lleno de gente", "que era muy viejo", "que era muy rápido"], 0, "Las sardinas en lata van muy apretadas."),
    M("Completa: «El computador tardó cinco minutos en abrir el archivo. ___ nos hizo perder la paciencia.»", ["La tortuga electrónica", "La ventana abierta", "El teclado nuevo"], 0, "Se retoma al computador por su lentitud, rasgo de la tortuga.")],
   [M("Lee: «Julián habló con su hermano y con su primo. El león se enojó.» ¿Por qué la metáfora no funciona?", ["No se sabe a cuál de los dos se refiere", "Los leones no se enojan", "Julián no aparece"], 0, "Sin una pista previa, «el león» puede ser cualquiera de los dos."),
    M("¿Cuál de las dos oraciones mezcla imágenes incompatibles?", ["La serpiente de agua aleteaba en lo alto del bosque.", "La serpiente de agua se deslizaba entre los cerros."], 0, "Una serpiente no aletea: la imagen se contradice.")],
   [M("¿En cuál de los textos se prepara la metáfora para que el lector la entienda?", ["Paula dirigía el curso como quien lleva un barco por aguas difíciles. La capitana repartió las pruebas.", "Paula revisó las pruebas. La capitana de las nubes repartió helado.", "La capitana repartió las pruebas. Una profesora revisó otras."], 0, "Primero se instala la semejanza entre Paula y quien dirige un barco."),
    ex("Lee: «El tren llegó. El dragón de hierro bufó y el caballo de acero se detuvo. En el andén esperaban dos niñas.» ¿Cuántas expresiones nombran al tren?", "3", "Son «El tren», «El dragón de hierro» y «el caballo de acero».")]),
  [M("En una crónica deportiva se lee: «La selección de camiseta roja entró a la cancha. Los guerreros de rojo saludaron al público.» ¿Qué efecto tiene «Los guerreros de rojo»?", ["Da una imagen épica y de combate al equipo", "Informa el marcador final", "Corrige un error del texto"], 0, "Compara el partido con una batalla para dar emoción.")],
  [E("¿La metáfora usa «como» para unir los dos elementos?", "No", "Eso es propio de la comparación."),
   E("¿Conviene nombrar primero el referente literal y luego la metáfora?", "Sí", "Así el lector reconoce de qué se habla."),
   E("¿Una metáfora usada como correferencia puede agregar una valoración sobre el referente?", "Sí", "Cambia el tono y la perspectiva.")],
  ("Lee: «El invierno llegó a la costa. El mar se alzó contra el muelle y el viento golpeó los techos. Los pescadores amarraron sus botes.» Reescribe el párrafo retomando una vez a «el mar» y una vez a «el viento» con una metáfora cada vez. Luego explica en una frase qué tono quedó y justifica la semejanza de cada metáfora.",
   "«El invierno llegó a la costa. El mar se alzó contra el muelle y el gigante azul lo golpeó sin descanso. El viento golpeó los techos y el látigo invisible los hizo crujir.» Tono: dramático. «Gigante azul»: tamaño y fuerza; «látigo invisible»: golpe rápido que no se ve.",
   ["nombra el referente literal antes de la metáfora", "justifica la semejanza", "identifica el tono"], ["párrafo reescrito", "explicación breve"], ["metáfora sin referente previo", "imágenes incompatibles"], "Pide a alguien que subraye a qué se refiere cada metáfora: debería acertar."),
  "Anota tres metáforas que escuches en canciones, noticias o conversaciones y di a qué refieren.",
  "Escribe dos metáforas distintas para retomar a un mismo referente y compara el tono de cada una.")

# ------------------------------------------------------------------ OA 17, clase 3
L(OA17, 3,
  MAT,
  "Aprenderé a usar la metonimia para retomar un referente por una relación de cercanía (lugar por institución, contenedor por contenido, autor por obra) y a distinguirla de la metáfora.",
  ["Distingo metáfora y comparación.", "Reconozco una cadena de referencia."],
  ["La metonimia nombra una cosa con el nombre de otra que está en relación real con ella, no parecida. Los casos frecuentes son: el lugar por la institución («La Moneda informó» es el gobierno que trabaja en ese edificio); el contenedor por el contenido («se tomó un vaso» es el líquido); el autor por la obra («leímos a Cervantes» son sus libros); la parte por el todo («cien velas» son barcos); y el instrumento por quien lo usa («el pincel de Fernanda» es la pintora).",
   "La diferencia con la metáfora está en la base. La metáfora se apoya en una semejanza («serpiente de agua»); la metonimia, en una cercanía real (el edificio y el gobierno que lo ocupa). Como correferencia, la metonimia ahorra palabras y da tono institucional, pero necesita que el lector comparta el conocimiento: quien no sabe qué es La Moneda no entiende la referencia.",
   "Cuídala en dos puntos. Primero, la ambigüedad: una misma palabra puede nombrar el lugar y la institución («La Moneda es un edificio histórico; ayer La Moneda anunció un decreto»); avisa cuando cambia el referente. Segundo, la audiencia: para un lector que no conoce el contexto, escribe la expresión literal («el gobierno de Chile»)."],
  [("metonimia", "figura que nombra algo con el nombre de otra cosa relacionada con ella"), ("contigüidad", "cercanía o relación real entre dos cosas"), ("contenedor", "objeto que guarda algo, como un vaso"), ("institución", "organización con funciones públicas, como un gobierno")],
  [("Leer una metonimia", "Lee: «El Presidente de la República se reunió con sus ministros. La Moneda informó que la reunión duró dos horas.» ¿Quién informó?",
    ["«La Moneda» es un edificio, pero un edificio no informa.", "Nombra a quienes trabajan allí: el gobierno.", "Es una metonimia de lugar por institución."],
    "El gobierno, nombrado por su sede"),
   ("Metáfora o metonimia", "Compara «el rey de la selva» (el león) y «La Corona decidió» (el rey y su gobierno). ¿Cuál es metonimia?",
    ["En el primero hay semejanza de poder: metáfora.", "En el segundo, la corona es un símbolo de la monarquía: cercanía.", "La metonimia es «La Corona decidió»."],
    "«La Corona decidió»")],
  [("Creer que toda expresión figurada es metáfora.", "Solo se piensa en la semejanza.", "Pregunta: ¿hay semejanza (metáfora) o relación real de cercanía (metonimia)?"),
   ("Usar una metonimia que el lector no puede descifrar.", "Se supone un conocimiento compartido.", "Si la audiencia no conoce la referencia, escribe la expresión literal.")],
  ([M("En «Leímos a Cervantes en clase», ¿qué se leyó?", ["las obras de Cervantes", "la ciudad de Cervantes", "los apuntes de la profesora"], 0, "Se nombra al autor para referirse a sus libros."),
    M("En «La Moneda anunció un nuevo plan», ¿quién anunció?", ["el gobierno que trabaja en esa sede", "el edificio como objeto", "la ciudad de Santiago"], 0, "Los edificios no anuncian: se nombra a los que trabajan en él."),
    M("En «Pedro se tomó un vaso de agua fría», ¿qué relación hay entre «vaso» y lo que se toma?", ["contenedor por contenido", "autor por obra", "instrumento por quien lo usa"], 0, "Se nombra el recipiente en vez del agua que contiene.")],
   [M("En «Cien velas cruzaron la bahía», ¿qué significa «velas»?", ["barcos", "pañuelos", "luces"], 0, "Una parte del barco se usa para nombrar todo el barco."),
    M("¿En qué se basa la metonimia?", ["en una relación de cercanía entre dos cosas", "en una semejanza entre dos cosas", "en la repetición de un sonido"], 0, "La semejanza corresponde a la metáfora."),
    M("En «La corona anunció nuevos impuestos», ¿a quién se refiere «la corona»?", ["a la monarquía que gobierna", "a un adorno de metal", "a una joya del museo"], 0, "El símbolo del poder real nombra a quienes lo ejercen.")],
   [M("Completa con una metonimia: «Los hinchas llenaron el estadio. ___ cantó el gol con fuerza.»", ["El estadio", "El gol", "La pelota"], 0, "Se nombra el lugar para referirse a las personas que están en él."),
    M("Completa: «El gobierno presentó un proyecto de ley. ___ explicó que la reforma tendría efecto en un año.»", ["La Moneda", "El proyecto", "La ley"], 0, "La sede retoma al gobierno por metonimia."),
    M("¿Qué significa «manos» en «Necesitamos más manos para armar el escenario»?", ["personas que ayuden", "guantes de trabajo", "herramientas"], 0, "Una parte del cuerpo representa a las personas que trabajan.")],
   [M("Lee: «La Moneda es un edificio histórico de Santiago. Ayer La Moneda anunció un decreto.» ¿Qué cambió entre ambas menciones?", ["La primera es el edificio y la segunda, el gobierno", "Nada, ambas son el edificio", "La primera es una metáfora"], 0, "Cambia el referente, y el texto no lo avisa."),
    M("«El pincel de Fernanda ganó el concurso de pintura» usa…", ["metonimia: el instrumento por quien pinta", "metáfora: el pincel se parece a Fernanda", "comparación con «como»"], 0, "Hay una relación real entre el pincel y la pintora, no una semejanza.")],
   [M("¿Cuál de estas expresiones NO es metonimia?", ["Un gigante de roca vigilaba el valle.", "Bebió una copa.", "Leyó a Cervantes."], 0, "Aquí la roca se identifica con un gigante por semejanza: es metáfora."),
    M("Una nota informativa será leída por lectores extranjeros que no conocen los edificios del gobierno chileno. ¿Qué versión es más clara?", ["El gobierno chileno informó.", "La Moneda informó."], 0, "La expresión literal no exige conocimientos locales.")]),
  [M("En un editorial se lee: «Los vecinos pidieron una plaza más segura. El municipio respondió con luminarias nuevas.» ¿Qué relación usa «El municipio»?", ["se nombra la institución para referirse a quienes la dirigen", "una semejanza con un animal", "una repetición exacta"], 0, "Se nombra la institución para referirse a quienes decidieron en ella.")],
  [E("¿La metonimia se basa en una cercanía real entre dos cosas?", "Sí", "Esa es la diferencia con la metáfora."),
   E("Si el lector no conoce la referencia, ¿conviene usar la expresión literal?", "Sí", "Se piensa en la audiencia."),
   E("¿«Se tomó un vaso» es un ejemplo de contenedor por contenido?", "Sí", "Se nombra el recipiente y no el líquido.")],
  ("Lee: «El Ministerio de Salud entregó nuevas recomendaciones. El Ministerio recordó a la población que debe lavarse las manos. Además, el Ministerio pidió a los consultorios ordenar sus filas.» Reescribe el párrafo retomando una vez a «El Ministerio» con la metonimia «la cartera de Salud» (la cartera nombra al ministerio por las funciones que tiene a cargo) y una vez con una descripción. Después explica si un lector extranjero entendería «la cartera de Salud».",
   "«El Ministerio de Salud entregó nuevas recomendaciones. La cartera de Salud recordó a la población que debe lavarse las manos. Además, la autoridad sanitaria pidió a los consultorios ordenar sus filas.» «La cartera de Salud» es metonimia; «la autoridad sanitaria» es una descripción. Un lector extranjero podría no entender «cartera», así que en un texto para esa audiencia conviene la forma literal.",
   ["usa una metonimia y una descripción", "mantiene claro el referente", "evalúa la audiencia"], ["párrafo reescrito", "reflexión breve"], ["confundir metonimia con metáfora", "no considerar a la audiencia"], "Pregunta a otra persona qué entendió por cada expresión y compara."),
  "Busca en un diario o en una conversación dos expresiones como «La Moneda anunció…» y escribe quién se esconde detrás.",
  "Escribe tres metonimias (lugar por institución, autor por obra, contenedor por contenido) y la expresión literal de cada una.")

# ------------------------------------------------------------------ OA 17, clase 4
L(OA17, 4,
  MAT,
  "Aprenderé a planificar una cadena de referencia combinando repetición, hiperónimos, metáforas y metonimias según mi propósito, mi audiencia y la perspectiva que quiero dar.",
  ["Reconozco metáforas y metonimias.", "Sé qué es una cadena de referencia."],
  ["Antes de escribir conviene planificar la cadena. Sigue cinco pasos: 1) identifica los referentes principales; 2) anota las expresiones posibles (repetición, sinónimo, hiperónimo, descripción, metáfora, metonimia); 3) decide según el propósito (informar, persuadir, narrar) y la audiencia; 4) ordena: primero una mención clara y literal, y después las variaciones; 5) revisa que no haya ambigüedad.",
   "La elección de la expresión cambia la perspectiva. Para un mismo hecho, «los manifestantes» informa sin tomar partido; «los vándalos» condena; «los valientes» elogia. En un texto informativo conviene la neutralidad; en un texto que busca persuadir, puedes usar expresiones valorativas, siempre que no inventes datos ni confundas al lector.",
   "Una regla práctica: en una cadena breve usa como máximo una o dos expresiones figuradas, porque muchas imágenes seguidas hacen perder de vista el referente. Y adapta el recurso al género: en una crónica o un cuento, las metáforas dan color; en un instructivo, un informe o una circular, prefiere expresiones literales."],
  [("propósito", "para qué se escribe un texto: informar, persuadir, narrar…"), ("audiencia", "personas a las que se dirige un texto"), ("perspectiva", "mirada o valoración con que un texto presenta un hecho"), ("neutral", "que no toma partido ni valora")],
  [("Planificar una cadena", "Quieres persuadir a la comunidad de que cuide un parque. Planifica la cadena del referente «el parque».",
    ["Propósito: persuadir; referente: el parque.", "Primera mención literal: «el parque».", "Variaciones: «el pulmón verde del barrio» (metáfora) y «el espacio público» (hiperónimo)."],
    "el parque, el pulmón verde del barrio, el espacio público"),
   ("Elegir la perspectiva", "Una noticia informa de una marcha pacífica. ¿Qué expresión usarías para nombrar a quienes marcharon: «los manifestantes» o «los alborotadores»?",
    ["El propósito es informar sin tomar partido.", "«Alborotadores» condena a las personas.", "«Manifestantes» es neutral."],
    "los manifestantes")],
  [("Elegir expresiones valorativas en un texto que debe informar.", "No se piensa en el propósito.", "Si informas, usa expresiones neutras."),
   ("Llenar el texto de metáforas para que suene bonito.", "Se cree que más imágenes es mejor.", "Usa pocas y asegúrate de que el referente sea claro.")],
  ([M("¿Qué orden es mejor para presentar al referente?", ["El parque del barrio fue limpiado. El pulmón verde de la comuna luce renovado.", "El pulmón verde del barrio fue limpiado. El parque luce renovado."], 0, "Primero va la mención literal y luego la figurada."),
    M("Al planificar una cadena de referencia, ¿qué conviene decidir primero?", ["el propósito y la audiencia", "la cantidad de metáforas", "el tamaño de la letra"], 0, "De eso depende el tipo de expresión que se elija."),
    M("Una nota informativa cuenta que mucha gente fue a un concierto. ¿Cómo nombrarías neutralmente a esas personas?", ["los asistentes", "los fanáticos desbocados", "la marea humana"], 0, "Es la única expresión literal y sin valoración.")],
   [M("¿Por qué conviene limitar las metáforas en una cadena breve?", ["Porque muchas imágenes seguidas hacen perder de vista el referente", "Porque están prohibidas en textos escolares", "Porque no se pueden pronunciar"], 0, "El lector necesita reconocer de qué se habla."),
    M("Para un instructivo de primeros auxilios, ¿qué expresión es más adecuada para nombrar al botiquín?", ["el botiquín, el kit de emergencia", "el salvavidas dorado", "el tesoro blanco"], 0, "Un instructivo requiere exactitud, no imágenes."),
    M("«El despilfarro» usado para nombrar un proyecto de obras públicas muestra una postura…", ["crítica", "neutral", "elogiosa"], 0, "Afirma que el dinero se gastó mal.")],
   [M("Debes informar con neutralidad sobre un incendio forestal. ¿Qué cadena eliges?", ["el incendio, el siniestro, el fuego", "el incendio, la bestia roja, el demonio", "el incendio, el espectáculo, el festival"], 0, "Las tres expresiones del primer grupo son literales."),
    M("Debes persuadir a la comunidad de cuidar un humedal. ¿Qué cadena eliges?", ["el humedal, el pulmón del valle, el refugio de las aves", "el humedal, el barro, el terreno inútil", "el humedal, el sitio 12, el lote"], 0, "Resalta su valor y apoya el propósito."),
    M("Completa sin generar dudas: «Ema paseó a su perra Luna y saludó a su vecina. ___ ladró de alegría.»", ["La compañera de cuatro patas", "La señora", "La vecina"], 0, "Solo la perra tiene cuatro patas; las otras opciones nombran a la vecina.")],
   [M("Un plan nombra al mismo lugar así: «la cuna del saber», «el faro del barrio», «el corazón de la comuna» y «el motor del pueblo». ¿Qué problema tiene?", ["Demasiadas metáforas de ámbitos distintos (saber, luz, cuerpo, máquina) dificultan seguir el referente", "No usa ninguna palabra literal", "Es demasiado corto"], 0, "Las imágenes se acumulan sin una pista que las aclare."),
    M("Una circular a madres, padres y apoderados informa la fecha de una reunión. ¿Es adecuado nombrar al colegio «el hogar del saber»?", ["No, porque una circular debe ser clara y directa", "Sí, porque toda circular lleva metáforas", "Sí, porque así se evita repetir"], 0, "El propósito es informar con precisión.")],
   [M("Un diario informa que un taller de teatro se presentó en la plaza. ¿Qué cadena para el taller es adecuada para una noticia neutral y clara?", ["el taller, el grupo de teatro, los participantes", "el taller, los genios de la escena, los dioses del arte", "el taller, ellos, ellos"], 0, "Son expresiones literales que no valoran ni confunden."),
    M("Quieres persuadir sobre el valor de una biblioteca. ¿Qué plan de cadena cumple mejor con ese propósito y mantiene claro el referente?", ["la biblioteca, el tesoro de la comuna, el espacio de lectura", "la biblioteca, el tesoro, el dragón de la cueva", "la biblioteca, la sala, la sala, la sala"], 0, "Combina un elogio con una expresión literal y es coherente.")]),
  [M("Un afiche invita a cuidar el río del pueblo. ¿Qué redacción cumple mejor con persuadir y se entiende?", ["El río es la vena del pueblo: cuidemos el agua que nos da vida.", "El cauce hídrico de la zona registra caudal.", "La vena del pueblo, el río, el cauce, el agua, la vena."], 0, "Usa una metáfora clara apoyada por el referente literal.")],
  [E("¿Conviene decidir el propósito antes de elegir las expresiones?", "Sí", "El propósito orienta el tono."),
   E("¿Una expresión valorativa es adecuada en una noticia que debe ser neutral?", "No", "Toma partido y no informa."),
   E("¿Es mejor llenar la cadena de metáforas?", "No", "Pueden confundir el referente.")],
  ("Lee este hecho de ejemplo: «El colegio instaló una huerta en el patio. Un grupo de estudiantes la riega cada tarde.» Planifica dos cadenas de referencia para la huerta: una para una noticia del diario mural (neutral) y otra para un afiche que invita a participar (persuasiva). Escribe, para cada una, cuatro expresiones ordenadas y explica en dos líneas por qué las elegiste.",
   "Noticia: la huerta, el huerto escolar, el espacio de cultivo, la iniciativa. Afiche: la huerta, el rincón verde del colegio, el jardín que alimenta, la huerta. Elegí expresiones literales para informar y expresiones valorativas para invitar.",
   ["escribe cuatro expresiones por cadena", "ordena de lo literal a lo figurado", "justifica por propósito"], ["dos cadenas", "justificación"], ["usar el mismo registro en ambas", "olvidar la mención literal"], "Lee ambas cadenas y comprueba que suenen distinto según el propósito."),
  "Anota tres formas distintas de nombrar a tu colegio: una neutral, una afectuosa y una que usarías en una circular.",
  "Escribe dos versiones de una noticia de tres líneas sobre un evento escolar, una neutral y otra valorativa.")

# ------------------------------------------------------------------ OA 17, clase 5
L(OA17, 5,
  MAT,
  "Aprenderé a revisar mis textos con una lista de control para detectar y corregir problemas de correferencia: ambigüedad, imágenes sin referente, mezcla de figuras y registro inadecuado.",
  ["Sé usar metáforas y metonimias como correferencia.", "Sé planificar una cadena de referencia."],
  ["Revisar un texto no es solo corregir la ortografía. En la cadena de referencia conviene hacer cuatro preguntas. ¿Se entiende siempre de quién o de qué se habla? ¿Cada metáfora o metonimia está apoyada por una mención literal previa? ¿Las imágenes combinan entre sí? ¿El tono sirve al propósito y a la audiencia? Si alguna respuesta es «no», hay que corregir.",
   "Las correcciones más comunes son estas. Contra la ambigüedad: repite el nombre o agrega un rasgo («el mayor»). Contra la metáfora sin referente: nombra primero lo literal. Contra la mezcla de imágenes: elige un solo campo (por ejemplo, el del mar). Contra el exceso de figuras: deja una y vuelve literal el resto. Contra un tono inadecuado: cambia por una expresión neutral.",
   "Revisa con evidencia: señala en el texto la palabra o frase que justifica cada decisión y explica el efecto del cambio. Por ejemplo: «Cambié “el monstruo” por “la locomotora” porque la circular debe informar y no atemorizar». Así tu revisión es una decisión argumentada y no solo un gusto personal."],
  [("lista de control", "serie de preguntas que sirve para revisar un texto"), ("ambigüedad", "doble interpretación posible de una expresión"), ("campo de imágenes", "conjunto de imágenes de un mismo ámbito, como el del mar"), ("evidencia", "frase o dato del texto que sostiene una decisión")],
  [("Revisar un párrafo", "Revisa: «Sofía conversó con Ema. La leona decidió quedarse.» ¿Qué falla y cómo lo corriges?",
    ["Pregunta 1: ¿se entiende quién es «la leona»?", "No: puede ser Sofía o Ema, y no hay pista previa.", "Corrijo nombrando la característica antes: «Sofía, que siempre lidera al grupo, conversó con Ema. La leona decidió quedarse»."],
    "La metáfora no tiene referente claro; se corrige con una pista previa"),
   ("Mezcla de imágenes", "Revisa: «El barco de la economía navegaba tranquilo, pero el techo de los precios se derrumbó.» ¿Qué corriges?",
    ["Las imágenes son de dos campos: el mar y la construcción.", "Dejo un solo campo: el del mar.", "Escribo: «El barco de la economía navegaba tranquilo, pero la tormenta de los precios lo sacudió»."],
    "Se unifica el campo de imágenes")],
  [("Corregir solo la ortografía y no la cadena de referencia.", "Se cree que revisar es solo escribir sin faltas.", "Haz una revisión de cohesión con las preguntas de la lista."),
   ("Cambiar una expresión sin explicar por qué.", "Se corrige por intuición.", "Cita la frase y explica el efecto del cambio.")],
  ([M("Lee: «Marta le dio el libro a Inés. La señora lo guardó.» ¿Qué problema tiene el texto?", ["No se sabe a quién se refiere «la señora»", "Falta una tilde", "Sobra la coma"], 0, "La expresión puede retomar a cualquiera de las dos."),
    M("Lee: «Hablé con mi abuelo. El sabio del cerro me aconsejó tomar la ruta del sur.» ¿Cómo se corrige si el lector no conoce al abuelo como «sabio del cerro»?", ["Presentar antes que el abuelo es el sabio del cerro", "Eliminar toda la oración", "Repetir tres veces «el abuelo»"], 0, "La metáfora necesita una pista previa."),
    M("¿Cuál es una pregunta de la lista de control de correferencia?", ["¿Se entiende siempre de quién se habla?", "¿Hay una metáfora en cada oración?", "¿Cada oración repite el nombre del referente?"], 0, "Es la primera pregunta para revisar la cadena.")],
   [M("Lee: «El tren, un caballo de acero, se deslizaba. La serpiente de metal aleteó.» ¿Qué se corrige?", ["Las imágenes de caballo y serpiente no combinan", "Falta un punto", "Sobra la palabra «tren»"], 0, "Se mezclan campos de imágenes: animal de monte y reptil."),
    M("Una circular dice: «El monstruo de ladrillo celebrará su aniversario.» (el colegio). Si la circular debe informar, ¿qué cambio corresponde?", ["Usar «el colegio» o «el establecimiento»", "Agregar más metáforas", "Poner todo en mayúsculas"], 0, "Una circular necesita expresiones literales."),
    M("Un estudiante cambia «el monstruo» por «la locomotora» y escribe: «Porque la circular debe informar y no atemorizar». ¿Qué hizo bien?", ["Justificó el cambio con el propósito", "Evitó explicar", "Cambió el tema"], 0, "Una revisión argumentada se apoya en el propósito.")],
   [M("Corrige la ambigüedad: «Pablo y su primo viajaron al sur. El muchacho trajo mapas.» ¿Cuál reemplazo mantiene claridad si Pablo es el mayor?", ["El mayor trajo mapas.", "El joven trajo mapas.", "El chico trajo mapas."], 0, "«El mayor» distingue a Pablo del primo."),
    M("Unifica el campo de imágenes: «La biblioteca es un faro y su lectura, una cueva de oro.» Elige la versión coherente:", ["La biblioteca es un faro y su lectura, una luz en la noche.", "La biblioteca es un faro y su lectura, una cueva de oro.", "La biblioteca es un faro y su lectura, un pastel de manzana."], 0, "Faro y luz pertenecen al mismo campo."),
    M("Reduce las figuras sin cambiar de referente: «El gigante de piedra, el guardián eterno, el rey inmóvil dominaba el valle.» ¿Cuál es una versión mejor?", ["El cerro, un gigante de piedra, dominaba el valle.", "El rey, el guardián, el gigante dominaba el valle.", "El rey inmóvil dominaba el valle."], 0, "Nombra lo literal y deja una sola metáfora.")],
   [M("Lee: «El mandatario saludó. El Palacio de Gobierno ordenó actuar.» ¿Qué problema puede tener la segunda oración para un lector que no conoce el palacio?", ["Usa una metonimia que exige conocimiento previo", "Está demasiado corta", "Usa mayúsculas"], 0, "Nombra la sede, no al gobierno."),
    M("Si en una noticia ves «los delincuentes» para nombrar a una persona detenida pero aún no condenada, ¿qué revisión corresponde?", ["Cambiar por «los detenidos» o «los sospechosos»", "Agregar un adjetivo", "No cambiar nada"], 0, "La expresión inicial da por probada una culpa.")],
   [M("Revisa: «La tormenta de ideas llovió sobre la sala. La nube de niños jugaba sobre el pasto. El océano de papeles se derritió.» ¿Qué diagnóstico es el más completo?", ["Muchas figuras de campos distintos y sin referentes literales", "Falta una tilde", "Es un texto perfecto"], 0, "Hay exceso y mezcla de imágenes."),
    M("Revisa: «Matías prestó su bicicleta a Daniel. Luego, el ciclista no la devolvió.» ¿Cuál es el mejor arreglo si Daniel es quien no la devolvió?", ["Daniel no la devolvió.", "El ciclista no la devolvió.", "El dueño no la devolvió."], 0, "Nombrar a la persona evita la ambigüedad.")]),
  [M("Un afiche escolar dice: «La reina de las aulas invita a su fiesta el viernes.» (sin haber nombrado antes a la biblioteca). ¿Qué corrección es la más adecuada?", ["Nombrar antes el referente: «La biblioteca, la reina de las aulas, te invita…»", "Subir el tamaño de la letra", "Eliminar la fecha"], 0, "La metáfora necesita su referente literal.")],
  [E("¿Una revisión de correferencia incluye preguntarse si el referente es claro?", "Sí", "Es la primera pregunta."),
   E("¿Se puede mezclar un faro con una cueva y un pastel en una misma cadena breve?", "No", "Las imágenes deben combinar."),
   E("¿Conviene justificar cada cambio con el propósito del texto?", "Sí", "Así la revisión es argumentada.")],
  ("Revisa este borrador de ejemplo: «Fabiola y Nora ensayaron una obra de teatro. La estrella del grupo olvidó el libreto en casa. El gigante de la sala, el techo del teatro y el piso de los aplausos temblaron cuando la reina se dio cuenta.» Escribe una versión corregida (máximo tres oraciones) y debajo anota tres decisiones de revisión, cada una con la palabra o frase que cambiaste y el motivo.",
   "«Fabiola y Nora ensayaron una obra de teatro. Fabiola, la protagonista, olvidó el libreto en casa. Al darse cuenta, la actriz se puso nerviosa y el teatro quedó en silencio.» Decisiones: 1) «La estrella del grupo» pasó a «Fabiola, la protagonista» porque era ambiguo. 2) Quité «el gigante, el techo y el piso» porque mezclaban imágenes. 3) Cambié «la reina» por «la actriz» porque no estaba presentada.",
   ["corrige la ambigüedad", "elimina la mezcla de figuras", "justifica tres cambios con evidencia"], ["versión corregida", "tres decisiones justificadas"], ["no explicar los cambios", "mantener todas las figuras"], "Pide a otra persona que marque con un color lo que no entiende del texto corregido."),
  "Elige un párrafo que hayas escrito este año y revisa su cadena de referencia con las cuatro preguntas.",
  "Escribe un párrafo con tres errores de correferencia a propósito y entrégaselo a alguien para que los encuentre.")
