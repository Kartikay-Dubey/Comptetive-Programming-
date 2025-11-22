s=input()
t=int(input())

pos=-1
for i in range(len(s)):
    if ord(s[i])==t:
        pos=i
        break

print(pos)
