"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing
Fecha: 2025-11-04 22:18:06
Total de archivos integrados: 4
"""

# ================================================================================
# ARCHIVO 1/4: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/__init__.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 2/4: buscar_paquete.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/buscar_paquete.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/4: constante.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/constante.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 4/4: main.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/main.py
# ================================================================================

import time
from datetime import date

# Servicios
from python_racing.servicios.escuderias.escuderia_service import EscuderiaService
from python_racing.servicios.escuderias.corredor_service import CorredorService
from python_racing.servicios.circuitos.circuito_service import CircuitoService
from python_racing.servicios.circuitos.carrera_service import CarreraService
from python_racing.servicios.motos.moto_service import MotoService

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
        "Francesco Bagnaia", "Italia", 63, 27, ducati)
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
    print("  - FACTORY METHOD (MotoFactory)")
    print("  - STRATEGY (Desgaste de neumáticos)")
    print("  - OBSERVER (Telemetría en tiempo real)")
    print("  - SINGLETON (Bonus - MotoServiceRegistry)")
    
    try:
        # Crear servicios
        moto_service = MotoService()
        
        # 1. FACTORY METHOD
        demostrar_factory()
        
        # 2. STRATEGY
        demostrar_strategy(moto_service)
        
        # 3. OBSERVER
        demostrar_observer()
        
        # 4. SIMULACIÓN COMPLETA
        demostrar_simulacion_carrera()
        
        # Resumen final
        imprimir_encabezado("EJEMPLO COMPLETADO EXITOSAMENTE")
        
        print("\nResumen de patrones demostrados:")
        print("  [OK] FACTORY     - Creación dinámica de 4 marcas de motos")
        print("  [OK] STRATEGY    - Algoritmos de desgaste intercambiables")
        print("  [OK] OBSERVER    - Sistema de telemetría con sensores")
        
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

