"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 19 (escasez, necesidades y circuito económico) y OA 20 (oferta, demanda y alteraciones del mercado)."""
from __future__ import annotations

from hi5_lib import build

MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ================================================================ OA 19
OA = "HI1M OA 19"

# ---------------------------------------------------------------- Clase 1
F1 = "Caso de ejemplo: Camila, de 15 años, dispone de $12.000 este mes. Opciones y precios: audífonos $9.000; entrada al cine $5.000; pasaje mensual de bus al entrenamiento $4.000; cuaderno $3.000."
build(
    OA, 1, F1,
    use="Aprenderé a plantear el problema económico: por qué todas las personas y los países deben elegir. Sirve para entender decisiones de consumo, de producción y de política pública.",
    prior=["Sé sumar y restar cantidades de dinero.", "Sé que las personas tienen necesidades y deseos distintos.", "Sé leer datos en un pequeño texto o tabla."],
    explain=[
        "El problema económico nace de una diferencia: las necesidades y los deseos de las personas son muy numerosos y siempre aparecen otros nuevos, pero los recursos para satisfacerlos (dinero, tiempo, trabajo, materias primas) son limitados. Esa falta de recursos frente a lo que se quiere se llama escasez. La escasez no es lo mismo que pobreza: también una persona con mucho dinero o un Estado grande debe elegir qué hacer primero.",
        "Las necesidades básicas son las que se requieren para vivir con dignidad, como alimento, abrigo, vivienda y salud. Los deseos son aquello que se quiere pero se puede postergar, como un videojuego nuevo. Para satisfacer necesidades y deseos se usan bienes, que son objetos (un cuaderno, un pan) y servicios, que son actividades que alguien realiza para otro (una función de cine, una atención de salud).",
        "Como no alcanza para todo, hay que elegir, y toda elección implica renunciar a algo. El costo de oportunidad es lo más valioso a lo que se renuncia al elegir una alternativa. Por ejemplo, si una familia usa su dinero extra en un viaje, el costo de oportunidad puede ser arreglar el techo. Elegir bien exige ordenar las necesidades por prioridad y comparar lo que se gana con lo que se pierde.",
    ],
    vocab=[("escasez", "falta de recursos suficientes para satisfacer todas las necesidades y deseos"), ("necesidad básica", "lo que se requiere para vivir con dignidad, como alimento, abrigo y salud"), ("bien", "objeto que satisface una necesidad o un deseo"), ("servicio", "actividad que una persona realiza para otra y satisface una necesidad"), ("costo de oportunidad", "lo más valioso a lo que se renuncia al elegir una alternativa")],
    worked=[
        ("Ver si el dinero alcanza", "Tomás (de ejemplo) tiene $8.000 y quiere zapatillas usadas de $7.000 y un libro de $3.000. ¿Le alcanza para ambos? ¿Cuánto le falta?",
         ["Sumo lo que quiere comprar: 7.000 + 3.000 = 10.000.", "Comparo con lo que tiene: 10.000 - 8.000 = 2.000."], "No le alcanza; le faltan $2.000, lo que muestra escasez"),
        ("Hallar el costo de oportunidad", "Un agricultor (de ejemplo) puede usar su terreno para sembrar papas o maíz. Prefiere papas y su segunda mejor opción era el maíz. ¿Cuál es el costo de oportunidad de sembrar papas?",
         ["El costo de oportunidad es lo más valioso a lo que se renuncia.", "Al elegir papas renuncia a su siguiente mejor opción: el maíz."], "Renunciar a sembrar maíz"),
    ],
    mistakes=[
        ("Creer que escasez es lo mismo que pobreza.", "La escasez afecta a todos porque los recursos son limitados frente a necesidades que crecen, aunque cambie su intensidad.", "Pregunta si los recursos alcanzan para todo lo que se quiere; si no alcanzan, hay escasez."),
        ("Pensar que todas las necesidades y deseos tienen la misma prioridad.", "Algunas son básicas y otras se pueden postergar; tratarlas igual lleva a decidir mal.", "Ordena primero las necesidades básicas y luego los deseos."),
    ],
    T=[
        ("En Economía: ¿qué es la escasez?", "Que los recursos disponibles son limitados y no alcanzan para satisfacer todas las necesidades y deseos", "Es la idea central del problema económico."),
        ("=", "{F} ¿Cuánto cuestan en total las cuatro opciones juntas (en pesos)?", "9000+5000+4000+3000", "Se suman los precios de las cuatro opciones."),
        ("En Economía: una entrada para una función de cine, ¿es un bien o un servicio? A) un bien, B) un servicio.", "B", "El cine es una actividad prestada, no un objeto."),
        ("{F} ¿Por qué Camila enfrenta escasez? A) porque es pobre, B) porque su dinero no alcanza para todo lo que desea comprar.", "B", "La escasez aparece cuando los recursos no alcanzan, sin importar si hay pobreza."),
        ("Un empresario muy rico quiere comprar un barco, una casa en la playa y un avión, pero su dinero solo alcanza para dos. ¿Enfrenta escasez? A) No, porque es rico, B) Sí, porque su dinero no alcanza para todo lo que quiere.", "B", "Los recursos limitados afectan también a quien tiene mucho."),
        ("Clasifica cada elemento como necesidad básica (NB) o deseo (D): a) alimento, b) videojuego nuevo, c) abrigo en invierno. Responde con las tres letras.", "a) NB, b) D, c) NB", "Alimento y abrigo son necesarios para vivir; el videojuego se puede postergar."),
        ("=", "{F} Si Camila compra los audífonos, ¿cuánto dinero le queda (en pesos)?", "12000-9000", "Se resta el precio de los audífonos a su dinero."),
        ("=", "{F} Si Camila compra el pasaje y la entrada al cine, ¿cuánto dinero le sobra (en pesos)?", "12000-(4000+5000)", "Se resta la suma de ambas compras al dinero total."),
        ("{F} Camila compra los audífonos y su segunda mejor opción era la entrada al cine. ¿Cuál es su costo de oportunidad?", "Renunciar a la entrada al cine", "Es lo más valioso a lo que renunció al elegir."),
        ("Un compañero dice: «Si tuviera más dinero, la escasez desaparecería para siempre». ¿Qué respuesta es la correcta? A) Tiene razón, con suficiente dinero se tiene todo, B) No, porque las necesidades y deseos siguen creciendo y los recursos siguen siendo limitados, C) Tiene razón, porque la escasez solo afecta a quienes ganan poco.", "B", "Con más dinero aparecen nuevos deseos y los recursos siguen siendo finitos."),
        ("{F} Camila decide pagar primero el pasaje, que necesita para entrenar. Con el dinero que le queda, ¿qué dos opciones juntas puede comprar sin pasarse?", "La entrada al cine y el cuaderno", "Le quedan $8.000 y solo 5.000 + 3.000 suman exactamente 8.000."),
        ("=", "{F} ¿Cuánto dinero le falta a Camila para comprar las cuatro opciones (en pesos)?", "9000+5000+4000+3000-12000", "Se resta su dinero al total de las cuatro opciones."),
        ("=", "Un colegio (de ejemplo) tiene $2.000.000 para el año y tres proyectos: techar el patio ($1.500.000), renovar computadores ($1.200.000) y ampliar la biblioteca ($800.000). Si el colegio quisiera hacer los tres proyectos, ¿cuántos pesos le faltarían?", "1500000+1200000+800000-2000000", "Se suman los tres proyectos y se resta el dinero disponible."),
    ],
    ctx=("Una municipalidad (de ejemplo) tiene dinero para pavimentar una calle o para ampliar una sala cuna, pero no para ambas cosas. Decide pavimentar. ¿Cuál es su costo de oportunidad? A) la calle pavimentada, B) la ampliación de la sala cuna.", "B", "Es la alternativa a la que renuncia al elegir."),
    sc=[("En Economía: ¿qué diferencia hay entre una necesidad básica y un deseo?", "La necesidad básica se requiere para vivir con dignidad; el deseo se puede postergar", "Esa es la diferencia que ordena las prioridades."),
        ("¿Qué es el costo de oportunidad?", "Lo más valioso a lo que se renuncia al elegir una alternativa", "Mide lo que se pierde al decidir."),
        ("¿Es correcto decir que solo las personas pobres enfrentan escasez?", "No, porque todos tienen recursos limitados frente a necesidades que crecen", "La escasez afecta a personas, familias y Estados.")],
    op=("Gabriel (de ejemplo) tiene $10.000 este mes. Opciones: zapatillas usadas $8.000; entrada a un recital $6.000; tarjeta de transporte $4.000; libro $5.000. Escribe: cuánto suman las cuatro opciones, qué conjunto de ellas elegirías sin pasarte de $10.000, cuál sería tu costo de oportunidad y una frase que explique por qué esto es escasez y no pobreza.",
        "Las cuatro suman $23.000. Elijo la tarjeta de transporte y el libro ($9.000). Mi costo de oportunidad es el recital, mi opción siguiente. Es escasez porque el dinero no alcanza para todo lo que quiere, aunque tenga dinero.",
        ["suma correctamente las cuatro opciones", "elige un conjunto que no pase de $10.000", "nombra el costo de oportunidad", "explica escasez sin confundirla con pobreza"], ["una respuesta de cuatro partes con cálculos"], ["elegir opciones que suman más de $10.000", "decir que hay escasez porque Gabriel es pobre"], "Muéstrale tu conjunto a una persona de tu casa y pídele que compruebe la suma."),
    reinforce="Anota tres cosas que quieres comprar este mes y marca cuál es necesidad básica y cuál es deseo.",
    extend="Escribe un ejemplo de escasez que enfrente un país y nombra el costo de oportunidad de una decisión que tome.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Fuente A (de ejemplo, liquidación de sueldo de un mes): la empresa Mar Azul paga a una trabajadora un sueldo bruto de $500.000; los descuentos legales (salud, previsión e impuestos) suman $100.000; sueldo líquido, $400.000. "
      "Fuente B (de ejemplo, informe trimestral de un instituto de estadísticas): exportaciones del trimestre, US$ 24.000 millones; importaciones del trimestre, US$ 21.000 millones. "
      "Fuente C (de ejemplo, columna de opinión): «Es injusto que el Estado cobre impuestos a las empresas; ya hacen bastante al dar empleo.»")
