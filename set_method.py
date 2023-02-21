b=set()
print(type(b))

#if we add some elements in set, then we can do use this methods
b.add(1)
b.add(2)
b.add(4)
b.add(5)
#b.add([6,8,9]) #return error bcz we can not add list in set method
b.add((6,8,9)) #now we can this 
#b.add({10:11}) #can not add dictionary 
print(b)

print(len(b)) #prints the length of sets

b.remove(5)
print(b)
print(b.pop())
print(b)