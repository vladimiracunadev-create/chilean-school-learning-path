"""Material del estudiante de 5.º básico, Historia, Geografía y Ciencias Sociales: OA 05 (vida colonial en Chile) y OA 06 (dependencia colonial, Iglesia y sociedad mestiza)."""
from __future__ import annotations

from hi5_lib import build

OA5 = "HI05 OA 05"
OA6 = "HI05 OA 06"

# ================================================================ OA 05 · VIDA COLONIAL EN CHILE
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (período colonial, hecha para este cuaderno). En Chile, la Colonia es el período en que el territorio formó parte del imperio español, desde la fundación de Santiago en 1541 hasta 1810, cuando se formó la Primera Junta Nacional de Gobierno. "
     "El territorio se llamaba Capitanía General de Chile y su capital era Santiago. Los españoles vivían sobre todo entre La Serena y Chiloé. Al sur del río Biobío estaba la frontera con el territorio mapuche. "
     "Las ciudades eran pequeñas. La mayoría de la gente vivía en el campo, en haciendas y pueblos. Para estudiar la vida colonial miramos cuatro dimensiones: la sociedad, los oficios, las costumbres y las celebraciones y el arte.")
build(
    OA5, 1, F,
    use="Aprenderé cuándo y dónde se desarrolló la Colonia en Chile y qué dimensiones de la vida vamos a estudiar. Sirve para ubicar la vida colonial en el tiempo y en el territorio.",
    prior=["Sé que Valdivia fundó Santiago en 1541.", "Sé que al sur del Biobío estaba el territorio mapuche.", "Sé calcular años entre dos fechas."],
    explain=[
        "La Colonia fue el período en que Chile formó parte del imperio español. Empezó con la fundación de Santiago, en 1541, y terminó en 1810, cuando se formó la Primera Junta Nacional de Gobierno. Fueron casi tres siglos.",
        "El territorio se llamaba Capitanía General de Chile y su capital era Santiago. Los españoles vivían sobre todo entre La Serena y Chiloé. Al sur del río Biobío estaba la frontera con el territorio mapuche. Las ciudades eran pequeñas y la mayoría de la gente vivía en el campo, en haciendas y pueblos.",
        "Para estudiar la vida colonial miramos cuatro dimensiones. La sociedad se pregunta quiénes formaban los grupos sociales. Los oficios y actividades económicas preguntan en qué trabajaba la gente. Las costumbres hablan de la vida diaria, y las celebraciones y el arte muestran las fiestas y las obras de la época.",
    ],
    vocab=[("Colonia", "período en que Chile fue parte del imperio español, de 1541 a 1810"), ("Capitanía General", "territorio colonial con un gobernador, como la Capitanía General de Chile"), ("hacienda", "gran propiedad agrícola y ganadera"), ("dimensión", "aspecto de la vida que se estudia, como la sociedad o la economía"), ("frontera", "zona de límite entre dos territorios")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años duró la Colonia en Chile?", ["Busco los años: 1541 y 1810.", "Resto: 1810 − 1541 = 269."], "269 años"),
        ("Ubicar un lugar", "{F} ¿Qué había al sur del río Biobío?", ["Busco el Biobío en la ficha.", "La ficha dice que ahí estaba la frontera con el territorio mapuche."], "La frontera con el territorio mapuche"),
    ],
    mistakes=[("Pensar que la mayoría vivía en grandes ciudades.", "Se compara con el Chile de hoy.", "Recuerda que las ciudades eran pequeñas y la mayoría vivía en el campo."),
              ("Decir que la Colonia terminó en 1541.", "Se confunde el inicio con el final.", "Empezó en 1541 y terminó en 1810.")],
    T=[
        ("{F} ¿En qué año empezó la Colonia en Chile?", "en 1541", "Con la fundación de Santiago."),
        ("{F} ¿En qué año terminó la Colonia?", "en 1810", "Con la Primera Junta Nacional de Gobierno."),
        ("{F} ¿Cuál era la capital de la Capitanía General de Chile?", "Santiago", "La ficha lo dice."),
        ("=", "{F} Ejemplo: una familia llegó a una hacienda en 1700. ¿Cuántos años faltaban para 1810?", "1810-1700", "Se resta el año de llegada al final.", " años"),
        ("{F} ¿Entre qué dos lugares vivían sobre todo los españoles?", "entre La Serena y Chiloé", "La ficha lo dice."),
        ("{F} ¿Dónde vivía la mayoría de la gente: en el campo o en grandes ciudades?", "en el campo", "Las ciudades eran pequeñas."),
        ("{F} Nombra las cuatro dimensiones que vamos a estudiar.", "sociedad, oficios, costumbres, celebraciones y arte", "La ficha las enumera."),
        ("{F} Un mapa muestra un fuerte español al sur del Biobío. ¿Qué debe recordar quien lo mira?", "que ahí estaba la frontera con el territorio mapuche", "Es la zona de límite."),
        ("{F} ¿A qué dimensión pertenece cada pregunta? a) ¿en qué trabajaba la gente? b) ¿qué fiestas celebraban?", "a: oficios y actividades económicas; b: celebraciones y arte", "Cada pregunta corresponde a una dimensión distinta."),
        ("{F} Ana dice: «La Colonia duró 50 años». Corrígela con los años de la ficha.", "duró 269 años, de 1541 a 1810", "La resta es 1810 − 1541."),
        ("{F} Pedro dice: «Santiago era una ciudad enorme». ¿Qué dato de la ficha lo contradice?", "las ciudades eran pequeñas y la mayoría vivía en el campo", "La ficha describe ciudades pequeñas."),
        ("{F} ¿Qué hecho marca el inicio de la Colonia y cuál marca su final?", "inicio: la fundación de Santiago en 1541; final: la Primera Junta Nacional de Gobierno en 1810", "La ficha da esos dos hechos como límites del período."),
        ("{F} Clasifica en «tiempo» o «lugar»: a) Chiloé; b) 1810; c) Biobío; d) 1541.", "tiempo: b y d; lugar: a y c", "Los años son tiempo y los nombres de sitios son lugares."),
    ],
    ctx=("Un cartel en una casa antigua dice: «Casa colonial, siglo XVIII, Santiago». ¿Qué parte indica el tiempo y qué parte el lugar?", "tiempo: siglo XVIII; lugar: Santiago", "El siglo es tiempo y la ciudad es lugar."),
    sc=[("¿Qué fue la Colonia en Chile?", "el período en que Chile formó parte del imperio español, de 1541 a 1810", "Así se define en la clase."),
        ("{F} ¿Dónde estaba la frontera con el territorio mapuche?", "al sur del río Biobío", "La ficha lo dice."),
        ("Nombra dos dimensiones de la vida colonial.", "por ejemplo la sociedad y los oficios", "Son dimensiones de la ficha.")],
    op=("Dibuja una línea de tiempo con 1541 y 1810 como extremos y escribe «Colonia» en medio. Debajo dibuja un mapa simple de Chile con tres puntos: La Serena, Santiago y Chiloé, y una línea que marque el río Biobío con la palabra «frontera». {F}",
        "Línea con 1541 a la izquierda y 1810 a la derecha. Mapa con La Serena arriba, Santiago en medio, Chiloé abajo y una línea para el Biobío al sur de Santiago.",
        ["años en orden", "tres lugares de norte a sur", "frontera bien ubicada"], ["línea de tiempo", "mapa simple"], ["poner la frontera al norte de Santiago", "cambiar el orden de los años"],
        "Pide que explique en voz alta por qué la frontera estaba al sur."),
    reinforce="Cuenta en voz alta cuándo empezó y terminó la Colonia y cuáles son las cuatro dimensiones.",
    extend="Calcula cuántos años pasaron entre 1810 y el año en que naciste, y compara ese número con los 269 años que duró la Colonia.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre la vida colonial (hechas para este cuaderno, con ejemplos de textos). Fuente A, de un viajero extranjero del siglo XVIII: «Las casas de Santiago son de adobe y de un solo piso, con patios interiores; las calles son rectas y se cruzan en ángulo recto». "
     "Fuente B, inventario de una hacienda del siglo XVIII, hecho por un escribano: «300 vacas, 40 caballos, 6 carretas, una capilla, un molino y casas para los trabajadores». "
     "Fuente C, una pintura religiosa de la época colonial que muestra una Virgen con un vestido muy decorado, hecha por un pintor para una iglesia. "
     "Fuente D, un bando del cabildo de Santiago que ordena a los vecinos barrer sus calles antes de la procesión de una fiesta religiosa.")
