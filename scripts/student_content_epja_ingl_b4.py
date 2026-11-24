"""Inglés EPJA Nivel 2, módulo 2 (OAD-08): presentar la familia, el hogar, el barrio y las reglas de la casa, y acordar reglas para la clase y la comunidad del futuro. Textos inventados."""
from __future__ import annotations

from epja_ingl_common import build, GUION

O = "EPJA-INGL-NB2-OAD-08"

F1 = ("Presentation (example), Rosa: Hello. My name is Rosa. This is my husband, Pedro. This is my son, Tomas. He is 14. This is my daughter, Lucia. She is 9. "
      "That woman is my mother. She is 65. Our family is small, but happy.")

F2 = ("My house (example), Rosa: My house is small. There is one kitchen and one bathroom. There are two bedrooms. There is a small yard with a lemon tree. There isn't a garage.")

F3 = ("My neighborhood (example): There is a market and a small clinic. There are three bakeries. The school is next to the church. The park is on Oak Street. "
      "My house is at the corner. There isn't a subway station.")

F4 = ("House rules (example): 1. Please take off your shoes. 2. Don't smoke inside. 3. You can use the kitchen after 6:00. 4. Please turn off the lights. 5. Don't make noise after 10:00 p.m.")

F5 = ("Class rules (example), agreed by the group: Rule 1: Please arrive on time. Rule 2: Don't use your phone in class. Rule 3: You can ask for help. Rule 4: Please listen to others. "
      "Our community of the future (example): There are many trees. There is a library on every block. Don't throw trash in the street. You can ride a bike everywhere.")

