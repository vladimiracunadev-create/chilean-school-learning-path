"""Danza 3.º y 4.º medio FG: OAC-06 (gestión y difusión de proyectos de danza), clases 1 a 5. Casos ficticios; sin plataformas reales."""
from __future__ import annotations

from fg_danz_common import build

O6 = "FG-DANZ-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Muestra de danza «Marea» del colectivo escolar ficticio, en el gimnasio del colegio. "
     "Objetivo: que asistan al menos 60 personas de la comunidad escolar. Público: familias y estudiantes del colegio. Mensaje central: «una obra de danza hecha por estudiantes, abierta y gratuita». "
     "Equipo de 8 personas con 4 roles (difusión, producción, técnica y registro), dos personas por rol. Plazo: 4 semanas desde hoy.")
build(
    O6, 1, F,
    use="Aprenderé a diseñar y organizar en equipo un proyecto de difusión de una obra de danza: definir objetivo, público, mensaje, roles y calendario.",
    prior=["Sé trabajar en grupo con acuerdos.", "Sé estructurar una obra.", "Sé que las personas tienen derechos sobre su imagen y su cuerpo."],
    explain=[
        "Difundir una obra es hacerla conocida para que llegue a su público. Un proyecto de difusión parte con cuatro decisiones: el objetivo (qué se quiere lograr, con una cifra o una condición observable, como «60 personas»), el público (a quién se dirige), el mensaje (qué se quiere que sepan y sientan, en pocas palabras) y los medios (cómo se comunicará). Un objetivo vago como «que vaya mucha gente» no se puede evaluar.",
        "La gestión colaborativa reparte el trabajo en roles y fechas. Por ejemplo, 8 personas y 4 roles dejan dos personas por rol; con 4 semanas, se puede decidir qué se hace en cada una (semana 1: diseñar el mensaje; semana 2: preparar materiales; semana 3: difundir; semana 4: confirmar y presentar). Un calendario realista incluye un margen para imprevistos. En la ficha, difusión comunica la muestra, producción organiza el espacio y los materiales, técnica cuida la luz y el sonido, y registro anota y guarda evidencia (fotos solo con autorización).",
        "Todo el equipo cuida la seguridad de la presentación (espacio, aforo, vías de salida) y el respeto a las personas: ninguna persona debe aparecer en material de difusión sin su autorización. Si el equipo tiene un desacuerdo, lo resuelve conversando y votando, y avisa a una persona adulta cuando no puede resolverlo.",
    ],
    vocab=[("difusión", "hacer conocida una obra para que llegue a su público"), ("objetivo", "lo que se quiere lograr, con una meta observable"), ("público", "personas a quienes se dirige la obra"), ("mensaje", "idea central que se quiere comunicar"), ("rol", "responsabilidad concreta dentro del equipo")],
    worked=[
        ("Revisar un objetivo", "¿Es «que vaya mucha gente» un buen objetivo? Reescríbelo.", ["No tiene cifra ni condición, así que no se puede evaluar.", "Una versión observable: que asistan al menos 60 personas de la comunidad escolar."], "No; mejor: que asistan al menos 60 personas"),
        ("Repartir roles", "En la ficha, ¿cuántas personas hay por rol?", ["Son 8 personas y 4 roles.", "8 ÷ 4 = 2 personas por rol."], "2 personas por rol"),
    ],
    mistakes=[("Plantear un objetivo sin número («que se conozca»).", "No se puede evaluar si se logró.", "Pon una cifra o condición observable."),
              ("Dejar a una sola persona haciendo todas las tareas.", "El trabajo se acumula y el equipo pierde ideas.", "Reparte roles y fechas con acuerdos.")],
    T=[
        ('abc', '¿Qué es el público de un proyecto de difusión?', 'Las personas a quienes se dirige la obra', 'Las personas que integran el equipo de trabajo', 'Los medios que se usarán para anunciar la obra', 'El público es el destinatario a quien se dirige la obra.'),
        ('abc', '{F} ¿Cuál es el objetivo de la ficha?', 'Que asistan al menos 60 personas de la comunidad escolar', 'Que el equipo se divierta mucho preparando y presentando la muestra', 'Que la obra sea hermosa y que a todo el mundo le guste mucho', 'Es el único con una cifra observable.'),
        ('=', '{F} ¿Cuántas personas hay por rol?', '8//4', 'Se reparten 8 personas entre 4 roles.', ' personas'),
        ('abc', '{F} ¿Cuál es un mensaje central bien formulado?', 'Una obra de danza hecha por estudiantes, abierta y gratuita', 'Vayan o se arrepentirán, porque no habrá otra función de esta obra', 'Es la mejor obra del año y no se la pueden perder, así que vengan todos', 'Es breve, comprensible y dirigido al público.'),
        ('abc', '{F} ¿Qué rol se encarga de que la sala esté lista y segura?', 'Producción', 'Registro', 'Difusión', 'Producción organiza el espacio y los medios materiales.'),
        ('abc', 'Un objetivo observable permite', 'evaluar al final si se logró', 'saber qué opinan todas las personas', 'omitir el calendario del proyecto, porque ya está claro qué hacer', 'Una meta observable se puede comprobar.'),
        ('abc', '{F} ¿Cuál tarea corresponde a la semana 1?', 'Diseñar el mensaje y definir medios', 'Presentar la obra', 'Evaluar los resultados', 'La planificación parte con el mensaje.'),
        ('=', '{F} Si cada persona del equipo invita a 9 personas, ¿cuántas invitaciones salen en total?', '8*9', 'Se multiplica el número de personas por las invitaciones.', ' invitaciones'),
        ('abc', '{F} Una integrante no quiere aparecer en el material de difusión. ¿Qué corresponde?', 'Respetar su decisión y usar otro material que no la muestre', 'Poner igual su foto, porque es parte del grupo', 'Pedirle que decida el último día', 'La imagen personal requiere la autorización de quien aparece.'),
        ('abc', 'Dos integrantes discuten quién coordina difusión. ¿Cuál es una solución respetuosa?', 'Conversar, proponer ambas y votar, o rotar el rol', 'Que decida el integrante más antiguo del equipo, porque tiene más experiencia', 'Que no haya ese rol y que cada persona difunda por su cuenta', 'Se resuelve con diálogo y acuerdos.'),
        ('=', 'Un equipo de 9 personas se reparte en 3 roles por igual. Si 3 personas se retiran, ¿cuántas quedan por rol?', '(9-3)//3', 'Se restan las personas que se retiran y se reparte entre 3 roles.', ' personas'),
        ('abc', 'El calendario es de 4 semanas y hay un día feriado en la semana 3. ¿Qué decisión es más razonable?', 'Planificar con margen y adelantar tareas de esa semana', 'No considerar el feriado y mantener el calendario tal como estaba planificado', 'Cancelar la muestra porque el calendario no alcanza para todas las tareas', 'Un calendario realista considera imprevistos y deja un margen de tiempo.'),
        ('abc', 'El equipo quiere atraer a 60 personas, pero el gimnasio permite 50 por seguridad. ¿Qué corresponde?', 'Ajustar el objetivo o hacer dos funciones, respetando el aforo', 'Dejar entrar a las 60 personas igualmente, porque el objetivo es lo primero', 'Ocultar el límite de aforo para que nadie se desanime de asistir', 'El aforo es una regla de seguridad.'),
    ],
    ctx=('abc', 'Un equipo de 6 quiere difundir una obra en 3 semanas. Propone: semana 1 mensaje y roles; semana 2 afiches y mensajes; semana 3 confirmar asistencia y función. ¿Qué falta para tener un plan más completo?', 'Fijar un objetivo con cifra y responsables de cada tarea', 'Cambiar el título de la obra por uno que suene más atractivo', 'Hacer los afiches más grandes y de colores más llamativos para el hall', 'Un plan necesita objetivo observable y responsables.'),
    sc=[
        ("En Danza: ¿qué es la difusión?", "Hacer conocida una obra para que llegue a su público", "Es una parte de la gestión."),
        ("¿Qué debe tener un objetivo para poder evaluarse?", "Una cifra o condición observable", "Así se puede comprobar al final si se logró."),
        ("¿Qué se hace si alguien no quiere aparecer en el material de difusión?", "Se respeta y se usa otro material", "La imagen es personal y su uso depende de quien aparece."),
    ],
    op=("Diseña un proyecto de difusión (ficticio) con objetivo con cifra, público, mensaje, 3 roles con responsables (nombres inventados) y un calendario de 3 semanas.",
        "Objetivo: 40 personas del curso y sus familias. Público: familias y estudiantes de primero a tercero medio. Mensaje: «danza hecha por estudiantes, abierta y gratuita». Roles: difusión (Ana y Luis), producción (Carla), registro (Diego). Semana 1 mensaje; semana 2 materiales; semana 3 función.",
        ["objetivo con cifra", "público y mensaje claros", "roles y calendario"],
        ["hoja con el plan"],
        ["objetivo sin número", "no repartir roles"],
        "Pregunta: «¿cómo sabrán si lo lograron?». Si no hay cifra, pídele agregar una."),
    reinforce="Escribe un objetivo con cifra y un mensaje de una línea para una muestra de danza ficticia.",
    extend="Explica por qué un objetivo sin cifra es difícil de evaluar.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (medios de ejemplo, inventados). "
     "Afiche impreso en el colegio: llega a quienes pasan por el hall; se hace con autorización de dirección. "
     "Invitación por el grupo de mensajería del curso: gratuita; llega a quienes están en el grupo y a sus familias si la reenvían. "
     "Programa de mano en papel: lo reciben las personas que asisten, con el orden de la obra y los créditos. "
     "Aviso en la radio escolar: dura 30 segundos; llega a quien escucha la radio en el recreo.")
