# In python `*args` and `**kwargs` are used in function definations to allow a variable number of arguments

# args = arguments
# kwargs = keyword arguments

# args and kwargs is simliar to the concept of the rest parameter operation

"""
*args collects additional positional arguments into a tuple.
**kwargs collects additional keyword arguments into a dictionary.
"""
#args can be any name you want to write 



def myfunc(*args):
    print(args) #tuple
    for item in args:
        print(item)

myfunc(2,3,4,52,35,2)


def examplefunc(**kwargs):
    print(kwargs) #dictionary

    for key,value in kwargs.items():
        print(f'{key}:{value}')

examplefunc(k1=1,k2=2,k3=3)



def anotherfunc(**kwargs):

    if 'name' in kwargs:
        print('dict has name of {}'.format(kwargs['name']))
    else:
        print('dict doesnot have name in it')


anotherfunc(name='anup',age=25)


def newfunc (*args,**kwargs):
    print('i would like {} {}'.format(args[0],kwargs['food']))


newfunc(10,20,30,food='peas')