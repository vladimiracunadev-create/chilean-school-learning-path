"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 21 (ahorro, crédito, inversión y riesgo financiero) y OA 22 (consumo informado, derechos y endeudamiento)."""
from __future__ import annotations

from hi5_lib import build

MAT = "Lápiz y papel. Las fichas, las ofertas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ================================================================ OA 21
OA = "HI1M OA 21"

# ---------------------------------------------------------------- Clase 1
F1 = ("Ficha de ejemplo de instrumentos financieros. Libreta de ahorro: guarda dinero con un interés bajo y se puede retirar casi de inmediato. "
      "Préstamo de consumo: se recibe dinero hoy y se devuelve en cuotas con interés. "
      "Tarjeta de crédito: se compra ahora y se paga después; si no se paga todo, se cobra interés sobre lo que queda. "
      "Acción: una parte pequeña de una empresa que se compra y vende en la bolsa; su valor sube y baja, y se puede ganar o perder dinero. "
      "Previsión: ahorro durante la vida laboral para recibir una pensión en la vejez.")
build(
    OA, 1, F1,
    use="Aprenderé a describir los instrumentos financieros de ahorro, crédito e inversión y a distinguir su riesgo y su liquidez. Sirve para decidir qué hacer con el dinero propio sin confundir ahorrar con invertir.",
    prior=["Sé qué es la escasez y qué es el costo de oportunidad.", "Sé calcular un porcentaje sencillo de una cantidad.", "Sé que una deuda es dinero que se debe devolver."],
    explain=[
        "Un instrumento financiero es un medio que permite guardar, prestar o hacer crecer el dinero. Ahorrar es guardar parte del ingreso para usarlo después, por ejemplo en una libreta de ahorro, una cuenta o una caja vecina, que es un punto de atención financiera instalado en un comercio de barrio, útil donde no hay sucursales cerca. El ahorro suele tener riesgo bajo, es decir, poca probabilidad de perder el dinero, pero también paga poco interés.",
        "El crédito es recibir dinero o comprar ahora y pagar después, con un costo llamado interés, que es lo que se paga por usar dinero ajeno. Son créditos el préstamo de consumo, la línea de crédito (monto disponible que se paga con interés al usarlo) y la tarjeta de crédito. Invertir es destinar dinero a algo que podría crecer, como una acción en la bolsa, y se acepta un riesgo mayor: se puede ganar más, pero también perder. La previsión es un ahorro de largo plazo para la pensión.",
        "Para comparar instrumentos uso tres ideas: la rentabilidad, que es lo que se espera ganar; el riesgo, que es la posibilidad de perder; y la liquidez, que es la facilidad para convertir el ahorro en dinero disponible. Ningún instrumento tiene alta rentabilidad, riesgo nulo y liquidez total a la vez. Ahorro, inversión y previsión no son equivalentes: sirven para objetivos y plazos distintos.",
    ],
    vocab=[("interés", "pago adicional por usar dinero ajeno, o ganancia por prestar el propio"), ("riesgo", "posibilidad de perder dinero o de ganar menos de lo esperado"), ("liquidez", "facilidad para convertir un ahorro en dinero disponible"), ("rentabilidad", "ganancia que se espera obtener con un instrumento"), ("acción", "parte pequeña de una empresa que se compra y vende en la bolsa")],
    worked=[
        ("Calcular un interés simple", "Una persona de ejemplo deposita $100.000 en una libreta que paga 4 % de interés al año. ¿Cuánto interés gana en un año?",
         ["Calculo el 4 % de 100.000: 100.000 × 4 ÷ 100.", "El resultado es 4.000."], "$4.000 de interés"),
        ("Calcular el costo de un préstamo", "Un préstamo de ejemplo de $100.000 se paga en 4 cuotas de $27.000. ¿Cuánto interés se pagó en total?",
         ["Total pagado: 4 × 27.000 = 108.000.", "Interés: 108.000 - 100.000 = 8.000."], "$8.000 de interés"),
    ],
    mistakes=[
        ("Creer que invertir y ahorrar son lo mismo.", "Invertir acepta un riesgo mayor y puede hacer perder dinero; ahorrar busca guardar con riesgo bajo.", "Pregunta qué riesgo corre el dinero y para qué plazo se necesita."),
        ("Pensar que un instrumento puede ser muy rentable, muy seguro y muy líquido a la vez.", "Lo que rinde más suele tener más riesgo o menos liquidez.", "Compara rentabilidad, riesgo y liquidez antes de elegir."),
    ],
    T=[
        ("En Finanzas: ¿qué es el interés en un préstamo?", "El pago adicional que se cobra por usar dinero ajeno", "Es el costo de recibir el dinero hoy."),
        ("{F} ¿Qué instrumento sirve para guardar dinero con riesgo bajo y retirarlo casi de inmediato?", "La libreta de ahorro", "La ficha dice que se puede retirar casi de inmediato."),
        ("En Finanzas: ¿qué es la liquidez? A) la facilidad para convertir un ahorro en dinero disponible, B) la ganancia esperada de una inversión.", "A", "La liquidez mide qué tan rápido se dispone del dinero."),
        ("{F} ¿Cuál instrumento puede hacer perder dinero aunque la persona no se equivoque en nada? A) la acción, B) la libreta de ahorro.", "A", "Su valor sube y baja en la bolsa."),
        ("Una joven necesitará dinero en un mes para pagar una matrícula. ¿Qué le conviene más? A) comprar una acción, B) guardar en una libreta de ahorro.", "B", "Necesita liquidez y poco riesgo en un plazo corto."),
        ("{F} ¿Para qué sirve la previsión? A) para recibir una pensión en la vejez, B) para comprar un producto la semana siguiente.", "A", "Es un ahorro de largo plazo."),
        ("=", "Una persona de ejemplo deposita $200.000 en una libreta que paga 5 % de interés al año. ¿Cuánto interés gana en un año (en pesos)?", "200000*5//100", "Se calcula el 5 % de 200.000."),
        ("=", "Un préstamo de ejemplo de $300.000 se paga en 6 cuotas de $55.000. ¿Cuánto se paga en total (en pesos)?", "6*55000", "Se multiplica la cuota por el número de cuotas."),
        ("=", "Con el mismo préstamo de $300.000 pagado en 6 cuotas de $55.000, ¿cuánto interés se paga (en pesos)?", "6*55000-300000", "Se resta el monto recibido al total pagado."),
        ("{F} Una persona compra con tarjeta de crédito y paga solo una parte del saldo. ¿Por qué puede salirle más caro? A) porque se cobra interés sobre lo que queda sin pagar, B) porque el precio del producto cambia.", "A", "La ficha indica interés sobre el saldo no pagado."),
        ("María tiene $100.000 guardados para una emergencia. Un conocido le dice que compre acciones porque «seguro suben». ¿Qué respuesta es la más sólida? A) puede aceptar, porque las acciones siempre suben, B) debe rechazar, porque las acciones pueden perder valor y su dinero de emergencia necesita liquidez.", "B", "El riesgo y la liquidez importan para un dinero de emergencia."),
        ("=", "Una familia de ejemplo ahorra $15.000 al mes durante 12 meses y al final del año la libreta suma 2 % de interés sobre el total ahorrado. ¿Cuánto dinero tiene al final (en pesos)?", "15000*12+15000*12*2//100", "Se suma el total ahorrado y su interés del 2 %."),
        ("Se comparan dos préstamos de $300.000: el primero se paga en 6 cuotas de $55.000 y el segundo, en 3 cuotas de $108.000. ¿Cuál cuesta menos en total y por cuántos pesos?", "El segundo, por $6.000 menos", "El primero suma 330.000 y el segundo, 324.000."),
    ],
    ctx=("Un grupo de estudiantes de ejemplo junta $60.000 para un viaje de curso dentro de seis meses. Dudan entre guardarlos en una libreta de ahorro o comprar acciones de una empresa para «duplicarlos». ¿Qué opción corresponde a un objetivo de plazo corto y poco riesgo? A) la libreta de ahorro, B) las acciones.", "A", "Necesitan el dinero pronto y sin perderlo."),
    sc=[("En Finanzas: ¿qué diferencia hay entre ahorrar e invertir?", "Ahorrar busca guardar con riesgo bajo; invertir acepta un riesgo mayor para ganar más", "Los objetivos y el riesgo son distintos."),
        ("¿Qué es una caja vecina?", "Un punto de atención financiera instalado en un comercio de barrio", "Sirve donde no hay sucursales cerca."),
        ("¿Por qué ningún instrumento tiene a la vez alta rentabilidad, riesgo nulo y liquidez total?", "Porque lo que rinde más suele tener más riesgo o menos liquidez", "Hay que escoger qué se prioriza.")],
    op=("Beatriz (de ejemplo) tiene $80.000 y los necesitará en tres meses para comprar un uniforme deportivo. Dispone de una libreta de ahorro, una acción de una empresa y una tarjeta de crédito. Escribe qué instrumento elegirías para guardar su dinero, qué riesgo evitas al no elegir otro y por qué la previsión no es la opción para este objetivo.",
        "Elijo la libreta de ahorro, porque necesita el dinero pronto y con riesgo bajo. Evito el riesgo de perder valor que tiene la acción. La previsión no sirve porque es ahorro de largo plazo para la pensión, no para un plazo de tres meses.",
        ["elige la libreta con una razón", "nombra el riesgo que evita", "explica por qué la previsión no corresponde"], ["tres respuestas breves"], ["elegir la acción por su posible ganancia", "confundir previsión con ahorro de corto plazo"], "Explícale tu elección a una persona de tu casa y pídele que diga si el plazo de tres meses se tomó en cuenta."),
    reinforce="Haz una tarjeta con tres instrumentos y escribe, para cada uno, si su riesgo es bajo o alto.",
    extend="Explica por qué la liquidez importa más para un fondo de emergencia que para un ahorro de largo plazo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Oferta A (de ejemplo, ficha de una financiera ficticia): préstamo de $600.000 que se paga en 12 cuotas de $60.000. "
      "Oferta B (de ejemplo, ficha de otra financiera ficticia): préstamo de $600.000 que se paga en 6 cuotas de $112.000. "
      "Aviso C (de ejemplo, cartel publicitario): «¡Préstamo fácil! Cuotas desde $60.000. Sin papeleos.» El aviso no indica cuánto se paga en total.")
