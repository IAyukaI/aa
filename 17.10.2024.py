def myfunc(n):
  return lambda a : a * n


aa = myfunc(4)
bb = myfunc(5)

print(aa(9))
print(bb(11))
