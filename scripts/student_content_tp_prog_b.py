"""Programación TP 3.º y 4.º medio: OAE-04 (aplicaciones con programación orientada a objetos), OAE-05 (aplicaciones web) y OAE-06 (mantención preventiva y correctiva de software). Código breve y datos inventados; todo se razona a mano."""
from __future__ import annotations

from tp_prog_common import build

O4 = "TP-PROG-3y4-OAE-04"
O5 = "TP-PROG-3y4-OAE-05"
O6 = "TP-PROG-3y4-OAE-06"

# ============================================================ OAE-04, clase 1
F = ("Ficha 13 (requerimiento de ejemplo, inventado). La «Papelería Los Cedros» quiere una aplicación que maneje productos. Clase de ejemplo (Python): "
     "class Producto: def __init__(self, nombre, precio): self.nombre = nombre ; self.precio = precio ; def total(self, cantidad): return self.precio * cantidad. "
     "Uso: p = Producto(«cuaderno», 1500) ; p.total(3). Exigencias: del usuario (la cajera) «que muestre el total rápido»; técnica «que no guarde datos personales de clientes en el producto».")
build(
    O4, 1, F,
    use="Aprenderé la idea de programar con objetos, qué exigencias debe cumplir una aplicación y qué cuidados con los datos corresponden.",
    prior=["Sé qué es una variable, una lista y una repetición.", "Sé qué es un requerimiento.", "Sé multiplicar cifras."],
    explain=[
        "La programación orientada a objetos organiza una aplicación en objetos que representan cosas del problema, como un producto, una cuenta o un alumno. Una clase es el molde que describe cómo son esos objetos; un objeto es un ejemplar concreto creado a partir de la clase. Cada objeto tiene atributos (los datos que guarda, como nombre y precio) y métodos (las acciones que sabe hacer, como calcular el total).",
        "En Python, el método __init__ se llama constructor: se ejecuta al crear el objeto y le da sus valores iniciales. La palabra self se refiere al objeto mismo. Así, p = Producto(«cuaderno», 1500) crea un objeto cuyo atributo precio vale 1500, y p.total(3) ejecuta su método con cantidad 3.",
        "Una aplicación debe cumplir exigencias de dos tipos: las de los usuarios (qué necesitan hacer, por ejemplo mostrar el total rápido) y las técnicas (cómo debe funcionar, por ejemplo seguridad, rapidez o no guardar datos personales de más). Antes de entregar, se prueba con datos de ejemplo y se deja un registro del cambio y de quién lo hizo.",
    ],
    vocab=[("clase", "molde que describe cómo son los objetos"), ("objeto", "ejemplar concreto creado a partir de una clase"), ("atributo", "dato que guarda un objeto"), ("método", "acción que sabe hacer un objeto"), ("constructor", "método que da los valores iniciales al crear el objeto (__init__)"), ("exigencia técnica", "condición de cómo debe funcionar la aplicación")],
    worked=[
        ("Atributo o método", "En la clase Producto de ejemplo, ¿«precio» es atributo o método, y «total» es atributo o método?", ["precio es un dato que el objeto guarda.", "total es una acción que calcula un valor."], "precio es atributo; total es método"),
        ("Usar un método", "Producto de ejemplo: p = Producto(«regla», 800). ¿Qué devuelve p.total(5)?", ["El método multiplica el precio por la cantidad.", "800 por 5."], "4000"),
    ],
    mistakes=[("Confundir la clase con el objeto y decir que «Producto» es el cuaderno de 1500 pesos.", "La clase es el molde; el cuaderno concreto es un objeto creado a partir de ella.", "Piensa: la clase describe cómo son todos; el objeto es uno en particular."),
              ("Guardar el teléfono de la clienta dentro del objeto Producto «por comodidad».", "Mezcla datos personales con datos que no los necesitan y rompe la exigencia técnica.", "Cada clase guarda solo los atributos que le corresponden.")],
    T=[
        ("abc", "En Programación: ¿qué es una clase?", "El molde que describe cómo son los objetos", "Un ejemplar concreto como el cuaderno de 1500 pesos", "Una variable que guarda un número", "La clase es el molde; el ejemplar concreto es el objeto."),
        ("abc", "En Programación: ¿qué es un método?", "Una acción que sabe hacer un objeto", "Un dato que guarda un objeto", "Un error del programa", "El método es una acción; el dato que guarda es un atributo."),
        ("abc", "¿Para qué sirve el constructor __init__?", "Para dar los valores iniciales al crear un objeto", "Para borrar el objeto", "Para mostrar el total en pantalla", "El constructor se ejecuta al crear el objeto."),
        ("=", "{F} ¿Qué devuelve p.total(3) con el objeto de la ficha?", "1500*3", "El método multiplica el precio por la cantidad.", ""),
        ("abc", "{F} ¿Qué atributos tiene un objeto Producto de la ficha?", "nombre y precio", "total y cantidad", "p y Producto", "Los atributos se crean en el constructor: nombre y precio."),
        ("abc", "{F} ¿Qué es p en la ficha?", "Un objeto creado a partir de la clase Producto", "La clase Producto", "Un método de la clase", "p es un ejemplar concreto: el cuaderno de 1500."),
        ("=", "Producto de ejemplo: p = Producto(«lápiz», 250). ¿Qué devuelve p.total(8)?", "250*8", "Se multiplica el precio del lápiz por la cantidad.", ""),
        ("abc", "{F} La exigencia «que muestre el total rápido» la pide la cajera. ¿Qué tipo de exigencia es?", "Del usuario", "Técnica de seguridad", "De licencia", "La pide quien usa la aplicación en su trabajo diario."),
        ("abc", "{F} Un programador agrega a la clase Producto el atributo «telefono_clienta». ¿Cuál es el problema?", "Incumple la exigencia de no guardar datos personales en el producto", "Hace que total devuelva cero", "El constructor deja de funcionar", "El producto no necesita datos personales de clientas."),
        ("abc", "Producto de ejemplo: a = Producto(«goma», 300) ; b = Producto(«tijera», 900). ¿Cuántos objetos y cuántas clases hay?", "2 objetos y 1 clase", "1 objeto y 2 clases", "2 objetos y 2 clases", "Hay dos ejemplares creados con el mismo molde Producto."),
        ("abc", "El programador entrega la clase sin probarla con ningún objeto de ejemplo ni registro del cambio. ¿Qué riesgo corre?", "Dar por bueno un resultado sin verificación ni responsable", "Que la clase tenga demasiados atributos", "Que la cajera aprenda más rápido", "Sin prueba ni registro nadie puede comprobar el resultado."),
        ("=", "Producto de ejemplo: p = Producto(«cartulina», 400). Se compran 3 y luego otras 2 con el mismo método. ¿Cuánto suman p.total(3) y p.total(2)?", "400*3+400*2", "Se suma el resultado de las dos llamadas al método.", ""),
        ("ab", "{F} ¿Cuántos atributos recibe el constructor de la ficha además de self?", "2, nombre y precio", "1, solo nombre", "El constructor recibe nombre y precio, es decir, dos atributos."),
    ],
    ctx=("abc", "La cajera de una papelería de ejemplo dice: «necesito que el programa muestre rápido el total de lo que llevo». La programadora lo anota. ¿Qué es lo siguiente que corresponde?", "Convertirlo en un requerimiento comprobable y confirmarlo con la jefatura", "Programar sin confirmar", "Cambiar la clase por una lista", "Una necesidad se traduce en una exigencia clara y comprobable antes de programar."),
    sc=[
        ("En Programación: ¿qué diferencia hay entre clase y objeto?", "La clase es el molde y el objeto es un ejemplar concreto", "Un molde puede crear muchos objetos."),
        ("¿Qué es un atributo?", "Un dato que guarda un objeto", "Por ejemplo, el nombre o el precio de un producto."),
        ("¿Qué datos no debe guardar un objeto Producto?", "Datos personales de clientes", "El producto no los necesita y se deben proteger."),
    ],
    op=("Una veterinaria de ejemplo pide una clase Mascota con atributos nombre y especie y un método saludo que devuelva «Hola, soy » más el nombre. Escribe la clase en Python, crea una mascota con datos inventados, escribe qué devuelve su método y explica en dos líneas qué dato del dueño no guardarías en la clase.",
        "class Mascota: def __init__(self, nombre, especie): self.nombre = nombre ; self.especie = especie ; def saludo(self): return «Hola, soy » + self.nombre. m = Mascota(«Luna», «gato») ; m.saludo() devuelve «Hola, soy Luna». No guardaría el teléfono ni la dirección del dueño en la clase, porque la mascota no los necesita.",
        ["define la clase con constructor y método", "crea un objeto y obtiene el resultado correcto", "nombra un dato personal que no guarda"],
        ["hoja con la clase, el objeto y las dos líneas"],
        ["olvidar self", "confundir la clase con el objeto", "guardar datos del dueño"],
        "Pregunta: «¿qué es la clase y qué es el objeto en tu ejemplo?». Si no responde, pídele que señale cada uno en su hoja."),
    reinforce="Escribe una clase Libro con atributos titulo y paginas y crea un objeto con datos inventados.",
    extend="Explica con un ejemplo inventado por qué una exigencia técnica puede ser tan importante como una del usuario.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 14 (diseño de ejemplo, inventado). Aplicación de un gimnasio de ejemplo. Clase base Persona (atributo nombre). Clase Socio hereda de Persona y agrega el atributo plan (mensual o anual). "
     "Clase Entrenador hereda de Persona y agrega el atributo especialidad. Atributo privado de Socio: _saldo (por convención, un guion bajo indica «no tocar desde fuera»). "
     "Historia de usuario: «Como recepcionista quiero registrar un socio para controlar su plan». Criterio de aceptación: «al registrar, el socio queda con su nombre y plan».")
