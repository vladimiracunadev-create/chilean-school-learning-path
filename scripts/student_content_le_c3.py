"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 23 (expresión oral) y OA 24 (vocabulario nuevo en la oralidad)."""
from __future__ import annotations

from student_lessons import ex, register

OA23, OA24 = "LE01 OA 23", "LE01 OA 24"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 23
reg(
    OA23, 1,
    "Las listas de temas de este cuaderno, lápiz y hoja. Para practicar se necesita un adulto que escuche.",
    "Aprenderé a escoger un tema y a hacerlo pequeño para poder hablar de él con claridad. Sirve para contar algo sin perderme ni hablar de mil cosas a la vez.",
    ["Sé contar algo que me pasó.", "Sé hablar frente a una persona."],
    [
        "Cuando hablo frente a otras personas, primero necesito un tema. Un tema es de qué voy a hablar. Conviene escoger algo que conozco y me interesa, como mi mascota, mi juego favorito o mi comida preferida. Así me sentiré seguro.",
        "Un tema muy grande es difícil de contar. «Los animales» es demasiado grande. En cambio, «mi gato Tomás» es más pequeño. Hacer un tema pequeño se llama delimitar. Para delimitar, pregunto: ¿qué parte quiero contar? Por ejemplo, de mi gato puedo contar cómo juega.",
        "Un tema bien delimitado cabe en tres o cuatro frases. Si al pensar tengo diez ideas distintas, el tema aún es muy grande. Entonces escojo solo una parte y la cuento bien.",
    ],
    [("tema", "de qué voy a hablar"), ("delimitar", "hacer un tema más pequeño y claro"), ("interés", "lo que me gusta y me llama la atención"), ("idea", "algo que pienso y quiero decir"), ("parte", "un pedazo del tema")],
    [
        ("Hacer pequeño un tema", "El tema «los animales» es muy grande. ¿Cómo lo delimito si tengo un gato llamado Tomás?", ["Pienso en un animal que conozco.", "Escojo una parte: cómo juega.", "El tema queda «cómo juega mi gato Tomás»."], "Cómo juega mi gato Tomás"),
        ("Revisar si cabe", "El tema es «mi cumpleaños». Quiero contar la torta, los regalos, los invitados, los juegos y la música. ¿Es un tema pequeño?", ["Cuento cinco partes distintas.", "Es demasiado para pocas frases.", "Escojo una: la torta."], "No; escojo solo la torta de mi cumpleaños."),
    ],
    [("Escoger un tema muy grande.", "Se quiere contar todo.", "Escoge una parte y cuéntala bien."), ("Escoger un tema que no conozco.", "Se elige por moda.", "Elige algo que conoces o te interesa.")],
    [
        E("Entre «los animales» y «mi perro Rex», ¿cuál tema es más pequeño?", "Mi perro Rex", "Habla de un solo animal."),
        E("¿Un tema debe ser algo que conozco?", "Sí", "Así puedo hablar con seguridad."),
        E("Entre «el colegio» y «mi sala de clases», ¿cuál es el tema más pequeño?", "Mi sala de clases", "Es una parte del colegio."),
    ],
    [
        E("¿Qué significa delimitar un tema?", "Hacerlo más pequeño y claro", "Escojo una parte para contar."),
        E("¿Por qué conviene un tema pequeño?", "Porque puedo contarlo con claridad en pocas frases", "Uno grande se pierde."),
        E("Si tengo diez ideas distintas, ¿el tema es grande o pequeño?", "Grande", "Hay demasiado para contar."),
    ],
    [
        E("Tema grande: «los juegos». Escribe un tema más pequeño que tenga relación.", "Por ejemplo: cómo se juega a la escondida", "Es una parte concreta de los juegos."),
        E("Tema grande: «mi familia». Escribe un tema pequeño sobre ella.", "Por ejemplo: lo que hago con mi abuela", "Se centra en una parte."),
        E("Tema grande: «la comida». Escribe un tema pequeño que te interese.", "Por ejemplo: cómo se hace mi sándwich favorito", "Es concreto y propio."),
    ],
    [
        E("Teo quiere hablar de «todo lo que hago en las vacaciones». ¿Es buen tema para 3 frases?", "No", "Es demasiado grande."),
        E("Luz eligió «cómo cuido mis plantas». ¿Es un tema pequeño?", "Sí", "Se centra en una actividad."),
    ],
    [
        E("Ordena de más grande a más pequeño: a) mi perro Rex, b) los animales, c) cómo juega mi perro Rex. Escribe las letras.", "b, a, c", "De general a específico."),
        E("Carla tiene 3 temas posibles: su gato, su bici y su casa. Quiere hablar solo de uno. ¿Cuántos tiene que dejar?", "2", "Escoge uno y deja dos."),
    ],
    [E("Tu profesora te pide contar algo breve a tu curso. Tienes tres ideas: mi mascota, mi barrio y mi familia. Escoge una y delimítala en una frase.", "Por ejemplo: Voy a contar cómo juega mi mascota con una pelota", "Escoge un tema y lo hace pequeño.")],
    [
        E("¿Qué debe ser un buen tema: grande como un océano o pequeño y claro?", "Pequeño y claro", "Se puede contar bien."),
        E("¿Puedo hablar de lo que me gusta?", "Sí", "Un tema de interés me da seguridad."),
        E("Para delimitar pregunto: ¿qué ___ quiero contar?", "parte", "Escojo una parte del tema."),
    ],
    ("Lee estos temas grandes: «los animales», «el colegio», «mi familia», «los juegos». Escoge dos y escribe, para cada uno, un tema pequeño que podrías contar en tres frases. Luego cuenta uno a un adulto en voz alta con un comienzo claro (por ejemplo: «Hoy les voy a contar…»).",
     "Tema grande: los animales. Pequeño: cómo juega mi gato. Tema grande: mi familia. Pequeño: lo que hago con mi abuela. Conté: Hoy les voy a contar cómo juega mi gato. Salta tras una pelota.",
     ["escoge un tema pequeño por cada uno", "el tema cabe en tres frases", "empieza con una frase clara"], ["dos temas escritos", "adulto escucha la presentación"], ["temas muy grandes", "hablar de varias cosas a la vez"],
     "Si el tema sigue grande, pregunta: ¿qué parte quieres contar? y reduce."),
    "Haz una lista de tres temas pequeños que conoces bien.",
    "Delimita tres veces un mismo tema grande en tres temas pequeños distintos.",
)

