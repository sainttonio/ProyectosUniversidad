def evaluacion_cosecha():
    
    nombre = input("Ingrese su nombre: ").capitalize()
    temp_ambiental = int(input("Ingrese la temperatura ambiental: "))
    humedad_relativa = int(input("Ingrese la humedad en terreno: "))
    velocidad_viento = int(input("Ingrese la velocidad del viento: "))

    temp_ok = 15 <= temp_ambiental <= 30
    humedad_ok = humedad_relativa <= 85
    velocidad_ok = humedad_relativa <= 20

    if temp_ok: 
        print(" {nombre} la temperatura está acorde al rango aceptado")
    else: 
        print("ERROR:{nombre} la temperatura está fuera del rango permitido para la cosecha")

    if humedad_ok: 
        print("{nombre} la humedad es está dentro del rango permitido para la cosecha")
    else: 
        print("ERROR: {nombre} la humedad está fuera del rango permitido para la cosecha")
    
    if velocidad_ok: 
        print(" {nombre} la velocidad es correcta, se encuentra dentro del rango permitido")
    else: 
        print("ERROR: {nombre} La velocidad excede el rango permitido para la cosecha")
    
    print(f"------DECISION FINAL PARA {nombre.upper()}")


    if temp_ok and humedad_ok and velocidad_ok: 
        print("{nombre} la cosecha fue permitida, todos los parametros están acorde a lo permitido para llevar a cabo al cosecha")
    else:
        print("PROCESO DENEGADO. Se niega la autorización para que {nombre} pueda llevar a cabo al cosecha, ya que uno o más parametros no cumplen con lo establecido")

evaluacion_cosecha()