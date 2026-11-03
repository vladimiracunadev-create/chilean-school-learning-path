"""Material del estudiante de 8.º básico, Historia, Geografía y Ciencias Sociales: OA 02 (de la sociedad medieval a la moderna)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI08 OA 02"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (hitos redondeados). Hacia 1450: imprenta de tipos móviles de Gutenberg, en Maguncia. 1492: los Reyes Católicos terminan la conquista de Granada y Colón llega a América. "
     "1517: Martín Lutero da a conocer sus 95 tesis, inicio de la Reforma. 1534: el rey Enrique VIII de Inglaterra se declara jefe de la Iglesia en su reino. "
     "1543: Nicolás Copérnico publica su obra sobre el movimiento de los planetas alrededor del Sol. 1687: Isaac Newton publica sus Principia. "
     "Sociedad medieval (siglos V al XV): poder repartido entre señores y reyes; Iglesia católica como única autoridad religiosa en Europa occidental; saber basado en autoridades antiguas y libros copiados a mano. "
     "Sociedad moderna (siglos XV al XVIII): reyes con más poder, Europa dividida en iglesias distintas, libros impresos y ciencia basada en la observación y el experimento.")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo los cambios que separan la sociedad medieval de la moderna, y a nombrar las cuatro transformaciones que estudiaremos.",
    prior=["Sé que Edad Media y Edad Moderna son convenciones.", "Sé calcular diferencias entre años y ubicar siglos.", "Conozco el Renacimiento y el Humanismo."],
    explain=[
        "La sociedad medieval y la sociedad moderna se diferencian en muchos aspectos. El OA nos pide comparar cuatro cambios principales: la ruptura de la unidad religiosa de Europa, el surgimiento de Estados con poder más centralizado, la difusión de ideas gracias a la imprenta y la revolución científica, que dio origen a la ciencia moderna.",
        "Estos cambios no ocurrieron el mismo año. La imprenta es de hacia 1450, la Reforma comenzó en 1517 y la obra de Copérnico es de 1543. Se suceden y se influyen: la imprenta ayudó a difundir tanto las ideas de la Reforma como las de la ciencia. Por eso conviene verlos como una red de cambios y no como hechos aislados.",
        "Pasar de una época a otra no significa que todo cambie de golpe. La Edad Media termina por convención en torno a 1453 o 1492, pero la religión, la nobleza y la vida campesina continuaron en la Edad Moderna. Comparar épocas es identificar qué cambia, qué continúa y en qué ritmo.",
    ],
    vocab=[("Reforma", "movimiento religioso del siglo XVI que rompió la unidad de la Iglesia católica en Europa"), ("Estado centralizado", "Estado en que el poder se concentra en un gobierno central"), ("imprenta", "máquina que imprime textos con letras móviles, creada hacia 1450"), ("revolución científica", "cambio en la manera de conocer, basada en observar y experimentar"), ("hito", "hecho importante que marca un punto en el tiempo")],
    worked=[
        ("Calcular una distancia en años", "Según la ficha, ¿cuántos años pasaron entre la imprenta de Gutenberg (hacia 1450) y las 95 tesis de Lutero?", ["Busco los años: 1450 y 1517.", "Resto: 1517 − 1450 = 67."], "67 años"),
        ("Clasificar un cambio", "El hecho «un rey se declara jefe de la Iglesia en su reino» ¿es un cambio religioso o científico?", ["El rey interviene en el gobierno de la Iglesia.", "Eso rompe la unidad religiosa."], "Religioso: ruptura de la unidad religiosa"),
    ],
    mistakes=[("Pensar que los cuatro cambios ocurrieron el mismo año.", "Se mezclan hitos que ocurren con décadas de diferencia.", "Ubica cada hito con su año en una línea de tiempo."),
              ("Creer que la sociedad moderna fue completamente distinta de la medieval.", "Se ignoran las continuidades como la religión cristiana y la vida campesina.", "Compara cambios y continuidades en cada aspecto.")],
    T=[
        ("{F} ¿En qué año se inicia la Reforma según la ficha?", "1517", "Es el año de las 95 tesis de Lutero."),
        ("{F} ¿Qué rey se declaró jefe de la Iglesia en su reino en 1534?", "Enrique VIII de Inglaterra", "La ficha lo indica."),
        ("{F} ¿Qué obra de 1543 se relaciona con la revolución científica?", "La obra de Copérnico sobre el movimiento de los planetas alrededor del Sol", "La ficha la cita entre los hitos."),
        ("=", "{F} ¿Cuántos años pasaron entre las 95 tesis de Lutero y la obra de Copérnico?", "1543-1517", "Se resta el año de las tesis al de la obra de Copérnico.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la publicación de los Principia de Newton y la de Copérnico?", "1687-1543", "Se restan los dos años de publicación.", " años"),
        ("{F} Ordena de más antiguo a más reciente: Newton publica los Principia, Lutero da a conocer las 95 tesis, se inventa la imprenta, Enrique VIII encabeza la Iglesia inglesa.", "Imprenta, 95 tesis de Lutero, Enrique VIII encabeza la Iglesia inglesa, Newton publica los Principia", "Los años son hacia 1450, 1517, 1534 y 1687."),
        ("{F} Clasifica cada hito en religioso, político o científico: a) Lutero y sus 95 tesis, b) Granada conquistada por los Reyes Católicos, c) la obra de Copérnico.", "a) religioso; b) político; c) científico", "Cada hito pertenece al ámbito que su protagonista transforma."),
        ("{F} ¿Qué rasgo de la sociedad medieval cambia con la Reforma? A) La Iglesia católica deja de ser la única autoridad religiosa de Europa occidental B) Los libros comienzan a copiarse a mano", "A) La Iglesia católica deja de ser la única autoridad religiosa de Europa occidental", "La Reforma rompe esa unidad; copiar a mano es medieval."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 50 años. ¿A cuántos cm de distancia quedan la imprenta (1450) y los Principia de Newton (1687) aproximadamente, redondeando hacia abajo?", "(1687-1450)//50", "Se calcula la diferencia de años y se divide por la escala.", " cm"),
        ("{F} Un compañero afirma: «La Edad Moderna empezó el mismo día en toda Europa». ¿Qué responde la ficha?", "Que los hitos están repartidos entre 1450 y 1687, así que el cambio fue gradual", "La ficha muestra hitos separados por décadas."),
        ("{F} ¿Qué cambio de la ficha ayudó a difundir tanto las ideas de la Reforma como las de la ciencia?", "La imprenta", "Permitió copiar textos más rápido que a mano."),
        ("{F} Según los apartados de sociedad medieval y moderna de la ficha, ¿qué figura de poder aparece en ambos periodos?", "Los reyes", "La ficha menciona reyes en la sociedad medieval y reyes con más poder en la moderna."),
        ("{F} La explicación de la clase presenta cuatro cambios clave para comparar sociedades. ¿Cuál no es uno de ellos? A) La ruptura de la unidad religiosa B) La Revolución Industrial", "B) La Revolución Industrial", "No es uno de los cuatro cambios y ocurre después, en el siglo XVIII."),
    ],
    ctx=("Un compañero de otro curso dice: «En 1500 la gente ya vivía en una sociedad totalmente moderna». Con la ficha, ¿qué le responderías? {F}", "Que en 1500 todavía no había empezado la Reforma (1517) ni se había publicado a Copérnico (1543)", "Varios cambios clave ocurren después de 1500, así que la transición continuó."),
    sc=[("¿Qué aparece hacia 1450 y ayuda a difundir ideas?", "La imprenta", "Es el invento de Gutenberg."),
        ("¿En qué año se publica la obra de Copérnico según la ficha?", "1543", "Es el año del hito científico."),
        ("¿Fue la transición medieval-moderna un cambio de un día para otro? A) Sí B) No, fue gradual y con continuidades", "B) No, fue gradual y con continuidades", "Los hitos se reparten entre 1450 y 1687.")],
    op=("Dibuja una línea de tiempo entre 1450 y 1700 con escala 1 cm = 50 años y marca los seis hitos de la ficha con rayas y nombres. Debajo escribe dos frases: una sobre un cambio y otra sobre una continuidad entre la sociedad medieval y la moderna. {F}",
        "Imprenta a 0 cm, Granada y Colón a 0,8 cm, Lutero a 1,3 cm, Enrique VIII a 1,7 cm, Copérnico a 1,9 cm, Newton a 4,7 cm. Cambio: la imprenta facilita difundir ideas. Continuidad: la religión cristiana sigue siendo importante.",
        ["usa la escala", "ubica los seis hitos", "escribe un cambio y una continuidad"], ["línea de tiempo", "dos frases"], ["no respetar la escala", "decir que todo cambió"],
        "Pide que explique por qué Newton queda tan lejos de Lutero en la línea."),
    reinforce="Menciona oralmente los cuatro cambios del OA y un año de la ficha para al menos tres de ellos.",
    extend="Escribe una pregunta que un historiador haría para saber si la Reforma llegó igual a todas las regiones de Europa.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuente de ejemplo escrita para este cuaderno; no es un documento histórico real). Carta de un impresor de Venecia a un comerciante de libros, 1500: «Con mi prensa produzco 200 ejemplares de un libro en tres meses. "
     "Un copista, escribiendo a mano, hace un solo ejemplar en seis meses. Por eso mis libros cuestan menos y llegan a más lectores. Mi taller imprime también escritos de religiosos que critican a la Iglesia, y los vendo bien.» ")
build(
    OA, 2, F,
    use="Aprenderé a analizar una fuente sobre la imprenta, a distinguir lo que dice de lo que interpreto y a calcular qué cambió en la difusión del conocimiento.",
    prior=["Sé contextualizar una fuente.", "Sé distinguir descripción e interpretación.", "Sé hacer divisiones simples."],
    explain=[
        "La imprenta de tipos móviles de Gutenberg, creada hacia 1450, permitió fabricar muchos ejemplares de un mismo texto con rapidez. Antes, los libros se copiaban a mano, sobre todo en monasterios o por copistas, y por eso eran escasos y caros. Con la imprenta aumentó la cantidad de libros, bajó su precio y creció el número de lectores.",
        "Para analizar una fuente sobre la imprenta hay que contextualizarla. Quien escribe una carta de ejemplo como la de la ficha es un impresor, que gana dinero vendiendo libros; por eso puede exagerar las ventajas de su negocio. Su carta describe su taller, pero no prueba que todos los talleres de Europa fueran iguales.",
        "La imprenta tuvo efectos sobre la difusión de ideas. Facilitó que textos humanistas, religiosos y científicos circularan más allá de las ciudades donde nacían. No garantizó que todos supieran leer: muchas personas aún no tenían acceso a la lectura. El cambio fue importante, pero también tuvo límites.",
    ],
    vocab=[("imprenta", "máquina que reproduce textos con letras móviles, creada hacia 1450"), ("copista", "persona que copiaba libros a mano antes de la imprenta"), ("ejemplar", "cada copia de un mismo libro"), ("difusión", "proceso por el que algo llega a más personas y lugares"), ("lector", "persona que lee un texto")],
    worked=[
        ("Calcular rapidez de producción", "Otro taller de ejemplo imprime 240 ejemplares en 3 meses. ¿Cuántos ejemplares por mes?", ["Divido el total entre los meses.", "240 ÷ 3 = 80."], "80 ejemplares por mes"),
        ("Descubrir un sesgo", "El autor de la carta vende libros. ¿Por qué hay que leer su afirmación «mis libros cuestan menos» con cuidado?", ["Un vendedor quiere atraer compradores.", "Puede destacar ventajas y callar problemas."], "Porque el autor tiene interés comercial"),
    ],
    mistakes=[("Creer todo lo que dice un impresor sobre su propio negocio.", "Tiene interés en mostrar su taller como el mejor.", "Contrasta con otra fuente, como un registro de precios, antes de generalizar."),
              ("Pensar que con la imprenta todos aprendieron a leer.", "Se confunde disponer de libros con saber leer.", "Recuerda que muchas personas aún no tenían acceso a la lectura.")],
    T=[
        ("{F} ¿Quién escribió la carta y en qué año?", "Un impresor de Venecia, en 1500", "La ficha lo dice al comienzo."),
        ("{F} ¿Cuántos ejemplares de un libro produce el taller en tres meses?", "200 ejemplares", "El impresor lo afirma en su carta."),
        ("{F} ¿Cuántos ejemplares hace un copista en seis meses?", "Uno", "La carta lo indica."),
        ("=", "{F} Si el taller mantiene ese ritmo, ¿cuántos ejemplares imprime en un año de doce meses?", "200*4", "En un año hay cuatro periodos de tres meses.", " ejemplares"),
        ("=", "{F} Un copista tarda seis meses en hacer un ejemplar. ¿Cuántos meses tardaría en hacer cuatro?", "6*4", "Se multiplica el tiempo de un ejemplar por la cantidad.", " meses"),
        ("{F} ¿Por qué los libros impresos costaban menos que los copiados a mano según la carta? A) Porque se producían muchos ejemplares con menos trabajo B) Porque los libros impresos eran más pequeños y tenían menos páginas", "A) Porque se producían muchos ejemplares con menos trabajo", "La carta compara 200 ejemplares en tres meses con uno en seis."),
        ("{F} Clasifica: (1) «El taller imprime escritos religiosos críticos con la Iglesia» (2) «Toda Venecia leía folletos críticos». ¿Cuál es descripción y cuál es una generalización?", "La (1) es descripción y la (2) es una generalización", "La carta habla del taller, no de toda Venecia."),
        ("{F} ¿Qué efecto tuvo la imprenta en la difusión de ideas, según la carta? A) Textos críticos circulaban y llegaban a más lectores B) Se prohibió imprimir libros", "A) Textos críticos circulaban y llegaban a más lectores", "El impresor menciona que vende escritos críticos a más lectores."),
        ("=", "{F} Si el copista produjera un ejemplar cada seis meses durante un año, ¿cuántos ejemplares haría?", "12//6", "Un año tiene doce meses y cada ejemplar tarda seis.", " ejemplares"),
        ("{F} Un compañero concluye: «Con la imprenta, en 1500 todos los europeos sabían leer». ¿Qué falla?", "La carta no habla de la capacidad de leer de la población y muchas personas no sabían leer", "Tener libros baratos no equivale a saber leer."),
        ("{F} El autor es dueño del taller. ¿Qué interés puede tener al decir «mis libros cuestan menos»?", "Atraer compradores y vender más", "Su ganancia depende de las ventas."),
        ("{F} ¿Qué otra fuente ayudaría a comprobar el precio de los libros? A) Un registro de ventas de una librería de la época B) Otra carta del mismo impresor que repite que sus libros son baratos", "A) Un registro de ventas de una librería de la época", "Un registro muestra precios reales, no una opinión."),
        ("{F} ¿Qué efecto de la imprenta muestra la carta sobre el conocimiento en la sociedad moderna?", "Que las ideas se difunden más rápido y llegan a más lectores", "El taller produce más ejemplares en menos tiempo que un copista."),
    ],
    ctx=("Un maestro quiere explicar a su curso por qué la imprenta influyó en la Reforma. Con la ficha, ¿qué relación puede señalar? {F}", "El taller imprimía escritos críticos con la Iglesia y los vendía a más lectores, lo que facilitó que esas ideas circularan", "La carta conecta imprenta, difusión y textos religiosos críticos."),
    sc=[("¿Qué reemplazó la imprenta en la producción de libros?", "La copia a mano", "Antes de la imprenta los libros se copiaban a mano."),
        ("¿Por qué hay que leer con cuidado la carta de un impresor?", "Porque tiene interés comercial en mostrar su taller como el mejor", "Su ganancia depende de vender libros."),
        ("=", "Un taller imprime 120 ejemplares al mes. ¿Cuántos imprime en 4 meses?", "120*4", "Se multiplica la producción mensual por los meses.", " ejemplares")],
    op=("Escribe una carta breve de seis líneas, desde la perspectiva de un lector de una ciudad pequeña en 1500, que cuente cómo cambió su vida ahora que los libros cuestan menos. Usa dos datos de la ficha y termina con una frase que reconozca un límite (por ejemplo, que no todos saben leer). {F}",
        "Querido amigo: un impresor de Venecia vende libros más baratos; un copista tarda seis meses en hacer uno y su prensa hace 200 en tres meses. Aun así, mi vecino no sabe leer y no puede aprovecharlos.",
        ["usa dos datos de la ficha", "la carta tiene perspectiva de lector", "incluye un límite"], ["carta escrita"], ["inventar datos que contradicen la ficha", "decir que todos aprendieron a leer"],
        "Pide que explique de dónde sacó cada dato de su carta."),
    reinforce="Explica a una persona de tu casa qué cambió cuando se pasó de copiar libros a mano a imprimirlos.",
    extend="Escribe una pregunta que le harías a un copista de 1450 sobre la llegada de la imprenta.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (mapa religioso de Europa hacia 1560, simplificado). Católicos: España, Portugal, la mayor parte de Italia, la mayor parte de Francia y Polonia. "
     "Luteranos: el norte de Alemania, Suecia y Dinamarca. Anglicanos: Inglaterra. Calvinistas: Ginebra y zonas de Escocia, de los Países Bajos y de Francia. "
     "Continuidades: en todos esos territorios la religión era cristiana y las monarquías o los príncipes seguían gobernando; la mayoría de la población vivía en el campo.")
build(
    OA, 3, F,
    use="Aprenderé a describir cómo se rompió la unidad religiosa de Europa en el territorio y qué continuó igual a pesar de esa ruptura.",
    prior=["Sé ubicar países europeos en un mapa.", "Sé distinguir cambio y continuidad.", "Conozco las 95 tesis de Lutero y la fecha de 1517."],
    explain=[
        "Durante la Edad Media, en Europa occidental había una sola Iglesia cristiana, la católica, con el papa como cabeza. Esa unidad religiosa se rompió en el siglo XVI con la Reforma. Lutero cuestionó prácticas de la Iglesia, como la venta de indulgencias, y sus ideas se difundieron con ayuda de la imprenta. Surgieron así nuevas iglesias: la luterana, la calvinista y la anglicana.",
        "El territorio muestra cómo se dividió Europa. Hacia 1560, el norte de Alemania, Suecia, Dinamarca e Inglaterra se separaron de Roma, mientras que España, Portugal y gran parte de Italia y de Francia siguieron católicas. La Reforma avanzó donde los gobernantes la apoyaron, y por eso muchas fronteras religiosas coincidieron con fronteras políticas.",
        "Aun con esta ruptura hubo continuidades: todos eran cristianos, los reyes y príncipes seguían gobernando y la mayoría vivía de la agricultura. La unidad religiosa se rompió, pero la religión siguió siendo central en la vida europea.",
    ],
    vocab=[("indulgencia", "documento que la Iglesia concedía para reducir castigos por pecados y que algunos vendían"), ("luterano", "seguidor de las ideas de Martín Lutero"), ("calvinista", "seguidor de las ideas de Juan Calvino"), ("anglicano", "miembro de la Iglesia de Inglaterra, encabezada por el rey"), ("unidad religiosa", "situación en que todos los habitantes pertenecen a una misma Iglesia")],
    worked=[
        ("Leer un mapa religioso", "Según la ficha, ¿qué países de Europa del sur se mantienen católicos?", ["Miro la lista de católicos.", "España, Portugal e Italia aparecen ahí."], "España, Portugal y la mayor parte de Italia"),
        ("Identificar continuidad", "En un reino luterano de 1560, ¿qué continuó igual respecto de la Edad Media?", ["Los príncipes seguían gobernando.", "La religión seguía siendo cristiana."], "El gobierno de príncipes o reyes y la religión cristiana"),
    ],
    mistakes=[("Pensar que Europa dejó de ser cristiana con la Reforma.", "Se confunde ruptura de la unidad con abandono de la religión.", "Recuerda que todas las iglesias eran cristianas."),
              ("Creer que toda Europa se volvió protestante.", "Se ignora que España, Portugal e Italia siguieron católicas.", "Revisa el mapa y nombra territorios católicos y protestantes.")],
    T=[
        ("{F} ¿Qué Iglesia encabezaba el rey en Inglaterra?", "La anglicana", "La ficha ubica a los anglicanos en Inglaterra."),
        ("{F} ¿Qué territorios eran luteranos hacia 1560?", "El norte de Alemania, Suecia y Dinamarca", "La ficha los menciona."),
        ("{F} ¿Qué ciudad se asocia a los calvinistas?", "Ginebra", "Aparece en la lista de calvinistas."),
        ("=", "{F} La Reforma comenzó en 1517 y el mapa de la ficha es de 1560. ¿Cuántos años pasaron?", "1560-1517", "Se resta el año de inicio de la Reforma al del mapa.", " años"),
        ("{F} ¿Dónde se mantuvo la unidad católica hacia 1560: España o Suecia?", "España", "Suecia es luterana según la ficha."),
        ("{F} ¿Qué continuidad aparece en todos los territorios de la ficha?", "La religión cristiana, los gobernantes y la vida en el campo", "La ficha las menciona como continuidades."),
        ("{F} Un mapa muestra Inglaterra de verde y España de azul. ¿Qué podrían representar los colores? A) Inglaterra anglicana y España católica B) Ambas luteranas", "A) Inglaterra anglicana y España católica", "Según la ficha, son confesiones distintas."),
        ("{F} ¿Por qué se dice que las fronteras religiosas coincidían con fronteras políticas?", "Porque la Reforma avanzó donde los gobernantes la apoyaron", "Los príncipes y reyes decidían qué Iglesia seguir en su territorio."),
        ("{F} Clasifica como cambio o continuidad: a) hay varias iglesias cristianas, b) los reyes siguen gobernando, c) la mayoría vive en el campo.", "a) cambio; b) continuidad; c) continuidad", "Lo nuevo es la división religiosa."),
        ("{F} Un compañero dice: «Con la Reforma, toda Europa dejó de creer en Dios». ¿Cómo lo corriges?", "La ficha muestra iglesias cristianas distintas, no abandono de la religión", "La Reforma dividió a los cristianos, no los hizo dejar de creer."),
        ("{F} ¿Qué región de la ficha mezcla calvinistas y católicos dentro del mismo país?", "Francia", "Hay zonas calvinistas de Francia aunque la mayor parte sea católica."),
        ("{F} ¿Qué pregunta histórica nueva surge al ver el mapa? A) ¿Por qué algunos gobernantes apoyaron la Reforma y otros no? B) ¿Cuántos habitantes tenía Ginebra?", "A) ¿Por qué algunos gobernantes apoyaron la Reforma y otros no?", "El mapa muestra decisiones políticas distintas."),
        ("{F} ¿Qué te dice el mapa sobre el ritmo del cambio religioso?", "Que no fue igual en todos los lugares: unos territorios cambiaron y otros no", "Hay territorios católicos y protestantes hacia 1560."),
    ],
    ctx=("Una estudiante dice: «En 1560 todos los habitantes de Europa occidental eran católicos, como en la Edad Media». Con la ficha, ¿cómo le respondes? {F}", "Hacia 1560 había luteranos, calvinistas y anglicanos además de católicos, así que la unidad religiosa se había roto", "El mapa muestra varios territorios no católicos."),
    sc=[("¿Qué cambio religioso ocurrió en Europa en el siglo XVI?", "La ruptura de la unidad religiosa", "Surgieron nuevas iglesias cristianas."),
        ("¿Qué territorio es anglicano?", "Inglaterra", "La ficha lo ubica ahí."),
        ("¿Qué continuó igual en 1560? A) La religión cristiana B) Una sola Iglesia", "A) La religión cristiana", "Todas las iglesias eran cristianas.")],
    op=("Dibuja un mapa sencillo de Europa (puede ser un croquis) y pinta con tres colores los territorios católicos, luteranos y anglicanos de la ficha. Escribe una leyenda y una frase que explique una continuidad. {F}",
        "Católicos: España, Portugal, Italia, Francia, Polonia. Luteranos: norte de Alemania, Suecia, Dinamarca. Anglicanos: Inglaterra. Continuidad: todos eran cristianos.",
        ["usa tres colores", "la leyenda coincide con la ficha", "explica una continuidad"], ["mapa con leyenda", "frase"], ["pintar toda Europa del mismo color", "no escribir ninguna continuidad"],
        "Pide que explique por qué decidió colocar un territorio en un color."),
    reinforce="Nombra un país católico, uno luterano y uno anglicano de la ficha.",
    extend="Escribe qué información te faltaría para saber si dentro de un mismo país todos pensaban igual.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; no son textos históricos reales). "
     "Voz 1, monje y profesor alemán, 1517: «La Iglesia no debe vender perdones; la fe y la Biblia son lo central.» "
     "Voz 2, obispo, 1518: «Estas críticas rompen la unidad de los fieles y desobedecen al papa.» "
     "Voz 3, príncipe alemán, 1521: «Apoyo la nueva predicación; así mi territorio dependerá menos de Roma.» "
     "Voz 4, astrónomo, 1610: «Con el telescopio veo lunas alrededor de Júpiter; la Tierra no es el centro de todos los giros.» "
     "Voz 5, teólogo de la Inquisición, 1633: «Enseñar que la Tierra se mueve contradice la interpretación tradicional de la Biblia y debe ser corregido.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar las perspectivas de quienes defendían la unidad religiosa y de quienes propusieron cambios en la religión y la ciencia, y a explicar sus causas.",
    prior=["Sé reconocer actores y perspectivas.", "Sé que una explicación puede tener varias causas.", "Conozco la Reforma y la revolución científica."],
    explain=[
        "Los cambios entre la sociedad medieval y la moderna provocaron conflictos entre actores. En la Reforma, un monje como Lutero criticó la venta de indulgencias; un obispo defendió la autoridad del papa y un príncipe apoyó la nueva predicación porque le convenía políticamente. Un mismo hecho tenía interpretaciones distintas según la posición de cada actor.",
        "En la revolución científica, un astrónomo como Galileo defendió con observaciones que la Tierra se mueve y no es el centro de todos los giros. Un teólogo del tribunal de la Inquisición, institución de la Iglesia que vigilaba la fe, lo juzgó en 1633 por contradecir una interpretación tradicional de la Biblia. Aquí chocaban dos formas de conocer: la autoridad antigua y la observación.",
        "Al contrastar voces hay que fijarse en causas distintas: religiosas, políticas y de conocimiento. El apoyo de un príncipe tenía una razón política; la crítica de Lutero, una razón religiosa. Ninguna voz cuenta toda la historia, y la explicación más completa las combina.",
    ],
    vocab=[("Inquisición", "tribunal de la Iglesia que vigilaba y juzgaba cuestiones de fe"), ("telescopio", "instrumento que acerca la imagen de objetos lejanos"), ("autoridad", "persona o texto cuya palabra se acepta como verdad"), ("observación", "mirada atenta a un hecho para obtener datos"), ("perspectiva", "punto de vista según la posición de cada actor")],
    worked=[
        ("Distinguir la razón de cada actor", "En la ficha, ¿por qué el príncipe apoya la nueva predicación?", ["Leo la voz 3.", "Dice que así dependerá menos de Roma."], "Por una razón política: depender menos de Roma"),
        ("Contrastar dos voces", "La voz 4 y la voz 5, ¿qué forma de conocer defiende cada una?", ["El astrónomo usa el telescopio y observa.", "El teólogo se apoya en una interpretación tradicional."], "El astrónomo, la observación; el teólogo, la autoridad tradicional"),
    ],
    mistakes=[("Decir que todos los católicos rechazaron la ciencia.", "Se generaliza desde un caso, el de un tribunal.", "Recuerda que había creyentes que hacían ciencia y que cada actor tenía sus razones."),
              ("Explicar la Reforma solo por la ambición de los príncipes.", "Se ignora la crítica religiosa de Lutero.", "Combina razones religiosas, políticas y culturales.")],
    T=[
        ("{F} ¿Quién dice que la fe y la Biblia son lo central?", "El monje y profesor alemán", "Es la voz 1."),
        ("{F} ¿Qué defiende el obispo en la voz 2?", "La unidad de los fieles y la obediencia al papa", "La voz 2 lo expresa."),
        ("{F} ¿Qué instrumento usa el astrónomo?", "El telescopio", "La voz 4 lo menciona."),
        ("=", "{F} ¿Cuántos años pasaron entre la voz del astrónomo (1610) y la del teólogo de la Inquisición (1633)?", "1633-1610", "Se resta el año de la primera voz al de la segunda.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la voz del monje (1517) y la del príncipe (1521)?", "1521-1517", "Se restan los años de ambas voces.", " años"),
        ("{F} ¿Cuál es la razón del príncipe: A) política, depender menos de Roma B) científica, observar lunas", "A) política, depender menos de Roma", "Su voz habla de poder, no de ciencia."),
        ("{F} ¿Qué forma de conocer defiende el astrónomo: la autoridad de textos antiguos o la observación?", "La observación", "Dice que con el telescopio ve lunas alrededor de Júpiter."),
        ("{F} Ordena las voces de la más antigua a la más reciente: teólogo, obispo, astrónomo, monje.", "Monje, obispo, astrónomo, teólogo", "Los años son 1517, 1518, 1610 y 1633."),
        ("{F} ¿Qué voces de la ficha defienden mantener lo establecido? A) La del obispo y la del teólogo B) La del monje y la del astrónomo", "A) La del obispo y la del teólogo", "Ambos defienden la autoridad tradicional."),
        ("{F} Un compañero dice: «El príncipe apoyó la Reforma solo por fe sincera». ¿Qué dato de la ficha lo contradice?", "El príncipe habla de depender menos de Roma, una razón política", "La voz 3 muestra un interés político."),
        ("{F} ¿Qué tienen en común el monje y el astrónomo respecto de la autoridad tradicional?", "Ambos la cuestionan con razones propias, uno con la Biblia y otro con observaciones", "Cada uno propone otra base para conocer."),
        ("{F} ¿Por qué ninguna voz cuenta toda la historia?", "Porque cada una habla desde su posición y faltan otras voces, como las de campesinos", "Las perspectivas son parciales."),
        ("{F} ¿Qué pregunta ayuda a explicar el conflicto entre el astrónomo y el teólogo? A) ¿Qué fuente de verdad aceptaba cada uno? B) ¿Cuántos libros se imprimieron en 1633?", "A) ¿Qué fuente de verdad aceptaba cada uno?", "El conflicto era sobre cómo se conoce la verdad."),
    ],
    ctx=("Un profesor propone un debate entre el astrónomo (1610) y el teólogo (1633) de la ficha. ¿Qué argumento sacaría cada uno? {F}", "El astrónomo, que su observación con el telescopio muestra lunas alrededor de Júpiter; el teólogo, que moverse la Tierra contradice la interpretación tradicional", "Cada uno defiende su forma de conocer."),
    sc=[("¿Qué tribunal de la Iglesia vigilaba la fe?", "La Inquisición", "Se definió en el vocabulario."),
        ("¿Qué actor buscaba depender menos de Roma al apoyar la nueva predicación?", "El príncipe alemán", "Era su razón política."),
        ("¿Qué observó el astrónomo con el telescopio? A) Lunas alrededor de Júpiter B) Un nuevo continente", "A) Lunas alrededor de Júpiter", "Lo dice en la voz 4.")],
    op=("Escribe un diálogo de seis líneas entre el monje y el obispo de la ficha. En tres líneas el monje critica la venta de perdones y en tres el obispo defiende la unidad. Usa una frase de la ficha en cada voz y termina con una frase tuya que explique en qué se separan sus perspectivas. {F}",
        "Monje: la Iglesia no debe vender perdones. Obispo: las críticas rompen la unidad de los fieles. Cierre: el monje pone la fe y la Biblia al centro y el obispo pone la obediencia al papa.",
        ["usa frases de la ficha", "respeta las dos perspectivas", "cierra contrastando"], ["diálogo", "frase de cierre"], ["poner a un personaje de acuerdo con el otro sin evidencia", "inventar datos"],
        "Pide que explique qué razón política podría haber detrás de un apoyo."),
    reinforce="Cuéntale a alguien de tu casa qué defendía cada una de las voces 1, 2 y 4.",
    extend="Escribe la voz de una persona campesina de 1520 ante estos debates; solo una pregunta.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (pregunta y datos de ejemplo). Pregunta: ¿qué cambio fue más decisivo para pasar de la sociedad medieval a la moderna? "
     "Cadena de hechos de la ficha: (1) la imprenta, hacia 1450, permite copiar textos rápido; (2) con ella circulan las 95 tesis de Lutero desde 1517; (3) con ella circulan también obras científicas como la de Copérnico, en 1543; "
     "(4) la Reforma divide a los cristianos de Europa; (5) los reyes de Inglaterra, España y Francia fortalecen sus Estados mientras tanto. "
     "Criterio de la clase: un cambio es «más decisivo» si hizo posibles otros cambios.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre qué cambio fue más decisivo en el paso de la sociedad medieval a la moderna, usando un criterio explícito y evidencias.",
    prior=["Sé que un argumento tiene tesis, evidencias y límite.", "Conozco los cuatro cambios del OA.", "Sé calcular diferencias de años."],
    explain=[
        "Para elegir cuál cambio fue más decisivo hay que definir un criterio. En esta clase el criterio es: un cambio es más decisivo si hizo posibles otros cambios. Con ese criterio, la imprenta (hecho 1) aparece además como medio de difusión en otros dos de los cinco hechos de la ficha, el 2 y el 3, porque ayudó a difundir las tesis de Lutero y las obras de ciencia. Eso la convierte en una candidata fuerte.",
        "Un argumento sólido propone una tesis, cita evidencias y reconoce límites. Por ejemplo: «La imprenta fue muy decisiva porque difundió ideas de la Reforma y de la ciencia, aunque sin los reyes que protegieron o prohibieron libros su efecto habría sido distinto». Ese límite muestra que ningún cambio explica todo por sí solo.",
        "Elegir un cambio no significa borrar los demás. La Reforma, el Estado centralizado y la revolución científica también cambiaron mucho a la sociedad. Un buen argumento compara con un criterio y deja claro hasta dónde llegan sus pruebas.",
    ],
    vocab=[("criterio", "regla que se usa para comparar y decidir"), ("decisivo", "que tiene un efecto clave sobre otros hechos"), ("argumento", "tesis apoyada en evidencias y razones"), ("límite", "lo que la evidencia no permite concluir"), ("cadena de hechos", "serie de hechos donde unos influyen en otros")],
    worked=[
        ("Aplicar un criterio", "Con el criterio de la clase, ¿en cuántos de los cinco hechos de la ficha aparece la imprenta como medio que hace circular ideas, sin contar el hecho 1, que es la propia imprenta?", ["Busco «con ella circulan»: hechos 2 y 3.", "Cuento dos hechos."], "En 2 hechos"),
        ("Redactar un límite", "Tesis: «La imprenta explica la Reforma». ¿Qué límite honesto agregarías?", ["La Reforma también tuvo causas religiosas y políticas.", "Los príncipes que la apoyaron tuvieron un papel clave."], "La imprenta ayudó, pero no fue la única causa; los príncipes también influyeron"),
    ],
    mistakes=[("Elegir un cambio sin explicar el criterio.", "No se sabe por qué es más importante que los demás.", "Escribe primero el criterio y luego compara."),
              ("Decir que un cambio explica todo por sí solo.", "Se ignora la multicausalidad.", "Añade un límite que nombre otras causas.")],
    T=[
        ("{F} ¿Qué cambio aparece como punto de partida de la cadena de hechos?", "La imprenta", "El hecho 1 es la imprenta."),
        ("{F} ¿Qué criterio usa la clase para decir que un cambio es más decisivo?", "Que hizo posibles otros cambios", "Está escrito al final de la ficha."),
        ("=", "{F} ¿Cuántos años pasaron entre la imprenta (hacia 1450) y la obra de Copérnico (1543)?", "1543-1450", "Se resta el año de la imprenta al de la obra.", " años"),
        ("{F} ¿En cuántos de los cinco hechos de la cadena participa la imprenta como medio de difusión?", "En dos: las tesis de Lutero y las obras científicas", "Los hechos 2 y 3 dicen «con ella circulan»."),
        ("{F} Clasifica cada hecho en religioso, científico o político: a) las 95 tesis de Lutero, b) la obra de Copérnico, c) los reyes fortalecen sus Estados.", "a) religioso; b) científico; c) político", "Cada hecho pertenece a un ámbito distinto."),
        ("{F} ¿Qué tesis se apoya mejor en la ficha con el criterio de la clase? A) La imprenta fue muy decisiva porque difundió ideas de la Reforma y de la ciencia B) La imprenta fue irrelevante porque solo copiaba libros ya conocidos", "A) La imprenta fue muy decisiva porque difundió ideas de la Reforma y de la ciencia", "La ficha muestra que ayudó a difundir ambos tipos de ideas."),
        ("{F} Un compañero dice: «La Reforma fue lo más decisivo porque dividió a los cristianos». ¿Qué le falta para usar el criterio de la clase?", "Mostrar que la Reforma hizo posibles otros cambios", "El criterio no es cuán grande fue el hecho, sino cuántos otros hizo posibles."),
        ("{F} ¿Qué hecho de la cadena podría usarse para decir que el Estado también fue importante?", "El hecho 5, donde los reyes fortalecen sus Estados", "Muestra otro cambio que ocurre mientras tanto."),
        ("{F} ¿Qué hecho de la cadena muestra que la imprenta ya existía cuando circularon las tesis de Lutero?", "El hecho 1: la imprenta es de hacia 1450, antes de 1517", "La imprenta es anterior a las tesis."),
        ("{F} Escribe un límite para la tesis «la imprenta fue lo más decisivo».", "Sin protectores políticos o personas que quisieran leer, la imprenta no habría tenido el mismo efecto", "Ningún cambio actúa solo."),
        ("{F} ¿Qué evidencia usarías para defender que la ciencia fue importante? A) La difusión de la obra de Copérnico en 1543 B) La lista de reyes de Francia", "A) La difusión de la obra de Copérnico en 1543", "Muestra circulación de ideas científicas."),
        ("{F} ¿Por qué ninguna elección es definitiva?", "Porque depende del criterio que se elija y de las fuentes que se usen", "Con otro criterio, otro cambio podría ser el más decisivo."),
        ("{F} Con el criterio de la clase, ¿es correcto decir que la imprenta fue decisiva porque costó poco dinero?", "No, porque el criterio es haber hecho posibles otros cambios", "El costo no es el criterio de la clase."),
    ],
    ctx=("Para una exposición, un grupo debe elegir qué cambio poner en el centro del afiche «Del Medioevo a la modernidad». Con el criterio de la ficha, ¿qué elegirían y por qué? {F}", "La imprenta, porque aparece en dos hechos como medio de difusión y hizo posibles otros cambios", "Cumple el criterio explícito de la clase."),
    sc=[("En Historia: ¿Qué es un criterio?", "Una regla para comparar y decidir", "Así se definió."),
        ("¿Qué hecho de la ficha es político?", "Los reyes fortalecen sus Estados", "Es el hecho 5."),
        ("=", "La imprenta es de hacia 1450 y las tesis de Lutero de 1517. ¿Cuántos años pasaron?", "1517-1450", "Se resta el año de la imprenta al de las tesis.", " años")],
    op=("Escribe un párrafo de seis líneas con tu tesis sobre cuál cambio fue más decisivo. Debes decir tu criterio, citar dos hechos numerados de la ficha como evidencias y cerrar con un límite. Puedes elegir cualquiera de los cuatro cambios del OA. {F}",
        "Pienso que la imprenta fue muy decisiva. Criterio: hizo posibles otros cambios. Hecho 2: las tesis de Lutero circularon. Hecho 3: las obras científicas circularon. Límite: sin protección política su efecto habría sido distinto.",
        ["declara el criterio", "cita dos hechos numerados", "incluye un límite"], ["párrafo escrito"], ["no declarar el criterio", "citar hechos que no están en la ficha"],
        "Pide que explique qué pasaría con su tesis si cambiara el criterio."),
    reinforce="Explica oralmente por qué es importante decir el criterio antes de comparar cambios.",
    extend="Propón otro criterio, por ejemplo cuántas personas afectó, y di si cambiaría tu elección.",
)
