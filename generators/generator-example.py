# def create_cubes(n):
#     result = []
#     for x in range(n):
#         result.append(x**3)
    
#     return result

# print(create_cubes(10))
# #notice 
# #[0, 1, 8, 27, 64, 125, 216, 343, 512, 729] entire output is keeping in memeory

# for x in create_cubes(10):
#     print(x) #one value at time




#----generator with yield-----------

#much more memeory efficient
# def create_cubes(n):
#     for x in range(n):
#         yield x**3


# for x in create_cubes(10):
#     print(x)



#another example

# def gen_fibon(n):

#     a=1
#     b=1
#     for x in range(n):
#         yield a #yielding them instead of storing them in list
#         a,b = b,a+b


# for number in gen_fibon(5):
#     print(number)



#-------next and iter function---

#next function tracks the prev value and return next value from generator
#iter function allow you to iterate thru objects(eg list)

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)


g = simple_gen()

print(g) # g is generator object

print(next(g)) #output 0
print(next(g)) #output 1



s='hello'

for letter in s:
    print(letter)

#next(s) #output error 'str' object is not an iterator

s_iter = iter(s) #iter make iterable object to iterator so now we can use next


print(next(s_iter)) #output h


#note

"""
generator comprehension is like list comprehension but we use () bracket
"""