build(
    OA, 2, F2,
    use="Aprenderé a leer ofertas de crédito y a elegir qué dato mirar para compararlas. Sirve para no decidir solo por la cuota más baja ni por la publicidad.",
    prior=["Sé qué es el interés y cómo se calcula el total pagado en un préstamo.", "Sé distinguir un dato de una opinión.", "Sé multiplicar y restar cantidades de dinero."],
    explain=[
        "Una oferta de crédito entrega datos que se pueden comparar: el monto que se recibe, el plazo (número de cuotas), el valor de cada cuota y, lo más importante, el costo total, que es lo que realmente se paga sumando todas las cuotas. Para saber cuánto cuesta el crédito se resta el monto recibido al costo total: esa diferencia es el interés pagado.",
        "Una fuente informativa, como la ficha de una financiera, entrega esos datos. Una fuente publicitaria, como un cartel, busca vender y suele destacar lo más atractivo, por ejemplo una cuota baja, sin mostrar el total. Por eso se pregunta quién la escribió, con qué propósito y qué dato omite. La cuota más baja no significa el crédito más barato: con más cuotas cada una es menor, pero se paga más interés en total.",
        "Antes de decidir conviene también revisar el riesgo del que toma el crédito: si los ingresos bajan, ¿podrá pagar las cuotas? Elegir una fuente adecuada significa preferir la que entrega los datos completos y comprobables, y contrastarla con una segunda fuente cuando sea posible.",
    ],
    vocab=[("cuota", "pago periódico que se hace para devolver un crédito"), ("plazo", "tiempo o número de cuotas en que se devuelve un crédito"), ("costo total", "suma de todas las cuotas que se pagan por un crédito"), ("fuente publicitaria", "texto o aviso cuyo propósito principal es vender"), ("omitir", "dejar de mencionar un dato")],
    worked=[
        ("Calcular el costo total", "Una oferta de ejemplo de $400.000 se paga en 10 cuotas de $44.000. ¿Cuál es el costo total y cuánto es el interés?",
         ["Costo total: 10 × 44.000 = 440.000.", "Interés: 440.000 - 400.000 = 40.000."], "Costo total $440.000; interés $40.000"),
        ("Detectar lo que omite un aviso", "Un cartel de ejemplo dice: «Crédito rápido, cuota de solo $20.000». ¿Qué datos no entrega?",
         ["Un cartel destaca la cuota.", "No dice cuántas cuotas son ni cuánto se paga en total."], "El número de cuotas y el costo total"),
    ],
    mistakes=[
        ("Elegir la oferta con la cuota más baja.", "Si el plazo es más largo, se paga más interés en total.", "Calcula el costo total antes de comparar."),
        ("Creer lo que dice un aviso sin pedir el costo total.", "La publicidad destaca lo atractivo y puede omitir lo costoso.", "Pide la ficha informativa con el costo total."),
    ],
    T=[
        ("En Finanzas: ¿qué es el costo total de un crédito?", "La suma de todas las cuotas que se pagan", "Incluye el monto recibido más los intereses."),
        ("{F} ¿Cuántas cuotas tiene la oferta A?", "12", "La ficha dice 12 cuotas de $60.000."),
        ("{F} ¿Qué fuente tiene propósito de vender y no entrega el total? A) el aviso C, B) la oferta A.", "A", "Es un cartel publicitario que omite el total."),
        ("=", "{F} ¿Cuánto se paga en total en la oferta A (en pesos)?", "12*60000", "Se multiplica la cuota por las cuotas."),
        ("=", "{F} ¿Cuánto se paga en total en la oferta B (en pesos)?", "6*112000", "Se multiplica la cuota por las cuotas."),
        ("{F} ¿Qué oferta tiene la cuota más baja? A) la oferta A, B) la oferta B.", "A", "60.000 es menor que 112.000."),
        ("=", "{F} ¿Cuánto interés se paga en la oferta A (en pesos)?", "12*60000-600000", "Se resta el monto recibido al costo total."),
        ("=", "{F} ¿Cuánto interés se paga en la oferta B (en pesos)?", "6*112000-600000", "Se resta el monto recibido al costo total."),
        ("{F} ¿Qué oferta es más barata en total y por cuánto? Responde con una frase.", "La oferta B, por $48.000 menos", "El costo total de A es 720.000 y el de B, 672.000."),
        ("{F} Una persona dice: «La oferta A es mejor porque su cuota es menor». ¿Qué le responderías con las fuentes? Responde con una frase.", "Que la cuota menor se paga en más cuotas y el total resulta más caro", "La oferta A suma $48.000 más."),
        ("{F} Para comparar los dos créditos, ¿qué fuente conviene usar? A) las fichas A y B, que entregan monto, cuotas y plazo, B) el aviso C, que no indica el total.", "A", "Permiten calcular el costo total."),
        ("{F} Una familia gana $300.000 al mes y no puede pagar una cuota mayor a $75.000. ¿Qué oferta cumple ese límite? A) la oferta A, B) la oferta B.", "A", "La cuota de B supera el límite."),
        ("=", "{F} Si el aviso C ofreciera la cuota de $60.000 durante 15 cuotas por los mismos $600.000, ¿cuánto sería el costo total (en pesos)?", "15*60000", "Se multiplica la cuota por las cuotas."),
    ],
    ctx=("Un joven de ejemplo ve un cartel que dice «Préstamo fácil, cuotas desde $30.000» y quiere pedir $300.000. ¿Qué dato debe pedir primero para decidir? A) el número de cuotas y el costo total, B) si otras personas ya aceptaron la oferta.", "A", "Sin ellos no se puede calcular el interés."),
    sc=[("En Finanzas: ¿qué diferencia hay entre una ficha informativa y un aviso publicitario?", "La ficha entrega datos comparables; el aviso busca vender y puede omitir el total", "Tienen propósitos distintos."),
        ("¿Cómo se calcula el interés pagado en un crédito?", "Se resta el monto recibido al costo total", "El resultado es el costo del crédito."),
        ("¿Por qué la cuota más baja no siempre es la mejor oferta?", "Porque con más cuotas se paga más interés en total", "El costo total puede ser mayor.")],
    op=("Se te ofrecen estas dos opciones (de ejemplo): préstamo X de $200.000 en 8 cuotas de $28.000 y préstamo Y de $200.000 en 5 cuotas de $44.000. Calcula el costo total de cada uno, di cuál cuesta menos y qué otra información pedirías antes de firmar.",
        "X cuesta 8 × 28.000 = 224.000; Y cuesta 5 × 44.000 = 220.000. Y cuesta $4.000 menos. Antes de firmar pediría el detalle de otros cobros, como comisiones o seguros.",
        ["calcula los dos costos totales", "compara con una cifra", "nombra un dato adicional"], ["dos cálculos y una comparación"], ["elegir por la cuota más baja", "no calcular el costo total"], "Pide a una persona de tu casa que compruebe tus dos multiplicaciones."),
    reinforce="En una tarjeta escribe qué cuatro datos tiene toda oferta de crédito.",
    extend="Explica por qué un aviso publicitario puede ser verdadero y aun así dar una imagen incompleta.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Datos de ejemplo. Localidad rural ficticia «Valle Alto»: la sucursal bancaria más cercana está a 80 km y viajar a ella cuesta $6.000 ida y vuelta. "
      "Desde hace un año hay una caja vecina en el almacén del pueblo, donde se pueden depositar y retirar montos pequeños sin viajar. "
      "Antes, muchas familias guardaban el dinero en efectivo en la casa. Una libreta de ahorro paga 3 % de interés al año y la inflación del año fue de 4 %.")
