'''
1- Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle
dictionary içinde saklayınız
2- Öğrenci numarasını kullanıcıdan alıp ilgili öğrenciyi gösterin
'''
ogrenciler = {}

ogrenciNo = input('Öğrenci Numarası : ')
ad = input('Öğrenci Adı : ')
soyad = input('Öğrenci Soyadı : ')
telefon = input('Öğrenci Telefon Numarası : ')

'''
ogrenciler[ogrenciNo] = {
    'ad' : ad,
    'soyad' : soyad,
    'telefon' : telefon
}
'''

ogrenciler.update({
    ogrenciNo: {
        'ad':ad,
        'soyad':soyad,
        'telefon':telefon
    }
})

ogrenciNo = input('Öğrenci Numarası : ')
ad = input('Öğrenci Adı : ')
soyad = input('Öğrenci Soyadı : ')
telefon = input('Öğrenci Telefon Numarası : ')

ogrenciler.update({
    ogrenciNo: {
        'ad':ad,
        'soyad':soyad,
        'telefon':telefon
    }
})

print(ogrenciler)

print('*'*50)

ogrenciNo = input('Aranacak öğrencinin Öğrenci Numarası :')
arananOgrenci = ogrenciler[ogrenciNo]

print(f"Aradığınız {ogrenciNo} numaralı öğrencinin adı : {arananOgrenci['ad']} , soyadı : {arananOgrenci['soyad']} , telefon numarası : {arananOgrenci['telefon']}")
