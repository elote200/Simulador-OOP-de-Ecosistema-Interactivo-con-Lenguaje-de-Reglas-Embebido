from .Regla import Regla
from Individuo import Estado
from evento.EventoCaza import EventoCaza

class ReglaCaza(Regla):
    def calDistancia(self, i1, i2):
        """
        Calcula la distancia entre dos individuos en el ambiente.
        Usamos la distancia de Manhattan para la simulación.
        """
        return ((i1.x - i2.x) ** 2 + (i1.y - i2.y) ** 2) ** 0.5

    def __init__(self, condiciones, operadores_logicos):
        super().__init__(condiciones, operadores_logicos)

    def evaluar(self, individuo):
        """
        Evalúa si el individuo cumple con las condiciones para empezar a cazar.
        Si está vivo y las condiciones se cumplen, cambia el estado a BUSCANDO_ALIMENTO.
        """
        e = super().evaluar(individuo)
        if e and individuo.estado != Estado.MUERTO:
            # Si las condiciones se cumplen y el individuo está vivo, empieza a buscar una presa.
            individuo.estado = Estado.BUSCANDO_ALIMENTO
        return e

    def ejecutar(self, individuo, ambiente):
        """
        Ejecuta la acción de caza.
        El individuo busca la presa más cercana, se mueve hacia ella y la caza si está cerca.
        """
        if individuo.estado != Estado.BUSCANDO_ALIMENTO:
            return  # Si no está buscando presa, no hace nada

        # Buscar la presa más cercana
        presa = ambiente.encontrarPresaMasCercana(individuo)

        if presa is None:
            return  # Si no hay presas cercanas, termina la ejecución

        # Si está cerca de la presa (distancia Manhattan <= 1)
        if self.calDistancia(individuo, presa) <= 1:
            print(f'lo va a cazar')
            # Si el individuo está cerca de la presa, cambia su estado a Cazando
            individuo.estado = Estado.CAZANDO
            presa.estado = Estado.MUERTO  # La presa muere

            # Crear un evento de caza, que se ejecutará en el siguiente ciclo
            evento = EventoCaza(ambiente.ciclo + 1, individuo, presa)
            ambiente.agregarEvento(evento)

    def __str__(self):
        """
        Representación en cadena de la regla de caza.
        """
        cadena = self.condiciones[0]['atributo'] + " " + self.condiciones[0]['operador'] + " " + str(self.condiciones[0]['valor'])
        if len(self.condiciones) > 1:
            for i in range(1, len(self.condiciones)):
                cadena += " " + self.operadores_logicos[i-1] + " " + self.condiciones[i]['atributo'] + " " + self.condiciones[i]['operador'] + " " + str(self.condiciones[i]['valor'])
        return f"ReglaCazar: {cadena}"

