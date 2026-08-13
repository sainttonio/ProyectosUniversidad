#BUCLES FOR LISTA SIMPLE\\

nombres = ["sebastian", "angel", "antonella"]

for nombre in nombres: 
   print(f"Hola",nombre)

#FUNCIONES DE LISTAS\\

# .append() = +1 elemento al final ; .lower() = todo minuscula ; .capitalize =  ; .sort() = Ordena alfabeticamente la lista
 #; .remove() = Quita un elemento(Si existe) ; .count() = Cuenta cuantas veces aparece un valor  ; 
 #.reverse() = invierte el orden de la lista. 

colores = ["rojo","amarillo","verde"]

contador = 0

for color in colores: 
    if color == "rojo":
        contador += 1
        print(f"E color elegido es",color)
    else:
       print(f"El color es", color)

 #DICCIONARIOS -> GUARDAN VALORES CON NOMBRE, EJ; (CLAVE -> VALOR)

 #FUNCIONES DEL DICCIONARIO: .keys() ; .values() ; items9() ; get(clave)

#EJEMPLO DE BUCLE CON FOR Y IF; EL BUCLE IMPRIME LA CANTIDAD DE VECES QUE ESTA EL COLOR ROJO EN LA LISTA

colores = ["rojo", "amarillo","verde","rojo", "azul","rojo"] 

contador = colores.count("rojo")

for color in colores: 
    if color == 2:
        contador += 1
        print(contador)
