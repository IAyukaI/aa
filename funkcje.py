def sil(n):
    if n == 0 or  n== 1:
        return 1
    elif n < 0:
        return "Niepoprawna wartość"
    return n * sil(n-1)


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n < 0:
        return "Niepoprawna wartość"
    return fib(n-1) + fib(n-2)


def nwd(a, b):
    if b == 0:
        return a
    else:
        return nwd(b, a % b)


def pali(t, j, i=0):
    if i >= j:
        return t
    else:
        t[i], t[j] = t[j], t[i]
    return pali(t, j-1, i+1)