reg(
    OA23, 2,
    "Las historias breves y la tabla de este cuaderno, lápiz y hoja. Se practica frente a un adulto.",
    "Aprenderé a contar un hecho en orden: primero, después y al final. Sirve para que me entiendan cuando cuento lo que me pasó.",
    ["Sé escoger un tema pequeño.", "Sé contar qué pasó."],
    [
        "Cuando cuento algo que ocurrió, conviene contarlo en orden. Primero digo cómo empezó, después qué pasó y al final cómo terminó. Si lo cuento desordenado, quienes me escuchan se confunden. El orden hace que la historia se entienda.",
        "Para marcar el orden uso palabras como «primero», «luego», «después», «más tarde» y «al final». Por ejemplo: «Primero llegamos a la plaza. Luego jugamos en el columpio. Al final tomamos helado». Cada palabra avisa el paso siguiente.",
        "También conviene decir cuándo y dónde pasó y quiénes estaban. Así tu historia tiene un lugar y un tiempo. Antes de contar, piensa tres frases: una para el inicio, una para el medio y una para el final.",
    ],
    [("orden", "una cosa después de otra"), ("primero", "lo que pasa al comienzo"), ("luego", "lo que pasa después"), ("al final", "lo que pasa al terminar"), ("evento", "algo que sucedió")],
    [
        ("Ordenar un paseo", "Frases desordenadas: «Tomamos helado», «Llegamos a la plaza», «Jugamos en el columpio». ¿En qué orden se cuenta?", ["Lo primero fue llegar.", "Luego jugaron.", "Al final tomaron helado."], "Llegamos a la plaza; jugamos en el columpio; tomamos helado."),
        ("Usar palabras de orden", "Cuenta con «primero, luego y al final»: me lavé las manos, me senté y comí.", ["Primero me lavé las manos.", "Luego me senté.", "Al final comí."], "Primero me lavé las manos, luego me senté y al final comí."),
    ],
    [("Contar de atrás para adelante.", "Se empieza por lo que más emociona.", "Empieza por lo primero que pasó."), ("No usar palabras de orden.", "No se sabe qué viene después.", "Usa primero, luego y al final.")],
    [
        E("¿Qué va primero al contar un paseo: llegar o volver a casa?", "Llegar", "Lo primero es la llegada."),
        E("¿Qué palabra marca el último paso: «al final» o «primero»?", "Al final", "Cierra la secuencia."),
        E("Si primero me lavé las manos y luego comí, ¿qué hice primero?", "Me lavé las manos", "Es lo primero que dice."),
    ],
    [
        E("¿Por qué contar en orden?", "Para que los demás entiendan la historia", "El orden evita confusiones."),
        E("¿Qué palabras marcan el orden?", "Primero, luego y al final", "Son palabras de orden."),
        E("¿Cuántas partes tiene una historia con inicio, medio y final?", "3", "Son tres partes."),
    ],
    [
        E("Ordena: a) tomamos once, b) nos sentamos a la mesa, c) mamá puso la tetera. Escribe las letras en orden lógico.", "c, b, a", "Primero se prepara, luego se sientan y al final toman once."),
        E("Escribe una frase de inicio para contar un día en la plaza, con «primero».", "Por ejemplo: Primero llegamos a la plaza", "Empieza el relato."),
        E("Escribe una frase de cierre con «al final» para ese mismo día.", "Por ejemplo: Al final volvimos a casa contentos", "Cierra el relato."),
    ],
    [
        E("Teo cuenta: «Al final nos acostamos. Primero cenamos. Luego nos lavamos los dientes.» ¿Qué orden correcto debió decir?", "Primero cenamos, luego nos lavamos los dientes y al final nos acostamos", "Es el orden en que ocurre."),
        E("Eva dice: «Fuimos a la playa y hacía calor». No dice cuándo. ¿Qué dato le falta?", "Cuándo fue", "Falta el tiempo del evento."),
    ],
    [
        E("Historia: «Lía comió. Después lavó el plato y al final lo guardó». ¿Qué hizo primero?", "Comió", "Es lo primero que cuenta la historia."),
        E("Escribe el inicio, el medio y el final de «ir a la panadería» en 3 frases separadas por punto y coma.", "Por ejemplo: Fui a la panadería; compré pan; volví a casa", "Hay inicio, medio y final."),
    ],
    [E("Quieres contar a tus abuelos cómo fue tu cumpleaños: llegaron amigos, cantaron, comieron torta y jugaron. Ordénalo con primero, luego y al final.", "Primero llegaron mis amigos, luego cantamos y comimos torta y al final jugamos", "El orden sigue lo que pasó.")],
    [
        E("¿Cómo empiezo el relato: con «primero» o con «al final»?", "Con primero", "Marca el comienzo."),
        E("¿Digo dónde ocurrió el hecho?", "Sí", "El lugar ayuda a entender."),
        E("Entre «luego» y «ayer», ¿cuál marca un paso siguiente?", "Luego", "Indica lo que viene después."),
    ],
    ("Cuenta frente a un adulto cómo fue tu mañana de hoy, en 4 frases, usando «primero», «luego» y «al final». Si necesitas ayuda, usa este modelo: «Primero me desperté. Luego me lavé la cara y me vestí. Después tomé desayuno. Al final fui a clases». Cuenta cuándo y dónde pasó lo que cuentas.",
     "Hoy en mi casa, primero me desperté. Luego me lavé los dientes y me vestí. Después desayuné pan con queso. Al final salí a la escuela.",
     ["cuenta en orden", "usa primero, luego y al final", "dice cuándo y dónde"], ["relato oral", "adulto marca las palabras de orden que oyó"], ["desorden", "falta el final"],
     "Si se pierde, pide que cuente solo el inicio y luego agregue el siguiente paso."),
    "Cuenta tu tarde de ayer en tres frases ordenadas.",
    "Cuenta el mismo hecho en otro orden y explica por qué no se entiende igual.",
)

