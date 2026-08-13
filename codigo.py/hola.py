rutaArchivo = "texto.txt" #Guardo archivo

miArchivo = open(rutaArchivo, "r")# abro archivo

print(miArchivo) #muestro content archivo

miArchivo.close() #cierro archivo 



""" rutaArchivo= "texto.txt"
    try :
        miArchivo= open(rutaArchivo, "r")
    except: 
        print("Error al abrir el archivo")

    else: 
        print(miArchivo)

        miArchivo.closed.() """  