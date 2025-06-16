from .Regla import Regla
from evento.EventoMuerte import EventoMuerte

class ReglaMorir(Regla):
    
    def __init__(self, condiciones, operadores_logicos):
        super().__init__(condiciones, operadores_logicos)    

    def ejecutar(self, individuo, ambiente):
        # Aqui hiria un evento dentro del ambiente que el ese individuo va a fallecer
        # El individuo muere primero y hasta dos dias despues se ejecuta el evento de muerte

        if not individuo.estaVivo():
            return
        
        individuo.morir()
        evento = EventoMuerte(ambiente.ciclo + 2, individuo)
        ambiente.agregarEvento(evento)

    def __str__(self):
        cadena = self.condiciones[0]['atributo'] + " " + self.condiciones[0]['operador'] + " " + str(self.condiciones[0]['valor']) 

        if len(self.condiciones) > 1:
            for i in range(1, len(self.condiciones)):
                cadena += " " + self.operadores_logicos[i-1] + " " + self.condiciones[i]['atributo'] + " " + self.condiciones[i]['operador'] + " " + str(self.condiciones[i]['valor'])


        return f"ReglaMorir: {cadena}"
