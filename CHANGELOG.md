# Changelog

## 2026-10-03 · Centro visible de evaluaciones y ensayos conectados

- Se amplía la documentación de los trece instrumentos o familias: definición, motivo de existencia, historia, antecesores, responsable, primera aplicación, periodicidad, diseño, lectura de resultados, límites y uso docente, siempre con fuentes institucionales.
- Se incorporan dos omisiones del panorama anterior: **Impulso Lector 2026**, separado de SIMCE y organizado en precursores, comprensión y fluidez, y la familia de **Estudios Nacionales** muestrales de lectura, escritura, formación ciudadana, inglés y competencias técnico-profesionales.
- Los ensayos originales pasan de 37 a 45 variantes; los ocho ejemplos nuevos conservan cálculo didáctico 0–4, criterios visibles, clases existentes, intervención y reevaluación, sin simular escalas oficiales.
- Las páginas dejan de ofrecer una lista genérica de OA: cada variante incorpora una ruta visual **preparar → enseñar/practicar → comprobar**, con nombre del contenido, clase existente exacta, fase, evidencia, intervención y reevaluación.
- El estado del Prompt Maestro pasa de quince etiquetas resumidas a una matriz completa de treinta bloques con evidencia visible, resultado concreto y trabajo pendiente.
- El diseño web incorpora navegación interna, datos esenciales, líneas de tiempo, tarjetas de antecedentes, paneles de resultados/límites y rutas curriculares adaptables a móvil.
- Se crea una entrada inequívoca llamada **Evaluaciones complementarias** desde la portada, la documentación, competencias y los doce niveles; ya no es necesario conocer la palabra técnica “marcos”.
- PAES, SIMCE, DIA, PISA, TIMSS, PIRLS, ERCE, ICILS, ICCS, ECES y evaluación interna tienen páginas identificables con propósito, población, documentos institucionales, estado real y límites.
- Cada variante escolar documentada enlaza OA, contenidos y clases existentes como referencias pedagógicas; comprensión lectora reúne PAES Lectora, SIMCE Lectura, DIA, PISA Lectura, PIRLS y ERCE sin tratarlas como equivalentes.
- Se publican 45 miniensayos originales con clave, rúbrica, cálculo interactivo de 0 a 4 puntos y decisión posterior; ningún resultado se convierte artificialmente en escala oficial.
- Las descargas pasan de 49 a 51 PDF: se agregan una guía docente de instrumentos/brechas/estado y una compilación completa de los 45 ensayos.
- El informe de brechas previo se conserva como línea base histórica y se añade un estado actual que indica brecha cerrada, parcial y acción pendiente, además de una tabla explícita para todos los bloques del prompt maestro.
- Markdown enlaza documentación Markdown; HTML enlaza páginas HTML. Los JSON permanecen como soporte técnico y no como interfaz docente.

## 2026-10-02 · Competencias y marcos legibles para docentes

- Los archivos JSON dejan de ser la interfaz pública: permanecen como fuente técnica validada, mientras habilidades, progresiones, marcos y tareas se presentan en páginas pedagógicas navegables.
- Se publica una respuesta directa sobre PAES, SIMCE, PISA, TIMSS y PIRLS que distingue qué se implementó, qué relación es oficial o inferida, cuántas tareas existen y qué afirmaciones no corresponden.
- Las seis tareas originales ahora tienen fichas completas con estímulo, consigna, respuesta, solución explicada, criterios, rúbrica, prerrequisitos, OA y enlaces a clases existentes.
- El README y el centro documental enlazan guías Markdown para docentes; el sitio enlaza sus equivalentes HTML, sin obligar a interpretar identificadores técnicos.
- La validación automática impide que las vistas docentes vuelvan a enlazar JSON como lectura principal o exhiban tipos internos sin traducir.

## 2026-10-02 · Novedades públicas sin caché obsoleta

- La portada solicita `catalog.json` y `updates.json` sin reutilizar respuestas almacenadas, de modo que una publicación nueva sea visible inmediatamente después del despliegue.
- El generador calcula una versión corta desde `app.js`, `catalog.json` y `updates.json`; `index.html` la agrega tanto al script como a cada solicitud de datos, por lo que el CDN no puede confundir una publicación nueva con la anterior.
- La validación automática comprueba el contrato de actualización tanto en el script como en la portada y evita que vuelva a publicarse un sitio que oculte contenido reciente.
- Se conserva el historial completo: esta corrección no sustituye ni reescribe las entradas que explican la capa longitudinal y el flujo de formatos.

