def calculadora(): 
    
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input('Ingrese el segundo número: '))

    eleccion = 0

    while True: 

        print('''
    Indique su elección 
    
    1. suma 
    2. resta
    3. multiplicación
    4. división
    5. cambiar números introducidos 
    6. salir
          ''')

        eleccion = int(input())

        if eleccion == 1:
            print("")
            print("Resultado: ", num1, " + ", num2, " = ", num1+num2)
        elif eleccion == 2: 
            print("")
            print("Resultado: ", num1, "-", num2, "=", num1-num2)
        elif eleccion == 3: 
            print("")
            print("Resultado: ", num1, "*", num2, "=", num1*num2)
        elif eleccion == 4: 
            print("")
            if num2 != 0:
                print("Resultado: ", num1, "//", num2, "=", num1//num2)
            else:
                print("Error: No se puede dividir por cero")
        elif eleccion == 5:
            num1 = int(input("Ingrese el primer número: "))
            num2 = int(input('Ingrese el segundo número: '))
        elif eleccion == 6:
            print("Saliendo...")
            break
        else:
            print("Opción inválida")

calculadora()