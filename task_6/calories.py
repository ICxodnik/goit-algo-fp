items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    # Розрахунок співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    total_calories = 0
    total_cost = 0
    selected_items = []

    for name, data in sorted_items:
        if total_cost + data['cost'] <= budget:
            selected_items.append(name)
            total_cost += data['cost']
            total_calories += data['calories']

    return selected_items, total_calories, total_cost

def dynamic_programming(items, budget):
    names = list(items.keys())
    n = len(names)

    # Створюємо кеш — словник для збереження вже порахованих результатів
    memo = {}

    # Рекурсивна функція
    def recursive_calc(i, remaining_budget):
        # Якщо не залишилось страв або бюджету — калорійність = 0
        if i >= n or remaining_budget <= 0:
            return 0

        # Якщо такий стан уже прорахований — повертаємо з кешу
        key = (i, remaining_budget)
        if key in memo:
            return memo[key]

        # Не беремо поточну страву
        without = recursive_calc(i + 1, remaining_budget)

        # Беремо поточну страву, якщо дозволяє бюджет
        cost = items[names[i]]["cost"]
        calories = items[names[i]]["calories"]

        with_item = 0
        if cost <= remaining_budget:
            with_item = calories + recursive_calc(i + 1, remaining_budget - cost)

        # Зберігаємо максимум у кеш і повертаємо
        memo[key] = max(without, with_item)
        return memo[key]

    # Запускаємо з першої страви і повним бюджетом
    total_calories = recursive_calc(0, budget)

    # Відновлюємо список вибраних страв
    selected_items = []
    i = 0
    remaining_budget = budget
    while i < n and remaining_budget > 0:
        current = recursive_calc(i, remaining_budget)
        skip = recursive_calc(i + 1, remaining_budget)
        if current != skip:
            selected_items.append(names[i])
            remaining_budget -= items[names[i]]["cost"]
        i += 1

    total_cost = sum(items[item]["cost"] for item in selected_items)
    return selected_items, total_calories, total_cost

# Приклад використання:
budget = 100

greedy_result = greedy_algorithm(items, budget)
dp_result = dynamic_programming(items, budget)

print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Сумарна калорійність:", greedy_result[1])
print("Сумарна вартість:", greedy_result[2])

print("\nДинамічне програмування:")
print("Вибрані страви:", dp_result[0])
print("Сумарна калорійність:", dp_result[1])
print("Сумарна вартість:", dp_result[2])
