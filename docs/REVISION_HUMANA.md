# ✅ Protocolo de revisión humana

> [⬅️ Centro de documentación](README.md) · [📏 Estándar de calidad](../QUALITY_STANDARD.md) · [🤝 Contribuir](../CONTRIBUTING.md)

Una clase no cambia a estado **revisada** por haber pasado tests. La revisión exige una persona competente, alcance explícito y evidencia reproducible.

## Objetivo

Comprobar que la propuesta interpreta responsablemente el OA, enseña contenido específico, ofrece evidencia válida, contempla acceso y seguridad y usa fuentes y materiales de forma adecuada.

## Roles de revisión

| Dimensión | Perfil recomendado | Pregunta central |
|---|---|---|
| Disciplinar | Docente o especialista del área y nivel | ¿El contenido es correcto y representa la disciplina? |
| Pedagógica | Docente de primer ciclo, UTP o diseñador instruccional | ¿La progresión permite aprender y observar? |
| Accesibilidad | Educador diferencial o profesional pertinente | ¿Las vías de acceso conservan el OA? |
| Cultural y contextual | Comunidad o especialista cuando corresponda | ¿Evita estereotipos y respeta el contexto? |
| Documental | Persona que verifica fuentes y trazabilidad | ¿Las afirmaciones y enlaces se sostienen? |
| Derechos y privacidad | Revisor de licencias y datos | ¿Puede publicarse sin vulnerar derechos? |

Una persona puede cubrir más de una dimensión si declara su alcance. No se infiere competencia por el cargo.

## Secuencia de revisión

1. Identificar nivel, asignatura, OA y clases.
2. Leer el OA en su fuente oficial.
3. Revisar la secuencia completa, no una clase aislada.
4. Aplicar cada control de la lista.
5. Registrar hallazgos como bloqueo, mejora o observación.
6. Corregir la fuente estructurada.
7. Regenerar y ejecutar validadores.
8. Volver a revisar los cambios relevantes.
9. Registrar decisión, responsable y fecha.

## Lista disciplinar

- [ ] El propósito responde al OA.
- [ ] Los conceptos, procedimientos y ejemplos son correctos.
- [ ] El vocabulario es preciso y comprensible para el nivel.
- [ ] El ejemplo y el error previsible son plausibles.
- [ ] La práctica exige pensamiento disciplinar, no solo participación.
- [ ] La profundización amplía comprensión.

## Lista pedagógica

- [ ] Se recuperan conocimientos previos relevantes.
- [ ] El modelado revela decisiones.
- [ ] Existe práctica guiada antes de autonomía.
- [ ] La carga y las transiciones son viables.
- [ ] La evidencia es atribuible a cada estudiante.
- [ ] Los criterios permiten decidir qué hacer después.
- [ ] La versión breve conserva el núcleo.

## Lista de acceso, cuidado y contexto

- [ ] El apoyo mantiene la acción cognitiva del OA.
- [ ] Hay alternativas pertinentes de percepción o respuesta.
- [ ] Las consignas evitan exposición innecesaria.
- [ ] Materiales, movimiento y herramientas tienen condiciones seguras.
- [ ] El contenido evita estereotipos culturales, lingüísticos o familiares.
- [ ] Cuando corresponde, se declara necesidad de validación local o comunitaria.

## Lista documental y de derechos

- [ ] OA, eje, fuente y enlaces son correctos.
- [ ] Se distingue texto oficial de propuesta editorial.
- [ ] No se reproduce material protegido sin autorización.
- [ ] No se incluyen datos personales o evidencias identificables.
- [ ] Los recursos externos tienen atribución y condiciones claras.

## Severidad de hallazgos

| Nivel | Ejemplo | Efecto |
|---|---|---|
| Bloqueante | error disciplinar, riesgo, discriminación, fuente falsa o vulneración de derechos | impide declarar revisión |
| Mayor | evidencia no mide el OA, secuencia inviable o apoyo que rebaja | requiere corrección y nueva revisión |
| Menor | redacción ambigua, ejemplo mejorable o enlace secundario | puede corregirse con verificación focalizada |
| Observación | sugerencia contextual no universal | se documenta sin invalidar |

## Registro de evidencia

Cada revisión debe guardar:

| Campo | Contenido |
|---|---|
| Revisor | Nombre o identificador acordado y rol |
| Fecha | ISO 8601 |
| Alcance | Asignatura, OA, clases y dimensiones |
| Versión | Commit revisado |
| Resultado | Aprobado, aprobado con observaciones o requiere cambios |
| Hallazgos | Lista trazable con severidad |
| Cambios | Commit o PR que los resuelve |
| Pendientes | Dimensiones aún no revisadas |

## Regla de publicación

“Revisada” solo se registra cuando todas las dimensiones exigidas para el alcance están aprobadas y los hallazgos bloqueantes o mayores se resolvieron. Una revisión parcial debe nombrarse como parcial; no habilita inflar el contador global.
