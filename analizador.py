# ENTERO    400
# REAL      401
# VARIABLE  100
# CADENA    101
# NUMERO    200
# =         300
# (         301
# )         302
# ,         303
# +         304
# -         305
# *         306
# /         307
# MOSTRAR   500
'''
ENTERO x = 5, y = 10
MOSTRAR("HOLA", x + 5)
'''

tokens = [400, 100, 300, 200, 303, 100, 300, 200,
            500, 301, 101, 303, 100, 304, 200, 302]

def ini(tokens):
    i = 0
    error = ''
    while i < len(tokens) and tokens[i] in (400, 401):
        i, error = definicion(tokens, i)
        if error != '':
            return error

    while i < len(tokens) and tokens[i] == 500:
        i, error = mostrar(tokens, i)
        if error != '':
            return error
    if i < len(tokens):
        return 'ERROR: TOKEN INESPERADO'
    return 'VALIDO'

def definicion(tokens, i):
    if i < len(tokens) and tokens[i] in (400, 401):
        i, error = tipo_dato(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR: SE ESPERABA UN TIPO DE DATO'

    if i < len(tokens) and tokens[i] == 100:
        i, error = lista_ini(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR: SE ESPERABA UNA VARIABLE'
    return i, ''

def tipo_dato(tokens, i):
    if i < len(tokens) and tokens[i] in (400, 401):
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA UN ENTERO O REAL'
    return i, ''

def lista_ini(tokens, i):
    if i < len(tokens) and tokens[i] == 100:
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA UNA VARIABLE'

    if i < len(tokens) and tokens[i] == 300:
        i = i + 1
    else:
        return i, "ERROR: SE ESPERABA EL OPERADOR ="

    if i < len(tokens) and tokens[i] == 200:
        i = i + 1
    else:
        return i, 'ERROR: SE ESPERABA UN NUMERO'

    while i < len(tokens) and tokens[i] == 303:
        i = i + 1

        if i < len(tokens) and tokens[i] == 100:
            i = i + 1
        else:
            return i, 'ERROR: SE ESPERABA UNA VARIABLE DESPUES DE LA COMA'

        if i < len(tokens) and tokens[i] == 300:
            i = i + 1
        else:
            return i, 'ERROR: SE ESPERABA ='

        if i < len(tokens) and tokens[i] == 200:
            i = i + 1
        else:
            return i, 'ERROR: SE ESPERABA UN NUMERO'

    return i, ''


def mostrar(tokens, i):

    if i < len(tokens) and tokens[i] == 500:
        i = i + 1
    else:
        return i, "ERROR: SE ESPERABA MOSTRAR"

    if i < len(tokens) and tokens[i] == 301:
        i = i + 1
    else:
        return i, "ERROR: SE ESPERABA UN ("

    if i < len(tokens) and tokens[i] in (101, 100, 200, 301):
        i, error = lista_exp(tokens, i)
        if error != '':
            return i, error
    else:
        return i, 'ERROR: SE ESPERABA UNA CADENA O EXPRESION'

    if i < len(tokens) and tokens[i] == 302:
        i = i + 1
    else:
        return i, "ERROR: SE ESPERABA UN )"

    return i, ''


def lista_exp(tokens, i):

    if i < len(tokens) and tokens[i] == 101:
        i = i + 1
    else:
        i, error = expresion(tokens, i)
        if error != '':
            return i, error

    while i < len(tokens) and tokens[i] == 303:

        i = i + 1

        if i < len(tokens) and tokens[i] == 101:
            i = i + 1
        else:
            i, error = expresion(tokens, i)
            if error != '':
                return i, error

    return i, ''


def expresion(tokens, i):

    i, error = termino(tokens, i)
    if error != '':
        return i, error

    while i < len(tokens) and tokens[i] in (304, 305):

        i = i + 1

        i, error = termino(tokens, i)
        if error != '':
            return i, error

    return i, ''


def termino(tokens, i):

    i, error = factor(tokens, i)
    if error != '':
        return i, error

    while i < len(tokens) and tokens[i] in (306, 307):

        i = i + 1

        i, error = factor(tokens, i)
        if error != '':
            return i, error

    return i, ''


def factor(tokens, i):

    if i < len(tokens) and tokens[i] == 100:
        i = i + 1

    elif i < len(tokens) and tokens[i] == 200:
        i = i + 1

    elif i < len(tokens) and tokens[i] == 301:
        i = i + 1

        i, error = expresion(tokens, i)
        if error != '':
            return i, error

        if i < len(tokens) and tokens[i] == 302:
            i = i + 1
        else:
            return i, 'ERROR: SE ESPERABA ) EN LA EXPRESION'

    else:
        return i, 'ERROR: FACTOR NO VALIDO'

    return i, ''


print(ini(tokens))