build(
    O6, 2, F,
    use="Aprenderé a escoger medios y tecnologías de comunicación (TIC) según el público y a redactar un mensaje claro, accesible y respetuoso para una obra de danza.",
    prior=["Sé qué es el público y el mensaje.", "Sé que las imágenes de personas requieren autorización.", "Sé hacer un plan con roles."],
    explain=[
        "Un medio es el canal por el que se comunica un mensaje: papel, mensajería, redes, audio, video. Las TIC son las tecnologías de la información y la comunicación, como el correo, la mensajería o las páginas web. Se elige el medio según el público: si se quiere llegar a estudiantes que pasan por el hall, sirve un afiche; si se quiere llegar a familias, sirve una invitación que puedan reenviar.",
        "Un mensaje de difusión claro responde seis preguntas: qué (nombre de la obra), quién (el colectivo), cuándo, dónde, para quién y cómo asistir (gratis, sin inscripción). Debe ser breve y fácil de leer. Para ser accesible, usa letra grande, buen contraste y texto en lugar de solo imagen, y evita siglas que el público no conozca. Se evita prometer algo que no se cumplirá.",
        "Antes de publicar en un medio del colegio se pide autorización a la dirección o a quien corresponda. Se cuidan los datos personales: no se publican direcciones, teléfonos ni horarios de personas del equipo.",
    ],
    vocab=[("medio", "canal por el que se comunica un mensaje"), ("TIC", "tecnologías de la información y la comunicación"), ("accesible", "que más personas pueden leer o escuchar sin dificultad"), ("alcance", "cuántas personas puede llegar a un mensaje"), ("datos personales", "información privada de una persona")],
    worked=[
        ("Elegir un medio", "Quieres que las familias reciban la invitación sin costo. ¿Qué medio de la ficha sirve?", ["La invitación por mensajería es gratuita.", "Puede reenviarse a familias."], "La invitación por mensajería"),
        ("Revisar un mensaje", "«Muestra de danza, vengan». ¿Qué le falta?", ["No dice cuándo ni dónde ni cómo asistir.", "Agrega fecha, lugar, para quién y que es gratuita."], "Falta cuándo, dónde y cómo asistir"),
    ],
    mistakes=[("Usar un solo medio para todo el público.", "No todos los públicos usan el mismo canal.", "Combina medios según a quién quieres llegar."),
              ("Publicar el teléfono personal de una integrante para consultas.", "Expone datos privados.", "Usa un contacto del colegio o del colectivo.")],
    T=[
        ('abc', '¿Qué es un medio de difusión?', 'El canal por el que se comunica un mensaje', 'La idea central que se quiere comunicar', 'La cantidad de personas que asisten', 'Un medio es el canal por el que se comunica un mensaje.'),
        ('abc', '{F} ¿Qué medio llega a quienes pasan por el hall?', 'El afiche impreso', 'La radio escolar', 'El programa de mano', 'El afiche está en el hall.'),
        ('abc', '{F} ¿Quiénes reciben el programa de mano?', 'Las personas que asisten a la función', 'Quienes pasan por el hall', 'Quienes escuchan la radio', 'El programa de mano se entrega a quienes asisten a la función.'),
        ('=', '{F} El aviso de radio dura 30 segundos y se emite 4 veces por día durante 5 días. ¿Cuántos segundos de aviso se emiten?', '30*4*5', 'Se multiplican los segundos por las repeticiones y los días.', ' segundos'),
        ('abc', '{F} Quieres llegar a las familias. ¿Qué medio conviene?', 'La invitación por mensajería, que puede reenviarse', 'La radio escolar, porque más gente la oye en la casa', 'El afiche en el hall, que es el que más ve toda la comunidad', 'La invitación reenviable llega a las familias.'),
        ('abc', '¿Cuál mensaje responde más preguntas básicas?', '«Danza «Marea», viernes a las 18:00 en el gimnasio, gratis, abierta a todas las personas»', '«Vengan a nuestra obra, que está muy bonita y con muchas ganas de que asistan»', '«La mejor obra de todo el colegio, hecha por el grupo más entusiasta del año»', 'Incluye qué, cuándo, dónde y cómo asistir.'),
        ('abc', 'Para que un afiche sea accesible conviene', 'usar letra grande, buen contraste y texto claro', 'usar letra pequeña con muchos adornos', 'usar solo imagen sin texto', 'La accesibilidad mejora la lectura para más personas.'),
        ('abc', '{F} Para el afiche se necesita autorización. ¿De quién?', 'De la dirección del colegio', 'De ninguna persona, porque los afiches del colegio no requieren permiso', 'Del público que asistirá a la función, que puede aceptar o no el afiche', 'La ficha indica que el afiche se hace con esa autorización.'),
        ('=', '{F} Se imprimen 25 afiches y cada uno cuesta $150. ¿Cuánto cuestan en total?', '25*150', 'Se multiplican los afiches por el precio.', ' pesos'),
        ('abc', 'Un integrante propone poner su número de teléfono personal en el afiche para consultas. ¿Qué corresponde?', 'No hacerlo y usar un contacto del colectivo o del colegio', 'Hacerlo para que sea más fácil que las personas consulten y se inscriban', 'Pedirle a todo el equipo que ponga el suyo', 'Los datos personales de una integrante no se publican.'),
        ('abc', 'El afiche usa texto muy pequeño y colores claros sobre fondo claro. ¿Qué problema tiene?', 'Poca accesibilidad: es difícil de leer', 'Es demasiado largo y por eso no se alcanza a leer en el hall', 'No tiene título ni nombre del colectivo, así que no se entiende de qué se trata', 'El contraste bajo y el texto pequeño dificultan leer.'),
        ('=', 'La invitación por mensajería llega a 40 personas y cada una la reenvía a 2 más. ¿Cuántas personas la reciben en total, contando las 40?', '40+40*2', 'Se suman las 40 iniciales y las que reciben el reenvío.', ' personas'),
        ('abc', 'Quieren anunciar «entrada liberada» pero habrá que inscribirse. ¿Qué corresponde?', 'Informar claramente la inscripción para no engañar al público', 'No decir nada sobre la inscripción para que no disminuya la cantidad de asistentes', 'Quitar el aviso de entrada liberada y no publicar nada más sobre el costo', 'El mensaje debe ser veraz y avisar de la inscripción.'),
    ],
    ctx=('abc', 'Un equipo debe comunicar su muestra a estudiantes de primero medio y a sus familias, sin gastar dinero. ¿Qué combinación es adecuada?', 'Invitación por mensajería del curso y aviso en la radio escolar, con texto claro', 'Una publicación con una foto de un integrante sin su permiso', 'Un afiche con el número de teléfono de una persona', 'Combina medios sin costo y no expone datos.'),
    sc=[
        ("En Danza: ¿qué son las TIC?", "Tecnologías de la información y la comunicación", "Las TIC incluyen, por ejemplo, el correo y la mensajería."),
        ("¿Qué datos no se publican?", "Datos personales como teléfonos o direcciones", "Esos datos son información privada de las personas."),
        ("¿Qué preguntas responde un mensaje claro?", "Qué, quién, cuándo, dónde, para quién y cómo asistir", "Así el público sabe qué hacer."),
    ],
    op=("Elige dos medios de la ficha y redacta, para cada uno, un mensaje breve de tu muestra ficticia con qué, quién, cuándo, dónde, para quién y cómo asistir. No incluyas datos personales.",
        "Radio: «Muestra de danza «Marea» del colectivo escolar, viernes 18:00 en el gimnasio. Para estudiantes y familias, gratis». Mensajería: «Te invitamos al estreno de «Marea». Viernes a las 18:00, en el gimnasio. Entrada gratuita. ¡Reenvía!»",
        ["dos medios con mensajes", "seis datos básicos", "sin datos personales"],
        ["hoja con dos mensajes"],
        ["omitir fecha o lugar", "incluir teléfonos personales"],
        "Pregunta: «¿qué datos faltan para asistir?». Si falta alguno, pídele agregarlo."),
    reinforce="Redacta una invitación breve para una muestra ficticia con los seis datos básicos.",
    extend="Explica por qué conviene combinar al menos dos medios para llegar a un público variado.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (presupuesto de ejemplo, inventado, en pesos chilenos). "
     "25 afiches impresos a $120 cada uno. 70 programas de mano a $60 cada uno. Cartulina para señalética: $2.400. "
     "Sala: el colegio la presta sin costo. Equipo: 8 personas que aportarán lo mismo. Fondo previo disponible: $0.")
