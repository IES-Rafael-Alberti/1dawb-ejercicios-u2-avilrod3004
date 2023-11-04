'''
Solicitar al usuario el ingreso de una frase y de una letra (que puede o no estar en la frase). Recorrer la frase, carácter a carácter, comparando con la letra buscada. Si el carácter no coincide, indicar que no hay coincidencia en esa posición (imprimiendo la posición) y continuar. Si se encuentra una coincidencia, indicar en qué posición se encontró y finalizar la ejecución.
'''

def pedirFrase():
    '''
    Pedir una frase por consola al usuario

    Retorna
    -------
    str
        cadena de texto introducida por el usuario
    '''
    frase = input('Introduce una frase: ')

    return frase


def pedirLetra():
    '''
    Pedir una letra por consola

    Retorna
    -------
    str
        cadena de caracteres con la letra introducida
    '''
    salir = False

    while salir == False:
        letra = input('Introduce una letra (puede o no estar en la frase): ')
        letra = letra.replace(' ', '')

        if len(letra) == 1:
            salir == True
        elif letra.isnumeric() == True:
            print('**ERROR** - NO SE PUEDE INTRODUCIR UN NÚMERO')
        else:
            print('**ERROR** - RESPUESTA NO VÁLIDA')

        return letra
    

def numCaracteres(frase):
    '''
    Calcular el número de caracteres en la frase

    Retorna
    -------
    int
        número entero con la cantidad de caracteres
    '''
    num = len(frase)

    return num


def main():
    frase = pedirFrase()
    letra = pedirLetra()
    num = numCaracteres(frase)

    for i in range(0, num):
        if frase[i] == letra:
            print('')
            print(f'Una coincidencia encontrada en la posición {i}')
            break
        else:
            print(f'En la posición {i} no hay coincidencias')


if __name__ == "__main__":
    main()