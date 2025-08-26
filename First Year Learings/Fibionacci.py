n = int(input("Enter the number of terms: "))
a = 0
b = 1

print("Fibonacci Series for the number,",n,":-", )
for i in range(n):
    print(a, end=" ")
    temp = a
    a = b
    b = temp + b

