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