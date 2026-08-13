import time
import os

def limpiar_pantalla():
    """Limpia la pantalla según el sistema operativo"""
    os.system('cls' if os.name == 'nt' else 'clear')

def corazon_ascii():
    """Dibuja un corazón usando caracteres ASCII"""
    corazon = """
    ♥♥♥♥♥♥♥     ♥♥♥♥♥♥♥
  ♥♥♥♥♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥♥♥♥♥
 ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
 ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
   ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
     ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
      ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
       ♥♥♥♥♥♥♥♥♥♥♥♥♥
        ♥♥♥♥♥♥♥♥♥♥♥
         ♥♥♥♥♥♥♥♥♥
          ♥♥♥♥♥♥♥
           ♥♥♥♥♥
            ♥♥♥
             ♥
    """
    return corazon

def corazon_animado():
    """Muestra un corazón con animación de latido"""
    limpiar_pantalla()
    
    # Corazón pequeño
    corazon_pequeno = """
      ♥♥♥     ♥♥♥
    ♥♥♥♥♥♥♥ ♥♥♥♥♥♥♥
   ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
  ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
   ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
    ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
     ♥♥♥♥♥♥♥♥♥♥♥♥♥
      ♥♥♥♥♥♥♥♥♥♥♥
       ♥♥♥♥♥♥♥♥♥
        ♥♥♥♥♥♥♥
         ♥♥♥♥♥
          ♥♥♥
           ♥
    """
    
    # Corazón grande
    corazon_grande = corazon_ascii()
    
    # Animación de latido
    for i in range(3):
        print(corazon_pequeno)
        time.sleep(0.5)
        limpiar_pantalla()
        print(corazon_grande)
        time.sleep(0.5)
        limpiar_pantalla()

def main():
    """Función principal"""
    print(" Generador de Corazón ")
    print("\nSelecciona una opción:")
    print("1. Corazón estático")
    print("2. Corazón animado (latido)")
    print("3. Salir")
    
    while True:
        try:
            opcion = input("\nIngresa tu opción (1-3): ")
            
            if opcion == "1":
                limpiar_pantalla()
                print(corazon_ascii())
                print("\n💕 ¡Corazón creado con amor! 💕")
                break
                
            elif opcion == "2":
                print("\n Iniciando animación... (Presiona Ctrl+C para detener)")
                time.sleep(1)
                try:
                    while True:
                        corazon_animado()
                except KeyboardInterrupt:
                    limpiar_pantalla()
                    print("\n ¡Animación detenida! ")
                break
                
            elif opcion == "3":
                print("\n ¡Hasta luego! ")
                break
                
            else:
                print(" Opción no válida. Por favor, ingresa 1, 2 o 3.")
                
        except KeyboardInterrupt:
            print("\n\n ¡Hasta luego! ")
            break

if __name__ == "__main__":
    main()