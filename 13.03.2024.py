import random
import datetime


def bubble_sort(l):
    n = len(l)
    for i in range(n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


n = 100000
t = []
for i in range(n):
    t.append(random.randint(0, 1000))

start = datetime.datetime.now()

print(bubble_sort(t.copy()))