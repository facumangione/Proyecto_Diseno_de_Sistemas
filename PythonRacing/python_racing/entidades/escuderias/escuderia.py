
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.corredor import Corredor


class Escuderia:
    """
    Representa una escudería de MotoGP.
    
    Attributes:
        nombre: Nombre de la escudería
        pais: País de origen
        presupuesto: Presupuesto disponible
        corredores: Lista de corredores
    """

    def __init__(self, nombre: str, pais: str, presupuesto: float):
        """
        Inicializa una escudería.
        
        Args:
            nombre: Nombre único de la escudería
            pais: País de origen
            presupuesto: Presupuesto inicial (debe ser > 0)
        
        Raises:
            ValueError: Si el presupuesto es inválido
        """
        if presupuesto <= 0:
            raise ValueError("El presupuesto debe ser mayor a 0")
        
        self._nombre = nombre
        self._pais = pais
        self._presupuesto = presupuesto
        self._corredores: list['Corredor'] = []

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_pais(self) -> str:
        return self._pais

    def get_presupuesto(self) -> float:
        return self._presupuesto

    def get_corredores(self) -> list['Corredor']:
        """Retorna copia de la lista de corredores (defensive copy)."""
        return self._corredores.copy()

    # Setters
    def set_presupuesto(self, presupuesto: float) -> None:
        """
        Establece el presupuesto de la escudería.
        
        Args:
            presupuesto: Nuevo presupuesto
        
        Raises:
            ValueError: Si el presupuesto es negativo
        """
        if presupuesto < 0:
            raise ValueError("El presupuesto no puede ser negativo")
        self._presupuesto = presupuesto

    # Métodos de negocio
    def agregar_corredor(self, corredor: 'Corredor') -> None:
        """Agrega un corredor a la escudería."""
        if corredor not in self._corredores:
            self._corredores.append(corredor)

    def remover_corredor(self, corredor: 'Corredor') -> None:
        """Remueve un corredor de la escudería."""
        if corredor in self._corredores:
            self._corredores.remove(corredor)

    def gastar_presupuesto(self, cantidad: float) -> None:
        """
        Gasta dinero del presupuesto.
        
        Args:
            cantidad: Cantidad a gastar
        
        Raises:
            PresupuestoInsuficienteException: Si no hay fondos suficientes
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        if self._presupuesto < cantidad:
            from python_racing.excepciones.presupuesto_insuficiente_exception import (
                PresupuestoInsuficienteException
            )
            raise PresupuestoInsuficienteException(
                presupuesto_actual=self._presupuesto,
                cantidad_requerida=cantidad
            )
        
        self._presupuesto -= cantidad

    def agregar_presupuesto(self, cantidad: float) -> None:
        """Agrega fondos al presupuesto."""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._presupuesto += cantidad

    def __str__(self) -> str:
        return (
            f"{self._nombre} ({self._pais}) - "
            f"Presupuesto: ${self._presupuesto:,.2f} - "
            f"Corredores: {len(self._corredores)}"
        )