"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS02: reconocer en el contexto sonidos propios de la lengua indígena. No se enseñan sonidos ni letras de
ninguna lengua indígena: se entrena la escucha, la observación de la boca y el contraste con palabras en
castellano. La única expresión indígena usada es el saludo «mari mari» (mapuzugun). La pronunciación real la
enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_content_lc_c1 import task, w
from student_lessons import ex, register

S2 = "LC01 OA LS02"

register(
    S2, 1,
    materials="Un adulto que lea las palabras en voz alta; hoja y lápiz. Las listas están escritas aquí.",
    use="Aprenderé a escuchar con atención un sonido antes de repetirlo. Sirve para reconocer sonidos en palabras de la lengua de un pueblo con respeto.",
    prior=["Sé decir mi nombre.", "Sé que cada lengua tiene sus propios sonidos."],
    explain=[
        "Cada lengua tiene sonidos propios. Algunos se parecen a los del castellano y otros no. Por eso primero escucho, y solo después, si me lo piden, repito. Escuchar bien es la mitad de aprender.",
        "Los sonidos aparecen en palabras de la vida diaria: partes del cuerpo, colores, números, comidas, elementos de la naturaleza y nombres de lugares. Hoy practico con palabras en castellano para entrenar el oído. Con palabras de una lengua indígena, escucho al educador o a la educadora tradicional.",
        "Una expresión que sí conocemos con seguridad es el saludo «mari mari», del mapuzugun. Cuando alguien lo dice, escucho cuántas veces lo dice y en qué momento. No invento otras palabras ni adivino cómo suenan.",
    ],
    vocab=[("sonido", "lo que oigo cuando alguien habla"), ("lengua", "forma de hablar de un pueblo"), ("primer sonido", "con el que empieza una palabra"), ("mari mari", "saludo en mapuzugun"), ("repetir", "decir otra vez lo que oí")],
    worked=[
        w("Primer sonido", "Un adulto dice «mesa». ¿Con qué sonido empieza: m o s?", ["Escucho despacio: m-e-sa.", "Lo primero que oigo es m."], "m"),
        w("Mismo sonido", "Palabras: mano, mesa, sapo. ¿Cuáles empiezan con el mismo sonido?", ["Escucho el inicio de cada una.", "Mano y mesa empiezan con m.", "Sapo empieza con s."], "mano y mesa"),
    ],
    mistakes=[
        {"wrong": "Repetir rápido sin escuchar.", "why": "Cambio el sonido sin darme cuenta.", "fix": "Escucho dos veces antes de repetir."},
        {"wrong": "Inventar cómo suena una palabra que no conozco.", "why": "Puedo equivocarme y faltar el respeto.", "fix": "Pido que el educador tradicional la diga."},
    ],
    tiers={
        "recovery": [
            ex("Un adulto dice «luna». ¿Con qué sonido empieza: l o n?", "l", "La primera parte que se oye es l."),
            ex("Antes de repetir un sonido, ¿escucho o hablo?", "escucho", "Primero se escucha."),
            ex("«Mari mari» es un saludo en mapuzugun. ¿Verdadero o falso?", "Verdadero", "Es un saludo conocido."),
        ],
        "understand": [
            ex("¿Cada lengua tiene sonidos propios?", "Sí", "Son parte de su identidad."),
            ex("Verdadero o falso: puedo adivinar cómo suena una palabra de una lengua que no conozco.", "Falso", "Hay que escuchar a quien la habla."),
            ex("¿Quién me enseña los sonidos de una lengua indígena: el educador tradicional o mi imaginación?", "el educador tradicional", "Él o ella conoce la lengua."),
        ],
        "apply": [
            ex("Palabras: pie, pelo, ojo. ¿Cuáles empiezan con el mismo sonido?", "pie y pelo", "Ambas empiezan con p."),
            ex("Palabras que nombran partes del cuerpo: mano, rojo, nariz. ¿Cuáles son partes del cuerpo?", "mano y nariz", "Rojo es un color."),
            ex("Guion: «Mari mari. Hola. Mari mari». ¿Cuántas veces se oye el saludo?", "2", "Aparece dos veces."),
        ],
        "reason": [
            ex("Un compañero dice «seguro suena así» sobre una palabra que no conoce. ¿Qué le dices?", "que escuche al educador tradicional", "No se adivina un sonido."),
            ex("¿Por qué escucho dos veces antes de repetir?", "para no cambiar el sonido", "La segunda escucha confirma."),
        ],
        "challenge": [
            ex("Lista: sol, mar, luna, nube. ¿Cuántas palabras nombran elementos de la naturaleza?", "4", "Las cuatro son elementos de la naturaleza."),
            ex("Lista: rojo, azul, mano, verde. ¿Cuántas son colores?", "3", "Rojo, azul y verde son colores."),
        ],
    },
    context=[ex("Una visita dice «mari mari» al entrar a tu sala. ¿Qué haces primero: escuchar o responder inventando una palabra?", "escuchar", "Primero se escucha con atención.")],
    selfcheck=[ex("¿Qué hago antes de repetir?", "escucho", "Escuchar es lo primero."), ex("¿Con qué empieza «mesa»?", "m", "La primera es m."), ex("¿Quién me enseña los sonidos de la lengua de un pueblo?", "el educador tradicional o la comunidad", "Ellos la hablan.")],
    open_task=task(
        "Pide a un adulto que diga estas palabras en castellano: A) mesa, mano, sol B) luna, lana, sapo. Escribe cuáles empiezan con el mismo sonido. Después dibuja la boca de quien habla y escribe una pregunta al educador/a tradicional sobre un saludo de su pueblo que puedan enseñar.",
        "En A, mesa y mano empiezan con m. Pregunta: ¿cómo se saluda en la lengua de su pueblo?",
        ["reconoce el primer sonido", "no inventa sonidos de otra lengua", "pregunta al educador/a tradicional o a la comunidad"],
        ["lista escrita", "pregunta"],
        ["adivinar sonidos", "repetir sin escuchar"],
        "Verifica la respuesta (A: mesa y mano; B: luna y lana); si inventó sonidos, vuelve a la regla de escuchar primero.",
    ),
    reinforce="Pide a alguien que diga cinco palabras y señala cuáles empiezan igual.",
    extend="Escucha en casa tres palabras que empiecen con el mismo sonido que tu nombre.",
)

