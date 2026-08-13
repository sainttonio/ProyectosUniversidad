#En este ejercicio el usuario debe adivinar, este programa de 3 intentos, en los cuales 
#Tiene que adivinar un numero del 1-10, el programa usa bucle while y condicional if.

def ingresar_numero():

    num = int(input("Ingrese un número del 1-10 y adivine el digito (solo tiene 3 intentos): "))

    num =  3

    while num != 3 : 
        print("El número que escogio es incorrecto, siga intentando")
        if num == 3: 
            print("Has acertado!, el número es 3")

ingresar_numero()
