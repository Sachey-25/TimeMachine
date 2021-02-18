#Practice : Python Loops
#Tool : Pycharm Community Edition
#Platform : WINDOWS 10
#Author : Sachin A

#Script starts from here
#For Loop
#while Loop
sentence="We are learning PythonLoops"
for i in sentence:
    print(i,end='')
print()

#[] ==> denoted into these square brackets are called lists (Data Structure)

'''numbers=[2,3,4,7,8,9]
print(type(numbers))
for i in numbers:
    if(i%2==0):
        print(i,"Is even ")
    else:
        print(i,"Is odd ")
#range()
for i in range(0,10):
    print(i,end='')

print("\nEven numbers from 1 to 10 are :")
for i in range(0,10,2):
    print(i)

print("\nOdd numbers from 1 to 10 are :")
for i in range(1,10,2):
    #count=count-1
    print(i)

#2. While loop
#Data stored to 0 to start a count
count=0
while(count<9): #Condition needs to check till becomes false
    print("The value of i", count)
    count=count+1 #Updating the count/iteration
print("We are Idiots")
print("Sachin is Intelligent")


print("Decending Order")
for i in range(10,1,-1):
    print(i, end=' ')'''

#While loop for unlimited time of execuition until user intrupts

variable=1
while(variable==1):
    number=int(input("\nEnter a number: "))
    print("You have entered :", number)
print("Good Bye")



#Script ends here
