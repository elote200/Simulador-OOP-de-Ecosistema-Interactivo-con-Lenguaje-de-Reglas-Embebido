from .lexer import tokenizar

def parsear_regla(texto):
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
