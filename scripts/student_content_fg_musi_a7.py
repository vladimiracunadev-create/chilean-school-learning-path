"""Música 3.º y 4.º medio FG: OAC-07 (gestión y difusión de obras e interpretaciones musicales propias con medios o TIC). Proyectos, presupuestos y métricas de ejemplo, inventados."""
from __future__ import annotations

from fg_musi_common import build

O7 = "FG-MUSI-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (tres proyectos de difusión de ejemplo, de un grupo escolar que creó una canción propia). Proyecto 1: un concierto en el patio para unas 60 personas del colegio y sus familias. "
     "Proyecto 2: una grabación de audio de la canción para subirla a un sitio donde la puede escuchar cualquier persona. Proyecto 3: un espacio de 5 minutos en la radio del colegio, que se oye solo dentro del establecimiento durante el recreo. "
     "Propósito del grupo: que el curso conozca su canción y opine sobre ella.")
build(
    O7, 1, F,
    use="Aprenderé a definir el propósito y la audiencia de un proyecto de difusión musical y a elegir el medio más adecuado (concierto, grabación, radio escolar, plataformas digitales) según ambos.",
    prior=["Creo y registro obras propias.", "Evalúo resultados y procesos.", "Sé qué es una audiencia."],
    explain=[
        "Difundir una obra es hacer que otras personas la conozcan. Antes de elegir cómo, se definen dos cosas: el propósito (para qué se quiere difundir: mostrar, recibir opiniones, recaudar fondos, acompañar un evento) y la audiencia (a quién se dirige: el curso, el colegio, la familia, la comunidad). Esas dos decisiones orientan el medio.",
        "Hay varios medios. El concierto en vivo permite contacto directo y respuesta inmediata, pero llega a pocas personas y depende de un lugar y una fecha. La grabación de audio se puede escuchar muchas veces y en distintos lugares. La radio del colegio alcanza a toda la comunidad escolar durante un horario. Las plataformas digitales llegan a mucha gente, pero exigen cuidar derechos de autor, imagen y seguridad. Cada medio tiene ventajas y límites.",
        "Un buen proyecto elige el medio que mejor sirve al propósito y a la audiencia, y no el que parece más moderno. Si lo que se busca es recibir opiniones del curso, quizá convenga un medio donde el curso pueda responder.",
    ],
    vocab=[("difusión", "acción de dar a conocer una obra a otras personas"), ("audiencia", "personas a las que se dirige la difusión"), ("propósito de difusión", "para qué se quiere dar a conocer la obra"), ("medio", "canal usado para difundir: concierto, radio, grabación, plataforma"), ("alcance", "cantidad de personas a las que llega una difusión")],
    worked=[
        ("Elegir según la audiencia", "El grupo quiere que su curso, de unas 35 personas, escuche la canción en el recreo. ¿Qué medio de la ficha sirve y por qué?", ["La audiencia es el curso, dentro del colegio.", "La radio del colegio se oye en el recreo.", "Alcanza al curso sin depender de internet."], "La radio escolar, porque llega al curso durante el recreo"),
        ("Comparar alcance", "Un concierto llega a 60 personas y la radio escolar a 300. ¿Cuántas personas más alcanza la radio?", ["Se resta el alcance menor del mayor.", "300 − 60 = 240 personas."], "240 personas más"),
    ],
    mistakes=[("Elegir el medio antes de definir propósito y audiencia.", "Puede llegar a quienes no corresponde o no cumplir el fin.", "Define primero para qué y para quién."),
              ("Pensar que más alcance siempre es mejor.", "Un medio masivo puede no servir si el propósito es recibir opiniones cercanas.", "Compara alcance con propósito.")],
    T=[
        ('abc', '{F} ¿Qué proyecto permite contacto directo y respuesta inmediata del público?', 'El concierto en el patio, porque el público responde de inmediato', 'La grabación para subir a un sitio', 'La radio escolar', 'Presencial: se ve y se oye la reacción de inmediato.'),
        ('abc', '{F} ¿Qué medio puede escucharse varias veces y en distintos lugares?', 'La grabación de audio, que queda disponible para repetirla', 'El concierto en vivo, que se oye en un solo momento', 'La radio escolar, que se oye solo en el recreo', 'Una grabación queda disponible y se puede repetir.'),
        ('abc', '{F} ¿Dónde se oye el proyecto 3?', 'Solo dentro del colegio, durante el recreo', 'En cualquier lugar del mundo', 'En las casas de las familias', 'La ficha lo restringe al establecimiento.'),
        ('=', '{F} El concierto llega a 60 personas y la grabación se compartió con 150. ¿Cuántas personas más alcanza la grabación?', '150-60', 'Se resta el alcance del concierto del alcance de la grabación.', ' personas'),
        ('abc', '{F} ¿Qué propósito del grupo orienta el medio?', 'Que el curso conozca la canción y opine', 'Ganar una competencia nacional', 'Aparecer en televisión', 'Es el propósito declarado en la ficha.'),
        ('abc', '{F} Si el curso debe poder opinar enseguida, ¿qué medio conviene más?', 'El concierto en el patio, por la respuesta inmediata', 'La grabación sin forma de comentar', 'La radio escolar, porque se oye en el recreo', 'Es el que permite ver y oír la reacción de inmediato.'),
        ('abc', 'Un grupo elige una plataforma digital «porque llega a más gente», aunque su propósito es mostrar la canción a la familia. ¿Qué falló?', 'Eligió el medio sin considerar el propósito y la audiencia', 'Eligió un medio muy pequeño', 'Olvidó los derechos', 'Más alcance no siempre sirve al fin.'),
        ('abc', '¿Qué es la audiencia de un proyecto de difusión?', 'Las personas a quienes se dirige', 'Los instrumentos que se usan', 'La duración del proyecto', 'Define quiénes son las personas que escucharán la obra.'),
        ('abc', '{F} ¿Qué límite tiene el concierto en el patio?', 'Llega a pocas personas y depende de un lugar y una fecha', 'Se puede escuchar siempre', 'No permite respuesta del público', 'Es el costo de la cercanía.'),
        ('abc', 'Una plataforma digital exige especialmente', 'cuidar derechos de autor, imagen y seguridad', 'tener un escenario grande', 'tocar sin ensayar', 'Al ser pública, aparecen riesgos que deben cuidarse.'),
        ('=', '{F} Si el grupo repitiera el concierto del proyecto 1 en 2 funciones, cada una con 60 personas, ¿a cuántas personas llegaría en total?', '60*2', 'Se multiplican las personas de cada función por el número de funciones.', ' personas'),
        ('abc', 'Para comparar medios, ¿qué criterios conviene usar?', 'Propósito, audiencia, alcance y cuidados necesarios', 'Solo el costo', 'Solo cuál es más novedoso', 'Cada criterio aporta información útil para comparar los medios.'),
        ('abc', '{F} La radio escolar dura 5 minutos y la canción 3 minutos y medio. ¿Qué conviene hacer con el tiempo restante?', 'Presentar el grupo y explicar de qué trata la canción', 'Dejar silencio', 'Repetir la canción diez veces', 'El tiempo extra puede servir para contextualizar la obra.'),
    ],
    ctx=('abc', 'Un grupo quiere que las familias vean su canción en vivo y comenten. Tienen una grabación lista. ¿Qué es lo más coherente con su propósito?', 'Organizar un concierto y usar la grabación como apoyo', 'Subir solo la grabación y no hacer concierto', 'No difundir nada', 'El concierto permite contacto y comentarios directos.'),
    sc=[
        ('¿Qué dos cosas se definen antes de elegir un medio?', 'El propósito y la audiencia', 'Ambas decisiones orientan la elección del medio adecuado.'),
        ('¿Cuántas personas más llegan 120 que 45?', '75', 'Al restar 45 de 120 resulta 75.'),
        ('abc', 'Un medio se elige', 'según el propósito y la audiencia', 'por ser el más novedoso', 'por ser el más barato siempre', 'Debe servir al fin del proyecto.'),
    ],
    op=("Con la {F} como modelo, define para una obra tuya (real o de ejemplo) el propósito de difusión, la audiencia, dos medios posibles con una ventaja y un límite cada uno, y el medio que elegirías con una razón.",
        "Obra: una canción sobre el colegio. Propósito: que el curso la conozca. Audiencia: el curso. Medios: radio escolar (ventaja: llega en el recreo; límite: solo dentro del colegio) y grabación compartida (ventaja: se escucha varias veces; límite: no hay respuesta inmediata). Elijo la radio, porque el curso está en el colegio.",
        ["propósito y audiencia", "dos medios con ventaja y límite", "elección justificada"], ["plan breve"], ["elegir sin propósito", "no mencionar límites"],
        "Reconoce el plan y pide relacionar el medio con el propósito."),
    reinforce="Anota tres lugares de tu comunidad donde se podría difundir una canción escolar.",
    extend="Compara dos medios de difusión que conozcas y anota qué propósito sirve mejor cada uno.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (lista de verificación de ejemplo para publicar una grabación del grupo). Pasos: grabar a volumen moderado en un lugar silencioso; editar para ordenar y limpiar el audio; escribir los créditos con el nombre de cada integrante; "
     "pedir permiso por escrito a una persona adulta responsable para publicar a integrantes menores de edad; revisar que la canción sea de autoría propia y que no incluya fragmentos de obras de otras personas sin permiso; "
     "no publicar datos personales (dirección, teléfono); decidir quién puede comentar y qué se hace con comentarios molestos. Si alguien recibe mensajes incómodos, avisa a una persona adulta de confianza.")
