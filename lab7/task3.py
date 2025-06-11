import matplotlib.pyplot as plt

text = """
Привіт! Як твої справи? Я сьогодні був у магазині... Там було багато людей. Це звичайний день. Ти підеш зі мною? Яка чудова погода!
"""

# list of sentences
sentences = []
sentence = ''
i = 0
while i < len(text):
    sentence += text[i]
    if text[i:i+3] == '...': # three dots
        sentence += text[i+1:i+3] 
        i += 2
        sentences.append(sentence.strip())
        sentence = ''
    # end of sentence conditions
    elif text[i] in '.!?…':
        sentences.append(sentence.strip())
        sentence = ''
    i += 1

counts = { # 0. Initialize counts for each type of sentence
    'Звичайні': 0,
    'Питальні': 0,
    'Окличні': 0,
    'Трикрапка': 0
}

for s in sentences:
    s = s.strip()
    if s.endswith('...') or s.endswith('…'): # three dots
        counts['Трикрапка'] += 1
    elif s.endswith('?'):
        counts['Питальні'] += 1
    elif s.endswith('!'):
        counts['Окличні'] += 1
    elif s.endswith('.'):
        counts['Звичайні'] += 1

plt.bar(counts.keys(), counts.values(), color='green', edgecolor='black') # 1. Create a bar chart for sentence types
plt.xlabel('Тип речення')
plt.ylabel('Частота')
plt.title('Гістограма типів речень у тексті')
plt.grid(axis='y')

plt.savefig('task3_histogram_sentences.png', dpi=300)
plt.show()