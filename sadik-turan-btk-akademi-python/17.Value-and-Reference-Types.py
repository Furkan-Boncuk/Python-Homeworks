# Value Types => String, number(int,float)
x = 5
y = 25

x = y

y = 10

print(x,y)

# Reference Types => list, class
a = ["apple","banana"]
b = ["apple","banana"]

a = b

b[0] = "grape"

print(a,b)

# referans tipler bir adrese bağlıdır. Örneğin bir listeyi
# kopyaladığımızda onun kopyası değil bellekteki adresinin bir
# kopyası alınır