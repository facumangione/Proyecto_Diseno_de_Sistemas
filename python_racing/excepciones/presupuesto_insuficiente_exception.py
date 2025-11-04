from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.mensajes_exception import MENSAJE_PRESUPUESTO_INSUFICIENTE


class PresupuestoInsuficienteException(RacingException):
    def __init__(self, presupuesto_actual: float, cantidad_requerida: float):
        self.presupuesto_actual = presupuesto_actual
        self.cantidad_requerida = cantidad_requerida
        
        mensaje = (
            f"{MENSAJE_PRESUPUESTO_INSUFICIENTE}. "
            f"Disponible: ${presupuesto_actual:,.2f}, "
            f"Requerido: ${cantidad_requerida:,.2f}"
        )
        super().__init__(mensaje)

    def get_faltante(self) -> float:
        """Calcula cuánto dinero falta."""
        return self.cantidad_requerida - self.presupuesto_actual