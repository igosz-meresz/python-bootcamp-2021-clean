# -----------------------------------------------------
# --------------**## Intro to Sets ##**----------------
# -----------------------------------------------------

# Sets are another data type in Python.
# They are mutable - they can be changed.
# Sets items must be of immutable types.
# Sets will never have duplicates.
# With sets you can perform mathematical set operations.

# *************------------- Example 1
first_set = {21, 32, 54, 666, 999}
print(first_set)
# they are not ordered

# *************------------- Example 2
mixed = {5.19, "Set", ("London", "Paris")}
print(mixed)
# again, unordered

# *************------------- Example 3
numbers = {1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6}
print(numbers)
# no duplicates

# *************------------- Example 4 ->>> Creating a set from a tuple
# colors = set(("blue", "red", "green", "blue"))
# print(colors)
# print(type(colors))

# *************------------- Example 5 ->>> Creating a set from a list
colors = set(["blue", "red", "green", "blue"])
print(colors)

# *************------------- Example 6 ->>> Creating a set from a dictionary
colors = set({
    "blue": 1,
    "red": 2,
    "green": 3
})

print(colors)

# *************------------- Example 7 ->>> A set cannot have a mutable data type as an item
# colors = {"red", "blue", [1, 2, 3]}
# typeError

# *************------------- Example 8 ->>> An empty set
names = {}
print(names)
print(type(names))
# class dict

numbers = set()
print(numbers)
print(type(numbers))
