"""Química (electivo 3.º y 4.º medio HC): OAC-01 (nanoquímica y polímeros, clases 1 a 5) y OAC-02 (ácido-base, óxido-reducción y polimerización-despolimerización, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, cuaderno y calculadora simple. Todos los datos, tablas y casos son de ejemplo (rotulados así) y están escritos completos en el enunciado o en la ficha de la clase. "
             "Este cuaderno no propone experimentos, mezclas ni procedimientos con sustancias: los resultados que se analizan vienen ya escritos y los cálculos se hacen en papel. "
             "Las masas atómicas y las constantes que se usan se entregan en cada ficha; si necesitas otras, pídelas a tu docente. Ante cualquier duda sobre sustancias reales, consulta a tu docente y nunca manipules productos químicos por tu cuenta.")
build = make_build(MATERIALS)

O1 = "CN-QUIM-3y4-OAC-01"
O2 = "CN-QUIM-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (datos de ejemplo). Escala: 1 metro equivale a 1.000.000.000 nanómetros (nm); 1 micrómetro (µm) equivale a 1.000 nm. Una nanopartícula de ejemplo mide 50 nm; una bacteria de ejemplo mide 2.000 nm (2 µm). "
     "Masas atómicas que se entregan: H = 1 y C = 12. El plástico polietileno está formado por cadenas largas de una molécula llamada eteno (C2H4), que se une consigo misma muchas veces. "
     "Tres preguntas de ejemplo: P1 «¿Es bueno el plástico?». P2 «¿Cómo cambia la capacidad de reaccionar de partículas de plata cuando su tamaño baja de 100 nm a 10 nm?». P3 «¿Qué pasa con la química y los materiales?».")
build(
    O1, 1, F,
    use="Aprenderé a delimitar una pregunta sobre nanoquímica y polímeros: qué sistema estudio, a qué escala y con qué variable. Sirve para evaluar cómo avanza el conocimiento y qué aplicaciones y consecuencias trae en lo ambiental, médico, agrícola e industrial.",
    prior=["Sé qué es un átomo y una molécula.", "Sé convertir entre unidades de longitud con potencias de diez.", "Distingo una pregunta general de una pregunta que se puede investigar."],
    explain=[
        "La nanoquímica estudia materiales cuyas estructuras miden aproximadamente entre 1 y 100 nanómetros. Un nanómetro es la milmillonésima parte de un metro. A esa escala, las propiedades de un material pueden cambiar respecto del mismo material en trozos grandes, porque una fracción mucho mayor de sus átomos queda en la superficie. Por eso se pueden diseñar partículas con color, reactividad o capacidad de transporte distintos.",
        "La química de polímeros estudia moléculas muy grandes, formadas por una unidad pequeña, el monómero, que se repite muchas veces. El polietileno, por ejemplo, está hecho de miles de moléculas de eteno unidas en cadena. Hay polímeros naturales, como el almidón y las proteínas, y sintéticos, como muchos plásticos. Su masa molar aproximada se calcula como el número de unidades por la masa del monómero.",
        "Para evaluar el desarrollo de este conocimiento hay que partir por delimitar la pregunta y el sistema: qué material, a qué escala, qué propiedad y qué consecuencia se quiere analizar. Una pregunta bien delimitada nombra una variable que se puede medir y un ámbito concreto, como el ambiental o el médico. Una pregunta como «¿es bueno el plástico?» mezcla demasiadas cosas y no se puede responder con datos.",
    ],
    vocab=[("nanómetro (nm)", "milmillonésima parte de un metro"), ("nanopartícula", "partícula cuyo tamaño está aproximadamente entre 1 y 100 nm"), ("monómero", "molécula pequeña que se repite para formar un polímero"), ("polímero", "molécula muy grande formada por muchas unidades repetidas"), ("sistema", "parte de la realidad que se delimita para estudiarla")],
    worked=[
        ("Elegir la mejor pregunta", "Quieres investigar nanopartículas de óxido de zinc usadas en protectores solares. ¿Qué pregunta está mejor delimitada: «¿es peligrosa la nanotecnología?» o «¿cómo varía la cantidad de nanopartículas que llega a un río con el número de bañistas por día?»",
         ["La primera abarca todo un campo y no nombra ningún material ni variable medible.", "La segunda nombra un material, una variable que se cambia (bañistas por día) y otra que se mide (cantidad en el río).", "Se puede responder con datos de recuentos y mediciones."],
         "La segunda pregunta"),
        ("Masa molar de un polímero", "Una cadena de polietileno de ejemplo tiene 200 unidades de eteno. ¿Cuál es su masa molar aproximada?",
         ["Masa del monómero C2H4: 2 × 12 + 4 × 1 = 28.", "Masa de la cadena: 200 unidades × 28.", "200 × 28 = 5.600."],
         "5.600 g/mol"),
    ],
    mistakes=[("Pensar que «nano» significa «malo» o «mejor» por definición.", "Nano solo indica una escala de tamaño; sus efectos dependen del material y se deben evaluar con datos.", "Habla de aplicaciones y de riesgos posibles, y pide evidencia para cada uno."),
              ("Formular preguntas como «¿qué pasa con los plásticos?».", "Es tan amplia que ningún dato la responde.", "Acótala: elige un material, una propiedad y un ámbito (por ejemplo, ambiental).")],
    T=[
        ("abc", "En Química: ¿qué estudia la nanoquímica?", "Materiales con estructuras de entre 1 y 100 nm cuyas propiedades pueden diferir de las del material en trozos grandes", "Solo átomos aislados, sin ninguna aplicación", "Únicamente los plásticos de uso cotidiano", "La nanoquímica se define por la escala de 1 a 100 nm y por los cambios de propiedades en ella."),
        ("{F} ¿Cuántos nanómetros hay en un micrómetro?", "1.000 nm", "La ficha indica que un micrómetro equivale a 1.000 nm, y la bacteria de 2.000 nm mide 2 µm."),
        ("{F} ¿Cuál de las tres preguntas (P1, P2 o P3) está mejor delimitada?", "P2", "P2 nombra un material, un rango de tamaños y una propiedad que se puede medir."),
        ("abc", "{F} ¿Por qué P1 «¿Es bueno el plástico?» está mal delimitada?", "Mezcla muchos tipos de plástico y de usos, y «bueno» no es una variable medible", "Porque nombra un nanómetro", "Porque es demasiado corta para ser una pregunta", "Una pregunta delimitada necesita un sistema acotado y una variable que se pueda medir."),
        ("=", "{F} ¿Cuántas veces es mayor la bacteria de ejemplo que la nanopartícula de ejemplo?", "2000/50", "Se divide el tamaño de la bacteria por el de la nanopartícula, ambos en nanómetros.", " veces"),
        ("{F} En la pregunta P2, ¿qué variable se cambia (la que decide quien investiga)?", "El tamaño de las partículas de plata", "En P2 se compara la reactividad con tamaños distintos, así que el tamaño es lo que se cambia."),
        ("=", "{F} Una fila tiene 8 nanopartículas iguales de 25 nm cada una, una al lado de otra. ¿Cuántos nanómetros mide la fila?", "8*25", "Se multiplica el número de partículas por el tamaño de cada una.", " nm"),
        ("=", "Una partícula de ejemplo mide 3 µm. ¿Cuántos nanómetros son?", "3*1000", "Cada micrómetro equivale a 1.000 nanómetros, así que se multiplica por 1.000.", " nm"),
        ("abc", "{F} Una partícula de ejemplo mide 300 nm. ¿Está en la nanoescala según el criterio de la clase?", "No, porque supera los 100 nm", "Sí, porque es menor que 1 µm", "Sí, porque mide más de 1 nm", "El criterio de la clase sitúa la nanoescala entre 1 y 100 nm, y 300 nm lo excede."),
        ("ab", "Un estudiante propone investigar «¿es peligrosa la nanotecnología?». ¿Qué mejora la pregunta?", "Acotarla a un material, un tamaño y un efecto que se pueda medir", "Hacerla aún más general para incluir todos los casos", "Delimitar es acotar el sistema y la variable para poder responder con datos concretos."),
        ("abc", "Quieres estudiar el polietileno de una bolsa como sistema. ¿Qué opción lo delimita mejor?", "Las cadenas de polietileno de una bolsa de ejemplo: su origen, su uso y su destino al desecharla", "Todos los plásticos del mundo y sus usos", "La palabra «plástico» en la publicidad", "Un sistema bien delimitado es un objeto concreto con un ciclo acotado que se puede describir con datos."),
        ("abc", "Alguien afirma: «los nanomateriales son siempre mejores que los materiales comunes». ¿Qué problema tiene esta afirmación?", "Generaliza con «siempre» sin indicar material, propiedad ni dato que la sostenga", "Ninguno: está bien formulada", "Solo que debería decir «nanómetros»", "Una afirmación científica debe indicar el caso y la evidencia; «siempre» sin datos no es evaluable."),
        ("=", "{F} Una cadena de polietileno de ejemplo tiene 500 unidades de eteno (C2H4). ¿Cuál es su masa molar aproximada?", "(2*12+4*1)*500", "Se calcula la masa del monómero C2H4 y se multiplica por el número de unidades.", " g/mol"),
    ],
    ctx=("abc", "Contexto: tu liceo debate si instalar en el patio un sistema de recolección de botellas plásticas. Debes proponer una pregunta de investigación para tu informe. ¿Cuál es la mejor delimitada?", "¿Cuántas botellas plásticas de un tipo se desechan en el liceo por semana y qué porcentaje se podría recolectar por separado?", "¿Es malo el plástico para el planeta?", "¿Qué piensa la gente sobre todo lo relacionado con residuos?", "La mejor pregunta nombra un objeto, una variable medible y un ámbito acotado."),
    sc=[
        ("En Química: ¿qué es un monómero?", "Una molécula pequeña que se repite para formar un polímero", "El monómero es la unidad repetida; muchos monómeros unidos forman la cadena del polímero."),
        ("ab", "Una pregunta bien delimitada:", "Nombra un sistema y una variable que se puede medir", "Abarca todo un campo científico", "Delimitar permite contestar con datos concretos."),
        ("ab", "La nanoescala se sitúa aproximadamente entre:", "1 y 100 nm", "1 y 100 mm", "La nanoescala es la de los nanómetros, no la de los milímetros."),
    ],
    op=("Con los datos de la ficha {F}: (1) elige uno de estos ámbitos: ambiental, médico, agrícola o industrial; (2) escribe una pregunta de investigación sobre nanopartículas o sobre un polímero, con material, variable y ámbito; (3) explica en dos oraciones por qué tu pregunta se puede responder con datos y qué sistema delimitas.",
        "(1) Ambiental. (2) ¿Cómo cambia la cantidad de microplásticos de polietileno en el agua de un arroyo con el número de lavados de ropa sintética de un barrio? (3) Se puede responder midiendo recuentos en muestras de agua y registrando lavados; el sistema es un tramo del arroyo.",
        ["ámbito elegido", "pregunta con material, variable y ámbito", "explicación de por qué se puede responder con datos", "sistema acotado"],
        ["tres respuestas numeradas"],
        ["formular una pregunta que mezcla muchos materiales", "usar «bueno» o «malo» como variable", "no indicar el sistema"],
        "Pregunta: «¿qué dato concreto necesitarías para responder tu pregunta?»."),
    reinforce="Escribe tres preguntas sobre nanomateriales o polímeros: una mal delimitada, una mejorada y una explicación de qué cambiaste al mejorarla.",
    extend="Explica por qué una nanopartícula puede reaccionar distinto de un trozo grande del mismo material, usando la idea de superficie.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (datos de ejemplo). Fuente A: artículo de una revista científica con método descrito, datos publicados y tres laboratorios independientes que obtuvieron resultados parecidos. "
     "Fuente B: aviso comercial de un fabricante de un «nano-spray milagroso», sin datos ni método. Fuente C: una publicación de redes sociales con el testimonio de una persona. "
     "Tabla de ejemplo de un ensayo con nanopartículas de plata sobre un cultivo de bacterias (a mayor concentración, menos bacterias vivas): concentración 1 mg/L: 20 % de reducción; 5 mg/L: 60 %; 10 mg/L: 90 %. "
     "Todo el ensayo se hizo con la misma especie de bacteria, a la misma temperatura y durante el mismo tiempo.")
build(
    O1, 2, F,
    use="Aprenderé a evaluar si una fuente sobre nanomateriales o polímeros es confiable y a identificar qué variables se cambian, se miden y se mantienen constantes. Sirve para no creer afirmaciones sin evidencia sobre aplicaciones y riesgos.",
    prior=["Sé leer una tabla de datos.", "Sé que una conclusión debe apoyarse en datos.", "Distingo una opinión de un resultado medido."],
    explain=[
        "No todas las fuentes valen lo mismo. Una fuente es más confiable cuando describe el método, publica los datos, ha sido revisada por especialistas independientes y sus resultados se repiten en otros laboratorios. También importa si quien la escribe tiene un interés económico en el resultado, porque eso puede sesgar lo que muestra. Un aviso comercial o un testimonio personal pueden ser útiles como pistas, pero no son evidencia suficiente.",
        "En un ensayo se distinguen tres tipos de variables. La variable independiente es la que quien investiga decide cambiar, por ejemplo la concentración de nanopartículas. La variable dependiente es la que se mide para ver el efecto, por ejemplo el porcentaje de bacterias eliminadas. Las variables controladas son las que se mantienen iguales, como la especie, la temperatura y el tiempo, para que el efecto se pueda atribuir a la variable cambiada.",
        "Con una tabla se puede describir la relación entre variables: si al aumentar la concentración aumenta el efecto, hay una relación creciente. La diferencia entre dos porcentajes se expresa en puntos porcentuales. Pero una relación observada en un ensayo no prueba por sí sola que el material sea seguro ni útil en otras condiciones: faltan ensayos con otros organismos y con concentraciones reales del ambiente.",
    ],
    vocab=[("fuente confiable", "fuente que muestra método, datos y resultados repetidos por otros"), ("variable independiente", "la que se cambia a propósito"), ("variable dependiente", "la que se mide para ver el efecto"), ("variable controlada", "la que se mantiene igual en todo el ensayo"), ("sesgo", "desviación que favorece un resultado por interés o por error")],
    worked=[
        ("Clasificar variables", "En el ensayo de la ficha con nanopartículas de plata, ¿qué tipo de variable es la temperatura?",
         ["La temperatura fue la misma en todo el ensayo.", "Nadie la cambió a propósito ni se midió como efecto.", "Se mantuvo igual para poder atribuir el efecto a la concentración."],
         "Variable controlada"),
        ("Leer una relación en una tabla", "Con la tabla de ejemplo, ¿cuántos puntos porcentuales más de reducción hay entre 1 mg/L y 5 mg/L?",
         ["Reducción a 5 mg/L: 60 %.", "Reducción a 1 mg/L: 20 %.", "Diferencia: 60 − 20 = 40 puntos porcentuales."],
         "40 puntos porcentuales"),
    ],
    mistakes=[("Confiar en una fuente porque suena científica («nano-spray milagroso»).", "El lenguaje técnico no es evidencia: falta método, datos y repetición.", "Pregunta siempre qué datos presenta, cómo se midieron y quién los repitió."),
              ("Decir que el ensayo demuestra que la plata nanométrica es segura porque mató bacterias.", "El ensayo mide el efecto sobre bacterias de un cultivo, no la seguridad para otros organismos.", "Limita la conclusión a lo medido y anota qué ensayos faltan.")],
    T=[
        ("abc", "En Química: ¿qué es la variable independiente de un ensayo?", "La que quien investiga decide cambiar", "La que se mantiene igual en todo el ensayo", "El resultado final del ensayo", "La variable independiente es la que se modifica a propósito para observar su efecto."),
        ("{F} En el ensayo de la ficha, ¿cuál es la variable independiente?", "La concentración de nanopartículas de plata", "La concentración es lo que cambió entre las tres condiciones del ensayo."),
        ("{F} ¿Cuál de las tres fuentes (A, B o C) describe método y datos y tiene resultados repetidos por tres laboratorios?", "La fuente A", "Solo la fuente A muestra método, datos y repetición independiente."),
        ("abc", "{F} ¿Qué variable se mide para ver el efecto de las nanopartículas?", "El porcentaje de reducción de bacterias", "La especie de bacteria", "El tiempo del ensayo", "La variable dependiente es la que se mide como efecto, aquí la reducción en porcentaje."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de reducción hay entre 5 mg/L y 10 mg/L?", "90-60", "Se resta la reducción a 5 mg/L de la reducción a 10 mg/L.", " puntos porcentuales"),
        ("ab", "{F} ¿Por qué se usó la misma especie, temperatura y tiempo en todo el ensayo?", "Para que el efecto se pueda atribuir solo a la concentración", "Para que todas las concentraciones den el mismo resultado", "Mantener controladas esas variables evita que expliquen la diferencia observada."),
        ("abc", "{F} ¿Qué relación muestra la tabla entre concentración y reducción?", "A mayor concentración, mayor reducción en este ensayo", "A mayor concentración, menor reducción", "No hay relación entre ambas", "Los porcentajes 20, 60 y 90 suben junto con la concentración."),
        ("=", "{F} Si cada aumento de 1 mg/L a 5 mg/L sumara lo mismo a la reducción, ¿cuántos puntos porcentuales sumaría por cada mg/L adicional entre esos dos valores?", "(60-20)/(5-1)", "Se divide el aumento de reducción por el aumento de concentración entre ambos puntos.", " puntos porcentuales por mg/L"),
        ("ab", "{F} La fuente B afirma que su nano-spray «elimina el 100 % de los gérmenes». ¿Qué se necesita para creerlo?", "Datos, método y repetición por laboratorios independientes", "Que el aviso repita la frase con más fuerza", "Una afirmación fuerte requiere evidencia fuerte, no solo repetición del mensaje."),
        ("abc", "{F} Un estudiante concluye: «el ensayo prueba que las nanopartículas de plata son seguras para peces». ¿Qué falla?", "El ensayo midió bacterias, no peces, así que no permite esa conclusión", "Nada: la plata es segura en todo caso", "Que la tabla tiene solo números", "Una conclusión no puede ir más allá de lo que midió el ensayo."),
        ("abc", "{F} Una empresa que vende nanoproductos financia un estudio y publica solo los resultados favorables. ¿Qué problema es este?", "Un sesgo por interés económico y por omisión de datos", "Una variable controlada", "Un error de unidades", "Mostrar solo los datos favorables sesga la imagen del producto."),
        ("ab", "{F} Para ganar confianza en la fuente C (testimonio), ¿qué conviene hacer?", "Buscar estudios con datos y método que confirmen o desmientan lo que cuenta", "Compartirla porque ya la leyeron muchas personas", "Un testimonio es una pista; la confirmación viene de datos medidos y repetidos."),
        ("abc", "{F} En un segundo ensayo de ejemplo con 15 mg/L la reducción fue de 95 %. ¿Qué muestra respecto del efecto al subir la concentración?", "Que el efecto sigue creciendo, pero cada vez más lento", "Que el efecto crece cada vez más rápido", "Que el efecto deja de existir", "Entre 10 y 15 mg/L la reducción sube 5 puntos, mucho menos que entre 1 y 5 mg/L."),
    ],
    ctx=("abc", "Contexto: un compañero te muestra un video que promociona un recubrimiento nano para botellas, con una persona vestida de científica pero sin datos. Debes decidir qué hacer antes de compartirlo. ¿Qué eliges?", "Buscar una fuente con método, datos y resultados repetidos antes de compartirlo", "Compartirlo porque parece profesional", "Compartirlo solo si tiene muchos «me gusta»", "Antes de difundir una afirmación se verifica en fuentes que muestren evidencia."),
    sc=[
        ("En Química: ¿qué es una variable controlada?", "La que se mantiene igual en todo el ensayo", "Se controla para que no explique las diferencias observadas."),
        ("ab", "Una fuente es más confiable cuando:", "Muestra método y datos y otros repiten sus resultados", "Usa palabras técnicas y promete resultados perfectos", "La repetición independiente y los datos publicados son la base de la confianza."),
        ("ab", "Un ensayo con bacterias permite concluir sobre:", "El efecto en esas bacterias en esas condiciones", "La seguridad para todos los organismos", "La conclusión se limita a lo que se midió."),
    ],
    op=("Con los datos de la ficha {F}: (1) clasifica las variables del ensayo (independiente, dependiente y dos controladas); (2) ordena las fuentes A, B y C de más a menos confiable y justifica con un criterio cada una; (3) escribe una conclusión que no vaya más allá de los datos y una limitación.",
        "(1) Independiente: concentración; dependiente: porcentaje de reducción; controladas: especie y temperatura. (2) A, luego C, luego B: A muestra método, datos y repetición; C es un testimonio sin datos; B busca vender. (3) A mayor concentración hubo mayor reducción de bacterias; falta ensayar con otros organismos.",
        ["variables bien clasificadas", "orden con un criterio por fuente", "conclusión acotada a los datos", "limitación formulada"],
        ["tres respuestas numeradas"],
        ["confundir variable independiente con dependiente", "ordenar sin criterio", "concluir seguridad para organismos no medidos"],
        "Pregunta: «¿qué otra variable controlarías en un ensayo mejor?»."),
    reinforce="Escribe una lista de cinco preguntas que haces a cualquier fuente antes de creerle sobre un nanomaterial o un plástico nuevo.",
    extend="Explica por qué la repetición del resultado por laboratorios independientes aumenta la confianza en una afirmación científica.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (datos de ejemplo). Modelo de cubo: un material con forma de cubo de lado L (en nm) tiene área total 6 × L × L y volumen L × L × L, así que su cociente superficie/volumen es 6 ÷ L. "
     "Cubos de ejemplo: lado 60 nm, lado 6 nm, lado 3 nm. Masas atómicas que se entregan: H = 1, C = 12, O = 16. "
     "Modelo de polímero: el polietileno se forma por la unión de n moléculas de eteno (C2H4, 28 g/mol cada una) sin perder átomos. "
     "El almidón se forma por la unión de n moléculas de glucosa (180 g/mol cada una); en cada unión se pierde una molécula de agua (18 g/mol).")
build(
    O1, 3, F,
    use="Aprenderé a interpretar dos modelos de la química de materiales: el cociente superficie/volumen y la formación de un polímero a partir de monómeros. Sirve para explicar por qué cambian las propiedades a escala nano y cómo se calcula la masa de una cadena.",
    prior=["Sé calcular áreas y volúmenes de un cubo.", "Sé leer una masa molar en g/mol.", "Sé qué es un monómero y un polímero."],
    explain=[
        "Un modelo es una representación simplificada que permite explicar y predecir. El modelo del cubo muestra por qué los materiales nano son especiales: al reducir el lado L, el cociente superficie/volumen, que vale 6 ÷ L, aumenta. Un cubo de lado 5 nm tiene cociente 1,2 por nm, y uno de lado 10 nm tiene 0,6 por nm. Más superficie por cada unidad de volumen significa que más átomos están expuestos y pueden reaccionar.",
        "El modelo de polímero describe cómo se forma una cadena. En una polimerización por adición, como la del polietileno, los monómeros se unen sin perder átomos, por lo que la masa del polímero es n por la masa del monómero. En una polimerización por condensación, como la del almidón, cada unión libera una molécula pequeña, por ejemplo agua. Con n monómeros se forman n − 1 uniones, y la masa del polímero es n por la masa del monómero menos (n − 1) por la masa del agua.",
        "Todo modelo tiene supuestos. El cubo supone una forma perfecta y no considera que las nanopartículas reales tienen formas irregulares y se agrupan. El modelo de polímero supone cadenas de igual largo, aunque en un plástico real hay cadenas de largos distintos. Un buen análisis siempre dice qué explica el modelo y qué deja fuera.",
    ],
    vocab=[("cociente superficie/volumen", "área total dividida por el volumen de un cuerpo"), ("polimerización por adición", "unión de monómeros sin pérdida de átomos"), ("polimerización por condensación", "unión de monómeros que libera una molécula pequeña, como agua"), ("masa molar", "masa de un mol de sustancia, en g/mol"), ("supuesto", "condición que el modelo da por cierta para poder funcionar")],
    worked=[
        ("Cociente de un cubo", "¿Cuánto vale el cociente superficie/volumen de un cubo de lado 12 nm?",
         ["Se aplica el modelo: 6 ÷ L.", "L es 12 nm.", "6 ÷ 12 = 0,5 por nm."],
         "0,5 por nm"),
        ("Masa de un polímero de condensación", "Una cadena de almidón de ejemplo tiene 4 unidades de glucosa. ¿Cuál es su masa molar aproximada?",
         ["Masa de las 4 glucosas: 4 × 180 = 720.", "Uniones: 4 − 1 = 3 y se pierden 3 × 18 = 54.", "Masa del polímero: 720 − 54 = 666."],
         "666 g/mol"),
    ],
    mistakes=[("Creer que el cociente superficie/volumen aumenta cuando el cubo crece.", "Como el cociente es 6 ÷ L, al crecer L el cociente disminuye.", "Recuerda: lado menor, cociente mayor, más átomos expuestos."),
              ("Olvidar restar el agua perdida en una polimerización por condensación.", "Si no se resta, la masa del polímero queda sobreestimada.", "Calcula siempre n − 1 uniones y resta una molécula de agua por unión.")],
    T=[
        ("abc", "En Química: ¿qué es un modelo?", "Una representación simplificada que permite explicar y predecir un fenómeno", "Un objeto idéntico al fenómeno real", "Una opinión sin supuestos", "Un modelo simplifica la realidad y declara sus supuestos para poder predecir."),
        ("=", "{F} ¿Cuánto vale el cociente superficie/volumen del cubo de lado 60 nm?", "6/60", "Se aplica la fórmula 6 dividido por el lado del cubo.", " por nm"),
        ("{F} ¿Qué cubo de la ficha (60 nm, 6 nm o 3 nm) tiene mayor cociente superficie/volumen?", "El de 3 nm", "Como el cociente es 6 ÷ L, el lado más pequeño da el cociente más grande."),
        ("=", "{F} ¿Cuánto vale el cociente del cubo de lado 6 nm?", "6/6", "Se divide 6 por el lado del cubo, que mide 6 nm.", " por nm"),
        ("abc", "{F} ¿Qué implica que un cubo tenga mayor cociente superficie/volumen?", "Que una fracción mayor de sus átomos está en la superficie y puede reaccionar", "Que tiene más masa total", "Que sus átomos son de otro elemento", "El cociente grande indica más superficie expuesta por cada unidad de volumen."),
        ("=", "{F} Una cadena de polietileno tiene 1.000 unidades de eteno. ¿Cuál es su masa molar aproximada?", "28*1000", "En una polimerización por adición la masa de la cadena es n por la masa del monómero.", " g/mol"),
        ("abc", "{F} ¿Por qué en el almidón se resta una molécula de agua en cada unión?", "Porque la polimerización por condensación libera agua al unir dos glucosas", "Porque el agua se agrega al final de la cadena", "Porque las glucosas pierden todos sus átomos", "En la condensación cada unión libera una molécula pequeña, aquí agua."),
        ("=", "{F} Una cadena de almidón de ejemplo tiene 10 unidades de glucosa. ¿Cuál es su masa molar aproximada?", "10*180-9*18", "Se suma la masa de las glucosas y se restan 9 uniones, una molécula de agua por cada una.", " g/mol"),
        ("=", "{F} Se compara un cubo de lado 12 nm con otro de lado 2 nm del mismo material. ¿Cuántas veces mayor es el cociente superficie/volumen del cubo de 2 nm?", "(6/2)/(6/12)", "Se calcula el cociente de cada cubo (3 y 0,5) y se divide el mayor por el menor.", " veces"),
        ("abc", "{F} Se compara polietileno (adición) y almidón (condensación) con n = 3 unidades cada uno. ¿Cuál tiene una masa menor que n por la masa de su monómero?", "El almidón, porque pierde agua en las uniones", "El polietileno, porque pierde agua en las uniones", "Ninguno: ambos pesan exactamente n por el monómero", "Solo en la condensación se libera agua y por eso baja la masa."),
        ("ab", "{F} ¿Qué supuesto hace el modelo del cubo?", "Que la partícula tiene forma de cubo perfecto", "Que todas las partículas reales son idénticas entre sí", "El modelo solo usa la forma de cubo; no describe formas reales irregulares."),
        ("=", "{F} Una cadena de almidón de ejemplo tiene 5 unidades de glucosa. ¿Cuál es su masa molar aproximada?", "5*180-4*18", "Se suma la masa de 5 glucosas y se restan 4 moléculas de agua, una por unión.", " g/mol"),
        ("abc", "{F} Un estudiante dice: «un polímero real tiene todas sus cadenas del mismo largo, como en el modelo». ¿Qué respondes?", "En un plástico real hay cadenas de largos distintos; el modelo las simplifica", "Es correcto: en la realidad todas miden igual", "El largo de las cadenas no importa nunca", "Un modelo declara su supuesto de cadenas iguales, que en la realidad no se cumple."),
    ],
    ctx=("abc", "Contexto: una empresa de ejemplo ofrece un filtro con partículas de lado 3 nm y dice que reacciona mejor que uno con partículas de lado 60 nm del mismo material. ¿Qué argumento del modelo del cubo respalda esa idea?", "Las partículas más pequeñas tienen mayor cociente superficie/volumen y exponen más átomos", "Las partículas pequeñas pesan más", "El tamaño de las partículas no cambia nada", "El modelo explica que más superficie por volumen significa más átomos disponibles para reaccionar."),
    sc=[
        ("En Química: ¿qué es una polimerización por condensación?", "Unión de monómeros que libera una molécula pequeña, como agua", "En la condensación cada unión suelta una molécula pequeña."),
        ("ab", "Si el lado del cubo disminuye, el cociente superficie/volumen:", "Aumenta", "Disminuye", "El cociente 6 ÷ L crece cuando L baja."),
        ("ab", "Un modelo siempre debe indicar:", "Sus supuestos y límites", "Que es idéntico a la realidad", "Declarar supuestos permite saber hasta dónde sirve."),
    ],
    op=("Con la ficha {F}: (1) calcula el cociente de los tres cubos y ordénalos de menor a mayor; (2) explica en dos oraciones qué significa para la reactividad; (3) escribe un supuesto del modelo del cubo y un caso real donde falle.",
        "(1) 60 nm: 0,1; 6 nm: 1; 3 nm: 2; orden 0,1 < 1 < 2. (2) El cubo de 3 nm expone más átomos por unidad de volumen, así que puede reaccionar más rápido. (3) Supone forma de cubo; falla con partículas irregulares o agrupadas.",
        ["tres cocientes correctos", "orden correcto", "explicación con superficie", "supuesto y caso donde falla"],
        ["tres respuestas numeradas"],
        ["dividir al revés (L ÷ 6)", "ordenar de mayor a menor", "no declarar ningún supuesto"],
        "Pregunta: «¿qué dato real contrastaría tu modelo?»."),
    reinforce="Calcula el cociente superficie/volumen de cubos de lado 1, 2 y 12 nm y escribe qué pasa con la reactividad esperada.",
    extend="Explica por qué dos plásticos con el mismo monómero pueden tener propiedades distintas si el largo de sus cadenas es distinto.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (datos de ejemplo). Ensayo agrícola de ejemplo con tres parcelas iguales de cultivo, con el mismo suelo y riego. Parcela 1 (fertilizante convencional): rendimiento 4.000 kg; nitrato en el agua de drenaje 50 mg/L. "
     "Parcela 2 (fertilizante con nanopartículas): rendimiento 4.400 kg; nitrato en el agua de drenaje 30 mg/L. Parcela 3 (sin fertilizante): rendimiento 2.500 kg; nitrato en el agua de drenaje 10 mg/L. "
     "Resultados de ejemplo de un recubrimiento nano para un envase: pérdida de agua del alimento en una semana en cuatro envases: 8, 6, 7 y 7 gramos (envase sin recubrimiento: 12 gramos). "
     "Dato de ejemplo en salud: una nanopartícula transporta un medicamento y lo libera en un tejido; se midió cuánto llega a ese tejido: 30 % con el transporte, 10 % sin él.")
build(
    O1, 4, F,
    use="Aprenderé a analizar evidencia sobre aplicaciones de la nanoquímica y los polímeros en lo agrícola, lo médico y lo industrial, calculando cambios porcentuales y promedios. Sirve para ver beneficios y consecuencias con datos y no con impresiones.",
    prior=["Sé calcular un promedio.", "Sé calcular un porcentaje.", "Sé leer una tabla de resultados."],
    explain=[
        "Analizar evidencia es leer los datos, calcular lo necesario y decir qué sí y qué no permiten concluir. Una herramienta básica es el cambio porcentual: se resta el valor de comparación del valor nuevo, se divide por el valor de comparación y se multiplica por 100. Si una parcela pasa de 4.000 a 4.400 kg, el cambio es 400 ÷ 4.000 × 100, es decir, 10 %.",
        "Otra herramienta es el promedio, que resume varios valores sumándolos y dividiendo por la cantidad. Sirve para repeticiones de una misma medición. Pero un promedio no muestra cuánto varían los datos: conviene mirar también el valor menor y el mayor, que forman el rango.",
        "Las aplicaciones de la nanoquímica y los polímeros pueden tener beneficios y consecuencias a la vez. Un nanofertilizante puede aumentar el rendimiento y reducir la pérdida de nitrato al agua, pero faltan datos de largo plazo sobre su efecto en el suelo. Un nanotransportador puede llevar más medicamento al tejido que necesita, pero se debe evaluar qué pasa con las partículas que no llegan. Una conclusión sólida dice qué mejora, cuánto y con qué incertidumbre.",
    ],
    vocab=[("cambio porcentual", "diferencia entre el valor nuevo y el de comparación, dividida por el de comparación y multiplicada por 100"), ("promedio", "suma de los valores dividida por la cantidad de valores"), ("rango", "diferencia entre el valor mayor y el menor"), ("rendimiento", "cantidad de cosecha obtenida en una parcela"), ("incertidumbre", "lo que no se sabe con seguridad a partir de los datos")],
    worked=[
        ("Cambio porcentual", "Con los datos de la ficha, ¿qué porcentaje de aumento tiene la parcela 2 respecto de la parcela 1 en nitrato de drenaje? ¿Aumenta o disminuye?",
         ["Valor de comparación: 50 mg/L; valor nuevo: 30 mg/L.", "Diferencia: 30 − 50 = −20.", "Cambio: −20 ÷ 50 × 100 = −40 %, es decir, disminuye 40 %."],
         "Disminuye 40 %"),
        ("Promedio y rango", "Con los cuatro envases recubiertos de la ficha (8, 6, 7 y 7 gramos), calcula el promedio de agua perdida.",
         ["Suma: 8 + 6 + 7 + 7 = 28.", "Cantidad de valores: 4.", "Promedio: 28 ÷ 4 = 7 gramos."],
         "7 gramos"),
    ],
    mistakes=[("Calcular el cambio porcentual dividiendo por el valor nuevo.", "El porcentaje de cambio se mide respecto del valor de comparación, no del nuevo.", "Divide siempre por el valor de partida o de comparación."),
              ("Decir que el nanofertilizante «es mejor en todo» porque rinde más.", "Los datos muestran más rendimiento y menos nitrato en el drenaje, pero no hablan de efectos a largo plazo ni de costos.", "Separa lo que muestran los datos de lo que aún no se sabe.")],
    T=[
        ("abc", "En Química: ¿qué es el cambio porcentual?", "La diferencia entre el valor nuevo y el de comparación, dividida por el de comparación y multiplicada por 100", "La suma de dos valores dividida por 100", "El valor mayor menos el menor", "Se mide la diferencia relativa respecto del valor de partida."),
        ("{F} ¿Qué parcela tuvo el mayor rendimiento?", "La parcela 2, con 4.400 kg", "Entre 4.000, 4.400 y 2.500 kg, el valor más alto es 4.400 kg."),
        ("{F} ¿Qué parcela tuvo menos nitrato en el agua de drenaje?", "La parcela 3, con 10 mg/L", "Entre 50, 30 y 10 mg/L el menor valor es 10 mg/L, en la parcela sin fertilizante."),
        ("=", "{F} ¿Cuántos kilogramos más rindió la parcela 2 que la parcela 1?", "4400-4000", "Se resta el rendimiento de la parcela 1 al de la parcela 2.", " kg"),
        ("=", "{F} ¿Cuál es el cambio porcentual de rendimiento de la parcela 2 respecto de la parcela 1?", "(4400-4000)*100/4000", "Se divide la diferencia por el rendimiento de comparación (parcela 1) y se multiplica por 100.", " %"),
        ("=", "{F} En tres días distintos se midió el nitrato en el drenaje de la parcela 2: 28, 30 y 32 mg/L. ¿Cuál es el promedio?", "(28+30+32)/3", "Se suman las tres mediciones y se divide por la cantidad de días.", " mg/L"),
        ("=", "{F} Un envase sin recubrimiento perdió 12 gramos. Los cuatro envases recubiertos perdieron 8, 6, 7 y 7 gramos. ¿Cuántos gramos menos perdieron en promedio los recubiertos?", "12-(8+6+7+7)/4", "Se resta el promedio del recubrimiento al valor sin recubrimiento.", " gramos"),
        ("=", "{F} ¿Cuál es el rango de la pérdida de agua de los cuatro envases recubiertos?", "8-6", "El rango es el valor mayor (8) menos el menor (6) de los cuatro envases.", " gramos"),
        ("=", "{F} Con el transportador nano llega 30 % del medicamento al tejido y sin él 10 %. ¿Cuántas veces más medicamento llega con el transportador?", "30/10", "Se divide el porcentaje que llega con transporte por el que llega sin él.", " veces"),
        ("abc", "{F} La parcela 2 muestra más rendimiento y menos nitrato en el drenaje que la 1. ¿Qué conclusión es correcta?", "En este ensayo el nanofertilizante mejoró el rendimiento y bajó el nitrato, pero faltan datos de largo plazo", "El nanofertilizante es seguro para siempre", "El nanofertilizante empeora el rendimiento", "La conclusión se limita a lo medido e indica lo que falta."),
        ("abc", "{F} Un agricultor dice: «como la parcela 3 tiene el menor nitrato, no conviene usar ningún fertilizante». ¿Qué falta considerar?", "Que la parcela 3 también tiene el menor rendimiento, y hay que ponderar ambos", "Nada: el nitrato es lo único importante", "Que la parcela 3 tiene el mayor rendimiento", "La decisión debe considerar rendimiento y nitrato juntos, no solo uno."),
        ("ab", "{F} ¿Qué pregunta ayuda más a evaluar el nanofertilizante a largo plazo?", "¿Cómo cambia el suelo tras varias temporadas de uso?", "¿Cuántos kilos pesó la parcela 3 una sola vez?", "Un efecto a largo plazo se evalúa con mediciones repetidas durante varias temporadas."),
        ("=", "{F} ¿Cuál es el cambio porcentual del rendimiento de la parcela 3 (sin fertilizante) respecto de la parcela 1?", "(2500-4000)*100/4000", "Se divide la diferencia (−1.500 kg) por el rendimiento de comparación y se multiplica por 100; el signo negativo indica disminución.", " %"),
    ],
    ctx=("abc", "Contexto: una cooperativa agrícola de ejemplo debe decidir si prueba el nanofertilizante en una parcela pequeña. ¿Qué decisión es la más razonable según los datos de la ficha?", "Probarlo a escala pequeña, midiendo rendimiento, nitrato y suelo en varias temporadas", "Usarlo en todos los campos ya, sin medir nada", "Descartarlo, porque la parcela 3 tuvo menos nitrato", "Una prueba piloto con mediciones permite reducir la incertidumbre antes de decidir."),
    sc=[
        ("En Química: ¿qué es el rango de un conjunto de datos?", "La diferencia entre el valor mayor y el menor", "El rango muestra qué tan separados están los datos."),
        ("ab", "El cambio porcentual se divide por:", "El valor de comparación", "El valor nuevo", "Se mide respecto del valor de partida."),
        ("ab", "Una conclusión sólida sobre una aplicación nano incluye:", "Lo que mejora, cuánto y la incertidumbre", "Solo los beneficios", "Mostrar incertidumbre y beneficios ayuda a decidir con más información."),
    ],
    op=("Con los datos de la ficha {F}: (1) calcula el cambio porcentual de rendimiento de la parcela 2 respecto de la 1; (2) calcula el cambio porcentual del nitrato en el drenaje; (3) escribe una conclusión sobre el nanofertilizante en dos oraciones y una pregunta que falta responder.",
        "(1) +10 %. (2) −40 %. (3) En este ensayo el nanofertilizante aumentó el rendimiento y redujo el nitrato en el drenaje. Falta saber qué efecto tiene en el suelo tras varias temporadas.",
        ["dos cambios porcentuales correctos", "signo interpretado", "conclusión acotada", "pregunta pendiente"],
        ["tres respuestas numeradas"],
        ["dividir por el valor nuevo", "perder el signo del cambio", "concluir seguridad total"],
        "Pregunta: «¿qué otra variable medirías para decidir?»."),
    reinforce="Calcula el cambio porcentual del nitrato en el drenaje de la parcela 3 respecto de la parcela 1 e interpreta el signo.",
    extend="Explica por qué un buen resultado en una parcela no basta para decidir su uso en todo un país.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (datos de ejemplo). Tres soluciones de ejemplo para reducir el desecho de envases plásticos de un liceo. Solución X: reciclaje mecánico (el plástico termoplástico se tritura, se funde y se moldea de nuevo). "
     "Solución Y: reducir el uso, reemplazando envases desechables por otros reutilizables. Solución Z: envases de un bioplástico que se degrada en condiciones industriales, no en el patio. "
     "Puntajes de ejemplo de 1 (malo) a 3 (bueno) y pesos de los criterios (peso × puntaje): "
     "criterio costo, peso 2: X = 2, Y = 3, Z = 1; criterio residuo que queda, peso 3: X = 2, Y = 3, Z = 2; criterio facilidad de aplicar en el liceo, peso 1: X = 3, Y = 2, Z = 1.")
build(
    O1, 5, F,
    use="Aprenderé a comparar soluciones de materiales y polímeros con una matriz de criterios y pesos, considerando consecuencias ambientales, industriales y de costo. Sirve para decidir con razones y reconocer los límites de la decisión.",
    prior=["Sé multiplicar y sumar.", "Sé qué es un termoplástico y un monómero.", "Sé justificar una elección con criterios."],
    explain=[
        "Comparar soluciones es elegir con criterios explícitos, no por gusto. Primero se definen los criterios, por ejemplo costo, residuo generado y facilidad de aplicar. Después se decide cuánto pesa cada criterio, porque no todos importan igual, y se da un puntaje a cada solución. El resultado de cada solución es la suma de peso por puntaje en todos los criterios.",
        "En polímeros, la distinción entre termoplásticos y termoestables es clave. Un termoplástico se ablanda con calor y se puede fundir y moldear de nuevo, por lo que admite reciclaje mecánico. Un termoestable, una vez formado, no se ablanda al calentarlo, y por eso es más difícil de reciclar de esa forma. Reducir el uso de un material suele generar menos residuo que reciclarlo, aunque puede costar cambios de hábitos.",
        "Una matriz da un orden, pero depende de los pesos y puntajes que alguien eligió. Si se cambian los pesos, el orden puede cambiar. Por eso, una decisión responsable muestra sus criterios, prueba qué pasa si se cambian y reconoce lo que no se midió, como el efecto de largo plazo de un material nuevo.",
    ],
    vocab=[("criterio", "aspecto con el que se juzga una solución"), ("peso", "importancia que se da a un criterio"), ("termoplástico", "polímero que se ablanda con calor y se puede moldear de nuevo"), ("termoestable", "polímero que no se ablanda al calentarlo una vez formado"), ("reciclaje mecánico", "trituración, fusión y nuevo moldeado de un termoplástico")],
    worked=[
        ("Puntaje total de una solución", "Con la matriz de la ficha, ¿cuál es el puntaje total de la solución X?",
         ["Costo: peso 2 × puntaje 2 = 4.", "Residuo: peso 3 × puntaje 2 = 6; facilidad: peso 1 × puntaje 3 = 3.", "Total: 4 + 6 + 3 = 13."],
         "13 puntos"),
        ("Efecto de cambiar un peso", "Si el peso del criterio costo pasara de 2 a 4, ¿cuánto sube el total de la solución Y?",
         ["Puntaje de Y en costo: 3.", "El producto pasa de 2 × 3 = 6 a 4 × 3 = 12.", "Sube 12 − 6 = 6 puntos."],
         "Sube 6 puntos"),
    ],
    mistakes=[("Elegir la solución que más gusta sin definir criterios.", "Sin criterios, la decisión no se puede justificar ni comparar con la de otra persona.", "Define criterios y pesos antes de puntuar."),
              ("Creer que el resultado de la matriz es un hecho indiscutible.", "El resultado depende de los pesos y puntajes elegidos.", "Prueba un cambio de pesos y declara qué no se midió.")],
    T=[
        ("abc", "En Química: ¿qué es un termoplástico?", "Un polímero que se ablanda con calor y se puede moldear de nuevo", "Un polímero que no se ablanda al calentarlo", "Un metal que se funde en un horno", "El termoplástico se funde y se moldea otra vez, por eso admite reciclaje mecánico."),
        ("{F} ¿Qué solución propone reducir el uso de envases desechables?", "La solución Y", "La solución Y reemplaza los envases desechables por reutilizables."),
        ("{F} ¿Qué solución necesita que el plástico sea termoplástico para poder aplicarse?", "La solución X", "El reciclaje mecánico funde y moldea de nuevo, algo que solo permite un termoplástico."),
        ("=", "{F} ¿Cuál es el puntaje total de la solución Y?", "2*3+3*3+1*2", "Se multiplica el peso de cada criterio por el puntaje de Y y se suman los tres resultados.", " puntos"),
        ("=", "{F} ¿Cuál es el puntaje total de la solución Z?", "2*1+3*2+1*1", "Se multiplica el peso por el puntaje de Z en cada criterio y se suma.", " puntos"),
        ("{F} Ordenando las tres soluciones por puntaje total, ¿cuál queda en segundo lugar?", "La solución X, con 13 puntos", "Los totales son Y = 17, X = 13 y Z = 9, así que X queda en el medio."),
        ("abc", "{F} ¿Por qué el criterio «residuo que queda» tiene peso 3 y «facilidad» peso 1?", "Porque en esta decisión se considera más importante reducir el residuo que la facilidad", "Porque 3 es siempre mayor que 1 por regla", "Porque el residuo es más fácil de medir", "El peso expresa la importancia que se decidió dar a cada criterio."),
        ("=", "{F} Si el peso de «facilidad» subiera de 1 a 4, ¿cuánto subiría el puntaje total de X?", "4*3-1*3", "Se resta el producto antiguo al nuevo con el puntaje de X en facilidad, que es 3.", " puntos"),
        ("=", "{F} Si el peso de «costo» subiera a 5 (y los demás pesos siguen igual), ¿cuál sería el puntaje total de la solución Y?", "5*3+3*3+1*2", "Se multiplica cada peso por el puntaje de Y, usando 5 en costo, y se suman los tres productos.", " puntos"),
        ("abc", "{F} Un estudiante afirma: «el bioplástico Z se degrada, así que es la mejor solución». ¿Qué falta considerar?", "Que solo se degrada en condiciones industriales y no en el patio", "Nada: se degrada siempre en cualquier lugar", "Que el bioplástico no es un polímero", "La ficha limita la degradación a condiciones industriales, lo que cambia su efecto real."),
        ("ab", "{F} ¿Qué conclusión es más honesta sobre el resultado de la matriz?", "Y obtiene el mayor puntaje con estos pesos y puntajes de ejemplo, que podrían cambiarse", "Y es la mejor solución en cualquier situación", "El resultado depende de los pesos y puntajes elegidos, y debe declararse."),
        ("abc", "Un material se calienta y no se ablanda ni se puede moldear de nuevo. ¿Cómo se clasifica?", "Termoestable", "Termoplástico", "Monómero", "El termoestable no se ablanda al calentarlo una vez formado."),
        ("=", "{F} ¿Cuántos puntos más tiene Y que X en el criterio de residuo, considerando el peso?", "3*3-3*2", "Se calcula peso por puntaje de Y y de X en residuo y se restan.", " puntos"),
    ],
    ctx=("abc", "Contexto: tu liceo de ejemplo debe elegir una solución para sus envases con la matriz de la ficha, y un grupo propone ignorar el costo. ¿Qué respuesta es la más razonable?", "Mantener el costo como criterio, mostrar cómo cambia el resultado al variar su peso y decidir con esa información", "Eliminar el costo sin explicar por qué", "Elegir la solución que más guste al grupo", "Una buena decisión muestra criterios y prueba su sensibilidad a los pesos."),
    sc=[
        ("En Química: ¿qué es un termoestable?", "Un polímero que no se ablanda al calentarlo una vez formado", "Por eso no se puede moldear de nuevo con calor."),
        ("ab", "Los pesos de una matriz expresan:", "La importancia que se da a cada criterio", "La masa de cada material", "Cada criterio tiene un peso según su importancia."),
        ("ab", "Si cambian los pesos de una matriz, el orden de las soluciones:", "Puede cambiar", "Nunca cambia", "El orden depende de los pesos elegidos."),
    ],
    op=("Con la matriz de la ficha {F}: (1) calcula el total de las tres soluciones; (2) cambia el peso de un criterio a tu elección y recalcula el orden; (3) escribe una recomendación en tres oraciones que incluya una limitación.",
        "(1) X = 13; Y = 17; Z = 9. (2) Con peso 1 en residuo: X = 4 + 2 + 3 = 9; Y = 6 + 3 + 2 = 11; Z = 2 + 2 + 1 = 5; el orden se mantiene. (3) Recomiendo Y porque tiene el mejor puntaje. Su limitación es que exige cambios de hábito. No se midió el costo real de reemplazar envases.",
        ["tres totales correctos", "recalculo con un peso distinto", "recomendación con razones", "limitación declarada"],
        ["tres respuestas numeradas"],
        ["sumar sin multiplicar por el peso", "no recalcular al cambiar el peso", "no declarar limitaciones"],
        "Pregunta: «¿qué criterio nuevo agregarías?»."),
    reinforce="Rehace la matriz con un cuarto criterio de tu elección, por ejemplo «efecto en el ambiente», y recalcula los totales.",
    extend="Explica por qué reducir el uso de un material suele ser mejor que reciclarlo y qué puede dificultar aplicarlo.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (datos de ejemplo). Constante: a 25 °C, el producto [H+] × [OH−] es 10 elevado a −14, por lo que pH + pOH = 14, con pOH = −log[OH−]. pH = −log[H+]; en esta ficha las concentraciones son potencias de diez, así que el pH es el número que queda sin el signo menos del exponente. "
     "Tres sistemas de ejemplo: agua de lluvia con [H+] = 10 elevado a −6; jugo de limón con [H+] = 10 elevado a −2; solución de limpieza con [H+] = 10 elevado a −11 (concentraciones en mol/L). "
     "Números de oxidación que se entregan: H = +1, O = −2, Na = +1, Cl = −1, Fe = 0 (hierro metálico). Reacción de óxido-reducción de ejemplo: el hierro metálico pasa a ion Fe con carga 3+ y pierde 3 electrones. "
     "Polimerización-despolimerización de ejemplo: el almidón se rompe en unidades de glucosa por reacción con agua (hidrólisis).")
build(
    O2, 1, F,
    use="Aprenderé a delimitar el sistema y la pregunta para explicar fenómenos ácido-base, de óxido-reducción y de polimerización-despolimerización en la naturaleza y en la tecnología. Sirve para saber qué se estudia y qué datos se necesitan antes de explicar.",
    prior=["Sé qué son un ion y una molécula.", "Sé leer potencias de diez.", "Sé distinguir un cambio químico de uno físico."],
    explain=[
        "Los fenómenos ácido-base, de óxido-reducción y de polimerización-despolimerización aparecen en el suelo, el agua, el cuerpo y la tecnología. En un fenómeno ácido-base se transfieren iones hidrógeno (H+): un ácido los cede y una base los recibe. La acidez se mide con el pH, que es −log[H+]. Si [H+] es 10 elevado a −6, el pH es 6; cada unidad menos de pH significa diez veces más H+.",
        "En un fenómeno de óxido-reducción se transfieren electrones. Se llama oxidación a la pérdida de electrones, y reducción a la ganancia. El número de oxidación es la carga que tendría un átomo si los electrones se asignaran por completo a un solo átomo. En un compuesto neutro, la suma de los números de oxidación de todos sus átomos es cero. Cuando el hierro metálico pasa de 0 a 3+, se oxida; quien recibe esos electrones se reduce.",
        "En polimerización-despolimerización, muchas unidades pequeñas se unen en una cadena y luego la cadena se rompe de nuevo en unidades. Así el cuerpo construye proteínas y rompe almidón en glucosa al digerir. Para explicar cualquiera de estos fenómenos, primero se delimita el sistema, es decir, qué sustancias y qué condiciones se consideran, y luego la pregunta: qué se cambia y qué se mide.",
    ],
    vocab=[("pH", "medida de la acidez de una disolución: −log[H+]"), ("ácido", "sustancia que cede iones H+"), ("base", "sustancia que recibe iones H+"), ("oxidación", "pérdida de electrones"), ("reducción", "ganancia de electrones")],
    worked=[
        ("Calcular un pH", "Con la ficha, el agua de lluvia tiene [H+] = 10 elevado a −6 mol/L. ¿Cuál es su pH?",
         ["pH = −log[H+].", "Como [H+] es 10 elevado a −6, el exponente es −6.", "El pH es 6."],
         "pH 6"),
        ("Identificar oxidación", "En la reacción del hierro de la ficha (Fe de 0 a 3+ perdiendo 3 electrones), ¿el hierro se oxida o se reduce?",
         ["El hierro pasa de número de oxidación 0 a +3.", "Para llegar a +3 tuvo que perder electrones.", "Perder electrones es oxidarse."],
         "Se oxida"),
    ],
    mistakes=[("Pensar que un pH más bajo significa menos ácido.", "A menor pH, mayor concentración de H+ y mayor acidez.", "Recuerda: pH bajo es ácido, pH alto es básico, con 7 como valor neutro a 25 °C."),
              ("Confundir oxidación con ganar electrones.", "La oxidación es pérdida de electrones; la ganancia es reducción.", "Usa la regla: se oxida el que pierde electrones y se reduce el que los gana.")],
    T=[
        ("abc", "En Química: ¿qué mide el pH?", "La acidez de una disolución a partir de la concentración de H+", "La temperatura de la disolución", "La masa de soluto disuelto", "El pH se define con la concentración de iones H+, no con la temperatura ni la masa."),
        ("{F} ¿Cuál es el pH del jugo de limón de ejemplo ([H+] = 10 elevado a −2)?", "pH 2", "El exponente es −2, así que el pH es 2."),
        ("{F} ¿Cuál es el pH de la solución de limpieza de ejemplo ([H+] = 10 elevado a −11)?", "pH 11", "El exponente es −11, así que el pH es 11."),
        ("abc", "{F} ¿Cuál de los tres sistemas (lluvia, limón o limpieza) es el más ácido?", "El jugo de limón, por su pH más bajo (2)", "La solución de limpieza, por su pH de 11", "El agua de lluvia, por su pH de 6", "Cuanto menor es el pH, mayor es la acidez."),
        ("=", "{F} A 25 °C el pH + pOH vale 14. Si el pH del agua de lluvia de ejemplo es 6, ¿cuánto vale su pOH?", "14-6", "Se resta el pH a 14 porque pH y pOH suman 14 a 25 °C.", ""),
        ("abc", "{F} Si el hierro pasa de 0 a +3 perdiendo electrones, ¿qué le ocurre al hierro?", "Se oxida", "Se reduce", "Se neutraliza", "Perder electrones y aumentar el número de oxidación es oxidarse."),
        ("=", "{F} ¿Cuántas veces mayor es [H+] en el jugo de limón de ejemplo que en el agua de lluvia de ejemplo? (potencias de diez: 10 elevado a −2 frente a 10 elevado a −6)", "10*10*10*10", "La diferencia de 4 unidades de pH equivale a 10 multiplicado cuatro veces, es decir, 10.000 veces.", " veces"),
        ("abc", "En el óxido de hierro Fe2O3, el oxígeno tiene número de oxidación −2 y la suma total es cero. ¿Cuál es el número de oxidación del hierro?", "+3", "+2", "−3", "Hay 3 oxígenos: 3 × (−2) = −6; los 2 hierros deben sumar +6, así que cada uno es +3."),
        ("abc", "{F} Se quiere explicar por qué un sistema de ejemplo (agua de lluvia) tiene pH 6. ¿Qué pregunta delimita mejor el sistema?", "¿Qué cantidad de H+ hay en el agua de lluvia y qué sustancias disueltas la explican?", "¿Es mala el agua de lluvia?", "¿Qué pasa con los ácidos en el mundo?", "Una pregunta delimitada nombra el sistema y una variable que se puede medir."),
        ("ab", "{F} Un estudiante dice que el almidón se «despolimeriza» en la digestión. ¿Qué quiere decir?", "Que la cadena de almidón se rompe en unidades de glucosa al reaccionar con agua", "Que se forma una cadena más larga de almidón", "Despolimerizar es lo opuesto a polimerizar: se rompe la cadena en sus unidades."),
        ("abc", "{F} La solución de limpieza de ejemplo tiene pH 11. ¿Cómo se clasifica a 25 °C?", "Básica", "Ácida", "Neutra", "A 25 °C el pH mayor que 7 indica una disolución básica."),
        ("abc", "Un estudiante afirma: «si el pH baja de 6 a 5, el H+ aumenta solo un poco». ¿Qué respondes?", "El H+ aumenta 10 veces, porque cada unidad de pH es un factor de diez", "Es correcto: sube un poco", "El H+ disminuye 10 veces", "La escala de pH es logarítmica: una unidad menos es diez veces más H+."),
        ("{F} En el NaCl el sodio pasa de 0 a +1 al formarse. Si el cloro pasa de 0 a −1, ¿cuántos electrones gana cada átomo de cloro?", "Un electrón", "Pasar de 0 a −1 significa ganar un electrón, que es el que pierde el sodio."),
    ],
    ctx=("abc", "Contexto: en una piscina de ejemplo el sensor entrega pH 8 y la persona encargada debe comunicar si la acidez es mayor o menor que la del agua de lluvia de la ficha (pH 6). ¿Qué dice?", "Menor, porque pH 8 tiene menos H+ que pH 6", "Mayor, porque 8 es mayor que 6", "Igual, porque ambos son cercanos a 7", "Mayor pH significa menor concentración de H+, es decir, menos acidez."),
    sc=[
        ("En Química: ¿qué es una reducción?", "Ganancia de electrones", "En una reducción el átomo gana electrones y baja su número de oxidación."),
        ("ab", "Una disolución con pH 3 es:", "Ácida", "Básica", "Un pH menor que 7 indica acidez a 25 °C."),
        ("ab", "Despolimerizar significa:", "Romper una cadena en sus unidades", "Unir unidades en una cadena", "Es el proceso contrario a la polimerización."),
    ],
    op=("Con la ficha {F}: (1) elige un sistema (lluvia, limón, limpieza, hierro o almidón) y escribe una pregunta delimitada sobre él; (2) indica qué variable cambiarías y cuál medirías; (3) escribe qué dato de la ficha usarías como evidencia.",
        "(1) Sistema: agua de lluvia. ¿Cómo cambia el pH si aumenta la cantidad de dióxido de carbono disuelto? (2) Cambiaría la cantidad de CO2 disuelto y mediría el pH. (3) Usaría el pH 6 de la lluvia como valor de comparación.",
        ["sistema elegido", "pregunta delimitada", "variable que cambia y variable que se mide", "evidencia de la ficha"],
        ["tres respuestas numeradas"],
        ["hacer una pregunta sin variable medible", "confundir variable que cambia con la que se mide", "no usar ningún dato"],
        "Pregunta: «¿qué sistema agregarías para comparar?»."),
    reinforce="Calcula el pH de tres disoluciones de ejemplo con [H+] iguales a 10 elevado a −3, −8 y −12 y clasifícalas como ácidas o básicas.",
    extend="Explica por qué la escala de pH es logarítmica y qué consecuencia tiene que una diferencia de 2 unidades sea un cambio de 100 veces.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (datos de ejemplo de un análisis no experimental: se leen resultados ya publicados). Fuente 1: informe de monitoreo de un lago con método descrito, que reporta pH de 6, 7 y 8 en tres puntos, medidos con el mismo instrumento calibrado. "
     "Fuente 2: comentario sin datos que dice «el lago está muy ácido». Tabla de ejemplo de una neutralización estudiada con lápiz y papel: 20 mL de ácido de concentración 0,1 mol/L se neutralizan con una base de concentración desconocida y se gastan 10 mL; la relación entre ácido y base es 1 a 1. "
     "Regla usada: concentración del ácido × volumen del ácido = concentración de la base × volumen de la base. "
     "Tabla de ejemplo de una pila de zinc y cobre: voltaje 1,1 V con soluciones al mismo nivel; 0,9 V cuando la solución de cobre es mucho más diluida.")
build(
    O2, 2, F,
    use="Aprenderé a evaluar fuentes y variables en estudios ácido-base y de pilas: qué se cambia, qué se mide y cómo se calcula una concentración desconocida con una regla de neutralización. Sirve para explicar fenómenos con datos confiables.",
    prior=["Sé la idea de pH y de oxidación y reducción.", "Sé multiplicar y dividir con decimales simples.", "Sé qué es una variable independiente y dependiente."],
    explain=[
        "Una investigación puede ser experimental, si se manipula una variable, o no experimental, si se analizan datos ya registrados. En esta clase se trabaja con la segunda: se leen informes, se evalúa su confiabilidad y se calculan resultados con los datos entregados. Una fuente confiable describe el instrumento, el método y los puntos de medición, y no solo da una opinión.",
        "En la neutralización, un ácido y una base reaccionan y forman una sal y agua. Si la reacción es 1 a 1, se cumple que la concentración del ácido por su volumen es igual a la de la base por su volumen. Con esa regla se calcula una concentración desconocida cuando se conocen las otras tres cantidades. Por ejemplo, 0,1 × 20 = C × 10 da C = 0,2 mol/L.",
        "En una pila, una reacción de óxido-reducción produce una diferencia de potencial eléctrico llamada voltaje. El electrodo donde ocurre la oxidación es el ánodo; el de la reducción es el cátodo, y los electrones fluyen del ánodo al cátodo. El voltaje depende de las sustancias y de las concentraciones. Para comparar condiciones hay que cambiar una variable a la vez.",
    ],
    vocab=[("neutralización", "reacción entre un ácido y una base que forma una sal y agua"), ("concentración", "cantidad de soluto por litro de disolución, en mol/L"), ("ánodo", "electrodo donde ocurre la oxidación"), ("cátodo", "electrodo donde ocurre la reducción"), ("voltaje", "diferencia de potencial eléctrico de una pila")],
    worked=[
        ("Concentración de una base", "Con los datos de la ficha, ¿cuál es la concentración de la base?",
         ["Regla: concentración del ácido × volumen del ácido = concentración de la base × volumen de la base.", "0,1 × 20 = C × 10, es decir, 2 = C × 10.", "C = 2 ÷ 10 = 0,2."],
         "0,2 mol/L"),
        ("Variable que cambió", "En la tabla de la pila de la ficha, ¿qué variable se cambió entre 1,1 V y 0,9 V?",
         ["Los electrodos y las sustancias fueron las mismas.", "Lo que cambió fue la concentración de la solución de cobre.", "El voltaje es lo que se midió como efecto."],
         "La concentración de la solución de cobre"),
    ],
    mistakes=[("Usar la regla de neutralización 1 a 1 sin comprobar que la relación sea 1 a 1.", "Si el ácido o la base liberan más de un H+ u OH−, la regla cambia.", "Antes de usarla, revisa la relación entre las cantidades de ácido y base."),
              ("Creer que el voltaje de una pila es siempre el mismo para los mismos metales.", "También depende de las concentraciones de las disoluciones.", "Anota las condiciones de concentración junto con el voltaje.")],
    T=[
        ("abc", "En Química: ¿qué es una neutralización?", "Reacción entre un ácido y una base que forma una sal y agua", "Cualquier reacción que libera calor", "La pérdida de electrones de un metal", "La neutralización es la reacción ácido-base típica."),
        ("{F} ¿Qué fuente (1 o 2) describe instrumento calibrado y puntos de medición?", "La fuente 1", "La fuente 1 muestra método, instrumento y puntos; la 2 solo opina."),
        ("{F} ¿Cuál es el pH medido más bajo en el lago, según la fuente 1?", "pH 6", "Entre 6, 7 y 8 el menor valor es 6, que indica el punto más ácido."),
        ("=", "Un ácido de concentración 0,2 mol/L, 30 mL, se neutraliza con una base 1 a 1. Si se usa una base de 0,3 mol/L, ¿qué volumen se necesita, en mL? Usa la regla de la ficha.", "0.2*30/0.3", "Se despeja el volumen de la base: concentración del ácido por su volumen, dividido por la de la base.", " mL"),
        ("=", "{F} Otro ácido de 0,1 mol/L y 50 mL se neutraliza con 20 mL de base. ¿Cuál es la concentración de la base?", "0.1*50/20", "Se aplica la regla y se despeja la concentración de la base.", " mol/L"),
        ("abc", "{F} ¿Por qué la fuente 2 («muy ácido») no es suficiente como evidencia?", "Porque no entrega datos, método ni instrumento", "Porque es demasiado breve para ser escrita", "Porque no usa la palabra pH", "Una opinión sin datos no se puede evaluar ni repetir."),
        ("abc", "{F} En la pila de la ficha, ¿qué ocurre en el ánodo?", "Oxidación", "Reducción", "Neutralización", "El ánodo es el electrodo donde ocurre la oxidación."),
        ("{F} ¿Cuál es la variable que se midió en la pila: concentración, voltaje o tipo de metal?", "El voltaje", "El voltaje es el efecto que se mide, y la concentración es lo que se cambió."),
        ("=", "{F} ¿Cuántos voltios bajó el voltaje de la pila al diluir la solución de cobre (de 1,1 a 0,9 V)?", "(11-9)/10", "Se resta el voltaje final al inicial (11 y 9 décimas de voltio).", " V"),
        ("abc", "{F} Un estudiante concluye: «la pila de zinc y cobre siempre da 1,1 V». ¿Qué responde la tabla?", "No: con la solución de cobre más diluida dio 0,9 V", "Sí: es un valor fijo", "Sí, porque 0,9 V no es un voltaje", "La tabla muestra que el voltaje cambia con la concentración."),
        ("ab", "{F} Para atribuir la baja de 1,1 a 0,9 V a la concentración, ¿qué se debe mantener igual?", "Los metales, la temperatura y las demás condiciones", "El valor de voltaje que se quiere medir", "Controlar las demás variables permite atribuir el cambio a la concentración."),
        ("abc", "{F} El pH 8 medido en un punto del lago, ¿cómo se clasifica a 25 °C?", "Básico", "Ácido", "Neutro", "A 25 °C, un pH mayor que 7 indica una disolución básica."),
        ("=", "{F} Un ácido de 0,5 mol/L y 10 mL se neutraliza con una base de 0,25 mol/L, relación 1 a 1. ¿Cuántos mL de base se usan?", "0.5*10/0.25", "Se aplica la regla y se despeja el volumen de la base.", " mL"),
    ],
    ctx=("abc", "Contexto: una comunidad de ejemplo recibe un informe del agua de un estero con pH 4 en un punto cercano a una faena minera, según un instrumento calibrado. Una vecina dice que «seguro hay un error». ¿Qué conviene hacer?", "Pedir el método y repetir la medición en otros puntos para confirmar el valor", "Descartar el informe sin revisarlo", "Aceptarlo como definitivo sin mirar el método", "Un resultado sorprendente se contrasta con método y repetición antes de aceptarse o descartarse."),
    sc=[
        ("En Química: ¿qué es el ánodo de una pila?", "El electrodo donde ocurre la oxidación", "En el ánodo el metal pierde electrones."),
        ("ab", "Una investigación no experimental:", "Analiza datos ya registrados", "Manipula variables en un laboratorio", "No experimental significa no intervenir y analizar registros."),
        ("ab", "La regla de neutralización 1 a 1 sirve para:", "Calcular una concentración o volumen desconocido", "Calcular la masa de un metal", "Relaciona concentración y volumen de ácido y base."),
    ],
    op=("Con la ficha {F}: (1) clasifica las fuentes 1 y 2 según su confiabilidad con un criterio cada una; (2) calcula la concentración de la base; (3) indica qué variable cambió y cuál se midió en la tabla de la pila, y una limitación.",
        "(1) La fuente 1 es más confiable porque describe método e instrumento; la 2 es una opinión sin datos. (2) 0,2 mol/L. (3) Cambió la concentración de cobre y se midió el voltaje. Limitación: solo hay dos concentraciones.",
        ["clasificación con criterios", "cálculo de la base", "variables bien identificadas", "limitación"],
        ["tres respuestas numeradas"],
        ["confundir cambiar con medir", "sin criterio para la fuente", "olvidar la relación 1 a 1"],
        "Pregunta: «¿qué tercer valor de concentración agregarías?»."),
    reinforce="Calcula la concentración de una base si 0,3 mol/L de ácido en 20 mL se neutraliza con 15 mL de base 1 a 1.",
    extend="Explica por qué una pila entrega menos voltaje al diluir una de sus soluciones, usando la idea de concentración.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (datos de ejemplo). Modelo de la sangre humana como sistema regulado: el pH normal está alrededor de 7,4 y el cuerpo mantiene ese valor con sistemas amortiguadores. "
     "Un amortiguador de ejemplo contiene un ácido débil y su base conjugada: si llegan H+, la base los recibe; si llegan OH−, el ácido los neutraliza. "
     "Modelo de la corrosión del hierro: el hierro metálico (Fe) se oxida a ion Fe con carga 3+ y el oxígeno del aire (O2) se reduce; la presencia de agua facilita la reacción. "
     "Pila de ejemplo: Zn pasa a Zn con carga 2+ en el ánodo (pierde 2 electrones); Cu con carga 2+ pasa a Cu metálico en el cátodo (gana 2 electrones). "
     "Modelo de polimerización-despolimerización del almidón: 10 glucosas (180 g/mol cada una) forman almidón perdiendo 9 moléculas de agua (18 g/mol cada una).")
build(
    O2, 3, F,
    use="Aprenderé a interpretar tres modelos: el amortiguador de pH, la corrosión y la pila como oxidación-reducción, y la polimerización-despolimerización como ganancia y pérdida de agua. Sirve para explicar fenómenos de sistemas naturales y de la tecnología.",
    prior=["Sé qué es el pH.", "Sé que oxidar es perder electrones.", "Sé calcular masas molares sumando."],
    explain=[
        "Un amortiguador, o tampón, es una mezcla que resiste los cambios de pH. Contiene un ácido débil y su base conjugada, que es la especie que queda cuando ese ácido cede un H+. Si llegan H+ adicionales, la base los recibe; si llegan OH−, el ácido los neutraliza. Gracias a sistemas así, la sangre mantiene su pH cerca de 7,4, y los lagos y suelos reducen cambios bruscos de acidez. Si el amortiguador se agota, el pH sí cambia.",
        "La corrosión del hierro es un proceso de óxido-reducción. El hierro se oxida y entrega electrones; el oxígeno del aire los recibe y se reduce. El agua facilita el movimiento de las cargas. En una pila de zinc y cobre ocurre algo parecido, pero ordenado: el zinc se oxida en el ánodo, los electrones circulan por un conductor hacia el cátodo y allí el ion cobre se reduce a cobre metálico. La suma de las semirreacciones debe conservar los electrones: los que se pierden son los que se ganan.",
        "En la polimerización-despolimerización, el almidón se forma al unir glucosas con pérdida de agua y se rompe, al digerirlo, agregando agua. Con 10 glucosas, la masa del polímero es 10 × 180 − 9 × 18. Cada modelo es una simplificación: el amortiguador tiene una capacidad límite, la corrosión depende de muchas condiciones y el almidón real tiene cadenas ramificadas.",
    ],
    vocab=[("amortiguador (tampón)", "mezcla que resiste los cambios de pH"), ("semirreacción", "parte de una reacción redox que muestra solo la pérdida o la ganancia de electrones"), ("corrosión", "oxidación lenta de un metal por su ambiente"), ("hidrólisis", "ruptura de un enlace por reacción con agua"), ("conservación de la carga", "los electrones perdidos son los ganados")],
    worked=[
        ("Balance de electrones", "En la pila de la ficha, Zn pierde 2 electrones y Cu2+ gana 2. ¿Cuántos electrones pasan por el conductor por cada átomo de zinc que se oxida?",
         ["El zinc pierde 2 electrones al oxidarse.", "Esos electrones viajan por el conductor.", "El cobre los gana: 2 electrones por átomo de Zn."],
         "2 electrones"),
        ("Masa del almidón", "¿Cuál es la masa molar del almidón de la ficha (10 glucosas)?",
         ["Masa de las 10 glucosas: 10 × 180 = 1.800.", "Agua perdida en 9 uniones: 9 × 18 = 162.", "1.800 − 162 = 1.638."],
         "1.638 g/mol"),
    ],
    mistakes=[("Creer que un amortiguador impide por completo que el pH cambie.", "Resiste cambios solo mientras tenga suficiente ácido débil y base conjugada.", "Escribe «resiste cambios hasta cierto límite»."),
              ("Balancear una semirreacción sin igualar los electrones.", "Los electrones perdidos en la oxidación deben ser los ganados en la reducción.", "Multiplica las semirreacciones hasta igualar los electrones.")],
    T=[
        ("abc", "En Química: ¿qué es un amortiguador (tampón)?", "Una mezcla que resiste los cambios de pH", "Una sustancia que siempre baja el pH", "Un metal que conduce electrones", "El amortiguador contiene un ácido débil y su base conjugada para resistir cambios de pH."),
        ("{F} ¿Cuál es el pH normal de la sangre humana según la ficha?", "Alrededor de 7,4", "La ficha entrega el valor 7,4 como pH normal."),
        ("{F} En el modelo de corrosión, ¿qué sustancia se oxida?", "El hierro", "El hierro entrega electrones y pasa de 0 a +3."),
        ("abc", "{F} En un amortiguador de la ficha, ¿qué ocurre si llegan H+ adicionales?", "La base conjugada los recibe", "El ácido débil los neutraliza", "Se agota el agua", "La base conjugada reacciona con los H+ y evita un gran cambio de pH."),
        ("abc", "{F} En la pila de zinc y cobre, ¿dónde ocurre la reducción?", "En el cátodo, donde el ion cobre gana electrones", "En el ánodo, donde el zinc gana electrones", "En el conductor, donde se funde el metal", "La reducción ocurre en el cátodo, con ganancia de electrones."),
        ("{F} ¿Cuántos átomos de zinc deben oxidarse para reducir 6 iones de cobre con carga 2+ a cobre metálico?", "6 átomos de zinc", "Cada átomo de zinc entrega 2 electrones y cada ion cobre recibe 2, por lo que se corresponden uno a uno."),
        ("=", "{F} Una cadena de almidón de ejemplo tiene 20 glucosas. ¿Cuántas moléculas de agua se pierden al formarse?", "20-1", "Con 20 unidades hay 19 uniones y una molécula de agua por cada una.", " moléculas de agua"),
        ("=", "{F} ¿Cuál es la masa molar de una cadena de almidón de ejemplo de 6 glucosas?", "6*180-5*18", "Se suma la masa de las 6 glucosas y se restan 5 moléculas de agua.", " g/mol"),
        ("abc", "{F} Un estudiante dice: «el amortiguador de la sangre nunca falla». ¿Qué responde el modelo?", "Resiste cambios solo mientras tenga ácido débil y base conjugada suficientes", "Es cierto: nunca falla", "Falla siempre ante cualquier cambio", "El modelo indica una capacidad límite del amortiguador."),
        ("abc", "{F} Si el hierro se oxida pero no hubiera nada que reciba sus electrones, ¿qué ocurriría?", "No ocurriría la oxidación, porque los electrones perdidos deben ser ganados por otra especie", "El hierro se oxidaría más rápido", "Se formaría más agua", "Una oxidación siempre ocurre junto con una reducción."),
        ("ab", "{F} ¿Qué enunciado explica la despolimerización del almidón?", "Se agregan moléculas de agua que rompen las uniones entre glucosas", "Se pierde más agua y las cadenas crecen", "La hidrólisis agrega agua para romper las uniones."),
        ("abc", "{F} Se recubre un clavo de hierro con una capa de zinc, que se oxida primero. ¿Por qué ayuda a proteger al hierro?", "Porque el zinc se oxida en lugar del hierro y le cede los electrones", "Porque el zinc reduce el agua", "Porque el zinc impide que el oxígeno exista", "El zinc se oxida antes que el hierro, protegiendo a este mientras haya zinc."),
        ("=", "{F} Una cadena de almidón tiene 100 glucosas. ¿Cuántos g/mol resta el agua perdida en la polimerización (masa de agua 18 g/mol)?", "99*18", "Se multiplican las 99 uniones por la masa del agua perdida en cada una.", " g/mol"),
    ],
    ctx=("abc", "Contexto: un lago de ejemplo recibe lluvia ácida durante años, pero su pH casi no cambió hasta que, de pronto, bajó mucho. ¿Qué explicación del modelo es la más razonable?", "El amortiguador del lago se fue agotando hasta superar su capacidad", "El amortiguador nunca existió", "El agua dejó de tener H+", "Un tampón resiste por un tiempo, pero cuando se agota el pH cambia rápido."),
    sc=[
        ("En Química: ¿qué es una semirreacción?", "La parte de una reacción redox que muestra solo la pérdida o la ganancia de electrones", "Cada semirreacción muestra una de las dos mitades."),
        ("ab", "En una oxidación-reducción, los electrones perdidos:", "Son los ganados por otra especie", "Desaparecen sin destino", "La carga se conserva: lo que pierde uno lo gana otro."),
        ("ab", "La hidrólisis del almidón requiere:", "Agregar agua", "Quitar agua", "La hidrólisis rompe uniones con agua."),
    ],
    op=("Con los modelos de la ficha {F}: (1) elige uno de los tres modelos (amortiguador, corrosión/pila o almidón); (2) escribe qué explica y dos supuestos que hace; (3) propón un dato nuevo que permitiría ponerlo a prueba.",
        "(1) Amortiguador. (2) Explica por qué la sangre mantiene su pH cerca de 7,4; supone que hay ácido débil y base conjugada en cantidad suficiente y que el aporte de H+ es pequeño. (3) Medir el pH tras agregar cantidades crecientes de ácido a una disolución y ver cuándo cambia bruscamente.",
        ["modelo elegido", "qué explica", "dos supuestos", "dato de prueba"],
        ["tres respuestas numeradas"],
        ["no declarar supuestos", "decir que el modelo es la realidad", "proponer un dato que no pone a prueba nada"],
        "Pregunta: «¿en qué condición dejaría de servir tu modelo?»."),
    reinforce="Calcula la masa molar de una cadena de almidón de 3, 5 y 8 glucosas y ordénalas de menor a mayor.",
    extend="Explica por qué el hierro protegido con zinc se corroe más lento, usando los conceptos de oxidación y reducción.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (datos de ejemplo). Serie de pH de un lago de ejemplo medido cada 5 años con el mismo instrumento: año 0: 7,5; año 5: 7,0; año 10: 6,5; año 15: 6,0. "
     "Corrosión de ejemplo: masa perdida por un clavo de hierro en agua tras 10 días: agua dulce 20 mg; agua con sal 50 mg; agua dulce con una capa de zinc: 2 mg. "
     "Despolimerización de ejemplo: botellas de PET de la misma masa (10 g) se rompen en sus unidades por la acción de una enzima en condiciones controladas; masa que ya se rompió tras 24 h: temperatura 20 °C: 1 g; 30 °C: 2 g; 40 °C: 4 g. "
     "Pila de ejemplo: corriente producida por una pila recién hecha: 100 mA; tras 10 horas de uso: 60 mA.")
build(
    O2, 4, F,
    use="Aprenderé a analizar evidencia numérica de procesos ácido-base, de corrosión, de despolimerización y de pilas, calculando cambios, tasas y factores. Sirve para explicar qué ocurre en sistemas naturales y en la tecnología a partir de datos.",
    prior=["Sé qué es el pH y cómo se interpreta.", "Sé calcular diferencias y cocientes.", "Sé qué es la corrosión y la despolimerización."],
    explain=[
        "Analizar evidencia es describir la tendencia de los datos y calcular lo necesario. Si el pH de un lago baja de 7,5 a 6,0 en 15 años, la tendencia es de acidificación. Como el pH es logarítmico, una baja de 1 unidad significa diez veces más H+: de 7,0 a 6,0 el H+ aumenta 10 veces, y la baja total de 1,5 unidades no es un cambio pequeño.",
        "Una tasa es un cambio por unidad de tiempo. Si un clavo pierde 30 mg en 10 días, la tasa es 3 mg por día. Comparar tasas permite ver cuánto influye una condición: el agua con sal acelera la corrosión, porque las sales disueltas ayudan a conducir la carga, y una capa de zinc la frena porque el zinc se oxida en lugar del hierro. En despolimerización, subir la temperatura puede acelerar la ruptura de la cadena, como muestran los datos.",
        "Las pilas también se analizan con datos. La corriente baja con el uso porque las sustancias que reaccionan se van consumiendo. Una conclusión sólida dice qué muestran los datos, cuánto cambian y qué no se puede asegurar, por ejemplo qué pasaría en condiciones que no se midieron.",
    ],
    vocab=[("tendencia", "dirección general en que cambian los datos"), ("tasa", "cambio por unidad de tiempo"), ("acidificación", "disminución del pH de un sistema"), ("factor", "número por el que se multiplica una cantidad"), ("condición", "valor de una variable en un ensayo")],
    worked=[
        ("Tasa de pérdida", "Con los datos de la ficha, ¿cuál es la tasa de pérdida del clavo en agua con sal?",
         ["Masa perdida en 10 días: 50 mg.", "Tasa = 50 mg ÷ 10 días.", "5 mg por día."],
         "5 mg/día"),
        ("Factor entre condiciones", "¿Cuántas veces es mayor la masa de PET que se rompió a 40 °C que a 20 °C?",
         ["Masa a 40 °C: 4 g; masa a 20 °C: 1 g.", "Se divide: 4 ÷ 1.", "El factor es 4."],
         "4 veces"),
    ],
    mistakes=[("Decir que el lago se acidificó «poco» porque el pH bajó solo 1,5 unidades.", "En una escala logarítmica cada unidad es un factor de diez en H+.", "Interpreta la baja con el factor de 10 por cada unidad entera de pH."),
              ("Extender una tendencia fuera del rango medido.", "No hay datos de 50 °C ni de más años, y la tendencia puede cambiar.", "Escribe «en el rango medido».")],
    T=[
        ("abc", "En Química: ¿qué es una tasa?", "El cambio de una cantidad por unidad de tiempo", "La suma de dos mediciones", "El valor mayor de una tabla", "La tasa mide cuánto cambia algo en cada unidad de tiempo."),
        ("{F} ¿Qué tendencia muestra el pH del lago de ejemplo con los años?", "Disminuye, es decir, el lago se acidifica", "Los valores 7,5; 7,0; 6,5 y 6,0 son cada vez menores."),
        ("{F} ¿Qué condición del clavo (agua dulce, agua con sal o agua dulce con zinc) tuvo la mayor pérdida de masa?", "Agua con sal", "50 mg es el valor más alto de los tres."),
        ("=", "{F} ¿Cuál es la tasa de pérdida del clavo en agua dulce durante los 10 días?", "20/10", "Se divide la masa perdida por los días del ensayo.", " mg/día"),
        ("=", "{F} ¿Cuántas veces mayor fue la pérdida de masa del clavo en agua con sal que en agua dulce?", "50/20", "Se divide la pérdida con sal por la pérdida en agua dulce.", " veces"),
        ("abc", "{F} ¿Qué efecto tuvo la capa de zinc sobre la pérdida de masa del clavo?", "La redujo mucho (de 20 a 2 mg)", "La aumentó", "No la afectó", "Con zinc la pérdida fue de solo 2 mg frente a 20 mg sin él."),
        ("=", "{F} ¿Cuántas unidades bajó el pH del lago entre el año 0 y el año 15?", "7.5-6", "Se resta el pH del año 15 al del año 0.", " unidades"),
        ("=", "{F} ¿En cuántos mg se redujo la pérdida del clavo al agregar zinc (de 20 a 2 mg)?", "20-2", "Se resta la pérdida con zinc a la pérdida en agua dulce.", " mg"),
        ("abc", "{F} Si cada unidad entera de pH equivale a 10 veces más H+, ¿cuántas veces aumentó [H+] entre pH 7,0 (año 5) y pH 6,0 (año 15)?", "10 veces", "2 veces", "100 veces", "Entre pH 7,0 y 6,0 hay una unidad entera, es decir, un factor de 10."),
        ("=", "{F} ¿Cuántas veces mayor es la masa de PET rota a 40 °C que la rota a 30 °C?", "4/2", "Se divide la masa rota a 40 °C entre la masa rota a 30 °C.", " veces"),
        ("abc", "{F} ¿Qué conclusión sobre la temperatura apoyan los datos del PET?", "En el rango de 20 a 40 °C, a más temperatura se rompió más PET en 24 h", "A cualquier temperatura el PET se rompe más", "La temperatura no influye", "Los valores 1, 2 y 4 g crecen con la temperatura dentro del rango medido."),
        ("ab", "{F} Un estudiante propone: «a 100 °C se romperá 20 g de PET». ¿Qué problema tiene?", "Extiende la tendencia fuera del rango medido, que llega solo hasta 40 °C", "Ninguno: es una buena predicción", "Los datos no incluyen 100 °C ni más masa de la que había (10 g), así que la predicción no está respaldada."),
        ("=", "{F} ¿En qué porcentaje bajó la corriente de la pila tras 10 horas (de 100 a 60 mA)?", "(100-60)*100/100", "Se divide la baja de 40 mA por los 100 mA iniciales y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Contexto: una autoridad local de ejemplo debe comunicar a la comunidad qué muestran los datos del lago. ¿Qué mensaje es el más preciso?", "En 15 años el pH bajó de 7,5 a 6,0; el lago se acidificó, y conviene seguir midiendo", "El lago está bien porque el pH sigue sobre 6", "El lago se acidificará siempre al mismo ritmo", "El mensaje correcto describe la tendencia, el cambio medido y la necesidad de seguir midiendo."),
    sc=[
        ("En Química: ¿qué es la acidificación?", "Disminución del pH de un sistema", "Acidificar es bajar el pH, es decir, aumentar la concentración de H+."),
        ("ab", "Una tendencia en datos:", "Debe interpretarse solo en el rango medido", "Se cumple siempre fuera de lo medido", "No hay datos fuera del rango, así que no se puede asegurar."),
        ("ab", "El zinc sobre el hierro:", "Se oxida primero y protege al hierro", "Acelera la corrosión del hierro", "El zinc es el que se oxida y cede los electrones."),
    ],
    op=("Con los datos de la ficha {F}: (1) elige dos tablas y calcula una tasa o un factor en cada una; (2) escribe una conclusión de cada una; (3) escribe una limitación general de los datos.",
        "(1) Clavo: agua con sal 5 mg/día, 2,5 veces la de agua dulce (2 mg/día). PET: factor 4 entre 40 °C y 20 °C. (2) La sal acelera la corrosión; la temperatura acelera la ruptura del PET. (3) Solo hay tres condiciones y un ensayo por condición.",
        ["dos cálculos correctos", "dos conclusiones", "limitación general"],
        ["tres respuestas numeradas"],
        ["no mostrar el cálculo", "extender la tendencia fuera del rango", "confundir tasa con masa total"],
        "Pregunta: «¿qué condición agregarías para completar la tabla?»."),
    reinforce="Calcula la tasa de caída del pH del lago por cada 5 años y comprueba que sea constante.",
    extend="Explica por qué la sal acelera la corrosión del hierro y qué dato de la ficha lo respalda.",
)
