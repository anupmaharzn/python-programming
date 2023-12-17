
#opening and closing files

 # file object = open(file_name [, access_mode][, buffering])

# open a file
fo  = open('newfile.txt',"wb")

print ("name of the file:",fo.name);
print ('closed or not:',fo.closed);
print ('opening mode:',fo.mode);

#close opened file
fo.close()


#-----write------#

fo = open("newfile.txt", "w")
fo.write( "Python is a great language.\nYeah its great!!\n")

fo.close()


#----read----#

with open('newfile.txt','r+') as fo:
    str = fo.read()
    print('read string is:',str)

print('closed or not?',fo.closed);

# we can also rename or deleting file using OS module in python
# we can also operation with files and directory using it's related methods