# Reporte de validación

Fecha: 2026-09-30

## Alcance verificable

- 12.997 clases con código único y ancla web estable.
- 2.823 OA con página HTML, Markdown y trazabilidad a Currículum Nacional.
- 12 niveles, 35 asignaturas y 595 vínculos de lectura.
- 691 clases de 1° básico, 721 de 2°, 757 de 3°, 811 de 4°, 920 de 5°, 952 de 6°, 760 de 7°, 771 de 8°, 753 de 1° medio y 744 de 2° medio: 7.880 desarrolladas en total; 4.156 experiencias transversales integradas y 0 revisiones humanas registradas.
- Desde 1° básico hasta 2° medio completos, con 0 propuestas pendientes dentro de esos diez niveles.
- 8° básico completo en doce denominaciones curriculares, con 771 clases y 430 experiencias integradas.
- Las once denominaciones de 1° medio están completas, con 753 clases y 456 experiencias integradas; no quedan propuestas secuenciadas ni borradores en el nivel.
- Las once denominaciones de 2° medio están completas, con 744 clases y 456 experiencias integradas; el nivel conserva 0 propuestas secuenciadas.
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
