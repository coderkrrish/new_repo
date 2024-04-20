#Data types are the representation or classification of data items.Data types represent the type of data present inside a variable

#Mainly in python there are three types of data types
# i)Numeric-int,float,complex
# ii)Sequential-string,set,list,tuple,frozenset,byte,bytearray,range,
# iii)Mapping-dictionary
# iv)bool
# v)None

a = 10
b = 20
# print(a<b)

# print(False-True)


# s1  = "D"
# print(type(s1))


#--------------------------------Type Casting
# print(int(10+10j))
# print(bool(ord("A")))


# print(float(10))
# # print(float(12+7j))  #error
# print(float("10"))
# print(float("10.88")) #10.88
# print(float("Nine"))
# print(float(10+4j))
 
# print(complex("ten"))  #error

# print(complex(10, 5))

# print(bool(True))

#Bytes are immutable and Bytearray are mutable
# a = [10, 20, 30, 40]
# b = (bytearray(a))
# b[0] = 100
# print(list(b))

#-----------------String data type
s1 = "Welcome To The World Of Python Programming"
# print(s1)
# print(s1[0])
# print(s1[:])
# print(s1[::])
# print(len(s1))

# print(s1[-1])
# print(s1[::-1])
# print(s1[0:20:2])
# print(s1[-42:])

# print(dir(s1))


# print(dir(s1))


#-----------------List Data Type :If we want to represent a group of values as a single entity where order is need to be preserved and duplicates are also allowded then one should go for list.An ordered,mutable,hetrogeneous collection of elements is nothing but list.

#Features of List:
#i)Mutable
# ii)Preserves order
# iii)Hetrogeneous as well as homogeneous elements
# iv)allows duplicates
# v)growable in nature

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] 
# print(l1)
# print(l1[0])
# print(l1[::])
# print(l1[::-1])
# print(l1[0::4])
# print(l1[-10:-2])

# l1.append("Pycharm")
# print(l1)
# print(dir(l1))


# l1.extend("Vega")
# print(l1)

# print(l1.count("V"))

# print(5+0j)

# Write a Python program to count the number of strings where the string length is 2 or more 

# lst = ['abc', 'xyz', 'aba', '1221']
# w_list = [ ]
# count = []
# add = 0
# for words in lst:
#     # if len(words) >=3:
#     #     w_list.append(words)
#     if words[0] == words[-1]:
#         add+=1 

# # print(w_list)
# print(add)
    

# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.

str1 ="Together We Unite"
# print(str1[-2:])
# new_str = 0

# a = str1[0:2] + str1[-2:]
# print(a) #Tote


# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).

def adding(str1):
  if len (str1) >= 3:
    a = str1+"ing"
    print(a)
  else:
    b = a + "ly"
    print(b)



adding("Geting")
 






    


