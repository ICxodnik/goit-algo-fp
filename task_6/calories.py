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

# Приклад використання:
budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Вибрані страви:", greedy_result[0])
print("Сумарна калорійність:", greedy_result[1])
print("Сумарна вартість:", greedy_result[2])
