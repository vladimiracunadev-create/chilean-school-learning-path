"""Biología de los ecosistemas (electivo 3.º y 4.º medio HC): OAC-03 (efectos del cambio climático, clases 1 a 4) y OAC-04 (prevenir, mitigar o reparar, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado: no necesitas salida a terreno, laboratorio ni internet. "
             "Este cuaderno no propone plantar, intervenir ni recolectar en ecosistemas reales: las acciones de restauración y protección se analizan sobre casos ya descritos. Si quieres participar en una actividad real, hazlo con una organización o un establecimiento que cuente con autorización y supervisión adulta. "
             "Las cifras son inventadas para practicar el razonamiento y no describen un lugar real; las fechas se dan solo cuando son bien conocidas.")
build = make_build(MATERIALS)

O3 = "CN-BECO-3y4-OAC-03"
O4 = "CN-BECO-3y4-OAC-04"

# ============================================================ OAC-03, clase 1
F = ("Ficha 10 (hechos de ejemplo). Hecho 1: el vapor de agua, el dióxido de carbono, el metano y el óxido nitroso absorben parte de la energía que emite la superficie terrestre y devuelven una parte hacia ella (efecto invernadero natural). "
     "Hecho 2: la quema de combustibles fósiles, la agricultura y la pérdida de bosques aumentan la cantidad de estos gases en la atmósfera. "
     "Hecho 3: en una ciudad ficticia, un 12 de julio la temperatura mínima fue de −2 °C y se registró una helada. "
     "Hecho 4: en la misma región ficticia, el promedio de la temperatura de cada década, calculado con datos de muchos años, fue subiendo de una década a la siguiente.")
build(
    O3, 1, F,
    use="Aprenderé a delimitar qué es el cambio climático y a diferenciarlo del tiempo atmosférico, para formular preguntas sobre sus efectos en los ecosistemas. Sirve para no confundir un día frío o caluroso con una tendencia de décadas.",
    prior=["Sé qué es un ecosistema y qué es la atmósfera.", "Sé calcular promedios.", "Sé leer una serie de datos en el tiempo."],
    explain=[
        "El tiempo atmosférico es el estado de la atmósfera en un lugar y un momento: si hoy llueve o hace frío. El clima es el promedio de esas condiciones durante muchos años, por lo general treinta o más. Por eso un día muy frío no contradice que el clima de una región se esté calentando: son escalas de tiempo distintas.",
        "El efecto invernadero natural es necesario para la vida, porque mantiene la superficie terrestre más cálida de lo que sería sin esos gases. El cambio climático actual ocurre porque las actividades humanas, como quemar combustibles fósiles, ciertas prácticas agrícolas y la pérdida de bosques, aumentan la cantidad de gases de efecto invernadero, y así intensifican ese efecto. El resultado es un calentamiento global y cambios en las lluvias y en los extremos del clima.",
        "Para estudiar sus efectos sobre los ecosistemas, la pregunta debe delimitar el sistema: qué ecosistema, qué grupo de organismos, qué variable climática y qué período. Por ejemplo: «¿cambió en 20 años la fecha de floración de una especie de arbusto de un valle?». En cambio, «¿qué pasa con el planeta?» es demasiado amplia. Además, hay que declarar qué no se puede concluir con los datos.",
    ],
    vocab=[("tiempo atmosférico", "estado de la atmósfera en un lugar y un momento"), ("clima", "promedio de las condiciones atmosféricas durante muchos años"), ("gas de efecto invernadero", "gas que absorbe y devuelve parte de la energía que emite la superficie"), ("cambio climático", "cambio del clima a largo plazo, hoy impulsado por actividades humanas"), ("combustible fósil", "recurso formado hace millones de años, como el carbón o el petróleo")],
    worked=[
        ("Clima o tiempo", "«Hoy amaneció con neblina en el valle.» ¿Es una afirmación sobre el clima o sobre el tiempo atmosférico?",
         ["Habla de un momento concreto: hoy.", "El clima exige promedios de muchos años."],
         "Sobre el tiempo atmosférico"),
        ("Delimitar la pregunta", "¿Cuál está mejor delimitada: «¿cómo afecta el calor a la naturaleza?» o «¿cambió entre dos décadas la altitud a la que vive una especie de planta en una cordillera?»",
         ["La primera no nombra ecosistema, grupo, variable ni período.", "La segunda nombra una especie, una variable (altitud) y dos décadas."],
         "La segunda pregunta"),
    ],
    mistakes=[("Usar una ola de frío para negar el calentamiento del clima.", "Un evento de unos días es tiempo atmosférico y no cambia el promedio de décadas.", "Compara promedios de períodos largos, no días sueltos."),
              ("Creer que el efecto invernadero es algo malo en sí mismo.", "El efecto natural permite la vida; el problema es su intensificación por más gases.", "Distingue efecto natural de efecto intensificado.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es el clima?", "El promedio de las condiciones de la atmósfera durante muchos años", "El estado de la atmósfera en un día", "La temperatura más alta que se ha medido", "El clima resume muchos años, mientras que el tiempo atmosférico describe un momento."),
        ("{F} ¿Cuántos gases de efecto invernadero nombra el Hecho 1?", "4", "El Hecho 1 nombra vapor de agua, dióxido de carbono, metano y óxido nitroso."),
        ("{F} ¿Qué hecho (1, 2, 3 o 4) describe un dato de tiempo atmosférico?", "Hecho 3", "La helada de un día concreto es tiempo atmosférico, no clima."),
        ("abc", "{F} ¿Qué se puede concluir de la helada del Hecho 3 sobre el clima de la región?", "Nada sobre la tendencia del clima, porque es un solo día", "Que el calentamiento no existe", "Que el clima está enfriándose", "Un solo día no permite concluir sobre promedios de décadas."),
        ("ab", "El efecto invernadero natural:", "Es necesario para que la vida sea posible en la superficie", "Es un problema creado solo por las personas", "Sin los gases de efecto invernadero la superficie sería mucho más fría y la vida sería muy distinta."),
        ("abc", "¿Qué cambió en el efecto invernadero con la actividad humana?", "Se intensificó porque aumentó la cantidad de gases en la atmósfera", "Dejó de existir", "Se volvió independiente del dióxido de carbono", "Más gases absorben y devuelven más energía a la superficie."),
        ("=", "En una región ficticia, la temperatura promedio de la primera década fue 12 °C y la de la tercera década, 15 °C. ¿Cuántos grados subió entre ambas?", "15-12", "Se restan los promedios de las dos décadas para ver el cambio.", " °C"),
        ("=", "Los promedios anuales de ejemplo de una estación son 13 °C, 15 °C y 14 °C. ¿Cuál es el promedio de los tres años?", "(13+15+14)/3", "El promedio suma los tres valores y divide por la cantidad de años.", " °C"),
        ("abc", "¿Cuál pregunta está mejor delimitada para estudiar un efecto del cambio climático?", "¿Cambió en 20 años la fecha de floración de una especie de arbusto de un valle de ejemplo?", "¿Qué pasa con el planeta?", "¿Es malo el calor?", "La primera nombra un grupo, una variable, un lugar y un período."),
        ("abc", "Un equipo quiere estudiar el efecto del calentamiento sobre los anfibios de una cordillera. ¿Qué debe delimitar primero?", "La zona, la especie o grupo, la variable y el período de estudio", "Todos los anfibios del mundo", "Solo la opinión de los visitantes", "Delimitar permite medir y comparar con datos concretos."),
        ("ab", "Un equipo afirma que un verano muy caluroso prueba el cambio climático. ¿Qué es más prudente?", "Decir que un verano es tiempo atmosférico y que se necesitan promedios de muchos años", "Aceptar la afirmación porque hace mucho calor", "El cambio climático se evidencia en tendencias de décadas, no en un verano aislado."),
        ("abc", "¿Cuál de estas afirmaciones se refiere al clima?", "En esta región ficticia, el promedio de lluvias de los últimos treinta años es menor que el de los treinta anteriores", "Hoy llovió mucho en la tarde", "Mañana se espera sol", "Solo la primera compara promedios de períodos largos."),
        ("Ordena de menor a mayor escala de tiempo: (a) el tiempo de una tarde, (b) el clima de un valle medido en promedios de treinta años, (c) una semana de calor. Escribe las letras separadas por comas.", "a, c, b", "Una tarde es lo más corto, una semana va después y treinta años de promedio es la escala mayor."),
    ],
    ctx=("abc", "Contexto: en la feria científica del liceo, un visitante dice «hoy nevó, así que no hay calentamiento global». ¿Qué respuesta es más adecuada?", "Un día de nieve es tiempo atmosférico; el clima se evalúa con promedios de muchos años", "Tiene razón, porque la nieve es fría", "Hay que dejar de hablar del clima", "La respuesta distingue las escalas de tiempo del tiempo atmosférico y del clima."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un gas de efecto invernadero?", "Un gas que absorbe y devuelve parte de la energía emitida por la superficie", "Estos gases retienen parte de la energía y calientan la superficie."),
        ("ab", "El clima se estudia con:", "Promedios de muchos años", "Datos de un solo día", "Las tendencias climáticas se detectan con series largas."),
        ("ab", "Una pregunta bien delimitada nombra:", "Sistema, variable y período", "Solo la palabra «clima»", "Sin sistema, variable y período no se puede responder con datos."),
    ],
    op=("Con la ficha {F}: (1) clasifica los Hechos 3 y 4 como tiempo atmosférico o clima; (2) escribe una pregunta bien delimitada sobre el efecto del calentamiento en un grupo de organismos; (3) indica qué dato o período usarías para responderla.",
        "(1) El Hecho 3 es tiempo atmosférico y el Hecho 4 es clima. (2) ¿Cambió entre dos décadas la altitud a la que vive una especie de planta de una cordillera de ejemplo? (3) La altitud mínima y máxima de la especie en cada década, medida con el mismo método.",
        ["clasificación correcta", "pregunta con sistema, variable y período", "dato o período coherente"],
        ["tres respuestas numeradas"],
        ["confundir un día con el clima", "hacer una pregunta demasiado amplia", "proponer un dato que no se relaciona con la pregunta"],
        "Pregunta: «¿qué conclusión no podrías sacar con ese dato?»."),
    reinforce="Escribe tres afirmaciones de tiempo atmosférico y tres de clima, y rotula cada una.",
    extend="Explica con tus palabras por qué el efecto invernadero natural es necesario pero su intensificación es un problema.",
)

# ============================================================ OAC-03, clase 2
F = ("Ficha 11 (datos de ejemplo de una estación ficticia). Temperatura media anual por década, en °C: década 1: 13; década 2: 14; década 3: 15. "
     "Concentración de dióxido de carbono en el aire, en partes por millón (ppm), de ejemplo: década 1: 320; década 2: 350; década 3: 390. "
     "Fuente A: informe de un instituto científico que muestra su método y publica los datos. Fuente B: página sin autor que dice «el clima no cambia» y no muestra datos. "
     "La estación está en el centro de una ciudad, rodeada de pavimento y edificios.")
build(
    O3, 2, F,
    use="Aprenderé a evaluar fuentes y variables en datos climáticos: qué mide cada serie, qué problemas puede tener y qué se puede concluir. Sirve para distinguir evidencia de opinión cuando se discute el cambio climático.",
    prior=["Sé qué es una variable.", "Sé calcular diferencias y promedios.", "Sé qué es un gas de efecto invernadero."],
    explain=[
        "Los datos climáticos se obtienen con estaciones de medición, boyas, satélites y registros históricos. Para usarlos hay que revisar quién los produjo, con qué instrumento, en qué período y con qué método. Una buena fuente publica sus datos y su método, y puede ser revisada por otras personas. Una afirmación sin datos ni autor no es evidencia.",
        "También hay que mirar las variables que pueden distorsionar. Una estación en el centro de una ciudad mide más calor que una en un parque, porque el pavimento y los edificios retienen calor; a eso se le llama efecto de isla de calor urbana. Si se quiere estudiar la región, conviene combinar estaciones de distintos lugares. Además, la escala importa: un dato local no representa a todo el planeta.",
        "Cuando dos variables suben juntas, como el CO2 y la temperatura, hay una asociación. Una tabla sola no prueba la causa. Pero la explicación del calentamiento por gases de efecto invernadero se apoya además en un mecanismo físico conocido, es decir, que esos gases absorben energía, y en muchas líneas de evidencia independientes. Un buen informe separa lo que muestra el dato, lo que explica el mecanismo y lo que sigue incierto.",
    ],
    vocab=[("serie de datos", "conjunto de mediciones ordenadas en el tiempo"), ("isla de calor urbana", "mayor temperatura en una ciudad por el pavimento y los edificios"), ("asociación", "relación entre dos variables que cambian juntas"), ("mecanismo", "explicación de cómo una causa produce un efecto"), ("escala", "tamaño del área o del período al que se refiere un dato")],
    worked=[
        ("Calcular un cambio", "En una serie de ejemplo, la temperatura media pasa de 11 °C a 14 °C. ¿Cuántos grados subió?",
         ["Se restan los dos valores.", "14 − 11 = 3."],
         "3 °C"),
        ("Reconocer un sesgo de medición", "Una estación de ejemplo está junto a un estacionamiento de asfalto. ¿Qué problema puede tener su temperatura?",
         ["El asfalto retiene calor.", "La estación puede medir más calor que su entorno natural."],
         "Puede sobreestimar la temperatura por el calor del asfalto"),
    ],
    mistakes=[("Concluir que una sola estación representa al planeta.", "Un dato local depende de su entorno y no se puede generalizar sin otras estaciones.", "Combina estaciones de distintos lugares y escalas."),
              ("Decir que «dos variables que suben juntas prueban la causa».", "La asociación es una pista; la causa se apoya en mecanismo, comparaciones y otras evidencias.", "Escribe «están asociadas» y explica qué más apoya la causa.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es una serie de datos?", "Un conjunto de mediciones ordenadas en el tiempo", "Una sola medición muy exacta", "Una opinión sobre el clima", "Una serie permite ver tendencias porque ordena las mediciones en el tiempo."),
        ("{F} ¿Cuál fue la temperatura media de la década 2?", "14 °C", "La ficha indica 14 °C para la década 2."),
        ("=", "{F} ¿Cuántos grados subió la temperatura media entre la década 1 y la década 3?", "15-13", "Se restan los valores de las décadas extremas.", " °C"),
        ("=", "{F} ¿Cuántas ppm aumentó el dióxido de carbono entre la década 1 y la década 3?", "390-320", "Se restan las concentraciones de las dos décadas.", " ppm"),
        ("abc", "{F} ¿Cuál fuente muestra su método y publica sus datos?", "La Fuente A", "La Fuente B", "Ninguna de las dos", "Solo el informe del instituto describe su método y sus datos."),
        ("=", "{F} ¿Cuál es la temperatura media de las tres décadas juntas?", "(13+14+15)/3", "Se suman las tres temperaturas medias y se divide por la cantidad de décadas.", " °C"),
        ("abc", "{F} La estación está en el centro de una ciudad. ¿Qué factor puede distorsionar sus datos?", "La isla de calor urbana", "La falta de luz solar", "El ruido de los autos", "El pavimento y los edificios retienen calor y elevan la temperatura medida."),
        ("abc", "{F} ¿Qué se podría hacer para que la conclusión sea más sólida respecto del clima de la región?", "Incluir estaciones de un parque, de una zona rural y de la costa", "Usar solo la estación del centro", "Eliminar la serie de CO2", "Combinar lugares distintos reduce el efecto de un entorno particular."),
        ("ab", "{F} Las dos series (temperatura y CO2) suben juntas. ¿Qué se puede decir solo con la tabla?", "Que están asociadas, sin probar por sí sola la causa", "Que el CO2 es la única causa de todo cambio de temperatura", "La tabla muestra una asociación; la causa necesita mecanismo y otras evidencias."),
        ("abc", "{F} ¿Por qué se menciona el mecanismo de absorción de energía de los gases al explicar el calentamiento?", "Porque explica cómo el CO2 puede causar calentamiento, más allá de la asociación", "Porque reemplaza la necesidad de medir", "Porque demuestra que la temperatura nunca varía por otras causas", "El mecanismo aporta la explicación física de la relación."),
        ("abc", "{F} Una persona dice que la Fuente B refuta a la A porque ambas son opiniones. ¿Qué respondes?", "No: la A entrega datos y método revisables, y la B no", "Sí: ambas valen lo mismo", "Sí, porque la B es más corta", "Una afirmación sin datos no equivale a un informe con método."),
        ("abc", "Un estudio de ejemplo midió la temperatura del aire a 1,5 m del suelo y otro la del agua en superficie. ¿Qué precaución hay que tomar al compararlos?", "Revisar que midan la misma variable y con el mismo método", "Juntar los datos sin revisar", "Descartar ambos estudios", "Variables distintas no son comparables directamente."),
        ("ab", "¿Qué hace más confiable una serie larga de datos?", "Permite distinguir tendencias de variaciones de un año", "Garantiza que no hay errores", "Una serie larga ayuda a separar variaciones puntuales de cambios sostenidos."),
    ],
    ctx=("abc", "Contexto: un compañero te manda una gráfica sin autor, sin unidades y sin período, que dice que «no hay calentamiento». ¿Qué haces primero?", "Buscar la fuente, las unidades, el método y el período antes de aceptarla o rechazarla", "Compartirla porque se ve convincente", "Borrarla sin revisar nada", "Una gráfica sin fuente ni unidades no puede evaluarse hasta conocer esos datos."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es la isla de calor urbana?", "Mayor temperatura en una ciudad por el pavimento y los edificios", "El pavimento y los edificios retienen calor y elevan la temperatura local."),
        ("ab", "Una buena fuente científica:", "Publica su método y sus datos", "Oculta cómo midió", "Mostrar el método permite revisarla y repetirla."),
        ("ab", "Dos variables asociadas:", "No prueban la causa por sí solas", "Siempre prueban la causa", "La causa requiere más evidencia además de la asociación."),
    ],
    op=("Con la ficha {F}: (1) calcula el aumento de temperatura y de CO2 entre la década 1 y la 3; (2) evalúa las Fuentes A y B con un criterio para cada una; (3) escribe una limitación de los datos de la estación y una mejora para superarla.",
        "(1) 2 °C y 70 ppm. (2) La A muestra método y datos; la B no cita datos ni autor. (3) La estación está en el centro de la ciudad y puede medir más calor; conviene sumar estaciones de otros lugares.",
        ["dos diferencias correctas", "criterio para cada fuente", "limitación y mejora coherentes"],
        ["tres respuestas numeradas"],
        ["aceptar la fuente sin datos", "no mencionar la isla de calor", "proponer una mejora que no soluciona la limitación"],
        "Pregunta: «¿qué otra variable querrías medir para comprender mejor el cambio?»."),
    reinforce="Haz una lista de cinco preguntas que debes hacerle a una fuente de datos climáticos antes de usarla.",
    extend="Explica por qué una asociación entre dos variables no basta por sí sola para afirmar una causa, con un ejemplo distinto del clima.",
)

# ============================================================ OAC-03, clase 3
F = ("Ficha 12 (modelo conceptual y datos de ejemplo). Cadena de efectos propuesta: más temperatura del aire → menos nieve y menos agua de deshielo en verano → menor humedad del suelo → menor crecimiento de las plantas (menor productividad primaria) → menos alimento para los herbívoros. "
     "Datos de una planta de montaña de ejemplo: década 1: vive entre 1.800 y 2.400 metros de altitud; década 3: vive entre 2.100 y 2.400 metros (la cumbre llega a 2.400 metros). "
     "Fenología de ejemplo (momento del año en que ocurre un evento): año 1: la planta florece el día 100 del año y su polinizador emerge el día 100; año 20: la planta florece el día 90 y el polinizador emerge el día 110.")
build(
    O3, 3, F,
    use="Aprenderé a interpretar un modelo que conecta el cambio climático con la biodiversidad, la productividad y la resiliencia de un ecosistema. Sirve para explicar efectos en cadena y prever qué puede pasar.",
    prior=["Sé qué es la productividad primaria.", "Sé qué es una especie y su hábitat.", "Sé calcular diferencias y porcentajes sencillos."],
    explain=[
        "Un modelo conceptual conecta causas y efectos con flechas. Para el cambio climático, una cadena típica es: más temperatura y cambios en la lluvia alteran el agua disponible, eso cambia el crecimiento de las plantas (productividad primaria) y, por tanto, el alimento de los herbívoros y de sus depredadores. Cada eslabón puede medirse y ponerse a prueba con datos.",
        "Los efectos sobre la biodiversidad se observan de varias formas. Muchas especies desplazan su distribución hacia zonas más frías, como mayores altitudes. Cambia la fenología, es decir, la época de eventos como la floración o la migración, y si dos especies que se necesitan cambian a ritmos distintos, se produce un desfase. En el océano, parte del dióxido de carbono se disuelve en el agua y la vuelve más ácida, lo que afecta a organismos con conchas o esqueletos de carbonato.",
        "La resiliencia es la capacidad de un ecosistema de recuperar su funcionamiento tras una perturbación. Los ecosistemas con más especies, más conexiones y menos presiones adicionales suelen ser más resilientes. Un modelo siempre simplifica: deja fuera otros factores, como los incendios o la contaminación, y por eso sus predicciones deben contrastarse con datos.",
    ],
    vocab=[("productividad primaria", "cantidad de materia orgánica que producen los productores"), ("fenología", "momento del año en que ocurren eventos biológicos como la floración"), ("desfase", "diferencia de tiempo entre dos eventos que antes coincidían"), ("acidificación del océano", "descenso del pH del agua por el dióxido de carbono que absorbe"), ("resiliencia", "capacidad de recuperar el funcionamiento tras una perturbación")],
    worked=[
        ("Calcular un desfase", "En un caso de ejemplo, una flor abre el día 120 y su polinizador emerge el día 135. ¿Cuántos días de desfase hay?",
         ["Se restan los días de los dos eventos.", "135 − 120 = 15."],
         "15 días"),
        ("Leer una cadena de efectos", "En un modelo de ejemplo: más temperatura → menos lluvia → menos pasto → menos alimento para los herbívoros. Si en una zona la lluvia no baja, ¿qué eslabón deja de tener su causa inmediata?",
         ["Cada flecha depende de la anterior.", "El eslabón que sigue a «menos lluvia» es «menos pasto».", "Sin menos lluvia, el pasto no baja por falta de agua."],
         "Menos pasto"),
    ],
    mistakes=[("Pensar que todas las especies se desplazan con el calor.", "Algunas no pueden: las de cumbres no tienen a dónde subir, o hay barreras.", "Revisa si existe un espacio disponible al que la especie pueda desplazarse."),
              ("Creer que si un efecto se mide en un lugar, ocurre igual en todos.", "Los efectos dependen del ecosistema, la especie y otras presiones.", "Declara el lugar y el grupo estudiado antes de generalizar.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es la fenología?", "El momento del año en que ocurren eventos biológicos como la floración", "El estudio de las rocas de una montaña", "La cantidad total de especies de un lugar", "La fenología estudia las fechas de eventos del ciclo de vida."),
        ("{F} Según el modelo, ¿qué ocurre primero: la menor humedad del suelo o el menor crecimiento de las plantas?", "La menor humedad del suelo", "En la cadena, la menor humedad del suelo provoca el menor crecimiento."),
        ("=", "{F} ¿Cuántos metros de rango de altitud tenía la planta en la década 1?", "2400-1800", "El rango se calcula restando el límite inferior al superior.", " metros"),
        ("=", "{F} ¿Cuántos metros de rango de altitud tiene la planta en la década 3?", "2400-2100", "El rango se calcula restando el límite inferior al superior de la década 3.", " metros"),
        ("abc", "{F} ¿Qué límite de la distribución de la planta cambió entre la década 1 y la 3?", "El límite inferior subió de 1.800 a 2.100 metros", "El límite superior subió", "No cambió ninguno", "La planta dejó de vivir en las partes bajas y el límite de arriba se mantiene."),
        ("=", "{F} ¿Qué porcentaje del rango original conserva la planta en la década 3?", "300/600*100", "Se divide el rango actual por el rango de la década 1 y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Por qué el límite superior de la planta no sube más?", "Porque la cumbre llega solo a 2.400 metros y no hay terreno más alto", "Porque a la planta no le gusta el calor", "Porque el rango no puede cambiar", "Una especie de cumbre no puede subir si ya está en la parte más alta."),
        ("=", "{F} En el año 20, ¿cuántos días de desfase hay entre la floración y la emergencia del polinizador?", "110-90", "Se restan las fechas de los dos eventos del año 20.", " días"),
        ("abc", "{F} ¿Por qué este desfase puede afectar a la planta?", "Porque cuando florece, el polinizador aún no ha emergido y puede producir menos semillas", "Porque el polinizador florece antes que la planta", "Porque la planta deja de necesitar polinizador", "Si no coinciden en el tiempo, la polinización disminuye."),
        ("abc", "{F} Según el modelo, ¿cómo puede el calentamiento afectar a los herbívoros que se alimentan de esa planta?", "Disminuye la humedad, baja el crecimiento de las plantas y hay menos alimento", "Les entrega alimento ilimitado", "No les afecta, porque el modelo termina en las plantas", "La cadena del modelo conecta la temperatura con el alimento disponible."),
        ("ab", "El agua de mar absorbe parte del dióxido de carbono del aire. ¿Qué efecto tiene eso sobre el agua?", "Aumenta su acidez, lo que afecta a organismos con conchas", "Aumenta su salinidad en forma directa", "El dióxido de carbono disuelto hace descender el pH del agua."),
        ("abc", "¿Qué ecosistema tiene probablemente mayor resiliencia ante una sequía?", "Uno con muchas especies que cumplen funciones parecidas y sin otras presiones", "Uno con una sola especie y con contaminación", "Uno fragmentado en parcelas aisladas", "La diversidad funcional y la ausencia de presiones adicionales favorecen la recuperación."),
        ("abc", "Un modelo no incluye los incendios forestales. ¿Qué precaución hay que tomar al usarlo?", "Declarar que sus predicciones valen solo si no hay incendios", "Considerar que el modelo es perfecto", "Eliminar el modelo", "Todo modelo simplifica y debe declarar lo que deja fuera."),
    ],
    ctx=("abc", "Contexto: una reserva de montaña de ejemplo observa que una planta emblemática sube de altitud cada década. ¿Qué información sería más útil para saber si está en riesgo?", "La altura de la cumbre y si hay terreno más alto adonde la planta pueda subir", "El color de las flores", "El número de visitantes del año pasado", "Si no hay terreno más alto, la especie queda con menos espacio y en mayor riesgo."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es la productividad primaria?", "La cantidad de materia orgánica que producen los productores", "Mide cuánta materia orgánica fabrican los productores."),
        ("ab", "Un modelo sirve para:", "Explicar y predecir, declarando sus supuestos", "Reemplazar toda medición", "Un modelo se contrasta con datos y se corrige."),
        ("ab", "La resiliencia es:", "Recuperar el funcionamiento tras una perturbación", "No cambiar jamás ante nada", "Describe la recuperación, no la ausencia de cambio."),
    ],
    op=("Con la ficha {F}: (1) explica la cadena de efectos del modelo con tus palabras en tres oraciones; (2) calcula el desfase fenológico y la reducción del rango de altitud; (3) propone una forma de medir en terreno real, en el futuro, si el modelo es correcto.",
        "(1) Más temperatura reduce la nieve y el agua de deshielo, baja la humedad del suelo, disminuye el crecimiento de las plantas y deja menos alimento para los herbívoros. (2) 20 días de desfase y el rango bajó de 600 a 300 metros. (3) Medir cada año la humedad del suelo, el crecimiento de las plantas y la fecha de floración y de emergencia del polinizador en las mismas parcelas.",
        ["cadena de efectos ordenada", "dos cálculos correctos", "medición concreta y repetible"],
        ["tres respuestas numeradas"],
        ["invertir el orden de la cadena", "calcular mal el desfase", "proponer una medición vaga"],
        "Pregunta: «¿qué factor no incluido en el modelo podría explicar el cambio?»."),
    reinforce="Dibuja con palabras una cadena de efectos del calentamiento sobre un humedal de ejemplo, con al menos cuatro eslabones.",
    extend="Explica por qué la acidificación del océano es un efecto del dióxido de carbono distinto del aumento de temperatura.",
)

# ============================================================ OAC-03, clase 4
F = ("Ficha 13 (datos de ejemplo de una bahía ficticia). Captura anual de un pez, en toneladas: año 1: 500; año 5: 420. "
     "Temperatura superficial del agua: año 1: 14 °C; año 5: 16 °C. Número de barcos que pescan: año 1: 20; año 5: 30. "
     "Caudal de verano de un río alimentado por deshielo, en millones de metros cúbicos: año 1: 80; año 5: 60. Una comunidad de pescadores artesanales de la bahía depende del pez y del agua del río para regar sus huertos.")
build(
    O3, 4, F,
    use="Aprenderé a analizar evidencia sobre las consecuencias del cambio climático en recursos naturales, personas y desarrollo sostenible. Sirve para separar lo que los datos muestran de lo que se supone y reconocer que hay varias causas a la vez.",
    prior=["Sé qué es un recurso natural.", "Sé calcular porcentajes de cambio.", "Sé que una asociación no prueba por sí sola una causa."],
    explain=[
        "Los recursos naturales son elementos de la naturaleza que las personas usan, como el agua, los peces o el suelo. El cambio climático puede afectarlos de varias maneras: cambia la disponibilidad de agua, mueve las zonas donde viven las especies pescadas o cultivadas, y altera la productividad de los ecosistemas. Esto repercute en el trabajo, la alimentación y la salud de las personas, y las comunidades que dependen directamente de un recurso son las más expuestas.",
        "El desarrollo sostenible es el que satisface las necesidades del presente sin comprometer la capacidad de las futuras generaciones de satisfacer las suyas. Tiene tres dimensiones que se influyen entre sí: la ambiental, la social y la económica. Una decisión sostenible considera las tres y no sacrifica una por otra. Por eso se analizan también los efectos desiguales: quién pierde más y quién tiene más recursos para adaptarse.",
        "Al analizar evidencia hay que cuidar la causalidad. Si cae la captura de un pez y sube la temperatura, pero también aumentó el número de barcos, no se puede atribuir toda la caída al clima: la sobrepesca también pudo influir. Se calcula el cambio relativo, se listan las posibles causas, se propone una comparación que las separe, y se declara qué sigue incierto.",
    ],
    vocab=[("recurso natural", "elemento de la naturaleza que las personas usan, como agua, peces o suelo"), ("desarrollo sostenible", "desarrollo que satisface las necesidades presentes sin comprometer las de futuras generaciones"), ("sobrepesca", "captura de peces a un ritmo mayor que el de su reposición"), ("cambio relativo", "variación expresada como porcentaje del valor inicial"), ("adaptación", "ajuste de las personas o los ecosistemas a nuevas condiciones")],
    worked=[
        ("Calcular un cambio relativo", "Una captura de ejemplo pasa de 200 a 170 toneladas. ¿Qué porcentaje bajó, calculado respecto del valor inicial?",
         ["Bajó 200 − 170 = 30 toneladas.", "30 ÷ 200 × 100 = 15."],
         "15 %"),
        ("Separar causas", "En un lago de ejemplo bajó la captura mientras subían la temperatura del agua y el número de pescadores. ¿Se puede atribuir la baja solo al clima?",
         ["Hay dos cambios simultáneos.", "Los datos no los separan.", "Hace falta comparar lagos o años con y sin el otro factor."],
         "No, con esos datos no se puede atribuir solo al clima"),
    ],
    mistakes=[("Atribuir toda la caída de un recurso al clima sin revisar otras causas.", "Otros factores, como la sobrepesca o la contaminación, pueden contribuir.", "Lista todas las causas posibles y propón una comparación que las separe."),
              ("Entender el desarrollo sostenible como «proteger la naturaleza y nada más».", "Incluye también las dimensiones social y económica, pensadas para las generaciones futuras.", "Revisa que la propuesta considere las tres dimensiones.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es el desarrollo sostenible?", "El que satisface las necesidades presentes sin comprometer las de futuras generaciones", "El que maximiza la ganancia de hoy", "El que prohíbe toda actividad económica", "Combina las necesidades presentes con la capacidad futura de satisfacerlas."),
        ("{F} ¿Cuántas toneladas de pez se capturaron en el año 5?", "420", "La ficha indica 420 toneladas en el año 5."),
        ("=", "{F} ¿Cuántas toneladas menos se capturaron en el año 5 que en el año 1?", "500-420", "Se resta la captura del año 5 a la del año 1.", " toneladas"),
        ("=", "{F} ¿Qué porcentaje de la captura del año 1 bajó hasta el año 5?", "(500-420)/500*100", "El cambio relativo compara la baja con el valor inicial.", " %"),
        ("=", "{F} ¿Cuántos grados subió la temperatura del agua entre el año 1 y el año 5?", "16-14", "Se restan las temperaturas de los dos años.", " °C"),
        ("=", "{F} ¿Qué porcentaje aumentó el número de barcos entre el año 1 y el año 5?", "(30-20)/20*100", "El aumento relativo compara los barcos nuevos con los iniciales.", " %"),
        ("=", "{F} ¿Qué porcentaje bajó el caudal de verano del río entre el año 1 y el año 5?", "(80-60)/80*100", "El cambio relativo es la baja dividida por el valor inicial.", " %"),
        ("abc", "{F} ¿Por qué no se puede atribuir toda la baja de la captura al calentamiento del agua?", "Porque también aumentó el número de barcos y pudo haber sobrepesca", "Porque la temperatura no cambió", "Porque la captura no bajó", "Hay otro factor simultáneo que pudo influir en la captura."),
        ("abc", "{F} ¿Qué comparación ayudaría más a separar el efecto del clima del de los barcos?", "Comparar bahías parecidas con distinto número de barcos y con temperaturas similares", "Preguntar a una sola persona", "Mirar solo la bahía con más barcos", "Una comparación con control de variables separa causas."),
        ("abc", "{F} ¿Qué parte de la comunidad de la ficha se vería más afectada si ambos recursos disminuyen?", "Los pescadores artesanales, que dependen del pez y del agua del río", "Las personas que no dependen de esos recursos", "Los turistas que visitan la bahía un fin de semana", "La comunidad de ejemplo depende directamente de ambos recursos."),
        ("ab", "{F} ¿Cuál es una medida coherente con el desarrollo sostenible para la bahía?", "Regular la captura y apoyar usos del agua que consideren a las futuras generaciones", "Aumentar la captura hasta agotar el recurso", "Una medida sostenible cuida el recurso y a las personas hoy y mañana."),
        ("abc", "Dos comunidades de ejemplo sufren la misma sequía. Una tiene embalses y apoyo técnico, la otra no. ¿Qué se puede esperar?", "Que la segunda sufra efectos más graves por tener menos capacidad de adaptación", "Que ambas sufran lo mismo", "Que la primera sufra más", "La capacidad de adaptación depende de los recursos disponibles."),
        ("abc", "Una conclusión bien redactada sobre la ficha sería:", "La captura bajó mientras subieron la temperatura y los barcos; los datos no permiten separar las causas", "El clima es la única causa de la baja", "Los barcos no influyen en nada", "Una conclusión correcta se ciñe a los datos y reconoce lo que no se puede separar."),
    ],
    ctx=("abc", "Contexto: una cooperativa de pescadores de ejemplo debe decidir cómo responder a la caída de sus capturas. ¿Qué paso es más sólido?", "Reunir datos de captura, esfuerzo de pesca y temperatura, y decidir con ellos", "Aumentar el número de barcos sin analizar", "Atribuir la baja a una causa sin datos", "Decidir con datos que separen causas reduce el riesgo de elegir una medida inútil."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es la sobrepesca?", "Capturar peces a un ritmo mayor que el de su reposición", "La sobrepesca agota el recurso cuando se extrae más de lo que se repone."),
        ("ab", "El desarrollo sostenible considera:", "Las dimensiones ambiental, social y económica", "Solo la dimensión económica", "Las tres dimensiones se influyen entre sí."),
        ("ab", "Para atribuir una causa hay que:", "Separar las causas posibles con comparaciones", "Elegir la que más gusta", "Una comparación controlada acerca al efecto de cada causa."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula el cambio relativo de la captura, de los barcos y del caudal; (2) redacta una conclusión de dos oraciones que no atribuya todo al clima; (3) propone una medida de desarrollo sostenible para la comunidad y la dimensión (ambiental, social o económica) que protege.",
        "(1) La captura bajó 16 %, los barcos subieron 50 % y el caudal bajó 25 %. (2) La captura bajó mientras subieron la temperatura y los barcos; con estos datos no se separa el efecto del clima del de la pesca. (3) Regular el esfuerzo de pesca y apoyar un riego eficiente: protege la dimensión ambiental y la económica de la comunidad.",
        ["tres cambios relativos correctos", "conclusión que declara incertidumbre", "medida con dimensión sostenible"],
        ["tres respuestas numeradas"],
        ["dividir por el valor final", "atribuir todo al clima", "proponer una medida sin dimensión"],
        "Pregunta: «¿qué dato nuevo te permitiría separar las causas?»."),
    reinforce="Haz una lista de tres recursos naturales de tu región y, para cada uno, cómo podría afectarle un cambio en el clima.",
    extend="Explica por qué una comunidad con menos recursos económicos puede sufrir más un mismo efecto del cambio climático.",
)

# ============================================================ OAC-04, clase 1
F = ("Ficha 14 (seis acciones de ejemplo ante el cambio climático). a) Reducir la quema de combustibles fósiles en una central de ejemplo. b) Crear corredores de vegetación nativa para que las especies se desplacen hacia zonas más frescas. "
     "c) Reforestar con especies nativas una ladera que se quemó. d) Proteger turberas y bosques que almacenan carbono. e) Restaurar un humedal que fue drenado. f) Instalar refugios con sombra y agua para la fauna en olas de calor.")
build(
    O4, 1, F,
    use="Aprenderé a delimitar si una acción busca prevenir, mitigar o reparar efectos del cambio climático sobre los sistemas naturales. Sirve para plantear preguntas de investigación sobre soluciones concretas.",
    prior=["Sé qué es el cambio climático y qué lo causa.", "Sé qué es un ecosistema.", "Sé distinguir una causa de un efecto."],
    explain=[
        "Las acciones frente al cambio climático se pueden ordenar según el momento en que actúan. Prevenir es evitar que el efecto ocurra o se agrave, por ejemplo reduciendo las emisiones de gases o protegiendo ecosistemas que almacenan carbono, como los bosques y las turberas (humedales con suelo rico en restos de plantas). Mitigar es atenuar el efecto cuando ya se está produciendo, por ejemplo facilitando que las especies se desplacen o tengan refugios. Reparar es restaurar lo que ya se dañó, por ejemplo reforestando o recuperando un humedal.",
        "En la literatura científica el término «mitigación» se usa a menudo solo para reducir emisiones o aumentar la captura de carbono, y «adaptación» para ajustarse a los efectos. Este cuaderno usa las tres palabras del objetivo de la asignatura, prevenir, mitigar y reparar, y las define como arriba; por eso conviene explicar siempre cómo se usa cada término en tu investigación.",
        "Una buena pregunta de investigación sobre soluciones nombra el sistema natural, el efecto climático que se quiere abordar, la acción y la forma de medir su resultado. Por ejemplo: «¿aumenta la riqueza de especies de plantas nativas de una ladera quemada cuando se reforesta, comparada con una ladera igual que no se reforesta?». Así se puede comprobar con datos.",
    ],
    vocab=[("prevenir", "evitar que un efecto ocurra o se agrave"), ("mitigar", "atenuar un efecto que ya se está produciendo"), ("reparar", "restaurar lo que ya se dañó"), ("sumidero de carbono", "ecosistema que absorbe y almacena más carbono del que libera"), ("restauración ecológica", "ayuda a la recuperación de un ecosistema degradado")],
    worked=[
        ("Clasificar una acción", "Se planta vegetación nativa para unir dos bosques separados y permitir que la fauna se desplace. ¿Previene, mitiga o repara?",
         ["La fauna ya enfrenta un efecto que se está produciendo.", "La acción atenúa ese efecto al permitir el desplazamiento."],
         "Mitiga"),
        ("Delimitar la pregunta", "¿Cuál está mejor delimitada: «¿sirve reforestar?» o «¿aumenta la cobertura de vegetación nativa de una ladera quemada de ejemplo cinco años después de reforestar, comparada con otra que no se reforestó?»",
         ["La primera no nombra sistema, efecto ni medida.", "La segunda nombra la ladera, la variable, el tiempo y un grupo de comparación."],
         "La segunda pregunta"),
    ],
    mistakes=[("Confundir prevenir con reparar.", "Prevenir actúa antes del daño; reparar actúa después de que ocurrió.", "Pregunta: ¿el daño ya ocurrió o se busca evitarlo?"),
              ("Creer que una sola acción resuelve el cambio climático.", "Los problemas son complejos y se necesitan varias acciones combinadas.", "Compara acciones y evalúa en qué se complementan.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué significa reparar un efecto del cambio climático sobre un ecosistema?", "Restaurar lo que ya se dañó", "Evitar que ocurra el daño", "Ignorar el daño", "Reparar actúa después del daño para recuperar el ecosistema."),
        ("{F} ¿Qué acción (a a f) propone reforestar con especies nativas una ladera quemada?", "c", "La acción c describe esa reforestación."),
        ("{F} ¿Qué acción (a a f) busca reducir la quema de combustibles fósiles?", "a", "La acción a se refiere a la central de ejemplo que reduce la quema."),
        ("abc", "{F} La acción a (reducir la quema de combustibles fósiles) es de tipo…", "preventivo", "reparador", "mitigador de efectos en la fauna", "Evita emisiones de gases antes de que causen más calentamiento."),
        ("abc", "{F} La acción c (reforestar una ladera quemada) es de tipo…", "reparador", "preventivo", "mitigador", "Restaura lo que ya se dañó con el incendio."),
        ("abc", "{F} La acción b (crear corredores de vegetación nativa) es de tipo…", "mitigador", "preventivo", "reparador", "Atenúa el efecto del calentamiento facilitando el desplazamiento de especies."),
        ("abc", "{F} La acción d (proteger turberas y bosques que almacenan carbono) es de tipo…", "preventivo", "reparador", "mitigador", "Evita que el carbono almacenado llegue a la atmósfera."),
        ("abc", "{F} La acción e (restaurar un humedal que fue drenado) es de tipo…", "reparador", "preventivo", "mitigador", "Recupera un ecosistema que ya fue dañado."),
        ("abc", "{F} La acción f (refugios con sombra y agua para fauna en olas de calor) es de tipo…", "mitigador", "preventivo", "reparador", "Atenúa el efecto del calor en la fauna cuando ya se está produciendo."),
        ("{F} ¿Cuántas acciones de la ficha son de tipo reparador?", "2", "Son la c, que reforesta una ladera quemada, y la e, que restaura un humedal drenado."),
        ("abc", "¿Cuál pregunta está mejor delimitada para investigar una solución?", "¿Aumenta la riqueza de especies de plantas nativas de una ladera quemada de ejemplo cuando se reforesta, comparada con una ladera igual sin reforestar?", "¿Sirve reforestar?", "¿Es buena la naturaleza?", "Solo la primera nombra sistema, variable y comparación."),
        ("ab", "En una investigación, usas «mitigar» para atenuar efectos ya presentes. ¿Qué debes hacer?", "Definir el término como lo usas, porque en otros textos puede significar otra cosa", "No explicar nada: todos usan la palabra igual", "Los términos de clima tienen usos distintos entre textos, por lo que conviene definirlos."),
        ("abc", "Un equipo quiere medir el resultado de una restauración de humedal. ¿Qué dato sirve mejor?", "La cobertura de plantas nativas y el número de especies antes y después", "El color del agua en una foto", "La opinión de un visitante", "Los datos antes y después permiten medir el cambio."),
    ],
    ctx=("abc", "Contexto: un liceo de ejemplo quiere proponer una acción para un humedal local degradado. Debe decidir si su meta es prevenir, mitigar o reparar. ¿Qué decisión es coherente si el humedal ya fue drenado?", "Reparar, por ejemplo restaurando su régimen de agua y su vegetación", "Prevenir, porque el daño ya ocurrió", "No hacer nada", "Si el daño ya ocurrió, la meta es restaurarlo, aunque también convenga prevenir nuevos daños."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un sumidero de carbono?", "Un ecosistema que absorbe y almacena más carbono del que libera", "Los sumideros retiran carbono de la atmósfera."),
        ("ab", "Prevenir significa:", "Evitar que el efecto ocurra o se agrave", "Esperar que el daño ocurra", "Prevenir actúa antes de que el daño ocurra."),
        ("ab", "Una pregunta sobre soluciones debe nombrar:", "Sistema, acción y forma de medir el resultado", "Solo la palabra «solución»", "Con esos elementos se puede responder con datos."),
    ],
    op=("Con la ficha {F}: (1) elige tres acciones, una que prevenga, una que mitigue y una que repare, y rotúlalas; (2) escribe una pregunta de investigación bien delimitada sobre una de ellas; (3) indica qué dato compararías y con qué grupo de comparación.",
        "(1) a previene, b mitiga, c repara. (2) ¿Aumenta la cobertura de vegetación nativa de una ladera quemada de ejemplo cinco años después de reforestar? (3) Compararía la cobertura de la ladera reforestada con la de una ladera parecida sin reforestar.",
        ["tres acciones bien clasificadas", "pregunta con sistema, variable y tiempo", "dato y grupo de comparación coherentes"],
        ["tres respuestas numeradas"],
        ["clasificar mal una acción", "hacer una pregunta sin variable", "olvidar el grupo de comparación"],
        "Pregunta: «¿qué limitación tendría tu comparación?»."),
    reinforce="Inventa dos acciones para cada uno de los tres tipos (prevenir, mitigar, reparar) para un bosque de ejemplo.",
    extend="Explica con un ejemplo por qué una misma acción puede cumplir más de un propósito, por ejemplo prevenir y reparar.",
)

# ============================================================ OAC-04, clase 2
F = ("Ficha 15 (dos estudios de ejemplo sobre reforestar con especies nativas). Estudio 1: se plantaron 5 parcelas y se dejaron otras 5, parecidas en suelo y pendiente, sin plantar; a los 5 años se midió en las 10 parcelas el porcentaje de superficie cubierta por plantas nativas. Parcelas plantadas: 60, 70, 80, 70, 70. "
     "Parcelas no plantadas: 10, 20, 10, 10, 0. Los autores publicaron su método y sus datos. "
     "Estudio 2: se plantó una sola parcela y se midió un mes después; no hay parcela de comparación. Lo difundió una empresa que vende plántulas.")
build(
    O4, 2, F,
    use="Aprenderé a evaluar fuentes y variables de una investigación sobre soluciones al cambio climático: qué se cambia, qué se mide, qué se controla y qué intereses hay detrás. Sirve para decidir si una solución tiene evidencia suficiente.",
    prior=["Sé qué es una variable.", "Sé calcular promedios.", "Sé que una comparación necesita un grupo de contraste."],
    explain=[
        "Para probar si una solución funciona se compara. En un estudio ordenado hay una variable independiente, que es lo que se cambia, por ejemplo plantar o no plantar; una variable dependiente, que es lo que se mide, como la supervivencia o la cobertura de plantas; y variables controladas, que se mantienen parecidas, como el suelo, la pendiente y el clima. Un grupo de control es el que no recibe la acción y sirve de comparación.",
        "También importa el tamaño y la duración del estudio. Una sola parcela medida un mes después no dice cómo estará el sistema en años. Con varias parcelas se puede calcular un promedio y ver cuánto varían los resultados. Además se revisa la fuente: quién financió, si publicó el método y los datos, y si tiene un interés económico en el resultado, lo que se llama conflicto de interés.",
        "Un estudio con conflicto de interés no es necesariamente falso, pero exige más cuidado y contraste con otras fuentes. Un informe responsable declara sus límites: qué no midió, qué podría cambiar con el tiempo y en qué condiciones sus resultados no se aplican.",
    ],
    vocab=[("variable independiente", "lo que se cambia a propósito en un estudio"), ("variable dependiente", "lo que se mide para ver el efecto"), ("variable controlada", "condición que se mantiene parecida para comparar con justicia"), ("grupo de control", "grupo que no recibe la acción y sirve de comparación"), ("conflicto de interés", "situación en que una fuente puede beneficiarse del resultado que informa")],
    worked=[
        ("Identificar variables", "En un estudio de ejemplo se riegan 4 parcelas y se dejan 4 sin regar; se mide cuántas plantas crecen. ¿Cuál es la variable independiente?",
         ["Es lo que se cambia a propósito.", "Se riega o no se riega."],
         "Regar o no regar"),
        ("Calcular un promedio", "Las supervivencias de ejemplo en tres parcelas fueron 50, 60 y 70 por ciento. ¿Cuál es el promedio?",
         ["Se suman: 50 + 60 + 70 = 180.", "Se divide por 3: 180 ÷ 3 = 60."],
         "60 %"),
    ],
    mistakes=[("Confiar en un estudio sin grupo de control.", "Sin comparación no se sabe si el resultado se debe a la acción o a otros factores.", "Pide una parcela comparable que no reciba la acción."),
              ("Descartar un estudio solo porque lo financia una empresa.", "El conflicto de interés pide más cuidado, pero no lo hace falso por sí mismo.", "Contrasta con otras fuentes y revisa su método y datos.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un grupo de control?", "El grupo que no recibe la acción y sirve de comparación", "El grupo que recibe todas las acciones", "El grupo que más resultados tiene", "El grupo de control permite saber qué habría pasado sin la acción."),
        ("{F} En el Estudio 1, ¿cuántas parcelas se plantaron?", "5", "La ficha indica que se plantaron 5 parcelas y otras 5 quedaron sin plantar."),
        ("{F} ¿Cuál es la variable independiente del Estudio 1?", "Plantar o no plantar", "Es lo que los investigadores cambian a propósito entre las parcelas."),
        ("=", "{F} ¿Cuál es el promedio de cobertura de plantas nativas en las parcelas plantadas del Estudio 1?", "(60+70+80+70+70)/5", "Se suman las cinco supervivencias y se divide por cinco.", " %"),
        ("=", "{F} ¿Cuál es el promedio de cobertura de plantas nativas en las parcelas no plantadas del Estudio 1?", "(10+20+10+10+0)/5", "Se suman las cinco mediciones y se divide por cinco.", " %"),
        ("abc", "{F} ¿Cuál de estas condiciones se controló en el Estudio 1?", "El tipo de suelo y la pendiente de las parcelas", "El número de visitantes", "El precio de las plántulas", "La ficha dice que las parcelas eran parecidas en suelo y pendiente."),
        ("abc", "{F} ¿Por qué el Estudio 2 aporta menos evidencia?", "Tiene una sola parcela, midió un mes después y no tiene comparación", "Porque lo escribió una empresa y por eso es falso", "Porque usa especies nativas", "Sin comparación ni duración suficiente no se puede concluir sobre la solución."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de cobertura tienen en promedio las parcelas plantadas que las no plantadas del Estudio 1?", "70-10", "Se restan los dos promedios calculados.", " puntos"),
        ("ab", "{F} ¿Qué hay que revisar del Estudio 2 por su origen?", "Si la empresa tiene interés económico en el resultado y si publicó su método y datos", "Si el nombre de la empresa es corto", "Un conflicto de interés pide revisar método y datos y contrastar con otras fuentes."),
        ("abc", "{F} Una persona dice que el Estudio 2 es falso porque lo difundió una empresa. ¿Qué respondes?", "No necesariamente: hay que revisar su método, sus datos y contrastarlo con otras fuentes", "Tiene razón: toda empresa miente", "Sí, porque no tiene parcelas", "El origen exige cuidado, pero la evaluación se basa en el método y los datos."),
        ("abc", "{F} Si en el Estudio 1 las parcelas plantadas tuvieran suelos más fértiles que las no plantadas, ¿qué problema habría?", "No se sabría si la diferencia se debe a plantar o al suelo", "Ningún problema", "Los datos serían más precisos", "Sin controlar el suelo, la diferencia puede deberse a él."),
        ("abc", "Los autores del Estudio 1 declaran que midieron solo hasta los cinco años. ¿Qué limitación declaran?", "No se sabe cómo estarán las parcelas después de cinco años", "Que las parcelas no existen", "Que las plantas no crecen", "Una medición de cinco años no permite afirmar lo que ocurrirá más tarde."),
        ("abc", "Un estudio de ejemplo dice: «Plantamos 1.000 árboles». ¿Qué dato falta para evaluar el resultado?", "Cuántos sobrevivieron después de varios años y si hubo comparación", "El color de las hojas", "El nombre del equipo", "Plantar no es lo mismo que tener un bosque que prospera."),
    ],
    ctx=("abc", "Contexto: tu municipio recibe una propuesta de una empresa de plántulas para reforestar una ladera. Piden tu opinión. ¿Qué respuesta es más sólida?", "Pedir los datos y el método, y compararlos con estudios de otras fuentes antes de decidir", "Aceptar porque la empresa es conocida", "Rechazar sin leer porque vende plántulas", "Evaluar método, datos y contraste con otras fuentes protege de decisiones sesgadas."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es una variable dependiente?", "Lo que se mide para ver el efecto", "La variable dependiente es el resultado que se registra."),
        ("ab", "Una variable controlada:", "Se mantiene parecida entre grupos", "Se cambia a propósito", "Se controla para comparar con justicia."),
        ("ab", "Un conflicto de interés:", "Exige más cuidado, pero no hace falso al estudio", "Prueba que el estudio es falso", "Hay que contrastar con otras fuentes y revisar el método."),
    ],
    op=("Con la ficha {F}: (1) identifica la variable independiente, la dependiente y dos controladas del Estudio 1; (2) calcula los dos promedios y escribe qué comparación permiten; (3) explica por qué el Estudio 2 no basta para decidir.",
        "(1) Independiente: plantar o no; dependiente: cobertura de plantas nativas; controladas: suelo y pendiente. (2) 70 % contra 10 % de cobertura: permiten comparar parcelas plantadas con parcelas sin plantar, con una diferencia de 60 puntos. (3) El Estudio 2 tiene una parcela, un mes de duración, sin comparación y un posible conflicto de interés.",
        ["variables bien identificadas", "dos promedios correctos", "tres razones contra el Estudio 2"],
        ["tres respuestas numeradas"],
        ["confundir independiente y dependiente", "comparar mal los promedios", "descartar el Estudio 2 solo por su origen"],
        "Pregunta: «¿qué agregarías al Estudio 2 para que sea comparable?»."),
    reinforce="Escribe un estudio de ejemplo de dos líneas para evaluar si un corredor de vegetación ayuda a una especie, nombrando sus tres tipos de variables.",
    extend="Explica por qué un solo estudio, aunque esté bien hecho, no basta para afirmar que una solución siempre funciona.",
)

# ============================================================ OAC-04, clase 3
F = ("Ficha 16 (balance de carbono de ejemplo para un territorio ficticio, en unidades de ejemplo por año). Emisiones: 100 unidades. Absorción por bosques y océano: 40 unidades. "
     "Escenario A: se reducen las emisiones en 20 unidades. Escenario B: se restauran bosques y la absorción aumenta en 10 unidades. Escenario C: se aplican A y B. "
     "Supuestos del modelo: la absorción no se satura y no hay incendios que liberen carbono.")
build(
    O4, 3, F,
    use="Aprenderé a interpretar un modelo de balance de carbono para comparar soluciones que previenen y reparan. Sirve para ver cómo las emisiones y los sumideros se combinan y qué supuestos hay que revisar.",
    prior=["Sé qué es el dióxido de carbono y de dónde proviene.", "Sé sumar y restar con cantidades.", "Sé qué es un sumidero de carbono."],
    explain=[
        "El carbono circula entre la atmósfera, los seres vivos, el suelo y los océanos. Las fuentes lo liberan, como la quema de combustibles fósiles y los incendios. Los sumideros lo absorben y almacenan, como los bosques, las turberas y el océano. Un balance simple se escribe así: balance = emisiones − absorción. Si es positivo, la cantidad de carbono en la atmósfera aumenta; si es cero, se estabiliza; si es negativo, disminuye.",
        "Las soluciones pueden actuar sobre cualquiera de los dos lados. Prevenir es reducir emisiones. Mejorar la absorción es proteger y restaurar sumideros, lo que se llama una solución basada en la naturaleza. Cada una tiene límites: un bosque tarda años en crecer, los sumideros pueden saturarse y un incendio o la sequía pueden convertirlo en fuente de carbono.",
        "Un modelo numérico como éste sirve para comparar escenarios y para mostrar qué supuestos hay detrás. Los números son de ejemplo y las unidades no corresponden a mediciones reales; lo que importa es el razonamiento. Si un supuesto falla, por ejemplo si hay incendios, el resultado del escenario cambia, y eso debe quedar declarado.",
    ],
    vocab=[("fuente de carbono", "proceso que libera carbono a la atmósfera"), ("sumidero de carbono", "proceso o ecosistema que absorbe y almacena carbono"), ("balance de carbono", "emisiones menos absorción"), ("solución basada en la naturaleza", "acción que usa o restaura ecosistemas para enfrentar un problema"), ("saturación", "punto en que un sumidero ya no puede absorber más")],
    worked=[
        ("Calcular un balance", "En un territorio de ejemplo hay 80 unidades de emisión y 30 de absorción. ¿Cuál es el balance?",
         ["Balance = emisiones − absorción.", "80 − 30 = 50."],
         "50 unidades (positivo: sube el carbono en la atmósfera)"),
        ("Evaluar un supuesto", "Un modelo supone que un bosque absorbe lo mismo cada año. Ocurre un incendio. ¿Qué pasa con el supuesto?",
         ["El incendio libera carbono y destruye árboles.", "El bosque absorbe menos y puede pasar a ser fuente.", "El supuesto deja de cumplirse."],
         "El supuesto falla"),
    ],
    mistakes=[("Pensar que plantar árboles resuelve de inmediato un exceso de emisiones.", "Los árboles tardan años en crecer y absorber; mientras tanto las emisiones siguen.", "Combina reducir emisiones con restaurar sumideros y considera los plazos."),
              ("Creer que un sumidero absorbe sin límite.", "Puede saturarse o convertirse en fuente por incendios o sequías.", "Declara los límites del sumidero en el modelo.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un balance de carbono?", "Las emisiones menos la absorción", "La suma de todo el carbono del planeta", "La cantidad de árboles", "El balance compara lo que se emite con lo que se absorbe."),
        ("{F} ¿Cuál es el balance del territorio sin ningún escenario?", "60", "Emisiones 100 menos absorción 40 dan un balance de 60 unidades."),
        ("=", "{F} ¿Cuál es el balance del escenario A?", "(100-20)-40", "Las emisiones bajan a 80 y la absorción sigue en 40.", " unidades"),
        ("=", "{F} ¿Cuál es el balance del escenario B?", "100-(40+10)", "La absorción sube a 50 y las emisiones siguen en 100.", " unidades"),
        ("=", "{F} ¿Cuál es el balance del escenario C?", "(100-20)-(40+10)", "Las emisiones bajan a 80 y la absorción sube a 50, así que el balance es la diferencia.", " unidades"),
        ("abc", "{F} ¿Cuál escenario deja el menor balance?", "El escenario C", "El escenario A", "El escenario B", "Combinar las dos acciones logra el menor balance, 30 unidades."),
        ("abc", "{F} ¿Qué tipo de acción es la del escenario A?", "Prevenir, porque reduce emisiones", "Reparar un daño ya hecho", "Absorber carbono", "Reducir emisiones evita que más carbono llegue a la atmósfera."),
        ("abc", "{F} ¿Qué tipo de acción es la del escenario B?", "Mejorar los sumideros restaurando bosques", "Reducir emisiones de combustibles", "Prevenir, porque reduce emisiones", "Restaurar bosques aumenta la absorción de carbono en el territorio."),
        ("=", "{F} ¿Cuántas unidades menos tiene el balance del escenario C que el balance inicial?", "60-30", "Se restan el balance de C y el balance inicial para ver la mejora.", " unidades"),
        ("ab", "{F} Un incendio libera 15 unidades de carbono en el territorio. ¿Qué supuesto del modelo falla?", "Que no hay incendios que liberen carbono", "Que las emisiones eran 100", "El modelo dice explícitamente que no hay incendios, así que un incendio rompe ese supuesto."),
        ("abc", "{F} Un estudiante dice que, con el escenario B, el balance será 50 de inmediato. ¿Qué advertencia hace falta?", "Los bosques restaurados tardan años en alcanzar esa absorción", "El balance de B es 100", "Los bosques nunca absorben carbono", "La absorción de un bosque joven crece con los años."),
        ("abc", "¿Cuál es un riesgo de depender solo de bosques como sumideros?", "Que un incendio o una sequía los convierta en fuente de carbono", "Que absorban demasiado agua", "Que no se pueda cuantificar nada", "Los incendios liberan el carbono almacenado."),
        ("abc", "Si el balance de un territorio de ejemplo fuera −10 unidades, ¿qué ocurriría con el carbono de la atmósfera?", "Disminuiría", "Aumentaría", "Quedaría igual", "Un balance negativo significa que se absorbe más de lo que se emite."),
    ],
    ctx=("abc", "Contexto: una región de ejemplo quiere elegir entre reducir emisiones industriales o plantar bosques. ¿Qué recomendación es más sólida según el modelo?", "Combinar ambas, porque reducen emisiones y aumentan absorción, y revisar los plazos y los riesgos", "Plantar bosques y no reducir emisiones", "No hacer ninguna", "El escenario combinado logra el mejor balance, pero hay que cuidar plazos y riesgos."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es una fuente de carbono?", "Un proceso que libera carbono a la atmósfera", "Las fuentes liberan carbono, como la quema de combustibles."),
        ("ab", "Un sumidero de carbono:", "Absorbe y almacena carbono", "Libera siempre carbono", "Los bosques jóvenes absorben carbono mientras crecen."),
        ("ab", "Un modelo debe declarar:", "Sus supuestos y límites", "Que no tiene límites", "Declarar supuestos permite evaluar cuándo falla."),
    ],
    op=("Con la ficha {F}: (1) calcula el balance de cada escenario; (2) ordena los escenarios del mejor al peor; (3) escribe un supuesto del modelo y qué pasaría si dejara de cumplirse.",
        "(1) A: 40; B: 50; C: 30. (2) C, A, B. (3) Supone que no hay incendios; si ocurre uno, el bosque libera carbono y el balance sube.",
        ["tres balances correctos", "orden coherente", "supuesto y consecuencia coherentes"],
        ["tres respuestas numeradas"],
        ["restar al revés", "ordenar sin calcular", "no relacionar el supuesto con una consecuencia"],
        "Pregunta: «¿cuánto tardaría el escenario B en lograr su absorción?»."),
    reinforce="Inventa un balance de carbono para un pueblo de ejemplo y calcula el efecto de una acción que reduzca emisiones y otra que aumente absorción.",
    extend="Explica por qué proteger un bosque maduro puede ser tan importante como plantar un bosque nuevo.",
)

# ============================================================ OAC-04, clase 4
F = ("Ficha 17 (datos de ejemplo, humedal ficticio a los 5 años de iniciar la restauración). Sitio de referencia, sano y sin degradar: 20 especies de plantas nativas y 70 % de cobertura vegetal. "
     "Sitio restaurado: 14 especies de plantas nativas, 56 % de cobertura vegetal y 9 especies de aves. Sitio degradado sin restaurar: 6 especies de plantas nativas, 25 % de cobertura vegetal y 4 especies de aves. "
     "En el sitio restaurado se detectaron 2 especies exóticas que no aparecían en el de referencia.")
build(
    O4, 4, F,
    use="Aprenderé a analizar datos de una restauración ecológica: cuánto se recuperó, qué sigue pendiente y qué dice la evidencia sobre la solución. Sirve para comunicar resultados sin exagerar ni minimizar.",
    prior=["Sé qué es una especie nativa y una exótica.", "Sé calcular porcentajes.", "Sé qué es un grupo de comparación."],
    explain=[
        "La restauración ecológica ayuda a recuperar un ecosistema degradado, dañado o destruido. Se mide comparando tres situaciones: un sitio de referencia, que es el ecosistema sano que se toma como meta; un sitio degradado sin restaurar, que muestra qué pasa sin intervención; y el sitio restaurado. Si el restaurado se acerca al de referencia y se aleja del degradado, hay evidencia de recuperación.",
        "Para medir la recuperación se usan indicadores: número de especies nativas, cobertura vegetal, presencia de aves o de otros grupos, y también procesos como la retención de agua. Un indicador útil es el porcentaje de recuperación respecto del sitio de referencia: valor del sitio restaurado ÷ valor del sitio de referencia × 100. Pero un solo indicador no cuenta toda la historia.",
        "La recuperación suele ser parcial y lenta. Pueden aparecer especies exóticas y algunas funciones tardan más que otras. Por eso se informa qué se logró, qué falta, cuánto tiempo se ha medido y qué se haría para seguir mejorando. Un informe honesto no exagera los éxitos ni oculta los problemas.",
    ],
    vocab=[("restauración ecológica", "ayuda a la recuperación de un ecosistema degradado, dañado o destruido"), ("sitio de referencia", "ecosistema sano que se toma como meta de la restauración"), ("indicador", "medida que resume una característica del ecosistema"), ("recuperación parcial", "mejora que aún no alcanza el estado de referencia"), ("monitoreo", "medición repetida en el tiempo para seguir un cambio")],
    worked=[
        ("Calcular un porcentaje de recuperación", "En un sitio de ejemplo el sitio de referencia tiene 40 especies y el restaurado 30. ¿Qué porcentaje de recuperación logró?",
         ["Se divide 30 entre 40.", "30 ÷ 40 × 100 = 75."],
         "75 %"),
        ("Leer los tres sitios", "Un sitio degradado tiene 5 especies, uno restaurado 12 y uno de referencia 18. ¿El restaurado se acerca a la referencia?",
         ["12 es mayor que 5, así que hay mejora.", "12 es menor que 18, así que falta recuperación."],
         "Sí, pero la recuperación es parcial"),
    ],
    mistakes=[("Declarar que el sitio quedó como nuevo porque mejoró.", "La mejora puede ser parcial y faltan indicadores y años de monitoreo.", "Compara con el sitio de referencia e informa lo que falta."),
              ("Medir solo un indicador y generalizar.", "Un indicador (por ejemplo, plantas) no refleja aves, suelo ni agua.", "Usa varios indicadores y di cuáles no se midieron.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un sitio de referencia?", "Un ecosistema sano que se toma como meta de la restauración", "El sitio más grande de la región", "El sitio donde se hizo la restauración", "Sirve de meta para comparar la recuperación."),
        ("{F} ¿Cuántas especies de plantas nativas tiene el sitio restaurado?", "14", "La ficha indica 14 especies de plantas nativas en el sitio restaurado."),
        ("=", "{F} ¿Cuántas especies de plantas nativas más tiene el sitio restaurado que el degradado?", "14-6", "Se restan las especies del sitio degradado a las del restaurado.", " especies"),
        ("=", "{F} ¿Cuántas especies de aves más tiene el sitio restaurado que el degradado?", "9-4", "Se restan las especies de aves del degradado a las del restaurado.", " especies"),
        ("=", "{F} ¿Qué porcentaje de las especies de plantas nativas del sitio de referencia hay en el sitio restaurado?", "14/20*100", "Se divide el valor del sitio restaurado por el de referencia y se multiplica por cien.", " %"),
        ("=", "{F} ¿Qué porcentaje de la cobertura vegetal del sitio de referencia alcanzó el sitio restaurado?", "56/70*100", "Se divide la cobertura del restaurado por la de referencia y se multiplica por cien.", " %"),
        ("abc", "{F} ¿Qué conclusión sostiene mejor la ficha?", "Hubo una recuperación parcial respecto del sitio de referencia", "El humedal quedó idéntico al de referencia", "La restauración no sirvió", "Los valores del restaurado están entre los del degradado y los de referencia."),
        ("abc", "{F} ¿Qué dato de la ficha debe informarse como problema pendiente?", "Las 2 especies exóticas detectadas en el sitio restaurado", "Las 9 especies de aves", "El 70 % de cobertura de referencia", "Las exóticas pueden competir con las nativas y no estaban en el sitio de referencia."),
        ("ab", "{F} Un informe dice: «La restauración fue un éxito total». ¿Qué falla?", "Los datos muestran recuperación parcial y presencia de especies exóticas", "Nada: el éxito es evidente", "Con estos datos aún falta alcanzar los valores de referencia y hay un problema pendiente."),
        ("abc", "{F} ¿Qué haría más sólida la conclusión sobre la restauración?", "Repetir las mediciones cada año y medir más indicadores", "Medir una sola vez", "Eliminar el sitio de referencia", "El monitoreo repetido muestra si la recuperación continúa."),
        ("abc", "{F} ¿Por qué se mide también el sitio degradado sin restaurar?", "Para saber qué habría pasado sin la intervención", "Para tener un segundo sitio de referencia", "Para reemplazar al sitio de referencia", "Es el grupo de comparación que muestra el efecto de la restauración."),
        ("abc", "{F} Un indicador que no se midió en la ficha y que ayudaría a evaluar la función del humedal es:", "La capacidad de retener agua", "El número de especies de plantas", "La cobertura vegetal", "La ficha mide plantas y aves, pero no la retención de agua, que es una función clave."),
        ("abc", "Si dos años después el sitio restaurado alcanzara 18 especies de plantas nativas, ¿qué diría el porcentaje respecto de las 20 de referencia?", "90 %", "70 %", "100 %", "18 dividido por 20 es 0,9, es decir 90 %."),
    ],
    ctx=("abc", "Contexto: un equipo de ejemplo debe presentar a la comunidad los resultados de cinco años de restauración. ¿Cuál presentación es más honesta?", "Mostrar los tres sitios, la recuperación parcial, las exóticas detectadas y el plan de monitoreo", "Mostrar solo las especies que volvieron", "Decir que está completamente restaurado", "Un informe honesto incluye logros, pendientes y próximos pasos."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es un indicador?", "Una medida que resume una característica del ecosistema", "Los indicadores resumen aspectos como la riqueza de especies."),
        ("ab", "La recuperación parcial significa:", "Hay mejora, pero aún no se alcanza la referencia", "No hubo ninguna mejora", "Se acerca al sitio de referencia sin alcanzarlo."),
        ("ab", "El monitoreo consiste en:", "Medir repetidamente en el tiempo", "Medir una sola vez", "La repetición permite seguir los cambios."),
    ],
    op=("Con la ficha {F}: (1) calcula el porcentaje de recuperación del sitio restaurado en plantas nativas y en cobertura; (2) escribe una conclusión de dos oraciones que declare lo logrado y lo pendiente; (3) propone dos indicadores adicionales y cómo los medirías.",
        "(1) 70 % en plantas nativas y 80 % en cobertura. (2) El sitio restaurado recuperó una parte importante de las plantas y de la cobertura, pero aún no alcanza el sitio de referencia y tiene especies exóticas. (3) Retención de agua, midiendo el nivel antes y después de una lluvia, y número de insectos polinizadores, contados en parcelas fijas.",
        ["dos porcentajes correctos", "conclusión con logros y pendientes", "indicadores y medición coherentes"],
        ["tres respuestas numeradas"],
        ["declarar éxito total", "calcular el porcentaje al revés", "proponer un indicador sin forma de medirlo"],
        "Pregunta: «¿qué haría el equipo con las especies exóticas?»."),
    reinforce="Escribe tres indicadores de recuperación de un bosque y cómo medirías cada uno con datos de ejemplo.",
    extend="Explica por qué la restauración suele ser más lenta y más cara que evitar el daño desde el inicio.",
)

# ============================================================ OAC-04, clase 5
F = ("Ficha 18 (tres soluciones de ejemplo para proteger un valle ante el calentamiento; puntajes de ejemplo de 1 a 5, donde 5 es lo mejor). "
     "Solución 1, restaurar el bosque nativo: eficacia 4, costo 3, riesgo 4, plazo 2, beneficio para la comunidad 4. "
     "Solución 2, una plantación de un solo árbol exótico de rápido crecimiento: eficacia 3, costo 5, riesgo 2, plazo 5, beneficio para la comunidad 3. "
     "Solución 3, corredores de vegetación nativa entre parches de bosque: eficacia 4, costo 4, riesgo 4, plazo 3, beneficio para la comunidad 4. "
     "En la tabla, costo 5 significa el más barato, riesgo 5 significa el menor riesgo y plazo 5 significa el más rápido.")
build(
    O4, 5, F,
    use="Aprenderé a comparar soluciones con una matriz de decisión y a comunicar una recomendación con evidencia, criterios y límites. Sirve para presentar a otras personas una propuesta clara y honesta.",
    prior=["Sé sumar puntajes.", "Sé qué es una variable y un criterio.", "Sé qué es una solución basada en la naturaleza."],
    explain=[
        "Comparar soluciones exige criterios explícitos. Los más usados son la eficacia (cuánto logra), el costo, el riesgo de que falle o cause daños, el plazo en que da resultados y el beneficio para las personas, incluida la equidad. Una matriz de decisión pone las opciones en las filas y los criterios en las columnas, con un puntaje en cada celda. Se pueden sumar los puntajes o darles pesos según la importancia de cada criterio.",
        "Los puntajes de ejemplo son valoraciones, no mediciones. Por eso se declara quién los asignó y con qué datos, y se prueba la sensibilidad: si el orden cambia al modificar un peso, la decisión es frágil. Además, una buena recomendación puede combinar soluciones, porque una compensa los límites de otra, por ejemplo una de resultados rápidos y otra de resultados duraderos.",
        "Comunicar también es parte del trabajo científico. Un mensaje claro tiene una pregunta, el método, la evidencia principal, la conclusión y las limitaciones, y está escrito para quien lo va a leer. Se evitan frases exageradas como «solución definitiva» y se citan las fuentes. Una conclusión que reconoce sus límites es más creíble que una que promete demasiado.",
    ],
    vocab=[("criterio", "aspecto con que se juzga una opción"), ("equidad", "reparto justo de beneficios y costos entre las personas"), ("sensibilidad", "cuánto cambia el resultado al cambiar un supuesto o un peso"), ("recomendación", "propuesta de acción apoyada en evidencia y criterios"), ("limitación", "aspecto que el estudio no permite concluir")],
    worked=[
        ("Sumar con pesos", "Una opción de ejemplo tiene eficacia 4, costo 3 y plazo 2, y la eficacia vale doble. ¿Cuál es su total?",
         ["Eficacia doble: 4 × 2 = 8.", "Costo y plazo se suman una vez: 3 + 2 = 5.", "8 + 5 = 13."],
         "13 puntos"),
        ("Revisar la sensibilidad", "Si una opción gana con puntaje 20 contra 19, pero cambia el orden al duplicar el peso de un criterio, ¿qué se concluye?",
         ["La diferencia inicial es muy pequeña.", "El orden depende de un peso discutible."],
         "Que la decisión es frágil"),
    ],
    mistakes=[("Elegir la solución más barata sin mirar los demás criterios.", "El costo es un solo criterio y una opción barata puede ser poco eficaz o riesgosa.", "Compara todos los criterios y declara los pesos."),
              ("Presentar los puntajes de ejemplo como si fueran datos medidos.", "Son valoraciones y pueden cambiar con nuevos datos.", "Rotúlalos como de ejemplo e indica su origen.")],
    T=[
        ("abc", "En Biología de los ecosistemas: ¿qué es un criterio en una matriz de decisión?", "Un aspecto con que se juzga cada opción", "El nombre de una opción", "El resultado final", "Los criterios, como costo o eficacia, permiten comparar."),
        ("{F} ¿Qué puntaje de eficacia tiene la Solución 2?", "3", "La ficha le asigna 3 puntos de eficacia a la Solución 2."),
        ("=", "{F} ¿Cuál es el total de la Solución 1 sumando sus cinco criterios?", "4+3+4+2+4", "Se suman los puntajes de eficacia, costo, riesgo, plazo y beneficio.", " puntos"),
        ("=", "{F} ¿Cuál es el total de la Solución 2 sumando sus cinco criterios?", "3+5+2+5+3", "Se suman los cinco puntajes de la Solución 2.", " puntos"),
        ("=", "{F} ¿Cuál es el total de la Solución 3 sumando sus cinco criterios?", "4+4+4+3+4", "Se suman los cinco puntajes de la Solución 3.", " puntos"),
        ("abc", "{F} Según la suma simple, ¿qué solución tiene el mayor total?", "La Solución 3", "La Solución 1", "La Solución 2", "La Solución 3 suma 19, la 2 suma 18 y la 1 suma 17."),
        ("abc", "{F} ¿Qué solución es la más rápida en dar resultados?", "La Solución 2", "La Solución 1", "La Solución 3", "Tiene el puntaje 5 en plazo, que significa el más rápido."),
        ("=", "{F} Si la eficacia vale el doble, ¿cuál es el total de la Solución 1?", "4*2+3+4+2+4", "Se duplica el puntaje de eficacia y se suman los otros cuatro criterios.", " puntos"),
        ("=", "{F} Si la eficacia vale el doble, ¿cuál es el total de la Solución 2?", "3*2+5+2+5+3", "Se duplica el puntaje de eficacia y se suman los otros cuatro criterios.", " puntos"),
        ("abc", "{F} Con la eficacia valiendo el doble, ¿qué solución queda con el mayor total?", "La Solución 3", "La Solución 1", "La Solución 2", "Con eficacia doble la 3 suma 23, mientras la 1 y la 2 suman 21 cada una."),
        ("abc", "{F} Una recomendación que combina soluciones podría ser:", "Corredores nativos (3) para resultados a mediano plazo y restauración del bosque (1) para el largo plazo", "Solo la plantación exótica porque es la más barata", "Plantación exótica y restauración del bosque, porque ambas dan resultados rápidos", "Combinar soluciones de plazos distintos compensa los límites de cada una."),
        ("abc", "{F} ¿Qué limitación hay que declarar de esta matriz?", "Los puntajes son de ejemplo y no mediciones", "Que tiene tres soluciones", "Que usa números", "Los puntajes son valoraciones que dependen de quién los asigna y con qué datos."),
        ("abc", "¿Cuál frase comunica mejor una recomendación?", "Recomendamos restaurar el bosque nativo y crear corredores; con puntajes de ejemplo suman más y reducen el riesgo, aunque dan resultados más lentos", "Esta es la solución definitiva para todo", "Elegimos la Solución 2 porque es la más barata, sin más análisis", "Una buena frase incluye recomendación, razón, evidencia y límite."),
    ],
    ctx=("abc", "Contexto: debes presentar ante el concejo de tu comuna una propuesta para proteger un valle. Tienes un minuto. ¿Qué estructura de presentación elegirías?", "Pregunta, evidencia principal, recomendación con sus criterios, y una limitación", "Solo la recomendación sin datos", "Una lista larga de datos sin conclusión", "Una estructura clara y breve permite que el mensaje se entienda y se pueda evaluar."),
    sc=[
        ("En Biología de los ecosistemas: ¿qué es la equidad?", "Un reparto justo de beneficios y costos entre las personas", "La equidad considera quién gana y quién pierde con una solución."),
        ("ab", "Una recomendación apoyada en evidencia debe incluir:", "Criterios, evidencia y limitaciones", "Solo una opinión", "Se evalúa por lo que la sostiene."),
        ("ab", "La sensibilidad de una decisión indica:", "Cuánto cambia el resultado al cambiar un peso o supuesto", "Cuánto cuesta la solución", "Si el orden cambia con pequeños cambios, la decisión es frágil."),
    ],
    op=("Con la ficha {F}: (1) calcula los totales simples de las tres soluciones; (2) elige un criterio que valga doble según tu juicio, justifícalo y recalcula; (3) redacta una recomendación en cuatro oraciones: pregunta, evidencia, conclusión y limitación.",
        "(1) 1: 17; 2: 18; 3: 19. (2) Elijo riesgo doble, porque una falla puede dañar el valle: 1: 21; 2: 20; 3: 23. (3) ¿Qué solución protege mejor el valle? Con puntajes de ejemplo y riesgo doble, la 3 suma más y la 1 la sigue. Recomiendo corredores nativos y restaurar el bosque. Los puntajes son de ejemplo y deberían apoyarse en datos medidos.",
        ["tres totales correctos", "criterio con justificación y recálculo", "recomendación con las cuatro partes"],
        ["tres respuestas numeradas"],
        ["no justificar el peso", "recomendar sin evidencia", "omitir la limitación"],
        "Pregunta: «¿qué dato real cambiaría tu recomendación?»."),
    reinforce="Haz una matriz de dos soluciones para reducir el calor en el patio de tu liceo con cuatro criterios y puntajes de ejemplo.",
    extend="Explica por qué una recomendación que reconoce sus límites puede ser más útil para una comunidad que una que promete resolverlo todo.",
)
