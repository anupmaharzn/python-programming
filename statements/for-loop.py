# many objects in python are 'iterable' meaning we can iterate over every element in the object
# we can use for loops to execute a block of code for every iteration


# syntax
"""
for variable in iterable:
    # code to be executed for each iteration
# Here, iterable is the sequence or iterable object you want to loop through, and variable is a variable that takes on each value in the sequence during each iteration of the loop.
"""


#loop throught list

fruits = ['apple','banana','orange']

for a in fruits:
    print(a)

#loop through a string:

for char in 'hello':
    print(char)

#looping through a range of numbers
for num in range(1,5):
    print(num)

#loooping with both index and value using 'enumerate'

fru = ['apple','banana','orange']

for index,value in enumerate(fru):
    print(f'Index {index}:{value}')


#looping with conditional statements

numbers = [1,2,3,4,5,6,7,3,4,5]
odd_list = []
even_list = []
for num in numbers:
    if num %2 == 0:
        print(f"{num} is even")
        even_list.append(num)
    else:
        print(f"{num} is odd")
        odd_list.append(num)

print('odd list numbers',odd_list)
print('even list numbers',even_list)


# with tuples

tup = (1,2,3)

for item in tup:
    print(item)



#tuple unpacking

mylist = [(1,2),(3,4),(5,6),(7,8)]
print('length of mylist',len(mylist))

for (a,b) in mylist:
     print(a)
     print(b)


dict = {
    'k1':1,
    'k2':2,
    'k3':3
}

for key,value in dict.items(): # dict.items() return in list of tuple form then using tuple unpacking
    print(value)

    # we also have dict.values()