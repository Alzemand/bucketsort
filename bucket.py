# Bucket Sort usando Python
from random import uniform
from matplotlib import pyplot as plt


elementos = 100000
count = 0
A = []
eixox = []
eixoy = []

def bucket_sort(array):
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

def bucketToArray(array):
    k = 0
    temp = []
    for i in range(len(array)):
        for j in range(len(array[i])):
            temp.append(array[i][j])
            k += 1
    return temp

for x in range(elementos):
    y = round(uniform(0.0, 1.0), 5)
    A.append(y)

bucket = bucket_sort(A)
A = bucketToArray(bucket)

for x in bucket:
    print ("[" + str(count) + "]", x)
    count += 1
    eixox.append(count)

count = 0

for x in bucket:
    eixoy.append(len(x))
    count += 1

for x in A:
    print(x)

plt.bar(eixox, eixoy)
plt.show()
