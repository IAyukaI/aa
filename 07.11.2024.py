def snr(n):
    if n == 1:
        n = 1
    elif n > 1:
        n = n + snr(n-1)
    return n


def sni(n):
    sn = 0
    for i in range(1, n + 1):
        sn = sn + i
    return sn


def lei(l1):
    d = 1
    while l1 > 10:
        d = d + 1
        l1 = l1 / 10
    return d


def ler(l2):
    d = 1
    if l2 < 10:
        return 1
    else:
        d = d + ler(l2/10)
    return d


def powr(n, p):
    if p == 1:
        return n
    else:
        return n * powr(n, p - 1)


def powi(n, p):
    a = 0
    while p > 1:
        p = p - 1
        a = a + n
    return a


def pali(n):
    n = str(n)
    a = 0
    b = len(n) - 1
    while a < b:
        if n[a] == n[b]:
            return True
        else:
            return False


print(snr(11), sni(11), lei(235325), ler(2353299999), powr(2, 5), powi(2, 5), pali(12321))
