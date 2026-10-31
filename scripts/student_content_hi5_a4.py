"""Material del estudiante de 5.º básico, Historia, Geografía y Ciencias Sociales: OA 07 (relaciones hispano-mapuche) y OA 08 (patrimonio colonial)."""
from __future__ import annotations

from hi5_lib import build

OA7 = "HI05 OA 07"
OA8 = "HI05 OA 08"

# ================================================================ OA 07 · RELACIONES HISPANO-MAPUCHE
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (cronología y lugares, hecha para este cuaderno). 1550: la guerra entre españoles y mapuche se extiende al sur del río Biobío; Valdivia había fundado Concepción ese año. "
     "1553: Valdivia muere en la batalla de Tucapel. 1598: los mapuche vencen a los españoles en Curalaba y muere el gobernador Martín García Óñez de Loyola; después varias ciudades al sur del Biobío fueron abandonadas o destruidas. "
     "1608: una real cédula autoriza esclavizar a los mapuche capturados en guerra. 1641: se realiza el Parlamento de Quilín, una reunión de paz entre autoridades españolas y caciques mapuche. 1683: el rey pone fin a esa esclavitud. "
     "Durante gran parte de la Colonia, el río Biobío fue la frontera entre el territorio español y el territorio mapuche.")
build(
    OA7, 1, F,
    use="Aprenderé cuándo y dónde se desarrollaron las relaciones entre españoles y mapuche en la Colonia. Sirve para ubicar la guerra, la esclavitud y los parlamentos en el tiempo y el territorio.",
    prior=["Sé que los mapuche vivían en el centro y sur de Chile.", "Sé que los españoles fundaron ciudades desde 1541.", "Sé calcular años entre dos fechas."],
    explain=[
        "Las relaciones entre españoles y mapuche duraron toda la Colonia y fueron de varios tipos: guerra, trabajo forzado, comercio, evangelización y acuerdos. Para ubicarlas, primero miramos el tiempo y el lugar.",
        "La guerra se extendió al sur del río Biobío desde 1550. En 1553 murió Valdivia en la batalla de Tucapel. En 1598, los mapuche vencieron en Curalaba y murió el gobernador Martín García Óñez de Loyola. Después, varias ciudades al sur del Biobío fueron abandonadas o destruidas. Fue una muestra de la resistencia mapuche.",
        "En 1608 una real cédula autorizó esclavizar a los mapuche capturados en guerra. En 1641 se realizó el Parlamento de Quilín, una reunión de paz entre autoridades españolas y caciques mapuche. En 1683 el rey puso fin a esa esclavitud. Durante gran parte de la Colonia, el río Biobío fue la frontera entre ambos territorios.",
    ],
    vocab=[("resistencia", "oposición de un pueblo a un poder que quiere dominarlo"), ("frontera", "zona de límite entre dos territorios"), ("parlamento", "reunión entre autoridades españolas y caciques mapuche para acordar paz y otros temas"), ("cacique", "jefe de una comunidad indígena"), ("real cédula", "orden escrita del rey")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre la muerte de Valdivia y la batalla de Curalaba?", ["Busco los años: 1553 y 1598.", "Resto: 1598 − 1553 = 45."], "45 años"),
        ("Ubicar la frontera", "{F} ¿Qué río era la frontera entre el territorio español y el mapuche?", ["Busco la frontera en la ficha.", "Era el río Biobío."], "El río Biobío"),
    ],
    mistakes=[("Decir que Valdivia murió en Curalaba.", "Se mezclan dos batallas.", "Valdivia murió en Tucapel en 1553; Curalaba fue en 1598."),
              ("Creer que solo hubo guerra.", "Se olvidan los parlamentos.", "Recuerda el Parlamento de Quilín y otras formas de relación.")],
    T=[
        ("{F} ¿En qué año se realizó el Parlamento de Quilín?", "en 1641", "La ficha lo dice."),
        ("{F} ¿Qué río era la frontera?", "el Biobío", "La ficha lo dice."),
        ("{F} ¿Dónde murió Valdivia?", "en la batalla de Tucapel", "La ficha lo dice."),
        ("=", "{F} Una real cédula autorizó esclavizar mapuche en 1608 y el rey terminó esa esclavitud en 1683. ¿Cuántos años pasaron?", "1683-1608", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué gobernador murió en Curalaba?", "Martín García Óñez de Loyola", "La ficha lo dice."),
        ("{F} ¿Quién ganó en Curalaba: los mapuche o los españoles?", "los mapuche", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre Curalaba (1598) y el Parlamento de Quilín (1641)?", "1641-1598", "Se resta el año menor al mayor.", " años"),
        ("Ordena de más antiguo a más reciente: Parlamento de Quilín, Curalaba, muerte de Valdivia, fin de la esclavitud.", "muerte de Valdivia, Curalaba, Parlamento de Quilín, fin de la esclavitud", "Los años son 1553, 1598, 1641 y 1683."),
        ("{F} Un mapa muestra un fuerte español al sur del Biobío en 1600. ¿Qué debe recordar quien lo ve?", "que esa zona era la frontera y de guerra", "La ficha ubica la frontera en el Biobío."),
        ("{F} Pedro dice: «Valdivia murió en Curalaba». Corrígelo con años y lugares.", "Valdivia murió en Tucapel en 1553; Curalaba fue en 1598", "Son hechos distintos."),
        ("{F} Ana dice: «Los españoles siempre ganaron». ¿Qué hecho de la ficha lo contradice?", "los mapuche vencieron en Curalaba", "Ahí murió un gobernador."),
        ("{F} Clasifica como «guerra» o «acuerdo»: a) Curalaba; b) Parlamento de Quilín; c) Tucapel.", "guerra: a y c; acuerdo: b", "El parlamento fue una reunión de paz."),
        ("{F} ¿Qué dato muestra que las relaciones no fueron solo de guerra?", "el Parlamento de Quilín, una reunión de paz", "Fue un acuerdo pacífico."),
    ],
    ctx=("Un cartel de museo dice: «Parlamento de Quilín, 1641». ¿Qué parte indica el tiempo y cuál el tipo de hecho?", "tiempo: 1641; tipo: parlamento", "El año es el tiempo y la palabra parlamento indica el hecho."),
    sc=[("{F} ¿Qué fue el Parlamento de Quilín?", "una reunión de paz entre autoridades españolas y caciques mapuche", "La ficha lo dice."),
        ("¿Qué es una frontera?", "una zona de límite entre dos territorios", "Así se define."),
        ("{F} ¿En qué año el rey puso fin a la esclavitud de mapuche capturados en guerra?", "en 1683", "La ficha lo dice.")],
    op=("Dibuja una línea de tiempo con los años 1550, 1553, 1598, 1608, 1641 y 1683. Escribe un hecho de la ficha en cada año. Luego dibuja un mapa simple de Chile con el río Biobío y escribe «frontera» sobre él. {F}",
        "1553 Tucapel; 1598 Curalaba; 1641 Parlamento de Quilín; 1683 fin de esclavitud. En el mapa, el Biobío al sur de Concepción.",
        ["seis años en orden", "hechos correctos", "frontera bien ubicada"], ["línea de tiempo", "mapa"], ["mezclar Tucapel y Curalaba", "poner el Biobío al norte de Santiago"],
        "Pregunta qué hechos fueron de guerra y cuáles de acuerdo."),
    reinforce="Cuenta en voz alta los hechos de la ficha con sus años.",
    extend="Calcula cuántos años pasaron entre 1550 y 1683 y explica qué significa para la Colonia.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre españoles y mapuche (hechas para este cuaderno, a partir de hechos conocidos). Fuente A: La Araucana, poema del siglo XVI de Alonso de Ercilla, un soldado español que estuvo en Chile; cuenta la guerra y admira la valentía mapuche. "
     "Fuente B: el acta de un parlamento, escrita por un secretario español, que anota lo acordado entre el gobernador y los caciques. "
     "Fuente C: una real cédula del rey de 1608 que autoriza esclavizar a los mapuche capturados en guerra. "
     "Fuente D: el libro «Cautiverio feliz», del siglo XVII, escrito por Francisco Núñez de Pineda y Bascuñán, un militar nacido en Chile que fue prisionero de los mapuche y cuenta cómo fue tratado.")
build(
    OA7, 2, F,
    use="Aprenderé a leer fuentes sobre españoles y mapuche y a preguntar quién las hizo y para qué. Sirve para saber qué voces tenemos y cuáles faltan.",
    prior=["Sé la procedencia de una fuente.", "Sé la cronología de la guerra y de los parlamentos."],
    explain=[
        "Las fuentes sobre las relaciones entre españoles y mapuche casi siempre fueron escritas por españoles o por criollos. Ercilla, autor de La Araucana, fue un soldado que estuvo en Chile y admiraba la valentía mapuche. Pero habla desde la mirada española y escribe un poema.",
        "El acta de un parlamento la escribió un secretario español, así que anota lo acordado según su manera de ver. La real cédula de 1608 muestra lo que el rey permitía, no lo que sentían los mapuche. Núñez de Pineda fue un militar nacido en Chile que estuvo prisionero de los mapuche, y su libro cuenta cómo fue tratado; es una fuente valiosa, pero sigue siendo su versión.",
        "Casi no se conservan documentos escritos por los propios mapuche en esa época; su cultura transmitía la historia sobre todo hablando. Por eso es importante la tradición oral y la voz mapuche actual, que no debemos inventar. Debemos decir qué voz falta.",
    ],
    vocab=[("acta", "texto que anota lo ocurrido o acordado en una reunión"), ("secretario", "persona que escribía los documentos de una autoridad"), ("cautiverio", "tiempo en que una persona está prisionera"), ("tradición oral", "historias que se transmiten hablando de una generación a otra"), ("poema", "texto escrito en versos")],
    worked=[
        ("Leer la procedencia", "{F} ¿Quién escribió el acta de la fuente B?", ["Busco al autor en la ficha.", "Un secretario español."], "Un secretario español"),
        ("Reconocer la voz que falta", "{F} ¿Qué voz casi no aparece en estas fuentes?", ["Reviso quién escribió cada una.", "Las cuatro son de españoles o criollos."], "La voz mapuche escrita de esa época"),
    ],
    mistakes=[("Creer que Ercilla habla en nombre de los mapuche.", "Se confunde admiración con voz propia.", "Ercilla era un soldado español que admiraba su valentía."),
              ("Inventar lo que habrían dicho los mapuche.", "Se llena el vacío con imaginación.", "Di que falta su voz escrita de la época y recuerda la tradición oral.")],
    T=[
        ("{F} ¿Quién escribió La Araucana?", "Alonso de Ercilla", "La ficha lo dice."),
        ("{F} ¿Qué autoriza la fuente C?", "esclavizar a los mapuche capturados en guerra", "La ficha lo dice."),
        ("{F} ¿Quién fue prisionero de los mapuche y escribió un libro?", "Francisco Núñez de Pineda y Bascuñán", "La ficha lo dice."),
        ("{F} ¿Qué anota el acta de un parlamento?", "lo acordado entre el gobernador y los caciques", "La ficha lo dice."),
        ("{F} ¿En qué siglo se escribió «Cautiverio feliz»?", "en el siglo XVII", "La ficha lo dice."),
        ("{F} ¿Qué fuente es un poema?", "la fuente A", "La Araucana es un poema."),
        ("{F} Quieres saber qué había acordado un parlamento. ¿Qué fuente usas?", "la fuente B", "Es el acta."),
        ("{F} Quieres saber cómo vivió un prisionero con los mapuche. ¿Qué fuente usas?", "la fuente D", "Cuenta su experiencia."),
        ("{F} Quieres saber qué permitía el rey sobre la esclavitud. ¿Qué fuente usas?", "la fuente C", "Es la real cédula."),
        ("{F} Luis dice: «El acta de un parlamento muestra la versión mapuche». ¿Qué corrección haces?", "la escribió un secretario español, así que muestra su manera de ver lo acordado", "El autor es español."),
        ("{F} Ana dice: «Núñez de Pineda cuenta todo con total objetividad». ¿Qué cuidado se necesita?", "es su versión, la de un prisionero que cuenta su experiencia", "Toda fuente tiene punto de vista."),
        ("{F} Elige la pregunta que estas fuentes no responden bien. A) ¿Qué permitía el rey en 1608? B) ¿Cómo explicaban los propios mapuche, por escrito en esa época, por qué resistían?", "B", "Faltan fuentes escritas por mapuche de la época."),
        ("{F} Para comparar la mirada de un soldado con la de un prisionero, ¿qué dos fuentes enfrentas?", "la fuente A con la fuente D", "Ercilla fue soldado y Núñez de Pineda prisionero."),
    ],
    ctx=("En un museo hay una copia del acta de un parlamento con el cartel «Siglo XVII, secretario español». ¿Qué datos de procedencia entrega y qué falta?", "época y autor; falta la voz mapuche y el propósito", "El cartel da dos datos y no el resto."),
    sc=[("¿Qué tres preguntas hacemos a una fuente?", "quién la hizo, cuándo y para qué", "Con ellas medimos lo que aporta."),
        ("{F} ¿Qué voz casi no tenemos por escrito de esa época?", "la voz mapuche", "La ficha dice que las fuentes son de españoles o criollos."),
        ("¿Qué es la tradición oral?", "historias que se transmiten hablando de una generación a otra", "Así se define.")],
    op=("Haz una tabla con las fuentes A, B, C y D. Escribe «quién la hizo», «qué muestra» y «qué voz falta». Al final escribe una frase sobre por qué es importante escuchar la voz mapuche actual, sin inventar lo que diría. {F}",
        "A: un soldado español; guerra y valentía; falta la voz mapuche. B: un secretario español; lo acordado; falta la mirada mapuche. C: el rey; esclavitud; falta la voz de los esclavizados. D: un militar criollo; su cautiverio; falta la voz mapuche escrita.",
        ["cuatro filas completas", "voz que falta", "respeto por la voz mapuche"], ["tabla", "frase final"], ["inventar lo que dirían los mapuche", "confundir autores"],
        "Pregunta cómo podría una persona conocer la historia contada por una comunidad mapuche actual."),
    reinforce="Nombra las cuatro fuentes y quién habla en cada una.",
    extend="Escribe una pregunta respetuosa que harías a un educador o una educadora tradicional mapuche sobre la historia de su pueblo.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (formas de relación, hecha para este cuaderno). Guerra y resistencia: los mapuche defendieron su territorio durante siglos; los españoles mantuvieron fuertes y un ejército en la frontera. "
     "Trabajo: la encomienda obligaba a indígenas a trabajar para un español; en la guerra, algunos mapuche capturados fueron esclavizados mientras estuvo permitido (1608 a 1683). "
     "Evangelización: misioneros, como los jesuitas, llegaron a la frontera para enseñar el cristianismo, con resultados distintos. "
     "Vida fronteriza: españoles y mapuche comerciaban ponchos, ganado, sal y trigo, y hubo mestizaje. "
     "Parlamentos: reuniones donde caciques y autoridades españolas acordaban paz, comercio y devolución de cautivos.")
build(
    OA7, 3, F,
    use="Aprenderé las distintas formas en que se relacionaron españoles y mapuche y por qué ocurrieron. Sirve para explicar la frontera con ejemplos concretos.",
    prior=["Sé la cronología de la guerra.", "Sé qué es la encomienda y un parlamento."],
    explain=[
        "Españoles y mapuche se relacionaron de muchas maneras. La primera fue la guerra y la resistencia: los mapuche defendieron su territorio durante siglos y los españoles mantuvieron fuertes y un ejército en la frontera. Esa guerra tuvo causas, como la ocupación de tierras y la imposición del trabajo, y consecuencias, como la existencia de una frontera.",
        "Otra forma fue el trabajo. La encomienda obligaba a indígenas a trabajar para un español. En la guerra, algunos mapuche capturados fueron esclavizados entre 1608 y 1683, cuando estuvo permitido. También hubo evangelización: los jesuitas y otros misioneros llegaron a la frontera para enseñar el cristianismo, con resultados distintos.",
        "En la vida fronteriza, españoles y mapuche comerciaban ponchos, ganado, sal y trigo, y hubo mestizaje. En los parlamentos, caciques y autoridades acordaban paz, comercio y devolución de cautivos. Estas formas no se excluyen: el mismo año podía haber guerra en un lugar y comercio en otro.",
    ],
    vocab=[("encomienda", "sistema en que un español recibía indígenas para que trabajaran para él"), ("esclavitud", "situación de una persona obligada a trabajar sin libertad ni pago"), ("evangelización", "enseñanza del cristianismo"), ("vida fronteriza", "vida de las personas que viven cerca de una frontera"), ("cautivo", "persona prisionera")],
    worked=[
        ("Reconocer una forma", "{F} Un mapuche y un soldado intercambian un poncho por sal. ¿Qué forma de relación es?", ["Veo un intercambio de productos.", "Es comercio en la vida fronteriza."], "Comercio, parte de la vida fronteriza"),
        ("Distinguir un acuerdo", "{F} ¿Qué se acordaba en un parlamento?", ["Busco los temas en la ficha.", "Paz, comercio y devolución de cautivos."], "Paz, comercio y devolución de cautivos"),
    ],
    mistakes=[("Pensar que solo hubo guerra.", "Se ignora el comercio y los parlamentos.", "Nombra varias formas de relación."),
              ("Mezclar encomienda con esclavitud.", "Ambas son trabajo, pero distintas.", "La esclavitud fue permitida solo de 1608 a 1683; la encomienda era otra forma.")],
    T=[
        ("{F} ¿Qué productos se comerciaban en la frontera?", "ponchos, ganado, sal y trigo", "La ficha los nombra."),
        ("{F} ¿Qué misioneros llegaron a la frontera?", "los jesuitas, entre otros", "La ficha los nombra."),
        ("{F} ¿Qué se acordaba en un parlamento?", "paz, comercio y devolución de cautivos", "La ficha lo dice."),
        ("{F} ¿Qué defendieron los mapuche durante siglos?", "su territorio", "La ficha lo dice."),
        ("{F} ¿Entre qué años estuvo permitido esclavizar a mapuche capturados en guerra?", "entre 1608 y 1683", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos años estuvo permitida esa esclavitud, de 1608 a 1683?", "1683-1608", "Se resta el año de inicio al de término.", " años"),
        ("{F} Clasifica como «guerra», «trabajo», «evangelización» o «comercio»: a) un jesuita enseña en la frontera; b) un fuerte vigila el Biobío; c) se vende sal por ponchos.", "a: evangelización; b: guerra; c: comercio", "Cada ejemplo corresponde a una forma."),
        ("{F} Une cada forma con su descripción: 1) encomienda; 2) parlamento. a) reunión para acordar paz; b) indígenas obligados a trabajar para un español.", "1 con b; 2 con a", "Así las define la ficha."),
        ("{F} ¿Qué consecuencia tuvo la vida fronteriza además del comercio?", "el mestizaje", "La ficha lo dice."),
        ("{F} Pedro dice: «En la frontera solo había guerra». Da dos datos que lo contradicen.", "se comerciaba y se hacían parlamentos de paz", "La ficha nombra varias formas."),
        ("{F} Ana dice: «Los parlamentos sirvieron para esclavizar». ¿Qué corrección haces?", "se acordaba paz, comercio y devolución de cautivos", "Ese era su propósito."),
        ("{F} Clasifica como «trabajo forzado» o «acuerdo»: a) encomienda; b) Parlamento de Quilín; c) esclavitud permitida entre 1608 y 1683.", "trabajo forzado: a y c; acuerdo: b", "La encomienda y la esclavitud obligaban a trabajar; el parlamento buscaba paz."),
        ("{F} ¿Qué actor tomaba la decisión de permitir o terminar con la esclavitud: el rey o los caciques?", "el rey", "Las reales cédulas son órdenes del rey."),
    ],
    ctx=("En un museo, una vitrina muestra un poncho y un saco de sal con el rótulo «Intercambios en la frontera del Biobío». ¿Con qué forma de relación de la ficha se vinculan esos objetos?", "con el comercio de la vida fronteriza", "La ficha nombra ponchos y sal."),
    sc=[("{F} Nombra tres formas de relación entre españoles y mapuche.", "por ejemplo guerra, comercio y parlamentos", "La ficha las enumera."),
        ("¿Qué es la vida fronteriza?", "la vida de las personas que viven cerca de una frontera", "Así se define."),
        ("{F} ¿Cuál fue una consecuencia de la vida fronteriza?", "el mestizaje", "La ficha lo dice.")],
    op=("Dibuja un círculo con «Relaciones españoles-mapuche» en el centro y seis rayos: «guerra y resistencia», «trabajo», «evangelización», «comercio», «mestizaje» y «parlamentos». En cada rayo escribe un ejemplo de la ficha. {F}",
        "Guerra: fuertes en el Biobío. Trabajo: encomienda. Evangelización: jesuitas. Comercio: ponchos y sal. Mestizaje: vida fronteriza. Parlamentos: paz y devolución de cautivos.",
        ["seis rayos completos", "ejemplo correcto en cada uno", "datos de la ficha"], ["esquema de seis rayos"], ["poner ejemplos en el rayo equivocado", "dejar rayos vacíos"],
        "Pregunta qué forma de relación crees que cambió más con el tiempo."),
    reinforce="Nombra en voz alta las seis formas de relación con un ejemplo cada una.",
    extend="Escribe cómo podría ayudar un parlamento a evitar la guerra, usando solo lo que dice la ficha.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (perspectivas y territorios, hecha para este cuaderno). Perspectiva española: las autoridades querían mantener la seguridad de las ciudades, extender el cristianismo y ocupar territorio; también negociaban cuando les convenía. "
     "Perspectiva mapuche: los mapuche querían defender su territorio y su forma de vida; aceptaban dialogar en los parlamentos cuando les convenía. "
     "Territorios: en la zona central, la presencia española era estable, con ciudades y haciendas; en la frontera del Biobío había fuertes, soldados, comercio y contactos frecuentes entre españoles y mapuche. "
     "En los parlamentos, ambas partes se sentaban a negociar.")
build(
    OA7, 4, F,
    use="Aprenderé a comparar cómo veían la frontera los españoles y los mapuche, y cómo era la vida en la zona central y en la frontera. Sirve para entender por qué hubo guerra y acuerdos.",
    prior=["Sé las formas de relación.", "Sé comparar con criterios."],
    explain=[
        "Los españoles y los mapuche tenían objetivos distintos. Las autoridades españolas querían mantener la seguridad de las ciudades, extender el cristianismo y ocupar territorio, y también negociaban cuando les convenía. Los mapuche querían defender su territorio y su forma de vida, y aceptaban dialogar cuando les convenía.",
        "Esos objetivos distintos ayudan a explicar la guerra. Pero en los parlamentos ambas partes se sentaban a negociar. Allí se hablaba de paz, comercio y devolución de cautivos. Fueron una forma de buscar acuerdo sin renunciar a sus intereses.",
        "También comparamos territorios. En la zona central, la presencia española era estable, con ciudades y haciendas. En la frontera del Biobío había fuertes, soldados, comercio y contactos frecuentes entre españoles y mapuche. Cada territorio tuvo una vida distinta.",
    ],
    vocab=[("perspectiva", "punto de vista de un grupo sobre un hecho"), ("negociar", "conversar para llegar a un acuerdo"), ("estable", "que se mantiene sin grandes cambios"), ("forma de vida", "manera de vivir de un pueblo"), ("territorio", "zona que un pueblo considera suya")],
    worked=[
        ("Comparar perspectivas", "{F} ¿Qué querían los mapuche y qué querían las autoridades españolas?", ["Los mapuche querían defender su territorio y su forma de vida.", "Las autoridades querían seguridad, cristianismo y territorio."], "Mapuche: defender su territorio; españoles: seguridad, cristianismo y ocupar territorio"),
        ("Comparar territorios", "{F} ¿En qué se diferenciaba la zona central de la frontera?", ["En la zona central había ciudades y haciendas estables.", "En la frontera había fuertes, soldados y comercio."], "En la central, ciudades y haciendas; en la frontera, fuertes, soldados y comercio"),
    ],
    mistakes=[("Decir que ambos querían lo mismo.", "Se ignoran los intereses distintos.", "Cada parte tenía objetivos propios."),
              ("Pensar que los mapuche nunca negociaban.", "Se olvidan los parlamentos.", "Aceptaban dialogar cuando les convenía.")],
    T=[
        ("{F} ¿Qué querían defender los mapuche?", "su territorio y su forma de vida", "La ficha lo dice."),
        ("{F} ¿Qué querían extender las autoridades españolas?", "el cristianismo", "La ficha lo dice."),
        ("{F} ¿Dónde había fuertes y soldados?", "en la frontera del Biobío", "La ficha lo dice."),
        ("{F} ¿Dónde era estable la presencia española?", "en la zona central", "La ficha lo dice."),
        ("{F} ¿Qué hacían ambas partes en los parlamentos?", "negociar", "La ficha lo dice."),
        ("{F} ¿Cuándo aceptaban los mapuche dialogar?", "cuando les convenía", "La ficha lo dice."),
        ("{F} Clasifica como perspectiva «española» o «mapuche»: a) defender el territorio; b) mantener la seguridad de las ciudades.", "a: mapuche; b: española", "Cada frase corresponde a su grupo."),
        ("{F} Clasifica como «zona central» o «frontera»: a) haciendas; b) fuertes y soldados; c) ciudades.", "zona central: a y c; frontera: b", "La ficha asigna cada elemento."),
        ("{F} Elige la comparación correcta. A) En la frontera había contactos frecuentes entre españoles y mapuche. B) En la zona central había guerra constante.", "A", "La ficha lo dice."),
        ("{F} Pedro dice: «Los mapuche y los españoles querían lo mismo». Da un dato que lo contradice.", "los mapuche querían defender su territorio y los españoles ocupar territorio", "Son objetivos opuestos."),
        ("{F} Ana dice: «En un parlamento ganaba solo una parte». ¿Qué dato de la ficha la corrige?", "ambas partes se sentaban a negociar", "Se buscaba un acuerdo."),
        ("{F} ¿Por qué los objetivos distintos ayudan a explicar la guerra?", "porque los españoles querían ocupar territorio y los mapuche defenderlo", "Sus intereses chocaban."),
        ("{F} ¿Qué datos de la ficha muestran contacto entre españoles y mapuche en la frontera?", "el comercio y los contactos frecuentes, además de los parlamentos", "La ficha los nombra para la frontera."),
    ],
    ctx=("Un compañero dice: «En clase aprendimos que los mapuche siempre estuvieron en guerra». Usa dos datos de la ficha para ayudarlo a matizar.", "también negociaban en los parlamentos y comerciaban en la frontera", "La ficha muestra otras formas de relación."),
    sc=[("¿Qué es negociar?", "conversar para llegar a un acuerdo", "Así se define."),
        ("{F} ¿Qué diferencia hay entre la zona central y la frontera?", "en la central había ciudades y haciendas estables; en la frontera, fuertes y soldados", "La ficha las describe."),
        ("¿Por qué conviene comparar perspectivas?", "porque cada grupo veía los hechos desde sus intereses", "Así se evita una sola versión.")],
    op=("Haz una tabla con dos columnas, «españoles» y «mapuche», y tres filas: «qué querían», «cómo actuaban» y «qué hacían en los parlamentos». Completa con la ficha. Después escribe una frase que empiece con «Un parecido es…» y otra con «Una diferencia es…». {F}",
        "Españoles: seguridad y territorio; fuertes; negociar. Mapuche: defender territorio; resistir; negociar. Un parecido es que ambos negociaban. Una diferencia es lo que querían.",
        ["tabla completa", "un parecido", "una diferencia"], ["tabla", "dos frases"], ["inventar datos", "dar la misma meta a ambos"],
        "Pregunta por qué es útil comparar antes de opinar."),
    reinforce="Cuenta en voz alta qué querían españoles y mapuche.",
    extend="Escribe una pregunta que le harías a un historiador para conocer mejor la perspectiva mapuche.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (argumento, hecha para este cuaderno). Afirmación: «La relación entre españoles y mapuche no fue solo de guerra: también hubo comercio, trabajo forzado, evangelización, mestizaje y acuerdos». Datos: "
     "1) Los mapuche resistieron durante siglos y vencieron en Curalaba en 1598. 2) La encomienda y la esclavitud (1608 a 1683) obligaron a trabajar a algunos indígenas. 3) Misioneros como los jesuitas llegaron a la frontera. "
     "4) En la frontera se comerciaban ponchos, ganado, sal y trigo, y hubo mestizaje. 5) Los parlamentos, como el de Quilín en 1641, buscaron acordar paz y comercio.")
build(
    OA7, 5, F,
    use="Aprenderé a defender con evidencia que la relación entre españoles y mapuche tuvo muchas formas. Sirve para argumentar sin reducir la historia a una sola idea.",
    prior=["Sé las formas de relación.", "Sé armar un argumento con afirmación, evidencia y conclusión."],
    explain=[
        "Argumentar es defender una idea con evidencia. La idea de hoy es que la relación entre españoles y mapuche no fue solo de guerra. Hubo guerra, y también comercio, trabajo forzado, evangelización, mestizaje y acuerdos.",
        "La evidencia de la guerra es que los mapuche resistieron durante siglos y vencieron en Curalaba en 1598. La evidencia del trabajo es la encomienda y la esclavitud permitida entre 1608 y 1683. La evidencia de la evangelización es la llegada de misioneros a la frontera. La del comercio y el mestizaje es el intercambio de ponchos, ganado, sal y trigo. La de los acuerdos es el Parlamento de Quilín, en 1641.",
        "Estos datos muestran que había conflicto y también contacto. Pero no sabemos, por esta ficha, cómo vivió cada persona de la frontera ni qué pensaban los propios mapuche en sus palabras. Un buen argumento reconoce esos límites.",
    ],
    vocab=[("conflicto", "enfrentamiento entre personas o grupos"), ("contacto", "relación entre personas o grupos distintos"), ("evidencia", "dato de una fuente que apoya una idea"), ("matizar", "mostrar que una idea tiene más de un aspecto"), ("conclusión", "idea final que sale de unir la afirmación y la evidencia")],
    worked=[
        ("Elegir evidencia", "{F} ¿Qué dato apoya que hubo acuerdos?", ["Busco un dato de paz.", "El Parlamento de Quilín en 1641."], "El Parlamento de Quilín en 1641"),
        ("Reconocer un límite", "{F} ¿La ficha dice cómo vivió una familia de la frontera?", ["Reviso los datos.", "Solo hay datos generales."], "No, solo da datos generales"),
    ],
    mistakes=[("Defender la idea con un solo ejemplo.", "Se cree que uno basta.", "Usa al menos tres tipos de evidencia."),
              ("Decir que la frontera era solo paz.", "Se invierte el error.", "La afirmación dice que no fue solo guerra, no que no hubo guerra.")],
    T=[
        ("{F} ¿Qué batalla ganaron los mapuche en 1598?", "Curalaba", "El dato 1 lo dice."),
        ("{F} ¿Qué sistemas obligaron a trabajar a indígenas?", "la encomienda y la esclavitud", "El dato 2 los nombra."),
        ("{F} ¿Qué misioneros se nombran?", "los jesuitas", "El dato 3 los nombra."),
        ("{F} ¿Qué productos se comerciaban?", "ponchos, ganado, sal y trigo", "El dato 4 los nombra."),
        ("{F} ¿En qué año fue el Parlamento de Quilín?", "en 1641", "El dato 5 lo dice."),
        ("{F} ¿Qué dato apoya el comercio: el dato 4 o el dato 2?", "el dato 4", "Habla de ponchos, ganado, sal y trigo."),
        ("{F} ¿Qué dato apoya la resistencia: el dato 1 o el dato 3?", "el dato 1", "Curalaba fue una victoria mapuche."),
        ("{F} Ordena el argumento: a) conclusión: hubo guerra y también contactos y acuerdos; b) evidencia: el Parlamento de Quilín y el comercio; c) afirmación: la relación no fue solo de guerra.", "c, b, a", "Se afirma, se prueba y se concluye."),
        ("{F} Elena dice: «Si hubo parlamentos, no hubo guerra». ¿Qué dato de la ficha la corrige?", "los mapuche vencieron en Curalaba en 1598", "Hubo guerra y acuerdos en la misma época."),
        ("{F} Mateo dice: «Todos los mapuche fueron esclavizados». ¿Qué corrección haces?", "la esclavitud solo se permitió a los capturados en guerra entre 1608 y 1683", "La ficha precisa el período y el grupo."),
        ("{F} Argumento A: «Hubo comercio». Argumento B: «Hubo comercio, pues se intercambiaban ponchos, ganado, sal y trigo en la frontera». ¿Cuál es mejor?", "B, porque incluye evidencia", "Un argumento necesita datos."),
        ("{F} ¿Qué evidencia nueva ayudaría a conocer la mirada mapuche?", "una fuente de tradición oral mapuche o un relato mapuche actual", "Falta su propia voz."),
        ("{F} ¿Qué dato apoya el trabajo forzado: el dato 2 o el dato 5?", "el dato 2", "La encomienda y la esclavitud obligaban a trabajar."),
    ],
    ctx=("En clase, alguien dice: «Los españoles y los mapuche solo se pelearon». Usa dos datos de la ficha para responder.", "hubo comercio de ponchos y sal, y parlamentos como el de Quilín en 1641", "Los datos muestran contacto y acuerdos."),
    sc=[("¿Qué tres partes tiene un argumento?", "afirmación, evidencia y conclusión", "Así se ordena."),
        ("{F} ¿Qué cinco formas de relación, además de la guerra, nombra la afirmación?", "comercio, trabajo forzado, evangelización, mestizaje y acuerdos", "La afirmación las enumera después de «también hubo»."),
        ("¿Por qué conviene decir lo que la ficha no muestra?", "porque evita afirmar más de lo que prueba", "Es parte de argumentar bien.")],
    op=("Escribe un párrafo de cinco líneas que defienda la afirmación de la ficha. Debe tener tres datos de tipos distintos y terminar con «La ficha no dice…». Usa palabras respetuosas hacia el pueblo mapuche. {F}",
        "La relación no fue solo de guerra. Hubo guerra: Curalaba. Hubo comercio de ponchos y sal. Hubo acuerdos: el Parlamento de Quilín. La ficha no dice cómo lo vivió cada familia.",
        ["afirmación clara", "tres datos de tipos distintos", "un límite reconocido", "lenguaje respetuoso"], ["párrafo escrito"], ["usar un solo tipo de relación", "inventar diálogos mapuche"],
        "Pide que subraye los tres tipos de evidencia con colores distintos."),
    reinforce="Explica en voz alta tres datos que prueban que la relación tuvo varias formas.",
    extend="Escribe una pregunta de investigación sobre un parlamento y qué fuente necesitarías.",
)

# ================================================================ OA 08 · PATRIMONIO COLONIAL
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (patrimonio colonial en Chile, hecha para este cuaderno). Patrimonio es lo que heredamos del pasado y queremos conservar. Ejemplos de patrimonio colonial que sigue presente: "
     "la Iglesia de San Francisco, en Santiago, construida durante la Colonia; la Casa Colorada, en Santiago, del siglo XVIII; el Palacio de La Moneda, en Santiago, construido a fines de la Colonia como Casa de Moneda; "
     "la iglesia de San Pedro de Atacama, en el norte, de adobe y madera de cardón; el Fuerte de Niebla, en la región de Los Ríos, construido en el siglo XVII; y las iglesias de madera de Chiloé, como la de Achao, del siglo XVIII. "
     "También hay costumbres con raíces coloniales, como las fiestas religiosas con procesiones y la carrera de Cuasimodo, que se mantienen hoy en la zona central. En la Iglesia de San Francisco se conservan pinturas e imágenes religiosas de la Colonia, que son obras de arte.")
build(
    OA8, 1, F,
    use="Aprenderé a ubicar en el mapa y en el tiempo elementos del patrimonio colonial que siguen presentes. Sirve para reconocerlos en mi entorno o en fotografías.",
    prior=["Sé que la Colonia fue entre 1541 y 1810.", "Sé ubicar el norte, la zona central y el sur de Chile.", "Sé qué es un monumento."],
    explain=[
        "El patrimonio es lo que heredamos del pasado y queremos conservar para el futuro. El patrimonio colonial son los edificios, obras de arte y costumbres de la época de la Colonia, entre 1541 y 1810, que todavía existen. Pueden ser edificios, obras de arte o costumbres.",
        "En Santiago hay edificios coloniales, como la Iglesia de San Francisco, la Casa Colorada y el Palacio de La Moneda, que se construyó a fines de la Colonia como Casa de Moneda. En el norte está la iglesia de San Pedro de Atacama, hecha de adobe y madera de cardón. En el sur, el Fuerte de Niebla y las iglesias de madera de Chiloé, como la de Achao.",
        "También hay costumbres con raíces coloniales que siguen vivas, como las fiestas religiosas con procesiones y la carrera de Cuasimodo en la zona central. En la Iglesia de San Francisco se conservan pinturas e imágenes religiosas de la Colonia, que son obras de arte. Para ubicar un elemento, decimos dónde está y de qué época viene.",
    ],
    vocab=[("patrimonio", "lo que heredamos del pasado y queremos conservar"), ("edificio colonial", "construcción hecha entre 1541 y 1810"), ("adobe", "ladrillo grande de barro y paja secado al sol"), ("fuerte", "construcción militar para defender un lugar"), ("costumbre", "práctica que una comunidad repite con el tiempo")],
    worked=[
        ("Ubicar un elemento", "{F} ¿Dónde está la Casa Colorada?", ["Busco la Casa Colorada en la ficha.", "Está en Santiago."], "En Santiago"),
        ("Clasificar un elemento", "{F} ¿La carrera de Cuasimodo es un edificio, una obra de arte o una costumbre?", ["Es algo que se repite cada año.", "Es una práctica de la comunidad."], "Una costumbre"),
    ],
    mistakes=[("Pensar que el patrimonio solo son edificios.", "Se olvidan obras de arte y costumbres.", "Incluye costumbres como las procesiones."),
              ("Ubicar Chiloé en el norte.", "Se confunde la ubicación.", "Chiloé está en el sur de Chile.")],
    T=[
        ("{F} ¿En qué ciudad están la Casa Colorada y el Palacio de La Moneda?", "en Santiago", "La ficha los ubica ahí."),
        ("{F} ¿De qué materiales es la iglesia de San Pedro de Atacama?", "adobe y madera de cardón", "La ficha lo dice."),
        ("{F} ¿Qué construcción de la ficha es un fuerte?", "el Fuerte de Niebla", "La ficha lo dice."),
        ("{F} ¿Qué obras de arte de la Colonia se conservan en la Iglesia de San Francisco?", "pinturas e imágenes religiosas", "La ficha lo dice."),
        ("{F} ¿Cuándo se construyó el Fuerte de Niebla?", "en el siglo XVII", "La ficha lo dice."),
        ("{F} ¿Qué costumbre colonial sigue hoy en la zona central?", "la carrera de Cuasimodo, además de fiestas religiosas con procesiones", "La ficha lo dice."),
        ("{F} Clasifica como «norte», «zona central» o «sur»: a) iglesia de San Pedro de Atacama; b) Casa Colorada; c) iglesia de Achao.", "norte: a; zona central: b; sur: c", "Cada elemento está en esa zona."),
        ("{F} Clasifica como «edificio» o «costumbre»: a) Palacio de La Moneda; b) fiestas con procesiones; c) Iglesia de San Francisco.", "edificio: a y c; costumbre: b", "Una costumbre es una práctica."),
        ("{F} ¿Cuál de estas construcciones se hizo a fines de la Colonia: el Palacio de La Moneda o el Fuerte de Niebla?", "el Palacio de La Moneda", "La ficha dice que La Moneda se construyó a fines de la Colonia y Niebla en el siglo XVII."),
        ("{F} Pedro dice: «Todo el patrimonio colonial está en Santiago». Da dos ejemplos que lo contradicen.", "la iglesia de San Pedro de Atacama y las iglesias de Chiloé", "Están fuera de Santiago."),
        ("{F} Ana dice: «El patrimonio colonial son solo cosas del siglo XX». Corrígela.", "es del período 1541 a 1810", "La ficha lo dice."),
        ("{F} Ordena los elementos según su ubicación de norte a sur: Fuerte de Niebla, San Pedro de Atacama, Casa Colorada.", "San Pedro de Atacama, Casa Colorada, Fuerte de Niebla", "Atacama está al norte, Santiago al centro y Niebla al sur."),
        ("{F} ¿Por qué son patrimonio las iglesias de Chiloé?", "porque heredamos esas obras del pasado y queremos conservarlas", "Es la definición de patrimonio."),
    ],
    ctx=("Una compañera muestra una foto de una iglesia de madera con techo de tejuelas, en una isla del sur. ¿De qué elemento de la ficha puede ser y por qué?", "de una iglesia de Chiloé, porque son de madera y están en el sur", "La ficha describe las iglesias de madera de Chiloé."),
    sc=[("¿Qué es el patrimonio?", "lo que heredamos del pasado y queremos conservar", "Así se define."),
        ("{F} Nombra dos elementos del patrimonio colonial en Santiago.", "por ejemplo la Casa Colorada y la Iglesia de San Francisco", "La ficha los ubica ahí."),
        ("{F} ¿Qué tipo de patrimonio es la carrera de Cuasimodo?", "una costumbre", "Es una práctica repetida.")],
    op=("Dibuja un mapa simple de Chile con tres zonas: norte, zona central y sur. Marca cinco elementos de la ficha con un punto y escribe su nombre: dos en la zona central, uno en el norte y dos en el sur. Al lado, escribe si es edificio o costumbre. {F}",
        "Norte: San Pedro de Atacama (edificio). Centro: Casa Colorada y Cuasimodo. Sur: Fuerte de Niebla y Achao.",
        ["cinco elementos", "ubicación correcta", "tipo bien indicado"], ["mapa simple"], ["poner Chiloé en el norte", "confundir edificio con costumbre"],
        "Pregunta cuál elemento de la ficha te gustaría visitar y por qué."),
    reinforce="Nombra tres elementos del patrimonio colonial con su lugar.",
    extend="Escribe un elemento colonial que puedas ver cerca de tu casa o en fotografías, si lo conoces.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes para identificar patrimonio (hechas para este cuaderno, con ejemplos). Fuente A: una fotografía actual de una iglesia con muros gruesos de adobe y techo de tejas; al pie dice: «Iglesia colonial, siglo XVII». "
     "Fuente B: una placa colocada por una municipalidad junto a una casa: «Casa construida en 1769. Fue de una familia de comerciantes». "
     "Fuente C: un decreto del Consejo de Monumentos Nacionales que declara Monumento Nacional un edificio colonial para protegerlo por ley. "
     "Fuente D: el relato de una vecina que cuenta que, cuando era niña, su familia iba cada año a una procesión en la plaza, igual que sus abuelos.")
build(
    OA8, 2, F,
    use="Aprenderé a reconocer en fotografías, placas y relatos si algo es patrimonio colonial y a preguntar quién lo dice. Sirve para identificar el patrimonio con evidencia.",
    prior=["Sé qué es el patrimonio colonial.", "Sé preguntar quién hizo una fuente."],
    explain=[
        "Para identificar patrimonio colonial usamos fuentes. Una fotografía actual muestra cómo se ve hoy un edificio. Si tiene muros gruesos de adobe y techo de tejas, y al pie dice «Iglesia colonial, siglo XVII», podemos pensar que es de la Colonia. Lo más seguro es la fecha del pie de la foto: el adobe y las tejas ayudan, pero no bastan, porque también se usaron después de 1810. La fotografía no dice quién la construyó.",
        "Una placa de una municipalidad entrega un dato: la casa se construyó en 1769. Pero la placa la puso la municipalidad años después, y debemos preguntar su fuente. Un decreto del Consejo de Monumentos Nacionales declara un edificio Monumento Nacional, es decir, protegido por ley.",
        "El relato de una vecina muestra una costumbre que se mantiene: una procesión en la plaza que sus abuelos también vivían. Es una fuente oral. Cada fuente muestra una parte: la foto lo físico, la placa una fecha, el decreto la protección y el relato la tradición viva.",
    ],
    vocab=[("Monumento Nacional", "bien declarado por el Estado como importante y protegido por la ley"), ("placa", "lámina con información puesta junto a un edificio"), ("decreto", "documento oficial con una decisión de una autoridad"), ("fuente oral", "relato contado por una persona"), ("tejas", "piezas de arcilla que cubren techos")],
    worked=[
        ("Reconocer un rasgo", "{F} ¿Qué rasgos de la fuente A indican que la iglesia es colonial?", ["Leo la descripción de la foto.", "Tiene muros de adobe y techo de tejas, pero lo más seguro es la nota del pie: siglo XVII."], "La nota «siglo XVII»; el adobe y las tejas ayudan, pero no bastan"),
        ("Reconocer un límite", "{F} ¿La placa de la fuente B dice quién construyó la casa?", ["Reviso el texto de la placa.", "Solo dice la fecha y que fue de una familia."], "No, solo da la fecha y la familia"),
    ],
    mistakes=[("Creer que cualquier edificio antiguo es colonial.", "No se revisa la fecha.", "Busca la época: debe ser entre 1541 y 1810."),
              ("Creer que una placa no necesita revisión.", "Se supone que siempre es exacta.", "Pregunta quién la puso y con qué fuente.")],
    T=[
        ("{F} ¿De qué siglo dice ser la iglesia de la fuente A?", "del siglo XVII", "El pie de la foto lo dice."),
        ("{F} ¿En qué año se construyó la casa de la fuente B?", "en 1769", "La placa lo dice."),
        ("{F} ¿Quién puso la placa de la fuente B?", "una municipalidad", "La ficha lo dice."),
        ("{F} ¿Qué institución emitió el decreto de la fuente C?", "el Consejo de Monumentos Nacionales", "La ficha lo dice."),
        ("{F} ¿Qué fuente es un relato oral?", "la fuente D", "La vecina cuenta su experiencia."),
        ("{F} ¿De qué material son los muros de la iglesia de la fuente A?", "de adobe", "La ficha lo dice."),
        ("{F} ¿Una casa construida en 1769 es colonial? Responde con la fecha límite de la Colonia.", "Sí, porque la Colonia llegó hasta 1810", "1769 es anterior a 1810."),
        ("{F} Quieres saber si un edificio está protegido por ley. ¿Qué fuente usas?", "la fuente C", "El decreto lo declara Monumento Nacional."),
        ("{F} Quieres saber si una costumbre sigue viva. ¿Qué fuente usas?", "la fuente D", "El relato cuenta que la procesión se mantiene."),
        ("{F} Luis dice: «Si es antiguo, es colonial». ¿Qué corrección haces?", "debe ser de la época entre 1541 y 1810", "Hay edificios antiguos de otras épocas."),
        ("{F} Ana dice: «La placa prueba todo sobre la casa». ¿Qué cuidado se necesita?", "preguntar quién la puso y en qué se basó, porque solo da algunos datos", "La placa tiene límites."),
        ("{F} Elige la pregunta que las fuentes no responden. A) ¿En qué año se construyó la casa de la placa? B) ¿Cuánto costó construirla?", "B", "Ninguna fuente da el costo."),
        ("{F} Para saber cómo se ve y cómo se protege un edificio, ¿qué dos fuentes unes?", "la fuente A con la fuente C", "Una muestra su aspecto y la otra su protección."),
    ],
    ctx=("En tu ciudad ves una placa que dice: «Iglesia de adobe, construida en 1780». ¿La puedes identificar como patrimonio colonial? Explica.", "sí, porque 1780 está entre 1541 y 1810", "La fecha cae dentro de la Colonia."),
    sc=[("¿Qué es un Monumento Nacional?", "un bien declarado importante y protegido por la ley", "Así se define."),
        ("{F} ¿Qué tipo de fuente es la fotografía de la fuente A?", "una fuente visual actual", "Es una imagen de hoy."),
        ("¿Por qué conviene revisar quién hizo una placa?", "porque puede tener errores o dar solo algunos datos", "Toda fuente tiene procedencia y límites.")],
    op=("Haz una tabla con las fuentes A, B, C y D. En las columnas escribe «qué tipo de fuente es», «qué me ayuda a identificar» y «qué no me dice». {F}",
        "A: fotografía; muestra el aspecto; no dice quién la construyó. B: placa; la fecha; no dice quién la construyó. C: decreto; la protección legal; no dice cómo se ve. D: relato oral; una costumbre; no dice el año de origen.",
        ["cuatro filas completas", "tipo de fuente correcto", "un límite por fuente"], ["tabla de tres columnas"], ["no indicar límites", "confundir las fuentes"],
        "Pregunta qué fuente le serviría para reconocer una costumbre."),
    reinforce="Nombra las cuatro fuentes y para qué sirve cada una.",
    extend="Escribe qué preguntas harías a una persona mayor de tu familia sobre una costumbre que se repite cada año.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (por qué se conserva el patrimonio, hecha para este cuaderno). Muchos edificios coloniales siguen en pie porque se construyeron con muros gruesos de adobe, techos de teja o madera resistente y porque la gente siguió usándolos: iglesias, casas, fuertes. "
     "Pero Chile tiene muchos terremotos y muchos edificios coloniales se cayeron y fueron reconstruidos. La humedad, el abandono y el paso del tiempo también los dañan. "
     "Hoy el Consejo de Monumentos Nacionales y las municipalidades protegen algunos edificios por ley, y vecinos y comunidades los cuidan y los restauran. "
     "Las costumbres, como las procesiones, siguen porque las familias las repiten cada año.")
build(
    OA8, 3, F,
    use="Aprenderé por qué algunos elementos coloniales siguen presentes, quiénes los protegen y qué los amenaza. Sirve para entender las causas y consecuencias de conservar el patrimonio.",
    prior=["Sé qué es el patrimonio colonial.", "Sé que Chile tiene terremotos."],
    explain=[
        "Hay elementos coloniales que siguen presentes por varias razones. Muchos edificios se construyeron con muros gruesos de adobe y techos de teja o madera resistente, y la gente siguió usándolos como iglesias, casas o fuertes. Un edificio que se usa se cuida más.",
        "Pero hay amenazas. Chile tiene muchos terremotos, y muchos edificios coloniales se cayeron y fueron reconstruidos. La humedad, el abandono y el paso del tiempo también los dañan. Por eso son importantes los actores que los protegen: el Consejo de Monumentos Nacionales y las municipalidades, que pueden protegerlos por ley, y los vecinos y comunidades que los cuidan y restauran.",
        "Las costumbres, como las procesiones, se conservan porque las familias las repiten cada año. El patrimonio vive mientras las personas lo cuidan y lo practican. Si se abandona, se pierde. Conservar es una decisión que se toma entre todos.",
    ],
    vocab=[("restaurar", "arreglar un edificio o una obra antigua cuidando que conserve su aspecto"), ("amenaza", "algo que puede dañar o hacer desaparecer"), ("proteger por ley", "declarar que un bien no se puede destruir ni cambiar sin permiso"), ("abandono", "falta de cuidado de un lugar"), ("comunidad", "grupo de personas que viven y trabajan juntas en un lugar")],
    worked=[
        ("Causa de conservación", "{F} ¿Por qué siguen en pie muchos edificios coloniales?", ["Busco las razones en la ficha.", "Tenían muros gruesos y techos resistentes y la gente siguió usándolos."], "Por sus materiales resistentes y porque se siguieron usando"),
        ("Identificar un actor", "{F} ¿Quién puede proteger un edificio por ley?", ["Busco al actor en la ficha.", "El Consejo de Monumentos Nacionales y las municipalidades."], "El Consejo de Monumentos Nacionales y las municipalidades"),
    ],
    mistakes=[("Creer que el patrimonio se cuida solo.", "Se olvida el papel de las personas.", "Nombra actores que lo protegen."),
              ("Creer que todo edificio colonial sigue intacto.", "Se ignoran terremotos y reconstrucciones.", "Muchos fueron reconstruidos.")],
    T=[
        ("{F} ¿Qué amenaza natural nombra la ficha?", "los terremotos", "La ficha lo dice."),
        ("{F} ¿De qué material eran los muros de muchos edificios?", "adobe", "La ficha lo dice."),
        ("{F} ¿Qué dos daños nombra además de los terremotos: humedad y abandono o lluvia y viento?", "humedad y abandono", "La ficha lo dice."),
        ("{F} ¿Quiénes cuidan y restauran los edificios además del Consejo de Monumentos Nacionales?", "vecinos y comunidades, y las municipalidades", "La ficha lo dice."),
        ("{F} ¿Por qué siguen las procesiones?", "porque las familias las repiten cada año", "La ficha lo dice."),
        ("{F} Clasifica como «causa de conservación» o «amenaza»: a) uso continuo; b) abandono; c) terremoto.", "causa de conservación: a; amenaza: b y c", "El uso ayuda y los otros dañan."),
        ("{F} ¿Qué consecuencia tuvo un terremoto en muchos edificios coloniales?", "muchos se cayeron y fueron reconstruidos", "La ficha lo dice."),
        ("{F} Ordena la cadena: a) se reconstruye el edificio; b) un terremoto lo daña; c) la comunidad decide cuidarlo.", "b, c, a", "El daño lleva a la decisión y luego a la reconstrucción."),
        ("{F} Une cada actor con lo que hace: 1) municipalidad; 2) vecinos. a) cuidan y restauran; b) protegen por ley.", "1 con b; 2 con a", "La ficha lo indica."),
        ("{F} Pedro dice: «Las iglesias coloniales duran por casualidad». Da una causa de la ficha.", "tenían muros gruesos y se siguieron usando", "La ficha explica por qué duran."),
        ("{F} Ana dice: «Un edificio abandonado no corre riesgo». ¿Qué dato lo contradice?", "el abandono lo daña con el tiempo", "La ficha lo nombra como daño."),
        ("{F} ¿Por qué decimos que conservar es una decisión que se toma entre todos?", "porque lo cuidan el Estado, la municipalidad y la comunidad", "Participan muchos actores."),
        ("{F} ¿Qué pasaría con una costumbre si ninguna familia la repitiera?", "se perdería", "Las costumbres siguen mientras las personas las practican."),
    ],
    ctx=("Una junta de vecinos quiere restaurar una iglesia dañada por la humedad. ¿Qué actores de la ficha podría pedir que la protejan?", "el Consejo de Monumentos Nacionales y la municipalidad", "La ficha nombra esos actores."),
    sc=[("¿Qué significa restaurar?", "arreglar una obra antigua cuidando que conserve su aspecto", "Así se define."),
        ("{F} ¿Por qué es importante el uso continuo de un edificio?", "porque un edificio que se usa se cuida más", "La ficha lo explica."),
        ("Nombra dos amenazas al patrimonio.", "por ejemplo terremotos y abandono", "La ficha las nombra.")],
    op=("Haz un esquema con tres columnas: «por qué se conserva», «qué lo amenaza» y «quién lo protege». Escribe dos ideas en cada columna usando la ficha. {F}",
        "Se conserva: adobe grueso y uso continuo. Amenaza: terremotos y abandono. Protegen: Consejo de Monumentos Nacionales y vecinos.",
        ["tres columnas", "dos ideas por columna", "datos de la ficha"], ["esquema de tres columnas"], ["mezclar amenazas con protecciones", "inventar actores"],
        "Pregunta qué harías tú para cuidar un lugar antiguo de tu barrio."),
    reinforce="Explica en voz alta una causa de conservación, una amenaza y un actor.",
    extend="Escribe una regla sencilla de buen trato para visitar una iglesia antigua o un fuerte.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación, hecha para este cuaderno). Casa Colorada, en Santiago: casa colonial del siglo XVIII, hoy museo. Iglesias de Chiloé: iglesias de madera del siglo XVIII y posteriores, que se siguen usando para ceremonias religiosas y fiestas, y que fueron declaradas Patrimonio Mundial por la UNESCO en el año 2000. "
     "Fuerte de Niebla: construcción del siglo XVII para defender la costa; hoy se visita como sitio histórico. Carrera de Cuasimodo: costumbre en que, después de Semana Santa, personas a caballo o en bicicleta acompañan al sacerdote para llevar la comunión a enfermos. "
     "Perspectivas: un vecino de Chiloé siente que su iglesia es un lugar de fe y de comunidad; un turista la mira como una obra de arte; un museo la mira como un recurso para enseñar historia.")
build(
    OA8, 4, F,
    use="Aprenderé a comparar elementos del patrimonio colonial, su uso antes y hoy, y cómo lo ven distintas personas. Sirve para valorar el patrimonio desde varias miradas.",
    prior=["Sé qué elementos coloniales siguen presentes.", "Sé comparar con criterios."],
    explain=[
        "Podemos comparar elementos del patrimonio con estos criterios: tipo, época, uso en el pasado y uso hoy. La Casa Colorada fue una casa del siglo XVIII y hoy es un museo. Las iglesias de Chiloé son de madera y se siguen usando para ceremonias religiosas y fiestas. En el año 2000 fueron declaradas Patrimonio Mundial por la UNESCO.",
        "El Fuerte de Niebla se construyó en el siglo XVII para defender la costa y hoy se visita como sitio histórico. La carrera de Cuasimodo es una costumbre: después de Semana Santa, personas a caballo o en bicicleta acompañan al sacerdote para llevar la comunión a enfermos. Entonces, algunos elementos cambiaron de uso y otros lo mantienen.",
        "Cada persona mira el patrimonio de manera distinta. Un vecino de Chiloé puede ver su iglesia como lugar de fe y de comunidad; un turista, como una obra de arte; un museo, como un recurso para enseñar historia. Todas las miradas son válidas y ayudan a cuidarlo.",
    ],
    vocab=[("UNESCO", "organización de las Naciones Unidas que protege la educación, la ciencia y la cultura"), ("Patrimonio Mundial", "bien cultural o natural reconocido como importante para toda la humanidad"), ("sitio histórico", "lugar importante por hechos del pasado"), ("comunión", "pan que reciben los fieles católicos en la misa"), ("recurso educativo", "material que sirve para enseñar")],
    worked=[
        ("Comparar el uso", "{F} ¿Cómo cambió el uso del Fuerte de Niebla?", ["Antes defendía la costa.", "Hoy se visita como sitio histórico."], "Antes defendía la costa y hoy se visita"),
        ("Comparar perspectivas", "{F} ¿Cómo mira una iglesia de Chiloé un vecino y cómo un museo?", ["El vecino la ve como lugar de fe y comunidad.", "El museo la ve como recurso para enseñar historia."], "El vecino, como lugar de fe y comunidad; el museo, como recurso para enseñar historia"),
    ],
    mistakes=[("Creer que todo el patrimonio mantiene su uso original.", "Se ignoran los cambios.", "Algunos edificios cambiaron de uso, como la Casa Colorada."),
              ("Creer que solo hay una forma de valorarlo.", "Se supone una sola mirada.", "Incluye la mirada de la comunidad, del turista y del museo.")],
    T=[
        ("{F} ¿Qué es hoy la Casa Colorada?", "un museo", "La ficha lo dice."),
        ("{F} ¿En qué año fueron declaradas Patrimonio Mundial las iglesias de Chiloé?", "en el año 2000", "La ficha lo dice."),
        ("{F} ¿Para qué se construyó el Fuerte de Niebla?", "para defender la costa", "La ficha lo dice."),
        ("{F} ¿Qué lleva el sacerdote a los enfermos en la carrera de Cuasimodo?", "la comunión", "La ficha lo dice."),
        ("{F} ¿De qué material son las iglesias de Chiloé?", "de madera", "La ficha lo dice."),
        ("{F} Clasifica como «sigue con el uso original» o «cambió de uso»: a) iglesias de Chiloé; b) Casa Colorada.", "a: sigue con el uso original; b: cambió de uso", "Una iglesia sigue como iglesia y una casa pasó a ser museo."),
        ("{F} ¿Qué elemento es una costumbre: el Fuerte de Niebla o la carrera de Cuasimodo?", "la carrera de Cuasimodo", "Es una práctica que se repite."),
        ("{F} Elige la comparación correcta. A) La Casa Colorada y el Fuerte de Niebla hoy no se usan como antes. B) Ambos se usan igual que en el pasado.", "A", "Ambos cambiaron de uso."),
        ("{F} El Fuerte de Niebla es del siglo XVII y la Casa Colorada del siglo XVIII. ¿Cuál es más antigua?", "el Fuerte de Niebla", "El siglo XVII es anterior al siglo XVIII."),
        ("{F} Tomás dice: «Para todos, una iglesia de Chiloé significa lo mismo». Da dos datos de la ficha que lo contradicen.", "para el vecino es fe y comunidad, para el turista obra de arte y para el museo recurso educativo", "Las miradas son distintas."),
        ("{F} Ana dice: «Una costumbre no es patrimonio». ¿Qué ejemplo de la ficha la corrige?", "la carrera de Cuasimodo", "Es una costumbre que sigue viva y que se hereda."),
        ("{F} ¿Por qué un museo valora una iglesia distinto a un vecino?", "porque la mira como recurso para enseñar historia y no como lugar de fe", "Cada mirada tiene un propósito."),
        ("{F} Compara cómo se usan hoy la Casa Colorada y el Fuerte de Niebla.", "la Casa Colorada es un museo y el Fuerte de Niebla un sitio histórico que se visita", "La ficha da el uso actual de ambos."),
    ],
    ctx=("Un afiche municipal dice: «Visita el Fuerte de Niebla, un lugar para aprender historia». ¿Qué perspectiva sobre el patrimonio muestra el afiche?", "la de un recurso para enseñar y visitar", "El afiche lo presenta como sitio para aprender."),
    sc=[("{F} ¿Qué organización declaró Patrimonio Mundial a las iglesias de Chiloé?", "la UNESCO", "La ficha lo dice."),
        ("¿Qué es un sitio histórico?", "un lugar importante por hechos del pasado", "Así se define."),
        ("¿Por qué conviene conocer varias miradas sobre el patrimonio?", "porque ayudan a valorarlo y cuidarlo desde distintos intereses", "Cada mirada aporta una razón.")],
    op=("Haz una tabla con tres filas: «Casa Colorada», «iglesias de Chiloé» y «Fuerte de Niebla». En las columnas escribe «época», «uso antes» y «uso hoy». Después escribe dos frases sobre cómo lo ven un vecino y un turista. {F}",
        "Casa Colorada: siglo XVIII; casa; museo. Iglesias de Chiloé: siglo XVIII; ceremonias; ceremonias y fiestas. Fuerte de Niebla: siglo XVII; defensa; visita.",
        ["tabla completa", "usos antes y hoy", "dos perspectivas"], ["tabla", "dos frases"], ["inventar usos", "olvidar una de las tres filas"],
        "Pregunta qué elemento cambió más su uso y por qué."),
    reinforce="Cuenta en voz alta cómo cambió el uso de tres elementos coloniales.",
    extend="Escribe una idea para que niños y niñas de tu escuela cuiden un lugar patrimonial.",
)
