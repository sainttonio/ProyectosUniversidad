
def solicitar_nombre():
    print("Ingrese su nombre completo: ")
    nombre = input()
    return nombre 


def solicitar_altura():
    print("Ingrese su altura en metros: ")
    altura = float(input)
    return altura 


def solicitar_edad():
    print("Ingrese su edad: ")
    edad = int(input())
    return edad 

def solicitar_peso(): 
    print("Ingrese su peso en kg: ")
    peso = float(input())
    return peso 


def confirmar_alergia(): 
    print("Si es alergico a algo ingrese 1, si no lo es, ponga 2: ")
    alergia = bool(input())   
    
    if alergia == 1: 
        print("El paciente es alergico ")

    else: 
        print("El paciente no es alergico ")
    return alergia


Nombre = solicitar_nombre()
Edad = solicitar_edad()
Altura = solicitar_altura()
Peso = solicitar_peso()
Alergia = confirmar_alergia()

print(f"-----------FICHA DEL PACIENTE {nombre} ------------")

print("Nombre:{nombre}")
print("Edad: {edad}")   
print("Altura: {altura}")
print("Peso: {peso}")
print("Alergia: {alergia}",)