build(
    O4, 2, F,
    use="Aprenderé herencia y encapsulamiento, y los documentos y roles que acompañan una aplicación orientada a objetos.",
    prior=["Sé qué son clase, objeto, atributo y método.", "Sé qué es el constructor.", "Sé qué es un requerimiento."],
    explain=[
        "La herencia permite que una clase tome los atributos y métodos de otra y agregue los suyos. La clase que se hereda se llama clase base (Persona) y la que hereda se llama clase derivada (Socio, Entrenador). Así se evita repetir código: el nombre se define una sola vez en Persona. Una clase derivada «es un tipo de» la clase base.",
        "El encapsulamiento significa proteger los datos de un objeto: se esconden los atributos importantes (por convención con un guion bajo, como _saldo) y se dejan métodos para consultarlos o cambiarlos con control. Así, un método puede rechazar un saldo negativo. El polimorfismo permite que objetos distintos respondan al mismo método a su manera.",
        "El trabajo deja documentos: el diagrama de clases (dibuja clases con sus atributos y métodos y las flechas de herencia), la historia de usuario (qué quiere hacer una persona y para qué) y el criterio de aceptación (cómo se comprueba que está bien). Los roles son el analista, el programador, el tester y el usuario que aprueba. Los datos personales de socios se protegen y no se usan en las pruebas.",
    ],
    vocab=[("herencia", "una clase toma atributos y métodos de otra"), ("clase base", "clase de la que otras heredan"), ("clase derivada", "clase que hereda de otra y agrega lo suyo"), ("encapsulamiento", "proteger los datos de un objeto y controlar su acceso"), ("diagrama de clases", "dibujo de clases con atributos, métodos y herencia"), ("historia de usuario", "frase que dice qué quiere hacer alguien y para qué"), ("criterio de aceptación", "condición que prueba que la historia está cumplida")],
    worked=[
        ("Reconocer la herencia", "Clases de ejemplo: Animal (atributo nombre), Perro hereda de Animal y agrega raza. ¿Qué atributos tiene un objeto Perro?", ["Hereda nombre de la clase base Animal.", "Agrega raza propia."], "nombre y raza"),
        ("Encapsular", "Un atributo _saldo no debe quedar negativo. ¿Cómo se protege?", ["No se cambia directamente desde fuera.", "Un método revisa el valor antes de cambiarlo y rechaza los negativos."], "Con un método que valida antes de cambiar el saldo"),
    ],
    mistakes=[("Copiar el atributo nombre en cada clase derivada en vez de heredarlo.", "Se repite código y, si cambia, hay que corregir en muchos lugares.", "Define el atributo común una vez en la clase base."),
              ("Cambiar _saldo directamente desde cualquier parte del programa.", "Se saltan las validaciones y el saldo puede quedar con valores inválidos.", "Cambia el saldo solo con métodos que validen.")],
    T=[
        ("abc", "En Programación: ¿qué es la herencia?", "Que una clase toma atributos y métodos de otra", "Que un objeto se copia a otro computador", "Que un programa se hereda a otra empresa", "La clase derivada reutiliza lo de la clase base."),
        ("abc", "En Programación: ¿qué es el encapsulamiento?", "Proteger los datos de un objeto y controlar cómo se cambian", "Copiar el objeto en una lista", "Escribir la clase sin atributos", "Se esconden los atributos importantes y se usan métodos para cambiarlos."),
        ("abc", "¿Qué dibuja un diagrama de clases?", "Las clases con sus atributos, métodos y herencias", "Los usuarios conectados al sistema", "Los respaldos de la base de datos", "Es un mapa de las clases y sus relaciones."),
        ("abc", "{F} ¿Cuál es la clase base?", "Persona", "Socio", "Entrenador", "Socio y Entrenador heredan de Persona."),
        ("abc", "{F} ¿Qué atributos tiene un objeto Socio?", "nombre y plan", "nombre y especialidad", "solo plan", "Hereda nombre de Persona y agrega plan."),
        ("abc", "{F} ¿Qué atributos tiene un objeto Entrenador?", "nombre y especialidad", "nombre y plan", "plan y especialidad", "Hereda el nombre de Persona y agrega la especialidad."),
        ("=", "{F} ¿Cuántas clases derivadas hay en el diseño?", "2", "Socio y Entrenador heredan de Persona.", " clases"),
        ("abc", "{F} ¿Qué parte de la historia de usuario dice el «para qué»?", "Para controlar su plan", "Como recepcionista", "Quiero registrar un socio", "La finalidad es lo que viene después de «para»."),
        ("abc", "{F} ¿Cuál es una buena prueba del criterio de aceptación?", "Registrar un socio de ejemplo y verificar que queda con nombre y plan", "Contar las clases del diagrama", "Borrar el atributo plan", "El criterio se comprueba con un caso concreto."),
        ("abc", "El código de la aplicación permite poner _saldo = -500 directamente. ¿Qué principio se rompe?", "El encapsulamiento", "La herencia", "El constructor", "El saldo debería cambiarse solo mediante métodos que validen."),
        ("abc", "Para probar el registro de socios, el tester copia la lista de socios reales del gimnasio con sus teléfonos. ¿Qué corresponde?", "Usar socios inventados de ejemplo", "Seguir con los reales para que sea más realista", "Pedir los datos a un amigo", "Las pruebas usan datos inventados que no identifican a personas."),
        ("=", "{F} Un gimnasio de ejemplo registra 18 socios con plan mensual y 7 con plan anual. ¿Cuántos objetos Socio hay?", "18+7", "Cada socio registrado es un objeto Socio.", " objetos"),
        ("ab", "{F} Se quiere agregar la clase Recepcionista con nombre y turno. ¿Qué conviene hacer?", "Que herede de Persona y agregue solo turno", "Copiar nombre y turno sin heredar", "Heredar de Persona evita repetir el atributo nombre."),
    ],
    ctx=("abc", "El programador de una aplicación de ejemplo piensa dejar todos los atributos de Socio abiertos «para que sea más fácil». La analista no está de acuerdo. ¿Qué propone ella?", "Proteger los atributos importantes y dar métodos que validen", "Dejar todo abierto y revisar si hay errores después", "Eliminar los atributos", "El encapsulamiento evita valores inválidos y ayuda a mantener el programa."),
    sc=[
        ("En Programación: ¿qué hereda una clase derivada?", "Atributos y métodos de la clase base", "Luego la clase derivada puede agregar los suyos."),
        ("¿Qué es una historia de usuario?", "Una frase que dice quién quiere hacer qué y para qué", "Ayuda a entender la necesidad antes de programar."),
        ("¿Qué datos se usan para probar?", "Datos de ejemplo inventados", "Los datos reales de personas no se usan en pruebas."),
    ],
    op=("Un colegio de ejemplo necesita una aplicación con Persona (nombre), Alumno (curso) y Profesor (asignatura). Dibuja el diagrama de clases con las flechas de herencia, escribe una historia de usuario con su criterio de aceptación y nombra los roles que revisarían el trabajo.",
        "Persona (nombre) es la clase base; Alumno (curso) y Profesor (asignatura) heredan de Persona. Historia: «Como secretaria quiero registrar un alumno para saber su curso». Criterio: al registrar un alumno de ejemplo queda con su nombre y curso. Revisarían el trabajo el tester y el usuario que aprueba, no quien programa.",
        ["dibuja la herencia con la clase base correcta", "escribe historia y criterio comprobable", "nombra revisores distintos al programador"],
        ["hoja con el diagrama, la historia y el criterio"],
        ["invertir la flecha de herencia", "escribir un criterio que no se puede comprobar", "revisar su propio trabajo"],
        "Pregunta: «¿qué atributo hereda Alumno?». Si no responde, pídele que lo marque en el diagrama."),
    reinforce="Dibuja un diagrama con una clase Vehículo y dos clases derivadas inventadas con un atributo propio cada una.",
    extend="Explica con un ejemplo inventado un caso en que la herencia no sea buena idea porque no hay una relación «es un tipo de».",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 15 (caso de ejemplo, inventado). Clase Cuenta del club «Los Lingües» (nombre de ejemplo): class Cuenta: def __init__(self, saldo): self._saldo = saldo ; "
     "def depositar(self, monto): if monto > 0: self._saldo = self._saldo + monto ; return True ; else: return False ; "
     "def retirar(self, monto): if monto > 0 and monto <= self._saldo: self._saldo = self._saldo - monto ; return True ; else: return False. "
     "Uso: c = Cuenta(1000) ; c.depositar(500) ; c.retirar(2000) ; c.retirar(300).")
