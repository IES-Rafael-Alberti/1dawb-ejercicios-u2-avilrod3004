'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo. 
'''

def pedirNum():
    '''
    '''
    num = input('Introduce un número entero: ')

    while num.isdecimal() == False:
        print('**ERROR** - SOLO SON VÁLIDOS LOS NÚMERO ENTERO')
        num = input('Introduce un número entero: ')

    return int(num)

def main():
    num = pedirNum()


if __name__ == '__main__':
    main()