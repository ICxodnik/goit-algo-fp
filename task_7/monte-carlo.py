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


probabilities = {k: v / num_simulations for k, v in results.items()}


print("Сума | Ймовірність")
print("-------------------")
for sum_, prob in probabilities.items():
    print(f"{sum_:>4} | {prob:.5f}")

