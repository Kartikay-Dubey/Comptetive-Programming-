s=input()
s=s+s

step1=""
for ch in s:
    if not('A'<=ch<='Z'):
        step1+=ch

final=""
vowels="aeiou"
for ch in step1:
    if ch in vowels:
        final+='#'
    else:
        final+=ch

print(final)
