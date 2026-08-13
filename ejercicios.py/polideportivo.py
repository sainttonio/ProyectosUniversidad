def verificar_acceso(): 
    
    nombre = str(input("Ingrese su nombre: "))

    edad = int(input("Ingrese su edad: "))

    if edad >= 18: 
        print("Hola " ,nombre)
        print ("puedes pasar, pero debes pagar $5000.")
    elif edad < 18 and edad >= 14:
        print("Hola " ,nombre)
        print("Puedes pasar, pero debes pagar 3000 ")
    else: 
        print("Hola " ,nombre)
        print("Eres menor, no puedes pasar")

verificar_acceso()