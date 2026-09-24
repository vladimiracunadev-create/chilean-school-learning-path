# 🇨🇱 Trayectoria Escolar Chile

**2.823 OA inventariados · 12.997 clases · 1° básico a 4° medio**

> **Estado editorial:** las 12.997 clases están inventariadas, secuenciadas y publicadas. **1° básico está completamente desarrollado: 1.034 clases, 237 OA y 11 asignaturas**. El total desarrollado es 1.056 al incluir 22 clases piloto de otros niveles. La revisión humana sigue en curso y se informa sin inflar cifras en [EDITORIAL_STATUS.md](EDITORIAL_STATUS.md).

Repositorio educativo abierto para planificar lo que niñas, niños y jóvenes aprenden durante su trayectoria escolar en Chile. Cada propuesta identifica nivel, asignatura, tema, OA oficial, cobertura y evidencia, y desarrolla el aprendizaje en 4 a 7 clases según su amplitud.

[Explorar las 12.997 clases](https://vladimiracunadev-create.github.io/chilean-school-learning-path/) · [Malla completa](CURRICULUM.md) · [Estado editorial](EDITORIAL_STATUS.md) · [Guía pedagógica](TEACHING_GUIDE.md)

## De OA a clases enseñables

Cada OA se dosifica en 4 a 7 clases identificadas de manera estable. Una clase “secuenciada” declara la arquitectura mínima; una clase “desarrollada” añade propósito docente, consigna concreta, modelado disciplinar, práctica guiada e individual, materiales, apoyos, profundización, ticket, criterios observables y decisión posterior.

El desarrollo editorial avanza nivel por nivel. [1° básico](CURRICULUM.md#1-básico) está completo en Artes Visuales, Ciencias Naturales, Educación Física y Salud, Historia, Inglés (Propuesta), Lengua y Cultura de los Pueblos Originarios Ancestrales, Lenguaje y Comunicación, Matemática, Música, Orientación y Tecnología. También se conservan cuatro OA piloto ya desarrollados en 3°, 4° y 8° básico.

- **Dificultades:** ejemplos resueltos, pasos visibles, vocabulario anticipado, varias formas de respuesta y retiro gradual de apoyos, sin rebajar el OA.
- **Dominio temprano o aburrimiento:** comparación de estrategias, objeciones, casos límite y transferencia; profundizar no es entregar más ejercicios repetidos.
- **Realidad chilena:** alternativas sin conectividad, cursos numerosos y diversidad cultural, lingüística, sensorial y motriz; bloques adaptables a 45 o 90 minutos.
- **Trazabilidad:** cada OA enlaza su ficha de Currículum Nacional y conserva fecha de verificación.

## Alcance responsable

Incluye formación general común, propuestas MINEDUC, asignaturas según contexto y opciones de 3°–4° medio. Están etiquetadas y no representan una carga simultánea para cada estudiante. La dosificación es un punto de partida: el docente la ajusta con evidencia y el proyecto educativo.

Los Textos Escolares 2026 son recursos alineados. Las obras se denominan lecturas vinculadas o sugeridas cuando así aparecen en el portal; no se inventa obligatoriedad ni se reproducen obras protegidas.

## Uso

1. Elige nivel y asignatura.
2. Busca tema, eje, OA o palabra, con o sin tildes.
3. Abre una de las 12.997 clases desde el portal.
4. Revisa la secuencia completa, las fuentes y el estado editorial.
5. Usa la evidencia para mantener, acortar o ampliar la dosificación.

## Desarrollo y validación

Requiere Python 3.12. El sitio no usa dependencias JavaScript ni servicios externos.

```bash
python scripts/generate_school_program.py
python scripts/validate_school_program.py
python scripts/validate_licensing.py
python -m unittest discover -s tests -p "test_*.py" -v
```

El workflow regenera todos los artefactos, comprueba que no haya diferencias, ejecuta validadores y tests, y solo entonces publica GitHub Pages.

## Ecosistema

Se complementa con [Education, Pedagogy & Learning Sciences Program](https://github.com/vladimiracunadev-create/education-pedagogy-learning-sciences-program), orientado a formación docente. Los programas especializados del perfil permiten continuar en matemática, computación, IA, datos, ciberseguridad, nube, negocios y creación digital; no sustituyen las Bases Curriculares.

Snapshot verificado el **2026-09-24** desde [Currículum Nacional](https://www.curriculumnacional.cl/curriculum/cursos-y-niveles). El catálogo registra **595 enlaces de lectura** asociados por MINEDUC.

Proyecto independiente, sin representación del Ministerio de Educación de Chile.
