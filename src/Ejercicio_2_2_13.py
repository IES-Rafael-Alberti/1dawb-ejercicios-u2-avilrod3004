'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''

def main():
    
    entrada = input('--> ')
    
    while entrada != 'salir':
        print(entrada)
        entrada = input('--> ')

if __name__ == '__main__':
    main()