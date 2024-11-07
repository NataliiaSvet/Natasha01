import pandas as pd
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
from matplotlib import rcParams
import streamlit as st
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# Выбор шрифта, поддерживающего кириллицу (например, Arial)
rcParams['font.family'] = 'Arial'

# Конфигурация страницы
st.set_page_config(page_title="Анализ затрат", layout="wide")

# Вывод заголовка по центру
st.markdown("<h1 style='text-align: center; color: black;'>Расходы Чешской республики, связанные с военным конфликтом в Украине, 2022-2024 гг.</h1>", unsafe_allow_html=True)

# Загрузка данных
df = pd.read_excel('DA_Svietashova_diagramma.xlsx')

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
    df = df[['Вид помощи', 'Сумма, тыс.крон']]  # Изменяем порядок столбцов
    styled_df = df.style.set_table_attributes('style="border-collapse: collapse; width: 100%;"') \
        .set_properties(**{'border': '2px solid black', 'text-align': 'center'}) \
        .set_table_styles([{'selector': 'th', 'props': [('font-weight', 'bold'), ('border', '2px solid black'), ('text-align', 'center'), ('font-size', '14px')]}])
    st.table(styled_df)

# Во второй колонке отображаем диаграмму
with col2:
    categories = df['Вид помощи'][:-1]  # Исключаем строку "Итого"
    values = df['Сумма, тыс.крон'][:-1].str.replace(' ', '').astype(float)  # Преобразуем для построения диаграммы

    # Построение круговой диаграммы
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=30)
    ax.axis('equal')  # Чтобы круг не был эллипсом

    # Отображение диаграммы
    st.pyplot(fig)
    plt.close(fig)  # Закрываем фигуру

# Добавление текста под таблицей
st.markdown("""<div style='text-align: left; font-weight: bold; font-size: 18px;'>
После начала полномасштабной войны в феврале 2022 г. Чешская республика оказала Украине помощь в размере более 54,5 млрд крон, 
в том числе в виде гуманитарной помощи, отправленной в Украину, а также помощи украинским беженцам на территории Чехии. 
1,3 млрд крон было компенсировано из Европейского союза.</div>""", unsafe_allow_html=True)

# Примечание
st.markdown("**Примечание:** Данные основаны на официальных отчетах за последние три года.")

# Отступ между графиками
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Заголовок для второй диаграммы
st.markdown("<h1 style='text-align: center; color: black;'>Количество лиц в Чешской республике, получивших временную защиту с февраля 2022 г.</h1>", unsafe_allow_html=True)

# Загрузка данных для столбчатой диаграммы
df_refugees = pd.read_excel('DA_Svietashova_gist.xlsx')

# Форматирование столбца 'Период времени' в формат YYYY-MM
df_refugees['Период времени'] = pd.to_datetime(df_refugees['Период времени']).dt.strftime('%Y-%m')

categories = df_refugees['Период времени']
values = df_refugees['Количество, чел.']

# Построение столбчатой диаграммы
plt.figure(figsize=(8, 4))  # Установка размера графика
plt.bar(categories, values, color='RoyalBlue', width=0.5)  # Построение графика

# Добавление меток осей
plt.xlabel('Период времени', fontsize=10)
plt.ylabel('Количество, чел.', fontsize=10)

# Уменьшение размера подписей по осям
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

# Отображение графика
plt.xticks(rotation=90)  # Поворот меток оси X для удобства
st.pyplot(plt)
plt.close()  # Закрываем фигуру

# Добавление текста под диаграммой
st.markdown("""<div style='text-align: left; font-weight: bold; font-size: 18px;'>
Чехия с февраля 2022 г. предоставила временную защиту более 600 тыс. беженцев из Украины. По текущим данным Министерства внутренних дел Ческой республики, в данный момент в стране находится более 380 тыс. беженцев из Украины с временной защитой всех возрастных категорий, включая детей и стариков.</div>""", unsafe_allow_html=True)

# Отступ между графиками
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Загрузка первого файла с координатами регионов и количеством беженцев
df = pd.read_excel('DA_Svietashova_karta.xlsx')  # Замените на ваш файл

# Создание карты
m = folium.Map(location=[49.8175, 15.473], zoom_start=7)  # Центр Чехии

# Создание кластеров маркеров
marker_cluster = MarkerCluster().add_to(m)

