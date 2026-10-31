"""Material del estudiante de 5.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (consecuencias de la conquista) y OA 04 (efectos sobre los pueblos indígenas)."""
from __future__ import annotations

from hi5_lib import build

OA3 = "HI05 OA 03"
OA4 = "HI05 OA 04"

# ================================================================ OA 03 · CONSECUENCIAS EN EUROPA Y AMÉRICA
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (intercambio entre continentes, hecha para este cuaderno). Desde 1492 empezaron a viajar productos, animales, personas y enfermedades entre Europa, América y África. "
     "De América hacia Europa viajaron la papa, el maíz, el tomate, el cacao y el poroto. De Europa hacia América viajaron el trigo, la vid, la caña de azúcar, el caballo, la vaca, la oveja, el cerdo y la gallina. "
     "Desde América se enviaban a España, en flotas que cruzaban el Atlántico, la plata y el oro. Personas africanas fueron llevadas a la fuerza a América para trabajar como esclavas.")
build(
    OA3, 1, F,
    use="Aprenderé qué viajó entre Europa y América después de 1492 y hacia dónde. Sirve para ubicar el intercambio entre continentes en el espacio y en el tiempo.",
    prior=["Sé que Colón llegó a América en 1492.", "Sé que el Atlántico separa Europa y América.", "Sé reconocer los continentes en un mapa."],
    explain=[
        "La conquista de América produjo grandes consecuencias, es decir, cambios que vinieron después. Una de ellas fue el intercambio entre continentes: desde 1492 empezaron a viajar productos, animales, personas e incluso enfermedades entre Europa, América y África.",
        "De América hacia Europa viajaron alimentos como la papa, el maíz, el tomate, el cacao y el poroto. De Europa hacia América llegaron el trigo, la vid, la caña de azúcar y animales como el caballo, la vaca, la oveja, el cerdo y la gallina. Antes de 1492, en América no había caballos ni vacas.",
        "También viajaron metales. En flotas que cruzaban el Atlántico, la plata y el oro de América se enviaban a España. Además, personas africanas fueron llevadas a la fuerza a América como esclavas. Para ubicar un cambio histórico, siempre preguntamos desde dónde, hacia dónde y desde cuándo.",
    ],
    vocab=[("consecuencia", "cambio que ocurre después de un hecho y por causa de él"), ("intercambio", "paso de productos, ideas o personas de un lugar a otro y de vuelta"), ("flota", "grupo de naves que viajan juntas"), ("esclavo", "persona obligada a trabajar sin libertad ni pago"), ("metal precioso", "metal muy valorado, como el oro y la plata")],
    worked=[
        ("Ubicar un producto", "{F} ¿Desde dónde y hacia dónde viajó el tomate?", ["Busco el tomate en la ficha.", "Está entre los productos que viajaron de América hacia Europa."], "Desde América hacia Europa"),
        ("Calcular un tiempo", "{F} Si el intercambio empezó en 1492, ¿cuántos años habían pasado en 1592?", ["Busco el año de inicio: 1492.", "Resto: 1592 − 1492 = 100."], "100 años"),
    ],
    mistakes=[("Decir que el trigo ya existía en América antes de 1492.", "Se piensa que todo siempre estuvo en todas partes.", "La ficha dice que el trigo viajó de Europa a América."),
              ("Creer que el intercambio fue solo de productos.", "Se olvidan personas y enfermedades.", "Incluye también metales, animales, personas y enfermedades.")],
    T=[
        ("{F} ¿Desde qué continente viajó la papa hacia Europa?", "desde América", "La ficha lo dice."),
        ("{F} ¿En qué año empezó el intercambio entre continentes?", "en 1492", "La ficha dice «desde 1492»."),
        ("{F} ¿Qué metales se enviaban a España desde América?", "plata y oro", "La ficha los nombra."),
        ("{F} ¿Cuál de estos animales llegó desde Europa a América: el caballo o el cacao?", "el caballo", "El cacao es un producto vegetal de América."),
        ("{F} ¿Qué océano cruzaban las flotas?", "el Atlántico", "La ficha lo indica."),
        ("{F} Clasifica: a) maíz; b) vaca. ¿Cuál viajó de América a Europa y cuál de Europa a América?", "a: de América a Europa; b: de Europa a América", "El maíz es del primer grupo y la vaca del segundo."),
        ("=", "{F} El intercambio empezó en 1492. ¿Cuántos años pasaron hasta 1692?", "1692-1492", "Se resta el año de inicio al final.", " años"),
        ("{F} Un mapa muestra una flecha desde España hacia América con una vaca dibujada. ¿La flecha está bien dibujada?", "Sí", "La vaca viajó de Europa a América."),
        ("{F} Un mapa muestra una flecha desde América hacia Europa con trigo dibujado. ¿Es correcto?", "No, el trigo viajó de Europa a América", "La flecha debería ir en el otro sentido."),
        ("{F} Laura dice: «Antes de 1492 había caballos en América». ¿Qué dato de la ficha la contradice?", "el caballo viajó de Europa a América", "La ficha lo incluye entre los animales llegados de Europa."),
        ("{F} Nico dice: «El intercambio solo fue de comida». Nombra otras dos cosas que viajaron.", "metales como plata y oro, y personas africanas llevadas a América", "La ficha menciona más tipos de intercambio."),
        ("{F} ¿Qué productos de la ficha, de América, se usan hoy en una ensalada: a) papa; b) trigo; c) tomate? Elige los de origen americano.", "a y c", "La papa y el tomate viajaron de América a Europa."),
        ("{F} Ordena por origen: grupo 1 «de América»; grupo 2 «de Europa». Poroto, cerdo, cacao, oveja.", "grupo 1: poroto y cacao; grupo 2: cerdo y oveja", "Los dos primeros son vegetales americanos y los otros dos animales europeos."),
    ],
    ctx=("En una feria escolar ves un mapa con tres flechas: «papa», «caballo» y «plata». ¿Qué flecha va de Europa a América y cuáles de América a Europa?", "el caballo va de Europa a América; la papa y la plata van de América a Europa", "Así lo indica la ficha."),
    sc=[("¿Desde cuándo empezó el intercambio entre continentes?", "desde 1492", "La ficha lo dice."),
        ("{F} Nombra un alimento que viajó de América a Europa.", "por ejemplo la papa, el maíz, el tomate, el cacao o el poroto", "Son los que la ficha nombra."),
        ("{F} Nombra un animal que viajó de Europa a América.", "por ejemplo el caballo, la vaca, la oveja, el cerdo o la gallina", "Son los que la ficha nombra.")],
    op=("Dibuja un mapa simple con dos continentes: Europa a la izquierda y América a la derecha, con el mar en medio. Dibuja una flecha en cada sentido y escribe sobre cada una tres productos de la ficha. Escribe el año «1492» como inicio. {F}",
        "Flecha de América a Europa: papa, tomate, cacao. Flecha de Europa a América: trigo, caballo, vaca. Año 1492.",
        ["dos flechas con sentido correcto", "tres productos en cada una", "año de inicio"], ["mapa simple"], ["poner una flecha en el sentido equivocado", "mezclar productos de ambos grupos"],
        "Pide que explique cómo sabe que un producto es de América o de Europa."),
    reinforce="Di en voz alta tres productos que fueron de América a Europa y tres que fueron de Europa a América.",
    extend="Escribe cinco alimentos que comes a la semana y averigua con una persona de tu casa si algún ingrediente es de origen americano, usando solo lo que la ficha dice.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre las consecuencias (hechas para este cuaderno, a partir de hechos conocidos). Fuente A: un registro de carga de una flota del siglo XVI, anotado por un funcionario de la Casa de Contratación de Sevilla, la oficina que controlaba el comercio con América; enumera plata, cacao y azúcar. "
     "Fuente B: un grabado europeo del siglo XVI que muestra trabajadores en una mina de plata de Potosí. "
     "Fuente C: el texto de un cronista del siglo XVI que cuenta que muchos indígenas murieron por enfermedades traídas por los europeos, como la viruela. "
     "Fuente D: una lista de palabras de origen indígena que usamos en español, como tomate, chocolate, papa, maíz y canoa, preparada por un lingüista actual.")