reg(
    OA23, 3,
    "Los objetos de la casa que se nombran en cada ejercicio (una manzana, una pelota, un lápiz) y este cuaderno. Todo se describe por escrito.",
    "Aprenderé a describir con palabras de modo que otra persona pueda imaginar la cosa. Sirve para contar cómo es algo sin mostrarlo.",
    ["Sé nombrar colores y formas.", "Sé decir frases completas."],
    [
        "Describir es decir cómo es algo para que otra persona lo imagine. Para describir una cosa puedes decir su nombre, su color, su forma, su tamaño y para qué sirve. Por ejemplo: «La pelota es redonda, roja, del tamaño de mi mano y sirve para jugar».",
        "Una buena descripción usa palabras que ayudan a ver: «grande», «pequeño», «suave», «áspero» (que raspa al tocarlo), «liso», «brillante». También puedes comparar: «es suave como un algodón». Si usas sentidos, como el olor o el sonido, la descripción es más rica.",
        "Para ordenar la descripción, empieza por lo más general y termina por los detalles. Primero nombra qué es, después cómo se ve y al final para qué sirve. Si la persona puede dibujar lo que describiste, tu descripción fue buena.",
    ],
    [("describir", "decir cómo es algo"), ("detalle", "dato pequeño que da información"), ("tamaño", "qué tan grande o pequeño es"), ("forma", "figura de algo, como redonda o larga"), ("comparar", "decir en qué se parece a otra cosa")],
    [
        ("Describir una manzana", "Describe una manzana roja: nombre, color, forma y tamaño.", ["Nombre: manzana.", "Color: roja.", "Forma: redonda; tamaño: como mi puño."], "Es una manzana roja, redonda y del tamaño de mi puño."),
        ("Mejorar una descripción", "«Es una cosa grande.» ¿Cómo la mejoro si es un elefante?", ["Digo el nombre: elefante.", "Digo el color: gris.", "Agrego un detalle: tiene trompa larga."], "Es un elefante gris, grande y con trompa larga."),
    ],
    [("Decir «es una cosa» sin dar datos.", "Se piensa que todos entienden.", "Nombra y da dos o más detalles."), ("Describir sin orden.", "Se dicen detalles al azar.", "Primero qué es y luego cómo es.")],
    [
        E("Describo una pelota. ¿Qué forma tiene: redonda o cuadrada?", "Redonda", "Las pelotas son esféricas."),
        E("Describo un plátano maduro. ¿Qué color tiene?", "Amarillo", "Es su color típico."),
        E("¿Qué dato describe el tamaño: «pequeño» o «rojo»?", "Pequeño", "Pequeño es un tamaño."),
    ],
    [
        E("¿Qué es describir?", "Decir cómo es algo", "Se dan datos para imaginarlo."),
        E("¿Para qué sirve una buena descripción?", "Para que otro imagine la cosa sin verla", "Da información clara."),
        E("¿Qué sentidos puedo usar para describir una flor?", "Vista y olfato", "Veo su color y huelo su aroma."),
    ],
    [
        E("Describe un lápiz con tres datos: color, forma y para qué sirve.", "Por ejemplo: Es amarillo, largo y sirve para escribir", "Incluye tres datos."),
        E("Describe tu mochila en una frase con tamaño y color.", "Por ejemplo: Mi mochila es grande y azul", "Incluye tamaño y color."),
        E("Completa con una comparación: «La nube es suave como ___».", "Por ejemplo: algodón", "Compara con algo suave."),
    ],
    [
        E("Ana describe: «Es redondo, rojo y dulce, crece en un árbol». ¿Qué es: manzana o limón?", "Manzana", "Las manzanas son rojas y dulces."),
        E("Beto dice: «Es una cosa». ¿Qué le falta a su descripción?", "Datos como color, forma y tamaño", "No da información."),
    ],
    [
        E("Lee la descripción: «Es amarillo, largo, se pela y se come». ¿Qué fruta es?", "Plátano", "Tiene esas características."),
        E("Ordena para describir: a) sirve para jugar, b) es una pelota, c) es redonda y roja. Escribe las letras.", "b, c, a", "Primero qué es, luego cómo es y al final su uso."),
    ],
    [E("Quieres contar a un amigo cómo es tu mascota para que la reconozca. Escribe tres datos (puedes inventar la mascota: perro blanco con manchas).", "Por ejemplo: Es un perro blanco, pequeño, con manchas negras y orejas largas", "Incluye color, tamaño y detalles.")],
    [
        E("¿Puedo usar «grande» y «pequeño» al describir?", "Sí", "Son palabras de tamaño."),
        E("¿Una buena descripción permite dibujar la cosa?", "Sí", "Da datos suficientes."),
        E("¿Qué dato describe la forma: «redondo» o «azul»?", "Redondo", "Redondo es una forma."),
    ],
    ("Describe en voz alta tres objetos de tu casa a un adulto, sin decir su nombre, para que los adivine: una cuchara, un vaso y un zapato. Cada descripción debe tener al menos tres datos entre estos cuatro: forma, tamaño, color (o material) y para qué sirve. Usa este modelo: «Es pequeño, de metal, alargado y sirve para tomar sopa».",
     "Es pequeño, de metal, alargado y sirve para tomar sopa. (cuchara) Es transparente, redondo y sirve para tomar agua. (vaso) Es de cuero, se pone en el pie y sirve para caminar. (zapato)",
     ["incluye al menos tres datos por objeto", "no dice el nombre", "el adulto adivina"], ["tres descripciones habladas", "adulto confirma si adivinó"], ["dar un solo dato", "decir el nombre"],
     "Si el adulto no adivina, pregunta qué dato falta y agrégalo."),
    "Describe tu juguete favorito con cuatro datos.",
    "Describe un animal sin decir su nombre y usa una comparación.",
)

reg(
    OA23, 4,
    "Las frases y los trabalenguas cortos de este cuaderno. Un adulto escucha.",
    "Aprenderé a hablar fuerte lo suficiente, a pronunciar claro y a usar palabras precisas. Sirve para que todos me escuchen y me entiendan.",
    ["Sé hablar con frases completas.", "Sé que hay voz fuerte y suave."],
    [
        "Para que me entiendan, mi voz debe oírse. Hablo con un volumen adecuado: ni tan bajito que nadie escuche, ni tan fuerte que grite. Un buen volumen es el que se oye en toda la sala sin molestar. También hablo despacio, para que cada palabra se entienda.",
        "Pronunciar bien es decir cada sonido de la palabra con claridad. Por ejemplo, decir «pelota» y no «pelo». Abro bien la boca, digo todas las sílabas y termino cada palabra. Si trabo la lengua, repito más despacio.",
        "Escoger palabras exactas también ayuda. En vez de «cosa» puedo decir «mochila», y en vez de «bonito» puedo decir «brillante» o «suave». Las palabras exactas permiten que el otro entienda mejor lo que quiero decir.",
    ],
    [("volumen", "qué tan fuerte o suave hablo"), ("pronunciar", "decir bien los sonidos de las palabras"), ("sílaba", "parte de una palabra que se dice de un golpe de voz"), ("claro", "que se entiende bien"), ("vocabulario", "las palabras que conozco y uso")],
    [
        ("Elegir el volumen", "Estás en una sala con 20 niños y hablas casi susurrando. ¿Se oye?", ["Hay mucha gente.", "El susurro es muy bajo.", "Debo subir un poco la voz."], "No se oye; debo hablar un poco más fuerte."),
        ("Pronunciar claro", "La palabra es «mariposa». ¿Cómo la digo claro?", ["La separo: ma-ri-po-sa.", "Abro la boca.", "Digo todas las sílabas."], "Ma-ri-po-sa, con las cuatro sílabas completas."),
    ],
    [("Hablar muy bajito.", "Da vergüenza.", "Sube un poco la voz y respira antes."), ("Hablar muy rápido y comerse sílabas.", "Hay nervios.", "Habla más despacio y completa cada palabra.")],
    [
        E("¿Cuántas sílabas tiene la palabra «mariposa»: 4 o 3?", "4", "Son ma, ri, po y sa."),
        E("En una sala grande, ¿qué volumen conviene: susurro o voz clara?", "Voz clara", "Así todos oyen."),
        E("¿Qué es mejor: hablar despacio o muy rápido?", "Despacio", "Se entiende cada palabra."),
    ],
    [
        E("¿Por qué conviene pronunciar bien?", "Para que se entienda cada palabra", "Una palabra mal dicha confunde."),
        E("¿Qué hago si me trabo con una palabra?", "La repito más despacio", "Así la pronuncio mejor."),
        E("¿Qué palabra es más exacta: «cosa» o «mochila»?", "Mochila", "Nombra algo concreto."),
    ],
    [
        E("Separa en sílabas la palabra «pelota».", "pe-lo-ta", "Tiene tres golpes de voz."),
        E("Cambia «cosa» por una palabra exacta en: «Puse la cosa en la mesa». Escribe una opción.", "Por ejemplo: Puse el libro en la mesa", "Una palabra exacta nombra el objeto."),
        E("Cambia «bonito» por una palabra más exacta para describir una flor.", "Por ejemplo: colorida", "Dice cómo es la flor."),
    ],
    [
        E("Mía dice: «el pato nada en el estanque» tan rápido que no se entiende. ¿Qué debe cambiar?", "Hablar más despacio", "Así se entiende cada sílaba."),
        E("Luis habla tan fuerte que molesta al curso. ¿Qué debe cambiar?", "Bajar un poco el volumen", "Debe ser adecuado, no gritar."),
    ],
    [
        E("Di despacio y cuenta las sílabas de: «ca-ra-co-la». ¿Cuántas tiene?", "4", "Ca, ra, co, la."),
        E("Frase: «El gato peludo duerme en la alfombra». Separa en sílabas la palabra «alfombra».", "al-fom-bra", "Tiene tres golpes de voz."),
    ],
    [E("Vas a presentar un tema ante tu curso en una sala grande. Escribe dos cosas que harás con tu voz.", "Por ejemplo: hablaré despacio y con voz clara", "Ayudan a que todos oigan.")],
    [
        E("¿Pronuncio todas las sílabas?", "Sí", "Así se entienden las palabras."),
        E("Para hablar claro, ¿abro bien la boca?", "Sí", "Ayuda a pronunciar."),
        E("¿Qué palabra es más exacta para un animal: «perro» o «cosa»?", "Perro", "Nombra el animal."),
    ],
    ("Lee estas tres frases en voz alta, despacio, abriendo bien la boca, y pide a un adulto que marque si oyó todas las palabras. Frase 1: «La mariposa se posó sobre una rosa». Frase 2: «Mi tortuga camina despacio por el jardín». Frase 3: «El caracol sube por la ventana». Luego agrega en cada frase un dato exacto (por ejemplo, «mariposa amarilla»).",
     "La mariposa amarilla se posó sobre una rosa roja. Mi tortuga verde camina despacio por el jardín. El caracol pequeño sube por la ventana. El adulto oyó todas las palabras.",
     ["volumen adecuado", "pronuncia todas las sílabas", "agrega palabras exactas"], ["lectura oral", "adulto marca si oyó las palabras"], ["comer sílabas", "hablar muy bajo"],
     "Si el adulto no oyó una palabra, repite esa palabra sola, despacio, y luego la frase."),
    "Repite en voz alta cinco palabras con tres sílabas y cuenta sus sílabas.",
    "Cambia tres palabras generales de tu vida (cosa, bonito, grande) por palabras exactas.",
)

