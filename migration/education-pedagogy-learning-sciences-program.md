# Evaluación del programa de Pedagogía actual

Repositorio: `vladimiracunadev-create/education-pedagogy-learning-sciences-program`

## Correcto hoy

- código: MIT;
- contenido educativo: CC BY-NC-SA 4.0;
- terceros: excluidos de la licencia de contenido.

## Ajuste recomendado

El `LICENSE` actual limita expresamente MIT a `scripts/` y `tests/`. Si se incorporan
`school_knowledge/`, `app/`, `api/`, `cli/` u otros componentes, esa nota deja ambigüedad.

### Migración

1. reemplazar `LICENSE` por MIT puro;
2. crear `LICENSING.md`;
3. declarar ahí que MIT cubre todo software original salvo aviso específico;
4. mantener `LICENSE-CONTENT.md`;
5. añadir `DATA-LICENSE.md`, `THIRD_PARTY_NOTICES.md` y `TRADEMARKS.md`;
6. registrar por separado las licencias MINEDUC, libros, papers y datasets.

No es necesario cambiar la licencia de las 300 clases.
