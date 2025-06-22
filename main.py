from motor_regla.parser import parsearJson
import os
import sys
import time
import json
from random import random
from Ambiente import Ambiente
from Comportamiento import Comportamiento
from Individuo import Individuo
from Especie import Especie

global leon, cebra, zorro, conejo, venado, tigre
global ambiente

# Variable para simular diferentes comportamientos
# 1: Cazar, 2: Reproducir, 3: Morir, 4: Simulación completa
simulacion = 4

def crearJSON(ambiente):
    data = {
        "ciclo": ambiente.ciclo,
        "ancho": ambiente.ancho,
        "alto": ambiente.alto,
        "individuos": ambiente.obtenerResumenIndividuos(),
        "hierbas": ambiente.hierbas
    }

    with open("estado_ambiente.json", "w") as archivo_json:
        json.dump(data, archivo_json, indent=4)

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

def cargarEspecies():
    global leon, cebra, zorro, conejo, venado, tigre
    global ambiente
    
    ambiente = Ambiente("Selva", 40, 30)  
    # Cargar las reglas desde el archivo JSON
    reglas = cargarJson()

    # Definimos algunas especies con sus comportamientos
    leon = Especie("Leon",'🦁', 40, Comportamiento(reglas[0]['reglas']))
    cebra = Especie("Cebra", '🦓', 30, Comportamiento(reglas[1]['reglas']))
    zorro = Especie("Zorro", '🦊', 20, Comportamiento(reglas[2]['reglas']))
    conejo = Especie("Conejo", '🐇', 10, Comportamiento(reglas[3]['reglas']))
    venado = Especie("Venado", '🦌', 25, Comportamiento(reglas[4]['reglas']))
    tigre = Especie("Tigre", '🐯', 50, Comportamiento(reglas[5]['reglas']))

# Definimos unas simulaciones

def simularCazar():
    c1 = Individuo(20, 10, cebra)
    c1.energia = 80
    c1.edad = 15

    l1 = Individuo(9, 10, leon)
    l1.energia = 30 
    l1.edad = 30

    ambiente.agregar_individuo(c1)
    ambiente.agregar_individuo(l1)
    pass

def simularReproducir():
    conejo1 = Individuo(5, 5, conejo)
    conejo2 = Individuo(9, 15, conejo)

    conejo1.energia = 100
    conejo2.energia = 100
    
    conejo1.edad = 30
    conejo2.edad = 20

    ambiente.agregar_individuo(conejo1)
    ambiente.agregar_individuo(conejo2)
    
    pass

def simularMorir():

    zebra1 = Individuo(10, 10, cebra)
    zebra2 = Individuo(15, 15, cebra)
    
    zebra1.energia = 10  # Simulamos que este individuo muere por falta de energia

    zebra2.energia = 50  # Este individuo sobrevive
    zebra2.edad = 75

    ambiente.agregar_individuo(zebra1)
    ambiente.agregar_individuo(zebra2)
    
    pass

def simulacionCompleta():
    # Simulación completa con todas las especies
    leon1 = Individuo(25, 20, leon)
    leon1.energia = 100
    leon1.edad = 50
    cebra1 = Individuo(20, 15, cebra)
    cebra1.energia = 80
    cebra1.edad = 40

    cebra2 = Individuo(30, 20, cebra)
    cebra2.energia = 90
    cebra2.edad = 45

    cebra3 = Individuo(18, 12, cebra)
    cebra3.energia = 70
    cebra3.edad = 35

    
    zorro1 = Individuo(15, 10, zorro)
    zorro1.energia = 60
    zorro1.edad = 30
    
    conejo1 = Individuo(5, 5, conejo)
    conejo1.energia = 50
    conejo1.edad = 20

    conejo2 = Individuo(20, 11, conejo)
    conejo2.energia = 55
    conejo2.edad = 22
    
    venado1 = Individuo(25, 15, venado)
    venado1.energia = 70
    venado1.edad = 35
    
    tigre1 = Individuo(38, 28, tigre)
    tigre1.energia = 90
    tigre1.edad = 60
    
    ambiente.agregar_individuo(leon1)
    ambiente.agregar_individuo(cebra1)
    ambiente.agregar_individuo(cebra2)
    ambiente.agregar_individuo(cebra3)
    ambiente.agregar_individuo(zorro1)
    ambiente.agregar_individuo(conejo1)
    ambiente.agregar_individuo(conejo2)
    ambiente.agregar_individuo(venado1)
    ambiente.agregar_individuo(tigre1)
    

def main(e):
    
    match e:
        case 1:
            simularCazar()
        case 2:
            simularReproducir()
        case 3:
            simularMorir()
        case 4:
            simulacionCompleta()

    while True:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            ambiente.mostrar()
            ambiente.actualizar()
            if(ambiente.ciclo % 2 == 0):
                crearJSON(ambiente)
            time.sleep(1)
        except KeyboardInterrupt:
            print("\nSaliendo del programa...")
            break

cargarEspecies()
main(simulacion)

    
