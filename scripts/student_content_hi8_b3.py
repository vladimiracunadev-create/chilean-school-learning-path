"""Cuaderno del estudiante, 8.º básico Historia, Geografía y Ciencias Sociales: OA 12 (guerra de Arauco y sociedad de frontera)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI08 OA 12"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a situar en el tiempo y en el espacio la guerra de Arauco y a plantear el problema: por qué la conquista fracasó al sur del Biobío y qué sociedad nació de ese fracaso.",
    ["Sé que Pedro de Valdivia fundó Santiago en 1541.", "Sé ubicar el río Biobío y la ciudad de Concepción en un mapa de Chile."],
    [
        "Tras fundar Santiago en 1541, los españoles avanzaron hacia el sur y fundaron ciudades como Concepción (1550). Al sur del río Biobío vivían los mapuches, que defendieron su territorio y su forma de vida. La guerra de Arauco fue el largo conflicto entre españoles y mapuches que duró más de un siglo, sobre todo entre 1550 y 1650, y con episodios posteriores. Se llama así por la zona de Arauco, donde ocurrieron muchos combates.",
        "Hubo hitos importantes. En 1553 murió Pedro de Valdivia en Tucapel, tras un ataque mapuche. En 1598, en la batalla de Curalaba, murió el gobernador Martín García Óñez de Loyola y los mapuches destruyeron varias ciudades españolas al sur del Biobío. Después de Curalaba, el río Biobío quedó como una frontera entre el territorio español y el mapuche, que se mantuvo por siglos.",
        "El problema que estudiaremos es doble: ¿por qué los españoles no pudieron conquistar ese territorio, y cómo se organizó la vida en la zona de frontera? La respuesta no es solo militar. También hay comercio, mestizaje, misiones y acuerdos, es decir, convivencia mezclada con conflicto. Para estudiarlo hay que ubicar fechas, lugares y actores.",
    ],
    [("guerra de Arauco", "largo conflicto entre españoles y mapuches por el control del territorio al sur del Biobío"), ("frontera", "zona de contacto y límite entre dos territorios, aquí entre el español y el mapuche"), ("mapuche", "pueblo originario que habitaba el centro-sur de Chile, cuyo nombre significa «gente de la tierra»"), ("Curalaba", "batalla de 1598 en que murió el gobernador Óñez de Loyola"), ("gobernador", "máxima autoridad del reino de Chile en la época colonial")],
    [
        ("Ubicar un hecho en el siglo", "La batalla de Curalaba ocurrió en 1598. ¿En qué siglo fue?", ["El siglo XVI va de 1501 a 1600.", "1598 está dentro."], "Siglo XVI"),
        ("Ubicar en el espacio", "Una ciudad española de ejemplo estaba al sur del Biobío antes de 1598. ¿Estaba en territorio español estable o en la zona de conflicto?", ["Al sur del Biobío vivían los mapuches.", "Esas ciudades fueron atacadas."], "En la zona de conflicto"),
    ],
    [
        ("Creer que la guerra de Arauco duró unos pocos años.", "Duró más de un siglo, con períodos de combate y de paz.", "Revisa las fechas de 1550 a 1650."),
        ("Pensar que fue solo una guerra de armas.", "También hubo comercio, mestizaje, misiones y acuerdos.", "Agrega la convivencia al análisis."),
    ],
    [
        ("¿En qué año fundó Pedro de Valdivia la ciudad de Santiago?", "1541", "Se dice en la clase."),
        ("¿Qué río quedó como frontera después de Curalaba?", "El Biobío", "Se explicó en el segundo párrafo."),
        ("¿Quiénes vivían al sur del Biobío?", "Los mapuches", "Así lo dice el primer párrafo."),
    ],
    [
        ("¿Qué pasó en 1553 en Tucapel?", "Murió Pedro de Valdivia tras un ataque mapuche", "Está en el segundo párrafo."),
        ("¿Por qué se llama «guerra de Arauco»?", "Por la zona de Arauco, donde ocurrieron muchos combates", "Lo explica el primer párrafo."),
        ("¿Qué significa que la guerra «no fue solo militar»?", "Que también hubo comercio, mestizaje, misiones y acuerdos", "Es la idea del tercer párrafo."),
    ],
    [
        arith("Valdivia fundó Santiago en 1541 y murió en 1553. ¿Cuántos años pasaron entre ambos hechos?", "1553-1541", "Se resta el año menor al mayor."),
        arith("Entre Curalaba (1598) y el año 1641 ocurrió el Parlamento de Quillín. ¿Cuántos años pasaron entre ambos hechos?", "1641-1598", "Se resta el año de Curalaba al de Quillín."),
        ("Una ficha de ejemplo dice: «1550: se funda Concepción, junto a la desembocadura del Biobío». ¿Qué ubicación aporta para entender la frontera posterior?", "Que Concepción estaba junto al Biobío, el río que luego fue frontera", "La ciudad quedó en el borde del territorio mapuche."),
    ],
    [
        ("Un estudiante escribe: «Los españoles perdieron porque no tenían armas». ¿Qué error comete según la clase?", "Reduce la causa a un solo factor; la clase explica que fue una resistencia mapuche prolongada y que la respuesta no es solo militar", "Una explicación histórica suele tener varias causas."),
        ("Una crónica de ejemplo española de 1600 dice: «Los indios bárbaros destruyeron las ciudades». ¿Qué palabra revela la perspectiva del autor?", "«Bárbaros»", "Esa palabra juzga a los mapuches desde la mirada del colonizador."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = Curalaba (1598), B = fundación de Santiago (1541), C = muerte de Valdivia (1553).", "B, C, A", "Las fechas en orden son 1541, 1553 y 1598."),
        arith("Un fuerte de ejemplo tenía 80 soldados antes de un ataque y quedan 55. ¿Cuántos soldados se perdieron?", "80-55", "Se resta lo que queda de lo inicial."),
    ],
    [("Una línea de tiempo de ejemplo marca 1541 (Santiago), 1550 (Concepción), 1553 (muerte de Valdivia) y 1598 (Curalaba). ¿Cuántos años pasaron desde la fundación de Concepción hasta Curalaba?", "48 años", "1598 menos 1550 es 48.")],
    [("¿Qué es una frontera, en esta unidad?", "Una zona de contacto y límite entre el territorio español y el mapuche", "Está en el vocabulario."), ("¿Qué batalla de 1598 cambió la situación?", "Curalaba", "Allí murió el gobernador y fueron destruidas ciudades."), ("¿Qué dos tipos de relación hubo en la frontera?", "Conflicto y convivencia", "Se explicó en el tercer párrafo.")],
    (
        "Dibuja un mapa simple de Chile central y sur con Santiago, Concepción, el río Biobío y la zona mapuche. Marca con una flecha el avance español y con una línea la frontera después de 1598. Escribe tres fechas de la clase y una pregunta que el mapa no responde.",
        "Mapa con Santiago, Concepción, Biobío, zona mapuche, frontera. Fechas: 1541, 1553, 1598. Pregunta: ¿quiénes comerciaban en la frontera?",
        ["ubica Santiago, Concepción y el Biobío", "marca la frontera", "escribe tres fechas", "formula una pregunta que el mapa no responde"],
        ["mapa simple con rótulos y una pregunta"],
        ["ubicar el Biobío al norte de Santiago", "olvidar la perspectiva mapuche"],
        "Cuenta el mapa a una persona de tu casa en un minuto.",
    ),
    "Escribe la diferencia entre conquista y colonización en dos líneas.",
    "Escribe una pregunta sobre cómo vivían las personas en la frontera.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a contextualizar y seleccionar fuentes sobre la guerra de Arauco y la frontera. Sirve para ver qué dicen las crónicas, las actas y los relatos, y quién queda sin voz.",
    ["Sé qué es una fuente primaria y una secundaria.", "Conozco los hitos de la guerra de Arauco."],
    [
        "Las fuentes sobre la guerra de Arauco son en su mayoría españolas: cartas de gobernadores, crónicas y actas de reuniones. Los cronistas escribían desde su mirada y muchas veces para justificar la conquista. Un poema largo, La Araucana, de Alonso de Ercilla, publicado en el siglo XVI, cuenta la guerra desde un soldado español que admiró el valor mapuche. Otro texto, Cautiverio feliz, de Francisco Núñez de Pineda y Bascuñán (siglo XVII), narra su cautiverio entre los mapuches y muestra convivencia y conflicto.",
        "Los mapuches transmitían su historia sobre todo de forma oral, por eso hay menos textos escritos por ellos en esa época. Hoy las comunidades mapuches mantienen su memoria y su visión de los hechos, y los historiadores la estudian con respeto y con cuidado. Los parlamentos eran reuniones entre autoridades españolas y jefes mapuches, y dejaron actas que registran acuerdos aunque escritas por los españoles.",
        "Al leer una fuente hay que preguntar: ¿quién habla?, ¿cuándo?, ¿para quién?, ¿qué quiere lograr?, ¿quién no aparece? Una fuente no sirve para todo: sirve para responder ciertas preguntas y no otras. Elegir bien la fuente y reconocer sus límites es parte del trabajo del historiador.",
    ],
    [("crónica", "relato de hechos escrito por un testigo o cronista de la época"), ("parlamento", "reunión entre autoridades españolas y jefes mapuches para acordar paz y reglas"), ("acta", "documento que registra lo que se acordó en una reunión"), ("fuente oral", "relato que se transmite hablando de generación en generación"), ("cautiverio", "situación de una persona retenida por otro grupo")],
    [
        ("Identificar la perspectiva", "Fuente de ejemplo: «Carta del gobernador, 1620: los indios rebeldes impiden poblar el sur». ¿Desde qué perspectiva habla?", ["Es una autoridad española.", "Califica a los mapuches de rebeldes."], "La de una autoridad española que ve la resistencia como rebeldía"),
        ("Elegir fuente", "Pregunta: ¿qué se acordó en un parlamento? Opciones: acta del parlamento o poema épico. ¿Cuál conviene?", ["El acta registra los acuerdos.", "El poema es literatura."], "El acta del parlamento"),
    ],
    [
        ("Pensar que las crónicas españolas cuentan toda la verdad de la guerra.", "Cuentan la guerra desde un lado y a veces justifican la conquista.", "Pregunta quién habla y quién falta."),
        ("Creer que sin textos mapuches no hay perspectiva mapuche.", "La memoria oral y los estudios actuales con comunidades la conservan.", "Reconoce las fuentes orales."),
    ],
    [
        ("¿Quién escribió La Araucana?", "Alonso de Ercilla", "Se nombra en el primer párrafo."),
        ("¿Qué es un parlamento en esta unidad?", "Una reunión entre autoridades españolas y jefes mapuches para acordar paz y reglas", "Está en el vocabulario."),
        ("¿Qué tipo de fuente es un relato que se transmite hablando?", "Una fuente oral", "Está en el vocabulario."),
    ],
    [
        ("¿Por qué hay menos textos escritos por mapuches en la época?", "Porque transmitían su historia sobre todo de forma oral", "Lo explica el segundo párrafo."),
        ("¿Qué muestra el libro Cautiverio feliz, según la clase?", "Convivencia y conflicto en la frontera", "Se explicó en el primer párrafo."),
        ("Un acta de ejemplo dice: «Se acuerda no atacar durante dos años». ¿Qué permite saber y qué no?", "Permite saber el acuerdo, pero no si se cumplió", "Un acuerdo escrito no prueba su cumplimiento."),
    ],
    [
        ("Pregunta: ¿cómo veían los mapuches la guerra? Fuentes: 1 = carta de un gobernador; 2 = memoria oral transmitida por comunidades mapuches; 3 = lista de soldados. ¿Cuál es la más adecuada?", "La 2", "Expresa la perspectiva mapuche."),
        arith("Un acta de ejemplo registra a 45 jefes mapuches y 12 autoridades españolas en un parlamento. ¿Cuántas personas se mencionan en total?", "45+12", "Se suman los dos grupos."),
        ("Un cronista de ejemplo escribe: «Esos bárbaros solo saben pelear». ¿Qué debe sospechar un historiador de esa frase?", "Que expresa un juicio del autor y no un hecho comprobado", "«Bárbaros» y «solo saben» son valoraciones."),
    ],
    [
        ("Un estudiante concluye: «Como La Araucana elogia a los mapuches, los españoles los respetaban». ¿Qué límite tiene la conclusión?", "Un poema de un autor no muestra lo que pensaban todos los españoles", "Es una sola fuente, con propósito literario."),
        ("¿Por qué conviene cruzar un acta de parlamento con una crónica?", "Porque el acta registra acuerdos y la crónica da contexto, y así se contrastan", "Cada fuente aporta algo distinto."),
    ],
    [
        ("Ordena por distancia temporal de los hechos de 1598, de más cercana a más lejana: A = carta de un soldado de 1599, B = libro publicado en 1673, C = estudio actual.", "A, B, C", "Cuanto más cerca de 1598, más cercana la fuente."),
        arith("Cautiverio feliz se escribió en 1673. ¿Cuántos años después de Curalaba (1598) fue?", "1673-1598", "Se resta el año de Curalaba."),
    ],
    [("Un parlamento de ejemplo: «Año 1641, Quillín: autoridades españolas y jefes mapuches acuerdan respetar el Biobío como frontera». ¿Qué tipo de fuente sería un registro de ese encuentro y cuántos años después de Curalaba ocurrió?", "Un acta; 43 años", "1641 menos 1598 es 43.")],
    [("¿Qué es una crónica?", "Un relato de hechos escrito por un testigo o cronista de la época", "Está en el vocabulario."), ("¿Cuál es una fuente oral?", "Un relato que se transmite hablando de generación en generación", "Se definió en el vocabulario."), ("¿Qué pregunta ayuda a ver los límites de una fuente?", "¿Quién no aparece en ella?", "Se explicó en el tercer párrafo.")],
    (
        "Lee esta fuente de ejemplo: «Carta del capitán, 1650: los mapuches atacaron el fuerte de noche. Pedimos más soldados». Escribe una tabla con cuatro filas: quién habla, cuándo, qué quiere lograr, qué voz falta. Cierra con una frase que explique qué fuente adicional pedirías.",
        "Habla un capitán español en 1650. Quiere lograr más soldados. Falta la voz de los mapuches. Pediría el relato oral de una comunidad o un acta de parlamento.",
        ["identifica autor y fecha", "señala el propósito", "indica la voz que falta", "propone una fuente adicional"],
        ["tabla de cuatro filas y una frase final"],
        ["tomar la carta como verdad completa", "no pedir otra fuente"],
        "Pide a una persona de tu casa que lea la carta y opine qué faltaría saber.",
    ),
    "Escribe en tres líneas por qué las fuentes escritas por españoles tienen límites.",
    "Elige un parlamento o un cautiverio y escribe una pregunta que quieras responder.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a relacionar cambio, continuidad y territorio en la guerra de Arauco: cómo pasó de guerra ofensiva a defensiva, a parlamentos y a una frontera estable. Sirve para ver la zona del Biobío como un espacio que cambió con el tiempo.",
    ["Conozco Curalaba y la frontera del Biobío.", "Sé que un parlamento es una reunión de acuerdos."],
    [
        "Antes de 1598 los españoles intentaron ocupar y poblar el sur con ciudades y fuertes. Después de Curalaba, la Corona reorganizó la defensa. En 1603 el gobernador Alonso de Ribera creó un ejército profesional y permanente, pagado con dinero enviado desde el Perú, el llamado real situado. Era un ejército para defender la frontera, no solo para avanzar.",
        "En 1612 el jesuita Luis de Valdivia propuso la guerra defensiva: los españoles no avanzarían ni atacarían, y se enviarían misioneros. La idea no tuvo el éxito esperado. Más adelante los parlamentos, como el de Quillín en 1641, formalizaron acuerdos y reconocieron el Biobío como límite. En el siglo XVIII siguieron los parlamentos, aunque hubo también rebeliones.",
        "Hay un cambio: de la guerra de ocupación a la guerra defensiva y a los pactos. Y hay una continuidad: los mapuches mantuvieron su territorio al sur del Biobío hasta fines del siglo XIX, cuando el Estado de Chile ocupó la Araucanía, en las décadas de 1860 y 1880. El territorio explica mucho: bosques, ríos y lluvias dificultaban a los ejércitos españoles, mientras los mapuches conocían la zona.",
    ],
    [("ejército permanente", "ejército con soldados pagados que existe todo el año"), ("real situado", "dinero enviado desde el Perú para pagar el ejército de Chile"), ("guerra defensiva", "propuesta de no avanzar ni atacar, y enviar misioneros"), ("Araucanía", "región del sur de Chile donde vivían muchos mapuches"), ("territorio", "espacio con rasgos naturales y humanos propios")],
    [
        ("Distinguir cambio", "Antes de 1598 los españoles fundaban ciudades al sur del Biobío; después defendían una frontera. ¿Qué cambió?", ["Antes ocupaban y poblaban.", "Después defendían una línea."], "Pasaron de ocupar el sur a defender una frontera"),
        ("Reconocer continuidad", "Los mapuches conservaron su territorio al sur del Biobío hasta fines del siglo XIX. ¿Es un cambio o una continuidad?", ["Se mantuvo por mucho tiempo.", "Hasta la ocupación de la Araucanía."], "Una continuidad"),
    ],
    [
        ("Creer que la frontera del Biobío fue una línea inmóvil sin contactos.", "Hubo parlamentos, comercio y mestizaje a ambos lados.", "Piensa en la frontera como zona de contacto."),
        ("Pensar que los parlamentos terminaron los conflictos.", "Hubo rebeliones y malones aunque se firmaran acuerdos.", "Distingue acuerdo y cumplimiento."),
    ],
    [
        ("¿Qué gobernador creó en 1603 un ejército profesional y permanente?", "Alonso de Ribera", "Se nombra en el primer párrafo."),
        ("¿De dónde venía el dinero del real situado?", "Del Perú", "Está en el primer párrafo."),
        ("¿Quién propuso la guerra defensiva en 1612?", "El jesuita Luis de Valdivia", "Está en el segundo párrafo."),
    ],
    [
        ("¿Qué quería lograr la guerra defensiva?", "No avanzar ni atacar y enviar misioneros", "Es la definición de la clase."),
        ("¿Qué reconoció el Parlamento de Quillín de 1641?", "El Biobío como límite entre los dos territorios", "Se explicó en el segundo párrafo."),
        ("¿Por qué el territorio dificultaba a los ejércitos españoles?", "Por los bosques, ríos y lluvias, y porque los mapuches conocían la zona", "Lo dice el tercer párrafo."),
    ],
    [
        arith("Un ejército de ejemplo cuesta 3.000 monedas al mes. ¿Cuánto cuesta en 6 meses?", "3000*6", "Se multiplica el costo mensual por los meses."),
        ("Un mapa de ejemplo muestra el Biobío con fuertes en el lado norte. ¿Qué indica sobre el cambio posterior a Curalaba?", "Que los españoles se ubicaron a defender la línea del Biobío", "Los fuertes del norte marcan una defensa."),
        ("¿Cuántos años pasaron desde la creación del ejército permanente (1603) hasta el Parlamento de Quillín (1641)?", "38 años", "1641 menos 1603 es 38."),
    ],
    [
        ("Un estudiante dice: «Con el real situado los españoles se hicieron dueños del sur». ¿Qué error comete?", "El ejército defendía la frontera; los mapuches conservaron su territorio hasta fines del siglo XIX", "El dinero pagaba soldados, no cambió la soberanía de ese territorio."),
        ("¿Por qué la guerra defensiva fue un cambio respecto de lo anterior?", "Porque abandonó la ocupación armada del sur y propuso misioneros", "Dejó de avanzar y de atacar."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = ejército permanente (1603), B = Curalaba (1598), C = Parlamento de Quillín (1641).", "B, A, C", "Las fechas son 1598, 1603 y 1641."),
        arith("Un fuerte de ejemplo recibe 400 monedas del situado cada mes durante 5 meses. ¿Cuántas monedas recibe?", "400*5", "Se multiplica el pago mensual por los meses."),
    ],
    [("Un esquema de ejemplo muestra tres columnas: «1550-1598: ocupación y ciudades», «1603-1640: ejército y guerra defensiva», «1641 en adelante: parlamentos». ¿En qué columna cae el ejército permanente de 1603?", "En la segunda", "1603 está entre 1603 y 1640.")],
    [("¿Qué es el real situado?", "Dinero enviado desde el Perú para pagar el ejército de Chile", "Está en el vocabulario."), ("¿Qué se mantuvo igual hasta fines del siglo XIX?", "El territorio mapuche al sur del Biobío", "Es la continuidad de la clase."), ("¿Qué cambió después de Curalaba?", "Los españoles pasaron a defender una frontera", "Es el cambio de la clase.")],
    (
        "Completa una línea de tiempo con tres tramos: «antes de 1598», «1603 a 1641» y «después de 1641». En cada tramo escribe qué hacían los españoles (ocupar, defender, pactar) y qué se mantenía igual para los mapuches. Termina con una frase que explique el papel del territorio.",
        "Antes de 1598: ocupar y fundar ciudades. 1603 a 1641: ejército permanente y guerra defensiva. Después de 1641: parlamentos. Los mapuches mantuvieron su territorio. El territorio de bosques y ríos favorecía la defensa.",
        ["ubica los tres tramos", "indica la acción española en cada uno", "señala la continuidad mapuche", "explica el papel del territorio"],
        ["línea de tiempo con tres tramos y una frase"],
        ["olvidar la continuidad mapuche", "desordenar las fechas"],
        "Explica tu línea de tiempo a una persona de tu casa.",
    ),
    "Dibuja un esquema del Biobío con fuertes y ciudades a ambos lados.",
    "Explica por qué la frontera fue un espacio que cambió con el tiempo.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a contrastar los actores de la frontera (españoles, mapuches y mestizos), sus causas y sus perspectivas. Sirve para ver que no hubo solo dos bandos y que había intereses distintos.",
    ["Conozco los hitos de la guerra de Arauco.", "Sé que una perspectiva es un punto de vista."],
    [
        "En la frontera convivían varios actores. Los españoles incluían a gobernadores, soldados, colonos y misioneros. Los mapuches incluían a jefes de comunidad, llamados lonkos, y a jefes de guerra, llamados toquis. Y estaban los mestizos, hijos de españoles y mapuches, que muchas veces servían de intermediarios. También había intérpretes, llamados lenguaraces, que traducían en las reuniones.",
        "Las causas del conflicto fueron varias. Los españoles buscaban tierras, mano de obra y control del territorio; durante el siglo XVII se permitió esclavizar a prisioneros mapuches de guerra, práctica que causó mucho daño y que después se prohibió. Los mapuches defendían su territorio, su libertad y su forma de vida, y usaron caballos y armas de hierro que aprendieron de los españoles. Los misioneros querían evangelizar y a veces protegían a los mapuches de abusos.",
        "Cada actor veía la frontera de forma distinta. Un soldado veía peligro y falta de pago; un lonko veía una amenaza a su comunidad y también oportunidades de comercio; un misionero veía almas por convertir. Para contrastar perspectivas hay que preguntar qué quería cada actor, qué ganaba y qué perdía, y quién cuenta la historia.",
    ],
    [("lonko", "jefe de una comunidad mapuche"), ("toqui", "jefe de guerra mapuche elegido en tiempos de conflicto"), ("lenguaraz", "intérprete entre españoles y mapuches"), ("mestizo", "hijo de español y mapuche u otro pueblo originario"), ("intermediario", "persona que sirve de puente entre dos grupos")],
    [
        ("Reconocer un actor", "Una persona de ejemplo traduce lo que dicen los jefes mapuches a las autoridades españolas. ¿Cómo se llamaba?", ["Traduce entre dos lenguas.", "Esa función era la de lenguaraz."], "Lenguaraz"),
        ("Contrastar perspectivas", "Un soldado español y un lonko mapuche observan el mismo fuerte. ¿Por qué lo ven distinto?", ["El soldado lo ve como defensa.", "El lonko lo ve como amenaza a su territorio."], "Porque tienen intereses y experiencias distintas"),
    ],
    [
        ("Creer que todos los españoles y todos los mapuches pensaban igual.", "Había grupos con intereses distintos, como misioneros y colonos.", "Distingue actores dentro de cada lado."),
        ("Olvidar a los mestizos en la historia de la frontera.", "Eran intermediarios y parte de la sociedad que se formó.", "Incluye a los mestizos como actores."),
    ],
    [
        ("¿Cómo se llamaba el jefe de una comunidad mapuche?", "Lonko", "Está en el vocabulario."),
        ("¿Cómo se llamaba el jefe de guerra?", "Toqui", "Está en el vocabulario."),
        ("¿Qué hacían los lenguaraces?", "Traducían entre españoles y mapuches", "Está en el vocabulario."),
    ],
    [
        ("Nombra una causa española del conflicto.", "Tierras, mano de obra o control del territorio", "Se nombran en el segundo párrafo."),
        ("¿Qué defendían los mapuches?", "Su territorio, su libertad y su forma de vida", "Se explicó en el segundo párrafo."),
        ("¿Qué nuevo medio usaron los mapuches que aprendieron de los españoles?", "El caballo y las armas de hierro", "Se nombran en el segundo párrafo."),
    ],
    [
        arith("En un parlamento de ejemplo asisten 30 lonkos, 6 intérpretes y 9 autoridades españolas. ¿Cuántas personas se mencionan?", "30+6+9", "Se suman los tres grupos."),
        ("Una carta de ejemplo de un misionero dice: «Los soldados cometen abusos contra los mapuches». ¿Qué perspectiva muestra?", "La de un misionero que critica los abusos", "Habla de defensa frente a los abusos."),
        ("Un mestizo de ejemplo trabaja de intérprete en el fuerte y es hijo de un soldado y de una mujer mapuche. ¿Por qué su posición es especial?", "Porque pertenece a ambos mundos y puede servir de puente", "Conoce las dos lenguas y culturas."),
    ],
    [
        ("Un estudiante dice: «Los mapuches solo peleaban y nunca comerciaban». ¿Qué error comete?", "Ignora que comerciaban y negociaban en parlamentos", "La frontera también fue espacio de comercio y acuerdos."),
        ("Una fuente de ejemplo española dice: «Los indios no entienden la paz». ¿Qué pregunta debe hacer un historiador?", "¿Por qué lo dice y qué dirían los mapuches?", "Hay que contrastar con la perspectiva mapuche."),
    ],
    [
        ("¿Quién era el jefe de guerra mapuche: el toqui o el lonko?", "El toqui", "El lonko era jefe de una comunidad; el toqui, jefe de guerra."),
        arith("Una comunidad de ejemplo tiene 90 familias y 15 comercian con los españoles. ¿Cuántas no comercian?", "90-15", "Se restan las que comercian del total."),
    ],
    [("Fuentes de ejemplo. Fuente A: «El fuerte protege a los colonos del sur». Fuente B: «El fuerte invade nuestras tierras». ¿Qué actor habla en cada una: colonos o mapuches?", "A, colonos; B, mapuches", "La A habla de proteger y la B de invasión.")],
    [("¿Qué es un intermediario?", "Una persona que sirve de puente entre dos grupos", "Está en el vocabulario."), ("¿Qué querían los misioneros?", "Evangelizar y a veces proteger de abusos", "Se explicó en el segundo párrafo."), ("¿Por qué contrastar perspectivas?", "Para no contar la historia desde un solo lado", "Se explicó en el tercer párrafo.")],
    (
        "Escribe un diálogo de seis líneas entre un soldado español y un lonko mapuche en un parlamento de ejemplo. Cada uno debe nombrar lo que quiere (soldado: paz y seguridad para el fuerte; lonko: respeto al territorio y comercio justo) y una cosa que el otro no ha considerado.",
        "Soldado: Queremos paz y seguridad para el fuerte. Lonko: Queremos respeto a nuestro territorio y comercio justo. Soldado: No habíamos considerado sus pérdidas. Lonko: Ustedes no entienden nuestra autoridad.",
        ["incluye a los dos actores", "cada uno dice lo que quiere", "cada uno menciona algo del otro", "mantiene respeto en el diálogo"],
        ["diálogo de seis líneas"],
        ["presentar a un solo lado como razonable", "usar términos despectivos"],
        "Lee el diálogo en voz alta con una persona de tu casa, cada uno en un papel.",
    ),
    "Escribe en cinco líneas qué ganaba y qué perdía cada actor en la frontera.",
    "Escribe una pregunta sobre cómo vivían las familias mestizas.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a construir un argumento con evidencia sobre las formas de convivencia y conflicto en la frontera. Sirve para evaluar si la frontera fue solo guerra o también intercambio.",
    ["Conozco los actores de la frontera.", "Sé que un argumento tiene afirmación, evidencia y límite."],
    [
        "En la frontera hubo conflicto y convivencia al mismo tiempo. El conflicto se vio en combates, malones (ataques mapuches a estancias y fuertes), malocas (expediciones españolas que capturaban personas) y esclavitud de prisioneros. La convivencia se vio en el comercio: los mapuches vendían ganado, ponchos y sal, y compraban hierro, vino y telas. También en las misiones, los parlamentos y los matrimonios y relaciones entre grupos, que dieron origen a población mestiza.",
        "Para argumentar sobre esta pregunta se necesita una afirmación clara, por ejemplo: «La frontera fue una zona de conflicto y de intercambio que formó una sociedad mestiza». La evidencia puede ser un registro de comercio, un acta de parlamento y un testimonio de cautiverio. El límite es que la mayoría de esos documentos fueron escritos por españoles y no muestran todo lo que vivieron las comunidades mapuches.",
        "También se puede pensar en las consecuencias: la frontera estimuló ganadería y comercio, mezcló costumbres y creó lazos de parentesco. Pero también causó muertes, pérdida de tierras y cautiverio. Un buen argumento incluye ambas caras y no oculta ninguna.",
    ],
    [("malón", "ataque mapuche a estancias, pueblos o fuertes"), ("maloca", "expedición española para capturar personas o ganado"), ("intercambio", "trueque o venta de productos entre grupos"), ("parentesco", "lazos familiares, como el matrimonio o la descendencia"), ("consecuencia", "resultado de un hecho")],
    [
        ("Clasificar un dato", "Un registro de ejemplo dice: «Se intercambian 20 ponchos mapuches por 10 cuchillos de hierro». ¿Es conflicto o convivencia?", ["Es un intercambio acordado.", "Eso es convivencia."], "Convivencia"),
        ("Separar afirmación y evidencia", "«La frontera fue una zona de conflicto y de intercambio». ¿Es una afirmación o una evidencia?", ["Es una respuesta general.", "Necesita datos que la apoyen."], "Una afirmación"),
    ],
    [
        ("Presentar la frontera solo como guerra.", "Hubo comercio, parlamentos, misiones y mestizaje.", "Incluye evidencias de convivencia."),
        ("Presentar la frontera solo como armonía.", "Hubo malones, malocas y esclavitud.", "Incluye evidencias de conflicto."),
    ],
    [
        ("¿Qué es un malón?", "Un ataque mapuche a estancias, pueblos o fuertes", "Está en el vocabulario."),
        ("¿Qué compraban los mapuches a los españoles?", "Hierro, vino y telas", "Se nombran en el primer párrafo."),
        ("¿Qué vendían los mapuches?", "Ganado, ponchos y sal", "Se nombran en el primer párrafo."),
    ],
    [
        ("¿Qué es una maloca?", "Una expedición española para capturar personas o ganado", "Está en el vocabulario."),
        ("¿Por qué un parlamento muestra convivencia?", "Porque ambos lados se reúnen a negociar acuerdos", "Es una forma de diálogo."),
        ("¿Qué límite tienen muchos documentos sobre la frontera?", "Fueron escritos por españoles y no muestran toda la vivencia mapuche", "Se explicó en el segundo párrafo."),
    ],
    [
        arith("En una feria de frontera de ejemplo se intercambian 35 ponchos y 25 sacos de sal. ¿Cuántos productos se intercambian?", "35+25", "Se suman los dos tipos de productos."),
        ("Una crónica de ejemplo cuenta: «Un malón destruyó 3 estancias». Otra: «Un parlamento acordó entregar 40 caballos como regalo». ¿Cuál muestra conflicto y cuál convivencia?", "La primera conflicto; la segunda convivencia", "El malón es ataque; el parlamento es acuerdo."),
        ("Elige la mejor evidencia para la afirmación «Hubo comercio en la frontera»: 1 = un acta con intercambio de ponchos y hierro; 2 = un poema sobre la guerra; 3 = una lista de soldados.", "La 1", "El acta muestra intercambios concretos."),
    ],
    [
        ("Un estudiante concluye: «Como hubo parlamentos, no hubo guerra después de 1641». ¿Qué error comete?", "Un acuerdo no impide rebeliones o ataques posteriores", "Hubo conflictos aun con parlamentos."),
        ("¿Por qué un buen argumento debe incluir tanto conflicto como convivencia?", "Porque la frontera tuvo ambas caras y omitir una distorsiona la historia", "Ambas caras forman la sociedad de frontera."),
    ],
    [
        ("Ordena las partes de un argumento: A = límite, B = afirmación, C = evidencia.", "B, C, A", "Primero se afirma, luego se prueba y al final se reconoce el límite."),
        arith("En un año de ejemplo hubo 6 malones y 14 intercambios en una zona. ¿Cuántos eventos se registraron?", "6+14", "Se suman los dos tipos de eventos."),
    ],
    [("Datos de ejemplo de una zona fronteriza en 1700: «3 malones, 5 parlamentos pequeños y 12 intercambios comerciales». Según esos datos, ¿cuántos hechos de convivencia (parlamentos e intercambios) y cuántos de conflicto (malones) hubo?", "17 de convivencia y 3 de conflicto", "5 + 12 = 17 de convivencia; los 3 malones son conflicto. Los datos cuentan hechos, no cuánta gente murió.")],
    [("¿Qué es una afirmación?", "La respuesta que defiendes ante una pregunta", "Es la respuesta que se defiende y luego se apoya con datos."), ("¿Qué muestra un registro de ponchos y hierro?", "Convivencia por intercambio", "Es comercio acordado."), ("¿Qué consecuencia negativa tuvo la frontera?", "Muertes, pérdida de tierras y cautiverio", "Se nombra en el tercer párrafo.")],
    (
        "Responde en cinco líneas: «¿Fue la frontera una zona de guerra o de convivencia?». Usa esta evidencia de ejemplo: malones; intercambio de ponchos por hierro; parlamento de Quillín (1641); población mestiza. Incluye afirmación, dos datos y un límite.",
        "Fue una zona de conflicto y de convivencia. Hubo malones, pero también intercambio de ponchos por hierro y parlamentos como el de Quillín. Límite: casi todos los documentos son españoles y no cuentan toda la vivencia mapuche.",
        ["escribe una afirmación que reconozca ambas caras", "usa al menos dos datos de la lista", "incluye un límite pertinente"],
        ["texto de cinco líneas"],
        ["presentar solo guerra o solo armonía", "no incluir límite"],
        "Lee tu texto a una persona de tu casa y pídele que identifique la afirmación.",
    ),
    "Dibuja un esquema con dos columnas, conflicto y convivencia, con tres ejemplos en cada una.",
    "Escribe una frase que explique por qué la frontera formó una sociedad mestiza.",
)

# ================================================================ clase 6
lesson(
    OA, 6,
    "Aprenderé a evaluar las proyecciones y los límites de lo aprendido sobre la guerra de Arauco y la sociedad de frontera. Sirve para ver qué dejó la frontera hasta hoy y qué no sabemos todavía.",
    ["Conozco los hitos, actores y formas de convivencia de la frontera.", "Sé construir un argumento con afirmación, evidencia y límite."],
    [
        "La frontera dejó huellas que continúan. En el territorio, muchas ciudades y fuertes del sur nacieron como puntos de defensa y de comercio. En la sociedad, se formó una población mestiza y una cultura fronteriza con mezcla de costumbres. En la historia de Chile, la ocupación de la Araucanía en el siglo XIX cambió la situación de las comunidades mapuches, que perdieron gran parte de su territorio. Hoy el pueblo mapuche mantiene su lengua, su cultura y reclamos que se discuten en la sociedad chilena.",
        "Evaluar es preguntar qué se puede afirmar con seguridad y qué no. Se puede afirmar que el Biobío fue frontera entre los siglos XVII y XIX y que hubo parlamentos y comercio. No se puede afirmar que todos los españoles tuvieran la misma actitud ni que todas las comunidades mapuches vivieran la frontera de igual forma. Tampoco se debe proyectar el pasado de forma simple a los conflictos actuales sin estudiar los cambios entre medio.",
        "Es importante hablar con respeto. La historia mapuche es parte de la historia de Chile, y los hechos deben contarse con rigor y sin estereotipos. Los detalles de su lengua, ritos y organización los enseñan las comunidades y las personas educadoras tradicionales, no esta clase.",
    ],
    [("proyección", "continuidad de un hecho o rasgo hacia épocas posteriores"), ("ocupación de la Araucanía", "avance del Estado de Chile sobre el territorio mapuche en el siglo XIX"), ("estereotipo", "idea simplificada y repetida sobre un grupo"), ("rigor", "cuidado en usar datos y fuentes verificables"), ("educador tradicional", "persona de una comunidad indígena que enseña su lengua y cultura")],
    [
        ("Reconocer una proyección", "¿Qué hecho del siglo XIX cambió la situación del territorio mapuche, según la clase?", ["Fue el avance del Estado de Chile.", "Se llama ocupación de la Araucanía."], "La ocupación de la Araucanía"),
        ("Reconocer un límite", "Un estudiante dice: «Todas las comunidades mapuches vivieron la frontera igual». ¿Se puede afirmar eso?", ["La clase indica que no todas la vivieron igual.", "Hay diferencias por zona y por actor."], "No, no se puede afirmar"),
    ],
    [
        ("Proyectar el pasado sin estudiar los cambios intermedios.", "Entre el siglo XVII y hoy hubo muchos cambios, como la ocupación de la Araucanía.", "Revisa los hechos intermedios."),
        ("Hablar de los mapuches con estereotipos.", "Simplifica a un pueblo con ideas repetidas sin fundamento.", "Usa datos y fuentes, y evita generalizar."),
    ],
    [
        ("¿Qué río fue frontera entre los siglos XVII y XIX?", "El Biobío", "Se afirmó en la clase."),
        ("¿Qué siglo vio la ocupación de la Araucanía?", "El siglo XIX", "Se explicó en el primer párrafo."),
        ("¿Quiénes enseñan la lengua y los ritos mapuches, según la clase?", "Las comunidades y los educadores tradicionales", "Se dijo en el tercer párrafo."),
    ],
    [
        ("Menciona una huella de la frontera en la sociedad.", "Una población mestiza y una cultura de frontera con mezcla de costumbres", "Se explicó en el primer párrafo."),
        ("En Historia: ¿Qué es un estereotipo?", "Una idea simplificada y repetida sobre un grupo", "Está en el vocabulario."),
        ("¿Por qué no se debe proyectar el pasado de forma simple al presente?", "Porque entre medio hubo muchos cambios que hay que estudiar", "Lo dice el segundo párrafo."),
    ],
    [
        arith("La frontera del Biobío se reconoció en 1641 y la ocupación de la Araucanía comenzó en la década de 1860. ¿Cuántos años aproximados pasaron entre 1641 y 1861?", "1861-1641", "Se resta el año menor al mayor."),
        ("Una afirmación de ejemplo dice: «Todos los españoles odiaban a los mapuches». ¿Qué evidencia de la clase la contradice?", "Había misioneros que protegían, comerciantes y mestizos que vivían entre ambos mundos", "La clase muestra actores con actitudes distintas."),
        ("Elige la fuente más útil para evaluar «los mapuches mantuvieron su territorio hasta el siglo XIX»: 1 = un acta de parlamento de 1700; 2 = un poema; 3 = una receta.", "La 1", "El acta de parlamento muestra el reconocimiento del territorio."),
    ],
    [
        ("Un estudiante dice: «Los conflictos de hoy son idénticos a los de 1600». ¿Qué error comete?", "Ignora los cambios de siglos, como la ocupación de la Araucanía y las nuevas leyes", "El contexto cambió mucho."),
        ("¿Por qué hay que hablar con rigor y respeto de los mapuches?", "Porque su historia es parte de la historia de Chile y hay que evitar estereotipos", "Lo explica el tercer párrafo."),
    ],
    [
        ("Ordena de más antiguo a más reciente: A = ocupación de la Araucanía (siglo XIX), B = Parlamento de Quillín (1641), C = Curalaba (1598).", "C, B, A", "Las fechas son 1598, 1641 y siglo XIX."),
        arith("Desde la creación del ejército permanente (1603) hasta el inicio de la ocupación de la Araucanía (1861), ¿cuántos años pasaron?", "1861-1603", "Se resta el año de inicio al de término."),
    ],
    [("Un texto de ejemplo dice: «Los mapuches de hoy son los mismos de la guerra de Arauco». Un estudiante responde: «Hay continuidad cultural, pero también cambios». ¿Por qué la respuesta del estudiante es mejor que el texto?", "Porque reconoce lo que continúa sin ignorar los cambios de siglos", "El texto supone que nada cambió; la respuesta distingue continuidad y cambio.")],
    [("¿Qué es una proyección?", "La continuidad de un hecho hacia épocas posteriores", "Está en el vocabulario."), ("¿Por qué se necesita rigor?", "Para usar datos y fuentes verificables", "Está en el vocabulario."), ("¿Qué no se puede afirmar sobre todas las comunidades?", "Que vivieron la frontera de la misma forma", "Lo dice el segundo párrafo.")],
    (
        "Escribe un párrafo de seis líneas: «Lo que sé y lo que no sé de la frontera». Incluye dos afirmaciones que sí se pueden hacer con las fuentes de la unidad, dos cosas que no se pueden afirmar y una pregunta que te gustaría investigar con ayuda de una persona educadora tradicional.",
        "Sé que el Biobío fue frontera y que hubo parlamentos. No sé qué pensaban todas las comunidades ni cómo era la vida diaria de cada familia. Pregunta: ¿qué cuentan hoy las comunidades sobre los parlamentos?",
        ["incluye dos afirmaciones fundadas", "señala dos límites", "formula una pregunta respetuosa"],
        ["párrafo de seis líneas"],
        ["afirmar cosas sin fuente", "usar estereotipos"],
        "Comparte tu pregunta con una persona de tu casa y piensen a quién podrían consultar.",
    ),
    "Escribe un balance de tres líneas sobre qué aprendiste de la frontera.",
    "Anota una pregunta que solo una comunidad mapuche podría responder.",
)