build(
    O6, 3, F,
    use="Aprenderé a producir un proyecto de danza con un presupuesto simple: listar recursos, calcular costos, repartirlos entre el equipo y buscar alternativas sin costo.",
    prior=["Sé usar billetes y monedas chilenos.", "Sé planificar un proyecto.", "Sé repartir cantidades en partes iguales."],
    explain=[
        "Producir una muestra es conseguir y organizar los recursos necesarios: espacio, materiales, tiempo, personas y, a veces, dinero. Un presupuesto es una lista de gastos con su costo. Se calcula multiplicando la cantidad de cada ítem por su precio y sumando los totales. Por ejemplo, 25 afiches a $120 cuestan 25 × 120 = $3.000.",
        "Si el total se reparte entre las personas del equipo, se divide el total por la cantidad de personas. Si el reparto no es exacto, se ajusta con un aporte voluntario o se reducen los gastos. Siempre existe la posibilidad de buscar alternativas sin costo: pedir una sala prestada, usar material reciclable seguro, o reducir la cantidad de impresiones.",
        "La producción también incluye seguridad y permisos: un espacio con salidas despejadas, el aforo respetado, el piso libre de objetos y la autorización para usar el espacio. Ninguna persona debe sentirse obligada a aportar dinero; se ofrecen alternativas de aporte, como tiempo o materiales.",
    ],
    vocab=[("presupuesto", "lista de gastos con su costo"), ("ítem", "cada elemento de una lista de gastos"), ("producción", "organizar los recursos necesarios para una muestra"), ("aporte", "contribución de una persona al proyecto"), ("alternativa sin costo", "opción que evita gastar dinero")],
    worked=[
        ("Calcular un ítem", "¿Cuánto cuestan los 70 programas de mano?", ["Se multiplica la cantidad por el precio.", "70 × 60 = $4.200."], "$4.200"),
        ("Total y reparto", "¿Cuánto suma el presupuesto y cuánto aporta cada persona de las 8?", ["Total: 25 × 120 + 70 × 60 + 2.400 = 3.000 + 4.200 + 2.400 = $9.600.", "Aporte: 9.600 ÷ 8 = $1.200."], "Total $9.600; cada persona aporta $1.200"),
    ],
    mistakes=[("Olvidar un ítem en el presupuesto y descubrirlo el día de la muestra.", "El total real queda más alto.", "Lista todos los ítems antes de sumar."),
              ("Exigir el mismo aporte en dinero a todas las personas sin alternativa.", "No todas pueden aportar y se generan presiones.", "Ofrece alternativas, como tiempo o materiales.")],
    T=[
        ('abc', '¿Qué es un presupuesto?', 'Una lista de gastos con su costo', 'Una lista de personas con sus roles', 'La fecha en que se hará la muestra', 'El presupuesto lista gastos y costos.'),
        ('=', '{F} ¿Cuánto cuestan los 25 afiches?', '25*120', 'Se multiplica la cantidad por el precio de cada uno.', ' pesos'),
        ('=', '{F} ¿Cuánto cuestan los 70 programas de mano?', '70*60', 'Se multiplica la cantidad por el precio de cada uno.', ' pesos'),
        ('=', '{F} ¿Cuánto suma el presupuesto total?', '25*120+70*60+2400', 'Se suman los tres costos de la lista.', ' pesos'),
        ('=', '{F} Si las 8 personas aportan lo mismo, ¿cuánto aporta cada una?', '(25*120+70*60+2400)//8', 'Se divide el total entre las 8 personas.', ' pesos'),
        ('abc', '{F} ¿Qué ítem no cuesta?', 'La sala, que el colegio presta', 'La cartulina para la señalética, que ya está incluida en el presupuesto', 'Los afiches, porque se imprimen en el mismo colegio', 'La ficha dice que la sala se presta.'),
        ('abc', '{F} Una persona no puede aportar dinero. ¿Qué corresponde?', 'Ofrecerle aportar con tiempo o materiales', 'Pedirle que pida dinero prestado para que aporte lo mismo que las demás personas', 'Excluirla del equipo de producción mientras no pueda aportar dinero', 'Existen otras formas de aportar, como tiempo o materiales.'),
        ('abc', '{F} Quieren gastar $1.200 menos. ¿Qué decisión lo logra?', 'Imprimir 50 programas en lugar de 70', 'Imprimir 50 afiches en lugar de 25, para tener más reserva', 'Comprar más cartulina para una señalética más grande', 'Imprimir 20 programas menos ahorra 20 × 60 = $1.200.'),
        ('abc', '{F} ¿Cuál es una alternativa sin costo para los afiches?', 'Reemplazar parte de los afiches por avisos en la mensajería del curso, que no tiene costo', 'Pedir a cada persona que pague de más para poder cubrir cualquier imprevisto', 'Imprimir todo en color para que el material se vea más atractivo', 'Disminuir las impresiones evita costos innecesarios.'),
        ('=', '{F} El total del presupuesto se paga con un billete de $10.000. ¿Cuánto vuelto se recibe?', '10000-(25*120+70*60+2400)', 'Se resta el total del presupuesto del billete con que se paga.', ' pesos'),
        ('abc', 'Antes de usar un patio para la muestra, ¿qué es adecuado?', 'Revisar que esté despejado y pedir autorización', 'Usarlo sin avisar', 'Cerrar las salidas para mantener el orden y evitar que el público entre y salga', 'La producción incluye permisos y seguridad.'),
        ('=', 'Un equipo de 6 recibe un presupuesto total de $7.200 y aporta lo mismo cada integrante. ¿Cuánto aporta cada uno?', '7200//6', 'Se divide el total entre las 6 personas.', ' pesos'),
        ('abc', 'El presupuesto se pasó en $600. ¿Qué decisión es razonable?', 'Revisar ítems y recortar o buscar alternativas sin costo', 'No pagar un ítem del presupuesto, el que sea más caro, y avisar después', 'Cancelar la muestra porque el calendario no alcanza para todas las tareas', 'Se ajusta el plan con alternativas.'),
    ],
    ctx=('abc', 'Un equipo de 5 tiene un presupuesto de $8.000. Cuenta con $3.000 de un fondo previo. ¿Cuánto debe aportar cada integrante si reparten el resto por igual?', '$1.000', '$1.600', '$800', 'Faltan 8.000 − 3.000 = 5.000 y 5.000 ÷ 5 = 1.000.'),
    sc=[
        ("En Danza: ¿cómo se calcula el costo de un ítem?", "Multiplicando cantidad por precio", "Así se obtiene el total del ítem."),
        ("¿Qué se hace si alguien no puede aportar dinero?", "Se ofrecen otras formas de aportar", "No se presiona a nadie para aportar dinero."),
        ("¿Qué se revisa antes de usar un espacio?", "Que esté despejado y con autorización", "Revisar el espacio es una medida de seguridad y de permiso."),
    ],
    op=("Arma un presupuesto de 3 ítems para la difusión de una muestra ficticia (cantidad, precio, total), suma el total y calcula el aporte por persona de un equipo de 5. Propón una alternativa sin costo.",
        "Afiches: 20 × $100 = $2.000. Programas: 50 × $50 = $2.500. Señalética: $1.500. Total $6.000. Aporte por persona: $1.200. Alternativa: usar la mensajería del curso en lugar de imprimir más afiches.",
        ["cantidad y precio por ítem", "suma y reparto correctos", "alternativa sin costo"],
        ["hoja con presupuesto y reparto"],
        ["olvidar ítems", "no ofrecer alternativas de aporte"],
        "Pregunta: «¿cuánto aporta cada persona?». Si el cálculo no cierra, pídele revisar la suma."),
    reinforce="Calcula el costo de 30 copias a $40 y 10 carpetas a $200, y súmalos.",
    extend="Explica por qué conviene buscar alternativas sin costo antes de pedir dinero al equipo.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (casos de ejemplo, inventados, sobre difusión digital de una muestra de danza). "
     "Caso 1: se quiere publicar una foto del ensayo en la que aparecen 5 estudiantes; una de ellas dice que no quiere salir. "
     "Caso 2: se quiere poner de fondo una canción comercial muy conocida en un video de la muestra. "
     "Caso 3: alguien deja un comentario burlón sobre el cuerpo de un integrante en una publicación. "
     "Caso 4: el afiche digital incluye la dirección de la casa de una integrante para que le escriban.")
