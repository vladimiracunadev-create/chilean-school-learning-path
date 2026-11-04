"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 06 (imperialismo, capitalismo y pueblos colonizados)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 06"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (siglo XIX: años 1801 a 1900). "
     "Imperialismo: dominio político y económico que ejercen potencias sobre otros territorios; en la segunda mitad del siglo XIX se expandió sobre todo en África y Asia. "
     "Colonia: territorio gobernado desde afuera por otra potencia. "
     "Capitalismo: sistema económico donde el capital privado se invierte para obtener ganancias. "
     "Potencias imperiales: Gran Bretaña, Francia, Alemania, Bélgica, Italia, Rusia, Estados Unidos y Japón. "
     "Hitos: Guerra del Opio entre Gran Bretaña y China, 1839–1842; Canal de Suez, 1869; Conferencia de Berlín sobre el reparto de África, 1884–1885; batalla de Adwa, en que Etiopía derrota a Italia, 1896.")
build(
    OA, 1, F,
    use="Aprenderé a situar el imperialismo europeo del siglo XIX en el tiempo y en el espacio, y a plantear la pregunta que guía este tema: ¿cómo cambió el mapa del mundo y cómo se vincula con el capitalismo?",
    prior=["Sé qué es la industrialización.", "Sé qué es un Estado y una frontera.", "Sé calcular diferencias entre años."],
    explain=[
        "El imperialismo es el dominio político y económico que ejercen algunas potencias sobre otros territorios. Durante la segunda mitad del siglo XIX, potencias como Gran Bretaña, Francia, Alemania y Bélgica se repartieron gran parte de África y Asia. Un territorio gobernado desde afuera se llama colonia. Estados Unidos y Japón también se expandieron, así que el fenómeno no fue solo europeo.",
        "El imperialismo se relaciona con el capitalismo, el sistema donde el capital privado se invierte para obtener ganancias. Las fábricas necesitaban materias primas y mercados donde vender, y los capitalistas buscaban lugares para invertir. Además influyeron razones políticas, como el prestigio y la rivalidad entre potencias, y razones ideológicas, como la creencia en la superioridad de unos pueblos sobre otros, que hoy se rechaza.",
        "Situar el fenómeno exige tiempo y espacio. La Conferencia de Berlín de 1884–1885 fijó reglas para el reparto de África entre potencias europeas, sin que los pueblos africanos participaran. También hubo resistencia, como la victoria de Etiopía sobre Italia en la batalla de Adwa en 1896. Hay que evitar pensar que los pueblos colonizados fueron solo pasivos.",
    ],
    vocab=[("imperialismo", "dominio político y económico de potencias sobre otros territorios"), ("colonia", "territorio gobernado desde afuera por otra potencia"), ("capitalismo", "sistema económico donde el capital privado se invierte para obtener ganancias"), ("materia prima", "recurso natural usado para producir otros bienes"), ("resistencia", "oposición de un pueblo a un dominio externo")],
    worked=[
        ("Calcular una diferencia de años", "La ficha da dos años para la Conferencia de Berlín: 1884 y 1885. ¿Cuántos años de diferencia hay entre ellos?", ["Tomo los dos años de la ficha.", "Resto: 1885 − 1884 = 1."], "1 año"),
        ("Calcular una diferencia", "¿Cuántos años pasaron entre la Guerra del Opio (inicio 1839) y el Canal de Suez (1869)?", ["Tomo los años de la ficha.", "Resto: 1869 − 1839 = 30."], "30 años"),
    ],
    mistakes=[("Decir que solo las potencias europeas fueron imperialistas.", "Estados Unidos y Japón también se expandieron.", "Nombra a todas las potencias de la ficha."),
              ("Creer que los pueblos colonizados no se resistieron.", "Hubo resistencia, como Adwa en 1896.", "Incluye ejemplos de resistencia.")],
    T=[
        ("{F} ¿En qué continentes se expandió sobre todo el imperialismo en la segunda mitad del siglo XIX?", "África y Asia", "La ficha lo indica."),
        ("{F} ¿Qué es una colonia?", "Un territorio gobernado desde afuera por otra potencia", "La ficha la define."),
        ("{F} ¿Qué país derrotó a Italia en la batalla de Adwa?", "Etiopía", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre el Canal de Suez y la batalla de Adwa?", "1896-1869", "Se resta el año del Canal al de Adwa.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Guerra del Opio (inicio) y la Conferencia de Berlín (inicio)?", "1884-1839", "Se resta el año de inicio de la Guerra del Opio al de la Conferencia.", " años"),
        ("{F} ¿Qué hito pertenece primero? A) Guerra del Opio B) Conferencia de Berlín", "A) Guerra del Opio", "1839 es anterior a 1884."),
        ("{F} Una fábrica necesita algodón y no lo produce en su país. ¿Qué razón del imperialismo ilustra? A) La necesidad de materias primas B) La rivalidad por el prestigio entre potencias", "A) La necesidad de materias primas", "Las fábricas buscaban materias primas en otros territorios."),
        ("{F} Una empresa invierte dinero en una mina en otro continente para obtener ganancias. ¿Qué sistema económico muestra? A) Capitalismo B) Autoconsumo", "A) Capitalismo", "El capital privado se invierte para ganar."),
        ("{F} ¿Quiénes participaron en la Conferencia de Berlín al repartirse África? A) Potencias europeas, sin pueblos africanos B) Pueblos africanos y europeos por igual", "A) Potencias europeas, sin pueblos africanos", "La explicación lo señala."),
        ("{F} ¿Por qué la victoria de Etiopía en Adwa es importante para entender el imperialismo?", "Porque muestra que hubo resistencia de pueblos colonizados", "Los pueblos no fueron solo pasivos."),
        ("{F} Un compañero dice: «Solo Europa se expandió». Corrígelo con la ficha.", "Estados Unidos y Japón también se expandieron", "La ficha los incluye entre las potencias."),
        ("{F} ¿Cuál es la mejor pregunta histórica? A) ¿Cómo el imperialismo cambió el mapa del mundo y se relacionó con el capitalismo? B) ¿Qué colonia tenía el mejor paisaje?", "A) ¿Cómo el imperialismo cambió el mapa del mundo y se relacionó con el capitalismo?", "La A se responde con hechos."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y va de 1830 a 1900. ¿Cuántos centímetros mide?", "7 cm", "Se divide el tramo de 70 años por 10."),
    ],
    ctx=("Un museo cuelga la frase «Todos los pueblos aceptaron el dominio imperial». ¿Qué ejemplo de la ficha lo contradice? A) La victoria de Etiopía en Adwa, 1896 B) El Canal de Suez, 1869", "A) La victoria de Etiopía en Adwa, 1896", "Muestra que hubo resistencia al dominio."),
    sc=[("¿Qué es el imperialismo?", "El dominio político y económico de potencias sobre otros territorios", "Así se define."),
        ("¿Qué es el capitalismo?", "Un sistema donde el capital privado se invierte para obtener ganancias", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1869 y 1884?", "1884-1869", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1830 a 1900 con escala 1 cm = 10 años y marca: Guerra del Opio (1839), Canal de Suez (1869), Conferencia de Berlín (1884) y batalla de Adwa (1896). Debajo escribe dos frases: una que defina imperialismo y otra que diga cómo se relaciona con el capitalismo. {F}",
        "Posiciones desde 1830: 0,9; 3,9; 5,4; 6,6 cm. Frases: «El imperialismo es el dominio político y económico de potencias sobre otros territorios»; «Las fábricas capitalistas buscaban materias primas, mercados e inversiones».",
        ["respeta la escala", "los cuatro hitos bien ubicados", "las definiciones son correctas"], ["línea de tiempo", "dos frases"], ["no medir con la escala", "confundir imperialismo con capitalismo"],
        "Pide que explique qué voz falta en la Conferencia de Berlín."),
    reinforce="Explica en voz alta qué es el imperialismo y da dos razones de su expansión.",
    extend="Busca en tu casa un producto que venga de otro continente y piensa cómo llegó hasta ti.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, carta de un empresario europeo a su socio, 1890: «Esa colonia tiene caucho y marfil en abundancia. Si conseguimos el permiso del gobierno, venderemos en Europa a buen precio. Los habitantes trabajarán por poco dinero.» "
     "Fuente B, relato oral de una mujer de un pueblo colonizado, recogido décadas después (ejemplo): «Los soldados llegaron y nos obligaron a trabajar en las plantaciones. Nos cobraron un impuesto que no podíamos pagar y perdimos nuestras tierras.»")
build(
    OA, 2, F,
    use="Aprenderé a contextualizar y comparar fuentes sobre el imperialismo: la de un empresario y la de una persona colonizada, para ver qué voces faltan.",
    prior=["Sé qué es el imperialismo.", "Sé contextualizar una fuente.", "Sé que una fuente expresa intereses."],
    explain=[
        "La carta del empresario es una fuente privada y económica: muestra qué buscaba, cuáles eran sus intereses. Habla de caucho, marfil, precios y salarios bajos. No habla de lo que pensaban los habitantes. El relato oral de una mujer colonizada es un testimonio que se recogió décadas después: tiene valor porque da una voz que suele faltar, pero también puede haberse modificado por el tiempo.",
        "Para comparar, se contextualiza cada fuente: quién la hizo, cuándo, para qué. La carta busca ganancias; el relato busca contar una experiencia de pérdida. Ambas son parciales. La comparación permite construir una visión más completa: los intereses económicos de unos y los costos humanos de otros.",
        "Un historiador no toma una fuente como una verdad total. Se pregunta qué dice, qué calla y qué fuentes faltan. Aquí faltan, por ejemplo, voces de autoridades coloniales o de líderes locales. Una conclusión debe ser proporcional: lo que muestran estas dos fuentes, y no lo que ocurrió en todas las colonias.",
    ],
    vocab=[("testimonio", "relato de una persona sobre algo que vivió"), ("relato oral", "historia contada de palabra y no escrita"), ("plantación", "gran terreno de cultivo comercial con muchos trabajadores"), ("impuesto", "pago obligatorio al Estado"), ("parcial", "que muestra solo una parte de la realidad")],
    worked=[
        ("Contextualizar", "¿Quién escribe la Fuente A, cuándo y para qué?", ["Autor: un empresario europeo.", "Fecha: 1890. Propósito: informar a su socio sobre negocios."], "Un empresario europeo, en 1890, para hablar de negocios"),
        ("Descripción o interpretación", "(1) «El empresario menciona caucho y marfil». (2) «El empresario odiaba a los habitantes». ¿Cuál es descripción?", ["La (1) repite el texto.", "La (2) agrega un sentimiento que no aparece."], "La (1) describe; la (2) interpreta de más"),
    ],
    mistakes=[("Tomar la carta del empresario como la verdad de la colonia.", "Muestra su interés económico, no la vida de los habitantes.", "Compara con la voz de las personas colonizadas."),
              ("Concluir que todas las colonias eran iguales.", "Las dos fuentes son de casos específicos.", "Escribe «en este caso»")],
    T=[
        ("{F} ¿Qué productos nombra el empresario?", "Caucho y marfil", "La carta los menciona."),
        ("{F} ¿Qué obligaron a hacer a la mujer del relato oral y a su pueblo?", "Trabajar en las plantaciones", "El relato lo dice."),
        ("{F} ¿Qué perdieron según el relato oral?", "Sus tierras", "El relato lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre la carta de 1890 y 1900?", "1900-1890", "Se resta el año de la carta a 1900.", " años"),
        ("{F} ¿Qué fuente muestra los intereses económicos de una potencia? A) La Fuente A B) La Fuente B", "A) La Fuente A", "Habla de ganancias y precios."),
        ("{F} ¿Qué fuente muestra los costos humanos del imperialismo? A) La Fuente B B) La Fuente A", "A) La Fuente B", "Cuenta trabajo forzado y pérdida de tierras."),
        ("{F} ¿Qué frase describe la Fuente A? A) El empresario dice que los habitantes trabajarán por poco dinero B) El empresario sentía culpa por la colonia", "A) El empresario dice que los habitantes trabajarán por poco dinero", "La B agrega un sentimiento que no está en el texto."),
        ("{F} ¿Qué valor tiene un relato oral recogido décadas después? A) Da una voz que suele faltar, aunque el tiempo pudo modificarlo B) Es siempre una prueba exacta", "A) Da una voz que suele faltar, aunque el tiempo pudo modificarlo", "Es testimonio, no registro exacto."),
        ("{F} ¿Qué voz falta en estas dos fuentes? A) Autoridades coloniales o líderes locales B) El empresario", "A) Autoridades coloniales o líderes locales", "Ninguna de las dos fuentes las incluye."),
        ("{F} ¿Por qué la carta del empresario no es suficiente para conocer la vida en la colonia?", "Porque expresa sus intereses económicos y no la experiencia de los habitantes", "Es una fuente parcial."),
        ("{F} Un compañero concluye: «Todos los habitantes de las colonias perdieron sus tierras». ¿Qué corrección haces?", "El relato es de una mujer en un caso específico", "No permite generalizar."),
        ("{F} ¿Qué relación hay entre las dos fuentes? A) Muestran los intereses de unos y los costos de otros B) Muestran lo mismo", "A) Muestran los intereses de unos y los costos de otros", "Las dos fuentes se complementan entre sí."),
        ("{F} ¿Qué conclusión es más proporcional? A) Estas dos fuentes muestran un interés económico y una experiencia de pérdida en casos concretos B) Estas fuentes prueban lo que ocurrió en todas las colonias", "A) Estas dos fuentes muestran un interés económico y una experiencia de pérdida en casos concretos", "No dice más de lo que muestran."),
    ],
    ctx=("Un grupo prepara una exposición sobre el imperialismo y solo usa cartas de empresarios. ¿Qué recomiendas? A) Sumar testimonios de personas colonizadas B) Usar más cartas de empresarios", "A) Sumar testimonios de personas colonizadas", "Aporta la voz que falta."),
    sc=[("¿Qué es un testimonio?", "El relato de una persona sobre algo que vivió", "Así se define."),
        ("¿Qué es una fuente parcial?", "Una que muestra solo una parte de la realidad", "Así se define."),
        ("¿Quién escribe la Fuente A?", "Un empresario europeo", "La ficha lo indica.")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (una frase); qué interpretas (con «Esto sugiere que…»). Cierra con una frase sobre qué no puedes concluir y qué voz falta. {F}",
        "Fuente B. Autor y fecha: una mujer de un pueblo colonizado, relato recogido décadas después. Dice: la obligaron a trabajar en plantaciones y perdió sus tierras. Interpretación: esto sugiere que los impuestos y el trabajo forzado afectaron a su comunidad. No puedo concluir que fue igual en todas las colonias; falta la voz de las autoridades coloniales.",
        ["contextualiza", "separa descripción e interpretación", "señala límite y voz ausente"], ["tabla de tres filas", "frase de cierre"], ["usar un juicio como descripción", "generalizar"],
        "Pide que cuente qué pregunta haría a la mujer del relato."),
    reinforce="Explica por qué una carta de empresario y un relato oral informan cosas distintas.",
    extend="Pregunta a una persona mayor de tu casa un recuerdo de su niñez y anota quién cuenta, cuándo y para qué.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cambios en el mapa; porcentajes redondeados y de ejemplo). "
     "África bajo control europeo, porcentaje del territorio: hacia 1870, cerca del 10 %; hacia 1914, cerca del 90 %. En 1914 solo Etiopía y Liberia seguían independientes. "
     "Fronteras coloniales: muchas se trazaron con líneas rectas, sin considerar los pueblos que vivían allí. "
     "Economía colonial: se cultivaba y se extraía lo que necesitaba la potencia (caucho, algodón, minerales) y se compraban productos industriales de la potencia. "
     "Continuidades: muchas fronteras trazadas por las potencias se mantuvieron al independizarse los territorios en el siglo XX.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio en el imperialismo: cómo cambió el mapa mundial y qué se mantuvo.",
    prior=["Sé qué es el imperialismo y una colonia.", "Sé calcular diferencias y porcentajes simples.", "Sé leer un mapa o cuadro."],
    explain=[
        "El mapa del mundo se reconfiguró entre 1870 y 1914. En África, el porcentaje del territorio controlado por potencias europeas pasó de cerca del 10 % a cerca del 90 %. Solo Etiopía y Liberia seguían independientes en 1914. Este cambio fue muy rápido y se produjo con acuerdos entre potencias, y no con consulta a los pueblos africanos.",
        "Las fronteras coloniales se trazaron muchas veces con líneas rectas, sin considerar a los pueblos que vivían allí. Algunos pueblos quedaron divididos entre colonias y otros fueron unidos con grupos rivales. Esto es una continuidad importante: muchas de esas fronteras se mantuvieron cuando los territorios se independizaron en el siglo XX, y aún influyen en conflictos.",
        "La economía colonial también cambió el territorio. Las colonias se especializaron en producir lo que necesitaba la potencia, como caucho, algodón o minerales, y compraban productos industriales de ella. Eso conectaba al mundo en un mercado mundial, pero de forma desigual: las potencias ganaban más. La relación entre potencia y colonia, entonces, fue de dependencia.",
    ],
    vocab=[("reconfiguración", "cambio en la forma o la organización de algo"), ("frontera colonial", "límite trazado por potencias para sus colonias"), ("especialización", "dedicarse a producir un solo tipo de bienes"), ("mercado mundial", "conjunto de intercambios entre países de todo el planeta"), ("dependencia", "situación de necesitar a otro para la economía")],
    worked=[
        ("Calcular el aumento", "¿Cuántos puntos porcentuales aumentó el control europeo en África entre 1870 y 1914?", ["1870: 10 %. 1914: 90 %.", "Resto: 90 − 10 = 80."], "80 puntos porcentuales"),
        ("Calcular el territorio restante", "En 1914, ¿qué porcentaje de África no estaba bajo control europeo?", ["Estaba bajo control el 90 %.", "100 − 90 = 10."], "10 %"),
    ],
    mistakes=[("Decir que las fronteras africanas siguieron a los pueblos.", "Muchas se trazaron sin considerar los pueblos.", "Pregunta quién trazó la frontera y para qué."),
              ("Olvidar que Etiopía y Liberia seguían independientes.", "No todo el continente fue colonizado.", "Menciona las excepciones.")],
    T=[
        ("{F} ¿Qué porcentaje de África controlaban las potencias europeas hacia 1870?", "Cerca del 10 %", "La ficha lo indica."),
        ("{F} ¿Qué dos países de África seguían independientes en 1914?", "Etiopía y Liberia", "La ficha los nombra."),
        ("{F} ¿Cómo se trazaron muchas fronteras coloniales?", "Con líneas rectas, sin considerar los pueblos", "La ficha lo dice."),
        ("=", "{F} En una región de ejemplo el control europeo pasó del 20 % al 85 %. ¿Cuántos puntos porcentuales aumentó?", "85-20", "Se resta el porcentaje de 1870 al de 1914.", " puntos"),
        ("=", "{F} En una región de ejemplo, el 85 % estaba bajo control europeo. ¿Qué porcentaje no lo estaba?", "100-85", "Se resta de 100 el porcentaje controlado.", " %"),
        ("{F} ¿Qué es un cambio? A) El control europeo en África pasó del 10 % al 90 % B) Muchas fronteras coloniales se mantuvieron en el siglo XX", "A) El control europeo en África pasó del 10 % al 90 %", "Es lo que se transformó; la B es una continuidad."),
        ("{F} ¿Qué es una continuidad? A) Las fronteras coloniales se mantuvieron al independizarse B) Cambió el control del territorio", "A) Las fronteras coloniales se mantuvieron al independizarse", "Es algo que se mantuvo."),
        ("{F} ¿Qué producía una colonia en la economía colonial? A) Lo que necesitaba la potencia, como caucho o minerales B) Todos sus propios productos industriales", "A) Lo que necesitaba la potencia, como caucho o minerales", "La ficha lo señala."),
        ("{F} Un pueblo queda dividido entre dos colonias por una línea recta. ¿Qué problema es probable? A) Comunidades separadas por la frontera B) Mejor comunicación", "A) Comunidades separadas por la frontera", "La frontera no considera a los pueblos."),
        ("{F} ¿Por qué se puede decir que la relación entre potencia y colonia fue de dependencia?", "Porque la colonia producía lo que la potencia necesitaba y compraba sus productos", "La economía quedó ligada a la potencia."),
        ("{F} Un compañero dice: «Las fronteras africanas actuales las decidieron los pueblos africanos». Refútalo.", "Muchas fronteras fueron trazadas por potencias, con líneas rectas, y se mantuvieron", "La ficha señala continuidad de fronteras coloniales."),
        ("{F} ¿Qué consecuencia tiene que Etiopía y Liberia sigan independientes? A) Muestra que no todo el territorio fue colonizado B) Muestra que todo fue colonizado", "A) Muestra que no todo el territorio fue colonizado", "Son excepciones al control europeo."),
        ("{F} ¿Qué conclusión es más ajustada? A) El mapa cambió muy rápido por el reparto de potencias, pero las fronteras trazadas persistieron B) El mapa no cambió", "A) El mapa cambió muy rápido por el reparto de potencias, pero las fronteras trazadas persistieron", "Reúne cambio y continuidad."),
    ],
    ctx=("Un diario escolar publica: «Las fronteras de África siguen a los pueblos desde siempre». ¿Qué dato de la ficha usas para corregirlo? A) Muchas fronteras se trazaron con líneas rectas sin considerar los pueblos B) Etiopía era independiente", "A) Muchas fronteras se trazaron con líneas rectas sin considerar los pueblos", "Contradice la afirmación."),
    sc=[("¿Qué es una frontera colonial?", "Un límite trazado por potencias para sus colonias", "Así se define."),
        ("En Historia: ¿Qué es la dependencia?", "Necesitar a otro para la economía", "Así se define."),
        ("=", "Si el 75 % de un territorio de ejemplo está bajo control de una potencia, ¿qué porcentaje no lo está?", "100-75", "Se resta de 100 el porcentaje controlado.", " %")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», y escribe tres datos en cada una con la ficha. Luego dibuja dos barras con escala 1 cm = 10 %: una para 1870 y otra para 1914, rotuladas con el porcentaje controlado por Europa. {F}",
        "Cambió: control europeo de 10 % a 90 %; reparto del mapa; economías de exportación. Continuó: fronteras coloniales; Etiopía y Liberia independientes; dependencia económica. Barras: 1 cm y 9 cm.",
        ["usa datos de la ficha", "separa cambio y continuidad", "barras con la escala"], ["tabla completa", "dos barras"], ["mezclar cambio y continuidad", "no usar la escala"],
        "Pide que diga qué problemas pueden traer las fronteras rectas."),
    reinforce="Explica en voz alta un cambio y una continuidad del mapa colonial.",
    extend="Mira un mapa de África y observa si hay fronteras en línea recta; anota dos países.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Administrador colonial, 1895: «Traemos orden, caminos y escuelas. Pagar impuestos es parte de pertenecer a un imperio civilizado.» "
     "Empresario, 1895: «Las colonias nos dan materias primas baratas y compradores para nuestros productos.» "
     "Líder local, 1895: «Nuestras tierras eran nuestras desde nuestros antepasados. No aceptamos que otros decidan por nosotros.» "
     "Economista crítico europeo, 1902: «El imperialismo beneficia a unos pocos inversionistas, mientras la mayoría paga el costo de las guerras y los pueblos colonizados pierden sus derechos.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores, causas y perspectivas del imperialismo: quién defendía, quién ganaba, quién resistía y quién criticaba.",
    prior=["Sé qué es el imperialismo.", "Sé contextualizar fuentes.", "Sé que cada actor tiene intereses."],
    explain=[
        "El imperialismo se justificó de varias maneras. Algunos administradores hablaban de llevar orden, caminos y escuelas, y creían que era una misión civilizadora, idea que hoy se rechaza porque desconoce la cultura de los pueblos. Los empresarios hablaban de materias primas y mercados. En ambos casos, los intereses europeos eran el centro.",
        "Los pueblos colonizados tuvieron otra perspectiva. Los líderes locales defendían que las tierras eran de sus antepasados y que no aceptaban decisiones impuestas. Hubo resistencia armada y no armada. En Europa también hubo críticos: un economista como J. A. Hobson escribió en 1902 que el imperialismo beneficiaba a pocos inversionistas y que otros pagaban los costos.",
        "Para contrastar, se compara qué quiere cada actor, qué le conviene y qué teme. El administrador teme perder el control; el empresario teme perder ganancias; el líder local teme perder tierras y autonomía; el crítico teme las guerras. Una explicación buena no repite la justificación de las potencias: la analiza y la contrasta con las otras voces.",
    ],
    vocab=[("misión civilizadora", "idea de que unos pueblos debían llevar su cultura a otros; hoy se rechaza"), ("administrador colonial", "autoridad que gobierna una colonia en nombre de la potencia"), ("autonomía", "capacidad de decidir por sí mismo"), ("inversionista", "persona que pone dinero en un negocio para obtener ganancias"), ("crítico", "quien examina y cuestiona una idea o práctica")],
    worked=[
        ("Quién se beneficia", "Según el empresario, ¿quién se beneficia de las colonias?", ["Dice que le dan materias primas baratas.", "También compradores para sus productos."], "El empresario europeo"),
        ("Quién resiste", "¿Qué actor defiende sus tierras y su autonomía?", ["Busco una voz que reclame decidir por sí misma.", "El líder local lo dice."], "El líder local"),
    ],
    mistakes=[("Repetir la justificación de las potencias como si fuera un hecho.", "El administrador expresa su propósito, no la realidad completa.", "Pregunta qué diría el pueblo colonizado."),
              ("Olvidar que hubo críticos en las propias potencias.", "Había voces europeas que cuestionaban el imperialismo.", "Incluye al economista crítico.")],
    T=[
        ("{F} ¿Qué trae según el administrador colonial?", "Orden, caminos y escuelas", "Su voz lo dice."),
        ("{F} ¿Qué buscan los empresarios en las colonias?", "Materias primas baratas y compradores", "Su voz lo dice."),
        ("{F} ¿Qué defiende el líder local?", "Sus tierras y su derecho a decidir", "Su voz lo dice."),
        ("{F} ¿Qué critica el economista en 1902?", "Que el imperialismo beneficia a pocos inversionistas y otros pagan los costos", "Su voz lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre las voces de 1895 y la del economista crítico?", "1902-1895", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué actor tiene un interés económico directo? A) El empresario B) El líder local", "A) El empresario", "Busca materias primas y compradores."),
        ("{F} ¿Qué actor defiende la autonomía de su pueblo? A) El líder local B) El administrador", "A) El líder local", "Reclama decidir sobre sus tierras."),
        ("{F} ¿Qué actor cuestiona el imperialismo desde Europa? A) El economista crítico B) El administrador colonial", "A) El economista crítico", "Critica que beneficie a pocos."),
        ("{F} ¿Qué justificación usa el administrador? A) Una misión civilizadora que hoy se rechaza B) La libertad de los pueblos", "A) Una misión civilizadora que hoy se rechaza", "Habla de orden y escuelas, sin considerar la cultura local."),
        ("{F} ¿Por qué el administrador y el líder local ven distinto el pago de impuestos?", "Porque uno lo ve como parte del imperio y el otro como una imposición sobre sus tierras", "Sus intereses chocan."),
        ("{F} Un compañero dice: «Todos en Europa apoyaban el imperialismo». Refútalo con la ficha.", "El economista crítico cuestionó el imperialismo en 1902", "Hubo voces críticas."),
        ("{F} ¿Qué voz falta para completar la perspectiva de los pueblos colonizados? A) La de una trabajadora de una plantación B) La de otro empresario", "A) La de una trabajadora de una plantación", "Aporta la vivencia diaria."),
        ("{F} ¿Qué conclusión es más equilibrada? A) El imperialismo fue defendido por potencias y empresarios, pero resistido y criticado por pueblos colonizados y algunos europeos B) El imperialismo fue aceptado por todos", "A) El imperialismo fue defendido por potencias y empresarios, pero resistido y criticado por pueblos colonizados y algunos europeos", "Reúne las cuatro voces."),
    ],
    ctx=("En un debate escolar, un grupo defiende «llevar civilización a las colonias». ¿Qué argumento usaría el otro grupo con la ficha? A) El líder local defendía sus tierras y su autonomía B) El empresario quería materias primas", "A) El líder local defendía sus tierras y su autonomía", "Muestra la perspectiva de los colonizados."),
    sc=[("¿Qué es la autonomía?", "La capacidad de decidir por sí mismo", "Así se define."),
        ("¿Qué actor critica que el imperialismo beneficie a pocos?", "El economista crítico", "Su voz lo dice."),
        ("¿Qué es un inversionista?", "Una persona que pone dinero en un negocio para ganar", "Así se define.")],
    op=("Elige dos actores de la ficha y haz una tabla con: qué quiere, qué le conviene y qué teme. Después escribe tres líneas sobre por qué sus perspectivas del imperialismo chocan. {F}",
        "Empresario: quiere ganancias; le conviene materias primas baratas; teme perder mercados. Líder local: quiere autonomía; le conviene conservar tierras; teme perderlas. Texto: «El empresario quiere recursos y el líder local defiende sus tierras, por eso sus intereses chocan».",
        ["elige dos actores", "tres columnas completas", "explica el choque"], ["tabla completa", "tres líneas"], ["mezclar voces", "opinar sin base"],
        "Pide que diga qué voz habría que escuchar primero para entender una colonia."),
    reinforce="Elige un actor y explica en voz alta qué pensaba del imperialismo.",
    extend="Piensa en una decisión de tu comunidad donde unos ganan y otros pierden, y nombra a dos actores.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento). "
     "Pregunta: ¿qué impacto tuvo el imperialismo europeo del siglo XIX? "
     "Dato 1: entre 1870 y 1914 el control europeo de África pasó de cerca del 10 % a cerca del 90 %. "
     "Dato 2: las colonias producían materias primas y compraban productos industriales, lo que amplió los mercados del capitalismo. "
     "Dato 3: en muchas colonias, los pueblos colonizados perdieron tierras, pagaron impuestos y trabajaron en plantaciones. "
     "Dato 4: hubo resistencia, como la victoria de Etiopía sobre Italia en Adwa, 1896. "
     "Dato 5: muchas fronteras coloniales se trazaron sin considerar los pueblos y se mantuvieron en el siglo XX.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre el impacto del imperialismo con afirmación, evidencia, razonamiento y una conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé contrastar actores.", "Sé que una conclusión debe ser proporcional."],
    explain=[
        "Un argumento sobre el imperialismo puede afirmar: «el imperialismo reconfiguró el mapa mundial, amplió los mercados del capitalismo y tuvo un impacto negativo en los pueblos colonizados, aunque estos resistieron». La evidencia son los datos: el 10 % al 90 % del control en África, las colonias como productoras y compradoras, la pérdida de tierras, la resistencia de Adwa y las fronteras trazadas por potencias.",
        "El razonamiento explica cómo cada dato apoya la afirmación. El dato 1 apoya la reconfiguración del mapa. El dato 2 apoya la expansión del capitalismo. El dato 3 apoya el impacto en los pueblos. El dato 4 muestra que los pueblos no fueron pasivos. El dato 5 muestra un efecto de larga duración.",
        "Para que sea proporcional, hay que decir que los datos son ejemplos y no cubren todas las colonias. Un contraargumento posible es que se construyeron caminos y escuelas, como decían los administradores; se responde mostrando que esos beneficios sirvieron sobre todo a los intereses de la potencia. Responderlo hace más fuerte el texto.",
    ],
    vocab=[("reconfigurar", "cambiar la organización de algo, como el mapa"), ("impacto", "efecto fuerte que deja un proceso"), ("pasivo", "que no actúa ni se opone"), ("efecto de larga duración", "consecuencia que dura mucho tiempo"), ("contraargumento", "dato o idea que podría contradecir la afirmación")],
    worked=[
        ("Elegir evidencia del mapa", "¿Qué dato apoya la reconfiguración del mapa?", ["Busco un dato sobre territorio.", "El dato 1 muestra el paso del 10 % al 90 %."], "Dato 1"),
        ("Elegir evidencia de resistencia", "¿Qué dato muestra que los pueblos no fueron pasivos?", ["Busco un dato de oposición.", "El dato 4 habla de la victoria de Etiopía."], "Dato 4"),
    ],
    mistakes=[("Escribir que el imperialismo solo trajo progreso.", "Los datos muestran pérdida de tierras y trabajo en plantaciones.", "Usa evidencia del impacto en los pueblos."),
              ("Olvidar el dato de resistencia.", "Se presenta a los pueblos como pasivos.", "Incluye el dato 4.")],
    T=[
        ("{F} ¿Qué dato muestra el impacto sobre los pueblos colonizados?", "El dato 3, pérdida de tierras, impuestos y trabajo en plantaciones", "Habla de efectos sobre ellos."),
        ("{F} ¿Qué dato muestra la relación con el capitalismo?", "El dato 2, colonias que producían materias primas y compraban productos industriales", "Amplió los mercados del capitalismo."),
        ("{F} ¿Qué dato muestra un efecto de larga duración?", "El dato 5, fronteras coloniales que se mantuvieron", "Perduraron en el siglo XX."),
        ("=", "{F} ¿Cuántos puntos porcentuales aumentó el control europeo de África entre 1870 y 1914?", "90-10", "Se resta el porcentaje de 1870 al de 1914.", " puntos"),
        ("=", "{F} Si 1914 es la fecha del dato 1 y 1896 la del dato 4, ¿cuántos años pasaron entre ambos?", "1914-1896", "Se resta el año de Adwa al de 1914.", " años"),
        ("{F} ¿Qué afirmación responde la pregunta? A) El imperialismo reconfiguró el mapa y amplió el capitalismo, con impacto negativo sobre los pueblos colonizados que resistieron B) El imperialismo no tuvo efectos", "A) El imperialismo reconfiguró el mapa y amplió el capitalismo, con impacto negativo sobre los pueblos colonizados que resistieron", "Se apoya en los cinco datos."),
        ("{F} ¿Qué dato sirve de contraargumento a «los pueblos fueron pasivos»? A) El dato 4 B) El dato 1", "A) El dato 4", "Muestra que hubo resistencia al dominio."),
        ("{F} Completa el razonamiento: «El dato 5 muestra que…» A) el imperialismo tuvo efectos que duraron más allá de la colonia B) las fronteras se borraron", "A) el imperialismo tuvo efectos que duraron más allá de la colonia", "Conecta el dato con una consecuencia."),
        ("{F} Un compañero escribe: «El imperialismo solo trajo caminos y escuelas». ¿Qué dato lo contradice?", "El dato 3, pérdida de tierras, impuestos y trabajo en plantaciones", "Muestra costos para los pueblos."),
        ("{F} ¿Por qué los datos no bastan para hablar de todas las colonias?", "Porque son ejemplos y no cubren todos los casos", "Cada colonia tuvo características propias."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «impacto negativo en los casos citados» B) «impacto igual en todo el mundo»", "A) «impacto negativo en los casos citados»", "Se limita a la evidencia."),
        ("{F} Ordena las partes de un argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y se explica."),
        ("{F} ¿Qué conclusión se ajusta mejor a los datos? A) El imperialismo cambió el mapa, amplió el capitalismo y dañó a pueblos colonizados, que resistieron B) El imperialismo fue aceptado por todos", "A) El imperialismo cambió el mapa, amplió el capitalismo y dañó a pueblos colonizados, que resistieron", "Reúne los cinco datos."),
    ],
    ctx=("Un diario escolar publica: «Los pueblos colonizados no se opusieron al imperialismo». ¿Qué evidencia de la ficha usas para responder? A) El dato 4, la victoria de Etiopía en Adwa B) El dato 1 solo", "A) El dato 4, la victoria de Etiopía en Adwa", "Muestra que hubo resistencia al dominio."),
    sc=[("Escribe, en orden, las tres partes de un argumento sobre el imperialismo.", "Afirmación, evidencia y razonamiento", "Son las partes enseñadas en la clase."),
        ("En un texto sobre el imperialismo, ¿qué sería un contraargumento a «los pueblos fueron pasivos»?", "Un dato de resistencia, como la victoria de Etiopía en Adwa", "Contradice la idea de pasividad."),
        ("=", "Si el control pasa del 15 % al 95 %, ¿cuántos puntos porcentuales aumentó?", "95-15", "Se resta el porcentaje inicial al final.", " puntos")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Qué impacto tuvo el imperialismo europeo del siglo XIX?». Usa al menos tres datos de la ficha, incluye el dato 4 como resistencia y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«El imperialismo reconfiguró el mapa mundial y amplió el capitalismo, pero dañó a los pueblos colonizados. En África el control europeo pasó del 10 % al 90 %. Las colonias producían materias primas y compraban productos industriales, y sus habitantes perdieron tierras. Sin embargo, hubo resistencia, como Adwa en 1896».",
        ["responde la pregunta", "usa tres datos y la resistencia", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["no incluir a los pueblos", "no explicar el vínculo"],
        "Pide que diga qué dato nuevo le gustaría tener sobre las colonias."),
    reinforce="Explica en voz alta dos impactos del imperialismo y una forma de resistencia.",
    extend="Escribe un contraargumento a tu párrafo y respóndelo con un dato.",
)