build(
    O4, 3, F,
    use="Aprenderé a seguir a mano un programa con objetos, anotando el estado del objeto, y a comprobar si cumple las exigencias.",
    prior=["Sé qué son clase, objeto, atributo y método.", "Sé hacer la traza de un programa.", "Sé qué es el encapsulamiento."],
    explain=[
        "El estado de un objeto son los valores de sus atributos en un momento dado. Para analizar un programa con objetos se hace una traza del estado: se anota el valor de cada atributo antes y después de cada llamada a un método. Si un método tiene un if, se decide primero si la condición se cumple y recién después se aplica el cambio.",
        "En la clase de la ficha, depositar acepta solo montos positivos y retirar acepta solo montos positivos que no superen el saldo. Cada método devuelve True si hizo el cambio y False si lo rechazó, de modo que quien lo usa sabe qué pasó. El operador and exige que se cumplan las dos condiciones a la vez.",
        "Al terminar se verifica con una condición clara: el saldo nunca debe quedar negativo y debe coincidir con la suma de depósitos menos retiros aceptados. Los montos rechazados no cambian el saldo. Las pruebas usan cuentas de ejemplo inventadas, nunca cuentas ni saldos reales de personas.",
    ],
    vocab=[("estado", "valores de los atributos de un objeto en un momento"), ("True / False", "valores que indican si algo se cumplió o no"), ("and", "operador que exige que se cumplan dos condiciones a la vez"), ("monto", "cantidad de dinero de una operación"), ("rechazar", "no realizar un cambio porque no cumple las condiciones")],
    worked=[
        ("Estado después de un depósito", "Cuenta de ejemplo con saldo 200. Se llama depositar(50). ¿Cuál es el saldo y qué devuelve?", ["50 es positivo, se acepta.", "Saldo 200 + 50 = 250 y devuelve True."], "Saldo 250; devuelve True"),
        ("Retiro rechazado", "Cuenta de ejemplo con saldo 200. Se llama retirar(500). ¿Qué ocurre?", ["500 es mayor que el saldo 200, no se cumple monto <= saldo.", "Se rechaza: el saldo no cambia."], "Devuelve False y el saldo sigue en 200"),
    ],
    mistakes=[("Restar el monto aunque el retiro haya sido rechazado.", "Un retiro rechazado no cambia el saldo.", "Aplica el cambio solo si el if se cumple."),
              ("Confundir monto <= saldo con monto < saldo y rechazar un retiro igual al saldo.", "Retirar todo el saldo es válido; el signo <= incluye la igualdad.", "Lee el signo exacto de la comparación.")],
    T=[
        ("abc", "En Programación: ¿qué es el estado de un objeto?", "Los valores de sus atributos en un momento", "El nombre de su clase", "La lista de métodos que tiene", "El estado cambia cuando un método modifica los atributos."),
        ("abc", "¿Qué devuelve depositar(-100) en la clase de la ficha?", "False", "True", "-100", "El monto negativo no cumple monto > 0, así que se rechaza."),
        ("abc", "¿Qué exige el operador and en una condición?", "Que se cumplan las dos condiciones a la vez", "Que se cumpla al menos una", "Que no se cumpla ninguna", "and es verdadero solo si ambas condiciones lo son."),
        ("=", "{F} Después de c.depositar(500), ¿cuánto vale el saldo de la cuenta?", "1000+500", "Se suma el depósito aceptado al saldo inicial.", ""),
        ("abc", "{F} ¿Qué devuelve c.retirar(2000) con saldo 1500?", "False", "True", "1500", "2000 supera el saldo de 1500, así que se rechaza."),
        ("=", "{F} Tras c.depositar(500), c.retirar(2000) rechazado y c.retirar(300), ¿cuánto vale el saldo final?", "1000+500-300", "El retiro de 2000 no cambió nada; solo cuentan el depósito y el retiro aceptados.", ""),
        ("abc", "{F} ¿Cuántas operaciones fueron aceptadas en la secuencia de uso?", "2", "3", "1", "Se aceptan depositar(500) y retirar(300); retirar(2000) se rechaza."),
        ("abc", "Cuenta de ejemplo con saldo 400. Se llama retirar(400). ¿Qué ocurre?", "Se acepta y el saldo queda en 0", "Se rechaza porque el monto es igual al saldo", "Se acepta y el saldo queda en 400", "monto <= saldo incluye la igualdad, por eso el retiro es válido."),
        ("=", "Cuenta de ejemplo con saldo 900. Se hacen depositar(100), retirar(300) y depositar(50). ¿Cuánto vale el saldo?", "900+100-300+50", "Los tres montos son positivos y el retiro no supera el saldo, así que se aceptan.", ""),
        ("abc", "{F} Una persona traza: saldo inicial 1000, retirar(2000) → saldo -1000. ¿Cuál es su error?", "Aplicó un retiro que la condición debía rechazar", "Olvidó el depósito de 500", "Usó la clase equivocada", "El retiro de 2000 supera el saldo y no debe cambiar nada."),
        ("abc", "El tester prueba la clase con la cuenta real de su familia «para que sea más realista». ¿Qué corresponde?", "Usar cuentas y saldos de ejemplo inventados", "Seguir con la cuenta real porque es solo una prueba", "Compartir su número de cuenta con el equipo", "Los datos financieros reales no se usan ni se comparten en pruebas."),
        ("=", "Cuenta de ejemplo con saldo 100. Se hacen retirar(60), retirar(60) y depositar(10). ¿Cuánto vale el saldo final?", "100-60+10", "El segundo retiro se rechaza porque el saldo era 40; el depósito se acepta.", ""),
        ("abc", "{F} Se quiere cumplir la exigencia «el saldo nunca queda negativo». ¿Qué parte de la clase la garantiza?", "La condición monto <= saldo en retirar", "El valor inicial 1000", "El nombre de la clase", "La condición impide retirar más que el saldo."),
    ],
    ctx=("abc", "Una cuenta de ejemplo muestra saldo negativo después de una prueba. ¿Qué hace el equipo?", "Revisa la traza, encuentra la condición que falló y lo anota en la bitácora", "Entrega la clase igual porque el saldo negativo es raro", "Borra el registro de la prueba", "El error se rastrea con la traza y se deja constancia."),
    sc=[
        ("En Programación: ¿qué devuelve un método que rechazó una operación en la ficha?", "False", "Así quien lo usa sabe que no se hizo."),
        ("¿Cuándo cambia el saldo?", "Solo cuando la operación fue aceptada", "Un rechazo no modifica el estado del objeto."),
        ("¿Qué datos se usan para probar una cuenta?", "Saldos de ejemplo inventados", "Los datos financieros reales no se usan en pruebas."),
    ],
    op=("Con la clase Cuenta de la ficha, traza esta secuencia de ejemplo: c = Cuenta(300) ; c.depositar(200) ; c.retirar(600) ; c.retirar(150) ; c.depositar(0). Anota en una tabla qué devuelve cada llamada y el saldo después de cada una, y escribe el saldo final y la suma de verificación.",
        "Tabla: depositar(200) → True, saldo 500; retirar(600) → False, saldo 500; retirar(150) → True, saldo 350; depositar(0) → False, saldo 350. Saldo final 350. Verificación: 300 + 200 − 150 = 350.",
        ["traza cada llamada con su resultado", "obtiene el saldo final correcto", "verifica con una suma"],
        ["tabla de cuatro filas con retorno y saldo, y la verificación"],
        ["aplicar el retiro rechazado", "aceptar depositar(0)", "no verificar con una suma"],
        "Pregunta: «¿por qué depositar(0) devuelve False?». Si no responde, pídele que relea la condición monto > 0."),
    reinforce="Haz la traza de una cuenta con saldo 50 que recibe depositar(20) y retirar(100).",
    extend="Explica con un ejemplo inventado por qué un método debe devolver si la operación se hizo o no.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 16 (caso de ejemplo, inventado). Aplicación del taller «Mecánica Los Pinos» (nombre de ejemplo) para ordenar el trabajo. Dos diseños propuestos: Diseño A, una sola clase Trabajo con los atributos cliente, teléfono, patente, descripción, costo y estado. "
     "Diseño B, tres clases: Cliente (nombre, teléfono), Vehículo (patente, dueño: un Cliente) y Trabajo (descripción, costo, estado, vehículo: un Vehículo). Exigencias: (E1) un cliente puede tener varios trabajos sin repetir sus datos; "
     "(E2) el teléfono del cliente se guarda una sola vez y con acceso restringido; (E3) el costo total de un cliente se calcula sumando sus trabajos. Datos de ejemplo: trabajos de costo 20.000, 35.000 y 15.000 del mismo cliente. Roles de ejemplo: recepcionista (contacta a los clientes), mecánico (hace el trabajo) y jefe del taller.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo para elegir un diseño orientado a objetos y justificarlo con las exigencias.",
    prior=["Sé qué son herencia y encapsulamiento.", "Sé hacer la traza del estado de un objeto.", "Sé qué es una exigencia técnica y de usuario."],
    explain=[
        "Un buen diseño orientado a objetos reparte responsabilidades: cada clase guarda sus propios datos y hace sus propias acciones. Cuando una clase necesita datos de otra, no los copia: guarda una referencia al objeto (por ejemplo, un Vehículo guarda a su dueño, que es un objeto Cliente). Así los datos de una persona viven en un solo lugar.",
        "Para elegir entre dos diseños se contrastan con las exigencias: ¿cada exigencia se cumple o se rompe? Repetir los datos del cliente en cada trabajo viola la idea de guardar el dato una sola vez, aumenta el riesgo de inconsistencias (dos teléfonos distintos para la misma persona) y expone más veces un dato personal. El acceso restringido se logra con encapsulamiento.",
        "El criterio técnico se completa con cálculos de verificación, como sumar los costos de los trabajos de un cliente, y con la seguridad: solo los roles autorizados ven el teléfono. La decisión se escribe con evidencias de la ficha y se revisa si cambia una condición.",
    ],
    vocab=[("referencia", "enlace de un objeto a otro objeto en vez de copiar sus datos"), ("responsabilidad", "lo que una clase guarda y hace"), ("inconsistencia", "datos contradictorios sobre lo mismo"), ("acceso restringido", "solo ciertos roles pueden ver o cambiar el dato"), ("diseño", "forma de repartir las clases y sus datos")],
    worked=[
        ("Evitar la repetición", "En un diseño de ejemplo, cada Pedido copia el nombre y el teléfono del cliente. Un cliente hace 3 pedidos. ¿Cuántas veces queda guardado su teléfono?", ["Cada pedido guarda una copia.", "Son 3 pedidos."], "3 veces; mejor guardarlo una sola vez en Cliente"),
        ("Elegir con una exigencia", "Exigencia de ejemplo: «un dato personal se guarda una sola vez». ¿Qué diseño cumple: copiarlo en cada pedido o guardar una referencia al Cliente?", ["Copiarlo lo guarda varias veces.", "La referencia lo deja en un solo lugar."], "La referencia al Cliente"),
    ],
    mistakes=[("Elegir el diseño con menos clases porque «es más simple» sin revisar las exigencias.", "Una clase única puede repetir datos personales y romper una exigencia.", "Compara cada diseño con cada exigencia antes de elegir."),
              ("Dar acceso al teléfono a todos los roles porque «el sistema es interno».", "Los datos personales se ven solo por quien los necesita.", "Aplica el menor privilegio y encapsulamiento.")],
    T=[
        ("abc", "En Programación: ¿qué es una referencia entre objetos?", "Un enlace de un objeto a otro en vez de copiar sus datos", "Una copia exacta de un objeto", "Un error de sintaxis", "La referencia mantiene los datos en un solo lugar."),
        ("abc", "{F} ¿Cuál diseño repite el teléfono del cliente en cada trabajo?", "El diseño A", "El diseño B", "Ambos por igual", "En el diseño A el teléfono es un atributo de cada Trabajo."),
        ("abc", "{F} ¿Qué diseño cumple la exigencia E2, teléfono guardado una sola vez?", "El diseño B", "El diseño A", "Ninguno", "En el diseño B el teléfono está solo en Cliente."),
        ("=", "{F} ¿Cuántos pesos suma el costo total del cliente con los tres trabajos de ejemplo (exigencia E3)?", "20000+35000+15000", "Se suman los costos de todos sus trabajos.", " pesos"),
        ("=", "{F} Con el diseño A y los tres trabajos del mismo cliente, ¿cuántas veces queda guardado su teléfono?", "3", "Cada trabajo guarda su propia copia del teléfono.", " veces"),
        ("=", "{F} Con el diseño B y los tres trabajos del mismo cliente, ¿cuántas veces queda guardado su teléfono?", "1", "El teléfono vive solo en el objeto Cliente.", " vez"),
        ("abc", "{F} Si el cliente cambia de teléfono, ¿qué ocurre en el diseño A?", "Hay que corregirlo en cada trabajo y pueden quedar teléfonos distintos", "Se corrige una sola vez automáticamente", "No se puede cambiar", "Las copias repetidas obligan a corregir todas y pueden quedar inconsistentes."),
        ("abc", "{F} ¿Qué rol del taller debería ver el teléfono, según el menor privilegio?", "La recepcionista que contacta a los clientes", "Todos los mecánicos y visitas", "Cualquier persona que entre a la oficina", "Solo quien necesita el dato para su trabajo debe verlo."),
        ("abc", "{F} Un mecánico de ejemplo solo necesita ver la descripción del trabajo. ¿Qué permiso conviene darle?", "Ver descripción y estado, sin el teléfono del cliente", "Ver todos los datos del cliente", "Cambiar los costos de cualquier trabajo", "El menor privilegio le da solo lo que su rol necesita."),
        ("abc", "{F} ¿Qué diseño cumple todas las exigencias E1, E2 y E3?", "El diseño B", "El diseño A", "Ninguno de los dos", "El B evita repetir datos, protege el teléfono y permite sumar los trabajos."),
        ("=", "{F} Un cliente de ejemplo tiene trabajos de 12.000, 8.000 y 30.000. ¿Cuánto suma su costo total?", "12000+8000+30000", "Se suman los costos de los trabajos del mismo cliente.", " pesos"),
        ("abc", "{F} Si el taller solo atendiera a un cliente, ¿seguiría siendo más recomendable el diseño B por las exigencias del enunciado?", "Sí, porque cumple E2 y deja el diseño listo para más clientes", "No, el diseño A siempre es mejor", "No se puede decidir con ningún dato", "El diseño B cumple las exigencias de protección y evita repetir datos cuando crezca el taller."),
        ("abc", "El jefe de ejemplo dice: «guardemos también el RUT y la dirección de cada cliente, por si acaso». ¿Qué principio conviene recordar?", "Guardar solo los datos necesarios para el fin informado", "Guardar la mayor cantidad posible de datos", "Compartir los datos con otros talleres", "Los datos personales se limitan a lo que se necesita."),
    ],
    ctx=("abc", "Dos programadores discuten qué diseño usar para el taller. ¿Cómo se resuelve de forma responsable?", "Contrastando cada diseño con las exigencias escritas y anotando la decisión", "Votando por el que tiene menos clases", "Dejando que decida el que habla más fuerte", "La decisión se apoya en las exigencias y queda registrada."),
    sc=[
        ("En Programación: ¿por qué un Vehículo guarda una referencia al Cliente y no copia sus datos?", "Para que los datos del cliente estén en un solo lugar", "Así se evitan repeticiones e inconsistencias."),
        ("¿Cómo se calcula el costo total de un cliente?", "Sumando los costos de sus trabajos", "Es una verificación simple de la exigencia."),
        ("¿Quién ve el teléfono de un cliente?", "Solo quien lo necesita para su trabajo", "El menor privilegio protege los datos personales."),
    ],
    op=("Una peluquería de ejemplo propone dos diseños: A, una clase Cita con nombre, teléfono, servicio y precio de la clienta; B, clases Clienta (nombre, teléfono) y Cita (servicio, precio, clienta). Exigencias: el teléfono se guarda una sola vez y el precio total de una clienta se calcula sumando sus citas. Una clienta de ejemplo tiene tres citas de 8.000, 12.000 y 5.000. Elige un diseño con dos evidencias, calcula el total y explica qué rol vería el teléfono.",
        "Elijo el diseño B: guarda el teléfono una sola vez en Clienta (con A quedaría tres veces) y permite sumar las citas de la clienta. Total: 8.000 + 12.000 + 5.000 = 25.000 pesos. El teléfono lo vería solo quien agenda y contacta a las clientas, no el resto del equipo.",
        ["elige un diseño con dos evidencias", "calcula bien el total", "asigna el acceso al teléfono según el menor privilegio"],
        ["hoja con la elección, el cálculo y la regla de acceso"],
        ["elegir A sin contrastar con las exigencias", "sumar mal las citas", "dar el teléfono a todos"],
        "Pregunta: «¿cuántas veces queda el teléfono guardado en cada diseño?». Si no responde, pídele que cuente las copias."),
    reinforce="Dibuja las clases de una biblioteca de ejemplo (Socio, Libro, Préstamo) y cómo se relacionan sin repetir datos.",
    extend="Explica con un ejemplo inventado cómo cambiaría tu decisión si aparece una nueva exigencia.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 17 (caso de ejemplo, inventado). La «Panadería Doña Rosa» (nombre de ejemplo) quiere un sitio web para mostrar sus productos y recibir pedidos con un formulario que pide nombre, teléfono y dirección. "
     "El sitio tendrá tres páginas: inicio, productos y contacto. Un equipo de ejemplo: una diseñadora, un desarrollador y la dueña que aprueba los textos.")
