import streamlit as st
import pandas as pd

df = pd.read_excel('DA_Svietashova_karta.xlsx')  # Замените на ваш файл
st.dataframe(df)
