"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 1 (parte 3): OAD-03, desarrollo político, económico, social y medioambiental de Chile en el siglo XIX y primera mitad del siglo XX, con la perspectiva de pueblos indígenas y mujeres. Fuentes y cifras de práctica inventadas («de ejemplo»), en papel."""
from __future__ import annotations

from epja_hgcs_nm1_a_common import build, PRIOR_BASE

O = "EPJA-HGCS-NM1-OAD-03"

# ======================================================= clase 1
F1 = ("Ficha 1. Línea de tiempo de hechos de la historia de Chile (hechos estándar de los textos escolares). "
      "1818: se declara la independencia de Chile. "
      "1833: se aprueba una Constitución que da amplias atribuciones al presidente. "
      "1861 a 1883: el Estado avanza sobre el territorio mapuche al sur del río Biobío (ocupación de la Araucanía). "
      "1879 a 1884: Guerra del Pacífico, en que Chile se enfrenta a Perú y Bolivia, con disputa por territorio y por recursos del desierto, como el salitre. "
      "1891: guerra civil. "
      "1925: se aprueba una nueva Constitución. "
      "1949: las mujeres obtienen el derecho a voto en elecciones presidenciales y parlamentarias.")
build(
    O, 1, F1,
    use="Hoy parto de lo que ya sé de Chile para ubicar hechos en una línea de tiempo y reconocer cuatro dimensiones del desarrollo: política, economía, sociedad y medioambiente.",
    prior=PRIOR_BASE + ["Sé que Chile es una república y que sus leyes principales están en una Constitución."],
    explain=[
        "Ya conoces huellas de la historia de Chile en la vida diaria: una plaza, una estación, una escuela, una votación. Muchas cosas que hoy usamos se formaron en el siglo XIX y en la primera mitad del siglo XX. Esta clase pone esos hechos en orden para entender qué cambió y qué se mantuvo.",
        "Para caracterizar el desarrollo de un país se miran cuatro dimensiones. La dimensión política trata del gobierno, las leyes y el voto. La económica, de cómo se produce, se vende y se trabaja. La social, de cómo viven los distintos grupos de personas, incluidas las mujeres y los pueblos indígenas. La medioambiental, de cómo se usan los bosques, el agua y la tierra.",
        "Una línea de tiempo no cuenta todo, pero ayuda a ver el orden y la distancia entre los hechos. Algunos duran un instante, como una votación, y otros son procesos largos, como la ocupación de la Araucanía. Más adelante verás cada dimensión con más detalle y desde varias perspectivas.",
    ],
    vocab=[("república", "forma de gobierno en que las autoridades se eligen y se rigen por leyes"), ("Constitución", "ley principal que organiza el Estado y los derechos"), ("dimensión", "aspecto desde el cual se estudia un tema: política, económica, social, medioambiental"), ("proceso largo", "conjunto de cambios que duran muchos años"), ("sufragio", "derecho a votar")],
    worked=[
        ("Ordenar en el tiempo", "{F} ¿Qué ocurrió primero: la Guerra del Pacífico o la guerra civil de 1891?", ["Miro las fechas: la Guerra del Pacífico fue de 1879 a 1884.", "La guerra civil fue en 1891, después."], "Primero la Guerra del Pacífico"),
        ("Calcular una distancia", "{F} ¿Cuántos años pasaron entre la independencia y el voto femenino de 1949?", ["Leo las fechas: 1818 y 1949.", "Resto 1949 menos 1818."], "131 años"),
    ],
    mistakes=[("Pensar que la historia de Chile comienza en 1818, con la independencia.", "Se olvida que antes ya vivían pueblos indígenas en el territorio.", "Reconoce que la independencia es un hito dentro de una historia más larga."),
              ("Creer que un hecho es solo político o solo económico.", "Los hechos tienen varias dimensiones a la vez.", "Pregunta qué dimensiones tiene cada hecho.")],
    T=[
        ("abc", "{F} ¿En qué año se declara la independencia de Chile?", "1818", "1833", "1879", "La línea de tiempo indica 1818 para la independencia."),
        ("ab", "{F} ¿Qué hecho ocurrió en 1925?", "Se aprobó una nueva Constitución", "Terminó la Guerra del Pacífico", "La ficha indica una nueva Constitución en 1925."),
        ("En Historia: ¿cómo se llama la ley principal que organiza el Estado y los derechos?", "Constitución", "La Constitución es la ley fundamental de un Estado."),
        ("=", "{F} ¿Cuántos años duró la Guerra del Pacífico, de 1879 a 1884?", "1884-1879", "Se restan el año final y el inicial para calcular su duración.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1833 y la de 1925?", "1925-1833", "Se restan las fechas de ambas constituciones.", " años"),
        ("abc", "{F} ¿Qué hecho de la ficha dura muchos años y es un proceso largo?", "La ocupación de la Araucanía, de 1861 a 1883", "La declaración de independencia de 1818", "La aprobación de la Constitución de 1925", "Las fechas 1861 y 1883 muestran que fue un proceso de más de veinte años."),
        ("ab", "En Historia: ¿a qué dimensión corresponde el derecho a voto de las mujeres?", "Política", "Medioambiental", "El voto es un derecho político: define quiénes participan en las elecciones."),
        ("=", "{F} ¿Cuántos años duró la ocupación de la Araucanía, de 1861 a 1883?", "1883-1861", "Se resta el año de inicio al de término para saber su duración.", " años"),
        ("abc", "{F} Una persona dice: «Antes de 1818 en Chile no había nadie». ¿Qué corrección corresponde?", "Ya vivían pueblos indígenas en el territorio", "Es cierto: había un territorio vacío", "Solo vivía población europea", "La independencia es un hito, pero los pueblos indígenas ya habitaban el territorio."),
        ("abc", "{F} ¿Qué dimensiones tiene la Guerra del Pacífico?", "Política y económica, pues hubo disputa por territorio y recursos", "Solo medioambiental", "Solo social", "Fue un conflicto entre Estados y por riquezas del desierto, por eso toca dos dimensiones."),
        ("abc", "{F} ¿Cuál es una buena pregunta para caracterizar el desarrollo social del siglo XIX?", "¿Cómo vivían las mujeres, los trabajadores y los pueblos indígenas?", "¿Cuántos kilómetros de ferrocarril había en 1900?", "¿Qué dice la Constitución sobre las atribuciones del presidente?", "La dimensión social se refiere a cómo viven los distintos grupos de personas."),
        ("ab", "{F} Entre 1818 y 1949 hubo muchos cambios. ¿Qué se mantuvo?", "Que Chile siguió siendo una república", "Que el presidente tuvo siempre las mismas atribuciones", "La ficha no muestra monarquía y habla de Constituciones de república; las atribuciones cambiaron."),
        ("abc", "{F} ¿Por qué la línea de tiempo no basta para caracterizar el desarrollo del país?", "Solo ordena hechos y falta explicar sus dimensiones y perspectivas", "Porque no tiene fechas", "Porque está escrita en papel", "La línea muestra el orden, pero no explica cómo vivían las personas ni sus causas."),
    ],
    ctx=("abc", "Una agrupación de mujeres adultas de ejemplo prepara una charla sobre el derecho a voto. Tiene estos datos: «Voto de las mujeres en elecciones municipales: 1934. En elecciones presidenciales y parlamentarias: 1949». ¿Cuántos años pasaron entre ambos hitos?", "15 años", "10 años", "25 años", "1949 menos 1934 son 15 años de diferencia."),
    sc=[("¿Cuáles son las cuatro dimensiones?", "Política, económica, social y medioambiental", "Esas dimensiones permiten caracterizar el desarrollo de un país."),
        ("En la historia de Chile: ¿cómo se define una Constitución?", "La ley principal que organiza el Estado", "Define las bases del gobierno y los derechos."),
        ("¿La historia de Chile empieza en 1818?", "No, antes ya vivían pueblos indígenas", "La independencia es un hito dentro de una historia más larga.")],
    op=("Con esta lista de hechos de ejemplo escribe cuál es político, cuál económico, cuál social y cuál medioambiental: «Se instala un telégrafo en el pueblo; una asociación de obreras funda una mutual para ayudarse en enfermedades; se quema un bosque para sembrar trigo; se aprueba una ley que cambia cómo se elige a los diputados». "
        "Después escribe una frase que explique por qué un mismo hecho puede tener más de una dimensión.",
        "Político: la ley que cambia la elección de diputados. Económico: el telégrafo, que ayuda al comercio. Social: la mutual de obreras. Medioambiental: la quema del bosque. Un mismo hecho puede tener más de una dimensión: por ejemplo, quemar un bosque para sembrar trigo es económico (se produce trigo) y medioambiental (se pierde bosque).",
        ["clasifica los cuatro hechos con una razón", "usa el vocabulario de dimensiones", "explica la multiplicidad de dimensiones"],
        ["una tabla con cuatro filas y una frase"], ["clasificar sin explicar", "olvidar que un hecho tiene varias dimensiones"],
        "Pregunta: «¿Qué dimensión es la más importante en este hecho y qué otra también aparece?»."),
    reinforce="Piensa en un cambio que hayas visto o escuchado contar en un barrio o pueblo y ubícalo en una dimensión (política, económica, social o medioambiental).",
    extend="Explica con un ejemplo por qué una línea de tiempo no incluye todas las voces de la historia.",
)

