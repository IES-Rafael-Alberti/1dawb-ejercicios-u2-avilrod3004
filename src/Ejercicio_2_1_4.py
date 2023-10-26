'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''

def pedirNumero():
    '''
    Pide un número y compueba que lo sea

    Retorna
    -------
    int
        un entero con el valor del número introducido por consola
    '''
    salir = False

    while not salir:
            entrada = input('Introduce un número: ')

            if entrada.isnumeric():
                salir = True
            else:
                 print('**ERROR** - DEBE SER UN NÚMERO')
    
    numero = int(entrada)

    return numero


def calcularResto(num):
    '''
    Recibe el número y calcula el resto de dividirlo entre 2

    Retorna
    -------
    float
        el valor del resto de la división entre dos
    '''
    resultado = num % 2
    return resultado


def restoCero(resto):
    '''
    Recibe el resto de la división

    Retorna
    -------
    bool
        True si el resto es cero / False si el resto es distinto a cero
    '''
    if resto == 0:
        return True
    else:
        return False
    

def main():
    num = pedirNumero()

    resto = calcularResto(num)

    if restoCero(resto) == True:
        print('El número introducido es PAR')
    else:
        print('El número introducido es IMPAR')
        

if __name__ == "__main__":
    main()