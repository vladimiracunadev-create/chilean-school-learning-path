"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 1 (parte 1): OAD-01, continuidad y cambio en procesos políticos y económicos del siglo XIX. Todas las fuentes y los datos son inventados («de ejemplo») y se leen en papel."""
from __future__ import annotations

from epja_hgcs_nm1_a_common import build, PRIOR_BASE

O = "EPJA-HGCS-NM1-OAD-01"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Un taller de costura de barrio, visto en dos momentos separados por 30 años. "
      "Primer momento (taller familiar): trabajan 4 personas, cosen a mano, la dueña fija el precio de cada prenda y cada persona termina 2 prendas al día. "
      "Segundo momento (fábrica en el mismo lugar): trabajan 40 personas con máquinas, por turnos, la empresa fija el precio y cada persona termina 10 prendas al día. "
      "En los dos momentos se viste a gente del barrio y quienes cosen reciben un pago por su trabajo.")
build(
    O, 1, F1,
    use="Hoy aprendo a mirar dos momentos de la historia y a separar lo que cambió de lo que siguió igual, empezando por situaciones de trabajo que ya conoces.",
    prior=PRIOR_BASE,
    explain=[
        "Cuando comparas tu trabajo de hoy con el de hace diez años, sin pensarlo ya distingues dos cosas: lo que cambió (las herramientas, los horarios, quién decide) y lo que siguió igual (la necesidad de ganarse la vida). Esa mirada es la base de la Historia.",
        "En Historia, un proceso es una serie de cambios que ocurren durante un periodo, y un periodo es un tramo de tiempo con rasgos propios. Analizar continuidad y cambio significa comparar dos momentos de un proceso y decir, con datos, qué se mantuvo y qué se transformó.",
        "Casi nunca cambia todo ni se mantiene todo. Por eso conviene elegir un aspecto concreto (por ejemplo, cómo se organiza el trabajo), mirar los dos momentos y anotar los datos de cada uno. Recién entonces se concluye, y sin inventar lo que la fuente no dice.",
    ],
    vocab=[("cambio", "algo que es distinto entre un momento y otro"), ("continuidad", "algo que se mantiene igual entre un momento y otro"), ("proceso", "serie de cambios que ocurren durante un periodo"), ("periodo", "tramo de tiempo con rasgos propios"), ("aspecto", "tema concreto que se compara: trabajo, gobierno, transporte")],
    worked=[
        ("Separar cambio y continuidad", "{F} Indica un cambio y una continuidad en el trabajo del taller.", ["Comparo el dato de los dos momentos: de 4 personas que cosen a mano se pasa a 40 con máquinas, eso es un cambio.", "Busco algo igual en ambos: en los dos momentos quienes cosen reciben un pago, eso es una continuidad."], "Cambio: se pasa de coser a mano a usar máquinas. Continuidad: se sigue pagando por el trabajo"),
        ("Medir un cambio con datos", "{F} ¿Cuántas prendas por día terminaba el taller familiar en total?", ["El dato dice 4 personas y 2 prendas por persona al día.", "Multiplico 4 por 2 y obtengo 8 prendas al día."], "8 prendas al día"),
    ],
    mistakes=[("Decir «todo cambió» cuando solo cambió la forma de hacer las cosas.", "Se mira lo más llamativo (las máquinas) y se olvida lo que sigue igual (el trabajo pagado).", "Busca siempre al menos una continuidad antes de concluir."),
              ("Dar por cierto que el cambio fue «bueno» o «malo» solo con los datos de cantidad.", "Contar cuántas prendas se hacen no dice nada de las condiciones de trabajo.", "Anota el cambio y pide más datos antes de juzgarlo.")],
    T=[
        ("abc", "{F} ¿Cuál de estas es un cambio entre los dos momentos?", "Quién fija el precio: de la dueña a la empresa", "Se viste a gente del barrio", "Quienes cosen reciben un pago", "En el primer momento fija el precio la dueña y en el segundo la empresa; las otras dos cosas se mantienen."),
        ("ab", "{F} ¿Cuál de estas es una continuidad entre los dos momentos?", "Quienes cosen reciben un pago por su trabajo", "Se pasa de coser a mano a usar máquinas", "El pago por el trabajo aparece en ambos momentos, por eso es continuidad."),
        ("En Historia: ¿cómo se llama lo que se mantiene igual entre un momento y otro?", "Continuidad", "Lo que permanece sin transformarse entre dos momentos se llama continuidad."),
        ("ab", "En Historia: ¿qué es un proceso?", "Una serie de cambios durante un periodo", "Un hecho que ocurre un solo día", "Un proceso se compone de varios cambios encadenados a lo largo del tiempo."),
        ("=", "{F} ¿Cuántas personas más trabajan en el segundo momento que en el primero?", "40-4", "Se restan las personas de ambos momentos para saber cuánto aumentó el número.", " personas"),
        ("=", "{F} En total, ¿cuántas prendas al día terminaba la fábrica del segundo momento?", "40*10", "Se multiplican las personas por las prendas que termina cada una al día.", " prendas al día"),
        ("=", "{F} El taller familiar terminaba 8 prendas al día. ¿Cuántas veces más prendas al día termina la fábrica?", "400//8", "Se divide la producción de la fábrica por la del taller para compararlas.", " veces"),
        ("abc", "{F} ¿Qué aspecto compara la frase «de coser a mano se pasa a usar máquinas»?", "La forma de hacer el trabajo", "El gobierno del país", "El clima del barrio", "Habla de herramientas y de método, es decir, de cómo se organiza el trabajo."),
        ("abc", "{F} Un vecino dice: «El número de personas que cosen se multiplicó por 10». ¿Cómo está ese dato?", "Correcto, porque 40 es 10 veces 4", "Incorrecto, porque solo se duplicó", "Incorrecto, porque no cambió", "En el primer momento hay 4 personas y en el segundo hay 40, que es diez veces más."),
        ("abc", "{F} Una vecina afirma: «No cambió nada, porque en los dos momentos se cose». ¿Qué respuesta se sostiene con la ficha?", "Siguió la costura, pero cambió cómo se cose y quién fija el precio", "Tiene razón, porque la costura sigue siendo la misma", "Cambió todo, porque hay más personas", "La ficha muestra continuidad en la costura y cambios en método, escala y quién decide el precio."),
        ("abc", "{F} ¿Qué conclusión se sostiene mejor con los datos de la ficha?", "El trabajo cambió en método y escala, pero siguió siendo un trabajo pagado", "Todo en el taller cambió por completo", "No hubo ningún cambio entre los dos momentos", "Solo esa conclusión reconoce a la vez lo que cambió y lo que siguió igual."),
        ("ab", "{F} Alguien dice que el cambio fue bueno para quienes cosen. ¿Qué haría falta para decidirlo?", "Más datos, por ejemplo sobre pagos y condiciones de trabajo", "Nada más, porque la ficha ya lo demuestra", "La ficha no entrega pagos ni condiciones, así que no permite juzgar si fue bueno."),
        ("abc", "Para informarte sobre las fábricas del siglo XIX buscas en internet. ¿Qué dato ayuda más a decidir si una página es confiable?", "Quién la publicó y con qué fecha", "Que tenga muchas fotografías", "Que aparezca primera en la búsqueda", "Saber quién publicó y cuándo permite juzgar la fuente; las fotos o el orden no prueban nada."),
    ],
    ctx=("abc", "Antes de una reunión de la junta de vecinos de ejemplo, una vecina compara el transporte del barrio: hace 30 años pasaba una micro sin horario fijo; hoy pasan tres recorridos con horario publicado, y en ambos casos la gente paga el pasaje al subir. ¿Qué es una continuidad?", "Que la gente paga el pasaje al subir", "Que ahora hay tres recorridos", "Que hoy existe un horario publicado", "Se mantiene el pago al subir; el número de recorridos y el horario son cambios."),
    sc=[("En Historia: ¿cómo se define un cambio entre dos momentos?", "Algo que es distinto entre un momento y otro", "Un cambio es una diferencia observable entre dos momentos comparados."),
        ("¿Qué conviene hacer antes de comparar dos momentos?", "Elegir un aspecto concreto, como el trabajo", "Comparar un aspecto concreto evita mezclar temas y confundirse."),
        ("¿Puede haber cambio y continuidad a la vez?", "Sí, casi siempre ocurren juntos", "En un proceso suelen cambiar algunas cosas y mantenerse otras.")],
    op=("Compara dos momentos de algo que conozcas por los datos de esta ficha de ejemplo: «Almacén de barrio. Primer momento: se anota la deuda de cada cliente en un cuaderno, atiende la dueña y se pesa a mano. Segundo momento: 25 años después, se paga con tarjeta o efectivo, atienden la dueña y un empleado, y hay una balanza digital. En ambos momentos los clientes son vecinos y el almacén abre de lunes a sábado». "
        "Escribe dos cambios, dos continuidades y una conclusión de dos frases sobre el aspecto «cómo se atiende al cliente».",
        "Cambios: se pasa del cuaderno de deudas al pago con tarjeta o efectivo; se pasa de pesar a mano a usar balanza digital. Continuidades: los clientes siguen siendo vecinos; abre de lunes a sábado. Conclusión: cambió la forma de cobrar y pesar, pero el almacén siguió siendo un negocio de barrio.",
        ["distingue cambios de continuidades usando solo los datos de la ficha", "elige y nombra un aspecto", "la conclusión reconoce las dos cosas"],
        ["una tabla de dos columnas (cambia, sigue igual) más una conclusión de dos frases"], ["decir que todo cambió", "agregar datos que la ficha no trae"],
        "Pregunta: «¿Eso cambió o se mantuvo? ¿Dónde lo dice la ficha?»."),
    reinforce="Elige algo de tu vida diaria (cómo pagas, cómo te desplazas) y anota un cambio y una continuidad entre hace 20 años y hoy.",
    extend="Explica con un ejemplo por qué decir «todo cambió» o «nada cambió» casi nunca es una buena conclusión histórica.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Tres procesos del siglo XIX descritos en frases breves. "
      "A) Industrialización: en una región se instalan fábricas con máquinas de vapor y miles de familias pasan del campo a la ciudad. "
      "B) Imperialismo: un país europeo toma el control político y económico de territorios lejanos, llamados colonias, para obtener materias primas y vender sus productos. "
      "C) Estado-nación: un territorio con una población que se reconoce como un pueblo, con una misma ley y un mismo gobierno, forma un Estado. "
      "Dato adicional: la Revolución Industrial comenzó en Gran Bretaña a fines del siglo XVIII y se extendió a otros países durante el siglo XIX. "
      "Otros dos datos: en la Conferencia de Berlín (1884-1885), potencias europeas se repartieron zonas de África sin consultar a los pueblos que vivían allí; y Alemania se unificó en 1871 como Estado-nación.")
