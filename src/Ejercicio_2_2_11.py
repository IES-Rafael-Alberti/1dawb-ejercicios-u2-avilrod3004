'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
'''

def pedirPalabra():
    '''
    '''
    palabra = input('Introduce un palabra: ')

    return palabra


def contarLetras(palabra):
    '''
    '''
    num = len(palabra)

    return num


def main():
    palabra = pedirPalabra()
    num = contarLetras(palabra)

    n = num - 1
    while n >= 0:
        print(palabra[n])
        n -= 1

    
if __name__ == '__main__':
    main()