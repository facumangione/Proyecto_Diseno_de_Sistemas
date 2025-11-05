"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/factory
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/factory/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: moto_factory.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/factory/moto_factory.py
# ================================================================================

from python_racing.entidades.motos.moto import Moto
from python_racing.entidades.motos.motor import Motor, TipoMotor
from constante import (
    COMBUSTIBLE_MAX_DUCATI, POTENCIA_DUCATI, PESO_DUCATI, REV_MAX_DUCATI,
    COMBUSTIBLE_MAX_YAMAHA, POTENCIA_YAMAHA, PESO_YAMAHA, REV_MAX_YAMAHA,
    COMBUSTIBLE_MAX_KTM, POTENCIA_KTM, PESO_KTM, REV_MAX_KTM,
    COMBUSTIBLE_MAX_HONDA, POTENCIA_HONDA, PESO_HONDA, REV_MAX_HONDA
)


class MotoFactory:

    @staticmethod
    def crear_moto(marca: str) -> Moto:

        # Diccionario de factories (NO if/elif cascades)
        factories = {
            "ducati": MotoFactory._crear_ducati,
            "yamaha": MotoFactory._crear_yamaha,
            "ktm": MotoFactory._crear_ktm,
            "honda": MotoFactory._crear_honda
        }
        
        marca_lower = marca.lower()
        if marca_lower not in factories:
            raise ValueError(
                f"Marca desconocida: {marca}. "
                f"Marcas disponibles: {', '.join(factories.keys())}"
            )
        
        return factories[marca_lower]()

    @staticmethod
    def _crear_ducati() -> Moto:
        """Crea una Ducati Desmosedici GP25."""
        motor = Motor(TipoMotor.V4, 1000, REV_MAX_DUCATI)
        return Moto(
            marca="Ducati",
            modelo="Desmosedici GP25",
            motor=motor,
            potencia_hp=POTENCIA_DUCATI,
            combustible_max=COMBUSTIBLE_MAX_DUCATI,
            peso_kg=PESO_DUCATI
        )

    @staticmethod
    def _crear_yamaha() -> Moto:
        """Crea una Yamaha YZR-M1."""
        motor = Motor(TipoMotor.LINEAL_4, 1000, REV_MAX_YAMAHA)
        return Moto(
            marca="Yamaha",
            modelo="YZR-M1",
            motor=motor,
            potencia_hp=POTENCIA_YAMAHA,
            combustible_max=COMBUSTIBLE_MAX_YAMAHA,
            peso_kg=PESO_YAMAHA
        )

    @staticmethod
    def _crear_ktm() -> Moto:
        """Crea una KTM RC16."""
        motor = Motor(TipoMotor.V4, 1000, REV_MAX_KTM)
        return Moto(
            marca="KTM",
            modelo="RC16",
            motor=motor,
            potencia_hp=POTENCIA_KTM,
            combustible_max=COMBUSTIBLE_MAX_KTM,
            peso_kg=PESO_KTM
        )

    @staticmethod
    def _crear_honda() -> Moto:
        """Crea una Honda RC213V."""
        motor = Motor(TipoMotor.V4, 1000, REV_MAX_HONDA)
        return Moto(
            marca="Honda",
            modelo="RC213V",
            motor=motor,
            potencia_hp=POTENCIA_HONDA,
            combustible_max=COMBUSTIBLE_MAX_HONDA,
            peso_kg=PESO_HONDA
        )

