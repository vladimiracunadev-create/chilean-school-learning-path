# Registros pedagógicos en Markdown y HTML

El proyecto publica **12.997 registros pedagógicos en ambos formatos**: **8.841 clases disciplinares** y **4.156 experiencias de integración transversal**. Las experiencias integradas documentan habilidades o actitudes dentro de clases de contenido y no aumentan la carga horaria como clases independientes. Cada OA posee un archivo Markdown y una página HTML, y cada registro conserva la misma ancla `cl-xxxxx` en ambos formatos.

| Formato | Cantidad | Uso principal |
|---|---:|---|
| Archivos Markdown por OA | 2.823 | edición, revisión, historial y reutilización |
| Páginas HTML por OA | 2.823 | lectura visual, navegación y accesibilidad web |
| Clases disciplinares | 8.841 | planificación autónoma desarrollada |
| Experiencias integradas | 4.156 | habilidad o actitud observada dentro del contenido |
| Registros con ancla en Markdown | 12.997 | enlace estable al contenido fuente |
| Registros con ancla en HTML | 12.997 | enlace estable para uso en navegador |

## Ejemplo de correspondencia

Un registro puede tener el código `CL-00746`:

- Markdown: `curriculum/1-basico/matematica/ma01-oa-01.md#cl-00746`
- HTML: `classes/1-basico/matematica/ma01-oa-01.html#cl-00746`

Los dos formatos conservan el mismo OA y las mismas anclas, pero su navegación está separada: un documento Markdown enlaza otros `.md`; una página de GitHub Pages enlaza otros `.html`. El validador recorre los 12.997 registros del catálogo y falla si falta un archivo, un ancla o aparece un cruce entre formatos.

## Qué incluye una clase desarrollada

Propósito, meta estudiantil, cinco momentos con tiempos, materiales, apoyo, profundización, evidencia, criterios, ticket, decisión posterior, versión de 45 minutos, tarea flexible, actividades complementarias, control de dificultades y coordinación de roles profesionales.

[Metodología](../METHODOLOGY.md) · [Índice curricular Markdown](../CURRICULUM.md) · [Volver al centro documental](README.md)
