"""Ciencias Naturales EPJA Básica N2, módulo 3 (parte 3): OAD-11, flujos de materia y energía en los ecosistemas (cadenas y tramas tróficas) a partir de diagramas descritos. Todo en papel; los ecosistemas y los datos son de ejemplo, inventados y rotulados."""
from __future__ import annotations

from hc_common import make_build


MATERIALS = ("Papel, lápiz y goma. Todos los diagramas están descritos con palabras y flechas dentro de cada ejercicio; los ecosistemas, las especies y los números son ejemplos inventados para practicar. "
             "No se necesitan salidas a terreno ni observar animales. Si algo te cuesta leer, pide apoyo a quien te acompañe.")
build = make_build(MATERIALS)

O = "EPJA-CNAT-NB2-OAD-11"
PRIOR = ["Conozco plantas, animales y hongos de mi entorno y sé que se alimentan de distinto modo.", "Sé leer listas y diagramas sencillos con flechas."]

# ============================================================ clase 1
F = ("Ficha 1 (laguna de ejemplo, inventada). Seres vivos: juncos, algas, insectos acuáticos, ranas, peces pequeños y garzas. "
     "Elementos sin vida: agua, luz del Sol, suelo, aire y temperatura.")
build(
    O, 1, F,
    use="Hoy reconozco qué es un ecosistema y distingo lo vivo de lo no vivo en un lugar que ya conozco.",
    prior=PRIOR,
    explain=[
        "Un ecosistema es un lugar donde los seres vivos y los elementos sin vida se relacionan entre sí. Una laguna, un bosque, una playa y una plaza con árboles son ecosistemas. Tú ya conoces alguno cerca de donde vives.",
        "Los seres vivos se llaman factores bióticos: plantas, animales, hongos y microbios. Los elementos sin vida se llaman factores abióticos: agua, luz, suelo, aire y temperatura. Unos dependen de otros: las plantas necesitan luz y agua; los animales necesitan plantas u otros animales para alimentarse.",
        "Para describir un ecosistema, conviene anotar qué seres vivos hay, qué elementos sin vida hay y cómo se relacionan. Así se empieza a entender cómo fluyen la materia y la energía por él.",
    ],
    vocab=[("ecosistema", "lugar donde seres vivos y elementos sin vida se relacionan"), ("factor biótico", "ser vivo de un ecosistema"), ("factor abiótico", "elemento sin vida de un ecosistema"), ("relación", "lo que une a un ser vivo con otro o con su ambiente")],
    worked=[
        ("Separar lo vivo de lo no vivo", F, ["Los juncos, las algas, los insectos, las ranas, los peces y las garzas son seres vivos.", "El agua, la luz, el suelo, el aire y la temperatura no tienen vida."], "Bióticos: juncos, algas, insectos, ranas, peces, garzas. Abióticos: agua, luz, suelo, aire, temperatura"),
        ("Una relación", "En la laguna, las ranas se alimentan de insectos acuáticos.", ["Una rana es un ser vivo y el insecto también.", "La rana depende del insecto para alimentarse."], "Es una relación entre dos seres vivos: la rana se alimenta del insecto"),
    ],
    mistakes=[("Pensar que el agua o el sol son seres vivos porque «hacen vivir» a las plantas.", "Son factores abióticos: no nacen, no crecen ni se reproducen.", "Pregunta si nace, crece y se reproduce."),
              ("Decir que un ecosistema solo incluye animales.", "También incluye plantas, hongos, microbios y elementos sin vida.", "Anota siempre lo vivo y lo no vivo.")],
    T=[
        ("abc", "{F} ¿Cuál de estos es un factor biótico?", "La rana", "El agua", "La luz del Sol", "La rana es un ser vivo; el agua y la luz no lo son."),
        ("ab", "{F} ¿Cuál de estos es un factor abiótico?", "El suelo", "Las algas", "El suelo no tiene vida, por eso es abiótico."),
        ("abc", "{F} De los seis seres vivos de la ficha, ¿cuántos son animales?", "4", "2", "6", "Son animales los insectos acuáticos, las ranas, los peces pequeños y las garzas; los juncos y las algas no."),
        ("abc", "¿Qué es un ecosistema?", "Un lugar donde seres vivos y elementos sin vida se relacionan", "Solo un conjunto de animales", "Un lugar sin plantas", "Incluye lo vivo, lo no vivo y sus relaciones."),
        ("ab", "¿Qué necesitan las plantas de la laguna para vivir?", "Luz, agua y suelo o nutrientes del agua", "Solo animales", "Las plantas obtienen su alimento con luz y agua, entre otros elementos."),
        ("abc", "{F} ¿Cuál afirmación describe una relación?", "Las ranas se alimentan de insectos acuáticos", "El suelo es oscuro", "El aire es invisible", "Una relación une dos elementos: aquí quién se alimenta de quién."),
        ("=", "{F} La ficha nombra 5 elementos sin vida. Si se agregara el viento, ¿cuántos serían?", "5+1", "Se suma el elemento nuevo a los que ya estaban.", " elementos"),
        ("abc", "{F} Una persona dice que la laguna sin garzas sigue siendo un ecosistema. ¿Es correcto?", "Sí, porque quedan seres vivos y elementos sin vida relacionados", "No, solo hay ecosistema con garzas", "No, porque falta el sol", "El ecosistema continúa mientras haya relaciones entre lo vivo y lo no vivo."),
        ("ab", "Una plaza con pasto, árboles, aves, tierra y agua de riego, ¿es un ecosistema?", "Sí, porque tiene seres vivos y elementos sin vida que se relacionan", "No, porque la hizo una persona", "Cualquier lugar con esas relaciones es un ecosistema."),
        ("abc", "{F} ¿Qué ocurriría con las algas si faltara la luz por muchos días?", "No podrían producir su alimento y disminuirían", "Crecerían más", "No pasaría nada", "Las algas necesitan luz para producir su alimento."),
        ("abc", "Una persona dice «el agua es viva porque siempre se mueve». ¿Qué respuesta corrige?", "Moverse no basta: un ser vivo nace, crece, se reproduce y se alimenta", "Tiene razón", "El agua es un animal", "Los seres vivos cumplen funciones propias."),
        ("abc", "{F} Se anotan factores del ecosistema como: juncos, agua, ranas, aire. ¿Cuántos son abióticos?", "2", "3", "1", "Solo el agua y el aire son abióticos."),
        ("ab", "Para describir un ecosistema, ¿qué conviene anotar?", "Seres vivos, elementos sin vida y sus relaciones", "Solo el nombre", "Con esos tres elementos se entiende cómo funciona."),
    ],
    ctx=("abc", "En una reunión sobre un humedal cercano, una persona dice que «lo importante son solo los pájaros». ¿Qué respuesta se apoya en lo aprendido?", "El humedal también incluye plantas, agua, suelo y otros seres vivos que se relacionan con las aves", "Los pájaros son lo único que importa", "El humedal es solo agua", "Un ecosistema reúne lo vivo y lo no vivo."),
    sc=[("En Ciencias: ¿qué es un factor abiótico?", "Un elemento sin vida del ecosistema", "Por ejemplo, el agua, la luz o el suelo."),
        ("En Ciencias: ¿qué es un ecosistema y qué incluye?", "Un lugar donde seres vivos y elementos sin vida se relacionan", "Incluye plantas, animales, hongos, microbios y ambiente físico."),
        ("¿Qué es un factor biótico?", "Un ser vivo del ecosistema", "Entre los seres vivos están las plantas, los animales, los hongos y los microbios.")],
    op=("Piensa en un ecosistema de tu entorno (una plaza, un cerro, una playa o un sitio con plantas) o usa esta escena de ejemplo: un pastizal con pasto, insectos, aves, tierra, lluvia y sol. Escribe una lista con cinco factores bióticos y cinco abióticos y una frase que describa una relación entre dos de ellos.",
        "Pastizal: bióticos: pasto, insectos, aves, hongos, lombrices. Abióticos: tierra, lluvia, sol, aire, temperatura. Relación: los insectos comen pasto.",
        ["separa bien lo vivo y lo no vivo", "da cinco de cada tipo", "describe una relación"],
        ["dos listas y una frase"],
        ["poner el sol o el agua como seres vivos", "olvidar la relación"],
        "Pregunta: «¿Nace, crece y se reproduce?»."),
    reinforce="Nombra tres seres vivos y tres elementos sin vida que veas desde una ventana o en la calle.",
    extend="Explica por qué cambiar el agua de un lugar puede afectar a plantas y animales.",
)

