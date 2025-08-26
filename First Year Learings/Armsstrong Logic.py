n=(int(input("Enter A Number to Check: ")))
sum=0
order=len(str(n))
copy_x=n

while (n>0):
    digit=n%10
    sum=sum+digit**order
    n=n//10

if sum==copy_x:
    print(copy_x, " is an Armstrong Number!")
else:
    print(copy_x,"is Not an Armstrong Number!")