# ======================================================= clase 2
F2 = ("Ficha 2. Hechos políticos de Chile, siglo XIX y comienzos del XX (hechos estándar de los textos escolares). "
      "Constitución de 1833: organiza una república con un presidente de amplias atribuciones y un Congreso. "
      "Votaban solo algunos hombres que cumplían ciertos requisitos; las mujeres y gran parte de la población no votaban. "
      "1891: guerra civil entre el presidente y el Congreso; después se instala un régimen parlamentario hasta 1925, en que el Congreso tiene más poder. "
      "1925: nueva Constitución que devuelve al presidente un papel fuerte. "
      "Voto de las mujeres: elecciones municipales desde 1934; presidenciales y parlamentarias desde 1949.")
build(
    O, 2, F2,
    use="Hoy reconozco el vocabulario del desarrollo político de Chile y distingo qué cambió y qué se mantuvo entre 1833 y 1949.",
    prior=PRIOR_BASE + ["Conozco las cuatro dimensiones del desarrollo y sé ubicar hechos en una línea de tiempo."],
    explain=[
        "Un Estado es la organización que gobierna un territorio, con leyes, autoridades e instituciones. En el siglo XIX, Chile se organizó como república, con una Constitución, un presidente y un Congreso. La Constitución de 1833 dio gran poder al presidente y estuvo vigente hasta 1925, aunque con reformas.",
        "El sufragio, el derecho a votar, no era universal: votaban pocos hombres con requisitos. Las mujeres obtuvieron el voto municipal en 1934 y el voto en elecciones presidenciales y parlamentarias en 1949. Muchas personas, por ser mujeres, por ser pobres o por ser indígenas, tuvieron muy poca participación en las decisiones.",
        "En 1891 hubo una guerra civil entre el presidente y el Congreso. Después, hasta 1925, el Congreso tuvo más poder: es el llamado régimen parlamentario. Con la Constitución de 1925 se volvió a un presidente fuerte. Esto muestra continuidades (siempre hubo república y Constitución) y cambios (quién tiene el poder y quién puede votar).",
    ],
    vocab=[("Estado", "organización que gobierna un territorio con leyes e instituciones"), ("Congreso", "grupo de personas elegidas que hacen las leyes"), ("régimen parlamentario", "sistema en que el Congreso tiene más poder que el presidente"), ("sufragio universal", "derecho de todas las personas adultas a votar"), ("participación política", "intervención de las personas en las decisiones de su sociedad")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años duró el régimen parlamentario, de 1891 a 1925?", ["Leo las fechas: 1891 y 1925.", "Resto 1925 menos 1891."], "34 años"),
        ("Reconocer una continuidad política", "{F} ¿Qué se mantuvo entre la Constitución de 1833 y la de 1925?", ["Comparo ambos momentos: en los dos hay república, Constitución y presidente.", "Lo que cambió fue el reparto del poder en el periodo 1891-1925 y quiénes votaban."], "Se mantuvo la república con Constitución y presidente"),
    ],
    mistakes=[("Creer que en el siglo XIX votaba toda la población adulta.", "Hoy el voto es universal y se supone que siempre fue así.", "Revisa quiénes tenían derecho a votar según la ficha."),
              ("Confundir el régimen parlamentario con la ausencia de presidente.", "Se piensa que «parlamentario» elimina al presidente.", "Recuerda que había presidente, pero con menos poder que el Congreso.")],
    T=[
        ("abc", "{F} ¿Qué organizó la Constitución de 1833?", "Una república con presidente y Congreso", "Una monarquía", "Un Estado sin leyes", "La ficha dice que organiza una república con presidente y Congreso."),
        ("ab", "En Historia: ¿qué es el sufragio?", "El derecho a votar", "El pago de impuestos", "Sufragio es el derecho a participar eligiendo autoridades."),
        ("{F} ¿En qué año se aprobó la Constitución que reemplazó a la de 1833?", "1925", "La ficha dice que la nueva Constitución es de 1925."),
        ("abc", "{F} ¿Quiénes votaban en la mayor parte del siglo XIX?", "Algunos hombres con requisitos", "Todas las personas adultas", "Solo las mujeres", "La ficha dice que votaban solo algunos hombres con requisitos."),
        ("ab", "{F} ¿En qué elecciones votaron las mujeres desde 1934?", "En las municipales", "En las presidenciales", "Según la ficha, desde 1934 podían votar en elecciones municipales."),
        ("=", "{F} ¿Cuántos años pasaron entre el voto femenino municipal (1934) y el presidencial y parlamentario (1949)?", "1949-1934", "Se restan las dos fechas para conocer el tiempo transcurrido.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1833 y la guerra civil de 1891?", "1891-1833", "Se restan las dos fechas para conocer el tiempo transcurrido.", " años"),
        ("abc", "{F} ¿Qué cambió con la guerra civil de 1891?", "El Congreso pasó a tener más poder que el presidente", "Chile dejó de ser república", "Las mujeres obtuvieron el voto", "La ficha indica que después de 1891 el Congreso tuvo más poder."),
        ("abc", "{F} ¿Qué se mantuvo entre 1833 y 1949 en el aspecto político?", "Que Chile siguió siendo una república con Constitución", "Que todas las personas votaban", "Que no había Congreso", "En todo el periodo hubo república y Constitución."),
        ("abc", "{F} Una persona dice: «Con la Constitución de 1925 votaron todas las mujeres en todas las elecciones». ¿Qué dice la ficha?", "Que el voto presidencial femenino llegó en 1949", "Que sí votaron en 1925", "Que nunca votaron", "El voto presidencial y parlamentario de las mujeres es de 1949."),
        ("ab", "{F} ¿Qué limitaba la participación política en el siglo XIX?", "Los requisitos para votar y la exclusión de las mujeres", "La ausencia de una Constitución", "Según la ficha, solo votaban algunos hombres con requisitos y las mujeres no votaban."),
        ("abc", "{F} ¿Qué conclusión se sostiene con la ficha?", "Cambió quién tenía poder y quién votaba, pero siguió la república con Constitución", "No cambió nada en el poder político", "Todo cambió, también la forma de gobierno", "Solo esa conclusión muestra a la vez cambio y continuidad con datos de la ficha."),
        ("abc", "{F} ¿Qué pregunta ayuda a pensar en las personas que no votaban?", "¿Cómo participaban en la comunidad aunque no votaran?", "¿Cuántos años tenía la Constitución?", "¿Quién escribió la ficha?", "Pensar en la participación fuera del voto reconoce a quienes no tenían ese derecho."),
    ],
    ctx=("abc", "Una dirigente vecinal de ejemplo prepara una charla sobre el voto en su comuna. Tiene este dato: «En 1900, de 10.000 habitantes adultos de ejemplo, podían votar 1.000 hombres». ¿Qué porcentaje podía votar?", "10 %", "1 %", "100 %", "1.000 entre 10.000 es 0,1, es decir, el 10 %."),
    sc=[("¿Qué es el régimen parlamentario?", "Un sistema en que el Congreso tiene más poder", "En Chile duró de 1891 a 1925."),
        ("¿Qué es el sufragio universal?", "El derecho de todas las personas adultas a votar", "Es lo contrario de un voto con requisitos."),
        ("¿En qué año votaron mujeres en elecciones presidenciales por primera vez según la ficha?", "Desde 1949", "La ficha indica 1949 para el voto presidencial femenino.")],
    op=("Escribe una frase corta sobre cada uno de estos tres momentos usando la ficha: Constitución de 1833, régimen parlamentario (1891-1925) y voto femenino (1934 y 1949). "
        "Luego escribe una frase que diga una continuidad y otra que diga un cambio político entre 1833 y 1949.",
        "1833: se organiza una república con presidente fuerte y Congreso. 1891-1925: el Congreso tiene más poder que el presidente. 1934 y 1949: las mujeres votan primero en elecciones municipales y después en las presidenciales y parlamentarias. Continuidad: siempre hubo república con Constitución. Cambio: se amplió quiénes podían votar, al incluir a las mujeres.",
        ["usa bien las fechas de la ficha", "nombra una continuidad y un cambio", "el lenguaje es claro y respetuoso"],
        ["cinco frases breves"], ["confundir fechas", "decir que votaba toda la población"],
        "Pregunta: «¿Dónde dice la ficha esta fecha o este dato?»."),
    reinforce="Anota, según lo que sabes, quiénes pueden votar hoy en Chile y compáralo con lo que decía la ficha para el siglo XIX.",
    extend="Explica con un ejemplo por qué ampliar el sufragio cambia la política de un país.",
)

