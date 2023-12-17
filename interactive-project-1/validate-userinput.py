some_value = '1000'


print(some_value.isdigit())

# if true then we can type conversion

print(int(some_value))



# example

def user_choice():
    
    choice = 'wrong'
    acceptable_range = range(0,10)
    within_range = False
    while choice.isdigit() == False or within_range == False:
        choice = input('Enter the number 0-10')
        # digit check
        if choice.isdigit() == False:
            print('please enter the digit!')
        # range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print('please enter the value within range !')
                within_range = False

    return int(choice)

user_choice()