n = input(print("podaj zakres:"))
pierwsza = []
for i in range(n):
    pierwsza = pierwsza + [i%2==1]
pierwsza[2] = True
d=3
while d*d<n:
    pierwsza[i+d]=False
    i+=2
d+=2
while not pierwsza[d]:
    d+=2
for i in range(1,n):
    if pierwsza[1]:
        print(i)
print()