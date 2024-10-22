import pandas as pd
import folium
from folium.plugins import MarkerCluster
import matplotlib.pyplot as plt
import streamlit as st

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
st.markdown("<h1 style='text-align: center;'>Карта количества беженцев в Чехии по регионам</h1>", unsafe_allow_html=True)

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
st.markdown("<h2 style='text-align: center;'>Распределение беженцев по регионам</h2>", unsafe_allow_html=True)

# Создаем ленточную диаграмму
fig, ax = plt.subplots(figsize=(15, 10))  # Увеличение размеров фигуры
bars = ax.barh(df_procent['Регион'], df_procent['Количество беженцев, %'], color='skyblue')
ax.set_xlabel('Количество беженцев, %')
ax.set_ylabel('Регион')
ax.set_title('Количество беженцев в процентах по регионам')

# Увеличение полей вокруг диаграммы
plt.subplots_adjust(left=0.2, right=1.5, top=0.9, bottom=0.2)  # Увеличение полей

# Добавление значений на каждый столбик
for bar in bars:
    width = bar.get_width()
    ax.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{width:.1f}%', va='center', ha='left')

# Отображаем диаграмму в Streamlit
st.pyplot(fig)








