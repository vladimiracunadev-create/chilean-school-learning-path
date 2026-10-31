"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 11 (regiones político-administrativas de Chile)."""
from __future__ import annotations

from hi5_lib import build

OA11 = "HI06 OA 11"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 47 (regiones de Chile de norte a sur y sus capitales regionales, hecha para este cuaderno). "
     "1. Arica y Parinacota (Arica). 2. Tarapacá (Iquique). 3. Antofagasta (Antofagasta). 4. Atacama (Copiapó). 5. Coquimbo (La Serena). 6. Valparaíso (Valparaíso). "
     "7. Metropolitana de Santiago (Santiago). 8. Libertador General Bernardo O'Higgins (Rancagua). 9. Maule (Talca). 10. Ñuble (Chillán). 11. Biobío (Concepción). "
     "12. La Araucanía (Temuco). 13. Los Ríos (Valdivia). 14. Los Lagos (Puerto Montt). 15. Aysén del General Carlos Ibáñez del Campo (Coyhaique). 16. Magallanes y de la Antártica Chilena (Punta Arenas). "
     "Zonas: Norte Grande (regiones 1 a 3), Norte Chico (4 y 5), Zona Central (6 a 10), Zona Sur (11 a 14) y Zona Austral (15 y 16). La región de Ñuble se creó en 2018.")
