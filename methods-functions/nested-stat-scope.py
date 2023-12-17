#nested statement and scope in function


"""
LEGB refers to the order in which python looks for names(idenifiers) in a program.
it represnets the scope resolution order in python.

"""

global_variable = 'i am global'

def outer_function():

    #enclosing scope

    enclosing_variable = 'I am enclosing'

    def inner_function():

        #local scope

        local_variable = "I am local"

        print(local_variable)
        print(enclosing_variable)
        print(global_variable)
    
    inner_function()

outer_function()








x=50

def func():
    global x
    print(f'x is {x}')

    # local reassignment on a global variable

    x= 'New value'
    print(f'I just locally changed global x to {x}')


print(x)

func()
print(x)
