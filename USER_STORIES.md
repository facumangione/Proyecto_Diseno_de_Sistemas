```python
from python_racing.servicios.corredor_service import CorredorService

corredor_service = CorredorService()
bagnaia = corredor_service.registrar_corredor(
    nombre="Francesco Bagnaia",
    nacionalidad="Italia",
    numero=63,
    edad=27,
    escuderia=ducati
)
```

**Validaciones:**
```python
bagnaia.set_edad(16)  # ValueError: corredor debe ser mayor de edad
```

---

## Epic 2: Gestión de Motos y Componentes

### US-003: Registrar Moto de Competición

**Como** ingeniero jefe  
**Quiero** registrar una moto con su marca, modelo, motor y potencia  
**Para** gestionarla dentro de la escudería  

#### Criterios de Aceptación
- [x] Cada moto debe tener:
  - Marca y modelo  
  - Tipo de motor (ej: monocilíndrico, bicilíndrico, V4)  
  - Potencia en HP (> 0)  
  - Capacidad de combustible (litros)  
- [x] Cada moto debe asociarse a un corredor  

#### Detalles Técnicos

**Clase**: `Moto` (`python_racing/entidades/moto.py`)  
**Servicio**: `MotoService` (`python_racing/servicios/moto_service.py`)  

**Ejemplo:**
```python
moto = MotoService().crear_moto(
    marca="Ducati",
    modelo="Desmosedici GP25",
    tipo_motor="V4",
    potencia_hp=275,
    combustible_max=22,
    corredor=bagnaia
)
```

---

### US-004: Asignar Neumáticos a la Moto

**Como** técnico de pista  
**Quiero** asignar neumáticos según el tipo de circuito  
**Para** optimizar el rendimiento de la moto  

#### Criterios de Aceptación
- [x] Los neumáticos deben tener:
  - Tipo (slick, intermedio, lluvia)  
  - Estado (nuevo, usado, gastado)  
- [x] Cada moto puede tener hasta 2 juegos activos  
- [x] El tipo de neumático debe ser compatible con las condiciones de la pista  

#### Detalles Técnicos
**Clase**: `Neumatico` (`python_racing/entidades/neumatico.py`)  
**Servicio**: `NeumaticoService` (`python_racing/servicios/neumatico_service.py`)  

**Ejemplo:**
```python
from python_racing.entidades.neumatico import TipoNeumatico

neumaticos = NeumaticoService().asignar_neumaticos(
    moto=moto,
    tipo=TipoNeumatico.SLICK,
    estado="nuevo"
)
```

---

### US-005: Cargar Combustible a la Moto

**Como** mecánico de box  
**Quiero** recargar combustible en la moto  
**Para** preparar la moto antes de la carrera  

#### Criterios de Aceptación
- [x] La carga no puede superar la capacidad máxima  
- [x] Si se excede, lanzar `CombustibleExcedidoException`  
- [x] Si la cantidad es negativa, lanzar `ValueError`  

**Ejemplo:**
```python
moto.cargar_combustible(10)  # OK
moto.cargar_combustible(50)  # CombustibleExcedidoException
```

---

## Epic 3: Sistema de Carreras y Pistas

### US-006: Registrar Circuito de Carrera

**Como** organizador del campeonato  
**Quiero** registrar circuitos con longitud, país y tipo  
**Para** planificar las competencias oficiales  

#### Criterios de Aceptación
- [x] Cada circuito debe tener:
  - Nombre  
  - Longitud (en km)  
  - País  
  - Tipo de superficie (asfalto, mixto, tierra)  

**Clase**: `Circuito` (`python_racing/entidades/circuito.py`)  
**Servicio**: `CircuitoService` (`python_racing/servicios/circuito_service.py`)  

**Ejemplo:**
```python
circuito = CircuitoService().registrar_circuito(
    nombre="Autódromo Termas de Río Hondo",
    longitud_km=4.8,
    pais="Argentina",
    superficie="asfalto"
)
```

---

### US-007: Simular Carrera

**Como** director de carrera  
**Quiero** simular una competencia completa  
**Para** determinar posiciones finales según el rendimiento de motos y pilotos  

#### Criterios de Aceptación
- [x] La simulación debe considerar:
  - Potencia del motor  
  - Tipo de neumático y su desgaste  
  - Nivel de combustible  
  - Condiciones del circuito  
  - Posibilidad de fallos mecánicos (aleatorio)  
- [x] Retornar clasificación final con tiempos promedio  

**Ejemplo:**
```python
from python_racing.servicios.carrera_service import CarreraService

carrera = CarreraService().simular(
    circuito=circuito,
    corredores=[bagnaia],
    vueltas=25
)
```

**Salida esperada:**
```
🏁 RESULTADO CARRERA: Termas de Río Hondo
-----------------------------------------
1. Francesco Bagnaia (Ducati Lenovo Team) - 41m 25s
```

---

## Epic 4: Gestión de Mantenimiento y Rendimiento

### US-008: Registrar Fallo Mecánico

**Como** ingeniero de pista  
**Quiero** registrar un fallo mecánico en una moto  
**Para** planificar su reparación  

#### Criterios de Aceptación
- [x] Cada fallo debe tener:
  - Tipo (motor, frenos, suspensión, electrónica)  
  - Gravedad (leve, media, grave)  
  - Fecha de detección  
- [x] El sistema debe impedir participar en carreras si hay fallos graves  

**Clase**: `FalloMecanico` (`python_racing/entidades/fallo_mecanico.py`)  

---

### US-009: Calcular Rendimiento Promedio

**Como** analista de datos  
**Quiero** obtener el rendimiento medio de cada moto  
**Para** evaluar su desempeño durante la temporada  

#### Criterios de Aceptación
- [x] El rendimiento se calcula como:  
  `(vueltas completadas * potencia) / tiempo_total`  
- [x] Debe generarse un ranking por escudería  

---

## Epic 5: Telemetría y Sensores en Tiempo Real

### US-010: Medir Temperatura del Motor

**Como** sistema de telemetría  
**Quiero** leer la temperatura del motor cada 2 segundos  
**Para** prevenir sobrecalentamiento  

#### Criterios de Aceptación
- [x] Sensor ejecutado en thread daemon  
- [x] Valores entre 40°C y 130°C  
- [x] Si supera 120°C, generar alerta automática  

---

### US-011: Medir Nivel de Combustible en Tiempo Real

**Como** ingeniero de box  
**Quiero** monitorear el combustible restante  
**Para** decidir cuándo ingresar a boxes  

#### Criterios de Aceptación
- [x] Lectura cada 1 segundo  
- [x] Si el nivel < 10%, avisar al equipo  

---

## Epic 6: Persistencia y Auditoría

### US-012: Guardar Datos de Carrera

**Como** analista del campeonato  
**Quiero** persistir los resultados y estadísticas  
**Para** analizarlas luego de cada evento  

---

## Historias Técnicas (Patrones de Diseño)

- **Factory Method** → creación de motos según marca (Ducati, Yamaha, KTM)  
- **Strategy** → gestión de neumáticos según clima  
- **Observer** → sensores de telemetría  
- **Singleton** → servicio de configuración global  
- **Command** → acciones de box (entrada/salida, carga, cambio de neumáticos)