from typing import TYPE_CHECKING
from python_racing.command.command import Command
from python_racing.excepciones.combustible_excedido_exception import CombustibleExcedidoException
from constante import TIEMPO_CARGA_COMBUSTIBLE

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class CargaCombustibleCommand(Command):
    
    def __init__(self, moto: 'Moto', cantidad: float):
        super().__init__(moto)
        
        if cantidad <= 0:
            raise ValueError("La cantidad de combustible debe ser positiva")
        
        self._cantidad = cantidad
        self._combustible_anterior = 0.0
    
    def ejecutar(self) -> bool:
        if self._ejecutado:
            print("[WARN] Comando ya ejecutado anteriormente")
            return False
        
        # Guardar combustible actual para poder deshacer
        self._combustible_anterior = self._moto.get_combustible_actual()
        
        try:
            # Intentar cargar combustible
            self._moto.cargar_combustible(self._cantidad)
            
            # Registrar tiempo y estado
            self._tiempo_ejecucion = TIEMPO_CARGA_COMBUSTIBLE
            self._ejecutado = True
            
            print(f"[OK] Combustible cargado: {self._cantidad:.1f}L")
            print(f"     Nivel actual: {self._moto.get_combustible_actual():.1f}L/"
                  f"{self._moto.get_combustible_max():.1f}L")
            print(f"     Tiempo: {self._tiempo_ejecucion}s")
            
            return True
            
        except CombustibleExcedidoException as e:
            print(f"[ERROR] No se puede cargar combustible: {e}")
            raise
    
    def deshacer(self) -> bool:
        if not self._ejecutado:
            print("[WARN] No se puede deshacer un comando no ejecutado")
            return False
        
        # Calcular cuánto combustible hay que consumir para volver al estado anterior
        combustible_actual = self._moto.get_combustible_actual()
        diferencia = combustible_actual - self._combustible_anterior
        
        if diferencia > 0:
            # Consumir la diferencia (esto es artificial, pero permite el undo)
            try:
                self._moto.consumir_combustible(diferencia)
                self._ejecutado = False
                print("[OK] Carga de combustible deshecha")
                return True
            except Exception as e:
                print(f"[ERROR] No se pudo deshacer la carga: {e}")
                return False
        
        return False
    
    def get_descripcion(self) -> str:
        estado = "EJECUTADO" if self._ejecutado else "PENDIENTE"
        return (
            f"Carga de combustible: {self._cantidad:.1f}L "
            f"({TIEMPO_CARGA_COMBUSTIBLE}s) - {estado}"
        )
    
    def get_cantidad(self) -> float:
        """Obtiene la cantidad de combustible a cargar."""
        return self._cantidad
    
    def get_combustible_anterior(self) -> float:
        """Obtiene el nivel de combustible antes de la carga."""
        return self._combustible_anterior