build(
    O, 2, F2,
    use="Hoy aprendo el vocabulario de tres grandes procesos del siglo XIX (industrialización, imperialismo y Estado-nación) para poder analizarlos después.",
    prior=PRIOR_BASE + ["Sé que un cambio es algo distinto entre dos momentos y que una continuidad es algo que se mantiene."],
    explain=[
        "El siglo XIX va de 1801 a 1900. En ese periodo ocurrieron tres procesos que cambiaron la política y la economía del mundo. Primero, la industrialización: la producción pasó de los talleres a las fábricas con máquinas, y muchas personas se trasladaron del campo a la ciudad para trabajar por un salario.",
        "Segundo, el imperialismo: potencias europeas, como Gran Bretaña, Francia y Alemania, ampliaron su dominio sobre territorios de África y Asia. Un ejemplo conocido es la Conferencia de Berlín de 1884 y 1885, en que potencias europeas se repartieron zonas de África sin consultar a los pueblos que vivían allí. Las colonias entregaban materias primas y compraban productos fabricados.",
        "Tercero, la consolidación de los Estados-nación: Estados que se organizan con una ley, un gobierno y la idea de pertenecer a una misma nación. Alemania, que se unificó en 1871, es un ejemplo. Estos tres procesos se relacionan: las fábricas necesitaban materias primas y mercados, y los Estados fuertes podían sostener el dominio sobre colonias.",
    ],
    vocab=[("industrialización", "paso de la producción artesanal a la de fábricas con máquinas"), ("imperialismo", "dominio político y económico de un país sobre territorios lejanos"), ("colonia", "territorio controlado por otro país"), ("materia prima", "producto natural que se usa para fabricar otros: algodón, cobre, trigo"), ("Estado-nación", "Estado con un gobierno y una ley, cuya población se reconoce como una nación")],
    worked=[
        ("Reconocer el proceso", "{F} ¿A qué proceso corresponde la frase «miles de familias pasan del campo a la ciudad y trabajan en fábricas»?", ["Busco las palabras clave: fábricas y paso del campo a la ciudad.", "En la ficha eso aparece en la industrialización (A)."], "Industrialización"),
        ("Relacionar dos procesos", "{F} ¿Por qué una potencia industrial querría colonias, según la ficha?", ["La ficha dice que las colonias entregan materias primas y compran productos.", "Una fábrica necesita materias primas para producir y mercados para vender."], "Para obtener materias primas y mercados para sus productos"),
    ],
    mistakes=[("Confundir imperialismo con cualquier guerra del siglo XIX.", "Se asocia el término con «conflicto» y no con el control de territorios lejanos.", "Pregunta si un país dominaba política y económicamente a otro territorio."),
              ("Pensar que una nación y un Estado son lo mismo.", "En el uso diario se dice «país» para todo.", "Recuerda: el Estado es la organización política (gobierno y ley); la nación es la idea de pertenecer a un mismo pueblo.")],
    T=[
        ("abc", "{F} ¿Cuál de estos procesos describe el paso de la producción artesanal a fábricas con máquinas?", "La industrialización", "El imperialismo", "El Estado-nación", "La industrialización es el paso a la producción con máquinas en fábricas."),
        ("ab", "En Historia: ¿qué es una colonia?", "Un territorio controlado por otro país", "Una ciudad que fabrica con máquinas", "Una colonia depende política y económicamente de otro país, por eso se llama así."),
        ("{F} ¿En qué país comenzó la Revolución Industrial, según el dato adicional?", "Gran Bretaña", "El dato adicional dice que la Revolución Industrial comenzó en Gran Bretaña."),
        ("abc", "{F} ¿Qué entregaban las colonias a los países que las dominaban?", "Materias primas", "Máquinas de vapor", "Leyes y gobierno propios", "Según la ficha, las colonias entregaban materias primas para las fábricas del país dominante."),
        ("ab", "En Historia: ¿cuál de estas es una materia prima?", "El algodón", "Una camisa ya cosida", "El algodón es un producto natural que se usa para fabricar telas; la camisa es producto terminado."),
        ("=", "{F} El siglo XIX termina en 1900 y empieza en 1801. ¿Cuántos años dura?", "1900-1801+1", "Se cuentan ambos años extremos, por eso se suma uno a la resta.", " años"),
        ("abc", "{F} Un país tiene un gobierno, una ley común y su población se siente parte de un mismo pueblo. ¿Qué es?", "Un Estado-nación", "Una colonia", "Un territorio sin gobierno ni ley común", "Esas tres características son las que define la ficha para un Estado-nación."),
        ("abc", "{F} ¿Por qué se dice que la industrialización y el imperialismo se relacionan?", "Las fábricas necesitaban materias primas y mercados que daban las colonias", "Porque ambos ocurrieron el mismo día", "Porque las colonias inventaron las máquinas", "La relación está en que la industria buscaba materias primas y compradores en territorios dominados."),
        ("abc", "{F} Una persona dice que en la Conferencia de Berlín (1884-1885) los pueblos de África decidieron cómo repartirse sus tierras. ¿Qué dice la ficha?", "Que potencias europeas se repartieron zonas de África sin consultar a esos pueblos", "Que los pueblos de África fueron consultados y aceptaron el reparto", "Que la reunión terminó con la unificación de Alemania", "La ficha dice que las potencias europeas se repartieron zonas de África sin consultar a quienes vivían allí."),
        ("ab", "{F} Un periodista escribe: «Alemania, unificada en 1871, es un ejemplo de Estado-nación». ¿Cómo está esa afirmación?", "Es coherente con la ficha", "Es falsa, porque Alemania era una colonia", "La ficha indica que Alemania se unificó en 1871 como Estado-nación."),
        ("abc", "Una persona afirma: «En el imperialismo, los pueblos de las colonias decidieron voluntariamente quién los gobernaba». ¿Qué dice la definición vista?", "Que otro país tomaba el control político y económico", "Que la colonia elegía a su gobierno", "Que no había ningún control externo", "La definición habla de dominio de un país sobre territorios lejanos, no de decisión voluntaria de las colonias."),
        ("abc", "{F} ¿Qué cambio de vida trajo la industrialización a miles de familias de la ficha?", "Pasaron del campo a la ciudad para trabajar", "Se quedaron en el campo sin cambios", "Dejaron de necesitar ingresos", "La ficha dice que miles de familias pasan del campo a la ciudad."),
        ("abc", "Dos fuentes de ejemplo hablan del mismo proceso. Fuente 1: «Se instalaron fábricas y creció la ciudad». Fuente 2: «Las familias dejaron el campo». ¿Qué proceso tienen en común?", "La industrialización", "El imperialismo", "La consolidación de un Estado-nación", "Ambas fuentes mencionan fábricas y movimiento del campo a la ciudad, rasgos de la industrialización."),
    ],
    ctx=("abc", "Un diario local de ejemplo escribe: «La empresa europea instaló ferrocarriles en la colonia para sacar el cobre hacia el puerto y vender allí sus productos». ¿Qué proceso ilustra?", "El imperialismo", "El Estado-nación", "Un cambio de gobierno interno", "Un país dominaba un territorio lejano para sacar materias primas y vender productos."),
    sc=[("En la Historia del siglo XIX: ¿cómo se define la industrialización?", "Paso de la producción artesanal a la de fábricas con máquinas", "La definición se centra en máquinas, fábricas y producción en masa."),
        ("¿Qué entregaban las colonias a las potencias?", "Materias primas y mercados", "Las colonias abastecían de recursos a la industria del país dominante."),
        ("¿Qué distingue a un Estado-nación?", "Un gobierno, una ley y una población que se reconoce como nación", "Esas tres ideas definen al Estado-nación del siglo XIX.")],
    op=("Escribe tres frases breves, cada una con un proceso distinto (industrialización, imperialismo, Estado-nación), usando esta lista de datos de ejemplo: «una fábrica de telas con máquinas de vapor; una potencia que domina una colonia para sacar algodón; un país con un solo gobierno y una sola ley para todo su territorio». "
        "Después escribe una frase que muestre cómo dos de esos procesos se relacionan.",
        "Industrialización: la fábrica de telas con máquinas de vapor reemplaza el trabajo a mano. Imperialismo: una potencia domina una colonia para sacar algodón. Estado-nación: el país tiene un gobierno y una ley para todo su territorio. Relación: la fábrica de telas necesita el algodón que la potencia saca de la colonia.",
        ["asigna cada dato al proceso correcto", "usa el vocabulario de la clase", "la relación entre dos procesos es lógica"],
        ["tres frases y una frase de relación"], ["confundir imperialismo con guerra", "mezclar Estado y nación sin explicar"],
        "Pregunta: «¿Qué palabra de la definición está en tu frase?»."),
    reinforce="Escribe con tus palabras qué significan industrialización, imperialismo y Estado-nación, en una frase cada una.",
    extend="Explica con un ejemplo por qué una fábrica de telas dependía de materias primas que venían de lejos.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Tabla sobre una región textil ficticia, comparando dos momentos. "
      "Aspecto: producción de telas. Momento 1 (hacia 1780): se hila a mano en las casas, la energía es la fuerza de las personas y de los animales, se vende en la feria local, hay 5 talleres. "
      "Momento 2 (hacia 1860): se hila con máquinas en fábricas, la energía es el vapor, se vende en la región y en puertos lejanos por ferrocarril, hay 5 fábricas grandes. "
      "Aspecto: desigualdad. En ambos momentos quienes son dueños de talleres o fábricas reciben ganancias y quienes trabajan reciben un pago menor.")
