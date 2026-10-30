"""Student material for 2.º básico Inglés, EN02 OA 10 (sonidos /w/, /th/, /s/-/z/ con chants, rimas y diálogos) y OA 11 (participar en interacciones breves).

Sin audio externo: un adulto lee en voz alta los guiones escritos. En los chants las sílabas fuertes van en MAYÚSCULAS.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import ex, register

OA10, OA11 = "EN02 OA 10", "EN02 OA 11"
ADULT = "Un adulto lee en voz alta (tapa el guion): "


def E(rows):
    return [ex(q, a, w) for q, a, w in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 10
lesson(
    OA10, 1,
    "Los chants y diálogos escritos en cada ejercicio, que lee un adulto en voz alta; una hoja para tapar el guion y lápiz.",
    "Aprenderé a escuchar y notar tres sonidos propios del inglés: /w/, /th/ y /s/-/z/. Sirve para reconocer esos sonidos en chants y en diálogos muy breves antes de decirlos.",
    ["Sé que un chant tiene ritmo y palabras que se repiten.", "Sé decir palabras como water, sun y three."],
    [
        "El inglés tiene sonidos que no siempre se parecen a los del español. Hoy escuchamos tres. El sonido /w/ está al comienzo de water (agua) y window (ventana). El sonido /th/ está al comienzo de three (tres) y thank you (gracias). El sonido /s/ está en sun (sol) y el sonido /z/ en zoo (zoológico).",
        "Para notar un sonido no necesitas leer: solo escucha el comienzo de la palabra. Un chant es una rima con ritmo y repetición, por lo que ayuda mucho: oyes el mismo sonido muchas veces. Por ejemplo, en «Water, water, wet, wet, wet» oyes /w/ al comienzo en todas las palabras.",
        "Al escuchar, practica con tu boca en silencio y observa. Escucha un sonido, repítelo bajito y luego compáralo con otra palabra. Si un adulto lee dos palabras como «sip» y «zip», oirás que no suenan igual. Escuchar bien primero te ayuda a hablar mejor después.",
    ],
    [("/w/", "sonido de water y window"), ("/th/", "sonido de three y thank you"), ("/s/", "sonido de sun"), ("/z/", "sonido de zoo"), ("sound", "sonido"), ("chant", "texto con ritmo y repetición")],
    [
        ("Notar /w/", ADULT + "«Water, water, wet, wet, wet.» ¿Qué sonido oyes al comienzo de cada palabra?", ["Escucho el comienzo de water.", "Wet empieza igual.", "Es el sonido de la w."], "/w/"),
        ("Notar /th/", ADULT + "«Three, three, thank you, thank you.» ¿Qué sonido oyes al comienzo de las palabras?", ["Escucho three.", "Thank you empieza igual.", "El sonido es th."], "/th/"),
    ],
    [
        ("Pensar que /th/ es lo mismo que /s/.", "En español no existe /th/ y se reemplaza por otro sonido.", "Escucha: three no se dice «sri»."),
        ("Mirar la letra y no escuchar el sonido.", "El sonido puede cambiar con la palabra.", "Escucha el comienzo, no solo mires la letra."),
    ],
    [
        (ADULT + "«Window, water, wet.» ¿Con qué sonido empiezan las tres palabras?", "/w/", "Las tres empiezan con w."),
        (ADULT + "«Sun, sun, sun.» ¿Es un sonido /s/ o /z/?", "/s/", "Sun empieza con el sonido s."),
        (ADULT + "«Zoo, zoo, zoo.» ¿Es un sonido /s/ o /z/?", "/z/", "Zoo empieza con el sonido z."),
    ],
    [
        ("¿Qué palabra en inglés significa «agua»?", "water", "Empieza con el sonido /w/."),
        ("¿Qué significa «three»?", "Tres", "Empieza con el sonido /th/."),
        ("¿Por qué ayuda un chant a notar un sonido?", "Porque el mismo sonido se repite muchas veces", "La repetición hace fácil escucharlo."),
    ],
    [
        (ADULT + "«Three thumbs, three thumbs.» ¿Qué sonido se repite al comienzo?", "/th/", "Three y thumbs empiezan con th."),
        (ADULT + "«Wind, wind, wall.» ¿Qué sonido se repite al comienzo?", "/w/", "Las tres palabras empiezan con w."),
        (ADULT + "«Zebra, zip, zoo.» ¿Qué sonido se repite al comienzo?", "/z/", "Zebra, zip y zoo empiezan con z."),
    ],
    [
        (ADULT + "«Sip» y después «zip». ¿Suenan igual o distinto?", "Distinto", "Una empieza con /s/ y otra con /z/."),
        ("Ana dice que «three» empieza con /t/. ¿Tiene razón?", "No; empieza con /th/", "El comienzo de three es /th/."),
    ],
    [
        (ADULT + "«Water, three, sun, zoo.» ¿Qué palabra empieza con /th/?", "three", "Es la única con el sonido th."),
        (ADULT + "«Sun, sit, zoo, six.» ¿Qué palabra empieza con /z/?", "zoo", "Las otras tres empiezan con /s/."),
    ],
    [(ADULT + "«We walk in the wind.» ¿Cuántas palabras empiezan con /w/ en esta oración? Cuenta we, walk, wind.", "3", "We, walk y wind comienzan con /w/.")],
    [
        ("¿Cómo se dice «sonido» en inglés?", "sound", "Es la palabra para sonido."),
        (ADULT + "«Thank you!» ¿Qué sonido oyes al comienzo?", "/th/", "Thank empieza con th."),
        ("¿Qué haces primero para notar un sonido?", "Escucho el comienzo de las palabras", "Eso permite compararlos."),
    ],
    task("Un adulto lee dos veces este chant: «Water, water, wet, wet, wet. Three, three, thank you, thank you. Sun, sun, zoo, zoo.» Escucha y levanta la mano derecha cuando oigas /w/, la izquierda con /th/ y los dos brazos con /z/. Luego di cuál sonido te costó más oír.", "Mano derecha en water y wet; mano izquierda en three y thank you; dos brazos en zoo.", ["reconoce /w/", "reconoce /th/", "reconoce /z/", "dice qué sonido le costó"], ["nota del adulto"], ["confundir /th/ con /s/", "no mover las manos a tiempo"], "Repite con él las palabras que le costaron, más despacio, sin corregir con burla."),
    "Escucha a un adulto decir «water» y «three» tres veces y levanta la mano al oír cada uno.",
    "Busca en casa algo que empiece con /w/ en inglés, por ejemplo window o water, y di su nombre.",
)

lesson(
    OA10, 2,
    "Un espejo pequeño si tienes, los chants escritos en cada ejercicio y un adulto que lea en voz alta.",
    "Aprenderé cómo poner la boca y soltar el aire para decir /w/, /th/ y /s/. Sirve para pronunciar mejor y ser entendido.",
    ["Sé escuchar /w/, /th/, /s/ y /z/ al comienzo de las palabras.", "Sé que la boca y la lengua pueden cambiar la forma de un sonido."],
    [
        "Para /w/, redondea los labios como para decir «uu», como cuando haces un beso. Después abre rápido los labios y di «ua». La palabra water empieza así. Para /th/, pon la punta de la lengua entre los dientes, sin morderla, y suelta aire suave. Así se dice three.",
        "Para /s/, junta los dientes casi cerrados y deja que el aire pase como un hilo fino: sssss. La lengua queda detrás de los dientes, sin salir. No confundas /th/ y /s/: en /th/ la lengua se ve entre los dientes, en /s/ no se ve.",
        "Si tienes un espejo, míralo. Con /w/, tus labios se redondean. Con /th/, ves la punta de la lengua. Con /s/, no ves la lengua. Pon la mano delante de tu boca: con /th/ y /s/ sientes aire suave. Practica despacio y sin forzar. Si te duele la boca, descansa.",
    ],
    [("lips", "labios"), ("tongue", "lengua"), ("teeth", "dientes"), ("air", "aire"), ("mirror", "espejo"), ("round", "redondo")],
    [
        ("Boca para /w/", "¿Cómo pones los labios para decir water?", ["Los redondeo como para un beso.", "Digo «uu».", "Los abro rápido: ua."], "Labios redondeados"),
        ("Boca para /th/", "¿Dónde pones la lengua para decir three?", ["La punta va entre los dientes.", "No la muerdo.", "Suelto aire suave."], "Entre los dientes"),
    ],
    [
        ("Poner la lengua entre los dientes para decir /s/.", "Se mezclan los sonidos.", "Para /s/ la lengua queda detrás de los dientes."),
        ("Soplar muy fuerte en /th/.", "Se piensa que mucha fuerza ayuda.", "Basta un aire suave."),
    ],
    [
        ("¿Qué significa «tongue»?", "Lengua", "Es la parte de la boca que se mueve."),
        ("¿Qué significa «teeth»?", "Dientes", "Son los que usas para morder."),
        ("¿Qué sonido hace el aire fino con los dientes casi cerrados?", "/s/", "Es el sonido de sun."),
    ],
    [
        ("¿Cómo son los labios en /w/?", "Redondeados", "Se parecen a un beso."),
        ("¿Dónde queda la lengua en /th/?", "Entre los dientes", "Se ve la punta de la lengua."),
        ("¿Qué diferencia hay entre /th/ y /s/?", "En /th/ la lengua sale entre los dientes y en /s/ no", "La posición de la lengua cambia."),
    ],
    [
        ("Quieres decir «water». ¿Qué sonido pones al comienzo? /w/ o /s/", "/w/", "Water empieza con /w/."),
        ("Quieres decir «three». ¿Qué sonido pones al comienzo? /th/ o /w/", "/th/", "Three empieza con /th/."),
        ("Quieres decir «sun». ¿Qué sonido pones al comienzo? /s/ o /th/", "/s/", "Sun empieza con /s/."),
    ],
    [
        ("Pedro dice «sree» para three. ¿Qué debe cambiar en su boca?", "Sacar la punta de la lengua entre los dientes", "Así produce /th/ y no /s/."),
        ("Mía mira el espejo y ve la punta de la lengua entre los dientes. ¿Qué sonido está diciendo?", "/th/", "Solo en /th/ la lengua se ve entre los dientes."),
    ],
    [
        (ADULT + "«Win, wet, wall.» Con el espejo, ¿qué forma tienen tus labios al comienzo?", "Redondeados", "Esas palabras empiezan con /w/."),
        (ADULT + "«Thin, thumb, thank.» ¿Qué se ve en el espejo al comienzo de las palabras?", "La punta de la lengua", "Es la posición de /th/."),
    ],
    [("Un niño quiere decir «thank you» a su profesora pero la lengua queda detrás de los dientes y dice «sank you». ¿Qué le recomiendas?", "Poner la punta de la lengua entre los dientes", "Así dice /th/ en thank.")],
    [
        ("¿Cómo se dice «labios» en inglés?", "lips", "Son las partes que redondeas en /w/."),
        ("¿Qué sonido tiene wind al comienzo?", "/w/", "Empieza con w."),
        ("¿Cuánta fuerza usas con /th/?", "Un aire suave", "No hay que soplar fuerte."),
    ],
    task("Frente a un espejo o con un adulto, di despacio estas seis palabras: water, wind, three, thumb, sun, sit. Para cada una, di en español dónde estaban los labios o la lengua. El adulto observa y confirma.", "Water: labios redondos. Three: lengua entre los dientes. Sun: lengua detrás de los dientes.", ["labios redondeados en /w/", "lengua entre dientes en /th/", "aire fino en /s/", "explica la posición"], ["nota del adulto"], ["morder la lengua", "decir /s/ en vez de /th/"], "Practica con él despacio y celebra cada sonido logrado."),
    "Di tres veces «water, water, water» mirando tus labios en un espejo.",
    "Dibuja una boca para /w/ y otra para /th/ y escribe una palabra bajo cada una.",
)

lesson(
    OA10, 3,
    "Los pares de palabras y chants escritos en cada ejercicio; un adulto que lea en voz alta y tu mano para sentir la garganta.",
    "Aprenderé a distinguir /s/ de /z/ usando la voz. Sirve para decir y entender pares de palabras como sip y zip.",
    ["Sé decir /s/ en sun.", "Sé que mi garganta vibra cuando uso la voz."],
    [
        "El sonido /s/ y el sonido /z/ usan la boca casi igual, pero cambian en la voz. En /s/ solo sale aire, sin voz: sssss. En /z/ usas la voz y la garganta vibra: zzzzz. Es como la diferencia entre una serpiente y una abeja.",
        "Para sentirlo, pon tu mano sobre la garganta. Di «sssss»: casi no sientes nada. Di «zzzzz»: sientes un cosquilleo, una vibración. Esa es la voz. Prueba con sun (sol), que usa /s/, y con zoo (zoológico), que usa /z/.",
        "Esto es muy importante en inglés porque dos palabras pueden cambiar de significado: «sip» (sorbo) y «zip» (cierre). También lo oirás al final de las palabras: cats termina en /s/, pero dogs termina en /z/. Y is, nose (nariz) y rose (rosa) terminan con /z/.",
    ],
    [("voice", "voz"), ("throat", "garganta"), ("sip", "sorbo"), ("zip", "cierre"), ("nose", "nariz"), ("dogs", "perros")],
    [
        ("Sentir la voz en /z/", "Pones la mano en la garganta y dices «zzzzz». ¿Qué sientes?", ["Digo zzzz.", "Con la mano siento algo.", "Es una vibración."], "Vibración (voz)"),
        ("Distinguir un par", ADULT + "«Sip... zip.» ¿Cuál tiene voz al comienzo?", ["Escucho sip: aire.", "Escucho zip: voz.", "Zip tiene /z/."], "zip"),
    ],
    [
        ("Decir siempre /s/ aunque haya z.", "En español la z suena como s en Chile.", "En inglés /z/ lleva voz: sientes la vibración."),
        ("Decir dogs terminando en /s/.", "Se pierde la voz al final.", "Dogs termina en /z/, con voz."),
    ],
    [
        ("¿Qué sientes en la garganta con /z/?", "Vibración", "La voz hace vibrar la garganta."),
        ("¿Qué significa «nose»?", "Nariz", "Termina en /z/."),
        ("¿Qué sonido tiene sun al comienzo?", "/s/", "Solo aire, sin voz."),
    ],
    [
        ("¿Cuál es la diferencia entre /s/ y /z/?", "/s/ no usa voz y /z/ sí", "La voz es la diferencia principal."),
        ("¿Cómo compruebas si un sonido tiene voz?", "Pongo la mano en la garganta y siento la vibración", "Es una prueba fácil."),
        ("¿Por qué es importante distinguir /s/ y /z/?", "Porque cambian palabras como sip y zip", "El sonido cambia el significado."),
    ],
    [
        (ADULT + "«Zoo.» ¿Empieza con /s/ o /z/?", "/z/", "Zoo lleva voz al comienzo."),
        (ADULT + "«Sun.» ¿Empieza con /s/ o /z/?", "/s/", "Sun no lleva voz."),
        ("Palabra: dogs. ¿Termina con /s/ o /z/?", "/z/", "Después de la g se usa voz."),
    ],
    [
        ("Ana dice «sip» y «zip» igual. ¿Qué debe sentir en la mano para decir zip?", "Vibración en la garganta", "Zip empieza con /z/."),
        ("Palabra: cats. ¿Termina con voz o sin voz?", "Sin voz, /s/", "Después de la t suena aire."),
    ],
    [
        (ADULT + "«Rose, rose, rose.» ¿Qué sonido oyes al final?", "/z/", "Rose termina con voz."),
        (ADULT + "«Bus, bus, bus.» ¿Qué sonido oyes al final?", "/s/", "Bus termina sin voz."),
    ],
    [("Un niño quiere decir «zebra» en el zoológico. ¿Con qué sonido empieza y qué siente en la garganta?", "Con /z/ y siente vibración", "Zebra empieza con el sonido de voz.")],
    [
        ("¿Cómo se dice «voz» en inglés?", "voice", "Es la palabra para voz."),
        ("¿Qué sonido tiene is al final?", "/z/", "Is lleva voz al final."),
        ("¿Qué significa «sip»?", "Sorbo", "Empieza con /s/."),
    ],
    task("Con la mano en la garganta, di cuatro veces cada palabra y marca en una tabla de dos columnas si sientes voz (/z/) o no (/s/). En sun, zoo, sit y zip escucha el comienzo; en bus y rose escucha el final. Luego pide a un adulto que lea «sip» y «zip» y tú dices cuál oyes.", "Comienzo: sun /s/, zoo /z/, sit /s/, zip /z/. Final: bus /s/, rose /z/.", ["usa la mano en la garganta", "clasifica seis palabras", "distingue sip y zip", "dice un ejemplo"], ["la tabla", "nota del adulto"], ["no sentir la vibración", "decir todas como /s/"], "Repite con él las palabras con /z/ y celebra cuando sienta la vibración."),
    "Di «sssss» y «zzzzz» tres veces con la mano en la garganta.",
    "Pide a alguien que lea en inglés zoo, sun, zip, sit y escribe /z/ o /s/ para cada una.",
)

lesson(
    OA10, 4,
    "Los chants escritos en cada ejercicio, un objeto para marcar el pulso (una cuchara de madera o una mesa para golpear suave) y un adulto que lea.",
    "Aprenderé a decir chants cortos con ritmo, marcando las sílabas fuertes y cuidando /w/, /th/ y /s/-/z/. Sirve para practicar los sonidos de forma entretenida.",
    ["Sé que los chants tienen ritmo.", "Sé decir /w/, /th/ y /s/-/z/ con ayuda."],
    [
        "El ritmo (rhythm) es el pulso de un chant, como un tambor suave. En inglés, algunas sílabas son más fuertes que otras. La sílaba fuerte se llama stress y la sentimos más larga y más fuerte. En este cuaderno las sílabas fuertes van en MAYÚSCULAS: WA-ter, THREE, SUN.",
        "Para decir un chant, marca el pulso con la mano o con una cuchara suave. Aplaude en cada sílaba fuerte. Por ejemplo, en «WA-ter, WA-ter, WET, WET, WET» aplaudes en WA, WA, WET, WET, WET. Así el chant suena parejo y fácil de recordar.",
        "Muchos chants tienen rimas: palabras que terminan con el mismo sonido, como sun y run, o zip y sip. Mientras dices el chant, cuida los sonidos. Pon los labios redondos en /w/. Muestra la punta de la lengua en /th/. Siente la vibración en /z/. Si te equivocas, no pares: sigue el ritmo y mejora la siguiente vez. Decir un chant varias veces ayuda a que tu boca aprenda.",
    ],
    [("chant", "texto con ritmo"), ("rhythm", "ritmo"), ("stress", "sílaba fuerte"), ("clap", "aplaudir"), ("beat", "pulso"), ("again", "otra vez")],
    [
        ("Marcar el pulso", "Chant: «WA-ter, WA-ter, WET, WET, WET.» ¿En cuántos lugares aplaudes?", ["Aplaudo en cada sílaba en mayúsculas.", "WA, WA, WET, WET, WET.", "Son cinco."], "5"),
        ("Cuidar el sonido", "En «THREE, THREE, THANK you», ¿qué sonido repites al comienzo de las palabras fuertes?", ["Veo THREE y THANK.", "Empiezan con th.", "La lengua sale entre los dientes."], "/th/"),
    ],
    [
        ("Decir todas las sílabas igual de fuertes.", "Se pierde el ritmo del chant.", "Marca más fuerte las sílabas en mayúsculas."),
        ("Parar cuando uno se equivoca.", "Se cree que hay que empezar de nuevo.", "Sigue el ritmo y mejora en la próxima vuelta."),
    ],
    [
        ("¿Qué significa «rhythm»?", "Ritmo", "Es el pulso de un chant."),
        ("¿Qué significa «clap»?", "Aplaudir", "Se usa para marcar el pulso."),
        ("¿Cómo se marcan las sílabas fuertes en este cuaderno?", "Con mayúsculas", "Así se ven fácilmente."),
    ],
    [
        ("¿Para qué sirve marcar el pulso en un chant?", "Para decirlo parejo y recordarlo", "El ritmo organiza las palabras."),
        ("¿Qué haces si te equivocas en un sonido durante el chant?", "Sigo el ritmo y mejoro la próxima vez", "No hay que parar."),
        ("¿Qué sílabas se dicen más fuertes?", "Las sílabas con stress", "Son las que van en mayúsculas."),
    ],
    [
        ("Chant: «SUN, SUN, SIT, SIT.» ¿Cuántas veces aplaudes?", "4", "Hay cuatro sílabas fuertes."),
        ("Chant: «WIND, WIND, WA-ter.» ¿Cuántos aplausos hay?", "3", "Aplaudes en WIND, WIND y WA, la sílaba fuerte de water."),
        ("Chant: «ZOO, ZOO, ZE-bra.» ¿En qué sílaba de zebra aplaudes?", "ZE", "La sílaba fuerte va en mayúsculas."),
    ],
    [
        ("Ana dice el chant sin pulso y se desordena. ¿Qué puede hacer?", "Aplaudir en las sílabas fuertes", "El pulso la ayuda a mantener el ritmo."),
        ("En «THIN, THIN, THREE, THREE» alguien dice «sin, sin». ¿Qué sonido está usando mal?", "Usa /s/ en vez de /th/", "Debe sacar la lengua entre los dientes."),
    ],
    [
        (ADULT + "«WET, WET, WIND. THREE, THREE, THIN.» Escribe cuántos aplausos hay en la primera línea.", "3", "Wet, wet, wind son tres sílabas fuertes."),
        ("Completa con una palabra con /z/: «ZOO, ZOO, ___, ZIP.» Elige entre zebra, sun, wet.", "zebra", "Solo zebra empieza con /z/."),
    ],
    [("En la clase, el profesor da el pulso con una cuchara suave y pide: «THREE, THREE, THANK you». ¿Qué debes hacer con la lengua en cada THREE y THANK?", "Ponerla entre los dientes", "El sonido es /th/.")],
    [
        ("¿Cómo se dice «pulso» en inglés?", "beat", "Es el golpe suave del ritmo."),
        ("Una rima es cuando dos palabras terminan con el mismo sonido. ¿Qué palabra rima con sun: run, zoo o wet?", "run", "Sun y run terminan igual."),
        ("¿Qué sílaba aplaudes en «WA-ter»?", "WA", "Es la sílaba fuerte."),
    ],
    task("Di este chant tres veces con un adulto y aplaude en las sílabas en mayúsculas: «WA-ter, WA-ter, WET, WET, WET. THREE, THREE, THANK you. SUN, SUN, ZOO, ZOO.» Cuida los labios en /w/, la lengua en /th/ y la voz en /z/. Después di cuál línea te salió mejor.", "Aplaudo en WA, WA, WET, WET, WET; en THREE, THREE, THANK; en SUN, SUN, ZOO, ZOO.", ["marca el pulso", "mantiene el ritmo", "cuida /w/, /th/ y /z/", "dice la línea que mejor le salió"], ["nota del adulto"], ["perder el ritmo", "decir /s/ en vez de /th/"], "Elogia el ritmo y repite despacio la línea más difícil."),
    "Aplaude y di «THREE, THREE, THANK you» cinco veces.",
    "Inventa un chant de dos líneas con las palabras wet, wind y water y di con las palmas.",
)

lesson(
    OA10, 5,
    "Los diálogos escritos en cada ejercicio, un adulto para hacer el otro papel y una hoja para tapar el guion.",
    "Aprenderé a usar /w/, /th/, /s/ y /z/ en un diálogo muy breve. Sirve para hablar con otra persona en inglés cuidando mi pronunciación.",
    ["Sé decir chants con /w/, /th/ y /s/-/z/.", "Sé que un diálogo tiene dos voces."],
    [
        "Un diálogo (dialogue) es una conversación breve entre dos personas. Después de practicar los sonidos en chants, puedes usarlos en frases cortas. En un diálogo, uno habla y el otro responde. Así practicas los sonidos con sentido.",
        "Mira este diálogo: «A: Is it a zebra? B: No, it is a dog. A: Thank you!» En él hay muchos sonidos de práctica: /z/ en zebra e is, /th/ en thank. También hay /s/ en «yes». Antes de decirlo, léelo despacio y marca las palabras donde debes cuidar un sonido.",
        "Cuando hables, mira a la otra persona, usa una voz clara y no hables muy rápido. Si te equivocas, repite la palabra con calma. Puedes cambiar una palabra del diálogo por otra y practicar con eso, pero siempre cuidando los sonidos. Lo importante es comunicarse, no ser perfecto.",
    ],
    [("dialogue", "diálogo"), ("Is it a...?", "¿Es un...?"), ("No, it is...", "No, es..."), ("Thank you", "gracias"), ("yes / no", "sí / no"), ("again", "otra vez")],
    [
        ("Identificar sonidos en el diálogo", "A: Is it a zebra? B: No, it is a dog. ¿Qué palabra tiene /z/ al comienzo?", ["Leo las palabras.", "Zebra empieza con z.", "Es la única."], "zebra"),
        ("Cambiar una palabra", "Cambia zebra por sock (calcetín) en «Is it a zebra?». ¿Qué sonido cuidas ahora?", ["Digo Is it a sock?", "Sock empieza con /s/.", "Cuido el aire sin voz."], "/s/"),
    ],
    [
        ("Hablar muy rápido y perder los sonidos.", "Se quiere terminar pronto.", "Habla despacio y con voz clara."),
        ("Quedarse callado por miedo a equivocarse.", "Se cree que debe ser perfecto.", "Equivocarse es parte de aprender; repite con calma."),
    ],
    [
        ("¿Qué significa «dialogue»?", "Diálogo", "Es una conversación breve."),
        ("¿Cómo se dice «gracias» en inglés?", "thank you", "Empieza con /th/."),
        ("¿Qué significa «No, it is a dog»?", "No, es un perro", "It is significa es y dog es perro."),
    ],
    [
        ("¿Para qué sirve usar los sonidos dentro de un diálogo?", "Para practicarlos en una conversación real", "Así se usan con sentido."),
        ("¿Cómo hablas en un diálogo para cuidar los sonidos?", "Despacio, con voz clara y mirando a la otra persona", "Eso ayuda a que te entiendan."),
        ("¿Qué haces si te equivocas en una palabra?", "La repito con calma", "Repetir ayuda a aprender."),
    ],
    [
        ("A: Is it a zoo? B: ___, it is. Es un zoológico de verdad. Completa con yes o no.", "Yes", "Si es un zoo, la respuesta es yes."),
        ("En «Thank you», ¿qué sonido hay al comienzo?", "/th/", "Thank empieza con th."),
        ("En el diálogo «A: Is it water? B: Yes!» ¿qué palabra tiene /w/?", "water", "Water empieza con /w/."),
    ],
    [
        ("Un niño dice «Sank you» a su profesora. ¿Qué sonido cambia y cómo?", "Usa /s/ en vez de /th/; debe poner la lengua entre los dientes", "Thank empieza con /th/."),
        ("A: Is it a zebra? B: Yes. Si cambias zebra por wolf (lobo), ¿qué sonido pasa a estar al comienzo?", "/w/", "Wolf empieza con /w/."),
    ],
    [
        ("Ordena el diálogo con números: (1) B: No, it is a farm. (2) A: Is it a zoo? (3) A: Thank you!", "2, 1, 3", "Primero A pregunta, luego B responde y A agradece."),
        ("Elige la palabra que empieza con /th/: three, wet o sun.", "three", "Solo three empieza con el sonido th."),
    ],
    [("Una amiga te pregunta: «Is it water?» mientras te muestra un vaso con agua. ¿Qué respondes en inglés con dos palabras?", "Yes, it is", "El vaso tiene agua, así que dices yes.")],
    [
        ("¿Cómo se dice «sí» en inglés?", "yes", "Es la palabra para sí."),
        ("¿Qué palabra de «Is it a zebra?» tiene /z/?", "zebra", "Empieza con z."),
        ("¿Qué haces si hablas muy rápido y no te entienden?", "Hablo más despacio y claro", "Así se oyen mejor los sonidos."),
    ],
    task("Con un adulto, di este diálogo con dos cambios. Original: «A: Is it a zebra? B: No, it is a dog. A: Thank you!» Primero dilo igual. Luego cambia «a zebra» por «water» y «a dog» por «a window». Cuida /z/, /w/ y /th/. El adulto hace el papel de A.", "«A: Is it water? B: No, it is a window. A: Thank you!»", ["mantiene el orden del diálogo", "cambia las palabras", "cuida /w/ y /th/", "habla claro"], ["nota del adulto"], ["decir sank en vez de thank", "hablar muy rápido"], "Elogia el esfuerzo y repite la palabra más difícil con él despacio."),
    "Di «Thank you!» a alguien de tu casa, cuidando el sonido /th/.",
    "Inventa otro diálogo de tres líneas con las palabras sun, zoo y yes.",
)

# ================================================================ OA 11
lesson(
    OA11, 1,
    "Las frases y objetos escritos en cada ejercicio (un lápiz, un cuaderno, un libro) y un adulto para practicar turnos.",
    "Aprenderé frases muy frecuentes para participar en la sala de clases, como pedir algo con «please» y agradecer. Sirve para interactuar en inglés con mis compañeros y profesores.",
    ["Sé decir hello, goodbye y thank you.", "Sé nombres de objetos de la escuela: pencil, book, bag."],
    [
        "En clase usamos frases cortas todos los días. Para pedir un objeto: «Can I have a pencil, please?» (¿Puedo tener un lápiz, por favor?). Para agradecer: «Thank you». Para responder: «You're welcome» (de nada). Si necesitas ayuda: «Help, please».",
        "Una interacción tiene turnos (turns). Primero habla uno y luego responde el otro. Por ejemplo: «Can I have a pencil, please?» «Yes, here you are.» «Thank you.» «You're welcome.» Escuchar al otro y esperar tu turno es parte de participar.",
        "Los gestos y los objetos ayudan. Si dices «pencil» mientras señalas un lápiz, te entienden mejor. Si no entiendes, puedes decir «Again, please» (otra vez, por favor) o «I don't understand» (no entiendo). Está bien pedir ayuda.",
    ],
    [("Can I have...?", "¿Puedo tener...?"), ("please", "por favor"), ("Thank you", "gracias"), ("You're welcome", "de nada"), ("Here you are", "aquí tienes"), ("Again, please", "otra vez, por favor")],
    [
        ("Pedir un objeto", "Necesitas un lápiz. ¿Qué dices en inglés?", ["Uso Can I have.", "Digo a pencil.", "Cierro con please."], "Can I have a pencil, please?"),
        ("Responder un agradecimiento", "Un compañero dice «Thank you». ¿Qué respondes?", ["Escucho thank you.", "Respondo con una frase amable.", "Es you're welcome."], "You're welcome"),
    ],
    [
        ("Pedir sin decir please.", "Se olvida la palabra de cortesía.", "Agrega please al final."),
        ("Hablar al mismo tiempo que el otro.", "No se respeta el turno.", "Espera a que termine y responde."),
    ],
    [
        ("¿Qué significa «please»?", "Por favor", "Es una palabra de cortesía."),
        ("¿Qué significa «You're welcome»?", "De nada", "Se dice después de thank you."),
        ("¿Qué significa «Here you are»?", "Aquí tienes", "Se dice al entregar algo."),
    ],
    [
        ("¿Qué es un turno en un diálogo?", "El momento en que me toca hablar", "Primero habla uno y luego el otro."),
        ("¿Cómo ayudas a que te entiendan con un objeto?", "Lo señalo mientras digo la palabra", "El gesto apoya la palabra."),
        ("¿Qué dices en inglés si no entiendes?", "Again, please o I don't understand", "Son frases útiles."),
    ],
    [
        ("Necesitas un libro. Completa: «Can I have a ___, please?»", "book", "Book es libro."),
        ("Un compañero te pasa tu lápiz y dices... (a) «Thank you.» (b) «Goodbye.»", "a", "Se agradece cuando recibes algo."),
        ("Te dicen «Again, please». ¿Qué te piden?", "Que lo repitas", "Again significa otra vez."),
    ],
    [
        ("Leo pide un lápiz y dice «Can I have a pencil?» sin cortesía. ¿Qué palabra le falta para ser amable?", "please", "Se agrega al final."),
        ("Ordena el mini diálogo: (1) «Yes, here you are.» (2) «Can I have a pencil, please?» (3) «Thank you.»", "2, 1, 3", "Pide, entrega y agradece."),
    ],
    [
        ("Completa el diálogo: A: «Thank you.» B: «___.»", "You're welcome", "Es la respuesta habitual."),
        ("Ana no entiende una frase y quiere que se la repitan. ¿Qué puede decir con dos palabras?", "Again, please", "Es una petición amable."),
    ],
    [("En una clase, Marta necesita una goma. Lo dice en inglés a su compañero, que se la pasa. ¿Qué dice el compañero al pasársela?", "Here you are", "Es lo que se dice al entregar algo.")],
    [
        ("¿Cómo se dice «de nada» en inglés?", "You're welcome", "Responde al thank you."),
        ("¿Cómo se dice «por favor» en inglés?", "please", "Se usa al pedir."),
        ("¿Qué significa «I don't understand»?", "No entiendo", "Se usa para pedir ayuda."),
    ],
    task("Con un adulto, practica este mini diálogo usando tres objetos de tu casa: un lápiz, un cuaderno y un libro. Tú pides: «Can I have a pencil, please?», el adulto responde «Here you are» y tú dices «Thank you». Repite para el cuaderno (notebook) y el libro (book). Luego intercambien turnos.", "«Can I have a notebook, please?» «Here you are.» «Thank you.» «You're welcome.»", ["pide con please", "agradece", "espera su turno", "usa el nombre del objeto"], ["nota del adulto"], ["olvidar please", "hablar en el turno del otro"], "Reconoce las frases correctas y repite las que se le olvidaron."),
    "Di «Thank you» y «You're welcome» en una conversación con alguien de tu casa.",
    "Haz una lista de cinco objetos de la sala y practica «Can I have a ___, please?» con cada uno.",
)

lesson(
    OA11, 2,
    "Los modelos escritos en cada ejercicio, un objeto de tu casa (un peluche, un lápiz) y un adulto como compañero.",
    "Aprenderé a presentarme y a presentar un objeto con frases muy simples y con apoyo de gestos. Sirve para participar en inglés al comienzo de una conversación.",
    ["Sé decir hello y goodbye.", "Sé mi nombre y mi edad."],
    [
        "Para presentarte usa el modelo «Hello! I'm Ana.» (Hola, soy Ana). Para decir tu edad: «I'm seven» (tengo siete años). Para decir algo que te gusta: «I like dogs» (me gustan los perros). Todas estas frases son cortas y muy frecuentes.",
        "También puedes presentar un objeto: «This is my bear» (este es mi oso). Para decir cómo es: «It is brown» (es café). Mientras hablas, muestra el objeto con la mano o los dedos. El gesto ayuda a que te entiendan.",
        "No es necesario decir datos privados. Basta con tu nombre de pila, tu edad y algo que te gusta. No digas tu dirección ni tu teléfono. Si no recuerdas una palabra, usa un gesto o di «I don't know» (no sé). Practicar varias veces con un adulto te da seguridad.",
    ],
    [("I'm...", "yo soy / tengo (con edad)"), ("my", "mi"), ("This is...", "este es / esta es"), ("It is...", "es..."), ("I like...", "me gusta..."), ("seven", "siete")],
    [
        ("Presentarme", "Te llamas Ana y tienes siete años. ¿Qué dices?", ["Digo hello.", "Digo mi nombre con I'm.", "Digo la edad con I'm."], "Hello! I'm Ana. I'm seven."),
        ("Presentar un objeto", "Tienes un oso café. ¿Cómo lo presentas con dos frases?", ["Digo This is my bear.", "Digo It is brown.", "Muestro el oso."], "This is my bear. It is brown."),
    ],
    [
        ("Decir «I am have seven».", "Se mezclan dos formas de decir la edad.", "Di «I'm seven»."),
        ("Contar la dirección para presentarse.", "Se cree que hay que dar muchos datos.", "Basta nombre, edad y algo que te gusta."),
    ],
    [
        ("¿Qué significa «I'm seven»?", "Tengo siete años", "En inglés se usa I'm más el número."),
        ("¿Qué significa «my»?", "Mi", "Muestra que algo es mío."),
        ("¿Qué significa «This is my bear»?", "Este es mi oso", "This is señala algo."),
    ],
    [
        ("¿Qué tres cosas dices para presentarte de forma segura?", "Mi nombre, mi edad y algo que me gusta", "Son datos simples y no privados."),
        ("¿Para qué sirve el gesto al presentar un objeto?", "Para que me entiendan mejor", "El gesto apoya las palabras."),
        ("¿Qué dices si no recuerdas una palabra?", "I don't know o uso un gesto", "Es una forma de seguir."),
    ],
    [
        ("Completa: «Hello! ___ Leo.» (Soy)", "I'm", "I'm significa soy."),
        ("Tienes ocho años. Completa: «I'm ___.»", "eight", "Eight es ocho."),
        ("Quieres decir «me gustan los gatos». Completa: «I ___ cats.»", "like", "Like significa gustar."),
    ],
    [
        ("Un niño dice «Hello! I'm seven. I'm Pedro». ¿Qué orden sería más natural?", "Hello! I'm Pedro. I'm seven.", "Primero se dice el nombre."),
        ("Lucía quiere presentarse y dice su dirección. ¿Qué le recomiendas?", "No decirla, y decir su nombre, edad y algo que le gusta", "La dirección es un dato privado."),
    ],
    [
        ("Ordena para formar una frase: bear / is / This / my. Escribe la frase.", "This is my bear", "This va primero, luego is, my y bear."),
        ("Presenta tu peluche: pon en orden las frases (1) It is white. (2) This is my rabbit.", "2, 1", "Primero se nombra el objeto, luego se describe."),
    ],
    [("Es el primer día de clases. Una niña nueva se acerca a ti. ¿Qué dices para presentarte si te llamas Sofía y tienes siete años?", "Hello! I'm Sofía. I'm seven.", "Es una presentación simple y segura.")],
    [
        ("¿Cómo se dice «mi» en inglés?", "my", "Se usa antes del nombre del objeto."),
        ("¿Qué significa «I like dogs»?", "Me gustan los perros", "Like es gustar."),
        ("¿Qué datos no debes decir al presentarte?", "Dirección y teléfono", "Son datos privados."),
    ],
    task("Con un adulto, practica tres frases: (1) «Hello! I'm ___. I'm ___.» con tu nombre y tu edad. (2) «I like ___.» con algo que te gusta. (3) Presenta tu objeto con «This is my ___. It is ___.», por ejemplo un peluche. Mira a la persona y muestra el objeto con la mano.", "«Hello! I'm Ana. I'm seven. I like dogs. This is my bear. It is brown.»", ["dice nombre y edad", "dice algo que le gusta", "presenta un objeto", "no da datos privados"], ["nota del adulto"], ["decir la dirección", "mezclar I am have"], "Valora la claridad y repite despacio la frase más difícil."),
    "Di «Hello! I'm ___. I'm ___.» frente a un espejo.",
    "Presenta a un peluche con «This is my ___. It is ___.» y escríbelo en una tarjeta.",
)

lesson(
    OA11, 3,
    "Las frases escritas en cada ejercicio, algunos objetos de casa (un lápiz, una taza, una pelota) y un adulto para practicar.",
    "Aprenderé a preguntar cómo se dice una palabra en inglés y a pedir ayuda cuando no sé. Sirve para seguir hablando aunque me falte una palabra.",
    ["Sé algunos nombres de objetos en inglés.", "Sé que puedo pedir ayuda."],
    [
        "Cuando no sabes una palabra, puedes preguntar: «How do you say 'perro' in English?» (¿Cómo se dice «perro» en inglés?). La respuesta puede ser «Dog». También puedes preguntar al revés: «How do you say 'dog' in Spanish?» (¿Cómo se dice «dog» en español?).",
        "Delante de palabras que empiezan con vocal, como apple (manzana), egg (huevo) u orange (naranja), se usa an: «It's an apple». Delante de cup o ball se usa a. Otra pregunta útil es «What's this?» (¿qué es esto?). La respuesta es «It's a cup» (es una taza), por ejemplo. Si no entendiste, puedes decir «Sorry?» (¿perdón?) o «Again, please» (otra vez, por favor). Cuando entiendas, di «Thank you».",
        "Usa objetos reales para apoyar. Puedes tomar una taza, señalarla y preguntar «What's this?». Así tu compañero ve de qué hablas. Es mejor preguntar que quedarse en silencio. Los buenos hablantes preguntan mucho.",
    ],
    [("How do you say...?", "¿Cómo se dice...?"), ("in English / in Spanish", "en inglés / en español"), ("What's this?", "¿qué es esto?"), ("It's a...", "es un / una..."), ("Sorry?", "¿perdón?"), ("cup", "taza")],
    [
        ("Preguntar una palabra", "Quieres saber cómo se dice «pelota» en inglés. ¿Qué preguntas?", ["Uso How do you say.", "Digo la palabra en español.", "Agrego in English."], "How do you say 'pelota' in English?"),
        ("Preguntar qué es", "Señalas una taza y quieres preguntar qué es. ¿Qué dices?", ["Señalo el objeto.", "Uso What's this?", "Espero la respuesta It's a cup."], "What's this?"),
    ],
    [
        ("Quedarse callado cuando no se sabe una palabra.", "Se piensa que preguntar es malo.", "Pregunta con How do you say...? y sigue la conversación."),
        ("Preguntar sin señalar el objeto.", "El compañero no sabe de qué hablas.", "Señala o muestra el objeto."),
    ],
    [
        ("¿Qué significa «in English»?", "En inglés", "Indica el idioma."),
        ("¿Qué significa «What's this?»", "¿Qué es esto?", "Se usa señalando algo."),
        ("¿Qué significa «Sorry?»", "¿Perdón?", "Se dice cuando no se entendió."),
    ],
    [
        ("¿Para qué sirve «How do you say...?»", "Para preguntar el nombre de una palabra", "Ayuda cuando no sé cómo decir algo."),
        ("¿Por qué es útil mostrar el objeto al preguntar?", "Porque ve de qué hablo", "El objeto ayuda a ser entendido."),
        ("¿Qué respondes cuando entiendes?", "Thank you", "Es amable y claro."),
    ],
    [
        ("Completa: «How do you ___ 'gato' in English?»", "say", "Say es decir."),
        ("Respondes a «What's this?» mostrando una taza. Completa: «It's a ___.»", "cup", "Cup es taza."),
        ("Quieres que repitan lo que dijeron. ¿Qué dices con una palabra?", "Sorry?", "Es una forma de pedir repetición."),
    ],
    [
        ("Un niño dice: «How you say pelota in English?» ¿Qué palabra le falta?", "do", "La pregunta correcta es How do you say...?"),
        ("Pedro señala una pelota y pregunta «What's this?». Ana responde «It's a ball». ¿Qué significa la respuesta?", "Es una pelota", "Ball es pelota."),
    ],
    [
        ("Ordena el diálogo: (1) «It's a bird.» (2) «What's this?» (3) «Thank you.»", "2, 1, 3", "Pregunta, responde y agradece."),
        ("A pregunta «How do you say 'libro' in English?». ¿Qué palabra responde B?", "Book", "Libro en inglés es book."),
    ],
    [("En el recreo, tu amigo señala una manzana en una imagen y pregunta «What's this?». Respondes en inglés con tres palabras.", "It's an apple", "Apple es manzana y empieza con vocal, por eso lleva an.")],
    [
        ("¿Cómo se dice «¿Qué es esto?» en inglés?", "What's this?", "Se usa para preguntar por un objeto."),
        ("¿Qué haces si no sabes una palabra en inglés?", "Pregunto How do you say...?", "Así sigo hablando."),
        ("¿Qué significa «It's a cup»?", "Es una taza", "Cup es taza."),
    ],
    task("Con un adulto y tres objetos de casa (por ejemplo una taza, una pelota y un lápiz), haz estas preguntas: (1) Señala la taza y pregunta «What's this?». (2) Pregunta «How do you say 'pelota' in English?». (3) Si no entiendes, di «Sorry?» o «Again, please». El adulto responde en inglés y tú dices «Thank you».", "«What's this?» «It's a cup.» «Thank you.»", ["pregunta con What's this?", "pregunta How do you say...?", "pide repetición si hace falta", "agradece"], ["nota del adulto"], ["quedarse en silencio", "olvidar señalar el objeto"], "Valora que haya preguntado y ayúdale a repetir la respuesta."),
    "Señala tres objetos y di «What's this?» a alguien de tu casa.",
    "Haz una tarjeta con «How do you say...?» y tres palabras en español para preguntar.",
)

lesson(
    OA11, 4,
    "El modelo escrito en cada ejercicio, un objeto o una imagen que quieras mostrar, y un adulto o un peluche como público.",
    "Aprenderé a hacer una mini-presentación muy breve en inglés con un objeto o una imagen. Sirve para comunicar algo conocido con frases simples.",
    ["Sé presentarme y presentar un objeto.", "Sé nombres de colores y animales."],
    [
        "Una mini-presentación (presentation) es hablar de algo en tres o cuatro frases. Tiene un comienzo, un medio y un final. Comienzo: «Hello! This is my dog.» Medio: «It is brown. It is big.» Final: «Thank you!» Usa un objeto o una imagen para apoyar lo que dices.",
        "Puedes presentar un tema de otra asignatura. En ciencias: «This is a plant. It is green. It needs water.» En matemática: «I have five pencils. They are red.» Usa palabras que ya conoces y gestos. No necesitas muchas palabras: lo importante es hablar claro.",
        "Antes de presentar, ensaya en privado con un peluche o frente al espejo. Hazlo despacio. Mira a la persona o a tu público. Mientras hablas, muestra la imagen o el objeto. Si te equivocas, respira y sigue. Puedes decir «Sorry» y repetir la frase.",
    ],
    [("presentation", "presentación"), ("Hello! This is...", "Hola, este es..."), ("It is...", "es..."), ("It needs water", "necesita agua"), ("plant", "planta"), ("Thank you!", "¡gracias!")],
    [
        ("Armar una presentación", "Tienes un dibujo de un gato negro. Escribe tres frases: saludo, descripción y cierre.", ["Saludo y nombre.", "Una descripción.", "Cierro con thank you."], "Hello! This is my cat. It is black. Thank you!"),
        ("Presentar un tema de ciencias", "Muestras una planta verde. ¿Qué dices en tres frases?", ["Digo This is a plant.", "Digo It is green.", "Digo It needs water."], "This is a plant. It is green. It needs water."),
    ],
    [
        ("Hablar sin mostrar el objeto o la imagen.", "No se usa el apoyo.", "Muestra el objeto mientras hablas."),
        ("Quedarse en blanco y parar.", "Se cree que hay que decirlo todo perfecto.", "Respira, di «Sorry» y repite la frase."),
    ],
    [
        ("¿Qué significa «presentation»?", "Presentación", "Es hablar de algo ante otros."),
        ("¿Qué significa «It needs water»?", "Necesita agua", "Needs es necesita."),
        ("¿Con qué frase terminas tu presentación?", "Thank you", "Es una despedida cortés."),
    ],
    [
        ("¿Qué partes tiene una mini-presentación?", "Un comienzo, un medio y un final", "Así se ordena lo que digo."),
        ("¿Qué haces antes de presentar?", "Ensayo con un peluche o frente al espejo", "El ensayo da seguridad."),
        ("¿Para qué sirve el objeto o la imagen?", "Para apoyar lo que digo", "Ayuda a que me entiendan."),
    ],
    [
        ("Completa el comienzo: «Hello! ___ is my dog.»", "This", "This is my dog es el modelo."),
        ("Quieres decir que tu pelota es roja. Completa: «It ___ red.»", "is", "It is red."),
        ("Terminas tu presentación. Completa: «___ you!»", "Thank", "Thank you es el cierre."),
    ],
    [
        ("Ana dice: «It is brown. Hello! This is my dog. Thank you.» ¿Qué orden debe corregir?", "Debe empezar con el saludo", "El comienzo va primero."),
        ("Un niño presenta un conejo y no lo muestra. ¿Qué mejora le sugieres?", "Mostrar el dibujo o el peluche", "El apoyo ayuda a que lo entiendan."),
    ],
    [
        ("Presentas cinco lápices rojos. Completa: «I have ___ red pencils.» con la palabra de cinco.", "five", "Five es cinco."),
        ("Ordena: (1) «Thank you!» (2) «Hello! This is my bird.» (3) «It is blue.»", "2, 3, 1", "Saludo, descripción y cierre."),
    ],
    [("Mañana presentas un dibujo de una rana verde en clase de ciencias. Escribe las tres frases en inglés que dirás, con Hello!, This is a... e It is...", "Hello! This is a frog. It is green.", "Saludo, nombre del animal y color.")],
    [
        ("¿Cómo se dice «planta» en inglés?", "plant", "Se parece mucho al español."),
        ("¿Cómo comienza la presentación de un objeto?", "Hello! This is...", "Es el modelo del comienzo."),
        ("¿Qué haces si te equivocas?", "Respiro y repito la frase", "Equivocarse es normal."),
    ],
    task("Elige un objeto o imagen y haz una mini-presentación a un adulto con cuatro frases: «Hello! This is my ___. It is ___. It is ___. Thank you!» Ensaya primero con un peluche. Muestra el objeto mientras hablas. Puedes usar un tema de ciencias o matemática, como una planta o cinco lápices.", "«Hello! This is my bear. It is brown. It is soft. Thank you!»", ["usa saludo, medio y cierre", "muestra el objeto", "habla claro", "usa frases simples en inglés"], ["nota del adulto"], ["no mostrar el objeto", "olvidar el cierre"], "Valora el uso del apoyo y propone repetir con más calma si hubo prisa."),
    "Ensaya tres veces «Hello! This is my ___.» con un objeto tuyo.",
    "Cambia tu presentación para otro objeto y compara cuáles palabras cambian.",
)

lesson(
    OA11, 5,
    "El diálogo modelo escrito en cada ejercicio, un adulto como compañero y objetos o imágenes de apoyo.",
    "Aprenderé a cambiar un diálogo modelo y a seguirlo aunque cambie la conversación. Sirve para participar con flexibilidad, no solo repetir de memoria.",
    ["Sé saludar, presentarme y agradecer.", "Sé preguntar What's this?"],
    [
        "Un diálogo modelo se puede cambiar. Por ejemplo: «A: Hello! How are you? B: I'm fine, thank you. And you? A: I'm happy.» Puedes cambiar fine por happy o tired (cansado). La estructura se mantiene, las palabras cambian.",
        "A veces la conversación no sale como esperabas. Quizá el otro dice algo distinto. Entonces escucha, usa los gestos y responde con una frase simple. Si no entiendes, usa «Sorry?», «Again, please» o «I don't understand». Si no sabes una palabra, pregunta «How do you say...?».",
        "Ser flexible (flexible) significa adaptarte. No importa si no dices la frase exacta del modelo. Lo que importa es que te entiendan y entender al otro. Practica con diferentes compañeros y diferentes palabras para ganar seguridad.",
    ],
    [("How are you?", "¿cómo estás?"), ("I'm fine", "estoy bien"), ("And you?", "¿y tú?"), ("happy / tired", "contento / cansado"), ("flexible", "que se adapta"), ("Sorry?", "¿perdón?")],
    [
        ("Cambiar una palabra", "En «I'm fine, thank you», cambia fine por una palabra que significa contento. ¿Cómo queda?", ["Busco contento en inglés.", "Es happy.", "La estructura es igual."], "I'm happy, thank you."),
        ("Seguir si no entiendo", "Tu compañero dice algo que no entiendes. ¿Qué puedes decir?", ["Uso una frase de ayuda.", "Digo Sorry?", "Espero que repita."], "Sorry? o Again, please"),
    ],
    [
        ("Repetir el diálogo de memoria sin escuchar al otro.", "Se cree que hay que decirlo igual.", "Escucha y adapta tu respuesta."),
        ("Bloquearse si la conversación cambia.", "Se tiene miedo a equivocarse.", "Usa Sorry? o Again, please y sigue."),
    ],
    [
        ("¿Qué significa «How are you?»", "¿Cómo estás?", "Es un saludo muy frecuente."),
        ("¿Qué significa «And you?»", "¿Y tú?", "Se usa para devolver la pregunta."),
        ("¿Qué significa «tired»?", "Cansado", "Es un estado."),
    ],
    [
        ("¿Qué significa ser flexible en un diálogo?", "Adaptarme y cambiar palabras si hace falta", "No tengo que repetir el modelo exacto."),
        ("¿Qué haces si no entiendes lo que dice el otro?", "Digo Sorry? o Again, please", "Pido que repita."),
        ("¿Qué se mantiene cuando cambias palabras de un diálogo?", "La estructura", "Solo cambian las palabras."),
    ],
    [
        ("A: «How are you?» B: «I'm ___, thank you.» Completa con una palabra que signifique cansado.", "tired", "Tired significa cansado."),
        ("A: «I'm fine. And ___?» Completa.", "you", "And you es y tú."),
        ("Cambia fine por happy: «I'm ___, thank you.»", "happy", "Happy es contento."),
    ],
    [
        ("Pedro responde «I'm fine» a «What's your name?». ¿Por qué no encaja?", "Porque la pregunta es por el nombre, no por cómo estás", "Hay que responder a lo que preguntan."),
        ("Ana no entiende y se queda callada. ¿Qué mejora le sugieres?", "Decir Sorry? o Again, please", "Pedir ayuda mantiene el diálogo."),
    ],
    [
        ("Ordena el diálogo: (1) «I'm fine, thank you. And you?» (2) «Hello! How are you?» (3) «I'm happy.»", "2, 1, 3", "Saludo, respuesta con pregunta y respuesta final."),
        ("Responde a «How are you?» si estás cansado y quieres devolver la pregunta, con cuatro palabras en inglés: I'm ___, and you?", "I'm tired, and you?", "Tired es cansado."),
    ],
    [("Un compañero te dice «Hello! How are you?» pero tú estás contento. ¿Qué respondes en inglés?", "I'm happy, thank you. And you?", "Respondes y devuelves la pregunta.")],
    [
        ("¿Cómo se dice «¿y tú?» en inglés?", "And you?", "Se usa al terminar tu respuesta."),
        ("¿Qué significa «I'm fine»?", "Estoy bien", "Fine es bien."),
        ("¿Qué haces si cambia la conversación?", "Escucho y adapto mi respuesta", "Es ser flexible."),
    ],
    task("Con un adulto, haz dos veces el diálogo: A «Hello! How are you?» B «I'm fine, thank you. And you?» A «I'm happy.» La primera vez, tal cual. La segunda, cambia fine por tired y happy por fine. El adulto dirá una vez algo que no entiendas bien; usa «Sorry?» o «Again, please».", "«Hello! How are you?» «I'm tired, thank you. And you?» «I'm fine.»", ["hace los dos turnos", "cambia las palabras", "usa Sorry? o Again, please", "mantiene la estructura"], ["nota del adulto"], ["decir lo mismo sin escuchar", "quedarse en silencio"], "Valora que se haya adaptado y repite la frase de ayuda con él."),
    "Pregunta a alguien «How are you?» y responde con una palabra distinta.",
    "Inventa un diálogo de tres líneas con how are you, tired y happy.",
)
