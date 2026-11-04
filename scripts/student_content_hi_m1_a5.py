"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 05 (industrialización, trabajo, ciudad y comunicaciones)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 05"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (siglo XIX: años 1801 a 1900). "
     "Industrialización: paso de una producción artesanal y agrícola a una producción con máquinas y fábricas. Comenzó en Gran Bretaña en la segunda mitad del siglo XVIII y se extendió después a otras regiones. "
     "Trabajo asalariado: trabajo por el que se recibe un salario. "
     "Burguesía industrial: dueños de fábricas y capital. Proletariado: personas que no tienen fábricas ni tierras y viven de su salario. "
     "Hitos: máquina de vapor perfeccionada por James Watt, patente de 1769; ferrocarril Liverpool–Manchester, 1830; telégrafo submarino entre Europa y América, 1866; teléfono, 1876; primer ferrocarril de Chile (Caldera–Copiapó), 1851.")
build(
    OA, 1, F,
    use="Aprenderé a situar el proceso de industrialización en el tiempo y en el espacio, y a plantear la pregunta que guía este tema: ¿cómo cambió la industrialización el trabajo, la ciudad y las comunicaciones?",
    prior=["Sé qué es la idea de progreso en el siglo XIX.", "Sé qué es la burguesía.", "Sé calcular diferencias entre años."],
    explain=[
        "La industrialización es el paso de una producción artesanal y agrícola a una producción con máquinas y fábricas. Comenzó en Gran Bretaña en la segunda mitad del siglo XVIII y se extendió durante el siglo XIX a otras regiones. Un símbolo es la máquina de vapor, que usa carbón para mover máquinas y trenes y cambió la forma de producir y de transportar.",
        "Con las fábricas se expandió el trabajo asalariado: las personas trabajaban para un dueño a cambio de un salario. Surgieron dos grupos sociales: la burguesía industrial, que era dueña de fábricas y capital, y el proletariado, formado por personas que no tienen fábricas ni tierras y viven de su salario. Este cambio de modo de producción también transformó la vida familiar y las ciudades.",
        "También cambiaron el transporte y las comunicaciones. El ferrocarril acortó viajes, el telégrafo permitió enviar mensajes en minutos y el teléfono permitió hablar a distancia. En Chile la industrialización fue más lenta, pero el ferrocarril llegó pronto a las zonas mineras. Hay que evitar el error de pensar que todos los países se industrializaron al mismo tiempo y de la misma manera.",
    ],
    vocab=[("industrialización", "paso de la producción artesanal y agrícola a la producción con máquinas y fábricas"), ("trabajo asalariado", "trabajo por el que se recibe un salario"), ("proletariado", "personas que viven de su salario porque no tienen fábricas ni tierras"), ("modo de producción", "forma en que una sociedad organiza el trabajo y los recursos"), ("telégrafo", "aparato que envía mensajes por señales eléctricas")],
    worked=[
        ("Calcular una diferencia", "¿Cuántos años pasaron entre el ferrocarril Liverpool–Manchester (1830) y el primer ferrocarril de Chile (1851)?", ["Tomo los dos años de la ficha.", "Resto: 1851 − 1830 = 21."], "21 años"),
        ("Ubicar en el siglo", "¿A qué siglo pertenece la patente de la máquina de Watt (1769)?", ["El siglo XVIII va de 1701 a 1800.", "El año 1769 está en ese tramo."], "Siglo XVIII"),
    ],
    mistakes=[("Decir que todos los países se industrializaron a la vez.", "El proceso partió en Gran Bretaña y se extendió a ritmos distintos.", "Pregunta cuándo y dónde llegó a cada lugar."),
              ("Confundir burguesía industrial y proletariado.", "Una es dueña de fábricas y capital; el otro vive de su salario.", "Define cada grupo por lo que posee.")],
    T=[
        ("{F} ¿Dónde comenzó la industrialización?", "En Gran Bretaña", "La ficha lo indica."),
        ("{F} ¿Qué es el trabajo asalariado?", "Trabajo por el que se recibe un salario", "La ficha lo define."),
        ("{F} ¿Qué grupo social vive de su salario porque no tiene fábricas ni tierras?", "El proletariado", "La ficha lo define así."),
        ("=", "{F} ¿Cuántos años pasaron entre la patente de la máquina de Watt y el ferrocarril Liverpool–Manchester?", "1830-1769", "Se resta el año de la patente al del ferrocarril.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el telégrafo submarino y el teléfono?", "1876-1866", "Se resta el año del telégrafo al del teléfono.", " años"),
        ("{F} ¿Qué hito es más reciente? A) El teléfono B) El telégrafo submarino", "A) El teléfono", "1876 es posterior a 1866."),
        ("{F} Una fábrica contrata personas que trabajan por un salario diario. ¿Qué tipo de trabajo es? A) Trabajo asalariado B) Trabajo artesanal por cuenta propia", "A) Trabajo asalariado", "Reciben un salario del dueño."),
        ("{F} Una persona es dueña de una fábrica y de sus máquinas. ¿A qué grupo pertenece? A) Burguesía industrial B) Proletariado", "A) Burguesía industrial", "Es dueña de fábricas y capital."),
        ("{F} Un obrero textil no tiene tierras ni fábrica y vive de su sueldo. ¿A qué grupo pertenece? A) Proletariado B) Burguesía industrial", "A) Proletariado", "Vive de su salario."),
        ("{F} ¿Por qué el ferrocarril y el telégrafo transformaron las comunicaciones?", "Porque acortaron los viajes y permitieron enviar mensajes en minutos", "Mejoraron la velocidad de personas y mensajes."),
        ("{F} Un compañero dice: «Chile se industrializó al mismo tiempo que Gran Bretaña». Corrígelo.", "La industrialización comenzó en Gran Bretaña en el siglo XVIII y llegó a otras regiones después", "La ficha muestra distintos ritmos."),
        ("{F} ¿Cuál es la mejor pregunta histórica? A) ¿Cómo cambiaron el trabajo, la ciudad y las comunicaciones con la industrialización? B) ¿Qué máquina era la más pesada?", "A) ¿Cómo cambiaron el trabajo, la ciudad y las comunicaciones con la industrialización?", "La A se responde con hechos y causas."),
        ("{F} Una línea de tiempo usa 1 cm = 20 años y va de 1760 a 1880. ¿Cuántos centímetros mide?", "6 cm", "Se divide el tramo de 120 años por 20."),
    ],
    ctx=("Una exposición titula: «La industrialización llegó a todos los países en 1800». ¿Qué problema tiene? A) Ignora que partió en Gran Bretaña y llegó a ritmos distintos B) Usa un siglo equivocado", "A) Ignora que partió en Gran Bretaña y llegó a ritmos distintos", "La ficha muestra distintos años."),
    sc=[("¿Qué es la industrialización?", "El paso a una producción con máquinas y fábricas", "Así se define."),
        ("¿Qué grupo es dueño de fábricas y capital?", "La burguesía industrial", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1851 y 1866?", "1866-1851", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1760 a 1880 con escala 1 cm = 20 años y marca: patente de Watt (1769), Liverpool–Manchester (1830), Caldera–Copiapó (1851), telégrafo submarino (1866) y teléfono (1876). Debajo escribe dos frases: una que defina industrialización y otra que defina proletariado. {F}",
        "Posiciones desde 1760: 0,45; 3,5; 4,55; 5,3; 5,8 cm. Frases: «La industrialización es el paso a una producción con máquinas y fábricas»; «El proletariado vive de su salario porque no tiene fábricas ni tierras».",
        ["respeta la escala", "los cinco hitos bien ubicados", "las definiciones son correctas"], ["línea de tiempo", "dos frases"], ["no medir con la escala", "confundir proletariado con burguesía"],
        "Pide que explique por qué las comunicaciones también cambiaron el trabajo."),
    reinforce="Explica en voz alta qué es la industrialización y quiénes son la burguesía industrial y el proletariado.",
    extend="Busca en tu casa un objeto hecho en fábrica y piensa cómo se habría hecho antes.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, registro de una fábrica textil, 1850: «Jornada de 13 horas, de lunes a sábado. Salario diario de un obrero adulto: 2 monedas de ejemplo. Salario diario de una mujer: 1 moneda de ejemplo. Salario diario de un niño de diez años: medio moneda de ejemplo.» "
     "Fuente B, informe de un médico sobre un barrio obrero, 1850: «Seis personas duermen en una pieza sin ventana. No hay agua potable en las calles y las enfermedades se propagan con rapidez.»")
build(
    OA, 2, F,
    use="Aprenderé a contextualizar y comparar fuentes sobre el trabajo y la vida en la ciudad industrial: quién las escribe, cuándo y para qué.",
    prior=["Sé qué es el proletariado y el trabajo asalariado.", "Sé contextualizar una fuente.", "Sé calcular multiplicaciones simples."],
    explain=[
        "Un registro de fábrica es una fuente administrativa: la escribe el dueño o un administrador para llevar cuentas. Informa jornadas y salarios, pero no incluye lo que sentían los trabajadores. Un informe de médico es una fuente de observación: describe lo que vio en un barrio, con un propósito de alertar sobre la salud pública.",
        "Las dos fuentes se complementan. El registro muestra que la jornada era larga y que mujeres y niños recibían salarios menores. El informe muestra que las viviendas eran estrechas y sin agua potable. Con ambas se puede explicar que la vida en la ciudad industrial era dura para muchos obreros. Cada fuente tiene límites: son de una fábrica y de un barrio.",
        "Con datos numéricos se puede calcular. Si la jornada diaria es de 13 horas y se trabaja seis días, en una semana son 78 horas. Calcular ayuda a comprender la dimensión del trabajo, pero no basta para evaluar: hay que comparar con otras fuentes y no generalizar a todas las fábricas.",
    ],
    vocab=[("registro", "documento donde se anotan datos de manera ordenada"), ("jornada", "horas que se trabajan en un día"), ("salario diario", "pago por un día de trabajo"), ("salud pública", "cuidado de la salud de toda la población"), ("barrio obrero", "zona de la ciudad donde viven trabajadores de fábricas")],
    worked=[
        ("Calcular horas semanales", "Según la Fuente A, ¿cuántas horas trabaja una persona en una semana?", ["Jornada de 13 horas, de lunes a sábado: 6 días.", "Multiplico: 13 × 6 = 78."], "78 horas"),
        ("Comparar salarios", "¿Cuántas veces más gana un obrero adulto que una mujer?", ["Obrero: 2 monedas. Mujer: 1 moneda.", "2 ÷ 1 = 2."], "El doble"),
    ],
    mistakes=[("Concluir que todas las fábricas pagaban igual.", "El registro es de una sola fábrica.", "Escribe «en esta fábrica» y compara con otras fuentes."),
              ("Tomar el informe médico como la opinión de los obreros.", "Lo escribe un médico, no un obrero.", "Pregunta quién habla.")],
    T=[
        ("{F} ¿Qué tipo de fuente es la Fuente A?", "Un registro de una fábrica textil", "La ficha lo presenta así."),
        ("{F} ¿Cuántas horas dura la jornada según la Fuente A?", "13 horas", "El registro lo dice."),
        ("{F} ¿Quién escribe la Fuente B?", "Un médico", "La ficha lo indica."),
        ("=", "{F} En otra fábrica de ejemplo la jornada es de 12 horas, de lunes a sábado. ¿Cuántas horas se trabajan por semana?", "12*6", "Se multiplica la jornada por los seis días.", " horas"),
        ("=", "{F} ¿Cuántas horas más se trabajan en una semana de 6 días de 13 horas que en una de 5 días de 8 horas?", "13*6-8*5", "Se calcula 13 × 6 = 78 y 8 × 5 = 40, y se restan.", " horas"),
        ("{F} ¿Quién gana menos por día en la fábrica? A) Un niño de diez años B) Una mujer", "A) Un niño de diez años", "Gana medio moneda, menos que la mujer (1)."),
        ("{F} ¿Qué problema de salud pública destaca el médico? A) Falta de agua potable y viviendas estrechas B) Falta de escuelas", "A) Falta de agua potable y viviendas estrechas", "El informe lo señala."),
        ("{F} ¿Qué frase es una descripción de la Fuente B? A) Seis personas duermen en una pieza sin ventana B) Los obreros no se esforzaban por vivir mejor", "A) Seis personas duermen en una pieza sin ventana", "La B es un juicio que el texto no hace."),
        ("{F} Si cada día de trabajo el obrero adulto gana 2 monedas, ¿cuántas gana en una semana de seis días? A) 12 monedas de ejemplo B) 13 monedas de ejemplo", "A) 12 monedas de ejemplo", "Se multiplica 2 por 6."),
        ("{F} ¿Por qué el registro de la fábrica no basta para conocer cómo vivían los obreros?", "Porque solo informa jornadas y salarios, no cómo vivían ni qué sentían", "Es un documento administrativo."),
        ("{F} Un compañero concluye: «Todos los barrios obreros no tenían agua potable». ¿Qué corrección haces?", "El informe habla de un solo barrio", "No se puede generalizar."),
        ("{F} ¿Qué fuente nueva ayudaría a conocer la voz de los obreros? A) Una carta de un obrero de esa época B) Un mapa actual de la ciudad", "A) Una carta de un obrero de esa época", "Aporta la voz de quienes trabajaban."),
        ("{F} ¿Qué conclusión es más proporcional? A) En esta fábrica la jornada era larga y los salarios desiguales, y en este barrio las condiciones eran duras B) En todas las fábricas se trabajaba 13 horas", "A) En esta fábrica la jornada era larga y los salarios desiguales, y en este barrio las condiciones eran duras", "No dice más de lo que muestran las fuentes."),
    ],
    ctx=("Un grupo prepara una exposición sobre la vida obrera y solo usa el registro de la fábrica. ¿Qué fuente suman para tener una visión más completa? A) El informe médico del barrio obrero B) Otro registro de la misma fábrica", "A) El informe médico del barrio obrero", "Muestra la vida fuera de la fábrica."),
    sc=[("¿Qué es una jornada?", "Las horas que se trabajan en un día", "Así se define."),
        ("¿Qué es un barrio obrero?", "Una zona donde viven trabajadores de fábricas", "Así se define."),
        ("=", "¿Cuántas horas son 5 días de 8 horas de trabajo?", "8*5", "Se multiplican las horas por los días.", " horas")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (una frase); qué interpretas (una frase con «Esto sugiere que…»). Cierra con qué no puedes concluir con esa sola fuente. {F}",
        "Fuente A. Autor y fecha: registro de una fábrica textil, 1850. Dice: jornada de 13 horas y salarios distintos según edad y sexo. Interpretación: esto sugiere que mujeres y niños recibían menos. No puedo concluir que todas las fábricas pagaban igual.",
        ["contextualiza", "separa descripción e interpretación", "señala un límite"], ["tabla de tres filas", "frase de cierre"], ["usar un juicio como descripción", "generalizar"],
        "Pide que cuente cómo habría descrito un obrero su día."),
    reinforce="Explica por qué un registro de fábrica y un informe médico informan cosas distintas.",
    extend="Calcula cuántas horas trabajas o estudias tú en una semana y compáralas con las 78 horas de la ficha.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de ciudad industrial; los datos de población son de ejemplo). "
     "Población de la ciudad de ejemplo: 1800, 80.000 habitantes; 1850, 240.000; 1900, 720.000. "
     "Explosión demográfica urbana: crecimiento muy rápido de la población de una ciudad, por migración desde el campo y por mejoras en la salud. "
     "Expansión urbana: crecimiento de la ciudad hacia nuevos terrenos. "
     "Marginalidad: situación de las personas que viven con menos servicios y derechos, por ejemplo en barrios sin agua potable ni alcantarillado. "
     "Transporte: el ferrocarril y el barco a vapor acortan los viajes; el telégrafo acelera las noticias.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio en la ciudad industrial: cómo creció, quién vivía dónde y qué cambió en el transporte.",
    prior=["Sé qué es la industrialización.", "Sé calcular multiplicaciones y divisiones simples.", "Sé leer un cuadro de datos."],
    explain=[
        "La industrialización transformó las ciudades. Las fábricas atrajeron a personas del campo que buscaban trabajo, y la población creció muy rápido. A eso se le llama explosión demográfica urbana. Si una ciudad pasa de 80.000 a 240.000 habitantes en cincuenta años, su población se multiplica por tres. Las ciudades crecieron además hacia nuevos terrenos: eso es la expansión urbana.",
        "Este crecimiento fue desigual. Se construyeron barrios burgueses con buenos servicios y barrios obreros con viviendas estrechas y sin agua potable. La marginalidad es la situación de quienes viven con menos servicios y derechos. Además, el ferrocarril y el barco a vapor acortaron los viajes, y el telégrafo aceleró las noticias, lo que conectó ciudades y regiones.",
        "Al analizar, se compara el antes y el después: el cambio en la población, los barrios, el transporte. Pero también hay continuidades: el campo siguió siendo importante y muchas personas migraron sin lograr mejores condiciones. Por eso es mejor decir que la ciudad cambió para todos, pero no mejoró igual para todos.",
    ],
    vocab=[("explosión demográfica", "crecimiento muy rápido de la población"), ("expansión urbana", "crecimiento de la ciudad hacia nuevos terrenos"), ("migración", "traslado de personas de un lugar a otro para vivir en él"), ("marginalidad", "situación de quienes viven con menos servicios y derechos"), ("alcantarillado", "red de tubos que retira las aguas sucias")],
    worked=[
        ("Calcular cuántas veces creció", "¿Cuántas veces mayor es la población de 1850 que la de 1800?", ["1800: 80.000. 1850: 240.000.", "240.000 ÷ 80.000 = 3."], "3 veces"),
        ("Calcular un aumento", "¿Cuántos habitantes aumentó la ciudad entre 1850 y 1900?", ["1900: 720.000. 1850: 240.000.", "Resto: 720.000 − 240.000 = 480.000."], "480.000 habitantes"),
    ],
    mistakes=[("Pensar que el crecimiento de la ciudad benefició igual a todos.", "Hubo barrios con servicios y barrios marginales.", "Pregunta dónde vivía cada grupo."),
              ("Creer que el campo desapareció.", "El campo siguió siendo importante y de él venían los migrantes.", "Menciona qué continuó.")],
    T=[
        ("{F} ¿Qué es la expansión urbana?", "El crecimiento de la ciudad hacia nuevos terrenos", "La ficha la define."),
        ("{F} ¿Qué es la marginalidad?", "La situación de quienes viven con menos servicios y derechos", "La ficha la define."),
        ("{F} ¿Cuántos habitantes tenía la ciudad de ejemplo en 1850?", "240.000", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos habitantes aumentó la ciudad entre 1800 y 1850?", "240000-80000", "Se resta la población de 1800 a la de 1850.", " habitantes"),
        ("=", "{F} ¿Cuántas veces mayor es la población de 1900 que la de 1800?", "720000/80000", "Se divide la población de 1900 entre la de 1800.", " veces"),
        ("{F} ¿Qué periodo tuvo un aumento mayor de población? A) 1850 a 1900 B) 1800 a 1850", "A) 1850 a 1900", "Aumentó 480.000 frente a 160.000."),
        ("{F} ¿Cuál es una causa de la explosión demográfica urbana según la ficha? A) La migración desde el campo B) El cierre de las fábricas", "A) La migración desde el campo", "La ficha lo señala."),
        ("{F} ¿Qué barrio muestra marginalidad? A) Uno sin agua potable ni alcantarillado B) Uno con buenos servicios", "A) Uno sin agua potable ni alcantarillado", "Es la definición de la ficha."),
        ("{F} ¿Qué medio de transporte acortó los viajes? A) El ferrocarril B) La carreta", "A) El ferrocarril", "La ficha dice que acorta los viajes."),
        ("{F} ¿Qué relación hay entre las fábricas y el crecimiento de la ciudad?", "Las fábricas atraían a personas del campo que buscaban trabajo", "La migración fue una causa."),
        ("{F} Un compañero dice: «Con las fábricas, todos vivieron mejor en la ciudad». ¿Qué dato de la ficha lo contradice?", "Existía marginalidad en barrios sin agua potable ni alcantarillado", "Hubo barrios con menos servicios."),
        ("{F} ¿Qué continuidad puede señalarse? A) Muchos migrantes venían del campo, que siguió siendo importante B) El campo dejó de existir", "A) Muchos migrantes venían del campo, que siguió siendo importante", "Hay un vínculo entre campo y ciudad."),
        ("{F} ¿Qué conclusión es más ajustada? A) La ciudad creció rápido y se conectó mejor, pero con desigualdad entre barrios B) La ciudad creció y todos tuvieron los mismos servicios", "A) La ciudad creció rápido y se conectó mejor, pero con desigualdad entre barrios", "Reúne cambio y desigualdad."),
    ],
    ctx=("Una autoridad de ejemplo plantea construir un barrio obrero cerca de las fábricas, pero sin agua potable. ¿Qué advertencia basada en la ficha harías? A) Generaría marginalidad y riesgos para la salud B) No habría ningún problema", "A) Generaría marginalidad y riesgos para la salud", "La ficha asocia la falta de servicios con marginalidad."),
    sc=[("¿Qué es la migración?", "El traslado de personas de un lugar a otro para vivir en él", "Así se define."),
        ("¿Qué es una explosión demográfica?", "Un crecimiento muy rápido de la población", "Así se define."),
        ("=", "Si una ciudad de ejemplo tenía 300.000 habitantes y ahora tiene 450.000, ¿cuántos habitantes aumentó?", "450000-300000", "Se resta la población inicial a la final.", " habitantes")],
    op=("Dibuja un gráfico de barras con la población de la ciudad de ejemplo en 1800, 1850 y 1900, usando la escala 1 cm = 100.000 habitantes. Debajo escribe dos frases: una que explique por qué creció y otra que diga qué problema trajo ese crecimiento. {F}",
        "Barras de 0,8 cm, 2,4 cm y 7,2 cm. Frases: «La ciudad creció porque las fábricas atraían a personas del campo»; «El crecimiento causó marginalidad en barrios sin agua potable ni alcantarillado».",
        ["escala correcta", "tres barras", "dos frases con datos de la ficha"], ["gráfico de barras", "dos frases"], ["no usar la escala", "no explicar el problema"],
        "Pide que diga qué servicio básico sería más urgente en un barrio marginal."),
    reinforce="Explica en voz alta por qué creció la ciudad industrial y qué problema trajo.",
    extend="Averigua cuántas personas viven en tu comuna y compara con otra comuna con una resta.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Dueño de una fábrica, 1860: «Doy trabajo a cien familias. Sin mi fábrica, esta ciudad no existiría. Si pago más, tendré que cerrar.» "
     "Obrero adulto, 1860: «Trabajo trece horas y apenas alcanzo a comprar pan. Si nos unimos, podemos exigir una jornada más corta.» "
     "Madre obrera, 1860: «Mis hijos de doce años también trabajan. Si no, no alcanza para comer.» "
     "Reformador social, 1860: «El Estado debe dictar leyes que limiten el trabajo de niños y mejoren las viviendas obreras.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores, causas y perspectivas en la ciudad industrial: dueños, obreros, familias y reformadores.",
    prior=["Sé qué es el proletariado y la burguesía industrial.", "Sé contextualizar una fuente.", "Sé que cada actor tiene intereses."],
    explain=[
        "En la industrialización convivieron actores con intereses distintos. El dueño de la fábrica da trabajo y paga salarios, pero quiere ganancias; por eso dice que si paga más tendrá que cerrar. El obrero necesita un salario digno y propone unirse para exigir una jornada más corta. Las familias pobres enviaban a niños a trabajar para sobrevivir. Un reformador social pide que el Estado dicte leyes de protección.",
        "Uno de los resultados fue el movimiento obrero: organizaciones como sindicatos y sociedades de ayuda mutua, que juntaban dinero para apoyar a socios en caso de enfermedad o accidente. Los obreros comenzaron a pedir mejores salarios, menos horas y seguridad. La libre asociación permitió que se organizaran, aunque muchas veces los dueños y el Estado se oponían.",
        "Contrastar significa mirar qué quiere cada actor, qué le conviene y qué teme. El dueño teme las pérdidas, el obrero teme el hambre y los accidentes, la madre teme no alcanzar a alimentar a sus hijos y el reformador teme el daño social. Una explicación sólida no elige un bando sin evidencia: muestra por qué los intereses chocan.",
    ],
    vocab=[("sindicato", "organización de trabajadores para defender sus derechos"), ("sociedad de ayuda mutua", "organización que reúne dinero para ayudar a sus socios en emergencias"), ("movimiento obrero", "conjunto de acciones y organizaciones de trabajadores"), ("ganancia", "dinero que queda después de pagar los costos"), ("reformador social", "persona que propone cambios para corregir injusticias")],
    worked=[
        ("Calcular la jornada semanal", "Según el obrero, si trabaja trece horas por seis días, ¿cuántas horas trabaja en una semana?", ["Trece horas por día.", "13 × 6 = 78."], "78 horas"),
        ("Identificar el temor del dueño", "¿Qué teme el dueño de la fábrica?", ["Dice que si paga más tendrá que cerrar.", "Teme perder ganancias."], "Cerrar la fábrica por pagar más"),
    ],
    mistakes=[("Explicar los conflictos con la voz del dueño solamente.", "Se ignora a los obreros y a las familias.", "Incluye al menos dos voces opuestas."),
              ("Pensar que el trabajo infantil era una decisión sin razón.", "Respondía a la pobreza de las familias.", "Explica la causa y también la crítica.")],
    T=[
        ("{F} ¿Cuántas familias dice el dueño que dependen de su fábrica?", "Cien", "Su voz lo dice."),
        ("{F} ¿Qué propone el obrero para conseguir una jornada más corta?", "Unirse", "Su voz lo dice."),
        ("{F} ¿Por qué trabajan los hijos de doce años de la madre obrera?", "Porque si no, no alcanza para comer", "Su voz lo explica."),
        ("{F} ¿Qué pide el reformador social?", "Leyes que limiten el trabajo infantil y mejoren las viviendas obreras", "Su voz lo propone."),
        ("=", "{F} Una fábrica de ejemplo tiene una jornada de 10 horas durante 6 días. ¿Cuántas horas se trabajan en una semana?", "10*6", "Se multiplica la jornada por los días.", " horas"),
        ("{F} ¿Qué actor defiende que la fábrica da trabajo? A) El dueño de la fábrica B) El reformador social", "A) El dueño de la fábrica", "Su voz lo dice."),
        ("{F} ¿Qué actor propone una acción colectiva? A) El obrero adulto B) El dueño", "A) El obrero adulto", "Propone que los obreros se unan."),
        ("{F} ¿Qué actor pide intervención del Estado? A) El reformador social B) La madre obrera", "A) El reformador social", "Pide leyes al Estado."),
        ("{F} ¿Qué es un sindicato? A) Una organización de trabajadores para defender sus derechos B) Una empresa", "A) Una organización de trabajadores para defender sus derechos", "Es la definición de la clase."),
        ("{F} ¿Por qué el dueño y el obrero tienen perspectivas distintas sobre el salario?", "Porque pagar más reduce las ganancias del dueño y el obrero necesita un salario mayor", "Sus intereses se oponen."),
        ("{F} Un compañero dice: «Todos los actores querían lo mismo». Refútalo con la ficha.", "El dueño teme cerrar, el obrero quiere jornada corta y el reformador pide leyes", "Las posturas difieren."),
        ("{F} ¿Qué actor critica el trabajo infantil? A) El reformador social B) El dueño de la fábrica", "A) El reformador social", "Pide limitarlo por ley."),
        ("{F} ¿Qué conclusión es más equilibrada? A) La industrialización produjo conflictos entre quienes querían ganancias y quienes pedían mejores condiciones B) Todos estaban conformes con la industrialización", "A) La industrialización produjo conflictos entre quienes querían ganancias y quienes pedían mejores condiciones", "Reúne las cuatro voces."),
    ],
    ctx=("En un debate escolar, un grupo defiende al dueño y otro al obrero sobre la jornada de trabajo. ¿Qué argumento da el segundo grupo? A) Trece horas diarias dejan poco tiempo de descanso y los obreros pueden organizarse B) Las fábricas no existían", "A) Trece horas diarias dejan poco tiempo de descanso y los obreros pueden organizarse", "Se apoya en la voz del obrero."),
    sc=[("¿Qué es un sindicato?", "Una organización de trabajadores para defender sus derechos", "Así se define."),
        ("¿Qué actor teme cerrar su fábrica?", "El dueño", "Su voz lo dice."),
        ("¿Qué es una sociedad de ayuda mutua?", "Una organización que reúne dinero para ayudar a sus socios", "Así se define.")],
    op=("Elige dos actores de la ficha y haz una tabla con: qué quiere, qué le conviene y qué teme. Después escribe tres líneas que expliquen por qué sus perspectivas sobre el trabajo en la fábrica chocan. {F}",
        "Dueño: quiere ganancias; le conviene pagar poco; teme cerrar. Obrero: quiere jornada corta; le conviene unirse; teme el hambre. Texto: «El dueño quiere ahorrar costos y el obrero quiere ganar más; por eso sus intereses chocan».",
        ["elige dos actores", "tres columnas completas", "explica el choque"], ["tabla completa", "tres líneas"], ["mezclar las voces", "opinar sin base"],
        "Pide que diga qué solución ayudaría a ambos."),
    reinforce="Elige un actor y explica en voz alta qué teme y qué quiere.",
    extend="Averigua qué es un sindicato hoy y si alguna persona de tu entorno participa en uno.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento). "
     "Pregunta: ¿cómo transformó la industrialización la economía, la población y el territorio? "
     "Dato 1: expansión del trabajo asalariado en fábricas. "
     "Dato 2: surgimiento del proletariado y consolidación de la burguesía industrial. "
     "Dato 3: en la ciudad de ejemplo la población pasó de 80.000 habitantes en 1800 a 720.000 en 1900. "
     "Dato 4: el ferrocarril y el telégrafo acortaron viajes y aceleraron las noticias. "
     "Dato 5: hubo barrios obreros sin agua potable ni alcantarillado.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre los efectos de la industrialización con afirmación, evidencia, razonamiento y una conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé contrastar actores.", "Sé que una conclusión debe ser proporcional."],
    explain=[
        "Un argumento sobre la industrialización puede afirmar: «la industrialización transformó la economía, la población y el territorio, pero de forma desigual». La evidencia son los datos: el trabajo asalariado, el surgimiento del proletariado, el crecimiento de la ciudad, el ferrocarril y los barrios sin servicios. El razonamiento explica cómo cada dato muestra un cambio en la economía, la población o el territorio.",
        "La economía cambió porque se expandió el trabajo asalariado y apareció el proletariado junto a una burguesía industrial más fuerte. La población cambió porque las ciudades crecieron mucho. El territorio cambió porque el ferrocarril y el telégrafo conectaron lugares y porque las ciudades se expandieron. Pero los barrios sin agua potable muestran que no todos se beneficiaron igual.",
        "Para que el argumento sea proporcional hay que reconocer los límites. Los datos son de una ciudad de ejemplo y no prueban lo que ocurrió en todas. Un buen texto anticipa un contraargumento, por ejemplo que la industrialización mejoró el transporte, y lo responde mostrando también los costos.",
    ],
    vocab=[("afirmación", "respuesta que defiendes a una pregunta"), ("evidencia", "dato de una fuente que sostiene la afirmación"), ("razonamiento", "explicación que conecta evidencia y afirmación"), ("desigual", "que no se reparte de la misma forma entre todos"), ("contraargumento", "idea o dato que podría contradecir la afirmación")],
    worked=[
        ("Elegir evidencia sobre la población", "¿Qué dato de la ficha muestra un cambio en la población?", ["Busco un dato sobre habitantes.", "El dato 3 muestra el crecimiento de 80.000 a 720.000."], "Dato 3"),
        ("Detectar un costo", "¿Qué dato muestra que no todos se beneficiaron?", ["Busco un dato sobre desigualdad o falta de servicios.", "El dato 5 habla de barrios sin agua potable."], "Dato 5"),
    ],
    mistakes=[("Escribir que la industrialización mejoró la vida de todos.", "Los datos muestran barrios sin servicios y desigualdad.", "Usa expresiones como «de forma desigual»."),
              ("Citar un dato sin explicarlo.", "Falta el razonamiento.", "Agrega «Esto muestra que…».")],
    T=[
        ("{F} ¿Qué dato muestra un cambio en la economía?", "El dato 1, la expansión del trabajo asalariado", "Es un cambio en cómo se trabaja."),
        ("{F} ¿Qué dato muestra un cambio en el territorio?", "El dato 4, el ferrocarril y el telégrafo", "Acortan las distancias entre lugares."),
        ("{F} ¿Qué dato muestra un cambio en los grupos sociales?", "El dato 2, el surgimiento del proletariado", "Aparecen grupos nuevos."),
        ("=", "{F} ¿Cuántos habitantes aumentó la ciudad de ejemplo entre 1800 y 1900?", "720000-80000", "Se resta la población de 1800 a la de 1900.", " habitantes"),
        ("=", "{F} En un barrio obrero de la ciudad de ejemplo viven 2.000 familias y el 25 % no tiene agua potable (dato de ejemplo). ¿Cuántas familias son?", "2000*25/100", "Se calcula el 25 % de 2.000.", " familias"),
        ("{F} ¿Qué afirmación responde la pregunta? A) La industrialización transformó la economía, la población y el territorio de forma desigual B) La industrialización no cambió nada", "A) La industrialización transformó la economía, la población y el territorio de forma desigual", "Se apoya en los cinco datos."),
        ("{F} ¿Qué dato sirve de contraargumento a la idea de progreso para todos? A) El dato 5 B) El dato 4", "A) El dato 5", "Muestra barrios sin servicios."),
        ("{F} Completa el razonamiento: «El dato 4 apoya el cambio territorial porque…» A) acortó los viajes y aceleró las noticias B) cerró las fábricas", "A) acortó los viajes y aceleró las noticias", "Conecta el dato con el territorio."),
        ("{F} Un compañero escribe: «Con las fábricas toda la población vivió mejor». ¿Qué dato lo contradice?", "El dato 5, barrios obreros sin agua potable ni alcantarillado", "Muestra que hubo desigualdad entre barrios."),
        ("{F} ¿Por qué el dato 3 es de una ciudad de ejemplo y no basta para toda la industrialización?", "Porque es un solo caso y no prueba lo que ocurrió en todas las ciudades", "Un caso no permite generalizar."),
        ("{F} Ordena las partes de un argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y se explica."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «desigual» B) «perfecta»", "A) «desigual»", "Refleja que no todos se beneficiaron."),
        ("{F} ¿Qué conclusión se ajusta mejor a los datos? A) La industrialización cambió la economía, el territorio y la población, pero generó desigualdad B) La industrialización no tuvo costos", "A) La industrialización cambió la economía, el territorio y la población, pero generó desigualdad", "Reúne cambios y costos."),
    ],
    ctx=("Un afiche escolar dice: «La industrialización fue solo progreso». ¿Qué evidencia de la ficha usarías para matizarlo? A) El dato 5, los barrios sin agua potable B) El dato 4 solo", "A) El dato 5, los barrios sin agua potable", "Muestra un costo."),
    sc=[("En un argumento sobre la industrialización, ¿cómo se llama la respuesta que defiendes a la pregunta?", "La afirmación", "Así se llama la respuesta que se defiende."),
        ("¿Qué dato de la ficha funciona como contraargumento a «la industrialización fue solo progreso»?", "El dato 5, los barrios sin agua potable ni alcantarillado", "Muestra un costo de la industrialización."),
        ("=", "Si una ciudad de ejemplo pasa de 100.000 a 500.000 habitantes, ¿cuántas veces creció?", "500000/100000", "Se divide la población final entre la inicial.", " veces")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Cómo transformó la industrialización la economía, la población y el territorio?». Usa al menos tres datos de la ficha, incluye el dato 5 como límite y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«La industrialización transformó la economía, la población y el territorio de forma desigual. Se expandió el trabajo asalariado y apareció el proletariado. La ciudad de ejemplo pasó de 80.000 a 720.000 habitantes y el ferrocarril acortó los viajes. Sin embargo, hubo barrios obreros sin agua potable, lo que muestra desigualdad».",
        ["responde la pregunta", "usa tres datos y el límite", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["usar «todos» sin evidencia", "no explicar el vínculo"],
        "Pide que diga qué dato le gustaría tener de otra ciudad."),
    reinforce="Explica en voz alta un cambio económico, uno de población y uno de territorio.",
    extend="Escribe un contraargumento y respóndelo con un dato de la ficha.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (proyecciones y límites de la industrialización). "
     "Ley de fábricas de Gran Bretaña, 1833: limitó el trabajo de niños en las fábricas textiles. "
     "Ley de las diez horas de Gran Bretaña, 1847: limitó a diez horas la jornada de mujeres y jóvenes en fábricas textiles. "
     "Contaminación: las fábricas a carbón llenaron el aire de humo en ciudades industriales. "
     "Economía de exportación en América Latina: muchos países vendían materias primas (minerales, productos agrícolas) y compraban productos industriales. "
     "Chile: la minería del norte exportaba minerales; el primer ferrocarril, 1851, conectaba una mina con un puerto.")
build(
    OA, 6, F,
    use="Aprenderé a evaluar proyecciones y límites de la industrialización: qué reformas surgieron, qué problemas dejó y cómo se insertó América Latina.",
    prior=["Sé qué cambió con la industrialización.", "Sé contrastar actores.", "Sé construir un argumento."],
    explain=[
        "La industrialización dejó problemas, pero también reacciones. Para limitar los abusos, algunos Estados dictaron leyes laborales. En Gran Bretaña, una ley de 1833 limitó el trabajo de niños en fábricas textiles, y otra de 1847 limitó a diez horas la jornada de mujeres y jóvenes. Estas leyes fueron respuesta a las presiones de reformadores y obreros, y son un ejemplo de cómo una sociedad corrige sus costos.",
        "Otro límite fue ambiental: las fábricas a carbón llenaron de humo el aire de las ciudades industriales. Un tercer límite fue la desigualdad entre países. Muchas regiones de América Latina vendían materias primas y compraban productos industriales, una economía de exportación. En Chile, el ferrocarril del norte conectó una mina con un puerto, lo que muestra esa orientación hacia afuera.",
        "Evaluar significa pesar logros y costos con evidencia. La industrialización creó riqueza y transportes, pero también desigualdad, contaminación y dependencia. Las proyecciones llegan hasta hoy: seguimos discutiendo jornadas laborales, medio ambiente y cómo repartir la riqueza.",
    ],
    vocab=[("ley laboral", "ley que regula el trabajo, como la jornada o el trabajo infantil"), ("contaminación", "presencia en el ambiente de sustancias dañinas"), ("materia prima", "recurso natural que se usa para producir otros bienes"), ("economía de exportación", "economía que vende al extranjero sobre todo recursos naturales"), ("dependencia", "situación en que un país necesita de otros para su economía")],
    worked=[
        ("Calcular una distancia entre leyes", "¿Cuántos años pasaron entre la ley de fábricas de 1833 y la de las diez horas de 1847?", ["Tomo los dos años.", "Resto: 1847 − 1833 = 14."], "14 años"),
        ("Pesar un logro y un costo", "Un logro de las fábricas fue producir más. ¿Qué costo señala la ficha?", ["La ficha menciona la contaminación del aire.", "Es un costo ambiental."], "La contaminación del aire por el humo"),
    ],
    mistakes=[("Decir que las leyes laborales resolvieron todos los problemas.", "Eran limitadas y se aplicaban a ciertos grupos y rubros.", "Pregunta a quiénes cubrían."),
              ("Olvidar la dimensión ambiental.", "La contaminación fue un costo importante.", "Menciona el humo de las fábricas a carbón.")],
    T=[
        ("{F} ¿Qué limitó la ley de 1833?", "El trabajo de niños en fábricas textiles", "La ficha lo indica."),
        ("{F} ¿Cuántas horas fijó la ley de 1847 para mujeres y jóvenes?", "Diez horas", "La ficha lo indica."),
        ("{F} ¿Qué vendían muchos países de América Latina?", "Materias primas", "La ficha lo señala."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley de las diez horas y el primer ferrocarril de Chile?", "1851-1847", "Se resta el año de la ley al del ferrocarril.", " años"),
        ("=", "{F} Una ley limita la jornada a 10 horas diarias. Si se trabajan 6 días, ¿cuántas horas son por semana?", "10*6", "Se multiplica la jornada por los días.", " horas"),
        ("{F} ¿Qué es un costo ambiental de las fábricas a carbón? A) El humo en el aire B) Los salarios altos", "A) El humo en el aire", "La ficha lo señala."),
        ("{F} ¿Qué efecto tuvieron las leyes laborales? A) Limitaron abusos en las fábricas B) Eliminaron el trabajo asalariado", "A) Limitaron abusos en las fábricas", "Regularon jornada y trabajo infantil."),
        ("{F} ¿Qué tipo de economía describe vender minerales y comprar productos industriales? A) Economía de exportación B) Economía de autoconsumo", "A) Economía de exportación", "La ficha la define."),
        ("{F} ¿Qué actor impulsó las leyes laborales? A) Reformadores y obreros que presionaron B) Solo los dueños de fábricas", "A) Reformadores y obreros que presionaron", "La explicación lo señala."),
        ("{F} ¿Por qué se dice que las leyes laborales fueron limitadas?", "Porque cubrían ciertos grupos y rubros, como niños, mujeres y jóvenes en fábricas textiles", "No alcanzaban a todos los trabajadores."),
        ("{F} Un compañero dice: «La industrialización no tuvo costos». Refútalo con la ficha.", "La ficha muestra contaminación del aire y trabajo infantil que debió limitarse", "Hubo costos sociales y ambientales."),
        ("{F} ¿Qué dependencia podía generar una economía de exportación? A) Necesitar vender materias primas y comprar productos industriales B) No necesitar a otros países", "A) Necesitar vender materias primas y comprar productos industriales", "Quedaba dependiente de mercados externos."),
        ("{F} ¿Qué conclusión pesa logros y costos? A) La industrialización creó riqueza y transportes, pero también desigualdad, contaminación y dependencia B) Solo trajo ventajas", "A) La industrialización creó riqueza y transportes, pero también desigualdad, contaminación y dependencia", "Considera ambas caras."),
    ],
    ctx=("Una comuna de ejemplo discute instalar una fábrica a carbón junto al barrio. ¿Qué advertencia basada en la ficha harías? A) Podría generar humo y contaminación del aire B) No habría ningún efecto", "A) Podría generar humo y contaminación del aire", "La ficha asocia las fábricas a carbón con contaminación."),
    sc=[("¿Qué es una ley laboral?", "Una ley que regula el trabajo", "Así se define."),
        ("En Historia: ¿Qué es una materia prima?", "Un recurso natural que se usa para producir otros bienes", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1833 y 1851?", "1851-1833", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Logros» y «Costos», con tres datos en cada una usando la ficha y la explicación. Luego escribe una frase que pese ambos y diga qué ley o medida crees que fue más importante, con una razón apoyada en la ficha. {F}",
        "Logros: más producción; transportes; riqueza. Costos: contaminación; trabajo infantil; dependencia. Frase: «La ley de 1833 fue importante porque protegió a niños de trabajos duros».",
        ["tres logros y tres costos", "usa evidencia", "frase que pesa ambos"], ["tabla completa", "una frase"], ["solo logros o solo costos", "opinar sin evidencia"],
        "Pide que diga qué ley laboral actual protege a los trabajadores jóvenes."),
    reinforce="Explica en voz alta un logro y un costo de la industrialización.",
    extend="Averigua qué dice la ley chilena actual sobre la edad mínima para trabajar y anota una frase.",
)
