# A)
List1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

List1.append(5)
print("Append :",List1)

List1.extend([5, 8, 9])
print("extend :",List1)

List1.remove(5)
print("remove :",List1)

List1.reverse()
print("reverse :",List1)

List1.sort()
print("List in ascending order:", List1)

List1.sort(reverse=True)
print("List in descending order:", List1)


# B)

List2 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]


Word1 = List2[8][2]
print("Word 1:", Word1)

Word2 = List2[4][0].capitalize()
print("Word 2:", Word2)
NewLST = [List2] * 5
print("Repeated list:", NewLST)



# C)

Olist = [1, 2, 3, 4, 5]

CList= Olist[:]

print("Original List:", Olist)
print("Copied List:", CList)


# D)
# Create a tuple
Tuple = (1, 2, 3, 4, 5)

TupleSum = sum(Tuple)
print("Sum of Tuple:", TupleSum)

TupleMax = max(Tuple)
print("Maximum value in Tuple:", TupleMax)

TuplaMin = min(Tuple)
print("Minimum value in Tuple:", TuplaMin)