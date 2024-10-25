import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize_Total_Products", pulp.LpMaximize)

# Визначення змінних
limonade = pulp.LpVariable('Limonade', lowBound=0, cat='Integer')  # Кількість лимонаду
juice = pulp.LpVariable('Juice', lowBound=0, cat='Integer')  # Кількість фруктового соку

# Цільова функція максимізації
model += limonade + juice, "Total_Products"

# Додавання обмежень на використання ресурсів
model += 2 * limonade + 1 * juice <= 100  # Обмеження на воду
model += 1 * limonade <= 50  # Обмеження на цукор
model += 1 * limonade <= 30  # Обмеження на лимонний сік
model += 2 * juice <= 40  # Обмеження на фруктове пюре

# Розв'язання моделі
model.solve()

# Вивід результатів
print(f"Виробляти одиниць лимонаду: {limonade.varValue}")
print(f"Виробляти одиниць фруктового соку: {juice.varValue}")
print(f"Статус розв'язання: {pulp.LpStatus[model.status]}")
