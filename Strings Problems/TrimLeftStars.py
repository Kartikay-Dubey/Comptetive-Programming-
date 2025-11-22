s=input()
i=0
while i<len(s) and s[i]=='*':
    i+=1

ans=""
for j in range(i,len(s)):
    ans+=s[j]

print(ans)
