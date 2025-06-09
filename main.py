from motor_regla.parser import parsear_regla
import os
import json
import sys

from Depredador import Depredador
from Presa import Presa
from regla import Regla
from Comportamiento import ComportamientoBuscarAlimento, ComportamientoHuir

def main():
    if len(sys.argv) < 2:
        print("Uso: python main.py archivo.json")
        return

    archivo = sys.argv[1]

    if not archivo.lower().endswith('.json'):
        print("Error: El archivo debe tener extensión .json")
        return

    if not os.path.isfile(archivo):
        print(f"Error: El archivo '{archivo}' no existe.")
        return

    try:
        with open(archivo, 'r', encoding='utf-8') as f:
            ambientes = json.load(f)

        if not isinstance(ambientes, list):
            print("Error: El JSON debe iniciar con [ ]")
            return

        for i, ambiente in enumerate(ambientes):
            for nombre_ambiente, animales in ambiente.items():
                print(f"\n🌿 Ambiente #{i + 1} - {nombre_ambiente}")

                for animal, info in animales.items():
                    print(f"\n🫎  Animal - {animal} del ambiente {nombre_ambiente}")

                    # =========================
                    # NUEVO: Crear instancia
                    # =========================

                    energia = info.get("energia", 10)
                    edad = info.get("edad", 0)
                    posicion = tuple(info.get("posicion", [0, 0]))

                    if "depredador" in animal.lower():
                        individuo = Depredador(energia, edad, posicion)
                    else:
                        individuo = Presa(energia, edad, posicion)

                    reglas_texto = info.get("reglas", [])
                    reglas_obj = []

                    for regla_str in reglas_texto:
                        try:
                            parsed = parsear_regla(regla_str)
                            print("Regla parseada correctamente:")
                            print(parsed)
                            print("\n")

                            # 🔁 Aquí deberías mapear condiciones a comportamientos
                            # (esto es muy simplificado, puedes personalizarlo)
                            if "buscar alimento" in regla_str:
                                comportamiento = ComportamientoBuscarAlimento()
                            elif "huir" in regla_str:
                                comportamiento = ComportamientoHuir()
                            else:
                                comportamiento = None

                            if comportamiento:
                                regla_obj = Regla(parsed["condicion"], comportamiento)
                                reglas_obj.append(regla_obj)

                        except SyntaxError as e:
                            print(f"Error de sintaxis: {e}\n")

                    # Guardamos reglas en el individuo (puedes mover esto a su clase después)
                    individuo.reglas = reglas_obj

                    # ====================================
                    # Simulamos que el individuo actúa
                    # ====================================
                    print(f"⚙️  Simulando acción de {animal}")
                    for regla in individuo.reglas:
                        if regla.se_cumple(individuo):
                            regla.ejecutar(individuo, nombre_ambiente)

    except json.JSONDecodeError:
        print("Error: El archivo no contiene un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")

main()
