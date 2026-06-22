"""
Alumnos por curso: calcular la cantidad de alumnos por curso

Promedio total de alumnos y nota maxima a quien corresponde
"""

cursos = ["1A", "1A", "1A", "1B", "1B", "1C", "1C", "1C", "1C", "2D"]

nombres = ["Ana","Luis","Juan","Pedro","Sofia","Carlos","Maria","Jose","Elena","Raul"]

notas = [8, 7, 9, 6, 8, 10, 7, 9, 8, 6]

indice = 0
cant_elementos = len(cursos)
total = 0

while indice < cant_elementos:

    cant_curso = 0
    curso_actual = cursos[indice]
    nombre_actual = nombres[indice]
    nota_actual = notas[indice]
    print(f'\ncurso: {curso_actual}')

    while indice < cant_elementos and cursos[indice] == curso_actual:

        print(f'alumno: {nombres[indice]}')
        print(f'nota: {notas[indice]}')
        cant_curso += 1
        total += notas[indice]
        indice += 1
        

    print(f'\nHay {cant_curso} alumnos en el curso {curso_actual}\n\n')
        
promedio = total / indice


maxima = 0
indice_max = 0
for i in range(len(notas)):
    if notas[i] > maxima:
        maxima = notas[i]
        indice_max = i
alumno_max = nombres[indice_max]
curso_max = cursos[indice_max]
    

print(f'promedio de notas: {promedio}')
print(f'la nota mas alta fue un {max(notas)} y pertenece a {alumno_max} del curso {curso_max}')
