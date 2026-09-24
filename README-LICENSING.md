# Guía rápida de licenciamiento

Resumen reutilizable del estándar. Para aprender el razonamiento completo, consulta el
[currículo](CURRICULUM.md); para aplicarlo, usa el [playbook](docs/IMPLEMENTATION_PLAYBOOK.md).

## Estándar

```text
SOFTWARE ORIGINAL            → MIT
CONTENIDO EDUCATIVO ORIGINAL → CC BY-NC-SA 4.0
DATOS / DATASETS              → licencia específica
FUENTES EXTERNAS              → licencia original
LICENCIA DESCONOCIDA          → cuarentena
TEXTOS ESCOLARES              → tratamiento restrictivo
MARCAS / LOGOS                → fuera de MIT/CC por defecto
```

## Aplicación

1. Auditar el repositorio real.
2. Clasificar código, contenido, datos, terceros y marca.
3. Ajustar `config/licensing-policy.json`.
4. Completar registro de fuentes.
5. Ejecutar validador y tests.
6. Integrar el workflow de CI.

## Regla de decisión

No elijas por el nombre de la licencia. Documenta primero el activo, quién controla los derechos,
el acto previsto, el canal de distribución, las obligaciones y la evidencia. Si falta uno de esos
datos, la decisión sigue abierta.

## Programa de Pedagogía

La combinación **MIT + CC BY-NC-SA 4.0** puede ser coherente cuando el titular desea adopción
amplia del software y reserva el uso comercial del contenido. No debe aplicarse a terceros ni
elegirse para otro repositorio sin verificar su objetivo y su cadena de titularidad.
