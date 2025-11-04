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