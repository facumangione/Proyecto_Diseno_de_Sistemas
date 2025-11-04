from enum import Enum


class TipoSuperficie(Enum):
    """Tipos de superficie de circuito."""
    ASFALTO = "Asfalto"
    MIXTO = "Mixto"
    TIERRA = "Tierra"


class CondicionClimatica(Enum):
    """Condiciones climáticas del circuito."""
    SECO = "Seco"
    HUMEDO = "Húmedo"
    LLUVIA = "Lluvia"


class Circuito:
    """
    Representa un circuito de carreras.
    
    Attributes:
        nombre: Nombre del circuito
        longitud_km: Longitud en kilómetros
        pais: País donde se encuentra
        superficie: Tipo de superficie
        condicion_climatica: Condición actual del clima
    """

    def __init__(
        self,
        nombre: str,
        longitud_km: float,
        pais: str,
        superficie: TipoSuperficie
    ):
        """
        Inicializa un circuito.
        
        Args:
            nombre: Nombre del circuito
            longitud_km: Longitud en km (debe ser > 0)
            pais: País donde se encuentra
            superficie: Tipo de superficie
        
        Raises:
            ValueError: Si la longitud es inválida
        """
        if longitud_km <= 0:
            raise ValueError("La longitud debe ser mayor a 0")
        
        self._nombre = nombre
        self._longitud_km = longitud_km
        self._pais = pais
        self._superficie = superficie
        self._condicion_climatica = CondicionClimatica.SECO

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_longitud_km(self) -> float:
        return self._longitud_km

    def get_pais(self) -> str:
        return self._pais

    def get_superficie(self) -> TipoSuperficie:
        return self._superficie

    def get_condicion_climatica(self) -> CondicionClimatica:
        return self._condicion_climatica

    # Setters
    def set_condicion_climatica(self, condicion: CondicionClimatica) -> None:
        """Establece la condición climática actual."""
        self._condicion_climatica = condicion

    def __str__(self) -> str:
        return (
            f"{self._nombre} ({self._pais}) - {self._longitud_km} km - "
            f"{self._superficie.value} - {self._condicion_climatica.value}"
        )