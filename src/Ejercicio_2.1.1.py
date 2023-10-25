# Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

def adulto(edad):
    if edad >= 18:
        return '¡Eres mayor de edad!'
    else:
        return 'Eres menor de edad'

########################################################

edad = int(input('¿Cuántos años tienes? \n'))

print(adulto(edad))