## 2026-10-02 · Flujo versionado y estándares Markdown, HTML y PDF

- Se documenta el ciclo completo fuente → versión → regeneración → validación → `main` → CI → GitHub Pages, incluyendo responsables, estados, rollback y comprobación posterior al despliegue.
- Se establece Markdown como representación canónica de lectura; los enlaces internos Markdown→Markdown y HTML→HTML pasan a verificarse en todo el repositorio, sin mezclar superficies.
- Los 3.047 documentos Markdown quedan sujetos a un contrato visual automatizado: UTF-8, un solo H1, jerarquía de títulos, bloques cercados balanceados, enlaces no vacíos y navegación interna coherente.
- Las 49 compilaciones PDF se declaran salidas derivadas del Markdown canónico, con versión documental visible, metadatos, índice, marcadores, enlaces, fuentes únicas y validación de lectura; nunca se editan manualmente.

## 2026-10-02 · README principal con mapa de la capa longitudinal

- El README principal enumera ahora el contenido nuevo con sus cifras verificables y sus fuentes editables: 86 habilidades, 6 progresiones, 36 etapas, 43 enlaces a 37 OA distintos, 5 relaciones interdisciplinarias, 8 patrones de error y 6 tareas originales.
- Se documenta la conexión completa `LE04 OA 04` → clases existentes → progresión → habilidades → tarea → observación → posible patrón → intervención con el mismo OA → reevaluación en una situación nueva.
- Se distingue en el punto de entrada del repositorio qué proviene del currículo oficial, qué es una inferencia pedagógica revisable y qué es una propuesta propia del proyecto.
- La validación automática exige que el README conserve el inventario, las fuentes y la explicación de reutilización; una futura ampliación no puede quedar oculta solo en archivos técnicos.

## 2026-10-02 · Competencias, evidencia y evaluación longitudinal

- Se agrega una taxonomía transversal versionada y seis progresiones demostrativas desde 1° básico hasta 4° medio, enlazadas a OA y clases existentes sin modificar el currículo.
- Se incorporan un banco inicial de tareas originales, esquemas JSON, patrones de error, intervenciones y un ciclo determinista de observación, hipótesis, práctica, reevaluación y transferencia.
- PAES, SIMCE, PISA, TIMSS, PIRLS y evaluaciones internas se modelan como marcos desacoplados con fuente, versión, alcance, limitaciones y correspondencias pedagógicas explícitamente inferidas.
- Se publica una vista web para estudiantes y docentes, con evidencia sintética trazable y sin porcentajes de dominio ficticios.
- CI, Pages y controles de seguridad se separan en workflows con permisos mínimos, acciones fijadas por SHA, matrices de Python y verificación de reproducibilidad.
- La portada publica automáticamente las tres novedades más recientes con fecha, resumen y acceso al historial; CI impide que esta vista quede desincronizada del changelog.

## 2026-10-01 · Apps de apoyo del aprendizaje en 5° básico

- Se analizan Pañuelo al Viento, Mi Aventura con el Violín y Mi Aventura con la Guitarra antes de integrarlas como recursos opcionales para niñas y niños alrededor de los 10 años.
- Se modifican siete clases de 5° básico: dos de `EF05 OA 05` y cinco de Música (`MU05 OA 01`, `03`, `04`, `07` y `08`), sin alterar los conteos curriculares.
- Cada integración declara propósito, mediación adulta o docente, evidencia válida, límites y una alternativa equivalente sin aplicación, dispositivo o instrumento propio.
- Se publica una guía de correspondencia curricular y se incorpora la misma información en las fichas Markdown, las guías de asignatura y GitHub Pages.

## 2026-10-01 · Enumeraciones completas en el README

- La sección “De dónde sale el contenido” incorpora las reconstrucciones de 3° y 4° medio, sus cifras, fuentes oficiales y separación entre OA oficial y explicación pedagógica interna.
- Una nueva validación estructural exige los doce índices de nivel en cada sección del README que presenta un recorrido completo; una enumeración truncada ya no puede pasar CI.
- Se conserva el historial anterior sin reescribir afirmaciones fechadas.

## 2026-10-01 · Coherencia integral del README y el syllabus

