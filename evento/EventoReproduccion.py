from .Evento import Evento
from Individuo import Individuo, Estado

class EventoReproduccion(Evento):
    """
    Evento que representa la reproduccion de un agente en el ambiente.
    Este evento se desencadena cuando un individuo cumple con las condiciones de reproduccion definidas en las reglas.
    """
    
    def __init__(self, nCiclo, padre, madre):
        super().__init__(nCiclo, f"Un {padre.especie.simbolo} y una {madre.especie.simbolo} han reproducido.")
        self.padre = padre
        self.madre = madre

    def evaluar(self, ambiente):
        return ambiente.ciclo >= self.nCiclo


    def ejecutar(self, ambiente):
        """
        Ejecuta el evento de reproduccion del individuo en el ambiente.
        """

        if self.padre.energia < self.padre.especie.energiaReproducion or self.madre.energia < self.madre.especie.energiaReproducion:
            print(f"El {self.padre.especie.simbolo} o el {self.madre.especie.simbolo} no tienen suficiente energia para reproducirse.")
            self.padre.estado = Estado.VIVO
            self.madre.estado = Estado.VIVO
            return
        
        # Crear un nuevo individuo como hijo de los padres
        hijo = Individuo(self.padre.x, self.padre.y, self.padre.especie)

        ambiente.agregar_individuo(hijo)

        self.padre.energia -= self.padre.especie.energiaReproducion
        self.madre.energia -= self.madre.especie.energiaReproducion

        self.padre.estado = Estado.VIVO
        self.madre.estado = Estado.VIVO




        