register(
    S2, 2,
    materials="Un espejo o la mano frente a la boca; hoja y lápiz. Todo se practica con palabras en castellano.",
    use="Aprenderé a observar cómo se mueve la boca al hablar, con respeto y sin burlas. Sirve para entender que cada sonido se produce de una forma.",
    prior=["Sé identificar el primer sonido de una palabra.", "Sé nombrar partes de la cara."],
    explain=[
        "Los sonidos se producen con la boca, la lengua, los labios y el aire. Si digo «mamá» y miro mis labios, veo que se juntan. Si digo «a» con la boca abierta, los labios se separan. Eso se puede observar.",
        "Observar cómo hablan otras personas es una forma de aprender, pero nunca para imitar de manera exagerada ni para burlarse. Imitar una lengua como broma es una caricatura y falta el respeto. Mi observación es seria y cuidadosa.",
        "Con una lengua indígena, observo cómo la dice el educador o la educadora tradicional y espero que me inviten a repetir. No invento ni exagero. Hoy practico solo con sonidos del castellano.",
    ],
    vocab=[("labios", "bordes de la boca"), ("lengua (en la boca)", "parte blanda que se mueve al hablar"), ("aire", "lo que sale cuando hablo"), ("caricatura", "imitar exagerando para burlarse"), ("articulación", "cómo se mueve la boca al decir un sonido")],
    worked=[
        w("Labios juntos", "Digo «mamá» frente al espejo. ¿Los labios se juntan en la m?", ["Digo m despacio.", "Miro mis labios.", "Se juntan."], "sí"),
        w("Boca abierta", "Digo «a» largo. ¿La boca está abierta o cerrada?", ["Digo aaa.", "Miro mi boca."], "abierta"),
    ],
    mistakes=[
        {"wrong": "Imitar con voz exagerada una lengua indígena.", "why": "Es caricatura y ofende.", "fix": "Observo en serio y espero la invitación."},
        {"wrong": "Mirar la boca de una persona sin que lo note, para copiar.", "why": "Puedo incomodarla.", "fix": "Observo cuando me la muestran para enseñar."},
    ],
    tiers={
        "recovery": [
            ex("Al decir «mamá», ¿los labios se juntan?", "Sí", "La m se hace juntando los labios."),
            ex("Al decir «a», ¿la boca se abre?", "Sí", "La a se hace con la boca abierta."),
            ex("¿Con qué hablo: con la boca o con los pies?", "con la boca", "La boca produce los sonidos."),
        ],
        "understand": [
            ex("¿Qué es una caricatura de una lengua?", "imitarla exagerando para burlarse", "Ofende al pueblo."),
            ex("Verdadero o falso: puedo burlarme para recordar mejor.", "Falso", "Burlarse falta el respeto."),
            ex("¿Observo en serio o en broma?", "en serio", "Es una forma de aprender."),
        ],
        "apply": [
            ex("Di «papá» frente al espejo. ¿Cuántas veces juntas los labios (una por cada p)?", "2", "Hay dos p en «papá»."),
            ex("Di «bebé». ¿Cuántas veces juntas los labios (una por cada b)?", "2", "Hay dos b."),
            ex("Di «sol». ¿Los labios se juntan con la s?", "No", "La s no se hace juntando los labios."),
        ],
        "reason": [
            ex("Un niño imita con exageración la forma de hablar de un pueblo para hacer reír. ¿Está bien?", "No", "Es una caricatura."),
            ex("¿Por qué espero a que me inviten a repetir un sonido de una lengua indígena?", "porque no debo inventar ni exagerar", "Primero se aprende de quien la habla."),
        ],
        "challenge": [
            ex("Palabras: mamá, sol, papá, luna. ¿En cuántas se juntan los labios al empezar?", "2", "Mamá y papá empiezan juntando los labios."),
            ex("En «mamá» y en «papá», ¿cuántos sonidos con labios juntos hay en total?", "4", "Hay dos en cada palabra."),
        ],
    },
    context=[ex("Un familiar habla una lengua originaria y te dice una palabra. Tu primo se ríe y la imita exagerando. ¿Qué le dices?", "que no se burle y que escuche", "Respeta a la persona y a la lengua.")],
    selfcheck=[ex("¿Qué junto al decir m?", "los labios", "La m se hace con labios juntos."), ex("¿Imito exagerando una lengua?", "No", "Eso es una caricatura ofensiva."), ex("¿Quién me invita a repetir una palabra de la lengua?", "el educador tradicional o la persona que la habla", "Ellos enseñan la lengua.")],
    open_task=task(
        "Frente a un espejo o con la mano delante de la boca, di estas palabras: A) mamá B) papá C) sol. Escribe en cuáles los labios se juntan al empezar. Dibuja tu boca en un caso. Escribe una pregunta al educador/a tradicional sobre cómo aprender sonidos de su lengua con respeto.",
        "Se juntan en mamá y papá. Dibujé mi boca diciendo m. Pregunta: ¿cómo podemos aprender sus sonidos sin burlarnos?",
        ["observa con seriedad", "responde correctamente (A y B)", "pregunta al educador/a tradicional o a la comunidad"],
        ["dibujo", "lista escrita"],
        ["burlarse", "exagerar"],
        "Confirma A y B; si hizo caricatura, recuerda que se observa en serio.",
    ),
    reinforce="Di tres palabras con m y mira tus labios.",
    extend="Explica a alguien de casa por qué no se debe imitar en broma una lengua.",
)

