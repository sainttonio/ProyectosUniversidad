 # 1. verificar/leer codigo ; 2. verificar clave; 3. sumar posiciones ; 4 verificar intentos
#usar .index() para recorrer tupla con funcion
# contraseña de prueba correcta: ---- abcdeabcde -------
def leer_codigo():
    letras = input('Ingrese el código de desbloquéo o pague 300 bitcoins: ').lower()
    

leer_codigo()
# 1. verificar/leer codigo ; 2. verificar clave; 3. sumar posiciones ; 4 verificar intentos
#usar .index() para recorrer tupla con funcion

def verificar_codigo(clave: str):
   return len('clave') == 10 and clave.isalpha()

verificar_codigo(clave = str)


def suma_posiciones(codigo: str, letras: str, suma: int): 

    letras = ['abcdefghijklmnñopqrstuvwxyz']
    suma = 0

    for letra in letras:  #error, variable no iterable 
        suma = suma + letras.index(letra) +1
    return suma 

suma_posiciones(codigo = str)

def intentos(suma: int, desbloqueo: bool,intento: int, codigo: str): #mejor utilizar un bucle while que parta en 3 y al llegar a 0 
                                                                    #imprima mensaje de pagar bitcoins 

    if intento and desbloqueo == 1:
        print('Clave incorrecta, vuelve a intentar. (Tienes 2 intentos más)')
    elif intento and desbloqueo == 2: 
        print('Clave incorrecta, vuelve a intentar. (Tienes solo 1 intento más)')
    else:
        print("Clave incorrecta!, paga 300 bitcoins para liberar el equipo")

intentos(suma = int, desbloqueo = bool,intento = int, codigo = str)


 
leer_codigo()
verificar_codigo() 
suma_posiciones() 
intentos()
#REVISAR ERRORES DE PROGRAMA 

