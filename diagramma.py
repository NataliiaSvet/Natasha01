import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Установка шрифта, поддерживающего кириллицу (DejaVu Sans)
rcParams['font.family'] = 'DejaVu Sans'

# Загрузка данных
try:
    df = pd.read_excel('DA_Svietashova_diagramma.xlsx')
except FileNotFoundError:
    print("Файл не найден. Убедитесь, что файл с таким названием существует в рабочем каталоге.")
    raise

# Предположим, что у вас есть столбцы 'Вид помощи' и 'Сумма, крон'
categories = df['Вид помощи']
values = df['Сумма, крон']

# Построение круговой диаграммы с увеличенным шрифтом и автопроцентами
plt.figure(figsize=(10, 10))  # Размер графика
plt.pie(values, labels=categories, autopct='%1.1f%%', textprops={'fontsize': 14}, startangle=45)  # Вращение диаграммы для удобства чтения
plt.title('Затраты Чешской республики на помощь беженцам из Украины, 2022-2024 гг.', fontsize=18, pad=40)  # Увеличенный заголовок
plt.axis('equal')  # Для того чтобы круг не был эллипсом
plt.show()
