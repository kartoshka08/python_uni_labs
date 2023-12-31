
# сортировка слиянием
import time

def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    global comp
    global switch

    # Т. к. длина списков применяется часто, создадим для удобства переменные
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            comp += 1
            # Сравниваем первые элементы в начале каждого списка
            # Если 1-й элемент левого подсписка меньше, добавляем его в сортированный массив

            if left_list[left_list_index] <= right_list[right_list_index]:
                comp += 1
                switch += 1
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если 1-й элемент правого подсписка меньше, добавляем его в сортированный массив
            else:
                comp += 1
                switch += 1
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Когда достигнут конец левого списка, добавляем элементы правого списка в конец результирующего списка
        elif left_list_index == left_list_length:
            comp += 1
            switch += 1
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Когда достигнут конец правого списка, добавляем элементы левого списка в сортированный массив
        elif right_list_index == right_list_length:
            switch += 1
            comp += 1
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, когда он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Чтобы найти середину списка, применяем деление без остатка Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем сортированные списки в результирующий
    return merge(left_list, right_list)


global comp
global switch

comp = 0
switch = 0







#3.2.1 внешняя сортировка (объединение. пересечение, разность, симметрич.разность)
#для объединения
print("3.2.1 внешняя сортировка (объединение. пересечение, разность, симметрич.разность):")

#записываем два файла
f = open("mergeSort/mass_3.2.1(1)")
from random import randint
a = merge_sort([randint(0, 4000) for i in range(2600)])
with open('mergeSort/mass_3.2.1(1)', 'w') as f:
    f.write(str(a))

f = open("mergeSort/mass_3.2.1(2)")
b = merge_sort([randint(0, 4000) for i in range(2600)])
with open('mergeSort/mass_3.2.1(2)', 'w') as f:
    f.write(str(b))

#выполняем остальное задание

start = time.time()
c1 = a + b
c1 = merge_sort(list(c1))
end = time.time() - start
print("сравнений: " + str(comp) + "    перестановок: " + str(switch))
print("time for 1st " + str(end) + " sec")


#для пересечения / перечисления  только те числа, которые есть и там и там
a = set(a)
b = set(b)
start = time.time()
c2 = a.intersection(b)
c2 = merge_sort(list(c2))
end = time.time() - start
print("сравнений: " + str(comp) + "    перестановок: " + str(switch))
print("time for 2nd " + str(end) + " sec")


#для разности (числа, принадлежащие первому множеству, но не второму)
start = time.time()
c3 = a.difference(b)
c3 = merge_sort(list(c3))
end = time.time() - start
print("сравнений: " + str(comp) + "    перестановок: " + str(switch))
print("time for 3rd " + str(end) + " sec")


#для симметрич.разности (объединение разностей множеств)
start = time.time()
c4 = a.symmetric_difference(b)
c4 = merge_sort(list(c4))
end = time.time() - start
print("сравнений: " + str(comp) + "    перестановок: " + str(switch))
print("time for 4th " + str(end) + " sec")


f = open("mergeSort/mass_3.2.1")
with open('mergeSort/mass_3.2.1', 'w') as f:
    f.write( str(c1)+ "\n" + str(c2) + "\n"
             + str(c3) + "\n" + str(c4))





print()
#3.2.2. Внутренняя сортировка.  Отсортировать два массива в один
print("3.2.2. Внутренняя сортировка.  Отсортировать два массива в один")
start = time.time()
f = open("mergeSort/mass_3.2.2")
from random import randint
m1 = merge_sort([randint(0, 10000) for i in range(3000)])
m2 = merge_sort([randint(0, 10000) for i in range(3000)])
m3 = merge_sort(m1+m2)
with open('mergeSort/mass_3.2.2', 'w') as f:
    f.write(str(m1) + "\n" + str(m2) + "\n" + "\n" + str(m3))
end = time.time() - start
print("сравнений: " + str(comp) + "    перестановок: " + str(switch))
print("time_3.2.2 = " + str(end) + " sec")



print()
#3.2.3. Внутренняя сортировка. Дана целочисленная квадратная матрица размером n=5000. Используя указанные методы,
# упорядочить в ней значения по возрастанию в строках и столбцах. Определить время работы, число сравнений и перестановок.
print("3.2.3. Внутренняя сортировка. Дана целочисленная квадратная матрица")
start = time.time()

from random import randint

# ввод матрицы
matrix = [0] * 50
for i in range(50):
    matrix[i] = [randint(0, 100) for i in range(50)]


# сортировка матриццы
    # сортировка строк матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i] = merge_sort(matrix[i])
    # сортировка столбцов матрицы
for i in range(len(matrix)):
    matrix = merge_sort(matrix)

with open('mergeSort/mass_3.2.3', 'w') as f:
    for i in range(len(matrix)):
        t = str(matrix[i])+ "\n"
        f.write(t)

end = time.time() - start
print("сравнений: " + str(comp) + "    перестановок: " + str(switch))
print("time_3.2.3 = " + str(end) + " sec")
