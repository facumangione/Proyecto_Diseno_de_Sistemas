"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/__init__.py
# ================================================================================

from python_racing.command.command import Command
from python_racing.command.impl.entrada_boxes_command import EntradaBoxesCommand
from python_racing.command.impl.carga_combustible_command import CargaCombustibleCommand
from python_racing.command.impl.cambio_neumatico_command import CambioNeumaticoCommand

__all__ = [
    'Command',
    'EntradaBoxesCommand',
    'CargaCombustibleCommand',
    'CambioNeumaticoCommand'
]

# ================================================================================
# ARCHIVO 2/2: command.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/command.py
# ================================================================================

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class Command(ABC):
    
    def __init__(self, moto: 'Moto'):
        self._moto = moto
        self._ejecutado = False
        self._tiempo_ejecucion = 0.0
    
    @abstractmethod
    def ejecutar(self) -> bool:
        pass
    
    @abstractmethod
    def deshacer(self) -> bool:
        pass
    
    def get_tiempo_ejecucion(self) -> float:
        return self._tiempo_ejecucion
    
    def esta_ejecutado(self) -> bool:
        return self._ejecutado
    
    @abstractmethod
    def get_descripcion(self) -> str:
        pass

