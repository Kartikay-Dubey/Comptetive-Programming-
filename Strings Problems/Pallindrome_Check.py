t=int(input())
for _ in range(t):
    s=input()
    rev=""
    for ch in s:
        rev=ch+rev
    if rev==s:
        print(1)
    else:
        print(0)
