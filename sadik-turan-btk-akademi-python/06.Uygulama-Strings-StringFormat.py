website = "http://www.sadikturan.com"
course = "Phyton Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"
#1
length = len(course)
print(length)
#2
print(website[7:10]) # 7. 8. 9. karakterleri alır
#3
length2 = int(len(website))
print(website[length2-3:length2])
#4
print(course[:15]+"  -  "+course[-15:])

#5 course ifadesindeki karakterleri tersten yazdırın
result = course[::-1]
print(result) #tersten yazdırır
print(result[::-1]) #tersini tersten yazdırır

name,surname,age,job = 'Furkan','Boncuk',18,'Bilgisayar Mühendisi'
#6
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")
#7
text = 'Hello world'
text = text[0:6] + 'W' + text[-4:]
print(text)
#8
result = 'abc' * 3
print(result) #abc ifadesini 3 kere yan yana yazdırır