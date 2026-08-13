def num_palindromo(): 

 
    numero = int(input("Ingresa un número: "))


    numero_original = numero


    numero_invertido = 0

    while numero > 0:

        digito = numero % 10

 
    numero_invertido = numero_invertido * 10 + digito

    numero = numero // 10

    if numero_original == numero_invertido:
        print("El número", numero_original, "ES un palíndromo")
    else:
        print("El número", numero_original, "NO es un palíndromo")

        #aplicar log base 10 para saber el largo de un numero)

num_palindromo()