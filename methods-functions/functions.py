# creating clean repeatable code is a key part of becoming an effective programmer
# functions allow us to create blocks of code that can be easily executed many times , without needing to constantly rewrite the enter block of code.

#-----------------------------------------------#

#creating a function requires a very specific syntax ,including the 

    #def keyword
    #correct indentation and proper structure
    #for naming convention use snake casing (lowercase) with underscore betweenwords

"""
--syntax--

def name_of_function(param1,param2,...):

    #Docstring explains function

    return value; # optional return allows us to aassign the output of the function to a new variable.

"""

#simple example

def add_num(n1,n2):
    return n1 + n2

result = add_num(1,1)

print(result)


#-----------------------------------------------------------------------------------
#default value in parameter simple
def greet(name='default'):
    print(f'hello {name}')

print(greet())

def check_even_list(num_list):
    # RETURN ALL THE EVEN NUMBERS IN A LIST

    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass # dont do anything

    return even_numbers


print(check_even_list([1,2,5]))


#-------------------------------------------------------------------------------------

# tuple unpacking with functions

stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]

print(len(stock_prices))
print(stock_prices[0])

for item in stock_prices:
    print(item)

for ticker,price in stock_prices:
    print(ticker)
    print(price+(0.1*price))


work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):

    current_max = 0
    employee_of_month = ''

    for employee,hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass
    #return's in tuple form
    return employee_of_month,current_max

name,hours = employee_check(work_hours)

print(name,hours)


#------------interaction between functions in python---------------

#typically a python script or notebook contains several functions interacting with each other

#let's create a few functions to mimic the carnival gussing game 'Three Cup Monte'

from random import shuffle



def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess=''
    while guess not in ['0','1','2']:
        guess = input('Pick a number: 0,1 or 2: ')
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('correct!')
    else:
        print('wrong guess!')
        print(mylist)


#inital list
mylist = [' ','O',' ']
#suffle list
mixedup_list = shuffle_list(mylist)
#user guess
guess = player_guess()
#check guess
check_guess(mixedup_list,guess)


