"""Teatro 3.º y 4.º medio FG: OAC-06 (gestión y difusión de proyectos teatrales), clases 4 y 5. Presupuestos y resultados de ejemplo, inventados; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O6 = "FG-TEAT-3y4-OAC-06"

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (contexto y presupuesto de ejemplo, inventados). Función en el gimnasio del colegio, con entrada gratuita, aforo de 80 personas, el viernes a las 12:00 (recreo largo). "
     "Gastos previstos: 40 afiches en blanco y negro a $100 cada uno; 80 programas de mano a $50 cada uno; cinta adhesiva por $1.000. Aporte del curso: $12.000. El gimnasio tiene una rampa de acceso y una puerta lateral.")
build(
    O6, 4, F,
    use="Aprenderé a adaptar la difusión al contexto (lugar, horario, accesibilidad, público) y a gestionar un presupuesto sencillo con ingresos, gastos y saldo, de manera transparente.",
    prior=["Sé qué datos lleva un mensaje de difusión.", "Sé hacer un cronograma con dependencias.", "Sé sumar, restar y multiplicar con números enteros."],
    explain=[
        "El contexto de una función determina cómo conviene difundirla. El horario define quiénes pueden asistir y cuándo avisar: una función en el recreo largo llega a quienes están en el colegio, pero no a las familias que trabajan. El lugar influye en la accesibilidad: una rampa y una puerta lateral permiten entrar a personas con movilidad reducida, y esa información puede incluirse en el afiche. El lenguaje debe ser claro y cercano al público, sin tecnicismos que no entienda.",
        "Un presupuesto es una estimación de los gastos y de los recursos con que se cuenta para un proyecto. Se anotan los gastos previstos (cantidad por precio) y los recursos disponibles; la diferencia entre ambos es el saldo. Un presupuesto transparente se comparte con quienes aportaron, se ajusta si cambian las condiciones y se rinde cuentas al terminar: se informa cuánto se gastó y cuánto sobró. Si se pensara en cobrar entrada, se pide autorización a la dirección y se explica para qué se usará el dinero.",
        "También se cuida la información al cambiar un dato. Si la función cambia de día u hora, se actualizan todos los medios, se retiran los afiches con el dato antiguo y se avisa el cambio por los mismos canales. Los precios de esta clase son de ejemplo y el dinero se maneja siempre con autorización y registro.",
    ],
    vocab=[("presupuesto", "estimación de gastos y recursos de un proyecto"), ("gasto", "dinero que se paga por algo necesario para el proyecto"), ("saldo", "diferencia entre los recursos y los gastos"), ("rendición de cuentas", "informe de cuánto se gastó y cuánto sobró"), ("accesibilidad física", "condiciones del lugar para que todas las personas puedan entrar y moverse")],
    worked=[
        ("Calcular un gasto", "Se imprimen 30 afiches a $120 cada uno. ¿Cuánto cuestan?", ["Se multiplica la cantidad por el precio.", "30 × 120 = 3.600."], "$3.600"),
        ("Calcular un saldo", "El curso aporta $10.000 y los gastos son $7.200. ¿Cuánto sobra?", ["Se resta el gasto al aporte.", "10.000 − 7.200 = 2.800."], "$2.800"),
    ],
    mistakes=[("Gastar el aporte sin anotar los gastos.", "No se puede rendir cuentas ni saber cuánto sobra.", "Anota cada gasto con su monto y fecha."),
              ("Dejar los afiches con la fecha antigua cuando la función cambió.", "Confunde al público.", "Retira los afiches viejos y actualiza todos los medios.")],
    T=[
        ('abc', '¿Qué es un presupuesto?', 'Una estimación de los gastos y de los recursos para un proyecto', 'El dinero que una persona gasta por su cuenta en la función', 'La lista de personas que asistirán a la función', 'Un presupuesto ordena lo que se espera gastar y con qué recursos se cuenta.'),
        ('=', '{F} ¿Cuánto cuestan los 40 afiches?', '40*100', 'Se multiplica la cantidad de afiches por el precio de cada uno.', ' pesos'),
        ('abc', '{F} ¿Qué característica del gimnasio favorece la accesibilidad física?', 'La rampa de acceso', 'La puerta lateral cerrada con llave', 'El horario de recreo largo', 'La rampa permite entrar a personas con movilidad reducida.'),
        ('abc', '¿Por qué el horario influye en la difusión?', 'Porque define quiénes pueden asistir y cuándo conviene avisar', 'Porque el horario cambia la duración de la obra', 'Porque la hora no importa mientras haya afiches', 'El horario determina qué parte del público puede asistir.'),
        ('abc', '{F} La entrada es gratuita y el aforo es de 80 personas. ¿Qué conviene informar al público?', 'Que los cupos son limitados y que llegar con tiempo ayuda a conseguir lugar', 'Que no hay límite de cupos, así que pueden llegar a cualquier hora sin preocuparse', 'Que se cobrará una cuota a la entrada del gimnasio', 'Informar el aforo ayuda a que el público se organice sin engaño.'),
        ('abc', 'Si el grupo piensa en cobrar una entrada, ¿qué corresponde?', 'Pedir autorización a la dirección y explicar para qué se usará el dinero', 'Cobrar a quienes parezcan tener más dinero y no explicar nada a nadie sobre el uso de lo recaudado', 'Cobrar sin avisar para ver cuánto reúnen y después decidir entre quienes organizaron en qué lo gastan', 'Cobrar requiere autorización y transparencia sobre el uso del dinero.'),
        ('=', '{F} ¿Cuánto suman los gastos previstos (afiches, programas y cinta)?', '40*100+80*50+1000', 'Se suman los gastos de afiches, programas y cinta adhesiva.', ' pesos'),
        ('=', '{F} ¿Cuánto dinero sobra del aporte del curso si se gastan los $9.000 previstos?', '12000-9000', 'Se resta el gasto total al aporte del curso.', ' pesos'),
        ('abc', '¿Cuál ajuste reduce gastos sin perjudicar la difusión?', 'Imprimir los programas por ambos lados para usar menos hojas', 'Eliminar todos los afiches y no avisar de otra forma', 'Imprimir programas en una calidad que no se pueda leer', 'Se reduce el gasto de papel manteniendo la información legible.'),
        ('abc', '{F} Una compañera propone imprimir 120 programas aunque el aforo es 80. ¿Qué observación corresponde?', 'Habría 40 programas de más, un gasto innecesario salvo que se justifique', 'Está bien, porque nunca es mala idea que sobren programas y así nadie se queda sin uno', 'No importa, porque el costo es el mismo que para 80', 'Más programas que aforo aumenta el gasto sin beneficio claro.'),
        ('abc', 'El público no entiende el afiche porque usa palabras muy técnicas. ¿Qué ajuste de contexto corresponde?', 'Usar lenguaje claro y cercano al público', 'Agregar más palabras técnicas para explicar mejor', 'Eliminar la fecha y el lugar del afiche', 'El mensaje debe ser comprensible para quienes lo reciben.'),
        ('=', '{F} Si cada afiche sube de $100 a $150, ¿cuántos pesos más cuestan los 40 afiches?', '(150-100)*40', 'Se calcula la diferencia por afiche y se multiplica por la cantidad.', ' pesos'),
        ('abc', 'La función se cambia del viernes 12:00 al lunes 8:00. ¿Qué debe hacer el grupo?', 'Actualizar todos los medios, retirar los afiches con la fecha antigua y avisar el cambio', 'Avisar solo en la radio, porque es el medio que más se escucha y ya llega a todo el colegio', 'Dejar los afiches antiguos para que el público no se confunda', 'Un dato desactualizado en cualquier medio confunde al público.'),
    ],
    ctx=('ab', 'Terminada la función sobraron $3.000 del aporte del curso. ¿Qué conviene hacer?', 'Informar a quienes aportaron y decidir entre todos cómo usarlo', 'Quedárselo quienes organizaron como pago por su trabajo', 'La rendición de cuentas es transparente y decide el curso en conjunto.'),
    sc=[
        ("En Teatro: ¿qué es el saldo de un presupuesto?", "La diferencia entre los recursos y los gastos", "Indica cuánto sobra o cuánto falta."),
        ("¿Qué se hace al terminar el proyecto con el dinero?", "Se informa cuánto se gastó y cuánto sobró", "Eso es rendir cuentas con transparencia."),
        ("Si cambia la fecha de la función, ¿qué se hace con los medios?", "Se actualizan todos y se retiran los afiches antiguos", "Así el público no recibe información contradictoria."),
    ],
    op=("Inventa un presupuesto para una función de tu colegio: lista tres gastos con cantidad, precio y total, un aporte inicial, el saldo y una decisión para adaptar la difusión al horario y al lugar (por ejemplo accesibilidad o lenguaje). Usa precios de ejemplo.",
        "Gastos: 30 afiches a $100 = $3.000; 60 programas a $50 = $3.000; cinta $800. Total $6.800. Aporte $9.000. Saldo $2.200. Adaptación: incluir en el afiche que hay rampa de acceso y usar lenguaje claro.",
        ["tres gastos con total", "calcula el saldo", "adapta al contexto", "usa precios de ejemplo y registra el dinero"],
        ["presupuesto de ejemplo"],
        ["no calcular el saldo", "ignorar el contexto del lugar"],
        "Pregunta: «¿cuánto gastaste y cuánto sobró?». Debe responder con números."),
    reinforce="Anota los gastos de una actividad de ejemplo en tu casa o curso con cantidad, precio y total.",
    extend="Explica por qué rendir cuentas con transparencia ayuda a que un proyecto futuro cuente con más apoyo.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (resultados de ejemplo, inventados). Aforo: 80 personas. Objetivo de asistencia: 60 personas. Asistieron: 56. "
     "Encuesta anónima y voluntaria a 40 asistentes sobre cómo se enteraron de la función: diario mural, 12; radio escolar, 10; lista de mensajes del curso, 14; afiche digital, 4.")
build(
    O6, 5, F,
    use="Aprenderé a evaluar un proyecto de difusión con indicadores (asistencia, medios que funcionaron, satisfacción), a leer sus límites y a proponer mejoras con datos, cuidando la privacidad de quienes responden.",
    prior=["Sé calcular porcentajes.", "Sé que una encuesta debe ser anónima y voluntaria.", "Sé armar un objetivo con una cifra."],
    explain=[
        "Evaluar un proyecto de difusión es comparar lo que se logró con lo que se quería. Un indicador es un dato que permite comprobar un resultado. Algunos son la asistencia (cuántas personas llegaron frente al objetivo y al aforo), los medios que funcionaron (cómo se enteró la gente) y la satisfacción del público (qué le pareció). Se calcula, por ejemplo, el porcentaje del aforo que asistió y cuántas personas mencionaron cada medio.",
        "Una encuesta breve, anónima y voluntaria sirve para recoger información. No se piden nombres ni datos personales, y nadie es presionado a responder. Hay que reconocer sus límites: si respondieron 40 de 56 asistentes y no todos quisieron responder, los resultados no necesariamente representan a todos. Un dato aislado no basta: que pocas personas mencionen un medio no prueba que sea inútil, porque quizá se difundió poco.",
        "Con los datos se decide qué mantener, qué cambiar y qué probar la próxima vez. Se conservan los medios que funcionaron, se revisa qué pasó con los que alcanzaron poco y se escribe un breve informe. Al cerrar el proyecto se agradece a quienes colaboraron, se guardan los resultados agrupados y se eliminan los datos que pudieran identificar a alguien.",
    ],
    vocab=[("indicador", "dato que permite comprobar un resultado"), ("asistencia", "cantidad de personas que llegaron a la función"), ("encuesta anónima", "cuestionario en que no se pide el nombre de quien responde"), ("muestra", "grupo de personas que respondió, que puede no representar a todos"), ("informe", "documento breve con los resultados y las mejoras propuestas")],
    worked=[
        ("Calcular un porcentaje de asistencia", "Asistieron 45 personas a un lugar con aforo de 60. ¿Qué porcentaje del aforo asistió?", ["Se calcula 45 × 100 ÷ 60.", "El resultado es 75."], "75 %"),
        ("Leer una limitación", "Solo 20 de 50 asistentes respondieron la encuesta. ¿Qué advertencia se hace?", ["Respondió menos de la mitad, y quienes respondieron pueden no representar a todos.", "Las conclusiones deben presentarse con cautela."], "Los resultados pueden no representar a todos"),
    ],
    mistakes=[("Concluir que un medio «no sirve» porque pocas personas lo mencionaron.", "Quizá se usó poco o llegó a quienes no asistieron.", "Revisa cómo y cuánto se difundió antes de concluir."),
              ("Pedir el nombre en la encuesta para «saber quién respondió».", "Expone a las personas y puede hacer que no sean sinceras.", "Hazla anónima y voluntaria.")],
    T=[
        ('abc', '¿Qué es un indicador de difusión?', 'Un dato que permite comprobar un resultado, como la asistencia', 'La opinión de quien organiza sobre cómo salió todo', 'El nombre del medio más conocido del colegio', 'Un indicador convierte el logro del proyecto en un dato comprobable.'),
        ('=', '{F} ¿Qué porcentaje del aforo de 80 asistió?', '56*100//80', 'Se divide la asistencia entre el aforo y se pasa a porcentaje.', ' %'),
        ('abc', '{F} ¿Qué medio fue más mencionado por quienes respondieron?', 'La lista de mensajes del curso, con 14 menciones', 'La radio escolar, con 10 menciones', 'El afiche digital, con 4 menciones', 'La lista del curso tiene el número mayor de menciones.'),
        ('abc', '{F} El objetivo era que asistieran 60 personas. ¿Se cumplió?', 'No, asistieron 56, cuatro personas menos que el objetivo', 'Sí, porque asistió más del 50 % del aforo y con eso se considera lograda cualquier meta', 'Sí, porque el aforo es de 80', 'La asistencia fue menor que la meta planteada.'),
        ('abc', '¿Por qué la encuesta debe ser anónima y voluntaria?', 'Para proteger a quienes responden y no presionarlas', 'Para que se responda más rápido y con menos reflexión', 'Para poder identificar quién dio cada opinión', 'Sin nombres ni presión, las respuestas son más sinceras y seguras.'),
        ('abc', '{F} ¿Qué limitación tiene esta encuesta?', 'Respondieron 40 de 56 asistentes, y puede no representar a todos', 'Tiene demasiadas preguntas para resolver en poco tiempo', 'Solo preguntó por la radio escolar y por el diario mural, y dejó de lado los demás medios', 'No todas las personas respondieron, por eso los resultados deben tomarse con cautela.'),
        ('=', '{F} ¿Qué porcentaje de quienes respondieron se enteró por la lista de mensajes del curso?', '14*100//40', 'Se divide quienes mencionaron la lista entre quienes respondieron.', ' %'),
        ('abc', '{F} El afiche digital fue mencionado solo 4 veces. ¿Qué mejora es adecuada?', 'Revisar cómo y a quiénes se difundió el afiche digital y probar cambios', 'Eliminarlo para siempre, porque con tan pocas menciones queda claro que no sirve', 'Mantenerlo igual y esperar que mejoren los resultados', 'Pocas menciones piden revisar la difusión, no descartar el medio sin evidencia.'),
        ('abc', 'Para registrar los resultados de una encuesta protegiendo a las personas, ¿qué se hace?', 'Guardar los resultados agrupados y eliminar cualquier dato que identifique a alguien', 'Publicar las respuestas con el nombre de cada persona, para reconocer a quienes colaboraron', 'Conservar las hojas originales con nombres en un lugar común', 'Los datos agrupados bastan para decidir y protegen la privacidad.'),
        ('abc', '{F} Alguien concluye que «el afiche digital no sirve». ¿Qué falta para afirmarlo?', 'Saber a cuántas personas llegó y cuánto se difundió, no solo cuántas lo mencionaron', 'Ninguna información adicional, porque con los números de la encuesta ya está probado', 'La opinión del grupo más numeroso del curso', 'Pocas menciones pueden deberse a poca difusión y no a un mal medio.'),
        ('abc', 'El grupo cuenta cuántas personas asistieron y, aparte, pregunta cómo se enteraron. ¿Qué mide cada dato?', 'La asistencia mide el resultado y la pregunta mide qué medio funcionó', 'Ambos miden exactamente lo mismo', 'La asistencia mide la satisfacción y la pregunta la asistencia', 'Son indicadores distintos que se complementan.'),
        ('=', 'Para la próxima función se espera un aumento de 25 % sobre los 56 asistentes. ¿Cuántos asistentes se esperan?', '56+56*25//100', 'Se calcula el 25 % de 56 y se suma al número original.', ' asistentes'),
        ('abc', 'El grupo debe decidir los medios de la próxima función con los datos de la ficha. ¿Qué decisión se apoya mejor?', 'Reforzar la lista del curso y la radio, revisar el afiche digital y mantener el diario mural', 'Dejar solo la lista del curso, que fue el más mencionado, y eliminar todos los otros medios', 'Repetir exactamente la misma difusión sin cambios', 'Se refuerza lo que funcionó, se revisa lo que alcanzó poco y se mantiene un respaldo.'),
    ],
    ctx=('ab', 'Terminada la encuesta, un integrante propone publicar las respuestas con los nombres. ¿Qué conviene responder?', 'No publicar nombres y compartir solo los resultados agrupados', 'Publicarlos para reconocer a cada colaborador', 'Los nombres exponen a las personas y no hacen falta para la mejora.'),
    sc=[
        ("En Teatro: ¿qué es un indicador?", "Un dato que permite comprobar un resultado", "Sirve para comparar lo logrado con lo esperado."),
        ("¿Cómo debe ser una encuesta sobre la difusión?", "Breve, anónima y voluntaria", "Protege la privacidad de quienes responden y evita presionarlas."),
        ("¿Qué se hace al cerrar el proyecto con los datos?", "Se guardan agrupados y se eliminan los que identifiquen a alguien", "Así se cuida la privacidad de las personas."),
    ],
    op=("Imagina que difundiste una función con tres medios y asistieron 45 de un aforo de 60. Inventa una encuesta anónima a 30 personas (cuántas se enteraron por cada medio). Calcula el porcentaje de asistencia, identifica el medio con más menciones, escribe una limitación de la encuesta y propone una mejora para la próxima vez.",
        "Asistió el 75 % del aforo. Medios (30 respuestas): lista del curso 12, radio 10, afiche 8. Más menciones: lista del curso. Limitación: no todos respondieron. Mejora: ampliar la difusión del afiche en el pasillo y mantener los demás medios.",
        ["calcula el porcentaje de asistencia", "identifica el medio más mencionado", "reconoce una limitación", "propone una mejora con base en los datos"],
        ["hoja con datos, cálculos y mejora"],
        ["concluir sin considerar los límites", "pedir nombres en la encuesta"],
        "Pregunta: «¿qué dato apoya tu mejora?». Debe citarlo."),
    reinforce="Con un grupo de 10 personas de tu curso inventado, anota cómo se enteraron de una actividad (sin nombres) y calcula el porcentaje de cada medio.",
    extend="Explica por qué un indicador aislado no basta para evaluar un proyecto de difusión y qué otros datos agregarías.",
)
