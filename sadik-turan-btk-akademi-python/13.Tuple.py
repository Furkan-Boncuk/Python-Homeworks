#tuple ile list aynı mantıktadır ancak tuple için bir eleman değişikliği yapamayız

list = ['ali','veli','ayşe']
tuple = 'ali','veli','ayşe'

print(f"Liste : {list}")
print(f"Tuple : {tuple}")

list[0] = 'ahmet'
#tuple[0] = 'deniz'  --> HATA VERİR.

names = ('demet','emel','zeynep') + tuple

print(names)


