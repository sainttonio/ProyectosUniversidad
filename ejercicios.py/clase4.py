def costo_ceramica(): 

    largo = int(input("Ingrese el largo del ceramico en cm: "))
    ancho = int(input("Ingrese el ancho del ceramico en cm: "))
    precio_caja = int(input("Ingrese el precio de una caja: "))

    costo : float 

    costo = ((largo * ancho) * precio_caja)
    return costo 

costo_ceramica()