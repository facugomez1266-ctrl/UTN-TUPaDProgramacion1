print("=== CAJA DEL KIOSCO ===")

nombre = input("Ingrese el nombre del cliente: ")

while not nombre.isalpha():
    print("Error: ingrese un nombre que contenga solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cantidad = input("Ingrese la cantidad de productos: ")

while not cantidad.isdigit() or int(cantidad) <= 0:
    print("Error: ingrese un número entero positivo.")
    cantidad = input("Ingrese la cantidad de productos: ")

cantidad = int(cantidad)

total_sin_descuentos = 0
total_con_descuentos = 0

for i in range(1, cantidad + 1):

    precio = input(f"Producto {i} - Precio: ")

    while not precio.isdigit():
        print("Error: el precio debe ser un número entero.")
        precio = input(f"Producto {i} - Precio: ")

    precio = int(precio)
    total_sin_descuentos += precio

    descuento = input("¿Tiene descuento? (S/N): ")

    while descuento.lower() != "s" and descuento.lower() != "n":
        print("Error: ingrese S o N.")
        descuento = input("¿Tiene descuento? (S/N): ")

    if descuento.lower() == "s":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuentos += precio_con_descuento

ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad

print()
print(f"Cliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuentos}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")