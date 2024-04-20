#Operators in python are used to perform operations on data types.
#1)ARITHMATIC OPERATORS:-Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
"""
i)Addition Operator:-
print(2+2) Output:-4
a=45
b=34
print(a+b) Output:-79

addition operator is also used for concatination operations
s="hello"
s2="world"
print(s+s2) Output:-helloworld

a=[12,24,36,48]
b=[60,72,84,"abc"]
print(a+b)  Output[12, 24, 36, 48, 60, 72, 84, 'abc']

ii)Substraction Oprator
print(90-10)  Output:-80
c=100
d=50
print(c-d) Output:-50

iii)Multiplication Operator
a=12
v=10
print(a*v) Output:-120

num1=113
num2=214
print(num1*num2) Output:-24182
print ("abc"*3)  Output:-abcabcabc

iv)division operator
num1=55
num2=11
print(num1/num2) Output:-5.0

a=200.0
b=20.0
print(a/b) Output:-10.0


v)Modulus Operator:It will return the reminder
a=14
b=7
print(a%b) Output:-0

num1=120
num2=13
print(num1%num2) Output:-3

'''
vi)Floor division:this will return the division in int type instead of float
a=60
b=15
print(a//b) Output:-4

num1=325
num2=12
print(num1//num2) Output:-27

# vii)Exponent opearator:-left operand raised to the power of right
a=7
b=7
print(a**b) Output:-823543
"""

#2)Comparison operators:-Comparison operators are used to compare values. 
'''
a=90
b=10
print(a>b)  Output:-True

a=50
b=100
print(b<a)
print(b>a)
print(b==a)
print(b!=a)
print(b>=a)
print(b<=a)

Output:-
False
True
False
True
True
False

c=124
d=799
print(c<d)
print(c>=d)
print(c<=d)
print(c==d)
print(c!=d)

Output:-True
False
True
False
True
'''


#3)Logical operators :- Logical operators are the and, or, not operators.
'''
a=23
b=456  #And opearator needs all conditions to be true
print(a>b & b>=a) Output:-False


num1=100002
num2=900
num3=103
print(num1>num2 & num1>num3) Output:-True

value1=2436
value2=3235  Or operator needs at least one condition to be true
print(value1<value2 | value2>value1) Output:-True

val1=1
val2=100
val3=587678
print(val1<val2 | val3>=val1) Output:-True

a=23
b=23
print(a!=b) Output:-False

val1=214
val2=351
print(val1!=val2)  Output:-True
'''

#4)Assignment Operators:-Assignment operators are used in Python to assign values to variables.
'''
val1=35

a=5
a+=10
print(a)  Output:-15


z=469
z-=100
print(z) Output:-369


j=80
j*=10
print(j) #Output:-800

k=144
k/=12
print(k) Output:-12.0
'''

#5)Special Operators
'''
#i)#Membership Operators(in and not in){This operator will check if the member is present or not}

l=[13,4413,646,86,97,97]
print(97 in l) #Output:-True

s="i can do it"
print("can" in s) #Output:-True



#ii)Identity operators(is and not is){This oprator will check if the memory location of two objects is equal or not}

a=134
b=134
print(id(a),id(b))         #Output:-2631654642064 2631654642064  
print(a is b)               #True

z=1323
x=32355
print(z is x)  #Output:-False
'''

#Math Module:-This module provides all the libraries releted to performing mathematicle operations
'''
import math
# a=math.sqrt(625)
# print(a)

# print(dir(math))

# print(math.pow(6,2))  Output:-36.0

# print(math.sin(90))      Output:-0.8939966636005579

# print(math.cosh(120))   Output:-6.520904391968161e+51

print(math.factorial(10)) #Output:3628800
'''
import time
s1="This module provides all the libraries"
for i in s1:
  print(i)

s="This module provides all the libraries"
for i in s:
  print(i,end=" ")
