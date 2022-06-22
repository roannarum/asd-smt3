from time import time
from random import randint

def selection_sort(data):
    start = time()
    count = len(data)
    for k in range(count):
        j = count - k - 1
        big = 0
        for i in range(j + 1):
            if data[i] > data[big]:
                big = i
        data[j], data[big] = data[big], data[j]

    end = time()
data = [7, 5, 2, 8, 9, 1, 0, 5, 3, 4]
selection_sort(data)
print(data)