F6 = ("Presentation (example), Tom: This is my family. My wife is Mary. We have two children. There are four people in my house. There are three bedrooms and one kitchen. "
      "In our neighborhood, there is a small park. House rules: Please wash your plate. Don't leave the door open. You can use the garden.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de lo que sé de mi familia y la presento en inglés: quiénes son, cuántos años tienen y cómo se llaman.",
    prior=["Sé decir el nombre de las personas de mi familia en español.", "Conozco el verbo to be (am, is, are).", "Sé decir números hasta 100."],
    explain=[
        "Tu familia es un tema que conoces bien. Para presentarla en inglés empiezas con This is... (Esta es, Este es...). This señala a alguien que está cerca, por ejemplo en una foto en tu mano.",
        "Para señalar a alguien más lejos, usa That: That woman is my mother. Los posesivos muestran de quién es algo: my (mi), your (tu), his (su, de él), her (su, de ella), our (nuestro).",
        "Para decir la edad usa to be, no have: He is 14, She is 9. Los números que dicen cuántos son se llaman cardinales: one, two, three. Los que dicen el orden son ordinales: first, second, third.",
        "Evita datos personales reales: usa nombres y edades de ejemplo para practicar. Presentar a tu familia no obliga a contar detalles privados.",
    ],
    vocab=[("husband", "esposo"), ("wife", "esposa"), ("son", "hijo"), ("daughter", "hija"), ("mother", "madre"), ("father", "padre"), ("family", "familia"), ("this", "este, esta (cerca)")],
    worked=[
        ("Presentar a una persona", "Quieres presentar a tu hija de 9 años (ejemplo).", ["Esta es mi hija: This is my daughter.", "Ella tiene 9 años: She is 9."], "This is my daughter. She is 9."),
        ("Usar el posesivo correcto", "Quieres decir «Su hijo tiene 14 años» hablando de Rosa.", ["Rosa es she: su es her.", "Hijo: son. Tiene 14: is 14.", "Escribo: Her son is 14."], "Her son is 14."),
    ],
    mistakes=[("Decir «She has 9 years».", "En inglés la edad se dice con to be, no con have.", "Escribe She is 9."),
              ("Usar his para una mujer.", "His es de él y her es de ella.", "Para Lucia usa her: Her brother is 14.")],
    T=[
        ("abc", "{F} Who is Pedro?", "Rosa's husband", "Rosa's father", "Rosa's son", "El texto dice «my husband, Pedro»."),
        ("{F} How old is Tomas? Escribe solo el número.", "14", "El texto dice «He is 14»."),
        ("abc", "{F} Who is Lucia?", "Rosa's daughter", "Rosa's mother", "Rosa's sister", "El texto dice «my daughter, Lucia»."),
        ("{F} How old is Lucia? Escribe solo el número.", "9", "El texto dice «She is 9» al presentar a Lucia; el 14 es la edad de Tomas."),
        ("ab", "{F} Who is 65?", "Rosa's mother", "Rosa's wife", "El texto dice «That woman is my mother. She is 65»."),
        ("abc", "En la presentación, «son» significa:", "Hijo", "Hija", "Esposo", "Son es hijo; daughter es hija."),
        ("abc", "Traduce: «Esta es mi hija».", "This is my daughter.", "This is my son.", "That is her daughter.", "This is significa «esta es» y my daughter es «mi hija»; las otras opciones cambian la persona."),
        ("abc", "Rosa señala a su madre al otro lado de la sala y dice: «___ is my mother.»", "That", "This", "These", "That se usa para alguien que está lejos."),
        ("abc", "Completa: Tomas ___ 14.", "is", "has", "are", "La edad se dice con to be: is 14."),
        ("abc", "Hablas de Rosa, no de ti. Completa: Pedro is ___ husband.", "her", "his", "my", "Rosa es she, y el posesivo de she es her; my sería el posesivo de quien habla."),
        ("ab", "Elige la oración correcta.", "Our family is small.", "Our family are small.", "Family es singular y se usa is."),
        ("{F} How many children does Rosa have? Escribe el número.", "2", "Tomas y Lucia son sus dos hijos."),
        ("abc", "¿Cuál oración sobre Lucia es correcta?", "She is 9.", "He is 9.", "It is 9.", "Lucia es una mujer, entonces el pronombre es she."),
    ],
    ctx=("abc", "En una reunión del centro (ejemplo) quieres presentar a una amiga, que está a tu lado. ¿Qué dices?", "This is my friend.", "That are my friend.", "This is me friend.", "This is se usa para una persona cercana y my es el posesivo de I."),
    sc=[("¿Cómo digo «mi esposo» en inglés?", "My husband", "Husband es esposo y my es mi."),
        ("Completa: She ___ 20 years old.", "is", "La edad se dice con to be."),
        ("¿Cuándo uso «that» en vez de «this»?", "Cuando la persona o cosa está lejos", "This señala algo cercano y that algo más lejano, por eso cambia la palabra.")],
    op=("Mira cómo Rosa presenta a su familia: {F} Escribe en tu cuaderno cinco oraciones para presentar a tu familia (usa nombres y edades de ejemplo): uso This is... y He/She is...",
        "This is my sister, Carla. She is 30. This is my brother, Luis. He is 25. Our family is big.",
        ["escribe cinco oraciones", "usa This is y he o she", "dice la edad con is"],
        ["cinco oraciones de presentación"],
        ["decir «has 9 years»", "mezclar his y her"],
        "Pregunta: «¿Quién es cada persona y cuántos años tiene?»."),
    reinforce="Escribe tres oraciones con my, his o her sobre personas de una foto de ejemplo.",
    extend="Presenta a tu familia de ejemplo a otra persona en voz alta, usando This is... y That is...",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo palabras del hogar y a decir qué hay en mi casa con There is y There are.",
    prior=["Sé decir mi familia en inglés.", "Conozco los números hasta diez.", "Conozco el verbo to be."],
    explain=[
        "Para describir lo que hay en un lugar se usa There is con una cosa: There is a kitchen. Se usa There are con varias: There are two bedrooms. There is y There are significan hay.",
        "Para decir que no hay, se agrega not: There isn't a garage (No hay garaje). Para varias cosas: There aren't two bathrooms. Para preguntar: Is there a yard? Are there two bedrooms?",
        "Las respuestas cortas repiten la forma: Yes, there is. No, there isn't. Yes, there are. No, there aren't.",
        "Las partes de la casa son rooms (habitaciones): kitchen (cocina), bathroom (baño), bedroom (dormitorio), living room (living), yard (patio).",
    ],
    vocab=[("kitchen", "cocina"), ("bathroom", "baño"), ("bedroom", "dormitorio"), ("living room", "living, sala"), ("yard", "patio"), ("there is", "hay (una cosa)"), ("there are", "hay (varias cosas)")],
    worked=[
        ("Elegir is o are", "Quieres decir: «Hay dos dormitorios».", ["Dos dormitorios son varias cosas.", "Uso there are.", "Escribo: There are two bedrooms."], "There are two bedrooms."),
        ("Decir que no hay", "Quieres decir: «No hay garaje».", ["Un garaje es una cosa: there is.", "En negativo: there isn't.", "Escribo: There isn't a garage."], "There isn't a garage."),
    ],
    mistakes=[("Escribir «There is two bedrooms».", "Con varias cosas se usa there are.", "Escribe There are two bedrooms."),
              ("Decir «Is there two bedrooms?».", "Se pregunta por varias cosas con Are there.", "Escribe Are there two bedrooms?")],
    T=[
        ("{F} How many bedrooms are there? Escribe solo el número.", "2", "El texto dice «There are two bedrooms»."),
        ("{F} How many bathrooms are there? Escribe solo el número.", "1", "El texto dice «one kitchen and one bathroom»."),
        ("ab", "{F} Is there a garage?", "No, there isn't.", "Yes, there is.", "El texto dice «There isn't a garage»."),
        ("abc", "{F} What is in the yard?", "A lemon tree", "A swimming pool", "A garage", "El texto dice «a small yard with a lemon tree»."),
        ("abc", "En la descripción, «bedroom» significa:", "Dormitorio", "Cocina", "Baño", "Bedroom es la habitación para dormir."),
        ("abc", "En la descripción, «yard» significa:", "Patio", "Garaje", "Techo", "Yard es el espacio abierto junto a la casa."),
        ("abc", "{F} Completa: There ___ two bedrooms.", "are", "is", "isn't", "Con dos cosas se usa there are."),
        ("abc", "{F} Completa: There ___ a kitchen.", "is", "are", "aren't", "Con una cosa se usa there is."),
        ("ab", "Elige la oración correcta.", "There are three chairs.", "There is three chairs.", "Con tres cosas se usa there are."),
        ("abc", "Traduce: «Hay un baño».", "There is a bathroom.", "There are a bathroom.", "It has a bathroom.", "Un baño es una sola cosa, así que se usa there is; there are va con varias."),
        ("ab", "«There isn't a garage» significa:", "No hay garaje", "Hay un garaje", "Isn't es la forma negativa de is."),
        ("abc", "Completa la pregunta: ___ there a yard?", "Is", "Are", "Do", "Con una cosa la pregunta empieza con Is there."),
        ("Ordena las palabras: bedrooms / two / are / There. Escribe la oración.", "There are two bedrooms.", "El orden es there are, el número y el sustantivo."),
    ],
    ctx=("abc", "Para un trámite de arriendo (ejemplo), una persona te pregunta en inglés: «Are there two bedrooms?» En tu casa de ejemplo hay dos. ¿Qué respondes?", "Yes, there are.", "Yes, there is.", "Yes, I do.", "La pregunta usa Are there, así que la respuesta repite are."),
    sc=[("¿Qué uso con varias cosas: there is o there are?", "There are", "El plural se usa con there are."),
        ("¿Cómo digo «No hay patio»?", "There isn't a yard.", "Isn't es la negación para una cosa."),
        ("¿Qué significa «living room»?", "Living o sala", "Es la habitación para estar y recibir a las personas.")],
    op=("Lee cómo Rosa describe su casa: {F} Escribe en tu cuaderno cinco oraciones sobre una casa de ejemplo: qué hay y qué no hay. Usa There is, There are y There isn't.",
        "There is a kitchen. There are three bedrooms. There is one bathroom. There isn't a garage. There is a small yard.",
        ["escribe cinco oraciones", "usa there is y there are bien", "usa al menos una negativa"],
        ["cinco oraciones sobre una casa"],
        ["usar there is con varias cosas", "olvidar la negativa"],
        "Pregunta: «¿Qué habitaciones tiene y cuántas?»."),
    reinforce="Mira tu casa y escribe tres oraciones con There is o There are.",
    extend="Haz tres preguntas con Is there...? o Are there...? sobre una casa y pide a otra persona que las responda.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a describir mi barrio con There is, There are y las palabras de lugar next to, on y at.",
    prior=["Digo qué hay en mi casa con there is y there are.", "Conozco next to y at the corner.", "Sé nombrar lugares del barrio."],
    explain=[
        "Un barrio se describe con lugares y con dónde están. Paso 1: nombra qué hay (there is un lugar, there are varios). Paso 2: di dónde está cada uno. Paso 3: di qué no hay.",
        "Para decir dónde, usa preposiciones de lugar: next to (al lado de), on (en una calle), at (en un punto, como la esquina), inside (dentro de). Ejemplo: The park is on Oak Street. My house is at the corner.",
        "Para preguntar: Is there a pharmacy in your neighborhood? Are there any parks? Respuestas: Yes, there is. No, there aren't.",
        "No uses la dirección real de tu casa. Usa nombres de calles de ejemplo para practicar con seguridad.",
    ],
    vocab=[("neighborhood", "barrio"), ("market", "mercado"), ("clinic", "consultorio"), ("church", "iglesia"), ("on", "en (una calle)"), ("at", "en (un punto)"), ("any", "algún, alguno (en preguntas)")],
    worked=[
        ("Describir con dónde", "Quieres decir: «El parque está en la calle Oak».", ["El parque: the park.", "Está en una calle: is on.", "Escribo: The park is on Oak Street."], "The park is on Oak Street."),
        ("Preguntar por una cosa", "Quieres preguntar si hay una farmacia.", ["Una cosa: Is there.", "Escribo: Is there a pharmacy in your neighborhood?"], "Is there a pharmacy in your neighborhood?"),
    ],
    mistakes=[("Decir «The park is in Oak Street».", "Con el nombre de una calle se usa on.", "Escribe The park is on Oak Street."),
              ("Escribir «There are a market».", "Una sola cosa lleva there is.", "Escribe There is a market.")],
    T=[
        ("abc", "{F} What is in the neighborhood?", "A market and a small clinic", "A subway station and a garage", "A swimming pool and a hotel", "El texto empieza diciendo «There is a market and a small clinic»."),
        ("{F} How many bakeries are there? Escribe solo el número.", "3", "El texto dice «There are three bakeries»."),
        ("ab", "{F} Where is the school?", "Next to the church", "Inside the market", "El texto dice «next to the church»."),
        ("abc", "{F} Where is the park?", "On Oak Street", "At the corner", "Next to the clinic", "El texto dice «on Oak Street»."),
        ("ab", "{F} Is there a subway station?", "No, there isn't.", "Yes, there is.", "El texto dice «There isn't a subway station»."),
        ("abc", "{F} Completa: There ___ three bakeries.", "are", "is", "isn't", "Con tres cosas se usa there are."),
        ("abc", "Completa la pregunta: ___ there a pharmacy in your neighborhood?", "Is", "Are", "Do", "Con una sola farmacia se usa Is there."),
        ("abc", "Completa la pregunta: ___ there any parks?", "Are", "Is", "Does", "Con varios parques se usa Are there."),
        ("ab", "{F} Are there two clinics? Elige la respuesta corta.", "No, there aren't.", "No, there isn't.", "El texto dice que hay una sola clínica, y la pregunta es plural, por eso aren't."),
        ("Ordena las palabras: is / The / bank / next to / the / market. Escribe la oración.", "The bank is next to the market.", "El orden es sujeto, verbo y lugar."),
        ("abc", "{F} Where is the house?", "At the corner", "On Oak Street", "Next to the church", "El texto dice «My house is at the corner»."),
        ("abc", "Traduce: «Hay una farmacia en mi barrio».", "There is a pharmacy in my neighborhood.", "There are a pharmacy in my neighborhood.", "It has a pharmacy in my neighborhood.", "Una farmacia es una sola cosa, así que se usa there is; there are va con varias."),
        ("ab", "¿Cuál es el error en «There are a market»?", "Debe ser There is", "Debe ser markets", "Una sola cosa lleva there is."),
    ],
    ctx=("abc", "Un vecino nuevo (ejemplo) te pregunta en inglés: «Is there a bakery near here?» Sí hay una, al lado de la iglesia. ¿Qué respondes?", "Yes, there is. It's next to the church.", "Yes, there are. It's in the church.", "Yes, I does. Next church.", "La respuesta repite is y agrega dónde está."),
    sc=[("¿Qué preposición uso con una calle?", "On", "On se usa con el nombre de una calle."),
        ("¿Qué significa «neighborhood»?", "Barrio", "Neighborhood es la zona de una ciudad con sus calles y lugares cercanos."),
        ("¿Cómo respondo «Is there a market?» si no hay?", "No, there isn't.", "Se repite is con la negación.")],
    op=("Revisa la descripción del barrio: {F} Escribe en tu cuaderno seis oraciones sobre tu barrio de ejemplo: tres cosas que hay, dónde están y una que no hay.",
        "There is a bakery. There are two schools. The park is on Pine Street. The clinic is next to the bank. My house is at the corner. There isn't a subway station.",
        ["escribe seis oraciones", "usa there is, there are y there isn't", "usa next to, on o at"],
        ["seis oraciones sobre el barrio"],
        ["usar in en vez de on con calles", "usar there is con varias cosas"],
        "Pregunta: «¿Qué lugar usas más seguido y dónde queda?»."),
    reinforce="Escribe tres lugares de tu barrio de ejemplo y dónde están con next to, on o at.",
    extend="Dibuja un mapa pequeño de tu barrio y rotula cuatro lugares con frases en inglés.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo las reglas de la casa con Please, Don't y You can, y las leo y escribo en inglés.",
    prior=["Entiendo avisos cortos.", "Conozco algunas órdenes como go straight.", "Sé decir los números."],
    explain=[
        "Las reglas de la casa dicen qué se debe hacer, qué no se debe hacer y qué se puede hacer. En inglés hay tres expresiones muy útiles: Please... (por favor), Don't... (no), You can... (puedes).",
        "Estas estructuras se enseñan como expresiones completas, sin teoría de tiempos nuevos. Please más una acción: Please take off your shoes. Don't más una acción: Don't make noise. You can más una acción: You can use the kitchen.",
        "Fíjate en que después de Please, Don't y You can, el verbo queda sin -s ni -ing: take, make, use.",
        "Las reglas se escriben a menudo en una lista numerada. Practica leyendo cada regla y diciendo si es una orden amable, una prohibición o un permiso.",
    ],
    vocab=[("please", "por favor"), ("don't", "no (prohibición)"), ("you can", "puedes"), ("take off", "sacar, quitarse"), ("turn off", "apagar"), ("noise", "ruido"), ("rule", "regla")],
    worked=[
        ("Leer una regla", "Regla (example): «Please turn off the lights.»", ["Please: por favor.", "Turn off: apagar.", "The lights: las luces."], "Por favor, apaga las luces"),
        ("Escribir una prohibición", "Quieres escribir: «No fumes adentro».", ["No: Don't.", "Fumar: smoke.", "Adentro: inside."], "Don't smoke inside."),
    ],
    mistakes=[("Escribir «Doesn't smoke inside».", "Para una prohibición en una regla se usa Don't, sin importar quién la lea.", "Escribe Don't smoke inside."),
              ("Escribir «You can to use the kitchen».", "Después de can el verbo va directo, sin to.", "Escribe You can use the kitchen.")],
    T=[
        ("abc", "{F} What do you do with your shoes?", "Take them off", "Turn them off", "Use them in the kitchen", "La regla 1 dice «take off your shoes»."),
        ("abc", "{F} «Don't smoke inside» significa:", "No fumes adentro", "Fuma adentro", "Fuma afuera", "Don't va antes de la acción y la prohíbe; inside significa adentro, no afuera."),
        ("ab", "{F} When can you use the kitchen?", "After 6:00", "Before 6:00", "La regla 3 dice «after 6:00»."),
        ("abc", "{F} What should you turn off?", "The lights", "The shoes", "The kitchen", "La regla 4 dice «turn off the lights»."),
        ("{F} After what time is noise not allowed? Escribe solo la hora, por ejemplo 9:00.", "10:00", "La regla 5 dice «after 10:00 p.m.»."),
        ("abc", "En las reglas, «please» significa:", "Por favor", "No", "Puedes", "Please es la palabra para pedir con amabilidad."),
        ("abc", "«You can use the kitchen» significa:", "Puedes usar la cocina", "No puedes usar la cocina", "Debes usar la cocina", "You can expresa un permiso (se puede), no una obligación ni una prohibición."),
        ("ab", "«Don't make noise» significa:", "No hagas ruido", "Haz ruido", "Don't indica que no se debe hacer algo."),
        ("abc", "Traduce: «Por favor, apaga las luces».", "Please turn off the lights.", "Please turns off the lights.", "Please turn on the lights.", "Please más una acción en forma base expresa una petición amable."),
        ("abc", "¿Qué regla permite hacer algo?", "You can use the kitchen after 6:00.", "Don't smoke inside.", "Don't make noise.", "You can expresa permiso; Don't prohíbe."),
        ("ab", "Elige la forma correcta.", "Don't smoke inside.", "Doesn't smoke inside.", "Don't es la forma de prohibición que se usa en reglas."),
        ("abc", "Completa: ___ take off your shoes.", "Please", "Can", "Doesn't", "La regla empieza con Please para pedir amablemente."),
        ("{F} How many rules are there? Escribe el número.", "5", "La lista tiene cinco reglas numeradas."),
    ],
    ctx=("abc", "En un edificio (ejemplo) ves un cartel en inglés: «Please keep the door closed.» ¿Qué debes hacer?", "Mantener la puerta cerrada", "Dejar la puerta abierta", "Pintar la puerta", "Please más keep the door closed pide mantenerla cerrada."),
    sc=[("¿Cómo digo «puedes usar»?", "You can use", "You can expresa permiso y después va el verbo sin -s ni to."),
        ("¿Qué significa «Don't»?", "No (prohibición)", "Don't indica que no se debe hacer algo."),
        ("Completa: Please ___ the lights.", "turn off", "Después de Please el verbo va en forma base.")],
    op=("Lee las reglas de la casa: {F} Escribe en tu cuaderno cuatro reglas para una casa de ejemplo: una con Please, dos con Don't y una con You can.",
        "Please wash your plate. Don't leave the door open. Don't make noise at night. You can use the garden.",
        ["escribe cuatro reglas", "usa Please, Don't y You can", "el verbo queda sin -s"],
        ["cuatro reglas escritas"],
        ["escribir «Doesn't»", "usar «to» después de can"],
        "Pregunta: «¿Qué reglas son más importantes en tu casa?»."),
    reinforce="Lee las cinco reglas en voz alta y marca con un color las que son permisos.",
    extend="Escribe tres reglas de ejemplo para el lugar donde trabajas con Please y Don't.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy acuerdo reglas para la clase y las uso para imaginar reglas de una comunidad del futuro.",
    prior=["Uso Please, Don't y You can.", "Digo qué hay con there is y there are.", "Entiendo ordinales como first, second y third."],
    explain=[
        "Acordar reglas es una tarea de grupo: cada persona propone, el grupo conversa y todos aceptan. En inglés puedes proponer con Please... y Don't..., y permitir con You can...",
        "Para imaginar una comunidad del futuro, usa There is y There are para decir qué hay: There are many trees. There is a library on every block. Y usa reglas: Don't throw trash in the street.",
        "Los números ordinales marcan el orden de las reglas: first rule, second rule, third rule. Los cardinales dicen cuántas hay: four rules.",
        "Imaginar el futuro no tiene respuestas correctas únicas: lo importante es usar las estructuras bien. Usa datos de ejemplo y no uses información personal.",
    ],
    vocab=[("on time", "a tiempo"), ("phone", "teléfono"), ("listen", "escuchar"), ("trash", "basura"), ("community", "comunidad"), ("future", "futuro"), ("everywhere", "en todas partes")],
    worked=[
        ("Proponer una regla", "Quieres proponer: «Por favor, llega a tiempo».", ["Por favor: Please.", "Llega a tiempo: arrive on time.", "Uno las partes."], "Please arrive on time."),
        ("Imaginar el futuro", "Quieres decir: «Hay muchos árboles».", ["Varios árboles: there are.", "Muchos: many.", "Escribo: There are many trees."], "There are many trees."),
    ],
    mistakes=[("Escribir «Don't to use your phone».", "Después de Don't el verbo va directo, sin to.", "Escribe Don't use your phone."),
              ("Usar there is con muchos árboles.", "Varias cosas llevan there are.", "Escribe There are many trees.")],
    T=[
        ("abc", "{F} What is Rule 1?", "Please arrive on time.", "Don't use your phone.", "You can ask for help.", "La primera regla pide llegar a tiempo."),
        ("abc", "{F} What is Rule 2?", "Don't use your phone in class.", "Please listen to others.", "You can ask for help.", "La segunda regla prohíbe usar el teléfono en clase."),
        ("ab", "{F} Can you ask for help in class?", "Yes, you can.", "No, you can't.", "La regla 3 dice «You can ask for help»."),
        ("abc", "{F} What does Rule 4 ask you to do?", "Listen to others", "Arrive on time", "Use your phone", "La regla 4 dice «Please listen to others»."),
        ("abc", "{F} What is on every block in the community of the future?", "A library", "A hospital", "A parking lot", "El texto dice «There is a library on every block»."),
        ("ab", "{F} «Don't throw trash in the street» significa:", "No tires basura en la calle", "Tira basura en la calle", "Don't antes de la acción la prohíbe, así que la frase pide no tirar basura."),
        ("abc", "Traduce: «Puedes andar en bicicleta por todas partes».", "You can ride a bike everywhere.", "You can to ride a bike everywhere.", "You ride can a bike everywhere.", "You can va seguido del verbo sin to."),
        ("ab", "Elige la regla bien escrita para tu clase.", "Please arrive on time.", "Arrives on time please.", "Please más una acción en forma base es una petición amable."),
        ("abc", "Completa: In our community, there ___ many trees.", "are", "is", "isn't", "Trees es plural, y con varias cosas se usa there are."),
        ("abc", "La regla 3 es la ___ regla.", "third", "second", "fourth", "Third es el ordinal de 3."),
        ("ab", "Elige la forma correcta.", "Don't use your phone.", "Doesn't use your phone.", "En una regla general se usa Don't."),
        ("abc", "{F} ¿Para qué sirve este texto?", "Para acordar reglas de la clase y la comunidad", "Para vender una casa", "Para contar un cuento", "El texto lista reglas acordadas por el grupo."),
        ("abc", "Traduce: «Por favor, escucha a los demás».", "Please listen to others.", "Please listens to others.", "Don't listen to others.", "Please va con el verbo en forma base."),
    ],
    ctx=("abc", "En tu grupo (ejemplo) deben acordar una regla sobre el teléfono. Alguien propone: «Don't use your phone in class.» ¿Qué dice la regla?", "No uses el teléfono en clase", "Usa el teléfono en clase", "Compra un teléfono nuevo", "Don't prohíbe la acción que sigue."),
    sc=[("¿Cómo digo «por favor, escucha»?", "Please listen", "Please más la acción en forma base."),
        ("¿Cómo digo «hay muchos árboles»?", "There are many trees", "Trees es plural, y con varias cosas se usa there are."),
        ("¿Qué ordinal es el de 2?", "Second", "Los ordinales marcan el orden: first es 1, second es 2 y third es 3.")],
    op=("Usa las reglas del grupo: {F} Escribe en tu cuaderno cuatro reglas para tu clase y tres oraciones sobre tu comunidad del futuro (datos imaginados). Después preséntalas a otra persona.",
        "Please arrive on time. Don't use your phone. You can ask for help. Please listen to others. There are many trees. There is a library on every block. You can ride a bike everywhere.",
        ["escribe cuatro reglas", "escribe tres oraciones sobre el futuro", "usa Please, Don't, You can, there is y there are"],
        ["cuatro reglas y tres oraciones"],
        ["escribir «Don't to»", "olvidar there are con varias cosas"],
        "Pregunta: «¿Qué regla propones para tu comunidad y por qué?»."),
    reinforce="Escribe tres reglas de ejemplo para una biblioteca comunitaria con Please y Don't.",
    extend="Imagina tu barrio dentro de veinte años y escribe cuatro oraciones con There is y There are.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado sobre familia, hogar, barrio y reglas, me autoevalúo y decido qué practicar después.",
    prior=["Presenté a mi familia.", "Describí mi casa y mi barrio.", "Escribí reglas de la casa y de la clase."],
    explain=[
        "Revisar lo logrado es comprobar qué puedes hacer ahora: presentar a tu familia con This is..., decir qué hay en tu casa y barrio con There is y There are, y dar reglas con Please, Don't y You can.",
        "Para revisar un texto tuyo, mira cuatro cosas: ¿usé his y her bien?, ¿usé there is con una cosa y there are con varias?, ¿usé el verbo sin -s después de Don't y You can?, ¿usé next to, on o at?",
        "Los siguientes pasos pueden ser: practicar una presentación en voz alta, escribir las reglas de tu casa en inglés o describir tu barrio a otra persona.",
        "Recuerda que este cuaderno no tiene audio: pide a otra persona que lea tu texto en voz alta y escucha cómo suena.",
    ],
    vocab=[("people", "personas"), ("children", "hijos, niños"), ("wash", "lavar"), ("plate", "plato"), ("door", "puerta"), ("open", "abierta"), ("garden", "jardín")],
    worked=[
        ("Revisar una presentación", "Alguien escribe: «There is four people in my house».", ["Cuatro personas son varias.", "Con varias se usa there are.", "Corrijo: There are four people in my house."], "There are four people in my house."),
        ("Usar una regla", "Quieres escribir: «No dejes la puerta abierta».", ["No: Don't.", "Dejar: leave.", "Escribo: Don't leave the door open."], "Don't leave the door open."),
    ],
    mistakes=[("Olvidar revisar los verbos después de Don't.", "El verbo debe quedar sin -s.", "Lee cada regla y comprueba que el verbo esté en forma base."),
              ("Confundir his y her.", "Se habla de la persona equivocada.", "Revisa si la persona es hombre o mujer.")],
    T=[
        ("abc", "{F} Who is Mary?", "Tom's wife", "Tom's mother", "Tom's daughter", "El texto dice «My wife is Mary»."),
        ("{F} How many children do Tom and Mary have? Escribe el número.", "2", "El texto dice «We have two children»."),
        ("{F} How many people are there in Tom's house? Escribe el número.", "4", "El texto dice «There are four people in my house»."),
        ("abc", "{F} How many bedrooms are there?", "Three", "Two", "Four", "El texto dice «There are three bedrooms»."),
        ("ab", "{F} What is in the neighborhood?", "A small park", "A big hospital", "El texto dice «there is a small park»."),
        ("abc", "{F} What is the first house rule?", "Please wash your plate.", "Don't leave the door open.", "You can use the garden.", "La primera regla de la casa dice «Please wash your plate»."),
        ("ab", "{F} «Don't leave the door open» significa:", "No dejes la puerta abierta", "Deja la puerta abierta", "Don't va antes de la acción y la prohíbe; open es abierta."),
        ("abc", "{F} What can you use?", "The garden", "The kitchen", "The phone", "El texto dice «You can use the garden»."),
        ("abc", "Completa: ___ is my wife.", "This", "Those", "These", "Con una persona cercana se usa This is."),
        ("abc", "Completa: There ___ four people.", "are", "is", "isn't", "Con varias personas se usa there are."),
        ("ab", "{F} Are there three bedrooms? Elige la respuesta corta.", "Yes, there are.", "Yes, there is.", "La pregunta usa Are there, y la respuesta repite are."),
        ("abc", "Traduce: «No dejes la puerta abierta».", "Don't leave the door open.", "Doesn't leave the door open.", "Don't leaves the door open.", "Don't va seguido del verbo en forma base."),
        ("abc", "¿Cuál oración tiene un error?", "There is two bedrooms.", "There are two bedrooms.", "There is a kitchen.", "Con dos cosas se usa there are."),
    ],
    ctx=("abc", "En una charla de tu comunidad (ejemplo), una persona presenta su casa y dice: «There are two bedrooms and one bathroom.» ¿Qué dice de su casa?", "Hay dos dormitorios y un baño", "Hay un dormitorio y dos baños", "Hay dos cocinas", "There are dos dormitorios; there is un baño."),
    sc=[("¿Cuándo uso there is?", "Con una sola cosa", "There is va con una cosa (there is a kitchen) y there are con varias."),
        ("Completa: ___ leave the door open. (no)", "Don't", "Don't prohíbe la acción que sigue."),
        ("¿Qué quiero practicar la próxima semana?", "Elijo una parte y la anoto", "Una meta propia ayuda a avanzar.")],
    op=("Haz la revisión final: {F} Escribe en tu cuaderno un texto de siete oraciones sobre tu familia de ejemplo, tu casa, tu barrio y tres reglas. Después anota un logro y un paso siguiente.",
        "This is my family. There are four people. There are three bedrooms. There is a market in my neighborhood. Please wash your plate. Don't leave the door open. You can use the garden. Achieved: there is and there are. Next: more rules.",
        ["escribe siete oraciones", "usa This is, there is o are y una regla", "anota un logro y un paso siguiente"],
        ["un texto y dos frases de autoevaluación"],
        ["no incluir una regla", "usar datos personales reales"],
        "Pregunta: «¿Qué parte te costó más y cómo la practicarás?»."),
    reinforce="Repasa las reglas de la clase 4 y escribe cuatro reglas nuevas.",
    extend="Presenta tu texto a otra persona en voz alta, mirando una lista de palabras de ayuda.",
)