build(
    OA3, 2, F,
    use="Aprenderé a preguntar quién hizo una fuente sobre las consecuencias de la conquista y qué ámbito muestra. Sirve para distinguir fuentes de la época y fuentes posteriores.",
    prior=["Sé qué es la procedencia de una fuente.", "Sé qué viajó entre Europa y América."],
    explain=[
        "Las consecuencias de la conquista se estudian en distintos ámbitos: el económico (riquezas y comercio), el demográfico (cuánta gente vivía), el cultural (lengua, creencias, alimentos) y el social. Cada fuente suele iluminar un solo ámbito.",
        "Una fuente primaria es de la época. El registro de carga muestra un ámbito económico: qué productos se enviaban. El grabado de la mina de Potosí muestra el trabajo en las minas de plata. El texto del cronista cuenta las muertes por enfermedades, un ámbito demográfico. La lista de palabras indígenas es una fuente secundaria, hecha después por un lingüista, y muestra un cambio cultural: palabras que hoy usamos.",
        "Antes de usar una fuente preguntamos quién la hizo, cuándo y para qué, y qué ámbito muestra. Un funcionario que anota carga no cuenta el sufrimiento de los trabajadores, y un cronista puede exagerar o calcular mal. Por eso combinamos fuentes distintas.",
    ],
    vocab=[("ámbito", "área de la vida, como la economía, la cultura o la población"), ("lingüista", "persona que estudia las lenguas"), ("Potosí", "ciudad de los Andes con una gran mina de plata en la época colonial"), ("viruela", "enfermedad contagiosa grave llevada desde Europa"), ("registro", "lista oficial donde se anotan datos")],
    worked=[
        ("Identificar el ámbito", "{F} ¿Qué ámbito muestra la fuente A?", ["Leo qué enumera: plata, cacao y azúcar.", "Son productos que se comerciaban."], "El ámbito económico"),
        ("Distinguir tipos de fuente", "{F} ¿La fuente D es primaria o secundaria?", ["La preparó un lingüista actual.", "No es de la época de la conquista."], "Secundaria"),
    ],
    mistakes=[("Creer que una lista de carga muestra cómo vivían las personas.", "Se pide a la fuente más de lo que dice.", "Usa cada fuente solo para el ámbito que muestra."),
              ("Pensar que una fuente actual es de la época de la conquista.", "No se mira la fecha.", "Pregunta cuándo se hizo.")],
    T=[
        ("{F} ¿Quién anotó el registro de carga de la fuente A?", "un funcionario de la Casa de Contratación de Sevilla", "La ficha lo dice."),
        ("{F} ¿Qué se extraía en la mina de la fuente B?", "plata", "La ficha dice «mina de plata de Potosí»."),
        ("{F} ¿Qué enfermedad nombra la fuente C?", "la viruela", "La ficha la nombra."),
        ("{F} ¿Qué fuente es la más reciente?", "la fuente D", "La preparó un lingüista actual."),
        ("{F} ¿Qué cambio cultural muestra la fuente D?", "palabras indígenas que hoy usamos en español", "La lista muestra esas palabras."),
        ("{F} ¿Qué fuente nos habla de muertes por enfermedades?", "la fuente C", "Es el texto del cronista."),
        ("{F} Quieres saber qué productos se enviaban a España. ¿Qué fuente usas?", "la fuente A", "Es el registro de carga."),
        ("{F} Quieres saber cómo se trabajaba en una mina de plata. ¿Qué fuente usas?", "la fuente B", "El grabado muestra trabajadores en la mina."),
        ("{F} Une cada fuente con su ámbito: 1) fuente A; 2) fuente D. a) cultural; b) económico.", "1 con b; 2 con a", "A muestra comercio y D palabras que usamos."),
        ("{F} Luis dice: «El registro de carga prueba que a todos los habitantes de América les fue bien». ¿Por qué no es válido?", "porque solo enumera productos y no cuenta cómo vivían las personas", "La fuente muestra un solo ámbito."),
        ("{F} Ana dice: «El cronista cuenta con exactitud cuántos murieron». ¿Qué cuidado hay que tener?", "revisar quién lo escribió y para qué, porque pudo no tener cifras exactas", "Un cronista puede calcular mal o exagerar."),
        ("{F} Elige la pregunta que ninguna fuente responde. A) ¿Qué productos se enviaban a España? B) ¿Cuántas personas vivían en Potosí en 1650?", "B", "Ninguna fuente da esa cifra."),
        ("{F} Para armar una explicación de cómo cambió la población y qué productos se enviaban a España, ¿qué dos fuentes unes?", "la fuente C y la fuente A", "C muestra la población y A los productos enviados."),
    ],
    ctx=("Un cartel de museo dice: «Grabado, siglo XVI, mina de Potosí». ¿Qué datos de procedencia entrega y cuál falta?", "entrega época y lugar; falta quién lo hizo y para qué", "La procedencia exige autor, fecha y propósito."),
    sc=[("¿Qué es una fuente secundaria?", "un texto hecho después, a partir de otras fuentes", "Se distingue de la fuente primaria, de la época."),
        ("{F} ¿Qué muestra la fuente D de la conquista?", "un cambio cultural: palabras indígenas en el español", "La lista recoge esas palabras."),
        ("Nombra dos ámbitos en que se estudian las consecuencias.", "por ejemplo económico y cultural", "Son ámbitos de la vida de las sociedades.")],
    op=("Haz una tabla con las columnas «fuente», «de qué época es», «ámbito que muestra» y «lo que no dice». Completa una fila para la fuente A y otra para la fuente C. {F}",
        "A: siglo XVI; económico; no dice cómo vivían las personas. C: siglo XVI; demográfico; no da cifras exactas.",
        ["dos filas completas", "ámbito correcto", "un límite por fuente"], ["tabla de cuatro columnas"], ["confundir ámbitos", "no señalar límites"],
        "Pregunta qué fuente nueva te gustaría tener para completar el cuadro."),
    reinforce="Nombra las cuatro fuentes y el ámbito que muestra cada una.",
    extend="Escribe tres palabras de origen indígena que uses en tu casa y qué significan.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (cadena de consecuencias, hecha para este cuaderno). Los europeos llevaron a América enfermedades como la viruela y el sarampión, que los pueblos indígenas no conocían. Muchas personas enfermaron y murieron. "
     "También hubo guerras y trabajos forzados. Con menos gente, faltaron trabajadores en minas y haciendas. Los españoles trajeron personas africanas esclavizadas para suplir esa falta. "
     "Al mismo tiempo, la plata de América llegaba a España en grandes cantidades y aumentaba el comercio con otros lugares. Desde América llegaron a Europa alimentos como la papa y el maíz, que hicieron más variada la alimentación.")