reg(
    OA23, 5,
    "La pauta de este cuaderno, lápiz y hoja. Un adulto o un compañero escucha.",
    "Aprenderé a presentar un tema corto, a escuchar a otros y a mejorar con sus comentarios. Sirve para hablar en público con seguridad.",
    ["Sé delimitar un tema, ordenar lo que cuento, describir y hablar claro."],
    [
        "Presentar es contar un tema a un público. Una presentación breve tiene tres partes: un comienzo donde digo mi nombre y el tema, un desarrollo donde cuento dos o tres ideas en orden, y un cierre donde termino con una frase final. Por ejemplo: «Hoy les cuento sobre mi gato. Mi gato es gris. Le gusta dormir. Gracias por escuchar».",
        "Mientras presento, miro al público, hablo con voz clara y uso mis manos con calma. Cuando otra persona presenta, la escucho en silencio y miro. Al final puedo decir algo bueno de su presentación y hacerle una pregunta sobre el tema.",
        "Cuando me dan un comentario, escucho sin enojarme. Un comentario sirve para mejorar. Puedo decir: «Gracias, la próxima vez hablaré más fuerte». Mejorar es volver a presentar cambiando una cosa.",
    ],
    [("presentación", "contar un tema a un público"), ("comienzo", "parte inicial de la presentación"), ("desarrollo", "parte central con las ideas"), ("cierre", "parte final"), ("comentario", "opinión para ayudar a mejorar")],
    [
        ("Armar una presentación", "Tema: mi gato. Ideas: es gris; le gusta dormir. Arma comienzo, desarrollo y cierre.", ["Comienzo: Hoy les cuento sobre mi gato.", "Desarrollo: es gris y le gusta dormir.", "Cierre: Gracias por escuchar."], "Hoy les cuento sobre mi gato. Es gris. Le gusta dormir. Gracias por escuchar."),
        ("Recibir un comentario", "Tu compañero te dice: «Hablaste muy bajito». ¿Qué respondes?", ["Escucho sin enojarme.", "Agradezco el comentario.", "Digo cómo mejoraré."], "Gracias; la próxima vez hablaré más fuerte."),
    ],
    [("Terminar sin cierre.", "No se sabe cómo acabar.", "Dile al público «Gracias por escuchar»."), ("Enojarse con un comentario.", "Se piensa que es una crítica.", "Recuerda que ayuda a mejorar.")],
    [
        E("¿Cuántas partes tiene una presentación: comienzo, desarrollo y cierre?", "3", "Son tres partes."),
        E("¿Qué digo al terminar: «Gracias por escuchar» o nada?", "Gracias por escuchar", "Es un buen cierre."),
        E("Mientras otro presenta, ¿qué hago?", "Escucho en silencio", "Así muestro respeto."),
    ],
    [
        E("¿Qué dice el comienzo de la presentación?", "Mi nombre y el tema", "Presenta de qué trata."),
        E("¿Para qué sirve un comentario sobre mi presentación?", "Para mejorar la próxima vez", "Muestra qué ajustar."),
        E("¿Por qué miro al público?", "Para mostrar que hablo con ellos", "Así genero conexión."),
    ],
    [
        E("Arma un comienzo para una presentación sobre tu juego favorito. Usa el nombre «Ana».", "Por ejemplo: Hola, soy Ana y les voy a contar sobre mi juego favorito", "Dice nombre y tema."),
        E("Escribe un cierre para esa presentación.", "Por ejemplo: Eso es todo; gracias por escuchar", "Cierra la presentación."),
        E("Escribe una pregunta para el compañero que presentó sobre su perro.", "Por ejemplo: ¿Cómo se llama tu perro?", "Se relaciona con el tema."),
    ],
    [
        E("Teo presentó sin decir su tema al inicio. ¿Qué parte le faltó?", "El comienzo", "No dijo de qué hablaría."),
        E("Luz recibió el comentario «Mira más al público» y dijo «No me importa». ¿Fue una buena respuesta?", "No", "Un comentario sirve para mejorar."),
    ],
    [
        E("Ordena una presentación: a) Gracias por escuchar, b) Hoy les cuento sobre mi gato, c) Es gris y juega con una pelota. Escribe las letras.", "b, c, a", "Comienzo, desarrollo y cierre."),
        E("Una presentación tiene 1 frase de comienzo, 3 de desarrollo y 1 de cierre. ¿Cuántas frases son en total?", "5", "1 + 3 + 1 = 5."),
    ],
    [E("En tu curso, cada niño presenta su comida favorita. A Mía le dicen: «Tu presentación fue clara, pero poco fuerte». Escribe qué hará ella para mejorar.", "Por ejemplo: Hablaré más fuerte y respiraré antes", "Aplica el comentario.")],
    [
        E("¿Cómo respondo a un comentario: «gracias» o «no me importa»?", "Gracias", "Es una respuesta respetuosa."),
        E("¿Hago preguntas a quien presenta?", "Sí, relacionadas con su tema", "Las preguntas muestran interés."),
        E("¿Cuál es la última parte de una presentación?", "El cierre", "Termina la presentación."),
    ],
    ("Prepara y presenta a un adulto (de 30 segundos a 1 minuto) un tema pequeño que escojas de esta lista: mi mascota, mi juego favorito, mi comida favorita, mi lugar preferido. Usa tres partes: comienzo (tu nombre y tema), desarrollo (dos o tres frases en orden con una descripción) y cierre. Pide al adulto un comentario con esta pauta: voz clara, orden de ideas y mirada. Luego mejora una cosa y vuelve a presentar.",
     "Hola, soy Ana y les voy a contar sobre mi mascota. Primero, mi gata es gris y pequeña. Luego, le gusta dormir en mi cama. Al final, me despierta con su ronroneo. Gracias por escuchar. Comentario: más fuerte la voz. Mejoré: hablé más fuerte.",
     ["tiene comienzo, desarrollo y cierre", "usa voz clara y mira al público", "mejora una cosa"], ["presentación oral", "pauta con comentario del adulto"], ["no tener cierre", "no mirar al público"],
     "Si no mejora nada, elige un solo punto de la pauta y practica solo eso antes de repetir."),
    "Repite tu presentación frente a un espejo.",
    "Presenta el mismo tema a una persona distinta y compara qué mejoró.",
)

