def is_pal(s, i, j):
    if i>=j:
        return True
    if s[i]!=s[j]:
        return False
    return is_pal(s, i+1, j-1)

s=input().strip()
if is_pal(s,0,len(s)-1):
    print("Palindrome")
else:
    print("Not Palindrome")
