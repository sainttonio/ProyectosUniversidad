'''print ("------Seleccione una opcción-------:   \n1) sumar \n2) restar \n3) multiplicar \n4) dividir ")
opcion_usuario = int(input())

if opcion_usuario == 1:
    primer_numero = int(input("Ingrese un numero: "))
    segudno_numero = int(input("Ingrese un segundo numero: " ))
    print(f"EL NUMERO ES: ",primer_numero + segudno_numero)

elif opcion_usuario == 2:
    primer_numero = int(input("Ingrese un numero: "))
    segudno_numero = int(input("Ingrese un segundo numero: " ))
    print(f"EL NUMERO ES: ",primer_numero - segudno_numero)

elif opcion_usuario == 3: 
    primer_numero = int(input("Ingrese un numero: "))
    segudno_numero = int(input("Ingrese un segundo numero: " ))
    print(f"EL NUMERO ES: ",primer_numero * segudno_numero)

else: 
    primer_numero = int(input("Ingrese un numero: "))
    segudno_numero = int(input("Ingrese un segundo numero: " ))
    print(f"EL NUMERO ES: ",primer_numero / segudno_numero)'''


''' FUNCION: GENERA UNA RELACION ENTRE ELEMENTOS 

    LAS FUNCIONES SON CODIGOS LOCALES, SON VOLATILES, VAN LIGADOS A TEMAS DE TEMPORALIDAD, NACEN, SE USAN, Y MUEREN EN LA MISMA DINTANCIA DE TIEMPO 
    '''

def sumar_num(x,y): 

    sumar= x + y

    return sumar 

x = 20
y= 4
resultado_suma = sumar_num(x,y)



def restar_num(x,y): 

    restar= x - y

    return restar

x = 20
y= 4
resultado_resta = restar_num(x,y)



def multiplicar_num(x,y): 

    multiplicar= x * y

    return multiplicar

x = 20
y= 4
resultado_multiplicacion = multiplicar_num(x,y)



def dividir_num(x,y): 

    dividir = x /y

    return dividir 

x = 20
y= 4
resultado_division = dividir_num(x,y)


print(resultado_suma)
print(resultado_resta)
print(resultado_multiplicacion)
print(resultado_division)



'''def seleccionar_opcion():

    print ("------Seleccione una opcción-------:   \n1) sumar \n2) restar \n3) multiplicar \n4) dividir ")
    
    opcion_usuario = int(input())
    return opcion_usuario

seleccionar_opcion()

def sumar_numero(primer_numero: int, segundo_numero: int ): 
        
        primer_numero = input("Ingrese un numero: ")
        segundo_numero = input("Ingrese un segundo numero: " )
        resultado_suma = print(f"EL NUMERO ES: ",primer_numero + segundo_numero)
        return resultado_suma
sumar_numero()


def restar_numero(primer_numero: int, segundo_numero: int ):
        
        primer_numero = input("Ingrese un numero: ")
        segundo_numero = input("Ingrese un segundo numero: " )
        resultado_resta = print(f"EL NUMERO ES: ",primer_numero - segundo_numero)
        return resultado_resta
restar_numero()

def multiplicar_numero(primer_numero: int, segundo_numero: int ):
        
        primer_numero = input("Ingrese un numero: ")
        segundo_numero = input("Ingrese un segundo numero: " )
        resultado_multiplicacion = print(f"EL NUMERO ES: ",primer_numero * segundo_numero)
        return multiplicar_numero
multiplicar_numero()

def dividir_numero(primer_numero: int, segundo_numero: int ): 
        
        primer_numero = input("Ingrese un numero: ")
        segundo_numero = input("Ingrese un segundo numero: " )
        resultado_division = print(f"EL NUMERO ES: ",primer_numero / segundo_numero)
        return resultado_division'''



