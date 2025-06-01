from motor_regla.parser import parsear_regla
import os
import json
import sys

def main():
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
        with open(archivo, 'r', encoding='utf-8') as f:
            ambientes = json.load(f)
        #Verifica si se inicio el .json con [{"Ambiente": {...}}]
        if not isinstance(ambientes, list):
            print("Error: El JSON debe iniciar con [ ]")
            return

        #Iteracion de ambientes para reglas y demas (Supongo que aqui guardaremos las especies, individuos, y ambientes)
        #Para la iteracion se ocupa crear variables de la (key[llave o nombre de la variable que tiene el json] y su valor)
        for i, ambiente in enumerate(ambientes):
            #Agarra cada ambiente
            for nombre_ambiente, animales in ambiente.items():
                print(f"\n🌿 Ambiente #{i + 1} - {nombre_ambiente}")
                #Agarra cada animal
                for animal, info in animales.items():
                    #Agarra las reglas
                    print(f"\n🫎  Animal - {animal} del ambiende {nombre_ambiente}")
                    for regla in info.get("reglas", []):
                        try:
                            resultado = parsear_regla(regla)
                            print("Regla parseada correctamente:")
                            print(resultado)
                            print("\n")

                        except SyntaxError as e:
                            print(f"Error de sintaxis: {e}\n")
    except json.JSONDecodeError:
        print("Error: El archivo no contiene un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")

main()
