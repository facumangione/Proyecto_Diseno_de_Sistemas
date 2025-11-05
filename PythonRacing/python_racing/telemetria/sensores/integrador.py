"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/__init__.py
# ================================================================================

"""
Sensores de telemetría
"""


# ================================================================================
# ARCHIVO 2/4: combustible_sensor.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/combustible_sensor.py
# ================================================================================

import threading
import time
from python_racing.patrones.observer.observable import Observable
from python_racing.entidades.motos.moto import Moto
from constante import INTERVALO_COMBUSTIBLE


class CombustibleSensor(threading.Thread, Observable[dict]):
    """Sensor de nivel de combustible con notificaciones estructuradas."""
    
    def __init__(self, moto: Moto):
        threading.Thread.__init__(self, daemon=True, name="CombustibleSensor")
        Observable.__init__(self)
        self._moto = moto
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        while not self._detenido.is_set():
            nivel = self._leer_nivel()
            
            # Enviar evento estructurado
            evento = {
                'tipo': 'combustible',
                'valor': nivel,
                'unidad': '%',
                'timestamp': time.time()
            }
            
            self.notificar_observadores(evento)
            time.sleep(INTERVALO_COMBUSTIBLE)

    def _leer_nivel(self) -> float:
        """Lee el nivel de combustible actual."""
        return self._moto.get_porcentaje_combustible()

    def detener(self) -> None:
        """Detiene el sensor."""
        self._detenido.set()

    def get_nivel_actual(self) -> float:
        """Retorna último nivel leído (%)."""
        return self._moto.get_porcentaje_combustible()

# ================================================================================
# ARCHIVO 3/4: temperatura_motor_sensor.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/temperatura_motor_sensor.py
# ================================================================================

import random
import threading
import time
from python_racing.patrones.observer.observable import Observable
from constante import (
    TEMP_MOTOR_MIN,
    TEMP_MOTOR_MAX,
    INTERVALO_TEMP_MOTOR
)


class TemperaturaMotorSensor(threading.Thread, Observable[dict]):
    """Sensor de temperatura del motor con notificaciones estructuradas."""
    
    def __init__(self):
        threading.Thread.__init__(self, daemon=True, name="TempSensor")
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._temperatura_actual = 40.0

    def run(self) -> None:
        """Loop principal del sensor."""
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            
            # Enviar evento estructurado en lugar de float directo
            evento = {
                'tipo': 'temperatura',
                'valor': temperatura,
                'unidad': '°C',
                'timestamp': time.time()
            }
            
            self.notificar_observadores(evento)
            time.sleep(INTERVALO_TEMP_MOTOR)

    def _leer_temperatura(self) -> float:
        """Simula lectura de temperatura."""
        # Generar temperatura aleatoria en rango
        self._temperatura_actual = random.uniform(
            TEMP_MOTOR_MIN,
            TEMP_MOTOR_MAX
        )
        return self._temperatura_actual

    def detener(self) -> None:
        """Detiene el sensor."""
        self._detenido.set()

    def get_temperatura_actual(self) -> float:
        """Retorna última temperatura leída."""
        return self._temperatura_actual

# ================================================================================
# ARCHIVO 4/4: velocidad_sensor.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/velocidad_sensor.py
# ================================================================================

import random
import threading
import time
from python_racing.patrones.observer.observable import Observable
from constante import INTERVALO_VELOCIDAD, VELOCIDAD_MAX_MOTOGP


class VelocidadSensor(threading.Thread, Observable[dict]):
    """Sensor de velocidad con notificaciones estructuradas."""
    
    def __init__(self):
        threading.Thread.__init__(self, daemon=True, name="VelocidadSensor")
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._velocidad_actual = 0.0

    def run(self) -> None:
        """Loop principal del sensor."""
        while not self._detenido.is_set():
            velocidad = self._leer_velocidad()
            
            # Enviar evento estructurado
            evento = {
                'tipo': 'velocidad',
                'valor': velocidad,
                'unidad': 'km/h',
                'timestamp': time.time()
            }
            
            self.notificar_observadores(evento)
            time.sleep(INTERVALO_VELOCIDAD)

    def _leer_velocidad(self) -> float:
        """Simula lectura de velocidad."""
        # Generar velocidad aleatoria entre 0 y velocidad máxima
        self._velocidad_actual = random.uniform(100, VELOCIDAD_MAX_MOTOGP)
        return self._velocidad_actual

    def detener(self) -> None:
        """Detiene el sensor."""
        self._detenido.set()

    def get_velocidad_actual(self) -> float:
        """Retorna última velocidad leída (km/h)."""
        return self._velocidad_actual

