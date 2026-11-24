"""Lengua y Literatura EPJA Media Nivel 1, módulo 2 (parte 2): OAD-06, analizar los recursos lingüísticos de un texto para identificar sus propósitos explícitos e inferir los implícitos. Todos los textos son inventados y se leen en papel."""
from __future__ import annotations

from epja_leli_nm1_b_common import build

O = "EPJA-LELI-NM1-OAD-06"

F1 = ("Texto A (inventado), etiqueta de un limpiador de ejemplo: «Diluya una tapa en un litro de agua. No lo mezcle con otros productos. Guárdelo lejos del alcance de las niñas y los niños.» "
      "Texto B (inventado), volante de una tienda de ejemplo: «Solo este fin de semana: 20 % de descuento en todas las ollas. ¡No te quedes sin la tuya!» "
      "Texto C (inventado), cartel de la municipalidad de ejemplo: «El punto limpio atenderá los sábados de 10:00 a 14:00. Reciclar es tarea de todos.»")

F2 = ("Texto (inventado), afiche de un instituto de ejemplo: «¿Quieres cambiar tu vida? ¡Inscríbete ya! Nuestro curso de soldadura es el mejor, el más completo y el más cómodo. "
      "Más de 500 personas ya aprendieron un oficio con nosotros. Tú también puedes. Los cupos son limitados, así que no lo pienses más.»")

F3 = ("Aviso (inventado) de una tienda de electrodomésticos de ejemplo: «¡Tu refrigerador te espera! Llévalo hoy por solo $9.990 al mes, sin pie y sin esperas. ¡Qué tranquilidad para tu familia!» "
      "Letra pequeña del mismo aviso: «Plan de 12 cuotas mensuales. Precio al contado: $99.900.»")

F4 = ("Mensaje A (inventado): «Doña Rosa, usuaria desde hace años, dice: «Con este jarabe de ejemplo mi casa se llenó de energía». Pruébalo tú también.» "
      "Mensaje B (inventado): «Nueve de cada diez familias del pasaje ya compraron este calefactor. ¡No te quedes atrás!» "
      "Mensaje C (inventado): «Últimas dos unidades en bodega. La oferta termina hoy a las 20:00.» "
      "Mensaje D (inventado): «Un médico de renombre recomienda este producto de ejemplo.» "
      "Mensaje E (inventado): «Piensa en tus hijos: ¿vas a dejarlos sin abrigo este invierno?»")

F5 = ("Volante A (inventado), comité de vecinos «Los Aromos»: «Vecina, vecino: nuestra plaza es de todos. El domingo 22, de 10:00 a 13:00, limpiaremos la plaza y pintaremos las bancas. Traiga guantes y bolsas si puede. ¿Nos ayuda? Entre todos se hace más liviano.» "
      "Mensaje B (inventado), recibido en un teléfono de un número desconocido: «¡Gana $300.000 a la semana trabajando desde tu casa! Sin experiencia, sin horarios. Solo debes depositar $20.000 hoy para recibir tu kit. Quedan pocos cupos.»")

