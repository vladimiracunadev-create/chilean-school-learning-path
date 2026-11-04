"""Student material for 1.º medio Música, OA 04 (interpretar repertorio diverso a una y más voces con precisión técnica y fluidez, usando medios de registro y transmisión en la gestión y presentación del quehacer musical).

Todas las piezas, partituras y programas de los ejercicios son inventados («de ejemplo»); el repertorio real lo selecciona el docente.
"""
from __future__ import annotations

from student_content_mu_m1_a import L
from student_lessons import arith, ex

OA4 = "MU1M OA 04"

LEY = ("corchea = 1 unidad; negra = 2 unidades; blanca = 4; redonda = 8; un compás de 4 pulsos tiene 8 unidades; "
       "cada silencio dura lo mismo que su figura")

# ---------------------------------------------------------------- OA 04 · clase 1 (precisión técnica)
L(
    OA4, 1,
    f"Lápiz y papel. Tabla de duraciones de ejemplo, que se repite en los ejercicios: {LEY}. Para practicar, basta con palmas suaves o tarareo.",
    "Aprenderé qué es la precisión técnica al interpretar (afinación, precisión rítmica y pulso estable) y a comprobar si un compás está completo usando duraciones. Sirve para cantar y tocar con exactitud y sin perderme.",
    ["Sé que el pulso es el latido regular de la música.", "Sé que la melodía es una sucesión de notas.", "Sé sumar y restar números pequeños."],
    [
        "Interpretar con precisión técnica significa que lo que se canta o toca coincide con lo que está escrito o acordado. Tiene tres partes. La afinación es producir la altura justa de cada nota: cantar más bajo o más alto que la nota pedida es desafinar. La precisión rítmica es dar a cada nota su duración exacta y entrar en el momento que corresponde. El pulso estable es mantener un latido parejo, sin acelerar ni frenar sin querer.",
        "Las duraciones se pueden sumar. En este cuaderno usamos unidades: corchea = 1, negra = 2, blanca = 4 y redonda = 8. En un compás de 4 pulsos caben 8 unidades. Si un compás tiene negra, negra y blanca, suma 2 + 2 + 4 = 8 y está completo. Si suma menos, falta duración; si suma más, sobra. Los silencios también suman: un silencio de negra vale lo mismo que una negra.",
        "Para practicar con precisión conviene cantar o tocar despacio, con un pulso marcado con palmas o con el pie. Se revisa cada compás y se corrige un error por vez. La fluidez, es decir, la continuidad sin detenerse, llega después de la precisión: primero se hace bien y lento, y luego se hace bien y fluido. Un instrumento o una voz bien cuidados también ayudan: nada de forzar la garganta ni golpear los instrumentos.",
    ],
    [("precisión técnica", "interpretar con la altura, la duración y el pulso correctos"), ("afinación", "producir la altura justa de cada nota"), ("desafinar", "cantar o tocar más alto o más bajo que la nota pedida"), ("unidad", "medida de duración que usamos en este cuaderno para sumar figuras"), ("fluidez", "continuidad al interpretar, sin detenerse")],
    [
        ("Comprobar un compás", f"Tabla: {LEY}. Un compás de 4 pulsos tiene negra, negra y blanca. ¿Está completo?", ["Se suman las unidades: 2 + 2 + 4 = 8.", "Un compás de 4 pulsos tiene 8 unidades."], "Sí, está completo"),
        ("Ver lo que falta", f"Tabla: {LEY}. Un compás de 4 pulsos tiene negra, negra, negra y corchea. ¿Cuánto falta?", ["2 + 2 + 2 + 1 = 7.", "Faltan 8 − 7 = 1 unidad."], "Falta 1 unidad, o sea una corchea"),
    ],
    [
        ("Acelerar sin darse cuenta cuando la parte es fácil.", "El pulso debe mantenerse parejo; si se acelera, el grupo se descoordina.", "Marca el pulso con palmas o con el pie."),
        ("Querer tocar rápido antes de tocar bien.", "La velocidad sin precisión fija errores.", "Primero lento y exacto; luego se sube el tempo."),
    ],
    [
        ex(f"Tabla: {LEY}. ¿Cuántas unidades vale una blanca?", "4", "Así lo indica la tabla."),
        ex("Cantar una nota más baja que la pedida, ¿es afinar bien o desafinar?", "Desafinar", "La altura no coincide con la pedida."),
        ex(f"Tabla: {LEY}. ¿Cuántas unidades tiene un compás de 4 pulsos?", "8", "Así lo indica la tabla."),
    ],
    [
        ex(f"Tabla: {LEY}. ¿Qué compás está completo, en un compás de 4 pulsos? A) Blanca, corchea, corchea y negra. B) Blanca, blanca y corchea.", "A", "4 + 1 + 1 + 2 = 8; en cambio 4 + 4 + 1 = 9 se pasa."),
        ex("¿Qué es la precisión rítmica? A) Dar a cada nota su duración exacta y entrar en el momento justo. B) Cantar siempre fuerte.", "A", "Se refiere a la duración y el momento, no al volumen."),
        ex("Una pieza de ejemplo debe ir a pulso parejo, pero el grupo aprieta el paso en la parte final. ¿Qué falla? A) El pulso estable. B) La afinación.", "A", "Acelerar sin querer rompe el pulso estable."),
    ],
    [
        arith(f"Tabla: {LEY}. ¿Cuántas negras caben en un compás de 4 pulsos?", "8//2", "Se divide el total de unidades del compás entre las unidades de una negra.", " negras"),
        ex(f"Tabla: {LEY}. Se reúnen 5 blancas. ¿Cuántos compases completos de 4 pulsos forman y cuántas unidades sobran?", "2 compases y sobran 4 unidades", "5 blancas son 20 unidades; 20 = 8 + 8 + 4."),
        ex(f"Tabla: {LEY}. Un compás tiene blanca, negra y silencio de negra. ¿Está completo?", "Sí", "4 + 2 + 2 = 8; el silencio suma lo mismo que su figura."),
    ],
    [
        ex(f"Tabla: {LEY}. Un compás tiene blanca, corchea y corchea. ¿Cuántas unidades suma y qué falta?", "6 unidades; faltan 2", "4 + 1 + 1 = 6 y 8 − 6 = 2."),
        ex("Dos estudiantes tocan la misma frase. Uno la toca a 60 pulsos por minuto y sin errores; el otro a 100 pulsos por minuto con cuatro errores. ¿Quién muestra más precisión técnica?", "El primero", "Hace la frase sin errores, y la precisión va antes que la velocidad."),
    ],
    [
        arith("Una frase de ejemplo tiene 16 compases de 4 pulsos y se toca a 80 pulsos por minuto. ¿Cuántos segundos dura?", "16*4*60//80", "Los pulsos totales se dividen entre los pulsos por segundo; 80 por minuto es 80/60.", " segundos"),
        arith("En una frase hay 6 compases con 8 unidades cada uno. ¿Cuántas unidades de duración suma toda la frase?", "6*8", "Se multiplican las unidades de cada compás por los compases.", " unidades"),
    ],
    [ex("En el ensayo de la banda del liceo, la persona que toca el tambor entra siempre medio pulso antes que el resto. ¿Qué criterio de precisión técnica debe trabajar? A) La precisión rítmica. B) La afinación.", "A", "El problema es el momento de entrada, no la altura de las notas.")],
    [ex("¿Qué es afinar?", "Producir la altura justa de cada nota", "Es la parte de la precisión que se refiere a la altura."), ex(f"Tabla: {LEY}. ¿Cuántas unidades vale una negra?", "2", "Así lo indica la tabla."), ex("¿Qué se logra primero: la precisión o la velocidad?", "La precisión", "Se practica lento y exacto antes de acelerar.")],
    (
        "Revisa estos tres compases de ejemplo, todos de 4 pulsos (8 unidades): compás 1 = blanca + negra + corchea; compás 2 = negra + negra + negra + negra; compás 3 = redonda. Escribe: a) cuánto suma cada compás, b) cuáles están completos y qué le falta o sobra al otro, c) una forma de practicar el compás con error con palmas suaves a pulso parejo.",
        "a) Compás 1: 4 + 2 + 1 = 7; compás 2: 2 + 2 + 2 + 2 = 8; compás 3: 8. b) Están completos el 2 y el 3; al 1 le falta 1 unidad (una corchea). c) Marcar cuatro pulsos con palmas suaves, decir en voz baja las figuras del compás 1 despacio y agregar la corchea que falta.",
        ["suma bien las unidades", "identifica cuánto falta o sobra", "propone una práctica lenta y segura"],
        ["tres sumas correctas", "propuesta de práctica"],
        ["no contar los silencios", "tocar rápido antes de tocar bien"],
        "Reconoce las sumas y pide inventar un compás completo con una blanca, una negra y dos corcheas.",
    ),
    "Marca con palmas suaves cuatro pulsos y cuenta en voz baja hasta 4 sin acelerar.",
    "Escribe tres compases de 4 pulsos completos usando figuras distintas y comprueba la suma.",
)

