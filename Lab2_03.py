import pandas as pd
import random


путь_к_файлу = r'C:\Users\marki\Desktop\Lab-2\books-en.csv'


данные_books_en = pd.read_csv(путь_к_файлу, delimiter=';', encoding='ISO-8859-1', on_bad_lines='skip')

данные_books_en['Year-Of-Publication'] = pd.to_numeric(данные_books_en['Year-Of-Publication'], errors='coerce')

утечка_данных = данные_books_en.dropna(subset=['Book-Author', 'Book-Title', 'Year-Of-Publication'])

# Seleccionar 20 registros de manera aleatoria
случайные_регистрации = утечка_данных.sample(n=20)

# Generar las referencias bibliográficas
ссылки = [
    f"{indice + 1}. {row['Book-Author']}. {row['Book-Title']} - {int(row['Year-Of-Publication'])}"
    for indice, row in случайные_регистрации.iterrows()
]

# Guardar las referencias en un archivo de texto
маршрут_выезда = r'C:\Users\marki\Desktop\Lab-2\referencias_bibliograficas.txt'
with open(маршрут_выезда, 'w', encoding='utf-8') as archivo:
    archivo.write("\n".join(ссылки))

print(f"Файл библиографической ссылки, сохраненный в: {маршрут_выезда}")
