class Ulamek:
    def __init__(self, licznik: int, mianownik: int):
        self.licznik = licznik
        self.mianownik = mianownik

    def __str__(self):
        return str(self.licznik) + "\n" + ('-' * 5) + "\n" + str(self.mianownik) + "\n"


u1 = Ulamek(12, 23)
u2 = Ulamek(34, 77)

print(u1)
print(u2)
