def solicitar_nombre():
    print("INGRESE EL NOMBRE DEL PRODUCTO : ")
    producto = str(input())
    return producto 

def solicitar_id():
    print("INGRESE LA ID DEL PRODUCTO (+ 4 DIGITOS ): ")
    id = int(input())

    if id > 10000:
        print(id)
        return id 
    else: 
        id = 0 
        print("ERROR: ID INCORRECTO")
        return id 
  
def solicitar_volumen(): 
    print("Ingrese el volumen del producto (decimales positivos, metros cubicos): ".upper())
    volumen = float(input())
    if 0.0 < volumen < 5.5: 
        return volumen 
    else: 
        volumen = 10
        print("VOLUMEN INCORRECTO, VUELVA A INGRESAR EL VOLUMEN CORRECTAMENTE")
        return volumen

#### main ####

nombre = solicitar_nombre()
id = solicitar_id()
if id != 0: 
    volumen = solicitar_volumen()
    if volumen != 10: 
        print("==== DATOS DEL PRODUCTO ====")
        print("NOMBRE DEL PRODUCTO: ",nombre)
        print("ID DEL PRODUCTO: ",id)
        print("VOLUMEN DEL PRODUCTO: ", volumen)
        print("=== PRODUCTO ALMACENADO CORRECTAMENTE ")

else: 
    print("EL PRODUCTO NO SE ALMACENARA, ID INVALIDO")

