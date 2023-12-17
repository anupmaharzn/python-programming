
# # def hello():
# #     return 1


# # greet = hello #function is an object that can be passed into other objects

# # print(greet())

# # del hello

# # # print(hello())

# # print(greet()) # greet is still pointing to the hello function

#-------------example of returning a function----------------#

# # # def hello(name='anup'):
# # #     print('the helo() function has been executed')

# # #     def greet():
# # #         return '\t this is the greet() func inside hello'
    
# # #     def welcome():
# # #         return '\t this is welcome() func inside hello'
    
# # #     print('i am going to return a function')

# # #     if name == 'anup':
# # #         return greet
# # #     else:
# # #         return welcome
# # # # print(welcome()) there scope is limited to hello function

# # # my_new_func = hello('anup')
# # # #output
# # # # the helo() function has been executed
# # # # i am going to return a function

# # # print(my_new_func)

# # # #output
# # # #<function hello.<locals>.greet at 0x00000130043554E0>

# # # print(my_new_func()) # now we are accessing the greet function using this assignement

# # # #output
# # # #this is the greet() func inside hello

#-------passing function as argument to another function---


# # # def hello():
# # #     return 'Hi jose'

# # # def other(some_def_func):
# # #     print('other code runs here!')
# # #     print(some_def_func())

# # # other(hello)

#---------------------------Decorator----------------------------------------------------------#

def new_decorator(original_func):
    
    def wrap_func():

        print('some extra code , before the original function')

        original_func()

        print('some extra code after original function!')

    return wrap_func


# def func_needs_decorator():
#     print('i want to be decorated!!')

# decorated_func = new_decorator(func_needs_decorator)

# print(decorated_func())


#----shortcut---
@new_decorator
def func_needs_decorator():
    print('i want to be decorated!!')

func_needs_decorator()