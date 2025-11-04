from enum import Enum


class TipoMotor(Enum):
    """Los tipos de motor que verás en MotoGP."""
    V4 = "V4"
    LINEAL_4 = "Lineal 4 cilindros"
    BICILINDRIRCO = "Bicilíndrico"
    MONOCILINDRIRCO = "Monocilíndrico"


class Motor:

    def __init__(self, tipo: TipoMotor, cilindrada: int, revoluciones_max: int):
        if cilindrada <= 0:
            raise ValueError("¿Un motor de 0cc? No funciona así, necesitas cilindrada")
        if revoluciones_max <= 0:
            raise ValueError("Sin revoluciones no hay motor, simple")
        
        self._tipo = tipo
        self._cilindrada = cilindrada
        self._revoluciones_max = revoluciones_max
        self._temperatura = 40.0  # Empieza frío, como debe ser
        self._horas_uso = 0.0

    def get_tipo(self) -> TipoMotor:
        """Qué tipo de motor es."""
        return self._tipo

    def get_cilindrada(self) -> int:
        """Cuántos cc tiene el motor."""
        return self._cilindrada

    def get_revoluciones_max(self) -> int:
        """Hasta dónde puede girar sin romperse."""
        return self._revoluciones_max

    def get_temperatura(self) -> float:
        """Qué tan caliente está ahora mismo."""
        return self._temperatura

    def get_horas_uso(self) -> float:
        """Cuántas horas lleva funcionando."""
        return self._horas_uso

    def set_temperatura(self, temperatura: float) -> None:
        if temperatura < 0:
            raise ValueError("Temperatura negativa no existe (al menos no aquí)")
        self._temperatura = temperatura

    def incrementar_horas_uso(self, horas: float) -> None:
        """Suma horas de uso. Cada hora cuenta para el mantenimiento."""
        if horas < 0:
            raise ValueError("No puedes retroceder el tiempo")
        self._horas_uso += horas

    def esta_sobrecalentado(self) -> bool:
        from constante import TEMP_MOTOR_ALERTA
        return self._temperatura >= TEMP_MOTOR_ALERTA

    def necesita_revision(self) -> bool:
        
        return self._horas_uso >= 50.0

    def __str__(self) -> str:
        estado = "🔥 SOBRECALENTADO" if self.esta_sobrecalentado() else "✓ OK"
        return (
            f"Motor {self._tipo.value} - {self._cilindrada}cc - "
            f"{self._revoluciones_max} RPM - {self._temperatura:.1f}°C {estado}"
        )