import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import streamlit as st

# Конфигурация страницы
st.set_page_config(page_title="Карта беженцев по регионам Чехии", layout="wide")

# Заголовок
st.markdown("<h1 style='text-align: center;'>Карта количества беженцев по регионам Чехии</h1>", unsafe_allow_html=True)
import os
print(os.getcwd())

df = pd.read_excel('DA_Svietashova_karta.xlsx.')


# Загрузка данных о беженцах (предположим, что у вас в файле есть столбцы "Регион" и "Количество беженцев")
df = pd.read_excel('karta.xlsx')

# Загрузка геоданных Чехии (shapefile с границами регионов)
map_df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))  # Это для примера, замените на реальные данные Чехии

# Пример соединения данных по столбцу региона (замените на актуальные поля)
merged = map_df.set_index('name').join(df.set_index('Регион'))

# Построение карты
fig, ax = plt.subplots(1, 1, figsize=(10, 10))
merged.plot(column='Количество беженцев', cmap='OrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Добавление карты в Streamlit
st.pyplot(fig)



  
