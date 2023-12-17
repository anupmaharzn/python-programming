# strings are sequence of characters
# its is an array basically (--in python we can say list) but only diff is list is mutable where as string is not
#single or double quotes

my_string = "hello, world"

print(my_string)
print(my_string[3])

# indexing and slicing with strings

#reverse indexing
    #revers indexing starts with -1 and -2 so on

print('last character of string',my_string[-1])
print('last to first',my_string[-12])


#slicing
    #substring
    #does not include stop index value
# [start:stop:step]
print(my_string[2:])
print(my_string[:4])
print(my_string[1:4])
print(my_string[3:10:2])
print('reverse the string',my_string[::-1]) # by default step size is 1



#--------------------------------------------------------------------------------------#

#---------------string properties and methods------------------------------------------#

name = 'anup'

last_letters = name[1:]

#string concate
print('A' + last_letters)

#string methods doesnot affect original string
# if you want you can reassign

new_up = name.upper()
print(name) #--original lower case
print(new_up) #--upper case

#split
    # Returns a list of substrings separated by the specified separator 
    #by default white space
greet = 'hello world'
print('split method',greet.split('o'))

#note there are a lot of string methods as well


#----------------------------------string formatter for print--------------------------------------------------------#


#using % operator (old style)

name = 'john'
age = 25

print('my name is %s and i am %d years old' % (name,age))

#using str.format() method
    # this method allows you to create formatted string by replacing placeholder with values

print('my name is {} and i am {} years old.'.format(name,age))

#or you can also provide index

print('my name is {0} and i am {1} years old.'.format(name,age))


#using f strings(python 3.6 and newer)
    #you can include expersion inside curly braces
print(f"my name is {name} and i am {age} years old");