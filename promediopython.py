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
    decision = input("¿Desea continuar? (s/n): ")
    while decision != "s" and decision != "n":
        print("Opción inválida. Por favor ingrese 's' o 'n'.")
        decision = input("¿Desea continuar? (s/n): ")
    if decision == "n":
        break
print("El promedio es:", promedio)
