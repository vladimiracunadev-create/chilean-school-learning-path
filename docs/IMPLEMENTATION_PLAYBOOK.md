# Playbook de implementación

## 1. Descubrir

Congela el commit; inventaría código, contenido, datos, medios, binarios, modelos y marcas; extrae
dependencias; registra fuentes; deja como `UNKNOWN` lo que no puedas probar.

**Gate:** cada activo distribuido tiene fuente o titular y clasificación.

## 2. Analizar

Describe el acto y canal de entrega; lee licencia y versión; identifica avisos, fuente,
reciprocidad y restricciones; evalúa compatibilidad; separa conclusiones de supuestos.

**Gate:** cada decisión enlaza hechos verificables y declara límites.

## 3. Implementar

Coloca licencias canónicas; declara por separado contenido, datos, terceros y marca; añade avisos en
una superficie visible; normaliza SPDX; documenta permisos especiales con alcance y fecha.

**Gate:** una persona externa entiende qué cubre cada licencia.

## 4. Automatizar

Valida archivos y registros; falla ante `UNKNOWN` redistribuido; conserva SBOM y avisos; revisa
cambios de dependencias; bloquea releases con excepciones vencidas.

**Gate:** el mismo commit produce el mismo expediente.

## 5. Operar

Asigna responsables; mide cobertura y deuda; reaudita cambios de versión, entrega o negocio; ante
un incidente, contiene, preserva evidencia y remedia.

**Gate:** el programa detecta cambios y conserva memoria organizacional.

## Expediente de release

- commit/tag revisado;
- inventario o SBOM;
- licencias, avisos y atribuciones;
- fuentes, permisos y excepciones;
- evidencia de pruebas y aprobación;
- riesgos aceptados y próxima revisión.