# ================================================================ OA 24
reg(
    OA24, 1,
    "Los textos de este cuaderno, lápiz y hoja. Un adulto lee en voz alta.",
    "Aprenderé a escuchar una palabra nueva y a entender qué significa. Sirve para tener más palabras y hablar con más precisión.",
    ["Sé que hay palabras que aún no conozco.", "Sé escuchar atento."],
    [
        "Cada día escuchamos palabras nuevas. Cuando una palabra nueva aparece en una conversación o en un cuento, presto atención a cómo la dicen y a qué sigue. Por ejemplo, si alguien dice «Tomás es curioso: pregunta todo», la palabra nueva es «curioso» y la pista es «pregunta todo».",
        "Para quedarme con la palabra, la repito en voz alta, la separo en sílabas (cu-rio-so) y digo qué significa con mis palabras: «una persona que quiere saber cosas». Si no estoy seguro, pregunto o busco una pista en la frase.",
        "Una palabra nueva se aprende mejor si la escucho en una frase real y la relaciono con algo que conozco. Por ejemplo, curioso se parece a mi hermano, que siempre pregunta por qué. Así la palabra se vuelve parte de mi vocabulario.",
    ],
    [("palabra nueva", "palabra que escucho por primera vez"), ("curioso", "que quiere saber y aprender cosas"), ("sílaba", "parte de una palabra"), ("pista", "señal para descubrir el significado"), ("vocabulario", "las palabras que conozco")],
    [
        ("Atrapar la palabra", "Escuchas: «Tomás es curioso: pregunta todo». ¿Cuál es la palabra nueva y qué significa?", ["La palabra nueva es «curioso».", "La pista es «pregunta todo».", "Significa que quiere saber."], "Curioso: que quiere saber cosas."),
        ("Repetir y separar", "La palabra nueva es «refugio». ¿Cómo la repito?", ["Digo re-fu-gio.", "La digo despacio.", "Pienso qué significa: lugar para protegerse."], "Re-fu-gio: lugar donde me protejo."),
    ],
    [("Dejar pasar la palabra nueva.", "Se piensa que no es importante.", "Detente y repítela."), ("Aprender la palabra sin pensar en su frase.", "Se memoriza sola.", "Usa la frase para entenderla.")],
    [
        E("Escuchas: «El conejo es veloz: corre muy rápido». ¿Cuál es la palabra nueva?", "Veloz", "Es la menos común de la frase."),
        E("¿Cuántas sílabas tiene «curioso»?", "3", "Se separa cu, rio, so."),
        E("En «Tomás es curioso: pregunta todo», ¿cuál es la pista?", "Pregunta todo", "Explica cómo es Tomás."),
    ],
    [
        E("¿Qué hago cuando oigo una palabra nueva?", "La repito y pienso qué significa", "Así la fijo."),
        E("¿Por qué conviene oírla en una frase?", "Porque la frase da pistas", "El contexto ayuda a entender."),
        E("¿Qué significa «refugio»?", "Un lugar donde me protejo", "Protege del frío o la lluvia."),
    ],
    [
        E("Separa en sílabas «refugio».", "re-fu-gio", "Tiene tres golpes de voz."),
        E("Escucha «El perro es leal: siempre me acompaña». Escribe qué crees que significa «leal».", "Que acompaña siempre y no abandona", "La pista es «siempre me acompaña»."),
        E("Escucha «La noche estaba serena: sin viento ni ruido». Escribe qué crees que significa «serena».", "Tranquila", "Sin viento ni ruido, todo está en calma."),
    ],
    [
        E("Ana dice que «curioso» es quien pregunta todo. Beto cree que significa «dormilón». ¿Quién tiene la idea correcta con la frase de Tomás?", "Ana", "La frase dice «pregunta todo»."),
        E("Luz repitió la palabra «refugio» tres veces y dijo qué significa. ¿Hizo un buen trabajo para aprenderla?", "Sí", "Repetir y explicar ayuda."),
    ],
    [
        E("Escucha: «El gato es ágil: salta de la mesa al estante sin caerse». ¿Qué significa «ágil»?", "Que se mueve con facilidad y rapidez", "Salta sin caerse."),
        E("Escucha: «Hoy el patio está desierto: no hay nadie». ¿Qué significa «desierto»?", "Sin personas", "La pista es «no hay nadie»."),
    ],
    [E("Tu profesora dice: «Hoy seremos pacientes: esperaremos nuestro turno sin apuro». Tomás no sabe «pacientes». Escribe qué significa.", "Que esperan con calma sin apuro", "La pista es «esperaremos sin apuro».")],
    [
        E("¿Repito la palabra nueva en voz alta?", "Sí", "Ayuda a recordarla."),
        E("¿Una palabra nueva se parece a algo que ya conozco?", "A veces", "Relacionarla con algo ayuda."),
        E("¿Qué palabra nueva significa «lugar para protegerse»?", "Refugio", "Es su significado."),
    ],
    ("Escucha estas cuatro frases (un adulto las lee) y para cada una anota: la palabra nueva, la pista y qué significa. Frase 1: «Mi tía es generosa: siempre comparte su comida». Frase 2: «El pasillo estaba oscuro: casi no se veía». Frase 3: «La abuela es paciente: nunca se enoja si me demoro». Frase 4: «El río es angosto: apenas cabe un bote».",
     "1) generosa; pista: comparte su comida; significa que da a otros. 2) oscuro; pista: casi no se veía; sin luz. 3) paciente; pista: nunca se enoja si me demoro; espera con calma. 4) angosto; pista: apenas cabe un bote; poco ancho.",
     ["identifica una palabra nueva por frase", "dice la pista", "explica con sus palabras"], ["hoja con cuatro filas o respuesta oral"], ["no dar pista", "repetir la frase completa"],
     "Si no da pista, pide que subraye en la frase la parte que lo ayudó."),
    "Cuenta a alguien de tu casa una palabra nueva que aprendiste hoy.",
    "Escucha una conversación en casa y anota una palabra nueva para averiguar.",
)

