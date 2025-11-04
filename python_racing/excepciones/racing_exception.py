

class RacingException(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[PythonRacing] {self.mensaje}"