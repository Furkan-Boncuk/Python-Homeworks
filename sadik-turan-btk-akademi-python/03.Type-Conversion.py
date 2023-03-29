x = input('1.sayı: ')
y = input('2.sayı: ')
toplam = x + y
print(toplam) #default olarak string değer alır
print(type(x))
print(type(y))
toplam2 = int(x) + int(y)
print(toplam2)
#Type Conversion
#   int to float
x = float(x)
print(x)
#   float to int
y = int(y) # y için float değer verdiğimizde yalnızca virgülden öncesini yazacak
print(y)
#   boolean to int
isOnline = False
isOnline = int(isOnline)
print(isOnline)

