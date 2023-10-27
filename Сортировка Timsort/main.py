import sys
class recursion_depth:
    def __init__(self, limit):
        self.limit = limit
        self.default_limit = sys.getrecursionlimit()
    def __enter__(self):
        sys.setrecursionlimit(self.limit)
    def __exit__(self, type, value, traceback):
        sys.setrecursionlimit(self.default_limit)
sys.setrecursionlimit(2600)




def binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = (start+end) // 2
    if the_array[mid] < item:
        return binary_search(the_array, item, mid + 1, end)
    elif the_array[mid] > item:
        return binary_search(the_array, item, start, mid - 1)
    else:
        return mid


def insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array

def merge(left, right):
    if left == []:
        return right
    if right == []:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def timsort(the_array):
    runs, sorted_runs = [], []
    l = len(the_array)
    new_run = [the_array[0]]

    for i in range(1, l):
        if i == l-1:
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        if the_array[i] < the_array[i-1]:
            if not new_run:
                runs.append([the_array[i-1]])
                new_run.append(the_array[i])
            else:
                runs.append(new_run)
                new_run = [the_array[i]]
        else:
            new_run.append(the_array[i])

    for each in runs:
        sorted_runs.append(insertion_sort(each))
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)
    return sorted_array
    # print(len(sorted_array))

from random import randint


# #defining the array to be sorted
# array = [randint(0, 4000) for i in range(2501)]
# print("The elements of the array before sorting are:")
# print(array)
# print(len(array))
# print("The elements of the array after sorting are:")
# timsort(array)

import time
#3.2.2. Внутренняя сортировка.  Отсортировать два массива в один
print("3.2.2. Внутренняя сортировка.  Отсортировать два массива в один")
start = time.time()
f = open("mergeSort/mass_3.2.2")
from random import randint
m1 = timsort([randint(0, 10000) for i in range(500)])
m2 = timsort([randint(0, 10000) for i in range(500)])
m3 = m1+m2
m3 = timsort(m3)
with open('mergeSort/mass_3.2.2', 'w') as f:
    f.write(str(m1) + "\n" + str(m2) + "\n" + "\n" + str(m3))
end = time.time() - start
print("timeInt = " + str(end) + " sec")