build(
    O7, 2, F,
    use="Aprenderé a usar medios y TIC para difundir una obra propia (grabar, editar, publicar) con cuidado de los derechos de autor, el permiso de las personas que aparecen, los créditos y la seguridad en línea.",
    prior=["Elijo un medio según propósito y audiencia.", "Sé que hay obras con derechos de autor.", "Cuido el volumen al grabar."],
    explain=[
        "Publicar una obra con TIC implica varias decisiones. Se graba en un lugar silencioso y a volumen moderado; se edita para ordenar partes y limpiar el audio; se escriben los créditos, es decir, el nombre de cada persona que participó y su rol; y se elige dónde publicar. Antes de hacerlo se revisan los derechos de autor: una obra es de quien la creó, y usar fragmentos de obras de otras personas normalmente requiere su permiso. Si la canción es propia y no incluye fragmentos ajenos, se puede difundir; si dudas, consulta a tu docente.",
        "También hay que cuidar a las personas. Quien aparece en una grabación o imagen debe dar su consentimiento; en el caso de menores de edad, se pide permiso a una persona adulta responsable. No se publican datos personales como dirección o teléfono. Conviene decidir quién modera los comentarios y qué hacer si aparecen mensajes ofensivos: no responder con enojo, guardar evidencia y avisar a una persona adulta de confianza.",
        "Los medios digitales amplían el alcance, pero también los riesgos. Planificar estos cuidados antes de publicar evita problemas.",
    ],
    vocab=[("créditos", "lista de personas que participaron y su rol"), ("derechos de autor", "derechos de quien creó una obra sobre su uso y difusión"), ("consentimiento", "permiso dado de forma libre y clara por una persona"), ("dato personal", "información que identifica o ubica a una persona"), ("moderar", "revisar y decidir qué comentarios se permiten")],
    worked=[
        ("Revisar un permiso", "En un grupo de 5 personas, 2 son menores de edad. ¿Para cuántas personas hay que pedir permiso a una persona adulta responsable?", ["El permiso se pide por cada menor que aparece.", "Hay 2 menores en el grupo."], "Para 2 personas, una autorización por cada menor"),
        ("Detectar un riesgo", "El grupo quiere publicar con su dirección en la descripción «para que nos visiten». ¿Qué hacer?", ["La dirección es un dato personal.", "No se publica.", "Se puede indicar solo el nombre del grupo."], "No publicarla"),
    ],
    mistakes=[("Usar un fragmento de una canción conocida sin pedir permiso.", "La obra es de otra persona y su uso requiere autorización.", "Crea material propio o pide el permiso."),
              ("Publicar nombres completos, direcciones o teléfonos.", "Pone en riesgo la privacidad y la seguridad.", "Usa solo nombres artísticos o primeros nombres con permiso.")],
    T=[
        ('abc', '{F} ¿Cuál es el primer cuidado para grabar?', 'Hacerlo en un lugar silencioso y a volumen moderado', 'Hacerlo en el patio con mucho ruido', 'Subir el volumen al máximo', 'Un lugar silencioso mejora el audio y el volumen moderado cuida el oído.'),
        ('abc', '{F} ¿Qué son los créditos?', 'La lista de personas que participaron y su rol', 'Un pago por la canción', 'El título de la canción', 'Permiten reconocer el aporte de cada integrante.'),
        ('abc', '{F} ¿Qué se necesita para publicar a integrantes menores de edad?', 'Permiso por escrito de una persona adulta responsable', 'Solo el permiso del docente', 'Ningún permiso', 'La ficha lo exige para menores.'),
        ('abc', '{F} La canción incluye 10 segundos de una obra conocida sin permiso. ¿Qué corresponde?', 'Quitar ese fragmento o pedir el permiso', 'Publicar igual porque son pocos segundos', 'Cambiarle el título', 'Usar obras ajenas requiere la autorización de quien las creó.'),
        ('abc', '{F} ¿Qué dato personal no se debe publicar?', 'La dirección de la casa de un integrante', 'El nombre del grupo', 'El título de la canción', 'La dirección identifica y ubica a la persona.'),
        ('abc', '{F} Recibes un mensaje incómodo en los comentarios. ¿Qué haces?', 'Avisar a una persona adulta de confianza y guardar el mensaje', 'Responder con enojo', 'Publicar tus datos para aclarar', 'Un adulto de confianza puede ayudar a actuar con seguridad.'),
        ('abc', 'La edición de una grabación sirve para', 'ordenar partes y limpiar el audio', 'cambiar la autoría de la obra', 'evitar los créditos', 'Es un trabajo técnico sobre el audio.'),
        ('=', '{F} El grupo tiene 5 integrantes y 2 son menores. ¿Cuántos integrantes mayores de edad hay?', '5-2', 'Se restan los menores del total.', ' integrantes'),
        ('abc', 'Una canción es de autoría propia si', 'la crearon sus integrantes sin copiar fragmentos de otras personas', 'se parece a una canción conocida', 'se aprendió de oído', 'La autoría es de quien crea la obra.'),
        ('abc', '{F} ¿Quién decide qué comentarios se permiten?', 'Quien modera, según lo que acordó el grupo', 'Cualquier persona sin reglas', 'Nadie', 'La ficha pide decidir quién puede comentar.'),
        ('abc', 'Un compañero dice: «Si está en internet, puedo usarlo libre». ¿Qué respuesta es mejor?', 'Estar en internet no significa que se pueda usar sin permiso', 'Tiene razón, todo en internet es libre', 'Solo se puede usar si dura menos de un minuto', 'Los derechos de autor siguen vigentes.'),
        ('abc', '{F} ¿Por qué conviene usar solo nombres artísticos o primeros nombres, con permiso, en los créditos?', 'Para no difundir más datos personales de los necesarios', 'Para que nadie sea reconocido por su aporte', 'Para evitar tener que escribir créditos', 'Los créditos reconocen el aporte sin exponer datos personales de más.'),
        ('abc', 'Antes de publicar, ¿por qué conviene revisar la lista de verificación?', 'Para prevenir problemas de derechos, privacidad y seguridad', 'Para tardar más y así tener más tiempo para ensayar', 'Para evitar grabar y publicar la canción', 'Planificar los cuidados evita problemas posteriores.'),
    ],
    ctx=('abc', 'Un grupo graba una canción con un fragmento de una obra famosa «porque le da más fuerza». Quiere publicarla. ¿Qué es lo más adecuado?', 'Retirar el fragmento o conseguir el permiso antes de publicar', 'Publicar y esperar que nadie lo note', 'Cambiar el nombre del grupo', 'Se respetan los derechos de quien creó la obra.'),
    sc=[
        ('En Música: ¿Qué es el consentimiento?', 'Un permiso dado de forma libre y clara', 'Quien aparece en la obra debe aceptar.'),
        ('Si de 6 integrantes 4 son menores, ¿cuántos son mayores de edad?', '2', 'Al restar 4 de 6 quedan 2.'),
        ('abc', 'Ante mensajes incómodos en línea, lo correcto es', 'avisar a una persona adulta de confianza', 'responder con insultos', 'borrar todo en silencio', 'Un adulto de confianza ayuda a actuar de forma segura.'),
    ],
    op=("Con la {F} como modelo, escribe una lista de verificación de 6 pasos para publicar una obra tuya (real o de ejemplo), incluyendo derechos de autor, créditos, permisos, datos personales y qué hacer con un mensaje incómodo.",
        "1) Grabar a volumen moderado. 2) Editar el audio. 3) Revisar que la canción sea propia. 4) Escribir créditos con nombres artísticos. 5) Pedir permiso por escrito a una persona adulta responsable para menores. 6) No publicar datos personales; si llega un mensaje incómodo, avisar a una persona adulta de confianza.",
        ["seis pasos", "derechos y permisos", "seguridad en línea"], ["lista de verificación"], ["olvidar los permisos", "publicar datos personales"],
        "Reconoce la lista y pide agregar quién modera los comentarios."),
    reinforce="Escribe los créditos de una grabación de ejemplo con nombres artísticos.",
    extend="Averigua con tu docente qué significa que una obra sea de uso libre y anota un ejemplo.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (plan de difusión de ejemplo: un concierto de 40 minutos en el gimnasio del colegio). Objetivo: que asistan al menos 80 personas. Tareas y plazos: ensayo general (viernes), afiches en papel reciclado, invitaciones escritas a mano y montaje del escenario. "
     "Presupuesto de ejemplo (en pesos chilenos): 20 hojas de papel a $100 cada una = $2.000; cartulinas por $5.000; un cable de reemplazo por $10.000. El curso reúne $20.000 con una colecta. "
     "Regla: no se piden préstamos ni se vende nada a menores de edad sin permiso de una persona adulta responsable.")