build(
    OA, 2, F2,
    use="Aprenderé a leer fuentes económicas y a distinguir qué flujo del circuito económico muestra cada una y quién la escribió. Sirve para no confundir un dato con una opinión.",
    prior=["Sé que hay escasez y que se debe elegir.", "Sé qué son un bien y un servicio.", "Sé distinguir un dato de una opinión."],
    explain=[
        "El circuito económico es un modelo que muestra cómo circulan bienes, servicios y dinero entre los agentes económicos: las familias, las empresas, el Estado y el resto del mundo. Las familias entregan su trabajo a las empresas y reciben remuneraciones, es decir, sueldos y salarios; con ese dinero compran bienes y servicios. Las empresas producen y venden, y pagan impuestos al Estado, que a su vez entrega servicios como educación y salud.",
        "El resto del mundo participa mediante el comercio exterior: las exportaciones son bienes y servicios que un país vende a otros, y las importaciones son los que compra a otros. La diferencia entre ambas se llama balanza comercial. Estos flujos dejan huellas en fuentes escritas: una liquidación de sueldo muestra una remuneración, un informe estadístico muestra exportaciones e importaciones, y una columna de opinión muestra un punto de vista.",
        "Para seleccionar una fuente pregunto quién la produjo, cuándo, con qué propósito y qué flujo me permite comprobar. Una fuente estadística entrega datos que se pueden contar; una columna de opinión entrega una postura que hay que contrastar con datos. Ninguna fuente por sí sola explica todo el circuito, por eso conviene usar al menos dos de distinto tipo.",
    ],
    vocab=[("circuito económico", "modelo que muestra cómo circulan bienes, servicios y dinero entre los agentes"), ("remuneración", "pago que recibe quien trabaja, como un sueldo o un salario"), ("impuesto", "pago obligatorio que personas y empresas entregan al Estado"), ("exportación", "bien o servicio que un país vende a otro"), ("importación", "bien o servicio que un país compra a otro")],
    worked=[
        ("Ubicar un flujo en una fuente", "Una liquidación de ejemplo dice: sueldo bruto $700.000, descuentos $120.000. ¿Qué flujo del circuito muestra y entre qué agentes?",
         ["Un sueldo es una remuneración.", "La paga una empresa y la recibe una familia (la persona trabajadora)."], "El pago de una remuneración, de una empresa a una familia"),
        ("Distinguir dato y opinión", "Dos frases de ejemplo: (1) «Las importaciones del trimestre fueron US$ 9.000 millones». (2) «Importamos demasiado». ¿Cuál es un dato verificable?",
         ["Un dato se puede comprobar con una cifra y una fuente.", "La frase (1) entrega una cifra; la (2) expresa un juicio."], "La frase (1)"),
    ],
    mistakes=[
        ("Usar una columna de opinión como si fuera un dato.", "La opinión expresa un punto de vista y puede no tener cifras que la respalden.", "Busca el dato que la apoye o la contradiga antes de usarla."),
        ("Confundir exportaciones con importaciones.", "Exportar es vender al exterior; importar es comprar al exterior.", "Pregunta si el dinero del país entra (se vende afuera) o sale (se compra afuera)."),
    ],
    T=[
        ("En Economía: ¿qué es una remuneración?", "El pago que recibe una persona por su trabajo, como un sueldo o un salario", "Se le paga al trabajador por su trabajo."),
        ("{F} En la fuente A, ¿qué agente paga el sueldo bruto?", "La empresa Mar Azul", "El texto dice que la empresa paga a la trabajadora."),
        ("En Economía: ¿qué es una exportación? A) un bien que un país vende a otro, B) un bien que un país compra a otro.", "A", "Exportar es vender hacia el exterior."),
        ("{F} ¿Cuál de las tres fuentes expresa una opinión y no un dato? A) la fuente A, B) la fuente B, C) la fuente C.", "C", "Afirma que algo es injusto, sin cifras ni medición."),
        ("{F} ¿Qué flujo del circuito económico permite comprobar la fuente B? A) el pago de remuneraciones, B) el comercio con el resto del mundo, C) el cobro de impuestos a las familias.", "B", "Informa exportaciones e importaciones."),
        ("Una persona usa la fuente C para afirmar que «las empresas ya pagan demasiados impuestos». ¿Qué le falta a su argumento? A) un dato sobre el pago de impuestos, B) más adjetivos.", "A", "Una opinión se respalda con datos que se puedan verificar."),
        ("=", "{F} En la fuente A, ¿qué porcentaje del sueldo bruto representan los descuentos legales?", "100000*100//500000", "Se divide el descuento por el sueldo bruto y se multiplica por 100.", "%"),
        ("=", "{F} En la fuente B, ¿cuánto mayor fueron las exportaciones que las importaciones, en millones de dólares?", "24000-21000", "Se restan las importaciones a las exportaciones."),
        ("{F} La fuente B informa más exportaciones que importaciones. ¿Qué nombre recibe esa diferencia y es a favor o en contra del país? Responde con una frase.", "Se llama balanza comercial y en este caso es favorable porque se vendió más de lo que se compró", "La balanza comercial compara exportaciones e importaciones."),
        ("{F} ¿Qué fuente usarías para saber cuánto recibe en mano una trabajadora cada mes, y por qué? Responde con una frase.", "La fuente A, porque muestra el sueldo líquido de $400.000", "La liquidación entrega el sueldo líquido."),
        ("Para un informe sobre cómo el comercio exterior afecta a un país, una estudiante elige solo una columna de opinión. ¿Es una selección adecuada? Responde con una frase.", "No, porque una opinión no entrega datos de exportaciones e importaciones; conviene sumar una fuente estadística", "Se necesitan fuentes que entreguen cifras."),
        ("{F} Al combinar las fuentes A y B, ¿qué agente aparece en la B y no en la A? A) el resto del mundo, B) las familias.", "A", "La A muestra empresa y trabajadora; la B, el comercio con otros países."),
        ("=", "{F} Si el sueldo líquido de la trabajadora fuera un cuarto menor porque se aumentaran los descuentos, ¿cuál sería su nuevo sueldo líquido (en pesos)?", "400000-400000//4", "Un cuarto de 400.000 es 100.000, que se resta del sueldo líquido."),
    ],
    ctx=("Para una feria escolar sobre economía, un curso debe elegir la mejor fuente para mostrar cuánto vendió un país al exterior en un año. Opciones: A) una columna de opinión sobre el comercio, B) un informe estadístico con exportaciones. ¿Cuál elige?", "B", "El informe entrega cifras de lo que se vendió al exterior."),
    sc=[("En Economía: ¿quiénes son los cuatro agentes del circuito económico?", "Las familias, las empresas, el Estado y el resto del mundo", "Son los agentes que enumera la clase."),
        ("¿Qué es un impuesto?", "Un pago obligatorio que personas y empresas entregan al Estado", "El Estado lo usa para financiar servicios."),
        ("¿Qué diferencia hay entre un dato y una opinión?", "El dato se puede comprobar con cifras; la opinión expresa un punto de vista", "Por eso conviene respaldar las opiniones con datos.")],
    op=("{F} Elige dos fuentes y completa para cada una: tipo (dato u opinión), flujo del circuito que muestra y agentes que participan. Termina con una frase que explique qué ganas al usar ambas juntas.",
        "Fuente A: dato; muestra el pago de remuneraciones; participan una empresa y una familia. Fuente B: dato; muestra el comercio exterior; participa el resto del mundo. Juntas muestran dos flujos distintos del circuito.",
        ["clasifica cada fuente", "nombra el flujo y los agentes", "justifica el uso conjunto"], ["dos fuentes analizadas y una conclusión"], ["tratar la fuente C como si fuera un dato", "no nombrar los agentes del flujo"], "Pide a una persona de tu casa que lea tu conclusión y diga si distingue bien dato y opinión."),
    reinforce="Mira una boleta de tu casa y anota qué producto o servicio muestra y quién la emitió.",
    extend="Escribe una pregunta que la fuente B no responde y qué otra fuente necesitarías para contestarla.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Tabla de ejemplo, localidad ficticia «Pueblo Seco», antes y después de abrirse una mina: "
      "empleos locales, 200 antes y 600 después; comercios del pueblo, 15 antes y 40 después; bienes comprados a otras regiones, 30 camiones al mes antes y 90 camiones al mes después; "
      "servicios del Estado (escuela, consultorio), 1 escuela y 1 consultorio antes y 1 escuela y 1 consultorio después; "
      "exportaciones de cobre que salen del puerto más cercano, ninguna antes y 12.000 toneladas al año después.")
