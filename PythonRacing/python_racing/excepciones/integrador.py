"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 7
"""

# ================================================================================
# ARCHIVO 1/7: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/__init__.py
# ================================================================================

from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.combustible_excedido_exception import CombustibleExcedidoException
from python_racing.excepciones.combustible_insuficiente_exception import CombustibleInsuficienteException
from python_racing.excepciones.presupuesto_insuficiente_exception import PresupuestoInsuficienteException
from python_racing.excepciones.fallo_grave_exception import FalloGraveException

__all__ = [
    'RacingException',
    'CombustibleExcedidoException',
    'CombustibleInsuficienteException',
    'PresupuestoInsuficienteException',
    'FalloGraveException'
]

# ================================================================================
# ARCHIVO 2/7: combustible_excedido_exception.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/combustible_excedido_exception.py
# ================================================================================

from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.mensajes_exception import MENSAJE_COMBUSTIBLE_EXCEDIDO


class CombustibleExcedidoException(RacingException):
    def __init__(
        self,
        capacidad_max: float,
        cantidad_actual: float,
        cantidad_intentada: float
    ):
        self.capacidad_max = capacidad_max
        self.cantidad_actual = cantidad_actual
        self.cantidad_intentada = cantidad_intentada
        
        mensaje = (
            f"{MENSAJE_COMBUSTIBLE_EXCEDIDO}. "
            f"Capacidad: {capacidad_max}L, Actual: {cantidad_actual}L, "
            f"Intentó cargar: {cantidad_intentada}L"
        )
        super().__init__(mensaje)

    def get_exceso(self) -> float:
        """Calcula cuánto combustible sobra."""
        return (self.cantidad_actual + self.cantidad_intentada) - self.capacidad_max

# ================================================================================
# ARCHIVO 3/7: combustible_insuficiente_exception.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/combustible_insuficiente_exception.py
# ================================================================================

from python_racing.excepciones.racing_exception import RacingException


class CombustibleInsuficienteException(RacingException):
    def __init__(self, cantidad_actual: float, cantidad_requerida: float):
        self.cantidad_actual = cantidad_actual
        self.cantidad_requerida = cantidad_requerida
        
        mensaje = (
            f"Combustible insuficiente. "
            f"Disponible: {cantidad_actual:.2f}L, "
            f"Requerido: {cantidad_requerida:.2f}L"
        )
        super().__init__(mensaje)

    def get_faltante(self) -> float:
        """Calcula cuánto combustible falta."""
        return self.cantidad_requerida - self.cantidad_actual

# ================================================================================
# ARCHIVO 4/7: fallo_grave_exception.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/fallo_grave_exception.py
# ================================================================================

from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.mensajes_exception import MENSAJE_FALLO_GRAVE


class FalloGraveException(RacingException):
    def __init__(self, tipo_fallo: str, descripcion: str):
        self.tipo_fallo = tipo_fallo
        self.descripcion = descripcion
        
        mensaje = (
            f"{MENSAJE_FALLO_GRAVE}. "
            f"Tipo: {tipo_fallo}, Detalle: {descripcion}"
        )
        super().__init__(mensaje)

# ================================================================================
# ARCHIVO 5/7: mensajes_exception.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/mensajes_exception.py
# ================================================================================


# Combustible
MENSAJE_COMBUSTIBLE_EXCEDIDO = (
    "La cantidad de combustible excede la capacidad máxima del tanque"
)
MENSAJE_COMBUSTIBLE_INSUFICIENTE = (
    "No hay suficiente combustible para completar la operación"
)

# Presupuesto
MENSAJE_PRESUPUESTO_INSUFICIENTE = (
    "La escudería no tiene presupuesto suficiente para esta operación"
)

# Fallos mecánicos
MENSAJE_FALLO_GRAVE = (
    "La moto tiene un fallo grave que impide continuar la carrera"
)

# Neumáticos
MENSAJE_NEUMATICOS_INCOMPATIBLES = (
    "El tipo de neumático no es compatible con las condiciones de la pista"
)

# Carreras
MENSAJE_CARRERA_NO_FINALIZADA = (
    "No se puede obtener resultados de una carrera no finalizada"
)

# Persistencia
MENSAJE_PERSISTENCIA = (
    "Error al guardar o recuperar datos del sistema"
)

# ================================================================================
# ARCHIVO 6/7: presupuesto_insuficiente_exception.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/presupuesto_insuficiente_exception.py
# ================================================================================

from python_racing.excepciones.racing_exception import RacingException
from python_racing.excepciones.mensajes_exception import MENSAJE_PRESUPUESTO_INSUFICIENTE


class PresupuestoInsuficienteException(RacingException):
    def __init__(self, presupuesto_actual: float, cantidad_requerida: float):
        self.presupuesto_actual = presupuesto_actual
        self.cantidad_requerida = cantidad_requerida
        
        mensaje = (
            f"{MENSAJE_PRESUPUESTO_INSUFICIENTE}. "
            f"Disponible: ${presupuesto_actual:,.2f}, "
            f"Requerido: ${cantidad_requerida:,.2f}"
        )
        super().__init__(mensaje)

    def get_faltante(self) -> float:
        """Calcula cuánto dinero falta."""
        return self.cantidad_requerida - self.presupuesto_actual

# ================================================================================
# ARCHIVO 7/7: racing_exception.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/racing_exception.py
# ================================================================================



class RacingException(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[PythonRacing] {self.mensaje}"

