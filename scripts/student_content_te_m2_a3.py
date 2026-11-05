"""Cuaderno del estudiante, 2.º medio Tecnología: OA 03 (evaluar propuestas de solución considerando aspectos o dilemas éticos, legales, económicos, ambientales y sociales), clases 1 a 5.

Seguridad: las tareas son de lectura, cálculo y escritura. Las cifras y los casos son de ejemplo y no nombran marcas ni personas reales.
Vacío declarado: las normas legales se tratan en general (derechos de autor, datos personales, seguridad, ambiente); la normativa chilena concreta queda para el docente o un especialista.
"""
from __future__ import annotations

from student_content_te_m2_a import reg
from student_lessons import arith, ex

OA3 = "TE2M OA 03"

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir las cinco dimensiones para evaluar una propuesta (ética, legal, económica, ambiental y social) y a reconocer un dilema. Sirve para juzgar una solución con más que un «me gusta».",
    prior=["Sé redactar criterios con indicador y meta.", "Sé comparar alternativas con una matriz.", "Sé calcular porcentajes."],
    explain=[
        "Evaluar una propuesta es juzgarla con criterios y evidencia. Se miran cinco dimensiones. La ética pregunta qué es justo y honesto y a quién se respeta o se daña. La legal pregunta si cumple normas, como las de seguridad, los derechos de autor y la protección de datos personales. La económica compara costos y beneficios en dinero. La ambiental revisa el efecto en recursos, residuos y emisiones. La social revisa el efecto en las personas y su comunidad.",
        "Una propuesta rara vez es buena en todas las dimensiones a la vez. Un dilema aparece cuando dos de ellas chocan y hay que decidir. Por ejemplo, un material barato (dimensión económica) puede dejar más residuos (dimensión ambiental). Un dilema no se resuelve ocultando una dimensión, sino pesándolas con razones.",
        "Para analizar un dilema se siguen cuatro pasos: describirlo, identificar las dimensiones que chocan y a quiénes afecta, evaluar las opciones con criterios y decidir justificando con evidencia. En esta clase solo se identifican las dimensiones y los dilemas; en las siguientes se profundiza en cada una.",
    ],
    vocab=[("dimensión ética", "revisa si es justo, honesto y respetuoso con las personas"), ("dimensión legal", "revisa si cumple normas y leyes"), ("dimensión económica", "compara costos y beneficios en dinero"), ("dimensión ambiental", "revisa el efecto en recursos, residuos y emisiones"), ("dimensión social", "revisa el efecto en las personas y la comunidad"), ("dilema", "situación en que dos dimensiones chocan y hay que decidir")],
    worked=[
        ("Clasificar un argumento", "¿En qué dimensión cae «la propuesta ahorra $50.000 al año»?", ["Habla de dinero que se ahorra.", "Compara costos y beneficios en dinero."], "Económica"),
        ("Reconocer un dilema", "Una propuesta de ejemplo reduce el gasto, pero deja sin acceso a quienes no tienen celular. ¿Qué dimensiones chocan?", ["El ahorro es económico.", "La falta de acceso es un efecto social."], "La económica y la social"),
    ],
    mistakes=[
        ("Evaluar una propuesta solo por su costo.", "Deja fuera lo ético, lo legal, lo ambiental y lo social.", "Revisa las cinco dimensiones antes de decidir."),
        ("Pensar que un dilema se resuelve ignorando una dimensión.", "Ocultar una parte no la hace desaparecer, solo oculta quién sale perjudicado.", "Nombra las dimensiones que chocan y pésalas con razones."),
    ],
    R=[
        ("«Genera 20 kg menos de residuos al mes» corresponde a la dimensión… A) ambiental B) legal", "A", "Habla de residuos, que es un efecto sobre el ambiente."),
        ("«Todos los cursos pueden usarla, incluso quienes no tienen internet» corresponde a la dimensión… A) social B) económica", "A", "Se refiere al acceso de las personas."),
        ("«Cuesta $30.000 y ahorra $10.000 al año» corresponde a la dimensión… A) económica B) ética C) legal", "A", "Compara un costo y un ahorro en dinero."),
    ],
    C=[
        ("¿Qué es un dilema? A) una situación en que dos dimensiones chocan y hay que decidir B) una duda que se resuelve mirando el precio", "A", "Un dilema exige pesar valores en conflicto."),
        ("Una propuesta cumple todas las normas, pero excluye a estudiantes sin celular. ¿Qué dimensión muestra el problema? A) la social, por la falta de acceso B) la legal, porque rompe una norma", "A", "Cumple las normas, así que el problema es de acceso."),
        ("Evaluar con criterios significa… A) revisar la propuesta en varias dimensiones con evidencia B) votar la que más se parece al gusto personal", "A", "Los criterios y la evidencia reemplazan el gusto personal."),
    ],
    A=[
        ("Clasifica por dimensión: (1) «ahorra $40.000 al año», (2) «reduce 15 kg de residuos», (3) «beneficia a quienes viven lejos del liceo», (4) «usa imágenes con licencia que permite su uso».", "1 económica, 2 ambiental, 3 social, 4 legal", "Cada frase apunta a dinero, residuos, personas y normas, respectivamente."),
        arith("De 20 comentarios de ejemplo sobre una propuesta, 8 hablan de costos, 6 de ambiente y 4 de acceso. El resto habla de normas. ¿Cuántos hablan de normas?", "20-8-6-4", "Se restan los comentarios de las otras tres dimensiones del total.", " comentarios"),
        arith("De 50 estudiantes encuestados, 35 podrían usar la propuesta. ¿Qué porcentaje queda sin acceso?", "(50-35)*100//50", "Se calculan los que no pueden usarla y se pasan a porcentaje.", " %"),
    ],
    Z=[
        ("Una propuesta ahorra mucho dinero, pero genera más residuos. ¿Por qué es un dilema?", "Porque la dimensión económica y la ambiental chocan y hay que decidir cuál pesa más", "Cada dimensión apunta a una decisión distinta."),
        ("Un grupo dice: «Como la propuesta es legal, ya es ética». ¿Qué se le responde?", "Que algo permitido por una norma puede igual dañar a personas o al ambiente", "Legal y ético no significan lo mismo."),
    ],
    D=[
        ex("En una encuesta de ejemplo a 40 estudiantes, 24 ven favorable la propuesta en lo económico, 30 en lo ambiental y 18 en lo social. ¿En qué dimensión es mayor el porcentaje de apoyo y cuánto es?", "En la ambiental, 75 %", "30 de 40 equivale a 75 %; 24 es 60 % y 18 es 45 %.", calc="30*100//40"),
        arith("De 60 comentarios de ejemplo, el 45 % trata de costos. ¿Cuántos comentarios son?", "60*45//100", "Se calcula el 45 % de 60.", " comentarios"),
    ],
    ctx=arith("Un liceo de ejemplo gasta $90.000 al año en vasos desechables y gastaría $54.000 con vasos lavables. ¿Qué porcentaje ahorraría?", "(90000-54000)*100//90000", "Se calcula el ahorro y se divide entre el gasto inicial.", " %"),
    sc=[
        ("En Tecnología: ¿qué es un dilema?", "Una situación en que dos dimensiones chocan y hay que decidir", "Es la definición de la clase."),
        ("Nombra las cinco dimensiones para evaluar una propuesta.", "Ética, legal, económica, ambiental y social", "Son las cinco que se revisan siempre."),
        ("¿Qué dimensión revisa si se cumplen normas, como las de seguridad?", "La legal", "Las normas corresponden a esa dimensión."),
    ],
    open_task=(
        "Escoge un caso. Caso 1: un casino propone vasos de cartón desechables porque son más baratos que los lavables. Caso 2: un curso propone una planilla compartida para registrar el consumo, pero pide el nombre de cada estudiante. Caso 3: un taller propone unos recipientes de plástico nuevos para guardar retazos, que cuestan $20.000. Escribe un argumento por cada una de las cinco dimensiones y cierra señalando qué dilema aparece y entre qué dimensiones.",
        "Caso 1: económica, más barato; ambiental, más residuos; social, quienes lavan no pierden tiempo; ética, se pasa el costo al ambiente; legal, hay que cumplir normas de higiene; dilema entre la económica y la ambiental",
        ["escribe un argumento por dimensión", "los argumentos son distintos", "identifica un dilema real", "nombra las dimensiones que chocan"],
        ["hoja con cinco argumentos y el dilema"],
        ["repetir el mismo argumento", "no nombrar qué choca"],
        "Pregunta: «¿qué ganas y qué pierdes con esta propuesta?». Debe nombrar la dimensión de cada ganancia y pérdida.",
    ),
    reinforce="Elige una propuesta de tu curso y escribe una ventaja y un problema, indicando a qué dimensión corresponde cada uno.",
    extend="Explica por qué evaluar solo la dimensión económica puede llevar a una mala decisión.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los datos escritos en este cuaderno.",
    use="Aprenderé a calcular el período de recuperación, el ahorro neto y la ganancia durante la vida útil de una propuesta. Sirve para evaluar su dimensión económica con números y no con impresiones.",
    prior=["Sé calcular porcentajes.", "Sé que un costo y un ahorro se comparan en dinero.", "Sé dividir y multiplicar números enteros."],
    explain=[
        "La dimensión económica compara lo que cuesta una propuesta con lo que ahorra. El costo inicial es lo que se paga al empezar. El costo de mantención es el gasto de cada año para que siga funcionando. El ahorro neto anual es el ahorro del año menos la mantención de ese año. La vida útil es el número de años que la propuesta sirve.",
        "El período de recuperación dice en cuántos años el ahorro cubre el costo inicial: costo inicial ÷ ahorro neto anual. Si ese período es mayor que la vida útil, la propuesta no recupera su inversión. La ganancia durante la vida útil es: ahorro neto anual × años de vida útil − costo inicial. Si resulta negativa, económicamente se pierde.",
        "Un resultado económico malo no descarta por sí solo una propuesta, porque puede tener grandes beneficios ambientales o sociales. Pero hay que mostrarlo con claridad, para que quien decida sepa lo que cuesta cada beneficio. Una afirmación como «ahorra $100.000 al año» no sirve sin el costo inicial, la mantención y la vida útil.",
    ],
    vocab=[("costo inicial", "lo que se paga al empezar"), ("costo de mantención", "gasto anual para que siga funcionando"), ("ahorro neto anual", "ahorro del año menos la mantención"), ("vida útil", "años durante los cuales sirve"), ("período de recuperación", "años en que el ahorro cubre el costo inicial"), ("ganancia", "ahorro total en la vida útil menos el costo inicial")],
    worked=[
        ("Período de recuperación", "Una propuesta de ejemplo cuesta $120.000 y ahorra $40.000 al año. ¿En cuántos años recupera el costo inicial?", ["Uso costo inicial ÷ ahorro neto anual.", "Calculo 120.000 ÷ 40.000 = 3."], "3 años"),
        ("Ahorro neto y ganancia", "Ahorro del año $50.000, mantención $10.000, vida útil 5 años y costo inicial $150.000. ¿Qué ganancia tiene?", ["Ahorro neto: 50.000 − 10.000 = 40.000.", "En 5 años ahorra 200.000; menos 150.000 deja 50.000."], "$50.000 de ganancia"),
    ],
    mistakes=[
        ("Comparar propuestas solo por su costo inicial.", "Una más barata puede ahorrar menos o durar menos.", "Calcula también el ahorro neto, la vida útil y la ganancia."),
        ("Olvidar restar la mantención al ahorro.", "Se sobreestima lo que realmente se ahorra cada año.", "Calcula primero el ahorro neto: ahorro del año menos mantención."),
    ],
    R=[
        arith("Una propuesta de ejemplo cuesta $80.000 y ahorra $20.000 al año. ¿En cuántos años recupera el costo inicial?", "80000//20000", "Período = costo inicial ÷ ahorro neto anual.", " años"),
        ("¿Qué es el costo de mantención? A) el gasto de cada año para que siga funcionando B) el precio que se paga al comprarla", "A", "El precio de compra es el costo inicial."),
        ("El período de recuperación es de 6 años y la vida útil de 4 años. ¿Qué pasa? A) no recupera su costo inicial B) sí lo recupera", "A", "Deja de servir antes de cubrir lo que costó."),
    ],
    C=[
        ("Dos propuestas tienen el mismo ahorro neto anual y la misma vida útil. ¿Cuál es mejor solo en lo económico? A) la de menor costo inicial B) la de mayor costo inicial", "A", "Con igual ahorro y duración, conviene pagar menos al inicio."),
        ("¿Por qué no basta comparar solo el costo inicial? A) porque también cuentan el ahorro y la mantención durante los años de uso B) porque el costo inicial no importa", "A", "Una propuesta barata puede tener mantención alta o poco ahorro."),
        ("¿Cómo se calcula el ahorro neto anual? A) ahorro del año menos la mantención B) ahorro del año más el costo inicial", "A", "La mantención reduce lo que realmente se ahorra."),
    ],
    A=[
        arith("Una propuesta de ejemplo ahorra $52.000 al año y su mantención cuesta $12.000 al año. ¿Cuál es el ahorro neto anual?", "52000-12000", "Se resta la mantención al ahorro.", " pesos"),
        arith("Una propuesta cuesta $150.000 y su ahorro neto es de $25.000 al año. ¿En cuántos años recupera la inversión?", "150000//25000", "Se divide el costo inicial entre el ahorro neto.", " años"),
        arith("Una propuesta dura 8 años, ahorra $20.000 netos al año y costó $120.000. ¿Cuál es su ganancia en la vida útil?", "8*20000-120000", "Se calcula el ahorro total y se resta el costo inicial.", " pesos"),
    ],
    Z=[
        ("Una propuesta recupera su costo en 6 años y dura 4, pero reduce mucho los residuos. ¿Se descarta solo por eso?", "No: pierde en lo económico, pero se pesa con la dimensión ambiental", "Un mal resultado económico se compara con los beneficios en otras dimensiones."),
        ("Un aviso dice «ahorra $100.000 al año», sin más datos. ¿Qué falta para evaluarla en lo económico?", "El costo inicial, la mantención y la vida útil", "Sin esos datos no se puede calcular el período ni la ganancia."),
    ],
    D=[
        ex("Propuesta M: cuesta $60.000, ahorro neto $20.000 al año, vida útil 5 años. Propuesta N: cuesta $90.000, ahorro neto $27.000 al año, vida útil 5 años. ¿Cuál tiene mayor ganancia y de cuánto?", "N, $45.000", "M gana 100.000 − 60.000 = 40.000 y N gana 135.000 − 90.000 = 45.000.", calc="27000*5-90000"),
        arith("El ahorro neto anual de una propuesta de ejemplo es $24.000 y su costo inicial $120.000. ¿Qué porcentaje del costo inicial ahorra cada año?", "24000*100//120000", "Se divide el ahorro anual entre el costo inicial y se pasa a porcentaje.", " %"),
    ],
    ctx=arith("Cambiar a vasos lavables en un casino de ejemplo cuesta $75.000 y ahorra $15.000 netos al año. ¿En cuántos años recupera la inversión?", "75000//15000", "Se divide el costo inicial entre el ahorro neto anual.", " años"),
    sc=[
        ("¿Cómo se calcula el período de recuperación?", "Costo inicial ÷ ahorro neto anual", "Dice en cuántos años se cubre lo que costó."),
        ("¿Qué es la vida útil?", "Los años durante los cuales la propuesta sirve", "Se compara con el período de recuperación."),
        ("¿Un mal resultado económico descarta siempre una propuesta?", "No, se pesa con las otras dimensiones", "Puede tener beneficios ambientales o sociales."),
    ],
    open_task=(
        "Escoge una propuesta de ejemplo. Propuesta 1: lámparas de menor consumo para 10 salas, costo $60.000, ahorro $24.000 al año, mantención $4.000 al año, vida útil 6 años. Propuesta 2: contenedores de cartón reforzado para el patio, costo $45.000, ahorro $9.000 al año, mantención $1.000 al año, vida útil 4 años. Calcula ahorro neto, período de recuperación y ganancia, y escribe una conclusión económica que diga qué otras dimensiones habría que mirar.",
        "Propuesta 1: ahorro neto 20.000; recupera en 3 años; ganancia 120.000 − 60.000 = 60.000; conclusión, económicamente conviene y falta revisar lo ambiental y lo social",
        ["calcula el ahorro neto", "calcula el período y la ganancia", "concluye con los números", "menciona otras dimensiones por revisar"],
        ["hoja con cálculos y conclusión"],
        ["olvidar la mantención", "concluir solo por el costo inicial"],
        "Pregunta: «¿recupera lo que costó antes de que termine su vida útil?». La respuesta sale de comparar dos números.",
    ),
    reinforce="Elige un objeto de tu casa que se pueda reutilizar y calcula cuánto cuesta por uso si se usa 50 veces.",
    extend="Explica por qué una propuesta con mal resultado económico puede igualmente ser recomendada.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a distinguir lo legal de lo ético, a reconocer principios éticos y a aplicar pasos para analizar un dilema. Sirve para evaluar una propuesta más allá de si «se puede hacer».",
    prior=["Sé las cinco dimensiones para evaluar una propuesta.", "Sé qué es un dilema.", "Sé que los datos personales se usan con consentimiento."],
    explain=[
        "Lo legal es lo que las normas permiten o exigen: normas de seguridad, protección de datos personales, derechos de autor, normas ambientales. Lo ético es lo que es correcto hacer según principios como la honestidad, el respeto, la responsabilidad, la equidad y el cuidado del ambiente. Algo puede ser legal y aun así dañar a otras personas; por eso la dimensión ética se revisa aparte.",
        "Un test sencillo para lo ético usa tres preguntas: ¿a quién beneficia y a quién daña?, ¿lo aceptaría si me ocurriera a mí?, ¿podría contarlo en público sin ocultar nada? La transparencia consiste en mostrar los datos y las decisiones tal como son, también los resultados malos. Ocultar un resultado desfavorable rompe la honestidad.",
        "Para analizar un dilema ético se ordenan cuatro pasos: describir el dilema, identificar las partes afectadas y las dimensiones que chocan, evaluar las opciones con el test y decidir justificando. Las normas concretas de cada materia no se inventan: se consultan con el docente o con una persona especialista.",
    ],
    vocab=[("dimensión legal", "lo que las normas permiten o exigen"), ("principio ético", "valor que guía lo correcto, como honestidad o equidad"), ("equidad", "dar a cada persona lo que necesita para participar en igualdad"), ("transparencia", "mostrar datos y decisiones tal como son"), ("consentimiento", "permiso claro de una persona para usar sus datos o imagen"), ("partes afectadas", "personas o grupos a quienes alcanza la decisión")],
    worked=[
        ("Legal o ético", "Un equipo oculta que su prueba bajó la reducción de 25 % a 5 %. ¿Qué principio rompe?", ["Sabe un resultado y no lo muestra.", "Eso rompe la honestidad y la transparencia."], "Honestidad"),
        ("Aplicar el test", "Un curso propone cobrar una cuota a quien use el punto de acopio del barrio. ¿Qué pregunta del test revela el problema?", ["Pregunto «¿a quién daña?».", "Daña a quienes no pueden pagar."], "Daña a quienes no pueden pagar"),
    ],
    mistakes=[
        ("Creer que, si es legal, no hay nada más que revisar.", "Una norma fija mínimos, pero no cubre todos los daños posibles.", "Revisa también el test ético."),
        ("Ocultar un resultado malo para que la propuesta se vea mejor.", "Engaña a quienes deben decidir y rompe la honestidad.", "Muestra todos los datos y explica qué se hará para mejorar."),
    ],
    R=[
        ("Ocultar un resultado desfavorable rompe el principio de… A) honestidad B) equidad", "A", "Mostrar lo que pasó realmente es parte de la honestidad."),
        ("¿Cuál es una pregunta legal? A) ¿cumple las normas de seguridad y de datos personales? B) ¿le gusta al grupo?", "A", "Las normas y los datos personales son parte de lo legal."),
        ("¿Legal y ético significan lo mismo? A) no: algo permitido por una norma puede dañar a otras personas B) sí: lo permitido siempre es correcto", "A", "Una norma fija mínimos y no cubre todos los daños."),
    ],
    C=[
        ("Un equipo mide 10 % de ahorro, pero informa 30 % «para que se vea mejor». ¿Qué principio rompe? A) la honestidad B) la equidad", "A", "Informa un dato que no es verdadero."),
        ("La propuesta beneficia solo a los cursos que tienen computador. ¿Qué principio se ve afectado? A) la equidad B) la honestidad", "A", "No todas las personas pueden participar en igualdad."),
        ("Un estudiante copia un texto completo sin citar. ¿Qué se revisa primero? A) la dimensión legal y la honestidad, por los derechos de autor B) solo la dimensión económica, porque copiar no cuesta dinero", "A", "Usar una obra sin reconocer al autor tiene un problema legal y ético."),
    ],
    A=[
        ("El test ético pregunta «¿a quién daña?». Un curso propone cobrar $500 a cada persona que use un punto de acopio que sirve a todo el barrio. ¿A quién perjudica?", "A quienes no pueden pagar", "La cuota deja fuera a quienes no pueden pagar."),
        arith("En una consulta de ejemplo a 80 personas, 20 dicen que no entienden cómo se usarían sus datos. ¿Qué porcentaje no lo entiende?", "20*100//80", "Se calcula la proporción sobre el total y se pasa a porcentaje.", " %"),
        ("Ordena los pasos para analizar un dilema: (a) decidir y justificar, (b) identificar partes afectadas y dimensiones, (c) describir el dilema, (d) evaluar las opciones con el test.", "c, b, d, a", "Se parte describiendo y se termina decidiendo con razones."),
    ],
    Z=[
        ("Una norma de ejemplo no prohíbe repartir folletos impresos en todo el barrio, pero el curso sabe que casi todos terminan en el suelo. ¿Basta con que sea legal?", "No: puede ser legal y aun así generar residuos que dañan la comunidad", "Lo legal no agota lo ético."),
        ("El equipo recibe una crítica a su propuesta. ¿Actúa éticamente si la ignora y no la registra?", "No: debe registrarla y responderla por transparencia", "Ocultar críticas impide mejorar y engaña a quien decide."),
    ],
    D=[
        arith("De 160 estudiantes fotografiados para un informe de ejemplo, 40 no dieron su consentimiento. ¿Qué porcentaje no lo dio?", "40*100//160", "Se calcula la proporción y se pasa a porcentaje.", " %"),
        ex("Pesos acordados: ética 3, legal 3, económica 1. Propuesta uno: ética 1, legal 3, económica 3. Propuesta dos: ética 3, legal 2, económica 1. ¿Cuál suma más y cuánto?", "La propuesta dos, 16 puntos", "La uno suma 3 + 9 + 3 = 15 y la dos suma 9 + 6 + 1 = 16.", calc="3*3+3*2+1*1"),
    ],
    ctx=arith("Un equipo pide consentimiento a 24 compañeros para usar sus fotos en un afiche y 18 aceptan. ¿Qué porcentaje aceptó?", "18*100//24", "Se divide los que aceptaron entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("¿Es lo mismo que algo sea legal y que sea ético?", "No", "Lo legal fija mínimos y lo ético mira también los daños."),
        ("En Tecnología: ¿qué es la transparencia?", "Mostrar datos y decisiones tal como son", "Incluye mostrar los resultados malos."),
        ("¿Cuál es el primer paso para analizar un dilema?", "Describirlo", "Antes de evaluar hay que saber qué choca."),
    ],
    open_task=(
        "Escoge un dilema. Dilema 1: un curso gana un concurso de reciclaje si publica una foto de sus compañeros, pero dos de ellos no quieren salir. Dilema 2: un equipo logró una reducción de 12 % y la meta era 20 %, pero el informe final debe mostrar buenos resultados. Dilema 3: un colegio propone un punto de acopio solo para quienes pagan una cuota. Sigue los cuatro pasos (describir, partes afectadas y dimensiones, evaluar opciones con el test y decidir justificando) y señala qué parte es legal y cuál ética.",
        "Dilema 2: describir, informar 12 % cuando la meta era 20 %; afectados, quienes leerán el informe; opción honesta, mostrar el dato y un plan de mejora; decisión, informar 12 % con transparencia; lo ético es la honestidad",
        ["sigue los cuatro pasos", "nombra a las partes afectadas", "separa lo legal de lo ético", "justifica con razones"],
        ["hoja con los cuatro pasos"],
        ["decidir sin evaluar opciones", "confundir legal con ético"],
        "Pregunta: «¿qué le dirías al grupo si el dato se hiciera público?». Si cambia de respuesta, falló el test de transparencia.",
    ),
    reinforce="Escribe un caso cotidiano donde algo sea legal pero discutible desde lo ético, y explica por qué.",
    extend="Explica por qué la transparencia obliga a mostrar también los resultados desfavorables.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a evaluar el ciclo de vida de una propuesta, a calcular su balance ambiental y a identificar a quiénes beneficia o perjudica. Sirve para decidir con las dimensiones ambiental y social.",
    prior=["Sé el ciclo de vida de un material.", "Sé qué es equidad.", "Sé calcular porcentajes."],
    explain=[
        "La evaluación ambiental revisa todo el ciclo de vida de la propuesta: la fabricación, el uso y el desecho. No basta con mirar solo cuando funciona, porque fabricar las piezas también gasta energía y materiales. El balance ambiental compara lo que la propuesta evita con lo que ella misma gasta o genera. Por ejemplo, si evita 40 kg de residuos y genera 15 kg, el balance es 25 kg a favor.",
        "La evaluación social revisa a quiénes alcanza la propuesta. Un grupo de interés es toda persona o grupo afectado por la decisión: estudiantes, docentes, auxiliares, vecinos. Se pregunta quién se beneficia, quién se perjudica, si todos pueden acceder y si alguien queda fuera por dónde vive, por una discapacidad o por falta de conexión.",
        "Una matriz de impactos ordena esta información: en filas van las dimensiones o los grupos y en columnas los beneficios y los perjuicios, con cifras cuando existen. Si una propuesta perjudica a un grupo, no se ignora aunque sea pequeño: se propone una medida de compensación o un cambio.",
    ],
    vocab=[("ciclo de vida", "fabricación, uso y desecho de la propuesta"), ("balance ambiental", "lo que se evita menos lo que se gasta o genera"), ("grupo de interés", "persona o grupo afectado por la decisión"), ("acceso", "posibilidad real de usar la propuesta"), ("matriz de impactos", "tabla de beneficios y perjuicios por dimensión o grupo"), ("compensación", "medida que repara o reduce un perjuicio")],
    worked=[
        ("Balance ambiental", "Una propuesta evita 40 kg de residuos al mes y genera 15 kg al fabricarse. ¿Cuál es el balance?", ["Resto lo que genera de lo que evita.", "Calculo 40 − 15 = 25."], "25 kg a favor"),
        ("Ver quién queda fuera", "Un punto de reciclaje se instala en un segundo piso sin rampa ni ascensor. ¿A quién perjudica?", ["Pregunto quién no puede llegar hasta allí.", "Quedan fuera quienes no pueden subir escaleras."], "A personas con movilidad reducida"),
    ],
    mistakes=[
        ("Evaluar el efecto ambiental solo durante el uso.", "Se ignoran la fabricación y el desecho, que también gastan recursos.", "Revisa las tres etapas del ciclo de vida."),
        ("Ignorar a un grupo porque es pequeño.", "Una persona perjudicada sigue siendo una persona perjudicada.", "Registra el perjuicio y propone una medida de compensación."),
    ],
    R=[
        ("La evaluación ambiental debe considerar… A) fabricación, uso y desecho de la propuesta B) solo el uso", "A", "Cada etapa gasta recursos."),
        ("Un grupo de interés es… A) una persona o grupo afectado por la propuesta B) la persona que la inventó", "A", "Se define por ser afectado, no por haberla creado."),
        arith("Una propuesta evita 70 kg de residuos y genera 25 kg al fabricarse. ¿Cuál es su balance ambiental?", "70-25", "Se resta lo que genera de lo que evita.", " kg"),
    ],
    C=[
        ("El punto de reciclaje queda en un segundo piso sin rampa ni ascensor. ¿A quién perjudica en lo social? A) a quienes no pueden subir escaleras B) a todas las personas por igual", "A", "El acceso físico limita a un grupo."),
        ("Una propuesta reduce emisiones, pero exige fabricar 500 piezas de plástico nuevas. ¿Qué se hace con esas piezas? A) se cuentan como impacto de la fabricación B) se ignoran porque se usarán después", "A", "La fabricación forma parte del ciclo de vida."),
        ("¿Qué muestra una matriz de impactos? A) beneficios y perjuicios por dimensión y por grupo B) solo el precio de la propuesta", "A", "Reúne la información para decidir."),
    ],
    A=[
        arith("Una propuesta usa 15 kg de cartón nuevo para fabricarse y evita 5 kg de residuos al mes. ¿En cuántos meses lo evitado iguala el cartón usado?", "15//5", "Se divide el material usado entre lo que se evita cada mes.", " meses"),
        arith("De 150 estudiantes de ejemplo, 120 se benefician con la propuesta. ¿Qué porcentaje se beneficia?", "120*100//150", "Se divide los beneficiados entre el total y se pasa a porcentaje.", " %"),
        ("Clasifica como ambiental (A) o social (S): (1) empleo para un vecino del barrio, (2) menos agua usada, (3) acceso para una estudiante con discapacidad visual.", "1 S, 2 A, 3 S", "El empleo y el acceso afectan a personas; el agua es un recurso."),
    ],
    Z=[
        ("Una propuesta beneficia al 90 % de la comunidad, pero perjudica con ruido a quienes viven junto al punto de acopio. ¿Se puede ignorar al 10 %?", "No: se reconoce el perjuicio y se busca cambiar la ubicación o compensar", "Un perjuicio no desaparece por afectar a menos personas."),
        ("Un equipo mide solo el uso y concluye que su solución es muy buena para el ambiente. ¿Qué error cometió?", "No evaluó todo el ciclo de vida: faltan fabricación y desecho", "Las etapas omitidas también gastan recursos."),
    ],
    D=[
        ex("Propuesta P: evita 50 kg de residuos y genera 20 kg. Propuesta Q: evita 45 kg y genera 5 kg. ¿Cuál tiene mayor balance ambiental y de cuánto?", "La Q, 40 kg", "P tiene 50 − 20 = 30 kg y Q tiene 45 − 5 = 40 kg.", calc="45-5"),
        arith("De 10 cursos, 6 pueden acceder a la propuesta. Con una rampa nueva podrán 8. ¿Cuántos puntos sube el porcentaje de cursos con acceso (por ejemplo, de 10 % a 15 % son 5 puntos)?", "8*100//10-6*100//10", "Se compara el porcentaje de acceso antes y después.", " puntos"),
    ],
    ctx=arith("Se fabrican 4 contenedores de 3 kg de cartón cada uno y se evitan 8 kg de residuos al mes. ¿Cuál es el balance neto después de 3 meses?", "8*3-4*3", "Se compara lo evitado en 3 meses con el cartón usado.", " kg"),
    sc=[
        ("¿Qué etapas tiene el ciclo de vida de una propuesta?", "Fabricación, uso y desecho", "Las tres gastan recursos."),
        ("En Tecnología: ¿qué es un grupo de interés?", "Una persona o grupo afectado por la decisión", "Puede beneficiarse o perjudicarse."),
        ("¿Cómo se calcula el balance ambiental?", "Lo que se evita menos lo que se gasta o genera", "Muestra el resultado neto."),
    ],
    open_task=(
        "Escoge un caso de ejemplo. Caso 1: un punto de acopio de papel en el patio evita 30 kg de residuos al mes y se fabrica con 10 kg de cartón; queda al fondo del patio, lejos de la rampa de acceso. Caso 2: una cartelera digital reemplaza los avisos de papel y evita 12 kg de papel al mes, pero solo la ven quienes tienen conexión. Caso 3: contenedores nuevos evitan 25 kg de residuos al mes y usan 20 kg de plástico nuevo. Calcula el balance, escribe una matriz con beneficios y perjuicios por grupo de interés y propone una medida de compensación.",
        "Caso 1: balance de 20 kg el primer mes; beneficiados, toda la comunidad; perjudicados, quienes no pueden llegar; compensación, un contenedor cerca de la rampa",
        ["calcula el balance", "nombra al menos dos grupos de interés", "señala un perjuicio", "propone una compensación"],
        ["hoja con matriz y compensación"],
        ["ignorar la fabricación", "no nombrar a quién perjudica"],
        "Pregunta: «¿quién podría quedar fuera?». Debe nombrar un grupo concreto antes de proponer la compensación.",
    ),
    reinforce="Elige un objeto que uses y anota qué se necesita para fabricarlo, usarlo y desecharlo.",
    extend="Explica por qué una propuesta puede ser buena para el ambiente y aun así injusta con un grupo.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a integrar las cinco dimensiones en una matriz con pesos, a descartar propuestas que incumplen normas y a emitir una recomendación con condiciones y seguimiento. Sirve para tomar una decisión justificada.",
    prior=["Sé evaluar cada una de las cinco dimensiones.", "Sé usar pesos y puntajes en una matriz.", "Sé calcular porcentajes."],
    explain=[
        "La evaluación final integra las cinco dimensiones. Primero se descarta o se corrige toda propuesta que incumple una norma. Luego se fijan los pesos de las dimensiones según la necesidad, antes de puntuar, y cada propuesta recibe un puntaje de 1 a 3 en cada una; en la dimensión legal, un puntaje 1 significa que incumple una norma. El aporte es peso × puntaje y el total es la suma. Por ejemplo, con pesos ético 3, legal 3, económica 2, ambiental 3 y social 2, el máximo posible es (3 + 3 + 2 + 3 + 2) × 3 = 39.",
        "El puntaje total ayuda, pero no decide solo. Si dos propuestas quedan casi empatadas, se revisan los dilemas abiertos y los datos que faltan. Además, la recomendación se escribe con condiciones, es decir, cosas que deben cumplirse para aplicarla, como pedir consentimiento antes de publicar una foto. Y con un plan de seguimiento: qué se medirá, cuándo y con qué meta.",
        "Una decisión honesta se apoya en evidencia reunida antes de elegir. Quien decide primero y busca después solo los datos que le dan la razón comete un sesgo. La decisión se comunica con los datos buenos y los malos, para que otras personas puedan revisarla y discutirla.",
    ],
    vocab=[("matriz integrada", "tabla con las cinco dimensiones, pesos y puntajes"), ("recomendación", "decisión final con sus razones"), ("condición", "requisito que debe cumplirse para aplicar la propuesta"), ("seguimiento", "plan de medir resultados después de aplicar"), ("sesgo", "decidir primero y buscar solo datos que dan la razón"), ("puntaje máximo", "total cuando todas las dimensiones reciben 3")],
    worked=[
        ("Total de una propuesta", "Pesos: ético 3, legal 3, económica 2, ambiental 3, social 2. Una propuesta recibe 3, 3, 1, 2 y 3. ¿Cuánto suma?", ["Aportes: 9, 9, 2, 6 y 6.", "Sumo 9 + 9 + 2 + 6 + 6 = 32."], "32 puntos"),
        ("Condición y seguimiento", "Se recomienda una cartelera con fotos de estudiantes. ¿Qué condición y qué seguimiento corresponden?", ["Condición: tener el consentimiento de cada persona.", "Seguimiento: contar cada mes cuántos estudiantes la usan."], "Consentimiento previo; conteo mensual de uso"),
    ],
    mistakes=[
        ("Elegir la propuesta con más puntos aunque incumpla una norma.", "Lo ilegal se descarta o se corrige antes de puntuar.", "Primero revisa las normas; luego puntúa."),
        ("Dar solo el número final como justificación.", "Los demás no pueden saber por qué se decidió.", "Muestra los pesos, los puntajes y las razones."),
    ],
    R=[
        ("Una propuesta incumple una norma de seguridad. ¿Qué se hace primero? A) se descarta o se corrige antes de puntuar B) se puntúa igual y después se verá", "A", "Las normas funcionan como restricción previa."),
        arith("Pesos: ético 3, legal 3, económica 2, ambiental 3 y social 2. ¿Cuántos puntos suma el puntaje máximo posible (3 en cada dimensión)?", "(3+3+2+3+2)*3", "Se suman los pesos y se multiplican por 3.", " puntos"),
        ("¿Qué debe incluir una recomendación? A) condiciones y plan de seguimiento B) solo el puntaje total", "A", "Sin condiciones y seguimiento, la decisión no se puede revisar."),
    ],
    C=[
        ("¿Por qué se justifica la decisión con evidencia? A) para que otras personas puedan revisarla y discutirla B) para que el informe se vea más largo", "A", "La evidencia hace la decisión revisable."),
        ("Dos propuestas empatan en puntaje total. ¿Qué se hace? A) revisar las dimensiones de mayor peso y los dilemas abiertos B) elegir con una moneda", "A", "Un empate se decide con razones, no con azar."),
        ("«Aplicar la propuesta si se pide consentimiento antes de publicar fotos» es… A) una condición de la recomendación B) un puntaje de la matriz", "A", "Es un requisito para aplicarla."),
    ],
    A=[
        arith("Pesos: ético 3, legal 3, económica 2, ambiental 3, social 2. La propuesta A recibe 2, 3, 1, 3 y 2. ¿Cuánto suma?", "3*2+3*3+2*1+3*3+2*2", "Se multiplica cada peso por su puntaje y se suman los aportes.", " puntos"),
        arith("Con los mismos pesos, la propuesta B recibe 3, 3, 3, 1 y 2. ¿Cuánto suma?", "3*3+3*3+2*3+3*1+2*2", "Se multiplica cada peso por su puntaje y se suman los aportes.", " puntos"),
        arith("Con los mismos pesos, la propuesta C recibe 3, 1, 3, 3 y 3, pero el puntaje 1 en lo legal significa que incumple una norma. ¿Cuánto suma?", "3*3+3*1+2*3+3*3+2*3", "Se suman los aportes, aunque este total no basta para elegirla.", " puntos"),
    ],
    Z=[
        ("Las propuestas A y B suman 30 y 31 puntos. ¿Qué conviene hacer con esa diferencia de 1 punto?", "Revisar datos y dilemas abiertos y decidir con condiciones, no solo con el número", "Una diferencia tan pequeña no sustenta una decisión segura."),
        ("Un equipo decide primero su propuesta favorita y luego busca solo datos que la apoyan. ¿Qué falla tiene?", "Un sesgo: la evidencia debe reunirse antes de decidir y en todas las dimensiones", "Buscar solo lo que da la razón impide una evaluación justa."),
    ],
    D=[
        ex("Entre A (30 puntos), B (31 puntos) y C (33 puntos, pero incumple una norma), ¿cuál se puede recomendar según puntaje y restricciones?", "La B", "C se descarta por incumplir una norma, y B supera a A por 1 punto."),
        arith("Se aplica la propuesta B y el equipo mide que las hojas bajaron de 160 a 128 por semana. ¿Qué porcentaje de reducción logró?", "(160-128)*100//160", "Se calcula la diferencia sobre el valor inicial.", " %"),
    ],
    ctx=arith("Se consulta a 30 personas y 24 aceptan la propuesta con la condición de pedir consentimiento. ¿Qué porcentaje la acepta con esa condición?", "24*100//30", "Se divide los que aceptan entre el total y se pasa a porcentaje.", " %"),
    sc=[
        ("¿Qué se revisa antes de puntuar una propuesta?", "Que no incumpla normas", "Lo ilegal se descarta o se corrige."),
        ("En Tecnología: ¿qué es un sesgo al decidir?", "Decidir primero y buscar solo datos que dan la razón", "Impide evaluar con justicia."),
        ("¿Qué debe llevar una recomendación además del puntaje?", "Condiciones y seguimiento", "Permiten aplicar y revisar la decisión."),
    ],
    open_task=(
        "Usa estos datos de ejemplo. Pesos: ético 3, legal 3, económica 2, ambiental 3, social 2. Propuesta 1 (punto de acopio de papel en el patio): puntajes 3, 3, 2, 3, 2. Propuesta 2 (cartelera digital con fotos de estudiantes sin consentimiento): puntajes 2, 1, 3, 3, 1. Propuesta 3 (campaña de uso del reverso de hojas): puntajes 3, 3, 3, 2, 3. Descarta lo que corresponda, calcula los totales, recomienda una propuesta con dos condiciones y un plan de seguimiento con una meta.",
        "Se descarta la 2 por puntaje 1 en lo legal; la 1 suma 9 + 9 + 4 + 9 + 4 = 35 y la 3 suma 9 + 9 + 6 + 6 + 6 = 36; se recomienda la 3, con condiciones de recopilar el reverso limpio y avisar a todos los cursos; seguimiento: medir hojas por semana con meta de bajar 20 %",
        ["descarta la que incumple", "calcula bien los totales", "recomienda con dos condiciones", "propone un seguimiento con meta"],
        ["hoja con totales y recomendación"],
        ["puntuar la propuesta ilegal", "recomendar sin seguimiento"],
        "Pregunta: «¿cómo sabrás en un mes si la decisión funcionó?». Debe poder nombrar un indicador y una meta.",
    ),
    reinforce="Explica a una persona de tu casa, con tus palabras, por qué una decisión de tecnología se evalúa en cinco dimensiones.",
    extend="Explica por qué es más honesto fijar los pesos antes de ver los puntajes.",
)
