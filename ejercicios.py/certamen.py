def validar_texto(texto):
    """
    Valida que el texto cumpla con las condiciones:
    - No puede comenzar con espacio
    - Debe tener al menos una letra
    
    Retorna True si es válido, False si no lo es
    """
    if len(texto) > 0 and texto[0] == " ":
        print("Error: el texto no puede comenzar con un espacio")
        return False
    
    if len(texto.strip()) == 0:
        print("Error: el texto debe tener al menos una letra")
        return False
    
    return True


def extraer_mensaje_oculto(texto):
    """
    Extrae el mensaje oculto del texto tomando la primera letra
    de cada palabra.
    
    Parámetro:
        texto: string con el texto a procesar
    
    Retorna:
        string con el mensaje oculto
    """
    texto = texto.strip()
    
    palabras = texto.split()
    
 
    mensaje_oculto = ""
    for palabra in palabras:  
        mensaje_oculto += palabra[0] 
    
    return mensaje_oculto


def main():
    """
    Función principal que coordina la ejecución del programa
    """
    texto = input("Ingrese el texto: ")
    
    if validar_texto(texto):

        mensaje = extraer_mensaje_oculto(texto)
        print("Mensaje oculto:", mensaje)

if __name__ == "__main__":
    main()