import pandas as pd

путь_к_файлу = r'C:\Users\marki\Desktop\Lab-2\books-en.csv'

# Cargar el archivo CSV con el delimitador correcto
данные_books_en = pd.read_csv(путь_к_файлу, delimiter=';', encoding='ISO-8859-1', on_bad_lines='skip')


# Convertir el campo 'Year-Of-Publication' a tipo numérico, asignando NaN a los valores no convertibles
данные_books_en['Year-Of-Publication'] = pd.to_numeric(данные_books_en['Year-Of-Publication'], errors='coerce')


autor = input("Ingrese el nombre del autor para buscar libros: ")

# Filtrar los registros que cumplen ambas condiciones:
# 1. El autor coincide con el valor ingresado en "Book-Author"
# 2. El "Year-Of-Publication" es mayor a 2000
отфильтрованные_результаты = данные_books_en[
    (данные_books_en['Book-Author'].str.contains(autor, case=False, na=False)) &
    (данные_books_en['Year-Of-Publication'] >= 2000)
]

# Mostrar el número de registros que cumplen ambas condiciones
print(f"Número de libros de '{autor}' publicados después del año 2000: {len(отфильтрованные_результаты)}")

print(отфильтрованные_результаты)

#Имена авторов:Rich Shapero,Amy Tan,Richard Bruce Wright,MICHAEL CRICHTON.и т.д.





