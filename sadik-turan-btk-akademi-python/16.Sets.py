fruits = { 'orange', 'apple', 'banana'}

#print(fruits[0]) index'lenemez !
#sıralayamayız.

for x in fruits:
    print(x)

fruits.add('cherry')
print(fruits)

fruits.update(['mango','grape','apple'])
print(fruits)
#Sets yapısı aynı elemandan iki tane içermez.

myList = [1,2,5,4,4,2,1]
print(f"***list : {myList}")
print(f"***set : {set(myList)}")
#set tekrarlanan eleman içermez

fruits.remove('mango')
print(fruits)

fruits.discard('apple')
print(fruits)

fruits.clear()
print(fruits)