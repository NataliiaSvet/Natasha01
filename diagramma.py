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

# Вывод загруженного DataFrame для диагностики
# st.write("### Загруженные данные:", df)

# Удаление первой колонки (нумерации)
# df = df.iloc[:, 1:]

# Вывод DataFrame после удаления первой колонки
# st.write("### Данные после удаления первой колонки:", df)

# Убедимся, что в DataFrame нет NaN
# df.dropna(inplace=True)

# Вычисление суммы по числовым столбцам
total_sum = df['Сумма, тыс.крон'].sum()  # Предполагается, что у вас есть столбец 'Сумма, тыс.крон'

# Добавление строки "Итого"
total_row = pd.DataFrame({'Вид помощи': ['Итого'], 'Сумма, тыс.крон': [total_sum]})
df = pd.concat([df, total_row], ignore_index=True)  # Добавляем строку в DataFrame

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

# Форматирование числового столбца с разделителями тысяч
df['Сумма, тыс.крон'] = df['Сумма, тыс.крон'].apply(lambda x: '{:,.0f}'.format(x).replace(',', ' '))

# Создание колонок
col1, col2 = st.columns([1, 2])

# В первой колонке отображаем таблицу
with col1:
    # st.write("### Таблица данных")
    # Форматируем таблицу, поменяв местами колонки
    df = df[['Вид помощи', 'Сумма, тыс.крон']]  # Изменяем порядок столбцов
    # Стиль таблицы с одинаковыми жирными границами
    styled_df = df.style.set_table_attributes('style="border-collapse: collapse; width: 100%;"') \
        .set_properties(**{'border': '2px solid black', 'text-align': 'center'}) \
        .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold'), ('border', '2px solid black'), ('text-align', 'center'), ('font-size', '14px')]}])
    st.table(styled_df)

# Во второй колонке отображаем диаграмму
with col2:
    # Предполагаем, что у вас есть столбцы 'Вид помощи' и 'Сумма, тыс.крон'
    categories = df['Вид помощи'][:-1]  # Исключаем строку "Итого"
    values = df['Сумма, тыс.крон'][:-1].str.replace(' ', '').astype(float)  # Преобразуем для построения диаграммы

    # Построение круговой диаграммы
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=30)
    # ax.set_title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.', fontsize=18, pad=40)
    ax.axis('equal')  # Чтобы круг не был эллипсом

    # Отображение диаграммы
    st.pyplot(fig)

# Добавление отступа в конце
st.markdown('<br>', unsafe_allow_html=True)

# Добавление текста под таблицей
st.write("После начала полномасштабной войны в феврале 2022 г. Ческая республика оказала Украине помощь в размере более 54,5 млрд.крон. 
В том числе это была гуманитарная помощь, отправленная в Украину, а также помощь украинским беженцам на территории Чехии. 1,3 млрд.крон 
было компенсировано из Европейского союза.")

# Вы также можете использовать markdown для стилизованного текста
st.markdown("**Примечание:** Данные основаны на официальных отчетах за последние три года.")


      


   