F6 = ("Afiche (inventado) de una tienda de ejemplo, descrito en palabras: fondo amarillo intenso; la palabra OFERTA en letras rojas enormes que ocupan la mitad del afiche; una fotografía de una familia sonriente junto a una cocina nueva; "
      "el precio «$199.990» en tamaño grande; y, al pie, en letras muy pequeñas y grises: «Válido hasta agotar stock. Precio con tarjeta de la tienda. Consulte condiciones en sala».")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy distingo el propósito explícito del propósito implícito de un texto y reconozco para qué se escribe cada uno.",
    prior=["Reconozco emisor y receptor.", "Sé que los textos se escriben para algo.", "Leo etiquetas, volantes y carteles."],
    explain=[
        "Los textos se escriben con un propósito. Algunos informan, otros dan instrucciones, otros buscan convencer, entretener o expresar lo que alguien siente. Tú ya lo notas cuando lees una receta y cuando lees un volante de una tienda.",
        "El propósito explícito es el que el texto declara con claridad, por ejemplo «este fin de semana hay 20 % de descuento». El propósito implícito es el que no se dice, pero se puede inferir con pistas, por ejemplo que compres pronto y en esa tienda.",
        "Inferir es llegar a una idea usando las pistas del texto y lo que ya sabes. Para inferir un propósito, pregunta: ¿qué dice el texto?, ¿qué palabras elige?, ¿qué quiere que yo haga o piense después de leerlo?",
    ],
    vocab=[("propósito explícito", "el que el texto dice abiertamente"), ("propósito implícito", "el que no se dice, pero se puede deducir de las pistas"), ("instruir", "explicar cómo hacer algo"), ("inferir", "llegar a una idea usando pistas del texto")],
    worked=[
        ("Propósito explícito", "Texto (inventado): «Lave las manos con agua y jabón durante 20 segundos antes de preparar alimentos.»", ["Veo un verbo en modo mandato: «lave».", "Explica qué hacer y cómo."], "Propósito explícito: instruir"),
        ("Propósito implícito", "Texto (inventado): «Último día de ofertas: la mejor ocasión del año».", ["Dice que es el último día: invita a no esperar.", "Quiere que la persona compre pronto."], "Propósito implícito: persuadir para que compre"),
    ],
    mistakes=[("Creer que todo texto solo informa.", "Muchos textos informan y a la vez buscan convencer.", "Pregunta qué quiere que hagas o pienses el emisor."),
              ("Tomar una pista como si fuera el propósito completo.", "Una palabra aislada no basta: hay que mirar varias pistas.", "Junta dos o tres pistas del texto antes de concluir.")],
    T=[
        ("abc", "{F} ¿Cuál es el propósito explícito del Texto A?", "Instruir sobre cómo usar el producto y qué precauciones tomar", "Contar una historia sobre el limpiador", "Convencer de que es el mejor producto", "Entrega instrucciones de uso y advertencias."),
        ("ab", "{F} ¿Qué texto pide hacer algo con urgencia?", "El Texto B, que dice «solo este fin de semana»", "El Texto A, que da instrucciones", "La expresión «solo este fin de semana» limita el tiempo para actuar."),
        ("{F} ¿Qué porcentaje de descuento anuncia el Texto B? Escribe solo el número.", "20", "El Texto B anuncia un 20 % de descuento."),
        ("abc", "{F} ¿Cuál es el propósito explícito del Texto B?", "Informar de un descuento en ollas durante el fin de semana", "Dar instrucciones para cocinar", "Pedir ayuda para limpiar una plaza", "Declara el descuento y el plazo."),
        ("abc", "{F} ¿Cuál es un propósito implícito del Texto B?", "Que la persona compre pronto en esa tienda", "Que la persona recicle", "Que la persona lave las ollas con cuidado", "La urgencia sugiere que compres antes de que termine la oferta."),
        ("abc", "{F} ¿Cuál es el propósito explícito del Texto C?", "Informar los días y horarios del punto limpio", "Vender un producto", "Contar un hecho del pasado", "Entrega los días y el horario de atención del lugar."),
        ("ab", "{F} La frase «Reciclar es tarea de todos» del Texto C, ¿qué propósito implícito sugiere?", "Motivar a las personas a reciclar", "Informar solo un horario", "La frase invita a participar, más allá del horario."),
        ("ab", "{F} ¿En cuál texto el propósito explícito y el implícito son casi iguales?", "En el Texto A, porque solo instruye", "En el Texto B, porque vende sin decirlo", "Las instrucciones y precauciones de A no ocultan otro propósito."),
        ("abc", "Lee: «Recuerde llevar su carné. Sin carné no se podrá retirar su pedido». ¿Cuál es el propósito explícito?", "Advertir qué documento llevar para retirar", "Convencer de comprar", "Entretener a quien lee", "Dice qué documento se necesita y qué pasa si no se lleva."),
        ("abc", "Lee: «Millones de personas ya usan nuestra aplicación; ¿y tú?». ¿Qué propósito implícito tiene?", "Convencer de usar la aplicación", "Enseñar a programar", "Contar una historia", "Usa a otras personas para empujar a usarla."),
        ("ab", "Camila dice que un cartel que informa horarios no tiene propósito implícito alguno. ¿Siempre es así?", "No: puede tener también un propósito implícito, como motivar a participar", "Sí: informar nunca persuade", "Un texto informativo puede, al mismo tiempo, buscar convencer."),
        ("abc", "{F} Si la tienda del Texto B dijera «20 % de descuento, hasta el 30 de este mes», ¿qué cambiaría en el propósito implícito?", "Habría menos presión por comprar de inmediato", "Pasaría a ser un texto instructivo", "Ya no sería un volante", "Un plazo más largo reduce la urgencia."),
        ("ab", "{F} Un amigo dice: «El Texto C solo informa horarios». ¿Qué respuesta es más completa?", "También anima a reciclar, porque dice que es tarea de todos", "Tiene razón: no hay nada más", "El segundo mensaje busca despertar compromiso."),
    ],
    ctx=("abc", "En un pasillo del trabajo ves este cartel (inventado): «Lávese las manos antes de volver al puesto. Cuidarnos es cosa de todos». ¿Cuál es el propósito explícito?", "Indicar que hay que lavarse las manos antes de volver al puesto", "Vender jabón", "Contar una historia de la empresa", "La primera frase da una instrucción clara."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es un propósito explícito?", "El que el texto declara abiertamente", "Lo explícito está dicho con claridad."),
        ("En Lengua y Literatura de EPJA: ¿qué es un propósito implícito?", "El que no se dice, pero se infiere de las pistas", "Lo implícito no se dice, pero se deduce con pistas."),
        ("En Lengua y Literatura de EPJA: ¿qué significa inferir?", "Llegar a una idea usando pistas del texto", "Inferir une pistas del texto con lo que ya sabes.")],
    op=("Lee los tres textos: {F} Elige el que más te llame la atención y escribe en tu cuaderno su propósito explícito, un propósito implícito y las dos pistas del texto que usaste para inferirlo.",
        "Texto B: explícito, informar un descuento en ollas. Implícito, que compres pronto en esa tienda. Pistas: «solo este fin de semana» y «¡No te quedes sin la tuya!».",
        ["distingue propósito explícito e implícito", "cita dos pistas del texto", "justifica su inferencia"],
        ["tres frases y dos citas"],
        ["decir que el propósito implícito es igual al explícito sin pistas", "no citar el texto"],
        "Pregunta: «¿Qué pista del texto te hace pensar eso?»."),
    reinforce="Mira un volante o un aviso de tu barrio y escribe qué dice y qué quiere que hagas.",
    extend="Escribe un aviso de dos líneas con un propósito explícito y otro implícito, y pide a otra persona que los descubra.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy reconozco recursos lingüísticos, como adjetivos que valoran, preguntas dirigidas al lector y repeticiones, y para qué se usan.",
    prior=["Distingo propósito explícito e implícito.", "Sé reconocer verbos y adjetivos.", "Leo afiches y volantes."],
    explain=[
        "Los recursos lingüísticos son las decisiones de lenguaje que toma quien escribe para lograr su propósito. Tú los has oído muchas veces: una pregunta que parece hablarte, un adjetivo que alaba, una frase que se repite.",
        "Algunos recursos frecuentes son: el adjetivo valorativo («el mejor»); el superlativo («el más completo»); la pregunta dirigida al lector («¿quieres cambiar tu vida?»); el mandato («inscríbete ya»); el uso de «tú» o «nosotros»; la cifra; y el verbo que mide la posibilidad («puedes», «podría»).",
        "Cada recurso produce un efecto. La pregunta atrae la atención; el superlativo exagera una cualidad; la cifra da apariencia de respaldo; el mandato apura. Reconocer el recurso y su efecto es el primer paso para evaluar un texto con cuidado.",
    ],
    vocab=[("adjetivo valorativo", "palabra que califica algo con un juicio, como «bueno» o «mejor»"), ("superlativo", "forma que expresa el grado más alto de una cualidad, como «el más cómodo»"), ("pregunta dirigida al lector", "pregunta que se hace al lector para llamar su atención"), ("modo imperativo", "forma verbal que da órdenes o invitaciones, como «inscríbete»")],
    worked=[
        ("Reconocer un recurso", "Frase (inventada): «Nuestro café es el más rico del barrio».", ["Busco una palabra que valora: «rico».", "Veo la forma «el más rico»: es un superlativo."], "Recurso: superlativo y adjetivo valorativo"),
        ("Reconocer el efecto", "Frase (inventada): «¿Cansada de pagar de más? ¡Cambia hoy!»", ["Hay una pregunta dirigida al lector.", "Hay un mandato: «cambia»."], "Efecto: atraer la atención y apurar a la persona"),
    ],
    mistakes=[("Confundir un adjetivo valorativo con un dato.", "«El mejor» expresa un juicio y no se puede comprobar como una cifra.", "Pregunta si se puede medir; si no, es un juicio."),
              ("Pensar que una cifra siempre prueba algo.", "Una cifra sin fuente solo da una impresión de respaldo.", "Pregunta de dónde sale el número y cuándo se midió.")],
    T=[
        ("abc", "{F} ¿Qué recurso es «¿Quieres cambiar tu vida?»?", "Una pregunta dirigida al lector", "Una cifra", "Un dato histórico", "La pregunta interpela directamente a quien lee el afiche."),
        ("ab", "{F} ¿Qué recurso es «Inscríbete ya»?", "Un mandato, que apura a actuar", "Un adjetivo valorativo", "El verbo inscríbete es una orden que invita a actuar de inmediato."),
        ("{F} ¿Cuántas personas dice el afiche que ya aprendieron un oficio? Escribe solo el número.", "500", "El afiche dice «más de 500 personas»."),
        ("abc", "{F} ¿Qué expresión es un superlativo?", "«el más completo»", "«soldadura»", "«500 personas»", "«Más» más un adjetivo expresa el grado más alto."),
        ("ab", "{F} ¿«El mejor» es un hecho o un juicio?", "Un juicio, porque no se puede medir sin criterios", "Un hecho, porque está en el afiche", "Se necesita un criterio para decir que algo es mejor."),
        ("abc", "{F} ¿Qué efecto busca la cifra «más de 500 personas»?", "Dar apariencia de respaldo al curso", "Informar la dirección del instituto", "Pedir una opinión al lector", "Una cifra grande sugiere que el curso ya funcionó."),
        ("abc", "{F} ¿Qué efecto busca la frase «los cupos son limitados»?", "Hacer sentir que hay que decidir rápido", "Explicar cómo se suelda", "Anunciar un descuento", "Sugiere que si esperas puedes perder el cupo."),
        ("abc", "{F} ¿Qué pronombre usa el afiche para acercarse al lector?", "«Tú»", "«Ellos»", "«Usted»", "El afiche dice «tú también puedes», dirigido al lector."),
        ("ab", "{F} ¿Qué dato del afiche se podría comprobar pidiendo información al instituto?", "Cuántas personas han terminado el curso", "Que el curso es el más cómodo", "La cantidad es un dato; «el más cómodo» es un juicio."),
        ("abc", "Lee: «Podrías ahorrar mucho». ¿Qué recurso aparece?", "Un verbo que expresa posibilidad, sin asegurar nada", "Una orden directa", "Una cifra exacta", "«Podrías» indica una posibilidad, no un hecho."),
        ("abc", "Lee: «Cada día, cada hora, cada minuto: ¡aprovecha!». ¿Qué recurso se repite?", "La palabra «cada»", "La palabra «aprovecha»", "La palabra «día»", "«Cada» se repite tres veces para dar ritmo y énfasis."),
        ("ab", "Un afiche dice: «Tú puedes». Otro: «Los estudiantes pueden». ¿Cuál se dirige más directamente al lector?", "El primero, porque usa «tú»", "El segundo, porque usa un sustantivo", "El pronombre «tú» interpela a quien lee."),
        ("abc", "{F} Si el afiche borrara «el mejor, el más completo y el más cómodo», ¿qué pasaría con el texto?", "Perdería sus juicios y sería más informativo", "Se volvería un poema", "Dejaría de ser un afiche", "Esas expresiones son valoraciones y no datos comprobables."),
    ],
    ctx=("abc", "En un diario mural de tu trabajo ves el cartel (inventado): «¿Te cuesta llegar a fin de mes? ¡Ahorra con nosotros! La mejor cooperativa, la más segura». ¿Cuál es un adjetivo valorativo?", "«la mejor»", "«cooperativa»", "«mes»", "«Mejor» expresa un juicio sobre la cooperativa."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es un adjetivo valorativo?", "Una palabra que califica algo con un juicio", "El adjetivo valorativo expresa una opinión."),
        ("En Lengua y Literatura de EPJA: ¿para qué sirve una pregunta dirigida al lector?", "Para llamar su atención y hacerlo sentir aludido", "La pregunta interpela a quien lee."),
        ("En Lengua y Literatura de EPJA: ¿qué efecto tiene un superlativo?", "Exagerar la cualidad de algo", "El superlativo expresa el grado más alto.")],
    op=("Lee el afiche: {F} Escribe en tu cuaderno tres recursos lingüísticos que encuentres, con una cita del afiche para cada uno y el efecto que producen. Después reescribe la primera frase del afiche para que informe sin exagerar.",
        "Recursos: pregunta dirigida al lector («¿Quieres cambiar tu vida?»): atrae la atención. Superlativo («el más completo»): exagera. Cifra («más de 500 personas»): da respaldo. Reescritura: «El instituto ofrece un curso de soldadura; consulte el programa y las fechas de inscripción».",
        ["identifica tres recursos con cita", "explica el efecto de cada uno", "reescribe sin exagerar"],
        ["tres recursos con cita y una frase nueva"],
        ["nombrar el recurso sin citar", "reescribir con otros superlativos"],
        "Pregunta: «¿Qué efecto busca cada recurso en quien lee?»."),
    reinforce="Busca en un volante tres palabras que valoren algo y subraya la que más exagera.",
    extend="Escribe cuatro frases sobre tu oficio, una con superlativo, una con pregunta, una con cifra y una con mandato, y explica el efecto de cada una.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy sigo, paso a paso, una pauta para inferir el propósito implícito de un texto a partir de sus recursos.",
    prior=["Reconozco recursos como superlativos, preguntas y mandatos.", "Distingo propósito explícito e implícito.", "Sé multiplicar."],
    explain=[
        "Para inferir el propósito implícito de un texto puedes seguir cinco pasos. Primero, lee completo, incluso la letra pequeña. Segundo, subraya los recursos lingüísticos. Tercero, anota el efecto de cada uno. Cuarto, escribe el propósito explícito. Quinto, formula la intención implícita.",
        "Cuando un texto destaca mucho una parte y esconde otra, esa diferencia también es una pista. Si el precio de cada cuota aparece grande y el total aparece pequeño, es posible que el texto quiera que mires la cuota y no el total.",
        "Inferir no es adivinar: se apoya en citas del texto. Por eso, tu respuesta debe decir «porque el texto dice…» y nombrar la pista. Si no hay pista, mejor deja la duda anotada.",
    ],
    vocab=[("cuota", "cada pago parcial de un total"), ("al contado", "pagar el total de una vez"), ("letra pequeña", "parte del texto escrita en tamaño muy chico que contiene condiciones"), ("pista", "dato o recurso del texto que ayuda a inferir")],
    worked=[
        ("Aplicar los cinco pasos", "Texto (inventado): «¡Llévalo hoy por solo $5.000 al mes!» y, abajo, en letra chica: «20 cuotas».", ["Leo todo: precio de la cuota y letra chica de 20 cuotas.", "Recurso: «solo» minimiza el precio.", "Explícito: informar el precio mensual.", "Implícito: que mires la cuota y no el total."], "Propósito implícito: que parezca barato"),
        ("Calcular el total", "Cuotas de $5.000 por 20 meses.", ["Multiplico 5.000 × 20.", "Obtengo 100.000."], "El total es $100.000"),
    ],
    mistakes=[("Quedarse con lo que el texto destaca y no leer la letra pequeña.", "La letra pequeña suele traer condiciones que cambian el sentido del texto.", "Lee el texto completo antes de concluir."),
              ("Inferir sin citar el texto.", "Sin pistas, la inferencia es solo una sospecha.", "Escribe «porque el texto dice…» con una cita.")],
    T=[
        ("abc", "{F} ¿Cuál es el propósito explícito del aviso?", "Informar que se puede comprar un refrigerador pagando cuotas mensuales", "Instruir sobre cómo limpiar un refrigerador", "Contar la historia de una familia", "Dice cuánto se paga al mes y qué se vende."),
        ("ab", "{F} ¿Qué expresión minimiza el valor del precio?", "«por solo $9.990 al mes»", "«Plan de 12 cuotas mensuales»", "«Solo» hace parecer pequeña la cuota."),
        ("=", "{F} ¿Cuánto se pagaría en total pagando las 12 cuotas?", "9990 * 12", "Se multiplica la cuota mensual por el número de cuotas.", " pesos"),
        ("=", "{F} El precio al contado es $99.900. ¿Cuántos pesos más se paga con el plan de cuotas?", "9990 * 12 - 99900", "Se resta el precio al contado al total de las cuotas.", " pesos"),
        ("abc", "{F} ¿Dónde aparece el precio al contado?", "En la letra pequeña, al final del aviso", "En el titular grande", "En la frase «Tu refrigerador te espera»", "El texto lo informa solo en la letra pequeña."),
        ("abc", "{F} ¿Qué propósito implícito sugiere el hecho de destacar la cuota y no el total?", "Que la persona se fije en que es barato y compre a cuotas", "Que la persona ahorre en cuotas", "Que la persona no compre", "El énfasis en la cuota desvía la atención del total."),
        ("ab", "{F} ¿Qué recurso es «¡Qué tranquilidad para tu familia!»?", "Una exclamación que apela a la emoción", "Una cifra exacta", "La exclamación produce una sensación de tranquilidad, sin dato alguno."),
        ("abc", "{F} ¿Qué recurso usa el aviso al decir «sin pie y sin esperas»?", "Una promesa que busca quitar dudas a quien lee", "Un dato comprobable", "Una instrucción de uso", "Promete facilidades para que la persona no dude."),
        ("abc", "En la pauta de cinco pasos, ¿qué se hace primero?", "Leer el texto completo, incluida la letra pequeña", "Escribir la inferencia final", "Comprar el producto", "Leer completo evita perder condiciones importantes."),
        ("ab", "Pablo dice: «El aviso es engañoso porque miente». ¿Qué conviene responder?", "Que nombre la pista: el total y el contado aparecen en letra pequeña", "Que tiene razón sin dar pruebas", "Una inferencia se apoya en pistas del texto, no en la sospecha."),
        ("abc", "{F} Si el aviso mostrara el total de $119.880 en letra grande junto a la cuota, ¿cambiaría el propósito implícito?", "Sí, ya no ocultaría el total", "No, seguiría igual", "Solo cambiaría el color", "Mostrar el total deja decidir con toda la información."),
        ("ab", "{F} ¿Qué conviene hacer antes de comprar con este aviso?", "Comparar el total a cuotas con el precio al contado", "Fijarse solo en la cuota", "Comparar los dos precios ayuda a decidir con la información completa."),
        ("abc", "{F} Una persona infiere: «El aviso quiere que compre hoy». ¿Qué pista del texto apoya esa idea?", "«Llévalo hoy»", "«refrigerador»", "«familia»", "«Hoy» presiona a decidir de inmediato."),
    ],
    ctx=("abc", "Un cartel de un gimnasio de ejemplo dice: «¡Solo $15.000 al mes!» y abajo, en letra chica: «Contrato por 18 meses». ¿Cuánto pagarías en total por el contrato?", "270.000", "150.000", "180.000", "Quince mil por dieciocho meses da doscientos setenta mil."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué se anota en el tercer paso de la pauta de inferencia?", "El efecto de cada recurso lingüístico", "El efecto muestra para qué se usa cada recurso."),
        ("En Lengua y Literatura de EPJA: ¿por qué es importante leer la letra pequeña?", "Porque suele traer condiciones que cambian el sentido del texto", "Allí aparecen datos que el titular no dice."),
        ("En Lengua y Literatura de EPJA: ¿cómo se apoya una inferencia?", "Con citas o pistas del texto", "Una inferencia sin pistas es una sospecha.")],
    op=("Usa los cinco pasos con este aviso: {F} Escribe en tu cuaderno una frase por paso: qué leíste, qué recursos subrayaste, qué efecto tienen, cuál es el propósito explícito y cuál es el implícito, con una cita del aviso.",
        "1. Leí el aviso y la letra chica. 2. Recursos: «solo», exclamaciones, promesa «sin pie». 3. Efecto: minimizar el precio y dar tranquilidad. 4. Explícito: informar un precio en cuotas. 5. Implícito: que compre a cuotas sin fijarme en que pagaría $119.880 en lugar de $99.900.",
        ["usa los cinco pasos en orden", "cita el aviso en el paso cinco", "incluye el cálculo o la comparación de precios"],
        ["cinco frases"],
        ["inferir sin citar", "no revisar la letra pequeña"],
        "Pregunta: «¿Qué pista del aviso respalda tu idea?»."),
    reinforce="Mira un aviso que ofrezca pagar en cuotas y busca el total en la letra pequeña.",
    extend="Reescribe el aviso de refrigerador para que informe cuota, total y precio al contado de manera clara.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo reconocer estrategias de persuasión: emoción, autoridad, mayoría, urgencia y testimonio.",
    prior=["Reconozco recursos como superlativos y mandatos.", "Sé inferir un propósito con pistas.", "Leo mensajes de venta."],
    explain=[
        "Persuadir es lograr que otra persona piense o haga algo. Es una acción normal: la usamos al pedir un favor o al convencer a un compañero. El problema aparece cuando se persuade sin dar razones comprobables.",
        "Estrategias frecuentes: apelar a la emoción («piensa en tus hijos»); citar a una autoridad («un médico recomienda»); apoyarse en la mayoría («todos ya lo compraron»); generar urgencia («últimas unidades»); usar un testimonio («doña Rosa dice…»). Cada una puede ser razonable o engañosa, según tenga o no datos que la respalden.",
        "Al analizar, nombra la estrategia, cita el texto y pregunta qué dato la respalda. Un testimonio sin datos no demuestra que un producto sirva; una urgencia sin fecha clara puede ser presión; una autoridad sin nombre no se puede verificar.",
    ],
    vocab=[("persuadir", "lograr que otra persona piense o haga algo"), ("testimonio", "relato de una persona que dice haber usado o vivido algo"), ("argumento de autoridad", "razón basada en lo que dice una persona experta"), ("urgencia", "presión para decidir sin tiempo de pensar")],
    worked=[
        ("Reconocer la estrategia", "Frase (inventada): «Dos de cada tres vecinos ya se cambiaron».", ["Se apoya en lo que hace la mayoría.", "No dice quién lo midió."], "Estrategia: apelar a la mayoría"),
        ("Preguntar por el respaldo", "Frase (inventada): «Un especialista recomienda esta crema».", ["La estrategia es la autoridad.", "No se dice quién es ni qué estudió."], "Autoridad sin nombre: no se puede verificar"),
    ],
    mistakes=[("Creer que toda persuasión es engañosa.", "Persuadir con razones y datos claros es legítimo.", "Evalúa si hay datos verificables que respalden lo que se dice."),
              ("Confundir testimonio con prueba.", "La experiencia de una persona no demuestra que algo sirva para todas.", "Pide datos y fuentes además del testimonio.")],
    T=[
        ("abc", "{F} ¿Qué estrategia usa el Mensaje A?", "Testimonio de una usuaria", "Urgencia", "Argumento de autoridad", "Presenta lo que dice doña Rosa."),
        ("ab", "{F} ¿Qué estrategia usa el Mensaje B?", "Apelar a la mayoría", "Apelar a la emoción", "«Nueve de cada diez familias» busca que te sumes a la mayoría."),
        ("{F} ¿Cuántas unidades dice el Mensaje C que quedan en bodega? Escribe solo el número.", "2", "El Mensaje C dice «últimas dos unidades»."),
        ("abc", "{F} ¿Qué estrategia usa el Mensaje C?", "Urgencia, por la oferta que termina hoy", "Testimonio", "Humor", "La hora límite y las pocas unidades presionan a decidir."),
        ("abc", "{F} ¿Qué estrategia usa el Mensaje D?", "Argumento de autoridad", "Apelar a la mayoría", "Urgencia", "Cita a un médico para dar prestigio."),
        ("abc", "{F} ¿Qué estrategia usa el Mensaje E?", "Apelar a la emoción, con la preocupación por los hijos", "Cifras de ventas", "Testimonio", "Apela a un sentimiento familiar de preocupación por los hijos."),
        ("ab", "{F} ¿Qué dato falta para comprobar el Mensaje D?", "El nombre del médico y el estudio que respalda su recomendación", "El color del producto", "«Un médico de renombre» no se puede verificar sin nombre ni respaldo."),
        ("ab", "{F} ¿Qué dato falta para comprobar el Mensaje B?", "Quién midió esa cifra y cuándo", "El nombre de la calle", "Nueve de cada diez requiere saber quién la midió."),
        ("abc", "{F} ¿Qué recurso lingüístico refuerza la urgencia del Mensaje C?", "La hora exacta límite, las 20:00", "El nombre del producto", "La palabra «bodega»", "La hora límite crea presión de tiempo."),
        ("abc", "{F} El Mensaje A dice que la casa «se llenó de energía». ¿Qué falta para comprobarlo?", "Datos o estudios que muestren qué efecto tiene el producto", "Más adjetivos", "Otra frase de doña Rosa", "Un testimonio solo cuenta una experiencia."),
        ("ab", "{F} ¿Cuál de los mensajes usa más fuertemente el sentimiento de culpa?", "El Mensaje E, al preguntar si vas a dejar a tus hijos sin abrigo", "El Mensaje B, al mencionar nueve de cada diez familias", "La pregunta del Mensaje E hace sentir culpa por no comprar."),
        ("abc", "Un cartel dice: «Elige este jabón: lo usa la mayoría». ¿Cuál es la mejor pregunta para evaluarlo?", "¿Quién dice cuántas personas lo usan y cómo lo supo?", "¿De qué color es el jabón?", "¿Cuántas letras tiene el cartel?", "Pedir el origen del dato permite revisar el argumento."),
        ("ab", "Paula dice: «Si algo me persuade, entonces es falso». ¿Qué corresponde responder?", "No: persuadir con razones comprobables puede ser legítimo", "Sí: toda persuasión es engaño", "Hay que revisar los datos, no rechazar toda persuasión."),
    ],
    ctx=("abc", "Una vecina te ofrece un producto (inventado) diciendo: «Mi prima lo usa y está feliz. Últimos frascos». ¿Qué dos estrategias usa?", "Testimonio y urgencia", "Autoridad y humor", "Mayoría y emoción", "Cuenta lo que vive su prima y dice que quedan pocos frascos."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es persuadir?", "Lograr que otra persona piense o haga algo", "Persuadir busca convencer a otra persona de algo."),
        ("En Lengua y Literatura de EPJA: ¿qué es un argumento de autoridad?", "Una razón basada en lo que dice una persona experta", "La autoridad apoya lo que se afirma."),
        ("En Lengua y Literatura de EPJA: ¿qué pregunta ayuda a evaluar una estrategia de persuasión?", "¿Qué dato comprobable la respalda?", "Si no hay datos, la estrategia queda sin respaldo.")],
    op=("Analiza dos mensajes: {F} Elige dos de los cinco mensajes y escribe en tu cuaderno, para cada uno, la estrategia de persuasión, la cita del texto y una pregunta que harías para saber si lo que dice es cierto.",
        "Mensaje B: estrategia, mayoría; cita: «Nueve de cada diez familias»; pregunta: ¿quién midió eso? Mensaje C: estrategia, urgencia; cita: «Últimas dos unidades»; pregunta: ¿cuántas unidades hay realmente y hasta cuándo dura la oferta?",
        ["nombra dos estrategias distintas", "incluye una cita por cada mensaje", "formula una pregunta de verificación"],
        ["dos análisis de tres datos"],
        ["nombrar la estrategia sin citar", "hacer preguntas que no verifican nada"],
        "Pregunta: «¿Qué dato respaldaría lo que dice el mensaje?»."),
    reinforce="Elige un anuncio que hayas visto y escribe qué estrategia usa para convencerte.",
    extend="Escribe un mensaje que persuada con una razón comprobable, por ejemplo invitar a una jornada de limpieza, y compara con uno que persuada solo por urgencia.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico el análisis de propósitos y recursos a dos textos de la comunidad: un volante de vecinos y un mensaje que promete ganancias.",
    prior=["Reconozco recursos lingüísticos.", "Reconozco estrategias de persuasión.", "Infiero propósitos con pistas."],
    explain=[
        "En la vida comunitaria y laboral recibimos textos que piden algo: tiempo, dinero, trabajo o apoyo. Analizar su propósito y sus recursos ayuda a decidir con calma.",
        "Un volante que invita a participar puede persuadir con razones claras: fecha, hora, lugar y un beneficio compartido. Un mensaje que promete mucho dinero sin horarios ni experiencia, y pide un pago adelantado, solo ofrece una promesa y una urgencia, sin datos que se puedan comprobar.",
        "Frente a una oferta que pide dinero o datos personales, no actúes por impulso. Pregunta quién es la persona o la institución, pide información por escrito y consulta con alguien de confianza o con la institución correspondiente. Este cuaderno no entrega consejo financiero ni legal.",
    ],
    vocab=[("promesa", "afirmación de que algo bueno ocurrirá"), ("pago adelantado", "dinero que se pide antes de entregar lo ofrecido"), ("bien común", "beneficio para toda una comunidad"), ("convocar", "llamar a que las personas se reúnan o participen")],
    worked=[
        ("Analizar un volante", "Volante (inventado): «El sábado a las 10:00 arreglamos la sede. Traiga una herramienta si puede. Terminamos a las 13:00».", ["Da fecha, hora y duración.", "Pide un aporte voluntario, no obligatorio."], "Persuade con datos claros y un propósito común"),
        ("Analizar una promesa", "Mensaje (inventado): «Gana mucho sin esfuerzo. Deposita hoy para participar».", ["No dice cuánto, cómo ni quién.", "Pide dinero y apura."], "Promesa sin datos y con urgencia: no hay cómo verificarla"),
    ],
    mistakes=[("Responder de inmediato a un mensaje que pide dinero.", "Una urgencia puede impedir pensar con calma.", "Espera, pregunta y consulta a una persona o institución de confianza."),
              ("Pensar que un volante vecinal no persuade.", "También convence, pero con razones y datos claros.", "Revisa si trae fecha, lugar y propósito.")],
    T=[
        ("abc", "{F} ¿Quién es el emisor del Volante A?", "El comité de vecinos «Los Aromos»", "Una tienda de ejemplo", "Una persona que no se identifica", "El volante termina con el nombre del comité y se dirige a vecinas y vecinos."),
        ("ab", "{F} ¿Cuál es el propósito explícito del Volante A?", "Invitar a limpiar y pintar la plaza el domingo 22", "Vender bancas para la plaza", "Convoca a una actividad con fecha, hora y tarea."),
        ("=", "{F} El Volante A dice que la actividad va de las 10:00 a las 13:00. ¿Cuántas horas dura?", "13 - 10", "Se resta la hora de inicio a la hora de término.", " horas"),
        ("abc", "{F} ¿Qué recurso del Volante A busca que la persona se sienta parte de algo?", "«Nuestra plaza es de todos»", "«El domingo 22»", "«Bolsas»", "La frase apela al sentido de comunidad de los vecinos."),
        ("ab", "{F} ¿Qué dato del Volante A permite comprobar la actividad?", "La fecha, la hora y la tarea que se hará", "El adjetivo «liviano»", "Esos datos se pueden constatar yendo a la plaza."),
        ("abc", "{F} ¿Qué estrategia usa el Mensaje B al decir «Quedan pocos cupos»?", "Urgencia", "Testimonio", "Humor", "Presiona a decidir rápido porque los cupos se acaban."),
        ("=", "{F} El Mensaje B promete $300.000 a la semana. ¿Cuánto serían en cuatro semanas, si la promesa fuera cierta?", "300000 * 4", "Se multiplica la promesa semanal por cuatro semanas.", " pesos"),
        ("abc", "{F} ¿Qué exige el Mensaje B antes de recibir el kit?", "Un depósito de $20.000", "Una reunión", "Una carta de recomendación", "El mensaje pide un pago adelantado de veinte mil pesos."),
        ("abc", "{F} ¿Qué dato esencial falta en el Mensaje B?", "Quién lo envía y en qué consiste el trabajo", "Una cifra de dinero", "Un saludo cordial", "Sin emisor ni descripción no se puede verificar."),
        ("ab", "{F} ¿Cuál texto se puede verificar más fácilmente?", "El Volante A, porque indica fecha, hora y lugar", "El Mensaje B, porque promete dinero", "Con el volante se puede ir y comprobar; el mensaje no da datos."),
        ("abc", "{F} Un amigo propone depositar «solo por probar». ¿Cuál es una respuesta respetuosa y prudente?", "Sugerir que pidan información por escrito y consulten a una institución antes de decidir", "Decirle que deposite rápido", "Decirle que no hable nunca de eso", "Una consulta evita decidir con presión."),
        ("ab", "{F} ¿Qué propósito implícito tiene la frase «Sin experiencia, sin horarios» del Mensaje B?", "Hacer parecer que cualquiera puede ganar sin esfuerzo", "Explicar cómo se hace el trabajo", "Elimina las dudas sobre requisitos para atraer a más personas."),
        ("abc", "Un volante de un taller (inventado) dice: «Aprenda panadería: curso de sábado a las 10:00, 8 clases, consultas en la sede». ¿Qué lo hace más confiable?", "Da día, hora, número de clases y dónde consultar", "Usa la palabra «aprenda»", "No dice nada concreto", "Los datos concretos permiten verificar la información en persona."),
    ],
    ctx=("abc", "Te llega este mensaje (inventado): «Ganaste un premio. Para retirarlo, envía tu cédula y un depósito». ¿Qué conviene hacer?", "No responder con datos y consultar con una persona o institución de confianza", "Enviar la cédula para no perder el premio", "Enviar el depósito de inmediato", "No hay emisor claro y se piden datos y dinero con urgencia."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es un pago adelantado?", "Dinero que se pide antes de entregar lo ofrecido", "Es una señal que conviene revisar con cuidado."),
        ("En Lengua y Literatura de EPJA: ¿qué hace confiable a un volante comunitario?", "Que dé fecha, hora, lugar y propósito claros", "Esos datos se pueden comprobar yendo a la plaza."),
        ("En Lengua y Literatura de EPJA: ¿qué conviene hacer ante una promesa de dinero fácil?", "Pedir información por escrito y consultar a una persona o institución de confianza", "Consultar evita decidir bajo presión y con poca información.")],
    op=("Analiza los dos textos: {F} Escribe en tu cuaderno una tabla con dos columnas, una para el Volante A y otra para el Mensaje B, y en filas: emisor, propósito explícito, propósito implícito, un recurso lingüístico y qué se puede comprobar. Luego escribe qué harías con cada texto.",
        "Volante A: emisor, comité; explícito, invitar a limpiar la plaza; implícito, fortalecer la comunidad; recurso, «Nuestra plaza es de todos»; comprobable, fecha y lugar. Mensaje B: emisor, no se identifica; explícito, ofrecer trabajo; implícito, que deposites dinero; recurso, «Quedan pocos cupos»; comprobable, nada. Con A: asistiría. Con B: no depositaría y consultaría.",
        ["completa las cinco filas con datos de los textos", "explica qué haría con cada texto", "usa un tono respetuoso y claro"],
        ["una tabla de dos columnas y dos frases"],
        ["no distinguir propósito explícito de implícito", "decidir sin justificar"],
        "Pregunta: «¿Qué dato te permite comprobar cada texto?»."),
    reinforce="Revisa un mensaje que pida dinero y anota qué datos faltan.",
    extend="Escribe un volante breve que invite a una actividad de tu barrio con fecha, hora, lugar y una razón clara.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy analizo recursos no lingüísticos (tamaños, colores, imágenes descritas) junto con el lenguaje y reviso lo que he logrado hasta aquí.",
    prior=["Reconozco recursos lingüísticos.", "Reconozco estrategias de persuasión.", "Reviso propósitos explícitos e implícitos."],
    explain=[
        "Los textos no solo usan palabras. Los recursos no lingüísticos son los que no son lenguaje verbal: el tamaño de las letras, los colores, las imágenes y la posición de cada elemento. En un afiche, lo más grande se lee primero.",
        "Estos recursos también persuaden. Un color intenso llama la atención. Una imagen de una familia sonriente asocia el producto con la felicidad. El tamaño del precio o de la palabra «oferta» orienta hacia donde quiere el emisor que mires, y las condiciones en letra pequeña pueden quedar fuera de la vista.",
        "Para evaluar un texto, junta ambos tipos de recursos: ¿qué dicen las palabras?, ¿qué destacan las imágenes y los tamaños?, ¿qué esconden?, ¿coinciden con el propósito declarado? Al final, revisa lo que lograste y decide qué practicar.",
    ],
    vocab=[("recurso no lingüístico", "elemento que no es palabra, como color, imagen o tamaño de letra"), ("destacar", "hacer que algo se note más"), ("condición", "requisito que limita lo que se ofrece"), ("jerarquía visual", "orden en que el ojo ve los elementos de un texto")],
    worked=[
        ("Analizar el tamaño", "Afiche (inventado): precio en letras grandes y condiciones en letras diminutas.", ["Identifico qué se destaca: el precio.", "Identifico qué se esconde: las condiciones."], "Se destaca lo atractivo y se minimiza lo que limita"),
        ("Analizar una imagen", "Afiche (inventado): foto de una persona sonriendo junto a un auto.", ["La imagen asocia el auto con la alegría.", "No entrega datos sobre el auto."], "La imagen apela a la emoción, no a los datos"),
    ],
    mistakes=[("Analizar solo las palabras y olvidar el diseño.", "Los tamaños y colores también transmiten un mensaje.", "Pregunta qué se ve primero y qué casi no se ve."),
              ("Creer que la letra pequeña no es parte del mensaje.", "Es parte del texto y puede contener condiciones decisivas.", "Léela completa antes de decidir.")],
    T=[
        ("abc", "{F} ¿Qué se destaca más en el afiche por su tamaño?", "La palabra OFERTA", "Las condiciones", "El nombre de la calle", "La palabra OFERTA ocupa la mitad del afiche."),
        ("ab", "{F} ¿Qué color se usa para la palabra OFERTA?", "Rojo", "Gris", "El texto dice «letras rojas enormes»."),
        ("{F} ¿Cuál es el precio destacado en el afiche? Escribe la cifra con punto, por ejemplo 100.000.", "199.990", "El afiche muestra «$199.990» en tamaño grande."),
        ("abc", "{F} ¿Qué recurso no lingüístico asocia el producto con la felicidad?", "La fotografía de una familia sonriente", "El color gris del pie", "El precio", "La imagen transmite alegría y bienestar."),
        ("abc", "{F} ¿Dónde aparecen las condiciones de la oferta?", "Al pie, en letras pequeñas y grises", "En el titular rojo", "En la fotografía", "Están escritas en tamaño pequeño y color poco visible."),
        ("ab", "{F} ¿Qué efecto tiene escribir las condiciones en letra pequeña y gris?", "Pasan más fácilmente desapercibidas", "Se leen primero", "El tamaño y el color poco llamativos hacen que se noten menos."),
        ("abc", "{F} ¿Qué condición dice la letra pequeña sobre el pago?", "Que el precio es con tarjeta de la tienda", "Que el pago es al contado sin condiciones", "Que no hay stock", "El afiche dice «Precio con tarjeta de la tienda»."),
        ("abc", "{F} ¿Cuál es el propósito explícito del afiche?", "Informar una oferta de cocinas con un precio", "Dar instrucciones de uso", "Contar una historia familiar", "Anuncia una oferta y su precio."),
        ("abc", "{F} ¿Qué propósito implícito se puede inferir?", "Que la persona compre con la tarjeta de la tienda", "Que la persona ahorre dinero sin condiciones", "Que la persona compare con otras tiendas", "Se destaca el precio y se condiciona a la tarjeta."),
        ("ab", "{F} Un amigo dice: «El precio del afiche aplica para todas las personas». ¿Es correcto?", "No: el afiche dice que es con tarjeta de la tienda", "Sí: el precio está en tamaño grande", "La letra pequeña limita el precio a quienes pagan con esa tarjeta."),
        ("abc", "{F} ¿Qué dato conviene preguntar antes de decidir?", "Cuáles son las condiciones de la oferta y cuánto vale sin la tarjeta", "De qué color es la cocina", "Cuántas personas salen en la foto", "Las condiciones definen el precio real."),
        ("ab", "Una persona termina esta unidad y dice que le falta practicar cómo verificar fuentes. ¿Qué paso sigue?", "Elegir un texto y comprobar quién lo emite y de dónde salen sus datos", "Memorizar los nombres de los recursos sin usarlos", "Practicar la fuente es el siguiente paso para fortalecer su análisis."),
        ("abc", "¿Cuál es la mejor forma de cerrar el análisis de un texto?", "Decidir si es confiable, dudoso o requiere confirmación, con razones", "Opinar sin citar el texto", "Pasar al siguiente texto sin decidir", "La evaluación termina con una decisión justificada."),
    ],
    ctx=("abc", "En la puerta de una ferretería de ejemplo hay un cartel con la palabra DESCUENTO en letras enormes y, abajo en letra chica, «Solo en productos seleccionados». ¿Qué conviene preguntar?", "Qué productos están seleccionados", "Qué tamaño tiene la puerta", "Quién pintó el cartel", "La letra pequeña limita a qué productos aplica el descuento."),
    sc=[("En Lengua y Literatura de EPJA: ¿qué es un recurso no lingüístico?", "Un elemento que no es palabra, como el color o la imagen", "Los colores, las imágenes y los tamaños también comunican."),
        ("En Lengua y Literatura de EPJA: ¿para qué se usa la letra pequeña en algunos afiches?", "Para incluir condiciones que limitan lo ofrecido", "La letra pequeña puede contener condiciones decisivas."),
        ("En Lengua y Literatura de EPJA: ¿qué se revisa al cerrar el análisis de un texto?", "Si es confiable, dudoso o necesita confirmación, y por qué", "Se concluye con una decisión justificada.")],
    op=("Analiza el afiche completo: {F} Escribe en tu cuaderno dos recursos lingüísticos, dos no lingüísticos y el propósito implícito. Luego completa esta lista con tus palabras: tres cosas que ya haces bien al analizar un texto, una que quieres practicar y a quién pedirías apoyo.",
        "Lingüísticos: «OFERTA» y mandato implícito de comprar. No lingüísticos: letras rojas enormes y foto de una familia sonriente. Implícito: que compre con la tarjeta de la tienda sin fijarme en las condiciones. Lo que hago bien: reconozco emisor, separo hechos de opiniones, reviso cifras. Practicar: verificar fuentes. Apoyo: mi facilitadora o un compañero.",
        ["identifica dos recursos de cada tipo", "infiere el propósito implícito con base en el afiche", "evalúa su avance y nombra apoyo"],
        ["cinco recursos o datos y una lista de revisión"],
        ["analizar solo las palabras", "no decir a quién pedir apoyo"],
        "Pregunta: «¿Qué muestra y qué esconde el afiche?»."),
    reinforce="Mira un afiche o volante y anota qué se ve primero y qué casi no se ve.",
    extend="Diseña en tu cuaderno, con palabras y un dibujo simple, un afiche honesto para una actividad de tu barrio, con las condiciones en tamaño legible.",
)
