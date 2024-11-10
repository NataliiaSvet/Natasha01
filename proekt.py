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
st.markdown("<h2 style='text-align: center; color: black;'>Расходы Чешской республики, связанные с военным конфликтом в Украине, 2022-2024 гг.</h1>", unsafe_allow_html=True)

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
st.markdown("<h2 style='text-align: center; color: black;'>Количество лиц в Чешской республике, получивших временную защиту с февраля 2022 г.</h1>", unsafe_allow_html=True)

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
st.markdown("<h2 style='text-align: center;'>Карта количества лиц с временной защитой в Чехии по регионам</h1>", unsafe_allow_html=True)

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

# Настройка данных для круговой диаграммы
labels = data_sorted['Направления']
sizes = data_sorted['Доля трудоустроенных']
colors = plt.cm.tab20(range(len(sizes)))

# Создаем более компактную фигуру с высоким разрешением для четкости
fig, ax = plt.subplots(figsize=(5, 3), dpi=200, subplot_kw=dict(aspect="equal"))

# Внутренний круг с уменьшенным шрифтом для отраслей
ax.pie(sizes, labels=labels, startangle=90, colors=colors, radius=0.9,
       wedgeprops=dict(width=0.2, edgecolor='w'), labeldistance=1.1,
       textprops={'fontsize': 6, 'weight': 'bold'})

# Внешний круг - с процентами, также уменьшенный шрифт
inner_sizes = sizes / sizes.sum()
ax.pie(inner_sizes, labels=[f'{int(size)}%' for size in sizes], labeldistance=0.6,
       startangle=90, colors=colors, radius=0.6, wedgeprops=dict(width=0.2, edgecolor='w'),
       textprops={'fontsize': 5, 'weight': 'bold'})

# Отображение диаграммы в Streamlit
st.pyplot(fig)

# Добавление текста под таблицей
st.markdown("""<div style='text-align: left; font-weight: bold; font-size: 18px;'>В настоящее время более 60% мигрантов из Ураины с временной защитой трудоустроены. Мигранты работают во всех наиболее важных отраслях экономики ЧР, которые долгое время требовали дополнительную рабочую силу. В группу "Административная и подсобная деятельность" входят фирмы, которые предоставляют трудовые ресурсы третьим лицам, в основном в таких направлениях как логистика, строительство, производство, сельское хозяйство. </div>""", unsafe_allow_html=True)

# Отступ между графиками
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Соотношение работающих в ЧР мигрантов из Украины с временной защитой и получающих гуманитарную помощь, 2023-2024 гг.</h2>", unsafe_allow_html=True)

# Загрузка данных из Excel файла
file_path = 'DA_Svietashova_gist2.xlsx'
df = pd.read_excel(file_path)

# Замените "Column1", "Column2" и "Column3" на реальные названия столбцов из вашего файла
x_column = df.columns[0]  # Столбец для оси X
y_column1 = df.columns[1]  # Первый столбец для линии 1
y_column2 = df.columns[2]  # Второй столбец для линии 2

# Построение графика с двумя линиями и уменьшенным размером
fig, ax = plt.subplots(figsize=(7, 3))  # Уменьшение размера фигуры

# Линия 1
ax.plot(df[x_column], df[y_column1], marker='o', color='b', label=y_column1)

# Линия 2
ax.plot(df[x_column], df[y_column2], marker='x', color='g', label=y_column2)

# Настройки графика
ax.set_xlabel(x_column)
ax.legend()
ax.grid(True)

# Поворот подписей оси X на 90 градусов и уменьшение размера шрифта
plt.xticks(rotation=90, fontsize=8)  # Уменьшение шрифта подписей на оси X
plt.yticks(fontsize=8)  # Уменьшение шрифта подписей на оси Y

# Отображение графика в Streamlit
st.pyplot(fig)

# Добавление текста под диаграммой
st.markdown("""<div style='text-align: left; font-weight: bold; font-size: 18px;'>
По сравнению с прошлым годом в 2024 году количество человек, получающих материальную помощь в Чехии резко сократилось. В то время как количество работающих и оплачичивающих налоги в бюджет ЧР постоянно растет.</div>""", unsafe_allow_html=True)

# Отступ между графиками
st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

# Вывод заголовка по центру
st.markdown("<h2 style='text-align: center; color: black;'>Соотношение расходов на помощь мигрантам из Украины и доходов от них в бюджет</h1>", unsafe_allow_html=True)


# Загрузка данных из Excel файла
file_path = 'DA_Svietashova_column.xlsx'
df = pd.read_excel(file_path)

# Установка ширины столбцов
bar_width = 0.35
index = np.arange(len(df))

# Построение графика
fig, ax = plt.subplots(figsize=(10, 6))
bar1 = ax.bar(index - bar_width / 2, df['Расходы на помощь украинским беженцам, млрд крон'], 
              bar_width, label='Расходы', color='salmon')
bar2 = ax.bar(index + bar_width / 2, df['Доходы от миграции украинцев (поступление в бюджет),млрд крон'], 
              bar_width, label='Доходы', color='skyblue')

# Добавление подписей и форматирование
ax.set_xlabel('Период времени')
ax.set_ylabel('Млрд крон')
# ax.set_title('Соотношение расходов на помощь украинским беженцам и доходов от беженцев в бюджет')
ax.set_xticks(index)
ax.set_xticklabels(df['Период времени'], rotation=45, ha='right')
ax.legend()

# Добавление значений над столбцами
for bar in bar1:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.3, round(yval, 1), ha='center', va='bottom', fontsize=9)

for bar in bar2:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 0.3, round(yval, 1), ha='center', va='bottom', fontsize=9)

# Оптимизация макета
plt.tight_layout()
plt.show()

# Отображение графика в Streamlit
st.pyplot(fig)
