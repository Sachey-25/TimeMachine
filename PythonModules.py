#Practice : Python Module
#Tool : Pycharm Community Edition
#Platform : WINDOWS 10
#Author : Sachin A

#Script starts from here
import os
print(os.name)
print(os.path)
#Present Working Directory

os.chdir('C:\\Users\\Coding-Machine\\Programmingwithsachin')
print("Current Working directory is chagnged successfully")
print(os.getcwd())

print(os.access('hellogit.html',os.R_OK),"File has read access")
print(os.access('hellogit.html',os.W_OK),"File has write access")
print(os.access('hellogit.html',os.X_OK),"File has executable access")
print(os.access('hellogit.html',os.F_OK),"File found successfully")

#Chflags(path,flags)

'''chflags() sets path flags to the numeric flags, These flags may take
a combination (bitwise OR)

os.UF_DUMP --> Dont dump a file
os.UF_IMMUTABLE -- You may not change a file
os.UF_APPEND --> You may only append to the file
os.UF_NOUNLINK-You may not rename or delete the file.'''

#To create new directory
#os.mkdir('DataScience')
print(os.getcwd())
print("Directory created successfully")

#Multiple Directories
#os.makedirs('DataScience\PythonScripting\OSModule')
print("Another Directory created successfully")

#Rename the directory
#os.rename('DataScience\PythonScripting\OSModule','OS-Module')
print("Directory renamed successfully")

#remove the directory
#os.remove('DataScience\PythonScripting')
#print(os.chroot('C:\\Users\\Coding-Machine\\Programmingwithsachin'))

'''Chroot()
---> Chroot Which alters the current process of root directory to the given path'''

os.rmdir('C:\\Users\\Coding-Machine\\Programmingwithsachin\\OS-Module')
print("Derectory removed successfully")



#script here here
