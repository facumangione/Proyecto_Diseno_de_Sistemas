"""
INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO
============================================================================
Directorio raiz: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing
Fecha de generacion: 2025-11-04 23:09:58
Total de archivos integrados: 75
Total de directorios procesados: 26
============================================================================
"""

# ==============================================================================
# TABLA DE CONTENIDOS
# ==============================================================================

# DIRECTORIO: .
#   1. __init__.py
#   2. buscar_paquete.py
#   3. constante.py
#   4. main.py
#
# DIRECTORIO: python_racing
#   5. __init__.py
#
# DIRECTORIO: python_racing/command
#   6. __init__.py
#   7. command.py
#
# DIRECTORIO: python_racing/command/impl
#   8. __init__.py
#   9. cambio_neumatico_command.py
#   10. carga_combustible_command.py
#   11. entrada_boxes_command.py
#
# DIRECTORIO: python_racing/entidades
#   12. __init__.py
#
# DIRECTORIO: python_racing/entidades/circuitos
#   13. __init__.py
#   14. carrera.py
#   15. circuito.py
#   16. vuelta.py
#
# DIRECTORIO: python_racing/entidades/escuderias
#   17. __init__.py
#   18. corredor.py
#   19. escuderia.py
#
# DIRECTORIO: python_racing/entidades/mantenimiento
#   20. __init__.py
#   21. fallo_mecanico.py
#
# DIRECTORIO: python_racing/entidades/motos
#   22. __init__.py
#   23. moto.py
#   24. motor.py
#   25. neumatico.py
#   26. tipo_neumatico.py
#
# DIRECTORIO: python_racing/entidades/personal
#   27. __init__.py
#   28. mecanico.py
#
# DIRECTORIO: python_racing/excepciones
#   29. __init__.py
#   30. combustible_excedido_exception.py
#   31. combustible_insuficiente_exception.py
#   32. fallo_grave_exception.py
#   33. mensajes_exception.py
#   34. presupuesto_insuficiente_exception.py
#   35. racing_exception.py
#
# DIRECTORIO: python_racing/patrones
#   36. __init__.py
#
# DIRECTORIO: python_racing/patrones/factory
#   37. __init__.py
#   38. moto_factory.py
#
# DIRECTORIO: python_racing/patrones/observer
#   39. __init__.py
#   40. observable.py
#   41. observer.py
#
# DIRECTORIO: python_racing/patrones/singleton
#   42. __init__.py
#   43. singleton.py
#
# DIRECTORIO: python_racing/patrones/strategy
#   44. __init__.py
#   45. neumatico_strategy.py
#
# DIRECTORIO: python_racing/patrones/strategy/impl
#   46. __init__.py
#   47. intermedio_strategy.py
#   48. lluvia_strategy.py
#   49. slick_strategy.py
#
# DIRECTORIO: python_racing/servicios
#   50. __init__.py
#
# DIRECTORIO: python_racing/servicios/circuitos
#   51. __init__.py
#   52. carrera_service.py
#   53. circuito_service.py
#
# DIRECTORIO: python_racing/servicios/escuderias
#   54. __init__.py
#   55. corredor_service.py
#   56. escuderia_service.py
#
# DIRECTORIO: python_racing/servicios/motos
#   57. __init__.py
#   58. moto_service.py
#   59. moto_service_registry.py
#   60. motor_service.py
#   61. neumatico_service.py
#
# DIRECTORIO: python_racing/servicios/negocio
#   62. __init__.py
#   63. campeonato_service.py
#   64. paquete.py
#
# DIRECTORIO: python_racing/telemetria
#   65. __init__.py
#
# DIRECTORIO: python_racing/telemetria/control
#   66. __init__.py
#   67. control_boxes_task.py
#
# DIRECTORIO: python_racing/telemetria/sensores
#   68. __init__.py
#   69. combustible_sensor.py
#   70. temperatura_motor_sensor.py
#   71. velocidad_sensor.py
#
# DIRECTORIO: python_racing/tests
#   72. __init__.py
#   73. test_carreras.py
#   74. test_motos.py
#   75. test_telemetria.py
#



################################################################################
# DIRECTORIO: .
################################################################################

# ==============================================================================
# ARCHIVO 1/75: __init__.py
# Directorio: .
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/__init__.py
# ==============================================================================

"""
PythonRacing - Sistema de Gestión de Carreras de Motos
======================================================

Sistema educativo que demuestra la implementación de patrones de diseño
en Python con enfoque en carreras de MotoGP.

Patrones implementados:
- SINGLETON: MotoServiceRegistry
- FACTORY METHOD: MotoFactory
- OBSERVER: Sistema de sensores de telemetría
- STRATEGY: Algoritmos de desgaste de neumáticos
- COMMAND: Acciones de boxes

Versión: 1.0.0
Python: 3.13+
"""

__version__ = "1.0.0"
__author__ = "PythonRacing Contributors"

# NO importes todo aquí, deja que cada módulo importe lo que necesita

# ==============================================================================
# ARCHIVO 2/75: buscar_paquete.py
# Directorio: .
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/buscar_paquete.py
# ==============================================================================

"""
Script para buscar el paquete python_racing desde el directorio raiz del proyecto.
Incluye funcionalidad para integrar archivos Python en cada nivel del arbol de directorios.
"""
import os
import sys
from datetime import datetime


def buscar_paquete(directorio_raiz: str, nombre_paquete: str) -> list:
    """
    Busca un paquete Python en el directorio raiz y subdirectorios.

    Args:
        directorio_raiz: Directorio desde donde iniciar la busqueda
        nombre_paquete: Nombre del paquete a buscar

    Returns:
        Lista de rutas donde se encontro el paquete
    """
    paquetes_encontrados = []

    for raiz, directorios, archivos in os.walk(directorio_raiz):
        # Verificar si el directorio actual es el paquete buscado
        nombre_dir = os.path.basename(raiz)

        if nombre_dir == nombre_paquete:
            # Verificar que sea un paquete Python (contiene __init__.py)
            if '__init__.py' in archivos:
                paquetes_encontrados.append(raiz)
                print(f"[+] Paquete encontrado: {raiz}")
            else:
                print(f"[!] Directorio encontrado pero no es un paquete Python: {raiz}")

    return paquetes_encontrados


def obtener_archivos_python(directorio: str) -> list:
    """
    Obtiene todos los archivos Python en un directorio (sin recursion).

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de archivos .py
    """
    archivos_python = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isfile(ruta_completa) and item.endswith('.py'):
                # Excluir archivos integradores para evitar recursion infinita
                if item not in ['integrador.py', 'integradorFinal.py']:
                    archivos_python.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(archivos_python)


def obtener_subdirectorios(directorio: str) -> list:
    """
    Obtiene todos los subdirectorios inmediatos de un directorio.

    Args:
        directorio: Ruta del directorio a examinar

    Returns:
        Lista de rutas completas de subdirectorios
    """
    subdirectorios = []
    try:
        for item in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, item)
            if os.path.isdir(ruta_completa):
                # Excluir directorios especiales
                if not item.startswith('.') and item not in ['__pycache__', 'venv', '.venv']:
                    subdirectorios.append(ruta_completa)
    except PermissionError:
        print(f"[!] Sin permisos para leer: {directorio}")

    return sorted(subdirectorios)


