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