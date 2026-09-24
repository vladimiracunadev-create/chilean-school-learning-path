# Clases en Markdown y HTML

El proyecto publica **12.997 clases en ambos formatos**. No existen dos contenidos diferentes: cada OA posee un archivo Markdown y una página HTML, y dentro de ambos cada clase tiene la misma ancla `cl-xxxxx`.

| Formato | Cantidad | Uso principal |
|---|---:|---|
| Archivos Markdown por OA | 2.823 | edición, revisión, historial y reutilización |
| Páginas HTML por OA | 2.823 | lectura visual, navegación y accesibilidad web |
| Clases con ancla en Markdown | 12.997 | enlace estable al contenido fuente |
| Clases con ancla en HTML | 12.997 | enlace estable para uso en navegador |

## Ejemplo de correspondencia

Una clase puede tener el código `CL-00746`:

- Markdown: `curriculum/1-basico/matematica/ma01-oa-01.md#cl-00746`
- HTML: `classes/1-basico/matematica/ma01-oa-01.html#cl-00746`

Los dos formatos conservan el mismo OA y las mismas anclas, pero su navegación está separada: un documento Markdown enlaza otros `.md`; una página de GitHub Pages enlaza otros `.html`. El validador recorre las 12.997 entradas del catálogo y falla si falta un archivo, un ancla o aparece un cruce entre formatos.

## Qué incluye una clase desarrollada de 1° básico

Propósito, meta estudiantil, cinco momentos con tiempos, materiales, apoyo, profundización, evidencia, criterios, ticket, decisión posterior, versión de 45 minutos, tarea flexible, actividades complementarias, control de dificultades y coordinación de roles profesionales.

[Metodología](../METHODOLOGY.md) · [Índice curricular Markdown](../CURRICULUM.md) · [Volver al centro documental](README.md)