build(
    OA, 3, F3,
    use="Aprenderé a describir qué cambia y qué se mantiene en el circuito económico de un territorio cuando aparece una nueva actividad. Sirve para entender por qué las regiones tienen economías distintas.",
    prior=["Conozco los cuatro agentes del circuito económico.", "Sé qué son remuneración, impuesto, exportación e importación.", "Sé comparar los datos de una tabla de antes y después."],
    explain=[
        "El circuito económico no es igual en todos los lugares ni en todos los tiempos. Cuando se instala una nueva actividad en un territorio, como una mina, un puerto o una planta de fruta, aumentan los empleos y las remuneraciones, y las familias gastan más en comercio y servicios. Eso es un cambio. Pero otras cosas pueden continuar igual, como la cantidad de servicios públicos si el Estado no amplía sus instalaciones.",
        "El territorio importa porque no todas las regiones tienen los mismos recursos. Una región minera depende de la minería, una región agrícola de la cosecha y una portuaria del comercio. Esa especialización permite exportar, pero también hace que la economía local sea más vulnerable a una caída de los precios o al agotamiento del recurso. La dependencia de una sola actividad es un riesgo que conviene reconocer.",
        "Al comparar el antes y el después se puede calcular el aumento absoluto, que es cuánto creció una cantidad, y el aumento relativo, que es cuántas veces creció o qué porcentaje representa. Leer ambos evita sacar conclusiones exageradas: un aumento grande en números puede ser pequeño en proporción, y al revés. Siempre se debe indicar la fecha, el lugar y la fuente de los datos.",
    ],
    vocab=[("especialización", "concentración de la economía de un lugar en una actividad principal"), ("dependencia económica", "situación en que un territorio vive sobre todo de una sola actividad"), ("aumento absoluto", "cuánto creció una cantidad, calculado con una resta"), ("aumento relativo", "cuántas veces o qué porcentaje creció una cantidad"), ("vulnerable", "expuesto a sufrir un daño si cambian las condiciones")],
    worked=[
        ("Calcular un aumento absoluto", "En una localidad de ejemplo, los comercios pasaron de 20 a 50. ¿Cuál fue el aumento absoluto?",
         ["El aumento absoluto se calcula con una resta.", "50 - 20 = 30."], "30 comercios más"),
        ("Separar cambio y continuidad", "En la misma localidad, las escuelas fueron 2 antes y 2 después, y los empleos pasaron de 300 a 900. ¿Qué rasgo cambió y cuál continuó?",
         ["Los empleos cambiaron: de 300 a 900.", "Las escuelas continuaron: eran 2 y siguen siendo 2."], "Cambiaron los empleos; continuó el número de escuelas"),
    ],
    mistakes=[
        ("Decir que, si una actividad crece, todo mejora en la localidad.", "Algunos rasgos, como los servicios públicos, pueden quedar iguales y presionar a la comunidad.", "Compara cada rasgo y separa cambios de continuidades."),
        ("Pensar que una región que vive de un recurso no corre riesgos.", "Si el precio cae o el recurso se agota, toda la economía local se resiente.", "Pregunta qué pasaría con las familias si esa actividad se detuviera."),
    ],
    T=[
        ("En Economía: ¿qué es el aumento absoluto de una cantidad?", "Cuánto creció, calculado con una resta", "Se resta la cantidad final menos la inicial."),
        ("{F} ¿Cuántos empleos locales había antes de abrirse la mina?", "200", "Lo informa la tabla."),
        ("{F} ¿Qué rasgo de la tabla continuó igual? A) los empleos, B) la cantidad de escuelas y consultorios.", "B", "Antes y después había una escuela y un consultorio."),
        ("=", "{F} ¿Cuántos empleos locales se sumaron tras abrirse la mina?", "600-200", "Se resta la cifra inicial a la final."),
        ("=", "{F} ¿Cuántos comercios nuevos hubo en el pueblo?", "40-15", "Se resta la cantidad inicial a la final."),
        ("{F} ¿Cuántas veces mayor es el número de empleos después que antes? A) 2 veces, B) 3 veces.", "B", "Seiscientos dividido por doscientos es tres."),
        ("=", "{F} ¿Cuántos camiones al mes más llegan al pueblo con bienes de otras regiones?", "90-30", "Se resta la cifra inicial a la final."),
        ("=", "{F} Supón (dato de ejemplo) que cada empleo nuevo mantiene a 4 personas. ¿Cuántas personas dependen de los empleos nuevos?", "(600-200)*4", "Los empleos nuevos son 600 - 200 = 400 y 400 por 4 da 1.600."),
        ("{F} La última fila de la tabla habla de exportaciones de cobre. ¿Con qué agente del circuito conecta esa fila al pueblo? Responde con una frase.", "Con el resto del mundo, porque el cobre se vende a otros países", "Las exportaciones son ventas al exterior."),
        ("Un estudiante concluye: «Con la mina, el pueblo no tiene ningún problema». Con la tabla, ¿qué dato debilita su conclusión? A) los empleos subieron de 200 a 600, B) los servicios públicos no aumentaron.", "B", "La población puede crecer sin que el Estado amplíe escuela ni consultorio."),
        ("{F} Si el precio del cobre cayera mucho y la mina cerrara, ¿qué riesgo muestra la tabla? Responde con una frase.", "Una dependencia económica: el pueblo perdería 600 empleos y la demanda de sus comercios", "Toda la economía local depende de la mina."),
        ("Una región de ejemplo exporta solo fruta y su cosecha se pierde por una helada. ¿Qué concepto del vocabulario describe mejor el problema que enfrenta? A) dependencia económica, B) balanza comercial.", "A", "Vive de una sola actividad que falló."),
        ("=", "{F} Si el número de comercios siguiera creciendo en la misma cantidad que entre antes y después, ¿cuántos comercios habría en el siguiente período?", "40+(40-15)", "Se suma al valor actual el mismo aumento absoluto."),
    ],
    ctx=("Una alcaldesa de ejemplo debe decidir si pedir más escuelas para su comuna, donde se abrió una planta de fruta que sumó 400 empleos en tres años. Los servicios públicos son los mismos que antes. ¿Qué argumento sirve mejor? A) hay más familias en la comuna, pero igual cantidad de escuelas, B) hay más empleos, así que no hace falta nada.", "A", "Muestra una continuidad que no se ajusta al cambio."),
    sc=[("En Economía: ¿qué es una especialización económica?", "La concentración de la economía de un lugar en una actividad principal", "Define a regiones mineras, agrícolas o portuarias."),
        ("¿Qué riesgo tiene depender de una sola actividad?", "Si esa actividad cae o se agota, toda la economía local se resiente", "No hay otras fuentes de ingreso que compensen."),
        ("¿Cómo se calcula un aumento absoluto?", "Restando la cantidad inicial a la final", "Mide cuánto creció.")],
    op=("{F} Escribe un párrafo corto que diga: dos cosas que cambiaron en Pueblo Seco, una que continuó y un riesgo que corre el pueblo. Usa al menos tres cifras de la tabla.",
        "Cambiaron los empleos (de 200 a 600) y los comercios (de 15 a 40). Continuó la cantidad de escuelas y consultorios (1 y 1). El pueblo corre el riesgo de depender de una sola actividad, la minería, porque exporta 12.000 toneladas de cobre.",
        ["nombra dos cambios con cifras", "nombra una continuidad", "explica un riesgo de la dependencia"], ["un párrafo con tres cifras"], ["inventar cifras que no están en la tabla", "no mencionar ninguna continuidad"], "Lee tu párrafo a una persona de tu casa y pídele que marque las cifras que usaste."),
    reinforce="Elige una actividad de tu región y anota qué empleos y negocios crea a su alrededor.",
    extend="Explica por qué un territorio que depende de una sola actividad es más vulnerable que uno con varias.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Caso de ejemplo: el Estado decide aplicar un impuesto de 5 % a los envases plásticos desechables. Antes, una bandeja costaba $1.000 al consumidor. "
      "Voces de ejemplo: la dueña de una empresa de envases dice que sus costos subirán y que podría vender menos; una familia dice que el precio sube y que debe cuidar su presupuesto; "
      "la autoridad del Estado dice que con lo recaudado se financiarán programas de reciclaje; un importador dice que traerá envases de papel desde otro país.")
