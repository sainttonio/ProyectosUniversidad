def leer_texto(): 
    while True: 
        texto = input("ingrese una frase: ").lower().strip()
        if len(texto) > 0 and texto.replace(" "," ").isalpha():
            return texto
        else:
            print("Error. La Frase no es correcta")

    

def procesar_texto():
    palabras = list
    palabra = str
    new_palabra = str
    texto = str 

    new_palabra = ""
    palabras = texto.split()
    for palabra in palabras: 
        new_palabra = new_palabra + palabra[0]
    print(f"El mensaje oculto es: {new_palabra}")

frase = leer_texto()
procesar_texto(frase)

