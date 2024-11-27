'''Ejercicio 2: Filtrar productos por precio

Se te da un DataFrame con la siguiente información sobre productos:

Productos: ['Televisor', 'Computadora', 'Celular', 'Tablet']
Precios: [800, 1200, 600, 300]
Filtra los productos que tienen un precio mayor a 500.
Encuentra el producto con el precio más bajo.
Ordena los productos por precio de forma ascendente.'''
import pandas as pd
# Datos de productos
productos_data = {
    'Producto': ['Televisor', 'Computadora', 'Celular', 'Tablet'],
    'Precio': [800, 1200, 600, 300]
}

# Crear el DataFrame
df_productos = pd.DataFrame(productos_data)

#Filtrar los productos con precio mayor a 500
productos_filtrados = df_productos[df_productos['Precio'] > 500]
print("Productos con precio mayor a 500:")
print(productos_filtrados)

#Producto con el precio más bajo
producto_barato = df_productos[df_productos['Precio'] == df_productos['Precio'].min()]
print("\nProducto con el precio más bajo:")
print(producto_barato)

#Ordenar los productos por precio (ascendente)
productos_ordenados = df_productos.sort_values(by='Precio')
print("\nProductos ordenados por precio (ascendente):")
print(productos_ordenados)