""" 
    python has 4 data type 
    - String ==> str
    - Integer ==> int
    - Float ==> float
    - Boolean ==> bool
    - Complex ==> complex

"""

a = 10
print("nilai a =", a, " ==> tipe data a adalah:", type(a))

b = 10.5
print("nilai b =", b, "==> tipe data b adalah", type(b))

c = 'ini adalah string'
print("nilai c =", c, "==> tipe data c adalah", type(c))

d = True
print("nilai d =", d, "==> tipe data d adalah", type(d))

e = 1j
print("nilai e =", e, "==> tipe data e adalah", type(e))

f = complex(a)
print("nilai conversion a:", a, "to complex adalah ", f)

g = complex(b)
print("nilai conversion b:", b, "to complex adalah ", g)