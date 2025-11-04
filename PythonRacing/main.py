"""
main.py - Punto de entrada del sistema PythonRacing

Este es el archivo que debes ejecutar:
    python3 main.py

NO ejecutes los __init__.py directamente.
"""

# Test básico de importaciones
def test_importaciones():
    """Prueba que todas las importaciones funcionen."""
    print("=" * 70)
    print("PROBANDO IMPORTACIONES DE PYTHONRACING")
    print("=" * 70)
    
    try:
        # Test 1: Importar Motor
        print("\n[TEST 1] Importando Motor...")
        from python_racing.entidades.motos.motor import Motor, TipoMotor
        motor = Motor(TipoMotor.V4, 1000, 18000)
        print(f"✅ Motor creado: {motor}")
        
        # Test 2: Importar Neumático
        print("\n[TEST 2] Importando Neumático...")
        from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico
        neumatico = Neumatico(TipoNeumatico.SLICK)
        print(f"✅ Neumático creado: {neumatico}")
        
        # Test 3: Importar Escudería
        print("\n[TEST 3] Importando Escudería...")
        from python_racing.entidades.escuderias.escuderia import Escuderia
        ducati = Escuderia("Ducati Lenovo Team", "Italia", 15000000.0)
        print(f"✅ Escudería creada: {ducati}")
        
        # Test 4: Importar Corredor
        print("\n[TEST 4] Importando Corredor...")
        from python_racing.entidades.escuderias.corredor import Corredor
        bagnaia = Corredor("Francesco Bagnaia", "Italia", 63, 27, ducati)
        print(f"✅ Corredor creado: {bagnaia}")
        
        # Test 5: Importar Moto
        print("\n[TEST 5] Importando Moto...")
        from python_racing.entidades.motos.moto import Moto
        moto = Moto(
            marca="Ducati",
            modelo="Desmosedici GP25",
            motor=motor,
            potencia_hp=275,
            combustible_max=22.0,
            peso_kg=157
        )
        moto.set_corredor(bagnaia)
        print(f"✅ Moto creada: {moto}")
        
        # Test 6: Importar Circuito
        print("\n[TEST 6] Importando Circuito...")
        from python_racing.entidades.circuitos.circuito import Circuito, TipoSuperficie
        circuito = Circuito(
            "Autódromo Termas de Río Hondo",
            4.8,
            "Argentina",
            TipoSuperficie.ASFALTO
        )
        print(f"✅ Circuito creado: {circuito}")
        
        # Test 7: Importar Mecánico
        print("\n[TEST 7] Importando Mecánico...")
        from python_racing.entidades.personal.mecanico import Mecanico, EspecialidadMecanico
        mecanico = Mecanico(
            "Carlo Luzzi",
            EspecialidadMecanico.JEFE_MECANICO,
            15,
            ducati
        )
        print(f"✅ Mecánico creado: {mecanico}")
        
        # Test 8: Importar Fallo Mecánico
        print("\n[TEST 8] Importando Fallo Mecánico...")
        from PythonRacing.python_racing.entidades.mantenimiento.fallo_mecanico import (
            FalloMecanico, TipoFallo, GravedadFallo
        )
        fallo = FalloMecanico(
            TipoFallo.MOTOR,
            GravedadFallo.LEVE,
            "Temperatura alta pero controlable",
            moto
        )
        print(f"✅ Fallo creado: {fallo}")
        
        print("\n" + "=" * 70)
        print("✅ TODOS LOS TESTS PASARON CORRECTAMENTE")
        print("=" * 70)
        return True
        
    except ImportError as e:
        print(f"\n❌ ERROR DE IMPORTACIÓN: {e}")
        print("\nVerifica que:")
        print("1. Estás en el directorio raíz (PythonRacing/)")
        print("2. Todas las carpetas tienen __init__.py")
        print("3. Los nombres de archivos coinciden")
        return False
    except Exception as e:
        print(f"\n❌ ERROR INESPERADO: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Función principal."""
    print("\n🏍️  BIENVENIDO A PYTHONRACING 🏍️\n")
    
    # Ejecutar tests de importación
    if test_importaciones():
        print("\n✅ Sistema listo para usar")
        print("\nPróximos pasos:")
        print("1. Implementar excepciones personalizadas")
        print("2. Crear patrones de diseño (Factory, Strategy, Observer)")
        print("3. Implementar servicios de negocio")
        print("4. Sistema de telemetría")
        return 0
    else:
        print("\n❌ Hay problemas con las importaciones")
        print("Revisa la estructura de carpetas y archivos")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())