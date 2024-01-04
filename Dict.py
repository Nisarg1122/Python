Dog = {}

Dog["Name"] = "Bruno"
 
Dog["Color"] = "Brown"
 
Dog["Breed"] = "German Sheferd"

Dog["Legs"] = 4

Dog["Age"] = 6

Student = {
    "First_Name": "Ram",
    "Last_Name": "Chaturvedi",
    "age": 28,
    "country": "India",
    "is_marred": True,
    "skills": ["HTML","JavaScript", "React", "Express", "Node", "MongoDB", "Python", "CSS"],
    "address": {
        "street": "Street - 6 ",
        "zipcode": "200412"
    }
}

print("Length of student dictionary:", len(Student))

Skills_Value = Student["Skills"]

print("Skills:", Skills_Value)

print("Data type of skills:", type(Skills_Value))

Student["Skills"].extend(["HTML", "Ruby"])

Keys_List = list(Student.keys())

print("Dictionary keys:", Keys_List)

Values_List = list(Student.values())

print("Dictionary values:", Values_List)

Student_Tuples = list(Student.items())

print("List of tuples:", Student_Tuples)

Student.pop('is_marred')

del Dog

print("Modified student dictionary:", Student)