register(
    S2, 3,
    materials="Un adulto para leer; hoja y lápiz. Las palabras de práctica están en castellano.",
    use="Aprenderé a unir una palabra con lo que significa y con la situación en que se usa. Sirve para entender que los sonidos llevan significado.",
    prior=["Sé nombrar partes del cuerpo, colores y números.", "Sé que mari mari es un saludo."],
    explain=[
        "Un sonido o una palabra no está sola: tiene un significado y se usa en situaciones. «Mano» significa una parte del cuerpo. «Rojo» significa un color. «Mari mari» es un saludo y se dice al encontrarse con alguien.",
        "Para reconocer una palabra verificada, me hago dos preguntas: ¿qué significa? ¿cuándo se dice? Si no sé la respuesta, no la invento: se la pregunto al educador o a la educadora tradicional.",
        "Las palabras de las lenguas indígenas también se agrupan por temas: cuerpo, colores, números, alimentos o naturaleza. Hoy practico agrupar palabras en castellano para entrenar el oído y el pensamiento.",
    ],
    vocab=[("significado", "lo que quiere decir una palabra"), ("situación", "momento en que algo se dice"), ("saludo", "palabra para encontrarse con alguien"), ("tema", "grupo de palabras parecidas"), ("verificada", "comprobada con una fuente")],
    worked=[
        w("Agrupar", "Palabras: mano, pie, rojo. ¿Cuáles son partes del cuerpo?", ["Pienso en el cuerpo.", "Mano y pie son partes del cuerpo.", "Rojo es un color."], "mano y pie"),
        w("Cuándo se dice", "«Mari mari» es un saludo. ¿Se dice al llegar o al dormir?", ["Un saludo se dice al encontrarse con alguien.", "Entonces es al llegar."], "al llegar"),
    ],
    mistakes=[
        {"wrong": "Decir un saludo cuando no corresponde.", "why": "Cada expresión tiene su momento.", "fix": "Pregunto cuándo se dice."},
        {"wrong": "Inventar el significado de una palabra que no conozco.", "why": "Puede estar equivocado.", "fix": "Pregunto al educador tradicional."},
    ],
    tiers={
        "recovery": [
            ex("«Rojo» es un color. ¿Verdadero o falso?", "Verdadero", "Rojo nombra un color."),
            ex("«Mano» es una parte del cuerpo. ¿Verdadero o falso?", "Verdadero", "La mano es parte del cuerpo."),
            ex("«Mari mari» es un saludo. ¿Se dice al encontrarse o al comer?", "al encontrarse", "Los saludos se dicen al encontrarse."),
        ],
        "understand": [
            ex("¿Qué es el significado de una palabra?", "lo que quiere decir", "Dice qué representa."),
            ex("Si no conozco el significado de una palabra, ¿la invento o pregunto?", "pregunto", "No debo inventar significados."),
            ex("¿Qué dos preguntas hago sobre una palabra?", "qué significa y cuándo se dice", "Así la entiendo en su situación."),
        ],
        "apply": [
            ex("Palabras: verde, ojo, azul, nariz. ¿Cuáles son colores?", "verde y azul", "Los otros son partes del cuerpo."),
            ex("Palabras: uno, dos, sol, tres. ¿Cuántas son números?", "3", "Uno, dos y tres son números."),
            ex("Palabras: pan, agua, luna, río. ¿Cuáles son elementos de la naturaleza?", "agua, luna y río", "El pan es un alimento."),
        ],
        "reason": [
            ex("Una compañera dice «mari mari» al despedirse. ¿Es lo correcto, si es un saludo para encontrarse?", "No", "No corresponde a la situación."),
            ex("¿Por qué conviene saber cuándo se dice una expresión?", "porque cada expresión tiene su momento", "Así se usa con respeto."),
        ],
        "challenge": [
            ex("Palabras: mano, rojo, uno, pie, azul, dos. ¿Cuántas son partes del cuerpo?", "2", "Mano y pie."),
            ex("Mismo grupo: mano, rojo, uno, pie, azul, dos. ¿Cuántas son colores?", "2", "Rojo y azul."),
        ],
    },
    context=[ex("Llega una visita a tu escuela y la saludan con «mari mari». ¿Para qué se dijo esa expresión?", "para saludar", "Es un saludo.")],
    selfcheck=[ex("En la lengua mapuzugun, «mari mari» ¿es un saludo o una despedida?", "un saludo", "Se usa para saludar al llegar."), ex("¿Qué hago si no sé un significado?", "pregunto", "No invento, pregunto."), ex("¿A qué tema pertenece «rojo»?", "colores", "Rojo es un color.")],
    open_task=task(
        "Clasifica estas ocho palabras en castellano en tres grupos: cuerpo, colores y naturaleza. Palabras: mano, verde, río, ojo, azul, sol, pie, rojo. Dibuja una tabla de tres columnas. Después pregunta al educador/a tradicional si hay palabras de su lengua que se puedan compartir sobre alguno de esos temas.",
        "Cuerpo: mano, ojo, pie. Colores: verde, azul, rojo. Naturaleza: río, sol. Pregunta: ¿qué palabra de su lengua podemos aprender sobre el sol?",
        ["clasifica correctamente", "no inventa palabras de otra lengua", "pregunta al educador/a tradicional o a la comunidad"],
        ["tabla", "pregunta"],
        ["mezclar grupos", "inventar palabras"],
        "Compara con la clasificación correcta; si inventó palabras, pídele reemplazarlas por una pregunta.",
    ),
    reinforce="Agrupa cinco palabras de tu casa por temas.",
    extend="Cuenta a alguien de casa qué significa «mari mari» y cuándo se dice.",
)

