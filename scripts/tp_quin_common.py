"""Ayudante de los cuadernos de Técnico-Profesional Química Industrial (3.º y 4.º medio; student_content_tp_quin_*, qula_*, qupl_*). Riesgo ALTO: solo conceptos, lectura de documentos, cálculos de planilla y reglas generales de seguridad."""
from __future__ import annotations

from hc_common import make_build

AVISO = ("Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente (por ejemplo, la autoridad sanitaria y ambiental de tu sector) y elementos de protección; "
         "este cuaderno no te habilita para trabajar en una planta ni en un laboratorio químico. Las tareas con sustancias y equipos las hace solo personal formado y autorizado por la empresa.")

EMER = ("Ante un derrame, una fuga, un olor extraño, humo, un incendio, una intoxicación, una descarga eléctrica o un equipo que funciona de forma anormal: no te acerques a la zona de riesgo, avisa a un adulto responsable y a emergencias.")

GOOD = "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias"
_BAD = [
    ("Acercarte un poco a mirar qué pasó para informar con más detalle", "Esperar unos minutos por si el problema se resuelve solo antes de avisar"),
    ("Intentar contener o limpiar el problema tú mismo con lo que haya a mano", "Esperar a que llegue tu jefe antes de llamar a nadie"),
    ("Ir a buscar elementos de protección y entrar a ayudar", "Sacar una foto de cerca para el informe antes de avisar"),
    ("Abrir una ventana o una puerta para ver mejor y luego avisar", "Seguir con la tarea hasta terminarla y avisar al final del turno"),
    ("Pedirle a un compañero que se asome mientras tú buscas el manual", "Intentar apagar el equipo tú mismo aunque no estés autorizado"),
    ("Entrar un momento a retirar tus cosas antes de salir", "Quedarte cerca de la zona para avisar a quien llegue"),
]


def em(scene: str, k: int = 0):
    """Ejercicio de conducta de emergencia (nivel desafío): siempre «no acercarse, avisar»."""
    b1, b2 = _BAD[k % len(_BAD)]
    return ("abc", f"{scene} ¿Qué corresponde según las reglas generales de seguridad?", GOOD, b1, b2,
            "Acercarse o intervenir sin formación puede sumar otra víctima; lo seguro es mantener distancia y avisar.")


MATERIALS = ("Lápiz, goma y papel (o cuaderno); una calculadora simple es opcional. No necesitas planta, laboratorio, reactivos, equipos, instrumentos, computador ni internet: las fichas, planillas, rótulos, registros e informes "
             "están escritos en el enunciado, son inventados y están rotulados «de ejemplo». Las medidas, masas, volúmenes, concentraciones, temperaturas, tiempos y costos son números de ejemplo "
             "para calcular en una planilla; los valores reales los fijan el proyecto, la empresa y «la norma vigente» de la autoridad sanitaria y ambiental. Este cuaderno no contiene procedimientos para preparar soluciones, mezclas o reacciones, manejar reactivos, ácidos, solventes o gases, "
             "operar reactores, hornos, calderas o equipos de planta, entrar a espacios confinados ni actuar ante derrames. La hoja de datos de seguridad se trabaja solo como lectura de documento. " + AVISO + " " + EMER)

build = make_build(MATERIALS)
