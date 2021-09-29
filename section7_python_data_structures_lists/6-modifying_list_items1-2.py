# -----------------------------------------------------
# -------------**## Modyfing Items ##**----------------
# -----------------------------------------------------

numbers = [1, 55, 64, 124, 654]
names = ['John', 'Mark', 'Emily', 'Sandra']
fruits = ['Apple', 'Orange', 'Banana']

# *************------------- Example 20 ->>>> append()
names.append('Igor')
print(names)

# *************------------- Example 21 ->>>> insert()
fruits.insert(1, "Lemon")
fruits.insert(0, "Peach")
print(fruits)

# *************------------- Example 22 ->>>> pop()
# remove last item
# numbers.pop()
# print(numbers)

# *************------------- Example 23 ->>>> pop()
# remove specific item
# numbers.pop(-1)
# numbers.pop(1)
names.pop(3)
print(numbers)
print(names)

# *************------------- Example 24 ->>>> remove()
fruits.remove("Banana")
print(fruits)

# *************------------- Example 25 ->>>> del statement
# del numbers[0]
# del numbers[1:4]
print(numbers)

# -----------------------------------------------------
# ------------**## Modyfing Items 2 ##**---------------
# -----------------------------------------------------

# *************------------- Example 26 ->>>> clear()
print(fruits.clear())

# *************------------- Example 27 ->>>> reverse()
names.reverse()
print(names)

numbers.reverse()
print(numbers)

# *************------------- Example 28 ->>>> join()
print(", ".join(names))


