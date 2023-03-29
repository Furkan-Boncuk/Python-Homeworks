# 1-100 e kadar sayıları yazdır
x = 1
while x<=100:
    print(x)
    x += 1
print('bitti...')

######################################
# isim bilgisi boş ifade olduğu sürece kullanıcıdan isim alma:

name = '' #False
while not name.strip():
    name = input('isminizi giriniz: ')

print(f'merhaba, {name}')