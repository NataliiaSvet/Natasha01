import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Конфигурация страницы
st.set_page_config(page_title="Анализ затрат", layout="wide")

# Выбор шрифта, поддерживающего кириллицу (например, Arial)
rcParams['font.family'] = 'Arial'

# Загрузка данных
df = pd.read_excel('DA_Svietashova_diagramma.xlsx')

# Удаление первой колонки (нумерации)
df = df.iloc[:, 1:]

# Проверка загруженных данных
st.write("Загруженные данные:")
st.dataframe(df)  # Отобразим таблицу с данными для отладки

# Вычисление суммы по числовым столбцам
total_sum = df['Сумма, крон'].sum()  # Предполагается, что у вас есть столбец 'Сумма, крон'
st.write(f"Сумма значений: {total_sum}")  # Отладочное сообщение

# Добавление строки "Итого"
total_row = pd.DataFrame({'Вид помощи': ['Итого'], 'Сумма, крон': [total_sum]})
df = pd.concat([df, total_row], ignore_index=True)  # Добавляем строку в DataFrame

# Создание колонок
col1, col2 = st.columns([1, 2])

# В первой колонке отображаем таблицу
with col1:
    st.write("### Таблица данных")
    # Форматируем таблицу
    styled_df = df.style.set_table_attributes('style="border-collapse: collapse; border: 1px solid black; width: 100%;"') \
        .set_properties(**{'border': '1px solid black', 'font-weight': 'bold', 'text-align': 'center'}) \
        .set_caption("Итого по всем видам помощи") \
        .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold'), ('text-align', 'center'), ('font-size', '14px')]}])

    st.table(styled_df)

# Во второй колонке отображаем диаграмму
with col2:
    # Предположим, что у вас есть столбцы 'Вид помощи' и 'Сумма, крон'
    categories = df['Вид помощи'][:-1]  # Исключаем строку "Итого"
    values = df['Сумма, крон'][:-1]  # Исключаем строку "Итого"

    # Построение круговой диаграммы
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=45)
    plt.title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.', fontsize=18, pad=20)
    plt.axis('equal')

    st.pyplot(plt)

# Добавление отступа в конце
st.markdown('<br>', unsafe_allow_html=True)


   
