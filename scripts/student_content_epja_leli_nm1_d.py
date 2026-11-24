"""Lengua y Literatura EPJA Media Nivel 1, módulo 4 (parte 1): OAD-13, leer y analizar dos obras literarias con relación de intertextualidad (personajes, temas y símbolos). Los resúmenes de obras clásicas son propios y los textos nuevos son inventados."""
from __future__ import annotations

from epja_leli_nm1_d_common import build

O = "EPJA-LELI-NM1-OAD-13"

F1 = ("Texto 1 (inventado), un jefe de turno a su cuadrilla: «Hoy peleamos contra molinos de viento: el informe de ayer sigue sin corregirse y nadie lo lee». "
      "Texto 2 (inventado), relato breve: Tras tres años trabajando en el sur, Raúl volvió a su casa. Nadie lo reconoció al principio, salvo el perro viejo, que movió la cola y se echó a sus pies. "
      "Texto 3 (inventado), aviso: Se vende carro de arrastre, buen estado, precio conversable. "
      "Texto 4 (inventado), conversación: —No toques esa carpeta, es la caja de Pandora de esta oficina. —¿Y qué tiene adentro? —Todos los reclamos de los últimos dos años. "
      "Datos de apoyo (resúmenes propios de la clase): en Don Quijote de la Mancha, de Cervantes, un hombre que leyó muchos libros de aventuras ataca unos molinos de viento creyendo que son gigantes. "
      "En la Odisea, de Homero, Ulises vuelve a su isla tras años de viaje y su viejo perro es el primero en reconocerlo. "
      "En un relato griego antiguo, Pandora abre una vasija (llamada después caja) y salen al mundo muchos males.")

F2 = ("Texto A (inventado), carta de una vecina: «Querida Rosa: como dice el refrán, «a quien madruga, Dios lo ayuda». Por eso te escribo temprano». "
      "Texto B (inventado), crónica del barrio: Don Aldo repartió pan toda la noche y volvió a su casa recién en la mañana. Nadie lo esperaba, y su regreso bajo el temporal fue una verdadera odisea. "
      "Texto C (inventado), relato: en un pueblo del norte, Inés teje de día un chal para su hermano, que está en el mar; cada noche deshace una parte, porque dice que todavía no es hora de entregarlo. "
      "Datos de apoyo: una cita copia palabras de otro texto, entre comillas y diciendo de dónde vienen. Una alusión menciona de paso un personaje, una historia o una frase de otra obra. "
      "Una reescritura cuenta de nuevo una historia conocida con otra época, otro lugar u otros personajes. "
      "En la Odisea, de Homero, Penélope espera a Ulises y de noche deshace la tela que teje de día. Odisea, como palabra común, significa viaje largo y lleno de dificultades. "
      "En un mito griego, el Minotauro es un monstruo encerrado en un laberinto.")

F3 = ("Texto base (resumen propio), la Odisea, de Homero: Ulises, rey de la isla de Ítaca, tarda muchos años en volver a casa después de la guerra de Troya. "
      "Su esposa, Penélope, lo espera. Muchos hombres le piden matrimonio y ella responde que decidirá cuando termine de tejer una tela, pero cada noche deshace lo tejido. "
      "Su hijo, Telémaco, sale a buscar noticias de su padre. "
      "Texto nuevo (inventado), «La espera de Marta»: Hugo, el esposo de Marta, partió a trabajar a una faena del sur y no ha vuelto en dos años. Marta teje un chaleco para él. "
      "Don Aníbal, un vecino, la visita cada semana y le dice que Hugo no regresará. Marta responde que lo terminará cuando llegue el invierno, pero cada noche suelta unas vueltas del chaleco. "
      "Su hijo Nico escribe cartas a distintas oficinas para saber algo de su padre. El texto no cuenta si Hugo vuelve.")

F4 = ("Texto base (resumen propio), Don Quijote de la Mancha, de Miguel de Cervantes: Alonso Quijano lee tantos libros de caballerías que decide hacerse caballero y se hace llamar don Quijote. "
      "Sale con su escudero, Sancho Panza, un campesino práctico. Don Quijote ve unos molinos de viento y cree que son gigantes; Sancho le advierte que son molinos, pero igual los ataca. "
      "Texto nuevo (inventado), «Don Eliseo y los casos»: Eliseo es guardia nocturno en un edificio y lee cada noche novelas policiales. Una madrugada ve a un vecino sacar una caja y decide que es un ladrón. "
      "Lo sigue con una linterna. Su compañero de turno, Pedro, le dice que es el panadero que lleva su pedido. Eliseo insiste, hasta que el panadero lo saluda y le regala un pan. "
      "Eliseo se ríe, pero a la noche siguiente vuelve a su novela.")

F5 = ("Texto base (resumen propio), mito griego del Minotauro: un monstruo vive en un laberinto en la isla de Creta. El héroe Teseo entra a enfrentarlo. "
      "Ariadna le entrega un hilo que él va soltando al avanzar, y así puede volver a la salida. "
      "Texto nuevo (inventado), «El pasillo amarillo»: Rosa llega a un hospital grande para entregar unos papeles en la oficina de exámenes. Los pasillos se parecen todos y se pierde dos veces. "
      "Una funcionaria le muestra una línea amarilla pintada en el piso y le dice: «Sígala y llegará a la oficina». Rosa la sigue por tres pasillos y llega. "
      "Al volver, descubre en cada esquina una flecha amarilla que antes no había visto.")

