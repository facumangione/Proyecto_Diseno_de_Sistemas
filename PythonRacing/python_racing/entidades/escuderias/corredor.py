from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.escuderia import Escuderia


class Corredor:
    """
    Representa un corredor de MotoGP.
    
    Attributes:
        nombre: Nombre completo
        nacionalidad: País de origen
        numero: Número de carrera (1-99)
        edad: Edad del corredor
        escuderia: Escudería a la que pertenece
        puntos_campeonato: Puntos acumulados en el campeonato
    """

    def __init__(
        self,
        nombre: str,
        nacionalidad: str,
        numero: int,
        edad: int,
        escuderia: Optional['Escuderia'] = None
    ):
        """
        Inicializa un corredor.
        
        Args:
            nombre: Nombre completo
            nacionalidad: País de origen
            numero: Número de carrera único (1-99)
            edad: Edad del corredor (>= 18)
            escuderia: Escudería (opcional)
        
        Raises:
            ValueError: Si los parámetros son inválidos
        """
        from constante import (
            EDAD_MIN_CORREDOR,
            NUMERO_MIN_CORREDOR,
            NUMERO_MAX_CORREDOR
        )
        
        if edad < EDAD_MIN_CORREDOR:
            raise ValueError(
                f"El corredor debe tener al menos {EDAD_MIN_CORREDOR} años"
            )
        if not (NUMERO_MIN_CORREDOR <= numero <= NUMERO_MAX_CORREDOR):
            raise ValueError(
                f"El número debe estar entre {NUMERO_MIN_CORREDOR} y "
                f"{NUMERO_MAX_CORREDOR}"
            )
        
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self._numero = numero
        self._edad = edad
        self._escuderia = escuderia
        self._puntos_campeonato = 0
        self._victorias = 0
        self._podios = 0

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_nacionalidad(self) -> str:
        return self._nacionalidad

    def get_numero(self) -> int:
        return self._numero

    def get_edad(self) -> int:
        return self._edad

    def get_escuderia(self) -> Optional['Escuderia']:
        return self._escuderia

    def get_puntos_campeonato(self) -> int:
        return self._puntos_campeonato

    def get_victorias(self) -> int:
        return self._victorias

    def get_podios(self) -> int:
        return self._podios

    # Setters
    def set_edad(self, edad: int) -> None:
        """
        Establece la edad del corredor.
        
        Args:
            edad: Nueva edad
        
        Raises:
            ValueError: Si la edad es menor a 18
        """
        from constante import EDAD_MIN_CORREDOR
        if edad < EDAD_MIN_CORREDOR:
            raise ValueError(
                f"El corredor debe tener al menos {EDAD_MIN_CORREDOR} años"
            )
        self._edad = edad

    def set_escuderia(self, escuderia: 'Escuderia') -> None:
        """Asigna el corredor a una escudería."""
        self._escuderia = escuderia

    # Métodos de negocio
    def agregar_puntos(self, puntos: int) -> None:
        """Agrega puntos del campeonato."""
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._puntos_campeonato += puntos

    def registrar_victoria(self) -> None:
        """Registra una victoria (1er lugar)."""
        self._victorias += 1
        self._podios += 1
        self.agregar_puntos(25)  # Puntos por victoria en MotoGP

    def registrar_podio(self, posicion: int) -> None:
        """
        Registra un podio.
        
        Args:
            posicion: Posición final (1, 2, o 3)
        """
        if posicion == 1:
            self.registrar_victoria()
        elif posicion == 2:
            self._podios += 1
            self.agregar_puntos(20)
        elif posicion == 3:
            self._podios += 1
            self.agregar_puntos(16)

    def __str__(self) -> str:
        escuderia_str = (
            self._escuderia.get_nombre() 
            if self._escuderia 
            else "Sin escudería"
        )
        return (
            f"#{self._numero} {self._nombre} ({self._nacionalidad}) - "
            f"{escuderia_str} - Puntos: {self._puntos_campeonato}"
        )
