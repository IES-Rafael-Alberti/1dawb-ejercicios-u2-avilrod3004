"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""

from src.Ejercicio_2_1_1 import pedirEdad


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