'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.
'''

def pedirFrase():
    '''
    '''
    frase = input('Intrduce una frase: ')

    return frase.replace(' ','').lower()


def pedirLetra():
    '''
    '''
    letra = input('Introduce un letra: ')

    while len(letra) > 1:
        print('**ERROR** - SOLO SE PUEDE INTRODUCIR UNA LETRA')
        letra = input('Introduce un letra: ')

    return letra

def contarLetra(frase:str, letra:str):
    '''
    '''
    num = frase.count(letra)

    return int(num)

def main():
    frase = pedirFrase()
    letra = pedirLetra()

    print(f'La letra {letra} aparece {contarLetra(frase, letra)} veces')


if __name__ == '__main__':
    main()