build(
    OA5, 2, F,
    use="Aprenderé a leer fuentes sobre la vida colonial y a preguntar quién las hizo y para qué. Sirve para saber qué podemos afirmar sobre la vida cotidiana de la época.",
    prior=["Sé qué es la procedencia de una fuente.", "Sé ubicar la Colonia entre 1541 y 1810."],
    explain=[
        "Para conocer la vida colonial usamos fuentes de distintos tipos. La descripción de un viajero extranjero muestra cómo se veía Santiago desde afuera: casas de adobe de un piso, con patios, y calles rectas. Es una mirada de alguien que no vivía allí.",
        "El inventario de una hacienda lo hizo un escribano, que anotaba los bienes. Sirve para saber qué había: vacas, caballos, carretas, una capilla y un molino. Pero no cuenta cómo vivían los trabajadores. La pintura religiosa muestra el arte de la época y las creencias. El bando del cabildo muestra una orden para preparar una fiesta religiosa.",
        "Cada fuente aporta un dato y tiene límites. Un inventario no cuenta emociones y una pintura no cuenta cómo comían. Por eso se comparan varias fuentes. Una afirmación sobre la vida colonial debe apoyarse en una fuente que la muestre.",
    ],
    vocab=[("inventario", "lista de bienes de una persona o propiedad"), ("escribano", "persona que redactaba y certificaba documentos"), ("bando", "orden pública dictada por una autoridad"), ("adobe", "ladrillo grande hecho de barro y paja secado al sol"), ("procesión", "desfile religioso por las calles")],
    worked=[
        ("Leer una fuente", "{F} ¿Qué muestra la fuente A sobre las casas de Santiago?", ["Leo qué dice sobre las casas.", "Dice que eran de adobe y de un piso, con patios."], "Eran de adobe, de un piso y con patios"),
        ("Reconocer un límite", "{F} ¿La fuente B dice cómo vivían los trabajadores de la hacienda?", ["La fuente B enumera bienes.", "No cuenta su vida diaria."], "No, solo enumera bienes"),
    ],
    mistakes=[("Creer que un inventario muestra cómo se sentía la gente.", "Se pide a la fuente más de lo que dice.", "Usa cada fuente solo para lo que muestra."),
              ("Creer que el viajero conocía todo Chile.", "No se mira su procedencia.", "Anota que describe Santiago y mira desde afuera.")],
    T=[
        ("{F} ¿Quién hizo el inventario de la fuente B?", "un escribano", "La ficha lo dice."),
        ("{F} ¿De qué material eran las casas de Santiago según la fuente A?", "de adobe", "La fuente A lo dice."),
        ("{F} ¿Cuántas vacas tenía la hacienda de la fuente B?", "300", "El inventario lo anota."),
        ("{F} ¿Qué ordenaba el bando del cabildo?", "barrer las calles antes de una procesión", "La fuente D lo dice."),
        ("{F} ¿Qué fuente es una pintura?", "la fuente C", "La fuente C es la pintura religiosa."),
        ("=", "{F} Si la hacienda tenía 300 vacas y 40 caballos, ¿cuántos animales anota el inventario en total?", "300+40", "Se suman los dos grupos de animales.", " animales"),
        ("{F} Quieres saber cómo era una calle de Santiago. ¿Qué fuente usas?", "la fuente A", "Describe las calles."),
        ("{F} Quieres saber qué se preparaba para una fiesta religiosa. ¿Qué fuente usas?", "la fuente D", "Muestra una orden para la procesión."),
        ("{F} Quieres saber qué había en una hacienda. ¿Qué fuente usas?", "la fuente B", "Es un inventario de bienes."),
        ("{F} Luis dice: «La pintura prueba cómo se vestía toda la gente». ¿Qué problema tiene?", "muestra una imagen religiosa pintada, no la ropa de todos", "Una pintura religiosa tiene otro propósito."),
        ("{F} Ana dice: «El viajero describe Chile completo». ¿Qué dato de la ficha lo corrige?", "describe Santiago, no todo Chile", "La fuente solo habla de Santiago."),
        ("{F} Elige la pregunta que las fuentes no responden. A) ¿De qué eran las casas de Santiago? B) ¿Qué sentían los trabajadores de la hacienda?", "B", "Ningún dato de la ficha cuenta sus sentimientos."),
        ("{F} Para comparar cómo eran las casas de una ciudad con lo que había en una hacienda, ¿qué dos fuentes unes?", "la fuente A con la fuente B", "A habla de la ciudad y B de una hacienda."),
    ],
    ctx=("Un museo muestra un inventario con la nota: «Hacienda, siglo XVIII, escribano». ¿Qué datos de procedencia faltan en la nota?", "falta decir para qué se hizo y dónde estaba la hacienda", "La nota da época y autor, pero no el propósito ni el lugar."),
    sc=[("¿Qué es un inventario?", "una lista de bienes de una persona o propiedad", "Así se define en la clase."),
        ("{F} ¿Qué fuente muestra una orden de la autoridad?", "la fuente D", "El bando es una orden."),
        ("¿Por qué conviene comparar fuentes de distinto tipo?", "porque cada una muestra una parte distinta de la vida", "Así se completa la imagen.")],
    op=("Haz una tabla con las fuentes A, B, C y D. En las columnas escribe «qué tipo de fuente es», «qué muestra» y «qué no muestra». {F}",
        "A: descripción de viajero; muestra casas de adobe; no muestra la vida de los pobres. B: inventario; muestra bienes; no muestra cómo vivían los trabajadores.",
        ["cuatro filas completas", "tipo de fuente correcto", "un límite por fuente"], ["tabla de tres columnas"], ["decir que una fuente muestra todo", "mezclar las fuentes"],
        "Pregunta qué fuente nueva te gustaría tener para saber cómo comían las familias."),
    reinforce="Nombra las cuatro fuentes y di qué muestra cada una.",
    extend="Escribe qué fuentes dejaría tu casa dentro de 200 años para que alguien la estudiara.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (sociedad y economía, hecha para este cuaderno). Grupos sociales: los españoles nacidos en España (peninsulares) tenían los cargos más altos; los criollos eran hijos de españoles nacidos en América; los mestizos eran hijos de español e indígena; había indígenas y personas africanas o de origen africano, muchas esclavizadas. "
     "Los grupos con más riqueza y poder eran los españoles y los criollos dueños de haciendas. "
     "Actividades económicas: la agricultura y la ganadería en las haciendas, la minería del oro en lavaderos y el comercio. Se vendían al Perú trigo, sebo, cueros y charqui. "
     "Oficios: agricultores, mineros, arrieros, artesanos como plateros y carpinteros, comerciantes y sirvientes.")
