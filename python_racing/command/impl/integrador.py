"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/__init__.py
# ================================================================================

"""
Comandos concretos de boxes
"""


# ================================================================================
# ARCHIVO 2/4: cambio_neumatico_command.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/cambio_neumatico_command.py
# ================================================================================

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


# ================================================================================
# ARCHIVO 3/4: carga_combustible_command.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/carga_combustible_command.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: entrada_boxes_command.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/entrada_boxes_command.py
# ================================================================================

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

