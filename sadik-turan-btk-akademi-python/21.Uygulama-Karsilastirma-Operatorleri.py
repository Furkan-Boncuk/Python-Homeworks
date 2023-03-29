# Girilen iki sayıdan hangisi büyüktür
a = int(input("1. sayı : "))
b = int(input("2. sayı : "))

result = (a > b)
print(f"a: {a} b: {b} den büyüktür: {result}")

# Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50den büyükse geçti küçükse kaldı yazdırın
vize_1 = int(input("1.vize notu : "))
vize_2 = int(input("2.vize notu : "))
final = int(input("final notu : "))
ort = (0.6 * (vize_1 + vize_2)) + (0.4 * (final))

result = ort > 50
print(f"not ortalaması: {ort} dersi geçti: {result}")

# Girilen sayının tek mi çift mi olduğunu yazdırın
sayi = int(input("sayı girin : "))
result = (sayi %2 == 0)
print(f"girdiğiniz sayı çifttir : {result}")

# Girilen sayının pozitif mi negatif mi olduğunu yazdırın
sayi = int(input("sayı girin : "))
result = (sayi > 0)
print(f"girdiğiniz sayı pozitiftir : {result}")

# Parola ve email bilgisini isteyip doğruluğunu kontrol edin
# (email:furkanboncuk@gmail.com , parola:abc123)
email, parola = "furkanboncuk@gmail.com" , "abc123"
in_email = input("email girin : ")
in_parola = input("parola girin : ")

isEmail = (email == in_email.lower().strip())
isParola = (parola == in_parola.lower().strip())
print(f"Email bilgisi doğru mu: {isEmail} ve Parola doğru mu: {isParola}")