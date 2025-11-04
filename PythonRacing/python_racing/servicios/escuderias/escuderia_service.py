from python_racing.entidades.escuderias.escuderia import Escuderia
from python_racing.entidades.escuderias.corredor import Corredor


class EscuderiaService:
    def __init__(self):
        self._escuderias: dict[str, Escuderia] = {}

    def crear_escuderia(
        self,
        nombre: str,
        pais: str,
        presupuesto: float
    ) -> Escuderia:
        if nombre in self._escuderias:
            raise ValueError(f"Ya existe una escudería llamada '{nombre}'")
        
        escuderia = Escuderia(nombre, pais, presupuesto)
        self._escuderias[nombre] = escuderia
        return escuderia

    def registrar_escuderia(self, escuderia: Escuderia) -> None:
        """Registra una escudería existente."""
        self._escuderias[escuderia.get_nombre()] = escuderia

    def buscar_escuderia(self, nombre: str) -> Escuderia:
        return self._escuderias.get(nombre)

    def listar_escuderias(self) -> list[Escuderia]:
        """Retorna lista de todas las escuderías."""
        return list(self._escuderias.values())

    def agregar_corredor_a_escuderia(
        self,
        escuderia: Escuderia,
        corredor: Corredor
    ) -> None:
        """Agrega un corredor a una escudería."""
        escuderia.agregar_corredor(corredor)
        corredor.set_escuderia(escuderia)

    def gastar_en_carrera(
        self,
        escuderia: Escuderia,
        cantidad: float
    ) -> None:
        escuderia.gastar_presupuesto(cantidad)