- Se corrige la contradicción del README que ubicaba las 8.841 clases desarrolladas y las 4.156 experiencias integradas dentro de “No es”, pese a declararlas como estado actual en el resto de la documentación.
- Las rutas docentes, el procedimiento de uso, la lista documental y el pie del README incluyen ahora 3° y 4° medio, sin terminar artificialmente en 2° medio.
- El syllabus completa su estructura por nivel desde 7° básico hasta 4° medio con OA, clases, integraciones y enlaces a las 149 guías verificables.
- Los validadores comprueban que el README no vuelva a contradecir sus cifras actuales y que las superficies principales mantengan alcance, terminología y enlaces coherentes.

## 2026-10-01 · Conteos inequívocos y explicación OA por OA en 3° y 4° medio

- Se corrige la terminología vigente: 12.997 corresponde a registros pedagógicos, compuestos por 8.841 clases disciplinares y 4.156 experiencias de integración transversal; estas últimas no son clases independientes.
- Las 18 guías de 3° medio y las 17 de 4° medio incorporan explicación pedagógica para cada OA: significado para la enseñanza, punto de entrada, conceptos explícitos, progresión, evidencia y fuente oficial.
- Los índices de ambos niveles explicitan qué está resuelto —desarrollo interno y 0 pendientes— y qué continúa pendiente: revisión profesional, pilotaje y certificación externa.
- El índice curricular distingue clases, experiencias integradas y propuestas pendientes, y los validadores impiden que vuelvan a omitirse las explicaciones OA por OA.

## 2026-10-01 · 4° medio completo y trayectoria escolar cerrada

- Desarrollo de los 91 OA de Formación General de 4° medio en 466 clases pedagógicas distribuidas en diecisiete denominaciones curriculares.
- Cada ficha conserva la fuente oficial del OA y distingue la prescripción curricular de la progresión, los criterios, los recursos y las decisiones pedagógicas internas.
- El catálogo queda en 8.841 clases desarrolladas y 4.156 experiencias integradas: 12.997 propuestas, 2.823 OA y 0 pendientes desde 1° básico hasta 4° medio.
- Publicación del índice de nivel, mapa técnico, vista web y diecisiete guías de asignatura de 4° medio, con continuidad explícita desde 3° medio y orientación de egreso.
- Sincronización de documentación vigente, plan maestro, portal, cobertura, estado editorial, roadmap, metodología, pruebas y validadores. La revisión profesional y el pilotaje de aula continúan pendientes.

## 2026-10-01 · 3° medio completo

- Desarrollo de los 85 OA y 419 clases restantes en dieciséis denominaciones de Formación General, conservando los 13 OA y 76 clases ya desarrollados de Matemática y Lengua y Literatura.
- 3° medio alcanza 98 OA, 495 clases desarrolladas, dieciocho guías de asignatura y 0 propuestas pendientes.
- Cada ficha enlaza su OA oficial de Currículum Nacional y separa la fuente oficial de la progresión, los criterios y las decisiones pedagógicas internas.
- Estado global actualizado a 8.375 clases desarrolladas y 4.156 experiencias integradas; las 466 propuestas pendientes corresponden a 4° medio.
- Sincronización de catálogo, plan maestro, portal, cobertura, estado editorial, roadmap, metodología, pruebas y validadores. La revisión humana y el pilotaje continúan pendientes.

## 2026-10-01 · Matemática y Lengua y Literatura de 3° medio

- Desarrollo de los 4 OA de Matemática de Formación General en 17 clases sobre números complejos, incerteza y probabilidad condicional, modelos exponenciales y logarítmicos y relaciones métricas de la circunferencia.
- Desarrollo de los 9 OA de Lengua y Literatura en 59 clases sobre interpretación y efecto estético, géneros discursivos y comunidades digitales, recursos multimodales, producción, diálogo e investigación ética.
- Cada ficha conserva la fuente oficial del OA y distingue los criterios de progresión pedagógica interna; el nivel mantiene 419 propuestas pendientes y revisión humana pendiente.
- Publicación del índice parcial, mapa técnico, vista web y dos guías de asignatura de 3° medio, con continuidad explícita desde 2° medio.
- Estado global actualizado a 7.956 clases desarrolladas y 4.156 experiencias integradas; quedan 885 propuestas pendientes entre 3° y 4° medio.

## 2026-09-30 · 2° medio completo

