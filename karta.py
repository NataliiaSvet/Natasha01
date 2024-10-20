import pandas as pd
import folium
from folium.plugins import MarkerCluster
import streamlit as st

# Заголовок, выровненный по центру
st.markdown("<h1 style='text-align: center; color: black;'>Карта количества беженцев в Чехии</h1>", unsafe_allow_html=True)

# Загрузите ваши данные
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

# Установите ширину и высоту карты
map_height = 800  # Установите желаемую высоту карты
map_width = 1000   # Установите желаемую ширину карты

# Сохраните карту в HTML
map_html = m._repr_html_()

# Оберните заголовок и карту в контейнер с отступами
st.markdown(
    f'<div style="margin-left: 50px;">'  # Отступ в 50 пикселей слева
    f'{map_html}'  # Вставьте HTML-код карты
    '</div>',
    unsafe_allow_html=True
)





