import numpy as np
import matplotlib.pyplot as plt

data = np.random.randn(1000) # Generate 1000 random numbers from a normal distribution

plt.hist(data, bins=30, color='green', edgecolor='black') # Create a histogram with 30 bins
plt.xlabel('Значення')
plt.ylabel('Частота')
plt.title('Гістограма випадкових чисел (нормальний розподіл)') # Task 3
plt.grid(True)

plt.savefig('task3_histogram_random.png', dpi=300) # Save the histogram as a PNG file
plt.show()