build(
    O7, 3, F,
    use="Aprenderé a diseñar un proyecto de difusión: definir objetivos medibles, tareas con plazos y responsables, y un presupuesto simple, ajustando el plan a los recursos disponibles.",
    prior=["Defino propósito y audiencia.", "Cuido derechos y seguridad al difundir.", "Calculo costos y totales con números enteros."],
    explain=[
        "Un proyecto de difusión se diseña con un plan. Primero, un objetivo medible: qué se quiere lograr y cómo se sabrá que se logró (por ejemplo, «que asistan al menos 80 personas»). Luego, las tareas necesarias, cada una con un responsable y un plazo. También se calcula un presupuesto: la lista de gastos con su costo y el dinero disponible, para saber si alcanza.",
        "Para calcular un gasto se multiplica la cantidad por el precio de cada unidad: 20 hojas a $100 cuestan 20 × 100 = $2.000. El presupuesto total es la suma de todos los gastos. Si el total supera el dinero disponible, se ajusta el plan: se reducen gastos, se busca material reciclado o se prioriza lo esencial. No se piden préstamos ni se ponen en riesgo el dinero de otras personas.",
        "Un plan realista usa los recursos que existen. Se revisa el cronograma con tiempo de sobra para imprevistos y se deja una persona a cargo de cada tarea para que nada quede sin responsable.",
    ],
    vocab=[("objetivo medible", "meta que dice qué se quiere lograr y cómo se comprobará"), ("cronograma", "orden de las tareas con sus plazos"), ("responsable", "persona a cargo de una tarea"), ("presupuesto", "lista de gastos con su costo y el dinero disponible"), ("imprevisto", "situación inesperada que puede alterar el plan")],
    worked=[
        ("Calcular un gasto", "Se compran 15 hojas a $200 cada una. ¿Cuánto cuestan?", ["Cantidad: 15.", "Precio: $200 por hoja.", "15 × 200 = $3.000."], "$3.000"),
        ("Ver si alcanza", "Un grupo tiene $10.000 y sus gastos son $4.000 y $5.000. ¿Alcanza y cuánto sobra?", ["Gastos: 4.000 + 5.000 = 9.000.", "Disponible: 10.000.", "Sobra 10.000 − 9.000 = 1.000."], "Alcanza y sobran $1.000"),
    ],
    mistakes=[("Planear sin calcular el costo.", "Se descubre tarde que el dinero no alcanza.", "Suma los gastos y compara con lo disponible."),
              ("Dejar una tarea sin responsable.", "Nadie se hace cargo y se retrasa.", "Asigna un nombre y un plazo a cada tarea.")],
    T=[
        ('=', '{F} ¿Cuánto cuestan las 20 hojas de papel a $100 cada una?', '20*100', 'Se multiplica la cantidad de hojas por el precio de cada una.', ' pesos'),
        ('=', '{F} ¿Cuánto suma el presupuesto total (papel, cartulinas y cable)?', '2000+5000+10000', 'Se suman los tres gastos.', ' pesos'),
        ('=', '{F} El curso reúne $20.000. ¿Cuánto dinero sobra después de pagar el presupuesto total?', '20000-(2000+5000+10000)', 'Se resta el presupuesto del dinero disponible.', ' pesos'),
        ('abc', '{F} ¿Cuál es el objetivo medible del plan?', 'Que asistan al menos 80 personas', 'Que el concierto sea bonito', 'Que todos se diviertan', 'Dice qué se logrará y cómo se comprobará.'),
        ('abc', '{F} ¿Qué gasto es el más alto?', 'El cable de reemplazo', 'Las cartulinas', 'El papel', 'El cable cuesta $10.000, más que los otros.'),
        ('abc', '{F} Si el cable costara $15.000, ¿alcanzaría el dinero reunido?', 'No: el total sería $22.000 y supera los $20.000 reunidos', 'Sí, porque $15.000 es menor que $20.000', 'Sí, porque los otros gastos son chicos', 'El total pasaría a ser $22.000, que supera los $20.000.'),
        ('abc', '{F} El total no alcanza. ¿Qué ajuste es razonable?', 'Reducir gastos o usar material reciclado', 'Pedir un préstamo', 'Cancelar el concierto sin intentar otra opción', 'Se ajusta el plan con los recursos que se tienen.'),
        ('abc', 'Un cronograma debe incluir', 'tareas, responsables y plazos', 'solo los nombres del grupo', 'solo los gastos', 'Es lo que permite coordinar el trabajo.'),
        ('abc', '{F} ¿Qué regla de la ficha protege a las personas menores?', 'No se vende nada a menores sin permiso de una persona adulta responsable', 'Se pide dinero a todos los asistentes', 'Se vende a menores sin límite', 'La ficha incluye esa regla de forma explícita.'),
        ('abc', '{F} Si se reemplazan las cartulinas por material reciclado sin costo, ¿cuánto baja el presupuesto total?', '$5.000', '$7.000', '$17.000', 'Se deja de gastar lo que costaban las cartulinas, o sea $5.000.'),
        ('abc', 'Para prever imprevistos conviene', 'dejar tiempo de sobra en el cronograma para reaccionar', 'dejar todas las tareas para el último día', 'no asignar responsables', 'El margen permite reaccionar a lo inesperado.'),
        ('abc', '{F} ¿Por qué se recomienda un objetivo medible?', 'Para saber después si se logró', 'Para que parezca importante', 'Para evitar evaluarlo', 'La medición permite comprobar el logro.'),
        ('=', '{F} Si el cable costara $8.000 y las cartulinas $4.000, ¿cuánto sumaría el presupuesto con las hojas de $2.000?', '2000+4000+8000', 'Se suman los tres gastos nuevos.', ' pesos'),
    ],
    ctx=('abc', 'Un grupo quiere imprimir 100 invitaciones a $50 cada una, pero solo tiene $3.000. ¿Qué concluye?', 'No alcanza: costarían $5.000 y deben ajustar el plan', 'Alcanza porque 100 es menor que 3.000', 'Alcanza justo', '100 × 50 = $5.000, que supera los $3.000.'),
    sc=[
        ('En Música: ¿Qué es un presupuesto?', 'Una lista de gastos con su costo y el dinero disponible', 'Permite saber si el dinero alcanza.'),
        ('¿Cuánto cuestan 10 cartulinas a $300 cada una?', '3.000', 'Al multiplicar 10 por $300 resulta $3.000.'),
        ('abc', 'Un plan realista', 'usa los recursos disponibles', 'ignora los costos', 'se hace al final', 'Se adapta a lo que realmente existe.'),
    ],
    op=("Con la {F} como modelo, diseña un plan de difusión para una obra tuya (real o de ejemplo): objetivo medible, cuatro tareas con responsable y plazo, un presupuesto con al menos dos gastos calculados y qué harías si el dinero no alcanza.",
        "Objetivo: que asistan 50 personas a una audición. Tareas: afiches (Ana, lunes), ensayo (todos, miércoles), invitaciones (Luis, martes), montaje (Marta, jueves). Presupuesto: 30 hojas a $100 = $3.000; 4 cartulinas a $500 = $2.000; total $5.000. Si no alcanza, uso material reciclado.",
        ["objetivo medible", "tareas con responsable", "presupuesto calculado"], ["plan de difusión"], ["cálculos incorrectos", "tareas sin responsable"],
        "Reconoce el plan y pide revisar la suma del presupuesto."),
    reinforce="Calcula el costo de 12 hojas a $150 cada una.",
    extend="Haz un cronograma de cinco días para organizar un pequeño concierto en tu colegio.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (equipo de ejemplo de 5 estudiantes que gestiona la difusión de su canción). Roles: coordinadora (organiza las reuniones y el cronograma), responsable de producción (grabación y edición), responsable de comunicación (afiches y mensajes), responsable de finanzas (presupuesto) y responsable de seguridad y permisos (créditos, derechos y consentimiento). "
     "Acuerdos del equipo: reunirse 20 minutos cada semana; decidir con voto cuando no hay consenso; que cada tarea tenga un nombre y un plazo; y que las diferencias se conversen con respeto. Situación: la responsable de producción y el responsable de comunicación discrepan sobre la fecha del concierto.")