build(
    OA, 3, F3,
    use="Aprenderé a ver qué cambió y qué se mantuvo en las formas de ahorrar y pedir crédito, y cómo el territorio influye en el acceso. Sirve para comprender por qué no todas las personas acceden igual a los servicios financieros.",
    prior=["Conozco libreta de ahorro, caja vecina, interés, riesgo y liquidez.", "Sé qué es la inflación.", "Sé calcular un porcentaje de una cantidad."],
    explain=[
        "Las formas de ahorrar y de endeudarse han cambiado. Antes, muchas familias guardaban el dinero en efectivo en la casa, lo que implica riesgo de pérdida o robo y no paga interés. Hoy existen libretas, cuentas y cajas vecinas que permiten depositar y retirar sin guardar billetes en el hogar. Lo que continúa es que cualquier instrumento mantiene alguna forma de riesgo o costo.",
        "El territorio influye en el acceso. En localidades rurales o alejadas puede no haber sucursales cercanas, y llegar hasta una cuesta tiempo y dinero. Las cajas vecinas acercan los servicios financieros, pero no resuelven todo: suelen permitir operaciones pequeñas. Por eso se dice que el acceso desigual es un desafío en regiones apartadas.",
        "Otro cambio es el efecto de la inflación sobre el ahorro. Si el interés que paga una libreta es menor que la inflación, el dinero ahorrado pierde poder de compra, es decir, alcanza para comprar menos cosas que antes. Para evaluar un ahorro se compara su interés con la inflación del mismo período.",
    ],
    vocab=[("acceso financiero", "posibilidad real de usar servicios como cuentas, ahorros y créditos"), ("sucursal", "oficina de una institución financiera donde se atiende a clientes"), ("inflación", "aumento general y sostenido de los precios"), ("poder de compra", "cantidad de bienes que se pueden comprar con una suma de dinero"), ("efectivo", "dinero en billetes y monedas")],
    worked=[
        ("Calcular un costo de acceso", "Un vecino de ejemplo viaja a una sucursal 5 veces al año y cada viaje cuesta $4.000. ¿Cuánto gasta al año en esos viajes?",
         ["Multiplico el costo por el número de viajes.", "5 × 4.000 = 20.000."], "$20.000 al año"),
        ("Comparar interés e inflación", "Un ahorro de ejemplo de $100.000 gana 2 % de interés, pero la inflación del año fue de 3 %. ¿Ganó o perdió poder de compra?",
         ["El interés es 2 % y la inflación, 3 %.", "Como 2 % es menor que 3 %, los precios subieron más que el ahorro."], "Perdió poder de compra"),
    ],
    mistakes=[
        ("Creer que todos tienen el mismo acceso a servicios financieros.", "Las distancias, el costo del traslado y la oferta local varían según el territorio.", "Pregunta dónde vive la persona y qué servicios tiene cerca."),
        ("Pensar que un ahorro que paga interés siempre gana poder de compra.", "Si la inflación es mayor que el interés, el poder de compra baja.", "Compara el interés con la inflación del mismo período."),
    ],
    T=[
        ("En Finanzas: ¿qué significa que el ahorro pierda poder de compra?", "Que con ese dinero se pueden comprar menos cosas que antes", "Ocurre cuando los precios suben más que el interés."),
        ("{F} ¿A cuántos kilómetros de Valle Alto queda la sucursal más cercana?", "80", "El dato aparece en la ficha."),
        ("{F} ¿Qué servicio acerca las operaciones pequeñas al pueblo sin viajar? A) la caja vecina, B) la acción.", "A", "Está en el almacén del pueblo."),
        ("=", "{F} Si una familia de Valle Alto viaja 12 veces al año a la sucursal, ¿cuánto gasta en viajes (en pesos)?", "12*6000", "Se multiplica el costo de un viaje por 12."),
        ("=", "{F} Si una familia ahorra $200.000 en una libreta, ¿cuánto interés gana en un año (en pesos)?", "200000*3//100", "Se calcula el 3 % de 200.000."),
        ("{F} ¿Qué rasgo del ahorro cambió respecto de antes? A) ahora se puede ahorrar sin guardar billetes en casa, B) el ahorro ya no tiene ningún riesgo.", "A", "Las cajas vecinas y libretas son una opción nueva."),
        ("=", "{F} Con una inflación de 4 % sobre $200.000, ¿cuánto dinero adicional se necesitaría para comprar lo mismo (en pesos)?", "200000*4//100", "Se calcula el 4 % de 200.000."),
        ("=", "{F} Con $200.000 ahorrados, ¿cuánto menos gana el interés que lo necesario para igualar la inflación (en pesos)?", "200000*4//100-200000*3//100", "Se resta el interés al aumento de precios."),
        ("{F} Con los datos de interés e inflación, ¿el ahorro en la libreta gana o pierde poder de compra? A) gana, B) pierde.", "B", "El interés es 3 % y la inflación, 4 %."),
        ("{F} Una vecina dice: «Guardar billetes en casa siempre es mejor porque no pago nada». ¿Qué desventaja ignora? A) el riesgo de pérdida y que el efectivo no gana interés, B) que los billetes son de papel.", "A", "El efectivo no rinde y puede perderse."),
        ("{F} ¿Qué cambio y qué continuidad hay entre el ahorro de antes y el actual? Responde con una frase.", "Cambió que hay cajas vecinas y libretas; continúa que todo ahorro tiene algún riesgo o costo", "Se separan una novedad y un rasgo estable."),
        ("Una localidad de ejemplo no tiene sucursal ni caja vecina a menos de 100 km. ¿Qué problema de acceso enfrentan sus familias? A) traslados largos y costosos para hacer operaciones, B) falta de interés de las personas por ahorrar.", "A", "La distancia limita el acceso."),
        ("=", "{F} Si el viaje a la sucursal se hiciera 12 veces al año y la caja vecina lo evitara por completo, ¿cuánto se ahorra por viajes en 3 años (en pesos)?", "12*6000*3", "Se multiplica el gasto anual por los tres años."),
    ],
    ctx=("Una comuna rural de ejemplo estudia instalar una caja vecina. Los datos: sin ella, cada familia gasta $24.000 al año en viajes. Con ella, gasta $0. Para 150 familias, ¿cuánto dinero ahorrarían entre todas al año (en pesos)? A) $3.600.000, B) $360.000.", "A", "24.000 por 150 familias da 3.600.000."),
    sc=[("En Finanzas: ¿qué es el acceso financiero?", "La posibilidad real de usar servicios como cuentas, ahorros y créditos", "Depende también de la distancia."),
        ("¿Cuándo un ahorro pierde poder de compra?", "Cuando el interés que paga es menor que la inflación", "Los precios suben más que el ahorro."),
        ("¿Qué riesgo tiene guardar dinero en efectivo en casa?", "Perderlo o que se lo roben, y que no gana interés", "No paga interés y puede perderse.")],
    op=("{F} Escribe un párrafo con: un cambio y una continuidad en la forma de ahorrar en Valle Alto, un problema de acceso por el territorio y el resultado de comparar el interés de la libreta con la inflación (con cifras).",
        "Cambió que ahora hay una caja vecina; continúa que todo ahorro tiene algún riesgo. La sucursal está a 80 km, lo que encarece los trámites. El interés es 3 % y la inflación 4 %, así que el ahorro pierde poder de compra.",
        ["nombra un cambio y una continuidad", "explica un problema territorial", "compara interés e inflación con cifras"], ["un párrafo con tres cifras"], ["decir que el ahorro gana poder de compra", "no mencionar el territorio"], "Léele tu párrafo a una persona de tu casa y pídele que marque las cifras que usaste."),
    reinforce="Anota dos formas de guardar dinero que existan en tu barrio y un riesgo de cada una.",
    extend="Explica por qué una caja vecina puede aumentar el acceso, pero no reemplaza a una sucursal completa.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Caso de ejemplo: Sofía, adulta ficticia, tiene una tarjeta de crédito con un saldo de $100.000 sin pagar; la entidad le cobra 3 % de interés mensual sobre ese saldo. "
      "Voz del banco (de ejemplo): «Cobramos interés porque prestamos dinero y corremos el riesgo de no recibirlo.» "
      "Voz de Sofía (de ejemplo): «Usé la tarjeta por una emergencia médica de la familia.» "
      "Voz de la autoridad financiera (de ejemplo): «Exigimos que los costos se informen de manera clara.» "
      "Voz de una tienda (de ejemplo): «Ofrecemos cuotas para vender más.»")
