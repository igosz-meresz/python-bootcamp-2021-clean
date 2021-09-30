# -----------------------------------------------------
# ---------------**## Changing Tuples ##**-------------
# -----------------------------------------------------

# *************------------- Example 10 ->>>> changing tuple elements
numbers = (4, 2, 3, [5, 6, 7, 8])
# numbers[1] = 10
# type error
# print(numbers)
numbers[3][2] = 111
# print(numbers)

# *************------------- Example 11 ->>>> reassignment of a tuple
numbers = (222, 333, 444)
# print(numbers)

# *************------------- Example 12 ->>>> repeating a tuple items
print(("Movie",)*5)

# *************------------- Example 13 ->>>> tuple concatenation
letters = ("p", "y", "t", "h", "o", "n")

# mixed = numbers + letters
# print(mixed)

# *************------------- Example 14 ->>>> deleting a tuple entirely
del letters
print(letters)
# nameError
