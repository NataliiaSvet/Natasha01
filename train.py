import matplotlib.pyplot as plt

# Загружаем данные (предположим, что данные уже в DataFrame data_sorted)
# Названия отраслей и доля трудоустроенных
labels = data_sorted['Направления']
sizes = data_sorted['Доля трудоустроенных']

# Устанавливаем цветовую палитру для вложенных кругов
colors = plt.cm.Paired(range(len(sizes)))  # Используем Paired для сочетающихся цветов

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))

# Внутренний круг - доля трудоустроенных
ax.pie(sizes, labels=labels, startangle=90, colors=colors, radius=1, wedgeprops=dict(width=0.3, edgecolor='w'))

# Внешний круг - указывает доли трудоустройства в процентах
inner_sizes = sizes / sizes.sum()  # Доли для внешнего круга
ax.pie(inner_sizes, labels=[f'{int(size)}%' for size in sizes], labeldistance=0.7,
       startangle=90, colors=colors, radius=0.7, wedgeprops=dict(width=0.3, edgecolor='w'))

# Добавляем заголовок
plt.title("Доля трудоустроенных украинских мигрантов по отраслям экономики ЧР")

# Отображение круговой диаграммы в Streamlit
st.pyplot(fig)








