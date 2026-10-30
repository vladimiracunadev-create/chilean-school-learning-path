# Análisis de alineación con el OA oficial · 1.º básico

Este análisis contrasta cada cuaderno con el **texto oficial del OA** y con el **título de la clase planificada**: mide qué parte de sus términos de contenido aparece realmente en el cuaderno, la longitud media de las oraciones de la explicación y algunas señales pedagógicas débiles. **No** juzga exactitud disciplinar: ordena las clases para que una persona lea primero las más débiles. Se regenera con `python scripts/audit_alignment.py --write`.

Criterio de marca: cobertura del OA menor que 34 % **y** del título menor que 50 %, o explicación con oraciones de más de 16 palabras en promedio, o respuestas «depende» en ejercicios cerrados.

**Límite de la medida.** Es una heurística de triage por coincidencia de términos: sobre-marca, sobre todo en Inglés, donde el título planificado es metalenguaje docente («Connect prior knowledge») que no aparece en un cuaderno para estudiantes, y en las clases de Lengua y Cultura, cuyo título lleva rótulos de método. Una marca no prueba un defecto; una ausencia de marca no prueba exactitud.

## Resumen por asignatura

| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |
|---|---:|---:|---:|
| artes-visuales | 24 | 39 % | 6 |
| ciencias-naturales | 49 | 46 % | 3 |
| educacion-fisica-salud | 48 | 37 % | 14 |
| historia-geografia-ciencias-sociales | 68 | 46 % | 10 |
| ingles-propuesta | 69 | 28 % | 28 |
| lengua-cultura-pueblos-originarios-ancestrales | 129 | 44 % | 13 |
| lenguaje-comunicacion | 131 | 41 % | 6 |
| matematica | 83 | 51 % | 7 |
| musica | 29 | 51 % | 1 |
| orientacion | 35 | 41 % | 0 |
| tecnologia | 26 | 34 % | 0 |

**Clases marcadas para lectura prioritaria:** 88 de 691.

## Segunda lectura crítica de las 691 clases

Después de la validación automática, cada una de las 691 clases de 1.º básico fue releída de principio a fin por un segundo lector (asistido por IA, independiente de quien la escribió), que la contrastó con el texto del OA y el título de la clase en el currículo del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional: se usó el texto oficial reproducido en cada ficha.

| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |
|---|---:|---|
| Matemática | 83 | Dato falso sobre la derecha y la izquierda; centímetros y operaciones de 2.º básico en OA 18 y otros; contradicciones internas entre explicación y ejemplos; respuestas falsas en patrones y familias de operaciones. |
| Lenguaje y Comunicación | 131 | Conteos de palabras erróneos; datos falsos en textos (gatos que no nadan, osos pescando en invierno); definiciones y terminología silábica; léxico difícil sin definir; ejercicios de oralidad ambiguos. |
| Ciencias Naturales | 49 | Conclusiones no justificadas por los datos; cifras de seres vivos eliminadas o hechas cualitativas; datos de ejemplo rotulados; operaciones de otro nivel; avisos de seguridad. |
| Historia, Geografía y Ciencias Sociales | 68 | Edades calculadas sin considerar el mes; voto femenino (1934 y 1949 son leyes, no el día en que votaron); restas de años fuera de nivel; fechas de casos inventados; ambigüedades de mapas. |
| Inglés | 69 | Inglés incorrecto o antinatural; estructuras de otro nivel; vocabulario usado sin enseñarse; explicaciones en español falsas; expresiones del OA agregadas (/s/-/z/, I want, Here). |
| Lengua y Cultura de los Pueblos Originarios | 129 | Conteos de sílabas y palabras; afirmaciones culturales no seguras eliminadas o generalizadas; frase inventada retirada; preguntas que jerarquizaban identidad; aritmética de otro nivel. |
| Educación Física y Salud | 48 | Riesgos motores (retroceder de espaldas); equivalencias falsas («dos brazos» = 2 m); cifras de salud generalizadas; ejercicios imposibles de practicar. |
| Orientación | 35 | Lenguaje de las clases de cuerpo y protección ajustado («no es tu culpa», nada es un secreto); ambigüedades; operaciones de otro nivel; seguridad con tijeras. |
| Música | 29 | Conteos de pulsos y sílabas erróneos; contradicciones entre consigna y ejemplo; objetos de vidrio y martillo reemplazados por opciones seguras. |
| Artes Visuales | 24 | Multiplicaciones y restas de años de otro nivel; datos de obras dudosos; ambigüedades. |
| Tecnología | 26 | Instrucciones de seguridad incorrectas; respuesta contraria a lo enseñado; multiplicaciones; software ficticio rotulado. |

