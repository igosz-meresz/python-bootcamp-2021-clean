# -----------------------------------------------------
# ----------**## Accessing List Items ##**-------------
# -----------------------------------------------------

# *************------------- Example 9
collection = [28, "M", 32, "H", "Parrot", "Sea Biscuit", "Goat"]

# access & modify
collection[5] = "Python"

print(collection)

# access
print(collection[2])

# *************------------- Example 10
# access range of items
print(collection[2:4])
print(collection[:3])
print(collection[4:])
print(collection[:])

# *************------------- Example 11
# access every 2nd item
print(collection[::2])
# access every 3rd item
print(collection[::3])
print(collection[2::3])
print(collection[2:5:3])
