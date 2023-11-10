'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

Formula para calcular El capital tras un año.
amount *= 1 + interest / 100

En donde:
- amount: Cantidad a invertir
- interest: Interes porcentual anual 
'''

def pedirCantidad():
    '''
    '''
    amount = input('Introduce cantidad a invertir: ')
    return float(amount)


def interesAnual():
    '''
    '''
    interest = input('Introduce el interés anual: ')
    return float(interest)


def numAnios():
    '''
    '''
    y = input('Introduce el número de años: ')
    return int(y)


def calcularInversion(amount, interest, y):
    '''
    '''
    amount = amount * y + interest / 100
    return amount


def main():
    amount = pedirCantidad()
    interest = interesAnual()
    y = numAnios()

    for i in range(1, (y + 1), 1):
        print('______________________')
        print(f'|| Capital al año {i} ||')
        print(f'   --> {calcularInversion(amount, interest, i)}')
        i += 1


if __name__ == "__main__":
    main()
