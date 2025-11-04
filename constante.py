# ============================================================================
# constante.py - PythonRacing
# ============================================================================
# Todas las constantes del sistema centralizadas.
# NO hardcodear valores mágicos en el código.
# ============================================================================

# ============================================================================
# MOTOS - Especificaciones por Marca
# ============================================================================

# Ducati Desmosedici GP25
COMBUSTIBLE_MAX_DUCATI = 22.0
POTENCIA_DUCATI = 275
PESO_DUCATI = 157
REV_MAX_DUCATI = 18000

# Yamaha YZR-M1
COMBUSTIBLE_MAX_YAMAHA = 21.5
POTENCIA_YAMAHA = 270
PESO_YAMAHA = 158
REV_MAX_YAMAHA = 17500

# KTM RC16
COMBUSTIBLE_MAX_KTM = 21.8
POTENCIA_KTM = 265
PESO_KTM = 159
REV_MAX_KTM = 17800

# Honda RC213V
COMBUSTIBLE_MAX_HONDA = 22.0
POTENCIA_HONDA = 268
PESO_HONDA = 157
REV_MAX_HONDA = 17900

# ============================================================================
# NEUMÁTICOS - Desgaste por Tipo y Condición
# ============================================================================

# Desgaste por vuelta (porcentaje)
DESGASTE_SLICK_SECO = 0.02      # 2% por vuelta en seco
DESGASTE_SLICK_LLUVIA = 0.10    # 10% por vuelta en lluvia
DESGASTE_INTERMEDIO_SECO = 0.05
DESGASTE_INTERMEDIO_LLUVIA = 0.03
DESGASTE_LLUVIA_SECO = 0.15
DESGASTE_LLUVIA_LLUVIA = 0.02

# Vida útil de neumáticos (vueltas)
VIDA_NEUMATICO_SLICK = 25
VIDA_NEUMATICO_INTERMEDIO = 20
VIDA_NEUMATICO_LLUVIA = 30

# ============================================================================
# TELEMETRÍA - Sensores y Alertas
# ============================================================================

# Temperatura del motor
TEMP_MOTOR_MIN = 40        # °C
TEMP_MOTOR_MAX = 130       # °C
TEMP_MOTOR_OPTIMA = 85     # °C
TEMP_MOTOR_ALERTA = 120    # °C
TEMP_MOTOR_CRITICA = 125   # °C

# Combustible
COMBUSTIBLE_ALERTA = 10.0  # porcentaje
COMBUSTIBLE_CRITICO = 5.0  # porcentaje

# Velocidad
VELOCIDAD_MAX_MOTOGP = 350  # km/h
VELOCIDAD_PROMEDIO = 180    # km/h

# ============================================================================
# SENSORES - Intervalos de Lectura (segundos)
# ============================================================================

INTERVALO_TEMP_MOTOR = 2.0
INTERVALO_COMBUSTIBLE = 1.0
INTERVALO_VELOCIDAD = 0.5
INTERVALO_CONTROL_BOXES = 3.0
THREAD_JOIN_TIMEOUT = 2.0

# ============================================================================
# CARRERAS - Configuración de Competencias
# ============================================================================

VUELTAS_DEFAULT = 25
VUELTAS_SPRINT = 10
TIEMPO_VUELTA_BASE = 90      # segundos
TIEMPO_ENTRADA_BOXES = 30    # segundos
TIEMPO_CAMBIO_NEUMATICOS = 5 # segundos
TIEMPO_CARGA_COMBUSTIBLE = 10 # segundos

# ============================================================================
# CIRCUITOS - Longitudes y Características
# ============================================================================

# Longitud promedio de circuitos MotoGP (km)
LONGITUD_MIN_CIRCUITO = 3.5
LONGITUD_MAX_CIRCUITO = 6.0

# ============================================================================
# ESCUDERÍAS - Límites Financieros
# ============================================================================

PRESUPUESTO_MIN_ESCUDERIA = 1000000.0    # 1 millón
PRESUPUESTO_MAX_ESCUDERIA = 50000000.0   # 50 millones

# Costos de operación
COSTO_CARRERA = 100000.0
COSTO_REPARACION_LEVE = 5000.0
COSTO_REPARACION_MEDIA = 25000.0
COSTO_REPARACION_GRAVE = 100000.0

# ============================================================================
# CORREDORES - Restricciones
# ============================================================================

EDAD_MIN_CORREDOR = 18
EDAD_MAX_CORREDOR = 50
NUMERO_MIN_CORREDOR = 1
NUMERO_MAX_CORREDOR = 99

# ============================================================================
# PERSISTENCIA - Configuración de Archivos
# ============================================================================

DIRECTORIO_DATA = "data"
EXTENSION_DATA = ".dat"

# ============================================================================
# SIMULACIÓN - Factores de Aleatoriedad
# ============================================================================

# Probabilidad de fallos mecánicos (por vuelta)
PROB_FALLO_MOTOR = 0.001      # 0.1%
PROB_FALLO_FRENOS = 0.002     # 0.2%
PROB_FALLO_SUSPENSION = 0.003 # 0.3%
PROB_FALLO_ELECTRONICA = 0.002

# Factores de rendimiento
FACTOR_EXPERIENCIA = 0.95  # Reduce tiempo por vuelta
FACTOR_NEUMATICO_NUEVO = 0.98
FACTOR_NEUMATICO_GASTADO = 1.05
FACTOR_COMBUSTIBLE_BAJO = 1.02

# ============================================================================
# CLIMA - Condiciones de Pista
# ============================================================================

PROB_LLUVIA = 0.15           # 15% probabilidad de lluvia
PROB_CAMBIO_CLIMA = 0.05     # 5% cambio por vuelta