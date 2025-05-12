import random
import matplotlib.pyplot as plt

def die_emulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}

    # Симуляція кидків двох кубиків
    for _ in range(num_simulations):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2
        results[total] += 1

    probabilities = {k: (v / num_simulations) * 100 for k, v in results.items()}

    print("Сума | Ймовірність")
    print("-------------------")
    for sum_, prob in probabilities.items():
        print(f"{sum_:>4} | {prob: .2f}")

    return probabilities

def build_picture(num_simulations, probabilities):
    # Побудова графіка
    plt.figure(figsize=(10, 6))
    plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', edgecolor='black')
    plt.xlabel("Сума на кубиках")
    plt.ylabel("Ймовірність %")
    plt.title(f"Ймовірності сум при {num_simulations:,} кидках двох кубиків")
    plt.xticks(range(2, 13))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def build_error_graph(simulation_counts, mae_values):
    plt.figure(figsize=(8, 5))
    plt.plot(simulation_counts, mae_values, marker='o', linestyle='-', color='green')
    plt.xlabel("Кількість симуляцій")
    plt.ylabel("Середня абсолютна похибка %")
    plt.title("Залежність точності від кількості симуляцій")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xscale('log')
    plt.tight_layout()
    plt.show()

# Теоретичні ймовірності для кожної суми
analytical_probs = {
    2: 1/36 * 100,
    3: 2/36 * 100,
    4: 3/36 * 100,
    5: 4/36 * 100,
    6: 5/36 * 100,
    7: 6/36 * 100,
    8: 5/36 * 100,
    9: 4/36 * 100,
    10: 3/36 * 100,
    11: 2/36 * 100,
    12: 1/36 * 100
}

# Функція для обчислення середньої абсолютної похибки
def calculate_mae(simulated_probs):
    error = 0
    for k in analytical_probs:
        error += abs(simulated_probs[k] - analytical_probs[k])
    return (error / len(analytical_probs))

if __name__ == "__main__":
    mae_values = []
    simulation_counts = [1_000, 100_000, 1_000_000]

    for num_simulations in simulation_counts:
        probabilities = die_emulation(num_simulations)
        build_picture(num_simulations, probabilities)
        mae = calculate_mae(probabilities)
        mae_values.append(mae)
        print(f"Похибка для {num_simulations:,} кидків: {mae*100:.2f}")

    build_error_graph(simulation_counts, mae_values)
