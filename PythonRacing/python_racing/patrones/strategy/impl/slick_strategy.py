
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