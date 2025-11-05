"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 3
"""

# ================================================================================
# ARCHIVO 1/3: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio/__init__.py
# ================================================================================

"""
Servicios de alto nivel
"""


# ================================================================================
# ARCHIVO 2/3: campeonato_service.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio/campeonato_service.py
# ================================================================================

from python_racing.entidades.circuitos.carrera import Carrera
from python_racing.entidades.escuderias.corredor import Corredor


class CampeonatoService:

    def __init__(self):
        self._carreras: list[Carrera] = []
        self._nombre = "MotoGP 2025"

    def agregar_carrera(self, carrera: Carrera) -> None:
        """Agrega una carrera al campeonato."""
        self._carreras.append(carrera)

    def obtener_clasificacion_general(self) -> list[tuple[Corredor, int]]:
        puntos_corredores = {}
        
        # Sumar puntos de todas las carreras
        for carrera in self._carreras:
            for resultado in carrera.get_resultados():
                corredor = resultado.get_corredor()
                puntos_corredores[corredor] = corredor.get_puntos_campeonato()
        
        # Ordenar por puntos
        clasificacion = sorted(
            puntos_corredores.items(),
            key=lambda x: x[1],
            reverse=True
        )
        
        return clasificacion

    def obtener_lider(self) -> Corredor:
        """Retorna el líder del campeonato."""
        clasificacion = self.obtener_clasificacion_general()
        if clasificacion:
            return clasificacion[0][0]
        return None

    def mostrar_clasificacion(self) -> None:
        """Imprime la clasificación del campeonato."""
        print("\n" + "=" * 70)
        print(f"CLASIFICACIÓN {self._nombre}".center(70))
        print("=" * 70)
        
        clasificacion = self.obtener_clasificacion_general()
        
        for pos, (corredor, puntos) in enumerate(clasificacion, 1):
            escuderia = corredor.get_escuderia()
            escuderia_str = escuderia.get_nombre() if escuderia else "Sin equipo"
            
            print(
                f"{pos:2d}. #{corredor.get_numero():2d} "
                f"{corredor.get_nombre():30s} "
                f"({escuderia_str:25s}) - "
                f"{puntos:3d} pts"
            )
        
        print("=" * 70)

# ================================================================================
# ARCHIVO 3/3: paquete.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio/paquete.py
# ================================================================================



