import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st

# Выбор шрифта, поддерживающего кириллицу (например, Arial)
rcParams['font.family'] = 'Arial'

# Конфигурация страницы
st.set_page_config(page_title="Анализ затрат", layout="wide")

# Вывод заголовка по центру
st.markdown("<h1 style='text-align: center; color: black;'>Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.</h1>", unsafe_allow_html=True)

# Загрузка данных
df = pd.read_excel('DA_Svietashova_diagramma.xlsx')

# Вычисление суммы по числовым столбцам
total_sum = df['Сумма, тыс.крон'].sum()

# Добавление строки "Итого"
total_row = pd.DataFrame({'Вид помощи': ['Итого'], 'Сумма, тыс.крон': [total_sum]})
df = pd.concat([df, total_row], ignore_index=True)

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
col1, col2 = st.columns([1, 2])

# В первой колонке отображаем таблицу
with col1:
    df = df[['Вид помощи', 'Сумма, тыс.крон']]
    styled_df = df.style.set_table_attributes('style="border-collapse: collapse; width: 100%;"') \
        .set_properties(**{'border': '2px solid black', 'text-align': 'center'}) \
        .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold'), ('border', '2px solid black'), ('text-align', 'center'), ('font-size', '14px')]}])
    st.table(styled_df)

# Во второй колонке отображаем объемную круговую диаграмму
with col2:
    categories = df['Вид помощи'][:-1]

    # Преобразование значений столбца 'Сумма, тыс.крон' в строки, затем удаление пробелов и преобразование обратно в числа
    values = df['Сумма, тыс.крон'][:-1].astype(str).str.replace(' ', '').astype(float)

    # Создание взрывной диаграммы с объемом
    explode = [0.05] * len(categories)  # Уменьшаем "вытягивание" сегментов

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=25, explode=explode, shadow=True, textprops={'fontsize': 14})

    # Поскольку круговая диаграмма сама по себе не может быть повернута, можно просто оставить ax.axis('equal').
    ax.axis('equal')  # Чтобы круг не был эллипсом

    # Отображение диаграммы
    st.pyplot(fig)

# Добавление текста под таблицей
st.markdown("""<div style='text-align: left; font-weight: bold; font-size: 16px;'>
После начала полномасштабной войны в феврале 2022 г. Чешская республика оказала Украине помощь в размере более 54,5 млрд крон, 
в том числе в виде гуманитарной помощи, отправленной в Украину, а также помощи украинским беженцам на территории Чехии. 
1,3 млрд крон было компенсировано из Европейского союза.</div>""", unsafe_allow_html=True)

# Примечание
st.markdown("**Примечание:** Данные основаны на официальных отчетах за последние три года.")




   
