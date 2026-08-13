def calculular_masa(): 
    nombre = input("Ingrese su nombre: ")
    densidad = float(input("ingrese la densidad de la sustancia en g/cm^3: "))
    volumen = int(input("Ingrese el volumen de la sustancia en m^3: "))

    densidad_ok = 0.1 <=  densidad <= 20
    
    if densidad_ok:
        print(f"La densidad es de: {densidad}g/cm^3, es segura de manipular")
    else: 
        print(f"La densidad es de: {densidad}g/cm^3, es un riesgo potencial por su peso. NO MANIPULAR ")

    volumen_ok = 10 <= volumen < 500

    if volumen_ok:
        print(f"El volumen es de: {volumen}m^3, es segura de manipular")
    else: 
        print(f"El volumen es de: {volumen}m^3, es un riesgo potencial por su peso. NO MANUPULAR ")
    
    print(f"RESULTADOS FINALES PARA {nombre.upper()}")
    masa = densidad_ok * volumen_ok 

    if masa > 500:
        print(f"PELIGRO: {nombre} la masa es es de {masa}g, es un riesgo potencial por su peso. NO MANUPULAR ")
    else: 
        print(f"{nombre} la masa es de: {masa}g, es segura de manipular")

calculular_masa()