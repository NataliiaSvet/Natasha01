import pandas as pd
import folium
from folium.plugins import MarkerCluster
import streamlit as st

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

import streamlit as st

# Используем HTML для заголовка
st.markdown('<h1 style='text-align: center;">Карта количества беженцев в Чехии</h1>', unsafe_allow_html=True)

# Остальной код для отображения карты


# Установите ширину и высоту карты
map_height = 600  # Установите желаемую высоту карты
map_width = 800   # Установите желаемую ширину карты

# Сохраните карту в HTML
map_html = m._repr_html_()

# Вставьте HTML-код карты
st.components.v1.html(map_html, height=map_height, width=map_width)






