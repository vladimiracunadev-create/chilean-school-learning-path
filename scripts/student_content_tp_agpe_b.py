"""Agropecuaria TP 4.º medio, mención Pecuaria: OAM-04 (producción lechera), OAM-05 (planes sanitarios y bienestar), OAM-06 (forrajes) y OAM-07 (verificación de máquinas, equipos e instrumentos). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_agpe_common import AVISO, EMER, build

O4 = "TP-AGPE-4-OAM-04"
O5 = "TP-AGPE-4-OAM-05"
O6 = "TP-AGPE-4-OAM-06"
O7 = "TP-AGPE-4-OAM-07"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Lechería Demo» es un establecimiento ficticio con 100 vacas, una sala de ordeña con un equipo de ordeña mecánico y un tanque de frío donde se guarda la leche. "
     "Peligros anotados: vacas que pueden patear o empujar, piso mojado y resbaladizo, electricidad cerca del agua, ruido de los equipos, productos de limpieza que dañan la piel y los ojos, y contacto con fluidos de los animales, que puede transmitir enfermedades (zoonosis).")
build(
    O4, 1, F,
    use="Aprenderé qué es la producción lechera, por qué la higiene y el frío cuidan la calidad de la leche y cuáles son los peligros del trabajo en una lechería.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "La producción lechera es la obtención de leche de vacas con fines productivos. La lactancia es el período en que una vaca produce leche después del parto. El calostro es la primera leche, rica en defensas, que es para la cría. La leche destinada a la venta debe tener buena calidad: poca contaminación con microbios y sin restos de medicamentos. Para eso importan la higiene de la ubre y de los equipos, y el enfriado rápido de la leche en un tanque de frío.",
        "El trabajo lechero tiene peligros. Una vaca puede patear aunque sea mansa; el piso mojado hace resbalar; el agua y la electricidad juntas son peligrosas; los productos de limpieza queman la piel y los ojos; y los fluidos animales pueden transmitir zoonosis. La jerarquía de controles ordena las medidas: eliminar, sustituir, cambiar el lugar o el equipo, reglas y capacitación y, al final, el equipo de protección personal (EPP).",
        f"Un piso antideslizante es un control de ingeniería; una regla de lavarse las manos es administrativa. El ordeño y el manejo de los equipos los hace personal capacitado y autorizado, según la norma sanitaria vigente. {EMER} {AVISO}",
    ],
    vocab=[("lactancia", "período en que una vaca produce leche después del parto"), ("calostro", "primera leche después del parto, rica en defensas"), ("sala de ordeña", "lugar donde se extrae la leche de las vacas"), ("tanque de frío", "depósito que enfría y guarda la leche"), ("higiene", "limpieza que evita la contaminación"), ("zoonosis", "enfermedad que pasa de los animales a las personas"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Lactancia", "Una vaca de ejemplo acaba de parir y empieza a producir leche. ¿Qué período comienza?", ["La producción de leche después del parto.", "Ese período se llama lactancia."], "La lactancia"),
        ("Clasificar un control", "Una lechería de ejemplo eleva las tomas eléctricas de la sala a una altura donde no llega el agua. ¿Qué tipo de control es?", ["Cambia físicamente el lugar de la instalación.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que una vaca mansa nunca patea.", "Un susto o un dolor puede hacerla reaccionar con fuerza.", "Se asume que cualquier vaca puede reaccionar."),
              ("Creer que leer sobre el ordeño habilita para ordeñar a las vacas del plantel.", "El ordeño exige formación y autorización.", "Aprende aquí el concepto y deja la labor a personal capacitado.")],
    T=[
        ("abc", "En la lechería: ¿qué es la lactancia?", "El período en que una vaca produce leche después del parto", "El período de gestación de la vaca", "El tiempo que dura el ordeño", "La lactancia es el período de producción de leche."),
        ("abc", "En la lechería: ¿qué es el calostro?", "La primera leche después del parto, rica en defensas", "La leche que se vende al final del mes", "La leche con más grasa", "El calostro es la primera leche, destinada a la cría."),
        ("abc", "En la lechería: ¿para qué sirve el tanque de frío?", "Para enfriar y guardar la leche", "Para calentar el agua de limpieza", "Para pesar a las vacas", "El tanque de frío conserva la leche enfriándola."),
        ("=", "{F} Cada vaca produce 20 litros por día (dato de ejemplo). ¿Cuántos litros produce el plantel en un día?", "100*20", "Se multiplica el número de vacas por la producción de cada una.", " litros"),
        ("abc", "{F} Un piso antideslizante en la sala de ordeña es un control de tipo:", "De ingeniería, porque cambia físicamente el lugar", "Administrativo, porque es una regla", "De EPP, porque protege a quien camina", "El piso modifica el lugar y no depende de que alguien lo recuerde."),
        ("abc", "{F} Una regla que dice «lavarse las manos antes y después de tocar a los animales» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el lugar", "De sustitución, porque cambia a los animales", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al piso mojado de la sala?", "Que una persona resbale y se lastime", "El piso mojado mismo", "Que la leche se enfríe más", "El riesgo es la posibilidad de daño; el piso mojado es el peligro."),
        ("abc", "{F} Una estudiante dice: «las vacas de la lechería son mansas, así que puedo ordeñar una yo sola». ¿Qué respuesta es correcta?", "Es incorrecto: el ordeño lo hace personal capacitado y autorizado", "Es correcto, si la vaca es mansa", "Es correcto, si usa guantes", "Una vaca mansa también puede reaccionar de forma imprevista."),
        ("abc", "{F} En una visita, una vaca patea a una persona y la deja en el suelo. ¿Qué corresponde según las reglas generales?", "No acercarte al animal ni a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte para levantarla tú", "Calmar a la vaca con tus manos", "Un animal inquieto es impredecible; se avisa a quienes pueden ayudar."),
        ("abc", "En la lechería: ¿por qué la leche debe enfriarse pronto después del ordeño?", "Porque el frío frena el crecimiento de microbios y conserva su calidad", "Porque así pesa menos", "Porque se vuelve más espesa", "El frío frena a los microbios que dañan la leche."),
        ("abc", "{F} Se propone solo entregar botas para evitar resbalones en el piso mojado. ¿Qué medida es más efectiva?", "Colocar un piso antideslizante con buen drenaje", "Entregar un segundo par de botas", "Pedir que se camine más despacio", "Cambiar el piso actúa sobre el peligro; las botas son EPP."),
        ("=", "{F} El tanque de ejemplo guarda 3.000 litros. Si se producen 2.000 litros por día, ¿cuántos litros quedan libres en el tanque tras un día de producción, partiendo vacío?", "3000-2000", "Se resta la producción de un día a la capacidad del tanque.", " litros"),
        ("abc", "En la lechería: ¿por qué los productos de limpieza deben guardarse cerrados y rotulados?", "Porque pueden dañar la piel y los ojos y no deben confundirse", "Porque se evaporan", "Porque ocupan mucho espacio", "Rotular y cerrar evita accidentes y confusiones."),
    ],
    ctx=("abc", "Un vecino te ofrece pagarte por ayudar en el ordeño de su lechería «porque ya viste cómo se hace». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, si las vacas son mansas", "Que sí, solo con una vaca", "Haber visto el concepto no habilita para trabajar con animales ni con equipos."),
    sc=[
        ("En la lechería: ¿qué es el calostro?", "La primera leche después del parto", "El calostro es la primera leche y tiene defensas para la cría."),
        ("En la sala de ordeña: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En la lechería: ¿qué hace el tanque de frío con la leche?", "La enfría y la conserva", "El frío conserva la calidad de la leche."),
    ],
    op=("La «Lechería Demo 2» anota una tarea de ejemplo: lavar el piso de la sala de ordeña con un producto fuerte mientras hay vacas y un equipo enchufado con el cable en el suelo mojado. Escribe (a) el peligro del cable y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a una vaca pateando a alguien.",
        "(a) Peligro: cable eléctrico en el piso mojado; riesgo: que una persona reciba una descarga eléctrica. (b) Una regla de no lavar el piso con equipos enchufados ni con animales presentes. (c) Tomas eléctricas elevadas y protegidas, instaladas por personal autorizado. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer tocar el cable", "proponer calmar a la vaca"],
        "Pregunta: «¿qué control aleja el cable del agua aunque nadie se acuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe tres peligros de una sala de ordeña y el riesgo asociado a cada uno.",
    extend="Explica con un ejemplo por qué la higiene del equipo cuida la calidad de la leche.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (parámetros y registros de ejemplo, inventados). «Lechería Demo»: 100 vacas, 2 ordeñas al día. Parámetros de ejemplo: la leche se enfría a 4 grados dentro de 2 horas después del ordeño; índice de células somáticas (indicador de inflamación de la ubre) de 300 como máximo; recuento bacteriano (indicador de limpieza) de 50 como máximo. "
     "Informe del laboratorio: células somáticas 250, recuento bacteriano 40. Documentos: el registro de producción, el registro de limpieza del equipo, el registro de temperatura del tanque y el informe de calidad del laboratorio. Roles: ordeñador capacitado, jefe de lechería y médico veterinario.")
build(
    O4, 2, F,
    use="Aprenderé los indicadores de calidad de la leche, los documentos de una lechería y los roles de quienes producen y controlan la leche.",
    prior=["Sé qué es la lactancia y el tanque de frío.", "Sé comparar un valor con un máximo.", "Sé multiplicar y dividir enteros."],
    explain=[
        "La calidad de la leche se mide con indicadores. El recuento de células somáticas indica si la ubre está inflamada: un valor alto sugiere un problema de salud de la vaca llamado mastitis, que evalúa el veterinario. El recuento bacteriano indica la limpieza del ordeño y del equipo: un valor alto sugiere falta de higiene. La temperatura del tanque indica si el enfriado se hizo a tiempo. Cada indicador tiene un máximo o un rango de referencia.",
        "Los documentos dejan evidencia: el registro de producción anota los litros de cada ordeña; el registro de limpieza dice cuándo se limpió el equipo y quién lo hizo; el registro de temperatura del tanque muestra el enfriado; el informe del laboratorio entrega los resultados de calidad. El ordeñador capacitado ejecuta, el jefe de lechería supervisa y el veterinario evalúa la salud de las vacas. Un valor fuera del máximo se informa tal cual.",
        f"La leche de vacas en tratamiento no se mezcla con la leche de venta mientras dure el período de resguardo que fija el veterinario. {EMER} {AVISO}",
    ],
    vocab=[("recuento de células somáticas", "indicador de inflamación de la ubre"), ("mastitis", "inflamación de la ubre, que evalúa el veterinario"), ("recuento bacteriano", "indicador de limpieza del ordeño y del equipo"), ("período de resguardo", "tiempo en que la leche de una vaca en tratamiento no se vende"), ("registro de producción", "documento con los litros de cada ordeña"), ("informe del laboratorio", "documento con los resultados de calidad de la leche")],
    worked=[
        ("Comparar con el máximo", "Un informe de ejemplo marca células somáticas 350 y el máximo es 300. ¿Cumple?", ["350 es mayor que 300.", "No cumple."], "No cumple"),
        ("Litros por día", "Un plantel de ejemplo de 50 vacas produce 18 litros por vaca por día. ¿Cuántos litros al día?", ["Se multiplican las vacas por los litros de cada una.", "50 por 18."], "900 litros"),
    ],
    mistakes=[("Mezclar leche de vacas en tratamiento con la de venta «porque es poca».", "Puede llevar restos de medicamentos.", "Se respeta el período de resguardo."),
              ("Creer que el recuento de células somáticas mide la limpieza del equipo.", "Mide la inflamación de la ubre.", "El recuento bacteriano mide la limpieza.")],
    T=[
        ("abc", "En la lechería: ¿qué indica el recuento de células somáticas?", "Si la ubre de la vaca está inflamada", "Si el equipo está limpio", "Cuánta grasa tiene la leche", "El recuento de células somáticas sugiere inflamación de la ubre."),
        ("abc", "En la lechería: ¿qué indica el recuento bacteriano?", "La limpieza del ordeño y del equipo", "La inflamación de la ubre", "El precio de la leche", "El recuento bacteriano sugiere el nivel de higiene."),
        ("abc", "En la lechería: ¿qué es el período de resguardo?", "El tiempo en que la leche de una vaca en tratamiento no se vende", "El tiempo entre dos ordeños", "El tiempo de gestación", "El resguardo evita que la leche con restos de medicamentos llegue al consumidor."),
        ("=", "{F} ¿Cuántas ordeñas hay en una semana de 7 días?", "2*7", "Se multiplican las ordeñas diarias por los días.", " ordeñas"),
        ("abc", "{F} ¿Cumple la leche el máximo de células somáticas?", "Sí, porque 250 es menor que 300", "No, porque 250 es mayor que 300", "No se puede saber", "250 está bajo el máximo de 300."),
        ("abc", "{F} ¿Cumple la leche el máximo de recuento bacteriano?", "Sí, porque 40 es menor que 50", "No, porque 40 es menor que 50", "No se puede saber", "40 está bajo el máximo de 50."),
        ("abc", "{F} ¿Qué documento muestra si el equipo se limpió y quién lo hizo?", "El registro de limpieza del equipo", "El registro de producción", "El informe del laboratorio", "El registro de limpieza guarda esa evidencia."),
        ("abc", "{F} ¿Qué rol evalúa la salud de las vacas?", "El médico veterinario", "El ordeñador", "El jefe de la venta", "El veterinario evalúa la salud de los animales del plantel."),
        ("=", "{F} Si cada vaca produce 20 litros por día, ¿cuántos litros produce el plantel en una semana de 7 días?", "100*20*7", "Se multiplican las vacas, los litros de cada una y los días.", " litros"),
        ("abc", "{F} Un ordeñador dice: «una vaca está en tratamiento, pero su leche es poca, la mezclo con la del tanque». ¿Qué respuesta es correcta?", "Es incorrecto: se respeta el período de resguardo", "Es correcto, porque es poca", "Es correcto, si se mezcla bien", "Los restos de medicamentos pueden llegar al consumidor."),
        ("abc", "{F} El jefe de lechería quiere anotar en el registro de temperatura 4 grados, aunque el tanque marcó 8. ¿Qué corresponde?", "Rechazarlo: se anota el valor real e informa", "Aceptarlo, para que cumpla", "Aceptarlo, si nadie lo revisa", "Alterar un registro oculta un problema."),
        ("abc", "{F} Una vaca se asusta en la sala y patea el equipo de ordeña, que cae cerca de una persona. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Acercarse a levantar el equipo", "Gritar a la vaca", "Un animal asustado es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En la lechería: ¿por qué se registra la producción de cada ordeña?", "Para detectar cambios que señalen problemas de salud o de manejo", "Para evitar el enfriado", "Para reemplazar al laboratorio", "Los cambios en la producción alertan sobre problemas."),
    ],
    ctx=("abc", "Un conocido te pide que firmes como «ordeñador» un registro de limpieza que no hiciste. ¿Qué respondes?", "Que no, porque firmar sin haberlo hecho lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías", "Que sí, solo una vez", "Una firma debe corresponder a algo realizado."),
    sc=[
        ("En la lechería: ¿qué sugiere un recuento bacteriano alto?", "Falta de higiene en el ordeño o el equipo", "El recuento bacteriano refleja la limpieza."),
        ("En la lechería: ¿qué sugiere un recuento de células somáticas alto?", "Inflamación de la ubre", "Ese indicador se asocia a la mastitis."),
        ("En la lechería: ¿quién evalúa la salud de las vacas?", "El médico veterinario", "El veterinario evalúa la salud animal."),
    ],
    op=("Informe de ejemplo de la «Lechería Demo 3»: 60 vacas que producen 25 litros por vaca por día; células somáticas 320 (máximo de ejemplo 300); recuento bacteriano 30 (máximo de ejemplo 50); el tanque marcó 6 grados (objetivo de ejemplo 4). Escribe (a) los litros por día, (b) qué indicador no cumple y por cuánto, (c) qué indica ese indicador, (d) a quién informas.",
        "(a) 60 × 25 = 1.500 litros. (b) Células somáticas: 320 supera 300 por 20. (c) Una posible inflamación de la ubre. (d) Al jefe de lechería y al médico veterinario.",
        ["calcula los litros", "identifica el indicador fuera de rango", "explica qué indica", "informa a quien corresponde"],
        ["hoja con las cuatro respuestas"],
        ["confundir células somáticas con limpieza", "alterar el dato"],
        "Pregunta: «¿qué valor supera su máximo?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los litros por día de 40 vacas que producen 22 litros cada una.",
    extend="Explica con un ejemplo por qué la leche de una vaca en tratamiento no se mezcla con la de venta.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Informes de calidad de tres semanas de la «Lechería Demo». Semana 1: células somáticas 200, recuento bacteriano 30. Semana 2: células somáticas 250, recuento bacteriano 45. Semana 3: células somáticas 350, recuento bacteriano 70. "
     "Máximos de ejemplo: células somáticas 300, recuento bacteriano 50. Observaciones: el registro de limpieza del equipo tiene dos días sin firma; en el tanque la leche tardó 3 horas en enfriarse (máximo de ejemplo 2 horas); tres vacas tienen la ubre inflamada.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso de calidad de la leche con indicadores de varias semanas, a relacionar las observaciones con posibles causas y a derivar al veterinario.",
    prior=["Sé qué son los indicadores de calidad de la leche.", "Sé comparar valores con máximos.", "Sé leer un registro con datos."],
    explain=[
        "Para analizar la calidad de la leche se compara cada indicador con su máximo y se mira la tendencia: si un valor sube semana a semana, el problema crece. Un recuento bacteriano que sube junto a registros de limpieza sin firma y a un enfriado lento apunta a falta de higiene o de frío. Un recuento de células somáticas alto junto a vacas con la ubre inflamada apunta a mastitis, que evalúa el veterinario.",
        "Un buen análisis nombra los datos, la tendencia, las evidencias y a quién se deriva cada hipótesis. El jefe de lechería revisa la limpieza y el enfriado; el veterinario evalúa a las vacas; el técnico de equipos revisa el tanque. Las causas son hipótesis hasta que se confirman. Ninguna decisión sobre medicamentos se toma sin el veterinario.",
        f"Mientras haya un valor fuera de lo permitido, la leche afectada no se entrega sin la decisión del jefe de lechería y del veterinario. {EMER} {AVISO}",
    ],
    vocab=[("tendencia", "dirección en que cambian los valores semana a semana"), ("hipótesis", "explicación posible que aún hay que confirmar"), ("evidencia", "dato del caso que respalda una hipótesis"), ("derivar", "pasar una decisión a quien corresponde"), ("mastitis", "inflamación de la ubre, que evalúa el veterinario")],
    worked=[
        ("Ver la tendencia", "Los recuentos de tres semanas de ejemplo son 30, 40 y 60. ¿Sube o baja?", ["Cada valor es mayor que el anterior.", "Sube."], "Sube"),
        ("Exceso sobre el máximo", "El máximo de ejemplo es 50 y se midió 65. ¿Cuánto lo excede?", ["Se resta el máximo al valor medido.", "65 menos 50."], "15"),
    ],
    mistakes=[("Culpar solo a las vacas sin revisar la limpieza y el frío.", "Varias causas pueden sumarse.", "Se listan todas las evidencias."),
              ("Dar un medicamento a una vaca con la ubre inflamada sin consultar.", "Solo el veterinario puede indicar tratamientos.", "Se informa y se deriva.")],
    T=[
        ("abc", "En la lechería: ¿qué es una tendencia en los indicadores?", "La dirección en que cambian los valores semana a semana", "El promedio de todos los valores", "El máximo permitido", "La tendencia muestra si los valores suben o bajan."),
        ("abc", "En la lechería: ¿qué es una hipótesis?", "Una explicación posible que aún hay que confirmar", "Una causa ya comprobada", "Un dato del laboratorio", "La hipótesis necesita confirmación antes de tomar una decisión."),
        ("abc", "En la lechería: ¿qué significa derivar al veterinario?", "Pasarle la decisión que le corresponde", "Ocultarle el problema", "Tratar a la vaca sin consultar", "Derivar es entregar la decisión a quien corresponde."),
        ("=", "{F} ¿Cuánto superó la semana 3 el máximo de células somáticas?", "350-300", "Se resta el máximo al valor de la semana 3.", " puntos"),
        ("=", "{F} ¿Cuánto superó la semana 3 el máximo de recuento bacteriano?", "70-50", "Se resta el máximo al valor de la semana 3.", " puntos"),
        ("abc", "{F} ¿Cuál es la tendencia del recuento bacteriano en las tres semanas?", "Sube", "Baja", "Se mantiene", "30, 45 y 70 suben semana a semana."),
        ("abc", "{F} ¿Qué evidencia apunta a falta de higiene?", "Dos días sin firma en el registro de limpieza", "La leche es abundante", "El tanque es nuevo", "Un registro de limpieza sin firma sugiere falta de control."),
        ("abc", "{F} ¿Qué evidencia apunta a un problema de frío?", "La leche tardó 3 horas en enfriarse y el máximo es 2", "Hay 100 vacas", "El máximo de células es 300", "El enfriado lento supera el tiempo de ejemplo."),
        ("abc", "{F} ¿A quién se deriva la evaluación de las tres vacas con la ubre inflamada?", "Al médico veterinario", "Al transportista", "Al comprador", "El veterinario evalúa la salud de las vacas."),
        ("abc", "{F} Una compañera dice: «ya sé qué tienen las vacas y les doy un antibiótico». ¿Qué respuesta es correcta?", "Es peligroso: el diagnóstico y el tratamiento los hace el veterinario", "Es correcto, si es poco", "Es correcto, si son tres vacas", "Solo el médico veterinario indica tratamientos a los animales."),
        ("abc", "{F} El jefe de lechería quiere firmar los dos días sin firma del registro de limpieza «para completar». ¿Qué corresponde?", "Rechazarlo: no se firma lo que no se hizo ni se supo", "Aceptarlo, para cumplir", "Aceptarlo, si nadie lo revisa", "Firmar sin saber falsea el registro."),
        ("abc", "{F} Una vaca con la ubre inflamada patea al ordeñador y el equipo cae. ¿Qué corresponde a quien lo observa?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Acercarse a ayudar", "Sujetar a la vaca", "Un animal con dolor es impredecible."),
        ("abc", "En la lechería: ¿por qué conviene analizar la tendencia y no solo el último dato?", "Porque muestra si el problema crece o se corrige", "Porque el último dato es siempre falso", "Porque las tendencias no existen", "La tendencia muestra la evolución del problema."),
    ],
    ctx=("abc", "Un conocido te pide que le digas qué antibiótico usar porque sus vacas tienen la ubre inflamada. ¿Qué respondes?", "Que no puedes indicarlo y que debe consultar a un médico veterinario", "Que use el del vecino", "Que use cualquiera", "Solo un veterinario puede indicar tratamientos."),
    sc=[
        ("En la lechería: ¿qué suele indicar un recuento bacteriano que sube?", "Falta de higiene o de frío", "El recuento bacteriano refleja limpieza y enfriado."),
        ("En la lechería: ¿quién evalúa a las vacas con ubre inflamada?", "El médico veterinario", "El veterinario evalúa la salud animal."),
        ("En la lechería: ¿qué hace falta antes de dar por cierta una causa?", "Confirmarla con el veterinario", "Las causas son hipótesis hasta confirmarlas."),
    ],
    op=("Caso de ejemplo de la «Lechería Demo 4»: células somáticas 280, 310 y 360 en tres semanas (máximo 300); recuento bacteriano 20, 25 y 28 (máximo 50). Observaciones: dos vacas con la ubre inflamada. Escribe (a) cuánto superó la semana 3 el máximo de células somáticas, (b) la tendencia de las células somáticas, (c) el indicador que sí cumple, (d) a quién derivas lo de las dos vacas.",
        "(a) 360 − 300 = 60. (b) Sube. (c) El recuento bacteriano, porque sigue bajo 50. (d) Al médico veterinario.",
        ["calcula el exceso", "describe la tendencia", "identifica el indicador que cumple", "deriva al veterinario"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "indicar un tratamiento"],
        "Pregunta: «¿qué valor de células somáticas aparece en la semana 3?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Escribe una tendencia inventada de tres recuentos que suba y otra que baje.",
    extend="Explica con un ejemplo por qué varias evidencias juntas fortalecen una hipótesis.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La «Lechería Demo» tiene 100 vacas en ordeña que producen 20 litros por día cada una. Precio base de ejemplo: $300 por litro. Bonificación de ejemplo por buena calidad: $20 por litro. "
     "Descuento de ejemplo si las células somáticas superan el máximo: $30 por litro. Tanque de frío de 3.000 litros. Costo de alimentación de ejemplo: $4.000 por vaca por día.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la producción, el ingreso con bonificación o descuento por calidad, y el margen de una lechería.",
    prior=["Sé qué es la calidad de la leche.", "Sé multiplicar y dividir enteros.", "Sé restar enteros."],
    explain=[
        "La producción diaria es el número de vacas por los litros de cada una. El ingreso es los litros por el precio por litro. El precio puede subir con una bonificación si la leche tiene buena calidad, o bajar con un descuento si algún indicador supera el máximo. Por eso cuidar la calidad tiene un valor económico, además del valor sanitario.",
        "El costo de alimentación es el número de vacas por el costo de cada una al día. El margen diario es el ingreso menos el costo. Con estos números se puede comparar un día con buena calidad contra uno con descuento. La capacidad del tanque se compara con la producción para saber si la leche cabe hasta el retiro. Los valores son de ejemplo y las decisiones las toma el jefe de lechería con el veterinario.",
        f"El cálculo no reemplaza el cuidado de las vacas ni de las personas. {EMER} {AVISO}",
    ],
    vocab=[("bonificación", "pago adicional por buena calidad"), ("descuento", "rebaja del pago por no cumplir un indicador"), ("precio base", "precio por litro sin bonificación ni descuento"), ("costo de alimentación", "gasto diario en alimentar a las vacas"), ("margen diario", "ingreso del día menos costo del día")],
    worked=[
        ("Ingreso con bonificación", "Un plantel de ejemplo produce 500 litros a $250 el litro y recibe $10 de bonificación por litro. ¿Cuál es el ingreso?", ["El precio por litro es 250 más 10.", "260 por 500."], "$130.000"),
        ("Margen", "Con un costo de ejemplo de $50.000 al día, ¿cuál es el margen de ese plantel?", ["Margen: ingreso menos costo.", "130.000 menos 50.000."], "$80.000"),
    ],
    mistakes=[("Olvidar que el descuento por calidad se aplica a todos los litros.", "El descuento es por litro y se multiplica por la producción.", "Se calcula el nuevo precio por litro y se multiplica."),
              ("Ahorrar en alimentación para subir el margen.", "Una mala alimentación daña la salud y la producción.", "Se respeta la ración que define el nutricionista.")],
    T=[
        ("abc", "En la lechería: ¿qué es la bonificación por calidad?", "Un pago adicional por leche de buena calidad", "Un descuento por baja calidad", "El precio de las vacas", "La bonificación premia la buena calidad con un pago adicional."),
        ("abc", "En la lechería: ¿qué es el precio base?", "El precio por litro sin bonificación ni descuento", "El precio de venta de una vaca", "El costo del tanque", "El precio base es el punto de partida."),
        ("abc", "En la lechería: ¿qué es el margen diario?", "El ingreso del día menos el costo del día", "El costo del día más el ingreso", "La producción de una vaca", "El margen resta los costos del ingreso."),
        ("=", "{F} ¿Cuántos litros produce el plantel al día?", "100*20", "Se multiplican las vacas por los litros de cada una.", " litros"),
        ("=", "{F} ¿Cuál es el ingreso diario con precio base y buena calidad (precio base más bonificación)?", "100*20*(300+20)", "Se multiplican los litros por el precio base más la bonificación.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso diario si las células somáticas superan el máximo (precio base menos descuento)?", "100*20*(300-30)", "Se multiplican los litros por el precio base menos el descuento.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más ingresa un día con buena calidad que un día con descuento?", "100*20*(300+20)-100*20*(300-30)", "Se resta el ingreso con descuento al ingreso con bonificación.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de alimentación del día?", "100*4000", "Se multiplican las vacas por el costo de cada una al día.", " pesos"),
        ("=", "{F} ¿Cuál es el margen diario con buena calidad?", "100*20*(300+20)-100*4000", "Se resta el costo de alimentación al ingreso con bonificación.", " pesos"),
        ("abc", "{F} Un jefe propone reducir a la mitad la ración de las vacas para subir el margen. ¿Qué corresponde?", "Rechazarlo: la ración la define el nutricionista y una ración insuficiente daña la salud", "Aceptarlo, para ahorrar", "Aceptarlo, si es por una semana", "Una mala alimentación daña a los animales y baja la producción."),
        ("abc", "{F} Una estudiante quiere ayudar con el ordeño porque ya sabe calcular el ingreso. ¿Qué corresponde?", "Rechazarlo: el ordeño lo hace personal capacitado y autorizado", "Aceptarlo, si va con un adulto", "Aceptarlo, si usa guantes", "Calcular valores no habilita para ordeñar a los animales."),
        ("=", "{F} Si el retiro de la leche fuera cada 2 días con el tanque vacío al comienzo, ¿cuántos litros no cabrían en el tanque de 3.000 litros?", "2*100*20-3000", "Se calcula la producción de 2 días y se resta la capacidad del tanque.", " litros"),
        ("abc", "En la lechería: ¿por qué cuidar la calidad tiene valor económico?", "Porque la bonificación sube el ingreso y el descuento lo baja", "Porque la calidad no se paga", "Porque solo importa el volumen", "El precio por litro cambia con la calidad."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene invertir en mejorar la calidad de la leche y te da solo el costo. ¿Qué respondes?", "Que faltan la producción y la bonificación esperada, y que lo evalúa un asesor", "Que sí, siempre", "Que no, nunca", "Sin ingresos esperados no se puede comparar."),
    sc=[
        ("En la lechería: ¿cómo se calcula el ingreso diario?", "Litros por precio por litro", "El ingreso multiplica producción y precio."),
        ("En la lechería: ¿qué pasa con el precio si las células somáticas superan el máximo?", "Baja por un descuento", "El descuento reduce el pago por litro."),
        ("En la lechería: ¿cómo se calcula el margen diario?", "Ingreso menos costo", "El margen es lo que queda después de pagar costos."),
    ],
    op=("Datos de ejemplo de la «Lechería Demo 5»: 50 vacas que producen 24 litros por día; precio base $280; bonificación $15 por litro; costo de alimentación $3.500 por vaca por día. Escribe (a) la producción diaria, (b) el ingreso con bonificación, (c) el costo de alimentación, (d) el margen diario.",
        "(a) 50 × 24 = 1.200 litros. (b) 1.200 × (280 + 15) = $354.000. (c) 50 × 3.500 = $175.000. (d) 354.000 − 175.000 = $179.000.",
        ["calcula la producción", "calcula el ingreso", "calcula el costo", "calcula el margen"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la bonificación", "no restar el costo"],
        "Pregunta: «¿qué precio por litro resulta de sumar la bonificación al precio base?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el ingreso de 800 litros a $260 el litro.",
    extend="Explica con un ejemplo por qué una buena higiene puede mejorar el ingreso.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Plantel Demo 2» cría 200 ovinos. Su plan sanitario lo diseña un médico veterinario e incluye vacunas, controles de parásitos y reglas de higiene. "
     "Peligros anotados: animales asustados que empujan o patean, agujas y otros elementos cortopunzantes, productos de uso veterinario, contacto con fluidos y partos (zoonosis), y animales nuevos que pueden traer enfermedades al plantel.")
build(
    O5, 1, F,
    use="Aprenderé qué son un plan sanitario y el bienestar animal, las cinco libertades, la cuarentena y por qué los tratamientos solo los indica el veterinario.",
    prior=["Sé qué es el bienestar animal.", "Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita."],
    explain=[
        "Un plan sanitario es el conjunto de acciones que previenen y controlan las enfermedades de los animales de un plantel: vacunas, control de parásitos, higiene y bioseguridad. Lo diseña el médico veterinario según la especie, la edad y la etapa del ciclo de vida. La prevención es mejor que el tratamiento. La cuarentena es el aislamiento de animales nuevos o enfermos para evitar contagiar al resto.",
        "El bienestar animal se evalúa con cinco libertades: libres de hambre y sed; de incomodidad; de dolor, lesión y enfermedad; libres para expresar su comportamiento normal; y libres de miedo y angustia. Los tratamientos curativos sencillos, sin cirugía, solo los indica el veterinario, con receta, y se respeta el período de resguardo del producto. Los cortopunzantes, como las agujas, y los productos veterinarios los maneja solo personal capacitado.",
        f"La zoonosis, enfermedad que pasa de los animales a las personas, se previene con higiene y ropa de trabajo. {EMER} {AVISO}",
    ],
    vocab=[("plan sanitario", "acciones que previenen y controlan enfermedades en un plantel"), ("cuarentena", "aislamiento de animales nuevos o enfermos para no contagiar al resto"), ("cinco libertades", "criterios para evaluar el bienestar de un animal"), ("receta veterinaria", "indicación escrita del veterinario para un producto"), ("cortopunzante", "elemento que corta o pincha, como una aguja"), ("período de resguardo", "tiempo en que no se aprovechan productos de un animal tratado"), ("zoonosis", "enfermedad que pasa de los animales a las personas")],
    worked=[
        ("Una libertad", "Un corral de ejemplo no tiene agua en los bebederos. ¿Qué libertad se afecta?", ["Los animales no pueden beber.", "Se afecta la libertad de hambre y sed."], "Libres de hambre y sed"),
        ("Clasificar un control", "Un plantel de ejemplo instala un lavamanos fijo con agua a la entrada del corral de aislamiento. ¿Qué tipo de control es?", ["El lavamanos fijo cambia físicamente el lugar.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que un animal con tos se puede medicar «con lo que sobró».", "Solo el médico veterinario indica tratamientos a los animales.", "Se avisa al encargado y al veterinario."),
              ("Creer que una aguja usada se deja en cualquier basurero.", "Puede pinchar a otra persona.", "Se guardan en un recipiente seguro, según la norma vigente.")],
    T=[
        ("abc", "En el plan sanitario: ¿qué es la cuarentena?", "El aislamiento de animales nuevos o enfermos para no contagiar al resto", "La vacunación de todos los animales", "El pesaje de los animales", "La cuarentena aísla para evitar contagios."),
        ("abc", "En el plan sanitario: ¿qué son las cinco libertades?", "Criterios para evaluar el bienestar de un animal", "Cinco vacunas obligatorias", "Cinco corrales del plantel", "Las cinco libertades evalúan el bienestar."),
        ("abc", "En el plan sanitario: ¿qué es una receta veterinaria?", "La indicación escrita del veterinario para un producto", "Un registro de producción", "Un permiso de transporte", "La receta autoriza un producto indicado por el veterinario."),
        ("=", "{F} Si en el plan sanitario se vacuna el 90 % de los ovinos, ¿cuántos ovinos se vacunan?", "200*90//100", "Se calcula el porcentaje sobre el total de ovinos.", " ovinos"),
        ("abc", "{F} Guardar las agujas usadas en un recipiente rígido con tapa y llave es un control de tipo:", "De ingeniería, porque cambia el lugar y el acceso", "Administrativo, porque es una regla", "De EPP, porque protege a quien las usa", "El recipiente es un elemento físico que funciona siempre."),
        ("abc", "{F} Una regla que dice «solo personal autorizado maneja agujas y productos veterinarios» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el producto", "De sustitución, porque cambia al personal", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a las agujas usadas?", "Que una persona se pinche y se infecte", "La aguja misma", "Que falte espacio", "El riesgo es la posibilidad de daño; la aguja usada es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí el plan sanitario, así que vacuno a un ovino con una aguja del plantel». ¿Qué respuesta es correcta?", "Es peligroso: los productos los maneja personal capacitado y autorizado", "Es correcto, si usa guantes", "Es correcto, si el ovino es manso", "Los cortopunzantes y los productos exigen formación."),
        ("abc", "{F} Durante una visita, un ovino enfermo se desploma y patalea. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Levantarlo tú", "Darle un medicamento", "Un animal enfermo y asustado es impredecible."),
        ("abc", "En el plan sanitario: ¿por qué se aísla en cuarentena a un animal nuevo?", "Porque podría traer una enfermedad y contagiar al resto", "Porque necesita dormir más", "Porque pesa menos", "La cuarentena evita contagios mientras se observa al animal."),
        ("abc", "{F} Se propone solo entregar guantes para prevenir pinchazos. ¿Qué medida es más efectiva?", "Guardar y desechar las agujas en recipientes seguros y que las maneje personal capacitado", "Entregar guantes más gruesos", "Pedir mayor cuidado", "Reducir la exposición actúa sobre el peligro."),
        ("=", "{F} Si cada vacuna de ejemplo cuesta $500 por animal, ¿cuánto cuesta vacunar a todo el plantel?", "200*500", "Se multiplica el número de animales por el costo de cada vacuna.", " pesos"),
        ("abc", "En el plan sanitario: ¿por qué un animal con dolor afecta el bienestar?", "Porque no está libre de dolor, lesión y enfermedad", "Porque come más", "Porque se vuelve más pesado", "El dolor es una de las libertades que se evalúan."),
    ],
    ctx=("abc", "Un vecino te pide que le pongas una inyección a una oveja enferma «porque ya viste cómo se hace». ¿Qué respondes?", "Que no, porque exige formación, receta y autorización, y que lo consultarás con un adulto responsable", "Que sí, una sola vez", "Que sí, con aguja nueva", "Haber visto el concepto no habilita para tratar animales."),
    sc=[
        ("En el plan sanitario: ¿quién diseña el plan sanitario?", "El médico veterinario", "El veterinario conoce las enfermedades y la especie."),
        ("En el plan sanitario: ¿qué es una zoonosis?", "Una enfermedad que pasa de los animales a las personas", "La zoonosis se previene con higiene."),
        ("En el plan sanitario: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
    ],
    op=("El «Plantel Demo 3» anota una tarea de ejemplo: desechar agujas usadas en una bolsa común junto a la basura, y guardar el producto veterinario sin rótulo en una repisa baja al alcance de cualquiera. Escribe (a) el peligro de las agujas y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a un animal enfermo caído y asustado.",
        "(a) Peligro: agujas usadas en una bolsa común; riesgo: que alguien se pinche y se infecte. (b) Una regla de que solo personal autorizado maneja agujas y productos. (c) Un recipiente rígido con tapa y llave para las agujas, y una bodega cerrada para los productos. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer manejar las agujas", "proponer tratar al animal"],
        "Pregunta: «¿qué control evita el pinchazo aunque nadie se acuerde de la regla?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Escribe las cinco libertades del bienestar animal y un ejemplo inventado de cuando se afecta una.",
    extend="Explica con un ejemplo por qué prevenir una enfermedad cuesta menos que tratarla.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (calendario y registros de ejemplo, inventados). Plan sanitario del «Plantel Demo 2» para 200 ovinos. Calendario de ejemplo: mes 3, vacunación A para todos; mes 6, control de parásitos; mes 9, revisión del veterinario. "
     "Vacunación del mes 3: se vacunaron 190 de los 200 ovinos. Registro de tratamientos de ejemplo: ovino O-14, tratado el día 40 del año por indicación del veterinario con un producto cuyo período de resguardo es de 14 días. "
     "Documentos: el calendario sanitario, el registro de tratamientos, la receta veterinaria y la ficha de cada animal. Roles: médico veterinario, encargado sanitario y auxiliar.")
build(
    O5, 2, F,
    use="Aprenderé a leer un calendario y un registro sanitario, a calcular la cobertura de vacunación y el fin de un período de resguardo, y a conocer los roles del plan sanitario.",
    prior=["Sé qué son un plan sanitario y el bienestar animal.", "Sé calcular porcentajes enteros.", "Sé sumar enteros."],
    explain=[
        "El calendario sanitario fija cuándo se hace cada acción preventiva. La cobertura de vacunación es el porcentaje de animales vacunados sobre el total: se divide los vacunados entre el total y se multiplica por 100. Una cobertura baja deja animales sin protección. El registro de tratamientos anota fecha, animal, producto, indicación y responsable, y el período de resguardo.",
        "El período de resguardo es el tiempo, después de un tratamiento, en que no se aprovechan los productos del animal, como la leche o la carne, porque pueden tener restos del producto. Para saber cuándo termina, se suma el resguardo a la fecha del tratamiento. La receta veterinaria autoriza el producto, la ficha del animal resume su historia, y el encargado sanitario lleva los registros. El veterinario indica y el auxiliar apoya sin tratar por cuenta propia.",
        f"Un registro sanitario no se altera ni se completa de memoria. {EMER} {AVISO}",
    ],
    vocab=[("calendario sanitario", "documento que fija cuándo se hace cada acción preventiva"), ("cobertura de vacunación", "porcentaje de animales vacunados sobre el total"), ("registro de tratamientos", "documento que anota fecha, animal, producto, indicación y responsable"), ("ficha del animal", "documento que resume la historia de un animal"), ("encargado sanitario", "persona que lleva los registros sanitarios"), ("período de resguardo", "tiempo después del tratamiento en que no se aprovechan los productos del animal")],
    worked=[
        ("Cobertura", "En un plantel de ejemplo se vacunan 45 de 50 animales. ¿Cuál es la cobertura?", ["Se divide 45 entre 50.", "45 de 50 equivale a 90 de 100."], "90 %"),
        ("Fin del resguardo", "Un animal de ejemplo se trató el día 30 y el resguardo es de 10 días. ¿Cuándo termina?", ["Se suma el resguardo a la fecha del tratamiento.", "30 más 10."], "El día 40"),
    ],
    mistakes=[("Aprovechar los productos del animal el mismo día en que termina el tratamiento.", "El resguardo debe cumplirse completo.", "Se cuenta el resguardo desde la fecha del tratamiento."),
              ("Anotar la vacunación de animales que no se vacunaron.", "Se falsea el registro y se deja a animales sin protección.", "Se anota solo lo realizado.")],
    T=[
        ("abc", "En el plan sanitario: ¿qué es la cobertura de vacunación?", "El porcentaje de animales vacunados sobre el total", "El número de vacunas que caben en una caja", "El precio de la vacuna", "La cobertura relaciona vacunados y total."),
        ("abc", "En el plan sanitario: ¿qué es el calendario sanitario?", "El documento que fija cuándo se hace cada acción preventiva", "El registro de los tratamientos ya hechos", "La receta de un producto", "El calendario programa las acciones preventivas de todo el año."),
        ("abc", "En el plan sanitario: ¿qué es el período de resguardo?", "El tiempo después del tratamiento en que no se aprovechan los productos del animal", "El tiempo entre dos vacunas", "El tiempo de gestación", "El resguardo protege al consumidor de restos de productos."),
        ("=", "{F} ¿Cuál es la cobertura de vacunación del mes 3, en porcentaje?", "190*100//200", "Se divide los vacunados entre el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos ovinos quedaron sin vacunar en el mes 3?", "200-190", "Se resta al total los ovinos vacunados.", " ovinos"),
        ("=", "{F} ¿En qué día del año termina el período de resguardo del ovino O-14?", "40+14", "Se suma el resguardo a la fecha del tratamiento.", " (día del año)"),
        ("abc", "{F} ¿Qué documento anota fecha, animal, producto y responsable de cada tratamiento?", "El registro de tratamientos", "El calendario sanitario", "La ficha del animal", "El registro de tratamientos guarda esos datos."),
        ("abc", "{F} ¿Qué rol indica los tratamientos?", "El médico veterinario", "El auxiliar", "El encargado de las ventas", "Los tratamientos los indica el veterinario."),
        ("abc", "{F} ¿Qué acción del calendario se hace en el mes 6?", "El control de parásitos", "La vacunación A", "La revisión del veterinario", "El calendario asigna el control de parásitos al mes 6."),
        ("abc", "{F} Un auxiliar dice: «el ovino O-14 se ve sano, aprovecho su carne el día 45». ¿Qué respuesta es correcta?", "Es incorrecto: el resguardo termina el día 54", "Es correcto, porque ya pasaron 5 días", "Es correcto, si se ve sano", "Aunque se vea sano, el resguardo debe cumplirse completo."),
        ("abc", "{F} El encargado sanitario quiere anotar que se vacunaron los 200 ovinos, aunque quedaron 10 sin vacunar, «para cumplir». ¿Qué corresponde?", "Rechazarlo: se anota solo lo realizado e informa", "Aceptarlo, para cumplir el plan", "Aceptarlo, si nadie lo revisa", "Falsear el registro deja animales sin protección."),
        ("abc", "{F} Un ovino se asusta durante el pesaje y empuja a una persona contra el cerco. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Acercarse a calmar al ovino", "Tirar a la persona hacia ti", "Un animal asustado es impredecible; se avisa a quienes pueden actuar."),
        ("abc", "En el plan sanitario: ¿por qué una cobertura de vacunación baja es un problema?", "Porque deja animales sin protección y expone al plantel", "Porque ahorra vacunas", "Porque aumenta el peso", "Los animales sin vacunar pueden enfermar y contagiar."),
    ],
    ctx=("abc", "Un conocido te pide que firmes en el registro que un animal fue tratado cuando no estabas presente. ¿Qué respondes?", "Que no, porque firmar sin haber visto lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si confías", "Que sí, solo una vez", "Una firma debe certificar algo que viste."),
    sc=[
        ("En el plan sanitario: ¿cómo se calcula la cobertura de vacunación?", "Vacunados entre total, por 100", "La cobertura es un porcentaje del total."),
        ("En el plan sanitario: ¿cómo se calcula el fin de un resguardo?", "Fecha del tratamiento más los días de resguardo", "El resguardo se suma a la fecha del tratamiento."),
        ("En el plan sanitario: ¿quién lleva los registros sanitarios?", "El encargado sanitario", "El encargado sanitario registra lo realizado."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 4»: 80 animales; se vacunan 72; un animal se trata el día 100 del año con un resguardo de 12 días. Escribe (a) la cobertura de vacunación, (b) cuántos animales quedan sin vacunar, (c) el día en que termina el resguardo, (d) qué documento anota el tratamiento.",
        "(a) 72 × 100 ÷ 80 = 90 %. (b) 80 − 72 = 8 animales. (c) 100 + 12 = día 112. (d) El registro de tratamientos.",
        ["calcula la cobertura", "calcula los no vacunados", "calcula el fin del resguardo", "nombra el documento"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por 100", "no sumar el resguardo"],
        "Pregunta: «¿cuántos vacunados hay entre el total?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la cobertura de 120 animales con 108 vacunados.",
    extend="Explica con un ejemplo por qué el período de resguardo protege a quien consume los productos.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (observaciones de ejemplo, inventadas). En el «Plantel Demo 2» se anotaron estas observaciones: A, los bebederos de un corral amanecen vacíos; B, un corral sin sombra con 33 grados al mediodía; C, cuatro ovinos cojean; "
     "D, los animales de un corral no tienen espacio para echarse todos a la vez; E, un grupo está muy asustado por un perro suelto. Libertades: 1, libres de hambre y sed; 2, libres de incomodidad; 3, libres de dolor, lesión y enfermedad; 4, libres para expresar su comportamiento normal; 5, libres de miedo y angustia.")
build(
    O5, 3, F,
    use="Aprenderé a analizar un caso de bienestar animal asociando cada observación con una libertad, a priorizar y a decidir a quién se informa sin tratar a ningún animal.",
    prior=["Sé qué son las cinco libertades.", "Sé qué es un plan sanitario.", "Sé leer una lista de observaciones."],
    explain=[
        "Para analizar el bienestar se asocia cada observación con la libertad que afecta. Un bebedero vacío afecta la libertad de hambre y sed. Un corral sin sombra con mucho calor afecta la libertad de incomodidad. Una cojera es dolor o lesión. La falta de espacio para echarse afecta el comportamiento normal. El miedo, por ejemplo ante un perro suelto, afecta la libertad de miedo y angustia.",
        "Luego se prioriza: lo que causa daño inmediato, como la falta de agua con calor, se atiende primero. Cada observación se informa a quien corresponde: el encargado corrige agua, sombra, espacio y presencia del perro; el veterinario evalúa las cojeras. Las acciones que implican manejar animales o aplicar productos las hace personal capacitado. Un buen análisis nombra la observación, la libertad, la prioridad y el responsable.",
        f"Quien analiza no trata a los animales ni los maneja: informa. {EMER} {AVISO}",
    ],
    vocab=[("observación", "dato que se ve en el plantel"), ("libertad afectada", "libertad del bienestar que se ve dañada"), ("prioridad", "orden en que se atiende cada problema"), ("cojera", "dificultad para caminar por dolor o lesión"), ("responsable", "persona a cargo de corregir un problema")],
    worked=[
        ("Asociar con una libertad", "Un animal de ejemplo tiene la piel con costras y se rasca todo el día. ¿Qué libertad afecta?", ["La enfermedad de la piel causa molestia y lesión.", "Afecta la libertad de dolor, lesión y enfermedad."], "Libres de dolor, lesión y enfermedad"),
        ("Priorizar", "En un plantel de ejemplo hay falta de agua con calor y un corral algo sucio. ¿Qué se atiende primero?", ["La falta de agua con calor causa daño inmediato.", "Se atiende primero la falta de agua."], "La falta de agua"),
    ],
    mistakes=[("Atender primero lo más cómodo de arreglar.", "Lo que causa daño inmediato debe ir primero.", "Se prioriza por gravedad."),
              ("Tratar la cojera de un ovino por cuenta propia.", "Solo el veterinario puede evaluar y tratar.", "Se informa y se deriva.")],
    T=[
        ("abc", "En el bienestar animal: ¿qué es una prioridad?", "El orden en que se atiende cada problema", "El nombre del corral", "El tipo de alimento", "La prioridad ordena la atención de los problemas por gravedad."),
        ("abc", "En el bienestar animal: ¿qué es una cojera?", "La dificultad para caminar por dolor o lesión", "La falta de apetito", "Un exceso de lana", "La cojera señala dolor o lesión."),
        ("abc", "En el bienestar animal: ¿qué libertad afecta la falta de agua?", "Libres de hambre y sed", "Libres de miedo y angustia", "Libres para expresar su comportamiento normal", "La falta de agua es sed."),
        ("abc", "{F} ¿Qué libertad afecta la observación A, bebederos vacíos?", "La libertad 1, libres de hambre y sed", "La libertad 2, libres de incomodidad", "La libertad 5, libres de miedo y angustia", "Sin agua en los bebederos los animales sufren sed."),
        ("abc", "{F} ¿Qué libertad afecta la observación B, corral sin sombra con 33 grados?", "La libertad 2, libres de incomodidad", "La libertad 1, hambre y sed", "La libertad 3, dolor", "El calor sin sombra incomoda a los animales."),
        ("abc", "{F} ¿Qué libertad afecta la observación C, cuatro ovinos cojean?", "La libertad 3, libres de dolor, lesión y enfermedad", "La libertad 4, comportamiento normal", "La libertad 5, miedo", "La cojera es dolor o lesión."),
        ("abc", "{F} ¿Qué libertad afecta la observación D, falta de espacio para echarse?", "La libertad 4, libres para expresar su comportamiento normal", "La libertad 1, hambre y sed", "La libertad 3, enfermedad", "Echarse es un comportamiento normal que no pueden realizar."),
        ("abc", "{F} ¿Qué libertad afecta la observación E, el perro suelto?", "La libertad 5, libres de miedo y angustia", "La libertad 2, incomodidad", "La libertad 4, comportamiento normal", "El perro asusta a los animales."),
        ("=", "{F} Si cojean 4 de 200 ovinos, ¿qué porcentaje del plantel cojea?", "4*100//200", "Se divide los ovinos con cojera entre el total y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué observación se atiende primero por causar daño inmediato?", "La A y la B, por la sed y el calor", "La D, por el espacio", "La E, por el perro", "La falta de agua con calor puede dañar rápido a los animales."),
        ("abc", "{F} Una estudiante dice: «puedo darles un analgésico a los cuatro ovinos que cojean». ¿Qué respuesta es correcta?", "Es peligroso: el diagnóstico y el tratamiento los hace el veterinario", "Es correcto, si es poca dosis", "Es correcto, si cojean poco", "Solo el médico veterinario indica tratamientos a los animales."),
        ("abc", "{F} Un perro suelto corre hacia el corral y los animales se agolpan contra el cerco. ¿Qué corresponde a quien lo observa?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Entrar al corral a calmar a los animales", "Perseguir al perro", "Animales agolpados pueden aplastar a una persona."),
        ("abc", "En el bienestar animal: ¿por qué conviene priorizar lo que causa daño inmediato?", "Porque el daño inmediato empeora rápido", "Porque lo urgente es siempre fácil", "Porque lo demás no importa", "El daño inmediato exige acción primero."),
    ],
    ctx=("abc", "Un conocido te muestra que sus ovinos cojean y te pide el nombre de un medicamento. ¿Qué respondes?", "Que no puedes indicarlo y que debe consultar a un veterinario", "Que use el del vecino", "Que les dé vitaminas", "Solo el veterinario puede evaluar y tratar."),
    sc=[
        ("En el bienestar animal: ¿qué libertad afecta el calor sin sombra?", "Libres de incomodidad", "El calor excesivo incomoda a los animales."),
        ("En el bienestar animal: ¿quién evalúa una cojera?", "El médico veterinario", "El veterinario diagnostica el estado de salud del animal."),
        ("En el bienestar animal: ¿qué se hace primero ante una falta de agua con calor?", "Se atiende de inmediato", "El daño inmediato tiene prioridad sobre los demás problemas."),
    ],
    op=("Observaciones de ejemplo del «Plantel Demo 5»: A, los comederos están vacíos; B, tres animales tienen una herida; C, un corral sin sombra con 35 grados; D, los animales están asustados por una máquina cercana. Libertades: 1, hambre y sed; 2, incomodidad; 3, dolor, lesión y enfermedad; 4, comportamiento normal; 5, miedo y angustia. Escribe (a) la libertad que afecta cada observación, (b) cuál atiendes primero y por qué, (c) a quién derivas las heridas, (d) qué haces si un animal se desploma frente a ti.",
        "(a) A: 1; B: 3; C: 2; D: 5. (b) La A y la C, por el daño inmediato de hambre y calor. (c) Al médico veterinario. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["asocia bien las libertades", "prioriza con razón", "deriva al veterinario", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["asociar mal una libertad", "tratar las heridas"],
        "Pregunta: «¿qué libertad se afecta cuando un animal tiene una herida?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Asocia cada observación inventada con una libertad: comederos vacíos, corral muy estrecho y animal asustado.",
    extend="Explica con un ejemplo por qué el miedo también es un problema de bienestar.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). El «Plantel Demo 2» tiene 200 ovinos. Sin plan sanitario completo: se enferma el 10 % y mueren 5 animales. Con plan sanitario completo: se enferma el 3 % y muere 1 animal. "
     "Valor de ejemplo de cada animal: $60.000. Costo del plan sanitario de ejemplo: $500 por animal por año.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular animales enfermos y perdidos, el costo del plan sanitario y el ahorro de prevenir.",
    prior=["Sé qué es un plan sanitario.", "Sé calcular porcentajes enteros.", "Sé multiplicar y restar enteros."],
    explain=[
        "El número de animales enfermos es el porcentaje de enfermos aplicado al total. Los animales perdidos son los que mueren. El valor de las pérdidas es los animales perdidos por su valor. El costo del plan es el número de animales por el costo por animal. El ahorro de prevenir es la pérdida sin plan menos la pérdida con plan, menos el costo del plan.",
        "Con estos cálculos se compara si el plan conviene económicamente. Pero un plan sanitario no se evalúa solo por dinero: cuida el bienestar de los animales y la salud de las personas, evitando zoonosis. Los valores son de ejemplo, y las decisiones las toma el veterinario con el encargado del plantel.",
        f"Prevenir no incluye medicar por cuenta propia: los productos los indica el veterinario. {EMER} {AVISO}",
    ],
    vocab=[("animales enfermos", "porcentaje de enfermos aplicado al total"), ("animales perdidos", "animales que mueren"), ("valor de las pérdidas", "animales perdidos por su valor"), ("costo del plan", "animales por el costo por animal"), ("ahorro de prevenir", "pérdida sin plan menos pérdida con plan, menos costo del plan")],
    worked=[
        ("Animales enfermos", "Un plantel de ejemplo tiene 100 animales y se enferma el 5 %. ¿Cuántos se enferman?", ["Se calcula el 5 % de 100.", "5 por 100 entre 100."], "5 animales"),
        ("Valor de pérdidas", "Se pierden 2 animales de ejemplo que valen $50.000 cada uno. ¿Cuánto es la pérdida?", ["Se multiplican los animales por su valor.", "2 por 50.000."], "$100.000"),
    ],
    mistakes=[("Olvidar restar el costo del plan al ahorro.", "Prevenir también cuesta.", "Se resta el costo del plan."),
              ("Medir el plan solo por el dinero ahorrado.", "También importan el bienestar y la salud de las personas.", "Se consideran todos los beneficios.")],
    T=[
        ("abc", "En el plan sanitario: ¿qué es el valor de las pérdidas?", "Los animales perdidos por su valor", "El costo del plan", "El precio de una vacuna", "El valor de las pérdidas multiplica animales perdidos por valor."),
        ("abc", "En el plan sanitario: ¿qué es el ahorro de prevenir?", "La pérdida sin plan menos la pérdida con plan, menos el costo del plan", "El costo del plan más las pérdidas", "El valor de un animal", "El ahorro resta el costo del plan de lo que se evita perder."),
        ("abc", "En el plan sanitario: ¿por qué un plan no se evalúa solo por dinero?", "Porque también cuida el bienestar animal y la salud de las personas", "Porque el dinero no importa", "Porque no tiene costo", "El plan protege más allá del ahorro."),
        ("=", "{F} ¿Cuántos ovinos se enferman sin plan sanitario?", "200*10//100", "Se calcula el porcentaje de enfermos sobre el total.", " ovinos"),
        ("=", "{F} ¿Cuántos ovinos se enferman con plan sanitario?", "200*3//100", "Se calcula el porcentaje de enfermos sobre el total.", " ovinos"),
        ("=", "{F} ¿Cuál es la pérdida en pesos por los 5 animales muertos sin plan?", "5*60000", "Se multiplican los animales perdidos por su valor.", " pesos"),
        ("=", "{F} ¿Cuál es la pérdida en pesos por el animal muerto con plan?", "1*60000", "Se multiplican los animales perdidos por su valor.", " pesos"),
        ("=", "{F} ¿Cuál es el costo anual del plan sanitario?", "200*500", "Se multiplican los animales por el costo por animal.", " pesos"),
        ("=", "{F} ¿Cuál es el ahorro de prevenir, descontando el costo del plan?", "5*60000-1*60000-200*500", "Se resta la pérdida con plan y el costo del plan a la pérdida sin plan.", " pesos"),
        ("abc", "{F} Un encargado propone eliminar el plan sanitario para ahorrar $100.000. ¿Qué corresponde?", "Rechazarlo: el plan ahorra más de lo que cuesta y cuida el bienestar", "Aceptarlo, porque cuesta", "Aceptarlo, si no hay enfermos hoy", "Los números de ejemplo muestran que prevenir conviene."),
        ("abc", "{F} Una estudiante quiere vacunar a los animales con una aguja del plantel porque ya sabe calcular el ahorro. ¿Qué corresponde?", "Rechazarlo: la vacunación la hace personal capacitado y autorizado", "Aceptarlo, si usa guantes", "Aceptarlo, si va con un adulto", "Calcular el ahorro no habilita para aplicar productos."),
        ("=", "{F} Si el plan costara $700 por animal, ¿cuál sería su costo anual?", "200*700", "Se multiplican los animales por el nuevo costo por animal.", " pesos"),
        ("abc", "En el plan sanitario: ¿por qué prevenir cuesta menos que tratar muchas enfermedades?", "Porque evita pérdidas, tratamientos y sufrimiento", "Porque nunca hay enfermedades", "Porque los animales no se enferman", "Prevenir evita pérdidas mayores de animales y de dinero."),
    ],
    ctx=("abc", "Un conocido te pregunta si le conviene gastar en un plan sanitario y te da solo el costo. ¿Qué respondes?", "Que faltan las pérdidas esperadas sin plan y con plan, y que lo evalúa un veterinario", "Que sí, siempre", "Que no, nunca", "Sin pérdidas esperadas no se puede comparar."),
    sc=[
        ("En el plan sanitario: ¿cómo se calcula el costo del plan?", "Animales por costo por animal", "El costo se multiplica por el número de animales."),
        ("En el plan sanitario: ¿qué se resta para el ahorro de prevenir?", "La pérdida con plan y el costo del plan", "El ahorro es lo que queda tras restar lo que cuesta prevenir."),
        ("En el plan sanitario: ¿cómo se calcula el valor de las pérdidas?", "Animales perdidos por su valor", "Se multiplican los animales por su valor."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 6»: 100 animales; sin plan: se pierden 4 animales; con plan: se pierde 1; valor de $50.000 por animal; plan de $400 por animal. Escribe (a) la pérdida sin plan, (b) la pérdida con plan, (c) el costo del plan, (d) el ahorro de prevenir.",
        "(a) 4 × 50.000 = $200.000. (b) 1 × 50.000 = $50.000. (c) 100 × 400 = $40.000. (d) 200.000 − 50.000 − 40.000 = $110.000.",
        ["calcula la pérdida sin plan", "calcula la pérdida con plan", "calcula el costo del plan", "calcula el ahorro"],
        ["hoja con las cuatro respuestas"],
        ["no restar el costo del plan", "multiplicar mal"],
        "Pregunta: «¿qué se multiplica por el valor de cada animal?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la pérdida de 3 animales que valen $40.000 cada uno.",
    extend="Explica con un ejemplo por qué la prevención también protege a las personas.",
)

# ============================================================ OAM-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Fundo Demo 6» cultiva 10 hectáreas de alfalfa para hacer heno (forraje seco, en fardos) y 5 hectáreas de maíz para hacer ensilaje (forraje picado y conservado en un silo cerrado). "
     "Peligros anotados: maquinaria que corta, rastrilla y enfarda; fardos muy pesados apilados en altura; calentamiento y posible incendio de heno guardado húmedo; gases que se forman dentro del silo; polvo y esporas de hongos; y trabajo con el sol fuerte.")
build(
    O6, 1, F,
    use="Aprenderé qué son los forrajes, el heno y el ensilaje, por qué se conservan y cuáles son los peligros del cultivo y la conservación de forrajes.",
    prior=["Sé qué es un cultivo y una cosecha.", "Sé qué es un peligro y un riesgo.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Un forraje es una planta que se cultiva o se cosecha para alimentar animales, como la alfalfa o el maíz. Se usa fresco, pastoreado, o se conserva para tener alimento cuando falta pasto. El heno es forraje cortado y secado hasta que casi no tenga agua, y se guarda en fardos. El ensilaje es forraje picado y almacenado sin aire en un silo, donde fermenta y se conserva. Conservar forraje cuida la alimentación de los animales todo el año.",
        "El trabajo con forrajes tiene peligros. La maquinaria que corta y enfarda atrapa y corta; los fardos pesados pueden caer y aplastar; el heno guardado húmedo se calienta y puede incendiarse solo; el silo acumula gases que dañan las vías respiratorias; y el polvo con esporas de hongos daña los pulmones. La jerarquía de controles ordena las medidas, desde eliminar el peligro hasta el EPP.",
        f"Una bodega de heno bien ventilada y con el heno seco es un control de ingeniería; una regla de no entrar al silo es administrativa. Las labores con maquinaria y con silos las hace personal capacitado y autorizado. {EMER} {AVISO}",
    ],
    vocab=[("forraje", "planta que se cultiva o cosecha para alimentar animales"), ("heno", "forraje cortado y secado, guardado en fardos"), ("ensilaje", "forraje picado y guardado sin aire en un silo, donde fermenta"), ("fardo", "paquete de heno atado, de gran peso"), ("silo", "estructura cerrada donde se guarda el ensilaje"), ("combustión espontánea", "calentamiento que enciende solo el heno guardado húmedo"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Distinguir heno y ensilaje", "En un fundo de ejemplo se pica el forraje y se guarda sin aire en un silo. ¿Es heno o ensilaje?", ["No se seca: se guarda picado y sin aire.", "Eso es ensilaje."], "Ensilaje"),
        ("Clasificar un control", "Un fundo de ejemplo cierra con una reja fija la entrada al silo de ensilaje. ¿Qué tipo de control es?", ["La reja fija cambia físicamente el acceso.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que el heno húmedo se puede guardar «porque se seca solo».", "Puede calentarse y prenderse fuego.", "El heno se guarda solo cuando está seco."),
              ("Creer que entrar al silo es seguro si se contiene la respiración.", "Los gases dañan en poco tiempo.", "Nadie entra al silo: lo hace personal autorizado.")],
    T=[
        ("abc", "En los forrajes: ¿qué es el heno?", "Forraje cortado y secado, guardado en fardos", "Forraje picado y guardado sin aire", "Pasto fresco que se pastorea", "El heno se seca; el ensilaje se guarda sin aire."),
        ("abc", "En los forrajes: ¿qué es el ensilaje?", "Forraje picado y guardado sin aire en un silo", "Forraje seco guardado en fardos", "Pasto cortado en el momento", "El ensilaje se conserva fermentando sin aire."),
        ("abc", "En los forrajes: ¿para qué se conserva el forraje?", "Para alimentar a los animales cuando falta pasto", "Para vender la maquinaria", "Para sembrar menos", "La conservación asegura alimento todo el año."),
        ("=", "{F} Cada fardo de ejemplo pesa 400 kg. ¿Cuántos kilos pesan 6 fardos?", "400*6", "Se multiplican los kilos de cada fardo por el número de fardos.", " kg"),
        ("abc", "{F} Guardar el heno seco bajo un techo ventilado es un control de tipo:", "De ingeniería, porque cambia el lugar de guarda", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "El lugar seco y ventilado reduce el calentamiento sin depender de las personas."),
        ("abc", "{F} Una regla que dice «nadie entra al silo sin autorización» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el silo", "De sustitución, porque cambia el forraje", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado al heno guardado húmedo?", "Que se caliente, se incendie y cause daños", "El heno mismo", "Que ocupe poco espacio", "El riesgo es la posibilidad de daño; el heno húmedo es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí cómo se enfarda, así que manejo la enfardadora». ¿Qué respuesta es correcta?", "Es peligroso: la maquinaria la opera personal capacitado y autorizado", "Es correcto, si va despacio", "Es correcto, si usa casco", "Operar maquinaria exige formación y autorización."),
        ("abc", "{F} Se ve salir humo de un montón de heno guardado. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Acercarte a revisar el montón", "Mover los fardos para ventilar", "Un incendio puede crecer rápido; se avisa a quienes pueden actuar."),
        ("abc", "En los forrajes: ¿por qué el silo es un espacio peligroso?", "Porque acumula gases que dañan las vías respiratorias", "Porque está lleno de agua", "Porque es muy luminoso", "Los gases de la fermentación son peligrosos."),
        ("abc", "{F} Se propone solo entregar mascarillas por el polvo del heno. ¿Qué medida es más efectiva?", "Reducir el polvo con una bodega ventilada y un manejo cuidadoso", "Entregar más mascarillas", "Pedir que se respire por la nariz", "Reducir el polvo en su origen está más arriba que el EPP."),
        ("=", "{F} Una pila de ejemplo tiene 20 fardos de 400 kg. ¿Cuántos kilos pesa la pila?", "20*400", "Se multiplican los fardos por el peso de cada uno.", " kg"),
        ("abc", "En los forrajes: ¿por qué los fardos apilados en altura son un peligro?", "Porque pueden caer y aplastar a una persona", "Porque se secan más", "Porque cambian de color", "El peso de los fardos puede causar graves lesiones."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por entrar a su silo a «revisar el ensilaje» porque eres delgado. ¿Qué respondes?", "Que no, porque el silo es un espacio peligroso, y que lo consultarás con un adulto responsable", "Que sí, un minuto", "Que sí, con una cuerda", "Nadie sin formación y equipos entra a un silo."),
    sc=[
        ("En los forrajes: ¿qué es un forraje?", "Una planta que alimenta a los animales", "El forraje es alimento vegetal para animales."),
        ("En los forrajes: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En los forrajes: ¿qué peligro tiene el heno guardado húmedo?", "Puede calentarse y prenderse fuego", "El calentamiento puede encender el heno solo."),
    ],
    op=("El «Fundo Demo 7» anota una tarea de ejemplo: guardar fardos de heno recién enfardados y aún húmedos, apilados hasta el techo de un galpón cerrado, sin ventilación. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves humo saliendo de la pila.",
        "(a) Peligro: heno húmedo apilado y sin ventilación; riesgo: que se caliente, se incendie y cause daños. (b) Una regla de guardar solo heno seco. (c) Un galpón ventilado y con pilas de baja altura. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer revisar el humo", "proponer solo EPP"],
        "Pregunta: «¿qué control cambia el lugar y no depende de que alguien lo recuerde?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe tres peligros del cultivo y conservación de forrajes y el riesgo de cada uno.",
    extend="Explica con un ejemplo por qué un fardo pesado es un peligro aunque esté quieto.",
)

# ============================================================ OAM-06, clase 2
F = ("Ficha 2 (datos y documentos de ejemplo, inventados). «Fundo Demo 6»: alfalfa para heno, rendimiento de ejemplo de 8.000 kg de materia seca por hectárea al año; maíz para ensilaje, rendimiento de ejemplo de 30.000 kg de materia seca por hectárea. "
     "Humedad máxima de ejemplo del heno para guardarlo: 15 %. El forraje contiene agua; la materia seca es lo que queda sin agua. Documentos: el registro de siembra y cosecha del forraje, el análisis de laboratorio del forraje (humedad y proteína) y el inventario de forraje. Roles: encargado de forrajes, operador autorizado y nutricionista animal.")
build(
    O6, 2, F,
    use="Aprenderé los conceptos de materia seca, rendimiento de forraje, humedad y calidad, y los documentos y roles del cultivo y la conservación de forrajes.",
    prior=["Sé qué son forraje, heno y ensilaje.", "Sé multiplicar y dividir enteros.", "Sé comparar un valor con un máximo."],
    explain=[
        "El forraje fresco contiene mucha agua. La materia seca es lo que queda del forraje sin su agua, y es lo que realmente alimenta al animal. Por eso el rendimiento se mide en kilos de materia seca por hectárea. La humedad es el porcentaje de agua del forraje. Para guardar heno, la humedad debe estar bajo un máximo; si está más alta, el heno se calienta y puede echarse a perder o incendiarse.",
        "La calidad del forraje se mide en un laboratorio, por ejemplo con la humedad y la proteína. Los documentos son el registro de siembra y cosecha, que anota qué se sembró y cuándo se cortó; el análisis de laboratorio; y el inventario, que dice cuánto forraje hay guardado. El encargado de forrajes lleva los registros, el operador autorizado maneja la maquinaria y el nutricionista animal calcula la ración.",
        f"Un análisis de laboratorio no se altera para que el forraje «cumpla». {EMER} {AVISO}",
    ],
    vocab=[("materia seca", "lo que queda del forraje sin su agua"), ("humedad", "porcentaje de agua del forraje"), ("rendimiento", "kilos de materia seca por hectárea"), ("inventario de forraje", "documento que dice cuánto forraje hay guardado"), ("proteína", "nutriente importante para el crecimiento y la producción"), ("nutricionista animal", "profesional que calcula la ración de los animales")],
    worked=[
        ("Rendimiento total", "Un cultivo de ejemplo de 5 hectáreas rinde 6.000 kg de materia seca por hectárea. ¿Cuánto produce en total?", ["Se multiplican las hectáreas por el rendimiento.", "5 por 6.000."], "30.000 kg de materia seca"),
        ("Comparar con el máximo", "Un forraje de ejemplo tiene 22 % de humedad y el máximo es 18 %. ¿Cuántos puntos lo excede?", ["Se resta el máximo a la humedad.", "22 menos 18."], "4 puntos"),
    ],
    mistakes=[("Medir el forraje en kilos frescos como si fueran materia seca.", "El agua no alimenta al animal.", "Se compara en materia seca."),
              ("Guardar heno sin medir su humedad.", "Un heno húmedo puede calentarse y prenderse fuego.", "Se mide la humedad antes de guardar.")],
    T=[
        ("abc", "En los forrajes: ¿qué es la materia seca?", "Lo que queda del forraje sin su agua", "El agua que contiene el forraje", "El peso del fardo con humedad", "La materia seca es lo que alimenta al animal."),
        ("abc", "En los forrajes: ¿qué es la humedad de un forraje?", "El porcentaje de agua que contiene", "El porcentaje de proteína", "El peso de cada fardo", "La humedad mide el agua del forraje."),
        ("abc", "En los forrajes: ¿qué dice el inventario de forraje?", "Cuánto forraje hay guardado", "Qué día se sembró", "Cuánta lluvia cayó", "El inventario cuenta el forraje guardado."),
        ("=", "{F} ¿Cuántos kilos de materia seca de heno producen las 10 hectáreas de alfalfa en un año?", "10*8000", "Se multiplican las hectáreas por el rendimiento por hectárea.", " kg"),
        ("=", "{F} ¿Cuántos kilos de materia seca de ensilaje producen las 5 hectáreas de maíz?", "5*30000", "Se multiplican las hectáreas por el rendimiento por hectárea.", " kg"),
        ("=", "{F} Si un heno tiene 18 % de humedad, ¿cuántos puntos excede el máximo de ejemplo?", "18-15", "Se resta el máximo a la humedad medida.", " puntos"),
        ("abc", "{F} ¿Puede guardarse un heno con 12 % de humedad según el máximo de ejemplo?", "Sí, porque 12 es menor que 15", "No, porque 12 es menor que 15", "No se puede saber", "12 % está bajo el máximo de 15 %."),
        ("abc", "{F} ¿Qué documento dice qué se sembró y cuándo se cortó el forraje?", "El registro de siembra y cosecha", "El inventario de forraje", "El análisis de laboratorio", "El registro anota las labores de siembra y cosecha."),
        ("abc", "{F} ¿Qué rol calcula la ración de los animales?", "El nutricionista animal", "El operador autorizado", "El comprador del heno", "El nutricionista calcula la ración según lo que necesitan los animales."),
        ("abc", "{F} Un operario dice: «el heno tiene 20 % de humedad, pero lo guardo igual, porque falta espacio». ¿Qué respuesta es correcta?", "Es peligroso: supera el máximo y puede calentarse y prenderse fuego", "Es correcto, porque falta espacio", "Es correcto, si es poco", "Un heno húmedo es un riesgo de incendio."),
        ("abc", "{F} El encargado quiere anotar 15 % de humedad en el informe del laboratorio, aunque midió 18 %. ¿Qué corresponde?", "Rechazarlo: se anota el valor real e informa", "Aceptarlo, para cumplir el máximo", "Aceptarlo, si nadie lo revisa", "Alterar un análisis oculta un riesgo."),
        ("abc", "{F} Una enfardadora se atasca y un operario quiere meter la mano para destrabarla con el motor andando. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Ayudarlo a destrabar", "Subir a la máquina", "Una máquina en funcionamiento atrapa; se avisa a quienes pueden actuar."),
        ("abc", "En los forrajes: ¿por qué se compara el forraje en materia seca?", "Porque el agua no alimenta y varía según la planta", "Porque el agua es lo más importante", "Porque la materia seca pesa más", "La materia seca permite comparar en la misma base."),
    ],
    ctx=("abc", "Un conocido te pide que firmes que su heno tiene la humedad correcta sin haberla medido. ¿Qué respondes?", "Que no, porque firmar sin medir lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si se ve seco", "Que sí, solo esta vez", "La humedad se mide; no se supone."),
    sc=[
        ("En los forrajes: ¿qué se mide en kilos de materia seca por hectárea?", "El rendimiento", "El rendimiento compara cultivos en una misma base."),
        ("En los forrajes: ¿qué pasa con un heno por sobre la humedad máxima?", "No se guarda", "Puede calentarse y echarse a perder."),
        ("En los forrajes: ¿quién lleva el inventario de forraje?", "El encargado de forrajes", "El encargado registra todo el forraje que hay guardado."),
    ],
    op=("Datos de ejemplo del «Fundo Demo 7»: 4 hectáreas de alfalfa que rinden 7.000 kg de materia seca por hectárea; 3 hectáreas de maíz para ensilaje que rinden 25.000 kg por hectárea; humedad medida del heno 17 % (máximo de ejemplo 15 %). Escribe (a) los kilos de materia seca del heno, (b) los kilos del ensilaje, (c) si se puede guardar el heno y por cuántos puntos se pasa, (d) a quién informas.",
        "(a) 4 × 7.000 = 28.000 kg. (b) 3 × 25.000 = 75.000 kg. (c) No se puede guardar; se pasa por 2 puntos (17 − 15). (d) Al encargado de forrajes y al jefe del fundo.",
        ["calcula el heno", "calcula el ensilaje", "concluye sobre la humedad", "informa a quien corresponde"],
        ["hoja con las cuatro respuestas"],
        ["guardar el heno húmedo", "alterar el análisis"],
        "Pregunta: «¿17 está arriba o abajo del máximo de 15?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula los kilos de materia seca de 6 hectáreas que rinden 5.000 kg por hectárea.",
    extend="Explica con un ejemplo por qué un heno muy húmedo es un riesgo de incendio.",
)

# ============================================================ OAM-06, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). En el «Fundo Demo 6» se anotaron cuatro observaciones: P, un montón de fardos de heno tiene el centro caliente, huele a quemado y se ve humo muy leve; Q, el silo de ensilaje tiene moho blanco en la superficie y un olor agrio fuerte; "
     "R, los fardos de otro galpón están secos, apilados a baja altura y con ventilación; S, el análisis de un lote de heno marca 14 % de humedad (máximo de ejemplo 15 %). Categorías: A, riesgo inmediato: alejarse y avisar; B, revisar y programar; C, sin acción.")
build(
    O6, 3, F,
    use="Aprenderé a analizar un caso de forrajes almacenados, a clasificar cada observación según su urgencia y a decidir quién actúa, sin tocar el forraje en riesgo.",
    prior=["Sé qué son heno y ensilaje.", "Sé qué es la humedad del forraje.", "Sé leer una lista de observaciones."],
    explain=[
        "Para analizar forraje almacenado se clasifica cada observación según su urgencia. Humo, olor a quemado o un centro muy caliente en el heno indican riesgo de incendio: es una emergencia y las personas se alejan y piden ayuda. Moho y olor agrio en un silo indican que la fermentación falló o que entró aire: se revisa y se informa, pero nadie entra al silo. Fardos secos, bien apilados y ventilados, o una humedad bajo el máximo, están en condiciones normales.",
        "Un buen análisis nombra la observación, la categoría, la evidencia y quién interviene. El encargado de forrajes informa, el jefe del fundo decide y el personal autorizado, con equipos y formación, revisa o retira el material. Nadie mueve un montón humeante ni entra a un silo por cuenta propia. El nutricionista decide si un ensilaje con moho puede usarse o debe descartarse.",
        f"El incendio de heno puede crecer sin aviso. {EMER} {AVISO}",
    ],
    vocab=[("urgencia", "qué tan rápido hay que actuar"), ("moho", "hongo que crece en el forraje húmedo"), ("fermentación", "proceso por el que el forraje se conserva sin aire en el silo"), ("riesgo inmediato", "riesgo que puede causar daño ahora"), ("descartar", "dejar de usar un material por no ser seguro")],
    worked=[
        ("Clasificar la urgencia", "Un montón de heno de ejemplo humea y huele a quemado. ¿A qué categoría corresponde?", ["Hay riesgo de incendio.", "Es riesgo inmediato: categoría A."], "A"),
        ("Condición normal", "Un galpón de ejemplo tiene heno seco, bajo y ventilado. ¿A qué categoría corresponde?", ["No hay señales de riesgo.", "Es categoría C."], "C"),
    ],
    mistakes=[("Mover un montón de heno humeante «para apagarlo».", "El aire puede avivar el fuego y hay riesgo de quemaduras.", "Se aleja y se avisa a emergencias."),
              ("Entrar al silo a sacar el moho de la superficie.", "El silo acumula gases peligrosos que dañan las vías respiratorias.", "Se informa; lo revisa personal autorizado.")],
    T=[
        ("abc", "En los forrajes: ¿qué es un riesgo inmediato?", "Un riesgo que puede causar daño ahora", "Un riesgo que se resuelve solo", "Un riesgo sin consecuencias", "El riesgo inmediato exige acción ahora."),
        ("abc", "En los forrajes: ¿qué es el moho?", "Un hongo que crece en el forraje húmedo", "Un nutriente del forraje", "Un tipo de fardo", "El moho es un hongo que daña el forraje."),
        ("abc", "En los forrajes: ¿qué significa descartar un forraje?", "Dejar de usarlo por no ser seguro", "Guardarlo para más tarde", "Venderlo más caro", "Descartar es dejar de usar un material peligroso."),
        ("abc", "{F} ¿A qué categoría corresponde la observación P, heno caliente con humo leve y olor a quemado?", "A, riesgo inmediato: alejarse y avisar", "B, revisar y programar", "C, sin acción", "Humo y olor a quemado indican riesgo de incendio."),
        ("abc", "{F} ¿A qué categoría corresponde la observación Q, moho y olor agrio en el silo?", "B, revisar y programar, sin entrar al silo", "A, alejarse y avisar siempre", "C, sin acción", "Es un problema de calidad que se revisa con personal autorizado."),
        ("abc", "{F} ¿A qué categoría corresponde la observación R, fardos secos y ventilados?", "C, sin acción", "A, riesgo inmediato", "B, revisar y programar", "Cumplen las condiciones de guarda: seco, bajo y ventilado."),
        ("abc", "{F} ¿A qué categoría corresponde la observación S, humedad de 14 %?", "C, sin acción, porque está bajo el máximo", "A, riesgo inmediato", "B, revisar y programar", "14 % es menor que el máximo de 15 %."),
        ("=", "{F} ¿Cuántos puntos de humedad faltan para llegar al máximo en la observación S?", "15-14", "Se resta la humedad medida al máximo.", " punto"),
        ("abc", "{F} Una compañera dice: «voy a mover los fardos humeantes para ventilarlos». ¿Qué respuesta es correcta?", "Es peligroso: se aleja y se avisa a emergencias", "Es correcto, si usa guantes", "Es correcto, si es rápido", "El aire puede avivar un fuego oculto."),
        ("abc", "{F} Alguien propone entrar al silo con una pala a retirar el moho. ¿Qué corresponde?", "Rechazarlo: nadie entra al silo, lo revisa personal autorizado", "Aceptarlo, con mascarilla", "Aceptarlo, si lo hace rápido", "El silo acumula gases peligrosos que dañan las vías respiratorias."),
        ("=", "{F} Si el montón P tiene 30 fardos de 400 kg, ¿cuántos kilos de heno están en riesgo?", "30*400", "Se multiplican los fardos por el peso de cada uno.", " kg"),
        ("abc", "{F} Se ve salir humo del montón P y una persona se acerca a tocarlo. ¿Qué corresponde a quien lo observa?", "Alejarse de la zona de riesgo y avisar a un adulto responsable y a emergencias", "Acercarse a apagarlo con las manos", "Echar agua sin saber si hay otros materiales", "Acercarse puede causar quemaduras; se avisa a quienes pueden actuar."),
        ("abc", "En los forrajes: ¿por qué quien analiza no mueve el forraje en riesgo?", "Porque puede empeorar el peligro y no está capacitado", "Porque el forraje no pesa", "Porque no importa", "Mover el material en riesgo puede empeorar el peligro."),
    ],
    ctx=("abc", "Un conocido te cuenta que su heno está caliente por dentro y te pregunta qué hacer. ¿Qué respondes?", "Que se aleje, no lo toque ni lo mueva y avise a emergencias", "Que lo mueva para ventilarlo", "Que le eche agua con un balde", "Un heno caliente puede incendiarse; se pide ayuda."),
    sc=[
        ("En los forrajes: ¿qué se hace ante humo en un montón de heno?", "Se aleja y se avisa a emergencias", "El incendio puede crecer sin aviso."),
        ("En los forrajes: ¿quién entra a un silo?", "Nadie de la clase: solo personal autorizado", "El silo acumula gases peligrosos que dañan las vías respiratorias."),
        ("En los forrajes: ¿qué categoría tiene un heno seco y ventilado?", "C, sin acción", "Cumple las condiciones de guarda: seco, bajo y ventilado."),
    ],
    op=("Observaciones de ejemplo del «Fundo Demo 7»: P1, fardos con el centro caliente y olor a quemado; P2, silo con moho en la superficie; P3, heno con 12 % de humedad, máximo de ejemplo 15 %; P4, fardos secos y ventilados. Categorías: A, alejarse y avisar; B, revisar y programar; C, sin acción. Escribe (a) la categoría de cada observación, (b) cuántos puntos faltan para el máximo en P3, (c) quién revisa el silo, (d) qué haces si ves humo.",
        "(a) P1: A; P2: B; P3: C; P4: C. (b) 15 − 12 = 3 puntos. (c) Personal autorizado, con equipos y formación. (d) Me alejo, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien las cuatro observaciones", "calcula la diferencia", "nombra quién revisa", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el humo como normal", "proponer entrar al silo"],
        "Pregunta: «¿qué observación indica riesgo de incendio?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres observaciones inventadas: olor a quemado, moho leve y heno seco.",
    extend="Explica con un ejemplo por qué un heno caliente es una emergencia.",
)

# ============================================================ OAM-06, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Balance forrajero del «Fundo Demo 6». Demanda: 100 vacas que consumen 12 kg de materia seca por día cada una durante 180 días de invierno. "
     "Oferta: 10 hectáreas de alfalfa que rinden 8.000 kg de materia seca por hectárea para heno, y 5 hectáreas de maíz que rinden 30.000 kg por hectárea para ensilaje. Pérdidas de conservación de ejemplo: 10 % de la oferta total. Costo de ejemplo de comprar el faltante: $120 por kilo de materia seca.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la demanda y la oferta de forraje, las pérdidas de conservación y el faltante o sobrante.",
    prior=["Sé qué es la materia seca y el rendimiento.", "Sé multiplicar y dividir enteros.", "Sé calcular porcentajes enteros."],
    explain=[
        "El balance forrajero compara la demanda con la oferta. La demanda es el forraje que necesitan los animales: animales por consumo diario por días. La oferta es lo que produce el fundo: hectáreas por rendimiento, sumando heno y ensilaje. Parte de la oferta se pierde al conservar, así que se calcula la oferta útil restando las pérdidas. El balance es la oferta útil menos la demanda: si es negativo, hay un faltante; si es positivo, un sobrante.",
        "Un faltante obliga a comprar forraje, reducir animales o conseguir otra fuente; un sobrante permite vender o guardar. Con el costo por kilo se calcula el gasto de comprar el faltante. Los valores son de ejemplo y las decisiones las toman el jefe del fundo y el nutricionista animal. Calcular no reemplaza la seguridad de las labores de cosecha y conservación.",
        f"Nunca se guarda un forraje húmedo para evitar el faltante. {EMER} {AVISO}",
    ],
    vocab=[("balance forrajero", "comparación entre el forraje que se necesita y el que se produce"), ("demanda", "forraje que necesitan los animales"), ("oferta", "forraje que produce el fundo"), ("oferta útil", "oferta menos las pérdidas de conservación"), ("faltante", "forraje que falta para cubrir la demanda"), ("sobrante", "forraje que sobra después de cubrir la demanda")],
    worked=[
        ("Demanda", "Un plantel de ejemplo de 20 vacas consume 10 kg de materia seca por día durante 100 días. ¿Cuál es la demanda?", ["Se multiplican animales, consumo y días.", "20 por 10 por 100."], "20.000 kg"),
        ("Oferta útil", "Una oferta de ejemplo de 25.000 kg pierde 10 % al conservarse. ¿Cuál es la oferta útil?", ["La pérdida es 10 % de 25.000, o sea 2.500.", "25.000 menos 2.500."], "22.500 kg"),
    ],
    mistakes=[("Comparar la oferta bruta con la demanda sin restar las pérdidas.", "Parte del forraje se pierde al conservarlo.", "Se compara la oferta útil."),
              ("Guardar forraje húmedo para evitar un faltante.", "Un forraje húmedo puede incendiarse o pudrirse.", "Se guarda solo forraje bajo la humedad máxima.")],
    T=[
        ("abc", "En los forrajes: ¿qué es la demanda de forraje?", "El forraje que necesitan los animales", "El forraje que produce el fundo", "El forraje que se pierde", "La demanda es lo que necesitan los animales."),
        ("abc", "En los forrajes: ¿qué es la oferta útil?", "La oferta menos las pérdidas de conservación", "La oferta más las pérdidas", "El forraje que se vende", "La oferta útil descuenta las pérdidas."),
        ("abc", "En los forrajes: ¿qué significa un balance negativo?", "Hay un faltante de forraje", "Hay un sobrante de forraje", "No hay animales", "Un balance negativo es un faltante."),
        ("=", "{F} ¿Cuántos kilos de materia seca demandan los animales en el invierno?", "100*12*180", "Se multiplican los animales por el consumo diario y por los días.", " kg"),
        ("=", "{F} ¿Cuánto costaría comprar el faltante al precio de ejemplo?", "(100*12*180-((10*8000+5*30000)-(10*8000+5*30000)*10//100))*120", "Se multiplica el faltante por el precio de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuántos kilos de materia seca de ensilaje produce el fundo?", "5*30000", "Se multiplican las hectáreas por el rendimiento.", " kg"),
        ("=", "{F} ¿Cuántos kilos suma la oferta total antes de pérdidas?", "10*8000+5*30000", "Se suman el heno y el ensilaje.", " kg"),
        ("=", "{F} ¿Cuántos kilos se pierden por conservación?", "(10*8000+5*30000)*10//100", "Se calcula el 10 % de la oferta total.", " kg"),
        ("=", "{F} ¿Cuál es la oferta útil?", "(10*8000+5*30000)-(10*8000+5*30000)*10//100", "Se resta la pérdida a la oferta total.", " kg"),
        ("=", "{F} ¿Cuántos kilos faltan para cubrir la demanda de los animales?", "100*12*180-((10*8000+5*30000)-(10*8000+5*30000)*10//100)", "Se resta la oferta útil a la demanda de los animales.", " kg"),
        ("abc", "{F} Con esos números, ¿hay faltante o sobrante de forraje?", "Faltante, porque la oferta útil es menor que la demanda", "Sobrante, porque la oferta total supera la demanda", "Ninguno, porque son iguales", "La oferta útil de 207.000 kg es menor que la demanda de 216.000 kg."),
        ("abc", "{F} El encargado quiere guardar heno con 20 % de humedad para aumentar la oferta. ¿Qué corresponde?", "Rechazarlo: un heno húmedo puede incendiarse o pudrirse", "Aceptarlo, para tener más oferta", "Aceptarlo, si es poco", "Un forraje húmedo es un riesgo de incendio y de pérdida."),
        ("abc", "En los forrajes: ¿por qué conviene calcular el balance antes del invierno?", "Para saber si habrá que comprar forraje o reducir animales a tiempo", "Para evitar sembrar", "Para ocultar las pérdidas", "Anticipar el faltante permite decidir con tiempo."),
    ],
    ctx=("abc", "Un conocido te pregunta si le alcanza el forraje para el invierno y te da solo las hectáreas. ¿Qué respondes?", "Que faltan los rendimientos, las pérdidas y la demanda, y que lo calcula con un nutricionista", "Que sí, siempre", "Que no, nunca", "Sin demanda y rendimientos no se puede hacer un balance."),
    sc=[
        ("En los forrajes: ¿cómo se calcula la demanda?", "Animales por consumo diario por días", "La demanda multiplica animales, consumo y días."),
        ("En los forrajes: ¿qué se resta a la oferta para obtener la oferta útil?", "Las pérdidas de conservación", "La oferta útil descuenta lo que se pierde."),
        ("En los forrajes: ¿qué es el balance forrajero?", "Oferta útil menos demanda", "El balance dice si falta o sobra forraje."),
    ],
    op=("Datos de ejemplo del «Fundo Demo 8»: 50 vacas que consumen 10 kg de materia seca por día durante 100 días; oferta de 60.000 kg con 10 % de pérdidas. Escribe (a) la demanda, (b) la oferta útil, (c) el balance y si hay faltante o sobrante, (d) qué haces si ves humo en el heno guardado.",
        "(a) 50 × 10 × 100 = 50.000 kg. (b) 60.000 − 6.000 = 54.000 kg. (c) 54.000 − 50.000 = 4.000 kg de sobrante. (d) Me alejo, aviso a un adulto responsable y a emergencias.",
        ["calcula la demanda", "calcula la oferta útil", "calcula el balance", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["no restar las pérdidas", "comparar oferta bruta con la demanda"],
        "Pregunta: «¿cuántos kilos son el 10 % de 60.000?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la demanda de 30 vacas que consumen 12 kg por día durante 60 días.",
    extend="Explica con un ejemplo por qué un faltante de forraje afecta el bienestar de los animales.",
)

# ============================================================ OAM-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Lechería Demo 6» usa estos equipos: una balanza de piso para pesar animales, el termómetro del tanque de frío, el equipo de ordeña, una bomba de agua, un cerco eléctrico y ventiladores. "
     "Peligros anotados: electricidad en lugares húmedos, partes móviles de bombas y ventiladores, el cerco eléctrico, productos de limpieza, animales que se asustan con los ruidos y equipos que fallan en pleno uso.")
build(
    O7, 1, F,
    use="Aprenderé qué significa verificar el funcionamiento de máquinas, equipos e instrumentos pecuarios, por qué hay que hacerlo y cuáles son los peligros, sin reparar ni manipular equipos.",
    prior=["Sé qué es un peligro y un riesgo.", "Sé leer una ficha escrita.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Verificar el funcionamiento es comprobar que una máquina, un equipo o un instrumento trabaja dentro de lo esperado. Una máquina o un equipo hace un trabajo, como un ventilador o una bomba; un instrumento mide algo, como una balanza o un termómetro. Una verificación se hace con una hoja de verificación, que lista qué revisar y cuál es el resultado esperado. Un equipo que falla puede dañar a los animales, a las personas o a la producción.",
        "Verificar tiene peligros: electricidad cerca de agua, partes móviles, cercos eléctricos y animales cercanos. Quien verifica en terreno es personal capacitado; el operador común solo observa y reporta anomalías, sin abrir ni reparar. La jerarquía de controles aplica: eliminar, sustituir, cambiar el lugar o el equipo, reglas y, al final, EPP.",
        f"Una protección fija sobre las partes móviles es un control de ingeniería; una regla de no tocar el cerco eléctrico es administrativa. {EMER} {AVISO}",
    ],
    vocab=[("verificar", "comprobar que algo funciona dentro de lo esperado"), ("instrumento", "aparato que mide algo, como una balanza o un termómetro"), ("hoja de verificación", "lista de qué revisar y cuál es el resultado esperado"), ("anomalía", "algo distinto de lo normal en el funcionamiento"), ("cerco eléctrico", "cerco que da una descarga para mantener a los animales dentro"), ("EPP", "equipo de protección personal, la última barrera")],
    worked=[
        ("Instrumento o equipo", "En un plantel de ejemplo, una balanza mide el peso de los animales. ¿Es un equipo o un instrumento?", ["Su trabajo es medir algo.", "Es un instrumento."], "Instrumento"),
        ("Clasificar un control", "Un plantel de ejemplo cambia un cable largo tendido en el piso por una canalización fija en la pared. ¿Qué tipo de control es?", ["La canalización cambia físicamente la instalación.", "Es un control de ingeniería."], "De ingeniería"),
    ],
    mistakes=[("Creer que verificar es lo mismo que reparar.", "Verificar es comprobar; reparar es intervenir.", "Si algo falla, se reporta; la repara personal autorizado."),
              ("Tocar un cerco eléctrico «para ver si funciona».", "La descarga puede dañar.", "Solo personal autorizado verifica los cercos.")],
    T=[
        ("abc", "En los equipos pecuarios: ¿qué significa verificar el funcionamiento?", "Comprobar que trabaja dentro de lo esperado", "Repararlo cuando se rompe", "Comprarlo nuevo", "Verificar es comprobar; reparar es otra tarea."),
        ("abc", "En los equipos pecuarios: ¿qué es un instrumento?", "Un aparato que mide algo, como una balanza", "Una máquina que mueve cargas", "Un producto de limpieza", "El instrumento mide una variable, como el peso o la temperatura."),
        ("abc", "En los equipos pecuarios: ¿qué es una hoja de verificación?", "Una lista de qué revisar y cuál es el resultado esperado", "Un manual de reparación", "Una factura de compra", "La hoja de verificación guía la revisión."),
        ("=", "{F} El plantel tiene 6 equipos que se verifican a diario, cada uno con 5 puntos de revisión. ¿Cuántos puntos se revisan al día?", "6*5", "Se multiplican los equipos por los puntos de cada uno.", " puntos"),
        ("abc", "{F} Una protección fija sobre las aspas de un ventilador es un control de tipo:", "De ingeniería, porque cambia físicamente el equipo", "Administrativo, porque es una regla", "De EPP, porque protege a quien trabaja", "La protección es una parte del equipo y funciona siempre."),
        ("abc", "{F} Una regla que dice «el cerco eléctrico solo lo verifica personal autorizado» es un control de tipo:", "Administrativo, porque ordena una conducta", "De ingeniería, porque cambia el cerco", "De sustitución, porque cambia el cerco por otro", "Una regla escrita es un control administrativo."),
        ("abc", "{F} ¿Cuál es el riesgo asociado a la electricidad en un lugar húmedo?", "Que una persona reciba una descarga eléctrica", "La electricidad misma", "Que el lugar esté mojado", "El riesgo es la posibilidad de daño; la electricidad con agua es el peligro."),
        ("abc", "{F} Una estudiante dice: «ya aprendí a verificar la bomba, así que la abro y reviso por dentro». ¿Qué respuesta es correcta?", "Es peligroso: abrir y reparar lo hace personal autorizado", "Es correcto, si apaga la luz", "Es correcto, si usa guantes", "Intervenir un equipo con electricidad exige formación."),
        ("abc", "{F} Durante una visita, un ventilador suelta chispas y se siente olor a quemado. ¿Qué corresponde según las reglas generales?", "No acercarte, avisar a un adulto responsable y a emergencias", "Acercarte a desconectarlo", "Echarle agua", "Chispas y olor a quemado indican riesgo de incendio o de descarga."),
        ("abc", "En los equipos pecuarios: ¿por qué conviene verificar los equipos antes de usarlos?", "Porque detecta fallas que podrían dañar a animales o personas", "Porque así duran menos", "Porque evita registrar", "Detectar una falla a tiempo previene accidentes."),
        ("abc", "{F} Se propone solo entregar guantes aislantes para tocar equipos eléctricos mojados. ¿Qué medida es más efectiva?", "Instalar tomas protegidas y fuera del agua, hechas por personal autorizado", "Entregar más guantes", "Pedir que se toque con cuidado", "Alejar la electricidad del agua actúa sobre el peligro."),
        ("=", "{F} La balanza se verifica cada semana. ¿Cuántas verificaciones tiene al año, si el año tiene 52 semanas?", "52*1", "Se multiplica el número de semanas por una verificación semanal.", " verificaciones"),
        ("abc", "En los equipos pecuarios: ¿qué hace un operador si nota ruido anormal en una bomba?", "Avisa de inmediato a su jefe, sin abrirla ni repararla", "La abre para revisarla", "La sigue usando", "El operador reporta; la revisión es de personal autorizado."),
    ],
    ctx=("abc", "Un conocido te ofrece pagarte por revisar y arreglar el cerco eléctrico de su potrero «porque ya viste cómo funciona». ¿Qué respondes?", "Que no, porque exige formación y autorización, y que lo consultarás con un adulto responsable", "Que sí, con guantes", "Que sí, si lo desconectas un rato", "Haber visto el concepto no habilita para intervenir instalaciones eléctricas."),
    sc=[
        ("En los equipos pecuarios: ¿qué es verificar el funcionamiento?", "Comprobar que trabaja como se espera", "Verificar es comparar con el resultado esperado."),
        ("En los equipos pecuarios: ¿qué nivel de la jerarquía de controles es el último?", "El equipo de protección personal (EPP)", "El EPP va al final porque no quita el peligro."),
        ("En los equipos pecuarios: ¿quién repara una bomba?", "Personal capacitado y autorizado", "La reparación exige formación y norma vigente."),
    ],
    op=("El «Plantel Demo 7» anota una tarea de ejemplo: revisar una bomba de agua con las manos mojadas, con el enchufe tirado en el piso encharcado y el motor andando. Escribe (a) el peligro y su riesgo, (b) un control administrativo, (c) un control de ingeniería, (d) qué haces si ves a alguien recibir una descarga.",
        "(a) Peligro: electricidad en el agua; riesgo: que la persona reciba una descarga eléctrica. (b) Una regla de no revisar equipos con las manos mojadas ni con el motor andando. (c) Una toma eléctrica elevada, protegida y fuera del agua, instalada por personal autorizado. (d) No me acerco, aviso a un adulto responsable y a emergencias.",
        ["distingue peligro y riesgo", "propone un control administrativo", "propone un control de ingeniería", "no se acerca y avisa"],
        ["hoja con las cuatro respuestas"],
        ["llamar riesgo al peligro", "proponer tocar a la persona", "proponer solo guantes"],
        "Pregunta: «¿qué control separa la electricidad del agua aunque nadie se acuerde?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Clasifica como equipo o instrumento: balanza, bomba de agua, termómetro y ventilador.",
    extend="Explica con un ejemplo por qué un operador reporta una anomalía y no la repara.",
)

# ============================================================ OAM-07, clase 2
F = ("Ficha 2 (datos y documentos de ejemplo, inventados). Verificación de la balanza de piso del «Plantel Demo 7»: se compara con un peso patrón de 50 kg (un peso conocido). La balanza marcó 52 kg. Tolerancia de ejemplo: no más de 1 kg de diferencia. "
     "Termómetro del tanque: patrón de 4 grados, marcó 4. Documentos: la hoja de verificación, el registro de verificaciones (fecha, equipo, resultado y responsable) y la hoja de vida de cada equipo. Roles: operador, técnico de servicio y jefe del plantel.")
build(
    O7, 2, F,
    use="Aprenderé los conceptos de patrón, tolerancia y error de un instrumento, los documentos de la verificación de equipos y los roles del operador, el técnico y el jefe.",
    prior=["Sé qué es verificar un equipo.", "Sé restar y calcular porcentajes enteros.", "Sé leer una ficha con datos."],
    explain=[
        "Un patrón es un valor conocido con el que se compara un instrumento. El error es la diferencia entre lo que marca el instrumento y el patrón. La tolerancia es el error máximo aceptable. Si el error es menor o igual que la tolerancia, el instrumento está conforme; si es mayor, está fuera de tolerancia y no se debe usar hasta que personal autorizado lo calibre. Calibrar es ajustar el instrumento para que marque el valor correcto.",
        "Los documentos dejan evidencia: la hoja de verificación guía la revisión; el registro de verificaciones anota fecha, equipo, resultado y responsable; la hoja de vida resume la historia de cada equipo. El operador verifica visualmente y reporta, el técnico de servicio calibra y repara, y el jefe del plantel decide el retiro de un equipo. Nunca se anota un resultado que no se midió.",
        f"Un instrumento fuera de tolerancia puede llevar a decisiones equivocadas sobre los animales. {EMER} {AVISO}",
    ],
    vocab=[("patrón", "valor conocido con el que se compara un instrumento"), ("error", "diferencia entre lo que marca el instrumento y el patrón"), ("tolerancia", "error máximo aceptable"), ("calibrar", "ajustar un instrumento para que marque el valor correcto"), ("fuera de tolerancia", "con un error mayor que el aceptable"), ("registro de verificaciones", "documento que anota fecha, equipo, resultado y responsable")],
    worked=[
        ("Calcular el error", "Una balanza de ejemplo marca 21 kg al pesar un patrón de 20 kg. ¿Cuál es el error?", ["Se resta el patrón a la lectura.", "21 menos 20."], "1 kg"),
        ("Comparar con la tolerancia", "El error es 3 kg y la tolerancia es 2 kg. ¿Está conforme?", ["3 es mayor que 2.", "Está fuera de tolerancia."], "No, está fuera de tolerancia"),
    ],
    mistakes=[("Seguir usando una balanza que está fuera de tolerancia «porque se acerca».", "Los pesos registrados serán incorrectos.", "Se retira hasta que se calibre."),
              ("Calibrar el instrumento sin autorización.", "La calibración exige formación y un patrón adecuado.", "La hace personal autorizado.")],
    T=[
        ("abc", "En los equipos pecuarios: ¿qué es un patrón?", "Un valor conocido con el que se compara un instrumento", "El nombre del instrumento", "El precio del instrumento", "El patrón es el valor de referencia."),
        ("abc", "En los equipos pecuarios: ¿qué es la tolerancia?", "El error máximo aceptable", "El error mínimo", "El promedio de las lecturas", "La tolerancia fija el límite del error."),
        ("abc", "En los equipos pecuarios: ¿qué es calibrar un instrumento?", "Ajustarlo para que marque el valor correcto", "Cambiarle el color", "Guardarlo en una caja", "Calibrar corrige la lectura del instrumento."),
        ("=", "{F} ¿Cuál es el error de la balanza, en kilos?", "52-50", "Se resta el patrón a la lectura de la balanza.", " kg"),
        ("abc", "{F} ¿Está la balanza dentro de la tolerancia de ejemplo?", "No, porque el error de 2 kg supera 1 kg", "Sí, porque el error es pequeño", "Sí, porque 52 es mayor que 50", "El error de 2 kg es mayor que la tolerancia de 1 kg."),
        ("abc", "{F} ¿Está el termómetro del tanque dentro de la tolerancia?", "Sí, porque marca igual que el patrón", "No, porque es un termómetro", "No se puede saber", "Marcó 4 igual que el patrón de 4."),
        ("=", "{F} ¿Qué porcentaje del patrón es el error de la balanza?", "2*100//50", "Se divide el error entre el patrón y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué documento anota fecha, equipo, resultado y responsable de cada verificación?", "El registro de verificaciones", "La hoja de vida", "La hoja de verificación", "El registro guarda lo ya verificado."),
        ("abc", "{F} ¿Qué rol calibra y repara los instrumentos?", "El técnico de servicio", "El operador", "El comprador", "El técnico de servicio calibra y repara."),
        ("abc", "{F} Un operador dice: «la balanza marca 2 kg de más, pero resto 2 kg a cada pesaje y listo». ¿Qué respuesta es correcta?", "Es incorrecto: el instrumento se retira y lo calibra personal autorizado", "Es correcto, porque el error es fijo", "Es correcto, si anota los pesos", "Un instrumento fuera de tolerancia no se usa con correcciones improvisadas."),
        ("abc", "{F} El jefe del plantel quiere anotar «conforme» en el registro de la balanza, aunque el error es 2 kg. ¿Qué corresponde?", "Rechazarlo: se anota el resultado real e informa", "Aceptarlo, para que cumpla", "Aceptarlo, si nadie lo revisa", "Anotar conforme algo que no lo es falsea el registro."),
        ("abc", "{F} Un animal se asusta con el ruido del equipo y empuja a una persona contra la balanza. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Acercarse a calmar al animal", "Tirar a la persona hacia ti", "Un animal asustado es impredecible, aunque sea manso."),
        ("abc", "En los equipos pecuarios: ¿por qué el error de una balanza afecta las decisiones?", "Porque los pesos incorrectos llevan a raciones o dosis equivocadas", "Porque la balanza pesa más rápido", "Porque no se anota", "Un peso falso lleva a decisiones equivocadas."),
    ],
    ctx=("abc", "Un conocido te pide que firmes que su balanza está calibrada sin haberla comparado con un patrón. ¿Qué respondes?", "Que no, porque firmar sin comprobar lo falsea, y que lo consultarás con un adulto responsable", "Que sí, si se ve bien", "Que sí, solo una vez", "La calibración se comprueba con un patrón."),
    sc=[
        ("En los equipos pecuarios: ¿cómo se calcula el error de un instrumento?", "Lectura menos patrón", "El error es la diferencia con el patrón."),
        ("En los equipos pecuarios: ¿qué se hace con un instrumento fuera de tolerancia?", "Se retira hasta que lo calibre personal autorizado", "Un instrumento fuera de tolerancia entrega datos falsos."),
        ("En los equipos pecuarios: ¿quién decide el retiro de un equipo?", "El jefe del plantel", "El jefe decide con la información del técnico."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 8»: balanza que marca 31 kg al pesar un patrón de 30 kg, con tolerancia de 2 kg; termómetro que marca 8 al medir un patrón de 4, con tolerancia de 1 grado. Escribe (a) el error de la balanza y si está conforme, (b) el error del termómetro y si está conforme, (c) qué haces con el instrumento fuera de tolerancia, (d) quién lo calibra.",
        "(a) 31 − 30 = 1 kg; está conforme, porque 1 es menor que 2. (b) 8 − 4 = 4 grados; no está conforme, porque 4 supera 1. (c) Se retira y se informa al jefe. (d) El técnico de servicio.",
        ["calcula el error de la balanza", "calcula el error del termómetro", "decide qué hacer", "nombra quién calibra"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "usar un instrumento fuera de tolerancia"],
        "Pregunta: «¿qué valor se resta a la lectura para obtener el error?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula el error de un termómetro que marca 5 al medir un patrón de 4 y compáralo con una tolerancia de 1.",
    extend="Explica con un ejemplo por qué un registro de verificación debe anotar el resultado real.",
)

# ============================================================ OAM-07, clase 3
F = ("Ficha 3 (hoja de verificación de ejemplo, inventada). Resultados del día en el «Plantel Demo 7»: E1, balanza, error de 3 kg con tolerancia de 1 kg; E2, ventilador, gira sin ruidos y con la protección fija; "
     "E3, bomba de agua, hace un ruido metálico fuerte y vibra; E4, cerco eléctrico, un cable suelto toca el suelo mojado; E5, termómetro del tanque, error de 0 grados con tolerancia de 1. "
     "Categorías: A, detener y avisar de inmediato; B, retirar o programar calibración; C, conforme.")
build(
    O7, 3, F,
    use="Aprenderé a analizar los resultados de una hoja de verificación, a clasificar cada equipo según su urgencia y a decidir quién actúa, sin reparar ni tocar nada.",
    prior=["Sé qué son error, tolerancia y calibración.", "Sé qué es una hoja de verificación.", "Sé leer una lista de resultados."],
    explain=[
        "Para analizar una hoja de verificación se clasifica cada equipo según su resultado. Un equipo con una falla que puede causar daño inmediato, como un cable suelto en el agua o un ruido metálico fuerte, se detiene y se avisa de inmediato. Un instrumento fuera de tolerancia no está en emergencia, pero se retira hasta calibrarlo. Un equipo que funciona como se espera está conforme.",
        "Un buen análisis nombra el equipo, la categoría, la evidencia y quién actúa. El operador reporta; el jefe del plantel decide el retiro; el técnico de servicio calibra o repara; y el personal eléctrico autorizado interviene los cables. Nadie toca un cable suelto ni sigue usando una bomba que vibra con ruido metálico. Cada resultado se anota tal cual en el registro.",
        f"La seguridad de las personas y de los animales va antes que la producción. {EMER} {AVISO}",
    ],
    vocab=[("conforme", "que cumple lo esperado"), ("fuera de tolerancia", "con un error mayor que el aceptable"), ("vibración", "temblor fuerte de una máquina que indica una posible falla"), ("detener", "dejar de usar un equipo de forma segura"), ("evidencia", "dato del resultado que respalda una decisión")],
    worked=[
        ("Clasificar un equipo", "Un equipo de ejemplo tiene el cable de alimentación pelado y con chispas. ¿A qué categoría corresponde?", ["Hay riesgo inmediato de descarga y de incendio.", "Categoría A: detener y avisar."], "A"),
        ("Instrumento fuera de tolerancia", "Un termómetro de ejemplo tiene un error de 2 grados y la tolerancia es 1 grado. ¿A qué categoría corresponde?", ["No hay emergencia.", "Se retira hasta calibrar: categoría B."], "B"),
    ],
    mistakes=[("Seguir usando una bomba con ruido metálico «hasta terminar la jornada».", "Puede romperse y causar un accidente.", "Se detiene si es seguro y se avisa."),
              ("Anotar «conforme» para evitar problemas.", "Se falsea el registro.", "Se anota el resultado real.")],
    T=[
        ("abc", "En los equipos pecuarios: ¿qué significa que un equipo esté conforme?", "Que cumple lo esperado", "Que está apagado", "Que es nuevo", "Conforme significa cumplir lo esperado en la verificación."),
        ("abc", "En los equipos pecuarios: ¿qué puede indicar la vibración fuerte de una bomba?", "Una posible falla", "Que está funcionando mejor", "Que está limpia", "La vibración fuerte señala una posible falla."),
        ("abc", "En los equipos pecuarios: ¿qué significa detener un equipo de forma segura?", "Dejar de usarlo sin exponer a nadie", "Taparlo con una manta", "Tirarlo", "Detenerlo evita que el problema crezca."),
        ("abc", "{F} ¿A qué categoría corresponde E1, la balanza con error de 3 kg?", "B, retirar o programar calibración", "A, detener y avisar de inmediato", "C, conforme", "Está fuera de tolerancia, pero no hay emergencia."),
        ("abc", "{F} ¿A qué categoría corresponde E2, el ventilador sin ruidos y con protección?", "C, conforme", "A, detener y avisar de inmediato", "B, retirar", "Funciona como se espera, sin ruidos ni fallas visibles."),
        ("abc", "{F} ¿A qué categoría corresponde E3, la bomba con ruido metálico y vibración?", "A, detener y avisar de inmediato", "B, programar calibración", "C, conforme", "El ruido metálico indica una falla que puede romper el equipo."),
        ("abc", "{F} ¿A qué categoría corresponde E4, el cerco con un cable suelto en el suelo mojado?", "A, detener y avisar de inmediato", "B, retirar", "C, conforme", "El riesgo de descarga es inmediato."),
        ("abc", "{F} ¿A qué categoría corresponde E5, el termómetro con error de 0?", "C, conforme", "A, detener y avisar", "B, programar calibración", "El error es menor que la tolerancia."),
        ("=", "{F} ¿Cuánto excede el error de la balanza a la tolerancia?", "3-1", "Se resta la tolerancia al error medido.", " kg"),
        ("abc", "{F} Una compañera dice: «puedo levantar el cable suelto del cerco para ver si funciona». ¿Qué respuesta es correcta?", "Es peligroso: solo personal eléctrico autorizado interviene", "Es correcto, si usa guantes", "Es correcto, si es rápido", "El cable puede dar una descarga."),
        ("abc", "{F} El jefe quiere seguir usando la bomba E3 «hasta fin de mes». ¿Qué corresponde?", "Rechazarlo: se detiene si es seguro y la revisa el técnico", "Aceptarlo, para no parar", "Aceptarlo, si baja la presión", "Una bomba con falla puede romperse y causar un accidente."),
        ("abc", "{F} Un animal toca el cerco con el cable suelto y se asusta, corriendo hacia las personas. ¿Qué corresponde a quien lo ve?", "Alejarse de la zona de riesgo y avisar a un adulto responsable", "Acercarse a desconectar el cerco", "Tomar el cable", "Un animal asustado y un cable con electricidad son peligrosos."),
        ("abc", "En los equipos pecuarios: ¿por qué se anota en el registro el resultado real aunque sea malo?", "Porque permite corregir y deja historia del equipo", "Porque evita reparar", "Porque hace desaparecer el problema", "Un registro veraz permite actuar a tiempo."),
    ],
    ctx=("abc", "Un conocido te describe un ruido metálico en su bomba y te pregunta si puede seguir usándola. ¿Qué respondes?", "Que deje de usarla y llame a un técnico", "Que la siga usando", "Que la abra para mirar", "Una bomba con ruido metálico puede romperse y causar un accidente."),
    sc=[
        ("En los equipos pecuarios: ¿qué se hace con un cable suelto en el agua?", "Se aleja y se avisa a personal autorizado", "El riesgo de descarga es inmediato."),
        ("En los equipos pecuarios: ¿qué categoría tiene un instrumento fuera de tolerancia?", "B, retirar o programar calibración", "No es una emergencia, pero no se debe usar."),
        ("En los equipos pecuarios: ¿qué se anota en el registro?", "El resultado real", "El registro debe reflejar lo medido."),
    ],
    op=("Resultados de ejemplo del «Plantel Demo 8»: F1, bomba con humo saliendo del motor; F2, balanza con error de 2 kg y tolerancia de 1; F3, termómetro con error de 0 y tolerancia de 1; F4, ventilador normal con protección. Categorías: A, detener y avisar; B, retirar o calibrar; C, conforme. Escribe (a) la categoría de F1, F2, F3 y F4, (b) cuánto excede F2 la tolerancia, (c) quién calibra F2, (d) qué haces si ves humo.",
        "(a) F1: A; F2: B; F3: C; F4: C. (b) 2 − 1 = 1 kg. (c) El técnico de servicio. (d) Me alejo, aviso a un adulto responsable y a emergencias.",
        ["clasifica bien los cuatro equipos", "calcula el exceso", "nombra quién calibra", "se aleja y avisa"],
        ["hoja con las cuatro respuestas"],
        ["clasificar el humo como normal", "proponer calibrar por cuenta propia"],
        "Pregunta: «¿qué equipo tiene riesgo inmediato?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Clasifica en A, B o C tres resultados inventados: cable suelto en el agua, balanza con error pequeño y ventilador normal.",
    extend="Explica con un ejemplo por qué un instrumento fuera de tolerancia no se sigue usando.",
)

# ============================================================ OAM-07, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La «Lechería Demo 6» tiene 8 equipos con verificación diaria. En 100 días de ejemplo, 5 equipos tuvieron cada uno 4 días detenidos por fallas, y los otros 3 no se detuvieron. "
     "Un día detenido de un equipo cuesta $50.000 en pérdidas de ejemplo. La balanza mal calibrada (error de 2 kg sobre 50 kg) hizo que 40 animales se pesaran con 2 kg de más. Una verificación preventiva cuesta $10.000 por equipo.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular la disponibilidad de los equipos, las pérdidas por días detenidos y el costo de verificar para prevenir.",
    prior=["Sé qué es verificar y calibrar.", "Sé calcular porcentajes enteros.", "Sé multiplicar y dividir enteros."],
    explain=[
        "La disponibilidad de un equipo es el porcentaje de días en que está listo para trabajar. Se calcula con los días disponibles divididos por los días totales, por 100. Los días detenidos son los días totales menos los disponibles. La pérdida por días detenidos es los días detenidos por el costo de cada día. Un error de instrumento se mide en porcentaje del patrón: error dividido por patrón, por 100.",
        "El costo de verificar es el número de equipos por el costo de cada verificación. Si prevenir cuesta menos que las pérdidas que evita, conviene. Los valores son de ejemplo y las decisiones las toman el jefe del plantel y el técnico de servicio. Calcular no reemplaza la verificación real hecha por personal capacitado.",
        f"Ningún ahorro justifica usar un equipo con falla ni saltarse una verificación. {EMER} {AVISO}",
    ],
    vocab=[("disponibilidad", "porcentaje de días en que un equipo está listo para trabajar"), ("días detenidos", "días en que un equipo no pudo trabajar"), ("pérdida por detención", "días detenidos por el costo de cada día"), ("error porcentual", "error dividido por el patrón, por 100"), ("verificación preventiva", "revisión planificada para detectar fallas a tiempo")],
    worked=[
        ("Disponibilidad", "Un equipo de ejemplo estuvo detenido 10 días de 100. ¿Cuál es su disponibilidad?", ["Días disponibles: 100 menos 10, o sea 90.", "90 de 100 es 90 por ciento."], "90 %"),
        ("Error porcentual", "Una balanza de ejemplo marca 21 kg al medir un patrón de 20 kg. ¿Cuál es el error porcentual?", ["El error es 1 kg.", "1 entre 20, por 100, es 5."], "5 %"),
    ],
    mistakes=[("Calcular la disponibilidad dividiendo entre los días detenidos.", "Debe dividirse entre los días totales.", "Disponibilidad es días disponibles entre días totales."),
              ("Saltarse una verificación para ahorrar $10.000.", "Una falla cuesta mucho más y puede ser peligrosa.", "Se respeta el plan de verificación.")],
    T=[
        ("abc", "En los equipos pecuarios: ¿qué es la disponibilidad de un equipo?", "El porcentaje de días en que está listo para trabajar", "El número de horas que trabaja", "El precio del equipo", "La disponibilidad mide los días listos para trabajar."),
        ("abc", "En los equipos pecuarios: ¿qué es el error porcentual?", "El error dividido por el patrón, por 100", "La tolerancia dividida por la lectura", "El patrón menos la tolerancia", "El error porcentual compara el error con el patrón."),
        ("abc", "En los equipos pecuarios: ¿qué es una verificación preventiva?", "Una revisión planificada para detectar fallas a tiempo", "Una reparación después de la falla", "La compra de un equipo nuevo", "La preventiva se anticipa a las fallas."),
        ("=", "{F} ¿Cuántos días detenidos suman en total los 5 equipos con fallas?", "5*4", "Se multiplican los equipos por los días detenidos de cada uno.", " días"),
        ("=", "{F} ¿Cuál fue la pérdida total por días detenidos?", "5*4*50000", "Se multiplican los días detenidos totales por el costo de cada día.", " pesos"),
        ("=", "{F} ¿Cuál fue la disponibilidad de uno de los 5 equipos con fallas en los 100 días?", "(100-4)*100//100", "Se dividen los días disponibles entre los días totales y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el error porcentual de la balanza?", "2*100//50", "Se divide el error entre el patrón y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuánto cuesta verificar los 8 equipos una vez?", "8*10000", "Se multiplican los equipos por el costo de cada verificación.", " pesos"),
        ("=", "{F} Si verificar los 8 equipos 4 veces en los 100 días evita todas las fallas, ¿cuánto se ahorra respecto de las pérdidas?", "5*4*50000-8*4*10000", "Se resta el costo de las verificaciones a la pérdida evitada.", " pesos"),
        ("abc", "{F} Con esos números, ¿conviene verificar los equipos?", "Sí, porque el costo de verificar es menor que las pérdidas por fallas", "No, porque verificar cuesta dinero", "No se puede saber", "Verificar cuesta 320.000 y las pérdidas son 1.000.000."),
        ("abc", "{F} El jefe quiere saltarse las verificaciones para ahorrar. ¿Qué corresponde?", "Rechazarlo: una falla cuesta más y puede ser peligrosa", "Aceptarlo, para ahorrar", "Aceptarlo, si los equipos son nuevos", "Las pérdidas por fallas superan el costo de prevenir."),
        ("abc", "{F} Una estudiante quiere calibrar la balanza porque ya calculó el error. ¿Qué corresponde?", "Rechazarlo: la calibración la hace personal autorizado", "Aceptarlo, si usa un patrón", "Aceptarlo, si es poco el error", "Calcular el error no habilita para calibrar."),
        ("abc", "En los equipos pecuarios: ¿por qué un error de 2 kg en una balanza puede ser importante?", "Porque lleva a raciones o decisiones equivocadas sobre los animales", "Porque el animal engorda", "Porque la balanza se cansa", "Un peso falso afecta las decisiones."),
    ],
    ctx=("abc", "Un conocido te pregunta si vale la pena verificar sus equipos y te da solo el costo de una verificación. ¿Qué respondes?", "Que faltan las pérdidas por fallas, y que decide con un técnico de servicio", "Que sí, siempre", "Que no, nunca", "Sin pérdidas esperadas no se puede comparar."),
    sc=[
        ("En los equipos pecuarios: ¿cómo se calcula la disponibilidad?", "Días disponibles entre días totales, por 100", "La disponibilidad es un porcentaje de los días."),
        ("En los equipos pecuarios: ¿cómo se calcula el error porcentual?", "Error entre patrón, por 100", "El error porcentual compara el error con el patrón."),
        ("En los equipos pecuarios: ¿qué compara el costo de prevenir?", "Lo que cuesta verificar contra las pérdidas que evita", "Si prevenir cuesta menos que corregir, conviene hacerlo."),
    ],
    op=("Datos de ejemplo del «Plantel Demo 9»: 4 equipos; en 100 días, 2 equipos estuvieron detenidos 5 días cada uno; cada día detenido cuesta $40.000; verificar un equipo cuesta $15.000; una balanza marca 21 kg con un patrón de 20 kg. Escribe (a) los días detenidos totales, (b) la pérdida total, (c) el costo de verificar los 4 equipos, (d) el error porcentual de la balanza.",
        "(a) 2 × 5 = 10 días. (b) 10 × 40.000 = $400.000. (c) 4 × 15.000 = $60.000. (d) 1 × 100 ÷ 20 = 5 %.",
        ["calcula los días", "calcula la pérdida", "calcula el costo de verificar", "calcula el error porcentual"],
        ["hoja con las cuatro respuestas"],
        ["no multiplicar por el costo", "dividir entre los días detenidos"],
        "Pregunta: «¿cuántos días detenidos tiene cada equipo y cuántos equipos son?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Calcula la disponibilidad de un equipo detenido 8 días de 200.",
    extend="Explica con un ejemplo por qué prevenir una falla cuesta menos que corregirla.",
)
