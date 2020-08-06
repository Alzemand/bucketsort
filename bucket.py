# Bucket Sort usando Python
from random import uniform
from matplotlib import pyplot as plt
import time
import timeit

# 1. Gere randomicamente o vetor A de 100000 elementos tipo float 0.0≤x<1.0
elementos = 1000
count = 0

A = []
for x in range(elementos):
    y = round(uniform(0.0, 1.0), 5)
    A.append(y)

def bucketSort(array):
    bucket = []

    # Criar uma lista vazia
    for i in range(100):
        bucket.append([])

    # Inserir elementos em seus respectivos indices
    for j in array:
        index_b = int(100 * j)
        bucket[index_b].append(j)

    # Classificar os elementos no bucket
    for i in range(100):
        bucket[i] = sorted(bucket[i])

    return bucket


bucket = bucketSort(A)

for x in bucket:
    print ("[" + str(count) + "]", x)
    count += 1

count = 0
for x in bucket:
    print ("[" + str(count) + "]", len(x))
    count += 1


plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()