# ---------------------------------------------------------------- OA 04 · clase 2 (cantar a una y más voces)
FORM = ("Disposición 1 (de ejemplo): una voz sola. Disposición 2: todas las voces al unísono. Disposición 3: dos voces, una con la melodía y otra más grave que la acompaña. "
        "Disposición 4: canon a tres voces, que entran con 2 compases de diferencia")
L(
    OA4, 2,
    f"Lápiz y papel. Disposiciones de ejemplo, que se repiten en los ejercicios: {FORM}.",
    "Aprenderé a distinguir las maneras de cantar o tocar a una voz y a más voces (solo, unísono, dos voces, canon) y qué aporta cada una al propósito de la pieza. Sirve para elegir y practicar mi parte según la manera en que se interpreta.",
    ["Sé qué es una voz principal y un acompañamiento.", "Sé qué es el canon.", "Sé mantener un pulso estable."],
    [
        "Una pieza puede interpretarse de varias maneras. A una voz, una persona canta o toca sola: se oye claro, pero con menos volumen y menos colores. Al unísono, todas las voces cantan la misma melodía a la misma altura: la música suena más potente y firme. A dos voces, una lleva la melodía y la otra la acompaña con notas diferentes, casi siempre más graves, y el sonido se vuelve más rico porque se combinan alturas distintas.",
        "En un canon, la misma melodía comienza en una voz y las demás entran después, con unos compases de diferencia. En un canon a tres voces con 2 compases de diferencia, la voz 1 empieza en el compás 1, la voz 2 en el compás 3 y la voz 3 en el compás 5. Esto exige escuchar mucho: cada persona debe mantener su parte aunque oiga otra melodía. Con práctica, la dificultad se vuelve una forma de apoyarse entre todas.",
        "Para interpretar bien a más voces hay que cuidar la precisión técnica de la propia parte y también la coordinación con las demás: el mismo pulso, las mismas entradas y un volumen equilibrado, de modo que ninguna voz tape a otra. Elegir la manera de interpretar depende del propósito: un anuncio solemne pide unísono; una canción íntima puede pedir una o dos voces; un juego de entradas pide canon.",
    ],
    [("a una voz", "una sola persona canta o toca la melodía"), ("unísono", "todas las voces cantan la misma melodía a la misma altura"), ("a dos voces", "una voz lleva la melodía y otra la acompaña con notas distintas"), ("canon", "la misma melodía entra en cada voz con unos compases de diferencia"), ("entrada", "momento exacto en que una voz empieza")],
    [
        ("Calcular entradas", f"{FORM}. En la disposición 4, ¿en qué compás entra la voz 3?", ["La voz 1 entra en el compás 1.", "Cada voz entra 2 compases después: la 2 en el 3 y la 3 en el 5."], "En el compás 5"),
        ("Elegir según el propósito", "Un grupo quiere un anuncio solemne y firme para abrir un acto. ¿Qué disposición conviene: una voz sola o unísono?", ["Un anuncio firme necesita potencia.", "El unísono suena más potente."], "Unísono"),
    ],
    [
        ("Cantar fuerte para que se oiga mi voz en el canon.", "Si cada voz sube su volumen, el grupo se descontrola y se pierde la melodía.", "Mantén el volumen equilibrado y escucha las otras voces."),
        ("Seguir la melodía de otra voz en lugar de la propia.", "En el canon cada voz tiene su entrada y su parte, aunque suenen otras.", "Concéntrate en tu entrada y en tu texto."),
    ],
    [
        ex(f"{FORM}. ¿Cuántas voces tiene el canon de la disposición 4?", "3", "Así lo indica la descripción."),
        ex(f"{FORM}. ¿Cómo se llama la disposición en que todas cantan la misma melodía a la misma altura?", "Unísono", "Esa es la definición del unísono."),
        ex(f"{FORM}. En la disposición 3, ¿qué hace la voz más grave?", "Acompañar a la melodía", "La otra voz lleva la melodía."),
    ],
    [
        ex("¿Qué se oye en un unísono, comparado con una voz sola? A) Un sonido más potente y firme. B) Un sonido más suave y solitario.", "A", "Varias voces sumadas aumentan la fuerza del sonido."),
        ex(f"{FORM}. En un canon, ¿qué hace la voz 2? A) Entra después de la voz 1 con la misma melodía. B) Canta una melodía totalmente distinta.", "A", "En un canon la melodía es la misma y cambia el momento de entrada."),
        ex("Para que un grupo a dos voces suene claro, ¿qué se necesita? A) Un volumen equilibrado, para que ninguna voz tape a la otra. B) Que la voz grave cante más fuerte.", "A", "La melodía debe oírse junto con su acompañamiento."),
    ],
    [
        arith(f"{FORM}. En la disposición 4, la melodía dura 8 compases. ¿En qué compás termina la voz 3, que entra en el compás 5?", "5+8-1", "La voz 3 empieza en el compás 5 y ocupa 8 compases, hasta el compás 12.", ""),
        ex(f"{FORM}. En el canon de la disposición 4 con melodía de 8 compases, ¿cuántas voces suenan a la vez en el compás 6? Considera que la voz 1 suena en 1 a 8, la 2 en 3 a 10 y la 3 en 5 a 12.", "3", "En el compás 6 coinciden las tres voces."),
        arith("Un coro tiene 18 personas y se divide en 3 voces iguales para un canon. ¿Cuántas personas hay en cada voz?", "18//3", "Se reparten las 18 personas en tres grupos iguales.", " personas"),
    ],
    [
        ex(f"{FORM}. En el compás 2 del canon (melodía de 8 compases), ¿cuántas voces suenan? Recuerda que la voz 1 suena en los compases 1 a 8, la 2 en 3 a 10 y la 3 en 5 a 12.", "1", "Solo la voz 1 ha entrado en el compás 2."),
        ex("Un grupo canta un canon de ejemplo y la voz 2 se confunde y empieza a cantar la melodía de la voz 1 en el mismo instante. ¿Qué disposición terminó cantando por error? A) Unísono. B) A dos voces.", "A", "Cantan lo mismo y a la vez."),
    ],
    [
        arith(f"{FORM}. El canon se canta completo una vez con 8 compases de melodía. Si cada compás dura 3 segundos, ¿cuántos segundos pasan desde que empieza la voz 1 hasta que termina la voz 3?", "(5-1+8)*3", "Hay 4 compases de entrada más los 8 de melodía; cada compás dura 3 segundos.", " segundos"),
        ex("Para abrir el acto de aniversario del liceo, un grupo debe elegir una manera de cantar. Quiere que el público sienta potencia y unidad. ¿Qué disposición conviene? A) Unísono. B) Una voz sola.", "A", "Varias voces cantando lo mismo dan potencia y sentido de grupo."),
    ],
    [ex(f"{FORM}. Estás en la voz 3 del canon. ¿Qué haces mientras esperas tu entrada en el compás 5? A) Escuchar las otras voces y contar los compases. B) Cantar desde el compás 1 para no olvidar.", "A", "Contar los compases asegura una entrada justa.")],
    [ex("¿Qué es un canon?", "La misma melodía entrando en cada voz con unos compases de diferencia", "Es una imitación completa entre las voces."), ex("¿Qué disposición suena más potente: una voz sola o un unísono?", "El unísono", "Hay más voces cantando lo mismo."), ex("En el canon de la clase, ¿cada cuántos compases entra una voz?", "Cada 2 compases", "Así dice la disposición 4.")],
    (
        "Elige una de las cuatro disposiciones de ejemplo para una presentación en tu curso con este propósito: «dar la bienvenida con alegría y unidad». Escribe: a) qué disposición eliges, b) dos razones, c) cómo cuidarás tu parte (afinación, entrada y volumen), d) qué harás si te pierdes.",
        "a) Unísono. b) Suena potente y muestra unidad; todas cantan la misma melodía y es más fácil seguirla. c) Afinar con atención a la nota inicial, entrar con la señal de la directora y cantar sin tapar a nadie. d) Seguir con calma en el siguiente compás fuerte, sin detener al grupo.",
        ["elige según el propósito", "da razones relacionadas con el sonido", "incluye un plan para cuando se pierde"],
        ["cuatro respuestas a) a d)", "razones apoyadas en lo que se oye"],
        ["elegir sin justificar", "no cuidar el volumen"],
        "Reconoce la elección y pide explicar qué cambiaría si eligieras el canon.",
    ),
    "Canta una frase conocida dos veces: una sola voz y luego con otra persona cantando al mismo tiempo.",
    "Escribe en una tabla las entradas de cada voz en un canon de 4 voces, con 2 compases de diferencia.",
)

