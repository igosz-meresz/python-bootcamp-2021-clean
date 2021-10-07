# -----------------------------------------------------
# --------**## Instance vs Class Methods ##**----------
# -----------------------------------------------------

# ***********----------- Example 10 ->>>> instance methods

class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"Walking coordinates ({self.x}, {self.y})")


test_walk = Robot(1.1, 4.6)
test_walk.walk()

# ***********----------- Example 11 ->>>> class methods


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # decorator
    @classmethod
    def specific_coordinate(cls):
        # cls is short for class, it's a convention name - the best practice
        return cls(1.1, 4.6)

    def walk(self):
        print(f"Walking coordinates ({self.x}, {self.y})")


test_walk = Robot.specific_coordinate()
test_walk.walk()
