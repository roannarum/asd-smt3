from time import time
from random import randint

def insertion_sort(data):
    start = time()
    count = len(data)
    for j in range(1, count):
        for i in range(j, 0, -1):
            if data[i] < data[i - 1]:
                data[i], data[i - 1] = data[i - 1], data[i]
            else:
                break
    end = time()
    return end - start

data = [randint(0,100) for i in range(4_000)]
interval = insertion_sort(data)
print(insertion_sort(data))