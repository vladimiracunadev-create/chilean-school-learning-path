# Matriz de decisión

Esta matriz organiza una investigación. No convierte una situación compleja en una respuesta automática.

## 1. Clasifica el activo

| Si el activo es… | Revisa primero | No asumas |
|---|---|---|
| código original | titularidad y contribuciones | que estar en GitHub lo vuelve open source |
| dependencia | licencia exacta, versión y distribución | que “gratis” significa sin condiciones |
| documentación o curso | autoría, fuentes, imágenes y adaptaciones | que MIT cubre el contenido por proximidad |
| dataset | procedencia, datos personales, contrato y estructura | que los hechos carecen de toda restricción |
| modelo/pesos | términos del modelo, dataset y uso previsto | que la licencia del código cubre los pesos |
| logo/nombre | titularidad y riesgo de confusión | que una licencia de copyright concede marca |
| secreto o dato personal | autorización, minimización y acceso | que una licencia pública sanea la publicación |

## 2. Define el acto

Documenta si habrá uso interno, modificación, enlace, entrenamiento, API, distribución de fuente,
binario o contenedor, SaaS, publicación web o venta. La respuesta puede cambiar según el acto.

## 3. Compara familias

| Familia | Redistribución | Derivados | Patente expresa | Uso típico |
|---|---|---|---|---|
| MIT/BSD | amplia, con avisos | no exige publicar | no expresa | adopción con obligaciones breves |
| Apache-2.0 | amplia, licencia y NOTICE cuando aplica | no exige publicar | sí | proyectos donde importa la concesión de patentes |
| MPL-2.0 | amplia | archivos cubiertos modificados | sí | copyleft por archivo |
| LGPL | amplia con condiciones | biblioteca/modificaciones según versión | revisar versión | bibliotecas reutilizables |
| GPL | distribución condicionada | fuente correspondiente de obra cubierta | según versión | reciprocidad fuerte |
| AGPL | incluye interacción remota en su alcance | fuente correspondiente ofrecida | sí en v3 | reciprocidad de red |
| CC BY | compartir/adaptar con atribución | no exige misma licencia | no diseñada para software | contenido abierto |
| CC BY-SA | compartir/adaptar con atribución | términos compatibles | no diseñada para software | contenido recíproco |
| CC BY-NC-SA | uso no comercial con atribución | mismos términos | no diseñada para software | contenido comunitario no comercial |

La versión, el texto completo y los hechos del caso mandan sobre este resumen.

## 4. Decide o escala

Cierra la decisión cuando conoces activo, titular, versión, acto, entrega, obligaciones y evidencia.
Escala cuando falte titularidad, exista incompatibilidad aparente, haya una patente relevante,
datos personales, uso comercial material, una disputa o una licencia personalizada.

## Registro mínimo

```text
Activo y versión:
Titular o fuente:
Uso y distribución previstos:
Licencia y evidencia:
Obligaciones:
Riesgos y supuestos:
Decisión:
Responsable, fecha y próxima revisión:
```

