# inheritance is a mechanism that allows a new class(subclass/derived class) to inherit attributes and methods from an existing class(base class/parent class)

#this promotes code reusebility and helps in creating a hierarchy of classes

#types of inheritanc in python

 #single inheritance
 #multiple inheritance (inherits from more than one base class)
 #multilevel inheritance 
 #hierarchical inheritance

# access modifiers in pythons
    #in python there are no strict modifiers like in some other programming langauage(eg java)
    #however there are conventions for inicating the visibility fo attributes and methods

    #public
    #-members are accessible from outside the class (by default)

    #protected
    #-members can be accessed in derived classes
    # we use `_` symbol in front of attributes and methods
    #example
"""
    class MyClass:
    _protected_variable = 20

    def _protected_method(self):
        pass
    """

    #private
    #-members should not be accessed from outside the class
    # we use `__` symbol in front of variable(attributes) and method names

 #note encapsualtion is achived thru access modifiers

#parent class
class Animal():

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('i am an animal')

    def eat(self):
        print('i am eating')
 
#child class
class Dog(Animal):

    def __init__(self):

        Animal.__init__(self)

        print('Dog created')
    #function overriding
    def who_am_i(self):
        print('i am dog')

    def bark(self):
        print('Woof!')

#instance
mydog = Dog()

mydog.who_am_i()
mydog.bark()



#polymorphism

#refers to the ability of taking different form

#compile-time polymorphism (method overloading)
#runtime polymorphism (method overriding)

#method overloading

class Mathoperations:
    def __init__(self) -> None:
        pass

    def add(self,a,b):
        return a+b
    #this add method overloads the above add method
    def add(self,a,b,c):
        return a+b+c
    
calculator_obj = Mathoperations()
# However, Python doesn't support traditional method overloading directly.
result1 = calculator_obj.add(a=2,b=3,c=3)
result2 = calculator_obj.add(a=1,b=2,c=3)

print(result1)
print(result2)


#method overriding

class Animal:

    def __init__(self,name):
        self.name = name
    def speak(self):
        raise NotImplementedError('subclass must implement this abstract method')

class Dog(Animal):
    #override parent method
    def speak(self):
        return self.name + " Dog barks" #simple attribute of parent class

class Cat(Animal):
    #override parent method
    def speak(self):
        return self.name + " Cat meows"

# Create instances
dog_instance = Dog('fido')
cat_instance = Cat('isis')

# Call overridden methods
print(dog_instance.speak())  # Output: Dog barks
print(cat_instance.speak())  # Output: Cat meows
