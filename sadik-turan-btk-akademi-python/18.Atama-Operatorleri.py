x, y, z = 16, 5, 20
print(x, y, z)

x, y = y, x
print(x, y, z)

x += 10
x -= 5
x *= 2
x %= 4 # bölümden kalanı yazdırır
y //= 3 # tam bölme operatörü. tam kısmını yazdırır
y **= 3 # üs alma işlemi
print(x, y, z)

values = 1,2,3
print(values)

x,y,z = values
print(x,y,z)