build(
    OA, 4, F4,
    use="Aprenderé a comparar cómo ven el crédito quienes lo ofrecen, quienes lo usan y quienes lo regulan, y a identificar varias causas del sobreendeudamiento. Sirve para evaluar el riesgo sin culpar a una sola persona.",
    prior=["Conozco interés, cuota, costo total y riesgo.", "Sé que cada agente económico tiene una perspectiva.", "Sé calcular un porcentaje de una cantidad."],
    explain=[
        "En el crédito participan varios actores con intereses distintos. Las entidades financieras prestan dinero y cobran interés a cambio; asumen el riesgo de que el cliente no pague. Las personas usan el crédito para cubrir una necesidad o hacer una compra, y asumen el riesgo de endeudarse más de lo que pueden pagar. Las tiendas ofrecen cuotas para vender más. El Estado regula, a través de una autoridad financiera, para que los costos se informen con claridad y se protejan los derechos.",
        "El sobreendeudamiento, que es tener deudas más altas de lo que los ingresos permiten pagar, rara vez tiene una sola causa. Puede deberse a una emergencia, a ingresos bajos o inestables, a ofertas que destacan la cuota y ocultan el total, y a decisiones de compra poco planificadas. Hablamos de multicausalidad: varias causas actúan a la vez, por lo que no basta con decir «es culpa del cliente» o «es culpa del banco».",
        "El interés mensual sobre un saldo impago puede calcularse con un porcentaje. Si la deuda no se paga, el costo crece mes a mes. Para evaluar el riesgo del crédito conviene preguntar quién gana, quién arriesga más, qué información faltó y qué alternativas existían, como pagar el total, negociar un plazo o pedir ayuda antes de que la deuda crezca.",
    ],
    vocab=[("sobreendeudamiento", "situación en que las deudas superan lo que los ingresos permiten pagar"), ("entidad financiera", "institución que presta dinero y recibe ahorros, como un banco"), ("regular", "fijar reglas para que una actividad se haga de manera justa"), ("multicausalidad", "situación en que un hecho tiene varias causas a la vez"), ("saldo", "parte de una deuda que todavía no se ha pagado")],
    worked=[
        ("Calcular el interés de un mes", "Una persona de ejemplo debe un saldo de $200.000 y se cobra 2 % mensual. ¿Cuánto interés se cobra ese mes?",
         ["Calculo 200.000 × 2 ÷ 100.", "El resultado es 4.000."], "$4.000 de interés en el mes"),
        ("Asociar una voz con su actor", "Una tienda de ejemplo dice: «Ofrecemos cuotas para que más gente pueda comprar». ¿Qué interés tiene?",
         ["Una tienda vende bienes.", "Al ofrecer cuotas busca aumentar sus ventas."], "Vender más"),
    ],
    mistakes=[
        ("Atribuir el sobreendeudamiento solo a la irresponsabilidad del cliente.", "Pueden influir emergencias, ingresos inestables y ofertas poco claras.", "Revisa varias causas antes de culpar a un actor."),
        ("Pensar que la entidad financiera no corre ningún riesgo.", "Presta dinero y puede no recuperarlo.", "Reconoce el riesgo de cada actor."),
    ],
    T=[
        ("En Finanzas: ¿qué es el sobreendeudamiento?", "Tener deudas más altas de lo que los ingresos permiten pagar", "Es un riesgo del crédito."),
        ("{F} ¿Qué actor dice que exige que los costos se informen con claridad?", "La autoridad financiera", "Su función es regular."),
        ("{F} ¿Qué actor dice «ofrecemos cuotas para vender más»? A) la tienda, B) Sofía.", "A", "Una tienda busca aumentar sus ventas."),
        ("=", "{F} ¿Cuánto interés se le cobra a Sofía en un mes (en pesos)?", "100000*3//100", "Se calcula el 3 % de 100.000."),
        ("=", "{F} Si no pagara nada y el interés se calculara cada mes solo sobre los $100.000 originales, ¿cuánto interés se acumularía en 4 meses (en pesos)?", "4*(100000*3//100)", "Se multiplica el interés mensual por 4."),
        ("{F} ¿Qué riesgo menciona el banco? A) que el cliente no le devuelva el dinero, B) que Sofía use la tarjeta en una emergencia.", "A", "El banco dice que corre el riesgo de no recibirlo."),
        ("{F} ¿Qué causa del endeudamiento aparece en la voz de Sofía? A) una emergencia médica, B) una compra por impulso.", "A", "Ella lo explica así."),
        ("=", "{F} Si Sofía pagara $25.000 del saldo, ¿cuánto saldo le quedaría (en pesos)?", "100000-25000", "Se resta el pago al saldo."),
        ("=", "{F} Si Sofía paga $25.000 y le quedan $75.000 de saldo, ¿cuánto interés se le cobraría el mes siguiente con el 3 % de la ficha (en pesos)?", "75000*3//100", "Se calcula el 3 % del saldo que queda."),
        ("{F} Un comentarista dice: «Si Sofía tiene deudas, es solo por su culpa». Usando las voces, ¿qué dos elementos contradicen la idea? Responde con una frase.", "Que hubo una emergencia médica y que las tiendas ofrecen cuotas para vender más, es decir, hay más de una causa", "Aparecen causas fuera de la voluntad del cliente."),
        ("{F} ¿Qué medida de la autoridad financiera ayudaría más a prevenir el sobreendeudamiento? A) exigir que los avisos informen el costo total, B) prohibir las cuotas por completo.", "A", "Informa mejor y no elimina el crédito útil."),
        ("{F} Sofía puede elegir entre pagar el total del saldo hoy o pagar un mínimo. ¿Qué opción evita pagar más interés? A) pagar el total, B) pagar el mínimo.", "A", "Sin saldo no hay interés."),
        ("Un joven de ejemplo se endeudó para comprar un celular nuevo sin necesitarlo, y su ingreso es de $250.000 al mes con una cuota de $90.000. ¿Qué porcentaje de su ingreso usa en la cuota? A) 36 %, B) 9 %.", "A", "90.000 dividido en 250.000 es 0,36."),
    ],
    ctx=("Una familia de ejemplo gana $500.000 al mes y las cuotas de este mes de tres tiendas son $200.000, $150.000 y $180.000. ¿Cuánto más que su ingreso suman esas cuotas (en pesos)? A) $30.000, B) $0.", "A", "Las cuotas suman 530.000 y el ingreso es 500.000."),
    sc=[("En Finanzas: ¿qué significa multicausalidad?", "Que un hecho tiene varias causas a la vez", "El sobreendeudamiento rara vez tiene una sola causa."),
        ("¿Cuál es el interés de la entidad financiera en un crédito?", "Cobrar interés a cambio de prestar dinero", "Esa es su ganancia."),
        ("¿Qué hace una autoridad financiera?", "Regula para que los costos se informen con claridad", "Protege a los usuarios.")],
    op=("{F} Elige dos voces y escribe: qué actor habla, qué interés tiene y qué riesgo corre. Después, nombra dos causas distintas que expliquen el sobreendeudamiento de Sofía y una medida para evitar un caso similar.",
        "El banco: busca ganancia con el interés y corre el riesgo de no recibir el pago. Sofía: busca resolver una emergencia y corre el riesgo de endeudarse. Causas: emergencia médica e información insuficiente sobre el costo. Medida: avisos con costo total.",
        ["identifica actor, interés y riesgo de dos voces", "nombra dos causas", "propone una medida"], ["dos voces, dos causas y una medida"], ["culpar a un solo actor", "no mencionar ninguna medida"], "Pide a una persona de tu casa que diga cuál de tus dos causas le parece más importante."),
    reinforce="Escribe tres preguntas que harías antes de aceptar un crédito.",
    extend="Explica por qué una emergencia no siempre se puede prever y cómo un ahorro de emergencia ayuda.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Dossier de ejemplo, «¿Cómo comprar una lavadora de $240.000?» "
      "Opción 1: ahorrar $20.000 al mes durante 12 meses y comprarla al contado; la lavadora actual se dañó y mientras tanto se lava a mano. "
      "Opción 2: comprarla hoy con crédito, en 12 cuotas de $25.000. "
      "Dato 3: el ingreso mensual de la familia es de $600.000. "
      "Dato 4: la familia ya paga cuotas de otras deudas por $100.000 al mes. "
      "Guía de ejemplo: conviene que todas las cuotas juntas no pasen de un cuarto del ingreso.")
build(
    OA, 5, F5,
    use="Aprenderé a defender una decisión financiera con cálculos, riesgos y beneficios, y a reconocer los límites de los datos. Sirve para tomar decisiones de ahorro y crédito de forma informada.",
    prior=["Sé calcular costo total e interés de un crédito.", "Conozco liquidez, riesgo y rentabilidad.", "Sé que un buen argumento tiene tesis, evidencia, objeción y límite."],
    explain=[
        "Una decisión financiera se argumenta comparando beneficios y riesgos. Al ahorrar para comprar al contado se evita pagar interés, pero hay que esperar; al comprar con crédito se obtiene el bien antes, pero se paga más en total y se compromete parte del ingreso. No hay una opción correcta para todos: depende del ingreso, de las deudas, de la urgencia y del riesgo que la familia pueda soportar.",
        "Para evaluar el esfuerzo del crédito se calcula la proporción del ingreso que se destina a cuotas. Una guía de ejemplo (inventada para este ejercicio) sugiere que las cuotas juntas no superen cerca de un cuarto del ingreso, aunque esa cifra es una orientación, no una ley. Si las cuotas pasan ese nivel, el riesgo de no poder pagar aumenta.",
        "Un argumento sólido presenta una tesis, usa cifras del dossier, reconoce una objeción (por ejemplo, la urgencia de tener la lavadora) y la responde con alternativas. También declara su límite: los datos no dicen si el ingreso de la familia puede bajar ni cuánto cuestan otros gastos imprevistos. Una conclusión proporcional afirma solo lo que los datos permiten afirmar.",
    ],
    vocab=[("contado", "pago completo de una compra en el momento"), ("guía de ejemplo", "orientación práctica que no es una ley"), ("compromiso financiero", "pago futuro al que una persona se obliga, como una cuota"), ("tesis", "afirmación que se defiende en un argumento"), ("objeción", "razón que va en contra de una tesis")],
    worked=[
        ("Calcular qué parte del ingreso va a cuotas", "Una familia de ejemplo gana $400.000 y paga cuotas por $80.000 al mes. ¿Qué porcentaje del ingreso son las cuotas?",
         ["Divido 80.000 por 400.000.", "80.000 ÷ 400.000 × 100 = 20."], "20 % del ingreso"),
        ("Comparar contado y crédito", "Un televisor de ejemplo cuesta $300.000 al contado, o 10 cuotas de $33.000. ¿Cuánto más cuesta a crédito?",
         ["Total a crédito: 10 × 33.000 = 330.000.", "Diferencia: 330.000 - 300.000 = 30.000."], "$30.000 más"),
    ],
    mistakes=[
        ("Decidir solo por la urgencia de tener el bien.", "Ignora el costo total y la capacidad real de pago.", "Calcula el costo y la parte del ingreso comprometida."),
        ("Citar la guía de ejemplo como si fuera una ley.", "Es una orientación; cada familia debe mirar su situación.", "Úsala como referencia y explica sus límites."),
    ],
    T=[
        ("En Finanzas: ¿qué significa comprar al contado?", "Pagar la compra completa en el momento", "No se pagan cuotas ni intereses."),
        ("{F} ¿Cuánto cuesta la lavadora al contado?", "$240.000", "El dossier lo informa."),
        ("{F} ¿Cuántos meses hay que ahorrar en la opción 1? A) 12 meses, B) 6 meses.", "A", "La opción 1 dice 12 meses."),
        ("=", "{F} ¿Cuánto se ahorra en total en la opción 1 (en pesos)?", "12*20000", "Se multiplica el ahorro mensual por los meses."),
        ("=", "{F} ¿Cuánto se paga en total en la opción 2 (en pesos)?", "12*25000", "Se multiplica la cuota por las cuotas."),
        ("=", "{F} ¿Cuánto más cuesta la lavadora con el crédito que al contado (en pesos)?", "12*25000-240000", "Se resta el precio al contado al total del crédito."),
        ("=", "{F} Si la familia aceptara la opción 2, ¿cuánto pagaría en cuotas cada mes en total, sumando sus cuotas actuales (en pesos)?", "100000+25000", "Se suma la nueva cuota a las cuotas actuales."),
        ("=", "{F} Según la guía, el límite de cuotas es un cuarto del ingreso. ¿Cuánto es ese límite (en pesos)?", "600000//4", "Un cuarto de 600.000 es 150.000."),
        ("=", "{F} Con la opción 2, ¿cuánto margen queda bajo el límite de la guía (en pesos)?", "600000//4-(100000+25000)", "Se resta el total de cuotas al límite de un cuarto del ingreso."),
        ("{F} ¿La opción 2 respeta la guía de ejemplo? A) sí, porque 125.000 no supera 150.000, B) no, porque supera 150.000.", "A", "Las cuotas quedarían bajo el límite."),
        ("{F} Una objeción a la opción 1 es que la familia lava a mano mientras tanto. ¿Qué respuesta la atiende? A) ahorrar un monto mayor al mes para acortar el tiempo si es posible, B) ignorar la objeción.", "A", "Reconoce el problema y propone una alternativa."),
        ("{F} Un compañero concluye: «La opción 2 es mejor porque tenemos la lavadora ya». ¿Qué cifra del dossier muestra el costo de esa ventaja? A) $60.000 más que al contado, B) $20.000 de ahorro al mes.", "A", "El crédito suma 300.000 y el contado cuesta 240.000."),
        ("=", "{F} Si la familia pudiera ahorrar $30.000 al mes, ¿en cuántos meses reuniría el precio al contado?", "240000//30000", "Se divide el precio por el ahorro mensual."),
    ],
    ctx=("Un joven de ejemplo gana $300.000 al mes y ya paga cuotas por $60.000. Quiere comprar un celular con una cuota de $40.000. Si el límite de ejemplo es un cuarto del ingreso, ¿le conviene? A) no, porque sus cuotas pasarían a $100.000 y el límite es $75.000, B) sí, porque el celular es nuevo.", "A", "Un cuarto de 300.000 es 75.000."),
    sc=[("En Finanzas: ¿qué parte de un argumento es una objeción?", "Una razón que va en contra de la tesis", "Debe reconocerse y responderse."),
        ("¿Por qué una guía de ejemplo no es una ley?", "Porque es una orientación y cada familia debe evaluar su situación", "No obliga, orienta."),
        ("¿Qué compara una persona que decide entre contado y crédito?", "El costo total, el tiempo de espera y el peso de las cuotas en el ingreso", "Son los elementos que cambian entre las opciones.")],
    op=("{F} Escribe un argumento de cinco a siete líneas que diga qué opción recomiendas a la familia. Incluye tu tesis, dos cifras del dossier, una objeción con su respuesta y un límite.",
        "Tesis: recomiendo ahorrar (opción 1). El crédito cuesta $60.000 más. Objeción: no tienen lavadora; se responde con ahorrar más cada mes. Límite: no sabemos si el ingreso podría bajar durante el año.",
        ["declara una tesis", "usa dos cifras", "responde una objeción", "indica un límite"], ["un argumento de cinco a siete líneas"], ["no usar cifras", "afirmar que una opción es mejor para todos"], "Léele tu argumento a una persona de tu casa y pídele que identifique tu objeción."),
    reinforce="Escribe una tesis sobre cómo pagar un objeto de $100.000 y una cifra que la respalde.",
    extend="Explica por qué la urgencia puede cambiar la conclusión sobre contado o crédito.",
    materials=MAT,
)

