"""Student material for 1.º básico Lengua y Cultura de los Pueblos Originarios Ancestrales, OA 13 (valores y principios) y OA 14 (producción e intercambio ancestral)."""
from __future__ import annotations

from student_content_lc_a1 import F_AYM, F_DIA, F_KAW, L, M, T, W
from student_lessons import ex

OA13, OA14 = "LC01 OA 13", "LC01 OA 14"

# ============================================================ OA 13 · Valores y principios personales y familiares
L(
    OA13, 1,
    materials="Lápiz y hojas. Los casos de niños y niñas están escritos en el cuaderno; son historias inventadas para practicar.",
    use="Aprenderé a reconocer un valor como el respeto, compartir o cuidar mirando lo que alguien hace, no solo lo que dice.",
    prior=["Sé qué es compartir.", "Sé qué es una acción."],
    explain=[
        "Un valor es una idea que consideramos importante para vivir bien con los demás. Respeto, compartir, cuidar, escuchar, agradecer y la honestidad (decir la verdad) son valores. Muchas familias y comunidades los enseñan, cada una a su manera.",
        "Para saber si alguien vive un valor, miramos lo que hace. Una persona puede decir «yo comparto» y no compartir nunca. Otra puede no decir nada y compartir su colación todos los días. La conducta, es decir lo que hacemos, muestra el valor.",
        "Para reconocer un valor en una acción nos preguntamos: ¿qué hizo?, ¿a quién ayudó o cuidó? y ¿qué valor muestra? No es necesario contar cosas privadas de nuestra familia. Podemos practicar con casos inventados.",
    ],
    vocab=[("valor", "idea importante para vivir bien con otros"), ("conducta", "lo que una persona hace"), ("respeto", "tratar bien a las personas y a lo que les importa"), ("compartir", "dar una parte de lo que tengo"), ("agradecer", "decir gracias por lo recibido")],
    worked=[
        W("Valor en una acción", "Caso inventado: Luz tiene dos galletas y le da una a su compañero que no trajo colación. ¿Qué valor muestra?", ["Miro qué hizo: dio una galleta.", "Miro a quién ayudó: a su compañero.", "Eso es compartir."], "Compartir."),
        W("Palabra y conducta", "Pedro dice «yo cuido las plantas», pero nunca las riega. ¿Su conducta muestra cuidado?", ["Dice una cosa.", "Hace otra.", "La conducta no muestra cuidado."], "No."),
    ],
    mistakes=[
        M("Creer que un valor se ve solo por lo que alguien dice.", "Lo que hacemos muestra más que lo que decimos.", "Mira la acción."),
        M("Pensar que hay un solo valor correcto.", "Cada familia puede enseñar varios valores.", "Reconoce los que ves en la acción."),
    ],
    R=[
        ex("Caso inventado: Ana ayuda a su amigo a levantarse. ¿Qué valor muestra: cuidar o romper?", "Cuidar", "Ayudar al otro muestra cuidado."),
        ex("Dar una parte de lo que tengo es compartir. ¿Verdadero o falso?", "Verdadero", "Esa es la idea."),
        ex("Decir «gracias» muestra el valor de ______.", "agradecer", "Gracias es agradecimiento."),
    ],
    C=[
        ex("¿Qué es la conducta? A) lo que una persona hace B) lo que una persona dice", "A", "La conducta son las acciones."),
        ex("Verdadero o falso: un valor se ve en lo que hacemos.", "Verdadero", "Las acciones muestran los valores."),
        ex("¿Debes contar cosas privadas de tu familia para aprender de valores?", "No", "Se puede usar casos inventados."),
    ],
    A=[
        ex("Une la acción con el valor. 1) escuchar sin interrumpir 2) dar la mitad de la colación 3) decir gracias. a) agradecer b) respeto c) compartir", "1-b, 2-c, 3-a", "Cada acción muestra un valor."),
        ex("Caso inventado: Tomás recoge un papel del patio sin que se lo pidan. ¿Qué valor muestra?", "Cuidar el lugar", "Cuida el patio."),
        ex("Marca las acciones que muestran respeto: a) esperar el turno b) burlarse de alguien c) saludar a una persona mayor.", "a y c", "La b no respeta."),
    ],
    Z=[
        ex("Beto dice «yo respeto a todos» y se ríe de un compañero. ¿Qué muestra su conducta?", "Que no respeta", "Su acción contradice sus palabras."),
        ex("¿Por qué miramos la conducta y no solo las palabras?", "Porque lo que hacemos muestra el valor", "Las palabras solas no bastan."),
    ],
    D=[
        ex("Rosa comparte 3 lápices con un amigo y se queda con 5. ¿Cuántos tenía al principio?", "8", "3 + 5 = 8 lápices."),
        ex("Dos familias enseñan valores distintos: una enfatiza compartir y otra, escuchar. ¿Cuál está equivocada?", "Ninguna", "Cada familia puede enseñar distintos valores."),
    ],
    context=[ex("Caso inventado: en un grupo, Matías reparte los lápices de colores para que todos puedan dibujar. ¿Qué valor muestra?", "Compartir", "Reparte lo que tiene.")],
    selfcheck=[ex("¿Qué es un valor?", "Una idea importante para vivir bien con otros", "Guía cómo tratamos a los demás."), ex("¿Qué muestra un valor: lo que digo o lo que hago?", "Lo que hago", "La conducta lo muestra."), ex("Nombra un valor.", "Respeto, compartir, cuidar, escuchar o agradecer", "Son los de la explicación.")],
    task=T("Elige uno de estos casos inventados y escribe qué hizo, a quién ayudó y qué valor muestra. Caso 1: una niña espera su turno en el juego. Caso 2: un niño le da la mitad de su pan a un compañero. Caso 3: una niña dice gracias a la señora que le abrió la puerta. No escribas nada privado de tu familia.",
           "Caso 2: el niño dio la mitad de su pan. Ayudó a su compañero. Muestra el valor de compartir.",
           ["dice qué hizo", "dice a quién ayudó", "nombra el valor"], ["tres frases"], ["nombrar un valor sin mirar la acción"],
           "Valora que mire la acción; si cuenta cosas de su familia, agradecer pero recordar que no es obligatorio."),
    reinforce="Observa una acción amable y di qué valor muestra.",
    extend="Pregunta en tu casa qué valor es importante y por qué, solo si te sientes cómodo contándolo.",
)

