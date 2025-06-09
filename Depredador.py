# Depredador.py
from Individuo import Individuo

class Depredador(Individuo):
    def actuar(self, ambiente):
        if self.energia < 10:
            self.buscar_comida(ambiente)
        else:
            self.descansar()

    def buscar_comida(self, ambiente):
        print(f"{self} busca comida en {ambiente}")
        # Simula búsqueda

    def descansar(self):
        print(f"{self} descansa")
        self.energia += 5
