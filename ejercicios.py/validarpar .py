#Instrucciones: 1. Validar que sea entero positivo. 
# 2.saber si es par o impar. 
# 3. Procesar numero, mostrar suma de pares y la suma de impares.

def ingresar_num(): 
    while True: 
        try: 
            num = int(input("Ingrese un número positivo: "))
            if num > 0: 
                print("El número es válido\n")
                return num
            else: 
                print("Error, vuelva a ingresar un número\n")
        except ValueError: 
            print("Error, debe ser un número entero y positivo\n")

    
def detectar_par(num): 

    suma_pares = 0     
    num_temp = num 

    print("Analizando dígitos...")
    while num_temp > 0: 
        digito = num_temp % 10
        
        if digito % 2 == 0: 
            suma_pares += digito     
            print(f"Dígito {digito} es PAR")
        else: 
            suma_impares += digito   
            print(f"Dígito {digito} es IMPAR")
        
        num_temp //= 10  

    print(f"\nSuma de números pares: {suma_pares}")
    print(f"Suma de números impares: {suma_impares}")


numero = ingresar_num()
detectar_par(numero)