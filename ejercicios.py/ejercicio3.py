def leer_comentario():
   
    while True:
        comentario = input("Ingrese el comentario: ")
        
        if not comentario.strip():
            print("Error: El comentario no puede estar vacío. Vuelva a solicitar la entrada.")
            continue
        
        noValido = False
        for char in comentario:
            if not (char.isalpha() or char.isdigit() or char == ' ' or char == '!'):
                noValido = True
                break
        
        if noValido:
            print("Error: El comentario contiene caracteres no permitidos. Vuelva a solicitar la entrada.")
            continue
        
        return comentario.lower() 

def procesar_comentario(comentario):
    
    frecuencia_letras = {}
    signos_exclamacion = 0
    digitos = 0
    
    for char in comentario:
        if char.isalpha():
            if char in frecuencia_letras:
                frecuencia_letras[char] += 1
            else:
                frecuencia_letras[char] = 1
        elif char == '!':
            signos_exclamacion += 1
        elif char.isdigit():
           
            digitos += 1
      
    
    analisis = ""
    
    letras_ordenadas = sorted(frecuencia_letras.keys())
    elementos_analisis = []
    
    for letra in letras_ordenadas:
        elementos_analisis.append(f"{letra}:{frecuencia_letras[letra]}")
    
    if signos_exclamacion > 0:
        elementos_analisis.append(f"!:{signos_exclamacion}")
    
    if digitos > 0:
        elementos_analisis.append(f"dígitos:{digitos}")
    
    analisis = ";".join(elementos_analisis) + ";"
    
    return analisis

if __name__ == "__main__":
    print("=== Análisis de Comentarios - HappyChileanTravellers ===")
    print("Ingrese comentarios para analizar su frecuencia de caracteres.")
    print("Caracteres permitidos: letras, números, espacios y signos de exclamación (!)")
    print()
    
    while True:
        try:
            comentario = leer_comentario()
            
       
            resultado = procesar_comentario(comentario)
            print(f"Análisis: {resultado}")
            print()
        
            continuar = input("¿Desea analizar otro comentario? (s/n): ").lower()
            if continuar != 's':
                break
                
        except KeyboardInterrupt:
            print("\nPrograma terminado por el usuario.")
            break
        except Exception as e:
            print(f"Error inesperado: {e}")
            continue
    
    print("¡Gracias por usar el analizador de comentarios!")