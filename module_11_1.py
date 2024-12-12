import matplotlib.pyplot as plt
import pandas as pd
from prettytable import PrettyTable
import os
from PIL import Image
import sys

#Библиотека matplotlib

fig, ax = plt.subplots()                                                  # Создайте фигуру, содержащую одну ось.
ax.plot([4, 3, 3, 4], [1, 2, 4, 3], [4, 5, 5, 4], [1, 2, 4, 3])    # Нарисуйте некоторые данные на оси.
plt.show()                                                                # Покажите фигуру.


#Библиотека pandas

def load_excel_file(file_path):                     # Загружает данные из Excel файла.
    if not os.path.exists(file_path):
        print(f"Файл {file_path} не найден.")
        return None
    df = pd.read_excel(file_path)
    return df

def display_data_in_table(df):                      # Отображает данные в виде таблицы в консоли.
    table = PrettyTable()                           # Создаем объект PrettyTable
    table.field_names = df.columns.tolist()         # Добавляем заголовки
    for index, row in df.iterrows():                # Добавляем строки из DataFrame
        table.add_row(row.tolist())
    print(table)                                    # Печатаем таблицу

def main():
    file_path = 'C:\ProjectsForUniversity\pythonProject\My\merch.xlsx'  # Укажите путь к вашему Excel файлу
    df = load_excel_file(file_path)                                     # Загружаем данные из файла
    if df is not None:
        display_data_in_table(df)                                       # Отображаем данные в таблице

if __name__ == "__main__":
    main()

#Библиотека pillow

img = Image.open('JPG.jpg')
img.show()                                          # Открыть изображение
img.crop((0, 0, 100, 200)).save('JPGcrop.jpg')      # Обрезать изображение
img = Image.open('JPGcrop.jpg')
img.show()
rotated = img.rotate(90)                            # Перевернуть изображение на 90 градусов
rotated.save('GPJ.jpg')
img = Image.open('GPJ.jpg')
img.show()
