parzyste = input("czy drukowac liczby parzyste (T/N) ")
maks = int(input("do jakiej wartosci: "))

if parzyste in("T", "t"):
    for i in range(2, maks+1, 2):
        print(i, end=" ")
else:
    for i in range(1, maks+1, 2):
        print(i, end=" ")
print()