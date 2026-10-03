# Marcos de evaluación como vistas desacopladas

PAES, SIMCE, PISA, TIMSS y PIRLS no constituyen el currículo de este proyecto. Cada marco se registra como una vista con procedencia, población, alcance y límites. El registro estructurado está en `competencies/frameworks.v1.json`.

## Tipos de relación

| Tipo | Uso |
|---|---|
| `official` | La institución responsable declara explícitamente la relación |
| `pedagogical_inference` | El proyecto propone una correspondencia razonada, no oficial |
| `project_proposal` | Tarea, criterio o instrumento original del proyecto |

Una tarea “PAES-like”, “PISA-like” o vinculada a TIMSS/PIRLS siempre es `project_proposal`. No predice un puntaje ni reproduce un ítem oficial.

## Registro vigente consultado

| Marco | Institución | Versión | Población y foco | Fuente |
|---|---|---|---|---|
| PAES | DEMRE, Universidad de Chile | Admisión 2027 | Acceso a educación superior; competencias lectoras, matemáticas y pruebas electivas | [DEMRE](https://portaldemre.demre.cl/paes/factores-seleccion/pruebas-acceso-paes) |
| SIMCE | Agencia de Calidad de la Educación | Aplicación 2026 | Logro de contenidos y habilidades del Currículum Nacional en niveles y áreas definidos por el plan vigente | [Agencia](https://www.agenciaeducacion.cl/evaluar/simce/) |
| PISA | OECD | PISA 2025, marco publicado en 2026 | Estudiantes de 15 años; transferencia en ciencias, lectura, matemática y aprendizaje digital | [OECD](https://www.oecd.org/en/publications/pisa-2025-assessment-and-analytical-framework_86c36975-en.html) |
| TIMSS | IEA / Boston College | TIMSS 2027 | Matemática y ciencias en 4° y 8° grado; conocer, aplicar y razonar | [TIMSS 2027](https://timss2027.org/frameworks/) |
| PIRLS | IEA / Boston College | PIRLS 2026 | Comprensión lectora alrededor del cuarto año de escolaridad | [IEA](https://www.iea.nl/publications/assessment-framework/pirls-2026-assessment-frameworks) |

**Fecha de consulta:** 2 de octubre de 2026.

## Límites de interpretación

- SIMCE, TIMSS y PIRLS tienen poblaciones, diseños y propósitos distintos.
- PISA evalúa aplicación en estudiantes de 15 años y no prescribe un currículo nacional.
- PAES es una evaluación de acceso; su preparación no reemplaza la trayectoria escolar.
- Los resultados agregados de un sistema no diagnostican por sí solos a un estudiante.
- La correspondencia entre un dominio externo y un OA chileno se publica como inferencia pedagógica salvo evidencia oficial explícita.
- Todo estímulo del banco del proyecto es original y declara licencia y autoría.

## Actualización

Cada framework puede actualizarse o retirarse sin modificar los OA ni los ID centrales de habilidades. Un cambio de versión conserva la referencia anterior cuando sea necesaria para interpretar tareas históricas.
