# Input two numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print("Before swapping: a=",a "and b=", b)

# Swapping without a third variable
a = a + b  # Step 1: Add both numbers
b = a - b  # Step 2: Subtract the second number from the sum to get the first number
a = a - b  # Step 3: Subtract the updated second number from the sum to get the second number

print("After swapping: a =",a "b=",b)