# ================================================================ OA 22
OA = "HI1M OA 22"

# ---------------------------------------------------------------- Clase 1
F6 = ("Presupuesto mensual de ejemplo de una familia: ingresos, $800.000. "
      "Gastos: arriendo, $300.000; alimentación, $250.000; transporte, $80.000; cuentas básicas, $70.000; cuota de una deuda, $60.000.")
build(
    OA, 1, F6,
    use="Aprenderé a planificar el consumo con un presupuesto y a conocer los derechos básicos de un consumidor. Sirve para comprar con información y sin comprometer el ingreso.",
    prior=["Conozco escasez, necesidad básica y costo de oportunidad.", "Sé qué son una cuota y un interés.", "Sé sumar y restar cantidades de dinero."],
    explain=[
        "Consumir es usar bienes y servicios para satisfacer necesidades. El consumo informado es el que se hace conociendo precio, características, condiciones y alternativas del producto; el consumo responsable considera además si el gasto cabe en el presupuesto y qué efectos tiene en otras personas y en el ambiente. Un presupuesto es el plan que compara los ingresos con los gastos de un período, por ejemplo un mes.",
        "En Chile existe una ley que protege los derechos de los consumidores y un organismo del Estado, el Servicio Nacional del Consumidor, que informa y recibe reclamos. Entre los derechos básicos están recibir información veraz y oportuna, elegir libremente, no ser discriminado, tener seguridad al consumir y ser compensado si un producto o servicio causa un daño o viene defectuoso. Los derechos conviven con deberes, como informarse y guardar la boleta.",
        "Endeudarse es asumir una deuda que se debe pagar con ingresos futuros. Puede ser útil si permite una compra importante y las cuotas son manejables, pero es riesgoso si los compromisos financieros, es decir, los pagos que ya se deben, son demasiado altos. Para evitarlo se compara el ingreso con los gastos, se reserva dinero para ahorrar y se revisa cuánto pesan las cuotas.",
    ],
    vocab=[("presupuesto", "plan que compara los ingresos con los gastos de un período"), ("consumo informado", "consumo que se hace conociendo precio, características y condiciones del producto"), ("derechos del consumidor", "protecciones que la ley da a quien compra bienes o servicios"), ("boleta", "comprobante que prueba una compra"), ("compromiso financiero", "pago futuro al que una persona ya se obligó")],
    worked=[
        ("Calcular el saldo de un presupuesto", "Una familia de ejemplo tiene ingresos de $500.000 y gastos de $430.000. ¿Cuánto le sobra al mes?",
         ["Resto los gastos a los ingresos.", "500.000 - 430.000 = 70.000."], "Le sobran $70.000"),
        ("Identificar un derecho", "Un local de ejemplo vende un jugo con un ingrediente que no indica en la etiqueta. ¿Qué derecho se afecta?",
         ["El consumidor debe poder conocer lo que consume.", "Eso corresponde a la información veraz y oportuna."], "El derecho a información veraz y oportuna"),
    ],
    mistakes=[
        ("Creer que el presupuesto solo sirve para quienes ganan poco.", "Toda familia necesita planificar, porque los recursos son limitados.", "Haz un presupuesto con ingresos y gastos."),
        ("Pensar que, si se firmó algo, ya no hay derechos.", "Los derechos del consumidor siguen vigentes aunque se firme un contrato.", "Revisa la información recibida y reclama si no fue clara."),
    ],
    T=[
        ("En Economía: ¿qué es un presupuesto?", "Un plan que compara los ingresos con los gastos de un período", "Permite ordenar el dinero."),
        ("=", "{F} ¿Cuánto suman los gastos del presupuesto (en pesos)?", "300000+250000+80000+70000+60000", "Se suman los cinco gastos."),
        ("En Economía: ¿qué es una boleta? A) un comprobante de una compra, B) un crédito.", "A", "Prueba que una compra se realizó."),
        ("=", "{F} ¿Cuánto dinero le sobra a la familia al mes (en pesos)?", "800000-(300000+250000+80000+70000+60000)", "Se resta el total de gastos a los ingresos."),
        ("{F} ¿Qué gasto del presupuesto es un compromiso financiero? A) la cuota de una deuda, B) la alimentación.", "A", "Es un pago que ya se debe."),
        ("Un producto de ejemplo no indica su fecha de vencimiento. ¿Qué derecho se afecta? A) el derecho a información veraz y oportuna, B) el derecho a la libre elección.", "A", "Falta información necesaria para consumir con seguridad."),
        ("=", "{F} ¿Cuántos pesos más gasta la familia en arriendo que en alimentación?", "300000-250000", "Se resta el gasto menor al mayor."),
        ("=", "{F} Una guía de ejemplo dice que las cuotas no pasen de un cuarto del ingreso. ¿Cuánto es ese límite (en pesos)?", "800000//4", "Se divide el ingreso por 4."),
        ("{F} La cuota de la deuda es de $60.000. ¿Respeta la guía del cuarto del ingreso? A) sí, porque 60.000 es menor que el límite, B) no, porque lo supera.", "A", "El límite es 200.000."),
        ("Una joven compra un electrodoméstico y le entregan una boleta. Después descubre que está defectuoso. ¿Para qué le sirve la boleta? A) para probar la compra al reclamar, B) para reducir el precio automáticamente.", "A", "Es el comprobante de la compra."),
        ("{F} La familia quiere comprar un artículo de $50.000 en un mes. ¿Le alcanza con lo que le sobra? A) no, porque sobran $40.000, B) sí, porque sobran $100.000.", "A", "800.000 menos 760.000 son 40.000."),
        ("Un consumidor dice: «Como firmé el contrato, ya no tengo derechos». ¿Qué respuesta corresponde? A) los derechos continúan aunque haya contrato, B) los derechos se pierden al firmar.", "A", "La ley los protege aunque se firme."),
        ("=", "{F} Si la familia ahorrara la mitad de lo que le sobra cada mes durante 6 meses, ¿cuánto juntaría (en pesos)?", "(800000-760000)//2*6", "Se calcula la mitad del saldo y se multiplica por 6."),
    ],
    ctx=("Una estudiante de ejemplo recibe $30.000 de mesada y anota: transporte $12.000, colación $10.000 y fotocopias $4.000. Quiere comprar un libro de $9.000. ¿Le alcanza? A) no, porque le sobran $4.000, B) sí, porque le sobran $14.000.", "A", "30.000 menos 26.000 son 4.000."),
    sc=[("En Economía: ¿qué es el consumo informado?", "El que se hace conociendo precio, características y condiciones del producto", "Evita decidir sin información."),
        ("Nombra un derecho básico del consumidor.", "Por ejemplo: recibir información veraz y oportuna", "Está entre los derechos básicos de la clase."),
        ("¿Para qué sirve guardar la boleta?", "Para probar la compra si hay que reclamar", "Es el comprobante.")],
    op=("Un estudiante de ejemplo tiene ingresos de $400.000 al mes y gastos de arriendo $180.000, alimentación $120.000 y transporte $40.000. Quiere comprar unos audífonos de $70.000 en una cuota única. Escribe cuánto le sobra, si le alcanza, y qué derecho exigirías si los audífonos vinieran defectuosos.",
        "Le sobran $60.000 (400.000 - 340.000). No le alcanza para $70.000. Si vinieran defectuosos, exigiría ser compensado, reparación o cambio, y mostraría la boleta.",
        ["calcula el saldo", "decide si alcanza", "nombra un derecho"], ["tres respuestas breves"], ["no restar todos los gastos", "no mencionar ningún derecho"], "Comprueba tu resta con una persona de tu casa."),
    reinforce="Haz un mini presupuesto de una semana con tu mesada o con una cantidad de ejemplo.",
    extend="Explica por qué ahorrar una parte del ingreso ayuda a evitar endeudarse.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F7 = ("Aviso A (de ejemplo, publicidad en una vitrina): «Notebook en 12 cuotas de $45.000. ¡Cuotas bajas!» "
      "Ficha B (de ejemplo, letra chica del contrato): precio al contado, $450.000; compra a crédito, 12 cuotas de $45.000. "
      "Boleta C (de ejemplo): compra al contado de un cargador, $12.000; garantía de ejemplo de 3 meses.")
