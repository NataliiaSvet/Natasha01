import pandas as pd

# Замените 'your_file.xlsx' на имя вашего файла
df = pd.read_excel('DA_Svietashova_karta.xlsx') 
# Для .xlsx
# df = pd.read_csv('your_file.csv')    # Для .csv

# Отображение первых 5 строк таблицы
print(df.head())

# Проверка названий колонок
print(df.columns)

