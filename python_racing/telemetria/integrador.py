"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/__init__.py
# ================================================================================

from python_racing.telemetria.sensores.temperatura_motor_sensor import TemperaturaMotorSensor
from python_racing.telemetria.sensores.combustible_sensor import CombustibleSensor
from python_racing.telemetria.sensores.velocidad_sensor import VelocidadSensor
from python_racing.telemetria.control.control_boxes_task import ControlBoxesTask

__all__ = [
    'TemperaturaMotorSensor',
    'CombustibleSensor',
    'VelocidadSensor',
    'ControlBoxesTask'
]

