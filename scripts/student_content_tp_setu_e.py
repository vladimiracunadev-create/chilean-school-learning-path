"""Servicios de Turismo TP 3.º y 4.º medio: OAE-05 (manejar situaciones imprevistas). SOLO conceptos y avisos; sin procedimientos clínicos ni operativos; casos ficticios en papel."""
from __future__ import annotations

from tp_setu_common import build

O5 = "TP-SETU-3y4-OAE-05"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (de ejemplo, inventada). El prestador «Rutas de Villa Brisa» tiene un plan de contingencia (conjunto de pasos acordados ante un imprevisto) con cinco tipos de situación: pérdida o robo de objetos; extravío de una persona; enfermedad; accidente; y descontrol de conducta de una persona. "
     "Principios del plan: primero la seguridad de las personas, mantener la calma, avisar al coordinador y a los servicios de emergencia cuando corresponda, registrar lo ocurrido y proteger los datos de los involucrados. "
     "El guía no es médico ni policía. Grupo del día: 25 personas inscritas.")
build(
    O5, 1, F,
    use="Aprenderé qué es un imprevisto y un plan de contingencia, los principios para reaccionar (seguridad, calma, aviso, registro y privacidad) y por qué el guía no hace diagnósticos ni persigue a nadie.",
    prior=["Sé que cada persona merece respeto.", "Sé que los datos personales son privados.", "Sé restar horas y minutos."],
    explain=[
        "Un imprevisto es un hecho inesperado que altera el programa y exige reaccionar: la pérdida o el robo de objetos, el extravío de una persona, una enfermedad, un accidente o el descontrol de conducta de alguien. El prestador prepara un plan de contingencia, que son los pasos acordados para cada caso. Sus principios son: primero la seguridad de las personas, mantener la calma, avisar al coordinador y a los servicios de emergencia cuando corresponda, registrar lo ocurrido y proteger los datos.",
        "El guía no es médico ni policía. No diagnostica, no da medicamentos y no persigue a nadie: acompaña a la persona, protege al resto del grupo y avisa a quien corresponde. El estado de salud es un dato sensible, es decir, un dato personal muy privado que se comparte solo con quien necesita saberlo para ayudar. Todo esto se hace con trato respetuoso, sin culpar a la persona afectada.",
        "Vivir un imprevisto puede dejar tensión. El equipo se cuida conversando con el coordinador o con una persona de confianza. Este cuaderno es aprendizaje conceptual en papel: manejar emergencias reales exige formación, instructor autorizado y norma vigente; no te habilita para trabajar.",
    ],
    vocab=[("imprevisto", "hecho inesperado que altera el programa y exige reaccionar"), ("plan de contingencia", "pasos acordados que se siguen ante un imprevisto"), ("servicios de emergencia", "instituciones que atienden urgencias de salud o seguridad"), ("dato sensible", "dato personal muy privado, como el estado de salud"), ("registro del incidente", "documento donde se anota lo ocurrido con hechos objetivos")],
    worked=[
        ("Clasificar el imprevisto", "Una turista de ejemplo dice que no encuentra su teléfono y cree que se lo sacaron en la feria. ¿Qué tipo de situación es?", ["Se trata de un objeto personal perdido o robado.", "Corresponde a pérdida o robo de objetos."], "Pérdida o robo de objetos"),
        ("Cuánto tardó el aviso", "Un turista de ejemplo se siente mal a las 10:10 y el guía avisa al coordinador a las 10:14. ¿Cuántos minutos pasaron?", ["Se restan los minutos: 14 − 10 = 4.", "Fueron 4 minutos."], "4 minutos"),
    ],
    mistakes=[("Decirle a un turista qué enfermedad tiene.", "El guía no es médico y un diagnóstico equivocado puede causar daño.", "Acompaña a la persona y avisa a los servicios de emergencia."),
              ("Contar al grupo la enfermedad de una persona para pedir comprensión.", "El estado de salud es un dato sensible y su dueño no autorizó contarlo.", "Comparte solo lo necesario con quienes deben ayudar.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un imprevisto?", "Un hecho inesperado que altera el programa y exige reaccionar", "Una actividad que se planifica con anticipación", "Un cambio de precio del programa", "Un imprevisto es inesperado; lo planificado o un cambio de precio no lo son."),
        ("abc", "En Servicios de Turismo: ¿qué es un plan de contingencia?", "Los pasos acordados que se siguen ante un imprevisto", "La lista de precios del programa", "El mapa del recorrido", "El plan de contingencia ordena cómo actuar cuando algo imprevisto ocurre."),
        ("abc", "En Servicios de Turismo: ¿qué es un dato sensible, como el estado de salud de un turista?", "Un dato personal muy privado, que se comparte solo con quien necesita saberlo para ayudar", "Un dato que puede contarse al grupo para pedir comprensión", "Un dato que el guía puede publicar en redes", "Los datos de salud son muy privados y su difusión requiere autorización."),
        ("abc", "{F} ¿Qué prioriza el plan ante cualquier imprevisto?", "La seguridad de las personas", "Cumplir el horario del programa", "Proteger la imagen del prestador", "El plan pone primero la seguridad; el horario y la imagen vienen después."),
        ("abc", "{F} Un turista resbala y se queja de dolor. ¿A qué tipo de situación del plan corresponde?", "Accidente", "Pérdida o robo de objetos", "Descontrol de conducta", "Una caída con dolor es un accidente."),
        ("abc", "{F} Una turista dice sentirse mareada. ¿Qué corresponde al guía?", "Acompañarla, mantener la calma y avisar al coordinador y a los servicios de emergencia si corresponde, sin diagnosticar ni dar medicamentos", "Decirle qué enfermedad tiene y darle algo del botiquín", "Pedirle que siga caminando para no atrasar al grupo", "El guía acompaña y avisa, pero no es médico para diagnosticar ni medicar."),
        ("=", "{F} Se avisa al coordinador a las 14:05 y él llega a las 14:30. ¿Cuántos minutos pasaron?", "(14*60+30)-(14*60+5)", "Se restan los minutos entre ambas horas.", " minutos"),
        ("abc", "{F} Un turista le cuenta al guía que tiene una enfermedad crónica y otro curioso le pregunta qué le pasa. ¿Qué corresponde?", "No contarlo, porque es un dato sensible, y compartirlo solo con quien deba ayudar si hace falta", "Contarlo, para que el grupo lo trate con cuidado", "Contarlo si el curioso promete guardar el secreto", "La salud es un dato sensible y solo su dueño decide a quién contarlo."),
        ("abc", "{F} Después de un imprevisto, el guía se siente muy angustiado. ¿Qué corresponde?", "Conversar con el coordinador o una persona de confianza y pedir apoyo", "Guardárselo para no preocupar al equipo", "Dejar el trabajo sin avisar", "Pedir apoyo cuida al guía y al equipo; ocultarlo o irse sin avisar no ayuda."),
        ("=", "{F} Tras un imprevisto se cuenta al grupo: 22 personas están presentes y 1 está acompañada por el coordinador. ¿Cuántas personas faltan por ubicar?", "25-22-1", "Se restan las presentes y la acompañada de las 25 inscritas.", " personas"),
        ("abc", "{F} Un turista exige que el guía persiga a quien le sacó la mochila. ¿Qué corresponde?", "Explicar que no se persigue a nadie por la seguridad de todos y ayudarle a avisar a la autoridad competente", "Perseguir al sospechoso mientras el grupo espera", "Decirle que no es problema del guía", "Perseguir expone al guía y al grupo; se ayuda a avisar a la autoridad."),
        ("abc", "{F} Un turista pide al guía que no registre el imprevisto «para no tener problemas». ¿Qué corresponde?", "Registrarlo igual, con hechos objetivos, y proteger los datos de los involucrados", "No registrarlo, para que nadie se moleste", "Registrarlo con la opinión del guía sobre quién tuvo la culpa", "El registro es parte del plan; se hace sin culpar y cuidando los datos."),
        ("abc", "{F} Un turista parece desorientado y dice cosas confusas. ¿Qué corresponde?", "Mantener la calma, acompañarlo, avisar al coordinador y a los servicios de emergencia, sin diagnosticarlo", "Pedirle que se calme y seguir el programa", "Suponer la causa y comentarla en voz alta", "No se supone la causa ni se espera: se acompaña y se avisa a quien puede ayudar."),
    ],
    ctx=("abc", "{F} Un integrante dice que su amigo del grupo se enfermó y le pide al guía que no avise a nadie. ¿Qué corresponde?", "Avisar al coordinador y a los servicios de emergencia si corresponde, aunque se lo hayan pedido", "No avisar, para respetar el pedido del amigo", "Anunciar al grupo lo que le pasa para ayudar", "La seguridad de la persona va primero; el aviso se hace a quien puede ayudar, sin difundir sus datos."),
    sc=[
        ("En Servicios de Turismo: ¿qué prioriza un plan de contingencia?", "La seguridad de las personas", "Todo el resto del plan se ordena después de ella."),
        ("¿Puede el guía diagnosticar o medicar?", "No, porque no es médico", "Acompaña y avisa a los servicios de emergencia."),
        ("¿Quién puede conocer el estado de salud de un turista?", "Solo quienes necesitan saberlo para ayudar", "Es un dato sensible que su dueño debe autorizar."),
    ],
    op=("Escribe un resumen de plan de contingencia de cinco líneas para la pérdida de un objeto personal de un turista (por ejemplo, un teléfono), con una línea para cada principio: seguridad, calma, aviso, registro y datos. Usa solo conceptos generales.",
        "Seguridad: mantener al turista y al grupo en un lugar seguro. Calma: hablarle con voz tranquila y sin culparlo. Aviso: informar al coordinador y, si corresponde, ayudarle a avisar a la autoridad competente. Registro: anotar hora, lugar y hechos sin opiniones. Datos: no publicar sus datos ni el detalle de sus pertenencias.",
        ["incluye las cinco líneas con los cinco principios", "usa solo conceptos generales", "no culpa al turista"],
        ["resumen de cinco líneas"],
        ["culpar al turista", "olvidar el registro o los datos", "dar pasos de una actividad peligrosa"],
        "Pregunta: «¿por qué la seguridad va primero?». Si no responde, repasa los principios del plan."),
    reinforce="Anota un imprevisto que haya ocurrido en un paseo que conozcas y qué principio del plan se habría aplicado.",
    extend="Explica con un ejemplo inventado por qué el guía no debe dar medicamentos aunque tenga un botiquín.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (de ejemplo, inventada). Formulario de registro de incidente del prestador, con los campos: fecha y hora; lugar; personas involucradas (solo iniciales); descripción de los hechos; acciones realizadas; a quién se avisó y a qué hora; resultado. "
     "Ejemplo anotado: «Jueves 15:10, mirador. La turista M. P. informa que no encuentra su cámara. El guía revisa con ella el recorrido del día y no aparece. Se avisa al coordinador a las 15:20. Se le entrega una constancia interna y se le indica que puede hacer la denuncia ante la autoridad competente». "
     "Roles: guía, coordinador, servicios de emergencia, autoridad competente (la policía), consulado (para turistas extranjeros) y seguro de viaje.")