# ---------------------------------------------------------------- OA 04 · clase 3 (ensayo por voces)
ENS = ("Plan de ejemplo para un trío (voz A, voz B y voz C) de una pieza de 12 compases de 4 pulsos: 1) cada voz ensaya sola a 60 pulsos por minuto; "
       "2) se juntan de a dos voces; 3) se juntan las tres a 60 pulsos por minuto; 4) se sube a 80 pulsos por minuto")
L(
    OA4, 3,
    f"Lápiz y papel; palmas suaves. Plan de ejemplo, que se repite en los ejercicios: {ENS}.",
    "Aprenderé a ensayar a varias voces por etapas (cada voz sola, de a dos, todas juntas y con aumento de tempo) y a usar un pulso común. Sirve para que el grupo suene seguro y para detectar en qué etapa nace un error.",
    ["Sé qué es una disposición a dos o más voces.", "Sé comprobar compases con unidades.", "Sé planificar un ensayo."],
    [
        "Ensayar a varias voces tiene un orden que ahorra tiempo. Primero cada voz trabaja sola, para aprender su parte con precisión. Luego se juntan de a dos voces, para coordinar entradas y alturas. Después se juntan todas las voces, a un tempo cómodo. Solo cuando todo sale parejo se sube el tempo hasta el definitivo. Si aparece un error, se vuelve a la etapa anterior para ver dónde nace: ¿en una voz sola, al juntar dos o al sumar la tercera?",
        "Un pulso común une al grupo. Puede marcarse con palmas suaves, con el pie o con un metrónomo, que es un aparato o aplicación que marca pulsos regulares. Cuando el pulso es de 60 por minuto, hay un pulso por segundo; en un compás de 4 pulsos, 4 segundos por compás. A 80 pulsos por minuto cada compás dura 3 segundos. Con esos datos se calcula cuánto dura la pieza y cuánto tiempo se dedica a cada etapa.",
        "El ensayo también exige actitud: escuchar sin interrumpir, esperar el turno de hablar y pedir ayuda cuando una parte no sale. Quien dirige da la señal de entrada y el grupo se mira antes de empezar. Si alguien se siente inseguro, el grupo puede repetir esa parte más veces sin burlas. Un grupo que se cuida mejora más rápido y disfruta el trabajo.",
    ],
    [("ensayo por etapas", "ensayo que avanza de cada voz sola a todas juntas y luego sube el tempo"), ("pulso común", "pulso que marca el grupo para coordinarse"), ("metrónomo", "aparato o aplicación que marca pulsos regulares"), ("etapa", "paso del ensayo"), ("coordinación", "trabajo conjunto de las voces para sonar parejas")],
    [
        ("Calcular la duración", f"{ENS}. ¿Cuántos segundos dura la pieza completa a 60 pulsos por minuto?", ["La pieza tiene 12 compases de 4 pulsos: 48 pulsos.", "A 60 por minuto hay un pulso por segundo."], "48 segundos"),
        ("Ubicar un error", f"{ENS}. Una pareja de voces suena bien por separado, pero al juntarse entran desfasadas. ¿En qué etapa nace el problema?", ["Cada voz sola está bien.", "El problema aparece al juntar dos voces."], "En la etapa 2, al juntar de a dos voces"),
    ],
    [
        ("Saltar a la etapa final sin pasar por las anteriores.", "Un error de una voz sola se multiplica cuando suenan todas.", "Respeta el orden de las etapas."),
        ("Interrumpir a quien se equivoca con burlas.", "El ensayo avanza mejor con respeto y escucha.", "Ofrece ayuda y repite la parte."),
    ],
    [
        ex(f"{ENS}. ¿Cuántas voces tiene el trío?", "3", "Son las voces A, B y C."),
        ex(f"{ENS}. ¿En qué etapa se juntan las tres voces?", "En la etapa 3", "Así lo dice el plan."),
        ex("¿Qué es un metrónomo?", "Un aparato o aplicación que marca pulsos regulares", "Sirve de pulso común para el grupo."),
    ],
    [
        ex(f"{ENS}. ¿Qué se hace en la etapa 4? A) Se sube el tempo a 80 pulsos por minuto. B) Se baja el tempo a 40 pulsos por minuto.", "A", "El plan sube el tempo al final."),
        ex("Una voz comete un error en la etapa de tres voces. ¿Qué conviene hacer? A) Volver a la etapa anterior para ver dónde nace el error. B) Seguir adelante sin revisar.", "A", "Volver atrás ubica el origen del error."),
        ex("Si una compañera se equivoca, ¿cuál es una reacción adecuada? A) Ofrecer ayuda y repetir la parte con ella. B) Reírse para que no vuelva a pasar.", "A", "Un ensayo respetuoso ayuda a todo el grupo."),
    ],
    [
        arith(f"{ENS}. ¿Cuántos pulsos tiene la pieza completa?", "12*4", "Son 12 compases de 4 pulsos.", " pulsos"),
        arith(f"{ENS}. ¿Cuántos segundos dura la pieza completa a 80 pulsos por minuto? Calcula con los 48 pulsos.", "48*60//80", "Se divide los pulsos entre los pulsos por segundo; 80 por minuto es 80/60 por segundo.", " segundos"),
        ex(f"{ENS}. Si cada etapa del plan se ensaya 3 veces, ¿cuántas veces se toca la pieza (o una parte de ella) en total en las 4 etapas?", "12", "Son 3 repeticiones por 4 etapas."),
    ],
    [
        arith(f"{ENS}. Cada una de las tres voces ensaya sola 4 minutos en la etapa 1, una tras otra. ¿Cuántos minutos dura la etapa 1?", "3*4", "Son tres voces con 4 minutos cada una.", " minutos"),
        ex(f"{ENS}. A 60 pulsos por minuto la pieza dura 48 segundos y a 80 dura 36 segundos. ¿Cuántos segundos dura menos a 80 que a 60?", "12", "Se restan 36 a 48."),
    ],
    [
        arith("El trío ensaya 3 días a la semana durante 4 semanas, 20 minutos cada día. ¿Cuántos minutos suman en total?", "3*4*20", "Se multiplican los días por semana, las semanas y los minutos de cada día.", " minutos"),
        ex(f"{ENS}. Dos voces suenan bien juntas, pero al sumar la voz C todo se desordena y la voz C está bien sola. ¿Qué conviene hacer? A) Ensayar la voz C con cada otra voz por separado a tempo lento. B) Cantar más fuerte la voz C.", "A", "Así se descubre con cuál de las voces choca y se corrige a tempo cómodo."),
    ],
    [ex(f"{ENS}. En tu liceo, la profesora dice que solo tienen 10 minutos para el ensayo. ¿Qué etapa no conviene saltarse? A) La de cada voz sola, porque asegura la precisión de la parte propia. B) La de subir el tempo, porque es la más corta.", "A", "Sin precisión individual, las etapas siguientes arrastran los errores.")],
    [ex("¿Cuál es la primera etapa del ensayo a varias voces?", "Cada voz sola", "Se aprende primero la parte propia."), ex("A 60 pulsos por minuto, ¿cuántos pulsos hay por segundo?", "1", "60 pulsos entre 60 segundos."), ex("Si el error nace al juntar dos voces, ¿a qué etapa se vuelve?", "A la etapa 2", "Se revisa cómo se coordinan las dos voces.")],
    (
        "Usa el plan de ejemplo (trío, 12 compases de 4 pulsos, etapas 1 a 4). Escribe: a) cuántos segundos dura la pieza en la etapa 1 (a 60 pulsos por minuto), b) un horario de 24 minutos con tiempo para las cuatro etapas (la suma debe dar 24), c) una regla de respeto que cumplirá el grupo, d) qué harás si tu voz es la que se equivoca.",
        "a) 48 segundos. b) Etapa 1: 6 minutos; etapa 2: 6 minutos; etapa 3: 6 minutos; etapa 4: 6 minutos; total 24. c) No interrumpir con burlas; esperar el turno de hablar. d) Pedir repetir mi parte sola más despacio y volver a juntarme con las otras voces.",
        ["la suma de minutos da 24", "incluye una regla de respeto", "propone una acción concreta ante un error propio"],
        ["cuatro respuestas a) a d)", "horario con total correcto"],
        ["repartos que no suman 24", "no incluir norma de respeto"],
        "Reconoce el horario y pide ajustarlo si la etapa 3 resulta más difícil que las otras.",
    ),
    "Marca con palmas suaves un pulso de 60 por minuto durante 20 segundos y cuenta cuántas palmas diste.",
    "Escribe un plan de ensayo de 20 minutos para un dúo, con tres etapas y minutos para cada una.",
)

