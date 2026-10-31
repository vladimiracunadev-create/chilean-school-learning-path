"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 01 (sexualidad, pubertad, afectividad y responsabilidad) y OA 02 (formación de un nuevo individuo)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _x(items):
    return [ex(*i) if isinstance(i, tuple) else i for i in items]


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": w[0], "problem": w[1], "steps": w[2], "answer": w[3]} for w in worked],
        mistakes=[{"wrong": m[0], "why": m[1], "fix": m[2]} for m in mistakes],
        tiers={"recovery": _x(rec), "understand": _x(und), "apply": _x(app), "reason": _x(rea), "challenge": _x(cha)},
        context=_x(context), selfcheck=_x(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


OA1, OA2 = "CN07 OA 01", "CN07 OA 02"

# ---------------------------------------------------------------- OA 01
L(OA1, 1,
  materials="Este cuaderno y lápiz. Todos los casos son inventados y no corresponden a ninguna persona real; no necesitas contar nada personal.",
  use="Aprenderé qué cambios físicos ocurren en la pubertad y a separarlos de las ideas estereotipadas. Sirve para entender que cada cuerpo cambia a su propio ritmo.",
  prior=["Sé que el cuerpo cambia en la pubertad y que ese ritmo varía entre personas.", "Sé que una observación se puede contar o medir y una opinión no."],
  explain=[
      "La pubertad es la etapa en que el cuerpo madura y se hace capaz de reproducirse. Suele empezar entre los 8 y los 14 años aproximadamente, pero la edad exacta y la rapidez varían mucho. Dos personas sanas de la misma edad pueden estar en momentos muy distintos, y ambas son normales.",
      "Los cambios los dirigen las hormonas, que son mensajeros químicos que viajan por la sangre. Los ovarios y los testículos fabrican hormonas sexuales. Algunos cambios aparecen en todas las personas: estirón (aumento rápido de la estatura), vello en axilas y zona púbica, sudor más fuerte y acné. Otros son más propios de unas personas, como la primera menstruación o el cambio marcado de la voz.",
      "Un estereotipo es una idea simplificada que se repite sobre un grupo, como «los hombres no lloran» o «todas las niñas maduran antes». No se basa en datos y puede dañar a quien no encaja. Para distinguirlo de un hecho, se pregunta si se puede comprobar con observaciones y si vale para todas las personas.",
  ],
  vocab=[("pubertad", "etapa en que el cuerpo madura y puede reproducirse"), ("hormona", "mensajero químico que viaja por la sangre"), ("estirón", "aumento rápido de la estatura"), ("estereotipo", "idea simplificada y repetida sobre un grupo, sin datos que la sostengan"), ("ritmo individual", "velocidad propia con que cambia cada cuerpo")],
  worked=[
      ("Cambio físico o estereotipo", "Lee: (1) A Joaquín le salió vello en las axilas y su voz se hizo más grave. (2) «Los hombres no deben mostrar sus emociones». ¿Cuál es un cambio físico y cuál un estereotipo?", ["Pregunto si se puede observar en el cuerpo.", "La frase 1 describe cambios que se ven y se oyen.", "La frase 2 es una regla repetida que no se comprueba y no vale para todos."], "La frase 1 es cambio físico; la frase 2 es un estereotipo"),
      ("Ritmo individual", "Valentina midió 140 cm en enero y 149 cm en diciembre. Su amigo Tomás midió 132 cm en enero y 135 cm en diciembre (datos de ejemplo). ¿Cuánto creció cada uno y es raro que difieran?", ["Resto: Valentina 149 − 140 = 9 cm.", "Tomás 135 − 132 = 3 cm.", "Cada cuerpo crece a su ritmo; en un año distinto el orden puede cambiar."], "Valentina 9 cm y Tomás 3 cm; no es raro, el ritmo es individual"),
  ],
  mistakes=[
      ("Pensar que quien empieza la pubertad antes o después que sus amigos tiene un problema.", "La edad de inicio varía en un rango amplio.", "Compara con el rango habitual (8 a 14 años) y no con una sola persona."),
      ("Creer que una idea repetida por muchos es un hecho.", "Que muchos lo digan no prueba nada; un hecho se puede comprobar.", "Pregunta qué observación o dato la sostiene."),
  ],
  rec=[
      ("Completa: las hormonas viajan por la ______ (sangre o saliva).", "Sangre", "Son mensajeros que circulan por el sistema sanguíneo."),
      ("El estirón es un aumento rápido de la estatura. ¿Es un cambio físico o un estereotipo?", "Un cambio físico", "Se puede medir con una huincha."),
      ("¿Qué órganos fabrican las hormonas sexuales? A) Ovarios y testículos; B) Pulmones y riñones.", "A", "Los ovarios y los testículos fabrican las hormonas sexuales."),
  ],
  und=[
      ("Una persona de 10 años y otra de 13 empiezan la pubertad en momentos distintos, ambas dentro del rango habitual. ¿Qué explicación es correcta? A) A una de las dos le pasa algo grave; B) La edad de inicio varía y ambas pueden estar bien.", "B", "El rango habitual es amplio y las dos edades caen dentro de él."),
      ("«Las niñas siempre maduran antes que los niños y por eso son más responsables.» ¿Es un hecho comprobado o un estereotipo?", "Un estereotipo", "Generaliza a todas las personas y mezcla madurez física con responsabilidad sin datos."),
      ("¿Qué cambio ocurre en todas las personas durante la pubertad? A) Primera menstruación; B) Estirón.", "B", "El estirón aparece en mujeres y en hombres; la menstruación solo en quienes tienen útero y ovarios."),
  ],
  app=[
      arith("Un estudiante midió 148 cm al comenzar el año y 157 cm al terminarlo (datos de ejemplo). ¿Cuántos centímetros creció?", "157-148", "Se resta la estatura inicial a la final."),
      arith("Cuatro estudiantes notaron su primer cambio a los 9, 14, 11 y 12 años (datos de ejemplo). ¿Cuántos años separan al que empezó antes del que empezó después?", "14-9", "Se resta la edad menor a la mayor."),
      arith("Una niña medía 138 cm en enero y 143 cm en junio. Si crece lo mismo en el segundo semestre, ¿cuánto medirá en diciembre?", "143+(143-138)", "Creció 5 cm en el semestre, y se suma otro tanto."),
  ],
  rea=[
      ("Un afiche dice: «Si no tienes bigote a los 13, algo anda mal». Explica en una frase por qué es un estereotipo.", "Porque la edad en que aparece el vello facial varía mucho y no indica un problema", "El rango de inicio es amplio y no todas las personas siguen el mismo calendario."),
      ("Mateo (12 años) ya cambió la voz y Lucas (12 años) aún no. Un compañero dice que Lucas «no es normal». ¿Está justificada esa conclusión? Responde Sí o No.", "No", "A los 12 años aún está dentro del rango habitual de inicio."),
  ],
  cha=[
      ("Sofía crece mucho y le da vergüenza ir a Educación Física. ¿Cuál es la mejor respuesta de una amiga? A) «Cada cuerpo cambia a su ritmo; si quieres, hablamos con un adulto de confianza.» B) «No es importante, deja de pensar en eso.»", "A", "Reconoce el ritmo individual y ofrece apoyo; la B minimiza lo que siente Sofía."),
      ("Datos de ejemplo de 20 estudiantes: 3 notaron su primer cambio a los 10 años, 6 a los 11, 7 a los 12 y 4 a los 13. Alguien afirma: «Todos empiezan a los 12». ¿Es correcto? Responde Sí o No y da el número que lo prueba.", "No; solo 7 de 20", "Menos de la mitad empezó a los 12, así que la generalización falla."),
  ],
  context=[("Dato de ejemplo. En un curso de 40 estudiantes, 14 han notado ya cambios de la pubertad. ¿Cuántos aún no los notan?", "26", "40 − 14 = 26; es habitual que en un mismo curso haya ritmos distintos.")],
  selfcheck=[("¿Qué son las hormonas?", "Mensajeros químicos que viajan por la sangre", "Dirigen los cambios de la pubertad."), ("¿La pubertad empieza a la misma edad en todas las personas?", "No", "Hay un rango amplio de edades normales."), ("¿Cómo se distingue un estereotipo de un hecho?", "El hecho se comprueba con observaciones y vale en los casos medidos; el estereotipo repite una generalización sin datos", "Se pregunta qué observación la sostiene.")],
  open_task=task("Lee estas cuatro frases inventadas: (1) «A Pía le llegó el estirón y subió 8 cm en un año». (2) «Los niños deben ser fuertes y no pedir ayuda». (3) «A Nico le cambió la voz». (4) «Las niñas son más tímidas por naturaleza». Rotula cada una como cambio físico o estereotipo y reescribe una de las que sean estereotipo como una afirmación respetuosa.", "(1) Cambio físico. (2) Estereotipo. (3) Cambio físico. (4) Estereotipo. Reescritura de la 2: «Todas las personas, sin importar su género, pueden pedir ayuda cuando la necesitan».", ["rotula las cuatro frases", "justifica con 'se puede observar' o 'se generaliza'", "reescribe sin generalizar ni descalificar"], ["lista de cuatro rótulos y una frase reescrita"], ["tratar una opinión como un hecho", "reescribir con otro estereotipo"], "Pregunta qué dato o medición cambiaría su decisión sobre alguna frase."),
  reinforce="Escribe dos cambios físicos de la pubertad que aparecen en todas las personas.",
  extend="Explica por qué un estereotipo puede hacer sentir mal a alguien cuyo cuerpo cambia más tarde que el de sus amigos.")

L(OA1, 2,
  materials="Este cuaderno y lápiz. Los casos son inventados; no necesitas contar nada personal.",
  use="Aprenderé a distinguir las dimensiones biológica, afectiva y social de la sexualidad y a ver cómo se influyen. Sirve para buscar la ayuda adecuada ante una duda.",
  prior=["Sé que en la pubertad cambian el cuerpo y las emociones.", "Sé que un estereotipo es una idea simplificada sobre un grupo."],
  explain=[
      "La sexualidad es una parte de la vida de todas las personas y tiene tres dimensiones que se influyen entre sí. La dimensión biológica es el cuerpo: órganos, hormonas, cambios de la pubertad y reproducción. La dimensión afectiva son las emociones y los vínculos: cariño, gusto por alguien, vergüenza, confianza y amistad.",
      "La dimensión social incluye lo que rodea a la persona: la familia, el curso, las costumbres, las normas, los medios, las redes y las leyes. Las tres dimensiones se mezclan. Si cambian las hormonas (biológica), alguien puede sentir ánimos variables (afectiva) y recibir burlas de compañeros (social).",
      "Para analizar un caso se hacen tres preguntas: ¿qué pasa en el cuerpo?, ¿qué siente la persona?, ¿qué papel tienen otros, las normas o el ambiente? Mirar solo una dimensión deja ayudas fuera: explicar las hormonas no basta si el problema es una burla del curso.",
  ],
  vocab=[("dimensión biológica", "lo que ocurre en el cuerpo, como hormonas y órganos"), ("dimensión afectiva", "emociones y vínculos con otras personas"), ("dimensión social", "familia, normas, costumbres, medios y leyes que rodean a la persona"), ("vínculo", "relación de cariño o confianza entre personas"), ("influirse", "cambiar una cosa a otra")],
  worked=[
      ("Clasificar frases", "Clasifica cada frase en biológica, afectiva o social: (1) Los testículos producen hormonas sexuales. (2) Marta siente nervios al hablar con un compañero que le gusta. (3) Una norma del colegio prohíbe grabar a otros sin permiso.", ["Frase 1: habla de un órgano y una hormona.", "Frase 2: habla de una emoción hacia otra persona.", "Frase 3: habla de una norma que rige al grupo."], "1 biológica; 2 afectiva; 3 social"),
      ("Un caso con tres dimensiones", "Diego (12) dio un estirón y ahora es el más alto del curso. Se siente incómodo y algunos le dicen «gigante». Señala una frase de cada dimensión.", ["Biológica: dio un estirón.", "Afectiva: se siente incómodo.", "Social: algunos le dicen «gigante»."], "Biológica: estirón; afectiva: incomodidad; social: apodos del curso"),
  ],
  mistakes=[
      ("Pensar que la sexualidad es solo lo biológico.", "Las emociones y las relaciones también son parte de ella.", "Revisa siempre las tres dimensiones."),
      ("Creer que las dimensiones no se tocan entre sí.", "Una burla (social) puede cambiar lo que alguien siente (afectiva).", "Busca cómo una dimensión influye en las otras."),
  ],
  rec=[
      ("¿Qué dimensión trata de las emociones y los vínculos: la biológica, la afectiva o la social?", "La afectiva", "Incluye cariño, vergüenza, confianza y amistad."),
      ("«Los ovarios producen hormonas sexuales» pertenece a la dimensión: ¿biológica, afectiva o social?", "Biológica", "Habla de órganos y hormonas del cuerpo."),
      ("Verdadero o falso: las burlas de un grupo forman parte de la dimensión social.", "Verdadero", "Es lo que hacen otras personas del entorno."),
  ],
  und=[
      ("Clasifica: «Camila siente mucho cariño por su mejor amigo y confía en él». ¿Biológica, afectiva o social?", "Afectiva", "Habla de un sentimiento y de un vínculo."),
      ("¿Cuál es un ejemplo de dimensión social? A) Los medios muestran un único tipo de cuerpo como ideal; B) Aumenta la actividad de las glándulas del sudor.", "A", "Los medios son parte del entorno social; las glándulas son biológicas."),
      ("Un estudiante sufre burlas por su estirón (social), crece rápido (biológica) y siente vergüenza (afectiva). ¿Cuántas dimensiones están presentes?", "3", "Aparecen la biológica, la afectiva y la social."),
  ],
  app=[
      ("Cinco frases: (1) Los testículos aumentan de tamaño. (2) Ana extraña a su amiga que cambió de curso y se siente triste. (3) En las redes se comparten bromas sobre los cuerpos. (4) Pablo siente nervios antes de invitar a Rosa a bailar en el acto. (5) La voz de Pablo se volvió más grave. ¿Cuántas frases son afectivas?", "2", "Las frases 2 y 4 hablan de emociones hacia otras personas."),
      ("Con las mismas cinco frases (testículos que crecen, Ana triste, bromas en redes, Pablo nervioso, voz más grave), ¿cuántas son biológicas?", "2", "Las frases 1 y 5 hablan de cambios del cuerpo."),
      ("Con las mismas cinco frases, ¿cuál dimensión aparece solo una vez?", "La social", "Solo la frase 3 habla de lo que ocurre en el entorno (redes)."),
  ],
  rea=[
      ("Si una escuela explicara solo qué hormonas actúan en la pubertad, ¿qué quedaría sin atender? A) Cómo manejar las emociones y el respeto en el curso; B) Cuál es el nombre de las hormonas.", "A", "Solo se atendería la dimensión biológica."),
      ("¿Por qué una burla del curso (social) puede afectar lo que alguien siente (afectiva)? Responde en una frase.", "Porque lo que hacen otros influye en las emociones de la persona", "Las dimensiones se influyen entre sí."),
  ],
  cha=[
      ("Mateo está en la etapa de cambio de voz y, cuando canta, falla. Un compañero imita su voz y todos ríen, así que deja de cantar. ¿Qué acción atiende la dimensión social? A) Acordar en el curso que nadie imita ni se burla de la voz de otro; B) Explicarle a Mateo que su voz cambia por las hormonas.", "A", "Cambia el ambiente del grupo; explicar el cambio de voz atiende la dimensión biológica."),
      ("Alguien dice: «La sexualidad es solo biología». Usa el caso de Mateo para explicar en una frase por qué esa idea es incompleta.", "Porque en el caso también hay vergüenza (afectiva) y burlas del curso (social)", "Ese caso muestra que hay emociones y entorno, no solo un cambio del cuerpo."),
  ],
  context=[("Dato de ejemplo. En una encuesta anónima a 30 estudiantes, 12 dijeron que su mayor duda era sobre el cuerpo, 10 sobre cómo manejar las emociones y el resto sobre la presión del grupo. ¿Cuántos eligieron la presión del grupo?", "8", "30 − 12 − 10 = 8; esa duda es de la dimensión social.")],
  selfcheck=[("¿Cuáles son las tres dimensiones de la sexualidad?", "Biológica, afectiva y social", "Se influyen entre sí."), ("¿Qué incluye la dimensión social?", "Familia, normas, costumbres, medios, redes y leyes", "Es el entorno que rodea a la persona."), ("¿Por qué conviene mirar las tres dimensiones al analizar un caso?", "Porque mirar solo una deja ayudas fuera", "Los problemas suelen mezclar varias dimensiones.")],
  open_task=task("Lee este caso inventado: «Rocío (13) tuvo su estirón y ahora usa ropa suelta para esconder su cuerpo. Dos compañeros comentan sus cambios en el grupo del curso y ella ya no quiere ir a clases de Educación Física». Escribe una frase por dimensión (biológica, afectiva, social) y una acción concreta que el curso podría hacer desde la dimensión social.", "Biológica: tuvo un estirón. Afectiva: siente vergüenza y se esconde. Social: dos compañeros comentan sus cambios en el grupo. Acción: acordar que no se comenta el cuerpo de nadie en el grupo.", ["una frase por dimensión", "acción concreta y respetuosa", "no culpa a Rocío"], ["tres frases y una acción"], ["poner una frase en la dimensión equivocada", "proponer una acción que expone a Rocío"], "Pregunta cómo cambiaría su acción si el comentario viniera de una persona adulta."),
  reinforce="Escribe una frase de cada dimensión sobre cualquier situación inventada del recreo.",
  extend="Explica con un ejemplo cómo un cambio biológico puede desencadenar una emoción y una reacción social.")

L(OA1, 3,
  materials="Este cuaderno y lápiz. Los casos son inventados y no corresponden a nadie real.",
  use="Aprenderé qué es el respeto mutuo y el consentimiento en una relación afectiva. Sirve para reconocer cuándo una situación es respetuosa y cuándo hay presión o falta de cuidado.",
  prior=["Sé que las personas tienen derecho a decidir sobre su cuerpo.", "Sé que debo avisar a una persona adulta de confianza cuando algo me incomoda."],
  explain=[
      "En una relación afectiva, como una amistad cercana o un pololeo, el respeto mutuo significa tratar al otro como igual: escuchar, aceptar sus límites, no burlarse y no controlar. Aceptar un «no» es la señal más clara de respeto.",
      "El consentimiento es un acuerdo libre, claro y voluntario para hacer algo con otra persona, como un abrazo, compartir una foto o un mensaje. Es libre si no hay presión, chantaje (amenaza o culpa para forzar), engaño ni miedo. Se puede retirar en cualquier momento. El silencio no es un «sí», y quien está asustado, dormido o bajo efecto de alcohol o drogas no puede consentir.",
      "El cuidado mutuo incluye proteger la intimidad del otro: no compartir fotos ni mensajes privados sin permiso. Si alguien presiona, controla o hace sentir mal, no es culpa de quien lo vive. Lo correcto es decir «no», alejarse y avisar a una persona adulta de confianza, como un familiar, un docente o la orientadora.",
  ],
  vocab=[("respeto mutuo", "trato digno en ambas direcciones, aceptando los límites del otro"), ("consentimiento", "acuerdo libre, claro y voluntario que se puede retirar"), ("chantaje", "presión con una amenaza o con culpa para obligar a alguien"), ("intimidad", "lo privado de una persona, como su cuerpo, fotos y mensajes"), ("persona adulta de confianza", "adulto que escucha y ayuda, como un familiar, docente u orientador")],
  worked=[
      ("¿Hay consentimiento?", "Raúl le pide un abrazo a Ema. Ella dice «prefiero no». Raúl insiste: «Dale, no seas pesada». ¿Hay consentimiento?", ["Busco si la respuesta es un acuerdo libre.", "Ema dijo que no.", "Raúl insistió con presión, que impide un acuerdo libre."], "No hay consentimiento; Raúl debe respetar el «no»"),
      ("Respeto o control", "En un pololeo, Ana revisa el celular de Luis cada noche y le prohíbe hablar con sus amigos. En otro, Bea y Nico se avisan dónde van y cada uno ve a sus amigos. ¿Cuál muestra respeto mutuo?", ["Reviso si hay control o libertad.", "Ana controla y prohíbe.", "Bea y Nico respetan los espacios del otro."], "El de Bea y Nico"),
  ],
  mistakes=[
      ("Pensar que si alguien no dice nada, está de acuerdo.", "El silencio puede ser miedo o confusión; un «sí» debe ser claro.", "Pregunta y acepta solo un acuerdo claro y libre."),
      ("Creer que quien dijo «sí» una vez no puede cambiar de idea.", "El consentimiento se puede retirar en cualquier momento.", "Respeta el cambio de opinión de inmediato."),
  ],
  rec=[
      ("Si alguien dice «no», ¿qué debes hacer: respetarlo o insistir?", "Respetarlo", "Aceptar un «no» es la señal de respeto más clara."),
      ("¿Se puede retirar el consentimiento después de haberlo dado?", "Sí", "El acuerdo puede cambiar en cualquier momento."),
      ("¿El silencio es un «sí»: verdadero o falso?", "Falso", "Un acuerdo debe ser claro; callar puede ser miedo."),
  ],
  und=[
      ("¿Cuál es una presión que impide el consentimiento libre? A) «Si no lo haces, cuento tu secreto a todos.» B) «Si quieres, dime; si no, no importa.»", "A", "La amenaza es un chantaje; la B deja libertad."),
      ("¿Qué conducta muestra cuidado mutuo? A) Pedir permiso antes de subir una foto de un amigo; B) Subir la foto porque salió bien.", "A", "La foto es parte de su intimidad y necesita su permiso."),
      ("Alguien escribe: «Si me quisieras, me mandarías esa foto». ¿Es un chantaje afectivo o una muestra de amistad?", "Un chantaje afectivo", "Usa la culpa para presionar y quita la libertad de decidir."),
  ],
  app=[
      ("Lista de conductas: (1) preguntar antes de abrazar, (2) revisar el celular de otro sin permiso, (3) aceptar que el otro no quiera una foto, (4) amenazar con contar un secreto, (5) respetar que el otro vea a sus amigos. ¿Cuántas muestran respeto mutuo?", "3", "Son la 1, la 3 y la 5."),
      ("Marcos siente que lo presionan para hacer algo que no quiere. Según la clase, la secuencia es: (a) contar a una persona adulta de confianza, (b) decir «no» con claridad, (c) alejarse de la situación. ¿Con qué letra parte esa secuencia?", "b", "Primero se expresa el límite y luego se aleja y pide ayuda."),
      ("Gabriela dio permiso para sacarle una foto en una actividad, pero luego pide que la borren. ¿Qué debe hacer la otra persona? A) Borrarla porque retiró el permiso; B) Guardarla porque ya había dicho sí.", "A", "El consentimiento se puede retirar."),
  ],
  rea=[
      ("Pedro dijo «sí» porque su compañero lo amenazó con contar algo que lo avergüenza. ¿Fue consentimiento? Responde Sí o No.", "No", "No fue libre, porque hubo amenaza."),
      ("Alguien dice: «Antes lo permitió, ahora tiene que aceptar». Explica en una frase por qué es incorrecto.", "Porque el consentimiento se puede retirar en cualquier momento", "Permitir una vez no obliga a permitir siempre."),
  ],
  cha=[
      ("En un grupo de mensajes alguien comparte una foto privada de una compañera sin permiso. ¿Cuál es la mejor acción? A) No reenviarla, apoyar a la compañera y avisar a una persona adulta de confianza; B) Reenviarla a un amigo para que se entere.", "A", "Reenviar aumenta el daño; avisar protege a la compañera."),
      ("Un chico se siente presionado de forma repetida por otro de su curso. ¿A quién puede recurrir? Escribe una persona adulta de confianza.", "A una persona adulta de confianza, como un familiar, un docente o la orientadora", "Un adulto de confianza puede ayudar a detener la presión."),
  ],
  context=[("Dato de ejemplo. En una encuesta anónima a 25 estudiantes, 17 dijeron sentirse cómodos al decir «no» a un amigo. ¿Cuántos no se sienten cómodos?", "8", "25 − 17 = 8; esa dificultad se trabaja practicando cómo decir «no».")],
  selfcheck=[("¿Qué tres características tiene el consentimiento?", "Es libre, claro y voluntario, y se puede retirar", "Sin presión ni engaño."), ("¿Qué debes hacer si te presionan para algo que no quieres?", "Decir «no», alejarte y avisar a una persona adulta de confianza", "No es tu culpa y no debes enfrentarlo solo."), ("¿Qué es el chantaje?", "Presionar con una amenaza o con culpa para obligar a alguien", "Impide que el acuerdo sea libre.")],
  open_task=task("Lee este caso inventado: «Lola y Ismael son amigos cercanos. Ismael le pide a Lola que le muestre sus mensajes privados con otras personas para demostrar que confía en él; si no, dice que se enojará». Marca qué parte es presión, explica por qué no hay consentimiento libre y escribe una respuesta respetuosa que Lola podría dar.", "Presión: «si no, se enojará». No es libre porque usa el enojo para obligar. Respuesta: «Mis mensajes son privados; confío en ti y no necesito mostrártelos».", ["identifica la presión", "explica por qué no es libre", "respuesta clara y respetuosa"], ["tres frases escritas"], ["decir que Lola debe ceder para evitar problemas", "responder con agresión"], "Pregunta a quién podría contarle Lola si Ismael insiste."),
  reinforce="Escribe dos frases que muestren aceptación de un «no».",
  extend="Explica por qué el silencio no basta como consentimiento y da un ejemplo cotidiano.")

L(OA1, 4,
  materials="Este cuaderno y lápiz. Los casos son inventados; no necesitas contar nada personal.",
  use="Aprenderé un método para tomar decisiones responsables sobre mi cuerpo y mis relaciones sin exponer información personal. Sirve para pensar antes de actuar y saber cuándo pedir ayuda.",
  prior=["Sé que el consentimiento es libre, claro y voluntario.", "Sé que puedo pedir ayuda a una persona adulta de confianza."],
  explain=[
      "La responsabilidad individual es hacerse cargo de las decisiones propias y de sus consecuencias, para uno mismo y para otros. Una decisión responsable se toma con información y sin apuro. Un método de seis pasos ayuda: 1) nombrar la decisión, 2) informarse en fuentes confiables, 3) pensar las consecuencias, 4) mirar los propios valores y límites, 5) decidir, 6) pedir ayuda si hay dudas o presión.",
      "Las fuentes confiables son profesionales de salud, docentes, orientadores y materiales de organismos de salud. Un rumor del recreo, un video anónimo o la frase «todos lo hacen» no son fuentes confiables. Las consecuencias pueden ser físicas, emocionales y sociales, y algunas aparecen de inmediato y otras mucho después.",
      "La presión del grupo es un empuje a decidir como los demás. Responsable es poder decir «no» o «todavía no», y cambiar de opinión. No hace falta contar detalles personales para pedir ayuda: se puede preguntar en general, de forma anónima o con un caso inventado.",
  ],
  vocab=[("responsabilidad individual", "hacerse cargo de las propias decisiones y sus consecuencias"), ("fuente confiable", "persona o material con información comprobada, como un profesional de salud"), ("consecuencia", "resultado de una decisión"), ("presión del grupo", "empuje a decidir como los demás"), ("valores", "ideas de lo que una persona considera importante y correcto")],
  worked=[
      ("Aplicar los pasos", "Joaquín (13) escucha en el recreo que «todos ya tuvieron pololeo» y que quien no, es raro. Debe decidir si se apura. Aplica los pasos.", ["Paso 2: el rumor no es una fuente confiable y no hay datos.", "Paso 3: apurarse por presión puede traer incomodidad y arrepentimiento.", "Pasos 4 a 6: decide esperar hasta sentirse listo y puede hablar con un adulto de confianza."], "Esperar hasta sentirse listo; no es verdad que «todos» lo hayan hecho"),
      ("Mensaje de un desconocido", "Bea recibe un mensaje de una persona desconocida que le pide fotos suyas. Decide qué hacer.", ["Identifico el riesgo: pedir fotos a un menor es una señal de peligro.", "No hay obligación de responder.", "Corresponde no responder, bloquear y avisar a una persona adulta de confianza."], "No responder, bloquear y avisar a un adulto de confianza"),
  ],
  mistakes=[
      ("Decidir porque «todos lo hacen».", "Lo que hacen otros no mide si es bueno ni si estás listo.", "Revisa tus valores, la información y las consecuencias."),
      ("Callarse la presión por vergüenza.", "Pedir ayuda protege; no hacerlo deja la presión sin resolver.", "Habla con una persona adulta de confianza."),
  ],
  rec=[
      ("¿Cuál es una fuente confiable: un profesional de salud o un rumor del recreo?", "Un profesional de salud", "Su información está comprobada."),
      ("Completa: el último paso del método es pedir ______ si hay dudas o presión.", "Ayuda", "Es el paso 6."),
      ("Verdadero o falso: se puede cambiar de opinión antes de decidir.", "Verdadero", "Es parte de decidir con calma."),
  ],
  und=[
      ("¿Qué paso del método consiste en pensar qué puede pasar después de decidir? A) Informarse; B) Pensar las consecuencias.", "B", "Ese es el paso 3."),
      ("La frase «todos lo hacen» sirve como argumento para decidir. ¿Verdadero o falso?", "Falso", "No es una fuente de información ni mide si estás listo."),
      ("Ordena por tiempo de aparición: (a) una molestia emocional que dura meses, (b) la vergüenza al instante. ¿Cuál aparece primero?", "La b", "La vergüenza ocurre de inmediato y el malestar prolongado aparece después."),
  ],
  app=[
      ("Elena dice: «Quiero informarme sobre cómo cuidarme». Tiene cuatro opciones: un video anónimo, un profesional de salud, el rumor de un compañero y una orientadora del colegio. ¿Cuántas son fuentes confiables?", "2", "Son el profesional de salud y la orientadora."),
      ("Un mensaje dice: «Pasa tu ubicación exacta y tu dirección para ganar un premio». ¿Qué paso del método usarías? A) Pedir ayuda a un adulto antes de responder; B) Responder rápido para no perder el premio.", "A", "Hay un riesgo y se necesita ayuda; la rapidez no es un valor responsable."),
      ("Al decidir, se te ocurren tres consecuencias posibles de una acción: dos negativas y una positiva. ¿Cuántas consecuencias hay en total?", "3", "Se cuentan todas, positivas y negativas."),
  ],
  rea=[
      ("Un compañero te presiona con «si no lo haces, eres cobarde». ¿Cuál es una respuesta responsable? A) «Todavía no quiero y está bien.» B) «Está bien, lo hago para que no se enoje.»", "A", "Mantiene tu límite y no cede a la presión."),
      ("Si dudas de una información que leíste, ¿qué conviene hacer primero: compartirla o contrastarla con una fuente confiable?", "Contrastarla con una fuente confiable", "Así evitas difundir un error."),
  ],
  cha=[
      ("Dos estudiantes de 7.º preguntan al orientador de forma anónima: «¿cómo sé si estoy listo para una relación afectiva?». ¿Qué ventaja tiene preguntar de forma anónima? A) No expone datos personales; B) Garantiza que la respuesta sea siempre correcta.", "A", "Permite resolver la duda sin revelar quién es."),
      ("En una fiesta inventada, Pía piensa: «Si me quedo, quizá sienta presión; si me voy, quedaré tranquila». Usa el paso 3 y 4 y decide. ¿Qué decisión protege más su bienestar?", "Irse", "Evita la presión y respeta su límite."),
  ],
  context=[("Dato de ejemplo. De 30 estudiantes, 6 dicen haber vivido presión de un grupo para hacer algo que no querían. ¿Qué porcentaje del curso es?", "20", "6 × 100 ÷ 30 = 20, o sea 20 %.")],
  selfcheck=[("Nombra tres pasos del método de decisión.", "Por ejemplo: informarse, pensar las consecuencias y pedir ayuda", "Son pasos del método."), ("¿Qué hacer si sientes presión?", "Decir «no» o «todavía no» y pedir ayuda a una persona adulta de confianza", "Protege tu decisión."), ("¿Por qué «todos lo hacen» no es un buen argumento?", "Porque no es información comprobada ni mide si estás listo", "Cada persona decide con sus valores.")],
  open_task=task("Un compañero inventado, Ian (13), dice: «En mi grupo todos hablan de tener pareja y se ríen de quienes no». Aplica a su caso los seis pasos del método: escribe una oración por paso, sin pedir ni dar datos personales reales.", "1 Decidir si se apura. 2 Preguntar a la orientadora. 3 Puede sentir presión o arrepentimiento. 4 Revisa que quiere ir a su ritmo. 5 Decide esperar. 6 Habla con un adulto de confianza.", ["seis pasos en orden", "una fuente confiable", "decisión coherente con sus valores"], ["seis oraciones"], ["omitir el paso de pedir ayuda", "usar el rumor como fuente"], "Pregunta qué haría si el grupo insistiera y a quién acudiría."),
  reinforce="Escribe una fuente confiable y una no confiable de información sobre salud.",
  extend="Explica con un ejemplo por qué una consecuencia puede aparecer tiempo después de la decisión.")

L(OA1, 5,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo, inventados, de cursos ficticios.",
  use="Aprenderé a contrastar una afirmación sobre pubertad, afectividad y responsabilidad con datos. Sirve para decidir si una frase está apoyada, contradicha o si faltan datos.",
  prior=["Sé que hay tres dimensiones de la sexualidad.", "Sé que un estereotipo no se apoya en datos."],
  explain=[
      "Contrastar una explicación con datos es preguntarse si los datos la apoyan, la contradicen o no alcanzan para decidir. Primero se lee el dato sin interpretar. Luego se compara con la afirmación. Por ejemplo, «la pubertad empieza siempre a los 12» se contradice si en una lista hay edades de 9 a 14 años.",
      "Para leer una lista de edades se usan tres resultados simples. El rango es la diferencia entre el valor mayor y el menor. La moda es el valor que más se repite. El conteo dice cuántos casos cumplen una condición. Con ellos se puede describir sin exagerar.",
      "Todo conjunto de datos tiene límites. Una encuesta a un solo curso o a pocas personas no representa a todo el país. Una conclusión prudente dice qué muestran los datos y reconoce lo que no pueden mostrar. Los casos de esta clase son ejemplos inventados.",
  ],
  vocab=[("apoyar", "mostrar que una afirmación es compatible con los datos"), ("contradecir", "mostrar que una afirmación no coincide con los datos"), ("rango", "diferencia entre el mayor y el menor valor"), ("moda", "valor que más se repite"), ("muestra", "grupo pequeño de datos tomado de un grupo mayor")],
  worked=[
      ("Leer una lista de edades", "Edades en que 8 estudiantes ficticios notaron su primer cambio: 10, 11, 11, 12, 12, 12, 13, 14. Calcula el rango y la moda.", ["Rango: 14 − 10 = 4.", "La moda es el valor que más se repite: 12 aparece 3 veces.", "Ningún otro valor se repite tanto."], "Rango 4 años; moda 12 años"),
      ("Contrastar una frase", "Con esa misma lista, ¿qué pasa con la frase «todos notaron su primer cambio a los 12»?", ["Cuento cuántos tienen 12: tres de ocho.", "La frase dice «todos».", "Cinco de ocho notaron el cambio en otra edad."], "La contradice: solo 3 de 8 notaron el cambio a los 12"),
  ],
  mistakes=[
      ("Concluir sobre «todos» a partir de pocos casos.", "Una muestra pequeña no representa a todas las personas.", "Limita la conclusión a las personas medidas."),
      ("Decir que los datos prueban una idea cuando solo no la contradicen.", "No contradecir no es probar.", "Distingue entre apoyar, contradecir y no alcanzar."),
  ],
  rec=[
      ("¿Qué es el rango de 8, 11 y 14 años: 6 años o 11 años?", "6 años", "14 − 8 = 6."),
      ("En la lista 9, 10, 10, 12, ¿cuál es la moda?", "10", "El 10 aparece dos veces; es el valor que más se repite."),
      ("Una afirmación que no coincide con los datos, ¿se apoya o se contradice?", "Se contradice", "Contradecir es no coincidir con los datos."),
  ],
  und=[
      ("Datos: 12 de 15 estudiantes de un curso ficticio dicen haber aprendido sobre pubertad de su familia. ¿La frase «la mayoría aprendió de su familia» se apoya o se contradice?", "Se apoya", "12 de 15 es más de la mitad."),
      ("¿Por qué una encuesta a un solo curso no permite hablar de todos los jóvenes de Chile? A) Porque es una muestra pequeña; B) Porque las encuestas no sirven.", "A", "Un curso no representa a todo el país."),
      ("Lista de edades: 9, 11, 11, 12, 14. ¿Qué frase está apoyada? A) La edad de inicio varía; B) Todos empiezan a los 11.", "A", "Hay edades desde 9 hasta 14."),
  ],
  app=[
      arith("Edades: 10, 10, 11, 11, 11, 12, 12, 13. ¿Cuál es el rango en años?", "13-10", "Se resta la menor a la mayor."),
      ("Encuesta ficticia a 40 estudiantes sobre dónde se informan: familia 15, docentes 10, redes 9, amigos 6. ¿Cuál fuente es la más mencionada?", "La familia", "15 es el valor más alto."),
      arith("Con esa misma encuesta de 40 estudiantes (familia 15, docentes 10, redes 9, amigos 6), ¿cuántos mencionan fuentes distintas a las redes?", "40-9", "Se resta la cifra de redes del total."),
  ],
  rea=[
      ("En una encuesta ficticia a 40 estudiantes (familia 15, docentes 10, redes 9, amigos 6), alguien afirma: «La mayoría se informa por redes». ¿Se apoya o se contradice? Explica en una frase.", "Se contradice; solo 9 de 40", "9 de 40 es menos de la mitad."),
      ("Un compañero afirma: «Con esa encuesta sé qué aprenden todos los jóvenes de Chile». ¿Qué límite tiene la afirmación?", "La muestra es de un solo curso y no representa a todos", "Una muestra pequeña no sirve para generalizar."),
  ],
  cha=[
      ("Dos cursos ficticios respondieron si saben a quién pedir ayuda: curso A, 21 de 30 estudiantes (7 de cada 10); curso B, 12 de 20 estudiantes (6 de cada 10). ¿En qué curso es mayor la proporción que sabe? A) Curso A; B) Curso B.", "A", "7 de cada 10 es mayor que 6 de cada 10, aunque el curso B tenga menos estudiantes."),
      ("Redacta una conclusión prudente para esta lista de edades ficticias: 9, 10, 11, 11, 12, 12, 12, 13, 14.", "La edad de inicio varía entre 9 y 14 años y la más frecuente es 12 en este grupo", "Describe rango y moda sin exagerar."),
  ],
  context=[("Dato de ejemplo. En un curso de 36 estudiantes, 27 dicen que preferirían hacer preguntas de forma anónima. ¿Cuántos prefieren otra forma?", "9", "36 − 27 = 9.")],
  selfcheck=[("¿Qué significa contrastar con datos?", "Ver si los datos apoyan, contradicen o no alcanzan para una afirmación", "Es el paso final de explicar con evidencia."), ("¿Qué es la moda?", "El valor que más se repite", "Se cuenta en la lista."), ("¿Por qué hay que declarar los límites?", "Porque una muestra pequeña no representa a todos", "Evita exagerar la conclusión.")],
  open_task=task("Con las edades ficticias de primer cambio de 12 estudiantes: 9, 10, 10, 11, 11, 11, 12, 12, 12, 12, 13, 14, calcula el rango y la moda, y contrasta estas dos frases: (a) «La pubertad empieza siempre a los 11». (b) «La edad de inicio varía». Escribe una conclusión con un límite.", "Rango: 14 − 9 = 5 años. Moda: 12. (a) Se contradice: solo 3 de 12 tienen 11. (b) Se apoya: hay edades de 9 a 14. Conclusión: en este grupo ficticio la edad varía, pero 12 jóvenes no representan a todos.", ["calcula rango y moda", "contrasta cada frase", "declara un límite"], ["cálculos y tres frases"], ["generalizar a todos", "confundir moda con rango"], "Pregunta qué dato nuevo haría más fuerte la conclusión."),
  reinforce="Calcula el rango de la lista 12, 9, 14, 11.",
  extend="Explica cómo cambiaría tu conclusión si agregaras 10 estudiantes más con edades entre 8 y 15.")

# ---------------------------------------------------------------- OA 02
L(OA2, 1,
  materials="Este cuaderno y lápiz. El ciclo de ejemplo es un modelo de 28 días; no corresponde a ninguna persona ni sirve para calcular el ciclo real de nadie.",
  use="Aprenderé las fases del ciclo menstrual, cuándo ocurre la ovulación y qué es la ventana fértil en un modelo. Sirve para entender cómo el cuerpo se prepara cada mes para un posible embarazo.",
  prior=["Sé que los ovarios producen ovocitos y hormonas.", "Sé que la pubertad trae la primera menstruación."],
  explain=[
      "El ciclo menstrual es una serie de cambios que se repite aproximadamente cada mes en los ovarios y el útero. Se cuenta desde el primer día de la menstruación, que es la salida de sangre y tejido del endometrio (la capa interna del útero) y dura entre 3 y 7 días. Luego un ovocito madura en un ovario.",
      "La ovulación es la liberación del ovocito. En el modelo de un ciclo de 28 días ocurre cerca del día 14. El ovocito vive unas 12 a 24 horas, y los espermatozoides pueden sobrevivir hasta 5 días en el cuerpo femenino. Lo más estable es que la ovulación ocurre unos 14 días antes de la siguiente menstruación. Por eso la ventana fértil, los días en que puede haber fecundación, va en este modelo desde 5 días antes de la ovulación hasta 1 día después. Es decir, de los días 9 al 15.",
      "Si no hay fecundación, bajan las hormonas, el endometrio se desprende y empieza otro ciclo. Los ciclos reales varían de persona en persona y, en la adolescencia, suelen ser irregulares. Por eso un calendario no basta para predecir los días fértiles de nadie.",
  ],
  vocab=[("ciclo menstrual", "serie de cambios mensuales en ovarios y útero"), ("menstruación", "salida de sangre y tejido del endometrio por la vagina"), ("ovulación", "liberación de un ovocito desde el ovario"), ("endometrio", "capa interna del útero"), ("ventana fértil", "días en que puede ocurrir fecundación")],
  worked=[
      ("Leer el modelo", "En el modelo de 28 días, la menstruación ocupa los días 1 a 5 y la ovulación es el día 14. ¿Cuántos días pasan desde que termina la menstruación hasta la ovulación?", ["La menstruación termina el día 5.", "La ovulación ocurre el día 14.", "Resto: 14 − 5 = 9 días."], "9 días"),
      ("Calcular la ventana fértil", "Si la ovulación del modelo es el día 14, ¿cuáles son los días de la ventana fértil (5 días antes hasta 1 día después)?", ["5 días antes: 14 − 5 = día 9.", "1 día después: 14 + 1 = día 15.", "La ventana va del 9 al 15."], "Del día 9 al día 15, o sea 7 días"),
  ],
  mistakes=[
      ("Creer que un calendario permite saber con exactitud los días fértiles de una adolescente.", "Los ciclos reales varían y suelen ser irregulares al comienzo.", "Usa el modelo solo para entender; no para predecir."),
      ("Confundir menstruación con ovulación.", "La menstruación es la salida del endometrio; la ovulación es la salida del ovocito.", "Recuerda: menstruación = sangre; ovulación = ovocito."),
  ],
  rec=[
      ("¿Qué se libera del ovario en la ovulación?", "Un ovocito", "Es la célula sexual femenina."),
      ("¿Cómo se llama la capa interna del útero que se desprende en la menstruación?", "Endometrio", "Se prepara cada mes para un posible embarazo."),
      ("En el modelo de 28 días, ¿en qué día aproximado ocurre la ovulación: día 14 o día 3?", "Día 14", "Ocurre cerca de la mitad del ciclo."),
  ],
  und=[
      ("¿Cuánto vive el ovocito después de la ovulación? A) Unas 12 a 24 horas; B) Unos 5 días.", "A", "Los 5 días corresponden a los espermatozoides."),
      ("¿Por qué la ventana fértil comienza 5 días antes de la ovulación?", "Porque los espermatozoides pueden sobrevivir hasta 5 días", "Pueden esperar al ovocito en el cuerpo femenino."),
      ("Si no hay fecundación, ¿qué ocurre con el endometrio? A) Se desprende y empieza otro ciclo; B) Se mantiene igual y no cambia.", "A", "Al bajar las hormonas, el endometrio se elimina en la menstruación."),
  ],
  app=[
      arith("En un ciclo de ejemplo de 30 días, la ovulación ocurre 14 días antes del próximo ciclo. ¿En qué día ocurre?", "30-14", "Se resta de la duración del ciclo."),
      arith("Con una ovulación el día 16 del ciclo de ejemplo, ¿en qué día comienza la ventana fértil (5 días antes)?", "16-5", "Se resta 5 al día de ovulación."),
      arith("Si en otro modelo la ovulación es el día 16, ¿cuántos días dura la ventana fértil (desde 5 días antes hasta 1 día después)? Cuenta ambos extremos.", "(16+1)-(16-5)+1", "Del 11 al 17 hay 7 días incluyendo los dos extremos."),
  ],
  rea=[
      ("Una joven dice: «Como mi ciclo dura exactamente 28 días, sé que soy fértil el día 14». Explica en una frase por qué esa seguridad es débil.", "Porque los ciclos reales varían y la ovulación puede ocurrir en otro día", "Un modelo no predice un ciclo real."),
      ("Un ovocito vive 1 día y los espermatozoides 5. ¿Por qué hay más días fértiles antes de la ovulación que después? Responde en una frase.", "Porque los espermatozoides pueden esperar varios días al ovocito", "Su supervivencia es más larga."),
  ],
  cha=[
      ("Modelo A: ciclo de 28 días con ovulación el día 14. Modelo B: ciclo de 35 días con ovulación el día 21. ¿En cuál modelo la ventana fértil (5 días antes hasta 1 día después) termina más tarde? A) Modelo A; B) Modelo B.", "B", "En B termina el día 22 y en A, el día 15."),
      ("Datos ficticios de tres ciclos: 26, 31 y 29 días. ¿Cuál es la diferencia entre el ciclo más largo y el más corto?", "5", "31 − 26 = 5 días; muestra que el ciclo varía."),
  ],
  context=[("Dato de ejemplo. Una ficha de un colegio dice que en un ciclo de 28 días la menstruación dura 5 días. ¿Cuántos días del ciclo no hay menstruación?", "23", "28 − 5 = 23 días.")],
  selfcheck=[("¿Qué ocurre en la ovulación?", "Un ovario libera un ovocito", "Ocurre cerca de la mitad del ciclo."), ("¿Por qué los ciclos reales no se pueden predecir con un calendario?", "Porque varían y pueden ser irregulares", "Sobre todo en la adolescencia."), ("¿Qué es la ventana fértil?", "Los días en que puede ocurrir la fecundación", "Incluye los días antes y después de la ovulación.")],
  open_task=task("Dibuja en tu cuaderno una línea de 28 casillas numeradas del 1 al 28 y pinta (o escribe una letra en cada casilla): los días 1 a 5 con rojo (menstruación), el día 14 con azul (ovulación) y los días 9 a 15 con un borde verde (ventana fértil). Escribe qué muestra el modelo y qué no muestra.", "Línea de 28 casillas con los días 1 a 5 en rojo, el 14 en azul y el 9 al 15 con borde verde. Muestra el orden de las fases; no muestra los ciclos reales, que varían.", ["28 casillas bien numeradas", "marca las tres zonas", "declara un límite del modelo"], ["dibujo y dos frases"], ["marcar la ovulación el día 5", "decir que el modelo sirve para predecir"], "Pregunta qué cambiaría si el ciclo durara 32 días."),
  reinforce="Escribe en qué se diferencian menstruación y ovulación.",
  extend="Explica por qué las hormonas son necesarias para que el ciclo ocurra en orden.")

L(OA2, 2,
  materials="Este cuaderno y lápiz. Las cifras son aproximadas y se explican en cada ejercicio.",
  use="Aprenderé cómo se unen un espermatozoide y un ovocito, qué es la fecundación y cómo se inicia el desarrollo. Sirve para explicar cómo se forma un nuevo individuo.",
  prior=["Sé que el ovocito sale del ovario en la ovulación.", "Sé que los testículos producen espermatozoides."],
  explain=[
      "Un nuevo individuo se forma cuando un espermatozoide se une a un ovocito. Los dos son células sexuales o gametos. Cada gameto lleva 23 cromosomas, que son estructuras con la información hereditaria. Los espermatozoides se producen en los testículos y tienen una cola para moverse; el ovocito es grande y trae reservas, y no se mueve por sí solo.",
      "La fecundación es la unión de un espermatozoide con un ovocito y ocurre normalmente en la trompa de Falopio, el tubo que une el ovario con el útero. Se forma el cigoto, una célula con 46 cromosomas (23 de cada gameto). Durante unos 5 a 6 días el cigoto se divide varias veces mientras avanza hacia el útero.",
      "Cuando llega al útero, la bola de células se pega al endometrio, donde recibe oxígeno y nutrientes de la madre. Eso se llama implantación y ocurre aproximadamente una semana después de la fecundación. Desde ese momento comienza el embarazo y no se produce la menstruación. Sin fecundación, el ovocito se pierde y el ciclo continúa.",
  ],
  vocab=[("gameto", "célula sexual: espermatozoide u ovocito"), ("fecundación", "unión de un espermatozoide con un ovocito"), ("cigoto", "primera célula del nuevo individuo, con 46 cromosomas"), ("trompa de Falopio", "tubo que une el ovario con el útero"), ("implantación", "unión de la bola de células al endometrio")],
  worked=[
      ("Contar cromosomas", "Un espermatozoide tiene 23 cromosomas y un ovocito, 23. ¿Cuántos tiene el cigoto?", ["Se suman los de cada gameto.", "23 + 23 = 46."], "46 cromosomas"),
      ("Contar divisiones", "El cigoto es 1 célula. Se divide en 2, luego esas 2 se dividen en 4. Si sigue así, ¿cuántas células hay después de 3 divisiones?", ["Cada división duplica el número de células.", "1 → 2 → 4 → 8."], "8 células"),
  ],
  mistakes=[
      ("Pensar que el ovocito y el espermatozoide tienen 46 cromosomas cada uno.", "Cada gameto trae 23; solo al unirse suman 46.", "Recuerda: 23 + 23 = 46."),
      ("Creer que la fecundación ocurre en el útero.", "Ocurre normalmente en la trompa de Falopio.", "El útero recibe la bola de células para la implantación."),
  ],
  rec=[
      ("¿Cuántos cromosomas tiene un ovocito?", "23", "Cada gameto lleva la mitad de la información."),
      ("¿Cómo se llama la primera célula del nuevo individuo?", "Cigoto", "Resulta de la fecundación."),
      ("¿Dónde se producen los espermatozoides: en los testículos o en los ovarios?", "En los testículos", "Los ovarios producen ovocitos."),
  ],
  und=[
      ("¿Dónde ocurre normalmente la fecundación? A) En la trompa de Falopio; B) En el endometrio.", "A", "El endometrio recibe la bola de células después, para la implantación."),
      ("¿Qué diferencia hay entre fecundación e implantación? A) La fecundación es la unión de gametos y la implantación es la unión al endometrio; B) Son el mismo proceso.", "A", "Ocurren en lugares y momentos distintos."),
      ("Si no hay fecundación, ¿qué ocurre con el ovocito? Responde: se pierde o forma un embrión.", "Se pierde", "Sin espermatozoide no se forma un cigoto."),
  ],
  app=[
      arith("Un cigoto de 1 célula se divide 4 veces seguidas, duplicando el número de células en cada división. ¿Cuántas células hay?", "1*2*2*2*2", "Se duplica cuatro veces."),
      arith("La fecundación ocurre el día 1 y la implantación el día 7. ¿Cuántos días pasan entre ambas?", "7-1", "Se resta el día de la fecundación al de la implantación."),
      ("Una persona tiene 46 cromosomas en cada célula del cuerpo, pero cada gameto lleva 23. ¿Qué pasaría si los gametos llevaran 46? A) El cigoto tendría 92; B) El cigoto tendría 23.", "A", "46 + 46 = 92, por eso cada gameto debe llevar solo la mitad."),
  ],
  rea=[
      ("Un amigo dice: «El espermatozoide y el ovocito se parecen en tamaño». Corrígelo con una característica del ovocito.", "El ovocito es mucho más grande y trae reservas; el espermatozoide es pequeño y tiene cola", "Son células muy distintas."),
      ("¿Por qué la bola de células debe implantarse en el endometrio para que siga el desarrollo? Responde en una frase.", "Porque ahí recibe nutrientes y oxígeno de la madre", "El endometrio le da alimento y protección."),
  ],
  cha=[
      ("Un cigoto empieza a dividirse en la trompa y avanza hacia el útero. Si se implantara en la trompa en vez del útero, ¿el desarrollo sería seguro? Responde Sí o No y explica.", "No; la trompa no está preparada para sostener el embarazo", "El útero es el órgano preparado para el desarrollo."),
      ("Un ovocito es fecundado por un espermatozoide en el día 15 de un ciclo. Estima en qué día del ciclo ocurre aproximadamente la implantación si tarda 7 días. Escribe el número.", "22", "15 + 7 = 22."),
  ],
  context=[("Dato de ejemplo. Un esquema muestra al cigoto avanzando por la trompa durante 6 días antes de llegar al útero, y la implantación 1 día después. ¿Cuántos días pasan desde la fecundación hasta la implantación?", "7", "6 + 1 = 7 días.")],
  selfcheck=[("¿Qué es la fecundación?", "La unión de un espermatozoide con un ovocito", "Forma el cigoto."), ("¿Cuántos cromosomas tiene el cigoto?", "46", "23 del espermatozoide y 23 del ovocito."), ("¿Qué es la implantación?", "La unión de la bola de células al endometrio", "Desde ahí empieza el embarazo.")],
  open_task=task("Dibuja y rotula una secuencia de cinco pasos: (1) ovulación, (2) fecundación en la trompa, (3) cigoto, (4) divisiones, (5) implantación en el endometrio. Escribe al lado de cada paso un dato: dónde ocurre y qué se forma.", "1 Ovario libera un ovocito. 2 Fecundación en la trompa. 3 Cigoto con 46 cromosomas. 4 Divisiones: 2, 4, 8 células. 5 Implantación en el útero a la semana.", ["cinco pasos en orden", "lugar de cada paso", "dato correcto en cada paso"], ["dibujo rotulado"], ["poner la fecundación en el útero", "olvidar el cigoto"], "Pregunta qué habría pasado si el ovocito no hubiera sido fecundado."),
  reinforce="Escribe la secuencia: ovulación, fecundación, cigoto, implantación, con una frase cada una.",
  extend="Explica por qué la unión de dos gametos con 23 cromosomas da un cigoto con 46.")

L(OA2, 3,
  materials="Este cuaderno y lápiz. Las semanas de la línea de tiempo están escritas en los ejercicios.",
  use="Aprenderé la diferencia entre embrión y feto y las etapas de la gestación. Sirve para entender cómo se forma un bebé y por qué los controles de salud son importantes.",
  prior=["Sé que el cigoto se implanta en el útero.", "Sé que la gestación dura unos 9 meses."],
  explain=[
      "La gestación es el tiempo de desarrollo dentro del útero y dura alrededor de 40 semanas (unos 9 meses). Se divide en tres trimestres: el primero va hasta la semana 13, el segundo de la 14 a la 27 y el tercero de la 28 hasta el parto.",
      "Hasta la semana 8 se habla de embrión. En esa etapa se forman los órganos principales, el corazón comienza a latir y aparecen los brazos y las piernas. Desde la semana 9 hasta el nacimiento se habla de feto, que crece, madura sus órganos y se mueve. Hacia el final practica movimientos de respiración, traga líquido y reacciona a sonidos. Las semanas de esta clase son una simplificación escolar.",
      "El feto se nutre por la placenta, un órgano que une el útero con el cordón umbilical. Por ella pasan oxígeno y nutrientes hacia el feto y salen desechos. El líquido amniótico lo protege de golpes. Algunas sustancias, como el alcohol y el tabaco, pueden pasar por la placenta y dañar el desarrollo; por eso los controles de salud durante el embarazo son importantes.",
  ],
  vocab=[("gestación", "tiempo de desarrollo dentro del útero"), ("embrión", "etapa hasta la semana 8, cuando se forman los órganos"), ("feto", "etapa desde la semana 9 hasta el nacimiento"), ("placenta", "órgano que intercambia oxígeno, nutrientes y desechos entre madre y feto"), ("trimestre", "cada período de tres meses de la gestación")],
  worked=[
      ("Embrión o feto", "A la semana 6 de desarrollo, ¿se habla de embrión o de feto?", ["Hasta la semana 8 se habla de embrión.", "6 es menor que 8."], "Embrión"),
      ("Trimestre de una semana", "¿En qué trimestre está la semana 20?", ["Primer trimestre: hasta la semana 13.", "Segundo trimestre: semanas 14 a 27.", "20 está en el segundo."], "Segundo trimestre"),
  ],
  mistakes=[
      ("Usar «embrión» y «feto» como si fueran lo mismo.", "Cambia la etapa: embrión hasta la semana 8 y feto desde la 9.", "Ubica la semana antes de nombrar la etapa."),
      ("Creer que la sangre de la madre y la del feto se mezclan directamente.", "El intercambio ocurre en la placenta, a través de paredes delgadas.", "Recuerda que la placenta es el lugar de intercambio."),
  ],
  rec=[
      ("¿Cuánto dura la gestación: 40 semanas o 12 semanas?", "40 semanas", "Son unos 9 meses."),
      ("¿Qué órgano permite el intercambio de oxígeno y nutrientes: la placenta o el estómago?", "La placenta", "Une el útero con el cordón umbilical."),
      ("A la semana 12, ¿hay embrión o feto?", "Feto", "Desde la semana 9 se habla de feto."),
  ],
  und=[
      ("¿Qué ocurre en la etapa de embrión? A) Se forman los órganos principales; B) El feto ya está listo para nacer.", "A", "El embrión llega hasta la semana 8."),
      ("¿Para qué sirve el líquido amniótico? A) Protege al feto de golpes; B) Fabrica sus huesos.", "A", "Amortigua los movimientos y golpes."),
      ("¿Por qué el alcohol es peligroso en el embarazo?", "Porque pasa por la placenta y puede dañar el desarrollo", "La placenta no lo filtra."),
  ],
  app=[
      ("¿En qué trimestre está la semana 30?", "Tercer trimestre", "Del trimestre 28 hasta el parto."),
      arith("Un embarazo dura 40 semanas. Si hoy van 25 semanas, ¿cuántas semanas faltan?", "40-25", "Se resta lo transcurrido del total."),
      arith("Del inicio de la semana 9 al final de la semana 40, ¿cuántas semanas dura la etapa de feto? Cuenta ambas.", "40-9+1", "La etapa fetal cubre desde la semana 9 hasta la 40."),
  ],
  rea=[
      ("Una persona dice: «A la semana 5 el bebé ya es feto». Corrige la frase usando el número de semanas.", "Hasta la semana 8 es embrión", "El nombre depende de la semana."),
      ("¿Por qué el control médico durante la gestación ayuda al desarrollo del feto? Responde en una frase.", "Porque permite detectar problemas y cuidar nutrición y salud", "Los controles dan información y prevención."),
  ],
  cha=[
      ("Una línea de tiempo marca hitos: semana 6 el corazón comienza a latir, semana 10 el feto mueve brazos, semana 30 aumenta de peso. ¿Cuántos de esos hitos ocurren en la etapa de embrión?", "1", "Solo la semana 6 es de embrión; la 10 y la 30 corresponden a feto."),
      ("Un amigo dice: «Si la placenta no funcionara bien, el feto no recibiría suficiente oxígeno». ¿Está bien razonado? Responde Sí o No y explica.", "Sí; la placenta entrega el oxígeno", "Es el órgano de intercambio."),
  ],
  context=[("Dato de ejemplo. Un afiche del consultorio dice: «El primer control debe hacerse cuanto antes». Si una persona se hace su primer control en la semana 10, ¿en qué trimestre está?", "Primer trimestre", "La semana 10 es anterior a la 13.")],
  selfcheck=[("¿Qué diferencia hay entre embrión y feto?", "Embrión hasta la semana 8; feto desde la semana 9", "Cambia la etapa del desarrollo."), ("¿Cuántas semanas dura la gestación?", "Alrededor de 40", "Unos 9 meses."), ("¿Qué hace la placenta?", "Intercambia oxígeno, nutrientes y desechos", "Une al feto con la madre.")],
  open_task=task("Dibuja una línea de tiempo de 40 semanas y marca: semana 8 (fin de embrión), semana 13 (fin del primer trimestre), semana 27 (fin del segundo) y semana 40 (parto). Escribe debajo una cosa que el control de salud protege.", "Línea de 40 semanas con cuatro marcas. Protección: detectar problemas a tiempo y cuidar la nutrición.", ["cuatro marcas correctas", "etapas rotuladas", "una función del control"], ["línea de tiempo"], ["marcar el embrión hasta la semana 13", "olvidar un trimestre"], "Pregunta por qué el nombre cambia de embrión a feto."),
  reinforce="Escribe qué cambia entre la semana 8 y la semana 9.",
  extend="Explica por qué la placenta es importante para que el feto crezca.")

L(OA2, 4,
  materials="Este cuaderno y lápiz. Los casos son inventados; no necesitas contar nada personal.",
  use="Aprenderé cómo funcionan los métodos de control de la natalidad y qué significa una paternidad y maternidad responsables. Sirve para saber dónde informarse con fuentes sanitarias.",
  prior=["Sé que el embarazo comienza con la fecundación y la implantación.", "Sé que una fuente confiable es un profesional de salud."],
  explain=[
      "Los métodos de control de la natalidad ayudan a decidir si se quiere un embarazo y cuándo. Los de barrera, como el preservativo, impiden que el espermatozoide llegue al ovocito. Los hormonales, como la píldora, el implante o el inyectable, evitan la ovulación. El dispositivo intrauterino (DIU) impide la fecundación. La vasectomía y la ligadura de trompas son procedimientos médicos pensados como permanentes.",
      "La abstinencia, que es no tener relaciones sexuales, es la única forma de evitar por completo el embarazo y también evita las ITS que se transmiten por relaciones sexuales. De los métodos que se usan durante una relación sexual, solo el preservativo, usado bien, reduce además el riesgo de infecciones de transmisión sexual (ITS). Ningún método es perfecto: funciona mejor cuando se usa de forma correcta y con orientación de un profesional de salud.",
      "La paternidad y la maternidad responsables significan que ambos progenitores se hacen cargo del cuidado, la educación, el afecto y los gastos de un hijo, y que la decisión de tenerlo se toma con información. En Chile los centros de salud familiar entregan orientación. Ser madre o padre exige tiempo, salud y recursos, por lo que conviene planificar.",
  ],
  vocab=[("método anticonceptivo", "forma de evitar un embarazo"), ("barrera", "método que impide el encuentro entre espermatozoide y ovocito"), ("hormonal", "método que evita la ovulación con hormonas"), ("abstinencia", "no tener relaciones sexuales"), ("paternidad y maternidad responsables", "hacerse cargo del cuidado, afecto y gastos de un hijo, tomando decisiones informadas")],
  worked=[
      ("Clasificar un método", "¿Cómo actúa el preservativo y cuál es su ventaja adicional?", ["Es un método de barrera: impide que el espermatozoide llegue al ovocito.", "Además reduce el riesgo de infecciones de transmisión sexual.", "Esa ventaja no la tienen los hormonales ni el DIU."], "Es de barrera y también reduce el riesgo de ITS"),
      ("Comparar acción", "¿Qué hace la píldora anticonceptiva y en qué se diferencia del preservativo?", ["La píldora es hormonal: evita la ovulación.", "El preservativo es de barrera.", "Actúan por mecanismos distintos."], "La píldora evita la ovulación; el preservativo impide el encuentro de los gametos"),
  ],
  mistakes=[
      ("Creer que cualquier método protege también contra infecciones de transmisión sexual.", "Entre los métodos que se usan en una relación sexual, solo el preservativo reduce ese riesgo.", "Revisa qué protege cada método."),
      ("Informarse de métodos con el rumor de un amigo.", "La información debe venir de un profesional de salud.", "Pregunta en un centro de salud o a la orientadora."),
  ],
  rec=[
      ("¿Qué método impide que el espermatozoide llegue al ovocito: la barrera o el DIU?", "La barrera", "Es lo que hace el preservativo."),
      ("¿Cuál es la única forma de evitar por completo el embarazo: la abstinencia o la píldora?", "La abstinencia", "Sin relaciones sexuales no llega el espermatozoide al ovocito."),
      ("¿Qué método reduce además el riesgo de ITS: el preservativo o la píldora?", "El preservativo", "Es de barrera."),
  ],
  und=[
      ("¿Cómo actúa un método hormonal? A) Evita la ovulación; B) Impide la entrada de aire al útero.", "A", "Sin ovocito liberado no hay fecundación."),
      ("La vasectomía y la ligadura de trompas se consideran de tipo permanente. ¿Verdadero o falso?", "Verdadero", "Son procedimientos médicos pensados como permanentes."),
      ("¿Dónde conviene informarse sobre métodos? A) En un centro de salud con un profesional; B) En un video anónimo.", "A", "La fuente debe ser un profesional de salud."),
  ],
  app=[
      ("De estos cuatro métodos: píldora, preservativo, implante y vasectomía, ¿cuántos actúan evitando la ovulación con hormonas?", "2", "Son la píldora y el implante; el preservativo es de barrera y la vasectomía es un procedimiento médico."),
      ("Una pareja inventada piensa tener un hijo. ¿Qué acción corresponde a una paternidad y maternidad responsables? A) Hablar con un profesional de salud y planificar los gastos; B) Decidir sin información para no perder tiempo.", "A", "La decisión informada y la planificación son parte de la responsabilidad."),
      ("¿Qué ventaja tiene usar un método y un control médico juntos? A) Mayor información y seguridad; B) Se evita toda enfermedad.", "A", "Un profesional ayuda a elegir y usar bien el método."),
  ],
  rea=[
      ("Un amigo dice: «Tomé la píldora, así que estoy protegido contra las ITS». Corrígelo en una frase.", "La píldora evita la ovulación pero no protege contra infecciones de transmisión sexual", "Solo el preservativo reduce ese riesgo."),
      ("Dos estudiantes discuten si «la responsabilidad es solo de la madre». Escribe una frase que corrija esa idea.", "Ambos progenitores comparten el cuidado y los gastos", "La paternidad y la maternidad responsables involucran a los dos."),
  ],
  cha=[
      ("Un afiche dice: «Un método anticonceptivo siempre funciona al 100 %». ¿Es correcto? Responde Sí o No y explica.", "No; ningún método es perfecto y depende del uso correcto", "Los métodos fallan si se usan mal."),
      ("Una orientadora presenta la siguiente tabla ficticia: preservativo (barrera, protege ITS), píldora (hormonal, no protege ITS), DIU (impide la fecundación, no protege ITS). Si alguien quiere reducir el riesgo de ITS, ¿qué método elegiría de esa tabla?", "El preservativo", "Es el único de la tabla que protege contra ITS."),
  ],
  context=[("Dato de ejemplo. Un centro de salud inventado atendió 60 consultas de adolescentes en un mes: 24 por métodos de control de natalidad, 18 por controles generales y el resto por otras razones. ¿Cuántas fueron por otras razones?", "18", "60 − 24 − 18 = 18.")],
  selfcheck=[("¿Qué hacen los métodos hormonales?", "Evitan la ovulación", "No se libera ovocito."), ("¿Qué método reduce el riesgo de ITS?", "El preservativo", "Es de barrera."), ("¿Qué significa paternidad y maternidad responsables?", "Hacerse cargo del cuidado, el afecto y los gastos tomando decisiones informadas", "Ambos progenitores participan.")],
  open_task=task("Construye una tabla de tres columnas (método, cómo actúa, si protege contra ITS) con estos cuatro métodos: preservativo, píldora, DIU, abstinencia. Escribe después dos recomendaciones para alguien que tiene dudas, sin dar datos personales.", "Preservativo: barrera, sí. Píldora: evita ovulación, no. DIU: impide fecundación, no. Abstinencia: no hay relaciones sexuales, sí evita las ITS de transmisión sexual. Recomendaciones: consultar a un profesional de salud; no usar rumores.", ["tabla completa", "información correcta", "dos recomendaciones sin datos personales"], ["tabla y dos frases"], ["afirmar que la píldora protege contra ITS", "dar un caso personal real"], "Pregunta por qué ningún método reemplaza la orientación profesional."),
  reinforce="Escribe tres métodos anticonceptivos y cómo actúa cada uno.",
  extend="Explica por qué la planificación es parte de la maternidad y la paternidad responsables.")
