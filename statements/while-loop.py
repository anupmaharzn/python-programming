# while loops will continue to execute a block of code while some condition remains true

#syntax
"""
while condition:
    #do something

"""

#simple example

count = 1 

while count <=5:
    print(count)
    count +=1


#break continue pass

"""
break : breaks out of the current closest enclosing loop.
continue : goes to the top of the closest enclosing loop.
pass : Does nothing at all

"""
mystring = 'mommy'

for letter in mystring:
    if letter == 'o':
        continue
    print(letter)


x=0
while x < 5:
    if x==2:
        break
    print(x)
    x += 1