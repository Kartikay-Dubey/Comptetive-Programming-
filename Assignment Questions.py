
"""
#For Decreasing Pattern

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
"""
# #For increasing Pattern

# for i in range(0,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()


# #For getting number of vowels in a string

# str=input("ENTER YOUR STRING: ")
# vowels="aeiouAEIOU"
# count=0

# for chr in str():
#     if chr in vowels():
#     count=count+1
# print(count)

#Tuple Functions

# tup=(1,2,2,2,5,6)
# print(len(tup))
# print(min(tup))
# print(max(tup))
# print(tup.count(2))
# print(tup.index(2))

a = 5       # Binary: 0101
b = 3       # Binary: 0011

result = a | b   # 0101 | 0011 -> 0111
print(result)    # Output: 7
