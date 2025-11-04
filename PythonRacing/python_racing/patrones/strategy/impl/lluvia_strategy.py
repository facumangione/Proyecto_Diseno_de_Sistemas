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