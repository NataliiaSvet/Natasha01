import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st

# Конфигурация страницы (должна быть первой командой)
st.set_page_config(page_title="Анализ затрат и беженцев", layout="wide")

# Выбор шрифта, поддерживающего кириллицу (например, Arial)
rcParams['font.family'] = 'Arial'

# Заголовок страницы
st.markdown("<h1 style='text-align: center; color: black;'>Расходы Чешской республики на помощь беженцам из Украины, 2022-2024 гг.</h1>", unsafe_allow_html=True)

# Загрузка данных для диаграммы расходов
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

# Создание колонок для первой диаграммы
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
    ax.pie(values, labels=categories, autopct='%1.1f%%', startangle=28, explode=explode, shadow=True, textprops={'fontsize': 14})

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

# ______________________________________________________________________________________________________

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Заголовок для второй диаграммы
st.markdown("<h1 style='text-align: center; color: black;'>Количество беженцев в Чешской республике с февраля 2022 г.</h1>", unsafe_allow_html=True)

# Загрузка данных для столбчатой диаграммы
df_refugees = pd.read_excel('DA_Svietashova_gist.xlsx')

# Предполагается, что у вас есть столбцы 'Период времени' и 'Количество, чел.'
categories = df_refugees['Период времени']
values = df_refugees['Количество, чел.']

# Построение столбчатой диаграммы
plt.figure(figsize=(8, 4))  # Установка размера графика
plt.bar(categories, values, color='blue', width=15)  # Построение графика, правильные аргументы

# Добавление заголовка и меток осей
# plt.title('Количество беженцев', fontsize=16)
plt.xlabel('Период времени', fontsize=10)
plt.ylabel('Количество, чел.', fontsize=10)

# Уменьшение размера подписей по осям
plt.xticks(fontsize=10)  # Уменьшение размера шрифта для меток оси X
plt.yticks(fontsize=10)  # Уменьшение размера шрифта для меток оси Y

# Отображение графика
plt.xticks(rotation=90)  # Поворот меток оси x для удобства
# plt.tight_layout()  # Автоматическая подгонка элементов на графике

# Отображение графика в Streamlit
st.pyplot(plt)







   
