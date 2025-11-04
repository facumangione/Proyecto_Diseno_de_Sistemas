
from typing import Generic, TypeVar, List, TYPE_CHECKING
from abc import ABC

if TYPE_CHECKING:
    from python_racing.patrones.observer.observer import Observer

T = TypeVar('T')


class Observable(Generic[T], ABC):
    def __init__(self):
        # ✅ Usar string literal para el tipo
        self._observadores: List['Observer[T]'] = []

    def agregar_observador(self, observador: 'Observer[T]') -> None:
        """Agrega un observador a la lista."""
        if observador not in self._observadores:
            self._observadores.append(observador)

    def eliminar_observador(self, observador: 'Observer[T]') -> None:
        """Elimina un observador de la lista."""
        if observador in self._observadores:
            self._observadores.remove(observador)

    def notificar_observadores(self, evento: T) -> None:
        """Notifica a todos los observadores."""
        for observador in self._observadores:
            observador.actualizar(evento)