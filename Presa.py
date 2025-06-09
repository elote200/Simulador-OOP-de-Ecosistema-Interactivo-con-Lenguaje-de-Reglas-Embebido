# Presa.py
from Individuo import Individuo

class Presa(Individuo):
    def actuar(self, ambiente):
        if self.energia < 10:
            self.huir()
        else:
            self.reproducirse()

    def huir(self):
        print(f"{self} huye")
        # Simula escape

    def reproducirse(self):
        print(f"{self} se reproduce")
        # Simula reproducción
