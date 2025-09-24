"""
Calcula el promedio final ponderado a partir de:
- Porcentaje de Examen
- Porcentaje de Tareas
- Calificación del Examen
- Varias calificaciones de Tareas (se promedian y luego se ponderan)

Validaciones incluidas:
- Los porcentajes deben ser números entre 0 y 100 y sumar 100.
- Las calificaciones deben estar entre 0 y 100.
"""

def leer_float(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue
            return valor
        except ValueError:
            print("Por favor ingrese un número válido.")


print("=== Cálculo de Promedio Ponderado (Examen / Tareas) ===")

# 1) Leer porcentajes
porcentaje_examen = leer_float("Ingrese el % del Examen (0-100): ", 0, 100)
porcentaje_tareas = leer_float("Ingrese el % de las Tareas (0-100): ", 0, 100)

while round(porcentaje_examen + porcentaje_tareas, 6) != 100.0:
    print("La suma de porcentajes debe ser exactamente 100. Intente nuevamente.")
    porcentaje_examen = leer_float("% Examen: ", 0, 100)
    porcentaje_tareas = leer_float("% Tareas: ", 0, 100)

# 2) Leer calificación de examen
cal_examen = leer_float("Ingrese la calificación del Examen (0-100): ", 0, 100)

# 3) Leer calificaciones de tareas (múltiples)
print("Ingrese calificaciones de Tareas (0-100). Escriba 'n' para terminar.")
suma_tareas = 0.0
cantidad_tareas = 0
while True:
    entrada = input("Calificación de tarea (o 'n' para terminar): ").strip().lower()
    if entrada == 'n':
        if cantidad_tareas == 0:
            print("Debe ingresar al menos una calificación de tarea.")
            continue
        break
    try:
        cal = float(entrada)
        if cal < 0 or cal > 100:
            print("La calificación debe estar entre 0 y 100.")
            continue
        suma_tareas += cal
        cantidad_tareas += 1
    except ValueError:
        print("Entrada inválida. Ingrese un número o 'n' para terminar.")

promedio_tareas = suma_tareas / cantidad_tareas

# 4) Cálculo ponderado final
final = (cal_examen * (porcentaje_examen / 100.0)) + (promedio_tareas * (porcentaje_tareas / 100.0))

print("\n=== Resultado ===")
print(f"% Examen: {porcentaje_examen:.2f}% | % Tareas: {porcentaje_tareas:.2f}%")
print(f"Calif. Examen: {cal_examen:.2f}")
print(f"Promedio Tareas: {promedio_tareas:.2f} (con {cantidad_tareas} tareas)")
print(f"Promedio Final Ponderado: {final:.2f}")
