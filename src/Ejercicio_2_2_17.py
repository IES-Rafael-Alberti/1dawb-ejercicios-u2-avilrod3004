'''
Leer un número entero positivo desde teclado e imprimir la suma de los dígitos que lo componen.
'''

def pedirNumPositivo() -> int:
    '''
    Pedir un número entero y positivo por consola

    Retorna
    ------
    int
        entero con el número introducido por consola
    '''
    num = input('Introduce un número entero positivo: ')
    num = int(num)

    while num < 0:
        print('**ERROR** - INTRODUCE UN NÚMERO ENTERO POSITIVO')
        num = input('Introduce un número entero positivo: ')
        num = int(num)

    return num


def sumaDigitos(num: int) -> int:
    '''
    Mide la longitud caracteres de la variable num. Con un bucle suma los digitos que lo componen.

    Retorna
    -------
    int
        entero con la suma de los digitos
    '''
    numStr = str(num)
    digitos = len(numStr)
    suma = 0

    for i in range(0, digitos, 1):
        suma = suma + int(numStr[i])
        i += 1

    return suma


def main():
    entero = pedirNumPositivo()
    
    print(f'La suma de los digitos es {sumaDigitos(entero)}')


if __name__ == '__main__':
    main()