build(
    OA, 2, F7,
    use="Aprenderé a leer publicidad, contratos y boletas para decidir una compra con información. Sirve para reconocer qué dato falta y qué documento sirve para reclamar.",
    prior=["Conozco costo total, interés, boleta y derechos del consumidor.", "Sé distinguir una fuente informativa de una publicitaria.", "Sé multiplicar y restar dinero."],
    explain=[
        "Al comprar aparecen tres tipos de documentos. La publicidad busca atraer y destaca lo más atractivo; no siempre muestra todo. El contrato o la ficha de condiciones contiene las reglas de la compra, como el precio, el plazo, las cuotas y las obligaciones de cada parte; muchas veces los datos importantes aparecen en letra pequeña. La boleta es el comprobante que prueba la compra y permite reclamar o hacer valer una garantía.",
        "La ley exige que el proveedor informe de manera veraz y oportuna el precio y las condiciones. Si una publicidad solo muestra la cuota, el consumidor debe pedir el precio total. Comparar el precio al contado con el total a crédito permite calcular cuánto cuesta financiar la compra. La garantía es el compromiso del proveedor de reparar, cambiar o devolver el dinero si el producto falla dentro de un plazo.",
        "Seleccionar la fuente adecuada es parte del consumo informado. Para saber cuánto pagaré, uso el contrato; para saber qué me ofrecen, miro la publicidad pero la contrasto con el contrato; para reclamar, necesito la boleta. Ninguna fuente basta sola: el contraste entre ellas revela diferencias.",
    ],
    vocab=[("contrato", "acuerdo escrito con las reglas de una compra o servicio"), ("letra pequeña", "parte de un documento con condiciones importantes escritas en tamaño reducido"), ("garantía", "compromiso de reparar, cambiar o devolver el dinero si el producto falla en un plazo"), ("proveedor", "persona o empresa que vende bienes o servicios"), ("financiar", "pagar una compra en cuotas con interés")],
    worked=[
        ("Calcular lo que cuesta financiar", "Un celular de ejemplo cuesta $200.000 al contado o 10 cuotas de $22.000. ¿Cuánto cuesta financiarlo?",
         ["Total a crédito: 10 × 22.000 = 220.000.", "Diferencia: 220.000 - 200.000 = 20.000."], "$20.000 más"),
        ("Elegir el documento para reclamar", "Un par de zapatillas de ejemplo se rompe a la semana. ¿Qué documento ayuda a probar la compra?",
         ["Se necesita un comprobante de que se compró.", "Ese comprobante es la boleta."], "La boleta"),
    ],
    mistakes=[
        ("Fiarse solo de lo que dice la publicidad.", "Puede destacar la cuota y omitir el total.", "Contrasta la publicidad con el contrato."),
        ("No guardar la boleta.", "Sin comprobante es más difícil hacer valer la garantía.", "Guarda boletas y contratos."),
    ],
    T=[
        ("En Economía: ¿qué es una garantía?", "El compromiso de reparar, cambiar o devolver el dinero si el producto falla en un plazo", "Protege al comprador."),
        ("{F} ¿Cuál es el precio al contado del notebook?", "$450.000", "La ficha B lo informa."),
        ("{F} ¿Qué documento prueba la compra del cargador? A) la boleta C, B) el aviso A.", "A", "Es el comprobante."),
        ("=", "{F} ¿Cuánto se paga en total si el notebook se compra a crédito (en pesos)?", "12*45000", "Se multiplica la cuota por las cuotas."),
        ("=", "{F} ¿Cuánto más cuesta el notebook a crédito que al contado (en pesos)?", "12*45000-450000", "Se resta el precio al contado al total a crédito."),
        ("{F} ¿Qué documento destaca la cuota y no indica el total? A) el aviso A, B) la ficha B.", "A", "Es un aviso publicitario."),
        ("=", "{F} ¿Qué porcentaje del precio al contado representa el costo extra del crédito?", "(12*45000-450000)*100//450000", "Se divide el costo extra por el precio al contado y se multiplica por 100.", "%"),
        ("{F} El aviso A dice «cuotas bajas». ¿Qué dato de la ficha B permite evaluar esa afirmación? A) el total a crédito, B) el precio del cargador de la boleta C.", "A", "Se compara con el contado."),
        ("{F} Si el cargador de la boleta C falla a los 2 meses, ¿qué puede hacer el comprador? A) usar la garantía de 3 meses con la boleta, B) no hacer nada.", "A", "Está dentro del plazo."),
        ("{F} ¿Qué diferencia hay entre el aviso A y la ficha B? Responde con una frase.", "El aviso busca vender y destaca la cuota; la ficha entrega precios y condiciones comparables", "Sus propósitos son distintos."),
        ("{F} Un comprador dice: «Con la boleta C puedo probar mi compra del notebook». ¿Es correcto? A) no, porque la boleta C es del cargador, B) sí, porque es una boleta.", "A", "Cada boleta prueba su compra."),
        ("=", "{F} Si la boleta C hubiera sido por 3 cargadores iguales, ¿cuánto habría costado (en pesos)?", "3*12000", "Se multiplica el precio por 3."),
        ("{F} Si el comprador desea evitar el costo extra, ¿qué opción tiene? A) ahorrar y comprar al contado, B) elegir más cuotas.", "A", "Se evita pagar el recargo del crédito."),
    ],
    ctx=("Una familia de ejemplo ve un aviso que dice «Refrigerador en 6 cuotas de $80.000» y en la ficha ve que al contado cuesta $450.000. ¿Cuánto más cuesta a crédito (en pesos)? A) $30.000, B) $0.", "A", "6 por 80.000 son 480.000; la diferencia con 450.000 es 30.000."),
    sc=[("En Economía: ¿para qué sirve la letra pequeña de un contrato?", "Para informar condiciones importantes que el comprador debe leer", "No se debe ignorar."),
        ("¿Qué documento permite reclamar una garantía?", "La boleta", "Prueba la compra."),
        ("¿Cómo se calcula cuánto cuesta financiar una compra?", "Restando el precio al contado al total a crédito", "La diferencia es el costo extra.")],
    op=("{F} Elige dos documentos y escribe para cada uno su tipo, su propósito y un dato que entrega o que omite. Calcula también cuánto más cuesta el notebook a crédito y escribe una pregunta que le harías al vendedor.",
        "Aviso A: publicidad; busca vender; omite el total. Ficha B: contrato; informa precios; entrega el contado y las cuotas. El crédito cuesta $90.000 más. Pregunta: ¿cuánto del total corresponde a intereses?",
        ["clasifica dos documentos", "calcula el costo extra", "formula una pregunta"], ["dos documentos, un cálculo y una pregunta"], ["tomar la publicidad como contrato", "no calcular el costo extra"], "Pide a una persona de tu casa que compruebe tu cálculo."),
    reinforce="Mira una boleta de tu casa y anota qué datos tiene.",
    extend="Explica por qué la garantía no sirve si se pierde el comprobante de compra.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F8 = ("Datos de ejemplo. Compra presencial: el producto se ve y se toca antes de comprar; el precio es $50.000; se paga en la tienda y se lleva el mismo día. "
      "Compra en línea desde una localidad lejana: el producto cuesta $50.000, más $7.000 de envío; el despacho demora 8 días; no se puede ver ni tocar antes. "
      "Antes de que existiera comercio en línea, las personas de zonas alejadas compraban sobre todo en tiendas cercanas, que eran pocas. "
      "En ambos casos, el proveedor debe informar el precio total y las condiciones, y el comprador conserva su derecho a reclamar si el producto es defectuoso.")