build(
    O6, 4, F,
    use="Aprenderé a difundir con TIC de manera segura y respetuosa: pedir consentimiento, cuidar datos personales, usar música y materiales con permiso y actuar frente a comentarios ofensivos.",
    prior=["Sé qué es el consentimiento.", "Sé escoger medios de difusión.", "Sé que las obras tienen derechos de autor."],
    explain=[
        "Difundir en internet o por mensajería llega a muchas personas y es difícil de retirar. Por eso se aplican cuatro reglas. Primera: consentimiento. Nadie debe salir en una foto o video sin su autorización; si la persona es menor de 18 años, además se pide la autorización de su madre, padre o apoderado según las reglas del colegio. Quien dice que no, no sale. Segunda: datos personales. No se publican direcciones, teléfonos ni horarios de las personas.",
        "Tercera: derechos de autor. Las canciones, imágenes y videos pertenecen a quien los creó; se usa música propia del grupo o con autorización de su autor. Cuarta: comentarios. Si alguien deja un comentario ofensivo o sobre el cuerpo de una persona, no se responde con agresión; se guarda una captura, se bloquea o se oculta el comentario y se avisa a una persona adulta del colegio. No se borran los mensajes originales que sirven de evidencia.",
        "Nunca se comparten ni se reenvían imágenes íntimas o que avergüencen a alguien. Si un integrante se siente presionado o amenazado en línea, lo cuenta a una persona adulta de confianza; no tiene que enfrentar solo la situación. Si necesita ayuda con una situación de violencia, puede usar el Fono Niños 147.",
    ],
    vocab=[("consentimiento", "autorización libre para usar la imagen o los datos de una persona"), ("datos personales", "información privada como dirección o teléfono"), ("derechos de autor", "protección de una obra creada por alguien"), ("captura", "imagen de pantalla que sirve de evidencia"), ("bloquear", "impedir que una cuenta siga enviando mensajes")],
    worked=[
        ("Aplicar el consentimiento", "En el caso 1, ¿qué corresponde hacer con la foto?", ["Una de las estudiantes dijo que no quiere salir.", "No se publica esa foto; se elige otra donde no aparezca o se recorta con su permiso."], "No publicar la foto con ella"),
        ("Actuar ante un comentario ofensivo", "En el caso 3, ¿qué se hace?", ["No se responde con agresión.", "Se guarda una captura, se oculta o bloquea y se avisa a una persona adulta del colegio."], "Guardar captura, ocultar o bloquear y avisar a una persona adulta"),
    ],
    mistakes=[("Publicar la foto «porque salió bien» aunque alguien dijo que no.", "El consentimiento es de la persona y no del grupo.", "Elige otra imagen o pide permiso."),
              ("Borrar el comentario ofensivo sin guardar evidencia.", "Se pierde la prueba para que una persona adulta pueda actuar.", "Guarda captura, luego oculta o bloquea y avisa.")],
    T=[
        ('abc', '¿Qué es el consentimiento para usar una imagen?', 'La autorización libre de la persona que aparece', 'La decisión del grupo, aunque alguien diga que no', 'La autorización de quien tomó la foto', 'Es la persona que aparece quien autoriza el uso.'),
        ('abc', '{F} En el caso 1, ¿cuántas estudiantes aparecen en la foto?', '5', '4', '6', 'La ficha indica que en la foto aparecen 5 estudiantes.'),
        ('abc', '{F} En el caso 1, ¿qué corresponde?', 'No publicar la foto con quien no quiere salir', 'Publicarla, porque la mayoría quiere', 'Publicarla con un emoji tapando su cara sin avisarle', 'El no de una persona se respeta.'),
        ('abc', '{F} En el caso 2, ¿cuál es una alternativa válida?', 'Usar música creada por el grupo o con autorización', 'Usar la canción igual, porque es para un colegio', 'Reducir el volumen para que no se note', 'Las obras tienen derechos de autor.'),
        ('abc', '{F} En el caso 3, ¿qué se hace primero?', 'Guardar captura y avisar a una persona adulta del colegio', 'Responder con otra burla, para que la persona sepa qué se siente', 'Borrar todo el hilo de comentarios para que nadie más lo lea', 'La captura es evidencia y ayuda a actuar.'),
        ('abc', '{F} En el caso 4, ¿por qué no se debe incluir la dirección de la casa?', 'Porque es un dato personal que expone a la persona', 'Porque ocupa mucho espacio en el afiche y distrae del mensaje principal', 'Porque a nadie le interesa saber dónde vive una integrante del colectivo', 'Los datos personales no se publican.'),
        ('=', '{F} Una foto aparece en 3 grupos de mensajería de 30 personas cada uno, sin que nadie se repita. ¿A cuántas personas llegó?', '3*30', 'Se multiplican los grupos por sus integrantes.', ' personas'),
        ('abc', 'Una estudiante de 17 años quiere salir en el video. ¿Qué se necesita según la clase?', 'Su autorización y también la de su madre, padre o apoderado, según las reglas del colegio', 'Solo la del grupo, porque todas las personas del equipo ya están de acuerdo', 'Ninguna, porque la persona tiene 17 años y puede decidir sola', 'Para menores de 18 se pide además la autorización del adulto.'),
        ('abc', 'Alguien te envía una imagen íntima de otra persona. ¿Qué corresponde?', 'No reenviarla ni comentarla y avisar de inmediato a una persona adulta de confianza', 'Reenviarla a quien la pida, para que se vea que no es una broma', 'Publicarla para advertir a otras personas de lo que está circulando', 'Las imágenes íntimas nunca se comparten ni se difunden, y se avisa a una persona adulta.'),
        ('abc', 'Un integrante recibe mensajes amenazantes por la muestra. ¿Qué corresponde?', 'No responder, guardar capturas, bloquear y contarlo a una persona adulta de confianza', 'Responder con más fuerza para que la persona deje de enviar mensajes', 'Callarlo para no arruinar la muestra y evitar que el equipo se preocupe', 'Nadie debe enfrentar solo una amenaza.'),
        ('=', 'La muestra se difunde en 4 publicaciones y cada una tiene 25 comentarios, de los que 3 son ofensivos. ¿Cuántos comentarios ofensivos hay en total?', '4*3', 'Se multiplican las publicaciones por los comentarios ofensivos de cada una.', ' comentarios'),
        ('abc', 'Un equipo quiere un video con una canción de un artista famoso. ¿Qué plan es más adecuado?', 'Crear una música con percusión corporal del grupo', 'Subirlo con la canción y esperar que nadie reclame', 'Cambiar la velocidad de la canción', 'La música propia evita problemas de derechos.'),
        ('abc', 'Antes de publicar un afiche digital, ¿qué lista de revisión conviene?', 'Consentimientos, datos personales, derechos de música e imágenes y respeto', 'Colores, tamaño de la letra y cantidad de fotos que lleva la publicación', 'Cantidad de likes esperados y número de seguidores del colegio', 'La revisión previa evita daños a las personas.'),
    ],
    ctx=('abc', 'Un equipo prepara una publicación con foto del ensayo, música comercial y el teléfono de una integrante. ¿Qué cambios mínimos necesita?', 'Pedir consentimiento para la foto, usar música propia y quitar el teléfono', 'Cambiar solo el color del afiche', 'Subir la publicación y corregir después si alguien reclama', 'Se corrigen consentimiento, música y datos antes de publicar.'),
    sc=[
        ("En Danza: ¿qué se hace antes de publicar una foto de una persona?", "Se pide su consentimiento", "Sin consentimiento de la persona no se publica su imagen."),
        ("¿Qué se hace ante un comentario ofensivo?", "Guardar captura, ocultar o bloquear y avisar a una persona adulta", "Se protege a la persona que fue ofendida."),
        ("¿Se publican datos personales?", "No", "Esos datos son información privada de las personas."),
    ],
    op=("Para la difusión digital de una muestra ficticia, escribe una lista de revisión de 5 puntos (consentimiento, datos personales, música, comentarios ofensivos, imágenes íntimas) con la acción que corresponde en cada caso.",
        "1) Consentimiento: pedir autorización por escrito y de apoderado si hay menores de 18. 2) Datos personales: no publicar teléfonos ni direcciones. 3) Música: usar música propia. 4) Comentarios ofensivos: capturar, ocultar y avisar a una persona adulta. 5) Imágenes íntimas: no compartir y avisar.",
        ["cinco puntos con acción", "protege a las personas", "avisa a una persona adulta"],
        ["hoja con lista de revisión"],
        ["publicar sin consentimiento", "responder con agresión"],
        "Pregunta: «¿qué haces si alguien dijo que no?». Si no respeta el no, pídele revisar."),
    reinforce="Escribe tres reglas para publicar fotos de un ensayo de danza.",
    extend="Explica por qué guardar una captura ayuda a proteger a una persona agredida en línea.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (balance de ejemplo, inventado). Meta: 60 asistentes. Asistieron 48. "
     "Medios y respuesta (datos de ejemplo): afiche en el hall: 12 personas dijeron que vinieron por él; mensajería del curso: 25 personas; radio escolar: 6 personas; programa de mano: se entregaron 48 y quedaron 22 sin repartir. "
     "Trabajo en equipo: 3 de las 4 tareas de difusión se entregaron a tiempo; la tarea de registro llegó tarde porque no se asignaron responsables claros.")
