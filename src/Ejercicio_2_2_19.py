'''
Mostrar un menú con tres opciones:

MENÚ
----
1 - Introduzca una nota
2 - Imprimir listado
3 - Finalizar programa
Seleccione una opción => 

A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3).
Si elige una opción incorrecta, informarle del error.
El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir.
Si elige la opción 1 debe pedir que introduzca una nota.
Si elige la opción 2 se imprimirá la lista de las notas introducidas.
Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
'''

def mostrarMenu():
    '''
    Mostrar el menu con las tres opciones

    Retorna
    -------
    str
        cadena de caracteres con la respuesta del usuario
    '''
    salir = False
    while salir == False:
        print('--- Menú ------------\nElige una opción:\n 1- Introduzca una nota\n 2- Imprimir listado\n 3- Finalizar programa')
        opcion = input('Seleccione una opción => ')

        if opcion == '1' or opcion == '2' or opcion == '3':
            salir = True
        elif opcion.isdecimal() == False:
            print('**ERROR** - INTRODUCE UN VALOR NUMERICO')
        else:
            print('**ERROR** - VALOR NUMERICO INCORRECTO')
        
    return opcion
    

def main():
    opcion = mostrarMenu()
    notas = 'Notas almacenadas -->'

    while True:
        if opcion == '1':
            print('')
            nota = input('Introduce una nota: ')
            print('')
            notas = notas + f' {nota}'
        elif opcion == '2':
            print('')
            print(notas)
            print('')
        else:
            print('')
            print('Cerrando programa...')
            print('')
            break
        
        opcion = mostrarMenu()

   
if __name__ == '__main__':
    main()