build(
    OA, 3, F8,
    use="Aprenderé a ver qué cambia y qué se mantiene en el consumo cuando se compra en línea o desde zonas alejadas. Sirve para comprar informado en distintos territorios.",
    prior=["Conozco derechos del consumidor, boleta, contrato y garantía.", "Sé comparar precios totales.", "Sé distinguir cambio de continuidad."],
    explain=[
        "Las formas de consumir cambian con el tiempo y el lugar. Antes, quienes vivían lejos de las ciudades compraban sobre todo en pocas tiendas cercanas. Hoy pueden comprar en línea a comercios ubicados en otras regiones o países. Eso aumenta la variedad de productos y la posibilidad de comparar precios, pero agrega costos de despacho, esperas y la imposibilidad de revisar el producto antes de comprar.",
        "Lo que continúa es la protección del consumidor. Sea una compra presencial o en línea, el proveedor debe informar el precio total, las características y las condiciones, y el comprador mantiene su derecho a reclamar si el producto es defectuoso o no corresponde a lo ofrecido. También continúa la importancia de guardar comprobantes como la boleta, el correo de confirmación y las capturas de pantalla de la oferta.",
        "El territorio influye en la decisión. En localidades apartadas puede haber pocas tiendas, entonces comprar en línea es una alternativa útil, pero el costo del envío y el tiempo de espera pesan más. Para comparar bien se calcula el precio total, que incluye el despacho, y se evalúa si la conveniencia justifica los riesgos y las esperas.",
    ],
    vocab=[("compra en línea", "compra hecha por internet, sin ir a la tienda"), ("despacho", "envío de un producto desde el vendedor hasta el comprador"), ("precio total", "precio del producto más todos los cobros adicionales"), ("variedad", "cantidad de opciones distintas entre las que se puede elegir"), ("comprobante", "documento que prueba una compra o una oferta")],
    worked=[
        ("Calcular el precio total", "Un artículo de ejemplo cuesta $30.000 en línea más $5.000 de envío. ¿Cuál es el precio total?",
         ["Sumo el precio y el despacho.", "30.000 + 5.000 = 35.000."], "$35.000"),
        ("Separar cambio y continuidad", "Antes se compraba solo en tiendas cercanas; hoy se puede comprar en línea, y en ambos casos el vendedor debe informar el precio total. ¿Qué cambia y qué continúa?",
         ["Cambia el lugar de compra: tienda o internet.", "Continúa la obligación de informar el precio total."], "Cambia dónde se compra; continúa el derecho a información"),
    ],
    mistakes=[
        ("Creer que comprar en línea es siempre más barato.", "El envío y la espera pueden anular la diferencia de precio.", "Calcula el precio total con despacho."),
        ("Pensar que comprar en línea elimina los derechos del consumidor.", "El derecho a información y a reclamar continúa.", "Guarda los comprobantes y exige información."),
    ],
    T=[
        ("En Economía: ¿qué es el precio total?", "El precio del producto más todos los cobros adicionales", "Incluye el despacho."),
        ("{F} ¿Cuánto cuesta el producto presencial?", "$50.000", "El dato aparece en la ficha."),
        ("{F} ¿Qué desventaja tiene la compra en línea según los datos? A) no se puede ver ni tocar el producto antes, B) se paga siempre más caro.", "A", "Eso lo dice la ficha."),
        ("=", "{F} ¿Cuál es el precio total de la compra en línea (en pesos)?", "50000+7000", "Se suma el envío al precio."),
        ("=", "{F} ¿Cuánto más cuesta la compra en línea que la presencial (en pesos)?", "50000+7000-50000", "Se resta el precio presencial al total en línea."),
        ("{F} ¿Qué cambió respecto de antes en las zonas alejadas? A) hoy se puede comprar en línea, B) ya no hay derechos del consumidor.", "A", "El comercio en línea es nuevo."),
        ("{F} ¿Qué continúa igual en ambos tipos de compra? A) el deber de informar el precio total, B) el despacho.", "A", "La ficha lo dice."),
        ("=", "{F} Si el despacho demora 8 días y el cliente compró el 3 de un mes, ¿qué día del mes llegará?", "3+8", "Se suman los días de espera."),
        ("=", "{F} Una familia compra 3 productos iguales en línea con un solo envío de $7.000. ¿Cuánto paga en total (en pesos)?", "3*50000+7000", "Se suman los productos y el envío."),
        ("{F} Una vecina de una zona alejada compra en línea porque en el pueblo no hay tiendas. ¿Qué dos costos debe considerar además del precio? Responde con una frase.", "El costo del envío y el tiempo de espera del despacho", "Son los costos extra de la compra en línea."),
        ("{F} Un joven compra en línea y el producto llega distinto al ofrecido. ¿Qué conviene que haya guardado? A) la captura de la oferta y el comprobante, B) nada.", "A", "Prueban lo que se ofreció."),
        ("Un compañero dice: «Como compré por internet, no puedo reclamar». ¿Qué respuesta corresponde? A) puede reclamar porque sus derechos continúan, B) no puede reclamar.", "A", "Los derechos no desaparecen por comprar en línea."),
        ("{F} ¿Qué compra conviene a alguien que necesita el producto hoy? A) la presencial, porque se lleva el mismo día, B) la compra en línea, porque demora 8 días.", "A", "La entrega es inmediata."),
    ],
    ctx=("Un taller de ejemplo en una isla sin tiendas compra una impresora a $120.000 en línea con envío de $15.000, o la compra en el continente por $125.000 con pasaje de $20.000. ¿Cuál tiene menor costo total? A) la compra en línea ($135.000), B) viajar ($145.000).", "A", "El total en línea es 135.000 y el del viaje, 145.000."),
    sc=[("En Economía: ¿qué cambió en la forma de comprar de las zonas alejadas?", "Que ahora pueden comprar en línea", "Antes dependían de pocas tiendas cercanas."),
        ("¿Qué derecho continúa al comprar en línea?", "El derecho a recibir información veraz y a reclamar", "La protección del consumidor no cambia."),
        ("¿Por qué conviene calcular el precio total en una compra en línea?", "Porque el despacho se suma al precio", "El costo extra puede cambiar la decisión.")],
    op=("{F} Escribe un párrafo con: dos diferencias entre la compra presencial y la compra en línea, una continuidad en los derechos y un cálculo del precio total en línea. Termina con una recomendación para una persona que vive lejos de las tiendas.",
        "Diferencias: presencial se ve el producto y se lleva el mismo día; en línea demora 8 días. Continúa el derecho a información y reclamo. Precio total en línea: $57.000. Recomendación: comprar en línea si no hay urgencia y se guardan comprobantes.",
        ["nombra dos diferencias", "señala una continuidad", "calcula el precio total", "da una recomendación"], ["un párrafo con una cifra"], ["decir que comprar en línea no tiene derechos", "olvidar el costo del envío"], "Pide a una persona de tu casa que opine sobre tu recomendación."),
    reinforce="Anota tres cosas que comprarías en línea y una que preferirías ver antes de comprar.",
    extend="Explica por qué el comercio en línea puede aumentar la variedad pero también las dudas sobre la calidad.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F9 = ("Caso de ejemplo: Rodrigo, adulto ficticio, firmó sin leer el contrato de un gimnasio ficticio. Una cláusula impide darse de baja y cobra una multa de tres cuotas mensuales de $25.000. "
      "Voz del gimnasio (de ejemplo): «El cliente firmó; es su responsabilidad.» "
      "Voz de Rodrigo (de ejemplo): «Nadie me explicó la cláusula de la multa.» "
      "Voz de la autoridad del consumidor (de ejemplo): «El proveedor debe informar con claridad y no puede imponer condiciones abusivas.» "
      "Voz de una asociación de consumidores (de ejemplo): «Hay que leer los contratos, pero también exigir contratos claros.»")
build(
    OA, 4, F9,
    use="Aprenderé a comparar las perspectivas del consumidor, del proveedor y de las autoridades ante un reclamo, y a ver que las dificultades tienen varias causas. Sirve para saber cómo actuar ante un problema de consumo.",
    prior=["Conozco derechos del consumidor, contrato, boleta y garantía.", "Sé que cada actor tiene una perspectiva.", "Sé calcular multiplicaciones de dinero."],
    explain=[
        "En un conflicto de consumo participan varios actores. El consumidor busca que se respeten sus derechos; el proveedor busca vender y cobrar; la autoridad del consumidor informa, fiscaliza y recibe reclamos; las asociaciones de consumidores orientan y defienden a las personas. Cada uno ve la situación desde su posición, por eso conviene escuchar todas las perspectivas antes de concluir.",
        "Culpar al consumidor por todo es un error. Es cierto que debe informarse y leer, pero el proveedor tiene el deber de informar con claridad, y una cláusula abusiva, que es una condición que deja al consumidor en una posición muy desventajosa, no se vuelve válida solo porque se firmó. Firmar un contrato no elimina los derechos ni la responsabilidad del proveedor de informar.",
        "Ante un problema, el camino habitual es reclamar primero al proveedor, guardando comprobantes y pidiendo una respuesta escrita; si no hay solución, acudir a la autoridad del consumidor. Las causas de un conflicto suelen ser varias: poca información, contratos poco claros, apuro del comprador y falta de revisión del proveedor. Hablamos de multicausalidad.",
    ],
    vocab=[("cláusula abusiva", "condición de un contrato que deja al consumidor en una posición muy desventajosa"), ("reclamo", "queja formal por un producto o servicio que no cumple lo ofrecido"), ("fiscalizar", "controlar que se cumplan las normas"), ("multa", "pago que se cobra como sanción por incumplir una norma o contrato"), ("multicausalidad", "situación en que un hecho tiene varias causas a la vez")],
    worked=[
        ("Calcular una multa", "Un contrato de ejemplo cobra una multa de dos cuotas de $18.000 al dar de baja el servicio. ¿Cuánto es la multa?",
         ["Multiplico las cuotas por su valor.", "2 × 18.000 = 36.000."], "$36.000"),
        ("Ordenar los pasos de un reclamo", "Una persona de ejemplo recibe un producto defectuoso. ¿A quién reclama primero y a quién después si no hay solución?",
         ["Primero se reclama al proveedor, guardando comprobantes.", "Si no responde, se acude a la autoridad del consumidor."], "Primero al proveedor; luego a la autoridad del consumidor"),
    ],
    mistakes=[
        ("Decir que el consumidor tiene toda la culpa por firmar.", "El proveedor también debe informar con claridad y no imponer cláusulas abusivas.", "Revisa la responsabilidad de ambos."),
        ("Creer que reclamar a la autoridad es el primer paso siempre.", "Lo habitual es reclamar primero al proveedor y guardar su respuesta.", "Reclama primero al proveedor y guarda los comprobantes."),
    ],
    T=[
        ("En Economía: ¿qué es una cláusula abusiva?", "Una condición de un contrato que deja al consumidor en una posición muy desventajosa", "No se vuelve válida solo por firmarse."),
        ("{F} ¿Qué cobra la cláusula del gimnasio si Rodrigo quiere darse de baja?", "Una multa de tres cuotas mensuales", "El caso lo dice."),
        ("{F} ¿Qué actor dice «es su responsabilidad»? A) el gimnasio, B) la asociación de consumidores.", "A", "Defiende su posición como proveedor."),
        ("=", "{F} ¿Cuánto es la multa que cobra el gimnasio (en pesos)?", "3*25000", "Se multiplica la cuota por 3."),
        ("=", "{F} Si Rodrigo pagara la multa y 2 cuotas más pendientes, ¿cuánto pagaría en total (en pesos)?", "3*25000+2*25000", "Se suman la multa y las cuotas pendientes."),
        ("{F} ¿Qué voz reconoce que los clientes deben leer pero que los contratos deben ser claros? A) la de la asociación de consumidores, B) la del gimnasio.", "A", "Equilibra el deber del cliente y el del proveedor."),
        ("{F} ¿Qué deber del gimnasio señala la autoridad del consumidor? A) informar con claridad, B) vender más.", "A", "Es el deber de información."),
        ("=", "{F} Si el contrato cobrara una multa de 5 cuotas en vez de 3, ¿cuánto sería (en pesos)?", "5*25000", "Se multiplica el valor de la cuota por 5."),
        ("{F} Rodrigo quiere reclamar. ¿Qué debe hacer primero? A) reclamar al gimnasio por escrito, B) ir directo a un juicio.", "A", "Lo habitual es reclamar primero al proveedor."),
        ("{F} Un comentarista dice: «Rodrigo es el único culpable por no leer». Usando las voces, ¿qué dato contradice esa idea? Responde con una frase.", "Que el proveedor también debe informar con claridad y no imponer cláusulas abusivas", "La responsabilidad es compartida."),
        ("{F} ¿Qué dos causas de este conflicto aparecen en el caso? Responde con una frase.", "Que Rodrigo no leyó el contrato y que el gimnasio no explicó la cláusula", "El caso muestra ambos hechos."),
        ("Una asociación de consumidores de ejemplo recibe 40 reclamos por cláusulas parecidas. ¿Qué indica eso? A) que puede haber un problema general en esos contratos y no solo un caso, B) que todos los clientes son descuidados.", "A", "Muchos casos iguales sugieren un problema común."),
        ("=", "{F} Si 12 clientes parecidos a Rodrigo pagaran la multa, ¿cuánto dinero recibiría el gimnasio en multas (en pesos)?", "12*3*25000", "Se multiplica la multa por 12 personas."),
    ],
    ctx=("Una tienda de ejemplo se niega a cambiar un celular defectuoso porque el cliente «aceptó las condiciones al comprar». El cliente tiene la boleta y el producto falla dentro del plazo de garantía. ¿Qué debe hacer primero? A) reclamar a la tienda por escrito y guardar su respuesta, B) comprar otro celular en la misma tienda.", "A", "Es el primer paso del reclamo."),
    sc=[("En Economía: ¿a quién se reclama primero en un problema de consumo?", "Al proveedor", "Después, si no responde, a la autoridad del consumidor."),
        ("¿Por qué firmar un contrato no elimina los derechos?", "Porque la ley protege al consumidor y el proveedor debe informar con claridad", "Una cláusula abusiva no es válida solo por firmarse."),
        ("¿Qué es la multicausalidad en un conflicto de consumo?", "Que hay varias causas a la vez, como poca información y contratos poco claros", "No hay una sola culpa.")],
    op=("{F} Escribe qué voz crees que está mejor fundamentada y por qué, nombra dos causas del conflicto y un paso concreto que Rodrigo debe dar. Usa una cifra del caso.",
        "La voz de la autoridad está mejor fundamentada porque exige información clara. Causas: Rodrigo no leyó y el gimnasio no explicó la cláusula. Paso: reclamar por escrito al gimnasio por la multa de $75.000 y guardar la respuesta.",
        ["elige una voz con razón", "nombra dos causas", "da un paso de reclamo", "usa una cifra"], ["un párrafo con una cifra"], ["culpar solo al consumidor", "no nombrar ningún paso concreto"], "Léele tu respuesta a una persona de tu casa y pídele que diga si estuvo de acuerdo con tu voz elegida."),
    reinforce="Escribe los pasos de un reclamo en orden: qué haces primero, segundo y tercero.",
    extend="Explica por qué las asociaciones de consumidores pueden ayudar cuando muchas personas tienen el mismo problema.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F10 = ("Dossier de ejemplo, «¿Debe Matías comprar un televisor de $400.000 al contado o en 12 cuotas de $40.000?» Matías es un adulto ficticio. "
       "Dato 1: su ingreso mensual es de $700.000. "
       "Dato 2: sus gastos fijos, sin contar deudas, son de $520.000 al mes. "
       "Dato 3: ya paga una cuota de otra deuda de $90.000 al mes. "
       "Dato 4: su televisor actual funciona bien. "
       "Guía de ejemplo: conviene que todas las cuotas juntas no pasen de un cuarto del ingreso.")
