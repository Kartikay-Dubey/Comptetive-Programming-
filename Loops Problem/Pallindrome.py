n=int(input("Enter a number"))

real=n
reverse=0

while n>0:
    d=n%10
    reverse=reverse*10+d
    n=n//10


if real==reverse:
    print("is a palindrome")
else:
    print("not a palindrome")