def verificar_codigo(codigo):
    letras = "abcdefghijklmnopqrstuvwxyz"
    acum = 0

    for letra in codigo:
        if letra in letras:
            letras_index = letras.index(letra)
            acum += letras_index + 1

    if acum != 0 and acum % 10 == 0: return True
    return False

intentos = 0

while intentos < 3:
    print(f"Ingrese el código de desbloqueo o deposite 300 Bitcoins.")
    codigo_desbloqueo = input()
    if verificar_codigo(codigo_desbloqueo): 
        print(f"¡Lograste desbloquear tu equipo en el intento {intentos}!")
        exit()
    else: print(f"Error. Código incorrecto. Ya tienes {intentos + 1} intento(s). ")
    intentos += 1

print("Ha Ha Ha! No lograste desbloquear tu equipo. Debes pagar 300 Bitcoins.")

#OCUPAR VARIABLES ACUMULADORAS PARA NO PERDER EL VALOR ENTRANTE Y SUMARLO EN SALIDA
#PRIORIZAR CODIGO CON MENOS FUNCIONES PERO CON MEJOR SINTAXIS PARA APROVECHAR LOS BUCLES DE MEJOR FORMA
#EL BUCLE NECESITA UNA VARIABLE INICIALIZADORA PARA PODER TENER UN PUNTO DE PARTIDA Y DISMINUIR/AUMENTAR AL PASAR LOS CICLOS 
#PENSAR BIEN LAS CONDICIONALES Y FUNCIONES .() QUE UTILIZARE PARA ACORTAR CODIGO 
#El codigo no salió como lo tenia pensado, pero se hizo lo que se pudo, el siguiente semestre con todo xD

exit()

