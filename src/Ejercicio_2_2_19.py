'''
Mostrar un menú con tres opciones: 1- comenzar programa, 2- imprimir listado, 3-finalizar programa. A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). Si elige una opción incorrecta, informarle del error. El menú se debe volver a mostrar luego de ejecutada cada opción, permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.
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
        print('--- Menú ------------\nElige una opción:\n 1- comenzar programa\n 2- imprimir listado\n 3- finalizar programa')
        opcion = input('--> ')

        if opcion == '1' or opcion == '2' or opcion == '3':
            salir = True
        elif opcion.isdecimal() == False:
            print('**ERROR** - INTRODUCE UN VALOR NUMERICO')
        else:
            print('**ERROR** - VALOR NUMERICO INCORRECTO')
        
    return opcion


def ejecutarOpciones(opcion):
    '''
    Dependiendo de la opción elegida se mostrará un texto por pantalla diferente

    Retorna
    -------
    bool
        True si las opciones son 1 ó 2 / False si es diferente a 1 ó 2 (siempre será 3)
    '''
    if opcion == '1':
        print('')
        print('Inicando programa...\n - No cierre la aplicación - ')
        print('')
        return True
    elif opcion == '2':
        print('')
        print('- tomates\n- galletas\n- lechuga\n- pasta de dientes\n- aceitunas')
        print('')
        return True
    else:
        print('Cerrando programa...')
        return False


def main():
    opcion = mostrarMenu()

    while ejecutarOpciones(opcion) == True:
        opcion = mostrarMenu()

    
if __name__ == '__main__':
    main()