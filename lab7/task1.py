import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 500) # Creating an array of 500 points from -3 to 3
y = 2**x * np.sin(10 * x) # Calculating the function Y(x) = 2^x * sin(10x)

plt.plot(x, y, 'r-', label='Y(x) = 2^x * sin(10x)')  # Plotting the function with a red line
plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Графік функції Y(x) = 2^x * sin(10x)') # Task 1
plt.legend()
plt.grid(True) 

plt.savefig('task1_plot.png', dpi=300) # Saving the plot as a PNG file
plt.show()
