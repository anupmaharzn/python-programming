# methods are simple a functions that are built into objects

#Functions are independent blocks of code that can be called from anywhere, while methods are tied to objects or classes and need an object or class instance to be invoked.

# A method definition always includes ‘self’ as its first parameter.


# let's explore #

    # built-in objects in python have a variety of methods you can use


mylist = [12,3,4]

print(type(mylist))
mylist.append('new elements')
print(mylist)
mylist.pop()
print(mylist)

mylist.insert