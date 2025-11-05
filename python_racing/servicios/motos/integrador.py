"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 5
"""

# ================================================================================
# ARCHIVO 1/5: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/__init__.py
# ================================================================================

"""
Servicios de gestión de motos
"""


# ================================================================================
# ARCHIVO 2/5: moto_service.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/moto_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 3/5: moto_service_registry.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/moto_service_registry.py
# ================================================================================



# ================================================================================
# ARCHIVO 4/5: motor_service.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/motor_service.py
# ================================================================================

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

# ================================================================================
# ARCHIVO 5/5: neumatico_service.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos/neumatico_service.py
# ================================================================================

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