- Se completaron Ciencias Naturales, Historia, Inglés e Inglés (Propuesta) con 374 clases disciplinares y 217 experiencias integradas nuevas.
- Se completaron Artes Visuales, Música, Educación Física y Salud, Orientación y Tecnología con 169 clases disciplinares y 117 experiencias integradas nuevas.
- 2° medio alcanza 744 clases desarrolladas, 456 experiencias integradas y 0 propuestas pendientes en sus once denominaciones.
- El proyecto suma 7.880 clases desarrolladas y 4.156 experiencias integradas; desde 1° básico hasta 2° medio hay diez niveles consecutivos con desarrollo interno completo.
- Se añadieron nueve guías y se reconciliaron README, portal, cobertura, estado editorial, roadmap, metodología, syllabus, validadores y plan maestro. La revisión humana continúa pendiente.

## 2026-09-30 · Matemática y Lengua y Literatura de 2° medio

- Se desarrollaron los 36 OA disciplinares de ambas asignaturas en 201 clases específicas: 55 de Matemática y 146 de Lengua y Literatura.
- Se integraron 29 OA de habilidades y actitudes mediante 122 experiencias: 89 en Matemática y 33 en Lengua y Literatura.
- Se publicaron el índice, el mapa técnico, la vista web y dos guías de asignatura de 2° medio, manteniendo explícitas las 877 propuestas pendientes del resto del nivel.
- El proyecto suma 7.337 clases desarrolladas y 3.822 experiencias integradas; la revisión humana continúa pendiente.

## 2026-09-30 · 1° medio completo

- Se completaron Artes Visuales, Música, Educación Física y Salud, Orientación y Tecnología con 167 clases disciplinares y 117 experiencias integradas nuevas.
- 1° medio alcanza 753 clases desarrolladas, 456 experiencias integradas y 0 propuestas pendientes en sus once denominaciones.
- El proyecto suma 7.136 clases desarrolladas y 3.700 experiencias integradas; desde 1° básico hasta 1° medio hay nueve niveles consecutivos con desarrollo interno completo.
- Se añadieron cinco guías y se reconciliaron README, portal, cobertura, estado editorial, roadmap, metodología, syllabus, validadores y plan maestro.

## 2026-09-30 · Cuatro nuevas asignaturas desarrolladas de 1° medio

- Se completaron Ciencias Naturales, Historia, Geografía y Ciencias Sociales, Inglés e Inglés (Propuesta) de 1° medio con 377 clases disciplinares y 217 experiencias integradas nuevas.
- El nivel alcanza 586 clases desarrolladas, 339 experiencias integradas y conserva 284 propuestas secuenciadas en cinco asignaturas.
- El total del proyecto queda en 6.969 clases desarrolladas y 3.583 experiencias integradas; se añadieron cuatro guías y se sincronizaron portal, README, estado editorial, roadmap, cobertura y validadores.

## 2026-09-30 — Matemática y Lengua y Literatura de 1° medio

- Desarrollo completo de los 15 OA disciplinares de Matemática en 66 clases y 21 OA transversales mediante 89 experiencias integradas.
- Desarrollo completo de los 24 OA disciplinares de Lengua y Literatura en 143 clases y 8 OA de actitudes mediante 33 experiencias integradas.
- Publicación del índice parcial de 1° medio, mapa técnico, vista web y dos guías de asignatura con continuidad desde 8° básico.
- Estado global actualizado a 6.592 clases desarrolladas y 3.366 experiencias integradas; las otras asignaturas de 1° medio conservan 878 propuestas secuenciadas y el nivel no se declara completo.

## 2026-09-30 — Navegación completa y coherencia del README principal

- Incorporación de badges, secciones disciplinares y enlaces directos para 7° y 8° básico; el README principal ahora informa y enlaza las 92 guías resueltas de 1° a 8°.
- Corrección de rutas incompletas que sólo orientaban a docentes de 1° a 3°, del flujo de mejora limitado hasta 5° y de la referencia obsoleta a seis asignaturas desarrolladas de 8°.
- Separación explícita entre los ocho niveles completos y las 3.370 propuestas futuras de 1° a 4° medio.
- Nuevo control automático que exige en el README el índice y cada guía de asignatura de los ocho niveles completos, además de comprobar sus enlaces locales.

## 2026-09-30 — 8° básico completo

- Desarrollo de las seis asignaturas restantes: Educación Física y Salud (26 clases), Orientación (49), Tecnología (26), Inglés (80), Inglés (Propuesta) (65) y Lengua Indígena (43).
- Integración de 65 experiencias transversales nuevas en Educación Física y Salud, Inglés y Tecnología, observables dentro del contenido y sin contarlas como clases adicionales.
- Cierre del nivel en 771 clases desarrolladas, 430 experiencias integradas, 253 OA, doce denominaciones curriculares y 0 propuestas pendientes.
- Publicación de seis guías nuevas y consolidación del índice, mapa técnico, syllabus, plan maestro, cobertura y GitHub Pages para declarar completos los niveles de 1° a 8° básico.
- Estado global actualizado a 6.383 clases desarrolladas y 3.244 experiencias integradas; la revisión humana especializada continúa pendiente.

