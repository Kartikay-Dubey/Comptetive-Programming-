N=int(input("Enter a number to find its factors: "))
count = 1
while count<=N:
    if (N%count==0):
        print(count)
        count=count+1