build(
    O, 3, F3,
    use="Hoy aprendo un método de cuatro pasos para analizar continuidad y cambio con datos de una tabla, y lo practico con el paso de los talleres a las fábricas.",
    prior=PRIOR_BASE + ["Conozco los procesos de industrialización, imperialismo y Estado-nación y sé que una fuente informa sobre el pasado."],
    explain=[
        "Para analizar continuidad y cambio hay un método simple de cuatro pasos. Paso 1: elige dos momentos y un aspecto. Paso 2: anota qué dice la fuente de cada momento. Paso 3: compara y marca qué cambió y qué se mantuvo. Paso 4: escribe una conclusión corta apoyada en los datos.",
        "Las tablas ayudan porque ponen los datos uno al lado del otro. Mira cada fila (un aspecto) y compara sus dos columnas (los dos momentos). Si dos celdas dicen lo mismo, hay continuidad; si dicen cosas distintas, hay cambio. Aun así, un cambio puede esconder una continuidad más profunda.",
        "Por ejemplo, la tabla dice que se pasó de hilar a mano a hilar con máquinas: cambió la técnica. Pero en ambos momentos los dueños reciben ganancias y quienes trabajan reciben un pago menor: eso es una continuidad de fondo. La conclusión debe nombrar las dos cosas y no sobrepasar lo que dicen los datos.",
    ],
    vocab=[("tabla de comparación", "cuadro con dos momentos lado a lado para ver diferencias y parecidos"), ("técnica", "forma de hacer algo, con ciertas herramientas"), ("energía", "fuerza que mueve las máquinas o el trabajo: personas, animales, vapor"), ("ganancia", "dinero que queda al dueño después de pagar los costos"), ("conclusión", "frase final que resume lo que se concluye con los datos")],
    worked=[
        ("Aplicar los cuatro pasos a un aspecto", "{F} Analiza el aspecto «energía» entre los dos momentos.", ["Paso 1: elijo el aspecto energía y los momentos 1780 y 1860.", "Paso 2: en 1780 la energía es la fuerza de personas y animales; en 1860 es el vapor.", "Paso 3: comparo: la fuente de energía cambió.", "Paso 4: concluyo que cambió la energía: de fuerza de personas y animales a vapor."], "Cambió la energía: de la fuerza de personas y animales al vapor"),
        ("Encontrar una continuidad de fondo", "{F} ¿Qué continuidad hay en el aspecto «desigualdad»?", ["Leo qué dice la ficha en ambos momentos.", "En ambos, los dueños reciben ganancias y quienes trabajan, un pago menor."], "Se mantuvo la diferencia entre dueños y trabajadores"),
    ],
    mistakes=[("Quedarse solo con lo más visible, como las máquinas, y no mirar los otros aspectos.", "Lo llamativo suele tapar rasgos de fondo.", "Revisa cada fila de la tabla y anota si cambió o se mantuvo."),
              ("Escribir una conclusión que dice más que los datos, como «todos vivían peor».", "Se mezcla opinión con evidencia.", "Usa solo los datos de la tabla y marca lo demás como pregunta pendiente.")],
    T=[
        ("abc", "{F} ¿Cuál es el primer paso del método de análisis?", "Elegir dos momentos y un aspecto", "Escribir la conclusión", "Opinar sobre el cambio", "El método empieza por decidir qué momentos y qué aspecto se compararán."),
        ("ab", "{F} En el aspecto «producción de telas», ¿qué cambió entre los dos momentos?", "La técnica: de hilar a mano a hilar con máquinas", "El número de talleres, que subió de 5 a 50", "En la ficha se pasa de hilado a mano en las casas a máquinas en fábricas; el número de unidades es 5 en ambos."),
        ("{F} ¿Qué energía se usa en el momento 2 (hacia 1860)?", "El vapor", "La ficha dice que en el momento 2 la energía es el vapor."),
        ("abc", "{F} ¿Dónde se vende en el momento 1?", "En la feria local", "En puertos lejanos", "Solo en la ciudad capital", "La ficha dice que en el momento 1 se vende en la feria local."),
        ("ab", "{F} Hay 5 talleres en el momento 1 y 5 fábricas grandes en el momento 2. ¿Qué se mantiene en ese dato?", "El número de unidades productivas", "El tamaño de las unidades", "Los dos momentos tienen 5 unidades, aunque las fábricas son más grandes y con máquinas."),
        ("=", "{F} Entre 1780 y 1860 pasaron varios años. ¿Cuántos?", "1860-1780", "Se restan los años de ambos momentos para saber el tiempo transcurrido.", " años"),
        ("abc", "{F} ¿Qué continuidad se observa en el aspecto «desigualdad»?", "Los dueños reciben ganancias y quienes trabajan un pago menor", "Los trabajadores pasan a ser dueños", "Desaparece la diferencia entre dueños y trabajadores", "La ficha muestra esa diferencia en ambos momentos, por eso es continuidad."),
        ("abc", "{F} Una persona concluye: «Con las fábricas se acabaron las diferencias entre dueños y trabajadores». ¿Qué dicen los datos?", "Que la diferencia se mantuvo en ambos momentos", "Que la diferencia desapareció", "Que los trabajadores eran más ricos", "La fila de desigualdad dice lo mismo en los dos momentos, así que la conclusión es falsa."),
        ("abc", "{F} ¿Qué cambio de mercado muestra la tabla entre los dos momentos?", "De venta local a venta regional y en puertos por ferrocarril", "De venta en puertos a venta en la feria", "No cambió el mercado", "Según la ficha, el mercado se amplió gracias al ferrocarril y los puertos."),
        ("abc", "{F} ¿Cuál conclusión usa los datos sin pasarse de lo que dicen?", "Cambiaron la técnica, la energía y el mercado, pero se mantuvo la desigualdad entre dueños y trabajadores", "Todo mejoró para todas las personas de la región", "Nada cambió en la producción de telas", "Esa conclusión se apoya solo en filas de la tabla; las otras afirman más o menos de lo que muestra."),
        ("ab", "{F} Un estudiante dice: «Como cambiaron las máquinas, también cambió la desigualdad». ¿Qué dato lo contradice?", "En ambos momentos hay diferencia entre dueños y trabajadores", "En el momento 2 hay vapor", "La desigualdad aparece sin cambios en la ficha, aunque cambió la técnica."),
        ("abc", "{F} Se agrega un dato: «en 1860 las fábricas emplean mujeres y niños con pagos más bajos». ¿Qué aspecto ayuda a analizar?", "La desigualdad entre quienes trabajan", "La energía de las máquinas", "La distancia al puerto", "El dato muestra diferencias de pago entre quienes trabajan, un tema de desigualdad."),
        ("abc", "{F} ¿Qué pregunta conviene hacer para ampliar el análisis?", "¿Cómo eran las horas de trabajo en los dos momentos?", "¿Qué opinan hoy sobre las máquinas de esa época?", "¿Cuántas fábricas hay hoy en otro país?", "Las horas de trabajo son otro aspecto de las condiciones de vida que se puede comparar."),
    ],
    ctx=("abc", "Un sindicato de ejemplo revisa esta tabla: «Hacia 1850: jornada de 14 horas, se trabaja de lunes a sábado, no hay contrato escrito. Hacia 1900: jornada de 12 horas, se trabaja de lunes a sábado, no hay contrato escrito». ¿Cuál es la continuidad?", "Se trabaja de lunes a sábado y no hay contrato escrito", "La jornada de 14 horas", "La jornada de 12 horas", "Los datos de ambos momentos coinciden en la semana laboral y en la falta de contrato; la jornada cambió."),
    sc=[("¿Cuáles son los cuatro pasos del método de análisis?", "Elegir, anotar, comparar y concluir", "El método ordena el trabajo en cuatro etapas simples."),
        ("Si dos celdas de una tabla dicen lo mismo, ¿qué hay?", "Una continuidad", "Lo que se repite entre momentos es una continuidad."),
        ("¿Qué debe cuidar una conclusión?", "Apoyarse solo en los datos", "No debe decir más de lo que muestra la fuente.")],
    op=("Analiza esta tabla de ejemplo con los cuatro pasos: «Aspecto: transporte de mercaderías. Momento 1 (hacia 1830): carretas tiradas por bueyes, el viaje al puerto dura 6 días, el flete lo cobra un arriero. Momento 2 (hacia 1880): ferrocarril a vapor, el viaje al puerto dura 1 día, el flete lo cobra la empresa ferroviaria. En ambos momentos las mercaderías se llevan al puerto para exportarlas». "
        "Escribe qué cambió, qué se mantuvo y una conclusión de dos frases.",
        "Cambió el medio (de carretas a ferrocarril), el tiempo del viaje (de 6 a 1 día) y quién cobra el flete (de un arriero a una empresa). Se mantuvo que las mercaderías se llevan al puerto para exportarlas. Conclusión: el transporte cambió mucho en técnica y rapidez, pero el objetivo (llegar al puerto) siguió igual.",
        ["aplica los cuatro pasos", "separa cambios de continuidad con datos de la tabla", "la conclusión no sobrepasa los datos"],
        ["dos listas (cambió y se mantuvo) y una conclusión"], ["usar datos que no están", "olvidar la continuidad"],
        "Pregunta: «¿Qué celda de la tabla respalda esa frase?»."),
    reinforce="Aplica los cuatro pasos a un cambio de tu trabajo o tu barrio de los últimos 20 años y escribe una conclusión de una frase.",
    extend="Explica con un ejemplo cómo un cambio de técnica puede esconder una continuidad de fondo.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Dos extractos breves, inventados, sobre una fábrica de telas hacia 1860, y un tercer dato. "
      "Fuente A (carta de la dueña): «Con las máquinas la producción creció y pudimos abrir otro turno. Damos trabajo a 200 familias». "
      "Fuente B (relato de una obrera, recogido años después): «Los turnos eran largos y a las más jóvenes nos pagaban menos. Sin ese sueldo no comíamos en casa». "
      "Fuente C (informe de una autoridad municipal): «La ciudad creció de prisa; faltan viviendas y las calles cercanas a la fábrica se llenan de gente recién llegada del campo».")
