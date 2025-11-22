s=input()
words=s.split()

rev=[]
i=len(words)-1
while i>=0:
    rev.append(words[i])
    i=i-1

print(" ".join(rev))
