class Examen:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def aprobado(self):
        return self.nota >= 10.5

# Solicitar datos
nombre = input("Ingrese el nombre del estudiante: ")
nota = float(input("Ingrese la nota del estudiante: "))

# Crear objeto Examen
examen = Examen(nombre, nota)

# Mostrar si aprobó o no
if examen.aprobado():
    print(f"{nombre} aprobó el examen.")
else:
    print(f"{nombre} no aprobó el examen.")
