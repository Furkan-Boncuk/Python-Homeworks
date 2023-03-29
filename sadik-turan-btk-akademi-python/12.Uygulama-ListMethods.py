names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998,2000,1998,1987]

#1- Cenk ismini listenin sonuna ekle :
names.append('Cenk')
result = names
#2- Sena ismini listenin başına ekle :
names.insert(0,'Selin')
result = names
#3- Deniz ismini listeden siliniz :
names.remove('Deniz')
result = names
#4- Yağmur isminin indeksi nedir :
result = names.index('Yağmur')
#5- Ali listenin bir elemanı mıdır :
result = 'Ali' in names
#6- Liste elemanlarını ters çevirin :
names.reverse()
print(names)
#7- Listeleri sırala
names.reverse()

names.sort()
print(names)
years.sort()
print(years)
#8- str = "Chevrolet,Dacia" karakter dizisini listeye çevir :
str = "Chevrolet,Dacia"
cars = str.split(',')
print(cars)
#9- years dizisinin en büyük ve en küçük elemanı :
valOfYears = max(years)
print(valOfYears)
valOfYears = min(years)
print(valOfYears)
#10- years dizisinde kaç tane 1998 değeri vardır :
result = years.count(1998)
#11- years dizisinin elemanlarını siliniz :
years.clear()
print(years)
#12- kullanıcıdan alınan 3 tane marka bilgisini bir listede sakla :
markalar = []

marka = input("1.marka : ")
markalar.append(marka)
marka = input("2.marka : ")
markalar.append(marka)
marka = input("3.marka : ")
markalar.append(marka)

print(markalar)



print(result)
