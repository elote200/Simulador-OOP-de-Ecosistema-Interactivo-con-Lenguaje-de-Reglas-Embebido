from enum import Enum
import random

class Estado(Enum):
    VIVO = 1
    MUERTO = 2
    CAMINANDO = 3
    CAZANDO = 4
    BUSCANDO_ALIMENTO = 5
    REPRODUCIENDOSE = 6
    BUSCANDO_PAREJA = 7

class Individuo:
    def __init__(self, x, y, especie):
        self.especie = especie
        # Especie
        self.energia = 100
        self.edad = 0
        self.estado = Estado.VIVO
        
        # Posicion
        self.x = x
        self.y = y

    def moverse(self, ambiente):

        if(self.estado == Estado.MUERTO or self.estado == Estado.REPRODUCIENDOSE or self.estado == Estado.CAZANDO):
            return
        dx, dy = random.choice([(0, 1), (1, 0), (0, -1), (-1, 0)])  

        if self.estado == Estado.BUSCANDO_PAREJA:
            pareja = ambiente.encontrarParejaMasCercana(self)
            if pareja is not None:
                dx = pareja.x - self.x
                dy = pareja.y - self.y
                if abs(dx) > abs(dy):
                    dx = 1 if dx > 0 else -1
                else:
                    dy = 1 if dy > 0 else -1 
        elif self.estado == Estado.BUSCANDO_ALIMENTO:
            presa = ambiente.encontrarPresaMasCercana(self)
            if presa is not None:
                dx = presa.x - self.x
                dy = presa.y - self.y
                if abs(dx) > abs(dy):
                    dx = 1 if dx > 0 else -1
                else:
                    dy = 1 if dy > 0 else -1

        nueva_x = self.x + dx
        nueva_y = self.y + dy

        # Hay que hacer otra logica para si el individuo se mueve a una posicion donde hay hierba o hacia una presa, o encontra pareja

        if ambiente.estaEnLimites(nueva_x, nueva_y) and not ambiente.hayColision(nueva_x, nueva_y):
            self.x = nueva_x
            self.y = nueva_y

            # Mientras esta buscando pareja, no gasta energia, simulado
            if self.estado == Estado.BUSCANDO_PAREJA:
                return
            self.energia -= 1  # Moverse consume energia
            



    def estaVivo(self):
        return self.estado == Estado.VIVO

    def estaReproduciendose(self):
        return self.estado == Estado.REPRODUCIENDOSE

    def estaBuscandoPareja(self):
        return self.estado == Estado.BUSCANDO_PAREJA
    
    def buscarAlimento(self, ambiente):
        pass
    
    def cazar(self, ambiente):
        return self.estado == Estado.CAZANDO

    def morir(self):
        self.estado = Estado.MUERTO
        pass
    
    def actualizar(self, ambiente):
        self.especie.ejecutarComportamiento(self, ambiente)
        self.moverse(ambiente)

        self.edad += 1


    def __str__(self):
        return f"Individuo(Posicion: [{self.x}, {self.y}], {self.especie.nombre}, Energia: {self.energia}, Edad: {self.edad}, Estado: {self.estado})"
        

        
    



    