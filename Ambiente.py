from Individuo import Estado

class Ambiente:
    def __init__(self, nombre, ancho, alto):
        self.nombre = nombre 

        self.ciclo = 0
        self.ancho = ancho
        self.alto = alto
        self.individuos = []
        self.hierbas = []

        self.generarHierba()
        self.generarHierba()
        self.generarHierba()
        self.generarHierba()


        self.eventos = []


    def agregarEvento(self, evento):
        self.eventos.append(evento)

    def ejecutarEventos(self):
        for evento in self.eventos:
            if evento.evaluar(self):
                evento.ejecutar(self)
                self.eventos.remove(evento)  # Eliminar el evento una vez ejecutado
        return
    
    def eliminarEventos(self):
        self.eventos.clear()
        return

    def eliminarIndividuos(self):
        self.individuos.clear()
        return

    def eliminarIndividuo(self, individuo):
        if individuo in self.individuos:
            self.individuos.remove(individuo)
        else:
            print(f"El individuo {individuo} no se encuentra en el ambiente {self.nombre}.")
        return

    def agregar_individuo(self, individuo):
        self.individuos.append(individuo)
    
    def generarHierba(self):
        from random import randint
        x = randint(0, self.ancho - 1)
        y = randint(0, self.alto - 1)
        while self.hayColision(x, y):
            x = randint(0, self.ancho - 1)
            y = randint(0, self.alto - 1)
        self.hierbas.append((x, y))
        
    def estaEnLimites(self, x, y):
        return 0 <= x < self.ancho and 0 <= y < self.alto

    def hayColision(self, x, y):
        for individuo in self.individuos:
            if individuo.x == x and individuo.y == y:
                return True
        return False

    def mostrar(self):

        from Individuo import Estado
        matriz = [[' * ' for _ in range(self.ancho)] for _ in range(self.alto)]
        for individuo in self.individuos:
            if individuo.estado == Estado.MUERTO:
                matriz[individuo.y][individuo.x] = '💀'
            else:
                matriz[individuo.y][individuo.x] = f'{individuo.especie.simbolo}'
            

        for x, y in self.hierbas:
            if 0 <= x < self.ancho and 0 <= y < self.alto:
                matriz[y][x] = '🌴'

        print(f"Ambiente: {self.nombre}, Ciclo: {self.ciclo}")

        for fila in matriz:
            print("".join(f"{celda:2}" for celda in fila))

    def actualizarIndividuos(self):
        for ind in self.individuos:
            ind.actualizar(self)

    def encontarHierbaMasCercana(self, individuo):
        hierbaCercana = None
        
        distanciaMinima = float('inf')
        for x, y in self.hierbas:
            distancia = abs(individuo.x - x) + abs(individuo.y - y)
            if distancia < distanciaMinima:
                distanciaMinima = distancia
                hierbaCercana = (x, y)
                
        return hierbaCercana

    def encontrarPresaMasCercana(self, individuo):
        presaCercana = None
        distanciaMinima = float('inf')  # Establecemos una distancia infinita al principio
        
        for otro_individuo in self.individuos:
            # Verificamos si el otro individuo es una presa (debe ser un individuo diferente y estar vivo)
            if otro_individuo != individuo and otro_individuo.estado == Estado.VIVO and otro_individuo.especie != individuo.especie:
                # Calculamos la distancia entre el cazador y la presa
                distancia = abs(individuo.x - otro_individuo.x) + abs(individuo.y - otro_individuo.y)
                
                # Si la distancia es menor que la mínima encontrada hasta ahora, actualizamos la presa más cercana
                if distancia < distanciaMinima:
                    distanciaMinima = distancia
                    presaCercana = otro_individuo

        return presaCercana
        
    def encontrarDepredadorMasCercano(self, individuo): #Para que el individuo se aleje del depredador mas cercano
        depredadorCercano = None
        
        pass
    
    def encontrarParejaMasCercana(self, individuo): #Para que el individuo se mueva hacia la pareja mas cercana
        parejaCercana = None
        
        distanciaMinima = float('inf')
        for otro_individuo in self.individuos:
            if otro_individuo != individuo and otro_individuo.estaBuscandoPareja():
                distancia = abs(individuo.x - otro_individuo.x) + abs(individuo.y - otro_individuo.y)
                if distancia <= distanciaMinima:
                    distanciaMinima = distancia
                    parejaCercana = otro_individuo

        return parejaCercana
        
    def actualizar(self):
        self.actualizarIndividuos()
        self.ejecutarEventos()
        self.ciclo += 1

    def obtenerResumenIndividuos(self):
        resumen = []

        for individuo in self.individuos:
            info = {
                "id": id(individuo),  # ID único del objeto en memoria
                "especie": individuo.especie.nombre if individuo.especie else "Desconocida",
                "posicion": (individuo.x, individuo.y),
                "estado": individuo.estado.name if hasattr(individuo.estado, "name") else str(individuo.estado),
                "energia": getattr(individuo, "energia", "N/D"),
                "edad": getattr(individuo, "edad", "N/D"),
                "reproduciendo": individuo.estaBuscandoPareja() if hasattr(individuo, "estaBuscandoPareja") else "N/D"
            }
            resumen.append(info)

        return resumen
        