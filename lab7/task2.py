import matplotlib.pyplot as plt
from collections import Counter
import string

text = "Випадковий текст для тестування роботи коду." # Text to analyze

letters = [char.lower() for char in text if char.lower() in string.ascii_letters or char.lower() in 'абвгґдеєжзийіїклмнопрстуфхцчшщьюя'] # Extracting letters
letter_counts = Counter(letters)

labels = sorted(letter_counts) # Sorting letters alphabetically
values = [letter_counts[letter] for letter in labels]

plt.bar(labels, values, color='skyblue') # Creating a bar chart
plt.xlabel('Літери')
plt.ylabel('Частота')
plt.title('Гістограма частоти появи літер у тексті') # Task 2
plt.grid(True, axis='y')

plt.savefig('task2_histogram_letters.png', dpi=300) # Saving the histogram as a PNG file
plt.show()