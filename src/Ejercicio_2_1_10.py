'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

    Ingredientes vegetarianos: Pimiento y tofu.
    Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
'''

def tipoPizza():
    '''
    '''
    print('¿Qué tipo de pizza quieres? \n 1 - vegetariana\n 2 - no vegetariana')
    entrada = input('--> ')
    tipo = int(entrada)

    while not tipo.isdecimal() or tipo != 1 or tipo != 2:
        print('**ERROR** - LAS RESPUESTAS VÁLIDAS SON 1 (vegetariana) O 2 (no vegetariana)')
        entrada = input('--> ')
        tipo = int(entrada)

    if tipo == 1:
        tipo = 'vegetariana'
    else:
        tipo = 'no vegetariana'

    return tipo


def mostrarIngredientes(tipo:str):
    '''
    '''
    if tipo == 'vegetariana':
        print('Los ingredinetes base son mozzarella y tomate, le puedes añadir uno extra:\na pimiento\nb tofu')
        ingrediente = input('--> ').lower()

        while ingrediente != 'a' or ingrediente != 'b':
            print('**ERROR** - LAS RESPUESTAS VÁLIDAS SON a (pimiento) O b (tofu)')
            ingrediente = input('--> ').lower()
        
        if ingrediente == 'a':
            return 'pimiento'
        else:
            return 'tofu'
    
    else:
        print('Los ingredinetes base son mozzarella y tomate, le puedes añadir uno extra:\na peperoni\nb jamón\nc salmón')
        ingrediente = input('--> ').lower()

        while ingrediente != 'a' or ingrediente != 'b' or ingrediente != 'c':
            print('**ERROR** - LAS RESPUESTAS VÁLIDAS SON a (peperoni), b (jamón) O c (salmón)')
            ingrediente = input('--> ').lower()
        
        if ingrediente == 'a':
            return 'peperoni'
        elif ingrediente == 'b':
            return 'jamón'
        else:
            return 'salmón'


def main():
    tipo = tipoPizza()

    print(f'La pizza que has elegido es {tipo}. Ingredientes:\n- mozzarella\n- tomate\n- {mostrarIngredientes(tipo)}')


if __name__ == "__main__":
    main()
