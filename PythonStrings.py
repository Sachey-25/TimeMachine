#Practice : Python Strings
#Tool : Pycharm Community Edition
#Platform : WINDOWS 10
#Author : Sachin A

#Script starts from here

'''statement="Programming is fun"
print(len(statement),'Is length of the string ')

arr="Python"
print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])
print(arr[5])


#string Sling is called travell within the string
#Denoting Start and end places ---> []
print(arr[0:6])
print(arr[1:6])
print(arr[1:6])
print(arr[5:5],"This is empty")
print(arr[6:1],"This is a test")

#Negative Indexing
print(arr[-7:-1],"This is Valid")
print(arr[-1:-6],'This is empty')'''

#String Methods
text="hello, welcome to string methods"
print(text.capitalize())
#It will turns lowercase letter to uppercase only starting letter
print(text.upper())
#It will turns all lowercase to uppercase
state="I BELONG TO KARNATAKA"
print(state.lower())
#it will tunrs all uppercase to lowercase

#Center () is used to allign the string where the programmer wants see the string
G=state.center(50)
H=state.center(60)
I=state.center(70)
J=state.center(80)
print(G)
print(H)
print(I)
print(J)

#Count ==> A specific charecter, How many times it repared
print(text.count('h'))

#find is used to check on a specific word or letter present in given index-string
print(text.find('welcome')) #i am not passing any parameter

#Split --> To separate on applied condition
fruit = "I like Strawberry"
print(fruit.split(' '))

print(text.casefold() ,"<----This is my First String") #---> Entire string
print(state.casefold(),"<----This is my Second String")
print(fruit.casefold(),"<----This is my Third String")

print(text.islower())
print(text.isalnum(),"<--- This is alphanumeric")
print(text.isdecimal())
print(text.isdigit())
print(text.isnumeric())
print(text.isprintable())


#Script ends here
#String slicing would preffred from low to high
