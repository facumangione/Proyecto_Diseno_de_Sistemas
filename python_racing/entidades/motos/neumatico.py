from enum import Enum


class TipoNeumatico(Enum):
    """Tipos de neumáticos según condiciones de pista."""
    SLICK = "Slick (seco)"
    INTERMEDIO = "Intermedio (mixto)"
    LLUVIA = "Lluvia (mojado)"


class EstadoNeumatico(Enum):
    """Estado de desgaste del neumático."""
    NUEVO = "Nuevo"
    USADO = "Usado"
    GASTADO = "Gastado"


class Neumatico:
    """
    Representa un neumático de competición.
    
    Attributes:
        tipo: Tipo de neumático (slick, intermedio, lluvia)
        estado: Estado de desgaste (nuevo, usado, gastado)
        desgaste: Porcentaje de desgaste (0-100)
        vueltas_rodadas: Número de vueltas completadas
    """

    def __init__(self, tipo: TipoNeumatico):
        """
        Inicializa un neumático nuevo.
        
        Args:
            tipo: Tipo de neumático
        """
        self._tipo = tipo
        self._estado = EstadoNeumatico.NUEVO
        self._desgaste = 0.0  # Porcentaje (0-100)
        self._vueltas_rodadas = 0

    # Getters
    def get_tipo(self) -> TipoNeumatico:
        return self._tipo

    def get_estado(self) -> EstadoNeumatico:
        return self._estado

    def get_desgaste(self) -> float:
        return self._desgaste

    def get_vueltas_rodadas(self) -> int:
        return self._vueltas_rodadas

    # Métodos de negocio
    def aplicar_desgaste(self, cantidad: float) -> None:
        """
        Aplica desgaste al neumático.
        
        Args:
            cantidad: Porcentaje de desgaste a aplicar
        """
        self._desgaste += cantidad
        if self._desgaste > 100:
            self._desgaste = 100.0
        
        # Actualizar estado según desgaste
        if self._desgaste >= 80:
            self._estado = EstadoNeumatico.GASTADO
        elif self._desgaste >= 40:
            self._estado = EstadoNeumatico.USADO
        else:
            self._estado = EstadoNeumatico.NUEVO

    def incrementar_vueltas(self) -> None:
        """Incrementa el contador de vueltas."""
        self._vueltas_rodadas += 1

    def esta_gastado(self) -> bool:
        """
        Verifica si el neumático está muy gastado.
        
        Returns:
            True si el desgaste es >= 80%
        """
        return self._desgaste >= 80.0

    def requiere_cambio(self) -> bool:
        """
        Verifica si el neumático requiere cambio urgente.
        
        Returns:
            True si está gastado o supera vida útil
        """
        from constante import (
            VIDA_NEUMATICO_SLICK,
            VIDA_NEUMATICO_INTERMEDIO,
            VIDA_NEUMATICO_LLUVIA
        )
        
        vida_maxima = {
            TipoNeumatico.SLICK: VIDA_NEUMATICO_SLICK,
            TipoNeumatico.INTERMEDIO: VIDA_NEUMATICO_INTERMEDIO,
            TipoNeumatico.LLUVIA: VIDA_NEUMATICO_LLUVIA
        }
        
        return (
            self._desgaste >= 80.0 or 
            self._vueltas_rodadas >= vida_maxima[self._tipo]
        )

    def __str__(self) -> str:
        return (
            f"Neumático {self._tipo.value} - {self._estado.value} - "
            f"Desgaste: {self._desgaste:.1f}% - Vueltas: {self._vueltas_rodadas}"
        )