print("=== ACCESO AL CAMPUS ===")

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3 and not acceso:

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        acceso = True
    else:
        intentos += 1
        print("Usuario o clave incorrectos.")

if not acceso:
    print("Cuenta bloqueada.")
else:

    opcion = 0

    while opcion != 4:

        print("\n1) Estado de inscripción")
        print("2) Cambiar clave")
        print("3) Mensaje motivacional")
        print("4) Salir")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        while opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: ingrese un número válido.")
                opcion = input("Opción: ")

            opcion = int(opcion)

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva_clave = input("Nueva clave: ")

            if len(nueva_clave) < 6:
                print("Error: mínimo 6 caracteres.")
            else:
                confirmacion = input("Confirme la nueva clave: ")

                if nueva_clave == confirmacion:
                    clave_correcta = nueva_clave
                    print("Clave cambiada correctamente.")
                else:
                    print("Error: las claves no coinciden.")

        elif opcion == 3:
            print("¡Seguí adelante, cada día estás más cerca de tu objetivo!")

        elif opcion == 4:
            print("Sesión finalizada.")