'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''

def pedirNum():
    '''
    '''
    num = input('Introduce un número entero: ')

    while num.isdecimal() == False:
        print('**ERROR** - INTRODUCE UN NÚMERO ENTERO')
        num = input('Introduce un número entero: ')

    return int(num)


def esPrimo(num):
    '''
    '''
    for n in range(2, num):
        if num % n == 0:
            return 'No es primo'
        

    return 'Es primo'
    

def main():
    num = pedirNum()

    print(esPrimo(num))


if __name__ == "__main__":
    main()