build(
    O, 4, F4,
    use="Hoy practico con apoyo la lectura de varias fuentes sobre un mismo proceso, con respeto por cada perspectiva, y aprendo a revisar si una fuente de internet es confiable.",
    prior=PRIOR_BASE + ["Conozco el método de cuatro pasos para analizar continuidad y cambio."],
    explain=[
        "Un mismo proceso se ve distinto según quién lo cuenta. Una dueña de fábrica, una obrera y una autoridad municipal pueden hablar de lo mismo y destacar cosas diferentes. Analizar varias fuentes significa leerlas con respeto, comparar qué dice cada una y preguntarse desde dónde habla su autor.",
        "Para cada fuente conviene anotar cuatro datos: quién la escribió, cuándo, para quién y qué dice con claridad. Luego se separa lo que la fuente afirma como hecho de lo que expresa como opinión. Una persona puede decir la verdad desde su experiencia y aun así mostrar solo una parte del proceso.",
        "Cuando buscas información en internet, aplica las mismas preguntas: ¿quién publica?, ¿cuándo?, ¿cita sus fuentes? Las herramientas digitales son útiles para informarse, pero no reemplazan el análisis. Contrasta siempre al menos dos fuentes antes de concluir.",
    ],
    vocab=[("perspectiva", "punto de vista de quien cuenta algo, según su situación"), ("hecho", "dato que se puede comprobar con evidencia"), ("opinión", "juicio personal sobre algo"), ("testimonio", "relato de una persona sobre lo que vivió"), ("contrastar", "comparar dos o más fuentes para ver en qué coinciden y en qué no")],
    worked=[
        ("Leer una fuente con cuatro preguntas", "{F} Analiza la fuente B: ¿quién la cuenta y qué dice con claridad?", ["Quién: una obrera; cuándo: años después de 1860.", "Dice con claridad: los turnos eran largos y a las más jóvenes se les pagaba menos."], "Una obrera relata turnos largos y pagos menores para las más jóvenes, años después"),
        ("Contrastar dos fuentes", "{F} Compara la fuente A y la fuente B en un punto.", ["La fuente A destaca que la fábrica da trabajo a 200 familias.", "La fuente B destaca que los turnos eran largos y los pagos desiguales.", "Ambas coinciden en que la fábrica era importante para las familias."], "Coinciden en que la fábrica daba ingresos a familias; difieren en cómo valoran las condiciones de trabajo"),
    ],
    mistakes=[("Creer solo en la fuente de la persona con más poder o más educación.", "Se supone que quien escribe mejor dice más verdad.", "Lee todas las perspectivas y compáralas con respeto."),
              ("Descartar un testimonio por ser «solo» un recuerdo.", "Se confunde que sea parcial con que sea falso.", "Úsalo como una perspectiva válida y contrástalo con otras fuentes.")],
    T=[
        ("abc", "{F} ¿Quién escribe la fuente A?", "La dueña de la fábrica", "Una obrera", "Una autoridad municipal", "La ficha dice que la fuente A es una carta de la dueña."),
        ("ab", "{F} ¿Cuál fuente es un testimonio recogido años después?", "La fuente B", "La fuente C", "La fuente B se describe como un relato recogido años después de lo ocurrido."),
        ("En Historia: ¿cómo se llama el punto de vista de quien cuenta algo, según su situación?", "Perspectiva", "Cada persona cuenta desde su situación, y eso se llama perspectiva."),
        ("abc", "{F} ¿Qué dato entrega la fuente A con claridad?", "La fábrica da trabajo a 200 familias", "Los turnos eran largos", "La ciudad creció de prisa", "Ese es el dato escrito en la carta de la dueña; los otros pertenecen a las otras fuentes."),
        ("abc", "{F} ¿Qué problema de la ciudad destaca la fuente C?", "Faltan viviendas", "No hay trabajo", "La fábrica cerró", "La autoridad dice que faltan viviendas y que llega gente del campo."),
        ("ab", "{F} La fuente B dice «a las más jóvenes nos pagaban menos». ¿Cómo conviene tratar esa frase?", "Un dato de su experiencia que habría que contrastar", "Una opinión sin ningún valor histórico", "Es un testimonio con un dato de pago que otras fuentes pueden confirmar o no."),
        ("=", "{F} Si cada una de las 200 familias de la fuente A tiene en promedio 4 personas, ¿cuántas personas dependen de la fábrica?", "200*4", "Se multiplica el número de familias por las personas de cada una.", " personas"),
        ("abc", "{F} ¿En qué coinciden las fuentes A y B?", "En que la fábrica era una fuente de ingresos para las familias", "En que los turnos eran cortos", "En que no faltaban viviendas", "La dueña habla de trabajo para 200 familias y la obrera dice que sin ese sueldo no comían."),
        ("abc", "{F} Una estudiante dice: «Solo vale la fuente A, porque la escribió la dueña». ¿Qué falla en su razonamiento?", "Ignora las otras perspectivas, que muestran otros aspectos del proceso", "Nada, porque la dueña sabe más", "Que la carta no tiene fecha", "Cada fuente muestra una parte; descartar las otras da una imagen incompleta."),
        ("abc", "{F} ¿Cuál es una buena conclusión que respeta las tres perspectivas?", "La fábrica dio ingresos a muchas familias, pero con turnos largos, pagos desiguales y falta de viviendas", "La fábrica fue buena para todas las personas", "La fábrica fue mala para todas las personas", "Solo esa conclusión integra lo que dicen las tres fuentes sin exagerar."),
        ("ab", "{F} Para saber si los pagos desiguales de la fuente B eran generales, ¿qué conviene hacer?", "Buscar otra fuente, como un registro de sueldos", "Suponer que sí eran generales", "Una sola fuente no permite generalizar; hay que contrastar con otra."),
        ("abc", "Buscas en internet sobre fábricas del siglo XIX y encuentras una página sin autor, sin fecha y sin citas. ¿Qué haces?", "La tomas con cautela y contrastas con otras fuentes", "La aceptas porque salió en la búsqueda", "La copias sin leerla", "Una fuente sin autor ni fecha no se puede evaluar, por eso se contrasta con otras."),
        ("abc", "{F} ¿Cómo se debe tratar el testimonio de la obrera en una clase con respeto?", "Como una perspectiva válida que se contrasta con otras fuentes", "Como un dato falso por no venir de la dueña", "Como la única verdad, sin comparar", "Respetar es escuchar la perspectiva sin dejar de contrastarla con otras fuentes."),
    ],
    ctx=("abc", "En un taller de memoria de la junta de vecinos de ejemplo se leen dos relatos sobre la llegada del ferrocarril al pueblo. Un comerciante dice: «Vendimos más porque llegaban productos nuevos». Una arriera dice: «Perdimos el trabajo de llevar la carga». ¿Cómo se analizan bien ambos relatos?", "Como perspectivas distintas del mismo cambio, que se contrastan", "Se elige uno y se descarta el otro", "Se concluye que ninguno dice la verdad", "Ambos hablan desde su situación; juntos muestran que el cambio tuvo ganadores y perdedores."),
    sc=[("¿Qué cuatro datos conviene anotar de una fuente?", "Quién, cuándo, para quién y qué dice", "Esos datos permiten ubicar la fuente y su perspectiva."),
        ("En un análisis de fuentes: ¿para qué sirve contrastarlas?", "Para ver en qué coinciden y en qué no", "Comparar muestra qué datos son más firmes."),
        ("Una página de internet sin autor ni fecha, ¿se acepta directamente?", "No, se contrasta con otras fuentes", "Sin autor ni fecha no se puede juzgar su confiabilidad.")],
    op=("Lee estas dos fuentes de ejemplo sobre una línea de ferrocarril hacia 1880. Fuente 1 (aviso de una empresa): «El tren llega al puerto en un día y baja el precio de transportar el trigo». Fuente 2 (relato de un arriero): «Antes llevábamos el trigo con carretas; con el tren, perdimos el trabajo del camino». "
        "Escribe en cuatro frases: quién habla en cada una, en qué coinciden, en qué se diferencian y qué otra fuente buscarías.",
        "La fuente 1 la escribe una empresa y la 2 un arriero. Coinciden en que el tren cambió el transporte del trigo. Se diferencian en que la empresa destaca el menor precio y el arriero destaca la pérdida de su trabajo. Buscaría un registro de cuántos arrieros quedaron sin empleo o de cuánto bajó el precio.",
        ["identifica quién habla", "compara con respeto ambas perspectivas", "propone una fuente nueva razonable"],
        ["cuatro frases ordenadas"], ["descartar una fuente por quien la escribe", "mezclar opinión y dato"],
        "Pregunta: «¿Desde qué situación habla esta persona y qué parte del cambio muestra?»."),
    reinforce="Si lo deseas, conversa con alguien que haya vivido un cambio en su trabajo (sin anotar su nombre) y escribe qué dice y desde qué situación habla; si prefieres, usa el relato de la ficha 4.",
    extend="Explica con un ejemplo por qué una fuente parcial puede ser útil para la historia.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). País ficticio «Costa Verde», colonia de una potencia europea, entre 1860 y 1900. "
      "1860: Costa Verde exporta algodón, cobre y maderas; compra telas, herramientas y máquinas; las autoridades locales cobran impuestos y deciden en asuntos de la comunidad. "
      "1900: Costa Verde exporta algodón, cobre y maderas en cantidades mucho mayores; compra telas, herramientas y máquinas de la potencia; las decisiones importantes las toma un gobernador enviado desde Europa y las autoridades locales solo ejecutan órdenes. "
      "Dato general: en ambos momentos hay puertos que concentran el comercio y una minoría que controla las exportaciones.")