build(
    OA, 4, F4,
    use="Aprenderé a comparar cómo ven una misma decisión económica las familias, las empresas, el Estado y el resto del mundo. Sirve para evaluar medidas públicas sin quedarme con una sola mirada.",
    prior=["Sé qué son impuestos, remuneraciones, exportaciones e importaciones.", "Sé que la escasez obliga a elegir.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "Una misma decisión económica afecta de manera distinta a cada agente. Cuando el Estado crea un impuesto, recauda dinero que puede destinar a servicios, pero las empresas ven subir sus costos y las familias pueden ver subir los precios. Por eso cada agente tiene una perspectiva, un punto de vista que depende de sus intereses y de su posición en el circuito económico.",
        "También hay varias causas y varias consecuencias. Un cambio de precio puede deberse a un impuesto, a la cantidad producida o a lo que cuesta importar un insumo. Hablamos de multicausalidad cuando un hecho tiene varias causas a la vez. Hay que separar la causa, que produce un efecto, de la correlación, que es solo una coincidencia entre dos hechos que ocurren juntos sin que uno cause el otro.",
        "El resto del mundo influye porque las empresas pueden reemplazar un producto nacional por uno importado si les conviene el precio. Evaluar una medida implica preguntar quién gana, quién pierde, quién decide y con qué efectos probables. Una buena evaluación presenta las perspectivas de cada agente y evita atribuirle toda la responsabilidad a uno solo.",
    ],
    vocab=[("perspectiva", "punto de vista que depende de los intereses y de la posición de cada agente"), ("multicausalidad", "situación en que un hecho tiene varias causas a la vez"), ("recaudar", "reunir dinero mediante el cobro de impuestos"), ("correlación", "coincidencia entre dos hechos que ocurren juntos sin que uno cause el otro"), ("insumo", "material o producto que se usa para fabricar otro")],
    worked=[
        ("Calcular el efecto del impuesto", "Un impuesto de ejemplo de 10 % se aplica a un producto de $2.000. ¿Cuánto sube el precio?",
         ["El 10 % de 2.000 es 2.000 × 10 ÷ 100 = 200.", "El nuevo precio es 2.000 + 200 = 2.200."], "Sube $200 y queda en $2.200"),
        ("Asociar perspectivas", "Una autoridad (de ejemplo) dice que el impuesto financiará programas de salud. ¿Qué agente habla y qué le interesa?",
         ["Quien recauda impuestos y los destina a servicios es el Estado.", "Le interesa financiar servicios para la población."], "El Estado; le interesa financiar servicios"),
    ],
    mistakes=[
        ("Atribuirle toda la responsabilidad de una alza de precios a un solo agente.", "Los precios dependen de impuestos, costos, demanda y comercio exterior a la vez.", "Revisa varias causas antes de culpar a un agente."),
        ("Creer que correlación es causa.", "Dos hechos pueden coincidir sin que uno provoque el otro.", "Pregunta si hay un mecanismo que conecte ambos hechos."),
    ],
    T=[
        ("En Economía: ¿qué significa recaudar?", "Reunir dinero mediante el cobro de impuestos", "Es lo que hace el Estado con los impuestos."),
        ("{F} ¿Qué agente dice que con lo recaudado se financiarán programas de reciclaje?", "El Estado", "Quien cobra el impuesto es la autoridad del Estado."),
        ("{F} La dueña de la empresa de envases teme que sus costos suban. ¿Qué agente es? A) una familia, B) una empresa.", "B", "Produce y vende envases."),
        ("=", "{F} ¿Cuánto sube el precio de la bandeja por el impuesto (en pesos)?", "1000*5//100", "Se calcula el 5 % de 1.000."),
        ("=", "{F} ¿Cuánto pasa a costar la bandeja con el impuesto (en pesos)?", "1000+1000*5//100", "Se suma el impuesto al precio original."),
        ("{F} ¿Cuál de las voces propone responder al impuesto con importaciones (comercio exterior)? A) la familia, B) el importador.", "B", "Propone traer envases de papel desde otro país."),
        ("=", "{F} Una familia compra 40 bandejas al año. ¿Cuánto paga de más en impuesto en el año (en pesos)?", "40*(1000*5//100)", "Se multiplica el impuesto de una bandeja por 40."),
        ("=", "{F} Si el Estado recauda por este impuesto $50 por cada una de 2.000.000 de bandejas vendidas, ¿cuánto dinero recauda (en pesos)?", "50*2000000", "Se multiplica lo que paga cada bandeja por la cantidad vendida."),
        ("{F} Un diario afirma: «Las ventas de bandejas bajaron porque llegó el impuesto». Otro dato: ese mismo año también hubo menos turistas. ¿Qué concepto del vocabulario describe mejor el problema de afirmar una sola causa? A) multicausalidad, B) recaudar.", "A", "La baja de ventas puede deberse a varias causas a la vez."),
        ("{F} El importador trae envases de papel. ¿Qué efecto puede tener esa decisión sobre la empresa nacional de envases plásticos? Responde con una frase.", "Puede perder ventas, porque los consumidores podrían comprar el producto importado", "El comercio exterior ofrece una alternativa."),
        ("Una periodista escribe: «Cada vez que aumentan los helados aumentan los ahogamientos en piscinas». ¿Es una causa o una correlación? A) correlación, B) causa.", "A", "Ambos hechos coinciden por el verano, pero uno no causa el otro."),
        ("{F} Elige la conclusión mejor sostenida. A) el impuesto es injusto porque la empresa sube sus precios, B) el impuesto afecta de manera distinta a empresas, familias y Estado, y su evaluación debe considerar a todos.", "B", "Reconoce perspectivas y no atribuye toda la responsabilidad a un agente."),
        ("=", "{F} Si el impuesto pasara de 5 % a 10 %, ¿cuánto costaría la bandeja (en pesos)?", "1000+1000*10//100", "Se calcula el 10 % de 1.000 y se suma al precio."),
    ],
    ctx=("Una comuna de ejemplo quiere cobrar una tarifa a los camiones que usan el camino rural. Los transportistas dicen que sus costos subirán, los vecinos dicen que habrá menos tráfico pesado y la municipalidad dice que arreglará el camino. ¿Qué agente no aparece en estas voces? A) las empresas, B) las familias, C) el resto del mundo.", "C", "No se menciona comercio exterior; los transportistas son empresas, los vecinos son familias y la municipalidad es el Estado."),
    sc=[("En Economía: ¿qué es la multicausalidad?", "Que un hecho tiene varias causas a la vez", "Evita explicar un cambio con una sola causa."),
        ("¿Qué diferencia hay entre una causa y una correlación?", "La causa produce el efecto; la correlación es solo una coincidencia entre dos hechos", "Coincidir no prueba causar."),
        ("¿Qué agente recauda los impuestos?", "El Estado", "Los cobra y los destina a servicios.")],
    op=("{F} Elige dos de las voces y escribe: qué agente habla, cuál es su interés y qué efecto probable tiene el impuesto sobre él, con una cifra de la bandeja. Termina con una frase que diga qué otra información necesitarías para evaluar el impuesto.",
        "La familia: su interés es cuidar el presupuesto; la bandeja sube $50, de $1.000 a $1.050. La empresa: su interés es no perder ventas; su costo sube. Necesitaría saber cuántas bandejas se venderán después del impuesto.",
        ["identifica el agente de cada voz", "explica su interés", "usa una cifra", "propone información adicional"], ["dos voces analizadas y una pregunta final"], ["dar un solo punto de vista", "no usar ninguna cifra"], "Lee tu respuesta en voz alta y pide a una persona de tu casa que diga cuál voz le pareció mejor explicada."),
    reinforce="Elige un precio que haya subido en tu barrio y anota dos causas posibles.",
    extend="Explica con un ejemplo por qué una medida económica puede ser buena para el Estado y mala para una empresa.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Dossier de ejemplo, «¿Debe el Estado financiar más becas de alimentación escolar subiendo un impuesto?» "
      "Dato 1 (de ejemplo): 100.000 estudiantes necesitan beca y cada una cuesta $300.000 al año. "
      "Dato 2 (de ejemplo): el Estado recauda hoy $20.000 millones por un impuesto y podría subir ese monto en 10 %. "
      "Dato 3 (de ejemplo): una asociación de empresas dice que un alza de impuestos las obligaría a despedir personal. "
      "Dato 4 (de ejemplo): un estudio de un centro universitario dice que los niños que se alimentan bien en el colegio tienen mejores resultados escolares.")
build(
    OA, 5, F5,
    use="Aprenderé a armar un argumento económico con una tesis, evidencia, una objeción y un límite. Sirve para participar en debates sobre políticas públicas con fundamentos.",
    prior=["Sé qué son impuesto, escasez y costo de oportunidad.", "Sé distinguir dato de opinión y causa de correlación.", "Sé reconocer perspectivas distintas."],
    explain=[
        "Un argumento económico tiene una tesis, que es la afirmación que se defiende, y evidencia, que son datos o razones que la apoyan. Un buen argumento también reconoce una objeción, es decir, una razón que va en contra, y la responde. Finalmente indica un límite: qué información falta o hasta dónde llegan los datos. Así la conclusión es proporcional a la evidencia.",
        "En decisiones públicas siempre aparece la escasez: si el Estado destina más dinero a una política, tiene menos para otra. Por eso se compara el costo con el beneficio y se menciona el costo de oportunidad. Las cifras ayudan, pero no resuelven solas: los datos dicen cuánto cuesta algo, mientras que decidir si vale la pena también depende de los valores de cada persona.",
        "Para argumentar con honestidad conviene presentar la mejor versión de la postura contraria, no una caricatura. Si un dato del dossier va en contra de mi tesis, debo mencionarlo y explicar por qué mi conclusión sigue siendo razonable, o corregirla. Una conclusión sólida dice qué se puede afirmar y qué no con la evidencia disponible.",
    ],
    vocab=[("tesis", "afirmación que se defiende en un argumento"), ("evidencia", "datos o razones que apoyan una afirmación"), ("objeción", "razón que va en contra de una tesis"), ("proporcional", "que corresponde al tamaño de la evidencia disponible"), ("límite", "aquello que la evidencia disponible no permite afirmar")],
    worked=[
        ("Calcular el costo de una política", "Una política de ejemplo daría un beneficio de $150.000 al año a cada uno de 20.000 estudiantes. ¿Cuánto cuesta en total al año?",
         ["Se multiplica el valor por estudiante por el número de estudiantes.", "150.000 × 20.000 = 3.000.000.000."], "$3.000.000.000 al año"),
        ("Reconocer una objeción", "Una tesis dice que subir un impuesto es bueno porque financia becas. Un dato de ejemplo dice que algunas empresas podrían despedir personal. ¿Qué parte del argumento es el dato?",
         ["La tesis es subir el impuesto.", "El dato va en contra de la tesis: es una objeción."], "Una objeción"),
    ],
    mistakes=[
        ("Dar una opinión sin ningún dato que la respalde.", "Sin evidencia, el argumento no se puede comprobar.", "Cita al menos dos datos de la fuente."),
        ("Ignorar los datos que contradicen la tesis.", "Una objeción ocultada hace el argumento débil y poco honesto.", "Nombra la objeción y respóndela."),
    ],
    T=[
        ("En Economía: ¿qué es una tesis?", "Una afirmación que se defiende en un argumento", "Es el punto central que se quiere sostener."),
        ("{F} Según el dato 1, ¿cuánto cuesta cada beca al año?", "$300.000", "El dato lo informa."),
        ("{F} ¿Cuál es una objeción a subir el impuesto? A) el dato 3, B) el dato 4.", "A", "Dice que las empresas despedirían personal."),
        ("=", "{F} ¿Cuánto costaría financiar todas las becas del dato 1 en un año (en pesos)?", "100000*300000", "Se multiplica el número de estudiantes por el costo de cada beca."),
        ("=", "{F} Según el dato 2, ¿cuánto dinero más recaudaría el Estado con el alza del 10 % (en millones de pesos)?", "20000*10//100", "Se calcula el 10 % de 20.000 millones."),
        ("{F} ¿El dato 4 prueba que las becas mejoran las notas en el país? A) sí, es una prueba total, B) no, apoya la idea pero tiene un límite porque es un solo estudio.", "B", "Un estudio no basta para generalizar a todo el país."),
        ("=", "{F} Si el Estado financiara solo la mitad de las becas del dato 1, ¿cuántos estudiantes recibirían la beca?", "100000//2", "La mitad de 100.000 son 50.000."),
        ("=", "{F} Con el alza del 10 % del dato 2, ¿cuánto dinero total recaudaría el Estado (en millones de pesos)?", "20000+20000*10//100", "Se suma el aumento a lo que ya recauda."),
        ("{F} Un compañero afirma que con el alza basta para pagar todas las becas. Compara el costo de las becas (30.000 millones) con la recaudación total tras el alza (22.000 millones): ¿tiene razón? Responde con una frase.", "No, porque 22.000 millones no alcanzan para 30.000 millones", "La recaudación no cubre el costo."),
        ("Una tesis dice: «El Estado debe financiar las becas, pero con alza gradual del impuesto». ¿Cuál es la mejor respuesta a la objeción de las empresas? A) ignorarla, B) proponer un alza gradual que le dé tiempo a las empresas para adaptarse.", "B", "Reconoce el problema y propone una respuesta."),
        ("{F} Una frase de conclusión dice: «Está probado que las becas son la mejor política del país». ¿Qué problema tiene? A) afirma más de lo que prueban los datos, B) es demasiado corta.", "A", "No hay evidencia para comparar con todas las demás políticas."),
        ("{F} Ordena estas partes de un argumento: a) objeción, b) tesis, c) evidencia, d) límite. Escribe las letras en el orden más lógico para empezar y terminar.", "b, c, a, d", "Primero se afirma, luego se respalda, se reconoce lo contrario y se indica el límite."),
        ("=", "{F} Si cada beca costara $200.000 en lugar de $300.000, ¿cuánto costarían las 100.000 becas (en pesos)?", "100000*200000", "Se multiplica el nuevo costo por la cantidad de becas."),
    ],
    ctx=("Un centro de estudiantes de ejemplo debate si cobrar una cuota de $2.000 a cada uno de los 500 estudiantes para comprar libros de la biblioteca. Si todos pagan, ¿cuánto dinero reuniría con la cuota y cuál es una objeción posible? A) $1.000.000; algunas familias podrían no poder pagar, B) $100.000; ninguna objeción.", "A", "500 por 2.000 son 1.000.000, y hay familias con poco dinero."),
    sc=[("En Economía: ¿para qué sirve una objeción en un argumento?", "Para reconocer una razón contraria y responderla", "Hace el argumento más honesto y completo."),
        ("¿Qué quiere decir que una conclusión sea proporcional a la evidencia?", "Que afirma solo lo que los datos permiten afirmar", "Así se evita exagerar los resultados."),
        ("¿Por qué las cifras no resuelven solas una decisión pública?", "Porque decidir si algo vale la pena también depende de los valores de las personas", "Los datos dicen cuánto cuesta, no qué es más justo.")],
    op=("{F} Escribe un argumento de 5 a 7 líneas que diga si el Estado debe subir el impuesto para financiar becas. Incluye: tesis, dos datos, una objeción con su respuesta y un límite.",
        "Tesis: sí, debe subir gradualmente el impuesto. Datos: las becas cuestan 30.000 millones y el alza recauda 2.000 millones más. Objeción: las empresas podrían despedir; se responde con alza gradual. Límite: no sabemos cuánto más se necesitaría ni si un estudio basta.",
        ["declara una tesis", "usa dos datos del dossier", "responde una objeción", "indica un límite"], ["un argumento de 5 a 7 líneas"], ["no incluir ninguna objeción", "usar datos que no están en el dossier"], "Pide a una persona de tu casa que identifique tu tesis y tu objeción."),
    reinforce="Escribe una tesis sobre cómo gastar $20.000 de un presupuesto familiar y nombra una objeción.",
    extend="Elige una política pública que conozcas y escribe un límite de los datos que usarías para evaluarla.",
    materials=MAT,
)

