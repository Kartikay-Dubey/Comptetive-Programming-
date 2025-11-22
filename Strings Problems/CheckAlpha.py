t=int(input())
v="aeiouAEIOU"

for _ in range(t):
    s=input().strip()
    vc=cc=0
    for ch in s:
        if ch.isalpha():
            if ch in v: vc+=1
            else: cc+=1
    print(vc,cc)
