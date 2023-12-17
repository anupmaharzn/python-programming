# lis compreshensions are a unique way of quickly creating a list with python

# if you find yourself using a for loop alog with .append() to create a list,List compreshensions are a good alternative


mystr = 'hello'

mylist = []

for letter in mystr:
    mylist.append(letter)


print(mylist)

#shorter form

shortlist = [letter for letter in mystr]

print(shortlist)

powlist = [num**2 for num in range(0,11)]

print(powlist)


divby2 = [x for x in range(0,11) if x%2==0]
print(divby2)


celcius = [0,10,20,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celcius] 

print(fahrenheit);