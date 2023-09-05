import random, os

usuarios_registrados = []

def registrar_usuario():
    nombre = input("\n <-- Ingresa tu nombre completo: ")
    email = input("\n <-- Ingresa tu correo electrónico: ")
    telefono = input("\n <-- Ingresa tu número de teléfono: ")
    password = input("\n <-- Ingresa tu contraseña: ")
    usuario = {
        "nombre": nombre,
        "email": email,
        "password": password,
        "telefono": telefono
    }

    usuarios_registrados.append(usuario)
    os.system('cls')
    print("\n Registro exitoso. Ahora puedes iniciar sesión. ")

def iniciar_sesion():
    opcion = input("\n <-- ¿Deseas ingresar con correo o teléfono? correo(1) telefono(2): ")
    if opcion.lower() == "1":
        email = input("\n <-- Ingresa tu correo electrónico: ")
        usuario = next((u for u in usuarios_registrados if u["email"] == email), None)
    elif opcion.lower() == "2":
        telefono = input("\n <-- Ingresa tu número de teléfono: ")
        usuario = next((u for u in usuarios_registrados if u["telefono"] == telefono), None)
    else:
        os.system('cls')
        print("\n Opción inválida. Por favor, intenta de nuevo.")
        iniciar_sesion()
        return
    if usuario:
        contraseña = input("\n <-- Ingresa tu contraseña: ")
        if contraseña == usuario["password"]:
            captcha_resultado = generar_captcha()
            captcha_respuesta = int(input(f"\n <-- Por favor, resuelve la siguiente operación (CAPTCHA): {captcha_resultado['operacion']} = "))
            if captcha_respuesta == captcha_resultado['resultado']:
                os.system('cls')
                print(f"\n Bienvenido/a, {usuario['nombre']}!")
                return True
            else:
                os.system('cls')
                print("\n Captcha incorrecto. Por favor, intenta de nuevo. ")
                ingresar_contraseña(usuario)
                return
        else:
            os.system('cls')
            print("\n Contraseña incorrecta. Por favor, intenta de nuevo.")
            iniciar_sesion()
            return
    else:
        os.system('cls')
        print("\n Usuario no encontrado. Por favor, intenta de nuevo.")
        iniciar_sesion()
        return

def generar_captcha():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    resultado = num1 + num2
    return {"operacion": f"{num1} + {num2}", "resultado": resultado}

def ingresar_contraseña(usuario):
    contraseña = input("\n Ingresa tu contraseña: ")
    if contraseña == usuario["password"]:
        captcha_resultado = generar_captcha()
        captcha_respuesta = int(input(f"\n Por favor, resuelve la siguiente operación (CAPTCHA): {captcha_resultado['operacion']} = "))
        if captcha_respuesta == captcha_resultado['resultado']:
            os.system('cls')
            print(f"\n Bienvenido/a, {usuario['nombre']}!" + "\n")
        else:
            os.system('cls')
            print("\n Captcha incorrecto. Por favor, intenta de nuevo.")
            ingresar_contraseña(usuario)
            return
    else:
        os.system('cls')
        print("\n Contraseña incorrecta. Por favor, intenta de nuevo.")
        iniciar_sesion()
        return

def juego_while():
    vidas = 5
    puntos = 0
    while vidas != 0:
        num = random.randint(0, 9)
        if num == 0:
            vidas -= 1
            print(f"\n Te quedan {vidas} vidas \n")
        else:
            puntos += 1
            print(f"Has ganado {puntos} puntos")
    print("Presiona Enter para continuar...")
    input()

def tarjeta_credito():
    cupo_total = 500
    print(f"\n Bienvenido, tienes un cupo de {cupo_total}")
    nombre = input("\n --> Ingrese su nombre: ")
    compra = int(input("\n --> Ingrese el valor de la compra: "))
    cuotas = int(input("\n --> Ingrese número de cuotas: "))
    if compra <= cupo_total:
        deuda = compra
        cupo_actual = cupo_total - compra
        separacion = compra / cuotas
        print(f"\n <-- Detalle de pagos de {nombre}, ahora tienes un cupo de {cupo_actual} \n")
        i = 1
        while deuda > 1 and i <= cuotas:
            total = cuotas * compra
            if total == cuotas:
                cuota_actual = deuda
            else:
                cuota_actual = separacion
                deuda -= cuota_actual
            print(f" -- Cuota {i}: ${cuota_actual:.2f} - Deuda restante: ${deuda:.2f} \n")
            i += 1 
        print("Presiona Enter para continuar...")
        input()
    else:
        print("\n No se puede hacer la compra")