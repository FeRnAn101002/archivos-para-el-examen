1.py
def generar_codigo(apellido, fecha_nacimiento):
    # Formato de fecha: "DD/MM/AAAA"
    partes_fecha = fecha_nacimiento.split("/")
    mes = partes_fecha[1]
    anio = partes_fecha[2]
    
    # Tomar hasta 4 letras del apellido
    parte_apellido = apellido[:4]
    
    # Si el apellido tiene menos de 4 letras, se usa completo
    if len(apellido) < 4:
        parte_apellido = apellido

    # Tomar los 2 dígitos del mes y los 2 del medio del año
    codigo = f"{parte_apellido}{mes}{anio[1:3]}"
    return codigo

# Ejemplo
apellido = input("Ingrese su apellido: ")
fecha = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
print("Código generado:", generar_codigo(apellido, fecha))
