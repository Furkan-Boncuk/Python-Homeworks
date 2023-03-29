name = 'furkan'
surname = 'boncuk'
age = 36

print('My name is {} {}'.format(name,surname)) # name surname bilgilerini süslü parantezlerin içine yazdırır
print('My name is {0} {1}'.format(name,surname)) # sırayla yazar
print('My name is {1} {0}'.format(name,surname)) # tam tersi yerlere yazdırır
print('My name is {} {} and I am {} years old'.format(name,surname,'36'))

print('My name is {s} {n}'.format(n=name,s=surname)) # kısaltmalar ile sıralayabiliriz

print(f"My name is {name} {surname} and I am {age} years old")

result = 22/7
print('the result is : {r:1.3} '.format(r = result))
# r:1.3 ifadesinde 3, sayının virgülden sonra 2 basamak gözükmesi için; 1 ise sayının başına bir boşluk bırakılması içindir