build(
    OA5, 3, F,
    use="Aprenderé quiénes formaban la sociedad colonial y de qué trabajaban. Sirve para explicar por qué algunos grupos tenían más poder y riqueza que otros.",
    prior=["Sé ubicar la Colonia entre 1541 y 1810.", "Sé que había haciendas y minas."],
    explain=[
        "La sociedad colonial en Chile estaba organizada en grupos sociales con distinto poder. Los peninsulares, españoles nacidos en España, tenían los cargos más altos. Los criollos eran hijos de españoles nacidos en América. Los mestizos eran hijos de español e indígena. También había indígenas y personas africanas o de origen africano, muchas de ellas esclavizadas.",
        "Los grupos con más riqueza y poder eran los españoles y los criollos que tenían haciendas. La economía se basaba en la agricultura y la ganadería, en la minería del oro en lavaderos y en el comercio. Se vendían al Perú trigo, sebo, cueros y charqui, que es carne seca.",
        "Los oficios mostraban la posición social. Había agricultores, mineros, arrieros que llevaban mercancías en mulas, artesanos como plateros y carpinteros, comerciantes y sirvientes. Mucha gente trabajaba para dueños de haciendas. Relacionar el grupo social con el oficio ayuda a entender por qué la sociedad era desigual.",
    ],
    vocab=[("peninsular", "español nacido en España"), ("criollo", "hijo de españoles nacido en América"), ("arriero", "persona que lleva mercancías en mulas"), ("sebo", "grasa de animal usada para hacer velas y jabón"), ("charqui", "carne seca y salada que se conserva mucho tiempo")],
    worked=[
        ("Clasificar un grupo", "{F} ¿Cómo se llamaba un hijo de español e indígena?", ["Busco el término en la ficha.", "Se llamaba mestizo."], "Mestizo"),
        ("Relacionar economía y comercio", "{F} ¿Qué productos de las haciendas se vendían al Perú?", ["Reviso las actividades económicas.", "Se vendían trigo, sebo, cueros y charqui."], "Trigo, sebo, cueros y charqui"),
    ],
    mistakes=[("Confundir criollo con peninsular.", "Ambos son españoles, pero nacieron en lugares distintos.", "Peninsular nació en España; criollo nació en América."),
              ("Creer que todos los grupos tenían el mismo poder.", "Se olvida la desigualdad.", "Recuerda que los cargos más altos eran de peninsulares y los dueños de haciendas tenían más riqueza.")],
    T=[
        ("{F} ¿Cómo se llamaban los españoles nacidos en España?", "peninsulares", "La ficha lo dice."),
        ("{F} ¿Cómo se llamaban los hijos de españoles nacidos en América?", "criollos", "La ficha lo dice."),
        ("{F} ¿Qué es el charqui?", "carne seca y salada", "Así lo define el vocabulario."),
        ("{F} ¿Qué oficio llevaba mercancías en mulas?", "arriero", "Así lo describe el vocabulario."),
        ("{F} ¿Qué se extraía de los lavaderos?", "oro", "La ficha habla de minería del oro."),
        ("{F} ¿Qué grupo ocupaba los cargos más altos?", "los peninsulares", "La ficha lo dice."),
        ("{F} ¿Un platero era agricultor o artesano?", "artesano", "La ficha lista a los plateros entre los artesanos."),
        ("{F} Une cada término con su significado: 1) peninsular; 2) mestizo. a) hijo de español e indígena; b) español nacido en España.", "1 con b; 2 con a", "Así los define la ficha."),
        ("=", "{F} Ejemplo: una hacienda vendía al Perú 120 sacos de trigo y 80 sacos más al año siguiente. ¿Cuántos sacos vendió en total?", "120+80", "Se suman los sacos de los dos años.", " sacos"),
        ("{F} Pedro dice: «En la Colonia todos tenían el mismo poder». ¿Qué dato lo contradice?", "los cargos más altos eran de peninsulares y los dueños de haciendas tenían más riqueza", "La ficha muestra desigualdad."),
        ("{F} Ana dice: «Los criollos nacían en España». Corrígela.", "los criollos nacían en América, de padres españoles", "Esa es la definición de la ficha."),
        ("{F} Ordena la relación: a) los dueños de haciendas vendían productos al Perú; b) tenían más riqueza; c) se criaba ganado y se cultivaba trigo.", "c, a, b", "Primero se produce, luego se vende y se gana."),
        ("{F} Clasifica como «agricultura y ganadería» o «minería»: a) criar vacas; b) lavar arenas en busca de oro; c) cultivar trigo.", "agricultura y ganadería: a y c; minería: b", "El oro viene de la minería."),
    ],
    ctx=("En una obra de teatro escolar hay un arriero, un platero y una dueña de hacienda. Explica qué hace cada uno con la ficha.", "el arriero lleva mercancías en mulas; el platero es artesano; la dueña de hacienda tiene tierras y ganado", "Cada personaje corresponde a un oficio o grupo de la ficha."),
    sc=[("{F} ¿Qué es un criollo?", "un hijo de españoles nacido en América", "Así lo define la ficha."),
        ("Nombra tres oficios de la Colonia.", "por ejemplo agricultor, minero y platero", "Son oficios de la ficha."),
        ("{F} ¿Por qué se dice que la sociedad era desigual?", "porque unos grupos tenían más poder y riqueza que otros", "La ficha lo explica.")],
    op=("Dibuja cuatro recuadros con los grupos sociales: «peninsulares», «criollos», «mestizos» y «indígenas y africanos». Bajo «peninsulares» escribe qué cargos tenían y bajo «criollos» qué podían poseer, según la ficha. Aparte, escribe tres oficios de la ficha sin unirlos a ningún grupo, porque la ficha no dice quién hacía cada uno. {F}",
        "Peninsulares: los cargos más altos. Criollos: haciendas (los dueños tenían riqueza y poder). Oficios: arriero, platero, agricultor.",
        ["cuatro grupos nombrados", "un dato de poder o riqueza para peninsulares y criollos", "tres oficios de la ficha"], ["cuatro recuadros", "lista de oficios"], ["unir un oficio con un grupo sin dato en la ficha", "poner a los criollos como nacidos en España"],
        "Pregunta por qué la ficha no permite saber qué oficio tenía cada grupo y qué fuente haría falta."),
    reinforce="Nombra los grupos sociales y un oficio de cada uno en voz alta.",
    extend="Escribe una pregunta sobre la vida de un grupo social que no sale en la ficha, como las mujeres.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación, hecha para este cuaderno). Vida en la ciudad: una familia rica de Santiago vivía en una casa de adobe con varios patios y salas, tenía sirvientes, iba a misa y asistía a las fiestas religiosas con sus mejores ropas. "
     "Vida en el campo: en una hacienda vivían el dueño y sus trabajadores; los trabajadores vivían en ranchos pequeños, cultivaban, cuidaban animales y celebraban fiestas del santo del lugar. "
     "Arte y celebraciones: en las iglesias había imágenes religiosas talladas y pinturas. Las fiestas más importantes eran religiosas, como la Semana Santa y las fiestas de los santos patronos, con procesiones, música y comidas.")
