
# range function is ues to generate a sequence of numbers

"""
syntax

range(stop)
range(start,stop)
range(start,stop,step)

"""
print(list(range(0,11,2)))


#enumerate function in python is used to iterate over a sequence (such as a list, tuple, or string)  along with an index

fruits = ["apple", "banana", "cherry"]

for index, value in enumerate(fruits):
    print(f"Index {index}: {value}")

#zip function in python is used to combine two or more iterables (eg lists tuples) element-wise.


color = ['red','yellow','purple']

for fru,col in zip(fruits,color):
    print(fru)
    print(col)

"""
#output
apple
red
banana
yellow
cherry
purple

"""

print(2 in [1,2,3]) # return True

print('mykey' in {'mykey':212}) #return True

d={
    'mykey':345
}
print(345 in d.values()) # return True
print('mykey' in d.keys()) # return True

mylist = list(range(1,11,2))

print(min(mylist))
print(max(mylist))

from random import shuffle

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist) # doesnot return

print(mylist)

from random import randint

randomnumber = randint(1,100)
print(randomnumber)

userinput = int(input('Enter a number here:')) #input type is string

print('you have entred :',userinput)

