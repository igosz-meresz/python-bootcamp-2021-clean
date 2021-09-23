# -----------------------------------------------------
# ------------**## Data Types part 1 & 2 ##**--------------
# -----------------------------------------------------

"""
-- Data type --             -- class--              --Value--
integers                    -> int                  -> 45
floating point numbers      -> float                -> 4.5
booleans                    -> bool                 -> True/False
strings                     -> str                  -> "Igor Remesz"
list                        -> list                 -> [1, 2, 3]
dictionary                  -> dict                 -> {"user_name: "awesome50", "user_id": 56}
tuple                       -> tuple                -> (10, 20, 30)
set                         -> set                  -> {"cat", 99}
"""

# *-*-*-*-*------------ Numbers ***********************

# Integer
age = 27
print(age)
print(type(age))

# Floats
grade = 8.9
print(grade)
print(type(grade))

# *-*-*-*-*------------ Booleans ***********************
alarm = True
offline = False
print(alarm, offline)
print(type(alarm))
print(type(offline))

# *-*-*-*-*------------ Strings ***********************
movie_name = "Goodfellas"
print(movie_name)
print(type(movie_name))

# *-*-*-*-*------------ List ***********************
# Ordered
numbers = [1, 2, 3.2, 5.4]
print(numbers)
print(type(numbers))

mixed = [1, 2, 3.2, 5.4, True, "Igor Remesz", [1, 2, 3]]
print(mixed)
print(type(mixed))

# *-*-*-*-*------------ Dictionary ***********************
# Unordered
user_info = {"user_name": "awesome50", "user_id": 56}
print(user_info)
print(type(user_info))

# *-*-*-*-*------------ Tuple ***********************
# They are immutable (you cannot change it once it is declared)
# ordered
mixed_tuple = (1, 2, 10.2, 5.4, True, "Igor Remesz", [1, 2, 3])
print(mixed_tuple)
print(type(mixed_tuple))

# *-*-*-*-*------------ Set ***********************
# unordered
mixed_set = {1, 2, 8.2, 5.4, "Python", "Igor Remesz"}
print(mixed_set)
print(type(mixed_set))
