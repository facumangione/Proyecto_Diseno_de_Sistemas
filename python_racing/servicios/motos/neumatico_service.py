from python_racing.entidades.motos.neumatico import Neumatico, TipoNeumatico


class NeumaticoService:
    def crear_juego_neumaticos(self, tipo: TipoNeumatico) -> tuple[Neumatico, Neumatico]:
        delantero = Neumatico(tipo)
        trasero = Neumatico(tipo)
        return delantero, trasero

    def verificar_estado_neumatico(self, neumatico: Neumatico) -> dict:
        desgaste = neumatico.get_desgaste()
        
        if desgaste >= 80:
            return {
                'estado': 'CRITICO',
                'mensaje': f'⚠️ Neumático MUY gastado ({desgaste:.1f}%) - CAMBIAR YA',
                'requiere_cambio': True
            }
        elif desgaste >= 60:
            return {
                'estado': 'ALERTA',
                'mensaje': f'⚠️ Neumático gastado ({desgaste:.1f}%) - Considerar cambio',
                'requiere_cambio': False
            }
        elif desgaste >= 40:
            return {
                'estado': 'USADO',
                'mensaje': f'Neumático usado ({desgaste:.1f}%) - Rendimiento óptimo',
                'requiere_cambio': False
            }
        else:
            return {
                'estado': 'NUEVO',
                'mensaje': f'✓ Neumático nuevo ({desgaste:.1f}%)',
                'requiere_cambio': False
            }

    def recomendar_tipo_neumatico(self, condicion: str) -> TipoNeumatico:
        recomendaciones = {
            'seco': TipoNeumatico.SLICK,
            'humedo': TipoNeumatico.INTERMEDIO,
            'lluvia': TipoNeumatico.LLUVIA
        }
        
        return recomendaciones.get(
            condicion.lower(),
            TipoNeumatico.INTERMEDIO  # Default seguro
        )