build(
    O5, 1, F,
    use="Aprenderé cómo funciona una aplicación web, qué hace cada parte y qué cuidados exigen los datos de las personas que la usan.",
    prior=["Sé usar un navegador.", "Sé qué es un dato personal.", "Sé qué es un requerimiento."],
    explain=[
        "Una aplicación web funciona entre dos partes. El cliente es el navegador de la persona, que muestra la página; el servidor es el computador de la empresa que guarda la página y los datos y responde a los pedidos. Una página se arma con HTML (la estructura y el contenido), CSS (la presentación: colores y tamaños) y JavaScript (el comportamiento: reacciona a clics y valida formularios).",
        "Para que la gente vea el sitio hay que publicarlo: se contrata un hosting (servicio que guarda el sitio y lo mantiene disponible) y un dominio (el nombre con que se encuentra, como un nombre de ejemplo «panaderia-ejemplo.cl»). Un sitio seguro usa HTTPS, que cifra la comunicación entre el navegador y el servidor para que nadie pueda leer los datos en el camino.",
        "Un formulario recoge datos personales, así que exige cuidado: se piden solo los datos necesarios, se informa para qué se usan y se actúa según la norma vigente de protección de datos. Las imágenes y textos del sitio deben ser propios o tener permiso. El sitio debe poder usarse por todas las personas: textos legibles y descripciones de las imágenes.",
    ],
    vocab=[("cliente", "navegador de la persona que muestra la página"), ("servidor", "computador que guarda la página y responde pedidos"), ("HTML", "lenguaje que da estructura y contenido a la página"), ("CSS", "lenguaje que define la presentación de la página"), ("JavaScript", "lenguaje que da comportamiento a la página"), ("hosting", "servicio que mantiene el sitio disponible"), ("HTTPS", "comunicación cifrada entre navegador y servidor")],
    worked=[
        ("Quién hace qué", "Una página de ejemplo cambia el color del título. ¿Qué lenguaje se encarga de la presentación?", ["El color es parte de la presentación.", "La presentación la define CSS."], "CSS"),
        ("Datos necesarios", "Un formulario de ejemplo pide nombre, teléfono, dirección y color favorito para entregar un pedido. ¿Cuál dato sobra?", ["Para entregar se necesita saber a quién y dónde.", "El color favorito no es necesario."], "El color favorito"),
    ],
    mistakes=[("Pedir en el formulario todos los datos posibles «por si sirven».", "Se recogen datos personales sin necesidad y aumenta el riesgo.", "Pide solo lo necesario y avisa para qué se usa."),
              ("Usar fotos descargadas de cualquier sitio sin permiso.", "Las imágenes pueden tener derechos de autor.", "Usa fotos propias o con permiso claro de uso.")],
    T=[
        ("abc", "En Programación: ¿qué es el servidor en una aplicación web?", "El computador que guarda la página y responde a los pedidos", "El navegador de la persona", "El lenguaje que define los colores", "El servidor atiende pedidos; el navegador es el cliente."),
        ("abc", "En Programación: ¿qué hace CSS?", "Define la presentación, como colores y tamaños", "Guarda los datos del formulario", "Cifra la comunicación", "CSS se ocupa del aspecto de la página."),
        ("abc", "¿Qué es el hosting?", "El servicio que mantiene el sitio disponible en internet", "El nombre con que se encuentra el sitio", "El lenguaje de programación del sitio", "El hosting guarda el sitio; el dominio es su nombre."),
        ("abc", "{F} ¿Qué es el navegador de una clienta en el esquema cliente-servidor?", "El cliente", "El servidor", "El hosting", "El navegador pide la página y la muestra."),
        ("abc", "{F} ¿Qué dato del formulario no debería pedirse si solo se quiere atender pedidos?", "El estado civil de la persona", "El nombre", "La dirección de entrega", "El estado civil no es necesario para atender el pedido."),
        ("=", "{F} ¿Cuántas páginas tendrá el sitio?", "3", "Son inicio, productos y contacto.", " páginas"),
        ("abc", "{F} La dueña quiere que los datos del formulario viajen cifrados. ¿Qué debe usar el sitio?", "HTTPS", "Solo HTTP sin cifrar", "Un dominio más corto", "HTTPS cifra la comunicación entre navegador y servidor."),
        ("abc", "{F} El desarrollador quiere usar en el sitio una foto de un cuadro de pan sacada de otro sitio. ¿Qué corresponde?", "Usar una foto propia o pedir permiso de uso", "Copiarla porque está en internet", "Cambiarle un poco el color y publicarla", "Las imágenes tienen derechos de autor."),
        ("=", "{F} Si el sitio recibe 14 pedidos por el formulario el lunes y 9 el martes, ¿cuántos pedidos recibió en los dos días?", "14+9", "Se suman los pedidos de cada día.", " pedidos"),
        ("abc", "¿Qué lenguaje se usa para que una página valide un formulario cuando la persona hace clic en enviar?", "JavaScript", "HTML", "CSS", "JavaScript da comportamiento a la página."),
        ("abc", "{F} Una descripción escrita para cada foto del sitio, por ejemplo «pan de campo en una canasta», ayuda a...", "Que las personas con discapacidad visual comprendan la imagen", "Que la página pese menos", "Cifrar la comunicación", "El texto alternativo permite que un lector de pantalla describa la imagen."),
        ("abc", "{F} La dueña pide guardar los teléfonos de quienes compran para enviarles ofertas, sin avisarles. ¿Qué corresponde?", "Informar para qué se usan y pedir su permiso", "Enviarlas igual porque son sus clientes", "Vender la lista a otra empresa", "Los datos personales se usan con permiso y fin claro."),
        ("ab", "{F} El sitio publicado muestra el nombre «panaderia-ejemplo.cl». ¿Qué es ese nombre?", "El dominio", "El hosting", "El nombre con que se encuentra el sitio es el dominio, no el servicio que lo guarda."),
    ],
    ctx=("abc", "Una dueña de negocio de ejemplo pide publicar el sitio hoy mismo, aunque el formulario guarda los datos sin cifrar. ¿Qué responde el desarrollador?", "Explica el riesgo y propone activar HTTPS antes de publicar", "Publica igual sin avisar", "Quita el formulario sin consultar", "El riesgo se informa y se propone una solución antes de publicar."),
    sc=[
        ("En Programación: ¿qué hace HTML?", "Da estructura y contenido a la página", "CSS da la presentación y JavaScript el comportamiento."),
        ("¿Qué protege HTTPS?", "La comunicación entre el navegador y el servidor", "Cifra los datos para que nadie los lea en el camino."),
        ("¿Qué datos pide un formulario?", "Solo los necesarios, informando para qué se usan", "Los datos personales se limitan a lo necesario."),
    ],
    op=("Una peluquería de ejemplo quiere un sitio con tres páginas (inicio, servicios y reserva) y un formulario de reserva. Escribe una lista de los datos mínimos que pedirías en el formulario, qué lenguaje usarías para la presentación, qué pondrías para proteger los datos y qué cuidarías con las fotos del local.",
        "Datos mínimos: nombre, un medio de contacto y el servicio y la hora deseada. CSS para la presentación. HTTPS para cifrar y un aviso de para qué se usan los datos. Fotos propias o con permiso, y una descripción escrita para cada una.",
        ["pide solo datos necesarios", "nombra HTTPS y el aviso de uso de datos", "cuida las fotos con permiso y descripción"],
        ["hoja con la lista de datos y las cuatro decisiones"],
        ["pedir demasiados datos", "olvidar HTTPS", "usar fotos sin permiso"],
        "Pregunta: «¿por qué no pides la fecha de nacimiento?». Si no responde, pídele que relacione cada dato con su uso."),
    reinforce="Escribe tres páginas que tendría el sitio de una tienda de ejemplo y qué dato personal pediría su formulario.",
    extend="Explica con un ejemplo inventado por qué un sitio sin HTTPS pone en riesgo a quienes llenan un formulario.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 18 (página de ejemplo, inventada). Código HTML de una página: <h1>Panadería de ejemplo</h1> <p>Pan fresco todos los días.</p> <a href=«productos.html»>Ver productos</a> <img src=«pan.jpg» alt=«Pan de campo en una canasta»> "
     "<form> <label>Nombre</label> <input type=«text»> <button>Enviar</button> </form>. Hoja de estilo (CSS): h1 { color: blue ; }. Documentos del proyecto: mapa del sitio (las páginas y cómo se enlazan), maqueta (dibujo de cada página) y política de privacidad. Roles: diseñadora, desarrollador, administradora del sitio.")
build(
    O5, 2, F,
    use="Aprenderé las etiquetas básicas de HTML, los documentos de un proyecto web y los roles del equipo.",
    prior=["Sé qué hacen HTML, CSS y JavaScript.", "Sé qué es un servidor y un navegador.", "Sé qué es un dato personal."],
    explain=[
        "HTML usa etiquetas que se abren y se cierran. <h1> es un título principal, <p> un párrafo, <a href> un enlace a otra página, <img src alt> una imagen con su descripción alternativa, <form> un formulario, <input> un campo para escribir y <button> un botón. CSS usa reglas con un selector (a quién se aplica, como h1) y propiedades entre llaves (qué cambia, como color).",
        "Un sitio se planifica con documentos. El mapa del sitio lista las páginas y sus enlaces; la maqueta es el dibujo de cómo se verá cada página; el documento de requisitos dice qué contenidos hacen falta, y la política de privacidad explica qué datos se recogen, para qué y por cuánto tiempo. Estos documentos permiten revisar el trabajo antes de programar.",
        "Los roles reparten el trabajo: la diseñadora crea la maqueta, el desarrollador escribe el código, la administradora publica y mantiene el sitio y la dueña aprueba el contenido. Cuando algo del sitio falla, un enlace que no funciona devuelve el código 404 (página no encontrada) y un fallo del servidor devuelve el código 500; el código 200 significa que todo salió bien.",
    ],
    vocab=[("etiqueta", "marca de HTML que indica qué es cada parte de la página"), ("enlace", "texto que lleva a otra página (<a href>)"), ("alt", "descripción escrita de una imagen"), ("selector (CSS)", "parte de la regla que dice a qué elemento se aplica"), ("mapa del sitio", "lista de páginas y cómo se enlazan"), ("maqueta", "dibujo de cómo se verá cada página"), ("código 404", "respuesta «página no encontrada»")],
    worked=[
        ("Leer una etiqueta", "Etiqueta de ejemplo: <a href=«contacto.html»>Escríbenos</a>. ¿Qué muestra la página y a dónde lleva?", ["El texto visible es Escríbenos.", "El enlace lleva a contacto.html."], "Muestra «Escríbenos» y lleva a contacto.html"),
        ("Leer una regla CSS", "Regla de ejemplo: p { color: red ; }. ¿A qué elementos se aplica y qué cambia?", ["El selector p apunta a los párrafos.", "La propiedad color cambia a rojo."], "A los párrafos; su color pasa a rojo"),
    ],
    mistakes=[("Escribir una imagen sin el atributo alt.", "Una persona con lector de pantalla no sabe qué muestra la imagen.", "Escribe una descripción breve en alt."),
              ("Dejar enlaces que llevan a páginas que no existen.", "El navegador mostrará el error 404 y la persona se frustra.", "Revisa todos los enlaces con el mapa del sitio.")],
    T=[
        ("abc", "En Programación: ¿qué es una etiqueta de HTML?", "Una marca que indica qué es cada parte de la página", "Un archivo de imagen", "Una contraseña", "Las etiquetas dan estructura y significado al contenido."),
        ("abc", "¿Qué etiqueta crea un enlace a otra página?", "<a href>", "<h1>", "<p>", "El atributo href dice a qué página lleva el enlace."),
        ("abc", "¿Qué indica el código 404?", "Página no encontrada", "Todo salió bien", "Un fallo interno del servidor", "El código 404 aparece cuando no se encuentra la página."),
        ("abc", "{F} ¿Qué texto aparece como enlace en la página de la ficha?", "Ver productos", "productos.html", "Pan fresco todos los días.", "El texto del enlace está entre las etiquetas <a> y </a>."),
        ("abc", "{F} ¿Qué efecto tiene la regla h1 { color: azul ; }?", "El título principal se muestra en azul", "El párrafo se muestra en azul", "La imagen se muestra en azul", "El selector h1 apunta al título principal."),
        ("abc", "{F} ¿Qué dice el atributo alt de la imagen?", "Pan de campo en una canasta", "pan.jpg", "Ver productos", "El atributo alt contiene la descripción alternativa de la imagen."),
        ("abc", "{F} ¿A qué página lleva el enlace?", "productos.html", "pan.jpg", "inicio.html", "href señala la página de destino."),
        ("=", "{F} ¿Cuántos botones tiene el formulario de la ficha?", "1", "El formulario tiene una etiqueta <button>.", " botón"),
        ("abc", "{F} ¿Qué documento muestra cómo se verá cada página antes de programar?", "La maqueta", "El mapa del sitio", "La política de privacidad", "La maqueta es el dibujo de la página."),
        ("abc", "{F} ¿Qué documento explica qué datos se recogen y para qué?", "La política de privacidad", "La maqueta", "La hoja de estilo", "La política de privacidad informa sobre el uso de datos."),
        ("abc", "Una página de ejemplo no tiene enlace a «contacto» aunque el mapa del sitio lo exige. ¿Qué rol lo detecta al revisar?", "El tester o la administradora al comparar con el mapa", "Nadie, porque no se puede detectar", "La imagen de la página", "Comparar la página con el mapa del sitio muestra enlaces que faltan."),
        ("=", "El sitio de ejemplo tiene 5 páginas y cada una enlaza a las otras 4. ¿Cuántos enlaces hay en total?", "5*4", "Cada una de las 5 páginas tiene 4 enlaces.", " enlaces"),
        ("ab", "{F} Un visitante abre una página que no existe. ¿Qué código recibe?", "404", "200", "El código 404 significa que la página no se encontró; el 200 indica que todo salió bien."),
    ],
    ctx=("abc", "La administradora descubre que el formulario de ejemplo no explica para qué usa los datos. ¿Qué hace?", "Agrega un aviso y completa la política de privacidad antes de publicar", "Deja el formulario sin aviso", "Quita todos los campos", "Se informa para qué se usan los datos antes de recogerlos."),
    sc=[
        ("En Programación: ¿para qué sirve el atributo alt?", "Para describir la imagen con texto", "Ayuda a quienes usan lector de pantalla."),
        ("¿Qué es el mapa del sitio?", "La lista de páginas y cómo se enlazan", "Sirve para revisar que los enlaces funcionen."),
        ("¿Qué significa el código 404?", "Que la página no se encontró", "Suele indicar que un enlace está roto."),
    ],
    op=("Escribe el HTML de una página de ejemplo para una biblioteca con: un título principal «Biblioteca de ejemplo», un párrafo de bienvenida de una línea, un enlace a catalogo.html con el texto «Ver catálogo» y una imagen libros.jpg con alt. Luego escribe una regla CSS que ponga el título en verde y un mapa del sitio de dos páginas.",
        "<h1>Biblioteca de ejemplo</h1> <p>Bienvenidos a la biblioteca.</p> <a href=«catalogo.html»>Ver catálogo</a> <img src=«libros.jpg» alt=«Estantes con libros»>. CSS: h1 { color: green ; }. Mapa: inicio (enlaza a catálogo) y catálogo (enlaza a inicio).",
        ["usa las etiquetas correctas con su cierre", "incluye alt en la imagen", "escribe la regla CSS y el mapa del sitio"],
        ["hoja con el código, la regla y el mapa"],
        ["olvidar cerrar etiquetas", "omitir alt", "escribir un enlace sin href"],
        "Pregunta: «¿qué pasa si el archivo catalogo.html no existe?». Si no responde, pídele que recuerde el código 404."),
    reinforce="Escribe un párrafo y un enlace en HTML para una página de ejemplo que lleve a una página de contacto.",
    extend="Explica con un ejemplo inventado por qué dibujar la maqueta antes de programar ahorra errores.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 19 (caso de ejemplo, inventado). Formulario de inscripción a un taller del liceo «Liceo Los Robles» (nombre de ejemplo). Reglas: (R1) la edad debe ser un número entre 14 y 20; (R2) el correo debe contener «@»; "
     "(R3) el nombre no puede quedar vacío. Función de validación (JavaScript): function valida(edad, correo, nombre) { if (nombre == «») return «falta nombre» ; if (!(edad >= 14 && edad <= 20)) return «edad fuera de rango» ; "
     "if (!correo.includes(«@»)) return «correo inválido» ; return «ok» ; }. El ! significa «no», && significa «y», y el return termina la función con ese resultado.")
