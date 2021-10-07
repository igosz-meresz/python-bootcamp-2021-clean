# -----------------------------------------------------
# --------**## What Are Exceptions? ##**---------------
# -----------------------------------------------------

# https://docs.python.org/3/library/exceptions.html

# Syntax Errors
# Logical Errors (Exceptions)

# ***********----------- Example 1 ->>> SyntaxErrors
# if 2 > 1 # Syntax Error

# ***********----------- Example 2 ->>> Logical Errors

# ZeroDivisionError
# 1 / 0

# FileNotFoundError
# open("imaginary.txt")

# ***********----------- Example 3 ->>> Exceptions
numbers = [1, 2]
# print(numbers[3]) # IndexError

# ***********----------- Example 4 ->>> Exceptions
age = int(input('age: '))
