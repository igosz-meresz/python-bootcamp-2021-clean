# -----------------------------------------------------
# -------------------**## Arrays ##**------------------
# -----------------------------------------------------

# ***********----------- Example 12
from array import array

# https://docs.python.org/3/library/array.html

numbers = array("i", [1, 2, 3])
numbers.append(4)
print(numbers)

# how to get an error if I try to insert a different type of data (not string or integer)
# numbers[0] = 2.3
