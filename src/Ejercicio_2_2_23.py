'''
Crear un programa que permita al usuario ingresar títulos de libros por teclado, finalizando el ingreso al leerse el string “*” (asterisco). Cada vez que el usuario ingrese un string de longitud 1 que contenga sólo una barra (“/”) se considera que termina una línea. Por cada línea completa, informar cuántos dígitos numéricos (del 0 al 9) aparecieron en total (en todos los títulos de libros que componen en esa línea). Finalmente, informar cuántas líneas completas se ingresaron.

Ejemplo de ejecución:
Libro: Los 3 mosqueteros
Libro: Historia de 2 ciudades
Libro: /
Línea completa. Aparecen 2 dígitos numéricos.
Libro: 20000 leguas de viaje submarino
Libro: El señor de los anillos
Libro: /
Línea completa. Aparecen 5 dígitos numéricos.
Libro: 20 años después
Libro: *
Fin. Se leyeron 2 líneas completas.
'''

def pedirLibro():
    '''
    Pedir el titulo de un libro por consola al usuario

    Retorna
    -------
    str
        cadena de caracteres del titulo del libro
    '''
    libro = input('Libro: ')

    return libro


def longitudTitulo(libro: str):
    '''
    Calcular el número de caracteres que tiene el titulo del libro

    Retorna
    -------
    int
        entero con el número de caracteres del titulo
    '''
    longitud = len(libro)

    return longitud


def encontrarNumero(libro: str, longitud: int):
    '''
    Contar cuantos números aparecen el titulo del libro

    Retorna
    -------
    int
        entero con la cantidad de la números del titulo
    '''
    numeros = 0

    for i in range(0, longitud, 1):
        c = libro[i]

        if c.isdecimal() == True:
            numeros = numeros + 1
        
        i += 1

    return numeros


def main():
    libro = pedirLibro()
    totalNumeros = 0
    num_lineas = 0

    while len(libro) > 0:
        if libro == '/':
            print(f'Línea completa. Aparecen {totalNumeros} dígitos numéricos.')
            num_lineas += 1
            totalNumeros = 0
        elif libro == '*':
            print(f'Fin. Se leyeron {num_lineas} líneas completas.')
            break
        else:
            longitud = longitudTitulo(libro)
            numeros = encontrarNumero(libro, longitud)

            totalNumeros = totalNumeros + numeros
        
        libro = pedirLibro()


if __name__ == '__main__':
    main()