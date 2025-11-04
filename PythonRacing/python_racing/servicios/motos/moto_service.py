from typing import Optional
from python_racing.entidades.motos.moto import Moto
from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico
from python_racing.patrones.strategy.impl.slick_strategy import SlickStrategy
from python_racing.patrones.strategy.impl.intermedio_strategy import IntermedioStrategy
from python_racing.patrones.strategy.impl.lluvia_strategy import LluviaStrategy
from python_racing.entidades.circuitos.circuito import CondicionClimatica


class MotoService:
    def __init__(self):
        self._motos: dict[str, Moto] = {}
        self._estrategias = {
            TipoNeumatico.SLICK: SlickStrategy(),
            TipoNeumatico.INTERMEDIO: IntermedioStrategy(),
            TipoNeumatico.LLUVIA: LluviaStrategy()
        }

    def registrar_moto(self, moto: Moto) -> None:
        """Registra una moto en el sistema."""
        identificador = f"{moto.get_marca()}_{moto.get_modelo()}"
        self._motos[identificador] = moto

    def asignar_neumaticos(
        self,
        moto: Moto,
        tipo: TipoNeumatico
    ) -> tuple[Neumatico, Neumatico]:
        delantero = Neumatico(tipo)
        trasero = Neumatico(tipo)
        
        moto.set_neumatico_delantero(delantero)
        moto.set_neumatico_trasero(trasero)
        
        return delantero, trasero

    def aplicar_desgaste_neumaticos(
        self,
        moto: Moto,
        condicion: CondicionClimatica,
        longitud_km: float
    ) -> None:
        if not moto.tiene_neumaticos_instalados():
            return
        
        # Obtener tipo de neumático
        tipo = moto.get_neumatico_delantero().get_tipo()
        estrategia = self._estrategias[tipo]
        
        # Calcular desgaste
        desgaste = estrategia.calcular_desgaste(condicion, longitud_km)
        
        # Aplicar a ambos neumáticos
        moto.get_neumatico_delantero().aplicar_desgaste(desgaste)
        moto.get_neumatico_trasero().aplicar_desgaste(desgaste)
        
        # Incrementar contador de vueltas
        moto.get_neumatico_delantero().incrementar_vueltas()
        moto.get_neumatico_trasero().incrementar_vueltas()

    def verificar_compatibilidad_neumaticos(
        self,
        moto: Moto,
        condicion: CondicionClimatica
    ) -> bool:
        if not moto.tiene_neumaticos_instalados():
            return False
        
        tipo = moto.get_neumatico_delantero().get_tipo()
        estrategia = self._estrategias[tipo]
        
        return estrategia.es_compatible(condicion)