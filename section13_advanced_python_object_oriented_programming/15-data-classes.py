# ---------------------------------------------------------------------------------
# ----------------------------**## Data Classes ##**-------------------------------
# ---------------------------------------------------------------------------------

# --**--**--**--**--** Example 38 ->>>> issue
from collections import namedtuple


class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


robot1 = Robot(1, 2)
robot2 = Robot(1, 2)

print(robot1 == robot2)
print(id(robot1))
print(id(robot2))


# --**--**--**--**--** Example 39 ->>>> solution 1 -> __eq__
class Robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


robot3 = Robot(1, 2)
robot4 = Robot(1, 2)

print(robot3 == robot4)
print(id(robot3))
print(id(robot4))

# --**--**--**--**--** Example 39 ->>>> solution 2 -> namedtuple()


Robot5 = namedtuple("Robot", ["x", "y"])

robot6 = Robot5(x=1, y=2)
robot7 = Robot5(x=1, y=2)

print(robot6 == robot7)
