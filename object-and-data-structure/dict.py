#dictionaries in python
    # built-in data type that represent an unordered collection of key-value pairs.
    # key should be unique
    # defined using curly braces {} and key value paris are seprated by commas.
    # in python you can use single or double quotes or even no quotes in key (you can write like javascript object)

    # objects retrived by key name

my_dict = {'key1':'value1','key2':'value2'}

print(my_dict)
print(my_dict['key1']) #value1

print(my_dict.keys()) # all keys
print(my_dict.values()) # all values
items = my_dict.items() # getting a list of key value pairs as tuples
print('items',items) 

d = {
    'k1':123,
    'k2':[1,2,3,4],
    'k3':{
        'ik':100
    }
}

print(d['k1'])
print(d['k2'][3])
print(d['k3']['ik'])


# modifying values

my_dict['key1'] = 'new value'
print(my_dict)

# removing key value paris

del my_dict['key1'] # removing th ekey value pair with key "key1"

print(my_dict)

popped_value = my_dict.pop('key2') #removing and returing the values associate with "key2"

print(popped_value)
print(my_dict)