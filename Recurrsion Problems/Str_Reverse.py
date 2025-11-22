def reverse_str(s):
    if s=="":
        return ""
    return s[-1] + reverse_str(s[:-1])

s=input().strip()
print(reverse_str(s))
