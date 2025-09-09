a = 10
b = 8


def dodaj(a, b):
    for i in range (b):
        a += 1
    suma = a
    return suma


def odejmij(a, b):
    for i in range (b):
        a -= 1
    roznica = a
    return roznica


def iloczyn(a, b):
    c = 0
    for i in range(b):
        c = dodaj(a, b)
    return c


def iloraz(a, b):
    i = 0
    while a >= b:
        a = odejmij(a, b)
        i += 1
    return i, a


print(dodaj(a, b))
print(odejmij(a, b))
print(iloczyn(a, b))
print(iloraz(a, b))
