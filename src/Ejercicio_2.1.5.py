# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

def impuesto(edad, ingresos):
    if edad >= 16 and ingresos >= 1000:
        return 'Tienes que tributar'
    else:
        return 'No tienes que tributar'

#################################################################################

edad = int(input('¿Cuántos años tienes? '))
ingresos = float(input('Ingresos mensuales: '))

print(impuesto(edad, ingresos))

'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
'''

def pedirEdad():
    '''
    Pedir la edad y comprobar que se trata de un número entero entre 1 y 100.

    Retorna
    -------
    int
        un entero con el valor de la edad introducida por consola
    '''
    salir = False
    while not salir:
        entrada = input("Introduzca su edad: ")

        if entrada.isnumeric() and 0 < int(entrada) <= 100:
            salir = True
        else:
            print("**ERROR** - EDAD INTRODUCIDA NO VALIDA")
    
    edad = int(entrada)

    return edad


def pedirIngresos():
    '''
    Pedir los ingresos mensuales y comprobar que se trata de un número

    Retorna
    -------
    int
        un entero con el valor de los ingresos introducidos por consola
    '''
    salir = False

    while not salir:
        entrada = input('Introduce tus ingresos mensuales: ')

        if entrada.isnumeric:
            salir = True
        else:
            print("**ERROR** - CANTIDAD INTRODUCIDA NO VALIDA")

    ingresos = int(entrada)
    return ingresos


def comprobarEdad(edad):
    '''
    Comprobar si la edad introducida es mayor de 16 años o no

    Retorna
    -------
    bool
        True si es 16 años o mayor / False si es menor de 16 años
    '''
    if edad >= 16:
        return True
    else:
        return False
    

def comprobarIngresos(ingresos):
    '''
    Comprobar si los ingresos mensuales introducidos son iguales o superiores a 1000€

    Retorna
    -------
    bool
        True si es igual o superiro a 1000€ / False si es menor a 1000€
    '''
    if ingresos >= 1000:
        return True
    else:
        return False
    

def main():
    edad = pedirEdad()
    ingresos = pedirIngresos

    


if __name__ == "__main__":
    main()