# ============================================================ clase 2
F = ("Ficha 2 (pradera de ejemplo). Pasto; saltamontes que se alimentan de pasto; lagartijas que comen saltamontes; "
     "zorros que comen lagartijas; hongos y bacterias del suelo que descomponen hojas secas y animales muertos.")
build(
    O, 2, F,
    use="Hoy aprendo el papel de productores, consumidores y descomponedores en un ecosistema.",
    prior=PRIOR + ["Distingo factores bióticos y abióticos."],
    explain=[
        "En un ecosistema cada ser vivo cumple un papel según cómo obtiene su alimento. Los productores, como las plantas y las algas, fabrican su propio alimento usando luz del Sol, agua y dióxido de carbono; este proceso se llama fotosíntesis y libera oxígeno.",
        "Los consumidores no pueden fabricar su alimento y se alimentan de otros seres vivos. Los herbívoros comen plantas, los carnívoros comen animales y los omnívoros comen de ambos. Los descomponedores, como los hongos y las bacterias, se alimentan de restos de seres vivos y devuelven nutrientes al suelo.",
        "Saber el papel de cada ser vivo ayuda a entender cómo pasan la materia y la energía por el ecosistema. Sin productores no hay alimento de base, y sin descomponedores los nutrientes quedarían en los restos.",
    ],
    vocab=[("productor", "ser vivo que fabrica su propio alimento"), ("consumidor", "ser vivo que se alimenta de otros seres vivos"), ("descomponedor", "ser vivo que se alimenta de restos y devuelve nutrientes"), ("fotosíntesis", "proceso en que las plantas fabrican su alimento con luz, agua y dióxido de carbono")],
    worked=[
        ("Clasificar por papel", F, ["El pasto fabrica su alimento: es productor.", "Saltamontes, lagartijas y zorros comen otros seres vivos: son consumidores.", "Hongos y bacterias descomponen restos."], "Productor: pasto. Consumidores: saltamontes, lagartijas, zorros. Descomponedores: hongos y bacterias"),
        ("Tipo de consumidor", "Un saltamontes come pasto.", ["Se alimenta de una planta.", "Eso corresponde a un herbívoro."], "El saltamontes es un consumidor herbívoro"),
    ],
    mistakes=[("Llamar productor a un animal porque «produce crías» o estiércol.", "En ciencias, productor es el que fabrica su alimento con energía del Sol.", "Pregunta cómo consigue su alimento."),
              ("Creer que los descomponedores solo «limpian».", "También devuelven nutrientes al suelo y permiten que las plantas los usen.", "Piensa en lo que devuelven al ecosistema.")],
    T=[
        ("abc", "{F} ¿Cuál es el productor de la pradera?", "El pasto", "El zorro", "Los hongos", "El pasto fabrica su alimento con luz solar."),
        ("ab", "{F} ¿Qué tipo de consumidor es el saltamontes?", "Herbívoro", "Carnívoro", "Se alimenta de pasto, que es una planta."),
        ("abc", "{F} ¿Quiénes son los descomponedores?", "Hongos y bacterias del suelo", "Zorros y lagartijas", "Saltamontes", "Descomponen hojas secas y animales muertos."),
        ("abc", "¿Qué necesita una planta para fabricar su alimento?", "Luz del Sol, agua y dióxido de carbono", "Solo tierra", "Alimento de otros animales", "Esos tres ingredientes participan en la fotosíntesis."),
        ("ab", "{F} ¿Qué consumidor es la lagartija?", "Carnívoro, porque come saltamontes", "Herbívoro", "Come animales, por eso es carnívora."),
        ("abc", "{F} De los seres vivos de la ficha, ¿cuántos son consumidores?", "3", "1", "5", "Son consumidores el saltamontes, la lagartija y el zorro; el pasto es productor y los hongos y bacterias son descomponedores."),
        ("abc", "{F} ¿Qué pasaría si desaparecieran los descomponedores?", "Los restos se acumularían y los nutrientes volverían menos al suelo", "Habría más luz", "Los zorros serían productores", "Sin descomponedores los nutrientes quedan retenidos en los restos."),
        ("abc", "Una persona come arroz y carne. ¿Qué tipo de consumidor es?", "Omnívoro", "Herbívoro", "Descomponedor", "Come plantas y animales, es decir, se alimenta de productores y de consumidores."),
        ("ab", "¿Qué libera la fotosíntesis a la atmósfera?", "Oxígeno", "Plástico", "Las plantas liberan oxígeno al hacer fotosíntesis."),
        ("abc", "{F} Una persona afirma que el zorro es productor porque «parece que mantiene la pradera». ¿Qué corrección es correcta?", "El zorro es consumidor porque se alimenta de otros seres vivos", "Tiene razón", "El zorro es un descomponedor", "El zorro no fabrica alimento con luz: lo consigue comiendo lagartijas."),
        ("=", "En un huerto de ejemplo hay 6 plantas de lechuga y 4 de tomate, todas productoras. ¿Cuántos productores hay?", "6+4", "Se suman las plantas de ambos cultivos.", " plantas"),
        ("abc", "{F} Si se retiraran todos los saltamontes, ¿qué sería probable que ocurra con las lagartijas?", "Tendrían menos alimento", "Tendrían más pasto", "No cambiarían", "Las lagartijas se alimentan de saltamontes, y por eso dependen de ellos."),
        ("ab", "¿Por qué los productores son la base del ecosistema?", "Porque fabrican el alimento de que dependen los demás", "Porque son los más grandes", "Los demás seres vivos se alimentan, directa o indirectamente, de ellos."),
    ],
    ctx=("abc", "En un taller de huerta comunitaria, una persona deja restos de verduras para hacer compost. Otra pregunta qué seres vivos transforman esos restos en abono. ¿Qué respondes?", "Hongos y bacterias, que son descomponedores", "Las lechugas, que son productoras", "Los zorros", "Los descomponedores devuelven nutrientes al suelo."),
    sc=[("En Ciencias: ¿qué es un productor?", "Un ser vivo que fabrica su alimento", "Como las plantas y las algas."),
        ("En una pradera, ¿qué hacen los descomponedores?", "Se alimentan de restos y devuelven nutrientes al suelo", "Por ejemplo, los hongos y las bacterias del suelo son descomponedores."),
        ("¿Qué comen los carnívoros?", "Otros animales", "Los herbívoros comen plantas y los omnívoros ambos.")],
    op=("Escribe tres seres vivos de un ecosistema que conozcas (o de la pradera de la ficha) y para cada uno di si es productor, consumidor o descomponedor y por qué. Dibuja una flecha simple de quién se alimenta de quién.",
        "Pasto: productor, fabrica su alimento. Saltamontes: consumidor herbívoro. Hongos: descomponedores. Flecha: pasto → saltamontes.",
        ["clasifica correctamente los tres", "da una razón para cada uno", "dibuja una flecha coherente"],
        ["tres frases y un esquema"],
        ["decir que un animal es productor", "poner la flecha al revés"],
        "Pregunta: «¿Cómo consigue su alimento?»."),
    reinforce="Haz una lista de cinco alimentos que comas y di si vienen de productores o de consumidores.",
    extend="Explica por qué un bosque sin hongos ni bacterias acumularía restos.",
)

