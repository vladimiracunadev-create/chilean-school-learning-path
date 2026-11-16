"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 03 clases 4 a 6 (relaciones y consecuencias, evaluación de alternativas, conclusión situada). Datos de ejemplo inventados."""
from __future__ import annotations

from fg_chla_common import build

O3 = "FG-CHLA-3y4-OAC-03"

# ============================================================ OA 03, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados; país ficticio Tierra Fértil, miles de millones de u.m.). Año 1: ingresos del Estado 100, de los cuales 40 vienen del mineral X y 60 de otras fuentes; "
     "el Estado gasta la mitad de sus ingresos en educación, salud y ayudas a las familias (gasto social). Año 2: el precio del mineral X baja y sus ingresos pasan de 40 a 30; las otras fuentes siguen en 60. "
     "El Estado tiene un pequeño fondo de ahorro y también puede pedir préstamos.")
build(
    O3, 4, F,
    use="Aprenderé a explicar relaciones y consecuencias entre precios de las materias primas, ingresos del Estado, empleo, pobreza y desigualdad en América Latina.",
    explain=[
        'Muchas economías latinoamericanas exportan materias primas, como minerales, productos agrícolas o pesca. Los precios internacionales de esos productos suben y bajan. Cuando el precio baja, el país recibe menos ingresos por sus exportaciones y el Estado recauda menos; entonces puede recortar el gasto, pedir préstamos o usar ahorros. Cuando el precio sube ocurre lo contrario. Por eso se dice que una economía muy dependiente de pocos productos es más vulnerable.',
        'El crecimiento económico puede ayudar a reducir la pobreza si genera empleos y mejores ingresos, pero no la elimina por sí solo: si sus beneficios se concentran en pocos, la desigualdad puede mantenerse. A su vez, la desigualdad puede frenar el desarrollo, porque limita el acceso a educación y salud. Una buena explicación conecta pasos en cadena (causa, mecanismo y efecto) y no afirma más de lo que muestran los datos. También conviene decir qué tan grande es un efecto: una baja de 10 % no es lo mismo que una de 50 %.',
    ],
    vocab=[("materia prima", "producto básico, como un mineral o un cultivo, que se vende sin gran transformación"), ("ingresos fiscales", "dinero que recibe el Estado, por ejemplo por impuestos"), ("gasto social", "dinero que el Estado destina a educación, salud y ayudas a las familias"), ("vulnerabilidad", "facilidad para sufrir daño cuando algo cambia"), ("fondo de ahorro", "dinero que el Estado guarda para usarlo en años difíciles")],
    worked=[
        ("Seguir una cadena", "En un país de ejemplo cae el precio de su producto principal. ¿Qué efecto en cadena es esperable en el Estado?", ["Baja el valor de las exportaciones.", "Con menos ingresos, el Estado dispone de menos dinero para gastar."], "Menos ingresos fiscales"),
        ("Medir el tamaño de un efecto", "Los ingresos de un Estado de ejemplo pasan de 100 a 90. ¿Cuánto bajaron?", ["Bajaron 10 unidades.", "Eso es 10 de 100, es decir, 10 %."], "10 %"),
    ],
    mistakes=[("Afirmar que si baja un precio, bajará necesariamente la pobreza o subirá, sin mirar los pasos intermedios.", "Entre ambos hechos hay mecanismos y otros factores.", "Escribe cada eslabón de la cadena y busca datos para comprobarlo."),
              ("Creer que el crecimiento elimina la desigualdad por sí solo.", "Depende de cómo se reparten sus beneficios.", "Mira la distribución del ingreso además del PIB.")],
    T=[
        ('¿Qué es una materia prima?', 'Un producto básico que se vende casi sin transformarlo', 'Un producto industrial con tecnología muy avanzada y mucho valor agregado', 'Un servicio financiero que los bancos prestan a las empresas del país', 'Las materias primas, como minerales o cultivos, se venden con poco procesamiento.'),
        ('¿Qué son los ingresos fiscales?', 'Lo que recibe el Estado, por ejemplo por impuestos', 'El dinero que gana cada familia con su trabajo', 'El dinero que las empresas ahorran para invertir', 'Los ingresos fiscales son los del Estado; los de familias y empresas son otro concepto.'),
        ('¿Qué es el gasto social?', 'Dinero del Estado para educación, salud y ayudas a las familias', 'Dinero que las empresas gastan en publicidad', 'Dinero que los hogares gastan en fiestas familiares', 'El gasto social es una parte del gasto del Estado dirigida al bienestar de las personas.'),
        ('=', '{F} ¿Cuánto gastó el Estado en gasto social en el año 1 (la mitad de sus ingresos)?', '100//2', 'Se calcula la mitad de los ingresos del año 1.', ' mil millones de u.m.'),
        ('=', '{F} ¿Cuánto recibió el Estado en total en el año 2 (mineral X más otras fuentes)?', '30+60', 'Se suman los ingresos del mineral X y los de otras fuentes.', ' mil millones de u.m.'),
        ('=', '{F} ¿En cuánto bajaron los ingresos del Estado entre el año 1 y el año 2?', '100-90', 'Se resta el ingreso del año 2 al del año 1.', ' mil millones de u.m.'),
        ('{F} ¿Qué porcentaje bajaron los ingresos totales del Estado del año 1 al año 2?', '10 %', '25 %', '30 %', 'Bajaron 10 sobre 100, es decir 10 %; el 25 % es la baja de los ingresos del mineral X (de 40 a 30).'),
        ('=', '{F} Si el Estado mantiene el gasto social de la mitad de sus ingresos del año 2, ¿cuánto sería?', '90//2', 'Se calcula la mitad de los ingresos del año 2.', ' mil millones de u.m.'),
        ('{F} Si el Estado quisiera mantener el gasto social del año 1 sin cambiar sus ingresos del año 2, ¿qué opciones tendría?', 'Usar el fondo de ahorro o pedir préstamos para cubrir la diferencia', 'Aumentar el precio internacional del mineral X por decreto', 'Dejar de gastar en todo lo que no sea gasto social', 'Con menos ingresos, mantener el gasto exige usar ahorros o deuda; el Estado no fija el precio mundial de un mineral.'),
        ('{F} ¿Por qué se dice que Tierra Fértil es vulnerable al precio del mineral X?', 'Porque gran parte de los ingresos del Estado depende de él', 'Porque el mineral X se exporta a todos los países de la región y del mundo', 'Porque el precio del mineral X nunca cambia durante todo el año económico', 'El 40 % de los ingresos del año 1 venía del mineral, así que su precio afecta mucho al Estado.'),
        ('{F} Alguien dice: «Si el precio baja, la pobreza aumentará con seguridad». ¿Qué respuesta es más precisa?', 'Puede ocurrir, pero depende de cómo respondan Estado y hogares', 'Es seguro, porque el precio del mineral decide todo en la economía del país', 'Es imposible, porque el precio internacional no afecta nunca a los hogares', 'Hay mecanismos intermedios, como el uso del ahorro o los empleos del sector, y no es una consecuencia automática.'),
        ('{F} ¿Qué medida podría reducir la vulnerabilidad del Estado en el futuro?', 'Ahorrar parte de los ingresos extra de los años buenos', 'Gastar todo el ingreso extra apenas llega', 'Concentrar aún más las exportaciones en el mineral X', 'Un fondo de ahorro amortigua las caídas; gastar todo o concentrar más aumentan el riesgo.'),
        ('Un país de ejemplo crece 5 % al año, pero el 20 % más rico recibe casi todo el aumento. ¿Qué efecto es esperable en la desigualdad?', 'Que la desigualdad se mantenga o aumente', 'Que la desigualdad desaparezca sola', 'Que la pobreza baje igual para todos', 'Cuando el beneficio se concentra, el crecimiento no reduce la desigualdad.'),
    ],
    ctx=('En un país de ejemplo, el precio de su cultivo principal sube y el Estado recibe más ingresos. El gobierno gasta todo en un año y guarda cero ahorro. Si el precio baja al año siguiente, ¿qué problema es probable?', 'Deberá recortar gasto o endeudarse por falta de ahorro', 'Tendrá más dinero que antes para gastar en educación y en salud', 'No cambiará nada, porque el ahorro no sirve cuando hay una caída de precios', 'Sin ahorro, la caída de ingresos obliga a recortar o a pedir préstamos.'),
    sc=[
        ('¿Qué relación hay entre el precio de una materia prima y los ingresos del Estado?', 'Si el precio baja, el Estado suele recaudar menos', 'Los ingresos fiscales dependen en parte del valor de las exportaciones.'),
        ('=', 'Los ingresos de un Estado de ejemplo pasan de 200 a 180. ¿En cuánto bajaron?', '200-180', 'Se resta el ingreso nuevo al anterior.', ' mil millones de u.m.'),
        ('¿Por qué es importante decir qué tan grande es un efecto?', 'Porque una baja de 10 % no tiene las mismas consecuencias que una de 50 %', 'El tamaño de un cambio ayuda a juzgar su importancia.'),
    ],
    op=("Usa la {F} Escribe una cadena con cinco eslabones desde la baja del precio del mineral X hasta una posible consecuencia en las familias. Indica en cuál eslabón el Estado puede intervenir y con qué medida.",
        "Baja el precio del mineral X → bajan los ingresos de exportación → el Estado recauda 10 % menos → debe recortar gasto social, usar ahorro o pedir préstamos → podrían reducirse ayudas o servicios para las familias. El Estado puede intervenir en el cuarto eslabón usando el fondo de ahorro para sostener el gasto.",
        ["cinco eslabones conectados", "usa datos de la ficha", "propone una medida concreta"], ["cadena de cinco eslabones", "una medida"], ["saltarse eslabones", "afirmar certezas sin matices"],
        "Pregunta qué dato mostraría que un eslabón no se cumple."),
    rx=("Explica con tus palabras por qué ahorrar en los años buenos reduce la vulnerabilidad.", "Averigua con apoyo de tu docente cuál es el principal producto de exportación de tu país y escribe cómo afectaría un cambio de precio."),
)

