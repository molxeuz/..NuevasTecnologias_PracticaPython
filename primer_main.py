import primer_proceso as proc
import os

def mostrar_menu_principal():
    print("\n --> Bienvenido!")
    print("\n 1. Registro de usuario")
    print("\n 2. Inicio de sesión")
    print("\n 3. Salir")

def mostrar_menu_secundario():
    print("\n --> Menú secundario:")
    print("\n 1. Tarjeta de credito")
    print("\n 2. Juego del ciclo While")
    print("\n 3. Cerrar sesión")

opcion = 0
usuario_ingresado = False

while opcion != 3:
    if not usuario_ingresado:
        mostrar_menu_principal()
        opcion = int(input("\n --> Seleccione una opción: "))
        if opcion == 1:
            os.system('cls')
            print("\n Has accedido al registro de usuario.")
            proc.registrar_usuario()
        elif opcion == 2:
            os.system('cls')
            print("\n Has accedido al inicio de sesión.")
            usuario_ingresado = proc.iniciar_sesion()
        elif opcion == 3:
            os.system('cls')
            print("\n Saliendo del programa... \n")
            break
        else:
            os.system('cls')
            print("Opción no válida. Por favor, selecciona una opción del menú. \n")
    else:
        os.system('cls')
        mostrar_menu_secundario()
        opcion = int(input("\n --> Seleccione una opción: "))
        if opcion == 1:
            os.system('cls')
            print("\n Has accedido a la tarjeta de credito")
            proc.tarjeta_credito()
            os.system('cls')
        elif opcion == 2:
            os.system('cls')
            print("\n Has accedido al juego del ciclo While \n")
            print(" Tienes 5 vidas")
            proc.juego_while()
            os.system('cls')
        elif opcion == 3:
            os.system('cls')
            print("\n Saliendo del programa... \n")
            break
        else:
            os.system('cls')
            print("Opción no válida. Por favor, selecciona una opción del menú. \n")