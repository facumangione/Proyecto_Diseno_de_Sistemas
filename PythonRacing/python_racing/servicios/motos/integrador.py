"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/servicios/motos
Fecha: 2025-11-04 23:10:05
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

