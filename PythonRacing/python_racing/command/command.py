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