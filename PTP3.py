print("=== ESCAPE ROOM: LA BÓVEDA ===")

nombre = input("Ingrese el nombre del agente: ")

while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Ingrese el nombre del agente: ")

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0
bloqueado = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueado:

    if alarma and tiempo <= 3:
        print("¡ALARMA! El sistema bloqueó la bóveda.")
        bloqueado = True
        break

    print("\n==============================")
    print(f"Agente: {nombre}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Alarma: {alarma}")
    print("==============================")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción: ")

    while not opcion.isdigit():
        print("Error: ingrese un número válido.")
        opcion = input("Seleccione una opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Seleccione una opción: ")

        while not opcion.isdigit():
            print("Error: ingrese un número válido.")
            opcion = input("Seleccione una opción: ")

        opcion = int(opcion)

    if opcion == 1:

        forzar_seguidas += 1

        energia -= 20
        tiempo -= 2

        if forzar_seguidas == 3:
            alarma = True
            print("¡La cerradura se trabó!")
            print("¡ALARMA ACTIVADA!")

        else:

            if energia < 40:

                numero = input("Riesgo de alarma. Elige un número del 1 al 3: ")

                while not numero.isdigit():
                    print("Error: ingrese un número válido.")
                    numero = input("Elige un número del 1 al 3: ")

                numero = int(numero)

                while numero < 1 or numero > 3:
                    print("Error: ingrese un número entre 1 y 3.")
                    numero = input("Elige un número del 1 al 3: ")

                    while not numero.isdigit():
                        print("Error: ingrese un número válido.")
                        numero = input("Elige un número del 1 al 3: ")

                    numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡ALARMA ACTIVADA!")
                else:
                    cerraduras_abiertas += 1
                    print("¡Cerradura abierta!")

            else:
                cerraduras_abiertas += 1
                print("¡Cerradura abierta!")

    elif opcion == 2:

        forzar_seguidas = 0

        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo...")

        for paso in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {paso}/4 - Progreso: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("¡Hackeo exitoso! Se abrió una cerradura.")
        else:
            print("El código todavía no es suficiente.")

    elif opcion == 3:

        forzar_seguidas = 0

        tiempo -= 1
        energia += 15

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

        print("Descansas y recuperas energía.")

if cerraduras_abiertas == 3:
    print("\n🎉 ¡VICTORIA!")
    print(f"{nombre} abrió las 3 cerraduras y escapó de la bóveda.")

elif bloqueado:
    print("\n💥 ¡DERROTA!")
    print("El sistema se bloqueó debido a la alarma.")

elif energia <= 0 or tiempo <= 0:
    print("\n💀 ¡DERROTA!")
    print("Te quedaste sin energía o sin tiempo.")