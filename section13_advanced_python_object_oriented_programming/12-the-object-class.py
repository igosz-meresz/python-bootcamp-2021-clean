# ---------------------------------------------------------------------------------
# --------------------------**## The Object Class ##**-----------------------------
# ---------------------------------------------------------------------------------

# --**--**--**--**--** Example 34 ->>>> attribute inheritance
class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    def running(self):
        print("Running")


runner = John()

# to find out if object is an instance of a class
print(isinstance(runner, John))
print(isinstance(runner, Person))

print(isinstance(Person, object))

base_object = object()


# to find out if object is a class inherits from another class
print(issubclass(John, Person))
print(issubclass(John, object))
