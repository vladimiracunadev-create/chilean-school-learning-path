"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 01 (liberalismo, republicanismo y transformaciones del siglo XIX)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 01"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (el siglo XIX son los años 1801 a 1900). "
     "Liberalismo: defiende las libertades individuales, la propiedad privada, la ley por encima del rey y el libre mercado (comerciar con pocas trabas del Estado). "
     "Republicanismo: defiende un gobierno sin monarca hereditario, con autoridades elegidas, y la idea de que el poder viene del pueblo. "
     "Hitos: independencia de Estados Unidos, 1776; Revolución Francesa, 1789; ley que reformó el voto en Gran Bretaña, 1832; abolición de la esclavitud en Chile, 1823; abolición de la esclavitud en Brasil, 1888.")
build(
    OA, 1, F,
    use="Aprenderé a situar en el tiempo y en el espacio las ideas liberales y republicanas, y a plantear la pregunta que guía este tema: ¿cómo cambiaron la política y la economía de América y Europa en el siglo XIX?",
    prior=["Sé calcular diferencias entre años y ubicar un año en su siglo.", "Conozco las independencias americanas como proceso de comienzos del siglo XIX.", "Sé que una época es una convención de los historiadores."],
    explain=[
        "El liberalismo y el republicanismo son dos conjuntos de ideas que se cruzan en el siglo XIX, pero no son lo mismo. El liberalismo pone en el centro la libertad de cada persona: opinar, reunirse, tener propiedades y comerciar sin que el Estado lo controle todo. Esto incluye el libre mercado, es decir, que los precios y los intercambios dependan de compradores y vendedores y no de decisiones del rey.",
        "El republicanismo se preocupa por cómo se organiza el poder. Propone que las autoridades sean elegidas por un tiempo y que el poder venga del pueblo, no de una familia real. Un país puede ser liberal y monarquía (con un rey limitado por una constitución) o republicano y poco liberal. Por eso conviene separar las dos ideas.",
        "Estas ideas surgen en Europa y Estados Unidos hacia fines del siglo XVIII y se extienden a América Latina durante el siglo XIX. Un error frecuente es pensar que apenas se declararon, todos tuvieron derechos: muchas leyes dejaron fuera a las mujeres, a los pobres y a las personas esclavizadas por años. Una declaración de derechos no es lo mismo que participación real.",
    ],
    vocab=[("liberalismo", "conjunto de ideas que defiende las libertades individuales, la propiedad y el libre mercado"), ("republicanismo", "conjunto de ideas que defiende un gobierno de autoridades elegidas, sin monarca hereditario"), ("libre mercado", "comercio donde los precios dependen de compradores y vendedores, con pocas trabas del Estado"), ("ciudadanía", "condición de quien tiene derechos políticos, como votar"), ("abolición", "término legal de una práctica, como la esclavitud")],
    worked=[
        ("Ubicar un hito en su siglo", "Según la ficha, la Revolución Francesa fue en 1789. ¿A qué siglo pertenece?", ["Recuerdo que el siglo XVIII va de 1701 a 1800.", "El año 1789 está en ese tramo."], "Siglo XVIII"),
        ("Comparar dos procesos", "¿Cuántos años pasaron entre la independencia de Estados Unidos (1776) y la reforma del voto en Gran Bretaña (1832)?", ["Tomo los dos años de la ficha.", "Resto: 1832 − 1776 = 56."], "56 años"),
    ],
    mistakes=[("Escribir que liberalismo y republicanismo significan lo mismo.", "Se mezcla una idea sobre libertades y mercado con otra sobre cómo se elige a las autoridades.", "Define cada una por separado y di en qué pueden coincidir."),
              ("Creer que una ley que declara derechos los da a todas las personas.", "Se confunde derecho declarado con participación efectiva.", "Pregunta quiénes quedaron fuera y cuándo se incorporaron.")],
    T=[
        ("{F} ¿Qué dice el liberalismo respecto a la ley y al rey?", "La ley está por encima del rey", "La ficha dice que defiende la ley por encima del rey."),
        ("{F} ¿Qué tipo de autoridades propone el republicanismo?", "Autoridades elegidas, sin monarca hereditario", "La ficha lo define así."),
        ("{F} ¿A qué siglo pertenece la abolición de la esclavitud en Brasil?", "Siglo XIX", "1888 está entre 1801 y 1900."),
        ("=", "{F} ¿Cuántos años pasaron entre la Revolución Francesa y la abolición de la esclavitud en Chile?", "1823-1789", "Se resta el año de la Revolución al de la abolición en Chile.", " años"),
        ("=", "{F} ¿Cuántos años separan la abolición de la esclavitud en Chile de la de Brasil?", "1888-1823", "Se resta el año chileno al año brasileño.", " años"),
        ("{F} ¿Cuál de estos hitos pertenece al siglo XIX? A) La independencia de Estados Unidos B) La reforma del voto en Gran Bretaña", "B) La reforma del voto en Gran Bretaña", "1832 está entre 1801 y 1900; 1776 es del siglo XVIII."),
        ("=", "{F} Una línea de tiempo usa 1 cm = 20 años y va de 1780 a 1900. ¿Cuántos centímetros mide?", "(1900-1780)/20", "Se divide el tramo de 120 años por lo que vale cada centímetro.", " cm"),
        ("{F} Una ley dice: «El Estado no fijará los precios del pan y cada comerciante venderá al precio que acuerde con sus clientes». ¿Qué idea expresa? A) Libre mercado B) Republicanismo", "A) Libre mercado", "Los precios acordados entre compradores y vendedores son el libre mercado de la ficha."),
        ("{F} Un país elimina la corona hereditaria y elige a un presidente por cinco años. ¿Qué idea aplica? A) Republicanismo B) Libre mercado", "A) Republicanismo", "Elegir autoridades sin monarca hereditario es la idea republicana de la ficha."),
        ("Un compañero dice: «Liberalismo y republicanismo son sinónimos». Corrígelo usando la ficha.", "El liberalismo defiende libertades y mercado; el republicanismo defiende autoridades elegidas sin monarca hereditario, y pueden combinarse pero no son lo mismo", "La ficha da definiciones distintas: una de libertades y otra de organización del poder."),
        ("{F} ¿Por qué la abolición de la esclavitud en Chile (1823) y en Brasil (1888) muestra que las ideas liberales se aplicaron de forma desigual?", "Porque la libertad se concretó con 65 años de diferencia según el país", "Los años de la ficha muestran ritmos distintos en cada país."),
        ("{F} Alguien afirma: «En 1832 todos los adultos de Gran Bretaña pudieron votar». ¿Se puede sostener con la ficha? A) Sí, porque hubo una reforma del voto B) No, la ficha solo dice que se reformó el voto, no que votaran todos", "B) No, la ficha solo dice que se reformó el voto, no que votaran todos", "Reformar el voto no prueba que todos votaran; sería afirmar más de lo que la evidencia permite."),
        ("¿Cuál es la mejor pregunta histórica para este tema? A) ¿Qué ideas liberales y republicanas cambiaron la política y la economía en América y Europa durante el siglo XIX? B) ¿Quién fue el mejor líder del siglo XIX?", "A) ¿Qué ideas liberales y republicanas cambiaron la política y la economía en América y Europa durante el siglo XIX?", "La pregunta A se puede responder con hechos, tiempo y lugar; la B es una opinión sin criterio."),
    ],
    ctx=("Una exposición escolar se titula «En 1800 todos los países se hicieron repúblicas liberales». ¿Qué problema tiene? A) Pone una fecha única a procesos graduales y distintos según el país B) Es un título demasiado largo", "A) Pone una fecha única a procesos graduales y distintos según el país", "La ficha muestra hitos entre 1776 y 1888, no una fecha única."),
    sc=[("¿A qué siglo pertenece el año 1832?", "Siglo XIX", "El siglo XIX va de 1801 a 1900."),
        ("¿Qué es el libre mercado según la ficha?", "Comercio con pocas trabas del Estado", "Así lo define la ficha en la idea liberal."),
        ("=", "¿Cuántos años pasaron entre 1776 y 1789?", "1789-1776", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo con escala 1 cm = 20 años, de 1760 a 1900. Marca con una raya y su nombre: independencia de Estados Unidos (1776), Revolución Francesa (1789), abolición de la esclavitud en Chile (1823), reforma del voto en Gran Bretaña (1832) y abolición en Brasil (1888). Debajo escribe dos frases: una que diga qué es el liberalismo y otra que diga qué es el republicanismo. {F}",
        "Posiciones desde 1760: 0,8 cm; 1,45 cm; 3,15 cm; 3,6 cm; 6,4 cm. Frases: «El liberalismo defiende libertades individuales, propiedad y libre mercado»; «El republicanismo defiende autoridades elegidas sin monarca hereditario».",
        ["respeta la escala", "los cinco hitos están bien ubicados", "las dos definiciones son distintas y correctas"], ["línea de tiempo dibujada", "dos frases escritas"], ["poner los hitos sin medir", "definir las dos ideas con las mismas palabras"],
        "Pide que explique por qué Brasil y Chile abolieron la esclavitud en años tan distintos."),
    reinforce="Explica en voz alta, con tus palabras, la diferencia entre liberalismo y republicanismo y da un hito con su año para cada uno.",
    extend="Busca en tu casa un objeto o documento con una fecha y di a qué siglo pertenece.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, editorial de un periódico liberal, 1848: «Exigimos que ningún impuesto se cobre sin la aprobación de una asamblea elegida y que cada persona pueda reunirse y publicar sin pedir permiso al gobierno.» "
     "Fuente B, carta de un dueño de plantación a un amigo, 1840: «Si se prohíbe la esclavitud, mis campos quedarán sin trabajadores y mi propiedad perderá valor. Los liberales dicen que la propiedad es un derecho sagrado.»")
build(
    OA, 2, F,
    use="Aprenderé a contextualizar fuentes sobre ideas liberales: ver quién habla, cuándo, para qué, y qué puedo concluir y qué no.",
    prior=["Sé situar el liberalismo y el republicanismo en el siglo XIX.", "Sé que una fuente es una huella del pasado.", "Sé separar lo que dice un texto de lo que yo interpreto."],
    explain=[
        "Para trabajar una fuente se pregunta: ¿quién la escribió?, ¿cuándo?, ¿dónde?, ¿para quién? y ¿para qué? Un editorial de periódico busca convencer a los lectores; una carta privada muestra lo que una persona dice a un amigo. Ninguno de los dos es neutral, y eso no los hace inútiles: son evidencia de lo que pensaba cada grupo.",
        "Hay que distinguir la descripción de la interpretación. Describir es repetir lo que dice el texto: «el editorial pide que los impuestos los apruebe una asamblea». Interpretar es una idea tuya apoyada en ese texto: «los liberales querían limitar el poder del gobierno sobre el dinero». Una interpretación sólida no dice más de lo que la fuente permite.",
        "Las fuentes pueden mostrar tensiones. En la carta, el dueño usa la idea liberal de propiedad para defender la esclavitud, mientras el editorial defiende la libertad de reunirse y publicar. Esa tensión ayuda a entender por qué el movimiento abolicionista, que pedía terminar con la esclavitud, chocó con intereses que también hablaban de propiedad.",
    ],
    vocab=[("fuente", "huella del pasado que sirve para conocer la historia"), ("editorial", "texto de opinión que expresa la postura de un periódico"), ("contextualizar", "averiguar autor, fecha, lugar y propósito de una fuente"), ("movimiento abolicionista", "grupo que pedía terminar con la esclavitud"), ("tensión", "choque entre dos ideas o intereses dentro de un mismo proceso")],
    worked=[
        ("Contextualizar", "Una nota de ejemplo dice: «Valparaíso, 1850. Un comerciante pide menos trabas para importar telas». ¿Quién, cuándo y dónde?", ["Autor: un comerciante.", "Fecha: 1850.", "Lugar: Valparaíso."], "Un comerciante, en 1850, en Valparaíso"),
        ("Descripción o interpretación", "De esa nota se afirma: (1) «Pide menos trabas para importar telas» y (2) «Todos los comerciantes eran liberales». ¿Cuál es descripción?", ["La frase (1) repite lo que dice la nota.", "La frase (2) generaliza a todos y la nota habla de uno."], "La (1) describe; la (2) generaliza más de lo permitido"),
    ],
    mistakes=[("Concluir con un solo editorial que «todos» pensaban igual.", "Un editorial muestra la postura de un periódico, no de toda la sociedad.", "Escribe «este periódico opina que» y busca otra fuente para comparar."),
              ("Tomar una carta privada como un hecho comprobado.", "Una carta expresa lo que su autor cree y le conviene.", "Pregunta qué intereses tenía quien escribió.")],
    T=[
        ("{F} ¿En qué año se escribió la Fuente A?", "1848", "La ficha fecha el editorial en 1848."),
        ("{F} ¿Qué tipo de texto es la Fuente B?", "Una carta de un dueño de plantación a un amigo", "La ficha la presenta como carta privada."),
        ("{F} ¿Qué pide la Fuente A sobre los impuestos?", "Que los apruebe una asamblea elegida", "El editorial lo dice de forma directa."),
        ("=", "{F} ¿Cuántos años separan la Fuente B de la Fuente A?", "1848-1840", "Se resta el año de la carta al del editorial.", " años"),
        ("{F} ¿Quién tiene más probabilidad de escribir para convencer a muchos lectores: A) El autor de la Fuente A, porque es un editorial B) El autor de la Fuente B, porque es una carta privada", "A) El autor de la Fuente A, porque es un editorial", "Un editorial se publica para convencer; una carta privada se dirige a una persona."),
        ("{F} ¿Qué frase es una descripción de la Fuente B? A) El dueño teme que sus campos queden sin trabajadores B) El dueño era una persona egoísta", "A) El dueño teme que sus campos queden sin trabajadores", "La frase A repite lo que dice el texto; la B es un juicio personal."),
        ("{F} ¿Qué derecho liberal cita el dueño de la Fuente B para defender su postura? A) La propiedad B) La libertad de prensa", "A) La propiedad", "El dueño menciona la propiedad como derecho sagrado de los liberales."),
        ("{F} ¿Qué dos derechos nombra la Fuente A, además de la aprobación de los impuestos por una asamblea? ", "Reunirse y publicar sin permiso del gobierno", "El editorial pide libertad de reunión y de publicación."),
        ("{F} ¿Qué idea de la Fuente A se relaciona con el republicanismo? A) Los impuestos los aprueba una asamblea elegida B) Cada persona puede reunirse", "A) Los impuestos los aprueba una asamblea elegida", "Una asamblea elegida limita al gobierno y representa a quienes la eligen."),
        ("{F} ¿Qué tensión muestra la Fuente B dentro del pensamiento liberal?", "Usa la propiedad para defender la esclavitud, que choca con la libertad de las personas", "La carta usa un derecho liberal contra la libertad de otros."),
        ("{F} Un compañero concluye: «En 1840 todos los dueños de tierras defendían la esclavitud». ¿Por qué no se puede sostener con la ficha?", "Porque la ficha tiene la carta de una sola persona", "Una carta no prueba lo que pensaban todos."),
        ("{F} ¿Qué fuente nueva te serviría para comparar con la Fuente B? A) Una carta de una persona abolicionista de la misma época B) Un mapa actual de plantaciones", "A) Una carta de una persona abolicionista de la misma época", "Comparar exige otra voz de la misma época y sobre el mismo tema."),
        ("{F} Un compañero escribe: «El editorial prueba que el siglo XIX fue la época de la libertad total». ¿Qué corrección haces? A) La fuente muestra lo que pedía un periódico, no que existiera libertad total B) Es correcto porque el editorial lo dice", "A) La fuente muestra lo que pedía un periódico, no que existiera libertad total", "Una petición no prueba que se cumpliera; la Fuente B muestra además un límite."),
    ],
    ctx=("Para una exposición sobre el liberalismo debes elegir entre usar solo la Fuente A o las dos fuentes. ¿Qué elección da una conclusión más ajustada a la evidencia? A) Usar las dos, porque muestran ideas liberales y su tensión con la esclavitud B) Usar solo la A, porque es la más corta", "A) Usar las dos, porque muestran ideas liberales y su tensión con la esclavitud", "Dos fuentes con intereses distintos permiten una conclusión más completa."),
    sc=[("¿Qué preguntas ayudan a contextualizar una fuente? Escribe tres de ellas.", "Quién la escribió, cuándo, dónde, para quién o para qué (tres de ellas)", "Son las preguntas de contexto de la explicación."),
        ("¿Qué es describir una fuente?", "Repetir lo que dice sin agregar ideas propias", "Describir se queda en el contenido del texto."),
        ("¿Qué tipo de texto busca convencer a los lectores de un periódico?", "Un editorial", "El editorial expresa y defiende la postura del periódico.")],
    op=("Elige una de las dos fuentes de la ficha. Escribe una tabla de tres filas con: autor y fecha; qué dice (descripción en una frase); qué interpretas (una frase que empiece con «Esto sugiere que…»). Termina con una frase que diga qué NO puedes concluir con esa sola fuente. {F}",
        "Fuente A. Autor y fecha: un periódico liberal, 1848. Dice: pide que los impuestos los apruebe una asamblea elegida. Interpretación: esto sugiere que los liberales querían limitar el poder del gobierno. No puedo concluir que todos los periódicos pensaran igual.",
        ["contextualiza con autor y fecha", "separa descripción de interpretación", "señala un límite de la fuente"], ["tabla de tres filas", "frase de límite"], ["escribir una interpretación como si fuera descripción", "concluir sobre toda la sociedad con un solo texto"],
        "Pide que cuente qué otra fuente buscaría para comparar y por qué."),
    reinforce="Escribe la diferencia entre describir e interpretar con un ejemplo propio de la Fuente A.",
    extend="Imagina el titular de un diario de hoy sobre un tema que te interese. Responde: quién lo escribe, para qué y qué no podrías concluir con él.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de hitos del siglo XIX). "
     "Gran Bretaña: parlamentarismo, el gobierno debe contar con la confianza del Parlamento y el monarca reina con poderes limitados; reforma del voto en 1832. "
     "Francia: en 1848 se establece el voto de todos los hombres adultos (sufragio masculino universal). En Gran Bretaña, Francia y Chile no votaban las mujeres en esas fechas. "
     "Chile: Constitución de 1833; vota solo quien cumple requisitos de renta o propiedad y sabe leer (voto censitario). "
     "Esclavitud: abolida en Estados Unidos en 1865, en Cuba en 1886 y en Brasil en 1888.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar el cambio y la continuidad en el siglo XIX, y a ver en qué territorios las ideas liberales avanzaron primero y dónde se demoraron.",
    prior=["Sé contextualizar una fuente.", "Sé diferenciar liberalismo y republicanismo.", "Sé calcular diferencias entre años."],
    explain=[
        "El parlamentarismo es un sistema donde el gobierno depende del Parlamento, una asamblea que representa a la población. Fue un modelo de representatividad: el monarca podía seguir existiendo, pero las decisiones importantes pasaban por representantes. El constitucionalismo es la idea de que el poder se limita por una constitución escrita que fija derechos y reglas.",
        "Para analizar un proceso hay que mirar qué cambió y qué continuó. Cambió que las autoridades debían rendir cuentas a asambleas y a leyes escritas. Continuó que muchas personas quedaban fuera: en la ficha, las mujeres no votaban en ninguno de los casos y en Chile votaba solo quien cumplía requisitos de renta o propiedad, lo que se llama voto censitario.",
        "También importa el territorio. Las ideas nacieron sobre todo en Europa y Estados Unidos, pero en América Latina se adaptaron a sociedades con esclavitud, grandes propiedades de tierra y población indígena. La ampliación de la ciudadanía, es decir, que más personas tuvieran derechos políticos, fue lenta y desigual según el país.",
    ],
    vocab=[("parlamentarismo", "sistema donde el gobierno depende de la confianza del Parlamento"), ("constitucionalismo", "idea de limitar el poder con una constitución escrita"), ("voto censitario", "voto reservado a quienes cumplen requisitos de renta o propiedad"), ("sufragio", "derecho a votar"), ("representatividad", "capacidad de un grupo de personas elegidas para hablar por una población")],
    worked=[
        ("Medir un desfase", "¿Cuántos años después del fin de la esclavitud en Estados Unidos terminó en Cuba?", ["Tomo 1865 y 1886 de la ficha.", "Resto: 1886 − 1865 = 21."], "21 años"),
        ("Señalar una continuidad", "En Francia, 1848, ¿qué grupo siguió sin votar aunque el sufragio se amplió?", ["La ficha dice que votan todos los hombres adultos.", "Dice también que las mujeres no votan."], "Las mujeres"),
    ],
    mistakes=[("Decir que el sufragio universal masculino significaba que votaba toda la población.", "Se olvida que dejaba fuera a las mujeres.", "Escribe «todos los hombres adultos» y nota quiénes no estaban."),
              ("Creer que el cambio político borró enseguida la esclavitud.", "La ficha muestra fechas de abolición muy posteriores al inicio del liberalismo.", "Compara años de cada país antes de afirmar.")],
    T=[
        ("{F} ¿De qué depende el gobierno en un sistema parlamentario?", "De la confianza del Parlamento", "La ficha lo dice para Gran Bretaña."),
        ("{F} ¿Qué tipo de voto existía en Chile con la Constitución de 1833?", "Voto censitario", "La ficha lo nombra y lo define por requisitos de renta o propiedad."),
        ("{F} ¿En qué año se estableció en Francia el voto de todos los hombres adultos?", "1848", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre el fin de la esclavitud en Estados Unidos y en Brasil?", "1888-1865", "Se resta el año estadounidense al brasileño.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la reforma del voto en Gran Bretaña y el voto masculino universal en Francia?", "1848-1832", "Se resta el año de Gran Bretaña al de Francia.", " años"),
        ("{F} De estos dos países, ¿cuál abolió la esclavitud más tarde que el otro? A) Cuba B) Estados Unidos", "A) Cuba", "Cuba abolió en 1886, después de Estados Unidos (1865)."),
        ("{F} Ordena por fecha de abolición de la esclavitud, de la más temprana a la más tardía: Cuba, Estados Unidos, Brasil.", "Estados Unidos, Cuba, Brasil", "Los años son 1865, 1886 y 1888."),
        ("{F} ¿Qué continuidad aparece en los tres casos políticos de la ficha (Gran Bretaña, Francia y Chile)? A) Las mujeres no votaban B) Todos los hombres votaban", "A) Las mujeres no votaban", "Ni Francia ni Chile ni Gran Bretaña les daban voto en esas fechas."),
        ("{F} Un país tiene constitución escrita pero el gobierno puede cambiarla sin límites. ¿Cumple el constitucionalismo? A) No, porque el poder no queda limitado por la constitución B) Sí, porque tiene un texto escrito", "A) No, porque el poder no queda limitado por la constitución", "El constitucionalismo exige que la constitución limite el poder."),
        ("{F} ¿Por qué se puede decir que en Chile, en 1833, la república tenía representatividad limitada?", "Porque votaba solo quien cumplía requisitos de renta o propiedad", "El voto censitario reduce quiénes pueden elegir."),
        ("{F} ¿Qué cambio y qué continuidad hay en Francia en 1848?", "Cambió que votan todos los hombres adultos; continuó que las mujeres no votaban", "La ficha muestra una ampliación y una exclusión que se mantiene."),
        ("{F} Un compañero dice: «Con el liberalismo, la esclavitud terminó en toda América en el mismo año». Usa la ficha para refutarlo.", "La ficha muestra tres años distintos: 1865, 1886 y 1888", "Las fechas de abolición no coinciden entre los países de la ficha."),
        ("{F} ¿Qué conclusión es más ajustada a la ficha? A) Las ideas liberales ampliaron derechos, pero de forma lenta y desigual B) Las ideas liberales dieron derechos iguales a toda la población en 1848", "A) Las ideas liberales ampliaron derechos, pero de forma lenta y desigual", "La ficha mezcla avances con exclusiones de mujeres y de personas esclavizadas."),
    ],
    ctx=("Un museo presenta una vitrina con la frase «Con el parlamentarismo el rey dejó de existir en Europa». ¿Cómo la corriges? A) El rey seguía existiendo en Gran Bretaña, con poderes limitados y un gobierno que dependía del Parlamento B) El rey nunca perdió poder", "A) El rey seguía existiendo en Gran Bretaña, con poderes limitados y un gobierno que dependía del Parlamento", "La ficha dice que el monarca reina con poderes limitados."),
    sc=[("¿Qué es el voto censitario?", "Voto solo para quienes cumplen requisitos de renta o propiedad", "Así se explica en la clase."),
        ("¿Qué es el constitucionalismo?", "Limitar el poder con una constitución escrita", "Esa es su definición."),
        ("=", "¿Cuántos años pasaron entre 1833 y 1888?", "1888-1833", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla de dos columnas, «Cambió» y «Continuó», con tres filas cada una, usando solo los datos de la ficha (por ejemplo, sobre quién votaba o la esclavitud). Luego escribe una frase que diga en qué país te parece más claro el avance de la ciudadanía y por qué. {F}",
        "Cambió: más hombres votaban en Francia (1848); el gobierno dependía del Parlamento en Gran Bretaña; Chile tenía constitución escrita (1833). Continuó: las mujeres no votaban; en Chile se exigía renta o propiedad; la esclavitud siguió hasta 1865, 1886 y 1888. Frase: «En Francia el avance es más claro porque votan todos los hombres adultos».",
        ["usa datos de la ficha", "separa cambio y continuidad", "justifica la elección con evidencia"], ["tabla completa", "frase con justificación"], ["escribir ideas sin sustento en la ficha", "poner el mismo dato en las dos columnas"],
        "Pide que diga qué grupo seguía excluido y por qué eso importa al hablar de ciudadanía."),
    reinforce="Explica a una persona de tu casa qué es el parlamentarismo y qué quedó igual aunque cambió el sistema.",
    extend="Averigua si en tu región o comuna hay una asamblea elegida (concejo municipal) y qué decide. Escribe una frase.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno; resumen de posturas posibles en el siglo XIX). "
     "Comerciante liberal: quiere comerciar con otros países y pagar menos aranceles (impuestos a los productos que cruzan la frontera). "
     "Artesano de ciudad: teme que las telas importadas, más baratas, arruinen su taller. "
     "Conservador: quiere mantener el orden y la influencia de la Iglesia y de las familias tradicionales. "
     "Abolicionista: pide terminar con la esclavitud porque cada persona nace libre. "
     "Mujer de clase media: pide ser reconocida como ciudadana con derecho a votar.")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores y perspectivas del liberalismo: quién ganaba, quién perdía y por qué cada uno opinaba distinto.",
    prior=["Sé que las fuentes expresan intereses.", "Sé qué es libre mercado y voto censitario.", "Sé comparar cambio y continuidad."],
    explain=[
        "Un actor histórico es una persona o grupo que toma decisiones o es afectado por ellas. En el siglo XIX, las ideas liberales no se vivieron igual para todos. Un comerciante podía ganar con el libre mercado, porque vendía a más lugares. Un artesano podía perder, porque competía con productos importados más baratos. Por eso una misma idea tuvo apoyo y rechazo.",
        "También hubo conflictos sobre el poder y los derechos. Los conservadores defendían el orden tradicional y la influencia de la Iglesia; los liberales querían limitar el poder del gobierno; los abolicionistas pedían terminar con la esclavitud, y muchas mujeres pedían derechos políticos. La libre asociación, es decir, el derecho a organizar grupos como sociedades o partidos, permitió que estas voces se organizaran.",
        "Para contrastar perspectivas se comparan tres cosas: qué quiere cada actor, qué le conviene y qué teme. Una buena explicación evita culpar a una sola causa. Por ejemplo, la abolición de la esclavitud tuvo causas morales, económicas y políticas a la vez, y no todos los que la apoyaron lo hicieron por la misma razón.",
    ],
    vocab=[("actor", "persona o grupo que participa en un proceso histórico"), ("perspectiva", "punto de vista de un actor según sus intereses"), ("arancel", "impuesto a los productos que cruzan una frontera"), ("libre asociación", "derecho de organizar grupos, sociedades o partidos"), ("conservador", "quien defiende mantener el orden y las instituciones tradicionales")],
    worked=[
        ("Identificar quién gana", "Un gobierno baja los aranceles. Según la ficha, ¿qué actor se beneficia más?", ["Bajar aranceles abarata el comercio con otros países.", "El comerciante liberal quiere comerciar y pagar menos aranceles."], "El comerciante liberal"),
        ("Identificar quién teme", "El mismo gobierno baja los aranceles. ¿Qué actor pierde y por qué?", ["Entran telas importadas más baratas.", "El artesano teme que arruinen su taller."], "El artesano, porque compite con productos importados baratos"),
    ],
    mistakes=[("Explicar el liberalismo como si todos lo apoyaran por igual.", "Se ignora que los artesanos, los conservadores y otros tenían intereses distintos.", "Pregunta qué ganaba y qué perdía cada actor."),
              ("Atribuir la abolición a una sola causa.", "Se simplifica un proceso con causas morales, económicas y políticas.", "Nombra al menos dos causas y a los actores que las impulsaron.")],
    T=[
        ("{F} ¿Qué actor teme que las telas importadas arruinen su taller?", "El artesano", "La ficha lo dice de forma directa."),
        ("{F} ¿Qué pide el abolicionista?", "Terminar con la esclavitud", "La ficha resume su postura."),
        ("{F} ¿Qué es un arancel según la ficha?", "Un impuesto a los productos que cruzan la frontera", "La ficha lo define entre paréntesis."),
        ("{F} ¿Qué actor quiere mantener la influencia de la Iglesia y de las familias tradicionales?", "El conservador", "La ficha lo describe así."),
        ("{F} Un gobierno prohíbe la importación de telas. ¿Qué actor se beneficia más? A) El artesano de ciudad B) El comerciante liberal", "A) El artesano de ciudad", "Sin competencia extranjera, el artesano protege su taller."),
        ("{F} Un gobierno permite que cualquier grupo forme sociedades y partidos. ¿Qué actor puede aprovechar esa libertad para reclamar derechos políticos? A) La mujer de clase media B) El comerciante que paga aranceles", "A) La mujer de clase media", "La libre asociación permite organizar grupos para pedir derechos como el voto."),
        ("{F} ¿Qué actor quiere tener derecho a votar? A) Mujer de clase media B) Conservador", "A) Mujer de clase media", "La ficha dice que pide ser reconocida como ciudadana."),
        ("{F} ¿Qué actor se opondría más a una ley que reduzca la influencia de la Iglesia? A) El conservador B) El abolicionista", "A) El conservador", "El conservador defiende esa influencia en la ficha."),
        ("{F} Un compañero dice: «El comerciante y el artesano opinan igual sobre los aranceles». Corrígelo.", "El comerciante quiere pagar menos aranceles y el artesano teme la competencia importada", "Sus intereses son distintos: uno vende afuera y el otro compite con lo que entra."),
        ("{F} ¿Por qué no se puede explicar la abolición solo con ideas morales?", "Porque también hubo causas económicas y políticas y actores con intereses distintos", "La clase explica que hubo causas morales, económicas y políticas."),
        ("{F} ¿Qué tienen en común el abolicionista y la mujer de clase media? A) Piden que se reconozcan derechos a personas que no los tenían B) Piden pagar menos aranceles", "A) Piden que se reconozcan derechos a personas que no los tenían", "El abolicionista pide libertad para las personas esclavizadas y la mujer pide derecho a votar; ninguno habla de aranceles."),
        ("{F} ¿Qué perspectiva falta en la ficha para entender mejor el tema? A) La de personas esclavizadas B) La de los comerciantes", "A) La de personas esclavizadas", "La ficha cita al abolicionista pero no a quienes vivían la esclavitud."),
        ("{F} Dos compañeros explican la abolición. Ana dice: «Se abolió solo por razones morales». Luis dice: «Se abolió solo por razones económicas». ¿Qué respuesta es más completa? A) Hubo causas morales, económicas y políticas, con actores distintos B) Ana tiene razón porque la moral es lo más importante", "A) Hubo causas morales, económicas y políticas, con actores distintos", "La clase explica que la abolición tuvo varias causas y no una sola."),
    ],
    ctx=("Para un trabajo sobre el libre mercado, un compañero solo entrevista al comerciante liberal. ¿Qué le recomiendas? A) Agregar la voz del artesano para mostrar quién pierde B) Mantener solo la del comerciante porque es la más importante", "A) Agregar la voz del artesano para mostrar quién pierde", "Contrastar actores exige incluir a quienes ganan y a quienes pierden."),
    sc=[("¿Qué es una perspectiva?", "El punto de vista de un actor según sus intereses", "Así se define en el vocabulario."),
        ("¿Qué actor gana con aranceles bajos en la ficha?", "El comerciante liberal", "Quiere comerciar y pagar menos aranceles."),
        ("¿Qué grupo pide derecho a voto en la ficha?", "La mujer de clase media", "Pide ser reconocida como ciudadana.")],
    op=("Elige dos actores de la ficha. En una tabla de tres columnas escribe, para cada uno: qué quiere, qué le conviene y qué teme. Luego redacta dos frases que expliquen por qué sus perspectivas chocan. {F}",
        "Comerciante: quiere vender fuera; le conviene pagar menos aranceles; teme los impuestos altos. Artesano: quiere proteger su taller; le conviene limitar importaciones; teme la competencia barata. Frases: «El comerciante gana con aranceles bajos y el artesano pierde. Por eso sus intereses chocan».",
        ["elige dos actores de la ficha", "completa quiere, conviene y teme", "explica el choque con evidencia"], ["tabla de tres columnas", "dos frases"], ["escribir lo mismo para ambos actores", "explicar con opiniones sin base en la ficha"],
        "Pide que explique quién tiene más poder para que su opinión se cumpla."),
    reinforce="Elige un actor de la ficha y explica en voz alta qué quiere, qué le conviene y qué teme.",
    extend="Piensa en una decisión actual de tu comuna (por ejemplo, abrir una feria). Nombra un actor que gana y uno que pierde.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento; fechas reales y afirmaciones de ejemplo). "
     "Pregunta: ¿las ideas liberales ampliaron la ciudadanía en el siglo XIX? "
     "Dato 1: Francia, 1848, voto de todos los hombres adultos. "
     "Dato 2: Chile, 1833, voto censitario con requisitos de renta o propiedad. "
     "Dato 3: Brasil, 1888, fin de la esclavitud. "
     "Dato 4: en ninguno de los países de los datos 1 y 2 votaban las mujeres.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento escrito: una afirmación, evidencia de fuentes y una explicación que las une, con una conclusión proporcional.",
    prior=["Sé contrastar actores y perspectivas.", "Sé distinguir descripción de interpretación.", "Sé que una conclusión no puede decir más que la evidencia."],
    explain=[
        "Un argumento histórico tiene tres partes. La afirmación responde a la pregunta: «la ciudadanía se amplió, pero de forma parcial». La evidencia son los datos de las fuentes que la apoyan: por ejemplo, el voto masculino universal de 1848 en Francia. El razonamiento explica por qué esa evidencia apoya la afirmación.",
        "Un buen argumento también reconoce límites. Si hay datos que muestran avances y otros que muestran exclusiones, la conclusión debe incluir ambos. Si dices «todos obtuvieron derechos», estás diciendo más de lo que la evidencia permite. Un adverbio como «parcialmente» o «lentamente» puede ser lo que hace correcta tu conclusión.",
        "Para evaluar un argumento se pregunta: ¿la afirmación responde la pregunta?, ¿cada evidencia es verdadera y está citada?, ¿el razonamiento conecta evidencia y afirmación? y ¿la conclusión es proporcional? Esta estructura sirve para cualquier tema de historia, no solo para el liberalismo.",
    ],
    vocab=[("afirmación", "respuesta que defiendes a una pregunta histórica"), ("evidencia", "dato de una fuente que sostiene la afirmación"), ("razonamiento", "explicación que conecta evidencia y afirmación"), ("conclusión proporcional", "conclusión que no dice más de lo que prueba la evidencia"), ("contraargumento", "dato o idea que va en contra de tu afirmación")],
    worked=[
        ("Elegir evidencia", "Afirmación: «En Francia se amplió la ciudadanía en 1848». ¿Cuál dato de la ficha la apoya?", ["Busco un dato sobre Francia.", "El dato 1 habla del voto de todos los hombres adultos."], "Dato 1"),
        ("Detectar un exceso", "Alguien concluye: «En el siglo XIX toda la población obtuvo derechos políticos». ¿Qué dato de la ficha lo contradice?", ["La conclusión dice «toda la población».", "El dato 4 dice que las mujeres no votaban."], "El dato 4"),
    ],
    mistakes=[("Escribir una conclusión absoluta («todos», «siempre») con datos parciales.", "La evidencia muestra avances y exclusiones a la vez.", "Usa palabras de grado como «parcialmente» y cita el límite."),
              ("Dar una evidencia que no tiene relación con la afirmación.", "No se explica el vínculo entre dato y afirmación.", "Añade una frase de razonamiento que conecte ambos.")],
    T=[
        ("{F} ¿Qué dato de la ficha apoya la idea de que hubo ampliación del voto?", "El dato 1, el voto de todos los hombres adultos en Francia en 1848", "Es el dato que muestra más personas votando."),
        ("{F} ¿Qué dato muestra una limitación del voto por riqueza?", "El dato 2, el voto censitario en Chile en 1833", "Los requisitos de renta o propiedad limitan quién vota."),
        ("{F} ¿Qué parte de un argumento es el dato tomado de una fuente?", "La evidencia", "La evidencia son los datos que sostienen la afirmación."),
        ("=", "{F} ¿Cuántos años pasaron entre el voto censitario de Chile y el fin de la esclavitud en Brasil de la ficha?", "1888-1833", "Se resta el año de Chile al de Brasil.", " años"),
        ("{F} ¿Qué afirmación responde mejor la pregunta de la ficha? A) La ciudadanía se amplió parcialmente, porque siguieron excluidas las mujeres y otros grupos B) La ciudadanía no cambió en todo el siglo", "A) La ciudadanía se amplió parcialmente, porque siguieron excluidas las mujeres y otros grupos", "Reúne el avance (dato 1) y la exclusión (datos 2 y 4)."),
        ("{F} ¿Qué dato usarías como evidencia de exclusión? A) El dato 4 B) El dato 1", "A) El dato 4", "El dato 4 dice que las mujeres no votaban."),
        ("{F} Completa el razonamiento: «El dato 3 apoya la afirmación porque…» ¿Qué opción corresponde? A) El fin de la esclavitud en 1888 muestra que se reconoció la libertad personal, pero muy tarde B) El fin de la esclavitud muestra que no hubo cambios", "A) El fin de la esclavitud en 1888 muestra que se reconoció la libertad personal, pero muy tarde", "Conecta el dato con la afirmación de avance parcial."),
        ("{F} Un compañero escribe: «Con el dato 1 queda probado que toda persona votó en Francia en 1848». ¿Qué le corriges?", "Que votaban los hombres adultos, no las mujeres", "El dato 4 muestra que las mujeres no votaban en esos países."),
        ("{F} ¿Por qué el dato 2 funciona como contraargumento de la afirmación «el voto se abrió a todos los chilenos»?", "Porque en Chile se exigían renta o propiedad", "El voto censitario excluye a quienes no cumplen requisitos."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «parcialmente» B) «totalmente»", "A) «parcialmente»", "La evidencia mezcla avances con exclusiones."),
        ("{F} Ordena las partes de un argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y luego se explica el vínculo."),
        ("{F} Un compañero responde a la pregunta solo con el dato 1 y el dato 3. ¿Qué dato debería sumar para ser más equilibrado? A) El dato 2 o el 4, que muestran límites B) Otro dato igual al dato 1", "A) El dato 2 o el 4, que muestran límites", "Un argumento equilibrado incluye avances y límites."),
        ("{F} ¿Qué conclusión es la más ajustada a todos los datos? A) Las ideas liberales ampliaron la ciudadanía de manera desigual y con límites B) Las ideas liberales ampliaron la ciudadanía de manera total", "A) Las ideas liberales ampliaron la ciudadanía de manera desigual y con límites", "Los cuatro datos muestran avance y exclusión."),
    ],
    ctx=("Un diario escolar publica: «El liberalismo trajo igualdad plena a toda América en el siglo XIX». ¿Qué evidencia de la ficha usarías para responder? A) El voto censitario de Chile en 1833 y que las mujeres no votaban B) Solo el fin de la esclavitud en Brasil", "A) El voto censitario de Chile en 1833 y que las mujeres no votaban", "Ambos datos muestran límites a la igualdad."),
    sc=[("En un argumento, ¿cómo se llama el dato tomado de una fuente que sostiene la afirmación?", "La evidencia", "Así se llama en la clase el dato que sostiene la afirmación."),
        ("¿Qué es una conclusión proporcional?", "La que no dice más de lo que prueba la evidencia", "Así se define en el vocabulario."),
        ("=", "¿Cuántos años pasaron entre 1848 y 1888?", "1888-1848", "Se resta el año menor al mayor.", " años")],
    op=("Escribe un párrafo de cinco a siete líneas que responda: «¿Las ideas liberales ampliaron la ciudadanía en el siglo XIX?». Usa al menos dos datos de la ficha y un dato que muestre un límite. Marca con una raya la afirmación, la evidencia y el razonamiento. {F}",
        "«Las ideas liberales ampliaron la ciudadanía de forma parcial. En Francia, en 1848, votaron todos los hombres adultos, lo que muestra una ampliación. Sin embargo, en Chile el voto de 1833 exigía renta o propiedad y las mujeres no votaban en ninguno de los dos casos. Por eso la ampliación fue desigual».",
        ["responde la pregunta", "usa dos datos y un límite", "incluye razonamiento y conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["usar «todos» sin evidencia", "citar datos sin explicar el vínculo"],
        "Pide que cuente qué dato nuevo le gustaría conseguir para mejorar su argumento."),
    reinforce="Elige un dato de la ficha y explica en voz alta cómo lo conectarías con la afirmación.",
    extend="Escribe un contraargumento a tu párrafo y responde con un dato de la ficha.",
)
