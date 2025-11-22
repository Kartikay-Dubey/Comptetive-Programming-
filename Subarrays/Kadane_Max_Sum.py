n=int(input())
a=list(map(int,input().split()))

best=a[0]
curr=a[0]

for x in a[1:]:
    curr=max(x,curr+x)
    best=max(best,curr)

print(best)
