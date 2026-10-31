"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 06 (período del salitre: expansión económica y cuestión social)."""
from __future__ import annotations

from hi5_lib import build

OA6 = "HI06 OA 06"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 25 (el salitre en el tiempo y el espacio, hecha para este cuaderno). "
     "El salitre es un mineral del desierto del norte, usado como fertilizante y para fabricar explosivos. Se extraía en la pampa de Tarapacá y de Antofagasta y se exportaba por puertos como Pisagua, Iquique y Antofagasta (en ese orden, de norte a sur). "
     "1879-1884: Guerra del Pacífico; Chile queda a cargo de Tarapacá y Antofagasta. "
     "Desde la década de 1880: auge del salitre; Chile cobra un impuesto a su exportación y el Estado recibe muchos ingresos. "
     "1907: huelga de trabajadores del salitre en Iquique, que termina con la muerte de muchas personas (matanza de la escuela Santa María). "
     "1912: Luis Emilio Recabarren funda el Partido Obrero Socialista en Iquique. "
     "1914-1918: durante la Primera Guerra Mundial, Alemania produce salitre sintético. "
     "Desde 1930: la crisis mundial y la competencia del salitre sintético hacen caer la actividad.")
build(
    OA6, 1, F,
    use="Aprenderé a ubicar el período del salitre en el tiempo y en el mapa. Sirve para entender dónde y cuándo ocurrieron la expansión económica y la cuestión social.",
    prior=["Sé que Chile incorporó Tarapacá y Antofagasta tras la Guerra del Pacífico.", "Sé leer una línea de tiempo y restar años.", "Sé ubicar el desierto del norte en un mapa."],
    explain=[
        "El salitre es un mineral que se encuentra en el desierto del norte de Chile. Se usaba como fertilizante para cultivar alimentos y para fabricar explosivos. Después de la Guerra del Pacífico, Chile quedó a cargo de las zonas salitreras de Tarapacá y Antofagasta, y desde la década de 1880 comenzó un gran auge: el período del salitre.",
        "En esa época hubo una expansión económica: crecieron las exportaciones, el Estado cobró impuestos al salitre y pudo construir caminos, ferrocarriles, escuelas y edificios. Pero el trabajo en la pampa era duro y mal pagado, y el crecimiento de las ciudades dejó a muchas familias en viviendas precarias. A estos problemas se les llama cuestión social.",
        "El período termina cuando el salitre natural ya no se vende tanto. Alemania produjo salitre sintético durante la Primera Guerra Mundial, y la crisis económica mundial de 1930 hizo caer aún más la actividad. Ubicar estos hechos en una línea de tiempo y en un mapa ayuda a ver el auge, los conflictos y la caída.",
    ],
    vocab=[("salitre", "mineral del desierto del norte usado como fertilizante y para explosivos"), ("pampa", "terreno llano y seco del norte de Chile donde se extraía el salitre"), ("exportar", "vender productos a otros países"), ("cuestión social", "conjunto de problemas de pobreza y de condiciones de vida y de trabajo de los obreros"), ("sintético", "fabricado por el ser humano, no sacado de la naturaleza")],
    worked=[
        ("Calcular un intervalo", "{F} ¿Cuántos años pasaron entre la huelga de 1907 y la fundación del Partido Obrero Socialista?", ["Busco los años: 1907 y 1912.", "Resto: 1912 − 1907 = 5."], "5 años"),
        ("Ubicar un lugar", "{F} ¿Dónde se extraía el salitre?", ["Reviso la ficha: dice que en la pampa del norte.", "Las zonas son Tarapacá y Antofagasta."], "En la pampa de Tarapacá y Antofagasta"),
    ],
    mistakes=[("Creer que el salitre se extraía en el sur de Chile.", "Se olvida que es un mineral del desierto.", "Se extraía en la pampa del norte."),
              ("Pensar que el auge del salitre duró hasta hoy.", "No se considera la crisis de 1930.", "El salitre cayó por el salitre sintético y la crisis mundial.")],
    T=[
        ("{F} ¿Para qué se usaba el salitre?", "como fertilizante y para fabricar explosivos", "La ficha lo dice."),
        ("{F} ¿Qué puerto de la ficha está más al norte?", "Pisagua", "La ficha los ordena de norte a sur."),
        ("{F} ¿Qué país produjo salitre sintético durante la Primera Guerra Mundial?", "Alemania", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos años duró la Primera Guerra Mundial según los años de la ficha?", "1918-1914", "Se resta el año de inicio al de término.", " años"),
        ("{F} ¿En qué ciudad fundó Recabarren el Partido Obrero Socialista?", "Iquique", "La ficha lo dice."),
        ("{F} Ordena de más antiguo a más reciente: salitre sintético, Partido Obrero Socialista, huelga de 1907, Guerra del Pacífico.", "Guerra del Pacífico, huelga de 1907, Partido Obrero Socialista, salitre sintético", "Los años son 1879, 1907, 1912 y 1914."),
        ("=", "{F} ¿Cuántos años pasaron entre el fin de la Guerra del Pacífico y la huelga de 1907?", "1907-1884", "Se resta el año menor al mayor.", " años"),
        ("{F} Clasifica como «expansión económica» o «cuestión social»: a) el Estado recibe muchos ingresos; b) la huelga de 1907; c) auge de exportaciones; d) Partido Obrero Socialista.", "expansión económica: a y c; cuestión social: b y d", "Los obreros reclamaban por sus condiciones."),
        ("{F} Un compañero dice: «El salitre se extraía en el sur de Chile». Corrígelo.", "No: se extraía en la pampa del norte, en Tarapacá y Antofagasta", "La ficha lo indica."),
        ("{F} Una alumna dice: «La Primera Guerra Mundial ayudó al auge del salitre natural». ¿Qué dato de la ficha lo contradice?", "que Alemania produjo salitre sintético en esa época", "El sintético compitió con el natural."),
        ("{F} ¿Qué dos hechos de la ficha explican que el salitre cayera desde 1930?", "la crisis mundial y la competencia del salitre sintético", "La ficha los menciona."),
        ("{F} Una línea de tiempo usa 1 cm = 10 años y parte en 1870. ¿A cuántos cm queda el año 1910?", "4 cm", "(1910 − 1870) ÷ 10 = 4."),
        ("{F} ¿Cuántas ciudades de la ficha son puertos de exportación del salitre?", "tres (Pisagua, Iquique y Antofagasta)", "La ficha las nombra como puertos."),
    ],
    ctx=("Un cartel de museo dice: «Auge del salitre, 1880-1930». ¿Qué dos hechos de la ficha marcan el comienzo y el fin de ese período?", "el inicio del auge desde la década de 1880 y la caída desde 1930", "La ficha ubica esos dos momentos."),
    sc=[("¿Qué es el salitre?", "un mineral del desierto usado como fertilizante y para explosivos", "Es la definición de la clase."),
        ("{F} ¿En qué año se produjo la huelga de Iquique?", "1907", "La ficha lo indica."),
        ("¿Qué quiere decir cuestión social?", "los problemas de pobreza y de condiciones de vida y de trabajo de los obreros", "Es la definición de la clase.")],
    op=("Dibuja una línea de tiempo desde 1870 hasta 1940. Marca al menos siete hechos de la ficha con su año. Usa un color para los hechos económicos y otro para los hechos sociales. Dibuja también un mapa simple del norte con tres puertos. {F}",
        "Puntos en 1879, 1880, 1907, 1912, 1914, 1930, con colores distintos; mapa con Pisagua, Iquique y Antofagasta de norte a sur.",
        ["siete hechos ordenados", "dos colores", "tres puertos bien ubicados"], ["línea de tiempo", "mapa simple"], ["poner Antofagasta al norte de Iquique", "poner la caída antes del auge"],
        "Pide que explique por qué eligió cada color."),
    reinforce="Di en voz alta cinco hechos de la ficha con su año.",
    extend="Escribe una pregunta sobre cómo vivía una familia que llegaba a trabajar a la pampa.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 26 (fuentes inventadas para este cuaderno, basadas en hechos conocidos de la época). "
     "Fuente A, carta de un obrero a su familia, 1905 (texto inventado): «Trabajo todo el día bajo el sol. Me pagan con fichas que solo sirven en la pulpería de la oficina. Los precios son altos». "
     "Fuente B, aviso de una empresa salitrera, 1900 (texto inventado): «Se necesitan trabajadores para la pampa. Habitación y pulpería a disposición del personal». "
     "Fuente C, informe del gobierno, 1910 (texto inventado): «El salitre aporta gran parte de los ingresos del Estado y permite construir escuelas y ferrocarriles». "
     "Fuente D, libro de historia de 2001: explica que el auge del salitre produjo riqueza para el Estado y para las empresas, pero muchos obreros vivían en condiciones difíciles.")
build(
    OA6, 2, F,
    use="Aprenderé a leer fuentes sobre el período del salitre preguntando quién habla y desde qué lugar. Sirve para no creer que todos vivieron el auge del mismo modo.",
    prior=["Sé qué es una fuente primaria y una secundaria.", "Sé qué fue el salitre.", "Sé que cada fuente tiene un punto de vista."],
    explain=[
        "Sobre el salitre existen fuentes muy distintas: cartas de obreros, avisos de empresas, informes del gobierno y libros de historia. Cada una se produjo para algo. Un aviso busca atraer trabajadores; un informe del gobierno resalta lo que el salitre aportó al país; una carta cuenta una experiencia personal.",
        "La carta del obrero (fuente A) muestra el trabajo duro y el pago en fichas, que solo servían en la tienda de la oficina. El aviso de la empresa (fuente B) muestra lo que la empresa quería mostrar. El informe del gobierno (fuente C) destaca la riqueza para el Estado. Las tres son primarias, pero hablan de lugares sociales distintos.",
        "El libro de 2001 (fuente D) es secundario y reúne ambas miradas. Aun así, ninguna fuente de la ficha nos dice qué pensaban las mujeres de la pampa, los niños que trabajaban o los empresarios extranjeros. Por eso hay que pedir más fuentes y no generalizar desde una sola.",
    ],
    vocab=[("ficha (salitrera)", "moneda propia de una empresa, válida solo en su tienda"), ("pulpería", "tienda de la oficina salitrera donde los obreros compraban sus productos"), ("aviso", "mensaje público para ofrecer algo"), ("informe", "documento que explica una situación"), ("generalizar", "decir que algo es igual para todos a partir de un solo caso")],
    worked=[
        ("Reconocer el propósito", "{F} ¿Para qué se escribió la fuente B?", ["Es un aviso de una empresa.", "Busca atraer trabajadores a la pampa."], "Para atraer trabajadores"),
        ("Reconocer un límite", "{F} ¿Qué no dice la fuente C?", ["Habla de ingresos del Estado.", "No dice cómo vivían los obreros."], "Cómo vivían los obreros"),
    ],
    mistakes=[("Creer que el aviso de la empresa muestra cómo era realmente el trabajo.", "Se olvida su propósito.", "Un aviso busca atraer trabajadores, así que destaca lo positivo."),
              ("Pensar que la carta de un obrero habla por todos.", "Se generaliza desde un caso.", "Es la experiencia de una persona; hay que compararla con otras.")],
    T=[
        ("{F} ¿Con qué se pagaba al obrero de la fuente A?", "con fichas", "La carta lo dice."),
        ("{F} ¿En qué año se escribió el informe del gobierno?", "1910", "La ficha lo indica."),
        ("{F} ¿Qué dos cosas ofrece el aviso de la fuente B?", "habitación y pulpería", "El aviso las menciona."),
        ("{F} ¿Cuál de las cuatro fuentes es secundaria?", "la fuente D", "Se escribió en 2001."),
        ("=", "{F} ¿Cuántos años pasaron entre la fuente B y la fuente C?", "1910-1900", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué critica el obrero de la fuente A?", "que le pagan con fichas y que los precios son altos", "La carta lo dice."),
        ("{F} ¿Qué valora el informe de la fuente C del salitre?", "que aporta ingresos al Estado para escuelas y ferrocarriles", "La fuente lo dice."),
        ("{F} Compara A y C: ¿quién habla de condiciones de trabajo y quién de ingresos del Estado?", "A habla de condiciones de trabajo y C de ingresos del Estado", "Cada una habla desde su lugar."),
        ("{F} Un compañero dice: «La fuente C prueba que todos mejoraron su vida». ¿Qué error comete?", "generaliza: el informe habla de ingresos del Estado, no de la vida de todos", "No dice nada sobre los obreros."),
        ("{F} Una alumna dice: «La fuente A es falsa porque es una sola carta». ¿Qué le responderías?", "no es falsa, pero muestra solo una experiencia y hay que compararla con otras fuentes", "Una carta sirve, pero es parcial."),
        ("{F} Nombra un grupo, mencionado en la explicación de la clase, que no aparece en ninguna fuente de la ficha.", "las mujeres de la pampa, los niños que trabajaban o los empresarios extranjeros (uno cualquiera)", "Ninguna los menciona."),
        ("{F} Para saber cómo vivían los obreros, ¿qué fuente es más útil: A, B o C?", "la A", "Es testimonio directo de un obrero."),
        ("{F} Ordena las fuentes de la más antigua a la más reciente.", "B, A, C, D", "Los años son 1900, 1905, 1910 y 2001."),
    ],
    ctx=("Un grupo escolar quiere presentar solo el aviso de la fuente B para explicar cómo era trabajar en el salitre. ¿Qué le dirías?", "que agregue la carta del obrero, porque el aviso solo muestra lo que la empresa quería mostrar", "Un aviso tiene propósito comercial."),
    sc=[("¿Qué pregunta haces para saber el propósito de una fuente?", "¿para qué se creó?", "El propósito explica su punto de vista."),
        ("{F} ¿Qué tipo de fuente es la A?", "primaria", "Se escribió en 1905."),
        ("¿Por qué no hay que generalizar desde una sola carta?", "porque muestra la experiencia de una sola persona", "Otras personas pudieron vivir distinto.")],
    op=("Haz una ficha con las fuentes A, B y C. Anota quién habla, año, qué dice, qué propósito tiene y qué no dice. Después, escribe dos oraciones que expliquen por qué una conclusión sobre el salitre necesita varias fuentes. {F}",
        "A: obrero, 1905, trabajo duro y pago en fichas; no dice qué piensa la empresa. B: empresa, 1900, atraer trabajadores; no dice los problemas.",
        ["tres fichas completas", "propósito identificado", "límite razonable en cada una"], ["ficha de análisis", "dos oraciones"], ["tratar B como descripción objetiva", "no anotar límites"],
        "Pide que explique en voz alta qué fuente le pareció más persuasiva y por qué."),
    reinforce="Con tus palabras, resume lo que cuenta cada fuente de la ficha.",
    extend="Escribe una pregunta sobre qué pensaría una mujer que vivía en una oficina salitrera.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 27 (causas y consecuencias, hecha para este cuaderno). "
     "Expansión económica: el salitre se exportaba a otros países; Chile cobraba un impuesto a la exportación y el Estado recibía muchos ingresos; con ese dinero se construyeron ferrocarriles, puertos, caminos, escuelas y edificios públicos; las ciudades del norte crecieron y llegaron trabajadores desde el centro y el sur de Chile. "
     "Cuestión social: salarios bajos y jornadas largas; pago con fichas válidas solo en la pulpería de la oficina; viviendas pequeñas y sin higiene (conventillos en las ciudades); enfermedades y poco acceso a la educación; desde fines del siglo XIX, los obreros se organizaron en mutuales, sociedades y sindicatos, y hubo huelgas para pedir mejores condiciones. "
     "Actores: obreros, dueños de empresas (muchos extranjeros), el Estado y las ciudades.")
build(
    OA6, 3, F,
    use="Aprenderé a explicar la expansión económica del salitre y el origen de la cuestión social. Sirve para entender quiénes se beneficiaron, quiénes sufrieron y por qué hubo huelgas.",
    prior=["Sé ubicar el período del salitre.", "Sé distinguir causa y consecuencia.", "Sé que un mismo hecho afecta distinto a cada grupo."],
    explain=[
        "La expansión económica del salitre tuvo una causa principal: la gran venta de este mineral a otros países. Una consecuencia fue que el Estado recibió muchos ingresos gracias al impuesto a la exportación. Con ese dinero se construyeron ferrocarriles, puertos, caminos y escuelas, y las ciudades del norte crecieron.",
        "Al mismo tiempo apareció la cuestión social. Muchos obreros ganaban poco, trabajaban muchas horas y recibían fichas en vez de dinero. En las ciudades, familias pobres vivían en conventillos, viviendas pequeñas y sin higiene. Esta desigualdad fue una causa de que los obreros se organizaran en mutuales y sindicatos y realizaran huelgas.",
        "Los actores del período fueron los obreros, los dueños de las empresas (muchos extranjeros), el Estado y las ciudades. Un mismo hecho puede ser positivo para unos y negativo para otros. Por eso, para explicar, siempre hay que preguntar quiénes ganaron y quiénes perdieron.",
    ],
    vocab=[("conventillo", "vivienda colectiva de piezas pequeñas donde vivían muchas familias"), ("sindicato", "organización de trabajadores para defender sus derechos"), ("huelga", "paro de trabajadores para exigir mejores condiciones"), ("mutual", "sociedad de ayuda entre trabajadores"), ("desigualdad", "diferencia grande en riqueza o derechos entre personas")],
    worked=[
        ("Clasificar causa y consecuencia", "{F} ¿Que el Estado construyera ferrocarriles es causa o consecuencia del impuesto al salitre?", ["Los ferrocarriles se construyeron con ese dinero.", "Ocurren después de recibir ingresos."], "Consecuencia"),
        ("Identificar un actor", "{F} ¿Quiénes se organizaron en mutuales y sindicatos?", ["Busco al grupo que reclamaba por sus condiciones.", "Eran los obreros."], "Los obreros"),
    ],
    mistakes=[("Pensar que el auge del salitre benefició a todos por igual.", "Se miran solo los ingresos del Estado.", "Los obreros tuvieron bajos salarios y condiciones difíciles."),
              ("Creer que la cuestión social era solo un problema de la pampa.", "Se olvida la vida en las ciudades.", "También apareció en las ciudades, por ejemplo en los conventillos.")],
    T=[
        ("{F} ¿Con qué se pagaba a muchos obreros en las oficinas salitreras?", "con fichas", "La ficha lo dice."),
        ("{F} ¿Qué cobraba el Estado al salitre exportado?", "un impuesto", "La ficha lo dice."),
        ("{F} ¿Cómo se llamaban las viviendas pequeñas y sin higiene de las ciudades?", "conventillos", "La ficha las nombra."),
        ("{F} Clasifica como «expansión económica» (E) o «cuestión social» (S): a) ferrocarriles; b) pago con fichas; c) puertos; d) viviendas sin higiene.", "a: E; b: S; c: E; d: S", "Los problemas de los obreros son cuestión social."),
        ("{F} ¿Qué hicieron los obreros para pedir mejores condiciones?", "se organizaron en sindicatos y realizaron huelgas", "La ficha lo dice."),
        ("{F} ¿Qué efecto tuvo el impuesto al salitre en las ciudades del norte?", "crecieron", "La ficha lo dice."),
        ("{F} ¿Quiénes eran muchos de los dueños de las empresas salitreras?", "extranjeros", "La ficha lo indica."),
        ("{F} ¿Qué causa de la ficha explica la cuestión social?", "salarios bajos, jornadas largas y viviendas precarias", "Son las condiciones de los obreros."),
        ("{F} Un compañero dice: «Todos ganaron con el salitre». Corrígelo con un dato.", "no: los obreros tenían salarios bajos y vivían en viviendas precarias", "La ficha describe esas condiciones."),
        ("{F} Una alumna dice: «Las huelgas ocurrieron sin motivos». ¿Qué dato de la ficha lo contradice?", "que pedían mejores condiciones de trabajo y de vida", "Había causas concretas."),
        ("{F} ¿Qué consecuencia positiva tuvo el salitre para el Estado?", "recibió muchos ingresos para construir obras", "La ficha lo dice."),
        ("{F} Elige la mejor explicación de la cuestión social. A) Un conjunto de problemas de vida y trabajo de los obreros. B) Una fiesta de la pampa.", "A", "La ficha enumera esos problemas."),
        ("{F} ¿Qué pregunta ayuda a no creer que el salitre benefició a todos por igual?", "quiénes ganaron y quiénes perdieron", "Muestra los distintos efectos."),
    ],
    ctx=("Un diario de 1908 dice: «El salitre ha traído solo riqueza a Chile». Usa la ficha para responder.", "no: también produjo cuestión social, con salarios bajos, fichas y viviendas precarias", "La ficha muestra problemas y no solo riqueza."),
    sc=[("¿Qué es una huelga?", "un paro de trabajadores para exigir mejores condiciones", "Es la definición de la clase."),
        ("{F} ¿Qué construyó el Estado con los ingresos del salitre?", "ferrocarriles, puertos, caminos, escuelas y edificios", "La ficha lo dice."),
        ("¿Por qué se organizaron los obreros?", "para defender sus derechos y mejorar sus condiciones", "Es la causa de los sindicatos.")],
    op=("Dibuja una tabla con dos columnas, «expansión económica» y «cuestión social». Escribe tres elementos de la ficha en cada una. Debajo, escribe una oración que explique cómo una causa de la expansión llevó a una consecuencia social. {F}",
        "Expansión: impuesto, ferrocarriles, ciudades del norte. Cuestión social: fichas, conventillos, salarios bajos. Oración: el auge atrajo trabajadores, pero no tenían viviendas dignas.",
        ["tres elementos por columna", "elementos en la columna correcta", "oración que conecta causa y consecuencia"], ["tabla de dos columnas", "una oración"], ["poner fichas en expansión", "no conectar causa y consecuencia"],
        "Pide que cambie un elemento de columna y explique por qué quedaría mal."),
    reinforce="Di tres ejemplos de expansión económica y tres de cuestión social.",
    extend="Escribe una pregunta sobre qué habría pasado si el Estado hubiera usado más dinero del salitre en viviendas para los obreros.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 28 (perspectivas sobre el salitre, hecha para este cuaderno; textos inventados). "
     "Dueño de una oficina salitrera (1906): «El salitre trae progreso. Damos trabajo, vivienda y una tienda. Los obreros no tienen de qué quejarse». "
     "Obrero de la pampa (1906): «Trabajamos muchas horas, nos pagan con fichas y los precios en la pulpería son altos. Queremos mejor salario y pago en dinero». "
     "Funcionario del gobierno (1906): «El salitre financia al Estado. Es importante mantener el orden y la producción». "
     "Comerciante de Iquique (1906): «Con el salitre venden más productos mis clientes y la ciudad crece, pero hay mucha gente pobre que llega sin vivienda».")
build(
    OA6, 4, F,
    use="Aprenderé a comparar cómo veían el auge del salitre el dueño, el obrero, el funcionario y el comerciante. Sirve para entender por qué hubo conflictos.",
    prior=["Sé qué fue el auge del salitre y la cuestión social.", "Sé que una perspectiva es un punto de vista.", "Sé distinguir hecho de opinión."],
    explain=[
        "Una perspectiva es la manera de ver un hecho según la situación de quien lo vive. En el período del salitre, el dueño de una oficina, el obrero, el funcionario del gobierno y el comerciante tenían intereses distintos. Por eso cada uno describía el mismo auge de manera diferente.",
        "El dueño destacaba el progreso y decía que daba trabajo. El obrero hablaba de largas jornadas, de las fichas y de los precios altos. El funcionario resaltaba los ingresos del Estado y el orden. El comerciante veía que su negocio crecía, pero también la pobreza de quienes llegaban a la ciudad sin vivienda.",
        "Comparar perspectivas es ver qué defiende cada una, qué teme y qué dato calla. Es un hecho que se pagaba con fichas; es una opinión decir que los obreros no tienen de qué quejarse. Entender las perspectivas ayuda a comprender por qué la cuestión social generó conflictos como las huelgas.",
    ],
    vocab=[("perspectiva", "manera de ver un hecho según la situación de quien lo vive"), ("interés", "lo que un grupo quiere lograr o proteger"), ("progreso", "avance económico o material de una sociedad"), ("conflicto", "desacuerdo fuerte entre personas o grupos"), ("orden", "situación en que no hay desorden ni protestas")],
    worked=[
        ("Reconocer un interés", "{F} ¿Qué quiere proteger el funcionario del gobierno?", ["Leo su texto.", "Habla de mantener el orden y la producción."], "El orden y la producción del salitre"),
        ("Separar hecho de opinión", "{F} ¿«Se paga con fichas» es un hecho o una opinión?", ["Se puede comprobar con documentos de la época.", "No depende de lo que piense cada persona."], "Un hecho"),
    ],
    mistakes=[("Creer que la perspectiva del dueño muestra cómo vivían los obreros.", "Se olvida su interés.", "Cada perspectiva responde a su situación; hay que contrastarlas."),
              ("Pensar que una sola perspectiva dice toda la verdad.", "Se confunde comprender con aceptar.", "Se comparan todas para tener una visión más completa.")],
    T=[
        ("{F} ¿Qué quiere el obrero que cambie?", "mejor salario y pago en dinero", "El texto lo dice."),
        ("{F} ¿Qué dice el dueño de la oficina que da a los trabajadores?", "trabajo, vivienda y una tienda", "El texto lo dice."),
        ("{F} ¿Qué preocupa al comerciante de Iquique, además de su negocio?", "la mucha gente pobre que llega sin vivienda", "El texto lo dice."),
        ("{F} ¿Qué perspectiva destaca los ingresos del Estado?", "la del funcionario del gobierno", "El texto lo dice."),
        ("=", "{F} En un ejemplo de práctica con cifras inventadas, un obrero gana 30 fichas al día y un pan cuesta 2 fichas en la pulpería. ¿Cuántos panes puede comprar con el sueldo de un día?", "30//2", "Se divide el sueldo por el precio.", " panes"),
        ("{F} Clasifica como hecho (H) u opinión (O): a) El pago es con fichas; b) los obreros no tienen de qué quejarse; c) el salitre financia al Estado.", "a: H; b: O; c: H", "Los hechos se pueden comprobar."),
        ("{F} ¿Qué tienen en común el dueño y el funcionario?", "ambos valoran de forma positiva el salitre y su producción", "Los dos valoran el auge."),
        ("{F} ¿En qué se diferencian el dueño y el obrero?", "el dueño dice que los obreros no tienen de qué quejarse y el obrero reclama por su salario", "Defienden intereses opuestos."),
        ("{F} Un compañero dice: «El dueño miente porque piensa distinto del obrero». ¿Qué error comete?", "confunde perspectiva con mentira: cada uno habla desde su interés", "Las perspectivas se analizan con evidencia."),
        ("{F} Una alumna dice: «El comerciante solo piensa en dinero». ¿Qué dato de la ficha la contradice?", "que también menciona la pobreza de quienes llegan sin vivienda", "Su texto incluye una preocupación social."),
        ("{F} ¿Qué perspectiva falta en la ficha?", "la de las mujeres y los niños de la pampa", "Ninguna de las cuatro los menciona."),
        ("{F} Elige la mejor oración comparativa. A) Mientras el dueño destaca el progreso, el obrero reclama por su salario. B) Todos piensan igual.", "A", "A compara dos perspectivas."),
        ("{F} ¿Por qué comparar perspectivas ayuda a entender las huelgas?", "porque muestra que los obreros y los dueños tenían intereses opuestos", "Los desacuerdos llevaron a conflictos."),
    ],
    ctx=("En un debate escolar, un compañero dice que el salitre fue «solo progreso». Usa dos perspectivas de la ficha para responderle.", "el dueño habla de progreso, pero el obrero reclama por salarios, fichas y precios altos", "Se contraponen dos perspectivas."),
    sc=[("¿Qué es una perspectiva?", "la manera de ver un hecho según la situación de quien lo vive", "Es la definición de la clase."),
        ("{F} ¿Qué perspectiva habla de las fichas?", "la del obrero", "Su texto las menciona."),
        ("¿Comprender una perspectiva es estar de acuerdo con ella?", "no, es entender por qué piensa así", "Comprender no es aprobar.")],
    op=("Elige dos perspectivas de la ficha y escribe un cuadro con tres filas: «qué defiende», «qué teme» y «qué dato calla». Después escribe una oración que compare ambas y otra que diga qué perspectiva falta. {F}",
        "Dueño: defiende el progreso; teme las quejas; calla el pago con fichas. Obrero: defiende un mejor salario; teme la pobreza; calla los beneficios de la empresa.",
        ["dos perspectivas con tres filas", "oración comparativa", "perspectiva faltante nombrada"], ["cuadro", "dos oraciones"], ["decir que una perspectiva es la única verdadera", "no incluir la perspectiva faltante"],
        "Pide que explique qué fila le pareció más difícil."),
    reinforce="Di en voz alta qué defiende cada una de las cuatro personas de la ficha.",
    extend="Escribe una pregunta que le harías al obrero de la ficha sobre su vida en la pampa.",
)
