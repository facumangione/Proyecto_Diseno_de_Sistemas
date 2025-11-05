"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/__init__.py
# ================================================================================

"""
Entidades de circuitos y carreras
"""


# ================================================================================
# ARCHIVO 2/4: carrera.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/carrera.py
# ================================================================================

from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_racing.entidades.circuitos.circuito import Circuito
    from python_racing.entidades.escuderias.corredor import Corredor


class ResultadoCarrera:

    def __init__(
        self,
        corredor: 'Corredor',
        posicion: int,
        tiempo_total: float,
        vueltas_completadas: int,
        abandono: bool = False
    ):
        self._corredor = corredor
        self._posicion = posicion
        self._tiempo_total = tiempo_total
        self._vueltas_completadas = vueltas_completadas
        self._abandono = abandono

    # Getters
    def get_corredor(self) -> 'Corredor':
        return self._corredor

    def get_posicion(self) -> int:
        return self._posicion

    def get_tiempo_total(self) -> float:
        return self._tiempo_total

    def get_vueltas_completadas(self) -> int:
        return self._vueltas_completadas

    def es_abandono(self) -> bool:
        return self._abandono

    def obtener_tiempo_formateado(self) -> str:
        """
        Formatea el tiempo total como MM:SS.
        
        Returns:
            String con formato de tiempo
        """
        minutos = int(self._tiempo_total // 60)
        segundos = int(self._tiempo_total % 60)
        return f"{minutos}m {segundos}s"

    def __str__(self) -> str:
        estado = "ABANDONO" if self._abandono else "COMPLETÓ"
        return (
            f"P{self._posicion}. {self._corredor.get_nombre()} - "
            f"{self.obtener_tiempo_formateado()} - {estado}"
        )


class Carrera:

    def __init__(
        self,
        circuito: 'Circuito',
        fecha: date,
        vueltas: int
    ):
       
        if vueltas <= 0:
            raise ValueError("El número de vueltas debe ser mayor a 0")
        
        self._circuito = circuito
        self._fecha = fecha
        self._vueltas = vueltas
        self._corredores_participantes: list['Corredor'] = []
        self._resultados: list[ResultadoCarrera] = []
        self._finalizada = False

    # Getters
    def get_circuito(self) -> 'Circuito':
        return self._circuito

    def get_fecha(self) -> date:
        return self._fecha

    def get_vueltas(self) -> int:
        return self._vueltas

    def get_corredores_participantes(self) -> list['Corredor']:
        return self._corredores_participantes.copy()

    def get_resultados(self) -> list[ResultadoCarrera]:
        return self._resultados.copy()

    def esta_finalizada(self) -> bool:
        return self._finalizada

    # Métodos de negocio
    def agregar_corredor(self, corredor: 'Corredor') -> None:
        """Agrega un corredor a la carrera."""
        if corredor not in self._corredores_participantes:
            self._corredores_participantes.append(corredor)

    def registrar_resultado(self, resultado: ResultadoCarrera) -> None:
        """Registra el resultado de un corredor."""
        self._resultados.append(resultado)

    def finalizar_carrera(self) -> None:
        """Marca la carrera como finalizada y ordena resultados."""
        self._finalizada = True
        # Ordenar por posición
        self._resultados.sort(key=lambda r: r.get_posicion())

    def obtener_ganador(self) -> ResultadoCarrera:
        """
        Obtiene el ganador de la carrera.
        
        Returns:
            Resultado del ganador (posición 1)
        
        Raises:
            ValueError: Si la carrera no ha finalizado
        """
        if not self._finalizada:
            raise ValueError("La carrera no ha finalizado")
        if not self._resultados:
            raise ValueError("No hay resultados registrados")
        
        return self._resultados[0]

    def obtener_podio(self) -> list[ResultadoCarrera]:
        """
        Obtiene el podio (3 primeros lugares).
        
        Returns:
            Lista con los 3 primeros resultados
        """
        if not self._finalizada:
            raise ValueError("La carrera no ha finalizado")
        
        return self._resultados[:3]

    def __str__(self) -> str:
        estado = "FINALIZADA" if self._finalizada else "EN CURSO"
        return (
            f"Carrera en {self._circuito.get_nombre()} - "
            f"{self._fecha} - {self._vueltas} vueltas - {estado}"
        )

# ================================================================================
# ARCHIVO 3/4: circuito.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/circuito.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: vuelta.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/vuelta.py
# ================================================================================

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.corredor import Corredor


class Vuelta:
    def __init__(
        self,
        numero: int,
        tiempo: float,
        corredor: 'Corredor'
    ):
        if numero <= 0:
            raise ValueError("El número de vuelta debe ser positivo")
        if tiempo <= 0:
            raise ValueError("El tiempo debe ser positivo")
        
        self._numero = numero
        self._tiempo = tiempo
        self._corredor = corredor
        self._velocidad_promedio = 0.0
        self._velocidad_maxima = 0.0
        self._neumaticos_degradados = False

    def get_numero(self) -> int:
        """Número de vuelta."""
        return self._numero

    def get_tiempo(self) -> float:
        """Tiempo en segundos."""
        return self._tiempo

    def get_corredor(self) -> 'Corredor':
        """Quién hizo la vuelta."""
        return self._corredor

    def get_velocidad_promedio(self) -> float:
        """Velocidad promedio en km/h."""
        return self._velocidad_promedio

    def set_velocidad_promedio(self, velocidad: float) -> None:
        """Establece la velocidad promedio."""
        self._velocidad_promedio = velocidad

    def get_velocidad_maxima(self) -> float:
        """Velocidad máxima alcanzada."""
        return self._velocidad_maxima

    def set_velocidad_maxima(self, velocidad: float) -> None:
        """Establece la velocidad máxima."""
        self._velocidad_maxima = velocidad

    def marcar_neumaticos_degradados(self) -> None:
        """Marca que los neumáticos estaban gastados."""
        self._neumaticos_degradados = True

    def obtener_tiempo_formateado(self) -> str:
        minutos = int(self._tiempo // 60)
        segundos = self._tiempo % 60
        return f"{minutos}:{segundos:06.3f}"

    def es_tiempo_competitivo(self, tiempo_referencia: float) -> bool:
        diferencia_porcentual = abs(self._tiempo - tiempo_referencia) / tiempo_referencia
        return diferencia_porcentual <= 0.01  # Dentro del 1%

    def __str__(self) -> str:
        return (
            f"Vuelta {self._numero} - {self.obtener_tiempo_formateado()} - "
            f"{self._corredor.get_nombre()} - "
            f"Vel.Max: {self._velocidad_maxima:.1f} km/h"
        )