build(
    O6, 5, F,
    use="Aprenderé a evaluar la difusión de un proyecto con indicadores y a revisar el trabajo colaborativo para decidir qué conservar, qué cambiar y cómo mejorar la próxima vez.",
    prior=["Sé planificar objetivos con cifras.", "Sé usar una bitácora.", "Sé dar retroalimentación respetuosa."],
    explain=[
        "Evaluar la difusión es comparar lo que se logró con lo que se planificó. Un indicador es un dato que permite medir: asistentes, personas que llegaron por cada medio, programas entregados, comentarios recibidos. Se compara con la meta (60 asistentes) y se calcula la diferencia: si asistieron 48, faltaron 12. El logro también se puede expresar como porcentaje de la meta: se divide lo logrado entre la meta y se multiplica por 100 (48 ÷ 60 × 100 = 80 %). También se analiza qué medio funcionó más (la mensajería del curso, con 25 personas) y cuál menos.",
        "Después se interpretan las causas con prudencia: ¿llegó poca gente porque el mensaje no era claro, porque se difundió tarde o porque coincidía con otra actividad? Se buscan hechos y no culpables. Además se evalúa el trabajo colaborativo: si se cumplieron los roles y los plazos, cómo se tomaron las decisiones y cómo se cuidó el respeto en el equipo.",
        "Una buena evaluación termina con acciones: qué conservar, qué cambiar y quién lo hará. Los datos del ejemplo son ficticios, y los datos reales se registran con cuidado, sin publicar información personal de quienes asistieron.",
    ],
    vocab=[("indicador", "dato que permite medir un resultado"), ("meta", "resultado que se esperaba lograr"), ("balance", "comparación entre lo planificado y lo logrado"), ("causa", "razón posible de un resultado"), ("conservar", "mantener lo que funcionó")],
    worked=[
        ("Comparar con la meta", "¿Cuántas personas faltaron para llegar a la meta?", ["La meta era 60 y asistieron 48.", "60 − 48 = 12 personas."], "12 personas"),
        ("Identificar el medio más efectivo", "¿Qué medio trajo más gente según la ficha?", ["Afiche: 12, mensajería: 25, radio: 6.", "El mayor es 25, de mensajería."], "La mensajería del curso"),
    ],
    mistakes=[("Culpar a una persona de que no llegó público.", "Pueden existir muchas causas y no se mejora con culpas.", "Analiza hechos y decisiones del equipo."),
              ("Medir solo cuánta gente asistió.", "No se sabe qué medio funcionó ni qué mejorar.", "Registra también el medio por el que se enteró cada persona.")],
    T=[
        ('abc', '¿Qué es un indicador?', 'Un dato que permite medir un resultado', 'Una opinión del equipo sobre la obra', 'El nombre de la muestra, que sirve para identificarla', 'Un indicador es un dato medible.'),
        ('=', '{F} ¿Cuántas personas faltaron para llegar a la meta?', '60-48', 'Se resta lo logrado de la meta.', ' personas'),
        ('abc', '{F} ¿Qué medio trajo más personas?', 'La mensajería del curso', 'El afiche en el hall', 'La radio escolar', 'Con 25 personas fue el que más trajo.'),
        ('=', '{F} ¿Cuántas personas en total declararon haber venido por afiche, mensajería o radio?', '12+25+6', 'Se suman las respuestas de los tres medios.', ' personas'),
        ('=', '{F} ¿Cuántos programas de mano se imprimieron si se entregaron 48 y quedaron 22?', '48+22', 'Se suman los entregados y los que quedaron.', ' programas'),
        ('abc', '{F} ¿Qué conviene concluir sobre la radio escolar?', 'Trajo pocas personas, así que conviene evaluar si vale el esfuerzo', 'Falló, así que debe eliminarse siempre de la difusión del colectivo', 'Funcionó mejor que la mensajería, porque llegó a más personas del colegio', 'Con 6 personas fue el medio con menos efecto.'),
        ('abc', '{F} ¿Cuál es una causa posible de que tarde la tarea de registro?', 'No se asignaron responsables claros', 'Una persona no quiso colaborar', 'El proyecto era imposible', 'La ficha lo explica: no se asignaron responsables claros.'),
        ('abc', '{F} Un integrante dice «llegó poca gente por culpa de una persona del equipo». ¿Qué respondes?', 'Mejor revisar los hechos y las decisiones del equipo, no buscar culpables', 'Estás de acuerdo porque alguien tiene que ser responsable', 'Que esa persona pida disculpas ante todos, porque la tarea de registro era suya', 'Se evalúan decisiones y no personas.'),
        ('=', '{F} Si asistieron 48 y la meta era 60, ¿qué porcentaje de la meta se logró?', '48*100//60', 'Se divide lo logrado entre la meta y se multiplica por 100.', ' %'),
        ('abc', 'Para mejorar la próxima vez, ¿qué conviene?', 'Conservar lo que funcionó, como la mensajería, y cambiar lo que falló', 'Repetir todo igual en la próxima muestra para mantener el mismo estilo', 'Cancelar el proyecto, porque no se llegó a la meta de asistentes', 'La evaluación orienta acciones para la próxima vez.'),
        ('abc', 'Un equipo pregunta a cada asistente cómo se enteró de la muestra. ¿Para qué?', 'Para saber qué medio funcionó mejor, sin pedir datos personales', 'Para publicar quiénes asistieron y agradecerles públicamente', 'Para premiar a las personas que más veces vinieron a las funciones', 'Se mide el medio, no a las personas.'),
        ('=', 'Una próxima muestra tendrá una meta de 80 personas y asistirán 72. ¿Cuántas personas faltarán?', '80-72', 'Se resta lo logrado de la meta.', ' personas'),
        ('abc', 'En el equipo, una persona sintió presión para aceptar más tareas de las acordadas. ¿Qué corresponde?', 'Hablar con el equipo, revisar el reparto y avisar a una persona adulta si no se resuelve', 'Aceptar las tareas extra para evitar conflictos con el resto del equipo', 'Dejar el equipo sin avisar para no generar una discusión mayor', 'Los acuerdos de trabajo se cuidan.'),
    ],
    ctx=('abc', 'Con los datos de la ficha, el equipo redacta: «Conservaremos la mensajería, pondremos el afiche más cerca de la entrada, asignaremos dos responsables al registro y fijaremos la fecha 2 semanas antes». ¿Qué tiene de valioso?', 'Conserva lo que funcionó, cambia lo débil y asigna responsables', 'Solo repite lo que se hizo, porque no cambia nada de la difusión', 'Culpa a una persona del equipo por los resultados y por los plazos no cumplidos', 'Tiene acciones concretas basadas en los datos.'),
    sc=[
        ("En Danza: ¿qué es un balance?", "Una comparación entre lo planificado y lo logrado", "El balance sirve para decidir mejoras concretas."),
        ("¿Se buscan culpables en una evaluación?", "No, se analizan hechos y decisiones", "Se mejora analizando hechos y no buscando culpables."),
        ("¿Qué se hace con los datos de las personas que asistieron?", "Se cuidan y no se publican", "Los datos de quienes asisten son información privada."),
    ],
    op=("Con una muestra ficticia (meta 50, asistieron 41), escribe un balance con: diferencia respecto de la meta, el medio más efectivo (con datos que inventes), una causa posible y dos acciones de mejora con responsables.",
        "Meta 50, asistieron 41: faltaron 9. Medio más efectivo: mensajería, 20 personas. Causa posible: el aviso salió una semana antes. Acciones: avisar dos semanas antes (Ana) y poner afiches más visibles (Luis).",
        ["calcula la diferencia", "identifica el medio más efectivo", "propone acciones con responsables"],
        ["hoja con balance"],
        ["culpar a personas", "no proponer acciones"],
        "Pregunta: «¿qué conservarías y qué cambiarías?». Si responde «todo», pídele elegir."),
    reinforce="Calcula la diferencia entre una meta de 40 y una asistencia de 33, y propone una acción de mejora.",
    extend="Explica por qué evaluar el trabajo colaborativo es tan importante como contar asistentes.",
)
