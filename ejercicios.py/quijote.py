def leer_texto():
    texto = input("Ingrese un texto: ")
    
    

    print("El texto ingresado es :")
    print(texto)

#cont frecuencia
    frecuencia = {}
    
    
    for letra in texto:
        letra = letra.lower() 
        if letra in frecuencia and letra.isalnum():
            frecuencia[letra] += 1
        elif letra.isalnum():
            frecuencia[letra] = 1


    print("Frecuencia de cada letra:")
    for letra, cantidad in frecuencia.items():
        print(f"'{letra}': {cantidad}")

leer_texto()


