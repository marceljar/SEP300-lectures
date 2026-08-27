list1 = [3, 4, 2, 1]  #list1 points to a list object
list2 = list1         #list2 points to the same list object
list2.append(6)       #object pointed by list1 and list2 changes

print("list1 contains: ", list1)
print("list2 contains: ", list2)