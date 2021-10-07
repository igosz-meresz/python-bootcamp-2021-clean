# ---------------------------------------------------------------------------------
# --------------------------**## Method Overriding ##**----------------------------
# ---------------------------------------------------------------------------------

# --**--**--**--**--** Example 35 ->>>> overriding
class Person:
    def __init__(self):
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    def __init__(self):
        self.jogger = True

    def run(self):
        print("Running")


runner = John()
print(runner.jogger)
# print(runner.employed)
# jogger has overriden employed in Person

# --**--**--**--**--** Example 35 ->>>> fixing overriding


class Person:
    def __init__(self):
        print("Base Class")
        self.employed = True

    def sing(self):
        print("Singing")


class John(Person):
    def __init__(self):
        super().__init__()
        # this is overriding

        print("Sub Class")

        self.jogger = True

    def run(self):
        print("Running")


runner = John()
print(runner.jogger)
print(runner.employed)
