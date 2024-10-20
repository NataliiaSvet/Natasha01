import pandas as pd
import folium
from folium.plugins import MarkerCluster
import streamlit as st
from streamlit_folium import folium_static

# Загрузите ваши данные
df = pd.read_excel('DA_Svietashova_karta.xlsx')  # Замените на ваш файл

# Создание карты
m = folium.Map(location=[49.8175, 15.473], zoom_start=8)  # Центр Чехии

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
st.title('Карта количества беженцев в Чехии')
folium_static(m)

