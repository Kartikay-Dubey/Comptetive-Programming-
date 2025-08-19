x=input("Select Tempreture Unit from F and C:")

while True:

    if x=="F":
        c=int(input("Enter the TEMPRETURE in Celcius: "))
        faren=(c*9/5)+32
        print("Tempr in fareheight unit is :",faren)

    if x=="C":
        f=int(input("Enter the TEMPRETURE in Farenheit: "))
        Cel=(f-32)*5/9
        print("Tempreture in Celcius unit is :",Cel)