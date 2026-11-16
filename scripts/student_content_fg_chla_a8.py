"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 05 clases 1 a 3 (medioambiente y sustentabilidad: conceptos y actividades humanas, indicadores y fuentes, causas y perspectivas). Datos y lugares de ejemplo inventados."""
from __future__ import annotations

from fg_chla_common import build

O5 = "FG-CHLA-3y4-OAC-05"

# ============================================================ OA 05, clase 1
F = ("Ficha 1 (región ficticia de ejemplo, Cuenca del Río Claro). Hay cuatro actividades principales: agricultura de riego con agua del río, una mina de cobre ficticia, una ciudad que usa leña y vehículos, y un bosque nativo con un parque protegido. "
     "En los últimos años llueve menos y el caudal del río ha bajado. Una empresa eléctrica estudia instalar paneles solares en una zona desértica. Las comunidades de la cuenca, el municipio, el Estado y las empresas participan en una mesa del agua.")
build(
    O5, 1, F,
    use="Aprenderé a describir el estado del medioambiente de Chile y América Latina, reconociendo las actividades humanas que lo afectan, sus actores y la idea de sustentabilidad.",
    explain=[
        'El medioambiente es el conjunto de elementos naturales (agua, aire, suelo, plantas y animales) y sociales con los que viven las personas. Los recursos naturales son elementos de la naturaleza que usamos: los renovables, como el agua y los bosques, pueden recuperarse si se usan con cuidado; los no renovables, como los minerales, no se regeneran en un tiempo humano. La biodiversidad es la variedad de seres vivos de un lugar. Las actividades humanas, como la agricultura, la minería, la energía, la pesca, la industria y las ciudades, usan recursos y pueden producir contaminación o pérdida de ecosistemas.',
        'La sustentabilidad consiste en satisfacer las necesidades de hoy sin comprometer las de las generaciones futuras; considera a la vez lo ambiental, lo económico y lo social. Para analizar un problema ambiental conviene ubicar actores (comunidades, empresas, Estado, científicos), tiempo (desde cuándo ocurre) y espacio y escala (una cuenca, un país o el planeta). América Latina tiene una gran biodiversidad y también desafíos: contaminación del aire en ciudades, escasez de agua en algunas zonas y pérdida de bosques, entre otros. La situación varía mucho entre lugares.',
    ],
    vocab=[("medioambiente", "conjunto de elementos naturales y sociales con los que viven las personas"), ("recurso renovable", "recurso que se recupera si se usa con cuidado, como el agua o los bosques"), ("recurso no renovable", "recurso que no se regenera en un tiempo humano, como un mineral"), ("biodiversidad", "variedad de seres vivos de un lugar"), ("sustentabilidad", "satisfacer las necesidades de hoy sin comprometer las de las generaciones futuras"), ("cuenca", "territorio cuyas aguas desembocan en un mismo río o lago")],
    worked=[
        ("Clasificar recursos", "En una región de ejemplo se usa agua de un río, madera de un bosque y cobre de una mina. ¿Cuáles son renovables?", ["El agua y el bosque pueden recuperarse si se manejan bien.", "El mineral no se regenera en un tiempo humano."], "Agua y bosque; el cobre es no renovable"),
        ("Aplicar sustentabilidad", "Una comunidad de ejemplo tala todos los árboles de un bosque para vender madera en un año. ¿Es sustentable?", ["Satisface una necesidad actual.", "Compromete el recurso para el futuro, así que no es sustentable."], "No es sustentable"),
    ],
    mistakes=[("Creer que sustentabilidad es solo proteger la naturaleza.", "Incluye también lo económico y lo social.", "Considera las tres dimensiones: ambiental, económica y social."),
              ("Pensar que cualquier recurso renovable es inagotable.", "Se agota si se usa más rápido de lo que se recupera.", "Compara el ritmo de uso con el ritmo de recuperación.")],
    T=[
        ('¿Qué es un recurso renovable?', 'Uno que se recupera si se usa con cuidado y sin exceso', 'Uno que no se agota aunque se use sin cuidado', 'Uno que solo se encuentra en zonas de desierto', 'Renovable no significa inagotable: depende de que el uso no supere su recuperación.'),
        ('¿Qué es la biodiversidad?', 'La variedad de seres vivos que habitan un lugar', 'La cantidad de agua que fluye por un río', 'Las actividades económicas de una región', 'La biodiversidad se refiere a la variedad de plantas, animales y otros seres vivos.'),
        ('¿Qué es la sustentabilidad?', 'Satisfacer las necesidades de hoy sin comprometer el futuro', 'Producir lo más posible hoy aunque se agoten los recursos', 'Dejar de usar todos los recursos naturales del lugar', 'La sustentabilidad busca equilibrio entre presente y futuro, no el uso total ni el no uso.'),
        ('{F} ¿Cuál de estas actividades de la ficha usa un recurso no renovable?', 'La mina de cobre', 'La agricultura de riego', 'Los paneles solares', 'El cobre es un mineral que no se regenera; el agua del río y el sol son renovables.'),
        ('{F} ¿Qué cambio reciente muestra la ficha respecto del agua?', 'Llueve menos y el caudal del río ha bajado', 'Llueve más y el caudal del río ha subido', 'El caudal del río no ha cambiado en los últimos años', 'La ficha indica menos lluvia y menor caudal.'),
        ('{F} ¿Qué actor estudia instalar paneles solares?', 'Una empresa eléctrica', 'Las comunidades de la cuenca', 'El municipio', 'La ficha dice que una empresa eléctrica estudia instalarlos.'),
        ('{F} ¿Qué actividad de la ficha puede afectar la calidad del aire de la ciudad?', 'El uso de leña y de vehículos en la ciudad', 'La instalación de paneles solares', 'La existencia del parque protegido', 'Quemar leña y usar vehículos emite contaminantes al aire.'),
        ('{F} ¿Qué espacio y escala corresponde a este caso?', 'Una cuenca, es decir, una escala regional', 'El planeta completo, escala global', 'Una sola vivienda, escala individual', 'La ficha se ubica en la Cuenca del Río Claro, una escala regional.'),
        ('{F} ¿Por qué el bosque nativo con parque protegido aporta a la sustentabilidad?', 'Porque conserva biodiversidad y ayuda a mantener el agua', 'Porque produce madera para vender en un solo año', 'Porque impide cualquier uso del territorio por las comunidades', 'Un bosque protegido conserva especies y contribuye a los ciclos del agua.'),
        ('{F} Alguien dice: «La sequía del río solo se debe a la agricultura». ¿Qué respuesta es más precisa?', 'Hay menos lluvia y varios usos del agua; no es un solo factor', 'Es cierto, porque la agricultura es la única actividad que usa agua', 'No es posible, porque la agricultura no usa agua del río', 'La ficha menciona menos lluvia y varios usos del agua; atribuir todo a un solo factor sin datos es una simplificación.'),
        ('{F} ¿Por qué la mesa del agua es relevante para la sustentabilidad?', 'Porque reúne actores distintos para decidir el uso del agua', 'Porque asegura que solo la mina podrá usar el agua en toda la cuenca del río', 'Porque elimina la necesidad de estudiar el caudal del río y la lluvia', 'Una mesa con varios actores ayuda a equilibrar usos presentes y futuros.'),
        ('Una empresa de ejemplo propone talar un bosque y replantar la misma cantidad de árboles en 10 años. ¿Qué pregunta de sustentabilidad se debe hacer?', '¿Se recupera el bosque al ritmo de uso y se protege la biodiversidad?', '¿Cuánto dinero ganará la empresa con la venta de la madera?', '¿Cuántos camiones harán falta para transportar la madera?', 'La sustentabilidad exige comparar el uso con la capacidad de recuperación y los efectos en la biodiversidad.'),
        ('{F} Si la empresa eléctrica instala los paneles sin hablar con las comunidades cercanas, ¿qué dimensión de la sustentabilidad se descuida?', 'La social, porque no se considera a los afectados', 'La ambiental, porque los paneles dañan siempre el aire de la zona cercana', 'La económica, porque los paneles nunca generan energía eléctrica útil', 'Aunque la energía solar sea renovable, el proyecto debe considerar a las comunidades.'),
    ],
    ctx=('Una ciudad de ejemplo consume cada año más agua de la que su río recupera con la lluvia. ¿Qué se puede decir sobre su uso del recurso?', 'No es sustentable: usa más de lo que el río recupera', 'Es sustentable, porque el agua es siempre un recurso renovable y se repone sola', 'Es sustentable, porque la ciudad tiene muchos habitantes y mucha demanda', 'Un recurso renovable deja de serlo si se consume más rápido de lo que se recupera.'),
    sc=[
        ('En Chile y la región, ¿qué diferencia hay entre recurso renovable y no renovable?', 'El renovable se recupera con buen manejo; el no renovable no se regenera en tiempo humano', 'El agua y los bosques son renovables; los minerales no lo son.'),
        ('Nombra las tres dimensiones de la sustentabilidad.', 'Ambiental, económica y social', 'La sustentabilidad considera esas tres dimensiones a la vez.'),
        ('¿Qué es una cuenca?', 'Un territorio cuyas aguas desembocan en un mismo río o lago', 'Es una unidad geográfica útil para analizar el uso del agua.'),
    ],
    op=("Usa la {F} Escribe un párrafo de cinco oraciones: nombra tres actividades humanas de la cuenca y el recurso que usa cada una; distingue un recurso renovable de uno no renovable; señala un cambio reciente; indica un actor y qué dimensión de la sustentabilidad le corresponde cuidar.",
        "En la cuenca hay agricultura de riego (agua), minería (cobre) y una ciudad (leña y vehículos). El agua es renovable y el cobre no. Un cambio reciente es que llueve menos y el caudal bajó. El municipio es un actor y debe cuidar la dimensión social, atendiendo el acceso al agua. La mesa del agua ayuda a equilibrar los usos.",
        ["nombra tres actividades con sus recursos", "distingue renovable de no renovable", "relaciona un actor con una dimensión"], ["párrafo de cinco oraciones"], ["confundir renovable con inagotable", "usar datos que no están en la ficha"],
        "Revisa que cada afirmación se apoye en una frase de la ficha."),
    rx=("Explica con un ejemplo por qué un recurso renovable puede agotarse.", "Observa tu comuna y anota una actividad que use un recurso natural y otra que lo cuide."),
)

