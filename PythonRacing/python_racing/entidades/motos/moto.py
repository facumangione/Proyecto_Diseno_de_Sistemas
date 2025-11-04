
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from python_racing.entidades.motos.motor import Motor
    from python_racing.entidades.motos.neumatico import Neumatico
    from python_racing.entidades.escuderias.corredor import Corredor


class Moto:
    """
    Representa una moto de competición.
    
    Attributes:
        marca: Marca de la moto (Ducati, Yamaha, etc.)
        modelo: Modelo específico
        motor: Motor de la moto
        potencia_hp: Potencia en caballos de fuerza
        combustible_max: Capacidad máxima de combustible (litros)
        combustible_actual: Combustible actual (litros)
        peso_kg: Peso de la moto en kg
        neumatico_delantero: Neumático delantero
        neumatico_trasero: Neumático trasero
        corredor: Corredor asignado
    """

    def __init__(
        self,
        marca: str,
        modelo: str,
        motor: 'Motor',
        potencia_hp: int,
        combustible_max: float,
        peso_kg: int
    ):
        """
        Inicializa una moto de competición.
        
        Args:
            marca: Marca de la moto
            modelo: Modelo de la moto
            motor: Motor de la moto
            potencia_hp: Potencia en HP (debe ser > 0)
            combustible_max: Capacidad máxima de combustible (debe ser > 0)
            peso_kg: Peso en kg (debe ser > 0)
        
        Raises:
            ValueError: Si algún parámetro es inválido
        """
        if potencia_hp <= 0:
            raise ValueError("La potencia debe ser mayor a 0")
        if combustible_max <= 0:
            raise ValueError("La capacidad de combustible debe ser mayor a 0")
        if peso_kg <= 0:
            raise ValueError("El peso debe ser mayor a 0")
        
        self._marca = marca
        self._modelo = modelo
        self._motor = motor
        self._potencia_hp = potencia_hp
        self._combustible_max = combustible_max
        self._combustible_actual = combustible_max  # Inicialmente llena
        self._peso_kg = peso_kg
        self._neumatico_delantero: Optional['Neumatico'] = None
        self._neumatico_trasero: Optional['Neumatico'] = None
        self._corredor: Optional['Corredor'] = None
        self._kilometros_recorridos = 0.0

    # Getters
    def get_marca(self) -> str:
        return self._marca

    def get_modelo(self) -> str:
        return self._modelo

    def get_motor(self) -> 'Motor':
        return self._motor

    def get_potencia_hp(self) -> int:
        return self._potencia_hp

    def get_combustible_max(self) -> float:
        return self._combustible_max

    def get_combustible_actual(self) -> float:
        return self._combustible_actual

    def get_peso_kg(self) -> int:
        return self._peso_kg

    def get_neumatico_delantero(self) -> Optional['Neumatico']:
        return self._neumatico_delantero

    def get_neumatico_trasero(self) -> Optional['Neumatico']:
        return self._neumatico_trasero

    def get_corredor(self) -> Optional['Corredor']:
        return self._corredor

    def get_kilometros_recorridos(self) -> float:
        return self._kilometros_recorridos

    # Setters
    def set_corredor(self, corredor: 'Corredor') -> None:
        """Asigna un corredor a la moto."""
        self._corredor = corredor

    def set_neumatico_delantero(self, neumatico: 'Neumatico') -> None:
        """Asigna neumático delantero."""
        self._neumatico_delantero = neumatico

    def set_neumatico_trasero(self, neumatico: 'Neumatico') -> None:
        """Asigna neumático trasero."""
        self._neumatico_trasero = neumatico

    # Métodos de negocio - Combustible
    def cargar_combustible(self, cantidad: float) -> None:
        """
        Carga combustible en la moto.
        
        Args:
            cantidad: Litros a cargar (debe ser > 0)
        
        Raises:
            ValueError: Si la cantidad es negativa
            CombustibleExcedidoException: Si excede la capacidad
        """
        if cantidad < 0:
            raise ValueError("La cantidad de combustible no puede ser negativa")
        
        if self._combustible_actual + cantidad > self._combustible_max:
            from python_racing.excepciones.combustible_excedido_exception import (
                CombustibleExcedidoException
            )
            raise CombustibleExcedidoException(
                capacidad_max=self._combustible_max,
                cantidad_actual=self._combustible_actual,
                cantidad_intentada=cantidad
            )
        
        self._combustible_actual += cantidad

    def consumir_combustible(self, cantidad: float) -> None:
        """
        Consume combustible durante una vuelta.
        
        Args:
            cantidad: Litros a consumir
        
        Raises:
            ValueError: Si no hay suficiente combustible
        """
        if cantidad < 0:
            raise ValueError("La cantidad de combustible no puede ser negativa")
        
        if self._combustible_actual < cantidad:
            from python_racing.excepciones.combustible_insuficiente_exception import (
                CombustibleInsuficienteException
            )
            raise CombustibleInsuficienteException(
                cantidad_actual=self._combustible_actual,
                cantidad_requerida=cantidad
            )
        
        self._combustible_actual -= cantidad

    def get_porcentaje_combustible(self) -> float:
        """
        Calcula el porcentaje de combustible restante.
        
        Returns:
            Porcentaje (0-100)
        """
        return (self._combustible_actual / self._combustible_max) * 100

    def combustible_bajo(self) -> bool:
        """
        Verifica si el combustible está bajo.
        
        Returns:
            True si el combustible es menor al 10%
        """
        from constante import COMBUSTIBLE_ALERTA
        return self.get_porcentaje_combustible() < COMBUSTIBLE_ALERTA

    # Métodos de negocio - Neumáticos
    def tiene_neumaticos_instalados(self) -> bool:
        """
        Verifica si la moto tiene ambos neumáticos instalados.
        
        Returns:
            True si tiene delantero y trasero
        """
        return (
            self._neumatico_delantero is not None and
            self._neumatico_trasero is not None
        )

    def neumaticos_requieren_cambio(self) -> bool:
        """
        Verifica si algún neumático requiere cambio.
        
        Returns:
            True si algún neumático está muy gastado
        """
        if not self.tiene_neumaticos_instalados():
            return True
        
        return (
            self._neumatico_delantero.requiere_cambio() or
            self._neumatico_trasero.requiere_cambio()
        )

    # Métodos de simulación
    def incrementar_kilometros(self, km: float) -> None:
        """Incrementa los kilómetros recorridos."""
        if km < 0:
            raise ValueError("Los kilómetros no pueden ser negativos")
        self._kilometros_recorridos += km

    def calcular_peso_total(self) -> float:
        """
        Calcula el peso total de la moto incluyendo combustible.
        
        Returns:
            Peso total en kg (combustible pesa ~0.75 kg/L)
        """
        peso_combustible = self._combustible_actual * 0.75
        return self._peso_kg + peso_combustible

    def __str__(self) -> str:
        corredor_str = (
            self._corredor.get_nombre() 
            if self._corredor 
            else "Sin corredor"
        )
        return (
            f"{self._marca} {self._modelo} - {self._potencia_hp} HP - "
            f"Combustible: {self._combustible_actual:.1f}L/"
            f"{self._combustible_max}L - {corredor_str}"
        )