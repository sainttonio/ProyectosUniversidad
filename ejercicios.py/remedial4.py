def solicitar_traccion():
    print("INGRESE LA TRACCION DE SU VEHICULO (DELANTERA, TRASERA O 4X4): ")
    traccion = input()
    return traccion

def solicitar_potencia(): 
    print("Ingrese la potencia de su vehiculo: ")
    hp = int(input())
    return hp 

def verificar_aire(): 
    print("SU VEHICULO CUENTA CON AIRE ACONDICIONADO? (1 = si , 2  = no) : ")
    aire = int(input())
    return aire 

def volumen_tanque(): 
    print("INGRESE EL VOLUMEN DE SU TANQUE DE GAS: ")
    volumen = float(input())
    return volumen

########### MAIN ##############


traccion = solicitar_traccion()
potencia = solicitar_potencia()
aire_acondicionado = verificar_aire()
capacidad_tanque = volumen_tanque()


if 1000 < potencia >= 1300: 
    if aire_acondicionado == 1:
        if 35.0 < capacidad_tanque > 70.5:
            print("EL VEHICULO CUMPLE CON TODOS LOS REQUISITOS PARA SER VENDIDOS")

else: 
    print("ERROR: EL VEHICULO NO CUENTA CON LA POTENCIA SUFICIENTE PARA SER VENDIDO")