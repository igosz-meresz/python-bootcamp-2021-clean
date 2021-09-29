# -----------------------------------------------------
# -------------**## Finding Items ##**-----------------
# -----------------------------------------------------

# numbers = [1, 1, 1, 3, 5]
numbers = [1, 1, 1, 3, 5] * 5

fruits = ['Apple', 'Orange', 'Banana']

# *************------------- Example 29 ->>>> index()
print(fruits.index("Orange"))

# *************------------- Example 30
if "Mango" in fruits:
    print(fruits.index("Mango"))

# *************------------- Example 31
print(fruits.count("Mango"))
print(fruits.count("Banana"))
print(numbers.count(1))