build(
    OA5, 4, F,
    use="Aprenderé a comparar la vida en la ciudad y en el campo, y entre familias ricas y trabajadores, en la Colonia. Sirve para describir costumbres, arte y celebraciones.",
    prior=["Sé los grupos sociales de la Colonia.", "Sé de qué trabajaba la gente."],
    explain=[
        "Comparar la vida colonial nos permite ver parecidos y diferencias entre territorios y entre grupos. En la ciudad, una familia rica vivía en una casa de adobe con varios patios y salas, tenía sirvientes y asistía a misa y a fiestas religiosas con sus mejores ropas.",
        "En el campo, en una hacienda, vivían el dueño y sus trabajadores. Los trabajadores vivían en ranchos pequeños, cultivaban, cuidaban animales y celebraban las fiestas del santo del lugar. La diferencia entre la casa del dueño y los ranchos muestra la desigualdad.",
        "Hay también un parecido: en ambos lugares las fiestas religiosas eran muy importantes. Las más conocidas eran la Semana Santa y las fiestas de los santos patronos, con procesiones, música y comidas. En las iglesias había imágenes talladas y pinturas religiosas, parte del arte colonial.",
    ],
    vocab=[("rancho", "casa humilde de campo, hecha de materiales simples"), ("santo patrono", "santo protector de un lugar, al que se dedica una fiesta"), ("procesión", "desfile religioso con imágenes por las calles"), ("tallar", "dar forma a madera o piedra con herramientas"), ("misa", "ceremonia religiosa de la Iglesia católica")],
    worked=[
        ("Comparar dos lugares", "{F} ¿En qué se parecía la vida en la ciudad y en el campo?", ["Busco algo que ocurriera en ambos.", "En ambos las fiestas religiosas eran importantes."], "En que las fiestas religiosas eran importantes en ambos lugares"),
        ("Comparar dos grupos", "{F} ¿En qué se diferenciaba la vivienda del dueño y la de un trabajador de la hacienda?", ["El dueño vivía en casa grande.", "Los trabajadores vivían en ranchos pequeños."], "El dueño tenía casa grande y los trabajadores, ranchos pequeños"),
    ],
    mistakes=[("Creer que todos vivían en casas grandes.", "Se mira solo a las familias ricas.", "Recuerda los ranchos de los trabajadores."),
              ("Pensar que las fiestas eran solo para los ricos.", "Se ignoran las fiestas del campo.", "Las fiestas del santo del lugar se celebraban en las haciendas también.")],
    T=[
        ("{F} ¿De qué eran las casas de las familias ricas de Santiago?", "de adobe", "La ficha lo dice."),
        ("{F} ¿Dónde vivían los trabajadores de una hacienda?", "en ranchos pequeños", "La ficha lo dice."),
        ("{F} ¿Qué fiestas eran las más importantes?", "las religiosas", "La ficha lo dice."),
        ("{F} ¿Qué dos cosas acompañaban a las procesiones, además de las imágenes?", "música y comidas", "La ficha dice «con procesiones, música y comidas»."),
        ("{F} ¿Qué había en las iglesias como parte del arte colonial?", "imágenes talladas y pinturas religiosas", "La ficha lo dice."),
        ("{F} ¿Quién tenía sirvientes: la familia rica de Santiago o los trabajadores de la hacienda?", "la familia rica", "La ficha lo dice."),
        ("{F} Clasifica como «ciudad» o «campo»: a) casa con varios patios; b) rancho pequeño; c) fiesta del santo del lugar en una hacienda.", "ciudad: a; campo: b y c", "La ficha ubica cada elemento."),
        ("{F} Elige la comparación correcta. A) Las fiestas religiosas eran importantes en la ciudad y en el campo. B) Solo se celebraban fiestas en la ciudad.", "A", "La ficha describe fiestas en ambos."),
        ("{F} Elige quién asistía a misa con sus mejores ropas según la ficha: A) una familia rica; B) todos los esclavizados.", "A", "La ficha lo dice de la familia rica."),
        ("{F} Pedro dice: «Todos vivían igual en la Colonia». Da dos datos de la ficha que lo contradicen.", "la familia rica vivía en casa con patios y los trabajadores en ranchos pequeños", "La vivienda mostraba desigualdad."),
        ("{F} Ana dice: «El arte colonial era sobre fútbol». Corrígela con un dato.", "el arte colonial incluía imágenes religiosas talladas y pinturas en las iglesias", "Era sobre todo arte religioso."),
        ("{F} ¿Por qué se dice que la casa del dueño y los ranchos muestran desigualdad?", "porque unos vivían en casas grandes y otros en viviendas humildes", "La diferencia de vivienda refleja diferencia de riqueza."),
        ("{F} ¿Qué parecido une la vida de la ciudad y del campo?", "las fiestas religiosas con música y comidas", "La ficha destaca esas fiestas."),
    ],
    ctx=("Una compañera dibuja una procesión con música frente a una iglesia, con una imagen de un santo. ¿Qué dimensiones de la vida colonial muestra su dibujo?", "celebraciones y arte", "Hay una fiesta religiosa y una imagen religiosa."),
    sc=[("{F} ¿Quiénes celebraban en el campo las fiestas del santo del lugar?", "los trabajadores de la hacienda", "La ficha lo dice de los trabajadores de la hacienda."),
        ("¿Qué es una procesión?", "un desfile religioso con imágenes por las calles", "Así se define en la clase."),
        ("¿Para qué sirve comparar la ciudad y el campo?", "para ver parecidos y diferencias en la vida de la época", "Así se entiende mejor la sociedad.")],
    op=("Haz un cuadro de dos columnas, «ciudad» y «campo», con tres filas: «vivienda», «trabajo o actividades» y «fiestas». Completa con datos de la ficha. Escribe debajo una frase que empiece con «Un parecido es…» y otra con «Una diferencia es…». {F}",
        "Vivienda: casa de adobe con patios / rancho pequeño. Fiestas: fiestas religiosas en ambos. Un parecido es que ambos celebraban. Una diferencia es la vivienda.",
        ["cuadro completo", "un parecido", "una diferencia"], ["cuadro de dos columnas", "dos frases"], ["dejar filas vacías", "inventar datos"],
        "Pregunta qué fila muestra más desigualdad."),
    reinforce="Cuenta en voz alta tres diferencias y un parecido entre la ciudad y el campo.",
    extend="Escribe una fiesta o costumbre que se celebre hoy en tu región y que tenga origen religioso, si conoces alguna.",
)

