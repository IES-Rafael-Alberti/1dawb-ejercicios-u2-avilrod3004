'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
'''
# solo funciona en pytest si pone src.Ejercicio_2_2_3
# para que funcione desde aqui hay que quitarlo...
from src.Ejercicio_2_2_3 import pedirNumero

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