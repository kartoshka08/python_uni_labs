TS_min = 32


def find_minrun(n):
   r = 0
   while n >= TS_min:
       r |= n & 1
       n >>= 1
   return n + r


def insertion_sort(array, left, right):
   for i in range(left + 1, right + 1):
       element = array[i]
       j = i - 1
       while element < array[j] and j >= left:
           array[j + 1] = array[j]
           j -= 1
       array[j + 1] = element
   return array


def merge(array, l, m, r):
   array_length1 = m - l + 1
   array_length2 = r - m
   left = []
   right = []
   for i in range(0, array_length1):
       left.append(array[l + i])
   for i in range(0, array_length2):
       right.append(array[m + 1 + i])

   i = 0
   j = 0
   k = l

   while j < array_length2 and i < array_length1:
       if left[i] <= right[j]:
           array[k] = left[i]
           i += 1

       else:
           array[k] = right[j]
           j += 1

       k += 1

   while i < array_length1:
       array[k] = left[i]
       k += 1
       i += 1

   while j < array_length2:
       array[k] = right[j]
       k += 1
       j += 1


def timsort(array):
   n = len(array)
   minrun = find_minrun(n)

   for start in range(0, n, minrun):
       end = min(start + minrun - 1, n - 1)
       insertion_sort(array, start, end)

   size = minrun
   while size < n:

       for left in range(0, n, 2 * size):
           mid = min(n - 1, left + size - 1)
           right = min((left + 2 * size - 1), (n - 1))
           merge(array, left, mid, right)

       size = 2 * size




import time


#3.2.1 внешняя сортировка (объединение. пересечение, разность, симметрич.разность)
#для объединения
print("3.2.1 внешняя сортировка (объединение. пересечение, разность, симметрич.разность):")

#записываем два файла
f = open("mergeSort/mass_3.2.1(1)")
from random import randint
a = [randint(0, 4000) for i in range(2600)]
timsort(a)
with open('mergeSort/mass_3.2.1(1)', 'w') as f:
    f.write(str(a))

f = open("mergeSort/mass_3.2.1(2)")
b = [randint(0, 4000) for i in range(2600)]
timsort(b)
with open('mergeSort/mass_3.2.1(2)', 'w') as f:
    f.write(str(b))

#выполняем остальное задание
#для объединения

c1 = []
for i in range(len(a)-1):
    c1.append(a[i])
for j in range(len(b)-1):
    c1.append(b[j])

start = time.time()
timsort(c1)
end = time.time() - start
print("time for 1st " + str(end) + " sec")


#для пересечения / перечисления  только те числа, которые есть и там и там

c2 = []
for i in a:
    for j in b:
        if i == j:
            c2.append(i)
            break


start = time.time()
timsort(list(c2))
end = time.time() - start
print("time for 2nd " + str(end) + " sec")


#для разности (числа, принадлежащие первому множеству, но не второму)
start = time.time()
c3 = []
sov = 0
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[i] == b[j]:
            sov += 1
    if sov == 0:
        c3.append(a[i])
    sov = 0

timsort(list(c3))
end = time.time() - start
print("time for 3rd " + str(end) + " sec")


#для симметрич.разности (объединение разностей множеств)
start = time.time()
a = set(a)
b = set(b)
c4 = a.symmetric_difference(b)
timsort(list(c4))
end = time.time() - start
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
m1 = [randint(0, 4000) for i in range(2500)]
timsort(m1)
m2 = [randint(0, 4000) for i in range(2500)]
timsort(m2)
m3 = m1+m2
timsort(m3)

with open('mergeSort/mass_3.2.2', 'w') as f:
    f.write(str(m1) + "\n" + str(m2) + "\n" + "\n" + str(m3))
end = time.time() - start
print("timeInt = " + str(end) + " sec")


#3.2.3. Внутренняя сортировка. Дана целочисленная квадратная матрица размером n=5000. Используя указанные методы,
# упорядочить в ней значения по возрастанию в строках и столбцах. Определить время работы, число сравнений и перестановок.
print("3.2.3. Внутренняя сортировка. Дана целочисленная квадратная матрица")
start = time.time()

from random import randint

# ввод матрицы
matrix = [0] * 10
for i in range(10):
    matrix[i] = [randint(0, 11) for i in range(10)]


# сортировка матриццы
    # сортировка строк матрицы
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        timsort(matrix[i])
    # сортировка столбцов матрицы
for i in range(len(matrix)):
    timsort(matrix)

with open('mergeSort/mass_3.2.3', 'w') as f:
    for i in range(len(matrix)):
        t = str(matrix[i])+ "\n"
        f.write(t)

end = time.time() - start
print("time_3.2.3 = " + str(end) + " sec")