register(
    S2, 4,
    materials="Un adulto para leer; hoja y lápiz.",
    use="Aprenderé a comparar sonidos con cuidado y a no escribir con letras del castellano los sonidos de otra lengua. Sirve para respetar cómo se escriben y suenan las lenguas indígenas.",
    prior=["Sé que cada lengua tiene sus sonidos.", "Sé decir primer sonido de una palabra."],
    explain=[
        "Contrastar es comparar para ver qué se parece y qué cambia. Incluso en castellano, una misma letra puede sonar distinto. La letra c suena diferente en «casa» y en «cena». La letra g suena diferente en «gato» y en «gente».",
        "Por eso no puedo suponer que un sonido de otra lengua se escribe como lo escribiría en castellano. Cada lengua tiene sus propias formas de escribirse. Si escribo con mis propias letras lo que oigo, puedo cambiar la palabra.",
        "Cuando el educador o la educadora tradicional me muestre cómo se escribe una palabra de su lengua, la copio tal como está. Mientras no la tenga, digo «no sé cómo se escribe» y lo pregunto.",
    ],
    vocab=[("contrastar", "comparar para ver qué cambia"), ("letra", "signo que se usa al escribir"), ("sonido", "lo que oigo"), ("escritura", "forma de escribir una lengua"), ("copiar tal como está", "escribir igual que el modelo")],
    worked=[
        w("Contraste en castellano", "En «casa» y «cena», ¿la c suena igual?", ["Digo casa: c suena fuerte.", "Digo cena: c suena como s.", "No suena igual."], "no suena igual"),
        w("No suponer", "Oigo una palabra de otra lengua y la escribo con letras del castellano. ¿Es seguro?", ["No sé si esa letra representa ese sonido.", "No es seguro."], "no es seguro"),
    ],
    mistakes=[
        {"wrong": "Escribir a mi manera una palabra de una lengua indígena.", "why": "Puedo cambiar la palabra.", "fix": "Copio solo lo que me muestran escrito."},
        {"wrong": "Pensar que una letra suena siempre igual.", "why": "En castellano mismo cambia.", "fix": "Escucho cada palabra."},
    ],
    tiers={
        "recovery": [
            ex("En «gato», la g suena fuerte. En «gente», ¿suena igual?", "No", "En gente suena distinto."),
            ex("Contrastar es comparar. ¿Verdadero o falso?", "Verdadero", "Eso significa contrastar."),
            ex("¿La c de «casa» suena como la c de «cena»?", "No", "Suenan distinto en cada palabra."),
        ],
        "understand": [
            ex("¿Puedo escribir con letras del castellano una palabra de otra lengua que oí?", "No sin que me la enseñen", "Podría cambiar la palabra."),
            ex("¿Quién me puede mostrar cómo se escribe una palabra de su lengua?", "el educador tradicional", "Conoce la escritura."),
            ex("Si no sé cómo se escribe, ¿qué digo?", "no sé cómo se escribe", "Es una respuesta honesta."),
        ],
        "apply": [
            ex("Palabras: casa, cine, codo. ¿En cuáles suena la c como k?", "casa y codo", "Con a y o suena fuerte."),
            ex("Palabras: gato, gente, gota. ¿En cuántas suena la g fuerte?", "2", "Gato y gota."),
            ex("Palabras: cena, cielo, casa. ¿En cuántas suena la c como s?", "2", "Cena y cielo."),
        ],
        "reason": [
            ex("Un compañero escribe a su manera lo que oyó a una persona de la comunidad. ¿Qué le propones?", "preguntar cómo se escribe", "Así no cambia la palabra."),
            ex("¿Por qué una letra del castellano puede no servir para otra lengua?", "porque cada lengua tiene sus sonidos", "No coinciden siempre."),
        ],
        "challenge": [
            ex("Lista: gato, gente, casa, cena, gota, cielo. ¿Cuántas palabras tienen la letra c o g con sonido suave (como s o j)?", "3", "Gente, cena y cielo."),
            ex("Mismo lista: gato, gente, casa, cena, gota, cielo. ¿Cuántas tienen c o g con sonido fuerte?", "3", "Gato, casa y gota."),
        ],
    },
    context=[ex("Una persona de la comunidad te dice una palabra. Tú quieres escribirla en tu cuaderno. ¿Qué haces: escribirla como tú oyes o pedirle que te la muestre escrita?", "pedirle que me la muestre escrita", "Así la copio tal como es.")],
    selfcheck=[ex("¿Qué es contrastar?", "comparar", "Ver qué cambia."), ex("¿Escribo a mi manera una palabra de otra lengua?", "No", "Podría cambiarla sin querer."), ex("¿A quién pido que me la muestre escrita?", "al educador tradicional o a la comunidad", "Ellos la conocen.")],
    open_task=task(
        "Pide a un adulto que diga estas palabras en castellano: casa, cena, gato, gente. Escribe cuáles tienen sonido fuerte (c como k y g fuerte) y cuáles suave. Luego escribe una pregunta al educador/a tradicional sobre cómo se escriben las palabras de su lengua.",
        "Fuertes: casa, gato. Suaves: cena, gente. Pregunta: ¿cómo se escribe la palabra de su lengua que nos enseñarán?",
        ["contrasta correctamente", "no inventa escritura", "pregunta al educador/a tradicional o a la comunidad"],
        ["lista", "pregunta"],
        ["escribir a su manera una palabra de otra lengua", "suponer"],
        "Confirma la clasificación; si escribió palabras de otra lengua a su manera, recuerda pedir el modelo escrito.",
    ),
    reinforce="Encuentra dos palabras donde la c suene distinto.",
    extend="Explica a alguien de casa por qué la g de «gato» y de «gente» suenan distinto.",
)

