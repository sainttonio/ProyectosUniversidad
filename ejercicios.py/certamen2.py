'''Mensaje oculto Los mensajes ocultos suelen ser parte de cualquier grupo de 
individuos que desean enviar información en una comunicación, pero que ésta 
realmente “diga” otra cosa. Uno de los mecanismos más utilizados es definir
un mensaje oculto en un texto, mediante la primera letra de cada palabra del
texto, en el orden en que aparecen. 

Dado un texto que consta sólo de letras y 
espacios, devuelva el mensaje oculto. Una palabra es una secuencia finita de 
letras consecutivas. Pueden existir varios espacios entre palabras. Debe validar
que el texto no puede comenzar con un espacio y que posea al menos una letra. Debe
eliminar (si existe) el espacio al final del texto. Como entrada: el usuario ingresa 
una línea, compuesta solo por letras ("a" - "z" y “A” - “Z”) o espacios (" "). Como 
salida: se muestra el mensaje oculto. Recomendación: - Revise la función split(): 
Divide una cadena en varias cadenas (string de string / listas de listas). - Revise
 la función strip(): Elimina carcateres del inicio y del final'''

def verificar_texto(texto): 

    if len(texto) > 0 and texto[0] == " ":
        print("Error: El texto no puede comenzar con un espacio") 
        return False 
    
    if len(texto.strip()) == 0: 
        print("Error: El texto no puede contener al menos una letra")
        return False 

    return True 

def extraer_mensaje_oculto(texto): 

    texto = texto.strip()
    palabras = texto.split()

    mensaje_oculto = ""

    for palabra in palabras: 

        mensaje_oculto += palabra[0]

    return mensaje_oculto

def main(): 

    texto = input("Ingrese el texto: ").lower()

    if verificar_texto(texto): 
        mensaje = extraer_mensaje_oculto(texto)

        print("Mensaje oculto: ", mensaje)

if __name__ == "__main__":

    main()












            

