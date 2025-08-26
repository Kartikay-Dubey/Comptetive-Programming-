"""

x=int(input("Enter a value of x: "))
y=int(input("Enter a value of y: "))
if x>y:
    small=x
else:
    small=y
for i in range(1,small+1):
    if((x%i==0)and (y%i==0)):
        hcf=i
lcm=int(x*y)/hcf
print("The HCF of", x, "and", y, "is", hcf)
print("The LCM of", x, "and", y, "is", lcm)

"""
   


#Using While Loop


#For HCF
"""
n1=15
n2=25

small=n1 if n1< n2 else n2  #lcm n1>n2 
i=small
while i>0:
    if n1%i==0 and n2%i==0:
        print("HCF is:",i)
        break
    i=i-1 #for lcm we justr do i=i+1
"""

#For LCM
n1=15 
n2=25
big=n1 if n1>n2 else n2

while True:
    if big%n1==0 and big%n2==0:
        print("LCM is:",big )
        break
    big=big+1
