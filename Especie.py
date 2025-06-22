from Comportamiento import Comportamiento


class Especie:
    def __init__(self, nombre, simbolo, energiaReproducion, comportamiento=None):
        self.nombre = nombre
        self.simbolo = simbolo
        self.comportamiento = comportamiento if comportamiento is not None else Comportamiento()
        self.energiaReproducion = energiaReproducion

    def ejecutarComportamiento(self, individuo, ambiente):
        self.comportamiento.ejecutar(individuo, ambiente)

    def agregarRegla(self, regla):
        self.comportamiento.agregarRegla(regla)

    def limpiarReglas(self):
        self.comportamiento.limpiarReglas()

    def __str__(self):
        return f"Especie: {self.nombre}, Simbolo: {self.simbolo}, Comportamiento: {self.comportamiento}"