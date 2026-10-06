list1 = [3, 4, 2, 1]  # list1 points to a list object
print("After list1 = [3, 4, 2, 1]")
print("id(list1):", id(list1))

list2 = list1         # list2 points to the same list object
print("After list2 = list1")
print("id(list1):", id(list1))
print("id(list2):", id(list2))

list2.append(6)  # objects pointed by both lists change
print("After list2.append(6)")
print("id(list1):", id(list1))
print("id(list2):", id(list2))

print("list1 contains: ", list1)
print("list2 contains: ", list2)