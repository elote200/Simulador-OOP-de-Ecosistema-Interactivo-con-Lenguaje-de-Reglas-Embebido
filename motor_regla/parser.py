from .lexer import tokenizar

def parsear_regla(texto):
    tokens = tokenizar(texto)

    if not tokens or tokens[0][0] != 'SI':
        raise SyntaxError("La regla debe comenzar con 'Si'")

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

        atributo = atributo_token[1]
        operador = operador_token[1]
        tipo_valor = valor_token[0]
        valor = valor_token[1]

        # Validaciones semánticas
        if atributo in ['energia', 'edad']:
            if tipo_valor != 'NUMERO':
                raise SyntaxError(f"'{atributo}' debe compararse con un número, no con '{valor}'")
            if int(valor) < 0:
                raise SyntaxError(f"'{atributo}' no puede ser negativo")
            valor = int(valor)
        
        elif atributo == 'vivo':
            if tipo_valor != 'BOOLEANO':
                raise SyntaxError("'vivo' solo puede compararse con valores booleanos")
            valor = valor == 'true'

        elif atributo == 'estado':
            if operador != '==':
                raise SyntaxError("'estado' solo puede compararse usando '=='")
            if tipo_valor != 'ESTADO':
                raise SyntaxError(f"El valor para 'estado' debe ser un estado válido, no '{valor}'")

        else:
            raise SyntaxError(f"Atributo desconocido: {atributo}")

        condiciones.append({
            "atributo": atributo,
            "operador": operador,
            "valor": valor
        })

        i += 3
        if i < len(condicion_tokens):
            if condicion_tokens[i][0] != 'LOGICO':
                raise SyntaxError(f"Operador lógico esperado después de condición en posición {i}")
            operadores_logicos.append(condicion_tokens[i][1])
            i += 1

            if i + 2 >= len(condicion_tokens):
                raise SyntaxError(f"Condición esperada después del operador lógico '{condicion_tokens[i-1][1]}'")

    return {
        "accion": accion,
        "condiciones": condiciones,
        "operadores_logicos": operadores_logicos
    }