build(
    O7, 4, F,
    use="Aprenderé a gestionar un proyecto de difusión en equipo: repartir roles, tomar acuerdos, hacer reuniones breves y resolver diferencias con respeto, dejando todo registrado.",
    prior=["Diseño un plan con tareas y presupuesto.", "Cuido derechos y seguridad.", "Sé dar retroalimentación respetuosa."],
    explain=[
        "Gestionar colaborativamente es trabajar en equipo con roles claros, acuerdos y comunicación. Cada rol tiene una responsabilidad: coordinación, producción, comunicación, finanzas, seguridad y permisos. Tener roles no significa trabajar aislado: las personas se apoyan, se informan y revisan juntas las decisiones importantes. Un buen equipo acuerda cómo se tomarán las decisiones (por consenso o por votación), cada cuánto se reunirá y cómo se registrarán los acuerdos.",
        "Las reuniones breves funcionan mejor con una pauta: objetivo, tareas pendientes, decisiones y plazos. Se registran los acuerdos con nombre y fecha para que nada quede olvidado. Cuando hay una diferencia, como una fecha en desacuerdo, se conversa con respeto: cada persona expone sus razones, se buscan criterios compartidos (por ejemplo, la disponibilidad de la mayoría) y, si no hay consenso, se decide con el método acordado.",
        "Cuando el conflicto se vuelve ofensivo o alguien se siente mal, se avisa a una persona adulta de confianza. Todos los integrantes merecen ser tratados con respeto.",
    ],
    vocab=[("rol", "función y responsabilidad dentro del equipo"), ("consenso", "acuerdo al que llegan todas las personas"), ("votación", "forma de decidir cuando no hay consenso"), ("acta", "registro breve de los acuerdos de una reunión"), ("discrepancia", "diferencia de opinión sobre un asunto")],
    worked=[
        ("Asignar un rol", "¿Qué rol del equipo debe revisar que la canción no incluya fragmentos ajenos?", ["Es un tema de derechos.", "El rol de seguridad y permisos revisa créditos, derechos y consentimiento."], "La responsable de seguridad y permisos"),
        ("Resolver con votación", "El equipo de 5 vota la fecha: 3 votos para el jueves y 2 para el viernes. ¿Qué fecha se decide?", ["3 es mayor que 2.", "Se aplica el método de voto acordado."], "El jueves"),
    ],
    mistakes=[("Asumir que tener roles significa no ayudar en otras tareas.", "Se pierde apoyo y se acumula trabajo.", "Cada persona responde por su rol y colabora cuando se necesita."),
              ("No registrar los acuerdos.", "Se olvidan o se discuten de nuevo.", "Escribe un acta con nombres y plazos.")],
    T=[
        ('abc', '{F} ¿Qué rol organiza las reuniones y el cronograma?', 'La coordinadora, que organiza las reuniones y el cronograma', 'La responsable de finanzas', 'La responsable de comunicación', 'Lo indica de forma explícita la ficha del equipo.'),
        ('abc', '{F} ¿Qué rol revisa el presupuesto?', 'La responsable de finanzas', 'La coordinadora', 'La responsable de producción', 'Revisar el presupuesto es el rol de finanzas.'),
        ('=', '{F} El equipo se reúne 20 minutos cada semana durante 6 semanas. ¿Cuántos minutos son?', '20*6', 'Se multiplican los minutos por las semanas.', ' minutos'),
        ('abc', '{F} Hay discrepancia por la fecha del concierto. ¿Qué paso conviene primero?', 'Que cada persona exponga sus razones', 'Votar sin hablar', 'Que decida la persona de mayor edad', 'Primero se escucha, luego se decide.'),
        ('abc', '{F} Dos personas prefieren el jueves, dos el viernes y una el sábado. ¿Qué se debe hacer según los acuerdos?', 'Conversar y, si no hay consenso, votar', 'Elegir el sábado por ser el último', 'Cancelar el concierto', 'El acuerdo es decidir con voto si no hay consenso.'),
        ('abc', 'Una persona dice: «Mi rol es la comunicación, así que no me importa el presupuesto». ¿Qué respuesta es mejor?', 'Cada rol aporta, pero el equipo revisa juntas las decisiones importantes', 'Tiene razón, no debe preocuparse', 'Debe asumir todos los roles', 'El trabajo en equipo requiere información compartida.'),
        ('abc', '¿Qué debe tener el acta de una reunión?', 'Acuerdos, responsables y plazos', 'Solo la hora de término', 'Solo los chistes', 'Sirve para recordar los acuerdos y cumplirlos.'),
        ('abc', '{F} En una votación de las 5 personas, el viernes obtiene 1 voto y el resto vota por el jueves. ¿Cuántos votos tiene el jueves?', '4', '3', '5', 'Al restar 1 de 5 quedan 4 votos para el jueves.'),
        ('abc', 'Un integrante se siente ofendido por comentarios en una reunión. ¿Qué corresponde?', 'Avisar a una persona adulta de confianza y buscar un trato respetuoso', 'Tolerarlo en silencio para no generar un conflicto', 'Responder con insultos para defenderse en la reunión', 'El respeto es una condición de trabajo; un adulto puede ayudar.'),
        ('abc', '{F} ¿Qué criterio compartido sirve para elegir la fecha?', 'La disponibilidad de la mayoría del equipo y del público', 'La preferencia de quien habla más fuerte', 'El día que le tocaría a otro curso', 'Es un criterio objetivo y compartido.'),
        ('abc', 'Una buena pauta de reunión incluye', 'objetivo, pendientes, decisiones y plazos', 'solo los problemas', 'solo los nombres', 'Ordena el tiempo y los acuerdos.'),
        ('abc', '{F} Una integrante publicó una foto de un compañero menor de edad sin su permiso. ¿Qué rol debería revisar y corregir esto?', 'La responsable de seguridad y permisos, que cuida el consentimiento', 'La responsable de finanzas, que cuida el presupuesto', 'La coordinadora, que organiza el cronograma', 'Ese rol cuida créditos, derechos y consentimiento, que es lo que faltó en este caso.'),
        ('abc', '{F} La responsable de producción se atrasa con la edición. ¿Qué conviene hacer?', 'Preguntar qué apoyo necesita y ajustar el plazo si es razonable', 'Quitarle el rol sin hablar con la persona', 'Ignorar el atraso y esperar que se resuelva', 'La colaboración busca resolver, no culpar.'),
    ],
    ctx=('abc', 'En una reunión, dos integrantes discuten fuerte sobre la fecha. El equipo ya acordó resolver con voto si no hay consenso. ¿Qué es lo más coherente?', 'Escuchar ambas razones y votar según lo acordado', 'Posponer el tema sin fecha', 'Que decida el más antiguo del grupo', 'Se respetan los acuerdos que el equipo tomó antes.'),
    sc=[
        ('En Música: ¿Qué es un consenso?', 'Un acuerdo al que llegan todas las personas', 'Nadie queda fuera de la decisión.'),
        ('¿Cuántos minutos son 4 reuniones de 25 minutos?', '100', 'Al multiplicar 4 por 25 resulta 100.'),
        ('abc', 'Un acta sirve para', 'registrar acuerdos, responsables y plazos', 'reemplazar las reuniones', 'esconder desacuerdos', 'Evita que los acuerdos se olviden.'),
    ],
    op=("Con la {F} como modelo, escribe un acta de una reunión de tu equipo (real o de ejemplo) con: objetivo, tres acuerdos con responsable y plazo, y una discrepancia resuelta explicando cómo se resolvió.",
        "Objetivo: decidir la fecha. Acuerdos: Ana imprime afiches (lunes); Luis revisa créditos (martes); Marta confirma el lugar (miércoles). Discrepancia: jueves o viernes; cada quien dio razones y se votó (3 a 2). Se eligió el jueves.",
        ["objetivo", "tres acuerdos con plazo", "discrepancia resuelta"], ["acta escrita"], ["acuerdos sin responsable", "sin método de decisión"],
        "Reconoce el acta y pide agregar el nombre de quien registra."),
    reinforce="Escribe tres reglas para que una reunión de equipo sea respetuosa y breve.",
    extend="Propón un método de decisión distinto a la votación y explica cuándo conviene.",
)

