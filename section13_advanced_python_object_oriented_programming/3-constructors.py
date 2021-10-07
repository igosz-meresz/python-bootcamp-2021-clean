# -----------------------------------------------------
# ----------------**## Constructors ##**---------------
# -----------------------------------------------------

# ***********----------- Example 4

# class Robot:
#     def walk(self):
#         print("The Robot is walking...")

# robot = Robot()
# robot.walk()


# robot = Robot(2.4, 6.5)

# class Robot:
#     def __init__(self, x, y):
#         pass

#     def walk(self):
#         print("The Robot is walking...")


# robot = Robot(2.4, 6.5)

# ***********----------- Example 5

class Robot:
    def __init__(self, x, y):
        # default value
        # self.x = 10

        self.x = x
        self.y = y

    def walk(self):
        print("The Robot is walking...")


robot = Robot(1.3, 11.2)
robot.walk()

print(robot.x)
print(robot.y)

# ***********----------- Example 6


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def walk(self):
        print(f"Walking Coordinates ({self.x}, {self.y})...")


robot = Robot(1.3, 11.2)
robot.walk()
