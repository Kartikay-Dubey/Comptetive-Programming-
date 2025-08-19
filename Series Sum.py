import math

def calculate_series(num):
    x=0
    for i in range(1, num+1):
        term=i/math.factorial(i)
        if i%2==0:
            x=x-term
        else:
            x=x+term
    return x



num = int(input("Enter a number: "))
result=calculate_series(num)

print(result)