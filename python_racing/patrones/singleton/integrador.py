"""
Archivo integrador generado automaticamente
Directorio: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/singleton
Fecha: 2025-11-04 22:18:17
Total de archivos integrados: 2
"""

# ================================================================================
# ARCHIVO 1/2: __init__.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/singleton/__init__.py
# ================================================================================



# ================================================================================
# ARCHIVO 2/2: singleton.py
# Ruta: /home/facundo/Escritorio/Proyecto_Diseno_de_Sistemas/PythonRacing/python_racing/patrones/singleton/singleton.py
# ================================================================================


from threading import Lock
from typing import Any, Callable


def singleton(cls: type) -> Callable:
    instances = {}
    lock = Lock()
    
    def get_instance(*args: Any, **kwargs: Any) -> Any:
        """Retorna la instancia única (thread-safe)."""
        if cls not in instances:
            with lock:  # Thread-safe
                if cls not in instances:  # Double-checked locking
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

