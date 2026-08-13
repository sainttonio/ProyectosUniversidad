#Ejercicio 5: Sistema de Multas de Tránsito
#Las multas de velocidad funcionan así:
#Velocidad permitida: 60 km/h check
#Multa base: $50000 por cada km/h de exceso che
#Si el exceso es múltiplo de 10 km/h, multa se duplica
#Si supera los 100 km/h, multa adicional de $200000
#Crear: Programa que calcule la multa total.

def validar_velocidad(velocidad: int):

    if velocidad > 60:
        return True 
    
    
def calcular_exceso(exceso: int): 
    if exceso % 10 == 0: 
        return True 
    
    
ingresar_velocidad = int(input("Ingrese la velocidad a la que circula el vehiculo: "))

if validar_velocidad(ingresar_velocidad):
    exceso = ingresar_velocidad - 60
    multa = exceso * 50000

    if calcular_exceso(ingresar_velocidad):
        multa = exceso * 2
    else:
        multa = multa 
    if ingresar_velocidad > 100: 
        multa = multa + 200000

    print(f'La velocidad del vehiculo es": {ingresar_velocidad} Km/h')
    print(f'El exceso de velocidad es de : {exceso} km/h')
    print(f'La multa a pagar es de: ${multa} clp')
else: 
    print(f'No hay multa, el vehiculo se encuentra circulando a una velocidad de {ingresar_velocidad} Km/h y es correcta')

