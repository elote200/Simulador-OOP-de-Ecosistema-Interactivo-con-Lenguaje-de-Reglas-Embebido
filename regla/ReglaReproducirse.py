from .Regla import Regla
from Individuo import Estado
from evento.EventoReproduccion import EventoReproduccion

class ReglaReproducirse(Regla):

    def calDistancia(self, i1, i2):
        return ((i1.x - i2.x) ** 2 + (i1.y - i2.y) ** 2) ** 0.5
    
    def __init__(self, condiciones, operadores_logicos):
        super().__init__(condiciones, operadores_logicos)
    
    def evaluar(self, individuo):
        e = super().evaluar(individuo)
        if not e:
            individuo.estado = Estado.VIVO 
        return e


        
    def ejecutar(self, individuo, ambiente):
        if individuo.estaReproduciendose():
            return

        individuo.estado = Estado.BUSCANDO_PAREJA
        pareja = ambiente.encontrarParejaMasCercana(individuo)

        if pareja is None:
            return
        
        if self.calDistancia(individuo, pareja) <= 1:
            individuo.estado = Estado.REPRODUCIENDOSE
            pareja.estado = Estado.REPRODUCIENDOSE

            # Aqui se crea un nuevo individuo, que es el hijo de los dos padres
            evento = EventoReproduccion(ambiente.ciclo + 1, individuo, pareja)
            ambiente.agregarEvento(evento)
            
    def __str__(self):
        cadena = self.condiciones[0]['atributo'] + " " + self.condiciones[0]['operador'] + " " + str(self.condiciones[0]['valor'])
        if len(self.condiciones) > 1:
            for i in range(1, len(self.condiciones)):
                cadena += " " + self.operadores_logicos[i-1] + " " + self.condiciones[i]['atributo'] + " " + self.condiciones[i]['operador'] + " " + str(self.condiciones[i]['valor'])
        return f"ReglaReproducirse: {cadena}"
    
# This code defines a rule for reproduction in a simulation environment, allowing individuals to find partners and reproduce based on specified conditions. It inherits from a base class `Regla` and implements the logic for checking conditions and executing reproduction events. The string representation method provides a readable format of the rule's conditions.

        
        