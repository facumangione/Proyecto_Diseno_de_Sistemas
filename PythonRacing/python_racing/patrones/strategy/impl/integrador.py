"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/4: intermedio_strategy.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/intermedio_strategy.py
# ================================================================================

from python_racing.patrones.strategy.neumatico_strategy import NeumaticoStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica
from constante import DESGASTE_INTERMEDIO_SECO, DESGASTE_INTERMEDIO_LLUVIA


class IntermedioStrategy(NeumaticoStrategy):
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        """Calcula desgaste según condición."""
        if condicion == CondicionClimatica.SECO:
            return DESGASTE_INTERMEDIO_SECO * longitud_km
        elif condicion == CondicionClimatica.HUMEDO:
            return DESGASTE_INTERMEDIO_LLUVIA * longitud_km * 0.8  # Óptimo
        else:  # LLUVIA
            return DESGASTE_INTERMEDIO_LLUVIA * longitud_km

    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        """Intermedios son versátiles."""
        return True  # Compatible con todas las condiciones

# ================================================================================
# ARCHIVO 3/4: lluvia_strategy.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/lluvia_strategy.py
# ================================================================================

from python_racing.patrones.strategy.neumatico_strategy import NeumaticoStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica
from constante import DESGASTE_LLUVIA_SECO, DESGASTE_LLUVIA_LLUVIA


class LluviaStrategy(NeumaticoStrategy):
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        """Calcula desgaste según condición."""
        if condicion == CondicionClimatica.SECO:
            return DESGASTE_LLUVIA_SECO * longitud_km  # Desgaste rápido
        elif condicion == CondicionClimatica.HUMEDO:
            return DESGASTE_LLUVIA_LLUVIA * longitud_km * 1.5
        else:  # LLUVIA
            return DESGASTE_LLUVIA_LLUVIA * longitud_km  # Óptimo

    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        """Lluvia es mejor en mojado."""
        return condicion in [CondicionClimatica.HUMEDO, CondicionClimatica.LLUVIA]

# ================================================================================
# ARCHIVO 4/4: slick_strategy.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/slick_strategy.py
# ================================================================================


from python_racing.patrones.strategy.neumatico_strategy import NeumaticoStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica
from constante import DESGASTE_SLICK_SECO, DESGASTE_SLICK_LLUVIA


class SlickStrategy(NeumaticoStrategy):
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        """Calcula desgaste según condición."""
        if condicion == CondicionClimatica.SECO:
            return DESGASTE_SLICK_SECO * longitud_km
        elif condicion == CondicionClimatica.HUMEDO:
            return DESGASTE_SLICK_SECO * longitud_km * 2  # Doble desgaste
        else:  # LLUVIA
            return DESGASTE_SLICK_LLUVIA * longitud_km  # Desgaste extremo

    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        """Slick solo es seguro en SECO."""
        return condicion == CondicionClimatica.SECO

