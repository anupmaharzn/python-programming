#special methods in python are also known as dunder methods,short from double underscore

"""
__init__(self,...) 
this method is called when an instance of the class is created

__str__(self)
this method is called when the str() fucntion or print() function is used on an object.
it should return human readable string representation of the object.


__len__(self)
this method is called when he len() function is used on an object.
it should return the length of the object.
"""


class Book():
    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author} "
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print('a book object has been deleted')

b = Book('python','joe',200)

#so if we use print or str function in objects __str__(self) method is called 
print(b)
str(b)

#so if we use len() function in object __len__(self) method is called
len(b)

del b #delete the variable from memory

print(b)