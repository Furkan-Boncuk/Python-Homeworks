carList = ['Bmw','Mercedes','Opel','Mazda']
#Listede eleman arama :
result = 'Mercedes' in carList
print(result)

#-2 deki elemanı alma :
elementInNegative = carList[-2]
print(elementInNegative)

#ilk 3 elemanı alma :
firstThreeElement = carList[0:3]
print(firstThreeElement)

# son 2 elemanının yerine Toyota ve Renault u ekle :
editedCarList = carList
editedCarList[2:4] = ['Toyota','Renault']
print(editedCarList)

#Listeye Audi ve Nissan değerlerini ekle :
addedCarList = carList + ['Audi','Nissan']
print(addedCarList)

#Listenin son elemanını sil :
deletedCarList = addedCarList
del deletedCarList[-1]
print(deletedCarList)


studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

resultA = f"{studentA[0]} {studentA[1]}, 9 yaşında ve notları:\n \
          {studentA[3][0]},{studentA[3][1]},{studentA[3][2]}"
print(resultA)












