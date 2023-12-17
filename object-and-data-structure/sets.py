#sets are unordered collections of unique elements
# meaning there can only be one representative of the same object.

myset = set()

print(myset)

myset.add(1)
print(myset)

myset.add(2)
print(myset) #output {1,2}
# it wont repeat it 
myset.add(2)
print(myset) #output {1,2}


#-----another example-----

mylist = [1,2,2,2,2,3,1,3,12,2,4,4,1,1]

print(set(mylist)) #output {1, 2, 3, 4, 12}