# ================================================================ OA 20
OA = "HI1M OA 20"

# ---------------------------------------------------------------- Clase 1
F6 = ("Tabla de ejemplo, mercado de tomates de una feria, cajas por día según el precio por caja: "
      "precio $400, los compradores quieren 90 y los productores ofrecen 10; "
      "precio $600, quieren 70 y ofrecen 30; "
      "precio $800, quieren 50 y ofrecen 50; "
      "precio $1.000, quieren 30 y ofrecen 70; "
      "precio $1.200, quieren 10 y ofrecen 90.")
build(
    OA, 1, F6,
    use="Aprenderé a leer una tabla de oferta y demanda y a encontrar el precio en que el mercado queda equilibrado. Sirve para entender por qué los precios suben o bajan.",
    prior=["Sé qué es la escasez y qué son un bien y un servicio.", "Sé leer una tabla de varias filas.", "Sé restar números de dos y tres cifras."],
    explain=[
        "Un mercado es el lugar, físico o virtual, donde compradores y vendedores se encuentran para intercambiar bienes y servicios. La demanda es la cantidad que los compradores quieren y pueden comprar a cada precio: cuando el precio sube, se suele querer menos. La oferta es la cantidad que los productores quieren vender a cada precio: cuando el precio sube, se suele ofrecer más.",
        "El precio de equilibrio es aquel en que la cantidad demandada es igual a la cantidad ofrecida. En la tabla de ejemplo, a $800 los compradores quieren 50 cajas y los productores ofrecen 50, por lo que no sobra ni falta producto. Si el precio es mayor al de equilibrio, se ofrece más de lo que se demanda y hay excedente. Si es menor, se demanda más de lo que se ofrece y hay faltante.",
        "Los precios no son una decisión arbitraria de un solo actor: resultan de la interacción de oferta y demanda. Pero esto solo funciona bien si hay competencia, es decir, varios vendedores y compradores sin que uno solo mande. Antes de aplicar el modelo hay que revisar las condiciones del mercado, porque no todos los mercados funcionan igual.",
    ],
    vocab=[("mercado", "lugar donde compradores y vendedores intercambian bienes y servicios"), ("demanda", "cantidad que los compradores quieren y pueden comprar a cada precio"), ("oferta", "cantidad que los productores quieren vender a cada precio"), ("precio de equilibrio", "precio en que la cantidad demandada es igual a la ofrecida"), ("excedente", "cantidad que sobra cuando se ofrece más de lo que se demanda")],
    worked=[
        ("Hallar el equilibrio", "En una tabla de ejemplo, a $300 se demandan 40 unidades y se ofrecen 40. A $500 se demandan 20 y se ofrecen 60. ¿Cuál es el precio de equilibrio?",
         ["Busco el precio en que demanda y oferta son iguales.", "A $300: 40 y 40, son iguales."], "$300"),
        ("Calcular un excedente", "A $500 de la misma tabla de ejemplo se demandan 20 unidades y se ofrecen 60. ¿Hay excedente o faltante y de cuánto?",
         ["Comparo oferta y demanda: 60 contra 20.", "Se ofrece más de lo que se demanda: 60 - 20 = 40."], "Excedente de 40 unidades"),
    ],
    mistakes=[
        ("Creer que el precio lo fija siempre un solo vendedor.", "En un mercado con competencia, el precio resulta de la interacción de oferta y demanda.", "Pregunta cuántos vendedores y compradores hay antes de afirmar quién fija el precio."),
        ("Confundir excedente con faltante.", "El excedente es lo que sobra cuando se ofrece más de lo demandado; el faltante es lo contrario.", "Compara cuál cantidad es mayor, la ofrecida o la demandada."),
    ],
    T=[
        ("En Economía: ¿qué es la demanda?", "La cantidad que los compradores quieren y pueden comprar a cada precio", "Describe el lado de los compradores."),
        ("{F} ¿Cuántas cajas se ofrecen a $600?", "30", "Se lee en la fila del precio de $600."),
        ("En Economía: ¿qué es el precio de equilibrio? A) aquel en que cantidad demandada y ofrecida son iguales, B) el precio más bajo posible.", "A", "En ese precio no sobra ni falta producto."),
        ("{F} ¿Cuál es el precio de equilibrio de este mercado?", "$800", "A $800 se quieren 50 cajas y se ofrecen 50."),
        ("{F} A medida que el precio sube de $400 a $1.200, ¿qué pasa con la cantidad demandada? A) disminuye, B) aumenta.", "A", "Va de 90 a 10 cajas."),
        ("{F} A medida que el precio sube de $400 a $1.200, ¿qué pasa con la cantidad ofrecida? A) disminuye, B) aumenta.", "B", "Va de 10 a 90 cajas."),
        ("=", "{F} A $1.000, ¿cuántas cajas sobran (excedente)?", "70-30", "Se resta la cantidad demandada a la ofrecida."),
        ("=", "{F} A $400, ¿cuántas cajas faltan (faltante)?", "90-10", "Se resta la cantidad ofrecida a la demandada."),
        ("{F} A $600, ¿hay excedente o faltante y de cuántas cajas? Responde con una frase.", "Faltante de 40 cajas", "Se demandan 70 y solo se ofrecen 30; faltan 40."),
        ("{F} Los vendedores quieren vender todo y los compradores quieren comprar lo que necesitan. ¿A qué precio se logra eso sin que sobre ni falte producto?", "A $800", "Es el precio de equilibrio."),
        ("En una feria de ejemplo hay un solo vendedor de sandías. ¿Por qué no se cumple bien el modelo de oferta y demanda con competencia? A) porque ese vendedor puede influir en el precio por sí solo, B) porque las sandías son baratas.", "A", "Sin varios vendedores falta la competencia."),
        ("{F} Si el precio se fija en $1.200 en este mercado, ¿cuántas cajas se venden? Considera que solo se vende lo que se demanda y lo que se ofrece al mismo tiempo, es decir, la menor de las dos cantidades.", "10", "A ese precio se quieren 10 y se ofrecen 90; solo se concreta lo que ambos quieren."),
        ("=", "{F} Si se vendieran las cajas del precio de equilibrio, ¿cuánto dinero reciben en total los productores (en pesos)?", "800*50", "Se multiplica el precio por la cantidad vendida."),
    ],
    ctx=("Una dueña de una verdulería de ejemplo sube el precio de la lechuga de $500 a $900 y se queda con muchas lechugas sin vender. Según la clase, ¿qué ocurrió? A) el precio quedó sobre el equilibrio y hay excedente, B) el precio quedó bajo el equilibrio y hay faltante.", "A", "Se ofrece más de lo que los compradores quieren."),
    sc=[("En Economía: ¿qué es un mercado?", "Un lugar donde compradores y vendedores intercambian bienes y servicios", "Puede ser físico o virtual."),
        ("¿Qué pasa con la demanda cuando sube el precio?", "Se suele demandar menos", "Es la regla general de la demanda."),
        ("¿Qué indica el precio de equilibrio?", "Que la cantidad demandada es igual a la cantidad ofrecida", "No sobra ni falta producto.")],
    op=("Esta es una tabla de ejemplo del mercado de pan en un barrio, hogazas por día según el precio por hogaza: $1.000, demanda 60 y oferta 20; $1.500, demanda 45 y oferta 45; $2.000, demanda 30 y oferta 70. Escribe el precio de equilibrio, di si a $2.000 hay excedente o faltante y de cuánto, y explica en una frase por qué los precios no los decide un solo actor.",
        "El precio de equilibrio es $1.500. A $2.000 hay excedente de 40 hogazas (70 - 30). El precio resulta de lo que quieren comprar y vender muchos actores, no de uno solo.",
        ["halla el precio de equilibrio", "calcula el excedente", "explica la formación del precio"], ["tres respuestas breves con una cifra"], ["decir que a $2.000 hay faltante", "afirmar que el precio lo fija un solo vendedor"], "Pide a una persona de tu casa que compruebe tu cálculo del excedente."),
    reinforce="Anota el precio de un producto de tu barrio en dos negocios distintos y escribe una razón de la diferencia.",
    extend="Explica por qué un producto de temporada suele ser más barato cuando hay mucha cosecha.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F7 = ("Fuente A (de ejemplo, registro de precios de una feria): la caja de tomates costó $900 en septiembre y $1.350 en octubre. "
      "Fuente B (de ejemplo, nota de prensa de una cooperativa de agricultores): «Una helada destruyó la tercera parte de la cosecha de tomates de la zona; hay menos cajas para vender.» "
      "Fuente C (de ejemplo, opinión en una red social): «Los feriantes suben los precios porque son abusivos.»")