# ================================================================ OA 06 · DEPENDENCIA COLONIAL, IGLESIA Y SOCIEDAD MESTIZA
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (el imperio español, hecha para este cuaderno). España era la metrópoli, es decir, el país que gobernaba las colonias. En América el rey nombró virreyes, que gobernaban en su nombre grandes territorios llamados virreinatos. "
     "El Virreinato de Nueva España se creó en 1535, con capital en la ciudad de México, y el Virreinato del Perú en 1542, con capital en Lima. "
     "Chile era una Capitanía General, con un gobernador en Santiago, y dependía del Virreinato del Perú en muchos asuntos. Las colonias enviaban a España metales y productos, y la metrópoli decidía las leyes y los impuestos.")
build(
    OA6, 1, F,
    use="Aprenderé cómo se organizaba el imperio español y dónde estaba Chile dentro de él. Sirve para entender qué significa que una colonia dependa de una metrópoli.",
    prior=["Sé que Chile fue colonia española entre 1541 y 1810.", "Sé que la Corona era el rey y su gobierno."],
    explain=[
        "Una colonia es un territorio gobernado por otro país, llamado metrópoli. España era la metrópoli de sus colonias americanas. El rey no podía gobernar desde lejos todos los territorios, así que nombraba autoridades que lo representaban.",
        "Los virreyes gobernaban grandes territorios llamados virreinatos. El Virreinato de Nueva España se creó en 1535, con capital en la ciudad de México. El Virreinato del Perú se creó en 1542, con capital en Lima. Chile era una Capitanía General, con un gobernador en Santiago, y en muchos asuntos dependía del Virreinato del Perú.",
        "Dependencia significa que las decisiones importantes se tomaban en España o en el virreinato, no en la colonia. Las colonias enviaban metales y productos a España, y la metrópoli dictaba las leyes y los impuestos. Para ubicar este sistema, miramos quién gobernaba y desde dónde.",
    ],
    vocab=[("metrópoli", "país que gobierna colonias"), ("virrey", "autoridad que gobernaba un virreinato en nombre del rey"), ("virreinato", "gran territorio colonial gobernado por un virrey"), ("impuesto", "dinero que se paga a la autoridad"), ("dependencia", "situación en que otra persona o país toma las decisiones importantes")],
    worked=[
        ("Ubicar una autoridad", "{F} ¿Dónde estaba la capital del Virreinato del Perú?", ["Busco el virreinato en la ficha.", "La capital era Lima."], "En Lima"),
        ("Calcular una diferencia de años", "{F} ¿Cuántos años pasaron entre la creación del Virreinato de Nueva España y la del Perú?", ["Busco los años: 1535 y 1542.", "Resto: 1542 − 1535 = 7."], "7 años"),
    ],
    mistakes=[("Decir que Chile era un virreinato.", "Se confunde Capitanía General con virreinato.", "Chile era una Capitanía General que dependía del Virreinato del Perú."),
              ("Decir que las leyes las dictaba el gobernador de Chile solo.", "Se olvida la dependencia.", "Las leyes y los impuestos los decidía la metrópoli.")],
    T=[
        ("{F} ¿Cuál era la metrópoli de Chile?", "España", "La ficha lo dice."),
        ("{F} ¿Cómo se llamaba la autoridad que gobernaba un virreinato?", "virrey", "La ficha lo dice."),
        ("{F} ¿Qué ciudad era capital del Virreinato de Nueva España?", "la ciudad de México", "La ficha lo dice."),
        ("=", "{F} Una orden del rey llegó a Lima en 1600. ¿Cuántos años habían pasado desde la creación del Virreinato del Perú?", "1600-1542", "Se resta el año de creación al año de la orden.", " años"),
        ("{F} ¿Cómo se llamaba la autoridad de Chile y dónde estaba?", "gobernador, en Santiago", "La ficha lo dice."),
        ("{F} ¿Qué decidía la metrópoli?", "las leyes y los impuestos", "La ficha lo dice."),
        ("{F} ¿Chile dependía de qué virreinato en muchos asuntos?", "del Virreinato del Perú", "La ficha lo dice."),
        ("{F} Elige la frase correcta. A) Chile era un virreinato. B) Chile era una Capitanía General.", "B", "La ficha lo dice."),
        ("{F} Un mapa muestra una flecha de Santiago a Lima y otra de Lima a España. ¿Qué dependencia muestra?", "que Chile dependía del Perú, y este de España", "Las flechas siguen la cadena de autoridad."),
        ("{F} Pedro dice: «En Chile se decidían todas las leyes». Corrígelo.", "la metrópoli, España, dictaba las leyes y los impuestos", "La ficha lo dice."),
        ("{F} Ana dice: «Los virreyes eran elegidos por los vecinos». ¿Qué dato de la ficha la corrige?", "el rey los nombraba para gobernar en su nombre", "No eran elegidos por vecinos."),
        ("{F} Ordena de la autoridad más alta a la más baja para Chile: gobernador, rey, virrey del Perú.", "rey, virrey del Perú, gobernador", "La cadena baja desde el rey."),
        ("{F} Clasifica en «metrópoli» o «colonia»: a) España; b) Chile; c) Nueva España.", "metrópoli: a; colonia: b y c", "Los otros dos eran territorios gobernados desde España."),
    ],
    ctx=("En un museo, un cartel dice: «Real orden del rey de España al virrey del Perú, 1600». ¿Qué cadena de autoridad aparece y qué muestra de dependencia?", "rey de España y virrey del Perú; las decisiones venían de la metrópoli", "La orden baja del rey al virrey."),
    sc=[("¿Qué es una metrópoli?", "un país que gobierna colonias", "Así se define en la clase."),
        ("{F} ¿En qué año se creó el Virreinato del Perú?", "1542", "La ficha lo dice."),
        ("¿Qué significa que una colonia dependa de la metrópoli?", "que las decisiones importantes se toman fuera de la colonia", "Esa es la dependencia.")],
    op=("Dibuja un esquema con tres recuadros unidos por flechas hacia abajo: «Rey de España», «Virrey del Perú» y «Gobernador de Chile». A un lado, escribe una cosa que decidía la metrópoli. Dibuja también una línea de tiempo con 1535, 1541 y 1542. {F}",
        "Rey → virrey → gobernador. Decidía las leyes y los impuestos. Línea con 1535, 1541, 1542.",
        ["tres autoridades en orden", "una decisión de la metrópoli", "años en orden"], ["esquema de tres recuadros", "línea de tiempo"], ["poner al gobernador sobre el rey", "olvidar la dependencia"],
        "Pregunta qué problemas podía tener que las leyes se decidieran lejos."),
    reinforce="Explica en voz alta qué significa metrópoli, virrey y capitanía general.",
    extend="Calcula cuántos años pasaron entre la creación del Virreinato de Nueva España (1535) y la fundación de Santiago (1541), y cuántos entre esa fundación y la creación del Virreinato del Perú (1542).",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre la Colonia (hechas para este cuaderno, con ejemplos de textos). Fuente A, una real cédula, es decir, una orden del rey, del siglo XVI: «Los barcos de las colonias deberán comerciar solo con España y con puertos autorizados». "
     "Fuente B, una partida de bautismo escrita por un cura de una parroquia, siglo XVIII: «Se bautizó a María, hija de un español y de una mujer indígena». "
     "Fuente C, un informe de un misionero jesuita al rey, siglo XVII, donde cuenta que enseña a leer y rezar en una misión. "
     "Fuente D, una pintura de castas del siglo XVIII, que muestra familias con padres de orígenes distintos y sus hijos, con rótulos escritos por el pintor.")
