'''
Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
'''
def pedirEdad():
    '''
    Pedir la edad de la persona y comprobar que sea numérico

    Retorna
    ------
    int
        dato de tipo entero con la edad de la persona
    '''
    entrada = input('Edad: ')

    while not entrada.isdecimal():
        print('**ERROR** - INTRODUCE UN VALOR NÚMERICO')
        entrada = input('Edad: ')

    edad = int(entrada)
    return edad


def calcularPrecio(edad: int):
    '''
    Calcular el precio de la entrada según la edad de la persona

    Retorna
    -------
    str
        cadena de caracteres con el precio correspondiente
    '''
    if edad < 4:
        return 'gratis'
    elif edad >= 4 and edad <= 18:
        return '5€'
    else:
        return '10€'
    

def main():
    edad = pedirEdad()

    print(f'La entrada es {calcularPrecio(edad)}.')


if __name__ == "__main__":
    main()