build(
    OA, 2, F7,
    use="Aprenderé a elegir fuentes que explican por qué cambia un precio y a distinguir causas con evidencia de opiniones. Sirve para evaluar noticias sobre alzas y bajas.",
    prior=["Sé qué son oferta, demanda y precio de equilibrio.", "Sé que una fuente tiene autor, fecha y propósito.", "Sé distinguir dato y opinión."],
    explain=[
        "Los precios cambian cuando se mueve la oferta o la demanda. Si hay un hecho que reduce lo que se produce, como una helada que destruye parte de la cosecha, la oferta disminuye: hay menos producto a cada precio y el precio de equilibrio sube. Si más compradores quieren un producto, aumenta la demanda y el precio también tiende a subir. Si aumenta la oferta o cae la demanda, el precio tiende a bajar.",
        "Para investigar un cambio de precio uso distintos tipos de fuente. Un registro de precios entrega el dato del cambio; una nota de prensa de una cooperativa puede explicar una causa, pero tiene el punto de vista de los productores; una opinión en una red social expresa una postura sin evidencia. Pregunto quién habló, cuándo, con qué propósito y si da datos comprobables.",
        "Una buena explicación combina un dato de cambio y una causa respaldada por evidencia. Si una fuente culpa de un alza a la mala intención de alguien, debo comprobar con datos de oferta y demanda antes de aceptarla. Seleccionar bien las fuentes ayuda a no confundir una causa real con una explicación simple pero sin pruebas.",
    ],
    vocab=[("disminuye la oferta", "se ofrece menos cantidad de un producto a cada precio"), ("aumenta la demanda", "se quiere comprar más cantidad de un producto a cada precio"), ("cosecha", "conjunto de frutos que se recogen del campo"), ("nota de prensa", "texto de una organización que informa un hecho a los medios"), ("causa", "hecho que produce un efecto")],
    worked=[
        ("Elegir una fuente para explicar", "Una caja de naranjas de ejemplo subió de precio. Fuente 1: registro de precios. Fuente 2: nota de prensa que informa una sequía que redujo la cosecha. ¿Cuál explica la causa?",
         ["El registro solo muestra que el precio subió.", "La nota informa un hecho que redujo la oferta: la sequía."], "La fuente 2"),
        ("Detectar una opinión sin evidencia", "Un comentario de ejemplo dice: «Esos vendedores son codiciosos y por eso la lechuga está cara». ¿Qué le falta?",
         ["El comentario culpa a un grupo.", "No entrega ningún dato de oferta, demanda ni cosecha."], "Le falta evidencia de oferta y demanda"),
    ],
    mistakes=[
        ("Aceptar la primera explicación que se oye sobre un alza.", "Puede ser una opinión sin respaldo.", "Busca una fuente que entregue datos de oferta y demanda."),
        ("Pensar que la nota de prensa de una organización es neutral.", "Puede mostrar el punto de vista de quienes la escriben.", "Pregunta quién la escribe y qué interés tiene."),
    ],
    T=[
        ("En Economía: ¿qué es una causa?", "Un hecho que produce un efecto", "Explica por qué algo ocurre."),
        ("{F} Según la fuente A, ¿en qué mes costó más la caja de tomates?", "En octubre", "La fuente informa $1.350 en octubre."),
        ("En Economía: si una helada destruye parte de la cosecha, ¿qué ocurre con la oferta? A) disminuye, B) aumenta.", "A", "Hay menos producto para vender."),
        ("{F} ¿Qué fuente da una causa del alza basada en un hecho concreto? A) la A, B) la B, C) la C.", "B", "Informa una helada que destruyó parte de la cosecha."),
        ("{F} ¿Qué fuente solo entrega un dato de precios sin explicar la causa? A) la A, B) la B, C) la C.", "A", "El registro muestra cuánto costó, no por qué."),
        ("{F} ¿Qué fuente expresa una opinión sin ninguna prueba? A) la A, B) la B, C) la C.", "C", "Afirma abuso, sin datos."),
        ("=", "{F} ¿Cuánto subió el precio de la caja entre septiembre y octubre (en pesos)?", "1350-900", "Se resta el precio de septiembre al de octubre."),
        ("=", "{F} ¿Qué porcentaje del precio de septiembre representó el alza?", "(1350-900)*100//900", "Se divide el alza por el precio inicial y se multiplica por 100.", "%"),
        ("=", "{F} La fuente B dice que se perdió la tercera parte de la cosecha. Si había 900 cajas previstas, ¿cuántas cajas quedaron?", "900-900//3", "Un tercio de 900 es 300, que se resta de 900."),
        ("{F} Un compañero dice que el alza se explica solo con la fuente C. ¿Qué le responderías con las fuentes A y B? Responde con una frase.", "Que las fuentes A y B muestran un alza y una pérdida de cosecha, que es una causa con datos", "La opinión no tiene evidencia; las otras dos sí."),
        ("Al comparar las tres fuentes, ¿cuál es la combinación más útil para explicar el alza? A) la A y la B, porque entregan el dato del cambio y una causa, B) la C sola, porque es la más reciente.", "A", "Una da el dato del cambio y la otra, la causa."),
        ("Si el alza se debiera a que muchos más compradores llegaron a la feria, ¿qué habría aumentado? A) la demanda, B) la oferta.", "A", "Más compradores aumentan la cantidad que se quiere comprar."),
        ("=", "{F} Si el precio de octubre se mantuviera en noviembre y una familia comprara 4 cajas, ¿cuánto gastaría (en pesos)?", "4*1350", "Se multiplica el precio de la caja por 4."),
    ],
    ctx=("Un noticiero de ejemplo informa que la palta subió de precio. Una vecina dice: «Es porque los comerciantes se pusieron de acuerdo». El noticiero dice que bajaron las lluvias y se cosechó menos. ¿Cuál afirmación tiene respaldo en un hecho verificable? A) la de la vecina, B) la del noticiero.", "B", "Menciona un hecho que reduce la oferta."),
    sc=[("En Economía: ¿qué le pasa a la oferta cuando se pierde parte de la cosecha?", "Disminuye", "Hay menos producto para vender."),
        ("¿Qué le falta a una opinión sin datos para explicar un alza?", "Evidencia de oferta y demanda", "Sin evidencia no se puede comprobar."),
        ("¿Por qué conviene usar dos fuentes para explicar un cambio de precio?", "Porque una entrega el dato del cambio y la otra la causa", "Las dos fuentes se complementan entre sí.")],
    op=("{F} Escribe una explicación de dos o tres líneas sobre por qué subió el precio de la caja de tomates. Cita las dos fuentes que usas, una cifra de cada una y descarta una fuente con una razón.",
        "El precio subió de $900 a $1.350 (fuente A) porque una helada destruyó un tercio de la cosecha y hubo menos cajas (fuente B). Descarto la fuente C porque es una opinión sin evidencia.",
        ["cita dos fuentes", "usa una cifra", "descarta una con razón"], ["explicación de dos o tres líneas"], ["usar la fuente C como prueba", "no citar cifras"], "Léele tu explicación a una persona de tu casa y pídele que diga qué fuente le convenció más."),
    reinforce="Mira el precio de un producto en dos días distintos y anota qué pudo haber cambiado.",
    extend="Explica qué fuente buscarías para comprobar que una alza se debe a más demanda.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F8 = ("Datos de ejemplo. País A: la canasta de bienes de una familia costaba $100.000 en 2020, $104.000 en 2021 y $109.000 en 2022. País B (ficticio): un índice de la canasta marcaba 100 en 2020, 98 en 2021 y 95 en 2022. "
      "Precio de una caja de manzanas en dos ciudades ficticias el mismo día: ciudad costera cercana al valle, $8.000; ciudad aislada del valle, $9.600.")
