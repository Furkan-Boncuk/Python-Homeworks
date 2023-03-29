# String : Karakter dizileri
name = 'furkan'
surname = 'boncuk'
age = 18

greeting = 'my name is '+ name + ' '+ surname + ' and \nI am '+ str(age) + 'years old .'

print(greeting)
print(greeting[0]) # output = m
print(greeting[3])

length = len(greeting) # uzunluğu verecektir,48.  len()
print(greeting[length-1]) # son karakterini bize getirir
print(greeting[-1]) # -1 dediğimizde yine son karakteri çağıracaktır.

print(greeting[3:7]) # 3 ile 7 arasında kalan elemanları getirir
print(greeting[8:]) # 8.karakterden başar ve tüm elemanları çağırır
print(greeting[:17]) # 17.karaktere kadar yazar

text2 = '12345678901234567890'
print(text2[0:20:2])
# 0 dan 20.karaktere kadar git ancak her karakteri alma 2 karakterde 1 al
