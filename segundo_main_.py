# Hacer un ejercicio el cual me permita ingresar los ingresos y las deduciones que he tenido en mi cuenta, que cada vez que ingrese esos datos me pida una confirmacion de que si eso es todo lo que ha habido de movimientos en la cuenta, si es lo contrario me envie el total de las ganancias que he tenido si es ganancias y si es perdida que lo especifique al enviar el mensaje

def mostrar_menu():
    print("\n-- Administrador de Finanzas --")
    print("1. Registrar Ingreso")
    print("2. Registrar Deducción")
    print("3. Mostrar Balance")
    print("4. Salir")

ingresos = []
deducciones = []

while True:

    mostrar_menu()
    
    opcion = input("\n--> Seleccione una opción: ")

    if opcion == "1":
        
        try:
    
            ingreso = float(input("\n<-- Ingrese el monto del ingreso: "))
            
            ingresos.append(ingreso)
            
            print(f"<-- Ingreso registrado: ${ingreso:.2f}\n")
            
        except ValueError:
            
            print("Entrada inválida. Introduzca un número válido.")

    elif opcion == "2":
        
        try:
            
            deduccion = float(input("\n<-- Ingrese el monto de la deducción: "))
            
            deducciones.append(deduccion)
            
            print(f"<-- Deducción registrada: ${deduccion:.2f}\n")
            
        except ValueError:
            
            print("\nEntrada inválida. Introduzca un número válido.")

    elif opcion == "3":
        
        total_ingresos = sum(ingresos)
    
        total_deducciones = sum(deducciones)
    
        saldo = total_ingresos - total_deducciones
        
        if saldo > 0:
    
            print(f"\n<-- Balance total: ${saldo:.2f} (Ganancias)")
    
        elif saldo < 0:
    
            print(f"\nBalance total: ${saldo:.2f} (Pérdidas) <--")
    
        else:
    
            print("\nBalance total: $0.00 (Sin cambios en el saldo) <--")

    elif opcion == "4":
        
        print("\nSaliendo del programa...")
        
        break

    else:
        
        print("Opción no válida. Por favor, seleccione una opción del menú.")