build(
    O5, 2, F,
    use="Aprenderé los documentos y roles ante un imprevisto (registro, constancia, denuncia, seguro, consulado) y frases breves en inglés para ayudar y tranquilizar.",
    prior=["Sé qué es un plan de contingencia.", "Sé qué es un dato sensible.", "Sé que el guía no es médico ni policía."],
    explain=[
        "Ante un imprevisto se usan varios documentos. El registro de incidente anota fecha, hora, lugar, personas (solo iniciales), hechos, acciones y avisos. Los hechos se escriben de forma objetiva, sin opiniones ni culpas: «la turista informó que no encuentra su cámara», y no «la turista estaba distraída». La constancia es un papel interno que acredita lo informado. La denuncia es el aviso formal que la propia persona hace ante la autoridad competente. El seguro de viaje es un contrato que puede cubrir pérdidas, según sus condiciones.",
        "Cada rol tiene su función: el guía acompaña, protege al grupo y avisa; el coordinador decide y apoya; los servicios de emergencia atienden urgencias de salud o seguridad; la autoridad competente recibe denuncias; y el consulado es la oficina del país de un turista extranjero que lo orienta, por ejemplo, si pierde su pasaporte. El guía informa a quién acudir, pero no reemplaza a ninguno.",
        "En inglés, tres frases útiles son «Are you OK?» (¿Está bien?), «I will call for help» (Voy a pedir ayuda) y «Please stay here with me» (Por favor, quédese aquí conmigo). Se dicen con calma y se acompañan con gestos tranquilos.",
    ],
    vocab=[("registro de incidente", "documento con los hechos, acciones y avisos de un imprevisto"), ("constancia", "papel interno que acredita lo que la persona informó"), ("denuncia", "aviso formal que hace la persona afectada ante la autoridad competente"), ("seguro de viaje", "contrato que puede cubrir pérdidas según sus condiciones"), ("consulado", "oficina del país de un turista extranjero que lo orienta"), ("hecho objetivo", "dato que se puede comprobar, sin opinión")],
    worked=[
        ("Hecho u opinión", "En un registro de ejemplo se anotó: «el turista fue descuidado». ¿Es un hecho objetivo?", ["Es un juicio sobre la persona.", "Un hecho objetivo sería: «el turista informó que no encuentra su billetera»."], "No: es una opinión y debe reemplazarse"),
        ("Tiempo de aviso", "Un guía de ejemplo se entera a las 9:40 y avisa al coordinador a las 9:46. ¿Cuántos minutos tardó?", ["Se restan los minutos: 46 − 40 = 6.", "Tardó 6 minutos."], "6 minutos"),
    ],
    mistakes=[("Escribir en el registro el nombre completo y el pasaporte del turista.", "Se exponen datos personales que no son necesarios en el registro.", "Usa solo las iniciales y los datos mínimos."),
              ("Decir al turista «yo hago la denuncia por usted».", "La denuncia la hace la persona afectada ante la autoridad competente.", "Acompáñalo e indícale a dónde acudir.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es una denuncia?", "El aviso formal que hace la persona afectada ante la autoridad competente", "Un papel interno que acredita lo informado", "El mapa del recorrido", "La denuncia la hace quien sufrió el hecho ante la autoridad."),
        ("abc", "En Servicios de Turismo: ¿qué es una constancia?", "Un papel interno que acredita lo que la persona informó", "Un permiso de la policía", "Un contrato de seguro", "La constancia es interna del prestador; la denuncia y el seguro son otros documentos."),
        ("abc", "En Servicios de Turismo: ¿qué es un consulado?", "La oficina del país de un turista extranjero que lo orienta, por ejemplo si pierde su pasaporte", "Un servicio de emergencia médica", "Una oficina del prestador turístico", "El consulado representa a un país en otro y orienta a sus ciudadanos."),
        ("abc", "{F} ¿Cuál es un hecho objetivo para el registro?", "La turista informó que no encuentra su cámara", "La turista estaba distraída", "La turista es descuidada", "Un hecho objetivo se puede comprobar; las otras son opiniones."),
        ("=", "{F} El incidente ocurre a las 15:10 y se avisa al coordinador a las 15:20. ¿Cuántos minutos pasaron?", "(15*60+20)-(15*60+10)", "Se restan los minutos entre ambas horas.", " minutos"),
        ("abc", "{F} ¿Por qué el formulario pide solo las iniciales de las personas?", "Para proteger sus datos personales", "Para ahorrar espacio", "Porque los nombres no importan", "Las iniciales reducen la exposición de datos personales en el registro."),
        ("abc", "{F} En el ejemplo, ¿quién hace la denuncia?", "La turista, ante la autoridad competente", "El guía, en nombre de ella", "El coordinador, sin avisarle", "La denuncia la hace la persona afectada; el guía la acompaña e informa a dónde acudir."),
        ("abc", "{F} Una turista extranjera perdió su pasaporte. ¿A qué oficina se le puede indicar acudir, además de la autoridad competente?", "A su consulado", "A otra agencia de viajes", "Al museo del pueblo", "El consulado orienta a los ciudadanos de su país que pierden documentos."),
        ("ab", "{F} ¿Cuál es el significado de «I will call for help»?", "Voy a pedir ayuda.", "Voy a irme a casa.", "«Call for help» significa pedir ayuda."),
        ("ab", "{F} ¿Cuál frase en inglés pregunta con amabilidad si la persona está bien?", "Are you OK?", "Are you late?", "«OK» indica estar bien, mientras que «late» significa tarde."),
        ("abc", "{F} Un compañero propone anotar en el registro el nombre completo y el pasaporte de la turista «para que quede claro». ¿Qué corresponde?", "Anotar solo las iniciales y los datos mínimos necesarios", "Anotar todo, para no olvidar nada", "No registrar nada", "Los datos personales no necesarios se evitan en los registros."),
        ("abc", "{F} Un periodista local pide el registro del incidente completo. ¿Qué corresponde?", "No entregarlo y derivar la consulta al coordinador o al prestador", "Entregarlo, porque es información pública", "Entregarlo si pide por favor", "El registro tiene datos de terceros; solo el prestador decide qué informar."),
        ("abc", "{F} La turista pregunta qué cubre su seguro de viaje. ¿Qué respondes?", "Que eso depende de las condiciones de su contrato y que debe consultarlo con su aseguradora", "Que cubre todo, sin importar su contrato", "Que los seguros nunca cubren nada", "Solo el contrato define qué cubre; el guía no conoce sus condiciones."),
    ],
    ctx=("abc", "{F} La turista está nerviosa y habla rápido en inglés. ¿Qué haces?", "Hablarle con calma y frases simples, como «Are you OK?» y «I will call for help»", "Hablarle en voz muy alta para que entienda", "Pedirle que vuelva cuando esté tranquila", "La calma y las frases breves tranquilizan; gritar o pedir que vuelva empeora la situación."),
    sc=[
        ("En Servicios de Turismo: ¿qué es un hecho objetivo?", "Un dato que se puede comprobar, sin opinión", "El registro debe contener hechos y no juicios."),
        ("¿Quién hace la denuncia?", "La persona afectada, ante la autoridad competente", "El guía la acompaña e informa a dónde acudir."),
        ("¿Qué datos se anotan de las personas en el registro?", "Solo las iniciales y los datos mínimos", "Así se protege la privacidad de las personas del registro."),
    ],
    op=("Completa un formulario de registro de incidente de ejemplo con estos hechos: un turista de iniciales J. R. dice a las 12:05, en la plaza, que le sacaron su billetera; el guía le ofrece agua y lo acompaña a un lugar tranquilo; a las 12:12 avisa al coordinador; se le indica que puede hacer la denuncia ante la autoridad competente. Escribe los siete campos con hechos objetivos y calcula cuántos minutos tardó el aviso.",
        "Fecha y hora: 12:05. Lugar: plaza. Personas: J. R. Hechos: el turista informó que le sacaron su billetera. Acciones: se le ofreció agua y se lo acompañó a un lugar tranquilo; se le indicó que puede hacer la denuncia ante la autoridad competente. Avisos: coordinador a las 12:12. Resultado: pendiente de denuncia. Tardó 7 minutos en avisar.",
        ["completa los siete campos", "los hechos son objetivos y sin opiniones", "calcula bien el tiempo del aviso"],
        ["formulario completado y cálculo del tiempo"],
        ["escribir el nombre completo", "anotar opiniones como «descuidado»", "olvidar la hora del aviso"],
        "Pregunta: «¿por qué solo escribiste las iniciales?». Si no responde, repasa la protección de datos."),
    reinforce="Escribe tres frases objetivas y tres opiniones sobre un mismo hecho inventado, y márcalas.",
    extend="Explica con un ejemplo inventado por qué una constancia interna no reemplaza una denuncia.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (de ejemplo, inventada). En la feria artesanal, parada de un programa de 20 personas con dos guías, la turista extranjera Ann (nombre de ejemplo) avisa a las 11:30 que a las 11:20 le robaron su mochila. "
     "Contenía su pasaporte, un teléfono (valor declarado $150.000), una cámara ($120.000) y un monedero con $30.000 en efectivo. Ann habla inglés básico y está muy alterada. "
     "Su seguro de viaje de ejemplo cubre el valor declarado del teléfono y la cámara, menos un deducible de ejemplo de $50.000; no cubre dinero en efectivo. El programa continúa 2 horas más.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de pérdida o robo: proteger a la persona y al grupo, calmar y comunicar en inglés básico, avisar a quien corresponde, registrar y calcular lo que cubre un seguro de ejemplo.",
    prior=["Sé qué son el registro, la constancia, la denuncia y el consulado.", "Sé restar horas y minutos.", "Sé que el guía no persigue a nadie."],
    explain=[
        "En un caso de robo o pérdida, el orden del plan es: primero, la seguridad de la persona y del grupo; segundo, calmar a la persona con un trato respetuoso, sin culparla; tercero, avisar al coordinador; cuarto, acompañarla para que, si lo desea, haga la denuncia ante la autoridad competente y, si perdió el pasaporte, contacte a su consulado; quinto, registrar el incidente con hechos objetivos y datos mínimos. El guía no busca al ladrón, no acusa a nadie y no revisa pertenencias de otros.",
        "El resto del grupo no se descuida: mientras un guía acompaña a la persona, el otro mantiene al grupo reunido en un lugar seguro y, con ayuda del coordinador, decide cómo continuar el programa. La cobertura de un seguro depende de su contrato: aquí, el seguro de ejemplo paga el valor declarado de ciertos objetos menos un deducible, que es una parte que paga el asegurado.",
        "En inglés, se pueden usar frases breves: «I am sorry. I will help you», «Please stay with me» y «Your embassy or consulate can help with your passport». Los documentos de las personas no se fotografían ni se comparten en chats del grupo.",
    ],
    vocab=[("valor declarado", "valor que el asegurado informó para un objeto asegurado"), ("deducible", "parte del daño que paga el asegurado"), ("cobertura", "lo que un seguro paga según su contrato"), ("seguridad del grupo", "cuidado del resto de las personas mientras se atiende un imprevisto"), ("lugar seguro", "sitio donde el grupo espera sin riesgo, definido por el guía y el coordinador")],
    worked=[
        ("Valor total", "Una mochila de ejemplo contenía un teléfono de $90.000 y una cámara de $60.000. ¿Cuál es el valor total de ambos?", ["Se suman los valores declarados.", "90.000 + 60.000 = 150.000."], "$150.000"),
        ("Cobertura con deducible", "Un seguro de ejemplo cubre el valor declarado menos un deducible de $20.000. El valor declarado es $150.000. ¿Cuánto paga el seguro?", ["Se resta el deducible al valor declarado.", "150.000 − 20.000 = 130.000."], "$130.000"),
    ],
    mistakes=[("Decirle a la turista «te lo advertí, no se deja la mochila suelta».", "Culpar a la persona la altera más y no ayuda a resolver.", "Habla con calma y acompáñala sin juzgar."),
              ("Revisar las mochilas de otros turistas del grupo para buscar la robada.", "Es una acusación sin pruebas y excede el rol del guía.", "Avisa al coordinador y a la autoridad competente.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un deducible en un seguro?", "La parte del daño que paga el asegurado", "El total que paga el seguro", "El dinero que cobra el guía", "El deducible lo paga el asegurado y se resta de lo que cubre el seguro."),
        ("abc", "¿Qué se hace primero ante un robo durante un programa?", "Proteger a la persona y al grupo y mantener la calma", "Perseguir al ladrón", "Buscar a quién culpar entre los turistas", "La seguridad va primero; perseguir o acusar agrava el riesgo."),
        ("abc", "¿Quién acude a la autoridad competente a hacer la denuncia?", "La persona afectada, con el acompañamiento del guía", "El guía en su reemplazo", "Cualquier turista del grupo", "La denuncia la hace quien sufrió el robo; el guía acompaña e informa."),
        ("=", "{F} ¿Cuántos minutos pasaron entre el robo y el aviso de Ann al guía?", "(11*60+30)-(11*60+20)", "Se restan los minutos entre ambas horas.", " minutos"),
        ("=", "{F} ¿Cuántos pesos suman el teléfono, la cámara y el efectivo?", "150000+120000+30000", "Se suman los tres valores de la mochila.", ""),
        ("=", "{F} ¿Cuántos pesos paga el seguro de ejemplo por el teléfono y la cámara?", "(150000+120000)-50000", "Se suman los dos objetos cubiertos y se resta el deducible.", ""),
        ("=", "{F} ¿Cuántos pesos de lo perdido no recupera Ann por el seguro?", "(150000+120000+30000)-((150000+120000)-50000)", "Se resta lo que paga el seguro al valor total perdido.", ""),
        ("abc", "{F} ¿Qué hace el segundo guía mientras el primero acompaña a Ann?", "Mantiene al resto del grupo reunido en un lugar seguro", "Se une a la búsqueda del ladrón", "Deja al grupo libre hasta que regresen", "El grupo no se descuida mientras se atiende el imprevisto."),
        ("abc", "{F} Ann dice: «I am afraid. My passport is gone». ¿Qué le indicas respecto de su pasaporte?", "Que su consulado puede orientarla y que puede acudir a la autoridad competente para denunciar", "Que el guía le consiga un pasaporte nuevo", "Que viaje sin pasaporte hasta el final del programa", "El consulado orienta por el pasaporte y la denuncia se hace ante la autoridad."),
        ("ab", "{F} ¿Cuál frase en inglés ofrece ayuda con calma?", "I am sorry. I will help you.", "Hurry up, we are late.", "La primera frase tranquiliza y ofrece ayuda; la segunda apura a la persona."),
        ("abc", "{F} Un turista del grupo opina que «la turista fue descuidada». ¿Qué corresponde?", "Pedirle respetuosamente que no la juzgue y centrarse en ayudarla", "Darle la razón para evitar discusiones", "Anotar su opinión como hecho en el registro", "Culpar a la víctima no ayuda y las opiniones no se registran como hechos."),
        ("abc", "{F} Otro turista pide fotografiar el pasaporte de Ann «para ayudarla con el consulado». ¿Qué corresponde?", "No fotografiarlo ni compartirlo, y dejar que ella decida a quién mostrarlo", "Fotografiarlo y enviarlo al chat del grupo", "Fotografiarlo y guardarlo en el teléfono del guía", "Los documentos son datos personales y no se comparten sin autorización de su dueña."),
        ("abc", "{F} El coordinador pregunta cómo seguir con el programa de 2 horas. ¿Qué corresponde?", "Decidir con él cómo continuar, cuidando que Ann esté acompañada y el grupo seguro", "Continuar sin avisar a Ann", "Suspender el programa sin consultar", "La decisión se toma con el coordinador, protegiendo a la afectada y al grupo."),
    ],
    ctx=("abc", "{F} Un vendedor de la feria se acerca ofendido: dice que lo están acusando del robo. ¿Qué corresponde al guía?", "Mantener la calma, decir que nadie lo acusa y que la denuncia se hará ante la autoridad competente", "Pedirle que le muestre sus bolsillos", "Aceptar la acusación para cerrar el tema", "El guía no acusa ni investiga; la autoridad competente es quien investiga."),
    sc=[
        ("En Servicios de Turismo: ¿qué es un deducible?", "La parte del daño que paga el asegurado", "Se resta de lo que cubre el seguro."),
        ("¿Quién hace la denuncia de un robo?", "La persona afectada, acompañada por el guía", "El guía no reemplaza a la persona."),
        ("¿Qué haces con el resto del grupo?", "Lo mantengo reunido en un lugar seguro", "El imprevisto no debe dejar a otros sin cuidado."),
    ],
    op=("Un turista de ejemplo de nombre Leo (hablante de inglés básico) pierde su teléfono, de $200.000 de valor declarado, durante un programa de 15 personas. Su seguro de ejemplo cubre el valor declarado menos un deducible de $40.000. Escribe: tres acciones del guía en orden, dos frases en inglés para tranquilizarlo, cuánto paga el seguro y cuánto de su teléfono no recupera.",
        "Acciones: 1) Proteger a Leo y al grupo y mantener la calma. 2) Avisar al coordinador. 3) Acompañarlo para que haga la denuncia ante la autoridad competente y registrar el incidente. Frases: «Are you OK?» y «I will help you». El seguro paga 200.000 − 40.000 = 160.000. No recupera 40.000, el deducible.",
        ["ordena tres acciones coherentes con el plan", "incluye dos frases en inglés correctas y tranquilizadoras", "calcula bien lo que paga el seguro y lo que no recupera"],
        ["tres acciones, dos frases y los cálculos"],
        ["culpar a Leo", "olvidar proteger al grupo", "calcular el seguro sumando el deducible"],
        "Pregunta: «¿por qué avisas al coordinador antes de buscar el teléfono?». Si no responde, repasa el orden del plan."),
    reinforce="Anota un objeto tuyo y su valor inventado, y calcula cuánto pagaría un seguro con un deducible de 20.000.",
    extend="Explica con un ejemplo inventado por qué el guía no debe acusar a ninguna persona de un robo.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (de ejemplo, inventada). Grupo de 24 personas con dos guías, G1 y G2, en un mirador. A las 15:00 un turista, T, dice sentirse mal. A las 15:02 G1 avisa al coordinador y a los servicios de emergencia; G1 permanece con T y G2 mantiene al resto del grupo en un lugar seguro. "
     "A las 15:12 llega el coordinador y a las 15:35 llegan los servicios de emergencia. Meta de ejemplo del prestador: el coordinador llega en 15 minutos o menos desde el aviso. "
     "Aviso: este cuaderno no enseña primeros auxilios ni atención médica; eso lo hacen personas formadas y los servicios de emergencia.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar criterios con datos ante una enfermedad, un accidente o el descontrol de conducta de una persona: tiempos de respuesta, reparto del grupo y principios de trato, sin técnicas clínicas.",
    prior=["Sé qué es un plan de contingencia.", "Sé restar horas y minutos.", "Sé que el guía no diagnostica ni medica."],
    explain=[
        "Ante una enfermedad o un accidente, el criterio es: acompañar a la persona, mantener la calma, avisar rápido al coordinador y a los servicios de emergencia, seguir sus indicaciones, y proteger al resto del grupo en un lugar seguro. Se mide el tiempo de respuesta: desde el aviso hasta la llegada del apoyo. Las metas de este cuaderno son de ejemplo. El guía no diagnostica, no da medicamentos y no hace maniobras clínicas: esas tareas son de personas formadas.",
        "Ante el descontrol de conducta de una persona, que puede tener causas muy distintas (estrés, conflicto, cansancio u otras), el guía no supone la causa ni la juzga. Mantiene una distancia segura, habla con voz tranquila, no discute ni confronta, no usa la fuerza y pide apoyo al coordinador. Si hay riesgo para alguien, se avisa a los servicios de emergencia o a la autoridad competente. La seguridad individual y la del grupo van primero.",
        "Todo se registra con hechos objetivos y datos mínimos, y se informa al coordinador. Después, el equipo conversa para cuidarse y revisar qué se puede mejorar, sin culpar a nadie.",
    ],
    vocab=[("tiempo de respuesta", "tiempo entre el aviso y la llegada del apoyo"), ("distancia segura", "espacio que protege a la persona y al guía ante una situación tensa"), ("descontrol de conducta", "comportamiento alterado de una persona, de causa diversa"), ("meta de ejemplo", "valor que el prestador se propone lograr, rotulado de ejemplo"), ("apoyo", "personas que llegan a ayudar, como el coordinador o los servicios de emergencia")],
    worked=[
        ("Tiempo de respuesta", "Un aviso de ejemplo se hace a las 10:05 y el coordinador llega a las 10:18. ¿Cuántos minutos tardó?", ["Se restan los minutos: 18 − 5 = 13.", "Tardó 13 minutos."], "13 minutos"),
        ("Reparto del grupo", "En un grupo de ejemplo de 18 personas, una persona se enferma y es acompañada por un guía. ¿Cuántas personas quedan con el otro guía?", ["Se descuenta a la persona enferma: 18 − 1 = 17.", "El guía acompañante no está en el grupo de 18."], "17 personas"),
    ],
    mistakes=[("Hablar fuerte a una persona alterada para «imponer respeto».", "Eleva la tensión y puede empeorar la situación.", "Mantén la calma, la distancia segura y una voz tranquila."),
              ("Suponer que un turista alterado «seguro tomó algo».", "Suponer la causa es un juicio sin pruebas y puede ser falso y ofensivo.", "Describe lo que observas, sin juzgar, y pide apoyo.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es el tiempo de respuesta?", "El tiempo entre el aviso y la llegada del apoyo", "El tiempo de duración de todo el programa", "El tiempo que dura un almuerzo", "El tiempo de respuesta mide qué tan rápido llega la ayuda tras el aviso."),
        ("abc", "En Servicios de Turismo: ¿qué es una distancia segura?", "El espacio que protege a la persona y al guía ante una situación tensa", "La distancia entre dos paradas del programa", "La distancia que recorre el grupo en un día", "La distancia segura evita contactos que podrían agravar la tensión."),
        ("abc", "El guía, ante una enfermedad, ¿qué no hace?", "Diagnosticar o dar medicamentos", "Mantener la calma y avisar a los servicios de emergencia", "Acompañar a la persona", "Diagnosticar o medicar son tareas de personas formadas."),
        ("=", "{F} ¿Cuántos minutos pasaron entre el aviso de G1 y la llegada del coordinador?", "(15*60+12)-(15*60+2)", "Se restan los minutos entre el aviso y la llegada.", " minutos"),
        ("=", "{F} ¿Cuántos minutos pasaron entre el aviso y la llegada de los servicios de emergencia?", "(15*60+35)-(15*60+2)", "Se restan los minutos entre el aviso y la llegada.", " minutos"),
        ("abc", "{F} Con la meta de ejemplo, ¿se cumplió el tiempo de llegada del coordinador?", "Sí, porque llegó en 10 minutos, menos que 15", "No, porque llegó después de las 15:10", "No, porque los servicios de emergencia tardaron 33 minutos", "10 minutos es menor que la meta de 15; por eso se cumple."),
        ("=", "{F} Con T siendo uno de los 24, ¿cuántas personas quedan con G2 en el lugar seguro?", "24-1", "Se descuenta a T, que está con G1.", " personas"),
        ("abc", "{F} T se siente mejor y quiere seguir el programa antes de que lleguen los servicios de emergencia. ¿Qué corresponde?", "Esperar a los servicios de emergencia y seguir sus indicaciones", "Dejar que siga, porque dice sentirse mejor", "Pedirle al grupo que decida", "La evaluación la hacen los servicios de emergencia, no el guía ni el grupo."),
        ("abc", "{F} Un turista pregunta en voz alta qué tiene T. ¿Qué corresponde?", "No dar información de T y pedir que den espacio para que lo ayuden", "Contar lo que se sabe de T", "Inventar una explicación que calme al grupo", "El estado de salud es un dato sensible; no se comparte ni se inventa."),
        ("abc", "Un turista del grupo comienza a gritar a otro por una discusión. ¿Qué corresponde al guía?", "Mantener distancia segura, hablar con voz calmada, no confrontar y pedir apoyo al coordinador", "Tomarlo del brazo para sacarlo del lugar", "Gritarle más fuerte para que se calle", "No se confronta ni se usa la fuerza; se calma y se pide apoyo."),
        ("abc", "Un turista alterado agrede verbalmente al guía. ¿Qué corresponde?", "No responder con agresión, mantener la calma y pedir apoyo al coordinador, avisando a la autoridad si hay riesgo", "Responder con el mismo tono para defenderse", "Ignorar y seguir el programa como si no pasara nada", "Responder con agresión agrava el conflicto; se prioriza la seguridad."),
        ("abc", "Un turista alterado dice cosas confusas. Otro propone: «seguro está borracho». ¿Qué corresponde?", "No suponer la causa y describir solo lo que se observa", "Confirmar la sospecha con el resto del grupo", "Anotarlo en el registro como un hecho", "Suponer la causa es un juicio sin pruebas; se registran hechos observados."),
        ("abc", "{F} Al terminar, G1 se siente muy tenso por lo vivido. ¿Qué corresponde?", "Conversar con el coordinador o una persona de confianza y participar en la revisión del equipo", "No decirlo, para que no lo crean débil", "Culpar al coordinador por la demora", "Pedir apoyo es parte del autocuidado y la revisión ayuda a mejorar sin culpar."),
    ],
    ctx=("abc", "{F} Un turista del grupo es médico y ofrece atender a T. ¿Qué corresponde?", "Agradecer, informar al coordinador y a los servicios de emergencia y dejar que ellos decidan sobre su ayuda", "Aceptar sin avisar a nadie", "Rechazar con mala cara y sin explicar", "El guía no decide la atención; coordina con el equipo y los servicios de emergencia."),
    sc=[
        ("En Servicios de Turismo: ¿qué es el tiempo de respuesta?", "El tiempo entre el aviso y la llegada del apoyo", "Se calcula restando la hora del aviso a la de llegada."),
        ("¿Qué haces ante el descontrol de conducta de una persona?", "Mantengo la calma y la distancia segura, no confronto y pido apoyo", "No se usa la fuerza ni se discute."),
        ("¿Se supone la causa de un comportamiento alterado?", "No, se describe lo que se observa", "Suponer la causa es un juicio sin pruebas."),
    ],
    op=("Un grupo de ejemplo de 20 personas con dos guías está en un museo. A las 11:00 una turista se siente mal; a las 11:03 el guía avisa al coordinador y a los servicios de emergencia; el coordinador llega a las 11:20; los servicios de emergencia, a las 11:40. La meta de ejemplo para el coordinador es 15 minutos. Calcula los tiempos de respuesta, di si se cumplió la meta, cuántas personas quedan con el otro guía y escribe tres acciones del guía que acompaña.",
        "Coordinador: 11:20 − 11:03 = 17 minutos, no cumple la meta de 15. Servicios de emergencia: 11:40 − 11:03 = 37 minutos. Con el otro guía quedan 19 personas. Acciones: acompañar a la turista, mantener la calma y proteger su privacidad, y seguir las indicaciones de los servicios de emergencia, sin diagnosticar ni dar medicamentos.",
        ["calcula los dos tiempos y compara con la meta", "calcula las personas que quedan con el otro guía", "las acciones no incluyen diagnóstico ni medicamentos"],
        ["tiempos, comparación con la meta y tres acciones"],
        ["calcular los tiempos desde las 11:00 y no desde el aviso", "incluir un diagnóstico", "olvidar al resto del grupo"],
        "Pregunta: «¿desde qué hora cuentas el tiempo de respuesta?». Si no responde, repasa la definición."),
    reinforce="Calcula cuánto tardas en llegar de tu casa a un lugar cercano y compáralo con una meta inventada de 10 minutos.",
    extend="Explica con un ejemplo inventado por qué se registra el tiempo de respuesta en un imprevisto.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (de ejemplo, inventada). Tres guías responden a un mismo imprevisto: un turista pierde sus documentos. Guía X: dice «usted fue descuidado», fotografía los documentos que quedan y los publica en el chat del grupo para pedir ayuda, y avisa al coordinador. "
     "Guía Y: calma al turista con voz tranquila, lo acompaña a un lugar seguro, avisa al coordinador, registra los hechos con iniciales y le indica que puede hacer la denuncia ante la autoridad competente. "
     "Guía Z: calma al turista, lo acompaña y avisa al coordinador, pero no hace registro y comenta el caso con otros turistas. "
     "Lista de cotejo (1 punto cada una): seguridad primero; trato respetuoso sin culpar; avisa al coordinador; registra con hechos y datos mínimos; protege los datos del turista. "
     "Tiempos de aviso de los 5 incidentes de un mes de ejemplo, en minutos: 3, 8, 4, 12 y 3. Meta de ejemplo: promedio de 5 minutos o menos. En otro mes de ejemplo hubo 10 incidentes y 8 tienen registro completo.")
