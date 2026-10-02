# Registros pedagógicos en Markdown y HTML

El proyecto publica **12.997 registros pedagógicos en ambos formatos**: **8.841 clases disciplinares** y **4.156 experiencias de integración transversal**. Las experiencias integradas documentan habilidades o actitudes dentro de clases de contenido y no aumentan la carga horaria como clases independientes. Cada OA posee un archivo Markdown y una página HTML, y cada registro conserva la misma ancla `cl-xxxxx` en ambos formatos.

| Formato | Cantidad | Uso principal |
|---|---:|---|
| Archivos Markdown por OA | 2.823 | edición, revisión, historial y reutilización |
| Páginas HTML por OA | 2.823 | lectura visual, navegación y accesibilidad web |
| Compilaciones PDF | 49 | descarga por etapa, nivel, asignatura o programa completo |
| Clases disciplinares | 8.841 | planificación autónoma desarrollada |
| Experiencias integradas | 4.156 | habilidad o actitud observada dentro del contenido |
| Registros con ancla en Markdown | 12.997 | enlace estable al contenido fuente |
| Registros con ancla en HTML | 12.997 | enlace estable para uso en navegador |

## Ejemplo de correspondencia

Un registro puede tener el código `CL-00746`:

- Markdown: `curriculum/1-basico/matematica/ma01-oa-01.md#cl-00746`
- HTML: `classes/1-basico/matematica/ma01-oa-01.html#cl-00746`

Los dos formatos conservan el mismo OA y las mismas anclas, pero su navegación está separada: un documento Markdown enlaza otros `.md`; una página de GitHub Pages enlaza otros `.html`. El validador recorre los 12.997 registros del catálogo y falla si falta un archivo, un ancla o aparece un cruce entre formatos.

## Compilaciones PDF

El [centro de descargas PDF](PDFS.md) ofrece Educación Básica completa, Enseñanza Media completa, un archivo para cada uno de los doce niveles, un archivo para cada una de las 34 denominaciones curriculares y una compilación general con toda la documentación. Cada PDF reúne las guías e índices, mantiene enlaces clicables a las fichas OA detalladas y declara el estado editorial vigente.

Las salidas se regeneran con `python scripts/export_pdfs.py`. La integración continua exige que los 49 archivos coincidan con sus fuentes Markdown antes de publicar GitHub Pages.

## Qué incluye una clase desarrollada

Propósito, meta estudiantil, cinco momentos con tiempos, materiales, apoyo, profundización, evidencia, criterios, ticket, decisión posterior, versión de 45 minutos, tarea flexible, actividades complementarias, control de dificultades y coordinación de roles profesionales.

[Metodología](../METHODOLOGY.md) · [Índice curricular Markdown](../CURRICULUM.md) · [Volver al centro documental](README.md)
