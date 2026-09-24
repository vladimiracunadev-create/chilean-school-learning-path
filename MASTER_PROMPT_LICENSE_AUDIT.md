# Prompt maestro — auditoría e implementación de licencias

Trabaja únicamente sobre el repositorio indicado.

## Regla 0

Antes de cambiar cualquier licencia:
1. revisar árbol, README, LICENSE, dependencias, generadores, datos y fuentes;
2. distinguir código, contenido educativo, datos, terceros, marca y artefactos generados;
3. no relicenciar contenido que el autor del repositorio no controla;
4. no borrar atribuciones existentes;
5. no editar artefactos generados si existe una fuente de verdad.

## Estándar objetivo

- software original → MIT;
- contenido educativo original → CC BY-NC-SA 4.0;
- datasets → licencia específica;
- terceros → licencia original;
- UNKNOWN → cuarentena;
- marcas/logos → fuera de MIT/CC por defecto.

## Auditoría

Clasifica cada directorio como:
`SOFTWARE`, `EDUCATIONAL_CONTENT`, `DATA`, `THIRD_PARTY`, `BRAND`, `GENERATED` o `UNKNOWN`.

## Implementación

- `LICENSE`: MIT puro.
- `LICENSE-CONTENT.md`: CC BY-NC-SA 4.0.
- `LICENSING.md`: alcance y precedencia.
- `DATA-LICENSE.md`: política de datos.
- `THIRD_PARTY_NOTICES.md`: terceros.
- `TRADEMARKS.md`: marca.
- registro de fuentes con licencia/estado.
- README con resumen de licencias.
- CI que valide la política.

## Reglas estrictas

- No marcar `UNKNOWN` como redistribuible.
- No almacenar/redistribuir textos escolares completos sin derechos explícitos.
- No aplicar CC BY-NC-SA a obras de terceros.
- No asumir que contenido público o descargable es dominio público.
- No afirmar CI verde sin ejecutar pruebas.
- No cambiar licencias existentes de dependencias.

## Entrega

1. inventario por directorio;
2. archivos de licencia;
3. registro de terceros;
4. política de datos;
5. política de marca;
6. README actualizado;
7. validador y tests;
8. riesgos/pending;
9. lista de recursos con licencia desconocida;
10. cambios listos para revisión.
