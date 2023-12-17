# reduce function in python is part of the `functools` module
# and used for performing a cumulative computation on a list
"""
functools.reduce(function,iterable[,initializer])
initailizer is optional

"""
from functools import reduce
#its like accumulater * currentvalue
def multiply(x,y):
    return x *y 

num=[1,2,3,4,5]

inital_product = 10

product_with_initalizer = reduce(multiply,num,inital_product)
print(product_with_initalizer)