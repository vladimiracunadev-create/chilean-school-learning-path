"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 12 (ambientes naturales de Chile) y OA 13 (región y localidad)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA12, OA13 = "HI06 OA 12", "HI06 OA 13"
MAT = "Este cuaderno y un lápiz. Los mapas, tablas y textos que se usan están escritos en cada ejercicio."


def _e(items):
    return [i if isinstance(i, dict) else ex(*i) for i in items]


def lesson(oa, n, use, prior, explain, vocab, worked, mistakes, r, c, a, z, h, ctx, sc, op, reinforce, extend, materials=MAT):
    """Registra una clase con datos compactos: ejercicios como tuplas (enunciado, respuesta, porqué) o resultados de arith."""
    register(
        oa, n,
        materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": an} for t, p, s, an in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": _e(r), "understand": _e(c), "apply": _e(a), "reason": _e(z), "challenge": _e(h)},
        context=_e(ctx), selfcheck=_e(sc), open_task=task(*op), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 12 · clase 1
lesson(
    OA12, 1,
    "Aprenderé a ubicar en el mapa los ocho ambientes naturales de Chile y a reconocerlos por su clima y su altura. Sirve para saber dónde ocurre cada oportunidad o dificultad que veremos después.",
    ["Sé que Chile es largo y angosto y que el norte queda arriba en un mapa.", "Sé que la altura y la lluvia cambian el paisaje."],
    [
        "Un ambiente natural es un lugar con un clima, un relieve, plantas y animales propios. Chile tiene ocho: desértico, altiplánico, costero, mediterráneo, andino, frío y lluvioso, patagónico y polar. Cambian porque el país es muy largo, porque hay mar en el oeste y cordillera en el este, y porque el terreno sube y baja.",
        "De norte a sur se ubican así: el desértico (muy poca lluvia) y el altiplánico (planicie muy alta, sobre los 3.000 metros) están en el norte; el mediterráneo (veranos secos e inviernos con lluvia) está en el centro; el frío y lluvioso está en el sur; el patagónico (viento fuerte y estepa) está en el extremo sur; y el polar (hielo) está en la Antártica Chilena, aún más al sur.",
        "Dos ambientes no se miden de norte a sur sino de oeste a este. El costero está junto al mar y recorre casi todo el país. El andino es la cordillera de los Andes, con montañas y nieve, y también recorre el país. Los pueblos originarios, como el aymara en el altiplano o el mapuche en el centro-sur, vivieron en estos ambientes mucho antes de que existiera el Estado de Chile.",
    ],
    [("ambiente natural", "lugar con clima, relieve, plantas y animales propios"), ("clima", "tiempo que se repite en un lugar durante muchos años"), ("altiplano", "planicie muy alta del norte, entre cordilleras"), ("estepa", "terreno plano de pastos duros con viento fuerte"), ("cordillera", "cadena larga de montañas")],
    [
        ("Ubicar con pistas", "Ficha del lugar H: está en el extremo sur, hay viento muy fuerte, estepa con pastos y se crían ovejas. ¿Qué ambiente es?", ["Extremo sur: patagónico o polar.", "Hay estepa, ovejas y viento: no hay hielo permanente.", "Corresponde al patagónico."], "Patagónico"),
        ("Ordenar de norte a sur", "Ordena de norte a sur: mediterráneo, desértico, frío y lluvioso.", ["El desértico está en el norte.", "El mediterráneo está en el centro.", "El frío y lluvioso está en el sur."], "Desértico, mediterráneo, frío y lluvioso"),
    ],
    [
        ("Creer que todo Chile tiene el mismo ambiente.", "El país es tan largo y tiene tanta altura que el clima y el paisaje cambian mucho.", "Ubica primero el lugar y luego el ambiente."),
        ("Confundir el altiplánico con el andino.", "El andino es toda la cordillera con nieve y montañas; el altiplánico es una planicie alta del norte.", "Pregunta si es montaña (andino) o planicie alta del norte (altiplánico)."),
    ],
    [
        ("En un mapa con el norte hacia arriba, ¿el ambiente desértico está en la parte de arriba o de abajo?", "Arriba", "El desierto de Atacama está en el norte de Chile."),
        ("¿El ambiente mediterráneo está en el norte, en el centro o en el extremo sur?", "En el centro", "La zona central tiene veranos secos e inviernos con lluvia."),
        ("¿Qué ambiente queda más al sur: el patagónico o el polar?", "El polar", "La Antártica Chilena está más al sur que la Patagonia."),
    ],
    [
        ("Un ambiente tiene veranos secos e inviernos con lluvia. ¿Cuál es?", "Mediterráneo", "Esa combinación de estaciones define al ambiente mediterráneo."),
        ("¿Por qué decimos que el andino y el altiplánico tienen que ver con la altura?", "Porque ambos están en lugares muy altos sobre el nivel del mar", "La cordillera y el altiplano están a gran altura."),
        ("El ambiente costero, ¿está solo en el norte o recorre casi todo el país?", "Recorre casi todo el país", "Chile tiene mar en todo su lado oeste."),
    ],
    [
        ("Ficha del lugar M: está en el norte, a más de 3.000 m de altura; de día hay sol y de noche hace mucho frío. ¿Su ambiente es altiplánico o costero?", "Altiplánico", "La planicie muy alta del norte es el altiplano."),
        ("Ficha del lugar N: está en el sur, llueve casi todo el año y hay bosques espesos. ¿Su ambiente es frío y lluvioso o desértico?", "Frío y lluvioso", "Un desierto casi no recibe lluvia."),
        arith("En un mapa de ejemplo la escala dice 1 cm = 400 km. Entre el desierto y el extremo sur hay 10 cm en el mapa. ¿Cuántos kilómetros reales separan esos dos puntos?", "10*400", "Cada centímetro vale 400 km, así que se multiplica por 10.", " km"),
    ],
    [
        ("Ana dice: «Todo Chile tiene el mismo ambiente porque es un solo país». ¿Qué error comete?", "Un país muy largo y con mar y cordillera cambia de ambiente de norte a sur y de oeste a este", "El clima y el relieve dependen de la ubicación, no del nombre del país."),
        ("Dos pueblos del norte: A está junto al mar y B está a 4.000 m de altura. ¿Cuál es altiplánico y por qué?", "B, porque está en una planicie muy alta", "El altiplano se define por su gran altura."),
    ],
    [
        ("Ordena de norte a sur: A) patagónico, B) desértico, C) mediterráneo, D) polar.", "B, C, A, D", "Desierto en el norte, centro, extremo sur y por último la Antártica."),
        ("Un viaje parte en la costa de la zona central y avanza hacia el este hasta lo más alto, con nieve. ¿Qué ambiente aparece al final?", "Andino", "Al este de la zona central se levanta la cordillera de los Andes."),
    ],
    [("Una familia viaja por tierra de norte a sur. Primero cruza un lugar casi sin lluvia, luego uno con veranos secos y por último bosques con lluvia casi todo el año. ¿Cuál es el ambiente del tramo del medio?", "Mediterráneo", "Los veranos secos con inviernos lluviosos son del centro de Chile.")],
    [("En Historia: ¿qué es un ambiente natural?", "Un lugar con clima, relieve, plantas y animales propios", "Así se definió en el vocabulario."), ("¿Por qué cambian los ambientes de Chile?", "Porque el país es muy largo y tiene mar, cordillera y distintas alturas", "Esos tres factores cambian el clima y el paisaje."), ("¿Cuál ambiente es una planicie alta del norte?", "Altiplánico", "El altiplano es una planicie a gran altura.")],
    (
        "Elige uno de estos dos viajes y escribe en orden los ambientes que cruza. Viaje 1: sale del mar en una ciudad del norte, avanza al este por el desierto y sube hasta un pueblo con llamas a 3.800 m. Viaje 2: sale de la costa de la zona central y avanza al este hasta un paso de la cordillera con nieve.",
        "Viaje 2: costero, mediterráneo, andino.",
        ["nombra al menos tres ambientes", "los escribe en el orden del viaje", "justifica uno con un rasgo (altura, lluvia o relieve)"],
        ["lista ordenada de ambientes con una frase de justificación"],
        ["poner el andino antes del costero", "confundir altiplánico con andino"],
        "Muestra tu lista a una persona de tu casa y pídele que siga el viaje con el dedo sobre un mapa de Chile.",
    ),
    "Mira un mapa de Chile y escribe en qué lugar ubicarías cada uno de los ocho ambientes.",
    "Escribe qué ambiente te gustaría visitar y dos rasgos que lo identifican.",
)