build(
    OA, 3, F8,
    use="Aprenderé a describir cómo cambian los precios en el tiempo (inflación y deflación) y por qué varían entre territorios. Sirve para leer noticias económicas y comparar el costo de vida.",
    prior=["Conozco la oferta, la demanda y el precio de equilibrio.", "Sé calcular un porcentaje sencillo.", "Sé leer una tabla de años."],
    explain=[
        "La inflación es un aumento general y sostenido de los precios; la deflación es una baja general y sostenida. No se trata de que un solo producto suba, sino de que el nivel de precios de muchos bienes cambie. Para medirlo se usa el índice de precios al consumidor, abreviado IPC, que sigue el costo de una canasta de bienes y servicios que consumen las familias a lo largo del tiempo.",
        "La variación de un valor se calcula con la fórmula: aumento ÷ valor inicial × 100. Si una canasta pasa de $100.000 a $104.000, el aumento es de $4.000 y la variación, de 4 %. Con inflación, el mismo dinero compra menos cosas, es decir, baja el poder de compra. Con deflación, el mismo dinero compra más, pero una baja general de precios puede indicar que la gente consume menos.",
        "El territorio también influye en los precios. Un producto cuesta más lejos de donde se produce porque el transporte y el almacenamiento suben los costos. Por eso una misma caja de manzanas puede valer distinto en dos ciudades. Describir bien un cambio de precios exige indicar el período, el lugar y la fuente de los datos, y distinguir lo que cambió de lo que se mantuvo.",
    ],
    vocab=[("inflación", "aumento general y sostenido de los precios"), ("deflación", "baja general y sostenida de los precios"), ("IPC", "índice que mide la variación de precios de una canasta de bienes y servicios"), ("poder de compra", "cantidad de bienes que se pueden comprar con una suma de dinero"), ("canasta", "conjunto de bienes y servicios que consume una familia")],
    worked=[
        ("Calcular una variación", "Una canasta de ejemplo costaba $200.000 y pasó a costar $210.000. ¿Cuál fue la variación porcentual?",
         ["El aumento es 210.000 - 200.000 = 10.000.", "La variación es 10.000 ÷ 200.000 × 100 = 5."], "5 %, hay inflación"),
        ("Explicar una diferencia territorial", "Un saco de papas de ejemplo cuesta $10.000 junto al campo y $12.000 en una ciudad a 600 km. ¿Qué puede explicar la diferencia?",
         ["La ciudad está lejos del lugar de producción.", "El transporte agrega costos al precio."], "El costo de transportar el producto"),
    ],
    mistakes=[
        ("Llamar inflación al alza de un solo producto.", "La inflación es un aumento general y sostenido de muchos precios.", "Mira una canasta amplia y varios períodos antes de hablar de inflación."),
        ("Pensar que una baja de precios siempre es buena noticia.", "Si la deflación es general, puede mostrar poco consumo y problemas en la economía.", "Pregunta por qué bajan los precios antes de celebrar."),
    ],
    T=[
        ("En Economía: ¿qué es la inflación?", "Un aumento general y sostenido de los precios", "No es el alza de un solo producto."),
        ("En Economía: ¿qué mide el IPC?", "La variación de precios de una canasta de bienes y servicios", "Sigue el costo de lo que consumen las familias."),
        ("{F} En el país A, ¿cuánto costaba la canasta en 2021?", "$104.000", "El dato aparece en los datos de ejemplo."),
        ("=", "{F} ¿Cuánto subió la canasta del país A entre 2020 y 2022 (en pesos)?", "109000-100000", "Se resta el costo inicial al final."),
        ("=", "{F} ¿Cuál fue la variación porcentual de la canasta del país A entre 2020 y 2021?", "(104000-100000)*100//100000", "Se divide el aumento por el costo inicial y se multiplica por 100.", "%"),
        ("{F} En el país B, donde el índice pasó de 100 a 98 y luego a 95, ¿hay inflación o deflación? A) inflación, B) deflación.", "B", "Los precios bajan de forma sostenida."),
        ("=", "{F} Entre 2021 y 2022, ¿cuánto subió la canasta del país A (en pesos)?", "109000-104000", "Se resta el costo de 2021 al de 2022."),
        ("{F} En el país A, ¿qué año tuvo mayor alza: 2021 o 2022? Calcula el aumento de cada año y responde.", "2022", "En 2021 subió $4.000 y en 2022 subió $5.000."),
        ("=", "{F} ¿Cuánta diferencia de precio hay entre la caja de manzanas de la ciudad aislada y la de la ciudad costera (en pesos)?", "9600-8000", "Se resta el precio menor al mayor."),
        ("{F} ¿Qué puede explicar que la caja de manzanas cueste más en la ciudad aislada? A) los costos de transporte hasta esa ciudad, B) que las manzanas son distintas por ser de otro país.", "A", "La distancia al valle sube los costos."),
        ("Una familia gana el mismo sueldo en 2020 y 2022 mientras su canasta pasa de $100.000 a $109.000. ¿Qué pasó con su poder de compra? A) bajó, B) subió.", "A", "Con el mismo dinero compra menos cosas."),
        ("{F} Un diario dice: «Los precios bajaron en el país B, así que su economía va perfecta». ¿Qué falta para sostener eso? A) saber por qué bajan los precios, B) más páginas del diario.", "A", "Una deflación puede deberse a poco consumo."),
        ("=", "{F} Si la canasta del país A siguiera subiendo $5.000 por año, ¿cuánto costaría en 2023 (en pesos)?", "109000+5000", "Se suma el alza anual al valor de 2022."),
    ],
    ctx=("Un colegio de ejemplo compra cuadernos y el proveedor informa que su lista de precios subió 8 % en un año, mientras el ingreso de la familia de un estudiante aumentó 3 % en el mismo período. ¿Qué pasó con el poder de compra de esa familia al comprar cuadernos? A) bajó, B) subió.", "A", "Los precios subieron más que los ingresos."),
    sc=[("En Economía: ¿qué diferencia hay entre inflación y deflación?", "La inflación es una alza general y sostenida de precios; la deflación es una baja general y sostenida", "Son procesos contrarios."),
        ("¿Cómo se calcula una variación porcentual?", "Dividiendo el aumento por el valor inicial y multiplicando por 100", "Mide el cambio en proporción."),
        ("¿Por qué un mismo producto puede costar más lejos de donde se produce?", "Porque el transporte agrega costos", "Es un efecto del territorio.")],
    op=("{F} Escribe un párrafo que diga: la variación porcentual del índice del país B entre 2020 y 2021 (de 100 a 98), si hay inflación o deflación y una razón territorial que explique por qué un producto puede costar distinto entre ciudades.",
        "Entre 2020 y 2021 el índice bajó de 100 a 98, una variación de 2 % a la baja; es deflación. Un producto puede costar más lejos de su zona de producción por los costos de transporte.",
        ["calcula la variación (2 % a la baja)", "clasifica el cambio como deflación", "da una razón territorial"], ["un párrafo con una cifra"], ["calcular la variación sobre el valor final", "no explicar el factor territorial"], "Pide a una persona de tu casa que revise tu cálculo."),
    reinforce="Anota el precio de tres productos que compra tu familia y revísalos en un mes.",
    extend="Explica por qué la inflación afecta más a quienes tienen ingresos fijos.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F9 = ("Casos de ejemplo. Caso 1: en un pueblo ficticio hay una sola empresa de agua potable, sin competidoras; sube su tarifa 20 %. "
      "Caso 2: las tres empresas de buses de una ciudad ficticia acuerdan en secreto cobrar el mismo pasaje alto y no competir. "
      "Caso 3: una autoridad de ejemplo fija un precio máximo para el pan de $1.000 por kilo, cuando el precio de equilibrio era $1.500. "
      "Caso 4: un país ficticio pone un arancel de 20 % a los zapatos importados que costaban $10.000 en la aduana.")
build(
    OA, 4, F9,
    use="Aprenderé a reconocer cuatro alteraciones del mercado (monopolio, colusión, fijación de precios y aranceles) y a comparar cómo las ven consumidores, empresas y Estado. Sirve para evaluar decisiones y noticias sobre precios.",
    prior=["Conozco oferta, demanda, precio de equilibrio, excedente y faltante.", "Sé calcular porcentajes sencillos.", "Sé distinguir dato y opinión."],
    explain=[
        "El mercado funciona mejor cuando hay competencia. Algunas situaciones lo alteran. En un monopolio hay un solo vendedor de un producto, sin competidores cercanos, y puede subir el precio con más facilidad. La colusión ocurre cuando empresas que deberían competir se ponen de acuerdo en secreto para fijar precios o repartirse el mercado, y es una práctica ilegal en Chile que las autoridades de libre competencia investigan y sancionan.",
        "El Estado también puede intervenir. La fijación de precios es cuando una autoridad establece un precio máximo o mínimo. Un precio máximo por debajo del equilibrio genera faltante, porque se demanda más de lo que se ofrece. Un arancel es un impuesto a los productos importados: sube su precio, protege a los productores nacionales, pero puede encarecer lo que pagan los consumidores y generar represalias de otros países.",
        "Cada actor ve estas medidas desde su perspectiva. Los consumidores quieren precios bajos y acceso; las empresas, ganancias y reglas claras; el Estado, equilibrar protección, recaudación y competencia. Evaluar una alteración exige preguntar quién gana, quién pierde, qué causas la explican y qué condiciones del mercado cambia, y no responder con una etiqueta.",
    ],
    vocab=[("monopolio", "mercado con un solo vendedor sin competidores cercanos"), ("colusión", "acuerdo secreto entre empresas competidoras para fijar precios o repartirse el mercado"), ("precio máximo", "precio más alto que una autoridad permite cobrar"), ("arancel", "impuesto que se cobra a los productos importados"), ("libre competencia", "situación en que varias empresas compiten por los compradores")],
    worked=[
        ("Identificar la alteración", "Dos empresas de ejemplo que venden el mismo producto acuerdan en secreto no bajar nunca sus precios. ¿Qué alteración es?",
         ["Hay un acuerdo secreto entre competidoras para fijar precios.", "Eso es colusión."], "Colusión"),
        ("Calcular un arancel", "Con un arancel de ejemplo de 10 %, un producto importado que cuesta $5.000 en la aduana, ¿cuánto pasa a costar?",
         ["El arancel es 5.000 × 10 ÷ 100 = 500.", "El nuevo costo es 5.000 + 500 = 5.500."], "$5.500"),
    ],
    mistakes=[
        ("Creer que cualquier alza de precios es colusión.", "La colusión exige un acuerdo entre competidoras; un alza puede deberse a otras causas.", "Pide evidencia del acuerdo antes de afirmarlo."),
        ("Pensar que un precio máximo siempre beneficia al consumidor.", "Si queda bajo el equilibrio puede generar faltante.", "Compara el precio máximo con el de equilibrio y calcula el faltante."),
    ],
    T=[
        ("En Economía: ¿qué es un monopolio?", "Un mercado con un solo vendedor sin competidores cercanos", "Esa es su definición."),
        ("En Economía: ¿qué es la colusión?", "Un acuerdo secreto entre empresas competidoras para fijar precios o repartirse el mercado", "Es una práctica ilegal."),
        ("{F} ¿Cuál de los cuatro casos es un monopolio? A) el caso 1, B) el caso 3.", "A", "Hay una sola empresa de agua, sin competidoras."),
        ("{F} ¿Cuál de los cuatro casos es una colusión? A) el caso 2, B) el caso 4.", "A", "Tres empresas acuerdan en secreto el precio del pasaje."),
        ("{F} ¿Qué caso es una fijación de precio por parte de una autoridad? A) el caso 3, B) el caso 1.", "A", "La autoridad impone un precio máximo."),
        ("=", "{F} En el caso 4, ¿cuánto vale el arancel por cada par de zapatos (en pesos)?", "10000*20//100", "Se calcula el 20 % de 10.000."),
        ("=", "{F} En el caso 4, ¿cuánto pasa a costar cada par con el arancel (en pesos)?", "10000+10000*20//100", "Se suma el arancel al costo en la aduana."),
        ("=", "{F} En el caso 3, ¿cuánto menor es el precio máximo que el de equilibrio (en pesos)?", "1500-1000", "Se resta el precio máximo al de equilibrio."),
        ("{F} En el caso 3, con el precio máximo por debajo del equilibrio, ¿qué es más probable? A) faltante, porque se demanda más de lo que se ofrece, B) excedente, porque se ofrece más de lo que se demanda.", "A", "A un precio bajo, los compradores quieren más y los productores ofrecen menos."),
        ("=", "{F} En el caso 1, la tarifa de agua era de $10.000 mensual para una familia. ¿Cuánto pagaría con el alza de 20 % (en pesos)?", "10000+10000*20//100", "El 20 % de 10.000 es 2.000 y se suma a la tarifa."),
        ("{F} Un vecino dice: «Con el arancel del caso 4, el consumidor gana». Con lo estudiado, ¿qué respuesta es más precisa? A) el consumidor paga más por el zapato importado, aunque los productores nacionales se protejan, B) el consumidor siempre paga menos.", "A", "El arancel sube el precio de lo importado."),
        ("{F} ¿Qué pregunta ayuda a verificar el caso 2? A) ¿hubo un acuerdo entre las tres empresas para fijar el pasaje?, B) ¿cuántos buses tiene cada una?", "A", "La colusión exige probar un acuerdo."),
        ("En el caso 1, una autoridad de ejemplo quiere impedir que el monopolio abuse. ¿Qué medida puede aplicar? A) regular la tarifa o abrir el mercado a competidores, B) prohibir que otras empresas entren al mercado.", "A", "Se busca limitar el poder de un único vendedor."),
    ],
    ctx=("Una asociación de consumidores de ejemplo descubre que las tres únicas cadenas de farmacias de una ciudad subieron el precio de un medicamento al mismo tiempo y en la misma cantidad. ¿Qué debe probar antes de hablar de colusión? A) que hubo un acuerdo entre las cadenas, B) que el medicamento es caro.", "A", "Un alza simultánea no prueba por sí sola un acuerdo."),
    sc=[("En Economía: ¿qué es un arancel?", "Un impuesto que se cobra a los productos importados", "Sube el precio de lo importado."),
        ("¿Qué ocurre si una autoridad fija un precio máximo bajo el equilibrio?", "Se genera un faltante", "Se demanda más de lo que se ofrece."),
        ("¿Qué distingue a un monopolio de una colusión?", "El monopolio es un solo vendedor; la colusión es un acuerdo entre varios competidores", "Son alteraciones distintas.")],
    op=("{F} Elige dos de los cuatro casos y escribe para cada uno: qué alteración es, quién gana, quién pierde y una pregunta que harías para evaluar mejor la situación. Usa una cifra del caso.",
        "Caso 3: es una fijación de precio máximo; ganan las familias que alcanzan a comprar pan a $1.000; pierden las que no lo encuentran y las panaderías; pregunta: ¿cuánto pan falta a ese precio?",
        ["identifica la alteración", "señala quién gana y quién pierde", "formula una pregunta de evaluación"], ["dos casos analizados con una cifra"], ["decir que la medida beneficia a todos", "usar el nombre de la alteración equivocada"], "Léele a una persona de tu casa uno de tus casos y pídele que diga si falta algún actor."),
    reinforce="Escribe tres frases, una por cada alteración (monopolio, colusión, arancel), con tus palabras.",
    extend="Explica por qué la colusión perjudica sobre todo a los consumidores.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F10 = ("Dossier de ejemplo, «¿Debe fijarse un precio máximo al pan?». Mercado del pan, kilos por día según el precio por kilo: "
       "$1.000, demanda 150 y oferta 60; $1.500, demanda 110 y oferta 110; $2.000, demanda 70 y oferta 160. "
       "Voz 1 (de ejemplo, una familia): «Con el pan caro apenas nos alcanza.» "
       "Voz 2 (de ejemplo, una panadería): «Si nos obligan a vender a $1.000, produciremos menos.» "
       "Voz 3 (de ejemplo, una autoridad): «Queremos proteger a las familias sin dejar al barrio sin pan.»")
