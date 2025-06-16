from motor_regla.parser import parsearJson
import os
import sys
import time

from random import random

from Ambiente import Ambiente
from Comportamiento import Comportamiento
from Individuo import Individuo

from Especie import Especie

def cargarJson():
    if len(sys.argv) < 2:
        print("Uso: python mi_script.py archivo.json")
        return

    archivo = sys.argv[1]

    #Este if ayuda a verificar si es .json la extension sino lo matamos.
    if not archivo.lower().endswith('.json'):
        print("Error: El archivo debe tener extensión .json")
        return

    #Solo verifica si el archivo mandado existe en si
    if not os.path.isfile(archivo):
        print(f"Error: El archivo '{archivo}' no existe.")
        return

    try:
       return parsearJson(archivo)
    except Exception as e:
        print(f"Error al procesar el archivo JSON: {e}")
        return

def main():

    # Cargar las reglas desde el archivo JSON
    reglas = cargarJson()
    
    ambiente = Ambiente("Bosque", 40, 30)

    # Definimos algunas especies con sus comportamientos
    leon = Especie("Leon",'🦁', 40, Comportamiento(reglas[0]['reglas']))
    cebra = Especie("Cebra", '🦓', 30, Comportamiento(reglas[1]['reglas']))
    zorro = Especie("Zorro", '🦊', 20, Comportamiento(reglas[2]['reglas']))
    conejo = Especie("Conejo", '🐇', 10, Comportamiento(reglas[3]['reglas']))
    venado = Especie("Venado", '🦌', 25, Comportamiento(reglas[4]['reglas']))
    tigre = Especie("Tigre", '🐯', 50, Comportamiento(reglas[5]['reglas']))


    # Creamos algunos individuos de diferentes especies
    # y les asignamos energía inicial
    # para probar los eventos y reglas

    c1 = Individuo(10, 10, cebra)
    c1.energia = 100
    c1.edad = 50
    c2 = Individuo(30, 12, cebra)
    c2.energia = 100 
    c2.edad = 30

    con1 = Individuo(5, 5, conejo)
    con1.edad = 30

    con2 = Individuo(15, 2, conejo)
    con2.edad = 18

    # Agregamos individuos al ambiente
    """
    ambiente.agregar_individuo(Individuo(3, 4, leon))
    ambiente.agregar_individuo(Individuo(5, 4, leon))
    ambiente.agregar_individuo(Individuo(2, 4, leon))

    ambiente.agregar_individuo(Individuo(10, 2, tigre))
    ambiente.agregar_individuo(Individuo(9, 15, zorro))
    ambiente.agregar_individuo(Individuo(15, 9, conejo))

    ambiente.agregar_individuo(Individuo(5, 5, cebra))
    ambiente.agregar_individuo(Individuo(3, 3, venado))

    """
    ambiente.agregar_individuo(c1)
    ambiente.agregar_individuo(c2)

    ambiente.agregar_individuo(con1)
    ambiente.agregar_individuo(con2)

    
    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            ambiente.mostrar()
            ambiente.actualizar()

            print(con1)
            print(con2)
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            break


main()
