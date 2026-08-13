# PROGRAMA DE INGRESO A MINERA ESCONDIDA

# PARA QUE EL TRABAJADOR PUEDA INGRESAR A MINERA DEBE CUMPLIR CON LOS SIGUIENTES REQUISITOS: 
# - LA TEMPERATURA CORPORAL DEBE ESTAR ENTRE 36.1 - 37.2 GRADOS
# - LA FRECUENCIA RESPIRATORIA DEBE ESTAR ENTRE 12 Y 20 RESPIRACIONES POR MINUTO (RPM)
# SI AMBAS SE CUMPLEN, EL TRABAJADOR PUEDE SUBIR A LA MINA, 
# SI NO, EL TRABAJADOR TIENE ACCESO DENEGADO A SUBIR A MINERA.

def ingreso_usuario(): 
    print("=== SISTEMA DE CONTROL DE ACCESO - MINERA ESCONDIDA ===\n")
    
 
    nombre = input("Ingrese su nombre: ").strip()
    
    try:
        temperatura = float(input("Ingrese su temperatura corporal (°C): "))
        frecuencia_respiratoria = int(input("Ingrese su frecuencia respiratoria (respiraciones por minuto): "))
    except ValueError:
        print("Error: Debe ingresar valores numéricos válidos.")
        return
  
    temperatura_ok = 36.1 <= temperatura <= 37.2
    frecuencia_ok = 12 <= frecuencia_respiratoria <= 20
    
    print(f"\n--- RESULTADOS PARA {nombre.upper()} ---")
    
   
    if temperatura_ok:
        print(f"✓ Temperatura: {temperatura}°C - DENTRO DEL RANGO NORMAL")
    else:
        print(f"✗ Temperatura: {temperatura}°C - FUERA DEL RANGO NORMAL (36.1-37.2°C)")
    

    if frecuencia_ok:
        print(f"✓ Frecuencia respiratoria: {frecuencia_respiratoria} rpm - DENTRO DEL RANGO NORMAL")
    else:
        print(f"✗ Frecuencia respiratoria: {frecuencia_respiratoria} rpm - FUERA DEL RANGO NORMAL (12-20 rpm)")
    

    print("\n" + "="*50)
    if temperatura_ok and frecuencia_ok:
        print(f"ACCESO AUTORIZADO para {nombre}")
        print("Ambos parámetros están dentro del rango. Puede ingresar a la minera.")
    else:
        print(f" ACCESO DENEGADO para {nombre}")
        print("No cumple con todos los parámetros establecidos.")
        print("No puede ingresar a la minera por razones de seguridad.")
    print("="*50)

def main():
    while True:
        ingreso_usuario()
        
        continuar = input("\n¿Desea realizar otra consulta? (s/n): ").lower().strip()
        if continuar not in ['s', 'si', 'sí', 'yes', 'y']:
            print("Gracias por usar el sistema de control de acceso.")
            break
        print("\n" + "-"*60 + "\n")

# Ejecutar el programa
if __name__ == "__main__":
    main()