build(
    OA, 5, F10,
    use="Aprenderé a defender una postura sobre una medida de mercado con datos de oferta y demanda, una objeción y un límite. Sirve para participar en debates económicos con evidencia.",
    prior=["Sé leer una tabla de oferta y demanda.", "Conozco precio máximo, excedente y faltante.", "Sé armar un argumento con tesis y evidencia."],
    explain=[
        "Para decidir si conviene una medida sobre los precios no basta con intuiciones. Se parte de un modelo: se comparan la oferta y la demanda a cada precio y se calcula qué ocurriría con la medida. Si un precio máximo queda bajo el equilibrio, aumenta la cantidad demandada y baja la ofrecida, y aparece un faltante. Si queda sobre el equilibrio, la medida casi no tiene efecto.",
        "El modelo tiene límites. Supone competencia y que se pueda producir más o menos con facilidad. Además hay valores en juego: la autoridad puede querer proteger a las familias con menos ingresos aunque exista un faltante, y proponer subsidios o programas para atenuarlo. Por eso un buen argumento nombra los efectos y las alternativas, y no solo condena o defiende la medida.",
        "Mi argumento debe incluir una tesis, evidencia numérica de la tabla, una objeción razonable con su respuesta y un límite. Debo mostrar cómo se calcula el faltante o el excedente y qué actores ganan o pierden. Si la evidencia no permite saber algo, como la cantidad exacta de familias afectadas, lo digo en vez de inventarlo.",
    ],
    vocab=[("tesis", "afirmación que se defiende en un argumento"), ("subsidio", "ayuda en dinero del Estado para reducir un costo"), ("faltante", "cantidad que no alcanza cuando se demanda más de lo que se ofrece"), ("intervención", "acción de una autoridad para modificar el funcionamiento de un mercado"), ("límite", "aquello que la evidencia disponible no permite afirmar")],
    worked=[
        ("Calcular el faltante de una medida", "En un mercado de ejemplo, a un precio máximo de $500 se demandan 80 unidades y se ofrecen 30. ¿Cuál es el faltante?",
         ["Comparo las dos cantidades al precio máximo.", "80 - 30 = 50."], "Faltante de 50 unidades"),
        ("Distinguir efecto y valor", "Una autoridad de ejemplo dice: «Prefiero un faltante pequeño a que las familias pobres no puedan comprar». ¿Qué parte es el valor?",
         ["El faltante es un efecto que se calcula.", "Priorizar a las familias es un valor que se defiende."], "Priorizar a las familias pobres es el valor"),
    ],
    mistakes=[
        ("Defender un precio máximo sin calcular su faltante.", "No se conoce el efecto real de la medida.", "Calcula la diferencia entre demanda y oferta al precio propuesto."),
        ("Presentar la postura contraria como una caricatura.", "Pierde credibilidad y no responde a las razones reales.", "Cita la mejor versión de la objeción."),
    ],
    T=[
        ("En Economía: ¿qué es un subsidio?", "Una ayuda en dinero del Estado para reducir un costo", "Puede atenuar los efectos de una medida."),
        ("{F} A un precio máximo de $1.000, ¿cuántos kilos de pan se demandan?", "150", "Se lee en la tabla."),
        ("{F} ¿Cuál es el precio de equilibrio del pan? A) $1.000, B) $1.500, C) $2.000.", "B", "A ese precio se demandan 110 y se ofrecen 110."),
        ("=", "{F} Con un precio máximo de $1.000, ¿cuántos kilos de pan faltan por día?", "150-60", "Se resta la oferta a la demanda."),
        ("=", "{F} Con el precio de $2.000, ¿cuántos kilos de pan sobran por día?", "160-70", "Se resta la demanda a la oferta."),
        ("{F} Cuando el precio baja de $1.500 a $1.000, ¿qué pasa con la cantidad ofrecida? A) disminuye de 110 a 60 kilos, B) aumenta de 110 a 150 kilos.", "A", "Los productores ofrecen menos cuando el precio baja."),
        ("{F} Un precio máximo de $2.500 está sobre el equilibrio. ¿Qué efecto tiene en este mercado? A) casi ninguno, B) un faltante grande.", "A", "El precio de equilibrio ya es menor y no se modifica."),
        ("=", "{F} Si la panadería produjera en el nivel de la oferta a $1.000 y vendiera todo a ese precio, ¿cuánto dinero recibiría por día (en pesos)?", "1000*60", "Se multiplica el precio máximo por los kilos que se ofrecen."),
        ("=", "{F} Si a $1.500 se vendiera todo lo ofrecido, ¿cuánto dinero recibiría la panadería por día (en pesos)?", "1500*110", "Se multiplica el precio de equilibrio por los kilos ofrecidos."),
        ("{F} La voz 2 dice que producirán menos si deben vender a $1.000. ¿Qué dato de la tabla apoya esa idea? Responde con una frase.", "Que a $1.000 se ofrecen 60 kilos, menos que los 110 que se ofrecen a $1.500", "La oferta baja cuando el precio baja."),
        ("{F} La voz 3 busca proteger a las familias sin dejar sin pan al barrio. ¿Qué medida complementaria sirve? A) un subsidio a las familias de menores ingresos, B) eliminar toda medida.", "A", "Atenúa el efecto sin crear un faltante tan grande."),
        ("{F} Una conclusión dice: «El precio máximo de $1.000 es bueno porque el pan queda barato». ¿Qué le falta? A) mencionar el faltante de 90 kilos por día, B) más adjetivos.", "A", "Un efecto importante queda fuera de la conclusión."),
        ("{F} Con un precio máximo de $1.000, ¿cuántos kilos de pan se venden realmente por día, si solo se vende lo que se ofrece?", "60", "Aunque se demandan 150, solo hay 60 kilos para vender."),
    ],
    ctx=("Un municipio de ejemplo estudia fijar un precio máximo para el arriendo de bicicletas de la plaza. Si el precio máximo es menor al de equilibrio, ¿qué problema es más probable? A) que falten bicicletas disponibles, B) que sobren bicicletas.", "A", "Con precio bajo se demanda más de lo que se ofrece."),
    sc=[("En Economía: ¿qué efecto tiene un precio máximo bajo el equilibrio?", "Genera un faltante", "Se demanda más de lo que se ofrece."),
        ("¿Qué diferencia hay entre un efecto y un valor en un argumento?", "El efecto se calcula con datos; el valor expresa qué se considera importante", "Ambos aparecen en las decisiones públicas."),
        ("¿Qué es un subsidio?", "Una ayuda en dinero del Estado para reducir un costo", "Puede atenuar un precio alto.")],
    op=("{F} Escribe un argumento de cinco a siete líneas sobre si conviene fijar un precio máximo de $1.000 al pan. Incluye tu tesis, el faltante calculado, una objeción con su respuesta y un límite de los datos.",
        "Tesis: no conviene fijar $1.000. A ese precio se demandan 150 y se ofrecen 60: faltan 90 kilos. Objeción: las familias necesitan pan barato; se responde con un subsidio. Límite: no sabemos cuántas familias necesitan el subsidio.",
        ["declara tesis", "calcula el faltante", "responde una objeción", "indica un límite"], ["un argumento de cinco a siete líneas"], ["no calcular el faltante", "no mencionar ninguna alternativa"], "Léele tu argumento a una persona de tu casa y pídele que diga si respondes a la objeción."),
    reinforce="Anota un precio máximo que conozcas de la vida cotidiana y escribe qué efecto puede tener.",
    extend="Explica cómo cambiaría tu conclusión si el pan se importara y no hubiera panaderías locales.",
    materials=MAT,
)
