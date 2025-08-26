import sys
import keyword
import operator


#Docstrings
def cube(a):
    return a**3
print(cube(6))



#evn odd

def evenodd(x):
    #evenodd is used as print function
    if x%2==0:
        print("Even Number")
    else:
        print("Odd Number")

evenodd(5)

#using id function
p=30
q=30
ab=id(p)
bc=id(q)
a=hex(id(p))#memory address in hexa form 
print(ab)
print(bc)
print(a)

#PS:id value depends on number not pn variable

p=20
q=40
r=q
print(r,type(p),hex(id(p)),hex(id(q)))


x=30
y=x+30   #variable overwriting
print(y)
print(len(a))














#Variable assignment
numval=34
decval=23
alphaval="CODING NINJAS"

print(numval, decval,alphaval)


num,str=10,"kartik"
print(num,str)


#Numeric Value


abc=20
print(abc,"is interger?",isinstance(abc,float),(type(abc)),sys.getsizeof(abc))

#sys.getsizeof shows the size of int

xyz=89.5
print(xyz,"is a float value",isinstance(xyz,float))


ww=65+40j 
print(ww,"is a complex value",isinstance(ww,complex))

e=54
u=60.5
f="computer"
print(sys.getsizeof(e))
print(sys.getsizeof(u))


#Boolean

bool1=True
bool2=False
print(type(bool1),isinstance(bool1,float))


#Statements

a=int(input("ENETR A VALUE:"))
if a<0:
    print(a,"Given value is Negative")
else:
    print(a,"Given no. is psotive")

#Give comment in variable

v='''HEY CODER'''
print(v)


#inexing adress   


























































