# a regular expression is a sequence of characters that define a search pattern.
#mainly for use in pattern matching with strings or string matching

# we already know we can search for substring with a larger string with the `in` opoerator

print('dog' in 'mydogisgreat') #output True

# this has severe limitation,we need to know the exact string and need to perform additional operation to account for capitalization and punctutation

#regular expression(regex) allow us to search for general patterns in text data!


#import re in python to import built in regex

"""
import re

re.match(pattern,string) # match only at the begining of string

re.search(pattern,string) # searches for match anywhere of string

re.findall(pattern,string) #return list of all occerance

for match in re.finditer(pattern,string) #returns an iterator over all non-overlapping matches

pattern = re.compile(r'pattern') #to create a regular expression object,which can be reused for multiple searches:
r'write_your_pattern'

"""




text = "the agent's phone number is 408-555-1234. call soon!"

print('phone' in text) #output True

import re

# pattern = 'phone'

# print(re.search(pattern,text)) #ouput re.Match object; span=(12, 17), match='phone'


# pattern1 = 'not in text'

# print(re.search(pattern1,text)) #None


# match = re.search(pattern,text)

# print(match.start()) #start index
# print(match.end())  #end index


# match2 = re.findall(pattern,text)

# print(match2) #['phone']


# for match in re.finditer(pattern,text):
#     #return match objects
#     print(match) #re.Match object; span=(12, 17), match='phone'
#     print(match.span())  #(12,17)
#     print(match.group()) #phone
#
#---------------------------------------------------------------------------------------------------#


phone = re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)

print(phone.group()) #408-555-1234 found this match

phone1 = re.search(r'\d{3}-\d{3}-\d{4}',text)

phone_pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})') #in this example complies group of 1,2,3 these into r'\d{3}-\d{3}-\d{4}'

results = re.search(phone_pattern,text)

print(results.group())
print(results.group(1)) #408
#print(results.group(4)) # no such group

#---------------------------------------------------------------------------------------

print(re.findall(r'...at','the cat in the hat went splat'))

print(re.findall(r'^\d','1 is a number'))

print(re.findall(r'\d$','the number is 2'))


test_phrase = 'this is a string! but it has punctuation.how can we remove it?'

print(re.findall(r'[^!.? ]+',test_phrase))

clean = re.findall(r'[^.!? ]+',test_phrase)

pfinal = ' '.join(clean)

print(pfinal)



