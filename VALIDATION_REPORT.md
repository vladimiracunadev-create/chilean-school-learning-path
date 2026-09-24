# Reporte de validación

Fecha: 2026-09-24

## Alcance verificado

- 192 clases con página propia y catálogo JSON.
- 16 asignaturas, cada una con 12 clases.
- 4 niveles, cada uno con 48 clases.
- Tema, asignatura, nivel, resultado, práctica y evidencia en cada registro.
- Política MIT + CC BY-NC-SA 4.0 y cuarentena de fuentes desconocidas.
- Manifiesto, enlaces Markdown locales y archivos esenciales del portal.
- Regeneración determinista del currículo sin diferencias.

## Comandos

```bash
python scripts/generate_curriculum.py
python scripts/validate_licensing.py
python -m unittest discover -s tests -p "test_*.py" -v
```

## Resultado

```text
OK: 192 clases, 16 asignaturas, 4 niveles y política de licenciamiento validados.
Ran 12 tests — OK
```

La automatización verifica estructura y hechos observables. No determina titularidad, compatibilidad
jurídica ni licitud de un caso concreto sin la evidencia humana correspondiente.
