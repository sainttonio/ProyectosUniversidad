#-----EVALUACION DE CONDICIONES AMBIENTALES EN FAENA MINERA SUBTERRANEA-----

#PARA QUE EL PERSONAL PUEDA ACCEDER DEBEN CUMPLIRSE CIERTOS REQUISITOS EN EL AREA 

# 1. CONCENTRACION DE MONOXIMO DE CARBONO (CO) DEBE SER IGUAL O INFERIOR A  25ppm 
# 2. NIVEL DE OXIGENO (O2) DEBE ESTAR ENTRE 19.5% y 23.5% 
# 3. TEMPERATURA AMBIENTAL DEBE ESTAR POR DEBAJO DEL LOS 30 GRADOS PARA PREVENIR GOLPES DE CALOR 

# SI SE CUMPLEN TODOS LOS PARAMETROS, SE PERMITE EL INGRESO ; SI SE INCUMPLE AUNQUE SEA UNO, SE DENIEGA EL PERMISO AUTOMATICAMENTE 

def ingreso_usuario(): 

    nombre = str(input("Ingrese su nombre: "))
    concentracion_co = int(input("Ingrese la concentración de CO: "))
    nivel_o2 = float(input("Ingrese el nivel de oxigeno: "))
    temperatura = float(input("Ingrese la temperatura ambiental: "))

    concentracion_ok = concentracion_co <= 25
    oxigeno_ok =  19.5 <= nivel_o2 <= 23.5
    temperatura_ok = temperatura <= 30

    if concentracion_ok:
        print(f"Concentración: {concentracion_co}, está dentro del rango normal, puede ingresar")
    else: 
        print(f"Concentración: {concentracion_co}, estáfuera del rango normal, no puede ingresar")

    if oxigeno_ok: 
        print(f"Nivel de oxigeno: {nivel_o2}, está dentro del rango permitido, puede ingresar")
    else: 
        print(f"Nivel de oxigeno: {nivel_o2}, está fuera del rango permitido, acceso denegado")
    
    if temperatura_ok: 
        print(f"Temperatura ambiental: {temperatura}, se encuentra dentro de lo normal, puede ingresar")
    else: 
        print(f"Temperatura: {temperatura}, se encuentra fuera de lo normal, no puede ingresar")

#DECISION FINAL DEL PROGRAMA

    print(f"------RESULTADOS PARA {nombre.upper()}---------")

    if concentracion_ok and oxigeno_ok and temperatura_ok:
        print(f"ACCESO PERMITIDO PARA {nombre.upper()} !")
        print(f"{nombre}. Dado que todos los parametros están dentro del rango correcto, puede ingresar a terreno")

    else: 
        print(f"ACCESO DENEGADO PARA {nombre.upper()}")
        print(f"{nombre}. Dado a que uno o más parametros no cumplen con lo establecido, se deniega el acceso por ambiente poco seguro para trabajador")

ingreso_usuario()