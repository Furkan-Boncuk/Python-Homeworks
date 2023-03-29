x, y, z = 2, 5, 10

# kullanıcıdan alınan iki sayının çarpımı ile x,y,z toplamının farkı nedir
number1 = int(input("1. sayı : "))
number2 = int(input("2. sayı : "))
result = (number1 * number2) - (x + y + z)
print(result)

# y nin x e kalansız bölümünü hesaplayınız
result = y//x
print(result)

# x,y,z toplamının mod 3 ü nedir
print((x+y+z) % 3)

# y nin x. kuvveti
result = y**x
print(result)

# !!! x, *y, z = numbers işlemini yapın
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
# bu şekildeki bir atama işleminde x ilk değeri alır, z son değeri alır. y ise arada kalanları alır
print(y)

# z nin küpünü bulun
result = z ** 3
print(result)

# y nin değerleri toplamı
result = y[0] + y[1] + y[2]
print(result)