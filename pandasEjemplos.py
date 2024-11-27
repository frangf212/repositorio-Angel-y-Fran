'''
Instalar pandas(es una libreria externa por lo que tendremos que instalarla mediante pip install pandas
'''

import pandas as pd

'''
Series: Es una estructura unidimensional que puede almacenar cualquier tipo de datos (números, cadenas, etc.). Piensa en una columna de Excel.
'''

s = pd.Series([10, 20, 30, 40])
print(s)


s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)


data = {'Nombre': ['Ana', 'Luis', 'Juan'],
        'Edad': [23, 21, 22],
        'Ciudad': ['Madrid', 'Barcelona', 'Sevilla']}
df = pd.DataFrame(data)
print(df)
print(df['Nombre'])
print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[0:22])
print("Elemento")
print(df.iloc[0, 0])

print(df.loc[0, 'Nombre'])
print(df.describe()) #me gusta mucho
print(df.info())
print(df['Edad']+10)


mayores_21 = df[df['Edad'] > 21]
print(mayores_21)


df1 = pd.DataFrame([{'Nombre':'María', 'Edad':18}, {'Nombre':'Luis', 'Edad':22}, {'Nombre':'Carmen'}])

print(df1)
df_limpiarNulos = df1.dropna()
print(df_limpiarNulos)