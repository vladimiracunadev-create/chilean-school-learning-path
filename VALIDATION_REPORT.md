# Reporte de validación

Fecha: 2026-09-30

## Alcance verificable

- 12.997 clases con código único y ancla web estable.
- 2.823 OA con página HTML, Markdown y trazabilidad a Currículum Nacional.
- 12 niveles, 35 asignaturas y 595 vínculos de lectura.
- 691 clases de 1° básico, 721 de 2°, 757 de 3°, 811 de 4°, 920 de 5°, 952 de 6°, 760 de 7° y 482 de 8°: 6.094 desarrolladas en total; 3.179 experiencias transversales integradas y 0 revisiones humanas registradas.
- 1° a 7° básico completos, con 0 propuestas pendientes dentro de esos niveles.
- Seis asignaturas de 8° completas, con 482 clases y 365 experiencias integradas; el nivel conserva 354 propuestas pendientes en las demás asignaturas.
- 4° básico completo: 175 OA disciplinares, 811 clases y 93 OA transversales integrados mediante 384 experiencias.
- 0 clases declaradas como revisadas sin evidencia humana.
- Contrato editorial estructurado con propósito, meta, cinco momentos, materiales, apoyos, profundización, evidencia, criterios, decisión y versión de 45 minutos.
- Búsqueda, filtros, URL compartible, carga progresiva, tema y estados vacío/error.
- Sitemap, manifest, 404, metadatos, navegación de teclado, foco visible, diseño adaptable e impresión.
- Licencias separadas para software, contenido, datos y terceros.

## Comandos de reproducción

```bash
python scripts/generate_school_program.py
python scripts/validate_school_program.py
python scripts/validate_licensing.py
python -m unittest discover -s tests -p "test_*.py" -v
python -m compileall -q scripts tests
git diff --exit-code
```

La CI ejecuta los mismos gates antes de publicar Pages. El validador comprueba que cada clase marcada como desarrollada materialice su contrato en la fuente y en HTML. Estas comprobaciones verifican estructura y comportamiento observable; la revisión pedagógica y disciplinar humana se registra por separado en [EDITORIAL_STATUS.md](EDITORIAL_STATUS.md).