build(
    OA11, 1, F,
    use="Aprenderé a ubicar las 16 regiones de Chile, sus capitales regionales y las zonas geográficas. Sirve para describir dónde está cada región y a qué zona pertenece.",
    prior=["Sé que Chile es largo y angosto.", "Sé reconocer el norte y el sur en un mapa.", "Sé qué es una capital."],
    explain=[
        "Chile se divide en regiones, que son unidades político-administrativas: cada una tiene límites definidos y una capital regional donde funciona el gobierno regional. Hoy el país tiene 16 regiones, numeradas en esta ficha de norte a sur. Una de ellas, Ñuble, se creó en 2018.",
        "Para estudiar el país se agrupan las regiones en cinco zonas geográficas. El Norte Grande incluye Arica y Parinacota, Tarapacá y Antofagasta. El Norte Chico incluye Atacama y Coquimbo. La Zona Central incluye Valparaíso, la Región Metropolitana, O'Higgins, Maule y Ñuble. La Zona Sur incluye Biobío, La Araucanía, Los Ríos y Los Lagos. La Zona Austral incluye Aysén y Magallanes.",
        "Para ubicar una región usamos un mapa y nos fijamos en su posición respecto de otras: al norte, al sur, junto al mar o junto a la cordillera. Conocer la capital regional y la zona facilita describirla. Por ejemplo, Concepción es la capital del Biobío, en la Zona Sur, y Temuco es la capital de La Araucanía.",
    ],
    vocab=[("región", "unidad en que se divide Chile para gobernarlo y administrarlo"), ("capital regional", "ciudad donde funciona el gobierno de una región"), ("zona geográfica", "grupo de regiones con rasgos parecidos"), ("político-administrativo", "relacionado con la forma en que un país se divide para gobernar"), ("Norte Grande", "zona del extremo norte, con desierto")],
    worked=[
        ("Ubicar una capital", "{F} ¿Cuál es la capital de la región de Los Lagos?", ["Busco la región 14.", "Su capital es Puerto Montt."], "Puerto Montt"),
        ("Ubicar una zona", "{F} ¿A qué zona pertenece la región de Coquimbo?", ["Busco la región 5.", "La ficha la ubica en el Norte Chico."], "Al Norte Chico"),
    ],
    mistakes=[("Creer que la capital de Chile es la capital de todas las regiones.", "Se confunde la capital nacional con las regionales.", "Cada región tiene su propia capital regional."),
              ("Contar 15 regiones.", "Se olvida alguna región, como Ñuble.", "Hoy son 16 regiones.")],
    T=[
        ("{F} ¿Cuál es la capital de la región de Tarapacá?", "Iquique", "La ficha lo indica."),
        ("{F} ¿Cuál es la capital de la región de Magallanes y de la Antártica Chilena?", "Punta Arenas", "La ficha lo indica."),
        ("{F} ¿En qué año se creó la región de Ñuble?", "2018", "La ficha lo dice."),
        ("=", "{F} ¿Cuántas regiones hay entre la región 3 y la región 8, contando solo las que están entre ambas?", "8-3-1", "Se restan los números y se descuenta la región de partida.", " regiones"),
        ("{F} ¿Qué regiones forman el Norte Chico?", "Atacama y Coquimbo", "La ficha lo indica."),
        ("{F} ¿A qué zona pertenece la región de Maule?", "a la Zona Central", "Está entre las regiones 6 a 10."),
        ("{F} ¿Cuál es la región más al sur de la lista?", "Magallanes y de la Antártica Chilena", "Es la región 16."),
        ("{F} Clasifica por zona: a) Antofagasta; b) Valparaíso; c) Los Ríos; d) Aysén.", "a: Norte Grande; b: Zona Central; c: Zona Sur; d: Zona Austral", "La ficha asigna cada región a una zona."),
        ("{F} ¿Cuál es la capital regional del Biobío?", "Concepción", "La ficha lo indica."),
        ("{F} Un compañero dice: «La capital de La Araucanía es Valdivia». Corrígelo.", "no: la capital de La Araucanía es Temuco; Valdivia es la capital de Los Ríos", "La ficha lo indica."),
        ("{F} Una alumna dice: «Chile tiene 15 regiones». ¿Qué error comete?", "tiene 16 regiones; se olvidó de alguna, como Ñuble", "La lista tiene 16 regiones."),
        ("{F} ¿Qué región está entre La Araucanía y Los Lagos?", "Los Ríos", "Son las regiones 12, 13 y 14."),
        ("{F} ¿Cuántas regiones forman la Zona Sur?", "cuatro", "Son Biobío, La Araucanía, Los Ríos y Los Lagos."),
    ],
    ctx=("Una familia viaja de Copiapó a Rancagua. ¿Por qué zonas pasa, según la ficha, desde la zona de origen hasta la de destino?", "del Norte Chico (Atacama) a la Zona Central (O'Higgins), pasando por Coquimbo y Valparaíso", "La ruta sigue el orden de las regiones."),
    sc=[("¿Qué es una capital regional?", "la ciudad donde funciona el gobierno de una región", "Es la definición de la clase."),
        ("{F} ¿Cuántas regiones tiene Chile?", "16", "La ficha las numera."),
        ("¿Qué es una zona geográfica?", "un grupo de regiones con rasgos parecidos", "Es la definición de la clase.")],
    op=("Dibuja un mapa simple de Chile en vertical, con el norte arriba. Divide el mapa en cinco franjas (las zonas) y escribe el nombre de cada zona. En cada franja escribe las regiones y sus capitales de la ficha (al menos una región por zona). {F}",
        "Cinco franjas de norte a sur: Norte Grande, Norte Chico, Zona Central, Zona Sur y Zona Austral. En cada una, al menos una región con su capital.",
        ["cinco franjas en orden", "al menos una región por zona", "capitales correctas"], ["mapa dividido en zonas"], ["poner la Zona Austral al norte", "mezclar capitales"],
        "Pide que recite las capitales de una zona."),
    reinforce="Recita en voz alta las 16 regiones de norte a sur.",
    extend="Escribe una pregunta sobre cómo se eligió la capital regional de alguna región.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 48 (fuentes geográficas, hechas para este cuaderno con datos redondeados de práctica, no oficiales). "
     "Gráfico A, lluvia al año en cuatro ciudades: Antofagasta, 5 milímetros; Santiago, 300 milímetros; Valdivia, 1.900 milímetros; Punta Arenas, 400 milímetros. "
     "Mapa B, mapa de regiones: muestra los límites y los nombres, pero no el relieve. "
     "Texto C, resumen de una región: «Es una región de clima seco, con minas de cobre y poca población; vive cerca del mar». "
     "Tabla D, población de práctica por zona: Norte Grande, 1.000.000 de personas; Zona Central, 10.000.000; Zona Sur, 3.000.000.")
