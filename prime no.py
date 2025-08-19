num=int(input("Enter a number to Check: "))
if num>1:
    for i in range (2,num):
        if num%i==0:
            print(num,"is not a PN!") 
            break
    else:
        print(num,"is a PN!")
else:
    print(num,"is not a PN!")