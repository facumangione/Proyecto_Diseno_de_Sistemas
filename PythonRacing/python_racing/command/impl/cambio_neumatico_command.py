from typing import TYPE_CHECKING, Optional
from python_racing.command.command import Command
from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico
from constante import TIEMPO_CAMBIO_NEUMATICOS

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class CambioNeumaticoCommand(Command):
    def __init__(self, moto: 'Moto', tipo_neumatico: TipoNeumatico):
        super().__init__(moto)
        self._tipo_neumatico = tipo_neumatico
        self._neumaticos_anteriores: Optional[tuple[Neumatico, Neumatico]] = None
    
    def ejecutar(self) -> bool:
        if self._ejecutado:
            print("[WARN] Comando ya ejecutado anteriormente")
            return False
        
        # Guardar neumáticos actuales para poder deshacer
        delantero_actual = self._moto.get_neumatico_delantero()
        trasero_actual = self._moto.get_neumatico_trasero()
        
        if delantero_actual is None or trasero_actual is None:
            raise ValueError("La moto no tiene neumáticos instalados")
        
        self._neumaticos_anteriores = (delantero_actual, trasero_actual)
        
        # Instalar nuevos neumáticos
        neumatico_delantero_nuevo = Neumatico(self._tipo_neumatico)
        neumatico_trasero_nuevo = Neumatico(self._tipo_neumatico)
        
        self._moto.set_neumatico_delantero(neumatico_delantero_nuevo)
        self._moto.set_neumatico_trasero(neumatico_trasero_nuevo)
        
        # Registrar tiempo y estado
        self._tiempo_ejecucion = TIEMPO_CAMBIO_NEUMATICOS
        self._ejecutado = True
        
        print(f"[OK] Neumáticos cambiados a {self._tipo_neumatico.value}")
        print(f"     Tiempo: {self._tiempo_ejecucion}s")
        
        return True
    
    def deshacer(self) -> bool:
        if not self._ejecutado:
            print("[WARN] No se puede deshacer un comando no ejecutado")
            return False
        
        if self._neumaticos_anteriores is None:
            print("[ERROR] No hay neumáticos anteriores guardados")
            return False
        
        # Restaurar neumáticos anteriores
        delantero_anterior, trasero_anterior = self._neumaticos_anteriores
        self._moto.set_neumatico_delantero(delantero_anterior)
        self._moto.set_neumatico_trasero(trasero_anterior)
        
        self._ejecutado = False
        print("[OK] Cambio de neumáticos deshecho")
        
        return True
    
    def get_descripcion(self) -> str:
        estado = "EJECUTADO" if self._ejecutado else "PENDIENTE"
        return (
            f"Cambio de neumáticos a {self._tipo_neumatico.value} "
            f"({TIEMPO_CAMBIO_NEUMATICOS}s) - {estado}"
        )
    
    def get_tipo_neumatico(self) -> TipoNeumatico:
        """Obtiene el tipo de neumático que se instalará/instaló."""
        return self._tipo_neumatico
