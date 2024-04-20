
import copy
l1=[10,20,[9,28,36,67],30]
l2= copy.deepcopy(l1)
l1[2][1]=6
l1[0]=100
print(l1)
print(l2)

# # import random
# # lst=[]
# # for i in range(1,4):
# #     emp_dict={}
# #     user_name=input("enter name")
# #     emp_dict["name"]=user_name
# #     user_sallery=eval(input("enter sallery"))
# #     emp_dict["sallery"]=user_sallery
# #     emp_id=randint(1,6)
# #     emp_dict["id"]=emp_id
# #     lst.append(emp_dict)
# # print(lst)

# # while True:
# #     user_inp=int(input("enter a id:-"))
# #     for d in lst:
# #         if d.get("id")==user_inp:
# #             print(d)

# lst=[]
# for i in range(1,3):
#     book_dict={}
#     book_name=input("enter book name:-")
#     book_dict["name"]=book_name
#     book_author=input("enter author name:-")
#     book_dict["author"]=book_author
#     book_price=eval(input("enter book price:-"))
#     book_dict["price"]=book_price
#     book_category=input("enter category")
#     book_dict["category"]=book_category
#     lst.append(book_dict)
# print(lst)

# while True:
#     user_inp=int(input("enter book price"))
#     for d in book_dict:
#         if d.get("book price")==user_inp:
#             print(d)



        
a = 2 
def add():
    b =3  
    c = a + b
    return c

res = add()
print(res)
print(a)
