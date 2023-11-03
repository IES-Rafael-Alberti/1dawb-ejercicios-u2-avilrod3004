'''
Leer números enteros de teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los números positivos ingresados.
'''

def pedirNumero():
    '''
    '''
    num = input('Introduce un número: ')

    return int(num)


def sumarNumeros(num):
    '''
    '''
    suma = 0

    while num != 0:

        if num > 0:
            suma = suma + num

        num = pedirNumero()

    return suma
   

def  main():
    num = pedirNumero()
    suma = sumarNumeros(num)

    print(f'La suma de los número introducidos es {suma}')


if __name__ == '__main__':
    main()