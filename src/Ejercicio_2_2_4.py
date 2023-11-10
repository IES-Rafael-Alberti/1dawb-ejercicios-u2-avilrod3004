'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
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


def cuentaAtras(num):
    '''
    '''
    serie = f'Cuenta atrás --> '

    for i in range(0, num, 1):
        serie = serie + f'{num - i}, '
        i += 1

    serie = serie + '0'

    return serie


def main():
    num = pedirNumero()

    print(cuentaAtras(num))


if __name__ == "__main__":
    main()