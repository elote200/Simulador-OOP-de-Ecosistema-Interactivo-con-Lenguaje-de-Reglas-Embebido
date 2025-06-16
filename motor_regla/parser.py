from .lexer import tokenizar
from regla.ReglaMorir import ReglaMorir
from regla.ReglaReproducirse import ReglaReproducirse
import json

def parsearRegla(texto):
    tokens = tokenizar(texto)

    if not tokens or tokens[0][0] != 'SI':
        raise SyntaxError("La regla debe comenzar con 'Si'")

    # Ahora buscamos la palabra 'entonces'
    try:
        entonces_index = next(i for i, t in enumerate(tokens) if t[0] == 'ENTONCES')
    except StopIteration:
        raise SyntaxError("Falta 'entonces' en la regla")

    condicion_tokens = tokens[1:entonces_index]
    if entonces_index + 1 >= len(tokens):
        raise SyntaxError("Falta la acción después de 'entonces'")

    accion = tokens[entonces_index + 1][1]

    condiciones = []
    operadores_logicos = []

    i = 0
    while i < len(condicion_tokens):
        if i + 2 >= len(condicion_tokens):
            raise SyntaxError("Condición incompleta")

        atributo_token = condicion_tokens[i]
        operador_token = condicion_tokens[i + 1]
        valor_token = condicion_tokens[i + 2]

        if atributo_token[0] != 'ATRIBUTO' or operador_token[0] != 'COMPARADOR':
            raise SyntaxError("Condición mal formada")

        # Parsear valor
        if valor_token[0] == 'NUMERO':
            valor = int(valor_token[1])
        elif valor_token[0] == 'BOOLEANO':
            valor = valor_token[1] == 'true'
        else:
            raise SyntaxError(f"Valor inválido: {valor_token[1]}")

        condiciones.append({
            "atributo": atributo_token[1],
            "operador": operador_token[1],
            "valor": valor
        })

        i += 3
        
        # Si hay más tokens, debería ser un operador lógico seguido de otra condición
        if i < len(condicion_tokens):
            if condicion_tokens[i][0] != 'LOGICO':
                raise SyntaxError(f"Operador lógico esperado después de condición en posición {i}")
            operadores_logicos.append(condicion_tokens[i][1])
            i += 1

            # Verificamos que haya al menos 3 tokens más para la siguiente condición
            if i + 2 >= len(condicion_tokens):
                raise SyntaxError(f"Condición esperada después del operador lógico '{condicion_tokens[i-1][1]}'")

      

    return {
        "accion": accion,
        "condiciones": condiciones,
        "operadores_logicos": operadores_logicos
    }

def getRegla(reg):
    if(reg['accion'] == 'morir'):
        return ReglaMorir(reg['condiciones'], reg['operadores_logicos'])
    elif(reg['accion'] == 'reproducirse'):
        return ReglaReproducirse(reg['condiciones'], reg['operadores_logicos'])
    else:
        raise SyntaxError(f"Acción desconocida: {reg['accion']}. Solo se admite 'morir' como acción.")

def parsearJson(archivo):

    """
    Esta funcion parsea el archivo .json y regresa un arreglo de reglas por especie
    que se estructura de la siguiente manera:
    
    [
        {'especie': 'Leon', 'reglas': [Regla1, Regla2, ...]},
        {'especie': 'Cebra', 'reglas': [Regla1, Regla2, ...]},
        ...
    ]
    
    Donde:
    reglas[0]['reglas'] contiene las reglas de la especie 'Leon',
    reglas[1]['reglas'] contiene las reglas de la especie 'Cebra', etc.
    """

    reglas = [
        {'especie': 'Leon', 'reglas': []},
        {'especie': 'Cebra', 'reglas': []},
        {'especie': 'Zorro', 'reglas': []},
        {'especie': 'Conejo', 'reglas': []},
        {'especie': 'Venado', 'reglas': []},
        {'especie': 'Tigre', 'reglas': []}
    ]
    
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
                    
                            reglaParseada = getRegla(parsearRegla(regla))

                            match animal:
                                case 'Leon':
                                      reglas[0]['reglas'].append(reglaParseada)
                                case 'Cebra':
                                      reglas[1]['reglas'].append(reglaParseada)
                                case 'Zorro':
                                      reglas[2]['reglas'].append(reglaParseada)
                                case 'Conejo':
                                      reglas[3]['reglas'].append(reglaParseada)
                                case 'Venado':
                                      reglas[4]['reglas'].append(reglaParseada)
                                case 'Tigre':
                                      reglas[5]['reglas'].append(reglaParseada)
                        except SyntaxError as e:
                            print(f"Error de sintaxis: {e}\n")
        
    except json.JSONDecodeError:
        print("Error: El archivo no contiene un JSON válido.")
    except Exception as e:
        print(f"Ocurrió un error al procesar el archivo: {e}")

    print("\nReglas parseadas:")
    for especie in reglas:
        print(f"{especie['especie']}: {len(especie['reglas'])} reglas")
        for regla in especie['reglas']:
            print(f"  - {regla}")
    return reglas



    