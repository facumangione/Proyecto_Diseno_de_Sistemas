
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