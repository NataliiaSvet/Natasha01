import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st

# Выбор шрифта, поддерживающего кириллицу (например, Arial)
rcParams['font.family'] = 'Arial'

# Заголовок приложения
st.title('Анализ затрат Чешской республики на помощь беженцам из Украины')

# Загрузка данных
df = pd.read_excel('DA_Svietashova_diagramma.xlsx')

# Предположим, что у вас есть столбцы 'Вид помощи' и 'Сумма, крон'
categories = df['Вид помощи']
values = df['Сумма, крон']

# Установка фона через markdown с использованием CSS
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #e6ffe6; /* Светло-зеленый фон */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Построение круговой диаграммы с увеличенным шрифтом и автопроцентами
plt.figure(figsize=(10, 10))  # Размер графика
plt.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=45)  # Вращение диаграммы для удобства чтения
plt.title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.', fontsize=18, pad=40)  # Увеличенный заголовок
plt.axis('equal')  # Для того чтобы круг не был эллипсом

# Отображение графика в Streamlit
st.pyplot(plt)

