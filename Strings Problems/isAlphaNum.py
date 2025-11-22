s=input()
flag=1

for ch in s:
    if not(ch.isdigit() or ch.isalpha()):
        flag=0
        break

print(flag)