# ================================================================ OA 12 · clase 2
lesson(
    OA12, 2,
    "Aprenderé a leer fuentes sobre los ambientes de Chile y a preguntar quién las hizo y para qué. Sirve para no creer una afirmación solo porque suena bien.",
    ["Sé ubicar los ocho ambientes naturales de Chile.", "Sé que una fuente entrega información."],
    [
        "Para conocer un ambiente natural usamos fuentes: tablas con datos, informes, relatos de personas, fotografías y folletos. Cada una muestra una parte. Una tabla con la lluvia anual en milímetros (mm) permite comparar lugares. Un relato de un pastor de llamas cuenta cómo vive en el altiplano.",
        "La procedencia es quién hizo la fuente, cuándo y para qué. Un folleto de una agencia de turismo se hace para atraer visitantes y suele mostrar solo lo bonito. Un informe científico busca explicar con datos. Un relato cuenta lo que vivió una persona, no lo de todo el ambiente.",
        "Al leer, separamos lo que la fuente dice, lo que nosotros interpretamos y lo que no permite saber. Si una tabla muestra que en una ciudad del desierto llovió muy poco un año, no podemos concluir que nunca llueve en todo el desierto. Para eso faltan más lugares y más años.",
    ],
    [("fuente", "lo que entrega información sobre un tema"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("dato", "información concreta, como una cifra con su unidad"), ("milímetro de lluvia (mm)", "medida de cuánta agua cae sobre el suelo"), ("generalizar", "decir que algo vale para todos los casos con base en uno solo")],
    [
        ("Preguntar por la procedencia", "Un folleto de turismo del sur dice: «Aquí el paisaje es el mejor del mundo». ¿Qué pregunta conviene hacer?", ["Pregunto quién lo hizo y para qué.", "Lo hizo una agencia para atraer visitantes.", "«El mejor» es una opinión sin dato."], "Quién lo hizo y para qué; «el mejor» no tiene prueba"),
        ("Leer una tabla", "Tabla de ejemplo, lluvia anual: Lugar X, 8 mm; Lugar Y, 700 mm. ¿Cuál es más seco?", ["Comparo los dos números.", "8 es menor que 700.", "Menos lluvia significa más seco."], "El lugar X"),
    ],
    [
        ("Creer todo lo que dice un folleto de turismo.", "Se hizo para atraer visitantes y no suele mostrar las dificultades.", "Revisa quién lo hizo y busca otra fuente."),
        ("Concluir algo de todo un ambiente con un solo dato.", "Un lugar o un año no representan a todo el ambiente.", "Di solo lo que muestra esa fuente."),
    ],
    [
        ("Un folleto de una agencia de turismo, ¿se hizo para atraer visitantes o para medir la lluvia?", "Para atraer visitantes", "Su propósito es mostrar lo atractivo de un lugar."),
        ("«En este lugar llovieron 12 mm en un año», ¿es un dato o una opinión?", "Un dato", "Es una cifra con unidad que se puede comprobar."),
        ("El relato de un pastor de llamas cuenta lo que vive él. ¿Describe la vida de una persona o la de todo Chile?", "La vida de una persona", "Un relato muestra una experiencia particular."),
    ],
    [
        ("¿Por qué conviene mirar dos fuentes sobre el mismo ambiente?", "Porque cada una muestra una parte y se pueden contrastar", "Una sola fuente puede dejar cosas fuera."),
        ("Una tabla con la lluvia de cinco años en un lugar, ¿qué permite saber que no entrega una sola cifra?", "Si la lluvia cambió con los años", "Varios años permiten ver subidas o bajadas."),
        ("¿Qué significa «generalizar» con un solo dato?", "Decir que vale para todos los casos con base en uno", "Esa es la definición del vocabulario."),
    ],
    [
        ("Tabla de ejemplo, lluvia anual: P, 5 mm; Q, 350 mm; R, 2.500 mm; S, 600 mm. ¿Cuál de los cuatro lugares es el más lluvioso?", "R", "2.500 mm es la cifra mayor de la tabla."),
        arith("Con la misma tabla de ejemplo (Q, 350 mm; R, 2.500 mm), ¿cuántos milímetros más de lluvia anual tiene R que Q?", "2500-350", "Se resta la lluvia menor a la mayor.", " mm"),
        ("En la tabla de ejemplo (P, 5 mm; R, 2.500 mm), uno de los lugares es del desierto y otro del sur lluvioso. ¿Cuál corresponde al desierto?", "P", "El desierto recibe muy poca lluvia."),
    ],
    [
        ("Dos fuentes sobre el altiplano: un blog dice «Allí no vive nadie» y un informe cuenta que familias aymara crían llamas y alpacas en esa zona. ¿Cuál entrega evidencia más concreta y por qué?", "El informe, porque nombra quiénes viven allí y qué hacen", "El blog no da pruebas; el informe sí da hechos."),
        ("En una tabla de ejemplo, la ciudad T recibió 2 mm de lluvia en el año 2020. Pía concluye: «En todo el desierto no llueve nunca». ¿Qué falta para concluir eso?", "Datos de muchos lugares y de muchos años", "Una ciudad y un año no representan a todo el ambiente."),
    ],
    [
        ("Ordena los pasos para usar una fuente: A) decidir qué conclusión permite, B) anotar qué dato entrega, C) preguntar quién la hizo y para qué.", "C, B, A", "Primero la procedencia, luego el contenido y al final la conclusión."),
        ("Un folleto de un hotel dice «En el sur siempre hay sol». Una tabla de ejemplo muestra 2.000 mm de lluvia al año en un pueblo del sur. ¿Cuál de las dos fuentes sirve más para decidir si llevar paraguas: el folleto o la tabla?", "La tabla", "Entrega un dato medido; el folleto busca vender estadías."),
    ],
    [("Una agencia publica: «En el desierto todo es perfecto para vivir». Un vecino de un pueblo del desierto cuenta que el agua llega en camiones cada semana. ¿Qué fuente sirve para conocer las dificultades de ese ambiente: el aviso o el relato del vecino?", "El relato del vecino", "El aviso busca atraer visitantes y no cuenta los problemas.")],
    [("En Historia: ¿qué es la procedencia de una fuente?", "Quién la hizo, cuándo y para qué", "Es la definición de la clase."), ("¿Para qué se hace un folleto de turismo?", "Para atraer visitantes", "Su propósito es mostrar lo atractivo de un lugar."), ("¿Un solo dato permite hablar de todo un ambiente?", "No", "Un dato aislado no representa a todo el ambiente.")],
    (
        "Lee esta fuente: «Informe de un liceo del altiplano: en nuestro pueblo, a 3.900 m de altura, la helada llegó 40 noches el año pasado y las llamas resistieron mejor el frío que las ovejas». Escribe una observación que sale del informe, una conclusión que NO se puede sacar de él y una pregunta de procedencia.",
        "Observación: hubo 40 noches de helada. No se puede decir que en todo el altiplano pase igual. Pregunta: ¿quién midió las heladas?",
        ["una observación tomada del informe", "una conclusión que el informe no permite", "una pregunta de procedencia"],
        ["tres frases escritas"],
        ["inventar datos que el informe no entrega", "olvidar la pregunta de procedencia"],
        "Muestra tus tres frases a una persona de tu casa y pídele que subraye cuáles salen directamente del informe.",
    ),
    "Mira un aviso o un envase de tu casa y escribe quién lo hizo y para qué.",
    "Escribe qué segunda fuente usarías para comprobar lo que dice un folleto de turismo.",
)

# ================================================================ OA 12 · clase 3
lesson(
    OA12, 3,
    "Aprenderé a relacionar el rasgo de un ambiente con las oportunidades y dificultades que crea y con lo que hicieron las personas para vivir allí. Sirve para entender por qué cada zona de Chile tiene actividades distintas.",
    ["Sé ubicar los ambientes de Chile.", "Sé leer una fuente y preguntar por su procedencia."],
    [
        "Un rasgo del ambiente puede ser una oportunidad o una dificultad, según cómo lo aprovechen las personas. Una oportunidad es una condición que ayuda a vivir o a trabajar. Una dificultad es una condición que complica la vida. Por ejemplo, el sol abundante del desierto es una oportunidad para producir energía solar y su falta de agua es una dificultad.",
        "Las personas buscan soluciones: en el desierto usan atrapanieblas, que son mallas que captan gotas de neblina, y plantas desaladoras, que sacan la sal del agua de mar. En el altiplano los pueblos cultivan en terrazas y crían llamas y alpacas. En la zona central se construyen embalses para guardar agua del invierno. En el sur lluvioso hay bosques que dan madera, pero los caminos se llenan de barro.",
        "Para relacionar hacemos una cadena: rasgo del ambiente, dificultad u oportunidad, actores, acción y consecuencia. Los actores son las personas o grupos que participan, como las comunidades, las empresas o el Estado. La consecuencia puede ser buena y a la vez traer un costo.",
    ],
    [("oportunidad", "condición del ambiente que ayuda a vivir o trabajar"), ("dificultad", "condición del ambiente que complica la vida"), ("atrapanieblas", "malla que capta gotas de neblina y las convierte en agua"), ("embalse", "lugar donde se guarda agua de un río"), ("consecuencia", "lo que ocurre después de una acción")],
    [
        ("Armar la cadena", "Un pueblo del desierto tiene poca agua. Sus vecinos instalan atrapanieblas en un cerro con neblina. Nombra la dificultad, la acción y la consecuencia.", ["Dificultad: poca agua.", "Acción: instalar mallas que captan neblina.", "Consecuencia: se consigue agua sin traerla de lejos."], "Dificultad: poca agua; acción: atrapanieblas; consecuencia: se obtiene agua"),
        ("Una oportunidad", "En el centro de Chile llueve en invierno y el verano es seco. ¿Qué construcción ayuda a usar el agua en verano?", ["Se necesita guardar agua del invierno.", "Un embalse guarda el agua.", "Así se usa en el verano seco."], "Un embalse"),
    ],
    [
        ("Pensar que una dificultad del ambiente impide vivir allí.", "Las personas han creado soluciones, como terrazas, embalses o desaladoras.", "Pregunta qué hicieron las personas para superarla."),
        ("Creer que una solución no tiene costos.", "Construir embalses o desaladoras cuesta dinero y trabajo.", "Busca siempre un beneficio y un costo."),
    ],
    [
        ("Poca agua en el desierto, ¿es una oportunidad o una dificultad?", "Una dificultad", "La falta de agua complica la vida y los cultivos."),
        ("Mucho sol en el desierto, ¿es una oportunidad o una dificultad para producir energía?", "Una oportunidad", "Los paneles solares aprovechan la luz del sol."),
        ("Un atrapanieblas, ¿capta gotas de neblina o sube el agua desde un pozo?", "Capta gotas de neblina", "Es una malla que junta las gotitas de neblina."),
    ],
    [
        ("¿Para qué sirve una planta desaladora?", "Para sacar la sal del agua de mar", "Así se obtiene agua que sirve para beber o regar."),
        ("¿Por qué en el altiplano se cultiva en terrazas?", "Porque el terreno es inclinado y las terrazas lo vuelven plano", "Las terrazas permiten sembrar en una pendiente."),
        ("¿Por qué los embalses son útiles en la zona central?", "Guardan agua del invierno para el verano seco", "En el verano casi no llueve."),
    ],
    [
        ("En el sur llueve casi todo el año y hay bosques. Nombra una oportunidad y una dificultad de ese ambiente.", "Oportunidad: madera de los bosques; dificultad: lluvia y barro en los caminos", "Los bosques dan madera, pero la lluvia complica el transporte."),
        ("En la Patagonia los pueblos están muy lejos unos de otros. ¿Qué dificultad crea eso para llevar alimentos?", "El transporte toma más tiempo y cuesta más", "Recorrer muchos kilómetros exige tiempo y dinero."),
        ("En el polar, hay bases científicas de varios países y de Chile. Las personas llegan por barco o avión. ¿Qué dificultad enfrentan para llegar?", "El aislamiento y el difícil acceso", "No hay caminos hacia la Antártica."),
    ],
    [
        ("Rosa dice: «Como en el desierto falta agua, nadie puede vivir allí». ¿Qué le falta considerar?", "Las soluciones de las personas, como atrapanieblas o desaladoras", "Las personas aprovechan lo que hay y superan lo que falta."),
        ("Una comunidad construye un embalse. Ordena la cadena: A) el verano trae agua guardada, B) llueve en invierno y hay poca agua en verano, C) se construye un embalse.", "B, C, A", "Primero el rasgo del ambiente, luego la acción y después el resultado."),
    ],
    [
        ("Una desaladora produce agua que sirve para una ciudad del norte, pero gasta mucha energía. ¿Cuál es el beneficio y cuál el costo?", "Beneficio: agua para la ciudad; costo: mucha energía", "Cada solución trae algo bueno y algo que hay que pagar."),
        ("Dos pueblos del norte: uno está junto al mar y el otro está a 200 km del mar, entre cerros. ¿Cuál puede usar una desaladora con agua del mar?", "El que está junto al mar", "La desaladora necesita agua de mar cerca."),
    ],
    [("Un pueblo del altiplano tiene noches muy frías y poco pasto. Sus habitantes crían llamas, que se adaptan a esas condiciones. ¿Qué actor toma la acción aquí: las familias del pueblo o las llamas?", "Las familias del pueblo", "Los actores son las personas que deciden criar a los animales.")],
    [("¿Qué es una oportunidad de un ambiente?", "Una condición que ayuda a vivir o trabajar", "Es la definición de la clase."), ("¿Qué hacen los atrapanieblas?", "Captan gotas de neblina", "Así se consigue agua en lugares sin lluvia."), ("¿Las dificultades de un ambiente impiden siempre vivir allí?", "No", "Las personas crean soluciones para superarlas.")],
    (
        "Elige uno de estos casos y escribe la cadena completa (rasgo del ambiente, dificultad u oportunidad, actores, acción, consecuencia y un costo). Caso a) un pueblo del desierto con neblina y poca agua; caso b) familias del altiplano en un cerro inclinado; caso c) una comunidad de la zona central con inviernos lluviosos y veranos secos.",
        "Caso c: veranos secos; dificultad de agua; actores: comunidad y regantes; acción: embalse; consecuencia: agua en verano; costo: dinero y mantención.",
        ["nombra el rasgo del ambiente", "distingue dificultad y acción de las personas", "incluye al menos un actor y un costo"],
        ["cadena escrita en cinco partes"],
        ["confundir el rasgo con la solución", "olvidar el costo"],
        "Lee tu cadena en voz alta y pide a una persona de tu casa que diga cuál es la dificultad y cuál la solución.",
    ),
    "Escribe una dificultad de tu zona y una acción que las personas hicieron para superarla.",
    "Escribe una oportunidad de un ambiente que no sea el tuyo y cómo se puede aprovechar.",
)

# ================================================================ OA 12 · clase 4
lesson(
    OA12, 4,
    "Aprenderé a comparar dos ambientes de Chile con los mismos criterios: oportunidades, dificultades y soluciones de las personas. Sirve para ver semejanzas y diferencias sin decir que un lugar es mejor que otro.",
    ["Sé relacionar un rasgo del ambiente con una oportunidad o dificultad.", "Sé que las personas crean soluciones."],
    [
        "Comparar es ver en qué se parecen y en qué se diferencian dos cosas. Para hacerlo bien se usan criterios, que son preguntas iguales para ambos lugares. Aquí usaremos tres: qué oportunidades ofrece el ambiente, qué dificultades tiene y qué soluciones inventaron las personas.",
        "Por ejemplo, el desierto y el sur frío y lluvioso son muy distintos. El desierto tiene sol y minerales, pero muy poca agua. El sur tiene bosques, ríos y lagos, pero lluvia casi todo el año y caminos difíciles. En los dos hay personas que viven y trabajan, y en los dos la solución depende de lo que falta o sobra.",
        "Al comparar no decimos que un ambiente es mejor. Decimos qué ofrece cada uno y qué desafíos tiene. También miramos las perspectivas, que son las miradas de personas según su situación. Una familia que cría llamas en el altiplano, una persona que trabaja en un puerto y un turista valoran de modo distinto el mismo lugar.",
    ],
    [("criterio", "pregunta o regla igual para comparar dos cosas"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian"), ("perspectiva", "mirada de una persona según su situación"), ("ambiente", "lugar con clima, relieve, plantas y animales propios")],
    [
        ("Comparar con criterios", "Ambiente A: sol y minerales, muy poca agua. Ambiente B: bosques y ríos, mucha lluvia. Compara el criterio «agua».", ["En A hay muy poca agua.", "En B hay mucha agua.", "La diferencia es la cantidad de agua disponible."], "A tiene poca agua y B tiene mucha"),
        ("Una semejanza", "En el altiplano y en el desierto llueve poco durante el año. ¿Qué semejanza hay entre ambos?", ["Miro el criterio lluvia en los dos.", "Ambos reciben poca lluvia.", "Eso es lo que se parece."], "Ambos reciben poca lluvia"),
    ],
    [
        ("Decir que un ambiente es «mejor» que otro.", "Cada ambiente tiene oportunidades y dificultades propias.", "Compara con criterios y evita juzgar."),
        ("Comparar usando un criterio distinto para cada lugar.", "La comparación no es justa si no se mide lo mismo.", "Usa las mismas preguntas en los dos lugares."),
    ],
    [
        ("Una semejanza, ¿es en lo que dos cosas se parecen o en lo que cambian?", "En lo que se parecen", "Lo que cambia es la diferencia."),
        ("El desierto y el sur lluvioso, ¿tienen la misma cantidad de agua o distinta?", "Distinta", "En el desierto llueve poco y en el sur mucho."),
        ("Un criterio de comparación, ¿es una pregunta igual para los dos lugares o una opinión?", "Una pregunta igual para los dos lugares", "Así la comparación es justa."),
    ],
    [
        ("¿Por qué no se dice que el sur es mejor que el desierto?", "Porque cada ambiente tiene oportunidades y dificultades distintas", "Los dos ofrecen y exigen cosas diferentes."),
        ("Una persona que cría llamas y un turista miran el altiplano. ¿Por qué pueden valorarlo distinto?", "Porque cada uno tiene una situación y un propósito distintos", "Eso es tener perspectivas distintas."),
        ("Para comparar dos ambientes, ¿sirve más usar los mismos criterios o elegir criterios distintos?", "Los mismos criterios", "Así se compara lo mismo en ambos."),
    ],
    [
        ("Tabla: Mediterráneo, oportunidad: tierras fértiles para frutas; dificultad: veranos secos. Patagónico, oportunidad: pastos para ovejas; dificultad: viento fuerte y lejanía. ¿En cuál ambiente de la tabla la dificultad es la falta de agua en una estación?", "En el mediterráneo", "Sus veranos son secos."),
        ("Con la misma tabla: ¿en cuál ambiente la oportunidad se relaciona con la crianza de ovejas?", "Patagónico", "Los pastos de la estepa alimentan a las ovejas."),
        ("Comparación: en el costero hay puertos para pescar y comerciar; en el andino hay nieve que se derrite y llena ríos. ¿En cuál ambiente la oportunidad está ligada al mar?", "En el costero", "Los puertos y la pesca dependen del mar."),
    ],
    [
        ("Marta escribe: «El mediterráneo es mejor que el altiplánico porque tiene más gente». ¿Qué error comete al comparar?", "Juzga con un solo dato en vez de comparar con criterios", "Tener más gente no dice si un ambiente es mejor."),
        ("En el desierto y en el altiplano falta agua. Las soluciones son distintas: desaladoras junto al mar y terrazas con canales en los cerros. ¿Qué tienen en común ambas soluciones?", "Buscan resolver la falta de agua o aprovecharla mejor", "El problema del agua es la semejanza."),
    ],
    [
        ("Tabla de ejemplo, días con helada al año: pueblo del altiplano, 180; pueblo de la costa del centro, 5. ¿Cuántos días más con helada tiene el altiplano?", "175", "Se resta: 180 menos 5."),
        ("Ordena de más a menos lluvia anual de ejemplo: Q (350 mm), R (2.500 mm), S (600 mm).", "R, S, Q", "Se ordenan las cifras de mayor a menor."),
    ],
    [("Una comunidad vive en el sur frío y lluvioso y otra en el desierto. Ambas usan el recurso que tienen cerca: bosques y sol. Si comparas con el criterio «recurso natural aprovechado», ¿cuál es el recurso del sur?", "Los bosques", "El recurso del sur lluvioso que se mencionó es el bosque.")],
    [("¿Para qué sirven los criterios al comparar?", "Para comparar lo mismo en ambos lugares", "Así la comparación es justa."), ("¿Qué es una perspectiva?", "La mirada de una persona según su situación", "Es la definición de la clase."), ("¿Un ambiente es mejor que otro?", "No, tienen oportunidades y dificultades distintas", "Se comparan, no se juzgan.")],
    (
        "Completa esta tabla con una frase por casilla. Columnas: desierto del norte / sur frío y lluvioso. Filas: una oportunidad, una dificultad y una solución de las personas. Luego escribe una semejanza y una diferencia. Pistas que puedes usar: sol, minerales, poca agua, bosques, lluvia, barro, atrapanieblas, caminos y puentes.",
        "Desierto: sol; poca agua; atrapanieblas. Sur: bosques; barro; caminos. Semejanza: en ambos hay personas que se adaptaron. Diferencia: agua escasa o abundante.",
        ["usa los mismos tres criterios en ambos ambientes", "escribe una semejanza y una diferencia", "evita decir que uno es mejor"],
        ["tabla de dos columnas y dos frases"],
        ["comparar con criterios distintos", "juzgar un ambiente como mejor"],
        "Pide a una persona de tu casa que lea tu tabla y diga si comparaste lo mismo en los dos ambientes.",
    ),
    "Elige dos ambientes que no hayas comparado y escribe una semejanza entre ellos.",
    "Escribe una pregunta que te gustaría hacerle a una persona que vive en un ambiente muy distinto al tuyo.",
)

# ================================================================ OA 12 · clase 5
lesson(
    OA12, 5,
    "Aprenderé a defender una idea sobre un ambiente de Chile con evidencia: una afirmación, un dato y una razón. Sirve para opinar con fundamentos y no solo porque sí.",
    ["Sé comparar ambientes con criterios.", "Sé que una fuente entrega datos y que hay que preguntar su procedencia."],
    [
        "Argumentar es defender una idea con razones. Un buen argumento tiene tres partes: una afirmación, que es lo que sostengo; una evidencia, que es un dato o una fuente que lo apoya; y una razón, que explica por qué la evidencia apoya la afirmación. Sin evidencia, una opinión queda sin fundamento.",
        "Por ejemplo: «El altiplano sirve para criar llamas». La evidencia puede ser que allí hay pastos duros y que las llamas resisten el frío y la altura. La razón es que esos animales se adaptan a las condiciones del lugar. Para que el argumento sea fuerte, la evidencia debe ser concreta y venir de una fuente confiable.",
        "También hay que decir qué no sabemos. Si la evidencia viene de un solo lugar, no se puede afirmar que valga para todo el ambiente. Un argumento honesto reconoce sus límites y propone qué datos faltan para estar más seguros.",
    ],
    [("argumento", "idea defendida con evidencia y razones"), ("afirmación", "lo que una persona sostiene"), ("evidencia", "dato o fuente que apoya una afirmación"), ("razón", "explicación de por qué la evidencia apoya la afirmación"), ("límite", "lo que la evidencia no permite saber")],
    [
        ("Identificar la evidencia", "Frase: «En el sur se pueden criar salmones, porque hay lagos y fiordos de aguas frías». ¿Cuál es la afirmación y cuál la evidencia?", ["La afirmación es lo que se sostiene: se pueden criar salmones.", "La evidencia es lo que lo apoya: hay lagos y fiordos de aguas frías.", "Los separo."], "Afirmación: se pueden criar salmones; evidencia: lagos y fiordos de aguas frías"),
        ("Reconocer un límite", "Un informe mide el viento en un solo pueblo de la Patagonia y dice que sopla fuerte. ¿Qué no permite saber?", ["Es un solo pueblo.", "No dice nada de otros lugares.", "No permite afirmar que todo el ambiente sea igual."], "No permite saber cómo es el viento en toda la Patagonia"),
    ],
    [
        ("Dar una opinión sin ningún dato que la apoye.", "Una opinión sin evidencia no convence ni se puede comprobar.", "Agrega un dato o una fuente."),
        ("Usar como evidencia algo que no tiene relación con la afirmación.", "La evidencia debe apoyar justamente lo que se afirma.", "Revisa si el dato sirve para esa afirmación."),
    ],
    [
        ("Una afirmación, ¿es lo que alguien sostiene o el dato que lo apoya?", "Lo que alguien sostiene", "El dato que lo apoya es la evidencia."),
        ("«En el desierto de ejemplo llovieron 3 mm en un año», ¿puede ser evidencia o es una opinión?", "Puede ser evidencia", "Es un dato con unidad."),
        ("La razón de un argumento, ¿explica por qué la evidencia apoya la afirmación o repite la afirmación?", "Explica por qué la evidencia apoya la afirmación", "Conecta el dato con la idea."),
    ],
    [
        ("¿Por qué un argumento necesita evidencia?", "Para que se pueda comprobar y convencer", "Sin datos, una opinión queda sin fundamento."),
        ("¿Por qué es importante decir qué no sabemos?", "Porque la evidencia de un solo lugar no vale para todo el ambiente", "Reconocer límites evita generalizar."),
        ("¿Por qué una fuente confiable da más fuerza a un argumento?", "Porque sus datos tienen una procedencia clara", "Se sabe quién los midió y para qué."),
    ],
    [
        ("Afirmación: «Los embalses ayudan a la agricultura de la zona central». ¿Cuál es una evidencia adecuada: «guardan agua de invierno para el verano seco» o «son bonitos»?", "Guardan agua de invierno para el verano seco", "Ese dato se relaciona con el riego de los cultivos."),
        ("Afirmación: «En el altiplano conviene criar llamas». ¿Qué evidencia sirve: «las llamas resisten el frío y la altura» o «a mucha gente le gustan las llamas»?", "Las llamas resisten el frío y la altura", "Esa característica se relaciona con las condiciones del ambiente."),
        ("Afirmación: «Una desaladora tiene un costo». ¿Qué evidencia sirve: «gasta mucha energía para sacar la sal» o «está junto al mar»?", "Gasta mucha energía para sacar la sal", "El gasto de energía es un costo concreto."),
    ],
    [
        ("Eva escribe: «El sur es el mejor ambiente de Chile porque me gusta». ¿Qué le falta a su argumento?", "Evidencia y razones, no solo gusto personal", "Un gusto no se puede comprobar con datos."),
        ("Un informe muestra que en un pueblo del desierto el agua se obtiene con atrapanieblas. Luis concluye: «En todo el desierto el agua viene de atrapanieblas». ¿Qué límite no respeta?", "Un solo pueblo no representa a todo el desierto", "Generaliza más allá de la evidencia."),
    ],
    [
        ("Ordena las partes de un argumento: A) razón, B) afirmación, C) evidencia.", "B, C, A", "Primero se afirma, luego se muestra el dato y por último se explica."),
        ("Dos ambientes y una tabla de ejemplo: Q tiene 350 mm de lluvia al año y R tiene 2.500 mm. Afirmación: «R es más adecuado para cultivar sin riego». ¿Qué dato de la tabla apoya mejor esa afirmación?", "Que R tiene 2.500 mm de lluvia", "Más lluvia aporta más agua a las plantas."),
    ],
    [("Una comunidad quiere decidir si cultivar papas en terrazas del altiplano. Un vecino dice: «Sí, porque las terrazas permiten sembrar en los cerros inclinados». ¿Cuál es la afirmación del vecino?", "Que conviene cultivar papas en terrazas del altiplano", "Esa es la idea que sostiene; lo demás son las razones.")],
    [("¿Qué tres partes tiene un buen argumento?", "Afirmación, evidencia y razón", "Así se enseñó en la clase."), ("¿Qué es la evidencia?", "Un dato o fuente que apoya una afirmación", "Es la definición del vocabulario."), ("¿Qué es un límite en un argumento?", "Lo que la evidencia no permite saber", "Es la definición del vocabulario.")],
    (
        "Elige una de estas preguntas y respóndela en cuatro frases con afirmación, evidencia, razón y límite. Pregunta a) ¿Qué ambiente conviene para criar ovejas: la estepa patagónica (pastos y viento) o el desierto (sin pastos)? Pregunta b) ¿Qué ambiente conviene para cultivar frutas: el mediterráneo (veranos secos con riego) o el polar (hielo todo el año)?",
        "Pregunta b: afirmación: el mediterráneo. Evidencia: tiene tierras fértiles y riego. Razón: las plantas reciben agua y calor. Límite: falta saber cuánta agua hay.",
        ["incluye afirmación y evidencia", "explica la razón", "señala un límite"],
        ["cuatro frases escritas"],
        ["no incluir evidencia", "generalizar sin reconocer límites"],
        "Lee tus frases a una persona de tu casa y pídele que diga cuál es tu afirmación y cuál tu evidencia.",
    ),
    "Elige una opinión sobre tu zona y escribe un dato que la apoye.",
    "Escribe una pregunta que sirva para buscar más evidencia sobre un ambiente de Chile.",
)

# ================================================================ OA 13 · clase 1
lesson(
    OA13, 1,
    "Aprenderé a ubicar mi región y mi localidad y a distinguir sus características físicas, humanas y económicas. Sirve para describir el lugar donde vivo con orden.",
    ["Sé que Chile tiene ambientes naturales distintos.", "Sé leer datos de una tabla."],
    [
        "Chile se divide en 16 regiones. Cada región se divide en provincias y cada provincia en comunas. La localidad es el pueblo, el barrio o la ciudad donde vive una persona dentro de una comuna. Para ubicar un lugar vamos de lo más grande a lo más pequeño: país, región, provincia, comuna y localidad.",
        "Al describir una región o localidad, miramos tres tipos de características. Las físicas son las de la naturaleza: relieve, clima, ríos, mar, plantas y animales. Las humanas tienen que ver con las personas: cuántas son, dónde viven, qué costumbres y servicios tienen. Las económicas son las actividades con que las personas obtienen ingresos, como agricultura, pesca, industria, comercio o turismo.",
        "Para esta clase usaremos un lugar inventado, llamado Lomas Verdes, solo para practicar. Una localidad puede ser rural, con pocos habitantes y mucho campo, o urbana, con más habitantes, calles y servicios. Cada ficha debe decir de dónde viene la información y cuándo fue recogida.",
    ],
    [("región", "gran división del territorio de Chile; el país tiene 16"), ("comuna", "división de una provincia, donde funciona una municipalidad"), ("localidad", "pueblo, barrio o ciudad donde vive una persona"), ("característica física", "rasgo de la naturaleza, como el relieve o el clima"), ("característica económica", "actividad con que las personas obtienen ingresos")],
    [
        ("Clasificar una característica", "En Lomas Verdes, un lugar inventado, «hay un río y cerros bajos». ¿Es característica física, humana o económica?", ["Un río y cerros son parte de la naturaleza.", "No hablan de personas ni de trabajo.", "Es física."], "Física"),
        ("Ubicar de lo grande a lo pequeño", "Ordena de mayor a menor: comuna, región, localidad.", ["La región es la más grande.", "La comuna está dentro de la región.", "La localidad está dentro de la comuna."], "Región, comuna, localidad"),
    ],
    [
        ("Pensar que la comuna es más grande que la región.", "Las comunas están dentro de las provincias, y estas dentro de las regiones.", "Ubica de lo más grande a lo más pequeño."),
        ("Poner el comercio y la pesca entre las características físicas.", "Son actividades de las personas, es decir, económicas.", "Pregunta si habla de naturaleza, personas o trabajo."),
    ],
    [
        ("¿Cuántas regiones tiene Chile?", "16", "Así se enseñó en la clase."),
        ("¿Una región es más grande o más pequeña que una comuna?", "Más grande", "La región contiene provincias y comunas."),
        ("«Hay 2.400 habitantes», ¿es una característica física o humana?", "Humana", "Habla de cuántas personas viven allí."),
    ],
    [
        ("¿Qué diferencia hay entre una comuna y una localidad?", "La comuna es una división administrativa y la localidad es el pueblo o barrio donde se vive", "Una localidad está dentro de una comuna."),
        ("¿Por qué el clima es una característica física y no económica?", "Porque pertenece a la naturaleza y no es una actividad de las personas", "El clima no lo hacen las personas."),
        ("¿Qué diferencia hay entre una localidad rural y una urbana?", "La rural tiene pocos habitantes y mucho campo; la urbana tiene más gente, calles y servicios", "Así se describieron en la clase."),
    ],
    [
        ("Ficha del lugar inventado Valle Alegre: «clima templado, río Claro, 3.000 habitantes, cultivo de manzanas». ¿Cuál dato es económico?", "El cultivo de manzanas", "Es una actividad con la que las personas obtienen ingresos."),
        ("Con la ficha de Valle Alegre: ¿cuál dato es físico?", "El clima templado y el río Claro", "Son rasgos de la naturaleza."),
        arith("En el lugar inventado Pueblo Sol viven 2.400 personas; 1.500 viven en la zona urbana y el resto en la zona rural. ¿Cuántas viven en la zona rural?", "2400-1500", "Se resta lo urbano al total.", " personas"),
    ],
    [
        ("Eva dice: «En mi localidad solo hay trabajo en el campo, así que no tiene características humanas». ¿Qué error comete?", "Las características humanas incluyen a las personas y cómo viven, además del trabajo", "El trabajo es económico, pero la población y los servicios son humanos."),
        ("Una ficha dice: «Puerto Brisa: junto al mar, 8.000 habitantes, pesca y turismo». Ordena los tres tipos de características de Puerto Brisa: a) pesca y turismo, b) junto al mar, c) 8.000 habitantes.", "b física, c humana, a económica", "El mar es naturaleza, los habitantes son personas y la pesca y el turismo son actividades."),
    ],
    [
        ("Ordena de mayor a menor: provincia, país, localidad, comuna, región.", "País, región, provincia, comuna, localidad", "Se parte del territorio más grande hacia el más pequeño."),
        ("Una ficha de ejemplo tiene tres datos: «precipitaciones 800 mm», «40 % de las personas trabaja en el comercio», «viven 5.000 personas». ¿Cuántos datos son económicos?", "1", "Solo «40 % trabaja en el comercio» habla de actividad económica."),
    ],
    [("Un niño dice que su localidad tiene un lago, 1.200 habitantes y un hotel que da trabajo. ¿Cuántos tipos de características distintos aparecen: físicas, humanas y económicas?", "Tres", "El lago es físico, los habitantes son humanos y el hotel es económico.")],
    [("En Historia: ¿cuántas regiones tiene Chile?", "16", "Es el número de regiones del país."), ("¿Qué son las características económicas?", "Las actividades con que las personas obtienen ingresos", "Es la definición de la clase."), ("¿Dónde queda una localidad?", "Dentro de una comuna", "La localidad es el pueblo o barrio de una comuna.")],
    (
        "Completa esta ficha para tu localidad, con una frase por casilla: región y comuna; relieve (cordillera, valle, costa o llanura); clima (cálido, templado o frío); cuántas personas viven (pocas, algunas o muchas); una actividad económica. Si no sabes tu región, usa esta alternativa: región costera con puerto, turismo y fruta. Termina escribiendo de dónde sacaste cada dato.",
        "Mi comuna está en una región con valle y clima templado; viven muchas personas; una actividad es el comercio. Dato sacado de un mapa de la escuela.",
        ["incluye datos físicos, humanos y económicos", "ubica de lo grande a lo pequeño", "indica la fuente de cada dato"],
        ["ficha de cinco casillas y una frase de fuentes"],
        ["mezclar lo físico con lo económico", "no decir de dónde sale cada dato"],
        "Muestra tu ficha a una persona de tu casa y pídele que corrija un dato que le parezca incorrecto.",
    ),
    "Dibuja un esquema con país, región, comuna y tu localidad, de mayor a menor.",
    "Escribe una característica de tu localidad que creas que otras personas no conocen.",
)

# ================================================================ OA 13 · clase 2
lesson(
    OA13, 2,
    "Aprenderé a usar fuentes sobre mi región y localidad: mapas, datos de censos, páginas de la municipalidad y entrevistas, y a preguntar quién las hizo. Sirve para describir un lugar con información confiable.",
    ["Sé distinguir características físicas, humanas y económicas.", "Sé que toda fuente tiene una procedencia."],
    [
        "Para conocer una región o una localidad usamos varias fuentes. Un mapa muestra relieve, ríos y caminos. Un censo, que hace el Instituto Nacional de Estadísticas (INE), cuenta a las personas y entrega datos de población. La municipalidad informa de sus servicios. Una entrevista a un vecino cuenta cómo se vive.",
        "Cada fuente tiene una procedencia: quién la hizo, cuándo y para qué. Un dato de hace diez años puede haber cambiado. La publicidad de un hotel resalta lo atractivo. Un vecino cuenta lo que ve en su barrio, no de toda la región. Por eso conviene comparar al menos dos fuentes antes de decir que algo es cierto.",
        "También hay que separar lo que la fuente dice de lo que interpretamos. Si una tabla dice que en una localidad hay 1.000 habitantes y que 300 son niños, podemos calcular que 700 no son niños. Pero no podemos decir que en toda la región pasa lo mismo, porque la tabla solo habla de esa localidad.",
    ],
    [("censo", "recuento oficial de las personas que viven en un país"), ("municipalidad", "institución que administra una comuna"), ("entrevista", "conversación para obtener información de una persona"), ("dato actualizado", "información reciente, no antigua"), ("procedencia", "quién hizo la fuente, cuándo y para qué")],
    [
        ("Elegir la fuente", "Quieres saber cuántas personas viven en una comuna. ¿Qué fuente conviene: un censo o un aviso de hotel?", ["El censo cuenta a las personas.", "El aviso de hotel busca vender estadías.", "Elijo el censo."], "Un censo"),
        ("Leer una tabla", "Tabla de ejemplo, Pueblo Sol en 2015: 1.200 habitantes; en 2025: 1.500 habitantes. ¿Cuántos habitantes más hay?", ["Comparo los años.", "1.500 menos 1.200.", "Son 300."], "300 habitantes más"),
    ],
    [
        ("Usar un dato antiguo como si fuera actual.", "La población y las actividades cambian con los años.", "Mira la fecha de la fuente."),
        ("Creer que lo que dice un vecino vale para toda la región.", "Un vecino cuenta lo que vive en su barrio.", "Agrega otra fuente."),
    ],
    [
        ("Un mapa, ¿muestra relieve y ríos o cuenta cuántas personas viven?", "Muestra relieve y ríos", "El conteo de personas lo hace un censo."),
        ("¿Quién hace el censo en Chile: el INE o un hotel?", "El INE", "El Instituto Nacional de Estadísticas lo realiza."),
        ("Un aviso de un hotel de la costa, ¿se hizo para vender estadías o para contar habitantes?", "Para vender estadías", "Su propósito es atraer clientes."),
    ],
    [
        ("¿Por qué conviene mirar la fecha de una fuente?", "Porque el dato puede haber cambiado con el tiempo", "La población y el trabajo cambian."),
        ("¿Por qué conviene comparar al menos dos fuentes?", "Para comprobar que la información coincide", "Una sola fuente puede equivocarse o ser parcial."),
        ("¿Por qué lo que cuenta un vecino no sirve para describir toda una región?", "Porque habla de su barrio y no de todo el territorio", "Su experiencia es una parte."),
    ],
    [
        ("Tabla de ejemplo, Puerto Brisa: 8.000 habitantes, 5.000 mayores de 18 años. ¿Cuántos tienen 18 años o menos?", "3.000", "Se resta: 8.000 menos 5.000."),
        ("Entrevista de ejemplo a un pescador: «Hoy pesqué menos que antes». ¿Es una fuente sobre la vida de una persona o sobre el total de pescadores de Chile?", "Sobre la vida de una persona", "Un relato cuenta una experiencia individual."),
        ("Mapa de ejemplo: Villa Monte tiene cerros al este y un río al sur. ¿Qué tipo de característica entrega el mapa: física o económica?", "Física", "Los cerros y el río son parte de la naturaleza."),
    ],
    [
        ("Luis lee que Villa Mar tenía 900 habitantes en 2015 y concluye: «Hoy también tiene 900». ¿Qué error comete?", "Usa un dato antiguo como si fuera actual", "La población puede haber cambiado en diez años."),
        ("Una página de la municipalidad dice «Somos la comuna más linda». ¿Es un dato comprobable o una opinión?", "Una opinión", "«La más linda» no se puede medir con cifras."),
    ],
    [
        ("Ordena los pasos para usar una fuente: A) calcular o concluir con lo que dice, B) revisar la fecha y quién la hizo, C) leer el dato.", "B, C, A", "Primero la procedencia, luego el dato y al final la conclusión."),
        ("Un censo de ejemplo dice que 300 de las 1.000 personas de una localidad son niños. ¿Qué porcentaje de la población son niños?", "30 %", "300 de 1.000 es 30 de cada 100."),
    ],
    [("Un niño quiere saber a qué se dedican los habitantes de su comuna. Puede consultar la página de la municipalidad o preguntar a un vecino, pero también puede hacer ambas. ¿Qué ventaja da usar las dos fuentes?", "Puede comparar un dato oficial con una experiencia personal", "Cada fuente aporta algo que la otra no muestra.")],
    [("En Historia: ¿quién realiza el censo en Chile?", "El INE", "Es el Instituto Nacional de Estadísticas."), ("¿Qué datos entrega un mapa?", "Relieve, ríos y caminos", "Muestra el espacio físico."), ("¿Por qué mirar la fecha de una fuente?", "El dato puede haber cambiado", "El tiempo modifica la población y el trabajo.")],
    (
        "Lee esta ficha de un lugar inventado: «Villa Monte, 2025. Fuente: oficina de turismo de la municipalidad. Hay 2.000 habitantes. El 60 % vive en el pueblo. Hay un río y cerros al este. Se cultivan cerezas». Escribe una característica física, una humana y una económica de Villa Monte, y una pregunta sobre la procedencia de la ficha.",
        "Física: hay un río y cerros al este. Humana: viven 2.000 habitantes. Económica: se cultivan cerezas. Pregunta: ¿la oficina de turismo cuenta también los problemas?",
        ["extrae un dato de cada tipo", "los copia sin inventar", "formula una pregunta de procedencia"],
        ["cuatro frases escritas"],
        ["inventar datos que la ficha no entrega", "confundir el tipo de característica"],
        "Muestra tus frases a una persona de tu casa y pídele que compruebe que cada dato esté en la ficha.",
    ),
    "Pregunta a una persona de tu casa qué cambió en tu localidad en los últimos años y anótalo con la fecha.",
    "Escribe qué fuente usarías para saber cuántas personas viven en tu comuna.",
)

# ================================================================ OA 13 · clase 3
lesson(
    OA13, 3,
    "Aprenderé a relacionar el relieve y el clima con las actividades de las personas, la población y los cambios que viven en una localidad. Sirve para explicar por qué un lugar es como es.",
    ["Sé que un lugar tiene características físicas, humanas y económicas.", "Sé usar fuentes con su procedencia."],
    [
        "Las características de una localidad se relacionan. El relieve y el clima influyen en las actividades económicas. Una costa con puerto favorece la pesca y el comercio. Un valle con riego favorece la agricultura. Una zona con montañas y nieve favorece el turismo y el esquí. Las actividades influyen en la población: donde hay trabajo suelen vivir más personas.",
        "Una causa es la razón de un hecho y una consecuencia es lo que pasa después. Si en una localidad cierra una fábrica, una consecuencia es que algunas personas pierden el empleo y otras se van a vivir a otro lugar. Si se abre un camino, la consecuencia puede ser que lleguen más turistas. Los actores son las personas o instituciones que participan, como las familias, los comerciantes y la municipalidad.",
        "Una cadena de causas y consecuencias puede ser larga: el clima seco permite sembrar frutas con riego, la fruta da trabajo en la cosecha, el trabajo atrae familias y llegan nuevos servicios, como una escuela. Por eso decimos que las características físicas, humanas y económicas están conectadas.",
    ],
    [("causa", "razón por la que algo ocurre"), ("consecuencia", "lo que ocurre después de un hecho"), ("actor", "persona o institución que participa en un hecho"), ("servicio", "ayuda que se ofrece a las personas, como una escuela o un consultorio"), ("favorecer", "ayudar a que algo ocurra")],
    [
        ("Armar una cadena", "En un valle con riego y clima templado se cultivan uvas. La cosecha da trabajo a muchas familias, que viven cerca. Ordena: causa, actividad, consecuencia.", ["La causa es el valle con riego y clima templado.", "La actividad es el cultivo de uvas.", "La consecuencia es que muchas familias tienen trabajo y viven cerca."], "Causa: valle con riego; actividad: uvas; consecuencia: trabajo y familias cerca"),
        ("Una consecuencia humana", "Cierra la única fábrica de un pueblo pequeño. Nombra una consecuencia en las personas.", ["Cierra la fábrica.", "Se pierden empleos.", "Algunas familias pueden irse a otro lugar."], "Se pierden empleos y algunas familias se van"),
    ],
    [
        ("Creer que el relieve y las actividades de un lugar no se relacionan.", "El relieve y el clima influyen en lo que se puede cultivar, pescar o construir.", "Pregunta qué hace posible cada actividad."),
        ("Nombrar un solo actor, como «la municipalidad».", "También participan las familias, los comerciantes y los trabajadores.", "Haz una lista de todos los actores."),
    ],
    [
        ("Una costa con puerto, ¿favorece la pesca o el esquí?", "La pesca", "El esquí necesita montañas con nieve."),
        ("Un camino nuevo llega a un pueblo con paisajes bonitos. ¿Qué actividad puede crecer: el turismo o la minería de cobre?", "El turismo", "El camino facilita que los visitantes lleguen al paisaje."),
        ("¿Una consecuencia ocurre antes o después de un hecho?", "Después", "La consecuencia es lo que ocurre a partir del hecho."),
    ],
    [
        ("¿Por qué las zonas con riego suelen tener más cultivos?", "Porque el riego lleva agua a las plantas", "Con agua las plantas crecen."),
        ("¿Por qué donde hay trabajo suelen vivir más personas?", "Porque las familias necesitan ingresos para vivir", "El trabajo atrae a las personas."),
        ("¿Por qué una escuela es un servicio y no una actividad económica?", "Porque ayuda a las personas, aunque no produzca algo para vender", "Los servicios atienden necesidades, como aprender."),
    ],
    [
        ("Un pueblo está en la montaña y recibe mucha nieve en invierno. ¿Qué actividad puede crecer allí: el turismo de nieve o la pesca en el mar?", "El turismo de nieve", "La nieve atrae visitantes que practican deportes de invierno."),
        ("Una bahía tiene aguas tranquilas y gran cantidad de peces. ¿Qué actividad usa directamente esos peces: la pesca o la minería?", "La pesca", "Los peces y las aguas tranquilas permiten pescar."),
        ("Un pueblo de 2.000 habitantes pierde 150 por la falta de empleo. ¿Cuántos habitantes quedan?", "1.850", "2.000 menos 150 es 1.850.", "2000-150"),
    ],
    [
        ("Eva dice: «Si una localidad tiene turismo, no necesita servicios como consultorio». ¿Qué error comete?", "Los turistas y los vecinos necesitan servicios para vivir bien", "Los servicios sirven a todas las personas."),
        ("Un pueblo de montaña quiere que lleguen más turistas. Una propuesta es mejorar el camino y la otra es poner más avisos publicitarios. ¿Cuál resuelve una causa del problema si los turistas no llegan por un camino malo?", "Mejorar el camino", "Resuelve la dificultad concreta de llegar."),
    ],
    [
        ("Ordena la cadena: A) llegan nuevos servicios, B) se instala una empresa de fruta, C) más familias llegan por trabajo.", "B, C, A", "Primero la empresa, luego la llegada de familias y después los servicios."),
        ("Dos pueblos, uno de costa y otro de valle. ¿Cuál tendrá más probabilidad de pescar como actividad principal?", "El de la costa", "La pesca necesita mar."),
    ],
    [("Un pueblo del valle cultiva fruta. Hay una sequía y el río lleva poca agua. ¿Qué consecuencia es más probable en la cosecha: que aumente o que disminuya?", "Que disminuya", "Con menos agua se cultiva menos fruta.")],
    [("En Historia: ¿Qué es una causa?", "La razón por la que algo ocurre", "Es la definición de la clase."), ("¿Qué actividad favorece una costa con puerto?", "La pesca y el comercio", "El mar y el puerto lo hacen posible."), ("¿Qué actores participan en un cambio de una localidad?", "Familias, comerciantes, trabajadores y municipalidad", "Hay varios grupos, no uno solo.")],
    (
        "Elige uno de estos casos y escribe una cadena de causa, actividad y dos consecuencias (una buena y una difícil). Caso a) Una localidad costera instala un nuevo puerto. Caso b) Un valle seco recibe riego por primera vez. Caso c) Un pueblo de montaña mejora su camino.",
        "Caso c: causa: camino mejorado; actividad: turismo; consecuencias: más trabajo, pero más ruido y basura.",
        ["nombra la causa y la actividad", "incluye una consecuencia buena y una difícil", "menciona al menos un actor"],
        ["cadena escrita en cuatro partes"],
        ["decir que todo es positivo", "no nombrar actores"],
        "Lee tu cadena a una persona de tu casa y pídele que diga qué consecuencia le parece más importante.",
    ),
    "Escribe una actividad de tu localidad y el rasgo del lugar que la hace posible.",
    "Escribe un cambio que mejoraría tu localidad y a qué actores involucraría.",
)

# ================================================================ OA 13 · clase 4
lesson(
    OA13, 4,
    "Aprenderé a comparar dos localidades con criterios físicos, humanos y económicos, y a reconocer perspectivas distintas de quienes viven en ellas. Sirve para entender que no hay una sola forma de vivir en Chile.",
    ["Sé relacionar relieve, clima y actividades.", "Sé usar fuentes con su procedencia."],
    [
        "Comparar dos localidades es ver en qué se parecen y en qué cambian, usando los mismos criterios. Aquí los criterios son tres: características físicas (relieve y clima), características humanas (población y servicios) y características económicas (actividades). Si usamos criterios distintos para cada una, la comparación no es justa.",
        "Veamos un ejemplo inventado. Puerto Brisa está en la costa, tiene 8.000 habitantes y vive de la pesca y el turismo. Valle Sol está en un valle, tiene 2.000 habitantes y vive de la agricultura. Las dos son localidades de Chile, pero sus actividades dependen de su relieve y de su población.",
        "Las personas ven su localidad desde su situación. Un pescador valora el mar. Una agricultora valora el agua del canal. Un comerciante valora que lleguen turistas. Eso se llama perspectiva. Al comparar, no decimos que una localidad es mejor; decimos qué ofrece cada una y qué necesita.",
    ],
    [("criterio", "regla igual para comparar dos cosas"), ("semejanza", "algo en que dos lugares se parecen"), ("diferencia", "algo en que dos lugares cambian"), ("perspectiva", "mirada de una persona según su situación"), ("población", "cantidad de personas que viven en un lugar")],
    [
        ("Comparar con criterios", "Puerto Brisa (costa, 8.000 habitantes, pesca) y Valle Sol (valle, 2.000 habitantes, agricultura). Compara el criterio «población».", ["Miro los habitantes de cada una.", "8.000 es mayor que 2.000.", "Puerto Brisa tiene más población."], "Puerto Brisa tiene más habitantes que Valle Sol"),
        ("Una semejanza", "En Puerto Brisa y en Valle Sol hay personas que trabajan con recursos de la naturaleza. ¿Qué semejanza hay?", ["En una se pesca y en la otra se cultiva.", "Ambas actividades usan recursos naturales.", "Esa es la semejanza."], "En ambas se aprovechan recursos naturales"),
    ],
    [
        ("Decir que una localidad es mejor porque tiene más habitantes.", "Tener más población no dice si una localidad es mejor.", "Compara con criterios y no juzgues."),
        ("Comparar la economía de una y la naturaleza de la otra.", "No se compara lo mismo.", "Usa el mismo criterio en ambas."),
    ],
    [
        ("Una diferencia, ¿es en lo que dos lugares se parecen o en lo que cambian?", "En lo que cambian", "Lo que se parece es la semejanza."),
        ("Una localidad de costa y otra de valle, ¿tienen el mismo relieve o distinto?", "Distinto", "La costa está junto al mar y el valle entre cerros."),
        ("Comparar con los mismos criterios, ¿hace la comparación más justa o menos justa?", "Más justa", "Se mide lo mismo en ambas."),
    ],
    [
        ("¿Por qué el pescador de Puerto Brisa y la agricultora de Valle Sol pueden valorar distinto su localidad?", "Porque sus trabajos y necesidades son distintos", "Eso es tener perspectivas distintas."),
        ("¿Por qué una localidad con pocos habitantes puede necesitar menos servicios que una con muchos?", "Porque hay menos personas que atender", "Los servicios dependen en parte de cuántas personas viven allí."),
        ("¿Por qué no se dice que una localidad es mejor que otra?", "Porque cada una ofrece y necesita cosas distintas", "No hay un solo modo de vivir bien."),
    ],
    [
        arith("Tabla de ejemplo: Puerto Azul tiene 9.500 habitantes y Valle Luz 3.500. ¿Cuántos habitantes más tiene Puerto Azul?", "9500-3500", "Se resta la población menor a la mayor.", " habitantes"),
        ("Tabla de ejemplo, actividad principal: Puerto Azul, turismo; Valle Luz, ganadería (cría de vacas). Según el criterio «actividad económica», ¿en qué se diferencian?", "En el tipo de actividad: una atiende turistas y la otra cría vacas", "El criterio es la actividad y cada lugar tiene una distinta."),
        ("Tabla de ejemplo: en Puerto Azul llueve poco y hay brisa del mar; en Valle Luz llueve poco y hay un canal de riego. ¿Qué semejanza hay en su clima?", "En ambas llueve poco", "Ese rasgo físico es igual en las dos."),
    ],
    [
        ("Marta dice: «Valle Sol es peor que Puerto Brisa porque tiene menos gente». ¿Qué error comete?", "Juzga con un solo dato y no compara con criterios", "La cantidad de gente no mide si un lugar es mejor."),
        ("Una agricultora dice que el canal de riego es lo más importante de su localidad y un comerciante dice que lo más importante es el camino. ¿Son perspectivas iguales o distintas?", "Distintas", "Cada uno valora lo que necesita para su trabajo."),
    ],
    [
        ("Ordena las localidades de ejemplo de más a menos habitantes: Villa A, 1.500; Villa B, 6.000; Villa C, 3.200.", "Villa B, Villa C, Villa A", "6.000 es mayor que 3.200 y este mayor que 1.500."),
        ("Una localidad tiene 4.000 habitantes y la mitad trabaja en la pesca. ¿Cuántos trabajan en la pesca?", "2.000", "La mitad de 4.000 es 2.000.", "4000//2"),
    ],
    [("Dos localidades se comparan con el criterio «servicios». Una tiene escuela y consultorio; la otra solo tiene escuela. ¿En cuál falta un servicio de salud?", "En la que solo tiene escuela", "La otra tiene escuela, pero no consultorio.")],
    [("¿Para qué sirve usar criterios iguales?", "Para comparar lo mismo en ambos lugares", "Así la comparación es justa."), ("¿Qué es una perspectiva?", "La mirada de una persona según su situación", "Es la definición de la clase."), ("¿Una localidad es mejor porque tiene más gente?", "No", "Se comparan con criterios, no se juzgan.")],
    (
        "Completa una tabla para comparar Puerto Brisa (costa, 8.000 habitantes, pesca y turismo) y Valle Sol (valle, 2.000 habitantes, agricultura). Filas: relieve, habitantes y actividad. Luego escribe una semejanza, una diferencia y qué opinaría un pescador y una agricultora de cada lugar.",
        "Relieve: costa y valle. Habitantes: 8.000 y 2.000. Actividad: pesca y agricultura. Semejanza: ambas usan recursos naturales. Diferencia: tamaño de la población.",
        ["usa los mismos criterios en ambas", "escribe una semejanza y una diferencia", "diferencia las perspectivas de los dos trabajadores"],
        ["tabla de tres filas y tres frases"],
        ["comparar con criterios distintos", "juzgar cuál localidad es mejor"],
        "Lee tu tabla a una persona de tu casa y pídele que señale si comparaste lo mismo en ambas.",
    ),
    "Escribe una semejanza entre tu localidad y otra que conozcas.",
    "Escribe una pregunta que le harías a una persona de otra localidad para comparar con la tuya.",
)
