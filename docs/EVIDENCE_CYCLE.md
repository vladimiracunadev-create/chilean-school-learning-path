# Evidencia, diagnóstico, intervención y reevaluación

El sistema separa eventos que suelen mezclarse. Una respuesta no se convierte automáticamente en una etiqueta sobre el estudiante.

## Estados distintos

| Estado | Qué significa | Qué no significa |
|---|---|---|
| Observación | Un desempeño ocurrió en una tarea y contexto concretos | que la habilidad esté dominada o ausente |
| Patrón | El mismo error relacionado apareció en dos ítems y sesiones distintas | que conozcamos su causa |
| Hipótesis | Un profesional documentó una explicación comprobable y sus evidencias | diagnóstico confirmado |
| Evidencia acumulada | Hay registros diversos, trazables y comparables | puntaje válido por sí mismo |
| Diagnóstico pedagógico | Un profesional confirma o rechaza una hipótesis para decidir enseñanza | diagnóstico clínico o rasgo personal |
| Dominio descriptivo | Una decisión profesional se apoya en práctica y transferencia diversa | percentil, nota o habilidad latente |

## Ciclo

```text
evaluar
→ observar
→ buscar un patrón
→ formular una hipótesis
→ intervenir con contenido existente
→ practicar
→ reevaluar en una situación nueva
→ comparar
→ avanzar, mantener o revisar la hipótesis
```

Las barreras de acceso y la evidencia insuficiente no cuentan como error conceptual. Antes de intervenir se revisa si la consigna, el formato, el tiempo, el idioma, la conectividad o la vía de respuesta impidieron observar el OA.

## Registro y privacidad

El esquema `evidence/evidence-cycle.schema.json` permite ejemplos `SYNTH-*` y códigos locales seudonimizados `LOCAL-*`. Este repositorio público no recibe nombres, RUN, correos, imágenes, producciones identificables ni diagnósticos.

Los registros reales deben vivir en un sistema autorizado por el establecimiento, con acceso, retención, finalidad y eliminación definidos. Git solo contiene el esquema y ejemplos sintéticos.

## Cómo leer el resumen

`scripts/competency_evidence.py` devuelve un estado descriptivo, su base, las cautelas y el próximo paso. No devuelve porcentaje. El motor detecta un patrón, pero una hipótesis, un diagnóstico pedagógico y una decisión de dominio siempre deben quedar firmados por un rol profesional.

## Reevaluación

La reevaluación cambia texto, números, representación o contexto y conserva la habilidad central. Repetir la misma respuesta comprueba memoria de la tarea, no transferencia.

Una intervención que no mejora la evidencia no se “compensa” bajando el criterio: se revisan la hipótesis, los prerrequisitos, la accesibilidad y la propia intervención.
