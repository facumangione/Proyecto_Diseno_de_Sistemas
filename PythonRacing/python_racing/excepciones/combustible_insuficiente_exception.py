from python_racing.excepciones.racing_exception import RacingException


class CombustibleInsuficienteException(RacingException):
    def __init__(self, cantidad_actual: float, cantidad_requerida: float):
        self.cantidad_actual = cantidad_actual
        self.cantidad_requerida = cantidad_requerida
        
        mensaje = (
            f"Combustible insuficiente. "
            f"Disponible: {cantidad_actual:.2f}L, "
            f"Requerido: {cantidad_requerida:.2f}L"
        )
        super().__init__(mensaje)

    def get_faltante(self) -> float:
        """Calcula cuánto combustible falta."""
        return self.cantidad_requerida - self.cantidad_actual