## 2026-09-30 — Ciencias, Historia, Artes y Música de 8° básico

- Desarrollo completo de Ciencias Naturales en 74 clases disciplinares y 89 experiencias integradas, con experimentación, modelos, evidencia y resguardos de seguridad.
- Desarrollo completo de Historia, Geografía y Ciencias Sociales en 117 clases disciplinares y 91 experiencias integradas, con fuentes, contextualización, contraste y argumentación histórica.
- Desarrollo completo de Artes Visuales en 29 clases disciplinares y 33 experiencias integradas, y de Música en 30 clases disciplinares y 37 experiencias integradas, con creación, interpretación, apreciación y reflexión específicas.
- Publicación de cuatro guías nuevas y actualización del índice, mapa técnico y GitHub Pages: 8° queda con seis asignaturas desarrolladas, 482 clases, 365 integraciones y 354 propuestas pendientes.
- Estado global actualizado a 6.094 clases desarrolladas y 3.179 experiencias integradas; la revisión humana especializada continúa pendiente.

## 2026-09-30 — Matemática y Lengua y Literatura de 8° básico

- Desarrollo completo de los 17 OA disciplinares de Matemática en 77 clases y 19 OA transversales en 82 experiencias integradas.
- Desarrollo completo de los 26 OA disciplinares de Lengua y Literatura en 155 clases y 8 OA transversales en 33 experiencias integradas, incorporando el piloto previo dentro del recorrido completo.
- Publicación del índice de 8°, dos guías de asignatura, mapa técnico y vista específica en GitHub Pages, con continuidad explícita desde 7° básico.
- Estado global actualizado a 5.844 clases desarrolladas y 2.929 experiencias integradas; 8° conserva 854 propuestas pendientes en las demás asignaturas.

## 2026-09-30 — 7° básico completo

- Cierre de las doce denominaciones curriculares en 760 clases disciplinares, 515 experiencias transversales integradas, 275 OA y 0 propuestas pendientes.
- Publicación del mapa técnico, índice completo, doce guías de asignatura y vista específica en GitHub Pages, con continuidad explícita desde 6° básico.
- Estado global actualizado a 5.619 clases desarrolladas y 2.814 experiencias integradas; la revisión humana especializada continúa pendiente.
- Sincronización de la portada, el plan maestro y la documentación para retirar referencias vigentes que aún presentaban 7° como parcial o futuro.

## 2026-09-30 — Paquete de calidad para 4.859 clases desarrolladas

- Incorporación por clase de un recurso concreto, una consigna exacta, una referencia de respuesta, una lista de preparación y una pauta analítica de cuatro niveles.
- Sustitución de la mención genérica a 45 minutos por una distribución explícita de activación, modelado, práctica guiada, desempeño individual y ticket.
- Eliminación de códigos de OA usados como relleno de unicidad y de frases genéricas detectadas en el barrido de 1° a 6° básico.
- Nuevos controles automáticos de paridad por clase en Markdown y HTML, junto con rechazo de regresiones de redacción conocidas.
- Protocolo y esquemas trazables para revisión humana y pilotaje de aula; ambos estados permanecen pendientes hasta contar con evidencia real.

## 2026-09-30 — 6° básico completo

- Desarrollo de las once denominaciones pendientes: 854 clases disciplinares y 334 experiencias transversales integradas.
- Cierre del nivel en 952 clases desarrolladas, 422 experiencias integradas, 301 OA, doce denominaciones curriculares y 0 propuestas pendientes.
- Publicación de doce guías de asignatura con continuidad desde 5°, mapa técnico, índice completo y vista específica en GitHub Pages.
- Secuencias diferenciadas por disciplina y OA, con evidencia individual, dificultades observables, apoyo, profundización y resguardos culturales, físicos, emocionales y digitales.
- Estado global actualizado a 4.859 clases desarrolladas y 2.299 experiencias integradas; la revisión humana especializada continúa pendiente.

## 2026-09-29 — Matemática de 6° básico completa

