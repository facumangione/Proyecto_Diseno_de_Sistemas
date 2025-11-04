from typing import TYPE_CHECKING
from python_racing.command.command import Command
from constante import TIEMPO_ENTRADA_BOXES

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class EntradaBoxesCommand(Command):
    def __init__(self, moto: 'Moto', vuelta: int, motivo: str = "Parada programada"):
        super().__init__(moto)
        self._vuelta = vuelta
        self._motivo = motivo
        self._tiempo_perdido = TIEMPO_ENTRADA_BOXES
    
    def ejecutar(self) -> bool:
        if self._ejecutado:
            print("[WARN] Comando ya ejecutado anteriormente")
            return False
        
        # Registrar tiempo y estado
        self._tiempo_ejecucion = self._tiempo_perdido
        self._ejecutado = True
        
        print(f"[OK] Entrada a boxes en vuelta {self._vuelta}")
        print(f"     Motivo: {self._motivo}")
        print(f"     Tiempo perdido: {self._tiempo_perdido}s")
        
        return True
    
    def deshacer(self) -> bool:
        print("[WARN] Una entrada a boxes no se puede deshacer")
        return False
    
    def get_descripcion(self) -> str:
        estado = "EJECUTADO" if self._ejecutado else "PENDIENTE"
        return (
            f"Entrada a boxes (vuelta {self._vuelta}) - "
            f"{self._motivo} - Tiempo: {self._tiempo_perdido}s - {estado}"
        )
    
    def get_vuelta(self) -> int:
        """Obtiene el número de vuelta de la entrada."""
        return self._vuelta
    
    def get_motivo(self) -> str:
        """Obtiene el motivo de la entrada a boxes."""
        return self._motivo
    
    def get_tiempo_perdido(self) -> float:
        """Obtiene el tiempo perdido por la entrada a boxes."""
        return self._tiempo_perdido