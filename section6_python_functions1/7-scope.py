# -----------------------------------------------------
# ------------------**## Scope ##**--------------------
# -----------------------------------------------------

# Local Variables
# Global Variables

# *************------------- Example 15
def message(date):
    content = "Something very cool has happened"


message("May 22, 2100")

# print(date) # NameError
# print(content) # NameError

# *************------------- Example 16


def comment(date):
    content = "amazing landscape"


comment("May 23, 2089")

# *************------------- Example 17
content = "just do it"


def post(date):
    content = "i am on a trip"


post("July 13, 1970")
print(content)

# *************------------- Example 17
# This is a bad practice (global)

dog_name = "Hachi"


def animal_names():
    # global dog_name
    dog_name = "Georgie"


animal_names()
print(dog_name)