# Добавление маркеров для каждого региона
for index, row in df.iterrows():
    folium.Marker(
        location=[row['Широта'], row['Долгота']],  # Убедитесь, что эти колонки есть в вашем DataFrame
        popup=f"{row['Регион']}: {row['Количество беженцев']}",
        icon=folium.Icon(color='blue')
    ).add_to(marker_cluster)

# Отображение карты в Streamlit
st.markdown("<h1 style='text-align: center;'>Карта количества лиц с временной защитой в Чехии по регионам</h1>", unsafe_allow_html=True)

# Установите размеры карты
map_height = 600  # Установите желаемую высоту карты
map_width = 800   # Установите желаемую ширину карты

# Сохраните карту в HTML
map_html = m._repr_html_()

# Вставьте HTML-код карты
st.components.v1.html(map_html, height=map_height, width=map_width)

# Загрузка второго файла с процентами
df_procent = pd.read_excel('DA_Svietashova_karta_procent.xlsx')  # Замените на ваш файл

# Построение ленточной диаграммы
st.markdown("<h2 style='text-align: center;'>Распределение лиц с временной защитой по регионам</h2>", unsafe_allow_html=True)

# Создаем ленточную диаграмму
fig, ax = plt.subplots(figsize=(8, 4))  # Увеличение размеров фигуры
bars = ax.barh(df_procent['Регион'], df_procent['Количество беженцев, %'], color='Coral')
ax.set_xlabel('Количество беженцев, %')
ax.set_ylabel('Регион')
# ax.set_title('Количество лиц с ВЗ в процентах по регионам')

# Увеличение полей вокруг диаграммы
plt.subplots_adjust(left=0.2, right=1.3, top=0.9, bottom=0.2)  # Увеличение полей

# Добавление значений на каждый столбик
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{width:.0f}%', va='center', ha='left')

# Отображаем диаграмму в Streamlit
st.pyplot(fig)

# Отступ между графиками
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Установка шрифта для кириллицы
plt.rcParams['font.family'] = 'Arial'

# Заголовок Streamlit-приложения
# st.title("Отрасли экономики Чешской республики, в которых работают мигранты из Украины с временной защитой")

st.markdown(
    "<h2 style='text-align: center; color: black;'>"
    "Отрасли экономики Чешской республики,<br>в которых работают мигранты из Украины "
    "с временной защитой</h2>", 
    unsafe_allow_html=True
)

# Загрузка данных из файла Excel
file_path = 'DA_Svietashova_diagramma2.xlsx'
df = pd.read_excel(file_path)

# Назначение колонок
directions = df['Направления экономики ЧР']
employment_rates = df['Доля трудоустроенных особ с ВЗ из Украины']

# Создание DataFrame и сортировка по значениям трудоустройства
data = pd.DataFrame({'Направления': directions, 'Доля трудоустроенных': employment_rates})
data_sorted = data.sort_values(by='Доля трудоустроенных')

# Настройка данных
labels = data_sorted['Направления']
sizes = data_sorted['Доля трудоустроенных']
colors = plt.cm.tab20(range(len(sizes)))

# Создаем фигуру с высоким dpi для четкости
fig, ax = plt.subplots(figsize=(6, 4), dpi=200, subplot_kw=dict(aspect="equal"))

# Внутренний круг с уменьшенным шрифтом для отраслей
ax.pie(sizes, labels=labels, startangle=90, colors=colors, radius=0.9,
       wedgeprops=dict(width=0.2, edgecolor='w'), labeldistance=1.15,
       textprops={'fontsize': 6, 'weight': 'bold'})  # Оптимизированный шрифт для текста

# Внешний круг с процентами и регулировкой `bbox` для улучшенного выравнивания
inner_sizes = sizes / sizes.sum()
ax.pie(inner_sizes, labels=[f'{int(size)}%' for size in sizes], labeldistance=0.55,
       startangle=90, colors=colors, radius=0.6, wedgeprops=dict(width=0.2, edgecolor='w'),
       textprops={'fontsize': 5, 'weight': 'bold', 'bbox': dict(facecolor='white', edgecolor='none', pad=0.5)}) 

# Увеличение плотности с помощью высокого dpi
st.pyplot(fig)

# Отображение в Streamlit
st.pyplot(fig)

# Добавление текста под таблицей
st.markdown("""<div style='text-align: left; font-weight: bold; font-size: 18px;'>Украинские мигранты трудоустроены во всех наиболее важных отраслях экономики ЧР, которые долгое время требовали дополнительную рабочую силу. </div>""", unsafe_allow_html=True)

# Отступ между графиками
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

   
