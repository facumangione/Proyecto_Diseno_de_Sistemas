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