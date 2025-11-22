def square_list(arr):
    squares=[]
    for x in arr:
        squares.append(x*x)
    return squares

def multiples_of_k(arr,k):
    ans=[]
    for x in arr:
        if x%k==0:
            ans.append(x)
    return ans

arr=list(map(int,input().split()))
k=int(input())

sq = square_list(arr)
filtered = multiples_of_k(sq,k)

print(filtered)
