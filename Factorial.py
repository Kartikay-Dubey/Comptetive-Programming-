import math


num = int(input("Enter a number: "))

fact = 1 
for i in range(1, num + 1):
    fact = fact/i

print("Factorial of", num , "is", fact)


"""
#CHECKING FACTORIAL :-

n=162
lst=[]

for i in range(1,n+1):
    if n%i==0:
        lst.append(i)

if not lst:
    print('Prime')
else:
    print('Not Prime')
    print('Factors of the Given num is: ',lst)

"""
