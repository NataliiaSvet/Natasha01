import pandas as pd
import streamlit as st

# Добавляем возможность загрузки файла
uploaded_file = st.file_uploader("Загрузите файл с данными о беженцах", type=["xlsx"])

# Проверяем, загружен ли файл
if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)  # Чтение файла
    st.write(df)  # Отображение данных файла

  
