import random
import matplotlib.pyplot as plt

num_simulations = 100_000
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

# Побудова графіка
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), color='skyblue', edgecolor='black')
plt.xlabel("Сума на кубиках")
plt.ylabel("Ймовірність %")
plt.title(f"Ймовірності сум при {num_simulations:,} кидках двох кубиків")
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
