def odwi(t):
    wynik = t[:0]

    for i in range(len(t)-1, -1, -1):
        wynik += t[i:i+1]
    return wynik


def odwr(t):
    if len(t) == 0:
        return t
    else:
        return odwr(t[1:]) + t[:1]


def fr(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fr(n - 1) + fr(n - 3)


def nwd1(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def nwd2(a, b):
    if b != 0:
        return nwd2(b, a % b)
    else:
        return a


print(odwi("abcdef"))
print(odwi([1, 2, 3, 4, 5]))

print(odwr("abcdef"))
print(odwr([1, 2, 3, 4, 5]))

for i in range(13):
    print(f"{fr(i)}")

print(nwd1(48, 18))
print(nwd2(48, 18))
