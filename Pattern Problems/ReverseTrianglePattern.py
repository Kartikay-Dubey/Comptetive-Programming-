# N=int(input("Enter rows:"))
# for i in range(N,0,-1):
#     for j in range(0,i):
#         print("*",end=" ")
#     print()


n = int(input())
for i in range(n, 0, -1):
    for h in range(n-i):
        print (" ", end = "")
    for h in range(i):
        print ("*", end = " ")
    print ()


# n = int(input())
# for i in range(1,n+1):
#     for h in range(n-i):
#         print (" ", end = "")
#     for h in range(i):
#         print ("*", end = " ")
#     print ()