reg(
    OA24, 2,
    "Los ejemplos escritos de este cuaderno, lápiz y hoja. Se practica con un adulto.",
    "Aprenderé a explicar una palabra nueva con ejemplos y a decir cuándo se usa. Sirve para que otros entiendan lo que quiero decir.",
    ["Sé escuchar una palabra nueva y repetirla.", "Sé dar ejemplos."],
    [
        "Para entender una palabra nueva, no basta con repetirla. Conviene explicarla con ejemplos. Por ejemplo, «generoso» es quien comparte con otros. Un ejemplo: «Mi tío es generoso porque me regala la mitad de su pan». Otro ejemplo: «Luz es generosa porque presta sus lápices».",
        "Un buen ejemplo muestra a alguien o algo que cumple con el significado. Uno que no lo cumple es un no ejemplo: «Pedro no es generoso porque no comparte sus juguetes». Mirar ejemplos y no ejemplos ayuda a distinguir cuándo usar la palabra.",
        "Para explicar con claridad, usa esta forma: «La palabra es…, significa… y un ejemplo es…». Por ejemplo: «La palabra es paciente, significa que espera con calma, y un ejemplo es mi abuela cuando espera a que me vista».",
    ],
    [("ejemplo", "caso que muestra cómo es algo"), ("no ejemplo", "caso que no cumple el significado"), ("generoso", "que comparte con otros"), ("paciente", "que espera con calma"), ("explicar", "decir con claridad qué significa")],
    [
        ("Dar un ejemplo", "Palabra: «generoso». ¿Cuál es un ejemplo?", ["Pienso en alguien que comparte.", "Digo: Luz presta sus lápices.", "Explico por qué cumple."], "Luz es generosa porque presta sus lápices."),
        ("Un no ejemplo", "Palabra: «paciente». ¿Cuál es un no ejemplo?", ["Pienso en alguien que no espera.", "Digo: Pedro grita si debe esperar.", "No cumple el significado."], "Pedro no es paciente porque grita cuando debe esperar."),
    ],
    [("Dar solo la palabra sin explicar.", "Se cree que todos la entienden.", "Agrega significado y un ejemplo."), ("Dar un ejemplo que no sirve.", "No se piensa si cumple.", "Pregunta: ¿cumple el significado?")],
    [
        E("¿«Compartir la comida» es un ejemplo de «generoso»?", "Sí", "Dar a otros es ser generoso."),
        E("¿«Esperar el turno con calma» es un ejemplo de «paciente»?", "Sí", "Esperar con calma es paciencia."),
        E("¿«Quitar el lápiz de otro» es un ejemplo de «generoso»?", "No", "Quitar no es compartir."),
    ],
    [
        E("¿Qué es un no ejemplo?", "Un caso que no cumple el significado", "Sirve para distinguir."),
        E("¿Por qué conviene dar ejemplos?", "Para que otros entiendan cómo se usa la palabra", "Los ejemplos aclaran."),
        E("¿Qué tres partes tiene una buena explicación de una palabra?", "Palabra, significado y ejemplo", "Es una forma clara de explicar."),
    ],
    [
        E("Explica «curioso» con la forma palabra, significado y ejemplo.", "Por ejemplo: La palabra es curioso, significa que quiere saber, y un ejemplo es mi hermano que pregunta por todo", "Tiene las tres partes."),
        E("Escribe un ejemplo de «paciente».", "Por ejemplo: Ana es paciente porque espera su turno", "Cumple el significado."),
        E("Escribe un no ejemplo de «ordenado» (que deja todo en su lugar).", "Por ejemplo: Beto dejó sus juguetes en el piso", "No cumple el significado."),
    ],
    [
        E("Pedro dice: «Luz es generosa porque no presta nada». ¿Su ejemplo es correcto?", "No", "No prestar no es ser generoso."),
        E("Eva dice: «Soy paciente porque grito si me hacen esperar». ¿Es un buen ejemplo?", "No", "Gritar no es esperar con calma."),
    ],
    [
        E("Palabra: «ágil» (que se mueve con facilidad y rapidez). Ejemplos: a) un gato que salta de una mesa a otra, b) una piedra en el suelo. ¿Cuál cumple?", "a", "Un gato salta con facilidad."),
        E("Palabra: «tímido» (que le da vergüenza estar con otros). ¿Qué ejemplo es mejor: a) un niño que se esconde cuando lo miran, b) un niño que habla a gritos?", "a", "Esconderse indica timidez."),
    ],
    [E("Tu hermano menor te pregunta qué significa «generoso». Explícaselo con significado y un ejemplo de tu casa.", "Por ejemplo: Generoso es quien comparte; mamá es generosa porque nos da de su postre", "Tiene significado y ejemplo.")],
    [
        E("¿Los ejemplos ayudan a entender?", "Sí", "Muestran el significado en acción."),
        E("¿Todo ejemplo debe cumplir el significado?", "Sí", "Si no cumple, es un no ejemplo."),
        E("¿Qué palabra significa «quien comparte»?", "Generoso", "Es su significado."),
    ],
    ("Escoge dos de estas palabras: generoso (que comparte), paciente (que espera con calma), curioso (que quiere saber) y ordenado (que deja todo en su lugar). Para cada una, di en voz alta a un adulto: «La palabra es…, significa… y un ejemplo es…» y agrega un no ejemplo.",
     "La palabra es generoso, significa que comparte, y un ejemplo es Luz, que presta sus lápices. Un no ejemplo es Pedro, que no comparte sus juguetes. La palabra es paciente, significa que espera con calma, y un ejemplo es mi abuela.",
     ["dice la palabra, significado y ejemplo", "agrega un no ejemplo", "el adulto comprende"], ["explicación oral de dos palabras"], ["ejemplo que no cumple", "olvidar el significado"],
     "Si el ejemplo no cumple, pregunta: ¿esa persona hace lo que dice la palabra?"),
    "Explica a alguien de tu casa «curioso» con un ejemplo.",
    "Piensa dos casos que muestren «ordenado» y uno que no.",
)