# ======================================================= clase 3
F3 = ("Ficha 3. Economía y medioambiente de Chile (hechos estándar de los textos escolares) y datos de práctica. "
      "Hacia mediados del siglo XIX, Chile exportaba sobre todo trigo, plata y cobre, y en 1851 comenzó a funcionar el primer ferrocarril del país, que unía Caldera y Copiapó para llevar minerales. "
      "Después de la Guerra del Pacífico, Chile incorporó territorios del norte donde había salitre, y este pasó a ser la principal exportación hasta comienzos del siglo XX. "
      "Más tarde, la competencia del salitre sintético provocó una crisis. "
      "Medioambiente: para sembrar trigo en el sur se despejaron bosques, muchas veces con fuego; y la minería del norte usó leña como combustible. "
      "Datos de práctica, inventados: un fundo de ejemplo tenía 1.000 hectáreas de bosque en 1860 y 400 hectáreas en 1920.")
build(
    O, 3, F3,
    use="Hoy caracterizo la economía de exportación de materias primas de Chile y su efecto en el medioambiente, con datos de práctica en papel.",
    prior=PRIOR_BASE + ["Conozco las dimensiones del desarrollo y sé calcular una diferencia y un porcentaje."],
    explain=[
        "La economía chilena del siglo XIX se basó en exportar materias primas: primero trigo, plata y cobre, y después de la Guerra del Pacífico, el salitre, que se usaba como fertilizante. Al exportar materias primas, la economía depende de los precios y de la demanda de otros países. Cuando apareció el salitre sintético, la exportación chilena entró en crisis.",
        "Esa economía tuvo un impacto social: crecieron puertos y ciudades, apareció una clase trabajadora minera y se construyeron ferrocarriles, como el de Caldera a Copiapó en 1851. También tuvo efectos en el medioambiente: para sembrar se despejaron bosques, muchas veces con fuego, y la minería usó leña como combustible.",
        "Un impacto ambiental se mide con datos. Si un fundo pasó de 1.000 a 400 hectáreas de bosque, perdió 600 hectáreas, es decir, el 60 %. Esos datos no dicen qué hacer, pero muestran un proceso que se puede comparar con el presente. Una buena caracterización menciona ganancias, costos y a quiénes afectó cada cosa.",
    ],
    vocab=[("exportación", "venta de productos a otros países"), ("salitre", "mineral del desierto del norte que se exportaba como fertilizante"), ("ferrocarril", "transporte sobre rieles que une minas, campos y puertos"), ("impacto ambiental", "cambio que una actividad produce en la naturaleza"), ("dependencia económica", "situación en que un país necesita vender un producto a otros")],
    worked=[
        ("Calcular una pérdida", "{F} ¿Cuántas hectáreas de bosque perdió el fundo de ejemplo entre 1860 y 1920?", ["Leo las hectáreas: 1.000 en 1860 y 400 en 1920.", "Resto 1.000 menos 400."], "600 hectáreas"),
        ("Relacionar un hecho con una dimensión", "{F} ¿A qué dimensión pertenece despejar bosques para sembrar trigo?", ["Tiene un fin económico: producir trigo para vender.", "Pero también cambia la naturaleza: se pierde bosque."], "Económica y medioambiental"),
    ],
    mistakes=[("Creer que la economía solo creció y no tuvo costos.", "Se mira lo que se ganó y se olvidan los impactos en el ambiente y en las personas.", "Pregunta siempre qué se ganó, qué se perdió y quiénes quedaron fuera."),
              ("Pensar que la crisis del salitre fue un hecho solo chileno.", "No se considera que dependía de lo que ocurría en otros países.", "Recuerda que una economía exportadora depende de la demanda y de nuevos productos en el mundo.")],
    T=[
        ("abc", "{F} ¿Qué exportaba sobre todo Chile hacia mediados del siglo XIX?", "Trigo, plata y cobre", "Solo máquinas", "Solo salitre", "La ficha indica trigo, plata y cobre."),
        ("ab", "{F} ¿Qué unía el ferrocarril de 1851?", "Caldera y Copiapó", "Santiago y Valparaíso", "La ficha dice que el primer ferrocarril unía Caldera y Copiapó."),
        ("{F} ¿Qué producto fue la principal exportación después de la Guerra del Pacífico?", "El salitre", "La ficha dice que el salitre pasó a ser la principal exportación."),
        ("=", "{F} ¿Cuántos años pasaron entre el primer ferrocarril (1851) y el comienzo de la Guerra del Pacífico (1879)?", "1879-1851", "Se restan las dos fechas para conocer el tiempo transcurrido.", " años"),
        ("=", "{F} ¿Qué porcentaje del bosque de 1860 perdió el fundo hasta 1920?", "600*100//1000", "Se divide lo perdido por lo que había al inicio y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué provocó la crisis del salitre?", "La competencia del salitre sintético", "El cierre de los puertos", "Una ley de 1833", "La ficha indica que el salitre sintético provocó la crisis."),
        ("abc", "{F} ¿Cuál fue un efecto ambiental de la economía de exportación?", "El despeje de bosques para sembrar y el uso de leña en la minería", "El aumento de los bosques nativos", "La limpieza de los ríos", "Esos dos efectos están en la ficha."),
        ("abc", "{F} Un estudiante dice: «Exportar materias primas no tuvo ningún costo». ¿Qué responde un análisis cuidadoso?", "Hubo costos ambientales y dependencia de la demanda externa", "Que no hubo costos en ningún aspecto", "Que solo tuvo costos y ningún beneficio", "La ficha muestra beneficios, pero también pérdida de bosque y crisis por la competencia."),
        ("ab", "{F} ¿Qué relación hay entre el ferrocarril de 1851 y la minería?", "El ferrocarril llevaba minerales", "El ferrocarril producía el cobre", "Según la ficha, el tren de Caldera a Copiapó se usó para llevar minerales."),
        ("abc", "{F} ¿Qué es la dependencia económica en este caso?", "Que la economía necesitaba vender trigo, cobre o salitre a otros países", "Que Chile no vendía nada", "Que Chile era gobernado por otro país", "Una economía exportadora depende de lo que compren otros."),
        ("abc", "{F} ¿Cuál es una conclusión bien apoyada en la ficha?", "La economía creció con las exportaciones, pero tuvo costos ambientales y dependencia externa", "La economía chilena nunca dependió de otros países", "Los bosques no se perdieron", "Solo esa conclusión integra beneficios, costos y datos de la ficha."),
        ("abc", "{F} ¿Qué pregunta ayuda a pensar en quiénes quedaron fuera de los beneficios?", "¿Quiénes trabajaban en las minas y cuánto ganaban?", "¿Cuántos pasajeros cabían en cada vagón?", "¿Qué nombre tenía cada locomotora?", "Esa pregunta reconoce a quienes trabajaban y la distribución de las ganancias."),
        ("abc", "{F} Se agrega este dato de práctica: «el fundo perdió bosque, pero aumentó su producción de trigo». ¿Cómo se analiza?", "Como una ganancia económica con un costo ambiental", "Como un hecho solo ambiental", "Como un hecho sin importancia", "Un mismo hecho puede dar un beneficio económico y un costo ambiental."),
    ],
    ctx=("abc", "Una cooperativa agrícola de ejemplo registra: «Bosque nativo del predio: 200 hectáreas en 1950 y 150 en 2000». ¿Qué porcentaje del bosque inicial se perdió?", "25 %", "50 %", "75 %", "Se perdieron 50 hectáreas de 200, es decir, el 25 %."),
    sc=[("¿Qué exportaba Chile después de la Guerra del Pacífico?", "Sobre todo salitre", "El salitre fue la principal exportación en esa época."),
        ("¿Qué es un impacto ambiental?", "Un cambio que una actividad produce en la naturaleza", "Se puede medir con datos, como las hectáreas de bosque."),
        ("¿Por qué una economía exportadora puede entrar en crisis?", "Porque depende de la demanda de otros países", "Si cambia lo que otros compran, la economía se ve afectada.")],
    op=("Caracteriza la economía de un pueblo minero ficticio con estos datos de ejemplo: «El pueblo vive de exportar cobre; en 1880 había 500 mineros y en 1920, 1.500; la leña de los cerros cercanos se usa en las fundiciones; el cerro tenía 2.000 hectáreas de arbustos en 1880 y 800 en 1920». "
        "Calcula cuánto aumentaron los mineros y cuánto bajaron las hectáreas, y escribe una frase que mencione un beneficio, un costo y la dependencia.",
        "Mineros: aumentaron 1.000. Hectáreas: bajaron 1.200. Beneficio: más empleo en la minería. Costo: pérdida de arbustos del cerro por el uso de leña. Dependencia: el pueblo vive de exportar cobre y su economía depende de que otros países lo compren.",
        ["calcula bien", "nombra un beneficio y un costo con datos", "menciona la dependencia"],
        ["dos cálculos y una frase"], ["olvidar el costo", "decir que la economía no dependía de nadie"],
        "Pregunta: «¿Qué ganó y qué perdió el pueblo con esta economía?»."),
    reinforce="Elige uno de los productos de la ficha (trigo, plata, cobre o salitre) y escribe un beneficio y un costo de exportarlo.",
    extend="Explica con un ejemplo por qué una economía basada en un solo producto puede ser frágil.",
)

