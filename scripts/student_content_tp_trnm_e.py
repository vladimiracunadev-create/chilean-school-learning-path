"""Tripulación de Naves Mercantes y Especiales TP 3.º y 4.º medio: OAE-09 (comunicar y recibir información en inglés marítimo: frases y vocabulario normalizados, lectura de registros, números y mensajes). Todo en papel, con datos de ejemplo; sin procedimientos operativos de radio ni de emergencia."""
from __future__ import annotations

from tp_trnm_common import AVISO, EMER, build

O9 = "TP-TRNM-3y4-OAE-09"

# ============================================================ OAE-09, clase 1
F = ("Ficha 1 (frases de ejemplo, en inglés). «Say again.» «Stand by.» «Understood.» «Confirm, please.» Palabras de aviso: «Mayday», «Pan-Pan» y «Sécurité». "
     "La «Nave Demo» tiene 24 tripulantes de ejemplo, de los cuales 6 hablan español como lengua materna.")
build(
    O9, 1, F,
    use="Aprenderé por qué se usa el inglés a bordo, qué son las frases normalizadas de la OMI y qué significan algunas frases y palabras de aviso básicas.",
    prior=["Sé qué es una orden y por qué se repite.", "Sé restar números enteros.", "Sé leer palabras simples en inglés."],
    explain=[
        "A bordo trabajan personas de distintos países y lenguas, por lo que el inglés es el idioma común del mar. La OMI (Organización Marítima Internacional) promueve frases normalizadas de comunicación marítima, que son frases cortas y siempre iguales para que todos las entiendan. Algunas son: «Say again» (repita, por favor), «Stand by» (espere), «Understood» (entendido) y «Confirm, please» (confirme, por favor). Un mensaje claro es corto, usa palabras estándar y se confirma repitiéndolo.",
        "Hay tres palabras de aviso que se reconocen en todo el mundo: «Mayday» indica un peligro grave e inmediato, «Pan-Pan» indica una urgencia que todavía no es un peligro inmediato, y «Sécurité» indica un aviso de seguridad, por ejemplo sobre el tiempo o la navegación. Este cuaderno enseña a reconocer su significado, no a hacer llamadas de radio. Un ejemplo con otra frase: «Not understood» significa «no entendido».",
        f"Ante un accidente o una caída al agua, la regla general es dar la alarma y avisar; las llamadas de socorro las hace personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("OMI", "Organización Marítima Internacional"), ("frase normalizada", "frase corta y siempre igual que se usa para evitar malentendidos"), ("Say again", "frase que pide repetir un mensaje"), ("Stand by", "frase que pide esperar"), ("Understood", "frase que indica que se entendió"), ("Mayday", "palabra que indica un peligro grave e inmediato"), ("Pan-Pan", "palabra que indica una urgencia sin peligro inmediato"), ("Sécurité", "palabra que anuncia un aviso de seguridad")],
    worked=[
        ("Traducir una frase", "Un oficial de ejemplo dice «Not understood». ¿Qué significa?", ["«Understood» es «entendido».", "«Not» niega la frase."], "No entendido"),
        ("Elegir la palabra de aviso", "Una nave de ejemplo quiere dar un aviso sobre una boya apagada que podría afectar la navegación, sin que haya un peligro inmediato. ¿Qué palabra de aviso corresponde?", ["No es un peligro grave e inmediato ni una urgencia.", "Es un aviso de seguridad."], "Sécurité"),
    ],
    mistakes=[("Creer que «Mayday» sirve para cualquier problema.", "Mayday es solo para un peligro grave e inmediato.", "Usa la palabra de aviso que corresponde a la situación."),
              ("Responder «sí» a una orden en inglés que no se entendió.", "Responder sin entender puede causar un error grave.", "Pide «Say again» hasta entender.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿por qué el inglés es el idioma común del mar?", "Porque las tripulaciones son de distintos países y necesitan una lengua compartida", "Porque todas las naves son de países de habla inglesa", "Porque el inglés es el único idioma permitido a bordo", "Las tripulaciones mezclan lenguas, por lo tanto se usa un idioma común."),
        ("abc", "En Tripulación de Naves: ¿qué es una frase normalizada?", "Una frase corta y siempre igual que se usa para evitar malentendidos", "Una frase larga que explica la maniobra", "Una frase secreta que solo entiende el capitán", "La normalización busca que todos entiendan igual."),
        ("abc", "{F} ¿Qué significa «Say again»?", "Repita, por favor", "Espere", "Entendido", "«Say again» pide repetir el mensaje."),
        ("abc", "{F} ¿Qué significa «Stand by»?", "Espere", "Repita, por favor", "Confirme, por favor", "«Stand by» es la frase que pide esperar."),
        ("abc", "{F} ¿Qué frase de la ficha se usa para indicar que se entendió un mensaje?", "«Understood»", "«Say again»", "«Stand by»", "«Understood» es la frase que significa entendido."),
        ("abc", "{F} ¿Qué indica la palabra «Mayday»?", "Un peligro grave e inmediato", "Un aviso de seguridad sobre el tiempo", "Una espera de unos minutos", "Mayday es la palabra de aviso de peligro grave e inmediato."),
        ("=", "{F} ¿Cuántos tripulantes de la nave de ejemplo no hablan español como lengua materna?", "24-6", "Se resta al total de tripulantes los que hablan español.", " tripulantes"),
        ("=", "{F} Si un mensaje de 12 palabras se repite 2 veces para confirmarlo, ¿cuántas palabras se dicen en total contando el mensaje original?", "12*3", "Se multiplica el mensaje por las 3 veces que se dice: la original y dos repeticiones.", " palabras"),
        ("abc", "{F} Un aviso sobre un cambio de tiempo que podría afectar la navegación, sin peligro inmediato, usa la palabra:", "«Sécurité»", "«Mayday»", "«Understood»", "Un aviso de seguridad sin peligro inmediato usa Sécurité."),
        ("abc", "Durante una visita de ejemplo ves a una persona caer al agua desde la pasarela. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo ni entrar al agua, dar la alarma («Man overboard») y avisar a un adulto responsable y a emergencias", "Acercarte al borde para ayudarla", "Entrar al agua con un chaleco para sacarla", "Intervenir sin formación puede causar otro accidente; se da la alarma y se avisa."),
        ("abc", "{F} Un compañero responde «Understood» a una orden en inglés, pero no la entendió, «para no quedar mal». ¿Qué respuesta es correcta?", "Es falso: debe pedir «Say again» hasta entender", "Es cierto, porque responder rápido es lo importante", "Es cierto, si la orden parece simple", "Responder sin entender puede llevar a un error grave."),
        ("abc", "{F} Una nave de ejemplo tiene un problema urgente, pero sin peligro inmediato. ¿Qué palabra de aviso corresponde?", "«Pan-Pan»", "«Mayday»", "«Sécurité»", "Una urgencia sin peligro inmediato usa Pan-Pan."),
        ("abc", "En Tripulación de Naves: ¿por qué un mensaje normalizado es corto y siempre igual?", "Para que todas las personas lo entiendan igual aunque tengan lenguas maternas distintas", "Para que sea difícil de entender", "Para que cada persona le cambie las palabras", "La repetición de la misma forma reduce los malentendidos."),
    ],
    ctx=("abc", "Estás de visita en el puente de una nave de ejemplo y alguien te pide que «llames por radio» para probar el equipo. ¿Qué respondes?", "Que no, porque las llamadas de radio las hace personal autorizado y este cuaderno solo enseña conceptos", "Que sí, si dices bien «Mayday»", "Que sí, si lo haces rápido", "Una llamada de socorro falsa o de prueba puede causar un problema grave; solo la hace personal autorizado."),
    sc=[
        ("En Tripulación de Naves: ¿qué es la OMI?", "La Organización Marítima Internacional", "La OMI promueve normas y frases comunes."),
        ("¿Qué frase pide repetir un mensaje?", "«Say again»", "Se usa para repetir lo que no se entendió."),
        ("¿Qué indica «Pan-Pan»?", "Una urgencia sin peligro inmediato", "Pan-Pan es menos grave que Mayday."),
    ],
    op=("En la «Nave Ejemplo» (caso de ejemplo) hay 30 tripulantes, 9 de los cuales hablan español como lengua materna. Un oficial dice en inglés «Stand by» y luego «Confirm, please». Escribe (a) cuántos tripulantes no hablan español como lengua materna, (b) qué significa cada frase del oficial, (c) qué palabra de aviso usarías para un aviso de seguridad sobre el tiempo, (d) por qué la comunicación se repite y se confirma.",
        "(a) 30 − 9 = 21 tripulantes. (b) «Stand by»: espere; «Confirm, please»: confirme, por favor. (c) «Sécurité». (d) Porque así se comprueba que todos entendieron el mismo mensaje y se evitan errores.",
        ["calcula los tripulantes", "traduce las frases", "elige la palabra de aviso", "explica por qué se confirma"],
        ["hoja con las cuatro respuestas"],
        ["usar Mayday para un aviso de tiempo", "confundir «Stand by» con «Say again»", "no explicar por qué se confirma"],
        "Pregunta: «¿qué pasaría si una orden se entiende mal?». Si no responde, pídele que relea el último ejemplo resuelto."),
    reinforce="Escribe en una tabla seis frases o palabras de esta clase con su significado en español.",
    extend="Explica con un ejemplo por qué una frase normalizada reduce los malentendidos entre tripulantes de distintos países.",
)

# ============================================================ OAE-09, clase 2
F = ("Ficha 2 (vocabulario y mensajes de ejemplo, en inglés). bridge, puente; deck, cubierta; engine room, sala de máquinas; bow, proa; stern, popa; port, babor; starboard, estribor; lifejacket, chaleco salvavidas; alarm, alarma. "
     "Mensaje 1: «Check the engine room alarm.» Mensaje 2: «Starboard side, near the bow.» Mensaje 3: «Lifejackets are in the deck locker.»")
build(
    O9, 2, F,
    use="Aprenderé el vocabulario básico en inglés de las áreas y partes de una nave y a entender mensajes cortos que lo usan.",
    prior=["Sé qué son proa, popa, babor y estribor.", "Sé qué hay en el puente, la cubierta y la sala de máquinas.", "Sé contar y restar números enteros."],
    explain=[
        "Para trabajar en una nave con tripulantes de varios países hay que conocer el vocabulario en inglés. Las áreas son: bridge (puente), deck (cubierta) y engine room (sala de máquinas). Las partes y lados son: bow (proa), stern (popa), port (babor) y starboard (estribor). Algunas palabras de seguridad son: lifejacket (chaleco salvavidas), alarm (alarma), fire (fuego) y exit (salida). También sirven check (revisar) y locker (armario). Las palabras de un mismo grupo se aprenden juntas.",
        "Un mensaje corto combina palabras clave: «Starboard side, near the bow» significa «lado de estribor, cerca de la proa». «Near» significa cerca y «far» significa lejos. Un ejemplo con otro mensaje: «Alarm in the bridge» es «alarma en el puente». Los mensajes también dicen dónde y qué; si falta alguno de los dos, se pide «Say again». Este cuaderno enseña a entender mensajes y no a operar equipos.",
        f"Si un mensaje habla de un peligro, la regla general es dar la alarma y avisar. {EMER} {AVISO}",
    ],
    vocab=[("bridge", "puente"), ("deck", "cubierta"), ("engine room", "sala de máquinas"), ("bow", "proa"), ("stern", "popa"), ("port", "babor"), ("starboard", "estribor"), ("lifejacket", "chaleco salvavidas"), ("alarm", "alarma"), ("near / far", "cerca / lejos")],
    worked=[
        ("Traducir una palabra", "En un mensaje de ejemplo aparece «stern». ¿Qué significa?", ["Stern es una parte de la nave.", "Es la parte de atrás."], "Popa"),
        ("Entender un mensaje", "Un mensaje de ejemplo dice «Alarm in the engine room». ¿Qué dice?", ["«Alarm» es alarma.", "«Engine room» es sala de máquinas."], "Alarma en la sala de máquinas"),
    ],
    mistakes=[("Confundir «port» (babor) con «puerto».", "En una nave «port» es el lado izquierdo; el puerto se dice «harbor» o «port» según el contexto.", "Revisa el contexto del mensaje."),
              ("Entender un mensaje sin ubicar el «dónde».", "Sin el lugar no se sabe a dónde ir ni qué revisar.", "Pide «Say again» si falta el lugar.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué significa «bridge» en una nave?", "Puente", "Cubierta", "Sala de máquinas", "Bridge es el puente de mando de la nave."),
        ("abc", "En Tripulación de Naves: ¿qué significa «lifejacket»?", "Chaleco salvavidas", "Bote salvavidas", "Alarma de incendio", "Lifejacket es la palabra inglesa del chaleco salvavidas."),
        ("abc", "{F} ¿Qué significa «starboard»?", "Estribor", "Babor", "Proa", "Starboard es el lado derecho de la nave, es decir, estribor."),
        ("abc", "{F} ¿Qué significa «bow»?", "Proa", "Popa", "Cubierta", "Bow es la parte delantera de la nave."),
        ("abc", "{F} ¿Qué dice el mensaje 2?", "Lado de estribor, cerca de la proa", "Lado de babor, lejos de la popa", "Lado de estribor, lejos de la proa", "Starboard es estribor y near the bow es cerca de la proa."),
        ("abc", "{F} ¿Qué dice el mensaje 3?", "Los chalecos salvavidas están en el armario de cubierta", "Los chalecos salvavidas están en la sala de máquinas", "Las alarmas están en el armario de cubierta", "Lifejackets son chalecos y deck locker es el armario de cubierta."),
        ("abc", "{F} ¿Qué dice el mensaje 1?", "Revisar la alarma de la sala de máquinas", "Revisar la alarma de la cubierta", "Apagar la sala de máquinas", "Check es revisar y engine room alarm es la alarma de la sala de máquinas."),
        ("=", "{F} El vocabulario de la ficha tiene 9 palabras con su traducción. Si 3 son de áreas, 4 de partes y lados y el resto son de seguridad, ¿cuántas son de seguridad?", "9-3-4", "Se restan al total las palabras de áreas y las de partes y lados.", " palabras"),
        ("abc", "{F} Se recibe el mensaje «Alarm in the bridge». ¿Cuál es su traducción?", "Alarma en el puente", "Alarma en la cubierta", "Puente en la alarma", "Bridge es puente y alarm es alarma."),
        ("abc", "{F} Un compañero recibe un mensaje que dice «Fire!» y no lo entiende. ¿Qué es lo correcto?", "Dar la alarma y avisar de inmediato, porque «Fire» significa fuego", "Pedir que lo repitan antes de hacer nada", "Esperar a saber qué hay en el mensaje", "Fire significa fuego, y ante un incendio se da la alarma sin acercarse."),
        ("abc", "{F} El mensaje dice «Starboard side» y no dice el lugar. ¿Qué corresponde?", "Pedir «Say again» para obtener la ubicación completa", "Suponer que es cerca de la popa", "Ignorar el mensaje", "Un mensaje sin lugar completo se pide de nuevo."),
        ("=", "{F} Si el armario de cubierta guarda 24 chalecos y se retiran 6 para una revisión de papel, ¿cuántos quedan?", "24-6", "Se restan los chalecos retirados a los que había.", " chalecos"),
        ("abc", "{F} En el mensaje «Lifejackets are in the deck locker», ¿qué palabra indica el lugar?", "«deck locker»", "«Lifejackets»", "«are»", "Deck locker nombra el armario de cubierta donde están los chalecos."),
    ],
    ctx=("abc", "Una persona de ejemplo te muestra un mensaje en inglés que no entiendes y te pide «hacer lo que dice» sin traducirlo. ¿Qué respondes?", "Que primero se debe entender el mensaje o pedir que lo repitan antes de hacer algo", "Que lo haces igual, porque ella lo pidió", "Que lo haces rápido y preguntas después", "Actuar sin entender un mensaje puede causar un error."),
    sc=[
        ("En Tripulación de Naves: ¿qué significa «engine room»?", "Sala de máquinas", "Engine room es el área de los motores."),
        ("¿Qué significa «port» como lado de la nave?", "Babor", "Port es el lado izquierdo de la nave."),
        ("¿Qué se hace si un mensaje no dice dónde?", "Se pide «Say again»", "Sin el lugar el mensaje queda incompleto."),
    ],
    op=("Mensajes de ejemplo en inglés. M1: «Alarm in the engine room, port side.» M2: «Lifejackets near the bridge.» M3: «Check the deck, starboard side, near the stern.» Escribe (a) la traducción de cada mensaje, (b) cuántos mensajes hablan de la cubierta o de la sala de máquinas, (c) qué hace una persona en formación al recibir M1, (d) qué haces si el mensaje M3 llega sin la palabra «stern».",
        "(a) M1: alarma en la sala de máquinas, lado de babor. M2: chalecos salvavidas cerca del puente. M3: revisar la cubierta, lado de estribor, cerca de la popa. (b) Dos: M1 y M3. (c) Informa al oficial a cargo y no interviene. (d) Pide «Say again» para completar la ubicación.",
        ["traduce los tres mensajes", "cuenta los mensajes por área", "indica qué hace con M1", "indica qué hace si falta un dato"],
        ["hoja con las cuatro respuestas"],
        ["confundir port con puerto", "no mencionar el lugar", "actuar sin entender"],
        "Pregunta: «¿qué dice cada palabra clave?». Si no responde, pídele que relea el vocabulario de la ficha."),
    reinforce="Haz una lista de diez palabras en inglés de esta clase con su traducción en español.",
    extend="Escribe en inglés un mensaje de cinco palabras con una ubicación y tradúcelo.",
)

# ============================================================ OAE-09, clase 3
F = ("Ficha 3 (extracto de bitácora de ejemplo, en inglés). «0800 – Engine room: cooling water temperature 78 °C. 0900 – Deck: wind 20 knots. 0930 – Bridge: course 090, speed 12 knots. "
     "1000 – Engine room: oil pressure low, reported to the chief engineer.»")
build(
    O9, 3, F,
    use="Aprenderé a leer un registro escrito en inglés, a entender las horas y los datos, y a escribir un informe corto en inglés.",
    prior=["Sé qué es una bitácora.", "Sé el vocabulario básico de áreas de una nave.", "Sé leer horas en formato de 24 horas."],
    explain=[
        "Una bitácora en inglés usa frases cortas con la hora, el área y el dato. La hora se escribe en formato de 24 horas, por ejemplo «0930» es las 09:30 y «1400» es las 14:00. Algunas palabras útiles son: «cooling water temperature» (temperatura del agua de enfriamiento), «oil pressure» (presión del aceite), «wind» (viento), «course» (rumbo), «speed» (velocidad), «knots» (nudos), «low» (baja) y «high» (alta). «Reported to» significa informado a, y «chief engineer» es el jefe de máquinas.",
        "Un informe corto en inglés tiene el mismo orden que en español: área, dato, valor y a quién se informó. Un ejemplo con otro registro: «1100 – Deck: wind 25 knots» es «11:00 – cubierta: viento 25 nudos». Los registros se escriben con datos reales y no se cambian para que cuadren.",
        f"Cuando un registro dice «reported to» alguien, esa persona es la que decide qué hacer. {EMER} {AVISO}",
    ],
    vocab=[("0930", "las 09:30, en formato de 24 horas"), ("cooling water temperature", "temperatura del agua de enfriamiento"), ("oil pressure", "presión del aceite"), ("course", "rumbo"), ("speed", "velocidad"), ("low / high", "baja / alta"), ("reported to", "informado a"), ("chief engineer", "jefe de máquinas")],
    worked=[
        ("Traducir un registro", "Un registro de ejemplo dice «1100 – Deck: wind 25 knots». ¿Qué dice?", ["1100 es las 11:00.", "Deck es cubierta y wind es viento."], "A las 11:00, en cubierta, viento de 25 nudos"),
        ("Escribir en inglés", "¿Cómo se dice en inglés «presión del aceite baja»?", ["Presión del aceite es «oil pressure».", "Baja es «low»."], "Oil pressure low"),
    ],
    mistakes=[("Leer «0930» como «novecientos treinta» y no como una hora.", "En la bitácora esa cifra es una hora en formato de 24 horas.", "Lee los dos primeros dígitos como horas y los dos últimos como minutos."),
              ("Traducir «low» como «lento».", "En un registro «low» significa baja, como en presión baja.", "Traduce según el contexto: low es baja.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿qué hora es «1400» en un registro?", "Las 14:00", "Las 1:40", "Las 4:00", "En formato de 24 horas, 1400 es las 14:00."),
        ("abc", "En Tripulación de Naves: ¿qué significa «chief engineer»?", "Jefe de máquinas", "Capitán", "Jefe de cubierta", "Chief engineer es el jefe de máquinas."),
        ("abc", "{F} ¿Qué significa «cooling water temperature»?", "Temperatura del agua de enfriamiento", "Temperatura del aire", "Presión del agua", "Cooling water es el agua de enfriamiento y temperature es temperatura."),
        ("abc", "{F} ¿Qué dice el registro de las 0900?", "En cubierta, viento de 20 nudos", "En la sala de máquinas, viento de 20 nudos", "En cubierta, velocidad de 20 nudos", "Deck es cubierta, wind es viento y knots es nudos."),
        ("=", "{F} ¿Cuántos minutos pasan entre el registro de las 0900 y el de las 0930?", "(9*60+30)-(9*60)", "Se pasan ambas horas a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Qué dice el registro de las 0930?", "En el puente, rumbo 090 y velocidad de 12 nudos", "En la cubierta, rumbo 090 y viento de 12 nudos", "En el puente, velocidad 090 y rumbo de 12 nudos", "Bridge es puente, course es rumbo y speed es velocidad."),
        ("abc", "{F} ¿Qué significa el registro de las 1000?", "Presión de aceite baja en la sala de máquinas, informada al jefe de máquinas", "Presión de aceite alta, informada al capitán", "Temperatura baja en cubierta, informada al jefe de máquinas", "Oil pressure low es presión de aceite baja y reported to the chief engineer es informado al jefe de máquinas."),
        ("=", "{F} Si la nave mantiene la velocidad de las 0930 durante 3 horas, ¿cuántas millas náuticas recorre?", "12*3", "Se multiplica la velocidad en nudos por las horas.", " millas"),
        ("=", "{F} ¿Cuántas horas pasan entre el primer registro y el último de la ficha?", "10-8", "Se resta la hora del primer registro a la del último.", " horas"),
        ("abc", "{F} ¿Cómo se escribe en inglés «temperatura del agua de enfriamiento alta»?", "Cooling water temperature high", "Cooling water pressure low", "Water temperature cooling low", "Cooling water temperature es la temperatura del agua de enfriamiento y high es alta."),
        ("abc", "{F} Un compañero dice que «reported to the chief engineer» significa que el jefe de máquinas informó al tripulante. ¿Qué respuesta es correcta?", "Es falso: significa que el dato se informó al jefe de máquinas", "Es cierto, porque reported significa informó", "Es cierto, si se lee de derecha a izquierda", "«Reported to» significa informado a alguien."),
        ("abc", "{F} La persona a cargo te dice que cambies «low» por «normal» en el registro de las 1000 para que no haya problemas. ¿Qué corresponde?", "No cambiarlo: el registro refleja el dato real e informar al responsable", "Cambiarlo, porque ella manda", "Cambiarlo y avisar después", "Alterar un registro oculta un dato importante."),
        ("abc", "{F} Una persona no entiende un mensaje en inglés por radio interna. ¿Qué dice?", "«Say again, please»", "«Understood»", "«Mayday»", "Para pedir repetir se dice Say again; Understood indicaría que entendió."),
    ],
    ctx=("abc", "Estás leyendo una bitácora de ejemplo y encuentras una anotación con una palabra que no conoces, «overheat». La persona a cargo no está. ¿Qué haces?", "Anotas la duda e informas al oficial para que te explique, sin suponer", "Supones que significa «normal»", "Tachas la anotación", "Una palabra desconocida se consulta; suponer o tachar pueden ocultar un problema."),
    sc=[
        ("En Tripulación de Naves: ¿qué hora es «0930»?", "Las 09:30", "Las dos primeras cifras son las horas y las dos últimas, los minutos."),
        ("¿Qué significa «oil pressure»?", "Presión del aceite", "Oil es aceite y pressure es presión."),
        ("¿Qué significa «reported to»?", "Informado a", "Reported to indica a quién se informó."),
    ],
    op=("Registro de ejemplo en inglés. «0600 – Bridge: course 180, speed 10 knots. 0700 – Engine room: oil temperature high, reported to the chief engineer. 0800 – Deck: wind 15 knots.» Escribe (a) la traducción de cada línea, (b) cuántas millas náuticas recorre la nave entre las 0600 y las 0800 si mantiene la velocidad, (c) qué dato se informó al jefe de máquinas, (d) cómo escribirías en inglés «temperatura del agua de enfriamiento alta».",
        "(a) 06:00, puente: rumbo 180, velocidad 10 nudos. 07:00, sala de máquinas: temperatura del aceite alta, informada al jefe de máquinas. 08:00, cubierta: viento 15 nudos. (b) 10 × 2 = 20 millas náuticas. (c) La temperatura del aceite alta. (d) «Cooling water temperature high».",
        ["traduce las líneas", "calcula la distancia", "identifica lo informado", "escribe la frase en inglés"],
        ["hoja con las cuatro respuestas"],
        ["leer la hora como una cantidad", "confundir high con low", "olvidar los nudos"],
        "Pregunta: «¿qué dice cada palabra clave?». Si no responde, pídele que relea el vocabulario de la clase."),
    reinforce="Escribe tres líneas de bitácora de ejemplo en inglés con hora, área y dato.",
    extend="Explica por qué la hora en formato de 24 horas evita confusiones en un registro internacional.",
)

# ============================================================ OAE-09, clase 4
F = ("Ficha 4 (números y letras de ejemplo, en inglés). Números: 0 zero, 1 one, 2 two, 3 three, 4 four, 5 five, 6 six, 7 seven, 8 eight, 9 nine. "
     "Alfabeto de deletreo: A Alfa, B Bravo, C Charlie, D Delta, E Echo, F Foxtrot. Mensajes de ejemplo: «Course two seven zero.» «Zone Bravo four.» «Time one four three zero.»")
build(
    O9, 4, F,
    use="Aprenderé a leer y decir números, horas y letras con el alfabeto de deletreo en inglés, y a calcular con esos datos.",
    prior=["Sé leer una hora en formato de 24 horas.", "Sé qué es un rumbo.", "Sé calcular duraciones en horas y minutos."],
    explain=[
        "Los números y las letras de un mensaje se dicen uno por uno para evitar confusiones. Los números son zero, one, two, three, four, five, six, seven, eight y nine. Las letras se dicen con un alfabeto de deletreo, que da una palabra a cada letra: A es Alfa, B es Bravo, C es Charlie, D es Delta, E es Echo y F es Foxtrot. Así, «Zone Bravo four» es la zona B4 y «Course two seven zero» es el rumbo 270.",
        "Las horas se dicen en formato de 24 horas, cifra por cifra: «one four three zero» es 1430, es decir, las 14:30. Para calcular una duración se pasan las horas a minutos y se restan. Un ejemplo con otros datos: de 0845 a 1015 hay 90 minutos. Este cuaderno enseña a leer y decir datos con claridad; no enseña a usar equipos de radio.",
        f"Si un número no se entiende, se pide «Say again» y no se adivina. {EMER} {AVISO}",
    ],
    vocab=[("alfabeto de deletreo", "lista de palabras que se usa para decir cada letra con claridad"), ("Alfa, Bravo, Charlie", "palabras de las letras A, B y C"), ("Delta, Echo, Foxtrot", "palabras de las letras D, E y F"), ("zero a nine", "los números del 0 al 9 en inglés"), ("formato de 24 horas", "forma de escribir la hora de 0000 a 2359")],
    worked=[
        ("Decir un rumbo", "¿Cómo se dice en inglés el rumbo 135?", ["Se dice cifra por cifra.", "1 es one, 3 es three y 5 es five."], "Course one three five"),
        ("Deletrear una zona", "¿Cómo se dice «zona C2» con el alfabeto de deletreo?", ["C es Charlie.", "2 es two."], "Zone Charlie two"),
    ],
    mistakes=[("Decir un número como un solo bloque, por ejemplo «two hundred seventy».", "Puede confundirse con otras cifras; se dice cifra por cifra.", "Di «two seven zero»."),
              ("Usar una palabra inventada para una letra.", "El alfabeto de deletreo es una lista fija.", "Usa solo las palabras de la lista.")],
    T=[
        ("abc", "En Tripulación de Naves: ¿cómo se dice «zero» en español?", "Cero", "Uno", "Nueve", "Zero es la palabra inglesa del número cero."),
        ("abc", "En Tripulación de Naves: ¿qué letra corresponde a la palabra «Bravo» del alfabeto de deletreo?", "La B", "La A", "La C", "Bravo es la palabra de la letra B."),
        ("abc", "{F} ¿Qué rumbo dice el mensaje «Course two seven zero»?", "270", "207", "72", "Two seven zero son las cifras 2, 7 y 0, o sea 270."),
        ("abc", "{F} ¿Qué zona dice «Zone Bravo four»?", "B4", "A4", "B14", "Bravo es la B y four es el 4."),
        ("abc", "{F} ¿Qué hora dice «Time one four three zero»?", "14:30", "13:40", "10:43", "One four three zero son las cifras 1, 4, 3, 0, o sea 14:30."),
        ("abc", "{F} ¿Cómo se dice en inglés el rumbo 180?", "Course one eight zero", "Course one hundred eighty", "Course eight one zero", "Se dice cifra por cifra: one, eight, zero."),
        ("=", "{F} Si el rumbo de 270 cambia a 090, ¿cuántos grados es la diferencia entre ambos?", "270-90", "Se restan los dos rumbos.", "°"),
        ("=", "{F} ¿Cuántos minutos pasan entre las 14:30 y las 16:00?", "(16*60)-(14*60+30)", "Se pasan ambas horas a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Cómo se dice la zona «D3» con el alfabeto de deletreo?", "Zone Delta three", "Zone Charlie three", "Zone Delta four", "D es Delta y 3 es three."),
        ("abc", "{F} Alguien dice «Zone Echo five» y no se entiende bien el último número. ¿Qué corresponde?", "Pedir «Say again» para confirmar la zona", "Suponer que es Echo cinco", "Ignorar el mensaje", "Un dato incierto se confirma; no se adivina."),
        ("abc", "{F} Una compañera dice que «two seven zero» y «two hundred seventy» son lo mismo y se pueden usar indistintamente. ¿Qué respuesta es correcta?", "Es falso: decirlo cifra por cifra reduce los errores", "Es cierto, porque son el mismo número", "Es cierto, si se escribe en la bitácora", "Dicho cifra por cifra, el número se confunde menos con otras palabras."),
        ("=", "{F} Si una nave navega 3 horas y media a 12 nudos, ¿cuántas millas náuticas recorre?", "12*210//60", "Se pasan las 3 horas y media a 210 minutos y se calcula la fracción de la hora.", " millas"),
        ("abc", "{F} ¿Cuál es la mejor forma de decir la zona «F2» a otra persona?", "«Zone Foxtrot two»", "«Zone Francisco dos»", "«Zone effe two»", "El alfabeto de deletreo usa palabras fijas, como Foxtrot para la F."),
    ],
    ctx=("abc", "Un compañero dice en voz alta una zona usando palabras inventadas para las letras. ¿Qué corresponde?", "Recordarle que se usa el alfabeto de deletreo con palabras fijas", "Aceptar las palabras que más le gusten", "Repetir el mensaje con otras palabras inventadas", "Las palabras fijas evitan que dos personas entiendan cosas distintas."),
    sc=[
        ("En Tripulación de Naves: ¿cómo se dice «1» en inglés?", "One", "One es la palabra inglesa del número uno."),
        ("¿Qué letra es «Echo»?", "La E", "Echo es la palabra de la letra E."),
        ("¿Cómo se dicen los números de un rumbo?", "Cifra por cifra", "Decirlos uno por uno reduce los errores."),
    ],
    op=("Mensajes de ejemplo en inglés. M1: «Course zero nine zero.» M2: «Zone Delta two.» M3: «Time zero eight four five.» Escribe (a) qué rumbo, qué zona y qué hora dicen, (b) cuántos minutos pasan entre las 08:45 y las 11:30, (c) cómo se dice en inglés el rumbo 315, (d) qué haces si no entiendes una cifra.",
        "(a) Rumbo 090, zona D2 y hora 08:45. (b) De 08:45 a 11:30 hay 165 minutos (de 525 a 690 minutos desde la medianoche). (c) «Course three one five». (d) Pido «Say again» y no adivino.",
        ["traduce los tres mensajes", "calcula los minutos", "dice un rumbo en inglés", "indica que pide repetir"],
        ["hoja con las cuatro respuestas"],
        ["decir el rumbo como un solo número", "confundir Delta con Charlie", "adivinar una cifra"],
        "Pregunta: «¿qué palabra corresponde a cada cifra o letra?». Si no responde, pídele que relea la ficha."),
    reinforce="Escribe en inglés tres rumbos y tres zonas de ejemplo usando cifras y alfabeto de deletreo.",
    extend="Explica por qué se dicen los números cifra por cifra en lugar de como un solo número.",
)

# ============================================================ OAE-09, clase 5
F = ("Ficha 5 (mensajes de ejemplo, en inglés). Tres versiones de un mismo aviso. Mensaje 1: «Something is wrong.» Mensaje 2: «Engine room, oil pressure low, 1000 hours, reported to the chief engineer.» Mensaje 3: «Oil pressure low at 1000 hours.» "
     "Criterios de un mensaje completo: lugar, dato, hora y a quién se informó (cuatro criterios). Mensaje enviado de ejemplo: «Course zero nine zero.» Mensaje recibido de ejemplo: «Course zero five zero.»")
build(
    O9, 5, F,
    use="Aprenderé a comparar mensajes en inglés según criterios de claridad y a verificar con una repetición que el mensaje recibido coincide con el enviado.",
    prior=["Sé el vocabulario básico en inglés de la nave.", "Sé qué es un informe completo.", "Sé calcular un porcentaje simple."],
    explain=[
        "Un mensaje completo en inglés responde cuatro preguntas: dónde (lugar), qué (dato), cuándo (hora) y a quién se informó. El dato es lo medido o leído, como «oil pressure low»; decir solo que algo anda mal no es un dato. Para comparar mensajes se cuenta cuántos criterios cumple cada uno, y el que cumple más es el mejor. El porcentaje de criterios cumplidos es los criterios cumplidos ÷ los criterios totales × 100.",
        "Para verificar que un mensaje se entendió, quien lo recibe lo repite con las mismas palabras y quien lo envió lo confirma. Si lo repetido no coincide con lo enviado, hay un error y se corrige antes de actuar. Un ejemplo con otro mensaje: se envía «Zone Charlie two» y se repite «Zone Charlie three»; los números no coinciden, por lo tanto se aclara.",
        f"La comunicación clara es una medida de seguridad: reduce los errores. {EMER} {AVISO}",
    ],
    vocab=[("mensaje completo", "mensaje con lugar, dato, hora y a quién se informó"), ("criterio", "regla con la que se evalúa o se compara algo"), ("repetir un mensaje", "decir lo recibido para comprobar que se entendió"), ("coincide", "es igual a lo enviado"), ("error de comunicación", "diferencia entre lo enviado y lo entendido")],
    worked=[
        ("Contar criterios", "Un mensaje de ejemplo dice «Deck, wind 20 knots, 1100 hours». ¿Cuántos de los cuatro criterios cumple?", ["Tiene lugar (deck), dato (wind 20 knots) y hora (1100).", "No dice a quién se informó."], "3 de 4"),
        ("Detectar un error", "Se envía «Speed one two knots» y se repite «Speed one three knots». ¿Coincide?", ["Se compara cifra por cifra.", "Dos no es igual a tres."], "No coincide: hay un error de comunicación"),
    ],
    mistakes=[("Elegir el mensaje más corto porque es más rápido.", "Un mensaje corto sin lugar ni hora puede no servir.", "Elige el que cumple más criterios."),
              ("Dar por entendido un mensaje que no se repitió.", "Sin repetición no se sabe si coincide con lo enviado.", "Repite el mensaje para confirmarlo.")],
    T=[
        ("abc", "{F} ¿Cuántos de los cuatro criterios cumple el mensaje 1?", "Ninguno, porque no dice dónde, qué se leyó, cuándo ni a quién se informó", "Uno, porque avisa que hay un problema", "Cuatro, porque es un mensaje de aviso", "«Something is wrong» no da lugar, dato, hora ni a quién se informó."),
        ("abc", "{F} ¿Cuántos de los cuatro criterios cumple el mensaje 2?", "Los cuatro", "Tres, porque no dice el lugar", "Dos, porque es demasiado largo", "El mensaje 2 dice lugar, dato, hora y a quién se informó."),
        ("abc", "{F} ¿Cuál mensaje es el más completo?", "El mensaje 2, porque cumple los cuatro criterios", "El mensaje 1, porque es el más corto", "El mensaje 3, porque tiene hora", "El mensaje 2 es el único que cumple los cuatro criterios."),
        ("=", "{F} ¿Cuántos criterios le faltan al mensaje 3, que dice el dato y la hora?", "4-2", "Se restan a los cuatro criterios los dos que el mensaje 3 cumple.", " criterios"),
        ("=", "{F} ¿Qué porcentaje de los criterios cumple el mensaje 3?", "2*100//4", "Se dividen los criterios cumplidos entre los totales y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué le falta al mensaje 3?", "El lugar y a quién se informó", "La hora y el dato", "Nada, porque tiene el dato", "El mensaje 3 no dice el lugar ni a quién se informó."),
        ("abc", "{F} ¿Coincide el mensaje recibido de ejemplo con el enviado?", "No, porque se envió 090 y se repitió 050", "Sí, porque ambos dicen «course»", "Sí, porque los dos terminan en cero", "Las cifras del medio no coinciden: 9 y 5."),
        ("=", "{F} ¿Cuántos grados de diferencia hay entre el rumbo enviado y el recibido?", "90-50", "Se restan los dos rumbos.", "°"),
        ("abc", "{F} Tras detectar que el mensaje recibido no coincide, ¿qué corresponde?", "Aclarar el mensaje con «Say again» antes de actuar", "Actuar según el rumbo recibido", "Actuar según el rumbo que cada uno crea", "Una discrepancia se aclara antes de actuar."),
        ("abc", "{F} Un compañero dice que, como los mensajes se entienden, no hace falta repetirlos. ¿Qué respuesta es correcta?", "Es falso: repetir permite detectar errores antes de que causen problemas", "Es cierto, porque repetir pierde tiempo", "Es cierto, si el mensaje es breve", "La repetición verifica que lo entendido coincide con lo enviado."),
        ("abc", "{F} El oficial pide un mensaje completo sobre la presión del aceite. ¿Cuál es el mejor?", "«Engine room, oil pressure low, 1000 hours, reported to the chief engineer»", "«Engine problem»", "«Oil low»", "Cumple lugar, dato, hora y a quién se informó."),
        ("=", "{F} Si de 4 mensajes de ejemplo solo 3 coinciden con lo enviado, ¿qué porcentaje coincide?", "3*100//4", "Se dividen los mensajes que coinciden entre el total y se multiplica por 100.", " %"),
        ("abc", "En Tripulación de Naves: ¿por qué la comunicación clara en inglés es una medida de seguridad?", "Porque reduce los errores entre personas que hablan lenguas distintas", "Porque hace innecesarios los instrumentos", "Porque evita que el oficial dé órdenes", "Un mensaje claro se entiende igual y disminuye los malentendidos."),
    ],
    ctx=("abc", "Un compañero de ejemplo te dice: «no repitas el mensaje, ya lo entendí». ¿Qué respondes?", "Que repetirlo ayuda a detectar errores y no lleva más que unos segundos", "Que no lo repites, porque él lo pidió", "Que lo repites solo si hay peligro", "La repetición es una forma sencilla de evitar malentendidos."),
    sc=[
        ("En Tripulación de Naves: ¿qué cuatro criterios tiene un mensaje completo?", "Lugar, dato, hora y a quién se informó", "Con esos criterios el mensaje se entiende sin preguntar."),
        ("¿Para qué se repite un mensaje?", "Para comprobar que lo entendido coincide con lo enviado", "La repetición ayuda a detectar errores a tiempo."),
        ("¿Qué se hace si el mensaje repetido no coincide?", "Se aclara antes de actuar", "No se actúa con un mensaje dudoso."),
    ],
    op=("Mensajes de ejemplo en inglés. P: «Bridge, wind 25 knots, 1500 hours, reported to the officer of the watch (oficial de guardia).» Q: «Wind 25.» R: «Deck, wind 25 knots.» Mensaje enviado: «Speed one two knots»; mensaje repetido: «Speed one four knots». Escribe (a) cuántos criterios cumple cada mensaje (lugar, dato, hora, a quién se informó), (b) cuál es el más completo, (c) si coincide el mensaje repetido y por qué, (d) qué haces con esa diferencia.",
        "(a) P cumple 4; Q cumple 1 (el dato); R cumple 2 (lugar y dato). (b) P. (c) No coincide: se envió 12 y se repitió 14. (d) Se aclara el mensaje con «Say again» antes de actuar.",
        ["cuenta los criterios", "elige el más completo", "detecta la diferencia", "indica qué hacer con ella"],
        ["hoja con las cuatro respuestas"],
        ["elegir el mensaje más corto", "no comparar cifra por cifra", "actuar con un mensaje dudoso"],
        "Pregunta: «¿qué responde cada mensaje: dónde, qué, cuándo y a quién?». Si no responde, pídele que lo marque en cada uno."),
    reinforce="Escribe en inglés un mensaje completo de cuatro criterios sobre una lectura de ejemplo.",
    extend="Explica por qué repetir un mensaje es especialmente importante cuando las personas tienen lenguas maternas distintas.",
)
