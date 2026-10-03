# Estándar de calidad editorial

Una entrada generada no equivale a una clase terminada.

| Estado | Evidencia mínima |
|---|---|
| Inventariada | OA, nivel, asignatura, eje y fuente oficial |
| Secuenciada | posición, prerrequisitos y duración justificada |
| Desarrollada | explicación específica, ejemplo resuelto, práctica, apoyo, profundización y evaluación |
| Revisada | control disciplinar, pedagógico, documental, accesible y de derechos |
| Publicada | Markdown y HTML válidos, navegables y comprobados en Pages |

Los conteos públicos muestran estos estados por separado. Una clase puede estar desarrollada y publicada sin estar revisada. **Desarrollo interno completo** significa que no quedan secuencias ni borradores pendientes; **revisada** exige evidencia humana competente. La documentación no debe usar “completa” sin indicar cuál de esos estados describe.

## Contrato mínimo por clase

Cada clase debe tener identificador, nivel, asignatura, OA, posición, propósito, meta para estudiantes, explicación disciplinar, vocabulario, conocimientos previos, error previsible, materiales, inicio, modelado, práctica guiada e individual, apoyo, profundización, cierre, evidencia, criterio de éxito, decisión posterior, accesibilidad y fuentes. Además, toda clase desarrollada publica cinco componentes utilizables sin completar una plantilla:

1. un insumo concreto reproducible o una especificación segura para prepararlo;
2. una consigna exacta para estudiantes;
3. una referencia de respuesta que permita modelar y corregir sin imponer una única forma;
4. una pauta de cuatro niveles con descriptores observables;
5. una distribución explícita de 45 minutos que conserva modelado, práctica y evidencia individual.

## Criterios de una clase desarrollada

### Especificidad disciplinar

- Nombra el contenido real del OA.
- Explica una decisión, relación o procedimiento propio de la disciplina.
- Incluye un ejemplo y un error plausible.
- Define un producto o desempeño reconocible.
- Evita párrafos intercambiables entre asignaturas.

### Coherencia pedagógica

- El inicio aporta información sobre conocimientos previos.
- El modelado hace visible el razonamiento, no solo el resultado.
- La práctica guiada prepara el desempeño individual.
- El ticket recoge evidencia vinculada a los criterios.
- La decisión posterior depende de lo observado.

### Acceso y desafío

- El apoyo cambia la vía de acceso sin sustituir el OA.
- Las formas de respuesta son pertinentes a la acción cognitiva.
- La profundización exige explicar, comparar, crear, mejorar o transferir.
- La versión de 45 minutos conserva el núcleo.
- La seguridad y el cuidado aparecen cuando la actividad lo exige.

### Viabilidad

- Los materiales pueden prepararse en un contexto escolar real.
- Existe alternativa cuando la conectividad no es esencial al OA.
- La organización permite participación amplia.
- Las transiciones no consumen la mayor parte del bloque.
- La evidencia puede recogerse de cada estudiante.

## Criterios de revisión humana

Una revisión completa cubre:

| Dimensión | Evidencia esperada |
|---|---|
| Disciplinar | conceptos, ejemplos, procedimientos y vocabulario contrastados |
| Pedagógica | progresión, carga, práctica y evaluación revisadas |
| Accesibilidad | apoyos y vías de respuesta analizados sin reducir el OA |
| Cultural | contexto, lenguaje y representaciones sin estereotipos |
| Documental | fuente, enlaces y distinción entre oficial y editorial |
| Derechos | materiales, privacidad y atribución comprobados |

El [protocolo de revisión](docs/REVISION_HUMANA.md) define responsables, severidad, registro y condición para cambiar el estado.

## Señales de rechazo

Una clase no cumple el estándar si:

- usa una actividad genérica que no permite reconocer la asignatura;
- promete aprendizaje sin evidencia observable;
- entrega todas las respuestas durante el apoyo;
- llama profundización a más ejercicios idénticos;
- confunde participación, conducta o velocidad con dominio;
- exige exposición de experiencias sensibles;
- inventa una fuente, obligatoriedad o revisión;
- depende de un recurso externo sin alternativa ni condiciones de uso;
- contiene material protegido o datos personales sin autorización.

## Comprobación automática

Los validadores revisan estructura, campos, conteos, estados, archivos, anclas y documentos esenciales. También exigen:

- separación verificable entre 8.841 clases desarrolladas, 4.156 experiencias integradas y 0 propuestas pendientes;
- índices completos de 1° a 8° básico;
- 149 guías de asignatura: 92 para los ocho niveles básicos completos, once para 1° medio, once para 2° medio, dieciocho para 3° medio y diecisiete para 4° medio;
- paridad documental: ningún índice o guía de un nivel completo puede tener menor profundidad estructural que su equivalente;
- syllabus, rúbrica, FAQ, guía para familias y protocolo de revisión;
- portada documental HTML;
- ausencia de contenido heredado ajeno al curso;
- presencia de los cinco componentes de uso de aula en cada una de las 8.841 clases desarrolladas;
- ausencia de criterios de relleno, códigos usados como falsa diferenciación y defectos de puntuación conocidos.
- referencias de habilidad, OA, prerrequisito, error, intervención e ítem válidas dentro del sistema longitudinal;
- fuente, versión, limitaciones y tipo de alineamiento explícitos para cada marco externo;
- separación verificable entre observación, patrón, hipótesis, diagnóstico pedagógico, intervención y reevaluación;
- rechazo de datos personales y de porcentajes o estados de dominio sin evidencia diversa y decisión profesional explícita.

La automatización detecta ausencia y deriva; no certifica verdad disciplinar ni pertinencia humana.
