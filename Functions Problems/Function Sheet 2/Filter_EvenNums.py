def filter_even():
    arr=list(map(int,input().split()))
    output=[]
    for x in arr:
        if x%2==0:
            output.append(x)
    print(output)

filter_even()
