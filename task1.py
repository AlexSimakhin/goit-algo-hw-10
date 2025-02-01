"""task1.py"""
import pulp

# Створення проблеми лінійного програмування
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Змінні для кількості вироблених напоїв
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat="Continuous")
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat="Continuous")

# Обмеження на ресурси
model += 2 * lemonade + fruit_juice <= 100, "Water"
model += lemonade <= 50, "Sugar"
model += lemonade <= 30, "Lemon_Juice"
model += 2 * fruit_juice <= 40, "Fruit_Puree"

# Функція цілі - максимізація кількості вироблених напоїв
model += lemonade + fruit_juice, "Total_Products"

# Розв'язання проблеми
model.solve()

# Виведення результатів
print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {pulp.value(lemonade)}")
print(f"Fruit Juice: {pulp.value(fruit_juice)}")
print(f"Total Products: {pulp.value(model.objective)}")