# ======================================================= clase 4
F4 = ("Ficha 4. Cuatro fuentes de ejemplo, inventadas, sobre cómo vivían distintos grupos en Chile entre 1880 y 1930. "
      "Fuente A (relato de ejemplo de una familia mapuche): «Nuestras tierras eran extensas; después del avance del Estado quedamos en un terreno mucho más pequeño». "
      "Fuente B (aviso de ejemplo de un periódico, 1885): «Se ofrecen tierras del sur a familias colonas para que las cultiven». "
      "Fuente C (carta de ejemplo de una joven, 1885): «Ahora una mujer puede dar exámenes y entrar a la universidad; quiero estudiar medicina». "
      "Fuente D (testimonio de ejemplo de una obrera de una fábrica de textiles, 1915): «Trabajo 12 horas y gano menos que mis compañeros hombres».")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo leer fuentes de distintos grupos (pueblos indígenas, mujeres, trabajadoras y trabajadores) para caracterizar el desarrollo social de Chile.",
    prior=PRIOR_BASE + ["Sé leer una fuente con las preguntas quién, cuándo, para quién y qué dice, y conozco las cuatro dimensiones."],
    explain=[
        "La historia social se interesa por cómo vivían las personas comunes. Para conocerlo hay que escuchar fuentes de varios grupos. En Chile, durante el siglo XIX y comienzos del XX, el Estado avanzó sobre el territorio mapuche al sur del río Biobío y las comunidades quedaron en terrenos mucho más pequeños, llamados reducciones. Las fuentes del Estado y las de las comunidades cuentan este proceso de forma distinta.",
        "Las mujeres también tienen su historia. En 1877 un decreto permitió que las mujeres rindieran exámenes y entraran a la universidad, y en la década de 1880 se titularon las primeras mujeres. Muchas obreras trabajaban en fábricas con salarios menores que los hombres y jornadas largas. El voto femenino llegó en 1934 (municipal) y 1949 (presidencial y parlamentario).",
        "Caracterizar lo social es unir estas perspectivas con respeto: no se opina sobre las personas, se usa lo que dicen las fuentes. Cada fuente es parcial, así que se contrastan. En esta clase todas las fuentes son de ejemplo y no representan a ninguna persona real.",
    ],
    vocab=[("reducción", "terreno pequeño en que quedaron comunidades mapuche tras el avance del Estado"), ("colono", "persona que llega a poblar y cultivar un territorio"), ("brecha salarial", "diferencia de pago entre dos grupos por un trabajo similar"), ("perspectiva", "punto de vista de quien cuenta un hecho"), ("pueblos indígenas", "pueblos que ya habitaban el territorio antes de la formación del Estado")],
    worked=[
        ("Leer una fuente con respeto", "{F} ¿Qué dice con claridad la fuente A?", ["La fuente es un relato de ejemplo de una familia mapuche.", "Dice que después del avance del Estado quedaron en un terreno mucho más pequeño."], "Que la familia perdió gran parte de sus tierras"),
        ("Contrastar dos fuentes", "{F} Compara las fuentes A y B en un punto.", ["La fuente A habla de la pérdida de tierras de una comunidad.", "La fuente B ofrece las tierras del sur a familias colonas.", "Ambas hablan del mismo territorio desde perspectivas opuestas."], "Una muestra la pérdida de tierras y la otra la oferta de esas tierras a colonos"),
    ],
    mistakes=[("Creer que una sola fuente representa a todo un pueblo o a todas las mujeres.", "Se generaliza a partir de un relato.", "Di «esta fuente de ejemplo muestra» y busca más voces."),
              ("Juzgar a las personas del pasado con estereotipos.", "Se rellenan los vacíos con prejuicios.", "Usa solo lo que dicen las fuentes y reconoce lo que no sabes.")],
    T=[
        ("abc", "{F} ¿Quién escribe la fuente C?", "Una joven", "Un colono", "Una autoridad municipal", "La ficha dice que es una carta de ejemplo de una joven."),
        ("ab", "{F} ¿Qué ofrece la fuente B?", "Tierras del sur a familias colonas", "Trabajo en una fábrica de textiles", "El aviso de ejemplo ofrece tierras del sur a familias colonas."),
        ("Sobre los pueblos indígenas de Chile: ¿qué se llamó reducción?", "Un terreno pequeño en que quedaron comunidades mapuche", "Una reducción es el terreno reducido que quedó a las comunidades tras el avance del Estado."),
        ("abc", "{F} ¿Qué dice la fuente D sobre el pago?", "Que gana menos que sus compañeros hombres", "Que gana más que sus compañeros", "Que no recibe pago", "La obrera dice que trabaja 12 horas y gana menos que los hombres."),
        ("=", "{F} Si la obrera de la fuente D trabaja 12 horas al día, ¿cuántas horas trabaja en 6 días?", "12*6", "Se multiplican las horas diarias por los días de la semana de trabajo.", " horas"),
        ("=", "{F} Una escuela de niñas de ejemplo tenía 40 alumnas en 1880 y 120 en 1910. ¿Cuántas alumnas más tenía en 1910?", "120-40", "Se resta el dato de 1880 al de 1910 para ver el aumento.", " alumnas"),
        ("abc", "{F} ¿Qué cambio de derecho aparece en la fuente C?", "Que una mujer ahora puede dar exámenes y entrar a la universidad", "Que una mujer puede votar en todo", "Que las mujeres dejan de trabajar", "La joven habla de acceso a exámenes y universidad, no de voto."),
        ("abc", "{F} ¿Qué muestra la comparación de las fuentes A y B?", "Una pérdida de tierras para una comunidad y una oferta para otras familias", "Que no hubo conflicto por tierras", "Que ambos grupos tenían iguales derechos", "Una fuente muestra la pérdida y la otra la oferta de esas mismas tierras."),
        ("abc", "{F} ¿Qué dimensión social se ve en la fuente D?", "Las condiciones de trabajo y la desigualdad entre hombres y mujeres", "El voto en las elecciones", "El uso del bosque", "La obrera describe su jornada y su pago comparado con los hombres."),
        ("ab", "{F} Una persona dice: «La fuente A prueba que todos los mapuche perdieron todas sus tierras». ¿Qué falla?", "Una sola fuente de ejemplo no permite afirmar eso de todos", "Nada: la fuente lo demuestra todo", "Se necesitan más fuentes para afirmar algo sobre todo un pueblo."),
        ("abc", "{F} ¿Cuál es una buena conclusión sobre la sociedad de la época?", "Había desigualdades entre grupos y distintas perspectivas sobre las mismas tierras y trabajos", "Todos los grupos vivían de igual manera", "No hay datos de nada", "Las fuentes muestran desigualdades y puntos de vista distintos."),
        ("abc", "{F} ¿Qué ayuda a comprender mejor la pérdida de tierras de la fuente A?", "Buscar otras fuentes de comunidades y del Estado y compararlas", "Aceptar solo la fuente B", "Aceptar solo la fuente A", "Contrastar fuentes de ambas partes da una imagen más completa."),
        ("abc", "{F} ¿Qué se necesita para decir que el acceso a la universidad cambió la vida de muchas mujeres?", "Más fuentes, como registros de cuántas mujeres estudiaron", "Nada: la carta C ya lo prueba", "Que otra persona opine", "Una carta muestra un caso; para generalizar hacen falta registros."),
    ],
    ctx=("abc", "En un taller de memoria de una comunidad de ejemplo se lee este testimonio: «Mi abuela contaba que antes cultivaban un campo extenso y después quedaron con un terreno pequeño». ¿Cómo se trata este testimonio?", "Como una fuente oral que se contrasta con otras", "Como un dato inválido por ser un recuerdo", "Como la única verdad sin comparar", "Un testimonio es una fuente válida; se contrasta con registros y otras voces."),
    sc=[("¿Qué es una reducción?", "Un terreno pequeño en que quedaron comunidades mapuche", "Fue una consecuencia del avance del Estado."),
        ("¿Qué permitió el decreto de 1877?", "Que las mujeres rindieran exámenes y entraran a la universidad", "Fue un paso hacia la educación superior de las mujeres."),
        ("En las fuentes sobre Chile: ¿por qué conviene contrastarlas?", "Porque cada fuente muestra una parte", "Comparar permite una imagen más completa.")],
    op=("Lee estas dos fuentes de ejemplo. Fuente 1 (carta de una familia de ejemplo): «Perdimos gran parte de nuestras tierras y tuvimos que irnos a trabajar a la ciudad». Fuente 2 (informe de ejemplo de una oficina estatal): «Se ocuparon tierras del sur y se ofrecieron a familias colonas». "
        "Escribe quién habla en cada una, en qué se parecen, en qué se diferencian y qué otra fuente buscarías.",
        "Habla una familia en la 1 y una oficina estatal en la 2. Se parecen en que ambas se refieren a las tierras del sur. Se diferencian en que una cuenta la pérdida y la otra la ocupación y oferta a colonos. Buscaría un registro de las tierras que tenían las comunidades antes y después.",
        ["identifica quién habla", "compara con respeto", "propone una fuente nueva"],
        ["cuatro frases ordenadas"], ["descartar una fuente", "generalizar a todo un pueblo"],
        "Pregunta: «¿Desde qué situación habla esta fuente y qué parte del proceso muestra?»."),
    reinforce="Si lo deseas, anota una fuente de tu entorno (un relato, una foto) que cuente cómo vivía un grupo hace 50 años y qué te dice; si no, usa una fuente de la ficha 4.",
    extend="Explica con un ejemplo por qué son importantes las voces de mujeres y pueblos indígenas en la historia.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo, inventada). Villa del Valle, localidad ficticia de Chile, entre 1860 y 1930. "
      "Político: en 1860 el alcalde era elegido por pocos vecinos; desde 1934 las mujeres pueden votar en las elecciones municipales. "
      "Económico: en 1860 la villa vivía de la agricultura de trigo; en 1900 llegó el ferrocarril y se instaló una fábrica de conservas. "
      "Social: en 1880 se abrió una escuela de niñas con 40 alumnas; en 1920 había 160. Una comunidad mapuche vecina quedó en un terreno de 500 hectáreas tras perder gran parte de sus tierras. "
      "Medioambiental: se despejaron 300 hectáreas de bosque para sembrar trigo y la quebrada se ensució con desechos de la fábrica.")
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido para caracterizar una localidad con las cuatro dimensiones y la perspectiva de mujeres y pueblos indígenas, y me preparo para hacer lo mismo con mi comunidad.",
    prior=PRIOR_BASE + ["Conozco las cuatro dimensiones, el vocabulario político y económico y la lectura de fuentes de varios grupos."],
    explain=[
        "Caracterizar es describir los rasgos principales de algo con datos. Para una localidad, se arma una ficha con las cuatro dimensiones: política, económica, social y medioambiental. En cada una se anotan hechos con su fecha, se marca qué cambió y qué se mantuvo y se agregan las perspectivas de los grupos que viven allí.",
        "En la ficha de Villa del Valle hay hechos de distintos grupos: pocos vecinos elegían al alcalde, las mujeres pudieron votar en elecciones municipales desde 1934, una escuela de niñas fue creciendo y una comunidad mapuche quedó con un terreno pequeño. Verlos juntos muestra que el mismo proceso, como la llegada del ferrocarril, pudo traer beneficios a unos y costos a otros.",
        "Una buena ficha es breve, ordenada y no inventa. Si falta un dato, se anota como pregunta pendiente. Con tu propia comunidad harás lo mismo: puedes empezar con lo que sabes y completar con fuentes, como registros o relatos de personas mayores, siempre respetando la privacidad de quienes cuentan.",
    ],
    vocab=[("caracterizar", "describir los rasgos principales de algo con datos"), ("ficha de caracterización", "cuadro que ordena hechos por dimensión"), ("localidad", "pueblo o barrio con rasgos propios"), ("beneficio", "ganancia o ventaja que recibe un grupo"), ("costo", "pérdida o dificultad que sufre un grupo")],
    worked=[
        ("Completar una dimensión", "{F} ¿Qué hecho de la ficha pertenece a la dimensión social?", ["Busco hechos sobre cómo viven las personas y los grupos.", "La escuela de niñas con 40 alumnas en 1880 y 160 en 1920 es un hecho social."], "La escuela de niñas que creció de 40 a 160 alumnas"),
        ("Beneficio y costo del mismo hecho", "{F} ¿Qué beneficio y qué costo trajo la fábrica de conservas?", ["Beneficio económico: dio una nueva actividad y empleo a la villa.", "Costo medioambiental: la quebrada se ensució con desechos de la fábrica."], "Beneficio: nueva actividad económica. Costo: contaminación de la quebrada"),
    ],
    mistakes=[("Escribir una ficha con opiniones en lugar de hechos con fecha.", "Se mezcla lo que se piensa con lo que dicen las fuentes.", "Cada línea de la ficha debe tener un dato o una fuente."),
              ("Olvidar las perspectivas de mujeres y pueblos indígenas.", "Se llena la ficha solo con los hechos más visibles.", "Pregunta qué cambió para cada grupo en cada dimensión.")],
    T=[
        ("abc", "{F} ¿Qué llegó a la villa en 1900?", "El ferrocarril", "La escuela de niñas", "El voto de las mujeres", "La ficha indica que el ferrocarril llegó en 1900."),
        ("ab", "{F} ¿En qué dimensión está el hecho «se despejaron 300 hectáreas de bosque»?", "Medioambiental", "Política", "Despejar bosque modifica la naturaleza, por eso es medioambiental."),
        ("{F} ¿Desde qué año pueden votar las mujeres en las elecciones municipales de la villa?", "1934", "La ficha dice que pueden votar desde 1934."),
        ("=", "{F} ¿Cuántas alumnas más tenía la escuela de niñas en 1920 que en 1880?", "160-40", "Se resta el número de alumnas de 1880 al de 1920.", " alumnas"),
        ("=", "{F} ¿Cuántas veces más alumnas había en 1920 que en 1880?", "160//40", "Se divide el dato de 1920 por el de 1880 para compararlos.", " veces"),
        ("=", "{F} ¿Cuántos años pasaron entre la llegada del ferrocarril (1900) y el año desde el cual las mujeres pueden votar en las elecciones municipales (1934)?", "1934-1900", "Se restan ambas fechas para conocer el tiempo transcurrido.", " años"),
        ("abc", "{F} ¿Qué cambio económico ocurrió entre 1860 y 1900?", "De vivir de la agricultura a sumar una fábrica de conservas", "De la fábrica a la agricultura", "No hubo cambio económico", "La ficha muestra trigo en 1860 y ferrocarril y fábrica en 1900."),
        ("abc", "{F} ¿Qué dato muestra una pérdida para una comunidad indígena?", "La comunidad mapuche quedó en 500 hectáreas tras perder gran parte de sus tierras", "La escuela de niñas creció", "Llegó el ferrocarril", "Solo ese dato describe una pérdida para la comunidad."),
        ("abc", "{F} ¿Qué dimensión tiene el derecho a voto municipal de 1934?", "Política y social", "Solo medioambiental", "Solo económica", "Es un derecho político que cambió la participación de las mujeres."),
        ("abc", "{F} ¿Qué conclusión se sostiene con la ficha?", "Villa del Valle cambió en sus cuatro dimensiones, pero con beneficios y costos distintos para cada grupo", "Todos ganaron por igual con el ferrocarril", "No hubo ningún cambio en la villa", "La ficha muestra cambios en cada dimensión y efectos distintos para grupos distintos."),
        ("ab", "{F} Un vecino dice: «La fábrica de conservas trajo solo beneficios a todos los grupos». ¿Qué dato lo contradice?", "La quebrada se ensució con desechos de la fábrica", "La escuela de niñas tuvo más alumnas", "La contaminación de la quebrada es un costo ambiental ligado a la fábrica."),
        ("abc", "{F} ¿Qué pregunta pendiente conviene anotar para la ficha?", "¿Cómo vivió la comunidad mapuche el cambio, según sus propios relatos?", "¿Cuántos vagones tenía cada tren?", "¿Cuántas máquinas tenía la fábrica?", "Falta la voz de la comunidad, y la ficha la deja como pregunta."),
        ("abc", "{F} Si agregas el dato «en 1930 había 3 escuelas más», ¿en qué dimensión lo ubicas?", "Social", "Medioambiental", "Política", "Las escuelas son parte de la vida social y educativa de la localidad."),
    ],
    ctx=("abc", "El comité de memoria de un barrio de ejemplo arma una ficha de su sede vecinal con estos datos: «Fundada en 1950, 20 socios; en 2000, 80 socios; en 2020, 100 socios; en 1950 solo hombres eran socios y desde 1980 hay mujeres». ¿En qué dimensión están los datos?", "Social, porque describen quiénes participan en la organización", "Medioambiental", "Económica solamente", "Los datos muestran cómo cambió la participación de las personas en una organización."),
    sc=[("¿Qué es caracterizar?", "Describir los rasgos principales con datos", "Caracterizar es ordenar hechos con fechas y fuentes."),
        ("¿Qué se hace cuando falta un dato?", "Se anota como pregunta pendiente", "No se inventa lo que no se sabe."),
        ("¿Qué grupos conviene incluir en la ficha?", "Mujeres, pueblos indígenas y trabajadores, además de las autoridades", "Así la ficha muestra distintas perspectivas y no solo una.")],
    op=("Completa una ficha de caracterización para la localidad ficticia Puerto Claro, con estos datos de ejemplo: «Voto: desde 1934 las mujeres votan en elecciones municipales. Economía: en 1880 vivía de la pesca; en 1910 se abrió una conservera. Social: una comunidad indígena vecina perdió parte de sus tierras antes de 1900. Medioambiente: la bahía se llenó de desechos de la conservera». "
        "Ordena los datos en las cuatro dimensiones y escribe una conclusión de dos frases y una pregunta pendiente.",
        "Política: el voto de las mujeres desde 1934. Económica: pasó de la pesca a sumar una conservera en 1910. Social: la comunidad indígena perdió parte de sus tierras. Medioambiental: la bahía se llenó de desechos. Conclusión: Puerto Claro cambió en sus cuatro dimensiones, con ganancias económicas y costos para la comunidad y el ambiente. Pregunta: ¿qué relatos tiene la comunidad indígena sobre esa pérdida?",
        ["ubica bien los datos en las cuatro dimensiones", "la conclusión reconoce beneficios y costos", "incluye una pregunta pendiente"],
        ["una tabla de cuatro filas, dos frases y una pregunta"], ["inventar datos", "olvidar a algún grupo"],
        "Pregunta: «¿Qué dato respalda cada fila de la tabla?»."),
    reinforce="Haz una mini ficha de tu barrio con un hecho para cada una de las cuatro dimensiones, usando solo lo que ya sabes.",
    extend="Explica con un ejemplo por qué una misma actividad económica puede beneficiar a unos y perjudicar a otros.",
)