# ============================================================ OA 03, clase 5
F = ("Ficha 5 (datos de ejemplo, inventados; país ficticio Tierra Fértil, millones de u.m.). Tres programas posibles para reducir la pobreza y la desigualdad. "
     "Programa A: transferencias de dinero a hogares pobres; cuesta 600 y llega a 300 hogares; efecto rápido (un año), no cambia la estructura de la economía. "
     "Programa B: capacitación técnica para personas desempleadas; cuesta 900 y llega a 150 personas; efecto en dos o tres años. "
     "Programa C: incentivos para crear una industria nueva; cuesta 1.200 y crearía 100 empleos; efecto en cinco años o más, y diversifica la economía.")
build(
    O3, 5, F,
    use="Aprenderé a evaluar alternativas de política económica y social con criterios como costo por beneficiario, plazo, alcance y efecto sobre la matriz productiva.",
    explain=[
        'Evaluar políticas para enfrentar la pobreza, la desigualdad o la dependencia de pocos productos exige criterios. Algunos son: el costo por beneficiario (costo total dividido por personas o hogares que llegan a recibir el beneficio), el plazo en que se ven los efectos, el alcance (a cuántas personas llega), si el efecto es duradero y si cambia la estructura de la economía. Los programas se pueden combinar: uno de efecto rápido y otro de efecto largo.',
        'Ninguna alternativa es mejor en todo. Una transferencia de dinero ayuda rápido, pero no crea empleos por sí misma; la capacitación mejora las oportunidades de las personas, pero tarda; una industria nueva diversifica la economía, pero cuesta más y demora. Para decidir hay que explicitar qué objetivo se prioriza, qué datos faltan y a quién deja fuera cada opción. La evaluación con números ayuda, pero las decisiones también implican valores, y por eso se justifican con argumentos y no con una cifra única.',
    ],
    vocab=[("costo por beneficiario", "costo total dividido por las personas que reciben el beneficio"), ("plazo", "tiempo en que se ven los resultados de una medida"), ("alcance", "cantidad de personas a las que llega una medida"), ("transferencia", "dinero que el Estado entrega a hogares sin que den algo a cambio"), ("incentivo", "ayuda que anima a las empresas a realizar una actividad")],
    worked=[
        ("Costo por beneficiario", "Un programa de ejemplo cuesta 500 y llega a 100 hogares. ¿Cuál es el costo por hogar?", ["Se divide el costo total por los hogares.", "500 ÷ 100 da el costo por hogar."], "5"),
        ("Plazo y objetivo", "Un gobierno de ejemplo necesita ayudar a familias que no tienen ingresos este mes. ¿Qué criterio pesa más?", ["Se necesita un efecto inmediato.", "El plazo corto es el criterio más relevante."], "El plazo corto"),
    ],
    mistakes=[("Elegir siempre la alternativa más barata.", "El costo es un criterio, pero también importan el alcance, el plazo y los efectos duraderos.", "Compara varias medidas a la vez."),
              ("Decir que una alternativa es la mejor sin indicar el objetivo.", "La mejor opción depende de lo que se quiere lograr.", "Primero define el objetivo y luego compara.")],
    T=[
        ('¿Qué es el costo por beneficiario?', 'El costo total dividido por quienes reciben el beneficio', 'El costo total multiplicado por las personas atendidas', 'El costo total dividido por el número de programas', 'El costo por beneficiario se obtiene dividiendo el gasto por quienes reciben el beneficio.'),
        ('¿Qué es una transferencia monetaria?', 'Dinero que el Estado entrega a hogares sin pedir nada', 'Un préstamo que los hogares deben devolver al Estado con intereses', 'Un impuesto que se cobra cada año a las familias con más ingresos', 'Una transferencia es una entrega directa de dinero; no es préstamo ni impuesto.'),
        ('¿Qué mide el alcance de un programa?', 'A cuántas personas o hogares llega', 'Cuánto tarda en dar resultados', 'Cuánto cuesta por beneficiario', 'El alcance se refiere a la cantidad de personas atendidas.'),
        ('=', '{F} ¿Cuál es el costo por hogar del Programa A?', '600//300', 'Se divide el costo total por el número de hogares.', ' millones de u.m.'),
        ('=', '{F} ¿Cuál es el costo por persona capacitada del Programa B?', '900//150', 'Se divide el costo total por el número de personas.', ' millones de u.m.'),
        ('=', '{F} ¿Cuál es el costo por empleo creado del Programa C?', '1200//100', 'Se divide el costo total por el número de empleos.', ' millones de u.m.'),
        ('{F} Si solo se mira el costo por beneficiario, ¿qué programa parece más barato?', 'El Programa A', 'El Programa B', 'El Programa C', 'El Programa A cuesta 2 por hogar, el B 6 y el C 12 por empleo.'),
        ('{F} ¿Qué programa tarda más en dar resultados?', 'El Programa C', 'El Programa A', 'El Programa B', 'La ficha indica cinco años o más para el Programa C; el A da efectos en un año.'),
        ('{F} ¿Qué programa diversifica la matriz productiva?', 'El Programa C', 'El Programa A', 'El Programa B', 'La industria nueva agrega una actividad económica; las otras dos no cambian la estructura productiva por sí solas.'),
        ('{F} Alguien dice: «El Programa A es el mejor, porque es el más barato». ¿Qué objeción es más sólida?', 'Que no cambia la estructura de la economía, aunque sea rápido y barato por hogar', 'Que el Programa A cuesta más que el C por cada hogar que recibe ayuda', 'Que ningún programa de transferencias de dinero llega a hogares pobres', 'El costo es solo un criterio; el A es rápido, pero no transforma la economía.'),
        ('{F} Si el objetivo es ayudar a los hogares pobres en el plazo más corto de los tres, ¿qué programa responde mejor?', 'El Programa A, de efecto más rápido', 'El Programa B, de capacitación', 'El Programa C, de industria nueva', 'El Programa A tiene efecto en un año; el B tarda dos o tres años y el C cinco o más.'),
        ('{F} ¿Qué combinación equilibra plazo corto y cambio de estructura?', 'Programa A más Programa C', 'Programa B más Programa C', 'Solo el Programa A', 'Una transferencia rápida junto a una industria nueva cubre el corto y el largo plazo.'),
        ('{F} Un funcionario propone usar solo un criterio, el costo por beneficiario, para decidir. ¿Qué problema tendría?', 'Dejaría fuera plazo, efecto duradero y cambio de estructura', 'Sería imposible calcular el costo por beneficiario con los datos', 'Haría que el Programa C quedara siempre con el menor costo', 'Un solo criterio simplifica y puede ocultar efectos importantes.'),
    ],
    ctx=('Un programa de ejemplo cuesta 800 y beneficia a 200 hogares; otro cuesta 600 y beneficia a 100 hogares. ¿Cuál tiene menor costo por hogar y cuánto es?', 'El primero, con 4 por hogar', 'El segundo, con 6 por hogar', 'El primero, con 8 por hogar', 'Se calcula 800 ÷ 200 = 4 y 600 ÷ 100 = 6; el primero cuesta menos por hogar.'),
    sc=[
        ('Nombra dos criterios para evaluar una política contra la pobreza.', 'Por ejemplo, costo por beneficiario y plazo', 'También sirven alcance, duración del efecto y cambio de estructura.'),
        ('=', 'Un programa de ejemplo cuesta 450 y llega a 150 hogares. ¿Cuál es el costo por hogar?', '450//150', 'Se divide el costo total por los hogares.', ' millones de u.m.'),
        ('¿Por qué la elección de una política implica valores y no solo números?', 'Porque se debe decidir a quién se prioriza y qué objetivos importan más', 'Los datos informan, pero la decisión también implica juicios sobre qué priorizar.'),
    ],
    op=("Usa la {F} Redacta una recomendación de seis líneas: qué programa o combinación elegirías, con el costo por beneficiario de cada uno; qué objetivo priorizas; a quién podría dejar fuera; y qué dato nuevo pedirías antes de decidir.",
        "Recomiendo combinar A y C. A cuesta 2 por hogar y ayuda rápido; C cuesta 12 por empleo y diversifica la economía. Priorizo reducir la pobreza ahora y cambiar la estructura después. Podría dejar fuera a personas desempleadas que necesitan capacitación. Pediría datos sobre cuántos hogares quedan fuera de A y cuántas personas podrían ocupar los empleos de C.",
        ["calcula costos por beneficiario", "explicita el objetivo", "reconoce a quién deja fuera"], ["seis líneas"], ["decidir solo por costo", "no mencionar a quién deja fuera"],
        "Revisa si tu recomendación cambiaría si el objetivo fuera otro."),
    rx=("Calcula el costo por beneficiario de dos programas inventados por ti y compáralos.", "Conversa con una persona de tu casa sobre qué ayuda pública considera más útil para una familia y por qué."),
)

