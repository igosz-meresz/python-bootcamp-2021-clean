# -----------------------------------------------------
# ------------**## Creating Classes ##**---------------
# -----------------------------------------------------

# ***********----------- Example 2
class Robot:
    def walk(self):
        print("The robot is walking")


robot = Robot()

robot.walk()

print(type(robot))

# '__main__' is a magic method

# ***********----------- Example 3 ->>>> isinstance()

print(isinstance(robot, Robot))
# true

robot_obj = Robot()

print(isinstance(robot_obj, Robot))
# true