- Desarrollo de los 24 OA disciplinares en 98 clases específicas y diferenciadas.
- Integración de 14 habilidades y 6 actitudes mediante 88 experiencias observables dentro del contenido, sin contarlas como clases adicionales.
- Progresión desde factores, razones, porcentajes, fracciones y decimales hacia álgebra, geometría, medición, distribuciones y azar.
- Publicación de guía de asignatura, índice parcial del nivel y vista específica de 6° básico; las demás asignaturas permanecen explícitamente pendientes.
- Estado global actualizado a 4.005 clases desarrolladas y 1.965 experiencias integradas, con revisión humana pendiente.

## 2026-09-29 — 5° básico completo

- Desarrollo de las nueve denominaciones pendientes: 575 clases disciplinares y 247 experiencias transversales integradas.
- Cierre del nivel en 920 clases desarrolladas, 420 experiencias integradas, 295 OA y 0 propuestas pendientes.
- Publicación de doce guías de asignatura con continuidad desde 4°, mapa técnico, índice completo y vista específica en GitHub Pages.
- Inclusión diferenciada de Inglés e Inglés (Propuesta), tal como aparecen en el inventario curricular oficial del nivel.
- Verificación automática de unicidad pedagógica, seguridad, privacidad, resguardos culturales, fuentes, licencias y reproducibilidad; revisión humana pendiente.
- Estado global actualizado a 3.907 clases desarrolladas y 1.877 experiencias integradas.

## 2026-09-29 — Matemática, Lenguaje y Ciencias de 5° básico

- Desarrollo de 71 OA disciplinares en 345 clases específicas: 115 de Matemática, 166 de Lenguaje y Comunicación y 64 de Ciencias Naturales.
- Integración de 40 OA de habilidades y actitudes mediante 173 experiencias dentro del contenido, sin duplicarlas como clases independientes.
- Progresiones diferenciadas por OA, con anclas concretas, errores frecuentes, evidencia individual, apoyo, profundización y transferencia.
- Publicación de tres guías equivalentes, índice parcial de 5° y vista específica en GitHub Pages; las otras nueve denominaciones curriculares permanecen explícitamente pendientes.
- Estado global actualizado a 3.332 clases desarrolladas y 1.630 experiencias integradas, con revisión humana pendiente.

## 2026-09-29 — 4° básico completo

- Desarrollo pedagógico de las diez asignaturas restantes de 4° básico, conservando Matemática: el nivel suma 811 clases disciplinares en 175 OA de contenido.
- Integración de 93 OA de habilidades y actitudes mediante 384 experiencias situadas dentro del contenido, sin duplicarlas como clases independientes.
- Guías equivalentes para las once asignaturas, mapa técnico, índice del nivel, vista de GitHub Pages y documentación general actualizados.
- Estado global actualizado a 2.987 clases desarrolladas y 1.457 experiencias integradas; 1°, 2°, 3° y 4° básico quedan completos con revisión humana pendiente.
- Pruebas de cobertura, unicidad pedagógica, resguardos culturales, generación y coherencia documental ampliadas para todo el nivel.

## 2026-09-29 — Matemática de 4° básico completa

- Desarrollo de los 27 OA disciplinares en 118 clases específicas y diferenciadas.
- Integración de 14 OA de habilidades y 6 OA de actitudes mediante 87 experiencias, sin contarlas como clases independientes.
- Progresión desde números hasta 10.000, cuatro operaciones, fracciones y decimales hacia patrones, ecuaciones, geometría, medición, área, volumen, datos y azar.
- Nueva guía de asignatura con continuidad desde 3°, recorrido OA por OA, evidencia, dificultades, acceso y profundización.
- Estado global actualizado a 2.298 clases desarrolladas y 1.160 experiencias integradas; 4° básico permanece en desarrollo en sus otras asignaturas.

## 2026-09-29 — Desarrollo interno completo de 3° básico

- Cierre de las once asignaturas de 3° básico con 757 clases disciplinares, 379 experiencias integradas y 0 propuestas pendientes.
- Matemática, Lenguaje, Ciencias, Historia, Artes, Educación Física, Inglés, Lengua y Cultura, Música, Orientación y Tecnología cuentan con secuencias diferenciadas, evidencia observable y continuidad con 2°.
- Resguardos explícitos de privacidad y actuación institucional en Orientación; seguridad física, digital y de herramientas en Tecnología; escucha segura en Música; y pertinencia cultural en Lengua y Cultura.
- Publicación del mapa completo, once guías de asignatura, vista específica en GitHub Pages y paridad documental con 1° y 2° básico.
- Estado global actualizado a 2.180 clases desarrolladas y 1.073 experiencias integradas; la revisión profesional humana continúa pendiente y no se confunde con CI verde.

