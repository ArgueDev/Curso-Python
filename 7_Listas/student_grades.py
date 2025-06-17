# Sistema de notas de alumunos por asignatura

math_class = [0] * 7
history_class = [0] * 7
language_class = [0] * 7

sum_math_grades = 0
sum_history_grades = 0
sum_language_grades = 0

print('Ingrese 7 notas de estudiantes para Matematicas')
for i in range(7):
    math_class[i] = float(input(f'Nota {i + 1}: '))


print('Ingrese 7 notas de estudiantes para Historia')
for i in range(7):
    history_class[i] = float(input(f'Nota {i + 1}: '))


print('Ingrese 7 notas de estudiantes para Lenguaje')
for i in range(7):
    language_class[i] = float(input(f'Nota {i + 1}: '))


for i in range(7):
    sum_math_grades += math_class[i]
    sum_history_grades += history_class[i]
    sum_language_grades += language_class[i]


average_math = sum_math_grades / 7
avergare_history = sum_history_grades / 7
average_language = sum_language_grades / 7

print(f'Promedio Matematicas: {average_math:.2f}')
print(f'Promedio Historia: {avergare_history:.2f}')
print(f'Promedio Lenguaje: {average_language:.2f}')

total_average = (average_math + average_language + avergare_history) / 3

print(f'Total General: {total_average:.2f}')

student_id = int(input('Ingrese el identificador del estudiante de 1 a 7: ')) - 1
student_average = (math_class[student_id] + history_class[student_id] + language_class[student_id]) / 3

print(f'Promedio del alumno Nro {student_id+1}: {student_average:.2f}')