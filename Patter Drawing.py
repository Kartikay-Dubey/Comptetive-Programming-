"""

for a in range(1,11,2):
    for b in range(1,a,2):
        print(b,end=" ")
    print()


#Drawing pattern without nested loop

n=1
for a in range(6):
    print(n)
    n=n*10+1
#Drawing reverse pyramid

    for i in range(5):
        for a in range(5,i,-1):
            print(a,end=" ")
        else:
            print()
"""
#Random Patterns

rows=4
for i in range(1,rows+1):
    print(' '*(rows-i)+'*'*(2*i-1))



"""
def triangle(n):
    for i in range(1,n+1):
        for j in range(1,i+1):  
            print(j, end=" ")
        print()

triangle(8)
"""