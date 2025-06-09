# Regla.py

class Regla:
    def __init__(self, condicion, comportamiento):
        self.condicion = condicion  # e.g. "individuo.energia < 10"
        self.comportamiento = comportamiento

    def se_cumple(self, individuo):
        try:
            return eval(self.condicion, {}, {"individuo": individuo})
        except Exception:
            return False

    def ejecutar(self, individuo, ambiente):
        self.comportamiento.ejecutar(individuo, ambiente)
