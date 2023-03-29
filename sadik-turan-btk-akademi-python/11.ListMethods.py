numbers = [1,10,5,16,10,10,4,9,12]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val = max(numbers)
val = max(letters)
val = min(letters)
val = numbers[3:6]
val = numbers[4:]
numbers.append(49) #eleman ekler
numbers.insert(3,78) #belirtilen indise eleman ekler
numbers.insert(-1,31)

numbers.pop(-1) #belirtilen indisteki elemanı siler. default sondaki elemanı siler
numbers.remove(31) #belirtilen elemanı siler

numbers.sort();#listeyi sıralar
letters.sort();
numbers.reverse();#tersten sıralar

print(f"10 elemanının sayısı : {numbers.count(10)}")

print(numbers)
print(letters)
print(val)
