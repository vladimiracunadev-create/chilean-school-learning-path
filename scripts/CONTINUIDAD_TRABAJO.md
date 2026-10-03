# Continuidad interna · evaluaciones complementarias

Memoria operativa para continuar la tarea aunque la conversación se compacte. No forma parte del portal docente ni debe enlazarse desde el sitio.

## Petición vigente

- Trabajar directamente en `main`, sin ramas paralelas, y publicar sólo con validaciones y workflows verdes.
- Retirar **Prompt Maestro** de toda superficie pedagógica pública: es una instrucción de IA, no una categoría educativa.
- Sustituirlo por un estado de implementación organizado por capacidades pedagógicas, evidencia, límites y próximos pasos.
- Los JSON pueden seguir como fuente técnica, pero nunca como interfaz principal para docentes.
- Crear un Markdown propio, amplio y navegable para PAES, SIMCE, DIA, PISA, TIMSS, PIRLS, ERCE, ICILS, ICCS, ECES, Impulso Lector, Estudios Nacionales y evaluación interna.
- Enriquecer visualmente las páginas HTML sin mezclar formatos: Markdown enlaza Markdown; HTML enlaza HTML; PDF conserva la misma estructura documental.
- Explicar historia, razón de existencia, responsables, población, diseño, resultados, límites, instrumentos anteriores, fuentes, ejemplos, cálculo y conexión con clases existentes.
- PAES no puede conectarse sólo con 4° medio: debe mostrar antecedentes, consolidación y transferencia en varios niveles, distinguiendo la progresión pedagógica del temario oficial vigente.
- Las piezas actuales de dos preguntas cerradas y una respuesta abierta no son “ensayos”. Deben rotularse como **muestras breves calculables**. Un ensayo de ejemplo requiere matriz y tarea por cada eje declarado; un ensayo completo debe cubrir todos los contenidos de la versión del temario o marco.
- Conservar el informe de brechas previo como línea base histórica. No reescribir menciones históricas del changelog.
- No crear un preuniversitario, copiar ítems oficiales, inventar equivalencias, escalas ni validez psicométrica.

## Criterios de aceptación

1. Ninguna superficie pública actual titula o navega por “Prompt Maestro”.
2. Existen 13 documentos individuales en `docs/evaluaciones/`, más un índice Markdown.
3. Cada documento incluye explicación, historia, diseño, interpretación, uso docente, rutas, muestras y fuentes.
4. PAES muestra clases de varios niveles por área, rotuladas como correspondencia pedagógica inferida y diferenciadas del temario oficial.
5. Cada HTML enlaza la versión HTML del documento individual generado desde Markdown.
6. Ninguna muestra parcial se presenta como ensayo completo; cada afirmación de cobertura se prueba con matriz visible.
7. Los cálculos son puntos propios y nunca escalas oficiales.
8. Validadores, tests, enlaces, exportación PDF y QA visual pasan antes del commit.
9. README, centro documental, changelog, sitemap y conteos se sincronizan con hechos comprobados.

## Estado inicial de esta corrección

- `main` sincronizada con `origin/main`; último commit: `3ccfd534`.
- Base: 13 instrumentos/familias, 45 muestras breves hoy mal llamadas miniensayos, 77 pruebas y 51 PDFs.
- Problemas confirmados: `ESTADO_PROMPT_MAESTRO.md`, página `estado-prompt-maestro.html`, un solo Markdown principal para los 13 instrumentos y rutas PAES rotuladas como “Egreso y 4° medio”.

## Estado al cierre de implementación local

- Catálogo y generador reestructurados; la página pública de “Prompt Maestro” fue sustituida por estado de implementación pedagógica.
- Creadas 13 guías Markdown individuales y sus 13 versiones HTML para docentes.
- PAES muestra cinco rutas longitudinales con antecedentes desde educación básica y media, sin confundirlos con el temario oficial.
- Las 45 piezas breves se presentan como muestras calculables de cobertura parcial; el estado declara **0 ensayos completos**. Los botones, tarjetas y explicaciones ya no las llaman ensayos.
- Regenerados y verificados 64 PDF; cada instrumento posee su PDF separado y los documentos generales funcionan únicamente como índices.
- QA funcional realizado en navegador: centro de evaluaciones, ruta PAES, cálculo 4/4 de una muestra y estado de implementación.
- Suite completa verificada: 80 pruebas, incluida la prohibición de concatenar instrumentos en los Markdown generales.

## Publicación comprobada

- Implementación publicada directamente en `main` mediante el commit `6e4345fb` (`feat: conectar evaluaciones con trayectoria y cobertura`), sin ramas paralelas.
- Workflows **Calidad**, **Pages** y **Seguridad** completados correctamente para ese commit.
- Despliegue público comprobado en el centro de evaluaciones, la página PAES, el estado de implementación y la guía HTML individual de PAES.
- Árbol local limpio después de la publicación. No quedan acciones técnicas pendientes de este cierre.

## Próxima brecha pedagógica real

No confundir ampliación de contenido con mantenimiento de esta entrega. Construir ensayos completos exige, por cada versión, una matriz oficial vigente, tareas originales para **todos** sus contenidos, revisión disciplinar, reglas de puntuación que no simulen escalas oficiales y pilotaje. Hasta que eso exista, las 45 piezas permanecen correctamente rotuladas como muestras parciales.

