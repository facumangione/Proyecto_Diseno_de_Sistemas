from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.mensajes_exception import MENSAJE_FALLO_GRAVE


class FalloGraveException(RacingException):
    def __init__(self, tipo_fallo: str, descripcion: str):
        self.tipo_fallo = tipo_fallo
        self.descripcion = descripcion
        
        mensaje = (
            f"{MENSAJE_FALLO_GRAVE}. "
            f"Tipo: {tipo_fallo}, Detalle: {descripcion}"
        )
        super().__init__(mensaje)