L(
    OA13, 2,
    materials="Lápiz y hojas. Los casos de familias diversas están escritos en el cuaderno.",
    use="Aprenderé que las familias y comunidades pueden enseñar valores de maneras distintas y que no existe una única práctica correcta.",
    prior=["Sé que cada familia es distinta.", "Sé qué son los valores."],
    explain=[
        "Las familias son distintas: unas son grandes y otras pequeñas; unas viven en el campo y otras en la ciudad; unas celebran ciertas fiestas y otras celebran fiestas distintas. Todas pueden enseñar valores como respeto, compartir y cuidar, aunque lo hagan de maneras diferentes.",
        "En una comunidad de un pueblo originario también hay diversidad. Una familia puede enseñar respeto saludando a los mayores; otra, ayudando en el trabajo; otra, escuchando las historias. No podemos decir que todas las familias de un pueblo hacen lo mismo.",
        "Por eso evitamos suponer. Si no sabemos cómo es una familia, preguntamos con respeto o no opinamos. No comparamos para decir quién lo hace mejor. Valoramos que cada familia cuida a los suyos a su manera.",
    ],
    vocab=[("familia", "personas que se cuidan y viven juntas o cercanas"), ("diverso", "distinto, que hay de muchos tipos"), ("suponer", "creer algo sin comprobarlo"), ("manera", "forma de hacer algo"), ("práctica", "algo que se hace con frecuencia")],
    worked=[
        W("Misma idea, distinta manera", "Caso inventado: En una casa los niños saludan a los mayores con un abrazo; en otra con un apretón de manos. ¿Ambas muestran respeto?", ["Las dos saludan.", "Cambia la forma.", "Las dos muestran respeto."], "Sí."),
        W("No suponer", "Luz cree que todos en su curso celebran lo mismo en invierno. ¿Qué hace antes de afirmarlo?", ["Pregunta con respeto.", "Escucha a sus compañeros.", "No supone."], "Pregunta antes de afirmarlo."),
    ],
    mistakes=[
        M("Pensar que mi familia hace lo correcto y las otras no.", "Hay muchas maneras de enseñar valores.", "Mira lo que valoran, no solo cómo lo hacen."),
        M("Decir «las familias de ese pueblo hacen todas lo mismo».", "Dentro de un pueblo hay diversidad.", "Di «algunas familias»."),
    ],
    R=[
        ex("Familias diversas son familias distintas. ¿Verdadero o falso?", "Verdadero", "Diverso significa distinto."),
        ex("Una familia saluda con abrazo y otra con la mano. ¿Ambas pueden mostrar respeto? Sí o No.", "Sí", "Hay varias formas de respetar."),
        ex("¿Suponer es creer algo sin comprobarlo? Sí o No.", "Sí", "Eso es suponer."),
    ],
    C=[
        ex("¿Qué haces antes de opinar de una familia? A) pregunto con respeto B) supongo", "A", "No se supone."),
        ex("Verdadero o falso: todas las familias de un pueblo hacen lo mismo.", "Falso", "Dentro de un pueblo hay diversidad."),
        ex("¿Se compara a las familias para decir quién es mejor?", "No", "Cada familia cuida a su manera."),
    ],
    A=[
        ex("Caso inventado A: una familia enseña a ayudar cocinando juntos. Caso B: otra enseña a ayudar cuidando a los animales. ¿Qué valor tienen en común?", "Ayudar", "En ambas se enseña a ayudar."),
        ex("Marca las frases que respetan la diversidad: a) «Algunas familias cocinan juntas» b) «Todas las familias hacen lo mismo» c) «Cada familia tiene su manera».", "a y c", "La b generaliza."),
        ex("Caso inventado: en la casa de Mía los niños saludan a los mayores con un abrazo y en la casa de Teo con la mano. ¿Cuántas de estas dos familias saludan con respeto?", "2", "Las dos muestran respeto, con formas distintas."),
    ],
    Z=[
        ex("Pedro dice «la familia de mi amigo es rara porque no celebra como yo». ¿Qué le dices?", "Que cada familia tiene su manera", "No hay una sola forma correcta."),
        ex("¿Por qué decimos «algunas familias» y no «todas»?", "Porque hay diversidad", "No todas hacen igual."),
    ],
    D=[
        ex("Un libro dice «las familias de un pueblo viven así». ¿Qué cuidado tienes al leerlo?", "Revisar la fuente y recordar que hay diversidad", "No toda la comunidad es igual."),
        ex("En un curso hay 24 niños y 6 viven en el campo. ¿Cuántos no viven en el campo?", "18", "24 − 6 = 18."),
    ],
    context=[ex("Caso inventado: Camila y Tomás cuentan que en sus casas se agradece distinto: ella dice gracias en voz alta y él hace un dibujo. ¿Quién agradece mal?", "Ninguno", "Las dos son formas de agradecer.")],
    selfcheck=[ex("¿Las familias son todas iguales?", "No", "Hay mucha diversidad."), ex("¿Qué evito?", "Suponer", "Pregunto con respeto."), ex("¿Hay una única manera de enseñar valores?", "No", "Hay muchas maneras.")],
    task=T("Dibuja dos familias inventadas (no la tuya) que enseñan el respeto de maneras distintas: una familia saluda a los mayores y otra escucha sus historias. Escribe qué tienen en común y una frase que diga «cada familia tiene su manera».",
           "Dibujé una familia que saluda y otra que escucha historias. En común: ambas enseñan respeto. Frase: «Cada familia tiene su manera».",
           ["muestra dos maneras distintas", "dice lo que tienen en común", "no jerarquiza"], ["dibujo", "frase"], ["decir que una familia es mejor"],
           "Reconoce que no jerarquizó; si apareció una familia real, agradecer sin pedir más detalles."),
    reinforce="Menciona una cosa en que dos familias se parecen y otra en que son distintas, con ejemplos inventados.",
    extend="Escribe una pregunta respetuosa que podrías hacer para conocer cómo otra familia enseña un valor.",
)

