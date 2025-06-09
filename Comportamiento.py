# Comportamiento.py

class ComportamientoBuscarAlimento:
    def ejecutar(self, individuo, ambiente):
        print(f"{individuo} ejecuta: buscar alimento")
        individuo.energia += 10

class ComportamientoHuir:
    def ejecutar(self, individuo, ambiente):
        print(f"{individuo} ejecuta: huir")
        individuo.mover((individuo.posicion[0] + 1, individuo.posicion[1] + 1))
