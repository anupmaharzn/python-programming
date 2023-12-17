# map() function in  python is a built in function that applies a secified function to all items in an iterable (list tuple string)
# and returns an iterator that products the results.


# syntax

 
""" 
map(function,iterable)
"""

def square(number):
    return number**2

my_nums = [1,2,3,4,5]


# for item in my_nums:
#     sq_num = square(item)
#     print(sq_num)

for item in map(square,my_nums):
    print(item)

#or can convert to list as well

print(list(map(square,my_nums)))


#anthoer example of map

def splicer(str):
    if (len(str) %2) ==0:
        return 'even'
    else:
        return str[0]
    
names = ['anup','sam','ram']

for item in map(splicer,names):
    print(item)

#or present in list

print(list(map(splicer,names)))
