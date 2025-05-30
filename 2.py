def filtrar_nombres_por_ultima_letra(nombres):
    if not nombres:
        return []
    
    letra_final = nombres[-1][-1].lower()  # Última letra del último nombre
    return [nombre for nombre in nombres if nombre[-1].lower() == letra_final]

# Ejemplo
n = int(input("¿Cuántos nombres ingresará?: "))
nombres = [input(f"Ingrese nombre {i+1}: ") for i in range(n)]
resultado = filtrar_nombres_por_ultima_letra(nombres)
print("Nombres que cumplen la condición:", resultado)