reg(
    OA24, 3,
    "Las situaciones y los diálogos de este cuaderno, lápiz y hoja. Se practica con un adulto.",
    "Aprenderé a usar una palabra nueva cuando converso, en el momento adecuado. Sirve para hablar con más precisión y que me entiendan mejor.",
    ["Sé explicar una palabra con ejemplos."],
    [
        "Una palabra nueva se aprende de verdad cuando la uso. Para usarla en una conversación, primero pienso en qué situación sirve. Por ejemplo, «paciente» sirve cuando alguien espera con calma, «curioso» cuando quiere saber algo, y «generoso» cuando comparte.",
        "Después busco el momento: espero mi turno y la digo en una frase completa que tenga sentido. Por ejemplo: «Mi abuela es paciente porque nunca se enoja cuando me demoro». Si me equivoco, puedo corregir y probar de nuevo.",
        "Usar una palabra nueva con naturalidad toma práctica. Puedes empezar con una palabra por día. Ponla en una conversación con tu familia y pide que te digan si tenía sentido. Cuando la usas varias veces, ya es tuya.",
    ],
    [("usar", "decir o escribir la palabra en una frase"), ("adecuado", "que sirve para la situación"), ("turno", "momento en que hablo"), ("práctica", "hacer algo muchas veces para mejorar"), ("naturalidad", "hacerlo fácil, sin esfuerzo")],
    [
        ("Elegir la palabra", "Tu hermano espera su turno sin molestarse. ¿Qué palabra nueva usas: paciente o curioso?", ["Veo lo que hace.", "Espera con calma.", "Corresponde «paciente»."], "Mi hermano es paciente porque espera su turno con calma."),
        ("Usarla en conversación", "Tu amiga comparte su colación. ¿Qué dices usando «generosa»?", ["Pienso en lo que hizo.", "Elijo la palabra.", "La digo en una frase completa."], "Eres generosa porque compartiste tu colación."),
    ],
    [("Usar la palabra donde no cabe.", "Se quiere probar sin pensar.", "Piensa si la situación cumple el significado."), ("Decir la palabra sin frase.", "Se la dice sola.", "Úsala en una frase completa.")],
    [
        E("Un niño que pregunta todo, ¿es curioso o generoso?", "Curioso", "Curioso es quien quiere saber."),
        E("¿Una frase con «paciente» debe tener sentido?", "Sí", "La palabra debe encajar."),
        E("Mi amiga comparte su pan. ¿Cuál palabra uso: generosa o tímida?", "Generosa", "Compartir es ser generosa."),
    ],
    [
        E("¿Cuándo uso la palabra «paciente»?", "Cuando alguien espera con calma", "Ese es su significado."),
        E("¿Por qué conviene practicar la palabra cada día?", "Para que sea parte de mi vocabulario", "La práctica la fija."),
        E("¿Digo la palabra en cualquier momento o cuando cabe?", "Cuando cabe", "Debe tener sentido."),
    ],
    [
        E("Usa «curioso» en una frase sobre un gato que mira por la ventana.", "Por ejemplo: El gato es curioso porque mira todo por la ventana", "La frase respeta el significado."),
        E("Usa «paciente» en una frase sobre tu abuelo que espera el bus.", "Por ejemplo: Mi abuelo es paciente porque espera el bus tranquilo", "Usa bien la palabra."),
        E("Usa «ordenado» en una frase sobre tu cuarto.", "Por ejemplo: Mi cuarto está ordenado porque guardé mis juguetes", "La frase cumple el significado."),
    ],
    [
        E("Diálogo: Ana: «Mi hermano espera con calma». Beto: «Es muy curioso». ¿Usó bien la palabra Beto?", "No, debió decir paciente", "Esperar con calma es ser paciente."),
        E("Luz dice: «El perro es generoso porque ladra». ¿Usó bien la palabra?", "No", "Ladrar no es compartir."),
    ],
    [
        E("Un diálogo: «¿Por qué miras tanto la luna?» «Soy curiosa; quiero saber cómo es». ¿Qué palabra nueva usa la niña?", "curiosa", "Está en su respuesta."),
        E("Completa: «Mi mamá es ___ porque comparte su postre».", "generosa", "Compartir es ser generosa."),
    ],
    [E("Tu amiga espera su turno en el columpio sin quejarse. Quieres felicitarla usando «paciente». ¿Qué le dices?", "Por ejemplo: Eres paciente porque esperaste tu turno sin quejarte", "Usa la palabra con sentido.")],
    [
        E("Si uso una palabra nueva, ¿la pongo en una frase completa?", "Sí", "Así tiene sentido."),
        E("¿Practicar una palabra por día ayuda?", "Sí", "Ayuda a recordarla."),
        E("¿Puedo corregir si me equivoco?", "Sí", "Es parte de aprender."),
    ],
    ("Escoge tres palabras de esta lista: paciente, generoso, curioso, ordenado, tímido (que le da vergüenza estar con otros). Para cada una escribe una frase sobre una persona de tu familia y dila en voz alta. Después usa una de ellas en una conversación real con un adulto y pregunta si tenía sentido.",
     "Mi abuela es paciente porque espera con calma. Mi tío es generoso porque comparte su pan. Mi hermano es curioso porque pregunta todo. Dije «paciente» en la mesa y mamá dijo que tenía sentido.",
     ["tres frases con sentido", "usa la palabra en conversación", "el adulto confirma sentido"], ["tres frases", "adulto confirma el uso"], ["usar la palabra donde no calza", "no decir frase completa"],
     "Si la frase no calza, pide que repita el significado y arme otra."),
    "Usa «paciente» hoy en una conversación real.",
    "Usa una palabra nueva en tres situaciones distintas y cuenta cómo cambió la frase.",
)

reg(
    OA24, 4,
    "Las frases y las tablas de este cuaderno, lápiz y hoja. Se practica con un adulto.",
    "Aprenderé a cambiar una palabra general por otra más exacta. Sirve para decir con precisión lo que quiero comunicar.",
    ["Sé usar palabras nuevas en frases."],
    [
        "A veces usamos palabras muy generales como «cosa», «bonito» o «animal». Reformular es decir lo mismo con palabras más exactas. Por ejemplo, en vez de «cosa» puedo decir «mochila», y en vez de «bonito» puedo decir «colorido» o «suave», según lo que quiera describir.",
        "Para reformular, hago tres preguntas: ¿qué quiero decir exactamente? ¿qué palabra lo dice mejor? ¿suena bien en la frase? Por ejemplo: «La cosa está en la mesa» pasa a «El libro está sobre la mesa». Ahora se entiende de qué hablo.",
        "Reformular también sirve cuando alguien no me entendió. Puedo decir: «Quise decir que…» y usar palabras más claras. Así corrijo con calma y todos comprenden mejor.",
    ],
    [("reformular", "decir lo mismo con otras palabras más claras"), ("exacto", "que dice justo lo que quiero decir"), ("general", "que sirve para muchas cosas"), ("preciso", "claro y exacto"), ("quise decir", "frase para aclarar lo que dije")],
    [
        ("Cambiar «cosa»", "«La cosa está en la mesa.» Sabes que es un libro. ¿Cómo lo reformulas?", ["Pregunto qué cosa es.", "Es un libro.", "Cambio «cosa» por «libro»."], "El libro está sobre la mesa."),
        ("Cambiar «bonito»", "«Mi gato es bonito.» Su pelo es suave y gris. ¿Cómo lo reformulas?", ["Pienso qué lo hace bonito.", "Es suave y gris.", "Escribo una frase exacta."], "Mi gato tiene el pelo suave y gris."),
    ],
    [("Usar siempre «cosa».", "Es más fácil.", "Piensa el nombre exacto."), ("Cambiar la palabra y perder el sentido.", "No se relee la frase.", "Relee y comprueba.")],
    [
        E("¿Qué palabra es más exacta: «cosa» o «lápiz»?", "Lápiz", "Nombra un objeto concreto."),
        E("¿Qué palabra es más exacta para un animal: «bicho» o «mariposa»?", "Mariposa", "Dice cuál es el animal."),
        E("Reformular, ¿es decir lo mismo con palabras más exactas?", "Sí", "Eso significa reformular."),
    ],
    [
        E("¿Para qué sirve reformular?", "Para que me entiendan mejor", "Se dicen las ideas con claridad."),
        E("¿Qué frase uso para aclarar lo que dije?", "Quise decir que…", "Introduce la aclaración."),
        E("¿Por qué «cosa» no es una palabra precisa?", "Porque sirve para muchas cosas", "No dice cuál."),
    ],
    [
        E("Reformula: «La cosa roja está en el patio» si es una pelota.", "La pelota roja está en el patio", "Se cambia cosa por pelota."),
        E("Reformula «mi casa es bonita» diciendo cómo es: tiene un jardín con flores.", "Mi casa tiene un jardín con flores", "Dice qué la hace bonita."),
        E("Reformula «Hay muchos animales» si en la granja hay vacas, gallinas y cerdos.", "En la granja hay vacas, gallinas y cerdos", "Nombra los animales."),
    ],
    [
        E("Beto dijo «Dame esa cosa» y Ana le pasó la regla. Quería el borrador. ¿Qué debió decir?", "Dame el borrador", "Nombró el objeto exacto."),
        E("Luz dice «Vi un animal grande». Pedro no sabe cuál. ¿Cómo podría reformular?", "Por ejemplo: Vi un elefante grande", "Nombra el animal."),
    ],
    [
        E("Reformula con tres datos: «Tengo una cosa» (es una mochila azul con dos bolsillos).", "Tengo una mochila azul con dos bolsillos", "Nombra y describe."),
        E("Elige la frase más precisa: a) «Compré cosas», b) «Compré pan, leche y huevos».", "b", "Dice qué compró."),
    ],
    [E("Tu hermana te pregunta «¿Dónde está la cosa que usé ayer?». Reformula para que sepas qué busca: era una linterna.", "¿Dónde está la linterna que usé ayer?", "Nombra el objeto exacto.")],
    [
        E("¿«Cosa» es una palabra exacta?", "No", "Es muy general."),
        E("¿Puedo reformular si alguien no me entendió?", "Sí", "Digo «quise decir que…»."),
        E("¿Qué es mejor decir: «un animal» o «un conejo» si hablo de un conejo?", "Un conejo", "Es más exacto."),
    ],
    ("Reformula estas cuatro frases con palabras más exactas, usando los datos entre paréntesis. 1) «Me puse la cosa» (es una bufanda roja). 2) «El lugar es bonito» (tiene un río con patos). 3) «Compré cosas» (pan, leche y huevos). 4) «Vi un animal» (era un zorro). Dilas en voz alta a un adulto.",
     "1) Me puse la bufanda roja. 2) El lugar tiene un río con patos. 3) Compré pan, leche y huevos. 4) Vi un zorro.",
     ["usa los datos", "cada frase es más exacta", "se entiende"], ["cuatro frases reformuladas"], ["seguir usando cosa", "inventar datos distintos"],
     "Si repite «cosa», pide que mire los datos entre paréntesis y escoja el nombre exacto."),
    "Hoy evita decir «cosa» durante una hora y usa nombres exactos.",
    "Reformula una descripción vaga que escuches en tu casa.",
)

