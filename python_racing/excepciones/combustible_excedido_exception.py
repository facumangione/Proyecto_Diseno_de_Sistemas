from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.mensajes_exception import MENSAJE_COMBUSTIBLE_EXCEDIDO


class CombustibleExcedidoException(RacingException):
    def __init__(
        self,
        capacidad_max: float,
        cantidad_actual: float,
        cantidad_intentada: float
    ):
        self.capacidad_max = capacidad_max
        self.cantidad_actual = cantidad_actual
        self.cantidad_intentada = cantidad_intentada
        
        mensaje = (
            f"{MENSAJE_COMBUSTIBLE_EXCEDIDO}. "
            f"Capacidad: {capacidad_max}L, Actual: {cantidad_actual}L, "
            f"Intentó cargar: {cantidad_intentada}L"
        )
        super().__init__(mensaje)

    def get_exceso(self) -> float:
        """Calcula cuánto combustible sobra."""
        return (self.cantidad_actual + self.cantidad_intentada) - self.capacidad_max