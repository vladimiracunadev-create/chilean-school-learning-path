"""Metalurgia Extractiva TP 3.º y 4.º medio: OAE-06 (laboratorio), OAE-07 (inventario y pérdidas) y OAE-08 (marco legal del trabajo minero). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_mete_common import AVISO, EMER, build

O6 = "TP-METE-3y4-OAE-06"
O7 = "TP-METE-3y4-OAE-07"
O8 = "TP-METE-3y4-OAE-08"

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El «Laboratorio Demo» de la empresa ficticia «Minera Demo» recibe 12 muestras por día. Áreas: preparación mecánica de muestras (donde la muestra se seca, se reduce de tamaño y se divide), balanza, ensayos químicos y pruebas metalúrgicas. "
     "Un resultado de ejemplo: de una muestra de 200 gramos (g) se determinó que contiene 8 g de metal. La preparación de cada muestra toma 30 minutos (dato de ejemplo). "
     "Peligros anotados: polvo fino en la preparación, frascos con sustancias sin rótulo, vidrio roto sobre una mesa, una estufa caliente sin señal y una zona de lavado de ojos bloqueada con cajas.")
build(
    O6, 1, F,
    use="Aprenderé qué hace un laboratorio metalúrgico (preparación de muestras, ensayos químicos y pruebas metalúrgicas), cómo se calcula la ley a partir de masas y qué peligros tiene, sin aprender a realizar los ensayos.",
    prior=["Sé qué es una muestra representativa.", "Sé calcular un porcentaje con números enteros.", "Sé la jerarquía de controles."],
    explain=[
        "El laboratorio metalúrgico entrega la información con que se controla una planta. Primero se hace la preparación mecánica de la muestra: se seca, se reduce de tamaño y se divide hasta una porción que represente al material original. Luego el ensayo químico determina cuánto de un elemento contiene la porción, y de ahí sale la ley. Una prueba metalúrgica reproduce en pequeño una etapa del proceso para estimar qué resultado tendría en la planta. Los equipos e instrumentos (por ejemplo, una balanza que mide masa) deben estar verificados, limpios y con su registro antes de usarse.",
        "La ley se calcula dividiendo la masa de metal entre la masa de la porción analizada y multiplicando por 100. Si en una porción de 400 g se determinan 12 g de metal, la ley es 3 %. Para que el resultado sirva, la muestra debe ser representativa; si no lo es, el mejor análisis entrega un número que engaña.",
        f"Un laboratorio tiene peligros: sustancias químicas, vidrio, superficies calientes, polvo fino y equipos eléctricos. Las sustancias se manejan con su hoja de datos de seguridad (HDS), rótulos y personal autorizado, y los accesos a la ducha y al lavado de ojos se mantienen despejados. Este cuaderno no enseña a hacer ensayos ni a preparar soluciones. La autoridad sanitaria y la autoridad minera fiscalizan según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("laboratorio metalúrgico", "lugar donde se preparan muestras y se miden leyes y resultados para controlar una planta"), ("preparación mecánica de la muestra", "secado, reducción de tamaño y división de la muestra antes de analizarla"), ("ensayo químico", "análisis que determina cuánto de un elemento contiene una muestra"), ("prueba metalúrgica", "ensayo que reproduce en pequeño una etapa del proceso para estimar su resultado"), ("ley", "porcentaje de metal que contiene un material"), ("verificación de un equipo", "comprobación de que un equipo mide correctamente antes de usarlo"), ("lavado de ojos", "dispositivo de emergencia para enjuagar los ojos tras una salpicadura")],
    worked=[
        ("Calcular la ley", "En una porción de ejemplo de 400 g se determinan 12 g de metal. ¿Cuál es la ley?", ["Se divide 12 entre 400 y se multiplica por 100.", "El resultado es 3 por ciento."], "3 %"),
        ("Tiempo de preparación", "Una preparación de ejemplo toma 20 minutos por muestra y llegan 9 muestras. ¿Cuántos minutos se necesitan?", ["Se multiplica el tiempo por las muestras.", "20 por 9 es 180."], "180 minutos"),
    ],
    mistakes=[("Creer que una solución o un polvo sin olor no son peligrosos.", "El peligro de una sustancia no se reconoce por el olor ni por el aspecto.", "Se consulta la HDS y el rótulo, y el manejo es de personal autorizado."),
              ("Creer que leer sobre ensayos habilita para hacerlos.", "Los ensayos usan sustancias, vidrio y calor, y exigen instructor autorizado y norma vigente.", "Aprende aquí el concepto y deja los ensayos a personal autorizado.")],
    T=[
        ("abc", "En Metalurgia Extractiva: ¿qué es un ensayo químico?", "Un análisis que determina cuánto de un elemento contiene una muestra", "La reducción del tamaño de las rocas en el chancador", "La toma de la muestra en un punto de la planta", "El ensayo mide el contenido de un elemento; reducir tamaño y tomar muestras son otras tareas."),
        ("abc", "En un laboratorio metalúrgico: ¿qué es una prueba metalúrgica?", "Un ensayo que reproduce en pequeño una etapa del proceso para estimar su resultado", "La visita de un supervisor a un punto de muestreo", "El análisis del agua de una poza", "La prueba metalúrgica imita una etapa a escala pequeña; visitar o analizar agua es otra cosa."),
        ("abc", "En un laboratorio metalúrgico: ¿qué es la preparación mecánica de la muestra?", "El secado, la reducción de tamaño y la división de la muestra antes de analizarla", "El cálculo de la ley con la masa de metal", "El rótulo que lleva el frasco", "La preparación deja la muestra lista para el análisis; calcular y rotular son otros pasos."),
        ("=", "{F} ¿Cuántas muestras recibe el laboratorio en una semana de 5 días?", "12*5", "Se multiplican las muestras por día por los días de la semana.", " muestras"),
        ("=", "{F} ¿Cuál es la ley de la muestra del resultado de ejemplo, en porcentaje?", "8*100//200", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
        ("=", "{F} Con la ley de la muestra de la ficha (8 g de metal en 200 g), ¿cuántos gramos de metal habría en una porción de 500 g?", "500*4//100", "Se aplica la ley a la masa de la nueva porción.", " g"),
        ("abc", "{F} Hay frascos con sustancias sin rótulo junto a la salida. ¿Qué corresponde?", "Informar al supervisor para que personal autorizado los rotule o retire según la HDS y la norma vigente", "Abrirlos para ver qué contienen y rotularlos", "Dejarlos así hasta que alguien los necesite", "Un frasco sin rótulo no debe abrirse; lo resuelve personal autorizado con la HDS."),
        ("abc", "{F} La zona de lavado de ojos está bloqueada con cajas. ¿Cuál es el riesgo?", "Que, tras una salpicadura, no se pueda usar a tiempo y el daño sea mayor", "Que los resultados de ley salgan más bajos", "Que la balanza pese de más", "El riesgo es un daño mayor por no poder usar el dispositivo de emergencia a tiempo."),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo preparar los reactivos y hacer los ensayos». ¿Qué respuesta es correcta?", "Es falso: los ensayos exigen instructor autorizado, HDS y norma vigente", "Es cierto, si usa guantes y lentes", "Es cierto, si repite los pasos de memoria", "El EPP y la memoria no reemplazan la formación y la autorización."),
        ("abc", "{F} Durante una visita de ejemplo, ves vidrio roto y un líquido derramado en una mesa. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Recoger el vidrio con la mano para despejar la mesa", "Secar el líquido con un trapo", "Acercarse a vidrio y a un líquido desconocido puede causar lesiones; se avisa a quienes pueden actuar."),
        ("=", "{F} ¿Cuántas horas de preparación necesitan las 12 muestras de un día?", "12*30//60", "Se multiplican las muestras por los minutos de cada una y se pasa a horas.", " horas"),
        ("abc", "{F} El jefe dice que, con guantes, no hace falta rotular los frascos. ¿Cuál es la mejor objeción?", "Los guantes son EPP, la última barrera; sin rótulo no se conoce el peligro ni el manejo correcto", "Ninguna, porque los guantes protegen de cualquier sustancia", "Que los rótulos solo sirven para los frascos grandes", "El EPP no reemplaza la información del rótulo y la HDS."),
        ("=", "{F} Otra muestra de 250 g contiene 5 g de metal. ¿Cuál es su ley, en porcentaje?", "5*100//250", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
    ],
    ctx=("abc", "Un vecino te ofrece un «kit de química» sacado de una faena para que hagas análisis de rocas en tu casa. ¿Qué respondes?", "Que no, porque manejar sustancias exige instructor autorizado y norma vigente, y que se lo contarás a un adulto responsable", "Que sí, si lo haces en el patio", "Que sí, si usas lentes", "Haber leído sobre ensayos no habilita para manipular sustancias; el lugar o los lentes no cambian el riesgo."),
    sc=[
        ("En Metalurgia Extractiva: ¿cómo se calcula la ley a partir de masas?", "Dividiendo la masa de metal entre la masa de la porción y multiplicando por 100", "La ley es el porcentaje de metal de la porción."),
        ("En un laboratorio metalúrgico: ¿qué hay que mantener despejado?", "El acceso al lavado de ojos y a la ducha de emergencia", "Un dispositivo bloqueado no puede usarse a tiempo."),
        ("En un laboratorio: ¿quién realiza los ensayos con sustancias?", "Personal autorizado, con HDS y norma vigente", "Los ensayos exigen formación y autorización."),
    ],
    op=("Ficha de ejemplo: el «Laboratorio Cordón Demo» recibe 15 muestras por día. En una porción de 250 g se determinaron 15 g de metal. En una mesa hay un frasco sin rótulo y un charco de líquido desconocido. Escribe (a) cuántas muestras recibe en una semana de 5 días, (b) la ley de la porción, (c) cuántos gramos de metal habría en una porción de 1.000 g con esa ley, (d) un peligro de la mesa y su riesgo, (e) qué debe hacer una persona que ve el charco.",
        "(a) 15 × 5 = 75 muestras. (b) 15 ÷ 250 × 100 = 6 %. (c) 1.000 × 6 ÷ 100 = 60 g. (d) Peligro: un líquido desconocido y un frasco sin rótulo; riesgo: que alguien se exponga a una sustancia sin conocer su peligro. (e) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien las muestras por semana", "calcula bien la ley", "calcula bien los gramos de metal", "distingue peligro y riesgo", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["olvidar multiplicar por 100", "dividir al revés las masas", "responder que se acerca a limpiar el charco"],
        "Pregunta: «¿qué masa va arriba y cuál abajo en la división de la ley?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una porción con su masa y la masa de metal determinada y calcula la ley; luego calcula cuántos gramos de metal habría en otra porción más grande.",
    extend="Explica con un ejemplo por qué una muestra que no es representativa da un resultado engañoso aunque el análisis sea perfecto.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Laboratorio Demo». Documentos: la orden de trabajo (qué análisis se pide, de qué muestras y para cuándo), el registro de verificación de la balanza (se compara la lectura con una masa patrón; tolerancia de ejemplo: diferencia máxima de 1 gramo), "
     "la muestra de referencia (muestra de ley conocida que se analiza para comprobar que el método funciona), el blanco (ensayo hecho sin muestra para detectar contaminación) y el informe de resultados. "
     "Datos de ejemplo: masa patrón de 200 g; lectura de la balanza el lunes, 201 g; el martes, 203 g. Muestra de referencia de ley conocida de 3 %: el análisis del lunes dio 3 % y el del martes dio 5 %. "
     "Tolerancia de ejemplo para la referencia: diferencia máxima de 1 punto de ley. El martes se analizaron 8 muestras de planta, cada una dos veces. Roles: analista, jefe de laboratorio, supervisor de planta y prevencionista de riesgos.")
build(
    O6, 2, F,
    use="Aprenderé los documentos del laboratorio (orden de trabajo, verificación de balanza, muestra de referencia, blanco e informe), los roles y cómo se comprueba que un equipo y un método están dentro de tolerancia.",
    prior=["Sé qué es un ensayo químico y cómo se calcula la ley.", "Sé leer un registro escrito.", "Sé restar números enteros."],
    explain=[
        "El laboratorio ordena su trabajo con documentos. La orden de trabajo dice qué análisis se pide, de qué muestras y para cuándo. El registro de verificación de un equipo anota que se comprobó que mide bien: en una balanza se pesa una masa patrón, cuyo valor se conoce, y se compara la lectura con ese valor; si la diferencia supera la tolerancia, la balanza no se usa para informar resultados hasta que personal autorizado la revise. El informe de resultados entrega los valores medidos.",
        "Para vigilar el método se usan dos controles. La muestra de referencia es una muestra de ley conocida: si el análisis da un valor lejos de lo conocido, el método no está funcionando bien ese día. El blanco es un ensayo hecho sin muestra: si da un resultado distinto de cero, hay contaminación. Si un control sale fuera de tolerancia, los resultados de ese día se retienen, se informa al jefe de laboratorio y se revisan; nunca se anota un valor distinto del leído. Por ejemplo, con una masa patrón de 100 g, una lectura de 102 g tiene una diferencia de 2 g.",
        f"Roles: el analista realiza y registra los ensayos, el jefe de laboratorio decide qué hacer ante un control fuera de tolerancia, el supervisor de planta recibe los resultados y el prevencionista asesora en riesgos. Cada firma certifica que quien firma comprobó lo que declara. {EMER} {AVISO}",
    ],
    vocab=[("orden de trabajo", "documento que dice qué análisis se pide, de qué muestras y para cuándo"), ("masa patrón", "masa de valor conocido con que se verifica una balanza"), ("tolerancia", "diferencia máxima aceptada entre un valor medido y el esperado"), ("muestra de referencia", "muestra de ley conocida que se analiza para comprobar que el método funciona"), ("blanco", "ensayo hecho sin muestra para detectar contaminación"), ("jefe de laboratorio", "persona que decide qué hacer ante un control fuera de tolerancia")],
    worked=[
        ("Verificar la balanza", "Una balanza de ejemplo lee 102 g al pesar una masa patrón de 100 g. La tolerancia es 1 g. ¿Cumple?", ["La diferencia es 102 menos 100, es decir 2 g.", "2 supera la tolerancia de 1 g."], "No cumple"),
        ("Referencia de ley", "Una muestra de referencia de ejemplo tiene ley conocida de 4 % y el análisis da 5 %. La tolerancia es 1 punto. ¿Cumple?", ["La diferencia es 5 menos 4, es decir 1 punto.", "Una diferencia igual a la tolerancia cumple."], "Sí, cumple"),
    ],
    mistakes=[("Seguir usando una balanza que no pasó la verificación porque «solo se desvía un poco».", "Fuera de tolerancia, los resultados no son confiables.", "Se informa al jefe de laboratorio y la balanza no se usa hasta que la revise personal autorizado."),
              ("Anotar el valor patrón en vez de la lectura real para evitar la revisión.", "Un registro falso oculta que el equipo está fuera de tolerancia.", "Se anota la lectura real y se informa.")],
    T=[
        ("abc", "En un laboratorio metalúrgico: ¿qué es una muestra de referencia?", "Una muestra de ley conocida que se analiza para comprobar que el método funciona", "Una muestra que se toma en el punto más alejado de la planta", "Una copia de la orden de trabajo", "La referencia tiene ley conocida y sirve de control; no es una muestra de planta ni un documento."),
        ("abc", "En un laboratorio metalúrgico: ¿qué es un blanco?", "Un ensayo hecho sin muestra para detectar contaminación", "Una muestra sin rótulo", "Un resultado igual a cero en el informe", "El blanco se hace sin muestra; su valor mostraría contaminación."),
        ("abc", "En un laboratorio metalúrgico: ¿qué indica la orden de trabajo?", "Qué análisis se pide, de qué muestras y para cuándo", "Cuántos gramos de metal tiene cada muestra", "Qué tolerancia tiene la balanza", "La orden de trabajo organiza el pedido; los resultados y las tolerancias están en otros registros."),
        ("=", "{F} ¿Cuántos gramos de diferencia tiene la lectura de la balanza del lunes respecto de la masa patrón?", "201-200", "Se resta la masa patrón a la lectura.", " g"),
        ("=", "{F} ¿Cuántos gramos de diferencia tiene la lectura del martes respecto de la masa patrón?", "203-200", "Se resta la masa patrón a la lectura.", " g"),
        ("abc", "{F} ¿Cumplió la balanza la tolerancia el lunes?", "Sí, porque la diferencia de 1 g no supera la tolerancia de 1 g", "No, porque la lectura no fue exactamente 200 g", "No, porque 1 g es igual a la tolerancia y debería ser menor", "La tolerancia permite diferencias de hasta 1 g, incluida exactamente 1 g."),
        ("abc", "{F} Con la lectura del martes, ¿qué corresponde hacer con la balanza?", "No usarla para informar resultados y avisar al jefe de laboratorio para que personal autorizado la revise", "Seguir usándola, porque la diferencia es pequeña", "Anotar 200 g en el registro para evitar la revisión", "Fuera de tolerancia, la balanza no es confiable; alterar el registro oculta el problema."),
        ("=", "{F} ¿Cuántos puntos de ley hay entre el análisis de la referencia del martes y su ley conocida?", "5-3", "Se resta la ley conocida al resultado del análisis.", " puntos"),
        ("abc", "{F} Con la referencia del martes, ¿qué se concluye sobre los resultados de ese día?", "Que el método no funcionó bien ese día y los resultados se retienen hasta revisarlos", "Que los resultados de planta son más altos y se informan igual", "Que el resultado es un valor de ley verdadero", "Una referencia fuera de tolerancia indica un problema del método."),
        ("abc", "{F} ¿Quién decide qué hacer con los resultados cuando un control sale fuera de tolerancia?", "El jefe de laboratorio", "El supervisor de planta, sin consultar al laboratorio", "El prevencionista de riesgos", "La decisión sobre el método y los resultados es del jefe de laboratorio."),
        ("abc", "{F} Un compañero dice que si el blanco da un valor distinto de cero «no importa». ¿Cuál es la mejor respuesta?", "Importa: puede indicar contaminación, y se informa para revisar antes de entregar resultados", "No importa, porque el blanco no tiene muestra", "Importa solo si el valor del blanco es mayor que la ley de la referencia", "Un blanco con valor indica que algo está agregando señal al ensayo."),
        ("=", "{F} El martes se analizaron 8 muestras de planta, cada una dos veces. ¿Cuántos análisis hay que revisar?", "8*2", "Se multiplican las muestras por los análisis de cada una.", " análisis"),
        ("abc", "{F} Un compañero propone anotar 200 g en el registro de verificación del martes «para no atrasar la entrega». ¿Cuál es la mejor respuesta?", "No se hace: se anota la lectura real, se informa y se espera la decisión del jefe de laboratorio", "Se puede, si después se arregla la balanza", "Se puede, si el supervisor de planta lo pide", "Un registro falso oculta que la balanza está fuera de tolerancia."),
    ],
    ctx=("abc", "Un compañero de práctica te dice que firmó por ti la verificación de la balanza porque estabas ocupado. ¿Qué respondes?", "Que no se firma por otra persona, y que lo consultarás con un adulto responsable para dejar el registro correcto", "Que está bien, porque la balanza estaba bien", "Que está bien, si no lo cuenta a nadie", "Una firma certifica una comprobación hecha por quien firma; firmar por otro es un registro falso."),
    sc=[
        ("En un laboratorio metalúrgico: ¿qué es la tolerancia?", "La diferencia máxima aceptada entre un valor medido y el esperado", "La tolerancia fija cuándo un equipo o método está dentro de lo aceptado."),
        ("En un laboratorio metalúrgico: ¿para qué sirve una masa patrón?", "Para verificar que una balanza mide correctamente", "La masa patrón tiene un valor conocido con que se compara la lectura."),
        ("En el control del laboratorio: ¿qué se hace con un control fuera de tolerancia?", "Se informa al jefe de laboratorio y se retienen los resultados", "Los resultados de un método dudoso no se entregan."),
    ],
    op=("Ficha de ejemplo: «Laboratorio Cordón Demo». Masa patrón de 500 g; tolerancia de ejemplo de 1 g. Lectura de la balanza: lunes, 500 g; martes, 502 g. Muestra de referencia de ley conocida de 4 %: lunes, 4 %; martes, 4 %. Escribe (a) la diferencia de la balanza cada día, (b) qué día queda fuera de tolerancia, (c) qué haces con la balanza ese día, (d) si la referencia indica problemas el martes, (e) quién decide qué hacer.",
        "(a) Lunes: 500 − 500 = 0 g; martes: 502 − 500 = 2 g. (b) El martes, porque 2 g supera la tolerancia de 1 g. (c) No usarla para informar resultados, informar al jefe de laboratorio y esperar la revisión por personal autorizado. (d) No: la referencia dio 4 %, igual a su ley conocida. (e) El jefe de laboratorio.",
        ["calcula bien las diferencias", "identifica el día fuera de tolerancia", "retiene la balanza e informa", "interpreta bien la referencia", "nombra al jefe de laboratorio"],
        ["hoja con las cinco respuestas"],
        ["decir que 2 g está dentro de tolerancia", "alterar el registro", "confundir la balanza con la referencia"],
        "Pregunta: «¿qué diferencia máxima permite la tolerancia y cuál fue la del martes?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una masa patrón, una tolerancia y dos lecturas de balanza, y decide qué día queda fuera de tolerancia.",
    extend="Explica con un ejemplo por qué la balanza y la muestra de referencia controlan cosas distintas.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (resultados de ejemplo, inventados). Ensayos del «Laboratorio Demo»; cada fila indica la masa de la porción analizada y la masa de metal determinada. Muestra S-1: 250 g y 10 g. Muestra S-2: 200 g y 12 g. "
     "Muestra S-3: 500 g y 10 g; duplicado de S-3: 400 g y 12 g. Muestra S-4: 250 g y 15 g; duplicado de S-4: 200 g y 8 g. Muestra de referencia R-1 (ley certificada de 6 %): 300 g y 15 g. "
     "Criterios de ejemplo: entre original y duplicado, diferencia máxima de 1 punto de ley; entre la referencia y su ley certificada, diferencia máxima de 1 punto (una diferencia de exactamente 1 punto cumple).")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel resultados de un laboratorio: calcular leyes a partir de masas, comprobar duplicados y la referencia contra un criterio, y decidir qué informar cuando un resultado no cumple.",
    prior=["Sé calcular la ley con masas.", "Sé qué son duplicado y muestra de referencia.", "Sé comparar un dato con un criterio."],
    explain=[
        "Un laboratorio no solo entrega números: comprueba que merecen confianza. Primero calcula cada ley como masa de metal dividida entre masa de la porción, por cien. Después aplica los controles. En el duplicado se analiza la misma muestra dos veces y se compara la diferencia con el máximo aceptado. En la muestra de referencia se compara el valor obtenido con su ley certificada. Un resultado fuera de control es el que no cumple su criterio.",
        "Si un resultado queda fuera de control, no se promedia con el otro ni se elige el que parece mejor. El analista informa al jefe de laboratorio, quien decide si se repite el análisis, se revisa la preparación o se investiga el método. Mientras tanto, el informe dice que el resultado está pendiente de repetición. Por ejemplo, una muestra de 100 g con 4 g de metal tiene ley 4 %, y su duplicado de 200 g con 6 g tiene ley 3 %: la diferencia es 1 punto y cumple un máximo de 1.",
        f"Cada resultado conserva su registro original: no se borra ni se reemplaza para que cuadre. Estos números son de ejemplo y los reales los generan personas autorizadas. {EMER} {AVISO}",
    ],
    vocab=[("resultado fuera de control", "resultado que no cumple su criterio de calidad"), ("ley certificada", "ley conocida de una muestra de referencia"), ("diferencia entre duplicados", "diferencia de ley entre el análisis original y su duplicado"), ("pendiente de repetición", "estado de un resultado que no puede informarse hasta repetir el análisis"), ("registro original", "anotación del valor tal como se leyó, que no se borra ni se cambia")],
    worked=[
        ("Duplicado dentro del límite", "Una muestra de ejemplo de 100 g con 4 g de metal y su duplicado de 200 g con 6 g. El máximo de diferencia es 1 punto. ¿Cumple?", ["Primera ley: 4 por ciento. Segunda ley: 3 por ciento.", "La diferencia es 1 punto, que no supera el máximo."], "Sí, cumple"),
        ("Referencia fuera del límite", "Una referencia de ejemplo tiene ley certificada de 5 % y el análisis da 8 %. El máximo es 1 punto. ¿Cumple?", ["La diferencia es 8 menos 5, es decir 3 puntos.", "3 supera el máximo de 1."], "No cumple"),
    ],
    mistakes=[("Promediar un original con un duplicado fuera de control para «arreglar» el resultado.", "El promedio oculta que los dos análisis no coinciden y que algo falló.", "Se informa al jefe de laboratorio y el resultado queda pendiente de repetición."),
              ("Repetir el análisis hasta que salga lo esperado y anotar solo ese.", "Se esconden los resultados que no gustaron y se pierde la evidencia del problema.", "Se conservan todos los resultados, con su registro original.")],
    T=[
        ("abc", "En el control de un laboratorio: ¿qué es un resultado fuera de control?", "Un resultado que no cumple su criterio de calidad, como un duplicado muy distinto del original", "Un resultado con una ley alta", "Un resultado que no lleva firma", "Fuera de control es no cumplir el criterio; una ley alta o una firma ausente son otras situaciones."),
        ("abc", "En un laboratorio: ¿para qué se analiza un duplicado?", "Para comprobar que el análisis de la misma muestra se repite dentro de un límite", "Para tener una segunda muestra de otro punto", "Para duplicar la cantidad de metal informada", "El duplicado comprueba la repetibilidad del análisis."),
        ("abc", "En un laboratorio: ¿para qué se analiza una muestra de referencia?", "Para comprobar que el método entrega un valor cercano a la ley certificada", "Para saber cuánto metal tiene la planta", "Para reemplazar el análisis de las muestras de planta", "La referencia tiene ley certificada y sirve de control del método."),
        ("=", "{F} ¿Cuál es la ley de la muestra S-1, en porcentaje?", "10*100//250", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la ley de la muestra S-2, en porcentaje?", "12*100//200", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la ley de la muestra S-3, en porcentaje?", "10*100//500", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la ley del duplicado de S-3, en porcentaje?", "12*100//400", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cumple la repetibilidad la muestra S-3 con su duplicado?", "Sí, porque la diferencia es 1 punto y el máximo es 1", "No, porque los dos resultados no son iguales", "No, porque las porciones tienen masas distintas", "La diferencia de 1 punto es igual al máximo y cumple."),
        ("=", "{F} ¿Cuál es la ley que obtuvo el laboratorio para la referencia R-1, en porcentaje?", "15*100//300", "Se divide la masa de metal entre la masa de la porción y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos puntos de ley hay entre los análisis original y duplicado de S-4?", "15*100//250-8*100//200", "Se calcula cada ley y se resta la menor a la mayor.", " puntos"),
        ("abc", "{F} ¿Cumple la referencia R-1 su criterio?", "Sí, porque 5 % difiere en 1 punto de la ley certificada de 6 %", "No, porque 5 % es menor que 6 %", "No, porque la referencia debe dar exactamente 6 %", "El criterio permite diferencias de hasta 1 punto, incluida exactamente 1."),
        ("abc", "{F} Con el resultado de S-4, ¿qué corresponde?", "Informar al jefe de laboratorio para que decida si se repite el análisis, y dejar el resultado pendiente", "Promediar 6 % y 4 % y entregar 5 %", "Elegir el 6 %, que es la ley más alta", "Un duplicado fuera de criterio se informa; promediar o elegir oculta el problema."),
        ("abc", "{F} Mientras no se repita el análisis de S-4, ¿qué debe decir el informe?", "Que el resultado está pendiente de repetición por no cumplir la repetibilidad", "Que la ley es 5 %", "Que la ley es 6 %", "Un resultado fuera de control no se entrega como válido hasta repetirlo."),
    ],
    ctx=("abc", "Un compañero propone repetir el análisis de S-4 hasta que salga un valor parecido y anotar solo ese. ¿Qué respondes?", "Que no, porque se conservan todos los resultados, y que lo consultarás con un adulto responsable", "Que sí, porque así el informe se ve mejor", "Que sí, si borra el primero", "Esconder resultados incómodos quita la evidencia de un posible problema."),
    sc=[
        ("En un laboratorio metalúrgico: ¿cómo se comprueba una muestra de referencia?", "Comparando el valor obtenido con su ley certificada", "La diferencia con la ley certificada se compara con la tolerancia."),
        ("En un laboratorio: ¿qué se hace con un duplicado fuera del criterio?", "Se informa y el resultado queda pendiente de repetición", "Un duplicado fuera de criterio no se promedia ni se descarta."),
        ("En un laboratorio: ¿qué es el registro original de un resultado?", "La anotación del valor tal como se leyó, que no se borra ni se cambia", "El registro original conserva la evidencia."),
    ],
    op=("Ficha de ejemplo: «Laboratorio Cordón Demo». Muestra T-1: 200 g y 6 g de metal; duplicado de T-1: 250 g y 5 g. Muestra T-2: 400 g y 8 g; duplicado de T-2: 250 g y 10 g. Criterio de ejemplo: diferencia máxima de 1 punto de ley entre original y duplicado. Escribe (a) las cuatro leyes, (b) qué par cumple y cuál no, (c) qué haces con el que no cumple, (d) qué dice el informe de ese resultado mientras tanto.",
        "(a) T-1: 6 ÷ 200 × 100 = 3 %; duplicado de T-1: 5 ÷ 250 × 100 = 2 %; T-2: 8 ÷ 400 × 100 = 2 %; duplicado de T-2: 10 ÷ 250 × 100 = 4 %. (b) T-1 cumple (diferencia de 1 punto); T-2 no cumple (diferencia de 2 puntos). (c) Informar al jefe de laboratorio para que decida si se repite el análisis, sin promediar ni descartar. (d) Que el resultado está pendiente de repetición.",
        ["calcula bien las cuatro leyes", "concluye bien cuál cumple", "informa y no promedia", "indica pendiente de repetición"],
        ["hoja con las cuatro respuestas"],
        ["promediar un par fuera de control", "dividir al revés las masas", "descartar el duplicado"],
        "Pregunta: «¿cuántos puntos de ley hay de diferencia en cada par?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un original y un duplicado con masas y metal, calcula sus leyes y decide si cumplen un máximo de 1 punto.",
    extend="Explica con un ejemplo por qué promediar un par fuera de control oculta información importante.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (prueba de ejemplo, inventada). Prueba metalúrgica a escala de laboratorio, en papel. Cabeza (lo que entra a la prueba): 1.000 g con ley analizada de 2 % (20 g de metal). Resultados: concentrado, 40 g con ley de 30 % (12 g de metal); relave, 960 g con 7 g de metal. "
     "La cabeza calculada es el metal del concentrado más el del relave. Criterio de ejemplo: la cabeza calculada no debe diferir de la cabeza analizada en más de 2 g de metal (10 % del metal analizado). "
     "En esta prueba, la recuperación se calcula sobre el metal de la cabeza analizada.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo en una prueba de laboratorio: calcular la cabeza calculada, la recuperación y la razón de concentración, y comprobar si el balance de la prueba es coherente.",
    prior=["Sé calcular la ley con masas.", "Sé calcular recuperación y razón de concentración.", "Sé comparar un dato con un criterio."],
    explain=[
        "En una prueba metalúrgica a escala de laboratorio se parte de una cabeza, que es el material que entra a la prueba. Se analiza su ley y de ahí se calcula el metal que contiene. Al terminar se obtienen productos, por ejemplo concentrado y relave, y se analiza el metal de cada uno. La cabeza calculada es la suma del metal de los productos, y se compara con el metal de la cabeza analizada: si la diferencia supera lo aceptado, hay un error de pesaje, de análisis o de preparación, y los resultados no se usan hasta revisarlos.",
        "Con los resultados coherentes se calculan la recuperación, que es el metal del concentrado dividido por el de la cabeza y multiplicado por 100, y la razón de concentración, que son los gramos de cabeza divididos por los del concentrado. Ejemplo: cabeza de 500 g con 10 g de metal, concentrado con 6 g y relave con 3 g: la cabeza calculada es 9 g, la diferencia es 1 g y la recuperación es 60 %.",
        f"Los balances y cálculos se registran con los valores originales, y la prueba misma la realiza personal autorizado; este cuaderno solo enseña a leer y calcular sus resultados. {EMER} {AVISO}",
    ],
    vocab=[("cabeza", "material que entra a una prueba o a una etapa"), ("cabeza analizada", "metal de la cabeza según su análisis directo"), ("cabeza calculada", "suma del metal de los productos de la prueba"), ("coherencia del balance", "grado en que la cabeza calculada coincide con la analizada dentro de lo aceptado"), ("recuperación de la prueba", "metal del concentrado dividido por el metal de la cabeza, en porcentaje")],
    worked=[
        ("Cabeza calculada", "Una prueba de ejemplo tiene concentrado con 6 g de metal y relave con 3 g. ¿Cuántos gramos de metal suma la cabeza calculada?", ["Se suman los gramos de metal de los productos.", "6 más 3 son 9."], "9 g"),
        ("Recuperación de la prueba", "El concentrado tiene 6 g de metal y la cabeza analizada 10 g. ¿Cuál es la recuperación?", ["Se divide 6 entre 10 y se multiplica por 100.", "El resultado es 60 por ciento."], "60 %"),
    ],
    mistakes=[("Calcular la recuperación con las masas de los productos en vez de con el metal.", "Una prueba puede dar poca masa de concentrado y mucho metal recuperado.", "La recuperación compara el metal del concentrado con el de la cabeza."),
              ("Ajustar el metal del relave para que la cabeza calculada coincida con la analizada.", "Un balance forzado oculta errores reales de pesaje o de análisis.", "Se informa la diferencia y se revisa la prueba.")],
    T=[
        ("abc", "En una prueba metalúrgica: ¿qué es la cabeza?", "El material que entra a la prueba", "El producto rico en metal que sale de la prueba", "El material que se descarta al final", "La cabeza es la entrada; el producto rico es el concentrado y lo descartado es el relave."),
        ("abc", "En una prueba metalúrgica: ¿qué es la cabeza calculada?", "La suma del metal de los productos de la prueba", "La ley de cabeza informada por la mina", "La ley de la muestra de referencia", "La cabeza calculada se obtiene sumando el metal de concentrado y relave."),
        ("abc", "En una prueba metalúrgica: ¿por qué se compara la cabeza calculada con la analizada?", "Para comprobar que los pesajes y los análisis de la prueba son coherentes", "Para aumentar la ley del concentrado", "Para elegir otro laboratorio", "Si no coinciden dentro de lo aceptado, hay un error por revisar."),
        ("=", "{F} ¿Cuántos gramos de metal tiene la cabeza analizada?", "1000*2//100", "Se multiplican los gramos por la ley y se divide por 100.", " g"),
        ("=", "{F} ¿Cuántos gramos de metal tiene el concentrado?", "40*30//100", "Se multiplican los gramos por la ley y se divide por 100.", " g"),
        ("=", "{F} ¿Cuántos gramos de metal suma la cabeza calculada?", "40*30//100+7", "Se suma el metal del concentrado y el del relave.", " g"),
        ("=", "{F} ¿Cuántos gramos de diferencia hay entre la cabeza analizada y la calculada?", "1000*2//100-(40*30//100+7)", "Se resta la cabeza calculada a la analizada.", " g"),
        ("abc", "{F} ¿Es coherente el balance de la prueba?", "Sí, porque la diferencia de 1 g no supera el máximo de 2 g", "No, porque existe una diferencia", "No, porque 1 g es menor que 2 g", "El criterio acepta hasta 2 g de diferencia, y 1 g está dentro."),
        ("=", "{F} ¿Cuál es la recuperación de la prueba, en porcentaje?", "12*100//20", "Se divide el metal del concentrado entre el de la cabeza analizada y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es la razón de concentración de la prueba?", "1000//40", "Se dividen los gramos de cabeza entre los del concentrado.", ""),
        ("abc", "{F} Si la diferencia entre cabeza analizada y calculada superara el máximo, ¿qué indicaría?", "Un error de pesaje, de análisis o de preparación que hay que revisar", "Que la planta es excelente", "Que el concentrado tiene más ley", "Una diferencia grande muestra datos incoherentes, no un buen resultado."),
        ("=", "{F} Si el relave hubiera informado solo 3 g de metal, ¿cuántos gramos de diferencia habría entre la cabeza analizada y la calculada?", "20-(12+3)", "Se suma el metal de los productos y se resta a la cabeza analizada.", " g"),
        ("abc", "{F} Con 5 g de diferencia y un máximo de 2 g, ¿qué corresponde?", "Informar al jefe de laboratorio y revisar pesajes y análisis, sin ajustar ningún dato", "Subir el metal del relave hasta que cuadre", "Entregar la recuperación igual, porque no cambia mucho", "Una diferencia mayor que el máximo se investiga; ajustar datos oculta el error."),
    ],
    ctx=("abc", "Un compañero propone cambiar el metal del relave de 7 g a 8 g para que la cabeza calculada coincida con la analizada. ¿Qué respondes?", "Que no, porque un balance forzado oculta errores, y que lo consultarás con un adulto responsable", "Que sí, porque es solo 1 g", "Que sí, si lo anota con lápiz", "Cambiar un dato para que cuadre quita la evidencia de un posible error."),
    sc=[
        ("En una prueba metalúrgica: ¿cómo se calcula la recuperación?", "Dividiendo el metal del concentrado entre el de la cabeza y multiplicando por 100", "La recuperación compara metal con metal."),
        ("En una prueba metalúrgica: ¿cómo se calcula la razón de concentración?", "Dividiendo los gramos de cabeza entre los gramos de concentrado", "Compara la masa que entra con la de concentrado."),
        ("En una prueba de laboratorio: ¿qué se hace si el balance es incoherente?", "Se informa y se revisan pesajes y análisis", "Una diferencia grande muestra un error por encontrar."),
    ],
    op=("Ficha de ejemplo: prueba a escala de laboratorio en el «Laboratorio Cordón Demo». Cabeza: 800 g con ley analizada de 5 % (40 g de metal). Concentrado: 100 g con ley de 30 %. Relave: 700 g con 8 g de metal. Criterio de ejemplo: diferencia máxima de 4 g entre cabeza analizada y calculada. Escribe (a) el metal del concentrado, (b) la cabeza calculada, (c) si el balance es coherente, (d) la recuperación, (e) la razón de concentración.",
        "(a) 100 × 30 ÷ 100 = 30 g. (b) 30 + 8 = 38 g. (c) La diferencia es 40 − 38 = 2 g, que no supera el máximo de 4 g: es coherente. (d) 30 ÷ 40 × 100 = 75 %. (e) 800 ÷ 100 = 8.",
        ["calcula bien el metal del concentrado", "calcula bien la cabeza calculada", "concluye que es coherente", "calcula bien la recuperación", "calcula bien la razón de concentración"],
        ["hoja con las cinco respuestas"],
        ["usar las masas en vez del metal", "olvidar sumar el relave", "decir que no es coherente por haber diferencia"],
        "Pregunta: «¿qué dos cantidades de metal comparas para el balance?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una prueba con cabeza, concentrado y relave y calcula la cabeza calculada, la diferencia y la recuperación.",
    extend="Explica con un ejemplo por qué una prueba puede tener buena recuperación y aun así un balance incoherente.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (comparación de ejemplo, inventada). El «Laboratorio Demo» compara dos métodos de análisis para el control diario de una planta (datos de ejemplo). Método A: resultado en 2 horas, costo de $12.000 por análisis, diferencia típica entre duplicados de 2 puntos de ley. "
     "Método B: resultado en 6 horas, costo de $20.000 por análisis, diferencia típica entre duplicados de 1 punto de ley. La planta necesita 30 análisis por día; la decisión de proceso exige una diferencia entre duplicados de 1 punto como máximo y un resultado en 8 horas o menos. "
     "Control de la muestra de referencia (ley certificada de 5 %) en seis días seguidos: 5, 5, 6, 4, 5 y 7 por ciento; límites de control de ejemplo: de 4 % a 6 %, ambos incluidos.")
build(
    O6, 5, F,
    use="Aprenderé a comparar dos métodos de análisis con requisitos de plazo y repetibilidad, a calcular costos y a leer un control de la muestra de referencia para decidir cuándo investigar.",
    prior=["Sé qué son duplicado y muestra de referencia.", "Sé comparar un dato con un criterio.", "Sé multiplicar y restar números enteros."],
    explain=[
        "Al comparar métodos de análisis se revisan primero los requisitos que la planta necesita: el plazo en que llega el resultado y la repetibilidad, es decir, cuánto se parecen dos análisis de la misma muestra. Un método que no cumple un requisito no puede elegirse, aunque sea el más barato o el más rápido. Entre los que cumplen, se compara el costo y se explica qué se acepta ceder, por ejemplo más tiempo o más gasto.",
        "El control de la muestra de referencia se registra día a día. Los límites de control marcan entre qué valores es normal que caiga el resultado; si un día queda fuera, se investiga antes de informar los resultados de ese día. Por ejemplo, con ley certificada de 7 % y límites de 6 % a 8 %, un resultado de 9 % queda 1 punto por encima del límite superior.",
        f"La recomendación cita el requisito que decide, las cifras y lo que se acepta ceder. Las cifras son de ejemplo; los métodos reales los fijan el laboratorio y la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("requisito del método", "condición que un método debe cumplir para poder elegirse, como plazo y repetibilidad"), ("plazo del resultado", "tiempo entre recibir la muestra y entregar el resultado"), ("límite de control", "valor máximo o mínimo que se acepta para un resultado de control"), ("investigar", "buscar la causa de un resultado fuera de límites antes de informar"), ("recomendación", "propuesta escrita con la alternativa elegida, el requisito que decide y lo que se cede")],
    worked=[
        ("Revisar requisitos primero", "Dos métodos de ejemplo: uno da duplicados con 4 puntos de diferencia y otro con 2 puntos. El requisito es 3 puntos como máximo. ¿Cuál puede elegirse?", ["4 supera el máximo de 3.", "2 está dentro del máximo."], "El segundo"),
        ("Control fuera de límites", "Una referencia de ejemplo tiene límites de 6 % a 8 % y un día da 9 %. ¿Cuántos puntos queda sobre el límite superior?", ["El límite superior es 8.", "9 menos 8 es 1 punto."], "1 punto"),
    ],
    mistakes=[("Elegir el método más barato sin revisar si cumple la repetibilidad y el plazo.", "Un método que no cumple un requisito entrega resultados que no sirven para decidir.", "Primero se revisan los requisitos y después se compara el costo."),
              ("Informar los resultados de un día con la referencia fuera de límites «porque ayer salió bien».", "Que un día salga bien no garantiza otro; la referencia fuera de límites indica un posible problema del método.", "Se investiga antes de informar los resultados de ese día.")],
    T=[
        ("abc", "En el control de un laboratorio: ¿qué es un límite de control?", "El valor máximo o mínimo que se acepta para un resultado de control", "La meta de producción de la planta", "El peso máximo de una muestra", "Un límite de control marca hasta dónde un resultado de control se considera normal."),
        ("abc", "En el control de un laboratorio: ¿para qué se registra la muestra de referencia cada día?", "Para detectar a tiempo si el método dejó de funcionar bien", "Para aumentar la ley de las muestras de planta", "Para contar cuántas muestras llegaron", "El registro diario permite ver cuándo el método se desvía."),
        ("abc", "En la comparación de métodos de análisis: ¿por qué no se elige solo por costo?", "Porque primero debe cumplir los requisitos de plazo y repetibilidad", "Porque el costo nunca importa", "Porque el método más barato siempre es el más lento", "Un método que no cumple los requisitos no sirve, aunque sea barato."),
        ("=", "{F} ¿Cuál es el costo diario del método A, en pesos?", "30*12000", "Se multiplican los análisis por día por el costo de cada uno.", " pesos"),
        ("=", "{F} ¿Cuál es el costo diario del método B, en pesos?", "30*20000", "Se multiplican los análisis por día por el costo de cada uno.", " pesos"),
        ("abc", "{F} ¿Qué método cumple los requisitos de la planta?", "El B, porque da duplicados con 1 punto y resultado en 6 horas", "El A, porque es más barato y más rápido", "Ambos, porque los dos entregan resultados en menos de 8 horas", "El método A tiene 2 puntos de diferencia entre duplicados, sobre el máximo de 1."),
        ("=", "{F} ¿Cuántos pesos más por día cuesta el método B que el A?", "30*20000-30*12000", "Se restan los costos diarios.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta el método B en una semana de 5 días?", "5*30*20000", "Se multiplican los días por los análisis diarios y el costo de cada uno.", " pesos"),
        ("abc", "{F} ¿En qué día salió el resultado de la referencia fuera de los límites de control?", "En el sexto día, con 7 %, que supera el límite de 6 %", "En el cuarto día, con 4 %, que es el límite inferior", "En el tercer día, con 6 %, que es el límite superior", "Los límites incluyen 4 % y 6 %, así que solo el 7 % del sexto día queda fuera."),
        ("=", "{F} ¿Cuántos puntos sobre el límite superior quedó el resultado del sexto día?", "7-6", "Se resta el límite superior al resultado.", " punto"),
        ("abc", "{F} Con el resultado del sexto día, ¿qué corresponde hacer con los análisis de planta de ese día?", "Retenerlos, informar al jefe de laboratorio e investigar antes de entregarlos", "Entregarlos igual, porque los otros cinco días salió bien", "Cambiar el 7 % por 6 % para que cumpla", "Una referencia fuera de límites indica un posible problema; se investiga antes de informar."),
        ("=", "{F} Si revisar cada análisis de ese día tomara 20 minutos y hay 30 análisis, ¿cuántas horas tomaría revisar todos?", "30*20//60", "Se multiplican los análisis por los minutos de cada uno y se pasa a horas.", " horas"),
        ("abc", "{F} El jefe pide una recomendación. ¿Cuál es la mejor?", "Elegir el método B, porque cumple repetibilidad y plazo, aceptando su mayor costo y su mayor demora, e investigar el control del sexto día", "Elegir el método A, porque es más barato", "Elegir el método B, porque da el resultado más rápido que el A", "El método B cumple los requisitos, pero tarda más y cuesta más que el A, no menos."),
    ],
    ctx=("abc", "Un compañero propone omitir hoy la muestra de referencia porque «ayer salió bien». ¿Qué respondes?", "Que la referencia se analiza todos los días y se registra, y que lo consultarás con un adulto responsable", "Que sí, porque ayer salió bien", "Que sí, si no hay tiempo", "El control diario es lo que detecta a tiempo una desviación del método."),
    sc=[
        ("En la comparación de métodos de análisis: ¿qué se revisa antes de comparar el costo?", "Si cumplen los requisitos de plazo y repetibilidad", "Un método que no cumple no puede elegirse."),
        ("En el control diario de laboratorio: ¿qué se hace si la referencia sale fuera de los límites?", "Se investiga antes de informar los resultados de ese día", "Un control fuera de límites indica un posible problema."),
        ("En una recomendación de laboratorio: ¿qué se cita además de las cifras?", "El requisito que decide y lo que se acepta ceder", "Así la decisión puede revisarse después con las mismas cifras."),
    ],
    op=("Ficha de ejemplo: el «Laboratorio Cordón Demo» compara el método X (resultado en 3 horas, $15.000 por análisis, duplicados con 1 punto de diferencia) con el método Y (resultado en 1 hora, $9.000 por análisis, duplicados con 3 puntos de diferencia). La planta necesita 20 análisis por día, con duplicados de 2 puntos como máximo y resultado en 4 horas o menos. Control de la referencia (ley certificada de 3 %, límites de 2 % a 4 %): 3, 4 y 5 por ciento en tres días. Escribe (a) qué método cumple los requisitos, (b) su costo diario, (c) qué día queda fuera de límites y por cuántos puntos, (d) qué haces con los análisis de ese día.",
        "(a) El método X, porque su diferencia de 1 punto no supera 2 y su resultado llega en 3 horas; el método Y tiene 3 puntos de diferencia. (b) 20 × 15.000 = 300.000 pesos. (c) El tercer día, con 5 %, queda 1 punto sobre el límite de 4 %. (d) Retenerlos, informar al jefe de laboratorio e investigar antes de entregarlos.",
        ["identifica el método que cumple", "calcula bien el costo diario", "identifica el día y los puntos", "retiene e investiga"],
        ["hoja con las cuatro respuestas"],
        ["elegir Y por ser más barato", "decir que 4 % queda fuera de los límites", "informar los análisis igual"],
        "Pregunta: «¿qué requisito incumple el método más barato?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Compara dos métodos inventados con requisitos de plazo y repetibilidad y escribe una recomendación de dos líneas.",
    extend="Explica con un ejemplo por qué un método rápido puede no ser el que conviene elegir.",
)

# ============================================================ OAE-07, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Planta Demo» de la empresa ficticia «Minera Demo» tiene un patio de recepción de mineral, una bodega de insumos, un patio de concentrado con capacidad máxima de 200 toneladas y un área de desechos. "
     "Inventario de concentrado de la semana (datos de ejemplo): saldo inicial, 120 toneladas; entradas por producción, 80 toneladas; despachos a la fundición, 150 toneladas. Una pila de la bodega tiene 40 sacos de insumo de 25 kilos cada uno. "
     "Peligros anotados: camiones que circulan por el patio sin señales, sacos apilados muy alto, envases de sustancias sin rotular junto a la salida y bidones de desechos mezclados con insumos.")
build(
    O7, 1, F,
    use="Aprenderé qué es controlar un inventario (saldo, entradas, salidas y pérdidas), qué se registra en la recepción y el despacho, qué peligros tiene una bodega o un patio y cómo se manejan los desechos con registro.",
    prior=["Sé sumar, restar y multiplicar números enteros.", "Sé qué es un registro.", "Sé la jerarquía de controles."],
    explain=[
        "Un inventario es la lista de lo que hay, con sus cantidades: mineral, insumos, productos finales y desechos. Se controla con registros: cada recepción es una entrada, y cada despacho es una salida. El saldo es lo que debería haber: saldo inicial más entradas menos salidas. Si un patio de ejemplo tenía 60 toneladas, recibió 40 y despachó 70, el saldo es 30 toneladas. Al contar lo que realmente hay se compara con el saldo, y la diferencia es la pérdida o un error de registro que se investiga.",
        "Los desechos también se inventarían: se registran qué son, cuánto hay y a quién se entregan, y los entrega personal autorizado a un destinatario autorizado con su guía, según la norma vigente. Nadie los elimina por cuenta propia. Los insumos y las sustancias se guardan rotulados, ordenados y separados según su hoja de datos de seguridad (HDS), y los apilamientos respetan alturas seguras. Un ejemplo de cálculo: 20 sacos de 30 kilos pesan 600 kilos.",
        f"Una bodega y un patio tienen peligros: tránsito de camiones, caída de cargas apiladas, sustancias sin rotular y desechos mezclados. Las medidas siguen la jerarquía de controles y las fiscalizan las autoridades minera, sanitaria y ambiental según la norma vigente. Este cuaderno no enseña a mover cargas ni a manejar sustancias. {EMER} {AVISO}",
    ],
    vocab=[("inventario", "lista de lo que hay, con sus cantidades"), ("entrada", "cantidad que se recibe y se suma al inventario"), ("salida", "cantidad que se despacha y se resta del inventario"), ("saldo", "cantidad que debería haber: saldo inicial más entradas menos salidas"), ("pérdida de inventario", "diferencia entre el saldo y lo que realmente se cuenta"), ("desecho", "material que ya no se usa y debe entregarse a un destinatario autorizado con registro"), ("recepción", "ingreso de mineral o insumos a la planta con su registro")],
    worked=[
        ("Calcular un saldo", "Un patio de ejemplo tenía 60 toneladas, recibió 40 y despachó 70. ¿Cuál es el saldo?", ["Se suma la entrada al saldo inicial: 60 más 40 son 100.", "Se resta la salida: 100 menos 70 son 30."], "30 toneladas"),
        ("Masa de una pila", "Una pila de ejemplo tiene 20 sacos de 30 kilos. ¿Cuántos kilos pesa?", ["Se multiplican los sacos por los kilos de cada uno.", "20 por 30 es 600."], "600 kilos"),
    ],
    mistakes=[("Creer que una diferencia pequeña entre el saldo y el conteo no necesita registro.", "Las diferencias pequeñas pueden repetirse y mostrar una fuga o un error sistemático.", "Toda diferencia se anota y se investiga."),
              ("Creer que un desecho puede botarse por cuenta propia si es poco.", "Los desechos se entregan a un destinatario autorizado con registro.", "Se registran y los entrega personal autorizado según la norma vigente.")],
    T=[
        ("abc", "En Metalurgia Extractiva: ¿qué es un inventario?", "La lista de lo que hay, con sus cantidades", "El plan de producción de la semana", "El informe de ley de un concentrado", "El inventario cuenta lo que hay; el plan y el informe son otros documentos."),
        ("abc", "En el control de inventario: ¿qué es el saldo?", "La cantidad que debería haber: saldo inicial más entradas menos salidas", "Solo lo que entró durante la semana", "Solo lo que salió durante la semana", "El saldo combina saldo inicial, entradas y salidas."),
        ("abc", "En el control de inventario: ¿qué es una pérdida de inventario?", "La diferencia entre el saldo y lo que realmente se cuenta", "Un mineral de baja ley", "El descuento que cobra un cliente", "La pérdida es una diferencia entre el registro y el conteo."),
        ("=", "{F} ¿Cuál es el saldo de concentrado al final de la semana, en toneladas?", "120+80-150", "Se suma la entrada al saldo inicial y se resta la salida.", " toneladas"),
        ("=", "{F} Con ese saldo, ¿cuántas toneladas más caben en el patio de concentrado?", "200-(120+80-150)", "Se resta el saldo a la capacidad máxima.", " toneladas"),
        ("=", "{F} ¿Cuántos kilos pesa la pila de sacos de la bodega?", "40*25", "Se multiplican los sacos por los kilos de cada uno.", " kg"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a los camiones que circulan sin señales?", "Que atropellen o choquen con una persona o un equipo", "Que baje el saldo de concentrado", "Que el patio quede lleno", "El riesgo es un daño a personas o equipos; el saldo o la capacidad son datos de inventario."),
        ("abc", "{F} Los sacos están apilados muy alto. ¿Qué medida de la jerarquía actúa mejor sobre el riesgo de caída?", "Rehacer las pilas con una altura segura, por personal autorizado y según la norma vigente", "Pedir al personal que pase rápido junto a las pilas", "Entregar cascos y dejar las pilas como están", "Corregir el apilamiento actúa sobre el peligro; pedir rapidez o usar casco son niveles inferiores."),
        ("abc", "{F} Hay envases sin rotular junto a la salida y bidones de desechos mezclados con insumos. ¿Qué corresponde?", "Informar al supervisor para que personal autorizado rotule y separe según la HDS y la norma vigente", "Abrir los envases para ver qué contienen", "Mover los bidones a un rincón sin avisar", "Sustancias y desechos sin rótulo se resuelven con personal autorizado y la HDS."),
        ("abc", "{F} Una estudiante dice: «ya sé inventariar, así que puedo mover los envases de sustancias de la bodega». ¿Qué respuesta es correcta?", "Es falso: mover sustancias exige instructor autorizado, HDS y norma vigente", "Es cierto, si usa guantes", "Es cierto, si los mueve de a uno", "Mover sustancias exige formación; los guantes o el número de envases no cambian el riesgo."),
        ("=", "{F} Si al contar el patio de concentrado se encuentran 45 toneladas, ¿cuántas toneladas de pérdida hay respecto del saldo?", "(120+80-150)-45", "Se resta lo contado al saldo.", " toneladas"),
        ("abc", "{F} El jefe dice que las diferencias pequeñas de inventario «no se registran». ¿Cuál es la mejor objeción?", "Toda diferencia se registra, porque las pequeñas pueden repetirse y mostrar una fuga", "Ninguna, porque lo pequeño no importa", "Que solo se registran las diferencias de los lunes", "Una diferencia pequeña repetida puede ser una pérdida real."),
        ("abc", "{F} Durante una visita de ejemplo, ves que un camión golpea a una persona en el patio. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a mover a la persona", "Pedirle al conductor que siga avanzando", "Acercarse sin formación puede causar otro accidente; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "Un conocido te pide que lo ayudes a deshacerte de unos bidones de «líquidos de la mina» tirándolos en una quebrada. ¿Qué respondes?", "Que no, porque los desechos se entregan a un destinatario autorizado con registro, y que lo consultarás con un adulto responsable", "Que sí, si es de noche", "Que sí, si son pocos bidones", "Botar desechos en el ambiente daña a personas y ecosistemas y es un incumplimiento."),
    sc=[
        ("En el control de inventario: ¿cómo se calcula el saldo?", "Sumando las entradas y restando las salidas al saldo inicial", "El saldo refleja lo que debería haber."),
        ("En la gestión de una planta: ¿qué se hace con los desechos?", "Se registran y los entrega personal autorizado a un destinatario autorizado", "Los desechos no se eliminan por cuenta propia."),
        ("En una bodega de planta: ¿cómo se guardan las sustancias?", "Rotuladas, ordenadas y separadas según su HDS", "La HDS indica cómo guardar cada sustancia."),
    ],
    op=("Ficha de ejemplo: el patio de mineral de la «Planta Cordón Demo» tiene capacidad máxima de 600 toneladas. Saldo inicial, 300 toneladas; recepciones, 200 toneladas; salidas a molienda, 350 toneladas. En la bodega hay una pila de 30 sacos de 15 kilos y un envase de sustancia sin rótulo. Escribe (a) el saldo del patio, (b) cuántas toneladas más caben, (c) cuántos kilos pesa la pila, (d) un peligro del envase sin rótulo y su riesgo, (e) qué debe hacer una persona que ve que un camión golpea a alguien en el patio.",
        "(a) 300 + 200 − 350 = 150 toneladas. (b) 600 − 150 = 450 toneladas. (c) 30 × 15 = 450 kg. (d) Peligro: una sustancia sin rótulo cuyo contenido se desconoce; riesgo: que alguien la maneje sin conocer sus peligros y se dañe. (e) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien el saldo", "calcula bien la capacidad restante", "calcula bien los kilos", "distingue peligro y riesgo", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["restar la entrada en vez de sumarla", "olvidar restar el saldo a la capacidad", "responder que se acerca a mover a la persona"],
        "Pregunta: «¿qué se suma y qué se resta al saldo inicial?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un saldo inicial, una entrada y una salida de un material de planta y calcula el saldo; luego inventa un conteo y calcula la pérdida.",
    extend="Explica con un ejemplo por qué el desecho también forma parte del inventario.",
)

# ============================================================ OAE-07, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Planta Demo». Documentos: la guía de recepción (anota qué entra, quién lo entrega y cuánto), la guía de despacho (anota qué sale, a quién y cuánto), el ticket de pesaje (peso bruto del camión cargado, tara del camión vacío y peso neto), "
     "la planilla de inventario y el registro de desechos (qué desecho, cuánto y a quién se entregó). Tres camiones de concentrado (datos de ejemplo): camión 1, peso bruto 38 toneladas y tara 14; camión 2, bruto 41 y tara 15; camión 3, bruto 36 y tara 14. "
     "La guía de despacho del día anota 74 toneladas en total. Se acepta una diferencia máxima de 1 tonelada entre la suma de los tickets y la guía (criterio de ejemplo). Roles: encargado de bodega, encargado de despacho, supervisor y encargado ambiental.")
build(
    O7, 2, F,
    use="Aprenderé los documentos del control de inventario (guías de recepción y despacho, ticket de pesaje, planilla y registro de desechos), los roles y cómo se calcula el peso neto y se comparan los documentos.",
    prior=["Sé qué son saldo, entrada y salida.", "Sé leer un registro escrito.", "Sé restar y sumar números enteros."],
    explain=[
        "El control de inventario se apoya en documentos que deben coincidir. La guía de recepción anota lo que entra: qué es, quién lo entrega y cuánto. La guía de despacho anota lo que sale: qué es, a quién y cuánto. El ticket de pesaje registra el peso bruto, que es el de un camión cargado, la tara, que es el de ese camión vacío, y el peso neto, que es la carga: peso bruto menos tara. La planilla de inventario resume entradas, salidas y saldo. El registro de desechos anota qué desecho, cuánto y a quién se entregó.",
        "Comparar documentos es parte del control: la suma de los pesos netos de los tickets debe coincidir con la guía de despacho dentro de lo aceptado. Por ejemplo, un camión de 30 toneladas brutas con tara de 12 lleva 18 toneladas netas, y otro de 28 con tara de 11 lleva 17; si los tickets suman 35 y la guía dice 35, coinciden. Si no coinciden, se informa y se busca la causa; los documentos no se alteran para que cuadren.",
        f"Roles: el encargado de bodega controla recepciones y saldos, el encargado de despacho prepara las guías, el supervisor revisa y decide, y el encargado ambiental vigila el registro y la entrega de desechos. Cada firma certifica que quien firma comprobó lo que declara. {EMER} {AVISO}",
    ],
    vocab=[("guía de recepción", "documento que anota qué entra, quién lo entrega y cuánto"), ("guía de despacho", "documento que anota qué sale, a quién y cuánto"), ("ticket de pesaje", "registro del peso bruto, la tara y el peso neto de un camión"), ("peso bruto", "peso de un camión cargado"), ("tara", "peso de un camión vacío"), ("peso neto", "peso de la carga: peso bruto menos tara"), ("registro de desechos", "anotación de qué desecho, cuánto y a quién se entregó")],
    worked=[
        ("Peso neto", "Un camión de ejemplo pesa 30 toneladas cargado y 12 vacío. ¿Cuánto pesa la carga?", ["El peso neto es el bruto menos la tara.", "30 menos 12 son 18."], "18 toneladas"),
        ("Comparar documentos", "Dos tickets de ejemplo suman 35 toneladas netas y la guía de despacho dice 35. El máximo aceptado es 1 tonelada de diferencia. ¿Coinciden?", ["La diferencia es 35 menos 35, es decir 0.", "0 no supera el máximo de 1."], "Sí, coinciden"),
    ],
    mistakes=[("Usar el peso bruto como si fuera el peso de la carga.", "El peso bruto incluye el camión; la carga es el peso neto.", "Se resta la tara al peso bruto."),
              ("Cambiar la guía de despacho para que coincida con los tickets.", "Un documento alterado oculta un error real de pesaje o de registro.", "Se informa la diferencia y se busca la causa.")],
    T=[
        ("abc", "En el control de inventario: ¿qué es la tara de un camión?", "El peso del camión vacío", "El peso del camión cargado", "El peso de la carga solamente", "La tara es el peso del vehículo sin carga."),
        ("abc", "En el control de inventario: ¿qué es el peso neto?", "El peso de la carga, igual al bruto menos la tara", "El peso del camión cargado", "La suma del bruto y la tara", "El neto es la carga; el bruto incluye el camión."),
        ("abc", "En el control de inventario: ¿qué anota la guía de despacho?", "Qué sale de la planta, a quién y cuánto", "Qué entra a la planta y quién lo entrega", "Cuántas muestras tomó el laboratorio", "La guía de despacho registra salidas; las entradas van en la guía de recepción."),
        ("=", "{F} ¿Cuántas toneladas netas lleva el camión 1?", "38-14", "Se resta la tara al peso bruto.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas netas lleva el camión 2?", "41-15", "Se resta la tara al peso bruto.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas netas suman los tres camiones?", "(38-14)+(41-15)+(36-14)", "Se calcula el neto de cada camión y se suman.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas de diferencia hay entre la guía de despacho y la suma de los tickets?", "74-((38-14)+(41-15)+(36-14))", "Se resta la suma de los netos a lo que anota la guía.", " toneladas"),
        ("abc", "{F} ¿Coinciden los documentos dentro del máximo aceptado?", "No, porque la diferencia de 2 toneladas supera el máximo de 1", "Sí, porque la diferencia es pequeña", "Sí, porque la guía anota más toneladas que los tickets", "El máximo aceptado es 1 tonelada y la diferencia es 2."),
        ("abc", "{F} ¿Qué corresponde hacer ante esa diferencia?", "Informar al supervisor y buscar la causa, sin cambiar la guía ni los tickets", "Cambiar la guía a 72 toneladas para que coincida", "Cambiar el ticket del camión 3 para sumar 74", "Un documento alterado oculta el error; se informa y se busca la causa."),
        ("abc", "{F} ¿Quién controla las recepciones y los saldos de la bodega?", "El encargado de bodega", "El encargado ambiental", "El encargado de despacho", "Recepciones y saldos son de bodega; ambiental vigila los desechos."),
        ("=", "{F} Si el camión 3 hubiera llevado 2 toneladas más de carga, ¿cuántas toneladas netas habrían sumado los tres camiones?", "(38-14)+(41-15)+(36-14)+2", "Se suma la carga adicional a la suma de los netos.", " toneladas"),
        ("abc", "{F} Un compañero propone anotar en la guía las toneladas de los tickets y dejar sin registrar la diferencia. ¿Cuál es la mejor respuesta?", "No se hace: se registra la diferencia observada, se informa y se busca su causa", "Se puede, si la diferencia es solo de 2 toneladas", "Se puede, si se corrige en el próximo despacho", "Una diferencia sin registro no se puede investigar ni corregir."),
        ("abc", "{F} Los desechos del día se entregaron a una empresa autorizada. ¿Dónde debe quedar constancia?", "En el registro de desechos, con qué desecho, cuánto y a quién se entregó", "En el ticket de pesaje del camión de concentrado", "En la guía de recepción de mineral", "El registro de desechos es el documento que sigue a los desechos."),
    ],
    ctx=("abc", "Un compañero de práctica te pide firmar una guía de despacho sin haber visto los tickets, «porque son de confianza». ¿Qué respondes?", "Que no, porque firmar sin comprobar es un registro falso, y que lo consultarás con un adulto responsable", "Que sí, porque siempre coinciden", "Que sí, si firma él primero", "La firma certifica una comprobación; firmar sin revisar engaña a quien lee el documento."),
    sc=[
        ("En el control de inventario: ¿cómo se calcula el peso neto?", "Restando la tara al peso bruto", "El neto es la carga sin el peso del camión."),
        ("En el control de inventario: ¿qué se hace si los documentos no coinciden?", "Se informa y se busca la causa, sin alterarlos", "Alterar documentos oculta el error y quita la base para corregirlo."),
        ("En el control de inventario: ¿qué anota la guía de recepción?", "Qué entra, quién lo entrega y cuánto", "La guía de recepción registra las entradas."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo». Camión A: peso bruto 40 toneladas y tara 16. Camión B: peso bruto 34 toneladas y tara 13. La guía de despacho anota 45 toneladas en total. Se acepta una diferencia máxima de 1 tonelada. Escribe (a) el peso neto de cada camión, (b) la suma, (c) la diferencia con la guía y si es aceptable, (d) qué haces si no lo es, (e) qué documento registra a quién se entregó un desecho.",
        "(a) Camión A: 40 − 16 = 24 toneladas; camión B: 34 − 13 = 21 toneladas. (b) 24 + 21 = 45 toneladas. (c) La guía anota 45: la diferencia es 0 y es aceptable. (d) Si no lo fuera, informar al supervisor y buscar la causa, sin alterar los documentos. (e) El registro de desechos.",
        ["calcula bien los pesos netos", "suma bien", "concluye que coinciden", "informa sin alterar", "nombra el registro de desechos"],
        ["hoja con las cinco respuestas"],
        ["usar el peso bruto como carga", "restar la tara en el orden contrario", "alterar la guía"],
        "Pregunta: «¿qué se resta al peso bruto para obtener la carga?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres camiones con peso bruto y tara y calcula el peso neto de cada uno y la suma.",
    extend="Explica con un ejemplo por qué comparar dos documentos ayuda a detectar errores.",
)

# ============================================================ OAE-07, clase 3
F = ("Ficha 3 (planilla de ejemplo, inventada). Inventario mensual de mineral en el patio de la «Planta Demo», en toneladas húmedas. Saldo inicial: 800. Recepciones: semana 1, 300; semana 2, 250; semana 3, 350; semana 4, 300. "
     "Salidas a molienda en el mes: 1.050. Saldo contado al fin del mes por el encargado (conteo de ejemplo): 940. Humedad de ejemplo del mineral: 10 % (porcentaje de agua del mineral húmedo). "
     "Criterio de ejemplo: una diferencia de hasta 2 % del saldo esperado es aceptable.")
build(
    O7, 3, F,
    use="Aprenderé a analizar una planilla mensual de inventario: calcular el saldo esperado, comparar con el conteo, decidir si la diferencia es aceptable y pasar toneladas húmedas a secas.",
    prior=["Sé calcular un saldo con entradas y salidas.", "Sé calcular un porcentaje con números enteros.", "Sé comparar un dato con un criterio."],
    explain=[
        "Al cerrar el mes, la planilla de inventario calcula el saldo esperado: saldo inicial más todas las entradas menos todas las salidas. El encargado cuenta lo que realmente hay y se compara: la diferencia entre el saldo esperado y lo contado es la pérdida (o un error de registro). Se compara con el máximo aceptado, que a veces se fija como porcentaje del saldo esperado. Si supera el máximo, se informa, se busca la causa y no se cambia ninguna cifra.",
        "El mineral contiene agua. La humedad es el porcentaje de agua del mineral húmedo. Las toneladas secas se calculan restando el agua: toneladas húmedas por (100 menos la humedad) dividido por 100. Con 400 toneladas húmedas y 5 % de humedad, hay 380 toneladas secas. Los balances metalúrgicos suelen hacerse en toneladas secas, porque el agua no aporta metal.",
        f"Una pérdida de inventario puede deberse a un error de pesaje, un registro incompleto o un derrame no anotado, y cada causa se investiga. Estas cifras son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("saldo esperado", "saldo inicial más entradas menos salidas"), ("conteo físico", "medición de lo que realmente hay"), ("diferencia de inventario", "saldo esperado menos lo contado"), ("humedad", "porcentaje de agua del mineral húmedo"), ("toneladas secas", "toneladas húmedas menos el agua que contienen")],
    worked=[
        ("Saldo esperado y diferencia", "Un patio de ejemplo tenía 200 toneladas, recibió 150 y despachó 180; el conteo da 165. ¿Cuál es la diferencia?", ["El saldo esperado es 200 más 150 menos 180, es decir 170.", "170 menos 165 son 5 toneladas."], "5 toneladas"),
        ("Toneladas secas", "Un lote de ejemplo de 400 toneladas húmedas tiene 5 % de humedad. ¿Cuántas toneladas secas tiene?", ["Se multiplica por 95 y se divide por 100.", "400 por 95 dividido por 100 es 380."], "380 toneladas"),
    ],
    mistakes=[("Hacer el balance metalúrgico con toneladas húmedas como si fueran secas.", "El agua no contiene metal y la ley se calcula sobre el material seco.", "Se pasan las toneladas húmedas a secas con la humedad."),
              ("Ajustar el conteo para que coincida con el saldo esperado.", "Se oculta una pérdida o un error real.", "Se anota el conteo real, se informa la diferencia y se investiga.")],
    T=[
        ("abc", "En el control de inventario: ¿qué es el saldo esperado?", "El saldo inicial más las entradas menos las salidas", "Lo que se cuenta físicamente en el patio", "El promedio de las recepciones", "El saldo esperado sale de los registros; lo contado es otra medición."),
        ("abc", "En el control de inventario: ¿qué es el conteo físico?", "La medición de lo que realmente hay", "El cálculo del saldo con los documentos", "El registro de las guías de despacho", "El conteo físico mide lo real para compararlo con el registro."),
        ("abc", "En el mineral de una planta: ¿qué es la humedad?", "El porcentaje de agua que contiene el mineral húmedo", "El porcentaje de metal que contiene el mineral", "La temperatura del mineral al llegar", "La humedad es agua; el porcentaje de metal es la ley."),
        ("=", "{F} ¿Cuántas toneladas se recibieron en el mes?", "300+250+350+300", "Se suman las recepciones de las cuatro semanas.", " toneladas"),
        ("=", "{F} ¿Cuál es el saldo esperado al fin del mes, en toneladas húmedas?", "800+300+250+350+300-1050", "Se suman las entradas al saldo inicial y se resta la salida.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas de diferencia hay entre el saldo esperado y el conteo?", "(800+300+250+350+300-1050)-940", "Se resta lo contado al saldo esperado.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas es el máximo de diferencia aceptable (2 % del saldo esperado)?", "(800+300+250+350+300-1050)*2//100", "Se calcula el 2 % del saldo esperado.", " toneladas"),
        ("abc", "{F} ¿Es aceptable la diferencia del mes?", "Sí, porque la diferencia en toneladas no supera el máximo aceptable", "No, porque existe una diferencia", "No, porque la diferencia es mayor que 2", "Se compara la diferencia con el máximo en toneladas, no con el porcentaje."),
        ("=", "{F} ¿Cuántas toneladas secas tiene el saldo esperado, con 10 % de humedad?", "950*90//100", "Se multiplica por 90 y se divide por 100.", " toneladas"),
        ("=", "{F} ¿Cuántas toneladas de agua contiene el saldo esperado?", "950*10//100", "Se aplica el porcentaje de humedad a las toneladas húmedas.", " toneladas"),
        ("abc", "{F} ¿Por qué los balances metalúrgicos suelen hacerse en toneladas secas?", "Porque el agua no contiene metal y la ley se calcula sobre el material seco", "Porque el mineral seco es más barato", "Porque las toneladas secas siempre son más que las húmedas", "El agua no aporta metal; contarla distorsiona la ley y los balances."),
        ("=", "{F} Si el conteo hubiera sido 920 toneladas, ¿cuántas toneladas de diferencia habría?", "(800+300+250+350+300-1050)-920", "Se resta el nuevo conteo al saldo esperado.", " toneladas"),
        ("abc", "{F} Con esa diferencia de 30 toneladas y un máximo de 19, ¿qué corresponde?", "Informar al supervisor y buscar la causa, sin cambiar ninguna cifra", "Cambiar el conteo a 931 para que sea aceptable", "Aceptarla, porque 30 es poco frente a 950", "Una diferencia mayor que el máximo se investiga; ajustar cifras la oculta."),
    ],
    ctx=("abc", "Un compañero propone anotar 950 en el conteo, aunque se contaron 940, «para cerrar el mes sin problemas». ¿Qué respondes?", "Que no, porque se anota el conteo real, y que lo consultarás con un adulto responsable", "Que sí, porque son solo 10 toneladas", "Que sí, si lo corrige el mes siguiente", "Un conteo alterado oculta una pérdida real y quita la base para investigarla."),
    sc=[
        ("En el control de inventario: ¿cómo se calcula la diferencia de inventario?", "Restando lo contado al saldo esperado", "La diferencia compara el registro con la realidad."),
        ("En el mineral de una planta: ¿cómo se calculan las toneladas secas?", "Multiplicando las húmedas por (100 menos la humedad) y dividiendo por 100", "Las toneladas secas excluyen el agua."),
        ("En un cierre de inventario con diferencia mayor al máximo: ¿qué se hace?", "Se informa y se busca la causa, sin cambiar cifras", "Una diferencia grande se investiga y se informa antes de cerrar."),
    ],
    op=("Ficha de ejemplo: patio de mineral de la «Planta Cordón Demo» (toneladas húmedas). Saldo inicial, 500; recepciones del mes, 200, 300 y 250; salidas del mes, 900; conteo de fin de mes, 340; humedad de ejemplo, 8 %; diferencia máxima aceptable de ejemplo, 2 % del saldo esperado. Escribe (a) el saldo esperado, (b) la diferencia con el conteo, (c) el máximo aceptable y si se cumple, (d) las toneladas secas del saldo esperado, (e) qué haces ante el resultado.",
        "(a) 500 + 200 + 300 + 250 − 900 = 350 toneladas. (b) 350 − 340 = 10 toneladas. (c) 2 % de 350 es 7 toneladas; 10 supera 7, así que no se cumple. (d) 350 × 92 ÷ 100 = 322 toneladas secas. (e) Informar al supervisor y buscar la causa (pesaje, registro o derrame), sin cambiar ninguna cifra.",
        ["calcula bien el saldo esperado", "calcula bien la diferencia", "concluye que no se cumple el máximo", "calcula bien las toneladas secas", "informa sin alterar"],
        ["hoja con las cinco respuestas"],
        ["olvidar alguna recepción", "comparar toneladas con el porcentaje", "ajustar el conteo"],
        "Pregunta: «¿cuántas toneladas es el 2 % del saldo esperado?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un inventario mensual con saldo inicial, entradas, salidas y conteo, y calcula el saldo esperado y la diferencia.",
    extend="Explica con un ejemplo por qué una diferencia de inventario puede deberse a un error de registro y no a una pérdida real.",
)

# ============================================================ OAE-07, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Insumo ficticio «I-3» de la «Planta Demo» (datos de ejemplo): saldo en bodega, 900 kilos; consumo registrado, 30 kilos por día; plazo de reposición (días entre hacer un pedido y recibirlo), 12 días; costo de ejemplo, $2.000 por kilo. "
     "Regla de ejemplo: se hace un nuevo pedido cuando el saldo baja a la cantidad que se consumirá durante el plazo de reposición (punto de pedido). Desechos del mes: 1.200 kilos registrados y 1.000 kilos entregados a una empresa autorizada con su guía.")
build(
    O7, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo al inventario: calcular cobertura y punto de pedido de un insumo, el valor del inventario y los desechos pendientes de entrega.",
    prior=["Sé calcular saldos y diferencias de inventario.", "Sé multiplicar y dividir números enteros.", "Sé leer un consumo registrado."],
    explain=[
        "Para que no falte un insumo se calcula la cobertura, que son los días que alcanza el saldo al consumo actual: saldo dividido por consumo diario. Entre hacer un pedido y recibirlo pasa el plazo de reposición, y durante ese plazo la planta sigue consumiendo. Por eso el pedido se hace cuando el saldo llega al punto de pedido, que es el consumo diario multiplicado por el plazo de reposición. Con un saldo de 500 kilos, un consumo de 20 kilos por día y un plazo de 10 días, la cobertura es 25 días y el punto de pedido es 200 kilos.",
        "El valor del inventario se calcula multiplicando los kilos por el costo de cada kilo. Los desechos registrados que aún no se entregan siguen en la planta y se guardan según su rótulo y su HDS hasta que personal autorizado los entregue con guía a un destinatario autorizado; los kilos pendientes son los registrados menos los entregados. El consumo registrado es una cifra de lo ocurrido, no una instrucción de cuánto usar: eso lo fija el procedimiento aprobado.",
        f"Estos valores son de ejemplo; los reales los registran personas autorizadas y cambian con la planta y el proveedor. Nunca se cambia una cifra del registro para que el inventario parezca mejor. {EMER} {AVISO}",
    ],
    vocab=[("cobertura", "días que alcanza el saldo al consumo actual"), ("plazo de reposición", "días entre hacer un pedido y recibirlo"), ("punto de pedido", "saldo al que se hace un nuevo pedido, igual al consumo diario por el plazo de reposición"), ("valor del inventario", "kilos del saldo multiplicados por el costo de cada kilo"), ("desechos pendientes", "desechos registrados que aún no se entregan a un destinatario autorizado")],
    worked=[
        ("Cobertura y punto de pedido", "Un insumo de ejemplo tiene saldo de 500 kilos, consumo de 20 kilos por día y plazo de reposición de 10 días. ¿Cuál es la cobertura y el punto de pedido?", ["Cobertura: 500 dividido por 20 es 25 días.", "Punto de pedido: 20 por 10 es 200 kilos."], "25 días; 200 kilos"),
        ("Valor del inventario", "Un saldo de ejemplo de 300 kilos cuesta $1.000 por kilo. ¿Cuál es el valor del inventario?", ["Se multiplican los kilos por el costo de cada uno.", "300 por 1.000 es 300.000."], "$300.000"),
    ],
    mistakes=[("Hacer el pedido cuando el saldo llega a cero.", "Durante el plazo de reposición se sigue consumiendo, y el insumo faltaría antes de que llegue.", "El pedido se hace al llegar al punto de pedido."),
              ("Creer que los desechos pendientes pueden eliminarse por cuenta propia si son pocos.", "Los desechos se entregan a un destinatario autorizado con registro.", "Se guardan según su rótulo y personal autorizado los entrega.")],
    T=[
        ("abc", "En el control de un insumo: ¿qué es la cobertura?", "Los días que alcanza el saldo al consumo actual", "La cantidad que se pide cada vez", "El costo total del insumo", "La cobertura relaciona saldo y consumo diario."),
        ("abc", "En el control de un insumo: ¿qué es el punto de pedido?", "El saldo al que se hace un nuevo pedido, igual al consumo durante el plazo de reposición", "El saldo inicial del mes", "El precio por kilo del insumo", "El punto de pedido anticipa lo que se consumirá mientras llega el pedido."),
        ("abc", "En el control de un insumo: ¿qué es el plazo de reposición?", "Los días entre hacer un pedido y recibirlo", "Los días que dura el insumo antes de vencer", "Los días que el proveedor cobra el envío", "El plazo cuenta el tiempo de espera del pedido."),
        ("=", "{F} ¿Cuántos días de cobertura tiene el saldo?", "900//30", "Se divide el saldo entre el consumo diario.", " días"),
        ("=", "{F} ¿Cuál es el punto de pedido, en kilos?", "30*12", "Se multiplica el consumo diario por el plazo de reposición.", " kg"),
        ("=", "{F} ¿Cuál es el valor del saldo, en pesos?", "900*2000", "Se multiplican los kilos por el costo de cada kilo.", " pesos"),
        ("=", "{F} ¿Cuántos kilos se pueden consumir antes de llegar al punto de pedido?", "900-30*12", "Se resta el punto de pedido al saldo.", " kg"),
        ("=", "{F} ¿Cuántos días faltan para llegar al punto de pedido?", "(900-30*12)//30", "Se divide lo que se puede consumir entre el consumo diario.", " días"),
        ("abc", "{F} ¿Por qué se hace el pedido antes de que el saldo llegue a cero?", "Porque durante el plazo de reposición se sigue consumiendo", "Porque pedir tarde sale más caro", "Porque el saldo nunca llega a cero", "Si el pedido se espera hasta el cero, el insumo faltaría mientras llega."),
        ("=", "{F} ¿Cuántos kilos de desechos están registrados y pendientes de entrega?", "1200-1000", "Se restan los kilos entregados a los registrados.", " kg"),
        ("abc", "{F} ¿Qué corresponde con los desechos pendientes?", "Guardarlos según su rótulo y su HDS hasta que personal autorizado los entregue con guía a un destinatario autorizado", "Botarlos en un lugar apartado de la planta", "Mezclarlos con insumos para ahorrar espacio", "Los desechos se entregan con registro; botarlos o mezclarlos es un incumplimiento y un riesgo."),
        ("=", "{F} Si el consumo subiera a 45 kilos por día, ¿cuál sería el nuevo punto de pedido, en kilos?", "45*12", "Se multiplica el nuevo consumo por el plazo de reposición.", " kg"),
        ("abc", "{F} Con ese nuevo consumo y el saldo de 900 kilos, ¿qué conclusión es correcta?", "Todavía no corresponde pedir, porque 900 es mayor que el punto de pedido de 540", "Corresponde pedir ya, porque el consumo subió", "Corresponde pedir ya, porque 900 es igual a 30 por 30", "Se pide cuando el saldo baja al punto de pedido; 900 aún lo supera."),
    ],
    ctx=("abc", "Un compañero propone botar los 200 kilos de desechos pendientes en una quebrada porque «la entrega es cara». ¿Qué respondes?", "Que no, porque los desechos se entregan a un destinatario autorizado con registro, y que lo consultarás con un adulto responsable", "Que sí, si lo hacen de noche", "Que sí, si son solo 200 kilos", "Botar desechos daña el ambiente y es un incumplimiento, aunque la entrega cueste."),
    sc=[
        ("En el control de un insumo: ¿cómo se calcula el punto de pedido?", "Multiplicando el consumo diario por el plazo de reposición", "El punto de pedido cubre el consumo mientras llega el pedido."),
        ("En el control de un insumo: ¿cómo se calcula la cobertura?", "Dividiendo el saldo entre el consumo diario", "La cobertura mide cuántos días alcanza el saldo."),
        ("En el control de desechos: ¿cómo se calculan los kilos pendientes?", "Restando los kilos entregados a los registrados", "Lo que no se entregó sigue en la planta."),
    ],
    op=("Ficha de ejemplo: insumo ficticio «I-4» de la «Planta Cordón Demo». Saldo, 700 kilos; consumo registrado, 25 kilos por día; plazo de reposición, 6 días; costo de ejemplo, $1.500 por kilo. Desechos del mes: 900 kilos registrados y 600 kilos entregados con guía. Escribe (a) la cobertura, (b) el punto de pedido, (c) el valor del saldo, (d) cuántos días faltan para llegar al punto de pedido, (e) los kilos de desechos pendientes y qué se hace con ellos.",
        "(a) 700 ÷ 25 = 28 días. (b) 25 × 6 = 150 kg. (c) 700 × 1.500 = 1.050.000 pesos. (d) (700 − 150) ÷ 25 = 22 días. (e) 900 − 600 = 300 kg; se guardan según su rótulo y su HDS hasta que personal autorizado los entregue con guía a un destinatario autorizado.",
        ["calcula bien la cobertura", "calcula bien el punto de pedido", "calcula bien el valor", "calcula bien los días", "calcula los desechos y no los elimina por cuenta propia"],
        ["hoja con las cinco respuestas"],
        ["pedir cuando el saldo es cero", "dividir al revés", "botar los desechos pendientes"],
        "Pregunta: «¿cuánto se consume mientras llega el pedido?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un insumo con saldo, consumo y plazo de reposición y calcula su cobertura y su punto de pedido.",
    extend="Explica con un ejemplo por qué un consumo mayor hace subir el punto de pedido.",
)

# ============================================================ OAE-08, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Planta Demo» de la empresa ficticia «Minera Demo» tiene 40 personas en el turno. Hechos de la semana (datos de ejemplo): 36 personas asistieron a la charla de seguridad; el supervisor anotó que 2 cintas no tenían resguardo; "
     "la empresa tenía pendiente comprar los resguardos; una trabajadora avisó de un derrame que llegaba a una canaleta; un trabajador, a quien se le había entregado su casco, no lo usó; el comité de seguridad del turno revisó los registros; y la autoridad minera fiscaliza según la norma vigente. "
     "Cada persona trabaja 8 horas al día, 5 días a la semana.")
build(
    O8, 1, F,
    use="Aprenderé qué es el marco legal del trabajo minero, qué autoridades fiscalizan y cómo se reparten las responsabilidades individuales, colectivas y empresariales en seguridad, prevención de riesgos y cuidado del ambiente.",
    prior=["Sé que existen normas de seguridad.", "Sé calcular un porcentaje con números enteros.", "Sé la jerarquía de controles."],
    explain=[
        "El marco legal del trabajo minero es el conjunto de leyes y reglamentos, la norma vigente, que regula la seguridad, la prevención de riesgos y el cuidado del medio ambiente en las plantas de procesamiento. Su aplicación la fiscalizan autoridades: la autoridad minera para la seguridad de la actividad minera, la autoridad sanitaria para condiciones de higiene y salud, y la autoridad ambiental para los permisos y el cuidado del ambiente. Las relaciones de trabajo se rigen además por el Código del Trabajo y la norma vigente.",
        "Las responsabilidades se reparten en tres niveles. La responsabilidad individual es la de cada persona: seguir los procedimientos, usar el equipo de protección que se le entregó, avisar los peligros y no alterar los registros. La responsabilidad colectiva es la del equipo en conjunto: participar en charlas y simulacros, cuidarse entre compañeros y trabajar con el comité de seguridad, que revisa condiciones y registros. La responsabilidad empresarial es la de la empresa: capacitar, entregar equipos de protección, mantener las máquinas y sus protecciones, informar los riesgos de cada tarea y cumplir los permisos ambientales. Un ejemplo de cálculo: si 15 de 20 personas asisten a una charla, asiste el 75 %.",
        f"Cumplir los tres niveles a la vez es lo que previene los accidentes: ninguno reemplaza a los otros. Este cuaderno no entrega asesoría legal; ante dudas se consulta a un adulto responsable o a la autoridad competente. {EMER} {AVISO}",
    ],
    vocab=[("marco legal", "conjunto de leyes y reglamentos que regulan el trabajo, la seguridad y el ambiente"), ("autoridad minera", "institución que fiscaliza la seguridad de la actividad minera según la norma vigente"), ("autoridad sanitaria", "institución que fiscaliza condiciones de higiene y salud"), ("responsabilidad individual", "lo que debe cumplir cada persona"), ("responsabilidad colectiva", "lo que cumple el equipo en conjunto"), ("responsabilidad empresarial", "lo que debe cumplir la empresa"), ("comité de seguridad", "grupo que revisa las condiciones de seguridad y los registros del trabajo")],
    worked=[
        ("Porcentaje de asistencia", "A una charla de ejemplo asisten 15 de 20 personas. ¿Qué porcentaje asiste?", ["Se divide 15 entre 20 y se multiplica por 100.", "El resultado es 75 por ciento."], "75 %"),
        ("Clasificar una responsabilidad", "En una planta de ejemplo, una persona avisa de una fuga y la empresa debe reparar el equipo. ¿Qué nivel corresponde a cada acción?", ["Avisar el peligro lo hace una persona.", "Reparar el equipo es una tarea de la empresa."], "Avisar: individual; reparar: empresarial"),
    ],
    mistakes=[("Creer que si la empresa entrega el equipo de protección, la seguridad es solo de la empresa.", "Cada persona debe además usarlo y seguir los procedimientos.", "Los tres niveles se cumplen a la vez."),
              ("Creer que leer sobre el marco legal permite dar asesoría legal.", "Interpretar casos legales exige profesionales y la norma vigente.", "Aprende aquí los conceptos y consulta a un adulto responsable o a la autoridad competente.")],
    T=[
        ("abc", "En el trabajo minero: ¿qué es la responsabilidad individual en seguridad?", "Lo que debe cumplir cada persona, como seguir procedimientos, usar su protección y avisar peligros", "Lo que la empresa debe cumplir para todo el personal", "Lo que fiscaliza la autoridad minera", "La responsabilidad individual es la de cada persona; la de la empresa y la fiscalización son otros niveles."),
        ("abc", "En el trabajo minero: ¿qué es la responsabilidad colectiva?", "Lo que cumple el equipo en conjunto, como participar en simulacros y cuidarse entre compañeros", "Lo que decide un solo supervisor", "Lo que paga la empresa por los equipos", "La responsabilidad colectiva es la del equipo; no depende de una sola persona."),
        ("abc", "En el trabajo minero: ¿qué es la responsabilidad empresarial?", "Lo que debe cumplir la empresa, como capacitar, entregar protección y mantener las máquinas y sus resguardos", "Lo que debe cumplir cada trabajador en su puesto", "La inspección que hace la autoridad minera", "La empresa tiene deberes propios de capacitación, equipos y mantención."),
        ("=", "{F} ¿Qué porcentaje del turno asistió a la charla de seguridad?", "36*100//40", "Se divide los asistentes entre el total de personas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas personas del turno no asistieron a la charla?", "40-36", "Se resta los asistentes al total de personas.", " personas"),
        ("abc", "{F} Comprar los resguardos pendientes de las cintas es una responsabilidad:", "Empresarial, porque la empresa debe mantener las máquinas con sus protecciones", "Individual, porque cada trabajador debe comprarlos", "De la autoridad minera, que compra los resguardos", "La empresa es responsable de los equipos y sus protecciones."),
        ("abc", "{F} Que una trabajadora avise del derrame que llega a la canaleta es cumplir una responsabilidad:", "Individual, porque avisar un peligro es un deber de cada persona", "Empresarial, porque la empresa debe avisar a cada persona", "De la autoridad sanitaria, que debe limpiar el derrame", "Avisar un peligro es un deber de cada persona."),
        ("abc", "{F} Un trabajador, a quien se le entregó su casco, no lo usó. ¿Qué responsabilidad incumplió?", "La individual, porque debía usar la protección que se le entregó", "La de la autoridad minera, que debía obligarlo", "Solo la empresarial, porque no lo vigiló", "Usar la protección entregada es un deber de cada persona."),
        ("=", "{F} ¿Cuántas horas trabaja cada persona en una semana?", "8*5", "Se multiplican las horas por día por los días de la semana.", " horas"),
        ("abc", "{F} ¿Qué hace la autoridad minera según la ficha?", "Fiscaliza el cumplimiento de la norma vigente de seguridad", "Compra los resguardos que faltan", "Dirige la charla de seguridad del turno", "La autoridad minera fiscaliza; la empresa compra los resguardos y capacita."),
        ("abc", "{F} El supervisor dice que, como la empresa entrega los equipos de protección, la seguridad es solo responsabilidad de la empresa. ¿Cuál es la mejor objeción?", "La seguridad se cumple a la vez en los tres niveles: individual, colectivo y empresarial", "Ninguna, porque la empresa lo decide todo", "Que solo importa lo que cumple cada trabajador", "Ningún nivel reemplaza a los otros."),
        ("=", "{F} Si se programa una charla de recuperación de 2 horas para quienes faltaron, ¿cuántas horas-persona suma?", "(40-36)*2", "Se multiplican las personas que faltaron por las horas de la charla.", " horas-persona"),
        ("abc", "{F} Durante una visita de ejemplo, ves que el derrame llega a una canaleta y una persona resbala y cae junto a él. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a levantar a la persona y limpiar el derrame", "Esperar a que la persona se levante sola", "Acercarse a un derrame sin formación puede causar otro accidente."),
    ],
    ctx=("abc", "Un compañero te pide que firmes la asistencia a una charla de seguridad a la que no fuiste, «para no tener problemas». ¿Qué respondes?", "Que no, porque firmar una asistencia falsa es alterar un registro, y que lo consultarás con un adulto responsable", "Que sí, porque la charla no es importante", "Que sí, si es solo esa vez", "Una firma certifica una asistencia real; firmar sin asistir engaña a quienes confían en el registro."),
    sc=[
        ("En el trabajo minero: ¿qué es el marco legal?", "El conjunto de leyes y reglamentos que regulan el trabajo, la seguridad y el ambiente", "El marco legal es la norma vigente."),
        ("En una planta minera: ¿qué hace el comité de seguridad?", "Revisa las condiciones de seguridad y los registros del trabajo", "El comité apoya la seguridad del equipo."),
        ("En una planta minera: ¿a quién corresponde mantener las máquinas con sus resguardos?", "A la empresa", "La mantención y los resguardos son responsabilidad empresarial."),
    ],
    op=("Ficha de ejemplo: en la «Planta Cordón Demo» hay 25 personas en el turno. Hechos de la semana: 20 personas asistieron a la capacitación de seguridad; la empresa no entregó a una persona el calzado de seguridad; un trabajador avisó de una fuga en una tubería; el comité de seguridad no revisó los registros del mes. Escribe (a) el porcentaje de asistencia a la capacitación, (b) cuántas personas faltaron, (c) a qué nivel (individual, colectivo o empresarial) corresponde cada uno de los tres últimos hechos, (d) qué haces si ves una fuga y a alguien caído junto a ella.",
        "(a) 20 ÷ 25 × 100 = 80 %. (b) 25 − 20 = 5 personas. (c) No entregar el calzado: empresarial; avisar de la fuga: individual; no revisar los registros: colectivo (del comité). (d) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien el porcentaje", "calcula bien las personas que faltaron", "clasifica los tres hechos", "indica no acercarse y avisar"],
        ["hoja con las cuatro respuestas"],
        ["dividir al revés", "confundir el nivel empresarial con el individual", "responder que se acerca a ayudar"],
        "Pregunta: «¿quién tenía el deber de cada hecho: una persona, el equipo o la empresa?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa cuatro hechos de una planta y clasifica cada uno como responsabilidad individual, colectiva o empresarial.",
    extend="Explica con un ejemplo por qué los tres niveles de responsabilidad deben cumplirse a la vez.",
)

# ============================================================ OAE-08, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Planta Demo». Documentos: el reglamento interno (normas de orden, higiene y seguridad de la empresa, que cada persona recibe y conoce), la matriz de riesgos (tabla que lista, por tarea, el peligro, el riesgo y el control), "
     "el procedimiento de trabajo seguro (documento aprobado que describe cómo hacer una tarea de forma segura; lo aplica personal autorizado), el registro de capacitación (quién se capacitó, en qué tema, cuántas horas y con qué firma), el informe de incidente (relato de un hecho que pudo causar o causó daño) y el permiso ambiental (autorización de la autoridad ambiental para operar bajo condiciones). "
     "Registro de capacitación de la semana (ejemplo): tema «uso del EPP», 2 horas, 20 personas convocadas, 16 con firma y 4 sin firma; tema «plan de emergencia», 1 hora, 20 personas con firma. "
     "Fragmento de la matriz: tarea «recorrido por el pasillo de molienda», peligro «pulpa derramada», riesgo «caída», control «mantener limpio y señalizar». Roles: trabajador, supervisor, prevencionista de riesgos, jefe de planta, comité de seguridad y autoridad fiscalizadora.")
build(
    O8, 2, F,
    use="Aprenderé los documentos con que una planta cumple el marco legal (reglamento interno, matriz de riesgos, procedimiento de trabajo seguro, registro de capacitación, informe de incidente y permiso ambiental) y los roles de cada persona.",
    prior=["Sé qué son las responsabilidades individual, colectiva y empresarial.", "Sé leer un registro escrito.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "Cumplir la norma vigente se demuestra con documentos. El reglamento interno reúne las normas de orden, higiene y seguridad de la empresa, y cada persona lo recibe y lo conoce. La matriz de riesgos es una tabla que lista, por cada tarea, el peligro, el riesgo y el control. El procedimiento de trabajo seguro es un documento aprobado que describe cómo hacer una tarea de forma segura; lo aplica personal autorizado y no se cambia por cuenta propia. El registro de capacitación deja constancia de quién se capacitó, en qué tema, cuántas horas y con qué firma.",
        "El informe de incidente es el relato de un hecho que pudo causar o causó daño; se informa aunque no haya lesionados, porque muestra fallas que pueden causar un accidente después. El permiso ambiental es la autorización de la autoridad ambiental para operar bajo ciertas condiciones, que la empresa debe cumplir. Las horas-persona de una capacitación son las personas por las horas: 10 personas durante 3 horas suman 30 horas-persona. Una persona convocada sin firma no cuenta como capacitada hasta que el hecho real se compruebe.",
        f"Roles: el trabajador cumple y avisa, el supervisor vigila que se cumplan los procedimientos, el prevencionista asesora, el jefe de planta responde por la empresa, el comité de seguridad revisa registros y condiciones, y la autoridad fiscalizadora controla el cumplimiento. Nadie firma por otra persona ni altera un registro. {EMER} {AVISO}",
    ],
    vocab=[("reglamento interno", "normas de orden, higiene y seguridad de la empresa que cada persona recibe y conoce"), ("matriz de riesgos", "tabla que lista, por tarea, el peligro, el riesgo y el control"), ("procedimiento de trabajo seguro", "documento aprobado que describe cómo hacer una tarea de forma segura"), ("registro de capacitación", "constancia de quién se capacitó, en qué tema, cuántas horas y con qué firma"), ("informe de incidente", "relato de un hecho que pudo causar o causó daño"), ("permiso ambiental", "autorización de la autoridad ambiental para operar bajo condiciones"), ("horas-persona", "personas multiplicadas por las horas que dura una actividad")],
    worked=[
        ("Horas-persona", "Una capacitación de ejemplo dura 3 horas y asisten 10 personas. ¿Cuántas horas-persona suma?", ["Se multiplican las personas por las horas.", "10 por 3 es 30."], "30 horas-persona"),
        ("Elegir el documento", "Una supervisora de ejemplo quiere dejar constancia escrita de un hecho que pudo causar un daño pero no hubo lesionados. ¿Qué documento usa?", ["Es el relato de un hecho que pudo causar daño.", "Ese documento es el informe de incidente."], "El informe de incidente"),
    ],
    mistakes=[("Contar como capacitada a una persona convocada que no firmó.", "Sin firma no hay constancia de que asistió.", "Se comprueba la asistencia real y se completa la capacitación si falta."),
              ("No informar un incidente porque nadie se lesionó.", "Un incidente sin lesiones muestra una falla que puede causar un accidente.", "Todo incidente se informa y se analiza.")],
    T=[
        ("abc", "En una planta minera: ¿qué es la matriz de riesgos?", "Una tabla que lista, por tarea, el peligro, el riesgo y el control", "El registro de las horas trabajadas por cada persona", "El plan de ventas del concentrado", "La matriz organiza la prevención por tarea."),
        ("abc", "En una planta minera: ¿qué es un informe de incidente?", "El relato de un hecho que pudo causar o causó daño", "La lista de asistentes a una charla", "El permiso para operar la planta", "El informe de incidente deja constancia de un hecho; la asistencia y el permiso son otros documentos."),
        ("abc", "En una planta minera: ¿qué es un procedimiento de trabajo seguro?", "Un documento aprobado que describe cómo hacer una tarea de forma segura y lo aplica personal autorizado", "Una opinión del supervisor sobre cómo trabajar", "Un manual que cada persona puede cambiar según su criterio", "El procedimiento es un documento aprobado; no se cambia por cuenta propia."),
        ("abc", "{F} ¿Qué documento muestra que la capacitación de «uso del EPP» tuvo asistentes firmados?", "El registro de capacitación", "El reglamento interno", "La matriz de riesgos", "El registro de capacitación anota asistentes, horas y firmas."),
        ("=", "{F} ¿Cuántas horas-persona suman las firmas de la capacitación «uso del EPP»?", "16*2", "Se multiplican las personas con firma por las horas.", " horas-persona"),
        ("=", "{F} ¿Cuántas horas-persona suma la capacitación «plan de emergencia»?", "20*1", "Se multiplican las personas con firma por las horas.", " horas-persona"),
        ("=", "{F} ¿Qué porcentaje de las personas convocadas firmó la capacitación «uso del EPP»?", "16*100//20", "Se divide los firmantes entre los convocados y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Cómo se consideran las 4 personas que no firmaron «uso del EPP»?", "Como no capacitadas hasta comprobar su asistencia real o completar la capacitación", "Como capacitadas, porque estaban convocadas", "Como capacitadas, si el supervisor las recuerda", "Sin firma no hay constancia de asistencia."),
        ("abc", "{F} Según el fragmento de la matriz, ¿cuál es el riesgo del recorrido por el pasillo de molienda?", "Caída", "Pulpa derramada", "Mantener limpio y señalizar", "La pulpa derramada es el peligro y mantener limpio es el control; el riesgo es la caída."),
        ("abc", "{F} ¿Quién vigila que se cumplan los procedimientos durante el turno?", "El supervisor", "El comité de seguridad, solo una vez al año", "La autoridad fiscalizadora, todos los días", "El supervisor está en el turno y vigila el cumplimiento."),
        ("=", "{F} ¿Cuántas horas-persona de capacitación firmada suman las dos capacitaciones de la semana?", "16*2+20*1", "Se suman las horas-persona de las dos capacitaciones.", " horas-persona"),
        ("abc", "{F} Un compañero propone no informar un incidente sin lesionados «porque no pasó nada». ¿Cuál es la mejor respuesta?", "Se informa igual, porque muestra una falla que puede causar un accidente después", "No se informa, porque no hubo lesionados", "Se informa solo si el supervisor lo pide", "Un incidente sin lesiones es una advertencia de una falla."),
        ("abc", "{F} El permiso ambiental establece condiciones de operación. ¿Quién debe cumplirlas?", "La empresa, y la autoridad ambiental fiscaliza su cumplimiento", "Solo el trabajador que está en el turno", "Solo la autoridad ambiental", "Las condiciones del permiso son de la empresa; la autoridad fiscaliza."),
    ],
    ctx=("abc", "Un compañero de práctica te pide que firmes por él el registro de capacitación porque llegó tarde. ¿Qué respondes?", "Que no se firma por otra persona, y que lo consultarás con un adulto responsable para que quede un registro real", "Que sí, porque llegó casi a tiempo", "Que sí, si él firma por ti otro día", "Una firma certifica la asistencia de quien firma."),
    sc=[
        ("En una planta minera: ¿qué es el reglamento interno?", "Las normas de orden, higiene y seguridad de la empresa que cada persona recibe y conoce", "El reglamento interno ordena el trabajo de todos."),
        ("En una planta minera: ¿cuántas horas-persona tiene una capacitación?", "Las personas multiplicadas por las horas que dura", "Las horas-persona miden la capacitación total."),
        ("En una planta minera: ¿qué se hace con un incidente sin lesiones?", "Se informa y se analiza igual", "Es una advertencia de una falla."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo». Registro de capacitación: tema «manejo de derrames», 3 horas, 25 personas convocadas, 20 con firma y 5 sin firma. Fragmento de la matriz: tarea «revisión de una cinta», peligro «partes en movimiento», riesgo «atrapamiento», control «resguardo fijo». Un trabajador vio que una persona retiraba un resguardo sin permiso, pero no hubo lesiones. Escribe (a) las horas-persona firmadas, (b) el porcentaje de firmantes, (c) cuál es el peligro, el riesgo y el control de la matriz, (d) qué documento corresponde para el hecho del resguardo y si se informa, (e) qué se hace con las 5 personas sin firma.",
        "(a) 20 × 3 = 60 horas-persona. (b) 20 ÷ 25 × 100 = 80 %. (c) Peligro: partes en movimiento; riesgo: atrapamiento; control: resguardo fijo. (d) El informe de incidente, y sí se informa aunque no hubo lesiones. (e) Se consideran no capacitadas hasta comprobar su asistencia real o completar la capacitación.",
        ["calcula bien las horas-persona", "calcula bien el porcentaje", "distingue peligro, riesgo y control", "nombra el informe de incidente", "trata a los sin firma como no capacitados"],
        ["hoja con las cinco respuestas"],
        ["contar a las personas sin firma como capacitadas", "decir que no se informa por no haber lesiones", "confundir peligro con riesgo"],
        "Pregunta: «¿qué prueba la asistencia real?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una matriz de riesgos de dos tareas con peligro, riesgo y control, y un registro de capacitación con asistentes firmados.",
    extend="Explica con un ejemplo por qué una persona sin firma no puede contarse como capacitada.",
)

# ============================================================ OAE-08, clase 3
F = ("Ficha 3 (informe de incidente de ejemplo, inventado). «Planta Demo». Relato: durante el turno de mañana, una persona de mantención retiró el resguardo de una cinta para alcanzar una pieza, sin permiso de trabajo y sin bloquear la energía, y lo dejó afuera. No hubo lesiones, pero la cinta arrancó y atrapó una herramienta. "
     "El supervisor no revisó la lista de verificación ese día. La empresa no había capacitado en bloqueo de energías a 2 de las 10 personas del equipo de mantención. "
     "Datos del mes (ejemplo): 50 personas que trabajaron 200 horas cada una y 2 accidentes con lesión. Índice de frecuencia de ejemplo = accidentes × 100.000 ÷ horas trabajadas (fórmula simplificada de ejemplo, no oficial).")
build(
    O8, 3, F,
    use="Aprenderé a analizar un caso de trabajo en papel con el marco legal: repartir responsabilidades individuales, colectivas y empresariales en un incidente, calcular un índice de ejemplo y proponer medidas ordenadas.",
    prior=["Sé qué son las responsabilidades individual, colectiva y empresarial.", "Sé qué documentos exige la norma vigente.", "Sé multiplicar y dividir números enteros."],
    explain=[
        "Analizar un incidente no es buscar culpables, sino entender qué falló en cada nivel para corregirlo. Se lee el relato, se separan los hechos y se pregunta quién tenía el deber en cada uno. Un hecho puede mostrar fallas en varios niveles a la vez: la persona que retiró un resguardo sin permiso incumplió su responsabilidad individual; el supervisor que no revisó la lista de verificación falló en vigilar el cumplimiento; la empresa que no capacitó falló en su responsabilidad empresarial.",
        "Las medidas se ordenan con la jerarquía de controles: primero lo que quita el peligro o lo vuelve imposible de alcanzar, como un resguardo que no se pueda retirar sin detener la máquina; después las reglas y la capacitación, y al final el equipo de protección. Un índice de frecuencia de ejemplo relaciona los accidentes con las horas trabajadas: con 1 accidente en 2.500 horas, el índice de ejemplo es 1 por 100.000 dividido entre 2.500, es decir 40. Sirve para comparar períodos; no es una fórmula oficial.",
        f"Un incidente se informa siempre, aunque no haya lesiones, y quien lo presencie no altera ni oculta nada. Quien ve a una persona en peligro junto a una máquina no se acerca: avisa. Este cuaderno no entrega asesoría legal. {EMER} {AVISO}",
    ],
    vocab=[("incidente", "hecho no deseado que pudo causar o causó daño y se informa aunque no haya lesiones"), ("accidente con lesión", "hecho que causó una lesión a una persona"), ("lista de verificación", "pauta con casillas que se marcan tras comprobar cada ítem"), ("bloqueo de energías", "medida que impide que un equipo parta por error mientras personal autorizado lo interviene"), ("índice de frecuencia de ejemplo", "accidentes multiplicados por 100.000 y divididos entre las horas trabajadas, fórmula simplificada de ejemplo")],
    worked=[
        ("Horas trabajadas", "En un mes de ejemplo, 30 personas trabajan 150 horas cada una. ¿Cuántas horas trabajan en total?", ["Se multiplican las personas por las horas de cada una.", "30 por 150 es 4.500."], "4.500 horas"),
        ("Índice de ejemplo", "Un mes de ejemplo tuvo 1 accidente con 2.500 horas trabajadas. ¿Cuál es el índice de ejemplo?", ["Se multiplica 1 por 100.000.", "100.000 dividido por 2.500 es 40."], "40"),
    ],
    mistakes=[("Creer que si nadie se lesionó, el incidente no necesita análisis.", "El incidente mostró fallas que pueden causar un accidente la próxima vez.", "Se informa y se analiza para corregir cada falla."),
              ("Atribuir todo el incidente a la persona que retiró el resguardo.", "Hubo fallas de vigilancia y de capacitación, que son de otros niveles.", "Se analizan los tres niveles: individual, colectivo y empresarial.")],
    T=[
        ("abc", "En la seguridad de una planta: ¿qué es un incidente?", "Un hecho no deseado que pudo causar o causó daño y que se informa aunque no haya lesiones", "Un accidente con lesionados graves solamente", "Una visita de la autoridad", "Un incidente se informa aunque no haya lesionados; es una advertencia."),
        ("abc", "En la seguridad de una planta: ¿por qué se informa un incidente sin lesiones?", "Porque muestra fallas que pueden causar un accidente después", "Porque así se sanciona a alguien", "Porque lo pide el proveedor de insumos", "El objetivo del informe es corregir fallas antes de que causen daño."),
        ("abc", "En la seguridad de una planta: ¿para qué sirve el índice de frecuencia de ejemplo?", "Para comparar períodos relacionando los accidentes con las horas trabajadas", "Para calcular el sueldo de cada persona", "Para medir la ley del concentrado", "El índice relaciona accidentes y horas; sirve para comparar."),
        ("=", "{F} ¿Cuántas horas trabajaron en total las 50 personas durante el mes?", "50*200", "Se multiplican las personas por las horas de cada una.", " horas"),
        ("=", "{F} ¿Cuál es el índice de frecuencia de ejemplo del mes?", "2*100000//(50*200)", "Se multiplican los accidentes por 100.000 y se dividen entre las horas trabajadas.", ""),
        ("abc", "{F} Retirar el resguardo de la cinta sin permiso de trabajo y sin bloquear la energía es incumplir una responsabilidad:", "Individual, porque cada persona debe seguir los procedimientos y los permisos", "De la autoridad minera, que debía impedirlo", "Colectiva del comité, que debía retirar el resguardo", "Seguir permisos y procedimientos es un deber de cada persona."),
        ("abc", "{F} No haber capacitado en bloqueo de energías a 2 de las 10 personas de mantención es incumplir una responsabilidad:", "Empresarial, porque capacitar es un deber de la empresa", "Individual de las 2 personas, que debían capacitarse solas", "De la autoridad minera", "La capacitación es una responsabilidad de la empresa."),
        ("abc", "{F} Que el supervisor no haya revisado la lista de verificación ese día es:", "Una falla en vigilar el cumplimiento, que es parte de su rol", "Una falla de la autoridad fiscalizadora", "Una falla solo de la persona de mantención", "Vigilar el cumplimiento de la lista es una tarea del supervisor."),
        ("=", "{F} Si el mes siguiente hubiera 1 accidente con las mismas horas, ¿cuál sería el índice de ejemplo?", "1*100000//(50*200)", "Se multiplica el accidente por 100.000 y se divide entre las horas trabajadas.", ""),
        ("abc", "{F} ¿Qué medida de la jerarquía actúa mejor sobre el origen del incidente?", "Un resguardo que no pueda retirarse sin detener la cinta", "Un letrero que diga «no retirar el resguardo»", "Pedir que quien retire el resguardo use guantes", "Una barrera que impide acceder al peligro actúa sobre su origen; el letrero y los guantes son niveles inferiores."),
        ("=", "{F} ¿Qué porcentaje del equipo de mantención está capacitado en bloqueo de energías?", "(10-2)*100//10", "Se resta los no capacitados al total y se calcula el porcentaje.", " %"),
        ("abc", "{F} Un compañero propone no informar el incidente porque «no hubo lesiones y solo se perdió una herramienta». ¿Cuál es la mejor respuesta?", "Se informa igual, para corregir las fallas antes de que causen un accidente", "No se informa, porque no hubo lesiones", "Se informa solo si la herramienta era cara", "Un incidente es una advertencia que debe analizarse."),
        ("abc", "{F} Durante una visita de ejemplo, ves que alguien retira un resguardo mientras la cinta está funcionando. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a empujar a la persona fuera de la cinta", "Esperar a ver qué pasa antes de avisar", "Acercarse a una máquina en marcha puede causar otro accidente; se avisa de inmediato."),
    ],
    ctx=("abc", "Un compañero de práctica te cuenta que retiró un resguardo sin permiso y te pide que no digas nada. ¿Qué respondes?", "Que lo informarás a un adulto responsable, porque un incidente se informa y no se oculta", "Que no dirás nada si no hubo lesiones", "Que lo guardarás en secreto si él promete no repetirlo", "Ocultar un incidente deja la falla sin corregir; ante un riesgo se avisa a un adulto responsable."),
    sc=[
        ("En la seguridad de una planta: ¿cuál es el objetivo de analizar un incidente?", "Entender qué falló en cada nivel para corregirlo", "El análisis busca corregir fallas, no solo señalar culpables."),
        ("En el análisis de un incidente: ¿cuántos niveles de responsabilidad se revisan?", "Los tres: individual, colectivo y empresarial", "Un incidente puede mostrar fallas en varios niveles."),
        ("En el análisis de un incidente: ¿cómo se calcula el índice de ejemplo?", "Multiplicando los accidentes por 100.000 y dividiendo entre las horas trabajadas", "El índice relaciona accidentes y horas."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo». Relato: una persona de bodega apiló sacos por encima de la altura permitida; el supervisor lo vio y no pidió corregirlo; la empresa no había capacitado en apilamiento a esa persona; los sacos cayeron, sin lesionados. Datos del mes: 25 personas con 160 horas cada una y 2 accidentes con lesión. Índice de ejemplo: accidentes × 100.000 ÷ horas trabajadas. Escribe (a) las horas trabajadas del mes, (b) el índice de ejemplo, (c) qué falla corresponde a cada nivel (individual, supervisión y empresarial), (d) una medida de ingeniería y una administrativa, (e) si el incidente se informa y por qué.",
        "(a) 25 × 160 = 4.000 horas. (b) 2 × 100.000 ÷ 4.000 = 50. (c) Individual: apilar sobre la altura permitida; supervisión: no pedir la corrección; empresarial: no capacitar en apilamiento. (d) Ingeniería: marcar o limitar físicamente la altura de las pilas; administrativa: una regla de altura máxima con capacitación y revisión. (e) Sí, porque aunque no hubo lesionados muestra fallas que pueden causar un accidente.",
        ["calcula bien las horas", "calcula bien el índice", "asigna bien las fallas por nivel", "propone una medida de ingeniería y una administrativa", "explica por qué se informa"],
        ["hoja con las cinco respuestas"],
        ["usar las horas de una sola persona", "decir que no se informa por no haber lesiones", "culpar solo a la persona que apiló"],
        "Pregunta: «¿quién tenía el deber en cada falla: la persona, quien supervisa o la empresa?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un incidente sin lesiones y escribe qué falló en el nivel individual, en la supervisión y en la empresa.",
    extend="Explica con un ejemplo por qué analizar solo la conducta de una persona no basta para evitar que el incidente se repita.",
)

# ============================================================ OAE-08, clase 4
F = ("Ficha 4 (matriz de riesgos de ejemplo, inventada). En la «Planta Demo» se valora cada riesgo con probabilidad (de 1 a 5) y consecuencia (de 1 a 5); el puntaje es probabilidad × consecuencia. Niveles de ejemplo: bajo, de 1 a 4; medio, de 5 a 12; alto, de 15 a 25. "
     "Tarea T1, recorrido por un pasillo con pulpa derramada: probabilidad 3 y consecuencia 4. Tarea T2, trabajo cerca de una cinta sin resguardo: probabilidad 4 y consecuencia 5. Tarea T3, revisión de una planilla en la oficina: probabilidad 2 y consecuencia 2. "
     "Tarea T4, paso de camiones por un patio sin señales: probabilidad 5 y consecuencia 3. Plan de acciones del mes: 8 acciones comprometidas y 6 cumplidas.")
build(
    O8, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular el puntaje de una matriz de riesgos, ordenar prioridades, ver el efecto de una medida y calcular el cumplimiento de un plan de acciones.",
    prior=["Sé qué es una matriz de riesgos.", "Sé multiplicar y dividir números enteros.", "Sé comparar un dato con un criterio."],
    explain=[
        "Una matriz de riesgos valora cada riesgo con dos números. La probabilidad dice qué tan posible es que el daño ocurra y la consecuencia dice qué tan grave sería. El puntaje es la probabilidad multiplicada por la consecuencia, y se compara con niveles que fija la empresa: por ejemplo, bajo, medio y alto. El puntaje sirve para ordenar las acciones: se atienden primero los riesgos de mayor puntaje. Con probabilidad 2 y consecuencia 3, el puntaje de ejemplo es 6.",
        "Una medida de control reduce la probabilidad o la consecuencia, y el puntaje se vuelve a calcular para verificar la mejora. Un riesgo bajo no es un riesgo inexistente: se mantiene su control. El cumplimiento de un plan de acciones se calcula dividiendo las acciones cumplidas entre las comprometidas y multiplicando por 100. Con 3 acciones cumplidas de 4, el cumplimiento es 75 %.",
        f"La valoración real de una planta la hacen personas con formación, con datos del lugar y la norma vigente; aquí solo se practica el razonamiento con números de ejemplo. Nunca se baja un puntaje sin haber aplicado una medida real. {EMER} {AVISO}",
    ],
    vocab=[("probabilidad", "qué tan posible es que el daño ocurra"), ("consecuencia", "qué tan grave sería el daño si ocurre"), ("puntaje de riesgo", "probabilidad multiplicada por consecuencia"), ("nivel de riesgo", "categoría (baja, media o alta) que resulta del puntaje"), ("plan de acciones", "lista de acciones comprometidas para controlar los riesgos"), ("cumplimiento del plan", "acciones cumplidas divididas entre comprometidas, en porcentaje")],
    worked=[
        ("Puntaje de riesgo", "Un riesgo de ejemplo tiene probabilidad 2 y consecuencia 3. ¿Cuál es el puntaje?", ["Se multiplica la probabilidad por la consecuencia.", "2 por 3 es 6."], "6"),
        ("Cumplimiento del plan", "Un plan de ejemplo tiene 4 acciones comprometidas y 3 cumplidas. ¿Cuál es el cumplimiento?", ["Se divide 3 entre 4 y se multiplica por 100.", "El resultado es 75 por ciento."], "75 %"),
    ],
    mistakes=[("Atender primero el riesgo con mayor consecuencia sin mirar la probabilidad.", "El puntaje combina probabilidad y consecuencia, y un riesgo muy probable puede ser más urgente.", "Se ordenan las acciones por puntaje."),
              ("Bajar la probabilidad en la matriz sin haber aplicado ninguna medida.", "Un puntaje alterado oculta que el riesgo sigue igual.", "El puntaje se recalcula solo después de una medida real.")],
    T=[
        ("abc", "En una matriz de riesgos: ¿qué es la probabilidad?", "Qué tan posible es que el daño ocurra", "Qué tan grave sería el daño si ocurre", "Cuánto cuesta la medida de control", "La probabilidad mide la posibilidad de que ocurra; la gravedad es la consecuencia."),
        ("abc", "En una matriz de riesgos: ¿qué es la consecuencia?", "Qué tan grave sería el daño si ocurre", "Qué tan posible es que el daño ocurra", "Cuántas personas trabajan en la tarea", "La consecuencia mide la gravedad del daño posible."),
        ("abc", "En una matriz de riesgos: ¿para qué sirve el puntaje?", "Para ordenar los riesgos y decidir cuáles se atienden primero", "Para calcular el sueldo de cada persona", "Para elegir el color de los cascos", "El puntaje sirve para priorizar las acciones de control."),
        ("=", "{F} ¿Cuál es el puntaje de la tarea T1?", "3*4", "Se multiplica la probabilidad por la consecuencia.", ""),
        ("=", "{F} ¿Cuál es el puntaje de la tarea T2?", "4*5", "Se multiplica la probabilidad por la consecuencia.", ""),
        ("=", "{F} ¿Cuál es el puntaje de la tarea T4?", "5*3", "Se multiplica la probabilidad por la consecuencia.", ""),
        ("abc", "{F} ¿Qué nivel tiene la tarea T1?", "Medio, porque su puntaje queda entre 5 y 12", "Alto, porque su consecuencia es 4", "Bajo, porque su probabilidad es 3", "El nivel depende del puntaje, no de un solo número."),
        ("abc", "{F} ¿Qué tarea debe atenderse primero?", "La T2, porque tiene el mayor puntaje", "La T4, porque tiene la mayor probabilidad", "La T3, porque es la que tiene menos personas", "T2 tiene 20 puntos, más que T4 con 15 y T1 con 12."),
        ("abc", "{F} La tarea T3 tiene nivel bajo. ¿Qué corresponde?", "Mantener sus controles, porque bajo no significa sin riesgo", "Quitar todos sus controles, porque no tiene riesgo", "Atenderla primero, porque es la más simple", "Un riesgo bajo se mantiene controlado."),
        ("=", "{F} Después de instalar un resguardo fijo, la probabilidad de T2 baja a 2 y la consecuencia sigue en 5. ¿Cuál es el nuevo puntaje?", "2*5", "Se multiplica la nueva probabilidad por la consecuencia.", ""),
        ("abc", "{F} ¿Qué nivel tiene ahora la tarea T2?", "Medio, porque su nuevo puntaje queda entre 5 y 12; mejoró, pero se sigue vigilando", "Bajo, porque la probabilidad bajó", "Alto, porque la consecuencia sigue en 5", "El nuevo puntaje de 10 corresponde al nivel medio."),
        ("=", "{F} ¿Cuál es el cumplimiento del plan de acciones, en porcentaje?", "6*100//8", "Se divide las acciones cumplidas entre las comprometidas y se multiplica por 100.", " %"),
        ("abc", "{F} El jefe dice que T4 se atiende después de T1 porque su consecuencia (3) es menor que la de T1 (4). ¿Cuál es la mejor objeción?", "El puntaje combina ambos números: T4 tiene mayor puntaje que T1 y es de nivel alto", "Ninguna, porque solo cuenta la consecuencia", "Que T1 no tiene consecuencia", "T4 es muy probable y su puntaje es mayor, así que su prioridad también."),
    ],
    ctx=("abc", "Un compañero propone bajar la probabilidad de T2 en la matriz de 4 a 2 «para que el riesgo salga medio», sin instalar nada. ¿Qué respondes?", "Que no, porque el puntaje solo baja si se aplica una medida real, y que lo consultarás con un adulto responsable", "Que sí, porque así se ve mejor", "Que sí, si lo corrige después", "Cambiar el puntaje sin cambiar la realidad oculta un riesgo que sigue igual."),
    sc=[
        ("En una matriz de riesgos: ¿cómo se calcula el puntaje?", "Multiplicando la probabilidad por la consecuencia", "El puntaje combina ambos números y permite comparar riesgos distintos."),
        ("En una matriz de riesgos: ¿qué se hace después de aplicar una medida?", "Se vuelve a calcular el puntaje para verificar la mejora", "Verificar confirma si la medida funcionó."),
        ("En un plan de acciones: ¿cómo se calcula el cumplimiento?", "Dividiendo las acciones cumplidas entre las comprometidas y multiplicando por 100", "El cumplimiento se expresa en porcentaje."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo». Niveles: bajo, de 1 a 4; medio, de 5 a 12; alto, de 15 a 25. Tarea T5, trabajo junto a una poza sin baranda: probabilidad 2 y consecuencia 5. Tarea T6, paso por un camino de camiones sin señales: probabilidad 5 y consecuencia 5. Tarea T7, apilado de sacos en la bodega: probabilidad 3 y consecuencia 3. Plan del mes: 10 acciones comprometidas y 5 cumplidas. Escribe (a) el puntaje y el nivel de cada tarea, (b) cuál se atiende primero, (c) el cumplimiento del plan, (d) qué haces si ves a una persona caer a la poza.",
        "(a) T5: 2 × 5 = 10, medio; T6: 5 × 5 = 25, alto; T7: 3 × 3 = 9, medio. (b) T6, por tener el mayor puntaje. (c) 5 ÷ 10 × 100 = 50 %. (d) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien los puntajes y niveles", "prioriza la tarea de mayor puntaje", "calcula bien el cumplimiento", "indica no acercarse y avisar"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "ordenar por una sola variable", "responder que se acerca al borde"],
        "Pregunta: «¿qué dos números multiplicas para cada tarea?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres tareas con probabilidad y consecuencia, calcula su puntaje y ordénalas por prioridad.",
    extend="Explica con un ejemplo por qué un riesgo con consecuencia grave pero poco probable puede tener menos prioridad que uno muy probable.",
)