build(
    O, 5, F5,
    use="Hoy aplico el método de continuidad y cambio a un caso de imperialismo y lo relaciono con la economía de exportación de materias primas de Chile en el siglo XIX.",
    prior=PRIOR_BASE + ["Conozco el vocabulario de industrialización, imperialismo y Estado-nación y el método de cuatro pasos."],
    explain=[
        "El imperialismo se puede analizar con el mismo método. Se eligen dos momentos y aspectos como la economía, el gobierno y el comercio. En un caso ficticio como Costa Verde, la economía de exportación de materias primas se mantiene, pero cambia quién toma las decisiones políticas.",
        "Esto muestra una idea importante: la dominación puede cambiar el gobierno y dejar casi igual la economía de exportación, o al revés. Por eso se analiza cada aspecto por separado. Además, que dos aspectos cambien a la vez no prueba que uno cause al otro: eso se evalúa con evidencia, como veremos más adelante.",
        "Algo parecido ocurre en lo local. Durante el siglo XIX, la economía de Chile exportaba materias primas como trigo, plata y cobre, y después salitre, e importaba productos manufacturados. Chile no era una colonia, pero estaba conectado a un comercio mundial que organizaban potencias industriales. Comparar el caso ficticio con el chileno ayuda a ver continuidades y diferencias.",
    ],
    vocab=[("exportar", "vender productos a otros países"), ("importar", "comprar productos a otros países"), ("producto manufacturado", "producto elaborado en una fábrica a partir de materias primas"), ("gobernador", "autoridad enviada para administrar un territorio"), ("economía de exportación", "economía que depende de vender materias primas al exterior")],
    worked=[
        ("Aspecto económico", "{F} ¿Qué se mantiene en la economía de Costa Verde entre 1860 y 1900?", ["Comparo qué exporta y qué compra en cada fecha.", "En ambas fechas exporta algodón, cobre y maderas, y compra telas, herramientas y máquinas."], "Se mantiene la economía de exportación de materias primas y de compra de manufacturas"),
        ("Aspecto político", "{F} ¿Qué cambió en quién decide?", ["En 1860 las autoridades locales deciden en asuntos de la comunidad.", "En 1900 decide un gobernador enviado desde Europa y las autoridades locales ejecutan órdenes."], "Cambió el poder de decisión: pasó de autoridades locales a un gobernador europeo"),
    ],
    mistakes=[("Pensar que si la economía no cambió, el imperialismo no tuvo efectos.", "Se mira un solo aspecto y se concluye sobre todo el proceso.", "Revisa por separado la economía, el gobierno y el comercio."),
              ("Usar «colonia» para cualquier país que vende materias primas.", "Se mezcla dominio político con comercio exterior.", "Una colonia está bajo el control político de otro país; Chile en el siglo XIX no lo estaba.")],
    T=[
        ("abc", "{F} ¿Qué exporta Costa Verde en 1860?", "Algodón, cobre y maderas", "Telas, herramientas y máquinas", "Solo oro", "La ficha dice que exporta algodón, cobre y maderas; telas y máquinas las compra."),
        ("ab", "En Historia: ¿qué significa exportar?", "Vender productos a otros países", "Comprar productos de otros países", "Exportar es vender hacia el exterior; comprar del exterior es importar."),
        ("{F} ¿Quién toma las decisiones importantes en 1900?", "Un gobernador enviado desde Europa", "La ficha dice que en 1900 decide un gobernador enviado desde Europa."),
        ("abc", "{F} ¿Qué cambió entre 1860 y 1900 en Costa Verde?", "Quién toma las decisiones políticas", "Qué materias primas exporta", "Que haya puertos con comercio", "Las otras dos cosas se mantienen; el poder de decisión pasó a un gobernador europeo."),
        ("ab", "{F} ¿Qué se mantuvo entre 1860 y 1900?", "La compra de telas, herramientas y máquinas", "La autoridad que decide los asuntos importantes", "La lista de productos comprados es la misma en las dos fechas."),
        ("abc", "{F} Una persona dice: «En 1900, Costa Verde exporta menos que en 1860». ¿Qué dice la ficha?", "Que exporta los mismos productos en cantidades mucho mayores", "Que exporta menos", "Que dejó de exportar", "La ficha afirma que las cantidades de 1900 son mucho mayores."),
        ("abc", "{F} ¿Qué relación hay entre lo que exporta y lo que importa?", "Vende materias primas y compra productos manufacturados", "Vende máquinas y compra algodón", "No compra ni vende nada", "Esa relación entre materias primas y manufacturas es la que describe la ficha."),
        ("abc", "{F} ¿Qué dato de la ficha se mantiene como continuidad social?", "Una minoría controla las exportaciones", "El gobernador es de la región", "La mayoría controla las exportaciones", "El dato general dice que en ambos momentos una minoría controla las exportaciones."),
        ("abc", "Un docente de ejemplo dice: «Chile fue una colonia de Gran Bretaña en el siglo XIX porque vendía materias primas». ¿Qué error hay?", "Chile no era colonia: era un Estado independiente que exportaba materias primas", "Ninguno, porque exportar es ser colonia", "Que Chile no exportaba nada", "Exportar materias primas no es ser colonia; la colonia está bajo el control político de otro país."),
        ("ab", "En el siglo XIX, la economía de Chile exportaba trigo, plata y cobre y después salitre, e importaba manufacturas. ¿Qué se parece al caso de Costa Verde?", "Ambos exportan materias primas e importan manufacturas", "Ambos están gobernados por un gobernador europeo", "La semejanza está en la economía de exportación; en lo político, Chile era independiente."),
        ("abc", "{F} ¿Qué conclusión se sostiene con la ficha?", "La economía de exportación siguió igual, pero cambió quién gobernaba", "Todo cambió, también la economía", "Nada cambió en el gobierno", "Esa conclusión separa el aspecto económico del político y respeta los datos."),
        ("abc", "{F} Se propone afirmar que el dominio europeo causó que las exportaciones crecieran. ¿Qué falta?", "Más evidencia, porque los datos solo muestran que ambos ocurrieron", "Nada: se prueba solo con la ficha", "Ningún dato: es obvio", "Que dos cosas ocurran a la vez no prueba que una cause la otra."),
        ("abc", "{F} El primer ferrocarril de Chile, entre Caldera y Copiapó (1851), llevaba minerales hacia el puerto. ¿Qué rasgo de Costa Verde se parece a ese caso?", "Una economía de exportación que movía materias primas hacia los puertos", "Un gobernador enviado desde Europa que decidía todo", "Autoridades locales sin ninguna decisión sobre el comercio", "El tren de Chile servía a una economía exportadora, igual que los puertos de Costa Verde; la diferencia es que Chile era un Estado independiente."),
    ],
    ctx=("abc", "Una asociación de ejemplo de ex trabajadores del cobre compara dos épocas: «Hacia 1860, el cobre se exportaba por puertos y la ganancia quedaba mayormente en manos de pocos dueños. Hoy, el cobre se sigue exportando y las ganancias se discuten en la sociedad». ¿Qué continuidad señala?", "La exportación de cobre sigue siendo importante", "El cobre dejó de venderse", "Hoy el cobre solo se vende dentro del país", "El cobre se exportaba antes y se exporta hoy; lo que cambia es cómo se discute su ganancia."),
    sc=[("¿Qué significa importar?", "Comprar productos de otros países", "Importar es traer productos desde el exterior."),
        ("En el imperialismo: ¿cómo se define una colonia?", "Un territorio controlado por otro país", "En una colonia las decisiones importantes las toma el país dominante."),
        ("¿Cambiar el gobierno cambia por sí solo la economía?", "No necesariamente, hay que revisar cada aspecto", "Cada aspecto se analiza con sus propios datos.")],
    op=("Dos fichas de ejemplo para analizar. Ficha 1: «Puerto de Alba, 1850: se exportan cueros y trigo; el trabajo de carga lo hacen jornaleros a mano; el puerto lo administra un gobierno regional». Ficha 2: «Puerto de Alba, 1900: se exportan cueros, trigo y minerales; hay grúas a vapor y un muelle de fierro; el puerto lo administra una empresa extranjera». "
        "Elige el aspecto «economía» y el aspecto «quién administra». Escribe qué cambió y qué se mantuvo en cada uno, y una conclusión.",
        "Economía: se mantienen las exportaciones de cueros y trigo; cambia que se agregan minerales y que se usan grúas a vapor. Administración: cambia, pues pasa de un gobierno regional a una empresa extranjera. Conclusión: el puerto siguió siendo exportador de materias primas, pero cambió su técnica y quién lo administraba.",
        ["separa dos aspectos", "usa solo datos de las fichas", "la conclusión integra cambio y continuidad"],
        ["una tabla con dos filas (aspectos) y una conclusión de dos frases"], ["mezclar aspectos", "inventar datos"],
        "Pregunta: «¿Esto sucede en la economía o en la administración?»."),
    reinforce="Anota dos materias primas y dos productos manufacturados que uses en tu vida diaria, y di cuáles de cada tipo podrían venir de otro país.",
    extend="Explica por qué exportar materias primas puede hacer que una economía dependa de lo que pase en otros países.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Tres hechos del siglo XIX para ordenar y analizar. "
      "1) Hacia 1780 se hila a mano en las casas y a fines del siglo XVIII comienza en Gran Bretaña la Revolución Industrial. "
      "2) En 1871 Alemania se unifica como Estado-nación. "
      "3) En 1884 y 1885, en la Conferencia de Berlín, potencias europeas se reparten zonas de África. "
      "Resumen de ejemplo para evaluar: «El siglo XIX fue solo de cambios: nada se mantuvo entre el comienzo y el final».")
