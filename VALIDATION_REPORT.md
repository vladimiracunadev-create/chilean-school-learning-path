# Reporte de validación

Fecha: 2026-10-02

## Alcance verificable

- 12.997 registros pedagógicos con código único y ancla web estable: 8.841 clases disciplinares y 4.156 experiencias de integración transversal.
- 2.823 OA con página HTML, Markdown y trazabilidad a Currículum Nacional.
- 12 niveles, 35 asignaturas y 595 vínculos de lectura.
- 691 clases de 1° básico, 721 de 2°, 757 de 3°, 811 de 4°, 920 de 5°, 952 de 6°, 760 de 7°, 771 de 8°, 753 de 1° medio, 744 de 2° medio, 495 de 3° medio y 466 de 4° medio: 8.841 desarrolladas en total; 4.156 experiencias transversales integradas y 0 revisiones humanas registradas.
- Desde 1° básico hasta 4° medio completos internamente, con 0 propuestas pendientes dentro de los doce niveles.
- 3° medio completo internamente: 98 OA y 495 clases en dieciocho denominaciones, con fuentes oficiales y criterios pedagógicos internos rotulados.
- 4° medio completo internamente: 91 OA y 466 clases en diecisiete denominaciones, con fuentes oficiales y criterios pedagógicos internos rotulados.
- Las 35 guías de 3° y 4° medio publican 189 explicaciones pedagógicas OA por OA con punto de entrada, conceptos, progresión, evidencia y fuente oficial.
- 8° básico completo en doce denominaciones curriculares, con 771 clases y 430 experiencias integradas.
- Las once denominaciones de 1° medio están completas, con 753 clases y 456 experiencias integradas; no quedan propuestas secuenciadas ni borradores en el nivel.
- Las once denominaciones de 2° medio están completas, con 744 clases y 456 experiencias integradas; el nivel conserva 0 propuestas secuenciadas.
- 4° básico completo: 175 OA disciplinares, 811 clases y 93 OA transversales integrados mediante 384 experiencias.
- 0 clases declaradas como revisadas sin evidencia humana.
- Contrato editorial estructurado con propósito, meta, cinco momentos, materiales, apoyos, profundización, evidencia, criterios, decisión y versión de 45 minutos.
- Búsqueda, filtros, URL compartible, carga progresiva, tema y estados vacío/error.
- Sitemap, manifest, 404, metadatos, navegación de teclado, foco visible, diseño adaptable e impresión.
- Licencias separadas para software, contenido, datos y terceros.
- Taxonomía versionada de siete dominios, seis progresiones longitudinales demostrativas y relaciones muchos-a-muchos con OA existentes.
- Seis tareas originales que demuestran selección, respuesta abierta, resolución, interpretación y proyecto interdisciplinario; su estado no implica validación psicométrica.
- Seis marcos de evaluación desacoplados, con fuente, versión, población, limitaciones y tipo de correspondencia.
- Ciclo sintético de evidencia cerrado y motor determinista sin porcentajes ficticios ni datos personales.
- 62 pruebas automáticas y tres workflows: Calidad, Pages y Seguridad.

## Comandos de reproducción

```bash
python scripts/generate_school_program.py
python scripts/generate_competency_portal.py
python scripts/export_pdfs.py
python scripts/validate_school_program.py
python scripts/validate_licensing.py
python scripts/validate_competency_system.py
python scripts/generate_competency_portal.py --check
python -m unittest discover -s tests -p "test_*.py" -v
python -m compileall -q scripts tests
python scripts/mojibake_probe.py .
git diff --exit-code -- . ':(exclude)output/pdf/*.pdf'
```

La CI ejecuta los mismos gates antes de publicar Pages. Los artefactos textuales se comparan byte a byte; los 49 PDF se regeneran y verifican semántica y estructuralmente porque ReportLab puede producir bytes distintos entre sistemas operativos. El validador comprueba que cada clase marcada como desarrollada materialice su contrato en la fuente y en HTML. Estas comprobaciones verifican estructura y comportamiento observable; la revisión pedagógica y disciplinar humana se registra por separado en [EDITORIAL_STATUS.md](EDITORIAL_STATUS.md).
