#string is a sequence of characters ..Beacause string is immutable operations performed on string wiil not change the original string instead return a new string

s1="Every string method does not change"
# print(dir(s1))

# s2=s1.capitalize()# This method will capitalize the first letter of the string
# print(s1)        #Output:-Every string method does not change

# s2=s1.casefold()  #implements caseless string matching
# print(s2)

# s2=s1.count("e")  #This method will give the count of that string given as argument 
# print(s2)  #Output :-

# s2=s1.encode()
# print(s2)

string1="The below functions are used to change"
# s2=string1.find("below") #This method wiil return the index at which the given string occures first but if we gave the string which is not present it will not raise error it will return -1
# print(s2) #Output:- 5
# s2=string1.find("paper")
# print(s2) #Output: -1

# s2=v.index("z") #This method will return the index position at which the string given as argument is present
# print(s2)  #Output:9 but if we given any string that is not present it will raise an error

# s2=v.isalnum() #This method wiil tell if the given string is alphanumeric 
# print(s2)   #Output:-False

# s2=v.isalpha()  #Returns “True” if all characters in the string are alphabets space is not allowded
# print(s2)

# s2=v.isdigit()  #	Returns “True” if all characters in the string are digits
# print(s2)

# s2=v.islower() #Checks if all characters in the string are lowercase
# print(s2)

# s2=v.isnumeric() #Returns “True” if all characters in the string are numeric characters
# print(s2)

# s2=v.isspace() #	Returns “True” if all characters in the string are whitespace characters
# print()
# s2=v.partition(" a" ) # it will split the string from the argument given 
# print(s2)        #output :- ('The below functions', ' a', 're used to change')
#a3=v.partition('f')
# print(a3)  #output:('The below ', 'f', 'unctions are used to change')

# s2=v.replace("The","These") 
# print(s2)  #Output :These below functions are used to change



# s2=v.rsplit()  #This method will return the string splitted in an list
# print(s2)      #Output:['The', 'below', 'functions', 'are', 'used', 'to', 'change']



# l1 = [1,2,4]
# a ="ALT"
# res = (8,9,0)
# print(l1,a ,res, sep = " ,")


# from sys import argv