build(
    OA3, 3, F,
    use="Aprenderé a ordenar causas y consecuencias de la conquista en distintos ámbitos y a nombrar a los actores. Sirve para explicar cómo un hecho llevó a otro.",
    prior=["Sé qué es una causa y una consecuencia.", "Sé qué productos viajaron entre continentes."],
    explain=[
        "Las consecuencias de la conquista se pueden ordenar como una cadena. Primero, los europeos llevaron enfermedades como la viruela y el sarampión, que los pueblos indígenas no conocían. Muchas personas murieron. A eso se sumaron guerras y trabajos forzados.",
        "Con menos habitantes, faltaron trabajadores en minas y haciendas. Los españoles trajeron entonces personas africanas esclavizadas, que fueron obligadas a trabajar. Esta cadena muestra consecuencias demográficas (cuánta gente) y sociales (quién trabajaba y en qué condiciones).",
        "En otro ámbito, el económico, la plata de América llegaba a España en grandes cantidades y aumentaba el comercio con otros lugares. En el ámbito de la alimentación, la papa y el maíz hicieron más variada la comida europea. Las consecuencias no fueron iguales para todos: unos ganaron riquezas y otros perdieron libertad, tierras o la vida.",
    ],
    vocab=[("demográfico", "relacionado con la cantidad de personas que viven en un lugar"), ("hacienda", "gran propiedad agrícola de la época colonial"), ("esclavizado", "obligado a trabajar sin libertad ni pago"), ("trabajo forzado", "trabajo hecho por obligación, sin elegirlo"), ("sarampión", "enfermedad contagiosa que llegó desde Europa")],
    worked=[
        ("Ordenar una cadena", "{F} Ordena: a) faltaron trabajadores en minas y haciendas; b) llegaron enfermedades europeas; c) muchas personas murieron.", ["Primero llegan las enfermedades.", "Luego mueren personas y después faltan trabajadores."], "b, c, a"),
        ("Identificar el ámbito", "{F} La papa y el maíz hicieron más variada la comida europea. ¿Qué ámbito es?", ["Habla de alimentos que se comen.", "Eso se relaciona con la alimentación y la cultura."], "La alimentación, un ámbito cultural"),
    ],
    mistakes=[("Decir que la conquista solo tuvo consecuencias positivas.", "Se mira solo la plata y los alimentos.", "Incluye las muertes, el trabajo forzado y la esclavitud."),
              ("Creer que las consecuencias fueron iguales para todos.", "No se pregunta quién ganó y quién perdió.", "Pregunta qué cambió para cada grupo.")],
    T=[
        ("{F} ¿Qué enfermedades llevaron los europeos a América?", "la viruela y el sarampión", "La ficha las nombra."),
        ("{F} ¿Qué faltó en las minas y haciendas al disminuir la población?", "trabajadores", "La ficha lo dice."),
        ("{F} ¿Qué llegaba a España en grandes cantidades desde América?", "plata", "La ficha lo indica."),
        ("{F} ¿Qué consecuencia tuvo la llegada de enfermedades: aumentó o disminuyó la población indígena?", "disminuyó", "Muchas personas murieron."),
        ("{F} ¿Quiénes fueron traídos a América para suplir la falta de trabajadores?", "personas africanas esclavizadas", "La ficha lo dice."),
        ("{F} ¿Qué alimentos americanos hicieron más variada la comida europea?", "la papa y el maíz", "La ficha los nombra."),
        ("=", "{F} Ejemplo inventado: un pueblo tenía 1.000 habitantes y, tras una epidemia, murieron 600. ¿Cuántas personas quedaron?", "1000-600", "Se resta los que murieron a los que había.", " personas"),
        ("{F} ¿Qué ámbito muestra el aumento del comercio por la plata: económico o cultural?", "económico", "Habla de riqueza y comercio."),
        ("{F} Ordena la cadena: a) se trajeron africanos esclavizados; b) murieron muchos indígenas; c) llegaron enfermedades.", "c, b, a", "Cada hecho lleva al siguiente."),
        ("{F} Marta dice: «La conquista benefició a todos por igual». Da dos datos de la ficha que la contradicen.", "murieron muchas personas y se trajeron africanos como esclavos", "Hubo pérdidas graves para algunos."),
        ("{F} Pablo dice: «La falta de trabajadores no tuvo relación con las enfermedades». Corrígelo.", "las enfermedades mataron a muchas personas y por eso faltaron trabajadores", "La ficha enlaza ambos hechos."),
        ("{F} Clasifica como «demográfica» o «económica»: a) murieron muchas personas; b) llegó mucha plata a España.", "a: demográfica; b: económica", "Una habla de población y la otra de riqueza."),
        ("{F} ¿Qué grupo perdió libertad como consecuencia: los africanos traídos como esclavos o los comerciantes de plata?", "los africanos traídos como esclavos", "Fueron obligados a trabajar sin libertad."),
    ],
    ctx=("Un afiche escolar dice: «La conquista solo trajo cosas buenas a Europa». Usa un dato de la ficha para decir qué le falta mostrar sobre América.", "en América murieron muchas personas por enfermedades y hubo trabajos forzados", "El afiche muestra solo un lado de las consecuencias."),
    sc=[("{F} ¿Cuál fue la causa de que faltaran trabajadores?", "la muerte de muchas personas por enfermedades, guerras y trabajos forzados", "La ficha explica la cadena."),
        ("¿Qué ámbitos de consecuencias vimos?", "por ejemplo demográfico, económico, cultural y social", "Cada ámbito muestra un tipo de cambio."),
        ("¿Por qué las consecuencias no fueron iguales para todos?", "porque unos ganaron riquezas y otros perdieron libertad, tierras o la vida", "Cada grupo vivió un efecto distinto.")],
    op=("Dibuja una cadena de cuatro recuadros con flechas, que empiece con «llegan enfermedades europeas». Agrega tres consecuencias de la ficha en orden. Al lado dibuja otra flecha corta para una consecuencia en Europa. {F}",
        "Enfermedades → mueren personas → faltan trabajadores → se trae africanos esclavizados. Al lado: llega plata a España.",
        ["cadena en orden", "cuatro recuadros", "una consecuencia en Europa"], ["cadena dibujada"], ["cambiar el orden causa-efecto", "no incluir a Europa"],
        "Pregunta qué grupo tuvo consecuencias más duras y pide un dato."),
    reinforce="Cuenta en voz alta la cadena de consecuencias de las enfermedades europeas.",
    extend="Escribe una consecuencia de la conquista que haya sido buena para Europa y no para América, y por qué.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (comparación, hecha para este cuaderno). Población: en América, muchos pueblos perdieron una gran parte de sus habitantes por enfermedades, guerras y trabajos forzados; en Europa no hubo esa pérdida a causa de la conquista. "
     "Economía: en América se extraían plata y oro, se instalaron haciendas y se llevó ganado; en Europa llegaron grandes cantidades de plata y creció el comercio. "
     "Alimentación: en Europa se agregaron la papa, el maíz, el tomate y el cacao; en América se agregaron el trigo, la carne de vaca, de cerdo y de gallina, y la caña de azúcar. "
     "Religión y lengua: en América se difundió el cristianismo y el castellano; en Europa aumentó el interés por conocer tierras y pueblos lejanos.")
build(
    OA3, 4, F,
    use="Aprenderé a comparar las consecuencias de la conquista en Europa y en América por ámbitos. Sirve para ver quién ganó, quién perdió y qué cambió en cada lado.",
    prior=["Sé qué viajó entre continentes.", "Sé nombrar ámbitos: población, economía, alimentación, cultura."],
    explain=[
        "Comparar consecuencias significa mirar el mismo ámbito en dos lugares y notar parecidos y diferencias. Los ámbitos de la ficha son: población, economía, alimentación, religión y lengua. Cada uno cambió en Europa y en América, pero de manera distinta.",
        "En población, América perdió una gran parte de sus habitantes por enfermedades, guerras y trabajos forzados, y Europa no tuvo esa pérdida por la conquista. En economía, a América se la usó para extraer plata y oro, y a Europa llegó plata y creció su comercio. En alimentación hubo ganancias para ambos: Europa recibió papa, maíz, tomate y cacao; América recibió trigo, ganado y caña de azúcar.",
        "En religión y lengua, en América se difundieron el cristianismo y el castellano. En Europa aumentó el interés por conocer tierras y pueblos lejanos. Entonces, la conquista cambió ambos continentes, pero con más costo humano para América. Una buena comparación usa un mismo criterio para los dos lados.",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("difundir", "extender algo a más personas o lugares"), ("castellano", "idioma de Castilla, hoy llamado español"), ("ganado", "animales de criadero, como vacas y ovejas"), ("costo humano", "daño que sufren las personas, como muertes o pérdida de libertad")],
    worked=[
        ("Comparar con un criterio", "{F} Compara la población de América y de Europa.", ["En América muchos pueblos perdieron gran parte de sus habitantes.", "En Europa no hubo esa pérdida por la conquista."], "América perdió población; Europa no"),
        ("Buscar un parecido", "{F} ¿En qué criterio ganaron ambos continentes?", ["Reviso los cinco criterios.", "En alimentación, Europa y América recibieron productos nuevos."], "En alimentación"),
    ],
    mistakes=[("Decir que Europa y América cambiaron de la misma manera.", "Se mira solo la existencia de cambios.", "Compara cada ámbito: la población no cambió igual."),
              ("Olvidar un lado de la comparación.", "Se habla solo de Europa o solo de América.", "Cada criterio debe tener el dato de los dos continentes.")],
    T=[
        ("{F} ¿Qué continente perdió gran parte de su población?", "América", "La ficha lo dice."),
        ("{F} ¿Qué llegó en grandes cantidades a Europa?", "plata", "La ficha lo dice en el criterio economía."),
        ("{F} ¿Qué idioma se difundió en América?", "el castellano", "Se difundió junto con el cristianismo."),
        ("{F} ¿Qué cereal llegó a América desde Europa?", "el trigo", "La ficha lo menciona en alimentación."),
        ("{F} ¿Qué alimento americano se agregó a la dieta de Europa: el cacao o la caña de azúcar?", "el cacao", "La caña de azúcar llegó a América."),
        ("{F} ¿En qué ámbito el cambio fue de ganancia para ambos continentes?", "en alimentación", "Ambos recibieron productos nuevos."),
        ("{F} ¿Qué se instaló en América para producir en el campo?", "haciendas", "La ficha lo menciona en economía."),
        ("{F} Elige la comparación correcta de población. A) América perdió habitantes y Europa no por la conquista. B) Europa perdió habitantes y América no.", "A", "La ficha lo dice así."),
        ("{F} Completa con «Europa» o «América»: a) aumentó el interés por tierras lejanas; b) se difundió el cristianismo.", "a: Europa; b: América", "Así lo muestra la ficha."),
        ("{F} Rosa dice: «Europa y América pasaron por lo mismo». Da un criterio donde fue distinto.", "en población: América perdió muchos habitantes y Europa no", "Es la diferencia más grande."),
        ("{F} Sofía dice: «Solo América cambió». ¿Qué dato de Europa la contradice?", "Europa recibió plata, papa, maíz, tomate y cacao, y su comercio creció", "La ficha muestra cambios en Europa."),
        ("{F} Clasifica cada dato como «costo» o «ganancia» para América: a) llegada del trigo; b) pérdida de población.", "a: ganancia; b: costo", "El trigo es un recurso nuevo y la pérdida de población es un daño."),
        ("{F} ¿Qué criterio muestra la mayor diferencia entre ambos continentes: alimentación o población? Explica.", "población, porque América perdió gran parte de sus habitantes y Europa no", "En alimentación ambos recibieron productos."),
    ],
    ctx=("En un museo, una tabla compara «Antes de 1492» y «Después de 1492» la dieta en Europa. ¿Qué cuatro alimentos americanos aparecerían en la columna «Después»?", "papa, maíz, tomate y cacao", "Son los alimentos americanos de la ficha."),
    sc=[("¿Qué es comparar con un criterio?", "mirar el mismo aspecto en dos casos para ver parecidos y diferencias", "El criterio mantiene la comparación justa."),
        ("{F} ¿Qué llegó a América desde Europa en el criterio de alimentación?", "trigo, carne de vaca, de cerdo y de gallina, y caña de azúcar", "La ficha los nombra."),
        ("{F} ¿Qué ganó Europa en economía?", "llegó plata y creció el comercio", "La ficha lo dice.")],
    op=("Haz una tabla de tres columnas: «ámbito», «Europa» y «América», con cuatro filas: población, economía, alimentación y religión y lengua. Completa con datos de la ficha. Después escribe una frase: «La mayor diferencia es…». {F}",
        "Población: Europa sin pérdida; América con pérdida grande. Economía: Europa recibe plata; América extrae plata. La mayor diferencia es la población.",
        ["tabla completa", "datos correctos", "una frase de conclusión"], ["tabla de cuatro filas"], ["dejar casillas vacías", "poner el mismo dato en ambos lados"],
        "Pregunta por qué los ámbitos no son iguales para los dos continentes."),
    reinforce="Compara en voz alta Europa y América en dos ámbitos.",
    extend="Escribe una pregunta para investigar un ámbito de la conquista que no aparece en la ficha, como las enfermedades de los europeos.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (argumento, hecha para este cuaderno). Afirmación: «La conquista cambió la vida de Europa y de América, pero los costos fueron mayores para América». Datos: "
     "1) La población indígena disminuyó mucho por enfermedades, guerras y trabajos forzados. 2) Se trajeron personas africanas esclavizadas a América. 3) La plata de América enriqueció a la Corona española y aumentó el comercio. "
     "4) La papa, el maíz, el tomate y el cacao enriquecieron la alimentación europea. 5) Llegaron a América el trigo, el ganado, la caña de azúcar y el castellano.")
