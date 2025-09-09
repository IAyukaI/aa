a = input(print("Podaj liczbe dodatnia, calkowita a: "))
if a <= "0":
    a = input(print("Nie spelniles wymogow! Podaj liczbe a jeszcze raz"))
if a >= "0":
    print("Podana liczba jest prawidlowa!")


M = input(print("Podaj liczbe dodatnia, calkowita M: "))
if M < "0":
    M = input(print("Nie spelniles wymogow! Podaj liczbe M jeszcze raz"))
if M > "0":
    print("Podana liczba jest prawidlowa!")


x = input(print("Podaj liczbe nieujemna, calkowita x: "))
if x <= "0":
    x = input(print("Nie spelniles wymogow! Podaj liczbe x jeszcze raz"))
if x >= "0":
    print("Podana liczba jest prawidlowa!")

b1 = a^x
b2 = b1 / M
b3 = int(b2)
b = M - (b3*b1)

print("wynik potegowania modulo dla podanych przez ciebie liczb wynosi: " ,b)



