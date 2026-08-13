# ALGORITMO PARA FREIR UN HUEVO 

#1. VER SI TENGO HUEVOS 
#2. SI TENGO HUEVOS, SIGUE EL ALGORITMO
#3. SI NO, SE ROMPE EL FLUJO Y EL ALGORITMO NOS SIGUE 
#4. SACAR EL SARTEN 
#5 ECHAR ACEITE AL SARTEN
#6 PRENDER LA COCINA
#7 ABRIR EL HUEVO Y PONERLO EN EL SARTEN 
#8 PONERLE SAL AL HUEVO 
#9 ESPERAR EL TIEMPO DE COCCION DE EL HUEVO
#10 REVISAR SI EL HUEVO YA ESTA LISTO 
#11 SI EL HUEVO ESTA LISTO, APAGAR COCINA, SI NO, ESPERAMOS UN TIEMPO MAS 
#11 APAGAR LA COCINA 
#12 TOMAR UN PLATO
#13 EMPLATAR EL HUEVO 
    #FIN DEL ALGORITMO 



def ingresar_usuario(): 

    nombre = str(input("Ingrese su nombre: "))
    edad = int(input("Ingrese su edad: "))
    direccion =str(input("Ingrese su direccion: "))
    salario = float(input("Ingrese su salario: "))

    print(f"Gracias por ingresar tus datos {nombre}")


ingresar_usuario()