## 2026-09-29 — Paridad documental entre 1° y 2° básico

- El índice narrativo de 2° básico alcanza el mismo contrato documental que 1°: propósito, problemas, resultados, prerrequisitos, recorrido, progresión, ritmo, anatomía, evaluación, estados y documentos relacionados.
- Las once guías de 2° incorporan continuidad con 1°, resultados, punto de entrada, método disciplinar, anatomía, ejes, recorrido completo de OA, observación, materiales, recuperación, acceso y fuentes.
- Se añade `docs/SEGUNDO_BASICO.md` como equivalente técnico de `docs/PRIMERO_BASICO.md` y el centro documental enlaza ambas guías por asignatura.
- La portada pública de documentación muestra las once tarjetas completas de 1° y las once de 2° con la misma jerarquía visual, enlaces directos y descripción pedagógica.
- El README principal presenta ambos niveles con insignias, métricas, once accesos por asignatura y reglas de mejora equivalentes, sin privilegiar visualmente a 1° básico.
- El validador y las pruebas rechazan futuras regresiones donde 2° tenga menor profundidad documental que 1°.

## 2026-09-29 — Desarrollo interno completo de 2° básico

- Cierre de las once asignaturas de 2° básico con 721 clases disciplinares, 351 experiencias integradas y 0 propuestas pendientes.
- Desarrollo de Lenguaje, Ciencias e Historia; Artes Visuales, Música y Educación Física; y finalmente Orientación, Tecnología, Inglés y Lengua y Cultura de los Pueblos Originarios Ancestrales.
- Clases diferenciadas por disciplina y OA, con modelado, práctica guiada, desempeño individual, evidencia, apoyo y profundización específicos.
- Resguardos explícitos de privacidad en Orientación, seguridad en Tecnología y Educación Física, comunicación comprensible sin exigir acento nativo en Inglés y fuentes comunitarias, no invención lingüística y no apropiación en Lengua y Cultura.
- Publicación de once guías de asignatura, mapa completo del nivel, catálogo, documentación general y portal de GitHub Pages sincronizados.
- Estado global actualizado a 1.434 clases desarrolladas y 694 experiencias integradas; la revisión profesional humana continúa pendiente y no se confunde con CI verde.

## 2026-09-28 — 2° básico definido y Matemática desarrollada

- Se delimitaron las once asignaturas, 247 OA y 1.072 propuestas de 2° básico.
- Matemática quedó desarrollada en 22 OA disciplinares, 93 clases y 64 experiencias que integran 15 OA de habilidades y actitudes.
- Las otras diez asignaturas conservan 915 propuestas en estado secuenciada, sin plantillas presentadas como contenido terminado.
- Se añadieron mapa web, documentación del nivel, guía de Matemática, validaciones estructurales y pruebas de especificidad.
- La revisión profesional humana continúa pendiente y no se confunde con CI verde.

## 2026-09-28 — Desarrollo interno completo de 1° básico

- Desarrollo de Música, Educación Física y Salud, Orientación, Tecnología, Inglés (Propuesta) y Lengua y Cultura de los Pueblos Originarios Ancestrales: 336 clases disciplinares y 114 experiencias transversales nuevas.
- Cierre de las once asignaturas de 1° básico con 691 clases disciplinares, 343 experiencias integradas y 0 borradores.
- Auditoría de variedad pedagógica sobre Ciencias, Historia y Artes Visuales: aperturas, modelados, prácticas, desempeños y tickets reescritos con movimientos propios de cada disciplina.
- Resguardos explícitos de privacidad en Orientación, seguridad y acceso en Educación Física, comunicación comprensible sin exigir acento nativo en Inglés y fuentes comunitarias, no invención lingüística y no apropiación en Lengua y Cultura.
- Pruebas nuevas para impedir clases intercambiables por repetición textual y para verificar cobertura completa de OA y actitudes por asignatura.

## 2026-09-28 — Ciencias, Historia y Artes Visuales de 1° básico

