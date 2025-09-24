cantidad = 0
suma = 0

decision = ""
while True:
    try:
        numero = float(input("Ingrese un número: "))
        suma += numero
        cantidad += 1
        promedio = suma / cantidad
    except ValueError:
        print("Por favor ingrese un número válido.")
        continue
    decision = input("¿Desea continuar? (si/no): ")
    while decision != "si" and decision != "no":
        print("Opción inválida. Por favor ingrese 'si' o 'no'.")
        decision = input("¿Desea continuar? (si/no): ")
    if decision == "no":
        break
print("El promedio es:", promedio)
