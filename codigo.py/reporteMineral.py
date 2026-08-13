def leer_datos(): 
    rutaArchivo = "reporte_mineral.txt" #Guardo archivo
    reportes = []
    try: 
        miArchivo = open(rutaArchivo, "r")# abro archivo
    except FileNotFoundError:
        print(f"El archivo {rutaArchivo} no existe")
    else:
        lineas = miArchivo.readlines() #leo lineas del archivo
        miArchivo.close() #cierro archivo
        for linea in lineas:
            reportes.append(linea.strip()) #agrego linea a la lista reportes
        return reportes
    

def procesar_datos(registros: list): 
    sum_oro= 0
    sum_plata= 0 
    sum_cobre= 0
    resumen = ""
    if len(registros) > 0:
        for registro in registros:
            datos = registro.split("-") #separo los datos por coma
            if datos[0] == "oro":
                sum_oro += int(datos[1])      # o float(datos[1]) si puede tener decimales
            elif datos[0] == "plata":
                sum_plata += int(datos[1])
            else:
                sum_cobre += int(datos[1])
            resumen = f"Total Oro: {sum_oro} \nTotal Cobre: {sum_cobre} \nTotal Plata: {sum_plata}" #muestro el resumen de los datos procesados
    else: 
        print("El registro no se puede procesar porque no hay datos")
    return resumen



def escrbir_datos(resumen_registro):
    rutaArchivo = "resumen_mineral.txt" #Guardo archivo
    try: 
        miArchivo = open(rutaArchivo, "w")# abro archivo
    except FileNotFoundError:
        print(f"El archivo {rutaArchivo} no existe")
    else:
        miArchivo.write(resumen_registro) #escribo el resumen en el archivo
        miArchivo.close() #cierro archivo 


registros_mineral = leer_datos() #llamo a la funcion leer_datos
resumen_registro= procesar_datos(registros_mineral) #llamo a la funcion procesar_datos
escrbir_datos(resumen_registro) #llamo a la funcion escrbir_datos