build(
    OA, 5, F10,
    use="Aprenderé a evaluar una decisión de consumo y de endeudamiento con datos, derechos y límites. Sirve para decidir con responsabilidad y sin culparse ni culpar a otros sin pruebas.",
    prior=["Sé calcular costo total, saldo de presupuesto y porcentaje del ingreso.", "Conozco derechos del consumidor.", "Sé armar un argumento con tesis, evidencia, objeción y límite."],
    explain=[
        "Evaluar una decisión de consumo significa comparar lo que se gana con lo que se compromete. Si se compra al contado, se evita el interés; si se compra a crédito, se paga más en total y se reduce el dinero disponible cada mes. El presupuesto mensual permite ver cuánto queda después de los gastos fijos y las cuotas. Si el saldo es pequeño, cualquier imprevisto puede transformar la deuda en un problema.",
        "También importa la necesidad. Un bien que se necesita con urgencia no se evalúa igual que uno que se desea pero que se puede postergar. La guía del cuarto del ingreso es una orientación: sirve para ver si las cuotas son manejables, pero no reemplaza el juicio sobre la situación de cada persona.",
        "Un argumento completo declara una tesis, usa cifras del presupuesto, reconoce una objeción razonable y la responde, y dice cuál es el límite de los datos. Por ejemplo, el dossier no informa si el ingreso podría bajar. Además, un consumo responsable exige informarse, guardar los comprobantes y saber a quién reclamar si hay un problema.",
    ],
    vocab=[("gasto fijo", "gasto que se repite cada mes, como el arriendo"), ("saldo", "dinero que queda después de pagar los gastos"), ("imprevisto", "gasto o problema que no se puede anticipar"), ("tesis", "afirmación que se defiende en un argumento"), ("objeción", "razón que va en contra de una tesis")],
    worked=[
        ("Calcular el saldo mensual", "Una persona de ejemplo gana $500.000, tiene gastos fijos de $350.000 y paga una cuota de $60.000. ¿Cuánto le queda al mes?",
         ["Sumo los gastos: 350.000 + 60.000 = 410.000.", "Resto: 500.000 - 410.000 = 90.000."], "Le quedan $90.000"),
        ("Aplicar la guía del cuarto", "La misma persona suma una cuota nueva de $50.000. Con el límite de un cuarto del ingreso, ¿está bajo o sobre el límite?",
         ["El límite es 500.000 ÷ 4 = 125.000.", "Sus cuotas serían 60.000 + 50.000 = 110.000, menor que el límite."], "Está bajo el límite"),
    ],
    mistakes=[
        ("Aceptar un crédito solo porque la cuota parece pequeña.", "Cada cuota nueva reduce el saldo y aumenta el compromiso.", "Calcula el saldo después de todas las cuotas."),
        ("Ignorar los imprevistos.", "Un gasto inesperado puede dejar sin recursos para pagar.", "Reserva un margen para imprevistos."),
    ],
    T=[
        ("En Economía: ¿qué es un imprevisto?", "Un gasto o problema que no se puede anticipar", "Obliga a tener margen en el presupuesto."),
        ("{F} ¿Cuál es el ingreso mensual de Matías?", "$700.000", "Lo informa el dato 1."),
        ("{F} ¿Funciona el televisor actual de Matías? A) sí, B) no.", "A", "El dato 4 lo dice."),
        ("=", "{F} Sin la nueva compra, ¿cuánto le queda a Matías al mes (en pesos)?", "700000-520000-90000", "Se restan gastos fijos y cuota actual al ingreso."),
        ("=", "{F} Con la nueva cuota, ¿cuánto le quedaría al mes (en pesos)?", "700000-520000-90000-40000", "Se resta también la cuota nueva."),
        ("=", "{F} ¿Cuánto se paga en total con el crédito de 12 cuotas (en pesos)?", "12*40000", "Se multiplica la cuota por las cuotas."),
        ("=", "{F} ¿Cuánto más paga a crédito que al contado (en pesos)?", "12*40000-400000", "Se resta el precio al contado."),
        ("=", "{F} Con la compra, ¿cuánto sumarían sus cuotas mensuales (en pesos)?", "90000+40000", "Se suma la cuota nueva a la actual."),
        ("=", "{F} Según la guía de ejemplo, el límite de cuotas es un cuarto del ingreso. ¿Cuánto es ese límite (en pesos)?", "700000//4", "Un cuarto de 700.000 es 175.000."),
        ("{F} ¿La compra a crédito respeta la guía? A) sí, porque 130.000 es menor que 175.000, B) no, porque supera 175.000.", "A", "Las cuotas quedarían bajo el límite."),
        ("{F} Pese a que respeta la guía, ¿qué argumento puede sostener que no conviene comprar? A) el televisor actual funciona y el crédito cuesta $80.000 más, B) las cuotas superan el límite de la guía.", "A", "Hay un costo extra y no hay urgencia."),
        ("=", "{F} Matías ahorra $40.000 al mes en vez de pagar cuotas. ¿En cuántos meses reúne el precio al contado?", "400000//40000", "400.000 dividido en 40.000 da 10."),
        ("{F} Una objeción a esperar 10 meses es que hay una oferta que podría acabarse. ¿Qué respuesta es razonable? A) las ofertas suelen repetirse y el televisor actual sirve mientras tanto, B) comprar de inmediato sin pensar.", "A", "Responde a la objeción con un dato del dossier."),
    ],
    ctx=("Una joven de ejemplo gana $250.000 al mes y quiere comprar zapatillas de $60.000 en 3 cuotas de $22.000. Si la guía de ejemplo es un cuarto del ingreso, ¿su cuota respeta ese límite? A) sí, porque el límite es $62.500, B) no, porque la cuota supera el límite.", "A", "Un cuarto de 250.000 es 62.500 y la cuota es 22.000."),
    sc=[("En Economía: ¿qué datos usas para saber si una cuota es manejable?", "El ingreso, los gastos fijos y las demás cuotas", "Con ellos se calcula el saldo."),
        ("¿Por qué conviene dejar un margen para imprevistos?", "Porque un gasto inesperado puede dejar sin dinero para pagar las cuotas", "Así se evita no poder pagar las cuotas."),
        ("¿Qué parte de un argumento responde a una razón contraria?", "La respuesta a la objeción", "Muestra que se consideró otra posición.")],
    op=("{F} Escribe un argumento de cinco a siete líneas sobre si Matías debe comprar el televisor ahora a crédito. Incluye tu tesis, dos cifras del dossier, una objeción con su respuesta y un límite de los datos.",
        "Tesis: Matías no debe comprarlo ahora. A crédito paga $80.000 más. Objeción: la oferta podría acabar; se responde con que su televisor funciona. Límite: no sabemos si su ingreso podría bajar o si habrá otras ofertas.",
        ["declara una tesis", "usa dos cifras", "responde una objeción", "indica un límite"], ["un argumento de cinco a siete líneas"], ["no usar cifras", "ignorar que el televisor actual funciona"], "Léele tu argumento a una persona de tu casa y pídele que diga si respondes a su objeción."),
    reinforce="Escribe tres preguntas que harías antes de comprar algo en cuotas.",
    extend="Explica cómo cambiaría tu conclusión si el televisor de Matías estuviera dañado.",
    materials=MAT,
)
