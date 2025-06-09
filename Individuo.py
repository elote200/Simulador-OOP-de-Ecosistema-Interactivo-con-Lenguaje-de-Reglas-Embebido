from abc import ABC, abstractmethod

class Individuo(ABC):
    def __init__(self, energia, edad, posicion):
        self.energia = energia
        self.edad = edad
        self.posicion = posicion
        self.estado = "vivo"

    def envejecer(self):
        self.edad += 1
        if self.edad > 100:  # ejemplo
            self.estado = "muerto"

    def mover(self, nueva_posicion):
        self.posicion = nueva_posicion

    @abstractmethod
    def actuar(self, ambiente):
        pass
