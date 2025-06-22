from .Evento import Evento
from Individuo import Estado

class EventoCaza(Evento):
    """
    Evento que representa la caza de un individuo por otro.
    Este evento se ejecuta cuando un cazador encuentra a su presa y la caza.
    """
    
    def __init__(self, nCiclo, cazador, presa):
        super().__init__(nCiclo, f"El {cazador.especie.simbolo} ha cazado a {presa.especie.simbolo}.")
        self.cazador = cazador
        self.presa = presa

    def evaluar(self, ambiente):
        """
        Evalúa si el evento de caza debe ejecutarse.
        """
        return ambiente.ciclo >= self.nCiclo

    def ejecutar(self, ambiente):
        """
        Ejecuta la caza, eliminando la presa y modificando el estado del cazador.
        """
        # El cazador gana algo de energía
        self.cazador.energia = 100 # Asignar energía máxima al cazador
        self.cazador.estado = Estado.VIVO
        # Elimina a la presa del ambiente
        ambiente.eliminarIndividuo(self.presa)
        
    def __str__(self):
        return f"EventoCaza: {self.descripcion} (Ciclo {self.nCiclo})"
    
    def __repr__(self):
        return self.__str__()
