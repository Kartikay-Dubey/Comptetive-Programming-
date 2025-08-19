a=int(input("Enter the first number : "))
b= int(input("Enter the second number : "))
c= int(input("Enter the third number : "))

if a<b and  a<c:
    print("The minimum number is : ", a)
elif b<c:
    print("The minimum number is : ", b)
else :
    print("The minimum number is : ", c)


