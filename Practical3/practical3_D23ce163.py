# A)
s1="Nisarg"
s2="Dobariya"
print("reversed string :",s1[::-1])
print("Replaced string :",s1.replace("isarg","ISARG"))
print("Merge two string :",s1+s2)
print("Find character in string :","N" in s1)

s = "Hello, World!"
print("words", s.split())
print("characters",[char for char in s])

# B)
dr={
    "name":"Nisarg",
    "age":19 ,   
    "grade":"AA"
}

print("update  Dictionary Values:",dr.update({'grade':'AA+'}))
print("Access Dictionary Values: ",dr.values())
print("Access Dictionary key: ",dr.keys())
print("Print the 'age': ",dr.get('age'))
print("pop : ",dr.pop('age'))
print("pop item :",dr.popitem())
print("clear :",dr.clear())
print("delete :")
del dr

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

merged_dict = dict1 | dict2 | dict3

print(merged_dict)
