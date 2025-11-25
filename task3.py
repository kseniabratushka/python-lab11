import matplotlib.pyplot as plt
import string
from collections import Counter
import re

# Зчитування тексту з файлу
with open('bible-kjv.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Базова токенізація
def tokenize_text(text):
    # Видаляємо пунктуацію та розділяємо на слова
    text = text.lower()
    words = re.findall(r'\b[a-z]+\b', text)
    return words

# Базовий список стоп-слів
basic_stopwords = {
    'the', 'and', 'of', 'to', 'a', 'in', 'that', 'he', 'shall', 'unto',
    'for', 'i', 'his', 'be', 'is', 'with', 'it', 'not', 'him', 'but',
    'as', 'was', 'are', 'you', 'me', 'my', 'they', 'have', 'from', 'or',
    'we', 'your', 'this', 'which', 'will', 'their', 'all', 'them', 'when',
    'there', 'if', 'so', 'what', 'then', 'were', 'who', 'had', 'been',
    'would', 'could', 'should', 'may', 'might', 'must', 'can'
}

# Токенізація
words = tokenize_text(text)
total_words = len(words)
print(f"Загальна кількість слів: {total_words}")

# Найбільш вживані слова
word_freq = Counter(words)
top_10 = word_freq.most_common(10)

print("\n10 найбільш вживаних слів:")
for i, (word, count) in enumerate(top_10, 1):
    print(f"{i}. {word}: {count}")

# Діаграма
words_list, counts = zip(*top_10)
plt.figure(figsize=(12, 6))
plt.bar(words_list, counts, color='skyblue')
plt.title('10 найбільш вживаних слів у тексті Біблії')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.3)
plt.show()

# Очищення від стоп-слів
cleaned_words = [word for word in words if word not in basic_stopwords]
cleaned_freq = Counter(cleaned_words)
top_10_cleaned = cleaned_freq.most_common(10)

print("\n10 найбільш вживаних слів після очищення:")
for i, (word, count) in enumerate(top_10_cleaned, 1):
    print(f"{i}. {word}: {count}")

# Діаграма для очищеного тексту
cleaned_words_list, cleaned_counts = zip(*top_10_cleaned)
plt.figure(figsize=(12, 6))
plt.bar(cleaned_words_list, cleaned_counts, color='lightgreen')
plt.title('10 найбільш вживаних слів (після видалення стоп-слів)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.grid(axis='y', alpha=0.3)
plt.show()