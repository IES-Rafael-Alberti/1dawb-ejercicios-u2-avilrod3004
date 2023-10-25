'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

def pedirPasswd():
    '''
    Pedir la contraseña
    
    Retorna
    -------
    str
        una cadena de caracteres con la respuesta dada por consola
    '''
    password = input('Contraseña: ')
    return password


def coincidePasswd(password):
    '''
    Comprobar si la contraseña coincide con la contraseña almacenada

    Retorna
    -------
    bool
        True si coincide / False si no coincide
    '''
    passwordOrigianl = 'contraseña'

    password = password.lower()

    if passwordOrigianl == password:
        return True
    else:
        return False


def main():
    passwd = pedirPasswd()

    if coincidePasswd(passwd):
        print('La contraseña introducida coincide con la guardada')
    else:
        print('La contraseña no coincide con la guardada')


if __name__ == "__main__":
    main()