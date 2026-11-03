"""Student material for 8.º básico Matemática, OA 12 (teorema de Pitágoras) y OA 13 (traslaciones, rotaciones y reflexiones)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA12, OA13 = "MA08 OA 12", "MA08 OA 13"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, mat, use, prior, explain, vocab, worked, mist, R, C, A, Z, D, ctx, chk, open, reinforce, extend):
    """Registra una clase con una forma compacta (misma estructura que register)."""
    register(
        oa, n,
        materials=mat, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mist],
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=chk, open_task=task(*open), reinforce=reinforce, extend=extend,
    )


MAT_GEO = "Hoja cuadriculada, lápiz, regla y, si quieres, una calculadora. Todos los datos que necesitas están escritos en cada ejercicio."

# ================================================================ OA 12
L(OA12, 1,
  mat=MAT_GEO,
  use="Aprenderé a mirar las áreas de los cuadrados construidos sobre los lados de un triángulo rectángulo y a descubrir qué relación hay entre ellas. Sirve para comprobar si una esquina es recta sin usar escuadra.",
  prior=["Sé calcular el área de un cuadrado: lado por lado.", "Sé que un ángulo recto mide 90° y que un triángulo rectángulo tiene uno."],
  explain=[
      "Un triángulo rectángulo tiene un ángulo de 90°. Los dos lados que forman ese ángulo se llaman catetos. El lado que queda enfrente del ángulo recto, que siempre es el más largo, se llama hipotenusa. La hipotenusa nunca es «el lado que se ve inclinado»: es el lado opuesto al ángulo recto, sin importar cómo esté girado el triángulo.",
      "Sobre cada lado del triángulo se puede dibujar un cuadrado que lo use como lado. El área de ese cuadrado es el lado multiplicado por sí mismo, o sea, el lado al cuadrado. En un triángulo con catetos de 3 y 4 unidades, los cuadrados de los catetos tienen 9 y 16 cuadritos, y el cuadrado de la hipotenusa, que mide 5, tiene 25 cuadritos. Y al revés: si conoces el área de un cuadrado, su lado es el número que multiplicado por sí mismo da esa área; por ejemplo, un cuadrado de 25 cuadritos tiene lado 5.",
      "Fíjate: 9 + 16 = 25. En todo triángulo rectángulo, la suma de las áreas de los cuadrados de los catetos es igual al área del cuadrado de la hipotenusa. Esa regularidad se llama teorema de Pitágoras. Si en un triángulo la suma no coincide, el triángulo no tiene ángulo recto. En la próxima clase la escribiremos con letras.",
  ],
  vocab=[("cateto", "cada uno de los dos lados que forman el ángulo recto"), ("hipotenusa", "lado opuesto al ángulo recto, el más largo"), ("triángulo rectángulo", "triángulo con un ángulo de 90°"), ("cuadrado de un lado", "cuadrado que tiene ese lado; su área es el lado multiplicado por sí mismo")],
  worked=[
      ("Catetos de 5 y 12", "Un triángulo rectángulo tiene catetos de 5 cm y 12 cm. Compara el área de los cuadrados de los catetos con la del cuadrado de la hipotenusa, que mide 13 cm.", ["Cuadrado del cateto de 5 cm: 5 × 5 = 25 cm².", "Cuadrado del cateto de 12 cm: 12 × 12 = 144 cm². La suma es 25 + 144 = 169 cm².", "Cuadrado de la hipotenusa: 13 × 13 = 169 cm². Las dos áreas son iguales."], "25 + 144 = 169 = 13 × 13: la suma de las áreas de los catetos es el área de la hipotenusa"),
      ("¿Es rectángulo?", "Un triángulo tiene lados de 4 cm, 6 cm y 7 cm. ¿Tiene un ángulo recto?", ["Cuadrados de los dos lados menores: 4 × 4 = 16 y 6 × 6 = 36; suma 52.", "Cuadrado del lado mayor: 7 × 7 = 49.", "52 no es igual a 49, así que la relación no se cumple."], "No es rectángulo, porque 16 + 36 es distinto de 49"),
  ],
  mist=[
      ("Llamar hipotenusa al lado que se ve inclinado.", "La hipotenusa se define por estar frente al ángulo recto, no por su inclinación.", "Busca primero el ángulo de 90°; la hipotenusa es el lado que queda enfrente."),
      ("Sumar los lados en vez de las áreas de los cuadrados: 3 + 4 = 7.", "La relación es entre áreas, no entre largos.", "Calcula primero el cuadrado de cada cateto y recién después suma."),
  ],
  R=[arith("Un cuadrado se construye sobre un lado de 7 cm. ¿Cuál es su área?", "7*7", "El área del cuadrado es el lado por sí mismo.", " cm²"),
     ex("¿Cómo se llama el lado de un triángulo rectángulo que está enfrente del ángulo recto?", "Hipotenusa", "Por definición, la hipotenusa es el lado opuesto al ángulo de 90°."),
     arith("Un triángulo rectángulo tiene catetos de 3 cm y 4 cm. ¿Cuál es la suma de las áreas de los cuadrados de sus catetos?", "3*3+4*4", "Se suman 9 cm² y 16 cm², que es el área del cuadrado de la hipotenusa.", " cm²")],
  C=[ex("El cuadrado construido sobre la hipotenusa de un triángulo rectángulo tiene 25 cm² de área. ¿Cuánto mide la hipotenusa?", "5 cm", "El lado de un cuadrado de 25 cm² es el número que multiplicado por sí mismo da 25, o sea 5."),
     arith("Los catetos de un triángulo rectángulo miden 6 cm y 8 cm. ¿Cuál es el área del cuadrado de la hipotenusa?", "6*6+8*8", "Es la suma de las áreas de los cuadrados de los catetos: 36 + 64.", " cm²"),
     ex("Un triángulo rectángulo tiene cuadrados de 13 cm², 36 cm² y 49 cm² sobre sus lados. ¿Cuál es el área del cuadrado de la hipotenusa?", "49 cm²", "Es el cuadrado mayor y cumple 13 + 36 = 49.")],
  A=[ex("Los cuadrados de los catetos de un triángulo rectángulo tienen 64 cm² y 225 cm². ¿Cuánto mide la hipotenusa?", "17 cm", "64 + 225 = 289, y 17 × 17 = 289."),
     ex("Los lados de un triángulo miden 9 cm, 12 cm y 15 cm. ¿Es un triángulo rectángulo? Responde sí o no.", "Sí", "81 + 144 = 225, que es 15 × 15."),
     arith("El cuadrado de la hipotenusa tiene 100 cm² y el cuadrado de un cateto tiene 36 cm². ¿Cuál es el área del cuadrado del otro cateto?", "100-36", "El cuadrado de la hipotenusa es la suma de los otros dos, así que se resta.", " cm²")],
  Z=[ex("Un triángulo tiene lados de 5 cm, 6 cm y 8 cm. ¿Es rectángulo? Responde sí o no.", "No", "25 + 36 = 61, que es distinto de 64."),
     ex("Lucas dice: «El cuadrado de un cateto puede tener más área que el cuadrado de la hipotenusa». ¿Es cierto? Responde sí o no.", "No", "El cuadrado de la hipotenusa es la suma de los dos de los catetos, así que es mayor que cada uno.")],
  D=[arith("Las áreas de los tres cuadrados construidos sobre los lados de un triángulo rectángulo suman 200 cm². ¿Cuál es el área del cuadrado de la hipotenusa?", "200//2", "El cuadrado de la hipotenusa vale lo mismo que los otros dos juntos, así que es la mitad del total.", " cm²"),
     arith("Un triángulo rectángulo tiene dos catetos iguales de 10 cm. ¿Cuál es el área del cuadrado de su hipotenusa?", "10*10+10*10", "Se suman las áreas de los cuadrados de los dos catetos.", " cm²")],
  ctx=[ex("Una carpintera arma una esquina con una tabla de 60 cm y otra de 80 cm, y mide 100 cm entre sus extremos libres. ¿La esquina es recta? Responde sí o no.", "Sí", "3.600 + 6.400 = 10.000, que es 100 × 100.")],
  chk=[ex("¿Cómo se llaman los dos lados que forman el ángulo recto de un triángulo rectángulo?", "Catetos", "Los lados que forman el ángulo de 90° son los catetos."),
       arith("Un cuadrado se construye sobre un lado de 9 cm. ¿Cuál es su área?", "9*9", "Lado por lado.", " cm²"),
       arith("Los cuadrados de los catetos de un triángulo rectángulo tienen 20 cm² y 5 cm². ¿Cuál es el área del cuadrado de la hipotenusa?", "20+5", "Se suman las áreas de los cuadrados de los catetos.", " cm²")],
  open=("En una hoja cuadriculada dibuja un triángulo rectángulo con catetos de 3 cuadritos y 4 cuadritos. Dibuja un cuadrado sobre cada uno de sus tres lados, cuenta los cuadritos de cada cuadrado (el cuadrado inclinado puedes rodearlo con un cuadrado de 7 × 7 cuadritos y restar los cuatro triángulos de 6 cuadritos que sobran) y escribe si la suma de los dos cuadrados de los catetos es igual al tercero. Si tienes un programa de geometría, puedes repetirlo con él.",
        "Cuadrado de los catetos: 9 y 16 cuadritos; cuadrado de la hipotenusa: 25 cuadritos. 9 + 16 = 25, así que sí es igual.",
        ["dibuja el triángulo con el ángulo recto", "dibuja los tres cuadrados", "cuenta los cuadritos de cada uno", "concluye si 9 + 16 es igual a 25"],
        ["dibujo con los tres cuadrados", "tres conteos anotados", "frase de conclusión"],
        ["dibujar el cuadrado sobre un lado equivocado", "contar mal los cuadritos del cuadrado inclinado", "sumar los largos en vez de las áreas"],
        "Pide que señale la hipotenusa y diga por qué lo es. Reconoce que haya comparado áreas, no largos."),
  reinforce="Dibuja un triángulo rectángulo con catetos de 6 y 8 cuadritos y comprueba con la regla que su hipotenusa mide 10 cuadritos, porque 36 + 64 = 100.",
  extend="Explica con tus palabras por qué la relación entre las áreas sirve para reconocer si una esquina es recta.")

L(OA12, 2,
  mat=MAT_GEO,
  use="Aprenderé a escribir el teorema de Pitágoras con letras, a justificar por qué es verdadero con un dibujo de áreas y a usarlo solo cuando el triángulo es rectángulo.",
  prior=["Sé qué son catetos e hipotenusa.", "Sé calcular el cuadrado de un número y el área de un triángulo."],
  explain=[
      "El teorema de Pitágoras dice: en un triángulo rectángulo con catetos a y b e hipotenusa c, se cumple a² + b² = c². La expresión a² significa a por a. El teorema solo vale para triángulos rectángulos. Y también al revés: si en un triángulo las medidas cumplen a² + b² = c², entonces ese triángulo es rectángulo.",
      "¿Por qué es verdadero? Toma un cuadrado grande de lado a + b. Dentro puedes poner cuatro triángulos rectángulos iguales, de catetos a y b, con las hipotenusas formando un cuadrado inclinado de lado c en el centro. El área del cuadrado grande es (a + b)², y también es 4 triángulos de área a·b/2 cada uno más el cuadrado inclinado c².",
      "Entonces a² + 2ab + b² = 2ab + c². Al quitar 2ab a ambos lados queda a² + b² = c². En la figura se ve concretamente y con símbolos se confirma. Cuidado: se suman los cuadrados de los catetos, no los catetos mismos. Con catetos 6 y 8 la hipotenusa no es 14, sino 10.",
  ],
  vocab=[("teorema", "afirmación matemática que se puede demostrar"), ("a²", "a multiplicado por a"), ("recíproco", "si se cumple a² + b² = c², el triángulo es rectángulo"), ("cuadrado inclinado", "cuadrado del centro de la figura, cuyo lado es la hipotenusa")],
  worked=[
      ("Calcular c² con catetos 6 y 8", "Un triángulo rectángulo tiene catetos de 6 cm y 8 cm. ¿Cuánto mide la hipotenusa?", ["Se escribe a² + b² = c²: 6² + 8² = c².", "36 + 64 = 100, así que c² = 100.", "El número que multiplicado por sí mismo da 100 es 10."], "c = 10 cm"),
      ("Comprobar con la figura", "Cuatro triángulos de catetos 2 y 3 se ubican dentro de un cuadrado de lado 5. ¿Cuál es el área del cuadrado inclinado y cuánto vale a² + b²?", ["Área del cuadrado grande: 5 × 5 = 25.", "Cada triángulo tiene 2 × 3 ÷ 2 = 3, y cuatro suman 12. El cuadrado inclinado es 25 − 12 = 13.", "Con símbolos: 2² + 3² = 4 + 9 = 13. Coinciden."], "c² = 13, igual que 2² + 3²"),
  ],
  mist=[
      ("Sumar los catetos: con 9 y 12 dice que c = 21.", "Se suman los cuadrados de los catetos, no los catetos.", "Escribe 9² + 12² = 225 y luego busca el número que al cuadrado da 225."),
      ("Aplicar a² + b² = c² a un triángulo cualquiera.", "El teorema solo vale en triángulos con un ángulo de 90°.", "Antes de usarlo, comprueba que el triángulo tiene ángulo recto."),
  ],
  R=[ex("En la igualdad a² + b² = c², ¿qué letra representa la hipotenusa?", "c", "a y b son los catetos y c es el lado opuesto al ángulo recto."),
     arith("¿Cuánto es 12², es decir, 12 por 12?", "12*12", "El cuadrado de un número es el número multiplicado por sí mismo."),
     arith("Un triángulo rectángulo tiene catetos de 8 cm y 15 cm. ¿Cuánto vale a² + b²?", "8*8+15*15", "Se suman los cuadrados de los catetos.", " cm²")],
  C=[ex("Un triángulo rectángulo tiene catetos de 9 cm y 12 cm. ¿Cuánto mide la hipotenusa?", "15 cm", "81 + 144 = 225, y 15 × 15 = 225."),
     arith("Los catetos de un triángulo rectángulo miden 7 cm y 24 cm. ¿Cuánto vale c²?", "7*7+24*24", "Se suman los cuadrados de los catetos: 49 + 576.", " cm²"),
     ex("¿Qué afirma el teorema de Pitágoras? A) En cualquier triángulo, la suma de los cuadrados de dos lados es el cuadrado del tercero. B) En un triángulo rectángulo, la suma de los cuadrados de los catetos es el cuadrado de la hipotenusa. C) En un triángulo rectángulo, la suma de los catetos es igual a la hipotenusa.", "B", "El teorema vale solo con ángulo recto y relaciona cuadrados, no largos.")],
  A=[ex("Un triángulo rectángulo tiene catetos de 20 cm y 21 cm. ¿Cuánto mide la hipotenusa?", "29 cm", "400 + 441 = 841, y 29 × 29 = 841."),
     ex("Un triángulo tiene lados de 12 cm, 16 cm y 20 cm. ¿Se cumple a² + b² = c² con c = 20? Responde sí o no.", "Sí", "144 + 256 = 400, que es 20 × 20."),
     arith("Cuatro triángulos rectángulos de catetos 4 cm y 7 cm se colocan dentro de un cuadrado de lado 11 cm. ¿Qué área tiene el cuadrado inclinado del centro?", "11*11-4*(4*7//2)", "Al área del cuadrado grande se le restan los cuatro triángulos, de 14 cm² cada uno.", " cm²")],
  Z=[ex("Sofía dice que un triángulo rectángulo de catetos 9 cm y 12 cm tiene hipotenusa 21 cm porque 9 + 12 = 21. ¿Tiene razón? Responde sí o no.", "No", "Hay que sumar los cuadrados, 81 + 144 = 225, y la hipotenusa es 15 cm."),
     ex("Tomás calculó 7² + 8² = 113 y 11² = 121 en un triángulo de lados 7, 8 y 11. ¿Puede asegurar que el triángulo es rectángulo? Responde sí o no.", "No", "113 es distinto de 121, así que no se cumple la relación.")],
  D=[ex("Cuatro triángulos rectángulos de catetos 8 cm y 15 cm se ubican dentro de un cuadrado de lado 23 cm. ¿Cuánto mide el lado del cuadrado inclinado del centro?", "17 cm", "Su área es 529 − 4 × 60 = 289, y 17 × 17 = 289."),
     ex("Un triángulo rectángulo tiene dos catetos iguales y c² = 50. ¿Cuánto mide cada cateto?", "5 cm", "a² + a² = 50 da a² = 25, así que a = 5.")],
  ctx=[ex("Un marco rectangular mide 30 cm de ancho y 40 cm de alto. Se le pone una varilla en diagonal de una esquina a la opuesta. ¿Cuánto mide la varilla?", "50 cm", "La diagonal es la hipotenusa: 900 + 1.600 = 2.500, y 50 × 50 = 2.500.")],
  chk=[ex("¿En qué clase de triángulos se puede usar a² + b² = c²?", "En los triángulos rectángulos", "El teorema necesita un ángulo recto."),
       arith("Si la hipotenusa mide 13 cm, ¿cuánto vale c²?", "13*13", "c² es la hipotenusa multiplicada por sí misma.", " cm²"),
       arith("En un triángulo rectángulo, c² = 100 y a² = 36. ¿Cuánto vale b²?", "100-36", "Como a² + b² = c², b² se obtiene restando.", " cm²")],
  open=("Dibuja un cuadrado de lado 7 cm. Marca en cada lado un punto a 3 cm de una esquina (siempre en el mismo sentido) y únelos: queda un cuadrado inclinado con cuatro triángulos rectángulos de catetos 3 cm y 4 cm. Calcula el área del cuadrado grande, la de los cuatro triángulos y la del cuadrado inclinado, y comprueba que es 3² + 4².",
        "Cuadrado grande: 49 cm². Cuatro triángulos: 4 × 6 = 24 cm². Cuadrado inclinado: 49 − 24 = 25 cm², igual a 9 + 16.",
        ["dibuja el cuadrado y marca los puntos", "calcula las tres áreas", "compara con 3² + 4²", "escribe la conclusión"],
        ["dibujo con la figura", "tres cálculos", "frase de conclusión"],
        ["marcar los puntos a distancias distintas", "olvidar multiplicar por 4 los triángulos", "no comparar con a² + b²"],
        "Pide que explique de dónde sale el 4 en 4 × 6. Reconoce que verifique con la medición del lado inclinado."),
  reinforce="Calcula la hipotenusa de un triángulo rectángulo de catetos 5 cm y 12 cm usando a² + b² = c².",
  extend="Explica por qué en (a + b)² aparece el término 2ab y por qué se cancela al comparar con los cuatro triángulos.")

L(OA12, 3,
  mat=MAT_GEO,
  use="Aprenderé a calcular la hipotenusa o un cateto desconocido de un triángulo rectángulo y a decir entre qué números enteros queda una raíz que no es exacta.",
  prior=["Sé que a² + b² = c² en un triángulo rectángulo.", "Sé cuáles son los cuadrados perfectos: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100…"],
  explain=[
      "Para hallar la hipotenusa se suman los cuadrados de los catetos y se busca el número que al cuadrado da esa suma: c = √(a² + b²). El símbolo √ se llama raíz cuadrada y responde: ¿qué número multiplicado por sí mismo da este valor? Por ejemplo, √144 = 12, porque 12 × 12 = 144.",
      "Para hallar un cateto se hace lo contrario: se resta. Si c es la hipotenusa y a un cateto, entonces b² = c² − a². Siempre se resta el cuadrado del cateto conocido al cuadrado de la hipotenusa, nunca al revés, porque la hipotenusa es el lado mayor.",
      "A veces el resultado no es un número entero. Por ejemplo, 41 no es cuadrado perfecto, pero 36 < 41 < 49, así que √41 está entre 6 y 7. Con eso se puede estimar una medida y revisar que el resultado tenga sentido: la hipotenusa debe ser mayor que cada cateto. Si te sale menor, algo se hizo mal.",
  ],
  vocab=[("raíz cuadrada", "número que multiplicado por sí mismo da el valor indicado"), ("cuadrado perfecto", "número cuya raíz cuadrada es un entero"), ("estimar", "dar un valor aproximado entre dos números conocidos"), ("trío pitagórico", "tres enteros que cumplen a² + b² = c², como 3, 4, 5")],
  worked=[
      ("Hipotenusa con catetos 10 y 24", "Un triángulo rectángulo tiene catetos de 10 cm y 24 cm. ¿Cuánto mide la hipotenusa?", ["c² = 10² + 24² = 100 + 576 = 676.", "Se busca el número que al cuadrado da 676: 26 × 26 = 676."], "c = 26 cm"),
      ("Hipotenusa que no es exacta", "Los catetos miden 4 cm y 5 cm. ¿Entre qué dos enteros consecutivos queda la hipotenusa?", ["c² = 16 + 25 = 41.", "36 < 41 < 49, es decir, 6² < 41 < 7².", "Por lo tanto la hipotenusa está entre 6 cm y 7 cm."], "Entre 6 cm y 7 cm"),
  ],
  mist=[
      ("Sumar para hallar un cateto: con c = 13 y a = 5 calcula 169 + 25.", "El cuadrado de la hipotenusa ya incluye al del cateto; hay que quitarlo.", "Usa b² = c² − a² y comprueba que b salga menor que c."),
      ("Dar como hipotenusa un número menor que un cateto.", "La hipotenusa es siempre el lado mayor del triángulo rectángulo.", "Revisa el resultado: debe ser mayor que cada cateto."),
  ],
  R=[arith("Un triángulo rectángulo tiene catetos de 9 cm y 12 cm. ¿Cuánto vale c²?", "9*9+12*12", "Se suman los cuadrados de los catetos.", " cm²"),
     ex("Si c² = 100, ¿cuánto mide c?", "10", "10 × 10 = 100."),
     arith("La hipotenusa mide 5 cm y un cateto mide 3 cm. ¿Cuánto vale el cuadrado del otro cateto?", "5*5-3*3", "Se resta el cuadrado del cateto conocido al de la hipotenusa.", " cm²")],
  C=[ex("Un triángulo rectángulo tiene catetos de 15 cm y 20 cm. ¿Cuánto mide la hipotenusa?", "25 cm", "225 + 400 = 625, y 25 × 25 = 625."),
     ex("La hipotenusa de un triángulo rectángulo mide 17 cm y un cateto mide 8 cm. ¿Cuánto mide el otro cateto?", "15 cm", "289 − 64 = 225, y 15 × 15 = 225."),
     ex("Los catetos de un triángulo rectángulo miden 3 cm y 6 cm. ¿Entre qué dos enteros consecutivos está la hipotenusa?", "Entre 6 cm y 7 cm", "c² = 9 + 36 = 45, y 36 < 45 < 49.")],
  A=[ex("La hipotenusa de un triángulo rectángulo mide 25 cm y un cateto mide 7 cm. ¿Cuánto mide el otro cateto?", "24 cm", "625 − 49 = 576, y 24 × 24 = 576."),
     ex("Un triángulo rectángulo tiene catetos de 9 cm y 40 cm. ¿Cuánto mide la hipotenusa?", "41 cm", "81 + 1.600 = 1.681, y 41 × 41 = 1.681."),
     ex("La hipotenusa de un triángulo rectángulo mide 29 cm y un cateto mide 20 cm. ¿Cuánto mide el otro cateto?", "21 cm", "841 − 400 = 441, y 21 × 21 = 441.")],
  Z=[ex("Camila calculó la hipotenusa de un triángulo de catetos 5 cm y 12 cm y obtuvo 17 cm, y Diego obtuvo 13 cm. ¿Quién tiene razón, Camila o Diego?", "Diego", "25 + 144 = 169 y 13 × 13 = 169; Camila sumó los catetos en vez de sus cuadrados."),
     ex("Pedro tiene un triángulo rectángulo con hipotenusa 10 cm y un cateto 8 cm, y calculó el otro cateto como la raíz de 100 + 64. ¿Está bien su cálculo? Responde sí o no.", "No", "Debió restar: 100 − 64 = 36, y el cateto mide 6 cm.")],
  D=[ex("Un cateto de un triángulo rectángulo mide 11 cm y la hipotenusa mide 1 cm más que el otro cateto. ¿Cuánto mide la hipotenusa?", "61 cm", "Si el otro cateto es b, (b + 1)² − b² = 2b + 1 = 121, así que b = 60 y la hipotenusa es 61."),
     ex("Un rombo tiene diagonales de 16 cm y 30 cm, que se cortan en ángulo recto en su punto medio. ¿Cuánto mide el lado del rombo?", "17 cm", "El lado es la hipotenusa de un triángulo de catetos 8 cm y 15 cm: 64 + 225 = 289.")],
  ctx=[ex("Una pantalla rectangular mide 16 cm de ancho y 12 cm de alto. ¿Cuánto mide su diagonal?", "20 cm", "256 + 144 = 400, y 20 × 20 = 400.")],
  chk=[ex("Para hallar un cateto desconocido, ¿se suman o se restan los cuadrados?", "Se restan", "Como c² = a² + b², el cateto sale de c² − a²."),
       ex("La hipotenusa de un triángulo rectángulo mide 13 cm y un cateto mide 12 cm. ¿Cuánto mide el otro cateto?", "5 cm", "169 − 144 = 25, y 5 × 5 = 25."),
       arith("Los catetos de un triángulo rectángulo miden 24 cm y 7 cm. ¿Cuánto vale c²?", "24*24+7*7", "Se suman los cuadrados de los catetos.", " cm²")],
  open=("En una hoja dibuja dos triángulos rectángulos: uno de catetos 6 cm y 8 cm (halla su hipotenusa) y otro de hipotenusa 13 cm y un cateto de 5 cm (halla el otro cateto). Calcula primero con el teorema, dibuja ambos con regla y escuadra, y mide para comprobar tu cálculo con un error de hasta 2 mm.",
        "Primero: 36 + 64 = 100, c = 10 cm. Segundo: 169 − 25 = 144, cateto = 12 cm. Se midió 10,0 cm y 12,0 cm.",
        ["calcula con a² + b² = c² y con c² − a²", "dibuja con regla y escuadra", "mide y compara", "escribe si el error es de hasta 2 mm"],
        ["dos cálculos escritos", "dibujo de los triángulos", "medidas anotadas"],
        ["sumar cuando hay que restar", "no usar la escuadra para el ángulo recto", "no anotar la unidad"],
        "Pide que muestre dónde está el ángulo recto en cada dibujo. Reconoce que compare cálculo y medida."),
  reinforce="Halla la hipotenusa de un triángulo de catetos 8 cm y 15 cm y el cateto de uno con hipotenusa 10 cm y cateto 6 cm.",
  extend="Busca otro trío pitagórico distinto de 3, 4, 5 multiplicando todos sus números por 2 o por 3, y comprueba que cumple a² + b² = c².")

L(OA12, 4,
  mat=MAT_GEO,
  use="Aprenderé a aplicar el teorema de Pitágoras en problemas de la vida diaria y en el plano cartesiano, y a verificar que el resultado tiene sentido.",
  prior=["Sé hallar hipotenusa y catetos con el teorema.", "Sé ubicar puntos en el plano cartesiano."],
  explain=[
      "Para resolver un problema con Pitágoras sigue cuatro pasos: haz un dibujo, marca el ángulo recto, decide si buscas la hipotenusa (se suma) o un cateto (se resta) y comprueba que el resultado tenga sentido. En una escalera apoyada en una pared, la escalera es la hipotenusa, la pared es un cateto y el suelo es el otro cateto.",
      "En una pantalla, una cancha o una puerta rectangular, la diagonal es la hipotenusa del triángulo que forman dos lados. En el plano cartesiano, la distancia entre dos puntos es la hipotenusa de un triángulo cuyos catetos son la diferencia de las x y la diferencia de las y.",
      "La verificación es parte del trabajo: la hipotenusa debe ser mayor que cada cateto, la unidad debe ser la del enunciado y, si puedes, mide en un dibujo a escala. También puedes usar la relación al revés: si tres medidas cumplen a² + b² = c², la esquina que forman es recta, como hacen los constructores con el triángulo 3-4-5.",
  ],
  vocab=[("diagonal", "segmento que une dos vértices no consecutivos de un rectángulo"), ("distancia entre dos puntos", "largo del segmento recto que los une"), ("a escala", "dibujado con las medidas reducidas en una misma proporción"), ("verificar", "comprobar que un resultado cumple lo que pide el problema")],
  worked=[
      ("Escalera y pared", "Una escalera de 10 m se apoya en una pared con su base a 6 m de ella. ¿A qué altura llega?", ["La escalera es la hipotenusa: c = 10 m; un cateto es 6 m.", "El otro cateto: 10² − 6² = 100 − 36 = 64.", "El número que al cuadrado da 64 es 8."], "Llega a 8 m de altura"),
      ("Distancia en el plano", "¿Cuál es la distancia entre A(2, 1) y B(5, 5)?", ["Diferencia en x: 5 − 2 = 3. Diferencia en y: 5 − 1 = 4.", "d² = 3² + 4² = 9 + 16 = 25.", "d = 5 porque 5 × 5 = 25."], "La distancia es 5 unidades"),
  ],
  mist=[
      ("Dibujar la escalera como un cateto.", "La escalera es el lado frente al ángulo recto, o sea la hipotenusa.", "Marca el ángulo recto entre pared y suelo; el lado de enfrente es la escalera."),
      ("Restar las coordenadas de A y B sin elevarlas al cuadrado y dar 7 como distancia entre (2, 1) y (5, 5).", "La distancia es la hipotenusa, no la suma de las diferencias.", "Calcula dx² + dy² y busca la raíz cuadrada."),
  ],
  R=[ex("Un cable une la punta de un poste de 12 m con un punto del suelo a 5 m de la base del poste. ¿Cuánto mide el cable?", "13 m", "144 + 25 = 169, y 13 × 13 = 169."),
     ex("En un problema de escalera apoyada en una pared, ¿qué parte de la figura es la hipotenusa?", "La escalera", "La escalera queda frente al ángulo recto que forman la pared y el suelo."),
     ex("Si calculas la hipotenusa de un triángulo y te da menor que uno de los catetos, ¿qué debes pensar?", "Que hay un error", "La hipotenusa siempre es mayor que cada cateto.")],
  C=[ex("Una cancha rectangular mide 24 m de ancho y 32 m de largo. ¿Cuánto mide su diagonal?", "40 m", "576 + 1.024 = 1.600, y 40 × 40 = 1.600."),
     ex("Una rampa de 13 m de largo sube 5 m de altura. ¿Qué distancia horizontal recorre?", "12 m", "169 − 25 = 144, y 12 × 12 = 144."),
     ex("¿Cuál es la distancia entre P(1, 2) y Q(7, 10)?", "10 unidades", "Los catetos son 6 y 8: 36 + 64 = 100.")],
  A=[ex("Dos amigos salen del mismo punto: uno camina 12 m hacia el norte y el otro 35 m hacia el este. ¿A qué distancia en línea recta quedan?", "37 m", "144 + 1.225 = 1.369, y 37 × 37 = 1.369."),
     ex("Una puerta mide 90 cm de ancho y 120 cm de alto. ¿Cuánto mide su diagonal?", "150 cm", "8.100 + 14.400 = 22.500, y 150 × 150 = 22.500."),
     ex("Desde un punto del suelo, la punta de un edificio está a 41 m en línea recta y la base a 9 m. ¿Qué altura tiene el edificio?", "40 m", "1.681 − 81 = 1.600, y 40 × 40 = 1.600.")],
  Z=[ex("Un carpintero mide en un marco dos lados de 50 cm y 120 cm y una diagonal de 130 cm. ¿El marco está en escuadra, es decir, con ángulo recto? Responde sí o no.", "Sí", "2.500 + 14.400 = 16.900, que es 130 × 130."),
     ex("Marta dice que una escalera de 5 m, con su base a 3 m de la pared, alcanza 6 m de altura. ¿Es posible? Responde sí o no.", "No", "La altura es la raíz de 25 − 9 = 16, o sea 4 m, no 6 m.")],
  D=[arith("De A a B hay 15 m al este y 8 m al norte. Caminando por las dos esquinas se recorren 23 m, y cortando en diagonal se recorren 17 m. ¿Cuántos metros se ahorran?", "(15+8)-17", "La diagonal es la hipotenusa (225 + 64 = 289, o sea 17 m); se resta de los 23 m.", " m"),
     ex("En un mapa a escala, 1 cm representa 10 m. Un camino sube 6 cm y se desplaza 8 cm a un lado. ¿Cuántos metros mide la ruta recta en la realidad?", "100 m", "La ruta recta mide 10 cm en el mapa (36 + 64 = 100), es decir 100 m.")],
  ctx=[ex("Un cable sujeta un mástil de 21 m desde un punto del suelo a 20 m de la base. ¿Cuánto mide el cable?", "29 m", "441 + 400 = 841, y 29 × 29 = 841.")],
  chk=[ex("¿Qué lado es siempre el mayor en un triángulo rectángulo?", "La hipotenusa", "Está frente al ángulo recto, que es el mayor."),
       ex("Una escalera de 13 m tiene su base a 5 m de la pared. ¿A qué altura llega?", "12 m", "169 − 25 = 144, y 12 × 12 = 144."),
       ex("Si los catetos están en metros, ¿en qué unidad queda la hipotenusa?", "En metros", "La hipotenusa se mide con la misma unidad que los catetos.")],
  open=("Elige una caja o un cuaderno rectangular de tu casa, mide con regla su largo y su ancho, y calcula con Pitágoras la diagonal de la tapa. Luego mide esa diagonal con la regla y compara. Anota las tres medidas, el cálculo y cuánto se diferencian. Si tienes un programa de geometría, también puedes verificar con él.",
        "Largo 20 cm, ancho 15 cm: 400 + 225 = 625, diagonal 25 cm. Medí 25,1 cm; la diferencia es de 1 mm.",
        ["mide largo y ancho", "calcula la diagonal con Pitágoras", "mide la diagonal", "compara y concluye"],
        ["tres medidas anotadas", "cálculo escrito", "frase de comparación"],
        ["medir con la regla mal puesta", "olvidar elevar al cuadrado", "no anotar unidades"],
        "Pide que dibuje el triángulo con el ángulo recto marcado. Reconoce que analice la diferencia entre cálculo y medida."),
  reinforce="Calcula la diagonal de una hoja de 21 cm por 28 cm y mídela para ver si coincide.",
  extend="Explica cómo un constructor puede usar un cordel con nudos a 3, 4 y 5 unidades para trazar una esquina recta.")
