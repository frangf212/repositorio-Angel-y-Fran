# Datos de calificaciones
import pandas as pd
calificaciones_data = {
    'Estudiante': ['Pedro', 'Lucía', 'Juan', 'Sara'],
    'Matemáticas': [85, 95, 75, 65],
    'Historia': [88, 90, 70, 80],
    'Ciencias': [92, 85, 78, 88]
}

# Crear el DataFrame
df_calificaciones = pd.DataFrame(calificaciones_data)

# 1. Calcular el promedio de cada estudiante
df_calificaciones['Promedio'] = df_calificaciones[['Matemáticas', 'Historia', 'Ciencias']].mean(axis=1)
print("Promedio de cada estudiante:")
print(df_calificaciones[['Estudiante', 'Promedio']])

# 2. Estudiante con el promedio más alto
mejor_estudiante = df_calificaciones[df_calificaciones['Promedio'] == df_calificaciones['Promedio'].max()]
print("\nEstudiante con el promedio más alto:")
print(mejor_estudiante)

# 3. Ordenar a los estudiantes por promedio (descendente)
estudiantes_ordenados = df_calificaciones.sort_values(by='Promedio', ascending=False)
print("\nEstudiantes ordenados por promedio (descendente):")
print(estudiantes_ordenados[['Estudiante', 'Promedio']])