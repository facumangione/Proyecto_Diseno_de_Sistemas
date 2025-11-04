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