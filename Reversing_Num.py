number = int(input("Enter a number to reverse its digits: "))
realdigit = number
reverse = 0

while number > 0:
    d = number % 10
    reverse = reverse * 10 + d
    number = number // 10

print("Reversed number:", reverse)
