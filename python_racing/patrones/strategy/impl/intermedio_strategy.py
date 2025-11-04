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