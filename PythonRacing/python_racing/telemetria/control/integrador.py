"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/control
Fecha: 2025-11-04 23:10:05
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/control/__init__.py
# ================================================================================

"""
Controladores de telemetría
"""


# ================================================================================
# ARCHIVO 2/2: control_boxes_task.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/telemetria/control/control_boxes_task.py
# ================================================================================

import threading
import time
from constante import (
    COMBUSTIBLE_ALERTA,
    COMBUSTIBLE_CRITICO,
    TEMP_MOTOR_ALERTA,
    TEMP_MOTOR_CRITICA,
    INTERVALO_CONTROL_BOXES
)
from python_racing.patrones.observer.observer import Observer


class ControlBoxesTask(Observer):
    def __init__(self, moto):
        self._moto = moto
        self._temperatura_actual = None
        self._combustible_actual = None
        self._velocidad_actual = None
        self._alerta_activa = False
        self._running = True
        
        # Thread para monitoreo periódico
        self._thread = threading.Thread(
            target=self._monitorear,
            daemon=True,
            name="ControlBoxes"
        )

    def actualizar(self, evento: dict) -> None:
        try:
            if not isinstance(evento, dict):
                print(f"[WARN] Evento inválido (tipo {type(evento).__name__}): {evento}")
                return
            
            tipo = evento.get('tipo')
            valor = evento.get('valor')
            
            if tipo == 'temperatura':
                self._temperatura_actual = float(valor)
            elif tipo == 'combustible':
                self._combustible_actual = float(valor)
            elif tipo == 'velocidad':
                self._velocidad_actual = float(valor)
            else:
                print(f"[WARN] Tipo de evento desconocido: {tipo}")
                
        except (ValueError, TypeError, KeyError) as e:
            print(f"[ERROR] Error procesando evento: {evento} - {e}")

    def iniciar(self) -> None:
        """Inicia el monitoreo en background."""
        self._thread.start()

    def start(self) -> None:
        """Alias para iniciar() (compatibilidad con threading)."""
        self.iniciar()

    def detener(self) -> None:
        """Detiene el monitoreo."""
        self._running = False

    def join(self, timeout=None) -> None:
        if self._thread.is_alive():
            self._thread.join(timeout=timeout)

    def _monitorear(self) -> None:
        while self._running:
            try:
                self._verificar_alertas()
                time.sleep(INTERVALO_CONTROL_BOXES)
            except Exception as e:
                print(f"[ERROR] En monitoreo: {e}")

    def _verificar_alertas(self) -> None:
        """Verifica si hay condiciones que requieren atención."""
        alertas = []
        
        # Verificar temperatura (solo si tenemos datos)
        if self._temperatura_actual is not None:
            if self._temperatura_actual >= TEMP_MOTOR_CRITICA:
                alertas.append(f"🔥 TEMPERATURA CRÍTICA: {self._temperatura_actual:.1f}°C")
            elif self._temperatura_actual >= TEMP_MOTOR_ALERTA:
                alertas.append(f"⚠️  Temperatura alta: {self._temperatura_actual:.1f}°C")
        
        # Verificar combustible (solo si tenemos datos)
        if self._combustible_actual is not None:
            if self._combustible_actual <= COMBUSTIBLE_CRITICO:
                alertas.append(f"⛽ COMBUSTIBLE CRÍTICO: {self._combustible_actual:.1f}%")
            elif self._combustible_actual <= COMBUSTIBLE_ALERTA:
                alertas.append(f"⚠️  Combustible bajo: {self._combustible_actual:.1f}%")
        
        # Si hay alertas nuevas, mostrarlas
        if alertas and not self._alerta_activa:
            self._alerta_activa = True
            print("\n" + "="*60)
            print("🚨 ALERTA DE BOXES 🚨")
            for alerta in alertas:
                print(f"   {alerta}")
            print("="*60 + "\n")
        elif not alertas:
            self._alerta_activa = False

    def obtener_estado(self) -> str:
        # Usar valores por defecto si aún no hay datos
        temp = self._temperatura_actual if self._temperatura_actual is not None else 0.0
        comb = self._combustible_actual if self._combustible_actual is not None else 0.0
        vel = self._velocidad_actual if self._velocidad_actual is not None else 0.0
        
        # Determinar estado general
        if temp >= TEMP_MOTOR_CRITICA or comb <= COMBUSTIBLE_CRITICO:
            estado = "🔴 CRÍTICO"
        elif temp >= TEMP_MOTOR_ALERTA or comb <= COMBUSTIBLE_ALERTA:
            estado = "🟡 ALERTA"
        else:
            estado = "🟢 NORMAL"
        
        return (
            f"{estado} | "
            f"Temp: {temp:.1f}°C | "
            f"Comb: {comb:.1f}% | "
            f"Vel: {vel:.1f} km/h"
        )

    def obtener_temperatura(self) -> float:
        """Temperatura actual del motor."""
        return self._temperatura_actual if self._temperatura_actual is not None else 0.0

    def obtener_combustible(self) -> float:
        """Nivel de combustible actual."""
        return self._combustible_actual if self._combustible_actual is not None else 0.0

    def obtener_velocidad(self) -> float:
        """Velocidad actual."""
        return self._velocidad_actual if self._velocidad_actual is not None else 0.0

    def __str__(self) -> str:
        return f"Control de Boxes - {self._moto.get_marca()} #{self._moto.get_corredor().get_numero()}"
    
    def requiere_entrada_boxes(self) -> bool:
        return self._alerta_activa


