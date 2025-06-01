from motor_regla.parser import parsear_regla

def main():

    regla = "Si energia < 51 && edad > 10 entonces cam" 

    try:
        resultado = parsear_regla(regla)
        print("Regla parseada correctamente:")
        print(resultado)
    except SyntaxError as e:
        print(f"Error de sintaxis: {e}")

main()
