from pathlib import Path
import json
R=Path(__file__).resolve().parents[1];c=json.loads((R/"curriculum/catalog.json").read_text(encoding="utf-8"));f=lambda n:f"{n:,}".replace(",",".")
(R/"README.md").write_text(f"""# 🇨🇱 Trayectoria Escolar Chile

**{f(c['class_count'])} clases planificadas · {f(c['objective_count'])} Objetivos de Aprendizaje · 1° básico a 4° medio**

Repositorio educativo abierto para planificar lo que niñas, niños y jóvenes aprenden durante su trayectoria escolar en Chile. Cada propuesta identifica nivel, asignatura, tema, OA oficial, cobertura y evidencia, y desarrolla el aprendizaje en 4 a 7 clases según su amplitud.

[Explorar clases](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) · [Malla completa](CURRICULUM.md) · [Textos y lecturas](BOOKS_AND_READINGS.md) · [Guía pedagógica](TEACHING_GUIDE.md)

## De OA a clases enseñables

Una lista curricular no es todavía una clase. Cada secuencia explica el contenido, anticipa vocabulario y errores, modela el razonamiento, propone práctica guiada e individual y termina con evidencia para decidir si avanzar, reenseñar o profundizar.

- **Dificultades:** ejemplos resueltos, pasos visibles, vocabulario anticipado, varias formas de respuesta y retiro gradual de apoyos, sin rebajar el OA.
- **Dominio temprano o aburrimiento:** comparación de estrategias, objeciones, casos límite y transferencia; profundizar no es entregar más ejercicios repetidos.
- **Realidad chilena:** alternativas sin conectividad, cursos numerosos y diversidad cultural, lingüística, sensorial y motriz; bloques adaptables a 45 o 90 minutos.
- **Trazabilidad:** cada OA enlaza su ficha de Currículum Nacional y conserva fecha de verificación.

## Alcance responsable

Incluye formación general común, propuestas MINEDUC, asignaturas según contexto y opciones de 3°–4° medio. Están etiquetadas y no representan una carga simultánea para cada estudiante. La dosificación es un punto de partida: el docente la ajusta con evidencia y el proyecto educativo.

Los Textos Escolares 2026 son recursos alineados. Las obras se denominan lecturas vinculadas o sugeridas cuando así aparecen en el portal; no se inventa obligatoriedad ni se reproducen obras protegidas.

## Uso

1. Elige nivel y asignatura.
2. Busca tema, eje, OA o palabra.
3. Revisa explicación y conocimientos previos.
4. Enseña la secuencia clase a clase.
5. Usa el ticket para mantener, acortar o ampliar la dosificación.

## Ecosistema

Se complementa con [Education, Pedagogy & Learning Sciences Program](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program), orientado a formación docente. Los programas especializados del perfil permiten continuar en matemática, computación, IA, datos, ciberseguridad, nube, negocios y creación digital; no sustituyen las Bases Curriculares.

Snapshot verificado el **{c['verified_at']}** desde [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/cursos-y-niveles). El catálogo registra **{c['reading_link_count']} enlaces de lectura** asociados por MINEDUC.

Proyecto independiente, sin representación del Ministerio de Educación de Chile.
""",encoding="utf-8")
(R/"TEACHING_GUIDE.md").write_text("""# Guía pedagógica

Cada OA se despliega en una secuencia variable. La primera clase diagnostica, las intermedias explican, practican y transfieren, y la última integra evidencia. No se avanza solo por calendario.

## Explicar con claridad
Presenta la idea central en lenguaje cotidiano, enseña vocabulario disciplinar y conecta ambos. Modela con ejemplo y contraejemplo; piensa en voz alta para revelar decisiones. Pide después reconstruir el razonamiento.

## Apoyar sin reducir
Mantén el OA y cambia el acceso: fragmenta instrucciones, usa apoyos visuales o concretos, permite ensayo oral, ofrece un ejemplo resuelto y retira apoyos gradualmente. La adecuación conserva la acción cognitiva.

## Profundizar
Cuando existe dominio, pide comparar métodos, explicar condiciones, construir un contraejemplo, evaluar una fuente o transferir. Evita más cantidad del mismo ejercicio y convertir siempre al estudiante en ayudante.

## Decidir con evidencia
- Logrado: aplica sin copiar y explica evidencia; continúa o profundiza.
- Próximo: conserva el foco y entrega apoyo puntual en grupo breve.
- Requiere otra explicación: cambia representación, ejemplo o vía de acceso y comprueba otra vez.
""",encoding="utf-8")
(R/"BOOKS_AND_READINGS.md").write_text(f"""# Textos escolares y lecturas

- **Bases Curriculares y OA:** definen aprendizajes esperados.
- **Textos Escolares MINEDUC:** recursos alineados para apoyar enseñanza.
- **Plan lector del establecimiento:** selección contextualizada.
- **Lecturas vinculadas por MINEDUC:** recursos asociados en fichas de OA; el portal mantiene lecturas sugeridas.

Se registraron **{c['reading_link_count']} enlaces** en fichas de Lenguaje y Lengua y Literatura. Un título puede aparecer varias veces. Su presencia no lo vuelve obligación nacional y su ausencia no impide una selección pertinente.

- [Catálogo Textos Escolares 2026](https://www.curriculumnacional.cl/noticias/ministerio-educacion-pone-disposicion-catalogo-textos-escolares-2026)
- [Portal Textos Escolares](https://www.curriculumnacional.cl/614/w3-propertyvalue-137118.html)
- [Lecturas sugeridas](https://www.curriculumnacional.cl/portal/Tipo/Lecturas/Lecturas-sugeridas/)
- [Biblioteca Digital Escolar](https://bdescolar.mineduc.cl/)

No se almacenan copias de libros ni fragmentos extensos.
""",encoding="utf-8")
(R/"METHODOLOGY.md").write_text("""# Metodología

El catálogo nace de un snapshot verificable de Currículum Nacional y conserva código, texto, eje, URL y cobertura. La dosificación comienza en cuatro clases y suma tiempo si el OA contiene varias acciones, tiene mayor extensión, exige investigación, creación, análisis, argumentación o interpretación, o incorpora lectura. Se limita a siete clases iniciales.

La heurística no reemplaza el diagnóstico docente. Los cambios de fuente requieren regeneración, validación y revisión humana.
""",encoding="utf-8")
(R/"OFFICIAL_REFERENCES.md").write_text("""# Fuentes oficiales

- [Cursos y niveles](https://www.curriculumnacional.cl/curriculum/cursos-y-niveles)
- [Bases Curriculares](https://www.curriculumnacional.cl/portal/Documentos-Curriculares/Bases-curriculares/)
- [Programas de estudio](https://www.curriculumnacional.cl/portal/Documentos-Curriculares/Programas/)
- [Textos Escolares 2026](https://www.curriculumnacional.cl/noticias/ministerio-educacion-pone-disposicion-catalogo-textos-escolares-2026)
- [Lecturas sugeridas](https://www.curriculumnacional.cl/portal/Tipo/Lecturas/Lecturas-sugeridas/)
- [Ley General de Educación](https://www.bcn.cl/leychile/navegar?idNorma=1006043)
- [Ley 17.336](https://www.bcn.cl/leychile/navegar?idNorma=28933)
""",encoding="utf-8")
print("written")