build(
    OA6, 2, F,
    use="Aprenderé a leer fuentes sobre el comercio colonial, la Iglesia y el mestizaje, y a preguntar quién las hizo. Sirve para ver qué puede probar cada una.",
    prior=["Sé qué es una metrópoli y un virrey.", "Sé preguntar la procedencia de una fuente."],
    explain=[
        "La historia colonial se conoce por fuentes de varios tipos. Una real cédula es una orden del rey. Muestra lo que el rey quería, pero no prueba que siempre se cumpliera. La fuente A ordena que los barcos comercien solo con España y con puertos autorizados, lo que muestra la dependencia de las colonias.",
        "Una partida de bautismo la escribía un cura y anotaba a la persona bautizada y a sus padres. La fuente B registra a una niña hija de un español y de una mujer indígena, un ejemplo de mestizaje. El informe del misionero muestra el trabajo de la Iglesia: enseñar a leer y rezar. Pero lo escribe el mismo misionero, y cuenta su versión.",
        "La pintura de castas la hizo un pintor en el siglo XVIII y clasifica a las familias. Muestra cómo la sociedad miraba el mestizaje y los grupos, no cómo se sentían las personas. Una fuente sola no basta; las comparamos y decimos qué no muestran.",
    ],
    vocab=[("real cédula", "orden escrita del rey"), ("partida de bautismo", "registro escrito del bautismo de una persona y sus padres"), ("misión", "lugar donde misioneros enseñaban el cristianismo y otras cosas"), ("castas", "palabra colonial para clasificar a las personas según su origen"), ("parroquia", "iglesia local con su cura y sus fieles")],
    worked=[
        ("Leer una orden", "{F} ¿Qué ordena la fuente A?", ["Leo la orden del rey.", "Que los barcos comercien solo con España y puertos autorizados."], "Comerciar solo con España y con puertos autorizados"),
        ("Reconocer un límite", "{F} ¿La fuente A prueba que todos los barcos cumplían la orden?", ["Una orden dice lo que el rey quería.", "No muestra cómo se actuó."], "No, solo muestra lo que el rey quería"),
    ],
    mistakes=[("Creer que una orden del rey siempre se cumplía.", "Se confunde norma con práctica.", "Busca otra fuente que muestre qué ocurrió."),
              ("Creer que una pintura muestra sentimientos de las personas.", "Se piensa que dice más de lo que muestra.", "Recuerda que solo muestra cómo el pintor clasificaba a las familias.")],
    T=[
        ("{F} ¿Quién escribió la fuente B?", "un cura de una parroquia", "La ficha lo dice."),
        ("{F} ¿Qué es una real cédula?", "una orden escrita del rey", "La ficha lo dice."),
        ("{F} ¿A quién escribió el informe el misionero de la fuente C?", "al rey", "La ficha lo dice."),
        ("{F} ¿Qué enseñaba el misionero en su misión?", "a leer y rezar", "La fuente C lo dice."),
        ("{F} ¿Qué fuente es una pintura?", "la fuente D", "Es la pintura de castas."),
        ("{F} ¿De quién era hija María, según la fuente B?", "de un español y de una mujer indígena", "La partida lo dice."),
        ("{F} Quieres conocer cómo se mezclaban los grupos en una familia. ¿Qué fuente usas?", "la fuente B", "Registra a una hija de padres de orígenes distintos."),
        ("{F} Quieres saber cómo se limitaba el comercio de las colonias. ¿Qué fuente usas?", "la fuente A", "Es la orden del rey sobre el comercio."),
        ("{F} Quieres saber qué hacía la Iglesia en una misión. ¿Qué fuente usas?", "la fuente C", "Es el informe del misionero."),
        ("{F} Luis dice: «Como lo ordenó el rey, nadie comerciaba con otros puertos». ¿Qué problema tiene?", "una orden no prueba que se cumpliera", "Falta otra fuente que muestre qué ocurrió."),
        ("{F} Ana dice: «El misionero cuenta su trabajo con total objetividad». ¿Qué pregunta de procedencia falta?", "para qué lo escribió: para informar al rey y mostrar su labor", "Quien informa suele destacar lo que hizo."),
        ("{F} Elige la pregunta que las fuentes no responden. A) ¿Qué ordenaba el rey sobre el comercio? B) ¿Cuántas personas mestizas había en Chile en 1750?", "B", "Ninguna fuente da esa cifra."),
        ("{F} Para saber qué ordenaba el rey y qué sabemos de una familia mestiza, ¿qué dos fuentes unes?", "la fuente A con la fuente B", "A es la orden del rey y B registra a una hija de padres de orígenes distintos."),
    ],
    ctx=("En una exposición hay una copia de una partida de bautismo con el cartel «Siglo XVIII, parroquia, cura». ¿Qué datos de procedencia entrega y qué falta?", "entrega época, lugar y autor; falta el propósito", "Una partida se escribía para registrar un bautismo."),
    sc=[("{F} ¿Qué tres preguntas hacemos a una fuente?", "quién la hizo, cuándo y para qué", "Con ellas medimos lo que aporta."),
        ("{F} ¿Qué muestra la pintura de castas?", "cómo el pintor clasificaba a las familias según su origen", "La ficha lo describe."),
        ("¿Por qué una ley o una orden no basta para conocer la realidad?", "porque muestra lo que se quería, no necesariamente lo que ocurría", "La norma y la práctica pueden diferir.")],
    op=("Haz una tabla con las fuentes A, B y C. En las columnas escribe «quién la hizo», «para qué» y «qué muestra de la Colonia». {F}",
        "A: el rey; para ordenar el comercio; muestra la dependencia. B: un cura; para registrar un bautismo; muestra mestizaje. C: un misionero; para informar; muestra la labor de la Iglesia.",
        ["tres filas completas", "autor y propósito correctos", "tema de la Colonia identificado"], ["tabla de tres columnas"], ["mezclar autores", "creer que una orden se cumplía siempre"],
        "Pregunta qué fuente le sirve para el tema de la Iglesia y cuál para el mestizaje."),
    reinforce="Nombra las cuatro fuentes y qué tema muestra cada una.",
    extend="Escribe una regla de tu colegio que no siempre se cumple, y qué otra fuente usarías para saber si se cumple.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (causas y consecuencias, hecha para este cuaderno). Dependencia: España ordenaba que las colonias comerciaran solo con la metrópoli, y cobraba impuestos. Los productos europeos llegaban pocos y caros, y algunos comerciantes practicaban el contrabando, que es comerciar sin permiso. "
     "Iglesia: los curas y frailes celebraban misas, bautizos y matrimonios, y los anotaban en registros; fundaron parroquias, conventos y misiones; muchas veces dirigían escuelas y hospitales y enseñaban el cristianismo, también a indígenas y mestizos. "
     "Mestizaje: al comienzo llegaron pocas mujeres españolas, y hubo uniones entre españoles y mujeres indígenas. Sus hijos fueron mestizos. Con el tiempo los mestizos fueron cada vez más numerosos y formaron una sociedad mestiza.")
