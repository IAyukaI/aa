import time


def f1(n):
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s


def f2(n):
    if n > 1:
        return n * f2(n - 1)
    else:
        return 1


start1 = time.time()
print(f1(15), "czas funkcji 1: ", start1 - time.time())

start2 = time.time()
print(f2(15), "czas funkcji 2: ", start2 - time.time())
