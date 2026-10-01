# Reporte de validación

Fecha: 2026-09-30

## Alcance verificable

- 12.997 clases con código único y ancla web estable.
- 2.823 OA con página HTML, Markdown y trazabilidad a Currículum Nacional.
- 12 niveles, 35 asignaturas y 595 vínculos de lectura.
- 691 clases de 1° básico, 721 de 2°, 757 de 3°, 811 de 4°, 920 de 5°, 952 de 6°, 760 de 7°, 771 de 8° y 586 de seis denominaciones de 1° medio: 6.969 desarrolladas en total; 3.583 experiencias transversales integradas y 0 revisiones humanas registradas.
- 1° a 8° básico completos, con 0 propuestas pendientes dentro de esos niveles.
- 8° básico completo en doce denominaciones curriculares, con 771 clases y 430 experiencias integradas.
- Matemática, Lengua y Literatura, Ciencias Naturales, Historia, Inglés e Inglés (Propuesta) de 1° medio completas, con 586 clases y 339 experiencias integradas; las otras cinco asignaturas conservan 284 propuestas secuenciadas.
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
