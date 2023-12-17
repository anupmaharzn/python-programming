#python os module and shutil allow us to easliy navigate files and directories on the computer and then perform actions on them.

f = open('practice.txt','w+')

f.write('this is a test string')

f.close()


import os

cwd = os.getcwd()
lst_dir = os.listdir()
print(cwd)
print('list of directories',lst_dir)



list_dir = os.listdir('C:\\users')

print(list_dir)


import shutil

# shutil.move('practice.txt','C:\\Users\\helle\\Desktop\\')

# shutil.move('C:\\Users\\helle\\Desktop\\practice.txt','C:\\Users\\helle\\Desktop\\python-basic\\advance-modules')



#deleting files

#os.unlink(path) which deletes a file at the path you provide
#os.rmdir(path) which deletes a folder (folder must be empty) at the path you provide
#shutil.rmtree(path) this is most dangerous,as it will remove all files and folder contained in the path.(can not be reversed)



# import send2trash

# send2trash.send2trash('practice.txt')






