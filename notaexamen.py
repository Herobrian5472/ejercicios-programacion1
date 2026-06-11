"""
Alumnos por curso: calcular la cantidad de alumnos por curso

Promedio total de alumnos y nota maxima a quien corresponde
"""

cursos = ["1A", "1A", "1A", "1B", "1B", "1C", "1C", "1C", "1C", "2D"]

nombres = [
    "Ana",
    "Luis",
    "Juan",
    "Pedro",
    "Sofia",
    "Carlos",
    "Maria",
    "Jose",
    "Elena",
    "Raul",
]

notas = [8, 7, 9, 6, 8, 10, 7, 9, 8, 6]

indice = 0
cant_elementos = len(cursos)
total = 0

while indice < cant_elementos:
    curso_actual = cursos[indice]
    nombre_actual = nombres[indice]
    nota_actual = notas[indice]
    print(f"\ncurso: {curso_actual}")

    # Corte de control
    while indice < cant_elementos and nombres[indice] == nombre_actual:
        total += notas[indice]
        indice += 1
        print(f"alumno: {nombre_actual}")
        print(f"nota: {nota_actual}")

promedio = total / indice


print(f"\nsuma de notas: {total}\n")
print(f"promedio de notas: {promedio}\n")