### Vacíos de cobertura frente al OA que no se resolvieron

- **Inglés:** el contraste /w/-/th/ del OA 03 y los temas de ocupaciones y comida del OA 07 no están cubiertos; falta decidir si se agrega una clase o se redistribuye.
- **Tecnología:** OA 03 (técnicas y materiales como fibras y plásticos) y OA 06 (simuladores y libros digitales) necesitan ampliar clases.
- **Lenguaje:** OA 17 y OA 09 piden obras completas y poemas de autor; el cuaderno usa textos originales breves por derechos de autor.
- **Lengua y Cultura de los Pueblos Originarios:** las clases de lengua se practican sólo con castellano y el saludo «mari mari»; el aprendizaje de la lengua real queda en manos del educador o educadora tradicional.
- **Historia:** quedan restas de años de cuatro cifras (resultados de hasta unos 56) que un especialista debe decidir si deja o cambia por comparación de años.

Todos los contenidos que requieren especialista, incluida la verificación contra el Programa de Estudio oficial, siguen listados en [Revisión profesional pendiente](REVISION_PENDIENTE_CUADERNOS.md).

## Clases marcadas

| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |
|---|---:|---|---:|---:|---:|---|
| EN01 OA 07 | 5 | Read actions happening now | 7 % | 0 % | 14.9 | — |
| EN01 OA 02 | 3 | Objects, possession and quantity | 8 % | 0 % | 12.8 | — |
| EN01 OA 02 | 2 | People and abilities | 8 % | 0 % | 12.6 | — |
| EN01 OA 02 | 1 | School instructions | 11 % | 50 % | 16.1 | — |
| EN01 OA 07 | 4 | Location and information questions | 12 % | 33 % | 7.1 | — |
| LE01 OA 23 | 3 | Describir para hacer visible | 12 % | 33 % | 14.1 | — |
| EN01 OA 03 | 3 | Notice frequent expressions | 12 % | 33 % | 10.5 | — |
| EN01 OA 02 | 4 | Places and location | 13 % | 0 % | 10.4 | — |
| EN01 OA 02 | 5 | Actions happening now | 13 % | 0 % | 9.7 | — |
| EN01 OA 07 | 2 | Ability, feeling and possession | 14 % | 0 % | 8.5 | — |
| EN01 OA 04 | 4 | Focus on key words | 14 % | 0 % | 10.0 | — |
| EF01 OA 07 | 2 | Juego tradicional contextualizado | 15 % | 67 % | 19.6 | — |
| EN01 OA 10 | 2 | Explore /th/ safely | 15 % | 0 % | 10.9 | — |
| EN01 OA 11 | 3 | Use objects and gestures | 17 % | 0 % | 9.8 | — |
| EN01 OA 11 | 5 | Interact after presenting | 17 % | 33 % | 7.3 | — |
| EN01 OA 12 | 5 | Location and current action | 18 % | 0 % | 19.9 | — |
| EN01 OA 12 | 2 | Ability and quantity | 19 % | 0 % | 19.3 | — |
| EN01 OA 03 | 4 | Distinguish key English sounds | 21 % | 33 % | 11.5 | — |
| EN01 OA 11 | 1 | Enter classroom interaction | 21 % | 0 % | 11.7 | — |
| EF01 OA 04 | 2 | Adaptar locomoción | 21 % | 0 % | 12.2 | — |
| EN01 OA 05 | 2 | Show meaning through drawing | 22 % | 0 % | 12.2 | — |
| LC01 OA LF02 | 4 | Lengua en uso · Contrastar con cuidado | 23 % | 33 % | 14.0 | — |
| EF01 OA 01 | 3 | Lanzar y recibir | 23 % | 100 % | 16.2 | — |
| EN01 OA 05 | 5 | Express a preference or feeling | 24 % | 33 % | 11.8 | — |
| EF01 OA 04 | 1 | Leer el entorno | 25 % | 0 % | 14.8 | — |
| EN01 OA 03 | 2 | Follow simple instructions | 25 % | 33 % | 12.1 | — |
| AR01 OA 01 | 5 | Ampliar la mirada latinoamericana y universal | 27 % | 25 % | 15.2 | — |
| EN01 OA 03 | 1 | Identify characters and objects | 27 % | 33 % | 16.0 | — |
| LC01 OA LS06 | 2 | Primer acercamiento · Escucha focalizada | 27 % | 25 % | 9.7 | — |
| LC01 OA LS06 | 3 | Primer acercamiento · Símbolo y soporte digital | 27 % | 40 % | 13.2 | — |
| EF01 OA 01 | 1 | Locomoción con control | 28 % | 100 % | 17.0 | — |
| EF01 OA 09 | 3 | Agua y colación | 28 % | 100 % | 17.7 | — |
| LE01 OA 05 | 2 | Releer para ganar continuidad | 28 % | 33 % | 9.9 | — |
| LE01 OA 07 | 1 | Explorar un repertorio | 28 % | 0 % | 8.1 | — |
| LE01 OA 10 | 1 | Carta y nota: quién comunica | 28 % | 100 % | 17.1 | — |
| EN01 OA 04 | 3 | Use images without guessing only | 29 % | 33 % | 12.0 | — |
| EN01 OA 09 | 4 | Write a supported reaction | 29 % | 33 % | 10.4 | — |
| LC01 OA LS04 | 3 | Primer acercamiento · Conectar con cuidado | 29 % | 25 % | 10.0 | — |
| EF01 OA 08 | 4 | Señales para regular o detener | 30 % | 33 % | 11.5 | — |
| LC01 OA LS04 | 2 | Primer acercamiento · Recuperar información cultural | 30 % | 40 % | 11.2 | — |
| EN01 OA 06 | 5 | Demonstrate understanding | 30 % | 0 % | 11.5 | — |
| MA01 OA 07 | 4 | Dobles y elección de estrategia | 31 % | 67 % | 18.0 | — |
| EN01 OA 05 | 1 | Connect safely to experience | 32 % | 33 % | 15.9 | — |
| EN01 OA 06 | 3 | Track characters and actions | 33 % | 33 % | 11.4 | — |
| EN01 OA 10 | 3 | Contrast /s/ and /z/ | 33 % | 0 % | 13.8 | — |
| LC01 OA LF06 | 5 | Lengua en uso · Guardar la procedencia | 33 % | 100 % | 18.7 | — |
| LC01 OA LR04 | 3 | Recuperar la lengua · Conectar con cuidado | 33 % | 25 % | 13.1 | — |
| LE01 OA 24 | 1 | Escuchar una palabra nueva | 33 % | 100 % | 16.2 | — |
| LE01 OA 11 | 1 | Un libro ofrece pistas | 38 % | 67 % | 16.4 | — |
| EF01 OA 04 | 4 | Ruta segura | 38 % | 100 % | 16.6 | — |
| EF01 OA 05 | 3 | Una idea en movimiento | 38 % | 100 % | 16.6 | — |
| EF01 OA 01 | 5 | Circuito combinado | 39 % | 50 % | 17.5 | — |
| HI01 OA 14 | 2 | Buena convivencia | 40 % | 100 % | 18.1 | — |
| MA01 OA 13 | 1 | Derecha e izquierda en mi cuerpo | 40 % | 100 % | 13.9 | respuesta «depende» en ejercicio cerrado |
| AR01 OA 01 | 6 | Obra con punto de vista propio | 41 % | 100 % | 20.0 | — |
| AR01 OA 04 | 1 | Detenerse a observar | 41 % | 50 % | 17.0 | — |
| EF01 OA 09 | 1 | Higiene después de moverse | 42 % | 67 % | 16.7 | — |
| LC01 OA LS01 | 1 | Primer acercamiento · Entrar por la escucha completa | 43 % | 60 % | 16.7 | — |
| MA01 OA 17 | 4 | Leer fechas significativas | 44 % | 100 % | 17.6 | — |
| HI01 OA 13 | 4 | Igualdad y no discriminación | 45 % | 100 % | 17.3 | — |
| EN01 OA 01 | 1 | Listen for the text type | 46 % | 100 % | 17.0 | — |
| HI01 OA 11 | 3 | Interdependencia local | 46 % | 100 % | 11.6 | respuesta «depende» en ejercicio cerrado |
| CN01 OA 07 | 1 | Rutinas que cuidan | 47 % | 100 % | 17.0 | — |
| MU01 OA 05 | 2 | Pregunta y respuesta | 47 % | 100 % | 11.6 | respuesta «depende» en ejercicio cerrado |
| HI01 OA 06 | 5 | Muestra cultural respetuosa | 48 % | 100 % | 19.1 | — |
| AR01 OA 03 | 1 | Laboratorio de materiales | 50 % | 100 % | 20.0 | — |
| AR01 OA 04 | 4 | Galería comparada | 50 % | 100 % | 19.1 | — |
| CN01 OA 11 | 1 | Observar el cielo diario | 50 % | 67 % | 20.4 | — |
| EF01 OA 06 | 2 | Circuito continuo | 50 % | 100 % | 16.1 | — |
| EF01 OA 07 | 1 | Moverse en la rutina | 50 % | 100 % | 17.4 | — |
| HI01 OA 05 | 3 | Conmemoraciones y memoria | 50 % | 50 % | 19.3 | — |
| HI01 OA 14 | 4 | Vía pública y autocuidado | 50 % | 100 % | 19.0 | — |
| MA01 OA 19 | 4 | Responder con evidencia | 50 % | 100 % | 17.0 | — |
| HI01 OA 06 | 2 | Fiestas y tradiciones | 52 % | 100 % | 24.5 | — |
| AR01 OA 03 | 2 | Herramientas y seguridad | 53 % | 100 % | 26.6 | — |
| MA01 OA 02 | 2 | Del sexto al décimo | 56 % | 100 % | 16.6 | — |
| LC01 OA 10 | 1 | Observar relaciones | 60 % | 100 % | 18.1 | — |
| LC01 OA 12 | 4 | Aprendizaje sin escenificación | 60 % | 100 % | 16.3 | — |
| CN01 OA 12 | 4 | Informe estacional local | 64 % | 67 % | 16.7 | — |
| MA01 OA 13 | 4 | Posiciones en un plano simple | 64 % | 100 % | 17.0 | — |
| LC01 OA LF03 | 2 | Lengua en uso · Toponimia con territorio | 64 % | 100 % | 16.9 | — |
| LC01 OA LF05 | 1 | Lengua en uso · Mirar con procedencia | 67 % | 67 % | 17.9 | — |
| HI01 OA 11 | 1 | Trabajo visible e invisible | 71 % | 100 % | 16.8 | — |
| HI01 OA 09 | 4 | Ruta de localización | 73 % | 100 % | 20.0 | — |
| EF01 OA 08 | 2 | Cambios durante el esfuerzo | 74 % | 100 % | 16.3 | — |
| HI01 OA 15 | 2 | Personas que la hacen funcionar | 76 % | 100 % | 21.6 | — |
| LC01 OA 11 | 2 | Fuente cultural | 78 % | 100 % | 17.9 | — |
| MA01 OA 18 | 1 | Largo y corto en un objeto | 86 % | 100 % | 13.8 | respuesta «depende» en ejercicio cerrado |
