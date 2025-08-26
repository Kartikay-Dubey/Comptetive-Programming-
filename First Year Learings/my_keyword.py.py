import sys
import keyword
import operator


"""RULES FOR IDENTIFIERS"""
 
#identifiers cant start with digit
#but can start with chr underscore
#cant use special symbols



aalse=10
"""comment
multiple'
lines
"""
print(aalse)


#Statements

b=23+34+23+23+45
print(b)

#multiple line statement
a=23+45\
   +34+60+\
   +70+56
print(a)


#line statement with chr

a1=('a','b','c','d')
print(a1)

a2=('a',
    'b',
    'c',
    'd')
print(a2)


#indentaion

c=20
if c==24:
    print(c)



e=30
for i in range(0,4):
    print(i)
print(e)    #outside the loop




#range function

for d in range(10,20):print(d)