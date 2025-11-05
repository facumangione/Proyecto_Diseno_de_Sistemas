"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: neumatico_strategy.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/neumatico_strategy.py
# ================================================================================


from abc import ABC, abstractmethod
from python_racing.entidades.circuitos.circuito import CondicionClimatica


class NeumaticoStrategy(ABC):
    @abstractmethod
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        pass

    @abstractmethod
    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        pass

