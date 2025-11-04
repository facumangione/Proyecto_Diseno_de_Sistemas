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