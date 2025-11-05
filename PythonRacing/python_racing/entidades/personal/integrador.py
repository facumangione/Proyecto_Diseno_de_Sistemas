"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/personal
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/personal/__init__.py
# ================================================================================

"""
Entidades de personal técnico
"""


# ================================================================================
# ARCHIVO 2/2: mecanico.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/personal/mecanico.py
# ================================================================================

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.escuderia import Escuderia


class EspecialidadMecanico(Enum):
    """En qué se especializa el mecánico."""
    MOTOR = "Motor"
    SUSPENSION = "Suspensión"
    ELECTRONICA = "Electrónica"
    NEUMATICOS = "Neumáticos"
    JEFE_MECANICO = "Jefe de Mecánicos"


class Mecanico:

    def __init__(
        self,
        nombre: str,
        especialidad: EspecialidadMecanico,
        experiencia: int,
        escuderia: 'Escuderia' = None
    ):

        if experiencia < 0:
            raise ValueError("La experiencia no puede ser negativa")
        
        self._nombre = nombre
        self._especialidad = especialidad
        self._experiencia = experiencia
        self._escuderia = escuderia
        self._carreras_trabajadas = 0
        self._reparaciones_realizadas = 0

    def get_nombre(self) -> str:
        """Nombre del mecánico."""
        return self._nombre

    def get_especialidad(self) -> EspecialidadMecanico:
        """En qué se especializa."""
        return self._especialidad

    def get_experiencia(self) -> int:
        """Años de experiencia."""
        return self._experiencia

    def get_escuderia(self) -> 'Escuderia':
        """Equipo donde trabaja."""
        return self._escuderia

    def get_carreras_trabajadas(self) -> int:
        """Cuántas carreras ha trabajado."""
        return self._carreras_trabajadas

    def set_escuderia(self, escuderia: 'Escuderia') -> None:
        """Asigna a una escudería."""
        self._escuderia = escuderia

    def registrar_carrera(self) -> None:
        """Suma una carrera más al contador."""
        self._carreras_trabajadas += 1

    def registrar_reparacion(self) -> None:
        """Suma una reparación realizada."""
        self._reparaciones_realizadas += 1

    def es_experimentado(self) -> bool:

        return self._experiencia >= 10

    def calcular_eficiencia(self) -> float:

        base = 0.5
        bonus_experiencia = min(self._experiencia * 0.02, 0.3)  # Max +30%
        bonus_carreras = min(self._carreras_trabajadas * 0.001, 0.2)  # Max +20%
        
        return min(base + bonus_experiencia + bonus_carreras, 1.0)

    def __str__(self) -> str:
        escuderia_str = (
            self._escuderia.get_nombre() 
            if self._escuderia 
            else "Sin equipo"
        )
        return (
            f"{self._nombre} - {self._especialidad.value} - "
            f"{self._experiencia} años exp. - {escuderia_str}"
        )


