def suma_y_resta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

# Solicitar números al usuario
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Llamar a la función
suma, resta = suma_y_resta(num1, num2)

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
