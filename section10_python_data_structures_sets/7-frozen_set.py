# -----------------------------------------------------
# -------------------**## Frozen Set ##**--------------
# -----------------------------------------------------

# *************------------- Example 31 ->>>> Creating a frozenset
numbers = frozenset([1, 2, 3, 4, 5, 6])
some_nums = frozenset([3, 4, 5, 6])
print(numbers)
print(type(numbers))

print(numbers.isdisjoint(some_nums))
# all of the numbers from set"numbers" and "some_nums" have common items

print(numbers.difference(some_nums))
# all elements in numbers but not in some_nums

# *************------------- Example 31 ->>>> frozenset() method
vowels = ("a", "e", "i", "o", "u")
frozen_vowels = frozenset(vowels)
print(frozen_vowels)

print("Empty Frozen Set", frozenset())

print(frozenset().add("y"))
# AttributeError, object has no attribute 'add'