build(
    OA6, 3, F,
    use="Aprenderé por qué la dependencia, la Iglesia y el mestizaje fueron aspectos centrales de la Colonia y qué consecuencias tuvieron. Sirve para explicar la Colonia con causas y efectos.",
    prior=["Sé qué es una metrópoli.", "Sé quiénes eran los mestizos."],
    explain=[
        "Un aspecto central de la Colonia fue la dependencia. España ordenaba que las colonias comerciaran solo con ella, y cobraba impuestos. La consecuencia fue que los productos europeos llegaban pocos y caros, y algunos comerciantes practicaban el contrabando, es decir, comerciaban sin permiso.",
        "Otro aspecto fue el rol de la Iglesia católica. Los curas y frailes celebraban misas, bautizos y matrimonios y los anotaban en registros, fundaron parroquias, conventos y misiones, y muchas veces dirigían escuelas y hospitales. También enseñaban el cristianismo a indígenas y mestizos. La Iglesia fue una institución muy importante en la vida diaria.",
        "El tercer aspecto fue el surgimiento de una sociedad mestiza. Al comienzo llegaron pocas mujeres españolas, y hubo uniones entre españoles y mujeres indígenas. Sus hijos fueron mestizos. Con el tiempo los mestizos fueron cada vez más numerosos y formaron la mayor parte de la población. Así nació una sociedad con raíces españolas e indígenas.",
    ],
    vocab=[("contrabando", "comercio hecho sin permiso de la autoridad"), ("convento", "casa de frailes o monjas"), ("misión", "lugar de enseñanza y evangelización"), ("matrimonio", "unión de dos personas registrada por la Iglesia"), ("mestizaje", "mezcla de personas y culturas de orígenes distintos")],
    worked=[
        ("Causa y consecuencia", "{F} Si España obligaba a comerciar solo con ella, ¿qué consecuencia tuvo para los productos europeos?", ["Busco el efecto en la ficha.", "Llegaban pocos y caros."], "Llegaban pocos y caros"),
        ("Explicar el mestizaje", "{F} ¿Por qué hubo uniones entre españoles y mujeres indígenas?", ["Busco la razón al comienzo de la Colonia.", "Llegaron pocas mujeres españolas."], "Porque al comienzo llegaron pocas mujeres españolas"),
    ],
    mistakes=[("Pensar que la Iglesia solo celebraba misas.", "Se ignoran sus otras funciones.", "Recuerda las escuelas, hospitales, misiones y registros."),
              ("Creer que la sociedad mestiza apareció de repente.", "Se olvida el proceso.", "Se formó de a poco con muchas uniones y generaciones.")],
    T=[
        ("{F} ¿Qué es el contrabando?", "comerciar sin permiso", "La ficha lo define."),
        ("{F} ¿Qué cobraba España a las colonias?", "impuestos", "La ficha lo dice."),
        ("{F} ¿Qué dirigían muchas veces los curas y frailes además de las misas?", "escuelas y hospitales", "La ficha lo dice."),
        ("{F} ¿Cómo se llamaba la persona hija de español e indígena?", "mestiza", "La ficha lo dice."),
        ("{F} ¿Qué faltaba al comienzo de la Colonia: mujeres españolas o hombres españoles?", "mujeres españolas", "La ficha dice que llegaron pocas."),
        ("{F} ¿Qué enseñaba la Iglesia a indígenas y mestizos?", "el cristianismo", "La ficha lo dice."),
        ("{F} Clasifica como «causa» o «consecuencia»: a) España ordenó comerciar solo con ella; b) hubo contrabando.", "a: causa; b: consecuencia", "La orden produce el contrabando."),
        ("{F} ¿Qué actor cumplía cada función? 1) llevar la mercancía sin permiso; 2) celebrar bautizos. a) un comerciante; b) un cura.", "1 con a; 2 con b", "Cada función corresponde a ese actor."),
        ("{F} Elige la cadena correcta. A) pocas mujeres españolas → uniones con mujeres indígenas → hijos mestizos. B) hijos mestizos → pocas mujeres españolas.", "A", "La causa va antes de la consecuencia."),
        ("{F} Pedro dice: «El contrabando ocurría porque a los comerciantes les gustaba el peligro». Da una causa mejor con la ficha.", "los productos llegaban pocos y caros por la orden de comerciar solo con España", "La ficha da causas económicas."),
        ("{F} Ana dice: «La Iglesia no tuvo importancia en la vida diaria». Da dos datos que la contradicen.", "celebraba bautizos y matrimonios y dirigía escuelas y hospitales", "La ficha muestra su presencia en la vida diaria."),
        ("{F} Mateo dice: «En la Colonia había muy pocos mestizos». Corrígelo con la ficha.", "con el tiempo los mestizos fueron cada vez más numerosos", "La ficha lo dice."),
        ("{F} ¿Qué relación hay entre la Iglesia y los registros de bautizos y matrimonios?", "la Iglesia los celebraba y los anotaba, por eso hoy sirven como fuentes", "Esos registros permiten conocer a la población."),
    ],
    ctx=("Una compañera cuenta: «Mi bisabuela dice que en su pueblo el cura hacía clases y atendía enfermos». ¿Con qué función de la Iglesia de la ficha se relaciona?", "con las escuelas y los hospitales", "La ficha dice que muchas veces los dirigían."),
    sc=[("{F} ¿Qué significa mestizaje?", "mezcla de personas y culturas de orígenes distintos", "Así se define en la clase."),
        ("Nombra dos instituciones fundadas por la Iglesia en la Colonia.", "por ejemplo parroquias y conventos", "La ficha las nombra."),
        ("{F} ¿Qué consecuencia tuvo la orden de comerciar solo con España?", "productos europeos pocos y caros, y contrabando", "La ficha lo explica.")],
    op=("Dibuja tres esquemas cortos. En el primero, escribe una causa y una consecuencia de la dependencia. En el segundo, tres funciones de la Iglesia. En el tercero, la cadena que llevó a la sociedad mestiza. Usa solo la ficha. {F}",
        "Dependencia: comerciar solo con España → productos caros y contrabando. Iglesia: misas, escuelas, hospitales. Mestizaje: pocas mujeres españolas → uniones → hijos mestizos → sociedad mestiza.",
        ["tres esquemas", "causas y consecuencias bien ordenadas", "tres funciones de la Iglesia"], ["tres esquemas"], ["invertir causa y consecuencia", "olvidar una función de la Iglesia"],
        "Pregunta cuál de los tres aspectos influyó más en la vida diaria y por qué."),
    reinforce="Explica en voz alta un efecto de la dependencia, una función de la Iglesia y cómo surgió la sociedad mestiza.",
    extend="Escribe una pregunta sobre la Iglesia colonial que quisieras investigar con una fuente.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación, hecha para este cuaderno). Perú: sede de un virreinato, con una capital, Lima, grande y rica para su época; recibía plata de minas y tenía universidad y muchas iglesias. "
     "Chile: era una Capitanía General alejada del centro del imperio, con pocas ciudades, una frontera de guerra al sur del Biobío y menos riqueza en metales; dependía del Perú para muchos asuntos. "
     "Perspectivas sobre la Iglesia: un misionero decía que su obra era salvar almas y educar; un indígena que vivía en una misión podía valorar las clases pero lamentar la pérdida de sus costumbres. "
     "Perspectivas sobre el mestizaje: algunos grupos de poder valoraban más a los peninsulares y criollos; los mestizos formaban una parte creciente de la población.")
