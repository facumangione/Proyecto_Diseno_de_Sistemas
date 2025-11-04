from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.corredor import Corredor


class Vuelta:
    def __init__(
        self,
        numero: int,
        tiempo: float,
        corredor: 'Corredor'
    ):
        if numero <= 0:
            raise ValueError("El número de vuelta debe ser positivo")
        if tiempo <= 0:
            raise ValueError("El tiempo debe ser positivo")
        
        self._numero = numero
        self._tiempo = tiempo
        self._corredor = corredor
        self._velocidad_promedio = 0.0
        self._velocidad_maxima = 0.0
        self._neumaticos_degradados = False

    def get_numero(self) -> int:
        """Número de vuelta."""
        return self._numero

    def get_tiempo(self) -> float:
        """Tiempo en segundos."""
        return self._tiempo

    def get_corredor(self) -> 'Corredor':
        """Quién hizo la vuelta."""
        return self._corredor

    def get_velocidad_promedio(self) -> float:
        """Velocidad promedio en km/h."""
        return self._velocidad_promedio

    def set_velocidad_promedio(self, velocidad: float) -> None:
        """Establece la velocidad promedio."""
        self._velocidad_promedio = velocidad

    def get_velocidad_maxima(self) -> float:
        """Velocidad máxima alcanzada."""
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad: float) -> None:
        """Establece la velocidad máxima."""
        self._velocidad_maxima = velocidad

    def marcar_neumaticos_degradados(self) -> None:
        """Marca que los neumáticos estaban gastados."""
        self._neumaticos_degradados = True

    def obtener_tiempo_formateado(self) -> str:
        minutos = int(self._tiempo // 60)
        segundos = self._tiempo % 60
        return f"{minutos}:{segundos:06.3f}"

    def es_tiempo_competitivo(self, tiempo_referencia: float) -> bool:
        diferencia_porcentual = abs(self._tiempo - tiempo_referencia) / tiempo_referencia
        return diferencia_porcentual <= 0.01  # Dentro del 1%

    def __str__(self) -> str:
        return (
            f"Vuelta {self._numero} - {self.obtener_tiempo_formateado()} - "
            f"{self._corredor.get_nombre()} - "
            f"Vel.Max: {self._velocidad_maxima:.1f} km/h"
        )