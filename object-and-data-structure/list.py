#lists
    #list is a built-in data type that represents an ordered , mutable collection of elements (diff data types)

my_list = [1,2,3,'apple','orange',True]

#accessing elements

print(my_list[0])
print(my_list)
print(my_list[2:5])

# we can also concate 2 diff list with + operator

another_list =['lets concate','this']

print('new concate',my_list + another_list)

#modifying elements

my_list[0] = 10 #modifying first element

my_list.append('banana') # adding an element to the end

my_list.extend([4,5,6]) #extending the list with another list

print('modified list',my_list)


#removing elements

my_list.remove(my_list[0]) # removing a specific element or you can also provide value in quotes or just provide index 

print('removed first element',my_list)

popped_element = my_list.pop() #remove and returing the last element

print('popped element ', popped_element)

#list operator
#len
print('length of string',len(my_list))

#sort
    # this method sort original list and doesnot return anything so you cant assign into variable (if you do its none type)
new_list = [1,2,31,3,4,5]
new_list.sort()
 #my_sorted_list = my_list.sort() # none type doesnt work like that 
my_sorted_list = new_list

print('my sorted list',my_sorted_list)
