'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo. 

1
3 1
5 3 1
7 5 3 1
9 7 5 3 1
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
    serie = ''

    for i in range(1, (num + 1), 2):
        serie = f'{i} ' + serie
        print(serie)
        i += 2


if __name__ == '__main__':
    main()