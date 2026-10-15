fruits = {"apple", "banana", "cherry", "apple"}  
print("Original set:", fruits)

fruits.add("orange")
print("After adding orange:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

#fruits[1] error - sets are non-indexable

boolean = "cherry" in fruits
print("Is 'cherry' in the set?", boolean)

# Set operations
more_fruits = {"melon", "grape", "apple"}

print("Union:", fruits | more_fruits) 
print("Intersection:", fruits & more_fruits) 
print("Difference:", fruits - more_fruits)   
print("Symmetric Difference:", fruits ^ more_fruits)