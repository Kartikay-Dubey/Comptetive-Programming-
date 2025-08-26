
"""
# Input
year = int(input("Enter a year: "))

# Check for leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
"""


x=int(input("Enter the Year: "))
if x%4==0:
    if x%100==0:
            if x%400:
                 print("Yes!")
            else:
                print("No!")
    else:
         print("Yes!")
else:
     print("No!")