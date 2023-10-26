'''
Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''

def pedirNumero():
    '''
    Pide un número

    Retorna
    -------
    int
        un entero con el número dado por consola
    '''
    num = int(input('Introduce un número: '))
    return num


def divisionNumeros(n1, n2):
    '''
    Hace la división entre los dos números

    Retorna
    -------
    float
        un float con el resultado de la división de los dos números
    '''
    resultado = n1 /n2
    return resultado


def divisorCero(divisor):
    '''
    Comprueba si el divisor es cero

    Retorna
    -------
    bool
        True si el divisor es cero / False si el divisor no es cero
    '''
    if divisor == 0:
        return True
    else:
        return False
    

def main():
    n1 = pedirNumero()
    n2 = pedirNumero()

    if divisorCero(n2) == True:
        print('**ERROR** - EL DIVISOR NO PUEDE SER CERO')
    else:
        print(f'El resultado de la división es {divisionNumeros(n1, n2)}')


if __name__ == "__main__":
    main()