build(
    OA11, 2, F,
    use="Aprenderé a leer gráficos, mapas, textos y tablas como fuentes para caracterizar una región. Sirve para extraer datos y reconocer sus límites.",
    prior=["Sé qué es una región y sus zonas.", "Sé leer una tabla simple.", "Sé que una fuente tiene un propósito."],
    explain=[
        "Para caracterizar una región se usan diferentes fuentes geográficas. Un gráfico de barras muestra datos numéricos, como la lluvia que cae al año. Un mapa muestra la ubicación y los límites. Un texto describe rasgos con palabras. Una tabla ordena datos en filas y columnas, por ejemplo la población.",
        "Cada fuente aporta algo distinto y tiene límites. El gráfico de lluvia permite comparar climas, pero no dice qué actividades hay. El mapa de regiones muestra límites, pero no el relieve. El texto resume rasgos, pero no entrega cifras. La tabla de población compara zonas, pero no explica por qué.",
        "Por eso conviene combinar fuentes. Los datos de esta ficha son redondeados y de práctica; en una investigación real se deben buscar fuentes oficiales y actuales. Siempre hay que preguntar quién hizo la fuente, cuándo y para qué, y no mezclar datos de años distintos sin avisar.",
    ],
    vocab=[("gráfico de barras", "dibujo con barras cuya altura muestra una cantidad"), ("milímetro de lluvia", "medida de cuánta lluvia cae en un lugar"), ("fuente oficial", "dato publicado por una institución del Estado"), ("redondeado", "aproximado a un número simple"), ("población", "cantidad de personas que viven en un lugar")],
    worked=[
        ("Leer un gráfico", "{F} ¿Qué ciudad del gráfico A recibe más lluvia al año?", ["Comparo las cuatro cantidades.", "Valdivia tiene 1.900 milímetros, la mayor."], "Valdivia"),
        ("Reconocer un límite", "{F} ¿Qué no muestra el mapa B?", ["Muestra límites y nombres.", "No muestra el relieve."], "El relieve"),
    ],
    mistakes=[("Creer que los datos de práctica son oficiales.", "Se olvida su carácter de práctica.", "La ficha dice que son redondeados y no oficiales."),
              ("Usar un gráfico de lluvia para saber la población.", "Se elige una fuente que no responde la pregunta.", "Para población se usa la tabla D.")],
    T=[
        ("{F} ¿Cuántos milímetros de lluvia al año tiene Santiago en el gráfico A?", "300", "El gráfico lo indica."),
        ("{F} ¿Qué ciudad tiene menos lluvia en el gráfico A?", "Antofagasta", "Tiene 5 milímetros."),
        ("{F} ¿Qué zona tiene más población en la tabla D?", "la Zona Central", "Tiene 10.000.000 de personas."),
        ("=", "{F} ¿Cuántos milímetros más de lluvia cae en Valdivia que en Santiago?", "1900-300", "Se resta la cantidad menor a la mayor.", " milímetros"),
        ("=", "{F} ¿Cuántas personas más viven en la Zona Central que en la Zona Sur, según la tabla D?", "10000000-3000000", "Se resta la población menor a la mayor.", " personas"),
        ("=", "{F} ¿Cuántas personas viven en total en las tres zonas de la tabla D?", "1000000+10000000+3000000", "Se suman las tres poblaciones.", " personas"),
        ("{F} ¿Qué fuente usarías para saber qué regiones limitan con la Región Metropolitana?", "el mapa B", "Muestra límites y nombres."),
        ("{F} ¿Qué fuente describe una región con palabras?", "el texto C", "Es un resumen escrito."),
        ("{F} ¿A qué zona puede corresponder la región que describe el texto C: Norte Grande o Zona Sur?", "al Norte Grande", "Es seca, con minas y poca población."),
        ("{F} Un compañero dice: «El gráfico A prueba que Valdivia tiene más habitantes». ¿Qué error comete?", "el gráfico mide la lluvia, no los habitantes", "Una fuente no sirve para todo."),
        ("{F} Una alumna dice: «Los datos de la ficha son oficiales y actuales». Corrígela.", "son redondeados y de práctica; para una investigación real hay que buscar fuentes oficiales", "La ficha lo indica."),
        ("{F} ¿Qué dos fuentes combinarías para decir qué ciudad tiene más lluvia y qué zona tiene más población?", "el gráfico A y la tabla D", "Cada una aporta un dato distinto."),
        ("{F} ¿Qué pregunta debes hacer a cualquier fuente?", "quién la hizo, cuándo y para qué", "Permite evaluar su valor."),
    ],
    ctx=("Para un trabajo sobre el clima, un grupo tiene solo el mapa B. ¿Qué otra fuente de la ficha necesitan y por qué?", "el gráfico A, porque el mapa no muestra datos de lluvia", "El mapa B solo muestra límites y nombres."),
    sc=[("¿Qué muestra un gráfico de barras?", "cantidades, con barras de distinta altura", "Es la definición de la clase."),
        ("{F} ¿Qué ciudad tiene 400 milímetros de lluvia?", "Punta Arenas", "El gráfico lo indica."),
        ("¿Por qué conviene combinar fuentes?", "porque cada una aporta datos distintos y tiene límites", "Una sola fuente no basta.")],
    op=("Haz una ficha con las cuatro fuentes. Anota qué dato da cada una, qué pregunta responde y qué límite tiene. Después, haz un gráfico de barras con las lluvias del gráfico A. {F}",
        "A: lluvia de cuatro ciudades; responde cuánta lluvia cae; no dice población. Barras: Antofagasta pequeña, Santiago mediana, Valdivia la más alta, Punta Arenas mediana.",
        ["cuatro fuentes con dato, pregunta y límite", "gráfico de barras con alturas proporcionales"], ["ficha", "gráfico de barras"], ["barras que no corresponden", "olvidar un límite"],
        "Pide que explique qué pregunta no puede responder cada fuente."),
    reinforce="Di en voz alta qué tipo de pregunta responde cada fuente.",
    extend="Escribe qué otra fuente buscarías para saber qué actividades económicas hay en cada zona.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 49 (rasgos físicos y humanos de las zonas, hecha para este cuaderno; datos generales). "
     "Norte Grande: clima desértico, casi sin lluvia; mucho mineral en el subsuelo; vegetación escasa, con tamarugos en la pampa; el río Loa cruza el desierto; actividad principal, la minería; ciudades en la costa. "
     "Norte Chico: clima semiárido; valles que bajan de la cordillera al mar (Elqui, Limarí); agricultura de riego y minería; observatorios astronómicos por el cielo despejado. "
     "Zona Central: clima templado, de veranos secos e inviernos lluviosos; ríos como el Aconcagua, el Maipo y el Maule; valles fértiles con agricultura; la mayor parte de la población del país; industria y servicios. "
     "Zona Sur: clima lluvioso y templado frío; ríos y lagos; bosques; agricultura, ganadería y actividad forestal; turismo. "
     "Zona Austral: clima frío y ventoso; fiordos y glaciares; poca población; ganadería ovina, pesca, hidrocarburos y turismo.")