# ============================================================ clase 3
F = ("Ficha 3 (cadenas de ejemplo). Cadena terrestre: pasto → saltamontes → lagartija → aguilucho. "
     "Cadena marina: fitoplancton → zooplancton → anchoveta → pingüino. La flecha va de lo que es comido hacia quien lo come.")
build(
    O, 3, F,
    use="Hoy aprendo, paso a paso, a leer y armar una cadena trófica y a seguir el camino de la energía.",
    prior=PRIOR + ["Distingo productores, consumidores y descomponedores."],
    explain=[
        "Una cadena trófica muestra quién se alimenta de quién, en orden. Se lee con flechas que apuntan de lo que es comido hacia quien lo come. Por eso la energía se mueve en la dirección de las flechas.",
        "Para armar una cadena sigue tres pasos. Paso 1: ubica el productor, que va al comienzo. Paso 2: agrega el consumidor que se alimenta de él, llamado consumidor primario. Paso 3: continúa con el consumidor secundario, que se alimenta del primario, y así hasta el último.",
        "Cada ser vivo ocupa un nivel trófico. El primer nivel son los productores, el segundo los consumidores primarios, el tercero los secundarios y así sucesivamente. Los descomponedores actúan en todos los niveles, porque se alimentan de los restos.",
    ],
    vocab=[("cadena trófica", "serie de seres vivos donde cada uno se alimenta del anterior"), ("nivel trófico", "lugar que ocupa un ser vivo en una cadena"), ("consumidor primario", "el que se alimenta del productor"), ("consumidor secundario", "el que se alimenta de un consumidor primario")],
    worked=[
        ("Leer una cadena", F, ["Tomo la cadena terrestre.", "Leo las flechas: el pasto es comido por el saltamontes, que es comido por la lagartija, que es comida por el aguilucho."], "La energía va del pasto al saltamontes, a la lagartija y al aguilucho"),
        ("Ubicar niveles", "En la cadena marina de la ficha, ¿quién es el consumidor primario?", ["El productor es el fitoplancton.", "El primero que se alimenta de él es el zooplancton."], "El zooplancton es el consumidor primario"),
    ],
    mistakes=[("Poner la flecha desde el que come hacia lo que es comido.", "La flecha indica el camino de la energía: desde lo comido hacia quien come.", "Lee la flecha como «es comido por»."),
              ("Empezar la cadena con un consumidor.", "Toda cadena empieza en un productor.", "Busca primero quién fabrica su alimento.")],
    T=[
        ("abc", "{F} ¿Quién es el productor en la cadena terrestre?", "El pasto", "El saltamontes", "El aguilucho", "Todo comienza en el productor, que es el pasto."),
        ("ab", "{F} ¿Qué consumidor primario hay en la cadena terrestre?", "El saltamontes", "La lagartija", "El saltamontes come pasto, es el primer consumidor."),
        ("=", "{F} ¿Cuántas flechas tiene la cadena marina?", "4-1", "Hay cuatro seres vivos y una flecha entre cada par, es decir, una menos que los seres vivos.", " flechas"),
        ("abc", "{F} ¿De quién se alimenta la lagartija en la cadena?", "Del saltamontes", "Del aguilucho", "Del pasto", "La flecha apunta del saltamontes a la lagartija."),
        ("ab", "{F} ¿Qué indica la flecha entre el zooplancton y la anchoveta?", "Que la anchoveta se alimenta del zooplancton", "Que el zooplancton come anchovetas", "La flecha va de lo comido hacia quien lo come."),
        ("abc", "{F} ¿Qué nivel trófico ocupa la lagartija?", "Tercero", "Segundo", "Primero", "Pasto es el primero, saltamontes el segundo y lagartija el tercero."),
        ("abc", "{F} ¿Qué nivel trófico ocupa el pingüino en la cadena marina?", "Cuarto", "Primero", "Segundo", "Cuenta fitoplancton, zooplancton, anchoveta y pingüino."),
        ("=", "{F} Si se agregara un ser vivo más a la cadena marina, que ya tiene 4, ¿cuántos niveles tendría?", "4+1", "Se agrega un nivel a los cuatro que ya hay.", " niveles"),
        ("ab", "Ordena: ¿cuál es una cadena trófica válida?", "Pasto → conejo → zorro", "Zorro → conejo → pasto", "El productor empieza y los consumidores siguen en orden de quién come a quién."),
        ("abc", "{F} Una persona dice que en la cadena terrestre el aguilucho pasa energía al saltamontes. ¿Qué corrección es correcta?", "La energía va del saltamontes hacia la lagartija y luego al aguilucho", "Tiene razón", "El aguilucho es productor", "La flecha siempre sigue el sentido en que se pasa la energía."),
        ("abc", "{F} Si disminuyen mucho las anchovetas, ¿qué sería probable que ocurra con los pingüinos?", "Tendrían menos alimento", "Tendrían más alimento", "No les afectaría", "Los pingüinos se alimentan de anchovetas."),
        ("abc", "Se arma una cadena con estos elementos de ejemplo: lechuza, pasto, ratón. ¿Cuál es el orden correcto?", "Pasto → ratón → lechuza", "Lechuza → ratón → pasto", "Ratón → pasto → lechuza", "Primero el productor y luego los consumidores en orden."),
        ("ab", "¿Por qué una cadena trófica es una simplificación?", "Porque casi todos los seres vivos comen más de una cosa", "Porque nadie come nada", "Las relaciones reales forman redes más complejas."),
    ],
    ctx=("abc", "En un humedal de ejemplo se observa: algas → insectos → ranas → garzas. Una persona pregunta qué pasa si se contamina el agua y mueren las algas. ¿Qué respondes?", "Los insectos tendrían menos alimento y esto afectaría a las ranas y a las garzas", "Solo se afectaría a las algas", "Las garzas comerían más ranas", "Todo el flujo parte de las algas, que son los productores."),
    sc=[("¿Qué indica la flecha en una cadena trófica?", "De lo comido hacia quien lo come", "También marca el camino de la energía."),
        ("En Ciencias: ¿quién inicia una cadena trófica?", "El productor", "Fabrica el alimento de que depende el resto."),
        ("¿Qué es un consumidor primario?", "El que se alimenta de un productor", "Es el segundo nivel de la cadena.")],
    op=("Arma dos cadenas tróficas de cuatro seres vivos cada una, una terrestre y una de agua, usando seres vivos de la pradera y de la laguna que ya conoces. Dibuja las flechas y rotula el productor, el consumidor primario y el último consumidor.",
        "Pasto → saltamontes → lagartija → aguilucho. Productor: pasto. Primario: saltamontes. Último: aguilucho.",
        ["empieza en un productor", "usa flechas en el sentido correcto", "rotula los niveles"],
        ["dos cadenas dibujadas"],
        ["empezar en un consumidor", "poner las flechas al revés"],
        "Pregunta: «¿Quién es comido por quién?»."),
    reinforce="Arma una cadena trófica con tres alimentos de tu mesa, empezando por el productor.",
    extend="Explica qué pasaría con una cadena si desapareciera su productor.",
)

