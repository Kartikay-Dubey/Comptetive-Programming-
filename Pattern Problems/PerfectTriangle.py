N=int(input("Enter rows:"))
for i in range(N):
    for j in range(N-I-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()