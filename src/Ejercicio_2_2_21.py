'''
Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.
'''
def ingresarMonto():
    '''
    Pedir al usuario que escriba el monto de una compra

    Retorna
    -------
    float
        monto de la compra
    '''
    monto = input('Ingresa el monto de la compra: ')
    monto = float(monto)

    return monto



def main():
    suma = 0
    monto = ingresarMonto()

    while monto != 0:
        if monto > 0:  
            suma = suma + monto
        monto = ingresarMonto()

    if suma > 1000:
        suma = suma - ((suma * 10) / 100)
    
    print(f'Total a pagar: {suma}€')


if __name__ == "__main__":
    main()