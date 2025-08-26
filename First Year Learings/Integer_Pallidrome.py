n = int(input("Enter a number to check if it is Pallidrome: "))


realdigit = n
reverse = 0

while n > 0:
    d = n % 10
    reverse = reverse * 10 + d
    n = n // 10


if realdigit == reverse:
    print(realdigit, "is a palindrome.")
else:
    print(realdigit, "is not a palindrome.")


