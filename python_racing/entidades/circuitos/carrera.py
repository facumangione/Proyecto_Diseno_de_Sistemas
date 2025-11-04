from typing import TYPE_CHECKING
from datetime import date

if TYPE_CHECKING:
    from python_racing.entidades.circuitos.circuito import Circuito
    from python_racing.entidades.escuderias.corredor import Corredor


class ResultadoCarrera:

    def __init__(
        self,
        corredor: 'Corredor',
        posicion: int,
        tiempo_total: float,
        vueltas_completadas: int,
        abandono: bool = False
    ):
        self._corredor = corredor
        self._posicion = posicion
        self._tiempo_total = tiempo_total
        self._vueltas_completadas = vueltas_completadas
        self._abandono = abandono

    # Getters
    def get_corredor(self) -> 'Corredor':
        return self._corredor

    def get_posicion(self) -> int:
        return self._posicion

    def get_tiempo_total(self) -> float:
        return self._tiempo_total

    def get_vueltas_completadas(self) -> int:
        return self._vueltas_completadas

    def es_abandono(self) -> bool:
        return self._abandono

    def obtener_tiempo_formateado(self) -> str:
        """
        Formatea el tiempo total como MM:SS.
        
        Returns:
            String con formato de tiempo
        """
        minutos = int(self._tiempo_total // 60)
        segundos = int(self._tiempo_total % 60)
        return f"{minutos}m {segundos}s"

    def __str__(self) -> str:
        estado = "ABANDONO" if self._abandono else "COMPLETÓ"
        return (
            f"P{self._posicion}. {self._corredor.get_nombre()} - "
            f"{self.obtener_tiempo_formateado()} - {estado}"
        )


class Carrera:

    def __init__(
        self,
        circuito: 'Circuito',
        fecha: date,
        vueltas: int
    ):
       
        if vueltas <= 0:
            raise ValueError("El número de vueltas debe ser mayor a 0")
        
        self._circuito = circuito
        self._fecha = fecha
        self._vueltas = vueltas
        self._corredores_participantes: list['Corredor'] = []
        self._resultados: list[ResultadoCarrera] = []
        self._finalizada = False

    # Getters
    def get_circuito(self) -> 'Circuito':
        return self._circuito

    def get_fecha(self) -> date:
        return self._fecha

    def get_vueltas(self) -> int:
        return self._vueltas

    def get_corredores_participantes(self) -> list['Corredor']:
        return self._corredores_participantes.copy()

    def get_resultados(self) -> list[ResultadoCarrera]:
        return self._resultados.copy()

    def esta_finalizada(self) -> bool:
        return self._finalizada

    # Métodos de negocio
    def agregar_corredor(self, corredor: 'Corredor') -> None:
        """Agrega un corredor a la carrera."""
        if corredor not in self._corredores_participantes:
            self._corredores_participantes.append(corredor)

    def registrar_resultado(self, resultado: ResultadoCarrera) -> None:
        """Registra el resultado de un corredor."""
        self._resultados.append(resultado)

    def finalizar_carrera(self) -> None:
        """Marca la carrera como finalizada y ordena resultados."""
        self._finalizada = True
        # Ordenar por posición
        self._resultados.sort(key=lambda r: r.get_posicion())

    def obtener_ganador(self) -> ResultadoCarrera:
        """
        Obtiene el ganador de la carrera.
        
        Returns:
            Resultado del ganador (posición 1)
        
        Raises:
            ValueError: Si la carrera no ha finalizado
        """
        if not self._finalizada:
            raise ValueError("La carrera no ha finalizado")
        if not self._resultados:
            raise ValueError("No hay resultados registrados")
        
        return self._resultados[0]

    def obtener_podio(self) -> list[ResultadoCarrera]:
        """
        Obtiene el podio (3 primeros lugares).
        
        Returns:
            Lista con los 3 primeros resultados
        """
        if not self._finalizada:
            raise ValueError("La carrera no ha finalizado")
        
        return self._resultados[:3]

    def __str__(self) -> str:
        estado = "FINALIZADA" if self._finalizada else "EN CURSO"
        return (
            f"Carrera en {self._circuito.get_nombre()} - "
            f"{self._fecha} - {self._vueltas} vueltas - {estado}"
        )