# ============================================================ OA 05, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados; ciudad ficticia de Aire Norte y región ficticia de Cuenca del Río Claro). "
     "Aire: promedio anual de partículas finas en el aire de la ciudad: 35 unidades; el límite de la norma de ejemplo es 20 unidades. "
     "Bosque nativo: 800 mil hectáreas en el año 1 y 760 mil hectáreas en el año 2. Áreas protegidas: 150 mil de las 1.000 mil hectáreas de la cuenca. "
     "Fuentes: las mediciones del aire vienen de 4 estaciones fijas, ninguna en la zona de la periferia; el dato del bosque viene de imágenes de satélite y de un estudio de una universidad; "
     "la cifra de áreas protegidas viene de un informe de un ministerio.")
build(
    O5, 2, F,
    use="Aprenderé a leer y calcular indicadores ambientales, como la calidad del aire, la superficie de bosque y las áreas protegidas, y a interrogar las fuentes que los entregan.",
    explain=[
        'Los indicadores ambientales resumen el estado del medioambiente. Algunos ejemplos son la concentración de partículas en el aire (que se compara con una norma), la superficie de bosque nativo, la disponibilidad de agua y el porcentaje del territorio protegido. Un porcentaje se calcula dividiendo la parte por el total y multiplicando por 100. Una variación se calcula restando el valor inicial al final; si es negativa, hubo disminución.',
        'Las fuentes son estaciones de monitoreo, imágenes de satélite, estudios de universidades, informes de ministerios, organizaciones de la sociedad civil y relatos de las comunidades. Cada una se interroga: ¿qué mide?, ¿dónde y cuándo?, ¿con qué método?, ¿qué deja fuera? Por ejemplo, si todas las estaciones de aire están en el centro, los datos pueden no representar a la periferia. Los datos de ejemplo de esta ficha son inventados y no describen a ninguna ciudad real.',
    ],
    vocab=[("indicador ambiental", "dato que resume el estado de un aspecto del medioambiente"), ("norma", "límite o regla fijada por la ley para proteger algo, por ejemplo la calidad del aire"), ("monitoreo", "medición periódica de una variable"), ("área protegida", "territorio resguardado por la ley para conservar su naturaleza"), ("variación", "diferencia entre un valor final y uno inicial")],
    worked=[
        ("Comparar con la norma", "En una ciudad de ejemplo, la medición es 30 y la norma es 25. ¿Cuántas unidades excede?", ["Se resta la norma a la medición.", "30 − 25 = 5."], "Excede en 5 unidades"),
        ("Calcular la variación", "Un bosque de ejemplo pasa de 500 a 450 mil hectáreas. ¿Cuál es la variación?", ["Se resta el valor inicial al final.", "450 − 500 da −50."], "−50 mil hectáreas (disminución)"),
    ],
    mistakes=[("Tomar la medición de una estación como la de toda la ciudad.", "Una estación mide solo su zona.", "Revisa dónde están las estaciones y qué zonas quedan sin medir."),
              ("Confundir la variación con el porcentaje de variación.", "La primera es una diferencia absoluta; el porcentaje la compara con el valor inicial.", "Calcula primero la diferencia y luego, si piden porcentaje, divide por el valor inicial.")],
    T=[
        ('¿Qué es una norma ambiental?', 'Un límite fijado por ley para proteger, como el del aire', 'Una opinión de una organización social', 'Una medición hecha por una estación en un solo día', 'La norma es un límite legal con el que se comparan las mediciones.'),
        ('¿Qué es el monitoreo ambiental?', 'La medición periódica de una variable, como el aire', 'La decisión de cerrar una actividad productiva', 'El reparto del agua entre los usos de una cuenca', 'Monitorear es medir con regularidad para seguir cambios.'),
        ('¿Qué es un área protegida?', 'Un territorio resguardado por ley para conservar su naturaleza', 'Un territorio donde está prohibido que viva cualquier persona o comunidad', 'Un territorio donde solo se pueden realizar actividades mineras o industriales', 'Las áreas protegidas buscan conservar naturaleza y regulan los usos, no impiden todo uso humano.'),
        ('=', '{F} ¿Cuántas unidades por sobre la norma está el promedio anual de partículas del aire?', '35-20', 'Se resta la norma a la medición.', ' unidades'),
        ('=', '{F} ¿Cuál es la variación de la superficie de bosque nativo entre el año 1 y el año 2 (en miles de hectáreas)?', '760-800', 'Se resta el valor inicial al final; el resultado negativo indica disminución.', ' mil hectáreas'),
        ('=', '{F} ¿Qué porcentaje de la cuenca es área protegida?', '150*100//1000', 'Se divide la superficie protegida por la total y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje del bosque del año 1 se perdió hasta el año 2 (40 mil de 800 mil)?', '40*100//800', 'Se divide la pérdida por la superficie inicial y se multiplica por 100.', ' %'),
        ('{F} ¿Qué limitación tiene la medición del aire de la ficha?', 'Ninguna de las 4 estaciones está en la zona de la periferia', 'Hay demasiadas estaciones para una ciudad pequeña', 'Se midió el aire solo en el interior de las casas', 'La ficha dice que ninguna estación está en la periferia, por lo que esa zona puede no estar representada.'),
        ('{F} ¿Qué tipo de fuente es el estudio de una universidad junto a imágenes de satélite?', 'Una fuente científica que mide la superficie del bosque', 'Una fuente oficial que fija la norma del aire', 'Una opinión personal sin datos ni método', 'Combina imágenes y análisis para medir el bosque; no fija normas ni es una opinión.'),
        ('{F} Un diario afirma: «El aire de toda la ciudad está dentro de la norma». ¿Qué corresponde decir?', 'Falso en estos datos: el promedio supera la norma', 'Verdadero, porque 35 es menor que 20', 'No se puede saber, porque 35 y 20 no se pueden comparar', 'Con la norma en 20 y el promedio en 35, el promedio excede el límite.'),
        ('{F} ¿Qué se puede afirmar sobre el bosque nativo con estos datos?', 'Disminuyó, pero no se conoce la causa', 'Aumentó, porque ambos años tienen cifras en miles de hectáreas medidas', 'Disminuyó por causa de la agricultura de riego de toda la cuenca', 'Los datos muestran la disminución, pero no explican por qué ocurrió.'),
        ('{F} Un ministerio dice: «La cuenca está bien protegida porque tiene 15 % de áreas protegidas». ¿Qué falta para evaluarlo?', 'Qué se protege y si la protección se cumple en la práctica', 'Nada, porque 15 % siempre es una cifra suficiente para proteger una cuenca', 'Solo el nombre de la persona que firmó el informe del ministerio', 'El porcentaje es una cifra de superficie; la calidad de la protección requiere más información.'),
        ('{F} Para evaluar mejor el aire de la periferia, ¿qué sería útil?', 'Instalar una estación de medición en la periferia', 'Quitar las estaciones de la zona central de la ciudad', 'Usar solo el promedio de los últimos cinco días', 'Más puntos de medición permiten conocer la calidad del aire donde hoy no hay datos.'),
    ],
    ctx=('En una ciudad de ejemplo la norma de partículas es 25 y se miden 40 unidades. ¿Cuántas unidades por sobre la norma y qué porcentaje de la norma es ese exceso?', '15 unidades, que es 60 % de la norma', '15 unidades, que es 15 % de la norma', '65 unidades, que es 160 % de la norma', 'El exceso es 40 − 25 = 15 y 15 ÷ 25 × 100 = 60.'),
    sc=[
        ('Nombra dos fuentes para conocer el estado del medioambiente.', 'Por ejemplo, estaciones de monitoreo e imágenes de satélite', 'También sirven estudios de universidades e informes de ministerios.'),
        ('=', 'Un bosque de ejemplo pasa de 600 a 570 mil hectáreas. ¿Cuántas mil hectáreas se perdieron?', '600-570', 'Se resta la superficie final a la inicial.', ' mil hectáreas'),
        ('¿Por qué importa saber dónde están las estaciones de medición?', 'Porque pueden no representar las zonas sin estación', 'Una estación mide solo su entorno.'),
    ],
    op=("Usa la {F} Escribe un informe de cinco oraciones: aire frente a la norma (con el exceso), variación del bosque (con el porcentaje), porcentaje de área protegida, un límite de las fuentes y una pregunta para investigar las causas. No inventes datos.",
        "El promedio de partículas es 35 y la norma 20: excede en 15 unidades. El bosque pasó de 800 a 760 mil hectáreas, una pérdida de 5 %. El 15 % de la cuenca es área protegida. Ninguna estación de aire está en la periferia. Pregunta: ¿qué actividades explican la pérdida de bosque entre el año 1 y el año 2?",
        ["calcula tres indicadores", "menciona un límite de fuente", "formula una pregunta de causa"], ["informe de cinco oraciones"], ["afirmar causas sin datos", "no mencionar el límite"],
        "Revisa si cada cifra tiene unidad y fuente."),
    rx=("Calcula un porcentaje de bosque perdido con cifras inventadas.", "Busca con tu docente dónde se publican mediciones de aire o de agua de tu zona y anota el nombre de la fuente."),
)

