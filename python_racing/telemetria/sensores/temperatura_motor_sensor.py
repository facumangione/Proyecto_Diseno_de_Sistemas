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