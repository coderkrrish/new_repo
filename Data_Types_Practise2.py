# data types in python
#int, float, string, list, set, tuple, dictionary, boolean, range, frozenset, bytes, bytearray

a = 20
# print(type(a))

b = 2.494
# print(type(b))


#  a = 987654321 iterate a without converting it into the string

a = 987654321
# new_var = str(a)
# for i in new_var:
#     print(i, end = ",")

# while a > 0:
#     a, digit = divmod(a, 10)
#     print(digit, end =" ")
# print(a)

# for c in map(int, str(a)):
#     print(c)

# val1 = 100
# val2 = 2.2
# print(divmod(val2, val1))

# 8. Write a function for second largest number in list

l1 = [1, 33, 923, 2393, 4293, 203, 230]
# l1.sort()
# print(l1)


def second_largest():
    l1.sort()
    print(l1[-2])

# second_largest()

list1  = [20, 392,429, 203,1042, 48348]
# list1.remove(max(list1))
# print(max(list1))

m  = max(list1)
ans = [c for i , c in enumerate(list1) if c<m]
# print(max(ans))