# ---------------------------------------------------------------- OA 04 · clase 4 (fluidez en la interpretación)
FLU = ("Registro de ejemplo de una pieza de 16 compases: se cantó sin detenerse en los compases 1 a 6 y 9 a 16; en los compases 7 y 8 hubo una pausa de error y se retomó en el compás 9")
L(
    OA4, 4,
    f"Lápiz y papel. Registro de ejemplo, que se repite en los ejercicios: {FLU}. Para practicar, basta tararear con volumen bajo.",
    "Aprenderé a interpretar con fluidez, es decir, sin detenerse cuando aparece un error, y a usar un plan de recuperación. Sirve para presentar música con seguridad y sin perder el pulso ni la entrada.",
    ["Sé mantener un pulso estable.", "Sé ensayar por etapas.", "Sé que equivocarse es parte de aprender."],
    [
        "La fluidez es interpretar de corrido, con continuidad, aunque se cometa un error pequeño. No significa tocar rápido: una pieza lenta también puede ser fluida. En una presentación, detenerse a corregir corta la música y deja al público esperando. Por eso se aprende a seguir. Un plan de recuperación tiene tres pasos: respirar, contar el pulso mentalmente y volver a entrar en el siguiente compás fuerte, que es un compás que el grupo acordó antes, casi siempre donde empieza una frase, y desde el cual todas las voces pueden volver a entrar.",
        "Para practicar la fluidez se ensaya con una grabación de pulso o con alguien que marca el tiempo. Se canta o se toca la pieza completa sin parar, aunque haya errores, y después se anotan los compases en que hubo dificultad. Así se separan dos tareas: tocar de corrido, y corregir. La proporción de compases tocados sin interrupción respecto del total es una medida simple de fluidez.",
        "Los nervios afectan la fluidez. Una respiración lenta antes de empezar, una mirada al grupo y un pulso mental ayudan. Si los nervios son tan fuertes que impiden tocar o cantar, no hay que callarlos: conviene contarlo a una persona adulta de confianza. Cada presentación es una oportunidad de aprender, no un examen sobre quién eres. Se evalúa el resultado musical, no a la persona.",
    ],
    [("fluidez", "continuidad al interpretar, sin detenerse"), ("plan de recuperación", "pasos para seguir después de un error: respirar, contar y volver a entrar"), ("compás fuerte", "compás acordado antes por el grupo, donde empieza una frase y todas las voces pueden volver a entrar"), ("retomar", "volver a entrar en la música después de un error"), ("registro", "anotación de lo que sucedió en un ensayo o presentación")],
    [
        ("Contar compases fluidos", f"{FLU}. ¿Cuántos compases se cantaron sin detenerse?", ["Los compases 1 a 6 son 6.", "Los compases 9 a 16 son 8.", "6 + 8 = 14."], "14 compases"),
        ("Aplicar el plan", "Un grupo se equivoca en el compás 7 y la directora hace una señal. ¿Qué tres pasos del plan de recuperación sigue cada integrante?", ["Respirar.", "Contar el pulso mentalmente.", "Volver a entrar en el siguiente compás fuerte."], "Respirar, contar el pulso y volver a entrar en el siguiente compás fuerte"),
    ],
    [
        ("Detener la pieza para empezar de nuevo.", "Se corta la música y se pierde el pulso del grupo.", "Sigue y anota el error para corregirlo después."),
        ("Pensar que fluidez es tocar rápido.", "La fluidez es continuidad, no velocidad.", "Mantén el tempo acordado, aunque sea lento."),
    ],
    [
        ex(f"{FLU}. ¿Cuántos compases tiene la pieza?", "16", "Así lo dice el registro."),
        ex(f"{FLU}. ¿En qué compás se retomó?", "En el compás 9", "El registro indica que se retomó en el compás 9."),
        ex("¿Cuál es el primer paso del plan de recuperación?", "Respirar", "Se respira antes de volver a entrar."),
    ],
    [
        ex("¿Qué es la fluidez? A) Interpretar con continuidad, sin detenerse. B) Interpretar lo más rápido posible.", "A", "No depende de la velocidad."),
        ex("Un grupo comete un error en el compás 3 de una pieza de 16 compases. ¿Qué conviene hacer? A) Seguir con calma hasta el final y corregir después. B) Detener la pieza y empezar de nuevo.", "A", "Seguir mantiene el pulso y la presentación."),
        ex("Una persona siente tanto nervio antes de presentar que no puede respirar con calma. ¿Qué conviene hacer? A) Contárselo a una persona adulta de confianza. B) Quedarse en silencio y no contarlo.", "A", "Contarlo permite recibir apoyo."),
    ],
    [
        arith(f"{FLU}. ¿Cuántos compases tuvieron dificultad o pausa?", "16-14", "Se restan los compases fluidos al total.", " compases"),
        ex(f"{FLU}. La directora dice que la proporción de compases fluidos fue 14 de 16. En otra presentación fue 12 de 16. ¿En cuál hubo más fluidez?", "En la primera", "14 de 16 es mayor que 12 de 16."),
        ex("Un estudiante registró: «Me detuve en el compás 5, no respiré y entré tarde en el compás 6». ¿Qué paso del plan de recuperación le faltó cumplir primero? A) Respirar. B) Subir el tempo.", "A", "No respiró antes de volver a entrar."),
    ],
    [
        arith("En un ensayo de 20 compases se cantaron 17 sin interrupción y en el siguiente 19 sin interrupción. ¿Cuántos compases más fluidos hubo en el segundo ensayo?", "19-17", "Se restan los compases fluidos del primer ensayo.", " compases"),
        ex("Dos estudiantes dicen: Ana: «La pieza fluyó porque fuimos muy rápidos». Beto: «La pieza fluyó porque seguimos sin detenernos a pesar de un error». ¿Quién usa bien el concepto de fluidez? A) Beto. B) Ana.", "A", "La fluidez es continuidad, no velocidad."),
    ],
    [
        arith("Un grupo canta una pieza de 24 compases. Se cantan 20 compases sin interrupción. ¿Cuántos compases con pausa o dificultad hay?", "24-20", "Se restan los compases fluidos del total.", " compases"),
        ex("En la presentación de fin de año de tu liceo, tu grupo comete un error en el compás 10 de 16 compases. La directora ha acordado que el siguiente compás fuerte es el 13. ¿En qué compás vuelven a entrar?", "En el compás 13", "El plan indica volver en el siguiente compás fuerte acordado."),
    ],
    [ex(f"{FLU}. Después del ensayo, el grupo anota los compases 7 y 8 como difíciles. ¿Qué hace con eso? A) Los ensaya por separado y luego los reintegra a la pieza. B) Cambia de pieza.", "A", "Corregir los compases difíciles aislados mejora la fluidez.")],
    [ex("¿Qué se evalúa en una presentación: el resultado musical o a la persona?", "El resultado musical", "Se habla de lo que sonó."), ex("¿Qué es un compás fuerte?", "Un compás acordado donde empieza una frase y todos pueden volver a entrar", "Sirve para volver a entrar juntos."), ex(f"{FLU}. ¿En qué compás empezó la pausa de error?", "En el compás 7", "El registro dice que los compases 7 y 8 tuvieron la pausa.")],
    (
        "Registro de ejemplo de una pieza de 12 compases: sin detenerse en los compases 1 a 4 y 7 a 12; pausa de error en los compases 5 y 6; se retomó en el compás 7. Escribe: a) cuántos compases fluidos hubo, b) la proporción (por ejemplo «x de 12»), c) los tres pasos del plan de recuperación aplicados a este caso, d) una acción de práctica para los compases 5 y 6.",
        "a) 4 + 6 = 10 compases fluidos. b) 10 de 12. c) Respirar, contar el pulso y volver a entrar en el compás 7. d) Practicar los compases 5 y 6 despacio, solos y luego unidos al 4 y al 7.",
        ["calcula bien los compases fluidos", "aplica los tres pasos al caso", "propone práctica aislada de lo difícil"],
        ["cuatro respuestas a) a d)", "proporción correcta"],
        ["calcular mal los compases", "proponer detener todo el grupo"],
        "Reconoce el análisis y pide explicar por qué conviene practicar primero a tempo lento.",
    ),
    "Respira hondo tres veces y tararea una frase de una canción sin detenerte, aunque te equivoques.",
    "Escribe tu propio plan de recuperación en tres pasos, con palabras tuyas.",
)

