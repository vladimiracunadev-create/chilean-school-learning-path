# Contribuir

Las contribuciones deben mejorar claridad, trazabilidad, accesibilidad o aplicación pedagógica. El proyecto acepta correcciones pequeñas, contenido desarrollado y revisiones documentadas.

[Metodología](METHODOLOGY.md) · [Estándar de calidad](QUALITY_STANDARD.md) · [Roadmap](ROADMAP.md)

## Antes de comenzar

- Describe el problema y quién se beneficia.
- Identifica nivel, asignatura, OA y clase afectada.
- Usa fuentes primarias para afirmaciones curriculares o normativas.
- No incluyas datos de estudiantes ni material de terceros sin permiso verificable.
- Conserva los identificadores existentes salvo que exista un error demostrado.

## Contrato de una clase desarrollada

Toda clase debe incluir:

1. identificador, posición, nivel, asignatura y OA;
2. propósito docente y meta en lenguaje estudiantil;
3. conocimientos previos, vocabulario y error previsible;
4. inicio, modelado, práctica guiada y desempeño individual;
5. materiales y preparación viables;
6. apoyo que conserva el OA y profundización no mecánica;
7. ticket, evidencia y al menos tres criterios observables;
8. decisión posterior y adaptación a 45 minutos;
9. accesibilidad, seguridad y fuentes pertinentes.

Evita frases intercambiables entre asignaturas. Una clase debe nombrar el contenido, el producto o desempeño, el razonamiento que se modela y la evidencia que se observará.

## Reglas editoriales

- Usa **clase**, no “sesión”, para las unidades de enseñanza del proyecto.
- Distingue texto oficial, interpretación editorial y sugerencia docente.
- No declares “revisada” una clase sin registrar evidencia humana.
- No presentes lecturas asociadas como obligatorias.
- Ofrece alternativas sin conectividad cuando la actividad dependa de tecnología.
- Mantén el OA al proponer apoyos; modifica el acceso, no la expectativa central.
- Profundiza mediante explicación, comparación o transferencia, no con más repetición.

## Fuente y artefactos generados

Modifica la fuente estructurada correspondiente. No edites manualmente miles de fichas derivadas: `scripts/generate_school_program.py` vuelve a producir catálogo, Markdown, HTML, malla, sitemap, portada documental, índice de 1° básico y sus 11 guías de asignatura.

Después del cambio ejecuta:

```bash
python scripts/generate_school_program.py
python scripts/validate_school_program.py
python scripts/validate_licensing.py
python -m unittest discover -s tests -p "test_*.py" -v
```

El diff después de una segunda generación debe quedar vacío.

## Revisión propuesta

Una revisión humana debe indicar:

- persona o rol revisor;
- fecha;
- alcance: disciplina, pedagogía, accesibilidad, documentación o derechos;
- OA y clases revisadas;
- hallazgos y cambios realizados;
- aspectos que siguen pendientes.

El equipo mantenedor decide cuándo la evidencia permite cambiar el estado editorial.

## Derechos y procedencia

Registra contenido externo y atribuciones según [LICENSING.md](LICENSING.md). Enlaza recursos cuando la licencia no permite redistribución y no copies fragmentos extensos de obras.

Al contribuir confirmas que puedes enviar tu aporte. El código se recibe bajo MIT y el contenido educativo original bajo CC BY-NC-SA 4.0.