# ============================================================ clase 4
F = ("Ficha 4 (trama de ejemplo, inventada). El conejo y el saltamontes comen pasto. La lagartija come saltamontes. "
     "El zorro come conejos y lagartijas. El aguilucho come conejos y lagartijas. Los hongos descomponen los restos de todos.")
build(
    O, 4, F,
    use="Hoy practico con una trama trófica y analizo qué pasa cuando cambia un organismo.",
    prior=PRIOR + ["Sé armar y leer cadenas tróficas."],
    explain=[
        "En la naturaleza, casi ningún ser vivo come una sola cosa. Por eso las cadenas se cruzan y forman una trama trófica, que es una red de cadenas conectadas. Un mismo ser vivo puede estar en varias cadenas.",
        "Para leer una trama, recorre las flechas desde los productores. Anota quién se alimenta de quién y cuántos caminos llegan a cada ser vivo. Un animal con varias fuentes de alimento tiene más alternativas si una disminuye.",
        "En una trama se pueden hacer predicciones. Si disminuye un organismo, quienes se alimentan de él suelen tener menos alimento, y aquello de lo que él se alimentaba puede aumentar. Son predicciones probables, no seguras, porque hay muchas relaciones.",
    ],
    vocab=[("trama trófica", "red de cadenas tróficas conectadas"), ("presa", "ser vivo que es comido por otro"), ("depredador", "ser vivo que come a otros animales"), ("alternativa de alimento", "otra fuente de la que alimentarse")],
    worked=[
        ("Leer la trama", F, ["Busco quién come lagartijas: el zorro y el aguilucho.", "Busco quién come conejos: el zorro y el aguilucho."], "El zorro y el aguilucho comen conejos y lagartijas"),
        ("Predecir un cambio", "Si desaparecieran los conejos de la trama de la ficha.", ["Zorros y aguiluchos tendrían menos alimento.", "Tendrían que depender más de las lagartijas."], "Probablemente aumentaría la presión sobre las lagartijas"),
    ],
    mistakes=[("Pensar que si un animal disminuye, todo lo demás desaparece.", "Los efectos dependen de cuántas alternativas haya y de cuántos se alimenten de él.", "Revisa cuántas flechas llegan a cada ser vivo."),
              ("Dar una predicción como si fuera segura.", "En una trama hay muchas relaciones y el resultado es probable, no seguro.", "Usa «es probable que» o «podría».")],
    T=[
        ("abc", "{F} ¿Quiénes comen pasto?", "El conejo y el saltamontes", "La lagartija", "El zorro", "La ficha dice que ambos se alimentan de pasto."),
        ("ab", "{F} ¿Qué come la lagartija?", "Saltamontes", "Conejos", "La lagartija es presa de zorros y aguiluchos y come saltamontes."),
        ("=", "{F} ¿Cuántos seres vivos se alimentan de pasto?", "1+1", "Se suman el conejo y el saltamontes.", " seres vivos"),
        ("abc", "{F} ¿Quién come lagartijas?", "El zorro y el aguilucho", "Solo el conejo", "El pasto", "Esa información está en la ficha."),
        ("ab", "{F} ¿Cuántas fuentes de alimento tiene el zorro?", "Dos: conejos y lagartijas", "Una", "El zorro come conejos y lagartijas."),
        ("abc", "{F} ¿Qué ser vivo está en más cadenas de la trama?", "El pasto, porque dos seres vivos dependen de él", "El aguilucho", "Los hongos solo descomponen", "El pasto es la base de varias cadenas."),
        ("abc", "{F} Si disminuyen los saltamontes, ¿qué ser vivo tendría menos alimento?", "La lagartija", "El conejo", "El pasto", "La lagartija se alimenta de saltamontes."),
        ("=", "{F} Si hay 12 lagartijas y el zorro y el aguilucho se comen 3 cada uno, ¿cuántas quedan?", "12-3-3", "Se restan las lagartijas comidas por cada depredador.", " lagartijas"),
        ("ab", "{F} Si los conejos desaparecieran, ¿qué es más probable?", "Que zorros y aguiluchos coman más lagartijas", "Que no cambie nada", "Quienes comían conejos buscan otra fuente de alimento."),
        ("abc", "{F} Si se retiraran los zorros, ¿qué es probable que le pase al conejo?", "Podría aumentar su número", "Desaparecería", "Se volvería productor", "Tendría un depredador menos que se alimente de él."),
        ("abc", "{F} Una persona dice «si los conejos desaparecen, el aguilucho también, seguro». ¿Qué respuesta es mejor?", "Es probable que le afecte, pero puede comer lagartijas", "Tiene razón, seguro", "El aguilucho es productor", "El aguilucho tiene otra alternativa de alimento, que son las lagartijas."),
        ("abc", "{F} ¿Qué pasaría si el pasto disminuye mucho?", "Conejos y saltamontes tendrían menos alimento y eso afectaría a toda la trama", "Solo cambiarían los hongos", "Nada", "El pasto es la base de la trama."),
        ("ab", "¿Por qué una trama es más real que una cadena?", "Porque muestra que cada ser vivo se relaciona con varios otros", "Porque tiene menos seres vivos", "Representa varias relaciones a la vez."),
    ],
    ctx=("abc", "En un cerro de ejemplo se observa que bajó el número de ratones. Una persona pregunta qué podría pasar con las lechuzas que los comen, sabiendo que también comen insectos. ¿Qué respondes?", "Tendrían menos alimento, pero podrían compensar con insectos", "Desaparecerían de inmediato", "No les afectaría nada", "Hay una alternativa, aunque el efecto es probable, no seguro."),
    sc=[("¿Qué es una trama trófica?", "Una red de cadenas tróficas conectadas", "Muestra que un ser vivo puede estar en varias cadenas."),
        ("¿Qué es un depredador?", "El que se alimenta de otros animales", "El que es comido se llama presa."),
        ("En Ciencias: ¿por qué las predicciones en una trama son probables y no seguras?", "Porque hay muchas relaciones y alternativas", "El resultado depende de varios factores.")],
    op=("Con la trama de la ficha, dibuja las flechas y responde: ¿quién depende de más seres vivos para comer? Luego haz una predicción de qué pasaría si disminuyeran las lagartijas y explícala con la trama.",
        "El zorro y el aguilucho tienen dos fuentes. Si disminuyen las lagartijas, los saltamontes podrían aumentar y zorros y aguiluchos comerían más conejos.",
        ["dibuja bien las flechas", "identifica quién depende de más seres vivos", "predice con «es probable que»"],
        ["un diagrama y dos frases"],
        ["poner las flechas al revés", "decir que todo desaparece"],
        "Pregunta: «¿Qué relación de la trama apoya tu predicción?»."),
    reinforce="Arma una trama con tres cadenas que compartan un productor.",
    extend="Explica por qué una trama con más alternativas de alimento es más estable.",
)

