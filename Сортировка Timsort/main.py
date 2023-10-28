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