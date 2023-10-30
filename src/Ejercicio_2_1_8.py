'''
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel 	            Puntuación
Inaceptable           	0.0
Aceptable 	            0.4
Meritorio 	        0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''

def pedirPuntos():
    '''
    Pedir la puntuación y comprbar que que sea una de las puntuaciones posibles

    Retorna
    ------
    float
        valor de la puntuación
    '''
    salir = False

    while not salir:
        entrada = input('Introduce puntuación: ')

        if entrada == '0.0' or entrada == '0.4' or entrada >= '0.6':
            salir = True
        else:
            print('**ERROR** - PUNTUACIÓN INTRODUCIDA NO VÁLIDA')

    puntos = float(entrada)
    return puntos


def nivelRendimiento(puntos: float):
    '''
    Comprobar la puntuación y devolver el nivel que le corresponde

    Retorna
    -------
    str
        cadena de caracteres con el nivel correspondiente a la puntuación
    '''
    if puntos == 0.0:
        return 'inaceptable'
    elif puntos == 0.4:
        return 'aceptable'
    else:
        return 'meritorio'
    

def cantidadDinero(puntos: float):
    '''
    Calcular la cantidad de dinero corresponiente a la puntuación obtenida

    Retorna
    ------
    float
        numero decimal con la cantidad de dinero para el trabajador
    '''
    if puntos == 0.0:
        return 0.0 * 2400
    elif puntos == 0.4:
        return 0.4 * 2400
    else:
        return puntos * 2400
    

def main():
    puntos = pedirPuntos()

    print(f'Tu nivel de rendimiento es {nivelRendimiento(puntos)}, recibirás {cantidadDinero(puntos)}€')


if __name__ == "__main__":
    main()