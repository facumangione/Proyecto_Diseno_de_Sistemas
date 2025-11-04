
from python_racing.entidades.circuitos.circuito import Circuito, TipoSuperficie


class CircuitoService:

    def __init__(self):
        self._circuitos: dict[str, Circuito] = {}

    def registrar_circuito(
        self,
        nombre: str,
        longitud_km: float,
        pais: str,
        superficie: TipoSuperficie
    ) -> Circuito:
        if nombre in self._circuitos:
            raise ValueError(f"Ya existe un circuito llamado '{nombre}'")
        
        circuito = Circuito(nombre, longitud_km, pais, superficie)
        self._circuitos[nombre] = circuito
        return circuito

    def buscar_circuito(self, nombre: str) -> Circuito:
        """Busca un circuito por nombre."""
        return self._circuitos.get(nombre)

    def listar_circuitos(self) -> list[Circuito]:
        """Retorna lista de todos los circuitos."""
        return list(self._circuitos.values())

    def listar_circuitos_por_pais(self, pais: str) -> list[Circuito]:
        """Retorna circuitos de un país específico."""
        return [
            c for c in self._circuitos.values()
            if c.get_pais().lower() == pais.lower()
        ]