build(
    OA3, 5, F,
    use="Aprenderé a defender, con datos de varios ámbitos, que la conquista cambió ambos continentes pero con costos desiguales. Sirve para argumentar con evidencia y reconocer sus límites.",
    prior=["Sé las consecuencias de la conquista por ámbitos.", "Sé armar un argumento con afirmación, evidencia y conclusión."],
    explain=[
        "Un argumento histórico necesita afirmación, evidencia y conclusión. Hoy defendemos esta idea: la conquista cambió la vida de Europa y de América, pero los costos fueron mayores para América. Para defenderla comparamos datos de distintos ámbitos.",
        "En población, los indígenas disminuyeron mucho por enfermedades, guerras y trabajos forzados. En lo social, se trajeron personas africanas esclavizadas. En lo económico, la plata enriqueció a la Corona y aumentó el comercio. En alimentación, Europa recibió papa, maíz, tomate y cacao, y América recibió trigo, ganado, caña de azúcar y castellano.",
        "Estos datos muestran que ambos continentes cambiaron, pero con costos humanos más graves en América. Aun así, la ficha no mide todo: no da cifras, no cuenta la voz de los afectados y no dice cuánto duraron los efectos. Un buen argumento admite lo que no sabe.",
    ],
    vocab=[("afirmación", "idea que se defiende"), ("evidencia", "dato de una fuente que apoya la idea"), ("costo", "daño o pérdida que sufre alguien"), ("enriquecer", "aumentar la riqueza o la variedad de algo"), ("conclusión", "idea final que sale de unir la afirmación y la evidencia")],
    worked=[
        ("Elegir evidencia", "{F} ¿Qué dato apoya que el costo fue mayor para América?", ["Busco un dato de pérdida humana.", "La población indígena disminuyó mucho y llegaron esclavizados africanos."], "La población indígena disminuyó mucho"),
        ("Reconocer un límite", "{F} ¿La ficha dice cuántos indígenas murieron?", ["Busco una cifra.", "Solo dice que disminuyó mucho."], "No, no da una cifra"),
    ],
    mistakes=[("Defender una idea con solo un ámbito.", "Se mira un solo tipo de dato.", "Usa datos de al menos dos ámbitos."),
              ("Inventar cifras para sonar más seguro.", "Se completa lo que falta.", "Di que la ficha no entrega cifras.")],
    T=[
        ("{F} ¿Qué disminuyó mucho en América según el dato 1?", "la población indígena", "El dato 1 lo dice."),
        ("{F} ¿Quién fue traído a América según el dato 2?", "personas africanas esclavizadas", "El dato 2 lo dice."),
        ("{F} ¿Qué enriqueció a la Corona española?", "la plata de América", "El dato 3 lo dice."),
        ("{F} ¿Qué cuatro productos mejoraron la alimentación en Europa?", "papa, maíz, tomate y cacao", "El dato 4 los nombra."),
        ("{F} ¿Qué idioma llegó a América según el dato 5?", "el castellano", "El dato 5 lo menciona."),
        ("{F} ¿Qué dato apoya el costo humano mayor en América: el dato 1 o el dato 4?", "el dato 1", "Habla de la disminución de la población."),
        ("{F} ¿Qué dato muestra una ganancia para Europa: el dato 3 o el dato 2?", "el dato 3", "La plata enriqueció a la Corona."),
        ("{F} Ordena: a) conclusión: ambos cambiaron, con mayor costo en América; b) evidencia: la población indígena disminuyó mucho; c) afirmación: los costos fueron mayores para América.", "c, b, a", "Se afirma, se prueba y se concluye."),
        ("{F} Elige la afirmación mejor apoyada. A) «Solo Europa cambió». B) «Ambos continentes cambiaron».", "B", "Los datos 3 y 5 muestran cambios en los dos."),
        ("{F} Tomás dice: «Murieron 5.000.000 de indígenas». ¿Qué le responderías con la ficha?", "la ficha no da esa cifra, solo dice que disminuyó mucho", "No se puede afirmar una cifra sin fuente."),
        ("{F} Ana dice: «Como América recibió trigo y ganado, la conquista solo la favoreció». ¿Qué dato lo contradice?", "la población indígena disminuyó mucho y llegaron esclavizados africanos", "Hubo costos graves."),
        ("{F} Argumento A: «Fue peor para América». Argumento B: «Fue peor para América, pues la población indígena disminuyó mucho y se trajo esclavizados». ¿Cuál es mejor y por qué?", "B, porque incluye evidencia", "Un argumento necesita datos."),
        ("{F} ¿Qué evidencia nueva ayudaría a saber cómo vivieron esos cambios las personas afectadas?", "un testimonio escrito o contado por ellas", "Falta la voz de los afectados."),
    ],
    ctx=("En clase, alguien afirma: «La conquista fue igual de buena para todos». Usa dos datos de la ficha para responder.", "la población indígena disminuyó mucho y se trajeron africanos como esclavizados, mientras la plata enriqueció a la Corona", "Los datos muestran costos y ganancias desiguales."),
    sc=[("¿Cuáles son las tres partes de un argumento?", "afirmación, evidencia y conclusión", "Así se ordena la defensa de una idea."),
        ("{F} ¿Qué productos de América enriquecieron la alimentación europea?", "papa, maíz, tomate y cacao", "El dato 4 los nombra."),
        ("¿Por qué es bueno reconocer qué no sabemos?", "porque evita afirmar cosas sin prueba", "Un argumento honesto muestra sus límites.")],
    op=("Escribe un párrafo de cinco líneas que defienda la afirmación de la ficha. Usa al menos un dato de población, uno de economía y uno de alimentación. Termina con «La ficha no dice…». {F}",
        "La conquista cambió ambos continentes, pero fue más costosa para América. La población indígena disminuyó mucho. La plata enriqueció a la Corona. La papa y el maíz mejoraron la dieta europea. La ficha no dice cuántas personas murieron.",
        ["afirmación clara", "tres datos de ámbitos distintos", "un límite reconocido"], ["párrafo escrito"], ["usar un solo ámbito", "inventar cifras"],
        "Pide que subraye los tres ámbitos en su párrafo con tres colores."),
    reinforce="Explica en voz alta dos datos que apoyan que el costo fue mayor para América.",
    extend="Escribe otra afirmación sobre la conquista y los ámbitos de evidencia que necesitarías para defenderla.",
)

# ================================================================ OA 04 · EFECTOS SOBRE PUEBLOS INDÍGENAS
# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (pueblos y lugares, hecha para este cuaderno). Antes de la llegada de los españoles vivían en América muchos pueblos. Algunos ejemplos: los taínos, en las islas del Caribe; los aztecas o mexicas, en el centro de lo que hoy es México; los mayas, en el sur de México y Centroamérica; los incas, en los Andes; y los mapuche, en el centro y sur de lo que hoy es Chile. "
     "La conquista comenzó en el Caribe después de 1492, siguió en México (1519–1521) y en los Andes (desde 1532), y llegó a Chile desde 1540. Los efectos no fueron iguales en todos los lugares ni en el mismo momento.")
