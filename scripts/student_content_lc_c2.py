"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR06 y LS06: usar recursos tecnológicos (TIC) para conocer sonidos de la lengua y símbolos de la escritura
ancestral. La «escucha» la lee un adulto (guiones escritos en castellano, con la única expresión indígena
ampliamente atestiguada «mari mari», saludo en mapuzugun). No se evalúa pronunciación ni se enseña lengua:
eso corresponde al educador/a tradicional o a la comunidad.
"""
from __future__ import annotations

from student_content_lc_c1 import task, w
from student_lessons import ex, register

LR6, LS6 = "LC01 OA LR06", "LC01 OA LS06"

# ------------------------------------------------------------------ LR06
register(
    LR6, 1,
    materials="Hoja y lápiz. Si quieres, un adulto puede mostrarte una pantalla; las páginas de práctica están escritas en este cuaderno.",
    use="Aprenderé a revisar quién publica algo en una pantalla y si tiene permiso. Sirve para aprender de la lengua y la escritura con fuentes confiables.",
    prior=["Sé qué es una pantalla.", "Sé que hay personas que enseñan la lengua de su pueblo."],
    explain=[
        "En una pantalla hay videos, audios y fotos. Antes de usarlos para aprender, reviso quién los publica y para qué. Una escuela, un museo o una comunidad que dice quién es, es una fuente más clara que una página sin nombre.",
        "Un audio o una foto de un pueblo pertenece a las personas que lo hicieron. Por eso reviso si dice que se puede usar y quién dio el permiso. Si no lo dice, no lo copio ni lo comparto.",
        "Cuando una lengua se está recuperando, las comunidades cuidan sus grabaciones. Lo más seguro es usar lo que me muestra el educador o la educadora tradicional o mi profesor o profesora, y no buscar solo en la pantalla.",
    ],
    vocab=[("publicar", "poner algo para que otros lo vean"), ("fuente", "quien da la información"), ("permiso", "un sí de quien hizo o cuida algo"), ("confiable", "que se puede creer porque dice quién es"), ("compartir", "mandar algo a otras personas")],
    worked=[
        w("Revisar quién publica", "Página de práctica (inventada): «Centro cultural de una comunidad. Contacto: dirección del centro». Otra: «Anónimo, sin datos». ¿Cuál es más confiable?", ["La primera dice quién es y cómo contactarlo.", "La segunda no dice nada.", "Elijo la primera."], "la del centro cultural"),
        w("Revisar el permiso", "Un audio dice: «Se puede escuchar en la escuela; no se puede copiar». ¿Puedo copiarlo?", ["Leo la regla: escuchar sí, copiar no.", "Entonces no lo copio."], "no"),
    ],
    mistakes=[
        {"wrong": "Creer que todo lo que sale en una pantalla es verdad.", "why": "Cualquiera puede publicar, aunque no sepa.", "fix": "Reviso quién lo publica y para qué."},
        {"wrong": "Mandar un audio de una persona a mis amigos sin preguntar.", "why": "La voz es de esa persona y de su comunidad.", "fix": "Pregunto si se puede compartir."},
    ],
    tiers={
        "recovery": [
            ex("Antes de usar un video, ¿reviso quién lo publica o no miro nada?", "reviso quién lo publica", "Así sé si es una fuente confiable."),
            ex("¿Cuál dice quién es: «Escuela de la comunidad» o «Sin nombre»?", "«Escuela de la comunidad»", "Dice quién publica."),
            ex("¿Qué es compartir: mandar algo a otras personas o borrarlo?", "mandar algo a otras personas", "Compartir es enviar a otros."),
        ],
        "understand": [
            ex("Verdadero o falso: todo lo que sale en una pantalla es verdad.", "Falso", "Cualquier persona puede publicar."),
            ex("Una foto de un tejido pertenece a quien lo hizo. ¿Puedo copiarla sin preguntar?", "No", "Es de sus creadores y de su comunidad."),
            ex("¿Quién me puede mostrar una fuente segura: el educador tradicional o una página sin nombre?", "el educador tradicional", "Es una persona que conozco y que sabe."),
        ],
        "apply": [
            ex("Página de práctica A: «Museo regional, con teléfono». Página B: «Sin nombre ni datos». ¿Cuál es más confiable?", "A", "A dice quién es."),
            ex("Un audio dice «solo para escuchar en clase». ¿Lo puedo mandar a otro curso?", "No", "El permiso es solo para escuchar en clase."),
            ex("Ordena: A) escucho B) reviso quién lo publica C) pregunto si puedo compartir. Escribe 3 letras.", "B, A, C", "Primero reviso la fuente, luego escucho y por último pregunto por compartir."),
        ],
        "reason": [
            ex("Pablo dice «lo vi en una pantalla, entonces es de verdad». ¿Qué le dirías?", "que revise quién lo publicó", "Hay que mirar la fuente."),
            ex("¿Por qué conviene aprender con el educador tradicional además de la pantalla?", "porque conoce y cuida el saber de su comunidad", "La pantalla no reemplaza a quien enseña."),
        ],
        "challenge": [
            ex("Tres páginas de práctica: una con nombre de museo, una con nombre de escuela y una sin nombre. ¿Cuántas dicen quién publica?", "2", "Solo la tercera no dice quién publica."),
            ex("Un video no dice si se puede compartir. ¿Qué hago: lo comparto o pregunto?", "pregunto", "Sin permiso no se comparte."),
        ],
    },
    context=[ex("Tu profesora te muestra en una pantalla un audio con una persona que dice «mari mari», saludo en mapuzugun. La página dice «Centro cultural, solo para escuchar». ¿Puedes grabarlo en un teléfono para mandarlo a tus primos?", "No", "El permiso es solo para escuchar.")],
    selfcheck=[ex("¿Qué reviso antes de usar un video?", "quién lo publica", "Eso dice si es una fuente confiable."), ex("¿Qué hago si no dice que lo puedo compartir?", "pregunto", "Sin permiso no se comparte."), ex("¿Quién me puede guiar mejor?", "el educador tradicional", "Conoce el saber.")],
    open_task=task(
        "Elige una de estas páginas de práctica y escribe una frase: «Esta fuente es / no es confiable porque…». A) «Museo del pueblo, contacto y fecha, solo para escuchar». B) «Video sin nombre ni fecha, copia libre». Pregunta al educador/a tradicional o a tu profesor/a si estás de acuerdo.",
        "A es confiable porque dice quién es y tiene contacto. No se puede copiar porque es solo para escuchar.",
        ["revisa quién publica", "considera el permiso", "consulta al educador/a tradicional o a la comunidad"],
        ["frase escrita", "conversación con el educador/a"],
        ["creer algo solo por estar en una pantalla", "compartir sin permiso"],
        "Verifica que justificó con quién publica y qué permiso hay; si dijo «es verdad porque sí», pídele mirar la fuente.",
    ),
    reinforce="Cuenta tres cosas que revisas antes de usar un audio o una foto.",
    extend="Pregunta en casa si algún adulto pidió permiso antes de compartir una foto de otra persona.",
)

register(
    LR6, 2,
    materials="Un adulto que lea en voz alta el guion escrito aquí; hoja y lápiz. No necesitas pantalla ni internet.",
    use="Aprenderé a escuchar con atención una voz y a reconocer una expresión que se repite. Sirve para disfrutar la lengua con respeto.",
    prior=["Sé escuchar sin interrumpir.", "Sé contar hasta 10."],
    explain=[
        "Escuchar con atención es mirar hacia la voz, estar en silencio y fijarme en una sola cosa. Hoy me fijo en una expresión que se repite. Puede ser un saludo, un nombre o una palabra.",
        "Mari mari es un saludo en mapuzugun, la lengua del pueblo mapuche. Es una expresión conocida y verificada. No intento decir otras palabras ni pronunciar de memoria lo que no sé. La pronunciación la enseña el educador o la educadora tradicional.",
        "Cuando uso un audio o una voz, escucho dos veces. La primera vez entiendo todo. La segunda vez cuento cuántas veces aparece la expresión. Así practico la atención sin copiar nada.",
    ],
    vocab=[("escuchar", "oír con atención"), ("expresión", "palabra o frase que se dice"), ("mari mari", "saludo en mapuzugun"), ("repetir", "decir otra vez"), ("mapuzugun", "lengua del pueblo mapuche")],
    worked=[
        w("Contar una expresión", "Guion: «Hola. Mari mari. Hoy aprendemos. Mari mari para todos». ¿Cuántas veces se dice «mari mari»?", ["Leo el guion y marco cada «mari mari».", "Aparece una vez en la segunda oración y otra al final.", "Total: 2."], "2 veces"),
        w("Reconocer dónde está", "En el guion anterior, ¿la expresión aparece al principio o al final?", ["Primero: «Hola».", "Después aparece «Mari mari».", "Aparece cerca del principio y también al final."], "al principio y al final"),
    ],
    mistakes=[
        {"wrong": "Hablar mientras escucho.", "why": "No oigo la expresión.", "fix": "Guardo silencio y levanto un dedo cuando la oigo."},
        {"wrong": "Inventar palabras que suenan parecidas.", "why": "No sé si existen ni qué significan.", "fix": "Solo repito lo que me enseña el educador o educadora tradicional."},
    ],
    tiers={
        "recovery": [
            ex("«Mari mari» es un saludo en mapuzugun. ¿Es una despedida o un saludo?", "un saludo", "Se usa para saludar."),
            ex("Guion: «Mari mari». ¿Cuántas veces dice «mari mari»?", "1", "Aparece una vez."),
            ex("Para escuchar bien, ¿hablo o hago silencio?", "hago silencio", "Así oigo la voz."),
        ],
        "understand": [
            ex("¿De qué lengua es el saludo «mari mari»?", "mapuzugun", "Es el saludo del pueblo mapuche."),
            ex("Verdadero o falso: puedo inventar otras palabras que suenen parecido.", "Falso", "Podrían no existir ni significar eso."),
            ex("¿Quién enseña la pronunciación: el educador tradicional o yo?", "el educador tradicional", "Él o ella conoce la forma correcta."),
        ],
        "apply": [
            ex("Guion: «Buenos días. Mari mari. Hoy es lunes. Mari mari. Gracias». ¿Cuántas veces aparece «mari mari»?", "2", "Aparece en la segunda y la cuarta oración."),
            ex("Guion: «Mari mari, mari mari, mari mari». ¿Cuántas veces aparece?", "3", "Se repite tres veces."),
            ex("Guion: «Hola. Mari mari. Hoy aprendemos a escuchar. Mari mari para el curso. Hasta luego». ¿En cuántas oraciones aparece «mari mari»?", "2", "Aparece en dos oraciones."),
        ],
        "reason": [
            ex("Si escucho una palabra distinta que no conozco, ¿la repito igual o pregunto?", "pregunto", "No quiero inventar ni equivocarme."),
            ex("¿Por qué conviene escuchar dos veces: para contar y entender mejor o para aburrirse?", "para contar y entender mejor", "La segunda escucha se enfoca en la expresión."),
        ],
        "challenge": [
            ex("Guion: «Mari mari. Hoy es martes. Hola a todos. Mari mari. Mari mari». ¿Cuántas oraciones tiene el guion y en cuántas aparece el saludo?", "5 oraciones y 3 con el saludo", "Hay cinco oraciones y tres son «Mari mari»."),
            ex("En el guion «Hola. Mari mari. Gracias», ¿la expresión viene antes o después de «Gracias»?", "antes", "«Mari mari» es la segunda oración y «Gracias» la tercera."),
        ],
    },
    context=[ex("Un adulto lee: «Buenas tardes. Mari mari. Hoy visitamos la escuela. Mari mari de nuevo». ¿Cuántas veces dijo el saludo en mapuzugun?", "2", "Aparece dos veces.")],
    selfcheck=[ex("¿Qué significa «mari mari»?", "es un saludo en mapuzugun", "Es una expresión de saludo."), ex("¿Escucho en silencio o hablando?", "en silencio", "Así oigo bien."), ex("¿Quién enseña la pronunciación?", "el educador tradicional o la comunidad", "Ellos conocen la forma.")],
    open_task=task(
        "Pide a un adulto que lea este guion: «Hola. Mari mari. Hoy aprendemos. Mari mari para todos. Hasta pronto». Cuenta cuántas veces escuchas «mari mari» y dibuja una marca por cada vez. Escribe una pregunta para el educador/a tradicional sobre cómo se dice y cuándo se usa.",
        "Escuché 2 veces el saludo. Dibujé 2 marcas. Pregunta: ¿cuándo se usa «mari mari»?",
        ["cuenta la expresión", "no inventa otras palabras", "pregunta al educador/a tradicional o a la comunidad"],
        ["marcas", "pregunta escrita"],
        ["contar mal", "inventar palabras"],
        "Reconoce el conteo correcto (2); pídele que la pronunciación la deje al educador/a tradicional.",
    ),
    reinforce="Pide a un adulto que lea otro guion y cuenta una palabra que se repita.",
    extend="Escucha una canción o poema en castellano en casa y cuenta cuántas veces se repite una palabra.",
)

register(
    LR6, 3,
    materials="Hoja y lápiz. Las descripciones de pantalla están escritas en este cuaderno.",
    use="Aprenderé a mirar una foto de un símbolo en una pantalla sin copiarlo fuera de contexto. Sirve para cuidar lo que es de otros pueblos.",
    prior=["Sé la diferencia entre un objeto y una foto.", "Sé describir formas."],
    explain=[
        "Una foto en una pantalla es una copia del objeto. En la foto no siento su peso, su textura ni su tamaño real. Puede verse más grande o más chica de lo que es. Por eso una foto no cuenta todo.",
        "Un símbolo puede tener una ocasión de uso y un lugar en el territorio de su pueblo. Si lo saco de su contexto y lo pongo en un trabajo o en un juego, puede perder su sentido. Por eso observo sin copiar a otro lugar.",
        "Para observar bien, me hago preguntas: ¿qué material es? ¿de qué pueblo? ¿quién publicó la foto? Y si quiero usar la imagen en otro lugar, pido permiso al educador o educadora tradicional.",
    ],
    vocab=[("foto", "imagen de un objeto, no el objeto"), ("contexto", "lugar y situación donde algo se usa"), ("textura", "cómo se siente al tocar"), ("copiar", "hacer otra igual"), ("imagen", "dibujo o foto")],
    worked=[
        w("Foto y objeto", "Una foto muestra una tablilla de madera. ¿Qué no puedo saber solo con la foto?", ["Veo la forma y el color.", "No puedo tocar la madera ni saber su tamaño real.", "Entonces la foto no cuenta todo."], "su textura y su tamaño real"),
        w("Observar sin copiar", "Quiero poner un símbolo de la foto en mi cartel. ¿Qué hago antes?", ["Anoto pueblo y fuente de la foto.", "Pregunto al educador tradicional si corresponde.", "Espero la respuesta."], "preguntar antes de usarlo"),
    ],
    mistakes=[
        {"wrong": "Pensar que la foto es igual al objeto.", "why": "La foto no muestra textura, olor ni tamaño real.", "fix": "Leo qué dice la ficha: material y tamaño."},
        {"wrong": "Cortar un símbolo de una foto para decorar.", "why": "Lo saco de su contexto sin permiso.", "fix": "Pregunto si puedo usarlo y cómo."},
    ],
    tiers={
        "recovery": [
            ex("Una foto de una tela, ¿es la tela o una imagen de la tela?", "una imagen de la tela", "La foto es una copia."),
            ex("En una foto, ¿puedo tocar la textura del objeto?", "No", "La textura solo se siente con el objeto."),
            ex("¿Cuál es el material de una tablilla de Rapa Nui: madera o plástico?", "madera", "Las tablillas son de madera."),
        ],
        "understand": [
            ex("Verdadero o falso: una foto cuenta todo sobre el objeto.", "Falso", "No muestra textura ni tamaño real."),
            ex("¿Qué significa contexto: dónde y cómo se usa algo o el color de algo?", "dónde y cómo se usa algo", "Es la situación en que algo tiene sentido."),
            ex("¿Sacar un símbolo de su contexto sin permiso es respetuoso?", "No", "Puede perder su sentido."),
        ],
        "apply": [
            ex("Foto de práctica: «Tela con rayas, pueblo desconocido, fuente: blog». ¿Qué dato anotas como pregunta?", "el pueblo", "El pueblo no se sabe."),
            ex("Una foto muestra un cordel con nudos. ¿Qué datos de la ficha quieres saber: material, pueblo y fuente o solo el color?", "material, pueblo y fuente", "Son los datos de procedencia."),
            ex("Ordena: A) uso la imagen B) pregunto si puedo C) observo la foto. Escribe 3 letras.", "C, B, A", "Observo, pregunto y recién uso si me dicen que sí."),
        ],
        "reason": [
            ex("Si la foto no dice su tamaño, ¿puedo asegurar que es grande? Responde Sí o No.", "No", "Una foto puede mostrarlo más grande o más chico."),
            ex("¿Por qué no debo cortar un símbolo de una foto para decorar un cuaderno?", "porque lo saco de su contexto sin permiso", "Puede perder su sentido."),
        ],
        "challenge": [
            ex("Hay tres datos de una foto: material, pueblo, fuente. Se conocen material y fuente. ¿Cuántos datos faltan?", "1", "Falta el pueblo."),
            ex("Dos fotos del mismo objeto se ven distintas por el tamaño en la pantalla. ¿Cambió el objeto?", "No", "Lo que cambió es la imagen."),
        ],
    },
    context=[ex("Tu amigo quiere poner la foto de un símbolo en la polera de su equipo. ¿Qué le recomiendas hacer primero?", "preguntar al educador tradicional si corresponde", "El símbolo puede tener un uso especial.")],
    selfcheck=[ex("¿Una foto es el objeto?", "No", "Es una imagen."), ex("¿Qué pregunto antes de usar una imagen?", "si puedo usarla", "Pido permiso a quien corresponde."), ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es contexto?", "dónde y cómo se usa algo", "Es su situación.")],
    open_task=task(
        "Mira esta descripción de pantalla: «Foto de una tablilla de madera con signos de Rapa Nui, publicada por un museo, sin tamaño». Escribe tres cosas que la foto SÍ te dice y dos que NO te dice. Luego escribe una pregunta al educador/a tradicional o a tu profesor/a.",
        "SÍ dice: es de madera, es de Rapa Nui, lo publica un museo. NO dice: el tamaño ni cómo se siente. Pregunta: ¿puedo ver una réplica?",
        ["distingue lo que la foto dice", "reconoce sus límites", "hace una pregunta a la comunidad"],
        ["lista escrita", "pregunta"],
        ["creer que la foto lo dice todo", "inventar significado"],
        "Verifica que separó lo que se sabe de lo que no; pídele ajustar si inventó el tamaño.",
    ),
    reinforce="Mira una foto de tu casa y di dos cosas que sí ves y dos que no puedes saber.",
    extend="Explica en casa por qué una foto no reemplaza al objeto.",
)

register(
    LR6, 4,
    materials="Hoja y lápiz. No necesitas grabar nada: practicamos con frases en castellano.",
    use="Aprenderé a usar mi voz o un audio sin grabar a otras personas y pidiendo consentimiento. Sirve para cuidar la voz y la intimidad de cada uno.",
    prior=["Sé que mi voz es mía.", "Sé pedir permiso."],
    explain=[
        "El consentimiento es decir «sí» después de que me preguntan, sabiendo para qué es. Si grabo o fotografío a una persona, necesito su sí. Una persona puede decir «no», y eso se respeta.",
        "La voz de las personas que hablan una lengua originaria es muy valiosa. Muchas comunidades cuidan sus grabaciones. No grabo a las personas sin consentimiento. Para practicar uso solo mi propia voz diciendo frases en castellano.",
        "Si quiero reproducir un audio de la escuela, pregunto a mi profesor o profesora, y a la comunidad si corresponde. Si no hay respuesta, no lo reproduzco fuera de clase.",
    ],
    vocab=[("consentimiento", "decir «sí» sabiendo para qué es"), ("grabar", "guardar una voz o imagen"), ("reproducir", "volver a poner un audio"), ("privacidad", "lo que es solo de cada persona"), ("autorizado", "con permiso")],
    worked=[
        w("Pedir consentimiento", "Quiero grabar a una vecina que habla una lengua originaria. ¿Qué hago?", ["No la grabo aún.", "Le pregunto si quiere y para qué sería.", "Si dice no, respeto su respuesta."], "pedir consentimiento y aceptar su respuesta"),
        w("Practicar con mi voz", "¿Cómo practico sin grabar a nadie?", ["Digo una frase en castellano con mi voz.", "La repito dos veces.", "No uso la voz de otras personas."], "usando solo mi propia voz"),
    ],
    mistakes=[
        {"wrong": "Grabar a alguien sin avisar.", "why": "Su voz es suya.", "fix": "Pido consentimiento y digo para qué."},
        {"wrong": "Mandar un audio de la escuela a mis amigos.", "why": "No sé si tiene permiso de circular.", "fix": "Pregunto a mi profesor o profesora."},
    ],
    tiers={
        "recovery": [
            ex("Si quiero grabar a una persona, ¿pido su permiso o grabo rápido?", "pido su permiso", "El consentimiento va primero."),
            ex("¿Qué significa consentimiento: decir «sí» sabiendo para qué es o decir «no sé»?", "decir «sí» sabiendo para qué es", "Es aceptar con información."),
            ex("¿De quién es mi voz?", "mía", "Mi voz es mía."),
        ],
        "understand": [
            ex("Si una persona dice «no» a que la grabe, ¿la grabo igual?", "No", "Su no se respeta."),
            ex("Verdadero o falso: puedo usar mi voz para practicar frases en castellano.", "Verdadero", "Es mi propia voz."),
            ex("¿Por qué las comunidades cuidan sus grabaciones?", "porque son valiosas para su lengua", "Contienen saber y voz de su pueblo."),
        ],
        "apply": [
            ex("Quieres grabar a tu abuelo diciendo un saludo. Elige: A) «¿Puedo grabarte para la escuela?» B) lo grabas sin avisar.", "A", "A pide consentimiento."),
            ex("Ordena: A) grabo B) pregunto C) recibo un sí. Escribe 3 letras.", "B, C, A", "Primero pregunto, luego recibo un sí y después grabo."),
            ex("Tienes un audio de la escuela. ¿A quién le preguntas si lo puedes reproducir fuera de clase?", "a mi profesor o profesora", "Ella o él sabe qué permiso hay."),
        ],
        "reason": [
            ex("Marcos dice «si es solo un ratito, no importa». ¿Tiene razón?", "No", "Aunque sea corto, se necesita consentimiento."),
            ex("¿Por qué practicamos con nuestra propia voz en castellano?", "para no usar la voz de otros sin permiso", "Cuidamos la privacidad."),
        ],
        "challenge": [
            ex("Hay 3 personas: una dice sí, una dice no y una no responde. ¿A cuántas puedo grabar?", "1", "Solo a quien dijo que sí."),
            ex("Una persona dijo «sí, para la clase». ¿Puedo subir su audio a una red social?", "No", "El permiso era solo para la clase."),
        ],
    },
    context=[ex("En tu casa hay un adulto que habla una lengua originaria y te dice un saludo. Tienes un teléfono. ¿Qué haces antes de grabar?", "pregunto si puedo y para qué", "Se necesita consentimiento.")],
    selfcheck=[ex("¿Qué es el consentimiento?", "decir sí sabiendo para qué es", "Es aceptar con información."), ex("¿Con la voz de quién practico?", "con la mía", "Así cuido a otros."), ex("¿Qué hago si dicen no?", "respeto", "El no se acepta.")],
    open_task=task(
        "Practica con tu voz. Elige una frase: A) «Hola, hoy aprendo con respeto.» B) «Gracias por enseñarme.» Dila dos veces en voz alta. Después escribe cómo le pedirías permiso a una persona de la comunidad para grabar su saludo, y qué harías si dice no.",
        "Dije A dos veces. Le preguntaría: ¿puedo grabar tu saludo para la clase? Si dice no, le agradezco.",
        ["practica con su propia voz", "pide consentimiento", "acepta un no"],
        ["práctica oral", "pregunta escrita"],
        ["grabar sin permiso", "insistir ante un no"],
        "Celebra la pregunta de consentimiento; si propuso grabar sin pedir, vuelve al orden pregunto-recibo-grabo.",
    ),
    reinforce="Di tres frases en castellano con tu voz, sin grabar a nadie.",
    extend="Cuéntale a alguien de casa qué es el consentimiento y da un ejemplo.",
)

# ------------------------------------------------------------------ LS06
register(
    LS6, 1,
    materials="Hoja y lápiz. Las páginas de práctica están descritas en este cuaderno.",
    use="Aprenderé a comprobar quién publica un audio o una imagen y para qué. Sirve para aprender con seguridad.",
    prior=["Sé qué es una pantalla.", "Sé pedir ayuda a un adulto."],
    explain=[
        "Las pantallas muestran muchas cosas: audios, fotos y videos. Algunas personas los publican para enseñar, otras para vender o para entretener. Por eso me pregunto: ¿quién lo publicó y para qué?",
        "Una escuela, un museo o una comunidad que dice quién es, suele ser una fuente clara. Una página sin nombre no me dice quién la hizo. Cuando dudo, pido ayuda a un adulto.",
        "Cuando se trata de la lengua o los símbolos de un pueblo, lo mejor es aprender con el educador o la educadora tradicional. La pantalla puede ayudar, pero no reemplaza a quien enseña.",
    ],
    vocab=[("publicar", "mostrar algo en una pantalla"), ("fuente", "quien da la información"), ("entretener", "hacer pasar un buen rato"), ("vender", "dar algo a cambio de plata"), ("adulto de confianza", "persona mayor que me cuida")],
    worked=[
        w("Quién y para qué", "Página de práctica: «Escuela de la comunidad, para enseñar». ¿Quién publica y para qué?", ["Quien publica: la escuela.", "Para qué: para enseñar."], "la escuela, para enseñar"),
        w("Cuando no se sabe", "Una página no dice quién la hizo. ¿Qué hago?", ["No confío aún.", "Le pido ayuda a un adulto de confianza."], "pedir ayuda a un adulto"),
    ],
    mistakes=[
        {"wrong": "Creer que todo lo de la pantalla es de confianza.", "why": "No siempre se sabe quién lo hizo.", "fix": "Pregunto quién publica."},
        {"wrong": "Seguir mirando una página rara sin avisar.", "why": "Puede no ser segura.", "fix": "Aviso a un adulto."},
    ],
    tiers={
        "recovery": [
            ex("Antes de usar una imagen, ¿pregunto quién la publicó o la copio?", "pregunto quién la publicó", "Eso muestra si es de confianza."),
            ex("¿Cuál dice quién es: «Museo del pueblo» o «Sin nombre»?", "«Museo del pueblo»", "Dice quién publica."),
            ex("Si dudo, ¿pido ayuda a un adulto o sigo solo?", "pido ayuda a un adulto", "Es lo más seguro."),
        ],
        "understand": [
            ex("Verdadero o falso: todas las páginas son de confianza.", "Falso", "Algunas no dicen quién las hizo."),
            ex("Alguien publica para enseñar y otro para vender. ¿Es lo mismo?", "No", "El motivo cambia."),
            ex("¿La pantalla reemplaza al educador tradicional?", "No", "La pantalla ayuda, pero no reemplaza."),
        ],
        "apply": [
            ex("Página A: «Escuela, para enseñar». Página B: sin nombre. ¿Cuál dice quién publica?", "A", "A tiene nombre."),
            ex("Una página dice «Compra ya». ¿Para qué publica: enseñar o vender?", "vender", "Invita a comprar."),
            ex("Ordena: A) uso la imagen B) pregunto quién publicó C) pido ayuda si dudo. Escribe 3 letras.", "B, C, A", "Primero pregunto, luego ayuda si dudo y después uso."),
        ],
        "reason": [
            ex("Si dos páginas dicen cosas distintas, ¿a quién consulto?", "al educador tradicional o a un adulto", "Ellos pueden aclarar."),
            ex("¿Por qué miro quién publica antes de creer?", "porque cualquiera puede publicar", "No todo es verdad."),
        ],
        "challenge": [
            ex("Tres páginas: dos con nombre y una sin nombre. ¿Cuántas son más confiables en su identificación?", "2", "Las que tienen nombre."),
            ex("Una página sin nombre dice enseñar la lengua de un pueblo. ¿La uso como única fuente?", "No", "Hay que contrastar con el educador."),
        ],
    },
    context=[ex("Tu profesora te muestra un video de una comunidad y dice quién lo publicó y para qué. ¿Qué dos datos te dio?", "quién y para qué", "Son los datos para comprobar la fuente.")],
    selfcheck=[ex("¿Qué miro primero?", "quién publica", "Es la fuente."), ex("¿A quién pido ayuda?", "a un adulto de confianza", "Es quien me cuida y orienta."), ex("¿Qué ayuda mejor a aprender la lengua?", "el educador tradicional", "Conoce el saber.")],
    open_task=task(
        "Elige una página de práctica y completa la frase «Publica ____ para ____»: A) «Museo, para mostrar objetos». B) «Sin nombre, para ganar plata». Cuéntale tu respuesta al educador/a tradicional o a un adulto y pregúntale si está de acuerdo.",
        "Publica el museo para mostrar objetos.",
        ["identifica quién publica", "dice para qué", "consulta a un adulto o al educador/a tradicional"],
        ["frase escrita", "conversación"],
        ["no mirar la fuente", "creer sin dudar"],
        "Revisa que respondió quién y para qué; si dudó, felicita que pidió ayuda.",
    ),
    reinforce="Di dos preguntas que haces antes de creer algo de una pantalla.",
    extend="Pregunta en casa cómo saben si una página es de confianza.",
)

register(
    LS6, 2,
    materials="Un adulto que lea el guion en voz alta; hoja y lápiz.",
    use="Aprenderé a escuchar un audio con atención y a reconocer una expresión verificada. Sirve para disfrutar la lengua con respeto.",
    prior=["Sé hacer silencio al escuchar.", "Sé contar hasta 10."],
    explain=[
        "Escuchar con atención es oír sin hablar y fijarme en algo concreto. Hoy me fijo en una expresión que se repite. La expresión verificada de hoy es «mari mari», un saludo en mapuzugun.",
        "No intento decir otras palabras de otras lenguas si no las conozco. La forma de decirlas la enseña el educador o la educadora tradicional. Yo solo reconozco cuando escucho el saludo y lo cuento.",
        "Para practicar, un adulto lee un guion. Yo levanto un dedo cada vez que oigo «mari mari». Al final cuento cuántos dedos levanté. Así practico atención sin copiar ni inventar.",
    ],
    vocab=[("saludo", "palabra que se dice al llegar"), ("guion", "texto que alguien lee"), ("verificada", "comprobada"), ("atención", "mirar o escuchar fijándome bien"), ("mapuzugun", "lengua del pueblo mapuche")],
    worked=[
        w("Levantar un dedo", "Guion: «Hola. Mari mari. Hoy es jueves. Mari mari». ¿Cuántos dedos levantas?", ["Oigo «mari mari» en la segunda oración.", "Lo oigo otra vez al final.", "Levanté dos dedos."], "2"),
        w("Ninguna vez", "Guion: «Hola. Hoy es jueves. Gracias». ¿Cuántos dedos levantas?", ["Reviso cada oración.", "No aparece el saludo."], "0"),
    ],
    mistakes=[
        {"wrong": "Levantar el dedo con otra palabra parecida.", "why": "Puedo confundir.", "fix": "Levanto el dedo solo con «mari mari»."},
        {"wrong": "Inventar cómo se dicen otras cosas.", "why": "No lo sé.", "fix": "Pregunto al educador tradicional."},
    ],
    tiers={
        "recovery": [
            ex("«Mari mari» es un saludo en mapuzugun. ¿Es un saludo o un número?", "un saludo", "Se usa para saludar."),
            ex("Guion: «Mari mari». ¿Cuántos dedos levantas?", "1", "Se oye una vez."),
            ex("Cuando escucho, ¿hablo o hago silencio?", "hago silencio", "Así presto atención."),
        ],
        "understand": [
            ex("¿De qué pueblo es la lengua mapuzugun?", "del pueblo mapuche", "Es la lengua mapuche."),
            ex("Verdadero o falso: puedo inventar saludos de otras lenguas.", "Falso", "No los conozco."),
            ex("¿Quién enseña a decir las palabras en la lengua?", "el educador tradicional", "Conoce la forma."),
        ],
        "apply": [
            ex("Guion: «Mari mari. Buenos días. Mari mari». ¿Cuántos dedos?", "2", "Aparece dos veces."),
            ex("Guion: «Hola, gracias, adiós». ¿Cuántos dedos?", "0", "No aparece el saludo."),
            ex("Guion: «Mari mari. Mari mari. Mari mari. Hoy es viernes». ¿Cuántos dedos?", "3", "Aparece tres veces."),
        ],
        "reason": [
            ex("Si escucho una palabra que no conozco, ¿la repito o pregunto?", "pregunto", "Para no inventar."),
            ex("¿Por qué solo cuento «mari mari» y no otras?", "porque es la expresión verificada", "Solo esa la conozco con seguridad."),
        ],
        "challenge": [
            ex("Guion: «Hola. Mari mari. Bienvenidos. Mari mari. Gracias. Mari mari». ¿Cuántas oraciones tiene y cuántas son saludo?", "6 oraciones y 3 saludos", "Son seis oraciones y tres «Mari mari»."),
            ex("En el guion «Hola. Mari mari. Gracias», ¿la expresión viene después de «Hola»?", "Sí", "Está en la segunda oración."),
        ],
    },
    context=[ex("Un adulto lee en voz alta: «Buenas tardes. Mari mari. Hoy conocemos el saludo mapuche. Mari mari». ¿Cuántas veces se dijo el saludo?", "2", "Se oye dos veces.")],
    selfcheck=[ex("¿Qué es «mari mari»?", "un saludo en mapuzugun", "Es un saludo."), ex("¿Cómo escucho?", "en silencio", "Así presto atención."), ex("¿Quién me enseña a decir bien las palabras de una lengua?", "el educador tradicional", "Conoce la forma de decirlas.")],
    open_task=task(
        "Pide a un adulto que lea este guion: «Hola. Mari mari. Hoy escuchamos con atención. Mari mari. Hasta luego». Levanta un dedo cada vez que oigas el saludo y dibuja los dedos que levantaste. Escribe una pregunta al educador/a tradicional.",
        "Levanté 2 dedos. Pregunta: ¿cuándo se dice «mari mari»?",
        ["cuenta bien", "no inventa palabras", "pregunta al educador/a tradicional o a la comunidad"],
        ["dibujo", "pregunta"],
        ["contar mal", "inventar palabras"],
        "Reconoce el conteo correcto (2); si inventó palabras, vuelve a la regla de solo repetir lo verificado.",
    ),
    reinforce="Escucha un guion corto y cuenta una palabra que se repite.",
    extend="Cuenta a alguien de casa cuál es el saludo en mapuzugun que aprendiste.",
)

register(
    LS6, 3,
    materials="Hoja y lápiz; las descripciones de pantalla están en este cuaderno.",
    use="Aprenderé a observar símbolos en pantallas sin copiarlos fuera de contexto. Sirve para cuidar lo que es de otros pueblos.",
    prior=["Sé describir formas.", "Sé la diferencia entre objeto y foto."],
    explain=[
        "Una foto es una imagen del objeto, no el objeto. En una pantalla puedo ver su forma y su color, pero no su textura ni su tamaño real. Por eso una foto no lo cuenta todo.",
        "Los símbolos tienen una historia y un lugar donde se usan. Si copio un símbolo de una foto y lo pongo en un trabajo mío, puede perder su sentido. Por eso observo con atención y no lo copio fuera de contexto.",
        "Lo que sí puedo hacer es describir lo que veo y anotar qué datos faltan. Si quiero usarlo en otro lugar, pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("imagen", "foto o dibujo"), ("contexto", "dónde y cómo se usa algo"), ("observar", "mirar con atención"), ("textura", "cómo se siente al tocar"), ("copiar", "hacer igual")],
    worked=[
        w("Qué dice la foto", "Foto de una tablilla de madera con signos. ¿Qué material se ve?", ["Miro la foto.", "Veo una pieza plana de madera."], "madera"),
        w("No copiar", "Quiero usar el símbolo de la foto en mi mochila. ¿Qué hago?", ["Pienso que puede tener un uso especial.", "Pregunto al educador tradicional."], "preguntar antes"),
    ],
    mistakes=[
        {"wrong": "Creer que la foto muestra el tamaño real.", "why": "La pantalla cambia el tamaño.", "fix": "Leo si la ficha dice el tamaño."},
        {"wrong": "Cortar y pegar símbolos de fotos.", "why": "Los saco de su lugar.", "fix": "Pregunto si puedo."},
    ],
    tiers={
        "recovery": [
            ex("Una foto de una tela es una imagen. ¿Verdadero o falso?", "Verdadero", "La foto no es la tela."),
            ex("¿Qué puedo ver en una foto: la forma o el olor?", "la forma", "El olor no se ve en una foto."),
            ex("¿Dónde se usa un símbolo es su contexto? Responde Sí o No.", "Sí", "El contexto es dónde y cómo se usa."),
        ],
        "understand": [
            ex("¿La foto muestra la textura?", "No", "La textura se siente al tocar."),
            ex("¿Es respetuoso cortar un símbolo de una foto para decorar?", "No", "Pierde su contexto."),
            ex("¿Quién puede decirme si corresponde usar el símbolo?", "el educador tradicional", "Él o ella conoce su uso."),
        ],
        "apply": [
            ex("Foto de práctica: «Cordel con nudos, museo». Escribe el material.", "cordel", "El material es el cordel."),
            ex("Una foto no dice el pueblo. ¿Qué pregunta anotas?", "¿De qué pueblo es?", "Falta el pueblo."),
            ex("Ordena: A) uso el símbolo B) observo C) pregunto. Escribe 3 letras.", "B, C, A", "Observo, pregunto y luego uso si me dicen que sí."),
        ],
        "reason": [
            ex("Una foto grande, ¿garantiza que el objeto es grande?", "No", "El tamaño de la foto depende de la pantalla."),
            ex("¿Por qué conviene decir qué datos faltan?", "para no inventar", "Así se respeta la verdad."),
        ],
        "challenge": [
            ex("Una ficha dice material y fuente pero no el pueblo. ¿Cuántos de los 3 datos de procedencia están?", "2", "Material y fuente están."),
            ex("Una foto se ve distinta si la acerco. ¿Cambió el objeto?", "No", "Solo cambió la imagen."),
        ],
    },
    context=[ex("Quieres poner el dibujo de una tablilla de madera de una foto como fondo de tu tarea. ¿Qué haces antes?", "pregunto si puedo usarlo", "Puede tener un uso especial.")],
    selfcheck=[ex("¿La foto es el objeto?", "No", "Es una imagen."), ex("¿Qué datos anoto de una foto?", "pueblo, material y fuente", "Son los datos de procedencia."), ex("¿Qué hago antes de usar un símbolo de una foto?", "pregunto", "Pido permiso a quien corresponde.")],
    open_task=task(
        "Observa esta descripción: «Foto de un cordel con nudos, publicada por un museo andino, sin tamaño». Escribe qué ves, qué datos tienes y cuál no tienes. Después escribe una pregunta al educador/a tradicional.",
        "Veo un cordel con nudos. Tengo material y fuente. No tengo el tamaño. Pregunta: ¿cómo se cuida un cordel así?",
        ["describe", "dice qué falta", "pregunta"],
        ["escritura", "pregunta"],
        ["inventar el tamaño", "copiar el símbolo"],
        "Revisa que separó lo que hay de lo que falta; si inventó, pídele corregir.",
    ),
    reinforce="Describe una foto de casa y di un dato que no se ve.",
    extend="Explica en casa por qué una foto no reemplaza al objeto.",
)

register(
    LS6, 4,
    materials="Hoja y lápiz. No hace falta grabar: se practica con la propia voz.",
    use="Aprenderé a usar mi voz sin grabar a otras personas y a pedir permiso. Sirve para cuidar la privacidad.",
    prior=["Sé que cada persona decide sobre su voz.", "Sé pedir permiso."],
    explain=[
        "Mi voz es mía y la voz de cada persona es suya. Si quiero grabar a alguien, primero le pregunto. Si dice que sí sabiendo para qué es, tengo su consentimiento. Si dice que no, lo respeto.",
        "Algunas voces cuidan saberes importantes, como la lengua de un pueblo. Por eso no las grabo sin permiso ni las comparto. Para practicar, uso mi propia voz con frases en castellano.",
        "También puedo escuchar audios que mi profesor o profesora me muestra. Los escucho en la clase y no los envío a otras personas, a menos que me digan que sí.",
    ],
    vocab=[("consentimiento", "sí dado sabiendo para qué es"), ("grabar", "guardar una voz"), ("compartir", "mandar a otras personas"), ("privacidad", "lo que cada persona cuida para sí"), ("respetar", "aceptar lo que otro decide")],
    worked=[
        w("Pedir permiso", "Quiero grabar a mi tía diciendo un saludo. ¿Qué hago?", ["Le pregunto si puedo.", "Le digo para qué.", "Espero su respuesta."], "preguntar y esperar su respuesta"),
        w("Aceptar un no", "Mi tía dijo que no. ¿Qué hago?", ["No grabo.", "Le agradezco."], "no grabar y agradecer"),
    ],
    mistakes=[
        {"wrong": "Grabar sin avisar.", "why": "La voz es de esa persona.", "fix": "Pido consentimiento."},
        {"wrong": "Enviar un audio de clase a mis amigos.", "why": "El permiso fue para la clase.", "fix": "No lo comparto."},
    ],
    tiers={
        "recovery": [
            ex("Antes de grabar a alguien, ¿pregunto o grabo?", "pregunto", "Se necesita su permiso."),
            ex("¿De quién es la voz de una persona?", "de esa persona", "Cada voz es de su dueño."),
            ex("Si dice no, ¿grabo igual?", "No", "Se respeta el no."),
        ],
        "understand": [
            ex("¿Qué es consentimiento?", "decir sí sabiendo para qué es", "Es aceptar con información."),
            ex("Verdadero o falso: puedo practicar frases con mi propia voz.", "Verdadero", "Mi voz es mía y no necesito permiso."),
            ex("¿Por qué no comparto audios de clase?", "porque el permiso fue para la clase", "No tengo permiso para más."),
        ],
        "apply": [
            ex("Elige la frase: A) «¿Puedo grabar tu voz para la clase?» B) «Voy a grabarte».", "A", "A pide permiso."),
            ex("Escribe en orden: A) pido permiso B) grabo C) recibo un sí. Usa las 3 letras.", "A, C, B", "Pido permiso, recibo un sí y recién grabo."),
            ex("Tienes un audio escuchado en clase. ¿Lo mandas a tu primo?", "No", "No tienes permiso."),
        ],
        "reason": [
            ex("Si grabo solo un ratito, ¿necesito permiso?", "Sí", "El tiempo no cambia el permiso."),
            ex("¿Por qué las voces de una comunidad se cuidan?", "porque cuidan saberes importantes", "Tienen valor para el pueblo."),
        ],
        "challenge": [
            ex("Hay 4 personas: 2 dicen sí, 1 dice no y 1 no responde. ¿A cuántas puedo grabar?", "2", "Solo a las que dijeron sí."),
            ex("Una persona dice «sí, pero solo para mi curso». ¿Puedo subirlo a una red social?", "No", "El permiso era solo para el curso."),
        ],
    },
    context=[ex("Tu profesora te invita a grabar una frase corta con tu voz. ¿Necesitas permiso de otra persona?", "No, solo mío", "Es tu propia voz.")],
    selfcheck=[ex("¿Qué pido antes de grabar?", "consentimiento", "Es el permiso informado."), ex("Para practicar frases en castellano, ¿uso mi voz o la de una vecina?", "mi voz", "Así no uso la voz de otros."), ex("Alguien me responde «no quiero». ¿Qué hago con su respuesta?", "la respeto", "Un no se acepta y se agradece.")],
    open_task=task(
        "Elige una frase en castellano: A) «Hoy aprendo con respeto.» B) «Gracias por enseñarme.» Dila dos veces. Luego escribe cómo pedirías permiso para grabar a una persona de la comunidad y qué harías si responde que no. Pregunta al educador/a tradicional si esa pregunta está bien hecha.",
        "Dije A dos veces. Preguntaría: ¿puedo grabar tu saludo para la clase? Si dice no, le agradezco.",
        ["usa su voz", "pide consentimiento", "acepta un no"],
        ["práctica oral", "pregunta escrita"],
        ["grabar sin permiso", "insistir"],
        "Reconoce la pregunta de consentimiento; si propuso grabar sin preguntar, repite el orden.",
    ),
    reinforce="Practica la pregunta de permiso tres veces.",
    extend="Cuéntale a alguien de casa qué es consentimiento.",
)