build(
    OA11, 3, F,
    use="Aprenderé a relacionar los rasgos físicos (clima, relieve, ríos, vegetación) con los humanos (población y actividades) de cada zona. Sirve para explicar por qué cada zona tiene su actividad principal.",
    prior=["Sé ubicar las cinco zonas.", "Sé qué es una causa y una consecuencia.", "Sé leer datos de climas."],
    explain=[
        "Los rasgos físicos de un lugar influyen en lo que las personas hacen allí. Los rasgos físicos son el clima, el relieve, los ríos y la vegetación. Los rasgos humanos son la cantidad y distribución de la población y las actividades económicas. Se relacionan: lo físico ofrece condiciones, y las personas las aprovechan o las enfrentan.",
        "Por ejemplo, el Norte Grande es un desierto con mucho mineral, por eso la minería es su actividad principal. En el Norte Chico, los valles de los ríos permiten la agricultura de riego, y el cielo despejado favorece los observatorios. En la Zona Central, el clima templado y los valles fértiles permiten agricultura, y allí vive la mayor parte de la población.",
        "En la Zona Sur, la lluvia y los ríos favorecen los bosques, la ganadería y el turismo. En la Zona Austral, el frío y las grandes distancias limitan a la población, pero hay pesca, ganadería ovina e hidrocarburos. Explicar estas relaciones es una forma de razonar con causas y consecuencias: el rasgo físico explica la actividad, y la actividad atrae población.",
    ],
    vocab=[("rasgo físico", "característica natural de un lugar, como el clima o el relieve"), ("rasgo humano", "característica de la población y de sus actividades"), ("riego", "agua llevada a los cultivos"), ("hidrocarburo", "recurso como el petróleo o el gas natural"), ("distribución de la población", "forma en que las personas se reparten en un territorio")],
    worked=[
        ("Relacionar clima y actividad", "{F} ¿Por qué la minería es la actividad principal del Norte Grande?", ["El Norte Grande es desierto, con mucho mineral en el subsuelo.", "Las condiciones favorecen la minería."], "Porque es un desierto con mucho mineral en el subsuelo"),
        ("Relacionar relieve y agricultura", "{F} ¿Por qué hay agricultura de riego en el Norte Chico?", ["Hay valles que bajan de la cordillera.", "Los ríos permiten regar."], "Porque los valles de los ríos permiten regar los cultivos"),
    ],
    mistakes=[("Pensar que las actividades no dependen de los rasgos físicos.", "Se separa lo físico de lo humano.", "El clima, el relieve y el agua influyen en lo que las personas hacen."),
              ("Creer que la población se reparte por igual.", "Se olvida la concentración.", "La Zona Central concentra la mayor parte de la población.")],
    T=[
        ("{F} ¿Qué clima tiene el Norte Grande?", "desértico", "La ficha lo dice."),
        ("{F} ¿Qué árbol crece en la pampa del Norte Grande?", "el tamarugo", "La ficha lo nombra."),
        ("{F} ¿Qué ríos se mencionan para la Zona Central?", "el Aconcagua, el Maipo y el Maule", "La ficha los nombra."),
        ("{F} Clasifica como rasgo físico (F) o humano (H): a) clima templado; b) minería; c) río Loa; d) mayor población del país.", "a: F; b: H; c: F; d: H", "El clima y el río son naturales; la minería y la población son humanas."),
        ("{F} ¿Qué actividad se asocia al cielo despejado del Norte Chico?", "los observatorios astronómicos", "La ficha lo indica."),
        ("{F} ¿Qué actividades se mencionan para la Zona Sur?", "agricultura, ganadería, actividad forestal y turismo", "La ficha las enumera."),
        ("{F} ¿Por qué la Zona Central tiene mucha población?", "porque su clima templado y sus valles fértiles permiten agricultura, industria y servicios", "Las condiciones atraen a las personas."),
        ("{F} ¿Qué recursos se mencionan en la Zona Austral?", "pesca, ganadería ovina e hidrocarburos", "La ficha los enumera."),
        ("{F} Une cada zona con su rasgo principal: Norte Grande, Zona Central, Zona Sur, Zona Austral.", "Norte Grande: desierto; Zona Central: valles fértiles y población; Zona Sur: lluvia y bosques; Zona Austral: frío y fiordos", "La ficha describe cada zona."),
        ("{F} Un compañero dice: «En el Norte Grande llueve mucho». Corrígelo.", "no: es un desierto con casi nada de lluvia", "La ficha lo indica."),
        ("{F} Una alumna dice: «La Zona Austral es la más poblada». ¿Qué error comete?", "la Zona Central es la más poblada; la Austral tiene poca población", "La ficha lo indica."),
        ("{F} ¿Qué causa física explica la actividad forestal del Sur?", "la lluvia y el clima templado frío que favorecen los bosques", "La ficha lo relaciona con bosques y lluvia."),
        ("{F} Elige la mejor explicación. A) La actividad principal depende de las condiciones físicas y de lo que las personas aprovechan. B) Las actividades no dependen de nada.", "A", "La ficha muestra la relación."),
    ],
    ctx=("Una empresa quiere instalar un observatorio astronómico. ¿En qué zona de la ficha conviene y por qué?", "en el Norte Chico, por su cielo despejado", "La ficha lo relaciona con el clima."),
    sc=[("¿Qué es un rasgo físico?", "una característica natural de un lugar, como el clima", "Es la definición de la clase."),
        ("{F} ¿Qué es el riego?", "agua llevada a los cultivos", "Es la definición de la clase."),
        ("¿Por qué lo físico y lo humano se relacionan?", "porque las personas aprovechan o enfrentan las condiciones del lugar", "Lo físico ofrece condiciones.")],
    op=("Dibuja una tabla con tres filas (clima, ríos o relieve, actividad principal) y cinco columnas (las cinco zonas). Completa con datos de la ficha. Debajo, escribe dos oraciones que expliquen la relación entre un rasgo físico y una actividad. {F}",
        "Norte Grande: desértico; río Loa; minería. Zona Central: templado; ríos Maipo y Maule; agricultura y población. Oración: como es desierto con minerales, hay minería.",
        ["cinco columnas completas", "datos de la ficha", "dos oraciones de relación"], ["tabla de zonas", "dos oraciones"], ["poner minería en la Zona Sur", "no relacionar lo físico con lo humano"],
        "Pide que explique con un ejemplo por qué las personas viven donde viven."),
    reinforce="Di en voz alta un rasgo físico y una actividad de cada zona.",
    extend="Escribe una pregunta sobre cómo cambia el clima desde el norte hasta el sur.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 50 (comparación de regiones, hecha para este cuaderno; datos generales). "
     "Región de Antofagasta: desierto; relieve de pampas y salares con la cordillera de los Andes al este; minería del cobre; ciudades en la costa y en el interior; poca vegetación. "
     "Región Metropolitana de Santiago: clima templado de verano seco; relieve de gran cuenca rodeada de cerros; río Maipo; mayor población del país (cerca de 4 de cada 10 personas); industria, comercio y servicios. "
     "Región de Los Lagos: lluvias abundantes; relieve con volcanes y la cordillera de los Andes al este; lagos y bosques; agricultura, ganadería, pesca y salmonicultura; turismo. "
     "Región de Magallanes y de la Antártica Chilena: clima frío y ventoso; relieve de fiordos y canales; estepa; poca población; ganadería ovina, hidrocarburos y turismo.")