# ============================================================ OA 05, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado; Cuenca del Río Claro). Cuatro voces hablan del problema del agua y del aire. "
     "Voz 1, una agricultora: sin agua de riego no se puede producir alimentos, y el riego ya está tecnificado. "
     "Voz 2, un ingeniero de la mina: la mina da empleo y trabaja para usar menos agua por tonelada, pero necesita agua para funcionar. "
     "Voz 3, un vecino de la ciudad: en invierno el humo de la leña hace difícil respirar y mucha gente la usa porque calefaccionar de otro modo es caro. "
     "Voz 4, una científica: llueve menos y las actividades usan más agua de la que el río recupera; hay que ajustar los usos.")
build(
    O5, 3, F,
    use="Aprenderé a comparar causas y perspectivas de distintos actores frente a problemas ambientales, reconociendo que la sustentabilidad busca equilibrar lo ambiental, lo económico y lo social.",
    explain=[
        'Los problemas ambientales tienen causas naturales y humanas que se combinan. Por ejemplo, una sequía puede depender de que llueve menos y también de cuánta agua usan las actividades. La contaminación del aire en invierno puede relacionarse con la calefacción a leña, el tránsito de vehículos y el clima del lugar. Para comprender un problema hay que preguntar qué causas son más importantes, con qué evidencia y qué actores pueden actuar sobre cada una.',
        'Los actores miran el problema desde su lugar: quienes producen defienden su actividad y su empleo; las comunidades, su acceso al agua y a un aire limpio; los científicos, la evidencia; el Estado, el equilibrio entre intereses y la ley. Estas perspectivas pueden tener puntos en común: casi todos quieren agua y aire para el futuro. Una buena comparación identifica quién habla, qué necesita y qué evidencia presenta, y no se queda con la perspectiva que más conviene. La sustentabilidad busca equilibrar las necesidades, no eliminar ninguna.',
    ],
    vocab=[("causa natural", "causa que no depende de las personas, como el clima"), ("causa humana", "causa que depende de actividades de las personas"), ("perspectiva", "punto de vista de un actor según su lugar y sus necesidades"), ("equilibrar", "buscar un punto intermedio que atienda varias necesidades"), ("evidencia", "dato o fuente que respalda una afirmación")],
    worked=[
        ("Separar causas", "En una zona de ejemplo baja el caudal de un río porque llueve menos y porque aumenta el riego. ¿Qué causa es natural y cuál humana?", ["Llover menos depende del clima: es natural.", "El aumento del riego depende de las personas: es humana."], "Natural: menos lluvia. Humana: más riego"),
        ("Encontrar un punto en común", "Un agricultor y una científica de ejemplo discuten sobre el río. Ambos quieren que el agua alcance en el futuro. ¿Qué coincidencia hay?", ["Los dos desean agua para el futuro.", "Esa coincidencia puede ser base de un acuerdo."], "Quieren que el agua no se agote"),
    ],
    mistakes=[("Culpar a un solo actor sin evidencia.", "Los problemas ambientales suelen tener varias causas y varios actores.", "Pregunta qué datos muestran la contribución de cada actor."),
              ("Descartar la perspectiva de quien produce o de quien contamina.", "Todas las perspectivas aportan información sobre necesidades y límites.", "Escucha todas y contrástalas con evidencia.")],
    T=[
        ('¿Qué es una causa natural de un problema ambiental?', 'Una que no depende de las personas, como el clima o la lluvia', 'Una que depende de las decisiones de una empresa', 'Una que se produce solo por actividades de la ciudad', 'Las causas naturales ocurren sin intervención humana directa.'),
        ('¿Qué significa equilibrar necesidades en sustentabilidad?', 'Atender a la vez necesidades ambientales, económicas y sociales', 'Atender solo la necesidad más urgente de las empresas de la región', 'Eliminar todas las actividades económicas que usen recursos naturales', 'Equilibrar es compatibilizar varias necesidades sin sacrificar del todo ninguna.'),
        ('¿Qué es la evidencia en un debate ambiental?', 'Datos o fuentes que respaldan una afirmación', 'La opinión más repetida entre los participantes', 'La postura de quien tiene el cargo más alto', 'La evidencia respalda lo que se dice; la repetición o el cargo no.'),
        ('{F} ¿Qué prioridad plantea la Voz 1?', 'Mantener agua de riego para producir alimentos', 'Cerrar la mina por completo para cuidar el agua', 'Prohibir el uso de leña en todas las viviendas', 'La agricultora defiende el agua de riego para la producción de alimentos.'),
        ('{F} ¿Qué reconoce la Voz 2 sobre el uso del agua?', 'Que la mina necesita agua, aunque busca usar menos', 'Que la mina no usa agua para funcionar', 'Que la mina no tiene relación con el empleo', 'El ingeniero reconoce la necesidad de agua y el esfuerzo por reducir su uso.'),
        ('{F} ¿Por qué mucha gente usa leña, según la Voz 3?', 'Porque calefaccionar de otro modo es caro', 'Porque la leña no produce humo ni contaminación', 'Porque la ciudad no tiene ningún acceso a otro combustible', 'El vecino explica que la alternativa es más cara, no que la leña no contamine.'),
        ('{F} ¿Qué causas menciona la Voz 4 para el problema del agua?', 'Menos lluvia y más usos que lo que recupera el río', 'Solo el aumento de las temperaturas en verano', 'Únicamente el uso del agua de los hogares', 'La científica combina una causa natural y una humana.'),
        ('{F} ¿En qué coinciden las Voces 1 y 2?', 'Ambas necesitan agua para sostener su actividad', 'Ambas piden eliminar el uso de leña', 'Ambas niegan que haya problemas de agua', 'La agricultora y el ingeniero dependen del agua para trabajar.'),
        ('{F} ¿Qué relación hay entre la Voz 3 y la calidad del aire?', 'El humo de la leña dificulta respirar en invierno', 'El humo de la leña mejora la calidad del aire en invierno', 'La leña no tiene relación alguna con el aire de la ciudad', 'El vecino relaciona la leña con dificultad para respirar.'),
        ('{F} Alguien afirma: «La sequía se debe solo a la mina». ¿Qué corrección es más precisa?', 'Hay menos lluvia y varios usos del agua, no solo la mina', 'Es verdad, porque la mina es el único actor que usa agua', 'Es falso, porque la mina no usa agua del río', 'Hay causas naturales y de varios usos; atribuirlo solo a la mina carece de evidencia.'),
        ('{F} ¿Qué medida atiende a la vez la Voz 3 y la calidad del aire?', 'Subsidiar el cambio a una calefacción menos contaminante', 'Prohibir la calefacción en las viviendas durante todo el invierno', 'Aumentar el precio de todas las formas de calefacción disponibles', 'Un subsidio reduce el costo para las familias y baja la contaminación.'),
        ('{F} ¿Cómo se podría equilibrar la Voz 1, la Voz 2 y la Voz 4?', 'Ajustar los usos del agua a lo que el río recupera', 'Dar toda el agua a la actividad que más empleo dé', 'Esperar a que llueva más sin tomar ninguna medida', 'La Voz 4 propone ajustar usos; con datos compartidos se pueden repartir cargas.'),
        ('{F} Para comparar bien estas cuatro voces, ¿qué conviene hacer?', 'Identificar quién habla, qué necesita y qué evidencia presenta', 'Elegir la voz que coincide con lo que uno piensa', 'Descartar las voces de quienes obtienen ganancias de la actividad', 'Todas las voces aportan información, pero se contrastan con evidencia.'),
    ],
    ctx=('En un pueblo de ejemplo, una fábrica emplea a muchas personas y vierte desechos a un río donde pesca la comunidad. ¿Qué enfoque de sustentabilidad es el más adecuado?', 'Reducir los desechos y mantener el empleo', 'Cerrar la fábrica de inmediato sin considerar a quienes trabajan en ella', 'Permitir los desechos para proteger los empleos sin ningún límite', 'La sustentabilidad busca compatibilizar lo ambiental, lo económico y lo social.'),
    sc=[
        ('Nombra una causa natural y una humana de la escasez de agua.', 'Natural: menos lluvia; humana: más usos del agua', 'Ambas pueden combinarse en un mismo problema.'),
        ('¿Por qué conviene escuchar a todos los actores?', 'Porque cada uno aporta una parte de la información y de las necesidades', 'La comparación con evidencia permite una decisión más justa.'),
        ('¿Qué significa buscar puntos en común entre perspectivas distintas?', 'Encontrar objetivos compartidos que permitan acordar', 'Muchos actores comparten el interés por un futuro con agua y aire limpios.'),
    ],
    op=("Usa la {F} Arma un cuadro con las cuatro voces: qué necesita cada una, qué causa destaca y qué evidencia pedirías. Cierra con una propuesta de dos oraciones que atienda a más de un actor.",
        "Voz 1: agua de riego; evidencia: caudal que necesita. Voz 2: empleo y agua; evidencia: agua por tonelada. Voz 3: aire respirable y calefacción accesible; evidencia: mediciones de partículas en invierno. Voz 4: ajustar usos; evidencia: balance entre lluvia y consumo. Propuesta: acordar en la mesa del agua una meta de uso según lo que el río recupera y apoyar con subsidios la calefacción menos contaminante.",
        ["resume cada voz", "propone evidencia posible", "propone algo que atiende a varios actores"], ["cuadro de cuatro filas", "propuesta de dos oraciones"], ["culpar a un solo actor", "no pedir evidencia"],
        "Revisa si tu propuesta toma en cuenta lo ambiental, lo económico y lo social."),
    rx=("Explica con tus palabras por qué la sustentabilidad busca equilibrar necesidades.", "Conversa con una persona de tu casa sobre un problema ambiental de tu comuna y anota una causa que mencione."),
)
