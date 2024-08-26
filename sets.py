# Creating a set
fruits = {"apple", "banana", "cherry"}

# Adding an element to the set
fruits.add("orange")

# Removing an element from the set
fruits.remove("banana")

# Checking if an element exists in the set
if "apple" in fruits:
    print("Apple is in the set")

# Looping through the set
for fruit in fruits:
    print(fruit)

# Performing set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Union of sets
union_set = set_a.union(set_b)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}

# Intersection of sets
intersection_set = set_a.intersection(set_b)
print(intersection_set)  # Output: {3, 4}

# Difference of sets
difference_set = set_a.difference(set_b)
print(difference_set)  # Output: {1, 2}
