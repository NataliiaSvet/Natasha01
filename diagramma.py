import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st

# Выбор шрифта, поддерживающего кириллицу (например, Arial)
rcParams['font.family'] = 'Arial'

# Конфигурация страницы
st.set_page_config(page_title="Анализ затрат", layout="wide")  # Используйте layout="wide" для широкой страницы

# Заголовок приложения
# st.title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.')

# Вывод заголовка по центру
st.markdown("<h1 style='text-align: center; color: black;'>Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.</h1>", unsafe_allow_html=True)

# Загрузка данных
df = pd.read_excel('DA_Svietashova_diagramma.xlsx')

# Удаление первой колонки (нумерации)
df = df.iloc[:, 1:]

# Вычисление суммы по числовым столбцам
total_sum = df['Сумма, крон'].sum()  # Предполагается, что у вас есть столбец 'Сумма, крон'

# Добавление строки "Итого"
total_row = pd.DataFrame({'Вид помощи': ['Итого'], 'Сумма, крон': [total_sum]})
df = pd.concat([df, total_row], ignore_index=True)  # Добавляем строку в DataFrame

# Предположим, что у вас есть столбцы 'Вид помощи' и 'Сумма, крон'
# categories = df['Вид помощи']
# values = df['Сумма, крон']

# Установка фона через markdown с использованием CSS
st.markdown(
"""
    <style>
    .stApp {
        background-color: #90EE90; /* Средне-зеленый фон */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Построение круговой диаграммы
fig, ax = plt.subplots(figsize=(10, 10))
ax.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=45)
ax.set_title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.', fontsize=18, pad=40)
ax.axis('equal')  # Чтобы круг не был эллипсом

# Отображение диаграммы
st.pyplot(fig)

      


   
