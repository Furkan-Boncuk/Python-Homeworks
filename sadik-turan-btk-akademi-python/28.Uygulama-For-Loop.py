sayilar = [1,3,5,7,9,12,19,21]

# hangi sayılar 3ün katı
for sayi in sayilar:
    if (sayi%3 == 0):
        print(sayi)

# sayıların toplamı
toplam = 0
for sayi in sayilar:
    toplam += sayi
print(toplam)

# tek sayıların karesini alın
for sayi in sayilar:
    if (sayi %2 != 0):
        print(sayi**2)

#############################################################
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']

# Şehirlerden hangileri en fazla 5 karakterlidir
for sehir in sehirler:
    if (len(sehir) <= 5):
        print(sehir)

#############################################################
urunler = [
    {'name': 'samsung S6', 'price': '3000'},
    {'name': 'samsung S7', 'price': '4000'},
    {'name': 'samsung S8', 'price': '5000'},
    {'name': 'samsung S9', 'price': '6000'},
    {'name': 'samsung S10', 'price': '7000'}
]

# ürünlerin fiyatları toplamı nedir
toplam = 0
for urun in urunler:
    toplam += int(urun['price'])

print(toplam)












