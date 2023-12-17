# class Sample():
#     pass
# my_sample = Sample()
# print(type(my_sample))
# #output <class '__main__.Sample'>


"""
 __init__  method is a special method, also known as a constructor.
It is automatically called when an object of a class is created.
#In javascript , constructor vanyira keyword nai hunxa
"""

"""
self is a convention used to represent the instance of the class
self is the first parameter in the method definition of instance method, including the `__init__` method.
#imp when a mehtod is called on an instance,the instance itself is passed as the first agrument to the method.

obj = MyClass()
obj.my_method("Hello", "World")

self: <__main__.MyClass object at 0x...>
arg1: Hello
arg2: World

"""

# class and attributes

# class Dog():

#     # attributes 
#     # we take in the argument
#     # assign it using self.attribute_name
#     def __init__(self,mybreed,name,spots):
#         self.breed = mybreed # this is instance attribute
#         self.name = name
#         #expect boolean
#         self.spots = spots

# my_dog = Dog(mybreed='Lab',name='sam',spots=True)

# print(type(my_dog)) #output <class '__main__.Dog'>

# print(my_dog.breed) #Lab
# print(my_dog.name) #sam
# print(my_dog.spots) #True

#------------- class object attribute aka class attribute and methods------------

# class attributes

# class attributes are shared by all instance of class.

# they are defined outside the `__init__` method,usually at the top of the class.

# class Car:

#     wheels = 4 #class attribute

#     def __init__(self,make,model,year):
#         self.make = make #instance attribute
#         self.model = model
#         self.year = year


# #create instance of the car class

# car1 = Car("Toyota", "Camry", 2022)
# car2 = Car("Honda", "Accord", 2023)

# print(car1.wheels) #output:4
# print(car2.wheels) #output:4



#-----methods-----#

#methods in class are functions that are defined within the class and operate on instance of that class.

# these methods can perform various actions and interact with the attribute of the class.

## There are two main types of methods in a class:
    #1 instance methods
    #2 class methods

#instance method

# class Car:

#     wheels =4 #class attribute

#     def __init__(self,make,model):

#         self.make = make #instance attribute
#         self.model = model
#         self.speed = 0 

#     #instance method
#     def accelerate(self,increment):
#         self.speed = self.speed + increment
    
#     def brake(self,decrement):
#         self.speed -=decrement
#         if self.speed < 0:
#             self.speed = 0
    
#     def info(self):
#         print(f"name of car {self.make} and model is {self.model} and has {Car.wheels} wheels")


# #creating an instance of the car

# my_car = Car('toyota','camry')

# my_car.accelerate(20)

# print(my_car.speed)

# my_car.brake(5)

# print(my_car.speed)

# my_car.info()


#class method and static method

#--class method
# class method is defined using @classmethod decorator

# the first parameter is conventionally named  `cls` and refers to the class ifself

# can access and modify class-level attribute

#--static method

#defined using th `@staticmethod` decorator

#no special first parameter like `self` or `cls`.

#it doesnt have access to instance or class level attributes

#note both class and static method doesnt need to create object to access it

class MathOperations:

    #class level attribute
    pi = 3.14159

    def __init__(self,radius):
        self.radius = radius #instance level attribute
    
    #class method 
    @classmethod
    def set_pi(cls,new_pi):
        cls.pi = new_pi
    
    #instance method
    def calculate_area(self):
        return self.pi * self.radius**2
    
    # static method to add two number

    @staticmethod
    def add_numbers(x,y):
        return x+y
    

#creating an instance of mathoperations

circle = MathOperations(radius=5)

#accessing instanc method to calculate area
area = circle.calculate_area()

print(f"area of the circle:{area}")

#acessing class method to set a new value for pi
MathOperations.set_pi(3.14)

area_with_updated_pi = circle.calculate_area()
print(f"Area with updated pi: {area_with_updated_pi}")

#accessing static method to add number

sum_result = MathOperations.add_numbers(10,20)

print(f"sum of two numbers: {sum_result}")