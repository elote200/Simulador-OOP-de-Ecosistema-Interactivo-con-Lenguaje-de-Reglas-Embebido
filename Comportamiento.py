
class Comportamiento:
    def __init__(self,  reglas = None):
        self.reglas = reglas

    def ejecutar(self, individuo, ambiente):
        if self.reglas is None:
            return
        
        for regla in self.reglas:
            if(regla.evaluar(individuo)):
                regla.ejecutar(individuo, ambiente)
    
    def agregarRegla(self, regla):
        if self.reglas is None:
            self.reglas = []
        self.reglas.append(regla)

    def limpiarReglas(self):
        if self.reglas is not None:
            self.reglas = []

    def __str__(self):
        return f"Comportamiento:{self.reglas}"