- Desarrollo completo de 12 OA y 49 clases de Ciencias Naturales, con indagación, diseño, seguridad y evidencia observable.
- Desarrollo completo de 15 OA y 68 clases de Historia, Geografía y Ciencias Sociales, con temporalidad, fuentes, territorio y ciudadanía.
- Desarrollo completo de 5 OA y 24 clases de Artes Visuales, con observación, experimentación, creación y apreciación fundamentada.
- Integración no duplicada de 33 OA transversales mediante 132 experiencias de habilidades y actitudes.
- Estado de 1° básico actualizado a 355 clases desarrolladas, 229 experiencias integradas y 450 borradores; Música queda como siguiente asignatura.
- Validadores, pruebas, documentación Markdown/HTML y portal actualizados desde la misma fuente.

## 2026-09-25 — Auditoría y endurecimiento de licencias

- Separación expresa entre hechos/metadatos, redacción oficial MINEDUC y elaboración pedagógica original.
- Avisos de derechos regenerados en las 2.823 fichas Markdown y HTML, sin relicenciar texto oficial.
- `DATA-LICENSE.md` consolidado como nombre canónico y protegido contra aliases obsoletos.
- Inventario de datasets y activos, procedencia del snapshot, enlaces legales y avisos generados cubiertos por el validador.
- Guías de uso comercial e historial de licenciamiento, auditoría técnica y DCO 1.1 para contribuciones futuras.
- Catálogo schema 8 con `rights_notice` heredado por las salidas JSON.

## 2026-09-24 — Corrección del estado pedagógico

- Reclasificación de 1.020 textos automáticos de 1° básico como borradores, no clases desarrolladas.
- Primera reconstrucción disciplinar de Matemática `MA01 OA 01` y Lenguaje `LE01 OA 03`, con alineación a indicadores oficiales, ejemplos, dificultades y evidencia.
- Estado verificable corregido a 14 clases desarrolladas y 1.020 borradores en 1° básico; 36 desarrolladas en todo el repositorio.
- Documentación y portal actualizados para distinguir inventario, borrador, desarrollo, revisión y publicación.

> Corrección: una versión anterior declaró 1.034 clases desarrolladas en 1° básico. Esa afirmación se retiró al comprobar que 1.020 provenían de plantillas generales sin desarrollo específico por OA.

## 2026-09-24 — Arquitectura documental pedagógica

- Portada documental visual dentro de GitHub Pages, conectada con el portal y la vista del nivel.
- README profesional con badges, navegación, cobertura, anatomía, evaluación, inclusión, fuentes y arquitectura.
- Syllabus, rúbrica, FAQ, guía para familias y protocolo de revisión humana.
- Índice narrativo de 1° básico y 11 guías de asignatura con propósito, resultados, prerrequisitos, método, ejes, recorrido OA por OA, evidencia y recuperación.
- Guía docente, metodología, roadmap y contribución alineados con los estados editoriales verificables.
- Reemplazo de rutas heredadas del antiguo programa de licenciamiento por rutas propias del currículo escolar.
- Validación automática de documentos esenciales, las 11 guías completas y la ausencia de términos heredados.

## 2026-09-24 — Portal curricular profesional y CI reproducible

- 1° básico desarrollado por completo: 1.034 clases, 237 OA y 11 asignaturas, más 22 clases piloto conservadas en otros niveles.
- Nueva vista profesional del nivel con mapa de contenidos, métricas, ejes y acceso por asignatura, acompañada de documentación específica.
- Fuente estructurada persistente y contrato automático para impedir que contenido genérico se contabilice como desarrollado.
- Nuevas fichas de clase con meta estudiantil, materiales, criterios observables, ticket, decisión posterior y adaptación a 45 minutos.
- Portal rediseñado con búsqueda tolerante a tildes, filtros combinables, URL compartible, carga progresiva, tema claro/oscuro y diseño adaptable.
- 12.997 clases con identificador estable enlazadas a 2.823 páginas HTML de OA, además de sus fuentes Markdown.
- Sitemap, manifest, icono, 404 útil, metadatos Open Graph, canonical, impresión y navegación anterior/siguiente.
- Estados editoriales explícitos para separar inventario, secuenciación, desarrollo, revisión y publicación.
- Workflow único con acciones fijadas por SHA, generación determinista, validación, tests y despliegue condicionado.
- Retiro del prompt maestro y del generador, manifiesto, tests e informes heredados del antiguo programa de licenciamiento.

## 1.0.0 — 2026-09-14
- MIT para software.
- CC BY-NC-SA 4.0 para contenido educativo.
- Política de datasets/terceros/marca.
- Licenciamiento comercial separado.
- Registro de fuentes.
- Validador, tests y CI.
- Prompt maestro de auditoría.
- Migración específica del programa pedagógico.
