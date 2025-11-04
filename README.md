# 🏍️ PythonRacing - Sistema de Gestión de Carreras de Motos

Sistema educativo que demuestra la implementación de **patrones de diseño** en Python con enfoque en carreras de MotoGP.

## 🎯 Patrones Implementados

1. **FACTORY METHOD** → Creación de motos por marca (Ducati, Yamaha, KTM, Honda)
2. **STRATEGY** → Algoritmos de desgaste de neumáticos según clima
3. **OBSERVER** → Sistema de telemetría con sensores en tiempo real
4. **SINGLETON** → Registro de servicios (bonus)
5. **COMMAND** → Acciones de boxes (bonus)

## 🚀 Instalación
```bash
# Clonar repositorio
git clone <repo-url>
cd PythonRacing

# Verificar Python 3.13+
python3 --version

# Ejecutar sistema
python3 main.py
```

## 📦 Estructura del Proyecto
```
PythonRacing/
├── python_racing/
│   ├── entidades/          # DTOs (Motos, Escuderías, Circuitos)
│   ├── servicios/          # Lógica de negocio
│   ├── patrones/           # Factory, Strategy, Observer, Command
│   ├── telemetria/         # Sensores en tiempo real
│   ├── excepciones/        # Excepciones personalizadas
│   └── tests/              # Tests unitarios
├── main.py                 # Punto de entrada
└── constante.py            # Constantes centralizadas
```

## 🧪 Tests
```bash
# Ejecutar todos los tests
python3 -m unittest discover -s python_racing/tests -t .

# Test específico
python3 -m unittest python_racing.tests.test_motos
```

## ✨ Características

- ✅ 4 marcas de motos (Ducati, Yamaha, KTM, Honda)
- ✅ Sistema de telemetría en tiempo real
- ✅ Simulación de carreras completas
- ✅ Gestión de neumáticos con desgaste
- ✅ Gestión de combustible
- ✅ Excepciones personalizadas
- ✅ Tests unitarios
- ✅ PEP 8 compliance

## 📖 Documentación

- `USER_STORIES.md` → Historias de usuario detalladas
- `constante.py` → Todas las constantes del sistema

## 🏆 Ejemplos de Uso

### Crear moto con Factory
```python
from python_racing.patrones.factory.moto_factory import MotoFactory

moto = MotoFactory.crear_moto("Ducati")
print(moto)  # Ducati Desmosedici GP25 - 275 HP
```

### Sistema de telemetría
```python
from python_racing.telemetria.sensores.temperatura_motor_sensor import TemperaturaMotorSensor

sensor = TemperaturaMotorSensor()
sensor.start()
# Sensor corre en thread daemon
```

## 📝 Licencia

MIT License - Proyecto educativo

---

**Versión**: 1.0.0  
**Python**: 3.13+  
**Autor**: PythonRacing Contributors