build(
    O, 6, F6,
    use="Hoy reviso lo que logré, ordeno hechos en el tiempo, evalúo una conclusión y decido qué quiero repasar o seguir estudiando.",
    prior=PRIOR_BASE + ["He practicado el método de cuatro pasos y el análisis de fuentes con distintas perspectivas."],
    explain=[
        "Para cerrar un análisis de continuidad y cambio se revisan cuatro cosas: ¿los hechos están ordenados en el tiempo?, ¿cada afirmación tiene un dato que la respalda?, ¿se nombró tanto lo que cambió como lo que se mantuvo?, ¿se usaron al menos dos fuentes? Si falta alguna, se corrige antes de concluir.",
        "Ordenar hechos en una línea de tiempo ayuda a ver el proceso completo: la industrialización comienza en Gran Bretaña a fines del siglo XVIII y se extiende durante el XIX; la unificación de Alemania ocurre en 1871; el reparto de África se discute en la Conferencia de Berlín de 1884 y 1885. Esos hechos no ocurren aislados: forman parte de procesos largos.",
        "Una buena conclusión es breve, usa palabras como «se mantuvo» y «cambió», y reconoce sus límites: si una fuente no dice algo, no se afirma. Al terminar, también conviene decidir qué repasar: términos, el método o el uso de fuentes en internet.",
    ],
    vocab=[("línea de tiempo", "esquema que ordena hechos según su fecha"), ("revisar", "volver sobre lo hecho para corregirlo o confirmarlo"), ("límite de una fuente", "lo que una fuente no permite afirmar"), ("síntesis", "resumen breve de lo más importante"), ("evaluar", "juzgar con criterios si algo está bien apoyado")],
    worked=[
        ("Ordenar hechos", "{F} Ordena de lo más antiguo a lo más reciente los hechos 1, 2 y 3.", ["Anoto la fecha de cada hecho: fines del siglo XVIII, 1871 y 1884-1885.", "Ordeno por fecha: 1, luego 2, luego 3."], "1, 2, 3 (de la Revolución Industrial a la unificación alemana y luego a la Conferencia de Berlín)"),
        ("Evaluar un resumen", "{F} Evalúa el resumen: «El siglo XIX fue solo de cambios».", ["Busco si se nombraron continuidades: el resumen no menciona ninguna.", "Ningún proceso cambia por completo: se mantiene algo."], "El resumen exagera: falta reconocer lo que se mantuvo"),
    ],
    mistakes=[("Concluir sin revisar las fuentes ni los límites.", "Se quiere terminar rápido y se omite la revisión.", "Usa la lista de cuatro preguntas antes de cerrar."),
              ("Mezclar fechas sin ordenarlas, lo que cambia el sentido del proceso.", "No se usa una línea de tiempo.", "Ordena siempre los hechos por fecha antes de explicar.")],
    T=[
        ("abc", "{F} ¿Cuál hecho de la ficha es el más antiguo?", "El inicio de la Revolución Industrial a fines del siglo XVIII", "La unificación de Alemania", "La Conferencia de Berlín", "Fines del siglo XVIII es anterior a 1871 y a 1884-1885."),
        ("ab", "En Historia: ¿para qué sirve una línea de tiempo?", "Para ordenar hechos según su fecha", "Para decidir quién tiene razón", "La línea de tiempo muestra el orden y la duración de los hechos."),
        ("{F} ¿En qué año se unifica Alemania según la ficha?", "1871", "La ficha indica que Alemania se unifica en 1871."),
        ("abc", "{F} ¿Qué dos años marcan la Conferencia de Berlín en la ficha?", "1884 y 1885", "1871 y 1884", "1780 y 1860", "La ficha dice que la Conferencia fue en 1884 y 1885."),
        ("=", "{F} ¿Cuántos años pasan entre la unificación de Alemania (1871) y el comienzo de la Conferencia de Berlín (1884)?", "1884-1871", "Se restan las fechas para conocer los años que separan los hechos.", " años"),
        ("ab", "{F} ¿Qué hecho pertenece al proceso de imperialismo?", "La Conferencia de Berlín", "La unificación de Alemania", "El reparto de zonas de África por potencias es un hecho del imperialismo."),
        ("abc", "{F} ¿A qué proceso pertenece el hecho 2 (1871)?", "La consolidación de un Estado-nación", "El imperialismo", "La industrialización", "La unificación de Alemania es un ejemplo de Estado-nación."),
        ("abc", "{F} El resumen dice que «nada se mantuvo». ¿Qué corrección se sostiene?", "Se mantuvo, por ejemplo, que potencias y Estados siguieron buscando materias primas y mercados", "Todo se mantuvo igual", "No hubo cambios en el siglo XIX", "Un resumen justo reconoce a la vez cambios y continuidades; la corrección propone una continuidad razonable."),
        ("abc", "{F} ¿Qué hecho de la ficha ocurrió inmediatamente después de la unificación de Alemania?", "La Conferencia de Berlín (1884-1885)", "El comienzo de la Revolución Industrial", "El hilado a mano en las casas hacia 1780", "La Conferencia de Berlín es de 1884-1885, posterior a 1871; los otros dos hechos son anteriores."),
        ("ab", "{F} Para concluir bien sobre el siglo XIX, ¿qué falta además de estos tres hechos?", "Más fuentes y datos sobre lo que se mantuvo", "Nada, bastan tres hechos", "Tres hechos aislados no permiten concluir sobre todo un siglo."),
        ("abc", "Revisas tu propio análisis. ¿Cuál de estas preguntas sirve de verdad para revisarlo?", "¿Cada afirmación tiene un dato que la respalda?", "¿Es muy largo el texto?", "¿Usé palabras difíciles?", "Verificar que cada afirmación tenga respaldo es el corazón de la revisión."),
        ("abc", "Un compañero de ejemplo escribe: «La industrialización hizo que Alemania se unificara en 1871». ¿Qué conviene preguntarle?", "¿Qué evidencia muestra que una cosa causó la otra?", "¿Por qué escribe con lápiz?", "¿Cuántas palabras usó?", "Una relación de causa necesita evidencia; ocurrir en la misma época no basta."),
        ("abc", "Terminas la clase y piensas qué repasar. ¿Cuál es la mejor decisión?", "Repasar los términos o los pasos que más me costaron", "No repasar nada porque ya terminé", "Repasar solo lo que ya sé muy bien", "Decidir con base en lo que costó hace útil el estudio siguiente."),
    ],
    ctx=("abc", "Una dirigente de la junta de vecinos de ejemplo prepara un resumen para una charla: «Desde el siglo XIX cambió el transporte, cambió el trabajo y cambió el gobierno, pero se mantuvo que el pueblo vive de la exportación de su cobre». ¿Qué logra bien este resumen?", "Nombra cambios y una continuidad", "Solo enumera cambios", "Solo cuenta lo que se mantuvo", "El resumen incluye lo que cambió y lo que se mantuvo, como pide una buena conclusión."),
    sc=[("¿Qué debe tener una buena conclusión?", "Cambios, continuidades y datos que la respalden", "Una conclusión sólida es breve y está apoyada en la fuente."),
        ("En Historia: ¿qué ayuda a hacer una línea de tiempo con los hechos?", "Para ordenar hechos por fecha", "Ordenar evita confundir el antes y el después."),
        ("¿Qué hago si una fuente no dice algo?", "No lo afirmo y lo anoto como pregunta", "No se debe afirmar lo que la fuente no entrega.")],
    op=("Elabora una síntesis con esta ficha de ejemplo: «Hacia 1840 un pueblo vive de la agricultura y el trabajo se hace a mano; hacia 1900 llegó el ferrocarril, se instaló una fábrica de conservas y hay más gente que vende su trabajo por un sueldo. En ambos momentos el pueblo sigue dependiendo de vender lo que produce a mercados lejanos». "
        "Escribe: una línea de tiempo con dos fechas, dos cambios, una continuidad, una conclusión de dos frases y una frase que diga qué repasarás.",
        "Línea: 1840 (agricultura a mano) y 1900 (ferrocarril y fábrica). Cambios: llegó el ferrocarril y se instaló una fábrica de conservas; hay más trabajo asalariado. Continuidad: el pueblo sigue dependiendo de vender a mercados lejanos. Conclusión: el pueblo cambió su forma de producir y de trabajar, pero siguió ligado a mercados lejanos. Repasaré cómo separar cambio y continuidad.",
        ["ordena con una línea de tiempo", "separa cambios y continuidades con datos", "reflexiona sobre qué repasar"],
        ["una línea de tiempo, dos listas y dos frases"], ["omitir la continuidad", "inventar datos"],
        "Pregunta: «¿Qué dato respalda cada frase de tu conclusión?»."),
    reinforce="Haz una línea de tiempo con tres hechos de tu vida laboral o de tu barrio y escribe un cambio y una continuidad entre el primero y el último.",
    extend="Explica con un ejemplo por qué dos hechos que ocurren en la misma época no siempre tienen una relación de causa.",
)
