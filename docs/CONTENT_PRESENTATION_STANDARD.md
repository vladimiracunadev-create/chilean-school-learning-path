# Estándar de presentación para Markdown, HTML y PDF

Este estándar mantiene una experiencia visual coherente sin convertir tres formatos en tres fuentes distintas. Markdown es la representación canónica de lectura y edición; HTML y PDF son salidas derivadas para navegación web e impresión.

[Flujo de contenido](CONTENT_LIFECYCLE.md) · [Formatos](FORMATOS.md) · [Descargas PDF](PDFS.md) · [Estándar de calidad](../QUALITY_STANDARD.md)

## Principio de correspondencia

```text
fuente estructurada
  → Markdown canónico
      → HTML navegable
      → PDF imprimible
```

- Un documento **Markdown enlaza su equivalente Markdown**.
- Una página **HTML enlaza su equivalente HTML**.
- Un **PDF se genera desde Markdown** y transforma esos enlaces en referencias clicables a la fuente canónica del repositorio.
- Una URL externa conserva su formato original; esta regla no reescribe fuentes oficiales o repositorios ajenos.
- El portal público raíz puede enlazarse desde Markdown como punto de entrada al producto. Las páginas HTML internas no sustituyen los enlaces Markdown del repositorio.

## Contrato visual de Markdown

Todos los archivos `.md` versionados deben cumplir:

1. UTF-8 sin BOM y salto de línea final;
2. exactamente un título H1 identificable;
3. jerarquía de encabezados sin saltar niveles;
4. títulos ATX con espacio (`## Título`, no `##Título`);
5. bloques de código cercados y balanceados;
6. texto de enlace visible y destino no vacío;
7. enlaces internos relativos, existentes y propios de la superficie Markdown;
8. tablas con encabezado y separador legibles;
9. párrafos, listas, tablas y bloques separados con espacio suficiente;
10. estado, fuente y límites visibles cuando el documento realiza afirmaciones curriculares o editoriales.

`README.md` y `docs/README.md` pueden abrir con un contenedor centrado antes del H1 para su portada. Esa excepción no permite ocultar más de un H1 ni usar HTML para reemplazar la estructura semántica.

## Patrón visual recomendado

```markdown
# Título único

Resumen breve que explica propósito y alcance.

[Navegación relacionada](FORMATOS.md)

## Sección

Texto introductorio antes de tablas o listas.

| Campo | Significado |
|---|---|
| Ejemplo | Contenido |

## Fuentes y límites

- Fuente primaria.
- Estado editorial.
- Aspectos pendientes de revisión.
```

Los emoji pueden orientar secciones de índices y portadas, pero no reemplazan etiquetas textuales. El énfasis se usa para jerarquía, no para decorar cada frase.

## Contrato visual de HTML

Las páginas generadas deben conservar:

- `lang="es"`, título, navegación principal y un único contenido principal;
- orden semántico de encabezados equivalente al Markdown;
- contraste, foco visible, navegación por teclado y enlace para saltar al contenido;
- tablas desplazables en pantallas estrechas;
- enlaces HTML internos, nunca rutas `.md` locales;
- estado editorial, fuentes y límites presentes en la fuente canónica;
- diseño adaptable, sin exigir una cuenta ni telemetría.

El HTML se corrige desde el generador, la plantilla o el Markdown fuente. No se parchean miles de páginas derivadas manualmente.

## Contrato visual de PDF

Las 51 compilaciones deben:

- generarse únicamente con `scripts/export_pdfs.py` desde Markdown canónico;
- mostrar título, alcance, corte documental y estado editorial en la portada;
- incluir metadatos de título, autor, asunto, creador y versión documental;
- ofrecer tabla de contenido, numeración y marcadores por cada fuente incluida;
- conservar encabezados, listas, tablas, avisos, código y enlaces en forma legible;
- incrustar tipografías con su aviso de licencia;
- mantener cada fuente una sola vez dentro de una compilación;
- permanecer bajo 100 MiB y tener texto extraíble;
- enlazar las fichas OA a la fuente Markdown canónica del commit publicado.

Un PDF no es una cuarta fuente ni puede declarar una versión distinta. Las diferencias binarias producidas por motores tipográficos en sistemas operativos distintos no son un cambio de contenido; la CI compara estructura, metadatos, inventario, fuentes, enlaces y texto extraíble.

## Validación automatizada

```bash
python scripts/validate_content_presentation.py
python scripts/export_pdfs.py --validate-only
```

El primer comando recorre todos los Markdown y HTML versionados. El segundo valida las 51 salidas PDF. Ambos se ejecutan en Calidad y Pages antes de publicar.

## Responsabilidad editorial

La automatización detecta estructura y sincronización; no decide si una explicación es pedagógicamente clara. La revisión humana debe comprobar lectura continua, densidad, lenguaje apropiado, accesibilidad, pertinencia cultural y fidelidad disciplinar en las tres representaciones.
