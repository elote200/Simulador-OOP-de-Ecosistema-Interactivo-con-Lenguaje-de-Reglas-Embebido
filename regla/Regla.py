from abc import ABC, abstractmethod

class Regla(ABC):
    """
    Clase abstracta que define una regla para los individuos en un ambiente.
    Las subclases deben implementar el método `ejecutar`.
    """

    def __init__(self, condiciones, operadores_logicos):    
        self.condiciones = condiciones
        self.operadores_logicos = operadores_logicos
        
    def evaluarCondicion(self, variable, operador, valorComparado) -> bool:
        match operador:
            case "==":
                return variable == valorComparado
            case "!=":
                return variable != valorComparado
            case "<":
                return variable < valorComparado
            case "<=":
                return variable <= valorComparado
            case ">":
                return variable > valorComparado
            case ">=":
                return variable >= valorComparado
            case _:
                raise ValueError(f"Operador desconocido: {operador}")


    def evaluar(self, individuo) -> bool:

        if not self.condiciones:
            raise ValueError("No se han definido condiciones para la regla.")
        
        # Evaluar la primera condición
        variable = self.condiciones[0]['atributo']
        operador = self.condiciones[0]['operador']
        valorComparado = self.condiciones[0]['valor']    

        atr = getattr(individuo, variable)

        result = self.evaluarCondicion(atr, operador, valorComparado)

        for i in range(1, len(self.condiciones)):
            variable = self.condiciones[i]['atributo']
            operador = self.condiciones[i]['operador']
            valorComparado = self.condiciones[i]['valor']

            atr = getattr(individuo, variable)

            operadorCondiciones = self.operadores_logicos[i-1]

            if operadorCondiciones == "&&":
                result = result and self.evaluarCondicion(atr, operador, valorComparado)
            elif operadorCondiciones == "||":
                result = result or self.evaluarCondicion(atr, operador, valorComparado)
            else:
                raise ValueError(f"Operador lógico desconocido: {operadorCondiciones}")
            
        return result
                
    @abstractmethod 
    def ejecutar(self, individuo, ambiente):
       pass 