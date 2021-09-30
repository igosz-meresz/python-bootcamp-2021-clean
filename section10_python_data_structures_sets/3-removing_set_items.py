# -----------------------------------------------------
# --------------**## Removing Set Items ##**-----------
# -----------------------------------------------------

# *************------------- Example 14 ->>>> discard()
numbers = {1, 2, 3, 4, 5, 6}
print(numbers)

numbers.discard(4)
print(numbers)

# *************------------- Example 15 ->>>> discard() -> item does not exist

numbers.discard(11)
print(numbers)
# set is unchanged, no error

# *************------------- Example 16 ->>>> remove()

numbers.remove(5)
print(numbers)

# *************------------- Example 17 ->>>> remove() -> item does not exist

# numbers.remove(11)
# print(numbers)
# traceback - KeyError

# *************------------- Example 18 ->>>> pop()
# it removes an arbitrary item from a set
numbers.pop()
print(numbers)
numbers.pop()
print(numbers)

# *************------------- Example 19 ->>>> clear()
numbers.clear()
print(numbers)