register(
    S2, 5,
    materials="Un adulto para leer; hoja y lápiz. Practico con palabras en castellano.",
    use="Aprenderé a ensayar un sonido paso a paso, respetando mi etapa de aprendizaje. Sirve para aprender sin presión y con cuidado.",
    prior=["Sé escuchar y observar la boca.", "Sé contar sílabas con palmas."],
    explain=[
        "Reproducir un sonido se hace paso a paso: escucho, observo y repito despacio. Después repito un poco más rápido. Si me equivoco, no pasa nada, vuelvo a escuchar. Aprender lleva tiempo.",
        "Puedo contar las sílabas con palmas. «Ma-ri» tiene dos sílabas, y «ma-ri ma-ri» tiene cuatro, escrito de esa manera. Contar ayuda a seguir el ritmo, pero la pronunciación exacta la enseña el educador o la educadora tradicional.",
        "Respeto mi etapa: no tengo que decir todo perfecto ni inventar palabras. Si me invitan a repetir, repito lo que me enseñan, con respeto. Si no, escucho y aprendo con los ojos y los oídos.",
    ],
    vocab=[("ensayar", "practicar paso a paso"), ("sílaba", "golpe de voz en una palabra"), ("despacio", "con calma"), ("etapa", "momento de mi aprendizaje"), ("invitación", "cuando me piden participar")],
    worked=[
        w("Contar sílabas", "¿Cuántas sílabas tiene «mariposa» (ma-ri-po-sa)?", ["Aplaudo en cada golpe: ma, ri, po, sa.", "Cuento las palmas: cuatro."], "4 sílabas"),
        w("Pasos para ensayar", "Ordena: repito, escucho, observo.", ["Primero escucho.", "Luego observo.", "Por último repito."], "escucho, observo, repito"),
    ],
    mistakes=[
        {"wrong": "Querer decir todo perfecto desde el primer intento.", "why": "Aprender lleva tiempo.", "fix": "Ensayo despacio y vuelvo a escuchar."},
        {"wrong": "Repetir una palabra de otra lengua sin que me inviten.", "why": "Puede no corresponder.", "fix": "Espero la invitación."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué hago primero para ensayar un sonido: escucho o repito?", "escucho", "Primero se escucha."),
            ex("¿Cuántas sílabas tiene «luna» (lu-na)?", "2", "Lu y na."),
            ex("Si me equivoco, ¿vuelvo a escuchar?", "Sí", "Así aprendo con calma."),
        ],
        "understand": [
            ex("¿Tengo que decir todo perfecto al primer intento?", "No", "Aprender lleva tiempo."),
            ex("¿Quién enseña la pronunciación exacta de una lengua indígena?", "el educador tradicional", "Conoce la lengua."),
            ex("Verdadero o falso: puedo repetir una palabra de otra lengua sin que me inviten.", "Falso", "Espero la invitación."),
        ],
        "apply": [
            ex("¿Cuántas sílabas tiene «mariposa» (ma-ri-po-sa)?", "4", "Ma, ri, po y sa."),
            ex("¿Cuántas sílabas tiene «mano» (ma-no)?", "2", "Ma y no."),
            ex("Si escribo «ma-ri ma-ri», ¿cuántas sílabas cuento?", "4", "Son cuatro golpes."),
        ],
        "reason": [
            ex("Un niño dice una palabra de otra lengua inventada. ¿Qué le dirías?", "que escuche al educador tradicional", "No debe inventar."),
            ex("¿Por qué ensayo despacio?", "para no cambiar el sonido", "Así lo cuido."),
        ],
        "challenge": [
            ex("Palabras: mesa (me-sa), sol (sol), mariposa (ma-ri-po-sa). ¿Cuántas sílabas hay en total?", "7", "2 + 1 + 4 = 7.", ),
            ex("Con «ma-ri» dos veces, ¿cuántas palmas das?", "4", "Dos palmas por cada ma-ri."),
        ],
    },
    context=[ex("Una persona mayor de la comunidad te invita a repetir un saludo. Lo haces despacio. ¿Está bien equivocarte?", "Sí", "Aprender lleva tiempo y se puede volver a ensayar.")],
    selfcheck=[ex("¿Cuál es el orden de los pasos?", "escucho, observo y repito", "Es el orden del ensayo."), ex("¿Cuántas sílabas tiene «luna»?", "2", "Lu y na."), ex("¿Quién me enseña la pronunciación exacta de una palabra indígena?", "el educador tradicional o la comunidad", "Ellos la saben.")],
    open_task=task(
        "Elige una palabra para ensayar: A) mariposa B) luna C) mano. Escúchala, observa la boca de quien la dice y repítela despacio. Cuenta las sílabas con palmas y escribe cuántas son. Pregunta al educador/a tradicional si te puede invitar a repetir un saludo de su pueblo.",
        "Elegí mariposa: 4 sílabas. Pregunta: ¿podemos ensayar un saludo de su lengua con usted?",
        ["sigue los pasos", "cuenta sílabas", "pregunta al educador/a tradicional o a la comunidad"],
        ["palmas", "número escrito"],
        ["querer hacerlo perfecto", "repetir sin invitación"],
        "Celebra el esfuerzo (A: 4, B: 2, C: 2); recuerda que no se espera perfección.",
    ),
    reinforce="Cuenta con palmas las sílabas de tres palabras de tu casa.",
    extend="Enseña a alguien de casa los tres pasos para ensayar un sonido.",
)
