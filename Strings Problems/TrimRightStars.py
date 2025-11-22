s=input()
i=len(s)-1
while i>=0 and s[i]=='*':
    i-=1

ans=""
for j in range(0,i+1):
    ans+=s[j]

print(ans)
