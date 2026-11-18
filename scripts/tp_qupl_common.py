"""Ayudante de la mención Planta Química (4.º medio TP). Reutiliza los textos de seguridad de tp_quin_common."""
from __future__ import annotations

from hc_common import make_build
from tp_quin_common import AVISO, EMER, em, GOOD, MATERIALS as _M

MATERIALS = _M.replace("No necesitas planta, laboratorio, reactivos", "No necesitas laboratorio, planta, reactivos")
build = make_build(MATERIALS)
