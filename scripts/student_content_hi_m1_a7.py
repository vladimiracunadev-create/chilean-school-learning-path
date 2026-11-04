"""Material del estudiante de 1.º medio, Historia, Geografía y Ciencias Sociales: OA 07 (Primera Guerra Mundial, sociedad civil y nuevo orden mundial)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 07"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (siglo XX: años 1901 a 2000). "
     "Primera Guerra Mundial: 1914–1918. Detonante: el asesinato del archiduque Francisco Fernando, heredero del trono austrohúngaro, en Sarajevo, el 28 de junio de 1914. "
     "Bandos: Triple Entente (Francia, Gran Bretaña, Rusia y después otros países, entre ellos Estados Unidos desde 1917) y Potencias Centrales (Alemania, Austria-Hungría, el Imperio otomano y Bulgaria). "
     "Hitos: Revolución rusa, 1917; armisticio (cese de combates), 11 de noviembre de 1918; Tratado de Versalles, 1919; Sociedad de Naciones, 1920. "
     "Movilización general: llamado a las armas de toda la población en edad de combatir y puesta de la economía al servicio de la guerra.")
build(
    OA, 1, F,
    use="Aprenderé a situar la Primera Guerra Mundial en el tiempo y en el espacio, y a plantear la pregunta que guía este tema: ¿cómo afectó la guerra a la sociedad civil y al orden mundial?",
    prior=["Sé qué es el imperialismo y el nacionalismo.", "Sé calcular diferencias entre años.", "Sé que una alianza une a países con un objetivo común."],
    explain=[
        "La Primera Guerra Mundial duró de 1914 a 1918 y enfrentó a dos bloques. La Triple Entente reunió a Francia, Gran Bretaña y Rusia, y se sumaron otros países, entre ellos Estados Unidos en 1917. Las Potencias Centrales fueron Alemania, Austria-Hungría, el Imperio otomano y Bulgaria. La chispa fue el asesinato del archiduque Francisco Fernando en Sarajevo, el 28 de junio de 1914, pero las causas de fondo eran más amplias.",
        "Esas causas incluyen la rivalidad imperial por colonias y mercados, el nacionalismo, la carrera armamentista y el sistema de alianzas, que hizo que un conflicto local se extendiera. El asesinato fue el detonante, no la única causa. Por eso es mejor hablar de causas múltiples que de un solo hecho.",
        "La guerra fue mundial por los países involucrados y porque incluyó a las colonias. También fue una guerra total: movilización general de la población para combatir y de la economía para producir armas y alimentos. Terminó con un armisticio el 11 de noviembre de 1918 y con tratados como el de Versalles en 1919. Hay que evitar el error de reducir la guerra a un solo evento o una sola causa.",
    ],
    vocab=[("armisticio", "acuerdo para detener los combates"), ("Triple Entente", "alianza de Francia, Gran Bretaña y Rusia, a la que se sumaron otros países"), ("Potencias Centrales", "alianza de Alemania, Austria-Hungría, Imperio otomano y Bulgaria"), ("movilización general", "llamado a las armas de la población y puesta de la economía al servicio de la guerra"), ("detonante", "hecho que desencadena un conflicto que ya tenía causas profundas")],
    worked=[
        ("Calcular la duración", "Según la ficha, la guerra fue de 1914 a 1918. ¿Cuántos años de diferencia hay entre esos años?", ["Tomo los años de la ficha.", "Resto: 1918 − 1914 = 4."], "4 años"),
        ("Distinguir detonante y causa", "El asesinato de Sarajevo, ¿fue la única causa de la guerra?", ["La ficha lo llama detonante.", "Las causas de fondo eran más amplias."], "No: fue el detonante; hubo causas de fondo"),
    ],
    mistakes=[("Decir que la guerra se produjo solo por el asesinato de Sarajevo.", "El asesinato fue el detonante; las causas de fondo eran rivalidades y alianzas.", "Escribe «el detonante» y nombra al menos una causa de fondo."),
              ("Confundir los bandos.", "Alemania estaba en las Potencias Centrales, no en la Entente.", "Repasa la lista de cada bloque.")],
    T=[
        ("{F} ¿En qué ciudad fue asesinado el archiduque Francisco Fernando?", "En Sarajevo", "La ficha lo indica."),
        ("{F} ¿Qué países formaban las Potencias Centrales?", "Alemania, Austria-Hungría, el Imperio otomano y Bulgaria", "La ficha los lista."),
        ("{F} ¿Qué fue el armisticio?", "Un acuerdo para detener los combates", "La ficha lo define."),
        ("=", "{F} ¿Cuántos años pasaron entre el inicio de la guerra y el Tratado de Versalles?", "1919-1914", "Se resta el año de inicio al del Tratado.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Revolución rusa y la Sociedad de Naciones?", "1920-1917", "Se resta el año de la Revolución al de la Sociedad.", " años"),
        ("{F} ¿Qué hito es posterior? A) Armisticio de 1918 B) Revolución rusa de 1917", "A) Armisticio de 1918", "1918 es posterior a 1917."),
        ("{F} ¿Qué bloque incluía a Francia? A) Triple Entente B) Potencias Centrales", "A) Triple Entente", "La ficha lo indica."),
        ("{F} Un país se une a la Entente en 1917. ¿Cuál puede ser? A) Estados Unidos B) Bulgaria", "A) Estados Unidos", "Bulgaria pertenecía a las Potencias Centrales."),
        ("{F} ¿Cuál es un ejemplo de movilización general? A) Llamar a las armas a toda la población en edad de combatir y poner la economía al servicio de la guerra B) Firmar un tratado", "A) Llamar a las armas a toda la población en edad de combatir y poner la economía al servicio de la guerra", "La ficha la define así."),
        ("{F} ¿Por qué el asesinato de Sarajevo no explica por sí solo la guerra?", "Porque fue el detonante de causas más profundas como las alianzas y la rivalidad entre potencias", "Las causas eran múltiples."),
        ("{F} Un compañero dice: «La guerra fue solo entre Francia y Alemania». Corrígelo con la ficha.", "Participaron dos bloques de varios países, incluyendo Rusia, Austria-Hungría y el Imperio otomano", "La ficha lista más países."),
        ("{F} ¿Cuál es la mejor pregunta histórica? A) ¿Cómo la guerra afectó a la sociedad civil y cambió el orden mundial? B) ¿Qué soldado era el más valiente?", "A) ¿Cómo la guerra afectó a la sociedad civil y cambió el orden mundial?", "La A se responde con hechos."),
        ("{F} Una línea de tiempo usa 1 cm = 2 años y va de 1914 a 1920. ¿Cuántos centímetros mide?", "3 cm", "Se divide el tramo de 6 años por 2."),
    ],
    ctx=("Un afiche escolar dice: «La Primera Guerra Mundial empezó porque un joven disparó en Sarajevo». ¿Cómo lo corriges? A) Fue el detonante de una guerra con causas de fondo como alianzas y rivalidades B) Fue la única causa", "A) Fue el detonante de una guerra con causas de fondo como alianzas y rivalidades", "La ficha distingue detonante y causas."),
    sc=[("¿Qué es el armisticio?", "Un acuerdo para detener los combates", "Así se define."),
        ("¿Qué es la movilización general?", "El llamado a las armas de la población y el uso de la economía para la guerra", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1914 y 1922?", "1922-1914", "Se resta el año menor al mayor.", " años")],
    op=("Dibuja una línea de tiempo de 1914 a 1920 con escala 1 cm = 2 años y marca: inicio de la guerra (1914), Revolución rusa (1917), armisticio (1918), Tratado de Versalles (1919) y Sociedad de Naciones (1920). Debajo escribe dos frases: una que nombre los dos bloques y otra que explique la diferencia entre detonante y causa. {F}",
        "Posiciones desde 1914: 0; 1,5; 2; 2,5; 3 cm. Frases: «Los bloques fueron la Triple Entente y las Potencias Centrales»; «El asesinato fue el detonante, pero las causas eran las alianzas y las rivalidades».",
        ["respeta la escala", "los cinco hitos bien ubicados", "las frases son correctas"], ["línea de tiempo", "dos frases"], ["no medir con la escala", "confundir detonante con causa"],
        "Pide que explique por qué una guerra puede crecer con un sistema de alianzas."),
    reinforce="Explica en voz alta los dos bloques de la guerra y el detonante.",
    extend="Busca un monumento o una placa en tu ciudad que recuerde alguna guerra y anota qué dice.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, afiche de reclutamiento, 1914: «Tu patria te necesita. Enrólate hoy. La guerra será breve y gloriosa.» "
     "Fuente B, carta de un soldado a su madre, 1916: «Llevamos semanas en la trinchera. Llueve y hay barro. Los cañones no dejan dormir. Muchos compañeros no volverán. Ya nadie dice que la guerra es gloriosa.» "
     "Fuente C, nota de una mujer obrera de una fábrica de municiones, 1917: «Antes cuidaba la casa. Ahora trabajo en la fábrica porque los hombres están en el frente. Me pagan menos que a ellos.»")
build(
    OA, 2, F,
    use="Aprenderé a contextualizar y comparar fuentes sobre la guerra: un afiche, una carta de un soldado y una nota de una obrera.",
    prior=["Sé qué fue la Primera Guerra Mundial.", "Sé contextualizar una fuente.", "Sé separar descripción de interpretación."],
    explain=[
        "Un afiche de reclutamiento es propaganda: busca convencer a los jóvenes de unirse al ejército. Por eso muestra la guerra como breve y gloriosa. La carta del soldado, en cambio, es un testimonio íntimo escrito en 1916 desde la trinchera, y cuenta una experiencia dura. Al compararlos se ve un cambio en la percepción de la guerra entre 1914 y 1916.",
        "La nota de la obrera muestra otro efecto: la entrada de mujeres al trabajo en fábricas mientras los hombres combatían. Dice que antes cuidaba la casa y que ahora recibe un salario, aunque menor que el de los hombres. Es una fuente útil para entender la guerra desde la sociedad civil, es decir, desde quienes no estaban en el frente.",
        "Cada fuente tiene límites: el afiche expresa la voz del Estado, la carta es de un solo soldado y la nota es de una sola obrera. Para concluir con prudencia hay que comparar y decir qué muestran y qué no pueden probar. Por ejemplo, ninguna de las tres nos dice qué pensaban los pueblos de las colonias, que también fueron movilizados.",
    ],
    vocab=[("propaganda", "mensaje diseñado para influir en lo que piensa la población"), ("reclutamiento", "llamado a incorporar personas al ejército"), ("trinchera", "zanja donde se protegen los soldados en el frente"), ("sociedad civil", "población que no forma parte del ejército"), ("municiones", "proyectiles y cargas para las armas")],
    worked=[
        ("Contextualizar", "¿Quién escribe la Fuente B, cuándo y para qué?", ["Autor: un soldado.", "Fecha: 1916. Propósito: contar su vida en la trinchera a su madre."], "Un soldado, en 1916, para contarle a su madre"),
        ("Descripción o interpretación", "(1) «El soldado dice que llueve y hay barro». (2) «Todos los soldados querían desertar». ¿Cuál es descripción?", ["La (1) repite el texto.", "La (2) generaliza algo que el texto no dice."], "La (1) describe; la (2) interpreta de más"),
    ],
    mistakes=[("Tomar el afiche como descripción de la guerra real.", "Es propaganda del Estado.", "Compara con el testimonio del soldado."),
              ("Concluir con una carta que todos los soldados pensaban igual.", "Es la voz de uno solo.", "Escribe «este soldado cuenta».")],
    T=[
        ("{F} ¿Qué dice el afiche sobre la guerra?", "Que será breve y gloriosa", "El afiche lo afirma."),
        ("{F} ¿Dónde escribe el soldado de la Fuente B?", "Desde la trinchera", "Lo indica la carta."),
        ("{F} ¿Por qué trabaja la mujer en la fábrica?", "Porque los hombres están en el frente", "Lo dice la nota."),
        ("=", "{F} ¿Cuántos años pasaron entre el afiche y la carta del soldado?", "1916-1914", "Se resta el año del afiche al de la carta.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre el afiche y la nota de la obrera?", "1917-1914", "Se resta el año del afiche al de la nota.", " años"),
        ("{F} ¿Qué fuente es propaganda del Estado? A) La Fuente A B) La Fuente B", "A) La Fuente A", "Busca convencer a los jóvenes."),
        ("{F} ¿Qué fuente muestra una experiencia íntima del frente? A) La Fuente B B) La Fuente A", "A) La Fuente B", "Es una carta a la madre."),
        ("{F} ¿Qué cambio de percepción aparece entre A y B? A) De guerra breve y gloriosa a guerra dura y sin gloria B) De guerra dura a guerra breve", "A) De guerra breve y gloriosa a guerra dura y sin gloria", "Lo dicen las dos fuentes."),
        ("{F} ¿Qué desigualdad señala la Fuente C? A) Las mujeres cobraban menos que los hombres B) Las mujeres cobraban más", "A) Las mujeres cobraban menos que los hombres", "La nota lo dice."),
        ("{F} ¿Por qué el afiche no basta para conocer la guerra?", "Porque busca convencer y no muestra lo que vivían los soldados", "Es propaganda del Estado."),
        ("{F} Un compañero concluye: «Todas las mujeres trabajaban en fábricas durante la guerra». ¿Qué corrección haces?", "La nota es de una sola obrera", "No permite generalizar."),
        ("{F} ¿Qué voz falta en las tres fuentes? A) La de los pueblos de las colonias que también fueron movilizados B) La de otro soldado", "A) La de los pueblos de las colonias que también fueron movilizados", "Ninguna fuente la incluye."),
        ("{F} ¿Qué conclusión es más proporcional? A) Las fuentes muestran propaganda, desencanto de un soldado y trabajo femenino con desigualdad B) Las fuentes prueban lo que pensaba toda Europa", "A) Las fuentes muestran propaganda, desencanto de un soldado y trabajo femenino con desigualdad", "No dice más de lo que muestran."),
    ],
    ctx=("Un grupo prepara una exposición sobre la guerra y solo usa afiches de reclutamiento. ¿Qué recomiendas? A) Sumar cartas de soldados y notas de trabajadoras B) Usar más afiches", "A) Sumar cartas de soldados y notas de trabajadoras", "Aportan la experiencia de la guerra."),
    sc=[("¿Qué es propaganda?", "Un mensaje diseñado para influir en lo que piensa la población", "Así se define."),
        ("¿Qué es la sociedad civil?", "La población que no forma parte del ejército", "Así se define."),
        ("¿Quién escribe la Fuente C?", "Una mujer obrera de una fábrica de municiones", "La ficha lo indica.")],
    op=("Elige una fuente de la ficha. Haz una tabla de tres filas con: autor y fecha; qué dice (una frase); qué interpretas (con «Esto sugiere que…»). Cierra con qué no puedes concluir y qué voz falta. {F}",
        "Fuente C. Autor y fecha: una obrera de una fábrica de municiones, 1917. Dice: trabaja en la fábrica porque los hombres están en el frente y cobra menos. Interpretación: esto sugiere que la guerra abrió trabajos a las mujeres, pero con desigualdad. No puedo concluir que fue igual en todos los países; falta la voz de las colonias.",
        ["contextualiza", "separa descripción e interpretación", "señala límite y voz ausente"], ["tabla de tres filas", "frase de cierre"], ["usar un juicio como descripción", "generalizar"],
        "Pide que cuente qué le preguntaría a la obrera."),
    reinforce="Explica por qué un afiche de reclutamiento y una carta de un soldado informan cosas distintas.",
    extend="Mira un afiche actual (de campaña o publicidad) y di qué quiere que pienses.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cuadro de cambio y continuidad; territorios). "
     "Imperios que desaparecen al terminar la guerra: Imperio alemán, Imperio austrohúngaro, Imperio ruso e Imperio otomano. "
     "Estados nuevos o restaurados en Europa hacia el final de la guerra y después de ella: Polonia, Checoslovaquia, Yugoslavia (entonces llamada Reino de los serbios, croatas y eslovenos), Finlandia, Estonia, Letonia y Lituania. "
     "URSS: la Revolución rusa de 1917 lleva a la creación de la Unión de Repúblicas Socialistas Soviéticas en 1922. "
     "Estados Unidos: entra en la guerra en 1917; después de la guerra es una potencia económica con créditos a países europeos. "
     "Continuidades: las colonias de Gran Bretaña y Francia se mantienen; parte de las colonias alemanas pasan a ser administradas por vencedores.")
build(
    OA, 3, F,
    use="Aprenderé a relacionar cambio, continuidad y territorio tras la guerra: cómo se rediseñó el mapa de Europa y qué siguió igual.",
    prior=["Sé qué fue la Primera Guerra Mundial.", "Sé qué es un imperio y un Estado-nación.", "Sé calcular diferencias de años."],
    explain=[
        "La guerra cambió el mapa de Europa. Desaparecieron cuatro imperios: el alemán, el austrohúngaro, el ruso y el otomano. En su lugar surgieron Estados nuevos o restaurados, como Polonia, Checoslovaquia, Yugoslavia, Finlandia, Estonia, Letonia y Lituania. Muchos se basaron en el principio de Estado-nación que ya conoces, aunque dentro de sus fronteras quedaron minorías.",
        "También aparecieron nuevas potencias. La Revolución rusa de 1917 dio origen a la URSS en 1922, un Estado con un sistema político y económico distinto. Estados Unidos, que entró a la guerra en 1917, salió de ella como potencia económica con créditos a países europeos. Así, el centro del poder mundial empezó a moverse de Europa hacia otras regiones.",
        "Hubo continuidades: Gran Bretaña y Francia mantuvieron sus imperios coloniales, y parte de las colonias alemanas pasó a ser administrada por los vencedores. Además, los pueblos colonizados, que habían aportado soldados y recursos, no obtuvieron la independencia. Analizar el territorio permite ver tanto lo que se rompió como lo que se mantuvo.",
    ],
    vocab=[("restaurado", "Estado que vuelve a existir tras un periodo en que no existía"), ("URSS", "Unión de Repúblicas Socialistas Soviéticas, Estado formado en 1922 tras la Revolución rusa"), ("potencia económica", "país con gran capacidad de producir y prestar dinero"), ("crédito", "dinero prestado que debe devolverse con intereses"), ("minoría", "grupo menos numeroso dentro de una población")],
    worked=[
        ("Contar cambios", "¿Cuántos imperios desaparecieron según la ficha?", ["La ficha nombra el alemán, el austrohúngaro, el ruso y el otomano.", "Cuento: 4."], "4 imperios"),
        ("Medir un intervalo", "¿Cuántos años pasaron entre la Revolución rusa (1917) y la creación de la URSS (1922)?", ["Tomo los dos años de la ficha.", "Resto: 1922 − 1917 = 5."], "5 años"),
    ],
    mistakes=[("Decir que todas las colonias se independizaron tras la guerra.", "Las colonias de Gran Bretaña y Francia se mantuvieron.", "Distingue Europa de las colonias."),
              ("Creer que los nuevos Estados eran homogéneos.", "Quedaron minorías dentro de sus fronteras.", "Menciona que había minorías.")],
    T=[
        ("{F} Según la ficha, ¿cuál de estos imperios no desapareció al terminar la guerra? A) Imperio otomano B) Imperio británico", "B) Imperio británico", "La ficha no lo incluye entre los desaparecidos y dice que Gran Bretaña mantuvo sus colonias."),
        ("{F} ¿En qué año se crea la URSS?", "1922", "La ficha lo indica."),
        ("{F} ¿Qué potencia económica sale fortalecida con créditos a Europa?", "Estados Unidos", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la creación de la URSS y el año 1939?", "1939-1922", "Se resta el año de creación de la URSS a 1939.", " años"),
        ("{F} Cuenta los Estados nuevos o restaurados que nombra la ficha y escribe el número.", "7", "Son Polonia, Checoslovaquia, Yugoslavia, Finlandia, Estonia, Letonia y Lituania."),
        ("{F} ¿Qué es un cambio? A) Desaparecieron cuatro imperios B) Gran Bretaña y Francia mantuvieron sus colonias", "A) Desaparecieron cuatro imperios", "La B es una continuidad."),
        ("{F} ¿Qué es una continuidad? A) Gran Bretaña y Francia mantuvieron sus colonias B) Surgió la URSS", "A) Gran Bretaña y Francia mantuvieron sus colonias", "Es algo que se mantuvo."),
        ("{F} ¿Cuál de estos países no figura entre los Estados nuevos o restaurados de la ficha? A) Francia B) Polonia", "A) Francia", "Polonia está en la lista de la ficha; Francia ya existía antes de la guerra."),
        ("{F} ¿Qué región cambió su papel después de la guerra? A) Estados Unidos, que pasó a ser potencia económica B) Francia, que perdió todas sus colonias", "A) Estados Unidos, que pasó a ser potencia económica", "Prestó dinero a Europa."),
        ("{F} ¿Por qué se dice que el centro del poder mundial empezó a moverse?", "Porque Estados Unidos y la URSS ganaron importancia frente a las potencias europeas", "Surgieron nuevas potencias."),
        ("{F} Un compañero dice: «Con la guerra, todos los pueblos colonizados lograron la independencia». Refútalo.", "La ficha señala que Gran Bretaña y Francia mantuvieron sus colonias", "Hubo continuidad colonial."),
        ("{F} ¿Qué problema pudo quedar en los nuevos Estados? A) Minorías dentro de sus fronteras B) Ninguno", "A) Minorías dentro de sus fronteras", "Las fronteras no coincidían siempre con las identidades."),
        ("{F} ¿Qué conclusión es más ajustada? A) El mapa de Europa se rediseñó con nuevos Estados y nuevas potencias, aunque los imperios coloniales de los vencedores continuaron B) Todo el mapa mundial cambió", "A) El mapa de Europa se rediseñó con nuevos Estados y nuevas potencias, aunque los imperios coloniales de los vencedores continuaron", "Reúne cambio y continuidad."),
    ],
    ctx=("Un afiche escolar muestra un mapa de Europa de 1914 y otro de 1920. ¿Qué titular explica mejor la comparación? A) Cuatro imperios desaparecen y surgen nuevos Estados B) El mapa de Europa no cambió", "A) Cuatro imperios desaparecen y surgen nuevos Estados", "Resume el cambio de la ficha."),
    sc=[("¿Qué es la URSS?", "La Unión de Repúblicas Socialistas Soviéticas, formada en 1922", "Así se define."),
        ("¿Qué es un crédito?", "Dinero prestado que debe devolverse con intereses", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1917 y 1939?", "1939-1917", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Cambió» y «Continuó», con tres datos en cada una usando la ficha. Luego dibuja un esquema con cuatro cuadros (los cuatro imperios) y una flecha hacia un cuadro que diga «Estados nuevos». {F}",
        "Cambió: desaparecen cuatro imperios; surgen Estados nuevos; nace la URSS. Continuó: colonias de Gran Bretaña y Francia; colonias alemanas administradas por vencedores; minorías en los nuevos Estados. Esquema: alemán, austrohúngaro, ruso, otomano → Estados nuevos.",
        ["usa datos de la ficha", "separa cambio y continuidad", "esquema completo"], ["tabla completa", "esquema con flecha"], ["poner el mismo dato en ambas columnas", "olvidar un imperio"],
        "Pide que diga qué grupo crees que quedó con menos voz."),
    reinforce="Explica en voz alta un cambio y una continuidad del mapa después de la guerra.",
    extend="Busca en un mapa de Europa un país que haya surgido en 1918–1919 y anota su nombre actual.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (voces de ejemplo escritas para este cuaderno). "
     "Soldado en la trinchera, 1916: «Esperaba una guerra corta y gloriosa. Estoy en el barro y veo morir a mis compañeros.» "
     "Mujer obrera, 1917: «Trabajo en una fábrica por primera vez. Gano un sueldo y hago algo útil, pero me pagan menos que a los hombres.» "
     "Gobernante, 1915: «Necesitamos que todos colaboren: los hombres en el frente, las mujeres en las fábricas y los niños ahorrando.» "
     "Pacifista, 1916: «Esta guerra mata a millones por intereses de unos pocos gobiernos. Hay que negociar la paz.» "
     "Habitante de una colonia, 1917 (ejemplo): «Nos llevan a combatir en una guerra que no es nuestra y no nos prometen nada a cambio.»")
build(
    OA, 4, F,
    use="Aprenderé a contrastar actores y perspectivas de la guerra: soldados, mujeres, gobernantes, pacifistas y pueblos colonizados.",
    prior=["Sé qué fue la movilización general.", "Sé contextualizar fuentes.", "Sé que cada actor tiene intereses."],
    explain=[
        "La guerra fue vivida de manera muy distinta por diferentes actores. El soldado vio morir a sus compañeros y perdió la ilusión de una guerra gloriosa. La mujer obrera entró a trabajar a una fábrica por primera vez y ganó un sueldo, pero con desigualdad. El gobernante pidió la colaboración de todos para sostener la guerra. Un pacifista, persona que rechaza la guerra y busca la paz, pidió negociar.",
        "Los pueblos colonizados también participaron: gran número de soldados y trabajadores de las colonias fueron enviados a luchar o a trabajar para las potencias, sin que sus intereses fueran considerados. Esta perspectiva suele ser menos recordada. Con la movilización general, la sociedad civil quedó involucrada: la guerra no solo ocurrió en el frente sino también en las fábricas y en los hogares.",
        "Para contrastar, se compara qué quiere cada actor, qué le conviene y qué teme. El gobernante teme perder la guerra; el soldado, morir; la obrera, perder el sueldo cuando vuelvan los hombres; el pacifista, la continuación de las muertes; y el habitante colonial, no recibir nada a cambio. Una buena explicación considera todas las voces.",
    ],
    vocab=[("pacifista", "persona que rechaza la guerra y busca la paz"), ("frente", "lugar donde se combate"), ("sueldo", "pago regular por un trabajo"), ("colaborar", "participar con otros para un fin común"), ("desencanto", "pérdida de la ilusión que se tenía")],
    worked=[
        ("Quién pide colaboración", "¿Qué actor pide que todos colaboren con la guerra?", ["Busco una voz que llame a toda la población.", "El gobernante pide a hombres, mujeres y niños."], "El gobernante"),
        ("Quién se opone", "¿Qué actor rechaza la guerra?", ["Busco una voz que pida negociar.", "El pacifista pide paz."], "El pacifista"),
    ],
    mistakes=[("Explicar la guerra solo con la voz de los gobernantes.", "Se ignora lo que vivieron soldados, mujeres y colonias.", "Incluye al menos tres voces."),
              ("Pensar que la guerra solo ocurrió en el frente.", "La sociedad civil también fue movilizada.", "Menciona fábricas y hogares.")],
    T=[
        ("{F} ¿Qué esperaba el soldado antes de ir a la trinchera?", "Una guerra corta y gloriosa", "Su voz lo dice."),
        ("{F} ¿Qué gana la mujer obrera por trabajar en la fábrica?", "Un sueldo", "Su voz lo dice."),
        ("{F} ¿Qué pide el pacifista?", "Negociar la paz", "Su voz lo dice."),
        ("{F} ¿Qué reclama el habitante de la colonia?", "Que lo llevan a combatir en una guerra que no es suya y sin prometerle nada", "Su voz lo dice."),
        ("{F} ¿Qué actor teme morir en el frente? A) El soldado B) El gobernante", "A) El soldado", "Ve morir a sus compañeros."),
        ("{F} ¿Qué actor señala una desigualdad de género? A) La mujer obrera B) El soldado", "A) La mujer obrera", "Dice que le pagan menos que a los hombres."),
        ("{F} ¿Qué actor representa a la sociedad civil movilizada? A) La mujer obrera B) El soldado", "A) La mujer obrera", "Trabaja en la fábrica para sostener la guerra."),
        ("{F} ¿Qué actor quiere sostener la guerra? A) El gobernante B) El pacifista", "A) El gobernante", "Pide colaboración de todos."),
        ("{F} ¿Por qué el soldado y el gobernante ven distinto la guerra?", "Porque el soldado vive la muerte y el gobernante busca mantener la guerra", "Sus posiciones son distintas."),
        ("{F} Un compañero dice: «Todos estaban de acuerdo con la guerra». Refútalo con la ficha.", "El pacifista pidió negociar y el habitante de la colonia dice que no era su guerra", "Hubo voces contrarias."),
        ("{F} ¿Qué voz falta para completar la perspectiva de la sociedad civil? A) La de un niño que sufrió hambre por el racionamiento B) La de otro gobernante", "A) La de un niño que sufrió hambre por el racionamiento", "Es otra vivencia civil."),
        ("{F} ¿Qué conclusión es más equilibrada? A) La guerra involucró a soldados, trabajadoras, gobernantes y colonias, con visiones y costos distintos B) La guerra fue aceptada por todos igual", "A) La guerra involucró a soldados, trabajadoras, gobernantes y colonias, con visiones y costos distintos", "Reúne las cinco voces."),
        ("{F} ¿Qué pregunta ayuda a contrastar actores? A) ¿Qué quiere, qué le conviene y qué teme cada uno? B) ¿Qué actor tiene la razón y cuál se equivoca?", "A) ¿Qué quiere, qué le conviene y qué teme cada uno?", "Es el método de contraste."),
    ],
    ctx=("Para un debate escolar, un grupo defiende la guerra y otro la critica. ¿Qué voz de la ficha usaría el segundo grupo? A) La del pacifista B) La del gobernante", "A) La del pacifista", "Pide negociar la paz."),
    sc=[("¿Qué es un pacifista?", "Una persona que rechaza la guerra y busca la paz", "Así se define."),
        ("¿Qué es el desencanto?", "La pérdida de la ilusión que se tenía", "Así se define."),
        ("¿Qué actor teme perder el sueldo cuando vuelvan los hombres?", "La mujer obrera", "Es una consecuencia previsible de su situación.")],
    op=("Elige dos actores de la ficha y haz una tabla con: qué quiere, qué le conviene y qué teme. Después escribe tres líneas que expliquen por qué sus perspectivas sobre la guerra chocan. {F}",
        "Gobernante: quiere ganar; le conviene la colaboración de todos; teme perder. Soldado: quiere sobrevivir; le conviene que termine; teme morir. Texto: «El gobernante necesita que la guerra continúe y el soldado quiere que termine; por eso chocan».",
        ["elige dos actores", "tres columnas completas", "explica el choque"], ["tabla completa", "tres líneas"], ["mezclar voces", "opinar sin base"],
        "Pide que diga qué voz habría que escuchar más para entender la guerra."),
    reinforce="Elige un actor y explica en voz alta qué vivió en la guerra.",
    extend="Pregunta a una persona mayor de tu casa si recuerda alguna historia familiar sobre una guerra y anota una frase.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (datos para construir un argumento). "
     "Pregunta: ¿cómo cambió la Primera Guerra Mundial a la sociedad y al orden mundial? "
     "Dato 1: movilización general; la economía y la población civil quedaron al servicio de la guerra. "
     "Dato 2: entrada masiva de mujeres a fábricas y a trabajos públicos; después de la guerra, en varios países se les reconoció el voto, por ejemplo en Alemania y Gran Bretaña en 1918 (en Gran Bretaña, solo mujeres mayores de 30 años que cumplían ciertos requisitos) y en Estados Unidos en 1920. "
     "Dato 3: desaparecen cuatro imperios y surgen nuevos Estados. "
     "Dato 4: surge la URSS en 1922 y Estados Unidos se vuelve potencia económica. "
     "Dato 5: la guerra puso en duda la idea de progreso del siglo XIX, porque la ciencia y la técnica se usaron para matar.")
build(
    OA, 5, F,
    use="Aprenderé a construir un argumento sobre las consecuencias de la guerra con afirmación, evidencia, razonamiento y una conclusión proporcional.",
    prior=["Sé qué partes tiene un argumento.", "Sé contrastar actores.", "Sé qué es la idea de progreso."],
    explain=[
        "Un argumento sobre la guerra puede afirmar: «la Primera Guerra Mundial transformó la sociedad y rediseñó el orden mundial». La evidencia son los datos: la movilización general, la entrada de mujeres al trabajo y al espacio público, la desaparición de imperios, el surgimiento de la URSS y de Estados Unidos como potencia, y la crisis de la idea de progreso.",
        "El razonamiento explica cómo cada dato apoya la afirmación. El dato 1 muestra que la guerra afectó a toda la sociedad. El dato 2 muestra un cambio en el papel de las mujeres, que en varios países obtuvieron el voto, aunque con restricciones. Los datos 3 y 4 muestran un nuevo mapa y nuevas potencias. El dato 5 muestra un cambio en la mentalidad.",
        "Para que sea proporcional, hay que reconocer límites. No todas las mujeres obtuvieron el voto al mismo tiempo y en Gran Bretaña se les limitó a las mayores de 30 años. La guerra tuvo efectos distintos según el país. Un contraargumento posible es que los cambios en el trabajo femenino fueron temporales para muchas; se responde mostrando que el cambio en el voto fue duradero en varios países.",
    ],
    vocab=[("crisis de la idea de progreso", "pérdida de confianza en que la ciencia y la técnica llevan siempre a un futuro mejor"), ("sufragio femenino", "derecho de las mujeres a votar"), ("orden mundial", "forma en que se reparten el poder y las relaciones entre países"), ("restricción", "límite que impide ejercer plenamente un derecho"), ("contraargumento", "dato o idea que podría contradecir la afirmación")],
    worked=[
        ("Elegir evidencia sobre mujeres", "¿Qué dato muestra un cambio en el papel de las mujeres?", ["Busco un dato sobre trabajo o voto femenino.", "El dato 2."], "Dato 2"),
        ("Elegir evidencia de mentalidad", "¿Qué dato muestra una crisis de la idea de progreso?", ["Busco un dato sobre mentalidad.", "El dato 5."], "Dato 5"),
    ],
    mistakes=[("Escribir que todas las mujeres obtuvieron el voto en 1918.", "Fue distinto en cada país y con restricciones.", "Cita países y años exactos de la ficha."),
              ("Citar un dato sin explicar el vínculo.", "Falta el razonamiento.", "Agrega «Esto muestra que…».")],
    T=[
        ("{F} ¿Qué dato muestra un cambio en el mapa de Europa?", "El dato 3, la desaparición de imperios y el surgimiento de Estados nuevos", "Habla de territorio."),
        ("{F} ¿Qué dato muestra el surgimiento de nuevas potencias?", "El dato 4, la URSS y Estados Unidos", "Habla de poder mundial."),
        ("{F} ¿En qué año obtuvieron el voto las mujeres en Estados Unidos según la ficha?", "1920", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años después del voto en Gran Bretaña (1918) llegó el voto femenino en Estados Unidos?", "1920-1918", "Se resta el año británico al de Estados Unidos.", " años"),
        ("{F} ¿Qué afirmación responde la pregunta? A) La guerra transformó la sociedad y rediseñó el orden mundial B) La guerra no cambió nada", "A) La guerra transformó la sociedad y rediseñó el orden mundial", "Se apoya en los cinco datos."),
        ("{F} ¿Qué dato sirve de límite a la idea de que todas las mujeres obtuvieron el voto? A) El dato 2, que señala que en Gran Bretaña solo mayores de 30 años B) El dato 4", "A) El dato 2, que señala que en Gran Bretaña solo mayores de 30 años", "Muestra una restricción."),
        ("{F} Completa el razonamiento: «El dato 5 apoya el cambio de mentalidad porque…» A) la ciencia y la técnica se usaron para matar B) las mujeres entraron a las fábricas", "A) la ciencia y la técnica se usaron para matar", "Puso en duda el progreso."),
        ("{F} Un compañero escribe: «La guerra no afectó a la población civil». ¿Qué dato lo contradice?", "El dato 1, la movilización general de la economía y la población civil", "La sociedad quedó al servicio de la guerra."),
        ("{F} ¿Por qué el dato 2 es una evidencia parcial?", "Porque el voto femenino no llegó a todas las mujeres ni a todos los países en esas fechas", "La ficha muestra restricciones y fechas distintas."),
        ("{F} ¿Qué palabra hace más proporcional la conclusión? A) «en varios países» B) «en todo el mundo»", "A) «en varios países»", "Se limita a la evidencia."),
        ("{F} Ordena las partes de un argumento: razonamiento, afirmación, evidencia.", "Afirmación, evidencia, razonamiento", "Primero se responde, luego se prueba y se explica."),
        ("{F} ¿Qué dato falta para completar el argumento sobre los pueblos colonizados? A) Un dato sobre soldados y trabajadores de las colonias B) Otro dato del mapa de Europa", "A) Un dato sobre soldados y trabajadores de las colonias", "Aporta la perspectiva ausente."),
        ("{F} ¿Qué conclusión se ajusta mejor a los datos? A) La guerra cambió la sociedad, el mapa y la mentalidad, aunque con límites y diferencias entre países B) La guerra cambió todo igual en todos los países", "A) La guerra cambió la sociedad, el mapa y la mentalidad, aunque con límites y diferencias entre países", "Reúne los cinco datos."),
    ],
    ctx=("Un diario escolar publica: «Después de la guerra las mujeres lograron igualdad total». ¿Qué evidencia de la ficha usarías para matizar? A) El dato 2, que muestra restricciones B) El dato 4", "A) El dato 2, que muestra restricciones", "Muestra voto limitado y fechas distintas."),
    sc=[("¿Qué parte de un argumento sobre la guerra puede ser un dato como el voto femenino en 1920?", "La evidencia", "Los datos de las fuentes son la evidencia."),
        ("¿Qué es el sufragio femenino?", "El derecho de las mujeres a votar", "Así se define."),
        ("=", "¿Cuántos años pasaron entre 1918 y 1922?", "1922-1918", "Se resta el año menor al mayor.", " años")],
    op=("Escribe un párrafo de seis a ocho líneas que responda: «¿Cómo cambió la Primera Guerra Mundial a la sociedad y al orden mundial?». Usa al menos tres datos de la ficha, incluye una restricción del dato 2 y marca la afirmación, la evidencia y el razonamiento. {F}",
        "«La Primera Guerra Mundial transformó la sociedad y rediseñó el orden mundial. Hubo movilización general y las mujeres entraron a fábricas; en varios países obtuvieron el voto, aunque en Gran Bretaña solo las mayores de 30 años. Desaparecieron cuatro imperios, surgió la URSS y Estados Unidos se volvió potencia, y la idea de progreso entró en crisis».",
        ["responde la pregunta", "usa tres datos y una restricción", "conclusión proporcional"], ["párrafo escrito", "partes marcadas"], ["usar «todas» sin evidencia", "no explicar el vínculo"],
        "Pide que diga qué dato le gustaría conocer de un país que no aparece."),
    reinforce="Explica en voz alta dos consecuencias de la guerra y un límite.",
    extend="Escribe un contraargumento y respóndelo con un dato de la ficha.",
)

# ---------------------------------------------------------------- clase 6
F = ("Ficha 6 (proyecciones y límites del nuevo orden). "
     "Tratado de Versalles, 1919: impuso a Alemania pagar reparaciones (compensaciones económicas), reducir su ejército y perder territorios; muchos alemanes lo consideraron humillante. "
     "Sociedad de Naciones, 1920: organización creada para mantener la paz; Estados Unidos no se integró a ella. "
     "Trabajo de mujeres: al volver los hombres, muchas mujeres perdieron los trabajos que habían ocupado durante la guerra. "
     "Colonias: los pueblos colonizados que apoyaron la guerra no obtuvieron la independencia. "
     "Proyección: veinte años después, en 1939, comenzó la Segunda Guerra Mundial.")
build(
    OA, 6, F,
    use="Aprenderé a evaluar proyecciones y límites del nuevo orden mundial: qué problemas dejó la paz y por qué la guerra no fue «la última».",
    prior=["Sé las consecuencias principales de la guerra.", "Sé construir un argumento.", "Sé qué es una proyección histórica."],
    explain=[
        "El Tratado de Versalles de 1919 buscó construir la paz, pero dejó problemas. Obligó a Alemania a pagar reparaciones, reducir su ejército y perder territorios, y muchos alemanes lo vieron como una humillación. El resentimiento por este tratado alimentó posteriormente movimientos nacionalistas. No fue la única causa de lo que vino después, pero sí un factor.",
        "La Sociedad de Naciones, creada en 1920 para mantener la paz, tuvo límites: Estados Unidos no se integró, lo que debilitó su poder. Además, los cambios sociales fueron limitados. Al volver los hombres del frente, muchas mujeres perdieron los trabajos que habían ocupado, y los pueblos colonizados no obtuvieron la independencia.",
        "Evaluar significa pesar logros y costos con evidencia. El nuevo orden creó Estados y una organización internacional, pero dejó tensiones que contribuyeron a una nueva guerra en 1939. La historia no es una línea recta: cada solución puede crear nuevos problemas. Por eso hay que evitar frases como «el Tratado de Versalles causó la Segunda Guerra Mundial» sin matices.",
    ],
    vocab=[("reparaciones", "compensaciones económicas que paga un país derrotado"), ("Sociedad de Naciones", "organización internacional creada en 1920 para mantener la paz"), ("humillante", "que hiere el orgullo o la dignidad de alguien"), ("proyección", "efecto que un proceso tiene hacia el futuro"), ("resentimiento", "malestar duradero por una ofensa")],
    worked=[
        ("Calcular un intervalo", "¿Cuántos años pasaron entre el Tratado de Versalles (1919) y el inicio de la Segunda Guerra Mundial (1939)?", ["Tomo los dos años de la ficha.", "Resto: 1939 − 1919 = 20."], "20 años"),
        ("Pesar un logro y un límite", "La Sociedad de Naciones buscaba la paz. ¿Qué límite señala la ficha?", ["La ficha menciona a Estados Unidos.", "No se integró a la organización."], "Estados Unidos no se integró"),
    ],
    mistakes=[("Decir que el Tratado de Versalles fue la única causa de la Segunda Guerra Mundial.", "Hubo otras causas y decisiones posteriores.", "Usa «contribuyó a» en lugar de «causó»."),
              ("Olvidar a los pueblos colonizados.", "Su situación no cambió con la paz.", "Menciona la continuidad colonial.")],
    T=[
        ("{F} ¿Qué debía pagar Alemania según el Tratado de Versalles?", "Reparaciones", "La ficha lo indica."),
        ("{F} ¿En qué año se creó la Sociedad de Naciones?", "1920", "La ficha lo indica."),
        ("{F} ¿Qué país no se integró a la Sociedad de Naciones?", "Estados Unidos", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre el armisticio de 1918 y el inicio de la Segunda Guerra Mundial?", "1939-1918", "Se resta el año del armisticio al del inicio.", " años"),
        ("=", "{F} ¿Cuántos años pasaron entre la Sociedad de Naciones y el inicio de la Segunda Guerra Mundial?", "1939-1920", "Se resta el año de la Sociedad al del inicio.", " años"),
        ("{F} ¿Qué efecto tuvo el regreso de los hombres en el trabajo de las mujeres? A) Muchas perdieron los trabajos que ocupaban B) Todas conservaron sus trabajos", "A) Muchas perdieron los trabajos que ocupaban", "La ficha lo señala."),
        ("{F} ¿Cómo vieron muchos alemanes el Tratado? A) Como una humillación B) Como un acuerdo justo que aceptaron sin reclamos", "A) Como una humillación", "La ficha lo dice."),
        ("{F} ¿Qué límite tuvo el nuevo orden para las colonias? A) No obtuvieron la independencia B) Se independizaron todas", "A) No obtuvieron la independencia", "La ficha lo señala."),
        ("{F} ¿Qué relación puede plantearse entre Versalles y la Segunda Guerra? A) Contribuyó a tensiones que influyeron, junto a otros factores B) Fue la única causa", "A) Contribuyó a tensiones que influyeron, junto a otros factores", "La explicación pide matizar."),
        ("{F} ¿Por qué la ausencia de Estados Unidos debilitó a la Sociedad de Naciones?", "Porque era una potencia importante y no formó parte de la organización", "Sin esa potencia, tenía menos poder."),
        ("{F} Un compañero dice: «Después de 1919 el mundo quedó en paz para siempre». Refútalo con la ficha.", "Veinte años después comenzó la Segunda Guerra Mundial", "La paz fue frágil."),
        ("{F} ¿Qué logro puede reconocerse en el nuevo orden? A) Se creó una organización internacional para mantener la paz B) Se terminó la desigualdad", "A) Se creó una organización internacional para mantener la paz", "La Sociedad de Naciones fue un intento."),
        ("{F} ¿Qué conclusión pesa logros y límites? A) El nuevo orden creó Estados y una organización de paz, pero dejó tensiones y exclusiones B) El nuevo orden fue perfecto", "A) El nuevo orden creó Estados y una organización de paz, pero dejó tensiones y exclusiones", "Considera ambas caras."),
    ],
    ctx=("Un compañero propone: «Si el tratado hubiera sido más suave, nunca habría habido otra guerra». ¿Cómo respondes con prudencia? A) Es posible que hubiera disminuido tensiones, pero hubo otros factores que también influyeron B) Tiene toda la razón", "A) Es posible que hubiera disminuido tensiones, pero hubo otros factores que también influyeron", "La historia es multicausal."),
    sc=[("¿Qué son las reparaciones?", "Compensaciones económicas que paga un país derrotado", "Así se define."),
        ("¿Para qué se creó la Sociedad de Naciones?", "Para mantener la paz", "Esa fue su finalidad."),
        ("=", "¿Cuántos años pasaron entre 1919 y 1930?", "1930-1919", "Se resta el año menor al mayor.", " años")],
    op=("Haz una tabla con dos columnas, «Logros» y «Límites», con tres datos en cada una usando la ficha y la explicación. Luego escribe una frase que pese ambos y diga si, en tu opinión, el nuevo orden fue más sólido o más frágil, con una razón apoyada en la ficha. {F}",
        "Logros: nuevos Estados; Sociedad de Naciones; voto femenino en varios países. Límites: Estados Unidos fuera; resentimiento alemán; colonias sin independencia. Frase: «Fue frágil porque veinte años después comenzó otra guerra».",
        ["tres logros y tres límites", "usa evidencia", "frase que pesa ambos"], ["tabla completa", "una frase"], ["solo logros o solo límites", "opinar sin evidencia"],
        "Pide que diga qué cambiaría en el tratado y por qué."),
    reinforce="Explica en voz alta un logro y un límite del nuevo orden mundial.",
    extend="Busca el nombre de una organización internacional actual que busque la paz y anota una función.",
)
