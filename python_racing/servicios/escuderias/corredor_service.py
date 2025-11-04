from python_racing.entidades.escuderias.corredor import Corredor
from python_racing.entidades.escuderias.escuderia import Escuderia


class CorredorService:
    def __init__(self):
        self._corredores: dict[int, Corredor] = {}  # Key: número de corredor

    def registrar_corredor(
        self,
        nombre: str,
        nacionalidad: str,
        numero: int,
        edad: int,
        escuderia: Escuderia = None
    ) -> Corredor:
        if numero in self._corredores:
            raise ValueError(f"El número {numero} ya está en uso")
        
        corredor = Corredor(nombre, nacionalidad, numero, edad, escuderia)
        self._corredores[numero] = corredor
        
        # Si tiene escudería, agregarlo
        if escuderia:
            escuderia.agregar_corredor(corredor)
        
        return corredor

    def buscar_corredor(self, numero: int) -> Corredor:
        """Busca un corredor por su número."""
        return self._corredores.get(numero)

    def listar_corredores(self) -> list[Corredor]:
        """Retorna lista de todos los corredores."""
        return list(self._corredores.values())

    def obtener_clasificacion(self) -> list[Corredor]:
        corredores = self.listar_corredores()
        return sorted(
            corredores,
            key=lambda c: c.get_puntos_campeonato(),
            reverse=True
        )