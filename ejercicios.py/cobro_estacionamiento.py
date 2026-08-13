def validar_tiempo(tiempo_estacionado: int):

    if 1 <= tiempo_estacionado <= 12:   
        return True 
    else:
        return False 
    
def verificar_descuento(tiempo: int):

    if tiempo % 3 == 0: 
        return True 
    else:
        return False

if __name__ == "__main__":

    tiempo_estacionado = int(input("ingrese el tiempo estacionado en horas: "))

    if validar_tiempo(tiempo_estacionado): 

        cobro = tiempo_estacionado * 500

        if verificar_descuento(tiempo_estacionado):
            cobro = cobro - 300
    
        if tiempo_estacionado > 8:
            cobro = cobro + 1000

        print(f"Debe pagar ${cobro}clp por el tiempo estacionado")

    else: 
        print("Error: El tiempo de estacionamiento debe ser de minimo 1 hora y maximo 12") 