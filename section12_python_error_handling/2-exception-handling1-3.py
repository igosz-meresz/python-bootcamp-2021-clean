# -----------------------------------------------------
# --------**## Handling Exceptions 1 ##**--------------
# -----------------------------------------------------

import sys

# ***********----------- Example 5 ->>> try ... except
# try:
#     age = int(input("Age: "))
# except:
#     print("Plase enter a valid age")

# print("No exceptions here")

# ***********----------- Example 6 ->>> try ... except... else
# try:
#     age = int(input("Age: "))
# except ValueError:
#     print("Plase enter a valid age")
# else:
#     print("No Errors Here")

# ***********----------- Example 7 ->>> try ... except... else
# try:
#     age = int(input("Age: "))
# except ValueError as exp_error:
#     print("Plase enter a valid age")
#     print(exp_error)
#     print(type(exp_error))
# else:
#     print("No Errors Here")

# ***********----------- Example 8 ->>> try ... except
# random_list = ["a", 0, 2]

# for entry in random_list:
#     try:
#         print("The entry is: ", entry)
#         r = 1 / int(entry)
#         break
#     except:
#         print("Oops...", sys.exc_info()[0], "occured.")

#         print("Next entry.")
#         print()

# print()
# print("The reciprocal of", entry, "is", r)

# ***********----------- Example 9 ->>> try ... except
# random_list = ["a", 0, 2]

# for entry in random_list:
#     try:
#         print("The entry is: ", entry)
#         r = 1 / int(entry)
#         break
#     except Exception as exp_error:
#         # Exception is the same as __class__
#         print("Oops...", exp_error.__class__, "occured.")

#         print("Next entry.")
#         print()

# print()
# print("The reciprocal of", entry, "is", r)

# -----------------------------------------------------
# --------**## Handling Exceptions 2 ##**--------------
# -----------------------------------------------------

# ***********----------- Example 10 ->>> get a ZeroDivisionError

# try:
#     age = int(input("Age: "))
#     x = 10 / age
# except ValueError:
#     print("Please enter a valid age")
# else:
#     print("No Errors Here")

# ***********----------- Example 11 ->>> Resolving a ZeroDivisonError

# try:
#     age = int(input("Age: "))
#     x = 10 / age
# except ValueError:
#     print("Please enter a valid age")
# except ZeroDivisionError:
#     print("age cannot be zero")
# else:
#     print("No Errors Here")

# ***********----------- Example 12 ->>> Creating a tuple of Errors

# try:
#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid age")
# else:
#     print("No Errors Here")

# -----------------------------------------------------
# --------**## Handling Exceptions 3 ##**--------------
# -----------------------------------------------------

# ***********----------- Example 13 ->>> try... except... else... finally

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age
#     note.close()

# except (ValueError, ZeroDivisionError):
#     print("Please, enter a valid age")
# else:
#     print("No errors here")

# Solution 1 ->>> moving the close() method to the except clause

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age

# except (ValueError, ZeroDivisionError):
#     print("Please, enter a valid age")
#     note.close()
# else:
#     print("No errors here")

# Solution 2 ->>> duplicate the close() method to the else clause

# try:
#     note = open("someFile.txt")
#     age = int(input("Age: "))
#     x = 10 / age

# except (ValueError, ZeroDivisionError):
#     print("Please, enter a valid age")
#     note.close()
# else:
#     print("No errors here")
#     note.close()
# This, however, does not follow the DRY principle

# Solution 3 ->>> use the finally clause

try:
    note = open("someFile.txt")
    age = int(input("Age: "))
    x = 10 / age

except (ValueError, ZeroDivisionError):
    print("Please, enter a valid age")
else:
    print("No errors here")
finally:
    note.close()
