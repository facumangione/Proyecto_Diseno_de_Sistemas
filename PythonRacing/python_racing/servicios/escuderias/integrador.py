"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias/__init__.py
# ================================================================================

"""
Servicios de gestión de escuderías
"""


# ================================================================================
# ARCHIVO 2/3: corredor_service.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias/corredor_service.py
# ================================================================================

from python_racing.entidades.escuderias.corredor import Corredor
from python_racing.entidades.escuderias.escuderia import Escuderia


class CorredorService:
    def __init__(self):
        self._corredores: dict[int, Corredor] = {}  # Key: número de corredor

    def registrar_corredor(
        self,
        nombre: str,
        nacionalidad: str,
        numero: int,
        edad: int,
        escuderia: Escuderia = None
    ) -> Corredor:
        if numero in self._corredores:
            raise ValueError(f"El número {numero} ya está en uso")
        
        corredor = Corredor(nombre, nacionalidad, numero, edad, escuderia)
        self._corredores[numero] = corredor
        
        # Si tiene escudería, agregarlo
        if escuderia:
            escuderia.agregar_corredor(corredor)
        
        return corredor

    def buscar_corredor(self, numero: int) -> Corredor:
        """Busca un corredor por su número."""
        return self._corredores.get(numero)

    def listar_corredores(self) -> list[Corredor]:
        """Retorna lista de todos los corredores."""
        return list(self._corredores.values())

    def obtener_clasificacion(self) -> list[Corredor]:
        corredores = self.listar_corredores()
        return sorted(
            corredores,
            key=lambda c: c.get_puntos_campeonato(),
            reverse=True
        )

# ================================================================================
# ARCHIVO 3/3: escuderia_service.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias/escuderia_service.py
# ================================================================================

from python_racing.entidades.escuderias.escuderia import Escuderia
from python_racing.entidades.escuderias.corredor import Corredor


class EscuderiaService:
    def __init__(self):
        self._escuderias: dict[str, Escuderia] = {}

    def crear_escuderia(
        self,
        nombre: str,
        pais: str,
        presupuesto: float
    ) -> Escuderia:
        if nombre in self._escuderias:
            raise ValueError(f"Ya existe una escudería llamada '{nombre}'")
        
        escuderia = Escuderia(nombre, pais, presupuesto)
        self._escuderias[nombre] = escuderia
        return escuderia

    def registrar_escuderia(self, escuderia: Escuderia) -> None:
        """Registra una escudería existente."""
        self._escuderias[escuderia.get_nombre()] = escuderia

    def buscar_escuderia(self, nombre: str) -> Escuderia:
        return self._escuderias.get(nombre)

    def listar_escuderias(self) -> list[Escuderia]:
        """Retorna lista de todas las escuderías."""
        return list(self._escuderias.values())

    def agregar_corredor_a_escuderia(
        self,
        escuderia: Escuderia,
        corredor: Corredor
    ) -> None:
        """Agrega un corredor a una escudería."""
        escuderia.agregar_corredor(corredor)
        corredor.set_escuderia(escuderia)

    def gastar_en_carrera(
        self,
        escuderia: Escuderia,
        cantidad: float
    ) -> None:
        escuderia.gastar_presupuesto(cantidad)

