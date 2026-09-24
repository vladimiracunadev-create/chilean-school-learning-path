# Reporte de validación

Fecha: 2026-09-24

## Alcance verificable

- 12.997 clases con código único y ancla web estable.
- 2.823 OA con página HTML, Markdown y trazabilidad a Currículum Nacional.
- 12 niveles, 35 asignaturas y 595 vínculos de lectura.
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

La CI ejecuta los mismos gates antes de publicar Pages. Estas comprobaciones verifican estructura y comportamiento observable; la revisión pedagógica y disciplinar humana se registra por separado en [EDITORIAL_STATUS.md](EDITORIAL_STATUS.md).
