import pandas as pd

# Datos de ejemplo
data = {
    'Producto': ['Televisor', 'Computadora', 'Celular', 'Tablet', 'Cámara', 'Reloj', 'Auriculares'],
    'Precio': [800, 1200, 600, 300, 450, 150, 200],
    'Cantidad': [10, 5, 20, 15, 8, 30, 25],
    'Categoría': ['Electrónica', 'Electrónica', 'Electrónica', 'Electrónica', 'Fotografía', 'Accesorios', 'Accesorios']
}

df = pd.DataFrame(data)
print(df)