def leer_contenido_archivo(ruta_archivo: str) -> str:
    """
    Lee el contenido de un archivo Python.

    Args:
        ruta_archivo: Ruta completa del archivo

    Returns:
        Contenido del archivo como string
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            return archivo.read()
    except Exception as error:
        print(f"[!] Error al leer {ruta_archivo}: {error}")
        return f"# Error al leer este archivo: {error}\n"


def crear_archivo_integrador(directorio: str, archivos_python: list) -> bool:
    """
    Crea un archivo integrador.py con el contenido de todos los archivos Python.

    Args:
        directorio: Directorio donde crear el archivo integrador
        archivos_python: Lista de rutas de archivos Python a integrar

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_python:
        return False

    ruta_integrador = os.path.join(directorio, 'integrador.py')

    try:
        with open(ruta_integrador, 'w', encoding='utf-8') as integrador:
            # Encabezado
            integrador.write('"""\n')
            integrador.write(f"Archivo integrador generado automaticamente\n")
            integrador.write(f"Directorio: {directorio}\n")
            integrador.write(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador.write(f"Total de archivos integrados: {len(archivos_python)}\n")
            integrador.write('"""\n\n')

            # Integrar cada archivo
            for idx, archivo in enumerate(archivos_python, 1):
                nombre_archivo = os.path.basename(archivo)
                integrador.write(f"# {'=' * 80}\n")
                integrador.write(f"# ARCHIVO {idx}/{len(archivos_python)}: {nombre_archivo}\n")
                integrador.write(f"# Ruta: {archivo}\n")
                integrador.write(f"# {'=' * 80}\n\n")

                contenido = leer_contenido_archivo(archivo)
                integrador.write(contenido)
                integrador.write("\n\n")

        print(f"[OK] Integrador creado: {ruta_integrador}")
        print(f"     Archivos integrados: {len(archivos_python)}")
        return True

    except Exception as error:
        print(f"[!] Error al crear integrador en {directorio}: {error}")
        return False


def procesar_directorio_recursivo(directorio: str, nivel: int = 0, archivos_totales: list = None) -> list:
    """
    Procesa un directorio de forma recursiva, creando integradores en cada nivel.
    Utiliza DFS (Depth-First Search) para llegar primero a los niveles mas profundos.

    Args:
        directorio: Directorio a procesar
        nivel: Nivel de profundidad actual (para logging)
        archivos_totales: Lista acumulativa de todos los archivos procesados

    Returns:
        Lista de todos los archivos Python procesados en el arbol
    """
    if archivos_totales is None:
        archivos_totales = []

    indentacion = "  " * nivel
    print(f"{indentacion}[INFO] Procesando nivel {nivel}: {os.path.basename(directorio)}")

    # Obtener subdirectorios
    subdirectorios = obtener_subdirectorios(directorio)

    # Primero, procesar recursivamente todos los subdirectorios (DFS)
    for subdir in subdirectorios:
        procesar_directorio_recursivo(subdir, nivel + 1, archivos_totales)

    # Despues de procesar subdirectorios, procesar archivos del nivel actual
    archivos_python = obtener_archivos_python(directorio)

    if archivos_python:
        print(f"{indentacion}[+] Encontrados {len(archivos_python)} archivo(s) Python")
        crear_archivo_integrador(directorio, archivos_python)
        # Agregar archivos a la lista total
        archivos_totales.extend(archivos_python)
    else:
        print(f"{indentacion}[INFO] No hay archivos Python en este nivel")

    return archivos_totales


def crear_integrador_final(directorio_raiz: str, archivos_totales: list) -> bool:
    """
    Crea un archivo integradorFinal.py con TODO el codigo fuente de todas las ramas.

    Args:
        directorio_raiz: Directorio donde crear el archivo integrador final
        archivos_totales: Lista completa de todos los archivos Python procesados

    Returns:
        True si se creo exitosamente, False en caso contrario
    """
    if not archivos_totales:
        print("[!] No hay archivos para crear el integrador final")
        return False

    ruta_integrador_final = os.path.join(directorio_raiz, 'integradorFinal.py')

    # Organizar archivos por directorio para mejor estructura
    archivos_por_directorio = {}
    for archivo in archivos_totales:
        directorio = os.path.dirname(archivo)
        if directorio not in archivos_por_directorio:
            archivos_por_directorio[directorio] = []
        archivos_por_directorio[directorio].append(archivo)

    try:
        with open(ruta_integrador_final, 'w', encoding='utf-8') as integrador_final:
            # Encabezado principal
            integrador_final.write('"""\n')
            integrador_final.write("INTEGRADOR FINAL - CONSOLIDACION COMPLETA DEL PROYECTO\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write(f"Directorio raiz: {directorio_raiz}\n")
            integrador_final.write(f"Fecha de generacion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write(f"Total de archivos integrados: {len(archivos_totales)}\n")
            integrador_final.write(f"Total de directorios procesados: {len(archivos_por_directorio)}\n")
            integrador_final.write("=" * 76 + "\n")
            integrador_final.write('"""\n\n')

            # Tabla de contenidos
            integrador_final.write("# " + "=" * 78 + "\n")
            integrador_final.write("# TABLA DE CONTENIDOS\n")
            integrador_final.write("# " + "=" * 78 + "\n\n")

            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)
                    integrador_final.write(f"#   {contador_global}. {nombre_archivo}\n")
                    contador_global += 1
                integrador_final.write("#\n")

            integrador_final.write("\n\n")

            # Contenido completo organizado por directorio
            contador_global = 1
            for directorio in sorted(archivos_por_directorio.keys()):
                dir_relativo = os.path.relpath(directorio, directorio_raiz)

                # Separador de directorio
                integrador_final.write("\n" + "#" * 80 + "\n")
                integrador_final.write(f"# DIRECTORIO: {dir_relativo}\n")
                integrador_final.write("#" * 80 + "\n\n")

                # Procesar cada archivo del directorio
                for archivo in sorted(archivos_por_directorio[directorio]):
                    nombre_archivo = os.path.basename(archivo)

                    integrador_final.write(f"# {'=' * 78}\n")
                    integrador_final.write(f"# ARCHIVO {contador_global}/{len(archivos_totales)}: {nombre_archivo}\n")
                    integrador_final.write(f"# Directorio: {dir_relativo}\n")
                    integrador_final.write(f"# Ruta completa: {archivo}\n")
                    integrador_final.write(f"# {'=' * 78}\n\n")

                    contenido = leer_contenido_archivo(archivo)
                    integrador_final.write(contenido)
                    integrador_final.write("\n\n")

                    contador_global += 1

            # Footer
            integrador_final.write("\n" + "#" * 80 + "\n")
            integrador_final.write("# FIN DEL INTEGRADOR FINAL\n")
            integrador_final.write(f"# Total de archivos: {len(archivos_totales)}\n")
            integrador_final.write(f"# Generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            integrador_final.write("#" * 80 + "\n")

        print(f"\n[OK] Integrador final creado: {ruta_integrador_final}")
        print(f"     Total de archivos integrados: {len(archivos_totales)}")
        print(f"     Total de directorios procesados: {len(archivos_por_directorio)}")

        # Mostrar tamanio del archivo
        tamanio = os.path.getsize(ruta_integrador_final)
        if tamanio < 1024:
            tamanio_str = f"{tamanio} bytes"
        elif tamanio < 1024 * 1024:
            tamanio_str = f"{tamanio / 1024:.2f} KB"
        else:
            tamanio_str = f"{tamanio / (1024 * 1024):.2f} MB"
        print(f"     Tamanio del archivo: {tamanio_str}")

        return True

    except Exception as error:
        print(f"[!] Error al crear integrador final: {error}")
        return False


def integrar_arbol_directorios(directorio_raiz: str) -> None:
    """
    Inicia el proceso de integracion para todo el arbol de directorios.

    Args:
        directorio_raiz: Directorio raiz desde donde comenzar
    """
    print("\n" + "=" * 80)
    print("INICIANDO INTEGRACION DE ARCHIVOS PYTHON")
    print("=" * 80)
    print(f"Directorio raiz: {directorio_raiz}\n")

    # Procesar directorios y obtener lista de todos los archivos
    archivos_totales = procesar_directorio_recursivo(directorio_raiz)

    print("\n" + "=" * 80)
    print("INTEGRACION POR NIVELES COMPLETADA")
    print("=" * 80)

    # Crear integrador final con todos los archivos
    if archivos_totales:
        print("\n" + "=" * 80)
        print("CREANDO INTEGRADOR FINAL")
        print("=" * 80)
        crear_integrador_final(directorio_raiz, archivos_totales)

    print("\n" + "=" * 80)
    print("PROCESO COMPLETO FINALIZADO")
    print("=" * 80)


def main():
    """Funcion principal del script."""
    # Obtener el directorio raiz del proyecto (donde esta este script)
    directorio_raiz = os.path.dirname(os.path.abspath(__file__))

    # Verificar argumentos de linea de comandos
    if len(sys.argv) > 1:
        comando = sys.argv[1].lower()

        if comando == "integrar":
            # Modo de integracion de archivos
            if len(sys.argv) > 2:
                directorio_objetivo = sys.argv[2]
                if not os.path.isabs(directorio_objetivo):
                    directorio_objetivo = os.path.join(directorio_raiz, directorio_objetivo)
            else:
                directorio_objetivo = directorio_raiz

            if not os.path.isdir(directorio_objetivo):
                print(f"[!] El directorio no existe: {directorio_objetivo}")
                return 1

            integrar_arbol_directorios(directorio_objetivo)
            return 0

        elif comando == "help" or comando == "--help" or comando == "-h":
            print("Uso: python buscar_paquete.py [COMANDO] [OPCIONES]")
            print("")
            print("Comandos disponibles:")
            print("  (sin argumentos)     Busca el paquete python_racing")
            print("  integrar [DIR]       Integra archivos Python en el arbol de directorios")
            print("                       DIR: directorio raiz (por defecto: directorio actual)")
            print("  help                 Muestra esta ayuda")
            print("")
            print("Ejemplos:")
            print("  python buscar_paquete.py")
            print("  python buscar_paquete.py integrar")
            print("  python buscar_paquete.py integrar python_racing")
            return 0

        else:
            print(f"[!] Comando desconocido: {comando}")
            print("    Use 'python buscar_paquete.py help' para ver los comandos disponibles")
            return 1

    # Modo por defecto: buscar paquete
    print(f"[INFO] Buscando desde: {directorio_raiz}")
    print(f"[INFO] Buscando paquete: python_racing")
    print("")

    # Buscar el paquete
    paquetes = buscar_paquete(directorio_raiz, "python_racing")

    print("")
    if paquetes:
        print(f"[OK] Se encontraron {len(paquetes)} paquete(s):")
        for paquete in paquetes:
            print(f"  - {paquete}")

            # Mostrar estructura basica del paquete
            print(f"    Contenido:")
            try:
                contenido = os.listdir(paquete)
                for item in sorted(contenido)[:10]:  # Mostrar primeros 10 items
                    ruta_item = os.path.join(paquete, item)
                    if os.path.isdir(ruta_item):
                        print(f"      [DIR]  {item}")
                    else:
                        print(f"      [FILE] {item}")
                if len(contenido) > 10:
                    print(f"      ... y {len(contenido) - 10} items mas")
            except PermissionError:
                print(f"      [!] Sin permisos para leer el directorio")
    else:
        print("[!] No se encontro el paquete python_racing")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())

# ==============================================================================
# ARCHIVO 3/75: constante.py
# Directorio: .
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/constante.py
# ==============================================================================

# ============================================================================
# constante.py - PythonRacing
# ============================================================================
# Todas las constantes del sistema centralizadas.
# NO hardcodear valores mágicos en el código.
# ============================================================================

# ============================================================================
# MOTOS - Especificaciones por Marca
# ============================================================================

# Ducati Desmosedici GP25
COMBUSTIBLE_MAX_DUCATI = 22.0
POTENCIA_DUCATI = 275
PESO_DUCATI = 157
REV_MAX_DUCATI = 18000

# Yamaha YZR-M1
COMBUSTIBLE_MAX_YAMAHA = 21.5
POTENCIA_YAMAHA = 270
PESO_YAMAHA = 158
REV_MAX_YAMAHA = 17500

# KTM RC16
COMBUSTIBLE_MAX_KTM = 21.8
POTENCIA_KTM = 265
PESO_KTM = 159
REV_MAX_KTM = 17800

# Honda RC213V
COMBUSTIBLE_MAX_HONDA = 22.0
POTENCIA_HONDA = 268
PESO_HONDA = 157
REV_MAX_HONDA = 17900

# ============================================================================
# NEUMÁTICOS - Desgaste por Tipo y Condición
# ============================================================================

# Desgaste por vuelta (porcentaje)
DESGASTE_SLICK_SECO = 0.02      # 2% por vuelta en seco
DESGASTE_SLICK_LLUVIA = 0.10    # 10% por vuelta en lluvia
DESGASTE_INTERMEDIO_SECO = 0.05
DESGASTE_INTERMEDIO_LLUVIA = 0.03
DESGASTE_LLUVIA_SECO = 0.15
DESGASTE_LLUVIA_LLUVIA = 0.02

# Vida útil de neumáticos (vueltas)
VIDA_NEUMATICO_SLICK = 25
VIDA_NEUMATICO_INTERMEDIO = 20
VIDA_NEUMATICO_LLUVIA = 30

# ============================================================================
# TELEMETRÍA - Sensores y Alertas
# ============================================================================

# Temperatura del motor
TEMP_MOTOR_MIN = 40        # °C
TEMP_MOTOR_MAX = 130       # °C
TEMP_MOTOR_OPTIMA = 85     # °C
TEMP_MOTOR_ALERTA = 120    # °C
TEMP_MOTOR_CRITICA = 125   # °C

# Combustible
COMBUSTIBLE_ALERTA = 10.0  # porcentaje
COMBUSTIBLE_CRITICO = 5.0  # porcentaje

# Velocidad
VELOCIDAD_MAX_MOTOGP = 350  # km/h
VELOCIDAD_PROMEDIO = 180    # km/h

# ============================================================================
# SENSORES - Intervalos de Lectura (segundos)
# ============================================================================

INTERVALO_TEMP_MOTOR = 2.0
INTERVALO_COMBUSTIBLE = 1.0
INTERVALO_VELOCIDAD = 0.5
INTERVALO_CONTROL_BOXES = 3.0
THREAD_JOIN_TIMEOUT = 2.0

# ============================================================================
# CARRERAS - Configuración de Competencias
# ============================================================================

VUELTAS_DEFAULT = 25
VUELTAS_SPRINT = 10
TIEMPO_VUELTA_BASE = 90      # segundos
TIEMPO_ENTRADA_BOXES = 30    # segundos
TIEMPO_CAMBIO_NEUMATICOS = 5 # segundos
TIEMPO_CARGA_COMBUSTIBLE = 10 # segundos

# ============================================================================
# CIRCUITOS - Longitudes y Características
# ============================================================================

# Longitud promedio de circuitos MotoGP (km)
LONGITUD_MIN_CIRCUITO = 3.5
LONGITUD_MAX_CIRCUITO = 6.0

# ============================================================================
# ESCUDERÍAS - Límites Financieros
# ============================================================================

PRESUPUESTO_MIN_ESCUDERIA = 1000000.0    # 1 millón
PRESUPUESTO_MAX_ESCUDERIA = 50000000.0   # 50 millones

# Costos de operación
COSTO_CARRERA = 100000.0
COSTO_REPARACION_LEVE = 5000.0
COSTO_REPARACION_MEDIA = 25000.0
COSTO_REPARACION_GRAVE = 100000.0

# ============================================================================
# CORREDORES - Restricciones
# ============================================================================

EDAD_MIN_CORREDOR = 18
EDAD_MAX_CORREDOR = 50
NUMERO_MIN_CORREDOR = 1
NUMERO_MAX_CORREDOR = 99

# ============================================================================
# PERSISTENCIA - Configuración de Archivos
# ============================================================================

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# ============================================================================
# SIMULACIÓN - Factores de Aleatoriedad
# ============================================================================

# Probabilidad de fallos mecánicos (por vuelta)
PROB_FALLO_MOTOR = 0.001      # 0.1%
PROB_FALLO_FRENOS = 0.002     # 0.2%
PROB_FALLO_SUSPENSION = 0.003 # 0.3%
PROB_FALLO_ELECTRONICA = 0.002

# Factores de rendimiento
FACTOR_EXPERIENCIA = 0.95  # Reduce tiempo por vuelta
FACTOR_NEUMATICO_NUEVO = 0.98
FACTOR_NEUMATICO_GASTADO = 1.05
FACTOR_COMBUSTIBLE_BAJO = 1.02

# ============================================================================
# CLIMA - Condiciones de Pista
# ============================================================================

PROB_LLUVIA = 0.15           # 15% probabilidad de lluvia
PROB_CAMBIO_CLIMA = 0.05     # 5% cambio por vuelta

# ==============================================================================
# ARCHIVO 4/75: main.py
# Directorio: .
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/main.py
# ==============================================================================

import time
from datetime import date

# Servicios
from python_racing.servicios.escuderias.escuderia_service import EscuderiaService
from python_racing.servicios.escuderias.corredor_service import CorredorService
from python_racing.servicios.circuitos.circuito_service import CircuitoService
from python_racing.servicios.circuitos.carrera_service import CarreraService
from python_racing.servicios.motos.moto_service import MotoService
from python_racing.servicios.motos.moto_service_registry import MotoServiceRegistry

# Patrones
from python_racing.patrones.factory.moto_factory import MotoFactory

# Entidades
from python_racing.entidades.circuitos.circuito import TipoSuperficie
from python_racing.entidades.motos.neumatico import TipoNeumatico

# Telemetría
from python_racing.telemetria.sensores.temperatura_motor_sensor import TemperaturaMotorSensor
from python_racing.telemetria.sensores.combustible_sensor import CombustibleSensor
from python_racing.telemetria.sensores.velocidad_sensor import VelocidadSensor
from python_racing.telemetria.control.control_boxes_task import ControlBoxesTask

# Constantes
from constante import THREAD_JOIN_TIMEOUT


def imprimir_encabezado(titulo: str, caracter: str = "=", ancho: int = 70):
    """Imprime un encabezado decorado."""
    print("\n" + caracter * ancho)
    print(titulo.center(ancho))
    print(caracter * ancho)


def imprimir_seccion(titulo: str, ancho: int = 70):
    """Imprime una sección con guiones."""
    print("\n" + "-" * ancho)
    print("  " + titulo)
    print("-" * ancho)


def demostrar_singleton_registry():
    """Demuestra los patrones SINGLETON y REGISTRY."""
    imprimir_seccion("PATRON SINGLETON + REGISTRY: MotoServiceRegistry")
    
    print("\n1. Verificando Singleton (múltiples instancias):")
    registry1 = MotoServiceRegistry()
    registry2 = MotoServiceRegistry()
    registry3 = MotoServiceRegistry()
    
    if registry1 is registry2 is registry3:
        print("   [OK] Todas las instancias son LA MISMA (Singleton)")
        print(f"   ID registry1: {id(registry1)}")
        print(f"   ID registry2: {id(registry2)}")
        print(f"   ID registry3: {id(registry3)}")
    else:
        print("   [ERROR] Singleton NO funciona correctamente")
    
    print("\n2. Creando motos de diferentes marcas:")
    ducati = MotoFactory.crear_moto("Ducati")
    yamaha = MotoFactory.crear_moto("Yamaha")
    ktm = MotoFactory.crear_moto("KTM")
    honda = MotoFactory.crear_moto("Honda")
    
    motos = [ducati, yamaha, ktm, honda]
    print(f"   [OK] {len(motos)} motos creadas")
    
    print("\n3. Mostrando datos usando Registry (dispatch polimórfico):")
    print("   " + "=" * 60)
    
    for moto in motos:
        # ✅ Registry hace dispatch automático SIN isinstance()
        registry1.mostrar_datos(moto)
    
    print("\n4. Verificando estado de todas las motos:")
    print("   " + "=" * 60)
    
    for moto in motos:
        estado = registry1.verificar_estado(moto)
        print(f"\n   {estado['marca']}:")
        print(f"     Estado: {estado['estado']}")
        for alerta in estado['alertas']:
            print(f"     {alerta}")
    
    print("\n   " + "=" * 60)
    
    print("\n5. Marcas registradas en el sistema:")
    marcas = registry1.listar_marcas_registradas()
    print(f"   {', '.join(marcas)}")
    
    print("\n[OK] Patrones SINGLETON + REGISTRY funcionan correctamente")
    print("     - Singleton: Única instancia compartida thread-safe")
    print("     - Registry: Dispatch polimórfico SIN isinstance()")


def demostrar_factory():
    """Demuestra el patrón FACTORY METHOD."""
    imprimir_seccion("PATRON FACTORY: Creacion dinamica de motos")
    
    print("\nCreando motos de diferentes marcas usando Factory Method:")
    
    marcas = ["Ducati", "Yamaha", "KTM", "Honda"]
    
    for marca in marcas:
        moto = MotoFactory.crear_moto(marca)
        print(f"  [OK] {moto}")
    
    print("\n[OK] Factory Method funciono correctamente")
    print("     El cliente NO conoce las clases concretas")


def demostrar_strategy(moto_service: MotoService):
    """Demuestra el patrón STRATEGY."""
    imprimir_seccion("PATRON STRATEGY: Desgaste de neumaticos")
    
    print("\nCreando moto y asignando neumáticos:")
    moto = MotoFactory.crear_moto("Ducati")
    print(f"  {moto}")
    
    print("\nAsignando neumáticos SLICK (óptimos en SECO):")
    moto_service.asignar_neumaticos(moto, TipoNeumatico.SLICK)
    print("  [OK] Neumáticos slick instalados")
    
    print("\nSimulando desgaste en pista SECA (5 vueltas):")
    from python_racing.entidades.circuitos.circuito import CondicionClimatica
    
    for vuelta in range(1, 6):
        moto_service.aplicar_desgaste_neumaticos(
            moto,
            CondicionClimatica.SECO,
            4.8
        )
        desgaste = moto.get_neumatico_delantero().get_desgaste()
        print(f"  Vuelta {vuelta}: Desgaste = {desgaste:.1f}%")
    
    print("\n[OK] Patron Strategy funciono correctamente")
    print("     Algoritmo de desgaste intercambiable según tipo de neumático")


def demostrar_observer():
    """Demuestra el patrón OBSERVER."""
    imprimir_seccion("PATRON OBSERVER: Sistema de telemetria")
    
    print("\nCreando moto y sensores:")
    moto = MotoFactory.crear_moto("Ducati")
    
    print("\n1. Inicializando sensores (Observable)...")
    sensor_temp = TemperaturaMotorSensor()
    sensor_combustible = CombustibleSensor(moto)
    sensor_velocidad = VelocidadSensor()
    print("   [OK] 3 sensores creados")
    
    print("\n2. Inicializando controlador de boxes (Observer)...")
    controlador = ControlBoxesTask(moto)
    print("   [OK] Controlador creado")
    
    print("\n3. Registrando observadores...")
    sensor_temp.agregar_observador(controlador)
    sensor_combustible.agregar_observador(controlador)
    print("   [OK] Controlador suscrito a sensores")
    
    print("\n4. Iniciando threads daemon...")
    sensor_temp.start()
    sensor_combustible.start()
    sensor_velocidad.start()
    controlador.start()
    print("   [OK] Sistema de telemetría activo")
    
    print("\n5. Monitoreando durante 5 segundos:")
    print("   " + "=" * 60)
    
    for i in range(5):
        time.sleep(1)
        print(f"\n   Segundo {i+1}:")
        print(f"     Temperatura: {sensor_temp.get_temperatura_actual():.1f}°C")
        print(f"     Combustible: {sensor_combustible.get_nivel_actual():.1f}%")
        print(f"     Velocidad: {sensor_velocidad.get_velocidad_actual():.1f} km/h")
        print(f"     Estado: {controlador.obtener_estado()}")
    
    print("\n   " + "=" * 60)
    
    # Detener threads
    print("\n6. Deteniendo sistema de telemetría...")
    sensor_temp.detener()
    sensor_combustible.detener()
    sensor_velocidad.detener()
    controlador.detener()
    
    sensor_temp.join(timeout=THREAD_JOIN_TIMEOUT)
    sensor_combustible.join(timeout=THREAD_JOIN_TIMEOUT)
    sensor_velocidad.join(timeout=THREAD_JOIN_TIMEOUT)
    controlador.join(timeout=THREAD_JOIN_TIMEOUT)
    
    print("   [OK] Todos los threads detenidos correctamente")
    
    print("\n[OK] Patron Observer funciono correctamente")
    print("     Notificaciones automaticas entre sensores y controlador")


def demostrar_simulacion_carrera():
    """Demuestra una simulación de carrera completa."""
    imprimir_seccion("SIMULACION DE CARRERA COMPLETA")
    
    # Crear servicios
    escuderia_service = EscuderiaService()
    corredor_service = CorredorService()
    circuito_service = CircuitoService()
    carrera_service = CarreraService()
    
    # Crear escuderías
    print("\n1. Creando escuderías...")
    ducati = escuderia_service.crear_escuderia("Ducati Lenovo Team", "Italia", 15000000)
    yamaha = escuderia_service.crear_escuderia("Monster Energy Yamaha", "Japón", 14000000)
    print(f"   [OK] {ducati}")
    print(f"   [OK] {yamaha}")
    
    # Crear corredores
    print("\n2. Registrando corredores...")
    bagnaia = corredor_service.registrar_corredor(
        "Francesco Bagnaia", "Italia", 63, 27, ducati
    )
    bastianini = corredor_service.registrar_corredor(
        "Enea Bastianini", "Italia", 23, 26, ducati
    )
    quartararo = corredor_service.registrar_corredor(
        "Fabio Quartararo", "Francia", 20, 25, yamaha
    )
    print(f"   [OK] {bagnaia}")
    print(f"   [OK] {bastianini}")
    print(f"   [OK] {quartararo}")
    
    # Crear circuito
    print("\n3. Registrando circuito...")
    circuito = circuito_service.registrar_circuito(
        "Autódromo Termas de Río Hondo",
        4.8,
        "Argentina",
        TipoSuperficie.ASFALTO
    )
    print(f"   [OK] {circuito}")
    
    # Simular carrera
    print("\n4. Simulando carrera de 25 vueltas...")
    carrera = carrera_service.simular_carrera(
        circuito,
        [bagnaia, bastianini, quartararo],
        25
    )
    
    # Mostrar resultados
    print("\n5. Resultados de la carrera:")
    print("   " + "=" * 60)
    
    for resultado in carrera.get_resultados():
        print(f"   {resultado}")
    
    print("   " + "=" * 60)
    
    # Mostrar podio
    print("\n6. Podio:")
    podio = carrera.obtener_podio()
    medallas = ["🥇", "🥈", "🥉"]
    
    for idx, resultado in enumerate(podio):
        print(f"   {medallas[idx]} {resultado.get_corredor().get_nombre()} - "
              f"{resultado.obtener_tiempo_formateado()}")
    
    print("\n[OK] Simulación de carrera completada exitosamente")


def main():
    """Función principal."""
    
    imprimir_encabezado("SISTEMA DE GESTION DE CARRERAS - PYTHONRACING")
    
    print("\nDemostración completa de patrones de diseño implementados:")
    print("  - SINGLETON (MotoServiceRegistry)")
    print("  - FACTORY METHOD (MotoFactory)")
    print("  - STRATEGY (Desgaste de neumáticos)")
    print("  - OBSERVER (Telemetría en tiempo real)")
    print("  - REGISTRY (Dispatch polimórfico)")
    
    try:
        # Crear servicios
        moto_service = MotoService()
        
        # 1. SINGLETON + REGISTRY
        demostrar_singleton_registry()
        
        # 2. FACTORY METHOD
        demostrar_factory()
        
        # 3. STRATEGY
        demostrar_strategy(moto_service)
        
        # 4. OBSERVER
        demostrar_observer()
        
        # 5. SIMULACIÓN COMPLETA
        demostrar_simulacion_carrera()
        
        # Resumen final
        imprimir_encabezado("EJEMPLO COMPLETADO EXITOSAMENTE")
        
        print("\nResumen de patrones demostrados:")
        print("  [OK] SINGLETON   - MotoServiceRegistry (instancia única)")
        print("  [OK] FACTORY     - Creación dinámica de 4 marcas de motos")
        print("  [OK] STRATEGY    - Algoritmos de desgaste intercambiables")
        print("  [OK] OBSERVER    - Sistema de telemetría con sensores")
        print("  [OK] REGISTRY    - Dispatch polimórfico sin isinstance()")
        
        print("\nFuncionalidades demostradas:")
        print("  [OK] Gestión de escuderías y corredores")
        print("  [OK] Gestión de motos con componentes")
        print("  [OK] Sistema de telemetría en tiempo real")
        print("  [OK] Simulación completa de carreras")
        print("  [OK] Cálculo de resultados y podio")
        
        print("\n" + "=" * 70)
        print("Gracias por utilizar PythonRacing".center(70))
        print("Sistema educativo de patrones de diseño en Python".center(70))
        print("=" * 70 + "\n")
        
        return 0
        
    except Exception as e:
        print(f"\n[ERROR CRITICO] {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())


################################################################################
# DIRECTORIO: python_racing
################################################################################

# ==============================================================================
# ARCHIVO 5/75: __init__.py
# Directorio: python_racing
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/__init__.py
# ==============================================================================

"""
Paquete principal de PythonRacing
"""



################################################################################
# DIRECTORIO: python_racing/command
################################################################################

# ==============================================================================
# ARCHIVO 6/75: __init__.py
# Directorio: python_racing/command
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/__init__.py
# ==============================================================================

from python_racing.command.command import Command
from python_racing.command.impl.entrada_boxes_command import EntradaBoxesCommand
from python_racing.command.impl.carga_combustible_command import CargaCombustibleCommand
from python_racing.command.impl.cambio_neumatico_command import CambioNeumaticoCommand

__all__ = [
    'Command',
    'EntradaBoxesCommand',
    'CargaCombustibleCommand',
    'CambioNeumaticoCommand'
]

# ==============================================================================
# ARCHIVO 7/75: command.py
# Directorio: python_racing/command
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/command.py
# ==============================================================================

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class Command(ABC):
    
    def __init__(self, moto: 'Moto'):
        self._moto = moto
        self._ejecutado = False
        self._tiempo_ejecucion = 0.0
    
    @abstractmethod
    def ejecutar(self) -> bool:
        pass
    
    @abstractmethod
    def deshacer(self) -> bool:
        pass
    
    def get_tiempo_ejecucion(self) -> float:
        return self._tiempo_ejecucion
    
    def esta_ejecutado(self) -> bool:
        return self._ejecutado
    
    @abstractmethod
    def get_descripcion(self) -> str:
        pass


################################################################################
# DIRECTORIO: python_racing/command/impl
################################################################################

# ==============================================================================
# ARCHIVO 8/75: __init__.py
# Directorio: python_racing/command/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/__init__.py
# ==============================================================================

"""
Comandos concretos de boxes
"""


# ==============================================================================
# ARCHIVO 9/75: cambio_neumatico_command.py
# Directorio: python_racing/command/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/cambio_neumatico_command.py
# ==============================================================================

from typing import TYPE_CHECKING, Optional
from python_racing.command.command import Command
from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico
from constante import TIEMPO_CAMBIO_NEUMATICOS

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class CambioNeumaticoCommand(Command):
    def __init__(self, moto: 'Moto', tipo_neumatico: TipoNeumatico):
        super().__init__(moto)
        self._tipo_neumatico = tipo_neumatico
        self._neumaticos_anteriores: Optional[tuple[Neumatico, Neumatico]] = None
    
    def ejecutar(self) -> bool:
        if self._ejecutado:
            print("[WARN] Comando ya ejecutado anteriormente")
            return False
        
        # Guardar neumáticos actuales para poder deshacer
        delantero_actual = self._moto.get_neumatico_delantero()
        trasero_actual = self._moto.get_neumatico_trasero()
        
        if delantero_actual is None or trasero_actual is None:
            raise ValueError("La moto no tiene neumáticos instalados")
        
        self._neumaticos_anteriores = (delantero_actual, trasero_actual)
        
        # Instalar nuevos neumáticos
        neumatico_delantero_nuevo = Neumatico(self._tipo_neumatico)
        neumatico_trasero_nuevo = Neumatico(self._tipo_neumatico)
        
        self._moto.set_neumatico_delantero(neumatico_delantero_nuevo)
        self._moto.set_neumatico_trasero(neumatico_trasero_nuevo)
        
        # Registrar tiempo y estado
        self._tiempo_ejecucion = TIEMPO_CAMBIO_NEUMATICOS
        self._ejecutado = True
        
        print(f"[OK] Neumáticos cambiados a {self._tipo_neumatico.value}")
        print(f"     Tiempo: {self._tiempo_ejecucion}s")
        
        return True
    
    def deshacer(self) -> bool:
        if not self._ejecutado:
            print("[WARN] No se puede deshacer un comando no ejecutado")
            return False
        
        if self._neumaticos_anteriores is None:
            print("[ERROR] No hay neumáticos anteriores guardados")
            return False
        
        # Restaurar neumáticos anteriores
        delantero_anterior, trasero_anterior = self._neumaticos_anteriores
        self._moto.set_neumatico_delantero(delantero_anterior)
        self._moto.set_neumatico_trasero(trasero_anterior)
        
        self._ejecutado = False
        print("[OK] Cambio de neumáticos deshecho")
        
        return True
    
    def get_descripcion(self) -> str:
        estado = "EJECUTADO" if self._ejecutado else "PENDIENTE"
        return (
            f"Cambio de neumáticos a {self._tipo_neumatico.value} "
            f"({TIEMPO_CAMBIO_NEUMATICOS}s) - {estado}"
        )
    
    def get_tipo_neumatico(self) -> TipoNeumatico:
        """Obtiene el tipo de neumático que se instalará/instaló."""
        return self._tipo_neumatico


# ==============================================================================
# ARCHIVO 10/75: carga_combustible_command.py
# Directorio: python_racing/command/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/carga_combustible_command.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_racing.command.command import Command
from python_racing.excepciones.combustible_excedido_exception import CombustibleExcedidoException
from constante import TIEMPO_CARGA_COMBUSTIBLE

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class CargaCombustibleCommand(Command):
    
    def __init__(self, moto: 'Moto', cantidad: float):
        super().__init__(moto)
        
        if cantidad <= 0:
            raise ValueError("La cantidad de combustible debe ser positiva")
        
        self._cantidad = cantidad
        self._combustible_anterior = 0.0
    
    def ejecutar(self) -> bool:
        if self._ejecutado:
            print("[WARN] Comando ya ejecutado anteriormente")
            return False
        
        # Guardar combustible actual para poder deshacer
        self._combustible_anterior = self._moto.get_combustible_actual()
        
        try:
            # Intentar cargar combustible
            self._moto.cargar_combustible(self._cantidad)
            
            # Registrar tiempo y estado
            self._tiempo_ejecucion = TIEMPO_CARGA_COMBUSTIBLE
            self._ejecutado = True
            
            print(f"[OK] Combustible cargado: {self._cantidad:.1f}L")
            print(f"     Nivel actual: {self._moto.get_combustible_actual():.1f}L/"
                  f"{self._moto.get_combustible_max():.1f}L")
            print(f"     Tiempo: {self._tiempo_ejecucion}s")
            
            return True
            
        except CombustibleExcedidoException as e:
            print(f"[ERROR] No se puede cargar combustible: {e}")
            raise
    
    def deshacer(self) -> bool:
        if not self._ejecutado:
            print("[WARN] No se puede deshacer un comando no ejecutado")
            return False
        
        # Calcular cuánto combustible hay que consumir para volver al estado anterior
        combustible_actual = self._moto.get_combustible_actual()
        diferencia = combustible_actual - self._combustible_anterior
        
        if diferencia > 0:
            # Consumir la diferencia (esto es artificial, pero permite el undo)
            try:
                self._moto.consumir_combustible(diferencia)
                self._ejecutado = False
                print("[OK] Carga de combustible deshecha")
                return True
            except Exception as e:
                print(f"[ERROR] No se pudo deshacer la carga: {e}")
                return False
        
        return False
    
    def get_descripcion(self) -> str:
        estado = "EJECUTADO" if self._ejecutado else "PENDIENTE"
        return (
            f"Carga de combustible: {self._cantidad:.1f}L "
            f"({TIEMPO_CARGA_COMBUSTIBLE}s) - {estado}"
        )
    
    def get_cantidad(self) -> float:
        """Obtiene la cantidad de combustible a cargar."""
        return self._cantidad
    
    def get_combustible_anterior(self) -> float:
        """Obtiene el nivel de combustible antes de la carga."""
        return self._combustible_anterior

# ==============================================================================
# ARCHIVO 11/75: entrada_boxes_command.py
# Directorio: python_racing/command/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/command/impl/entrada_boxes_command.py
# ==============================================================================

from typing import TYPE_CHECKING
from python_racing.command.command import Command
from constante import TIEMPO_ENTRADA_BOXES

if TYPE_CHECKING:
    from python_racing.entidades.motos.moto import Moto


class EntradaBoxesCommand(Command):
    def __init__(self, moto: 'Moto', vuelta: int, motivo: str = "Parada programada"):
        super().__init__(moto)
        self._vuelta = vuelta
        self._motivo = motivo
        self._tiempo_perdido = TIEMPO_ENTRADA_BOXES
    
    def ejecutar(self) -> bool:
        if self._ejecutado:
            print("[WARN] Comando ya ejecutado anteriormente")
            return False
        
        # Registrar tiempo y estado
        self._tiempo_ejecucion = self._tiempo_perdido
        self._ejecutado = True
        
        print(f"[OK] Entrada a boxes en vuelta {self._vuelta}")
        print(f"     Motivo: {self._motivo}")
        print(f"     Tiempo perdido: {self._tiempo_perdido}s")
        
        return True
    
    def deshacer(self) -> bool:
        print("[WARN] Una entrada a boxes no se puede deshacer")
        return False
    
    def get_descripcion(self) -> str:
        estado = "EJECUTADO" if self._ejecutado else "PENDIENTE"
        return (
            f"Entrada a boxes (vuelta {self._vuelta}) - "
            f"{self._motivo} - Tiempo: {self._tiempo_perdido}s - {estado}"
        )
    
    def get_vuelta(self) -> int:
        """Obtiene el número de vuelta de la entrada."""
        return self._vuelta
    
    def get_motivo(self) -> str:
        """Obtiene el motivo de la entrada a boxes."""
        return self._motivo
    
    def get_tiempo_perdido(self) -> float:
        """Obtiene el tiempo perdido por la entrada a boxes."""
        return self._tiempo_perdido


################################################################################
# DIRECTORIO: python_racing/entidades
################################################################################

# ==============================================================================
# ARCHIVO 12/75: __init__.py
# Directorio: python_racing/entidades
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/__init__.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_racing/entidades/circuitos
################################################################################

# ==============================================================================
# ARCHIVO 13/75: __init__.py
# Directorio: python_racing/entidades/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/__init__.py
# ==============================================================================

"""
Entidades de circuitos y carreras
"""


# ==============================================================================
# ARCHIVO 14/75: carrera.py
# Directorio: python_racing/entidades/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/carrera.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 15/75: circuito.py
# Directorio: python_racing/entidades/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/circuito.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 16/75: vuelta.py
# Directorio: python_racing/entidades/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/circuitos/vuelta.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_racing/entidades/escuderias
################################################################################

# ==============================================================================
# ARCHIVO 17/75: __init__.py
# Directorio: python_racing/entidades/escuderias
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/escuderias/__init__.py
# ==============================================================================

"""
Entidades de escuderías y corredores
"""


# ==============================================================================
# ARCHIVO 18/75: corredor.py
# Directorio: python_racing/entidades/escuderias
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/escuderias/corredor.py
# ==============================================================================

from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.escuderia import Escuderia


class Corredor:
    """
    Representa un corredor de MotoGP.
    
    Attributes:
        nombre: Nombre completo
        nacionalidad: País de origen
        numero: Número de carrera (1-99)
        edad: Edad del corredor
        escuderia: Escudería a la que pertenece
        puntos_campeonato: Puntos acumulados en el campeonato
    """

    def __init__(
        self,
        nombre: str,
        nacionalidad: str,
        numero: int,
        edad: int,
        escuderia: Optional['Escuderia'] = None
    ):
        """
        Inicializa un corredor.
        
        Args:
            nombre: Nombre completo
            nacionalidad: País de origen
            numero: Número de carrera único (1-99)
            edad: Edad del corredor (>= 18)
            escuderia: Escudería (opcional)
        
        Raises:
            ValueError: Si los parámetros son inválidos
        """
        from constante import (
            EDAD_MIN_CORREDOR,
            NUMERO_MIN_CORREDOR,
            NUMERO_MAX_CORREDOR
        )
        
        if edad < EDAD_MIN_CORREDOR:
            raise ValueError(
                f"El corredor debe tener al menos {EDAD_MIN_CORREDOR} años"
            )
        if not (NUMERO_MIN_CORREDOR <= numero <= NUMERO_MAX_CORREDOR):
            raise ValueError(
                f"El número debe estar entre {NUMERO_MIN_CORREDOR} y "
                f"{NUMERO_MAX_CORREDOR}"
            )
        
        self._nombre = nombre
        self._nacionalidad = nacionalidad
        self._numero = numero
        self._edad = edad
        self._escuderia = escuderia
        self._puntos_campeonato = 0
        self._victorias = 0
        self._podios = 0

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_nacionalidad(self) -> str:
        return self._nacionalidad

    def get_numero(self) -> int:
        return self._numero

    def get_edad(self) -> int:
        return self._edad

    def get_escuderia(self) -> Optional['Escuderia']:
        return self._escuderia

    def get_puntos_campeonato(self) -> int:
        return self._puntos_campeonato

    def get_victorias(self) -> int:
        return self._victorias

    def get_podios(self) -> int:
        return self._podios

    # Setters
    def set_edad(self, edad: int) -> None:
        """
        Establece la edad del corredor.
        
        Args:
            edad: Nueva edad
        
        Raises:
            ValueError: Si la edad es menor a 18
        """
        from constante import EDAD_MIN_CORREDOR
        if edad < EDAD_MIN_CORREDOR:
            raise ValueError(
                f"El corredor debe tener al menos {EDAD_MIN_CORREDOR} años"
            )
        self._edad = edad

    def set_escuderia(self, escuderia: 'Escuderia') -> None:
        """Asigna el corredor a una escudería."""
        self._escuderia = escuderia

    # Métodos de negocio
    def agregar_puntos(self, puntos: int) -> None:
        """Agrega puntos del campeonato."""
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._puntos_campeonato += puntos

    def registrar_victoria(self) -> None:
        """Registra una victoria (1er lugar)."""
        self._victorias += 1
        self._podios += 1
        self.agregar_puntos(25)  # Puntos por victoria en MotoGP

    def registrar_podio(self, posicion: int) -> None:
        """
        Registra un podio.
        
        Args:
            posicion: Posición final (1, 2, o 3)
        """
        if posicion == 1:
            self.registrar_victoria()
        elif posicion == 2:
            self._podios += 1
            self.agregar_puntos(20)
        elif posicion == 3:
            self._podios += 1
            self.agregar_puntos(16)

    def __str__(self) -> str:
        escuderia_str = (
            self._escuderia.get_nombre() 
            if self._escuderia 
            else "Sin escudería"
        )
        return (
            f"#{self._numero} {self._nombre} ({self._nacionalidad}) - "
            f"{escuderia_str} - Puntos: {self._puntos_campeonato}"
        )


# ==============================================================================
# ARCHIVO 19/75: escuderia.py
# Directorio: python_racing/entidades/escuderias
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/escuderias/escuderia.py
# ==============================================================================


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from python_racing.entidades.escuderias.corredor import Corredor


class Escuderia:
    """
    Representa una escudería de MotoGP.
    
    Attributes:
        nombre: Nombre de la escudería
        pais: País de origen
        presupuesto: Presupuesto disponible
        corredores: Lista de corredores
    """

    def __init__(self, nombre: str, pais: str, presupuesto: float):
        """
        Inicializa una escudería.
        
        Args:
            nombre: Nombre único de la escudería
            pais: País de origen
            presupuesto: Presupuesto inicial (debe ser > 0)
        
        Raises:
            ValueError: Si el presupuesto es inválido
        """
        if presupuesto <= 0:
            raise ValueError("El presupuesto debe ser mayor a 0")
        
        self._nombre = nombre
        self._pais = pais
        self._presupuesto = presupuesto
        self._corredores: list['Corredor'] = []

    # Getters
    def get_nombre(self) -> str:
        return self._nombre

    def get_pais(self) -> str:
        return self._pais

    def get_presupuesto(self) -> float:
        return self._presupuesto

    def get_corredores(self) -> list['Corredor']:
        """Retorna copia de la lista de corredores (defensive copy)."""
        return self._corredores.copy()

    # Setters
    def set_presupuesto(self, presupuesto: float) -> None:
        """
        Establece el presupuesto de la escudería.
        
        Args:
            presupuesto: Nuevo presupuesto
        
        Raises:
            ValueError: Si el presupuesto es negativo
        """
        if presupuesto < 0:
            raise ValueError("El presupuesto no puede ser negativo")
        self._presupuesto = presupuesto

    # Métodos de negocio
    def agregar_corredor(self, corredor: 'Corredor') -> None:
        """Agrega un corredor a la escudería."""
        if corredor not in self._corredores:
            self._corredores.append(corredor)

    def remover_corredor(self, corredor: 'Corredor') -> None:
        """Remueve un corredor de la escudería."""
        if corredor in self._corredores:
            self._corredores.remove(corredor)

    def gastar_presupuesto(self, cantidad: float) -> None:
        """
        Gasta dinero del presupuesto.
        
        Args:
            cantidad: Cantidad a gastar
        
        Raises:
            PresupuestoInsuficienteException: Si no hay fondos suficientes
        """
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        if self._presupuesto < cantidad:
            from python_racing.excepciones.presupuesto_insuficiente_exception import (
                PresupuestoInsuficienteException
            )
            raise PresupuestoInsuficienteException(
                presupuesto_actual=self._presupuesto,
                cantidad_requerida=cantidad
            )
        
        self._presupuesto -= cantidad

    def agregar_presupuesto(self, cantidad: float) -> None:
        """Agrega fondos al presupuesto."""
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        self._presupuesto += cantidad

    def __str__(self) -> str:
        return (
            f"{self._nombre} ({self._pais}) - "
            f"Presupuesto: ${self._presupuesto:,.2f} - "
            f"Corredores: {len(self._corredores)}"
        )


################################################################################
# DIRECTORIO: python_racing/entidades/mantenimiento
################################################################################

# ==============================================================================
# ARCHIVO 20/75: __init__.py
# Directorio: python_racing/entidades/mantenimiento
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/mantenimiento/__init__.py
# ==============================================================================

"""
Entidades de mantenimiento
"""


# ==============================================================================
# ARCHIVO 21/75: fallo_mecanico.py
# Directorio: python_racing/entidades/mantenimiento
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/mantenimiento/fallo_mecanico.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_racing/entidades/motos
################################################################################

# ==============================================================================
# ARCHIVO 22/75: __init__.py
# Directorio: python_racing/entidades/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/__init__.py
# ==============================================================================

"""
Entidades de motos
"""


# ==============================================================================
# ARCHIVO 23/75: moto.py
# Directorio: python_racing/entidades/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/moto.py
# ==============================================================================


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

# ==============================================================================
# ARCHIVO 24/75: motor.py
# Directorio: python_racing/entidades/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/motor.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 25/75: neumatico.py
# Directorio: python_racing/entidades/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/neumatico.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 26/75: tipo_neumatico.py
# Directorio: python_racing/entidades/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/motos/tipo_neumatico.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_racing/entidades/personal
################################################################################

# ==============================================================================
# ARCHIVO 27/75: __init__.py
# Directorio: python_racing/entidades/personal
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/personal/__init__.py
# ==============================================================================

"""
Entidades de personal técnico
"""


# ==============================================================================
# ARCHIVO 28/75: mecanico.py
# Directorio: python_racing/entidades/personal
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/entidades/personal/mecanico.py
# ==============================================================================

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



################################################################################
# DIRECTORIO: python_racing/excepciones
################################################################################

# ==============================================================================
# ARCHIVO 29/75: __init__.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/__init__.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 30/75: combustible_excedido_exception.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/combustible_excedido_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 31/75: combustible_insuficiente_exception.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/combustible_insuficiente_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 32/75: fallo_grave_exception.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/fallo_grave_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 33/75: mensajes_exception.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/mensajes_exception.py
# ==============================================================================


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

# ==============================================================================
# ARCHIVO 34/75: presupuesto_insuficiente_exception.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/presupuesto_insuficiente_exception.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 35/75: racing_exception.py
# Directorio: python_racing/excepciones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/excepciones/racing_exception.py
# ==============================================================================



class RacingException(Exception):
    def __init__(self, mensaje: str):
        super().__init__(mensaje)
        self.mensaje = mensaje

    def __str__(self):
        return f"[PythonRacing] {self.mensaje}"


################################################################################
# DIRECTORIO: python_racing/patrones
################################################################################

# ==============================================================================
# ARCHIVO 36/75: __init__.py
# Directorio: python_racing/patrones
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/__init__.py
# ==============================================================================


from python_racing.patrones.singleton.singleton import singleton
from python_racing.patrones.factory.moto_factory import MotoFactory

__all__ = [
    'singleton',
    'MotoFactory'
]


################################################################################
# DIRECTORIO: python_racing/patrones/factory
################################################################################

# ==============================================================================
# ARCHIVO 37/75: __init__.py
# Directorio: python_racing/patrones/factory
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/factory/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 38/75: moto_factory.py
# Directorio: python_racing/patrones/factory
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/factory/moto_factory.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_racing/patrones/observer
################################################################################

# ==============================================================================
# ARCHIVO 39/75: __init__.py
# Directorio: python_racing/patrones/observer
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/observer/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 40/75: observable.py
# Directorio: python_racing/patrones/observer
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/observer/observable.py
# ==============================================================================


from typing import Generic, TypeVar, List, TYPE_CHECKING
from abc import ABC

if TYPE_CHECKING:
    from python_racing.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    def __init__(self):
        # ✅ Usar string literal para el tipo
        self._observadores: List['Observer[T]'] = []

    def agregar_observador(self, observador: 'Observer[T]') -> None:
        """Agrega un observador a la lista."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: 'Observer[T]') -> None:
        """Elimina un observador de la lista."""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores."""
        for observador in self._observadores:
            observador.actualizar(evento)

# ==============================================================================
# ARCHIVO 41/75: observer.py
# Directorio: python_racing/patrones/observer
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/observer/observer.py
# ==============================================================================


from typing import Generic, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')


class Observer(Generic[T], ABC):
    @abstractmethod
    def actualizar(self, evento: T) -> None:
        pass


################################################################################
# DIRECTORIO: python_racing/patrones/singleton
################################################################################

# ==============================================================================
# ARCHIVO 42/75: __init__.py
# Directorio: python_racing/patrones/singleton
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/singleton/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 43/75: singleton.py
# Directorio: python_racing/patrones/singleton
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/singleton/singleton.py
# ==============================================================================


from threading import Lock
from typing import Any, Callable


def singleton(cls: type) -> Callable:
    instances = {}
    lock = Lock()
    
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        """Retorna la instancia única (thread-safe)."""
        if cls not in instances:
            with lock:  # Thread-safe
                if cls not in instances:  # Double-checked locking
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance


################################################################################
# DIRECTORIO: python_racing/patrones/strategy
################################################################################

# ==============================================================================
# ARCHIVO 44/75: __init__.py
# Directorio: python_racing/patrones/strategy
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 45/75: neumatico_strategy.py
# Directorio: python_racing/patrones/strategy
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/neumatico_strategy.py
# ==============================================================================


from abc import ABC, abstractmethod
from python_racing.entidades.circuitos.circuito import CondicionClimatica


class NeumaticoStrategy(ABC):
    @abstractmethod
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        pass

    @abstractmethod
    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        pass


################################################################################
# DIRECTORIO: python_racing/patrones/strategy/impl
################################################################################

# ==============================================================================
# ARCHIVO 46/75: __init__.py
# Directorio: python_racing/patrones/strategy/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/__init__.py
# ==============================================================================



# ==============================================================================
# ARCHIVO 47/75: intermedio_strategy.py
# Directorio: python_racing/patrones/strategy/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/intermedio_strategy.py
# ==============================================================================

from python_racing.patrones.strategy.neumatico_strategy import NeumaticoStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica
from constante import DESGASTE_INTERMEDIO_SECO, DESGASTE_INTERMEDIO_LLUVIA


class IntermedioStrategy(NeumaticoStrategy):
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        """Calcula desgaste según condición."""
        if condicion == CondicionClimatica.SECO:
            return DESGASTE_INTERMEDIO_SECO * longitud_km
        elif condicion == CondicionClimatica.HUMEDO:
            return DESGASTE_INTERMEDIO_LLUVIA * longitud_km * 0.8  # Óptimo
        else:  # LLUVIA
            return DESGASTE_INTERMEDIO_LLUVIA * longitud_km

    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        """Intermedios son versátiles."""
        return True  # Compatible con todas las condiciones

# ==============================================================================
# ARCHIVO 48/75: lluvia_strategy.py
# Directorio: python_racing/patrones/strategy/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/lluvia_strategy.py
# ==============================================================================

from python_racing.patrones.strategy.neumatico_strategy import NeumaticoStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica
from constante import DESGASTE_LLUVIA_SECO, DESGASTE_LLUVIA_LLUVIA


class LluviaStrategy(NeumaticoStrategy):
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        """Calcula desgaste según condición."""
        if condicion == CondicionClimatica.SECO:
            return DESGASTE_LLUVIA_SECO * longitud_km  # Desgaste rápido
        elif condicion == CondicionClimatica.HUMEDO:
            return DESGASTE_LLUVIA_LLUVIA * longitud_km * 1.5
        else:  # LLUVIA
            return DESGASTE_LLUVIA_LLUVIA * longitud_km  # Óptimo

    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        """Lluvia es mejor en mojado."""
        return condicion in [CondicionClimatica.HUMEDO, CondicionClimatica.LLUVIA]

# ==============================================================================
# ARCHIVO 49/75: slick_strategy.py
# Directorio: python_racing/patrones/strategy/impl
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/strategy/impl/slick_strategy.py
# ==============================================================================


from python_racing.patrones.strategy.neumatico_strategy import NeumaticoStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica
from constante import DESGASTE_SLICK_SECO, DESGASTE_SLICK_LLUVIA


class SlickStrategy(NeumaticoStrategy):
    def calcular_desgaste(
        self,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> float:
        """Calcula desgaste según condición."""
        if condicion == CondicionClimatica.SECO:
            return DESGASTE_SLICK_SECO * longitud_km
        elif condicion == CondicionClimatica.HUMEDO:
            return DESGASTE_SLICK_SECO * longitud_km * 2  # Doble desgaste
        else:  # LLUVIA
            return DESGASTE_SLICK_LLUVIA * longitud_km  # Desgaste extremo

    def es_compatible(self, condicion: CondicionClimatica) -> bool:
        """Slick solo es seguro en SECO."""
        return condicion == CondicionClimatica.SECO


################################################################################
# DIRECTORIO: python_racing/servicios
################################################################################

# ==============================================================================
# ARCHIVO 50/75: __init__.py
# Directorio: python_racing/servicios
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/__init__.py
# ==============================================================================

from python_racing.servicios.escuderias.escuderia_service import EscuderiaService
from python_racing.servicios.escuderias.corredor_service import CorredorService
from python_racing.servicios.motos.moto_service import MotoService
from python_racing.servicios.motos.motor_service import MotorService
from python_racing.servicios.motos.neumatico_service import NeumaticoService
from python_racing.servicios.circuitos.circuito_service import CircuitoService
from python_racing.servicios.circuitos.carrera_service import CarreraService
from python_racing.servicios.negocio.campeonato_service import CampeonatoService

__all__ = [
    'EscuderiaService',
    'CorredorService',
    'MotoService',
    'MotorService',
    'NeumaticoService',
    'CircuitoService',
    'CarreraService',
    'CampeonatoService'
]


################################################################################
# DIRECTORIO: python_racing/servicios/circuitos
################################################################################

# ==============================================================================
# ARCHIVO 51/75: __init__.py
# Directorio: python_racing/servicios/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/circuitos/__init__.py
# ==============================================================================

"""
Servicios de circuitos y carreras
"""


# ==============================================================================
# ARCHIVO 52/75: carrera_service.py
# Directorio: python_racing/servicios/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/circuitos/carrera_service.py
# ==============================================================================

import random
from datetime import date
from python_racing.entidades.circuitos.circuito import Circuito
from python_racing.entidades.circuitos.carrera import Carrera, ResultadoCarrera
from python_racing.entidades.circuitos.vuelta import Vuelta
from python_racing.entidades.escuderias.corredor import Corredor
from python_racing.servicios.motos.moto_service import MotoService
from constante import (
    TIEMPO_VUELTA_BASE,
    FACTOR_NEUMATICO_NUEVO,
    FACTOR_NEUMATICO_GASTADO,
    FACTOR_COMBUSTIBLE_BAJO,
    PROB_FALLO_MOTOR
)


class CarreraService:
    def __init__(self):
        self._moto_service = MotoService()

    def simular_carrera(
        self,
        circuito: Circuito,
        corredores: list[Corredor],
        vueltas: int
    ) -> Carrera:
        carrera = Carrera(circuito, date.today(), vueltas)
        
        # Registrar corredores
        for corredor in corredores:
            carrera.agregar_corredor(corredor)
        
        # Simular vueltas para cada corredor
        resultados = []
        
        for corredor in corredores:
            tiempo_total, completadas, abandono = self._simular_participacion(
                corredor,
                circuito,
                vueltas
            )
            
            resultado = ResultadoCarrera(
                corredor=corredor,
                posicion=0,  # Se ordenará después
                tiempo_total=tiempo_total,
                vueltas_completadas=completadas,
                abandono=abandono
            )
            resultados.append(resultado)
        
        # Ordenar por tiempo (abandonos al final)
        resultados.sort(
            key=lambda r: (r.es_abandono(), r.get_tiempo_total())
        )
        
        # Asignar posiciones
        for idx, resultado in enumerate(resultados, 1):
            resultado._posicion = idx  # Hack temporal
            carrera.registrar_resultado(resultado)
        
        carrera.finalizar_carrera()
        return carrera

    def _simular_participacion(
        self,
        corredor: Corredor,
        circuito: Circuito,
        vueltas: int
    ) -> tuple[float, int, bool]:
        tiempo_total = 0.0
        vueltas_completadas = 0
        
        for vuelta_num in range(1, vueltas + 1):
            # Simular fallo mecánico aleatorio
            if random.random() < PROB_FALLO_MOTOR:
                # Abandono por fallo
                return tiempo_total, vueltas_completadas, True
            
            # Calcular tiempo de vuelta
            tiempo_vuelta = self._calcular_tiempo_vuelta(
                corredor,
                circuito
            )
            
            tiempo_total += tiempo_vuelta
            vueltas_completadas += 1
        
        return tiempo_total, vueltas_completadas, False

    def _calcular_tiempo_vuelta(
        self,
        corredor: Corredor,
        circuito: Circuito
    ) -> float:
        """Calcula el tiempo de una vuelta."""
        # Tiempo base
        tiempo = TIEMPO_VUELTA_BASE
        
        # Factor de longitud del circuito
        tiempo *= (circuito.get_longitud_km() / 5.0)
        
        # Variación aleatoria ±2 segundos
        tiempo += random.uniform(-2, 2)
        
        return max(tiempo, 60)  # Mínimo 60 segundos

# ==============================================================================
# ARCHIVO 53/75: circuito_service.py
# Directorio: python_racing/servicios/circuitos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/circuitos/circuito_service.py
# ==============================================================================


from python_racing.entidades.circuitos.circuito import Circuito, TipoSuperficie


class CircuitoService:

    def __init__(self):
        self._circuitos: dict[str, Circuito] = {}

    def registrar_circuito(
        self,
        nombre: str,
        longitud_km: float,
        pais: str,
        superficie: TipoSuperficie
    ) -> Circuito:
        if nombre in self._circuitos:
            raise ValueError(f"Ya existe un circuito llamado '{nombre}'")
        
        circuito = Circuito(nombre, longitud_km, pais, superficie)
        self._circuitos[nombre] = circuito
        return circuito

    def buscar_circuito(self, nombre: str) -> Circuito:
        """Busca un circuito por nombre."""
        return self._circuitos.get(nombre)

    def listar_circuitos(self) -> list[Circuito]:
        """Retorna lista de todos los circuitos."""
        return list(self._circuitos.values())

    def listar_circuitos_por_pais(self, pais: str) -> list[Circuito]:
        """Retorna circuitos de un país específico."""
        return [
            c for c in self._circuitos.values()
            if c.get_pais().lower() == pais.lower()
        ]


################################################################################
# DIRECTORIO: python_racing/servicios/escuderias
################################################################################

# ==============================================================================
# ARCHIVO 54/75: __init__.py
# Directorio: python_racing/servicios/escuderias
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias/__init__.py
# ==============================================================================

"""
Servicios de gestión de escuderías
"""


# ==============================================================================
# ARCHIVO 55/75: corredor_service.py
# Directorio: python_racing/servicios/escuderias
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias/corredor_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 56/75: escuderia_service.py
# Directorio: python_racing/servicios/escuderias
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/escuderias/escuderia_service.py
# ==============================================================================

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


################################################################################
# DIRECTORIO: python_racing/servicios/motos
################################################################################

# ==============================================================================
# ARCHIVO 57/75: __init__.py
# Directorio: python_racing/servicios/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/__init__.py
# ==============================================================================

"""
Servicios de gestión de motos
"""


# ==============================================================================
# ARCHIVO 58/75: moto_service.py
# Directorio: python_racing/servicios/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/moto_service.py
# ==============================================================================

from typing import Optional
from python_racing.entidades.motos.moto import Moto
from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico
from python_racing.patrones.strategy.impl.slick_strategy import SlickStrategy
from python_racing.patrones.strategy.impl.intermedio_strategy import IntermedioStrategy
from python_racing.patrones.strategy.impl.lluvia_strategy import LluviaStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica


class MotoService:
    def __init__(self):
        self._motos: dict[str, Moto] = {}
        self._estrategias = {
            TipoNeumatico.SLICK: SlickStrategy(),
            TipoNeumatico.INTERMEDIO: IntermedioStrategy(),
            TipoNeumatico.LLUVIA: LluviaStrategy()
        }

    def registrar_moto(self, moto: Moto) -> None:
        """Registra una moto en el sistema."""
        identificador = f"{moto.get_marca()}_{moto.get_modelo()}"
        self._motos[identificador] = moto

    def asignar_neumaticos(
        self,
        moto: Moto,
        tipo: TipoNeumatico
    ) -> tuple[Neumatico, Neumatico]:
        delantero = Neumatico(tipo)
        trasero = Neumatico(tipo)
        
        moto.set_neumatico_delantero(delantero)
        moto.set_neumatico_trasero(trasero)
        
        return delantero, trasero

    def aplicar_desgaste_neumaticos(
        self,
        moto: Moto,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> None:
        if not moto.tiene_neumaticos_instalados():
            return
        
        # Obtener tipo de neumático
        tipo = moto.get_neumatico_delantero().get_tipo()
        estrategia = self._estrategias[tipo]
        
        # Calcular desgaste
        desgaste = estrategia.calcular_desgaste(condicion, longitud_km)
        
        # Aplicar a ambos neumáticos
        moto.get_neumatico_delantero().aplicar_desgaste(desgaste)
        moto.get_neumatico_trasero().aplicar_desgaste(desgaste)
        
        # Incrementar contador de vueltas
        moto.get_neumatico_delantero().incrementar_vueltas()
        moto.get_neumatico_trasero().incrementar_vueltas()

    def verificar_compatibilidad_neumaticos(
        self,
        moto: Moto,
        condicion: CondicionClimatica
    ) -> bool:
        if not moto.tiene_neumaticos_instalados():
            return False
        
        tipo = moto.get_neumatico_delantero().get_tipo()
        estrategia = self._estrategias[tipo]
        
        return estrategia.es_compatible(condicion)

# ==============================================================================
# ARCHIVO 59/75: moto_service_registry.py
# Directorio: python_racing/servicios/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/moto_service_registry.py
# ==============================================================================

from python_racing.patrones.singleton.singleton import singleton
from python_racing.entidades.motos.moto import Moto


@singleton
class MotoServiceRegistry:
    def __init__(self):
        """Inicializa el registro con handlers por marca."""
        # Registry pattern: diccionario de handlers
        self._mostrar_datos_handlers = {
            "Ducati": self._mostrar_datos_ducati,
            "Yamaha": self._mostrar_datos_yamaha,
            "KTM": self._mostrar_datos_ktm,
            "Honda": self._mostrar_datos_honda
        }
        
        self._verificar_estado_handlers = {
            "Ducati": self._verificar_estado_ducati,
            "Yamaha": self._verificar_estado_yamaha,
            "KTM": self._verificar_estado_ktm,
            "Honda": self._verificar_estado_honda
        }

    def mostrar_datos(self, moto: Moto) -> None:
        marca = moto.get_marca()
        
        if marca not in self._mostrar_datos_handlers:
            raise ValueError(f"Marca no registrada: {marca}")
        
        # Dispatch automático al handler correcto (NO isinstance)
        self._mostrar_datos_handlers[marca](moto)

    def verificar_estado(self, moto: Moto) -> dict:
        """
        Verifica el estado de una moto según su marca.
        
        Args:
            moto: Moto a verificar
        
        Returns:
            Dict con estado y recomendaciones
        """
        marca = moto.get_marca()
        
        if marca not in self._verificar_estado_handlers:
            raise ValueError(f"Marca no registrada: {marca}")
        
        return self._verificar_estado_handlers[marca](moto)

    def _mostrar_datos_ducati(self, moto: Moto) -> None:
        """Handler específico para Ducati."""
        print(f"\n{'=' * 60}")
        print(f"  DUCATI DESMOSEDICI GP25")
        print(f"{'=' * 60}")
        print(f"  Marca:           {moto.get_marca()}")
        print(f"  Modelo:          {moto.get_modelo()}")
        print(f"  Potencia:        {moto.get_potencia_hp()} HP")
        print(f"  Motor:           {moto.get_motor().get_tipo().value}")
        print(f"  Cilindrada:      {moto.get_motor().get_cilindrada()} cc")
        print(f"  Rev. Máximas:    {moto.get_motor().get_revoluciones_max()} RPM")
        print(f"  Combustible:     {moto.get_combustible_actual():.1f}L / "
              f"{moto.get_combustible_max()}L ({moto.get_porcentaje_combustible():.1f}%)")
        print(f"  Peso:            {moto.get_peso_kg()} kg")
        print(f"  Peso total:      {moto.calcular_peso_total():.1f} kg (con combustible)")
        print(f"  Km recorridos:   {moto.get_kilometros_recorridos():.1f} km")
        
        # Corredor asignado
        if moto.get_corredor():
            corredor = moto.get_corredor()
            print(f"  Corredor:        #{corredor.get_numero()} {corredor.get_nombre()}")
        else:
            print(f"  Corredor:        Sin asignar")
        
        # Neumáticos
        if moto.tiene_neumaticos_instalados():
            delantero = moto.get_neumatico_delantero()
            trasero = moto.get_neumatico_trasero()
            print(f"  Neumáticos:      {delantero.get_tipo().value}")
            print(f"    - Delantero:   {delantero.get_estado().value} "
                  f"({delantero.get_desgaste():.1f}%)")
            print(f"    - Trasero:     {trasero.get_estado().value} "
                  f"({trasero.get_desgaste():.1f}%)")
        else:
            print(f"  Neumáticos:      No instalados")
        
        print(f"{'=' * 60}")

    def _mostrar_datos_yamaha(self, moto: Moto) -> None:
        """Handler específico para Yamaha."""
        print(f"\n{'=' * 60}")
        print(f"  YAMAHA YZR-M1")
        print(f"{'=' * 60}")
        print(f"  Marca:           {moto.get_marca()}")
        print(f"  Modelo:          {moto.get_modelo()}")
        print(f"  Potencia:        {moto.get_potencia_hp()} HP")
        print(f"  Motor:           {moto.get_motor().get_tipo().value}")
        print(f"  Combustible:     {moto.get_combustible_actual():.1f}L / "
              f"{moto.get_combustible_max()}L")
        
        if moto.get_corredor():
            print(f"  Corredor:        #{moto.get_corredor().get_numero()} "
                  f"{moto.get_corredor().get_nombre()}")
        
        print(f"{'=' * 60}")

    def _mostrar_datos_ktm(self, moto: Moto) -> None:
        """Handler específico para KTM."""
        print(f"\n{'=' * 60}")
        print(f"  KTM RC16")
        print(f"{'=' * 60}")
        print(f"  Marca:           {moto.get_marca()}")
        print(f"  Modelo:          {moto.get_modelo()}")
        print(f"  Potencia:        {moto.get_potencia_hp()} HP")
        print(f"  Motor:           {moto.get_motor().get_tipo().value}")
        print(f"  Combustible:     {moto.get_combustible_actual():.1f}L / "
              f"{moto.get_combustible_max()}L")
        
        if moto.get_corredor():
            print(f"  Corredor:        #{moto.get_corredor().get_numero()} "
                  f"{moto.get_corredor().get_nombre()}")
        
        print(f"{'=' * 60}")

    def _mostrar_datos_honda(self, moto: Moto) -> None:
        """Handler específico para Honda."""
        print(f"\n{'=' * 60}")
        print(f"  HONDA RC213V")
        print(f"{'=' * 60}")
        print(f"  Marca:           {moto.get_marca()}")
        print(f"  Modelo:          {moto.get_modelo()}")
        print(f"  Potencia:        {moto.get_potencia_hp()} HP")
        print(f"  Motor:           {moto.get_motor().get_tipo().value}")
        print(f"  Combustible:     {moto.get_combustible_actual():.1f}L / "
              f"{moto.get_combustible_max()}L")
        
        if moto.get_corredor():
            print(f"  Corredor:        #{moto.get_corredor().get_numero()} "
                  f"{moto.get_corredor().get_nombre()}")
        
        print(f"{'=' * 60}")

    def _verificar_estado_ducati(self, moto: Moto) -> dict:
        """Verifica estado específico de Ducati."""
        alertas = []
        estado = "OK"
        
        # Verificar combustible
        if moto.combustible_bajo():
            alertas.append("⚠️ Combustible bajo")
            estado = "ALERTA"
        
        # Verificar neumáticos
        if moto.neumaticos_requieren_cambio():
            alertas.append("⚠️ Neumáticos requieren cambio")
            estado = "ALERTA"
        
        # Verificar motor
        if moto.get_motor().esta_sobrecalentado():
            alertas.append("⚠️ Motor sobrecalentado")
            estado = "CRITICO"
        
        # Ducati específico: verificar RPM altas
        if moto.get_motor().get_revoluciones_max() > 17500:
            alertas.append("✓ Motor de alto rendimiento (>17500 RPM)")
        
        return {
            'marca': 'Ducati',
            'estado': estado,
            'alertas': alertas if alertas else ['✓ Todo OK'],
            'requiere_boxes': estado == "CRITICO"
        }

    def _verificar_estado_yamaha(self, moto: Moto) -> dict:
        """Verifica estado específico de Yamaha."""
        alertas = []
        estado = "OK"
        
        if moto.combustible_bajo():
            alertas.append("⚠️ Combustible bajo")
            estado = "ALERTA"
        
        if moto.neumaticos_requieren_cambio():
            alertas.append("⚠️ Neumáticos gastados")
            estado = "ALERTA"
        
        # Yamaha específico: motor lineal 4 cilindros
        if moto.get_motor().get_tipo().value == "Lineal 4 cilindros":
            alertas.append("✓ Motor lineal 4 - equilibrio perfecto")
        
        return {
            'marca': 'Yamaha',
            'estado': estado,
            'alertas': alertas if alertas else ['✓ Todo OK'],
            'requiere_boxes': estado == "CRITICO"
        }

    def _verificar_estado_ktm(self, moto: Moto) -> dict:
        """Verifica estado específico de KTM."""
        alertas = []
        estado = "OK"
        
        if moto.combustible_bajo():
            alertas.append("⚠️ Combustible bajo")
            estado = "ALERTA"
        
        if moto.neumaticos_requieren_cambio():
            alertas.append("⚠️ Neumáticos gastados")
            estado = "ALERTA"
        
        return {
            'marca': 'KTM',
            'estado': estado,
            'alertas': alertas if alertas else ['✓ Todo OK'],
            'requiere_boxes': estado == "CRITICO"
        }

    def _verificar_estado_honda(self, moto: Moto) -> dict:
        """Verifica estado específico de Honda."""
        alertas = []
        estado = "OK"
        
        if moto.combustible_bajo():
            alertas.append("⚠️ Combustible bajo")
            estado = "ALERTA"
        
        if moto.neumaticos_requieren_cambio():
            alertas.append("⚠️ Neumáticos gastados")
            estado = "ALERTA"
        
        return {
            'marca': 'Honda',
            'estado': estado,
            'alertas': alertas if alertas else ['✓ Todo OK'],
            'requiere_boxes': estado == "CRITICO"
        }

    def listar_marcas_registradas(self) -> list[str]:
        return list(self._mostrar_datos_handlers.keys())

    def esta_marca_registrada(self, marca: str) -> bool:
        return marca in self._mostrar_datos_handlers

# ==============================================================================
# ARCHIVO 60/75: motor_service.py
# Directorio: python_racing/servicios/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/motor_service.py
# ==============================================================================

from python_racing.entidades.motos.motor import Motor
from constante import TEMP_MOTOR_ALERTA, TEMP_MOTOR_CRITICA


class MotorService:

    def verificar_temperatura(self, motor: Motor) -> dict:
        temp = motor.get_temperatura()
        
        if temp >= TEMP_MOTOR_CRITICA:
            return {
                'estado': 'CRITICO',
                'mensaje': f'⚠️ TEMPERATURA CRÍTICA: {temp:.1f}°C - DETENER MOTOR',
                'requiere_accion': True
            }
        elif temp >= TEMP_MOTOR_ALERTA:
            return {
                'estado': 'ALERTA',
                'mensaje': f'⚠️ Temperatura alta: {temp:.1f}°C - Reducir revoluciones',
                'requiere_accion': True
            }
        else:
            return {
                'estado': 'OK',
                'mensaje': f'✓ Temperatura normal: {temp:.1f}°C',
                'requiere_accion': False
            }

    def simular_calentamiento(self, motor: Motor, minutos: float) -> None:
        # Incrementar temperatura gradualmente
        temp_actual = motor.get_temperatura()
        incremento = minutos * 2  # 2°C por minuto
        
        nueva_temp = min(temp_actual + incremento, TEMP_MOTOR_CRITICA)
        motor.set_temperatura(nueva_temp)
        motor.incrementar_horas_uso(minutos / 60)

    def enfriar_motor(self, motor: Motor, minutos: float) -> None:
        temp_actual = motor.get_temperatura()
        decremento = minutos * 3  # 3°C por minuto (enfría más rápido)
        
        nueva_temp = max(temp_actual - decremento, 40.0)  # Mín 40°C
        motor.set_temperatura(nueva_temp)

# ==============================================================================
# ARCHIVO 61/75: neumatico_service.py
# Directorio: python_racing/servicios/motos
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/neumatico_service.py
# ==============================================================================

from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico


class NeumaticoService:
    def crear_juego_neumaticos(self, tipo: TipoNeumatico) -> tuple[Neumatico, Neumatico]:
        delantero = Neumatico(tipo)
        trasero = Neumatico(tipo)
        return delantero, trasero

    def verificar_estado_neumatico(self, neumatico: Neumatico) -> dict:
        desgaste = neumatico.get_desgaste()
        
        if desgaste >= 80:
            return {
                'estado': 'CRITICO',
                'mensaje': f'⚠️ Neumático MUY gastado ({desgaste:.1f}%) - CAMBIAR YA',
                'requiere_cambio': True
            }
        elif desgaste >= 60:
            return {
                'estado': 'ALERTA',
                'mensaje': f'⚠️ Neumático gastado ({desgaste:.1f}%) - Considerar cambio',
                'requiere_cambio': False
            }
        elif desgaste >= 40:
            return {
                'estado': 'USADO',
                'mensaje': f'Neumático usado ({desgaste:.1f}%) - Rendimiento óptimo',
                'requiere_cambio': False
            }
        else:
            return {
                'estado': 'NUEVO',
                'mensaje': f'✓ Neumático nuevo ({desgaste:.1f}%)',
                'requiere_cambio': False
            }

    def recomendar_tipo_neumatico(self, condicion: str) -> TipoNeumatico:
        recomendaciones = {
            'seco': TipoNeumatico.SLICK,
            'humedo': TipoNeumatico.INTERMEDIO,
            'lluvia': TipoNeumatico.LLUVIA
        }
        
        return recomendaciones.get(
            condicion.lower(),
            TipoNeumatico.INTERMEDIO  # Default seguro
        )


################################################################################
# DIRECTORIO: python_racing/servicios/negocio
################################################################################

# ==============================================================================
# ARCHIVO 62/75: __init__.py
# Directorio: python_racing/servicios/negocio
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio/__init__.py
# ==============================================================================

"""
Servicios de alto nivel
"""


# ==============================================================================
# ARCHIVO 63/75: campeonato_service.py
# Directorio: python_racing/servicios/negocio
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio/campeonato_service.py
# ==============================================================================

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

# ==============================================================================
# ARCHIVO 64/75: paquete.py
# Directorio: python_racing/servicios/negocio
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/negocio/paquete.py
# ==============================================================================




################################################################################
# DIRECTORIO: python_racing/telemetria
################################################################################

# ==============================================================================
# ARCHIVO 65/75: __init__.py
# Directorio: python_racing/telemetria
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/__init__.py
# ==============================================================================

from python_racing.telemetria.sensores.temperatura_motor_sensor import TemperaturaMotorSensor
from python_racing.telemetria.sensores.combustible_sensor import CombustibleSensor
from python_racing.telemetria.sensores.velocidad_sensor import VelocidadSensor
from python_racing.telemetria.control.control_boxes_task import ControlBoxesTask

__all__ = [
    'TemperaturaMotorSensor',
    'CombustibleSensor',
    'VelocidadSensor',
    'ControlBoxesTask'
]


################################################################################
# DIRECTORIO: python_racing/telemetria/control
################################################################################

# ==============================================================================
# ARCHIVO 66/75: __init__.py
# Directorio: python_racing/telemetria/control
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/control/__init__.py
# ==============================================================================

"""
Controladores de telemetría
"""


# ==============================================================================
# ARCHIVO 67/75: control_boxes_task.py
# Directorio: python_racing/telemetria/control
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/control/control_boxes_task.py
# ==============================================================================

import threading
import time
from constante import (
    COMBUSTIBLE_ALERTA,
    COMBUSTIBLE_CRITICO,
    TEMP_MOTOR_ALERTA,
    TEMP_MOTOR_CRITICA,
    INTERVALO_CONTROL_BOXES
)
from python_racing.patrones.observer.observer import Observer


class ControlBoxesTask(Observer):
    def __init__(self, moto):
        self._moto = moto
        self._temperatura_actual = None
        self._combustible_actual = None
        self._velocidad_actual = None
        self._alerta_activa = False
        self._running = True
        
        # Thread para monitoreo periódico
        self._thread = threading.Thread(
            target=self._monitorear,
            daemon=True,
            name="ControlBoxes"
        )

    def actualizar(self, evento: dict) -> None:
        try:
            if not isinstance(evento, dict):
                print(f"[WARN] Evento inválido (tipo {type(evento).__name__}): {evento}")
                return
            
            tipo = evento.get('tipo')
            valor = evento.get('valor')
            
            if tipo == 'temperatura':
                self._temperatura_actual = float(valor)
            elif tipo == 'combustible':
                self._combustible_actual = float(valor)
            elif tipo == 'velocidad':
                self._velocidad_actual = float(valor)
            else:
                print(f"[WARN] Tipo de evento desconocido: {tipo}")
                
        except (ValueError, TypeError, KeyError) as e:
            print(f"[ERROR] Error procesando evento: {evento} - {e}")

    def iniciar(self) -> None:
        """Inicia el monitoreo en background."""
        self._thread.start()

    def start(self) -> None:
        """Alias para iniciar() (compatibilidad con threading)."""
        self.iniciar()

    def detener(self) -> None:
        """Detiene el monitoreo."""
        self._running = False

    def join(self, timeout=None) -> None:
        if self._thread.is_alive():
            self._thread.join(timeout=timeout)

    def _monitorear(self) -> None:
        while self._running:
            try:
                self._verificar_alertas()
                time.sleep(INTERVALO_CONTROL_BOXES)
            except Exception as e:
                print(f"[ERROR] En monitoreo: {e}")

    def _verificar_alertas(self) -> None:
        """Verifica si hay condiciones que requieren atención."""
        alertas = []
        
        # Verificar temperatura (solo si tenemos datos)
        if self._temperatura_actual is not None:
            if self._temperatura_actual >= TEMP_MOTOR_CRITICA:
                alertas.append(f"🔥 TEMPERATURA CRÍTICA: {self._temperatura_actual:.1f}°C")
            elif self._temperatura_actual >= TEMP_MOTOR_ALERTA:
                alertas.append(f"⚠️  Temperatura alta: {self._temperatura_actual:.1f}°C")
        
        # Verificar combustible (solo si tenemos datos)
        if self._combustible_actual is not None:
            if self._combustible_actual <= COMBUSTIBLE_CRITICO:
                alertas.append(f"⛽ COMBUSTIBLE CRÍTICO: {self._combustible_actual:.1f}%")
            elif self._combustible_actual <= COMBUSTIBLE_ALERTA:
                alertas.append(f"⚠️  Combustible bajo: {self._combustible_actual:.1f}%")
        
        # Si hay alertas nuevas, mostrarlas
        if alertas and not self._alerta_activa:
            self._alerta_activa = True
            print("\n" + "="*60)
            print("🚨 ALERTA DE BOXES 🚨")
            for alerta in alertas:
                print(f"   {alerta}")
            print("="*60 + "\n")
        elif not alertas:
            self._alerta_activa = False

    def obtener_estado(self) -> str:
        # Usar valores por defecto si aún no hay datos
        temp = self._temperatura_actual if self._temperatura_actual is not None else 0.0
        comb = self._combustible_actual if self._combustible_actual is not None else 0.0
        vel = self._velocidad_actual if self._velocidad_actual is not None else 0.0
        
        # Determinar estado general
        if temp >= TEMP_MOTOR_CRITICA or comb <= COMBUSTIBLE_CRITICO:
            estado = "🔴 CRÍTICO"
        elif temp >= TEMP_MOTOR_ALERTA or comb <= COMBUSTIBLE_ALERTA:
            estado = "🟡 ALERTA"
        else:
            estado = "🟢 NORMAL"
        
        return (
            f"{estado} | "
            f"Temp: {temp:.1f}°C | "
            f"Comb: {comb:.1f}% | "
            f"Vel: {vel:.1f} km/h"
        )

    def obtener_temperatura(self) -> float:
        """Temperatura actual del motor."""
        return self._temperatura_actual if self._temperatura_actual is not None else 0.0

    def obtener_combustible(self) -> float:
        """Nivel de combustible actual."""
        return self._combustible_actual if self._combustible_actual is not None else 0.0

    def obtener_velocidad(self) -> float:
        """Velocidad actual."""
        return self._velocidad_actual if self._velocidad_actual is not None else 0.0

    def __str__(self) -> str:
        return f"Control de Boxes - {self._moto.get_marca()} #{self._moto.get_corredor().get_numero()}"
    
    def requiere_entrada_boxes(self) -> bool:
        return self._alerta_activa



################################################################################
# DIRECTORIO: python_racing/telemetria/sensores
################################################################################

# ==============================================================================
# ARCHIVO 68/75: __init__.py
# Directorio: python_racing/telemetria/sensores
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/__init__.py
# ==============================================================================

"""
Sensores de telemetría
"""


# ==============================================================================
# ARCHIVO 69/75: combustible_sensor.py
# Directorio: python_racing/telemetria/sensores
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/combustible_sensor.py
# ==============================================================================

import threading
import time
from python_racing.patrones.observer.observable import Observable
from python_racing.entidades.motos.moto import Moto
from constante import INTERVALO_COMBUSTIBLE


class CombustibleSensor(threading.Thread, Observable[dict]):
    """Sensor de nivel de combustible con notificaciones estructuradas."""
    
    def __init__(self, moto: Moto):
        threading.Thread.__init__(self, daemon=True, name="CombustibleSensor")
        Observable.__init__(self)
        self._moto = moto
        self._detenido = threading.Event()

    def run(self) -> None:
        """Loop principal del sensor."""
        while not self._detenido.is_set():
            nivel = self._leer_nivel()
            
            # Enviar evento estructurado
            evento = {
                'tipo': 'combustible',
                'valor': nivel,
                'unidad': '%',
                'timestamp': time.time()
            }
            
            self.notificar_observadores(evento)
            time.sleep(INTERVALO_COMBUSTIBLE)

    def _leer_nivel(self) -> float:
        """Lee el nivel de combustible actual."""
        return self._moto.get_porcentaje_combustible()

    def detener(self) -> None:
        """Detiene el sensor."""
        self._detenido.set()

    def get_nivel_actual(self) -> float:
        """Retorna último nivel leído (%)."""
        return self._moto.get_porcentaje_combustible()

# ==============================================================================
# ARCHIVO 70/75: temperatura_motor_sensor.py
# Directorio: python_racing/telemetria/sensores
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/temperatura_motor_sensor.py
# ==============================================================================

import random
import threading
import time
from python_racing.patrones.observer.observable import Observable
from constante import (
    TEMP_MOTOR_MIN,
    TEMP_MOTOR_MAX,
    INTERVALO_TEMP_MOTOR
)


class TemperaturaMotorSensor(threading.Thread, Observable[dict]):
    """Sensor de temperatura del motor con notificaciones estructuradas."""
    
    def __init__(self):
        threading.Thread.__init__(self, daemon=True, name="TempSensor")
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._temperatura_actual = 40.0

    def run(self) -> None:
        """Loop principal del sensor."""
        while not self._detenido.is_set():
            temperatura = self._leer_temperatura()
            
            # Enviar evento estructurado en lugar de float directo
            evento = {
                'tipo': 'temperatura',
                'valor': temperatura,
                'unidad': '°C',
                'timestamp': time.time()
            }
            
            self.notificar_observadores(evento)
            time.sleep(INTERVALO_TEMP_MOTOR)

    def _leer_temperatura(self) -> float:
        """Simula lectura de temperatura."""
        # Generar temperatura aleatoria en rango
        self._temperatura_actual = random.uniform(
            TEMP_MOTOR_MIN,
            TEMP_MOTOR_MAX
        )
        return self._temperatura_actual

    def detener(self) -> None:
        """Detiene el sensor."""
        self._detenido.set()

    def get_temperatura_actual(self) -> float:
        """Retorna última temperatura leída."""
        return self._temperatura_actual

# ==============================================================================
# ARCHIVO 71/75: velocidad_sensor.py
# Directorio: python_racing/telemetria/sensores
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/sensores/velocidad_sensor.py
# ==============================================================================

import random
import threading
import time
from python_racing.patrones.observer.observable import Observable
from constante import INTERVALO_VELOCIDAD, VELOCIDAD_MAX_MOTOGP


class VelocidadSensor(threading.Thread, Observable[dict]):
    """Sensor de velocidad con notificaciones estructuradas."""
    
    def __init__(self):
        threading.Thread.__init__(self, daemon=True, name="VelocidadSensor")
        Observable.__init__(self)
        self._detenido = threading.Event()
        self._velocidad_actual = 0.0

    def run(self) -> None:
        """Loop principal del sensor."""
        while not self._detenido.is_set():
            velocidad = self._leer_velocidad()
            
            # Enviar evento estructurado
            evento = {
                'tipo': 'velocidad',
                'valor': velocidad,
                'unidad': 'km/h',
                'timestamp': time.time()
            }
            
            self.notificar_observadores(evento)
            time.sleep(INTERVALO_VELOCIDAD)

    def _leer_velocidad(self) -> float:
        """Simula lectura de velocidad."""
        # Generar velocidad aleatoria entre 0 y velocidad máxima
        self._velocidad_actual = random.uniform(100, VELOCIDAD_MAX_MOTOGP)
        return self._velocidad_actual

    def detener(self) -> None:
        """Detiene el sensor."""
        self._detenido.set()

    def get_velocidad_actual(self) -> float:
        """Retorna última velocidad leída (km/h)."""
        return self._velocidad_actual


################################################################################
# DIRECTORIO: python_racing/tests
################################################################################

# ==============================================================================
# ARCHIVO 72/75: __init__.py
# Directorio: python_racing/tests
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/tests/__init__.py
# ==============================================================================

#Ejecutar con: python -m unittest discover -s python_racing/tests -t .


# ==============================================================================
# ARCHIVO 73/75: test_carreras.py
# Directorio: python_racing/tests
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/tests/test_carreras.py
# ==============================================================================

import unittest
from datetime import date
from python_racing.entidades.circuitos.circuito import Circuito, TipoSuperficie
from python_racing.entidades.circuitos.carrera import Carrera, ResultadoCarrera
from python_racing.entidades.escuderias.escuderia import Escuderia
from python_racing.entidades.escuderias.corredor import Corredor


class TestCircuito(unittest.TestCase):
    def test_crear_circuito(self):
        """Verifica creación de circuito."""
        circuito = Circuito(
            "Termas de Río Hondo",
            4.8,
            "Argentina",
            TipoSuperficie.ASFALTO
        )
        self.assertEqual(circuito.get_nombre(), "Termas de Río Hondo")
        self.assertEqual(circuito.get_longitud_km(), 4.8)

    def test_longitud_invalida(self):
        """Debe lanzar error si longitud es 0 o negativa."""
        with self.assertRaises(ValueError):
            Circuito("Test", 0, "Argentina", TipoSuperficie.ASFALTO)


class TestCarrera(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada test."""
        self.circuito = Circuito(
            "Test Circuit",
            5.0,
            "Argentina",
            TipoSuperficie.ASFALTO
        )
        self.carrera = Carrera(self.circuito, date.today(), 20)

    def test_crear_carrera(self):
        """Verifica creación de carrera."""
        self.assertEqual(self.carrera.get_vueltas(), 20)
        self.assertFalse(self.carrera.esta_finalizada())

    def test_vueltas_invalidas(self):
        """Debe lanzar error si vueltas <= 0."""
        with self.assertRaises(ValueError):
            Carrera(self.circuito, date.today(), 0)

    def test_agregar_corredor(self):
        """Verifica agregar corredores."""
        escuderia = Escuderia("Ducati", "Italia", 10000000)
        corredor = Corredor("Bagnaia", "Italia", 63, 27, escuderia)
        
        self.carrera.agregar_corredor(corredor)
        
        self.assertEqual(len(self.carrera.get_corredores_participantes()), 1)

    def test_finalizar_carrera(self):
        """Verifica finalización de carrera."""
        self.carrera.finalizar_carrera()
        self.assertTrue(self.carrera.esta_finalizada())


if __name__ == "__main__":
    unittest.main()

# ==============================================================================
# ARCHIVO 74/75: test_motos.py
# Directorio: python_racing/tests
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/tests/test_motos.py
# ==============================================================================

import unittest
from python_racing.entidades.motos.moto import Moto
from python_racing.entidades.motos.motor import Motor, TipoMotor
from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico
from python_racing.patrones.factory.moto_factory import MotoFactory
from python_racing.excepciones.combustible_excedido_exception import CombustibleExcedidoException
from python_racing.excepciones.combustible_insuficiente_exception import CombustibleInsuficienteException


class TestMotor(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada test."""
        self.motor = Motor(TipoMotor.V4, 1000, 18000)

    def test_creacion_motor(self):
        """Verifica que el motor se crea correctamente."""
        self.assertEqual(self.motor.get_tipo(), TipoMotor.V4)
        self.assertEqual(self.motor.get_cilindrada(), 1000)
        self.assertEqual(self.motor.get_revoluciones_max(), 18000)
        self.assertEqual(self.motor.get_temperatura(), 40.0)

    def test_motor_cilindrada_invalida(self):
        """Debe lanzar error si cilindrada es 0 o negativa."""
        with self.assertRaises(ValueError):
            Motor(TipoMotor.V4, 0, 18000)
        with self.assertRaises(ValueError):
            Motor(TipoMotor.V4, -100, 18000)

    def test_incrementar_temperatura(self):
        """Verifica que la temperatura se puede aumentar."""
        self.motor.set_temperatura(85.0)
        self.assertEqual(self.motor.get_temperatura(), 85.0)

    def test_motor_sobrecalentado(self):
        """Verifica detección de sobrecalentamiento."""
        self.motor.set_temperatura(125.0)
        self.assertTrue(self.motor.esta_sobrecalentado())

    def test_incrementar_horas_uso(self):
        """Verifica contador de horas."""
        self.motor.incrementar_horas_uso(2.5)
        self.assertEqual(self.motor.get_horas_uso(), 2.5)


class TestNeumatico(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada test."""
        self.neumatico = Neumatico(TipoNeumatico.SLICK)

    def test_creacion_neumatico(self):
        """Verifica que el neumático se crea nuevo."""
        self.assertEqual(self.neumatico.get_tipo(), TipoNeumatico.SLICK)
        self.assertEqual(self.neumatico.get_desgaste(), 0.0)
        self.assertEqual(self.neumatico.get_vueltas_rodadas(), 0)

    def test_aplicar_desgaste(self):
        """Verifica que el desgaste se aplica correctamente."""
        self.neumatico.aplicar_desgaste(50.0)
        self.assertEqual(self.neumatico.get_desgaste(), 50.0)

    def test_desgaste_maximo(self):
        """El desgaste no debe superar 100%."""
        self.neumatico.aplicar_desgaste(150.0)
        self.assertEqual(self.neumatico.get_desgaste(), 100.0)

    def test_incrementar_vueltas(self):
        """Verifica contador de vueltas."""
        self.neumatico.incrementar_vueltas()
        self.neumatico.incrementar_vueltas()
        self.assertEqual(self.neumatico.get_vueltas_rodadas(), 2)

    def test_neumatico_gastado(self):
        """Verifica detección de neumático gastado."""
        self.neumatico.aplicar_desgaste(85.0)
        self.assertTrue(self.neumatico.esta_gastado())


class TestMoto(unittest.TestCase):
    def setUp(self):
        """Configuración antes de cada test."""
        motor = Motor(TipoMotor.V4, 1000, 18000)
        self.moto = Moto(
            marca="Ducati",
            modelo="Desmosedici GP25",
            motor=motor,
            potencia_hp=275,
            combustible_max=22.0,
            peso_kg=157
        )

    def test_creacion_moto(self):
        """Verifica que la moto se crea correctamente."""
        self.assertEqual(self.moto.get_marca(), "Ducati")
        self.assertEqual(self.moto.get_potencia_hp(), 275)
        self.assertEqual(self.moto.get_combustible_max(), 22.0)
        self.assertEqual(self.moto.get_combustible_actual(), 22.0)

    def test_cargar_combustible(self):
        """Verifica carga de combustible."""
        self.moto.consumir_combustible(10.0)
        self.moto.cargar_combustible(5.0)
        self.assertEqual(self.moto.get_combustible_actual(), 17.0)

    def test_combustible_excedido(self):
        """Debe lanzar excepción si se excede capacidad."""
        with self.assertRaises(CombustibleExcedidoException):
            self.moto.cargar_combustible(10.0)  # Ya está llena

    def test_consumir_combustible(self):
        """Verifica consumo de combustible."""
        self.moto.consumir_combustible(5.0)
        self.assertEqual(self.moto.get_combustible_actual(), 17.0)

    def test_combustible_insuficiente(self):
        """Debe lanzar excepción si no hay suficiente."""
        with self.assertRaises(CombustibleInsuficienteException):
            self.moto.consumir_combustible(30.0)

    def test_porcentaje_combustible(self):
        """Verifica cálculo de porcentaje."""
        self.moto.consumir_combustible(11.0)  # 50%
        self.assertEqual(self.moto.get_porcentaje_combustible(), 50.0)

    def test_asignar_neumaticos(self):
        """Verifica asignación de neumáticos."""
        delantero = Neumatico(TipoNeumatico.SLICK)
        trasero = Neumatico(TipoNeumatico.SLICK)
        
        self.moto.set_neumatico_delantero(delantero)
        self.moto.set_neumatico_trasero(trasero)
        
        self.assertTrue(self.moto.tiene_neumaticos_instalados())


class TestMotoFactory(unittest.TestCase):
    def test_crear_ducati(self):
        """Verifica creación de Ducati."""
        moto = MotoFactory.crear_moto("Ducati")
        self.assertEqual(moto.get_marca(), "Ducati")
        self.assertEqual(moto.get_modelo(), "Desmosedici GP25")
        self.assertEqual(moto.get_potencia_hp(), 275)

    def test_crear_yamaha(self):
        """Verifica creación de Yamaha."""
        moto = MotoFactory.crear_moto("Yamaha")
        self.assertEqual(moto.get_marca(), "Yamaha")
        self.assertEqual(moto.get_modelo(), "YZR-M1")

    def test_crear_ktm(self):
        """Verifica creación de KTM."""
        moto = MotoFactory.crear_moto("KTM")
        self.assertEqual(moto.get_marca(), "KTM")

    def test_crear_honda(self):
        """Verifica creación de Honda."""
        moto = MotoFactory.crear_moto("Honda")
        self.assertEqual(moto.get_marca(), "Honda")

    def test_marca_desconocida(self):
        """Debe lanzar error si la marca no existe."""
        with self.assertRaises(ValueError):
            MotoFactory.crear_moto("Suzuki")


if __name__ == "__main__":
    unittest.main()

# ==============================================================================
# ARCHIVO 75/75: test_telemetria.py
# Directorio: python_racing/tests
# Ruta completa: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/tests/test_telemetria.py
# ==============================================================================

import unittest
import time
from python_racing.telemetria.sensores.temperatura_motor_sensor import TemperaturaMotorSensor
from python_racing.telemetria.sensores.velocidad_sensor import VelocidadSensor
from python_racing.patrones.factory.moto_factory import MotoFactory
from python_racing.telemetria.sensores.combustible_sensor import CombustibleSensor
from python_racing.telemetria.control.control_boxes_task import ControlBoxesTask
from constante import THREAD_JOIN_TIMEOUT


class TestSensores(unittest.TestCase):
    def test_sensor_temperatura(self):
        """Verifica que el sensor de temperatura funciona."""
        sensor = TemperaturaMotorSensor()
        
        # El sensor debe arrancar en 40°C
        temp = sensor.get_temperatura_actual()
        self.assertGreaterEqual(temp, 40.0)

    def test_sensor_temperatura_thread(self):
        """Verifica que el sensor funciona en thread."""
        sensor = TemperaturaMotorSensor()
        sensor.start()
        
        time.sleep(1)  # Esperar 1 segundo
        
        temp = sensor.get_temperatura_actual()
        self.assertGreaterEqual(temp, 40.0)
        self.assertLessEqual(temp, 130.0)
        
        sensor.detener()
        sensor.join(timeout=THREAD_JOIN_TIMEOUT)

    def test_sensor_velocidad(self):
        """Verifica que el sensor de velocidad funciona."""
        sensor = VelocidadSensor()
        sensor.start()
        
        time.sleep(1)
        
        velocidad = sensor.get_velocidad_actual()
        self.assertGreaterEqual(velocidad, 0.0)
        self.assertLessEqual(velocidad, 350.0)
        
        sensor.detener()
        sensor.join(timeout=THREAD_JOIN_TIMEOUT)


class TestControlBoxes(unittest.TestCase):
    def test_control_boxes_creacion(self):
        """Verifica creación del controlador."""
        moto = MotoFactory.crear_moto("Ducati")
        control = ControlBoxesTask(moto)
        
        self.assertFalse(control.requiere_entrada_boxes())


if __name__ == "__main__":
    unittest.main()


################################################################################
# FIN DEL INTEGRADOR FINAL
# Total de archivos: 75
# Generado: 2025-11-04 23:09:58
################################################################################
