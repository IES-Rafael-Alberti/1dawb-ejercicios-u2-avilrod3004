'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.
'''

def main():
    passwdOriginal = 'contraseña'
    passwd = input('Introduce la contraseña: ')

    while passwdOriginal != passwd:
        print('**ERROR** - CONTRASEÑA INCORRECTA!! Vuelve a intentarlo')
        passwd = input('Introduce la contraseña: ')

    print('¡¡HAS ADIVINADO!!')


if __name__ == '__main__':
    main()