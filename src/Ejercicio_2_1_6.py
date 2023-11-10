'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
'''

def pedirNombre():
    '''
    Pedir el nombre de la persona

    Retorna
    -------
    str
        una cadena de caracteres con el nombre del alumno
    '''
    nombre = input('Nombre: ').title()
    return nombre


def pedirSexo():
    '''
    Pedir el sexo del alumno

    Retorna
    -------
    str
        cadena de caracteres con la respueta de la persona
    '''
    sexo = input('Sexo (mujer o hombre): ')
    return sexo


def comprobarInicial(nombre):
    '''
    Toma la inicial de los nombres

    Retorna
    -------
    bool
        True si el nombre empieza por una letra entre la A y la M / False si el nombre empieza por una letra entre la N y la Z
    '''
    inicial = nombre[0]

    if inicial <= 'M':
        return True
    else:
        return False
    

def comprobarSexo(sexo):
    '''
    Retorna
    -------
    bool
        True si el sexo es mujer / False si el sexo es hombre
    '''

    if sexo.lower() == 'mujer':
        return True
    else:
        return False
    

def main():
    nombre = pedirNombre()
    sexo = pedirSexo()

    if comprobarInicial(nombre) == True and comprobarSexo(sexo) == True:
        print('Te corresponde el GRUPO A')
    elif comprobarInicial(nombre) == False and comprobarSexo(sexo) == False:
        print('Te corresponde el GRUPO A')
    elif comprobarInicial(nombre) == True and comprobarSexo(sexo) == False:
        print('Te corresponde el GRUPO B')
    else:
        print('Te corresponde el GRUPO B')


if __name__ == "__main__":
    main()