build(
    O5, 3, F,
    use="Aprenderé a seguir a mano la validación de un formulario web y a decidir qué respuesta recibe cada persona.",
    prior=["Sé qué es un formulario HTML.", "Sé hacer la traza de un condicional.", "Sé qué es validar un dato."],
    explain=[
        "Validar un formulario es revisar los datos antes de aceptarlos. En el navegador, JavaScript puede hacerlo apenas la persona envía, y muestra un mensaje claro si algo está mal, sin perder lo que escribió. Una función de validación recibe los datos y devuelve un resultado; el primer if que se cumple termina la función con su return, y los demás no se evalúan.",
        "Para razonar a mano se prueban casos de ejemplo uno por uno: se evalúan las condiciones en el orden en que están escritas y se anota el resultado. Los casos límite (14 y 20 en la edad) son los más importantes, porque ahí se cometen más errores. Los operadores && (y), || (o: basta que una se cumpla) y ! (no) permiten combinar condiciones.",
        "La validación en el navegador ayuda a la persona, pero no basta: cualquiera puede saltarse el navegador, así que el servidor debe volver a validar. Los mensajes de error no deben revelar datos de otros usuarios. Y los datos de personas menores de edad exigen especial cuidado: solo se piden los necesarios y se avisa a una persona adulta responsable cuando corresponde.",
    ],
    vocab=[("validación", "revisión de los datos antes de aceptarlos"), ("caso límite", "valor justo en el borde de lo permitido"), ("return", "instrucción que termina la función entregando un resultado"), ("&&", "operador «y»: ambas condiciones a la vez"), ("!", "operador «no»: invierte la condición"), ("validar en el servidor", "volver a revisar los datos en el servidor aunque ya se hayan revisado en el navegador")],
    worked=[
        ("Probar un caso límite", "Con las reglas de la ficha, ¿qué devuelve valida(14, «a@b.cl», «Ana»)?", ["El nombre no está vacío.", "14 está entre 14 y 20, y el correo tiene «@»: devuelve «ok»."], "ok"),
        ("Orden de las reglas", "Con la ficha, ¿qué devuelve valida(30, «sin_arroba», «»)?", ["La primera regla que se revisa es el nombre vacío.", "Se cumple y la función termina: devuelve «falta nombre»."], "falta nombre"),
    ],
    mistakes=[("Probar solo valores del medio, como 16 años, y creer que la función funciona.", "Los errores suelen estar en los bordes, como 14 y 20.", "Prueba siempre los casos límite."),
              ("Creer que si el navegador valida, el servidor ya no necesita validar.", "Los datos pueden llegar al servidor sin pasar por el navegador.", "El servidor valida de nuevo.")],
    T=[
        ("abc", "En Programación: ¿qué es un caso límite?", "Un valor justo en el borde de lo permitido", "Un valor imposible de escribir", "El último dato de la tabla", "Los casos límite revelan errores en las comparaciones."),
        ("abc", "¿Qué hace la instrucción return?", "Termina la función entregando un resultado", "Repite la función", "Borra el formulario", "return entrega el valor y la función termina."),
        ("abc", "{F} ¿Qué devuelve valida(14, «a@b.cl», «Ana»)?", "ok", "edad fuera de rango", "correo inválido", "La edad 14 cumple 14 ≤ edad ≤ 20 y el correo tiene @."),
        ("abc", "{F} ¿Qué devuelve valida(21, «a@b.cl», «Ana»)?", "edad fuera de rango", "ok", "correo inválido", "21 supera el máximo de 20."),
        ("abc", "{F} ¿Qué devuelve valida(18, «ana.cl», «Ana»)?", "correo inválido", "ok", "falta nombre", "El correo no contiene el símbolo @ pedido."),
        ("abc", "{F} ¿Qué devuelve valida(18, «a@b.cl», «»)?", "falta nombre", "ok", "correo inválido", "La primera regla revisada es el nombre vacío."),
        ("abc", "{F} ¿Qué devuelve valida(13, «sin_arroba», «Luis»)?", "edad fuera de rango", "correo inválido", "ok", "El nombre está bien; la regla de la edad se evalúa antes que la del correo y 13 no es válido."),
        ("=", "{F} De las edades 13, 14, 20 y 21, ¿cuántas aceptan la regla R1?", "2", "Solo 14 y 20 están dentro del rango permitido.", " edades"),
        ("abc", "{F} Una persona escribe edad >= 14 || edad <= 20 en vez de &&. ¿Qué problema aparece?", "Aceptaría cualquier edad, incluso 5 o 90", "Rechazaría todas las edades", "Aceptaría solo la edad 14", "Con «o» basta que se cumpla una condición, y toda edad cumple al menos una."),
        ("abc", "{F} Se cambia la regla a 14 < edad. ¿Qué pasa con una persona de 14 años?", "Queda rechazada, y es un error si la regla debía incluirla", "Queda aceptada igual", "Se cambia su edad a 15", "Con < la edad 14 queda fuera: se cambió el borde."),
        ("abc", "Un mensaje de error de ejemplo dice: «ese correo ya está inscrito por Marta López». ¿Cuál es el problema?", "Revela el dato de otra persona", "Es demasiado corto", "Usa HTML", "Los mensajes de error no deben mostrar datos de otros usuarios."),
        ("=", "Hay 120 inscripciones de ejemplo; 8 fueron rechazadas por la validación. ¿Cuántas quedaron aceptadas?", "120-8", "Se restan las rechazadas del total.", " inscripciones"),
        ("abc", "{F} El taller recibe la inscripción de una persona de 15 años. ¿Qué cuidado adicional corresponde?", "Pedir solo los datos necesarios y avisar a una persona adulta responsable cuando corresponde", "Pedir su dirección y la de sus amistades", "Publicar su nombre en el sitio", "Los datos de menores de edad se limitan al mínimo y se informa a la persona adulta responsable."),
    ],
    ctx=("abc", "El navegador valida bien, pero el desarrollador de ejemplo piensa que el servidor «no necesita» validar. La administradora no está de acuerdo. ¿Qué argumento da?", "Los datos pueden llegar al servidor sin pasar por el navegador, así que debe revisarlos", "El servidor es más lento", "Validar dos veces ocupa más espacio", "El servidor no puede confiar en que el navegador revisó."),
    sc=[
        ("En Programación: ¿qué casos se prueban primero en una validación?", "Los casos límite", "Los bordes del rango concentran más errores."),
        ("¿Quién vuelve a validar en el servidor?", "El servidor, aunque el navegador ya lo hizo", "Los datos pueden llegar sin pasar por el navegador."),
        ("¿Qué datos pides a una persona menor de edad?", "Solo los necesarios", "Así se protege la privacidad de la persona."),
    ],
    op=("Un club de ejemplo valida la inscripción así: function valida(edad, nombre) { if (nombre == «») return «falta nombre» ; if (!(edad >= 12 && edad <= 18)) return «edad fuera de rango» ; return «ok» ; }. Prueba a mano estos casos: (12, «Pía»), (19, «Beto»), (15, «») y (18, «Sol»). Anota qué devuelve cada uno y explica por qué 12 y 18 son casos límite.",
        "(12, «Pía») → ok. (19, «Beto») → edad fuera de rango. (15, «») → falta nombre. (18, «Sol») → ok. 12 y 18 son los bordes del rango permitido y ahí se cometen más errores de comparación.",
        ["evalúa cada caso en el orden de las reglas", "obtiene los cuatro resultados correctos", "explica qué es un caso límite"],
        ["tabla de cuatro filas con su resultado y la explicación"],
        ["evaluar el correo antes del nombre", "rechazar los casos límite", "olvidar el nombre vacío"],
        "Pregunta: «¿por qué (15, «») devuelve falta nombre y no ok?». Si no responde, pídele que siga las reglas en orden."),
    reinforce="Escribe una regla de validación para una contraseña de ejemplo de al menos 8 caracteres y prueba con dos casos inventados.",
    extend="Explica con un ejemplo inventado por qué un mensaje de error debe ser claro sin revelar datos de otras personas.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 20 (caso de ejemplo, inventado). Lista de verificación antes de publicar el sitio de la «Librería Los Lagos» (nombre de ejemplo). Los siete elementos son obligatorios. Elementos de la lista: (1) HTTPS activado; (2) contraseñas guardadas como hash; (3) validación también en el servidor; "
     "(4) imágenes con permiso y con alt; (5) política de privacidad visible; (6) respaldo del sitio; (7) revisión de enlaces. Peso de la página de inicio (datos de ejemplo): 3 imágenes de 400 KB cada una, un archivo de estilo de 50 KB y uno de JavaScript de 150 KB. "
     "Velocidad de ejemplo de la conexión de una visitante: 200 KB por segundo.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo para decidir si un sitio está listo para publicarse, cuidando seguridad, privacidad y rendimiento.",
    prior=["Sé qué hacen HTML, CSS y JavaScript.", "Sé qué es HTTPS y validar en el servidor.", "Sé calcular tiempos con división."],
    explain=[
        "Publicar un sitio es una decisión técnica que se respalda con una lista de verificación. Se revisa la seguridad (HTTPS, contraseñas guardadas como hash, validación en el servidor), la privacidad (política visible y solo datos necesarios), los contenidos (permiso y alt en imágenes) y la continuidad (respaldo y enlaces sin errores). Si falta un elemento obligatorio, no se publica hasta corregirlo.",
        "El rendimiento también importa: una página pesada tarda más en cargar, sobre todo en conexiones lentas. El peso de la página es la suma de sus archivos (imágenes, estilos y scripts) y el tiempo estimado de carga es el peso dividido por la velocidad. Reducir el tamaño de las imágenes es una mejora común.",
        "Una regla de seguridad clave: nunca confiar en lo que escribe el usuario. Todo dato que llega por un formulario se valida y se trata como texto, no como instrucciones, para evitar que alguien manipule el sitio. Las contraseñas nunca se guardan escritas y en este cuaderno jamás se escriben contraseñas reales. El equipo anota la decisión y a quien la autorizó.",
    ],
    vocab=[("lista de verificación", "lista de comprobaciones antes de publicar"), ("peso de la página", "suma del tamaño de todos sus archivos"), ("KB", "kilobyte: unidad de tamaño de archivos"), ("entrada no confiable", "dato que llega del usuario y debe validarse"), ("hash", "resumen que se guarda en vez de la contraseña escrita")],
    worked=[
        ("Tiempo de carga", "Una página de ejemplo pesa 600 KB y la conexión es de 100 KB por segundo. ¿Cuánto tarda?", ["Tiempo = peso dividido por velocidad.", "600 ÷ 100."], "6 segundos"),
        ("Decidir publicar", "En una lista de verificación de ejemplo falta HTTPS y todo lo demás está listo. ¿Se publica?", ["HTTPS protege los datos del formulario.", "Es obligatorio: se corrige antes de publicar."], "No, se corrige primero"),
    ],
    mistakes=[("Publicar el sitio con un elemento obligatorio pendiente «para cumplir la fecha».", "Los datos de las personas quedan expuestos.", "Informa a la jefatura y mueve la fecha."),
              ("Aceptar el texto del formulario sin revisar porque «solo escriben clientes».", "Cualquiera puede enviar datos inesperados o dañinos.", "Trata toda entrada como no confiable y valídala.")],
    T=[
        ("abc", "En Programación: ¿qué es el peso de una página?", "La suma del tamaño de todos sus archivos", "La cantidad de visitas por día", "El número de enlaces", "El peso incluye imágenes, estilos y scripts."),
        ("abc", "¿Cuándo debe publicarse un sitio con un elemento obligatorio pendiente?", "No debe publicarse hasta corregirlo", "Cuando llegue la fecha prevista", "Solo si la dueña lo pide una vez", "Los obligatorios se cumplen antes de publicar."),
        ("abc", "¿Cómo se trata un dato que escribe una visitante en un formulario?", "Como entrada no confiable: se valida", "Como una instrucción del sistema", "Como un dato ya correcto", "Todo dato del usuario debe revisarse."),
        ("=", "{F} ¿Cuántos KB pesa la página de inicio?", "3*400+50+150", "Se suman las tres imágenes, el estilo y el script.", " KB"),
        ("=", "{F} ¿Cuántos segundos tarda en cargar la página de inicio con la velocidad de ejemplo?", "(3*400+50+150)//200", "El tiempo es el peso total dividido por la velocidad.", " segundos"),
        ("=", "{F} Si se reduce cada imagen a 100 KB, ¿cuántos KB pesa la página?", "3*100+50+150", "Cambia el peso de las tres imágenes; lo demás queda igual.", " KB"),
        ("=", "{F} Con las imágenes reducidas y una conexión más lenta de 100 KB por segundo, ¿cuántos segundos tarda en cargar?", "(3*100+50+150)//100", "Se divide el nuevo peso por la velocidad de 100 KB por segundo.", " segundos"),
        ("abc", "{F} Falta el elemento (2): las contraseñas están guardadas escritas tal cual. ¿Qué corresponde?", "Guardarlas como hash antes de publicar", "Publicar y corregirlo después", "Enviarlas por correo a las clientas", "Contraseñas escritas tal cual exponen las cuentas si alguien accede a los datos."),
        ("abc", "{F} Falta el elemento (7): hay un enlace roto en la página de contacto. ¿Qué corresponde?", "Corregir el enlace y volver a revisar antes de publicar", "Publicar y esperar que nadie lo note", "Borrar el elemento (7) de la lista", "Un enlace roto muestra el error 404 y se corrige antes."),
        ("abc", "{F} Se revisaron seis de los siete elementos de la lista. ¿Qué dice el criterio?", "Falta uno obligatorio, no se publica aún", "Basta con seis, se publica", "Se publica si la dueña tiene prisa", "La lista exige cumplir todos los elementos obligatorios."),
        ("abc", "El desarrollador prueba el inicio de sesión con la contraseña real de su correo. ¿Qué corresponde?", "Usar una contraseña inventada de ejemplo", "Seguir con la real porque es solo una prueba", "Pedirle una contraseña real a un compañero", "Las contraseñas reales no se escriben ni se piden en pruebas."),
        ("abc", "{F} La política de privacidad dice que se guardan los datos por tiempo indefinido sin explicar por qué. ¿Qué conviene?", "Indicar para qué se guardan y por cuánto tiempo", "Dejarlo así", "Quitar la política", "La política debe informar con claridad el fin y la duración."),
        ("ab", "{F} Un visitante pide ver los datos suyos que guarda el sitio. ¿Qué corresponde?", "Derivar el pedido a quien administra los datos, según la norma vigente", "Ignorar el pedido", "Una persona puede consultar sus datos y el pedido se atiende por quien corresponde."),
    ],
    ctx=("abc", "A un día de publicar, el equipo de ejemplo descubre que el formulario no valida en el servidor. ¿Qué propone el técnico?", "Informar el riesgo, corregir la validación y publicar cuando esté lista", "Publicar y avisar después", "Ocultar el problema para no atrasar la fecha", "El riesgo se informa y se corrige antes de exponer datos."),
    sc=[
        ("En Programación: ¿cómo se calcula el tiempo de carga?", "Peso dividido por la velocidad", "A más peso, más tiempo de carga."),
        ("¿Cómo se guardan las contraseñas?", "Como hash, nunca escritas tal cual", "Así no se pueden leer si se filtra la tabla."),
        ("¿Se publica con un elemento obligatorio pendiente?", "No, primero se corrige", "Los obligatorios protegen a las personas."),
    ],
    op=("Un colegio de ejemplo tiene su página de inicio con 2 imágenes de 500 KB, un estilo de 100 KB y un script de 100 KB; la velocidad de ejemplo es de 300 KB por segundo. Calcula el peso, el tiempo de carga y cuánto tardaría si cada imagen se reduce a 200 KB. Luego marca cuáles de estos elementos son obligatorios antes de publicar: HTTPS, validación en el servidor, un color de fondo azul, política de privacidad.",
        "Peso: 2 × 500 + 100 + 100 = 1.200 KB. Tiempo: 1.200 ÷ 300 = 4 segundos. Con imágenes de 200 KB: 2 × 200 + 100 + 100 = 600 KB y 600 ÷ 300 = 2 segundos. Obligatorios: HTTPS, validación en el servidor y política de privacidad; el color de fondo no es obligatorio.",
        ["calcula peso y tiempos correctos", "calcula el tiempo con las imágenes reducidas", "distingue obligatorios de opcionales"],
        ["hoja con los cálculos y la clasificación de elementos"],
        ["sumar solo las imágenes", "dividir al revés", "considerar obligatorio el color"],
        "Pregunta: «¿qué mejora reduce más el tiempo?». Si no responde, pídele que compare los dos cálculos."),
    reinforce="Escribe cinco elementos de una lista de verificación para publicar un blog de ejemplo.",
    extend="Explica con un ejemplo inventado por qué las imágenes pesadas afectan más a quienes tienen una conexión lenta.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 21 (caso de ejemplo, inventado). La «Cooperativa Agua Clara» (nombre de ejemplo) usa un programa de cobro de cuentas que atiende a 6 usuarios. En el mes se registraron estas situaciones: (a) el programa se cierra solo al imprimir un recibo; "
     "(b) el disco del servidor está al 90 % de uso; (c) los trabajadores piden que el reporte incluya la comuna; (d) hace tres meses que no se prueba el respaldo. "
     "Tipos de mantención: correctiva (arregla una falla que ya ocurrió), preventiva (evita fallas futuras) y evolutiva (agrega o mejora funciones).")