# ======================================================= clase 6
F6 = ("Ficha 6. Dos resúmenes de ejemplo para evaluar sobre Chile entre 1818 y 1949. "
      "Resumen A: «En el siglo XIX Chile se organizó como república, creció su economía exportando salitre y cobre, y se construyeron ferrocarriles. Fue un progreso para todo el país». "
      "Resumen B: «En el siglo XIX y comienzos del XX Chile fue república con Constitución; la economía exportó trigo, plata, cobre y salitre y dependió de la demanda externa; hubo pérdida de tierras mapuche, jornadas largas para obreras y obreros, cambios en el voto y en la educación de las mujeres, y daño a bosques y aguas». "
      "Datos de apoyo: Guerra del Pacífico 1879-1884; ocupación de la Araucanía 1861-1883; decreto que permite el ingreso de mujeres a la universidad, 1877; voto presidencial femenino, 1949.")
build(
    O, 6, F6,
    use="Hoy reviso lo que aprendí sobre Chile en el siglo XIX y comienzos del XX, evalúo dos resúmenes y decido qué quiero seguir estudiando.",
    prior=PRIOR_BASE + ["He practicado la ficha de caracterización, las fuentes de distintos grupos y las cuatro dimensiones."],
    explain=[
        "Evaluar un resumen es juzgar si está bien apoyado. Se revisan cuatro cosas: ¿incluye las cuatro dimensiones?, ¿menciona a distintos grupos, como las mujeres y los pueblos indígenas?, ¿dice cosas que los datos no respaldan?, ¿reconoce costos además de beneficios? Un buen resumen es corto, pero no deja afuera lo esencial.",
        "Al comunicar el desarrollo de Chile conviene usar una estructura simple: hecho, fecha, dimensión y perspectiva. Por ejemplo: «En 1949 las mujeres obtuvieron el voto presidencial y parlamentario; es un cambio político y social». Con frases así, quien lee puede ver el dato y la razón.",
        "Al terminar, haz tu balance personal: qué términos ya manejas, qué te cuesta y qué quieres revisar. También puedes pensar qué preguntas te quedan, como qué dicen las fuentes de tu comunidad. La historia sigue abierta mientras se hacen nuevas preguntas.",
    ],
    vocab=[("evaluar", "juzgar con criterios si algo está bien apoyado"), ("balance", "revisión de lo logrado y lo pendiente"), ("omisión", "dato importante que se deja fuera"), ("generalización", "afirmar algo para todos a partir de pocos casos"), ("progreso", "avance, que puede tener beneficios y costos")],
    worked=[
        ("Evaluar un resumen", "{F} ¿Qué dimensiones faltan en el resumen A?", ["Reviso las cuatro dimensiones en el texto.", "Menciona la política y la economía, pero no la social ni la medioambiental."], "Faltan la dimensión social y la medioambiental"),
        ("Detectar una generalización", "{F} ¿Qué problema tiene la frase «Fue un progreso para todo el país»?", ["La frase generaliza a todos los grupos.", "Los datos de apoyo muestran pérdida de tierras mapuche y jornadas largas."], "Generaliza: no todos los grupos se beneficiaron"),
    ],
    mistakes=[("Elegir el resumen más corto porque es más fácil de leer.", "Se prefiere la comodidad por sobre la calidad.", "Evalúa con los cuatro criterios, no por el largo."),
              ("Pensar que un resumen más largo siempre es mejor.", "Se confunde cantidad con calidad.", "Revisa si cada dato tiene respaldo y si faltan perspectivas.")],
    T=[
        ("abc", "{F} ¿Cuántas dimensiones nombra expresamente el resumen A?", "Dos", "Cuatro", "Una", "El resumen A habla de política y economía."),
        ("ab", "{F} ¿Qué resumen menciona la pérdida de tierras mapuche?", "El resumen B", "El resumen A", "La pérdida de tierras mapuche aparece solo en el resumen B."),
        ("{F} ¿En qué año se permite el ingreso de mujeres a la universidad, según los datos de apoyo?", "1877", "Los datos de apoyo indican 1877."),
        ("=", "{F} ¿Cuántos años duró la Guerra del Pacífico, según los datos de apoyo?", "1884-1879", "Se resta el año de inicio al de término de la guerra.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el decreto de 1877 y el voto presidencial femenino de 1949?", "1949-1877", "Se restan las dos fechas para conocer el tiempo transcurrido.", " años"),
        ("abc", "{F} ¿Qué omisión tiene el resumen A?", "No menciona costos ni a las mujeres ni a los pueblos indígenas", "Incluye datos de la Guerra del Pacífico", "Cita una fuente de ejemplo", "Habla solo de progreso y deja fuera a varios grupos y costos."),
        ("abc", "{F} ¿Qué tiene de bueno el resumen B?", "Incluye las cuatro dimensiones y distintas perspectivas", "Es el más corto", "No usa datos", "Menciona política, economía, sociedad y medioambiente y a varios grupos."),
        ("abc", "{F} ¿Cuál frase del resumen B corresponde a la dimensión medioambiental?", "Daño a bosques y aguas", "Cambios en el voto", "Jornadas largas para obreros", "El daño a bosques y aguas es un cambio en la naturaleza."),
        ("ab", "{F} ¿Qué parte del resumen B se apoya en el dato de 1949?", "Los cambios en el voto de las mujeres", "La pérdida de tierras mapuche", "El voto femenino de 1949 es parte de los cambios en el voto."),
        ("abc", "{F} Una compañera dice: «El resumen A es mejor porque es más optimista». ¿Qué responderías?", "Que un buen resumen se evalúa por sus datos y perspectivas, no por su ánimo", "Tiene razón: el optimismo importa más", "Que no hay forma de evaluarlos", "Un resumen se evalúa por su respaldo y por incluir a distintos grupos."),
        ("abc", "{F} ¿Cómo mejorarías el resumen A?", "Agregando la dimensión social y medioambiental, y los costos para algunos grupos", "Eliminando todas las fechas", "Repitiendo la palabra progreso", "Agregar dimensiones y perspectivas lo vuelve más completo."),
        ("abc", "{F} Si quisieras comunicar la ocupación de la Araucanía con respeto, ¿qué frase usarías?", "Entre 1861 y 1883 el Estado avanzó sobre el territorio mapuche y las comunidades perdieron gran parte de sus tierras", "Fue un episodio sin importancia", "Fue un progreso sin costo", "Es una frase con fecha, hecho y perspectiva de la comunidad."),
        ("abc", "Terminas la unidad y haces tu balance. ¿Cuál es la mejor decisión?", "Anotar qué término me cuesta y repasarlo con un ejemplo", "No repasar nada", "Estudiar solo lo que ya domino", "Decidir con base en lo que costó hace útil el estudio."),
    ],
    ctx=("abc", "Una agrupación de vecinas de ejemplo prepara una exposición sobre el voto. Quiere poner el cartel «El voto femenino en Chile llegó en 1949». ¿Qué conviene agregar para ser más preciso?", "Que desde 1934 podían votar en elecciones municipales y desde 1949 en las presidenciales y parlamentarias", "Que las mujeres nunca votaron", "Nada, el cartel ya es suficiente", "El cartel simplifica: el voto municipal fue anterior, de 1934."),
    sc=[("¿Qué se revisa al evaluar un resumen?", "Dimensiones, grupos, respaldo y costos", "Esos criterios muestran si el resumen es completo."),
        ("¿Qué es una generalización?", "Afirmar algo para todos a partir de pocos casos", "Puede dejar fuera a grupos importantes."),
        ("¿Para qué sirve un balance personal?", "Para decidir qué repasar y qué seguir estudiando", "Orienta el estudio según lo logrado.")],
    op=("Escribe una síntesis de seis a ocho líneas sobre Chile entre 1818 y 1949 usando esta lista de ejemplo: «república con Constitución; salitre y cobre; ferrocarriles; ocupación de la Araucanía y pérdida de tierras mapuche; voto femenino en 1934 y 1949; obreros y obreras con jornadas largas; daño a bosques». "
        "Incluye las cuatro dimensiones, al menos dos grupos y un costo. Termina con una frase de balance sobre lo que quieres repasar.",
        "Chile fue una república con Constitución (política). Su economía se apoyó en el salitre y el cobre y se construyeron ferrocarriles (económica). Hubo pérdida de tierras mapuche, jornadas largas para obreros y obreras y los cambios en el voto de las mujeres (social). El despeje de bosques dañó la naturaleza (medioambiental). Balance: quiero repasar las fechas del voto femenino.",
        ["incluye las cuatro dimensiones", "menciona al menos dos grupos y un costo", "cierra con un balance"],
        ["un texto breve con balance"], ["omitir dimensiones", "decir que todos se beneficiaron"],
        "Pregunta: «¿Qué dimensión o qué grupo falta en tu síntesis?»."),
    reinforce="Elige una de las cuatro dimensiones y escribe dos hechos sobre ella con su fecha.",
    extend="Explica por qué ampliar los grupos que se incluyen en un relato histórico cambia la forma de entender el pasado.",
)
