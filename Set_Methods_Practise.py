s = {1, "abc", 23, 44, 56, 10+2}
# print(dir(s))

# Because in set order is not prserves elements will be added at random positions

# s.add("krrish") #This method will add the given element in set
# print(s)        #{1, 'krrish', 23, 56, 44, 12, 'abc'}


# s.update("Man","Feb")     #this method will  add one by one elements like extend in list do .we can pass multiple arguments
# print(s)                  #{1, 'a', 'e', 'n', 12, 23, 'F', 44, 'b', 'abc', 'M', 56}

# s.clear()      #this method will remove all the elements from the set and returns an empty set
# print(s)        #set()

# s.remove(99)   #this method will remove the given element from the set
# print(s)           #{1, 23, 56, 44, 12} If we try to remove an unpresent element it will throw error

# s.pop()        #this method wiil pop the random value from the set
# print(s)       #{'abc', 23, 56, 44, 12}

# s.discard("abc")  # this method is same as remove and pop
# print(s)  # {1, 23, 56, 44, 12} only
# the difference is if we try to remove any unpresent element it wont throw error
# s.discard(33)
# print(s)  # {1, 23, 56, 44, 12}

#Range Data Type
# values = range(ord("A"),ord("Z"))
# print(values[0])
# print(values[1])

# print(list(values))
# print((values))


#Set Defn : When we want to represent values as a single entitiy where order is not preserved and duplicates are not allowded then we should go for set..

#Features Of Set :

#1)Growable In Nature
#2)Do not preserves order
#3)Supports only immutable data type
#4)Supports homo as well as hetro 
#5)Duplicates Are Not Allowded
#6)Because order is not preserved index based operations are not supported

s1  ={1,2,3,1,3,2}

# print(s1)

s2 = {"A", "ABhay",7+8j,9.7,1,(10,20,39),0}
# print(s2)

# print(s2[0]) #TypeError: 'set' object is not subscriptable


# print(list(s2))

# print(dir(s2))

#'add', 'clear', 'copy','discard,'pop', 'remove', 'update'

s3 = {1,9,True,(12,24,36,),"A","Python",9+7j}
s3.add(10)
# print(s3)  #Add Is like list append 

s3.add("Program")
# print(s3) 

# s3.add(45,87) #.Only one element at a time can be added
# print(s3) #TypeError: set.add() takes exactly one argument (2 given)

s4 = {1,2,0,11+7j,(12,6,3),"Backspace"}
# print(s4)


s5 = s4.copy()
# print(s5)

s4.update("Control", "ALT")  #Update is like list extend .Multiple elements can be added
# print(s4)


s4.update(range(1,7))
# print(s4)


s5 = {10,20,40,"Cover","Hang"}
# s5.remove(10)
# print(s5)

res = s5.pop()
# print(res)

s5.discard('Hang')
# print(s5)

s5.discard("Memory")
# print(s5)


# print(dir(s5))


s1 = {1,2,33,4,5,6}
s2 ={1,2,6,365,23,65}
# print(s1.intersection(s2))  #Intersection will return the commom elements from two sets



# print(s1.difference(s2)) #Difference will give the other than commom elements with resepect to the other set

# print(s2.difference(s1)) #

# print(s1.symmetric_difference(s2))
# print(s2.symmetric_difference(s1)) #symmetric element will return different elements from two sets in one set

s4 ={1,3,2,"j", "k", "g","Python"}
s5 = {1,2,3,"Program", "Language"}

# print(s5.union(s4))

# s4.difference_update(s5)
# print(s4)  #Difference update will remove the common elements from the sets


# s6 = {"Apple","Banana","Cherry"}
# s7 = {"Microsoft","Apple","IBM"}
# s7.difference_update(s6)
# print(s7)



# s1 = {2,33,12,5,3,632,623}
# total = 0
# for i in s1:
#     total +=i
# print(total)


# b1 = bytes(178)
# print(b1)

# for i in enumerate(b1):
#     print(i, end = " ")



# r = range(1,11)
# for i in enumerate(r, 9):
#     print(i)



lst = []

for i in range(1,4):
    d ={}
    Emp_id =i
    Emp_name = input("Enter Name")
    Emp_Salary = float(input("Enter Salary"))
    d["id"] = Emp_id
    d["Name"]  = Emp_name
    d["Salary"] = Emp_Salary
    lst.append(d)

print(lst)

while True:
    user_inp = int(input("Enter Emp Id"))
    for d in lst:
        if d.get("id") == user_inp:
            print(d)
    inp = input("Would You Like TO Continue : Y/N")
    if inp == "Y":
        pass
    else:
        break