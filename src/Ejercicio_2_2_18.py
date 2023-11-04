'''
Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir la suma de los dígitos que lo componen. La condición de corte es que se ingrese el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.
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

    return f'La suma de los digitos de {num} es {suma}'


def numPar(num: int, contador: int) -> int:
    '''
    Comprobar si el número es par y añadir 1 al contador

    Retorna
    -------
    int
        un entero con la cantidad de números positivos
    '''

    if num % 2 == 0:
        contador += 1
    
    return contador


def main():
    entero = pedirNumPositivo()
    contador = 0

    while entero > -1:
        print(sumaDigitos(entero))
        contador = numPar(entero, contador)
        entero = pedirNumPositivo()

    print(f'_________________________________\n')
    print(f'Números pares introducidos: {contador}\n')


if __name__ == '__main__':
    main()