build(
    O6, 1, F,
    use="Aprenderé qué es la mantención de software, qué tipos existen y por qué se hace con registro, autorización y cuidado de los datos.",
    prior=["Sé qué es un respaldo, una bitácora y una versión.", "Sé qué es un requerimiento.", "Sé calcular porcentajes simples."],
    explain=[
        "La mantención de software es el trabajo de mantener un programa funcionando y útil después de que se entregó. Hay tres tipos. La mantención correctiva arregla una falla que ya ocurrió. La mantención preventiva evita fallas futuras, por ejemplo probando el respaldo o liberando espacio en el disco. La mantención evolutiva agrega o mejora funciones a pedido de los usuarios.",
        "Un plan de mantención ordena el trabajo: qué se revisa, cada cuánto y quién es responsable. Su objetivo es mejorar la productividad, es decir, que las personas trabajen sin interrupciones y con menos errores. Una buena mantención reduce las caídas del sistema y el tiempo perdido por fallas.",
        "Todo cambio tiene riesgos, así que se hace con autorización, respaldo previo, prueba en un ambiente separado y bitácora. Los datos personales que maneja el programa, como los de los socios que pagan, se protegen según la norma vigente y se usan datos de ejemplo para probar. Nadie cambia el programa real sin que otra persona lo haya revisado.",
    ],
    vocab=[("mantención correctiva", "arregla una falla que ya ocurrió"), ("mantención preventiva", "evita fallas futuras"), ("mantención evolutiva", "agrega o mejora funciones"), ("plan de mantención", "documento que dice qué se revisa, cada cuánto y quién"), ("productividad", "trabajar sin interrupciones y con menos errores"), ("falla", "situación en que el programa no funciona como se espera")],
    worked=[
        ("Clasificar", "Un programa de ejemplo se cae todos los lunes y el equipo lo arregla. ¿Qué tipo de mantención es?", ["La falla ya ocurrió.", "Se arregla lo que falló: mantención correctiva."], "Correctiva"),
        ("Clasificar la prevención", "El equipo de ejemplo borra archivos temporales cada mes para que el disco no se llene. ¿Qué tipo es?", ["Se actúa antes de que falle el programa.", "Es mantención preventiva."], "Preventiva"),
    ],
    mistakes=[("Corregir una falla directamente en el programa que usan todos, sin respaldo ni prueba.", "Un cambio mal hecho puede dejar sin servicio a los usuarios.", "Haz el respaldo y prueba en un ambiente separado."),
              ("Esperar a que el disco se llene para actuar.", "Es mantención correctiva tardía y puede detener el trabajo.", "Planifica la mantención preventiva con anticipación.")],
    T=[
        ("abc", "En Programación: ¿qué es la mantención correctiva?", "La que arregla una falla que ya ocurrió", "La que evita fallas futuras", "La que agrega funciones nuevas", "Correctiva significa corregir lo que ya falló."),
        ("abc", "En Programación: ¿qué es la mantención preventiva?", "La que evita fallas futuras", "La que arregla una falla ya ocurrida", "La que cambia el diseño visual", "Prevenir es actuar antes de que ocurra la falla."),
        ("abc", "En Programación: ¿qué es la mantención evolutiva?", "La que agrega o mejora funciones", "La que borra el programa", "La que cambia al proveedor", "Evolutiva significa que el programa crece o mejora."),
        ("abc", "{F} La situación (a), el programa se cierra solo al imprimir, ¿qué tipo de mantención exige?", "Correctiva", "Preventiva", "Evolutiva", "Es una falla que ya ocurrió."),
        ("abc", "{F} La situación (b), el disco está al 90 %, ¿qué tipo de mantención corresponde para evitar que se llene?", "Preventiva", "Correctiva", "Evolutiva", "Se actúa antes de que el disco se llene y detenga el programa."),
        ("abc", "{F} La situación (c), agregar la comuna al reporte, ¿qué tipo de mantención es?", "Evolutiva", "Correctiva", "Preventiva", "Se agrega una función a pedido de los usuarios."),
        ("abc", "{F} La situación (d), hace tres meses que no se prueba el respaldo, ¿qué tipo de mantención conviene?", "Preventiva: probar la restauración del respaldo", "Evolutiva: cambiar el color del reporte", "Correctiva: no hay falla y no se hace nada", "Probar el respaldo evita descubrir tarde que no sirve."),
        ("=", "{F} Si el disco tiene 500 GB y está al 90 %, ¿cuántos GB están ocupados?", "500*90//100", "Se calcula el 90 % de 500.", " GB"),
        ("=", "{F} Con el disco de 500 GB al 90 %, ¿cuántos GB libres quedan?", "500-450", "Se resta el espacio ocupado al total.", " GB"),
        ("abc", "{F} Seis usuarios no pueden imprimir recibos por la falla (a) durante 2 horas. ¿Qué mide eso?", "El tiempo de trabajo perdido por la falla", "El costo de la licencia", "La velocidad del disco", "La mantención busca reducir esas pérdidas de productividad."),
        ("=", "{F} Los 6 usuarios pierden 2 horas cada uno por la falla (a). ¿Cuántas horas de trabajo se pierden en total?", "6*2", "Se multiplican los usuarios por las horas perdidas.", " horas"),
        ("abc", "Un técnico de ejemplo propone arreglar la falla probando con la base real de socios, con sus nombres y teléfonos. ¿Qué corresponde?", "Probar con datos de ejemplo inventados", "Probar con los datos reales porque es más rápido", "Copiar la base real a su celular", "Las pruebas no deben exponer datos personales reales."),
        ("ab", "{F} Sin ningún plan de mantención, ¿qué ocurre probablemente con el disco al 90 %?", "Se llenará y detendrá el programa en algún momento", "Se vaciará solo", "Sin plan se espera a que el problema ocurra y se pasa a mantención correctiva con interrupción."),
    ],
    ctx=("abc", "La administradora de una cooperativa de ejemplo dice: «arreglemos todo hoy directamente en el programa real, no hay tiempo para probar». ¿Qué responde el técnico?", "Explica el riesgo y propone respaldar y probar primero, aunque tome un poco más de tiempo", "Acepta sin decir nada", "Se niega a trabajar", "El técnico informa el riesgo y propone la forma segura."),
    sc=[
        ("En Programación: ¿qué tipos de mantención hay?", "Correctiva, preventiva y evolutiva", "Arreglan, previenen o mejoran el programa."),
        ("¿Qué se hace antes de cambiar el programa real?", "Respaldo, prueba y autorización", "Así se evita dejar sin servicio a los usuarios."),
        ("¿Para qué sirve un plan de mantención?", "Para ordenar qué se revisa, cada cuánto y quién", "Previene fallas y mejora la productividad."),
    ],
    op=("Una escuela de ejemplo usa un programa de notas. Clasifica estas situaciones como correctiva, preventiva o evolutiva y propone una acción para cada una: (a) no calcula bien el promedio de un curso; (b) quedan 10 GB libres de 100 GB; (c) piden agregar un reporte por asignatura; (d) hace un año no se prueba el respaldo.",
        "(a) correctiva: corregir el cálculo en una copia y probar con datos de ejemplo. (b) preventiva: liberar o ampliar espacio. (c) evolutiva: diseñar el reporte nuevo y probarlo. (d) preventiva: probar la restauración del respaldo.",
        ["clasifica bien las cuatro situaciones", "propone una acción segura para cada una", "incluye prueba con datos de ejemplo y registro"],
        ["tabla de cuatro filas con tipo y acción"],
        ["confundir preventiva con correctiva", "proponer cambiar el programa real sin respaldo", "usar datos reales de estudiantes"],
        "Pregunta: «¿qué diferencia hay entre corregir y prevenir?». Si no responde, pídele que ponga un ejemplo de cada una."),
    reinforce="Inventa tres situaciones de un programa de una tienda y clasifícalas por tipo de mantención.",
    extend="Explica con un ejemplo inventado cómo la mantención preventiva ahorra tiempo frente a la correctiva.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 22 (documentos de ejemplo, inventados). Registro de versiones de un programa de ejemplo: versión 1.0.0 (primera entrega); 1.0.1 (corrige un error de impresión); 1.1.0 (agrega el reporte por comuna); 2.0.0 (cambia el formato de la base de datos). "
     "Convención común de ejemplo: el primer número sube con cambios grandes, el segundo con funciones nuevas y el tercero con correcciones pequeñas. "
     "Reporte de error de ejemplo (REP-14): pasos para reproducirlo, resultado esperado, resultado obtenido y prioridad. Roles: mesa de ayuda (recibe el reporte), desarrollador, tester y jefe de TI.")
