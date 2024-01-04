#Exersise : 1

lst = []
it_company = ["Google","Facebook","Microsoft","Apple","IBM"]
print(len(it_company))

print("First = ",it_company[int(len(it_company)-5)],"Middle = ",it_company[int(len(it_company)/2)], "Last = ", it_company[len(it_company)-1])

mixed_data = ["Nisarg", 19, "5'8", "Non merried", "VVN"]

it_comps = ["Google","Facebook","Microsoft","Apple","IBM", "Oracle", "Amazon"]

print(it_comps)

print(len(it_comps))

print("First = ",it_comps[int(len(it_comps)-7)],"Middle = ",it_comps[int(len(it_comps)/2)], "Last = ", it_comps[len(it_comps)-1])

it_comps[4] = "Black Rock"

print(it_comps)

it_comps.append("TCS")

it_comps[int(len(it_comps)/2)] = "Infosys"

it_comps[1] = it_comps[1].upper()

print(it_comps)

x = "#;".join(it_comps)

print(x)

x = "Google"

print(x in it_comps)

it_comps.sort()

print(it_comps)

it_comps.reverse()

print(it_comps)

print(it_comps[0:3])

print(it_comps[-3:])

print(it_comps[int(len(it_comps)/2) : int(len(it_comps)/2 + 1)] )

it_comps.pop(0)

print(it_comps)

it_comps.pop(int(len(it_comps)/2))

print(it_comps)

it_comps.pop(int(len(it_comps)-1))

print(it_comps)

it_comps.clear()

print(it_comps)

del(it_comps)

front_end = ['HTML', 'CSS', 'JS', 'React' ,'Redux']

back_end = ['Node', 'Express', 'MongoDB']

Third_list = front_end + back_end

Full_Stack = Third_list.copy()

Full_Stack.insert(Full_Stack.index("Redux") + 1, "Python")
Full_Stack.insert(Full_Stack.index("Python") + 1, "SQL")

print(Full_Stack)


#Exersise : 2


Student_Ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

Student_Ages.sort()

MIN_Age = min(Student_Ages)
MAX_Age= max(Student_Ages)

print(Student_Ages)

Student_Ages.insert(MIN_Age,MAX_Age)

print(Student_Ages)

Median_Age = (Student_Ages[len(Student_Ages)//2 - 1] + Student_Ages[len(Student_Ages)//2]) / 2 if len(Student_Ages) % 2 == 0 else Student_Ages[len(Student_Ages)//2]

Average_Age = sum(Student_Ages) / len(Student_Ages)

Age_Range = MAX_Age - MIN_Age

Min_Average_Diff = abs(MIN_Age - Average_Age)

Max_Average_Diff = abs(MAX_Age - Average_Age)

print("Sorted Ages: ", Student_Ages)

print("Min Age: ", MIN_Age)

print("Max Age: ", MAX_Age)

print("Median Age: ", Median_Age)

print("Average Age: ", Average_Age)

print("Age Range: ", Age_Range)

print("Abs(Min - Average): ", Min_Average_Diff)

print("Abs(Max - Average): ", Max_Average_Diff)

Countries = ['India', 'Russia', 'USA', 'Finland', 'France', 'Norway', 'Denmark']

Middle_Countries = Countries[len(Countries)//2 - 1:len(Countries)//2 + 1] if len(Countries) % 2 == 0 else [Countries[len(Countries)//2]]

First_Half = Countries[:len(Countries)//2 + len(Countries) % 2]

Second_Half = Countries[len(Countries)//2 + len(Countries) % 2:]

First_Three, *Scandic_Countries = Countries[:3], Countries[3:]

print("\nMiddle Country(ies): ", Middle_Countries)

print("First Half: ", First_Half)

print("Second Half: ", Second_Half)

print("First Three Countries:", First_Three)

print("Scandic Countries: ", Scandic_Countries)