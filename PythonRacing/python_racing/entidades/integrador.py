"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 1
"""

# ================================================================================
# ARCHIVO 1/1: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/__init__.py
# ================================================================================

# ============================================================================
# python_racing/entidades/__init__.py
# ============================================================================
"""
Entidades de dominio del sistema PythonRacing.

Este paquete contiene todas las entidades (DTOs) del sistema:
- Motos y componentes
- Escuderías y corredores
- Personal técnico
- Circuitos y carreras
"""

# ============================================================================
# python_racing/entidades/motos/__init__.py
# ============================================================================
"""
Entidades relacionadas con las motos de competición.

Incluye:
- Moto: La moto completa
- Motor: El corazón de la moto
- Neumatico: Los neumáticos
- FalloMecanico: Fallos que pueden ocurrir
"""

from python_racing.entidades.motos.moto import Moto
from python_racing.entidades.motos.motor import Motor, TipoMotor
from python_racing.entidades.motos.neumatico import (
    Neumatico,
    TipoNeumatico,
    EstadoNeumatico
)
# ✅ CORREGIDO: Sin "PythonRacing." al inicio
from python_racing.entidades.mantenimiento.fallo_mecanico import (
    FalloMecanico,
    TipoFallo,
    GravedadFallo
)

__all__ = [
    'Moto',
    'Motor',
    'TipoMotor',
    'Neumatico',
    'TipoNeumatico',
    'EstadoNeumatico',
    'FalloMecanico',
    'TipoFallo',
    'GravedadFallo'
]


# ============================================================================
# python_racing/entidades/escuderias/__init__.py
# ============================================================================
"""
Entidades relacionadas con escuderías y corredores.

Incluye:
- Escuderia: El equipo de carreras
- Corredor: El piloto
"""

from python_racing.entidades.escuderias.escuderia import Escuderia
from python_racing.entidades.escuderias.corredor import Corredor

__all__ = [
    'Escuderia',
    'Corredor'
]


# ============================================================================
# python_racing/entidades/personal/__init__.py
# ============================================================================
"""
Entidades relacionadas con el personal técnico.

Incluye:
- Mecanico: Personal técnico de la escudería
"""

from python_racing.entidades.personal.mecanico import (
    Mecanico,
    EspecialidadMecanico
)

__all__ = [
    'Mecanico',
    'EspecialidadMecanico'
]


# ============================================================================
# python_racing/entidades/circuitos/__init__.py
# ============================================================================
"""
Entidades relacionadas con circuitos y carreras.

Incluye:
- Circuito: La pista de carreras
- Carrera: Una competencia completa
- Vuelta: Una vuelta individual
- ResultadoCarrera: Resultado de un corredor
"""

from python_racing.entidades.circuitos.circuito import (
    Circuito,
    TipoSuperficie,
    CondicionClimatica
)
from python_racing.entidades.circuitos.carrera import (
    Carrera,
    ResultadoCarrera
)
from python_racing.entidades.circuitos.vuelta import Vuelta

__all__ = [
    'Circuito',
    'TipoSuperficie',
    'CondicionClimatica',
    'Carrera',
    'ResultadoCarrera',
    'Vuelta'
]