L(
    OA13, 3,
    materials="Lápiz y hojas. Un dilema inventado está escrito en el cuaderno.",
    use="Aprenderé a pensar qué acción elegir cuando un valor se enfrenta con otro y qué pasaría con cada decisión.",
    prior=["Sé qué son los valores.", "Sé que cada decisión tiene un efecto."],
    explain=[
        "A veces dos valores parecen chocar. Un dilema es una situación en que hay que elegir entre dos acciones y las dos tienen algo bueno. Por ejemplo, un niño tiene una sola galleta: puede comérsela o compartirla con alguien que no trajo colación.",
        "Para decidir, pensamos: ¿qué opciones hay?, ¿qué valor muestra cada una?, ¿qué efecto tiene en las personas? y ¿qué haría una persona que quiere cuidar a los demás? Es mejor pensar antes que actuar sin pensar.",
        "No hay una única respuesta perfecta en todos los dilemas. Lo importante es elegir con razones y anticipar lo que ocurrirá. Practicamos con casos inventados para no hablar de personas reales.",
    ],
    vocab=[("dilema", "situación en que hay que elegir entre dos opciones"), ("opción", "una de las cosas que puedo elegir"), ("efecto", "lo que ocurre después de una decisión"), ("razón", "motivo por el que elijo algo"), ("anticipar", "pensar antes lo que ocurrirá")],
    worked=[
        W("Analizar un dilema", "Caso inventado: Ana tiene una galleta y su compañero no trajo colación. Puede comerla o compartirla. ¿Qué efecto tiene compartirla?", ["Si la comparte, el compañero come.", "Ana come menos.", "Se muestra el valor de compartir."], "El compañero come y Ana muestra compartir."),
        W("Elegir con razones", "Ana decide compartir la mitad. ¿Qué razón puede dar?", ["Quiere cuidar a su compañero.", "También ella come algo.", "Es una decisión que respeta a ambos."], "Quiere cuidar a su compañero y también come ella."),
    ],
    mistakes=[
        M("Elegir sin pensar en el efecto.", "Puede dañar a alguien.", "Pregunta: ¿qué pasará después?"),
        M("Pensar que hay una sola respuesta correcta siempre.", "En un dilema hay dos cosas valiosas.", "Elige con razones y cuida a las personas."),
    ],
    R=[
        ex("Un dilema es elegir entre dos opciones. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("Caso inventado: Luz puede comerse su galleta o compartirla. ¿Cuántas opciones tiene?", "2", "Comer o compartir."),
        ex("El efecto es lo que ocurre después de una decisión. ¿Verdadero o falso?", "Verdadero", "Eso significa efecto."),
    ],
    C=[
        ex("¿Qué haces antes de decidir? A) pienso en el efecto B) elijo al azar", "A", "Anticipar ayuda a cuidar."),
        ex("Verdadero o falso: una razón es el motivo de mi elección.", "Verdadero", "Eso es una razón."),
        ex("¿Qué pasa si no pensamos en el efecto?", "Podemos dañar a alguien", "No anticipamos lo que ocurre."),
    ],
    A=[
        ex("Caso inventado: Tomás ve que un niño pequeño está solo en el patio y tiene su juego favorito. Puede jugar solo o invitarlo. Escribe el efecto de invitarlo.", "El niño no queda solo y Tomás comparte", "Invitar muestra compañía y compartir."),
        ex("Une cada opción con su valor. 1) esperar el turno 2) ayudar a levantar a un compañero 3) decir la verdad. a) cuidar b) honestidad c) respeto", "1-c, 2-a, 3-b", "Cada opción muestra un valor."),
        ex("Ordena para decidir bien: 1) elijo 2) pienso en el efecto 3) miro mis opciones.", "3, 2, 1", "Primero opciones, luego efecto y al final decisión."),
    ],
    Z=[
        ex("Pedro eligió sin pensar y un compañero se puso triste. ¿Qué paso saltó?", "Pensar en el efecto", "No anticipó lo que ocurriría."),
        ex("¿Por qué conviene dar razones de una decisión?", "Porque otros entienden por qué elegí", "Las razones ayudan a convivir."),
    ],
    D=[
        ex("Un niño tiene 4 galletas y comparte 1 con cada uno de sus 2 compañeros. ¿Cuántas le quedan?", "2", "4 − 1 − 1 = 2."),
        ex("En un dilema inventado, dos niños eligen cosas distintas con buenas razones. ¿Alguno está equivocado?", "No necesariamente", "Puede haber más de una buena decisión."),
    ],
    context=[ex("Caso inventado: Rosa encuentra una moneda en la sala y no sabe de quién es. Puede guardarla o preguntar de quién es. ¿Qué opción cuida la confianza?", "Preguntar de quién es", "Eso muestra honestidad.")],
    selfcheck=[ex("¿Qué es un dilema?", "Elegir entre dos opciones", "Hay dos caminos."), ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es un efecto?", "Lo que ocurre después", "Es la consecuencia."), ex("¿Qué debo dar al decidir?", "Razones", "Explican mi elección.")],
    task=T("Lee este dilema inventado: «Una niña tiene una sola pelota en el recreo. Dos grupos quieren usarla a la vez.» Escribe dos opciones, el valor que muestra cada una y el efecto de cada una. Después elige una y da una razón.",
           "Opción 1: turnos (respeto), todos juegan. Opción 2: dársela a un grupo (injusto), el otro se enoja. Elijo turnos porque todos juegan.",
           ["dice dos opciones", "anticipa los efectos", "da una razón"], ["tabla de dos opciones", "frase de razón"], ["no pensar en el efecto"],
           "Valora que anticipa los efectos; no hay una respuesta única, escuchar la razón."),
    reinforce="Cuenta un dilema inventado y di dos opciones.",
    extend="Escribe un dilema inventado con un valor de compartir y uno de cuidar.",
)

L(
    OA13, 4,
    materials="Lápiz y hojas. Un diálogo inventado con tres opiniones está escrito en el cuaderno.",
    use="Aprenderé a escuchar otra razón y a revisar mi opinión sin atacar a nadie.",
    prior=["Sé escuchar sin interrumpir.", "Sé dar una opinión con una razón."],
    explain=[
        "Cuando conversamos sobre qué es lo mejor, puede haber opiniones distintas. Escuchar otra razón significa prestar atención a lo que dice la otra persona y entender por qué lo piensa. No es lo mismo que estar de acuerdo.",
        "Después de escuchar, podemos mantener nuestra opinión o cambiarla, según las razones. Cambiar de opinión con buenas razones no es perder. Lo que no hacemos es burlarnos de la persona ni atacar su identidad.",
        "Para revisar una idea usamos frases como «entiendo que piensas…», «yo pienso… porque…» y «¿puedes contarme más?». Estas frases cuidan a la persona y nos ayudan a aprender de ella.",
    ],
    vocab=[("escuchar", "prestar atención a lo que dice otra persona"), ("opinión", "lo que yo pienso sobre algo"), ("razón", "motivo de una opinión"), ("atacar", "decir algo para herir a alguien"), ("revisar", "mirar de nuevo para mejorar")],
    worked=[
        W("Escuchar una razón", "Caso inventado: Ana dice que el recreo se debe dividir en turnos. Luis dice que mejor se juega todos juntos porque así nadie queda solo. ¿Qué razón da Luis?", ["Busco la palabra «porque».", "Luis dice que así nadie queda solo.", "Esa es su razón."], "Que así nadie queda solo."),
        W("Responder con respeto", "Luis no está de acuerdo con Ana. ¿Qué frase respeta a Ana? A) «Tu idea es tonta» B) «Entiendo tu idea; yo pienso otra cosa porque…»", ["A ataca a la persona.", "B escucha y da una razón.", "Elijo B."], "B"),
    ],
    mistakes=[
        M("Burlarse de la idea de otra persona.", "Daña su confianza.", "Escucha y responde con respeto."),
        M("Cambiar de opinión solo para no discutir.", "Debe haber una buena razón.", "Cambia si entiendes una razón mejor."),
    ],
    R=[
        ex("Escuchar es prestar atención. ¿Verdadero o falso?", "Verdadero", "Esa es la idea."),
        ex("¿Burlarse de una idea es respetuoso? Sí o No.", "No", "Hiere a la persona."),
        ex("«Yo pienso… porque…» sirve para dar una ______.", "razón", "Después de «porque» va la razón."),
    ],
    C=[
        ex("¿Qué haces primero al escuchar otra opinión? A) la escucho B) la interrumpo", "A", "Escuchar va primero."),
        ex("Verdadero o falso: escuchar a otro significa estar de acuerdo siempre.", "Falso", "Se puede escuchar y pensar distinto."),
        ex("¿Se puede cambiar de opinión con buenas razones?", "Sí", "No es perder, es aprender."),
    ],
    A=[
        ex("Ordena una buena conversación: 1) doy mi razón 2) escucho al otro 3) agradezco.", "2, 1, 3", "Primero escuchar, luego mi razón y agradecer."),
        ex("Elige la frase respetuosa: A) «Qué idea tan tonta» B) «¿Puedes contarme más de tu idea?»", "B", "B invita a entender."),
        ex("Clasifica como RESPETUOSA o NO RESPETUOSA: a) «Entiendo lo que dices» b) «Tú no sabes nada» c) «Yo pienso otra cosa porque…».", "a) respetuosa, b) no respetuosa, c) respetuosa", "Solo b ataca."),
    ],
    Z=[
        ex("Matías se burló de la idea de Camila. ¿Qué podría haber dicho?", "«Entiendo tu idea; yo pienso otra cosa porque…»", "Así no ataca a Camila."),
        ex("¿Por qué no atacamos la identidad de alguien?", "Porque todos merecen respeto", "La identidad es de cada persona."),
    ],
    D=[
        ex("Tres niños opinan: 2 prefieren jugar en grupos y 1 prefiere turnos. ¿Cuántos niños opinan?", "3", "2 + 1 = 3."),
        ex("Después de escuchar, Pedro cambia su opinión porque entendió una razón nueva. ¿Perdió? Sí o No.", "No", "Aprendió algo nuevo."),
    ],
    context=[ex("En un debate inventado, Ana y Luis dan sus razones y ambos escuchan. Al final no se ponen de acuerdo pero se despiden con respeto. ¿Hubo una conversación respetuosa?", "Sí", "Escucharon y no se atacaron.")],
    selfcheck=[ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es escuchar?", "Prestar atención a otra persona", "Es entender su razón."), ex("¿Se ataca a la persona?", "No", "Se respeta a todos."), ex("¿Puedo cambiar de opinión?", "Sí, con razones", "Es parte de aprender.")],
    task=T("Con este diálogo inventado, escribe qué razón dio cada niño y una frase respetuosa para responder. Ana: «Hagamos turnos, así todos juegan». Luis: «Mejor todos juntos, así nadie queda solo». Escribe una frase que empiece con «Entiendo que…».",
           "Ana: así todos juegan. Luis: así nadie queda solo. Frase: «Entiendo que quieren que todos jueguen; yo propongo turnos cortos».",
           ["identifica las razones", "escribe una frase respetuosa", "no ataca"], ["dos razones", "frase"], ["burlarse de una razón"],
           "Valora la frase; si atacó, reformular juntos."),
    reinforce="Practica con alguien la frase «Entiendo que…» y una opinión distinta.",
    extend="Escribe dos frases para pedirle a alguien que te cuente más de su idea.",
)

L(
    OA13, 5,
    materials="Lápiz y hojas. Una tabla de siete casillas está dibujada en el cuaderno.",
    use="Aprenderé a formular un compromiso de acción respetuosa que pueda observarse durante una semana.",
    prior=["Sé qué es un valor.", "Sé qué es un compromiso."],
    explain=[
        "Un compromiso observable es una promesa pequeña que otras personas pueden ver que cumplimos. Por ejemplo: «esta semana saludaré a las personas mayores cuando entre a la sala». No es una promesa vaga como «seré bueno».",
        "Un buen compromiso responde tres preguntas: ¿qué haré?, ¿cuándo? y ¿cómo sabré que lo cumplí? Podemos marcar cada día en una tabla de siete casillas. Así podemos revisar si nos faltó algo.",
        "Elegimos un valor que queramos practicar, como respeto, compartir, agradecer o cuidar. No es necesario contar secretos de la familia. Al final de la semana, contamos qué aprendimos y qué ayuda necesitamos.",
    ],
    vocab=[("compromiso", "promesa de hacer algo"), ("observable", "que otros pueden ver"), ("vago", "poco claro"), ("tabla", "cuadro para anotar"), ("cumplir", "hacer lo prometido")],
    worked=[
        W("Un compromiso claro", "Valor: respeto. ¿Qué compromiso es observable? A) «seré bueno» B) «saludaré a mi profesora cada mañana»", ["A es vago.", "B dice qué haré y cuándo.", "Elijo B."], "B"),
        W("Revisar con la tabla", "Luz marcó 5 días de 7. ¿Cuántos días le faltaron?", ["Resto: 7 − 5.", "Son 2 días.", "Puede mejorar."], "2 días"),
    ],
    mistakes=[
        M("Prometer algo vago como «seré bueno».", "No se puede observar.", "Di qué haré y cuándo."),
        M("Prometer algo muy difícil.", "Se hace difícil cumplir.", "Elige algo pequeño y diario."),
    ],
    R=[
        ex("Observable significa que otros pueden verlo. ¿Verdadero o falso?", "Verdadero", "Eso es observable."),
        ex("¿Cuál es vago? A) «seré bueno» B) «saludaré cada mañana»", "A", "No dice qué haré."),
        ex("Una semana tiene 7 días. ¿Cuántas casillas tiene la tabla?", "7", "Una por día."),
    ],
    C=[
        ex("¿Qué debe decir un buen compromiso? A) qué haré y cuándo B) solo un adjetivo", "A", "Así se puede cumplir."),
        ex("Verdadero o falso: un compromiso puede ser muy difícil.", "Falso", "Debe ser posible."),
        ex("¿Para qué sirve la tabla?", "Para marcar si cumplí cada día", "Así permite revisar."),
    ],
    A=[
        ex("Valor: agradecer. Escribe un compromiso observable.", "Respuesta aceptable: «Diré gracias cada vez que me ayuden»", "Dice qué haré y cuándo."),
        ex("Marca los compromisos observables: a) «diré gracias cuando me ayuden» b) «seré amable» c) «esperaré mi turno en el juego».", "a y c", "La b es vaga."),
        ex("Completa: «Qué haré, ____ y cómo sabré que lo cumplí».", "cuándo", "Las tres preguntas son qué, cuándo y cómo."),
    ],
    Z=[
        ex("Pedro prometió «ser mejor persona». ¿Qué le falta para ser observable?", "Decir qué hará y cuándo", "Debe ser algo que se vea."),
        ex("Rosa cumplió 4 de 7 días. ¿Qué puede hacer para mejorar?", "Buscar un recordatorio y volver a intentarlo", "Es parte de aprender."),
    ],
    D=[
        ex("Una niña cumple su compromiso 6 días de 7. ¿Cuántos días más que 4 cumplió?", "2", "6 − 4 = 2."),
        ex("Un compromiso pide traer una planta cara. ¿Es adecuado para todos? Sí o No.", "No", "No todos pueden hacerlo."),
    ],
    context=[ex("Caso inventado: Ana se comprometió a escuchar sin interrumpir durante el recreo. Marcó 3 días en la tabla. ¿Cuántas casillas están sin marcar?", "4", "7 − 3 = 4.")],
    selfcheck=[ex("¿Qué tres preguntas responde un compromiso?", "Qué haré, cuándo y cómo sabré que lo cumplí", "Lo hacen observable."), ex("¿Es «seré bueno» un compromiso observable?", "No", "Es algo muy vago."), ex("¿Cuántas casillas tiene la tabla?", "7", "Una por día.")],
    task=T("Escribe tu compromiso de la semana con esta forma: «Esta semana yo [acción] cuando [momento]». Puedes elegir: saludar a los mayores al llegar, esperar mi turno, decir gracias cuando me ayuden o guardar mis útiles. Dibuja la tabla de 7 casillas y marca cada día que lo cumplas.",
           "Esta semana yo diré gracias cuando me ayuden. Marqué 5 de 7 días.",
           ["dice qué y cuándo", "se puede observar", "tiene tabla"], ["frase", "tabla de siete casillas"], ["compromiso vago"],
           "Valora lo concreto; si falló un día, reconocer el esfuerzo y volver a intentarlo."),
    reinforce="Practica tu compromiso hoy y marca una casilla.",
    extend="Cuéntale a alguien de confianza tu compromiso y pídele que te recuerde.",
)

# ============================================================ OA 14 · Producción e intercambio ancestral
L(
    OA14, 1,
    materials="Lápiz y hojas. La ficha con datos generales de tres actividades de producción está escrita en el cuaderno.",
    use="Aprenderé a decir cuándo y dónde se realizan actividades de producción (cultivo, crianza, tejido o cerámica) de un pueblo originario, según una fuente.",
    prior=["Sé las estaciones del año.", "Sé que algunos alimentos y objetos se hacen con las manos."],
    explain=[
        "Los pueblos originarios producen alimentos y objetos con su trabajo: cultivan la tierra, crían animales, tejen, hacen cerámica y navegan para pescar. Cada actividad depende del territorio y de la época del año.",
        "Ficha general: el pueblo aymara cría llamas y alpacas y cultiva papas en el altiplano. El pueblo diaguita hace cerámica en los valles del Norte Chico. El pueblo kawésqar navega en canoas por los canales. Cada actividad se hace en un lugar y un tiempo que la comunidad conoce.",
        "Para describirlas decimos: qué se hace, dónde, y cuándo, según una fuente. No inventamos detalles de la técnica ni de las fechas. Si falta un dato, lo anotamos como pregunta para el educador tradicional.",
    ],
    vocab=[("producción", "hacer alimentos u objetos con el trabajo"), ("cultivar", "sembrar y cuidar plantas para cosechar"), ("criar", "cuidar animales"), ("cerámica", "objetos hechos de arcilla"), ("época", "tiempo del año")],
    worked=[
        W("Qué, dónde y cuándo", "Ficha: «" + F_AYM + "» ¿Qué se hace y dónde?", ["Qué: criar llamas y alpacas, cultivar papas.", "Dónde: en el altiplano.", "Cuándo: no lo dice la ficha."], "Criar llamas y alpacas y cultivar papas, en el altiplano."),
        W("Dato que falta", "La ficha no dice en qué mes se siembra. ¿Qué haces?", ["No invento un mes.", "Anoto la pregunta.", "Pregunto a una fuente."], "Anoto la pregunta y pregunto."),
    ],
    mistakes=[
        M("Inventar el mes en que se hace una actividad.", "Puede ser falso.", "Escribe «falta el dato»."),
        M("Decir que todos los pueblos producen lo mismo.", "Cada territorio ofrece cosas distintas.", "Mira la ficha de cada pueblo."),
    ],
    R=[
        ex("Ficha: " + F_AYM + " ¿Qué animales cría?", "Llamas y alpacas", "Lo dice la ficha."),
        ex("Ficha: " + F_DIA + " ¿Qué hace el pueblo diaguita?", "Cerámica", "Lo dice la ficha."),
        ex("Ficha: " + F_KAW + " ¿En qué navega?", "En canoas", "La ficha lo dice."),
    ],
    C=[
        ex("Cultivar es sembrar y cuidar plantas. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
        ex("¿Qué depende el trabajo de un pueblo? A) del territorio y la época B) de nada", "A", "Cada lugar ofrece cosas distintas."),
        ex("Si falta un dato, ¿qué haces?", "Lo anoto como pregunta", "No se inventa."),
    ],
    A=[
        ex("Une pueblo y actividad. 1) aymara 2) diaguita 3) kawésqar. a) cerámica b) criar llamas c) navegar en canoas", "1-b, 2-a, 3-c", "Está en las fichas."),
        ex("Ficha: " + F_AYM + " Escribe una frase con «qué» y «dónde».", "Respuesta aceptable: «Cultiva papas en el altiplano»", "Incluye qué y dónde."),
        ex("Marca los datos que NO están en la ficha aymara: llamas, mar, papas, canoas.", "mar y canoas", "La ficha no los menciona."),
    ],
    Z=[
        ex("Ana dice que el pueblo diaguita cría llamas en el altiplano. ¿Qué error comete?", "Mezcla las fichas", "La ficha diaguita habla de valles y cerámica."),
        ex("¿Por qué las actividades cambian según el territorio?", "Porque cada lugar ofrece cosas distintas", "Hay desierto, valle, mar, altiplano."),
    ],
    D=[
        ex("Una niña dice que en la ficha kawésqar hay cultivo de papas. ¿Es cierto? Sí o No.", "No", "La ficha habla de canoas y canales."),
        ex("En una feria hay 3 cestos de papas y 2 de otros alimentos. ¿Cuántos cestos hay?", "5", "3 + 2 = 5."),
    ],
    context=[ex("En tu ficha hay tres actividades: criar, hacer cerámica y navegar. Si cada una tiene dos preguntas pendientes, ¿cuántas preguntas hay en total?", "6", "Se suma 2 + 2 + 2 = 6 preguntas.")],
    selfcheck=[ex("¿Qué es cultivar?", "Sembrar y cuidar plantas", "Es producir alimentos."), ex("¿Qué haces si falta un dato?", "Lo anoto como pregunta", "No se inventa."), ex("¿Qué pueblo hace cerámica según la ficha?", "El pueblo diaguita", "La ficha lo dice.")],
    task=T("Elige una de las tres fichas (aymara, diaguita o kawésqar) y dibuja el lugar y la actividad. Escribe «Qué se hace», «Dónde» y «Cuándo (pregunta pendiente)». Escribe una pregunta para el educador tradicional sobre cuándo se realiza.",
           "Elegí diaguita. Qué: cerámica. Dónde: valles del Norte Chico. Cuándo: pregunta pendiente. Pregunta: ¿en qué época se hace la cerámica?",
           ["usa la ficha", "separa qué, dónde y cuándo", "deja una pregunta pendiente"], ["dibujo", "tres frases", "pregunta"], ["inventar la época"],
           "Valora la pregunta pendiente; si inventó la época, reconvertir en pregunta."),
    reinforce="Une con flechas el pueblo y su actividad.",
    extend="Pregunta a una persona mayor qué productos hacía o consumía su familia en cada estación.",
)

L(
    OA14, 2,
    materials="Lápiz y hojas. Una ficha general de lana está escrita en el cuaderno.",
    use="Aprenderé de dónde vienen los materiales que se usan para producir y cómo se cuidan.",
    prior=["Sé que las lanas vienen de animales.", "Sé que la arcilla viene de la tierra."],
    explain=[
        "Para producir se necesitan insumos, es decir, materiales. La lana viene de animales como las ovejas, las llamas o las alpacas. La arcilla viene de la tierra. El agua, la leña y las fibras vegetales también son insumos.",
        "Los insumos tienen procedencia, que es dónde y cómo se obtienen. Muchas comunidades cuidan los lugares de donde sacan sus insumos: toman solo lo necesario, para que haya también en el futuro. Eso es cuidar el territorio.",
        "Antes de usar un insumo, se prepara. La lana se lava, se hila y a veces se tiñe; la arcilla se amasa y se limpia. Cada comunidad enseña sus formas de preparar, y no las inventamos. Aquí aprendemos los pasos generales.",
    ],
    vocab=[("insumo", "material que se usa para producir algo"), ("procedencia", "dónde y cómo se obtiene algo"), ("lana", "pelo de animales que se hila para tejer"), ("arcilla", "tierra blanda que se moldea"), ("preparar", "dejar listo un material para usarlo")],
    worked=[
        W("Reconocer el insumo", "Quieres hacer un tejido. ¿Qué insumo necesitas y de dónde viene?", ["Necesito lana.", "La lana viene de animales como ovejas, llamas o alpacas.", "Hay que cuidarlos."], "Lana, que viene de animales."),
        W("Tomar solo lo necesario", "Una comunidad necesita 4 ovillos de lana y tiene 6. ¿Cuántos puede guardar?", ["Resto lo que usa.", "6 − 4 = 2.", "Guarda 2."], "2 ovillos"),
    ],
    mistakes=[
        M("Pensar que los insumos aparecen sin cuidado.", "Vienen de animales, plantas o tierra que se cuidan.", "Pregunta de dónde vienen."),
        M("Inventar cómo se prepara un material tradicional.", "Cada comunidad tiene sus formas.", "Usa solo los pasos generales y pregunta."),
    ],
    R=[
        ex("La lana viene de animales. ¿Verdadero o falso?", "Verdadero", "Viene de ovejas, llamas o alpacas."),
        ex("La arcilla viene de la tierra. ¿Verdadero o falso?", "Verdadero", "Es una tierra blanda."),
        ex("Un insumo es un material para producir. ¿Verdadero o falso?", "Verdadero", "Esa es la definición."),
    ],
    C=[
        ex("¿Qué es la procedencia? A) dónde y cómo se obtiene un material B) su color", "A", "Eso es procedencia."),
        ex("¿Por qué se toma solo lo necesario? A) para que haya en el futuro B) para gastar más", "A", "Así se cuida el territorio."),
        ex("Verdadero o falso: la lana se usa tal cual sale del animal.", "Falso", "Se lava y se hila antes."),
    ],
    A=[
        ex("Une insumo y procedencia. 1) lana 2) arcilla 3) agua. a) tierra b) animal c) río o vertiente", "1-b, 2-a, 3-c", "Cada insumo tiene su fuente."),
        ex("Ordena la preparación de la lana: 1) hilar 2) lavar 3) tejer.", "2, 1, 3", "Se lava, se hila y se teje."),
        ex("Necesitas 3 ovillos y tienes 5. ¿Cuántos sobran?", "2", "5 − 3 = 2."),
    ],
    Z=[
        ex("Beto sacó toda la arcilla de un lugar para tener de sobra. ¿Qué error cometió?", "Tomó más de lo necesario", "No cuidó el lugar."),
        ex("¿Por qué preguntamos de dónde viene un insumo?", "Para saber cómo cuidarlo", "Conocer la procedencia ayuda a cuidar."),
    ],
    D=[
        ex("Una familia usa 3 ovillos por manta. ¿Cuántos ovillos necesita para 2 mantas?", "6", "Se suma 3 + 3 = 6."),
        ex("Una niña dice que cada comunidad prepara la lana igual. ¿Es seguro? Sí o No.", "No", "Hay formas propias."),
    ],
    context=[ex("En una familia, la abuela hila un ovillo por día durante 5 días. ¿Cuántos ovillos hay?", "5", "5 días × 1 ovillo = 5.")],
    selfcheck=[ex("¿Qué es un insumo?", "Un material para producir", "Es la materia prima."), ex("¿De dónde viene la lana?", "De animales", "Ovejas, llamas, alpacas."), ex("¿Por qué se toma solo lo necesario?", "Para cuidar el territorio", "Así hay para el futuro.")],
    task=T("Elige un objeto de esta lista: un tejido de lana, una olla de arcilla o una canasta de fibras. Dibuja el objeto y escribe su insumo, de dónde viene y una forma de cuidar ese insumo. No escribas técnicas especiales; pregunta cómo lo hace la comunidad.",
           "Objeto: tejido de lana. Insumo: lana. Viene de animales como las llamas. Se cuida tomando solo la que se necesita.",
           ["nombra el insumo", "dice la procedencia", "propone cuidado"], ["dibujo", "tres frases"], ["inventar técnicas"],
           "Valora el cuidado; recordar que las técnicas las enseña la comunidad."),
    reinforce="Une cada objeto con su insumo.",
    extend="Escribe una pregunta sobre cómo se obtiene un material en una comunidad.",
)

L(
    OA14, 3,
    materials="Lápiz y hojas. Un proceso general está escrito en el cuaderno.",
    use="Aprenderé a ordenar los pasos y herramientas de un proceso de producción de forma general, sin inventar técnicas.",
    prior=["Sé ordenar pasos.", "Sé qué es una herramienta."],
    explain=[
        "Un proceso es una secuencia de pasos para hacer algo. Para producir un tejido, un proceso general es: obtener la lana, lavarla, hilarla y tejerla. Para la cerámica, un proceso general es: preparar la arcilla, modelarla, secarla y cocerla.",
        "En cada paso se usan herramientas. Por ejemplo, para hilar se usa un huso; para tejer, un telar. Cada comunidad tiene sus propios modos de hacerlo, y los conoce bien. Nosotros solo aprendemos el orden general.",
        "No debemos inventar ni mezclar técnicas. Si queremos saber cómo lo hace una comunidad, pedimos al educador tradicional o al artesano o artesana que nos enseñe. También pedimos permiso antes de dibujar o fotografiar su trabajo.",
    ],
    vocab=[("proceso", "pasos que se siguen para hacer algo"), ("herramienta", "objeto que ayuda a trabajar"), ("hilar", "convertir la lana en hilo"), ("telar", "armazón donde se teje"), ("secuencia", "pasos en orden")],
    worked=[
        W("Ordenar el proceso", "Ordena: tejer, lavar la lana, hilar. ¿Cuál es el orden?", ["Primero se lava.", "Luego se hila.", "Al final se teje."], "Lavar, hilar, tejer."),
        W("Herramienta por paso", "Une el paso con la herramienta: hilar y tejer. Herramientas: huso, telar.", ["Hilar se hace con huso.", "Tejer se hace en telar.", "Uno a uno."], "Hilar-huso; tejer-telar."),
    ],
    mistakes=[
        M("Cambiar el orden de los pasos.", "El resultado no sale.", "Revisa la secuencia."),
        M("Inventar una técnica de un pueblo.", "Cada comunidad tiene la suya.", "Pregunta al artesano o educador."),
    ],
    R=[
        ex("Un proceso es una secuencia de pasos. ¿Verdadero o falso?", "Verdadero", "Eso es proceso."),
        ex("Una herramienta es un objeto que ayuda a trabajar. ¿Verdadero o falso?", "Verdadero", "Eso es herramienta."),
        ex("¿Qué va primero: hilar o lavar la lana?", "Lavar la lana", "Primero se limpia."),
    ],
    C=[
        ex("Orden general de un tejido: A) lavar, hilar, tejer B) tejer, hilar, lavar", "A", "El tejido se arma al final."),
        ex("Verdadero o falso: el huso se usa para hilar.", "Verdadero", "Es la herramienta del hilado."),
        ex("¿Dónde se teje en este proceso general?", "En un telar", "El telar es la herramienta del tejido."),
    ],
    A=[
        ex("Ordena el proceso de la cerámica: 1) cocer 2) modelar 3) preparar la arcilla 4) secar.", "3, 2, 4, 1", "Se prepara, se modela, se seca y se cuece."),
        ex("Une paso y herramienta. 1) hilar 2) tejer. a) telar b) huso", "1-b, 2-a", "Huso para hilar y telar para tejer."),
        ex("Un tejido necesita 4 pasos: obtener lana, lavarla, hilarla y tejerla. Si ya hiciste 2, ¿cuántos faltan?", "2", "4 − 2 = 2."),
    ],
    Z=[
        ex("Luz tejió antes de hilar. ¿Qué pasó?", "No tenía hilo", "El hilo se hace antes de tejer."),
        ex("¿Por qué no inventamos técnicas de una comunidad?", "Porque las conoce quien las practica", "Cada comunidad tiene su saber."),
    ],
    D=[
        ex("Una artesana teje 2 mantas al mes. ¿Cuántas mantas teje en 3 meses?", "6", "Se suma 2 + 2 + 2 = 6."),
        ex("Un libro describe un proceso distinto al que cuenta una artesana. ¿Qué haces?", "Pregunto y anoto las dos fuentes", "Puede haber diferencias."),
    ],
    context=[ex("Una familia hila 3 ovillos el lunes y 2 el martes. ¿Cuántos ovillos hay?", "5", "3 + 2 = 5.")],
    selfcheck=[ex("¿Qué es un proceso?", "Pasos en orden", "Es una secuencia."), ex("¿Qué herramienta se usa para tejer?", "El telar", "Es donde se teje."), ex("¿Qué hago si no sé la técnica?", "Pregunto al artesano o educador", "Ellos saben hacerlo.")],
    task=T("Dibuja el proceso general del tejido en 4 cuadros: obtener lana, lavarla, hilarla y tejerla. Escribe debajo el nombre del paso y la herramienta (huso o telar). Escribe una pregunta para un artesano sobre su técnica.",
           "Cuadro 1: lana. Cuadro 2: lavar. Cuadro 3: hilar con huso. Cuadro 4: tejer en telar. Pregunta: ¿cómo prepara usted la lana?",
           ["ordena bien los pasos", "nombra herramientas", "formula una pregunta"], ["4 cuadros", "pregunta"], ["cambiar el orden"],
           "Revisa el orden; si inventó técnicas, volver a leer la explicación."),
    reinforce="Ordena tres pasos de una receta de tu casa.",
    extend="Escribe una pregunta para un artesano sobre cómo aprendió su oficio.",
)

L(
    OA14, 4,
    materials="Lápiz y hojas. Un caso de trueque inventado está escrito en el cuaderno.",
    use="Aprenderé cómo circulan los productos entre comunidades y para qué sirven, incluyendo el trueque.",
    prior=["Sé qué es comprar y vender.", "Sé qué es dar algo a cambio de otra cosa."],
    explain=[
        "Los productos no solo se hacen: también circulan, es decir, pasan de unas personas a otras. En muchos pueblos andinos existió el trueque, que es cambiar un producto por otro sin usar dinero, como cambiar papas por lana.",
        "El intercambio permite que cada comunidad tenga cosas que su territorio no produce. Una comunidad del altiplano puede tener lana y otra de un valle, fruta. Intercambian y las dos ganan. Algunos lo hacen en ferias, otros entre familias.",
        "El uso también importa: los productos sirven para alimentar, abrigar, ayudar en el trabajo o celebrar. Un intercambio justo es el que beneficia a ambas partes y respeta lo acordado.",
    ],
    vocab=[("intercambio", "dar algo y recibir otra cosa"), ("trueque", "cambiar un producto por otro sin dinero"), ("circular", "pasar de unas personas a otras"), ("feria", "lugar donde se reúnen a intercambiar o vender"), ("justo", "que beneficia a las dos partes")],
    worked=[
        W("Trueque", "Caso inventado: Ana cambia 3 kilos de papas por 2 ovillos de lana. ¿Es trueque?", ["Hay dos productos.", "No se usa dinero.", "Es trueque."], "Sí."),
        W("Intercambio justo", "Dos familias cambian lana por fruta y ambas quedan conformes. ¿Es justo?", ["Ambas ganan.", "Respetaron lo acordado.", "Es justo."], "Sí."),
    ],
    mistakes=[
        M("Pensar que el trueque es regalar.", "Se da y se recibe algo.", "Piensa en lo que cada parte entrega y recibe."),
        M("Creer que el intercambio es solo con dinero.", "También se hace con trueque.", "Recuerda las dos formas."),
    ],
    R=[
        ex("Trueque es cambiar un producto por otro sin dinero. ¿Verdadero o falso?", "Verdadero", "Eso es trueque."),
        ex("Caso inventado: cambias papas por lana. ¿Usas dinero? Sí o No.", "No", "Es un trueque."),
        ex("Intercambio es dar algo y recibir otra cosa. ¿Verdadero o falso?", "Verdadero", "Esa es la idea."),
    ],
    C=[
        ex("¿Para qué sirve el intercambio? A) para tener lo que mi territorio no produce B) para perder cosas", "A", "Amplía lo que tengo."),
        ex("Verdadero o falso: un intercambio justo beneficia a las dos partes.", "Verdadero", "Eso es justo."),
        ex("¿Qué puede ser una feria?", "Un lugar para intercambiar o vender", "Reúne a las personas."),
    ],
    A=[
        ex("Caso inventado: Beto cambia 1 queso por 2 ovillos de lana. ¿Cuántos ovillos recibe por 2 quesos?", "4", "Se suma 2 + 2 = 4 ovillos."),
        ex("Une producto y uso. 1) lana 2) papas 3) cerámica. a) abrigar b) alimentar c) guardar o servir alimentos", "1-a, 2-b, 3-c", "Cada producto tiene un uso."),
        ex("Ordena un trueque: 1) acordar 2) intercambiar 3) agradecer.", "1, 2, 3", "Se acuerda, se cambia y se agradece."),
    ],
    Z=[
        ex("Pedro dio 1 papa y pidió 10 ovillos. La otra persona se negó. ¿Fue justo? Sí o No.", "No", "No benefició a ambas partes."),
        ex("¿Por qué el intercambio ayuda a las comunidades?", "Porque cada una consigue lo que no produce", "Todas reciben algo útil."),
    ],
    D=[
        ex("Caso inventado: una familia cambia 2 kilos de papas por 1 ovillo. ¿Cuántos kilos da por 3 ovillos?", "6", "Se suma 2 + 2 + 2 = 6 kilos."),
        ex("Un libro dice que el trueque se hacía igual en todos los pueblos. ¿Qué cuidado tienes?", "Revisar la fuente y evitar generalizar", "Cada pueblo tiene sus formas."),
    ],
    context=[ex("En una feria inventada hay 5 puestos de lana, 3 de papas y 2 de cerámica. ¿Cuántos puestos hay?", "10", "5 + 3 + 2 = 10.")],
    selfcheck=[ex("¿Qué es el trueque?", "Cambiar un producto por otro sin dinero", "No hay dinero."), ex("¿Qué es un intercambio justo?", "Uno que beneficia a ambas partes", "Ambas partes ganan."), ex("¿Para qué sirve una feria?", "Para intercambiar o vender", "Reúne a las personas.")],
    task=T("Con este caso inventado, completa la tabla: «Una familia del altiplano tiene lana y quiere fruta. Una familia de un valle tiene fruta y quiere lana.» Escribe: qué da cada familia, qué recibe, para qué sirve cada producto y por qué es un intercambio justo. Escribe una pregunta para el educador tradicional sobre cómo circulan los productos en su comunidad.",
           "Familia altiplano: da lana, recibe fruta. Familia valle: da fruta, recibe lana. Lana abriga y fruta alimenta. Es justo porque ambas ganan.",
           ["dice lo que da y recibe cada una", "dice para qué sirve", "justifica que es justo"], ["tabla", "pregunta"], ["decir que una familia pierde"],
           "Valora la justificación; recordar que el caso es inventado y no describe a un pueblo en particular."),
    reinforce="Haz un trueque de dibujos con un compañero.",
    extend="Pregunta a una persona mayor si se hacía trueque en su familia o comunidad.",
)
