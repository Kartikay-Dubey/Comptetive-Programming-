
"""
#Pyramid Pattern
num=int(input("Enter the numbers of Rows:"))
for i in range (0,num):   
    for j in range (0,num-i-1):  #to create spaces in each row!
        print(end=" ")
    for j in range (0,i+1):       #to create star pattern in each row!
        print("*", end=" ")
    print()

"""

"""
#InversE Pyramid
num=int(input("Enter the numbers of Rows: "))
for i in range (num,0,-1):
    for j in range (0,num-i):
        print(end=" ")
    for j in range (0,i):
        print("*", end=" ")
    print()
"""

"""
#Armstrong Number
num=int(input("Enter the number: "))
x=num
order=len(str(num))
result=0

while num>0:
    digit=num%10
    result=result+digit**order
    num=num//10

if result==x:
    print("Yes")
else:
    print("No")

"""


"""
#Fibonacci Series
n=int(input("Enter the Number: "))
a=0
b=1

for i in range (n):
    print(a,end=" ")
    temp=a
    a=b
    b=temp+b
"""
"""
#LCM 

n1=15 
n2=25
big=n1 if n1>n2 else n2

while True:
    if big%n1==0 and big%n2==0:
        print("LCM is:",big )
        break
    big=big+1
"""

"""
#Prime Number
n=int(input("Enter a Number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not a PN!")
            break
    else:
        print("Yes a PN!")
else:
    print("Not a PN!")

    
"""

"""
#Leap Year
a=int(input("Enter a Year: "))

if a%4==0:
    if a%100==0:
        if a%400==0:
            print("Yes a LP!")
        else:
            print("No not a LP!")
    else:
        print("Yes a LP!")
else:
    ("No not a LP!")

"""

string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print("Number of vowels:", count)