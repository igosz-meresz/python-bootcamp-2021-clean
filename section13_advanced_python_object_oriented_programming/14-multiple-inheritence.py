# ---------------------------------------------------------------------------------
# --------------------------**## Method Overriding ##**----------------------------
# ---------------------------------------------------------------------------------


# --**--**--**--**--** Example 36 ->>>> bad multiple inheritance
class Person:
    def sport_status(self):
        print("Runner")


class John:
    def sport_status(self):
        print("Jogger")


class Jane(Person, John):
    pass


jane = Jane()
jane.sport_status()


# --**--**--**--**--** Example 37 ->>>> good multiple inheritance
class Person:
    def runner(self):
        print("Runner")


class John:
    def jogger(self):
        print("Jogger")


class Jane(Person, John):
    pass


jane1 = Jane()
jane1.runner()
jane1.jogger()
