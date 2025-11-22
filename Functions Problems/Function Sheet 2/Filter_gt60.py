def greater_than_60():
    arr=list(map(int,input().split()))
    ans=[]
    for x in arr:
        if x>60:
            ans.append(x)
    print(ans)

greater_than_60()