build(
    OA4, 1, F,
    use="Aprenderé dónde y cuándo vivían algunos pueblos indígenas que fueron afectados por la conquista. Sirve para ubicar los efectos en el espacio y en el tiempo.",
    prior=["Sé que Colón llegó a América en 1492.", "Sé que Cortés y Pizarro conquistaron imperios.", "Sé ubicar México, los Andes y Chile en un mapa."],
    explain=[
        "Antes de la llegada de los españoles, en América vivían muchos pueblos con sus propias formas de gobierno, creencias y lenguas. Eran los taínos en el Caribe, los aztecas en el centro de México, los mayas en el sur de México y Centroamérica, los incas en los Andes y los mapuche en el centro y sur de lo que hoy es Chile.",
        "La conquista no ocurrió de golpe. Empezó en el Caribe después de 1492, siguió en México entre 1519 y 1521, en los Andes desde 1532 y llegó a Chile desde 1540. Por eso los efectos sobre cada pueblo fueron distintos y ocurrieron en momentos diferentes.",
        "Para investigar los efectos, primero ubicamos al pueblo en el mapa y en la línea de tiempo. Así evitamos mezclar lo que le pasó a un pueblo con lo que le pasó a otro. Un efecto es un cambio que sufrió o vivió un pueblo por causa de la conquista.",
    ],
    vocab=[("pueblo indígena", "grupo de personas con una cultura, una lengua y un territorio propios que ya vivían en un lugar"), ("efecto", "cambio causado por un hecho"), ("territorio", "zona donde vive un pueblo"), ("Caribe", "mar y sus islas, donde llegó Colón"), ("mapuche", "pueblo que vive en el centro y sur de Chile")],
    worked=[
        ("Ubicar un pueblo", "{F} ¿Dónde vivían los incas?", ["Busco a los incas en la ficha.", "La ficha dice que vivían en los Andes."], "En los Andes"),
        ("Calcular un tiempo", "{F} ¿Cuántos años pasaron entre 1532, inicio de la conquista de los Andes, y 1540, llegada a Chile?", ["Busco los dos años.", "Resto: 1540 − 1532 = 8."], "8 años"),
    ],
    mistakes=[("Pensar que todos los pueblos sufrieron lo mismo y a la vez.", "Se mira la conquista como un solo hecho.", "Ubica cada pueblo y su momento."),
              ("Ubicar a los mapuche en México.", "Se confunden pueblos con lugares lejanos.", "Los mapuche vivían en el centro y sur de lo que hoy es Chile.")],
    T=[
        ("{F} ¿Dónde vivían los taínos?", "en las islas del Caribe", "La ficha lo dice."),
        ("{F} ¿Dónde vivían los mapuche?", "en el centro y sur de lo que hoy es Chile", "La ficha lo dice."),
        ("{F} ¿Qué pueblo vivía en el sur de México y Centroamérica?", "los mayas", "La ficha lo dice."),
        ("{F} ¿En qué años se conquistó el imperio azteca según la ficha?", "entre 1519 y 1521", "La ficha lo indica."),
        ("=", "{F} La conquista de México terminó en 1521 y la de los Andes empezó en 1532. ¿Cuántos años pasaron?", "1532-1521", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Dónde empezó la conquista: en el Caribe o en Chile?", "en el Caribe", "La ficha lo dice."),
        ("{F} Un mapa muestra una mancha en los Andes con la palabra «incas». ¿Está bien ubicada?", "Sí", "La ficha ubica a los incas en los Andes."),
        ("{F} Un mapa muestra a los mayas en la Patagonia. ¿Es correcto?", "No, estaban en el sur de México y Centroamérica", "La Patagonia es del extremo sur de Sudamérica."),
        ("Ordena por el momento en que llegó la conquista: Chile, el Caribe, los Andes, México.", "el Caribe, México, los Andes, Chile", "Los años son después de 1492, 1519, 1532 y 1540."),
        ("{F} Ana dice: «La conquista llegó a todos los pueblos en 1492». ¿Qué dato de la ficha la corrige?", "la conquista llegó en momentos distintos: 1519 a México, 1532 a los Andes y 1540 a Chile", "La ficha da fechas distintas."),
        ("{F} Pedro dice: «Lo que le pasó a los taínos es lo mismo que a los mapuche». ¿Qué cuidado se necesita?", "mirar que vivían en lugares distintos y fueron conquistados en tiempos distintos", "Los efectos dependen del lugar y del momento."),
        ("{F} Clasifica en «lugar» o «tiempo»: a) Andes; b) 1540; c) Caribe; d) 1519–1521.", "lugar: a y c; tiempo: b y d", "Los nombres de zonas son lugares y los años son tiempo."),
        ("{F} ¿Cuál de estos pueblos sufrió la conquista más tarde: los aztecas o los mapuche?", "los mapuche", "A Chile llegó desde 1540, después de 1519."),
    ],
    ctx=("Una exposición muestra tres fotos: una isla del Caribe, un valle andino y un bosque del sur de Chile, con los pueblos «taínos», «incas» y «mapuche». ¿Cómo las unirías con los nombres?", "isla del Caribe con taínos; valle andino con incas; bosque del sur de Chile con mapuche", "Cada pueblo corresponde a su lugar según la ficha."),
    sc=[("¿Qué es un efecto de la conquista?", "un cambio que sufrió o vivió un pueblo por causa de la conquista", "Así se define en esta clase."),
        ("{F} ¿Dónde vivían los aztecas?", "en el centro de lo que hoy es México", "La ficha lo dice."),
        ("¿Por qué conviene ubicar al pueblo antes de estudiar sus efectos?", "porque los efectos fueron distintos según el lugar y el momento", "Así no se mezclan los casos.")],
    op=("Dibuja un mapa simple de América con cinco puntos y los nombres de los pueblos de la ficha: taínos, aztecas, mayas, incas y mapuche. Debajo, dibuja una línea de tiempo con 1492, 1519, 1532 y 1540 y une cada año con el lugar donde llegó la conquista. {F}",
        "Taínos en el Caribe; aztecas en México; mayas en el sur de México; incas en los Andes; mapuche en el sur de Chile. 1492 Caribe, 1519 México, 1532 Andes, 1540 Chile.",
        ["cinco pueblos bien ubicados", "cuatro años en orden", "años unidos con lugares correctos"], ["mapa", "línea de tiempo"], ["ubicar a los mapuche en el norte", "unir 1540 con México"],
        "Pregunta qué diferencia habrá entre lo que vivieron los taínos y los mapuche, solo por el tiempo."),
    reinforce="Nombra en voz alta los cinco pueblos de la ficha y su lugar.",
    extend="Escribe una pregunta que te gustaría investigar sobre un pueblo indígena de la ficha.",
)

# ---------------------------------------------------------------- clase 2
F = ("Fuentes sobre los efectos de la conquista (hechas para este cuaderno, a partir de hechos conocidos). Fuente A: un texto de Bartolomé de las Casas, fraile dominico del siglo XVI, que denuncia los malos tratos a los indígenas y pide protegerlos. "
     "Fuente B: la crónica de Bernal Díaz del Castillo, un soldado que acompañó a Cortés y escribió años después lo que recordaba de la conquista de México. "
     "Fuente C: la obra de Felipe Guamán Poma de Ayala, un indígena de los Andes que, hacia 1615, escribió y dibujó una carta al rey de España para contar los abusos que vio. "
     "Fuente D: las Leyes de Burgos, de 1512, normas del rey para regular el trato a los indígenas, que muchas veces no se cumplían.")
build(
    OA4, 2, F,
    use="Aprenderé a preguntar quién hizo cada fuente sobre los efectos de la conquista y qué voz escucho. Sirve para investigar con fuentes dadas sin quedarse con una sola versión.",
    prior=["Sé que la procedencia es quién, cuándo y para qué.", "Sé que una fuente tiene límites."],
    explain=[
        "Para investigar los efectos de la conquista sobre los pueblos indígenas usamos fuentes de distinta voz. Bartolomé de las Casas era un fraile español que denunció los malos tratos y pidió proteger a los indígenas. Su texto muestra abusos, pero lo escribe un español que buscaba convencer al rey.",
        "Bernal Díaz del Castillo fue soldado de Cortés. Escribió años después, de memoria, y cuenta la conquista como la vivió un conquistador. Felipe Guamán Poma de Ayala fue un indígena andino que escribió y dibujó una carta al rey para denunciar abusos; es una voz indígena. Las Leyes de Burgos, de 1512, son normas del rey que muestran lo que se quería regular, aunque muchas veces no se cumplían.",
        "Una ley no prueba que se cumpliera. Un soldado cuenta su triunfo. Un fraile defiende a los indígenas, pero habla desde fuera. Un autor indígena habla desde dentro. Si juntamos las cuatro fuentes, entendemos mejor los efectos. Siempre anotamos quién habla y qué voz falta.",
    ],
    vocab=[("denunciar", "contar públicamente un abuso para que se corrija"), ("crónica", "relato de hechos ordenado en el tiempo"), ("fraile dominico", "religioso de la orden de Santo Domingo"), ("ley", "norma dictada por una autoridad que debe cumplirse"), ("voz", "persona o grupo que cuenta su versión")],
    worked=[
        ("Reconocer la voz", "{F} ¿Qué fuente tiene una voz indígena?", ["Reviso quién escribió cada fuente.", "Guamán Poma era un indígena de los Andes."], "La fuente C"),
        ("Reconocer un límite", "{F} Si una ley de 1512 prohíbe el maltrato, ¿prueba que no hubo maltrato?", ["Reviso lo que dice la ficha de las leyes.", "Dice que muchas veces no se cumplían."], "No, porque muchas veces no se cumplían"),
    ],
    mistakes=[("Creer que una ley prueba que algo se cumplía.", "Se confunde la norma con la realidad.", "Busca otra fuente que muestre cómo se actuó."),
              ("Creer que quien defiende a los indígenas habla por ellos.", "No se mira de quién es la voz.", "Distingue la voz de un fraile de la voz de un autor indígena.")],
    T=[
        ("{F} ¿Quién escribió la fuente B?", "Bernal Díaz del Castillo", "La ficha lo nombra."),
        ("{F} ¿Qué denunciaba Bartolomé de las Casas?", "los malos tratos a los indígenas", "La ficha lo indica."),
        ("{F} ¿En qué año se dictaron las Leyes de Burgos?", "en 1512", "La ficha lo indica."),
        ("{F} ¿Qué dibujó y escribió Guamán Poma?", "una carta al rey para contar los abusos que vio", "La ficha lo dice."),
        ("{F} ¿Quién acompañó a Cortés y escribió sobre la conquista?", "Bernal Díaz del Castillo", "La ficha dice que fue soldado de Cortés."),
        ("{F} ¿Qué fuente reúne normas del rey?", "la fuente D", "Son las Leyes de Burgos."),
        ("{F} Quieres conocer cómo vio los abusos una persona indígena. ¿Qué fuente usas?", "la fuente C", "Guamán Poma era indígena."),
        ("{F} Quieres saber qué quería regular el rey sobre el trato a los indígenas. ¿Qué fuente usas?", "la fuente D", "Las leyes muestran lo que se quería regular."),
        ("{F} Une cada fuente con su voz: 1) fuente A; 2) fuente B. a) un soldado conquistador; b) un fraile defensor de los indígenas.", "1 con b; 2 con a", "A es de Las Casas y B de Bernal Díaz del Castillo."),
        ("{F} Luis dice: «Si existían las Leyes de Burgos, todos trataban bien a los indígenas». ¿Qué dato lo corrige?", "la ficha dice que muchas veces no se cumplían", "Una ley no prueba su cumplimiento."),
        ("{F} Ana dice: «Bernal Díaz fue testigo, así que su relato es perfecto». ¿Qué cuidado se necesita?", "lo escribió años después, de memoria, y contaba como conquistador", "Un testigo también tiene su mirada y su memoria."),
        ("{F} Elige la pregunta que ninguna fuente responde bien. A) ¿Qué denunciaba Las Casas? B) ¿Qué sintió una niña mexica el día en que cayó Tenochtitlan?", "B", "Ninguna fuente de la ficha recoge esa voz."),
        ("{F} Para comparar una mirada española con una indígena sobre los abusos, ¿qué dos fuentes enfrentas?", "la fuente A con la fuente C", "Una la escribe un fraile español y la otra un indígena."),
    ],
    ctx=("En una biblioteca ves un libro con una ficha que dice: «Dibujos y carta de un autor indígena andino, hacia 1615». ¿Qué datos de procedencia entrega y cuál es la voz?", "autor indígena andino y época hacia 1615; la voz es indígena", "La ficha da autor y fecha; el autor indica la voz."),
    sc=[("¿Qué tres preguntas hacemos a una fuente?", "quién la hizo, cuándo y para qué", "Con ellas medimos lo que aporta."),
        ("{F} ¿Quién fue Bartolomé de las Casas?", "un fraile dominico del siglo XVI que defendía a los indígenas", "La ficha lo describe."),
        ("¿Por qué una ley no basta para saber lo que ocurría?", "porque dice lo que se debía hacer, no necesariamente lo que se hizo", "La norma y la práctica pueden ser distintas.")],
    op=("Haz una tabla con las fuentes A y C. En las columnas escribe «quién habla», «desde qué lugar», «qué denuncia o cuenta» y «qué voz falta». {F}",
        "A: Las Casas, un fraile español; denuncia malos tratos; falta la voz indígena directa. C: Guamán Poma, un indígena andino; cuenta abusos que vio; falta la mirada de un soldado.",
        ["dos filas completas", "voz identificada", "un límite por fuente"], ["tabla de cuatro columnas"], ["confundir los autores", "decir que una fuente cuenta todo"],
        "Pregunta cuál fuente le parece más cercana a un indígena y por qué."),
    reinforce="Nombra las cuatro fuentes y di quién habla en cada una.",
    extend="Escribe cómo contarían el mismo recreo un niño que jugó, una niña que miró y una profesora que cuidó, y qué diferencia habría.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (causas y efectos, hecha para este cuaderno). Enfermedades como la viruela, llevadas por los europeos, afectaron mucho a los pueblos indígenas, que no tenían defensas contra ellas. "
     "Muchas personas murieron. Los españoles organizaron sistemas de trabajo obligatorio: la encomienda, en que un español recibía indígenas para que trabajaran para él y debía evangelizarlos, y la mita, en que comunidades andinas debían enviar trabajadores por turnos a las minas. "
     "Muchos pueblos perdieron tierras. Los misioneros enseñaron el cristianismo y el castellano, y las creencias y lenguas indígenas fueron perseguidas o debilitadas, aunque muchas se conservaron. Con el tiempo nació una población mestiza.")
build(
    OA4, 3, F,
    use="Aprenderé a relacionar las causas con los efectos de la conquista sobre los pueblos indígenas. Sirve para explicar por qué cambió su vida.",
    prior=["Sé que hubo enfermedades, guerra y trabajo forzado.", "Sé distinguir causa y efecto."],
    explain=[
        "La conquista tuvo efectos profundos sobre los pueblos indígenas. Una causa fue la llegada de enfermedades como la viruela, para las que no tenían defensas. El efecto fue la muerte de muchas personas. Otra causa fue la organización de trabajos obligatorios por parte de los españoles.",
        "En la encomienda, un español recibía indígenas para que trabajaran para él, y debía evangelizarlos, es decir, enseñarles el cristianismo. En la mita, comunidades andinas enviaban trabajadores por turnos a las minas. El efecto fue la pérdida de tiempo, de salud y de cultivos propios.",
        "Otros efectos fueron la pérdida de tierras y el cambio de creencias y lenguas: los misioneros enseñaron el cristianismo y el castellano, y las lenguas y creencias indígenas fueron muchas veces perseguidas o debilitadas, aunque no desaparecieron del todo. Con el tiempo nació una población mestiza. Los pueblos no solo sufrieron: también resistieron, se adaptaron y conservaron partes de su cultura.",
    ],
    vocab=[("encomienda", "sistema en que un español recibía indígenas para que trabajaran para él y debía evangelizarlos"), ("mita", "trabajo obligatorio por turnos de comunidades andinas en las minas"), ("evangelizar", "enseñar el cristianismo"), ("resistir", "oponerse a algo que se impone"), ("mestizo", "persona descendiente de español e indígena")],
    worked=[
        ("Relacionar causa y efecto", "{F} La llegada de la viruela, ¿qué efecto tuvo?", ["Busco qué pasó con las personas.", "La ficha dice que muchas murieron porque no tenían defensas."], "Murieron muchas personas"),
        ("Distinguir sistemas", "{F} ¿Qué sistema enviaba trabajadores por turnos a las minas?", ["Repaso los dos sistemas de la ficha.", "La mita enviaba comunidades andinas a las minas por turnos."], "La mita"),
    ],
    mistakes=[("Decir que los pueblos indígenas fueron solo víctimas.", "No se consideran resistencia y adaptación.", "Agrega que resistieron y conservaron partes de su cultura."),
              ("Confundir encomienda y mita.", "Ambas eran trabajo obligatorio.", "La encomienda era con un español; la mita era por turnos en minas.")],
    T=[
        ("{F} ¿Qué enfermedad nombra la ficha?", "la viruela", "La ficha la nombra."),
        ("{F} ¿Qué sistema entregaba indígenas a un español para trabajar?", "la encomienda", "Así la describe la ficha."),
        ("{F} ¿Dónde trabajaban por turnos los mitayos, es decir, quienes cumplían la mita?", "en las minas", "La ficha lo dice."),
        ("{F} ¿Qué enseñaron los misioneros además del cristianismo?", "el castellano", "La ficha lo indica."),
        ("{F} ¿Qué perdieron muchos pueblos según la ficha?", "tierras", "La ficha lo dice."),
        ("{F} ¿Qué población nació con el tiempo?", "una población mestiza", "La ficha lo dice."),
        ("{F} Clasifica como «causa» o «efecto»: a) llegó la viruela; b) murieron muchas personas.", "a: causa; b: efecto", "La enfermedad produce las muertes."),
        ("{F} ¿Qué efecto tuvo el cambio de creencias y lenguas: desaparecieron del todo o se debilitaron y en parte se conservaron?", "se debilitaron y en parte se conservaron", "La ficha dice que muchas se conservaron."),
        ("{F} Une cada sistema con lo que hacía: 1) encomienda; 2) mita. a) turnos de trabajo en minas; b) indígenas entregados a un español que debía evangelizarlos.", "1 con b; 2 con a", "Así los describe la ficha."),
        ("{F} Marta dice: «Los pueblos indígenas solo sufrieron y no hicieron nada». Corrígela.", "también resistieron, se adaptaron y conservaron partes de su cultura", "La ficha dice que muchas creencias y lenguas se conservaron."),
        ("{F} Pablo dice: «La mita era en las haciendas». ¿Qué dato lo corrige?", "la mita enviaba trabajadores por turnos a las minas", "La ficha precisa el lugar."),
        ("{F} Ordena una cadena de efectos: a) faltaron personas en las comunidades; b) llegaron enfermedades; c) murieron muchas personas.", "b, c, a", "Primero la causa y luego los efectos."),
        ("{F} ¿Qué efecto se relaciona con la pérdida de tierras: menos cultivos propios o más cultivos propios?", "menos cultivos propios", "Sin tierras, los pueblos tenían menos para cultivar."),
    ],
    ctx=("Un museo muestra una frase de una tarjeta: «Los pueblos indígenas fueron eliminados». Usando la ficha, explica qué datos la corrigen.", "murieron muchas personas, pero muchos pueblos resistieron y se conservaron creencias y lenguas", "La ficha dice que hubo pérdida grande, pero también continuidad."),
    sc=[("¿Qué es la encomienda?", "un sistema en que un español recibía indígenas para que trabajaran para él y debía evangelizarlos", "Así lo define la ficha."),
        ("{F} ¿Qué efecto tuvo la llegada de la viruela?", "murieron muchas personas", "No tenían defensas contra ella."),
        ("Nombra dos formas en que los pueblos indígenas respondieron a la conquista.", "por ejemplo resistieron y conservaron parte de su cultura", "No solo sufrieron; también actuaron.")],
    op=("Dibuja un esquema con cuatro flechas: de «enfermedades» a un efecto, de «encomienda y mita» a un efecto, de «misioneros» a un efecto, y de «los pueblos» a una respuesta (resistencia o continuidad). Usa solo datos de la ficha. {F}",
        "Enfermedades → mueren muchas personas. Encomienda y mita → pérdida de tiempo y salud. Misioneros → cambio de creencias y lengua. Pueblos → conservan partes de su cultura.",
        ["cuatro flechas", "causa y efecto bien ordenados", "una respuesta de los pueblos"], ["esquema con flechas"], ["poner efectos como causas", "no incluir la respuesta de los pueblos"],
        "Pregunta qué efecto pudo tardar más en notarse y por qué."),
    reinforce="Explica en voz alta un efecto de las enfermedades y uno del trabajo obligatorio.",
    extend="Escribe una pregunta que le harías a una persona de un pueblo indígena actual sobre lo que se conservó.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (perspectivas, hecha para este cuaderno; las frases resumen ideas de cada voz y no son citas textuales). Perspectiva A, de un soldado español del siglo XVI: «Llegamos a tierras ricas y nos ganamos tierras y honores para servir al rey y a la fe». "
     "Perspectiva B, de Bartolomé de las Casas: «A los indígenas se les trata con crueldad y se debe proteger su vida y su libertad». "
     "Perspectiva C, de Guamán Poma, un indígena andino: «Los abusos de los españoles hacen sufrir a nuestro pueblo y el rey debería escucharnos». "
     "Territorios: en el Caribe, la población taína disminuyó tanto que casi desapareció en algunas islas; en los Andes, muchas comunidades siguieron viviendo y conservando su lengua; en Chile, los mapuche resistieron durante mucho tiempo la entrada de los españoles al sur del río Biobío.")
build(
    OA4, 4, F,
    use="Aprenderé a comparar cómo vieron la conquista distintas personas y cómo cambió en tres territorios. Sirve para entender por qué no hay una sola versión.",
    prior=["Sé quién fue Las Casas y quién fue Guamán Poma.", "Sé que los efectos fueron distintos según el lugar."],
    explain=[
        "Una perspectiva es el punto de vista de alguien sobre un hecho. Un soldado español veía la conquista como una oportunidad de ganar tierras y honores. Bartolomé de las Casas veía crueldad y pedía proteger la vida y la libertad de los indígenas. Guamán Poma, un indígena andino, veía el sufrimiento de su pueblo y pedía al rey que lo escuchara.",
        "También comparamos territorios. En el Caribe, la población taína disminuyó tanto que casi desapareció en algunas islas. En los Andes, muchas comunidades siguieron viviendo y conservaron su lengua. En Chile, los mapuche resistieron durante mucho tiempo la entrada de los españoles al sur del río Biobío.",
        "Al comparar, usamos los mismos criterios para todos: qué dice cada voz, qué cambió y qué se conservó. Las diferencias nos muestran que la conquista no fue una sola experiencia. Cada grupo y cada lugar vivió algo distinto.",
    ],
    vocab=[("perspectiva", "punto de vista de una persona o grupo sobre un hecho"), ("crueldad", "trato muy duro que causa sufrimiento"), ("honor", "reconocimiento social que se da a una persona"), ("río Biobío", "río del centro-sur de Chile que fue frontera entre españoles y mapuche"), ("resistir", "oponerse a algo que se impone")],
    worked=[
        ("Comparar perspectivas", "{F} ¿Qué buscaba el soldado y qué pedía Guamán Poma?", ["El soldado buscaba tierras y honores.", "Guamán Poma pedía que el rey escuchara a su pueblo."], "El soldado, tierras y honores; Guamán Poma, ser escuchado"),
        ("Comparar territorios", "{F} ¿Qué pasó con la población taína y con los mapuche?", ["Los taínos casi desaparecieron en algunas islas.", "Los mapuche resistieron al sur del Biobío."], "Los taínos casi desaparecieron en algunas islas; los mapuche resistieron"),
    ],
    mistakes=[("Pensar que todos los españoles opinaban lo mismo.", "Se ignora a Las Casas.", "Incluye que algunos españoles defendían a los indígenas."),
              ("Creer que los efectos fueron iguales en todo el continente.", "No se compara por territorio.", "Compara el Caribe, los Andes y Chile.")],
    T=[
        ("{F} ¿Qué buscaba el soldado español?", "tierras y honores", "La perspectiva A lo dice."),
        ("{F} ¿Qué pedía Las Casas?", "proteger la vida y la libertad de los indígenas", "La perspectiva B lo dice."),
        ("{F} ¿Quién escribió «el rey debería escucharnos»?", "Guamán Poma", "La perspectiva C lo dice."),
        ("{F} ¿Qué pasó con la población taína en algunas islas?", "casi desapareció", "La ficha lo dice."),
        ("{F} ¿Qué conservaron muchas comunidades de los Andes?", "su lengua", "La ficha lo dice."),
        ("{F} ¿Dónde resistieron los mapuche?", "al sur del río Biobío", "La ficha lo dice."),
        ("{F} Elige quién habla desde dentro de un pueblo indígena: A) Las Casas; B) Guamán Poma.", "B", "Guamán Poma era indígena andino."),
        ("{F} Elige la frase que une a Las Casas y a Guamán Poma. A) Ambos piden mejor trato para los indígenas. B) Ambos buscaban tierras y honores.", "A", "Los dos denuncian abusos."),
        ("{F} Clasifica como territorio «Caribe», «Andes» o «Chile»: a) los mapuche resistieron; b) los taínos casi desaparecieron; c) las comunidades conservaron su lengua.", "a: Chile; b: Caribe; c: Andes", "Cada dato corresponde a ese lugar."),
        ("{F} Tomás dice: «Los españoles y los indígenas pensaban igual sobre la conquista». Da dos datos de la ficha que lo contradicen.", "el soldado buscaba tierras y honores y Guamán Poma pedía ser escuchado por el rey", "Son intereses distintos."),
        ("{F} Ana dice: «Todos los españoles querían abusar de los indígenas». ¿Qué perspectiva de la ficha la corrige?", "la de Las Casas, que pedía protegerlos", "Algunos españoles los defendían."),
        ("{F} ¿En qué territorio de la ficha el efecto fue más grave para la población: el Caribe o los Andes? Explica.", "el Caribe, porque en algunas islas la población taína casi desapareció", "Los Andes conservaron comunidades."),
        ("{F} Compara lo que buscaba el soldado con lo que pedía Las Casas.", "el soldado buscaba tierras y honores; Las Casas pedía proteger la vida y la libertad de los indígenas", "Los dos hablan de la conquista, pero con intereses distintos."),
    ],
    ctx=("En un debate escolar, una compañera dice: «La conquista fue igual para los taínos que para los mapuche». ¿Qué dos datos de la ficha le responden?", "los taínos casi desaparecieron en algunas islas y los mapuche resistieron al sur del Biobío", "Los datos muestran experiencias distintas."),
    sc=[("¿Qué es una perspectiva?", "el punto de vista de una persona o grupo sobre un hecho", "Así se define en la clase."),
        ("{F} ¿Qué voz indígena aparece en la ficha?", "la de Guamán Poma", "Es el autor indígena."),
        ("¿Por qué conviene comparar territorios?", "porque los efectos fueron distintos según el lugar", "Así se evita generalizar.")],
    op=("Haz una tabla con tres filas: «soldado», «Las Casas» y «Guamán Poma». En las columnas escribe «qué buscaba o pedía» y «a quién protege». Después escribe dos frases comparando un territorio del Caribe con uno de los Andes. {F}",
        "Soldado: tierras y honores; protege su interés y el del rey. Las Casas: proteger a los indígenas. Guamán Poma: que escuchen a su pueblo. Caribe: casi desapareció; Andes: conservaron la lengua.",
        ["tres filas completas", "dos territorios comparados", "datos solo de la ficha"], ["tabla", "dos frases"], ["mezclar voces", "inventar datos de territorios"],
        "Pregunta qué territorio vivió un efecto más duro y pide un dato."),
    reinforce="Cuenta en voz alta las tres perspectivas y los tres territorios de la ficha.",
    extend="Escribe qué pregunta le harías a cada voz de la ficha si pudieras entrevistarla.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (argumento, hecha para este cuaderno). Afirmación: «La conquista tuvo efectos profundos y duraderos sobre los pueblos indígenas, pero ellos no desaparecieron: resistieron y conservaron parte de su cultura». Datos: "
     "1) Las enfermedades causaron la muerte de muchas personas. 2) La encomienda y la mita obligaron a trabajar a muchos indígenas. 3) Muchos pueblos perdieron tierras. 4) Las creencias y lenguas indígenas fueron debilitadas, pero muchas comunidades, como las andinas, conservaron su lengua. "
     "5) Los mapuche resistieron durante mucho tiempo al sur del río Biobío. 6) Nació una población mestiza que mezcló tradiciones.")
build(
    OA4, 5, F,
    use="Aprenderé a defender con evidencia que la conquista afectó mucho a los pueblos indígenas y que ellos resistieron y conservaron parte de su cultura. Sirve para concluir una investigación con fuentes.",
    prior=["Sé los efectos de la conquista.", "Sé armar un argumento con afirmación, evidencia y conclusión."],
    explain=[
        "Para terminar una investigación, escribimos una conclusión con evidencia. La afirmación de hoy tiene dos partes: la conquista tuvo efectos profundos y duraderos, y los pueblos indígenas no desaparecieron. Cada parte necesita datos.",
        "Para la primera parte tenemos las enfermedades, la encomienda y la mita, la pérdida de tierras y el debilitamiento de las creencias y las lenguas. Para la segunda, tenemos que las comunidades andinas conservaron su lengua, que los mapuche resistieron al sur del río Biobío y que nació una población mestiza que mezcló tradiciones.",
        "Una buena conclusión no exagera. Con esta ficha podemos decir que los efectos fueron profundos, pero no dar cifras exactas ni afirmar que todos los pueblos vivieron lo mismo. También reconocemos lo que falta: más voces indígenas y más fuentes para cada territorio.",
    ],
    vocab=[("duradero", "que permanece por mucho tiempo"), ("conclusión", "idea final que sale de unir la afirmación y la evidencia"), ("tradición", "costumbre que pasa de una generación a otra"), ("investigar", "buscar información en fuentes para responder una pregunta"), ("evidencia", "dato de una fuente que apoya una idea")],
    worked=[
        ("Elegir evidencia", "{F} ¿Qué dato apoya que los pueblos indígenas resistieron?", ["Busco un dato de oposición.", "Los mapuche resistieron al sur del Biobío."], "Los mapuche resistieron durante mucho tiempo al sur del Biobío"),
        ("Reconocer un límite", "{F} ¿La ficha permite afirmar que todos los pueblos vivieron lo mismo?", ["Reviso los datos.", "Hay datos distintos: lengua conservada en los Andes, resistencia mapuche."], "No, hubo experiencias distintas"),
    ],
    mistakes=[("Concluir que los pueblos indígenas desaparecieron.", "Se mira solo el daño.", "Agrega que resistieron y conservaron cultura."),
              ("Concluir que no hubo daño.", "Se mira solo la continuidad.", "Incluye las muertes, el trabajo obligatorio y la pérdida de tierras.")],
    T=[
        ("{F} ¿Qué causó la muerte de muchas personas según el dato 1?", "las enfermedades", "El dato 1 lo dice."),
        ("{F} ¿Qué dos sistemas obligaron a trabajar a muchos indígenas?", "la encomienda y la mita", "El dato 2 los nombra."),
        ("{F} ¿Qué perdieron muchos pueblos según el dato 3?", "tierras", "El dato 3 lo dice."),
        ("{F} ¿Qué conservaron las comunidades andinas?", "su lengua", "El dato 4 lo dice."),
        ("{F} ¿Dónde resistieron los mapuche?", "al sur del río Biobío", "El dato 5 lo dice."),
        ("{F} ¿Qué población nació mezclando tradiciones?", "la población mestiza", "El dato 6 lo dice."),
        ("{F} ¿Qué dato apoya la parte «efectos profundos»: el dato 2 o el dato 5?", "el dato 2", "El trabajo obligatorio fue un efecto profundo."),
        ("{F} ¿Qué dato apoya la parte «no desaparecieron»: el dato 4 o el dato 3?", "el dato 4", "La lengua conservada muestra continuidad."),
        ("{F} Ordena la conclusión: a) los pueblos sufrieron muertes, trabajo obligatorio y pérdida de tierras; b) pero resistieron y conservaron parte de su cultura; c) por eso la conquista tuvo efectos profundos sin eliminarlos.", "a, b, c", "Se presentan los daños, la continuidad y la conclusión."),
        ("{F} Elena dice: «Si hubo resistencia, no hubo efectos graves». ¿Qué dato la corrige?", "murieron muchas personas, hubo trabajo obligatorio y pérdida de tierras", "La resistencia convive con daño."),
        ("{F} Mateo dice: «Murieron exactamente 10.000.000 de indígenas». ¿Qué le responderías?", "la ficha no da cifras, solo dice que murieron muchas personas", "No se puede afirmar una cifra sin fuente."),
        ("{F} Argumento A: «Los pueblos indígenas resistieron». Argumento B: «Resistieron, pues los mapuche se opusieron al sur del Biobío y los andinos conservaron su lengua». ¿Cuál es mejor?", "B, porque incluye evidencia", "Un argumento necesita datos."),
        ("{F} ¿Qué evidencia nueva ayudaría a conocer mejor lo que se conservó?", "testimonios o fuentes de comunidades indígenas", "Falta su propia voz."),
    ],
    ctx=("En la feria del curso, un cartel dice «Los pueblos indígenas ya no existen». Usa dos datos de la ficha para corregirlo.", "los andinos conservaron su lengua y los mapuche resistieron; además nació una población mestiza", "Los datos muestran continuidad."),
    sc=[("¿Qué dos partes tiene la afirmación de hoy?", "efectos profundos y pueblos que no desaparecieron", "Así dice la ficha."),
        ("{F} ¿Qué dato muestra un efecto de la mita y la encomienda?", "muchos indígenas fueron obligados a trabajar", "Es el dato 2."),
        ("¿Por qué conviene reconocer qué falta?", "porque una conclusión honesta no afirma más de lo que prueban las fuentes", "Así se evita exagerar.")],
    op=("Escribe una conclusión de cinco líneas que responda: «¿Cómo afectó la conquista a los pueblos indígenas?». Usa tres datos de la ficha, uno de daño, uno de resistencia y uno de continuidad, y termina con «Para saber más, necesitaría…». {F}",
        "La conquista afectó mucho a los pueblos indígenas. Murieron muchas personas y se perdieron tierras. Los mapuche resistieron. Las comunidades andinas conservaron su lengua. Para saber más, necesitaría fuentes escritas por ellos.",
        ["tres datos de tipos distintos", "conclusión clara", "una necesidad de más fuentes"], ["texto escrito"], ["solo mostrar daño", "inventar cifras"],
        "Pide que marque con tres colores el daño, la resistencia y la continuidad."),
    reinforce="Explica en voz alta un dato de daño y uno de continuidad.",
    extend="Escribe una pregunta de investigación sobre un pueblo indígena actual de Chile y qué tipo de fuente necesitarías.",
)
