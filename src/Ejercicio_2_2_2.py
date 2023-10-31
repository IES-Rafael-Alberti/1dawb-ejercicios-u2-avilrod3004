"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

# from Ejercicio_2_1_1 import pedirEdad (da error al hacer el test de aniosCumplidos)
def pedirEdad():
    """
    Pedir la edad y comprobar que se trata de un número entero entre 1 y 100
    
    Retorna
    -------
    int
        un entero con el valor de la edad introducida por consola
    """
    salir = False
    while not salir:
        entrada = input("Introduzca su edad: ")

        if entrada.isnumeric() and 0 < int(entrada) <= 100:
            salir = True
        else:
            print("**ERROR** - LA EDAD DEBE SER ENTRE O Y 100")
    
    edad = int(entrada)

    return edad


def aniosCumplidos(edad: int):
    lista = 'Años cumplicos -->'

    for i in range(1, (edad + 1), 1):
        lista = lista + f' {i}'

    return lista


def main():
    edad = pedirEdad()

    print(aniosCumplidos(edad))


if __name__ == "__main__":
    main()