build(
    O6, 2, F,
    use="Aprenderé los documentos de la mantención (reporte de error, registro de versiones, plan y bitácora) y los roles de quienes participan.",
    prior=["Sé los tres tipos de mantención.", "Sé qué es una bitácora.", "Sé qué es un respaldo."],
    explain=[
        "El reporte de error es el documento con que se informa una falla. Debe decir los pasos para reproducirla, el resultado esperado, el resultado obtenido y la prioridad. Un buen reporte permite que otra persona vea la falla sin adivinar. Se evita escribir datos personales reales: se describen con datos de ejemplo.",
        "El registro de versiones (changelog) lista cada versión del programa con lo que cambió, para saber qué hay instalado y poder volver atrás. Una convención común numera las versiones con tres números: el primero sube con cambios grandes, el segundo con funciones nuevas y el tercero con correcciones pequeñas. El plan de mantención y la bitácora completan los documentos.",
        "Los roles se reparten el trabajo: la mesa de ayuda recibe y registra el reporte, el desarrollador busca y corrige la causa, el tester comprueba la corrección con datos de ejemplo y el jefe de TI (tecnologías de la información) aprueba y autoriza el cambio. Quien corrige no se aprueba a sí mismo; otra persona revisa antes de que la nueva versión llegue a los usuarios.",
    ],
    vocab=[("reporte de error", "documento que informa una falla con pasos, esperado y obtenido"), ("reproducir", "repetir los pasos para ver la falla"), ("changelog", "registro de versiones con lo que cambió"), ("prioridad", "qué tan urgente es atender algo"), ("versión", "estado numerado del programa en un momento"), ("jefe de TI", "responsable de tecnologías de la información que autoriza cambios")],
    worked=[
        ("Leer una versión", "Con la convención de ejemplo, el programa pasa de 1.2.0 a 1.2.1. ¿Qué tipo de cambio es?", ["Solo subió el tercer número.", "El tercer número indica correcciones pequeñas."], "Una corrección pequeña"),
        ("Completar un reporte", "Un reporte de ejemplo dice «no funciona». ¿Qué le falta?", ["Faltan pasos para reproducir.", "Falta lo esperado y lo obtenido."], "Pasos para reproducir y resultados esperado y obtenido"),
    ],
    mistakes=[("Escribir un reporte de error que solo diga «el programa falla».", "Nadie puede reproducir la falla ni saber qué se esperaba.", "Describe los pasos, lo esperado y lo obtenido."),
              ("Subir una versión nueva a los usuarios sin anotarla en el registro de versiones.", "No se sabe qué cambió ni cómo volver atrás.", "Anota cada versión y su cambio antes de entregarla.")],
    T=[
        ("abc", "En Programación: ¿qué es un reporte de error?", "Un documento que informa una falla con pasos, resultado esperado y obtenido", "Una copia de los datos del programa", "La lista de usuarios con permiso", "El reporte permite reproducir y corregir la falla."),
        ("abc", "En Programación: ¿para qué sirve el registro de versiones?", "Para saber qué cambió en cada versión y poder volver atrás", "Para guardar contraseñas", "Para medir la velocidad del programa", "El registro deja constancia de los cambios."),
        ("abc", "¿Qué rol autoriza el cambio antes de que llegue a los usuarios?", "El jefe de TI", "La mesa de ayuda al recibir el reporte", "El usuario que reportó", "La aprobación la da quien responde por la tecnología."),
        ("abc", "{F} Con la convención de ejemplo, la versión 1.0.1 agrega...", "Una corrección pequeña, la del error de impresión", "Una función nueva", "Un cambio grande en la base de datos", "El tercer número sube con correcciones pequeñas."),
        ("abc", "{F} ¿Qué cambio indica el paso de 1.0.1 a 1.1.0?", "Una función nueva: el reporte por comuna", "Una corrección pequeña", "Un cambio grande del formato de datos", "El segundo número sube con funciones nuevas."),
        ("abc", "{F} ¿Qué cambio indica el paso de 1.1.0 a 2.0.0?", "Un cambio grande: el formato de la base de datos", "Una corrección pequeña", "Una función nueva sencilla", "El primer número sube con cambios grandes."),
        ("=", "{F} ¿Cuántas versiones están registradas en la ficha?", "4", "Se cuentan 1.0.0, 1.0.1, 1.1.0 y 2.0.0.", " versiones"),
        ("abc", "{F} Un reporte de ejemplo dice: «al imprimir, se cierra». ¿Qué le falta para ser útil?", "Los pasos exactos, lo que se esperaba y lo que ocurrió", "El nombre completo de la usuaria", "La contraseña de la usuaria", "Sin pasos para reproducir y sin esperado y obtenido, no se puede corregir."),
        ("abc", "{F} ¿Quién recibe y registra el reporte de error?", "La mesa de ayuda", "El tester", "El jefe de TI", "La mesa de ayuda recibe y registra los pedidos."),
        ("abc", "{F} El desarrollador corrigió la falla y dice: «yo mismo lo apruebo». ¿Qué corresponde?", "Que lo pruebe el tester y lo autorice el jefe de TI", "Aceptar porque él lo conoce mejor", "Entregarlo sin revisar", "Quien corrige no se aprueba a sí mismo."),
        ("=", "El registro de ejemplo pasa de la versión 1.4.2 a la 1.4.5 con tres correcciones pequeñas seguidas. ¿Cuántas correcciones pequeñas hubo?", "5-2", "El tercer número sube de 2 a 5.", " correcciones"),
        ("abc", "El reporte REP-14 de ejemplo incluye el nombre completo y el teléfono de una cliente real para «reproducir mejor». ¿Qué corresponde?", "Reemplazarlos por datos de ejemplo inventados", "Dejarlos porque ayudan al desarrollador", "Enviar el reporte a todo el equipo", "Los reportes no deben llevar datos personales reales."),
        ("ab", "{F} Se entrega la versión 2.0.0 sin registro. Meses después hay un problema. ¿Qué dificultad aparece?", "No se sabe qué cambió ni a qué versión volver", "No aparece ninguna, el registro es opcional", "Sin registro de versiones es difícil rastrear qué cambió y volver atrás."),
    ],
    ctx=("abc", "La mesa de ayuda de una empresa de ejemplo recibe una llamada: «el sistema no sirve». ¿Qué hace?", "Pide los pasos, lo esperado y lo obtenido y lo registra como reporte", "Reenvía la llamada al desarrollador sin registrar", "Responde que no puede ayudar", "El reporte bien hecho permite corregir la falla."),
    sc=[
        ("En Programación: ¿qué incluye un buen reporte de error?", "Pasos para reproducir, resultado esperado, obtenido y prioridad", "Permite que otra persona vea la falla."),
        ("¿Qué indica el tercer número de una versión?", "Una corrección pequeña", "Es la convención común de ejemplo."),
        ("¿Quién autoriza la nueva versión?", "El jefe de TI", "Otra persona distinta del que programó revisa y autoriza."),
    ],
    op=("Un taller de ejemplo usa un programa de órdenes de trabajo versión 1.3.0. Un usuario dice que «el total sale mal». Con estos datos: se ingresan dos trabajos, uno de $10.000 y otro de $5.000, y el programa muestra un total de $10.000. Escribe el reporte de error con pasos, resultado esperado, resultado obtenido y prioridad; luego anota qué número tendría la versión si la corrección es pequeña y quién la probaría y autorizaría.",
        "Reporte: pasos: ingresar un trabajo de $10.000 y otro de $5.000 y pulsar total. Esperado: $15.000. Obtenido: $10.000. Prioridad: alta. Con una corrección pequeña la versión sería 1.3.1. Lo probaría el tester con datos de ejemplo y lo autorizaría el jefe de TI.",
        ["escribe pasos, esperado, obtenido y prioridad", "numera la versión según la convención", "nombra quien prueba y quien autoriza"],
        ["hoja con el reporte, la versión y los roles"],
        ["reporte vago", "numerar mal la versión", "dejar que el mismo programador autorice"],
        "Pregunta: «¿cómo sabría otra persona reproducir tu falla?». Si no responde, pídele que relea sus pasos."),
    reinforce="Escribe un reporte de error con los cuatro elementos para un programa de ejemplo que no guarda un archivo.",
    extend="Explica con un ejemplo inventado por qué una versión mal registrada dificulta volver atrás.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 23 (caso de ejemplo, inventado). Reporte REP-21 de la «Librería Los Boldos»: una usuaria dice que el promedio de las ventas de la semana «sale mal» y que otra rutina «no muestra el último valor». Primera rutina de ejemplo (Python; al dividir con / Python entrega un decimal, así que 200 se muestra como 200.0): "
     "ventas = [100, 200, 300] ; total = 0 ; for v in ventas: total = total + v ; promedio = total / len(ventas) ; print(promedio). "
     "Segunda rutina de ejemplo: for i in range(len(ventas) - 1): print(ventas[i]). range(n) recorre las posiciones 0, 1, …, n−1, y len(lista) es la cantidad de valores.")