F6 = ("Texto base (resumen propio), la Odisea, de Homero: Ulises, rey de Ítaca, vuelve a casa después de años de viaje y de pruebas en el mar. Su viejo perro lo reconoce antes que nadie. "
      "Penélope, su esposa, lo espera y cuida la casa. "
      "Texto 1 (inventado), «Calle 5»: vivo en un edificio llamado Ítaca, que eligió una inmobiliaria sin ninguna razón. Mi vecino se llama Ulises y es contador. Cada día saluda en el ascensor y entra a su departamento. "
      "Texto 2 (inventado), «El regreso de Nelly»: Nelly, camionera, vuelve a su barrio después de tres años de rutas lejanas. En el camino sufrió un temporal y un cierre de ruta que la obligaron a dar un largo rodeo. "
      "Al llegar nadie la reconoce, salvo su perro, que ladra de alegría. Su hermana, que cuidó la casa, abre la puerta.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco que ya conozco historias antiguas por lo que se dice a diario y descubro qué es la intertextualidad.",
    prior=["Escucho refranes y expresiones en el trabajo y en la casa.", "Sé que un texto puede recordar a otro.", "Puedo contar con mis palabras una historia que conozco."],
    explain=[
        "Tú ya usas la intertextualidad aunque no conozcas la palabra. Cuando alguien dice «estamos peleando contra molinos de viento», llama a otra historia: la del Quijote. La intertextualidad es la relación que un texto tiene con otros textos: los recuerda, los nombra o los transforma.",
        "Esa relación puede hacerse con personajes (alguien «es un Quijote»), con temas (el regreso a casa tras un largo viaje) o con símbolos (una caja que guarda problemas). Para entender la mención hay que conocer la obra de la que viene o averiguar de qué trata.",
        "Los textos clásicos son obras muy antiguas que se siguen leyendo y recordando. Por eso aparecen en conversaciones, noticias y canciones. Hoy partimos de lo que ya sabes: expresiones de la vida diaria que vienen de historias conocidas.",
    ],
    vocab=[("intertextualidad", "relación de un texto con otros textos que recuerda, cita o transforma"), ("texto clásico", "obra antigua que se sigue leyendo y recordando"), ("alusión", "mención breve de un personaje, historia o frase de otra obra"), ("expresión", "frase hecha que usamos al hablar")],
    worked=[
        ("Reconocer una alusión", "Frase (inventada): «Esta bodega es el laberinto del Minotauro: nadie encuentra nada». Dato de apoyo: el Minotauro vive en un laberinto, en un mito griego.", ["Busco un nombre de otra historia: Minotauro.", "Pregunto qué rasgo se usa: el laberinto, donde uno se pierde.", "Lo aplico: la bodega es confusa."], "Alude al mito del Minotauro para decir que la bodega es confusa"),
        ("Distinguir un texto sin alusión", "Aviso (inventado): «Cambio de horario: la oficina atiende desde las nueve».", ["No nombra ningún personaje ni historia conocida.", "Solo da una información."], "No hay intertextualidad: informa sin recordar otra obra"),
    ],
    mistakes=[("Pensar que alguien debe copiar un texto entero para relacionarse con él.", "Una alusión puede ser una sola palabra o un nombre.", "Busca nombres, imágenes o frases conocidas de otras historias."),
              ("Creer que si no conozco la obra, la frase no significa nada.", "La frase se entiende mejor si averiguas de qué obra viene.", "Pregunta o lee un resumen breve de la obra.")],
    T=[
        ("abc", "{F} ¿Cuál de los textos NO recuerda a ninguna otra historia?", "El Texto 3, el aviso del carro de arrastre", "El Texto 1, el del informe", "El Texto 4, el de la carpeta", "El aviso solo informa de una venta y no menciona otra historia."),
        ("ab", "{F} ¿A qué obra alude la expresión «molinos de viento» del Texto 1?", "Don Quijote de la Mancha, de Cervantes", "La Odisea, de Homero", "Los datos de apoyo asocian los molinos con el Quijote."),
        ("{F} ¿Cuántos de los cuatro textos aluden a otra historia? Escribe el número.", "3", "Aluden los Textos 1, 2 y 4; el aviso del Texto 3 no."),
        ("abc", "En Lengua y Literatura: ¿qué es la intertextualidad?", "La relación de un texto con otros que recuerda o transforma", "Un texto escrito solo con refranes populares conocidos", "La cantidad de páginas que suman dos obras seguidas", "Es la relación entre textos; no depende del largo ni de usar refranes."),
        ("ab", "{F} ¿Qué personaje de la Odisea recuerda Raúl en el Texto 2?", "Ulises, que vuelve tras años de ausencia", "Un caballero que ataca molinos", "El Texto 2 habla de un regreso largo y de un perro que reconoce a quien vuelve."),
        ("abc", "{F} En el Texto 4, ¿qué representa la «caja de Pandora» de la oficina?", "Un lugar que guarda muchos problemas", "Un regalo para el personal", "Un mueble muy caro", "Según los datos de apoyo, al abrirla salen males: aquí, los reclamos acumulados."),
        ("abc", "Una vecina dice: «Mi hermano es un Quijote: se pasa peleando contra cosas que no tienen arreglo». ¿Qué rasgo del personaje usa?", "Que pelea contra enemigos que no son reales", "Que viaja años lejos de casa", "Que guarda males en una caja", "El Quijote ataca molinos creyendo que son gigantes, y ese rasgo se usa en la comparación."),
        ("abc", "¿Qué señal en un texto indica que puede haber una alusión a otra obra?", "Nombra un personaje o una imagen muy conocidos de otra historia", "Tiene muchos números de teléfono", "Está escrito con letra pequeña", "Las alusiones suelen mencionar un nombre o una imagen de otra historia."),
        ("ab", "{F} Marcela dice que la «caja de Pandora» es una cita de la Odisea. ¿Tiene razón?", "No: viene de otro relato griego, el de Pandora", "Sí: toda la mitología está en la Odisea", "Los datos de apoyo ubican la caja en el relato de Pandora, no en la Odisea."),
        ("{F} Escribe en una palabra el animal que reconoce a Raúl en el Texto 2.", "perro", "El Texto 2 dice que el perro viejo lo reconoció."),
        ("abc", "Si no conoces la obra a la que alude un texto, ¿qué puedes hacer?", "Preguntar a otra persona o leer un resumen de la obra", "Suponer que el texto no dice nada", "Cambiar el final del texto", "Para entender una alusión conviene averiguar de qué obra viene."),
        ("abc", "{F} ¿Qué tienen en común los Textos 1 y 4?", "Ambos usan una expresión que viene de una historia conocida", "Ambos son avisos de venta", "Ambos hablan de un perro", "Los dos recuerdan historias conocidas: el Quijote y Pandora."),
        ("ab", "{F} ¿El Texto 2 copia toda la Odisea?", "No: es un relato nuevo que solo recuerda un momento del regreso", "Sí: cuenta todo el viaje de Ulises", "Cuenta a Raúl, un personaje distinto, y solo recuerda un episodio."),
    ],
    ctx=("abc", "Alguien comenta: «Llegar hoy fue una odisea: dos horas de bus bajo la lluvia». ¿Qué quiere decir con «odisea»?", "Que fue un viaje largo y lleno de dificultades", "Que viajó en barco por el mar", "Que leyó un libro en el bus", "La palabra odisea nombra un viaje largo y difícil, recordando la obra de Homero."),
    sc=[("En Lengua y Literatura: ¿qué es una alusión?", "Una mención breve de un personaje, historia o frase de otra obra", "La alusión no copia la obra: la recuerda con un nombre o una imagen."),
        ("¿Dónde puede aparecer la intertextualidad?", "En personajes, temas y símbolos", "Un texto puede relacionarse con otro por quién actúa, de qué trata o qué imagen usa."),
        ("¿Qué haces si no conoces la obra aludida?", "Averiguo de qué trata", "Entender la alusión exige conocer al menos un resumen de la obra.")],
    op=("Elige UNO de los Textos 1, 2 o 4 de esta ficha y explica en tres oraciones: a qué obra o historia alude, qué se parece y qué cambia. {F}",
        "Texto 2: alude a la Odisea porque Raúl vuelve tras años y solo el perro lo reconoce. Se parece en el regreso largo y en el perro. Cambia que Raúl vuelve de un trabajo en el sur, no de un viaje por el mar.",
        ["nombra la obra aludida", "dice qué se parece con datos de los textos", "dice qué cambia"],
        ["tres oraciones escritas"],
        ["decir solo «se parece» sin dato", "copiar el texto entero"],
        "Pregunta: «¿Qué palabra o imagen del texto te hizo pensar en la otra historia?»."),
    reinforce="Anota dos expresiones que escuches esta semana que vengan de una historia, un cuento o una canción, y di de cuál.",
    extend="Averigua con alguien cercano qué cuentos o refranes antiguos se usan para hablar de esperar, de volver o de perderse, y anótalos.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo el vocabulario de la intertextualidad: cita, alusión, reescritura, personaje, tema y símbolo.",
    prior=["Sé que un texto puede recordar a otro.", "Reconozco una expresión que viene de una historia.", "Distingo qué cuenta un texto y cómo lo cuenta."],
    explain=[
        "Un texto puede relacionarse con otro de tres formas. En la cita copia palabras de otra obra, entre comillas y con la fuente. En la alusión menciona de paso un personaje, una historia o una frase. En la reescritura cuenta de nuevo una historia conocida, cambiando la época, el lugar o los personajes.",
        "Para analizar la relación miramos tres cosas. Los personajes: quién actúa y qué papel cumple. El tema: la idea central sobre la vida, como la espera, la ambición o el regreso. El símbolo: un objeto o imagen que representa algo más amplio, como un laberinto que representa perderse.",
        "Al comparar dos textos no basta decir que se parecen. Hay que señalar en qué: qué personaje recuerda a cuál, qué tema comparten y qué objeto se repite. También se debe decir qué cambia, porque ahí aparece la voz propia del texto nuevo.",
    ],
    vocab=[("cita", "palabras de otro texto, entre comillas y con la fuente"), ("reescritura", "historia conocida contada de nuevo con otra época, lugar o personajes"), ("tema", "idea central sobre la vida que trata una obra"), ("símbolo", "objeto o imagen que representa una idea más amplia")],
    worked=[
        ("Clasificar un recurso", "Frase (inventada): «Mi tía es una Penélope: espera cada noche la llamada de su hijo». Dato de apoyo: Penélope espera a Ulises durante años.", ["Menciona de paso a un personaje: Penélope.", "No copia palabras entre comillas ni cuenta otra vez la historia."], "Es una alusión a un personaje"),
        ("Distinguir tema y símbolo", "Relato (inventado): una mujer teje un chal que nunca termina mientras espera a su hermano.", ["El tema es la espera de alguien que está lejos.", "El símbolo es el chal que se teje y no se termina."], "Tema: la espera; símbolo: el tejido"),
    ],
    mistakes=[("Llamar cita a cualquier parecido con otra obra.", "La cita exige copiar palabras con comillas y con su fuente.", "Si solo se menciona un nombre o una idea, es una alusión."),
              ("Confundir tema con símbolo.", "El tema es una idea; el símbolo es un objeto o imagen que la representa.", "Pregunta: «¿esto es una idea o algo que se puede ver?».")],
    T=[
        ("abc", "{F} ¿Qué recurso usa el Texto A cuando pone «a quien madruga, Dios lo ayuda» entre comillas y dice «como dice el refrán»?", "Una cita", "Una reescritura", "Un símbolo", "Copia palabras entre comillas y dice de dónde vienen: es una cita."),
        ("abc", "{F} ¿Qué recurso usa el Texto B al decir que el regreso de don Aldo «fue una verdadera odisea»?", "Una alusión", "Una cita", "Una reescritura completa", "Menciona de paso una obra para decir que el regreso fue largo y difícil."),
        ("abc", "{F} ¿Qué recurso usa el Texto C?", "Una reescritura de la historia de Penélope", "Una cita de Homero", "Un aviso informativo", "Cuenta de nuevo la espera de Penélope en un pueblo del norte, con otros personajes."),
        ("{F} ¿Cuántas veces nombra el Texto C a Penélope? Escribe el número.", "0", "El Texto C nunca dice su nombre: la relación se descubre por la historia."),
        ("ab", "En Lengua y Literatura: ¿qué diferencia hay entre citar y aludir?", "Citar copia palabras con comillas; aludir solo menciona de paso", "Citar es inventar; aludir es copiar", "La cita lleva comillas y fuente; la alusión puede ser una mención breve sin copiar."),
        ("abc", "En Lengua y Literatura: ¿qué es una reescritura?", "Una historia conocida contada de nuevo en otra época o lugar", "Un refrán puesto entre comillas", "El resumen de una obra en tres líneas", "La reescritura transforma una historia conocida cambiando época, lugar o personajes."),
        ("abc", "Alguien escribe: «Como Penélope, esperó a que sonara el teléfono». ¿Qué recurso es?", "Una alusión a un personaje", "Una cita textual de Homero", "Un tema", "Nombra a Penélope de paso para hablar de la espera."),
        ("abc", "Una obra nueva cuenta el regreso de Ulises, pero en una ciudad moderna y con una camionera como protagonista. ¿Qué es?", "Una reescritura", "Una cita", "Un aviso", "Cambia el lugar y los personajes de una historia conocida: es una reescritura."),
        ("abc", "{F} ¿Qué parte del Texto C permite relacionarlo con la Odisea?", "Una mujer teje de día y deshace de noche mientras espera", "Que ocurre en un pueblo del norte", "Que su hermano está en el mar", "El gesto de tejer y deshacer repite el de Penélope; el lugar y el mar solo son escenario."),
        ("ab", "{F} Un compañero dice que el Texto B es una reescritura de la Odisea. ¿Tiene razón?", "No: solo usa la palabra «odisea» como alusión a un viaje difícil", "Sí: cuenta todo el viaje de Ulises", "El texto no cuenta la historia de Ulises, solo toma una palabra de ella."),
        ("abc", "¿Cuál de estas frases alude a un personaje o historia de otra obra?", "«Con ese plan, eres un Quijote contra la municipalidad»", "«Compré pan y leche esta mañana»", "«Llegué a las ocho al trabajo»", "Solo la primera nombra a un personaje conocido para dar una idea."),
        ("abc", "Si copias una frase de un libro entre comillas y dices de qué libro viene, ¿qué recurso usas?", "Una cita", "Una alusión", "Una reescritura", "Copiar palabras con comillas y fuente es citar."),
        ("ab", "{F} ¿Qué texto cambia el lugar de una historia conocida?", "El Texto C, que lleva la espera de Penélope a un pueblo del norte", "El Texto A, que habla de un refrán", "El Texto C traslada la historia; el Texto A solo cita un refrán."),
    ],
    ctx=("abc", "Un compañero dice: «Esta sala de archivos es el laberinto del Minotauro». ¿Qué recurso usa y qué quiere decir?", "Una alusión: que en esa sala es fácil perderse", "Una cita: que copió una frase de un libro", "Una reescritura: que contó de nuevo el mito completo", "Nombra de paso un laberinto conocido para decir que el lugar confunde."),
    sc=[("En Lengua y Literatura: ¿qué es un símbolo?", "Un objeto o imagen que representa una idea más amplia", "El símbolo se ve en el texto y significa algo más."),
        ("¿Qué recurso copia palabras de otro texto con comillas?", "La cita", "La cita copia con comillas y con la fuente."),
        ("¿Qué tres cosas miramos al comparar dos obras?", "Personajes, tema y símbolo", "Son los puntos de contacto entre un texto y otro.")],
    op=("Lee la ficha y escribe en tu cuaderno una tabla de tres filas (cita, alusión, reescritura) con un ejemplo de la ficha para cada una y una frase que explique por qué. {F}",
        "Cita: Texto A, copia el refrán entre comillas. Alusión: Texto B, nombra la odisea de paso. Reescritura: Texto C, cuenta de nuevo la espera de Penélope en otro lugar.",
        ["tres filas con ejemplos distintos de la ficha", "cada ejemplo con una explicación breve", "no mezcla los recursos"],
        ["una tabla de tres filas"],
        ["usar el mismo texto para dos recursos", "no explicar por qué"],
        "Pregunta: «¿Copia palabras, menciona de paso o cuenta de nuevo la historia?»."),
    reinforce="Escribe una frase tuya que contenga una alusión a un personaje de un cuento que conozcas.",
    extend="Busca en tu memoria un refrán y explica si lo usas como cita o si solo lo recuerdas.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy comparo paso a paso dos obras que se relacionan: la Odisea y un relato nuevo.",
    prior=["Reconozco cita, alusión y reescritura.", "Sé qué es un personaje y un tema.", "Puedo hacer una tabla simple."],
    explain=[
        "Para analizar la relación entre dos obras sigue cinco pasos. Paso 1: lee los dos textos completos. Paso 2: anota los personajes y qué papel cumple cada uno. Paso 3: anota el tema y los símbolos. Paso 4: pon lado a lado lo que se parece y lo que cambia. Paso 5: escribe qué relación hay.",
        "Un papel es la función que cumple un personaje. En la Odisea, Penélope es quien espera; en «La espera de Marta» ese papel lo cumple Marta. No hace falta que el nombre ni la época coincidan: importa la función que cumple en la historia.",
        "Lo que cambia es tan importante como lo que se parece. Si el texto nuevo cambia el lugar, la época o el final, ahí está su mirada propia. Analizar es mostrar ambas cosas con datos de los textos, no solo decir que se parecen.",
    ],
    vocab=[("papel del personaje", "función que cumple un personaje en la historia"), ("ausente", "persona que no está presente"), ("tela", "tejido que se hace con hilos"), ("comparar", "poner dos cosas lado a lado para ver qué se parece y qué cambia")],
    worked=[
        ("Poner los papeles lado a lado", "Texto base: Penélope espera. Texto nuevo: Marta espera.", ["Papel en la Odisea: quien espera.", "Papel en el texto nuevo: quien espera.", "Coinciden en el papel; cambian el nombre, la época y la tarea que hacen."], "Marta cumple el papel de Penélope"),
        ("Ver qué cambia", "Odisea: la tela se teje de día y se deshace de noche. Texto nuevo: un chaleco se teje y se sueltan vueltas por la noche.", ["Se repite el gesto de tejer y deshacer.", "Cambia el objeto: una tela se vuelve un chaleco para Hugo."], "Se repite el gesto y cambia el objeto"),
    ],
    mistakes=[("Decir que dos personajes son iguales solo porque se llaman parecido o hacen lo mismo una vez.", "Se comparan por el papel que cumplen en toda la historia.", "Explica qué función cumple cada uno con datos del texto."),
              ("Contar solo lo que se parece.", "Un análisis también muestra lo que cambia.", "Agrega al menos una diferencia con datos de los textos.")],
    T=[
        ("abc", "{F} ¿Con qué personaje de la Odisea se relaciona Marta?", "Con Penélope, la esposa que espera", "Con Telémaco, el hijo", "Con Ulises, el que viaja", "Marta espera al esposo que está lejos, igual que Penélope."),
        ("abc", "{F} ¿Quién cumple en «La espera de Marta» el papel de Ulises?", "Hugo, el esposo que está lejos", "Don Aníbal, el vecino", "Nico, el hijo", "Hugo es quien partió y todos esperan, como Ulises."),
        ("{F} ¿Cuántos años lleva ausente Hugo? Escribe el número.", "2", "El texto nuevo dice que no ha vuelto en dos años."),
        ("abc", "{F} ¿Qué personaje del texto nuevo se parece a Telémaco?", "Nico, que escribe cartas para saber de su padre", "Marta, que teje el chaleco", "Don Aníbal, que visita cada semana", "Telémaco busca noticias de su padre y Nico hace algo parecido."),
        ("ab", "{F} ¿Qué objeto se repite en ambos textos?", "Algo que se teje y se deshace", "Una isla", "Penélope deshace la tela y Marta suelta vueltas del chaleco."),
        ("abc", "{F} ¿Qué tema une los dos textos?", "La espera de alguien que está lejos", "El éxito en el trabajo", "La ambición de poder", "En ambos hay una persona que espera un regreso."),
        ("abc", "{F} ¿Con quiénes de la Odisea se parece don Aníbal?", "Con los hombres que presionan a Penélope para que deje de esperar", "Con Telémaco", "Con Ulises", "Don Aníbal insiste en que Marta deje de esperar, igual que los pretendientes."),
        ("abc", "{F} ¿Cuál es una diferencia entre los dos textos?", "En la Odisea son muchos hombres los que presionan; en el texto nuevo, solo un vecino", "En ambos hay una isla", "En ambos el esposo ya regresó", "El resumen habla de muchos pretendientes y el texto nuevo de un solo vecino."),
        ("abc", "En Lengua y Literatura: en el análisis de dos obras, ¿qué paso va entre anotar los personajes y comparar?", "Anotar el tema y los símbolos", "Escribir el final", "Elegir el título", "Los pasos 2 y 3 reúnen los datos que se comparan en el paso 4."),
        ("ab", "Beto dice: «Marta es una copia de Penélope». ¿Qué respuesta es más precisa?", "Marta repite el papel de quien espera, pero es un personaje nuevo en otra situación", "Marta es Penélope con otro nombre y nada cambia", "Marta tiene hijo y vecino propios y cambia la época, por eso no es una copia."),
        ("abc", "{F} Marta suelta vueltas del chaleco cada noche. ¿Qué puede significar este gesto al relacionarlo con la Odisea?", "Que gana tiempo para no renunciar a la espera", "Que ya no quiere a su esposo", "Que no sabe tejer", "En la Odisea deshacer la tela es una forma de seguir esperando."),
        ("abc", "{F} En la Odisea la espera termina cuando Ulises regresa. ¿Cómo queda la espera en el texto nuevo?", "Sin terminar: el texto no cuenta si Hugo vuelve", "Termina porque Hugo regresa en invierno", "Termina porque Marta olvida a Hugo", "El texto aclara que no cuenta si Hugo vuelve."),
        ("ab", "{F} ¿Qué cambia más entre los dos textos?", "El lugar y la época: de una isla antigua a una faena del sur", "El tema de la espera", "Ambos se centran en la espera; lo que cambia es dónde y cuándo ocurre."),
    ],
    ctx=("abc", "En el club de lectura de tu barrio proponen comparar la Odisea con «La espera de Marta». ¿Qué conviene hacer primero?", "Leer los dos textos completos", "Escribir la conclusión final", "Elegir cuál es mejor", "El análisis parte por leer los dos textos antes de anotar o concluir."),
    sc=[("¿Cuántos pasos tiene el análisis de dos obras?", "Cinco", "Leer, anotar personajes, anotar tema y símbolos, comparar y escribir la relación."),
        ("En Lengua y Literatura: ¿qué es el papel de un personaje?", "La función que cumple en la historia", "Dos personajes se comparan por la función que cumplen."),
        ("¿Qué muestra un buen análisis además de lo que se parece?", "Lo que cambia", "El texto nuevo se entiende mejor al ver qué cambia.")],
    op=("Haz en tu cuaderno una tabla de tres columnas (Odisea, «La espera de Marta», qué cambia) y cuatro filas (esposo ausente, quien espera, quien presiona, hijo). Llénala con datos de la ficha y escribe una oración que diga qué relación hay. {F}",
        "Esposo ausente: Ulises; Hugo; el motivo del viaje. Quien espera: Penélope; Marta; el objeto que teje. Quien presiona: varios hombres; don Aníbal; la cantidad. Hijo: Telémaco; Nico; cómo busca noticias. Relación: el texto nuevo repite los papeles de la Odisea en otra época.",
        ["tabla de 4 filas con datos correctos", "tres columnas completas", "una oración que dice la relación"],
        ["una tabla y una oración"],
        ["mezclar datos de los dos textos", "no indicar qué cambia"],
        "Pregunta: «¿Qué dato del texto nuevo apoya cada fila?»."),
    reinforce="Elige una historia que conozcas, como un cuento familiar o una película, y di qué personaje espera, cuál se va y cuál presiona.",
    extend="Reescribe en tres oraciones el pasaje de Marta, pero con un final en que Hugo vuelve, y di qué papel cambia.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo el análisis de otro par de obras: el Quijote y un relato nuevo sobre alguien que confunde lo que lee con la realidad.",
    prior=["Sé comparar personajes, tema y símbolo.", "Reconozco el papel de un personaje.", "Distingo lo que se parece de lo que cambia."],
    explain=[
        "Practicamos el método con otro par de obras. En el Quijote, un hombre que lee muchos libros de caballerías cree vivir una aventura de caballero y ve gigantes donde hay molinos. Su escudero Sancho Panza mira las cosas con sentido práctico.",
        "En «Don Eliseo y los casos», un guardia nocturno que lee novelas policiales ve crímenes donde no los hay. Hay un personaje práctico, Pedro, que le muestra la realidad. Los papeles se repiten: quien confunde la ficción con la vida y quien lo trae de vuelta.",
        "Para que tu análisis sea sólido, cada parecido debe apoyarse en un dato del texto y cada diferencia también. Fíjate en el tema: lo que ambas obras dicen sobre la lectura y la realidad, sin exagerar ni inventar lo que los textos no cuentan.",
    ],
    vocab=[("escudero", "ayudante que acompaña a un caballero"), ("realista", "persona que mira las cosas como son"), ("confundir", "tomar una cosa por otra"), ("ficción", "historia inventada")],
    worked=[
        ("Buscar el papel práctico", "Quijote: Sancho advierte que son molinos. Texto nuevo: Pedro advierte que es el panadero.", ["Ambos avisan de la realidad.", "Ambos acompañan a quien se equivoca.", "El papel es el de la mirada práctica."], "Pedro cumple el papel de Sancho Panza"),
        ("Decir qué cambia", "Quijote: ataca los molinos igual. Eliseo: se ríe cuando el panadero lo saluda.", ["Ambos insisten antes de reconocer algo.", "Eliseo termina riéndose del error; el resumen del Quijote no dice eso."], "En el texto nuevo el error se resuelve con humor"),
    ],
    mistakes=[("Decir que Eliseo y don Quijote son lo mismo.", "Se parecen en un rasgo, pero viven situaciones distintas.", "Nombra el rasgo que comparten y lo que los diferencia."),
              ("Afirmar algo del texto que no cuenta.", "Un análisis solo puede usar lo que el texto dice o muestra.", "Cita el dato del texto que apoya cada afirmación.")],
    T=[
        ("abc", "{F} ¿Qué personaje del Quijote se parece a Eliseo?", "Don Quijote, que confunde lo que lee con la realidad", "Sancho Panza, el escudero práctico", "Un molino de viento", "Eliseo lee novelas y ve un crimen donde no lo hay, como don Quijote ve gigantes."),
        ("abc", "{F} ¿Quién cumple en el texto nuevo el papel de Sancho Panza?", "Pedro, el compañero de turno", "El panadero", "Eliseo", "Pedro advierte de la realidad, como Sancho."),
        ("{F} ¿Con qué objeto sale Eliseo a seguir al vecino? Escribe una palabra.", "linterna", "El texto dice que lo sigue con una linterna."),
        ("abc", "{F} ¿Qué tema une ambos textos?", "La confusión entre lo que se lee y la realidad", "La espera de un regreso", "El miedo a los monstruos", "Los dos personajes toman por real algo que viene de sus lecturas."),
        ("ab", "{F} ¿Qué equivale a los molinos de viento en el texto nuevo?", "El vecino panadero, a quien Eliseo toma por ladrón", "La linterna del guardia", "Los molinos son lo que el personaje interpreta mal; en el texto nuevo es el vecino que lleva su pedido."),
        ("abc", "{F} ¿Qué lectura provoca la confusión de cada personaje?", "Libros de caballerías en el Quijote y novelas policiales en el texto nuevo", "Libros de cocina en ambos", "Cartas en el Quijote y avisos en el texto nuevo", "Cada personaje se confunde por el tipo de libros que lee."),
        ("abc", "¿Qué función cumplen Sancho y Pedro en sus historias?", "Mostrar una mirada realista frente a la fantasía", "Atacar a los gigantes", "Escribir las novelas", "Ambos advierten lo que realmente se ve."),
        ("abc", "{F} ¿Qué dato confirma que Pedro tenía razón sobre el vecino?", "El panadero saluda a Eliseo y le regala un pan", "Eliseo vuelve a su novela", "Eliseo lo sigue con linterna", "El saludo y el pan muestran que no era un ladrón."),
        ("abc", "{F} Una reseña dice: «Eliseo es un Quijote de edificio». ¿Qué recurso intertextual usa?", "Una alusión a un personaje", "Una cita textual", "Una reescritura completa", "Nombra de paso al Quijote para describir a Eliseo."),
        ("{F} ¿Cuántos personajes con nombre propio actúan en el texto nuevo? Escribe el número.", "2", "Actúan Eliseo y Pedro; el panadero y el vecino no tienen nombre."),
        ("abc", "{F} Según ambos textos, ¿qué idea sobre leer es más razonable?", "El problema no es leer, sino no distinguir la ficción de la realidad", "Leer siempre hace daño", "Nadie debería leer novelas", "Los dos personajes se equivocan al confundir, no por el hecho de leer."),
        ("ab", "{F} Después del error, ¿qué hace Eliseo?", "Se ríe, pero esa noche vuelve a leer", "Deja de leer para siempre", "El texto dice que se ríe y vuelve a su novela la noche siguiente."),
        ("abc", "{F} ¿Qué diferencia hay entre los lugares de ambas historias?", "Unos molinos de viento frente a un edificio de noche", "Ambas ocurren en un edificio", "Ambas ocurren en el mar", "El resumen habla de molinos de viento y el texto nuevo de un edificio de noche."),
    ],
    ctx=("abc", "En el club de lectura alguien dice que Eliseo y don Quijote «son lo mismo». ¿Qué respuesta es más precisa?", "Se parecen en confundir ficción y realidad, pero viven situaciones distintas", "Son lo mismo porque ambos leen", "No se parecen en nada", "Un buen análisis nombra el rasgo común y también lo que cambia."),
    sc=[("En Lengua y Literatura: ¿qué papel cumple Sancho Panza?", "El del escudero que mira las cosas con sentido práctico", "Sancho advierte que lo que se ve son molinos."),
        ("¿Qué tema comparten el Quijote y el texto nuevo?", "Confundir lo que se lee con la realidad", "Ambos personajes se equivocan por sus lecturas."),
        ("¿Cómo apoyas una afirmación en un análisis?", "Con un dato del texto", "Sin dato del texto, la afirmación es solo una opinión.")],
    op=("Escribe en tu cuaderno cinco oraciones que digan qué relación hay entre el Quijote y «Don Eliseo y los casos»: dos parecidos, una diferencia y qué piensas del tema, cada una con un dato de la ficha. {F}",
        "Se parecen porque Eliseo y don Quijote creen real lo que leen. También porque Pedro y Sancho advierten la verdad. Cambia que Eliseo se ríe de su error. Creo que los textos muestran que leer es bueno si distingues la ficción. Se ve cuando Pedro le muestra al panadero.",
        ["dos parecidos con datos", "una diferencia con dato", "una opinión sobre el tema apoyada en el texto"],
        ["cinco oraciones escritas"],
        ["no dar datos del texto", "decir que son iguales"],
        "Pregunta: «¿Qué frase del texto apoya tu opinión?»."),
    reinforce="Piensa en alguien que conozcas que tomó por verdad algo que vio en una historia y explica en una oración qué papel cumpliría en una obra.",
    extend="Escribe cuatro oraciones sobre un tercer personaje que pide ayuda a Pedro, y di qué papel cumple.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a los símbolos: sigo un laberinto y un hilo en un mito y en una situación de hospital.",
    prior=["Sé qué es un símbolo.", "Analizo personajes y temas.", "Distingo lo que se parece de lo que cambia."],
    explain=[
        "Un símbolo es un objeto, lugar o imagen que representa una idea más amplia. El laberinto es un lugar donde uno se pierde, y por eso se usa para hablar de situaciones confusas, como un trámite o una ciudad. El hilo que ayuda a salir representa la guía para no perderse.",
        "Un símbolo no siempre significa lo mismo. Su sentido depende del texto: un hilo puede ser guía en un relato y unión entre personas en otro. Por eso no basta con decir «es un símbolo»: debes explicar qué representa en esa obra y con qué dato del texto lo ves.",
        "En esta clase relacionamos el mito del Minotauro con una situación de la vida actual: una persona que se pierde en un hospital grande y una línea amarilla que la guía. Aplicamos así el análisis a un tema de la vida diaria: orientarse en trámites y lugares confusos.",
    ],
    vocab=[("laberinto", "lugar con muchos caminos donde es fácil perderse"), ("guía", "persona o señal que indica el camino"), ("orientarse", "encontrar el camino o la dirección"), ("representar", "estar en el lugar de otra cosa o idea")],
    worked=[
        ("Buscar el símbolo que se repite", "Mito: laberinto e hilo. Texto nuevo: pasillos parecidos y línea amarilla.", ["Laberinto: lugar donde uno se pierde; en el hospital, los pasillos iguales.", "Hilo: guía para volver; en el hospital, la línea amarilla."], "Se repite el símbolo de perderse y de la guía que ayuda"),
        ("Explicar qué cambia", "Hilo: lo suelta Teseo al avanzar. Línea: ya está pintada en el piso.", ["El hilo se suelta mientras se avanza.", "La línea es una señal fija que alguien más preparó."], "Cambia quién pone la guía"),
    ],
    mistakes=[("Decir que un símbolo siempre significa lo mismo.", "Su sentido depende de la obra y de cómo se usa.", "Explica qué representa en este texto con un dato."),
              ("Decir que la línea amarilla «es» el hilo.", "Son objetos distintos que cumplen una función parecida.", "Di que la línea cumple la función del hilo y señala qué cambia.")],
    T=[
        ("abc", "{F} ¿Qué lugar de los dos textos se parece a un laberinto?", "Los pasillos del hospital donde Rosa se pierde", "La oficina de exámenes", "La funcionaria", "Los pasillos que se parecen todos son el laberinto del texto nuevo."),
        ("abc", "{F} ¿Qué objeto del mito ayuda a Teseo a volver?", "Un hilo", "Una línea pintada en el piso", "Una linterna", "Ariadna le entrega un hilo para volver a la salida."),
        ("{F} ¿De qué color es la línea que guía a Rosa? Escribe una palabra.", "amarilla", "La funcionaria le muestra una línea amarilla en el piso."),
        ("abc", "{F} ¿Qué símbolo del texto nuevo cumple una función parecida al hilo?", "La línea amarilla", "La oficina de exámenes", "Los papeles de Rosa", "Ambos son guías que permiten llegar y volver."),
        ("ab", "{F} ¿Qué personaje del texto nuevo se parece a Ariadna?", "La funcionaria que muestra la línea", "Rosa, que se pierde dos veces", "Ariadna entrega la guía, y la funcionaria hace lo mismo con la línea."),
        ("abc", "En Lengua y Literatura: ¿qué es un símbolo?", "Un objeto o imagen que representa una idea más amplia", "Una palabra con tilde", "Un número en una tabla", "El símbolo representa algo más que su aspecto."),
        ("abc", "{F} ¿Qué representa la línea amarilla para Rosa?", "Una guía confiable para no perderse", "Un peligro que debe evitar", "Una decoración sin sentido", "Rosa la sigue por tres pasillos y llega a su destino."),
        ("abc", "{F} ¿Qué se puede decir de que los pasillos «se parezcan todos»?", "Muestra lo fácil que es perderse, como en un laberinto", "Muestra que el hospital es pequeño", "Muestra que Rosa conoce el lugar", "Pasillos iguales hacen que alguien se pierda, igual que en un laberinto."),
        ("ab", "{F} Al volver, Rosa ve una flecha amarilla en cada esquina. ¿Qué puede significar?", "Que la guía estaba ahí y solo se ve cuando se sabe buscarla", "Que el hospital tiene muchos pasillos", "El detalle muestra que la ayuda ya existía y Rosa antes no la había visto."),
        ("abc", "¿Un símbolo significa siempre lo mismo en todos los textos?", "No: su sentido depende de la obra", "Sí: siempre significa lo mismo", "Solo cambia en los poemas", "Un hilo puede ser guía en un texto y unión entre personas en otro."),
        ("abc", "En una oficina, un letrero dice: «Siga la línea azul para llegar a caja». ¿Qué función cumple?", "Como el hilo del mito, orienta para llegar y volver", "Es una cita del Quijote", "Es el nombre de un personaje", "La línea cumple una función de guía parecida a la del hilo."),
        ("abc", "{F} Elena dice: «La línea amarilla es solo pintura, no un símbolo». ¿Qué respuesta sirve?", "En el texto cumple la función del hilo: guía a Rosa", "Tiene razón: la pintura no significa nada", "Es un personaje del mito", "Un objeto común puede ser símbolo si en el texto representa una idea."),
        ("abc", "{F} ¿Qué cambia entre el hilo y la línea amarilla?", "El hilo se suelta al avanzar y la línea ya está pintada", "Ambos se sueltan al avanzar", "Ambos están en un monstruo", "Los textos muestran quién y cuándo pone la guía."),
    ],
    ctx=("abc", "En un trámite grande, la persona que te atiende te dibuja el camino con flechas en un papel. ¿Con qué elemento del mito se relaciona?", "Con el hilo de Ariadna, que guía para llegar y volver", "Con el Minotauro, que persigue", "Con Pandora, que abre la caja", "Las flechas orientan como el hilo en el laberinto."),
    sc=[("¿Qué representa el laberinto en el mito del Minotauro?", "Un lugar donde es fácil perderse", "El laberinto es un símbolo de perderse."),
        ("En Lengua y Literatura: ¿qué representa el hilo del mito?", "Una guía para volver a la salida", "El hilo permite a Teseo orientarse."),
        ("¿Cómo explicas un símbolo en un análisis?", "Digo qué representa con un dato del texto", "No basta con nombrarlo: se justifica con el texto.")],
    op=("Escribe un párrafo de cinco oraciones que relacione el mito con «El pasillo amarillo»: señala el símbolo del laberinto, el de la guía, un papel de personaje y qué cambia. {F}",
        "En ambos textos aparece un lugar donde uno se pierde: el laberinto y el hospital. La guía es el hilo y la línea amarilla. Ariadna y la funcionaria cumplen el papel de quien ayuda. Cambia que el hilo se suelta y la línea ya está pintada. Así, el texto nuevo cuenta una orientación cotidiana.",
        ["señala dos símbolos con datos", "relaciona un papel de personaje", "dice qué cambia"],
        ["un párrafo de cinco oraciones"],
        ["decir «es un símbolo» sin explicar", "no mencionar qué cambia"],
        "Pregunta: «¿Qué dato del texto prueba que la línea es una guía?»."),
    reinforce="Anota un lugar de tu barrio o trabajo donde es fácil perderse y qué señal o persona te guía.",
    extend="Escribe cuatro oraciones de un relato breve en que alguien se pierde en una feria y una señal lo orienta; di qué símbolo repites.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo aprendido: decido si una relación entre dos obras es sólida y comunico mi conclusión.",
    prior=["Sé comparar personajes, tema y símbolo.", "Reconozco cita, alusión y reescritura.", "Apoyo lo que digo con datos del texto."],
    explain=[
        "No todo parecido es intertextualidad. Dos textos pueden compartir un nombre por casualidad y no tener relación. Una relación sólida aparece cuando se repiten personajes con un papel parecido, un tema o un símbolo, y esas coincidencias se pueden mostrar con datos de ambos textos.",
        "Para revisar, hazte tres preguntas. ¿Coinciden los papeles de los personajes? ¿Coincide el tema? ¿Hay un objeto o imagen que se repite? Si respondes sí con evidencia a dos o tres, la relación es sólida. Si solo coincide un nombre, es débil.",
        "Cierra con una frase que diga qué relación hay y qué cambia, y revisa que cada afirmación tenga un dato. Después piensa qué parte te costó para decidir cómo seguir: leer más una obra, practicar la comparación o apoyar mejor tus opiniones.",
    ],
    vocab=[("relación sólida", "coincidencia apoyada en varios datos de ambos textos"), ("casualidad", "parecido sin relación entre los textos"), ("evidencia", "dato del texto que prueba lo que dices"), ("conclusión", "frase final que resume lo que se descubrió")],
    worked=[
        ("Descartar una coincidencia", "Texto 1: edificio llamado Ítaca y vecino llamado Ulises, sin otra relación con la Odisea.", ["Coincide el nombre.", "No coincide el papel ni el tema ni un símbolo.", "No hay datos para apoyar una relación."], "Relación débil: solo coinciden los nombres"),
        ("Confirmar una relación", "Texto 2: Nelly vuelve después de tres años, pasa pruebas en el camino y su perro la reconoce.", ["Papel: quien regresa tras una larga ausencia.", "Tema: el regreso a casa.", "Dato que se repite: el perro que reconoce."], "Relación sólida con tres coincidencias"),
    ],
    mistakes=[("Decir que hay relación solo porque se repite un nombre.", "El nombre puede ser casualidad.", "Busca papeles, tema o símbolos que coincidan con datos."),
              ("Cerrar sin decir qué cambia.", "La conclusión queda incompleta si solo cuenta lo que se parece.", "Agrega una frase con la diferencia.")],
    T=[
        ("abc", "{F} ¿Cuál de los textos nuevos mantiene una relación sólida con la Odisea?", "El Texto 2, «El regreso de Nelly»", "El Texto 1, «Calle 5»", "Ninguno", "El Texto 2 repite el regreso, las pruebas y el perro que reconoce."),
        ("abc", "{F} ¿Por qué el Texto 1 no tiene una relación sólida con la Odisea?", "Solo coinciden nombres, sin papeles, tema ni símbolo en común", "Porque ocurre en un edificio", "Porque no hay animales", "Los nombres Ítaca y Ulises no bastan sin otras coincidencias."),
        ("{F} ¿Cuántos años estuvo Nelly fuera? Escribe el número.", "3", "El texto dice que volvió después de tres años."),
        ("ab", "{F} ¿Qué personaje del Texto 2 se parece a Ulises?", "Nelly, que vuelve tras años de ausencia", "Su perro", "Nelly regresa después de pruebas, como Ulises."),
        ("abc", "{F} ¿Qué personaje reconoce a quien vuelve en la Odisea y en el Texto 2?", "El perro", "La hermana", "Un vecino", "Ambos textos muestran un perro que reconoce a quien regresa."),
        ("abc", "{F} ¿Qué tema une la Odisea y el Texto 2?", "El regreso a casa después de una larga ausencia", "La ambición", "El miedo al mar", "En los dos hay alguien que vuelve tras años de viaje."),
        ("abc", "{F} ¿Qué papel cumple la hermana de Nelly?", "Uno parecido al de Penélope: cuida la casa y recibe a quien vuelve", "El de Ulises, el viajero", "El de un vecino sin relación", "La hermana cuidó la casa, como Penélope en el resumen."),
        ("abc", "{F} ¿Qué situación del camino de Nelly equivale a las pruebas de Ulises?", "El temporal y el cierre de ruta que la obligan a dar un rodeo", "El perro que ladra de alegría", "La puerta de su casa", "Son obstáculos del camino, como las pruebas en el mar."),
        ("ab", "{F} ¿Qué cambia más entre Ulises y Nelly?", "Un rey de una isla frente a una camionera de un barrio", "El tema del regreso", "El texto nuevo mantiene el regreso; cambian el personaje y el lugar."),
        ("abc", "Quieres confirmar si una relación es sólida. ¿Qué haces?", "Releo ambos textos y anoto al menos dos coincidencias con datos", "Elijo el texto que me gusta más", "Cuento cuántas palabras tienen", "Una relación se confirma con coincidencias apoyadas en datos."),
        ("abc", "{F} Paula escribe: «Nelly recuerda a Ulises porque vuelve tras años y su perro la reconoce». ¿Qué tiene de bueno esa frase?", "Dice una relación y la apoya con datos de los textos", "Copia el texto completo", "No menciona ningún dato", "La frase señala dos datos que prueban la relación."),
        ("ab", "{F} Si Nelly no tuviera perro, ¿seguiría habiendo relación con la Odisea?", "Sí, pero más débil: quedarían el regreso y los obstáculos", "No: el perro es la única coincidencia", "El regreso y los obstáculos siguen presentes, aunque falte un dato."),
        ("abc", "{F} ¿Qué haces si al analizar solo encuentras que coincide un nombre?", "Concluyo que la relación es débil y busco otros datos", "Afirmo que es una reescritura", "Cambio el nombre del texto", "Un solo nombre no prueba que haya relación."),
    ],
    ctx=("abc", "Una amiga te cuenta que su relato «se parece al Quijote porque el protagonista se llama Alonso». ¿Qué le recomiendas?", "Buscar otras coincidencias: papel, tema o símbolo, con datos", "Cambiarle el nombre al protagonista", "No escribir más", "Un nombre no basta: se necesita más evidencia."),
    sc=[("En Lengua y Literatura: ¿qué hace sólida una relación entre dos obras?", "Coincidencias apoyadas en datos de ambos textos", "La evidencia hace sólida la relación."),
        ("¿Qué tres preguntas me hago al revisar?", "Papeles, tema y símbolo", "Si coinciden, la relación gana fuerza."),
        ("¿Cómo cierro mi análisis?", "Con una frase que diga qué relación hay y qué cambia", "Una conclusión completa muestra parecido y diferencia.")],
    op=("Escribe en cuatro oraciones tu conclusión sobre el Texto 2 y la Odisea: la relación, dos datos de apoyo, una diferencia y qué parte del método te costó más. {F}",
        "El Texto 2 se relaciona con la Odisea porque Nelly regresa tras años y su perro la reconoce. Tiene pruebas en el camino, como Ulises. Cambia que Nelly es camionera y vuelve a un barrio. Me costó explicar el tema con datos.",
        ["dice la relación", "da dos datos", "indica una diferencia", "nombra qué le costó"],
        ["cuatro oraciones escritas"],
        ["no dar datos", "no decir qué le costó"],
        "Pregunta: «¿Cómo vas a practicar lo que te costó?»."),
    reinforce="Elige una historia de tu familia y explica en dos oraciones si se parece a algún texto clásico y en qué.",
    extend="Compara en una tabla la Odisea, «La espera de Marta» y «El regreso de Nelly» según personajes, tema y símbolo.",
)
