"""a=int(input("Enter a Marks : "))
if a>90<100:
    print('Hurrah! Your grade is A')
elif a>80<90:
    print('Your grade is B')
elif a>70<80:
    print('Your grade is C')
elif a>60<70:
    print('Your grade is D')
elif a>45<60:
    print('Your grade is E')
else:
    print("You are  FAILED with a clear F!")"""

print("Marks Calculation and Grading Program")
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

if percentage >= 80:
    grade = 'A'
elif percentage >= 70:
    grade = 'B'
elif percentage >= 60:
    grade = 'C'
elif percentage >= 40:
    grade = 'D'
else:
    grade = 'E'

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

