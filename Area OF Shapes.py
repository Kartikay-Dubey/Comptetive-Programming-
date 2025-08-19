print("Choose the Shape from given Options")
print("1. for Square")
print("2. for Rectangle")
print("3. for Circle")
while True:
    choice=(input("Choose Shape number from given options: "))

    if choice=="1":
        l=int(input("Enter L of Square: "))
        area=l*l
        print("The Area of Square is ",area)
        break
    elif choice=="2":
        a=int(input("Enter L of Rectangle: "))
        b=int(input("Enter W of Rectangle: "))
        c=int(input("Enter H of Rectangle: "))
        area=a*b*c
        print("The Area of Rectangle is ",area)
        break
    elif choice=="3":
        r=int(input("Enter Radius of Crcle: "))
        area=3.14*r*r
        print("The Area of Circle is ",area)
        break
    else:
        print("The given Shape isn't available in the given choices Sorry! TRY AGAIN")
        continue
   




