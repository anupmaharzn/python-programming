# lambda expression is a way to create anonymous function aka lambda functions.
# these fucntions are defined using he `lambda` keyword


"""
synatx

lambda arguments:expression

note: they can take any numbers of arguments but can only have on expression

"""

#example

add_numbers = lambda x,y: x+y

result = add_numbers(1,1)

print(result)

#Using map with lambda

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#using filter with lambda

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

#using reduce with lambda

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

