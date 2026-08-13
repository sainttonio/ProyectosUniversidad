def descifrar_numero(): 
    numero = int(input("Ingrese un numero par: "))
    if numero in numero == numero + 1:
        print("Su numero es : {numero} ")
    elif numero != numero+1:
        print("Su numero no es par, vuelva a ingresar un numero.")
    else:
        print("Error: El programa no reconoce caracter, vuelva a intentar")
descifrar_numero()

def asignacion_valores():
    num = int(input("Asigne un valor para partir: "))
    if num == num+1:
        print("Su numero cumple con los requerimientos")
    elif num != num+1:
        print("Su numero no puede ser procesado por el programa, vuelva a intentar")
    else:
        print("Error: El caracter ingresado no cumple con los requisitos")
asignacion_valores()

def crip_numero():
# para encriptar el nunmero debemos seleccionar una key, la cual puede ser cualquier numero entero
#segun el indice de cada elemento de la cadena debemos sumarle el valor que le asignemos a la key, ej: indice = key 