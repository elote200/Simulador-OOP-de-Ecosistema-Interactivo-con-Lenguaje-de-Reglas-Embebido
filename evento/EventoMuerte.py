from .Evento import Evento

class EventoMuerte(Evento):
    """
    Evento que representa la muerte de un agente en el ambiente.
    Este evento se desencadena cuando un individuo cumple con las condiciones de muerte definidas en las reglas.
    """
    
    def __init__(self, nCiclo, individuo):
        super().__init__(nCiclo, f"Un {individuo.especie.simbolo} ha muerto.")
        self.individuo = individuo

    def evaluar(self, ambiente):
        return ambiente.ciclo >= self.nCiclo

    def ejecutar(self, ambiente):
        """
        Ejecuta el evento de muerte del individuo en el ambiente.
        """
        ambiente.eliminarIndividuo(self.individuo)

    def __str__(self):
        return f"EventoMuerte: {self.descripcion} (Ciclo {self.nCiclo})"
    
    def __repr__(self):
        return self.__str__()