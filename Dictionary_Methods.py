d1= {"Name": 'KISHOR',"DOB":'24/2/1999',"Gender":'Male',"Address":{"Village":'sasure',"City":'sasure',"Pincode":413402},"Age":24}
# print(d1,(type(d1))
# print(dir(d1)

# d2=(d1.clear())
# print(d1)

# print(d1.copy())


# d2=d1.get('KISHOR')
# d2=d1.get('Address')
# d2=d1.get("Gender")

# print(d1.keys())
# print(d1.values())

# res=d1.pop("Name")
# print(res)
# print(d1)

# print(d1.pop("Age"))

# # print(d1.popitem())
# res=d1.popitem()
# print(res)
# print(d1)
# res=d1.popitem()
# print(res)
# print(d1)

# print(d2)

# res=d1.setdefault("Name")
# print(res)
# res=d1.setdefault("Age")
# print(res)
# d2=d1.setdefault("Nationality")
# print(d2)
# d3={"Degree":"B.tech","Petname":"Nana"}
# d1.update(d3)
# print(d1)

# print(d1.values())
# print(d1.keys())
# alphabates={'a','b','c','d'}
# values=(1)
# d2=(d1.fromkeys(alphabates,values))
# print(d2)
# print(d1)


d1= {"Name": 'KISHOR',"DOB":'24/2/1999',"Gender":'Male',"Address":{"Village":'Sasure',"City":'Sasure',"Pincode":413402},"Age":24}


# print(d1)


new_dic = d1.copy()
# print(new_dic)

# print(d1.get("Name"))

# print(d1.get("Address"))


# print(d1.get("Address").get("Village"))


# update_dic = {"Qualification" : "B.Tech"}
# d1.update(update_dic)
# print(d1)


# for keys ,values in d1.items():
#     print(keys,values)


# res= d1.popitem()  #Pop item will remove the last key value pair from the dict
# print(res)


# res = d1.pop("Address") #Pop takes only one argument and pops out the key value pair given as argument
# print(res)
# print(d1)

# print(d1)

# print(d1.setdefault("Name")) #Setdefault will return the value associated with the argument given 

d1.setdefault("Salary") #But if the key is not present then it will add the argument with the value set to none
# print(d1)


# print(d1.keys())

# print(d1.values())


# print(d1.items())

# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {**dict1, **dict2}
# print(dict3)

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

print(sampleDict["class"]["student"]["marks"]["history"])

print(sampleDict.get("class").get("student").get("marks").get("history"))


for key,values in sampleDict.items():
    print(key,values)


a = print(sampleDict.items())