# ============================================================ OAC-07, clase 5
F = ("Ficha 5 (resultados de ejemplo de un concierto escolar). Objetivo: que asistan al menos 80 personas. Asistieron 64. Se entregaron 30 encuestas breves y se recibieron 24 respuestas: 18 personas dijeron que la canción les gustó, 4 que les fue indiferente y 2 que no les gustó. "
     "Comentarios escritos de ejemplo: «No se entendía la letra al fondo del gimnasio» (3 personas) y «Faltó un lugar para sentarse» (2 personas). Gastos reales: $17.000. Dinero reunido: $20.000.")
build(
    O7, 5, F,
    use="Aprenderé a evaluar los resultados de una difusión con indicadores y comentarios, a comparar con el objetivo y a ajustar el proyecto para una próxima vez.",
    prior=["Diseño un plan con objetivo medible.", "Gestiono un equipo con acuerdos.", "Evalúo con evidencia."],
    explain=[
        "Evaluar una difusión es comparar lo logrado con el objetivo. Los indicadores son datos que se pueden contar o comprobar: cuántas personas asistieron, cuántas respuestas hubo, cuántas personas dijeron que les gustó, cuánto se gastó. Se comparan con la meta (por ejemplo, 80 asistentes) para ver si se cumplió, se cumplió en parte o no se cumplió.",
        "Además de los números, los comentarios cualitativos aportan información sobre qué mejorar: «no se entendía la letra al fondo» sugiere ajustar el sonido o la ubicación. Se agrupan los comentarios por tema y se priorizan los que más se repiten o más afectan al propósito. También se revisan los gastos: si hubo dinero sobrante o faltante y por qué.",
        "Con estos datos se ajusta el proyecto: se decide qué se conserva, qué se cambia y cómo se comprobará la mejora la próxima vez. Se agradece a quienes participaron y se registra todo para el equipo siguiente.",
    ],
    vocab=[("indicador", "dato que permite medir si se logró algo"), ("cualitativo", "que describe cualidades, como los comentarios escritos"), ("cumplimiento", "grado en que se alcanzó el objetivo"), ("encuesta", "preguntas breves para recoger opiniones"), ("ajuste", "cambio para mejorar el siguiente proyecto")],
    worked=[
        ("Comparar con la meta", "En otro evento de ejemplo la meta era 100 personas y asistieron 72. ¿Cuántas personas faltaron?", ["Se resta lo logrado de la meta.", "100 − 72 = 28."], "Faltaron 28 personas"),
        ("Leer una encuesta", "Se entregaron 30 encuestas y se recibieron 21 respuestas. ¿Cuántas no se devolvieron?", ["Se restan las respuestas recibidas de las entregadas.", "30 − 21 = 9."], "9 encuestas"),
    ],
    mistakes=[("Medir el éxito solo por la cantidad de asistentes.", "Se pierden la opinión del público y los aprendizajes del proceso.", "Combina indicadores numéricos con comentarios."),
              ("Ignorar los comentarios que pocas personas mencionan.", "Pueden señalar problemas reales, como accesibilidad.", "Léelos todos y prioriza según el propósito.")],
    T=[
        ('=', '{F} ¿Cuántas personas faltaron para llegar a la meta de asistencia?', '80-64', 'Se resta lo logrado de la meta.', ' personas'),
        ('=', '{F} ¿Cuánto dinero sobró del reunido, si los gastos reales fueron $17.000?', '20000-17000', 'Se resta el gasto real del dinero reunido.', ' pesos'),
        ('abc', '{F} ¿Se cumplió el objetivo de asistencia?', 'No, asistieron menos de 80 personas', 'Sí, asistieron más de 80', 'Sí, porque hubo encuestas', 'Como 64 es menor que 80, la meta no se alcanzó.'),
        ('abc', '{F} ¿Cuántas respuestas de la encuesta no fueron positivas?', '6', '2', '4', '4 indiferentes más 2 que no les gustó suman 6.'),
        ('abc', '{F} ¿Qué comentario sugiere mejorar el sonido o la ubicación?', 'No se entendía la letra al fondo del gimnasio', 'Faltó un lugar para sentarse', 'La canción les gustó', 'Habla de claridad auditiva según el lugar.'),
        ('abc', '{F} De las 24 respuestas, 18 fueron positivas. ¿Qué afirmación es correcta?', 'Fueron más de la mitad de las respuestas, porque la mitad es 12', 'Fueron menos de la mitad', 'Fueron exactamente la mitad', 'La mitad de 24 es 12, y 18 es más que eso.'),
        ('abc', 'Un indicador es', 'un dato que permite medir si se logró algo', 'una opinión sin razones', 'un instrumento', 'Se puede contar o comprobar de manera objetiva.'),
        ('abc', '{F} ¿Qué ajuste para la próxima vez responde al comentario del fondo del gimnasio?', 'Probar el sonido desde el fondo antes del concierto', 'Cancelar el concierto', 'Subir el volumen al máximo', 'Se resuelve con una prueba, sin dañar los oídos.'),
        ('abc', '{F} ¿Qué dato muestra que el proyecto fue financieramente viable?', 'Los gastos reales fueron menores que el dinero reunido', 'Se hicieron más afiches', 'Asistieron 64 personas', 'No se gastó más de lo que se tenía.'),
        ('abc', 'Una compañera dice: «Como no llegamos a 80, el proyecto fracasó». ¿Qué respuesta es más completa?', 'No se cumplió la meta de asistencia, pero hay logros que conservar', 'Tiene razón: sin la meta, no sirvió nada del proyecto', 'La meta de asistencia no importa para evaluar', 'Una evaluación equilibrada mira logros y límites.'),
        ('abc', '{F} 3 personas dijeron que no se entendía la letra y 2 que faltó dónde sentarse. ¿Cuál tema se repite más?', 'La claridad de la letra', 'El lugar para sentarse', 'Ambos igual', 'Como 3 es mayor que 2, ese tema se repite más.'),
        ('abc', 'Después de evaluar, ¿qué conviene dejar para el próximo equipo?', 'Un registro de datos, comentarios y ajustes', 'Nada, porque cada equipo debe empezar de cero', 'Solo las fotos del evento para recordarlo', 'El registro ayuda a evitar repetir los mismos errores.'),
        ('abc', '{F} Si la próxima meta es 90 asistentes, ¿cuántos más que los 64 de esta vez deben llegar?', '26', '16', '36', 'Al restar 64 de 90 se obtiene 26.'),
    ],
    ctx=('abc', 'Un equipo revisa su evaluación: cumplió la meta de asistencia pero 10 personas escribieron que no pudieron ver el escenario. ¿Qué es lo más razonable?', 'Valorar el logro y ajustar la ubicación del público para la próxima vez', 'Ignorar los comentarios porque se cumplió la meta', 'Culpar a quienes asistieron', 'Los comentarios indican qué mejorar aun cuando la meta se cumplió.'),
    sc=[
        ('En Música: En Música: ¿Qué es un indicador?', 'Un dato que permite medir si se logró algo', 'Se compara con la meta para ver si se logró.'),
        ('Si la meta era 50 y asistieron 41, ¿cuántas personas faltaron?', '9', 'Al restar 41 de 50 faltan 9.'),
        ('abc', 'Los comentarios cualitativos sirven para', 'saber qué mejorar, algo que los números solos no muestran', 'reemplazar los datos numéricos', 'justificar cualquier decisión', 'Aportan información que los números no muestran.'),
    ],
    op=("Con la {F} como modelo, evalúa una difusión tuya o de ejemplo: compara dos indicadores con la meta, resume un comentario cualitativo, nombra un logro y un límite, y escribe dos ajustes concretos para la próxima vez.",
        "Meta: 50 asistentes; asistieron 41 (faltaron 9). Encuesta: 15 de 20 dijeron que les gustó. Comentario: «No se veía el escenario». Logro: buena recepción de la canción. Límite: asistencia menor a la meta. Ajustes: difundir una semana antes y ubicar mejor al público.",
        ["dos indicadores", "logro y límite", "dos ajustes concretos"], ["evaluación escrita"], ["solo números", "ajustes vagos"],
        "Reconoce la evaluación y pide indicar cómo comprobará cada ajuste."),
    reinforce="Escribe tres preguntas breves para una encuesta de opinión sobre una presentación.",
    extend="Compara los resultados de dos difusiones distintas y concluye qué medio sirvió mejor al propósito.",
)
