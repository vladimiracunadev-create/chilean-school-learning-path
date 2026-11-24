"""Lengua y Literatura EPJA Media N1, módulo 1, OAD-04: elaborar un comentario literario para comunicar la interpretación de una obra, con coherencia y cohesión. Todos los cuentos y textos son inventados y se resuelven en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = (
    "Lápiz, goma y cuaderno. Todos los cuentos, mensajes y comentarios de este cuaderno son inventados («de ejemplo») y están escritos en cada ejercicio: "
    "no necesitas libros, audio, video ni internet. Si algo te cuesta escribir, puedes decir tu comentario en voz alta y que otra persona lo anote; pedir apoyo es parte de aprender. "
    "No escribas datos personales reales (cédula, dirección ni teléfono)."
)
build = make_build(MATERIALS)

O = "EPJA-LELI-NM1-OAD-04"
PRIOR = ["Cuento a otras personas lo que pienso de una película, una serie o un relato.", "Sé escribir oraciones y unirlas en un párrafo.", "He explicado por qué algo me gustó o no me gustó."]

BICI = ("Cuento (inventado), «La bicicleta azul»: Hernán guardaba en el fondo del garaje una bicicleta azul sin ruedas. Cada vez que su hija le pedía venderla, él decía: «Todavía no». "
        "Un sábado, la hija encontró el viejo manubrio envuelto en un paño. Hernán lo tomó, lo limpió con la manga y le dijo: «Con esto aprendí a llevar el rumbo». "
        "Esa tarde, entre los dos, armaron una bicicleta nueva con las piezas que había.")
MODELO = ("Comentario modelo (inventado) sobre «La bicicleta azul». [Introducción] En «La bicicleta azul», un padre guarda por años una bicicleta sin ruedas. "
          "[Tesis] El cuento muestra que los objetos viejos guardan recuerdos que una familia puede transformar en algo nuevo. "
          "[Argumento 1] En primer lugar, Hernán se resiste a vender la bicicleta: dice «Todavía no». Esa frase indica que, para él, la bicicleta es más que un objeto. "
          "[Argumento 2] Además, cuando limpia el manubrio dice «Con esto aprendí a llevar el rumbo», lo que une el objeto con su propia vida. "
          "[Cierre] Por eso, al armar juntos una bicicleta nueva, padre e hija convierten el recuerdo en un lazo presente.")
CERRADURA = ("Cuento (inventado), «La cerradura nueva»: Elías cambió la cerradura de la casa de su madre porque habían forzado la anterior. Le entregó dos llaves nuevas. "
             "Ella las guardó en un frasco de vidrio y dejó la puerta sin cerrar toda la noche. Al día siguiente, Elías la encontró sentada en la entrada, esperando a los vecinos que pasaban a saludarla.")
LIBRETA = ("Cuento (inventado), «La libreta de fiado»: En el almacén de doña Chela había una libreta donde anotaba lo que los vecinos le debían. Un diciembre, Chela la abrió, miró los nombres y la cerró sin hacer ningún cobro. "
           "Esa noche la guardó en el cajón con una cinta. Al otro día, los vecinos llegaron con pan y dulces para compartir.")
BANCO = ("Cuento (inventado), «El banco de la plaza»: Todas las mañanas, don Aurelio se sentaba en el mismo banco de la plaza con un termo y dos tazas. Una era para él. La otra la dejaba en el banco, boca abajo. "
         "Un día una joven con uniforme de enfermera se sentó a su lado y le preguntó por la segunda taza. Don Aurelio la dio vuelta, sirvió té y le dijo: «Hoy sí hacía falta».")


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    build(O, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ============================================================ clase 1
K(1, BICI + " Mensaje 1 (inventado): «Un papá guarda una bicicleta y al final la arman con su hija». "
      "Mensaje 2 (inventado): «Me encantó, está buenísimo». "
      "Mensaje 3 (inventado): «El cuento muestra que lo viejo puede volver a ser útil: Hernán dice ‘Todavía no’ cuando le piden vender la bicicleta, y al final la rearma con su hija».",
  "Hoy parto de lo que ya hago: contar a otros lo que pienso de un relato. Distingo resumen, opinión y comentario literario.",
  ["Todos hemos comentado alguna vez una película, un capítulo o un relato: «me gustó porque…», «no entendí por qué…». Esa costumbre de dar razones es el inicio de un comentario literario.",
   "Un resumen cuenta qué pasó. Una opinión dice si algo gustó o no. Un comentario literario va más lejos: propone qué significa la obra, lo explica con razones y lo apoya con citas. Quiere que otra persona entienda tu interpretación y pueda comprobarla.",
   "Un comentario literario se escribe para alguien: un grupo de lectura, un boletín, una clase. Por eso conviene que sea claro y ordenado. Hoy solo distinguiremos los tres tipos de texto; en las siguientes clases aprenderás a armar cada parte."],
  [("comentario literario", "texto que explica una interpretación de una obra con razones y citas"), ("resumen", "relato breve de lo que ocurre"), ("opinión", "juicio personal sobre si algo gusta o no"), ("cita", "frase copiada exacta de la obra")],
  [("Distinguir los tres", "Mensajes 1, 2 y 3 sobre «La bicicleta azul».", ["El 1 cuenta qué pasa: resumen.", "El 2 solo dice que le gustó: opinión.", "El 3 propone un sentido y usa una cita: comentario."], "1 resumen; 2 opinión; 3 comentario"),
   ("Mejorar una opinión", "Opinión: «Me encantó». Se convierte en comentario.", ["Agrego por qué: porque muestra cómo lo viejo vuelve a servir.", "Agrego una cita: «Todavía no».", "Ahora explica y prueba."], "Opinión convertida en comentario")],
  [("Creer que un comentario literario es solo decir si me gustó.", "Eso es una opinión sin razones.", "Agrega el sentido que ves y una cita."),
   ("Repetir el argumento y llamarlo comentario.", "Es un resumen.", "Agrega qué significa lo que cuentas.")],
  [("abc", "{F} ¿Qué hay en el fondo del garaje de Hernán?", "Una bicicleta azul sin ruedas", "Un auto antiguo", "Una caja de herramientas", "El cuento dice que guardaba una bicicleta azul sin ruedas."),
   ("ab", "{F} ¿Qué responde Hernán cuando su hija le pide venderla?", "«Todavía no»", "«Cuando quieras»", "El cuento incluye esa respuesta entre comillas."),
   ("{F} ¿Cuántos mensajes de personas lectoras hay? Escribe el número.", "3", "Aparecen los mensajes 1, 2 y 3."),
   ("abc", "En Lengua y Literatura: ¿qué es un comentario literario?", "Un texto que explica una interpretación de la obra con razones y citas", "Un resumen de todos los hechos", "Una opinión corta", "El comentario propone un sentido y lo prueba."),
   ("abc", "{F} ¿Cuál mensaje es un resumen?", "El Mensaje 1", "El Mensaje 2", "El Mensaje 3", "El 1 solo cuenta qué pasa en el cuento."),
   ("ab", "{F} ¿Cuál mensaje es solo una opinión?", "El Mensaje 2, porque dice «me encantó»", "El Mensaje 3, porque cita", "Expresa gusto sin dar razones del texto."),
   ("abc", "{F} ¿Qué cita usa el Mensaje 3?", "«Todavía no»", "«Con esto aprendí a llevar el rumbo»", "«una bicicleta nueva»", "El mensaje cita lo que dice Hernán cuando le piden vender la bicicleta."),
   ("abc", "{F} ¿Qué falta en el Mensaje 1 para ser un comentario?", "Proponer qué significa el cuento", "Cambiar a segunda persona", "Agregar más hechos", "Un resumen cuenta; el comentario interpreta."),
   ("abc", "{F} ¿Qué falta en el Mensaje 2 para ser un comentario?", "Una razón y una cita del cuento", "Una fecha", "Una exclamación más", "Una opinión, para ser comentario, necesita razones del texto."),
   ("ab", "{F} ¿Qué idea central propone el Mensaje 3?", "Lo viejo puede volver a ser útil", "El garaje es un lugar peligroso", "Se desprende de la cita y del final del cuento."),
   ("abc", "Escribes: «El cuento me hizo pensar en mi barrio». ¿Qué tipo de texto es?", "Una opinión o reacción personal", "Un comentario literario completo", "Un resumen", "No explica el texto ni lo prueba."),
   ("abc", "Un compañero dice que su comentario está bien porque tiene cinco líneas. ¿Qué respondes?", "Lo importante es que tenga idea, razones y citas", "Lo importante es que sea largo", "Basta con que tenga la palabra «cuento»", "El comentario se evalúa por su contenido, no por su largo."),
   ("ab", "{F} Si el Mensaje 3 no incluyera la cita, ¿seguiría siendo un buen comentario?", "Quedaría menos probado, aunque tendría una idea", "Sí, la cita nunca importa", "La cita permite comprobar que la idea sale del texto.")],
  ("abc", "En el grupo de lectura de tu centro te piden «comentar» un cuento. ¿Qué entiendes que debes hacer?", "Decir qué significa y por qué, citando una frase", "Contar toda la historia otra vez", "Decir solo si te gustó", "Un comentario explica, prueba y comunica."),
  [("En Lengua y Literatura: ¿qué es una cita?", "Una frase copiada exacta de la obra", "La cita prueba que la idea sale del texto."),
   ("¿Qué diferencia hay entre opinión y comentario?", "El comentario da razones y citas", "La opinión puede quedarse en gusto."),
   ("¿Para qué se escribe un comentario?", "Para comunicar una interpretación a otras personas", "Quiere que otro lector entienda y compruebe la idea.")],
  ("Lee el cuento: {F} Escribe en tu cuaderno tres textos de una oración sobre «La bicicleta azul»: un resumen, una opinión y un comentario con cita. Después marca cuál de los tres explica mejor el cuento y di por qué.",
   "Resumen: un padre guarda una bicicleta y al final la rearma con su hija. Opinión: me gustó mucho. Comentario: el cuento muestra que el pasado puede servir para construir algo nuevo; Hernán dice «Todavía no» y al final la rearma. El comentario es el que explica y prueba.",
   ["los tres textos son distintos", "el comentario tiene sentido y cita", "justifica cuál explica mejor"],
   ["tres oraciones y una justificación"],
   ["confundir resumen con comentario", "comentar sin cita"],
   "Pregunta: «¿Esa oración explica qué significa o solo cuenta qué pasa?»."),
  "Cuéntale a alguien lo que pensaste de un relato y pídele que te diga si entendió por qué.",
  "Reescribe una opinión tuya sobre un programa o relato como un comentario con una razón.")

# ============================================================ clase 2
K(2, MODELO,
  "Hoy reconozco las partes de un comentario literario y las palabras que ayudan a que sea claro: tesis, argumento, cita, conector y referente.",
  ["Un comentario literario tiene una estructura sencilla. La introducción presenta la obra. La tesis es la idea central que sostienes. Los argumentos son las razones que la apoyan, cada una con una cita. El cierre recoge la idea y deja algo para pensar.",
   "Para que un texto se entienda necesita coherencia y cohesión. La coherencia significa que todas las ideas se relacionan con el tema y no se contradicen. La cohesión significa que las oraciones están bien unidas, con conectores como «además», «por eso» o «en primer lugar», y con referentes, que son palabras que reemplazan a otras, como «esa frase» o «lo que».",
   "Fíjate en el comentario modelo: cada parte tiene una función. Si quitas la tesis, no se sabe qué idea se defiende. Si quitas los conectores, las oraciones quedan sueltas. Hoy aprenderás a ubicar cada parte; después aprenderás a escribirlas."],
  [("tesis", "idea central que defiende un comentario"), ("argumento", "razón que apoya la tesis"), ("conector", "palabra que une ideas, como «además» o «por eso»"), ("referente", "palabra que reemplaza a otra para no repetirla")],
  [("Ubicar la tesis", "En el modelo, ¿cuál es la tesis?", ["Es la idea central: lo que el comentario defiende.", "Está marcada: «El cuento muestra que los objetos viejos guardan recuerdos que una familia puede transformar en algo nuevo»."], "Es la oración de la tesis"),
   ("Ubicar conectores y referente", "Frases del modelo: «En primer lugar», «Además», «Por eso», «Esa frase».", ["«En primer lugar» y «Además» ordenan los argumentos.", "«Por eso» introduce una consecuencia en el cierre.", "«Esa frase» es un referente de «Todavía no»."], "Conectores: ordenar y consecuencia; referente: «esa frase»")],
  [("Poner la tesis al final sin haberla anunciado.", "El lector no sabe qué idea sigue el comentario.", "Anuncia la tesis en la parte inicial."),
   ("Escribir oraciones sin conectores.", "Las ideas quedan separadas.", "Usa conectores simples para unirlas.")],
  [("abc", "{F} ¿Cuál es la tesis del comentario modelo?", "Los objetos viejos guardan recuerdos que una familia puede transformar en algo nuevo", "Hernán vende una bicicleta", "La hija encuentra un manubrio", "Está marcada como tesis en el modelo."),
   ("ab", "{F} ¿Cuántos argumentos tiene el comentario modelo?", "Dos", "Tres", "El modelo marca el Argumento 1 y el Argumento 2."),
   ("{F} ¿Cuántas partes marcadas entre corchetes tiene el comentario modelo? Escribe el número.", "5", "Introducción, tesis, argumento 1, argumento 2 y cierre suman cinco."),
   ("abc", "En Lengua y Literatura: ¿qué es la tesis de un comentario?", "La idea central que se defiende", "El título del cuento", "La cita más larga", "La tesis guía todo el comentario."),
   ("abc", "{F} ¿Qué cita usa el Argumento 1?", "«Todavía no»", "«Con esto aprendí a llevar el rumbo»", "«una bicicleta nueva»", "Está entre comillas en la parte marcada como Argumento 1."),
   ("ab", "{F} ¿Qué conector abre el Argumento 2?", "«Además»", "«Por eso»", "El Argumento 2 comienza con «Además»."),
   ("abc", "{F} ¿Qué función tiene «Por eso» en el cierre?", "Presentar una consecuencia de lo dicho", "Comparar dos ideas", "Presentar un ejemplo", "El cierre extrae una conclusión de los argumentos."),
   ("abc", "{F} En «Esa frase indica que…», ¿a qué se refiere «esa frase»?", "A «Todavía no»", "A «una bicicleta nueva»", "Al título del cuento", "El referente reemplaza la cita que se acaba de nombrar."),
   ("abc", "{F} ¿Qué parte del comentario modelo presenta la obra?", "La introducción", "El cierre", "El argumento 2", "La introducción dice cuál es la obra y de qué trata en general."),
   ("ab", "{F} Si quitáramos la tesis del modelo, ¿qué pasaría?", "No se sabría qué idea se defiende", "El comentario se entendería mejor", "Los argumentos quedarían sin una idea que apoyar."),
   ("abc", "Un comentario dice: «La obra es buena. Tiene personajes. Hay un final». ¿Qué le falta?", "Una tesis, argumentos con citas y conectores", "Un título más largo", "Más adjetivos", "Se queda en frases sueltas sin una idea que las una."),
   ("abc", "¿Cuál de estos es un conector de orden?", "En primer lugar", "Hernán", "Cuaderno", "Ordena los argumentos de un texto."),
   ("ab", "{F} ¿Cuál es el cierre del modelo?", "«Por eso, al armar juntos una bicicleta nueva, padre e hija convierten el recuerdo en un lazo presente»", "«En primer lugar, Hernán se resiste a vender la bicicleta»", "Es la última parte marcada y recoge la idea central.")],
  ("abc", "Tienes que presentar un libro en la reunión del taller. ¿Con qué parte del comentario comenzarías?", "Con una introducción que diga qué obra es", "Con el cierre", "Con una cita sin explicar", "Se parte presentando la obra que se va a comentar."),
  [("En Lengua y Literatura: ¿qué es un conector?", "Una palabra que une ideas, como «además»", "Ayuda a ordenar y relacionar las oraciones."),
   ("¿Qué es un argumento en un comentario?", "Una razón que apoya la tesis, con cita", "Sin una cita el argumento queda sin prueba textual."),
   ("En Lengua y Literatura: ¿qué es un referente?", "Una palabra que reemplaza a otra para no repetirla", "Por ejemplo, «esa frase» retoma una cita ya nombrada.")],
  ("Lee el modelo: {F} En tu cuaderno copia el comentario modelo y subraya con colores o signos (1) la tesis, (2) las dos citas, (3) tres conectores y (4) un referente. Escribe al lado de cada uno para qué sirve.",
   "Tesis: «El cuento muestra que los objetos viejos…». Citas: «Todavía no» y «Con esto aprendí a llevar el rumbo». Conectores: «En primer lugar» (ordena), «Además» (suma), «Por eso» (consecuencia). Referente: «esa frase» (reemplaza «Todavía no»).",
   ["identifica la tesis", "ubica dos citas y tres conectores", "explica para qué sirve cada uno"],
   ["un texto marcado y una lista"],
   ["confundir cita y tesis", "no explicar la función"],
   "Pregunta: «¿Qué parte cumple esa función?»."),
  "Marca en un texto breve que te guste un conector y di qué une.",
  "Escribe una introducción de una oración para otro cuento que conozcas.")

# ============================================================ clase 3
K(3, CERRADURA,
  "Hoy aprendo, paso a paso, a planificar y escribir un comentario literario: elegir la tesis, buscar citas, armar un esquema y redactar.",
  ["Para escribir un comentario conviene seguir pasos. Primero, relee el cuento y formula tu interpretación: será tu tesis. Segundo, elige dos o tres evidencias con cita exacta. Tercero, arma un esquema con introducción, argumentos y cierre. Cuarto, redacta usando conectores. Quinto, revisa.",
   "Con «La cerradura nueva» podemos formular una tesis: «El cuento muestra que, para la madre, la confianza en los vecinos vale más que una cerradura». Las evidencias están en el texto: guarda las llaves en un frasco, deja la puerta sin cerrar y espera en la entrada a los vecinos que pasan a saludarla.",
   "Un esquema sencillo para redactar es: una oración de introducción; la tesis; el argumento 1 con cita; el argumento 2 con cita; un cierre. Al escribir, une las ideas con conectores y evita repetir la misma palabra todo el tiempo. Después revisa si cada oración sirve a la tesis."],
  [("esquema", "plan breve que ordena las partes de un texto"), ("redactar", "escribir un texto ordenando las ideas"), ("evidencia", "dato o cita que sostiene la tesis"), ("revisar", "leer de nuevo para corregir y mejorar")],
  [("De la interpretación a la tesis", "Interpretación: la madre confía en los vecinos más que en la cerradura. Se escribe la tesis.", ["Digo qué muestra el cuento.", "Uso la estructura «El cuento muestra que…».", "Tesis: «El cuento muestra que la confianza en los vecinos vale más que una cerradura»."], "Tesis redactada en una oración"),
   ("Armar el esquema", "Se arma el esquema con las evidencias del cuento.", ["Introducción: «En ‘La cerradura nueva’, Elías cambia la cerradura de la casa de su madre».", "Argumento 1: guarda las llaves en un frasco.", "Argumento 2: la encuentra esperando a los vecinos en la entrada."], "Esquema con introducción, dos argumentos y cierre")],
  [("Escribir sin planificar y perder el hilo.", "El texto se llena de ideas sueltas.", "Arma primero el esquema."),
   ("Escribir una tesis demasiado amplia, como «el cuento habla de la vida».", "No se puede comprobar.", "Haz la tesis concreta y ligada al cuento.")],
  [("abc", "{F} ¿Dónde guarda la madre las llaves nuevas?", "En un frasco de vidrio", "En un cajón de la cocina", "En el bolsillo de su delantal", "El cuento dice que las guarda en un frasco de vidrio."),
   ("ab", "{F} ¿Qué deja la madre toda la noche?", "La puerta sin cerrar", "La luz encendida", "El cuento dice que dejó la puerta sin cerrar."),
   ("{F} ¿Cuántas llaves nuevas le entrega Elías? Escribe el número.", "2", "El cuento dice que le entregó dos llaves nuevas."),
   ("abc", "En Lengua y Literatura: ¿cuál es el primer paso para escribir un comentario?", "Releer el cuento y formular una interpretación", "Escribir el cierre", "Copiar el cuento completo", "Sin una interpretación no hay tesis."),
   ("abc", "{F} ¿Cuál es una tesis bien formulada para el cuento?", "El cuento muestra que la confianza en los vecinos vale más que una cerradura", "El cuento habla de la vida", "El cuento tiene una puerta", "Es una idea concreta que se puede probar con citas."),
   ("ab", "{F} ¿Qué cita apoya la tesis de la confianza?", "«la encontró sentada en la entrada, esperando a los vecinos que pasaban a saludarla»", "«Elías cambió la cerradura»", "Muestra que ella espera a los vecinos sin miedo."),
   ("abc", "{F} ¿Qué parte del esquema ocupa «guarda las llaves en un frasco»?", "El argumento 1, como evidencia", "El título", "La tesis", "Es un hecho del cuento que se usa como prueba."),
   ("abc", "{F} ¿Qué conector sirve para abrir el argumento 2?", "Además", "Aunque", "En primer lugar", "La palabra «Además» suma una segunda razón a la primera."),
   ("abc", "{F} ¿Qué se agrega a un argumento para apoyarlo?", "Una cita exacta del cuento", "Una opinión sin prueba", "Un dibujo", "La cita muestra de dónde sale la razón."),
   ("ab", "{F} Un estudiante escribe como tesis: «El cuento es sobre una cerradura». ¿Qué le falta?", "Una idea que diga qué significa lo que ocurre", "Más palabras", "Describe el objeto, pero no propone un sentido."),
   ("abc", "{F} ¿Qué cierre es mejor?", "«Por eso, la madre convierte la entrada en un lugar de confianza compartida»", "«Fin»", "«La cerradura era nueva»", "El cierre recoge la tesis con una consecuencia."),
   ("abc", "{F} Un lector dice: «La madre odia a su hijo». ¿Qué problema tiene?", "No tiene cita del cuento que lo apoye", "Es muy corto", "Tiene un conector", "No hay evidencia de odio en el texto."),
   ("ab", "{F} Si el cuento dijera que la madre cierra con llave toda la noche, ¿qué pasaría con la tesis?", "Perdería apoyo y habría que replantearla", "Quedaría más sólida", "Cerrar con llave contradice la evidencia principal.")],
  ("abc", "Debes escribir dos párrafos sobre un cuento para el boletín de tu centro. ¿Qué haces primero?", "Elegir mi tesis y las citas que la apoyan", "Empezar a escribir sin un plan", "Copiar el cuento", "Planificar antes evita que las ideas queden desordenadas."),
  [("En Lengua y Literatura: ¿qué es una tesis?", "La idea central que se defiende en el comentario", "Resume mi interpretación en una oración."),
   ("¿Qué partes tiene el esquema de hoy?", "Introducción, tesis, argumento 1, argumento 2 y cierre", "Es una estructura simple y completa."),
   ("¿Qué se hace al final, antes de entregar?", "Revisar el texto", "Revisar el texto ayuda a corregir errores y repeticiones.")],
  ("Lee el cuento: {F} Arma un esquema de comentario con (1) introducción, (2) tesis, (3) argumento 1 con cita exacta, (4) argumento 2 con cita exacta y (5) cierre. Después redáctalo en un párrafo de seis a ocho líneas, con al menos tres conectores.",
   "Introducción: En «La cerradura nueva», Elías cambia la cerradura de su madre. Tesis: el cuento muestra que la confianza en los vecinos vale más que una cerradura. Argumento 1: ella guarda las llaves en «un frasco de vidrio». Argumento 2: la encuentra «esperando a los vecinos». Cierre: por eso, la entrada es un lugar de encuentro.",
   ["esquema con cinco partes", "dos citas exactas", "al menos tres conectores"],
   ["un esquema y un párrafo"],
   ["tesis muy amplia", "citas inexactas"],
   "Pregunta: «¿Qué conector une tu argumento con el siguiente?»."),
  "Lee tu esquema a otra persona y pregúntale si entiende cuál es tu tesis.",
  "Cambia la tesis por otra posible y busca dos citas distintas.")

# ============================================================ clase 4
K(4, "Comentario borrador (inventado) sobre «La cerradura nueva»: «La madre confía. Elías cambió la cerradura. Elías le entregó dos llaves. La madre guardó las llaves en un frasco. La madre dejó la puerta sin cerrar. La madre esperó a los vecinos. La madre esperó en la entrada». "
      "Conectores disponibles: además, porque, por eso, en primer lugar, sin embargo, finalmente. Referentes: ella, esa decisión, allí, lo que.",
  "Hoy practico con apoyo la coherencia y la cohesión: uno ideas con conectores y referentes y evito repetir palabras sin necesidad.",
  ["La cohesión es la unión de las oraciones dentro de un texto. Se logra con conectores, que indican la relación entre dos ideas, y con referentes, que reemplazan a una palabra ya dicha. Un texto sin cohesión se lee como una lista de frases sueltas.",
   "Los conectores más útiles son: «porque» (causa), «por eso» (consecuencia), «además» (suma), «sin embargo» (contraste), «en primer lugar» y «finalmente» (orden). Un referente puede ser un pronombre, como «ella», o una frase como «esa decisión», que retoma lo dicho antes.",
   "La coherencia es que todas las ideas se relacionen con la tesis y no se contradigan. En el borrador de hoy, todas las oraciones empiezan con «la madre» y no hay conectores. Corrigiendo eso, el texto se vuelve más fluido y fácil de entender."],
  [("cohesión", "unión de las oraciones mediante conectores y referentes"), ("coherencia", "relación lógica de las ideas con el tema, sin contradicciones"), ("pronombre", "palabra que reemplaza a un nombre, como «ella»"), ("repetición", "decir muchas veces la misma palabra sin necesidad")],
  [("Reemplazar con un referente", "Oraciones: «La madre guardó las llaves. La madre dejó la puerta abierta». Se corrige.", ["Identifico la repetición de «La madre».", "Reemplazo la segunda por «ella».", "Resultado: «La madre guardó las llaves. Ella dejó la puerta abierta»."], "Referente «ella» evita repetir"),
   ("Unir con un conector", "Oraciones: «La madre dejó la puerta abierta. Esperó a los vecinos». Se unen.", ["La segunda explica el motivo.", "Uso «porque» o «y» según el sentido.", "«La madre dejó la puerta abierta porque esperaba a los vecinos»."], "Con «porque» una oración explica la otra")],
  [("Poner muchos conectores sin que tengan sentido.", "Cada conector debe indicar una relación real.", "Elige el conector según lo que quieres expresar."),
   ("Usar «ella» sin saber a quién se refiere.", "El lector se confunde si hay dos personas posibles.", "Aclara el referente si hay duda.")],
  [("abc", "{F} ¿Qué problema principal tiene el borrador?", "Repite «la madre» en cada oración y no usa conectores", "No tiene ninguna cita del cuento", "Está escrito en tercera persona", "Todas las oraciones empiezan igual y quedan sueltas."),
   ("ab", "{F} ¿Con qué palabra se puede reemplazar «La madre» en la segunda mención?", "Ella", "Elías", "«Ella» retoma a la madre; Elías es otro personaje."),
   ("{F} ¿Cuántas veces aparece «La madre» en el borrador? Escribe el número.", "5", "«La madre» abre cinco oraciones del borrador: confía, guardó, dejó y dos veces esperó."),
   ("abc", "En Lengua y Literatura: ¿qué es la cohesión?", "La unión de las oraciones con conectores y referentes", "El tema general de un texto", "La cantidad de párrafos", "Une las distintas partes del texto en un solo conjunto."),
   ("abc", "¿Qué conector indica causa?", "Porque", "Además", "Sin embargo", "«Porque» introduce la razón de algo."),
   ("abc", "¿Qué conector indica contraste?", "Sin embargo", "Además", "Finalmente", "Este conector sirve para oponer dos ideas distintas."),
   ("ab", "¿Qué conector sirve para sumar una segunda razón?", "Además", "Por eso", "«Además» agrega algo más a lo ya dicho."),
   ("abc", "{F} Une con un conector: «La madre dejó la puerta abierta. Esperó a los vecinos». ¿Cuál es el mejor?", "La madre dejó la puerta abierta porque esperaba a los vecinos", "La madre dejó la puerta abierta sin embargo esperaba a los vecinos", "La madre dejó la puerta abierta finalmente esperaba a los vecinos", "«Porque» muestra el motivo de dejar la puerta abierta."),
   ("abc", "{F} ¿Qué referente de la lista retoma la acción de dejar la puerta abierta?", "Esa decisión", "Allí", "Ella", "Una frase como «esa decisión» retoma la acción anterior."),
   ("ab", "{F} ¿Qué oración tiene mejor cohesión?", "La madre guardó las llaves en un frasco y, además, dejó la puerta sin cerrar", "La madre guardó las llaves. La madre dejó la puerta. La madre esperó", "La primera une las ideas con conectores y evita repetir."),
   ("abc", "{F} ¿Qué oración final cierra mejor con consecuencia?", "Por eso, la entrada se convierte en un lugar de confianza", "Sin embargo, era un frasco", "Allí estaba el borrador", "«Por eso» conecta una consecuencia con lo anterior."),
   ("abc", "{F} Dos oraciones se contradicen: «La madre confía en los vecinos» y «La madre desconfía de todos». ¿Qué falla?", "La coherencia", "La ortografía", "El título", "Las dos ideas se contradicen entre sí en el texto."),
   ("ab", "{F} ¿Se pierde coherencia si el comentario agrega: «La madre vive en el campo y tiene muchos animales»?", "Sí, porque esa idea no se relaciona con la tesis", "No, siempre se pueden agregar datos", "Los datos que no se relacionan con la tesis restan coherencia.")],
  ("abc", "En tu trabajo te piden escribir un correo breve. Si todas las oraciones empiezan igual y no tienen conectores, ¿qué podría pasar?", "Que el mensaje se entienda como una lista de frases sueltas", "Que se entienda mejor", "Que parezca más largo", "Mejorar la cohesión ayuda a que se entienda el mensaje."),
  [("En Lengua y Literatura: ¿qué es la coherencia?", "Que las ideas se relacionen con el tema sin contradecirse", "Todas las ideas deben servir a la tesis."),
   ("¿Para qué sirve un referente?", "Para reemplazar una palabra y evitar repetirla", "Así el texto se mantiene fluido y sin repeticiones."),
   ("¿Qué conector uso para marcar consecuencia?", "Por eso", "Une una causa con su resultado.")],
  ("Lee el borrador: {F} Reescribe el borrador en un solo párrafo de cuatro a seis oraciones, usando al menos tres conectores de la lista y dos referentes distintos. Mantén la idea «la madre confía en los vecinos» y quita lo que se repita.",
   "La madre confía en los vecinos. En primer lugar, guardó las llaves en un frasco; además, dejó la puerta sin cerrar porque esperaba a los vecinos. Ella los aguardó en la entrada. Por eso, esa decisión muestra su confianza.",
   ["usa tres conectores con sentido", "usa dos referentes", "no se contradice"],
   ["un párrafo reescrito"],
   ["poner conectores sin sentido", "referentes confusos"],
   "Pregunta: «¿Qué conector expresa mejor la relación entre estas dos ideas?»."),
  "Escribe tres oraciones sobre tu día unidas con dos conectores distintos.",
  "Agrega una oración de contraste con «sin embargo» a tu párrafo reescrito.")

# ============================================================ clase 5
K(5, LIBRETA + " Comentario A (inventado): «El cuento muestra la generosidad de doña Chela. Ella cierra la libreta ‘sin hacer ningún cobro’. Por eso, los vecinos llegan con pan y dulces. Esto demuestra que un gesto de confianza vuelve en forma de gratitud». "
      "Comentario B (inventado): «Doña Chela tiene un almacén. En mi barrio había un almacén. Los precios suben mucho. Me gusta el pan. La libreta es de papel».",
  "Hoy aplico lo aprendido a una situación de comunidad: escribo y reviso un comentario para compartir en un grupo de lectura del barrio.",
  ["Un comentario literario no solo se hace en la escuela: se comparte en un grupo de lectura, en un boletín o en una charla. Cuando escribes para otras personas, piensa en quién va a leer y qué necesita para entender tu idea.",
   "Un comentario eficaz tiene una tesis clara, argumentos con citas y buena unión entre las oraciones. Un comentario que mezcla ideas sin relación pierde coherencia, aunque cada oración esté bien escrita. Por eso, antes de entregar, revisa que cada oración sirva a la tesis.",
   "Una buena revisión sigue preguntas simples: ¿se entiende mi tesis?, ¿cada argumento tiene cita?, ¿hay conectores y referentes?, ¿alguna oración no tiene que ver con el tema? Si una respuesta es «no», corrige esa parte."],
  [("grupo de lectura", "reunión donde varias personas leen y conversan sobre un texto"), ("boletín", "hoja breve que informa a un grupo"), ("generosidad", "disposición a dar sin esperar algo a cambio"), ("revisión", "lectura crítica para mejorar un texto")],
  [("Evaluar el comentario A", "Comentario A del enunciado. ¿Qué tiene?", ["Tiene tesis: la generosidad de doña Chela.", "Tiene una cita: «sin hacer ningún cobro».", "Tiene conectores («Por eso») y un referente («Esto»)."], "Es coherente y cohesionado"),
   ("Evaluar el comentario B", "Comentario B del enunciado. ¿Qué le falta?", ["No tiene tesis: solo frases sueltas.", "Mezcla ideas sin relación con el cuento: precios, pan.", "No cita ni usa conectores."], "No tiene coherencia ni cohesión")],
  [("Mezclar recuerdos personales sin relación con la tesis.", "El comentario pierde foco.", "Elige solo los datos que apoyen tu idea."),
   ("Entregar sin revisar.", "Se escapan repeticiones y contradicciones.", "Lee en voz alta y corrige.")],
  [("abc", "{F} ¿Qué anotaba doña Chela en la libreta?", "Lo que los vecinos le debían", "Las recetas de pan", "Los nombres de sus clientes preferidos", "El cuento dice que la libreta guardaba lo que le debían."),
   ("ab", "{F} ¿Qué hizo doña Chela con la libreta en diciembre?", "La cerró sin hacer ningún cobro", "La rompió en pedazos", "El cuento dice que la cerró sin cobrar."),
   ("{F} ¿Cuántos comentarios hay para evaluar? Escribe el número.", "2", "Se presentan el comentario A y el B."),
   ("abc", "{F} ¿Qué tesis tiene el comentario A?", "Doña Chela es generosa", "Los precios suben", "El pan es bueno", "El comentario A dice «el cuento muestra la generosidad de doña Chela»."),
   ("abc", "{F} ¿Qué cita usa el comentario A?", "«sin hacer ningún cobro»", "«con pan y dulces»", "«en el cajón»", "Está entre comillas dentro del comentario A."),
   ("ab", "{F} ¿Qué conector usa el comentario A para introducir una consecuencia?", "«Por eso»", "«Además»", "«Por eso» aparece antes de «los vecinos llegan con pan y dulces»."),
   ("abc", "{F} ¿Qué referente usa el comentario A para retomar lo dicho?", "«Esto»", "«Allí»", "«Aquello»", "La palabra «Esto» retoma todo lo anterior."),
   ("abc", "{F} ¿Por qué el comentario B no es coherente?", "Mezcla ideas que no se relacionan con una tesis", "Es demasiado largo", "Tiene demasiadas citas", "Pasa de un tema a otro sin relación."),
   ("abc", "{F} ¿Qué falta al comentario B para tener cohesión?", "Conectores y referentes que unan las ideas", "Más puntos", "Un título largo", "Las oraciones están sueltas y sin relación explícita."),
   ("ab", "{F} ¿Qué oración de B sirve al tema del cuento?", "«Doña Chela tiene un almacén»", "«Me gusta el pan»", "Es un dato del cuento; la segunda es una preferencia sin relación."),
   ("abc", "{F} ¿Qué debería agregar B para ser un comentario?", "Una tesis y una cita sobre lo que hace doña Chela con la libreta", "Más datos sobre precios", "El nombre de otro almacén", "Un comentario necesita idea central y evidencia."),
   ("abc", "{F} ¿Qué pregunta sirve en la revisión?", "¿Cada argumento tiene una cita?", "¿Cuántas palabras tiene el título?", "¿De qué color es la hoja?", "La pregunta ayuda a comprobar el apoyo en el texto."),
   ("ab", "{F} Si el comentario A agregara «los precios suben mucho», ¿mejoraría?", "No, esa idea no se relaciona con la tesis", "Sí, cualquier dato mejora el comentario", "Una idea sin relación resta coherencia.")],
  ("abc", "Tu grupo de lectura del barrio te pide un comentario de un cuento para el boletín. ¿Qué haces al terminar de escribir?", "Lo reviso con preguntas sobre tesis, citas y conectores", "Lo entrego sin leerlo", "Lo vuelvo un resumen", "Revisar ayuda a que otras personas lo entiendan."),
  [("En Lengua y Literatura: ¿qué tres cosas revisas en un comentario?", "Tesis, citas y conectores", "Con eso compruebo coherencia y cohesión."),
   ("¿Qué hago con una oración que no se relaciona con la tesis?", "La quito o la cambio", "Quitarla mejora la coherencia de todo el comentario."),
   ("¿Para qué leer el comentario en voz alta?", "Para notar repeticiones y partes confusas", "Al oírlo en voz alta se detectan errores y repeticiones.")],
  ("Lee el cuento: {F} Escribe tu propio comentario de cinco a siete oraciones sobre «La libreta de fiado» con tesis, dos citas exactas, tres conectores y un cierre. Luego revísalo con las cuatro preguntas de la clase y corrige lo necesario.",
   "En «La libreta de fiado», un gesto de confianza vuelve en forma de gratitud. Doña Chela cierra la libreta «sin hacer ningún cobro» y la guarda con una cinta. Por eso, los vecinos llegan con «pan y dulces» al otro día. Además, el cuento muestra que la comunidad responde con cuidado. En conclusión, un favor sin cobro crea lazos.",
   ["tesis clara", "dos citas exactas", "tres conectores con sentido", "cierre coherente"],
   ["un comentario de cinco a siete oraciones"],
   ["mezclar ideas sin relación", "no revisar"],
   "Pregunta: «¿Qué oración no ayuda a tu tesis?»."),
  "Pide a otra persona que lea tu comentario y diga cuál es su tesis.",
  "Escribe un cierre distinto, con una pregunta para el grupo de lectura.")

# ============================================================ clase 6
K(6, BANCO + " Comentario de ejemplo (inventado): «Don Aurelio deja una taza en el banco. Una joven le pregunta por la segunda taza. Él sirve té. El cuento muestra la soledad. Hoy hay sol».",
  "Hoy reviso lo logrado: evalúo un comentario con una pauta, lo reescribo para comunicarlo mejor y decido qué debo seguir practicando.",
  ["Hemos recorrido un camino: pasamos de opinar a comentar, aprendimos las partes de un comentario, practicamos la cohesión y la coherencia y escribimos para una comunidad. Hoy revisamos todo con una pauta de cinco criterios.",
   "La pauta pregunta: 1) ¿tiene una tesis clara?; 2) ¿hay al menos dos argumentos con cita exacta?; 3) ¿las ideas se relacionan con la tesis y no se contradicen?; 4) ¿hay conectores y referentes que unan las oraciones?; 5) ¿tiene un cierre que recoja la idea? Cada criterio logrado muestra un avance.",
   "Evaluar un comentario, propio o ajeno, es una conversación respetuosa para mejorar. Se empieza por lo que está logrado, se nombra lo que falta y se propone una forma concreta de corregirlo. Después, es útil comunicar el comentario en voz alta en un minuto, con las tres ideas clave."],
  [("pauta", "lista de criterios para evaluar"), ("criterio", "aspecto que se mira para evaluar"), ("comunicar", "hacer que otra persona entienda una idea"), ("cierre", "parte final que recoge la idea central")],
  [("Evaluar el ejemplo", "Comentario de ejemplo: «Don Aurelio deja una taza en el banco…». Se evalúa con la pauta.", ["1) Tesis: «el cuento muestra la soledad»: es una idea, pero sin explicar.", "2) Citas: no hay citas exactas.", "3) Coherencia: «Hoy hay sol» no se relaciona con la tesis."], "Cumple solo parcialmente el criterio 1"),
   ("Mejorar el comentario", "Se reescribe con tesis, cita y conectores.", ["Tesis: el cuento muestra que compartir una taza puede acompañar la soledad.", "Cita: «Hoy sí hacía falta».", "Cierre: por eso, la segunda taza tiene sentido."], "Comentario mejorado con tesis, cita y cierre")],
  [("Corregir sin decir qué está bien.", "La persona no sabe qué conservar.", "Empieza por lo logrado."),
   ("Entregar un comentario que cumple dos criterios y creer que está completo.", "Faltan criterios por cumplir.", "Revisa los cinco criterios.")],
  [("abc", "{F} ¿Qué lleva don Aurelio a la plaza?", "Un termo y dos tazas", "Un diario y un paraguas", "Una radio y una silla", "El cuento dice que se sentaba con un termo y dos tazas."),
   ("ab", "{F} ¿Qué hace don Aurelio con la segunda taza al final?", "La da vuelta y sirve té", "La guarda en el bolso", "Sirve té a la joven en esa taza, que estaba boca abajo."),
   ("{F} ¿Cuántos criterios tiene la pauta? Escribe el número.", "5", "La pauta del enunciado enumera cinco criterios."),
   ("abc", "{F} ¿Qué tesis tiene el comentario de ejemplo?", "El cuento muestra la soledad", "Hoy hay sol", "Una joven pregunta", "La dice la oración «El cuento muestra la soledad»."),
   ("abc", "{F} ¿Qué oración del comentario de ejemplo no se relaciona con la tesis?", "«Hoy hay sol»", "«Él sirve té»", "«Una joven le pregunta»", "El sol no se vincula con la soledad ni con el cuento."),
   ("ab", "{F} ¿Qué criterio incumple el comentario de ejemplo al no tener citas exactas?", "El criterio 2, argumentos con cita", "El criterio 5, cierre", "Sin cita exacta no cumple el segundo criterio."),
   ("abc", "{F} ¿Qué cita serviría para apoyar la tesis de soledad acompañada?", "«Hoy sí hacía falta»", "«un termo y dos tazas»", "«boca abajo»", "La frase final muestra que la segunda taza cobra sentido."),
   ("abc", "{F} ¿Qué conector sirve para empezar el cierre?", "Por eso", "Sin embargo", "Aunque", "Este conector marca la consecuencia final del comentario."),
   ("abc", "{F} ¿Qué tesis mejora la del ejemplo?", "El cuento muestra que compartir una taza puede acompañar la soledad", "El cuento es sobre té", "Don Aurelio tiene un termo", "Dice qué significa el gesto, no solo el tema."),
   ("ab", "{F} ¿Por qué conviene empezar la evaluación por lo logrado?", "Porque así la persona sabe qué conservar y siente respeto", "Porque no hay nada que mejorar", "Evaluar con respeto ayuda a aprender."),
   ("abc", "{F} Si debes comunicar el comentario en un minuto, ¿qué dices primero?", "La tesis", "El cierre", "El título del cuento solamente", "La tesis orienta lo que sigue."),
   ("abc", "{F} ¿Qué referente puede retomar «dar vuelta la taza» en el cierre?", "Ese gesto", "Aquella casa", "Mi barrio", "Este referente retoma una acción que ya se dijo."),
   ("ab", "{F} Si el comentario agrega «don Aurelio tiene un sombrero rojo», ¿mejora la coherencia?", "No, el dato no se relaciona con la tesis", "Sí, cualquier detalle ayuda", "Un detalle sin relación con la tesis desvía la atención.")],
  ("abc", "Te piden comentar el informe de un compañero de trabajo. ¿Cómo aplicas lo que aprendiste?", "Digo qué logró, qué falta y cómo corregirlo", "Digo que está mal sin explicar", "Lo copio", "La retroalimentación respetuosa es concreta y ayuda a mejorar."),
  [("En Lengua y Literatura: ¿qué cinco criterios tiene la pauta?", "Tesis, argumentos con cita, coherencia, cohesión y cierre", "Son los cinco criterios de hoy."),
   ("¿Qué hago después de evaluar un comentario?", "Lo reescribo para mejorar lo que falta", "Evaluar sirve para corregir y seguir aprendiendo."),
   ("¿Qué digo primero al comunicar el comentario en un minuto?", "La tesis", "La tesis guía todo lo demás que se dice.")],
  ("Aplica la pauta: {F} Reescribe el comentario de ejemplo para cumplir los cinco criterios (tesis clara, dos citas exactas, coherencia, conectores y referentes, cierre). Después escribe, en dos líneas, cómo lo dirías en voz alta en un minuto y qué criterio debes practicar más.",
   "Reescritura: «El cuento muestra que compartir una taza puede acompañar la soledad. Don Aurelio deja siempre una taza ‘boca abajo’; además, cuando la joven pregunta, sirve té y dice ‘Hoy sí hacía falta’. Por eso, ese gesto convierte la espera en compañía». Voz alta: digo la tesis, una cita y el cierre. Debo practicar los conectores.",
   ["cumple los cinco criterios", "citas exactas", "reflexiona sobre qué practicar"],
   ["un comentario reescrito y dos líneas de reflexión"],
   ["quedarse con menos criterios", "no explicar qué practicar"],
   "Pregunta: «¿Qué criterio de la pauta te cuesta más y por qué?»."),
  "Lee tu comentario reescrito en voz alta en un minuto, sin mirar el texto más de dos veces.",
  "Escribe un comentario de cuatro oraciones sobre otro cuento que hayas leído, aplicando la pauta.")
