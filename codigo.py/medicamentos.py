def leer_datos(): 
    rutaArchivo = "inventario_medicamentos.csv"
    medicamentos= []

    try: 
        miArchivo = open(rutaArchivo, "r")
    except FileNotFoundError: 
        print(f"El archivo {rutaArchivo} no existe")
        return []

    else: 
        lineas = miArchivo.readlines()
        miArchivo.close()

        for linea in lineas: 
            datos = linea.strip().split()
            medicamentos.append(datos)
        return medicamentos



def procesar_datos(inventario): #procesamos medicamento por medicamento 
    medicamentos_vigentes = []
    for medicamento in inventario: 
        cantidad = int(medicamento[1])
        vigente = medicamento[2]

        tiene_stock = cantidad > 0
        esta_vigente == vigente == "True"

        if tiene_stock and esta_vigente: 
            medicamentos_vigentes.append(medicamento)
    return medicamentos_vigentes





def guardar_datos(lista ): # Inventario de medicamentos actualizado

    ruta = leer_datos()
    inventario_actualizado = procesar_datos(inventario)
    guardar_datos = guardar_datos(inventario_actualizado)
    print("Archivo actualizado correctamente!")
    