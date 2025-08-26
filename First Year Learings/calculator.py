a=int(input("Enter a number : "))
b=int(input("Enter another number:"))
c=input("Enter an operation: ")

if c=="+":
    print(a+b)

elif c=="-":
    print(a-b)

elif c=="/":
    print(a/b)

elif c=="*":
    print(a*b)

elif c=="//":
    print(a//b)

elif c=="%":
    print(a%b)

else:
    print("This operator is not valid")