build(
    OA6, 4, F,
    use="Aprenderé a comparar Perú y Chile como territorios coloniales, y a comparar perspectivas sobre la Iglesia y el mestizaje. Sirve para explicar mejor la dependencia y la sociedad mestiza.",
    prior=["Sé qué es un virreinato y una capitanía general.", "Sé las funciones de la Iglesia."],
    explain=[
        "Comparar territorios muestra diferencias de poder. El Perú era sede de un virreinato. Su capital, Lima, era grande y rica para su época, recibía plata de las minas y tenía universidad y muchas iglesias. Chile era una Capitanía General alejada del centro del imperio, con pocas ciudades, una frontera de guerra al sur del Biobío y menos riqueza en metales.",
        "Por eso Chile dependía del Perú en muchos asuntos. Comparar ayuda a entender que dependencia significa que unos territorios tenían más poder que otros dentro del imperio.",
        "También comparamos perspectivas. Un misionero pensaba que su obra era salvar almas y educar. Un indígena en una misión podía valorar las clases pero lamentar la pérdida de sus costumbres. Sobre el mestizaje, algunos grupos de poder valoraban más a peninsulares y criollos, aunque los mestizos eran una parte creciente de la población. Una misma realidad se ve distinta desde cada lugar.",
    ],
    vocab=[("sede", "lugar donde está la autoridad principal"), ("perspectiva", "punto de vista de una persona o grupo"), ("universidad", "institución de estudios superiores"), ("salvar almas", "expresión religiosa de la época para convertir al cristianismo"), ("periferia", "zona alejada del centro del poder")],
    worked=[
        ("Comparar territorios", "{F} ¿En qué se diferenciaban Lima y Chile en riqueza?", ["Lima era grande y rica para su época.", "Chile tenía menos riqueza en metales."], "Lima era más rica; Chile tenía menos riqueza en metales"),
        ("Comparar perspectivas", "{F} ¿Cómo podía valorar la misión un indígena según la ficha?", ["Podía valorar las clases.", "Pero lamentar la pérdida de sus costumbres."], "Valorar las clases y lamentar la pérdida de sus costumbres"),
    ],
    mistakes=[("Pensar que Chile y el Perú eran igual de ricos.", "Se ignora la diferencia de poder.", "El Perú era sede de virreinato; Chile, una capitanía alejada."),
              ("Creer que todos veían la misión de la misma manera.", "Se supone una sola perspectiva.", "Incluye la mirada del misionero y la del indígena.")],
    T=[
        ("{F} ¿Cuál era la capital del Perú colonial?", "Lima", "La ficha lo dice."),
        ("{F} ¿Qué tenía Lima además de iglesias?", "universidad", "La ficha lo dice."),
        ("{F} ¿Qué había al sur del Biobío?", "una frontera de guerra", "La ficha lo dice."),
        ("{F} ¿De qué dependía Chile para muchos asuntos?", "del Perú", "La ficha lo dice."),
        ("{F} ¿Qué pensaba un misionero sobre su obra?", "que era salvar almas y educar", "La ficha lo dice."),
        ("{F} ¿Qué podía lamentar un indígena de una misión?", "la pérdida de sus costumbres", "La ficha lo dice."),
        ("{F} Elige la comparación correcta. A) Lima recibía plata de minas y Chile tenía menos metales. B) Chile era más rico que Lima.", "A", "La ficha lo dice."),
        ("{F} Clasifica como «Perú» o «Chile»: a) sede de un virreinato; b) frontera de guerra al sur del Biobío; c) plata de minas.", "Perú: a y c; Chile: b", "Cada dato corresponde a un territorio."),
        ("{F} Elige quién habla desde la mirada de la Iglesia: A) un misionero que quiere educar; B) un indígena que lamenta perder sus costumbres.", "A", "El misionero habla desde la Iglesia."),
        ("{F} Pedro dice: «Chile y el Perú eran iguales en poder». Da dos datos de la ficha que lo contradicen.", "Lima era sede de virreinato y rica; Chile estaba alejado, con frontera de guerra y menos metales", "Las diferencias muestran la dependencia."),
        ("{F} Ana dice: «Los mestizos eran muy pocos». Corrígela con la ficha.", "formaban una parte creciente de la población", "La ficha lo dice."),
        ("{F} ¿Por qué se dice que Chile era una periferia del imperio?", "porque estaba alejado del centro del poder y era menos rico", "La ficha lo describe así."),
        ("{F} ¿Qué dos perspectivas diferentes sobre la misión aparecen en la ficha y qué tienen en común?", "la del misionero y la del indígena; ambos valoran la educación aunque uno lamenta pérdidas", "Hay valoración y crítica."),
    ],
    ctx=("En un libro de texto hay dos cuadros: «Lima, siglo XVII» y «Santiago, siglo XVII». ¿Qué diferencia general esperas ver, según la ficha?", "Lima más grande y rica; Santiago más pequeña y con menos riqueza", "La ficha compara ambos."),
    sc=[("¿Qué es una perspectiva?", "el punto de vista de una persona o grupo sobre un hecho", "Así se define."),
        ("{F} ¿Cuál era más rico en metales: Chile o el Perú?", "el Perú", "La ficha dice que Chile tenía menos."),
        ("¿Por qué conviene comparar territorios coloniales?", "para entender que unos tenían más poder que otros dentro del imperio", "Así se explica la dependencia.")],
    op=("Haz una tabla de dos columnas, «Perú» y «Chile», con tres filas: «poder», «riqueza» y «situación en el territorio». Completa con datos de la ficha. Luego escribe dos frases: una de un misionero y otra de un indígena de una misión sobre la educación. {F}",
        "Perú: sede de virreinato, riqueza en plata, capital grande. Chile: capitanía, menos metales, frontera de guerra. Misionero: la educación salva almas. Indígena: valoro las clases pero pierdo mis costumbres.",
        ["tabla completa", "dos perspectivas", "datos de la ficha"], ["tabla", "dos frases"], ["inventar datos", "dar la misma opinión a los dos"],
        "Pregunta qué relación hay entre la riqueza de un territorio y su poder."),
    reinforce="Cuenta en voz alta tres diferencias entre Perú y Chile.",
    extend="Escribe una pregunta sobre cómo pudo sentirse un mestizo ante los grupos de poder, sin inventar la respuesta.",
)
