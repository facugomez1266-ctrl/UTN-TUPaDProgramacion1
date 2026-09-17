print("--- BIENVENIDO A LA ARENA ---")

nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3

ataque_pesado = 15
ataque_enemigo = 12

turno_gladiador = True
juego_activo = True

print("\n=== INICIO DEL COMBATE ===")

while juego_activo:

    if turno_gladiador:

        print()
        print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)

        while opcion < 1 or opcion > 3:
            print("Error: opción fuera de rango.")
            opcion = input("Opción: ")

            while not opcion.isdigit():
                print("Error: Ingrese un número válido.")
                opcion = input("Opción: ")

            opcion = int(opcion)

        if opcion == 1:

            if vida_enemigo < 20:
                dano = ataque_pesado * 1.5
                print("¡GOLPE CRÍTICO!")
            else:
                dano = float(ataque_pesado)

            vida_enemigo -= dano

            print(f"¡Atacaste al enemigo por {dano} puntos de daño!")

        elif opcion == 2:

            print(">> ¡Inicias una ráfaga de golpes!")

            for golpe in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        elif opcion == 3:

            if pociones > 0:
                vida_jugador += 30
                pociones -= 1

                print("¡Usaste una poción!")
                print("Recuperaste 30 puntos de vida.")

            else:
                print("¡No quedan pociones!")

        turno_gladiador = False

    else:

        vida_jugador -= ataque_enemigo

        print(f">> ¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")

        turno_gladiador = True

    if vida_jugador <= 0 or vida_enemigo <= 0:
        juego_activo = False

if vida_jugador > 0:
    print("\n¡VICTORIA!")
    print(f"{nombre} ha ganado la batalla.")
else:
    print("\nDERROTA.")
    print("Has caído en combate.")