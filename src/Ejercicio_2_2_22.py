'''
Crear un programa que solicite el ingreso de números enteros positivos, hasta que el usuario ingrese el 0. Por cada número, informar cuántos dígitos pares y cuántos impares tiene. Al finalizar, informar la cantidad de dígitos pares y de dígitos impares leídos en total.
'''

def pedirNumPositivo():
    '''
    Pedir un número entero y positivo por consola

    Retorna
    ------
    str
        entero con el número introducido por consola
    '''
    num = input('Introduce un número entero positivo: ')
    num = int(num)

    while num < 0:
        print('**ERROR** - INTRODUCE UN NÚMERO ENTERO POSITIVO')
        num = input('Introduce un número entero positivo: ')
        num = int(num)

    return num


def numDigitos(num: int):
    '''
    Calcular el número de digitos que tiene el número

    Retorna
    -------
    int
        entero con el número de digitos
    '''
    num = str(num)
    digitos = len(num)

    return digitos


def main():
    num = pedirNumPositivo()
    sumaPares = 0
    sumaImpares = 0

    while num > 0:
        digitos = numDigitos(num)
        totalPares = 0
        totalImpares = 0
        

        for i in range(0, digitos, 1):
            pares = 0
            impares = 0

            n = str(num)[i]
            n = int(n)

            if n % 2 == 0:
                pares += 1
            else:
                impares += 1
        
            totalPares = totalPares + pares
            totalImpares = totalImpares + impares

            i += 1
        
        print(f'Digitos pares --> {totalPares} || Digitos impares --> {totalImpares}')

        sumaPares = sumaPares + totalPares
        sumaImpares = sumaImpares + totalImpares

        num = pedirNumPositivo()

        
    print(f'Digitos pares en total --> {sumaPares} || Digitos impares en total {sumaImpares}')


if __name__ == '__main__':
    main()