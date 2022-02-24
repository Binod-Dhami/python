#crating the empty set
from queue import Empty
from turtle import clear


b=set()
b.add(1)
b.add(4)
#b.add([4,5,3,2])#list cant be use 
b.add(5)#we can use tuple
b.add(4)#can't repited the value 
#b.add({4:5})#cant be use 
print(b)
#.length of set
print(len(b))
#.remove
b.remove(1)
print(b)
#.pop()S
print(b.pop())
print(b.clear())
print(b.union({4,7}))
print(b.intersection({8,11}))