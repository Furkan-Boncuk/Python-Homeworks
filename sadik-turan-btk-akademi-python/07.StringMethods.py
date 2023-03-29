message = "Hello There. My Name is Furkan Boncuk"
bigMessage = message.upper() #büyük karakter

smallMessage = message.lower() #küçük karakter

titleMessage = message.title() #başlık şeklinde yazar

firstLetterBigMessage = message.capitalize() #ilk harfi büyük yazar

spaceCharacterClippedMessage = message.strip() #metnin başındaki boşluk karakterini siler

arrayMessage = message.split() #metindeki her kelimeyi diziye dönüştürür
print(arrayMessage[6])

arrayMessage2 = message.split('e') #e harfine göre elemanlara ayırır

joinedMessage = '-'.join(arrayMessage) #elemanları birleştirebilir,birleştirirken elemanlarına arasına bir ifade koyabiliriz

soughtMessage = message.find('Furkan') #verilen ifadeyi metinde arar ve bulursa ilk harfinin hangi indexte olduğunu söyler
print(soughtMessage)

isFound = message.startswith("H") #Metin H hargi ile mi başlıyor ? true false
print(isFound)

isFound2 = message.endswith("K") #Metin H hargi ile mi başlıyor ? true false
print(isFound2)

changedMessage = message.replace('Furkan Boncuk','Furkan Bey') #1.kısımda belirtilen ifadeyi 2.kısımdakiyle değiştirir
print(changedMessage)

changedMessage2 = message.replace('H','h').replace('i','I').replace(' ','-')
print(changedMessage2)

centerMessage = message.center(50) #50 karakterlik bir yer açar ve metni oraya tam ortalar
print(centerMessage)




