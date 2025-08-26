
number = int(input("Enter a number to find the sum of its digits: "))

digit_sum = 0
for digit in str(number):
    digit_sum = digit_sum + int(digit)

print("Sum of digits:", digit_sum)