# ============================================================ clase 5
F = ("Ficha 5 (pirámide de energía de ejemplo, valores inventados para practicar). Productores (pasto): 1.000 unidades de energía. "
     "Consumidores primarios (conejos): 100 unidades. Consumidores secundarios (zorros): 10 unidades. "
     "Regla aproximada de ejemplo: en cada paso pasa cerca de una décima parte de la energía; el resto se usa en vivir y sale como calor.")
build(
    O, 5, F,
    use="Hoy comparo cómo fluye la energía, que no se recicla, y cómo circula la materia en un ecosistema.",
    prior=PRIOR + ["Sé leer cadenas y tramas tróficas."],
    explain=[
        "La energía entra al ecosistema desde el Sol y los productores la transforman en energía química guardada en su alimento. Luego pasa a los consumidores, siempre en un solo sentido. En cada paso una parte se usa en moverse, crecer y mantenerse, y sale como calor.",
        "Por eso, a medida que subimos en la cadena, cada nivel recibe menos energía que el anterior. Esto explica que haya menos zorros que conejos y menos conejos que pasto. Si en el primer nivel hay 1.000 unidades, en el segundo hay unas 100, y en el tercero unas 10, en esta pirámide de ejemplo.",
        "La materia, en cambio, circula. Los nutrientes pasan de los productores a los consumidores, vuelven al suelo con los descomponedores y los productores los usan otra vez. Se resume así: la energía fluye y la materia se recicla.",
    ],
    vocab=[("flujo de energía", "paso de la energía de un nivel al siguiente, en un solo sentido"), ("reciclaje de materia", "paso de la materia de los restos otra vez a las plantas"), ("pirámide de energía", "diagrama que muestra cuánta energía hay en cada nivel"), ("nutrientes", "sustancias que usan los seres vivos para crecer")],
    worked=[
        ("Calcular energía por nivel", F, ["Productores: 1.000.", "Se pasa cerca de una décima parte a los conejos: 1.000 dividido en 10.", "De ellos, otra décima parte a los zorros."], "Conejos: 100 unidades. Zorros: 10 unidades"),
        ("Dónde va el resto", "De las 1.000 unidades de los productores, solo 100 llegan a los conejos.", ["1.000 menos 100.", "Esa parte se usa en vivir y sale como calor."], "900 unidades no pasan al siguiente nivel"),
    ],
    mistakes=[("Decir que la energía vuelve de los descomponedores a los productores.", "La energía fluye en un solo sentido y se pierde como calor; lo que vuelve es la materia.", "Recuerda: la energía fluye, la materia se recicla."),
              ("Creer que cada nivel recibe tanta energía como el anterior.", "En cada paso se pierde gran parte como calor.", "Compara los valores de la pirámide nivel por nivel.")],
    T=[
        ("abc", "{F} ¿Cuántas unidades de energía tienen los conejos?", "100", "1.000", "10", "Los conejos son consumidores primarios con 100 unidades."),
        ("ab", "¿De dónde viene la energía que entra al ecosistema?", "Del Sol", "De los descomponedores", "Los productores la transforman a partir de la luz del Sol."),
        ("=", "{F} Si de las 100 unidades de los conejos pasaran solo 20 al siguiente nivel, ¿cuántas unidades no pasarían?", "100-20", "Se resta lo que pasa del total que había.", " unidades"),
        ("abc", "{F} ¿Cuántas unidades de energía tienen los zorros?", "10", "100", "1", "Los zorros reciben una décima parte de lo que tienen los conejos."),
        ("ab", "¿Por qué hay menos zorros que conejos en el ecosistema de ejemplo?", "Porque cada nivel recibe menos energía que el anterior", "Porque los zorros son más pequeños", "La energía disponible disminuye al subir de nivel."),
        ("abc", "{F} ¿Cuántas unidades se pierden entre los conejos y los zorros?", "90", "10", "100", "Se restan los 10 que llegan a los zorros a los 100 de los conejos y quedan 90."),
        ("=", "{F} Si los productores tuvieran 2.000 unidades y pasara una décima parte, ¿cuántas recibirían los consumidores primarios?", "2000/10", "Una décima parte se obtiene dividiendo entre diez.", " unidades"),
        ("ab", "¿Qué circula en el ecosistema, volviendo a las plantas?", "La materia, en forma de nutrientes", "La energía", "Los descomponedores devuelven nutrientes al suelo."),
        ("abc", "{F} Una persona dice «la energía de los zorros vuelve al pasto». ¿Qué corrección es correcta?", "La energía no vuelve: se pierde como calor; vuelven los nutrientes", "Tiene razón", "El zorro es productor", "La energía fluye en un solo sentido."),
        ("abc", "¿Qué sale de los seres vivos como calor?", "Parte de la energía que usan para moverse y mantenerse", "Los nutrientes", "El pasto", "Esa parte ya no puede pasar al siguiente nivel."),
        ("abc", "{F} Si hay 1.000 unidades en los productores y solo 10 en el tercer nivel, ¿qué fracción de la energía de los productores llega a ese nivel?", "1 de cada 100 unidades", "1 de cada 10 unidades", "La mitad de las unidades", "10 de 1.000 equivalen a 1 de cada 100."),
        ("abc", "Un pastizal pierde la mitad de sus hierbas por una sequía. ¿Qué es más probable que ocurra con los consumidores?", "Habrá menos energía disponible y disminuirán", "Aumentarán", "No cambiarán", "Menos base de energía implica menos consumidores."),
        ("ab", "Resume el flujo en un ecosistema:", "La energía fluye en un sentido y la materia se recicla", "La energía se recicla y la materia fluye", "La energía se pierde como calor; la materia vuelve con los descomponedores."),
    ],
    ctx=("abc", "En una charla sobre huertas comunitarias, una persona dice que el compost «devuelve vida a la tierra». ¿Cómo lo explicas con lo aprendido?", "Los descomponedores devuelven los nutrientes de los restos, que las plantas vuelven a usar", "El compost entrega energía del Sol", "El compost fabrica agua", "La materia se recicla; la energía no."),
    sc=[("En Ciencias: ¿qué fluye y qué se recicla en un ecosistema?", "La energía fluye y la materia se recicla", "La energía se pierde como calor y la materia vuelve con descomponedores."),
        ("¿Por qué hay menos animales en los niveles altos?", "Porque llega menos energía a cada nivel", "Se pierde parte en cada paso."),
        ("¿Quién devuelve nutrientes al suelo?", "Los descomponedores", "Hongos y bacterias de los restos.")],
    op=("Con una pirámide de ejemplo de 3.000 unidades de energía en los productores, calcula cuántas llegarían a los consumidores primarios y a los secundarios usando la regla de una décima parte. Explica en una frase por qué hay menos consumidores secundarios.",
        "Primarios: 300 unidades. Secundarios: 30. Hay menos consumidores secundarios porque en cada paso se pierde gran parte de la energía como calor.",
        ["calcula 300 y 30", "explica la pérdida de energía", "distingue energía y materia"],
        ["dos cálculos y una frase"],
        ["dividir mal", "decir que la energía se recicla"],
        "Pregunta: «¿Qué fluye y qué circula?»."),
    reinforce="Explica con tus palabras la diferencia entre «fluye» y «se recicla».",
    extend="Explica por qué la energía de una cadena necesita al Sol de forma permanente.",
)

