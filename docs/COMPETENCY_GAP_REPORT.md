# Informe de brechas previo · sistema longitudinal de competencias

**Fecha de auditoría:** 2 de octubre de 2026

**Commit auditado:** `2cb899fd` (`main`, árbol limpio y sincronizado con `origin/main`)

**Propósito:** registrar el estado comprobado antes de ampliar el repositorio. Este documento es histórico: describe la línea base previa a la implementación y no debe reescribirse para aparentar que las capacidades nuevas ya existían.

## Alcance revisado

La auditoría cubrió `README.md`, `CURRICULUM.md`, `METHODOLOGY.md`, `TEACHING_GUIDE.md`, `EDITORIAL_STATUS.md`, `OFFICIAL_REFERENCES.md`, `QUALITY_STANDARD.md`, `VALIDATION_REPORT.md`, `ROADMAP.md`, `docs/`, `curriculum/`, `content/`, `sources/`, `reviews/`, `scripts/`, `tests/`, el portal `site/`, las salidas PDF y `.github/workflows/pages.yml`.

La fuente curricular canónica es `sources/mineduc-curriculum-snapshot.json`; `scripts/generate_school_program.py` produce catálogo, Markdown, HTML, malla y sitemap; `scripts/validate_school_program.py`, `scripts/validate_licensing.py` y 56 pruebas estructurales controlan la salida. La línea base contiene 2.823 OA, 12.997 registros pedagógicos, 12 niveles, 35 denominaciones de asignatura y 149 guías. La publicación no equivale a revisión humana: `reviews/` conserva esquemas de revisión y pilotaje, pero todavía no contiene registros aprobados.

## Matriz de brechas obligatoria

| Elemento | Estado | Evidencia encontrada | Acción |
|---|---|---|---|
| Comprensión lectora | **EXISTE Y DEBE CONSERVARSE** | OA y clases de Lenguaje desde 1° básico a 4° medio en `curriculum/`; secuencias, evidencia y dificultades por OA; fuente en `sources/mineduc-curriculum-snapshot.json` | Conservar el contenido; conectarlo mediante habilidades y progresiones, sin crear otro curso genérico |
| Evaluación formativa | **EXISTE Y DEBE AMPLIARSE** | `docs/EVALUACION_FORMATIVA.md`, `docs/RUBRICA_EVALUACION.md`, tickets, criterios, pauta de cuatro niveles y decisión posterior en cada clase | Mantener la escala descriptiva y agregar registros longitudinales de evidencia y reevaluación |
| Competencias | **EXISTE PARCIALMENTE** | OA de habilidad/actitud integrados y perfiles disciplinares en generadores y guías; no existe taxonomía transversal versionada | Crear taxonomía estable y muchos-a-muchos, separada del currículo oficial |
| Diagnóstico | **EXISTE PARCIALMENTE** | Fase “Conectar y diagnosticar”, registros mínimos y matrices de dificultad; opera dentro de una clase u OA | Modelar observación, patrón, hipótesis e intervención sin convertir una respuesta aislada en diagnóstico |
| Banco de ítems | **NO EXISTE** | Hay tickets, consignas, referencias y tareas dentro de clases, pero no registros reutilizables con ID, versión, autoría, distractores y framework | Crear esquema y banco inicial de tareas originales; enlazar a OA y competencias |
| PAES | **NO EXISTE** | Sin rutas, datos ni equivalencias PAES | Incorporar como marco desacoplado; registrar alineamiento oficial o correspondencia inferida por separado |
| SIMCE | **NO EXISTE** | Sin representación estructurada; solo evaluación curricular interna | Incorporar como marco nacional desacoplado y limitado a niveles/áreas justificables |
| PISA | **NO EXISTE** | Existen tareas situadas y transferencia dentro de clases, pero no marco PISA | Incorporar marco y tareas originales contextualizadas; no copiar ítems protegidos |
| TIMSS | **NO EXISTE** | Matemática y ciencias tienen OA y progresión, sin vista TIMSS | Incorporar marco por nivel y dominio cognitivo, sin presentarlo como equivalencia oficial chilena |
| PIRLS | **NO EXISTE** | Lectura en básica está desarrollada, sin vista PIRLS | Incorporar marco de lectura para población correspondiente y correspondencias pedagógicas explícitamente inferidas |
| Progresión longitudinal | **EXISTE PARCIALMENTE** | Continuidad entre niveles en guías y secuencias; `LEARNING_PATHS.md`; no se puede recorrer una habilidad transversal de 1° básico a 4° medio | Crear grafo de prerrequisitos, etapas e hitos enlazados a OA reales |
| Análisis de errores | **EXISTE Y DEBE AMPLIARSE** | Cada clase desarrollada contiene errores previsibles, acción inmediata y comprobación; `docs/DIFICULTADES_EN_EL_AULA.md` | Normalizar patrones de error y conectarlos con habilidades e intervenciones, sin etiquetar estudiantes |
| Adaptación | **EXISTE PARCIALMENTE** | Apoyo, profundización, otra vía de acceso y decisión posterior; sin estado longitudinal ni selector de actividad | Definir política determinista simple y auditable; dejar IA como extensión opcional |

## Capacidades que se conservan como fuentes de verdad

