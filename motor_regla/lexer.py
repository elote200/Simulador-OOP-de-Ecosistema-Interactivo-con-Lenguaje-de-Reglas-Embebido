import re

TOKEN_REGEX = [
    ('SI', r'\bSi\b'),
    ('ENTONCES', r'\bentonces\b'),
    ('COMPARADOR', r'==|!=|<|>'),
    ('LOGICO', r'\&\&|\|\|'),
    ('ATRIBUTO', r'\b(edad|energia|vivo)\b'),
    ('BOOLEANO', r'\b(true|false)\b'),
    ('NUMERO', r'\b\d+\b'),
    ('ACCION', r'\bcaminar\b|\breproducirse\b|\bcazar\b|\bmorir\b'),
    ('ESPACIO', r'\s+'),
    ('DESCONOCIDO', r'.')
]

def tokenizar(string):
    tokens = []

    while string:
        for tipo, patron in TOKEN_REGEX:
            match = re.match(patron, string)
            if match:
                if tipo != 'ESPACIO':
                    tokens.append((tipo, match.group()))
                
                string = string[len(match.group()):]
                break
    return tokens