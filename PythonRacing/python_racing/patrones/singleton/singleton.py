
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