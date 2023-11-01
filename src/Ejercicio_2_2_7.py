'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''

def tablas(num):
    '''
    '''
    print('╔═════════════════╗')
    print(f'    Tabla del {num} ')
    print('╚═════════════════╝')
    
    for i in range(1, 11, 1):
        print(f'{i} x {num} = {i * num}\n')
        i += 1

    
def main():
    for i in range(1, 11, 1):
        print(tablas(i))
        i += 1


if __name__ == "__main__":
    main()