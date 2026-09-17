print("=== AGENDA DE TURNOS ===")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha():
    print("Error: ingrese solo letras.")
    operador = input("Ingrese el nombre del operador: ")

opcion = 0

while opcion != 5:

    print("\n1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda")
    print("4. Resumen general")
    print("5. Cerrar sistema")

    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número.")
            opcion = input("Opción: ")

        opcion = int(opcion)

    if opcion == 1:

        dia = input("Seleccione día: 1. Lunes / 2. Martes: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Seleccione día: 1. Lunes / 2. Martes: ")

        dia = int(dia)

        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: ingrese solo letras.")
            paciente = input("Nombre del paciente: ")

        if dia == 1:

            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("El paciente ya tiene un turno el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print("Turno reservado.")
            elif lunes2 == "":
                lunes2 = paciente
                print("Turno reservado.")
            elif lunes3 == "":
                lunes3 = paciente
                print("Turno reservado.")
            elif lunes4 == "":
                lunes4 = paciente
                print("Turno reservado.")
            else:
                print("No hay turnos disponibles el lunes.")

        else:

            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("El paciente ya tiene un turno el martes.")
            elif martes1 == "":
                martes1 = paciente
                print("Turno reservado.")
            elif martes2 == "":
                martes2 = paciente
                print("Turno reservado.")
            elif martes3 == "":
                martes3 = paciente
                print("Turno reservado.")
            else:
                print("No hay turnos disponibles el martes.")

    elif opcion == 2:

        dia = input("Seleccione día: 1. Lunes / 2. Martes: ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: seleccione 1 o 2.")
            dia = input("Seleccione día: 1. Lunes / 2. Martes: ")

        dia = int(dia)

        paciente = input("Nombre del paciente: ")

        while not paciente.isalpha():
            print("Error: ingrese solo letras.")
            paciente = input("Nombre del paciente: ")

        encontrado = False

        if dia == 1:

            if lunes1 == paciente:
                lunes1 = ""
                encontrado = True
            elif lunes2 == paciente:
                lunes2 = ""
                encontrado = True
            elif lunes3 == paciente:
                lunes3 = ""
                encontrado = True
            elif lunes4 == paciente:
                lunes4 = ""
                encontrado = True

        else:

            if martes1 == paciente:
                martes1 = ""
                encontrado = True
            elif martes2 == paciente:
                martes2 = ""
                encontrado = True
            elif martes3 == paciente:
                martes3 = ""
                encontrado = True

        if encontrado:
            print("Turno cancelado.")
        else:
            print("Paciente no encontrado.")

    elif opcion == 3:

        print("\n--- LUNES ---")
        print("Turno 1:", lunes1 if lunes1 != "" else "(libre)")
        print("Turno 2:", lunes2 if lunes2 != "" else "(libre)")
        print("Turno 3:", lunes3 if lunes3 != "" else "(libre)")
        print("Turno 4:", lunes4 if lunes4 != "" else "(libre)")

        print("\n--- MARTES ---")
        print("Turno 1:", martes1 if martes1 != "" else "(libre)")
        print("Turno 2:", martes2 if martes2 != "" else "(libre)")
        print("Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1

        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} disponibles")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} disponibles")

        if ocupados_lunes > ocupados_martes:
            print("El lunes tiene más turnos ocupados.")
        elif ocupados_martes > ocupados_lunes:
            print("El martes tiene más turnos ocupados.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")

    elif opcion == 5:
        print("Sistema cerrado.")