build(
    O5, 5, F,
    use="Aprenderé a comparar respuestas ante un imprevisto con una lista de cotejo, a calcular indicadores simples del mes y a mejorar el plan sin culpar a una persona.",
    prior=["Sé qué es un plan de contingencia y un registro de incidente.", "Sé calcular promedios y porcentajes exactos.", "Sé que los datos personales se protegen."],
    explain=[
        "Comparar alternativas ante un imprevisto es evaluar cada respuesta con los mismos criterios. En la lista de cotejo, cada criterio vale un punto: seguridad primero, trato respetuoso sin culpar, aviso al coordinador, registro con hechos y datos mínimos, y protección de los datos del turista. Una respuesta que publica documentos en un chat grupal o comenta el caso con otros turistas no protege los datos, aunque haya avisado.",
        "La calidad se verifica también con indicadores del mes. El promedio del tiempo de aviso se obtiene sumando los tiempos y dividiendo por la cantidad de incidentes; el porcentaje de registros completos se calcula con los registros completos sobre el total. Se comparan con las metas de ejemplo del prestador, y si no se cumplen, se busca la causa en el proceso y no se culpa a una persona.",
        "Después de un imprevisto el equipo hace una revisión: qué funcionó, qué se puede mejorar y cómo cuidarse. Ese aprendizaje se incorpora al plan y a la capacitación. Este cuaderno es conceptual; el manejo real de imprevistos corresponde a personas formadas y al prestador autorizado.",
    ],
    vocab=[("indicador", "dato simple que mide cómo va un aspecto de la calidad"), ("revisión del equipo", "conversación posterior para ver qué funcionó y qué mejorar"), ("causa en el proceso", "falla del procedimiento y no de una persona en particular"), ("registro completo", "registro con todos los campos llenos con hechos objetivos"), ("capacitación", "formación del equipo para actuar mejor")],
    worked=[
        ("Puntaje de cotejo", "Un guía de ejemplo cuida la seguridad, trata con respeto y avisa al coordinador, pero no registra ni protege los datos. ¿Cuántos puntos obtiene?", ["Cumple 3 de los 5 criterios.", "Cada criterio vale un punto."], "3 puntos"),
        ("Promedio de tiempos", "Tres avisos de ejemplo tardaron 2, 4 y 6 minutos. ¿Cuál es el promedio?", ["Se suman: 2 + 4 + 6 = 12.", "Se divide por 3: 12 ÷ 3 = 4."], "4 minutos"),
    ],
    mistakes=[("Culpar a un guía porque el tiempo de aviso fue largo, sin revisar por qué.", "La demora puede deberse a un proceso confuso o falta de teléfono con carga.", "Busca primero la causa en el proceso y mejora el plan."),
              ("Dejar sin registrar un incidente «menor».", "Los incidentes menores muestran patrones que ayudan a prevenir otros.", "Registra todos los incidentes con hechos y datos mínimos.")],
    T=[
        ("abc", "En Servicios de Turismo: ¿qué es un indicador de calidad?", "Un dato simple que mide cómo va un aspecto del servicio", "Una opinión personal del guía", "Una lista de turistas inscritos", "Un indicador mide con datos; una opinión o un listado no lo hacen."),
        ("abc", "En Servicios de Turismo: ¿qué es una revisión del equipo después de un imprevisto?", "Una conversación para ver qué funcionó y qué se puede mejorar, sin culpar", "Una reunión para decidir quién tuvo la culpa", "Una encuesta solo para los turistas", "La revisión busca aprender y mejorar el plan, no culpar."),
        ("abc", "En Servicios de Turismo: ¿qué es un registro completo?", "Uno con todos los campos llenos, con hechos objetivos", "Uno que incluye la opinión del guía", "Uno con el nombre completo del turista", "Un registro completo tiene todos los campos y solo hechos."),
        ("abc", "{F} ¿Cuál guía obtiene el mayor puntaje en la lista de cotejo?", "El guía Y", "El guía X", "El guía Z", "Y cumple los cinco criterios; Z y X cumplen menos."),
        ("=", "{F} Si Y cumple los cinco criterios y Z cumple tres, ¿cuántos puntos más tiene Y que Z?", "5-3", "Se resta el puntaje de Z al de Y.", " puntos"),
        ("abc", "{F} ¿Qué criterios incumple el guía Z?", "Registrar con hechos y proteger los datos", "Calmar al turista y acompañarlo", "Avisar al coordinador", "Z no hizo registro y comentó el caso con otros turistas."),
        ("abc", "{F} ¿Qué error grave comete el guía X respecto de los datos?", "Publica fotos de los documentos del turista en el chat del grupo", "Avisa al coordinador", "Le habla con calma", "Publicar los documentos expone datos personales a muchas personas."),
        ("=", "{F} ¿Cuántos minutos suman los cinco tiempos de aviso del mes?", "3+8+4+12+3", "Se suman los cinco tiempos de aviso.", " minutos"),
        ("=", "{F} ¿Cuál es el promedio del tiempo de aviso?", "(3+8+4+12+3)//5", "Se divide la suma de los tiempos por 5 incidentes.", " minutos"),
        ("abc", "{F} ¿Se cumple la meta de ejemplo de 5 minutos o menos de promedio?", "No, porque el promedio es 6 minutos", "Sí, porque tres avisos fueron de 3 o 4 minutos", "Sí, porque el promedio es 5", "El promedio es 6, mayor que la meta de 5."),
        ("=", "{F} ¿Qué porcentaje de los incidentes del otro mes tiene registro completo?", "8*100//10", "Ocho de diez se pasan a porcentaje.", " %"),
        ("abc", "{F} El aviso de 12 minutos fue el más largo. ¿Qué corresponde?", "Revisar por qué ocurrió, en el proceso, antes de culpar a una persona", "Sancionar al guía sin escuchar", "Borrar ese dato para mejorar el promedio", "Se busca la causa en el proceso; borrar datos oculta el problema."),
        ("abc", "{F} Una compañera propone no registrar los incidentes pequeños para ahorrar tiempo. ¿Qué respondes?", "Que los incidentes pequeños también se registran, porque muestran patrones para prevenir", "Que tiene razón, el tiempo es limitado", "Que se registren solo si el turista lo pide", "El registro de todos los incidentes ayuda a mejorar el plan."),
    ],
    ctx=("abc", "{F} Tras el mes, el coordinador pregunta qué mejorarías para cumplir la meta de aviso. ¿Qué propones?", "Revisar el proceso de aviso y asegurar teléfonos con carga y contactos a mano", "Pedir al guía que viaje sin teléfono", "Eliminar la meta de 5 minutos", "Mejorar el proceso es una causa concreta; eliminar la meta no resuelve el problema."),
    sc=[
        ("En Servicios de Turismo: ¿cómo se calcula el promedio del tiempo de aviso?", "Se suman los tiempos y se divide por la cantidad de incidentes", "Se compara con la meta de ejemplo."),
        ("¿Qué se hace si no se cumple una meta?", "Se busca la causa en el proceso y se mejora el plan", "Culpar a una persona no corrige el proceso."),
        ("¿Qué criterio protege la privacidad del turista?", "Proteger los datos del turista", "No se publican ni se comentan sus documentos."),
    ],
    op=("Dos guías de ejemplo atienden a una turista que perdió su monedero. Ambos cuidan la seguridad. Guía M: la calma, avisa al coordinador a los 2 minutos, registra con iniciales y la acompaña a denunciar. Guía N: le dice «qué lástima, para eso hay que tener cuidado», avisa al coordinador a los 9 minutos y comenta el caso con el grupo. Aplica la lista de cotejo de la ficha, da el puntaje de cada guía, calcula la diferencia de tiempos de aviso y escribe una propuesta de mejora.",
        "M: seguridad, trato respetuoso, aviso, registro y datos: 5 puntos. N: seguridad quizá sí, trato no (culpa), aviso sí, registro no, datos no: 2 puntos. Diferencia de aviso: 9 − 2 = 7 minutos. Mejora: capacitar al equipo en trato sin culpar, en protección de datos y en el registro, y revisar el proceso de aviso.",
        ["aplica los cinco criterios a ambos guías", "calcula la diferencia de tiempos", "propone una mejora centrada en el proceso"],
        ["puntaje de cada guía, cálculo y propuesta de mejora"],
        ["no distinguir el trato respetuoso", "culpar a N en lugar de mejorar el proceso", "olvidar los datos del turista"],
        "Pregunta: «¿qué mejorarías en el proceso y no en la persona?». Si no responde, repasa la revisión del equipo."),
    reinforce="Anota tres criterios para evaluar cómo te atendieron en un reclamo que hayas hecho o presenciado.",
    extend="Explica con un ejemplo inventado por qué una meta de tiempo debe revisarse con datos antes de cambiarla.",
)
