# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

def grupo(nombre, sexo):
    inicial = nombre[0].lower()
    sexo = sexo.lower()

    if inicial <= 'm' and sexo == 'mujer':
        return 'Te corresponde el Grupo A'
    elif inicial >= 'n' and sexo == 'hombre':
        return 'Te corresponde el Grupo A'
    else:
        return 'Te corresponde el Grupo B'

####################################################################################

nombre = input('Nombre: ')
sexo = input('Sexo (Mujer o Hombre): ')

print(grupo(nombre, sexo))
