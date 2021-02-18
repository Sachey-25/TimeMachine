#Practice : Python Operators
#Tool : Pycharm Community Edition
#Platform : WINDOWS 10
#Author : Sachin A

#Script starts here

'''#Arithamtic Operators in python
#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print("Additon of entered number is :" , number_third+number_fourth)

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Substration process
print("Substration of entered number is :" , number_third-number_fourth)

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Multiplication process
print("Multiplication of entered number is :" , number_third*number_fourth)

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Divison process
print("Divison of entered number is :" , number_third/number_fourth)

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Exponential process
print("Exponential of entered number is :" , number_third**number_fourth)

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Floor Division process
print("Floor Division of entered number is :" , number_third//number_fourth)

#Comparison Operator --> Returns result in boolean type : true / False'''
'''#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print(number_third == number_fourth,"Because numbers are equal")

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print(number_third != number_fourth,"Because numbers are not equal")

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print(number_third < number_fourth,"Because number_third is less then number_fourth")


#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print(number_third > number_fourth,"Because number_third is greater then number_fourth")

#First number
number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print(number_third <= number_fourth,"Because number_third is less then equal")

number_third=int(input("Enter a number: "))
#Second Number
number_fourth=int(input("Enter another number: "))
#Addition process
print(number_third >= number_fourth,"Because number_third is greater then equal")'''

'''#Logical Operator
statement = "ProgrammingIsFun"
statement_two="ProgrammingIsFun_SecondSentence"
print(not statement)
print(not statement_two)

#Combination of not operator and And operator
print(not statement and statement_two)
#Combination of not operator and OR operator
print(not statement or statement_two)

#True Scenario And Operator
print(statement and statement_two, "This is and operator")
print(statement_two and statement, "This is and operator")

print(statement < statement_two and statement != statement_two)

print(len(statement_two),"Length of the second statement")
print(len(statement,),"Length of the first statement")
print("------------------------------------------------------------")
#True Scenarios of OR Operator
print(statement == statement_two or statement < statement_two)

print("*****************************************************")
#False Scenarion
print(statement == statement_two and statement > statement_two)
print(statement == statement_two or statement > statement_two)'''

#Find Odd or Even using only arithamtic operator , comparision and logical

number=9
print(number is int)
print(number%2==0 and not number%2==1,"It is a Even Number")
print(number%2==0 or number%2==0, "It is a Even number")

city="Bangalore"
print(type(city) is str ,"This is a output from type()" )#true
print(type(city) is str ,"String as a Bangalore") #false
#reason why is we are not specifying type as same as pvm
#type() ---> results into datatype of the variable declared.
print('*'*50)
number=9
print(type(number))

print('*'*50)
number=100
print(type(number) is int)
print(type(number) is not int)

print(type(number) is str)
print(type(number) is not str)

print("----------------------------")
#Membership Operator
Demat = "Programming"
print(Demat[0] in Demat,Demat[0])
print(Demat[0] not in Demat,Demat[0])
#No Concept of Arrays in python, However String are array representation
print('Program' in Demat)
print('program' not in Demat)

#Note : In day today programming membership especially 'in' operator
#used in python for loop

'''for i in Demat:
    print(i)'''
#in="Sachin"
#Script ends here
