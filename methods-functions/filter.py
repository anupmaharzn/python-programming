#filter is python's another built in function that is used to filter elements of an iterable based on specified function.
#it returns an iterator containing only the elements for which the function returns `true`


def checkadult(age):
    return age >= 18

age=[32,22,11,45]

for i in filter(checkadult,age):
    print(i)

#or convert into list

print(list(filter(checkadult,age)))