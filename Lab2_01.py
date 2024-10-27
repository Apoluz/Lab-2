import pandas as pd

# Configuración para mostrar todo el contenido de las celdas
pd.set_option('display.max_colwidth', None)

# Cargar el archivo CSV
данные = pd.read_csv('C:/Users/marki/Desktop/Lab-2/books.csv', delimiter=';', encoding='cp1251', on_bad_lines='skip')

# Convertir el campo 'Дата поступления' a tipo fecha
данные['Дата поступления'] = pd.to_datetime(данные['Дата поступления'], errors='coerce', dayfirst=True)

# Filtrar los registros que cumplen ambas condiciones:
# 1. Longitud de 'Название' mayor a 30 caracteres
# 2. 'Дата поступления' posterior a 2018
Записи_удовлетворяющие_обоим_условиям = данные[(данные['Название'].str.len() > 30) & (данные['Дата поступления'].dt.year > 2018)]

# Mostrar el número de registros que cumplen ambas condiciones
print(f"Количество записей, удовлетворяющих обоим условиям: {len(Записи_удовлетворяющие_обоим_условиям)}")

# Mostrar los registros que cumplen ambas condiciones
print(Записи_удовлетворяющие_обоим_условиям)