# ---------------------------------------------------------------- OA 04 · clase 5 (registro, transmisión y presentación)
PROG = ("Programa de ejemplo de una presentación: pieza 1, solo de voz, 3 minutos; pieza 2, canon a tres voces, 4 minutos; pieza 3, unísono con percusión suave, 5 minutos; "
        "entre una pieza y otra, 1 minuto de pausa y de presentación hablada")
L(
    OA4, 5,
    f"Lápiz y papel. Programa de ejemplo, que se repite en los ejercicios: {PROG}. Para registrar, puedes usar la grabadora de un teléfono solo si todas las personas del grupo y una persona adulta están de acuerdo.",
    "Aprenderé a registrar mis versiones de una pieza (grabación, partitura, bitácora) y a usar medios de transmisión (en vivo, grabación compartida, programa de mano) para gestionar y presentar mi trabajo musical. Sirve para comparar versiones, mejorar y comunicar con orden y respeto.",
    ["Sé interpretar con fluidez.", "Sé ensayar por etapas.", "Sé evaluar con una pauta."],
    [
        "Registrar es dejar constancia de lo que se hizo para poder revisarlo. Se puede registrar una versión de varias maneras: una grabación de audio o video, una partitura con anotaciones, o una bitácora, que es una libreta donde se anota fecha, pieza, tempo, errores y mejoras. Para comparar versiones, se anotan los mismos datos de cada una y se miran las diferencias: por ejemplo, 3 errores en la versión 1 y 1 error en la versión 2.",
        "Transmitir es hacer llegar la música a un público. Puede ser en vivo, con las personas presentes; con una grabación que se comparte; o con un programa de mano, una hoja que dice qué piezas se tocarán, en qué orden y cuánto durará cada una. Gestionar una presentación es planificarla: orden de las piezas, duración total, quién presenta cada una, qué instrumentos se necesitan y cuándo se ensaya.",
        "Grabar y compartir exige respeto. Antes de grabar o publicar, todas las personas del grupo deben aceptar, y si hay personas menores de edad, también una persona adulta responsable. No se comparten datos personales ni grabaciones sin permiso. Si alguien pide no ser grabado, se respeta su decisión. Si alguien sube una grabación tuya sin permiso, guarda una captura, pide que la retiren y avisa a una persona adulta de confianza.",
    ],
    [("registro", "constancia de lo que se hizo, como una grabación o una bitácora"), ("bitácora", "libreta donde se anotan datos de cada ensayo"), ("programa de mano", "hoja que informa las piezas, el orden y la duración de una presentación"), ("transmisión", "hacer llegar la música a un público, en vivo o grabada"), ("gestión", "planificación de una presentación: orden, tiempos y roles")],
    [
        ("Duración de un programa", f"{PROG}. ¿Cuántos minutos suman las tres piezas, sin contar las pausas?", ["Las piezas duran 3, 4 y 5 minutos.", "3 + 4 + 5 = 12."], "12 minutos"),
        ("Comparar versiones", "Bitácora: versión 1, 3 errores a 70 pulsos por minuto; versión 2, 1 error a 70 pulsos por minuto. ¿Qué mejoró?", ["El tempo se mantuvo.", "Los errores bajaron de 3 a 1."], "Bajaron 2 errores"),
    ],
    [
        ("Grabar y publicar sin avisar.", "Se necesita el permiso de todas las personas grabadas.", "Pide permiso y explica para qué será la grabación."),
        ("Anotar «mejoró» sin datos.", "Sin datos no se puede comprobar la mejora.", "Anota errores, tempo y duración."),
    ],
    [
        ex(f"{PROG}. ¿Cuántas piezas tiene el programa?", "3", "Se describen la pieza 1, la 2 y la 3."),
        ex("¿Qué es un programa de mano?", "Una hoja que informa las piezas, el orden y la duración", "Sirve para que el público sepa qué se presentará."),
        ex("Antes de grabar a un grupo, ¿quién debe estar de acuerdo?", "Todas las personas del grupo", "Se necesita permiso de quienes aparecen en la grabación."),
    ],
    [
        ex("¿Qué datos conviene anotar en una bitácora? A) Fecha, pieza, tempo, errores y mejoras. B) Solo si me gustó.", "A", "Los datos permiten comparar versiones."),
        ex("Una persona del grupo no quiere ser grabada. ¿Qué se hace? A) Se respeta su decisión y se busca otra forma de registrar. B) Se graba igual.", "A", "El permiso es voluntario y debe respetarse."),
        ex("¿Qué medio de transmisión es en vivo? A) Tocar frente al público presente. B) Enviar un archivo de audio.", "A", "En vivo significa con el público presente."),
    ],
    [
        arith(f"{PROG}. Hay 2 pausas de 1 minuto cada una entre las 3 piezas. ¿Cuántos minutos dura la presentación completa?", "3+4+5+2*1", "Se suman las piezas y las dos pausas.", " minutos"),
        ex("Bitácora: versión 1 dura 3 minutos 20 segundos y versión 2 dura 3 minutos 5 segundos. ¿Cuántos segundos más corta es la segunda?", "15", "3 min 20 s son 200 s y 3 min 5 s son 185 s."),
        ex("Un estudiante anota: «Versión 2: mejor». ¿Qué dato falta para poder comparar? A) Cuántos errores y a qué tempo. B) Una foto del grupo.", "A", "Con errores y tempo se puede comprobar si mejoró."),
    ],
    [
        arith("Una grabación de audio dura 4 minutos. Si un grupo graba 3 versiones de la misma pieza, una tras otra, ¿cuántos minutos de grabación hay?", "4*3", "Se multiplican los minutos de cada versión por el número de versiones.", " minutos"),
        ex("Un grupo anota en su bitácora: ensayo 1, 6 errores; ensayo 2, 4 errores; ensayo 3, 4 errores. ¿Qué conclusión se apoya en los datos? A) Mejoró del ensayo 1 al 2, pero no del 2 al 3. B) Mejoró siempre.", "A", "Los errores bajaron de 6 a 4 y luego se mantuvieron en 4."),
    ],
    [
        arith(f"{PROG}. El programa empieza a las 18:00 horas. Si no se retrasa, ¿cuántos minutos después de las 18:00 termina?", "3+1+4+1+5", "Se suman las tres piezas y las dos pausas.", " minutos después de las 18:00"),
        ex("Una persona sube una grabación de un compañero a una red social sin su permiso. El compañero se siente mal. ¿Qué debe hacer el compañero? A) Guardar una captura, pedir que la retiren y avisar a una persona adulta de confianza. B) Borrar el chat y no contárselo a nadie.", "A", "Es un protocolo seguro: evidencia, solicitud de retiro y apoyo adulto."),
    ],
    [ex(f"{PROG}. Quieres imprimir un programa de mano. ¿Qué datos debe tener? A) Nombre de las piezas, orden y duración. B) Dirección de las casas de los integrantes.", "A", "No se incluyen datos personales; solo la información de la presentación.")],
    [ex("¿Para qué sirve una bitácora?", "Para anotar datos de cada ensayo y comparar versiones", "Registra fecha, tempo, errores y mejoras."), ex("¿Qué se hace si alguien pide no ser grabado?", "Se respeta su decisión", "El permiso es voluntario."), ex("Una versión pasó de 5 errores a 2. ¿Cuántos errores bajó?", "3", "5 menos 2.")],
    (
        "Prepara un programa de mano para una presentación de tu curso usando estas tres piezas de ejemplo: «Canon de las estaciones» (4 minutos), «Marcha del patio» (3 minutos) y «Canción de despedida» (5 minutos), con 1 minuto de pausa entre piezas. Escribe: a) el orden que eliges y por qué, b) la duración total, c) un registro de ensayo con dos versiones (datos de ejemplo que inventes: errores y tempo), d) una regla para grabar con permiso.",
        "a) Marcha del patio, Canon de las estaciones, Canción de despedida: empiezo con energía y termino con calma. b) 4 + 3 + 5 + 2 = 14 minutos. c) Versión 1: 5 errores a 70; versión 2: 2 errores a 70; bajaron 3. d) Solo grabaremos si todos aceptan.",
        ["el total de minutos es correcto", "el orden tiene una razón musical", "incluye datos comparables y una regla de permiso"],
        ["programa con orden y total", "registro comparativo y regla"],
        ["datos personales en el programa", "comparar versiones sin datos"],
        "Reconoce el programa y pide explicar qué cambiaría si se agrega una cuarta pieza de 3 minutos.",
    ),
    "Anota en tres líneas la fecha, el tempo y los errores de un ensayo tuyo (aunque sea tarareado).",
    "Haz un programa de mano para una presentación imaginaria de tu familia con tres piezas y sus duraciones.",
)
