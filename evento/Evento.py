from abc import ABC, abstractmethod

class Evento(ABC):
    """
    Clase abstracta que define un evento en un ambiente.
    Las subclases deben implementar el método `ejecutar`.
    """
    
    def __init__(self, nCiclo, descripcion):
        self.nCiclo = nCiclo  # Ciclo en el que ocurre el evento
        self.descripcion = descripcion  # Descripción del evento

    @abstractmethod
    def evaluar(self, ambiente):
        """
        Método abstracto que debe ser implementado por las subclases.
        Este método se utiliza para evaluar si el evento debe ejecutarse en el ambiente.
        """
        pass
        
    @abstractmethod
    def ejecutar(self, ambiente):
        """
        Método abstracto que debe ser implementado por las subclases.
        """
        pass

    def __str__(self):
        return f"Evento en el ciclo {self.nCiclo}: {self.descripcion}"
    
    def __repr__(self):
        return self.__str__()
    