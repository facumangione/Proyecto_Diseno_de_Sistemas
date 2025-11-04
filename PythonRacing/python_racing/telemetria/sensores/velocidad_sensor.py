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