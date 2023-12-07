#подготовка статьи
import time
import re

def text_to_array(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            text = file.read()
            # Удаление знаков препинания, цифр, чисел и скобок
            cleaned_text = re.sub(r'[\W\d\[\]()]', ' ', text)

            # Преобразование в строчные буквы и разбиение на слова
            words = cleaned_text.lower().split()

            # Удаление повторяющихся слов
            unique_words = list(set(words))

            return unique_words
    except FileNotFoundError:
        print("Файл не найден.")
        return []

# Пример использования:


#unique_words_array = text_to_array(filename)

#print(unique_words_array)
#print(len(unique_words_array))




# ИНДЕКСНО-ПОСЛЕДОВАТЕЛЬНЫЙ ПОИСК

global usageFirst #число обращений
usageFirst = 0

def sequential_search(arr, target):
    for i in range(len(arr)):
        global usageFirst
        usageFirst += 1
        if arr[i] == target:
            return i
    return -1

file_1 = "articleFirst.txt"
word_array = text_to_array(file_1)
target_word = "заканчивая"

start = time.time()
result = sequential_search(word_array, target_word)

if result != -1:
    print(f"Слово '{target_word}' найдено на позиции {result}")
else:
    print(f"Слово '{target_word}' не найдено в массиве")

end = time.time() - start
print("time for sequential search: " + str(end) + " sec")
print("число обращений при этом: " + str(usageFirst) + " раз")
print()


#ЛОГАРИФМИЧЕСКИЙ ПОИСК

global usageSecond
usageSecond = 0

def logarithmic_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        mid_value = array[mid]

        global usageSecond

        if mid_value == target:
            return mid
            usageSecond += 1
        elif mid_value < target:
            low = mid + 1
            usageSecond += 1
        else:
            high = mid - 1
            usageSecond += 1

    return -1

file_2 = "articleSecond.txt"
words = text_to_array(file_2)


target_word = "можно"

start = time.time()
result = logarithmic_search(words, target_word)

if result != -1:
    print(f"Слово {target_word} найдено на позиции {result}.")
else:
    print(f"Слово {target_word} не найдено.")

end = time.time() - start
print("time for sequential search: " + str(end) + " sec")
print("число обращений при этом: " + str(usageSecond) + " раз")