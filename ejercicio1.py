
'''Ejercicio 1: Crear un DataFrame de empleados

Tienes una lista de empleados con los siguientes datos:

Nombres: ['Ana', 'Luis', 'Carlos', 'Marta']
Edades: [25, 32, 45, 28]
Salarios: [30000, 40000, 50000, 35000]
Crea un DataFrame con estos datos.
Calcula el salario promedio de los empleados.
Encuentra el empleado con el salario más alto.'''

import pandas as pd
# Datos de empleados
data = {
    'Nombre': ['Ana', 'Luis', 'Carlos', 'Marta'],
    'Edad': [25, 32, 45, 28],
    'Salario': [30000, 40000, 50000, 35000]
}

#Creamos el DataFrame
df = pd.DataFrame(data)

# 1. Mostrar el DataFrame
print("DataFrame de empleados:")
print(df)

# 2. Calcular el salario promedio
salario_promedio = df['Salario'].mean()
print("\nSalario promedio:", salario_promedio)

# 3. Encontrar el empleado con el salario más alto
empleado_salario_alto = df[df['Salario'] == df['Salario'].max()]
print("\nEmpleado con el salario más alto:")
print(empleado_salario_alto)