#Practice : Python Conditional Statements
#Tool : Pycharm Community Edition
#Platform : WINDOWS 10
#Author : Sachin A

#Script starts from here

'''We use keyword called if '''
#Number taken on runtime
'''number=int(input("Enter a number: "))
if(number%2==0): #Checking conditon whether devides by 2
    print(number, "Is Even")
#Global Statements
print("This statement doent belong to If")
print("Though the condition true/false, This will get prints")'''


'''number=int(input("Enter a number: "))
if(number%2==0): #Checking conditon whether devides by 2
    print(number, "Is Even")
#Global Statements
print("This statement doent belong to If")
print("Though the condition true/false, This will get prints")

#if else statement ---> Whereever true scenario if executes, on false else executes.
'''

'''#Number taken on runtime
number=int(input("Enter a number: "))
if(number%2==0): #Checking conditon whether devides by 2
    print(number, "Is Even")
    print("IF block")
else:
    print(number,"Is odd")
    print("ELSE Block")

#Global Statements
print("This statement doent belong to If")
print("Though the condition true/false, This will get prints")'''

#3. if elif else --> elif another conditiont to check
#Number Dynamically running
'''statement=input("Enter a Sentence: ")
demat=input("Enter another Sentence: ")
if(len(statement)!=len(demat)):
    print("Entered string are not equal in length")
elif(len(statement) > 15 and len(demat) > 15):
    print("Entered string are greater then 15 in lengh")
elif(statement=='Sachin' and demat=='Sachin'):
    print("Enter string as 'Sachin' ")
else:
    print("Else Block")
    print("Entered Strings are not satisfying any condition")'''

#Simple Calculator
value=1
while(value==1): #while loop infinite
    number_one=int(input("Enter a number: "))
    number_two=int(input("Enter another number: "))
    #What operation needs to be performed
    select=int(input("1.addition\n2.Substraction\n 3.Multiplication\n 4.Division\n"
                 "5.Modulous\n 6.Expoenential\n 7.Floor Divison\n"))
    if(select==1):
        print(number_one+number_two)
    elif(select==2):
        print(number_one-number_two)
    elif(select==3):
        print(number_one*number_two)
    elif(select==4):
        print(number_one/number_two)
    elif(select==5):
        print(number_one%number_two)
    elif(select==6):
        print(number_one**number_two)
    elif(select==7):
        print(number_one//number_two)
    else:
        print("Operation Invalid")



#Note: We got to know that if statement will execute only when
#the conditon holds true
