
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

# Предположим, что у вас есть столбцы 'Вид помощи' и 'Сумма, крон'
categories = df['Вид помощи']
values = df['Сумма, крон']

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

# Создание колонок
col1, col2 = st.columns([1, 2])  # Устанавливаем пропорции колонок

# В первой колонке отображаем таблицу
with col1:
    # st.write("### Таблица данных")
    st.table(df)

# Во второй колонке отображаем диаграмму
with col2:

    # Построение круговой диаграммы с увеличенным шрифтом и автопроцентами
    plt.figure(figsize=(10, 10))  # Размер графика
    plt.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=45)  # Вращение диаграммы для удобства чтения
    # plt.title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.', fontsize=18, pad=40)  # Увеличенный заголовок
    plt.axis('equal')  # Для того чтобы круг не был эллипсом

    # Отображение графика в Streamlit
    st.pyplot(plt)

    # Добавление текста под таблицей
    st.write("Эта таблица отображает распределение затрат Чешской республики на помощь беженцам из Украины за 2022-2024 гг.")

    # Вы также можете использовать markdown для стилизованного текста
    st.markdown("**Примечание:** Данные основаны на официальных отчетах за последние три года.")