reg(
    OA24, 5,
    "Las situaciones escritas en este cuaderno, lápiz y hoja. Se practica con un adulto.",
    "Aprenderé a usar una palabra nueva en situaciones distintas. Sirve para que la palabra me acompañe siempre, no solo en una clase.",
    ["Sé usar y explicar una palabra nueva."],
    [
        "Una palabra nueva se vuelve tuya cuando puedes usarla en varios lugares y con distintas personas. A eso se le llama transferir. Por ejemplo, «refugio» se usa en una excursión («nos protegimos en un refugio»), en una casa («mi casa es un refugio») y en un cuento («el oso buscó un refugio»).",
        "Cada vez que uso la palabra en otro lugar, pienso: ¿sigue significando lo mismo? Sí, «refugio» siempre es un lugar donde alguien se protege. Cambia el lugar, pero el significado se mantiene. Si el significado no cambia, la uso bien.",
        "También puedo hablar distinto según con quién estoy. A un amigo le digo «mi cuarto es mi refugio», y a un adulto le digo «la casa es un refugio para toda la familia». La palabra es la misma, pero cambio la frase según la situación.",
    ],
    [("transferir", "usar lo aprendido en otra situación"), ("refugio", "lugar donde alguien se protege"), ("contexto", "situación en que se usa una palabra"), ("significado", "lo que quiere decir la palabra"), ("situación", "lugar y momento donde hablo")],
    [
        ("Usarla en otro lugar", "Palabra: «refugio». Ya la usaste en una excursión. ¿Cómo la usas en tu casa?", ["El significado es lugar para protegerme.", "Pienso en mi casa.", "Armo la frase."], "Mi casa es un refugio cuando llueve."),
        ("Cambiar de persona", "Quieres decir «refugio» a un amigo y a un adulto. ¿Qué dices a cada uno?", ["Amigo: más cercano.", "Adulto: más formal.", "La palabra es la misma."], "Amigo: mi cuarto es mi refugio. Adulto: la casa es un refugio para la familia."),
    ],
    [("Creer que la palabra solo sirve en un lugar.", "Se la aprendió en un solo caso.", "Prueba otras situaciones."), ("Cambiar el significado.", "Se confunde con otra palabra.", "Pregunta si el significado se mantiene.")],
    [
        E("¿«Refugio» significa lugar de protección?", "Sí", "Es su significado."),
        E("En una excursión, la lluvia empieza y nos cubrimos en una cabaña. ¿Qué palabra nueva uso: refugio o paciente?", "Refugio", "La cabaña nos protege."),
        E("¿El significado de «refugio» cambia en un cuento?", "No", "Sigue siendo un lugar para protegerse."),
    ],
    [
        E("¿Qué significa transferir una palabra?", "Usarla en otra situación", "Se aplica en varios contextos."),
        E("¿Por qué conviene usar la palabra en distintos lugares?", "Para que se vuelva parte de mi vocabulario", "Así la uso con seguridad en cualquier situación."),
        E("¿La palabra cambia de significado en otra situación?", "No", "Solo cambia la frase."),
    ],
    [
        E("Usa «refugio» en una frase sobre un oso en el bosque.", "Por ejemplo: El oso encontró un refugio en la cueva", "La cueva lo protege."),
        E("Usa «paciente» en una frase sobre una fila del supermercado.", "Por ejemplo: Mi mamá es paciente en la fila", "Espera con calma."),
        E("Usa «curioso» en una frase sobre un niño en un museo.", "Por ejemplo: El niño curioso preguntó por todas las piezas", "Cumple el significado."),
    ],
    [
        E("Un niño dice «Mi refugio es la plaza» porque allí no se siente solo. ¿Usó bien la palabra?", "Sí", "La plaza es un lugar donde se siente protegido."),
        E("Una niña dice «El refugio es una fruta». ¿Usó bien la palabra?", "No", "Refugio es un lugar, no una fruta."),
    ],
    [
        E("Una misma palabra, «refugio», en 3 situaciones: casa, cueva y cabaña. ¿Cuántas situaciones hay?", "3", "Son tres situaciones."),
        E("Elige la frase que usa bien «refugio»: a) El gato se escondió en un refugio durante la tormenta, b) El refugio corre muy rápido.", "a", "El gato se protege en un lugar."),
    ],
    [E("Estás de paseo con tu familia y empieza a llover. Ven un quiosco con techo. Usa la palabra «refugio» para decirlo.", "Por ejemplo: Corramos al quiosco: es un buen refugio para la lluvia", "Usa la palabra en una situación nueva.")],
    [
        E("¿Puedo usar «refugio» en un cuento?", "Sí", "La palabra sirve en varias situaciones."),
        E("¿Hablo igual a un amigo que a un adulto?", "No, adapto la frase", "La situación cambia."),
        E("¿Me sirve repetir la palabra en varios lugares?", "Sí", "La palabra se vuelve mía."),
    ],
    ("Escoge una palabra de esta lista: refugio, paciente, curioso, generoso. Úsala en tres situaciones distintas: 1) en una conversación con un amigo, 2) con un adulto de tu casa y 3) en un cuento corto de dos frases que tú inventes. Dilas en voz alta y pide a un adulto que diga si el significado se mantuvo.",
     "Palabra: refugio. 1) A un amigo: mi cuarto es mi refugio. 2) A mi mamá: el techo del patio es un refugio de la lluvia. 3) Cuento: El conejo corrió hacia su madriguera. Era un refugio seguro. El adulto dijo que el significado se mantuvo.",
     ["usa la palabra en tres situaciones", "mantiene el significado", "adapta la frase"], ["tres frases dichas y escritas"], ["cambiar el significado", "repetir la misma frase"],
     "Si repite la misma frase, pide que cambie el lugar y la persona y la diga otra vez."),
    "Usa hoy tu palabra nueva en un lugar distinto de tu casa.",
    "Explica una palabra nueva a un compañero y pídele que la use en una frase.",
)
