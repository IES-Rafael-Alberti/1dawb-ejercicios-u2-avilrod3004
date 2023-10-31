'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

def pedirPalabra():
    '''
    '''
    palabra = input('Introduce una palabra: ')

    while palabra.count(" ") >= 1 or palabra.isnumeric():
        print('**ERROR** - SOLO PUEDES INTRODUCIR UNA PALABRA')
        palabra = input('Introduce una palabra: ')

    return palabra


def repetirPalabra(palabra):
    '''
    '''
    n = 1
    serie = ''

    while n <= 10:
        serie = serie + f'{palabra}\n'
        n += 1

    return serie


def main():
    palabra = pedirPalabra()

    print(repetirPalabra(palabra))


if __name__ == "__main__":
    main()