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