# ============================================================ clase 6
F = ("Ficha 6 (diagrama de ejemplo, descrito). Laguna: el Sol entrega luz a las algas. Algas → insectos acuáticos → ranas → garzas. "
     "Algas → peces pequeños → garzas. Los hongos y bacterias del fondo descomponen restos de todos y devuelven nutrientes al agua. "
     "Las flechas van de lo comido a quien lo come.")
build(
    O, 6, F,
    use="Hoy reviso lo aprendido: describo los flujos de un diagrama completo y pienso cómo cuidar el ecosistema.",
    prior=PRIOR + ["Conozco cadenas, tramas y el flujo de energía y materia."],
    explain=[
        "Para describir los flujos de un diagrama, sigue estos pasos. Primero ubica la entrada de energía: el Sol. Segundo, identifica el productor. Tercero, sigue las flechas por los consumidores. Cuarto, señala dónde actúan los descomponedores y qué devuelven.",
        "En una descripción completa usa las palabras «energía» y «materia». Di que la energía entra por el Sol, pasa de nivel en nivel y se va perdiendo como calor, y que la materia circula: los nutrientes vuelven al agua o al suelo gracias a los descomponedores.",
        "Cuando algo daña al productor, o a los descomponedores, el efecto se propaga por toda la trama. Por eso la prevención, que busca evitar el daño, y la mitigación, que busca reducirlo cuando ya ocurrió, ayudan a cuidar los ecosistemas. Lo veremos en el siguiente desempeño.",
    ],
    vocab=[("describir un diagrama", "contar con palabras los pasos y las relaciones que muestra"), ("propagarse", "extenderse de un lugar a otro"), ("prevención", "acciones para evitar un daño"), ("mitigación", "acciones para reducir un daño que ya ocurrió")],
    worked=[
        ("Describir el flujo", F, ["Entrada: luz del Sol a las algas, que son productoras.", "Camino 1: algas, insectos, ranas, garzas. Camino 2: algas, peces, garzas.", "Descomponedores devuelven nutrientes al agua."], "La energía entra por el Sol, pasa por dos caminos hasta la garza y la materia vuelve al agua por los descomponedores"),
        ("Predecir un efecto", "Un contaminante de ejemplo hace que mueran muchas algas.", ["Menos algas, menos alimento para insectos y peces.", "Luego les llega menos alimento a ranas y garzas."], "El daño se propaga: disminuirían insectos, peces, ranas y garzas"),
    ],
    mistakes=[("Describir solo un camino de la trama.", "El diagrama tiene más de un camino y la garza se alimenta de dos.", "Sigue todas las flechas antes de describir."),
              ("Olvidar a los descomponedores en la descripción.", "Sin ellos no se explica cómo vuelve la materia al ecosistema.", "Agrega siempre el cierre del ciclo de la materia.")],
    T=[
        ("abc", "{F} ¿Cuál es el productor?", "Las algas", "Las ranas", "La garza", "Las algas fabrican su alimento con luz."),
        ("ab", "{F} ¿Qué ser vivo se alimenta por dos caminos?", "La garza", "Las algas", "La garza come ranas y peces pequeños."),
        ("abc", "{F} ¿Cuántos caminos distintos llevan desde las algas hasta la garza?", "2", "1", "3", "Uno pasa por insectos y ranas, y el otro pasa por los peces pequeños."),
        ("abc", "{F} ¿Qué entra al ecosistema desde fuera?", "La energía del Sol", "Las garzas", "Los hongos", "El Sol es la fuente de energía."),
        ("ab", "{F} ¿Qué devuelven los descomponedores al agua?", "Nutrientes", "Luz", "Los nutrientes de los restos vuelven al agua."),
        ("abc", "{F} Si mueren las ranas, ¿qué es probable que le pase a las garzas?", "Se alimentarían más de peces", "No cambiaría nada", "Desaparecerían seguro", "Las garzas tienen otra fuente de alimento, que son los peces pequeños."),
        ("=", "{F} En la laguna hay 20 insectos y las ranas se comen 4. ¿Cuántos insectos quedan?", "20-4", "Se resta lo comido del total.", " insectos"),
        ("abc", "{F} Si se secara la laguna, ¿qué elemento abiótico faltaría?", "El agua", "El Sol", "El aire", "Sin agua no se sostienen las algas ni el resto."),
        ("ab", "¿Qué diferencia hay entre prevención y mitigación?", "Prevenir evita el daño; mitigar reduce un daño que ya ocurrió", "Son lo mismo", "La prevención va antes y la mitigación después."),
        ("abc", "{F} Un grupo sugiere «echar basura al agua no afecta a nadie porque la laguna es grande». ¿Qué respuesta es mejor?", "La basura puede dañar a las algas y el efecto se propaga por la trama", "Tiene razón", "La basura produce más garzas", "El daño al productor afecta a todos los niveles."),
        ("abc", "{F} ¿Qué medida de prevención es coherente?", "No botar basura ni desechos en la laguna", "Pescar todos los peces", "Secar la laguna", "Evita que el daño ocurra, porque la basura no llega a la laguna."),
        ("abc", "Un grupo describe el diagrama diciendo solo «hay algas y garzas». ¿Qué le falta?", "Los demás seres vivos, los caminos, el Sol y los descomponedores", "Nada", "Más colores", "Una descripción completa incluye el flujo de energía y de materia."),
        ("ab", "¿Qué hace más completa una descripción de flujos?", "Usar las palabras energía y materia y nombrar la entrada, los caminos y el reciclaje", "Dibujar flechas bonitas", "La descripción debe explicar cómo fluyen las dos cosas."),
    ],
    ctx=("abc", "En un taller vecinal sobre un humedal de ejemplo, una persona dice que si bajan los insectos solo se afectarán las ranas. ¿Qué corriges con el diagrama de la ficha?", "También se afectarían las garzas, que comen ranas, y los peces serían más importantes para ellas", "Solo se afectan las ranas", "No pasa nada", "El efecto sube por la trama."),
    sc=[("En Ciencias: ¿qué significa que la energía fluye?", "Pasa en un solo sentido y se va perdiendo como calor", "La energía no vuelve a los productores, solo se pierde como calor."),
        ("¿Qué hacen los descomponedores en el diagrama?", "Devuelven los nutrientes de los restos al agua o al suelo", "Así la materia de los restos se recicla y vuelve a los productores."),
        ("Frente al daño de un ecosistema, ¿qué diferencia hay entre prevenir y mitigar?", "Prevenir evita el daño; mitigar lo reduce cuando ya ocurrió", "Son dos formas de cuidar el ecosistema.")],
    op=("Con el diagrama de la laguna de la ficha, escribe una descripción de cuatro líneas: la entrada de energía, los dos caminos hasta la garza, el papel de los descomponedores y una predicción de qué pasaría si se contaminara el agua. Añade una medida de prevención.",
        "El Sol da energía a las algas. Un camino va por insectos y ranas, otro por peces. Los descomponedores devuelven nutrientes. Si se contamina, las algas disminuirían y el daño subiría. Prevención: no botar basura.",
        ["nombra la entrada de energía", "describe los dos caminos y los descomponedores", "propone una medida de prevención"],
        ["cuatro líneas escritas"],
        ["describir un solo camino", "olvidar a los descomponedores"],
        "Pregunta: «¿Qué fluye y qué se recicla en tu descripción?»."),
    reinforce="Dibuja un diagrama con cuatro seres vivos y el Sol, y descríbelo en voz alta.",
    extend="Explica por qué la contaminación del agua puede afectar a animales que no viven en el agua.",
)