- El OA oficial, su texto, nivel, eje y URL siguen viniendo del snapshot Mineduc.
- Las clases, actividades, apoyos, profundizaciones, tickets y evidencias existentes son la primera fuente para intervenir.
- Los artefactos de `curriculum/`, `CURRICULUM.md` y `site/` siguen siendo derivados del generador.
- “Publicada”, “desarrollada”, “revisada” y “pilotada” continúan siendo estados distintos.
- No se guardan datos personales ni diagnósticos individuales en el repositorio público.
- La licencia del contenido propio no altera los derechos de textos oficiales ni de marcos externos.

## Investigación de marcos y alcance justificable

| Marco | Fuente oficial consultada | Población o alcance | Uso permitido en esta ampliación |
|---|---|---|---|
| PAES | DEMRE, temarios y descripción de pruebas del proceso de admisión 2027 | Egreso de enseñanza media; pruebas obligatorias y electivas | Registrar habilidades y conocimientos publicados por DEMRE; construir tareas “PAES-like” originales y trazar antecedentes curriculares |
| SIMCE | Agencia de Calidad de la Educación, características generales 2026 e informes técnicos | Niveles y áreas definidos por el plan vigente; en 2026, Lectura y Matemática en 4° y 6° básico y II medio | Vista de evaluación del Currículum Nacional; no usar resultados agregados para diagnosticar a una persona |
| PISA | OECD, *PISA 2025 Assessment and Analytical Framework* (2026) | Estudiantes de 15 años; ciencias, lectura, matemática y aprendizaje en el mundo digital | Tareas de transferencia contextualizadas; correspondencia pedagógica inferida, nunca alineamiento oficial con OA chilenos |
| TIMSS | IEA/TIMSS & PIRLS International Study Center, *TIMSS 2027 Assessment Frameworks* | Matemática y ciencias en 4° y 8° grado; dominios conocer, aplicar y razonar | Vista por contenido y demanda cognitiva; correspondencia inferida con niveles chilenos |
| PIRLS | IEA/TIMSS & PIRLS International Study Center, *PIRLS 2026 Assessment Frameworks* | Comprensión lectora al final de primaria | Vista de propósitos y procesos lectores; correspondencia inferida con OA, sin copiar textos o ítems |

**Fecha de consulta:** 2 de octubre de 2026. Las versiones se registrarán junto a cada marco para poder actualizarlas sin modificar OA ni taxonomía central.

## Revisión de repositorios relacionados

- `psychometrics-and-assessment-program` separa instrumento, motor y presentación, rechaza baremos inexistentes y documenta una ruta de validación que pasa por contenido, piloto, estructura, fiabilidad, validez e invarianza. La ampliación adoptará esa honestidad de estados, no sus instrumentos de personalidad.
- `education-pedagogy-learning-sciences-program` trata la validez como argumento sobre la interpretación y el uso, recomienda no decidir con una sola medición y diferencia evidencia robusta, consistente, emergente, debatida, normativa y profesional. Se reutiliza el principio, no el currículo del otro repositorio.
- `langgraph-realworld/cases/11-educacion-tutor-adaptativo` aporta un flujo conceptual de diagnóstico, selección, respuesta, ajuste y reporte, pero usa una escala IRT simplificada y estudiantes simulados. Aquí no se copiará esa escala ni se llamará IRT a una heurística: el núcleo será determinista, sin LLM y sin puntajes ficticios.

## Diseño aprobado después de la auditoría

La extensión mínima coherente tendrá cinco capas desacopladas:

1. `competencies/`: taxonomía versionada, grafo longitudinal y marcos externos con procedencia.
2. `assessments/`: esquema y banco inicial de tareas originales, con licencias y distractores interpretables cuando corresponda.
3. `evidence/`: esquemas para observaciones agregadas o seudonimizadas, hipótesis, intervenciones y reevaluaciones; ningún dato personal en Git.
4. `scripts/validate_competency_system.py`: invariantes referenciales, ciclos, OA existentes, licencias y límites de inferencia.
5. Portal y documentación: vistas de trayectoria, estudiante y docente generadas a partir de los mismos datos.

No se introduce base de datos, API, LLM, IRT ni dependencia de ejecución nueva. JSON versionado y validación Python son suficientes para esta etapa. La primera entrega demostrará el ciclo completo con un conjunto pequeño y diverso de competencias y tareas; ampliar cobertura exige revisión disciplinar y no generación masiva automática.

## Riesgos y controles

| Riesgo | Control de diseño |
|---|---|
| Presentar una equivalencia inferida como oficial | Campo obligatorio `alignment_type`: `official`, `pedagogical_inference` o `project_proposal` |
| Diagnosticar por una sola respuesta | Estados separados y umbrales descriptivos basados en múltiples observaciones |
| Inventar porcentajes de dominio | Perfil por cantidad, diversidad, actualidad y consistencia de evidencias; sin porcentaje si no existe modelo validado |
| Duplicar comprensión lectora | Competencias apuntan a OA y clases existentes |
| Copiar ítems protegidos | Banco exclusivamente original, con autoría y licencia explícitas |
| Llamar psicometría a una heurística | Estados `experimental`, `pilotado`, `analizado`, `revisado`, `validado`; solo evidencia real permite avanzar |
| Acoplar el currículo a PAES/SIMCE/PISA/TIMSS/PIRLS | Marcos como datos removibles; ningún OA depende de ellos |
| Usar IA como medición | IA opcional, revisable y fuera del cálculo de evidencia; fallback determinista |
