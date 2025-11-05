"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/__init__.py
# ================================================================================

"""
Entidades de motos
"""


# ================================================================================
# ARCHIVO 2/5: moto.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/moto.py
# ================================================================================


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

# ================================================================================
# ARCHIVO 3/5: motor.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/motor.py
# ================================================================================

from enum import Enum


class TipoMotor(Enum):
    """Los tipos de motor que verás en MotoGP."""
    V4 = "V4"
    LINEAL_4 = "Lineal 4 cilindros"
    BICILINDRIRCO = "Bicilíndrico"
    MONOCILINDRIRCO = "Monocilíndrico"


class Motor:

    def __init__(self, tipo: TipoMotor, cilindrada: int, revoluciones_max: int):
        if cilindrada <= 0:
            raise ValueError("¿Un motor de 0cc? No funciona así, necesitas cilindrada")
        if revoluciones_max <= 0:
            raise ValueError("Sin revoluciones no hay motor, simple")
        
        self._tipo = tipo
        self._cilindrada = cilindrada
        self._revoluciones_max = revoluciones_max
        self._temperatura = 40.0  # Empieza frío, como debe ser
        self._horas_uso = 0.0

    def get_tipo(self) -> TipoMotor:
        """Qué tipo de motor es."""
        return self._tipo

    def get_cilindrada(self) -> int:
        """Cuántos cc tiene el motor."""
        return self._cilindrada

    def get_revoluciones_max(self) -> int:
        """Hasta dónde puede girar sin romperse."""
        return self._revoluciones_max

    def get_temperatura(self) -> float:
        """Qué tan caliente está ahora mismo."""
        return self._temperatura

    def get_horas_uso(self) -> float:
        """Cuántas horas lleva funcionando."""
        return self._horas_uso

    def set_temperatura(self, temperatura: float) -> None:
        if temperatura < 0:
            raise ValueError("Temperatura negativa no existe (al menos no aquí)")
        self._temperatura = temperatura

    def incrementar_horas_uso(self, horas: float) -> None:
        """Suma horas de uso. Cada hora cuenta para el mantenimiento."""
        if horas < 0:
            raise ValueError("No puedes retroceder el tiempo")
        self._horas_uso += horas

    def esta_sobrecalentado(self) -> bool:
        from constante import TEMP_MOTOR_ALERTA
        return self._temperatura >= TEMP_MOTOR_ALERTA

    def necesita_revision(self) -> bool:
        
        return self._horas_uso >= 50.0

    def __str__(self) -> str:
        estado = "🔥 SOBRECALENTADO" if self.esta_sobrecalentado() else "✓ OK"
        return (
            f"Motor {self._tipo.value} - {self._cilindrada}cc - "
            f"{self._revoluciones_max} RPM - {self._temperatura:.1f}°C {estado}"
        )

# ================================================================================
# ARCHIVO 4/5: neumatico.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/neumatico.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: tipo_neumatico.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/tipo_neumatico.py
# ================================================================================



