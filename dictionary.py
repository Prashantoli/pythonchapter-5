# Creating a dictionary
student = {
    "name": "Prashant Oli",
    "age": 22,
    "course": "Computer Science",
    "email": "prashantoolee7@gmail.com"
}

# Accessing a value using the key
print(student["name"])  # Output: Prashant Oli

# Adding a new key-value pair
student["graduation_year"] = 2024

# Updating an existing value
student["age"] = 23

# Removing a key-value pair
del student["email"]

# Looping through the dictionary
for key, value in student.items():
    print(key, value)

# Output:
# name Prashant Oli
# age 23
# course Computer Science
# graduation_year 2024
