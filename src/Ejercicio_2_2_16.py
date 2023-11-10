'''
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 0. Informar cuál fue el mayor número ingresado.
'''

def pedirNumero():
    '''
    '''
    num = input('Introduce un número: ')

    return int(num)


def maxNumero(num):
    '''
    '''
    maximo = 0
    while num != 0:

        if num > maximo:
            maximo = num
        
        num = pedirNumero()

    return maximo
            
   

def main():
    num = pedirNumero()
    maximo = maxNumero(num)

    print(f'El mayor numero es {maximo}')


if __name__ == '__main__':
    main()