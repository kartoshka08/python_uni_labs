import re

b = {
   "a" : 0,
   "б" : 1,
   "в" : 2,
   "г" : 3,
   "д" : 4,
   "е" : 5,
   "ж" : 6,
   "з" : 7,
   "и" : 8,
   "й" : 9,
   "к" : 10,
   "л" : 11,
   "м" : 12,
   "н" : 13,
   "о" : 14,
   "п" : 15,
   "р" : 16,
   "с" : 17,
   "т" : 18,
   "у" : 19,
   "ф" : 20,
   "х" : 21,
   "ц" : 22,
   "ч" : 23,
   "ш" : 24,
   "щ" : 25,
   "ь" : 26,
   "ы" : 27,
   "ъ" : 28,
   "э" : 29,
   "ю" : 30,
   "я" : 31,
}
text = open('file.txt','r').read()
text = text.lower()
text = re.sub("[.,;:()\n1234567890%abcdefghijklmnopqrstuvwxyz]","",text)
text = text.replace(" — ", " ")
text = text.replace("  ", " ")
text1 = sorted(list(set(text.split(" "))))
text2 = sorted(list(text.split(" ")))

a1 = []
array1 = []
for i in range(0, len(text1)):
    a1.append(list(text1[i]))

for i in range(0, len(text1)):
    l1 = a1[i]
    l1 = [b.get(k, 0) for k in l1]
    array1.append(l1)

a2 = []
array2 = []
for i in range(0, len(text2)):
    a2.append(list(text2[i]))

for i in range(0, len(text2)):
    l2 = a2[i]
    l2 = [b.get(k, 0) for k in l2]
    array2.append(l2)



import time
import pandas as pd

def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

dict = []

def create_dict(array1, array2, text1):
    start = time.time()
    global dict
    global count
    for i in array1:
        count = 0
        for j in array2:
            if i==j and sequential_search(array2,i):
                count+=1
                del j
        stop = time.time()
        a = count
        dict.append([text1[array1.index(i)],a,(stop-start)])
    return dict

DATA1 = create_dict(array1, array2, text1)
DATA1 = sorted(DATA1, reverse = True, key = lambda finalTableSecond: finalTableSecond[1])

df = pd.DataFrame(DATA1,columns=["Слово", "Количество", "Время поиска"])
print(df)





def logarithmic_search(array, target):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        mid_value = array[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

dict = []

def create_dict(array1, array2, text1):
    start = time.time()
    global dict
    global count
    for i in array1:
        count = 0
        for j in array2:
            if i==j and logarithmic_search(array2,i):
                count+=1
                del j
        stop = time.time()
        a = count
        dict.append([text1[array1.index(i)],a,(stop-start)])
    return dict
DATA1 = create_dict(array1, array2, text1)
DATA1 = sorted(DATA1, reverse = True, key = lambda finalTableSecond: finalTableSecond[1])

df = pd.DataFrame(DATA1,columns=["Слово", "Количество", "Время поиска"])
print(df)



#ЧЕСТЬ 2

import re
import random

b = {
   "a" : 0,
   "б" : 1,
   "в" : 2,
   "г" : 3,
   "д" : 4,
   "е" : 5,
   "ж" : 6,
   "з" : 7,
   "и" : 8,
   "й" : 9,
   "к" : 10,
   "л" : 11,
   "м" : 12,
   "н" : 13,
   "о" : 14,
   "п" : 15,
   "р" : 16,
   "с" : 17,
   "т" : 18,
   "у" : 19,
   "ф" : 20,
   "х" : 21,
   "ц" : 22,
   "ч" : 23,
   "ш" : 24,
   "щ" : 25,
   "ь" : 26,
   "ы" : 27,
   "ъ" : 28,
   "э" : 29,
   "ю" : 30,
   "я" : 31,
}
text = open('file.txt','r').read()
text = text.lower()
text = re.sub("[.,;:()\n1234567890%abcdefghijklmnopqrstuvwxyz]","",text)
text = text.replace(" — ", " ")
text = text.replace("  ", " ")
random_words = []
for i in range(10000):
    random_words.append(random.choice(text))

text = sorted(list(set(text.split(" "))))
a = []
array = []
for i in range(0, len(text)):
    a.append(list(text[i]))

for i in range(0, len(text)):
    l = a[i]
    l = [b.get(k, 0) for k in l]
    array.append(l)


import time
find_word = input("Введите слово: ")
find_word = find_word.lower()
find_word = re.sub("[.–,:()\n1234567890 ]","",find_word)
find_word = list(find_word)
find_word = [b.get(k, 0) for k in find_word]

start_time = time.time()
def sequential_search(arr, n, target):
    global count
    count = 0
    for i in range(len(arr)):
        count += 1
        if arr[i] == target:
            return i, count
    return -1, count
time = time.time() - start_time
n = len(array)
result = sequential_search(array, n, find_word)
if(result == -1):
    print("Не найдено", count)
else:
    print("Найдено", "\n", "Время поиска: ", time , "seconds", "\n", "число обращений к массиву: ", count)

import time

start_time = time.time()


def logarithmic_search(array, target):
    global count
    count = 0
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int(low + (high - low) / 2)
        mid_value = array[mid]
        count += 1
        if mid_value == target:
            return mid, count
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, count


time = time.time() - start_time
find_word = input("Введите слово: ")
find_word = find_word.lower()
find_word = re.sub("[.–,:()\n1234567890 ]", "", find_word)
find_word = list(find_word)
find_word = [b.get(k, 0) for k in find_word]

result = logarithmic_search(array, find_word)

if result != -1:
    print("Найдено", "\n", "Время поиска: ", time, "seconds", "\n", "число обращений к массиву: ", count)
else:
    print("Не найдено", count)