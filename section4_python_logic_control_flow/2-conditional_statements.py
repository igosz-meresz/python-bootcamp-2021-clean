# -----------------------------------------------------
# --------**## Conditional Statements ##**-------------
# -----------------------------------------------------

"""
if (boolean expression):
    execute the statements

"""

# *************------------- Example -->>> check for a single condition
temp = 35
temp = 29
temp = 10
temp = 45
temp = 55

if temp > 30:
print("It is a good day for walking")
this is outside the 'if' statement
print("It is not part of the if statement")

# *************------------- Example -->>> check for 2 conditions
if temp > 25:
    print("Awesome")
else:
    print("Cold")

# *************------------- Example -->>> check for multiple conditions
temp = 55
temp = 35
temp = 34
temp = 25
temp = 19


if temp > 35:
    print("Hot")
elif temp > 25:
    print("Awesome")
elif temp < 20:
    print("Cold")
else:
    print("Undecided")
