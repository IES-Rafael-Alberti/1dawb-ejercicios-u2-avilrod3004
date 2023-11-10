'''
Solicitar al usuario que ingrese una frase y luego informar cuál fue la palabra más larga (en caso de haber más de una, mostrar la primera) y cuántas palabras había. Precondición: se tomará como separador de palabras al carácter “ “ (espacio), ya sea uno o más.
'''

def pedirFrase():
    '''
    Pedir una frase por consola al usuario

    Retorna
    -------
    str
        cadena de caracteres con la frase
    '''
    frase = input('Introduce una frase: ')

    return frase


def separarPorEspacios(frase: str):
    '''
    '''
    palabras = frase.split()

    return palabras


def contarPalabras(palabras):
    '''
    '''
    num = len(palabras)

    return num


def contarLetras(palabras, num:int):
    '''
    Contar las letras de las palabras
    '''
    masLarga = ''
    
    for i in range(0, num, 1):
        una = ''
        una = palabras[i]
        if len(una) > len(masLarga):
            masLarga = una

        i += 1
    
    return masLarga


def main():
    frase = pedirFrase()
    palabras = separarPorEspacios(frase)
    num = contarPalabras(palabras)

    print(f'La palabra más larga de las {num} es: {contarLetras(palabras, num)}')


if __name__ == "__main__":
    main()