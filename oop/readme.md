# objest oriented programming allows programmers to create their own objects that have methods and attributes.

# these methods act as functions that use information about the object,as well as the object itself to return results, or change the current object.

# oop allows users to create their own objects.

# oop allows us to create code that is repeatable and organized.

# for much larger scripts of python code, function by themselves arent enought for organization and repeatablilty.

-syntax

class NameofClass():

    def __init__(self,param1,param2):
    self.param1 = param1
    self.param2 = param2

    def some_method(self):
        #perform some action
        print(self.param1)