# ============================================================ OA 03, clase 6
F = ("Ficha 6 (datos de ejemplo, inventados; dos países ficticios). Tierra Fértil: el PIB creció 10 %, la tasa de desempleo es 10 % y el 20 % más rico recibe 10 veces lo que el 20 % más pobre. "
     "Mar Azul: el PIB creció 4 %, la tasa de desempleo es 6 % y el 20 % más rico recibe 6 veces lo que el 20 % más pobre. "
     "Nota: son datos de un solo año; no se conocen las causas de las diferencias.")
build(
    O3, 6, F,
    use="Aprenderé a comunicar una conclusión situada sobre un desafío económico y social: con afirmación, evidencia, límites y propuesta, sin generalizar más allá de los datos.",
    explain=[
        'Una conclusión situada es una conclusión que dice a qué lugar, tiempo y datos se refiere. No afirma «en América Latina pasa esto» si solo se estudiaron dos países en un año. Una buena conclusión tiene cuatro partes: una afirmación clara, la evidencia que la respalda (con cifras de la fuente), un límite o matiz (qué no se puede decir con esos datos) y una propuesta o pregunta que invite a seguir investigando o actuando.',
        'También conviene usar palabras de prudencia cuando corresponde: «en estos datos», «parece», «podría». No es debilidad: es precisión. Hay que separar los hechos (las cifras) de las opiniones o interpretaciones (lo que creemos que significan), y evitar el lenguaje que culpa o elogia a un sector político sin evidencia. Al comunicar, el título debe ser fiel al dato: un título que exagera confunde a quien lee. Las tablas y los gráficos ayudan si se rotulan con fuente, año y unidad. Cuando se comparan dos porcentajes, la diferencia se expresa en puntos porcentuales: de 6 % a 10 % hay 4 puntos porcentuales.',
    ],
    vocab=[("conclusión situada", "conclusión que indica el lugar, el tiempo y los datos a los que se refiere"), ("evidencia", "dato o fuente que respalda una afirmación"), ("matiz", "precisión que limita o completa una afirmación"), ("generalizar", "extender lo observado en pocos casos a todos los casos"), ("hecho e interpretación", "el hecho es lo que muestran los datos; la interpretación es lo que creemos que significan")],
    worked=[
        ("Reconocer una generalización", "Con datos de dos países en un año, un texto dice «en toda la región la desigualdad baja». ¿Qué falla?", ["Los datos son de dos países y un año.", "La afirmación se extiende a toda la región sin respaldo."], "Generaliza más allá de los datos"),
        ("Armar una conclusión", "Con datos de ejemplo: el país P tiene 8 % de desempleo y el país Q 5 %. ¿Cómo se redacta con prudencia?", ["Se afirma lo que muestran los datos.", "Se añade un límite: son datos de un solo año."], "En estos datos, P tiene más desempleo que Q; falta saber las causas"),
    ],
    mistakes=[("Escribir conclusiones sobre toda la región con datos de dos casos.", "Se pierde la precisión y se puede inducir a error.", "Indica siempre lugar, año y fuente de los datos."),
              ("Mezclar el dato con una opinión sin avisar.", "El lector no distingue qué es hecho y qué es interpretación.", "Escribe primero la cifra y después, aparte, tu interpretación.")],
    T=[
        ('¿Qué hace situada a una conclusión sobre un desafío económico?', 'La que indica lugar, tiempo y datos de referencia', 'La que se escribe antes de mirar los datos', 'La que se aplica sin cambios a todos los países', 'Situar es acotar la conclusión a su contexto; no es adelantarla ni extenderla a todo.'),
        ('¿Qué es generalizar con pocos datos?', 'Extender lo observado en pocos casos a todos los casos', 'Comparar los casos con una fuente confiable y actualizada', 'Dividir los casos en grupos para estudiarlos por separado', 'Generalizar es dar por válido para todos lo que solo se vio en pocos casos.'),
        ('¿Qué es un matiz en una conclusión?', 'Una precisión que limita o completa lo que se afirma', 'Una opinión que reemplaza la evidencia', 'Un dato que se agrega solo para llenar espacio', 'El matiz señala límites o condiciones de la afirmación.'),
        ('=', '{F} ¿Cuántos puntos porcentuales más creció el PIB de Tierra Fértil que el de Mar Azul?', '10-4', 'Se resta el crecimiento de Mar Azul al de Tierra Fértil.', ' puntos porcentuales'),
        ('=', '{F} ¿Cuántos puntos porcentuales más de desempleo tiene Tierra Fértil que Mar Azul?', '10-6', 'Se resta el desempleo de Mar Azul al de Tierra Fértil.', ' puntos porcentuales'),
        ('=', '{F} El 20 % más rico recibe 10 veces lo que el 20 % más pobre en Tierra Fértil y 6 veces en Mar Azul. ¿Cuántas veces de diferencia hay entre esas dos cifras?', '10-6', 'Se resta la razón de Mar Azul a la de Tierra Fértil.', ' veces de diferencia'),
        ('{F} ¿Qué afirmación está respaldada por los datos?', 'En estos datos, Mar Azul tiene menos desempleo y menos diferencia entre ricos y pobres', 'Mar Azul es un mejor país para vivir que Tierra Fértil en todos los aspectos', 'Las diferencias entre los dos países se deben a la política económica de cada gobierno', 'Solo la primera se apoya en cifras de la ficha; las otras agregan juicios y causas que no se conocen.'),
        ('{F} ¿Qué dice la nota de la ficha sobre los límites de los datos?', 'Son datos de un solo año y no se conocen las causas', 'Son datos de diez años que prueban las causas', 'Son datos de toda la región latinoamericana completa', 'La nota advierte que los datos son de un año y que las causas no se conocen.'),
        ('{F} Un título dice: «Tierra Fértil crece más, por eso es más justo». ¿Qué falla?', 'Salta del crecimiento económico a un juicio sobre justicia', 'Está bien, porque más crecimiento significa más justicia', 'Está bien, porque el título repite el dato de desempleo', 'Crecer más no prueba mayor justicia; de hecho, la ficha muestra más diferencia entre ricos y pobres.'),
        ('{F} ¿Cuál es la mejor redacción de la parte de «límite»?', 'Son datos de un solo año y no explican las causas', 'Los datos prueban que Mar Azul aplica mejores políticas económicas que Tierra Fértil', 'Los datos demuestran lo que pasa en toda la región latinoamericana y en el mundo', 'El límite dice lo que los datos no permiten afirmar.'),
        ('{F} Alguien afirma: «La desigualdad es más alta en los países que crecen más». ¿Qué respuesta es más prudente?', 'Con solo dos países y un año no se puede afirmar una regla general', 'Es cierto, porque en la ficha crece más el país más desigual', 'Es falso, porque ningún país que crece tiene desigualdad', 'Dos casos no bastan para afirmar una regla general, aunque coincidan.'),
        ('{F} ¿Qué propuesta final es coherente con una conclusión prudente?', 'Reunir más datos de varios años antes de sacar una regla', 'Aplicar en Tierra Fértil la política de Mar Azul de inmediato y sin estudiarla', 'Concluir que no vale la pena seguir investigando las diferencias entre ambos países', 'Una propuesta prudente amplía datos antes de generalizar o copiar políticas.'),
        ('Un estudiante escribe: «Según los datos de ejemplo, en un año Mar Azul tiene menos desempleo que Tierra Fértil». ¿Qué cualidad tiene su frase?', 'Está situada: indica fuente, año y alcance', 'Es una generalización a toda la región latinoamericana', 'Es una opinión política que no se apoya en datos', 'Menciona dónde, cuándo y sobre qué datos se afirma.'),
    ],
    ctx=('En un afiche escolar se muestra un gráfico con el desempleo de dos países de ejemplo, sin año ni fuente. ¿Qué falta para que sea una comunicación responsable?', 'Indicar el año, la fuente y la unidad de los datos', 'Agregar un título más grande y llamativo en colores fuertes', 'Quitar los números para que no se discutan', 'Sin año, fuente y unidad, el gráfico no se puede verificar.'),
    sc=[
        ('Nombra las cuatro partes de una buena conclusión situada.', 'Afirmación, evidencia, límite y propuesta', 'Son las partes que permiten afirmar con respaldo, matizar y seguir investigando.'),
        ('¿Por qué conviene usar palabras como «parece» o «en estos datos»?', 'Porque indican el alcance real de la afirmación', 'La prudencia en el lenguaje es precisión, no debilidad.'),
        ('¿Qué diferencia hay entre un hecho y una interpretación?', 'El hecho es lo que muestran los datos; la interpretación es lo que creemos que significan', 'Conviene presentar primero el hecho y después la interpretación.'),
    ],
    op=("Usa la {F} Escribe una conclusión de seis líneas con las cuatro partes (afirmación, evidencia, límite y propuesta) sobre la comparación de Tierra Fértil y Mar Azul. Usa al menos una expresión de prudencia y evita juicios políticos.",
        "Afirmación: en estos datos, Mar Azul tiene menos desempleo y menos diferencia de ingresos que Tierra Fértil. Evidencia: 6 % frente a 10 % de desempleo, y 6 veces frente a 10 veces entre el 20 % más rico y el más pobre. Matiz: Tierra Fértil creció más, 10 % frente a 4 %. Límite: son datos de un año y no se conocen las causas. Propuesta: reunir datos de varios años y estudiar qué políticas aplicó cada país.",
        ["incluye las cuatro partes", "usa cifras de la ficha", "evita juicios políticos"], ["conclusión de seis líneas"], ["generalizar a toda la región", "mezclar hechos con opiniones"],
        "Revisa que cada afirmación tenga su cifra y que el límite sea honesto."),
    rx=("Reescribe una frase exagerada de un titular imaginario para hacerla más prudente.", "Muestra tu conclusión a alguien de tu casa y anota si entendió cuál era la evidencia."),
)