build(
    OA11, 4, F,
    use="Aprenderé a comparar cuatro regiones de Chile según su clima, su población y sus actividades. Sirve para ver diferencias y semejanzas y para dar razones.",
    prior=["Sé relacionar rasgos físicos y humanos.", "Sé comparar con criterios.", "Sé ubicar las regiones en las zonas."],
    explain=[
        "Comparar regiones es ver qué tienen en común y en qué se diferencian. Podemos usar criterios como el clima, la vegetación, el relieve, la hidrografía, la población y las actividades económicas. Con la ficha comparamos cuatro regiones: Antofagasta, Metropolitana, Los Lagos y Magallanes.",
        "Antofagasta es desértica y vive de la minería. La Región Metropolitana tiene clima templado y concentra a cerca de 4 de cada 10 personas, con industria, comercio y servicios. Los Lagos es lluviosa, con lagos y bosques, y vive de la agricultura, la ganadería, la pesca y el turismo. Magallanes es fría y ventosa, con poca población y recursos como las ovejas y los hidrocarburos.",
        "Una semejanza es que las cuatro regiones tienen actividades económicas ligadas a su entorno. Una diferencia es el clima: del desierto al frío extremo. Comparar nos ayuda a entender que Chile es diverso y que cada región tiene necesidades y fortalezas propias. Siempre hay que apoyar las comparaciones con datos de la ficha.",
    ],
    vocab=[("estepa", "terreno llano con pasto bajo y pocos árboles"), ("fiordo", "entrada larga y angosta del mar entre montañas"), ("salmonicultura", "cultivo de salmones en el mar o en lagos"), ("criterio", "aspecto que se usa para comparar"), ("fortaleza", "ventaja que tiene un lugar")],
    worked=[
        ("Comparar el clima", "{F} Compara el clima de Antofagasta y de Los Lagos.", ["Antofagasta es desierto, casi sin lluvia.", "Los Lagos tiene lluvias abundantes."], "Antofagasta es seca y Los Lagos es lluviosa"),
        ("Encontrar una semejanza", "{F} ¿Qué tienen en común Los Lagos y Magallanes?", ["Busco una actividad que se repita.", "Ambas tienen ganadería y turismo."], "Ganadería y turismo"),
    ],
    mistakes=[("Decir que todas las regiones tienen la misma población.", "Se olvida la concentración.", "La Región Metropolitana concentra cerca de 4 de cada 10 personas."),
              ("Comparar sin criterio.", "Se mezclan clima y población.", "Hay que elegir un criterio y compararlo en las regiones.")],
    T=[
        ("{F} ¿Qué actividad principal tiene la región de Antofagasta?", "la minería del cobre", "La ficha lo indica."),
        ("{F} ¿Qué región tiene cerca de 4 de cada 10 personas del país?", "la Región Metropolitana", "La ficha lo dice."),
        ("{F} ¿Qué actividad acuática se menciona en Los Lagos?", "la salmonicultura", "La ficha la nombra."),
        ("{F} ¿Qué recurso se menciona en Magallanes además de las ovejas?", "los hidrocarburos", "La ficha lo dice."),
        ("{F} ¿Cuál de las cuatro regiones tiene lluvias abundantes?", "Los Lagos", "La ficha lo dice."),
        ("{F} ¿Cuál de las cuatro regiones es desértica?", "Antofagasta", "La ficha lo dice."),
        ("=", "{F} Si en un grupo de 10 personas del país 4 viven en la Región Metropolitana, ¿cuántas personas de un grupo de 50 vivirían allí (usa la misma proporción)?", "50*4//10", "Se calcula 4 de cada 10 para 50 personas.", " personas"),
        ("{F} Ordena las regiones de la ficha de norte a sur: Magallanes, Antofagasta, Los Lagos, Metropolitana.", "Antofagasta, Metropolitana, Los Lagos, Magallanes", "Siguen el orden de la ficha de regiones."),
        ("{F} Compara el relieve de Los Lagos y de Magallanes: ¿qué rasgo menciona la ficha para cada una?", "Los Lagos: volcanes; Magallanes: fiordos y canales", "La ficha describe el relieve de cada región."),
        ("{F} Un compañero dice: «Antofagasta y Los Lagos tienen el mismo clima». Corrígelo.", "no: Antofagasta es desértica y Los Lagos es lluviosa", "La ficha lo muestra."),
        ("{F} Una alumna dice: «Magallanes tiene mucha población». ¿Qué error comete?", "tiene poca población", "La ficha lo indica."),
        ("{F} ¿Qué tipo de recurso aprovechan Antofagasta (cobre) y Magallanes (hidrocarburos)?", "recursos del subsuelo", "El cobre y los hidrocarburos se extraen del subsuelo."),
        ("{F} Elige la mejor frase comparativa. A) Mientras Antofagasta es desértica, Los Lagos es lluviosa. B) Todas las regiones son iguales.", "A", "A contrasta un criterio con datos."),
    ],
    ctx=("Una familia piensa mudarse de la Región Metropolitana a Magallanes. Escribe una diferencia que notarían en el clima y otra en la población, según la ficha.", "el clima es frío y ventoso y la población es mucho menor", "La ficha describe ambos contrastes."),
    sc=[("¿Qué es la salmonicultura?", "el cultivo de salmones", "Es la definición de la clase."),
        ("{F} ¿Qué región tiene lagos y volcanes?", "Los Lagos", "La ficha lo indica."),
        ("¿Por qué es útil comparar regiones?", "porque muestra la diversidad de Chile y las necesidades de cada región", "Cada una es distinta.")],
    op=("Elige dos de las cuatro regiones y haz una tabla con filas de clima, hidrografía, vegetación, población y actividades. Completa con la ficha. Escribe una semejanza y una diferencia. {F}",
        "Antofagasta y Los Lagos: clima seco / lluvioso; vegetación escasa / bosques; minería / agricultura y turismo. Semejanza: ambas aprovechan sus recursos naturales.",
        ["tabla de cinco filas", "datos de la ficha", "semejanza y diferencia"], ["tabla comparativa", "dos oraciones"], ["inventar datos", "no escribir ninguna semejanza"],
        "Pide que explique qué fila le mostró la mayor diferencia."),
    reinforce="Di en voz alta una característica de cada región de la ficha.",
    extend="Escribe una pregunta sobre qué ventajas y desafíos tiene vivir en una región con poca población.",
)
