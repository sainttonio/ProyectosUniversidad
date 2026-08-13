def calcular_imc():
     
    peso = float(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc : float 

    imc = peso / (altura**2)
    print("Su imc es: {imc}")
    return imc 

calcular_imc()

def gasto_basal(peso: float, altura: float, edad: int): 

    peso = float(input("Ingrese su peso en kg: "))
    altura = int("Ingrese su altura en cm: ")
    if altura is float: 
        return False 
    edad = int(input("Ingrese su edad: "))
    if edad < 1:
        return False
    
    geb: int 

    geb = (88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * edad)).__round__