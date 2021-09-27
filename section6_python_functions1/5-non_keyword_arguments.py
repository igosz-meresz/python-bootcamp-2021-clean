# -----------------------------------------------------
# -----------**## Non-Keyword Arguments ##**-----------
# -----------------------------------------------------

# *************------------- Example 10
def sum(x, y):
    return x + y


print(sum(89, 98))

# print(sum(89, 98, 23, 56, 45))  # Traceback, too many arguments (2 expected)

# *************------------- Example 11


def num(*numbers):
    return numbers


print(num(10, 21, 65, 221, 555, 666))

# *************------------- Example 12


def subtract(*nums):
    number = 100
    for x in nums:
        number = number - x
    return number


print(subtract(2, 3, 5, 25, -45, 111))
