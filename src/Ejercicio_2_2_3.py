'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
'''

def pedirNumero():
    '''
    '''
    salir = False
    while not salir:
        entrada = int(input("Introduzca un número entero y positivo: "))

        if entrada > 0:
            salir = True
        else:
            print("**ERROR** NÚMERO INTRIDUCIDO NO VÁLIDO")


    return entrada


def numImpares(num):
    serie = f'{num} --> '

    for i in range(1, num, 2):
        serie = serie + f' {i},'

    serie = serie + f' {num}'

    return serie


def main():
    num = pedirNumero()

    print(numImpares(num))


if __name__ == "__main__":
    main()