build(
    O6, 3, F,
    use="Aprenderé a analizar en papel una falla, encontrar su causa con una traza y proponer una corrección segura.",
    prior=["Sé qué es un reporte de error.", "Sé hacer una traza de un for.", "Sé qué es len y qué es una posición de lista."],
    explain=[
        "Analizar una falla es buscar su causa con método. Primero se reproduce la falla con datos de ejemplo, luego se hace una traza para comparar lo que el programa hace con lo que debería hacer y finalmente se identifica la línea donde ambos se separan. Se corrige solo esa causa y se vuelve a probar, sin cambiar lo que funciona.",
        "Dos errores muy comunes son el error por uno (off-by-one), cuando una repetición se pasa o se queda corta en una posición, y el uso del valor equivocado en un cálculo. En la segunda rutina de la ficha, range(len(ventas) - 1) llega solo hasta la posición 1 y deja fuera el último valor; para recorrer todos se usa range(len(ventas)). El promedio se calcula con total dividido por la cantidad de valores.",
        "La corrección sigue el mismo cuidado que cualquier cambio: respaldo, prueba en una copia con datos de ejemplo, revisión por otra persona, nueva versión numerada y bitácora. Se registra la causa para evitar que se repita y se informa a quien reportó la falla.",
    ],
    vocab=[("causa raíz", "origen real de una falla"), ("error por uno", "repetición que se pasa o se queda corta en una posición"), ("promedio", "total dividido por la cantidad de valores"), ("len", "cantidad de valores de una lista"), ("range", "genera las posiciones que recorre un for"), ("regresión", "falla nueva que aparece al corregir otra cosa")],
    worked=[
        ("Calcular el promedio", "Valores de ejemplo: [10, 20, 30]. ¿Cuál es el promedio?", ["Total: 10 + 20 + 30 = 60.", "Cantidad: 3. Promedio: 60 ÷ 3."], "20"),
        ("Error por uno", "for i in range(len(lista) - 1) en una lista de 4 valores. ¿Qué posiciones recorre?", ["len es 4, así que range(3) recorre 0, 1 y 2.", "Queda fuera la posición 3."], "0, 1 y 2; falta la última"),
    ],
    mistakes=[("Corregir la falla cambiando varias líneas «por si acaso».", "Se pueden introducir fallas nuevas y es imposible saber qué corrigió el error.", "Cambia solo la causa identificada y vuelve a probar."),
              ("Dar por corregida la falla sin probar con los mismos datos del reporte.", "No se sabe si el caso original quedó resuelto.", "Repite los pasos del reporte con datos de ejemplo.")],
    T=[
        ("abc", "En Programación: ¿qué es la causa raíz de una falla?", "El origen real de la falla", "El síntoma que ve la usuaria", "La persona que la reportó", "Se corrige el origen, no solo el síntoma."),
        ("abc", "En Programación: ¿qué es un error por uno?", "Una repetición que se pasa o se queda corta en una posición", "Un reporte escrito dos veces", "Un usuario con dos cuentas", "Suele aparecer en los bordes de un recorrido."),
        ("abc", "¿Qué hace len(lista)?", "Entrega la cantidad de valores de la lista", "Borra la lista", "Entrega el último valor", "len cuenta los valores de la lista."),
        ("=", "{F} ¿Cuánto vale total al terminar el for de la primera rutina?", "100+200+300", "El for suma los tres valores.", ""),
        ("=", "{F} ¿Qué valor tiene la variable promedio al terminar la primera rutina?", "(100+200+300)//3", "El promedio es el total dividido por la cantidad de valores.", ""),
        ("abc", "{F} La segunda rutina de la ficha, ¿qué posiciones recorre con ventas de 3 valores?", "0 y 1", "0, 1 y 2", "1 y 2", "range(len(ventas) - 1) es range(2), que recorre 0 y 1."),
        ("abc", "{F} ¿Qué valores imprime la segunda rutina con ventas = [100, 200, 300]?", "100 y 200", "100, 200 y 300", "200 y 300", "Deja fuera la posición 2, el último valor."),
        ("abc", "{F} ¿Cómo se corrige la segunda rutina para que imprima los tres valores?", "Usar range(len(ventas))", "Usar range(len(ventas) - 2)", "Cambiar print por total", "range(3) recorre las posiciones 0, 1 y 2."),
        ("abc", "{F} Un técnico dice que la primera rutina está mal porque el promedio sale 200 y debería ser 300. ¿Cuál es el error de él?", "Confunde el promedio con el último valor", "Sumó mal los valores", "Olvidó dividir", "(100 + 200 + 300) ÷ 3 es 200; la rutina funciona bien."),
        ("=", "Valores de ejemplo: [4, 6, 8, 10]. ¿Cuál es el promedio?", "(4+6+8+10)//4", "Se divide el total por la cantidad de valores.", ""),
        ("abc", "{F} El técnico corrigió la segunda rutina pero también cambió la forma de sumar la primera. Aparece un error nuevo. ¿Cómo se llama esto?", "Una regresión", "Un respaldo", "Una versión mayor", "Una regresión es una falla nueva que aparece al corregir otra cosa."),
        ("abc", "{F} Después de corregir, ¿cuál es el siguiente paso seguro?", "Probar con los datos del reporte en una copia y pedir revisión", "Subir la versión a todos los usuarios de inmediato", "Borrar el reporte", "La corrección se prueba y revisa antes de entregarla."),
        ("abc", "El reporte REP-21 llegó con las ventas reales de una cliente con su nombre. ¿Qué corresponde al guardar el reporte?", "Reemplazar los datos por datos de ejemplo", "Guardarlo igual con los datos reales", "Publicarlo en un grupo abierto", "Los datos personales reales no se guardan en un reporte."),
    ],
    ctx=("abc", "Una usuaria de ejemplo reporta que «a veces el último producto no aparece en la lista». El técnico recuerda que el recorrido usa range(len(lista) - 1). ¿Qué hace?", "Reproduce con una lista de ejemplo, confirma el error por uno y corrige solo esa línea", "Cambia todo el programa", "Le dice a la usuaria que lo ignore", "Se confirma la causa con una prueba y se corrige solo lo necesario."),
    sc=[
        ("En Programación: ¿cómo se calcula un promedio?", "Total dividido por la cantidad de valores", "Se suma todo y se divide por cuántos son."),
        ("¿Qué posiciones recorre range(3)?", "0, 1 y 2", "Termina una posición antes del número."),
        ("¿Qué se prueba después de corregir?", "El caso original del reporte, con datos de ejemplo", "Así se confirma que la falla desapareció."),
    ],
    op=("Un programa de ejemplo debe imprimir todas las notas de una lista notas = [6, 5, 7, 4]. El código es: for i in range(len(notas) - 1): print(notas[i]). Haz la traza, indica qué imprime, qué falta, cómo se corrige y qué calcularías para comprobar con el promedio de las notas.",
        "len(notas) es 4, así que range(3) recorre las posiciones 0, 1 y 2 e imprime 6, 5 y 7; falta la nota 4. Se corrige con range(len(notas)). Promedio para comprobar: (6 + 5 + 7 + 4) ÷ 4 = 5,5, y el programa corregido debe mostrar los cuatro valores.",
        ["hace la traza e identifica los valores impresos", "señala la causa y la corrección", "propone una comprobación con datos de ejemplo"],
        ["hoja con la traza, la corrección y la comprobación"],
        ["decir que imprime todo", "cambiar varias líneas a la vez", "no comprobar la corrección"],
        "Pregunta: «¿qué posición queda fuera?». Si no responde, pídele que escriba las posiciones 0 a 3."),
    reinforce="Escribe una lista de cinco valores inventados y señala qué posiciones recorre range(len(lista) - 1).",
    extend="Explica con un ejemplo inventado por qué corregir una causa sin entenderla puede crear una regresión.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 24 (datos de ejemplo, inventados) de la «Cooperativa Agua Clara». Fallas registradas en un trimestre: 12 en total; 4 fueron reincidentes (la misma falla repetida). Tiempos de solución en horas: 2, 6, 4, 8 (cuatro fallas muestreadas). "
     "Prioridad = impacto × urgencia, ambos de 1 a 3 (3 es lo más alto). Fallas pendientes: F1 (impacto 3, urgencia 2); F2 (impacto 1, urgencia 3); F3 (impacto 2, urgencia 2). "
     "Plan preventivo de ejemplo: probar el respaldo cada 30 días y revisar el espacio del disco cada 15 días.")
build(
    O6, 4, F,
    use="Aprenderé a aplicar criterios técnicos con datos de ejemplo: priorizar fallas, calcular indicadores simples de mantención y planificar lo preventivo.",
    prior=["Sé los tipos de mantención.", "Sé calcular promedios y porcentajes simples.", "Sé qué es un plan de mantención."],
    explain=[
        "Cuando hay varias fallas pendientes se prioriza. Una forma sencilla es multiplicar el impacto (cuántas personas o procesos afecta) por la urgencia (qué tan rápido hay que actuar); mientras mayor el resultado, antes se atiende. Si dos fallas empatan, se desempata con un criterio escrito, como la seguridad de los datos.",
        "Los indicadores de mantención miden si el trabajo mejora. El tiempo promedio de solución es la suma de los tiempos dividida por la cantidad de fallas. El porcentaje de reincidencia es las fallas repetidas dividido por el total, multiplicado por 100: si es alto, las correcciones no están atacando la causa raíz. Los indicadores se leen con cuidado: pocos datos no permiten grandes conclusiones.",
        "El plan preventivo calendariza tareas repetidas, como probar el respaldo y revisar el espacio del disco, con responsable y fecha. La decisión final siempre queda registrada con sus datos y su límite, y quien la toma es la persona autorizada. Los datos personales se protegen y las pruebas usan datos de ejemplo.",
    ],
    vocab=[("impacto", "cuánto afecta una falla a personas o procesos"), ("urgencia", "qué tan rápido hay que actuar"), ("reincidencia", "falla que se repite"), ("tiempo promedio de solución", "suma de los tiempos dividida por la cantidad de fallas"), ("indicador", "cifra que mide si el trabajo mejora"), ("calendarizar", "fijar fechas y responsables para tareas repetidas")],
    worked=[
        ("Calcular la prioridad", "Falla de ejemplo con impacto 2 y urgencia 3. ¿Cuál es su prioridad?", ["Prioridad = impacto × urgencia.", "2 por 3."], "6"),
        ("Porcentaje de reincidencia", "En un mes de ejemplo hubo 20 fallas y 5 fueron reincidentes. ¿Qué porcentaje es?", ["5 ÷ 20 = 0,25.", "0,25 × 100."], "25 %"),
    ],
    mistakes=[("Atender primero la falla que más molesta a una persona, sin medir su impacto.", "Una molestia personal no siempre es la que más afecta a la organización.", "Calcula la prioridad con impacto y urgencia y desempata con un criterio escrito."),
              ("Concluir que el equipo trabaja mal porque un indicador subió una vez.", "Un solo dato no muestra una tendencia.", "Compara varios períodos y revisa las causas antes de concluir.")],
    T=[
        ("abc", "En Programación: ¿qué es la reincidencia de una falla?", "Que la misma falla se repite", "Que la falla nunca se arregla", "Que la falla afecta a todos", "La reincidencia indica que la causa no se corrigió del todo."),
        ("abc", "¿Cómo se calcula la prioridad de una falla?", "Impacto × urgencia", "Impacto + tiempo", "Urgencia − impacto", "La ficha define la prioridad como el producto de impacto y urgencia."),
        ("=", "{F} ¿Cuál es la prioridad de la falla F1?", "3*2", "Se multiplica el impacto 3 por la urgencia 2.", ""),
        ("=", "{F} ¿Cuál es la prioridad de la falla F2?", "1*3", "Se multiplica el impacto 1 por la urgencia 3.", ""),
        ("abc", "{F} ¿Qué falla se atiende primero según la prioridad?", "F1", "F2", "F3", "F1 tiene prioridad 6; F2 tiene 3 y F3 tiene 4."),
        ("abc", "{F} ¿Cuál es el orden de atención de mayor a menor prioridad?", "F1, F3, F2", "F2, F3, F1", "F3, F1, F2", "Las prioridades son 6, 4 y 3."),
        ("=", "{F} ¿Cuál es el tiempo promedio de solución de las cuatro fallas muestreadas?", "(2+6+4+8)//4", "Se suman los tiempos y se divide por la cantidad.", " horas"),
        ("=", "{F} ¿Qué porcentaje de las 12 fallas fue reincidente?", "4*100//12", "Se divide las reincidentes por el total y se multiplica por 100, redondeando hacia abajo.", " %"),
        ("abc", "{F} Un jefe dice: «con 33 % de reincidencia las correcciones no atacan bien la causa raíz». ¿Es una conclusión prudente?", "Es una pista que hay que revisar con más datos y las causas", "Es una prueba definitiva de mala gestión", "No dice nada sobre las correcciones", "Un indicador sugiere una revisión, pero no prueba por sí solo."),
        ("=", "{F} Con el plan preventivo, ¿cuántas revisiones del disco se hacen en 60 días?", "60//15", "Se divide el período por la frecuencia de revisión.", " revisiones"),
        ("=", "{F} Con el plan preventivo, ¿cuántas pruebas de respaldo se hacen en 90 días?", "90//30", "Se divide el período por la frecuencia de la prueba.", " pruebas"),
        ("abc", "{F} Dos fallas de ejemplo empatan en prioridad: una puede exponer datos personales de socios y otra solo cambia el color de un botón. ¿Cuál se atiende primero?", "La que puede exponer datos personales", "La del color del botón", "Da lo mismo", "Se desempata con un criterio escrito que prioriza la seguridad de los datos."),
        ("abc", "El técnico entrega un informe con indicadores que no coinciden con sus registros y dice «da lo mismo». ¿Qué principio se rompe?", "Dar por bueno un resultado sin verificación ni responsable", "El menor privilegio", "La clave primaria única", "Los indicadores deben respaldarse en los registros y verificarse."),
    ],
    ctx=("abc", "El jefe de TI de una empresa de ejemplo pide reducir la reincidencia a cero este mes y sugiere ocultar las fallas repetidas del informe. ¿Qué responde la técnica?", "Propone atacar las causas y mantener el informe completo y verdadero", "Oculta las fallas repetidas para cumplir", "Cambia las cifras del informe", "Los indicadores deben ser verdaderos y la mejora se logra atacando las causas."),
    sc=[
        ("En Programación: ¿cómo se calcula el tiempo promedio de solución?", "Suma de tiempos dividida por la cantidad de fallas", "Es el promedio de los tiempos de solución."),
        ("¿Qué indica una reincidencia alta?", "Que quizás no se corrigió la causa raíz", "Hay que revisar las causas con más datos."),
        ("¿Quién decide qué falla se atiende primero?", "La persona autorizada, con un criterio escrito", "La decisión queda registrada con sus datos."),
    ],
    op=("Una empresa de ejemplo tiene tres fallas pendientes: A (impacto 2, urgencia 3), B (impacto 3, urgencia 3) y C (impacto 1, urgencia 1). Calcula la prioridad de cada una y el orden de atención. Además, el mes tuvo 15 fallas con 3 reincidentes: calcula el porcentaje de reincidencia y escribe dos líneas de conclusión con un límite.",
        "Prioridades: A = 6, B = 9, C = 1. Orden: B, A, C. Reincidencia: 3 ÷ 15 × 100 = 20 %. Conclusión: la reincidencia es moderada y conviene revisar las causas de las tres reincidentes. Límite: un solo mes no muestra una tendencia.",
        ["calcula bien las tres prioridades y el orden", "calcula el porcentaje de reincidencia", "concluye con prudencia y declara un límite"],
        ["hoja con la tabla de prioridades, el porcentaje y la conclusión"],
        ["sumar en vez de multiplicar", "dividir al revés", "concluir sin declarar un límite"],
        "Pregunta: «¿qué falla atiendes primero y por qué?». Si no responde, pídele que relea las prioridades."),
    reinforce="Inventa tres fallas con impacto y urgencia, calcula su prioridad y ordénalas.",
    extend="Explica con un ejemplo inventado por qué un indicador de un solo mes no basta para tomar una decisión grande.",
)
