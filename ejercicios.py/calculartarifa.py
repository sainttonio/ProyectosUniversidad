def validad_carga(peso_carga:int): 

    if 100 <= peso_carga <=  3000: 
        return True 
    else:
        return False

def verificar_descuento(peso: int): 

     if peso % 100 == 0: 
        return True 
     else: 
         return False 
     
ingresar_peso = int(input("Ingrese el peso de la carga en kg: "))

if validad_carga(ingresar_peso):
    precio = ingresar_peso * 200
    if verificar_descuento(ingresar_peso):
        precio = precio - 1000
    else: 
        precio = precio 

    print(f'El precio de la carga es ${precio}clp')

else: 
    print(f'Error: El peso debe estar entre 100 y 3000 kg')




    
    

