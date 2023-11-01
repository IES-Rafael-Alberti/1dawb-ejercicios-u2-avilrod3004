'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido. 

*
**
***
****
*****
'''

def pedirNumero():
    '''
    '''
    num = input('Introduce un número entero: ')

    while num.isdecimal() == False:
        print('**ERROR** - INTRODUCE UN NÚMEROE ENTERO')
        num = input('Introduce un número entero: ')

    return int(num)


def main():
    num = pedirNumero()

    for i in range(1, (num + 1), 1):
        print('*' * i)
        i += 1

if __name__ == '__main__':
    main()
