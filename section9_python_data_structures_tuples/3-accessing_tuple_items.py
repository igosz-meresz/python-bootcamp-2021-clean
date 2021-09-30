# -----------------------------------------------------
# ------------**## Accessing Tuple Items ##**----------
# -----------------------------------------------------

# *************------------- Example 8 ->>>> Indexing

mixed = (False, 3.14159, "Python", ["Web", "Mobile"], 45)
print(mixed[0])
print(mixed[2])
# print(mixed[5])
# IndexError, doesn't exist
# print(mixed["a"])
# TypeError

# *************------------- Example 8 ->>>> Negative Indexing
print(mixed[-1])
print(mixed[-4])
print(mixed[-2])

# *************------------- Example 9 ->>>> Slicing
print(mixed[0:2])
print(mixed[2:4])
print(mixed[:3])
print(mixed[3:])
print(mixed[:])
# that just prints all
