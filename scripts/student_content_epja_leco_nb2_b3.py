"""Lenguaje y Comunicación EPJA Nivel 2 básico, módulo 2 (parte 3): OAD-07, escribir un párrafo para las redes sociales con hechos y opiniones. Publicaciones y borradores originales con datos inventados; sin redes ni marcas reales. Todo se escribe en papel."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-07"

F1 = ("Publicación de ejemplo para el grupo de un barrio (datos inventados): «El sábado se limpió la plaza con la ayuda de 25 vecinos. "
      "Para mí fue la mejor jornada del año, porque la plaza quedó lista para el fin de semana. Los invito a repetirlo el próximo mes.»")
F2 = ("Pares de palabras de ejemplo. Sinónimos: aumentar e incrementar; importante y relevante; comenzar e iniciar. "
      "Antónimos: aumentar y disminuir; ventaja y desventaja; antiguo y moderno; público y privado.")
F3 = ("Plan de ejemplo. Tema: nuevo horario de la feria. Hecho: la feria abre a las 8:00; antes abría a las 9:00. "
      "Opinión: me parece mejor porque hay menos calor. Cierre: invito a probar el nuevo horario este sábado.")
F4 = ("Palabras de ejemplo: café, camión, papel, árbol, lápiz, teléfono, música, joven, casa, también, campo, invitar, envase.")
F5 = ("Tres temas con sus datos (de ejemplo). Tema A, la plaza: el sábado se plantaron 15 árboles y participaron 30 personas. "
      "Tema B, la feria: ahora abre a las 8:00; antes abría a las 9:00. Tema C, la biblioteca: tiene 5 computadores nuevos y hay lista de espera.")
F6 = ("Borrador de ejemplo: «El sabado se inauguro la biblioteca con 5 computadores nuevos Me parece que es un avance importante porque muchos vecinos quieren usarlos por eso invito a todos a pasar»")

build(
    O, 1, F1,
    use="Hoy descubro qué es un párrafo para redes sociales: tiene un propósito, un público y mezcla un hecho con una opinión.",
    prior=["Sé distinguir un hecho de una opinión.", "He leído publicaciones en grupos o muros.", "Sé que una oración empieza con mayúscula y termina en punto."],
    explain=[
        "Escribir para las redes sociales es escribir para un público real, como un grupo del barrio. Antes de escribir, piensa para qué lo haces: informar un hecho, dar una opinión o invitar a participar. Con ese propósito claro, el texto sale más ordenado.",
        "Un párrafo es un grupo de oraciones que desarrollan una sola idea. Empieza con mayúscula y termina en punto aparte. Por ejemplo, en «El domingo se repartieron 40 platos de comida en la sede. Me pareció una actividad solidaria, porque llegó mucha gente. Los invito a sumarse la próxima vez», el hecho es la entrega de platos; la opinión es que fue solidaria; y el cierre invita a sumarse.",
        "Mezclar hecho y opinión es una buena forma de escribir: el hecho informa y la opinión muestra tu punto de vista. Lo importante es que se note cuál es cuál. Cuida el tono: respetuoso y claro, porque cualquiera puede leerlo.",
    ],
    vocab=[("propósito", "para qué escribes: informar, opinar o invitar"), ("párrafo", "grupo de oraciones sobre una idea"), ("tono", "manera de decir las cosas: amable, formal, serio"), ("destinatario", "persona o grupo que lee lo que escribes")],
    worked=[
        ("Reconocer el propósito", "Publicación de ejemplo: «El domingo se repartieron 40 platos de comida en la sede. Me pareció una actividad solidaria, porque llegó mucha gente. Los invito a sumarse la próxima vez».", ["La publicación cuenta que se repartieron platos.", "También da una opinión y termina con una invitación.", "Los tres propósitos se combinan: informar, opinar e invitar."], "Informa, opina e invita."),
        ("Separar hecho y opinión", "La misma publicación de los platos.", ["Hecho: «se repartieron 40 platos de comida en la sede».", "Opinión: «Me pareció una actividad solidaria».", "La opinión tiene una razón: «porque llegó mucha gente»."], "El hecho es el reparto de 40 platos y la opinión es que fue una actividad solidaria."),
    ],
    mistakes=[
        ("Escribir una opinión sin ningún hecho.", "El lector no sabe a qué se refiere.", "Cuenta primero el hecho y luego da tu opinión."),
        ("Escribir sin pensar en quién leerá.", "El tono puede resultar brusco o confuso.", "Imagina al grupo que lee y elige un tono respetuoso."),
    ],
    T=[
        ("abc", "{F} ¿Qué se hizo el sábado?", "Se limpió la plaza", "Se pintó la sede", "Se hizo una feria", "La primera oración cuenta que se limpió la plaza."),
        ("=", "{F} Si además de los 25 vecinos llegan 5 más al sábado siguiente, ¿cuántos participarían en total?", "25+5", "25 más 5 son 30 vecinos.", "vecinos"),
        ("ab", "{F} «Se limpió la plaza con la ayuda de 25 vecinos», ¿es hecho u opinión?", "Hecho", "Opinión", "La cifra y la acción se pueden comprobar."),
        ("ab", "{F} «Fue la mejor jornada del año», ¿es hecho u opinión?", "Opinión", "Hecho", "«La mejor» es un juicio personal."),
        ("abc", "{F} ¿Cuál es el propósito de la última oración?", "Invitar a repetirlo", "Informar una cifra", "Dar una razón", "«Los invito a repetirlo» es una invitación."),
        ("abc", "{F} ¿Qué razón da la publicación de su opinión?", "Que la plaza quedó lista para el fin de semana", "Que había 25 vecinos", "Que el mes es largo", "La razón de la opinión es lo que sigue a «porque» en la publicación."),
        ("ab", "{F} ¿Quién es el destinatario más probable de esta publicación?", "Los vecinos del grupo del barrio", "Un tribunal", "Es una publicación para un grupo del barrio."),
        ("En Lenguaje EPJA: ¿con qué signo termina un párrafo antes de pasar a otro párrafo? (una palabra)", "punto", "Un párrafo se cierra con punto aparte."),
        ("abc", "{F} ¿Qué tono usa la publicación?", "Amable y claro", "Burlón", "Enojado", "Usa palabras como «invito» y no ataca a nadie."),
        ("ab", "Una persona escribe solo «Qué lata todo». ¿Qué le falta?", "Un hecho que explique a qué se refiere", "Más signos de exclamación", "Sin hecho, el lector no entiende de qué habla."),
        ("abc", "¿Cuál es un propósito válido para escribir en un grupo de vecinos?", "Invitar a una reunión", "Burlarse de alguien", "Publicar datos privados de otra persona", "Invitar informa y reúne sin dañar a nadie."),
        ("ab", "Una persona va a escribir sobre una feria. ¿Qué paso conviene antes de escribir?", "Pensar el propósito y el público", "Escribir lo primero que se le ocurra sin pensar", "Con propósito y público claros, el texto sale ordenado."),
        ("abc", "Frase de ejemplo: «Creo que la feria debería abrir más temprano, porque hay menos calor». ¿Cuál es la razón?", "porque hay menos calor", "Creo que", "la feria", "La razón está después de «porque»."),
    ],
    ctx=("abc", "Una persona quiere avisar en el grupo de su barrio que el taller de costura cambió de día y que le gustó mucho la primera clase. ¿Cuál es la mejor forma de ordenar su párrafo?", "Primero el cambio de día, luego su opinión con una razón y al final una invitación", "Solo su opinión, sin decir el día", "Solo una invitación sin decir qué taller", "Hecho, opinión con razón y cierre hacen un párrafo claro."),
    sc=[("En Lenguaje EPJA: ¿qué es un párrafo?", "Un grupo de oraciones sobre una sola idea", "Desarrolla una idea con varias oraciones."),
        ("¿Qué propósitos puede tener una publicación?", "Informar, opinar o invitar", "Son las tres funciones más comunes."),
        ("¿Por qué conviene mezclar un hecho con una opinión?", "El hecho informa y la opinión da mi punto de vista", "Juntos hacen el texto claro y personal.")],
    op=("Escribe un párrafo de tres o cuatro oraciones para el grupo de tu barrio sobre este tema de ejemplo: «El sábado hubo una feria de libros usados en la sede, con 40 libros disponibles». Debe incluir un hecho, una opinión con razón y una invitación. Marca con un color cada parte.",
        "El sábado hubo una feria de libros usados en la sede, con 40 libros disponibles. Me pareció una excelente idea porque permite leer sin gastar mucho. Los invito a traer un libro para intercambiar la próxima vez.",
        ["incluye un hecho comprobable", "incluye una opinión con razón", "cierra con una invitación", "usa mayúsculas y puntos"],
        ["un párrafo de tres o cuatro oraciones con las partes marcadas"],
        ["no dar un hecho", "escribir una opinión sin razón"],
        "Pregunta: «¿Se nota cuál oración es el hecho y cuál la opinión?»."),
    reinforce="Escribe dos oraciones sobre un lugar que conozcas: una con un hecho y otra con una opinión.",
    extend="Escribe dos párrafos breves sobre el mismo tema con distinto propósito: uno para informar y otro para invitar.",
)

build(
    O, 2, F2,
    use="Hoy amplío mi vocabulario con palabras de la actualidad y de la vida social, y uso sinónimos y antónimos para escribir con precisión.",
    prior=["Escribo oraciones con hecho y opinión.", "Conozco palabras de uso diario.", "Sé que una misma idea se puede decir de varias maneras."],
    explain=[
        "Escribir con un vocabulario variado y preciso ayuda a que te entiendan mejor y a no repetir siempre la misma palabra. Un sinónimo es una palabra con significado parecido a otra, como «aumentar» e «incrementar». Un antónimo es una palabra con significado opuesto, como «aumentar» y «disminuir».",
        "Cada ámbito tiene sus propias palabras. En lo social: «comunidad» es un grupo de personas que comparte un lugar o un fin; «convivencia» es vivir juntos con respeto; «participación» es tomar parte en algo con otros. En ciencia: «hipótesis» es una explicación posible que hay que comprobar, y «evidencia» es el dato que la respalda.",
        "En historia: «patrimonio» es lo que una comunidad quiere conservar, y «testimonio» es el relato de alguien que vivió algo. En la actualidad: «campaña» es un conjunto de acciones para lograr un fin, y «tendencia» es la dirección en que algo cambia. Úsalas solo cuando las entiendas bien.",
    ],
    vocab=[("sinónimo", "palabra de significado parecido a otra"), ("antónimo", "palabra de significado opuesto a otra"), ("evidencia", "dato o prueba que respalda una idea"), ("comunidad", "grupo de personas que comparte un lugar o un fin")],
    worked=[
        ("Elegir un sinónimo", "«La respuesta de los vecinos fue rápida».", ["Busco una palabra parecida a «rápida».", "«Veloz» significa casi lo mismo.", "La oración queda: «La respuesta de los vecinos fue veloz»."], "Veloz es sinónimo de rápida."),
        ("Elegir un antónimo", "«La biblioteca abre a las 9:00».", ["Busco el opuesto de «abre».", "El opuesto es «cierra».", "La oración nueva: «La biblioteca cierra a las 18:00»."], "El antónimo de abrir es cerrar."),
    ],
    mistakes=[
        ("Cambiar una palabra por otra que parece sinónimo pero tiene otro sentido.", "Cambia lo que quieres decir.", "Comprueba que la oración mantenga el mismo significado."),
        ("Usar una palabra difícil sin saber qué significa.", "El mensaje puede quedar equivocado.", "Úsala solo si puedes explicarla con tus palabras."),
    ],
    T=[
        ("abc", "{F} ¿Cuál es un sinónimo de «aumentar»?", "Incrementar", "Disminuir", "Parar", "Incrementar significa hacer algo mayor, igual que aumentar, por eso son sinónimos."),
        ("ab", "{F} ¿Cuál es el antónimo de «aumentar»?", "Disminuir", "Incrementar", "Disminuir es hacer algo menor, lo opuesto de aumentar."),
        ("abc", "{F} ¿Cuál es el antónimo de «público» según la ficha?", "privado", "relevante", "moderno", "Los pares de antónimos incluyen público y privado."),
        ("abc", "{F} ¿Qué palabra es sinónimo de «comenzar»?", "iniciar", "terminar", "cerrar", "Iniciar y comenzar significan lo mismo."),
        ("ab", "{F} ¿Qué es la «evidencia» en ciencia?", "El dato que respalda una idea", "Una opinión sin prueba", "La evidencia es una prueba que apoya una explicación."),
        ("abc", "¿Qué es una «hipótesis»?", "Una explicación posible que se debe comprobar", "Un hecho ya comprobado", "Una opinión de gusto", "Por eso se pone a prueba con datos."),
        ("ab", "¿Qué significa «convivencia»?", "Vivir juntos con respeto", "Vivir solo", "Es la base del buen trato entre personas."),
        ("abc", "¿Qué es el «patrimonio» de una comunidad?", "Lo que quiere conservar, como sus tradiciones y lugares", "Un tipo de impuesto", "Un partido de fútbol", "Incluye bienes y tradiciones valiosos para la comunidad."),
        ("ab", "¿Qué es un «testimonio» en historia?", "El relato de alguien que vivió un hecho", "Un mapa", "Es una fuente de quien lo presenció."),
        ("abc", "Oración de ejemplo: «El número de socios disminuyó este año». ¿Qué palabra sirve como antónimo de «disminuyó»?", "aumentó", "bajó", "se redujo", "Bajó y se redujo son sinónimos; aumentó es el opuesto."),
        ("ab", "Oración de ejemplo: «La reunión es importante». ¿Qué sinónimo puede reemplazar «importante»?", "relevante", "inútil", "Relevante conserva el sentido de importante y no cambia el mensaje de la oración."),
        ("abc", "¿Qué es una «campaña» en la actualidad?", "Un conjunto de acciones para lograr un fin", "Un tipo de planta", "Una calle", "Por ejemplo, una campaña de reciclaje reúne acciones organizadas."),
        ("ab", "Oración de ejemplo: «La tendencia es que cada año hay más usuarios». ¿Qué indica «tendencia»?", "Hacia dónde cambia algo con el tiempo", "Un hecho puntual", "Una tendencia describe una dirección de cambio."),
    ],
    ctx=("abc", "Una persona escribe en un grupo del barrio: «La participación aumentó, y esto es una ventaja». Para no repetir palabras, elige reemplazar «aumentó». ¿Qué opción mantiene el sentido?", "La participación se incrementó", "La participación disminuyó", "La participación terminó", "Incrementó mantiene el significado de aumento."),
    sc=[("En Lenguaje EPJA: ¿qué es un sinónimo?", "Una palabra de significado parecido", "Permite variar sin cambiar el sentido."),
        ("En Lenguaje EPJA: ¿qué es un antónimo?", "Una palabra de significado opuesto", "Expresa lo contrario de otra palabra."),
        ("¿Cuándo uso una palabra nueva?", "Cuando entiendo su significado", "Si entiendo la palabra y su significado, no cambio sin querer el mensaje.")],
    op=("Escribe tres oraciones sobre un tema de actualidad de tu comunidad, por ejemplo el reciclaje o el uso de la plaza. En cada una usa una de estas palabras: comunidad, participación o campaña. Después reescribe una oración cambiando una palabra por un sinónimo y otra oración cambiando una palabra por un antónimo.",
        "La comunidad organizó una campaña de reciclaje. La participación aumentó en el último mes. Esta campaña es una ventaja para el barrio. Con sinónimo: La participación se incrementó. Con antónimo: La participación disminuyó.",
        ["usa las tres palabras", "reescribe una oración con un sinónimo", "reescribe una oración con un antónimo"],
        ["cinco oraciones escritas"],
        ["usar una palabra que no entiende", "cambiar el sentido con el sinónimo"],
        "Pregunta: «¿Mi oración con sinónimo dice lo mismo que la original?»."),
    reinforce="Anota cinco pares de sinónimos y cinco de antónimos.",
    extend="Escribe un párrafo de cuatro oraciones sobre tu barrio sin repetir ninguna palabra importante.",
)

build(
    O, 3, F3,
    use="Hoy escribo un párrafo siguiendo el proceso de escritura: planifico, escribo un borrador, reviso y dejo la versión final.",
    prior=["Sé qué es un párrafo.", "Distingo hecho y opinión.", "Conozco sinónimos y antónimos."],
    explain=[
        "Escribir bien no es escribir de una vez. El proceso de escritura tiene cuatro pasos: planificar, escribir un borrador, revisar y reescribir. Planificar es decidir el propósito, el hecho que contarás y la opinión que darás. El borrador es la primera versión, que puede mejorar.",
        "Un buen párrafo para redes sigue este orden: primero el hecho, luego la opinión con su razón y al final un cierre. Los conectores unen las ideas: «porque» da una razón, «por eso» muestra una consecuencia, «sin embargo» marca un contraste y «además» suma otra idea.",
        "Por ejemplo, con el plan «hecho: la feria se instala ahora en la calle Los Pinos; opinión: me parece mejor porque hay más espacio; cierre: invito a conocerla», el párrafo sale ordenado: «La feria se instala ahora en la calle Los Pinos. Me parece mejor porque hay más espacio. Por eso, los invito a conocerla».",
    ],
    vocab=[("planificar", "decidir qué se escribirá antes de empezar"), ("borrador", "primera versión de un texto, que se puede mejorar"), ("conector", "palabra que une ideas, como porque o por eso"), ("cierre", "última parte del párrafo, que invita o concluye")],
    worked=[
        ("Del plan al párrafo", "Plan de ejemplo: hecho, la reunión pasó del lunes al jueves; opinión, me parece mejor porque más personas pueden asistir; cierre, invito a anotar la fecha.", ["Pongo el hecho primero: «La reunión pasó del lunes al jueves».", "Sigo con la opinión y su razón: «Me parece mejor porque más personas pueden asistir».", "Cierro con la invitación: «Por eso, los invito a anotar la fecha»."], "La reunión pasó del lunes al jueves. Me parece mejor porque más personas pueden asistir. Por eso, los invito a anotar la fecha."),
        ("Elegir el conector", "Idea 1: hay más espacio. Idea 2: me parece mejor el nuevo lugar.", ["Quiero dar una razón de mi opinión.", "El conector que da razón es «porque».", "Escribo: «Me parece mejor el nuevo lugar porque hay más espacio»."], "Se usa «porque» para dar la razón."),
    ],
    mistakes=[
        ("Escribir la versión final sin revisar.", "Se quedan errores de ortografía y de claridad.", "Relee el borrador y corrige antes de publicar."),
        ("Poner muchos conectores iguales.", "Se repite y cansa al lector.", "Varía: porque, por eso, además, sin embargo."),
    ],
    T=[
        ("abc", "{F} ¿Cuál es el hecho del plan?", "La feria abre a las 8:00; antes abría a las 9:00", "Me parece mejor porque hay menos calor", "Invito a probar el nuevo horario", "El hecho es el cambio de horario."),
        ("=", "{F} ¿Cuánto más temprano abre la feria ahora? (la diferencia entre las 9:00 y las 8:00)", "9-8", "De 8 a 9 hay una hora, porque 9 menos 8 es 1.", "hora"),
        ("ab", "{F} ¿Cuál es la opinión del plan?", "Me parece mejor porque hay menos calor", "La feria abre a las 8:00", "La opinión se marca con «me parece» y da una razón después de «porque»."),
        ("abc", "{F} ¿Cuál es la razón de la opinión?", "Que hay menos calor", "Que antes abría a las 9:00", "Que es sábado", "La razón está después de «porque»."),
        ("ab", "{F} ¿Cuál es el cierre?", "Invito a probar el nuevo horario este sábado", "La feria abre a las 8:00", "El cierre es la invitación final."),
        ("abc", "¿Cuál es el primer paso del proceso de escritura?", "Planificar", "Publicar", "Revisar", "Antes de escribir se decide qué decir."),
        ("ab", "¿Qué conector da una razón?", "porque", "pero", "«Porque» introduce la causa de algo."),
        ("abc", "¿Qué conector muestra una consecuencia?", "por eso", "porque", "además", "«Por eso» presenta el resultado de lo anterior."),
        ("ab", "En un párrafo de redes, ¿qué conector marca un contraste con la idea anterior?", "sin embargo", "además", "«Sin embargo» introduce una idea opuesta a la anterior."),
        ("abc", "Oración de ejemplo: «El bus pasa cada 15 minutos; ___, siempre llega lleno». ¿Qué conector va en el espacio?", "sin embargo", "porque", "además de", "El hecho de pasar seguido contrasta con que llegue lleno."),
        ("ab", "Después de escribir el borrador, ¿qué conviene hacer?", "Releerlo y corregirlo", "Publicarlo de inmediato", "La revisión mejora la claridad y la ortografía."),
        ("abc", "¿Qué orden tiene un buen párrafo de este tipo?", "Hecho, opinión con razón y cierre", "Cierre, razón y hecho", "Solo opinión", "Ese orden permite entender primero qué pasó y luego qué se opina."),
        ("ab", "Oración de ejemplo: «La plaza quedó limpia; ___, se plantaron árboles nuevos». ¿Qué conector sirve para sumar otra idea?", "además", "sin embargo", "«Además» agrega otra idea a la anterior."),
    ],
    ctx=("abc", "Una persona quiere escribir en un grupo sobre el nuevo día de recolección de basura (hecho: ahora es martes) y sobre su opinión (le parece cómodo, porque coincide con otra tarea). ¿Cuál es la mejor oración final con conector?", "Me parece cómodo porque coincide con otra tarea", "Es cómodo y no sé por qué", "Todos saben que es cómodo", "Da una razón concreta y clara."),
    sc=[("¿Cuáles son los pasos del proceso de escritura?", "Planificar, escribir un borrador, revisar y reescribir", "Cada paso del proceso mejora el texto: se planifica, se escribe, se revisa y se reescribe."),
        ("En Lenguaje EPJA: ¿qué es un conector?", "Una palabra que une ideas", "Muestra razón, consecuencia, contraste o suma."),
        ("¿Qué va primero en el párrafo?", "El hecho", "Primero se cuenta el hecho, porque da el contexto para entender la opinión.")],
    op=("Usa este plan de ejemplo para escribir tu párrafo: Hecho: la biblioteca prestó 300 libros este mes. Opinión: me parece un buen resultado porque hay más personas que leen. Cierre: invitar a pasar por la biblioteca. Escribe un borrador, revísalo con esta lista (hecho claro, opinión con razón, un conector, cierre) y escribe la versión final.",
        "Borrador: La biblioteca prestó 300 libros este mes. Me parece un buen resultado porque hay más personas que leen. Por eso, los invito a pasar por la biblioteca. Revisión: hay hecho, opinión con razón, conector y cierre.",
        ["escribe un borrador", "revisa con la lista", "escribe la versión final", "usa al menos un conector"],
        ["borrador, revisión y versión final"],
        ["no revisar", "no usar conectores"],
        "Pregunta: «¿Cada parte del plan aparece en mi párrafo?»."),
    reinforce="Haz un plan de cuatro líneas (propósito, hecho, opinión, cierre) sobre un tema de tu barrio.",
    extend="Reescribe tu párrafo cambiando el orden y cuenta cómo cambia su efecto.",
)

build(
    O, 4, F4,
    use="Hoy repaso la ortografía que más importa al publicar: puntuación, tildes y letras que se confunden.",
    prior=["Sé escribir párrafos con hecho y opinión.", "Sé separar palabras en sílabas.", "Reconozco una tilde."],
    explain=[
        "La ortografía tiene tres partes. La puntual usa mayúsculas, punto, coma y signos de interrogación y exclamación: se abren y se cierran. La acentual decide dónde va la tilde. La literal elige la letra correcta dentro de la palabra.",
        "Para las tildes, mira qué sílaba se pronuncia más fuerte. Si es la última (agudas), lleva tilde si termina en n, s o vocal: «café», «camión». Si es la penúltima (graves), lleva tilde si NO termina en n, s ni vocal: «árbol», «lápiz». Si es la antepenúltima (esdrújulas), siempre lleva tilde: «teléfono», «música».",
        "En la ortografía de las letras, recuerda dos reglas seguras: antes de b y de p se escribe m («también», «campo»), y antes de v se escribe n («invitar», «envase»). Revisar estas cosas antes de publicar muestra respeto por quien lee.",
    ],
    vocab=[("tilde", "rayita que se pone sobre una vocal, como en café"), ("palabra aguda", "la que se pronuncia más fuerte en la última sílaba"), ("palabra grave", "la que se pronuncia más fuerte en la penúltima sílaba"), ("palabra esdrújula", "la que se pronuncia más fuerte en la antepenúltima sílaba")],
    worked=[
        ("Poner la tilde", "«camion»: ca-MION.", ["La sílaba más fuerte es la última: es aguda.", "Termina en n: las agudas que terminan en n llevan tilde.", "Escribo «camión»."], "camión"),
        ("Elegir m o n", "«e_vase» y «ca_bio».", ["Antes de v va n: «envase».", "Antes de b va m: «cambio».", "Aplico las dos reglas."], "envase y cambio"),
    ],
    mistakes=[
        ("Poner tilde a «papel», pensando que toda palabra aguda la lleva.", "«Papel» termina en l y las agudas solo llevan tilde si terminan en n, s o vocal.", "Mira cómo termina la palabra antes de poner tilde."),
        ("Escribir «tanbién» con n.", "Antes de b se escribe m.", "Recuerda la regla: mb, mp y nv."),
    ],
    T=[
        ("abc", "{F} ¿Dónde está la sílaba más fuerte de «café»?", "En la última: ca-FÉ", "En la primera", "En la del medio", "Se dice ca-FÉ, con fuerza al final."),
        ("ab", "{F} «Café» es...", "aguda", "grave", "Su fuerza está en la última sílaba."),
        ("ab", "{F} ¿«Papel» lleva tilde?", "No, es aguda y termina en l", "Sí, porque es aguda", "Las agudas solo llevan tilde si terminan en n, s o vocal."),
        ("abc", "{F} ¿Por qué «árbol» lleva tilde?", "Es grave y no termina en n, s ni vocal", "Es aguda y termina en l", "Es esdrújula", "Se pronuncia ÁR-bol, con fuerza en la penúltima sílaba, y termina en l."),
        ("ab", "{F} ¿«Casa» lleva tilde?", "No, es grave y termina en vocal", "Sí, es grave", "Las graves que terminan en vocal no llevan tilde."),
        ("abc", "{F} ¿Por qué «teléfono» lleva tilde?", "Es esdrújula", "Es aguda", "Es grave", "Su fuerza está en la antepenúltima sílaba."),
        ("ab", "{F} ¿«Joven» lleva tilde?", "No, es grave y termina en n", "Sí, porque termina en n", "Las graves que terminan en n no llevan tilde."),
        ("abc", "{F} ¿Cómo se escribe correctamente?", "también", "tanbién", "tambien", "Antes de b va m y además la palabra es aguda terminada en n."),
        ("ab", "{F} ¿Cuál es correcta?", "invitar", "imvitar", "Antes de v se escribe n."),
        ("abc", "¿Qué signo de puntuación se abre y se cierra en una pregunta?", "¿ ?", "? solo", "¡ ?", "En español la pregunta se abre con ¿ y se cierra con ?."),
        ("ab", "¿Cuál oración está bien escrita?", "Compré pan, queso y tomates.", "compré pan queso y tomates", "Lleva mayúscula inicial, comas en la enumeración y punto final."),
        ("abc", "¿Qué letra va antes de una p en «ca_po»?", "m", "n", "b", "Antes de p y de b se escribe m."),
        ("ab", "¿«Lápiz» lleva tilde?", "Sí, es grave y termina en z", "No, es aguda", "Las graves que no terminan en n, s ni vocal llevan tilde."),
    ],
    ctx=("abc", "Una persona va a publicar: «¿Podemos juntarnos el sabado en la plaza». Revisa la ortografía. ¿Qué cambios necesita?", "Tilde en sábado y el signo de cierre ?", "Quitar la mayúscula", "Cambiar «plaza» por «plasa»", "«Sábado» es esdrújula y la pregunta debe cerrarse con ?."),
    sc=[("¿Qué lleva siempre tilde?", "Las palabras esdrújulas", "Su fuerza está en la antepenúltima sílaba."),
        ("¿Qué letra va antes de b y de p?", "m", "Es una regla segura de la ortografía literal."),
        ("¿Qué letra va antes de v?", "n", "Antes de v se escribe siempre n, como en «invitar» y «envase».")],
    op=("Corrige este texto de ejemplo con las reglas de la clase y reescríbelo: «tambien el sabado hubo musica en el campo. invito a todos». Anota los cambios que hiciste.",
        "También el sábado hubo música en el campo. Invito a todos. Cambios: mayúsculas iniciales; tilde en también, sábado y música; puntos.",
        ["pone las tildes", "usa mayúsculas y puntos", "anota los cambios"],
        ["el texto corregido y una lista de cambios"],
        ["olvidar una tilde", "olvidar los puntos"],
        "Pregunta: «¿Revisé tilde, puntuación y letra en cada palabra?»."),
    reinforce="Escribe diez palabras con tilde y di si son agudas, graves o esdrújulas.",
    extend="Escribe un párrafo de cuatro oraciones sin errores de puntuación, tildes ni m y n antes de b, p o v.",
)

build(
    O, 5, F5,
    use="Hoy escribo una publicación para mi comunidad con hechos y opiniones, cuidando respeto y privacidad.",
    prior=["Sé planificar y escribir un párrafo.", "Cuido ortografía y conectores.", "Distingo hecho y opinión."],
    explain=[
        "Una publicación comunitaria llega a personas que no siempre conoces. Por eso, cuida tres cosas. Primero, que el hecho sea correcto y comprobable. Segundo, que la opinión tenga una razón y respete a quien piensa distinto. Tercero, que no incluyas datos privados de otras personas, como teléfonos o direcciones.",
        "Escribir con respeto no significa callar tu opinión. Significa decirla sin insultar ni humillar y con razones. «Me parece mal que la luz esté apagada, porque hay que caminar a oscuras» es una opinión clara y respetuosa. «Los responsables son unos flojos» ataca y no ayuda.",
        "En la ficha hay tres temas con datos de ejemplo. Elige uno y arma tu párrafo: hecho, opinión con razón y un cierre que invite a participar. No necesitas una red real: escríbelo en tu cuaderno.",
    ],
    vocab=[("respeto", "tratar a otras personas con consideración, aunque piensen distinto"), ("privacidad", "los datos personales que no se comparten sin permiso"), ("insultar", "decir palabras que ofenden a alguien"), ("comunitario", "de la comunidad o pensado para ella")],
    worked=[
        ("Armar una publicación", "Tema D (de ejemplo), el comedor: ayer se sirvieron 80 almuerzos y colaboraron 12 personas.", ["Hecho: «Ayer se sirvieron 80 almuerzos con la ayuda de 12 personas».", "Opinión con razón: «Me parece un gran esfuerzo, porque requiere mucho trabajo».", "Cierre: «Los invito a colaborar la próxima semana»."], "Ayer se sirvieron 80 almuerzos con la ayuda de 12 personas. Me parece un gran esfuerzo, porque requiere mucho trabajo. Los invito a colaborar la próxima semana."),
        ("Cuidar la privacidad", "Borrador: «Llamen a Ana al número 0000 0000 para inscribirse».", ["El borrador publica un teléfono de una persona.", "Sin su permiso, eso es un dato privado.", "Lo mejor es decir «inscríbanse con la tesorera»."], "No se publican teléfonos personales sin permiso."),
    ],
    mistakes=[
        ("Publicar la opinión con insultos.", "Hiere a otras personas y no aporta razones.", "Di tu opinión con una razón, sin atacar."),
        ("Compartir datos privados de otra persona.", "Puede perjudicarla.", "Pide permiso o no los pongas."),
    ],
    T=[
        ("abc", "{F} ¿Cuántos árboles se plantaron en el tema A?", "15", "30", "5", "El tema A dice 15 árboles y 30 personas."),
        ("=", "{F} Si las 30 personas del tema A se juntan en parejas y cada pareja planta un árbol, ¿cuántos árboles se plantan?", "30/2", "Si cada pareja planta un árbol, 30 personas forman 15 parejas y se plantan 15 árboles.", "árboles"),
        ("ab", "{F} En el tema B, ¿a qué hora abre ahora la feria?", "8:00", "9:00", "Ahora abre a las 8:00; antes abría a las 9:00."),
        ("abc", "{F} En el tema C, ¿cuántos computadores nuevos hay?", "5", "15", "30", "El tema C dice que hay 5 computadores nuevos."),
        ("ab", "{F} «Hay lista de espera» (tema C), ¿es hecho u opinión?", "Hecho", "Opinión", "Se puede comprobar con la lista."),
        ("abc", "{F} ¿Cuál es una buena opinión con razón para el tema C?", "Me parece que faltan computadores, porque hay lista de espera", "Los de la biblioteca son unos flojos", "Todo está mal", "Da una razón concreta y respeta a las personas."),
        ("ab", "{F} ¿Qué opinión respeta a otras personas?", "Me parece que el nuevo horario ayuda, porque hay menos calor", "Quienes dijeron que no se podía son unos tontos", "La primera da razón y no ofende."),
        ("abc", "¿Qué dato NO se debe publicar sin permiso?", "El teléfono de una vecina", "La hora de la reunión", "El nombre de la calle de la plaza", "Un teléfono es un dato personal y no se publica sin permiso."),
        ("ab", "Una persona quiere subir una foto donde aparece otra vecina. ¿Qué conviene antes?", "Pedirle permiso", "Subirla igual", "Respetar la imagen y la privacidad de otras personas."),
        ("abc", "¿Cuál es una buena frase de cierre para una publicación vecinal?", "Los invito a participar el próximo sábado", "Ojalá se muera el proyecto", "No me importa quién venga", "Invita a participar sin ofender a nadie."),
        ("ab", "Antes de publicar un hecho, ¿qué conviene?", "Revisar que sea correcto", "Escribirlo rápido sin revisar", "Un dato equivocado confunde a la comunidad."),
        ("abc", "Frase de ejemplo: «Creo que la plaza necesita más luz, porque de noche da miedo caminar». ¿Qué tiene de bueno?", "Da una opinión con razón y sin ofender", "No tiene opinión", "Ataca a alguien", "Cumple con el respeto y con las razones que pide una buena opinión."),
        ("ab", "¿Cuál es un dato que sí se puede publicar sobre una reunión vecinal?", "Día, hora y lugar", "Dirección de la casa de una persona", "Día, hora y lugar son información de interés común, no datos privados."),
    ],
    ctx=("abc", "Alguien escribe: «Me parece mal que la sede cierre temprano, porque los talleres terminan tarde. Además, la tesorera es incapaz». ¿Qué conviene cambiar para que sea respetuosa?", "Quitar el ataque a la tesorera y dejar la opinión con su razón", "Quitar la razón", "Dejar todo igual", "La crítica a una persona no aporta; la opinión con razón sí."),
    sc=[("¿Qué debe tener una opinión respetuosa?", "Una razón y ningún insulto", "Con razones y sin insultos se puede debatir sin dañar a nadie."),
        ("¿Qué datos no publico sin permiso?", "Datos privados de otras personas", "Teléfonos, direcciones y fotos son privados."),
        ("¿Qué parte de la publicación invita a participar?", "El cierre", "El cierre es la última frase y es la que invita a participar.")],
    op=("Elige uno de los tres temas de la ficha y escribe una publicación de cuatro oraciones: un hecho, una opinión con razón y un cierre que invite. Después revisa con esta lista: ¿hecho correcto?, ¿opinión respetuosa?, ¿sin datos privados?, ¿ortografía revisada?",
        "El sábado se plantaron 15 árboles con 30 personas. Me parece un gran trabajo, porque ahora la plaza tendrá sombra. Por eso, los invito a regarlos entre todos. ¡Gracias por participar! Revisión: sin datos privados y con tildes revisadas.",
        ["incluye hecho, opinión con razón y cierre", "no incluye datos privados ni insultos", "revisa ortografía"],
        ["una publicación de cuatro oraciones y una lista de revisión"],
        ["publicar datos privados", "insultar"],
        "Pregunta: «¿Esta opinión podría ayudar a la comunidad?»."),
    reinforce="Reescribe una opinión fuerte con una razón y sin ofender.",
    extend="Escribe una publicación para invitar a una actividad con cuatro datos: día, hora, lugar y qué traer.",
)

build(
    O, 6, F6,
    use="Hoy reviso un borrador con una lista de control, lo corrijo y reviso mi proceso de escritura.",
    prior=["Sé planificar y escribir un párrafo.", "Cuido ortografía puntual, acentual y literal.", "Uso conectores y vocabulario preciso."],
    explain=[
        "Revisar es leer lo que escribiste como si fueras otra persona. Una lista de control ayuda: ¿el hecho está claro?, ¿la opinión tiene una razón?, ¿uso conectores?, ¿hay mayúsculas y puntos?, ¿las tildes están bien puestas?, ¿hay un dato privado o una frase que ofenda?",
        "En un borrador pueden faltar puntos, mayúsculas y tildes. Por ejemplo, «repartio» necesita tilde porque es aguda terminada en vocal: «repartió». Y cuando dos ideas quedan pegadas, se separan con un punto y la oración siguiente parte con mayúscula.",
        "Al terminar, compara la primera versión con la última y anota qué mejoró. Esa mirada te ayuda a ver cómo avanzas. Reescribir no es un castigo: es lo que hacen las personas que escriben con cuidado.",
    ],
    vocab=[("revisar", "leer con atención para encontrar y corregir errores"), ("lista de control", "lista de preguntas para comprobar que nada falta"), ("reescribir", "volver a escribir un texto con las correcciones"), ("versión final", "texto ya corregido, listo para compartir")],
    worked=[
        ("Corregir las tildes", "Borrador de ejemplo: «El lunes se repartio pan en la plaza Me pareció una linda actividad porque participaron muchos vecinos por eso invito a la próxima».", ["«Repartio» es aguda y termina en vocal: «repartió».", "Los demás términos tienen tilde correcta o no la necesitan."], "repartió"),
        ("Corregir la puntuación", "El mismo borrador del pan.", ["Falta un punto después de «plaza» y mayúscula en «Me».", "Falta un punto después de «vecinos» y mayúscula en «Por eso».", "Falta el punto final."], "El lunes se repartió pan en la plaza. Me pareció una linda actividad porque participaron muchos vecinos. Por eso invito a la próxima."),
    ],
    mistakes=[
        ("Revisar solo la ortografía y olvidar el hecho.", "Un dato mal escrito confunde aunque esté bien escrito.", "Revisa también si el hecho es correcto."),
        ("Cambiar tanto el texto que se pierde la idea.", "La revisión corrige, no cambia lo que quieres decir.", "Cambia solo lo necesario."),
    ],
    T=[
        ("abc", "{F} ¿Cuántos computadores nuevos tiene la biblioteca según el borrador?", "5", "50", "15", "El borrador dice «5 computadores nuevos»."),
        ("ab", "{F} ¿Cómo se escribe «sabado» correctamente?", "sábado", "sabado", "Es esdrújula y siempre lleva tilde."),
        ("ab", "{F} ¿Cómo se escribe «inauguro» correctamente?", "inauguró", "inauguro", "Es aguda y termina en vocal."),
        ("abc", "{F} ¿Qué falta después de «computadores nuevos»?", "Un punto", "Una coma y nada más", "Una pregunta", "Ahí termina la primera oración; la siguiente empieza con mayúscula."),
        ("ab", "{F} ¿Con qué letra comienza «por eso» al empezar una oración?", "Mayúscula", "Minúscula", "Toda oración nueva inicia con mayúscula."),
        ("abc", "{F} ¿Cuál es la opinión del borrador?", "Es un avance importante", "Se inauguró la biblioteca", "Hay 5 computadores", "La opinión usa «me parece que»."),
        ("ab", "{F} ¿Qué conector usa para dar una razón?", "porque", "pero", "«Porque muchos vecinos quieren usarlos» da la razón."),
        ("abc", "{F} ¿Qué parte es el cierre del borrador?", "Por eso invito a todos a pasar", "El sábado se inauguró", "Computadores nuevos", "El cierre del borrador es la frase que invita a pasar por la biblioteca."),
        ("ab", "{F} ¿Qué falta al final del borrador?", "Un punto", "Un signo de pregunta", "Cada texto debe terminar con punto."),
        ("abc", "¿Qué pregunta de la lista de control revisa el hecho?", "¿El hecho está claro y es correcto?", "¿Tiene muchas palabras largas?", "¿Es muy corto?", "Se centra en el contenido del dato."),
        ("ab", "Una persona corrige su texto cambiando «tambien» por «también». ¿Qué revisó?", "La tilde", "El hecho", "Agregó la tilde de una aguda terminada en n."),
        ("abc", "¿Para qué sirve la versión final?", "Para compartir un texto ya corregido", "Para olvidar el borrador", "Para empezar de cero siempre", "Es el resultado de corregir el borrador."),
        ("ab", "Una persona dice: «El borrador no se toca, está perfecto». ¿Qué le falta?", "Revisarlo con atención", "Nada más", "Revisar ayuda a encontrar errores que no se ven al escribir."),
    ],
    ctx=("abc", "Una persona está por publicar en un grupo este borrador de ejemplo: «La feria cambio de dia, ahora es el domingo a las 9:00 Me gusta mas el horario porque no hay tanto calor». Al revisar con la lista de control, ¿qué debería corregir primero?", "Las tildes y el punto que falta, para que se entienda bien", "Borrar el hecho", "Cambiar el domingo por el sábado", "Una lista de control empieza por lo que más afecta a la lectura."),
    sc=[("En Lenguaje EPJA: ¿para qué sirve una lista de control al revisar un párrafo?", "Para comprobar que no falte nada", "La lista reúne las preguntas de revisión para no olvidar ningún punto del texto."),
        ("En Lenguaje EPJA: ¿qué significa reescribir?", "Volver a escribir con las correcciones", "Se reescribe después de revisar, incorporando las correcciones que se encontraron."),
        ("¿Qué comparo al final del proceso?", "La primera versión con la última", "Al comparar la primera y la última versión veo qué mejoró.")],
    op=("Escribe un borrador de cuatro oraciones sobre este hecho de ejemplo: «El jueves se entregaron 50 canastas de alimentos en la sede». Incluye una opinión con razón y un cierre. Luego revísalo con la lista de control, corrígelo y escribe una nota con tres cosas que mejoraste.",
        "Borrador: El jueves se entregaron 50 canastas de alimentos en la sede. Me parece una ayuda importante, porque muchas familias las necesitan. Por eso invito a colaborar en la próxima entrega. Mejoras: agregué los puntos, puse mayúscula después de cada punto y usé el conector «porque».",
        ["escribe un borrador completo", "revisa con la lista de control", "corrige y reescribe", "anota tres mejoras"],
        ["borrador, versión final y nota de mejoras"],
        ["no cambiar nada", "corregir sin anotar mejoras"],
        "Pregunta: «¿La versión final se entiende mejor que el borrador?»."),
    reinforce="Revisa un mensaje que hayas escrito antes con la lista de control y corrígelo.",
    extend="Escribe tu propia lista de control de cinco preguntas y úsala en otro texto.",
)
