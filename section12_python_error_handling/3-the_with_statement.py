# -----------------------------------------------------
# ---------**## The with Statement ##**----------------
# -----------------------------------------------------

# ***********----------- Example 14 ->>> opening a single file
# try:
#     with open("someFile.txt") as note:
#         print("note opened")

#     age = int(input("Age: "))
#     x = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("Please enter a valid age.")
# except FileNotFoundError:
#     print("oops, file not found")
# else:
#     print("No exceptions here")

# ***********----------- Example 15 ->>> opening multiple files

try:
    with open("someFile.txt") as note, open("anotherFile.txt") as my_note:
        print("notes opened")

    age = int(input("Age: "))
    x = 10 / age
except (ValueError, ZeroDivisionError):
    print("Please enter a valid age.")
except FileNotFoundError:
    print("oops, file not found")
else:
    print("No exceptions here")
