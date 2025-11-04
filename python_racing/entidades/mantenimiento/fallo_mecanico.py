from enum import Enum
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class TipoFallo(Enum):
    """Los tipos de fallo que pueden arruinar tu domingo."""
    MOTOR = "Motor"                    # El corazón se para
    FRENOS = "Frenos"                  # No frenas = no vives
    SUSPENSION = "Suspensión"          # La moto no dobla
    ELECTRONICA = "Electrónica"        # Los sensores mienten
    NEUMATICOS = "Neumáticos"          # Reventón
    TRANSMISION = "Transmisión"        # No cambia de marcha
    COMBUSTIBLE = "Combustible"        # Se queda sin gasolina


class GravedadFallo(Enum):
    """Qué tan jodido estás."""
    LEVE = "Leve"        # Se puede terminar la carrera
    MEDIA = "Media"      # Difícil pero posible
    GRAVE = "Grave"      # Abandono inmediato


class FalloMecanico:

    def __init__(
        self,
        tipo: TipoFallo,
        gravedad: GravedadFallo,
        descripcion: str,
        moto: 'Moto' = None
    ):
        
        self._tipo = tipo
        self._gravedad = gravedad
        self._descripcion = descripcion
        self._moto = moto
        self._fecha_deteccion = datetime.now()
        self._reparado = False
        self._costo_reparacion = 0.0

    def get_tipo(self) -> TipoFallo:
        """Qué tipo de fallo es."""
        return self._tipo

    def get_gravedad(self) -> GravedadFallo:
        """Qué tan grave es."""
        return self._gravedad

    def get_descripcion(self) -> str:
        """Descripción del fallo."""
        return self._descripcion

    def get_fecha_deteccion(self) -> datetime:
        """Cuándo se detectó."""
        return self._fecha_deteccion

    def esta_reparado(self) -> bool:
        """Si ya se arregló."""
        return self._reparado

    def get_costo_reparacion(self) -> float:
        """Cuánto costó (o costará) arreglarlo."""
        return self._costo_reparacion

    def marcar_reparado(self, costo: float) -> None:
        self._reparado = True
        self._costo_reparacion = costo

    def requiere_abandono(self) -> bool:
        return self._gravedad == GravedadFallo.GRAVE

    def calcular_costo_estimado(self) -> float:
        from constante import (
            COSTO_REPARACION_LEVE,
            COSTO_REPARACION_MEDIA,
            COSTO_REPARACION_GRAVE
        )
        
        costos = {
            GravedadFallo.LEVE: COSTO_REPARACION_LEVE,
            GravedadFallo.MEDIA: COSTO_REPARACION_MEDIA,
            GravedadFallo.GRAVE: COSTO_REPARACION_GRAVE
        }
        
        return costos[self._gravedad]

    def __str__(self) -> str:
        estado = "✓ Reparado" if self._reparado else "⚠️ Pendiente"
        return (
            f"Fallo {self._tipo.value} - {self._gravedad.value} - "
            f"{estado} - {self._descripcion}"
        )