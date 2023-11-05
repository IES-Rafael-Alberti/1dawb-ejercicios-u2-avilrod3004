'''
Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados.
'''

def pedirNumero():
    '''
    Pedir un número mayor que 1 por consola al usuario

    Retorna
    -------
    int
        entero con el número introducido por el usuario
    '''
    num = input('Introduce un número: ')

    while num.isdecimal() == False:
        print('**ERROR** - INTRODUCE UN NÚMERO')
        num = input('Introduce un número: ')

    return int(num)


def esPrimo(num: int):
    '''
    '''
    for n in range(2, num):
        if num % n == 0:
            return False
            
    return True


def main():
    num = pedirNumero()
    primos = 0

    while num > 0:
        if num > 1:
            if esPrimo(num) == True:
                primos += 1
            
            num = pedirNumero()
        else:
            break

    print(f'Cantidad de números primos introducidos --> {primos}')


if __name__ == '__main__':
    main()